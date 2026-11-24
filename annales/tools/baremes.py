"""Build parcours/baremes.json: the « Copie 20/20 » examples, one list per level.

An example is one exercise of an OFFICIAL correction in annales/md (statement + `> ` solution
lines), with its points from the heading « (5,5 points) » and the exam total when the file gives them. Corrections written
for the site (« corrigé rédigé », « pas de corrigé officiel ») are left out: the copy shown as
the model must be the teachers' own (decision of 2026-11-24, PLAN_BETA étape 4).
The annales give points per exercise, almost never per step, so no step-level grid is invented.

Usage: python3 annales/tools/baremes.py   (also prints the paths evaluated within 14 days
that have levels without an example; parcours/build.py calls `warn_missing`).
"""
import glob, json, os, re, sys
from datetime import date, timedelta

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # annales/
OUT = os.path.join(ROOT, '..', 'parcours', 'baremes.json')
NOT_OFFICIAL = ('rédigé', 'pas de corrigé officiel')
HEAD = re.compile(r'^## (.+?)(?:\s*\((\d+(?:[.,]\d+)?)\s*(?:pts?|points?)\b[^)]*\))?\s*$', re.I | re.M)
NIVEAU = re.compile(r'· Niveau : (\S+/\d+)')
TOTAL = re.compile(r'(?:barème|noté|notée)\s*(?:sur|:)\s*(\d+)', re.I)
REAL_DATE = re.compile(r'Date réelle : ([^(.;]+)')


def num(s):
    return float(s.replace(',', '.'))


def solution_blocks(lines):
    """Markdown text where each run of `> ` solution lines is its own blockquote: a blank line
    before it (else it is glued to the question) and, under a numbered question, indented into it."""
    out, in_list = [], False
    for l in lines:
        if re.match(r'\d+\. ', l):
            in_list = True
        elif l and not l.startswith(('>', ' ')):
            in_list = False
        if l.startswith('>') and not (out and out[-1].lstrip().startswith('>')):
            out.append('')
        out.append(('    ' + l) if l.startswith('>') and in_list else l)
    return '\n'.join(out).strip()


def parse(path):
    """Official exercises of one correction file, as dicts; [] for a non-official correction."""
    text = open(path, encoding='utf-8').read()
    head = text.split('\n## ', 1)[0]
    if any(k in head.lower() for k in NOT_OFFICIAL):
        return []
    blocks = re.split(r'\n(?=## )', text)[1:]
    marks = [(HEAD.match(b), b) for b in blocks]
    m_total = TOTAL.search(head)
    total = int(m_total.group(1)) if m_total else sum(num(m.group(2)) for m, _ in marks if m and m.group(2))
    when = REAL_DATE.search(head)
    out = []
    for m, block in marks:
        niv = NIVEAU.search(block)
        if not (m and niv):
            continue
        lines = block.split('\n')
        # drop the heading, the Type and Formules lines: the copy is statement + solution only
        body = solution_blocks([l for l in lines[1:] if not l.startswith(('Type : ', 'Formules : '))])
        out.append({'niveau': niv.group(1), 'titre': m.group(1).strip(), 'points': num(m.group(2)) if m.group(2) else None,
                    'sur': (int(total) if total == int(total) else total) or None, 'date': when.group(1).strip() if when else '',
                    'fichier': os.path.relpath(path, ROOT), 'texte': body})
    return out


def build():
    by_level = {}
    for f in sorted(glob.glob(ROOT + '/md/**/*.md', recursive=True)):
        if re.search(r'correction|_COR', os.path.basename(f)) and not f.endswith('-en.md'):
            for ex in parse(f):
                by_level.setdefault(ex.pop('niveau'), []).append(ex)
    for exs in by_level.values():  # newest exam first: the folder name holds the promo year
        exs.sort(key=lambda e: re.search(r'/(\d{4})', e['fichier']).group(1), reverse=True)
    return dict(sorted(by_level.items()))


def warn_missing(today=None, days=14, root=None):
    """Lines « path: levels without a copy » for the paths evaluated in the next `days` days."""
    parcours = os.path.join(root or os.path.join(ROOT, '..'), 'parcours')
    syl = json.load(open(os.path.join(parcours, 'syllabus.json'), encoding='utf-8'))
    have = set(json.load(open(os.path.join(parcours, 'baremes.json'), encoding='utf-8'))['niveaux'])
    ecues = {f"{m['id']}/{s['id']}/{e['id']}": e['parcours']
             for m in syl['matieres'] for s in m['semestres'] for e in s['ecues']}
    today = today or date.today()
    soon = set()
    for ev in syl.get('calendrier', []):
        if today <= date.fromisoformat(ev['debut']) <= today + timedelta(days=days):
            soon |= set(ev.get('parcours') or ecues.get(ev.get('ecue'), []))
    sizes = {}
    for p in glob.glob(os.path.join(parcours, '*.json')):
        d = json.load(open(p, encoding='utf-8'))
        if isinstance(d, dict) and 'levels' in d:
            sizes[d['subject']['id']] = len(d['levels'])
    out = []
    for pid in sorted(soon & set(sizes)):
        missing = [n for n in range(1, sizes[pid] + 1) if f'{pid}/{n}' not in have]
        if missing:
            out.append(f"{pid}: {len(missing)}/{sizes[pid]} niveaux sans copie officielle ({', '.join(map(str, missing))})")
    return out


if __name__ == '__main__':
    levels = build()
    json.dump({'niveaux': levels}, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    n = sum(map(len, levels.values()))
    print(f'{n} exercices officiels sur {len(levels)} niveaux -> parcours/baremes.json')
    assert n and all((e['points'] is None or e['points'] > 0) and e['texte'] for v in levels.values() for e in v), 'empty example'
    for line in warn_missing():
        print('Avertissement :', line, file=sys.stderr)
