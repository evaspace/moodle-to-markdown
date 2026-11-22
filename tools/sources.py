#!/usr/bin/env python3
"""Origin of each maths exercise: TD sheet, exam or written for the site, copied as is or adapted.

The source is the one already cited in the content (`src`); an exercise without one is « written
for the site ». Automatic attribution was tried and rejected (2026-11-22): the best matches of
uncited exercises were other exercises on the same topic, not the same exercise.
The text comparison only decides « copied as is » vs « adapted » for cited exercises: every statement is compared with every exercise of the source documents
(annales/md transcriptions + current-year Moodle TD sheets) on a normalised text: lowercase
letters and digits only, LaTeX commands dropped, so `$\\dfrac{2x}{x^2+1}$` and the PDF text
`2x / x2+1` both become `2xx21`. The score is the share of the statement's 8-character chunks
found in the source exercise, counting only chunks that appear in at most RARE source exercises
(boilerplate such as « montrer que pour tout » would otherwise match everything).

Output: parcours/origines.json {path id: {exo id: [origin of the exo, origin of variant 1, ...]}},
origin = {"src": label, "kind": "TD" | "Examen" | "site", "adapte": bool}, read by levels.py.

    python3 tools/sources.py            # write parcours/origines.json + print a summary
    python3 tools/sources.py --report   # also list every match with its score
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MOODLE = Path.home() / 'Documents/Business/mathsdoomscrolling/EPITA_Moodle_Notes_MD'
MOODLE_TD = [
    *sorted((MOODLE / "S1-MATHS-2031/03_Documents de travail - TD, corrections d'examens, etc/fichiers").rglob('*.md')),
    *sorted((MOODLE / 'S2-MATHS-2030/03_PDF utiles/fichiers/TD du semestre').glob('*_Etudiants.md')),
]
OUT = ROOT / 'parcours' / 'origines.json'
GRAM = 8
RARE = 4
COPY = 0.85   # share of rare chunks found in a source exercise to call the statement copied as is
SITE = {'src': 'Écrit pour le site', 'kind': 'site', 'adapte': False}
MODEL = {'src': 'Écrit pour le site sur le modèle des annales', 'kind': 'site', 'adapte': False}
# short citations written in the content -> full label
CITED = [(r'^TD3 ex\.', 'TD3 Primitives et intégrales S1 2031, ex.'), (r'; TD3 ex\.', '; TD3 Primitives et intégrales S1 2031, ex.')]
EXAM_WORDS = ('examen', 'contrôle', 'controle', 'partiel', 'final', 'mi-semestre', 'midterm', 'rattrapage', 'qcm',
              'annale', 'b1', 'b2', 'b3', 'b4')


def norm(text):
    text = re.sub(r'\\[a-zA-Z]+', ' ', text)                     # LaTeX commands
    text = unicodedata.normalize('NFKD', text.lower())             # x² -> x2, accents split off
    return ''.join(c for c in text if c.isascii() and c.isalnum())


def grams(s):
    return {s[i:i + GRAM] for i in range(len(s) - GRAM + 1)}


def kind_of(label):
    low = label.lower()
    if 'feuille de td' in low or re.match(r'td\s*\d', low) and 'contrôle' not in low:
        return 'TD'
    return 'Examen' if any(w in low for w in EXAM_WORDS) else 'TD'


def annales_docs():
    """(label, kind, [(exercise ref, normalised text)]) for each French annales transcription."""
    for f in sorted((ROOT / 'annales' / 'md').rglob('*.md')):
        if '-en' in f.stem or '/Phys/' in str(f) or '/Elec/' in str(f) or '/Archi/' in str(f):
            continue
        text = f.read_text(encoding='utf-8')
        h1 = re.search(r'^# (.+)$', text, re.M)
        if not h1:
            continue
        label = re.sub(r'\s*\((sujet|corrigé|correction|fichier)[^)]*\)', '', h1.group(1)).strip()
        label = re.sub(r'^Corr(ection|igé)( du| de la| de l\'| de)?\s+', '', label)
        label = label[0].upper() + label[1:]
        parts = re.split(r'^## (.+)$', text, flags=re.M)
        exos = []
        for head, body in zip(parts[1::2], parts[2::2]):
            m = re.match(r'(?:Exercice|Exercise|Question)\s+([\w.]+)', head)
            ref = f'ex. {m.group(1)}' if m else re.sub(r'\s*\(.*\)$', '', head).strip()
            body = '\n'.join(l for l in body.splitlines() if not l.startswith(('Type :', 'Formules :', '- Source')))
            exos.append((ref, norm(body)))
        yield label, kind_of(label), exos


def moodle_docs():
    """Moodle TD sheets (PDF text): exercises start at a line « Exercice 1.2 » (tables flattened)."""
    for f in MOODLE_TD:
        m = re.match(r'S(\d)_?(\d{4})_TD(\d+)_(.+?)_Etudiants', f.stem)
        if m:
            label = f'TD{m.group(3)} {m.group(4).replace("_", " ")} (S{m.group(1)} {m.group(2)})'
        else:
            label = f'TD séminaire {f.stem.replace("_", " ")}'
        exos, ref, buf = [], None, []
        for line in f.read_text(encoding='utf-8').splitlines():
            flat = ' '.join(c.strip() for c in line.split('|') if c.strip())
            hit = re.match(r'Exercice\s+(\d+(?:\.\d+)*)\b', flat)
            if hit and '. .' not in flat:
                if ref:
                    exos.append((ref, norm('\n'.join(buf))))
                ref, buf = f'ex. {hit.group(1)}', []
            elif ref:
                buf.append(flat)
        if ref:
            exos.append((ref, norm('\n'.join(buf))))
        yield label, 'TD', exos


def best_match(text, index, df):
    g = {x for x in grams(norm(text)) if df.get(x, 0) <= RARE}
    if len(g) < 3:
        return None, 0.0
    best, score = None, 0.0
    for label, kind, ref, sg in index:
        s = len(g & sg) / len(g)
        if s > score:
            best, score = (label, kind, ref), s
    return best, score


def origin(text, index, df, cited=None):
    """Origin of one statement, None if nothing is cited. `cited` = the `src` written in the content."""
    found, score = best_match(text, index, df)
    if not cited:
        return None, found, score
    if re.match(r'(Type annale|Rattrapage type)', cited):
        return MODEL, found, score
    for pat, full in CITED:
        cited = re.sub(pat, full, cited)
    return {'src': cited, 'kind': kind_of(cited), 'adapte': score < COPY}, found, score


def maths_paths():
    for f in sorted((ROOT / 'parcours').glob('*.json')):
        try:
            data = json.loads(f.read_text(encoding='utf-8'))
        except ValueError:
            continue
        if isinstance(data, dict) and str(data.get('subject', {}).get('id', '')).startswith('maths'):
            yield data


def main(report=False):
    index = [(label, kind, ref, grams(t)) for docs in (annales_docs(), moodle_docs())
             for label, kind, exos in docs for ref, t in exos if t]
    df = {}
    for *_, sg in index:
        for x in sg:
            df[x] = df.get(x, 0) + 1
    out, counts, lines = {}, {'TD': 0, 'Examen': 0, 'site': 0, 'adapte': 0, 'total': 0}, []
    for data in maths_paths():
        pid = data['subject']['id']
        for lvl in data['levels']:
            for exo in lvl['exos']:
                main_o, found, score = origin(exo['enonce'], index, df, exo.get('src'))
                res = [main_o or SITE]
                lines.append(f"{score:.2f} {pid}/{lvl['n']}/{exo['id']} -> {found}")
                for v in exo.get('variants', []):
                    vo, found, score = origin(v.get('enonce', exo['enonce']), index, df, v.get('src'))
                    if not vo and main_o:   # variant of a sourced exercise: adapted from it
                        vo = {**main_o, 'adapte': True}
                    res.append(vo or SITE)
                    lines.append(f"{score:.2f} {pid}/{lvl['n']}/{exo['id']}~v -> {found}")
                out.setdefault(pid, {})[exo['id']] = res
                for o in res:
                    counts['total'] += 1
                    counts[o['kind']] += 1
                    counts['adapte'] += o['adapte']
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    if report:
        print('\n'.join(sorted(lines, reverse=True)))
    print(f"{len(index)} source exercises; statements: {counts}")


if __name__ == '__main__':
    main('--report' in sys.argv)
