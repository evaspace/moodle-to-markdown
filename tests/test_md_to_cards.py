#!/usr/bin/env python3
"""Tests de md_to_cards.py — Passes A/B/C, validation, dédup, idempotence.

Exécution : .venv/bin/python -m unittest tests.test_md_to_cards -v
(aucun pytest installé ; unittest suffit, aucune dépendance ajoutée)
"""

import json
import shutil
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

import md_to_cards as mc
from md_converter import normalize_mathjax_tags

REPO = Path(__file__).resolve().parent.parent
MD = REPO / "EPITA_Moodle_Notes_MD"

# Fichiers représentatifs réels (en lecture seule)
F_PGCD = MD / "S1-MATHS-2030/11_Division euclidienne et PGCD/qcms/07_✅ QCM - PGCD, algorithme d'Euclide et nombres premiers entre eux.md"
F_ARITH = MD / "S1-MATHS-2030/10_Cours 3 - Arithmétique/qcms/02_✅ QCM - Motivation, divisibilité et division euclidienne.md"
F_STUB = MD / "S2-MATHS-2030/07_Cours 3 - Espaces vectoriels/qcms/13_✅ QCM Propriétés d'un espace vectoriel.md"
F_PARTIAL = MD / "S1-MATHS-2030/17_Cours 4 - Suites numériques/qcms/25_✅ QCM - Limite finie, limite infinie.md"
F_MATHJAX_PAGE = MD / "S2-MATHS-2030/07_Cours 3 - Espaces vectoriels/pages/57_Correction des exercices - somme et sev engendrés.md"


def fake_args(**kw):
    base = dict(limit=0, only="", retry_failed=False, force=False,
                dry_run=False, allow_llm=False, offline=False)
    base.update(kw)
    return SimpleNamespace(**base)


# --------------------------------------------------------------- Passe A ----
class TestPassANormalization(unittest.TestCase):
    def test_inline_tag(self):
        self.assertEqual(normalize_mathjax_tags("[mathjaxinline]126[/mathjaxinline]"),
                         "$126$")

    def test_block_tag(self):
        self.assertEqual(normalize_mathjax_tags("[mathjax]\\int_0^1 f[/mathjax]"),
                         "$$\\int_0^1 f$$")

    def test_multiline_content_intact(self):
        src = "[mathjaxinline]\\left\\{\\begin{array}{l} a=3\\\\ b=-1 \\end{array}\\right.[/mathjaxinline]"
        out = normalize_mathjax_tags(src)
        self.assertTrue(out.startswith("$") and out.endswith("$"))
        self.assertIn("\\begin{array}{l}", out)
        self.assertIn("a=3", out)

    def test_latex_commands_intact(self):
        src = "[mathjaxinline] \\frac{a}{b} \\neq \\beta [/mathjaxinline]"
        out = normalize_mathjax_tags(src)
        self.assertEqual(out, "$\\frac{a}{b} \\neq \\beta$")

    def test_no_tags_unchanged(self):
        text = "# Titre\n\n| a | b |\n|---|---|\n| 1 | 2 |\n\n```python\nx = 1\n```"
        self.assertEqual(normalize_mathjax_tags(text), text)

    def test_real_page_file(self):
        if not F_MATHJAX_PAGE.exists():
            self.skipTest("fichier représentatif absent")
        out = normalize_mathjax_tags(F_MATHJAX_PAGE.read_text(encoding="utf-8"))
        self.assertNotIn("[mathjaxinline]", out)
        self.assertNotIn("[/mathjaxinline]", out)
        self.assertIn("$", out)


# --------------------------------------------------------------- Passe B ----
class TestPassBRealFiles(unittest.TestCase):
    def test_full_score_real_qcm(self):
        """QCM à note pleine : [x] = bonne réponse, choix dédupliqués."""
        questions, rejects, skips = mc.parse_qcm_file(F_PGCD)
        self.assertEqual(skips, [])
        self.assertEqual(rejects, [])
        self.assertEqual(len(questions), 1)
        q = questions[0]
        self.assertEqual(q.number, 1)
        self.assertEqual(q.front, "Le PGCD de  $230$  et $126$ est")
        # 12 lignes d'options exportées en 3 exemplaires → 4 choix distincts
        self.assertEqual(len(q.choices), 4)
        self.assertEqual([c.text for c in q.choices],
                         ["$5$", "$1$", "$4$", "$2$"])
        correct = [c for c in q.choices if c.correct]
        self.assertEqual(len(correct), 1)
        self.assertEqual(correct[0].text, "$2$")
        # correction : lignes administratives retirées, LaTeX intact
        # (le nbsp est préservé tel quel, comme tout le contenu source)
        self.assertEqual(q.back, "La réponse correcte est\xa0:\n$2$")

    def test_mission_named_file_all_rejected(self):
        """Fichier « vrai QCM » de la mission : Q1 à choix vides (labels seuls),
        Q2 à note 0 → les deux questions sont REJETÉES, jamais publiées."""
        questions, rejects, skips = mc.parse_qcm_file(F_ARITH)
        self.assertEqual(skips, [])
        self.assertEqual(questions, [])
        self.assertEqual(len(rejects), 2)
        self.assertTrue(any("moins de 2 choix distincts" in r for r in rejects))
        self.assertTrue(any("note 0/1" in r for r in rejects))

    def test_stub_skipped(self):
        questions, rejects, skips = mc.parse_qcm_file(F_STUB)
        self.assertEqual(questions, [])
        self.assertEqual(rejects, [])
        self.assertEqual(len(skips), 1)
        self.assertIn("stub", skips[0])

    def test_partial_score_rejected(self):
        """Note partielle (0,67/1,00) : [x] = réponse de l'élève → rejet."""
        questions, rejects, skips = mc.parse_qcm_file(F_PARTIAL)
        self.assertTrue(any("0.67/1" in r for r in rejects),
                        msg=f"rejets : {rejects}")
        self.assertFalse(any("suite divergente" in q.front.lower()
                             for q in questions))


class TestPassBSynthetic(unittest.TestCase):
    def _write(self, text):
        d = Path(tempfile.mkdtemp())
        f = d / "qcm.md"
        f.write_text(text, encoding="utf-8")
        return f

    def test_multiple_correct_answers(self):
        f = self._write(
            "# T\n\n### Question1 (Note de 1,00 sur 1,00)\nCocher les vrais.\n\n"
            "**Options / Réponses :**\n"
            "- [x] a. Vrai chose\n- [ ] a. Vrai chose\n- [ ] Vrai chose\n"
            "- [x] b. Autre chose\n- [ ] b. Autre chose\n- [ ] Autre chose\n"
            "> **Correction / Feedback :**\n> Les deux sont vrais.\n")
        questions, rejects, _ = mc.parse_qcm_file(f)
        self.assertEqual(rejects, [])
        self.assertEqual(len(questions), 1)
        self.assertEqual(sorted(c.text for c in questions[0].choices if c.correct),
                         ["Autre chose", "Vrai chose"])

    def test_missing_correction_valid(self):
        """Correction absente : back vide, carte valide."""
        f = self._write(
            "# T\n\n### Question1 (Note de 1,00 sur 1,00)\nQuestion ?\n\n"
            "**Options / Réponses :**\n"
            "- [x] a. Bonne\n- [ ] a. Bonne\n- [ ] Bonne\n"
            "- [ ] b. Mauvaise\n- [ ] b. Mauvaise\n- [ ] Mauvaise\n")
        questions, rejects, _ = mc.parse_qcm_file(f)
        self.assertEqual(rejects, [])
        self.assertEqual(questions[0].back, "")

    def test_duplicate_labels_dedup(self):
        f = self._write(
            "# T\n\n### Question1 (Note de 1,00 sur 1,00)\nQ ?\n\n"
            "**Options / Réponses :**\n"
            "- [ ] a. texte A\n- [ ] a. texte A\n- [ ] texte A\n"
            "- [ ] b. texte B\n- [ ] b. texte B\n- [ ] texte B\n"
            "- [x] c. texte C\n- [ ] c. texte C\n- [ ] texte C\n"
            "> **Correction / Feedback :**\n> C est correct.\n")
        questions, rejects, _ = mc.parse_qcm_file(f)
        self.assertEqual(rejects, [])
        self.assertEqual(len(questions[0].choices), 3)
        self.assertTrue(questions[0].choices[2].correct)

    def test_label_only_choices_rejected(self):
        f = self._write(
            "# T\n\n### Question1 (Note de 1,00 sur 1,00)\nQ ?\n\n"
            "**Options / Réponses :**\n"
            "- [ ] a.\n- [ ] a.\n- [ ] a.\n"
            "- [x] b.\n- [ ] b.\n- [ ] b.\n"
            "> **Correction / Feedback :**\n> x\n")
        questions, rejects, _ = mc.parse_qcm_file(f)
        self.assertEqual(questions, [])
        self.assertTrue(any("moins de 2 choix distincts" in r for r in rejects))

    def test_latex_intact_through_pipeline(self):
        f = self._write(
            "# T\n\n### Question1 (Note de 1,00 sur 1,00)\n"
            "Valeur de [mathjaxinline]\\frac{1}{2}[/mathjaxinline] ?\n\n"
            "**Options / Réponses :**\n"
            "- [x] a. $\\frac{1}{2}$\n- [ ] a. $\\frac{1}{2}$\n- [ ] $\\frac{1}{2}$\n"
            "- [ ] b. $\\neq \\beta$\n- [ ] b. $\\neq \\beta$\n- [ ] $\\neq \\beta$\n"
            "> **Correction / Feedback :**\n> Car $\\frac{1}{2} \\neq \\beta$.\n")
        questions, rejects, _ = mc.parse_qcm_file(f)
        self.assertEqual(rejects, [])
        self.assertIn("$\\frac{1}{2}$", questions[0].front)
        self.assertIn("$\\frac{1}{2}$", questions[0].choices[0].text)
        self.assertIn("$\\frac{1}{2} \\neq \\beta$", questions[0].back)


# --------------------------------------------------- sérialisation / parse --
class TestBlockEmission(unittest.TestCase):
    def test_block_to_text_grammar(self):
        block = mc.CardBlock(
            category="Maths S1 - ARITH", subcategory="Cours 3 - Arithmétique",
            ctype="QCM", front="Le PGCD de $230$ et $126$ est",
            back="La réponse correcte est :\n\n$2$",
            choices=[mc.Choice("$2$", True), mc.Choice("$5$"),
                     mc.Choice("$1$"), mc.Choice("$4$")])
        text = mc.block_to_text(block)
        self.assertIn("CAT: Maths S1 - ARITH / Cours 3 - Arithmétique", text)
        self.assertIn("Q: [QCM] Le PGCD de $230$ et $126$ est", text)
        self.assertIn("C1: [x] $2$", text)
        self.assertIn("C2: $5$", text)
        self.assertIn("R: La réponse correcte est :\n\n$2$", text)
        self.assertTrue(text.rstrip().endswith("---"))

    def test_validate_with_real_parser(self):
        block = mc.CardBlock(
            category="Maths S1 - ARITH", subcategory="Cours 3 - Arithmétique",
            ctype="QCM", front="Le PGCD de $230$ et $126$ est",
            back="La réponse correcte est :\n\n$2$",
            choices=[mc.Choice("$2$", True), mc.Choice("$5$"),
                     mc.Choice("$1$"), mc.Choice("$4$")])
        n_cards, errors = mc.validate_with_parse_blocks(mc.block_to_text(block))
        self.assertEqual(errors, [])
        self.assertEqual(n_cards, 1)

    def test_parse_blocks_roundtrip_payload(self):
        block = mc.CardBlock(
            category="C", subcategory="S", ctype="QCM", front="Q ?",
            back="R", choices=[mc.Choice("oui", True), mc.Choice("non")])
        from app import parse_blocks
        cards, errors = parse_blocks(mc.block_to_text(block))
        self.assertEqual(errors, [])
        card = cards[0]
        self.assertEqual(card["type"], "QCM")
        self.assertEqual(card["front"], "Q ?")
        self.assertEqual(json.loads(card["payload"])["choices"],
                         [{"text": "oui", "correct": True},
                          {"text": "non", "correct": False}])

    def test_tf_and_course_blocks(self):
        tf = mc.CardBlock("C", "S", ctype="TF", front=" affirmation",
                          back="R", correct_bool=True)
        self.assertIn("Q: [TF]  affirmation", mc.block_to_text(tf))
        self.assertIn("A: Vrai", mc.block_to_text(tf))
        course = mc.CardBlock("C", "S", ctype="COURSE", front="Chapitre : X",
                                back="Résumé")
        self.assertIn("Q: Chapitre : X", mc.block_to_text(course))


# -------------------------------------------------------- catégories/clés ---
class TestCategoryResolver(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.resolver = mc.CategoryResolver(
            REPO / "selected_courses.json", REPO / "SYLLABUS_ORGANISATION.md")

    def test_multi_ecue_maths_s1(self):
        cat, sub = self.resolver.resolve("S1-MATHS-2030", "10_Cours 3 - Arithmétique")
        self.assertEqual((cat, sub), ("Maths S1 - ARITH", "Cours 3 - Arithmétique"))

    def test_multi_ecue_maths_s2(self):
        cat, sub = self.resolver.resolve("S2-MATHS-2030", "07_Cours 3 - Espaces vectoriels")
        self.assertEqual((cat, sub), ("Maths S2 - EV", "Cours 3 - Espaces vectoriels"))

    def test_single_ecue_folder(self):
        cat, sub = self.resolver.resolve("Archi S1 - Promo 2030", "01_Numération")
        self.assertEqual((cat, sub), ("Architecture S1", "Numération"))

    def test_unknown_folder_falls_back_to_raw(self):
        cat, sub = self.resolver.resolve("Inconnu - Promo 9999", "01_Chapitre")
        self.assertEqual((cat, sub), ("Inconnu - Promo 9999", "Chapitre"))

    def test_stable_key_normalization(self):
        self.assertEqual(
            mc.chapter_key("S1-MATHS-2030", "10_Cours 3 - Arithmétique"),
            "s1-maths-2030/cours-3-arithmetique")
        self.assertEqual(
            mc.chapter_key("[algo] TAA - Types algébriques abstraits",
                           "03_👨‍🏫 TAA - Cours - MiMos"),
            "algo-taa-types-algebriques-abstraits/taa-cours-mimos")

    def test_course_front_deterministic(self):
        self.assertEqual(mc.course_front("10_Cours 3 - Arithmétique"),
                         "Chapitre : Cours 3 - Arithmétique")
        self.assertEqual(mc.course_front("07_Cours 3 - Espaces vectoriels"),
                         "Chapitre : Cours 3 - Espaces vectoriels")


# ------------------------------------------------------------- Passe C ------
class TestEnsureCourseCard(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.index = mc.CourseIndex([])
        self.tracker = mc.Tracker(self.tmp / "tracker.json")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_existing_chapter_skipped(self):
        self.index = mc.CourseIndex([
            {"category": "Maths S1 - ARITH", "subcategory": "Cours 3 - Arithmétique",
             "type": "COURSE", "front": "Chapitre : Cours 3 - Arithmétique",
             "back": "x", "payload": "{}"}])
        chapter = self.tmp / "S1-MATHS-2030" / "10_Cours 3 - Arithmétique"
        chapter.mkdir(parents=True)
        status, block = mc.ensure_course_card(
            "Maths S1 - ARITH", "Cours 3 - Arithmétique", chapter,
            self.tmp, self.index, self.tracker)
        self.assertEqual(status, "SKIPPED_EXISTS")
        self.assertIsNone(block)
        self.assertEqual(self.tracker.data["chapters"][
            "s1-maths-2030/cours-3-arithmetique"]["status"], "SKIPPED_EXISTS")

    def test_empty_chapter_no_content(self):
        chapter = self.tmp / "X" / "99_Vide"
        chapter.mkdir(parents=True)
        status, _ = mc.ensure_course_card("X", "Vide", chapter,
                                          self.tmp, self.index, self.tracker)
        self.assertEqual(status, "NO_CONTENT")

    def test_new_chapter_pending_llm_without_allow(self):
        chapter = self.tmp / "X" / "01_Chapitre - Alpha"
        (chapter / "pages").mkdir(parents=True)
        (chapter / "pages" / "p1.md").write_text("# Alpha\n\nContenu $x$.\n",
                                                 encoding="utf-8")
        status, block = mc.ensure_course_card("X", "Chapitre - Alpha", chapter,
                                              self.tmp, self.index, self.tracker)
        self.assertEqual(status, "PENDING_LLM")  # dry-run : aucun appel LLM
        self.assertIsNone(block)


# ----------------------------------------------------------- dédup / front --
class TestDedup(unittest.TestCase):
    def setUp(self):
        self.index = mc.CourseIndex([])
        self.seen: set[tuple[str, str]] = set()

    def _block(self, front, back="R", n=1):
        return mc.CardBlock("C", "S", ctype="QCM", front=front, back=back,
                            number=n)

    def test_no_collision_keeps_front(self):
        b = self._block("Question unique")
        front, reason = mc.disambiguate_front(b, self.index, self.seen)
        self.assertEqual(front, "Question unique")
        self.assertIsNone(reason)

    def test_run_collision_reformulated(self):
        b1 = self._block("Même énoncé", back="R1", n=1)
        f1, _ = mc.disambiguate_front(b1, self.index, self.seen)
        self.seen.add(("QCM", f1))
        b2 = self._block("Même énoncé", back="R2", n=2)
        f2, reason = mc.disambiguate_front(b2, self.index, self.seen)
        self.assertNotEqual(f1, f2)  # les deux questions survivent
        self.assertIn("[Q2", f2)
        self.assertIsNotNone(reason)

    def test_db_collision_reformulated(self):
        self.index = mc.CourseIndex([
            {"category": "C", "subcategory": "S", "type": "QCM",
             "front": "Énoncé en base", "back": "autre", "payload": "{}"}])
        b = self._block("Énoncé en base", back="R")
        f2, reason = mc.disambiguate_front(b, self.index, self.seen)
        self.assertNotEqual(f2, "Énoncé en base")
        self.assertIsNotNone(reason)

    def test_exact_duplicate_detected(self):
        block = mc.CardBlock("C", "S", ctype="QCM", front="Doublon",
                             back="R", choices=[mc.Choice("a", True),
                                                mc.Choice("b")])
        self.index = mc.CourseIndex([
            {"category": "C", "subcategory": "S", "type": "QCM",
             "front": "Doublon", "back": "R",
             "payload": json.dumps({"choices": [
                 {"text": "a", "correct": True},
                 {"text": "b", "correct": False}]})}])
        self.assertTrue(self.index.exact_duplicate(block))
        block2 = mc.CardBlock("C", "S", ctype="QCM", front="Doublon",
                              back="R", choices=[mc.Choice("a", True),
                                                 mc.Choice("c")])
        self.assertFalse(self.index.exact_duplicate(block2))


# -------------------------------------------------------------- idempotence --
class TestIdempotence(unittest.TestCase):
    """Test d'idempotence obligatoire : 2e passage = 0 nouveau fichier,
    0 nouvelle carte."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.md = self.tmp / "MD"
        chapter = self.md / "CourseX" / "01_Chapitre - Alpha" / "qcms"
        chapter.mkdir(parents=True)
        (chapter / "01_✅ QCM Test.md").write_text(
            "# T\n\n### Question1 (Note de 1,00 sur 1,00)\nQ1 ?\n\n"
            "**Options / Réponses :**\n"
            "- [x] a. Bonne\n- [ ] a. Bonne\n- [ ] Bonne\n"
            "- [ ] b. Mauvaise\n- [ ] b. Mauvaise\n- [ ] Mauvaise\n"
            "> **Correction / Feedback :**\n> Expl.\n", encoding="utf-8")
        (chapter / "02_✅ QCM Test2.md").write_text(
            "# T\n\n### Question1 (Note de 1,00 sur 1,00)\nQ2 ?\n\n"
            "**Options / Réponses :**\n"
            "- [x] a. Vrai\n- [ ] a. Vrai\n- [ ] Vrai\n"
            "- [ ] b. Faux\n- [ ] b. Faux\n- [ ] Faux\n"
            "> **Correction / Feedback :**\n> Expl.\n", encoding="utf-8")
        self.out = self.tmp / "out"
        self.tracker_path = self.tmp / "tracker.json"
        self.index = mc.CourseIndex([])
        self.resolver = mc.CategoryResolver(
            REPO / "selected_courses.json", REPO / "SYLLABUS_ORGANISATION.md")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _run(self):
        tracker = mc.Tracker(self.tracker_path)
        return mc.run_pass_b(self.md, self.out, self.resolver, self.index,
                             tracker, fake_args())

    def test_second_run_produces_nothing_new(self):
        s1 = self._run()
        self.assertEqual(s1["files_written"], 2)
        self.assertEqual(s1["cards_qcm"], 2)
        written = sorted(p.name for p in self.out.glob("*.txt"))
        self.assertEqual(len(written), 2)

        s2 = self._run()
        self.assertEqual(s2["files_written"], 0)     # aucun nouveau fichier
        self.assertEqual(s2["cards_qcm"], 0)         # aucune nouvelle carte
        self.assertEqual(s2["files_done"], 2)
        written2 = sorted(p.name for p in self.out.glob("*.txt"))
        self.assertEqual(written2, written)          # contenu stable

        # et le contenu des fichiers est déterministe
        texts1 = {p.name: p.read_text(encoding="utf-8") for p in self.out.glob("*.txt")}
        self._run()
        texts2 = {p.name: p.read_text(encoding="utf-8") for p in self.out.glob("*.txt")}
        self.assertEqual(texts1, texts2)


# ------------------------------------------------- dedup au sein d'un lot --
class TestWithinRunDedup(unittest.TestCase):
    """Deux exports de la même tentative = mêmes cartes → le doublon
    est rejeté (une seule carte en ligne), pas reformulé."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.md = self.tmp / "MD"
        chapter = self.md / "CourseX" / "01_Chapitre - Alpha" / "qcms"
        chapter.mkdir(parents=True)
        qcm_text = (
            "# T\n\n### Question1 (Note de 1,00 sur 1,00)\nQ1 ?\n\n"
            "**Options / Réponses :**\n"
            "- [x] a. Bonne\n- [ ] a. Bonne\n- [ ] Bonne\n"
            "- [ ] b. Mauvaise\n- [ ] b. Mauvaise\n- [ ] Mauvaise\n"
            "> **Correction / Feedback :**\n> Expl.\n")
        (chapter / "01_✅ QCM Test.md").write_text(qcm_text,
                                                         encoding="utf-8")
        (chapter / "02_✅ QCM Test.md").write_text(qcm_text,
                                                         encoding="utf-8")
        # question distincte : même énoncé, autres choix
        (chapter / "03_✅ QCM Test.md").write_text(
            "# T\n\n### Question1 (Note de 1,00 sur 1,00)\nQ1 ?\n\n"
            "**Options / Réponses :**\n"
            "- [x] a. Autre bonne\n- [ ] a. Autre bonne\n- [ ] Autre bonne\n"
            "- [ ] b. Autre mauvaise\n- [ ] b. Autre mauvaise\n"
            "- [ ] Autre mauvaise\n"
            "> **Correction / Feedback :**\n> Expl.\n", encoding="utf-8")
        self.out = self.tmp / "out"
        self.tracker_path = self.tmp / "tracker.json"
        self.index = mc.CourseIndex([])
        self.resolver = mc.CategoryResolver(
            REPO / "selected_courses.json", REPO / "SYLLABUS_ORGANISATION.md")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _run(self):
        tracker = mc.Tracker(self.tracker_path)
        return mc.run_pass_b(self.md, self.out, self.resolver, self.index,
                             tracker, fake_args())

    def test_duplicate_exports_dropped_distinct_kept(self):
        s = self._run()
        # fichier 1 : 1 carte ; fichier 2 : doublon exact → rejeté ;
        # fichier 3 : même énoncé mais choix différents → conservé,
        # front reformulé pour différencier les deux questions distinctes
        self.assertEqual(s["cards_qcm"], 2)
        self.assertEqual(s["duplicates_dropped"], 1)
        self.assertEqual(s["fronts_reformulated"], 1)
        rejected = [k for k, v in
                      json.loads(self.tracker_path.read_text(
                          encoding="utf-8"))["files"].items()
                      if v["status"] == "REJECTED"]
        self.assertEqual(len(rejected), 1)
        self.assertIn("02_✅ QCM Test.md", rejected[0])
        # le front reformulé différencie bien les deux questions
        texts = [p.read_text(encoding="utf-8") for p in
                   sorted(self.out.glob("*.txt"))]
        self.assertEqual(len(texts), 2)
        self.assertTrue(any("[Q1·" in t for t in texts))


# ------------------------------------------------------- validation globale --
class TestFullPipelineValidation(unittest.TestCase):
    """Chaque .txt produit par la passe B doit passer parse_blocks() sans erreur."""

    def test_real_full_score_file_end_to_end(self):
        questions, rejects, _ = mc.parse_qcm_file(F_PGCD)
        self.assertEqual(rejects, [])
        resolver = mc.CategoryResolver(
            REPO / "selected_courses.json", REPO / "SYLLABUS_ORGANISATION.md")
        category, subcategory = resolver.resolve(
            "S1-MATHS-2030", "11_Division euclidienne et PGCD")
        blocks = [mc.question_to_block(q, category, subcategory)
                  for q in questions]
        text = "\n".join(mc.block_to_text(b) for b in blocks)
        n_cards, errors = mc.validate_with_parse_blocks(text)
        self.assertEqual(errors, [])
        self.assertEqual(n_cards, len(blocks))


if __name__ == "__main__":
    unittest.main()
