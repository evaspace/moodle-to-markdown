#!/usr/bin/env python3
"""Daily consistent copy of cards.db (sqlite online backup, safe while the app writes) into backups/daily, keeps 14.

Cron: 30 3 * * * cd /opt/pierref/epitadoomscrolling && python3 tools/backup_db.py >> ~/.local/state/epita_backup.log 2>&1
Restore: stop the app, copy a backup over cards.db, delete cards.db-wal and cards.db-shm, start the app.
"""
import sqlite3
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KEEP = 14
out = ROOT / 'backups' / 'daily'
out.mkdir(parents=True, exist_ok=True)
dest = out / f"cards-{time.strftime('%Y%m%d')}.db"
src, dst = sqlite3.connect(ROOT / 'cards.db'), sqlite3.connect(dest)
with dst:
    src.backup(dst)
assert dst.execute('PRAGMA integrity_check').fetchone()[0] == 'ok', 'backup is corrupt'
src.close()
dst.close()
for old in sorted(out.glob('cards-*.db'))[:-KEEP]:
    old.unlink()
print(dest, dest.stat().st_size)
