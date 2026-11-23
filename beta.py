"""Admin beta (/admin/beta): revision planner built on the real EPITA timetable.

Pure functions, no Flask: the route in app.py feeds them. Inputs:
- the owner's courses (planning_cours.json, exported from auriga2google by tools/planning_cours.py),
- syllabus.json (ECUE -> level paths, exam dates),
- the owner's level progress and exercise log (exo_log).
Outputs: class progress vs own progress per ECUE (lateness), prerequisites to catch up first,
personal rhythm (success rate by hour, block length before fatigue), a day plan with breaks and
meals, and the « copie 20/20 » checklists. Decisions and reasons: README_OBJECTIFS.md, « Beta ».
"""
import json
import unicodedata
from datetime import datetime, time, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

TZ = ZoneInfo('Europe/Paris')
LESSON_TYPES = {'CM', 'TD', 'TP', 'SOU'}   # Auriga codes that move the course forward (SOU = soutien)
EVAL_TYPES = {'EVAL', 'EX'}

# Auriga course title -> syllabus ECUE key (matiere/semestre/id), when the titles differ.
# shortcut: S1 only, add a line when a new Auriga title appears (unmapped titles are listed on the page).
ALIASES = {
    'analyse : primitives, integrales et suites': 'maths/S1/APIS',
    'mecanique du point': 'physique/S1/Mécanique',
    'numeration': 'archi/S1/Numération',
    'algebre de boole': 'archi/S1/Algèbre de Boole',
    "outils d'analyse de circuits": "electronique/S1/Outils d'analyse de circuits",
    'python et environnement de travail': 'algo/S1/Algorithmique Python',
    'listes et matrices': 'algo/S1/Algorithmique Python',
    'c - les bases': 'prog/S1/Programmation C (début)',
}

# Being late in a prerequisite makes the dependent course hard: catch up the prerequisite first.
PREREQUIS = {
    'physique/S1/Mécanique': ['maths/S1/APIS', 'maths/S1/OBM'],
    "electronique/S1/Outils d'analyse de circuits": ['maths/S1/OBM'],
    'archi/S1/Algèbre de Boole': ['maths/S1/OBM'],
    'maths/S1/APIS': ['maths/S1/OBM'],
}
IMMINENT = 3   # days: an eval this close beats catching up its prerequisites
LATE = 15   # points of lateness (class % - my %) from which a course counts as late

# Day frame (« garder l'humanité »): fixed meals, a stop time for sleep, a daily cap, one evening off.
DAY_START, DAY_STOP = time(8, 0), time(22, 0)
MEALS = [(time(12, 0), time(13, 0), 'Déjeuner'), (time(19, 30), time(20, 15), 'Dîner')]
CAP_COURSE_DAY, CAP_FREE_DAY = 180, 300   # minutes of revision per day
EVENING_OFF = 5        # Saturday: nothing after 18:00
DEFAULT_GOOD_HOURS = {8: 3, 9: 3, 10: 3, 11: 3, 14: 1, 15: 1, 16: 2, 17: 2, 18: 2, 20: 2, 21: 1}

COPIE_20 = {
    'commun': [
        'Recopier la question en une ligne avant de répondre : on répond à ce qui est demandé, pas à côté.',
        'Une idée par ligne, les égalités alignées, rien de rayé au milieu : le correcteur lit en 10 secondes.',
        'Résultat final encadré, avec son unité ou son ensemble.',
        'Citer le théorème ou la règle utilisée et vérifier ses hypothèses à voix haute (« f est continue sur [a, b] car… »).',
        'Relire à la fin : signes, parenthèses, recopie des données de l\'énoncé.',
        'Bloqué : écrire ce qu\'on sait faire et admettre le résultat intermédiaire pour la suite (points partiels).',
    ],
    'maths': [
        'Annoncer le raisonnement : « Par récurrence », « Par l\'absurde », « Analyse-synthèse ».',
        'Récurrence : initialisation, hérédité, conclusion, les trois écrites.',
        'Quantificateurs dans le bon ordre, chaque variable introduite (« Soit x ∈ ℝ »).',
        'Intégrale : primitive vérifiée en la dérivant au brouillon ; borne du haut moins borne du bas.',
        'Suite / limite : nommer le théorème (gendarmes, monotone bornée) et la forme indéterminée levée.',
    ],
    'physique': [
        'Système, référentiel, repère et bilan des forces avant toute équation, avec un schéma.',
        'Projection sur les axes écrite composante par composante.',
        'Équation littérale d\'abord, application numérique ensuite.',
        'Vérifier l\'homogénéité (unités des deux côtés) avant de passer à la suite.',
        'Ordre de grandeur du résultat commenté en une phrase.',
    ],
    'electronique': [
        'Schéma redessiné avec les sens de courant et de tension choisis (convention récepteur / générateur).',
        'Nommer la loi utilisée : loi des mailles, des nœuds, diviseur de tension, Thévenin, Millman.',
        'Résultat littéral puis numérique, avec l\'unité (V, A, Ω).',
        'Vérifier un cas limite (R → 0 ou R → ∞) pour contrôler le signe.',
    ],
    'archi': [
        'Indiquer la base de chaque nombre (indice 2, 10, 16) et le nombre de bits.',
        'Dépassement de capacité et retenue : dire s\'il y en a un, même quand il n\'y en a pas.',
        'Table de vérité complète (2ⁿ lignes) avant la simplification ; tableau de Karnaugh avec les regroupements entourés.',
        'Vérifier l\'expression simplifiée sur deux lignes de la table.',
    ],
    'algo': [
        'OCaml : `let rec` pour une fonction récursive, `;;` à la fin, cas de base en premier dans le `match`.',
        'OCaml : `match` exhaustif (tous les constructeurs), `failwith "..."` pour les cas interdits demandés.',
        'Python : indentation de 4 espaces, `return` dans toutes les branches, pas de `print` à la place de `return`.',
        'Respecter le nom et la signature imposés par l\'énoncé, au caractère près.',
        'Tester à la main sur la liste vide et sur un élément.',
    ],
    'prog': [
        'C : type de retour et types des paramètres explicites, `;` à chaque instruction, accolades partout.',
        'C : variables initialisées, bornes des boucles vérifiées (`<` ou `<=`), pas de dépassement de tableau.',
        'Inclure les en-têtes nécessaires (`stdio.h`, `stdlib.h`) et `return 0;` dans `main`.',
        'Respecter le prototype imposé au caractère près.',
    ],
}

RECUPERATION = [
    'Pause = loin de l\'écran : marcher, boire de l\'eau, s\'étirer. Le téléphone et les réseaux ne reposent pas l\'attention.',
    'Toutes les 3 séances, une vraie pause de 20 à 30 minutes.',
    'Revoir le cours le soir même, même 20 minutes : c\'est le moment où on retient le plus pour le moins d\'effort.',
    'Se tester (exercices, cartes) plutôt que relire : relire donne l\'impression de savoir.',
    'Alterner les matières dans la journée plutôt qu\'un seul bloc de 4 heures sur la même.',
    'Dormir : la mémoire se consolide la nuit. Pas de révision après 22 h, coucher à heure fixe.',
    'Repas à heures fixes, un vrai petit-déjeuner, de l\'eau à côté de soi. Pas de café après 16 h.',
    'Un soir libre par semaine, sans culpabilité : sans repos on décroche au bout de quelques semaines.',
]


def norm(s):
    s = unicodedata.normalize('NFKD', s or '').encode('ascii', 'ignore').decode()
    return ' '.join(s.lower().split())


def ecues(syllabus):
    """{'matiere/S/id': {...}} for every ECUE of the registry."""
    out = {}
    for m in syllabus.get('matieres', []):
        for sem in m['semestres']:
            for e in sem['ecues']:
                out[f"{m['id']}/{sem['id']}/{e['id']}"] = dict(matiere=m['id'], semestre=sem['id'], titre=e['titre'],
                                                              parcours=e.get('parcours', []))
    return out


def ecue_of(title, reg):
    t = norm(title)
    for key, e in reg.items():
        if norm(e['titre']) == t:
            return key
    for prefix, key in ALIASES.items():
        if t.startswith(prefix) and key in reg:
            return key
    return None


def load_planning(path):
    """Courses as dicts with aware Paris datetimes; [] when the export is missing."""
    p = Path(path)
    if not p.exists():
        return []
    out = []
    for ev in json.loads(p.read_text()):
        out.append(dict(ev, debut=datetime.fromisoformat(ev['debut']).astimezone(TZ),
                        fin=datetime.fromisoformat(ev['fin']).astimezone(TZ)))
    return out


def syllabus_evals(syllabus, reg, events):
    """Exams and tests of syllabus.json « calendrier » (mails, Moodle) as EVAL events, for the ECUEs of the timetable.

    An entry names its ECUE (`ecue`) or its paths (`parcours`); the date has no hour: 08:00 is assumed."""
    seen = {ecue_of(ev['titre'], reg) for ev in events}
    auriga = {(ecue_of(ev['titre'], reg), ev['debut'].date()) for ev in events if ev['type'] in EVAL_TYPES}
    by_path = {p: k for k, e in reg.items() for p in e['parcours']}
    out = []
    for c in syllabus.get('calendrier', []):
        key = c.get('ecue') or next((by_path[p] for p in c.get('parcours') or [] if p in by_path), None)
        if key in seen and key in reg and c.get('debut'):
            a = datetime.fromisoformat(c['debut']).replace(hour=8, tzinfo=TZ)
            if (key, a.date()) in auriga:  # Auriga already has it, with the real hour
                continue
            out.append(dict(titre=reg[key]['titre'], type='EVAL', debut=a, fin=a + timedelta(hours=1), detail=c['titre']))
    return out


def advancement(events, reg, my_pct, now):
    """Per ECUE seen in the timetable: class progress (lessons done / planned), mine (paths), lateness, next eval.

    my_pct: {path_id: percent of the path}. Class progress is relative to the lessons Auriga knows today."""
    rows = {}
    for ev in events:
        key = ecue_of(ev['titre'], reg)
        if not key:
            continue
        r = rows.setdefault(key, dict(key=key, titre=reg[key]['titre'], matiere=reg[key]['matiere'],
                                      faits=0, total=0, eval=None, prochain=None, parcours=reg[key]['parcours']))
        if ev['type'] in LESSON_TYPES:
            r['total'] += 1
            r['faits'] += ev['fin'] <= now
            if ev['debut'] > now and (r['prochain'] is None or ev['debut'] < r['prochain']):
                r['prochain'] = ev['debut']
        elif ev['type'] in EVAL_TYPES and ev['debut'] <= now:
            r['eval_passee'] = True
        elif ev['type'] in EVAL_TYPES and (r['eval'] is None or ev['debut'] < r['eval']):
            r['eval'] = ev['debut']
    for r in rows.values():
        r['classe'] = round(100 * r['faits'] / r['total']) if r['total'] else 0
        pcts = [my_pct.get(p, 0) for p in r['parcours']]
        r['moi'] = round(sum(pcts) / len(pcts)) if pcts else 0
        r['retard'] = max(0, r['classe'] - r['moi'])
        r['jours_eval'] = (r['eval'].date() - now.date()).days if r['eval'] else None
    for r in rows.values():
        r['bloque_par'] = [rows[p]['titre'] for p in PREREQUIS.get(r['key'], [])
                           if p in rows and rows[p]['retard'] >= LATE]
        r['priorite'] = priority(r)
        r['conseil'] = conseil(r)
    return sorted(rows.values(), key=lambda r: -r['priorite'])


JOURS = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']


def conseil(r):
    """One concrete thing to do for this course now (« conseils par cours »)."""
    if r['jours_eval'] is not None and r['jours_eval'] <= IMMINENT:
        return (f"Évaluation dans {r['jours_eval']} j : refais les niveaux déjà vus et la fiche du chapitre, "
                "pas de nouveau chapitre. Relis la copie 20/20 la veille.")
    if r['bloque_par']:
        return f"Rattrape d'abord {', '.join(r['bloque_par'])} : sans ça les TD de ce cours ne passent pas."
    if r['retard'] >= LATE:
        return (f"{r['retard']} pts de retard : 2 séances par jour sur ce cours jusqu'à rejoindre la classe, "
                "en commençant par le premier niveau non validé.")
    if r['moi'] < 100 and r['prochain']:
        d = r['prochain']
        return f"À jour : fais le niveau suivant avant le prochain cours ({JOURS[d.weekday()]} {d.day}, {d:%H:%M}) pour arriver en avance."
    return "À jour : une séance de révision espacée par semaine suffit (/niveaux/revoir)."


def short(title):
    """Calendar label: « Mécanique du point - Dynamique… » -> « Mécanique du point »; keeps « C - Les bases »."""
    for sep in (' - ', ' : '):
        head, _, tail = title.partition(sep)
        if tail and len(head) >= 4:
            return ('À chaud : ' + short(tail)) if head == 'À chaud' else head
    return title


def next_eval(adv):
    """The closest upcoming evaluation among the courses, for the countdown block."""
    rows = [r for r in adv if r['eval']]
    return min(rows, key=lambda r: r['eval']) if rows else None


def week_grid(events, adv, monday, now, hours=None, block=None):
    """The week of `monday` for the calendar grid: courses, evals and planned revision blocks, JSON-ready.

    Each item: day (0-6), start/end in minutes since midnight, kind (cours / eval / revision), title,
    link to the first path of its ECUE, my % and the class %, advice. Revision blocks only from today on."""
    by_key = {r['key']: r for r in adv}
    items = []

    def add(day, a, b, kind, titre, key, extra=''):
        r = by_key.get(key)
        items.append(dict(jour=day, debut=a.hour * 60 + a.minute, fin=b.hour * 60 + b.minute, kind=kind,
                          titre=titre, court=short(titre), heure=f'{a:%H:%M}–{b:%H:%M}', detail=extra,
                          matiere=r['matiere'] if r else 'autre',
                          lien='/niveaux/' + r['parcours'][0] if r and r['parcours'] else None,
                          moi=r['moi'] if r else None, classe=r['classe'] if r else None,
                          conseil=r['conseil'] if r else ''))
    for d in range(7):
        day = monday + timedelta(days=d)
        for ev in events:
            if ev['debut'].date() == day:
                kind = 'eval' if ev['type'] in EVAL_TYPES else 'cours'
                add(d, ev['debut'], ev['fin'], kind, ev['titre'], ecue_of(ev['titre'], by_key),
                    ev.get('detail') or ' · '.join(x for x in (ev['type'], ev.get('salle')) if x))
        if day >= now.date():
            for p in plan_day(day, events, adv, hours, block, now if day == now.date() else None):
                add(d, p['debut'], p['fin'], 'revision', p['quoi'], p['key'], p['pourquoi'])
    return dict(lundi=monday.isoformat(), jours=[f'{JOURS[d][:3]}. {(monday + timedelta(days=d)).day}'
                                                for d in range(7)],
                aujourdhui=(now.date() - monday).days, maintenant=now.hour * 60 + now.minute, items=items)


def priority(r):
    """Lateness, plus urgency in the 3 weeks before an eval; a course done by the class and by me scores 0.
    Once its eval is past (and none is planned), lateness counts for a quarter: finals and later courses only."""
    p = r['retard'] // 4 if r.get('eval_passee') and not r['eval'] else r['retard']
    if r['jours_eval'] is not None and r['jours_eval'] <= 21:
        p += (21 - r['jours_eval']) * 4 + (10 if r['moi'] < 100 else 0)
    return p


def unmapped(events, reg):
    return sorted({ev['titre'] for ev in events if ev['type'] in LESSON_TYPES and not ecue_of(ev['titre'], reg)})


def rhythm(logs, min_total=40, min_hour=8):
    """Success rate by hour of the day from (at, ok) logs; None if there is not enough data yet."""
    if len(logs) < min_total:
        return None
    by = {}
    for at, ok in logs:
        n, good = by.get(at.hour, (0, 0))
        by[at.hour] = (n + 1, good + ok)
    return {h: dict(n=n, pct=round(100 * g / n)) for h, (n, g) in sorted(by.items()) if n >= min_hour}


def block_length(logs, gap=20, split=25, min_sessions=3):
    """Revision block length in minutes: 25 if success drops by 10+ points after 25 min of a session, else 45.

    Sessions are cut at pauses longer than `gap` minutes. Without 3 long sessions: 45 (default)."""
    sessions, cur = [], []
    for at, ok in sorted(logs):
        if cur and (at - cur[-1][0]) > timedelta(minutes=gap):
            sessions.append(cur)
            cur = []
        cur.append((at, ok))
    if cur:
        sessions.append(cur)
    early, late, long_ones = [0, 0], [0, 0], 0
    for s in sessions:
        if s[-1][0] - s[0][0] < timedelta(minutes=2 * split):
            continue
        long_ones += 1
        for at, ok in s:
            side = early if at - s[0][0] < timedelta(minutes=split) else late
            side[0] += 1
            side[1] += ok
    if long_ones < min_sessions or not early[0] or not late[0]:
        return dict(minutes=45, pause=10, raison='par défaut : pas encore 3 longues séances mesurées')
    e, l_ = round(100 * early[1] / early[0]), round(100 * late[1] / late[0])
    if e - l_ >= 10:
        return dict(minutes=25, pause=5, raison=f'ta réussite baisse après 25 min ({e} % puis {l_} %)')
    return dict(minutes=45, pause=10, raison=f'ta réussite tient sur une longue séance ({e} % puis {l_} %)')


def _at(day, t):
    return datetime.combine(day, t, TZ)


def free_slots(events, day):
    """Free (start, end) intervals of the day between DAY_START and the stop time, outside courses and meals."""
    stop = time(18, 0) if day.weekday() == EVENING_OFF else DAY_STOP
    busy = [(ev['debut'], ev['fin']) for ev in events if ev['debut'].date() == day]
    busy += [(_at(day, a), _at(day, b)) for a, b, _ in MEALS]
    busy.sort()
    slots, cur, end = [], _at(day, DAY_START), _at(day, stop)
    for a, b in busy:
        if a > cur:
            slots.append((cur, min(a, end)))
        cur = max(cur, b)
    if cur < end:
        slots.append((cur, end))
    return [(a, b) for a, b in slots if b - a >= timedelta(minutes=20)]


def plan_day(day, events, adv, hours=None, block=None, now=None):
    """Suggested blocks for one day: [{debut, fin, quoi, pourquoi, lien}], breaks included between blocks.

    1. each course of the day gets a 20-min « à chaud » review in the first free slot after it;
    2. the remaining time (up to the daily cap) is cut in blocks; the best hours (personal rhythm, else
       DEFAULT_GOOD_HOURS) go to the most urgent ECUE, a late prerequisite coming first unless the ECUE's
       eval is IMMINENT;
    3. an ECUE gets at most 2 blocks a day (alternating subjects helps memory)."""
    block = block or dict(minutes=45, pause=10)
    lessons = [ev for ev in events if ev['debut'].date() == day and ev['type'] in LESSON_TYPES]
    cap = CAP_COURSE_DAY if lessons else CAP_FREE_DAY
    slots = free_slots(events, day)
    if now:
        slots = [(max(a, now), b) for a, b in slots if b > now + timedelta(minutes=20)]
    plan, used = [], 0
    by_key = {r['key']: r for r in adv}

    def take(after, minutes):
        for i, (a, b) in enumerate(slots):
            start = max(a, after)
            if b - start >= timedelta(minutes=minutes):
                end = start + timedelta(minutes=minutes)
                slots[i:i + 1] = [s for s in ((a, start), (end + timedelta(minutes=block['pause']), b)) if s[1] > s[0]]
                return start, end
        return None

    for ev in lessons:
        got = take(ev['fin'], 20)
        if got:
            used += 20
            key = ecue_of(ev['titre'], by_key)
            plan.append(dict(debut=got[0], fin=got[1], quoi=f"À chaud : {ev['titre']}",
                             pourquoi='le cours du jour, relu le jour même', key=key,
                             lien='/niveaux/' + by_key[key]['parcours'][0] if key and by_key[key]['parcours'] else None))

    targets = []
    for r in adv:
        if r['priorite'] <= 0:
            continue
        imminent = r['jours_eval'] is not None and r['jours_eval'] <= IMMINENT
        late_pre = [] if imminent else [by_key[p] for p in PREREQUIS.get(r['key'], [])
                                        if p in by_key and by_key[p]['retard'] >= LATE]
        for pre in late_pre:
            targets.append((pre, f"prérequis de {r['titre']}, à rattraper d'abord ({pre['retard']} pts de retard)"))
        targets.append((r, reason(r)))
    seen, ordered = {}, []
    for r, why in targets:
        if r['eval'] and r['eval'].date() == day:  # too late on the eval day itself
            continue
        if seen.get(r['key'], 0) < 2:
            seen[r['key']] = seen.get(r['key'], 0) + 1
            ordered.append((r, why))

    # cut what is left into blocks, best hours first
    m = block['minutes']
    blocks = []
    for a, b in slots:
        t = a
        while b - t >= timedelta(minutes=m) and used + m * (len(blocks) + 1) <= cap:
            blocks.append(t)
            t += timedelta(minutes=m + block['pause'])
    score = (lambda h: hours[h]['pct'] if h in hours else 0) if hours else (lambda h: DEFAULT_GOOD_HOURS.get(h, 0))
    for t, (r, why) in zip(sorted(blocks, key=lambda t: -score(t.hour)), ordered):
        plan.append(dict(debut=t, fin=t + timedelta(minutes=m), quoi=r['titre'], pourquoi=why, key=r['key'],
                         lien='/niveaux/' + r['parcours'][0] if r['parcours'] else None))
    plan.sort(key=lambda p: p['debut'])
    return plan


def reason(r):
    parts = []
    if r['retard']:
        parts.append(f"{r['retard']} pts de retard sur la classe")
    if r['jours_eval'] is not None:
        parts.append(f"évaluation dans {r['jours_eval']} j")
    return ', '.join(parts) or 'entretien'


def week(events, now, days=7):
    """Courses of the next `days` days grouped by date."""
    end = now + timedelta(days=days)
    out = {}
    for ev in events:
        if now - timedelta(hours=2) <= ev['debut'] <= end:
            out.setdefault(ev['debut'].date(), []).append(ev)
    return sorted(out.items())
