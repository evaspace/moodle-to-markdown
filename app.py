import hmac
import json
import logging
import os
import random
import re
import sqlite3
from contextlib import contextmanager
from functools import wraps

from flask import Flask, Response, jsonify, render_template, request, send_from_directory

from init_db import DB_PATH, init_db

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD')
if not ADMIN_PASSWORD:
    logger.warning("ADMIN_PASSWORD non défini : /admin est ouvert à tout le monde")

app = Flask(__name__)
init_db()

# Auto-seed if database is empty
try:
    from seed_data import seed
    with sqlite3.connect(DB_PATH) as _conn:
        _count = _conn.execute("SELECT count(*) FROM card").fetchone()[0]
        if _count == 0:
            logger.info("Base de données vide : injection des cartes initiales...")
            seed(DB_PATH)
except Exception as e:
    logger.warning(f"Auto-seed check: {e}")


@contextmanager
def db():
    conn = sqlite3.connect(DB_PATH, timeout=10)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if ADMIN_PASSWORD:
            auth = request.authorization
            if not auth or not hmac.compare_digest((auth.password or ''), ADMIN_PASSWORD):
                return Response('Authentification requise', 401,
                                {'WWW-Authenticate': 'Basic realm="admin"'})
        return f(*args, **kwargs)
    return wrapper


# ---------------------------------------------------------------- ADMIN ----
TRUE_WORDS = {'vrai', 'true', 't', 'v', '1'}
FALSE_WORDS = {'faux', 'false', 'f', '0'}
SEP_RE = re.compile(r'^\s*---+\s*$', re.M)
CHOICE_RE = re.compile(r'^C\d*\s*:\s*(.*)$', re.I)
TYPE_RE = re.compile(r'^\[(QCM|TF)\]\s*(.*)$', re.I | re.S)


def parse_blocks(raw):
    cards, errors = [], []
    cat, sub = None, 'Général'
    for n, block in enumerate(SEP_RE.split(raw), 1):
        lines = [l.strip() for l in block.splitlines() if l.strip()]
        if not lines:
            continue

        ctype, front, back, choices, tf, target = 'COURSE', [], [], [], None, None
        had_cat = False
        for s in lines:
            up = s.upper()
            if up.startswith('CAT:'):
                name, _, subname = s[4:].partition('/')
                cat, sub = (name.strip() or None), (subname.strip() or 'Général')
                had_cat, target = True, None
            elif up.startswith('Q:'):
                q = s[2:].strip()
                m = TYPE_RE.match(q)
                if m:
                    ctype, q = m.group(1).upper(), m.group(2).strip()
                front.append(q)
                target = front
            elif up.startswith('R:'):
                back.append(s[2:].strip())
                target = back
            elif up.startswith('A:') and ctype == 'TF':
                v = s[2:].strip().lower()
                tf = True if v in TRUE_WORDS else False if v in FALSE_WORDS else None
                target = None
            elif ctype == 'QCM' and (m := CHOICE_RE.match(s)):
                text = m.group(1)
                ok = bool(re.search(r'\[x\]', text, re.I))
                choices.append({'text': re.sub(r'\[x\]', '', text, flags=re.I).strip(), 'correct': ok})
                target = None
            elif target is not None:
                target.append(s)

        front_txt = '\n'.join(front).strip()
        if not front_txt:
            if not had_cat:
                errors.append(f"Bloc {n} : pas de ligne Q:")
            continue

        if ctype == 'QCM':
            if len(choices) < 2 or not any(c['correct'] for c in choices):
                errors.append(f"Bloc {n} : QCM invalide (≥ 2 choix dont au moins un [X])")
                continue
            payload = {'choices': choices}
        elif ctype == 'TF':
            if tf is None:
                errors.append(f"Bloc {n} : TF sans ligne A: (vrai/faux)")
                continue
            payload = {'correct': tf}
        else:
            payload = {}

        cards.append({'type': ctype, 'front': front_txt, 'back': '\n'.join(back).strip(),
                      'payload': json.dumps(payload), 'cat': cat, 'sub': sub})
    return cards, errors


def get_subcategory(conn, cat, sub):
    conn.execute("INSERT OR IGNORE INTO category (name) VALUES (?)", (cat,))
    cat_id = conn.execute("SELECT id FROM category WHERE name = ?", (cat,)).fetchone()['id']
    row = conn.execute("SELECT id FROM subcategory WHERE category_id = ? AND name = ?",
                       (cat_id, sub)).fetchone()
    if row:
        return row['id']
    return conn.execute("INSERT INTO subcategory (category_id, name) VALUES (?, ?)",
                        (cat_id, sub)).lastrowid


@app.route('/admin', methods=['GET', 'POST'])
@admin_required
def admin():
    result = None
    if request.method == 'POST':
        cards, errors = parse_blocks(request.form.get('raw_text', ''))
        inserted = duplicates = 0
        if cards:
            with db() as conn:
                cache = {}
                for c in cards:
                    if conn.execute("SELECT 1 FROM card WHERE type = ? AND front = ?",
                                    (c['type'], c['front'])).fetchone():
                        duplicates += 1
                        continue
                    sub_id = None
                    if c['cat']:
                        key = (c['cat'], c['sub'])
                        if key not in cache:
                            cache[key] = get_subcategory(conn, *key)
                        sub_id = cache[key]
                    conn.execute(
                        "INSERT INTO card (subcategory_id, type, front, back, payload, status) "
                        "VALUES (?, ?, ?, ?, ?, 0)",
                        (sub_id, c['type'], c['front'], c['back'], c['payload']))
                    inserted += 1
        result = {'inserted': inserted, 'duplicates': duplicates, 'errors': errors}
    return render_template('admin.html', result=result)


# ------------------------------------------------------------------ API ----
def fetch_batch(conn, cat=None, sub=None, exclude=None):
    exclude = exclude or []
    cond = 'c.status = 0'
    params = []
    join = ''
    
    if sub:
        join = 'JOIN subcategory sc ON sc.id = c.subcategory_id'
        cond += ' AND sc.id = ?'
        params.append(sub)
    elif cat:
        join = 'JOIN subcategory sc ON sc.id = c.subcategory_id'
        cond += ' AND sc.category_id = ?'
        params.append(cat)
        
    if exclude:
        cond += f" AND c.id NOT IN ({','.join('?' * len(exclude))})"
        params += exclude
        
    base = f"""
        SELECT c.id, c.type, c.front, c.back, c.payload,
               sc.name AS subcategory_name, cat.name AS category_name,
               (SELECT 1 FROM favorite f WHERE f.card_id = c.id LIMIT 1) AS is_favorite
        FROM card c
        LEFT JOIN subcategory sc ON sc.id = c.subcategory_id
        LEFT JOIN category cat ON cat.id = sc.category_id
        WHERE {cond}
    """

    # Spaced repetition: Cartes dont la DERNIÈRE réponse était fausse
    failed_rows = conn.execute(base + '''
        AND c.id IN (
            SELECT s.card_id FROM session_log s
            WHERE s.is_correct = 0
              AND s.id = (SELECT MAX(s2.id) FROM session_log s2
                          WHERE s2.card_id = s.card_id AND s2.is_correct IS NOT NULL)
        )
        ORDER BY RANDOM() LIMIT 2''', params).fetchall()
    got = [r['id'] for r in failed_rows]

    def rnd(ctype, limit):
        extra, p = '', list(params)
        if got:
            extra = f" AND c.id NOT IN ({','.join('?' * len(got))})"
            p += got
        return conn.execute(base + extra + ' AND c.type = ? ORDER BY RANDOM() LIMIT ?',
                            p + [ctype, limit]).fetchall()

    rows = list(failed_rows) + rnd('COURSE', 4) + rnd('QCM', 3) + rnd('TF', 3)
    
    # Si la combinaison spécifique est vide mais qu'il reste des cartes dans le filtre
    if not rows:
        rows = conn.execute(base + ' ORDER BY RANDOM() LIMIT 8', params).fetchall()
        
    batch = [dict(r) for r in rows]
    random.shuffle(batch)
    for r in batch:
        r['payload'] = json.loads(r['payload']) if r['payload'] else {}
        r['is_favorite'] = bool(r.get('is_favorite'))
    return batch


@app.route('/robots.txt')
def robots():
    return send_from_directory(app.static_folder, 'robots.txt', mimetype='text/plain')


@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(app.static_folder, 'sitemap.xml', mimetype='application/xml')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/categories')
def get_categories():
    with db() as conn:
        cats = conn.execute('''
            SELECT cat.id, cat.name, COUNT(c.id) AS n
            FROM category cat
            JOIN subcategory sc ON sc.category_id = cat.id
            JOIN card c ON c.subcategory_id = sc.id
            WHERE c.status = 0
            GROUP BY cat.id ORDER BY cat.name''').fetchall()
        
        result = []
        for cat in cats:
            subs = conn.execute('''
                SELECT sc.id, sc.name, COUNT(c.id) AS n
                FROM subcategory sc
                JOIN card c ON c.subcategory_id = sc.id
                WHERE sc.category_id = ? AND c.status = 0
                GROUP BY sc.id ORDER BY sc.name''', (cat['id'],)).fetchall()
            result.append({
                'id': cat['id'],
                'name': cat['name'],
                'n': cat['n'],
                'subcategories': [dict(s) for s in subs]
            })
    return jsonify(result)


@app.route('/api/cards')
def get_cards():
    cat = request.args.get('cat', type=int)
    sub = request.args.get('sub', type=int)
    exclude = [int(x) for x in request.args.get('exclude', '').split(',') if x.strip().isdigit()][:2000]
    with db() as conn:
        batch = fetch_batch(conn, cat=cat, sub=sub, exclude=exclude)
        if not batch and exclude:
            # When cycling, try to get fresh batch but frontend will filter dups
            batch = fetch_batch(conn, cat=cat, sub=sub, exclude=[])
    return jsonify(batch)


@app.route('/api/search')
def search_cards():
    """Recherche rapide : catégories + cartes par texte (front/back).

    Paramètres :
      q : texte de recherche (minimum 2 caractères)
      limit : max résultats de cartes (default 20)

    Retourne :
      { categories: [...], cards: [...] }
    """
    q = request.args.get('q', '').strip()
    if len(q) < 2:
        return jsonify({"categories": [], "cards": []})

    limit = request.args.get('limit', 20, type=int)
    pattern = '%' + q.lower() + '%'

    with db() as conn:
        cat_rows = conn.execute('''
            SELECT cat.id, cat.name, COUNT(c.id) AS n
            FROM category cat
            JOIN subcategory sc ON sc.category_id = cat.id
            JOIN card c ON c.subcategory_id = sc.id
            WHERE c.status = 0
              AND (LOWER(cat.name) LIKE ? OR LOWER(sc.name) LIKE ?)
            GROUP BY cat.id ORDER BY cat.name LIMIT 10
        ''', (pattern, pattern)).fetchall()

        card_rows = conn.execute('''
            SELECT c.id, c.type, c.front, c.back, c.payload,
                   cat.name AS category_name, sc.name AS subcategory_name
            FROM card c
            JOIN subcategory sc ON sc.id = c.subcategory_id
            JOIN category cat ON cat.id = sc.category_id
            WHERE c.status = 0
              AND (LOWER(c.front) LIKE ? OR LOWER(c.back) LIKE ?)
            ORDER BY c.type, RANDOM()
            LIMIT ?
        ''', (pattern, pattern, limit)).fetchall()

    categories = [{"id": r["id"], "name": r["name"], "n": r["n"]} for r in cat_rows]
    cards = [{
        "id": r["id"],
        "type": r["type"],
        "front": r["front"],
        "back": r["back"],
        "payload": r["payload"],
        "category_name": r["category_name"],
        "subcategory_name": r["subcategory_name"]
    } for r in card_rows]

    return jsonify({"categories": categories, "cards": cards})


@app.route('/api/user_state')
def get_user_state():
    with db() as conn:
        state = conn.execute("SELECT streak, max_streak, level, xp FROM user_state WHERE id = 1").fetchone()
    return jsonify(dict(state) if state else {"streak": 0, "max_streak": 0, "level": 1, "xp": 0})
    with db() as conn:
        state = conn.execute("SELECT streak, max_streak, level, xp FROM user_state WHERE id = 1").fetchone()
    return jsonify(dict(state) if state else {"streak": 0, "max_streak": 0, "level": 1, "xp": 0})


@app.route('/api/log', methods=['POST'])
def log_session():
    data = request.get_json(silent=True) or {}
    try:
        card_id = int(data.get('card_id'))
    except (TypeError, ValueError):
        return jsonify(error='card_id invalide'), 400
    try:
        spent = max(0, min(int(data.get('time_spent_ms') or 0), 3_600_000))
    except (TypeError, ValueError):
        spent = 0
    ok = data.get('is_correct')
    ok = None if ok is None else int(bool(ok))

    with db() as conn:
        conn.execute("INSERT INTO session_log (card_id, time_spent_ms, is_correct) VALUES (?, ?, ?)",
                     (card_id, spent, ok))
        if ok == 1:
            conn.execute("""UPDATE user_state
                            SET streak = streak + 1,
                                xp = xp + 15,
                                level = (xp + 15) / 100 + 1,
                                max_streak = MAX(max_streak, streak + 1)
                            WHERE id = 1""")
        elif ok == 0:
            conn.execute("UPDATE user_state SET streak = 0 WHERE id = 1")
        state = conn.execute("SELECT streak, max_streak, level, xp FROM user_state WHERE id = 1").fetchone()
    return jsonify(status='ok', state=dict(state))


@app.route('/api/folders', methods=['GET', 'POST'])
def handle_folders():
    with db() as conn:
        if request.method == 'POST':
            name = ((request.get_json(silent=True) or {}).get('name') or '').strip()[:40]
            if name:
                conn.execute("INSERT OR IGNORE INTO folder (name) VALUES (?)", (name,))
        folders = conn.execute("SELECT id, name FROM folder ORDER BY name").fetchall()
    return jsonify([dict(r) for r in folders])


@app.route('/api/favorite', methods=['POST'])
def toggle_favorite():
    """Sans folder_id : bascule like/unlike. Avec folder_id : range le favori dans le dossier."""
    data = request.get_json(silent=True) or {}
    try:
        card_id = int(data.get('card_id'))
    except (TypeError, ValueError):
        return jsonify(error='card_id invalide'), 400
    folder_id = data.get('folder_id')

    with db() as conn:
        if not conn.execute("SELECT 1 FROM card WHERE id = ?", (card_id,)).fetchone():
            return jsonify(error='carte inconnue'), 404
        existing = conn.execute("SELECT id FROM favorite WHERE card_id = ?", (card_id,)).fetchone()
        if existing and folder_id is None:
            conn.execute("DELETE FROM favorite WHERE id = ?", (existing['id'],))
            action = 'removed'
        else:
            if existing:
                conn.execute("DELETE FROM favorite WHERE id = ?", (existing['id'],))
            conn.execute("INSERT INTO favorite (card_id, folder_id) VALUES (?, ?)", (card_id, folder_id))
            action = 'added'
    return jsonify(status='ok', action=action)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
