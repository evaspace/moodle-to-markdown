#!/usr/bin/env python3
"""Tests of the adaptive scroll (scroll.py). Run: python -m unittest tests.test_scroll -v"""
import os
import random
import sys
import tempfile
import unittest
from unittest import mock
from pathlib import Path

TMP = tempfile.mkdtemp()
os.environ.update(DB_PATH=os.path.join(TMP, 'test.db'), COOKIE_INSECURE='1', SECRET_KEY='test')
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scroll import COURSE_EVERY, Item, next_card, unlocked  # noqa: E402

ORDER = ['a', 'b', 'c']
QUIZ = [{'notion': 'a'}, {'notion': 'a'}, {'notion': 'b'}, {'notion': 'c'}]


class Rules(unittest.TestCase):
    def setUp(self):
        self.rng = random.Random(1)

    def test_first_card_is_a_course_card_on_first_notion(self):
        self.assertEqual(next_card([], ORDER, QUIZ, 0, self.rng), ('c', 'a'))

    def test_course_card_is_tested_next(self):
        kind, key = next_card([Item('c', 'a', 'a', None)], ORDER, QUIZ, 0, self.rng)
        self.assertEqual((kind, QUIZ[int(key)]['notion']), ('q', 'a'))

    def test_wrong_answer_brings_course_card(self):
        h = [Item('c', 'a', 'a', None), Item('q', '0', 'a', 0)]
        self.assertEqual(next_card(h, ORDER, QUIZ, 0, self.rng), ('c', 'a'))

    def test_missed_question_comes_back(self):
        h = [Item('q', '2', 'b', 0), Item('c', 'b', 'b', None)] + [Item('q', '0', 'a', 1), Item('c', 'a', 'a', None)] * 2
        self.assertEqual(next_card(h + [Item('q', '1', 'a', 1)], ORDER, QUIZ, 4, self.rng), ('q', '2'))

    def test_ratio_one_course_card_out_of_four(self):
        h, pts = [], 0
        for _ in range(60):
            kind, key = next_card(h, ORDER, QUIZ, pts, self.rng)
            ok = 1 if kind == 'q' else None
            h.append(Item(kind, key, key if kind == 'c' else QUIZ[int(key)]['notion'], ok))
            pts += kind == 'q'
        for i in range(len(h) - COURSE_EVERY + 1):
            self.assertTrue(any(x.kind == 'c' for x in h[i:i + COURSE_EVERY]), i)
        courses = sum(x.kind == 'c' for x in h)
        self.assertLessEqual(courses, len(h) // 2)

    def test_level_unlocks_notions(self):
        self.assertEqual([unlocked(p, 3) for p in (0, 1, 2, 4, 99, -3)], [1, 1, 2, 3, 3, 1])


class Api(unittest.TestCase):
    def test_scroll_flow(self):
        import app as app_module
        c = app_module.app.test_client()
        self.assertEqual(c.get('/scroll/maths-s1-dp').status_code, 302)
        c.post('/api/register', json={'username': 'scroller', 'password': 'secret1'})
        self.assertEqual(c.get('/scroll/maths-s1-dp').status_code, 200)
        card = c.get('/api/scroll/maths-s1-dp/next').get_json()['card']
        self.assertEqual(card['kind'], 'c')
        card = c.get('/api/scroll/maths-s1-dp/next').get_json()['card']
        self.assertEqual(card['kind'], 'q')
        d = c.post('/api/scroll/maths-s1-dp/answer', json={'key': card['key'], 'choice': len(card['choix']) - 1}).get_json()
        if d['ok']:  # last position was right: the wrong-answer path below needs a miss
            self.assertEqual(d['bonne'], len(card['choix']) - 1)
            card = c.get('/api/scroll/maths-s1-dp/next').get_json()['card']
            while card['kind'] != 'q':
                card = c.get('/api/scroll/maths-s1-dp/next').get_json()['card']
            d = c.post('/api/scroll/maths-s1-dp/answer', json={'key': card['key'], 'choice': 0}).get_json()
            if d['ok']:
                self.skipTest('two lucky answers in a row')
        self.assertFalse(d['ok'])
        self.assertEqual(c.get('/api/scroll/maths-s1-dp/next').get_json()['card']['kind'], 'c')
        self.assertEqual(c.post('/api/scroll/maths-s1-dp/answer', json={'key': 'x'}).status_code, 400)


    def test_qcm_choices_shuffled_and_mapped_back(self):
        import app as app_module
        import scroll
        from levels import get_parcours
        c = app_module.app.test_client()
        c.post('/api/register', json={'username': 'shuffler', 'password': 'secret1'})
        quiz = get_parcours('maths-s1-dp')['quiz']
        rev = lambda r, k: list(reversed(r))  # deterministic "shuffle": last authored choice shown first
        with mock.patch.object(scroll.random, 'sample', rev):
            for _ in range(30):
                card = c.get('/api/scroll/maths-s1-dp/next').get_json()['card']
                if card['kind'] == 'q' and card['type'] == 'qcm':
                    break
                if card['kind'] == 'q':  # true/false: answer right so the scroll moves on
                    good = 0 if quiz[int(card['key'])]['bonne'] else 1
                    c.post('/api/scroll/maths-s1-dp/answer', json={'key': card['key'], 'choice': good})
            else:
                self.skipTest('no QCM card reached')
        q = quiz[int(card['key'])]
        shown = len(q['choix']) - 1 - q['bonne']
        d = c.post('/api/scroll/maths-s1-dp/answer', json={'key': card['key'], 'choice': shown}).get_json()
        self.assertTrue(d['ok'])
        self.assertEqual(d['bonne'], shown)
        # a screen position outside the shown choices is refused
        self.assertEqual(c.post('/api/scroll/maths-s1-dp/answer', json={'key': card['key'], 'choice': 99}).status_code, 400)


if __name__ == '__main__':
    unittest.main()
