import json
import unittest
from pathlib import Path

import squelettes

PARCOURS = Path(__file__).resolve().parent.parent / 'parcours'


class TestSquelettes(unittest.TestCase):
    def test_every_skeleton_cites_an_official_copy(self):
        baremes = json.loads((PARCOURS / 'baremes.json').read_text(encoding='utf-8'))['niveaux']
        for key, s in squelettes.SQUELETTES.items():
            self.assertTrue(s['source'], key)
            for src in s['source']:
                self.assertIn(src, baremes, f'{key}: {src} has no official copy')

    def test_levels_exist_and_every_skeleton_is_used(self):
        levels = {}
        for p in PARCOURS.glob('*.json'):
            d = json.loads(p.read_text(encoding='utf-8'))
            if 'levels' in d:
                levels[d['subject']['id']] = {lv['n'] for lv in d['levels']}
        for k, v in squelettes.NIVEAUX.items():
            subject, n = k.rsplit('/', 1)
            self.assertIn(int(n), levels.get(subject, ()), k)
            self.assertIn(v, squelettes.SQUELETTES, k)
        self.assertEqual(set(squelettes.NIVEAUX.values()), set(squelettes.SQUELETTES))

    def test_stages_fade(self):
        self.assertEqual([squelettes.palier(f) for f in (0, 1, 2, 3, 5, 6, 40)], [1, 2, 2, 3, 3, 4, 4])
        s = squelettes.pour('maths-s1-apis-edo', 9, 3)
        self.assertEqual((s['cle'], s['palier']), ('edo2', 3))
        self.assertIsNone(squelettes.pour('maths-s1-apis-edo', 11, 0))  # exam level: mixed types
        self.assertIn(('maths-s1-apis-edo', 7), squelettes.niveaux_du_type('edo2'))

    def test_every_step_has_a_label_and_text(self):
        for key, s in squelettes.SQUELETTES.items():
            for lab, t in s['etapes']:
                self.assertTrue(lab and t, key)
                self.assertEqual(t.count('$') % 2, 0, f'{key}: unbalanced $ in « {t} »')

    def test_every_suites_exercise_has_a_copy(self):
        data = json.loads((PARCOURS / 'apis_suites.json').read_text(encoding='utf-8'))
        for lvl in data['levels']:
            for e in lvl['exos']:
                self.assertTrue(e.get('copie'), e['id'])
                self.assertNotIn('<', e['copie'].replace(' < ', ''), f"{e['id']}: write `a < b` (raw HTML)")
                self.assertEqual(e['copie'].count('$') % 2, 0, e['id'])

    def test_variant_shows_no_copy(self):
        import levels
        exo = {'id': 'x', 'copie': 'base', 'variants': [{'enonce': 'autre'}]}
        self.assertEqual(levels.variant(exo, 0)['copie'], 'base')
        self.assertIsNone(levels.variant(exo, 1)['copie'])  # other numbers: the base copy would be wrong


if __name__ == '__main__':
    unittest.main()
