"""
Test de bout en bout du scrappeur contre un FAUX Moodle local (serveur HTTP en thread).
Aucun accès à moodle.epita.fr, aucune API payante. Vérifie : découverte des cours via AJAX,
tous les types de modules, téléchargements, QCM multi-tentatives, médias embarqués réécrits,
détection de session expirée, et que md_to_cards lit la sortie.
"""
import json
import os
import sys
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from exporter import CourseExporter  # noqa: E402
from moodle_client import MoodleClient, SessionExpired  # noqa: E402

PDF = b"%PDF-1.4 fake pdf content " * 20
PNG = b"\x89PNG\r\n\x1a\n" + b"0" * 64
MP4 = b"\x00\x00\x00\x18ftypmp42" + b"1" * 256
STATE = {"expired": False}


def page(body: str, extra_js: str = "") -> bytes:
    return (f'<html><head><title>x</title></head><body>'
            f'<script>M.cfg = {{"sesskey":"SESS12345"}};{extra_js}</script>{body}</body></html>').encode()


COURSE = """
<h1 class="page-header-headings">S1-TEST</h1>
<ul>
<li id="section-1" class="section main"><h3 class="sectionname">Chapitre 1</h3>
 <ul>
  <li class="activity resource modtype_resource" id="module-11"><a class="aalink" href="/mod/resource/view.php?id=11"><span class="instancename">Poly<span class="accesshide"> Fichier</span></span></a></li>
  <li class="activity folder modtype_folder" id="module-12"><a class="aalink" href="/mod/folder/view.php?id=12"><span class="instancename">TD</span></a></li>
  <li class="activity page modtype_page" id="module-13"><a class="aalink" href="/mod/page/view.php?id=13"><span class="instancename">Cours en ligne</span></a></li>
  <li class="activity quiz modtype_quiz" id="module-14"><a class="aalink" href="/mod/quiz/view.php?id=14"><span class="instancename">QCM 1</span></a></li>
  <li class="activity book modtype_book" id="module-15"><a class="aalink" href="/mod/book/view.php?id=15"><span class="instancename">Livre</span></a></li>
  <li class="activity url modtype_url" id="module-16"><a class="aalink" href="/mod/url/view.php?id=16"><span class="instancename">Vidéo cours</span></a></li>
  <li class="activity lesson modtype_lesson" id="module-17"><a class="aalink" href="/mod/lesson/view.php?id=17"><span class="instancename">Leçon</span></a></li>
 </ul></li></ul>
"""

REVIEW = lambda sel_b, sel_c, state: f"""
<div class="que multichoice incorrect"><div class="info"><span class="qno">1</span>
<div class="state">{state}</div><div class="grade">Note de 0,00 sur 1,00</div></div>
<div class="qtext"><p>Combien font 1+1 ?</p></div>
<div class="answer">
 <div class="r0 {'incorrect' if sel_b else ''}"><input type="radio" {'checked="checked"' if sel_b else ''}><label><span class="answernumber">a. </span>3</label></div>
 <div class="r1 {'correct' if sel_c else ''}"><input type="radio" {'checked="checked"' if sel_c else ''}><label><span class="answernumber">b. </span>2</label></div>
</div><div class="rightanswer">La réponse correcte est : 2</div></div>"""


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def send(self, code=200, body=b"", ctype="text/html; charset=utf-8", headers=None):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        for k, v in (headers or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        n = int(self.headers.get("Content-Length", 0))
        req = json.loads(self.rfile.read(n) or b"[]")
        m = req[0]["methodname"]
        if "SESS12345" not in self.path or m != "core_course_get_enrolled_courses_by_timeline_classification":
            return self.send(200, json.dumps([{"error": True, "exception": {}}]).encode(), "application/json")
        data = {"courses": [{"id": 7, "fullname": "S1-TEST", "shortname": "S1T"}], "nextoffset": 0}
        self.send(200, json.dumps([{"error": False, "data": data}]).encode(), "application/json")

    def do_GET(self):
        p = self.path
        host = f"http://127.0.0.1:{self.server.server_port}"
        if STATE["expired"] and "/pluginfile" in p:
            return self.send(200, b'<html><form id="login"><input name="logintoken"></form></html>')
        if p.startswith("/my/"):
            return self.send(200, page('<span class="usertext">Eleve Test</span>'))
        if p.startswith("/course/view.php?id=7"):
            return self.send(200, page(COURSE))
        if p.startswith("/course/resources.php"):
            return self.send(200, page('<a href="/mod/lesson/view.php?id=18">Annexe orpheline</a>'))
        if p.startswith("/mod/resource/view.php?id=11"):
            return self.send(302, b"", headers={"Location": "/pluginfile.php/1/mod_resource/content/1/poly.pdf"})
        if p.startswith("/pluginfile.php") and p.split("?")[0].endswith(".pdf"):
            return self.send(200, PDF, "application/pdf")
        if p.startswith("/pluginfile.php") and p.split("?")[0].endswith(".png"):
            return self.send(200, PNG, "image/png")
        if p.startswith("/pluginfile.php") and p.split("?")[0].endswith(".mp4"):
            return self.send(200, MP4, "video/mp4")
        if p.startswith("/mod/folder/view.php"):
            return self.send(200, page(
                '<div id="region-main">'
                f'<a href="{host}/pluginfile.php/2/mod_folder/content/0/Corriges/td1.pdf">td1.pdf</a>'
                f'<a href="{host}/pluginfile.php/2/mod_folder/content/0/enonce.pdf">enonce.pdf</a></div>'))
        if p.startswith("/mod/page/view.php"):
            return self.send(200, page(
                '<div class="generalbox"><p>Théorème \\(x^2\\)</p>'
                f'<img src="{host}/pluginfile.php/3/mod_page/content/1/schema.png">'
                f'<iframe src="https://www.youtube.com/embed/abc123"></iframe>'
                f'<video><source src="{host}/pluginfile.php/3/mod_page/content/1/demo.mp4"></video></div>'))
        if p.startswith("/mod/quiz/view.php"):
            return self.send(200, page(
                '<div id="intro"><p>Consignes</p></div><table class="quizattemptsummary">'
                '<a href="/mod/quiz/review.php?attempt=21&cmid=14">Revoir</a>'
                '<a href="/mod/quiz/review.php?attempt=22&cmid=14">Revoir</a></table>'))
        if p.startswith("/mod/quiz/review.php?attempt=21") or p.startswith("/mod/quiz/review.php?showall=1&attempt=21") \
                or "attempt=21" in p:
            return self.send(200, page(REVIEW(True, False, "Incorrect")))
        if "attempt=22" in p:
            return self.send(200, page(REVIEW(False, True, "Correct").replace("incorrect", "correct")))
        if p.startswith("/mod/book/view.php") and "chapterid" not in p:
            return self.send(200, page('<div class="book_toc"><a href="/mod/book/view.php?id=15&chapterid=1">Intro</a>'
                                       '<a href="/mod/book/view.php?id=15&chapterid=2">Suite</a></div>'
                                       '<div class="book_content"><p>Chapitre un</p></div>'))
        if p.startswith("/mod/book/view.php") and "chapterid=2" in p:
            return self.send(200, page('<div class="book_content"><p>Chapitre deux $a+b$</p></div>'))
        if p.startswith("/mod/book/view.php"):
            return self.send(200, page('<div class="book_content"><p>Chapitre un</p></div>'))
        if p.startswith("/mod/url/view.php"):
            return self.send(302, b"", headers={"Location": "https://www.youtube.com/watch?v=zzz"})
        if p.startswith("/mod/lesson/view.php?id=17"):
            return self.send(200, page(
                '<div id="region-main"><p>Contenu de leçon</p>'
                f'<a href="{host}/pluginfile.php/4/mod_lesson/content/1/annexe.pdf">annexe</a></div>'))
        if p.startswith("/mod/lesson/view.php?id=18"):
            return self.send(200, page('<div id="region-main"><p>Orpheline</p></div>'))
        self.send(404, b"nope")


class E2E(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.srv = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        threading.Thread(target=cls.srv.serve_forever, daemon=True).start()
        cls.base = f"http://127.0.0.1:{cls.srv.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.srv.shutdown()

    def setUp(self):
        STATE["expired"] = False
        self.tmp = tempfile.TemporaryDirectory()
        self.out = os.path.join(self.tmp.name, "out")
        self.client = MoodleClient(self.base, session_cookie="abc", min_delay=0)

    def tearDown(self):
        self.tmp.cleanup()

    def export(self, videos=False):
        ok, msg = self.client.validate_auth()
        self.assertTrue(ok, msg)
        courses = self.client.get_enrolled_courses()
        self.assertEqual([c["id"] for c in courses], [7])
        data = self.client.get_course_details(7)
        ex = CourseExporter(self.client, self.out, True, videos, os.path.join(self.tmp.name, "state.json"), workers=3)
        stats = ex.export_course(data)
        return ex, stats, data

    def test_full_export(self):
        ex, stats, data = self.export(videos=True)
        root = Path(self.out) / "S1-TEST"
        files = {p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file()}
        joined = "\n".join(sorted(files))
        # fichiers (resource redirigée, dossier avec sous-dossier), médias de page, vidéo locale
        self.assertIn("poly.pdf", joined)
        self.assertTrue(any(f.endswith("Corriges/td1.pdf") for f in files), joined)
        self.assertTrue(any(f.endswith("enonce.pdf") for f in files), joined)
        self.assertTrue(any(f.endswith("medias/schema.png") for f in files), joined)
        self.assertTrue(any(f.endswith("demo.mp4") for f in files), joined)
        self.assertTrue(any(f.endswith("annexe.pdf") for f in files), joined)
        # modules sans traitement dédié + module orphelin de /course/resources.php
        mds = "\n".join(p.read_text() for p in root.rglob("*.md"))
        self.assertIn("Contenu de leçon", mds)
        self.assertIn("Orpheline", mds)
        # livre : 2 chapitres
        self.assertIn("Chapitre un", mds)
        self.assertIn("Chapitre deux $a+b$", mds)
        # page : lien local vers l'image, plus d'URL du serveur pour le média
        page_md = next(root.rglob("*Cours en ligne*.md")).read_text()
        self.assertIn("../medias/schema.png", page_md)
        self.assertNotIn("pluginfile.php/3/mod_page/content/1/schema.png", page_md)
        self.assertIn("youtube.com/embed/abc123", page_md)
        # vidéo d'un mod_url
        self.assertIn("youtube.com/watch?v=zzz", mds)
        # manifeste + rapport
        report = ex.write_report([{"id": 7}], {"7": stats})
        self.assertTrue(os.path.exists(report))
        manifest = json.load(open(os.path.join(self.out, "manifest.json")))
        self.assertTrue(any(m["type"] == "qcm" for m in manifest))
        # seules les vidéos externes (YouTube) peuvent échouer : le test n'utilise pas Internet
        self.assertTrue(all("youtube.com" in f["url"] for f in ex.failures), ex.failures)
        self.assertTrue(all(f["reason"] for f in ex.failures))

    def test_quiz_attempts_merged_and_parsed_by_md_to_cards(self):
        ex, stats, _ = self.export()
        qfile = next((Path(self.out) / "S1-TEST").rglob("qcms/*.md"))
        text = qfile.read_text()
        self.assertEqual(stats["questions"], 1)           # 2 tentatives -> 1 question fusionnée
        self.assertIn("**Réponses correctes :**", text)
        self.assertIn("- ✔ 2", text)
        self.assertEqual(text.count("- [ ] 3") + text.count("- [x] 3"), 1)  # pas de doublon d'options
        import md_to_cards
        questions, rejects, skips = md_to_cards.parse_qcm_file(qfile)
        self.assertEqual(len(questions), 1, (rejects, skips))
        q = questions[0]
        self.assertEqual([c.correct for c in q.choices], [False, True])

    def test_expired_session_is_detected_not_saved(self):
        self.client.validate_auth()
        STATE["expired"] = True
        ex = CourseExporter(self.client, self.out, True, False, os.path.join(self.tmp.name, "s.json"))
        data = {"id": 7, "fullname": "X", "summary": "", "url": "", "sections": [
            {"section_number": 1, "name": "S", "summary_html": "", "modules": [
                {"id": 1, "name": "f", "type": "resource", "url": "", "description": "", "extra": {},
                 "contents": [{"filename": "a.pdf", "fileurl": f"{self.base}/pluginfile.php/1/a.pdf"}]}]}]}
        with self.assertRaises(SessionExpired):
            ex.export_course(data)
        self.assertFalse(any(p.suffix == ".pdf" for p in Path(self.out).rglob("*")))


if __name__ == "__main__":
    unittest.main()
