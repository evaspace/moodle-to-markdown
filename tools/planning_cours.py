#!/usr/bin/env python3
"""Export the owner's EPITA timetable (Auriga, as synced by auriga2google) to planning_cours.json for /admin/beta.

Runs on the host (cron): reads the auriga2google Postgres through `docker exec`, keeps the account whose
e-mail is AURIGA_OWNER_EMAIL (from .env), writes the courses as JSON next to cards.db (mounted at /data).
The file is private (git-ignored): it is the owner's own timetable.
"""
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'planning_cours.json'
SQL = """SELECT COALESCE(json_agg(json_build_object('titre', s.title, 'type', s.activity_type_code,
       'debut', s.start_dt, 'fin', s.end_dt, 'salle', s.room) ORDER BY s.start_dt), '[]')
FROM course_snapshots s JOIN users u ON u.id = s.user_id
WHERE lower(u.email) = lower(:'email') AND s.status <> 'removed';"""


def env(name):
    if os.environ.get(name):
        return os.environ[name]
    for line in (ROOT / '.env').read_text().splitlines():
        if line.startswith(name + '='):
            return line.split('=', 1)[1].strip().strip('"\'')
    return ''


def main():
    email = env('AURIGA_OWNER_EMAIL')
    if not email:
        sys.exit('AURIGA_OWNER_EMAIL missing in .env')
    out = subprocess.run(['docker', 'exec', '-i', 'auriga_sync_db', 'sh', '-c',
                          'psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -At -v email="$1"', 'sh', email],
                         input=SQL, capture_output=True, text=True, check=True).stdout
    events = json.loads(out)
    if not events:  # keep the last good export rather than blanking the page
        sys.exit('no course found for the owner, planning_cours.json left as is')
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(json.dumps(events, ensure_ascii=False, indent=0))
    tmp.replace(OUT)
    print(f'{len(events)} courses -> {OUT}')


if __name__ == '__main__':
    main()
