"""Blog section: Markdown articles in `articles/*.md`, rendered inside the app (nav, footer, KaTeX).

Each file starts with a `---` block (`title`, `date` as YYYY-MM-DD, `description`); the slug is the file name.
blogbot (/opt/pierref/blogbot) also drops `articles/<slug>.json` (title, date, meta_description, markdown_content)
and its images in `articles/images/`, served at `/blog/images/`.
`/blog/<slug>.html` redirects to `/blog/<slug>` if it exists, else to the index.
"""
import json
import re
from datetime import date
from pathlib import Path

from flask import Blueprint, abort, redirect, render_template, send_from_directory, url_for

bp = Blueprint('blog', __name__)
DIR = Path(__file__).parent / 'articles'
MONTHS = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']


SCRIPT_RE = re.compile(r'<script\b.*?</script>', re.S | re.I)


def _parse(path):
    if path.suffix == '.json':  # blogbot: drop its "# title" line (the template prints it) and its JSON-LD
        j = json.loads(path.read_text(encoding='utf-8'))
        body = SCRIPT_RE.sub('', re.sub(r'\A\s*# .*\n', '', j['markdown_content']))
        meta = {'title': j['title'], 'date': j['date'], 'description': j['meta_description']}
    else:
        head, _, body = path.read_text(encoding='utf-8').removeprefix('---\n').partition('\n---\n')
        meta = dict(line.split(':', 1) for line in head.splitlines() if ':' in line)
        meta = {k.strip(): v.strip() for k, v in meta.items()}
    d = date.fromisoformat(meta['date'])
    return {'slug': path.stem, 'title': meta['title'], 'description': meta['description'], 'date': d.isoformat(),
            'date_fr': f'{d.day} {MONTHS[d.month - 1]} {d.year}', 'body': body.strip(),
            'minutes': max(1, round(len(body.split()) / 200))}


def articles():
    """Newest first; read on every call (a handful of small files), so a new file shows without restart."""
    return sorted((_parse(p) for p in [*DIR.glob('*.md'), *DIR.glob('*.json')]), key=lambda a: a['date'], reverse=True)


@bp.route('/blog')
@bp.route('/blog/')
def index():
    return render_template('blog.html', articles=articles())


@bp.route('/blog/images/<path:name>')
def image(name):
    return send_from_directory(DIR / 'images', name)


def _find(slug):
    return next((p for p in (DIR / f'{slug}.md', DIR / f'{slug}.json') if '/' not in slug and p.is_file()), None)


@bp.route('/blog/<slug>')
def article(slug):
    if slug.endswith('.html') or slug == 'images':  # old static blog / blogbot URLs
        stem = slug.removesuffix('.html')
        return redirect(f'/blog/{stem}' if _find(stem) else url_for('blog.index'), 301)
    path = _find(slug)
    if not path:
        abort(404)
    from app import render_markdown_with_math  # same Markdown + LaTeX renderer as the course pages
    a = _parse(path)
    return render_template('article.html', a=a, html=render_markdown_with_math(a['body']))
