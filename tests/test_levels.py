#!/usr/bin/env python3
"""Tests of the Niveaux mode: game rules, accounts, progress API.

Run: python -m unittest tests.test_levels -v   (needs Flask, Markdown, bleach)
"""
import json
import os
import sys
import tempfile
import unittest
from unittest import mock
from pathlib import Path

TMP = tempfile.mkdtemp()
os.environ.update(DB_PATH=os.path.join(TMP, 'test.db'), COOKIE_INSECURE='1', SECRET_KEY='test')
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import levels  # noqa: E402
from levels import COMBO_GAP, apply_result, combo, due_reviews, easier_level, percent, pick_exo, score  # noqa: E402
from datetime import date  # noqa: E402

SUBJECT = 'maths-s1-apis-integrales'


class Rules(unittest.TestCase):
    def test_level_passes_only_when_every_formula_is_green(self):
        self.assertEqual(apply_result(1, 0, True, False, 14), (1, 0, 'progress'))
        self.assertEqual(apply_result(1, 0, True, True, 14), (2, 1, 'up'))

    def test_failure_drops_one_level_only_after_two_misses(self):
        self.assertEqual(apply_result(5, 4, False, False, 14, prev_ko=False), (5, 4, 'warn'))
        self.assertEqual(apply_result(5, 4, False, False, 14), (4, 4, 'down'))
        self.assertEqual(apply_result(1, 0, False, False, 14), (1, 0, 'retry'))

    def test_spaced_review_d1_d3_d7(self):
        d = date(2026, 11, 1)
        day = lambda k: date.fromordinal(d.toordinal() + k)  # noqa: E731
        miss = [('a', 0, d), ('a', 1, d)]  # a success the same day as the miss does not count
        self.assertEqual(due_reviews(miss, d), {})
        self.assertEqual(due_reviews(miss, day(1)), {'a': day(1)})
        once = miss + [('a', 1, day(1))]
        self.assertEqual(due_reviews(once, day(3)), {})
        self.assertEqual(due_reviews(once, day(4)), {'a': day(4)})
        thrice = once + [('a', 1, day(4)), ('a', 1, day(11))]
        self.assertEqual(due_reviews(thrice, day(60)), {})  # learnt: leaves the queue
        self.assertEqual(due_reviews(thrice + [('a', 0, day(12))], day(13)), {'a': day(13)})  # a miss restarts
        self.assertEqual(due_reviews([('b', 1, d)], day(9)), {})  # never missed: never reviewed

    def test_combo_resets_on_miss_and_after_pause(self):
        rows = [(1, 100), (1, 90), (1, 80), (1, 70), (1, 60), (1, 50)]  # newest first
        self.assertEqual(combo(rows), 6)
        self.assertEqual(combo([(0, 110)] + rows), 0)          # a miss resets to zero
        self.assertEqual(combo([(1, 120), (0, 110)] + rows), 1)
        self.assertEqual(combo([(1, 100 + COMBO_GAP + 1)] + rows), 1)  # long pause: new run

    def test_last_level(self):
        self.assertEqual(apply_result(14, 13, True, True, 14), (14, 14, 'finished'))
        self.assertEqual(percent(14, 14), 100)

    def test_score_speed_and_peek(self):
        self.assertEqual(score(False, 10, 100, False, 1), 0)
        self.assertEqual(score(True, 100, 100, False, 1), 100)
        self.assertEqual(score(True, 10, 100, False, 1), 150)    # capped x1.5
        self.assertEqual(score(True, 1000, 100, False, 1), 50)   # floored x0.5
        self.assertEqual(score(True, 100, 100, True, 1), 33)     # a third after the solution formulas
        self.assertEqual(score(True, 100, 100, 2, 1), 50)        # half after the chapter sheet only
        self.assertGreater(score(True, 100, 100, False, 5), score(True, 100, 100, False, 1))

    def test_pick_never_done_then_failed_then_rotation(self):
        exos = [{'id': i} for i in 'abc']
        self.assertEqual(pick_exo(exos, {'a': 1})['id'], 'b')
        self.assertEqual(pick_exo(exos, {'a': 1, 'b': 0, 'c': None}, 'b')['id'], 'c')
        self.assertEqual(pick_exo(exos, {'a': 0, 'b': 1, 'c': 0}, 'a')['id'], 'c')   # red, not the one just failed
        self.assertEqual(pick_exo(exos, {'a': 0, 'b': 1, 'c': 1}, 'a')['id'], 'b')   # only red = just failed: move on
        self.assertNotEqual(pick_exo(exos, {'a': 1, 'b': 1, 'c': 1}, 'a', 5)['id'], 'a')

    def test_easier_level_same_notion_else_previous(self):
        levels_ = [{'notions': ['a']}, {'notions': ['b']}, {'notions': ['c']}, {'notions': ['a', 'd']}]
        self.assertEqual(easier_level(levels_, 4), 1)   # highest lower level sharing a notion
        self.assertEqual(easier_level(levels_, 3), 2)   # no shared notion: the level just below
        self.assertEqual(easier_level(levels_, 1), 1)   # nothing easier: same level (another exercise)

    def test_time_bonus(self):
        import sqlite3
        c = sqlite3.connect(':memory:'); c.executescript(levels.SCHEMA)
        log = lambda ok, to: c.execute("INSERT INTO exo_log (account_id, subject, level, exo_id, ok, timeout) "
                                       "VALUES (1, 's', 1, 'e', ?, ?)", (ok, to))
        bonus = lambda: levels.time_bonus(c, 1, 's', 1, 'e')
        self.assertEqual(bonus(), 1)
        log(0, 1); self.assertEqual(bonus(), 1.5)
        log(0, 0); log(0, 1); self.assertEqual(bonus(), 2)   # plain failures add nothing
        for _ in range(5): log(0, 1)
        self.assertEqual(bonus(), levels.TIMEOUT_MAX)
        log(1, 0); self.assertEqual(bonus(), 1)              # a success resets it

    def test_variant_rotation(self):
        e = {'id': 'x', 'src': 'annale', 'enonce': 'A', 'variants': [{'enonce': 'B'}]}
        self.assertEqual([levels.variant(e, k)['enonce'] for k in range(3)], ['A', 'B', 'A'])
        self.assertIsNone(levels.variant(e, 1)['src'])  # a variant is not the past-exam exercise
        self.assertEqual(levels.variant({'id': 'y', 'enonce': 'C'}, 5)['enonce'], 'C')

    def test_maths_origins_complete(self):
        # every maths exercise and variant has its own origin: rerun tools/sources.py after a content change
        for pid, data in levels.load_parcours().items():
            if not pid.startswith('maths'):
                continue
            for lvl in data['levels']:
                for e in lvl['exos']:
                    for k, x in enumerate([e] + e.get('variants', [])):
                        self.assertIn('origine', x, f'{pid}/{lvl["n"]}/{e["id"]} version {k}')
                        o = levels.variant(e, k)['origine']
                        self.assertIn(o['kind'], ('TD', 'Examen', 'site'))
                        if k and not e.get('src'):
                            self.assertEqual(o['kind'], 'site')  # variant of an uncited exercise


class Selection(unittest.TestCase):
    P = [('a', {'subject': {'semestre': 'S1', 'matiere': 'maths', 'ecue': 'A', 'titre': 'a'}}),
         ('b', {'subject': {'semestre': 'S2', 'matiere': 'maths', 'ecue': 'B', 'titre': 'b'}}),
         ('c', {'subject': {'semestre': 'S1', 'matiere': 'info', 'ecue': 'C', 'titre': 'c'}})]

    def f(self, **kw):
        return dict({'ordre': 'semestre', 'sem': '', 'mat': '', 'ch': ''}, **kw)

    def ids(self, **kw):
        return [sid for sid, _ in levels.select_paths(self.P, self.f(**kw))]

    def test_filters(self):
        self.assertEqual(self.ids(), ['a', 'b', 'c'])
        self.assertEqual(self.ids(sem='S1'), ['a', 'c'])
        self.assertEqual(self.ids(sem='S1', mat='maths'), ['a'])
        self.assertEqual(self.ids(ch='b'), ['b'])
        self.assertEqual(self.ids(sem='S1', ch='b'), ['a', 'c'])  # chapter outside the semester: ignored

    def test_options_follow_order(self):
        self.assertEqual(levels.selector(self.P, self.f(sem='S2'))['mats'], ['maths'])
        self.assertEqual(levels.selector(self.P, self.f(ordre='matiere', mat='info'))['sems'], ['S1'])
        self.assertEqual(levels.selector(self.P, self.f(ordre='matiere', sem='S2'))['mats'], ['info', 'maths'])


_S1_CAL = [  # fixed calendar for the tests: the real one in syllabus.json changes with every sync
    {'debut': '2026-10-26', 'fin': '2026-10-30', 'titre': 'Dénombrement et probabilités', 'type': 'Examen', 'source': 'Auriga', 'ecue': 'maths/S1/DP'},
    {'debut': '2026-12-07', 'titre': 'Test à distance : APIS en entier', 'type': 'Test à distance', 'source': 'Moodle', 'ecue': 'maths/S1/APIS'},
    {'debut': '2026-12-14', 'fin': '2026-12-18', 'titre': 'Analyse : primitives, intégrales et suites', 'type': 'Examen', 'source': 'Auriga', 'ecue': 'maths/S1/APIS'},
]


class Api(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import app as app_module
        cls.app = app_module.app
        cls.data = levels.load_parcours()[SUBJECT]

    def setUp(self):
        self.c = self.app.test_client()

    def register(self, name):
        return self.c.post('/api/register', json={'username': name, 'password': 'secret1'})

    def answer(self, level, ok):
        page = self.c.get(f'/niveaux/{SUBJECT}')
        self.assertEqual(page.status_code, 200)
        exo_id = page.get_data(as_text=True).split('data-exo="')[1].split('"')[0]
        return self.c.post(f'/api/niveaux/{SUBJECT}/result', json={'level': level, 'exo_id': exo_id, 'ok': ok}).get_json()

    def test_pages_need_login(self):
        self.assertEqual(self.c.get('/niveaux').status_code, 302)
        self.assertEqual(self.c.post(f'/api/niveaux/{SUBJECT}/result', json={}).status_code, 401)

    def test_register_login_and_validation(self):
        self.assertEqual(self.c.post('/api/register', json={'username': 'a', 'password': 'secret1'}).status_code, 400)
        self.assertEqual(self.c.post('/api/register', json={'username': 'bob', 'password': '123'}).status_code, 400)
        self.assertEqual(self.register('bob').status_code, 200)
        self.assertEqual(self.register('BOB').status_code, 409)  # case-insensitive
        self.c.post('/api/logout')
        self.assertEqual(self.c.post('/api/login', json={'username': 'bob', 'password': 'nope00'}).status_code, 401)
        self.assertEqual(self.c.post('/api/login', json={'username': 'bob', 'password': 'secret1'}).status_code, 200)
        self.assertEqual(self.c.get('/niveaux').status_code, 200)

    def test_nav_state_and_footer_everywhere(self):
        self.assertFalse(self.c.get('/api/me').get_json()['logged'])
        self.register('navuser')
        me = self.c.get('/api/me').get_json()
        self.assertEqual((me['username'], me['levels_done'], me['xp']), ('navuser', 0, 0))
        self.assertGreater(me['levels_total'], 0)
        for path in ('/niveaux', '/stats', '/formules', '/compte', f'/niveaux/{SUBJECT}', '/inconnu'):
            html = self.c.get(path).get_data(as_text=True)
            self.assertIn('morgan-footer', html, path)  # footer on every page, exercise page included (user 2026-11-17)
            self.assertIn('app-nav', html, path)
        self.answer(1, True)
        self.assertEqual(self.c.get('/api/me').get_json()['streak'], 1)
        self.assertEqual(self.c.post(f'/api/niveaux/{SUBJECT}/copie', json={'level': 1, 'exo_id': 'x'}).status_code, 200)
        self.c.get(f'/niveaux/{SUBJECT}?facile=x')  # « Trop dur, passer »
        html = self.c.get('/stats').get_data(as_text=True)
        self.assertIn('st-wk-detail', html)
        self.assertIn('st-fold', html)
        with levels.db() as conn:
            kinds = {k for (k,) in conn.execute('SELECT kind FROM event_log e JOIN account a ON a.id=e.account_id '
                                                "WHERE a.username='navuser'")}
        self.assertTrue({'copie_ia', 'passer'} <= kinds, kinds)

    def test_admin_only_for_owner_account(self):
        os.environ['ADMIN_PASSWORD'] = 'x'
        import app as app_module
        app_module.ADMIN_PASSWORD = 'secret-admin'
        self.register('plainuser')
        self.assertEqual(self.c.get('/admin/stats').status_code, 401)
        self.assertNotIn('>Admin</a>', self.c.get('/niveaux').get_data(as_text=True))
        self.c.post('/api/logout')
        self.register('morgan.pierrefeu')
        self.assertIn('>Admin</a>', self.c.get('/niveaux').get_data(as_text=True))
        self.assertEqual(self.c.get('/admin/stats').status_code, 200)
        html = self.c.get('/admin/stats').get_data(as_text=True)
        self.assertIn('app-nav', html)
        self.assertIn('Comportements', html)
        self.c.post('/admin', data={'raw_text': 'Q: Carte de test admin\nR: Verso'})
        html = self.c.get('/admin').get_data(as_text=True)
        self.assertIn('app-nav', html)
        self.assertIn('Carte de test admin', html)  # live list of the last cards
        self.assertIn('morgan-footer', html)

    def test_skip_too_hard_serves_easier_without_penalty(self):
        self.register('skipper')
        page = self.c.get(f'/niveaux/{SUBJECT}').get_data(as_text=True)
        first = page.split('data-exo="')[1].split('"')[0]
        self.assertIn('Trop dur, passer', page)
        page = self.c.get(f'/niveaux/{SUBJECT}?facile={first}').get_data(as_text=True)
        self.assertNotIn(f'data-exo="{first}"', page.split('lv-squares')[0])  # level 1: another exercise
        self.assertIn('Plus facile, même notion', page)
        self.assertNotIn('Trop dur, passer', page)
        with levels.db() as conn:
            uid = conn.execute("SELECT id FROM account WHERE username='skipper'").fetchone()[0]
            self.assertEqual(conn.execute('SELECT COUNT(*) FROM exo_log WHERE account_id=?', (uid,)).fetchone()[0], 0)

    def test_grind_review_stays_in_the_same_subject(self):
        self.register('reviewer')
        with levels.db() as conn:
            uid = conn.execute("SELECT id FROM account WHERE username='reviewer'").fetchone()[0]
            miss = lambda s, e: conn.execute("INSERT INTO exo_log (account_id, subject, level, exo_id, ok, practice, at) "
                                             "VALUES (?, ?, 1, ?, 0, 1, datetime('now', '-1 day'))", (uid, s, e))
            miss('physique-s2-thermo', 'he1')   # another subject: never served in the maths grind
        with self.c.session_transaction() as sess:
            sess['grind_n'] = levels.REVIEW_EVERY
        self.assertEqual(self.c.get(f'/niveaux/{SUBJECT}').status_code, 200)
        with levels.db() as conn:
            miss('maths-s1-apis-suites', 'ag1')  # another chapter of the same subject: fine
        with self.c.session_transaction() as sess:
            sess['grind_n'] = levels.REVIEW_EVERY
        self.assertIn('/niveaux/maths-s1-apis-suites?', self.c.get(f'/niveaux/{SUBJECT}').headers['Location'])

    def test_progress_up_down_and_isolation(self):
        self.register('alice')
        n1 = len(self.data['levels'][0]['exos'])
        for i in range(n1):
            d = self.answer(1, True)
            if i < n1 - 1:
                self.assertEqual((d['event'], d['green']), ('progress', i + 1))
        self.assertEqual((d['event'], d['level']), ('up', 2))
        self.assertGreater(d['percent'], 0)
        d = self.answer(2, False)  # first miss: warning only
        self.assertEqual((d['event'], d['level']), ('warn', 2))
        d = self.answer(2, False)  # second miss in a row: one level down
        self.assertEqual((d['event'], d['level'], d['best']), ('down', 1, 1))
        # the missed exercise is due tomorrow, not today
        self.assertNotIn('à revoir', self.c.get('/niveaux').get_data(as_text=True))
        self.assertIn('revu=1', self.c.get('/niveaux/revoir').headers['Location'])
        # a review miss never demotes, even on the current level
        for _ in range(2):
            d = self.c.post(f'/api/niveaux/{SUBJECT}/result', json={'level': 1, 'exo_id': self.data['levels'][0]['exos'][0]['id'],
                                                                    'ok': False, 'revoir': True}).get_json()
            self.assertEqual((d['event'], d['level']), ('review', 1))
        # practice on another level does not move progress
        exo = self.data['levels'][4]['exos'][0]['id']
        d = self.c.post(f'/api/niveaux/{SUBJECT}/result', json={'level': 5, 'exo_id': exo, 'ok': True}).get_json()
        self.assertEqual((d['event'], d['level']), ('practice', 1))
        # wrong exercise id for the level is rejected
        r = self.c.post(f'/api/niveaux/{SUBJECT}/result', json={'level': 1, 'exo_id': 'zzz', 'ok': True})
        self.assertEqual(r.status_code, 400)
        # another account starts at level 1
        other = self.app.test_client()
        other.post('/api/register', json={'username': 'carol', 'password': 'secret1'})
        self.assertIn('Continuer au niveau 1', other.get('/niveaux').get_data(as_text=True))

    def test_bet_double_and_pari_setting(self):
        self.register('gaby')
        self.assertIn('data-pari="0"', self.c.get(f'/niveaux/{SUBJECT}').get_data(as_text=True))  # off by default
        self.assertTrue(self.c.post('/api/pari', json={'on': True}).get_json()['on'])
        page = self.c.get(f'/niveaux/{SUBJECT}').get_data(as_text=True)
        self.assertIn('data-pari="1"', page)
        def post(**kw):  # a fresh page view (server clock) for each answer
            exo_id = self.c.get(f'/niveaux/{SUBJECT}').get_data(as_text=True).split('data-exo="')[1].split('"')[0]
            return self.c.post(f'/api/niveaux/{SUBJECT}/result', json={'level': 1, 'exo_id': exo_id, **kw}).get_json()
        with mock.patch('levels.random.random', return_value=0.0):  # « Coup double » drawn
            d = post(ok=True, conf=2)
        self.assertTrue(d['double'])
        self.assertEqual(d['calib'], levels.CALIB_POINTS)
        self.assertEqual(d['points'], 2 * levels.score(True, d['secs'], d['ref'], 0, 1) + levels.CALIB_POINTS)
        with mock.patch('levels.random.random', return_value=0.0):
            d = post(ok=False, conf=0)  # « Au hasard » and missed: lucid
        self.assertEqual((d['double'], d['calib'], d['points'], d['combo']), (False, levels.CALIB_POINTS, levels.CALIB_POINTS, 0))
        d = post(ok=False, conf=2)  # « Sûr » and missed: no lucidity points
        self.assertEqual((d['calib'], d['points']), (0, 0))

    def test_points_and_users_average(self):
        self.register('erin')
        d = self.answer(1, True)
        self.assertGreater(d['points'], 0)
        self.assertEqual(d['xp'], d['points'])
        page = self.c.get(f'/niveaux/{SUBJECT}').get_data(as_text=True)
        exo_id = page.split('data-exo="')[1].split('"')[0]
        d = self.c.post(f'/api/niveaux/{SUBJECT}/result', json={'level': 1, 'exo_id': exo_id, 'ok': True, 'peek': True}).get_json()
        self.assertTrue(d['peek'])
        # replayed answer without a page view: logged, no points
        d = self.c.post(f'/api/niveaux/{SUBJECT}/result', json={'level': 1, 'exo_id': exo_id, 'ok': True}).get_json()
        self.assertEqual(d['points'], 0)
        # helps are recorded by the server: extra time once, strongest help sets the points factor
        page = self.c.get(f'/niveaux/{SUBJECT}').get_data(as_text=True)
        exo_id = page.split('data-exo="')[1].split('"')[0]
        hint = lambda kind: self.c.post(f'/api/niveaux/{SUBJECT}/hint', json={'kind': kind})
        self.assertEqual(hint('nope').status_code, 400)
        first = hint('fiche').get_json()
        self.assertGreater(first['extra'], 0)
        self.assertEqual(first['div'], 2)
        self.assertEqual(hint('fiche').get_json()['extra'], 0)
        d = self.c.post(f'/api/niveaux/{SUBJECT}/result', json={'level': 1, 'exo_id': exo_id, 'ok': True}).get_json()
        self.assertEqual(d['peek'], 2)
        self.assertEqual(levels.hint_code(['fiche', 'solution']), 1)
        self.assertEqual(levels.hint_limit(100, ['fiche', 'solution', 'fiche']), 250)
        # "more time" only: extra time, points not divided
        self.c.get(f'/niveaux/{SUBJECT}')
        t = hint('temps').get_json()
        self.assertGreater(t['extra'], 0)
        self.assertEqual(t['div'], 1)
        self.assertEqual(levels.hint_code(['temps']), 0)
        self.assertEqual(levels.hint_limit(100, ['temps']), 200)
        # after MIN_SAMPLES successes, the reference time comes from the users' average
        with levels.db() as conn:
            for _ in range(levels.MIN_SAMPLES):
                conn.execute("INSERT INTO exo_log (account_id, subject, level, exo_id, ok, secs) VALUES (1, ?, 2, 'x', 1, 40)", (SUBJECT,))
            lvl = self.data['levels'][1]
            ref, limit = levels.timing(conn, SUBJECT, lvl, lvl['exos'][0])
        mean = sum(int(e.get('duree', 5)) for e in lvl['exos']) / len(lvl['exos'])
        self.assertAlmostEqual(ref, 40 * int(lvl['exos'][0].get('duree', 5)) / mean, delta=1)
        self.assertGreaterEqual(limit, min(int(lvl['exos'][0].get('duree', 5)) * 60, levels.MIN_LIMIT))

    def test_abandon_path_clears_stats_and_reviews(self):
        self.register('quitter')
        self.answer(1, False)  # a miss: would come back in the spaced review
        self.c.get(f'/niveaux/{SUBJECT}?facile=x')
        with levels.db() as conn:
            uid = conn.execute("SELECT id FROM account WHERE username='quitter'").fetchone()[0]
        bad = self.c.post(f'/niveaux/{SUBJECT}/abandon', data={'mode': 'x'})
        self.assertEqual(bad.status_code, 400)
        r = self.c.post(f'/niveaux/{SUBJECT}/abandon', data={'mode': 'recommencer'})
        self.assertEqual(r.status_code, 302)
        with levels.db() as conn:
            for t in ('exo_log', 'event_log', 'level_progress'):
                self.assertEqual(conn.execute(f'SELECT COUNT(*) FROM {t} WHERE account_id=? AND subject=?',
                                              (uid, SUBJECT)).fetchone()[0], 0, t)
            self.assertEqual(conn.execute('SELECT COUNT(*) FROM exo_log_archive WHERE account_id=?', (uid,)).fetchone()[0], 1)
            self.assertEqual(levels.prestige(conn, uid, SUBJECT), 1)
        self.assertIn('Prestige 1', self.c.get('/niveaux').get_data(as_text=True))
        self.answer(1, True)
        self.c.post(f'/niveaux/{SUBJECT}/abandon', data={'mode': 'erreur'})  # misclick: no prestige
        with levels.db() as conn:
            self.assertEqual(levels.prestige(conn, uid, SUBJECT), 1)
            self.assertEqual(levels.xp(conn, uid), 0)

    def test_password_reset(self):
        sent = []
        sync = lambda target, args, daemon: type('T', (), {'start': lambda self: target(*args)})()  # noqa: E731
        with mock.patch.object(levels, 'send_mail', lambda to, subject, body: sent.append((to, body))), \
                mock.patch.object(levels.threading, 'Thread', sync):
            self._reset_flow(sent)

    def _reset_flow(self, sent):
        self.c.post('/api/register', json={'username': 'frank', 'password': 'secret1', 'email': 'f@example.org'})
        self.c.post('/api/logout')
        self.assertEqual(self.c.post('/api/reset/request', json={'who': 'nobody'}).status_code, 200)
        self.c.post('/api/reset/request', json={'who': 'f@example.org'})
        self.c.post('/api/reset/request', json={'who': 'frank'})  # cooldown: no second mail
        self.assertEqual(len(sent), 1)
        token = sent[0][1].split('reset=')[1].split()[0]
        self.assertTrue(sent[0][1].count('https://epitadoomscrolling.pierref.eu/compte?reset='))
        self.assertEqual(self.c.post('/api/reset/confirm', json={'token': 'bad', 'password': 'newpass1'}).status_code, 400)
        self.assertEqual(self.c.post('/api/reset/confirm', json={'token': token, 'password': 'newpass1'}).status_code, 200)
        self.assertEqual(self.c.post('/api/reset/confirm', json={'token': token, 'password': 'again11'}).status_code, 400)
        self.c.post('/api/logout')
        self.assertEqual(self.c.post('/api/login', json={'username': 'frank', 'password': 'newpass1'}).status_code, 200)

    def test_every_level_renders(self):
        self.register('dave')
        for sid, data in levels.load_parcours().items():
            for lvl in data['levels']:
                r = self.c.get(f'/niveaux/{sid}?n={lvl["n"]}')
                self.assertEqual(r.status_code, 200, (sid, lvl['n']))
                self.assertIn('Rappel de cours du niveau', r.get_data(as_text=True))  # per-exercise formulas shown
                self.assertTrue(all(e.get('formules') for e in lvl['exos']), (sid, lvl['n']))
            self.assertIn('Formules du niveau', r.get_data(as_text=True))

    def test_exam_calendar(self):
        from datetime import date
        syl = json.loads((levels.PARCOURS_DIR / 'syllabus.json').read_text(encoding='utf-8'))
        syl['calendrier'] = _S1_CAL
        cal = levels.exam_calendar(date(2026, 12, 15), syllabus=syl)
        apis = next(e for e in cal['upcoming'] if e.get('ecue') == 'maths/S1/APIS' and e['type'] == 'Examen')
        self.assertTrue(apis['en_cours'])  # 14-18 Dec
        self.assertEqual(apis['links'][0]['url'], '/niveaux/maths-s1-apis-integrales')
        self.assertTrue(all(l['exam_url'] for l in apis['links']))
        self.assertEqual(cal['past'][0]['titre'], 'Test à distance : APIS en entier')  # most recent first
        undated = {e['titre'] for e in cal['undated']}
        self.assertIn('Outils de base mathématiques', undated)
        self.assertNotIn('Dénombrement et probabilités', undated)  # has a date
        months = cal['months']
        self.assertEqual((len(months), months[0]['anchor'], months[-1]['anchor']), (11, 'm2026-9', 'm2027-7'))
        self.assertIn('Thermodynamique', [e['titre'] for e in months[8]['probable']])  # « partiel en mai »
        html = self.c.get('/calendrier').get_data(as_text=True)  # public page
        self.assertIn('Calendrier des examens', html)
        self.assertIn('morgan-footer', html)

    def test_exam_calendar_semester_filter(self):
        from datetime import date
        syl = json.loads((levels.PARCOURS_DIR / 'syllabus.json').read_text(encoding='utf-8'))
        syl['calendrier'] = _S1_CAL + [
            {'debut': '2026-11-23', 'titre': 'Contrôle PSE', 'type': 'Contrôle', 'source': 'Mail EPITA', 'ecue': 'maths/S3/PSE'},
            {'debut': '2026-11-24', 'titre': 'Annonce', 'type': 'Examen', 'source': 'Mail EPITA', 'semestre': 'S3'},
            {'debut': '2026-11-25', 'titre': 'Sans semestre', 'type': 'Examen', 'source': 'Mail EPITA'}]
        titres = lambda c: {e['titre'] for m in c['months'] for e in m['events']}  # noqa: E731
        allc = levels.exam_calendar(date(2026, 11, 20), syllabus=syl)
        self.assertTrue({'S1', 'S3', 'none'} <= set(allc['sems']) and allc['sems'][-1] == 'none')  # + semesters of undated ECUEs
        s3 = levels.exam_calendar(date(2026, 11, 20), syllabus=syl, sem='S3')
        nov = next(m for m in s3['months'] if m['anchor'] == 'm2026-11')
        self.assertEqual((nov['exams'], nov['tests']), (2, 0))  # Contrôle and Examen are both « exams » (red)
        self.assertEqual(titres(s3), {'Contrôle PSE', 'Annonce'})  # explicit `semestre` and ECUE semester
        self.assertEqual(levels.exam_calendar(date(2026, 11, 20), syllabus=syl, sem='none')['upcoming'][0]['titre'], 'Sans semestre')
        self.assertTrue({'Contrôle PSE', 'Annonce', 'Sans semestre'} < titres(allc))  # no filter: everything stays
        self.assertTrue(all(e['semestre'] == 'S3' for e in s3['undated']))
        self.register('cal_user')
        html = self.c.get('/calendrier?sem=S3').get_data(as_text=True)
        self.assertIn('data-sem="tous"', html)
        self.assertIn('Contrôle de cours AL', html)
        self.assertNotIn('Test Moodle 1', html)  # S1 hidden when S3 is selected

    def test_copy_for_ai_button(self):
        self.register('copy_user')
        html = self.c.get(f'/niveaux/{SUBJECT}').get_data(as_text=True)
        self.assertIn('data-copy-llm="#exo-statement|Énoncé; #solution-body|Correction"', html)
        self.assertIn('https://morgan.pierref.eu', html)
        self.assertIn(f'/niveaux/{SUBJECT}?n=', html)
        self.assertIn('/static/copy-for-llm.js', html)

    def test_prerequisite_links_after_failure(self):
        paths = levels.load_parcours()
        for sid, pre in levels.PREREQ.items():
            self.assertIn(sid, paths)
            self.assertTrue(all(p in paths and p != sid for p in pre), sid)
        self.register('prereq_user')
        r = self.answer(1, False)
        self.assertEqual([p['id'] for p in r['prereq']], levels.PREREQ.get(SUBJECT, []))
        self.assertNotIn('prereq', self.answer(1, True))


if __name__ == '__main__':
    unittest.main()


class Stats(unittest.TestCase):
    def test_compute_stats(self):
        from datetime import date, datetime
        today = date(2026, 11, 14)
        def row(day, hour, exo, ok, secs=60):
            return {'subject': 's', 'level': 1, 'exo_id': exo, 'ok': ok, 'secs': secs, 'timeout': 0,
                    'at': datetime(2026, 11, day, hour)}
        rows = [row(12, 9, 'a', 0), row(13, 9, 'a', 1), row(13, 10, 'b', 1, 99999), row(14, 9, 'c', 0)]
        s = levels.compute_stats(rows, today, {'s': 'Sujet'})
        self.assertEqual((s['done'], s['ok'], s['ko'], s['rate']), (4, 2, 2, 50))
        self.assertEqual(s['minutes'], (60 * 3 + levels.MAX_SECS) // 60)
        self.assertEqual((s['streak'], s['best_streak'], s['active_days']), (3, 3, 3))
        self.assertEqual(s['revenge'], 1)
        self.assertEqual(s['first_try'], 33)
        self.assertEqual(s['hardest']['subject'], 'Sujet')
        self.assertEqual(s['hour'], 9)
        last = s['weeks'][-1]
        self.assertEqual(last[5]['color'], levels.day_color(0, 1))  # Saturday 14 nov: red
        self.assertIsNone(last[6])                                   # Sunday: future
        self.assertEqual(len(s['chart']), 30)
        self.assertEqual(s['chart'][-2]['min'], 31)
        self.assertEqual(len(s['chart_all']), 30)  # first activity inside the last 30 days: one window
        self.assertEqual([w['label'] for w in s['heat_weeks']], ['Semaine du 9 nov. (en cours)'])
        old = levels.compute_stats(rows + [row(1, 9, 'd', 1)], date(2026, 12, 20))  # 1 nov is 49 days back
        self.assertEqual(len(old['chart_all']), 30 + 7 * 3)
        self.assertEqual(old['chart_all'][-30:], [{'label': c['label'], 'min': c['min']} for c in old['chart']])
        self.assertEqual(len(old['heat_weeks']), 8)  # weeks of 26 oct .. 14 dec
        self.assertEqual(sum(r['total'] for r in old['heat_weeks'][2]['heat']), 4)  # week of 9 nov

    def test_week_history(self):
        from datetime import date, datetime
        today = date(2026, 11, 18)  # Wednesday; weeks start on Mondays 2, 9 and 16 nov
        def row(day, ok, secs=120, points=10):
            return {'ok': ok, 'secs': secs, 'points': points, 'review': 0, 'at': datetime(2026, 11, day, 9)}
        rows = [row(3, 1), row(3, 0), row(17, 1), row(18, 1, 99999)]
        events = [{'kind': 'passer', 'at': datetime(2026, 11, 17, 9)}, {'kind': 'aide_fiche', 'at': datetime(2026, 11, 17, 9)},
                  {'kind': 'niveau_up', 'at': datetime(2026, 11, 3, 9)}, {'kind': 'copie_ia', 'at': datetime(2026, 11, 18, 9)}]
        h = levels.week_history(rows, events, today)
        self.assertEqual([w['label'] for w in h], ['16 nov.', '9 nov.', '2 nov.'])
        now, empty, first = h
        self.assertTrue(now['current'])
        self.assertEqual((now['n'], now['rate'], now['days'], now['skip'], now['help'], now['copies']), (2, 100, 2, 1, 1, 1))
        self.assertEqual(now['minutes'], round((120 + levels.MAX_SECS) / 60))
        self.assertEqual((empty['n'], empty['rate'], empty['delta']['n']), (0, None, -2))
        self.assertNotIn('rate', now['delta'])  # no rate the week before: no change shown
        self.assertEqual((first['rate'], first['up'], first['delta']), (50, 1, None))
        self.assertEqual(levels.week_history([], [], today), [])


class Leaderboard(unittest.TestCase):
    def test_period_start_is_local_midnight_in_utc(self):
        from datetime import datetime
        from zoneinfo import ZoneInfo
        now = datetime(2026, 11, 18, 10, 0, tzinfo=ZoneInfo('Europe/Paris'))  # a Wednesday, UTC+1
        self.assertEqual(levels.period_start('jour', now), '2026-11-17 23:00:00')
        self.assertEqual(levels.period_start('semaine', now), '2026-11-15 23:00:00')
        self.assertEqual(levels.period_start('mois', now), '2026-10-31 23:00:00')
        self.assertEqual(levels.period_start('annee', now), '2025-12-31 23:00:00')

    def test_opt_in_period_and_subject_filter(self):
        import sqlite3
        conn = sqlite3.connect(':memory:')
        conn.executescript(levels.SCHEMA)
        conn.execute('ALTER TABLE account ADD COLUMN leaderboard INTEGER NOT NULL DEFAULT 0')
        conn.execute('ALTER TABLE account ADD COLUMN board_ban INTEGER NOT NULL DEFAULT 0')
        conn.executemany('INSERT INTO account (id, username, pw_hash, leaderboard) VALUES (?, ?, ?, ?)',
                         [(1, 'ann', 'x', 1), (2, 'ben', 'x', 1), (3, 'hid', 'x', 0)])
        log = 'INSERT INTO exo_log (account_id, subject, level, exo_id, ok, secs, points, at) VALUES (?, ?, 1, ?, 1, ?, ?, ?)'
        conn.executemany(log, [(1, 'a', 'e', 600, 10, '2026-11-18 08:00:00'), (2, 'a', 'e', 99999, 5, '2026-11-18 08:00:00'),
                               (2, 'b', 'e', 60, 50, '2026-11-18 08:00:00'), (1, 'a', 'e', 900, 99, '2026-11-01 08:00:00'),
                               (3, 'a', 'e', 5000, 500, '2026-11-18 08:00:00')])
        ev = 'INSERT INTO event_log (account_id, kind, subject, level, at) VALUES (?, ?, ?, ?, ?)'
        conn.executemany(ev, [(1, 'niveau_up', 'a', 1, '2026-11-18 08:00:00'), (1, 'niveau_up', 'a', 1, '2026-11-18 09:00:00'),
                              (1, 'niveau_up', 'a', 2, '2026-11-18 09:00:00'), (2, 'niveau_down', 'a', 1, '2026-11-18 09:00:00')])
        b = levels.leaderboards(conn, '2026-11-17 23:00:00')
        self.assertEqual([(r[1], r[2]) for r in b['points']], [('ben', 55), ('ann', 10)])  # hidden and older rows out
        self.assertEqual([(r[1], r[2]) for r in b['temps']], [('ben', levels.MAX_SECS + 60), ('ann', 600)])  # capped
        self.assertEqual([(r[1], r[2]) for r in b['niveaux']], [('ann', 2)])  # same level twice counts once
        self.assertEqual([r[1] for r in levels.leaderboards(conn, '2026-11-17 23:00:00', ['a'])['points']], ['ann', 'ben'])

    def test_ranks_ties(self):
        self.assertEqual(levels.ranks([9, 9, 5, 4, 4, 1]), [1, 1, 3, 4, 4, 6])
        self.assertEqual(levels.ranks([]), [])

    def test_page_and_toggle(self):
        import app as app_module
        c = app_module.app.test_client()
        self.assertEqual(c.get('/classement').status_code, 302)
        c.post('/api/register', json={'username': 'boarduser', 'password': 'secret1'})
        html = c.get('/classement?p=mois&m=maths').get_data(as_text=True)
        self.assertIn('morgan-footer', html)
        self.assertNotIn('boarduser</td>', html)
        self.assertTrue(c.post('/api/classement', json={'visible': True}).get_json()['visible'])
        self.assertIn('checked', c.get('/compte').get_data(as_text=True))


class Cheat(unittest.TestCase):
    def test_suspects(self):
        authored = {('a', 1): 300, ('b', 1): 300}  # usual time 180 s until MIN_SAMPLES successes
        honest = [(1, 'a', 1, i % 7 != 0, 150, i * 400) for i in range(60)]
        fast = [(2, 'a', 1, 1, 10, i * 20) for i in range(6)]  # 10 s < 20 % of 180 s
        streak = [(3, 'b', 1, 1, 200, i * 400) for i in range(levels.STREAK_FLAG)]
        ups = [(4, s, n, 100 * n) for s in ('a', 'b') for n in (1, 2)] + [(1, 'a', n, 4000 * n) for n in range(1, 5)]
        found = levels.suspects(honest + fast + streak, ups, {'a': 'maths', 'b': 'algo'}, authored)
        self.assertEqual(sorted(found), [2, 3, 4])
        self.assertIn('6 réussites trop rapides', found[2][0])
        self.assertIn(f"{levels.STREAK_FLAG} réussites d'affilée", found[3][0])
        self.assertIn('4 niveaux validés', found[4][0])

    def test_ban_hides_from_board_and_is_admin_only(self):
        import sqlite3
        conn = sqlite3.connect(':memory:')
        conn.executescript(levels.SCHEMA)
        conn.execute('ALTER TABLE account ADD COLUMN leaderboard INTEGER NOT NULL DEFAULT 1')
        conn.execute('ALTER TABLE account ADD COLUMN board_ban INTEGER NOT NULL DEFAULT 0')
        conn.executemany('INSERT INTO account (id, username, pw_hash, board_ban) VALUES (?, ?, ?, ?)', [(1, 'ok', 'x', 0), (2, 'ban', 'x', 1)])
        conn.executemany("INSERT INTO exo_log (account_id, subject, level, exo_id, ok, secs, points) VALUES (?, 'a', 1, 'e', 1, 60, 9)", [(1,), (2,)])
        self.assertEqual([r[1] for r in levels.leaderboards(conn, '2000-01-01 00:00:00')['points']], ['ok'])
        import app as app_module
        c = app_module.app.test_client()
        c.post('/api/register', json={'username': 'notadmin', 'password': 'secret1'})
        self.assertEqual(c.post('/api/admin/classement', json={'account_id': 1, 'ban': True}).status_code, 403)


class FraudWarning(unittest.TestCase):
    def test_flagged_user_sees_warning(self):
        import app as app_module
        c = app_module.app.test_client()
        c.post('/api/register', json={'username': 'fastcheat', 'password': 'secret1'})
        self.assertNotIn('fraud-warn', c.get('/stats').get_data(as_text=True))
        with mock.patch.object(levels, 'all_suspects', lambda conn: {levels.session['uid']: ['6 réussites trop rapides']}):
            html = c.get('/stats').get_data(as_text=True)
            self.assertIn('fraud-warn', html)
            self.assertIn('6 réussites trop rapides', html)
            page = c.get(f'/niveaux/{SUBJECT}').get_data(as_text=True)
            exo_id = page.split('data-exo="')[1].split('"')[0]
            d = c.post(f'/api/niveaux/{SUBJECT}/result', json={'level': 1, 'exo_id': exo_id, 'ok': True}).get_json()
            self.assertIn('Triche suspectée', d['warning'])
