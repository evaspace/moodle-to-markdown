#!/usr/bin/env python3
"""index_cards.py — indexe les cartes par (catégorie, sous-catégorie) et dit où il manque des QCM/TF.

Usage:
  python index_cards.py                     # rapport depuis cards.db local
  python index_cards.py --write-index       # écrit aussi course_index.json (pour md_to_cards.py --offline)
  python index_cards.py --db autre.db --min 8
"""
import argparse, json, sqlite3, sys
from collections import defaultdict

SQL = ("SELECT cat.name AS category, sc.name AS subcategory, c.type, c.front, c.back, c.payload "
       "FROM card c JOIN subcategory sc ON sc.id = c.subcategory_id "
       "JOIN category cat ON cat.id = sc.category_id")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default="cards.db")
    ap.add_argument("--min", type=int, default=8, help="QCM+TF minimum par chapitre")
    ap.add_argument("--write-index", action="store_true")
    ap.add_argument("--index-file", default="course_index.json")
    a = ap.parse_args()

    con = sqlite3.connect(f"file:{a.db}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    rows = [dict(r) for r in con.execute(SQL)]
    if a.write_index:
        with open(a.index_file, "w", encoding="utf-8") as f:
            json.dump(rows, f, ensure_ascii=False, indent=1)
        print(f"Index écrit : {a.index_file} ({len(rows)} cartes)")

    stat = defaultdict(lambda: {"COURSE": 0, "QCM": 0, "TF": 0})
    for r in rows:
        stat[(r["category"], r["subcategory"])][r["type"]] += 1
    short = {k: v for k, v in stat.items() if v["QCM"] + v["TF"] < a.min}
    print(f"{len(stat)} chapitres, {len(short)} avec moins de {a.min} QCM+TF")
    print(f"{'COURSE':>6} {'QCM':>4} {'TF':>3}  catégorie / chapitre")
    for (cat, sub), v in sorted(short.items(), key=lambda kv: -kv[1]["COURSE"])[:40]:
        print(f"{v['COURSE']:>6} {v['QCM']:>4} {v['TF']:>3}  {cat} / {sub}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
