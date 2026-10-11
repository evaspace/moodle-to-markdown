#!/usr/bin/env python3
"""
main.py - Lanceur CLI pour l'extraction complète des cours Moodle EPITA en Markdown.
Gère l'authentification (Cookie MoodleSession / Token), le parcours de l'arborescence,
la conversion des descriptions et équations MathJax, l'extraction des QCM et des vidéos,
et le téléchargement des fichiers.
"""

import argparse
import os
import sys
from typing import List

import config
from exporter import CourseExporter
from moodle_client import MoodleClient


def print_banner():
    banner = r"""
========================================================================
  🎓 EPITA Moodle Scraper & Markdown Notes Generator
  Extraction intégrale : Textes, LaTeX, Pages, QCM, Vidéos & Documents
========================================================================
"""
    print(banner)


def prompt_for_cookie(base_url: str) -> str:
    print("\n🔑 Aucune méthode d'authentification active trouvée dans config.py.")
    print("=" * 70)
    print("👉 Comment vous authentifier simplement avec votre compte EPITA Forge ID :")
    print(f"1. Connectez-vous sur {base_url} dans votre navigateur (Chrome/Firefox/Brave).")
    print("2. Appuyez sur F12 (Outils de développement).")
    print("3. Allez dans l'onglet 'Application' (ou 'Stockage') -> Cookies -> URL Moodle")
    print("4. Copiez la valeur du cookie nommé 'MoodleSession' (ex: abc123def456...)")
    print("=" * 70)

    try:
        cookie = input("\n👉 Collez votre cookie MoodleSession ici (ou Ctrl+C pour quitter) : ").strip()
        if cookie:
            save = input("💾 Voulez-vous enregistrer ce cookie dans config.py ? [O/n] : ").strip().lower()
            if save in ["", "o", "oui", "y", "yes"]:
                update_config_cookie(cookie)
        return cookie
    except (KeyboardInterrupt, EOFError):
        print("\n\nOpération annulée.")
        sys.exit(0)


def update_config_cookie(cookie_val: str):
    """Met à jour MOODLE_SESSION dans config.py."""
    cfg_path = os.path.join(os.path.dirname(__file__), "config.py")
    if os.path.exists(cfg_path):
        try:
            with open(cfg_path, "r", encoding="utf-8") as f:
                content = f.read()
            import re
            content = re.sub(
                r'MOODLE_SESSION\s*=\s*".*?"',
                f'MOODLE_SESSION = "{cookie_val}"',
                content,
            )
            with open(cfg_path, "w", encoding="utf-8") as f:
                f.write(content)
            print("✅ Cookie sauvegardé dans config.py !")
        except Exception as e:
            print(f"⚠️ Impossible d'écrire dans config.py : {e}")


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Scrape l'ensemble des cours Moodle EPITA pour les étudier en local au format Markdown."
    )
    parser.add_argument("--cookie", type=str, help="Valeur du cookie MoodleSession (Forge ID SSO)")
    parser.add_argument("--token", type=str, help="Token WebService Moodle (wstoken)")
    parser.add_argument("--username", "-u", type=str, help="Identifiant Moodle / CRI")
    parser.add_argument("--password", "-p", type=str, help="Mot de passe Moodle / CRI")
    parser.add_argument("--url", type=str, default=config.MOODLE_URL, help="URL de Moodle EPITA")
    parser.add_argument("--output", "-o", type=str, default=config.OUTPUT_DIR, help="Dossier de destination")
    parser.add_argument("--course", "-c", type=str, action="append", help="Filtrer un ou plusieurs cours par ID ou mot-clé")
    parser.add_argument("--list", "-l", action="store_true", help="Lister uniquement les cours inscrits sans télécharger")
    parser.add_argument("--no-files", action="store_true", help="Ne pas télécharger les documents (générer uniquement le Markdown)")
    parser.add_argument("--download-videos", action="store_true", help="Télécharger les vidéos en local avec yt-dlp")
    return parser.parse_args()


def main():
    print_banner()
    args = parse_arguments()

    base_url = args.url or config.MOODLE_URL
    token = args.token or config.MOODLE_TOKEN
    session_cookie = args.cookie or config.MOODLE_SESSION
    username = args.username or config.MOODLE_USERNAME
    password = args.password or config.MOODLE_PASSWORD
    output_dir = args.output or config.OUTPUT_DIR
    download_files = not args.no_files and config.DOWNLOAD_FILES
    download_videos = args.download_videos or config.DOWNLOAD_VIDEOS

    client = MoodleClient(base_url=base_url, token=token, session_cookie=session_cookie)

    # 1. Vérification si identifiants fournis pour token direct
    if not client.token and not client.session_cookie and username and password:
        print(f"🔑 Tentative de connexion directe avec l'identifiant '{username}'...")
        if client.authenticate_with_credentials(username, password):
            print("✅ Token obtenu avec succès via les identifiants !")
        else:
            print("⚠️ La connexion directe a échoué (normal avec le SSO Forge ID).")

    # 2. Validation de l'authentification existante
    is_valid, msg = client.validate_auth()

    # 3. Si non valide, demander interactivement le cookie MoodleSession
    if not is_valid:
        if sys.stdin.isatty():
            session_cookie = prompt_for_cookie(base_url)
            client = MoodleClient(base_url=base_url, token=token, session_cookie=session_cookie)
            is_valid, msg = client.validate_auth()

    if not is_valid:
        print(f"\n❌ Erreur d'authentification : {msg}")
        print("💡 Astuce : Récupérez votre cookie 'MoodleSession' après connexion sur https://moodle.epita.fr")
        print("   et lancez : python main.py --cookie \"VOTRE_COOKIE\"")
        sys.exit(1)

    print(f"\n✅ Authentification réussie : {msg}")
    print(f"🌐 Mode actif : {'API WebService REST' if client.auth_mode == 'token' else 'Web Scraping (Session Forge ID)'}")
    print(f"📁 Dossier d'export : {os.path.abspath(output_dir)}\n")

    # 4. Récupération de la liste des cours
    print("🔍 Récupération de la liste de vos cours inscrits...")
    enrolled_courses = client.get_enrolled_courses()

    if not enrolled_courses:
        print("❌ Aucun cours trouvé. Vérifiez que vous êtes bien inscrit à des cours sur cette plateforme.")
        sys.exit(1)

    print(f"📚 {len(enrolled_courses)} cours trouvés sur Moodle :")
    for idx, c in enumerate(enrolled_courses, 1):
        print(f"   [{idx:02d}] (ID: {c['id']}) {c['fullname']}")

    # Mode --list : quitter après affichage
    if args.list:
        print("\n✅ Mode liste terminé.")
        return

    # 5. Filtrage des cours si spécifié
    filter_criteria = args.course or config.COURSES_FILTER
    courses_to_process = []

    if filter_criteria:
        filter_criteria = [str(f).lower() for f in filter_criteria]
        for c in enrolled_courses:
            cid_str = str(c["id"]).lower()
            cname_str = c["fullname"].lower()
            if any(crit in cid_str or crit in cname_str for crit in filter_criteria):
                courses_to_process.append(c)

        print(f"\n🎯 Filtre appliqué : {len(courses_to_process)} cours sélectionné(s)")
        for c in courses_to_process:
            print(f"   • {c['fullname']}")
    else:
        courses_to_process = enrolled_courses

    if not courses_to_process:
        print("❌ Aucun cours ne correspond aux critères de filtre sélectionnés.")
        sys.exit(1)

    # 6. Initialisation de l'exportateur
    exporter = CourseExporter(
        client=client,
        output_dir=output_dir,
        download_files=download_files,
        download_videos=download_videos,
        state_file=config.STATE_FILE,
    )

    all_stats = {}
    print("\n" + "=" * 70)
    print("🚀 Début de l'extraction et de la génération des notes Markdown...")
    print("=" * 70)

    for c_idx, c in enumerate(courses_to_process, 1):
        cid = c["id"]
        cname = c["fullname"]
        print(f"\n📚 [{c_idx}/{len(courses_to_process)}] Traitement du cours : {cname} (ID: {cid})")
        print("   🔍 Analyse de l'arborescence et des sections...")

        course_data = client.get_course_details(cid)
        # Conserver le nom propre si renvoyé vide
        if not course_data.get("fullname"):
            course_data["fullname"] = cname

        sec_count = len(course_data.get("sections", []))
        print(f"   📂 {sec_count} sections/chapitres détectés. Extraction en cours...")

        stats = exporter.export_course(course_data)
        all_stats[str(cid)] = stats

        print(f"   ✅ Cours exporté :")
        print(f"      • {stats['sections']} sections rédigées en Markdown")
        print(f"      • {stats['pages']} pages de cours extraites")
        print(f"      • {stats['qcms']} QCM & tests répertoriés")
        print(f"      • {stats['videos']} vidéos / contenus interactifs")
        if download_files:
            print(f"      • {stats['files']} documents téléchargés")

    # 7. Génération du README global à la racine
    exporter.build_global_index(courses_to_process, all_stats)

    # 8. Résumé final
    total_sections = sum(s["sections"] for s in all_stats.values())
    total_pages = sum(s["pages"] for s in all_stats.values())
    total_qcms = sum(s["qcms"] for s in all_stats.values())
    total_videos = sum(s["videos"] for s in all_stats.values())
    total_files = sum(s["files"] for s in all_stats.values())

    print("\n" + "=" * 70)
    print("🎉 SYNCHRONISATION TERMINÉE AVEC SUCCÈS !")
    print("=" * 70)
    print(f"📊 Bilan général :")
    print(f"   • Cours traités : {len(courses_to_process)}")
    print(f"   • Sections / Chapitres : {total_sections}")
    print(f"   • Pages de cours créées : {total_pages}")
    print(f"   • QCM & Corrigés intégrés : {total_qcms}")
    print(f"   • Liens Vidéos & H5P : {total_videos}")
    if download_files:
        print(f"   • Fichiers & Feuilles de TD téléchargés : {total_files}")
    print(f"\n📂 Emplacement de vos notes : {os.path.abspath(output_dir)}")
    print("💡 Astuce : Ouvrez ce dossier dans Obsidian ou VS Code pour réviser et prendre des notes !")
    print("=" * 70)


if __name__ == "__main__":
    main()
