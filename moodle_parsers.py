"""
moodle_parsers.py - Parsing HTML de Moodle (EPITA), sans aucun accès réseau.

Tout ce qui transforme une page Moodle en données structurées vit ici, pour pouvoir
être testé hors ligne avec des fragments HTML (tests/test_moodle_parsers.py).
Les fonctions sont tolérantes : Moodle 3.x et 4.x (thèmes Boost / Classic / Edunao)
n'ont pas exactement le même balisage, donc chaque extraction a des repli.
"""

from __future__ import annotations

import json
import re
import urllib.parse
from typing import Any, Dict, List, Optional, Set

from bs4 import BeautifulSoup, Tag

MOD_LINK_RE = re.compile(r"/mod/(\w+)/view\.php\?(?:[^#]*&)?id=(\d+)")
PLUGINFILE_RE = re.compile(r"/(?:webservice/)?pluginfile\.php/")
VIDEO_EXT_RE = re.compile(r"\.(mp4|webm|mkv|mov|m4v|avi|ogv)(?:$|[?#])", re.I)
AUDIO_EXT_RE = re.compile(r"\.(mp3|m4a|wav|ogg|oga|flac)(?:$|[?#])", re.I)
VIDEO_HOST_RE = re.compile(
    r"(youtube\.com|youtu\.be|youtube-nocookie\.com|vimeo\.com|dailymotion\.com|"
    r"pod\.epita\.fr|panopto\.|mediasite\.|canal-u\.tv|peertube|"
    r"loom\.com|zoom\.us/rec|teams\.microsoft\.com|web\.microsoftstream\.com|"
    r"\.sharepoint\.com/.*stream|drive\.google\.com/file|"
    r"cloud\.epita\.fr|video\.epita\.fr|learn-videos\.)",
    re.I,
)

# Modules dont le contenu est une simple page à lire (pas de traitement dédié)
GENERIC_PAGE_TYPES = {
    "lesson", "glossary", "wiki", "choice", "feedback", "data", "workshop",
    "scorm", "imscp", "lti", "survey", "chat", "bigbluebuttonbn", "hvp",
    "h5pactivity", "subsection", "etherpadlite", "zoom", "attendance",
    "kalvidres", "kalvidassign", "panopto", "videotime", "customcert",
}


# --------------------------------------------------------------------------- #
# Utilitaires
# --------------------------------------------------------------------------- #
def attr(tag: Any, name: str, default: str = "") -> str:
    """Attribut HTML toujours renvoyé comme str (BeautifulSoup peut renvoyer une liste)."""
    val = tag.get(name, default) if tag is not None else default
    if isinstance(val, list):
        val = " ".join(val)
    return val if isinstance(val, str) else default


def soup_of(html: str) -> BeautifulSoup:
    return BeautifulSoup(html or "", "html.parser")


def absolutize(base_url: str, href: Optional[str]) -> str:
    return urllib.parse.urljoin(base_url + "/", href) if href else ""


def clean_text(el: Optional[Tag]) -> str:
    """Texte visible d'un nœud, sans les libellés d'accessibilité cachés."""
    if el is None:
        return ""
    clone = BeautifulSoup(str(el), "html.parser")
    for h in clone.find_all(class_=re.compile(r"\b(accesshide|sr-only|visually-hidden|text-muted)\b")):
        h.decompose()
    return re.sub(r"\s+", " ", clone.get_text(" ", strip=True)).strip()


def is_login_page(html: str, url: str = "") -> bool:
    """True si la réponse est la page de connexion (session expirée / cookie invalide)."""
    if re.search(r"/login/(index|logout)\.php|/auth/[^/]+/(login|index)\.php|/login\?|forgeid|"
                 r"sso\.[^/]*epita|cri\.epita\.fr/(?:auth|login)|/realms/[^/]+/protocol/openid", url or "", re.I):
        return True
    if not html:
        return False
    head = html[:60000]
    return bool(
        re.search(r'name="logintoken"', head)
        or re.search(r'<form[^>]+id="login"', head)
        or re.search(r'id="loginbtn"', head)
        or ("Vous n'êtes pas connecté" in head and "/login/index.php" in head)
    )


def extract_sesskey(html: str) -> str:
    m = re.search(r'"sesskey"\s*:\s*"([A-Za-z0-9]{6,})"', html or "")
    if m:
        return m.group(1)
    m = re.search(r"[?&]sesskey=([A-Za-z0-9]{6,})", html or "")
    return m.group(1) if m else ""


def fix_mojibake(name: str) -> str:
    """« RÃ©f » -> « Réf » : en-têtes HTTP décodés en latin-1 alors que Moodle envoie de l'UTF-8."""
    try:
        return name.encode("latin-1").decode("utf-8")
    except (UnicodeEncodeError, UnicodeDecodeError):
        return name


def filename_from_url(url: str) -> str:
    path = urllib.parse.urlparse(url).path
    return urllib.parse.unquote(path.rsplit("/", 1)[-1]) or "document"


def pluginfile_subpath(url: str) -> str:
    """Sous-dossier d'un fichier dans un mod_folder, déduit de l'URL pluginfile."""
    path = urllib.parse.unquote(urllib.parse.urlparse(url).path)
    m = re.search(r"/mod_folder/content/\d+/(.+)$", path)
    if not m:
        return ""
    parts = m.group(1).split("/")
    return "/".join(parts[:-1])


def with_forcedownload(url: str) -> str:
    """Ajoute forcedownload=1 aux pluginfile pour obtenir le fichier brut (pas un viewer)."""
    if not PLUGINFILE_RE.search(url) or "forcedownload" in url:
        return url
    return url + ("&" if "?" in url else "?") + "forcedownload=1"


# --------------------------------------------------------------------------- #
# Médias / pièces jointes embarqués dans du HTML
# --------------------------------------------------------------------------- #
def find_embedded(html: str, base_url: str) -> Dict[str, List[Dict[str, str]]]:
    """
    Inventorie ce qu'un bloc HTML embarque :
      assets  : fichiers Moodle (pluginfile) - images, PDF, pièces jointes, médias locaux
      videos  : vidéos/lecteurs (iframe YouTube/Pod/Panopto..., <video>, liens .mp4)
    """
    soup = soup_of(html)
    assets: List[Dict[str, str]] = []
    videos: List[Dict[str, str]] = []
    seen_a: Set[str] = set()
    seen_v: Set[str] = set()

    def add_asset(url: str, kind: str, name: str = "") -> None:
        url = absolutize(base_url, url)
        key = url.split("?")[0]
        if not url or key in seen_a:
            return
        seen_a.add(key)
        assets.append({"url": url, "kind": kind, "filename": name or filename_from_url(url)})

    def add_video(url: str, title: str = "", local: bool = False) -> None:
        url = absolutize(base_url, url)
        key = url.split("?")[0]
        if not url or key in seen_v:
            return
        seen_v.add(key)
        videos.append({"url": url, "title": title, "local": "1" if local else ""})

    for tag in soup.find_all(["img", "source", "video", "audio", "object", "embed", "iframe", "a"]):
        attr = {"a": "href", "object": "data"}.get(tag.name, "src")
        val = tag.get(attr)
        if not val or val.startswith(("javascript:", "#", "data:", "mailto:")):
            continue
        full = absolutize(base_url, val)
        is_pf = bool(PLUGINFILE_RE.search(full))

        if tag.name in ("video", "source") and (VIDEO_EXT_RE.search(full) or tag.name == "video"
                                                or (tag.parent and tag.parent.name == "video")):
            if is_pf:
                add_video(full, local=True)
                add_asset(full, "video")
            else:
                add_video(full)
            continue
        if tag.name in ("audio", "source") and (AUDIO_EXT_RE.search(full)
                                                or (tag.parent and tag.parent.name == "audio")):
            if is_pf:
                add_asset(full, "audio")
            continue
        if tag.name == "iframe":
            if is_pf:
                add_asset(full, "document")
            elif VIDEO_HOST_RE.search(full) or "/h5p/" in full or "embed" in full:
                add_video(full, tag.get("title", ""))
            continue
        if tag.name == "a":
            if VIDEO_EXT_RE.search(full):
                if is_pf:
                    add_video(full, clean_text(tag), local=True)
                    add_asset(full, "video", clean_text(tag) and filename_from_url(full))
                else:
                    add_video(full, clean_text(tag))
            elif VIDEO_HOST_RE.search(full):
                add_video(full, clean_text(tag))
            elif is_pf:
                add_asset(full, "document")
            continue
        if is_pf:  # img / object / embed
            add_asset(full, "image" if tag.name == "img" else "document")

    return {"assets": assets, "videos": videos}


# --------------------------------------------------------------------------- #
# Découverte des cours
# --------------------------------------------------------------------------- #
def parse_courses_from_html(html: str, base_url: str) -> List[Dict[str, Any]]:
    """Liste de cours depuis n'importe quelle page contenant des liens course/view.php."""
    soup = soup_of(html)
    found: Dict[int, Dict[str, Any]] = {}
    for a in soup.find_all("a", href=re.compile(r"/course/view\.php\?(?:[^#]*&)?id=\d+")):
        m = re.search(r"[?&]id=(\d+)", a["href"])
        if not m:
            continue
        cid = int(m.group(1))
        if cid <= 1:
            continue
        title = clean_text(a)
        if not title or len(title) < 2:
            card = a.find_parent(class_=re.compile(r"course|card|coursebox"))
            if card:
                t = card.find(class_=re.compile(r"coursename|card-title|course-name|multiline"))
                title = clean_text(t) if t else ""
        entry = found.setdefault(cid, {"id": cid, "fullname": "", "shortname": "", "summary": "",
                                       "url": f"{base_url}/course/view.php?id={cid}"})
        if title and title.lower() not in {"tableau de bord", "accueil", "dashboard", "home", "voir"} \
                and len(title) > len(entry["fullname"]):
            entry["fullname"] = title
            entry["shortname"] = title
    return [c for c in found.values() if c["fullname"]] or []


def parse_pagination_links(html: str, base_url: str) -> List[str]:
    """Liens de pagination (page=N / perpage) d'une page de listing."""
    soup = soup_of(html)
    urls = []
    for a in soup.select("ul.pagination a[href], .paging a[href], nav.pagination a[href]"):
        href = a.get("href", "")
        if "page=" in href:
            urls.append(absolutize(base_url, href))
    return sorted(set(urls))


# --------------------------------------------------------------------------- #
# Page de cours
# --------------------------------------------------------------------------- #
def parse_module_element(el: Tag, base_url: str) -> Optional[Dict[str, Any]]:
    classes = attr(el, "class")
    tm = re.search(r"modtype_(\w+)", classes)
    mod_type = tm.group(1) if tm else "unknown"
    link = el.find("a", href=MOD_LINK_RE)
    mod_url, mod_id = "", 0
    if link:
        m = MOD_LINK_RE.search(attr(link, "href"))
        if m:
            mod_type, mod_id = m.group(1), int(m.group(2))
        mod_url = absolutize(base_url, attr(link, "href"))
    elif attr(el, "id").startswith("module-"):
        try:
            mod_id = int(attr(el, "id").split("-", 1)[1])
        except ValueError:
            pass

    inst = el.find(class_=re.compile(r"\b(instancename|activityname|activity-name)\b"))
    name = clean_text(inst) if inst else ""
    if not name and link:
        name = clean_text(link)
    desc_el = el.find(class_=re.compile(r"\b(contentafterlink|activity-description|description)\b"))
    desc_html = desc_el.decode_contents() if desc_el else ""

    if mod_type in ("label", "unknown") and not link:
        body = el.find(class_=re.compile(r"\b(contentwithoutlink|no-overflow|activity-altcontent|course-description-item)\b"))
        desc_html = body.decode_contents() if body else el.decode_contents()
        if mod_type == "unknown":
            mod_type = "label"
        name = name or "Note d'information"
    if not name and not desc_html:
        return None

    restricted = bool(el.find(class_=re.compile(r"availabilityinfo|isrestricted")))
    hidden = "dimmed" in classes or bool(el.find(class_=re.compile(r"\bdimmed")))
    return {
        "id": mod_id, "name": name, "type": mod_type, "url": mod_url,
        "description": desc_html, "contents": [], "extra": {},
        "restricted": restricted, "hidden": hidden,
    }


def parse_course_page(html: str, base_url: str, course_id: int) -> Dict[str, Any]:
    """Titre, résumé et sections/modules d'une page course/view.php."""
    soup = soup_of(html)
    title_tag = soup.find(["h1", "h2"], class_=re.compile(r"page-header-headings|coursename|h2"))
    title = clean_text(title_tag) if title_tag else (soup.title.get_text(strip=True) if soup.title else "")
    title = re.sub(r"^\s*(Cours|Course)\s*:\s*", "", re.sub(r"\s*\|\s*Plateforme.*", "", title)).strip()

    summary_el = soup.find(class_=re.compile(r"\b(course-summary|course-description)\b"))
    summary = summary_el.decode_contents() if summary_el else ""

    sections: List[Dict[str, Any]] = []
    seen_ids: Set[int] = set()
    sec_els = [e for e in soup.find_all(["li", "div", "section"], id=re.compile(r"^section-\d+$"))]
    if not sec_els:
        sec_els = soup.find_all(attrs={"data-sectionid": True})

    for s_idx, sec_el in enumerate(sec_els):
        m = re.search(r"section-(\d+)", attr(sec_el, "id"))
        s_num = int(m.group(1)) if m else s_idx
        name_el = sec_el.find(class_=re.compile(r"\b(sectionname|section-title)\b")) \
            or sec_el.find(["h3", "h4"])
        sec_name = clean_text(name_el) if name_el else (attr(sec_el, "data-sectionname") or f"Section {s_num}")
        sum_el = sec_el.find(class_=re.compile(r"\b(summary|section-summary|summarytext)\b"))
        modules: List[Dict[str, Any]] = []

        act_els = sec_el.find_all(attrs={"id": re.compile(r"^module-\d+$")})
        if not act_els:
            act_els = sec_el.find_all("li", class_=re.compile(r"\bactivity\b"))
        for act in act_els:
            mod = parse_module_element(act, base_url)
            if not mod:
                continue
            if mod["id"]:
                if mod["id"] in seen_ids:
                    continue
                seen_ids.add(mod["id"])
            modules.append(mod)

        sections.append({
            "id": s_num, "section_number": s_num, "name": sec_name,
            "summary_html": sum_el.decode_contents() if sum_el else "",
            "modules": modules,
        })

    # Filet de sécurité : tout lien /mod/x/view.php de la page absent des sections
    orphan: List[Dict[str, Any]] = []
    for a in soup.find_all("a", href=MOD_LINK_RE):
        m = MOD_LINK_RE.search(attr(a, "href"))
        if not m:
            continue
        mid = int(m.group(2))
        if mid in seen_ids:
            continue
        name = clean_text(a)
        if not name or (m.group(1) == "forum" and "discuss" in attr(a, "href")):
            continue
        seen_ids.add(mid)
        orphan.append({"id": mid, "name": name, "type": m.group(1), "url": absolutize(base_url, attr(a, "href")),
                       "description": "", "contents": [], "extra": {}, "restricted": False, "hidden": False})
    if orphan:
        next_num = (max((s["section_number"] for s in sections), default=-1)) + 1
        sections.append({"id": next_num, "section_number": next_num, "name": "Autres activités du cours",
                         "summary_html": "", "modules": orphan})

    return {"id": course_id, "fullname": title, "summary": summary,
            "url": f"{base_url}/course/view.php?id={course_id}", "sections": sections}


def parse_section_links(html: str, base_url: str, course_id: int) -> List[str]:
    """Liens vers les sections individuelles (format « une section par page » / onglets)."""
    soup = soup_of(html)
    urls: Set[str] = set()
    for a in soup.find_all("a", href=re.compile(r"/course/view\.php\?[^#]*id=%d[^#]*section=\d+" % course_id)):
        urls.add(absolutize(base_url, a["href"]))
    for a in soup.find_all("a", href=re.compile(r"/course/section\.php\?id=\d+")):
        urls.add(absolutize(base_url, a["href"]))
    return sorted(urls)


def merge_courses(primary: Dict[str, Any], extra: Dict[str, Any]) -> Dict[str, Any]:
    """Fusionne les modules d'une 2e page de cours dans la 1re (par id de module)."""
    known = {m["id"] for s in primary["sections"] for m in s["modules"] if m["id"]}
    by_num = {s["section_number"]: s for s in primary["sections"]}
    for sec in extra["sections"]:
        tgt = by_num.get(sec["section_number"])
        if tgt is None:
            primary["sections"].append(sec)
            by_num[sec["section_number"]] = sec
            known.update(m["id"] for m in sec["modules"] if m["id"])
            continue
        if not tgt.get("summary_html") and sec.get("summary_html"):
            tgt["summary_html"] = sec["summary_html"]
        for m in sec["modules"]:
            if m["id"] and m["id"] in known:
                continue
            tgt["modules"].append(m)
            if m["id"]:
                known.add(m["id"])
    primary["sections"].sort(key=lambda s: s["section_number"])
    return primary


# --------------------------------------------------------------------------- #
# Ressources, dossiers, pages, livres
# --------------------------------------------------------------------------- #
def main_region(soup: BeautifulSoup) -> Optional[Tag]:
    return (soup.find(id="region-main") or soup.find(attrs={"role": "main"})
            or soup.find("main") or soup.find(id="page-content"))


def parse_resource_page(html: str, base_url: str) -> List[Dict[str, str]]:
    """Fichier(s) d'une page mod/resource affichée (mode « page »/« embed »)."""
    soup = soup_of(html)
    region = main_region(soup) or soup
    files: List[Dict[str, str]] = []
    seen: Set[str] = set()
    cands = []
    for sel in ("object[data]", "iframe#resourceobject[src]", "embed[src]", "img.resourceimage[src]",
                "video source[src]", "video[src]", ".resourceworkaround a[href]", "a[href]"):
        for el in region.select(sel):
            cands.append(el.get("data") or el.get("src") or el.get("href"))
    for href in cands:
        if not href:
            continue
        full = absolutize(base_url, href)
        key = full.split("?")[0]
        if PLUGINFILE_RE.search(full) and key not in seen:
            seen.add(key)
            files.append({"filename": filename_from_url(full), "fileurl": full})
    return files


def parse_folder_page(html: str, base_url: str) -> List[Dict[str, str]]:
    """Tous les fichiers d'un dossier Moodle, avec leur sous-dossier."""
    soup = soup_of(html)
    region = main_region(soup) or soup
    files, seen = [], set()
    for a in region.find_all("a", href=PLUGINFILE_RE):
        full = absolutize(base_url, a["href"])
        key = full.split("?")[0]
        if key in seen or "/mod_folder/" not in full:
            continue
        seen.add(key)
        name = filename_from_url(full)
        files.append({"filename": name, "fileurl": full, "subpath": pluginfile_subpath(full)})
    return files


def folder_zip_url(html: str, base_url: str) -> str:
    soup = soup_of(html)
    form = soup.find("form", action=re.compile(r"/mod/folder/download_folder\.php"))
    if not form:
        return ""
    params = {i.get("name"): i.get("value", "") for i in form.find_all("input") if i.get("name")}
    return absolutize(base_url, form["action"]) + "?" + urllib.parse.urlencode(params)


def parse_page_module(html: str, base_url: str) -> Dict[str, str]:
    """Contenu HTML d'un mod_page (zone de contenu sans la navigation)."""
    soup = soup_of(html)
    title_el = soup.find(["h1", "h2"], class_=re.compile(r"page-header-headings|main"))
    box = (soup.find(class_=re.compile(r"\bbox\b.*\bgeneralbox\b|\bgeneralbox\b"))
           or soup.find(class_="page-content") or main_region(soup))
    return {"title": clean_text(title_el), "content_html": box.decode_contents() if box else ""}


def parse_generic_module(html: str, base_url: str) -> Dict[str, Any]:
    """Page quelconque (leçon, glossaire, wiki, H5P, SCORM...) : contenu + pièces jointes."""
    soup = soup_of(html)
    region = main_region(soup)
    if region:
        for junk in region.select("nav, .activity-navigation, .secondary-navigation, form.mform, "
                                  ".action-menu, script, style, .breadcrumb"):
            junk.decompose()
    content = region.decode_contents() if region else ""
    emb = find_embedded(content, base_url)
    return {"content_html": content, "assets": emb["assets"], "videos": emb["videos"]}


def parse_book_toc(html: str, base_url: str) -> List[Dict[str, str]]:
    soup = soup_of(html)
    chapters, seen = [], set()
    for a in soup.select(".book_toc a[href], .block_book_toc a[href], #page-mod-book-view a[href*='chapterid']"):
        m = re.search(r"chapterid=(\d+)", a.get("href", ""))
        if not m or m.group(1) in seen:
            continue
        seen.add(m.group(1))
        chapters.append({"id": m.group(1), "title": clean_text(a), "url": absolutize(base_url, a["href"])})
    return chapters


def parse_book_chapter(html: str, base_url: str) -> Dict[str, str]:
    soup = soup_of(html)
    box = soup.find(class_=re.compile(r"\bbook_content\b")) or soup.find(class_="generalbox") or main_region(soup)
    title_el = soup.find(class_=re.compile(r"\bbook_chapter_title\b")) or soup.find(["h3", "h2"])
    return {"title": clean_text(title_el), "content_html": box.decode_contents() if box else ""}


def parse_forum_discussions(html: str, base_url: str) -> List[Dict[str, str]]:
    soup = soup_of(html)
    out, seen = [], set()
    for a in soup.find_all("a", href=re.compile(r"/mod/forum/discuss\.php\?d=\d+")):
        m = re.search(r"d=(\d+)", a["href"])
        if m.group(1) in seen:
            continue
        seen.add(m.group(1))
        out.append({"id": m.group(1), "title": clean_text(a), "url": absolutize(base_url, a["href"])})
    return out


def parse_forum_discussion(html: str, base_url: str) -> Dict[str, Any]:
    soup = soup_of(html)
    posts = []
    for p in soup.select("[data-region='post'], article.forum-post-container, div.forumpost"):
        body = p.find(class_=re.compile(r"post-content-container|posting|content"))
        author = p.find(class_=re.compile(r"author|byline|username"))
        posts.append({"author": clean_text(author)[:120],
                      "html": body.decode_contents() if body else ""})
    emb = find_embedded(str(main_region(soup) or soup), base_url)
    return {"posts": posts, "assets": emb["assets"], "videos": emb["videos"]}


def parse_assign_page(html: str, base_url: str) -> Dict[str, Any]:
    soup = soup_of(html)
    intro = soup.find(id="intro") or soup.find(class_=re.compile(r"\b(assign_intro|activity-description)\b"))
    due = ""
    for row in soup.find_all(["tr", "div"], class_=re.compile(r"\b(r\d|row|activity-dates)\b")):
        text = clean_text(row)
        if re.search(r"date limite|due date|échéance|remise|closes|ferme", text, re.I) and len(text) < 200:
            due = text
            break
    files = []
    for f in find_embedded(str(main_region(soup) or soup), base_url)["assets"]:
        if f["kind"] != "image" or "/mod_assign/" in f["url"]:
            files.append({"filename": f["filename"], "fileurl": f["url"]})
    return {"title": "", "intro_html": intro.decode_contents() if intro else "", "due_date": due, "files": files}


# --------------------------------------------------------------------------- #
# QCM
# --------------------------------------------------------------------------- #
def parse_quiz_page(html: str, base_url: str) -> Dict[str, Any]:
    """Consignes, règles et liens de relecture de TOUTES les tentatives d'un quiz."""
    soup = soup_of(html)
    intro = soup.find(id="intro") or soup.find(class_=re.compile(r"\bquizinfo\b|activity-description"))
    rules = []
    for el in soup.select(".quizinfo p, .quizinfo div, .quizattempt p, .generalbox p, li"):
        text = clean_text(el)
        if text and len(text) < 260 and re.search(
                r"tentative|temps|ouvert|fermé|note|méthode|limite|attempt|time|opens|closes|grade", text, re.I):
            if text not in rules:
                rules.append(text)
    reviews: Dict[str, str] = {}
    for a in soup.find_all("a", href=re.compile(r"/mod/quiz/review\.php\?[^#]*attempt=\d+")):
        aid = re.search(r"attempt=(\d+)", a["href"]).group(1)
        reviews.setdefault(aid, absolutize(base_url, a["href"]))
    return {"title": "", "intro_html": intro.decode_contents() if intro else "",
            "rules": rules[:12], "review_urls": list(reviews.values()), "review_url": next(iter(reviews.values()), ""),
            "questions": []}


def with_showall(url: str) -> str:
    """Force l'affichage de toutes les questions sur une seule page de relecture."""
    parsed = urllib.parse.urlparse(url)
    q = urllib.parse.parse_qs(parsed.query)
    q["showall"] = ["1"]
    q.pop("page", None)
    return urllib.parse.urlunparse(parsed._replace(query=urllib.parse.urlencode(q, doseq=True)))


def quiz_review_pages(html: str, base_url: str) -> List[str]:
    """Autres pages de la même relecture (au cas où showall=1 est ignoré)."""
    soup = soup_of(html)
    urls = {absolutize(base_url, a["href"]) for a in soup.select(".qnbutton[href], a.qnbutton[href]")
            if "review.php" in a["href"]}
    return sorted(urls)


_LABEL_PREFIX_RE = re.compile(r"^\s*[A-Za-z0-9]{1,2}[.)]\s+")


def _option_text(row: Tag) -> str:
    node = row
    for lab in row.find_all("label"):
        node = lab
        break
    text = clean_text(node)
    # retire le préfixe « a. » exporté 3 fois par certains thèmes
    for nb in node.find_all(class_=re.compile(r"answernumber")):
        nb.decompose()
    text2 = clean_text(node)
    return _LABEL_PREFIX_RE.sub("", text2 or text).strip()


def parse_quiz_review(html: str, base_url: str) -> List[Dict[str, Any]]:
    """
    Questions d'une page de relecture de tentative, avec la CORRECTION quand Moodle
    l'affiche :
      answers[i] = {text, checked (cochée par l'élève), correct (True/False/None)}
      right_answer_text = « La réponse correcte est : ... »
    """
    soup = soup_of(html)
    questions: List[Dict[str, Any]] = []
    for qb in soup.find_all("div", class_=re.compile(r"\bque\b")):
        classes = qb.get("class", [])
        qtype = next((c for c in classes if c in {
            "multichoice", "truefalse", "shortanswer", "numerical", "match", "essay", "calculated",
            "calculatedmulti", "calculatedsimple", "ddwtos", "gapselect", "multianswer", "ddmarker", "ddimageortext",
            "ordering", "description", "stack", "coderunner", "randomsamatch"}), "unknown")
        state_el = qb.find(class_="state")
        state = clean_text(state_el)
        grade_el = qb.find(class_="grade")
        grade = clean_text(grade_el)
        no_el = qb.find(class_="qno")
        number = clean_text(no_el) or "Question"
        qtext_el = qb.find(class_="qtext")
        qtext_html = qtext_el.decode_contents() if qtext_el else ""

        answers: List[Dict[str, Any]] = []
        ans_root = qb.find(class_="answer")
        if ans_root:
            rows = [r for r in ans_root.find_all("div", recursive=False)
                    if re.search(r"\br\d\b", " ".join(r.get("class", [])))]
            if not rows:
                rows = ans_root.find_all(["div", "tr"], class_=re.compile(r"\br[01]\b"))
            for row in rows:
                inp = row.find("input", attrs={"type": re.compile("radio|checkbox")})
                rcls = " ".join(row.get("class", [])) + " " + " ".join(
                    " ".join(x.get("class", [])) for x in row.find_all(True, class_=True))
                correct: Optional[bool] = None
                if re.search(r"\bcorrect\b", rcls) and not re.search(r"\bincorrect\b", rcls):
                    correct = True
                elif re.search(r"\bincorrect\b", rcls):
                    correct = False
                text = _option_text(row)
                if not text:
                    continue
                answers.append({"text": text, "checked": bool(inp and inp.has_attr("checked")), "correct": correct})
        else:  # réponses courtes / numériques : valeur saisie
            for inp in qb.find_all("input", attrs={"type": "text"}):
                val = (inp.get("value") or "").strip()
                if val:
                    answers.append({"text": val, "checked": True, "correct": None})

        right_el = qb.find(class_="rightanswer")
        right = clean_text(right_el)
        right_html = right_el.decode_contents() if right_el else ""
        fb_parts = []
        for cls in ("specificfeedback", "generalfeedback", "feedback", "comment"):
            for el in qb.find_all(class_=re.compile(r"^%s$" % cls)):
                t = el.decode_contents().strip()
                if t and t not in fb_parts:
                    fb_parts.append(t)

        # complète « correct » à partir de « La réponse correcte est : A, B » (comparaison exacte)
        if right and answers:
            body = re.sub(r"^.*?(?:est|sont|is|are)\s*:\s*", "", right, count=1, flags=re.I)
            items = {re.sub(r"\s+", " ", i).strip().lower() for i in re.split(r"[;,\n]|\bet\b", body) if i.strip()}
            items.add(re.sub(r"\s+", " ", body).strip().lower())
            matched = [a["text"].strip().lower() in items for a in answers]
            if any(matched):
                for a, hit in zip(answers, matched):
                    if a["correct"] is None or hit:
                        a["correct"] = hit

        questions.append({
            "number": number, "type": qtype, "state": state, "grade": grade,
            "question_html": qtext_html, "answers": answers,
            "right_answer": right, "right_answer_html": right_html,
            "feedback_html": "\n".join(fb_parts),
        })
    return questions


def merge_quiz_attempts(attempts: List[List[Dict[str, Any]]]) -> List[Dict[str, Any]]:
    """
    Fusionne les tentatives : une même question (même énoncé) n'apparaît qu'une fois ;
    la version la plus informative gagne et les « bonnes réponses » connues s'additionnent.
    Moodle mélange parfois l'ordre des options : on raisonne sur le texte.
    """
    merged: Dict[str, Dict[str, Any]] = {}
    order: List[str] = []

    def key_of(q: Dict[str, Any]) -> str:
        return re.sub(r"\W+", " ", soup_of(q["question_html"]).get_text(" ")).strip().lower()

    for qs in attempts:
        for q in qs:
            k = key_of(q)
            if not k:
                continue
            if k not in merged:
                merged[k] = q
                order.append(k)
                continue
            cur = merged[k]
            known = {a["text"].lower(): a for a in cur["answers"]}
            for a in q["answers"]:
                t = a["text"].lower()
                if t in known:
                    if a["correct"] is True:
                        known[t]["correct"] = True
                    elif known[t]["correct"] is None and a["correct"] is False:
                        known[t]["correct"] = False
                else:
                    cur["answers"].append(a)
            if not cur["right_answer"] and q["right_answer"]:
                cur["right_answer"], cur["right_answer_html"] = q["right_answer"], q["right_answer_html"]
            if len(q["feedback_html"]) > len(cur["feedback_html"]):
                cur["feedback_html"] = q["feedback_html"]
            if "correct" in q["state"].lower() and "incorrect" not in q["state"].lower() \
                    and "correct" not in cur["state"].lower().replace("incorrect", ""):
                cur["state"], cur["grade"] = q["state"], q["grade"]
    return [merged[k] for k in order]


# --------------------------------------------------------------------------- #
# H5P (mod_hvp) : contenu interactif exposé dans H5PIntegration
# --------------------------------------------------------------------------- #
def _h5p_text(s: Any) -> str:
    """HTML H5P -> texte simple (une ligne par bloc)."""
    if not isinstance(s, str):
        return ""
    soup = BeautifulSoup(s.replace("&#039;", "'"), "html.parser")
    return re.sub(r"[ \t]+", " ", soup.get_text("\n", strip=True)).strip()


def _h5p_walk(node: Any, out: Dict[str, Any], base: str) -> None:
    """Parcourt récursivement le JSON d'un contenu H5P et collecte vidéos, textes, questions."""
    if isinstance(node, list):
        for it in node:
            _h5p_walk(it, out, base)
        return
    if not isinstance(node, dict):
        return
    lib = str(node.get("library", "")).split(" ")[0] if isinstance(node.get("library"), str) else ""
    params = node.get("params") if lib else None
    if isinstance(params, dict):
        if lib == "H5P.MultiChoice":
            answers = [{"text": _h5p_text(a.get("text")), "correct": bool(a.get("correct"))}
                       for a in params.get("answers", [])]
            out["questions"].append({"type": "multichoice", "question": _h5p_text(params.get("question")),
                                     "answers": [a for a in answers if a["text"]]})
        elif lib == "H5P.TrueFalse":
            out["questions"].append({"type": "truefalse", "question": _h5p_text(params.get("question")),
                                     "correct": str(params.get("correct")).lower() == "true"})
        elif lib == "H5P.Summary":
            for s in params.get("summaries", []):
                st = [_h5p_text(x) for x in s.get("summary", [])]
                if len(st) >= 2 and st[0]:
                    out["questions"].append({"type": "summary", "question": _h5p_text(params.get("intro")),
                                             "answers": [{"text": t, "correct": i == 0} for i, t in enumerate(st) if t]})
        elif lib in ("H5P.AdvancedText", "H5P.Text"):
            t = _h5p_text(params.get("text"))
            if t:
                out["texts"].append(t)
        elif lib == "H5P.Blanks":
            t = _h5p_text(params.get("text") or "")
            qs = [_h5p_text(q) for q in params.get("questions", []) if isinstance(q, str)]
            out["texts"].extend(x for x in [t] + qs if x)
        elif lib == "H5P.DragText":
            t = _h5p_text(params.get("textField"))
            if t:
                out["texts"].append(t)
        for f in (params.get("files") or []) if isinstance(params.get("files"), list) else []:
            _h5p_video(f, out, base)
        _h5p_walk(params, out, base)
        return
    for k, v in node.items():
        if k == "files" and isinstance(v, list):
            for f in v:
                _h5p_video(f, out, base)
        else:
            _h5p_walk(v, out, base)


def _h5p_video(f: Any, out: Dict[str, Any], base: str) -> None:
    if not isinstance(f, dict) or not isinstance(f.get("path"), str):
        return
    path, mime = f["path"], str(f.get("mime", ""))
    if mime.startswith("video") or VIDEO_EXT_RE.search(path) or "youtube" in path or "youtu.be" in path:
        url = path if path.startswith("http") else base.rstrip("/") + "/" + path.lstrip("/")
        if url not in [v["url"] for v in out["videos"]]:
            out["videos"].append({"url": url, "title": "", "local": "" if path.startswith("http") else "1"})


def parse_h5p(html: str, base_url: str) -> List[Dict[str, Any]]:
    """Contenus H5P d'une page mod/hvp/view.php : bibliothèque, vidéos, textes, questions, export .h5p."""
    m = re.search(r"H5PIntegration\s*=\s*(\{.*?\});\s*(?:</script>|\n)", html or "", re.S)
    if not m:
        return []
    try:
        integ = json.loads(m.group(1))
    except ValueError:
        return []
    items = []
    for cid, c in (integ.get("contents") or {}).items():
        try:
            data = json.loads(c.get("jsonContent") or "{}")
        except ValueError:
            data = {}
        out: Dict[str, Any] = {"videos": [], "texts": [], "questions": []}
        base = c.get("contentUrl") or base_url
        _h5p_walk({"library": c.get("library", ""), "params": data}, out, base)
        items.append({"id": cid, "library": c.get("library", ""), "title": _h5p_text(c.get("title")),
                      "export_url": (c.get("exportUrl") or "").replace("\\/", "/"), **out})
    return items
