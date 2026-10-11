"""
config.py - Configuration pour le Scraper Moodle EPITA.
"""

# URL de la plateforme Moodle de l'EPITA
MOODLE_URL = "https://moodle.epita.fr"

# ==========================================
# AUTHENTIFICATION
# ==========================================
# Option 1 (Recommandée pour EPITA) : Cookie MoodleSession
# 1. Connectez-vous sur https://moodle.epita.fr via Forge ID dans votre navigateur.
# 2. F12 -> Onglet Application (ou Stockage) -> Cookies -> https://moodle.epita.fr
# 3. Copiez la valeur de 'MoodleSession' ci-dessous :
MOODLE_SESSION = ""

# Option 2 : Token d'API WebService (si généré dans Moodle -> Préférences -> Clés de sécurité)
MOODLE_TOKEN = ""

# Option 3 : Identifiants CRI directs
MOODLE_USERNAME = ""
MOODLE_PASSWORD = ""

# Optionnel : Clé API Mistral (pour le nettoyage automatique IA via batch_convert.py)
MISTRAL_API_KEY = ""

# ==========================================
# PARAMÈTRES D'EXPORTATION & TÉLÉCHARGEMENT
# ==========================================
# Dossier où seront créés tous les cours et notes Markdown
OUTPUT_DIR = "EPITA_Moodle_Notes"

# Télécharger les fichiers (PDF, polycopiés, TP, corrections, etc.)
DOWNLOAD_FILES = True

# Télécharger les vidéos en local avec yt-dlp (si False, les liens cliquables et aperçus sont intégrés en Markdown)
DOWNLOAD_VIDEOS = False

# Fichier de suivi de l'état (pour éviter de retélécharger les fichiers inchangés)
STATE_FILE = "state.json"

# Filtre de cours : liste vide [] pour TOUT scraper, ou liste de mots-clés / IDs
# Ex: COURSES_FILTER = ["Mathématiques"]
COURSES_FILTER = []
