#!/usr/bin/env bash
set -Eeuo pipefail

REMOTE_HOST="${REMOTE_HOST:-hetzner}"
REMOTE_APP_DIR="${REMOTE_APP_DIR:-/opt/pierref/mathsdoomscroll}"
REMOTE_CONTAINER="${REMOTE_CONTAINER:-mathsdoomscroll_app}"
DB_PATH="${DB_PATH:-cards.db}"
STAGE_NAME="cards.db.upload.$$"

if [[ ! -s "$DB_PATH" ]]; then
  echo "Base locale absente ou vide : $DB_PATH" >&2
  exit 1
fi

snapshot="$(mktemp)"
trap 'python3 -c '\''import os,sys; os.unlink(sys.argv[1]) if os.path.exists(sys.argv[1]) else None'\'' "$snapshot"' EXIT
python3 - "$DB_PATH" "$snapshot" <<'PY'
import sqlite3, sys
with sqlite3.connect(sys.argv[1]) as source, sqlite3.connect(sys.argv[2]) as target:
    source.backup(target)
    check = target.execute("PRAGMA integrity_check").fetchone()[0]
    if check != "ok":
        raise SystemExit(f"Snapshot SQLite invalide : {check}")
PY

echo "Snapshot SQLite cohérent : $(du -h "$snapshot" | cut -f1)"
rsync -av "$snapshot" "$REMOTE_HOST:$REMOTE_APP_DIR/$STAGE_NAME"
ssh "$REMOTE_HOST" "cd '$REMOTE_APP_DIR' && REMOTE_CONTAINER='$REMOTE_CONTAINER' bash deploy_db_remote.sh '$STAGE_NAME'"
