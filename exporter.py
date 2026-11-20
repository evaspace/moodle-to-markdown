"""
exporter.py - Écrit un cours Moodle sur disque : Markdown (LaTeX préservé), fichiers, médias, vidéos.

Arborescence produite (compatible batch_convert.py / md_to_cards.py / lecteur /cours/ du site) :
  <sortie>/<Cours>/<NN_Section>/README.md      index de la section
                               /pages/*.md       pages de cours + livres + forums + modules génériques
                               /qcms/*.md        QCM avec corrigés (format lu par md_to_cards.py)
                               /fichiers/...     PDF, polys, dossiers de TD, pièces jointes
                               /medias/...       images / médias embarqués dans les pages (liens locaux)
                               /videos/...       vidéos téléchargées (--download-videos)
  <sortie>/manifest.json                         inventaire machine-lisible de tout ce qui a été trouvé
  <sortie>/RAPPORT_SCRAPING.md                   ce qui a été trouvé, téléchargé, ou a échoué
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import threading
import urllib.parse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from typing import Any, Dict, List, Optional

from bs4 import BeautifulSoup

import moodle_parsers as mp
from md_converter import html_to_markdown, preserve_user_notes, sanitize_filename
from moodle_client import MoodleClient, SessionExpired

QCM_NOTES_MARKER = "## ✍️ Mes Notes / Erreurs à retenir"


class Downloader:
    """File d'attente de téléchargements parallèles, dédupliqués, avec noms sans collision."""

    def __init__(self, client: MoodleClient, workers: int = 4, video_quality: int = 720,
                 youtube_cookies: str = ""):
        self.client = client
        self.youtube_cookies = youtube_cookies
        self._yt_blocked = False
        self.workers = max(1, workers)
        self.video_quality = video_quality
        self._by_url: Dict[str, str] = {}
        self._dests: Dict[str, str] = {}
        self._jobs: List[Dict[str, Any]] = []
        self._aliases: List[tuple] = []
        self.results: List[Dict[str, Any]] = []
        self._lock = threading.Lock()

    def reserve(self, url: str, dest: str) -> str:
        """Réserve un chemin local pour une URL ; la même URL redonne le même chemin."""
        key = url.split("#")[0]
        with self._lock:
            if key in self._by_url:
                if self._by_url[key] != dest:  # même fichier demandé ailleurs : lien créé après téléchargement
                    self._aliases.append((self._by_url[key], dest))
                return self._by_url[key]
            base, ext = os.path.splitext(dest)
            final, n = dest, 2
            while final in self._dests and self._dests[final] != key:
                final = f"{base}_{n}{ext}"
                n += 1
            self._dests[final] = key
            self._by_url[key] = final
            return final

    def queue(self, url: str, dest: str, label: str = "", kind: str = "file") -> str:
        dest = self.reserve(url, dest)
        with self._lock:
            if not any(j["dest"] == dest for j in self._jobs):
                self._jobs.append({"url": url, "dest": dest, "label": label or os.path.basename(dest), "kind": kind})
        return dest

    def _run_one(self, job: Dict[str, Any]) -> Dict[str, Any]:
        if job["kind"] == "ytdlp":
            ok, reason = self._ytdlp(job["url"], job["dest"])
        else:
            ok, reason = self.client.download_file_ex(job["url"], job["dest"])
        return {**job, "ok": ok, "reason": reason}

    def _ytdlp(self, url: str, dest_dir: str) -> tuple:
        marker = os.path.join(dest_dir, f".done_{hashlib.md5(url.encode()).hexdigest()[:10]}")
        if os.path.exists(marker):
            return True, "déjà présent"
        if self._yt_blocked and re.search(r"youtu", url):
            return False, "YouTube exige une connexion (cookies) : non tenté (voir --youtube-cookies)"
        exe = shutil.which("yt-dlp")
        cmd = [exe] if exe else [sys.executable, "-m", "yt_dlp"]
        if not exe:
            try:
                import yt_dlp  # noqa: F401
            except ImportError:
                return False, "yt-dlp non installé (pip install yt-dlp)"
        os.makedirs(dest_dir, exist_ok=True)
        fmt = f"bv*[height<={self.video_quality}]+ba/b[height<={self.video_quality}]/b"
        if self.youtube_cookies:
            cmd += ["--cookies", self.youtube_cookies, "--js-runtimes", "node"]
        cmd += ["--no-playlist", "--no-progress", "--restrict-filenames", "-f", fmt, "--merge-output-format", "mp4",
                "-o", os.path.join(dest_dir, "%(title).80s.%(ext)s"), url]
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=3600)
        except subprocess.TimeoutExpired:
            return False, "yt-dlp : délai dépassé"
        if r.returncode != 0:
            if "Sign in to confirm" in r.stderr:
                self._yt_blocked = True
            return False, "yt-dlp : " + (r.stderr.strip().splitlines() or ["échec"])[-1][:200]
        open(marker, "w").close()
        return True, "téléchargée"

    def run(self) -> List[Dict[str, Any]]:
        """Exécute la file. Les SessionExpired des workers sont relevées après coup."""
        jobs, self._jobs = self._jobs, []
        expired: Optional[SessionExpired] = None
        done: List[Dict[str, Any]] = []

        def safe(job: Dict[str, Any]) -> Dict[str, Any]:
            nonlocal expired
            if expired:
                return {**job, "ok": False, "reason": "interrompu (session expirée)"}
            try:
                return self._run_one(job)
            except SessionExpired as e:
                expired = e
                return {**job, "ok": False, "reason": "session expirée"}

        with ThreadPoolExecutor(max_workers=self.workers) as pool:
            done = list(pool.map(safe, jobs))
        self.results += done
        aliases, self._aliases = self._aliases, []
        for src, alias in aliases:
            if os.path.exists(src) and not os.path.exists(alias):
                os.makedirs(os.path.dirname(alias), exist_ok=True)
                try:
                    os.link(src, alias)
                except OSError:
                    shutil.copy2(src, alias)
        if expired:
            raise expired
        return done


class CourseExporter:
    def __init__(
        self,
        client: MoodleClient,
        output_dir: str = "EPITA_Moodle_Notes",
        download_files: bool = True,
        download_videos: bool = False,
        state_file: str = "state.json",
        workers: int = 4,
        video_quality: int = 720,
        youtube_cookies: str = "",
    ):
        self.client = client
        self.output_dir = output_dir
        self.download_files = download_files
        self.download_videos = download_videos
        self.state_file = state_file
        self.state = self._load_state()
        self.dl = Downloader(client, workers, video_quality, youtube_cookies)
        self.manifest: List[Dict[str, Any]] = []
        self.failures: List[Dict[str, str]] = []

    # ------------------------------------------------------------------ état
    def _load_state(self) -> Dict[str, Any]:
        if os.path.exists(self.state_file):
            try:
                with open(self.state_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}

    def _save_state(self) -> None:
        try:
            tmp = self.state_file + ".tmp"
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(self.state, f, indent=2, ensure_ascii=False)
            os.replace(tmp, self.state_file)
        except Exception as e:
            print(f"⚠️ Erreur sauvegarde state.json : {e}")

    # ------------------------------------------------------------- utilitaires
    def _md(self, html: str) -> str:
        return html_to_markdown(html, self.client.base_url) if html else ""

    def _write(self, path: str, content: str) -> None:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

    def _rel(self, from_file: str, to_path: str) -> str:
        rel = os.path.relpath(to_path, os.path.dirname(from_file)).replace(os.sep, "/")
        return urllib.parse.quote(rel, safe="/._-~")

    def _log(self, course: str, section: str, kind: str, name: str, url: str = "", local: str = "",
             status: str = "ok") -> None:
        self.manifest.append({"course": course, "section": section, "type": kind, "name": name,
                              "url": url, "local": local, "status": status})

    def _fetch(self, url: str, dest: str, label: str, need: bool = True) -> str:
        """Programme le téléchargement d'un fichier ; renvoie le chemin local (même si pas encore là)."""
        if not self.download_files or not need:
            return dest
        return self.dl.queue(url, dest, label)

    def _unique_name(self, name: str, used: set, default: str = "fichier") -> str:
        name = sanitize_filename(name) or default
        base, ext = os.path.splitext(name)
        cand, n = name, 2
        while cand.lower() in used:
            cand = f"{base}_{n}{ext}"
            n += 1
        used.add(cand.lower())
        return cand

    def _localize_html(self, html: str, md_file: str, medias_dir: str, label: str) -> str:
        """Télécharge les médias/pièces jointes embarqués et réécrit leurs liens en chemins locaux."""
        if not html:
            return html
        emb = mp.find_embedded(html, self.client.base_url)
        if not emb["assets"] or not self.download_files:
            return html
        mapping: Dict[str, str] = {}
        used: set = set()
        for a in emb["assets"]:
            if a["kind"] == "video" and not self.download_videos:
                continue
            name = self._unique_name(a["filename"] or "media", used)
            dest = self.dl.queue(a["url"], os.path.join(medias_dir, name), f"{label}/{name}")
            mapping[a["url"].split("?")[0]] = self._rel(md_file, dest)
        soup = BeautifulSoup(html, "html.parser")
        for tag in soup.find_all(["img", "source", "video", "audio", "a", "object", "embed", "iframe"]):
            att = {"a": "href", "object": "data"}.get(tag.name, "src")
            val = mp.attr(tag, att)
            if not val:
                continue
            key = mp.absolutize(self.client.base_url, val).split("?")[0]
            if key in mapping:
                tag[att] = mapping[key]
        return str(soup)

    def _add_videos(self, videos: List[Dict[str, str]], out: List[Dict[str, Any]], vdir: str,
                    md_file: str = "") -> None:
        """Enregistre les vidéos trouvées (liens) et télécharge si demandé."""
        seen = {v["url"] for v in out}
        for v in videos:
            if v["url"] in seen:
                continue
            seen.add(v["url"])
            entry: Dict[str, Any] = {"name": v.get("title") or mp.filename_from_url(v["url"]), "url": v["url"],
                                     "local": ""}
            if self.download_videos and self.download_files:
                if v.get("local"):
                    dest = self.dl.queue(v["url"], os.path.join(vdir, sanitize_filename(
                        mp.filename_from_url(v["url"]))), entry["name"])
                else:
                    dest = self.dl.queue(v["url"], vdir, entry["name"], kind="ytdlp")
                entry["local"] = dest
            out.append(entry)

    # ------------------------------------------------------------------ cours
    def export_course(self, course_data: Dict[str, Any]) -> Dict[str, int]:
        c_name = course_data.get("fullname") or f"Cours_{course_data.get('id', 0)}"
        course_dir = os.path.join(self.output_dir, sanitize_filename(c_name))
        os.makedirs(course_dir, exist_ok=True)
        stats = {"sections": 0, "files": 0, "pages": 0, "qcms": 0, "videos": 0, "folders": 0,
                 "books": 0, "forums": 0, "others": 0, "questions": 0, "failed": 0}
        sections_toc: List[Dict[str, Any]] = []
        fail_start = len(self.dl.results)

        for sec in course_data.get("sections", []):
            s_num = sec.get("section_number", 0)
            sec_name = sec.get("name", "").strip() or f"Section {s_num}"
            safe_sec = f"{s_num:02d}_{sanitize_filename(sec_name)}"
            sec_dir = os.path.join(course_dir, safe_sec)
            os.makedirs(sec_dir, exist_ok=True)
            stats["sections"] += 1
            cat = self._export_section(c_name, sec_name, sec_dir, sec, stats)

            sec_readme = os.path.join(sec_dir, "README.md")
            summary_html = self._localize_html(sec.get("summary_html", ""), sec_readme,
                                               os.path.join(sec_dir, "medias"), "résumé")
            content = self._build_section_readme(sec_name, self._md(summary_html), cat)
            if os.path.exists(sec_readme):
                with open(sec_readme, "r", encoding="utf-8") as f:
                    content = preserve_user_notes(f.read(), content)
            self._write(sec_readme, content)
            sections_toc.append({
                "title": sec_name, "rel_dir": safe_sec, "readme_path": f"./{urllib.parse.quote(safe_sec)}/README.md",
                "counts": {"pages": len(cat["pages"]), "qcms": len(cat["qcms"]), "videos": len(cat["videos"]),
                           "files": len(cat["resources"]) + sum(len(f["files"]) for f in cat["folders"])}})

        # exécute les téléchargements du cours (parallèle) puis consigne les échecs
        try:
            self.dl.run()
        finally:
            new = self.dl.results[fail_start:]
            stats["files"] = sum(1 for r in new if r["ok"] and r["kind"] == "file")
            for r in new:
                if not r["ok"]:
                    stats["failed"] += 1
                    self.failures.append({"course": c_name, "name": r["label"], "url": r["url"], "reason": r["reason"]})
            bad = {r["dest"] for r in new if not r["ok"]}
            for m in self.manifest:
                if m["local"] in bad:
                    m["status"] = "échec téléchargement"

        self._write(os.path.join(course_dir, "README.md"), self._build_course_readme(
            c_name, course_data.get("url", ""), self._md(course_data.get("summary", "")), sections_toc, stats))
        return stats

    def _export_section(self, c_name: str, sec_name: str, sec_dir: str, sec: Dict[str, Any],
                        stats: Dict[str, int]) -> Dict[str, List[Any]]:
        files_dir = os.path.join(sec_dir, "fichiers")
        pages_dir = os.path.join(sec_dir, "pages")
        qcms_dir = os.path.join(sec_dir, "qcms")
        medias_dir = os.path.join(sec_dir, "medias")
        videos_dir = os.path.join(sec_dir, "videos")
        cat: Dict[str, List[Any]] = {k: [] for k in
                                     ("pages", "videos", "qcms", "resources", "folders", "assigns", "labels", "others")}
        used_files: set = set()
        p_idx = q_idx = 1

        for mod in sec.get("modules", []):
            m_type, m_name = mod.get("type", ""), (mod.get("name") or "").strip()
            extra = mod.get("extra", {})
            m_url = mod.get("url", "")
            desc_md = self._md(mod.get("description", ""))
            note = " *(restreint — non accessible avec ce compte)*" if mod.get("restricted") else ""
            # vidéos / assets trouvés dans la description du module
            self._add_videos(extra.get("embedded_videos", []), cat["videos"], videos_dir)
            for a in extra.get("embedded_assets", []):
                if a["kind"] == "video":
                    continue
                nm = self._unique_name(a["filename"], used_files)
                loc = self._fetch(a["url"], os.path.join(files_dir, nm), nm)
                cat["resources"].append({"name": nm, "filename": nm, "path": f"./fichiers/{urllib.parse.quote(nm)}",
                                         "desc": ""})
                self._log(c_name, sec_name, "annexe", nm, a["url"], loc)

            if m_type == "page":
                page_file = os.path.join(pages_dir, f"{p_idx:02d}_{sanitize_filename(m_name)}.md")
                pc = extra.get("page_content", {})
                html = self._localize_html(pc.get("content_html", ""), page_file, medias_dir, m_name)
                self._add_videos(pc.get("videos", []), cat["videos"], videos_dir)
                text = f"# {m_name}\n\n> **Lien Moodle :** [{m_url}]({m_url})\n\n"
                if desc_md:
                    text += f"## Description\n{desc_md}\n\n"
                text += f"## Contenu du cours\n\n{self._md(html)}\n"
                if pc.get("videos"):
                    text += "\n## Vidéos de la page\n" + "".join(f"- [{v['title'] or v['url']}]({v['url']})\n"
                                                                  for v in pc["videos"])
                self._write(page_file, text)
                stats["pages"] += 1
                cat["pages"].append({"name": m_name, "path": "./pages/" + urllib.parse.quote(os.path.basename(page_file)), "desc": desc_md})
                self._log(c_name, sec_name, "page", m_name, m_url, page_file)
                p_idx += 1

            elif m_type == "book":
                chapters = extra.get("book", {}).get("chapters", [])
                book_file = os.path.join(pages_dir, f"{p_idx:02d}_{sanitize_filename(m_name)}.md")
                text = f"# {m_name}\n\n> **Lien Moodle :** [{m_url}]({m_url})\n\n"
                if desc_md:
                    text += f"{desc_md}\n\n"
                for ch in chapters:
                    html = self._localize_html(ch["content_html"], book_file, medias_dir, m_name)
                    self._add_videos(ch.get("videos", []), cat["videos"], videos_dir)
                    text += f"## {ch['title'] or 'Chapitre'}\n\n{self._md(html)}\n\n"
                self._write(book_file, text)
                stats["books"] += 1
                stats["pages"] += 1
                cat["pages"].append({"name": f"{m_name} (livre, {len(chapters)} chapitres)",
                                     "path": "./pages/" + urllib.parse.quote(os.path.basename(book_file)), "desc": desc_md})
                self._log(c_name, sec_name, "livre", m_name, m_url, book_file)
                p_idx += 1

            elif m_type == "forum":
                discussions = extra.get("forum", {}).get("discussions", [])
                if discussions:
                    forum_file = os.path.join(pages_dir, f"{p_idx:02d}_{sanitize_filename(m_name)}.md")
                    text = f"# {m_name}\n\n> **Lien Moodle :** [{m_url}]({m_url})\n\n"
                    for d in discussions:
                        text += f"## {d['title']}\n\n> [{d['url']}]({d['url']})\n\n"
                        for post in d["posts"][:20]:
                            html = self._localize_html(post["html"], forum_file, medias_dir, m_name)
                            text += f"{self._md(html)}\n\n"
                        for a in d.get("assets", []):
                            if a["kind"] == "image" and "/mod_forum/" not in a["url"]:
                                continue
                            nm = self._unique_name(a["filename"], used_files)
                            loc = self._fetch(a["url"], os.path.join(files_dir, nm), nm)
                            text += f"- 📎 [{nm}]({self._rel(forum_file, loc)})\n"
                            self._log(c_name, sec_name, "pièce jointe forum", nm, a["url"], loc)
                        self._add_videos(d.get("videos", []), cat["videos"], videos_dir)
                    self._write(forum_file, text)
                    stats["forums"] += 1
                    cat["pages"].append({"name": f"{m_name} (forum, {len(discussions)} sujets)",
                                         "path": "./pages/" + urllib.parse.quote(os.path.basename(forum_file)), "desc": desc_md})
                    self._log(c_name, sec_name, "forum", m_name, m_url, forum_file)
                    p_idx += 1

            elif m_type == "url":
                target = extra.get("target_url") or m_url
                is_video = bool(mp.VIDEO_HOST_RE.search(target) or mp.VIDEO_EXT_RE.search(target))
                stats["videos"] += 1
                entry = {"name": m_name, "url": target, "desc": desc_md, "local": ""}
                if is_video:
                    tmp: List[Dict[str, Any]] = []
                    self._add_videos([{"url": target, "title": m_name, "local": ""}], tmp, videos_dir)
                    entry["local"] = tmp[0]["local"] if tmp else ""
                cat["videos"].append(entry)
                self._log(c_name, sec_name, "vidéo/lien" if is_video else "lien", m_name, target, entry["local"])

            elif m_type == "quiz":
                q_file = os.path.join(qcms_dir, f"{q_idx:02d}_{sanitize_filename(m_name)}.md")
                qd = extra.get("quiz_details", {})
                text = self._quiz_markdown(m_name, m_url, qd)
                if os.path.exists(q_file):
                    with open(q_file, "r", encoding="utf-8") as f:
                        text = preserve_user_notes(f.read(), text, marker=QCM_NOTES_MARKER)
                self._write(q_file, text)
                stats["qcms"] += 1
                stats["questions"] += len(qd.get("questions", []))
                cat["qcms"].append({"name": m_name, "path": "./qcms/" + urllib.parse.quote(os.path.basename(q_file)), "desc": desc_md,
                                    "has_questions": bool(qd.get("questions"))})
                self._log(c_name, sec_name, "qcm", m_name, m_url, q_file,
                          "ok" if qd.get("questions") else "consignes seulement (aucune relecture disponible)")
                q_idx += 1

            elif m_type == "resource":
                got = False
                for f in mod.get("contents", []):
                    if not f.get("fileurl"):
                        continue
                    got = True
                    nm = self._unique_name(f.get("filename") or "document", used_files)
                    loc = self._fetch(f["fileurl"], os.path.join(files_dir, nm), nm)
                    if mp.VIDEO_EXT_RE.search(nm) and not self.download_videos:
                        cat["videos"].append({"name": m_name or nm, "url": f["fileurl"], "desc": desc_md, "local": ""})
                        stats["videos"] += 1
                        self._log(c_name, sec_name, "vidéo", nm, f["fileurl"], "", "non téléchargée (--download-videos)")
                        continue
                    cat["resources"].append({"name": m_name or nm, "filename": nm,
                                             "path": f"./fichiers/{urllib.parse.quote(nm)}", "desc": desc_md})
                    self._log(c_name, sec_name, "fichier", nm, f["fileurl"], loc)
                if not got:
                    self._log(c_name, sec_name, "fichier", m_name, m_url, "", "introuvable (restreint ?)")
                    cat["others"].append({"name": f"{m_name}{note or ' *(fichier introuvable)*'}", "path": m_url,
                                          "desc": desc_md})

            elif m_type == "folder":
                subfiles = []
                fname = sanitize_filename(m_name)
                raw = extra.get("folder_files") or mod.get("contents", [])
                for sf in raw:
                    if not (sf.get("filename") and sf.get("fileurl")):
                        continue
                    sub = "/".join(sanitize_filename(p) for p in
                                   (sf.get("subpath") or sf.get("filepath") or "").strip("/").split("/") if p)
                    nm = sanitize_filename(sf["filename"])
                    dest = os.path.join(files_dir, fname, *([sub] if sub else []), nm)
                    loc = self._fetch(sf["fileurl"], dest, nm)
                    rel = os.path.relpath(loc, sec_dir).replace(os.sep, "/")
                    subfiles.append({"name": (sub + "/" if sub else "") + nm, "path": "./" + urllib.parse.quote(rel)})
                    self._log(c_name, sec_name, "fichier (dossier)", nm, sf["fileurl"], loc)
                stats["folders"] += 1
                cat["folders"].append({"name": m_name, "desc": desc_md, "files": subfiles})

            elif m_type == "assign":
                ad = extra.get("assign_details", {})
                a_files = []
                for af in ad.get("files", []):
                    nm = self._unique_name(af.get("filename", "sujet.pdf"), used_files)
                    loc = self._fetch(af["fileurl"], os.path.join(files_dir, nm), nm)
                    a_files.append({"name": nm, "path": f"./fichiers/{urllib.parse.quote(nm)}"})
                    self._log(c_name, sec_name, "sujet de devoir", nm, af["fileurl"], loc)
                cat["assigns"].append({"name": m_name, "url": m_url,
                                       "desc": self._md(ad.get("intro_html", "")) or desc_md,
                                       "due_date": ad.get("due_date", ""), "files": a_files})

            elif m_type == "label":
                if desc_md:
                    html = self._localize_html(mod.get("description", ""), os.path.join(sec_dir, "README.md"),
                                               medias_dir, "label")
                    cat["labels"].append(self._md(html))

            elif m_type in ("hvp", "h5pactivity"):  # vidéos interactives H5P : lien(s) + textes + questions
                items = extra.get("h5p", [])
                page_file = os.path.join(pages_dir, f"{p_idx:02d}_{sanitize_filename(m_name)}.md")
                text = f"# {m_name}\n\n- **Type Moodle :** H5P\n- **Lien :** [{m_url}]({m_url})\n\n"
                if desc_md:
                    text += f"{desc_md}\n\n"
                for it in items:
                    vids = [{**v, "title": m_name} for v in it["videos"]]
                    stats["videos"] += len(vids)
                    self._add_videos(vids, cat["videos"], videos_dir)
                    for v in it["videos"]:
                        text += f"## Vidéo\n\n- 🎬 [{m_name}]({v['url']})\n\n"
                        self._log(c_name, sec_name, "vidéo H5P", m_name, v["url"], "")
                    for t in it["texts"]:
                        text += f"{t}\n\n"
                    for qn in it["questions"]:
                        text += f"### Question\n{qn['question']}\n\n"
                        for a in qn.get("answers", []):
                            text += f"- [{'x' if a['correct'] else ' '}] {a['text']}\n"
                        if qn["type"] == "truefalse":
                            text += f"- Réponse : {'Vrai' if qn['correct'] else 'Faux'}\n"
                        text += "\n"
                if items:
                    self._write(page_file, text)
                    stats["others"] += 1
                    cat["pages"].append({"name": f"{m_name} (vidéo)", "path": "./pages/" + urllib.parse.quote(os.path.basename(page_file)),
                                         "desc": desc_md})
                    p_idx += 1
                else:
                    self._log(c_name, sec_name, "hvp", m_name, m_url, "", "contenu H5P introuvable")

            else:  # leçon, glossaire, wiki, SCORM, module inconnu... : contenu + pièces jointes
                gen = extra.get("generic", {})
                page_file = os.path.join(pages_dir, f"{p_idx:02d}_{sanitize_filename(m_name or m_type)}.md")
                for f in mod.get("contents", []):
                    if f.get("fileurl"):
                        nm = self._unique_name(f.get("filename", "fichier"), used_files)
                        loc = self._fetch(f["fileurl"], os.path.join(files_dir, nm), nm)
                        cat["resources"].append({"name": m_name or nm, "filename": nm,
                                                 "path": f"./fichiers/{urllib.parse.quote(nm)}", "desc": desc_md})
                        self._log(c_name, sec_name, m_type or "fichier", nm, f["fileurl"], loc)
                if gen.get("content_html") or desc_md:
                    html = self._localize_html(gen.get("content_html", ""), page_file, medias_dir, m_name)
                    for a in gen.get("assets", []):
                        if a["kind"] != "image":
                            nm = self._unique_name(a["filename"], used_files)
                            loc = self._fetch(a["url"], os.path.join(files_dir, nm), nm)
                            cat["resources"].append({"name": nm, "filename": nm,
                                                     "path": f"./fichiers/{urllib.parse.quote(nm)}", "desc": ""})
                            self._log(c_name, sec_name, "annexe", nm, a["url"], loc)
                    self._add_videos(gen.get("videos", []), cat["videos"], videos_dir)
                    text = f"# {m_name}\n\n- **Type Moodle :** {m_type}\n- **Lien :** [{m_url}]({m_url})\n\n"
                    if desc_md:
                        text += f"{desc_md}\n\n"
                    text += self._md(html) + "\n"
                    self._write(page_file, text)
                    stats["others"] += 1
                    cat["others"].append({"name": f"{m_name} ({m_type})",
                                          "path": "./pages/" + urllib.parse.quote(os.path.basename(page_file)), "desc": desc_md})
                    p_idx += 1
                elif m_url:
                    cat["others"].append({"name": f"{m_name} ({m_type}){note}", "path": m_url, "desc": desc_md})
                self._log(c_name, sec_name, m_type or "module", m_name, m_url, page_file if gen else "")

        return cat

    # ------------------------------------------------------------------- QCM
    def _quiz_markdown(self, name: str, url: str, qd: Dict[str, Any]) -> str:
        """Markdown d'un QCM. `[x]` = case cochée par l'élève ; la section « Réponses correctes »
        (nouvelle) donne la vraie correction, lue par md_to_cards.py même si la note n'est pas pleine."""
        text = f"# {name}\n\n- **Type :** Test / QCM Moodle\n- **Lien Moodle :** [{url}]({url})\n"
        if qd.get("attempts"):
            text += f"- **Tentatives relues :** {qd['attempts']}\n"
        if qd.get("rules"):
            text += "- **Règles & Paramètres :**\n" + "".join(f"  - {r}\n" for r in qd["rules"])
        text += "\n---\n\n"
        intro = self._md(qd.get("intro_html", ""))
        if intro:
            text += f"## 📋 Consignes & Présentation\n{intro}\n\n---\n\n"
        questions = qd.get("questions", [])
        if questions:
            text += "## 📝 Questions & Corrigé de la tentative\n\n"
            for i, q in enumerate(questions, 1):
                num = re.search(r"\d+", q.get("number", ""))
                n = num.group(0) if num else str(i)
                grade = q.get("grade", "")
                text += f"### Question {n} ({grade})\n" if grade else f"### Question {n}\n"
                text += f"{self._md(q.get('question_html', ''))}\n\n"
                answers = q.get("answers", [])
                if answers:
                    text += "**Options / Réponses :**\n"
                    for a in answers:
                        text += f"- [{'x' if a.get('checked') else ' '}] {a['text']}\n"
                    text += "\n"
                    good = [a["text"] for a in answers if a.get("correct")]
                    if good and q.get("type", "unknown") in ("multichoice", "truefalse", "unknown"):
                        text += "**Réponses correctes :**\n" + "".join(f"- ✔ {g}\n" for g in good) + "\n"
                fb = []
                if q.get("right_answer"):
                    fb.append(q["right_answer"])
                if q.get("feedback_html"):
                    fb.append(self._md(q["feedback_html"]))
                if q.get("state"):
                    fb.append(f"Résultat : {q['state']}")
                if fb:
                    body = "\n\n".join(fb).replace("\n", "\n> ")
                    text += f"> **Correction / Feedback :**\n> {body}\n\n"
        text += f"{QCM_NOTES_MARKER}\n<!-- Notez vos réflexions ou erreurs ici -->\n"
        return text

    # --------------------------------------------------------------- README
    def _build_section_readme(self, sec_name: str, sec_summary_md: str, c: Dict[str, List[Any]]) -> str:
        t = f"# {sec_name}\n\n"
        if sec_summary_md:
            t += f"## 📖 Présentation du chapitre\n\n{sec_summary_md}\n\n"
        for lbl in c["labels"]:
            t += f"{lbl}\n\n"

        def quote(d: str) -> str:
            return "".join(f"  > {ln}\n" for ln in d.splitlines()[:30] if ln.strip())

        if c["pages"]:
            t += "## 📄 Pages de cours\n"
            for p in c["pages"]:
                t += f"- 📄 [**{p['name']}**]({p['path']})\n" + (quote(p["desc"]) if p["desc"] else "")
            t += "\n"
        if c["videos"]:
            t += "## 🎬 Vidéos & Liens interactifs\n"
            for v in c["videos"]:
                t += f"- 🎬 [**{v['name']}**]({v['url']})"
                if v.get("local"):
                    t += " *(téléchargée dans `videos/`)*"
                t += "\n" + (quote(v["desc"]) if v.get("desc") else "")
            t += "\n"
        if c["qcms"]:
            t += "## 📝 Tests & QCM\n"
            for q in c["qcms"]:
                badge = "*(Corrigé inclus)*" if q["has_questions"] else "*(Consignes & lien)*"
                t += f"- 📝 [**{q['name']}**]({q['path']}) {badge}\n" + (quote(q["desc"]) if q["desc"] else "")
            t += "\n"
        if c["resources"]:
            t += "## 📎 Documents & Fichiers de travail\n"
            for r in c["resources"]:
                t += f"- 📎 [**{r['name']}**]({r['path']}) *({r['filename']})*\n" + (quote(r["desc"]) if r["desc"] else "")
            t += "\n"
        if c["folders"]:
            t += "## 📁 Dossiers (Feuilles de TD & Séminaires)\n"
            for fold in c["folders"]:
                t += f"### 📁 {fold['name']}\n" + (f"> {fold['desc']}\n\n" if fold["desc"] else "")
                t += "".join(f"- 📄 [{sf['name']}]({sf['path']})\n" for sf in fold["files"]) or \
                    "*(Dossier vide ou fichiers non détectés)*\n"
                t += "\n"
        if c["others"]:
            t += "## 🧩 Autres activités\n"
            for o in c["others"]:
                t += f"- 🧩 [**{o['name']}**]({o['path']})\n" + (quote(o["desc"]) if o["desc"] else "")
            t += "\n"
        if c["assigns"]:
            t += "## 📬 Devoirs maisons & Travaux à rendre\n"
            for a in c["assigns"]:
                t += f"### 📬 [{a['name']}]({a['url']})\n"
                if a["due_date"]:
                    t += f"- **Date limite :** {a['due_date']}\n"
                if a["desc"]:
                    t += f"> {a['desc']}\n\n"
                if a["files"]:
                    t += "**Fichiers joints au sujet :**\n" + "".join(f"- 📎 [{f['name']}]({f['path']})\n" for f in a["files"])
                t += "\n"
        t += ("---\n\n## ✍️ Mes Notes Personnelles\n<!-- Écris tes formules, résumés et remarques ici. "
              "Cette section est préservée lors des prochaines synchronisations. -->\n\n")
        return t

    def _build_course_readme(self, c_name: str, c_url: str, c_summary: str,
                             sections_toc: List[Dict[str, Any]], stats: Dict[str, int]) -> str:
        now = datetime.now().strftime("%d/%m/%Y %H:%M")
        t = f"# 📚 {c_name}\n\n> **Dernière synchronisation :** {now}  \n> **Lien Moodle :** [{c_url}]({c_url})\n\n"
        if c_summary:
            t += f"## 📋 Présentation du cours\n\n{c_summary}\n\n"
        t += "## 🗂️ Sommaire des chapitres & sections\n\n"
        for s in sections_toc:
            cnt = s["counts"]
            parts = [f"{cnt['pages']} page(s)" if cnt["pages"] else "", f"{cnt['qcms']} QCM" if cnt["qcms"] else "",
                     f"{cnt['videos']} vidéo(s)" if cnt["videos"] else "",
                     f"{cnt['files']} document(s)" if cnt["files"] else ""]
            detail = f" *({', '.join(p for p in parts if p)})*" if any(parts) else ""
            t += f"- 📂 [**{s['title']}**]({s['readme_path']}){detail}\n"
        t += "\n---\n\n## 📊 Statistiques du cours\n\n"
        t += f"- **Chapitres / Sections :** {stats['sections']}\n- **Pages de cours (dont livres) :** {stats['pages']}\n"
        t += f"- **Tests et QCM répertoriés :** {stats['qcms']} ({stats['questions']} questions)\n"
        t += f"- **Vidéos & Liens :** {stats['videos']}\n- **Documents téléchargés :** {stats['files']}\n"
        if stats.get("failed"):
            t += f"- **Téléchargements en échec :** {stats['failed']} (voir RAPPORT_SCRAPING.md)\n"
        return t + "\n"

    def build_global_index(self, courses_list: List[Dict[str, Any]], all_stats: Dict[str, Dict[str, int]]) -> None:
        os.makedirs(self.output_dir, exist_ok=True)
        now = datetime.now().strftime("%d/%m/%Y %H:%M")
        t = ("# 🎓 EPITA — Notes & Cours Moodle\n\n"
             f"> **Index centralisé des cours synchronisés hors-ligne**  \n> **Dernière mise à jour :** {now}\n\n"
             "## 📚 Vos Cours\n\n")
        tot = {k: 0 for k in ("sections", "pages", "qcms", "videos", "files", "questions")}
        for c in courses_list:
            st = all_stats.get(str(c.get("id")), {})
            for k in tot:
                tot[k] += st.get(k, 0)
            name = c.get("fullname", f"Cours {c.get('id')}")
            t += (f"- 📖 [**{name}**](./{urllib.parse.quote(sanitize_filename(name))}/README.md) — "
                  f"*{st.get('sections', 0)} sections, {st.get('pages', 0)} pages, {st.get('files', 0)} docs, "
                  f"{st.get('qcms', 0)} QCM*\n")
        t += (f"\n---\n\n## 📈 Vue d'ensemble globale\n\n- **Nombre total de cours :** {len(courses_list)}\n"
              f"- **Sections / chapitres :** {tot['sections']}\n- **Pages de cours :** {tot['pages']}\n"
              f"- **QCM & Tests :** {tot['qcms']} ({tot['questions']} questions)\n- **Vidéos & liens :** {tot['videos']}\n"
              f"- **Documents téléchargés :** {tot['files']}\n")
        self._write(os.path.join(self.output_dir, "README.md"), t)

    # -------------------------------------------------------- manifeste / rapport
    def write_report(self, courses: List[Dict[str, Any]], all_stats: Dict[str, Dict[str, int]]) -> str:
        """Écrit manifest.json et RAPPORT_SCRAPING.md ; renvoie le chemin du rapport."""
        os.makedirs(self.output_dir, exist_ok=True)
        with open(os.path.join(self.output_dir, "manifest.json"), "w", encoding="utf-8") as f:
            json.dump(self.manifest, f, ensure_ascii=False, indent=1)
        by_type: Dict[str, int] = {}
        for m in self.manifest:
            by_type[m["type"]] = by_type.get(m["type"], 0) + 1
        problems = [m for m in self.manifest if m["status"] != "ok"]
        t = f"# Rapport de scraping — {datetime.now().strftime('%d/%m/%Y %H:%M')}\n\n"
        t += f"- Cours traités : {len(courses)}\n- Éléments inventoriés : {len(self.manifest)}\n"
        t += "".join(f"  - {k} : {v}\n" for k, v in sorted(by_type.items(), key=lambda kv: -kv[1]))
        t += f"- Téléchargements en échec : {len(self.failures)}\n- Éléments à vérifier : {len(problems)}\n"
        t += f"- Incidents réseau/parsing : {len(self.client.errors)}\n\n"
        if self.failures:
            t += "## Téléchargements en échec\n\n" + "".join(
                f"- **{x['course']}** — {x['name']} : {x['reason']} ({x['url']})\n" for x in self.failures) + "\n"
        if problems:
            t += "## Éléments à vérifier (restreints, vides, non téléchargés)\n\n" + "".join(
                f"- **{m['course']} / {m['section']}** — {m['type']} « {m['name']} » : {m['status']}\n"
                for m in problems[:300]) + "\n"
        if self.client.errors:
            t += "## Incidents\n\n" + "".join(f"- {e['where']} : {e['error']}\n" for e in self.client.errors[:200])
        path = os.path.join(self.output_dir, "RAPPORT_SCRAPING.md")
        self._write(path, t)
        return path
