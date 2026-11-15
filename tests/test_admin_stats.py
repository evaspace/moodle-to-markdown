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


if __name__ == '__main__':
    unittest.main()
