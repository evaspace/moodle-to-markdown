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


if __name__ == '__main__':
    unittest.main()
