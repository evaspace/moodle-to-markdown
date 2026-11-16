#!/usr/bin/env python3
"""Fetch exam dates from the Moodle and Auriga iCal feeds and merge them into parcours/syllabus.json.

Run about once a month:
    .venv/bin/python tools/exam_dates.py           # show what is new
    .venv/bin/python tools/exam_dates.py --apply   # add the new dates to the « calendrier » list

Feeds (secret URLs, in .env only):
    MOODLE_CALENDAR_URL  Moodle > Calendrier > Exporter le calendrier > « Tous les cours », « Événements récents
                         et à venir » > Obtenir l'URL du calendrier.
    AURIGA_ICS_URL       the .ics link of the EPITA planning (the one given to auriga2google).
The /calendrier page reads syllabus.json on each request: no restart needed.
"""
import argparse
import json
import re
import sys
import unicodedata
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

import requests

ROOT = Path(__file__).resolve().parent.parent
SYLLABUS = ROOT / 'parcours' / 'syllabus.json'
TZ = ZoneInfo('Europe/Paris')
EXAM = re.compile(r'\b(examen|exam|eval|partiel|midterm|final|test|contr[oô]le|qcm|rattrapage)', re.I)
STOP = {'et', 'de', 'des', 'du', 'la', 'le', 'les', 'l', 'd', 'a', 'en', 's1', 's2'}


def env(key):
    for line in (ROOT / '.env').read_text(encoding='utf-8').splitlines():
        if line.startswith(key + '='):
            return line.split('=', 1)[1].strip().strip('"\'')
    return ''


def words(text):
    t = unicodedata.normalize('NFKD', text.lower()).encode('ascii', 'ignore').decode()
    return {w for w in re.findall(r'[a-z0-9]+', t) if w not in STOP}


def parse_ics(text):
    """VEVENTs as dicts {summary, description, start: date, end: date}. Minimal RFC 5545 reader."""
    lines = re.sub(r'\r?\n[ \t]', '', text).splitlines()  # unfold
    events, ev = [], None
    for line in lines:
        if line == 'BEGIN:VEVENT':
            ev = {}
        elif line == 'END:VEVENT' and ev is not None:
            if 'start' in ev:
                ev.setdefault('end', ev['start'])
                events.append(ev)
            ev = None
        elif ev is not None and ':' in line:
            head, value = line.split(':', 1)
            name, params = head.split(';')[0].upper(), head.upper()
            value = value.replace('\\n', '\n').replace('\\,', ',').replace('\\;', ';')
            if name in ('SUMMARY', 'DESCRIPTION', 'CATEGORIES'):
                ev[name.lower()] = value
            elif name in ('DTSTART', 'DTEND'):
                d = to_date(value, params)
                if name == 'DTEND' and 'VALUE=DATE' in params:
                    d -= timedelta(days=1)  # all-day DTEND is exclusive
                ev['start' if name == 'DTSTART' else 'end'] = d
    return events


def to_date(value, params):
    if len(value) == 8:
        return datetime.strptime(value, '%Y%m%d').date()
    dt = datetime.strptime(value[:15], '%Y%m%dT%H%M%S')
    if value.endswith('Z'):
        return dt.replace(tzinfo=ZoneInfo('UTC')).astimezone(TZ).date()
    return dt.date()  # TZID=Europe/Paris or floating: already local


def ecue_for(text, syllabus):
    """'matiere/semestre/id' of the ECUE whose title words are all in the text, else None."""
    have = words(text)
    best = None
    for m in syllabus['matieres']:
        for s in m['semestres']:
            for e in s['ecues']:
                need = words(e['titre'])
                if need and need <= have and (best is None or len(need) > best[0]):
                    best = (len(need), f"{m['id']}/{s['id']}/{e['id']}")
    return best and best[1]


def candidates(events, source, syllabus, since):
    out = []
    for ev in events:
        text = ' '.join(ev.get(k, '') for k in ('summary', 'description', 'categories'))
        if ev['start'] < since or not EXAM.search(text):
            continue
        title = re.sub(r'\s*\((EVAL|EXAMEN)\)\s*$', '', ev.get('summary', '').strip(), flags=re.I)
        kind = 'Examen' if re.search(r'type:\s*examen|\beval\b|examen|partiel|final|midterm', text, re.I) else 'Test à distance'
        item = {'debut': ev['start'].isoformat()}
        if ev['end'] != ev['start']:
            item['fin'] = ev['end'].isoformat()
        item.update({'titre': title, 'type': kind, 'source': source})
        ecue = ecue_for(text, syllabus)
        if ecue:
            item['ecue'] = ecue
        out.append(item)
    return out


def key(item):
    return item['debut'], tuple(sorted(words(item['titre'])))


def merge(known, found):
    """New items (not already listed on the same start date with the same title), deduplicated."""
    seen = {key(k) for k in known}
    new = []
    for f in found:
        if key(f) not in seen:
            seen.add(key(f))
            new.append(f)
    return new


def write_calendar(items):
    """Replace only the « calendrier » list in syllabus.json, keeping the rest of the file as it is."""
    text = SYLLABUS.read_text(encoding='utf-8')
    start = text.index('"calendrier": [')
    end = text.index('\n ]', start) + 3
    block = json.dumps(items, ensure_ascii=False, indent=1).replace('\n', '\n ')
    text = text[:start] + '"calendrier": ' + block + text[end:]
    json.loads(text)
    SYLLABUS.write_text(text, encoding='utf-8')


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--apply', action='store_true', help='add the new dates to syllabus.json')
    args = ap.parse_args()
    syllabus = json.loads(SYLLABUS.read_text(encoding='utf-8'))
    today = date.today()
    since = date(today.year if today.month >= 9 else today.year - 1, 9, 1)
    found = []
    for var, source in (('MOODLE_CALENDAR_URL', 'Moodle'), ('AURIGA_ICS_URL', 'Auriga')):
        url = env(var)
        if not url:
            print(f'{var} absent de .env : source {source} ignorée (voir l\'aide en tête du script).')
            continue
        r = requests.get(url, timeout=30, headers={'Accept': 'text/calendar'})
        if r.status_code != 200 or 'BEGIN:VCALENDAR' not in r.text:
            print(f'{source} : réponse inattendue (HTTP {r.status_code}). URL expirée ?')
            continue
        evs = candidates(parse_ics(r.text), source, syllabus, since)
        print(f'{source} : {len(evs)} examens ou tests trouvés depuis le {since:%d/%m/%Y}.')
        found += evs
    known = syllabus.get('calendrier', [])
    new = merge(known, found)
    for n in new:
        print(f"  + {n['debut']}{' → ' + n['fin'] if 'fin' in n else ''}  {n['type']:16} {n['titre']}  [{n.get('ecue', 'ECUE non reconnue')}]")
    if not new:
        print('Rien de nouveau.')
    elif args.apply:
        write_calendar(sorted(known + new, key=lambda i: i['debut']))
        print(f'{len(new)} date(s) ajoutée(s) à {SYLLABUS.relative_to(ROOT)}. Vérifie /calendrier.')
    else:
        print('Relance avec --apply pour les ajouter.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
