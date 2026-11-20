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
from datetime import datetime

import config
from exporter import CourseExporter
from moodle_client import MoodleClient, SessionExpired


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
    parser.add_argument("--download-videos", action="store_true", help="Télécharger les vidéos en local (yt-dlp + vidéos hébergées par Moodle)")
    parser.add_argument("--video-quality", type=int, default=720, help="Hauteur max des vidéos téléchargées (défaut 720)")
    parser.add_argument("--youtube-cookies", type=str, default="", help="Fichier cookies.txt YouTube (requis si YouTube bloque : « Sign in to confirm you're not a bot »)")
    parser.add_argument("--workers", type=int, default=4, help="Téléchargements simultanés (défaut 4)")
    parser.add_argument("--delay", type=float, default=0.15, help="Délai minimal entre deux requêtes, en secondes (défaut 0.15)")
    parser.add_argument("--course-id", type=int, action="append", help="Scraper ce cours par son ID même s'il n'est pas listé (répétable)")
    parser.add_argument("--resume", action="store_true", help="Reprendre une exécution interrompue (cookie expiré) sans refaire les cours terminés")
    parser.add_argument("--verbose", "-v", action="store_true", help="Afficher les incidents et retries en direct")
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

    client = MoodleClient(base_url=base_url, token=token, session_cookie=session_cookie,
                          min_delay=args.delay, verbose=args.verbose)

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
            client = MoodleClient(base_url=base_url, token=token, session_cookie=session_cookie,
                                  min_delay=args.delay, verbose=args.verbose)
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

    known_ids = {c["id"] for c in enrolled_courses}
    for extra_id in args.course_id or []:
        if extra_id not in known_ids:
            enrolled_courses.append({"id": extra_id, "fullname": f"Cours {extra_id}", "shortname": "", "summary": "",
                                     "url": f"{base_url}/course/view.php?id={extra_id}"})

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
        workers=args.workers,
        video_quality=args.video_quality,
        youtube_cookies=args.youtube_cookies,
    )

    run = exporter.state.get("run", {}) if args.resume else {}
    done_ids = set(run.get("done", []))
    exporter.state["run"] = {"started": run.get("started") or datetime.now().isoformat(timespec="seconds"),
                             "done": sorted(done_ids), "stats": run.get("stats", {})}
    all_stats = dict(exporter.state["run"]["stats"])
    processed = []

    print("\n" + "=" * 70)
    print("🚀 Début de l'extraction et de la génération des notes Markdown...")
    if done_ids:
        print(f"   ↩️  Reprise : {len(done_ids)} cours déjà terminés ignorés")
    print("=" * 70)

    interrupted = False
    for c_idx, c in enumerate(courses_to_process, 1):
        cid, cname = c["id"], c["fullname"]
        if cid in done_ids:
            processed.append(c)
            continue
        print(f"\n📚 [{c_idx}/{len(courses_to_process)}] Traitement du cours : {cname} (ID: {cid})")
        try:
            course_data = client.get_course_details(cid)
            if not course_data.get("fullname"):
                course_data["fullname"] = cname
            n_mods = sum(len(s["modules"]) for s in course_data.get("sections", []))
            print(f"   📂 {len(course_data.get('sections', []))} sections, {n_mods} activités. Export en cours...")
            stats = exporter.export_course(course_data)
        except SessionExpired as e:
            interrupted = True
            print(f"\n🔒 {e}")
            print("   Le cookie MoodleSession a expiré. Reconnectez-vous dans le navigateur, copiez le nouveau cookie et relancez :")
            print('   python main.py --resume --cookie "NOUVEAU_COOKIE"')
            break
        except Exception as e:  # un cours défaillant ne doit pas arrêter les autres
            client.note_error(f"cours {cname} ({cid})", e)
            print(f"   ❌ Cours ignoré après erreur : {e}")
            continue

        all_stats[str(cid)] = stats
        processed.append(c)
        exporter.state["run"]["done"].append(cid)
        exporter.state["run"]["stats"] = all_stats
        exporter._save_state()
        print(f"   ✅ {stats['pages']} pages, {stats['qcms']} QCM ({stats['questions']} questions), "
              f"{stats['videos']} vidéos/liens, {stats['files']} fichiers, {stats['books']} livres, "
              f"{stats['forums']} forums" + (f", ⚠️ {stats['failed']} échecs" if stats["failed"] else ""))

    # 7. Index global + manifeste + rapport (même si interrompu : on garde ce qui est fait)
    exporter.build_global_index(processed, all_stats)
    report = exporter.write_report(processed, all_stats)
    if not interrupted:
        exporter.state.pop("run", None)
    exporter._save_state()

    # 8. Résumé final
    def total(key):
        return sum(s.get(key, 0) for s in all_stats.values())

    print("\n" + "=" * 70)
    print("⚠️  EXTRACTION INTERROMPUE (session expirée)" if interrupted else "🎉 SYNCHRONISATION TERMINÉE")
    print("=" * 70)
    print(f"   • Cours traités : {len(processed)}/{len(courses_to_process)}")
    print(f"   • Sections : {total('sections')} | Pages (livres inclus) : {total('pages')} | Autres modules : {total('others')}")
    print(f"   • QCM : {total('qcms')} ({total('questions')} questions) | Vidéos & liens : {total('videos')}")
    print(f"   • Fichiers téléchargés : {total('files')} | Échecs : {total('failed')} | Incidents : {len(client.errors)}")
    print(f"\n📂 Notes : {os.path.abspath(output_dir)}")
    print(f"📋 Rapport détaillé : {os.path.abspath(report)}")
    print("   Suite : make convert (PDF -> Markdown), make md-cards-b (QCM -> cartes), make sync-all (site)")
    print("=" * 70)
    if interrupted:
        sys.exit(2)


if __name__ == "__main__":
    main()
