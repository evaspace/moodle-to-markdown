#!/usr/bin/env python3
"""Map every card (category, subcategory) to the course file it comes from.

Writes course_links.json, read by app.py to show a "Lire le chapitre" link on each card:
    {"<norm category>||<norm subcategory>": "Course/Chapter/README.md", ...,
     "<norm category>": "Course/README.md", ...}

Matching, best first:
  1. exact chapter folder via md_to_cards.CategoryResolver (same rules as the card pipeline)
  2. word overlap between the subcategory and file paths / first headings in the category's courses
  3. the category's course index (README.md)

Usage: python build_course_links.py [--db cards.db] [--out course_links.json]
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
from collections import defaultdict
from pathlib import Path

import md_to_cards as m

ROOT = Path(__file__).resolve().parent
MD_ROOT = ROOT / "EPITA_Moodle_Notes_MD"
STOPWORDS = {
    "les", "des", "une", "aux", "pour", "par", "sur", "dans", "avec", "cours", "section",
    "chapitre", "partie", "introduction", "readme", "general", "fichiers", "pages", "qcms",
    "promo", "the", "and", "and", "s1", "s2", "td", "tp",
}
MIN_SCORE = 0.5


def key(s: str) -> str:
    return m.normalize_key(s.replace("*", ""))


def tokens(s: str) -> set[str]:
    words = re.findall(r"[a-z0-9]+", key(s))
    return {w for w in words if len(w) >= 3 and w not in STOPWORDS}


def first_heading(path: Path) -> str:
    try:
        with path.open(encoding="utf-8", errors="ignore") as f:
            for _, line in zip(range(40), f):
                if line.startswith("#"):
                    return line.lstrip("#").strip()
    except OSError:
        pass
    return ""


def overlap(query: set[str], target: set[str]) -> float:
    return len(query & target) / len(query) if query else 0.0


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(ROOT / "cards.db"))
    ap.add_argument("--out", default=str(ROOT / "course_links.json"))
    args = ap.parse_args()

    resolver = m.CategoryResolver(ROOT / m.SELECTED_COURSES, ROOT / m.SYLLABUS)

    # Course folders per category, and exact chapter folders per (category, subcategory)
    folders_by_cat: dict[str, set[Path]] = defaultdict(set)
    exact: dict[str, Path] = {}
    for course_dir, chapter_dir in m.iter_chapters(MD_ROOT):
        cat, sub = resolver.resolve(course_dir.name, chapter_dir.name)
        folders_by_cat[key(cat)].add(course_dir)
        readme = chapter_dir / "README.md"
        if readme.is_file():
            exact.setdefault(f"{key(cat)}||{key(sub)}", readme)

    courses = [d for d in sorted(MD_ROOT.iterdir()) if d.is_dir()]
    course_tokens = {d: tokens(d.name) | tokens(first_heading(d / "README.md")) for d in courses}

    # Searchable documents: every .md, described by its path and first heading
    docs: dict[Path, list[tuple[Path, set[str]]]] = defaultdict(list)
    for course in courses:
        for md in course.rglob("*.md"):
            rel_parts = md.relative_to(course).with_suffix("").parts
            desc = " ".join(p for p in rel_parts if p != "README") + " " + first_heading(md)
            docs[course].append((md, tokens(desc)))

    conn = sqlite3.connect(f"file:{args.db}?mode=ro", uri=True)
    rows = conn.execute(
        "SELECT cat.name, sc.name, COUNT(c.id) FROM subcategory sc "
        "JOIN category cat ON cat.id = sc.category_id "
        "JOIN card c ON c.subcategory_id = sc.id GROUP BY sc.id").fetchall()

    links: dict[str, str] = {}
    stats = {"exact": 0, "fuzzy": 0, "course": 0, "none": 0}
    for cat_name, sub_name, n in rows:
        ck = key(cat_name)
        cat_folders = folders_by_cat.get(ck)
        if not cat_folders:
            # Category not produced by the resolver (older imports): closest course folder names
            cq = tokens(cat_name)
            scored = sorted(((overlap(cq, t), d) for d, t in course_tokens.items()), reverse=True,
                            key=lambda x: x[0])
            cat_folders = {d for s, d in scored if s >= MIN_SCORE and s == scored[0][0]} if scored else set()
        if cat_folders and ck not in links:
            readme = sorted(cat_folders)[0] / "README.md"
            if readme.is_file():
                links[ck] = str(readme.relative_to(MD_ROOT))

        sk = f"{ck}||{key(sub_name)}"
        if sk in exact:
            links[sk] = str(exact[sk].relative_to(MD_ROOT))
            stats["exact"] += n
            continue
        sq = tokens(sub_name)
        search_in = cat_folders or set(courses)
        best, best_score = None, 0.0
        for course in search_in:
            for md, t in docs[course]:
                s = overlap(sq, t)
                # Prefer chapter READMEs over individual files at equal score
                if s > best_score or (s == best_score and best is not None and md.name == "README.md"
                                      and best.name != "README.md"):
                    best, best_score = md, s
        if best is not None and best_score >= MIN_SCORE:
            links[sk] = str(best.relative_to(MD_ROOT))
            stats["fuzzy"] += n
        elif ck in links:
            stats["course"] += n
        else:
            stats["none"] += n

    Path(args.out).write_text(json.dumps(links, ensure_ascii=False, indent=1), encoding="utf-8")
    total = sum(stats.values())
    print(f"{len(links)} links written to {args.out}")
    for k, v in stats.items():
        print(f"  cards linked {k:6}: {v:5} ({v / total:.0%})")


if __name__ == "__main__":
    main()
