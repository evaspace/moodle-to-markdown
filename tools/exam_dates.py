#!/usr/bin/env python3
"""Fetch exam dates from the Moodle and Auriga iCal feeds and merge them into parcours/syllabus.json.

Runs twice a day from the user crontab (7:05 and 19:05, `--apply`, log in ~/.local/state/epita_exam_dates.log).
By hand:
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
    envfile = ROOT / '.env'
    if not envfile.exists():  # mails only: no iCal feeds configured
        return ''
    for line in envfile.read_text(encoding='utf-8').splitlines():
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


# Moodle course codes that name no ECUE (category « 2627_I_INF_FISE_S01_CN_PC_MECA_1 »).
# shortcut: one entry per course seen in the feed, add new ones when « ECUE non reconnue » shows up.
ALIASES = {'meca': 'physique/S1/Mécanique', 'num': 'archi/S1/Numération', 'taa': 'algo/S1/Types algébriques abstraits',
           'oac': "electronique/S1/Outils d'analyse de circuits", 'pet': 'prog/S1/Programmation C (début)',
           # S3 course codes seen in Moodle mails (2627_I_INF_FISE_S03_<UE>_<code>, S3-2030 algo-<code>)
           'tb': 'electronique/S3/TB', 'ba': 'archi/S3/ASM68K', 'graphs': 'algo/S3/Graphes', 'thlr': 'algo/S3/THLR',
           'pse': 'maths/S3/PSE', 'al': 'maths/S3/AL'}
# Moodle sends one event when a test opens and one when it closes: merged into one item
PHASE = re.compile(r"\s+(s[’']ouvre|se termine|doit [eê]tre achev[ée]e?)\s*$", re.I)


def ecue_for(text, syllabus):
    """'matiere/semestre/id' of the ECUE whose title words are all in the text, or whose id and
    subject are both named (« MATHS APIS »), else a course-code alias, else None."""
    have = words(text)
    best = None
    for m in syllabus['matieres']:
        for s in m['semestres']:
            for e in s['ecues']:
                need = words(e['titre'])
                named = words(e['id']) <= have and words(m['id']) <= have
                if (need and need <= have or named) and (best is None or len(need) > best[0]):
                    best = (len(need), f"{m['id']}/{s['id']}/{e['id']}")
    return best[1] if best else next((v for k, v in ALIASES.items() if k in have), None)


MONTHS = ['janvier', 'fevrier', 'mars', 'avril', 'mai', 'juin', 'juillet', 'aout', 'septembre', 'octobre', 'novembre', 'decembre']
_DAY = r'(?:(?:lundi|mardi|mercredi|jeudi|vendredi|samedi|dimanche)\s+)?'
OPENING = re.compile(r'^ouverture le \w+ (\d{1,2}) (\w+) (\d{4}), \d\d:\d\d : (.+)$', re.I)
DATE_WORDS = re.compile(_DAY + r'(\d{1,2})(?:er)?\s+(' + '|'.join(MONTHS) + r')(?:\s+(\d{4}))?', re.I)
WEEK_OF = re.compile(r'semaine du (\d{1,2})(?:/(\d{1,2})|(?:er)? (' + '|'.join(MONTHS) + '))', re.I)
GRADES = re.compile(r'vos notes|notes? sur 20|notes? (?:d.examen )?disponibles?', re.I)  # results mails: private, no date to add
DATE_NUM = re.compile(_DAY + r'(?<![\d/])(\d{1,2})/(\d{1,2})(?:/(\d{2,4}))?(?![\d/])', re.I)
EXAM_SENTENCE = re.compile(r'aura lieu|auront lieu|examen|exam\b|partiel|test|qcm|contr[oô]le', re.I)


def _ascii(text):
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode()


def _year(day, month, sent, year=None):
    """Date from day/month; without a year, the one closest to the mail (announcements point ahead)."""
    try:
        if year:
            return date(int(year) + (2000 if int(year) < 100 else 0), month, day)
        d = date(sent.year, month, day)
        return d.replace(year=d.year + 1) if d < sent - timedelta(days=60) else d
    except ValueError:
        return None


def mail_event(subject, body, sent):
    """Pseudo-iCal event {summary, categories, start, end} from one Moodle mail, else None.
    subject: decoded Subject; body: plain text; sent: date of the mail."""
    subject = re.sub(r'\s+', ' ', re.sub(r'^\s*\[EPITA\]\s*', '', subject)).strip()  # \s+ also eats non-breaking spaces
    if re.match(r'^(re|tr|fwd?)\s*:', subject, re.I) or GRADES.search(subject + ' ' + body[:600]):
        return None
    m = OPENING.match(subject)  # « Ouverture le lundi 5 octobre 2026, 07:00 : Test 1 FR : ECUE DP »
    if m and _ascii(m[2]).lower() in MONTHS:
        d = date(int(m[3]), MONTHS.index(_ascii(m[2]).lower()) + 1, int(m[1]))
        return {'summary': m[4], 'categories': '', 'start': d, 'end': d}
    course, _, title = subject.partition(' : ') if ' : ' in subject else ('', '', subject)
    # the forum header repeats the post date (« par X, lundi 19 octobre 2026, 12:51 »): only the text after it
    text = body.split('-' * 20, 1)[-1] if '-' * 20 in body else body
    for chunk in [title] + [c for c in re.split(r'(?<=[.!?])\s+', text) if EXAM_SENTENCE.search(c)]:
        a = _ascii(chunk)
        if (w := WEEK_OF.search(a)) and (d := _year(int(w[1]), int(w[2]) if w[2] else MONTHS.index(w[3].lower()) + 1, sent)):
            return {'summary': title, 'categories': course, 'start': d, 'end': d + timedelta(days=4)}
        for rx in (DATE_WORDS, DATE_NUM):
            if (w := rx.search(a)):
                month = MONTHS.index(w[2].lower()) + 1 if rx is DATE_WORDS else int(w[2])
                d = _year(int(w[1]), month, sent, w[3]) if 1 <= month <= 12 else None
                if d and d >= sent:
                    return {'summary': title, 'categories': course, 'start': d, 'end': d}
    return None


def fetch_mails(since):
    """Pseudo-events from the EPITA mailbox (tools/epita_mail.py), mails sent since `since`."""
    import email
    import email.header
    import email.utils
    import html
    sys.path.insert(0, str(Path(__file__).parent))
    import epita_mail
    dec = lambda h: str(email.header.make_header(email.header.decode_header(h or '')))  # noqa: E731
    conn = epita_mail.imap()
    conn.select('INBOX', readonly=True)
    ids = set()
    # ASCII substrings only: Exchange refuses UTF-8 searches, and « controle » does not match « Contrôle »
    for w in ('examen', 'exam', 'partiel', 'controle', 'QCM', 'test', 'evaluation', 'valuation', 'ouverture', 'rattrapage', 'cours', 'CC'):
        ids |= set(conn.search(None, 'SINCE', since.strftime('%d-%b-%Y'), 'SUBJECT', f'"{w}"')[1][0].split())
    events = []
    for i in sorted(ids, key=int):
        msg = email.message_from_bytes(conn.fetch(i, '(BODY.PEEK[])')[1][0][1])
        body = ''
        for part in msg.walk():
            if part.get_content_type() in ('text/plain', 'text/html') and not part.get_filename():
                t = part.get_payload(decode=True).decode(part.get_content_charset() or 'utf-8', 'replace')
                body = html.unescape(re.sub(r'<[^>]+>', ' ', t)) if part.get_content_type() == 'text/html' else t
                break
        body = re.sub(r'\{mlang EN\}.*?\{mlang\}', ' ', body, flags=re.S)  # French part only
        sent = email.utils.parsedate_to_datetime(msg['Date']).astimezone(TZ).date()
        ev = mail_event(dec(msg['Subject']), re.sub(r'\s+', ' ', body), sent)
        if ev:
            events.append(ev)
    conn.logout()
    return events


def candidates(events, source, syllabus, since):
    out = []
    for ev in events:
        text = ' '.join(ev.get(k, '') for k in ('summary', 'description', 'categories'))
        if ev['start'] < since or not EXAM.search(text):
            continue
        title = re.sub(r'\s*\((EVAL|EXAMEN)\)\s*$', '', ev.get('summary', '').strip(), flags=re.I)
        title = PHASE.sub('', title)
        kind = ('Examen' if re.search(r'type:\s*examen|\beval\b|examen|partiel|final|midterm', text, re.I)
                else 'Contrôle' if re.search(r'contr[oô]le', text, re.I) else 'Test à distance')
        item = {'debut': ev['start'].isoformat()}
        if ev['end'] != ev['start']:
            item['fin'] = ev['end'].isoformat()
        item.update({'titre': title, 'type': kind, 'source': source})
        ecue = ecue_for(text, syllabus)
        if ecue:
            item['ecue'] = ecue
        sm = re.search(r'_S0?(\d)_|^S0?(\d)-\d{4}', ev.get('categories', ''))  # course codes carry the semester
        if sm:
            item['semestre'] = 'S' + (sm.group(1) or sm.group(2))
        same = next((o for o in out if o['titre'] == title), None)
        if same:  # « s'ouvre » + « se termine »: one item from the first start to the last end
            dates = sorted({same['debut'], same.get('fin', same['debut']), item['debut'], item.get('fin', item['debut'])})
            same['debut'], same['fin'] = dates[0], dates[-1]
            if same['fin'] == same['debut']:
                del same['fin']
        else:
            out.append(item)
    return out


def key(item):
    return item['debut'], tuple(sorted(words(item['titre'])))


def merge(known, found):
    """New items (not already listed on the same start date with the same title or type), deduplicated."""
    seen = {key(k) for k in known}
    typed = {(k['debut'], k['type']) for k in known}  # hand-written entries use other titles
    new, slots = [], set()
    # the same test often comes several times (Moodle feed, announcement, « Ouverture » mail, FR and EN):
    # an item without ECUE is dropped when another one has the same date and type
    for f in sorted(found, key=lambda f: 'ecue' not in f):
        slot = (f['debut'], f['type'], f.get('ecue'))
        if key(f) in seen or (f['debut'], f['type']) in typed or slot in slots \
                or ('ecue' not in f and any(s[:2] == slot[:2] for s in slots)):
            continue
        seen.add(key(f))
        slots.add(slot)
        new.append(f)
    return sorted(new, key=lambda f: f['debut'])


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
            if var == 'MOODLE_CALENDAR_URL':  # Auriga: the user has no link, mails replace it
                print(f'{var} absent de .env : source {source} ignorée (voir l\'aide en tête du script).')
            continue
        r = requests.get(url, timeout=30, headers={'Accept': 'text/calendar'})
        if r.status_code != 200 or 'BEGIN:VCALENDAR' not in r.text:
            print(f'{source} : réponse inattendue (HTTP {r.status_code}). URL expirée ?')
            continue
        evs = candidates(parse_ics(r.text), source, syllabus, since)
        print(f'{source} : {len(evs)} examens ou tests trouvés depuis le {since:%d/%m/%Y}.')
        found += evs
    try:
        evs = candidates(fetch_mails(since), 'Mail EPITA', syllabus, since)
        print(f'Mail EPITA : {len(evs)} examens ou tests trouvés depuis le {since:%d/%m/%Y}.')
        found += evs
    except SystemExit as e:  # no token yet, or Microsoft refused it: the other sources still run
        print(f'Mail EPITA ignoré : {e}')
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
