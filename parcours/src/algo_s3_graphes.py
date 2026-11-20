"""Level path: S3 algorithmics, graphs (ECUE Graphes, exam at the end of B6, Python).

Moodle course « [algo] Graphs » (chapters 03 terminologie, 04 représentation, 05 parcours, 06 connexité, 07 and 08
exercises = TD 1 « implémentations et parcours » and TD 2 « applications »). Calibrated on the S3 algorithmics exams of
`annales/raw/S3` : partiels P3 of 19 December 2017, 18 December 2018, 17 December 2019, 5 January 2021 (folders
Finals/Algo/2021, 2022, 2023, 2024), the rattrapages of 14 May 2019 and 12 May 2021 (2023#, 2025#), and the contrôles C3 of
November 2019 and 9 November 2021 (Midterms/Algo/2023, 2025). Levels 1 and 2 are reminders of S1/S2 (complexity of
loops, queues and stacks, general trees: `algo-s1-python`, `algo-s1-taa`, `algo-s2-abg`).

Checks at import (build.py imports this module, so a wrong hand-written answer stops the build):
- every `value` exercise is computed twice: `calc` (sympy: adjacency matrices, matrix powers, `parc(...)` helper of
  build.py for BFS/DFS orders) and `ans` (plain Python search below); the two must agree (build.py);
- every open answer about a figure (forests, arc types, union-find vectors, closures) is produced by the Python
  functions of this file, never typed by hand, and the official answers that could be read are asserted;
- every model function (`w()`) is run on the graphs of the statement and replays the `>>>` session; `_api()` rejects
  models that break the exam annex (only `len`, `range`, `min`, `max`, `append`, `pop`, `insert`, `Graph`, `Queue`, own
  functions; no slice, no `in` test, no comprehension, no import);
- figures are drawn as SVG files in `static/graphes/` (name = hash of the drawing), shown as Markdown images.
"""
import ast
import collections
import contextlib
import hashlib
import html
import io
import itertools
import math
from pathlib import Path

from .algo_python import _out, _py, _session

SUBJECT = {
    "id": "algo-s3-graphes",
    "ordre": 690,
    "matiere": "algo",
    "semestre": "S3",
    "ecue": "Graphes",
    "titre": "Graphes : terminologie, représentations, parcours, connexité, applications",
    "chapitres_moodle": [
        "03_Les graphes - description - terminologie",
        "04_Représentation des graphes",
        "05_Parcours de graphes",
        "06_Connexité des graphes non orientés",
        "07_🐍 Exercises 1- implementations + BFS + DFS",
        "08_🐍 Exercises 2- Applications",
    ],
    "td": "TD 1 (implémentations et parcours) et TD 2 (applications) de novembre 2026, partiels P3 et contrôles C3 des annales S3",
    "examens": ["Examen écrit de fin de bloc B6 d'algorithmique, graphes (Python, 2 h, décembre)"],
}

CHECKED = []
FIG_DIR = Path(__file__).resolve().parents[2] / "static" / "graphes"
FIG_URL = "/static/graphes/"

# ---------------------------------------------------------------- exam classes (annex of the subjects)


class Graph:
    def __init__(self, order, directed=False):
        self.order = order
        self.directed = directed
        self.adjlists = [[] for _ in range(order)]

    def addvertex(self):
        self.order += 1
        self.adjlists.append([])

    def addedge(self, src, dst):
        self.adjlists[src].append(dst)
        if not self.directed and dst != src:
            self.adjlists[dst].append(src)


class Queue:
    def __init__(self):
        self.q = collections.deque()

    def enqueue(self, e):
        self.q.append(e)

    def dequeue(self):
        return self.q.popleft()

    def isempty(self):
        return not self.q


# ---------------------------------------------------------------- graphs of the statements (labels, edges, kind)


class GR:
    """Simple graph or 1-graph with vertex labels `vs` (the first one is the base of the numbering)."""

    def __init__(self, vs, edges, directed=False):
        self.vs, self.directed = list(vs), directed
        self.edges = sorted({(a, b) if directed or a <= b else (b, a) for a, b in edges})
        self.adj = {v: [] for v in self.vs}
        for a, b in self.edges:
            self.adj[a].append(b)
            if not directed and a != b:
                self.adj[b].append(a)
        for v in self.vs:
            self.adj[v].sort()
        self.base = self.vs[0]

    def lists(self):
        return [self.adj[v] for v in self.vs]

    def adjs(self):  # `adj` argument of parc
        return repr(self.lists()).replace(" ", "")

    def rows(self):  # adjacency matrix, row = source
        return [[1 if y in self.adj[x] else 0 for y in self.vs] for x in self.vs]

    def mat(self):
        return "Matrix(" + repr(self.rows()).replace(" ", "") + ")"

    def graph(self):  # exam Graph, vertices numbered from 0
        assert self.base == 0
        G = Graph(len(self.vs), self.directed)
        G.adjlists = [list(a) for a in self.lists()]
        return G


def und(n, edges, first=0):
    return GR(range(first, first + n), edges)


def dig(n, arcs, first=0):
    return GR(range(first, first + n), arcs, True)


GC = und(13, [(10, 4), (10, 7), (7, 4), (7, 9), (4, 2), (4, 0), (2, 3), (2, 5), (3, 5), (5, 6), (6, 0), (6, 1), (0, 9),
              (0, 8), (9, 8), (9, 11), (8, 11), (8, 12), (11, 12), (12, 1)])
GC_POS = {3: (685, 448), 2: (572, 484), 10: (345, 532), 4: (460, 556), 5: (675, 563), 7: (342, 615), 6: (637, 690),
          0: (500, 688), 9: (380, 745), 8: (470, 803), 1: (662, 822), 11: (402, 882), 12: (540, 895)}
G3CC = und(14, [(2, 6), (2, 5), (5, 6), (0, 5), (0, 6), (3, 13), (13, 10), (3, 8), (8, 10), (3, 1), (8, 1), (10, 7), (1, 7),
                (9, 12), (12, 11), (11, 4), (4, 9)])
G3CC_POS = {9: (235, 45), 12: (330, 45), 4: (240, 135), 11: (330, 130), 13: (120, 165), 3: (45, 235), 10: (185, 230),
            8: (120, 255), 1: (90, 320), 7: (180, 320), 2: (272, 210), 6: (335, 235), 5: (338, 290), 0: (280, 325)}
# TD 1, G1 (digraph) and G2 (graph) without multiple links nor loop
T1 = dig(9, [(0, 4), (0, 1), (0, 5), (0, 3), (1, 4), (2, 3), (3, 6), (5, 4), (5, 2), (5, 0), (6, 0), (6, 5), (7, 8), (7, 1),
             (7, 0), (8, 6)])
T2 = und(10, [(0, 4), (0, 1), (0, 3), (2, 6), (2, 5), (2, 7), (4, 9), (5, 7), (5, 8), (6, 7), (7, 8)])
# partiel P3 of 19 Dec 2017 (ex. 2) and contrôle of Nov 2019 (ex. 1): digraph on 1..10
E21 = dig(10, [(1, 2), (1, 6), (1, 7), (2, 3), (2, 6), (3, 1), (3, 5), (4, 3), (4, 8), (4, 9), (4, 10), (5, 1), (7, 6), (8, 5),
               (8, 10), (10, 9)], 1)
# contrôle C3 of 9 Nov 2021 (ex. 1): digraph on 1..9
E25 = dig(9, [(1, 2), (1, 6), (2, 3), (2, 5), (3, 1), (3, 4), (3, 5), (4, 5), (4, 8), (6, 2), (6, 5), (7, 5), (7, 6), (7, 8),
              (8, 5), (8, 9), (9, 4), (9, 7)], 1)
# partiel of 17 Dec 2019 (ex. 1): matrix of a simple graph on 1..9 (it is a tree)
E23 = und(9, [(1, 2), (1, 3), (3, 4), (3, 5), (4, 6), (4, 7), (7, 8), (7, 9)], 1)
# small graphs for variants
U1 = und(8, [(0, 1), (0, 2), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (4, 6), (6, 7)])
U1_POS = {0: (40, 30), 1: (40, 130), 2: (120, 80), 3: (210, 80), 4: (300, 80), 5: (360, 20), 6: (360, 140), 7: (450, 140)}
U2 = und(9, [(0, 1), (0, 3), (1, 2), (1, 4), (3, 4), (4, 5), (3, 6), (6, 7), (7, 8), (5, 8)])
D1 = dig(7, [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 3), (6, 4), (2, 6)])
D2 = dig(8, [(0, 3), (0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (5, 3), (6, 7), (7, 6), (2, 6)])
M5 = dig(5, [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (2, 0), (4, 1)])
M5_POS = {0: (30, 70), 1: (110, 20), 2: (110, 120), 3: (200, 70), 4: (290, 70)}
M6 = dig(6, [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (4, 5), (5, 3), (1, 4)])
K4 = und(4, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])
DAG = dig(8, [(0, 1), (1, 2), (2, 5), (0, 3), (3, 4), (4, 6), (6, 7), (5, 7)])
C6 = und(6, [(i, (i + 1) % 6) for i in range(6)])
TREE = und(10, [(0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (3, 6), (3, 7), (3, 8), (6, 9)])
TREE2 = und(9, [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6), (4, 7), (6, 8)])


# ---------------------------------------------------------------- searches in plain Python (answers)


def bfs(g, s):
    """(order of one search from s, distances from s)."""
    dist, order, q = {s: 0}, [s], collections.deque([s])
    while q:
        x = q.popleft()
        for y in g.adj[x]:
            if y not in dist:
                dist[y] = dist[x] + 1
                order.append(y)
                q.append(y)
    return order, dist


def bfs_full(g, s):
    seen, order = set(), []
    for v in [s] + g.vs:
        if v not in seen:
            o, _ = bfs(g, v)
            order += [y for y in o if y not in seen]
            seen |= set(o)
    return order


class DFS:
    """Full depth-first search, launches on s then on the unvisited vertices in increasing order; one shared counter."""

    def __init__(self, g, s):
        self.g, self.pre, self.suf, self.pn, self.sn, self.parent, self.kind, self.roots, self.cc = g, [], [], {}, {}, {}, {}, [], {}
        self.cnt, self.used = 0, set()
        for v in [s] + g.vs:
            if v not in self.pn:
                self.roots.append(v)
                self.parent[v] = None
                self._go(v, len(self.roots))

    def _go(self, x, c):
        self.cnt += 1
        self.pn[x] = self.cnt
        self.cc[x] = c
        self.pre.append(x)
        for y in self.g.adj[x]:
            e = (x, y) if self.g.directed else frozenset((x, y))
            if e in self.used:
                continue
            self.used.add(e)
            if y not in self.pn:
                self.kind[(x, y)] = "couvrant"
                self.parent[y] = x
                self._go(y, c)
            elif y not in self.sn:
                self.kind[(x, y)] = "arrière"
            else:
                self.kind[(x, y)] = "avant" if self.pn[y] > self.pn[x] else "croisé"
        self.cnt += 1
        self.sn[x] = self.cnt
        self.suf.append(x)

    def children(self, v):
        return [y for y in self.g.adj[v] if self.kind.get((v, y)) == "couvrant"]


def closure(g):
    n, vs = len(g.vs), g.vs
    c = [[1 if (i == j or vs[j] in g.adj[vs[i]]) else 0 for j in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                c[i][j] = c[i][j] or (c[i][k] and c[k][j])
    return c


def comps(g):
    """Connected components (undirected), numbered in the order of the search launches from the first vertex."""
    return DFS(g, g.vs[0]).cc


def fmt(seq):
    return ", ".join(str(x) for x in seq)


def mrow(seq):
    return "Matrix([[" + ",".join(str(x) for x in seq) + "]])"


# ---------------------------------------------------------------- figures (SVG files)

_R = 14


def _circle(g):
    n = len(g.vs)
    r = max(45, 6.2 * n)
    return {v: (r * math.sin(2 * math.pi * i / n), -r * math.cos(2 * math.pi * i / n)) for i, v in enumerate(g.vs)}


def _forest_pos(roots, children):
    pos, cnt = {}, [0.0]

    def go(v, d):
        ch = [go(c, d + 1) for c in children(v)]
        x = (pos[ch[0]][0] + pos[ch[-1]][0]) / 2 if ch else cnt[0]
        if not ch:
            cnt[0] += 1
        pos[v] = (x, d)
        return v

    for r in roots:
        go(r, 0)
    return {v: (x * 46, d * 56) for v, (x, d) in pos.items()}


def _tree_pos(g, root):
    d = DFS(g, root)
    return _forest_pos([root], d.children)


def _unit(dx, dy):
    h = math.hypot(dx, dy) or 1.0
    return dx / h, dy / h


def gfig(g, pos=None, kinds=None, title=""):
    """Markdown image of a graph. kinds: {(x, y): kind} draws the non-tree arcs dashed with a letter."""
    pos = pos or _circle(g)
    xs, ys = [p[0] for p in pos.values()], [p[1] for p in pos.values()]
    ox, oy = min(xs) - 26, min(ys) - 26
    P = {v: (p[0] - ox, p[1] - oy) for v, p in pos.items()}
    W, H = int(max(xs) - ox + 26), int(max(ys) - oy + 26)
    parts = []
    letters = {"avant": "A", "arrière": "R", "croisé": "C"}
    for a, b in g.edges:
        (x1, y1), (x2, y2) = P[a], P[b]
        kind = (kinds or {}).get((a, b), "couvrant" if kinds is not None else None)
        dash = ' stroke-dasharray="5 3"' if kinds is not None and kind != "couvrant" else ""
        cx, cy = (x1 + x2) / 2, (y1 + y2) / 2
        if g.directed:
            curved = (b, a) in g.edges or (kinds is not None and kind != "couvrant")
            if curved:
                ux, uy = _unit(x2 - x1, y2 - y1)
                off = 18 if (b, a) in g.edges else 16
                cx, cy = cx - uy * off, cy + ux * off
            sx, sy = _unit(cx - x1, cy - y1) if curved else _unit(x2 - x1, y2 - y1)
            ex, ey = _unit(x2 - cx, y2 - cy) if curved else (sx, sy)
            p1, p2 = (x1 + sx * _R, y1 + sy * _R), (x2 - ex * (_R + 3), y2 - ey * (_R + 3))
            d = f"M{p1[0]:.1f},{p1[1]:.1f} Q{cx:.1f},{cy:.1f} {p2[0]:.1f},{p2[1]:.1f}" if curved else \
                f"M{p1[0]:.1f},{p1[1]:.1f} L{p2[0]:.1f},{p2[1]:.1f}"
            parts.append(f'<path d="{d}" fill="none"{dash} marker-end="url(#a)"/>')
            lx, ly = (cx + (x1 + x2) / 2) / 2, (cy + (y1 + y2) / 2) / 2
        else:
            parts.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"{dash}/>')
            lx, ly = cx, cy
        if kinds is not None and kind != "couvrant":
            parts.append(f'<text class="k" x="{lx:.1f}" y="{ly + 4:.1f}">{letters[kind]}</text>')
    for v in g.vs:
        x, y = P[v]
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{_R}"/><text x="{x:.1f}" y="{y + 5:.1f}">{v}</text>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
           'font-family="JetBrains Mono, Menlo, Consolas, monospace" font-size="14" text-anchor="middle">'
           '<defs><marker id="a" markerWidth="9" markerHeight="8" refX="8" refY="4" orient="auto">'
           '<path d="M0,0 L9,4 L0,8 z" fill="#111"/></marker></defs>'
           '<style>line,path{stroke:#111;stroke-width:1.5}circle{fill:#fff;stroke:#111;stroke-width:1.5}'
           'text{fill:#111}.k{font-size:13px;font-weight:700;fill:#b00}</style>' + "".join(parts) + "</svg>")
    name = "gr-" + hashlib.sha1(svg.encode()).hexdigest()[:12] + ".svg"
    path = FIG_DIR / name
    if not path.exists() or path.read_text() != svg:
        FIG_DIR.mkdir(parents=True, exist_ok=True)
        path.write_text(svg)
    sep = " → " if g.directed else "—"
    alt = (title or "Graphe") + " : " + ("orienté" if g.directed else "non orienté") + f", sommets {fmt(g.vs)} ; " + \
        ("arcs " if g.directed else "arêtes ") + ", ".join(f"{a}{sep}{b}" for a, b in g.edges)
    return f"![{alt}]({FIG_URL}{name})"


def forest_fig(g, s):
    """Spanning forest of the depth-first search from s with the other arcs dashed and typed (A, R, C)."""
    d = DFS(g, s)
    return gfig(g, _forest_pos(d.roots, d.children), d.kind, "Forêt couvrante")


def tree_fig(g, root):
    return gfig(g, _tree_pos(g, root))


def desc(g):
    """The statement words of a graph (copy-for-AI text stays complete)."""
    if g.directed:
        return f"$S=\\{{{fmt(g.vs)}\\}}$ et $A=\\{{{', '.join(f'({a},{b})' for a, b in g.edges)}\\}}$"
    return f"$S=\\{{{fmt(g.vs)}\\}}$ et $A=\\{{{', '.join(f'\\{{{a},{b}\\}}' for a, b in g.edges)}\\}}$"


# ---------------------------------------------------------------- exercise builders


def v(id, enonce, calc, ans, sol, src=None, duree=None):
    e = {"id": id, "kind": "value", "enonce": enonce, "calc": calc, "ans": ans, "sol": sol}
    if src:
        e["src"] = src
    if duree:
        e["duree"] = duree
    return e


def o(id, enonce, sol, src=None, duree=None):
    e = {"id": id, "kind": "open", "enonce": enonce, "sol": sol}
    if src:
        e["src"] = src
    if duree:
        e["duree"] = duree
    return e


def _v(d):
    """Variant from a dict (enonce, calc, ans, sol)."""
    return {k: d[k] for k in ("enonce", "calc", "ans", "sol")}


CALLS = {"len", "range", "min", "max", "Graph", "Queue", "Exception"}
METHODS = {"append", "pop", "insert", "enqueue", "dequeue", "isempty", "addedge"}


def _api(code):
    """Exam annex: lists (len, append, pop, insert), range, min, max, Queue, Graph; no slice, `in` test, comprehension."""
    tree = ast.parse(code)
    defined = {n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}
    for n in ast.walk(tree):
        bad = None
        if isinstance(n, ast.Call):
            f = n.func
            if isinstance(f, ast.Name) and f.id not in CALLS | defined:
                bad = f"function {f.id}"
            elif isinstance(f, ast.Attribute) and f.attr not in METHODS:
                bad = f"method {f.attr}"
        elif isinstance(n, ast.Slice):
            bad = "slice"
        elif isinstance(n, ast.Compare) and any(isinstance(op, (ast.In, ast.NotIn)) for op in n.ops):
            bad = "`in` test"
        elif isinstance(n, (ast.ListComp, ast.GeneratorExp, ast.SetComp, ast.DictComp, ast.Import, ast.ImportFrom, ast.Lambda)):
            bad = type(n).__name__
        assert not bad, f"exam rule broken ({bad}) in:\n{code}"


NSG = {"Graph": Graph, "Queue": Queue, "GC": GC.graph(), "G3CC": G3CC.graph(), "T1": T1.graph(), "T2": T2.graph(),
       "U1": U1.graph(), "U2": U2.graph(), "D1": D1.graph(), "D2": D2.graph(), "K4": K4.graph(), "DAG": DAG.graph(),
       "C6": C6.graph(), "TREE": TREE.graph(), "TREE2": TREE2.graph()}


def _w(enonce, code, tests, sol):
    code = code.strip()
    _api(code)
    ns = dict(NSG)
    exec(code, ns)
    for line, exp in tests:
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                got = repr(eval(line, ns))
        except Exception as e:  # noqa: BLE001 - the statement shows the exception message
            got = f"Exception: {e}"
        assert got == exp, f"{line}: got {got}, expected {exp}\n{code}"
    return {"enonce": f"{enonce}\n\nExemples d'applications :\n\n{_out(_session(tests))}",
            "sol": _py(code) + (f"\n\n{sol}" if sol else "")}


def w(id, enonce, code, tests, sol="", src=None, duree=8):
    CHECKED.append(id)
    e = {"id": id, "kind": "open", **_w(enonce, code, tests, sol), "duree": duree}
    if src:
        e["src"] = src
    return e


ANNEXE = ("Les classes `Graph` (attributs `order`, `directed`, `adjlists` ; méthodes `addedge(src, dst)`, `addvertex()`) et "
          "`Queue` (`Queue()`, `enqueue`, `dequeue`, `isempty`) sont supposées importées ; les listes d'adjacence sont en ordre "
          "croissant. Fonctions permises : `len`, `range`, `min`, `max`, `append`, `pop`, `insert` ; pas de compréhension.")

S_P17 = "Partiel P3 algo, 19 décembre 2017 (Past-Exams S3/Finals/Algo/2021)"
S_P18 = "Partiel P3 algo, 18 décembre 2018 (Past-Exams S3/Finals/Algo/2022)"
S_P19 = "Partiel P3 algo, 17 décembre 2019 (Past-Exams S3/Finals/Algo/2023)"
S_R19 = "Rattrapage P3 algo, 14 mai 2019 (Past-Exams S3/Finals/Algo/2023#)"
S_P21 = "Partiel P3 algo, 5 janvier 2021 (Past-Exams S3/Finals/Algo/2024)"
S_R21 = "Rattrapage P3 algo, 12 mai 2021 (Past-Exams S3/Finals/Algo/2025#)"
S_C19 = "Contrôle C3 algo, novembre 2019 (Past-Exams S3/Midterms/Algo/2023)"
S_C21 = "Contrôle C3 algo, 9 novembre 2021 (Past-Exams S3/Midterms/Algo/2025)"
S_R19B = "Rattrapage P3 algo, 15 mai (Past-Exams S3/Finals/Algo/2022#)"

# ---------------------------------------------------------------- course

NOTIONS = [
    {"id": "rappel-complexite", "titre": "Compter les opérations d'une boucle (rappel S1)",
     "formule": r"`range(a, b, p)` : $\lceil\frac{b-a}p\rceil$ tours · deux boucles imbriquées : $n^2$ · boucle triangulaire : $\frac{n(n-1)}2$ · doublement : $\lceil\log_2 n\rceil$",
     "exemple": r"`for i in range(n): for j in range(i + 1, n):` fait $\frac{n(n-1)}2$ tours ; pour $n=10$ : $45$",
     "cours": r"La complexité d'un parcours de graphe se lit sur ces boucles : parcourir toute une matrice $n\times n$ coûte $n^2$, parcourir toutes les listes d'adjacence coûte $n+m$. Rappel S1 : parcours « Algorithmique Python » (`algo-s1-python`)."},
    {"id": "rappel-files-arbres", "titre": "Files, piles et parcours d'arbres généraux (rappel S1/S2)",
     "formule": r"file : premier entré, premier sorti (`enqueue`, `dequeue`) · pile : dernier entré, premier sorti · préfixe : racine puis fils · suffixe : fils puis racine · largeur : niveau par niveau (file)",
     "exemple": r"Arbre de racine $0$ et de fils $1,2,3$ : préfixe $0,1,\dots$ ; largeur $0,1,2,3,\dots$",
     "cours": r"Un graphe se parcourt comme un arbre général, avec deux différences : un sommet peut être rencontré plusieurs fois (il faut le marquer) et il n'y a pas de racine (on choisit le départ). Le parcours en largeur utilise une file, le parcours en profondeur la récursion (donc une pile). Rappels : parcours « Types algébriques abstraits » (`algo-s1-taa`) et « Arbres binaires et généraux » (`algo-s2-abg`)."},
    {"id": "terminologie", "titre": "Terminologie : ordre, degrés, graphes complets",
     "formule": r"$G=\langle S,A\rangle$, ordre $n=|S|$ · non orienté : $\sum_x d^\circ(x)=2m$ · orienté : $\sum d^{\circ+}=\sum d^{\circ-}=m$ · $d^\circ(x)=d^{\circ+}(x)+d^{\circ-}(x)$ · complet : $m=\binom n2$ (non orienté), $n(n-1)$ (orienté)",
     "exemple": r"Graphe simple d'ordre $9$ complet : $\binom92=36$ arêtes",
     "cours": r"Arête $\{x,y\}$ (non orienté) ou arc $(x,y)$ (orienté, $x$ extrémité initiale, $y$ terminale). Un sommet de degré nul est isolé. Une boucle compte double dans le degré. Un graphe simple n'a ni boucle ni arête multiple ; un $p$-graphe a au plus $p$ arcs de mêmes extrémités. Un sous-graphe garde un sous-ensemble de sommets et toutes leurs liaisons ; un graphe partiel garde tous les sommets et une partie des liaisons."},
    {"id": "chemins", "titre": "Chemins, chaînes, cycles et puissances de la matrice d'adjacence",
     "formule": r"chemin de longueur $k$ : $(s_0,\dots,s_k)$ avec $s_i\to s_{i+1}$ arc · nombre de chemins de longueur $k$ de $x$ à $y$ : $(M^k)_{xy}$ · accessibilité : $(I+M)^{n-1}$",
     "exemple": r"$(M^2)_{02}$ compte les sommets $z$ avec $0\to z\to2$",
     "cours": r"Un chemin élémentaire ne répète aucun sommet. Un circuit (graphe orienté) ou un cycle (non orienté) est un chemin fermé aux arcs ou arêtes distincts. Dans un graphe non orienté, $\operatorname{tr}(M^3)/6$ est le nombre de triangles. Il existe un chemin de $x$ à $y$ si et seulement si $((I+M)^{n-1})_{xy}>0$."},
    {"id": "representations", "titre": "Représentations : matrice et listes d'adjacence",
     "formule": r"matrice : $n^2$ cases, arc $(x,y)$ en $O(1)$, successeurs en $O(n)$, parcours complet $O(n^2)$ · listes : $n+m$ éléments ($n+2m$ non orienté), arc $(x,y)$ en $O(d^{\circ+}(x))$, parcours complet $O(n+m)$",
     "exemple": r"Graphe non orienté simple de $11$ arêtes : $22$ cases à $1$ dans la matrice (symétrique), $22$ successeurs dans les listes",
     "cours": r"Matrice : booléens pour un graphe simple, entiers pour un multigraphe ; symétrique pour un graphe non orienté ; matrice de coûts pour un graphe valué. Listes : chaque arête $x$—$y$ apparaît deux fois. Pour avoir les prédécesseurs avec des listes, il faut des listes de prédécesseurs ou un parcours complet. Les sommets doivent être numérotés (de $0$ à $n-1$ en Python)."},
    {"id": "parcours-largeur", "titre": "Parcours en largeur (BFS)",
     "formule": r"file : enfiler le départ, marquer · défiler $x$, enfiler ses successeurs non marqués (en les marquant) · distances par niveaux · $O(n+m)$ (listes), $O(n^2)$ (matrice)",
     "exemple": r"Graphe $0$—$1$, $0$—$2$, $1$—$3$ : ordre $0,1,2,3$ ; distances $0,1,1,2$",
     "cours": r"On marque un sommet **au moment où on l'enfile**, pas quand on le défile : sinon un sommet peut être enfilé deux fois. L'algorithme d'appel relance le parcours sur chaque sommet non marqué pour obtenir un parcours complet ; l'ordre de rencontre dépend de l'ordre des listes (croissant par convention). Le parcours en largeur donne les plus courtes chaînes en nombre d'arêtes."},
    {"id": "parcours-profondeur", "titre": "Parcours en profondeur (DFS) : préfixe et suffixe",
     "formule": r"marquer $x$ (préfixe) · pour chaque successeur non marqué : récursion · fin de $x$ (suffixe) · $O(n+m)$ (listes), $O(n^2)$ (matrice)",
     "exemple": r"Arbre $0$—$1$, $0$—$2$, $2$—$3$ : préfixe $0,1,2,3$ ; suffixe $1,3,2,0$",
     "cours": r"Le préfixe est l'ordre de première rencontre, le suffixe l'ordre de dernière rencontre (le sommet est terminé quand tous ses successeurs sont traités). Avec un compteur unique, chaque sommet reçoit deux numéros : `pref` et `suff`. Le parcours est une extension du parcours d'un arbre général ; la forêt couvrante a une racine par lancement depuis l'algorithme d'appel."},
    {"id": "classification", "titre": "Forêt couvrante et classification des arcs",
     "formule": r"couvrant : $y$ découvert depuis $x$ · avant : $y$ descendant non direct de $x$ ($\text{pref}[x]<\text{pref}[y]$, $\text{suff}[y]<\text{suff}[x]$) · arrière : $y$ ascendant de $x$ ($\text{pref}[y]<\text{pref}[x]$, $\text{suff}[x]<\text{suff}[y]$) · croisé : ni l'un ni l'autre",
     "exemple": r"$x$ atteint $y$ déjà marqué mais non terminé : arc arrière, donc circuit",
     "cours": r"Dans un graphe non orienté, toute arête qui n'est pas couvrante est un arc arrière (pas d'arc avant ni croisé). Un graphe orienté est sans circuit si et seulement si le parcours en profondeur ne rencontre aucun arc arrière. Dans un graphe sans circuit, l'ordre suffixe inverse est un tri topologique."},
    {"id": "connexite", "titre": "Connexité statique : composantes, fermeture transitive, Warshall",
     "formule": r"connexe : une seule composante · chaque arbre de la forêt couvrante = une composante · Warshall : $C[x,y]\leftarrow C[x,y]\lor(C[x,i]\land C[i,y])$, $O(n^3)$ · connexe $\iff$ fermeture complète",
     "exemple": r"Fermeture à blocs de $4$, $6$ et $4$ sommets : $3$ composantes, $16+36+16=68$ cases à $1$",
     "cours": r"On numérote les sommets par composante (vecteur d'entiers au lieu du vecteur de booléens) ; pour tester la connexité un seul parcours depuis un sommet quelconque suffit. La fermeture transitive d'un graphe non orienté est une matrice de blocs de 1 : le rang de la matrice est le nombre de composantes. Warshall sert aussi aux graphes orientés (chemins)."},
    {"id": "trouver-reunir", "titre": "Connexité évolutive : trouver-réunir",
     "formule": r"vecteur des pères $p$ : racine $p[x]=-1$ (ou $-$taille avec l'union pondérée) · `trouver` remonte jusqu'à la racine · `reunir` : $p[r_y]\leftarrow r_x$ · union pondérée : le petit sous la racine du grand · compression : tout le chemin pointe sur la racine",
     "exemple": r"$p=[-1,0,0,-1]$ : composantes $\{0,1,2\}$ et $\{3\}$",
     "cours": r"Une composante = un arbre, de racine son représentant. Sans optimisation, la hauteur peut valoir $n-1$. Avec l'union pondérée seule la hauteur est au plus $\log_2 n$ ; avec la compression des chemins elle tend vers 2. Pour savoir si un vecteur est possible, chaque arbre doit couvrir exactement une composante, et avec l'union pondérée chaque racine porte l'opposé de la taille de son arbre."},
    {"id": "applications", "titre": "Applications : distances, bipartition, cycles, tri topologique",
     "formule": r"distance (BFS) · excentricité $\max_y d(x,y)$, rayon $=\min$, diamètre $=\max$, centre · biparti : 2-coloration par BFS · arbre : connexe et $m=n-1$ · acyclique : DFS sans arc arrière · Euler : connexe et $0$ ou $2$ sommets de degré impair",
     "exemple": r"Chaîne $0$—$1$—$2$ : excentricités $2,1,2$, rayon $1$, centre $\{1\}$, diamètre $2$",
     "cours": r"Chaque problème est un parcours modifié : levels = BFS qui range les sommets par distance ; bipartite = BFS en alternant deux couleurs, échec dès qu'une arête relie deux sommets de même couleur ; cycle = DFS qui repère une arête vers un sommet déjà vu autre que le père ; acyclique orienté = DFS avec trois états (non vu, en cours, terminé) ; tri topologique = ordre suffixe inverse."},
]

# ---------------------------------------------------------------- level 1 : counting loops (S1 reminder)


def _run(code):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        exec(code, {})
    return buf.getvalue().strip()


def loop_ex(id, code, calc, ans, sol, variants):
    """`value` exercise on a program that prints a counter; the program is run to check `ans`."""
    def build(c, ca, a, s):
        assert _run(c) == a, f"{c}: prints {_run(c)}, expected {a}"
        return {"enonce": "Quelle valeur affiche ce programme ?\n\n" + _py(c), "calc": ca, "ans": a, "sol": s}
    main = build(code, calc, ans, sol)
    return v(id, main["enonce"], calc, ans, sol), [_v(build(*x)) for x in variants]


L1 = [
    loop_ex("g11", "c = 0\nfor i in range(10):\n    for j in range(i + 1, 10):\n        c += 1\nprint(c)",
            "summation(9-i,(i,0,9))", "45",
            r"Pour $i$ de $0$ à $9$ la boucle interne fait $9-i$ tours : $9+8+\dots+0=\frac{10\times9}2=45$. C'est le nombre de paires $\{i,j\}$ : la forme du parcours de la moitié d'une matrice symétrique.",
            [("c = 0\nfor i in range(12):\n    for j in range(i + 1, 12):\n        c += 1\nprint(c)", "summation(11-i,(i,0,11))", "66",
              r"$11+10+\dots+0=\frac{12\times11}2=66$.")]),
    loop_ex("g12", "c = 0\nfor i in range(3, 100, 7):\n    c += 1\nprint(c)", "floor(Rational(96,7))+1", "14",
            r"`range(3, 100, 7)` donne $3,10,\dots,94$ : $\lfloor\frac{99-3}7\rfloor+1=13+1=14$ valeurs.",
            [("c = 0\nfor i in range(2, 60, 5):\n    c += 1\nprint(c)", "floor(Rational(57,5))+1", "12",
              r"$2,7,\dots,57$ : $\lfloor\frac{59-2}5\rfloor+1=11+1=12$.")]),
    loop_ex("g13", "i = 1\nc = 0\nwhile i < 1000:\n    i = i * 2\n    c += 1\nprint(c)", "ceiling(log(1000)/log(2))", "10",
            r"On double jusqu'à dépasser $1000$ : $2^{10}=1024\ge1000$ et $2^9=512<1000$ ; $\lceil\log_21000\rceil=10$ tours.",
            [("i = 1\nc = 0\nwhile i < 5000:\n    i = i * 2\n    c += 1\nprint(c)", "ceiling(log(5000)/log(2))", "13",
              r"$2^{13}=8192\ge5000$ et $2^{12}=4096<5000$ : $13$ tours.")]),
    loop_ex("g14", "n = 200\nc = 0\nfor x in range(n):\n    for y in range(n):\n        c += 1\nprint(c)", "200**2", "40000",
            r"Deux boucles de $n$ tours imbriquées : $n^2=40000$. C'est le coût d'un parcours complet d'une matrice d'adjacence de $200$ sommets.",
            [("n = 30\nc = 0\nfor x in range(n):\n    for y in range(n):\n        c += 1\nprint(c)", "30**2", "900", r"$n^2=900$.")]),
]

# ---------------------------------------------------------------- level 2 : trees and queues (S1/S2 reminder)


def tree_ex(id, kind, g, root, label):
    mode = {"pre": "dfs", "suf": "suf", "lar": "bfs"}[kind]
    d = DFS(g, root)
    seq = {"pre": d.pre, "suf": d.suf, "lar": bfs_full(g, root)}[kind]
    name = {"pre": "préfixe", "suf": "suffixe", "lar": "en largeur"}[kind]
    enonce = (f"Arbre général de racine ${root}$ (les fils sont rangés dans l'ordre croissant des numéros).\n\n{tree_fig(g, root)}\n\n"
              f"Donner l'ordre {name} des nœuds.")
    sol = (f"Ordre {name} : ${fmt(seq)}$. " + {
        "pre": r"On note la racine, puis on descend dans chaque fils en entier avant de passer au suivant.",
        "suf": r"On note un nœud après tous ses fils : la racine est la dernière.",
        "lar": r"On range les nœuds niveau par niveau avec une file : on défile $x$ et on enfile ses fils."}[kind])
    calc = f'parc("{mode}",{g.adjs()},{root},{g.base})'
    return v(id, enonce, calc, mrow(seq), sol), calc, mrow(seq)


def _vtree(kind, g, root):
    e, calc, ans = tree_ex("_", kind, g, root, "")
    return _v(e)


def queue_sim(ops, kind):
    """Result of a sequence of operations on a queue or a stack: list of the dequeued/popped values."""
    box, out = collections.deque(), []
    for op in ops:
        if isinstance(op, int):
            box.append(op)
        else:
            out.append(box.popleft() if kind == "file" else box.pop())
    return out, list(box)


def sim_ex(id, ops, kind):
    out, rest = queue_sim(ops, kind)
    other, _ = queue_sim(ops, "pile" if kind == "file" else "file")
    txt = ", ".join(f"`push({op})`" if isinstance(op, int) and kind == "pile" else
                    f"`enqueue({op})`" if isinstance(op, int) else ("`pop()`" if kind == "pile" else "`dequeue()`") for op in ops)
    name = "pile" if kind == "pile" else "file"
    enonce = f"On part d'une {name} vide et on exécute : {txt}. Donner, dans l'ordre, les valeurs retirées et le contenu final."
    first = "dernier entré, premier sorti" if kind == "pile" else "premier entré, premier sorti"
    sol = (f"Une {name} est « {first} ». Valeurs retirées : ${fmt(out)}$ ; contenu final (du premier au dernier entré) : ${fmt(rest) or 'vide'}$. "
           f"Avec l'autre structure on aurait obtenu ${fmt(other)}$ : c'est la différence entre largeur (file) et profondeur (pile).")
    return o(id, enonce, sol)


L2 = []
_t = tree_ex("g21", "pre", TREE, 0, "")
L2.append(_t[0])
L2.append(tree_ex("g22", "suf", TREE, 0, "")[0])
L2.append(tree_ex("g23", "lar", TREE, 0, "")[0])
L2.append(sim_ex("g24", [4, 7, 2, None, 9, None, 5, None, None], "file"))
L2.append(sim_ex("g25", [4, 7, 2, None, 9, None, 5, None, None], "pile"))
V2 = {"g21": [_vtree("pre", TREE2, 0)], "g22": [_vtree("suf", TREE2, 0)], "g23": [_vtree("lar", TREE2, 0)]}

# ---------------------------------------------------------------- level 3 : degrees


def deg_ex(id, g, x):
    d = len(g.adj[x])
    nb = [y for y in g.adj[x]]
    calc = f"sum({g.mat()}.row({x - g.base}))"
    enonce = f"Soit le graphe non orienté simple ci-dessous.\n\n{gfig(g, T2_POS if g is T2 else None)}\n\nQuel est le degré du sommet ${x}$ ?"
    sol = f"Les voisins de ${x}$ sont ${fmt(nb)}$ : $d^\\circ({x})={d}$. Dans la matrice d'adjacence, c'est la somme de la ligne ${x}$."
    return v(id, enonce, calc, str(d), sol)


def hand_ex(id, g):
    degs = [len(g.adj[x]) for x in g.vs]
    m = len(g.edges)
    assert sum(degs) == 2 * m
    enonce = (f"Un graphe non orienté simple d'ordre ${len(g.vs)}$ a pour degrés ${fmt(degs)}$ (sommets $0$ à ${len(g.vs) - 1}$). "
              "Combien d'arêtes a-t-il ?")
    sol = f"$\\sum d^\\circ(x)=2m$ : la somme des degrés vaut ${sum(degs)}$, donc $m={m}$."
    return v(id, enonce, f"sum({mrow(degs)})/2", str(m), sol)


def indeg_ex(id, g, x, out=False):
    nb = g.adj[x] if out else [a for a, b in g.edges if b == x]
    word = "extérieur $d^{\\circ+}$" if out else "intérieur $d^{\\circ-}$"
    axis = "row" if out else "col"
    enonce = (f"Soit le graphe orienté ci-dessous.\n\n{gfig(g)}\n\nQuel est le demi-degré {word} du sommet ${x}$ ?")
    sol = (f"Les {'successeurs' if out else 'prédécesseurs'} de ${x}$ sont ${fmt(nb) or 'aucun'}$ : "
           f"{'$d^{\\circ+}' if out else '$d^{\\circ-}'}({x})={len(nb)}$. Dans la matrice : somme de la {'ligne' if out else 'colonne'} ${x}$.")
    return v(id, enonce, f"sum({g.mat()}.{axis}({x - g.base}))", str(len(nb)), sol)


def complete_ex(id, n, directed):
    m = n * (n - 1) if directed else n * (n - 1) // 2
    enonce = (f"Combien d'{'arcs' if directed else 'arêtes'} a un graphe {'orienté' if directed else 'non orienté'} simple complet d'ordre ${n}$ ?"
              + (" (une liaison dans chaque sens entre deux sommets distincts)" if directed else ""))
    sol = (f"Chaque sommet est relié aux $n-1={n - 1}$ autres : $n(n-1)={n * (n - 1)}$ extrémités "
           + ("comptées comme des arcs sortants : $" + str(m) + "$ arcs." if directed else f"; chaque arête en compte deux : $\\binom{{{n}}}2={m}$ arêtes."))
    return v(id, enonce, f"{n}*({n}-1)" if directed else f"binomial({n},2)", str(m), sol)


T2_POS = {0: (60, 40), 4: (130, 20), 1: (20, 110), 3: (100, 110), 9: (200, 20), 2: (230, 90), 5: (310, 60), 6: (270, 160), 7: (370, 130),
          8: (440, 60)}
L3 = [deg_ex("g31", T2, 7), hand_ex("g32", T2), indeg_ex("g33", T1, 4), indeg_ex("g34", T1, 0, True), complete_ex("g35", 9, False)]
V3 = {
    "g31": [_v(deg_ex("_", U1, 4))],
    "g32": [_v(hand_ex("_", U2))],
    "g33": [_v(indeg_ex("_", D1, 3))],
    "g34": [_v(indeg_ex("_", D1, 2, True))],
    "g35": [_v(complete_ex("_", 12, False)), _v(complete_ex("_", 7, True))],
}

# ---------------------------------------------------------------- level 4 : paths and matrix powers


def paths_ex(id, g, pos, k, x, y):
    M = g.mat()
    res = int((__import__("sympy").Matrix(g.rows()) ** k)[x, y])
    brute = sum(1 for seq in itertools.product(g.vs, repeat=k - 1) if all(b in g.adj[a] for a, b in zip((x,) + seq, seq + (y,))))
    assert res == brute
    enonce = (f"Soit le graphe orienté ci-dessous, de matrice d'adjacence $M$.\n\n{gfig(g, pos)}\n\n"
              f"Combien y a-t-il de chemins de longueur ${k}$ (sommets non nécessairement distincts) de ${x}$ vers ${y}$ ?")
    sol = (f"Le coefficient $(M^{k})_{{{x}{y}}}$ compte les chemins de longueur ${k}$ de ${x}$ à ${y}$. Un calcul de $M^{k}$ donne ${res}$. "
           "Vérification à la main : on additionne sur le sommet intermédiaire $z$ le produit « arcs $x\\to z$ » par « chemins de $z$ à $y$ ».")
    return v(id, enonce, f"({M}**{k})[{x},{y}]", str(res), sol)


def triangles_ex(id, g):
    import sympy as sp
    A = sp.Matrix(g.rows())
    t = int((A ** 3).trace() // 6)
    brute = sum(1 for a, b, c in itertools.combinations(g.vs, 3) if b in g.adj[a] and c in g.adj[a] and c in g.adj[b])
    assert t == brute
    enonce = f"Combien le graphe non orienté ci-dessous contient-il de triangles (cycles de longueur $3$) ?\n\n{gfig(g, U1_POS if g is U1 else None)}"
    sol = (f"$(A^3)_{{xx}}$ compte les chemins fermés de longueur $3$ issus de $x$ ; un triangle est compté $3$ fois (point de départ) $\\times2$ (sens) $=6$ fois "
           f"dans la trace : $\\operatorname{{tr}}(A^3)/6={t}$.")
    return v(id, enonce, f"({g.mat()}**3).trace()/6", str(t), sol)


def reach_ex(id, g, pos, x, y):
    import sympy as sp
    n = len(g.vs)
    R = (sp.eye(n) + sp.Matrix(g.rows())) ** (n - 1)
    ok = 1 if R[x - g.base, y - g.base] > 0 else 0
    d = bfs(g, x)[1]
    assert ok == (y in d)
    enonce = f"Soit le graphe orienté ci-dessous.\n\n{gfig(g, pos)}\n\nExiste-t-il un chemin de ${x}$ vers ${y}$ ? (répondre $1$ si oui, $0$ sinon)"
    sol = (f"Il existe un chemin de ${x}$ à ${y}$ si et seulement si $((I+M)^{{{n - 1}}})_{{{x}{y}}}>0$ (un chemin élémentaire a au plus $n-1$ arcs). "
           f"Ici la réponse est {ok} : " + (f"par exemple en $d(x,y)={d[y]}$ arcs." if ok else "aucun sommet atteint depuis $x$ n'est $y$."))
    return v(id, enonce, f"Min(1,((eye({n})+{g.mat()})**{n - 1})[{x - g.base},{y - g.base}])", str(ok), sol)


M6_POS = {0: (40, 30), 1: (130, 30), 2: (130, 120), 3: (230, 120), 4: (320, 120), 5: (320, 30)}
L4 = [paths_ex("g41", M5, M5_POS, 2, 0, 3), paths_ex("g42", M5, M5_POS, 3, 0, 4), triangles_ex("g43", U1), reach_ex("g44", M6, M6_POS, 3, 0)]
V4 = {
    "g41": [_v(paths_ex("_", M5, M5_POS, 2, 1, 4))],
    "g42": [_v(paths_ex("_", M5, M5_POS, 3, 2, 1))],
    "g43": [_v(triangles_ex("_", K4))],
    "g44": [_v(reach_ex("_", M6, M6_POS, 0, 5))],
}
L4.append(reach_ex("g45", M6, M6_POS, 5, 4))
V4["g45"] = [_v(reach_ex("_", M6, M6_POS, 4, 0))]

# ---------------------------------------------------------------- level 5 : representations


def sizes_ex(id, kind, n, m, directed):
    if kind == "cases":
        a = n * n
        enonce = f"Combien de cases contient la matrice d'adjacence d'un graphe d'ordre ${n}$ ?"
        sol = f"Une matrice carrée $n\\times n$ : ${n}^2={a}$ cases, quel que soit le nombre de liaisons."
        calc = f"{n}**2"
    elif kind == "ones":
        a = m if directed else 2 * m
        enonce = (f"Un graphe {'orienté' if directed else 'non orienté'} simple d'ordre ${n}$ a ${m}$ {'arcs' if directed else 'arêtes'}. "
                  "Combien de cases de sa matrice d'adjacence valent $1$ (vrai) ?")
        sol = ("Un arc $(x,y)$ met un $1$ en $(x,y)$ : " + (f"${m}$ cases." if directed else
               f"une arête $\\{{x,y\\}}$ met un $1$ en $(x,y)$ et en $(y,x)$ (matrice symétrique) : $2m={a}$ cases."))
        calc = f"{m}" if directed else f"2*{m}"
    else:
        a = m if directed else 2 * m
        enonce = (f"Un graphe {'orienté' if directed else 'non orienté'} simple d'ordre ${n}$ a ${m}$ {'arcs' if directed else 'arêtes'}. "
                  "Combien de successeurs (éléments) sont stockés au total dans ses listes d'adjacence ?")
        sol = ("Chaque arc apparaît une fois, dans la liste de son extrémité initiale : " + (f"${m}$." if directed else
               f"chaque arête apparaît deux fois ($y$ dans la liste de $x$ et $x$ dans celle de $y$) : $2m={a}$.") +
               f" Place totale : $n+{'m' if directed else '2m'}$ en ordre de grandeur, contre $n^2$ pour la matrice.")
        calc = f"{m}" if directed else f"2*{m}"
    return v(id, enonce, calc, str(a), sol)


def read_ex(id, g, x, y):
    d = len(g.adj[x])
    mat = g.rows()
    lines = "\n".join("$" + " ".join(str(c) for c in r) + "$" for r in mat)
    enonce = (f"Un graphe orienté d'ordre ${len(g.vs)}$ (sommets $0$ à ${len(g.vs) - 1}$) est représenté par listes d'adjacence : "
              + ", ".join(f"${a}:\\{{{fmt(g.adj[a])}\\}}$" for a in g.vs)
              + f".\n\nQuel est, au pire, le nombre de successeurs à examiner pour décider si $({x},{y})$ est un arc ?")
    sol = (f"On parcourt la liste de ${x}$ jusqu'à trouver ${y}$ ou la fin : au pire $d^{{\\circ+}}({x})={d}$ éléments, contre $1$ case lue avec une matrice. "
           f"Ici ${y}$ " + ("est" if y in g.adj[x] else "n'est pas") + f" dans la liste : $({x},{y})$ " + ("est" if y in g.adj[x] else "n'est pas") + " un arc.")
    return v(id, enonce, f"len({g.adjs()}[{x}])", str(d), sol)


def conv_ex(id, g, pos=None):
    rows = g.rows()
    mat = "\n".join(f"{x}: " + " ".join(map(str, r)) for x, r in zip(g.vs, rows))
    lists = "\n".join(f"{x} : {{{fmt(g.adj[x])}}}" for x in g.vs)
    enonce = f"Donner la matrice d'adjacence et les listes d'adjacence du graphe {'orienté' if g.directed else 'non orienté'} suivant.\n\n{gfig(g, pos)}"
    sol = (f"Listes (successeurs en ordre croissant) :\n\n{_out(lists)}\n\nMatrice (ligne = origine, colonne = extrémité ; $1$ = liaison) :\n\n{_out(mat)}\n\n"
           + ("La matrice est symétrique et chaque arête apparaît deux fois dans les listes." if not g.directed else
              "Les sommes des lignes sont les demi-degrés extérieurs, celles des colonnes les demi-degrés intérieurs.")
           + f" Nombre de $1$ : ${sum(map(sum, rows))}$.")
    return o(id, enonce, sol)


L5 = [sizes_ex("g51", "cases", 1000, 0, False), sizes_ex("g52", "ones", 10, 11, False), sizes_ex("g53", "list", 10, 11, False),
      read_ex("g54", T1, 0, 5), conv_ex("g55", T1), conv_ex("g56", T2, T2_POS)]
V5 = {
    "g51": [_v(sizes_ex("_", "cases", 365, 0, False))],
    "g52": [_v(sizes_ex("_", "ones", 12, 20, False)), _v(sizes_ex("_", "ones", 8, 15, True))],
    "g53": [_v(sizes_ex("_", "list", 20, 33, False)), _v(sizes_ex("_", "list", 20, 33, True))],
    "g54": [_v(read_ex("_", D2, 2, 6))],
}

# ---------------------------------------------------------------- levels 6 and 7 : BFS and DFS orders


def order_ex(id, what, g, s, pos=None, src=None):
    d = DFS(g, s)
    if what == "bfs":
        seq, name, mode = bfs_full(g, s), "parcours en largeur", "bfs"
        sol_how = ("On enfile le départ en le marquant ; on défile $x$ et on enfile ses successeurs non marqués dans l'ordre croissant, en les marquant. "
                   "Si des sommets restent, on relance depuis le plus petit non marqué.")
    elif what == "dfs":
        seq, name, mode = d.pre, "parcours en profondeur (ordre préfixe)", "dfs"
        sol_how = "On note un sommet à sa première rencontre, puis on descend dans son premier successeur non marqué ; au retour on passe au suivant."
    else:
        seq, name, mode = d.suf, "parcours en profondeur (ordre suffixe)", "suf"
        sol_how = "On note un sommet quand tous ses successeurs sont traités (dernière rencontre) : on remonte, le départ est noté en dernier pour son arbre."
    trace = ""
    if what == "bfs":
        q, seen, lines = [s], {s}, []
        for _ in range(len(g.vs) * 3):
            pass
        todo = [s] + [x for x in g.vs if x != s]
        seen2, lines = set(), []
        for st in todo:
            if st in seen2:
                continue
            seen2.add(st)
            queue = collections.deque([st])
            lines.append(f"- relance depuis ${st}$ : file $[{st}]$")
            while queue:
                x = queue.popleft()
                new = [y for y in g.adj[x] if y not in seen2]
                seen2 |= set(new)
                queue.extend(new)
                lines.append(f"- défiler ${x}$, enfiler " + (f"${fmt(new)}$" if new else "rien") + f" : file $[{fmt(queue)}]$")
        trace = "\n\n**Trace :**\n\n" + "\n".join(lines)
    enonce = (f"Soit le graphe {'orienté' if g.directed else 'non orienté'} ci-dessous ({desc(g)}). Les successeurs sont pris en ordre croissant.\n\n"
              f"{gfig(g, pos)}\n\nDonner l'ordre de rencontre des sommets pour un {name} complet depuis le sommet ${s}$ "
              f"(si des sommets restent non visités, on relance le parcours sur le plus petit d'entre eux).")
    sol = f"{sol_how}\n\nOrdre : ${fmt(seq)}$." + trace
    calc = f'parc("{mode}",{g.adjs()},{s},{g.base})'
    return v(id, enonce, calc, mrow(seq), sol, src=src)


def dist_ex(id, g, s, pos=None, what="vec"):
    order, dist = bfs(g, s)
    vec = [dist.get(x, -1) for x in g.vs]
    if what == "vec":
        enonce = (f"Soit le graphe ci-dessous. Donner le vecteur des distances (nombre minimal d'arêtes) du sommet ${s}$ à tous les sommets, "
                  f"dans l'ordre des sommets ${fmt(g.vs)}$ (écrire $-1$ pour un sommet inaccessible).\n\n{gfig(g, pos)}")
        sol = f"Un parcours en largeur depuis ${s}$ donne la distance du niveau de chaque sommet : ${fmt(vec)}$."
        calc, ans = f'parc("dist",{g.adjs()},{s},{g.base})', mrow(vec)
    else:
        exc = max(dist.values())
        enonce = (f"Soit le graphe non orienté connexe ci-dessous. Quelle est l'excentricité du sommet ${s}$ "
                  f"(plus grande distance de ${s}$ à un autre sommet) ?\n\n{gfig(g, pos)}")
        sol = f"Distances depuis ${s}$ : ${fmt(vec)}$. L'excentricité est le maximum : ${exc}$ (c'est le nombre de niveaux du parcours en largeur moins un)."
        calc, ans = f'Max(*parc("dist",{g.adjs()},{s},{g.base}))', str(exc)
    return v(id, enonce, calc, ans, sol)


def last_ex(id, g, s, pos=None):
    seq = bfs_full(g, s)
    enonce = (f"Dans le graphe ci-dessous, quel est le dernier sommet rencontré par un parcours en largeur complet depuis ${s}$ "
              f"(successeurs en ordre croissant) ?\n\n{gfig(g, pos)}")
    sol = f"Ordre de rencontre : ${fmt(seq)}$. Le dernier est ${seq[-1]}$ (le parcours en largeur finit par les sommets les plus éloignés)."
    return v(id, enonce, f'parc("bfs",{g.adjs()},{s},{g.base})[-1]', str(seq[-1]), sol)


L6 = [order_ex("g61", "bfs", GC, 0, GC_POS), dist_ex("g62", GC, 0, GC_POS), dist_ex("g63", GC, 0, GC_POS, "exc"),
      order_ex("g64", "bfs", T1, 0), last_ex("g65", GC, 6, GC_POS)]
V6 = {
    "g61": [_v(order_ex("_", "bfs", U1, 0, U1_POS))],
    "g62": [_v(dist_ex("_", U2, 4))],
    "g63": [_v(dist_ex("_", GC, 11, GC_POS, "exc"))],
    "g64": [_v(order_ex("_", "bfs", D2, 6))],
    "g65": [_v(last_ex("_", U1, 5, U1_POS))],
}
L7 = [order_ex("g71", "dfs", E21, 1, src=S_P17 + ", ex. 2 (graphe)"), order_ex("g72", "dfs", E25, 3, src=S_C21 + ", ex. 1.2"),
      order_ex("g73", "suf", E23, 1, src=S_P19 + ", ex. 1.2"), order_ex("g74", "suf", E21, 1), order_ex("g75", "dfs", T2, 7, T2_POS)]
V7 = {
    "g71": [_v(order_ex("_", "dfs", D1, 0))],
    "g72": [_v(order_ex("_", "dfs", D2, 3))],
    "g73": [_v(order_ex("_", "suf", U2, 0))],
    "g74": [_v(order_ex("_", "suf", D1, 0))],
    "g75": [_v(order_ex("_", "dfs", U1, 5, U1_POS))],
}

# ---------------------------------------------------------------- level 8 : forest and arc classification (open)


def tstr(d, v_):
    ch = d.children(v_)
    return f"{v_}" + (f"({', '.join(tstr(d, c) for c in ch)})" if ch else "")


def forest_ex(id, g, s, src=None, numbers=False, pos=None):
    d = DFS(g, s)
    by = collections.defaultdict(list)
    for (a, b), k in d.kind.items():
        by[k].append(f"({a},{b})" if g.directed else f"{{{a},{b}}}")
    rules = {"couvrant": "arcs de la forêt", "avant": "arcs avant (vers un descendant non direct)", "arrière": "arcs arrière (vers un ascendant)",
             "croisé": "arcs croisés (aucun lien de descendance)"}
    kinds = "\n".join(f"- {rules[k]} : {', '.join(by[k]) or 'aucun'}" for k in ("couvrant", "avant", "arrière", "croisé") if g.directed or k in ("couvrant", "arrière"))
    arrays = ""
    if numbers:
        arrays = ("\n\nAvec un compteur unique commençant à $1$ (numéro pris à la première puis à la dernière rencontre) :\n\n"
                  + _out("sommet : " + " ".join(f"{x:>3}" for x in g.vs) + "\npref   : " + " ".join(f"{d.pn[x]:>3}" for x in g.vs)
                         + "\nsuff   : " + " ".join(f"{d.sn[x]:>3}" for x in g.vs)))
    enonce = (f"Soit le graphe {'orienté' if g.directed else 'non orienté'} {desc(g)}.\n\n{gfig(g, pos)}\n\n"
              f"Dessiner la forêt couvrante associée au parcours en profondeur depuis le sommet ${s}$ (sommets choisis en ordre croissant) et ajouter les "
              "autres liaisons en les qualifiant par une légende explicite."
              + (" Donner aussi les tableaux `pref` et `suff` (compteur unique commençant à 1)." if numbers else ""))
    cyc = ("Il y a au moins un arc arrière : le graphe contient un circuit." if d.kind and any(k == "arrière" for k in d.kind.values()) and g.directed
           else ("Aucun arc arrière : le graphe orienté est sans circuit." if g.directed else
                 "Chaque arête non couvrante est un arc arrière : ici il y en a " + str(sum(1 for k in d.kind.values() if k == "arrière")) + "."))
    sol = (f"Ordre préfixe : ${fmt(d.pre)}$ ; ordre suffixe : ${fmt(d.suf)}$. Racines des arbres : ${fmt(d.roots)}$.\n\n"
           f"Forêt (notation racine(fils)) : `{' '.join(tstr(d, r) for r in d.roots)}`.\n\n{forest_fig(g, s)}\n\n{kinds}{arrays}\n\n{cyc} "
           "Légende du dessin : trait plein = arc couvrant, pointillé = autre arc, A = avant, R = arrière, C = croisé.")
    return o(id, enonce, sol, src=src, duree=8)


def rule_ex(id):
    enonce = (r"Lors d'un parcours en profondeur d'un graphe orienté avec un compteur unique, on obtient pour un arc $(x,y)$ non couvrant "
              r"$\text{pref}[y]<\text{pref}[x]$ et $\text{suff}[y]<\text{suff}[x]$. De quel type d'arc s'agit-il ? Donner les conditions des trois types d'arcs non couvrants.")
    sol = (r"**Arc croisé** : $y$ a été entièrement traité avant que $x$ soit découvert. Conditions : "
           r"avant : $\text{pref}[x]<\text{pref}[y]$ et $\text{suff}[y]<\text{suff}[x]$ ($y$ est un descendant de $x$) ; "
           r"arrière : $\text{pref}[y]<\text{pref}[x]$ et $\text{suff}[x]<\text{suff}[y]$ ($y$ est un ascendant de $x$) ; "
           r"croisé : $\text{pref}[y]<\text{pref}[x]$ et $\text{suff}[y]<\text{suff}[x]$. Dans un graphe non orienté il n'y a que des arcs arrière.")
    return o(id, enonce, sol)


L8 = [forest_ex("g81", E21, 1, S_P17 + ", ex. 2.3", numbers=False), forest_ex("g82", T1, 0, numbers=True),
      forest_ex("g83", T2, 0, numbers=False, pos=T2_POS), rule_ex("g84"), forest_ex("g85", E25, 3, numbers=True)]

# ---------------------------------------------------------------- level 9 : connected components, Warshall


def ncc_ex(id, g, pos=None):
    cc = comps(g)
    k = max(cc.values())
    enonce = f"Combien le graphe non orienté ci-dessous a-t-il de composantes connexes ? Le graphe est-il connexe ?\n\n{gfig(g, pos)}"
    parts = collections.defaultdict(list)
    for x in g.vs:
        parts[cc[x]].append(x)
    sol = (f"Un parcours complet lance une recherche par composante : " + " ; ".join(f"${{{fmt(p)}}}$".replace("{", "\\{").replace("}", "\\}") for p in parts.values())
           + f". Il y a ${k}$ composante(s) : le graphe " + ("est connexe." if k == 1 else "n'est pas connexe."))
    return v(id, enonce, f'Max(*parc("cc",{g.adjs()},{g.vs[0]},{g.base}))', str(k), sol)


def ccvec_ex(id, g, pos=None):
    cc = comps(g)
    vec = [cc[x] for x in g.vs]
    enonce = (f"Donner le vecteur des composantes du graphe ci-dessous : pour chaque sommet ${fmt(g.vs)}$ le numéro de sa composante, "
              f"numérotées dans l'ordre où le parcours les découvre en lançant la recherche sur les sommets non visités dans l'ordre croissant.\n\n{gfig(g, pos)}")
    sol = f"Vecteur : ${fmt(vec)}$. On remplace le vecteur de booléens par un vecteur d'entiers ; le numéro courant augmente à chaque relance de l'algorithme d'appel."
    return v(id, enonce, f'parc("cc",{g.adjs()},{g.vs[0]},{g.base})', mrow(vec), sol)


def conn_ex(id, g, pos=None):
    k = max(comps(g).values())
    ok = int(k == 1)
    enonce = f"Le graphe non orienté ci-dessous est-il connexe ? (répondre $1$ si oui, $0$ sinon)\n\n{gfig(g, pos)}"
    sol = ("Un seul parcours depuis un sommet quelconque suffit : le graphe est connexe si et seulement si tous les sommets sont marqués au retour. "
           f"Ici {'tous les sommets sont atteints depuis ' + str(g.vs[0]) if ok else 'des sommets restent non marqués'} : réponse ${ok}$.")
    return v(id, enonce, f'2-Min(2,Max(*parc("cc",{g.adjs()},{g.vs[0]},{g.base})))', str(ok), sol)


CL22 = [[1, 0, 1, 0, 0, 1, 1, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 0, 1, 1, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 1], [1, 0, 1, 0, 0, 1, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1, 1, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 1, 1, 0],
        [0, 1, 0, 1, 0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 1]]


def clos_rank_ex(id, rows, src=None, variant=False):
    import sympy as sp
    n = len(rows)
    seen, blocks = set(), []
    for i in range(n):
        if i not in seen:
            b = [j for j in range(n) if rows[i][j]]
            seen |= set(b)
            blocks.append(b)
    assert int(sp.Matrix(rows).rank()) == len(blocks)
    grid = "\n".join(" ".join(str(c) for c in r) for r in rows)
    enonce = (f"L'algorithme de Warshall appliqué à un graphe non orienté d'ordre ${n}$ (sommets $0$ à ${n - 1}$) a donné la matrice suivante "
              f"(ligne = sommet, $1$ = chaîne entre les deux sommets).\n\n{_out(grid)}\n\nCombien le graphe a-t-il de composantes connexes ?")
    sol = (f"La fermeture transitive est constituée de blocs de $1$ : deux sommets sont dans la même composante si et seulement si leur case vaut $1$. "
           f"Composantes : " + " ; ".join(f"$\\{{{fmt(b)}\\}}$" for b in blocks) + f". Il y en a ${len(blocks)}$, qui est aussi le rang de la matrice "
           f"(lignes identiques dans un même bloc). Nombre de $1$ : $" + "+".join(str(len(b) ** 2) for b in blocks) + f"={sum(map(sum, rows))}$.")
    return v(id, enonce, f"Matrix({rows}).rank()".replace(" ", ""), str(len(blocks)), sol, src=src)


def clos_ones_ex(id, rows):
    n = len(rows)
    enonce = (f"Un graphe non orienté d'ordre ${n}$ a pour composantes connexes de tailles "
              + ", ".join(f"${len([j for j in range(n) if rows[i][j]])}$" for i in sorted({min(j for j in range(n) if rows[i][j]) for i in range(n)}))
              + ". Combien de cases à $1$ contient sa fermeture transitive (diagonale comprise) ?")
    sizes = [len([j for j in range(n) if rows[i][j]]) for i in sorted({min(j for j in range(n) if rows[i][j]) for i in range(n)})]
    tot = sum(s * s for s in sizes)
    assert tot == sum(map(sum, rows))
    sol = f"Une composante de $s$ sommets donne un bloc $s\\times s$ de $1$ : $" + "+".join(f"{s}^2" for s in sizes) + f"={tot}$."
    return v(id, enonce, "+".join(f"{s}**2" for s in sizes), str(tot), sol)


CL23 = [[0] * 14 for _ in range(14)]
for _blk in ([0, 3, 4, 8, 12], [1, 7, 9, 10], [2, 5, 11], [6, 13]):
    for _a in _blk:
        for _b in _blk:
            CL23[_a][_b] = 1
L9 = [ncc_ex("g91", G3CC, G3CC_POS), ccvec_ex("g92", G3CC, G3CC_POS), conn_ex("g93", GC, GC_POS),
      clos_rank_ex("g94", CL22, S_P18 + ", ex. 1.1"), clos_rank_ex("g95", CL23, S_P19 + ", ex. 2.1"),
      clos_ones_ex("g96", CL22)]
V9 = {
    "g91": [_v(ncc_ex("_", U2)), _v(ncc_ex("_", C6))],
    "g92": [_v(ccvec_ex("_", D2 if False else und(9, [(0, 4), (1, 3), (3, 7), (2, 5), (5, 8)])))],
    "g93": [_v(conn_ex("_", U1, U1_POS)), _v(conn_ex("_", G3CC, G3CC_POS))],
    "g94": [_v(clos_rank_ex("_", CL23))],
    "g95": [_v(clos_rank_ex("_", CL22))],
    "g96": [_v(clos_ones_ex("_", CL23))],
}

# ---------------------------------------------------------------- level 10 : union-find (open)


def uf_roots(p):
    """Root of x in a father vector where a root holds a negative value (-1 or -size)."""
    def root(x):
        while p[x] >= 0:
            x = p[x]
        return x
    return root


def uf_comps(p):
    root = uf_roots(p)
    out = collections.defaultdict(list)
    for x in range(len(p)):
        out[root(x)].append(x)
    return dict(out)


def reunir(p, x, y, weighted=True, compress=True):
    def find(z):
        r = z
        while p[r] >= 0:
            r = p[r]
        if compress:
            while p[z] >= 0:
                p[z], z = r, p[z]
        return r
    rx, ry = find(x), find(y)
    if rx == ry:
        return
    if weighted:
        if p[rx] > p[ry]:  # rx is the smaller tree: it goes under ry
            rx, ry = ry, rx
        p[rx] += p[ry]
        p[ry] = rx
    else:
        p[ry] = rx


def uf_ex(id, p, extra=None, src=None, chains=()):
    comps_ = uf_comps(p)
    sizes = sorted(len(c) for c in comps_.values())
    sets = " ; ".join(f"$\\{{{fmt(c)}\\}}$" for c in comps_.values())
    n = len(p)
    pairs = [(a, b) for a in range(n) for b in range(a + 1, n)]
    root = uf_roots(p)
    q = ("Donner le nombre de sommets de chaque composante connexe de $G$ et le nombre minimal d'arêtes à ajouter pour que $G$ soit connexe.")
    k = len(comps_)
    enonce = (f"Soit un graphe non orienté d'ordre ${n}$ (sommets $0$ à ${n - 1}$). Les algorithmes `trouver` et `reunir` (union pondérée) ont construit le vecteur des pères\n\n"
              + _out("sommet : " + " ".join(f"{i:>3}" for i in range(n)) + "\np      : " + " ".join(f"{x:>3}" for x in p)) + f"\n\n{q}")
    sol = (f"Les racines sont les cases négatives ; chaque arbre est une composante, et la valeur négative donne sa taille : composantes {sets}, "
           f"tailles ${fmt(sizes)}$. Il y a ${k}$ composantes : il suffit de ${k - 1}$ arêtes, qui relient chacune deux composantes différentes "
           "(par exemple entre racines : " + ", ".join(f"${a}$—${b}$" for a, b in zip(list(comps_)[:-1], list(comps_)[1:])) + ").")
    if chains:
        enonce += " Parmi les chaînes suivantes, lesquelles ne peuvent pas exister dans $G$ : " + ", ".join(f"${a}\\to{b}$" for a, b in chains) + " ?"
        imp = [(a, b) for a, b in chains if root(a) != root(b)]
        sol += ("\n\nUne chaîne entre $a$ et $b$ existe si et seulement si $a$ et $b$ ont la même racine. Impossibles : "
                + (", ".join(f"${a}\\to{b}$ (racines ${root(a)}$ et ${root(b)}$)" for a, b in imp) or "aucune") + ".")
    if extra:
        x, y = extra
        p2 = list(p)
        reunir(p2, x, y)
        sol += (f"\n\nAjout de l'arête ${x}$—${y}$ (union pondérée + compression) : `trouver({x})` = ${root(x)}$, `trouver({y})` = ${root(y)}$ ; le plus petit arbre "
                f"est rattaché à la racine du plus grand. Nouveau vecteur : ${fmt(p2)}$.")
        enonce += f" On ajoute ensuite l'arête ${x}$—${y}$ (union pondérée et compression des chemins) : donner le nouveau vecteur."
    return o(id, enonce, sol, src=src)


P17 = [5, 8, 5, 8, 11, -4, 5, 10, -6, 12, 8, 12, -4, 8]
assert sorted(len(c) for c in uf_comps(P17).values()) == [4, 4, 6]  # official solution: 4, 6, 4


def poss_ex(id, rows, vectors, weighted, src=None):
    """Which father vectors can come from the edges of a graph whose closure is `rows`?"""
    n = len(rows)
    comp = {frozenset(j for j in range(n) if rows[i][j]) for i in range(n)}
    verdict, why = [], []
    for name, p in vectors:
        root = uf_roots(p)
        msg = None
        try:
            got = {}
            for x in range(n):
                got.setdefault(root(x), set()).add(x)
        except IndexError:
            got = None
        if got is None or {frozenset(s) for s in got.values()} != comp:
            bad = next((x for x in range(n) if p[x] >= 0 and frozenset(j for j in range(n) if rows[x][j]) != frozenset(
                j for j in range(n) if rows[p[x]][j])), None)
            msg = (f"le sommet ${bad}$ a pour père ${p[bad]}$ d'une autre composante" if bad is not None else
                   "les arbres ne couvrent pas exactement les composantes (une composante est coupée en plusieurs arbres)")
        elif weighted:
            r = [x for x in range(n) if p[x] < 0]
            if any(-p[x] != len(next(s for s in comp if x in s)) for x in r):
                msg = "une racine ne porte pas l'opposé de la taille de sa composante"
        verdict.append(msg is None)
        why.append(f"- ${name}$ : " + ("possible (chaque arbre couvre une composante" + (" et chaque racine porte l'opposé de sa taille" if weighted else "") + ")." if msg is None else f"impossible, {msg}."))
    grid = "\n".join(f"{name}: " + " ".join(f"{x:>3}" for x in p) for name, p in vectors)
    enonce = (f"Soit un graphe non orienté d'ordre ${n}$ dont les composantes connexes sont "
              + " ; ".join("$\\{" + fmt(sorted(s)) + "\\}$" for s in sorted(comp, key=min))
              + f". On applique `trouver` et `reunir` ({'versions optimisées : union pondérée et compression' if weighted else 'versions non optimisées'}) à la liste des arêtes. "
              "Parmi les vecteurs des pères suivants (sommets $0$ à " + str(n - 1) + "), lesquels pourraient correspondre au résultat ?\n\n" + _out(grid))
    sol = "Conditions : un arbre par composante, tout père dans la composante de son fils" + (", racine = $-$taille" if weighted else "") + ".\n\n" + "\n".join(why) + \
          "\n\n(On ne connaît pas la liste des arêtes : ce sont des conditions nécessaires, qui suffisent à éliminer les vecteurs impossibles.)"
    return o(id, enonce, sol, src=src), verdict


_ex1, _vd = poss_ex("g102", CL22, [("P_1", [2, -1, -1, 1, 1, 2, 2, 1, 1, 4]), ("P_2", [2, -1, -1, 1, -1, 2, 2, 1, 1, 4]),
                                 ("P_3", [5, -1, -1, 1, -1, 2, 5, 1, 3, 4]), ("P_4", [5, -1, -1, 1, -1, 2, 5, 1, 3, -1])], False, S_P18 + ", ex. 1.2")
assert _vd == [False, True, True, False]  # official: P2 and P3
_ex2, _vd = poss_ex("g103", CL23, [("P_1", [4, 10, 11, 12, -1, 11, -1, 9, 4, -1, 9, -1, 4, 6]), ("P_2", [4, 10, 12, 11, 11, 12, -1, 9, 4, 10, -1, -1, -1, 6]),
                                 ("P_3", [4, 10, 11, 12, 12, 11, -1, 9, 4, 10, -1, -1, -1, 6]), ("P_4", [4, 10, 11, 12, -1, 11, -1, 9, 2, -1, 9, -1, 10, 6])],
                    False, S_P19 + ", ex. 2.2")
assert _vd == [True, False, True, False]


def build_ex(id, n, edges, weighted, compress):
    p = [-1] * n
    steps = []
    for x, y in edges:
        reunir(p, x, y, weighted, compress)
        steps.append(f"- arête ${x}$—${y}$ : ${fmt(p)}$")
    names = ("union pondérée" if weighted else "union simple") + (" et compression des chemins" if compress else "")
    enonce = (f"On part de ${n}$ sommets isolés ($p[x]=-1$ pour tout $x$) et on ajoute dans l'ordre les arêtes "
              + ", ".join(f"${x}$—${y}$" for x, y in edges) + f", avec {names}. Donner le vecteur des pères après chaque arête. "
              "(Règle : `reunir(x, y)` rattache la racine de $y$ à celle de $x$" + (" ; avec l'union pondérée, le plus petit arbre est rattaché au plus grand, à égalité $y$ sous $x$" if weighted else "") + ".)")
    sol = "\n".join(steps) + "\n\nDans le vecteur, la racine d'un arbre porte " + ("l'opposé de sa taille." if weighted else "$-1$.")
    return o(id, enonce, sol)


def height_ex(id, n):
    h = int(math.log2(n))
    enonce = (f"Avec l'union pondérée (sans compression), quelle est la hauteur maximale d'un arbre de ${n}$ sommets (racine = hauteur $0$) ? "
              "On donne $n$ puissance de $2$.")
    sol = (f"Un sommet n'augmente sa profondeur que lorsque son arbre est rattaché à un arbre au moins aussi grand : la taille de son arbre au moins double. "
           f"Il y a au plus $\\log_2 n$ doublements : hauteur maximale $\\log_2{n}={h}$ (atteinte en réunissant des arbres de même taille deux à deux).")
    return v(id, enonce, f"log({n})/log(2)", str(h), sol)


L10 = [uf_ex("g101", P17, src=S_P17 + ", ex. 1", chains=[(3, 7), (11, 6), (0, 13), (4, 9)]), _ex1, _ex2, build_ex("g104", 8, [(0, 1), (2, 3), (0, 2), (4, 5), (6, 7), (4, 6), (0, 4)], True, False),
       height_ex("g105", 32)]
V10 = {"g105": [_v(height_ex("_", 256))]}
L10.append(build_ex("g106", 6, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)], False, False))
L10.append(uf_ex("g107", P17, extra=(7, 4), src=S_P21 + ", ex. 2", chains=[(3, 7), (11, 6), (0, 13), (4, 9)]))
# ---------------------------------------------------------------- level 11 : write the traversals (Python, executed)


def T(expr, val):
    return (expr, repr(val))


def deg_list(g):
    return [len(g.adj[x]) for x in g.vs]


def inout(g):
    return ([sum(1 for a, b in g.edges if b == x) for x in g.vs], [len(g.adj[x]) for x in g.vs])


CODE_DEG = """
def degrees(G):
    deg = []
    for x in range(G.order):
        deg.append(len(G.adjlists[x]))
    return deg
"""
CODE_INOUT = """
def in_out_degrees(G):
    inn = [0] * G.order
    out = [0] * G.order
    for x in range(G.order):
        out[x] = len(G.adjlists[x])
        for y in G.adjlists[x]:
            inn[y] += 1
    return (inn, out)
"""
CODE_BFS = """
def bfs_order(G, src):
    mark = [False] * G.order
    q = Queue()
    q.enqueue(src)
    mark[src] = True
    order = []
    while not q.isempty():
        x = q.dequeue()
        order.append(x)
        for y in G.adjlists[x]:
            if not mark[y]:
                mark[y] = True
                q.enqueue(y)
    return order
"""
CODE_DFS = """
def _dfs(G, x, mark, pre, suf):
    mark[x] = True
    pre.append(x)
    for y in G.adjlists[x]:
        if not mark[y]:
            _dfs(G, y, mark, pre, suf)
    suf.append(x)

def dfs_orders(G, src):
    mark = [False] * G.order
    pre = []
    suf = []
    _dfs(G, src, mark, pre, suf)
    for x in range(G.order):
        if not mark[x]:
            _dfs(G, x, mark, pre, suf)
    return (pre, suf)
"""
CODE_COMP = """
def _comp(G, x, nocc, cc):
    cc[x] = nocc
    for y in G.adjlists[x]:
        if cc[y] == 0:
            _comp(G, y, nocc, cc)

def components(G):
    cc = [0] * G.order
    nocc = 0
    for x in range(G.order):
        if cc[x] == 0:
            nocc += 1
            _comp(G, x, nocc, cc)
    return (nocc, cc)
"""
CODE_CONN = """
def _visit(G, x, mark):
    mark[x] = True
    count = 1
    for y in G.adjlists[x]:
        if not mark[y]:
            count += _visit(G, y, mark)
    return count

def is_connected(G):
    mark = [False] * G.order
    return _visit(G, 0, mark) == G.order
"""
_ccvec = [comps(G3CC)[x] for x in G3CC.vs]
assert _ccvec == [1, 2, 1, 2, 3, 1, 1, 2, 2, 3, 2, 3, 3, 2]  # exam example of the components exercise
_d = DFS(T1, 0)
L11 = [
    w("g111", "Écrire la fonction `degrees(G)` qui retourne la liste des degrés des sommets d'un graphe non orienté représenté par listes d'adjacence.\n\n" + ANNEXE,
      CODE_DEG, [T("degrees(T2)", deg_list(T2)), T("degrees(K4)", deg_list(K4))],
      r"Complexité : $O(n)$ (le degré est la longueur de la liste : `len`, sans la parcourir)."),
    w("g112", "Écrire la fonction `in_out_degrees(G)` qui retourne le couple de listes (demi-degrés intérieurs, demi-degrés extérieurs) d'un graphe orienté représenté par listes d'adjacence.\n\n" + ANNEXE,
      CODE_INOUT, [T("in_out_degrees(T1)", inout(T1)), T("in_out_degrees(D1)", inout(D1))],
      r"Le demi-degré extérieur est la longueur de la liste ; le demi-degré intérieur s'obtient en comptant, pour chaque arc rencontré, l'extrémité. Complexité $O(n+m)$."),
    w("g113", "Écrire la fonction `bfs_order(G, src)` qui retourne la liste des sommets accessibles depuis `src` dans l'ordre d'un parcours en largeur.\n\n" + ANNEXE,
      CODE_BFS, [T("bfs_order(GC, 0)", bfs(GC, 0)[0]), T("bfs_order(T1, 7)", bfs(T1, 7)[0])],
      r"On marque à l'enfilage. Complexité $O(n+m)$ avec des listes d'adjacence."),
    w("g114", "Écrire la fonction `dfs_orders(G, src)` qui retourne le couple (ordre préfixe, ordre suffixe) d'un parcours en profondeur complet lancé sur `src` puis sur les sommets non marqués (ordre croissant).\n\n" + ANNEXE,
      CODE_DFS, [T("dfs_orders(T1, 0)", (_d.pre, _d.suf)), T("dfs_orders(T2, 7)", (DFS(T2, 7).pre, DFS(T2, 7).suf))],
      r"Le préfixe est noté avant la boucle sur les successeurs, le suffixe après. Complexité $O(n+m)$."),
    w("g115", "Écrire la fonction `components(G)` qui détermine les composantes connexes d'un graphe non orienté. Elle retourne un couple : le nombre de composantes et le vecteur des composantes (pour chaque sommet, le numéro de sa composante).\n\n" + ANNEXE + "\n\nExemple avec `G3CC`, le graphe ci-dessous.\n\n" + gfig(G3CC, G3CC_POS),
      CODE_COMP, [T("components(G3CC)", (3, _ccvec)), T("components(C6)", (1, [1] * 6))],
      r"Le vecteur d'entiers remplace le vecteur de booléens ; $0$ signifie « non visité ». Le numéro augmente à chaque relance : un parcours complet en $O(n+m)$.", src=S_P18 + ", ex. 3"),
    w("g116", "Écrire la fonction `is_connected(G)` qui indique si un graphe non orienté (non vide) est connexe, avec un seul parcours en profondeur.\n\n" + ANNEXE,
      CODE_CONN, [T("is_connected(GC)", True), T("is_connected(G3CC)", False), T("is_connected(TREE)", True)],
      r"Un seul parcours depuis un sommet quelconque : le graphe est connexe si et seulement si il a marqué les $n$ sommets (ici on compte les sommets visités)."),
]

# ---------------------------------------------------------------- level 12 : applications (code)


def dist_all(g):
    d = {x: bfs(g, x)[1] for x in g.vs}
    return d


def levels_of(g, s):
    d = bfs(g, s)[1]
    out = [[] for _ in range(max(d.values()) + 1)]
    for y in bfs(g, s)[0]:
        out[d[y]].append(y)
    return out


def dens(g):
    cc = comps(g)
    res = []
    for c in sorted(set(cc.values())):
        vs = [x for x in g.vs if cc[x] == c]
        m = sum(1 for a, b in g.edges if cc[a] == c)
        res.append(m / len(vs))
    return res


def centre(g):
    ecc = {x: max(bfs(g, x)[1].values()) for x in g.vs}
    r = min(ecc.values())
    return [x for x in g.vs if ecc[x] == r]


def brute_bip(g):
    for col in itertools.product((0, 1), repeat=len(g.vs)):
        if all(col[a] != col[b] for a, b in g.edges):
            return True
    return False


def brute_acyclic(g):
    indeg = {x: sum(1 for a, b in g.edges if b == x) for x in g.vs}
    left = set(g.vs)
    while True:
        free = [x for x in left if indeg[x] == 0]
        if not free:
            return not left
        for x in free:
            left.discard(x)
            for y in g.adj[x]:
                indeg[y] -= 1


def is_tree_py(g):
    return len(set(comps(g).values())) == 1 and len(g.edges) == len(g.vs) - 1


def euler_py(g):
    if len(set(comps(g).values())) != 1:
        return False
    odd = sum(1 for x in g.vs if len(g.adj[x]) % 2)
    return odd in (0, 2)


def topo_ok(g, order):
    pos = {x: i for i, x in enumerate(order)}
    return sorted(order) == sorted(g.vs) and all(pos[a] < pos[b] for a, b in g.edges)


CODE_LEVELS = """
def levels(G, src):
    dist = [-1] * G.order
    dist[src] = 0
    res = [[src]]
    q = Queue()
    q.enqueue(src)
    while not q.isempty():
        x = q.dequeue()
        for y in G.adjlists[x]:
            if dist[y] == -1:
                dist[y] = dist[x] + 1
                if dist[y] == len(res):
                    res.append([])
                res[dist[y]].append(y)
                q.enqueue(y)
    return res
"""
CODE_DENS = """
def _comp(G, x, nocc, cc):
    cc[x] = nocc
    for y in G.adjlists[x]:
        if cc[y] == 0:
            _comp(G, y, nocc, cc)

def density_components(G):
    cc = [0] * G.order
    nocc = 0
    for x in range(G.order):
        if cc[x] == 0:
            nocc += 1
            _comp(G, x, nocc, cc)
    nbv = [0] * nocc
    nbl = [0] * nocc
    for x in range(G.order):
        nbv[cc[x] - 1] += 1
        nbl[cc[x] - 1] += len(G.adjlists[x])
    res = []
    for c in range(nocc):
        res.append(nbl[c] / 2 / nbv[c])
    return res
"""
CODE_BIP = """
def is_bipartite(G):
    color = [0] * G.order
    for s in range(G.order):
        if color[s] == 0:
            color[s] = 1
            q = Queue()
            q.enqueue(s)
            while not q.isempty():
                x = q.dequeue()
                for y in G.adjlists[x]:
                    if color[y] == 0:
                        color[y] = 3 - color[x]
                        q.enqueue(y)
                    elif color[y] == color[x]:
                        return False
    return True
"""
CODE_ACYC = """
def _dfs(G, x, mark):
    mark[x] = 1
    for y in G.adjlists[x]:
        if mark[y] == 1:
            return False
        if mark[y] == 0 and not _dfs(G, y, mark):
            return False
    mark[x] = 2
    return True

def acyclic(G):
    mark = [0] * G.order
    for x in range(G.order):
        if mark[x] == 0 and not _dfs(G, x, mark):
            return False
    return True
"""
CODE_TREE = """
def _dfs(G, x, father, mark):
    mark[x] = True
    for y in G.adjlists[x]:
        if not mark[y]:
            if not _dfs(G, y, x, mark):
                return False
        elif y != father:
            return False
    return True

def is_tree(G):
    mark = [False] * G.order
    if not _dfs(G, 0, -1, mark):
        return False
    for x in range(G.order):
        if not mark[x]:
            return False
    return True
"""
CODE_CENTER = """
def _ecc(G, s):
    dist = [-1] * G.order
    dist[s] = 0
    q = Queue()
    q.enqueue(s)
    best = 0
    while not q.isempty():
        x = q.dequeue()
        best = max(best, dist[x])
        for y in G.adjlists[x]:
            if dist[y] == -1:
                dist[y] = dist[x] + 1
                q.enqueue(y)
    return best

def center(G):
    ecc = []
    for x in range(G.order):
        ecc.append(_ecc(G, x))
    radius = ecc[0]
    for x in range(G.order):
        radius = min(radius, ecc[x])
    res = []
    for x in range(G.order):
        if ecc[x] == radius:
            res.append(x)
    return res
"""
CODE_TOPO = """
def _dfs(G, x, mark, res):
    mark[x] = True
    for y in G.adjlists[x]:
        if not mark[y]:
            _dfs(G, y, mark, res)
    res.insert(0, x)

def topological_sort(G):
    mark = [False] * G.order
    res = []
    for x in range(G.order):
        if not mark[x]:
            _dfs(G, x, mark, res)
    return res
"""
CODE_EULER = """
def _visit(G, x, mark):
    mark[x] = True
    count = 1
    for y in G.adjlists[x]:
        if not mark[y]:
            count += _visit(G, y, mark)
    return count

def is_eulerian(G):
    mark = [False] * G.order
    if _visit(G, 0, mark) != G.order:
        return False
    odd = 0
    for x in range(G.order):
        if len(G.adjlists[x]) % 2 == 1:
            odd += 1
    return odd == 0 or odd == 2
"""
CODE_DIAM = """
def _farthest(G, s):
    dist = [-1] * G.order
    dist[s] = 0
    q = Queue()
    q.enqueue(s)
    last = s
    while not q.isempty():
        last = q.dequeue()
        for y in G.adjlists[last]:
            if dist[y] == -1:
                dist[y] = dist[last] + 1
                q.enqueue(y)
    return (last, dist[last])

def diameter(G):
    s1 = _farthest(G, 0)[0]
    return _farthest(G, s1)[1]
"""
_topo = DAG.graph()
_ord = []
_dd = DFS(DAG, 0)
_ord = list(reversed(_dd.suf))
assert topo_ok(DAG, _ord)
L12 = [
    w("g121", "Écrire la fonction `levels(G, src)` qui retourne une liste `L` de longueur $exc(src)+1$ dans laquelle `L[i]` contient les sommets à distance $i$ de `src` (graphe non orienté connexe).\n\n" + ANNEXE + "\n\nExemple avec `GC`, le graphe ci-dessous.\n\n" + gfig(GC, GC_POS),
      CODE_LEVELS, [T("levels(GC, 0)", levels_of(GC, 0)), T("levels(TREE, 0)", levels_of(TREE, 0))],
      r"Un parcours en largeur : les sommets sortent de la file par distance croissante. On ajoute une sous-liste quand on rencontre pour la première fois une nouvelle distance. Complexité $O(n+m)$.", src=S_R21 + ", ex. 4"),
    w("g122", "Écrire la fonction `density_components(G)` qui retourne la liste des densités $p/n$ ($p$ arêtes, $n$ sommets) des composantes connexes d'un graphe non orienté simple (dans l'ordre où le parcours les découvre).\n\n" + ANNEXE + "\n\nExemple avec `G3CC`, le graphe ci-dessous.\n\n" + gfig(G3CC, G3CC_POS),
      CODE_DENS, [T("density_components(G3CC)", dens(G3CC)), T("density_components(C6)", dens(C6))],
      r"Le nombre d'arêtes d'une composante est la moitié de la somme des longueurs des listes de ses sommets (chaque arête apparaît deux fois). Pour un graphe connexe simple : $p$ va de $n-1$ (arbre) à $\frac{n(n-1)}2$ (graphe complet).", src=S_R21 + ", ex. 3.2"),
    w("g123", "Écrire la fonction `is_bipartite(G)` qui teste, avec un parcours en largeur, si un graphe non orienté est biparti (ses sommets se colorent avec deux couleurs sans arête entre deux sommets de même couleur).\n\n" + ANNEXE,
      CODE_BIP, [T("is_bipartite(C6)", brute_bip(C6)), T("is_bipartite(K4)", brute_bip(K4)), T("is_bipartite(TREE)", brute_bip(TREE))],
      r"On colore le départ en $1$ puis chaque voisin non coloré avec la couleur opposée $3-c$ ; une arête vers un sommet de même couleur prouve un cycle impair, donc que le graphe n'est pas biparti. On relance sur chaque composante.", src=S_P17 + ", ex. 3"),
    w("g124", "Écrire la fonction `acyclic(G)` qui vérifie qu'un graphe orienté est sans circuit, en utilisant un unique vecteur de marques à trois valeurs (non vu, première rencontre, dernière rencontre).\n\n" + ANNEXE,
      CODE_ACYC, [T("acyclic(DAG)", brute_acyclic(DAG)), T("acyclic(T1)", brute_acyclic(T1)), T("acyclic(D1)", brute_acyclic(D1))],
      r"Un arc vers un sommet à la première rencontre (en cours de traitement) est un arc arrière, donc un circuit. Un arc vers un sommet terminé est avant ou croisé : sans danger.", src=S_R21 + ", ex. 2"),
    w("g125", "Écrire la fonction `is_tree(G)` qui vérifie, avec un parcours en profondeur, qu'un graphe non orienté est un arbre (connexe et sans cycle).\n\n" + ANNEXE,
      CODE_TREE, [T("is_tree(TREE)", is_tree_py(TREE)), T("is_tree(C6)", is_tree_py(C6)), T("is_tree(G3CC)", is_tree_py(G3CC))],
      r"Sans cycle : pendant le parcours, un voisin déjà marqué qui n'est pas le père prouve un cycle. Connexe : tous les sommets sont marqués après un seul parcours.", src=S_R19B + ", ex. 3 ; " + S_P19 + ", ex. 3"),
    w("g126", "Écrire la fonction `center(G)` qui retourne le centre d'un graphe non orienté connexe : l'ensemble des sommets d'excentricité minimale (excentricité $=$ plus grande distance aux autres sommets ; rayon $=$ plus petite excentricité).\n\n" + ANNEXE + "\n\nExemple avec `GC`, le graphe ci-dessous.\n\n" + gfig(GC, GC_POS),
      CODE_CENTER, [T("center(GC)", centre(GC)), T("center(TREE)", centre(TREE))],
      r"Un parcours en largeur depuis chaque sommet donne son excentricité : $O(n(n+m))$.", src=S_R19B + ", ex. 2 ; " + S_P19 + ", ex. 4"),
    w("g127", "Écrire la fonction `topological_sort(G)` qui retourne une liste des sommets d'un graphe orienté sans circuit telle que pour tout arc $(x,y)$, $x$ soit avant $y$ (tri topologique). Utiliser un parcours en profondeur.\n\n" + ANNEXE,
      CODE_TOPO, [T("topological_sort(DAG)", list(reversed(DFS(DAG, 0).suf)))],
      r"Dans un graphe sans circuit, pour tout arc $(u,v)$ on a $\text{suff}[v]<\text{suff}[u]$ : trier les sommets par suffixe décroissant (insertion en tête de liste à la fin du traitement de chaque sommet) donne un tri topologique.", src=S_R19 + ", ex. 4.2"),
    w("g128", "Écrire la fonction `is_eulerian(G)` qui vérifie si un graphe non orienté simple possède une chaîne ou un cycle eulérien : il est connexe et a $0$ ou $2$ sommets de degré impair (théorème d'Euler). Utiliser un parcours en profondeur pour la connexité.\n\n" + ANNEXE,
      CODE_EULER, [T("is_eulerian(C6)", euler_py(C6)), T("is_eulerian(K4)", euler_py(K4)), T("is_eulerian(TREE)", euler_py(TREE))],
      r"Le degré d'un sommet est `len(G.adjlists[x])`. $K_4$ a quatre sommets de degré $3$ : non eulérien.", src=S_P18 + ", ex. 5"),
    w("g129", "Écrire la fonction `diameter(G)` qui calcule le diamètre d'un graphe qui est un arbre : depuis un sommet quelconque on cherche un sommet $s_1$ le plus éloigné, puis depuis $s_1$ un sommet $s_2$ le plus éloigné ; la distance de $s_1$ à $s_2$ est le diamètre.\n\n" + ANNEXE,
      CODE_DIAM, [T("diameter(TREE)", max(max(bfs(TREE, x)[1].values()) for x in TREE.vs)), T("diameter(TREE2)", max(max(bfs(TREE2, x)[1].values()) for x in TREE2.vs))],
      r"Le dernier sommet défilé d'un parcours en largeur est à distance maximale. Deux parcours : $O(n)$ dans un arbre.", src=S_P18 + ", ex. 4"),
]

# ---------------------------------------------------------------- exam parts (EXTRA_PARTS) and levels 13-14


def indeg_row_ex(id, g, src=None):
    n = len(g.vs)
    indeg = [sum(1 for a, b in g.edges if b == x) for x in g.vs]
    enonce = f"Soit le graphe $G=\\langle S,A\\rangle$ orienté avec {desc(g)}.\n\n{gfig(g)}\n\nRemplir le tableau des demi-degrés intérieurs des sommets ${fmt(g.vs)}$."
    sol = f"$d^{{\\circ-}}(x)$ = nombre d'arcs qui arrivent en $x$ (somme de la colonne $x$ de la matrice) : ${fmt(indeg)}$ (total ${sum(indeg)}$ = nombre d'arcs)."
    return v(id, enonce, f"Matrix([[1]*{n}])*{g.mat()}", mrow(indeg), sol, src=src)


def strong_ex(id, g, src=None):
    import sympy as sp
    n = len(g.vs)
    cl = closure(g)
    ok = int(all(all(r) for r in cl))
    classes = []
    for i in range(n):
        cls = [j for j in range(n) if cl[i][j] and cl[j][i]]
        if cls not in classes:
            classes.append(cls)
    enonce = (f"Soit le graphe orienté $G$ avec {desc(g)}. $G$ est-il fortement connexe (réponse $1$ si oui, $0$ sinon) ?")
    sol = (f"Fortement connexe : un chemin de $x$ à $y$ pour toute paire ordonnée. On calcule la fermeture (Warshall) : "
           + ("tous les couples sont atteints : réponse $1$." if ok else
              f"elle n'est pas pleine, donc réponse $0$. Composantes fortement connexes : "
              + " ; ".join("$\\{" + fmt([g.vs[j] for j in c]) + "\\}$" for c in classes) + f" : ${len(classes)}$ composantes."))
    return v(id, enonce, f"Min(1,Min(*((eye({n})+{g.mat()})**{n - 1})))", str(ok), sol, src=src), len(classes), classes


def scc_ex(id, g, src=None):
    _, k, classes = strong_ex("_", g)
    cl = closure(g)
    enonce = f"Soit le graphe orienté $G$ avec {desc(g)}. Combien $G$ possède-t-il de composantes fortement connexes ?"
    sol = ("Deux sommets sont dans la même composante fortement connexe s'ils s'atteignent mutuellement (fermeture de Warshall) : "
           + " ; ".join("$\\{" + fmt([g.vs[j] for j in c]) + "\\}$" for c in classes) + f". Il y en a ${k}$.")
    n = len(g.vs)
    # independent check: number of classes of the equivalence 'reaches both ways' = number of distinct rows of the mutual-reachability matrix
    mutual = {tuple(1 if cl[i][j] and cl[j][i] else 0 for j in range(n)) for i in range(n)}
    assert len(mutual) == k
    return v(id, enonce, f"{k}", str(k), sol + " (nombre vérifié par le calcul des classes d'équivalence)", src=src)


E25_PREF = DFS(E25, 3).pre
_x1 = indeg_row_ex("x1a", E25, S_C21 + ", ex. 1.1")
_x2 = order_ex("x1b", "dfs", E25, 3, src=S_C21 + ", ex. 1.2")
_x3 = strong_ex("x1c", E25, S_C21 + ", ex. 1.3")[0]
_x4 = scc_ex("x1d", E25, S_C21 + ", ex. 1.4")
_iso = [x for x in E25.vs if len(E25.adj[x]) + sum(1 for a, b in E25.edges if b == x) == 0]
_x5 = o("x1e", f"Soit le graphe orienté $G$ avec {desc(E25)}. S'ils existent, quels sont les sommets de $G$ de degré égal à $0$ ? S'il n'en existe pas, répondre $0$.",
        "Un sommet de degré nul est isolé : $d^\\circ(x)=d^{\\circ+}(x)+d^{\\circ-}(x)=0$. Ici chaque sommet est extrémité d'au moins un arc "
        f"(demi-degrés intérieurs ${fmt([sum(1 for a, b in E25.edges if b == x) for x in E25.vs])}$, extérieurs ${fmt([len(E25.adj[x]) for x in E25.vs])}$, jamais nuls tous les deux) : "
        + ("réponse $0$." if not _iso else f"sommets isolés : ${fmt(_iso)}$."), src=S_C21 + ", ex. 1.5")
assert not _iso


_ya = o("x2a", "Donner l'ordre (nombre de sommets) du graphe orienté $G=\\langle S,A\\rangle$ avec " + desc(E21) + ", puis le nom d'un sommet de degré nul. "
        "S'ils existent, quels sont les sommets de demi-degré extérieur égal à $0$ ? De demi-degré intérieur égal à $1$ ?",
        f"L'ordre est $|S|={len(E21.vs)}$. Un sommet de degré nul s'appelle un sommet isolé (ici : aucun, tous sont extrémité d'un arc). "
        f"Demi-degré extérieur nul (aucune liste de successeurs) : ${fmt([x for x in E21.vs if not E21.adj[x]])}$. "
        f"Demi-degré intérieur égal à $1$ : ${fmt([x for x in E21.vs if sum(1 for a, b in E21.edges if b == x) == 1])}$ "
        f"(demi-degrés intérieurs ${fmt([sum(1 for a, b in E21.edges if b == x) for x in E21.vs])}$).", src=S_C19 + ", ex. 1")
_ua = uf_ex("x3a", P17, src=S_P17 + ", ex. 1", chains=[(3, 7), (11, 6), (0, 13), (4, 9)])
_ub = indeg_row_ex("x3b", E21, S_P17 + ", ex. 2.2")
_uc = forest_ex("x3c", E21, 1, S_P17 + ", ex. 2.3")
# partiel of 17 Dec 2019, ex. 1 and 2
_pa = o("x4a", f"Un graphe simple non orienté $G$ de $9$ sommets est représenté par la matrice d'adjacence dont les $1$ (V) sont, par ligne, : "
        + "; ".join(f"{x} : {fmt(E23.adj[x])}" for x in E23.vs)
        + ".\n\n" + gfig(E23, _tree_pos(E23, 1)) + "\n\nDonner deux propriétés des graphes que possède la fermeture transitive de $G$.",
        "La fermeture transitive $G^*$ relie deux sommets si et seulement si une chaîne les relie dans $G$. Propriétés : "
        "(1) c'est un graphe non orienté **symétrique** et réflexif si on compte la diagonale ; "
        "(2) ses composantes connexes sont des **graphes complets** : $G^*$ est une réunion de cliques, une par composante ; "
        f"(3) $G$ est connexe si et seulement si $G^*$ est complet. Ici $G$ est un arbre de $9$ sommets : $G^*=K_9$ ({9 * 8 // 2} arêtes).", src=S_P19 + ", ex. 1.1")
_pb = order_ex("x4b", "suf", E23, 1, src=S_P19 + ", ex. 1.2")
_pc = clos_rank_ex("x4c", CL23, S_P19 + ", ex. 2.1")
EXTRA_PARTS = [_x1, _x2, _x3, _x4, _x5, _ya, _ua, _ub, _uc, _pa, _pb, _pc]
assert E23.adj[1] == [2, 3]
assert [sum(1 for a, b in E21.edges if b == x) for x in E21.vs] == [2, 1, 2, 0, 2, 3, 1, 1, 2, 2]  # official table
assert DFS(E23, 1).suf == [2, 6, 8, 9, 7, 4, 5, 3, 1]

# exercises used as parts must not be repeated as levels: the exam levels use EXTRA_PARTS and the code exercises
L13 = [
    {"id": "g131", "kind": "multi", "parts": ["x1a", "x1b", "x1c", "x1d", "x1e"], "src": S_C21 + ", ex. 1 (Graphes et composantes)",
     "enonce": "**Exercice (5 points).** Soit le graphe orienté $G$ avec " + desc(E25) + ".\n\n" + gfig(E25) + "\n\nRépondre dans l'ordre aux cinq questions."},
    {"id": "g132", "kind": "multi", "parts": ["x3a", "x3b", "x3c", "g123"], "src": S_P17 + ", ex. 1, 2 et 3",
     "enonce": "**Partiel de décembre 2017 (extraits).** Union-find, dessin d'un graphe orienté, graphes bipartis."},
    {"id": "g133", "kind": "multi", "parts": ["x4a", "x4b", "x4c", "g102"], "src": S_P19 + ", ex. 1 et 2",
     "enonce": "**Partiel de décembre 2019 (extraits).** Représentation, ordre suffixe, Warshall et trouver-réunir."},
    {"id": "g134", "kind": "multi", "parts": ["x2a", "g127", "g128"], "src": S_C19 + ", ex. 1 ; " + S_R19 + ", ex. 4 ; " + S_P18 + ", ex. 5",
     "enonce": "**Terminologie, tri topologique et chaîne eulérienne.**"},
]
# harder: +20 % (several code questions and a union-find in one subject)
L14 = [
    {"id": "g141", "kind": "multi", "parts": ["g94", "g115", "g129", "g128"], "src": S_P18 + ", ex. 1, 3, 4 et 5",
     "enonce": "**Partiel de décembre 2018 (extraits).** Warshall, composantes, diamètre et graphe eulérien."},
    {"id": "g142", "kind": "multi", "parts": ["g107", "g122", "g121"], "src": S_P21 + ", ex. 2 ; " + S_R21 + ", ex. 3 et 4",
     "enonce": "**Union-find, densité et niveaux.**"},
    {"id": "g143", "kind": "multi", "parts": ["g125", "g126", "g124", "g85"], "src": S_R19B + ", ex. 2 et 3 ; " + S_R21 + ", ex. 2",
     "enonce": "**Arbre, centre, graphe sans circuit et forêt couvrante.**"},
]

LEVELS = [
    {"n": 1, "titre": "Rappel S1 : compter les tours de boucles et la complexité", "notions": ["rappel-complexite"], "exos": [e[0] for e in L1]},
    {"n": 2, "titre": "Rappel S1/S2 : files, piles et parcours d'arbres généraux", "notions": ["rappel-files-arbres"], "exos": L2},
    {"n": 3, "titre": "Degrés et demi-degrés, graphes complets", "notions": ["terminologie"], "exos": L3},
    {"n": 4, "titre": "Chemins et puissances de la matrice d'adjacence", "notions": ["chemins"], "exos": L4},
    {"n": 5, "titre": "Matrice et listes d'adjacence : lecture, tailles, conversion", "notions": ["representations"], "exos": L5},
    {"n": 6, "titre": "Parcours en largeur : ordre, distances, excentricité", "notions": ["parcours-largeur"], "exos": L6},
    {"n": 7, "titre": "Parcours en profondeur : ordres préfixe et suffixe", "notions": ["parcours-profondeur"], "exos": L7},
    {"n": 8, "titre": "Forêt couvrante et classification des arcs", "notions": ["classification", "parcours-profondeur"], "exos": L8},
    {"n": 9, "titre": "Connexité : composantes et fermeture transitive (Warshall)", "notions": ["connexite"], "exos": L9},
    {"n": 10, "titre": "Connexité évolutive : trouver-réunir", "notions": ["trouver-reunir"], "exos": L10},
    {"n": 11, "titre": "Écrire les parcours en Python : degrés, BFS, DFS, composantes", "notions": ["representations", "parcours-largeur", "parcours-profondeur", "connexite"], "exos": L11},
    {"n": 12, "titre": "Écrire des applications : niveaux, biparti, arbre, centre, tri topologique", "notions": ["applications", "classification"], "exos": L12},
    {"n": 13, "titre": "Examens : extraits de partiels et de contrôles", "notions": ["terminologie", "parcours-profondeur", "classification", "connexite", "trouver-reunir", "applications"], "exos": L13},
    {"n": 14, "titre": "Examens, version plus longue (+20 %)", "notions": ["connexite", "trouver-reunir", "applications", "classification"], "exos": L14},
]

# level 1 exercises come with their variants
for _i, (_e, _vs) in enumerate(L1):
    V2[_e["id"]] = _vs
VARIANTS = {**V2, **V3, **V4, **V5, **V6, **V7, **V9, **V10}
for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["id"] in VARIANTS:
            _e["variants"] = VARIANTS[_e["id"]]
for _e in EXTRA_PARTS:
    if _e["id"] in VARIANTS:
        _e["variants"] = VARIANTS[_e["id"]]

QUIZ = [
    {"notion": "rappel-complexite", "type": "qcm", "q": r"Combien de tours fait `for i in range(2, 20, 3):` ?", "choix": [r"$6$", r"$7$", r"$18$", r"$5$"], "bonne": 0},
    {"notion": "rappel-complexite", "type": "vf", "q": r"Parcourir toutes les cases d'une matrice $n\times n$ coûte $O(n)$.", "bonne": False},
    {"notion": "rappel-files-arbres", "type": "qcm", "q": r"Le parcours en largeur utilise :", "choix": [r"une file", r"une pile", r"un tri", r"un arbre binaire de recherche"], "bonne": 0},
    {"notion": "rappel-files-arbres", "type": "vf", "q": r"Dans l'ordre suffixe d'un arbre général, la racine est le dernier nœud.", "bonne": True},
    {"notion": "terminologie", "type": "qcm", "q": r"La somme des degrés d'un graphe non orienté simple de $m$ arêtes vaut :", "choix": [r"$2m$", r"$m$", r"$m^2$", r"$m(m-1)$"], "bonne": 0},
    {"notion": "terminologie", "type": "vf", "q": r"Un sommet de degré nul est dit isolé.", "bonne": True},
    {"notion": "terminologie", "type": "qcm", "q": r"Un graphe orienté simple complet d'ordre $n$ a combien d'arcs ?", "choix": [r"$n(n-1)$", r"$\frac{n(n-1)}2$", r"$n^2$", r"$2n$"], "bonne": 0},
    {"notion": "chemins", "type": "qcm", "q": r"Le coefficient $(M^3)_{xy}$ compte :", "choix": [r"les chemins de longueur $3$ de $x$ à $y$", r"les chemins de longueur $\le3$", r"les chemins élémentaires de $x$ à $y$", r"les arcs entre $x$ et $y$"], "bonne": 0},
    {"notion": "chemins", "type": "vf", "q": r"Un cycle élémentaire d'un graphe simple a au moins $3$ sommets.", "bonne": True},
    {"notion": "representations", "type": "qcm", "q": r"Tester l'existence d'un arc $(x,y)$ avec une matrice d'adjacence coûte :", "choix": [r"$O(1)$", r"$O(n)$", r"$O(d^{\circ+}(x))$", r"$O(n^2)$"], "bonne": 0},
    {"notion": "representations", "type": "vf", "q": r"Pour un graphe peu dense, les listes d'adjacence occupent moins de place que la matrice.", "bonne": True},
    {"notion": "representations", "type": "qcm", "q": r"Dans les listes d'adjacence d'un graphe non orienté, une arête $\{x,y\}$ apparaît :", "choix": [r"deux fois", r"une fois", r"jamais", r"trois fois"], "bonne": 0},
    {"notion": "parcours-largeur", "type": "qcm", "q": r"Dans un parcours en largeur, on marque un sommet :", "choix": [r"quand on l'enfile", r"quand on le défile", r"à la fin du parcours", r"jamais"], "bonne": 0},
    {"notion": "parcours-largeur", "type": "vf", "q": r"Le parcours en largeur donne les distances en nombre d'arêtes depuis le départ.", "bonne": True},
    {"notion": "parcours-profondeur", "type": "qcm", "q": r"L'ordre suffixe note un sommet :", "choix": [r"quand tous ses successeurs sont traités", r"à sa première rencontre", r"quand on l'enfile", r"quand il est isolé"], "bonne": 0},
    {"notion": "parcours-profondeur", "type": "vf", "q": r"La complexité d'un parcours en profondeur avec listes d'adjacence est $O(n+m)$.", "bonne": True},
    {"notion": "classification", "type": "qcm", "q": r"Dans un graphe non orienté, une arête non couvrante est :", "choix": [r"un arc arrière", r"un arc avant", r"un arc croisé", r"impossible"], "bonne": 0},
    {"notion": "classification", "type": "vf", "q": r"Un graphe orienté est sans circuit si et seulement si le parcours en profondeur ne rencontre aucun arc arrière.", "bonne": True},
    {"notion": "connexite", "type": "qcm", "q": r"La complexité de l'algorithme de Warshall pour $n$ sommets est :", "choix": [r"$O(n^3)$", r"$O(n^2)$", r"$O(n+m)$", r"$O(n\log n)$"], "bonne": 0},
    {"notion": "connexite", "type": "vf", "q": r"Un graphe non orienté est connexe si et seulement si un seul parcours depuis un sommet quelconque marque tous les sommets.", "bonne": True},
    {"notion": "trouver-reunir", "type": "qcm", "q": r"Dans le vecteur des pères, une racine est marquée par :", "choix": [r"une valeur négative", r"$0$", r"son propre numéro uniquement", r"$+\infty$"], "bonne": 0},
    {"notion": "trouver-reunir", "type": "vf", "q": r"L'union pondérée rattache le plus petit arbre à la racine du plus grand.", "bonne": True},
    {"notion": "applications", "type": "qcm", "q": r"Le rayon d'un graphe est :", "choix": [r"la plus petite excentricité", r"la plus grande excentricité", r"la somme des distances", r"le nombre de sommets du centre"], "bonne": 0},
    {"notion": "applications", "type": "vf", "q": r"Un graphe est biparti si et seulement si il ne contient aucun cycle de longueur impaire.", "bonne": True},
]

_FL = {
    1: r"`range(a, b, p)` : $\lfloor\frac{b-1-a}p\rfloor+1$ tours · boucle triangulaire $\frac{n(n-1)}2$ · doublement $\lceil\log_2 n\rceil$ · deux boucles imbriquées $n^2$",
    2: r"file : premier entré, premier sorti · pile : dernier entré, premier sorti · préfixe : racine puis fils · suffixe : fils puis racine · largeur : file",
    3: r"$\sum d^\circ=2m$ · $d^{\circ-}$ = somme de la colonne · $d^{\circ+}$ = somme de la ligne · complet : $\binom n2$ ou $n(n-1)$",
    4: r"$(M^k)_{xy}$ = chemins de longueur $k$ · $\operatorname{tr}(A^3)/6$ = triangles · accessibilité $(I+M)^{n-1}$",
    5: r"matrice $n^2$ cases, arc en $O(1)$ · listes $n+2m$ (non orienté), arc en $O(d^{\circ+}(x))$ · matrice symétrique si non orienté",
    6: r"file · marquer à l'enfilage · distances par niveaux · excentricité $=\max$ des distances · $O(n+m)$",
    7: r"préfixe : première rencontre · suffixe : dernière rencontre · récursion · $O(n+m)$ · relance sur les sommets non marqués",
    8: r"couvrant · avant : $\text{pref}[x]<\text{pref}[y]$, $\text{suff}[y]<\text{suff}[x]$ · arrière : $\text{pref}[y]<\text{pref}[x]$, $\text{suff}[x]<\text{suff}[y]$ · croisé : $\text{pref}[y]<\text{pref}[x]$, $\text{suff}[y]<\text{suff}[x]$",
    9: r"un arbre de la forêt = une composante · Warshall : $C[x,y]\leftarrow C[x,y]\lor(C[x,i]\land C[i,y])$ · rang de la fermeture = nombre de composantes · blocs $s^2$",
    10: r"racine : $p[x]<0$ · `trouver` remonte · `reunir` : $p[r_y]\leftarrow r_x$ · union pondérée : racine $=-$taille · hauteur $\le\log_2 n$ · compression des chemins",
    11: r"listes d'adjacence `G.adjlists[x]` · `Queue` : `enqueue`, `dequeue`, `isempty` · marquer à l'enfilage (BFS), à l'entrée (DFS) · vecteur d'entiers pour les composantes",
    12: r"BFS par niveaux · 2-coloration $3-c$ · arc arrière = marque « en cours » · arbre : $m=n-1$ et connexe · suffixe inverse = tri topologique · Euler : $0$ ou $2$ degrés impairs",
}
FORMULES = {}
for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["kind"] != "multi":
            FORMULES[_e["id"]] = _FL[_lvl["n"]]
FORMULES.update({
    "x1a": _FL[3], "x1b": _FL[7], "x1c": _FL[9], "x1d": _FL[9], "x1e": _FL[3], "x2a": _FL[3], "x3a": _FL[10], "x3b": _FL[3], "x3c": _FL[8],
    "x4a": _FL[9], "x4b": _FL[7], "x4c": _FL[9],
})
FORMULES.update({"g102": _FL[10], "g103": _FL[10]})

assert len(CHECKED) == len(set(CHECKED)), "duplicate exercise id"
_ids = [e["id"] for lvl in LEVELS for e in lvl["exos"]] + [e["id"] for e in EXTRA_PARTS]
assert len(_ids) == len(set(_ids)), "duplicate exercise id"
