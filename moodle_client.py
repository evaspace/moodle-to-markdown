"""
moodle_client.py - Client Moodle (EPITA) : API REST (wstoken) ou session web (cookie MoodleSession).

Couche réseau uniquement ; tout le parsing HTML est dans moodle_parsers.py (testé hors ligne).
Points clés :
  * retries + backoff sur 429/5xx/erreurs réseau, délai minimal entre requêtes (poli pour le serveur)
  * SessionExpired levée dès qu'une réponse est la page de connexion (jamais de page de login
    enregistrée à la place d'un PDF) ; main.py sauvegarde alors l'état pour reprendre
  * liste des cours via l'AJAX interne de Moodle (le tableau de bord /my/ est rendu en JS)
  * tous les types de modules : fichier, dossier, page, livre, URL/vidéo, QCM (toutes les
    tentatives, bonnes réponses), devoir, forum (pièces jointes), H5P/leçon/glossaire/etc.
  * médias et pièces jointes embarqués (images, PDF, vidéos) inventoriés pour téléchargement
"""

from __future__ import annotations

from html import unescape as _unescape
from html import unescape as html_unescape
import json
import os
import re
import threading
import time
import urllib.parse
from typing import Any, Dict, List, Optional, Tuple

import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter

import moodle_parsers as mp


class SessionExpired(RuntimeError):
    """Le cookie MoodleSession n'est plus valide (redirection vers la page de connexion)."""


class MoodleClient:
    def __init__(
        self,
        base_url: str = "https://moodle.epita.fr",
        token: Optional[str] = None,
        session_cookie: Optional[str] = None,
        min_delay: float = 0.15,
        verbose: bool = False,
    ):
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.session_cookie = (session_cookie or "").strip() or None
        self.min_delay = min_delay
        self.verbose = verbose
        self.session = requests.Session()
        adapter = HTTPAdapter(pool_connections=8, pool_maxsize=16)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)
        self.session.headers.update({
            "User-Agent": ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                           "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"),
            "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
        })
        self._set_cookie()
        self.user_info: Dict[str, Any] = {}
        self.auth_mode: str = "none"  # "token", "cookie" ou "none"
        self.sesskey = ""
        self.errors: List[Dict[str, str]] = []  # incidents non bloquants, repris dans le rapport
        self._lock = threading.Lock()
        self._last_request = 0.0

    # ------------------------------------------------------------------ réseau
    def _set_cookie(self) -> None:
        if self.session_cookie:
            value = self.session_cookie
            if value.lower().startswith("moodlesession="):
                value = value.split("=", 1)[1]
            self.session.cookies.set("MoodleSession", value.strip().rstrip(";"),
                                     domain=urllib.parse.urlparse(self.base_url).hostname)

    def _throttle(self) -> None:
        with self._lock:
            wait = self.min_delay - (time.monotonic() - self._last_request)
            if wait > 0:
                time.sleep(wait)
            self._last_request = time.monotonic()

    def _request(self, method: str, url: str, retries: int = 4, **kw: Any) -> requests.Response:
        kw.setdefault("timeout", 40)
        last_exc: Optional[Exception] = None
        for attempt in range(retries):
            self._throttle()
            try:
                resp = self.session.request(method, url, **kw)
                if resp.status_code in (429, 502, 503, 504):
                    wait = float(resp.headers.get("Retry-After", 0) or 0) or 2 ** (attempt + 1)
                    if self.verbose:
                        print(f"   ⏳ HTTP {resp.status_code} sur {url[:80]}, nouvelle tentative dans {wait:.0f}s")
                    resp.close()
                    time.sleep(min(wait, 60))
                    continue
                return resp
            except (requests.ConnectionError, requests.Timeout, requests.exceptions.ChunkedEncodingError) as e:
                last_exc = e
                time.sleep(2 ** attempt)
        raise requests.ConnectionError(f"{url} injoignable après {retries} essais : {last_exc}")

    def get_html(self, url: str, **kw: Any) -> Tuple[str, str]:
        """GET d'une page HTML. Lève SessionExpired si on est renvoyé vers la connexion."""
        resp = self._request("GET", url, **kw)
        text = resp.text
        if self.auth_mode == "cookie" and mp.is_login_page(text, resp.url):
            raise SessionExpired(f"Session Moodle expirée en visitant {url}")
        return text, resp.url

    def note_error(self, where: str, what: Exception | str) -> None:
        self.errors.append({"where": where, "error": str(what)})
        if self.verbose:
            print(f"   ⚠️ {where} : {what}")

    # ---------------------------------------------------------- authentification
    def authenticate_with_credentials(self, username: str, password: str) -> bool:
        """Tente d'obtenir un token WebService via login/token.php (rarement actif avec le SSO)."""
        try:
            resp = self._request("GET", f"{self.base_url}/login/token.php", retries=1, timeout=15,
                                 params={"username": username, "password": password,
                                         "service": "moodle_mobile_app"})
            data = resp.json()
            if "token" in data:
                self.token, self.auth_mode = data["token"], "token"
                return True
        except Exception:
            pass
        return False

    def validate_auth(self) -> Tuple[bool, str]:
        """Vérifie le token puis le cookie ; récupère aussi le sesskey (appels AJAX)."""
        if self.token:
            try:
                info = self.call_rest_api("core_webservice_get_site_info")
                if isinstance(info, dict) and "userid" in info:
                    self.user_info, self.auth_mode = info, "token"
                    return True, f"Token API valide ({info.get('fullname', 'Utilisateur')})"
            except Exception:
                pass

        if self.session_cookie:
            self._set_cookie()
            try:
                resp = self._request("GET", f"{self.base_url}/my/", timeout=25)
            except Exception as e:
                return False, f"Erreur de connexion : {e}"
            if resp.status_code == 200 and not mp.is_login_page(resp.text, resp.url):
                self.auth_mode = "cookie"
                self.sesskey = mp.extract_sesskey(resp.text)
                soup = BeautifulSoup(resp.text, "html.parser")
                user_el = soup.find(class_=re.compile(r"usertext|user-name|userbutton"))
                name = mp.clean_text(user_el) if user_el else "Connecté (SSO)"
                self.user_info = {"fullname": name}
                return True, f"Session Web valide ({name})"
            return False, "Cookie MoodleSession expiré ou invalide (redirigé vers la connexion)"
        return False, "Aucune méthode d'authentification valide (Token ou MoodleSession manquant)"

    def check_alive(self) -> bool:
        """Test léger : la session est-elle toujours valide ?"""
        try:
            resp = self._request("GET", f"{self.base_url}/my/", retries=2, timeout=25)
            return resp.status_code == 200 and not mp.is_login_page(resp.text, resp.url)
        except Exception:
            return False

    def call_rest_api(self, function: str, params: Optional[Dict[str, Any]] = None) -> Any:
        if not self.token:
            raise ValueError("Token requis pour appeler l'API REST Moodle")
        data = {"wstoken": self.token, "wsfunction": function, "moodlewsrestformat": "json"}
        data.update(params or {})
        return self._request("POST", f"{self.base_url}/webservice/rest/server.php", data=data, timeout=40).json()

    def call_ajax(self, method: str, args: Dict[str, Any]) -> Any:
        """Appel de l'API AJAX interne (cookie + sesskey), la même que l'interface web."""
        if not self.sesskey:
            raise RuntimeError("sesskey indisponible")
        url = (f"{self.base_url}/lib/ajax/service.php?sesskey={self.sesskey}&info={method}")
        resp = self._request("POST", url, json=[{"index": 0, "methodname": method, "args": args}], timeout=40)
        payload = resp.json()
        if isinstance(payload, list) and payload and not payload[0].get("error"):
            return payload[0].get("data")
        raise RuntimeError(f"AJAX {method} refusé : {str(payload)[:200]}")

    # --------------------------------------------------------------- cours
    def get_enrolled_courses(self) -> List[Dict[str, Any]]:
        """Tous les cours : API token, sinon AJAX (tous statuts), sinon scraping des listings."""
        courses: Dict[int, Dict[str, Any]] = {}

        def add(c: Dict[str, Any]) -> None:
            cid = int(c["id"])
            if cid > 1 and cid not in courses:
                courses[cid] = {
                    "id": cid, "fullname": _unescape((c.get("fullname") or c.get("shortname") or f"Cours {cid}").strip()),
                    "shortname": (c.get("shortname") or "").strip(), "summary": c.get("summary", "") or "",
                    "url": f"{self.base_url}/course/view.php?id={cid}",
                }

        if self.auth_mode == "token" and self.token:
            try:
                uid = self.user_info.get("userid") or self.call_rest_api("core_webservice_get_site_info").get("userid")
                raw = self.call_rest_api("core_enrol_get_users_courses", {"userid": uid})
                if isinstance(raw, list):
                    for c in raw:
                        add(c)
                    if courses:
                        return list(courses.values())
            except Exception as e:
                self.note_error("liste des cours (API)", e)

        if self.auth_mode == "cookie":
            for classification in ("all", "inprogress", "past", "future", "hidden", "favourites"):
                offset = 0
                while True:
                    try:
                        data = self.call_ajax("core_course_get_enrolled_courses_by_timeline_classification", {
                            "offset": offset, "limit": 0 if offset == 0 else 100, "classification": classification,
                            "sort": "fullname", "customfieldname": "", "customfieldvalue": ""})
                    except Exception as e:
                        if classification == "all":
                            self.note_error("liste des cours (AJAX)", e)
                        break
                    for c in data.get("courses", []):
                        add(c)
                    nxt = data.get("nextoffset", 0)
                    if not nxt or nxt <= offset or not data.get("courses"):
                        break
                    offset = nxt

            if not courses:  # repli : pages HTML de listing
                for path in ("/my/courses.php", "/my/", "/course/index.php"):
                    try:
                        html, _ = self.get_html(f"{self.base_url}{path}")
                    except SessionExpired:
                        raise
                    except Exception as e:
                        self.note_error(f"listing {path}", e)
                        continue
                    for c in mp.parse_courses_from_html(html, self.base_url):
                        add(c)
                    for page_url in mp.parse_pagination_links(html, self.base_url):
                        try:
                            for c in mp.parse_courses_from_html(self.get_html(page_url)[0], self.base_url):
                                add(c)
                        except SessionExpired:
                            raise
                        except Exception as e:
                            self.note_error(page_url, e)
                    if courses:
                        break
        return sorted(courses.values(), key=lambda c: c["fullname"].lower())

    def get_course_details(self, course_id: int) -> Dict[str, Any]:
        """Un cours complet : sections, modules, et contenu détaillé de chaque module."""
        if self.auth_mode == "token" and self.token:
            try:
                contents = self.call_rest_api("core_course_get_contents", {"courseid": course_id})
                if isinstance(contents, list) and contents:
                    course = {"id": course_id, "fullname": "", "summary": "",
                              "url": f"{self.base_url}/course/view.php?id={course_id}",
                              "sections": self._format_api_sections(contents)}
                    # complète avec la page web si un cookie est aussi disponible
                    return course
            except Exception as e:
                self.note_error(f"core_course_get_contents({course_id})", e)

        course = self._scrape_course_structure(course_id)
        for sec in course["sections"]:
            for mod in sec["modules"]:
                self.enrich_module(mod)
        return course

    def _format_api_sections(self, contents: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        out = []
        for s_idx, sec in enumerate(contents):
            modules = []
            for mod in sec.get("modules", []):
                m = {"id": mod.get("id"), "name": (mod.get("name") or "").strip(), "type": mod.get("modname", ""),
                     "url": mod.get("url") or f"{self.base_url}/mod/{mod.get('modname')}/view.php?id={mod.get('id')}",
                     "description": mod.get("description", ""), "contents": mod.get("contents", []) or [],
                     "extra": {}, "restricted": not mod.get("uservisible", True), "hidden": False}
                self.enrich_module(m)
                modules.append(m)
            out.append({"id": sec.get("id", s_idx), "section_number": s_idx,
                        "name": (sec.get("name") or "").strip() or f"Section {s_idx}",
                        "summary_html": sec.get("summary", ""), "modules": modules})
        return out

    def _structure_from_state(self, course_id: int) -> Optional[Dict[str, Any]]:
        """Structure exacte via core_courseformat_get_state (Moodle 4+, tous formats : tiles, flexsections...)."""
        if not self.sesskey:
            return None
        try:
            raw = self.call_ajax("core_courseformat_get_state", {"courseid": course_id})
            st = json.loads(raw) if isinstance(raw, str) else raw
            cms = {str(c["id"]): c for c in st.get("cm", [])}
            sections = []
            for sec in sorted(st.get("section", []), key=lambda x: int(x.get("number", 0) or 0)):
                mods = []
                for cid in sec.get("cmlist", []):
                    cm = cms.get(str(cid))
                    if not cm:
                        continue
                    mods.append({
                        "id": int(cm["id"]), "name": html_unescape(cm.get("name", "")).strip(),
                        "type": cm.get("module") or cm.get("modname", ""),
                        "url": cm.get("url") or "", "description": "", "contents": [], "extra": {},
                        "restricted": not cm.get("uservisible", True), "hidden": not cm.get("visible", True)})
                num = int(sec.get("number", len(sections)) or 0)
                sections.append({"id": num, "section_number": num,
                                 "name": html_unescape(sec.get("title", "")).strip() or f"Section {num}",
                                 "summary_html": sec.get("summary", "") or "", "modules": mods})
            if not sections:
                return None
            course_info = st.get("course", {})
            return {"id": course_id, "fullname": html_unescape(course_info.get("fullname", "")),
                    "summary": "", "url": f"{self.base_url}/course/view.php?id={course_id}", "sections": sections}
        except SessionExpired:
            raise
        except Exception as e:
            self.note_error(f"état du cours {course_id}", e)
            return None

    def _fill_from_html(self, course: Dict[str, Any], course_id: int) -> None:
        """Complète descriptions / textes d'étiquettes depuis les pages HTML (page de cours + une par section)."""
        urls = [f"{self.base_url}/course/view.php?id={course_id}"] + [
            f"{self.base_url}/course/view.php?id={course_id}&section={s['section_number']}"
            for s in course["sections"] if s["section_number"] > 0]
        by_id = {m["id"]: m for s in course["sections"] for m in s["modules"] if m["id"]}
        summaries = {s["section_number"]: s for s in course["sections"]}
        for u in urls:
            try:
                page_html, _ = self.get_html(u, timeout=60)
            except SessionExpired:
                raise
            except Exception as e:
                self.note_error(u, e)
                continue
            parsed = mp.parse_course_page(page_html, self.base_url, course_id)
            if not course.get("summary"):
                course["summary"] = parsed.get("summary", "")
            for sec in parsed["sections"]:
                tgt = summaries.get(sec["section_number"])
                if tgt is not None and not tgt.get("summary_html") and sec.get("summary_html"):
                    tgt["summary_html"] = sec["summary_html"]
                for m in sec["modules"]:
                    cur = by_id.get(m["id"])
                    if cur is not None and not cur["description"] and m.get("description"):
                        cur["description"] = m["description"]
                    elif cur is None and m["id"] and sec["name"] != "Autres activités du cours":
                        by_id[m["id"]] = m
                        if tgt is not None:
                            tgt["modules"].append(m)

    def _scrape_course_structure(self, course_id: int) -> Dict[str, Any]:
        url = f"{self.base_url}/course/view.php?id={course_id}"
        state_course = self._structure_from_state(course_id)
        if state_course is not None:
            self._fill_from_html(state_course, course_id)
            course = state_course
            html = ""
        else:
            html, _ = self.get_html(url, timeout=60)
            course = mp.parse_course_page(html, self.base_url, course_id)
        # formats « une section par page » / onglets : on visite chaque section
        for sec_url in (mp.parse_section_links(html, self.base_url, course_id) if html else []):
            try:
                sub = mp.parse_course_page(self.get_html(sec_url, timeout=60)[0], self.base_url, course_id)
                mp.merge_courses(course, sub)
            except SessionExpired:
                raise
            except Exception as e:
                self.note_error(sec_url, e)
        # index « tout le cours » : filet de sécurité pour les ressources que la page n'affiche pas
        try:
            html_res, _ = self.get_html(f"{self.base_url}/course/resources.php?id={course_id}")
            known = {m["id"] for s in course["sections"] for m in s["modules"]}
            extra = []
            for a in BeautifulSoup(html_res, "html.parser").find_all("a", href=mp.MOD_LINK_RE):
                m = mp.MOD_LINK_RE.search(mp.attr(a, "href"))
                if m and int(m.group(2)) not in known and mp.clean_text(a):
                    known.add(int(m.group(2)))
                    extra.append({"id": int(m.group(2)), "name": mp.clean_text(a), "type": m.group(1),
                                  "url": mp.absolutize(self.base_url, mp.attr(a, "href")), "description": "",
                                  "contents": [], "extra": {}, "restricted": False, "hidden": False})
            if extra:
                n = max((s["section_number"] for s in course["sections"]), default=-1) + 1
                course["sections"].append({"id": n, "section_number": n, "name": "Ressources (index du cours)",
                                           "summary_html": "", "modules": extra})
        except SessionExpired:
            raise
        except Exception:
            pass
        return course

    # ------------------------------------------------------- détail d'un module
    def enrich_module(self, mod: Dict[str, Any]) -> None:
        """Remplit mod['extra'] / mod['contents'] selon le type. N'échoue jamais : note l'erreur."""
        mtype, url = mod.get("type", ""), mod.get("url", "")
        extra = mod.setdefault("extra", {})
        # médias/pièces jointes embarqués dans la description du module
        if mod.get("description"):
            emb = mp.find_embedded(mod["description"], self.base_url)
            extra["embedded_assets"], extra["embedded_videos"] = emb["assets"], emb["videos"]
        if not url:
            return
        try:
            if mtype == "page":
                extra["page_content"] = self.get_page_content(mod.get("id", 0), url)
            elif mtype == "url":
                extra["target_url"] = self.resolve_url_target(mod.get("id", 0), url, mod.get("contents"))
            elif mtype == "quiz":
                extra["quiz_details"] = self.get_quiz_details(mod.get("id", 0), url)
            elif mtype == "folder":
                extra["folder_files"] = self.get_folder_files(mod.get("id", 0), url)
            elif mtype == "assign":
                extra["assign_details"] = self.get_assignment_details(mod.get("id", 0), url)
            elif mtype == "resource":
                if not mod.get("contents"):
                    mod["contents"] = self.resolve_resource_files(url)
            elif mtype in ("hvp", "h5pactivity"):
                extra["h5p"] = mp.parse_h5p(self.get_html(url)[0], self.base_url)
            elif mtype == "book":
                extra["book"] = self.get_book(url)
            elif mtype == "forum":
                extra["forum"] = self.get_forum(url)
            elif mtype != "label":
                html, final = self.get_html(url)
                if "/pluginfile.php" in final:  # redirigé directement vers un fichier
                    mod["contents"] = [{"filename": mp.filename_from_url(final), "fileurl": final}]
                else:
                    extra["generic"] = mp.parse_generic_module(html, self.base_url)
        except SessionExpired:
            raise
        except Exception as e:
            self.note_error(f"module {mod.get('name', '?')} ({mtype} #{mod.get('id')})", e)

    def get_page_content(self, page_id: int, page_url: str) -> Dict[str, Any]:
        html, _ = self.get_html(page_url)
        data: Dict[str, Any] = dict(mp.parse_page_module(html, self.base_url))
        emb = mp.find_embedded(data["content_html"], self.base_url)
        data["assets"], data["videos"] = emb["assets"], emb["videos"]
        return data

    def resolve_url_target(self, url_id: int, moodle_url: str, contents_list: Optional[List[Dict[str, Any]]] = None) -> str:
        """URL externe réelle d'un mod_url (YouTube, Pod EPITA, Panopto, etc.)."""
        for item in contents_list or []:
            if item.get("type") == "url" and item.get("fileurl"):
                return item["fileurl"]
        try:
            resp = self._request("GET", moodle_url, allow_redirects=True, timeout=30)
            if mp.is_login_page(resp.text, resp.url) and self.auth_mode == "cookie":
                raise SessionExpired("Session expirée (mod_url)")
            if resp.url != moodle_url and "/mod/url/" not in resp.url:
                return resp.url
            soup = BeautifulSoup(resp.text, "html.parser")
            wk = soup.find(class_=re.compile(r"urlworkaround|generalbox"))
            link = wk.find("a") if wk else None
            if link and link.get("href"):
                return mp.absolutize(self.base_url, mp.attr(link, "href"))
            emb = mp.find_embedded(resp.text, self.base_url)
            if emb["videos"]:
                return emb["videos"][0]["url"]
            return resp.url
        except SessionExpired:
            raise
        except Exception:
            return moodle_url

    def resolve_resource_files(self, resource_url: str) -> List[Dict[str, str]]:
        """URL(s) directe(s) d'un mod_resource, qu'il redirige vers le fichier ou l'affiche dans une page."""
        resp = self._request("GET", resource_url, allow_redirects=True, stream=True, timeout=40)
        try:
            ctype = resp.headers.get("Content-Type", "")
            if "text/html" not in ctype:  # redirigé vers le fichier lui-même
                cd = resp.headers.get("Content-Disposition", "")
                name = ""
                m = re.search(r"filename\*=UTF-8''([^;]+)", cd, re.I) or re.search(r'filename="?([^";]+)"?', cd, re.I)
                if m:
                    name = mp.fix_mojibake(urllib.parse.unquote(m.group(1).strip("\"'")))
                return [{"filename": name or mp.filename_from_url(resp.url), "fileurl": resp.url}]
            html = resp.text
        finally:
            resp.close()
        if self.auth_mode == "cookie" and mp.is_login_page(html, resp.url):
            raise SessionExpired("Session expirée (mod_resource)")
        return mp.parse_resource_page(html, self.base_url)

    def resolve_resource_file(self, resource_id: int, resource_url: str) -> Optional[Dict[str, str]]:
        files = self.resolve_resource_files(resource_url)
        return files[0] if files else None

    def get_folder_files(self, folder_id: int, folder_url: str) -> List[Dict[str, str]]:
        html, _ = self.get_html(folder_url)
        files = mp.parse_folder_page(html, self.base_url)
        if not files:
            zip_url = mp.folder_zip_url(html, self.base_url)
            if zip_url:
                files = [{"filename": f"dossier_{folder_id}.zip", "fileurl": zip_url, "subpath": ""}]
        return files

    def get_assignment_details(self, assign_id: int, assign_url: str) -> Dict[str, Any]:
        html, _ = self.get_html(assign_url)
        return mp.parse_assign_page(html, self.base_url)

    def get_book(self, book_url: str) -> Dict[str, Any]:
        """Livre Moodle : tous les chapitres (HTML) + médias."""
        html, _ = self.get_html(book_url)
        toc = mp.parse_book_toc(html, self.base_url)
        chapters = []
        if not toc:  # livre à un seul chapitre
            toc = [{"id": "0", "title": "", "url": book_url}]
        for ch in toc:
            try:
                page = html if ch["url"] == book_url else self.get_html(ch["url"])[0]
                data = mp.parse_book_chapter(page, self.base_url)
                emb = mp.find_embedded(data["content_html"], self.base_url)
                chapters.append({"title": ch["title"] or data["title"], "content_html": data["content_html"],
                                 "assets": emb["assets"], "videos": emb["videos"]})
            except SessionExpired:
                raise
            except Exception as e:
                self.note_error(f"chapitre de livre {ch['url']}", e)
        return {"chapters": chapters}

    def get_forum(self, forum_url: str, max_discussions: int = 200) -> Dict[str, Any]:
        """Forum (annonces, ressources partagées) : messages et pièces jointes."""
        html, _ = self.get_html(forum_url)
        discussions = []
        for d in mp.parse_forum_discussions(html, self.base_url)[:max_discussions]:
            try:
                data = mp.parse_forum_discussion(self.get_html(d["url"])[0], self.base_url)
                discussions.append({"title": d["title"], "url": d["url"], **data})
            except SessionExpired:
                raise
            except Exception as e:
                self.note_error(f"discussion {d['url']}", e)
        return {"discussions": discussions}

    # ------------------------------------------------------------------ QCM
    def get_quiz_details(self, quiz_id: int, quiz_url: str) -> Dict[str, Any]:
        """Consignes + questions/corrigés fusionnés de TOUTES les tentatives relisibles."""
        html, _ = self.get_html(quiz_url)
        details = mp.parse_quiz_page(html, self.base_url)
        attempts = []
        for review_url in details["review_urls"]:
            try:
                attempts.append(self._scrape_quiz_review(review_url))
            except SessionExpired:
                raise
            except Exception as e:
                self.note_error(f"relecture QCM {review_url}", e)
        details["questions"] = mp.merge_quiz_attempts(attempts) if attempts else []
        details["attempts"] = len(attempts)
        return details

    def _scrape_quiz_review(self, review_url: str) -> List[Dict[str, Any]]:
        html, _ = self.get_html(mp.with_showall(review_url), timeout=60)
        questions = mp.parse_quiz_review(html, self.base_url)
        if not questions:  # showall ignoré : pages une à une
            for page_url in mp.quiz_review_pages(html, self.base_url):
                questions += mp.parse_quiz_review(self.get_html(page_url)[0], self.base_url)
        return questions

    def _scrape_course_page(self, course_id: int) -> Dict[str, Any]:  # compat ancienne API
        return self._scrape_course_structure(course_id)

    # ------------------------------------------------------------ téléchargement
    def download_file(self, file_url: str, dest_path: str, force: bool = False) -> bool:
        """
        Télécharge un fichier Moodle (streaming, écriture atomique). Refuse d'enregistrer une page
        de connexion à la place du fichier et lève SessionExpired dans ce cas.
        """
        ok, _reason = self.download_file_ex(file_url, dest_path, force)
        return ok

    def download_file_ex(self, file_url: str, dest_path: str, force: bool = False) -> Tuple[bool, str]:
        if not force and os.path.exists(dest_path) and os.path.getsize(dest_path) > 0:
            return True, "déjà présent"
        os.makedirs(os.path.dirname(dest_path) or ".", exist_ok=True)
        tmp_path = f"{dest_path}.part"
        url = mp.with_forcedownload(file_url)
        if self.auth_mode == "token" and self.token and "token=" not in url:
            url += ("&" if "?" in url else "?") + f"token={self.token}"
        try:
            resp = self._request("GET", url, stream=True, timeout=(15, 120))
            try:
                if resp.status_code != 200:
                    return False, f"HTTP {resp.status_code}"
                ctype = resp.headers.get("Content-Type", "")
                wants_html = dest_path.lower().endswith((".html", ".htm"))
                if "text/html" in ctype and not wants_html:
                    body = resp.text[:60000]
                    if self.auth_mode == "cookie" and mp.is_login_page(body, resp.url):
                        raise SessionExpired(f"Session expirée pendant le téléchargement de {file_url}")
                    return False, "réponse HTML au lieu d'un fichier (accès refusé ?)"
                expected = int(resp.headers.get("Content-Length", 0) or 0)
                written = 0
                with open(tmp_path, "wb") as f:
                    for chunk in resp.iter_content(chunk_size=1 << 17):
                        if chunk:
                            f.write(chunk)
                            written += len(chunk)
                if expected and written < expected and "gzip" not in resp.headers.get("Content-Encoding", ""):
                    os.remove(tmp_path)
                    return False, f"téléchargement tronqué ({written}/{expected} octets)"
            finally:
                resp.close()
            if written == 0:
                os.remove(tmp_path)
                return False, "fichier vide"
            os.replace(tmp_path, dest_path)
            return True, f"{written} octets"
        except SessionExpired:
            raise
        except Exception as e:
            if os.path.exists(tmp_path):
                try:
                    os.remove(tmp_path)
                except OSError:
                    pass
            return False, str(e)
