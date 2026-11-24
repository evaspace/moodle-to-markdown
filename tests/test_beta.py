import sys
import unittest
from datetime import date, datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import beta  # noqa: E402

REG = {
    'maths/S1/APIS': dict(matiere='maths', semestre='S1', titre='Analyse : primitives, intégrales, suites', parcours=['m']),
    'maths/S1/OBM': dict(matiere='maths', semestre='S1', titre='Outils de base mathématiques', parcours=['o']),
    'physique/S1/Mécanique': dict(matiere='physique', semestre='S1', titre='Mécanique du point', parcours=['p']),
}
DAY = date(2026, 11, 24)  # a Tuesday


def ev(titre, typ, day, h, dur=2):
    a = datetime(day.year, day.month, day.day, h, tzinfo=beta.TZ)
    return dict(titre=titre, type=typ, debut=a, fin=a + timedelta(hours=dur))


EVENTS = [ev('Analyse : primitives, intégrales et suites', 'TD', DAY - timedelta(days=7), 9),
          ev('Analyse : primitives, intégrales et suites', 'TD', DAY + timedelta(days=7), 9),
          ev('Mécanique du point - Dynamique', 'TD', DAY - timedelta(days=2), 9),
          ev('Mécanique du point - Dynamique', 'TD', DAY, 9),
          ev('Analyse : primitives, intégrales et suites', 'EVAL', DAY + timedelta(days=5), 9),
          ev('CROUS', 'EVN', DAY, 14)]
NOW = datetime(2026, 11, 24, 7, tzinfo=beta.TZ)


class Beta(unittest.TestCase):
    def test_mapping(self):
        self.assertEqual(beta.ecue_of('Outils de base mathématiques', REG), 'maths/S1/OBM')
        self.assertEqual(beta.ecue_of('Mécanique du point - Dynamique en référentiel', REG), 'physique/S1/Mécanique')
        self.assertIsNone(beta.ecue_of('CROUS', REG))

    def test_advancement_lateness_and_prerequisite(self):
        adv = {r['key']: r for r in beta.advancement(EVENTS, REG, {'m': 0, 'p': 50}, NOW)}
        m, p = adv['maths/S1/APIS'], adv['physique/S1/Mécanique']
        self.assertEqual((m['faits'], m['total'], m['classe'], m['retard'], m['jours_eval']), (1, 2, 50, 50, 5))
        self.assertEqual((p['classe'], p['retard']), (50, 0))
        self.assertEqual(p['bloque_par'], ['Analyse : primitives, intégrales, suites'])

    def test_plan_respects_courses_meals_cap_and_puts_prerequisite_first(self):
        adv = beta.advancement(EVENTS, REG, {'m': 0, 'p': 0}, NOW)
        plan = beta.plan_day(DAY, EVENTS, adv)
        busy = [(e['debut'], e['fin']) for e in EVENTS if e['debut'].date() == DAY]
        busy += [(datetime.combine(DAY, a, beta.TZ), datetime.combine(DAY, b, beta.TZ)) for a, b, _ in beta.MEALS]
        for p in plan:
            self.assertTrue(all(p['fin'] <= a or p['debut'] >= b for a, b in busy), p)
            self.assertLessEqual(p['fin'].time(), beta.DAY_STOP)
        self.assertLessEqual(sum((p['fin'] - p['debut']).seconds // 60 for p in plan), beta.CAP_COURSE_DAY)
        hot = [p for p in plan if p['quoi'].startswith('À chaud')]
        self.assertEqual([p['debut'].hour for p in hot], [11])            # right after the 9-11 course
        keys = [p['key'] for p in sorted([p for p in plan if p['key']], key=lambda p: -beta.DEFAULT_GOOD_HOURS.get(p['debut'].hour, 0))]
        self.assertEqual(keys[0], 'maths/S1/APIS')                        # best hour: the late maths
        self.assertLessEqual(keys.count('maths/S1/APIS'), 2)

    def test_past_eval_lowers_priority(self):
        evs = [ev('Outils de base mathématiques', 'TD', DAY - timedelta(days=30), 9),
               ev('Outils de base mathématiques', 'EVAL', DAY - timedelta(days=20), 9)]
        r = beta.advancement(evs, REG, {}, NOW)[0]
        self.assertEqual((r['retard'], r['priorite']), (100, 25))

    def test_syllabus_evals(self):
        syl = {'calendrier': [{'debut': '2026-11-25', 'titre': 'QCM2', 'ecue': 'physique/S1/Mécanique'},
                              {'debut': '2026-11-26', 'titre': 'Test', 'parcours': ['m']},
                              {'debut': '2026-11-26', 'titre': 'S3', 'ecue': 'maths/S3/AL'},
                              {'debut': '2026-11-29', 'titre': 'déjà dans Auriga', 'parcours': ['m']}]}
        out = beta.syllabus_evals(syl, REG, EVENTS)
        self.assertEqual([(e['titre'], e['debut'].day) for e in out],
                         [('Mécanique du point', 25), ('Analyse : primitives, intégrales, suites', 26)])
        p = {r['key']: r for r in beta.advancement(EVENTS + out, REG, {}, NOW)}['physique/S1/Mécanique']
        self.assertEqual(p['jours_eval'], 1)
        adv = beta.advancement(EVENTS + out, REG, {}, NOW)
        first = max(beta.plan_day(DAY, EVENTS, adv), key=lambda b: beta.DEFAULT_GOOD_HOURS.get(b['debut'].hour, 0)
                    if b['key'] else -1)
        self.assertEqual(first['key'], 'physique/S1/Mécanique')   # eval tomorrow: no detour by the maths

    def test_no_revision_on_the_eval_day(self):
        adv = beta.advancement(EVENTS, REG, {}, NOW)
        evday = DAY + timedelta(days=5)
        self.assertNotIn('maths/S1/APIS', [p['key'] for p in beta.plan_day(evday, EVENTS, adv)])

    def test_week_grid(self):
        adv = beta.advancement(EVENTS, REG, {'m': 10}, NOW)
        w = beta.week_grid(EVENTS, adv, DAY - timedelta(days=1), NOW)
        self.assertEqual((w['lundi'], w['aujourdhui']), ('2026-11-23', 1))
        td = [i for i in w['items'] if i['kind'] == 'cours' and i['jour'] == 1][0]
        self.assertEqual((td['debut'], td['fin'], td['lien'], td['classe']), (540, 660, '/niveaux/p', 50))
        self.assertFalse([i for i in w['items'] if i['kind'] == 'revision' and i['jour'] == 0])  # past day

    def test_short(self):
        self.assertEqual(beta.short('Mécanique du point - Dynamique en référentiel'), 'Mécanique du point')
        self.assertEqual(beta.short('C - Les bases'), 'C - Les bases')
        self.assertEqual(beta.short('À chaud : Analyse : primitives'), 'À chaud : Analyse')

    def test_pause_state(self):
        t0 = datetime(2026, 11, 24, 14, tzinfo=beta.TZ)
        work = [t0 + timedelta(minutes=5 * k) for k in range(10)]           # 14:00 -> 14:45
        st = beta.pause_state(work, t0 + timedelta(minutes=46), 45, 10)
        self.assertTrue(st['force'])
        self.assertEqual(st['restant'], 9 * 60)                            # until 14:55
        self.assertFalse(beta.pause_state(work, t0 + timedelta(minutes=56), 45, 10)['force'])   # break done
        self.assertEqual(beta.pause_state(work[:4], t0 + timedelta(minutes=16), 45, 10)['avant_pause'], 30)
        # third break of the day is a long one
        day = []
        for c in range(3):
            day += [t0 + timedelta(minutes=60 * c + 5 * k) for k in range(10)]
        self.assertTrue(beta.pause_state(day, day[-1] + timedelta(minutes=12), 45, 10)['longue'])

    def test_pause_settings(self):
        avg = dict(minutes=25, pause=5, raison='moyenne')
        mine = dict(minutes=45, pause=10, raison='ta réussite tient')
        self.assertEqual(beta.pause_settings(10, mine, avg)['travail'], 45)
        self.assertEqual(beta.pause_settings(10, dict(mine, raison='par défaut : x'), avg)['travail'], 25)
        ev = beta.pause_settings(21, mine, avg)
        self.assertEqual((ev['travail'], ev['pause']), (34, 15))

    def test_rhythm_and_block_length(self):
        self.assertIsNone(beta.rhythm([(NOW, 1)] * 10))
        start = datetime(2026, 11, 1, 9, tzinfo=beta.TZ)
        logs = []
        for d in range(3):  # 3 sessions of 60 min: 100 % for 25 min then 50 %
            for k in range(12):
                logs.append((start + timedelta(days=d, minutes=5 * k), 1 if k < 5 else k % 2))
        self.assertEqual(beta.block_length(logs)['minutes'], 25)
        self.assertEqual(beta.block_length(logs[:5])['minutes'], 45)
        self.assertEqual(beta.rhythm(logs, min_total=10)[9]['n'], 36)

    def test_saturday_evening_off(self):
        sat = date(2026, 11, 28)
        self.assertTrue(all(b.hour <= 18 for _, b in beta.free_slots([], sat)))

    def test_day_plan_frozen_and_block_state(self):
        adv = beta.advancement(EVENTS, REG, {'m': 10}, NOW)
        store = {}
        plan = beta.day_plan(DAY, EVENTS, adv, NOW, store)
        self.assertIn(DAY.isoformat(), store)                                # today is frozen
        later = NOW + timedelta(hours=3)
        self.assertEqual([b['debut'] for b in beta.day_plan(DAY, EVENTS, adv, later, store)], [b['debut'] for b in plan])
        beta.day_plan(DAY + timedelta(days=1), EVENTS, adv, NOW, store)
        self.assertEqual(list(store), [DAY.isoformat()])                     # future days are not
        self.assertEqual(beta.day_plan(DAY - timedelta(days=1), EVENTS, adv, NOW, store), [])
        b = dict(debut=datetime(2026, 11, 24, 10, tzinfo=beta.TZ), fin=datetime(2026, 11, 24, 10, 45, tzinfo=beta.TZ))
        after = b['fin'] + timedelta(hours=1)
        five = [(b['debut'] + timedelta(minutes=8 * k), 'm') for k in range(5)]
        self.assertIsNone(beta.block_state(b, five, {'m'}, b['fin'] - timedelta(minutes=1)))   # not over
        self.assertEqual(beta.block_state(b, five, {'m'}, after), 'fait')
        self.assertEqual(beta.block_state(b, five[:4], {'m'}, after), 'manque')
        self.assertEqual(beta.block_state(b, five, {'p'}, after), 'manque')                    # other ECUE
        self.assertIsNone(beta.block_state(b, five, None, after))                              # nothing to measure

    def test_now_block(self):
        t = lambda h, m=0: datetime(2026, 11, 24, h, m, tzinfo=beta.TZ)
        bl = [dict(debut=t(14), fin=t(14, 45)), dict(debut=t(10), fin=t(10, 45))]
        self.assertTrue(beta.now_block(bl, t(10, 20))['en_cours'])
        nxt = beta.now_block(bl, t(11))
        self.assertEqual((nxt['debut'], nxt['en_cours']), (t(14), False))
        self.assertIsNone(beta.now_block(bl, t(15)))

    def test_conflicts(self):
        self.assertIsNone(beta.conflicts(None))
        self.assertIsNone(beta.conflicts({9: dict(n=20, pct=80, score=80), 10: dict(n=20, pct=70, score=70), 14: dict(n=20, pct=60, score=60)}))
        c = beta.conflicts({19: dict(n=20, pct=73, score=73), 23: dict(n=20, pct=75, score=75), 10: dict(n=20, pct=60, score=60), 20: dict(n=20, pct=10, score=10)})
        self.assertIn('19 h (73 %, dîner)', c)
        self.assertIn('23 h (75 %, après 22 h)', c)
        self.assertNotIn('10 h', c)

    def test_ics(self):
        a = datetime(2026, 11, 24, 10, tzinfo=beta.TZ)
        out = beta.ics([dict(debut=a, fin=a + timedelta(minutes=45), quoi='Analyse : primitives, intégrales',
                             pourquoi='évaluation dans 5 j; ' + 'x' * 120, key='maths/S1/APIS', lien='/niveaux/m')],
                       'https://e.x', a)
        self.assertTrue(out.startswith('BEGIN:VCALENDAR\r\n') and out.endswith('END:VCALENDAR\r\n'))
        self.assertIn('DTSTART:20261124T090000Z', out)                       # Paris winter = UTC+1
        self.assertIn('SUMMARY:Analyse : primitives\\, intégrales', out)
        self.assertIn('UID:20261124T1000-maths-S1-APIS@epitadoomscrolling', out)
        self.assertTrue(all(len(x.encode()) <= 75 for x in out.split('\r\n')))
        self.assertIn('https://e.x/niveaux/m', out.replace('\r\n ', ''))
    def test_seance_next(self):
        t = lambda d, h=9: datetime(2026, 11, d, h, tzinfo=beta.TZ)
        now = t(24, 15)
        a, b, c = ('m', 2, 'e1'), ('m', 3, 'e2'), ('p', 1, 'x')
        log = [(a, 0, t(20)), (b, 0, t(23)), (c, 0, t(23))]
        self.assertEqual(beta.seance_next(log, [a], ['m'], set(), now), ('revoir', a))          # due first
        self.assertEqual(beta.seance_next(log, [], ['m'], set(), now), ('rate', b))             # a: too old
        self.assertEqual(beta.seance_next(log + [(b, 1, t(24, 10))], [], ['m'], set(), now), ('niveau', 'm'))
        recent = log + [(b, 0, now - timedelta(minutes=5))]
        self.assertEqual(beta.seance_next(recent, [b], ['m'], set(), now), ('niveau', 'm'))     # just tried: skip
        self.assertIsNone(beta.seance_next([], [], ['m'], {'m'}, now))
        self.assertEqual(beta.seance_link('maths/S1/Mécanique'), '/beta/seance/maths/S1/M%C3%A9canique')
    def test_rhythm_difficulty(self):
        t = lambda h: datetime(2026, 11, 20, h, tzinfo=beta.TZ)
        logs = [(t(9), 1)] * 10 + [(t(15), 1)] * 5 + [(t(15), 0)] * 5
        easy, hard = [0.9] * 10, [0.2] * 10        # 9 h: easy exercises, 15 h: hard ones
        h = beta.rhythm(logs, min_total=10, expected=easy + hard)
        self.assertEqual((h[9]['pct'], h[15]['pct']), (100, 50))
        self.assertEqual((h[9]['score'], h[15]['score']), (60, 80))   # 15 h is the better hour
        self.assertEqual(beta.rhythm(logs, min_total=10)[9]['score'], 100)
        rate = beta.expected_rates([(1, 'e', 1), (2, 'e', 0), (2, 'e', 0), (1, 'f', 1)])
        self.assertEqual(rate(1, 'e'), 1 / 4)         # others: 0/2
        self.assertEqual(rate(2, 'e'), 2 / 3)         # others: 1/1
        self.assertEqual(rate(1, 'f'), 0.5)           # nobody else

    def test_load_factor(self):
        now = datetime(2026, 11, 24, 12, tzinfo=beta.TZ)

        def store(done, missed):
            blocks, answers = [], []
            for i in range(done + missed):
                a = datetime(2026, 11, 20, 8, tzinfo=beta.TZ) + timedelta(hours=i)
                blocks.append(dict(debut=a.isoformat(), fin=(a + timedelta(minutes=45)).isoformat(), key='k'))
                if i < done:
                    answers += [(a + timedelta(minutes=5 * j), 'm') for j in range(5)]
            return {'2026-11-20': blocks}, answers
        self.assertEqual(beta.load(*store(1, 2), {'k': {'m'}}, now)['facteur'], 1.0)   # too few blocks
        self.assertEqual(beta.load(*store(2, 4), {'k': {'m'}}, now)['facteur'], 0.8)
        self.assertEqual(beta.load(*store(10, 0), {'k': {'m'}}, now)['facteur'], 1.1)
        self.assertEqual(beta.load(*store(7, 3), {'k': {'m'}}, now)['facteur'], 1.0)
        self.assertEqual(beta.caps(0.8), (144, 240))
        self.assertEqual(beta.caps(1.1), (198, 300))  # 5 h at most
        self.assertEqual(beta.caps(0.1), (60, 60))    # 1 h at least

if __name__ == '__main__':
    unittest.main()
