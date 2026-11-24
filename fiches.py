"""Course notion sheets (`fiches/<ID>.md`, id `MATIERE-chap.section`) and their checks.

Front-matter: id, syllabus (ECUE key of parcours/syllabus.json), type, papier (`<path id>/<level n>` or empty),
prereq and alias (comma-separated). `python3 fiches.py` checks duplicate ids and broken prereq/papier/body links;
`.venv/bin/python fiches.py --index` also rebuilds the Pagefind index in static/pagefind (commit it: the site has no build step).
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FICHES_DIR = ROOT / 'fiches'
TYPES = {'définition', 'théorème', 'méthode', 'exemple'}
LINK_RE = re.compile(r'/cours/fiches/([A-Z]+-[0-9]+\.[0-9]+)')


def parse(text):
    """'---' front-matter + Markdown body -> (meta dict, body). List fields are split on commas."""
    _, head, body = text.split('---\n', 2)
    meta = dict(line.split(': ', 1) if ': ' in line else (line.rstrip(':'), '') for line in head.splitlines())
    for key in ('prereq', 'alias'):
        meta[key] = [v.strip() for v in meta.get(key, '').split(',') if v.strip()]
    return meta, body


def load_all():
    """{file stem: (meta, body)} for every sheet."""
    return {p.stem: parse(p.read_text(encoding='utf-8')) for p in sorted(FICHES_DIR.glob('*.md'))}


def check():
    """List of problems: duplicate or misnamed ids, unknown type/ECUE, broken prereq, unknown path or level."""
    fiches, errors, seen = load_all(), [], set()
    levels = {}
    for p in (ROOT / 'parcours').glob('*.json'):
        data = json.loads(p.read_text(encoding='utf-8'))
        if 'subject' in data:
            levels[data['subject']['id']] = {lv['n'] for lv in data['levels']}
    syllabus = json.loads((ROOT / 'parcours' / 'syllabus.json').read_text(encoding='utf-8'))
    ecues = {e['id'] for m in syllabus['matieres'] for s in m['semestres'] for e in s['ecues']}
    for stem, (meta, body) in fiches.items():
        errors += [f'{stem}: link to missing fiche {r}' for r in LINK_RE.findall(body) if r not in fiches]
        fid = meta.get('id', '')
        if fid in seen:
            errors.append(f'{stem}: duplicate id {fid}')
        seen.add(fid)
        if fid != stem:
            errors.append(f'{stem}: id {fid!r} differs from the file name')
        if meta.get('type') not in TYPES:
            errors.append(f'{stem}: type {meta.get("type")!r} not in {sorted(TYPES)}')
        if meta.get('syllabus') not in ecues:
            errors.append(f'{stem}: syllabus {meta.get("syllabus")!r} is not an ECUE of syllabus.json')
        errors += [f'{stem}: prereq {r} does not exist' for r in meta['prereq'] if r not in fiches]
        if meta.get('papier'):
            path, _, n = meta['papier'].partition('/')
            if not n.isdigit() or int(n) not in levels.get(path, ()):
                errors.append(f'{stem}: papier {meta["papier"]} is not an existing level')
    return errors


def build_index(out=ROOT / 'static' / 'pagefind'):
    """Render every sheet with the app, then let Pagefind (npx, free, no account) index them into `out`."""
    import shutil
    import subprocess
    import tempfile
    from app import app
    client = app.test_client()
    shutil.rmtree(out, ignore_errors=True)  # Pagefind adds hashed files: drop the previous index
    with tempfile.TemporaryDirectory() as site:
        for fid in load_all():
            page = Path(site, 'cours', 'fiches', f'{fid}.html')
            page.parent.mkdir(parents=True, exist_ok=True)
            resp = client.get(f'/cours/fiches/{fid}')
            assert resp.status_code == 200, (fid, resp.status_code)
            page.write_bytes(resp.get_data())
        subprocess.run(['npx', '--yes', 'pagefind@1.6.0', '--site', site, '--output-path', str(out),
                        '--force-language', 'fr'], check=True)


if __name__ == '__main__':
    if '--index' in sys.argv:
        build_index()
    problems = check()
    print('\n'.join(problems) or f'{len(load_all())} fiches OK')
    sys.exit(1 if problems else 0)
