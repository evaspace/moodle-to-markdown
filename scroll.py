"""Adaptive scroll on a level path's notions (course cards) and quiz (QCM / vrai-faux).

Rules (README_OBJECTIFS.md, mode Scroll):
- about 1 course card out of 4, the rest are questions;
- a notion seen on a course card is tested 1 or 2 cards later;
- a wrong answer brings a course card on that notion next, and the missed question comes back later;
- the scroll level moves at every answer (+1 right, -1 wrong) and unlocks notions in syllabus order;
- the scroll never changes the exercise levels (separate tables).
"""
import random
import sqlite3
from collections import namedtuple

from flask import Blueprint, jsonify, render_template, request, session

from init_db import DB_PATH
from levels import db, get_parcours, login_required

bp = Blueprint('scroll', __name__)
COURSE_EVERY = 4      # one course card in the last COURSE_EVERY - 1 cards at least
PTS_PER_NOTION = 2    # right answers needed to unlock the next notion
RETRY_AFTER = 4       # a missed question comes back after this many cards
Item = namedtuple('Item', 'kind key notion ok')  # kind 'c' (course, key = notion id) or 'q' (quiz, key = index)

SCHEMA = '''
    CREATE TABLE IF NOT EXISTS scroll_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_id INTEGER NOT NULL,
        subject TEXT NOT NULL,
        kind TEXT NOT NULL,
        key TEXT NOT NULL,
        notion TEXT NOT NULL,
        ok INTEGER,
        at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE INDEX IF NOT EXISTS idx_scroll_log ON scroll_log(account_id, subject, id);
    CREATE TABLE IF NOT EXISTS scroll_progress (
        account_id INTEGER NOT NULL,
        subject TEXT NOT NULL,
        pts INTEGER NOT NULL DEFAULT 0,
        PRIMARY KEY (account_id, subject)
    );
'''


def init_scroll_db(path=DB_PATH):
    with sqlite3.connect(path) as conn:
        conn.executescript(SCHEMA)


# ---------------------------------------------------------------- rules ----
def notion_order(data):
    """Notions in the order the levels first use them (= syllabus order), then the others."""
    order = []
    for lvl in data['levels']:
        order += [n for n in lvl['notions'] if n not in order]
    return order + [n['id'] for n in data['notions'] if n['id'] not in order]


def unlocked(pts, n_notions):
    """Number of notions open in the scroll for this score (at least 1)."""
    return min(n_notions, 1 + max(pts, 0) // PTS_PER_NOTION)


def next_card(history, order, quiz, pts, rng=random):
    """Pick the next card. history: Items oldest -> newest. Returns ('c', notion_id) or ('q', quiz_index)."""
    open_notions = order[:unlocked(pts, len(order))]
    by_notion = {}
    for i, q in enumerate(quiz):
        by_notion.setdefault(q['notion'], []).append(i)
    recent_q = {h.key for h in history[-3:] if h.kind == 'q'}

    def quiz_on(notion):
        pool = by_notion.get(notion, [])
        fresh = [i for i in pool if str(i) not in recent_q]
        return ('q', str(rng.choice(fresh or pool))) if pool else None

    last = history[-1] if history else None
    # 1. wrong answer: course card on that notion
    if last and last.kind == 'q' and last.ok == 0:
        return ('c', last.notion)
    # 2. a course card 1 or 2 cards ago whose notion has not been tested since
    for back in (1, 2):
        if len(history) >= back and history[-back].kind == 'c':
            notion = history[-back].key
            tested = any(h.kind == 'q' and h.notion == notion for h in history[len(history) - back + 1:])
            card = None if tested else quiz_on(notion)
            if card:
                return card
    # 3. a missed question comes back
    last_answer = {}
    for pos, h in enumerate(history):
        if h.kind == 'q':
            last_answer[h.key] = (pos, h.ok)
    for key, (pos, ok) in last_answer.items():
        if ok == 0 and len(history) - pos > RETRY_AFTER and int(key) < len(quiz):
            return ('q', key)
    # 4. at least one course card in the last COURSE_EVERY - 1 cards: newest open notion first,
    #    then the open notion with the least recent course card
    if not any(h.kind == 'c' for h in history[-(COURSE_EVERY - 1):]):
        seen = {h.key: pos for pos, h in enumerate(history) if h.kind == 'c'}
        newest = open_notions[-1]
        if newest not in seen:
            return ('c', newest)
        return ('c', min(open_notions, key=lambda nid: seen.get(nid, -1)))
    # 5. a question: half the time on the newest open notion, else any open notion
    notion = open_notions[-1] if rng.random() < 0.5 else rng.choice(open_notions)
    return quiz_on(notion) or ('c', notion)  # a notion without questions shows its course card


# ---------------------------------------------------------------- routes ----
def _history(conn, uid, subject, limit=40):
    rows = conn.execute('SELECT kind, key, notion, ok FROM scroll_log WHERE account_id=? AND subject=? '
                        'ORDER BY id DESC LIMIT ?', (uid, subject, limit)).fetchall()
    return [Item(r['kind'], r['key'], r['notion'], r['ok']) for r in reversed(rows)]


def _pts(conn, uid, subject):
    row = conn.execute('SELECT pts FROM scroll_progress WHERE account_id=? AND subject=?', (uid, subject)).fetchone()
    return row['pts'] if row else 0


def _inline(md, text):
    html = md(text).strip()
    return html[3:-4] if html.startswith('<p>') and html.endswith('</p>') and html.count('<p>') == 1 else html


def _progress(data, pts):
    order = notion_order(data)
    n = unlocked(pts, len(order))
    titles = {x['id']: x['titre'] for x in data['notions']}
    return {'unlocked': n, 'total': len(order), 'notion': titles[order[n - 1]]}


@bp.route('/api/client-log', methods=['POST'])
def client_log():
    """Browser-side errors and true/false tap traces (debug of the Android tap bug, 2026-11-17): written to the app log."""
    import logging
    body = (request.get_data(as_text=True) or '')[:2000]
    logging.getLogger('client').warning('client-log uid=%s ua=%s %s', session.get('uid'),
                                        (request.headers.get('User-Agent') or '')[:160], body)
    return '', 204


@bp.route('/scroll/<subject>')
@login_required
def scroll_page(subject):
    data = get_parcours(subject)
    with db() as conn:
        pts = _pts(conn, session['uid'], subject)
    return render_template('scroll.html', subject=data['subject'], progress=_progress(data, pts))


@bp.route('/api/scroll/<subject>/next')
@login_required
def scroll_next(subject):
    from app import render_markdown_with_math as md
    data = get_parcours(subject)
    uid = session['uid']
    notions = {x['id']: x for x in data['notions']}
    with db() as conn:
        pts = _pts(conn, uid, subject)
        kind, key = next_card(_history(conn, uid, subject), notion_order(data), data['quiz'], pts)
        if kind == 'c':  # course cards are logged when shown; questions when answered
            conn.execute('INSERT INTO scroll_log (account_id, subject, kind, key, notion) VALUES (?, ?, ?, ?, ?)',
                         (uid, subject, 'c', key, key))
    if kind == 'c':
        n = notions[key]
        card = {'kind': 'c', 'notion': key, 'titre': n['titre'], 'formule': md(n['formule']),
                'exemple': md(n['exemple']), 'cours': md(n['cours'])}
    else:
        q = data['quiz'][int(key)]
        # QCM choices in a new random order each time: recall the answer, not its position (README_OBJECTIFS).
        # The shown order stays in the session so the check is done on the server. Vrai/Faux keep their side (swipe).
        perm = random.sample(range(len(q['choix'])), len(q['choix'])) if q['type'] == 'qcm' else [0, 1]
        session['scroll_perm'] = [subject, key, perm]
        card = {'kind': 'q', 'key': key, 'type': q['type'], 'notion_titre': notions[q['notion']]['titre'],
                'q': _inline(md, q['q']),
                'choix': [_inline(md, q['choix'][i]) for i in perm] if q['type'] == 'qcm' else ['Vrai', 'Faux']}
    return jsonify(card=card, progress=_progress(data, pts))


@bp.route('/api/scroll/<subject>/answer', methods=['POST'])
@login_required
def scroll_answer(subject):
    data = get_parcours(subject)
    body = request.get_json(silent=True) or {}
    try:
        idx, choice = int(body.get('key')), int(body.get('choice'))
        q = data['quiz'][idx]
    except (TypeError, ValueError, IndexError):
        return jsonify(error='question inconnue'), 400
    good = q['bonne'] if q['type'] == 'qcm' else (0 if q['bonne'] else 1)  # vf: choice 0 = Vrai
    sub, key, perm = session.get('scroll_perm') or [None, None, None]
    if q['type'] == 'qcm':  # choice is a position on screen: map it back to the authored index
        if (sub, key) != (subject, str(idx)) or not 0 <= choice < len(perm):
            return jsonify(error='question expirée, recharge la page'), 400
        choice, good = perm[choice], perm.index(good)
        ok = choice == q['bonne']
    else:
        ok = choice == good
    uid = session['uid']
    with db() as conn:
        conn.execute('INSERT INTO scroll_log (account_id, subject, kind, key, notion, ok) VALUES (?, ?, ?, ?, ?, ?)',
                     (uid, subject, 'q', str(idx), q['notion'], int(ok)))
        conn.execute('''INSERT INTO scroll_progress (account_id, subject, pts) VALUES (?, ?, ?)
                        ON CONFLICT(account_id, subject) DO UPDATE SET pts = MAX(0, pts + ?)''',
                     (uid, subject, int(ok), 1 if ok else -1))
        pts = _pts(conn, uid, subject)
    return jsonify(ok=ok, bonne=good, progress=_progress(data, pts))
