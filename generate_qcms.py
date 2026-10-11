#!/usr/bin/env python3
"""
generate_qcms.py - Générateur automatique de QCM et Flashcards pour Doomscrolling EPITA.
Parcourt les notes Moodle au format Markdown (.md) et appelle l'API Mistral (tier gratuit)
pour générer des blocs compatibles avec le parser de l'application Flask (cards.db).

Comprend un système de reprise d'état (checkpointing / tracking) pour relancer à tout moment.

Auteur: Morgan Pierrefeu (@evaspace)
Licence: MIT
"""

import os
import sys
import json
import time
import argparse
from pathlib import Path
from typing import Dict, Any, Optional
import requests
from dotenv import load_dotenv

load_dotenv()

DEFAULT_INPUT_DIR = "EPITA_Moodle_Notes_MD"
DEFAULT_OUTPUT_DIR = "Generated_QCMs"
TRACKER_FILE = "qcm_progress.json"
DEFAULT_MODEL = os.getenv("MISTRAL_MODEL", "open-mistral-7b")

SYSTEM_PROMPT = """Tu es un professeur d'école d'ingénieurs (EPITA). Ton rôle est d'analyser le cours fourni et de générer des flashcards et QCM de haute qualité pédagogique au FORMAT TEXTE STRICT ci-dessous.

IMPORTANT: Ne réponds qu'avec les blocs de cartes. Aucun texte introductif, aucune conclusion, pas de balises de code Markdown (```).

Format strict attendu (chaque bloc séparé par "---") :

CAT: {Matière} / {Chapitre}
Q: [QCM] {Question précise sur une notion clé}
C1: [x] {Réponse correcte}
C2: {Distracteur plausible 1}
C3: {Distracteur plausible 2}
C4: {Distracteur plausible 3}
R: {Explication concise du pourquoi}
---
CAT: {Matière} / {Chapitre}
Q: [TF] {Affirmation technique vérifiable}
A: Vrai
R: {Démonstration ou contre-exemple rapide}
---
CAT: {Matière} / {Chapitre}
Q: {Titre ou concept clé du cours}
R: {Formule essentielle en LaTeX ou définition punchy}
---

Règles impératives :
1. Chaque bloc de carte DOIT commencer par "CAT:" puis "Q:".
2. Pour les QCM, la bonne réponse comporte obligatoirement "[x]". Les mauvaises n'en ont pas.
3. Pour les Vrai/Faux, utilise "A: Vrai" ou "A: Faux".
4. Pour les maths et formules, utilise la syntaxe LaTeX standard : $...$ pour inline et $$...$$ pour les équations.
5. Génère entre 3 et 6 cartes pertinentes par bloc de cours.
6. Ne paraphrase pas inutilement : concentre-toi sur les pièges classiques, définitions clés et théorèmes.
"""


def load_tracker(path: str = TRACKER_FILE) -> Dict[str, Any]:
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    if "files" not in data:
                        return {"files": data, "total_cards": 0}
                    return data
        except Exception as e:
            print(f"⚠️ Avertissement: Impossible de lire {path} ({e}), réinitialisation.")
    return {"files": {}, "total_cards": 0}


def save_tracker(tracker: Dict[str, Any], path: str = TRACKER_FILE) -> None:
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(tracker, f, indent=2, ensure_ascii=False)
    os.replace(tmp_path, path)


def count_cards(text: str) -> int:
    return len([b for b in text.split("---") if "Q:" in b])


def call_mistral(
    text: str,
    category: str,
    subcategory: str,
    api_key: str,
    model: str = DEFAULT_MODEL,
    max_retries: int = 3,
) -> Optional[str]:
    if not text.strip():
        return ""

    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    user_prompt = (
        f"Génère les cartes pour le cours suivant.\n"
        f"Matière : {category}\n"
        f"Chapitre : {subcategory}\n\n"
        f"--- CONTENU DU COURS ---\n{text}"
    )

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": 0.25,
    }

    for attempt in range(max_retries):
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=60)
            if resp.status_code == 200:
                data = resp.json()
                content = data["choices"][0]["message"]["content"].strip()
                # Nettoyage si le LLM a mis des ```markdown
                if content.startswith("```"):
                    lines = content.splitlines()
                    if lines and lines[0].startswith("```"):
                        lines = lines[1:]
                    if lines and lines[-1].strip() == "```":
                        lines = lines[:-1]
                    content = "\n".join(lines).strip()
                return content
            elif resp.status_code == 429:
                wait_time = 4 * (attempt + 1)
                print(f"    ⏳ Rate limit (429) atteint. Pause de {wait_time}s (tentative {attempt + 1}/{max_retries})...")
                time.sleep(wait_time)
            else:
                print(f"    ❌ Erreur HTTP {resp.status_code}: {resp.text[:120]}")
                time.sleep(2)
        except Exception as e:
            print(f"    ⚠️ Erreur réseau: {e}")
            time.sleep(2)

    return None


def show_status(input_dir: str, tracker: Dict[str, Any]) -> None:
    all_files = [f for f in Path(input_dir).rglob("*.md") if f.name.lower() != "readme.md"]
    total = len(all_files)
    files_tracked = tracker.get("files", {})
    done = sum(1 for v in files_tracked.values() if isinstance(v, dict) and v.get("status") == "DONE" or v == "DONE")
    skipped = sum(1 for v in files_tracked.values() if isinstance(v, dict) and v.get("status") == "SKIPPED")
    failed = sum(1 for v in files_tracked.values() if isinstance(v, dict) and v.get("status") == "FAILED")
    cards = tracker.get("total_cards", 0)

    print("=================================================================")
    print("📊 ÉTAT DU TRACKER DE GÉNÉRATION QCM / FLASHCARDS")
    print("=================================================================")
    print(f"  Fichiers .md détectés : {total}")
    print(f"  Traités avec succès   : {done}")
    print(f"  Ignorés (trop courts) : {skipped}")
    print(f"  Échoués (à re-tenter) : {failed}")
    print(f"  Restants              : {max(0, total - (done + skipped))}")
    print(f"  Cartes générées tot.  : {cards}")
    print("=================================================================")


def main():
    parser = argparse.ArgumentParser(
        description="Générateur de QCM & Flashcards via Mistral AI pour Moodle Doomscrolling."
    )
    parser.add_argument("--input", default=DEFAULT_INPUT_DIR, help="Dossier des cours Markdown source")
    parser.add_argument("--output", default=DEFAULT_OUTPUT_DIR, help="Dossier de sortie des QCM générés")
    parser.add_argument("--api-key", default="", help="Clé API Mistral (ou via MISTRAL_API_KEY dans .env)")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Modèle Mistral (défaut: {DEFAULT_MODEL})")
    parser.add_argument("--limit", type=int, default=0, help="Nombre max de fichiers à traiter (0 = illimité)")
    parser.add_argument("--course", default="", help="Filtrer par nom de cours (ex: 'algo', 'archi', 'maths')")
    parser.add_argument("--selected", action="store_true", help="Ne traiter que la sélection des cours majeurs de selected_courses.json")
    parser.add_argument("--config", default="selected_courses.json", help="Chemin du fichier de sélection des cours (défaut: selected_courses.json)")
    parser.add_argument("--delay", type=float, default=0.8, help="Délai entre requêtes en secondes (défaut: 0.8)")
    parser.add_argument("--status", action="store_true", help="Afficher les statistiques actuelles et quitter")
    parser.add_argument("--reset", action="store_true", help="Réinitialiser l'historique du tracker")
    parser.add_argument("--retry-failed", action="store_true", help="Retenter les fichiers marqués en échec")
    args = parser.parse_args()

    tracker = load_tracker()

    if args.reset:
        if os.path.exists(TRACKER_FILE):
            os.remove(TRACKER_FILE)
            print("🔄 Tracker réinitialisé.")
        tracker = {"files": {}, "total_cards": 0}

    if args.status:
        show_status(args.input, tracker)
        return

    api_key = args.api_key or os.getenv("MISTRAL_API_KEY")
    if not api_key:
        try:
            import config
            api_key = getattr(config, "MISTRAL_API_KEY", "")
        except ImportError:
            pass

    if not api_key:
        print("❌ Erreur: Aucune clé API Mistral trouvée.")
        print("Définissez MISTRAL_API_KEY dans votre fichier .env ou passez --api-key.")
        sys.exit(1)

    os.makedirs(args.output, exist_ok=True)

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"❌ Dossier introuvable : {args.input}")
        sys.exit(1)

    folder_mapping = {}
    if os.path.exists(args.config):
        try:
            with open(args.config, "r", encoding="utf-8") as f:
                cfg_data = json.load(f)
                for domain in cfg_data.get("domains", []):
                    for c in domain.get("courses", []):
                        folder_mapping[c.get("source_folder")] = c.get("category_name", c.get("title"))
        except Exception as e:
            print(f"⚠️ Avertissement lecture config {args.config}: {e}")

    all_files = [f for f in input_path.rglob("*.md") if f.name.lower() != "readme.md"]
    if args.selected and folder_mapping:
        all_files = [f for f in all_files if any(sf in str(f) for sf in folder_mapping.keys())]
    if args.course:
        all_files = [f for f in all_files if args.course.lower() in str(f).lower()]

    print(f"🔍 {len(all_files)} fichiers Markdown trouvés à analyser.")
    files_tracked = tracker.setdefault("files", {})

    processed_in_run = 0

    for i, md_file in enumerate(all_files, 1):
        if args.limit and processed_in_run >= args.limit:
            print(f"🛑 Limite atteinte ({args.limit} fichiers traités).")
            break

        rel_path = str(md_file.relative_to(input_path))
        track_info = files_tracked.get(rel_path)

        is_done = False
        if isinstance(track_info, dict):
            status = track_info.get("status")
            if status == "DONE" or (status == "SKIPPED" and not args.retry_failed):
                is_done = True
            elif status == "FAILED" and not args.retry_failed:
                is_done = True
        elif track_info == "DONE":
            is_done = True

        if is_done:
            continue

        try:
            with open(md_file, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()
        except Exception as e:
            print(f"⚠️ [{i}/{len(all_files)}] Impossible de lire {rel_path}: {e}")
            continue

        # Filtrage des fichiers vides ou stubs de navigation sans valeur pédagogique
        clean_text = content.strip()
        lines = [l.strip() for l in clean_text.splitlines() if l.strip() and not l.startswith("#")]
        text_without_headers = "\n".join(lines)

        if len(text_without_headers) < 180:
            files_tracked[rel_path] = {"status": "SKIPPED", "reason": "too_short"}
            save_tracker(tracker)
            continue

        parts = md_file.relative_to(input_path).parts
        raw_cat = parts[0] if len(parts) > 0 else "Général"
        category = folder_mapping.get(raw_cat, raw_cat)
        subcategory = parts[1] if len(parts) > 1 else "Général"

        # Nettoyage des préfixes éventuels (ex: '05_👨‍🏫 II - ' -> 'II - ')
        if subcategory.startswith(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")):
            import re
            subcategory = re.sub(r"^\d+_[^a-zA-Z0-9]*\s*", "", subcategory) or subcategory

        print(f"🚀 [{i}/{len(all_files)}] {category} > {subcategory} ({rel_path})")

        # Tronquage sécurisé pour respecter les tokens
        content_payload = clean_text[:14000]

        result = call_mistral(content_payload, category, subcategory, api_key, model=args.model)

        if result and ("Q:" in result or "CAT:" in result):
            cards_nb = count_cards(result)
            slug = re.sub(r"[^a-zA-Z0-9_\-]+", "_", f"{category}_{subcategory}_{md_file.stem}")[:80]
            out_filename = f"{slug}.txt"
            out_file = Path(args.output) / out_filename

            with open(out_file, "w", encoding="utf-8") as f:
                f.write(result + "\n")

            files_tracked[rel_path] = {
                "status": "DONE",
                "output_file": str(out_file),
                "cards_count": cards_nb,
                "timestamp": int(time.time()),
            }
            tracker["total_cards"] = tracker.get("total_cards", 0) + cards_nb
            save_tracker(tracker)
            processed_in_run += 1
            print(f"   ✅ {cards_nb} cartes générées -> {out_filename}")
        else:
            print(f"   ❌ Échec pour {rel_path}")
            files_tracked[rel_path] = {"status": "FAILED", "timestamp": int(time.time())}
            save_tracker(tracker)

        time.sleep(args.delay)

    print("\n🏁 Session terminée.")
    show_status(args.input, tracker)


if __name__ == "__main__":
    main()
