#!/usr/bin/env bash
set -Eeuo pipefail

stage_name="${1:?staged database filename required}"
container="${REMOTE_CONTAINER:-mathsdoomscroll_app}"
cd "$(dirname "$0")"

mkdir -p backups
stamp="$(date +%Y%m%d_%H%M%S)"
backup="/app/backups/cards_${stamp}.db"

# Start the old/current app first so SQLite's online backup API can include WAL data.
docker compose up -d app
docker exec "$container" python -c 'import sqlite3,sys; s=sqlite3.connect("/app/cards.db"); d=sqlite3.connect(sys.argv[1]); s.backup(d); d.close(); s.close()' "$backup"
docker compose stop app
python3 -c 'from pathlib import Path; [Path(p).unlink(missing_ok=True) for p in ("cards.db-wal", "cards.db-shm")]'

if ! mv "$stage_name" cards.db; then
  docker compose start app
  exit 1
fi

docker compose up -d app
for attempt in $(seq 1 30); do
  if docker exec "$container" python -c 'import urllib.request; urllib.request.urlopen("http://127.0.0.1:5000/healthz", timeout=3)' >/dev/null 2>&1; then
    echo "Base restaurée et application saine. Sauvegarde : backups/cards_${stamp}.db"
    exit 0
  fi
  sleep 2
done

echo "La nouvelle base ne passe pas le health check ; restauration de la sauvegarde." >&2
docker compose stop app || true
python3 -c 'from pathlib import Path; [Path(p).unlink(missing_ok=True) for p in ("cards.db-wal", "cards.db-shm")]'
cp "backups/cards_${stamp}.db" cards.db
docker compose up -d app
exit 1
