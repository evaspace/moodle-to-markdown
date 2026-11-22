#!/usr/bin/env python3
"""Security guards: foreign Origin rejected, login lockout, request size cap."""
import os
import sys
import tempfile
import unittest
from pathlib import Path

TMP = tempfile.mkdtemp()
os.environ.update(DB_PATH=os.path.join(TMP, 'test.db'), COOKIE_INSECURE='1', SECRET_KEY='test')
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import app  # noqa: E402
import ratelimit  # noqa: E402


class Security(unittest.TestCase):
    def setUp(self):
        ratelimit._hits.clear()
        self.c = app.test_client()

    def test_foreign_origin_rejected(self):
        r = self.c.post('/api/login', json={'username': 'x', 'password': 'y'}, headers={'Origin': 'https://evil.example'})
        self.assertEqual(r.status_code, 403)
        r = self.c.post('/api/login', json={'username': 'x', 'password': 'y'},
                        headers={'Origin': 'https://epitadoomscrolling.pierref.eu'})
        self.assertEqual(r.status_code, 401)

    def test_login_lockout_per_username(self):
        self.c.post('/api/register', json={'username': 'victim', 'password': 'goodpass'})
        self.c.post('/api/logout')
        for _ in range(10):
            self.assertEqual(self.c.post('/api/login', json={'username': 'victim', 'password': 'bad'}).status_code, 401)
        # locked even with the right password, and other accounts still work
        self.assertEqual(self.c.post('/api/login', json={'username': 'VICTIM', 'password': 'goodpass'}).status_code, 429)
        self.c.post('/api/register', json={'username': 'other', 'password': 'goodpass'})
        self.c.post('/api/logout')
        self.assertEqual(self.c.post('/api/login', json={'username': 'other', 'password': 'goodpass'}).status_code, 200)

    def test_body_size_cap(self):
        r = self.c.post('/api/client-log', data='x' * (3 * 1024 * 1024))
        self.assertEqual(r.status_code, 413)


if __name__ == '__main__':
    unittest.main()
