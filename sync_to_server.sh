#!/bin/bash
# sync_to_server.sh
# Transfère les QCMs générés vers le serveur et les insère dans la base de données.

LOCAL_DIR="Generated_QCMs"
REMOTE_HOST="hetzner"
REMOTE_APP_DIR="/opt/pierref/mathsdoomscroll"
REMOTE_IMPORT_DIR="$REMOTE_APP_DIR/import_queue"

if [ ! -d "$LOCAL_DIR" ]; then
    echo "❌ Le dossier $LOCAL_DIR n'existe pas. Lancez generate_qcms.py d'abord."
    exit 1
fi

echo "🚀 1/2. Envoi des QCMs générés vers le serveur..."
ssh $REMOTE_HOST "mkdir -p $REMOTE_IMPORT_DIR"
rsync -avz --progress "$LOCAL_DIR/" "$REMOTE_HOST:$REMOTE_IMPORT_DIR/"

echo "📦 2/2. Création du script d'ingestion et exécution dans le conteneur Docker..."
ssh $REMOTE_HOST "cat << 'EOF' > $REMOTE_APP_DIR/ingest_all.py
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
EOF"

# Exécute le script à l'intérieur du conteneur en cours d'exécution
echo "▶️ Exécution dans mathsdoomscroll_app..."
ssh $REMOTE_HOST "docker exec mathsdoomscroll_app python /app/ingest_all.py"

echo "✅ Synchronisation et ingestion terminées !"
