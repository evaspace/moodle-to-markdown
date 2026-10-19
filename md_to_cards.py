#!/usr/bin/env python3
"""
md_to_cards.py — Convertisseur Markdown EPITA → blocs de cartes MathsDoomscroll.

Cible : le format texte interprété par parse_blocks() (app.py:71).
L'application NE LIT AUCUN JSON de cartes ; le LaTeX reste en texte brut.

Pipeline en 3 passes :

  Passe A  Normalisation mathématique (déterministe, 0 token)
           [mathjaxinline]X[/mathjaxinline] -> $X$
           [mathjax]X[/mathjax]             -> $$X$$
           (md_converter.normalize_mathjax_tags)

  Passe B  Extraction QCM réels (déterministe, 0 token)
           Un fichier qcms/*.md est un vrai QCM s'il contient des titres
           « ### Question N (Note …) » ET des lignes de choix « - [x]/- [ ] ».
           SEULES les questions à note PLEINE sont extraites : dans ces
           exports Moodle, [x] marque la réponse SÉLECTIONNÉE par l'élève.
           À note pleine, l'élève a tout bon donc [x] = bonne réponse.
           À note partielle/nulle/« Non noté », [x] = réponse de l'élève
           (souvent fausse) : la question est REJETÉE, jamais publiée avec
           une « bonne réponse » erronée. Ces questions sont candidates pour
           une passe LLM future.
           Les options sont exportées 3 fois (label « a. », label « a. »,
           sans label) : déduplication sur le texte, [x] combiné (OU).

  Passe C  Cartes COURSE par chapitre (existence + génération)
           ensure_course_card() consulte un INDEX EN LECTURE SEULE de la
           base SERVEUR (SELECT via ssh + docker exec, jamais d'écriture).
           Clé stable dérivée du chemin (minuscules, sans accents, sans
           préfixe numérique, séparateurs unifiés) — aucune comparaison de
           titres bruts.
           Front déterministe : « Chapitre : <titre> » pour que la dédup
           (type, front) fonctionne à chaque relance.
           Un cours existe si (catégorie, sous-catégorie) est présent AVEC
           au moins une carte COURSE → SKIPPED_EXISTS.
           Le résumé (R:) est sémantique : il n'est produit que par un LLM,
           uniquement avec --allow-llm après validation du tier gratuit
           (contrainte de coût zéro). Sans LLM : dry-run, statut PENDING_LLM.

Options CLI : --limit N, --only SUBSTR, --retry-failed, --dry-run,
              --only-pass ab, --allow-llm, --offline (index local),
              --refresh-index, --force.

Reprise : tracker md_to_cards_progress.json (DONE / SKIPPED / SKIPPED_EXISTS
          / PENDING_LLM / FAILED / REJECTED) sauvegardé atomiquement.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import re
import subprocess
import sys

from dotenv import load_dotenv
load_dotenv()
import time
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

from md_converter import normalize_mathjax_tags

# ------------------------------------------------------------------ constantes --
DEFAULT_INPUT_DIR = "EPITA_Moodle_Notes_MD"
DEFAULT_OUTPUT_DIR = "Generated_QCMs"
TRACKER_FILE = "md_to_cards_progress.json"
INDEX_FILE = "course_index.json"
SELECTED_COURSES = "selected_courses.json"
SYLLABUS = "SYLLABUS_ORGANISATION.md"
MAX_CHUNK_CHARS = 14000  # generate_qcms.py:295 — troncature sécurisée tokens
REMOTE_HOST = "hetzner"
REMOTE_CONTAINER = "mathsdoomscroll_app"
REMOTE_DB = "/app/cards.db"

# ------------------------------------------------------- Pass C v2 — modèles --
# Mapping user-proposed names → valid Mistral API model IDs (docs.mistral.ai/models).
# User proposed: mistral-large-2512, codestral-2508, ministral-14b-2512,
#                mistral-medium-latest, ministral-8b-2512
# Valid API IDs resolve these to the versioned names; "mistral-medium-latest"
# does not exist — mapped to the deprecated mistral-medium-2508 (Aug 2025 retire).
MISTRAL_MODEL_ALIASES = {
    "mistral-large-2512": "mistral-large-2411",
    "mistral-large-latest": "mistral-large-latest",
    "codestral-2508": "codestral-2405",
    "codestral-latest": "codestral-2405",
    "ministral-14b-2512": "open-mistral-nemo-2407",
    "ministral-8b-2512": "open-mistral-nemo-2407",
    "ministral-8b-latest": "open-mistral-nemo-2407",
    "mistral-medium-latest": "mistral-medium-latest",
}

# Rotation de génération : 1 modèle par chapitre.
# Trié du plus économique au plus performant (input $/M tokens).
# Source : docs.mistral.ai/inference/pricing (2026-10-13)
# NOTE : La clé API utilisée est en tier "Experiment/Limited" — les modèles
# récents (ministral-3-*, codestral-25-08, mistral-large-3, etc.) retournent
# HTTP 400 "Invalid model". Les modèles disponibles sont :
#   - open-mistral-nemo-2407  : $0.15 / $0.15 (32K ctx, 7B, open-weight)
#   - mistral-small-latest    : $0.15 / $0.60 (32K ctx, 24B, deprecated mais actif)
#   - mistral-medium-latest   : $1.50 / $7.50 (32K ctx, 32B, le plus performant dispo)
DEFAULT_GENERATION_MODELS = [
    "open-mistral-nemo-2407",
    "mistral-small-latest",
    "mistral-medium-latest",
]

# Modèle de vérification : distinct du modèle de génération,
# coût marginal minimal (nemo 2407 le plus économique et disponible).
DEFAULT_VERIFY_MODEL = "open-mistral-nemo-2407"

# Rate limiting : 60 % des limites publiques.
# Mistral publie des limites par modèle; on impose une marge de sécurité
# pour éviter le 429 sur les pics. Valeurs typiques :
#   Nemo 2407 / Small : 300 RPM, 400k TPM
# On rate-limits à 60 % de la limite la plus restrictive pour rester conservatif.
SAFE_DELAY_BETWEEN_CALLS = float(os.getenv("MISTRAL_DELAY", "0.3"))
VERIFY_DELAY = float(os.getenv("MISTRAL_VERIFY_DELAY", "0.3"))
TPM_CAP = int(os.getenv("MISTRAL_TPM_CAP", "300000"))

# --------------------------------------------------------------- Passe B ----
Q_HEAD_RE = re.compile(r"^###\s+Question\s*(\d+)?\s*(?:\((.*?)\))?\s*$", re.I)
NOTE_RE = re.compile(r"Note\s+de\s+([\d]+[.,]\d+)\s+sur\s+([\d]+[.,]\d+)", re.I)
CHOICE_RE = re.compile(r"^-\s+\[(x| )\]\s*(.*)$")
OPTIONS_HEADER_RE = re.compile(r"^\*\*Options\s*/\s*Réponses\s*:\*\*\s*$")
FEEDBACK_HEADER_RE = re.compile(r"^(?:>\s*)?\*\*Correction\s*/\s*Feedback\s*:\*\*\s*$")
CHOICE_LABEL_RE = re.compile(r"^[a-z]\.\s*")
ADMIN_LINE_RE = re.compile(
    r"^(?:Correct|Incorrect|Partially correct\b|"
    r"Votre réponse est (?:correcte|incorrecte|partiellement correcte)\.?|"
    r"Vous en avez sélectionné correctement\s+\d+|"
    r"(?:Note|Points) pour cet envoi\s*:.*)$",
    re.I,
)


@dataclass
class Choice:
    text: str
    correct: bool = False


@dataclass
class Question:
    number: int | None
    front: str
    choices: list[Choice]
    back: str


@dataclass
class CardBlock:
    category: str
    subcategory: str
    ctype: str  # 'QCM' | 'TF' | 'COURSE'
    front: str
    back: str = ""
    choices: list[Choice] = field(default_factory=list)  # QCM
    correct_bool: bool | None = None                     # TF
    number: int | None = None                            # n° question source


# ----------------------------------------------------------- Passe B : parse --
def parse_score(note: str | None) -> tuple[float, float] | None:
    m = NOTE_RE.search(note or "")
    if not m:
        return None
    return (float(m.group(1).replace(",", ".")),
            float(m.group(2).replace(",", ".")))


def split_question_blocks(lines: list[str]) -> list[list[str]]:
    """Découpe la section « Questions & Corrigé » en blocs par « ### Question »."""
    blocks: list[list[str]] = []
    current: list[str] = []
    for line in lines:
        if Q_HEAD_RE.match(line.strip()):
            if current:
                blocks.append(current)
            current = [line]
        elif current:
            if line.strip().startswith("## "):  # fin de section (Mes Notes…)
                blocks.append(current)
                current = []
            else:
                current.append(line)
    if current:
        blocks.append(current)
    return blocks


def parse_question(block: list[str]) -> tuple[Question | None, str | None]:
    """Parse un bloc « ### Question ». Retourne (Question, None) ou (None, raison)."""
    head = Q_HEAD_RE.match(block[0].strip())
    number = int(head.group(1)) if head.group(1) else None
    score = parse_score(head.group(2))
    if score is None:
        return None, "note illisible (impossible de certifier que [x] = correction)"
    got, mx = score
    if got < mx:
        return None, (
            f"note {got:g}/{mx:g} : [x] = réponse sélectionnée par l'élève, "
            "pas la correction (question rejetée, candidate LLM)"
        )

    # texte de la question = entre le titre et « **Options / Réponses :** »
    qlines: list[str] = []
    opt_idx = None
    for i in range(1, len(block)):
        if OPTIONS_HEADER_RE.match(block[i].strip()):
            opt_idx = i
            break
        qlines.append(block[i])
    if opt_idx is None:
        return None, "pas d'en-tête « **Options / Réponses :** » (question ouverte)"
    front = "\n".join(l for l in qlines if l.strip()).strip()
    if not front:
        return None, "énoncé de question vide"

    # choix : lignes « - [x]/- [ ] » consécutives, dédupliquées sur le texte
    choices: list[Choice] = []
    seen: dict[str, int] = {}
    for line in block[opt_idx + 1:]:
        m = CHOICE_RE.match(line.strip())
        if not m:
            break  # fin de la liste de choix
        marked = m.group(1) == "x"
        text = CHOICE_LABEL_RE.sub("", m.group(2).strip()).strip()
        if not text:
            continue  # choix dégénéré (« a. » seul, sans contenu)
        key = re.sub(r"\s+", " ", text).casefold()
        if key in seen:
            if marked:
                choices[seen[key]].correct = True  # OU sur les doublons
            continue
        seen[key] = len(choices)
        choices.append(Choice(text=text, correct=marked))

    if len(choices) < 2:
        return None, f"moins de 2 choix distincts exploitables ({len(choices)})"
    if not any(c.correct for c in choices):
        return None, "aucune option cochée [x] à note pleine"

    # correction = bloc « > **Correction / Feedback :** » jusqu'à fin de bloc
    back_lines: list[str] = []
    in_fb = False
    for line in block[opt_idx + 1:]:
        if FEEDBACK_HEADER_RE.match(line.strip()):
            in_fb = True
            continue
        if not in_fb:
            continue
        s = line.strip()
        if s.startswith("> "):
            s = s[2:].strip()
        elif s == ">":
            s = ""
        if s and not ADMIN_LINE_RE.match(s):
            back_lines.append(s)
    back = re.sub(r"\n{3,}", "\n\n", "\n".join(back_lines)).strip()

    return Question(number=number, front=front, choices=choices, back=back), None


def parse_qcm_file(path: Path) -> tuple[list[Question], list[str], list[str]]:
    """Retourne (questions valides, rejets, motifs de saut) pour un fichier."""
    raw = path.read_text(encoding="utf-8", errors="replace")
    text = normalize_mathjax_tags(raw)
    lines = text.splitlines()
    has_head = any(Q_HEAD_RE.match(l.strip()) for l in lines)
    has_choices = any(CHOICE_RE.match(l.strip()) for l in lines)
    if not has_head:
        return [], [], ["stub de métadonnées : aucune question"]
    if not has_choices:
        return [], [], ["questions ouvertes sans options (pas un QCM à choix)"]

    questions, rejects = [], []
    for block in split_question_blocks(lines):
        q, reason = parse_question(block)
        if q is None:
            rejects.append(f"{block[0].strip()[:70]} → {reason}")
        else:
            questions.append(q)
    return questions, rejects, []


# ------------------------------------------------------- Passe B : émission --
def question_to_block(q: Question, category: str, subcategory: str) -> CardBlock:
    ordered = sorted(q.choices, key=lambda c: (not c.correct,))
    return CardBlock(category=category, subcategory=subcategory, ctype="QCM",
                     front=q.front, back=q.back, choices=ordered,
                     number=q.number)


def block_to_text(b: CardBlock) -> str:
    """Sérialise au format exact attendu par parse_blocks() (app.py:71)."""
    out = [f"CAT: {b.category} / {b.subcategory}"]
    if b.ctype == "QCM":
        out.append(f"Q: [QCM] {b.front}")
        for i, c in enumerate(b.choices, 1):
            mark = "[x] " if c.correct else ""
            out.append(f"C{i}: {mark}{c.text}")
    elif b.ctype == "TF":
        out.append(f"Q: [TF] {b.front}")
        out.append(f"A: {'Vrai' if b.correct_bool else 'Faux'}")
    else:  # COURSE
        out.append(f"Q: {b.front}")
    out.append(f"R: {b.back}")
    out.append("---")
    return "\n".join(out)


# ------------------------------------------- résolution catégories canoniques --
def strip_chapter_prefix(name: str) -> str:
    """« 10_Cours 3 - Arithmétique » → « Cours 3 - Arithmétique »
    (même regex que generate_qcms.py:288-290)."""
    if name and name[0].isdigit():
        return re.sub(r"^\d+_[^a-zA-Z0-9]*\s*", "", name) or name
    return name


class CategoryResolver:
    """Catégories canoniques via selected_courses.json + SYLLABUS_ORGANISATION.md.

    selected_courses.json mappe source_folder → category_name, mais plusieurs
    ECUE partagent un dossier (S1-MATHS-2030 = OBM+DP+ARITH+SR). Pour ceux-
    là, SYLLABUS_ORGANISATION.md fournit la table chapitre → ECUE.
    """

    def __init__(self, selected_path: Path, syllabus_path: Path):
        self.courses_by_folder: dict[str, list[dict]] = {}
        self.course_by_ecue: dict[str, dict] = {}
        if selected_path.exists():
            data = json.loads(selected_path.read_text(encoding="utf-8"))
            for domain in data.get("domains", []):
                for c in domain.get("courses", []):
                    self.courses_by_folder.setdefault(
                        c.get("source_folder", ""), []).append(c)
                    if c.get("ecue_code"):
                        self.course_by_ecue[c["ecue_code"]] = c
        self.chapter_ecue: dict[tuple[str, str], str] = {}
        self.folder_ecue: dict[str, str] = {}
        if syllabus_path.exists():
            self._parse_syllabus(syllabus_path)

    def _parse_syllabus(self, path: Path) -> None:
        current_source: str | None = None
        for raw in path.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            m = re.match(r"Dossier source\s*:\s*`([^`]+)`", line)
            if m:
                current_source = m.group(1).split("EPITA_Moodle_Notes_MD/")[-1].rstrip("/")
                continue
            if not line.startswith("|"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if not cells:
                continue
            first = cells[0].replace("*", "").replace("`", "").strip()
            if first in ("Code ECUE", "") or set(first) <= {"-", ":", " "}:
                continue  # ligne d'en-tête ou séparateur
            if not re.fullmatch(r"[A-Z][A-Z0-9\-]*", first):
                continue  # pas un code ECUE
            ecue = first
            for tok in re.findall(r"`([^`]+)`", line):
                tok = tok.strip()
                if tok.endswith("/"):          # colonne « Dossier source Moodle »
                    self.folder_ecue[tok.rstrip("/")] = ecue
                elif current_source:           # colonne « Chapitres Moodle »
                    self.chapter_ecue[(current_source, tok)] = ecue

    def resolve(self, folder: str, chapter: str | None = None) -> tuple[str, str]:
        """Retourne (catégorie canonique, sous-catégorie)."""
        subcategory = strip_chapter_prefix(chapter) if chapter else "Général"
        ecue = self.chapter_ecue.get((folder, chapter)) if chapter else None
        if ecue is None:
            ecue = self.folder_ecue.get(folder)
        course = self.course_by_ecue.get(ecue) if ecue else None
        if course is None:
            entries = self.courses_by_folder.get(folder, [])
            course = entries[0] if len(entries) == 1 else None
        category = course["category_name"] if course else folder
        return category, subcategory


# -------------------------------------------------- clés stables et titres --
def normalize_key(s: str) -> str:
    """Clé stable : minuscules, sans accents, sans préfixe numérique,
    espaces/tirets unifiés (jamais de comparaison de titres bruts)."""
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    s = re.sub(r"^\d+_", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def chapter_key(folder: str, chapter: str) -> str:
    return f"{normalize_key(folder)}/{normalize_key(chapter)}"


def clean_chapter_title(chapter: str) -> str:
    return re.sub(r"\s+", " ", strip_chapter_prefix(chapter)).strip()


def course_front(chapter: str) -> str:
    """Front déterministe d'une carte COURSE de chapitre (dédup type, front)."""
    return f"Chapitre : {clean_chapter_title(chapter)}"


# ------------------------------------------- index SERVEUR (lecture seule) --
COURSE_INDEX_SQL = (
    "SELECT cat.name AS category, sc.name AS subcategory, "
    "c.type, c.front, c.back, c.payload "
    "FROM card c "
    "JOIN subcategory sc ON sc.id = c.subcategory_id "
    "JOIN category cat ON cat.id = sc.category_id"
)


class CourseIndex:
    """Snapshot en lecture seule de la base SERVEUR (la seule source de vérité).

    Le cards.db local n'est JAMAIS utilisé : il peut différer de la prod.
    """

    def __init__(self, rows: list[dict]):
        self.rows = rows
        self.course_cards: set[tuple[str, str]] = set()
        self.by_front: dict[tuple[str, str], list[dict]] = {}
        for r in rows:
            if r.get("type") == "COURSE":
                self.course_cards.add((r.get("category") or "",
                                       r.get("subcategory") or ""))
            self.by_front.setdefault((r.get("type"), r.get("front")), []).append(r)

    @classmethod
    def fetch_from_server(cls, host: str = REMOTE_HOST,
                          container: str = REMOTE_CONTAINER,
                          db: str = REMOTE_DB, timeout: int = 90) -> "CourseIndex":
        script = (
            "import sqlite3, json\n"
            f"c = sqlite3.connect('file:{db}?mode=ro', uri=True)\n"
            "cur = c.execute('''" + COURSE_INDEX_SQL + "''')\n"
            "cols = [d[0] for d in cur.description]\n"
            "print(json.dumps([dict(zip(cols, row)) for row in cur.fetchall()]))"
        )
        b64 = base64.b64encode(script.encode()).decode()
        # base64 est sûr pour le shell : aucune injection de guillemets possible
        remote = f"echo {b64} | base64 -d | docker exec -i {container} python"
        proc = subprocess.run(["ssh", host, remote],
                              capture_output=True, text=True, timeout=timeout)
        if proc.returncode != 0:
            raise RuntimeError(f"index serveur inaccessible : {proc.stderr.strip()[:300]}")
        return cls(json.loads(proc.stdout))

    def to_json(self) -> str:
        return json.dumps(self.rows, ensure_ascii=False, indent=1)

    @classmethod
    def from_json(cls, text: str) -> "CourseIndex":
        return cls(json.loads(text))

    def has_course_card(self, category: str, subcategory: str) -> bool:
        return (category, subcategory) in self.course_cards

    def exact_duplicate(self, block: CardBlock) -> bool:
        """Une carte identique (type, front, back, contenu) existe déjà en base."""
        for r in self.by_front.get((block.ctype, block.front), []):
            if (r.get("back") or "").strip() != block.back.strip():
                continue
            if block.ctype == "QCM":
                try:
                    existing = json.loads(r.get("payload") or "{}").get("choices", [])
                except (json.JSONDecodeError, TypeError):
                    continue
                mine = [{"text": c.text, "correct": c.correct} for c in block.choices]
                if existing == mine:
                    return True
            else:
                return True
        return False


# ------------------------------------------------------- dédup / front ------
def content_signature(block: CardBlock) -> str:
    """Signature de contenu (catégorie, sous-catégorie, type, front,
    back, choix) — deux blocs de même signature sont la MÊME question
    (export en double d'une même tentative Moodle), pas deux questions
    distinctes. La catégorie fait partie de la signature : une même
    question dans deux chapitres différents est conservée dans les deux.
    """
    return json.dumps({
        "cat": block.category, "sub": block.subcategory,
        "type": block.ctype, "front": block.front, "back": block.back,
        "choices": [{"text": c.text, "correct": c.correct}
                    for c in block.choices],
    }, ensure_ascii=False)


def disambiguate_front(block: CardBlock, index: CourseIndex,
                       seen_fronts: set[tuple[str, str]]) -> tuple[str, str | None]:
    """Dédup (type, front) AVANT déploiement.

    Retourne (front_final, raison_ou_None). Deux questions DISTINCTES
    partageant le même front reçoivent un suffixe déterministe
    [Q<n>·<hash6>] pour ne pas être perdues à l'ingestion (parse_blocks
    dédupe sur (type, front) : sans suffixe, l'une serait écrasée).
    """
    front = block.front
    key = (block.ctype, front)
    if key not in seen_fronts and key not in index.by_front:
        return front, None
    digest = hashlib.md5(f"{block.front}||{block.back}".encode("utf-8")).hexdigest()[:6]
    tag = f" [Q{block.number}·{digest}]" if block.number is not None else f" [·{digest}]"
    new_front = front + tag
    return new_front, (
        f"front reformulé pour différencier deux questions distinctes "
        f"(doublon (type, front) détecté) : {new_front!r}"
    )


# ------------------------------------------------------- validation parseur --
def validate_with_parse_blocks(text: str, strict_generated: bool = False) -> tuple[int, list[str]]:
    """Passe le .txt généré dans le VRAI parseur de l'application (app.py:71).

    Tout bloc en erreur est rejeté — jamais déployé.
    """
    from app import parse_blocks  # import paresseux : app.py a des effets de bord
    cards, errors = parse_blocks(text)
    for number, card in enumerate(cards, 1):
        if strict_generated:
            if not card.get("back") and card.get("type") != "TF":
                errors.append(f"Carte {number} : explication R: vide")
            if len(card.get("back") or "") > 600:
                errors.append(f"Carte {number} : explication R: supérieure à 600 caractères")
            math_text = f"{card.get('front', '')}\n{card.get('back', '')}"
            math_text = re.sub(r"```[\s\S]*?```|`[^`]*`", "", math_text)
            if math_text.count("$") % 2:
                errors.append(f"Carte {number} : délimiteurs LaTeX $ non équilibrés")
        if card.get("type") == "QCM":
            try:
                choices = json.loads(card.get("payload") or "{}").get("choices", [])
                correct = sum(bool(choice.get("correct")) for choice in choices)
                if len(choices) < 2 or correct < 1:
                    errors.append(f"Carte {number} : QCM sans choix valides ou réponse juste")
                if strict_generated and (len(choices) != 4 or correct != 1):
                    errors.append(f"Carte {number} : QCM généré doit avoir 4 choix et exactement une bonne réponse")
            except (ValueError, TypeError):
                errors.append(f"Carte {number} : choix QCM illisibles")
    return len(cards), errors


# ----------------------------------------------------------- backends LLM --
SYSTEM_PROMPT_COURSE = (
    "Tu es un professeur d'école d'ingénieurs (EPITA). Tu résumes un chapitre "
    "de cours sous forme de cartes au FORMAT TEXTE STRICT ci-dessous.\n\n"
    "IMPORTANT : ne réponds qu'avec les blocs de cartes. Aucun texte "
    "introductif, aucune conclusion, pas de balises de code Markdown (```), "
    "PAS DE JSON (le LaTeX comme \\frac, \\neq, \\beta casse json.loads).\n\n"
    "Format strict attendu (chaque bloc séparé par \"---\") :\n\n"
    "CAT: {Matière} / {Chapitre}\n"
    "Q: {Titre ou concept clé du cours}\n"
    "R: {Formule essentielle en LaTeX ou définition punchy}\n"
    "---\n\n"
    "Règles impératives :\n"
    "1. Chaque bloc commence par \"CAT:\" puis \"Q:\".\n"
    "2. LaTeX standard : $...$ inline et $$...$$ pour les équations.\n"
    "3. Une carte COURSE = une idée atomique ; titre court et réponse concise.\n"
    "4. Utilise uniquement les informations du texte fourni. N'invente aucune formule, hypothèse, valeur ou lien ; ignore les notions ambiguës/incomplètes.\n"
    "5. Dans R:, ajoute une intuition utile (pourquoi le résultat est vrai, quand l'utiliser, ou le piège à éviter), sans dépasser 600 caractères.\n"
)
# La grammaire ci-dessus reprend SYSTEM_PROMPT de generate_qcms.py:30-61
# (format texte brut, blocs séparés par ---), adaptée aux cartes COURSE.


class LLMBackend:
    """Backend LLM abstrait — configuré par variables d'environnement.

    LLM_PROVIDER  : 'mistral' (défaut) ou 'ollama'
    LLM_MODEL     : modèle à utiliser
    LLM_API_KEY   : clé (Mistral)
    LLM_BASE_URL  : endpoint (Ollama)
    Tout appel est interdit sans --allow-llm (contrainte de coût zéro).
    """

    def generate(self, system_prompt: str, user_prompt: str) -> str:
        raise NotImplementedError


class MistralBackend(LLMBackend):
    def __init__(self, api_key: str | None = None,
                 model: str | None = None,
                 base_url: str = "https://api.mistral.ai/v1",
                 max_retries: int = 4, delay: float = 1.0):
        self.api_key = api_key or os.getenv("LLM_API_KEY") or os.getenv("MISTRAL_API_KEY")
        # ATTENTION : le modèle par défaut de generate_qcms.py (open-mistral-7b)
        # est PAYANT. Le tier gratuit Experiment de Mistral couvre
        # mistral-small-latest / open-mistral-nemo (à vérifier en console).
        self.model = model or os.getenv("LLM_MODEL", "mistral-small-latest")
        self.base_url = base_url.rstrip("/")
        self.max_retries = max_retries
        self.delay = delay

    def generate(self, system_prompt: str, user_prompt: str) -> str:
        import requests
        url = f"{self.base_url}/chat/completions"
        headers = {"Authorization": f"Bearer {self.api_key}",
                   "Content-Type": "application/json"}
        payload = {"model": self.model,
                   "messages": [{"role": "system", "content": system_prompt},
                                {"role": "user", "content": user_prompt}],
                   "temperature": 0.25}
        last_err = None
        for attempt in range(self.max_retries):
            try:
                resp = requests.post(url, headers=headers, json=payload, timeout=60)
                if resp.status_code == 200:
                    return resp.json()["choices"][0]["message"]["content"].strip()
                if resp.status_code == 429:  # backoff exponentiel
                    wait = self.delay * (2 ** (attempt + 1))
                    print(f"    ⏳ 429 rate limit, pause {wait:.0f}s")
                    time.sleep(wait)
                    continue
                last_err = f"HTTP {resp.status_code}: {resp.text[:120]}"
            except Exception as e:
                last_err = f"réseau : {e}"
            time.sleep(self.delay * (2 ** attempt))
        raise RuntimeError(last_err or "échec LLM")


class ModelRotator:
    """Rotation stricte : 1 modèle par chapitre, pas de retry-loop.

    Le même modèle est utilisé pour tous les appels d'un chapitre ; le
    suivant sert au chapitre suivant. En cas de 429 (rate limit), on
    passe au modèle suivant dans la rotation (fallback) et on checkpointe
    le chapitre comme FAILED pour reprise ultérieure. Aucun retry boucle
    n'est effectué : le 429 = changement de modèle OU checkpoint.
    """

    def __init__(self, models: list[str]):
        self.models = list(models)
        self._idx = 0

    def current(self) -> str:
        return self.models[self._idx % len(self.models)]

    def advance(self) -> str:
        """Passe au modèle suivant (à utiliser après un 429 fallback)."""
        self._idx = (self._idx + 1) % len(self.models)
        return self.current()

    def __len__(self) -> int:
        return len(self.models)


class MistralBackendV2(LLMBackend):
    """Backend Mistral v2 : rotation de modèles, 429 fallback, rate limiting.

    - generate() : utilise le modèle courant du ModelRotator.
      En cas de 429 → passe au modèle suivant (une seule fois), puis
      lève une exception pour déclencher le checkpoint.
    - verify()   : utilise un modèle DISTINCT (DEFAULT_VERIFY_MODEL) pour
      valider l'output du LLM. Batch sur tout le chapitre en un seul appel.
    """

    def __init__(self, api_keys: list[str] | None = None,
                 gen_models: list[str] | None = None,
                 verify_model: str | None = None,
                 base_url: str = "https://api.mistral.ai/v1",
                 max_fallbacks: int = 2,
                 safe_delay: float = SAFE_DELAY_BETWEEN_CALLS):
        keys = api_keys or []
        if not keys:
            for env_name in ("MISTRAL_API_KEY_2", "MISTRAL_API_KEY", "LLM_API_KEY"):
                v = os.getenv(env_name)
                if v:
                    keys.append(v)
        self.api_keys = keys
        self._key_idx = 0
        self.base_url = base_url.rstrip("/")
        self.max_fallbacks = max_fallbacks
        self.safe_delay = safe_delay
        self.gen_models = gen_models or DEFAULT_GENERATION_MODELS
        self.rotator = ModelRotator(self.gen_models)
        self.verify_model = verify_model or DEFAULT_VERIFY_MODEL

    @property
    def api_key(self) -> str:
        return self.api_keys[self._key_idx % len(self.api_keys)] if self.api_keys else ""

    @property
    def model(self) -> str:
        return self.rotator.current()

    def _cycle_key(self):
        """Passe à la clé API suivante (fallback sur rate-limit global)."""
        if len(self.api_keys) > 1:
            self._key_idx = (self._key_idx + 1) % len(self.api_keys)

    def _post(self, model: str, system_prompt: str,
              user_prompt: str) -> str:
        import requests
        url = f"{self.base_url}/chat/completions"
        headers = {"Authorization": f"Bearer {self.api_key}",
                   "Content-Type": "application/json"}
        payload = {"model": model,
                   "messages": [{"role": "system", "content": system_prompt},
                                {"role": "user", "content": user_prompt}],
                   "temperature": 0.25}
        resp = requests.post(url, headers=headers, json=payload, timeout=120)
        if resp.status_code == 429:
            raise RateLimitError(resp.text[:200])
        if resp.status_code != 200:
            raise RuntimeError(f"HTTP {resp.status_code}: {resp.text[:200]}")
        return resp.json()["choices"][0]["message"]["content"].strip()

    def generate(self, system_prompt: str, user_prompt: str) -> tuple[str, str]:
        """Génère avec le modèle courant. Retourne (content, model_used).

        429 → fallback au modèle suivant (max_fallbacks fois), sinon
        lève RateLimitError pour déclencher un checkpoint.
        """
        last_err: str | None = None
        for fallback in range(self.max_fallbacks + 1):
            model = self.rotator.current()
            try:
                time.sleep(self.safe_delay)
                content = self._post(model, system_prompt, user_prompt)
                return content, model
            except RateLimitError as e:
                last_err = str(e)
                print(f"    ⏳ 429 sur {model} → fallback au modèle suivant")
                self.rotator.advance()
                self._cycle_key()
                continue
        raise RateLimitError(last_err or "tous les modèles en 429")

    def verify(self, text: str, category: str, subcategory: str,
               source_text: str = "", generation_model: str | None = None) -> tuple[bool, str]:
        """Compare les cartes au texte source et rejette les affirmations non étayées."""
        verify_model = self.verify_model
        if generation_model and verify_model == generation_model:
            verify_model = next((m for m in self.gen_models if m != generation_model), "")
        if not verify_model:
            return False, "aucun modèle distinct disponible pour la vérification"
        system = (
            "Tu es relecteur pédagogique. Vérifie chaque affirmation, formule, "
            "hypothèse et réponse des cartes uniquement contre le texte source fourni. "
            "Rejette toute information non étayée, ambiguë ou contradictoire. "
            "Vérifie aussi le format CAT:/Q:/R:/---. Ne corrige pas les cartes. "
            "Réponds exactement OK si toutes les cartes sont valides et étayées ; "
            "sinon réponds NOT_OK suivi des numéros des cartes et d'une raison brève."
        )
        user = (
            f"Matière : {category} / {subcategory}\n\n"
            f"SOURCE DU COURS :\n{source_text[:10000]}\n\n"
            f"CARTES À VÉRIFIER :\n{text[:6000]}"
        )
        try:
            time.sleep(self.verify_delay)
            raw = self._post(verify_model, system, user)
            ok = raw.strip().upper() == "OK"
            return ok, raw
        except RateLimitError:
            raise
        except Exception as e:
            return False, f"erreur vérif : {e}"

    @property
    def verify_delay(self) -> float:
        return VERIFY_DELAY


class RateLimitError(RuntimeError):
    """429 — déclenche le checkpoint, pas un retry-loop."""


class OllamaBackend(LLMBackend):
    """Backend local Ollama — coût marginal zéro, mais nécessite Ollama installé
    et un modèle téléchargé (aucune installation n'est faite automatiquement)."""

    def __init__(self, base_url: str | None = None, model: str | None = None,
                 max_retries: int = 3, delay: float = 0.5):
        self.base_url = (base_url or os.getenv("LLM_BASE_URL",
                          "http://localhost:11434")).rstrip("/")
        self.model = model or os.getenv("LLM_MODEL", "mistral")
        self.max_retries = max_retries
        self.delay = delay

    def generate(self, system_prompt: str, user_prompt: str) -> str:
        import requests
        payload = {"model": self.model,
                   "messages": [{"role": "system", "content": system_prompt},
                                {"role": "user", "content": user_prompt}],
                   "stream": False, "options": {"temperature": 0.25}}
        last_err = None
        for attempt in range(self.max_retries):
            try:
                resp = requests.post(f"{self.base_url}/api/chat",
                                     json=payload, timeout=300)
                if resp.status_code == 200:
                    return resp.json()["message"]["content"].strip()
                last_err = f"HTTP {resp.status_code}: {resp.text[:120]}"
            except Exception as e:
                last_err = f"réseau : {e} (Ollama lancé ?)"
            time.sleep(self.delay * (2 ** attempt))
        raise RuntimeError(last_err or "échec Ollama")


def build_backend_from_env(v2: bool = True) -> LLMBackend | None:
    provider = os.getenv("LLM_PROVIDER", "mistral").lower()
    if provider == "ollama":
        return OllamaBackend()
    if provider == "mistral":
        # Collect all available Mistral keys (MISTRAL_API_KEY_2 appended, MISTRAL_API_KEY)
        keys = []
        for env_name in ("MISTRAL_API_KEY_2", "MISTRAL_API_KEY", "LLM_API_KEY"):
            v = os.getenv(env_name)
            if v and v not in keys:
                keys.append(v)
        if not keys:
            return None
        # Resolve user-proposed model aliases to valid API IDs
        gen_env = os.getenv("MISTRAL_GEN_MODELS", "").strip()
        if gen_env:
            gen_models = [MISTRAL_MODEL_ALIASES.get(m.strip(), m.strip())
                          for m in gen_env.split(",") if m.strip()]
        else:
            gen_models = list(DEFAULT_GENERATION_MODELS)
        if v2:
            verify_env = os.getenv("MISTRAL_VERIFY_MODEL", "").strip()
            verify_model = MISTRAL_MODEL_ALIASES.get(verify_env, verify_env) if verify_env else DEFAULT_VERIFY_MODEL
            return MistralBackendV2(api_keys=keys, gen_models=gen_models,
                                    verify_model=verify_model)
        return MistralBackend(api_key=keys[0],
                              model=os.getenv("LLM_MODEL", gen_models[0]))
    return None


# -------------------------------------------------------------- tracker ----
class Tracker:
    """Suivi de progression (reprise sans retraitement), format qcm_progress.json."""

    def __init__(self, path: str | Path = TRACKER_FILE):
        self.path = Path(path)
        self.data = self._load()

    def _load(self) -> dict:
        if self.path.exists():
            try:
                return json.loads(self.path.read_text(encoding="utf-8"))
            except Exception:
                pass
        return {"files": {}, "chapters": {}, "total_cards": 0}

    def save(self) -> None:
        tmp = self.path.with_suffix(self.path.suffix + ".tmp")
        tmp.write_text(json.dumps(self.data, ensure_ascii=False, indent=1),
                       encoding="utf-8")
        os.replace(tmp, self.path)  # atomique

    def file_status(self, rel: str) -> dict | None:
        return self.data["files"].get(rel)

    def mark_file(self, rel: str, status: str, **info) -> None:
        entry = {"status": status, "timestamp": int(time.time())}
        entry.update(info)
        self.data["files"][rel] = entry

    def mark_chapter(self, key: str, status: str, **info) -> None:
        entry = {"status": status, "timestamp": int(time.time())}
        entry.update(info)
        self.data["chapters"][key] = entry


# ------------------------------------------------------------- Passe C ------
def collect_chapter_content(chapter_path: Path) -> str:
    """Contenu normalisé d'un chapitre : README + pages/ + fichiers/.

    Renvoie la concaténation (tronquée à MAX_CHUNK_CHARS pour le prompt LLM).
    """
    chunks: list[str] = []
    readme = chapter_path / "README.md"
    if readme.exists():
        chunks.append(readme.read_text(encoding="utf-8", errors="replace"))
    for sub in ("pages", "fichiers"):
        d = chapter_path / sub
        if not d.is_dir():
            continue
        for f in sorted(d.rglob("*.md")):
            chunks.append(f.read_text(encoding="utf-8", errors="replace"))
    text = normalize_mathjax_tags("\n\n".join(chunks))
    return text[:MAX_CHUNK_CHARS]


def ensure_course_card(category: str, subcategory: str, chapter_path: Path,
                       source_md_dir: Path, index: CourseIndex,
                       tracker: Tracker, allow_llm: bool = False,
                       backend: LLMBackend | None = None,
                       out_dir: Path | None = None,
                       dry_run: bool = False) -> tuple[str, CardBlock | None]:
    """Carte COURSE d'un chapitre : existe-t-elle déjà sur le serveur ?

    Retourne (statut, bloc_ou_None) :
      SKIPPED_EXISTS — (catégorie, sous-catégorie) présente avec ≥1 carte COURSE
      NO_CONTENT     — chapitre sans pages/ ni fichiers/ (rien à résumer)
      PENDING_LLM    — contenu disponible, mais génération LLM non autorisée (dry-run)
      GENERATED      — cartes générées par le LLM (uniquement avec --allow-llm)
      FAILED         — échec LLM ou échec de validation parse_blocks
    """
    chapter = chapter_path.name
    folder = chapter_path.parent.name
    key = chapter_key(folder, chapter)
    front = course_front(chapter)

    if index.has_course_card(category, subcategory):
        tracker.mark_chapter(key, "SKIPPED_EXISTS", category=category,
                             subcategory=subcategory, front=front)
        return "SKIPPED_EXISTS", None

    content = collect_chapter_content(chapter_path)
    if not content.strip():
        tracker.mark_chapter(key, "NO_CONTENT", category=category,
                             subcategory=subcategory)
        return "NO_CONTENT", None

    if not allow_llm or backend is None or dry_run:
        tracker.mark_chapter(key, "PENDING_LLM", category=category,
                             subcategory=subcategory, front=front,
                             content_chars=len(content))
        return "PENDING_LLM", None

    # Génération LLM (réservée : nécessite --allow-llm + tier gratuit validé)
    user_prompt = (
        f"Génère les cartes COURSE pour le chapitre suivant.\n"
        f"Matière : {category}\nChapitre : {clean_chapter_title(chapter)}\n\n"
        f"--- CONTENU DU CHAPITRE ---\n{content}"
    )

    # Support du backend V2 (rotation + fallback) vs backend V1 (simple)
    v2 = isinstance(backend, MistralBackendV2)
    try:
        if v2:
            raw, gen_model = backend.generate(SYSTEM_PROMPT_COURSE, user_prompt)
        else:
            raw = backend.generate(SYSTEM_PROMPT_COURSE, user_prompt)  # type: ignore[union-attr]
            gen_model = getattr(backend, "model", "?")
    except RateLimitError as e:
        # 429 sur tous les modèles de fallback → checkpoint pour reprise
        tracker.mark_chapter(key, "FAILED", category=category,
                             subcategory=subcategory,
                             error=f"429 checkpoint : {e}", rate_limited=True)
        return "FAILED", None
    except Exception as e:
        tracker.mark_chapter(key, "FAILED", category=category,
                             subcategory=subcategory, error=str(e)[:200])
        return "FAILED", None

    # Validation 1 : parse_blocks (grammaire stricte)
    n_cards, errors = validate_with_parse_blocks(raw, strict_generated=True)
    if errors or n_cards == 0:
        tracker.mark_chapter(key, "FAILED", category=category,
                             subcategory=subcategory,
                             error="parse_blocks : " + "; ".join(errors[:3]),
                             model=gen_model)
        return "FAILED", None

    # Validation 2 : vérification factuelle contre le contenu source.
    if v2:
        try:
            verified, vmsg = backend.verify(raw, category, subcategory, content, gen_model)
            if not verified:
                tracker.mark_chapter(key, "FAILED", category=category,
                                     subcategory=subcategory,
                                     error=f"vérification bloquante : {vmsg[:180]}",
                                     model=gen_model, rejected=True)
                return "FAILED", None
        except RateLimitError:
            pass

    # Écriture du fichier .txt dans out_dir/ (Generated_QCMs/ par défaut)
    out_base = out_dir or Path(DEFAULT_OUTPUT_DIR)
    safe_cat = re.sub(r"[^a-zA-Z0-9_-]+", "-", category)[:40]
    safe_sub = re.sub(r"[^a-zA-Z0-9_-]+", "-", subcategory)[:40]
    slug = f"{safe_cat}_{safe_sub}_{gen_model.replace('/', '_')[:30]}"[:80]
    out_file = out_base / f"{slug}.txt"
    if not dry_run:
        out_base.mkdir(parents=True, exist_ok=True)
        out_file.write_text(raw + "\n", encoding="utf-8")

    block = CardBlock(category=category, subcategory=subcategory,
                      ctype="COURSE", front=front, back="")
    tracker.mark_chapter(key, "GENERATED", category=category,
                         subcategory=subcategory, front=front, cards=n_cards,
                         model=gen_model, output_file=str(out_file))
    return "GENERATED", block


SYSTEM_PROMPT_QCM = (
    "Tu es un professeur d'école d'ingénieurs (EPITA). Génère des cartes QCM "
    "et Vrai/Faux qui testent la COMPRÉHENSION CONCRÈTE, pas la mémoire factuelle. "
    "Chaque QCM doit demander de raisonner, appliquer ou analyser — jamais de "
    "calculer un PGCD ou une racine.\n\n"
    "IMPORTANT : ne réponds qu'avec les blocs de cartes, aucun texte hors-format.\n\n"
    "Format (blocs séparés par ---) :\n\n"
    "CAT: {Matière} / {Chapitre}\n"
    "Q: [QCM] {question conceptuelle}\n"
    "R: {explication concise pourquoi la réponse est correcte}\n"
    "C1: {choix A}\n"
    "C2: {choix B}\n"
    "C3: [x] {choix C juste}\n"
    "C4: {choix D}\n"
    "---\n\n"
    "Pour les questions Vrai/Faux:\n\n"
    "CAT: {Matière} / {Chapitre}\n"
    "Q: [TF] {affirmation à évaluer}\n"
    "R: {explication}\n"
    "A: vrai\n"
    "---\n\n"
    "Règles :\n"
    "1. Chaque bloc commence par CAT: puis Q: avec [QCM] ou [TF].\n"
    "2. LaTeX standard : $...$ inline, $$...$$ display.\n"
    "3. QCM : exactement 4 choix (C1-C4), exactement un seul [x] = bonne réponse.\n"
    "4. TF : une ligne A: vrai ou A: faux.\n"
    "5. Génère 2-3 QCM et 1-2 TF par bloc de réponse.\n"
    "6. Questions de NIVEAU difficile : application, analyse, synthèse.\n"
    "7. Utilise uniquement le contenu fourni ; n'invente aucune formule, hypothèse ou valeur.\n"
    "8. Chaque R: explique brièvement le raisonnement et l'intuition, en 600 caractères maximum.\n"
)


def ensure_qcm_cards(category: str, subcategory: str, chapter_path: Path,
                     course_content: str, index: CourseIndex, tracker: Tracker,
                     backend: LLMBackend | None = None,
                     out_dir: Path | None = None, dry_run: bool = False) -> tuple[str, int]:
    """Génère des cartes QCM/TF d'entraînement pour un chapitre.

    Lit le contenu du COURSE existant (ou le chapitre MD) et produit
    des questions conceptuelles au format parse_blocks.

    Retourne (status, n_cards) :
      SKIPPED_EXISTS — le serveur possède déjà des QCM pour (cat, sub)
      NO_CONTENT     — pas de contenu à générer
      PENDING_LLM    — sans --allow-llm
      GENERATED      — cartes générées
      FAILED         — échec LLM / validation
    """
    chapter = chapter_path.name
    folder = chapter_path.parent.name
    key = chapter_key(folder, chapter)

    # Vérifier si des QCM existent déjà sur le serveur
    has_qcm = any(
        r.get("type") in ("QCM", "TF") and
        r.get("category") == category and
        r.get("subcategory") == subcategory
        for r in index.rows
    )
    if has_qcm:
        tracker.mark_chapter(key, "SKIPPED_EXISTS_QCM", category=category,
                             subcategory=subcategory)
        return "SKIPPED_EXISTS", 0

    content = course_content
    if not content.strip():
        content = collect_chapter_content(chapter_path)
    if not content.strip():
        tracker.mark_chapter(key, "NO_CONTENT", category=category,
                             subcategory=subcategory)
        return "NO_CONTENT", 0

    if not backend or dry_run:
        tracker.mark_chapter(key, "PENDING_LLM_QCM", category=category,
                             subcategory=subcategory)
        return "PENDING_LLM", 0

    user_prompt = (
        f"Génère des cartes QCM et Vrai/Faux pour le chapitre suivant.\n"
        f"Objectif : tester la COMPRÉHENSION CONCRÈTE (raisonner, appliquer, analyser).\n"
        f"Matière : {category}\nChapitre : {clean_chapter_title(chapter)}\n\n"
        f"--- CONTENU COURS (EXTRAITS) ---\n{content[:MAX_CHUNK_CHARS]}"
    )

    v2 = isinstance(backend, MistralBackendV2)
    try:
        if v2:
            raw, gen_model = backend.generate(SYSTEM_PROMPT_QCM, user_prompt)
        else:
            raw = backend.generate(SYSTEM_PROMPT_QCM, user_prompt)
            gen_model = getattr(backend, "model", "?")
    except RateLimitError as e:
        tracker.mark_chapter(key, "FAILED", category=category,
                             subcategory=subcategory,
                             error=f"429 QCM : {e}", rate_limited=True)
        return "FAILED", 0
    except Exception as e:
        tracker.mark_chapter(key, "FAILED", category=category,
                             subcategory=subcategory, error=str(e)[:200])
        return "FAILED", 0

    # Validation parse_blocks
    n_cards, errors = validate_with_parse_blocks(raw, strict_generated=True)
    if errors or n_cards == 0:
        tracker.mark_chapter(key, "FAILED", category=category,
                             subcategory=subcategory,
                             error="parse_blocks QCM : " + "; ".join(errors[:3]),
                             model=gen_model)
        return "FAILED", 0

    # Vérification factuelle bloquante contre le contenu du chapitre.
    if v2:
        try:
            verified, vmsg = backend.verify(raw, category, subcategory, content, gen_model)
            if not verified:
                tracker.mark_chapter(key, "FAILED", category=category,
                                     subcategory=subcategory,
                                     error=f"vérification QCM bloquante : {vmsg[:180]}",
                                     model=gen_model, rejected=True)
                return "FAILED", 0
        except RateLimitError:
            pass

    # Écriture du fichier
    out_base = out_dir or Path(DEFAULT_OUTPUT_DIR)
    safe_cat = re.sub(r"[^a-zA-Z0-9_-]+", "-", category)[:40]
    safe_sub = re.sub(r"[^a-zA-Z0-9_-]+", "-", subcategory)[:40]
    slug = f"{safe_cat}_{safe_sub}_QCM_{gen_model.replace('/', '_')[:30]}"[:80]
    out_file = out_base / f"{slug}.txt"
    if not dry_run:
        out_base.mkdir(parents=True, exist_ok=True)
        out_file.write_text(raw + "\n", encoding="utf-8")

    tracker.mark_chapter(key, "GENERATED_QCM", category=category,
                         subcategory=subcategory, cards=n_cards,
                         model=gen_model, output_file=str(out_file))
    return "GENERATED", n_cards


def run_pass_d(md_root: Path, resolver: CategoryResolver, index: CourseIndex,
               tracker: Tracker, args, backend: LLMBackend | None = None,
               out_dir: Path | None = None) -> dict:
    """Passe D : cartes QCM/TF d'entraînement par chapitre.

    Pour chaque chapitre avec COURSE mais SANS QCM, génère des questions
    conceptuelles via LLM. Même politique de rotation/429/fallback que Pass C.
    """
    stats = {"chapters_total": 0, "chapters_needs_qcm": 0,
             "skipped_exists": 0, "generated": 0, "failed": 0,
             "pending_llm": 0, "no_content": 0, "total_qcm_cards": 0}

    pass_d_done = 0
    pass_d_limit = getattr(args, "pass_d_limit", 0) or 0

    for course_dir, chapter_dir in iter_chapters(md_root):
        stats["chapters_total"] += 1
        folder, chapter = course_dir.name, chapter_dir.name
        key = chapter_key(folder, chapter)
        category, subcategory = resolver.resolve(folder, chapter)

        prev = tracker.data.get("chapters", {}).get(key)
        if prev and not args.force:
            prev_status = prev.get("status")
            if prev_status in ("SKIPPED_EXISTS_QCM", "GENERATED_QCM", "NO_CONTENT"):
                stats[PASS_D_STAT_KEYS.get(prev_status, "failed")] += 1
                if prev_status == "GENERATED_QCM":
                    stats["total_qcm_cards"] += prev.get("cards", 0)
                continue

        # Vérifier si le serveur a déjà un QCM pour ce chapitre
        has_qcm = any(
            r.get("type") in ("QCM", "TF") and
            r.get("category") == category and
            r.get("subcategory") == subcategory
            for r in index.rows
        )
        if has_qcm:
            stats["skipped_exists"] += 1
            continue

        # Le chapitre doit avoir un COURSE card pour pouvoir générer QCM
        if not index.has_course_card(category, subcategory):
            stats["no_content"] += 1
            continue

        stats["chapters_needs_qcm"] += 1

        allow_llm = bool(args.allow_llm) and not args.dry_run and backend is not None
        if allow_llm and pass_d_limit and pass_d_done >= pass_d_limit:
            break

        # Récupérer le contenu du chapitre (COURSE cards du fichier existant)
        course_content = collect_chapter_content(chapter_dir)
        if not course_content.strip():
            stats["no_content"] += 1
            tracker.mark_chapter(key, "NO_CONTENT", category=category,
                                 subcategory=subcategory)
            continue

        status, n_cards = ensure_qcm_cards(
            category, subcategory, chapter_dir, course_content,
            index, tracker, backend=backend,
            out_dir=out_dir, dry_run=args.dry_run)

        stats[PASS_D_STAT_KEYS.get(status, "failed")] += 1
        if status == "GENERATED":
            pass_d_done += 1
            stats["total_qcm_cards"] += n_cards
        tracker.save()

    return stats


PASS_D_STAT_KEYS = {
    "SKIPPED_EXISTS": "skipped_exists",
    "NO_CONTENT": "no_content",
    "PENDING_LLM": "pending_llm",
    "GENERATED_QCM": "generated",
    "FAILED": "failed",
}
def iter_qcm_files(md_root: Path) -> Iterable[Path]:
    return sorted(p for p in md_root.rglob("*.md") if "/qcms/" in str(p))


def iter_chapters(md_root: Path) -> Iterable[tuple[Path, Path]]:
    for course_dir in sorted(md_root.iterdir()):
        if not course_dir.is_dir():
            continue
        for chapter_dir in sorted(course_dir.iterdir()):
            if chapter_dir.is_dir():
                yield course_dir, chapter_dir


def run_pass_b(md_root: Path, out_dir: Path, resolver: CategoryResolver,
               index: CourseIndex, tracker: Tracker, args) -> dict:
    """Passe B : QCM déterministes. Retourne les métriques."""
    stats = {"files_total": 0, "files_done": 0, "files_failed_skipped": 0,
             "files_skipped_stub": 0, "files_rejected": 0, "files_failed": 0,
             "files_written": 0, "questions_extracted": 0,
             "questions_rejected": 0, "cards_qcm": 0,
             "duplicates_dropped": 0, "fronts_reformulated": 0}
    seen_fronts: set[tuple[str, str]] = set()
    seen_signatures: set[str] = set()  # portée : tout le lot (cross-fichiers)
    limit = args.limit or 0
    processed = 0

    for path in iter_qcm_files(md_root):
        rel = str(path.relative_to(md_root))
        stats["files_total"] += 1
        if args.only and args.only not in rel:
            continue
        if limit and processed >= limit:
            break

        prev = tracker.file_status(rel)
        if prev and not args.force:
            if prev.get("status") == "DONE":
                stats["files_done"] += 1
                continue
            if prev.get("status") == "FAILED" and not args.retry_failed:
                stats["files_failed_skipped"] += 1
                continue
        processed += 1

        questions, rejects, skips = parse_qcm_file(path)
        stats["questions_rejected"] += len(rejects)

        if skips and not questions:
            stats["files_skipped_stub"] += 1
            tracker.mark_file(rel, "SKIPPED", reason=skips[0])
            tracker.save()
            continue

        if not questions:
            stats["files_rejected"] += 1
            tracker.mark_file(rel, "REJECTED", reasons=rejects)
            tracker.save()
            continue

        parts = path.relative_to(md_root).parts
        folder = parts[0] if parts else "Général"
        chapter = parts[1] if len(parts) > 1 else None
        category, subcategory = resolver.resolve(folder, chapter)

        blocks, dropped, reformulated = [], 0, 0
        for q in questions:
            block = question_to_block(q, category, subcategory)
            sig = content_signature(block)
            if sig in seen_signatures:
                # même question exportée plusieurs fois (tentatives en double)
                stats["duplicates_dropped"] += 1
                dropped += 1
                continue
            if index.exact_duplicate(block):
                stats["duplicates_dropped"] += 1
                dropped += 1
                continue
            seen_signatures.add(sig)
            final_front, reason = disambiguate_front(block, index, seen_fronts)
            if reason:
                reformulated += 1
            block.front = final_front
            seen_fronts.add((block.ctype, block.front))
            blocks.append(block)
        stats["fronts_reformulated"] += reformulated

        if not blocks:
            stats["files_rejected"] += 1
            if dropped:
                reason_all = ("toutes les questions sont des doublons exacts "
                              "(même énoncé, même correction, mêmes choix — "
                              "déjà générées dans ce lot ou déjà en base)")
            else:
                reason_all = "aucune carte valide"
            tracker.mark_file(rel, "REJECTED",
                              reasons=[reason_all] + rejects)
            tracker.save()
            continue

        text = "\n".join(block_to_text(b) for b in blocks)
        n_cards, errors = validate_with_parse_blocks(text)
        if errors or n_cards != len(blocks):
            stats["files_failed"] += 1
            tracker.mark_file(rel, "FAILED",
                              errors=errors, expected=len(blocks), parsed=n_cards)
            tracker.save()
            continue

        slug = re.sub(r"[^a-zA-Z0-9_\-]+", "_",
                      f"{category}_{subcategory}_{path.stem}")[:80]
        out_file = out_dir / f"{slug}.txt"
        if not args.dry_run:
            out_dir.mkdir(parents=True, exist_ok=True)
            out_file.write_text(text + "\n", encoding="utf-8")
        stats["files_written"] += 1  # en dry-run : fichier qui SERAIT écrit
        stats["questions_extracted"] += len(questions)
        stats["cards_qcm"] += len(blocks)
        tracker.mark_file(rel, "DONE", output_file=str(out_file),
                          cards_count=len(blocks),
                          rejected_questions=rejects[:20],
                          duplicates=dropped, reformulated=reformulated,
                          category=category, subcategory=subcategory)
        tracker.save()

    return stats


PASS_C_STAT_KEYS = {"SKIPPED_EXISTS": "skipped_exists", "NO_CONTENT": "no_content",
                    "PENDING_LLM": "pending_llm", "GENERATED": "generated",
                    "FAILED": "failed"}


def run_pass_c(md_root: Path, resolver: CategoryResolver, index: CourseIndex,
               tracker: Tracker, args, backend: LLMBackend | None = None,
               out_dir: Path | None = None) -> dict:
    """Passe C : cartes COURSE par chapitre.

    En dry-run (ou sans --allow-llm) : analyse d'existence SEULEMENT,
    aucun appel LLM. Le résumé (R:) est sémantique, il ne peut être
    produit que par un LLM validé en coût zéro.

    Modèle de génération : rotation 1 modèle/chapitre (début du lot au
    prochain). 429 → fallback au modèle suivant → checkpoint FAILED.
    Vérification LLM : modèle distinct (DEFAULT_VERIFY_MODEL).
    """
    stats = {"chapters_total": 0, "chapters_with_qcm": 0, "skipped_exists": 0,
             "no_content": 0, "pending_llm": 0, "generated": 0, "failed": 0}

    # chapitres contenant de vrais QCM (pour le rapport de cohérence)
    qcm_chapters: set[str] = set()
    for f in iter_qcm_files(md_root):
        parts = f.relative_to(md_root).parts
        if len(parts) >= 2:
            qcm_chapters.add(chapter_key(parts[0], parts[1]))

    pass_c_done = 0
    pass_c_limit = getattr(args, "pass_c_limit", 0) or 0

    for course_dir, chapter_dir in iter_chapters(md_root):
        stats["chapters_total"] += 1
        folder, chapter = course_dir.name, chapter_dir.name
        key = chapter_key(folder, chapter)
        if key in qcm_chapters:
            stats["chapters_with_qcm"] += 1
        category, subcategory = resolver.resolve(folder, chapter)

        # Reprise : FAILED peut être retenté avec --retry-failed
        prev = tracker.data.get("chapters", {}).get(key)
        if prev and not args.force:
            if not args.retry_failed:
                if prev.get("status") in ("SKIPPED_EXISTS", "NO_CONTENT",
                                          "PENDING_LLM", "GENERATED", "FAILED"):
                    stats[PASS_C_STAT_KEYS.get(prev["status"], "failed")] += 1
                    continue
            elif prev.get("status") in ("SKIPPED_EXISTS", "NO_CONTENT",
                                      "PENDING_LLM", "GENERATED"):
                # --retry-failed : reprend aussi les FAILED
                stats[PASS_C_STAT_KEYS.get(prev["status"], "failed")] += 1
                continue

        allow_llm = bool(args.allow_llm) and not args.dry_run and backend is not None
        if allow_llm and pass_c_limit and pass_c_done >= pass_c_limit:
            break

        status, _block = ensure_course_card(
            category, subcategory, chapter_dir, md_root, index, tracker,
            allow_llm=allow_llm, backend=backend,
            out_dir=out_dir, dry_run=args.dry_run)
        if status == "GENERATED":
            pass_c_done += 1
        stats[PASS_C_STAT_KEYS.get(status, "failed")] += 1
        tracker.save()
    return stats


# ------------------------------------------------------------------ CLI -----
def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Convertisseur Markdown EPITA → blocs de cartes (parse_blocks).")
    ap.add_argument("--input", default=DEFAULT_INPUT_DIR)
    ap.add_argument("--output", default=DEFAULT_OUTPUT_DIR)
    ap.add_argument("--limit", type=int, default=0,
                    help="nombre max de fichiers qcms à traiter (0 = illimité)")
    ap.add_argument("--only", default="",
                    help="ne traiter que les fichiers dont le chemin contient SUBSTR")
    ap.add_argument("--only-pass", default="abc",
                    help="passes à exécuter : combinaison de 'a' (implicite dans "
                         "chaque passe), 'b' (QCM), 'c' (chapitres COURSE) et "
                         "'d' (QCM d'entraînement LLM)")
    ap.add_argument("--retry-failed", action="store_true")
    ap.add_argument("--force", action="store_true",
                    help="retraiter les fichiers DONE/FAILED")
    ap.add_argument("--dry-run", action="store_true",
                    help="analyse et validation sans écrire de fichier")
    ap.add_argument("--allow-llm", action="store_true",
                    help="AUTORISE les appels LLM (passe C). Interdit par défaut "
                         "jusqu'à validation du tier gratuit (coût zéro).")
    ap.add_argument("--offline", action="store_true",
                    help=f"utiliser {INDEX_FILE} local au lieu du serveur")
    ap.add_argument("--refresh-index", action="store_true",
                    help="reconstruire course_index.json depuis le serveur")
    ap.add_argument("--tracker", default=TRACKER_FILE)
    ap.add_argument("--pass-c-limit", type=int, default=0,
                    help="nombre max de chapitres COURSE à générer en LLM (0 = illimité)")
    ap.add_argument("--pass-d-limit", type=int, default=0,
                    help="nombre max de chapitres QCM à générer en LLM (0 = illimité)")
    ap.add_argument("--verify", action="store_true",
                    help="Passer par la vérification LLM (modèle distinct) après génération")
    args = ap.parse_args(argv)

    md_root = Path(args.input)
    if not md_root.is_dir():
        print(f"❌ Dossier introuvable : {md_root}")
        return 2
    out_dir = Path(args.output)
    resolver = CategoryResolver(Path(SELECTED_COURSES), Path(SYLLABUS))

    # Index : serveur (lecture seule) ou cache local
    index_path = Path(INDEX_FILE)
    index = None
    if not args.offline:
        try:
            index = CourseIndex.fetch_from_server()
            index_path.write_text(index.to_json(), encoding="utf-8")
            print(f"📇 Index serveur (lecture seule) : {len(index.rows)} cartes")
        except Exception as e:
            print(f"⚠️ serveur inaccessible ({e})")
    if index is None and index_path.exists():
        index = CourseIndex.from_json(index_path.read_text(encoding="utf-8"))
        print(f"📇 Index local de secours : {len(index.rows)} cartes")
    if index is None:
        print("❌ aucun index disponible (serveur inaccessible, pas de cache)")
        return 2

    tracker = Tracker(args.tracker)
    report: dict = {}

    if "b" in args.only_pass:
        print("\n===== PASSE B — QCM déterministes =====")
        report["pass_b"] = run_pass_b(md_root, out_dir, resolver, index, tracker, args)
    if "c" in args.only_pass:
        print("\n===== PASSE C — cartes COURSE par chapitre =====")
        backend = None
        if args.allow_llm and not args.dry_run:
            backend = build_backend_from_env(v2=True)
            if backend is None:
                print("❌ --allow-llm demandé mais aucun backend configuré "
                      "(MISTRAL_API_KEY / MISTRAL_API_KEY_2).")
                return 2
            if isinstance(backend, MistralBackendV2):
                print(f"🤖 LLM v2 — rotation : {backend.rotator.models}")
                print(f"   Vérif modèle : {backend.verify_model}")
                print(f"   Clés API : {len(backend.api_keys)}, délai safe : "
                      f"{backend.safe_delay}s")
            else:
                print(f"🤖 LLM : {type(backend).__name__} "
                      f"(modèle {getattr(backend, 'model', '?')}) — COÛT À VÉRIFIER")
        else:
            print("ℹ️ dry-run : aucun appel LLM (le résumé R: est sémantique)")
        report["pass_c"] = run_pass_c(md_root, resolver, index, tracker, args,
                                      backend=backend, out_dir=out_dir)
    if "d" in args.only_pass:
        print("\n===== PASSE D — cartes QCM d'entraînement LLM =====")
        if backend is None and not args.dry_run:
            backend = build_backend_from_env(v2=True)
            if backend is None:
                print("❌ --allow-llm demandé mais aucun backend configuré "
                      "(MISTRAL_API_KEY / MISTRAL_API_KEY_2).")
                return 2
        report["pass_d"] = run_pass_d(md_root, resolver, index, tracker, args,
                                      backend=backend, out_dir=out_dir)

    print("\n===== RAPPORT =====")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
