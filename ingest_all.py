import os
import sys
import glob

# On s'assure d'être dans le bon dossier (dans le conteneur, c'est /app)
sys.path.append('/app')
from app import parse_blocks, get_subcategory, db

def ingest_queue():
    import_dir = '/app/import_queue'
    files = glob.glob(os.path.join(import_dir, '*.txt'))
    if not files:
        print('Aucun fichier .txt à ingérer.')
        return

    total_inserted = 0
    total_duplicates = 0
    
    with db() as conn:
        cache = {}
        for file_path in files:
            print(f'Traitement de {file_path}...')
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    raw_text = f.read()
            except Exception as e:
                print(f'  [Erreur de lecture] {e}')
                continue
                
            cards, errors = parse_blocks(raw_text)
            if errors:
                for err in errors:
                    print(f'  [Erreur de parsing] {err}')
                    
            inserted = 0
            for c in cards:
                # Vérifier les doublons
                if conn.execute('SELECT 1 FROM card WHERE type = ? AND front = ?', (c['type'], c['front'])).fetchone():
                    total_duplicates += 1
                    continue
                    
                sub_id = None
                if c['cat']:
                    key = (c['cat'], c['sub'])
                    if key not in cache:
                        cache[key] = get_subcategory(conn, *key)
                    sub_id = cache[key]
                    
                conn.execute(
                    'INSERT INTO card (subcategory_id, type, front, back, payload, status) VALUES (?, ?, ?, ?, ?, 0)',
                    (sub_id, c['type'], c['front'], c['back'], c['payload'])
                )
                inserted += 1
                total_inserted += 1
                
            print(f'  -> {inserted} cartes insérées.')
            
            # Marquer le fichier comme traité
            os.rename(file_path, file_path + '.done')

    print(f'Terminé. Total inséré: {total_inserted} (Doublons ignorés: {total_duplicates})')

if __name__ == '__main__':
    ingest_queue()
