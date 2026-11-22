"""Accounts and the "Niveaux" mode (paper exercises, level up / level down).

Rules (README_OBJECTIFS.md, decision of 2026-11-14): a level is passed when every one of its
exercises (one per formula) has been answered right; a failed exercise turns red and comes back,
it turns green again when answered right. One failure drops one level and shows the formulas;
the green squares are kept, so coming back to the level only asks for the missing ones.
Content comes from parcours/*.json, built and checked by parcours/build.py.
"""
import hashlib
import json
import logging
import os
import random
import re
import secrets
import smtplib
import sqlite3
import threading
import time
from datetime import datetime, timedelta, timezone
from email.message import EmailMessage
from contextlib import contextmanager
from functools import wraps
from pathlib import Path
from urllib.parse import urlencode

from flask import Blueprint, abort, jsonify, redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash

from init_db import DB_PATH
from ratelimit import client_ip, too_many

bp = Blueprint('levels', __name__)
ROOT = Path(__file__).resolve().parent
PARCOURS_DIR = ROOT / 'parcours'
BASE_POINTS = 100          # points of a level-1 exercise done in the reference time
# Help opened before answering: code stored in exo_log.peek, points factor, extra time (share of the time limit).
HINTS = {'solution': (1, 1 / 3, 1.0),   # the formulas used in the solution
         'fiche': (2, 1 / 2, 0.5),      # the whole chapter sheet: the right formula still has to be found
         'temps': (0, 1, 1.0)}          # more time only: no division, the speed factor already lowers the points
PEEK_FACTOR = {0: 1, 1: 1 / 3, 2: 1 / 2}
SPEED_CAP = 1.5           # max speed multiplier: a higher one pays for clicking « Réussi » without checking
CALIB_POINTS = 10         # confidence bet right: « Sûr » and success, or « Au hasard » and miss
DOUBLE_ODDS = 1 / 6       # « Coup double »: chance of x2 on a success without any help
# path id -> section of annales/FORMULES.md shown in the chapter sheet
FICHE_SECTION = {'maths-s1-obm': 'OBM', 'maths-s1-dp': 'DP', 'maths-s1-apis-integrales': 'APIS (intégrales)',
                 'maths-s1-apis-suites': 'APIS (suites)', 'maths-s1-apis-edo': 'APIS (EDO)',
                 'maths-s2-apef-polynomes': 'APEF (polynômes)', 'maths-s2-apef-fonctions': 'APEF (fonctions)',
                 'maths-s2-ev': 'EV', 'maths-s2-alm': 'ALM', 'physique-s1-meca': 'Mécanique', 'physique-s2-energie': 'Mécanique',
                 'physique-s2-thermo': 'Thermodynamique', 'elec-s2-filtres': 'Études des filtres',
                 'archi-s1-numeration': 'Numération', 'archi-s2-sequentielle': 'Logique séquentielle',
                 'archi-s2-microprocesseur': 'Systèmes à microprocesseur'}
# path id -> paths whose notions it relies on; shown as links after a failed exercise
PREREQ = {'maths-s1-dp': ['maths-s1-obm'], 'maths-s1-apis-suites': ['maths-s1-obm'],
          'maths-s1-apis-edo': ['maths-s1-apis-integrales'], 'maths-s2-apef-polynomes': ['maths-s1-obm'],
          'maths-s2-apef-fonctions': ['maths-s1-apis-suites'],
          'maths-s2-ev': ['maths-s2-apef-polynomes'], 'maths-s2-alm': ['maths-s2-ev'],
          'maths-s3-asn': ['maths-s1-apis-suites', 'maths-s2-apef-fonctions'],
          'maths-s3-pse': ['maths-s1-dp', 'maths-s3-asn'],
          'maths-s3-al': ['maths-s2-ev', 'maths-s2-alm'],
          'physique-s3-quantique': ['physique-s1-meca', 'physique-s2-energie'],
          'physique-s3-em': ['physique-s2-em', 'maths-s1-apis-integrales'],
          'electronique-s3-transistors': ['elec-s1-circuits', 'elec-s2-diodes'],
          'algo-s3-hachage': ['algo-s1-taa'],
          'algo-s3-arbres': ['algo-s2-abg'],
          'algo-s3-graphes': ['algo-s1-python', 'algo-s1-taa', 'algo-s2-abg'],
          'algo-s3-thlr': ['algo-s1-taa', 'maths-s1-obm'],
          'archi-s3-assembleur-68000': ['archi-s1-numeration', 'archi-s2-microprocesseur']}
TIMEOUT_BONUS = 0.5        # +50 % time per timeout on the same exercise since its last success
TIMEOUT_MAX = 3.0          # at most x3
MIN_LIMIT = 180            # floor of the time limit in seconds (user, 2026-11-22: 3 min from integrals level 5 on)
MIN_SAMPLES = 5            # successful attempts needed before the users' average replaces the authored time
USERNAME_RE = re.compile(r'^[A-Za-z0-9_.-]{3,32}$')
RESET_TTL = 3600           # reset link lifetime, seconds
RESET_COOLDOWN = 300       # one reset mail per account every 5 minutes
# fixed public URL: never build the reset link from the request Host header
PUBLIC_URL = os.environ.get('PUBLIC_URL', 'https://epitadoomscrolling.pierref.eu').rstrip('/')
log = logging.getLogger(__name__)

SCHEMA = '''
    CREATE TABLE IF NOT EXISTS account (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE COLLATE NOCASE,
        pw_hash TEXT NOT NULL,
        email TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE TABLE IF NOT EXISTS level_progress (
        account_id INTEGER NOT NULL,
        subject TEXT NOT NULL,
        level INTEGER NOT NULL DEFAULT 1,
        streak INTEGER NOT NULL DEFAULT 0,
        best INTEGER NOT NULL DEFAULT 0,      -- highest level passed (0 = none)
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (account_id, subject),
        FOREIGN KEY(account_id) REFERENCES account(id)
    );
    CREATE TABLE IF NOT EXISTS exo_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_id INTEGER NOT NULL,
        subject TEXT NOT NULL,
        level INTEGER NOT NULL,
        exo_id TEXT NOT NULL,
        ok INTEGER NOT NULL,
        secs INTEGER,
        peek INTEGER NOT NULL DEFAULT 0,
        points INTEGER NOT NULL DEFAULT 0,
        practice INTEGER NOT NULL DEFAULT 0,
        timeout INTEGER NOT NULL DEFAULT 0,  -- failed because the countdown ran out
        at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE INDEX IF NOT EXISTS idx_exo_log ON exo_log(account_id, subject, level);
    CREATE TABLE IF NOT EXISTS event_log (     -- what exo_log does not hold: skips, helps, AI copies, level changes
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_id INTEGER NOT NULL,
        kind TEXT NOT NULL,
        subject TEXT,
        level INTEGER,
        exo_id TEXT,
        at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE INDEX IF NOT EXISTS idx_event_log ON event_log(account_id, at);
    CREATE TABLE IF NOT EXISTS prestige (     -- times the user restarted a path from scratch
        account_id INTEGER NOT NULL,
        subject TEXT NOT NULL,
        n INTEGER NOT NULL DEFAULT 0,
        PRIMARY KEY (account_id, subject)
    );
    CREATE TABLE IF NOT EXISTS password_reset (
        token_hash TEXT PRIMARY KEY,          -- sha256 of the token sent by e-mail
        account_id INTEGER NOT NULL,
        expires REAL NOT NULL,
        used INTEGER NOT NULL DEFAULT 0,
        FOREIGN KEY(account_id) REFERENCES account(id)
    );
'''


def init_levels_db(path=DB_PATH):
    with sqlite3.connect(path) as conn:
        conn.executescript(SCHEMA)
        cols = {r[1] for r in conn.execute('PRAGMA table_info(exo_log)')}
        for col, decl in (('secs', 'INTEGER'), ('peek', 'INTEGER NOT NULL DEFAULT 0'),
                          ('points', 'INTEGER NOT NULL DEFAULT 0'), ('practice', 'INTEGER NOT NULL DEFAULT 0'),
                          ('timeout', 'INTEGER NOT NULL DEFAULT 0'), ('review', 'INTEGER NOT NULL DEFAULT 0'),
                          ('conf', 'INTEGER')):  # confidence bet: NULL none, 0 au hasard, 1 moyen, 2 sûr
            if col not in cols:
                conn.execute(f'ALTER TABLE exo_log ADD COLUMN {col} {decl}')
        if 'leaderboard' not in {r[1] for r in conn.execute('PRAGMA table_info(account)')}:
            # opt-in: an account shows in /classement only once its owner ticks the box
            conn.execute('ALTER TABLE account ADD COLUMN leaderboard INTEGER NOT NULL DEFAULT 0')
        if 'board_ban' not in {r[1] for r in conn.execute('PRAGMA table_info(account)')}:
            # set by the admin from the « Triche possible » list of /admin/stats
            conn.execute('ALTER TABLE account ADD COLUMN board_ban INTEGER NOT NULL DEFAULT 0')
        if 'pari' not in {r[1] for r in conn.execute('PRAGMA table_info(account)')}:
            # opt-in confidence bet before the correction (an extra tap: off by default)
            conn.execute('ALTER TABLE account ADD COLUMN pari INTEGER NOT NULL DEFAULT 0')
        # abandoned paths: their rows move here, out of every stat, review and board (kept, never shown)
        for t in ('exo_log', 'event_log'):
            conn.execute(f'CREATE TABLE IF NOT EXISTS {t}_archive AS SELECT * FROM {t} WHERE 0')
            have = {r[1] for r in conn.execute(f'PRAGMA table_info({t}_archive)')}
            for (col,) in conn.execute('SELECT name FROM pragma_table_info(?)', (t,)).fetchall():
                if col not in have:  # a column added to the live table later
                    conn.execute(f'ALTER TABLE {t}_archive ADD COLUMN {col}')


def log_event(conn, uid, kind, subject=None, level=None, exo_id=None):
    conn.execute('INSERT INTO event_log (account_id, kind, subject, level, exo_id) VALUES (?, ?, ?, ?, ?)',
                 (uid, kind, subject, level, exo_id))


def secret_key():
    """SECRET_KEY env var, else a key file shared by all gunicorn workers."""
    if os.environ.get('SECRET_KEY'):
        return os.environ['SECRET_KEY']
    path = ROOT / '.secret_key'
    try:
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd, 'w') as f:
            f.write(secrets.token_hex(32))
    except FileExistsError:
        pass
    return path.read_text().strip()


# ------------------------------------------------------------ content ----
_cache = {}


def load_parcours():
    """All level paths, reloaded when a JSON file changes. Each exercise and variant gets its
    `origine` (TD, exam or written for the site) from parcours/origines.json (tools/sources.py)."""
    out = {}
    orig_path = PARCOURS_DIR / 'origines.json'
    orig_mtime = orig_path.stat().st_mtime if orig_path.exists() else None
    for p in sorted(PARCOURS_DIR.glob('*.json')):
        if p.name in ('syllabus.json', 'origines.json'):  # registry and origins, not level paths
            continue
        mtime = (p.stat().st_mtime, orig_mtime)
        if _cache.get(p.name, (None,))[0] != mtime:
            data = json.loads(p.read_text(encoding='utf-8'))
            origins = json.loads(orig_path.read_text(encoding='utf-8')).get(data['subject']['id'], {}) if orig_mtime else {}
            for lvl in data['levels']:
                for exo in lvl['exos']:
                    o = origins.get(exo['id'], [])
                    for i, x in enumerate([exo] + exo.get('variants', [])):
                        if i < len(o):
                            x['origine'] = o[i]
            _cache[p.name] = (mtime, data)
        data = _cache[p.name][1]
        out[data['subject']['id']] = data
    return out


def get_parcours(subject):
    data = load_parcours().get(subject)
    if not data:
        abort(404)
    return data


# ---------------------------------------------------------- game rules ----
def apply_result(level, best, ok, all_green, n_levels, prev_ko=True):
    """Return the new (level, best, event) after one answered exercise of the current level.
    A miss only drops a level when the previous answer on this level was also a miss (`prev_ko`):
    one bad evening must not send the user down a cascade of levels."""
    if not ok:
        if not prev_ko:
            return level, best, 'warn'
        return max(1, level - 1), best, 'down' if level > 1 else 'retry'
    if not all_green:
        return level, best, 'progress'
    best = max(best, level)
    if level >= n_levels:
        return level, best, 'finished'
    return level + 1, best, 'up'


def pick_exo(exos, status, last_id=None, attempts=0):
    """Next exercise: never done first (list order), then failed ones (not the one just failed),
    then, once all are green, a rotation for practice."""
    todo = [e for e in exos if status.get(e['id']) is None]
    red = [e for e in exos if status.get(e['id']) == 0 and e['id'] != last_id]
    if todo or red:
        return (todo or red)[0]
    others = [e for e in exos if e['id'] != last_id] or exos
    return others[attempts % len(others)]


def easier_level(levels, n):
    """« Trop dur, passer »: the highest level below n that shares a notion with level n,
    else the level just below (n itself at level 1)."""
    notions = set(levels[n - 1]['notions'])
    shared = [k for k in range(n - 1, 0, -1) if notions & set(levels[k - 1]['notions'])]
    return shared[0] if shared else max(1, n - 1)


REVIEW_EVERY = 5 # in the grind, one due review is slipped in after this many answers (never blocks)
REVIEW_DAYS = (1, 3, 7)  # a failed exercise comes back at D+1, then D+3, then D+7 after each success


def due_reviews(attempts, today):
    """Spaced review. attempts: (key, ok, day) oldest first, day = local date.
    A miss (re)starts the cycle; each success on a later day than the previous step moves it one
    interval further; after len(REVIEW_DAYS) successes the key leaves the queue.
    Returns {key: due_day} for the keys due on or before `today`."""
    state = {}  # key -> (anchor day, successes since the last miss)
    for key, ok, day in attempts:
        if not ok:
            state[key] = (day, 0)
        elif key in state and day > state[key][0]:
            state[key] = (day, state[key][1] + 1)
    due = {}
    for key, (anchor, k) in state.items():
        if k < len(REVIEW_DAYS):
            when = anchor + timedelta(days=REVIEW_DAYS[k])
            if when <= today:
                due[key] = when
    return due


def review_queue(conn, uid, today):
    """Exercises due for review today, oldest due first: [(subject, level, exo_id)]."""
    from zoneinfo import ZoneInfo
    tz = ZoneInfo(TZ)
    rows = conn.execute('SELECT subject, level, exo_id, ok, at FROM exo_log WHERE account_id=? ORDER BY id', (uid,))
    attempts = [((r[0], r[1], r[2]), r[3],
                 datetime.fromisoformat(r[4]).replace(tzinfo=timezone.utc).astimezone(tz).date()) for r in rows]
    paths = load_parcours()
    due = due_reviews(attempts, today)
    known = {k: d for k, d in due.items() if k[0] in paths and 1 <= k[1] <= len(paths[k[0]]['levels'])
             and k[2] in {e['id'] for e in paths[k[0]]['levels'][k[1] - 1]['exos']}}
    return sorted(known, key=lambda k: known[k])


def variant(exo, tries):
    """Version shown after `tries` previous attempts: the base, then each variant in turn (other numbers)."""
    versions = [exo] + [{**exo, 'src': None, **v} for v in exo.get('variants', [])]
    return versions[tries % len(versions)]


def score(ok, secs, ref, peek, level):
    """Points for one exercise: faster than the reference time = more points (x0.5 to SPEED_CAP),
    0 if failed. `peek` is the help opened before answering: 0 none, 1 (or True) formulas of the
    solution = a third, 2 chapter sheet only = half."""
    if not ok:
        return 0
    speed = min(SPEED_CAP, max(0.5, ref / max(secs, 1)))
    pts = BASE_POINTS * (1 + (level - 1) / 4) * speed
    return round(pts * PEEK_FACTOR[int(peek)])


def hint_code(hints):
    """exo_log.peek value for the helps opened: the strongest one counts."""
    return 1 if 'solution' in hints else 2 if 'fiche' in hints else 0


def hint_limit(limit, hints):
    """Time limit once the helps are opened: each one adds its share of the base limit, once."""
    return round(limit * (1 + sum(HINTS[h][2] for h in set(hints))))


def time_bonus(conn, uid, subject, level, exo_id):
    """Time multiplier: each timeout on this exercise since its last success gives +50 %, up to x3,
    so a slow user still finishes (fewer points) instead of always failing."""
    k = 0
    for ok, timeout in conn.execute('SELECT ok, timeout FROM exo_log WHERE account_id=? AND subject=? AND level=? '
                                    'AND exo_id=? ORDER BY id DESC', (uid, subject, level, exo_id)):
        if ok:
            break
        k += timeout
    return min(TIMEOUT_MAX, 1 + TIMEOUT_BONUS * k)


def timing(conn, subject, lvl, exo):
    """(reference seconds, time limit seconds) for one exercise.

    Reference = users' average time on successful attempts of this level (one average per level,
    so it fills up fast), scaled by the exercise's authored length relative to the level's.
    Before MIN_SAMPLES attempts: the authored length is the limit and 60 % of it the reference.
    The limit never drops under MIN_LIMIT (or the authored length if shorter): a few fast users
    must not leave 1 min to solve a 5 min exercise."""
    authored = int(exo.get('duree', 5)) * 60
    row = conn.execute('SELECT AVG(secs), COUNT(*) FROM exo_log WHERE subject=? AND level=? AND ok=1 AND secs > 0',
                       (subject, lvl['n'])).fetchone()
    if row[1] < MIN_SAMPLES:
        return round(authored * 0.6), authored
    level_mean = sum(int(e.get('duree', 5)) * 60 for e in lvl['exos']) / len(lvl['exos'])
    ref = row[0] * authored / level_mean
    return round(ref), int(min(max(ref * 1.6, min(authored, MIN_LIMIT)), 1800))


COMBO_GAP = 30 * 60  # a pause longer than this (seconds) ends the combo


def combo(rows):
    """Combo: +1 per success, a miss resets it to 0 (user choice 2026-11-22, was halved before).
    A pause longer than COMBO_GAP starts a new run.
    rows = (ok, unix time) newest first, across all paths. Computed by the server: survives reloads."""
    run = []
    for ok, at in rows:
        if run and run[-1][1] - at > COMBO_GAP:
            break
        run.append((ok, at))
    n = 0
    for ok, _ in reversed(run):
        n = n + 1 if ok else 0
    return n


def current_combo(conn, uid):
    rows = conn.execute("SELECT ok, CAST(strftime('%s', at) AS INTEGER) FROM exo_log WHERE account_id=? "
                        'ORDER BY id DESC LIMIT 200', (uid,)).fetchall()
    if rows and time.time() - rows[0][1] > COMBO_GAP:
        return 0
    return combo(rows)


def xp(conn, uid):
    return conn.execute('SELECT COALESCE(SUM(points), 0) FROM exo_log WHERE account_id=?', (uid,)).fetchone()[0]


def percent(best, n_levels):
    return round(100 * best / n_levels) if n_levels else 0


# ------------------------------------------------------------- helpers ----
@contextmanager
def db():
    conn = sqlite3.connect(DB_PATH, timeout=10)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not session.get('uid'):
            if request.path.startswith('/api/'):
                return jsonify(error='connexion requise'), 401
            return redirect('/compte?next=' + request.path)
        return f(*args, **kwargs)
    return wrapper


def prestige(conn, uid, subject):
    row = conn.execute('SELECT n FROM prestige WHERE account_id=? AND subject=?', (uid, subject)).fetchone()
    return row[0] if row else 0


def abandon_path(conn, uid, subject, restart):
    """Drop a path: its history leaves stats, reviews and boards; restart=True adds one prestige."""
    for t in ('exo_log', 'event_log'):
        cols = ', '.join(r[1] for r in conn.execute(f'PRAGMA table_info({t})'))
        conn.execute(f'INSERT INTO {t}_archive ({cols}) SELECT {cols} FROM {t} WHERE account_id=? AND subject=?',
                     (uid, subject))
        conn.execute(f'DELETE FROM {t} WHERE account_id=? AND subject=?', (uid, subject))
    conn.execute('DELETE FROM level_progress WHERE account_id=? AND subject=?', (uid, subject))
    if restart:
        conn.execute('INSERT INTO prestige (account_id, subject, n) VALUES (?, ?, 1) '
                     'ON CONFLICT(account_id, subject) DO UPDATE SET n = n + 1', (uid, subject))


def progress(conn, uid, subject):
    row = conn.execute('SELECT level, streak, best FROM level_progress WHERE account_id=? AND subject=?',
                       (uid, subject)).fetchone()
    return (row['level'], row['streak'], row['best']) if row else (1, 0, 0)


def statuses(conn, uid, subject):
    """{(level, exo_id): last result} for this user: 1 green, 0 red; absent = never done."""
    out = {}
    for r in conn.execute('SELECT level, exo_id, ok FROM exo_log WHERE account_id=? AND subject=? ORDER BY id',
                          (uid, subject)):
        out[(r['level'], r['exo_id'])] = r['ok']
    return out


def level_status(st, lvl):
    return {e['id']: st.get((lvl['n'], e['id'])) for e in lvl['exos']}


def total_percent(st, data):
    """Share of all the exercises of the path currently green (the 'total' progress bar)."""
    total = sum(len(lvl['exos']) for lvl in data['levels'])
    green = sum(1 for lvl in data['levels'] for e in lvl['exos'] if st.get((lvl['n'], e['id'])) == 1)
    return round(100 * green / total) if total else 0


def squares(lvl, status):
    return [{'id': e['id'], 'state': {1: 'ok', 0: 'ko'}.get(status[e['id']], '')} for e in lvl['exos']]


# ------------------------------------------------------------ accounts ----
@bp.route('/compte')
def account_page():
    email, board = None, 0
    if session.get('uid'):
        with db() as conn:
            row = conn.execute('SELECT email, leaderboard FROM account WHERE id=?', (session['uid'],)).fetchone()
            email, board = (row['email'], row['leaderboard']) if row else (None, 0)
    return render_template('compte.html', username=session.get('username'), email=email, board=board,
                           reset_token=request.args.get('reset', '')[:100])


def _credentials():
    data = request.get_json(silent=True) or {}
    return (data.get('username') or '').strip(), data.get('password') or '', (data.get('email') or '').strip()


@bp.route('/api/register', methods=['POST'])
def register():
    username, password, email = _credentials()
    if too_many(('register', client_ip()), 30, 3600):  # generous: a whole class shares the school IP
        return jsonify(error='Trop de comptes créés depuis cette connexion, réessaie plus tard'), 429
    if not USERNAME_RE.match(username):
        return jsonify(error='Identifiant : 3 à 32 caractères, lettres, chiffres, . _ -'), 400
    if not 6 <= len(password) <= 200:
        return jsonify(error='Mot de passe : 6 caractères minimum'), 400
    if email and (len(email) > 200 or '@' not in email):
        return jsonify(error='E-mail invalide'), 400
    with db() as conn:
        try:
            uid = conn.execute('INSERT INTO account (username, pw_hash, email) VALUES (?, ?, ?)',
                               (username, generate_password_hash(password), email or None)).lastrowid
        except sqlite3.IntegrityError:
            return jsonify(error='Identifiant déjà pris'), 409
    session.clear()
    session.update(uid=uid, username=username)
    session.permanent = True
    return jsonify(ok=True, username=username)


@bp.route('/api/login', methods=['POST'])
def login():
    username, password, _ = _credentials()
    user_key, ip_key = ('login-fail', username.lower()), ('login-fail-ip', client_ip())
    if too_many(user_key, 10, 900, hit=False) or too_many(ip_key, 50, 900, hit=False):
        return jsonify(error='Trop de tentatives, réessaie dans 15 minutes'), 429
    with db() as conn:
        row = conn.execute('SELECT id, username, pw_hash FROM account WHERE username=?', (username,)).fetchone()
    if not row or not check_password_hash(row['pw_hash'], password):
        too_many(user_key, 10, 900)
        too_many(ip_key, 50, 900)
        return jsonify(error='Identifiant ou mot de passe incorrect'), 401
    session.clear()
    session.update(uid=row['id'], username=row['username'])
    session.permanent = True
    return jsonify(ok=True, username=row['username'])


@bp.route('/api/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify(ok=True)


@bp.route('/api/email', methods=['POST'])
@login_required
def set_email():
    email = ((request.get_json(silent=True) or {}).get('email') or '').strip()
    if email and (len(email) > 200 or '@' not in email):
        return jsonify(error='E-mail invalide'), 400
    with db() as conn:
        conn.execute('UPDATE account SET email=? WHERE id=?', (email or None, session['uid']))
    return jsonify(ok=True)


def _token_hash(token):
    return hashlib.sha256(token.encode()).hexdigest()


def send_mail(to, subject, body):
    """Plain-text mail from morgan@pierref.eu (OVH SMTP, credentials from the environment)."""
    user, password = os.environ.get('MAIL_USERNAME'), os.environ.get('MAIL_PASSWORD')
    if not (user and password):
        log.warning('MAIL_USERNAME/MAIL_PASSWORD not set: reset mail to %s not sent', to)
        return False
    msg = EmailMessage()
    msg['From'], msg['To'], msg['Subject'] = f'Epita Doomscrolling <{user}>', to, subject
    msg.set_content(body)
    try:
        with smtplib.SMTP(os.environ.get('MAIL_SERVER', 'ssl0.ovh.net'), int(os.environ.get('MAIL_PORT', 587)),
                          timeout=15) as smtp:
            smtp.starttls()
            smtp.login(user, password)
            smtp.send_message(msg)
        return True
    except (OSError, smtplib.SMTPException) as e:
        log.error('reset mail to %s failed: %s', to, e)
        return False


@bp.route('/api/reset/request', methods=['POST'])
def reset_request():
    """Same answer whether the account exists or not (no account enumeration)."""
    who = ((request.get_json(silent=True) or {}).get('who') or '').strip()[:200]
    if too_many(('reset', client_ip()), 10, 3600):
        return jsonify(error='Trop de demandes, réessaie dans une heure'), 429
    if who:
        with db() as conn:
            row = conn.execute('SELECT id, username, email FROM account WHERE (username=? OR email=? COLLATE NOCASE) '
                               'AND email IS NOT NULL', (who, who)).fetchone()
            recent = row and conn.execute('SELECT 1 FROM password_reset WHERE account_id=? AND expires > ?',
                                          (row['id'], time.time() + RESET_TTL - RESET_COOLDOWN)).fetchone()
            if row and not recent:
                token = secrets.token_urlsafe(32)
                conn.execute('INSERT INTO password_reset (token_hash, account_id, expires) VALUES (?, ?, ?)',
                             (_token_hash(token), row['id'], time.time() + RESET_TTL))
                body = (f"Bonjour {row['username']},\n\n"
                        f"Pour choisir un nouveau mot de passe, ouvre ce lien (valable 1 heure) :\n"
                        f"{PUBLIC_URL}/compte?reset={token}\n\n"
                        "Si tu n'as rien demandé, ignore ce message : ton mot de passe ne change pas.\n")
                threading.Thread(target=send_mail, args=(row['email'], 'Nouveau mot de passe', body),
                                 daemon=True).start()
    return jsonify(ok=True, message="Si ce compte a un e-mail, un lien vient d'y être envoyé.")


@bp.route('/api/reset/confirm', methods=['POST'])
def reset_confirm():
    data = request.get_json(silent=True) or {}
    token, password = str(data.get('token') or ''), data.get('password') or ''
    if not 6 <= len(password) <= 200:
        return jsonify(error='Mot de passe : 6 caractères minimum'), 400
    with db() as conn:
        row = conn.execute('SELECT r.account_id, a.username FROM password_reset r JOIN account a ON a.id = r.account_id '
                           'WHERE r.token_hash=? AND r.used=0 AND r.expires > ?',
                           (_token_hash(token), time.time())).fetchone()
        if not row:
            return jsonify(error='Lien expiré ou déjà utilisé : redemande un e-mail'), 400
        conn.execute('UPDATE password_reset SET used=1 WHERE account_id=?', (row['account_id'],))
        conn.execute('UPDATE account SET pw_hash=? WHERE id=?', (generate_password_hash(password), row['account_id']))
    session.clear()
    session.update(uid=row['account_id'], username=row['username'])
    session.permanent = True
    return jsonify(ok=True, username=row['username'])


ADMIN_USERS = {u.strip().lower() for u in os.environ.get('ADMIN_USERNAMES', 'morgan.pierrefeu').split(',') if u.strip()}


def is_admin():
    return (session.get('username') or '').lower() in ADMIN_USERS


def nav_state():
    """What the navbar shows for the logged-in user: validated paper levels, points, day streak."""
    uid = session.get('uid')
    if not uid:
        return {'logged': False}
    from datetime import datetime, timedelta, timezone
    from zoneinfo import ZoneInfo
    tz = ZoneInfo(TZ)
    paths = _paths_meta()
    with db() as conn:
        best = {r['subject']: r['best'] for r in conn.execute(
            'SELECT subject, best FROM level_progress WHERE account_id=?', (uid,))}
        points = xp(conn, uid)
        fraud = all_suspects(conn).get(uid, [])
        hours = [r[0] for r in conn.execute('SELECT DISTINCT substr(at, 1, 13) FROM exo_log WHERE account_id=?', (uid,))]
    days = {datetime.fromisoformat(h + ':00:00').replace(tzinfo=timezone.utc).astimezone(tz).date() for h in hours}
    today = datetime.now(tz).date()
    day = today if today in days else today - timedelta(days=1)
    streak = 0
    while day in days:
        streak, day = streak + 1, day - timedelta(days=1)
    total = sum(len(d['levels']) for _, d in paths)
    done = sum(min(best.get(sid, 0), len(d['levels'])) for sid, d in paths)
    return {'logged': True, 'username': session['username'], 'admin': is_admin(), 'xp': points, 'streak': streak,
            'levels_done': done, 'levels_total': total, 'percent': percent(done, total),
            'fraud': fraud, 'fraud_warning': FRAUD_WARNING}


@bp.app_context_processor
def inject_nav():
    return {'nav': nav_state(), 'public_url': PUBLIC_URL}


@bp.route('/api/me')
def me():
    return jsonify({'username': None, **nav_state()})


# --------------------------------------------------------------- pages ----
def _paths_meta():
    """[(id, data)] in syllabus order."""
    return sorted(load_parcours().items(), key=lambda kv: kv[1]['subject'].get('ordre', 999))


def _filters():
    """Selection from the query string: ordre (semestre|matiere), sem, mat, ch ('' = all)."""
    a = request.args
    return {'ordre': 'matiere' if a.get('ordre') == 'matiere' else 'semestre',
            'sem': a.get('sem', ''), 'mat': a.get('mat', ''), 'ch': a.get('ch', '')}


def select_paths(paths, f):
    """Paths matching the selection; a chapter outside the chosen semester/subject is ignored."""
    out = [(sid, d) for sid, d in paths
           if (not f['sem'] or d['subject']['semestre'] == f['sem'])
           and (not f['mat'] or d['subject']['matiere'] == f['mat'])]
    one = [(sid, d) for sid, d in out if sid == f['ch']]
    return one or out


def selector(paths, f):
    """Options of the three lists, each narrowed by the lists placed before it in the chosen order."""
    sems = sorted({d['subject']['semestre'] for _, d in paths})
    mats = sorted({d['subject']['matiere'] for _, d in paths})
    if f['ordre'] == 'semestre':
        mats = sorted({d['subject']['matiere'] for _, d in paths if not f['sem'] or d['subject']['semestre'] == f['sem']})
    else:
        sems = sorted({d['subject']['semestre'] for _, d in paths if not f['mat'] or d['subject']['matiere'] == f['mat']})
    chs = [{'id': sid, 'titre': f"{d['subject']['ecue']} · {d['subject']['titre']}"}
           for sid, d in select_paths(paths, dict(f, ch=''))]
    return {'sems': sems, 'mats': mats, 'chs': chs}


@bp.route('/niveaux')
@login_required
def levels_home():
    uid, subjects, f = session['uid'], [], _filters()
    paths = _paths_meta()
    with db() as conn:
        for sid, data in select_paths(paths, f):
            level, _, best = progress(conn, uid, sid)
            n = len(data['levels'])
            st = statuses(conn, uid, sid)
            subjects.append({'id': sid, 'titre': data['subject']['titre'], 'matiere': data['subject']['matiere'],
                             'ecue': data['subject']['ecue'], 'semestre': data['subject']['semestre'],
                             'level': level, 'best': best, 'n': n, 'percent': total_percent(st, data),
                             'prestige': prestige(conn, uid, sid), 'started': bool(st),
                             'squares': squares(data['levels'][level - 1], level_status(st, data['levels'][level - 1])),
                             'levels': [{'n': l['n'], 'titre': l['titre'], 'examen': l.get('examen', False)}
                                        for l in data['levels']]})
        total_xp = xp(conn, uid)
        n_review = len(review_queue(conn, uid, _today()))
        last = {r[0]: r[1] for r in conn.execute('SELECT subject, MAX(id) FROM exo_log WHERE account_id=? GROUP BY subject',
                                                 (uid,))}
    subjects.sort(key=lambda x: -last.get(x['id'], 0))  # the path worked on last comes first (stable otherwise)
    return render_template('niveaux.html', subjects=subjects, username=session['username'], xp=total_xp,
                           f=f, sel=selector(paths, f), qs=urlencode(f), n_review=n_review,
                           reviewed=bool(request.args.get('revu')))


@bp.route('/niveaux/<subject>/abandon', methods=['POST'])
@login_required
def level_abandon(subject):
    """« Abandonner le chapitre »: recommencer (+1 prestige) or erase a misclick (no prestige)."""
    get_parcours(subject)  # 404 on an unknown path
    mode = request.form.get('mode')
    if mode not in ('recommencer', 'erreur'):
        abort(400)
    with db() as conn:
        abandon_path(conn, session['uid'], subject, mode == 'recommencer')
    return redirect('/niveaux')


@bp.route('/niveaux/melange')
@login_required
def levels_mix():
    """'Tout confondu': next exercise from a random selected path, at the user's current level there."""
    f = _filters()
    chosen = [sid for sid, _ in select_paths(_paths_meta(), f)]
    if not chosen:
        return redirect('/niveaux')
    return redirect(f'/niveaux/{random.choice(chosen)}?' + urlencode(dict(f, mix=1)))


def _today():
    from zoneinfo import ZoneInfo
    return datetime.now(ZoneInfo(TZ)).date()


@bp.route('/niveaux/revoir')
@login_required
def levels_review():
    """Next exercise due for spaced review (D+1, D+3, D+7 after a miss), whatever the path."""
    with db() as conn:
        queue = review_queue(conn, session['uid'], _today())
    if not queue:
        return redirect('/niveaux?revu=1')
    subject, n, exo_id = queue[0]
    return redirect(f'/niveaux/{subject}?' + urlencode({'n': n, 'exo': exo_id, 'revoir': 1}))


@bp.route('/niveaux/<subject>')
@login_required
def level_page(subject):
    """Current level by default; ?n=K opens level K in practice mode (does not move progress)."""
    from app import render_markdown_with_math  # same Markdown + LaTeX renderer as the course pages
    data = get_parcours(subject)
    uid, n_levels = session['uid'], len(data['levels'])
    if not request.args and session.get('grind_n', 0) >= REVIEW_EVERY:  # plain grind page: interleave a review
        with db() as conn:
            paths, mat = load_parcours(), data['subject']['matiere']
            # same subject only (another chapter is fine): a review must not pull the user out of maths
            queue = [q for q in review_queue(conn, uid, _today()) if paths[q[0]]['subject']['matiere'] == mat]
        if queue:
            session['grind_n'] = 0
            s, k, e = queue[0]
            return redirect(f'/niveaux/{s}?' + urlencode({'n': k, 'exo': e, 'revoir': 1, 'apres': subject}))
    skipped = request.args.get('facile')  # « Trop dur, passer »: nothing logged, so no penalty
    with db() as conn:
        level, _, best = progress(conn, uid, subject)
        if skipped:
            log_event(conn, uid, 'passer', subject, level, skipped[:40])
        n = easier_level(data['levels'], level) if skipped else request.args.get('n', type=int) or level
        n = min(max(1, n), n_levels)
        lvl = data['levels'][n - 1]
        st = statuses(conn, uid, subject)
        status = level_status(st, lvl)
        last = conn.execute('SELECT exo_id, (SELECT COUNT(*) FROM exo_log WHERE account_id=? AND subject=? AND level=?) '
                            'FROM exo_log WHERE account_id=? AND subject=? AND level=? ORDER BY id DESC LIMIT 1',
                            (uid, subject, n, uid, subject, n)).fetchone()
        asked = next((e for e in lvl['exos'] if e['id'] == request.args.get('exo')), None)  # review queue
        others = [e for e in lvl['exos'] if e['id'] != skipped] or lvl['exos']  # level 1: another exercise
        exo = asked or pick_exo(others, status, last[0] if last else None, last[1] if last else 0)
        tries = conn.execute('SELECT COUNT(*) FROM exo_log WHERE account_id=? AND subject=? AND level=? AND exo_id=?',
                             (uid, subject, n, exo['id'])).fetchone()[0]
        exo = variant(exo, tries)
        ref, limit = timing(conn, subject, lvl, exo)
        bonus = time_bonus(conn, uid, subject, n, exo['id'])
        limit = round(limit * bonus)  # the reference (points) does not move: slower still means fewer points
        total_xp = xp(conn, uid)
        streak_now = current_combo(conn, uid)
        pari = conn.execute('SELECT pari FROM account WHERE id=?', (uid,)).fetchone()
    # server-side clock: the time spent is measured from here, not sent by the browser
    session['exo_clock'] = [subject, n, exo['id'], time.time(), ref, limit, []]  # last: helps opened
    notions = {x['id']: x for x in data['notions']}
    md = render_markdown_with_math
    return render_template(
        'niveau.html', subject=data['subject'], lvl=lvl, n_levels=n_levels, current=level,
        best=best, practice=(n != level), percent=total_percent(st, data), xp=total_xp,
        easier=bool(skipped),
        mix=f'/niveaux/{subject}' if skipped else
            ('/niveaux/melange?' + urlencode(_filters())) if request.args.get('mix') else
            (f"/niveaux/{request.args['apres']}" if request.args.get('apres') in load_parcours() else '/niveaux/revoir')
            if request.args.get('revoir') else None,
        review=bool(request.args.get('revoir')),
        squares=squares(lvl, status), combo=streak_now, pari=bool(pari and pari[0]), calib=CALIB_POINTS,
        exo={'id': exo['id'], 'src': exo.get('src'), 'origine': exo.get('origine'), 'duree': limit, 'ref': ref, 'bonus': round((bonus - 1) * 100),
             'enonce': md(exo['enonce']), 'sol': md(exo['sol']),
             # one formula per line; the level notions stay below as course reminder
             'formules': md('\n'.join(f'- {f}' for f in exo.get('formules', '').split(' · ') if f))},
        notions=[{'titre': notions[i]['titre'], 'formule': md(notions[i]['formule']),
                  'exemple': md(notions[i]['exemple']), 'cours': md(notions[i]['cours'])}
                 for i in lvl['notions']],
        hints={k: {'div': round(1 / f), 'extra': round(limit * t)} for k, (_, f, t) in HINTS.items()},
        chapter=[{'titre': x['titre'], 'formule': md(x['formule'])} for x in data['notions']],
        fiche=next((s['html'] for s in formula_sheet() if s['titre'] == FICHE_SECTION.get(subject)), ''))


@bp.route('/api/niveaux/<subject>/hint', methods=['POST'])
@login_required
def level_hint(subject):
    """A help (chapter sheet, formulas of the solution or just more time) is opened before answering:
    recorded in the server clock, so the extra time and the reduced points do not depend on the browser."""
    kind = (request.get_json(silent=True) or {}).get('kind')
    clock = session.get('exo_clock')
    if kind not in HINTS or not clock or clock[0] != subject or len(clock) < 7:
        return jsonify(error='aide inconnue'), 400
    new = kind not in clock[6]
    if new:
        with db() as conn:
            log_event(conn, session['uid'], 'aide_' + kind, subject, clock[1], clock[2])
    session['exo_clock'] = clock[:6] + [clock[6] + [kind] if new else clock[6]]
    return jsonify(extra=round(clock[5] * HINTS[kind][2]) if new else 0, div=round(1 / HINTS[kind][1]))


@bp.route('/api/niveaux/<subject>/result', methods=['POST'])
@login_required
def level_result(subject):
    data = get_parcours(subject)
    body = request.get_json(silent=True) or {}
    n_levels, uid = len(data['levels']), session['uid']
    try:
        n = int(body.get('level'))
    except (TypeError, ValueError):
        return jsonify(error='niveau invalide'), 400
    if not 1 <= n <= n_levels:
        return jsonify(error='niveau invalide'), 400
    exo_id = str(body.get('exo_id') or '')[:40]
    if exo_id not in {e['id'] for e in data['levels'][n - 1]['exos']}:
        return jsonify(error='exercice inconnu'), 400
    ok, peek = bool(body.get('ok')), int(bool(body.get('peek')))  # browser flag: fallback if the hint call failed
    clock = session.pop('exo_clock', None)
    secs = ref = None
    timeout = False
    if clock and clock[:3] == [subject, n, exo_id]:
        secs, ref = max(1, round(time.time() - clock[3])), clock[4]
        # trusted only if the server clock agrees (5 s margin for the request)
        hints = clock[6] if len(clock) > 6 else []
        peek = hint_code(hints) or peek
        timeout = bool(body.get('timeout')) and not ok and len(clock) > 5 and secs >= hint_limit(clock[5], hints) - 5
    with db() as conn:
        level, _, best = progress(conn, uid, subject)
        review = bool(body.get('revoir'))
        practice = n != level or review  # a review miss only puts the exercise back at D+1, never demotes
        if not review:
            session['grind_n'] = session.get('grind_n', 0) + 1
        prev = conn.execute('SELECT ok FROM exo_log WHERE account_id=? AND subject=? AND level=? AND practice=0 '
                            'ORDER BY id DESC LIMIT 1', (uid, subject, n)).fetchone()
        pts = score(ok, secs, ref, peek, n) if secs else 0  # no matching page view: no points
        double = bool(pts) and not peek and random.random() < DOUBLE_ODDS
        pts *= 2 if double else 1
        conf = body.get('conf') if body.get('conf') in (0, 1, 2) else None
        calib = CALIB_POINTS if secs and (conf, ok) in ((2, True), (0, False)) else 0
        pts += calib
        conn.execute('''INSERT INTO exo_log (account_id, subject, level, exo_id, ok, secs, peek, points, practice, timeout, review, conf)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                     (uid, subject, n, exo_id, int(ok), secs, int(peek), pts, int(practice), int(timeout), int(review), conf))
        total_xp = xp(conn, uid)
        combo_now = current_combo(conn, uid)
        st = statuses(conn, uid, subject)
        status = level_status(st, data['levels'][n - 1])
        green = sum(1 for v in status.values() if v == 1)
        extra = dict(combo=combo_now, points=pts, double=double, calib=calib, conf=conf, xp=total_xp, timeout=timeout, secs=secs, ref=ref, peek=peek, green=green, total=len(status),
                     percent=total_percent(st, data))
        fraud = all_suspects(conn).get(uid)
        if fraud:
            extra['warning'] = FRAUD_WARNING + ' (' + ' · '.join(fraud) + ')'
        if not ok:
            extra['prereq'] = [{'id': p, 'titre': get_parcours(p)['subject']['titre']} for p in PREREQ.get(subject, [])]
        if practice:  # practice on another level: logged (squares change), level unchanged
            return jsonify(event='review' if review else 'practice', ok=ok, level=level, best=best, **extra)
        level, best, event = apply_result(level, best, ok, green == len(status), n_levels,
                                          prev_ko=bool(prev) and not prev['ok'])
        if event in ('up', 'down', 'finished'):
            log_event(conn, uid, 'niveau_' + event, subject, n, exo_id)
        streak = green  # column kept for compatibility: greens on the level just answered
        conn.execute('''INSERT INTO level_progress (account_id, subject, level, streak, best) VALUES (?, ?, ?, ?, ?)
                        ON CONFLICT(account_id, subject) DO UPDATE SET level=excluded.level,
                        streak=excluded.streak, best=excluded.best, updated_at=CURRENT_TIMESTAMP''',
                     (uid, subject, level, streak, best))
    return jsonify(event=event, level=level, best=best, **extra)


@bp.route('/api/niveaux/<subject>/copie', methods=['POST'])
@login_required
def level_copy(subject):
    """« Copier pour une IA » clicked: only counted, for the stats."""
    get_parcours(subject)  # 404 on an unknown subject
    body = request.get_json(silent=True) or {}
    level = body.get('level') if isinstance(body.get('level'), int) else None
    with db() as conn:
        log_event(conn, session['uid'], 'copie_ia', subject, level, str(body.get('exo_id') or '')[:40])
    return jsonify(ok=True)


# --------------------------------------------------------------- stats ----
TZ = 'Europe/Paris'
MAX_SECS = 1800            # one attempt counts at most 30 min of work (tab left open)
MONTHS = ['janv.', 'févr.', 'mars', 'avr.', 'mai', 'juin', 'juil.', 'août', 'sept.', 'oct.', 'nov.', 'déc.']


def day_color(ok, n):
    """Red for a failed day, green for a successful one, in between when mixed (hue 0 -> 130)."""
    return f'hsl({round(130 * ok / n)}, 62%, {48 if n else 90}%)'


def compute_stats(rows, today, titles=None):
    """Statistics of one user's exo_log rows (dicts with subject, level, exo_id, ok, secs, timeout, at as local datetime)."""
    from collections import Counter, defaultdict
    from datetime import timedelta
    titles = titles or {}
    days, hours, per_subject = defaultdict(lambda: [0, 0, 0]), Counter(), defaultdict(lambda: [0, 0])
    fails, first, revenge, failed_before, firsts_ok = Counter(), {}, set(), set(), 0
    for r in rows:
        d = days[r['at'].date()]
        d[0] += 1
        d[1] += r['ok']
        d[2] += min(r['secs'] or 0, MAX_SECS)
        hours[r['at'].hour] += 1
        per_subject[r['subject']][0] += 1
        per_subject[r['subject']][1] += r['ok']
        key = (r['subject'], r['level'], r['exo_id'])
        if key not in first:
            first[key] = r['ok']
            firsts_ok += r['ok']
        if r['ok']:
            if key in failed_before:
                revenge.add(key)
        else:
            failed_before.add(key)
            fails[key] += 1
    done = len(rows)
    ok = sum(r['ok'] for r in rows)
    # heatmap: 53 weeks ending this week, columns start on Monday
    start = today - timedelta(days=today.weekday() + 52 * 7)
    weeks, months = [], []
    for w in range(53):
        col = []
        for k in range(7):
            day = start + timedelta(days=7 * w + k)
            n, g, _ = days.get(day, (0, 0, 0))
            col.append(None if day > today else {
                'date': f'{day.day} {MONTHS[day.month - 1]} {day.year}', 'n': n, 'ok': g,
                'color': day_color(g, n) if n else ''})
        weeks.append(col)
        first_day = start + timedelta(days=7 * w)
        months.append(MONTHS[first_day.month - 1] if first_day.day <= 7 else '')
    # streaks of active days
    active = sorted(days)
    best = run = 0
    for i, day in enumerate(active):
        run = run + 1 if i and (day - active[i - 1]).days == 1 else 1
        best = max(best, run)
    current, day = 0, today if today in days else today - timedelta(days=1)
    while day in days:
        current, day = current + 1, day - timedelta(days=1)
    # minutes per day, last 30 days
    last30 = [today - timedelta(days=29 - i) for i in range(30)]
    minutes = [round(days.get(d, (0, 0, 0))[2] / 60) for d in last30]
    top = max(minutes) or 1
    chart = [{'label': f'{d.day} {MONTHS[d.month - 1]}', 'min': m, 'h': round(100 * m / top)}
             for d, m in zip(last30, minutes)]
    # same chart back to the first activity, in steps of 7 days (the page slides a 30-day window)
    back = -(-max(0, (last30[0] - min(days)).days) // 7) if days else 0
    span = [last30[0] - timedelta(days=7 * back - i) for i in range(30 + 7 * back)]
    chart_all = [{'label': f'{d.day} {MONTHS[d.month - 1]}', 'min': round(days.get(d, (0, 0, 0))[2] / 60)} for d in span]
    # hour x weekday grid, one per week from the first activity to this week
    from admin_stats import week_heat
    monday = today - timedelta(days=today.weekday())
    first_monday = min(days) - timedelta(days=min(days).weekday()) if days else monday
    heat_weeks = []
    while first_monday <= monday:
        end = first_monday + timedelta(days=7)
        heat_weeks.append({'label': f'Semaine du {first_monday.day} {MONTHS[first_monday.month - 1]}'
                                    + (' (en cours)' if first_monday == monday else ''),
                           'heat': week_heat([r['at'] for r in rows if first_monday <= r['at'].date() < end])})
        first_monday = end
    best_day = max(days.items(), key=lambda kv: (kv[1][1], kv[1][0]), default=None)
    hard = fails.most_common(1)
    # weakest levels (>= 3 attempts)
    lvl = defaultdict(lambda: [0, 0])
    for r in rows:
        lvl[(r['subject'], r['level'])][0] += 1
        lvl[(r['subject'], r['level'])][1] += r['ok']
    weak = sorted(((k, v) for k, v in lvl.items() if v[0] >= 3 and v[1] < v[0]), key=lambda kv: (kv[1][1] / kv[1][0], -kv[1][0]))[:5]
    return {
        'heat': week_heat([r['at'] for r in rows]), 'heat_weeks': heat_weeks, 'chart_all': chart_all,
        'weak': [{'id': k[0], 'subject': titles.get(k[0], k[0]), 'level': k[1], 'n': v[0], 'rate': round(100 * v[1] / v[0])} for k, v in weak],
        'avg_secs': round(sum(min(r['secs'] or 0, MAX_SECS) for r in rows) / done) if done else 0,
        'done': done, 'ok': ok, 'ko': done - ok, 'rate': round(100 * ok / done) if done else 0,
        'minutes': round(sum(v[2] for v in days.values()) / 60),
        'week_minutes': sum(minutes[-7:]), 'chart': chart, 'weeks': weeks, 'months': months,
        'active_days': len(days), 'streak': current, 'best_streak': best,
        'best_day': best_day and {'date': f'{best_day[0].day} {MONTHS[best_day[0].month - 1]}',
                                  'ok': best_day[1][1], 'n': best_day[1][0]},
        'hour': hours.most_common(1)[0][0] if hours else None,
        'first_try': round(100 * firsts_ok / len(first)) if first else 0,
        'distinct': len(first), 'revenge': len(revenge),
        'timeouts': sum(r.get('timeout', 0) for r in rows),
        'hardest': hard and {'subject': titles.get(hard[0][0][0], hard[0][0][0]), 'level': hard[0][0][1],
                             'exo': hard[0][0][2], 'fails': hard[0][1]},
        'subjects': sorted(({'titre': titles.get(s, s), 'n': v[0], 'rate': round(100 * v[1] / v[0])}
                            for s, v in per_subject.items()), key=lambda x: -x['n']),
    }


def week_history(rows, events, today):
    """One entry per week (Monday first) from the first activity to this week, newest first,
    with the change against the week before. rows: exo_log dicts, events: event_log dicts (local 'at')."""
    from collections import defaultdict
    from datetime import timedelta
    monday = lambda d: d - timedelta(days=d.weekday())
    w = defaultdict(lambda: {'n': 0, 'ok': 0, 'secs': 0, 'points': 0, 'days': set(), 'review': 0,
                             'up': 0, 'down': 0, 'skip': 0, 'help': 0, 'copies': 0})
    for r in rows:
        x = w[monday(r['at'].date())]
        x['n'] += 1
        x['ok'] += r['ok']
        x['secs'] += min(r['secs'] or 0, MAX_SECS)
        x['points'] += r.get('points') or 0
        x['review'] += r.get('review') or 0
        x['days'].add(r['at'].date())
    kinds = {'niveau_up': 'up', 'niveau_finished': 'up', 'niveau_down': 'down', 'passer': 'skip', 'copie_ia': 'copies'}
    for e in events:
        k = kinds.get(e['kind']) or ('help' if e['kind'] in ('aide_fiche', 'aide_solution') else None)
        if k:
            w[monday(e['at'].date())][k] += 1
    if not w:
        return []
    out, prev, day = [], None, min(w)
    while day <= monday(today):
        x = w.get(day) or w.default_factory()
        cur = {**{k: v for k, v in x.items() if k not in ('days', 'secs')}, 'days': len(x['days']),
               'minutes': round(x['secs'] / 60), 'rate': round(100 * x['ok'] / x['n']) if x['n'] else None,
               'label': f'{day.day} {MONTHS[day.month - 1]}' + (f' {day.year}' if day.year != today.year else ''),
               'current': day == monday(today)}
        cur['delta'] = prev and {k: cur[k] - prev[k] for k in ('n', 'minutes', 'points', 'days')}
        if cur['delta'] is not None and cur['rate'] is not None and prev['rate'] is not None:
            cur['delta']['rate'] = cur['rate'] - prev['rate']
        out.append(cur)
        prev, day = cur, day + timedelta(days=7)
    return out[::-1]


_FICHE = {'mtime': None, 'sections': []}


def formula_sheet():
    """Sections of annales/FORMULES.md (one per ECUE), rendered once per file change."""
    from app import render_markdown_with_math
    path = ROOT / 'annales' / 'FORMULES.md'
    mtime = path.stat().st_mtime
    if _FICHE['mtime'] != mtime:
        parts = re.split(r'^## (.+)$', path.read_text(encoding='utf-8'), flags=re.M)[1:]
        _FICHE['sections'] = [{'id': 'f%d' % i, 'titre': t.strip(), 'html': render_markdown_with_math(body)}
                              for i, (t, body) in enumerate(zip(parts[::2], parts[1::2]))]
        _FICHE['mtime'] = mtime
    return _FICHE['sections']


@bp.route('/formules')
@login_required
def formulas_page():
    return render_template('formules.html', sections=formula_sheet())


MOIS = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre',
        'novembre', 'décembre']


JOURS = ['lun.', 'mar.', 'mer.', 'jeu.', 'ven.', 'sam.', 'dim.']


def _date_fr(d):
    return f"{'1er' if d.day == 1 else d.day} {MOIS[d.month - 1]} {d.year}"


EXAM_TYPES = ('Examen', 'Contrôle')  # on-paper events, shown in red on /calendrier


def event_semester(ev):
    """Semester of a calendar event: explicit `semestre`, else the one of its ECUE, else read from its source (« Moodle S1-MATHS »), else ''."""
    if ev.get('semestre'):
        return ev['semestre']
    if ev.get('ecue'):
        return ev['ecue'].split('/')[1]
    m = re.search(r'\bS0?([1-8])(?!\d)', ev.get('source', ''))
    return f'S{m.group(1)}' if m else ''


def exam_calendar(today, syllabus=None, paths=None, sem=None):
    """Exam dates of syllabus.json 'calendrier' split into upcoming / past, each with links to its
    paths and their first exam level; ECUEs with no date are listed with their periode_examen.
    `sem` ('S3', 'none' for unclassified events) keeps only that semester; `sems` lists the ones present."""
    from datetime import date
    syllabus = syllabus or json.loads((PARCOURS_DIR / 'syllabus.json').read_text(encoding='utf-8'))
    paths = load_parcours() if paths is None else paths
    ecues = {f"{m['id']}/{s['id']}/{e['id']}": (m, s, e)
             for m in syllabus['matieres'] for s in m['semestres'] for e in s['ecues']}

    def links(ids):
        out = []
        for pid in ids:
            data = paths.get(pid)
            if not data:
                continue
            exam = next((l['n'] for l in data['levels'] if l.get('examen')), None)
            out.append({'id': pid, 'titre': data['subject']['titre'], 'url': f'/niveaux/{pid}',
                        'exam_url': f'/niveaux/{pid}?n={exam}' if exam else None})
        return out

    upcoming, past, dated = [], [], set()
    present = set()
    for ev in syllabus.get('calendrier', []):
        present.add(event_semester(ev) or 'none')
        if sem and sem != 'tous' and (event_semester(ev) or 'none') != sem:
            continue
        debut = date.fromisoformat(ev['debut'])
        fin = date.fromisoformat(ev.get('fin', ev['debut']))
        ids = ev.get('parcours') or (ecues[ev['ecue']][2]['parcours'] if ev.get('ecue') else [])
        if ev.get('ecue'):
            dated.add(ev['ecue'])
        item = {**ev, 'sem': event_semester(ev), 'quand': _date_fr(debut) if fin == debut else f'du {_date_fr(debut)} au {_date_fr(fin)}',
                'jours': (debut - today).days, 'en_cours': debut <= today <= fin, 'links': links(ids),
                'jour': debut.day, 'jour_fin': fin.day if fin != debut else None, 'wd': JOURS[debut.weekday()],
                'mois': f'{MOIS[debut.month - 1]} {debut.year}', 'ym': (debut.year, debut.month)}
        (past if fin < today else upcoming).append(item)
    undated = [{'matiere': m['titre'], 'semestre': s['id'], 'titre': e['titre'], 'bloc': e.get('bloc', ''),
                'periode': e.get('periode_examen', ''), 'links': links(e['parcours'])}
               for key, (m, s, e) in ecues.items() if key not in dated and e['parcours']]
    present |= {e['semestre'] for e in undated}
    if sem and sem != 'tous':
        undated = [e for e in undated if e['semestre'] == sem]
    start = today.year if today.month >= 9 else today.year - 1  # school year: September to July
    months = []
    for k in range(11):
        y, m = start + (8 + k) // 12, (8 + k) % 12 + 1
        evs = [e for e in past + upcoming if e['ym'] == (y, m)]
        months.append({
            'nom': MOIS[m - 1][:4], 'label': f'{MOIS[m - 1]} {y}', 'anchor': f'm{y}-{m}',
            'now': (y, m) == (today.year, today.month), 'past': (y, m) < (today.year, today.month),
            'events': evs, 'exams': sum(e['type'] in EXAM_TYPES for e in evs), 'tests': sum(e['type'] not in EXAM_TYPES for e in evs),
            # undated ECUEs whose usual exam period names this month ("décembre-janvier", "partiel en mai")
            'probable': [e for e in undated if re.search(rf'\b{MOIS[m - 1]}\b', e['periode'].lower())]})
    sems = sorted(x for x in present if x != 'none') + (['none'] if 'none' in present else [])
    return {'upcoming': upcoming, 'past': past[::-1], 'undated': undated, 'months': months, 'sems': sems, 'sem': sem or 'tous'}


@bp.route('/calendrier')
def calendar_page():
    from datetime import datetime
    from zoneinfo import ZoneInfo
    cal = exam_calendar(datetime.now(ZoneInfo(TZ)).date(), sem=request.args.get('sem') or None)
    pct = {}
    if session.get('uid'):  # readiness bar per path for logged-in users
        with db() as conn:
            pct = {sid: total_percent(statuses(conn, session['uid'], sid), data) for sid, data in load_parcours().items()}
    return render_template('calendrier.html', pct=pct, **cal)


@bp.route('/stats')
@login_required
def stats_page():
    from datetime import datetime, timezone
    from zoneinfo import ZoneInfo
    tz = ZoneInfo(TZ)
    with db() as conn:
        rows = [dict(r) for r in conn.execute(
            'SELECT subject, level, exo_id, ok, secs, timeout, points, review, at FROM exo_log WHERE account_id=? ORDER BY id',
            (session['uid'],))]
        events = [dict(r) for r in conn.execute('SELECT kind, at FROM event_log WHERE account_id=?', (session['uid'],))]
        total_xp = xp(conn, session['uid'])
    for r in rows + events:  # sqlite CURRENT_TIMESTAMP is UTC
        r['at'] = datetime.fromisoformat(r['at']).replace(tzinfo=timezone.utc).astimezone(tz)
    paths = _paths_meta()
    titles = {sid: d['subject']['titre'] for sid, d in paths}
    s = compute_stats(rows, datetime.now(tz).date(), titles)
    s['history'] = week_history(rows, events, datetime.now(tz).date())
    with db() as conn:
        s['paths'] = []
        for sid, data in paths:
            _, _, best = progress(conn, session['uid'], sid)
            st = statuses(conn, session['uid'], sid)
            green = sum(1 for l in data['levels'] for e in l['exos'] if st.get((l['n'], e['id'])) == 1)
            s['paths'].append({'id': sid, 'titre': data['subject']['titre'], 'best': best, 'n': len(data['levels']),
                               'green': green, 'total': sum(len(l['exos']) for l in data['levels']),
                               'percent': total_percent(st, data)})
    # one foldable block per subject, in syllabus order, with its overall progress
    mats = json.loads((PARCOURS_DIR / 'syllabus.json').read_text(encoding='utf-8'))['matieres']
    s['path_groups'] = []
    for m in mats:
        ps = [x for (sid, d), x in zip(paths, s['paths']) if d['subject'].get('matiere') == m['id']]
        if ps:
            total = sum(x['total'] for x in ps)
            s['path_groups'].append({'titre': m['titre'], 'paths': ps, 'best': sum(x['best'] for x in ps),
                                     'n': sum(x['n'] for x in ps),
                                     'percent': round(sum(x['percent'] * x['total'] for x in ps) / total) if total else 0})
    with db() as conn:  # home feed (session_log is per account since uid)
        n, answered, right, ms = conn.execute(
            'SELECT COUNT(*), COUNT(is_correct), COALESCE(SUM(is_correct), 0), COALESCE(SUM(time_spent_ms), 0)'
            ' FROM session_log WHERE uid=?', (session['uid'],)).fetchone()
        best = conn.execute('SELECT max_streak FROM user_state WHERE uid=?', (session['uid'],)).fetchone()
    s['feed'] = {'n': n, 'answered': answered, 'rate': round(100 * right / answered) if answered else 0,
                 'minutes': round(ms / 60000), 'combo': best[0] if best else 0}
    return render_template('stats.html', s=s, username=session['username'], xp=total_xp)


# ---------------------------------------------------------- classement ----
PERIODS = {'jour': "Aujourd'hui", 'semaine': 'Cette semaine', 'mois': 'Ce mois', 'annee': 'Cette année'}
BOARD_SIZE = 20


def period_start(period, now):
    """UTC timestamp text (exo_log.at format) of the start of the local day/week/month/year of `now` (aware)."""
    from datetime import datetime, time as dtime, timedelta, timezone
    d = now.date()
    d = {'jour': d, 'semaine': d - timedelta(days=d.weekday()), 'mois': d.replace(day=1),
         'annee': d.replace(month=1, day=1)}[period]
    return datetime.combine(d, dtime(), now.tzinfo).astimezone(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')


def leaderboards(conn, since, subjects=None):
    """{'temps'|'niveaux'|'points': [(account_id, username, value)] best first}: visible accounts only,
    activity since `since` (UTC text), restricted to `subjects` (path ids) when given."""
    filt, args = '', [since]
    if subjects is not None:
        filt, args = f" AND l.subject IN ({','.join('?' * len(subjects))})", args + list(subjects)
    q = ('SELECT a.id, a.username, {v} AS v FROM {t} l JOIN account a ON a.id = l.account_id '
         'WHERE a.leaderboard = 1 AND a.board_ban = 0 AND l.at >= ?' + filt + '{w} GROUP BY a.id HAVING v > 0 ORDER BY v DESC, a.username')
    return {
        'temps': conn.execute(q.format(v=f'SUM(MIN(COALESCE(l.secs, 0), {MAX_SECS}))', t='exo_log', w=''), args).fetchall(),
        # levels passed in the period, each (path, level) once even if passed again after a drop
        'niveaux': conn.execute(q.format(v="COUNT(DISTINCT l.subject || '/' || l.level)", t='event_log',
                                         w=" AND l.kind IN ('niveau_up', 'niveau_finished')"), args).fetchall(),
        'points': conn.execute(q.format(v='SUM(l.points)', t='exo_log', w=''), args).fetchall(),
    }


def ranks(values):
    """Competition ranks of values sorted best first: ties share a rank, the next one skips (1, 1, 3)."""
    out = []
    for i, v in enumerate(values):
        out.append(out[-1] if i and v == values[i - 1] else i + 1)
    return out


def _duration(secs):
    h, m = divmod(round(secs / 60), 60)
    return f'{h} h {m:02d}' if h else f'{m} min'


@bp.route('/api/classement', methods=['POST'])
@login_required
def set_leaderboard():
    visible = bool((request.get_json(silent=True) or {}).get('visible'))
    with db() as conn:
        conn.execute('UPDATE account SET leaderboard=? WHERE id=?', (int(visible), session['uid']))
    return jsonify(ok=True, visible=visible)


@bp.route('/api/pari', methods=['POST'])
@login_required
def set_pari():
    on = bool((request.get_json(silent=True) or {}).get('on'))
    with db() as conn:
        conn.execute('UPDATE account SET pari=? WHERE id=?', (int(on), session['uid']))
    return jsonify(ok=True, on=on)


@bp.route('/classement')
@login_required
def leaderboard_page():
    from datetime import datetime
    from zoneinfo import ZoneInfo
    period = request.args.get('p') if request.args.get('p') in PERIODS else 'semaine'
    mats = [{'id': m['id'], 'titre': m['titre']} for m in
            json.loads((PARCOURS_DIR / 'syllabus.json').read_text(encoding='utf-8'))['matieres']]
    mat = request.args.get('m') if request.args.get('m') in {m['id'] for m in mats} else ''
    subjects = [sid for sid, d in _paths_meta() if d['subject'].get('matiere') == mat] if mat else None
    uid = session['uid']
    with db() as conn:
        raw = leaderboards(conn, period_start(period, datetime.now(ZoneInfo(TZ))), subjects)
        visible = conn.execute('SELECT leaderboard FROM account WHERE id=?', (uid,)).fetchone()[0]
    fmt = {'temps': _duration, 'niveaux': str, 'points': str}
    boards = {}
    for key, rows in raw.items():
        ranked = [{'rank': rank, 'name': name, 'value': fmt[key](v), 'me': aid == uid}
                  for (aid, name, v), rank in zip(rows, ranks([r[2] for r in rows]))]
        top = ranked[:BOARD_SIZE]
        top += [dict(r, gap=True) for r in ranked[BOARD_SIZE:] if r['me']]  # own rank even outside the top
        boards[key] = top
    return render_template('classement.html', boards=boards, periods=PERIODS, period=period,
                           mats=mats, mat=mat, visible=visible)


# -------------------------------------------------------------- triche ----
# Levels are self-graded: cheating = clicking « Réussi » without doing the exercise.
FAST_RATIO = 0.2    # a success in under 20 % of the level's usual time is too fast to be real
FAST_MIN = 5        # flagged from this many too-fast successes...
FAST_SHARE = 0.5    # ...when they are at least half of the account's successes
STREAK_FLAG = 40    # successes in a row without a single miss
RUSH_WINDOW = 3600  # seconds
RUSH_LEVELS = 4     # levels validated within RUSH_WINDOW...
RUSH_MATIERES = 2   # ...spread over at least this many subjects


def suspects(logs, ups, matiere_of, authored):
    """{account_id: [reasons]} for accounts whose answers are too fast or too perfect to be real.
    logs: (account_id, subject, level, ok, secs, unix time) in id order; ups: (account_id, subject, level,
    unix time) of niveau_up/finished events; matiere_of: path id -> subject id; authored: (path, level) ->
    authored mean seconds, used as the usual time until MIN_SAMPLES successes give a median."""
    from collections import defaultdict
    from statistics import median
    times = defaultdict(list)
    for _, sub, lvl, ok, secs, _ in logs:
        if ok and secs:
            times[(sub, lvl)].append(secs)
    usual = {k: median(v) if len(v) >= MIN_SAMPLES else authored.get(k, 300) * 0.6 for k, v in times.items()}
    out = defaultdict(list)
    per = defaultdict(list)
    for row in logs:
        per[row[0]].append(row)
    for aid, rows in per.items():
        oks = [r for r in rows if r[3]]
        fast = sum(1 for r in oks if r[4] and r[4] < FAST_RATIO * usual[(r[1], r[2])])
        if fast >= FAST_MIN and fast >= FAST_SHARE * len(oks):
            out[aid].append(f'{fast} réussites trop rapides ({round(100 * fast / len(oks))} % de ses réussites)')
        run = best = 0
        for r in rows:
            run = run + 1 if r[3] else 0
            best = max(best, run)
        if best >= STREAK_FLAG:
            out[aid].append(f"{best} réussites d'affilée sans une erreur")
    by_acc = defaultdict(list)
    for aid, sub, lvl, at in sorted(ups, key=lambda u: u[3]):
        by_acc[aid].append((at, matiere_of.get(sub, sub)))
    for aid, evs in by_acc.items():
        worst = None
        for i, (t0, _) in enumerate(evs):
            win = [m for t, m in evs[i:] if t - t0 <= RUSH_WINDOW]
            if len(win) >= RUSH_LEVELS and len(set(win)) >= RUSH_MATIERES and (not worst or len(win) > worst[0]):
                worst = (len(win), len(set(win)))
        if worst:
            out[aid].append(f'{worst[0]} niveaux validés en moins d\'1 h dans {worst[1]} matières')
    return dict(out)


FRAUD_WARNING = ('Triche suspectée : tes réponses sont trop rapides ou trop parfaites pour être réelles. '
                 "Ton compte est signalé à l'admin et peut être exclu du classement.")


def all_suspects(conn):
    """suspects() over the whole database: {account_id: [reasons]}.
    shortcut: rescans every exo_log row (called on each page view), cache it once exo_log has ~100k rows."""
    paths = load_parcours()
    matiere_of = {sid: d['subject'].get('matiere', sid) for sid, d in paths.items()}
    authored = {(sid, l['n']): sum(int(e.get('duree', 5)) * 60 for e in l['exos']) / len(l['exos'])
                for sid, d in paths.items() for l in d['levels'] if l['exos']}
    logs = conn.execute("SELECT account_id, subject, level, ok, secs, CAST(strftime('%s', at) AS INTEGER) "
                        'FROM exo_log ORDER BY id').fetchall()
    ups = conn.execute("SELECT account_id, subject, level, CAST(strftime('%s', at) AS INTEGER) FROM event_log "
                       "WHERE kind IN ('niveau_up', 'niveau_finished')").fetchall()
    return suspects([tuple(r) for r in logs], [tuple(r) for r in ups], matiere_of, authored)


def suspect_list(conn):
    """Rows for the « Triche possible » table of /admin/stats, most reasons first."""
    found = all_suspects(conn)
    names = {r[0]: (r[1], r[2], r[3]) for r in conn.execute('SELECT id, username, leaderboard, board_ban FROM account')}
    rows = [{'id': aid, 'username': names[aid][0], 'visible': names[aid][1], 'banned': names[aid][2], 'reasons': why}
            for aid, why in found.items() if aid in names]
    return sorted(rows, key=lambda r: (-len(r['reasons']), r['username'].lower()))


@bp.route('/api/admin/classement', methods=['POST'])
@login_required
def ban_from_leaderboard():
    if not is_admin():
        return jsonify(error='réservé à l\'admin'), 403
    body = request.get_json(silent=True) or {}
    try:
        aid = int(body.get('account_id'))
    except (TypeError, ValueError):
        return jsonify(error='compte invalide'), 400
    with db() as conn:
        conn.execute('UPDATE account SET board_ban=? WHERE id=?', (int(bool(body.get('ban'))), aid))
    return jsonify(ok=True)
