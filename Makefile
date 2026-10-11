# ==============================================================================
# 🐱 MATHSDOOMSCROLL ++ — Makefile Haute Performance
# Architecture unifiée : Plateforme Web Flask + Scraper Moodle + Pipeline IA Mistral
# Support officiel Promo 2030 (Blocs B1, B2, B3, B4 & ECUEs)
# ==============================================================================

# Couleurs ANSI pour un terminal ultra-lisible
BLUE   := \033[1;34m
GREEN  := \033[1;32m
CYAN   := \033[1;36m
YELLOW := \033[1;33m
RED    := \033[1;31m
PURPLE := \033[1;35m
BOLD   := \033[1m
RESET  := \033[0m

# ==============================================================================
# CONFIGURATION PAR DÉFAUT (surchargeable en ligne de commande)
# ==============================================================================

# Application Web
PORT          ?= 5000
HOST          ?= 0.0.0.0
DB_PATH       ?= cards.db

# Environnement Python
VENV          ?= .venv
PYTHON        ?= $(VENV)/bin/python
PIP           ?= $(VENV)/bin/pip

# Scraping Moodle EPITA
COOKIE        ?=
URL           ?= https://moodle.epita.fr
COURSE        ?=
LIMIT         ?=
OUTPUT        ?= EPITA_Moodle_Notes
DOWNLOAD_VIDEOS ?= 0

# Conversion Markdown
MD_SOURCE     ?= $(OUTPUT)
MD_TARGET     ?= EPITA_Moodle_Notes_MD

# Génération QCM Mistral AI
MISTRAL_KEY   ?=
QCM_INPUT     ?= $(MD_TARGET)
QCM_OUTPUT    ?= Generated_QCMs
QCM_MODEL     ?= open-mistral-7b
QCM_DELAY     ?= 0.8
QCM_LIMIT     ?=
QCM_COURSE    ?=
CONFIG_FILE   ?= selected_courses.json

# Serveur distant Hetzner
REMOTE_HOST       ?= hetzner
REMOTE_APP_DIR    ?= /opt/pierref/mathsdoomscroll
REMOTE_CONTAINER  ?= mathsdoomscroll_app

# Arguments dynamiques Scraper
SCRAPE_ARGS := --url "$(URL)" --output "$(OUTPUT)"
ifneq ($(strip $(COOKIE)),)
	SCRAPE_ARGS += --cookie "$(COOKIE)"
endif
ifneq ($(strip $(COURSE)),)
	SCRAPE_ARGS += --course "$(COURSE)"
endif
ifeq ($(DOWNLOAD_VIDEOS),1)
	SCRAPE_ARGS += --download-videos
endif

# Arguments dynamiques Générateur QCM
QCM_ARGS := --input "$(QCM_INPUT)" --output "$(QCM_OUTPUT)" --model "$(QCM_MODEL)" --delay $(QCM_DELAY) --config "$(CONFIG_FILE)"
ifneq ($(strip $(MISTRAL_KEY)),)
	QCM_ARGS += --api-key "$(MISTRAL_KEY)"
endif
ifneq ($(strip $(QCM_LIMIT)),)
	QCM_ARGS += --limit $(QCM_LIMIT)
endif
ifneq ($(strip $(QCM_COURSE)),)
	QCM_ARGS += --course "$(QCM_COURSE)"
endif

.DEFAULT_GOAL := help

# ==============================================================================
# MENU D'AIDE PRINCIPAL
# ==============================================================================

.PHONY: all help info check-env setup install

all: help

help:
	@echo ""
	@echo "$(BOLD)$(CYAN)==============================================================================$(RESET)"
	@echo "$(BOLD)$(YELLOW)  🐱 MATHSDOOMSCROLL ++ — Contrôle & Déploiement Intégral$(RESET)"
	@echo "$(BOLD)$(CYAN)==============================================================================$(RESET)"
	@echo "  $(BOLD)Plateforme Web :$(RESET) Flask / SQLite / Docker / Spaced Repetition"
	@echo "  $(BOLD)Pipeline IA    :$(RESET) Mistral AI ($(QCM_MODEL)) -> QCM & Flashcards LaTeX"
	@echo "  $(BOLD)Syllabus EPITA :$(RESET) Blocs B1, B2, B3, B4 & Sciences de l'Ingénieur"
	@echo ""
	@echo "$(BOLD)$(PURPLE)🌐 APPLICATION WEB & DEV LOCAL :$(RESET)"
	@echo "  $(GREEN)make serve$(RESET)            Lancer l'application web en local ($(BLUE)http://localhost:$(PORT)$(RESET))"
	@echo "  $(GREEN)make dev$(RESET)              Lancer en mode Debug avec rechargement à chaud"
	@echo "  $(GREEN)make open$(RESET)             Ouvrir l'application dans le navigateur par défaut"
	@echo ""
	@echo "$(BOLD)$(PURPLE)🐳 DOCKER LOCAL :$(RESET)"
	@echo "  $(GREEN)make docker-up$(RESET)        Démarrer l'application dans un conteneur en arrière-plan"
	@echo "  $(GREEN)make docker-down$(RESET)      Arrêter le conteneur Docker local"
	@echo "  $(GREEN)make docker-logs$(RESET)      Afficher les logs en direct du conteneur"
	@echo "  $(GREEN)make docker-restart$(RESET)   Redémarrer le conteneur local"
	@echo "  $(GREEN)make docker-build$(RESET)     Reconstruire l'image Docker locale"
	@echo ""
	@echo "$(BOLD)$(PURPLE)🧠 GÉNÉRATION QCM & FLASHCARDS IA (MISTRAL) :$(RESET)"
	@echo "  $(GREEN)make qcm$(RESET)              Générer sur tout avec reprise automatique ($(YELLOW)qcm_progress.json$(RESET))"
	@echo "  $(GREEN)make qcm-selected$(RESET)     Générer uniquement les 13 cours officiels majeurs"
	@echo "  $(GREEN)make qcm-status$(RESET)       Afficher les statistiques du tracker et cartes créées"
	@echo "  $(GREEN)make qcm-retry$(RESET)        Retenter automatiquement les fichiers ayant échoué"
	@echo "  $(GREEN)make qcm-reset$(RESET)        Réinitialiser le suivi du générateur"
	@echo "  $(GREEN)make qcm-test$(RESET)         Test de génération rapide sur 3 fichiers"
	@echo ""
	@echo "$(BOLD)$(PURPLE)🎯 RÉVISION PAR BLOC D'EXAMEN EPITA :$(RESET)"
	@echo "  $(GREEN)make qcm-b1$(RESET)           Bloc B1 : OBM (Logique/Complexes) + DP (Dénombrement/Probas)"
	@echo "  $(GREEN)make qcm-b2$(RESET)           Bloc B2 : ARITH (Arithmétique) + SR (Suites Réelles)"
	@echo "  $(GREEN)make qcm-b3$(RESET)           Bloc B3 : APEF (Polynômes/EDO/DL) + EV (Espaces Vectoriels)"
	@echo "  $(GREEN)make qcm-b4$(RESET)           Bloc B4 : EV (suite) + ALM (Applications Linéaires/Matrices)"
	@echo "  $(GREEN)make qcm-algo$(RESET)         Algorithmique : TAA (Types Abstraits) + OCaml (Récursivité)"
	@echo "  $(GREEN)make qcm-archi$(RESET)        Architecture : Archi S1 (Numération) + Archi S2 (Séquentiel)"
	@echo "  $(GREEN)make qcm-elec$(RESET)         Électronique : Circuits, Diodes, Filtres de Bode, Transitoires"
	@echo "  $(GREEN)make qcm-cyber$(RESET)        Cybersécurité & IA Générative"
	@echo ""
	@echo "$(BOLD)$(PURPLE)🚀 DÉPLOIEMENT & SERVEUR HETZNER :$(RESET)"
	@echo "  $(GREEN)make sync-server$(RESET)      Transférer les QCM générés et les injecter dans la prod"
	@echo "  $(GREEN)make sync-app$(RESET)         Déployer le code source (app.py, templates, static) sur Hetzner"
	@echo "  $(GREEN)make sync-md$(RESET)          Transférer l'ensemble des 4200+ cours Markdown sur le serveur"
	@echo "  $(GREEN)make sync-all$(RESET)         Synchronisation TOTALE (Code + Cours MD + QCM en base)"
	@echo "  $(GREEN)make server-status$(RESET)    État du conteneur en production et nombre de cartes"
	@echo "  $(GREEN)make server-logs$(RESET)      Logs en direct du serveur distant"
	@echo "  $(GREEN)make server-restart$(RESET)   Redémarrer l'application sur le serveur Hetzner"
	@echo "  $(GREEN)make server-shell$(RESET)     Ouvrir un shell dans le conteneur de production"
	@echo ""
	@echo "$(BOLD)$(PURPLE)📊 GESTION BASE DE DONNÉES (SQLITE) :$(RESET)"
	@echo "  $(GREEN)make db-stats$(RESET)         Statistiques locales détaillées (catégories, cartes)"
	@echo "  $(GREEN)make db-remote-stats$(RESET)  Statistiques de production sur Hetzner"
	@echo "  $(GREEN)make db-backup$(RESET)        Sauvegarder la base de données locale"
	@echo "  $(GREEN)make db-browse$(RESET)        Ouvrir le client interactif SQLite local"
	@echo ""
	@echo "$(BOLD)$(PURPLE)📥 SCRAPING & CONVERSION MOODLE :$(RESET)"
	@echo "  $(GREEN)make scrape$(RESET)           Lancer le scraper Moodle ($(YELLOW)COOKIE=\"...\"$(RESET))"
	@echo "  $(GREEN)make scrape-list$(RESET)      Lister les cours Moodle sans télécharger"
	@echo "  $(GREEN)make scrape-maths$(RESET)     Télécharger uniquement les cours de Mathématiques"
	@echo "  $(GREEN)make convert$(RESET)          Convertir les fichiers téléchargés en Markdown propre"
	@echo "  $(GREEN)make convert-test$(RESET)     Tester la conversion Markdown sur 15 fichiers"
	@echo ""
	@echo "$(BOLD)$(PURPLE)🧹 MAINTENANCE :$(RESET)"
	@echo "  $(GREEN)make clean$(RESET)            Nettoyer caches Python, temporaires et logs"
	@echo "  $(GREEN)make distclean$(RESET)        Nettoyage complet (y compris environnement virtuel .venv)"
	@echo "$(BOLD)$(CYAN)==============================================================================$(RESET)"
	@echo ""

# ==============================================================================
# GESTION DE L'ENVIRONNEMENT PYTHON
# ==============================================================================

setup: $(VENV)/bin/activate

$(VENV)/bin/activate:
	@echo "$(BOLD)$(BLUE)📦 [1/3] Création de l'environnement virtuel (.venv)...$(RESET)"
	python3 -m venv $(VENV)
	@echo "$(BOLD)$(BLUE)📦 [2/3] Mise à niveau de pip...$(RESET)"
	$(PIP) install --upgrade pip --quiet
	@echo "$(BOLD)$(BLUE)📦 [3/3] Installation des dépendances (requirements.txt)...$(RESET)"
	$(PIP) install -r requirements.txt --quiet
	@echo "$(BOLD)$(GREEN)✅ Environnement prêt et configuré !$(RESET)"

install: setup

check-env:
	@echo "$(BOLD)$(CYAN)🔍 Vérification des variables d'environnement...$(RESET)"
	@if [ -f .env ]; then echo "  $(GREEN)✔ Fichier .env présent$(RESET)"; else echo "  $(YELLOW)⚠ Fichier .env absent (recherche dans l'OS)$(RESET)"; fi
	@$(PYTHON) -c "import os; from dotenv import load_dotenv; load_dotenv(); k = os.getenv('MISTRAL_API_KEY'); print('  ' + ('$(GREEN)✔ Clé MISTRAL_API_KEY détectée (' + str(len(k)) + ' cars)$(RESET)' if k else '$(RED)✘ MISTRAL_API_KEY absente$(RESET)'))"

info:
	@echo "$(BOLD)$(CYAN)Informations Système & MathsDoomscroll :$(RESET)"
	@echo "  Python   : $$($(PYTHON) --version 2>/dev/null || echo 'Non installé')"
	@echo "  Dossier  : $$(pwd)"
	@echo "  Base DB  : $(DB_PATH) ($$([ -f $(DB_PATH) ] && ls -lh $(DB_PATH) | awk '{print $$5}' || echo 'inexistante'))"
	@echo "  Serveur  : $(REMOTE_HOST):$(REMOTE_APP_DIR)"

# ==============================================================================
# APPLICATION WEB FLASK & DÉVELOPPEMENT LOCAL
# ==============================================================================

serve: setup
	@echo "$(BOLD)$(GREEN)🌐 Lancement du serveur Web MathsDoomscroll...$(RESET)"
	@echo "👉 Rendez-vous sur : $(BOLD)$(CYAN)http://localhost:$(PORT)$(RESET)"
	@$(PYTHON) app.py

dev: setup
	@echo "$(BOLD)$(GREEN)⚡ Lancement en mode DEBUG avec rechargement automatique...$(RESET)"
	FLASK_DEBUG=1 FLASK_APP=app.py $(PYTHON) -m flask run --host=$(HOST) --port=$(PORT)

web: serve

open:
	@xdg-open "http://localhost:$(PORT)" 2>/dev/null || open "http://localhost:$(PORT)" 2>/dev/null || echo "Ouvrez http://localhost:$(PORT) dans votre navigateur."

# ==============================================================================
# DOCKER LOCAL
# ==============================================================================

docker-build:
	@echo "$(BOLD)$(BLUE)🐳 Construction de l'image Docker locale...$(RESET)"
	docker compose build

docker-up:
	@echo "$(BOLD)$(GREEN)🚀 Démarrage du conteneur MathsDoomscroll...$(RESET)"
	docker compose up -d
	@echo "👉 Application accessible sur : $(BOLD)$(CYAN)http://localhost:5080$(RESET)"

docker-down:
	@echo "$(BOLD)$(YELLOW)🛑 Arrêt des conteneurs Docker...$(RESET)"
	docker compose down

docker-restart: docker-down docker-up

docker-logs:
	docker compose logs -f app

docker-shell:
	docker exec -it mathsdoomscroll_app /bin/bash

# ==============================================================================
# GÉNÉRATION QCM & FLASHCARDS (MISTRAL AI)
# ==============================================================================

qcm: setup
	@echo "$(BOLD)$(GREEN)🧠 Lancement de la génération QCM / Flashcards (Mistral AI)...$(RESET)"
	$(PYTHON) generate_qcms.py $(QCM_ARGS)

qcm-selected: setup
	@echo "$(BOLD)$(GREEN)🎯 Génération ciblée sur les cours du Syllabus officiel...$(RESET)"
	$(PYTHON) generate_qcms.py $(QCM_ARGS) --selected

qcm-status: setup
	$(PYTHON) generate_qcms.py --input "$(QCM_INPUT)" --status

qcm-retry: setup
	@echo "$(BOLD)$(YELLOW)🔄 Retentative des fichiers ayant échoué...$(RESET)"
	$(PYTHON) generate_qcms.py $(QCM_ARGS) --retry-failed

qcm-reset: setup
	@echo "$(BOLD)$(RED)⚠ Réinitialisation du tracker de progression...$(RESET)"
	$(PYTHON) generate_qcms.py --reset

qcm-test: setup
	@echo "$(BOLD)$(CYAN)🧪 Test de génération rapide sur 3 fichiers...$(RESET)"
	$(PYTHON) generate_qcms.py $(QCM_ARGS) --limit 3

# Raccourcis par Bloc d'examen officiel EPITA Promo 2030
qcm-b1: setup
	@echo "$(BOLD)$(CYAN)📝 Génération Bloc B1 : OBM + DP (Maths S1)...$(RESET)"
	$(PYTHON) generate_qcms.py $(QCM_ARGS) --selected --course "S1-MATHS" --limit 20

qcm-b2: setup
	@echo "$(BOLD)$(CYAN)📝 Génération Bloc B2 : ARITH + SR (Maths S1)...$(RESET)"
	$(PYTHON) generate_qcms.py $(QCM_ARGS) --selected --course "S1-MATHS" --limit 20

qcm-b3: setup
	@echo "$(BOLD)$(CYAN)📝 Génération Bloc B3 : APEF + EV (Maths S2)...$(RESET)"
	$(PYTHON) generate_qcms.py $(QCM_ARGS) --selected --course "S2-MATHS" --limit 20

qcm-b4: setup
	@echo "$(BOLD)$(CYAN)📝 Génération Bloc B4 : EV + ALM (Maths S2)...$(RESET)"
	$(PYTHON) generate_qcms.py $(QCM_ARGS) --selected --course "S2-MATHS" --limit 20

qcm-algo: setup
	@echo "$(BOLD)$(CYAN)💻 Génération Algorithmique & OCaml...$(RESET)"
	$(PYTHON) generate_qcms.py $(QCM_ARGS) --course "algo"

qcm-archi: setup
	@echo "$(BOLD)$(CYAN)💻 Génération Architecture S1 & S2...$(RESET)"
	$(PYTHON) generate_qcms.py $(QCM_ARGS) --course "Archi"

qcm-elec: setup
	@echo "$(BOLD)$(CYAN)🔌 Génération Électronique (Circuits, Diodes, Filtres, Transitoires)...$(RESET)"
	$(PYTHON) generate_qcms.py $(QCM_ARGS) --course "Electronique"

qcm-cyber: setup
	@echo "$(BOLD)$(CYAN)🛡️ Génération Cybersécurité & IA...$(RESET)"
	$(PYTHON) generate_qcms.py $(QCM_ARGS) --course "Cyber"

# ==============================================================================
# SYNCHRONISATION & DÉPLOIEMENT SERVEUR (HETZNER)
# ==============================================================================

sync-server:
	@echo "$(BOLD)$(GREEN)🚀 [1/2] Transfert des cartes générées vers $(REMOTE_HOST)...$(RESET)"
	./sync_to_server.sh

sync-app:
	@echo "$(BOLD)$(BLUE)📦 Déploiement du code applicatif sur $(REMOTE_HOST):$(REMOTE_APP_DIR)...$(RESET)"
	rsync -avz --progress app.py init_db.py seed_data.py Dockerfile docker-compose.yml requirements.txt $(REMOTE_HOST):$(REMOTE_APP_DIR)/
	rsync -avz --progress templates/ $(REMOTE_HOST):$(REMOTE_APP_DIR)/templates/
	rsync -avz --progress static/ $(REMOTE_HOST):$(REMOTE_APP_DIR)/static/
	@echo "$(BOLD)$(GREEN)🔄 Redémarrage du conteneur en production...$(RESET)"
	ssh $(REMOTE_HOST) "cd $(REMOTE_APP_DIR) && docker compose restart"
	@echo "$(BOLD)$(GREEN)✅ Application mise à jour en production !$(RESET)"

sync-md:
	@echo "$(BOLD)$(BLUE)📦 Transfert des 4200+ cours Markdown vers $(REMOTE_HOST)...$(RESET)"
	ssh $(REMOTE_HOST) "mkdir -p $(REMOTE_APP_DIR)/EPITA_Moodle_Notes_MD"
	rsync -avz --progress $(MD_TARGET)/ $(REMOTE_HOST):$(REMOTE_APP_DIR)/EPITA_Moodle_Notes_MD/
	@echo "$(BOLD)$(GREEN)✅ Cours Markdown synchronisés !$(RESET)"

sync-all: sync-app sync-md sync-server
	@echo "$(BOLD)$(GREEN)🎉 DÉPLOIEMENT INTÉGRAL TERMINÉ AVEC SUCCÈS !$(RESET)"

server-status:
	@echo "$(BOLD)$(CYAN)📊 État du conteneur de production sur $(REMOTE_HOST) :$(RESET)"
	@ssh $(REMOTE_HOST) "docker ps --filter name=$(REMOTE_CONTAINER) --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'"
	@echo ""
	@echo "$(BOLD)$(CYAN)📚 Cartes actuellement en ligne dans la base de production :$(RESET)"
	@ssh $(REMOTE_HOST) "sqlite3 $(REMOTE_APP_DIR)/cards.db 'SELECT category.name, COUNT(card.id) AS total_cartes FROM card JOIN subcategory ON card.subcategory_id = subcategory.id JOIN category ON subcategory.category_id = category.id GROUP BY category.name ORDER BY total_cartes DESC;'"

server-logs:
	ssh $(REMOTE_HOST) "docker logs -f --tail 100 $(REMOTE_CONTAINER)"

server-restart:
	ssh $(REMOTE_HOST) "cd $(REMOTE_APP_DIR) && docker compose restart"

server-shell:
	ssh -t $(REMOTE_HOST) "docker exec -it $(REMOTE_CONTAINER) /bin/bash"

# ==============================================================================
# BASE DE DONNÉES (SQLITE)
# ==============================================================================

db-stats: setup
	@echo "$(BOLD)$(CYAN)📊 STATISTIQUES DE LA BASE DE DONNÉES LOCALE ($(DB_PATH)) :$(RESET)"
	@$(PYTHON) -c "import sqlite3, os; exit(0) if not os.path.exists('$(DB_PATH)') else None; conn = sqlite3.connect('$(DB_PATH)'); c = conn.cursor(); print(f'  • Total Cartes : {c.execute(\"SELECT COUNT(*) FROM card\").fetchone()[0]}'); print(f'  • Catégories   : {c.execute(\"SELECT COUNT(*) FROM category\").fetchone()[0]}'); print(f'  • Sous-cat.    : {c.execute(\"SELECT COUNT(*) FROM subcategory\").fetchone()[0]}'); print(f'  • Favoris      : {c.execute(\"SELECT COUNT(*) FROM favorite\").fetchone()[0]}\n'); rows = c.execute('SELECT cat.name, sc.name, count(c.id) FROM card c JOIN subcategory sc ON sc.id = c.subcategory_id JOIN category cat ON cat.id = sc.category_id GROUP BY cat.name, sc.name ORDER BY cat.name, sc.name').fetchall(); cur = None; [print(f'📁 {cat}:\n   └── {sub} : {n} carte(s)') if cat != cur and (cur := cat) else print(f'   └── {sub} : {n} carte(s)') for cat, sub, n in rows]"

db-remote-stats:
	@$(MAKE) server-status

db-backup:
	@mkdir -p backups
	@cp $(DB_PATH) backups/cards_$$(date +%Y%m%d_%H%M%S).db 2>/dev/null && echo "$(GREEN)✔ Sauvegarde locale créée dans backups/$(RESET)" || true
	@ssh $(REMOTE_HOST) "mkdir -p $(REMOTE_APP_DIR)/backups && cp $(REMOTE_APP_DIR)/cards.db $(REMOTE_APP_DIR)/backups/cards_$$(date +%Y%m%d_%H%M%S).db" && echo "$(GREEN)✔ Sauvegarde distante créée sur $(REMOTE_HOST)$(RESET)"

db-browse:
	sqlite3 $(DB_PATH)

# ==============================================================================
# SCRAPING MOODLE & BATCH CONVERT
# ==============================================================================

scrape: setup
	@echo "$(BOLD)$(BLUE)📥 Lancement du scraper Moodle EPITA...$(RESET)"
	$(PYTHON) main.py $(SCRAPE_ARGS)

run: scrape

sync: run

scrape-maths: setup
	$(PYTHON) main.py $(SCRAPE_ARGS) --course "Mathématiques"

scrape-list: setup
	$(PYTHON) main.py $(SCRAPE_ARGS) --list

scrape-no-files: setup
	$(PYTHON) main.py $(SCRAPE_ARGS) --no-files

convert: setup
	@echo "$(BOLD)$(BLUE)📝 Conversion des fichiers bruts en Markdown...$(RESET)"
	$(PYTHON) batch_convert.py --source "$(MD_SOURCE)" --target "$(MD_TARGET)"

convert-test: setup
	$(PYTHON) batch_convert.py --source "$(MD_SOURCE)" --target "$(MD_TARGET)" --test-limit 15

# ==============================================================================
# NETTOYAGE & MAINTENANCE
# ==============================================================================

clean:
	@echo "$(BOLD)$(YELLOW)🧹 Nettoyage des caches et temporaires...$(RESET)"
	rm -rf __pycache__ *.pyc *.pyo *.tmp state.json .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.py[cod]" -delete 2>/dev/null || true
	@echo "$(BOLD)$(GREEN)✔ Cache nettoyé avec succès !$(RESET)"

distclean: clean
	@echo "$(BOLD)$(RED)🧨 Suppression complète de l'environnement virtuel (.venv)...$(RESET)"
	rm -rf $(VENV)
	@echo "$(BOLD)$(GREEN)✔ Réinitialisation complète terminée !$(RESET)"
