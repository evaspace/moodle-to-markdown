import html
import os
import tempfile
import unittest

os.environ.update(DB_PATH=os.path.join(tempfile.mkdtemp(), "test.db"), COOKIE_INSECURE="1", SECRET_KEY="test")

import blogsection  # noqa: E402
from app import app  # noqa: E402


class BlogTest(unittest.TestCase):
    def setUp(self):
        self.c = app.test_client()

    def test_every_article_renders(self):
        arts = blogsection.articles()
        self.assertGreaterEqual(len(arts), 3)
        self.assertIn(html.escape(arts[0]['title']), self.c.get('/blog/').get_data(as_text=True))
        for a in arts:
            r = self.c.get(f'/blog/{a["slug"]}')
            self.assertEqual(r.status_code, 200, a['slug'])
            self.assertIn(a['title'], r.get_data(as_text=True))

    def test_blogbot_json_article(self):
        """blogbot drops <slug>.json in articles/: the site shows it in its own layout."""
        import json
        from pathlib import Path
        d = Path(tempfile.mkdtemp())
        (d / 'images').mkdir()
        (d / 'images' / 'x.jpg').write_bytes(b'jpg')
        (d / 'bot-post.json').write_text(json.dumps({
            'title': 'Titre bot', 'slug': 'bot-post', 'date': '2030-01-01', 'meta_description': 'Desc bot',
            'markdown_content': '# Titre bot\n\nCorps $x^2$.\n\n![a](/blog/images/x.jpg)\n\n'
                                '<script type="application/ld+json">{"@type": "Article"}</script>\n'}))
        old, blogsection.DIR = blogsection.DIR, d
        try:
            self.assertEqual(blogsection.articles()[0]['slug'], 'bot-post')
            html = self.c.get('/blog/bot-post').get_data(as_text=True)
            self.assertIn('Corps', html)
            self.assertNotIn('"@type": "Article"', html)  # JSON-LD block dropped, not shown as text
            self.assertEqual(html.count('Titre bot</h1>'), 1)  # leading "# title" not repeated
            self.assertEqual(self.c.get('/blog/images/x.jpg').status_code, 200)
            r = self.c.get('/blog/bot-post.html')
            self.assertEqual((r.status_code, r.location), (301, '/blog/bot-post'))
            self.assertIn('/blog/bot-post</loc>', self.c.get('/sitemap.xml').get_data(as_text=True))
        finally:
            blogsection.DIR = old

    def test_legacy_and_unknown(self):
        self.assertEqual(self.c.get('/blog/old-post.html').status_code, 301)
        self.assertEqual(self.c.get('/blog/nope').status_code, 404)


if __name__ == '__main__':
    unittest.main()
