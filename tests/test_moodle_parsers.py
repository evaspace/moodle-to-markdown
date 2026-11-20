"""Tests hors ligne de moodle_parsers.py (aucun accès réseau, aucune API payante)."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import moodle_parsers as mp  # noqa: E402

BASE = "https://moodle.epita.fr"

COURSE_HTML = """
<html><head><title>Cours: S1-MATHS | Plateforme</title></head><body>
<h1 class="page-header-headings">S1-MATHS</h1>
<ul>
<li id="section-0" class="section main"><h3 class="sectionname">Général</h3>
  <ul>
  <li class="activity forum modtype_forum" id="module-10"><div class="activity-instance">
     <a class="aalink" href="/mod/forum/view.php?id=10"><span class="instancename">Annonces<span class="accesshide"> Forum</span></span></a></div></li>
  </ul></li>
<li id="section-1" class="section main"><h3 class="sectionname">Chapitre 1</h3>
  <div class="summary"><p>Résumé \\(x^2\\)</p></div>
  <ul>
  <li class="activity resource modtype_resource" id="module-11"><div class="activity-item"><div class="activity-instance">
     <a class="aalink" href="/mod/resource/view.php?id=11"><span class="instancename">Poly<span class="accesshide"> Fichier</span></span></a>
     <div class="activity-altcontent">desc</div></div></div></li>
  <li class="activity quiz modtype_quiz" id="module-12"><div class="activity-instance">
     <a class="aalink" href="/mod/quiz/view.php?id=12"><span class="instancename">QCM 1</span></a></div></li>
  <li class="activity label modtype_label" id="module-13"><div class="contentwithoutlink"><p>Texte libre</p></div></li>
  </ul></li>
</ul>
<a href="/mod/book/view.php?id=99">Livre caché hors section</a>
</body></html>
"""


class CourseTests(unittest.TestCase):
    def test_sections_and_modules_no_duplicates(self):
        c = mp.parse_course_page(COURSE_HTML, BASE, 5)
        self.assertEqual(c["fullname"], "S1-MATHS")
        names = [[m["name"] for m in s["modules"]] for s in c["sections"]]
        self.assertEqual(names[0], ["Annonces"])
        self.assertEqual(names[1], ["Poly", "QCM 1", "Note d'information"])
        types = [m["type"] for m in c["sections"][1]["modules"]]
        self.assertEqual(types, ["resource", "quiz", "label"])

    def test_orphan_module_is_kept(self):
        c = mp.parse_course_page(COURSE_HTML, BASE, 5)
        last = c["sections"][-1]
        self.assertEqual(last["name"], "Autres activités du cours")
        self.assertEqual(last["modules"][0]["id"], 99)

    def test_merge_adds_only_new_modules(self):
        a = mp.parse_course_page(COURSE_HTML, BASE, 5)
        b = mp.parse_course_page(COURSE_HTML, BASE, 5)
        before = sum(len(s["modules"]) for s in a["sections"])
        mp.merge_courses(a, b)
        self.assertEqual(before, sum(len(s["modules"]) for s in a["sections"]))


class LoginTests(unittest.TestCase):
    def test_login_detection(self):
        self.assertTrue(mp.is_login_page("<form id=\"login\">", BASE + "/x"))
        self.assertTrue(mp.is_login_page("", BASE + "/login/index.php"))
        self.assertTrue(mp.is_login_page("<input name=\"logintoken\">", ""))
        self.assertFalse(mp.is_login_page("<html>cours</html>", BASE + "/my/"))

    def test_sesskey(self):
        self.assertEqual(mp.extract_sesskey('M.cfg = {"sesskey":"AbC123xyz"}'), "AbC123xyz")
        self.assertEqual(mp.extract_sesskey('<a href="/login/logout.php?sesskey=Zz9988kk">'), "Zz9988kk")


class EmbeddedTests(unittest.TestCase):
    def test_assets_and_videos(self):
        html = f"""
        <p><img src="{BASE}/pluginfile.php/1/mod_page/content/3/fig.png">
        <a href="/pluginfile.php/1/mod_resource/content/1/cours.pdf">PDF</a>
        <video><source src="/pluginfile.php/1/mod_page/content/3/demo.mp4"></video>
        <iframe src="https://www.youtube.com/embed/abc"></iframe>
        <iframe src="https://pod.epita.fr/video/123/?is_iframe=true"></iframe>
        <a href="https://example.org/page">ext</a></p>"""
        r = mp.find_embedded(html, BASE)
        kinds = {a["filename"]: a["kind"] for a in r["assets"]}
        self.assertEqual(kinds["fig.png"], "image")
        self.assertEqual(kinds["cours.pdf"], "document")
        self.assertEqual(kinds["demo.mp4"], "video")
        urls = [v["url"] for v in r["videos"]]
        self.assertTrue(any("youtube" in u for u in urls))
        self.assertTrue(any("pod.epita.fr" in u for u in urls))
        self.assertTrue(any(u.endswith("demo.mp4") for u in urls))
        self.assertEqual(len(r["videos"]), 3)


class FolderBookTests(unittest.TestCase):
    def test_folder_subpath(self):
        html = f"""<div id="region-main">
        <a href="{BASE}/pluginfile.php/9/mod_folder/content/0/TD/Corr/td1.pdf?forcedownload=1">td1.pdf</a>
        <a href="{BASE}/pluginfile.php/9/mod_folder/content/0/enonce.pdf">enonce.pdf</a></div>"""
        files = mp.parse_folder_page(html, BASE)
        self.assertEqual({(f["filename"], f["subpath"]) for f in files},
                         {("td1.pdf", "TD/Corr"), ("enonce.pdf", "")})

    def test_book_toc(self):
        html = '<div class="book_toc"><a href="/mod/book/view.php?id=4&chapterid=7">Intro</a>' \
               '<a href="/mod/book/view.php?id=4&chapterid=8">Suite</a></div>'
        ch = mp.parse_book_toc(html, BASE)
        self.assertEqual([c["id"] for c in ch], ["7", "8"])

    def test_resource_page_object(self):
        html = f'<div id="region-main"><object data="{BASE}/pluginfile.php/1/mod_resource/content/1/a.pdf"></object></div>'
        self.assertEqual(mp.parse_resource_page(html, BASE)[0]["filename"], "a.pdf")


QUIZ_REVIEW = """
<div id="q1" class="que multichoice deferredfeedback incorrect">
  <div class="info"><h3 class="no">Question <span class="qno">1</span></h3>
    <div class="state">Incorrect</div><div class="grade">Note de 0,00 sur 1,00</div></div>
  <div class="content"><div class="formulation">
    <div class="qtext"><p>Combien font $1+1$ ?</p></div>
    <div class="ablock"><div class="answer">
      <div class="r0 incorrect"><input type="radio" checked="checked"><label><span class="answernumber">a. </span>3</label></div>
      <div class="r1 correct"><input type="radio"><label><span class="answernumber">b. </span>2</label></div>
      <div class="r0"><input type="radio"><label><span class="answernumber">c. </span>4</label></div>
    </div></div></div>
    <div class="outcome"><div class="rightanswer">La réponse correcte est : 2</div>
    <div class="generalfeedback">Car 1+1=2.</div></div></div></div>
<div id="q2" class="que multichoice deferredfeedback correct">
  <div class="info"><span class="qno">2</span><div class="state">Correct</div><div class="grade">Note de 1,00 sur 1,00</div></div>
  <div class="qtext"><p>Premiers ?</p></div>
  <div class="answer">
    <div class="r0 correct"><input type="checkbox" checked="checked"><label>2</label></div>
    <div class="r1 correct"><input type="checkbox" checked="checked"><label>3</label></div>
    <div class="r0"><input type="checkbox"><label>4</label></div></div>
  <div class="rightanswer">Les réponses correctes sont : 2, 3</div></div>
"""


class QuizTests(unittest.TestCase):
    def test_review_questions(self):
        qs = mp.parse_quiz_review(QUIZ_REVIEW, BASE)
        self.assertEqual(len(qs), 2)
        q1 = qs[0]
        self.assertEqual([a["text"] for a in q1["answers"]], ["3", "2", "4"])  # sans « a. », sans doublons
        self.assertEqual([a["checked"] for a in q1["answers"]], [True, False, False])
        self.assertEqual([a["correct"] for a in q1["answers"]], [False, True, False])
        self.assertIn("2", q1["right_answer"])
        self.assertIn("Car 1+1=2", q1["feedback_html"])
        self.assertEqual(sum(1 for a in qs[1]["answers"] if a["correct"]), 2)

    def test_correct_inferred_from_rightanswer_text(self):
        html = QUIZ_REVIEW.replace("incorrect\"", "\"").replace(" correct\"", "\"")
        html = html.replace('class="r0 "', 'class="r0"')
        qs = mp.parse_quiz_review(html, BASE)
        q1 = qs[0]
        self.assertTrue(any(a["correct"] for a in q1["answers"]))

    def test_merge_attempts_unions_correct_answers(self):
        a1 = mp.parse_quiz_review(QUIZ_REVIEW, BASE)
        a2 = mp.parse_quiz_review(QUIZ_REVIEW, BASE)
        a2[0]["answers"][2]["correct"] = True  # une autre tentative révèle « 4 » aussi
        m = mp.merge_quiz_attempts([a1, a2])
        self.assertEqual(len(m), 2)
        self.assertTrue(m[0]["answers"][2]["correct"])

    def test_quiz_page_lists_all_attempts(self):
        html = """<table class="quizattemptsummary">
        <a href="/mod/quiz/review.php?attempt=11&cmid=3">Revoir</a>
        <a href="/mod/quiz/review.php?attempt=12&cmid=3">Revoir</a>
        <a href="/mod/quiz/review.php?attempt=11&cmid=3">Revoir</a></table>"""
        q = mp.parse_quiz_page(html, BASE)
        self.assertEqual(len(q["review_urls"]), 2)
        self.assertIn("showall=1", mp.with_showall(q["review_urls"][0]))


class H5PTests(unittest.TestCase):
    def test_interactive_video_with_question(self):
        import json
        content = {"interactiveVideo": {"video": {"files": [{"path": "https://youtu.be/abc", "mime": "video/YouTube"}]},
                   "assets": {"interactions": [{"action": {"library": "H5P.MultiChoice 1.16", "params": {
                       "question": "<p>1+1 ?</p>", "answers": [{"text": "<div>2</div>", "correct": True},
                                                                 {"text": "<div>3</div>", "correct": False}]}}}]}}}
        integ = {"contents": {"cid-1": {"library": "H5P.InteractiveVideo 1.22", "title": "Titre &#039;x",
                                        "jsonContent": json.dumps(content), "exportUrl": "https:\\/\\/m\\/a.h5p"}}}
        html = "<script>H5PIntegration = " + json.dumps(integ) + ";\n</script>"
        it = mp.parse_h5p(html, BASE)[0]
        self.assertEqual(it["videos"][0]["url"], "https://youtu.be/abc")
        self.assertEqual(it["questions"][0]["answers"], [{"text": "2", "correct": True}, {"text": "3", "correct": False}])
        self.assertEqual(it["export_url"], "https://m/a.h5p")


if __name__ == "__main__":
    unittest.main()
