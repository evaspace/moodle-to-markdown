import unittest

import fiches
from app import app


class TestFiches(unittest.TestCase):
    def test_no_duplicate_id_nor_broken_link(self):
        self.assertEqual(fiches.check(), [])

    def test_sheet_page_shows_links_and_search_box_on_index(self):
        client = app.test_client()
        page = client.get('/cours/fiches/APIS-3.12').get_data(as_text=True)
        self.assertIn('data-pagefind-meta="id:APIS-3.12"', page)
        self.assertIn('/niveaux/maths-s1-apis-integrales?n=6', page)
        self.assertIn('/cours/fiches/APIS-3.8', page)
        self.assertEqual(client.get('/cours/fiches/NOPE-1.1').status_code, 404)
