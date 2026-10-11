# 🎓 Moodle to Markdown (`moodle-to-markdown`)

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Moodle](https://img.shields.io/badge/Moodle-3.x%20%7C%204.x-orange.svg)](https://moodle.org/)
[![MarkItDown](https://img.shields.io/badge/Powered%20by-MarkItDown%20%26%20Mistral%20AI-success.svg)](https://github.com/microsoft/markitdown)

> **Universal Moodle scraper and batch course-to-markdown converter.**  
> Transform entire Moodle platforms and course archives (PDFs, Word docs, PowerPoint slides, Excel sheets, quizzes, lecture notes) into clean, beautifully formatted **Markdown (`.md`)** files ready for **Obsidian**, **VS Code**, **Logseq**, **Notion**, or **Typora**.

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
