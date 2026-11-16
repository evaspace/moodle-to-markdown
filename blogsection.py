"""Blog section: Markdown articles in `articles/*.md`, rendered inside the app (nav, footer, KaTeX).

Each file starts with a `---` block (`title`, `date` as YYYY-MM-DD, `description`); the slug is the file name.
Old blogbot URLs (`/blog/<slug>.html`) redirect to the index.
"""
from datetime import date
from pathlib import Path

from flask import Blueprint, abort, redirect, render_template, url_for

bp = Blueprint('blog', __name__)
DIR = Path(__file__).parent / 'articles'
MONTHS = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']


def _parse(path):
    head, _, body = path.read_text(encoding='utf-8').removeprefix('---\n').partition('\n---\n')
    meta = dict(line.split(':', 1) for line in head.splitlines() if ':' in line)
    meta = {k.strip(): v.strip() for k, v in meta.items()}
    d = date.fromisoformat(meta['date'])
    return {'slug': path.stem, 'title': meta['title'], 'description': meta['description'], 'date': d.isoformat(),
            'date_fr': f'{d.day} {MONTHS[d.month - 1]} {d.year}', 'body': body.strip(),
            'minutes': max(1, round(len(body.split()) / 200))}


def articles():
    """Newest first; read on every call (a handful of small files), so a new file shows without restart."""
    return sorted((_parse(p) for p in DIR.glob('*.md')), key=lambda a: a['date'], reverse=True)


@bp.route('/blog')
@bp.route('/blog/')
def index():
    return render_template('blog.html', articles=articles())


@bp.route('/blog/<slug>')
def article(slug):
    if slug.endswith('.html') or slug == 'images':  # old static blog
        return redirect(url_for('blog.index'), 301)
    path = DIR / f'{slug}.md'
    if '/' in slug or not path.is_file():
        abort(404)
    from app import render_markdown_with_math  # same Markdown + LaTeX renderer as the course pages
    a = _parse(path)
    return render_template('article.html', a=a, html=render_markdown_with_math(a['body']))
