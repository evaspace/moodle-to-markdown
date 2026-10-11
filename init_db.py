import os
import sqlite3

DB_PATH = os.environ.get('DB_PATH', 'cards.db')

SCHEMA = '''
    CREATE TABLE IF NOT EXISTS category (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    );
    CREATE TABLE IF NOT EXISTS subcategory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        FOREIGN KEY(category_id) REFERENCES category(id)
    );
    CREATE TABLE IF NOT EXISTS card (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subcategory_id INTEGER,
        type TEXT NOT NULL,          -- 'COURSE', 'QCM', 'TF'
        front TEXT NOT NULL,
        back TEXT,                   -- Explication
        payload TEXT,                -- JSON: choix (QCM) ou vérité (TF)
        status INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(subcategory_id) REFERENCES subcategory(id)
    );
    CREATE TABLE IF NOT EXISTS folder (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    );
    CREATE TABLE IF NOT EXISTS favorite (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        card_id INTEGER NOT NULL,
        folder_id INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(card_id) REFERENCES card(id),
        FOREIGN KEY(folder_id) REFERENCES folder(id),
        UNIQUE(card_id, folder_id)
    );
    CREATE TABLE IF NOT EXISTS user_state (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        streak INTEGER DEFAULT 0,
        max_streak INTEGER DEFAULT 0,
        level INTEGER DEFAULT 1,
        xp INTEGER DEFAULT 0
    );
    CREATE TABLE IF NOT EXISTS session_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        card_id INTEGER NOT NULL,
        time_spent_ms INTEGER NOT NULL,
        is_correct INTEGER,          -- 1=Vrai, 0=Faux, NULL=Cours
        viewed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(card_id) REFERENCES card(id)
    );
    CREATE INDEX IF NOT EXISTS idx_log_card ON session_log(card_id, id);
    CREATE INDEX IF NOT EXISTS idx_card_sub ON card(subcategory_id);
'''


def init_db(path=DB_PATH):
    conn = sqlite3.connect(path)
    conn.execute('PRAGMA journal_mode=WAL')
    conn.executescript(SCHEMA)
    conn.execute("INSERT OR IGNORE INTO user_state (id, streak, max_streak, level, xp) VALUES (1, 0, 0, 1, 0)")
    conn.commit()
    conn.close()


if __name__ == '__main__':
    init_db()
