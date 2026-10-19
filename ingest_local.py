import os
import sys
import glob
import argparse
import json
import re

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from app import parse_blocks, get_subcategory, db


def card_is_publishable(card):
    """Keep cards compatible with the one-answer-at-a-time web interface."""
    if not card.get('back') and card.get('type') != 'TF':
        return False, 'explication vide'
    if len(card.get('back') or '') > 600:
        return False, 'explication trop longue (>600 caractères)'

    math_text = f"{card.get('front', '')}\n{card.get('back', '')}"
    math_text = re.sub(r'```[\s\S]*?```|`[^`]*`', '', math_text)
    if math_text.count('$') % 2:
        return False, 'délimiteurs LaTeX $ non équilibrés'

    if card.get('type') == 'QCM':
        try:
            choices = json.loads(card.get('payload') or '{}').get('choices', [])
        except (TypeError, ValueError):
            return False, 'choix QCM illisibles'
        if len(choices) < 2:
            return False, 'QCM avec moins de deux choix'
        if not any(bool(choice.get('correct')) for choice in choices):
            return False, 'QCM sans réponse correcte'
    return True, None


def ingest_local(dry_run=False):
    import_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Generated_QCMs')
    files = sorted(glob.glob(os.path.join(import_dir, '*.txt')))
    if not files:
        print('Aucun fichier .txt à ingérer dans Generated_QCMs/.')
        return

    print(f'Trouvé {len(files)} fichiers à ingérer...')
    total_inserted = 0
    total_duplicates = 0
    total_errors = 0
    total_rejected = 0

    with db() as conn:
        cache = {}
        existing = {(r['type'], r['front']) for r in conn.execute('SELECT type, front FROM card')}
        for file_path in files:
            fname = os.path.basename(file_path)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    raw_text = f.read()
            except Exception as e:
                print(f'  [Erreur lecture] {fname}: {e}')
                total_errors += 1
                continue

            cards, errors = parse_blocks(raw_text)
            if errors:
                for err in errors:
                    print(f'  [Parse] {fname}: {err}')

            inserted = 0
            for c in cards:
                publishable, reason = card_is_publishable(c)
                if not publishable:
                    print(f'  [Rejet qualité] {fname}: {c["front"][:70]} — {reason}')
                    total_rejected += 1
                    continue

                card_key = (c['type'], c['front'])
                if card_key in existing:
                    total_duplicates += 1
                    continue

                sub_id = None
                if c['cat'] and not dry_run:
                    key = (c['cat'], c['sub'])
                    if key not in cache:
                        cache[key] = get_subcategory(conn, *key)
                    sub_id = cache[key]

                if not dry_run:
                    conn.execute(
                        'INSERT INTO card (subcategory_id, type, front, back, payload, status) VALUES (?, ?, ?, ?, ?, 0)',
                        (sub_id, c['type'], c['front'], c['back'], c['payload'])
                    )
                existing.add(card_key)
                inserted += 1
                total_inserted += 1

            if inserted:
                print(f'  ✅ {fname}: +{inserted} cartes')

    action = 'à insérer (dry-run)' if dry_run else 'insérées'
    print(f'\n✅ Terminé ! {action}: {total_inserted} | Doublons ignorés: {total_duplicates} | Cartes rejetées: {total_rejected} | Erreurs: {total_errors}')

    # Vérif finale
    import sqlite3
    from init_db import DB_PATH
    if not dry_run:
        conn2 = sqlite3.connect(DB_PATH)
        total = conn2.execute('SELECT COUNT(*) FROM card WHERE status=0').fetchone()[0]
        conn2.close()
        print(f'📊 Total cartes actives dans cards.db : {total}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Valider puis ingérer les cartes locales dans cards.db.')
    parser.add_argument('--dry-run', action='store_true', help='Auditer sans modifier la base locale.')
    ingest_local(dry_run=parser.parse_args().dry_run)
