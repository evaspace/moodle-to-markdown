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
        self.assertIn(arts[0]['title'], self.c.get('/blog/').get_data(as_text=True))
        for a in arts:
            r = self.c.get(f'/blog/{a["slug"]}')
            self.assertEqual(r.status_code, 200, a['slug'])
            self.assertIn(a['title'], r.get_data(as_text=True))

    def test_legacy_and_unknown(self):
        self.assertEqual(self.c.get('/blog/old-post.html').status_code, 301)
        self.assertEqual(self.c.get('/blog/nope').status_code, 404)


if __name__ == '__main__':
    unittest.main()
