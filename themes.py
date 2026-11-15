"""Group the raw course categories (Moodle folder names) into a few themes for the home page.

Categories come from several imports and are inconsistent ("MATHS-2030", "S1-MATHS-2030",
"Maths S1 - OBM", "**Génie Logiciel**"...). Each one is assigned to the first theme whose
keywords match its normalized name; anything unmatched lands in "Autres".
"""
import re
import unicodedata

# (id, label, icon, keywords) — order matters: first match wins
THEMES = [
    ('maths', 'Mathématiques', '∑', ['math', 'probabilit', 'statisti', 'arith', 'analyse', 'algebre']),
    ('physique', 'Physique', '⚛', ['physique', 'mecanique', 'thermo']),
    ('electronique', 'Électronique', '🔌', ['electronique', 'elec']),
    ('algo', 'Algo & Programmation', '⚡', ['algo', 'programmation', 'caml', 'python', 'minimake',
                                           'backtobasics', 'genie logiciel', 'code']),
    ('archi', 'Architecture des ordinateurs', '💻', ['archi']),
    ('cyber_ia', 'Cyber & IA', '🛡️', ['cyber', 'intelligence artificielle', ' ia ']),
    ('langues', 'Langues & Communication', '🗣️', ['anglais', 'rosetta', 'expression', 'communication',
                                                   'francais', 'com s', 'ecrit', 'oral',
                                                   'acf sup', 'adp sup']),
    ('projets', 'Projets', '🛠️', ['projet']),
    ('methodo', 'Méthodologie & Concours', '🧭', ['methodo', 'prepa', 'preparation', 'concours',
                                                  'examen', 'ddrs', 'soutenab']),
    ('campus', 'Vie de campus', '🏫', ['campus']),
]
OTHER = ('autres', 'Autres', '📦')


def _normalize(name: str) -> str:
    s = unicodedata.normalize('NFD', name)
    s = ''.join(c for c in s if not unicodedata.combining(c)).lower()
    s = re.sub(r'[^a-z0-9]+', ' ', s)
    return f' {s.strip()} '


def clean_name(name: str) -> str:
    """Display name without leftover Markdown bold markers."""
    return re.sub(r'\s+', ' ', name.replace('*', '')).strip() or name


def theme_for(category_name: str) -> dict:
    norm = _normalize(clean_name(category_name))
    for theme_id, label, icon, keywords in THEMES:
        if any(k in norm for k in keywords):
            return {'id': theme_id, 'label': label, 'icon': icon}
    theme_id, label, icon = OTHER
    return {'id': theme_id, 'label': label, 'icon': icon}


def theme_order(theme_id: str) -> int:
    ids = [t[0] for t in THEMES]
    return ids.index(theme_id) if theme_id in ids else len(ids)


def syllabus_rank(category_name: str) -> int:
    """Sort key putting promo 2031 first, then S1, then S2, then the rest (unlabelled categories)."""
    norm = _normalize(clean_name(category_name))
    if ' 2031 ' in norm:
        return 0
    if ' s1 ' in norm:
        return 1
    if ' s2 ' in norm:
        return 2
    return 3
