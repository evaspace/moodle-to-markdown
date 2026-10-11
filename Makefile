# ==============================================================================
# PARAMÈTRES CONFIGURABLES
# Modifiez ces variables directement ici ou surchargez-les en ligne de commande :
# Ex: make run COOKIE="votre_cookie"
#     make maths COOKIE="votre_cookie"
#     make convert
#     make convert-test
# ==============================================================================

# Cookie MoodleSession (obtenu via DevTools F12 après connexion Forge ID SSO)
COOKIE ?=

# URL du Moodle EPITA
URL ?= https://moodle.epita.fr

# Dossier d'exportation brut des cours Moodle
OUTPUT ?= EPITA_Moodle_Notes

# Dossier d'exportation cible pour les cours convertis en Markdown (.md)
MD_SOURCE ?= $(OUTPUT)
MD_TARGET ?= EPITA_Moodle_Notes_MD

# Clé API Mistral (optionnelle, pour le nettoyage automatique des incohérences)
MISTRAL_KEY ?=

# Limite de fichiers à convertir (optionnel, pour tests ciblés)
LIMIT ?=

# Filtre de cours par défaut pour le scraper (laisser vide pour tout télécharger)
COURSE ?=

# Téléchargement des vidéos via yt-dlp (0 = désactivé, 1 = activé)
DOWNLOAD_VIDEOS ?= 0

# Environnement Python
VENV ?= .venv
PYTHON ?= $(VENV)/bin/python
PIP ?= $(VENV)/bin/pip

# Options dynamiques passées au scraper (main.py)
ARGS := --url "$(URL)" --output "$(OUTPUT)"
ifneq ($(strip $(COOKIE)),)
	ARGS += --cookie "$(COOKIE)"
endif
ifneq ($(strip $(COURSE)),)
	ARGS += --course "$(COURSE)"
endif
ifeq ($(DOWNLOAD_VIDEOS),1)
	ARGS += --download-videos
endif

# Options dynamiques passées au convertisseur Markdown (batch_convert.py)
CONVERT_ARGS := --source "$(MD_SOURCE)" --target "$(MD_TARGET)"
ifneq ($(strip $(MISTRAL_KEY)),)
	CONVERT_ARGS += --mistral-key "$(MISTRAL_KEY)"
endif
ifneq ($(strip $(LIMIT)),)
	CONVERT_ARGS += --test-limit $(LIMIT)
endif

.PHONY: all help setup install run sync maths math list no-files convert convert-test clean

all: help

help:
	@echo "========================================================================"
	@echo "🎓 Moodle to Markdown - Scraper & Batch Converter Guide"
	@echo "========================================================================"
	@echo "1. SCRAPING MOODLE (main.py) :"
	@echo "  make setup          : Crée le venv et installe toutes les dépendances"
	@echo "  make run            : Lance l'extraction complète (COOKIE=\"...\")"
	@echo "  make maths          : Télécharge uniquement les cours de Mathématiques"
	@echo "  make list           : Liste les cours sans rien télécharger"
	@echo "  make no-files       : Scrape les pages/QCM sans les pièces jointes lourdes"
	@echo ""
	@echo "2. CONVERSION MARKDOWN EN PARALLÈLE (batch_convert.py) :"
	@echo "  make convert        : Convertit toute l'arborescence vers MD_TARGET"
	@echo "  make convert-test   : Teste la conversion sur 15 fichiers uniquement"
	@echo ""
	@echo "3. MAINTENANCE :"
	@echo "  make clean          : Supprime les caches Python et fichiers temporaires"
	@echo ""
	@echo "Exemples d'utilisation :"
	@echo "  make run COOKIE=\"abc123...\""
	@echo "  make convert"
	@echo "  make convert-test"
	@echo "  make convert LIMIT=50"
	@echo "  make convert MD_SOURCE=\"EPITA_Moodle_Notes/S2-MATHS-2030\""
	@echo "  make convert MISTRAL_KEY=\"votre_cle_api\""
	@echo "========================================================================"

setup: $(VENV)/bin/activate

$(VENV)/bin/activate:
	@echo "📦 Création du venv et installation des dépendances..."
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@echo "✅ Environnement prêt !"

install: setup

run: setup
	$(PYTHON) main.py $(ARGS)

sync: run

maths: setup
	$(PYTHON) main.py $(ARGS) --course "Mathématiques"

math: maths

list: setup
	$(PYTHON) main.py $(ARGS) --list

no-files: setup
	$(PYTHON) main.py $(ARGS) --no-files

convert: setup
	$(PYTHON) batch_convert.py $(CONVERT_ARGS)

convert-test: setup
	$(PYTHON) batch_convert.py --source "$(MD_SOURCE)" --target "$(MD_TARGET)" --test-limit 15

clean:
	rm -rf __pycache__ *.pyc *.pyo *.tmp state.json
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@echo "🧹 Cache nettoyé !"
