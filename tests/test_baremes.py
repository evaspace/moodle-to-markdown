"""annales/tools/baremes.py: only official corrections become « Copie 20/20 » examples."""
import os, sys, tempfile, unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'annales', 'tools'))
import baremes  # noqa: E402

OFFICIAL = """# Partiel (corrigé, FR)

- Source : scan. Date réelle : juin 2016. Barème sur 20.

## Exercice 1 (5,5 points)
Type : x · ECUE : y · Niveau : maths-s1-dp/3
Formules : f

1. Calculer.
> 42.

## Exercice 2
Type : x · ECUE : y · Niveau : maths-s1-dp/4

Énoncé.
> Réponse.

## Exercice 3 (2 points)
Type : x · ECUE : y

Sans niveau : ignoré.
"""


class Baremes(unittest.TestCase):
    def write(self, text):
        f = tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8')
        f.write(text)
        f.close()
        self.addCleanup(os.unlink, f.name)
        return f.name

    def test_official(self):
        exs = baremes.parse(self.write(OFFICIAL))
        self.assertEqual([e['niveau'] for e in exs], ['maths-s1-dp/3', 'maths-s1-dp/4'])
        self.assertEqual((exs[0]['points'], exs[0]['sur'], exs[0]['date']), (5.5, 20, 'juin 2016'))
        self.assertIsNone(exs[1]['points'])
        self.assertNotIn('Formules', exs[0]['texte'])
        self.assertIn('> 42.', exs[0]['texte'])

    def test_written_for_site_is_left_out(self):
        self.assertEqual(baremes.parse(self.write(OFFICIAL.replace('scan.', 'corrigé rédigé.'))), [])

    def test_real_annales(self):
        levels = baremes.build()
        self.assertTrue(levels)
        self.assertTrue(all(e['texte'] for v in levels.values() for e in v))


if __name__ == '__main__':
    unittest.main()
