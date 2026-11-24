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
import re
import unicodedata
from datetime import datetime, time, timedelta, timezone
from pathlib import Path
from urllib.parse import quote
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
    if r.get('eval_passee') and not r['eval']:
        return ("Examen passé : ce cours revient aux partiels de fin de semestre. 1 à 2 séances par semaine "
                "pour ne pas l'oublier, priorité aux cours qui ont une évaluation à venir.")
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


def course_cards(adv):
    """One card per course for /admin/beta, most urgent first: progress, lateness, eval, advice, link."""
    return [dict(titre=short(r['titre']), matiere=r['matiere'], moi=r['moi'], classe=r['classe'], retard=r['retard'],
                 faits=r['faits'], total=r['total'], jours_eval=r['jours_eval'],
                 eval=f"{JOURS[r['eval'].weekday()]} {r['eval'].day}/{r['eval'].month}" if r['eval'] else None,
                 bloque_par=[short(t) for t in r['bloque_par']], conseil=r['conseil'],
                 urgent=r['jours_eval'] is not None and r['jours_eval'] <= IMMINENT,
                 lien='/niveaux/' + r['parcours'][0] if r['parcours'] else None) for r in adv]


def rhythm_chart(hours):
    """Bars for the rhythm chart: the 3 best hours are marked."""
    if not hours:
        return None
    best = sorted((h for h in hours if DAY_START.hour <= h < DAY_STOP.hour), key=lambda h: -hours[h]['score'])[:3]
    return dict(barres=[dict(h=h, pct=v['pct'], n=v['n'], top=h in best) for h, v in hours.items()],
                meilleures=sorted(best))


def next_eval(adv):
    """The closest upcoming evaluation among the courses, for the countdown block."""
    rows = [r for r in adv if r['eval']]
    return min(rows, key=lambda r: r['eval']) if rows else None


def week_grid(events, adv, monday, now, hours=None, block=None, plan_for=None):
    """The week of `monday` for the calendar grid: courses, evals and planned revision blocks, JSON-ready.

    Each item: day (0-6), start/end in minutes since midnight, kind (cours / eval / revision), title,
    link to the first path of its ECUE, my % and the class %, advice, state (fait / manque / None).
    `plan_for(day)` gives the revision blocks of a day (default: plan_day from today on)."""
    by_key = {r['key']: r for r in adv}
    items = []
    plan_for = plan_for or (lambda day: plan_day(day, events, adv, hours, block, now if day == now.date() else None)
                            if day >= now.date() else [])

    def add(day, a, b, kind, titre, key, extra='', etat=None, lien=None):
        r = by_key.get(key)
        items.append(dict(jour=day, debut=a.hour * 60 + a.minute, fin=b.hour * 60 + b.minute, kind=kind,
                          titre=titre, court=short(titre), heure=f'{a:%H:%M}–{b:%H:%M}', detail=extra,
                          matiere=r['matiere'] if r else 'autre',
                          lien=lien or ('/niveaux/' + r['parcours'][0] if r and r['parcours'] else None),
                          moi=r['moi'] if r else None, classe=r['classe'] if r else None,
                          conseil=r['conseil'] if r else '', etat=etat))
    for d in range(7):
        day = monday + timedelta(days=d)
        for ev in events:
            if ev['debut'].date() == day:
                kind = 'eval' if ev['type'] in EVAL_TYPES else 'cours'
                add(d, ev['debut'], ev['fin'], kind, ev['titre'], ecue_of(ev['titre'], by_key),
                    ev.get('detail') or ' · '.join(x for x in (ev['type'], ev.get('salle')) if x))
        for p in plan_for(day):
            add(d, p['debut'], p['fin'], 'revision', p['quoi'], p['key'], p['pourquoi'], p.get('etat'), p.get('lien'))
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


def rhythm(logs, min_total=40, min_hour=8, expected=None):
    """Success rate by hour of the day from (at, ok) logs; None if there is not enough data yet.

    `expected` (same order as logs): the other users' success rate on each exercise. Then `score` =
    50 + my success minus the expected one, in points: a success on a hard exercise counts more, and an
    hour spent on easy exercises no longer looks good. Without it, score = pct. Plans rank hours by score."""
    if len(logs) < min_total:
        return None
    by = {}
    for i, (at, ok) in enumerate(logs):
        n, good, exp = by.get(at.hour, (0, 0, 0.0))
        by[at.hour] = (n + 1, good + ok, exp + (expected[i] if expected else 0))
    return {h: dict(n=n, pct=round(100 * g / n), score=round(50 + 100 * (g - e) / n) if expected else round(100 * g / n))
            for h, (n, g, e) in sorted(by.items()) if n >= min_hour}


def expected_rates(rows):
    """Other users' success rate per exercise, smoothed ((ok + 1) / (n + 2), so 0.5 when nobody did it).
    rows: [(account_id, key, ok)]; returns f(account_id, key) excluding that account's own answers."""
    tot = {}
    mine = {}
    for acc, key, ok in rows:
        n, g = tot.get(key, (0, 0))
        tot[key] = (n + 1, g + ok)
        n, g = mine.get((acc, key), (0, 0))
        mine[(acc, key)] = (n + 1, g + ok)

    def rate(acc, key):
        n, g = tot.get(key, (0, 0))
        mn, mg = mine.get((acc, key), (0, 0))
        return (g - mg + 1) / (n - mn + 2)
    return rate


CAP_MIN, CAP_MAX, CAP_MIN_BLOCKS = 60, 300, 5


def load(store, answers, paths, now):
    """Daily cap factor from the last 7 days of frozen plans: share of finished blocks marked done.
    Below 60 %: caps -20 %; above 90 %: +10 %; fewer than 5 measurable blocks: defaults.
    store: date iso -> blocks (beta_plans.json); paths: ECUE key -> path ids. Returns dict(facteur, raison)."""
    states = []
    for k, blocks in store.items():
        if 0 < (now.date() - datetime.fromisoformat(k).date()).days <= 7:
            for b in blocks:
                b = dict(b, debut=datetime.fromisoformat(b['debut']), fin=datetime.fromisoformat(b['fin']))
                st = block_state(b, answers, paths.get(b.get('key')), now)
                if st:
                    states.append(st == 'fait')
    if len(states) < CAP_MIN_BLOCKS:
        return dict(facteur=1.0, raison=f'plafond par défaut : {len(states)} bloc(s) mesuré(s) sur 7 jours, il en faut {CAP_MIN_BLOCKS}')
    pct = round(100 * sum(states) / len(states))
    f = 0.8 if pct < 60 else 1.1 if pct > 90 else 1.0
    what = 'baissé de 20 %' if f < 1 else 'monté de 10 %' if f > 1 else 'inchangé'
    return dict(facteur=f, raison=f'tu as fait {pct} % des {len(states)} blocs des 7 derniers jours : plafond {what}')


def caps(facteur):
    """(course day, free day) caps in minutes after the load factor, between 1 h and 5 h."""
    return tuple(min(CAP_MAX, max(CAP_MIN, round(c * facteur))) for c in (CAP_COURSE_DAY, CAP_FREE_DAY))


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


LONG_PAUSE = 20   # minutes, every 3rd break of the day


def pause_settings(hour, personal, average):
    """Work/break minutes for a forced break: the person's measured block, else the users' median, then the hour.

    personal/average: block_length() dicts (personal counts only when measured). Evening: shorter work
    (x0.75 from 20 h), longer break (+5 min from 21 h)."""
    base = personal if personal and not personal['raison'].startswith('par défaut') else average
    travail, pause = base['minutes'], base['pause']
    source = 'ton rythme mesuré' if base is personal else 'la moyenne des élèves'
    if hour >= 20:
        travail = max(20, round(travail * .75))
        source += ', raccourci le soir'
    if hour >= 21:
        pause += 5
    return dict(travail=travail, pause=pause, source=source)


def pause_state(times, now, travail, pause):
    """Forced-break state from today's answer times (sorted, aware). Stateless: a break is done once no
    answer was given for `pause` minutes. Every 3rd break of the day lasts LONG_PAUSE minutes."""
    if not times:
        return dict(force=False, travaille=0, avant_pause=travail)
    chains, start = 0, times[0]
    for a, b in zip(times, times[1:]):
        if b - a >= timedelta(minutes=pause):
            chains += (a - start) >= timedelta(minutes=travail)
            start = b
    worked = (times[-1] - start).total_seconds() / 60
    if worked >= travail:
        length = LONG_PAUSE if chains % 3 == 2 else pause
        end = times[-1] + timedelta(minutes=length)
        if now < end:
            return dict(force=True, travaille=round(worked), jusqua=end.isoformat(),
                        restant=int((end - now).total_seconds()), longue=length == LONG_PAUSE)
    if now - times[-1] >= timedelta(minutes=pause):   # break taken: a new work stretch starts
        return dict(force=False, travaille=0, avant_pause=travail)
    return dict(force=False, travaille=round(worked), avant_pause=max(0, round(travail - worked)))


def average_block(logs_by_account):
    """Median block of the accounts whose block is measured (45 min default when nobody is)."""
    measured = sorted(b['minutes'] for b in map(block_length, logs_by_account) if not b['raison'].startswith('par défaut'))
    m = measured[len(measured) // 2] if measured else 45
    return dict(minutes=m, pause=5 if m <= 25 else 10, raison='moyenne')


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


def plan_day(day, events, adv, hours=None, block=None, now=None, facteur=1.0):
    """Suggested blocks for one day: [{debut, fin, quoi, pourquoi, lien}], breaks included between blocks.

    1. each course of the day gets a 20-min « à chaud » review in the first free slot after it;
    2. the remaining time (up to the daily cap) is cut in blocks; the best hours (personal rhythm, else
       DEFAULT_GOOD_HOURS) go to the most urgent ECUE, a late prerequisite coming first unless the ECUE's
       eval is IMMINENT;
    3. an ECUE gets at most 2 blocks a day (alternating subjects helps memory)."""
    block = block or dict(minutes=45, pause=10)
    lessons = [ev for ev in events if ev['debut'].date() == day and ev['type'] in LESSON_TYPES]
    cap = caps(facteur)[0 if lessons else 1]
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
                             lien=seance_link(key) if key and by_key[key]['parcours'] else None))

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
    score = (lambda h: hours[h]['score'] if h in hours else 0) if hours else (lambda h: DEFAULT_GOOD_HOURS.get(h, 0))
    for t, (r, why) in zip(sorted(blocks, key=lambda t: -score(t.hour)), ordered):
        plan.append(dict(debut=t, fin=t + timedelta(minutes=m), quoi=r['titre'], pourquoi=why, key=r['key'],
                         lien=seance_link(r['key']) if r['parcours'] else None))
    plan.sort(key=lambda p: p['debut'])
    return plan


DONE_MIN, DONE_MARGIN = 5, 30   # done = 5+ answers of the block's ECUE within ±30 min: nothing to tick


def day_plan(day, events, adv, now, store, hours=None, block=None, facteur=1.0):
    """Revision blocks of `day`. Today's plan is frozen in `store` (date iso -> blocks) the first time it is
    computed, so its blocks can later be marked done or missed; later days are recomputed on every call and
    past days only come from the store. The caller saves `store` when it gained a key."""
    k = day.isoformat()
    if k in store:
        return [dict(p, debut=datetime.fromisoformat(p['debut']), fin=datetime.fromisoformat(p['fin'])) for p in store[k]]
    if day < now.date():
        return []
    plan = plan_day(day, events, adv, hours, block, now if day == now.date() else None, facteur)
    if day == now.date():
        store[k] = [dict(p, debut=p['debut'].isoformat(), fin=p['fin'].isoformat()) for p in plan]
    return plan


def block_state(b, answers, paths, now):
    """'fait' / 'manque' once the block is over, None before or when its ECUE has no path to measure.
    answers: [(at, path id)] of the account."""
    if b['fin'] > now or not paths:
        return None
    lo, hi = b['debut'] - timedelta(minutes=DONE_MARGIN), b['fin'] + timedelta(minutes=DONE_MARGIN)
    return 'fait' if sum(1 for at, s in answers if s in paths and lo <= at <= hi) >= DONE_MIN else 'manque'


def _protected(h):
    """Why hour h is never planned (its middle falls in a meal, at night or on Saturday evening), else None."""
    mid = time(h, 30)
    if h < DAY_START.hour or h >= DAY_STOP.hour:
        return f'après {DAY_STOP.hour} h' if h >= DAY_STOP.hour else f'avant {DAY_START.hour} h'
    return next((name.lower() for a, b, name in MEALS if a <= mid < b), None)


def conflicts(hours):
    """One sentence when some of my 3 best measured hours fall in a protected range, else None."""
    if not hours:
        return None
    best = sorted(hours, key=lambda h: -hours[h]['score'])[:3]
    bad = [(h, _protected(h)) for h in sorted(best) if _protected(h)]
    if not bad:
        return None
    return ('Tu réussis très bien à ' + ', '.join(f"{h} h ({hours[h]['pct']} %, {why})" for h, why in bad)
            + " : le calendrier n'y place rien, pour garder repas et sommeil.")


def _ics_text(s):
    return s.replace('\\', '\\\\').replace(';', '\\;').replace(',', '\\,').replace('\n', '\\n')


def _fold(line):
    """RFC 5545: lines of at most 75 octets, continued with a leading space."""
    out, cur = [], ''
    for ch in line:
        if len((cur + ch).encode()) > 74:
            out.append(cur)
            cur = ' '
        cur += ch
    return '\r\n'.join(out + [cur])


def ics(blocks, base, stamp):
    """iCalendar feed of revision blocks; each event links to its path and rings 5 min before."""
    utc = lambda t: t.astimezone(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    lines = ['BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:-//epitadoomscrolling//beta//FR', 'CALSCALE:GREGORIAN',
             'X-WR-CALNAME:Révisions', 'X-PUBLISHED-TTL:PT1H']
    for b in blocks:
        url = base + b['lien'] if b.get('lien') else base
        uid = re.sub(r'[^A-Za-z0-9]+', '-', f"{b['debut']:%Y%m%dT%H%M}-{b.get('key') or 'revision'}")
        lines += ['BEGIN:VEVENT', f'UID:{uid}@epitadoomscrolling', f'DTSTAMP:{utc(stamp)}',
                  f"DTSTART:{utc(b['debut'])}", f"DTEND:{utc(b['fin'])}", f"SUMMARY:{_ics_text(b['quoi'])}",
                  f"DESCRIPTION:{_ics_text(b['pourquoi'] + chr(10) + url)}", f'URL:{url}',
                  'BEGIN:VALARM', 'ACTION:DISPLAY', 'TRIGGER:-PT5M', f"DESCRIPTION:{_ics_text(b['quoi'])}",
                  'END:VALARM', 'END:VEVENT']
    lines.append('END:VCALENDAR')
    return '\r\n'.join(_fold(x) for x in lines) + '\r\n'


def seance_link(key):
    return '/beta/seance/' + quote(key)


RECENT_MISS_DAYS, RECENT_MINUTES = 3, 20


def recent_misses(attempts, paths, now, skip=()):
    """Exercises of `paths` whose last try failed in the last 3 days, oldest first."""
    last = {}
    for k, ok, at in attempts:
        last[k] = (ok, at)
    return [k for k, (ok, at) in sorted(last.items(), key=lambda x: x[1][1])
            if k[0] in paths and not ok and k not in skip and now - at <= timedelta(days=RECENT_MISS_DAYS)]


def seance_next(attempts, due, paths, finished, now):
    """Next step of a revision session on one ECUE (PLAN_BETA étape 1), from the exercise log only:
    1. an exercise due for spaced review (levels.review_queue order), 2. an exercise whose last try failed
    in the last 3 days (oldest first), 3. the current level of the first unfinished path.
    Exercises tried in the last 20 min are skipped, so a session never loops on the same one.
    attempts: [((path, level, exo_id), ok, at)] oldest first; due: [(path, level, exo_id)];
    paths: the ECUE's path ids in syllabus order; finished: path ids whose last level is done.
    Returns ('revoir', key) | ('rate', key) | ('niveau', path) | None (nothing left)."""
    recent = {k for k, _, at in attempts if now - at < timedelta(minutes=RECENT_MINUTES)}
    for k in due:
        if k[0] in paths and k not in recent:
            return 'revoir', k
    miss = recent_misses(attempts, paths, now, recent)
    if miss:
        return 'rate', miss[0]
    return next((('niveau', p) for p in paths if p not in finished), None)


FATIGUE_KO, FATIGUE_SLOW, SITTING = 3, 1.5, 60   # 3 misses in a row, or 1.5x my usual time, within the last hour


def fatigue(answers, now):
    """Why to stop now, else None. answers: [(at, ok, secs)] of the account, oldest first."""
    sitting = [a for a in answers if now - a[0] <= timedelta(minutes=SITTING)]
    if len(sitting) >= FATIGUE_KO and not any(ok for _, ok, _ in sitting[-FATIGUE_KO:]):
        return f'{FATIGUE_KO} ratés d\'affilée'
    usual = [s for _, _, s in answers[:-1] if s]
    if sitting and len(usual) >= 10 and sitting[-1][2] and sitting[-1][2] > FATIGUE_SLOW * sum(usual) / len(usual):
        return 'tu mets bien plus de temps que d\'habitude'
    return None


def seance_line(titre, n_due, n_miss, level, tired=None, ended=None):
    """The one sentence shown on top of a session exercise (PLAN_BETA étape 3), most urgent first.
    ended: dict(pause, reprise, quoi, conseil) when the planned block is over."""
    if tired:
        return f'Ta réussite baisse ({tired}) : pause maintenant, la suite est gardée.'
    if ended:
        nxt = f" Reprise à {ended['reprise']:%H:%M} avec {short(ended['quoi'])}." if ended.get('reprise') else ''
        return f"Bloc fini : {ended['pause']} min de pause. {ended['conseil']}{nxt}"
    parts = []
    if n_due:
        parts.append(f"{n_due} exo{'s' if n_due > 1 else ''} à revoir")
    if n_miss:
        parts.append(f"{n_miss} raté{'s' if n_miss > 1 else ''} récent{'s' if n_miss > 1 else ''}")
    first = ', '.join(parts) + ' d\'abord, puis ' if parts else ''
    return f'{short(titre)} : {first}le niveau {level}.'


def copie_tip(matiere, exo_id):
    """One « copie 20/20 » rule for this subject, the same for a given exercise (shown after a miss)."""
    rules = COPIE_20.get(matiere, []) + COPIE_20['commun']
    return rules[sum(map(ord, exo_id)) % len(rules)]


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
