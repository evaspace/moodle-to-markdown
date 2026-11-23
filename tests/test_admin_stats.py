import sys
import unittest
from datetime import date, datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from admin_stats import compute  # noqa: E402

TODAY = date(2026, 11, 15)
PATHS = {'p': {'titre': 'Path', 'levels': 3}}


def log(u, days_ago, ok=1, exo='a', level=1):
    return dict(account_id=u, subject='p', level=level, exo_id=exo, ok=ok, secs=60, peek=0, timeout=0,
                at=datetime(2026, 11, 15, 10) - timedelta(days=days_ago))


class AdminStats(unittest.TestCase):
    def test_empty(self):
        s = compute([], [], [], PATHS, TODAY)
        self.assertEqual((s['accounts'], s['exercises'], s['activation']), (0, 0, 0))

    def test_retention_activation_hard(self):
        accounts = [dict(id=1, created=TODAY - timedelta(days=10), email='x'), dict(id=2, created=TODAY - timedelta(days=10), email=None)]
        logs = [log(1, 10), log(1, 9)] + [log(2, 0, ok=0, exo='h') for _ in range(5)]
        s = compute(accounts, logs, [dict(account_id=1, subject='p', level=2, best=1)], PATHS, TODAY)
        self.assertEqual(s['activation'], 100)
        self.assertEqual(s['with_email'], 50)
        self.assertEqual(s['retention']['d1']['pct'], 50)   # only account 1 came back the day after
        self.assertEqual(s['hard'][0]['exo'], 'h')
        self.assertEqual(s['hard'][0]['fail'], 100)
        self.assertEqual(s['funnel'][0]['started'], 2)
        self.assertEqual(s['funnel'][0]['bars'][0]['n'], 1)

    def test_events_and_history(self):
        events = [dict(kind='aide_fiche', at=datetime(2026, 11, 14, 9)), dict(kind='niveau_finished', at=datetime(2026, 11, 1, 9))]
        s = compute([dict(id=1, created=TODAY, email=None)], [log(1, 0)], [], PATHS, TODAY, events)
        self.assertEqual((s['events']['aide']['all'], s['events']['aide']['week']), (1, 1))
        self.assertEqual((s['events']['niveau_up']['all'], s['events']['niveau_up']['week']), (1, 0))
        self.assertEqual(s['history'][0]['n'], 1)

    def test_owner_apart(self):
        accounts = [dict(id=1, created=TODAY, email=None), dict(id=9, created=TODAY, email='o')]
        logs = [log(1, 0), log(9, 0), log(9, 0, ok=0)]
        events = [dict(account_id=9, kind='passer', at=datetime(2026, 11, 15, 9))]
        progress = [dict(account_id=9, subject='p', level=2, best=1)]
        s = compute(accounts, logs, progress, PATHS, TODAY, events, owner_ids=[9])
        self.assertEqual((s['accounts'], s['exercises'], s['success']), (1, 1, 100))
        self.assertEqual((s['me']['accounts'], s['me']['exercises'], s['me']['success']), (1, 2, 50))
        self.assertEqual((s['events']['passer']['all'], s['me']['events']['passer']['all']), (0, 1))
        today = s['exo_chart'][-1]
        self.assertEqual((today['n'], today['me'], today['h'], today['hm']), (1, 2, 33, 67))
        f = s['funnel'][0]
        self.assertEqual((f['started'], f['me']['started'], f['bars'][0]['hm']), (1, 1, 50))
        self.assertNotIn('_exo', s['me'])


if __name__ == '__main__':
    unittest.main()
