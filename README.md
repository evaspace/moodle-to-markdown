# 🎓 Moodle to Markdown (`moodle-to-markdown`)

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Moodle](https://img.shields.io/badge/Moodle-3.x%20%7C%204.x-orange.svg)](https://moodle.org/)
[![MarkItDown](https://img.shields.io/badge/Powered%20by-MarkItDown%20%26%20Mistral%20AI-success.svg)](https://github.com/microsoft/markitdown)

> **Universal Moodle scraper and batch course-to-markdown converter.**  
> Transform entire Moodle platforms and course archives (PDFs, Word docs, PowerPoint slides, Excel sheets, quizzes, lecture notes) into clean, beautifully formatted **Markdown (`.md`)** files ready for **Obsidian**, **VS Code**, **Logseq**, **Notion**, or **Typora**.

> For deploying the Epita Doomscrolling web app and its SQLite card database to a server, see [DEPLOYMENT.md](DEPLOYMENT.md).
> Product goals for the revision app (levels, scroll, exams calibration): see [README_OBJECTIFS.md](README_OBJECTIFS.md).

---

### 🌐 Language / Langue
- [🇬🇧 English Documentation](#-english-documentation)
- [🇫🇷 Documentation en Français](#-documentation-en-français)

---

<a name="-english-documentation"></a>
# 🇬🇧 English Documentation

## 🌟 Highlights & Features

- **Universal Compatibility**: Works with **any university or school** powered by Moodle 3.x or 4.x (EPITA, Sorbonne, Paris-Saclay, Polytechnique, Centrale, Lyon, McGill, etc.).
- **Zero-Friction Authentication**: Supports SSO / Ent / 2FA (Microsoft, Google, CAS, Shibboleth, SAML) via `MoodleSession` cookie, as well as Moodle WebService tokens and standard credentials.
- **Full Hierarchy Preservation**: Keeps your exact course architecture (Semesters -> Courses -> Chapters -> Sections).
- **Deep Content Extraction**: Scrapes not just files, but chapter summaries, rich HTML lecture pages (`mod_page`), quizzes/tests with solutions (`mod_quiz`), assignments (`mod_assign`), and video links (`mod_url`, YouTube, Panopto, Pod).
- **Mathematical Integrity**: Preserves inline (`$...$`) and display (`$$...$$`) LaTeX/MathJax formulas with 100% precision.
- **Batch Converter (`batch_convert.py`)**: Uses Microsoft's **MarkItDown** engine to automatically convert all downloaded PDFs, DOCX, PPTX, XLSX, HTML, and CSV files into clean Markdown in a mirrored folder tree.
- **Optional AI Polish (Mistral AI)**: Automated post-processing with Mistral AI to fix OCR imperfections, table alignments, and mathematical formatting.
- **Persistent Personal Notes**: Keeps your custom annotations under `## ✍️ Mes Notes Personnelles` intact even after future resynchronizations.
- **100% Local & Private**: No third-party servers, no telemetry. Your school documents and credentials remain strictly on your local machine.

---

## 👨‍💻 Credits & Attribution

- **Author & Creator**: **Morgan Pierrefeu** ([@evaspace](https://github.com/evaspace))
- **Document Conversion Engine**: [Microsoft MarkItDown](https://github.com/microsoft/markitdown)
- **AI Enhancement**: [Mistral AI](https://mistral.ai/)
- **License**: Released under the [MIT License](LICENSE).

---

## 🚀 Quick Start Guide

### 1. Requirements & Installation

Make sure you have **Python 3.9+** installed:

```bash
# Clone the repository
git clone https://github.com/evaspace/moodle-to-markdown.git
cd moodle-to-markdown

# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

*(Or simply run `make setup`)*

---

### 2. Workflow: 2 Simple Steps

```text
 ┌───────────────────────┐
 │   Moodle Platform     │
 └──────────┬────────────┘
            │  Step 1: Scrape courses & files
            ▼  (main.py / make run)
 ┌───────────────────────┐
 │   moodle_notes/       │  (Course tree with PDFs, DOCX, PPTX, pages, quizzes)
 └──────────┬────────────┘
            │  Step 2: Batch convert to Markdown
            ▼  (batch_convert.py / make convert)
 ┌───────────────────────┐
 │   moodle_notes_MD/    │  (100% clean Markdown tree for Obsidian / VS Code)
 └───────────────────────┘
```

#### Step 1: Scrape Courses from Moodle

Authenticate easily using your browser's session cookie:
1. Log in to your university Moodle in Chrome, Firefox, or Brave.
2. Press **F12** (Developer Tools) ➔ **Application** (or **Storage**) ➔ **Cookies** ➔ your Moodle URL.
3. Copy the value of `MoodleSession` (e.g. `abc123def456...`).

Run the scraper:
```bash
# Interactive mode (will prompt for cookie if not set)
python main.py

# Or provide your cookie directly
python main.py --cookie "abc123def456..."

# Target a specific university Moodle URL
python main.py --url "https://moodle.your-university.edu" --cookie "YOUR_COOKIE"

# Scrape only a specific course keyword
python main.py --course "Mathematics"
```

#### Step 2: Batch Convert All Course Documents to Markdown

Once your courses are downloaded, convert the entire tree of documents (.pdf, .docx, .pptx, .xlsx, .html) into Markdown:

```bash
# Run the batch converter on the downloaded tree
python batch_convert.py

# Or with Make shortcut:
make convert
```

Want to test on just 15 files first?
```bash
make convert-test
# or: python batch_convert.py --test-limit 15
```

Enable automated AI formatting and equation cleanup with Mistral AI:
```bash
python batch_convert.py --mistral-key "YOUR_MISTRAL_API_KEY"
# or set environment variable:
export MISTRAL_API_KEY="YOUR_KEY"
python batch_convert.py
```

---

## 🛠️ Makefile Commands Cheat Sheet

| Command | Description |
|---|---|
| `make setup` | Create virtual environment and install dependencies |
| `make run COOKIE="..."` | Run full Moodle scraping and note extraction |
| `make maths COOKIE="..."` | Scrape only courses matching "Mathématiques" |
| `make list COOKIE="..."` | List enrolled courses without downloading anything |
| `make no-files COOKIE="..."` | Scrape course pages and quizzes without heavy file attachments |
| `make convert` | Recursively convert all files in the course tree to `.md` |
| `make convert-test` | Test conversion on the first 15 files |
| `make convert LIMIT=50` | Convert up to 50 files |
| `make clean` | Clean up Python caches and temporary files |

---

## ⚙️ Configuration Reference (`config.py`)

You can edit default preferences directly in `config.py`:

```python
# Target Moodle URL
MOODLE_URL = "https://moodle.epita.fr"

# Authentication (Option 1: Session Cookie, Option 2: Token, Option 3: User/Pass)
MOODLE_SESSION = ""
MOODLE_TOKEN = ""
MOODLE_USERNAME = ""
MOODLE_PASSWORD = ""

# Mistral AI API key (optional for smart cleanup)
MISTRAL_API_KEY = ""

# Output folder for raw course downloads
OUTPUT_DIR = "EPITA_Moodle_Notes"

# Download options
DOWNLOAD_FILES = True
DOWNLOAD_VIDEOS = False
COURSES_FILTER = []  # Empty for all courses, or e.g. ["Maths", "Physics"]
```

---

## 📖 Using Your Notes in Obsidian or VS Code

1. Complete the scraping and conversion steps (`make run` then `make convert`).
2. Open **Obsidian** ➔ Click **Open folder as vault** ➔ Select the generated markdown folder (`EPITA_Moodle_Notes_MD` or `moodle_notes_MD`).
3. Enjoy:
   - Full bi-directional links between chapters, exercises, and exams.
   - LaTeX mathematical formulas render natively via MathJax/KaTeX.
   - All slides, lecture sheets, and summaries converted to searchable Markdown text.
   - Your custom notes in `## ✍️ Mes Notes Personnelles` are preserved across future syncs.

---
---

<a name="-documentation-en-français"></a>
# 🇫🇷 Documentation en Français

## 🌟 Points Forts & Fonctionnalités

- **Compatibilité Universelle** : Fonctionne avec **n'importe quelle université ou école** sous Moodle 3.x ou 4.x (EPITA, Sorbonne, Paris-Saclay, Polytechnique, Centrale, Lyon, McGill, etc.).
- **Authentification sans friction** : Compatible avec tous les SSO / Ent / 2FA (Microsoft, Google, CAS, Shibboleth, SAML, Forge ID) via le cookie standard `MoodleSession`, ainsi que les tokens WebService et identifiants classiques.
- **Conservation fidèle de l'arborescence** : Reproduit la structure exacte de vos cours (Semestres -> Matières -> Chapitres -> Fichiers).
- **Extraction exhaustive** : Récupère les résumés de chapitres, les pages de cours (`mod_page`), les QCM et tests avec corrigés (`mod_quiz`), les devoirs (`mod_assign`) et les liens vidéo (`mod_url`, YouTube, Panopto, Pod).
- **Formules mathématiques préservées** : Maintient intactes les équations LaTeX/MathJax inline (`$...$`) et display (`$$...$$`).
- **Convertisseur par lot (`batch_convert.py`)** : Exploite le moteur **MarkItDown** de Microsoft pour convertir automatiquement tous les PDF, DOCX, PPTX, XLSX, HTML et CSV en fichiers Markdown `.md` dans une arborescence miroir.
- **Passe de correction IA optionnelle (Mistral AI)** : Nettoyage automatique des artefacts OCR, réalignement des tableaux et harmonisation des formules LaTeX grâce à l'API Mistral AI.
- **Préservation des notes personnelles** : Votre section `## ✍️ Mes Notes Personnelles` n'est jamais écrasée lors des resynchronisations.
- **100% Local et Confidentiel** : Aucun serveur tiers, aucune télémétrie. Vos cours et identifiants restent exclusivement sur votre machine.

---

## 👨‍💻 Crédits & Remerciements

- **Auteur & Créateur** : **Morgan Pierrefeu** ([@evaspace](https://github.com/evaspace))
- **Moteur de conversion de documents** : [Microsoft MarkItDown](https://github.com/microsoft/markitdown)
- **Nettoyage et amélioration IA** : [Mistral AI](https://mistral.ai/)
- **Licence** : Publié sous licence open-source [MIT](LICENSE).

---

## 🚀 Guide de Démarrage Rapide

### 1. Prérequis & Installation

Assurez-vous d'avoir **Python 3.9+** :

```bash
# Cloner le dépôt
git clone https://github.com/evaspace/moodle-to-markdown.git
cd moodle-to-markdown

# Créer et activer l'environnement virtuel
python3 -m venv .venv
source .venv/bin/activate  # Sur Windows : .venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt
```

*(Ou lancez simplement `make setup`)*

---

### 2. Les 2 Étapes du Workflow

```text
 ┌───────────────────────┐
 │   Plateforme Moodle   │
 └──────────┬────────────┘
            │  Étape 1 : Scraping des cours et documents
            ▼  (main.py / make run)
 ┌───────────────────────┐
 │   moodle_notes/       │  (Arborescence des cours avec PDF, DOCX, QCM, pages)
 └──────────┬────────────┘
            │  Étape 2 : Conversion automatique en Markdown
            ▼  (batch_convert.py / make convert)
 ┌───────────────────────┐
 │   moodle_notes_MD/    │  (Notes 100% Markdown prêtes pour Obsidian / VS Code)
 └───────────────────────┘
```

#### Étape 1 : Télécharger vos cours depuis Moodle

Récupérez votre cookie de session en 15 secondes :
1. Connectez-vous sur votre Moodle avec votre navigateur (Chrome, Firefox, Brave).
2. Appuyez sur **F12** ➔ **Application** (ou **Stockage**) ➔ **Cookies** ➔ URL de votre Moodle.
3. Copiez la valeur du cookie `MoodleSession` (ex: `abc123def456...`).

Lancez le scraper :
```bash
# Mode interactif (le script vous demandera le cookie s'il n'est pas renseigné)
python main.py

# Ou en passant directement le cookie
python main.py --cookie "abc123def456..."

# Cibler l'URL d'une université spécifique
python main.py --url "https://moodle.votre-universite.fr" --cookie "VOTRE_COOKIE"

# Télécharger uniquement un cours particulier
python main.py --course "Mathématiques"
```

#### Étape 2 : Convertir l'ensemble des documents en Markdown

Une fois vos cours téléchargés, lancez la conversion récursive de tous les documents (.pdf, .docx, .pptx, .xlsx, .html) en Markdown :

```bash
# Lancer la conversion par lot
python batch_convert.py

# Ou avec le raccourci Make :
make convert
```

Pour tester rapidement sur 15 fichiers :
```bash
make convert-test
# ou : python batch_convert.py --test-limit 15
```

Pour activer le nettoyage automatique des formules et tableaux via Mistral AI :
```bash
python batch_convert.py --mistral-key "VOTRE_CLE_MISTRAL"
# ou via variable d'environnement :
export MISTRAL_API_KEY="VOTRE_CLE"
python batch_convert.py
```

---

## 🛠️ Commandes Make disponibles

| Commande | Action |
|---|---|
| `make setup` | Crée l'environnement virtuel et installe toutes les dépendances |
| `make run COOKIE="..."` | Lance l'extraction complète des cours Moodle |
| `make maths COOKIE="..."` | Télécharge uniquement les cours contenant "Mathématiques" |
| `make list COOKIE="..."` | Liste vos cours sans rien télécharger |
| `make no-files COOKIE="..."` | Extrait les pages et QCM sans télécharger les fichiers lourds |
| `make convert` | Convertit récursivement tous les documents en Markdown |
| `make convert-test` | Teste la conversion sur les 15 premiers fichiers |
| `make convert LIMIT=50` | Convertit jusqu'à 50 fichiers |
| `make clean` | Supprime les caches temporaires Python |

---

## ⚙️ Configuration avancée (`config.py`)

Personnalisez les réglages par défaut dans `config.py` :

```python
# URL du Moodle
MOODLE_URL = "https://moodle.epita.fr"

# Authentification (Option 1: Cookie, Option 2: Token API, Option 3: Identifiants)
MOODLE_SESSION = ""
MOODLE_TOKEN = ""
MOODLE_USERNAME = ""
MOODLE_PASSWORD = ""

# Clé API Mistral (optionnel pour la retouche intelligente)
MISTRAL_API_KEY = ""

# Dossier d'exportation des cours bruts
OUTPUT_DIR = "EPITA_Moodle_Notes"

# Options de téléchargement
DOWNLOAD_FILES = True
DOWNLOAD_VIDEOS = False
COURSES_FILTER = []  # Laisser vide pour tout télécharger
```

---

## 📝 Utilisation avec Obsidian ou VS Code

1. Lancez l'extraction puis la conversion (`make run` puis `make convert`).
2. Ouvrez **Obsidian** ➔ Cliquez sur **Ouvrir un dossier comme coffre** ➔ Sélectionnez le dossier généré (`EPITA_Moodle_Notes_MD` ou `moodle_notes_MD`).
3. Vous profitez immédiatement d'un espace de travail complet :
   - Navigation fluide entre chapitres, devoirs et corrigés via les liens Markdown relatifs.
   - Formules mathématiques rendues proprement via MathJax / KaTeX.
   - Textes de polycopiés et présentations entièrement indexables et consultables hors-ligne.
   - Vos annotations personnelles sous `## ✍️ Mes Notes Personnelles` restent préservées à chaque mise à jour.

## Renommage et footer (2026-11-12)
- Ancien nom: mathsdoomscrolling. Dossier `/opt/pierref/epitadoomscrolling`, container `epitadoomscrolling_app`, domaine `epitadoomscrolling.pierref.eu` (les anciens domaines redirigent en 301 via Caddy).
- Le dossier `/opt/pierref/landing` est devenu `/opt/pierref/morgan` (service compose `landing` inchangé).
- Footer identique à morgan.pierref.eu: `templates/footer.html` + `static/footer.css` (accueil et /cours). Blog: `blogbot/morgan_footer.py`, appelé par `blogbot/html_renderer.py`.
- Notation: widget `pierref-review.js` avec `data-site="epitadoomscrolling"` sur la balise script (sinon le site est déduit du hostname). Avis dans `morgan/data/reviews.db`.
- DNS OVH: l'enregistrement A `epitadoomscrolling` → 109.24.217.120 est nécessaire pour que Caddy obtienne le certificat.

## Levels mode (`/niveaux`)

Paper exercises graded from the simplest skill up to exam level + 20 %. Goals and rules: [README_OBJECTIFS.md](README_OBJECTIFS.md); work plan: [TODO_REFONTE.md](TODO_REFONTE.md).

- Accounts: `/compte` (username + password, optional e-mail). Session key from `SECRET_KEY` env or the generated `.secret_key` file (git-ignored).
- Rules (`levels.py`): one exercise per formula; a level is passed when **all** its exercises are green (last answer right). A failure turns the square red, drops one level and shows the formulas; greens are kept, reds come back (`pick_exo`: never done first, then red, never the one just failed). Opening another level (`?n=K`) is free practice: squares change, the level does not. The page shows the total progress bar (% of all the path's exercises green).
- Selection (`/niveaux?ordre=semestre|matiere&sem=&mat=&ch=`): order of the lists (semester first or subject first), then semester / subject / chapter (= level path), each narrowed by the lists before it; empty = all (`levels.select_paths`, `levels.selector`). "Tout confondu" (`/niveaux/melange?<same filters>`) redirects to a random selected path at the user's current level there, with `mix=1` so "Exercice suivant" draws again.
- Variants (`"variants"` on an exercise in `parcours/src/*.py`, e.g. the `VARIANTS` dict of `apis_integrales.py`): same formula, other numbers; each overrides `f`/`ans`/`a`/`b`/`calc`/`enonce`/`sol` and is checked by `build.py` like the exercise. The page shows the base, then each variant in turn, one more per previous attempt of that exercise (`levels.variant`); a variant never shows the past-exam `src`. The square stays the same.
- Formulas per exercise (`FORMULES` dict at the end of each `parcours/src/*.py`, id → formulas separated by ` · `): what the help « Formules de la solution » shows first, one per line, above the level's course reminder. `build.py` fails if an exercise (or an `EXTRA_PARTS` part) has no entry or an entry names an unknown id; a `multi` exercise gets the union of its parts. Variants share the formulas of their exercise.
- 404: `templates/404.html` (the cat explodes), JSON `{error}` under `/api/`.
- `ode` exercises (`parcours/build.py`): general solution `f` with constants `C1`, `C2` plugged into `lhs` (`Y0`=y, `Y1`=y', `Y2`=y''); the number of constants must equal the order.
- `value` exercises (`parcours/build.py`): `calc` must equal `ans`. Numbers are compared numerically; expressions with a variable (polynomial quotient, `series(f, x, 0, n+1).removeO()`, factorisation) are compared at sample points; sympy matrices (`Matrix([[..]])`, product, `.inv()`, `.rank()`) must be exactly equal. Any sympy name can be used in `calc` (`quo`, `rem`, `roots`, `limit`, `degree`, `LC`).
- S2 paths (2026-11-15): `apef_polynomes.py` (10 levels, 43 exercises), `apef_fonctions.py` (11, 57), `ev.py` (11, 60), `alm.py` (12, 64), calibrated on the 2026 exams of promo 2030 (APEF, EV B3 and B4, ALM). No complex numbers (promo 2031). A new path needs: its file in `parcours/src/`, its name in `PATHS` (`parcours/build.py`), its id in `parcours/syllabus.json` and in `FICHE_SECTION` (`levels.py`, section title of `annales/FORMULES.md`).
- Exercise text is inserted as raw HTML: never write `<` directly followed by a letter inside a formula (`$a<b$` opens a `<b>` tag); write `$a < b$`.
- Past exams ↔ levels: S2 `Type :` lines of `annales/md/` now carry `· Niveau : maths-s2-…/k` (394 exercises tagged by type); `python3 annales/tools/index.py` checks every id and rebuilds `annales/INDEX.md`.
- Content: one Python file per path in `parcours/src/`, verified with sympy and exported to JSON:
  `python parcours/build.py` (needs `sympy`, not needed by the web app). Every answer (derivative, primitive, integral value) is checked; the build fails on any wrong answer.
- Physics past exams (2026-11-15): the 21 S1 files (mécanique du point: kinematics, Frenet, statics, energy; 14 subjects, 7 corrections) are transcribed in `annales/md/S1/*/Phys/`, ECUE `Mécanique`, level ids `physique-s1-meca/k`; their types feed the « Mécanique » section of `annales/FORMULES.md` (course sheet of the path). Scans with no correction are subjects only; two PDFs (midterm 2027, final 2027) are annotated student copies, so only the statements are kept. Not done: the 27 S2 physics PDFs (thermodynamique B3, électromagnétisme B4, TDs).
- Physics S2 thermodynamics path (2026-11-16): `parcours/src/phys_thermo.py` → `physique-s2-thermo` (14 levels, 77 exercises, 10 notions, 23 quiz, variants, FORMULES), built from the Moodle course `Cours_thermodynamique_V2`, TD1-3 (B3, read as images) and the three text-layer S2 exams (partiel May 2019, partiel 2020/2021, midterm 2030 correction). Listed in `syllabus.json` (S2, ECUE `Thermodynamique`, block B3). Not done: transcription of the S2 physics annales to `annales/md` (so no `FICHE_SECTION` entry yet: the chapter sheet shows the notions only), the other S2 exams are scans, électromagnétisme (B4) path.
- Physics S2 work and energy path (2026-11-16): `parcours/src/phys_energie.py` → `physique-s2-energie` (11 levels, 64 exercises, 9 notions, 18 quiz, 22 variant sets, FORMULES; levels 10-11 exam). Covers the mechanics part of the S2 physics exams (work, power, kinetic energy theorem, mechanical energy, non-conservative forces, spring, Newton with pulley), calibrated on the text-layer S2 exams 2026 (partiel and midterm). Listed in `syllabus.json` (S2, ECUE `Travail et énergie`, block B3); `FICHE_SECTION` points to the S1 `Mécanique` sheet. Own work, no official correction: sympy checks the `value` exercises.
- Physics S2 past exams (2026-11-16): 10 of the 27 S2 physics PDFs are transcribed in `annales/md/S2/*/Phys/` (finals May 2019, 2020/21, May 2022, May 2024, May 2025; midterms March 2020, February 2023, March 2024, March 2025, promo 2030), each as a correction file (statement + `> ` solutions) and a subject file derived from it. ECUE `Thermodynamique` (levels `physique-s2-thermo/k`) or `Mécanique` (levels `physique-s2-energie/k` or `physique-s1-meca/k`; oscillators have no level). Official corrections where the repository has one; « corrigé rédigé » otherwise (March/May 2025, February 2023 which is an annotated student copy); the promo 2030 midterm has no subject, its statements are rebuilt from the correction. `FICHE_SECTION['physique-s2-thermo'] = 'Thermodynamique'`. `S2/Midterms/Phys/2026` is the S1 November 2021 test (already in S1): skipped. Older scans done on 2026-11-16: finals June 2016 (folder 2020: a 56-page bundle of the whole June 2016 session, only physics pages 1-7 in French transcribed), May 2017 (2021), June 2018 (2022) and midterms February 2017 (2021), March 2018 (2022), promo 2025 (correction only, page 1 with QCM 1-5 missing from the scan); « corrigé rédigé » for finals 2016 and 2017 (no correction in the repository). All 16 S2 physics exams are now in `annales/md` (TDs not transcribed). No S2 exam covers électromagnétisme, so no `Électromagnétisme` sheet.
- June 2016 bundle, other subjects (2026-11-16): the French maths (pages 15-22), électronique (31-37) and architecture (45-50) exams of `raw/S2/Finals/Phys/2020` are transcribed in `annales/md/S2/Finals/{Maths PC,Elec,Archi}/2020/` with a « corrigé rédigé » (sympy / Python checks; chronograms simulated by hand on the answer-sheet grid, time in half-periods of C). English versions (pages 8-14, 23-30, 38-44, 51-56) are not transcribed. These are the first électronique and architecture annales: ECUEs `Études des filtres`, `Numération`, `Systèmes à microprocesseur`, `Logique séquentielle`; 9 new types in `annales/tools/formules.py`. The bundle PDF is listed in `syllabus.json` for ALM, APEF, filtres, séquentielle and microprocesseur.
- Architecture S1 paths (2026-11-16): `parcours/src/archi_numeration.py` → `archi-s1-numeration` (14 levels, 75 exercises: bases, fractions, binary/hex arithmetic, capacity, two's complement, overflow, IEEE 754 single/double; levels 13-14 exam) and `parcours/src/archi_boole.py` → `archi-s1-boole` (12 levels, 69 exercises: gates, laws, De Morgan, canonical forms, Karnaugh 3/4 variables with don't-cares, XOR, truth-table problems, NAND-only; levels 11-12 exam). Sources: Moodle `Archi S1 - Promo 2030` (chapters 1-2, TD4-7) and the exams `b1_exam_fr`, `s1_exam2_fr`, `b2_exam_fr` (no `annales/` transcription: `annales` list empty in `syllabus.json`). `build.py` gained helpers for `calc`/`ans`: `bits`, `hexa`, `octal` (value of a number in that base, fractions allowed), `tc` (two's complement), `f32`/`f64` (IEEE bits as integer), `f32d`/`f64d` (decode), `eqv` (two Boolean expressions equivalent → 1), `cover(expr, 'DCBA', ones, dont_cares)` (Karnaugh check, variables most significant first), plus symbols `A B C D`, `Xor`, `Not`.
- Architecture S1 combinational circuits (2026-11-16): `parcours/src/archi_circuits.py` → `archi-s1-circuits` (8 levels, 46 exercises: full adder, 4-bit ripple adder, adder-subtractor, comparators, multiplexers/decoders, TD6 vending machine; levels 7-8 exam), from the Moodle TD6/TD7. Next in Archi: S2 sequential logic (flip-flops, counters, microprocessor) from `Archi S2 2030 - ...`.
- Architecture S2 sequential logic (2026-11-16): `parcours/src/archi_sequentielle.py` → `archi-s2-sequentielle` (10 levels, 56 exercises: JK/D/T flip-flops, timing diagrams, asynchronous counters and modulo N reset, excitation tables, synchronous counter synthesis with D and JK, shift registers; levels 9-10 exam), from the Moodle `Archi S2 2030` chapters 1-2 and the B3 exam 2025/2026. New `build.py` helpers `seqD(n, sequence, [D_{n-1}..D_0])` and `seqJK(n, sequence, [J_{n-1},K_{n-1},..,J_0,K_0])` (1 if the inputs drive the counter through the cyclic sequence, unused states ignored; symbols `Q0..Q3`). Not done in Archi: microprocessor systems (B4, `Chapitre_3.pdf`, exam `b4_exam_fr.pdf`).
- Past exams: `annales/raw/` (PDF from the Epidocs Past-Exams GitHub repo), `annales/md/` (clean LaTeX transcription of all 146 maths S1/S2 files, 956 exercises, done 2026-11-15). Each exercise is a `## ` heading followed by `Type : <type> · ECUE : <ecue> · Niveau : <path id>/<n>` (Niveau only for S1 paths) and `Formules : ...` (every formula needed to solve it). In corrections that restate the statement, the solution lines start with `> `.
- `annales/tools/formules.py`: exercise type -> formulas (single source). `python3 annales/tools/index.py` rebuilds `annales/INDEX.md` (exam -> real date -> exercises -> type -> ECUE -> level) and `annales/FORMULES.md` (formula sheet by ECUE); it fails if a type has no formulas, an exercise has no Type/Formules line or a level id does not exist. Run it after editing any file in `annales/md/`.
- Formula sheet page: `/formules` (login required, linked from `/niveaux`), rendered from `annales/FORMULES.md` (`formula_sheet()` in `levels.py`, cached per file change), template `templates/formules.html`.
- Corrections: every subject file has a sibling `*-correction-*.md` (official, or written for this app and marked « corrigé rédigé » in its header, checked with sympy; ambiguous readings of a statement are flagged in the text). Same `Type/ECUE/Niveau/Formules` header per exercise as the subject.
- Prerequisites: `levels.PREREQ` maps a path to the paths it relies on; a failed answer returns `prereq` and `static/niveaux.js` shows them as links (« Notions de base à revoir »). Edit the dict to change the graph; `tests/test_levels.py` checks every id exists.
- Other tools in `annales/tools/`: `bx.py` (text layer with exponent markers), `addf.py SCRATCH` (installs `SCRATCH/out/NNN.md` into `annales/md` and inserts the Formules lines), `en.py` (English-version note from the French file), `subj.py` (subject file derived from a correction with `> ` solutions), `list.txt` (line N = raw PDF N).
- Points (`levels.score`): 100 × (1 + (level − 1)/4) × speed, speed = reference time / time spent, clamped to ×0.5..×2. Two helps can be opened before answering (`levels.HINTS`, buttons on the exercise page): « Fiche du chapitre » (every notion of the path + the path's section of `annales/FORMULES.md`, mapped by `FICHE_SECTION`) halves the points and adds 50 % of the time limit; « Formules de la solution » (the notions of the level) gives a third of the points and doubles the time limit. Both opened: a third, +150 % time. The browser calls `POST /api/niveaux/<subject>/hint {kind}`; the helps are stored in the session clock, so points and the timeout check are computed by the server. `exo_log.peek`: 0 none, 1 solution formulas, 2 chapter sheet only. A failure gives 0. Time is measured server-side (session clock set when the exercise page is served).
- Reference time (`levels.timing`): average time of all users' successful attempts on the **level** (one average per level so it fills quickly), scaled by the exercise's authored length; used once a level has 5 successes, before that the authored `duree` is the limit and 60 % of it the reference. Time limit = 1.6 × reference. When the countdown ends the exercise counts as failed (`timeout` column of `exo_log`, trusted only if the server clock agrees); each timeout on that exercise since its last success adds +50 % to its limit, up to ×3 (`levels.time_bonus`). The reference used for points does not move, so a slower answer still earns fewer points.
- Cat: `static/cat.js` (shared with the feed): fixed bottom-right, idle life every 4–9 s, claps on success, explodes in pixel blood on failure and respawns after 1.5 s.
- Password reset: `/compte` → "Mot de passe oublié" sends a one-hour link (`/compte?reset=TOKEN`, only the sha256 is stored, one mail per account every 5 min, same answer whether the account exists). Mail from morgan@pierref.eu via OVH SMTP; `MAIL_SERVER`, `MAIL_PORT`, `MAIL_USERNAME`, `MAIL_PASSWORD` in `.env` (mode 600, git-ignored), passed by `docker-compose.yml`. Links use `PUBLIC_URL`, never the Host header.
- Syllabus registry: `parcours/syllabus.json` (subject → semester → ECUE → Moodle chapters → level paths → past exams → exam period). `parcours/build.py` fails if a Moodle chapter, a past exam file or a listed level path is missing, or if a built path is not in the registry.
- Adaptive scroll (`scroll.py`, `/scroll/<path>`): course cards from the path's notions, QCM / true-false from its quiz. About 1 course card in 4, a course card is tested on the next 1–2 cards, a wrong answer brings the notion's course card back and the missed question returns after 4 cards. Scroll level: +1 right, −1 wrong, one more notion unlocked every 2 points (notions in syllabus order). Never changes exercise levels. Display: same markup and CSS as the main feed (`templates/scroll.html` reuses `#app-header`, `#feed` snap scrolling and `.card`/`.card-front`/`.choice-btn` from `static/style.css`; `static/scroll.js` builds the cards).
- Tests: `.venv/bin/python -m unittest tests.test_levels tests.test_scroll -v`.
- Deploy: the container bind-mounts the project; after a Python or template change run `docker restart epitadoomscrolling_app`.

### Stats page (`/stats`)
Per-account statistics computed from `exo_log` by `levels.compute_stats` (pure function, unit-tested):
totals (done, passed, failed, success rate, time, points), a year heatmap (53 weeks, one square per day,
hue from red = all failed to green = all passed, grey = no work), minutes per day over 30 days, streaks,
best day, first-try rate, "revenges" (failed then passed), favourite hour, most failed exercise, timeouts,
and a per-subject bar. Times are shown in Europe/Paris; one attempt counts at most 30 min (`MAX_SECS`).
Linked from `/niveaux` and `/compte`.


## Navbar, stats et admin (2026-11-15)
- `templates/nav.html` : navbar commune, alimentée par `levels.nav_state()` (processeur de contexte `nav`, route `/api/me`). Footer `footer.html` inclus sur toutes les pages sauf les fils plein écran.
- `/stats` : stats personnelles. `/admin/stats` (HTTP Basic `ADMIN_PASSWORD`, `?format=json`) : stats agrégées calculées par `admin_stats.compute()` (testée dans `tests/test_admin_stats.py`).


## Home feed state per account

`user_state`, `session_log`, `folder` and `favorite` have a `uid` column (account id, `0` = anonymous visitors, who share one state as before). `init_db.migrate_uid` adds it and rebuilds `folder`/`favorite` (UNIQUE now includes `uid`). Streak, XP, failed-card replay, likes and folders therefore follow the logged-in account. The home category list for maths is sorted promo 2031, then S1, then S2, then the rest (`themes.syllabus_rank`).
- Architecture S2 microprocessor systems (2026-11-16): `parcours/src/archi_micro.py` → `archi-s2-microprocesseur` (13 levels, 85 exercises: capacity/depth/width, address and data buses, parallel/series/mixed memory assembly, which memory is active, zone decoding, memory map with low/high addresses (checked with `hexa(...)`), redundancy (mirror images), linear decoding, decoding without gaps; levels 12-13 exam), from the Moodle `Archi S2 2030` chapter 3, TD3, TD4 and the exams `b4_exam_fr` (2025/2026) and `s2_exam4_fr` (2024/2025). Not covered: TD5 (circuit drawing: RS latch, 74HCT193 counters, M2716 ROM, serial transmission), listed in `a_faire` of `syllabus.json`. Overlines of the `CS` expressions were lost by `pdftotext`: rebuilt from the memory maps.
- Electronics S1 (2026-11-16): `parcours/src/elec_circuits.py` → `elec-s1-circuits` (12 levels, 80 exercises: charge/power, Ohm and C/L relations, Kirchhoff, series/parallel, dividers, Thévenin/Norton, Millman, sinusoidal quantities, complex impedances; levels 11-12 exam), matière `electronique` in `syllabus.json`. Sources: Moodle `S1 - Electronique - Promo 2030` (`Concepts de base`, TD1-4) and the B1 exams of October 2024 and 2025. Figures are not reproduced: circuits are described in words, exam exercises that depend on a figure are `open` with the official results. Not done: S2 (diodes, filters, transients).
- Electronics S1 B2 (2026-11-16): `parcours/src/elec_sinus.py` → `elec-s1-sinus` (12 levels, 85 exercises: complex amplitude, impedances and their associations, generalised Ohm's law, complex voltage divider, complex Thévenin/Norton, low/high frequency limits, transfer function and gain, first and second order filters; levels 11-12 exam). Sources: `Kit de Survie Régime Sinusoïdal`, TD4 (with correction) and the exams of January 2025 (B2, filters) and January 2026. Symbolic answers use the sympy symbols `R`, `L`, `C`, `w` and `I` (= j), checked at sample points by `build.py`; never use `E` in `calc` (it is Euler's number in `NS`). No source covers AC power, so it is not in the path.
- Electronics S2 filters (2026-11-16): `parcours/src/elec_filtres.py` → `elec-s2-filtres` (12 levels, 84 exercises: transfer function and gain, components at low/high frequency, nature and order, dB and slopes, cut-off and bandwidth, first order high/low pass, second order low/high/band pass, full method with Thévenin; level 12 exam). Sources: Moodle `Electronique S2 - Études des filtres` (survival kit, course, TD with correction, B3 exam March 2026 with correction). S2 vocabulary: `G = |H|` is the gain. The three S2 electronics Moodle courses sit under one `S2` semester whose `moodle` is `.`, so chapters are written from the Moodle root.
- Electronics S2 transients (2026-11-16): `parcours/src/elec_transitoires.py` → `elec-s2-transitoires` (12 levels, 83 exercises: C/L relations and continuity, DC steady state, initial conditions, first order ODE, solution `s(inf) + (s(0+) - s(inf)) exp(-t/tau)`, RC charge, RL current rise, time constant, Thévenin reduction, discharge and spark, Millman reminder; level 12 exam). Sources: survival kit, TD with correction, February 2023 test (no promo 2030 exam published). Time-dependent answers use `t` (in ms when stated) and are checked at sample points; some `calc` use `diff(..., t)` to check the solution against its ODE.
- Electronics S2 diodes (2026-11-16): `parcours/src/elec_diodes.py` → `elec-s2-diodes` (12 levels, 84 exercises: polarisation, ideal/threshold/real models, proof by contradiction, diode circuits, transfer characteristic and clipper, diode logic gates, half-wave and bridge rectifiers, Zener diode, Zener clipping, Zener voltage regulator; level 12 exam). Sources: Moodle `Electronique S2 - Diodes` (course, « Précisions et méthodes », TD diodes and TD Zener with corrections) and the March 2025 exam (English, no official correction: level 12 answers are our own, labelled « corrigé rédigé, non officiel »). Zener TD ex. 4 values (R = 1 kΩ, Rc = 2.2 kΩ, |Vz| = 6.2 V) were inferred from the corrected results (8.25 V, 5.5 V, Rc,min ≈ 1 kΩ): the statement page is missing from the scan.
- Algorithmics S1 TAA (2026-11-16): `parcours/src/algo_taa.py` → `algo-s1-taa` (15 levels, 93 exercises: signature, hierarchy (defined/predefined types, internal operations/observers), axioms and preconditions, recursive list, iterative list, conversions and extensions (concaténer, existe, rechercher), stacks, queues, writing axioms of an extension, static/dynamic representations, sets and multisets; level 12 = B1 exam of 30 October 2024, level 13 = stack/queue output orders and sequential/dichotomic search (tested in the B2), levels 14-15 = B2 exams of 9 January 2024 and 7 January 2025). Exam sources: Past-Exams `S1/Midterms/Algo/2029/TAA`, `S1/Finals/Algo/2028|2029/TAA`; the file `final-2027-s1-algo-correction-fr.pdf` is not a correction but a student copy of the 9 January 2024 exam marked 9/10 by the teacher (used as reference, student name not reproduced). Output orders, dichotomy calls (g, d, milieu) and search paths are computed by `_out_bad`, `_calls`, `_path_bad` and asserted against that marked copy (the course dichotomy stops when g = d: the copy loses its point for an extra call g = 1, d = 0). No official correction for the 2025 B2: found-value dichotomy count given as 3 (equality tested first), 4 mentioned as the 2-per-step alternative. Sources: Moodle `[algo] TAA - Types algébriques abstraits` ([doc] pages, exercice d'application) and the public EPITA algo wiki it links to (https://algo.infoprepa.epita.fr). Every « Évaluer : … » exercise is built with `t()`: a small model of the types in the same file (`_NS`, `ev`) evaluates the term at import time and asserts the hand-written answer (`indéfini` when a precondition fails), so a wrong answer stops `build.py`. Matière `algo` in `syllabus.json` (moodle `.`, two Moodle courses); the Caml ECUE is listed in `a_faire` (`algo-s1-caml`). Exercise page: code blocks wrap (`niveaux.css` `pre-wrap`) so axioms stay readable at 390 px.
- Algorithmics S1 Caml (2026-11-16): `parcours/src/algo_caml.py` → `algo-s1-caml` (14 levels, 90 exercises: expressions and types, functions, currying, if, exceptions, pattern matching and tuples, simple and multiple recursion (Fibonacci, Pascal, Hanoï), optimisation (wrapper functions, accumulators), lists, two lists / `e1 :: e2 :: l`, higher order; levels 13-14 are the B1 exams of October 2023 and 30 October 2024 from Past-Exams `S1/Midterms/Algo/2028|2029/CAML`, PDFs in `annales/raw`). Exercises are built with `ev()` (give Caml's toplevel answer) and `w()` (write the function: model code, its `val` line and the statement's examples). Every phrase is stored in `CHECKS` and replayed in a real OCaml 4.14 toplevel by `python3 parcours/check_caml.py` (one throwaway `alpine:3.20` container, `apk add ocaml`; needs Docker, not run by `build.py`). Run it after any change to the file. Model solutions use no predefined function except `failwith`/`invalid_arg` (exam rule), except where a statement says otherwise.
- Algorithmics S1 Python (2026-11-16): `parcours/src/algo_python.py` → `algo-s1-python` (15 levels, 70 exercises: operators and lazy booleans, loops, functions and in-place lists, `len`/`append`/`pop`, full traversals, sequential search, list properties, dichotomy, building lists, in-place deletion/insertion, lists of pairs, histogram/selection/merge sorts; levels 13-15 are the partiels P1 of 18 January 2021 and 4 January 2022 and the B2 exam of 7 January 2025). The Moodle course « Python et Environnement de Travail » only links to GitLab, so the path is calibrated on the 189 algo/prog PDFs of Epidocs Past-Exams downloaded to `annales/raw/S{1,2}/{Finals,Midterms,TDs}/{Algo,Prog}` (S1 finals algo = Python part of the B2 exam, `2028|2029` split into `PYTHON` and `TAA`). Checks run at import (so `build.py` fails on a wrong answer): `w()` replays the statement's `>>>` session on the model code, `pr()` runs the program and compares stdout, `_api()` rejects models that break the exam annex rule (only `len`, `range`, `append`, `pop()` without argument, `raise Exception`; no slice, no `in`, no operator on list literals). Dichotomy follows the decision tree of the official correction of January 2018 (inclusive bounds, `(left + right) // 2`, every node met costs 2 comparisons): official answers 8 (λ) and 32 (32768) are reproduced; for « longest list giving k + 2 comparisons » the official 65536 is not the maximum, the level asks for 131071 and explains it.
- Algorithmics S2 matrices (2026-11-16): `parcours/src/algo_matrices.py` → `algo-s2-matrices` (11 levels, 38 exercises: lists of lists and aliasing, building matrices with `append` only, full traversals (gap, minimax), searches with early stop, rows/columns/diagonals and symmetry, property tests (sorted matrix, sub-list, is matrix), transpose/product/rotation, magic square (Siamese method), grid paths (dungeon) and `mystery` traces; levels 10-11 = B3 « Matrices » exams of 12 March 2024 (scan) and 5 March 2025). Sources: Past-Exams `S2/Midterms/Algo/2028|2029/MATRICES` and official corrections of the C2 tests 2017-2020 and S2# (maxgap, searchMatrix, minimax, isSymmetric, Siamese, sub_line, dungeon, matrix_sorted). Model solutions are replayed and checked against the exam annex with the helpers of `algo_abg.py` (`_w`, `_api`); « what does it print » programs reuse `algo_python.pr`. The official 2020 `sub_line` (first version, `while j < colM - n`) misses a list at the end of a row: asserted in the module, the level teaches the `<=` bound. No official correction for the B3 exams.
- Algorithmics S2 binary and general trees (2026-11-16): `parcours/src/algo_abg.py` → `algo-s2-abg` (16 levels, 72 exercises: recursion (TD 1), vocabulary, measures (size, height, LC/LCE/LCI, PM/PME/PMI), special trees (degenerate, complete, perfect, locally complete), hierarchical numbering and occurrences, depth-first orders and linear form, measures and traversals in Python, breadth-first with `Queue` and level markers, tests, constructions (transpose, hierarchical vector both ways, `BinTreeSize`), searches (hierarchical number, kinship, prefix code), general trees in first child - right sibling form; levels 14-16 = B3 exams of 12 March 2024, 5 March 2025 and 10 March 2026). No Moodle course for S2 algo: sources are Past-Exams `S2/TDs/2030/Algo/B3`, `S2/Midterms/Algo/2028|2029|2030` (2024 and 2026 are scans, read as images) and the official corrections of the March 2019/2020 C2 tests; definitions follow the EPITA algo course mirror (height of root 0, empty tree -1, PMI = LCI / internal nodes). Trees are nested tuples `(key, left, right)` (bare value = leaf); every answer about a figure (orders, measures, numbers, conversions, `mystery` results) is computed from them at import, so `build.py` fails on a wrong figure answer. `w()` runs each model solution on `BinTree`/`Queue` objects built from the figures, replays the statement's `>>>` session, compares returned trees node by node and, with `fresh=True`, checks no input node is reused; `_api()` enforces the exam annex (only `len`, `range`, `append`, two-value `min`/`max`, `BinTree`, `Queue`, `str`, `print`; no slice, no `in`, no list operator). Figures: `fig()` writes SVG files to `static/arbres/abg-<hash>.svg` (in-order layout for binary trees, centred parents for general trees, wrap at 380 px so phone scale stays near 1) and returns a Markdown image (bleach keeps `img`; `data:` URIs are stripped, hence files). `niveaux.css` makes statement/solution images responsive. Remove `static/arbres/abg-*.svg` before a rebuild to drop stale figures. No official correction for the B3 exams: model answers are ours; the TD example `fibo_calls(4) == (3, 9)` is a typo (fibo(4) = 5).
- Blog section (2026-11-16): `/blog` and `/blog/<slug>` are served by the app (`blogsection.py`, `templates/blog.html`, `article.html`, nav link « Blog »). Articles are Markdown files `articles/<slug>.md` with a `---` block (`title`, `date` YYYY-MM-DD, `description`), rendered with the course Markdown+KaTeX renderer, listed newest first, picked up without restart. Add the URL to `static/sitemap.xml`. Caddy no longer serves `/blog/*` statically for this host (backup `Caddyfile.bak-edsblog-20261116`); old blogbot URLs `/blog/*.html` redirect (301) to `/blog/`. The old blogbot pages (`/opt/pierref/blog/epitadoomscrolling`) are unlinked and inaccurate (they describe a maths-only flashcard app): the blogbot daily batch still writes there for this site, its output is no longer shown. Tests: `tests/test_blog.py` (sets its own `DB_PATH` before importing `app`: any test importing `app` must do the same, or it writes into the real `cards.db`).
- Programming S1, start of C (2026-11-16): `parcours/src/prog_c_debut.py` → `prog-s1-c-debut` (8 levels, 58 exercises: compilation and `printf`, types and operators, conditions, loops, functions, arrays and strings, pointers, `malloc` and strings). **Not calibrated**: the official course is on prepa.pages.epita.fr (GitLab login), no prog PDF/TD/exam is on the server; content follows a standard first C course and must be recalibrated when the real material is found. Exercises use `pr()` (what does the program print) and `w()` (write the function, with the test `main` shown); every program is stored in `CHECKS` and compiled/run by `python3 parcours/check_c.py` (gcc in a throwaway `alpine:3.20` container; needs Docker, not run by `build.py`). Run it after any change to the file.

## Exam calendar (`/calendrier`) and « Copier pour une IA » (2026-11-16)

- **Calendar**: public page `/calendrier` (nav link « Examens »), `levels.exam_calendar(today)`. Data: key `calendrier` in `parcours/syllabus.json` (`debut`, optional `fin`, `titre`, `type`, `source`, and `ecue` = `matiere/semestre/id` or an explicit `parcours` list). Each date links to its paths and their first `examen` level (`/niveaux/<id>?n=K`). ECUEs with paths but no date are listed under « Date pas encore publiée » with their `periode_examen`. Sources: Auriga planning (events of type Examen, via the user's synced Google calendar) and Moodle S1-MATHS-2031 (remote tests). Update by hand when Auriga publishes new exams (S1 Jan., S2).
- **Calendar layout**: ink block with the next exam (countdown, « Faire l'examen blanc » = first exam level), school-year strip (red square = exam, grey = remote test, links to the month), upcoming exams grouped by month with a date tile (red for exams), a green progress bar per path for logged-in users, undated ECUEs and past exams folded in `<details>`.
- **Navbar**: under 640 px the links fold behind a three-line button (`.app-nav-burger`, script in `templates/nav.html`, Escape closes).
- **Copy for an AI**: under the statement of every paper exercise (`templates/niveau.html`, all subjects), button `#btn-copy-ia`, always visible. Before the correction it copies the statement with a « help me start without the answer » prompt; once the correction is shown (`static/niveaux.js`, `data-prompt-after`) it copies Markdown: a ready-made prompt (explain the correction step by step), the statement and the correction with formulas as LaTeX source, and a source line (exercise URL built from `PUBLIC_URL`, mention of https://morgan.pierref.eu). Script `static/copy-for-llm.js` is a vendored copy of the public library https://github.com/evaspace/copy-for-llm (source in `/opt/pierref/copy-for-llm`, MIT): update it there first, then copy it here and bump `?v=`.
- **Copy for an AI on cards**: home feed cards (`static/app.js` `buildCard`) and scroll cards (`static/scroll.js` `shell`) have an « IA » button in `.card-action-bar`. `static/card-copy.js` (`copyCardForLLM`) builds the text with the same library: question, QCM choices, the explanation only once the card is revealed (then an « explain it » prompt), source line = current page URL + https://morgan.pierref.eu.
- Tests: `test_exam_calendar`, `test_copy_for_ai_button` in `tests/test_levels.py`.
- **Calendar months**: every month of the strip (September to July) links to its own section (`months` in `exam_calendar`). An empty month says so and lists the undated ECUEs whose `periode_examen` names that month. Past months sit in the folded « Mois passés » section; a link to one opens it.
- **Exam dates tool** (about once a month): `.venv/bin/python tools/exam_dates.py` reads the iCal feeds `MOODLE_CALENDAR_URL` (Moodle > Calendrier > Exporter) and `AURIGA_ICS_URL` (EPITA planning .ics) from `.env`, keeps exams and tests, maps each to an ECUE by its title, and lists what is not yet in `syllabus.json`; `--apply` adds them (only the `calendrier` list is rewritten). No restart needed. Tests: `tests/test_exam_dates.py`.
- **Scroll cards like the feed** (`/scroll/<path>`, `static/scroll.js`): a right answer throws pixel confetti (`pixelConfetti`, now in `static/cat.js`, shared with the level page) and the cat claps; a wrong one makes the cat explode. True/false cards use the feed's markup and gesture: swipe right = vrai, left = faux (pointer events, so mouse drag works too), buttons stay as a fallback.
