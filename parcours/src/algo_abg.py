"""Level path: S2 algorithmics, binary and general trees (Algo-S2-ABG, exam B3 in March, Python).

Sources: no Moodle course for S2 algo on the server, so the path is calibrated on Epidocs Past-Exams (PDFs in
`annales/raw/S2`): TDs of January 2026 (`TDs/2030/Algo/B3`: recursion, binary and general trees), the B3 exams
of 12 March 2024 (`Midterms/Algo/2028/BST & GENERAL TREES`, scan), 5 March 2025 (`Midterms/Algo/2029/BST & GENERAL
TREES`) and 10 March 2026 (`Midterms/Algo/2030`, scan), and the official corrections of the older C2 tests (March
2019 and 2020, `Midterms/Algo/2023|2024`: leaves, equal, width, partially ordered tree, general tree measures).
Definitions (measures, internal/external nodes, hierarchical numbering, first child - right sibling) follow the
public EPITA algorithmics course mirror (https://algo.infoprepa.epita.fr, page « Structures arborescentes »):
height of the root = 0, PMI = LCI / number of internal nodes (points simples or doubles).

Checks at import (build.py imports this module, so a wrong answer stops the build):
- trees are written as nested tuples `(key, left, right)` (a bare value is a leaf, None the empty tree); every
  answer about a figure (orders, measures, numbers, conversions) is computed from that tuple, never typed by hand;
- `w()` runs the model code on `BinTree`/`Queue` objects built from the figures and replays the `>>>` session;
  returned trees are compared node by node (`outs`), and `fresh=True` also checks no input node is reused;
- `_api()` rejects models that break the exam annex: only `len`, `range`, `append`, `min`/`max` with two values,
  `BinTree`, `Queue` (`enqueue`, `dequeue`, `isempty`), `str`, `print`; no slice, no `in` test, no list operator;
- figures are drawn as SVG files in `static/arbres/` (name = hash of the drawing), shown as Markdown images.
"""
import ast
import collections
import contextlib
import hashlib
import html
import io
from fractions import Fraction
from pathlib import Path

from .algo_python import _out, _py, _session

SUBJECT = {
    "id": "algo-s2-abg",
    "ordre": 630,
    "matiere": "algo",
    "semestre": "S2",
    "ecue": "Arbres binaires et généraux",
    "titre": "Arbres binaires et généraux : récursion, mesures, parcours, constructions",
    "chapitres_moodle": [],
    "td": "TD Algo-S2-ABG de janvier 2026 (récursion, arbres binaires et généraux), examens B3 de 2024, 2025 et 2026",
    "examens": ["Examen écrit B3 d'algorithmique, arbres binaires et généraux (Python, 1 h 30 à 2 h, début mars)"],
}

CHECKED = []
FIG_DIR = Path(__file__).resolve().parents[2] / "static" / "arbres"
FIG_URL = "/static/arbres/"

# ---------------------------------------------------------------- trees (exam annex classes)


class BinTree:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right


class BinTreeSize:
    def __init__(self, key, left, right, size):
        self.key = key
        self.left = left
        self.right = right
        self.size = size


class Queue:
    def __init__(self):
        self._d = collections.deque()

    def enqueue(self, e):
        self._d.append(e)

    def dequeue(self):
        return self._d.popleft()

    def isempty(self):
        return not self._d


def key(s):
    return s[0] if isinstance(s, tuple) else s


def kids(s):
    return (s[1], s[2]) if isinstance(s, tuple) else (None, None)


def bt(s):
    """Tuple spec -> BinTree objects."""
    if s is None:
        return None
    left, right = kids(s)
    return BinTree(key(s), bt(left), bt(right))


def spec(B):
    """BinTree (or BinTreeSize) objects -> tuple spec."""
    if B is None:
        return None
    left, right = spec(B.left), spec(B.right)
    return B.key if left is None and right is None else (B.key, left, right)


def nodes(B):
    return [] if B is None else [B] + nodes(B.left) + nodes(B.right)


def pre(s):
    return [] if s is None else [key(s)] + pre(kids(s)[0]) + pre(kids(s)[1])


def ino(s):
    return [] if s is None else ino(kids(s)[0]) + [key(s)] + ino(kids(s)[1])


def post(s):
    return [] if s is None else post(kids(s)[0]) + post(kids(s)[1]) + [key(s)]


def levels(s):
    out, cur = [], [s] if s is not None else []
    while cur:
        out.append([key(x) for x in cur])
        cur = [c for x in cur for c in kids(x) if c is not None]
    return out


def bfs(s):
    return [k for lv in levels(s) for k in lv]


def _walk(s, d=0):
    """(key, depth, number of children) of every node, prefix order."""
    if s is None:
        return []
    left, right = kids(s)
    return [(key(s), d, (left is not None) + (right is not None))] + _walk(left, d + 1) + _walk(right, d + 1)


def measures(s, walk=_walk):
    w = walk(s)
    ext = [d for _, d, c in w if c == 0]
    inn = [d for _, d, c in w if c > 0]
    m = {"T": len(w), "H": max((d for _, d, _ in w), default=-1), "LC": sum(d for _, d, _ in w),
         "LCE": sum(ext), "LCI": sum(inn), "Nbe": len(ext), "Nbi": len(inn)}
    m["PM"] = Fraction(m["LC"], m["T"])
    m["PME"] = Fraction(m["LCE"], m["Nbe"])
    m["PMI"] = Fraction(m["LCI"], m["Nbi"]) if inn else Fraction(0)
    return m


def hier(s, n=1):
    """[(hierarchical number, key)] in prefix order."""
    if s is None:
        return []
    return [(n, key(s))] + hier(kids(s)[0], 2 * n) + hier(kids(s)[1], 2 * n + 1)


def occ(s, o=""):
    if s is None:
        return []
    return [(o or "ε", key(s))] + occ(kids(s)[0], o + "0") + occ(kids(s)[1], o + "1")


def rgd(s):
    if s is None:
        return "_"
    return f"⟨{key(s)}, {rgd(kids(s)[0])}, {rgd(kids(s)[1])}⟩"


def linear(s):
    if s is None:
        return "()"
    return f"({key(s)}{linear(kids(s)[0])}{linear(kids(s)[1])})"


def parse_linear(t):
    """Inverse of linear() for integer keys: '(5(2()())())' -> spec."""
    pos = 0

    def tree():
        nonlocal pos
        assert t[pos] == "("
        pos += 1
        if t[pos] == ")":
            pos += 1
            return None
        j = pos
        while t[pos] != "(":
            pos += 1
        k = int(t[j:pos])
        left, right = tree(), tree()
        assert t[pos] == ")"
        pos += 1
        return k if left is None and right is None else (k, left, right)

    s = tree()
    assert pos == len(t)
    return s


def kind(s):
    """Shapes of the course: dégénéré, complet, parfait, localement complet."""
    w, m = _walk(s), measures(s)
    out = []
    if all(c <= 1 for _, _, c in w):
        out.append("dégénéré")
    if m["T"] == 2 ** (m["H"] + 1) - 1:
        out.append("complet")
    hn = [n for n, _ in hier(s)]
    if max(hn) == m["T"]:  # numbers 1..n all used: perfect (parfait)
        out.append("parfait")
    if all(c != 1 for _, _, c in w):
        out.append("localement complet")
    return out


# general trees: (key, [children]) or a bare key for a leaf


def gkey(g):
    return g[0] if isinstance(g, tuple) else g


def gch(g):
    return g[1] if isinstance(g, tuple) else []


def gpre(g):
    return [gkey(g)] + [k for c in gch(g) for k in gpre(c)]


def gpost(g):
    return [k for c in gch(g) for k in gpost(c)] + [gkey(g)]


def gbfs(g):
    out, cur = [], [g]
    while cur:
        out += [gkey(x) for x in cur]
        cur = [c for x in cur for c in gch(x)]
    return out


def _gwalk(g, d=0):
    return [(gkey(g), d, len(gch(g)))] + [x for c in gch(g) for x in _gwalk(c, d + 1)]


def fcrs(forest):
    """First child - right sibling binary form of a forest (list of general trees)."""
    if not forest:
        return None
    g = forest[0]
    left, right = fcrs(gch(g)), fcrs(forest[1:])
    return gkey(g) if left is None and right is None else (gkey(g), left, right)


def from_fcrs(s):
    """Inverse: binary first child - right sibling -> list of general trees."""
    out = []
    while s is not None:
        ch = from_fcrs(kids(s)[0])
        out.append((key(s), ch) if ch else key(s))
        s = kids(s)[1]
    return out


# ---------------------------------------------------------------- figures (SVG files)

_R, _DX, _DY, _CAP = 14, 30, 46, 24


def _bin_nodes(s, d, acc, edges):
    left, right = kids(s)
    li = _bin_nodes(left, d + 1, acc, edges) if left is not None else None
    me = len(acc)
    acc.append((me, d, key(s)))
    ri = _bin_nodes(right, d + 1, acc, edges) if right is not None else None
    edges += [(me, i) for i in (li, ri) if i is not None]
    return me


def _gen_nodes(g, d, acc, edges, cnt):
    idx = len(acc)
    acc.append(None)
    cis = [_gen_nodes(c, d + 1, acc, edges, cnt) for c in gch(g)]
    if cis:
        x = (acc[cis[0]][0] + acc[cis[-1]][0]) / 2
    else:
        x, cnt[0] = cnt[0], cnt[0] + 1.25  # sibling leaves share a level: more room than in-order slots
    acc[idx] = (x, d, gkey(g))
    edges += [(idx, c) for c in cis]
    return idx


def _label(k):
    return "" if k is None else html.escape(str(k))


def fig(*items, general=False):
    """Markdown image of one or more trees side by side: items = (caption, spec) pairs."""
    parts, x0, y0, row_h, width = [], 10, 10, 0, 0
    for cap, s in items:
        acc, edges = [], []
        if s is None:
            acc = []
        elif general:
            _gen_nodes(s, 0, acc, edges, [0])
        else:
            _bin_nodes(s, 0, acc, edges)
        w = max([_DX] + [(x + 1) * _DX for x, _, _ in acc]) + 10
        h = (max((d for _, d, _ in acc), default=0) + 1) * _DY + (_CAP if cap else 0)
        if x0 > 10 and x0 + w > 380:  # keep phone scale close to 1
            x0, y0, row_h = 10, y0 + row_h + 12, 0
        px = lambda i: x0 + acc[i][0] * _DX + _DX / 2  # noqa: E731
        py = lambda i: y0 + acc[i][1] * _DY + _R + 4  # noqa: E731
        for a, b in edges:
            parts.append(f'<line x1="{px(a):.1f}" y1="{py(a):.1f}" x2="{px(b):.1f}" y2="{py(b):.1f}"/>')
        for i, (_, _, k) in enumerate(acc):
            parts.append(f'<circle cx="{px(i):.1f}" cy="{py(i):.1f}" r="{_R}"/>'
                         f'<text x="{px(i):.1f}" y="{py(i) + 5:.1f}">{_label(k)}</text>')
        if not acc:
            parts.append(f'<text x="{x0 + w / 2:.1f}" y="{y0 + 22}">vide</text>')
        if cap:
            parts.append(f'<text class="c" x="{x0 + w / 2:.1f}" y="{y0 + h - 6:.1f}">{html.escape(cap)}</text>')
        x0 += w + 24
        row_h = max(row_h, h)
        width = max(width, x0)
    W, H = int(width - 14), int(y0 + row_h + 10)  # drop the trailing gap
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
           'font-family="JetBrains Mono, Menlo, Consolas, monospace" font-size="14" text-anchor="middle">'
           '<style>line{stroke:#111;stroke-width:1.5}circle{fill:#fff;stroke:#111;stroke-width:1.5}'
           'text{fill:#111}.c{font-size:15px;font-weight:700}</style>' + "".join(parts) + "</svg>")
    name = "abg-" + hashlib.sha1(svg.encode()).hexdigest()[:12] + ".svg"
    path = FIG_DIR / name
    if not path.exists() or path.read_text() != svg:
        FIG_DIR.mkdir(parents=True, exist_ok=True)
        path.write_text(svg)
    alt = " ; ".join(f"{c} = {rgd(s) if not general else s}" for c, s in items).replace("[", "(").replace("]", ")")
    return f"![{alt}]({FIG_URL}{name})"


def gfig(*items):
    return fig(*items, general=True)


# ---------------------------------------------------------------- exercise builders

ALLOWED = {"len", "range", "min", "max", "BinTree", "BinTreeSize", "Queue", "str", "print", "Exception"}
METHODS = {"append", "enqueue", "dequeue", "isempty"}


def _api(code, extra=(), methods=()):
    """Exam annex check; `extra`/`methods`: names and methods another path's annex adds."""
    tree = ast.parse(code)
    defined = {n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}
    for n in ast.walk(tree):
        bad = None
        if isinstance(n, ast.Call):
            f = n.func
            if isinstance(f, ast.Name) and f.id not in ALLOWED | set(extra) | defined:
                bad = f"function {f.id}"
            elif isinstance(f, ast.Name) and f.id in ("min", "max") and len(n.args) != 2:
                bad = f"{f.id} with {len(n.args)} values"
            elif isinstance(f, ast.Attribute) and f.attr not in METHODS | set(methods):
                bad = f"method {f.attr}"
        elif isinstance(n, ast.Slice):
            bad = "slice"
        elif isinstance(n, ast.Compare) and any(isinstance(op, (ast.In, ast.NotIn)) for op in n.ops):
            bad = "`in` test"
        elif isinstance(n, ast.BinOp) and (isinstance(n.left, ast.List) or isinstance(n.right, ast.List)):
            bad = "operator on a list"
        elif isinstance(n, (ast.ListComp, ast.GeneratorExp, ast.Import, ast.ImportFrom, ast.Lambda)):
            bad = type(n).__name__
        assert not bad, f"exam rule broken ({bad}) in:\n{code}"


def _ns(code, trees):
    ns = {"BinTree": BinTree, "BinTreeSize": BinTreeSize, "Queue": Queue}
    ns.update({k: bt(s) for k, s in trees.items()})
    exec(code, ns)
    return ns


def _w(enonce, code, tests, sol, trees, outs, fresh, api, figs):
    code = code.strip()
    if api:
        _api(code)
    ns = _ns(code, trees)
    for line, exp in tests:
        if exp is None:
            exec(line, ns)
            continue
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                got = repr(eval(line, ns))
        except Exception as e:  # noqa: BLE001 - the statement shows the exception message
            got = f"Exception: {e}"
        assert got == exp, f"{line}: got {got}, expected {exp}\n{code}"
    for expr, exp in outs:
        ns = _ns(code, trees)
        before = {id(x) for name in trees for x in nodes(ns[name])}
        res = eval(expr, ns)
        assert spec(res) == exp, f"{expr}: got {spec(res)}, expected {exp}"
        if fresh:
            assert not {id(x) for x in nodes(res)} & before, f"{expr}: reuses input nodes"
    text = enonce
    if figs is None:
        figs = [(k, s) for k, s in trees.items()]
    if figs:
        text += "\n\n" + fig(*figs)
    if tests:
        text += f"\n\nExemples d'applications :\n\n{_out(_session(tests))}"
    if outs:
        text += "\n\nRésultats attendus :\n\n" + fig(*outs)
    return {"enonce": text, "sol": _py(code) + (f"\n\n{sol}" if sol else "")}


def w(id, enonce, code, tests, sol="", trees=None, outs=(), fresh=False, src=None, duree=8, api=True, figs=None):
    """« Write the function » exercise: the model code replays the session on the figures' trees."""
    CHECKED.append(id)
    return {"id": id, "kind": "open", **_w(enonce, code, tests, sol, trees or {}, outs, fresh, api, figs),
            "src": src or S, "duree": duree}


def wv(enonce, code, tests, sol="", trees=None, outs=(), fresh=False, figs=None):
    return _w(enonce, code, tests, sol, trees or {}, outs, fresh, True, figs)


def v(id, enonce, ans, sol, src=None, duree=2):
    """Value exercise; `ans` is computed (Fraction, int), never typed by hand."""
    a = str(ans)
    return {"id": id, "kind": "value", "enonce": enonce, "calc": a, "ans": a, "sol": f"**Réponse :** ${a}$\n\n{sol}",
            "src": src or S, "duree": duree}


def vv(enonce, ans, sol):
    a = str(ans)
    return {"enonce": enonce, "calc": a, "ans": a, "sol": f"**Réponse :** ${a}$\n\n{sol}"}


def o(id, enonce, sol, src=None, duree=4):
    return {"id": id, "kind": "open", "enonce": enonce, "sol": sol, "src": src or S, "duree": duree}


def _output(code, expect):
    """Value of OUTPUT after running `code`, or the error raised; `expect` must appear in it."""
    ns = {}
    try:
        exec(code, ns)
        got = repr(ns["OUTPUT"])
    except Exception as e:  # noqa: BLE001
        got = f"{type(e).__name__}: {e}"
    assert expect in got, f"OUTPUT: got {got}, expected {expect}"
    return got


def seq(L):
    return ", ".join(map(str, L))


def frac(f):
    f = Fraction(f)
    return str(f.numerator) if f.denominator == 1 else f"{f.numerator}/{f.denominator}"


def frac_tex(f):
    f = Fraction(f)
    return f"{f.numerator}" if f.denominator == 1 else rf"\dfrac{{{f.numerator}}}{{{f.denominator}}} \approx {float(f):.2f}"


S = "Calé sur le TD Algo-S2-ABG (janvier 2026) et les examens B3 (Past-Exams S2/Midterms/Algo)"
TD = "TD Algo-S2-ABG, janvier 2026 (Past-Exams S2/TDs/2030/Algo/B3)"
TDR = "TD 1 récursion, janvier 2026 (Past-Exams S2/TDs/2030/Algo/B3)"
C19 = "Contrôle C2, 4 mars 2019, corrigé officiel (Past-Exams S2/Midterms/Algo/2023)"
C20 = "Contrôle C2, 2 mars 2020, corrigé officiel (Past-Exams S2/Midterms/Algo/2024)"
B24 = "Examen B3, 12 mars 2024 (Past-Exams S2/Midterms/Algo/2028), pas de corrigé officiel"
B25 = "Examen B3, 5 mars 2025 (Past-Exams S2/Midterms/Algo/2029), pas de corrigé officiel"
B26 = "Examen B3, 10 mars 2026 (Past-Exams S2/Midterms/Algo/2030), pas de corrigé officiel"
RULE = ("Annexe de l'examen : arbre vide `None`, sinon `BinTree` (`key`, `left`, `right`) ; file `Queue()` avec "
        "`enqueue`, `dequeue`, `isempty` ; seuls `len`, `range`, `append`, et `min`/`max` sur deux entiers.")

# ---------------------------------------------------------------- trees of the figures

# TD Algo-S2-ABG, figure B5 (loaded from its linear form, exercise 7.4)
TD_LIN = "(5(2(-1(4()())())(0()(11()())))(12()(1(-2()(15()()))())))"
B = parse_linear(TD_LIN)
assert B == (5, (2, (-1, 4, None), (0, None, 11)), (12, None, (1, (-2, None, 15), None)))
# exam 10 March 2026, tree B1 of exercises 1 and 4: B with a left child 4 under 12
E26 = (5, (2, (-1, 4, None), (0, None, 11)), (12, 4, (1, (-2, None, 15), None)))
# small trees used for drills
T1 = ("A", ("B", "D", ("E", "G", None)), ("C", None, ("F", "H", "I")))
T2 = (8, (3, 1, (6, 4, 7)), (10, None, (14, 13, None)))
T3 = (1, (2, (4, 8, 9), (5, 10, 11)), (3, (6, 12, 13), (7, 14, 15)))  # complete, height 3
T4 = (1, (2, 4, 5), (3, 6, None))  # perfect, not complete
T5 = (1, None, (2, (3, None, 4), None))  # degenerate
T6 = (1, (2, 4, (5, 6, 7)), 3)  # locally complete

m_B, m_T1, m_T2 = measures(B), measures(T1), measures(T2)
assert (m_B["T"], m_B["H"], m_B["LC"]) == (10, 4, 21)
assert kind(T3) == ["complet", "parfait", "localement complet"] and kind(T4) == ["parfait"]
assert kind(T5) == ["dégénéré"] and kind(T6) == ["localement complet"]

# general tree of the B3 exam of 5 March 2025 (figure 9, given in first child - right sibling form)
A25_BIN = ("E", ("B", ("I", None, "G"), ("D", None, ("K", ("A", None, ("F", None, "J")), ("C", "H", None)))), None)
A25 = from_fcrs(A25_BIN)[0]
assert A25 == ("E", [("B", ["I", "G"]), "D", ("K", ["A", "F", "J"]), ("C", ["H"])]) and fcrs([A25]) == A25_BIN
m_A25 = measures(A25, _gwalk)
# general tree of the B3 exam of 12 March 2024 (rebuilt from its prefix and suffix orders)
A24 = ("E", [("D", ["J", "I", "C"]), "H", ("A", ["B", ("F", ["G"])])])
assert "".join(gpre(A24)) == "EDJICHABFG" and "".join(gpost(A24)) == "JICDHBGFAE"
# general tree for drills
G1 = ("R", [("S", ["U", "V"]), "T", ("W", [("X", ["Z"]), "Y"])])
m_G1 = measures(G1, _gwalk)

# ---------------------------------------------------------------- model code shared by several levels

SIZE = '''def size(B):
    if B == None:
        return 0
    else:
        return 1 + size(B.left) + size(B.right)'''

HEIGHT = '''def height(B):
    if B == None:
        return -1
    else:
        return 1 + max(height(B.left), height(B.right))'''

FACT_A = "def fact(n):\n    if n < 2:\n        return 1\n    else:\n        fact(n - 1)\nOUTPUT = fact(4)"
FACT_C = ("def rec_fact(n, res):\n    if n < 2:\n        return res\n    else:\n        res = res * rec_fact(n - 1, res)\n"
          "def fact(n):\n    res = 1\n    rec_fact(n, res)\nOUTPUT = fact(4)")
FACT_D = ("def rec_fact(n, res):\n    if n < 2:\n        return res\n    else:\n        res = res * rec_fact(n - 1, res)\n"
          "        return res\ndef fact(n):\n    res = 1\n    return rec_fact(n, res)\nOUTPUT = fact(4)")
OUTQ = "Valeur de `OUTPUT` après l'exécution du programme ? Si une erreur se produit, préciser sa nature."

MYST26 = '''def aux_mystery(B, a):
    if B.left == None:
        if B.right == None:
            if a == 0:
                return None
            else:
                return B
        else:
            if a == 0:
                return B.right
            else:
                B.right = aux_mystery(B.right, a-1)
    else:
        if B.right == None:
            if a == 0:
                return B.left
            else:
                B.left = aux_mystery(B.left, a-1)
        else:
            B.left = aux_mystery(B.left, a-1)
            B.right = aux_mystery(B.right, a-1)
    return B

def mystery(B, a):
    if B == None:
        return None
    else:
        return aux_mystery(B, a)'''

MYST24 = '''def mystery(B):
    if B == None:
        return (None, 0)
    else:
        C = BinTree(0, None, None)
        C.left, b = mystery(B.left)
        if B.left != None:
            if B.right != None:
                b = b + 1
        C.right, d = mystery(B.right)
        C.key = b + d
        return (C, C.key)'''

BQUID = ("V", ("D", ("I", ("Q", None, "U"), None), ("S", "E", "T")), ("I", ("E", None, "R"), ("A", "T", "S")))
_m24 = _ns(MYST24, {"Bquid": BQUID})
MYST24_RES = spec(eval("mystery(Bquid)", _m24)[0])
_m26 = _ns(MYST26, {"B": E26})
MYST26_RES = spec(eval("mystery(B, 3)", _m26))
_m26b = _ns(MYST26, {"B": E26})
MYST26_RES1 = spec(eval("mystery(B, 2)", _m26b))
assert MYST24_RES == (5, (2, (0, (0, None, 0), None), (1, 0, 0)), (2, (0, None, 0), (1, 0, 0)))

# Huffman tree of the TD (exercise 4.4): internal nodes have no key
HT = (None, "a", (None, (None, "u", "n"), (None, (None, "f", "m"), "H")))
CODE = {"a": "0", "f": "1100", "H": "111", "m": "1101", "n": "101", "u": "100"}


def _decode(bits, codes):
    inv, out, cur = {c: k for k, c in codes.items()}, "", ""
    for b in bits:
        cur += b
        if cur in inv:
            out, cur = out + inv[cur], ""
    assert cur == ""
    return out


DECODED = _decode("1111001100110011010101", CODE)


def _codes_of(s, c=""):
    left, right = kids(s)
    if left is None:
        return {key(s): c}
    return _codes_of(left, c + "0") | _codes_of(right, c + "1")


assert _codes_of(HT) == CODE

# ---------------------------------------------------------------- course

NOTIONS = [
    {"id": "recursion", "titre": "Récursion : cas d'arrêt, valeur retournée, paramètres",
     "formule": r"cas d'arrêt d'abord · chaque branche fait `return` · un paramètre est local : le modifier ne change rien chez l'appelant · renvoyer un couple pour remonter deux résultats",
     "exemple": r"`fibo_calls(4)` renvoie `(5, 9)` : valeur et nombre d'appels",
     "cours": r"Une fonction récursive s'appelle sur un problème plus petit jusqu'au cas d'arrêt. Le résultat d'un appel récursif est perdu s'il n'est ni retourné ni utilisé. Un compteur passé en paramètre ne remonte pas : on le renvoie avec la valeur (couple)."},
    {"id": "vocabulaire", "titre": "Vocabulaire : racine, fils, feuilles, points simples et doubles",
     "formule": r"$B=\langle r, G, D\rangle$ · point double : deux fils (nœud interne) · point simple à gauche / à droite : un seul fils (nœud interne) · feuille : aucun fils (nœud externe) · branche : chemin racine $\to$ feuille · autant de branches que de feuilles · bord gauche : liens gauches depuis la racine",
     "exemple": r"`⟨1, ⟨2, _, _⟩, _⟩` : $1$ est un point simple à gauche, $2$ une feuille",
     "cours": r"Un arbre binaire est vide ou formé d'une racine et de deux sous-arbres $G$ et $D$. Le nœud racine de $G$ est le fils gauche. Les nœuds internes ont au moins un fils, les nœuds externes (feuilles) aucun."},
    {"id": "mesures", "titre": "Mesures : taille, hauteur, cheminements, profondeurs moyennes",
     "formule": r"$T(B)$ : nombre de nœuds · $H(\text{racine})=0$, $H(x)=1+H(\text{père})$ · $H(B)=\max H(x)$ (arbre vide : $-1$) · $LC=\sum H(x)$ · $LCE$ : sur les feuilles · $LCI$ : sur les nœuds internes · $LC=LCE+LCI$ · $PM=LC/T$ · $PME=LCE/N_e$ · $PMI=LCI/N_i$",
     "exemple": r"$\langle 1, 2, 3\rangle$ : $T=3$, $H=1$, $LC=2$, $LCE=2$, $LCI=0$, $PME=1$",
     "cours": r"La profondeur (hauteur, niveau) d'un nœud compte les liens depuis la racine. La profondeur moyenne externe sert à mesurer le coût moyen d'une recherche qui aboutit à une feuille."},
    {"id": "particuliers", "titre": "Arbres particuliers : dégénéré, complet, parfait, localement complet",
     "formule": r"dégénéré : chaque nœud a au plus un fils, $T=H+1$ · complet : tous les niveaux pleins, $T=2^{H+1}-1$, $2^H$ feuilles · parfait : niveaux pleins sauf le dernier, rempli à gauche, $H=\lfloor\log_2 T\rfloor$ · localement complet : aucun point simple, $T=2N_e-1$ · pour tout arbre : $\lfloor\log_2 T\rfloor\le H\le T-1$",
     "exemple": r"un arbre complet de hauteur $3$ a $15$ nœuds et $8$ feuilles",
     "cours": r"Dans un arbre parfait, les numéros hiérarchiques des nœuds sont exactement $1, 2, \dots, T$ : on peut le ranger dans un tableau sans trou (c'est le tas du module suivant)."},
    {"id": "hierarchique", "titre": "Numérotation hiérarchique et occurrences",
     "formule": r"racine : $1$ · fils gauche de $i$ : $2i$ · fils droit : $2i+1$ · père : $\lfloor i/2\rfloor$ · niveau de $i$ : $\lfloor\log_2 i\rfloor$ · occurrence : racine $\varepsilon$, puis $0$ à gauche et $1$ à droite",
     "exemple": r"le fils droit du nœud $6$ est $13$ ; son occurrence est $101$",
     "cours": r"Le numéro hiérarchique est l'indice du nœud dans le parcours en largeur d'un arbre complet. Vecteur hiérarchique : case $i$ = clé du nœud $i$, `None` si absent (case $0$ inutilisée)."},
    {"id": "profondeur", "titre": "Parcours en profondeur : ordres préfixe, infixe, suffixe",
     "formule": r"main gauche : chaque nœud est rencontré $3$ fois · préfixe : 1re rencontre (avant $G$) · infixe : 2e (entre $G$ et $D$) · suffixe : 3e (après $D$) · rang de la racine : préfixe $1$, infixe $T(G)+1$, suffixe $T(B)$",
     "exemple": r"$\langle 1, 2, 3\rangle$ : préfixe $1, 2, 3$ ; infixe $2, 1, 3$ ; suffixe $2, 3, 1$",
     "cours": r"Le parcours profondeur est récursif : traitement préfixe, appel sur le fils gauche, traitement infixe, appel sur le fils droit, traitement suffixe. Il coûte $O(T)$."},
    {"id": "largeur", "titre": "Parcours en largeur avec une file",
     "formule": r"enfiler la racine · tant que la file n'est pas vide : défiler, traiter, enfiler les fils non vides · changement de niveau : marqueur `None` (ou deux files)",
     "exemple": r"$\langle 1, \langle 2, 4, \_\rangle, 3\rangle$ : $1, 2, 3, 4$",
     "cours": r"Le parcours largeur (ordre hiérarchique) est itératif. Pour travailler niveau par niveau (largeur, sommes), on enfile `None` après chaque niveau : quand on le défile, le niveau est fini et on le réenfile si la file n'est pas vide."},
    {"id": "construction", "titre": "Construire et tester des arbres",
     "formule": r"construire : `BinTree(clé, construire(G), construire(D))` · ne jamais réutiliser un nœud d'entrée si l'énoncé l'interdit · test : `and` paresseux, s'arrête au premier échec · remonter plusieurs infos : renvoyer un couple",
     "exemple": r"`transpose(B)` : `BinTree(2 * B.key, transpose(B.right), transpose(B.left))`",
     "cours": r"Une construction récursive crée un nœud par appel et renvoie l'arbre construit. Un test récursif renvoie `False` dès qu'un nœud viole la propriété ; un paramètre supplémentaire (clé du père, niveau, longueur courante) transporte l'information qui descend."},
    {"id": "generaux", "titre": "Arbres généraux : premier fils - frère droit",
     "formule": r"$A=\langle o, A_1, \dots, A_n\rangle$ · lien gauche $=$ premier fils · lien droit $=$ frère droit · mêmes nœuds (bijection) · préfixe général $=$ préfixe du binaire · suffixe général $=$ infixe du binaire · nœud interne : au moins un fils",
     "exemple": r"`⟨A, B, C⟩` devient `⟨A, ⟨B, _, ⟨C, _, _⟩⟩, _⟩`",
     "cours": r"Un arbre général a un nombre quelconque de fils (une forêt). Sa forme binaire premier fils - frère droit permet de réutiliser les algorithmes des arbres binaires. Les mesures (taille, hauteur, cheminements) sont celles de l'arbre général, pas de sa forme binaire."},
]

# ---------------------------------------------------------------- levels


def _mes_sol(m):
    return (rf"Profondeurs : feuilles $LCE={m['LCE']}$ sur $N_e={m['Nbe']}$ feuilles, nœuds internes $LCI={m['LCI']}$ "
            rf"sur $N_i={m['Nbi']}$, $LC={m['LC']}$, $T={m['T']}$, $H={m['H']}$.")


_wB = _walk(B)
SIMPLE_B = [k for k, _, c in _wB if c == 1]
DOUBLE_B = [k for k, _, c in _wB if c == 2]
LEAVES_B = [k for k, _, c in _wB if c == 0]
H_B = dict(hier(B))
HN = {k: n for n, k in hier(B)}
V_T4 = [None] * (max(n for n, _ in hier(T4)) + 1)
for _n, _k in hier(T4):
    V_T4[_n] = _k
V_GAP = [None, "A", "B", "C", None, "D", "E", None, None, None, "F"]
GAP = ("A", ("B", None, ("D", "F", None)), ("C", "E", None))
assert [k for _, k in sorted(hier(GAP))] == [x for x in V_GAP if x] and max(n for n, _ in hier(GAP)) == 10

LEVELS = [
    {"n": 1, "titre": "Récursion : retour, paramètres, compteurs", "notions": ["recursion"], "exos": [
        o("a11", f"{OUTQ}\n\n{_py(FACT_A)}",
          f"**`OUTPUT` vaut** `{_output(FACT_A, 'None')}`.\n\nLa branche récursive appelle `fact(n - 1)` sans `return` : "
          "le résultat est perdu et la fonction renvoie `None`.", src=TDR, duree=2),
        o("a12", f"{OUTQ}\n\n{_py(FACT_C)}",
          f"**Erreur :** `{_output(FACT_C, 'TypeError')}`.\n\n`rec_fact(1, 1)` renvoie `1`, mais `rec_fact(2, 1)` n'a pas de "
          "`return` dans sa branche récursive : il renvoie `None`, et `rec_fact(3, 1)` calcule `1 * None`.", src=TDR, duree=3),
        o("a13", f"{OUTQ}\n\n{_py(FACT_D)}",
          f"**`OUTPUT` vaut** `{_output(FACT_D, '1')}`.\n\n`res` vaut $1$ à chaque appel : on calcule $1\\times1\\times1\\times1$. "
          "Il faudrait multiplier par `n` : `return n * rec_fact(n - 1, res)`, ou accumuler `rec_fact(n - 1, res * n)`.", src=TDR, duree=3),
        w("a14", r"Écrire la fonction `fibo_calls(n)` qui renvoie le couple `(value, nb_calls)` : $\mathrm{fibo}(n)$ (avec $\mathrm{fibo}(n)=1$ si $n\le1$) et le nombre total d'appels récursifs effectués.",
          "def fibo_calls(n):\n    if n < 2:\n        return (1, 1)\n    else:\n        (a, c1) = fibo_calls(n - 1)\n        (b, c2) = fibo_calls(n - 2)\n        return (a + b, c1 + c2 + 1)",
          [("fibo_calls(0)", "(1, 1)"), ("fibo_calls(1)", "(1, 1)"), ("fibo_calls(4)", "(5, 9)")],
          r"Un compteur passé en paramètre (`nb_calls += 1`) ne modifie que la copie locale : chaque appel renvoie son propre nombre d'appels, et l'appelant fait la somme $+1$. Le TD affiche `(3, 9)` pour $n=4$ : c'est une coquille, $\mathrm{fibo}(4)=5$.",
          src=TDR, duree=6),
        w("a15", r"Écrire la fonction récursive `reverse(n)` qui renvoie le nombre formé par les chiffres de l'entier $n$ dans l'ordre inverse (le signe est conservé).",
          "def _reverse(n, acc):\n    \"\"\"n >= 0: digits of n appended in reverse order after acc\"\"\"\n    if n == 0:\n        return acc\n    else:\n        return _reverse(n // 10, acc * 10 + n % 10)\n\ndef reverse(n):\n    if n < 0:\n        return -_reverse(-n, 0)\n    else:\n        return _reverse(n, 0)",
          [("reverse(1234)", "4321"), ("reverse(5089)", "9805"), ("reverse(-5089)", "-9805"), ("reverse(0)", "0")],
          r"L'accumulateur reçoit les chiffres de droite à gauche : `acc * 10 + n % 10`.", src=TDR, duree=6),
        w("a16", r"La version du TD de la recherche dichotomique récursive (`right` exclu, appel initial `(0, len(L))`) oublie le `return` devant les appels récursifs et teste `left > right`. Écrire la version correcte `binary_search(L, x)` : indice de `x` dans la liste triée `L`, $-1$ s'il est absent.",
          "def _bs(L, x, left, right):\n    \"\"\"search x in L[left:right], right excluded\"\"\"\n    if left >= right:\n        return -1\n    else:\n        mid = left + (right - left) // 2\n        if x == L[mid]:\n            return mid\n        elif x < L[mid]:\n            return _bs(L, x, left, mid)\n        else:\n            return _bs(L, x, mid + 1, right)\n\ndef binary_search(L, x):\n    return _bs(L, x, 0, len(L))",
          [("binary_search([1, 3, 5, 8], 5)", "2"), ("binary_search([1, 3, 5, 8], 9)", "-1"), ("binary_search([], 4)", "-1")],
          r"Sans `return`, le résultat de l'appel récursif est perdu (`None`). Avec `right` exclu, l'intervalle est vide dès que `left == right` : avec `left > right`, on lit `L[len(L)]` (`IndexError`) en cherchant une valeur plus grande que toutes.",
          src=TDR, duree=6),
    ]},
    {"n": 2, "titre": "Vocabulaire des arbres binaires", "notions": ["vocabulaire"], "exos": [
        v("a21", f"Combien l'arbre $B$ ci-dessous a-t-il de feuilles ?\n\n{fig(('B', B))}", len(LEAVES_B),
          f"Feuilles (aucun fils) : ${seq(LEAVES_B)}$. Autant de branches que de feuilles.", src=TD),
        v("a22", f"Combien l'arbre $B$ a-t-il de points simples ?\n\n{fig(('B', B))}", len(SIMPLE_B),
          f"Un seul fils : ${seq(SIMPLE_B)}$. Points doubles : ${seq(DOUBLE_B)}$.", src=TD),
        o("a23", f"Donner le bord gauche et le bord droit de l'arbre $T$.\n\n{fig(('T', T1))}",
          "Bord gauche (liens gauches depuis la racine) : A, B, D. Bord droit : A, C, F, I.", duree=2),
        o("a24", f"Dans l'arbre $T$, donner les branches, puis les nœuds internes et les nœuds externes.\n\n{fig(('T', T1))}",
          "Branches : (A, B, D), (A, B, E, G), (A, C, F, H), (A, C, F, I) : 4 branches pour 4 feuilles.\n\n"
          f"Nœuds internes : {seq(k for k, _, c in _walk(T1) if c)}. Externes (feuilles) : {seq(k for k, _, c in _walk(T1) if not c)}.", duree=3),
        o("a25", f"Donner l'arbre $T$ sous la forme ⟨r, G, D⟩, avec \\_ pour l'arbre vide.\n\n{fig(('T', T2))}",
          f"`{rgd(T2)}`", src=TD, duree=3),
    ]},
    {"n": 3, "titre": "Mesures : taille, hauteur, cheminements", "notions": ["mesures"], "exos": [
        v("a31", f"Hauteur de l'arbre $B$ ?\n\n{fig(('B', B))}", m_B["H"], "La feuille $15$ est à la profondeur $4$.", src=TD),
        v("a32", f"Longueur de cheminement $LC$ de l'arbre $B$ ?\n\n{fig(('B', B))}", m_B["LC"], _mes_sol(m_B), src=TD),
        v("a33", f"Profondeur moyenne externe $PME$ de l'arbre $B$ (fraction) ?\n\n{fig(('B', B))}", frac(m_B["PME"]),
          rf"$PME=LCE/N_e$ : feuilles ${seq(LEAVES_B)}$ aux profondeurs $3, 3, 4$, soit ${frac_tex(m_B['PME'])}$.", src=TD),
        v("a34", f"Profondeur moyenne interne $PMI$ de l'arbre $T$ (fraction) ?\n\n{fig(('T', T1))}", frac(m_T1["PMI"]),
          rf"Nœuds internes : points simples et doubles. ${frac_tex(m_T1['PMI'])}$. " + _mes_sol(m_T1), duree=3),
        v("a35", f"Profondeur moyenne $PM$ de l'arbre $T$ (fraction) ?\n\n{fig(('T', T2))}", frac(m_T2["PM"]),
          rf"$PM=LC/T$ : ${frac_tex(m_T2['PM'])}$. " + _mes_sol(m_T2), duree=3),
    ]},
    {"n": 4, "titre": "Arbres particuliers", "notions": ["particuliers", "mesures"], "exos": [
        v("a41", r"Taille d'un arbre binaire complet de hauteur $5$ ?", 2 ** 6 - 1, r"$T=2^{H+1}-1=2^6-1$."),
        v("a42", r"Hauteur d'un arbre binaire parfait de $100$ nœuds ?", 6, r"$2^6=64\le100<128=2^7$ : $H=\lfloor\log_2 100\rfloor$."),
        v("a43", r"Hauteur maximale, puis minimale, d'un arbre binaire de $20$ nœuds ? (donner la maximale)", 19,
          r"Maximale : arbre dégénéré, $H=T-1=19$. Minimale : arbre parfait, $\lfloor\log_2 20\rfloor=4$."),
        v("a44", r"Un arbre localement complet a $12$ feuilles. Combien a-t-il de nœuds ?", 23,
          r"Chaque point double ajoute une feuille : $N_e=N_i+1$, donc $T=2N_e-1=23$."),
        o("a45", f"Pour chacun des arbres, dire s'il est dégénéré, complet, parfait, localement complet.\n\n"
          f"{fig(('T3', T3), ('T4', T4), ('T5', T5), ('T6', T6))}",
          "\n\n".join(f"**{n}** : {', '.join(kind(s))}" for n, s in (("T3", T3), ("T4", T4), ("T5", T5), ("T6", T6)))
          + "\n\nUn arbre complet est aussi parfait et localement complet.", duree=4),
    ]},
    {"n": 5, "titre": "Numérotation hiérarchique et occurrences", "notions": ["hierarchique"], "exos": [
        v("a51", f"Numéro hiérarchique du nœud $15$ dans l'arbre $B$ ?\n\n{fig(('B', B))}", HN[15],
          f"Chemin $5\\to12\\to1\\to-2\\to15$ : droite, gauche, gauche, droite. $1\\to3\\to6\\to12\\to25$.", src=TD),
        o("a52", f"Donner la liste des numéros hiérarchiques des nœuds de l'arbre $T$, dans l'ordre croissant.\n\n{fig(('T', T2))}",
          seq(sorted(n for n, _ in hier(T2))), src=C19),
        v("a53", r"Dans la numérotation hiérarchique, quel est le numéro du père du nœud $45$ ? (puis son niveau)", 22,
          r"Père : $\lfloor 45/2\rfloor=22$. Niveau de $45$ : $\lfloor\log_2 45\rfloor=5$."),
        o("a54", f"Donner la liste d'occurrences de l'arbre $T$ (racine $\\varepsilon$, $0$ à gauche, $1$ à droite).\n\n{fig(('T', T1))}",
          ", ".join(f"{k} : {c}" for c, k in occ(T1)), src=TD),
        o("a55", f"Dessiner l'arbre dont le vecteur hiérarchique (case $0$ inutilisée) est :\n\n{_out(repr(V_GAP))}",
          fig(("", GAP)) + "\n\nCase $i$ : fils en $2i$ et $2i+1$. $F$ en case $10$ est le fils gauche de $D$ (case $5$).", src=TD),
    ]},
    {"n": 6, "titre": "Parcours profondeur : les trois ordres", "notions": ["profondeur"], "exos": [
        o("a61", f"Donner les ordres préfixe, infixe et suffixe de l'arbre $T$.\n\n{fig(('T', T1))}",
          f"Préfixe : {seq(pre(T1))}\n\nInfixe : {seq(ino(T1))}\n\nSuffixe : {seq(post(T1))}", src=TD, duree=4),
        o("a62", f"Donner l'ordre infixe de l'arbre $T$. Que remarque-t-on ?\n\n{fig(('T', T2))}",
          f"Infixe : {seq(ino(T2))}. Croissant : c'est un arbre binaire de recherche.", duree=3),
        o("a63", f"Donner la représentation linéaire de $B$ : vide `()`, sinon `(rGD)`.\n\n{fig(('B', B))}",
          f"`{linear(B)}`", src=TD, duree=4),
        o("a64", "Dessiner l'arbre de représentation linéaire `(5(4(11(0()())(2()()))())(8(13()())(4(7()())(1()()))))`.",
          fig(("", parse_linear("(5(4(11(0()())(2()()))())(8(13()())(4(7()())(1()()))))"))), src=TD, duree=4),
        v("a65", f"Rang de la racine dans l'ordre suffixe, puis infixe, de l'arbre $B$ ? (donner le rang infixe)\n\n{fig(('B', B))}",
          len(ino(kids(B)[0])) + 1, rf"Infixe : tout $G$ avant la racine : $T(G)+1={len(ino(kids(B)[0])) + 1}$. Suffixe : en dernier, rang $T(B)={m_B['T']}$.", duree=2),
    ]},
    {"n": 7, "titre": "Écrire les mesures en Python", "notions": ["mesures", "recursion"], "exos": [
        w("a71", r"Écrire la fonction `size(B)` qui renvoie la taille de l'arbre binaire `B`.", SIZE,
          [("size(None)", "0"), ("size(B)", str(m_B["T"]))], r"Axiomes : $T(\text{vide})=0$, $T(\langle r, G, D\rangle)=1+T(G)+T(D)$.",
          trees={"B": B}, src=TD, duree=3),
        w("a72", r"Écrire la fonction `height(B)` (arbre vide : $-1$).", HEIGHT,
          [("height(None)", "-1"), ("height(B)", str(m_B["H"]))], r"`max` sur deux entiers est autorisé.", trees={"B": B}, src=TD, duree=3),
        w("a73", r"Écrire la fonction `leaves(B)` qui renvoie le nombre de feuilles de `B`.",
          "def leaves(B):\n    if B == None:\n        return 0\n    elif B.left == None and B.right == None:\n        return 1\n    else:\n        return leaves(B.left) + leaves(B.right)",
          [("leaves(None)", "0"), ("leaves(B)", str(len(LEAVES_B)))], r"Corrigé officiel : le test `B.left == B.right` marche aussi (deux `None`).",
          trees={"B": B}, src=C19, duree=4),
        w("a74", r"Écrire la fonction `average_depth(B)` : profondeur moyenne $LC/T$ de l'arbre non vide `B`, en un seul parcours.",
          "def _size_lc(B, d):\n    \"\"\"(size, path length) of B whose root is at depth d\"\"\"\n    if B == None:\n        return (0, 0)\n    else:\n        (s1, l1) = _size_lc(B.left, d + 1)\n        (s2, l2) = _size_lc(B.right, d + 1)\n        return (1 + s1 + s2, d + l1 + l2)\n\ndef average_depth(B):\n    (s, lc) = _size_lc(B, 0)\n    return lc / s",
          [("average_depth(B)", repr(m_B["LC"] / m_B["T"]))], r"Le niveau descend en paramètre ; taille et cheminement remontent dans un couple.",
          trees={"B": B}, src=TD, duree=8),
        w("a75", r"Écrire la fonction `nb_simple(B)` : nombre de points simples de `B`.",
          "def nb_simple(B):\n    if B == None:\n        return 0\n    else:\n        n = nb_simple(B.left) + nb_simple(B.right)\n        if (B.left == None) != (B.right == None):\n            n = n + 1\n        return n",
          [("nb_simple(None)", "0"), ("nb_simple(B)", str(len(SIMPLE_B)))], r"Exactement un fils vide : les deux tests diffèrent.",
          trees={"B": B}, duree=5),
    ]},
    {"n": 8, "titre": "Parcours profondeur en Python", "notions": ["profondeur", "recursion"], "exos": [
        w("a81", r"Écrire la fonction `prefix_list(B)` qui renvoie la liste des clés de `B` en ordre préfixe.",
          "def _prefix(B, L):\n    \"\"\"appends the keys of B to L, prefix order\"\"\"\n    if B != None:\n        L.append(B.key)\n        _prefix(B.left, L)\n        _prefix(B.right, L)\n\ndef prefix_list(B):\n    L = []\n    _prefix(B, L)\n    return L",
          [("prefix_list(None)", "[]"), ("prefix_list(T)", repr(pre(T2)))], r"Pas de `+` sur les listes : une seule liste remplie par `append`.",
          trees={"T": T2}, duree=5),
        w("a82", r"Écrire la fonction `to_linear(B)` qui renvoie la représentation linéaire de `B` (chaîne) : `()` pour l'arbre vide, `(rGD)` sinon.",
          "def to_linear(B):\n    if B == None:\n        return \"()\"\n    else:\n        return \"(\" + str(B.key) + to_linear(B.left) + to_linear(B.right) + \")\"",
          [("to_linear(None)", "'()'"), ("to_linear(T)", repr(linear(T4)))], r"Le `+` porte sur des chaînes, pas sur des listes.",
          trees={"T": T4}, src=TD, duree=4),
        w("a83", r"Écrire la fonction `equal(B1, B2)` qui teste si deux arbres binaires sont identiques (mêmes clés aux mêmes places).",
          "def equal(B1, B2):\n    if B1 == None or B2 == None:\n        return B1 == B2\n    else:\n        return B1.key == B2.key and equal(B1.left, B2.left) and equal(B1.right, B2.right)",
          [("equal(None, None)", "True"), ("equal(B1, B2)", "False"), ("equal(B1, B1)", "True")],
          r"Si l'un est vide, ils sont égaux seulement si les deux le sont. `and` s'arrête au premier échec.",
          trees={"B1": T4, "B2": (1, (2, 4, 5), (3, None, 6))}, src=C19, duree=5),
        w("a84", r"Écrire la fonction `print_tree(B)` qui renvoie la chaîne `<r, G, D>` de `B`, avec `_` pour l'arbre vide.",
          "def print_tree(B):\n    if B == None:\n        return \"_\"\n    else:\n        return \"<\" + str(B.key) + \", \" + print_tree(B.left) + \", \" + print_tree(B.right) + \">\"",
          [("print_tree(T)", repr(rgd(T4).replace("⟨", "<").replace("⟩", ">")))], trees={"T": T4}, src=TD, duree=4),
    ]},
    {"n": 9, "titre": "Parcours largeur avec une file", "notions": ["largeur"], "exos": [
        o("a91", f"Donner l'ordre hiérarchique (parcours largeur) de l'arbre $B$.\n\n{fig(('B', B))}", seq(bfs(B)), src=TD, duree=2),
        w("a92", r"Écrire la fonction `bfs_list(B)` : liste des clés de `B` en ordre hiérarchique.",
          "def bfs_list(B):\n    L = []\n    if B != None:\n        q = Queue()\n        q.enqueue(B)\n        while not q.isempty():\n            B = q.dequeue()\n            L.append(B.key)\n            if B.left != None:\n                q.enqueue(B.left)\n            if B.right != None:\n                q.enqueue(B.right)\n    return L",
          [("bfs_list(None)", "[]"), ("bfs_list(B)", repr(bfs(B)))], RULE, trees={"B": B}, src=TD, duree=5),
        w("a93", r"Écrire la fonction `width(B)` : largeur de `B`, nombre maximal de nœuds sur un même niveau ($0$ si vide).",
          "def width(B):\n    w_max = 0\n    if B != None:\n        q = Queue()\n        q.enqueue(B)\n        q.enqueue(None)\n        w = 0\n        while not q.isempty():\n            B = q.dequeue()\n            if B == None:\n                w_max = max(w, w_max)\n                if not q.isempty():\n                    q.enqueue(None)\n                w = 0\n            else:\n                w = w + 1\n                if B.left != None:\n                    q.enqueue(B.left)\n                if B.right != None:\n                    q.enqueue(B.right)\n    return w_max",
          [("width(None)", "0"), ("width(B)", str(max(len(x) for x in levels(B)))), ("width(T)", "8")],
          r"Corrigé officiel : le marqueur `None` sépare les niveaux ; on le réenfile seulement si la file n'est pas vide (sinon boucle infinie).",
          trees={"B": B, "T": T3}, src=C20, duree=8),
        w("a94", r"Écrire la fonction `get_node(B, lvl, n)` : clé du $n$-ième nœud (base $0$) du niveau `lvl` de `B`, `None` s'il n'existe pas.",
          "def get_node(B, lvl, n):\n    if B == None:\n        return None\n    q = Queue()\n    q.enqueue(B)\n    q.enqueue(None)\n    (cur, i) = (0, 0)\n    while not q.isempty() and cur <= lvl:\n        B = q.dequeue()\n        if B == None:\n            (cur, i) = (cur + 1, 0)\n            if not q.isempty():\n                q.enqueue(None)\n        else:\n            if cur == lvl and i == n:\n                return B.key\n            i = i + 1\n            if B.left != None:\n                q.enqueue(B.left)\n            if B.right != None:\n                q.enqueue(B.right)\n    return None",
          [("print(get_node(None, 0, 0))", "None"), ("get_node(B, 0, 0)", "5"), ("get_node(B, 2, 2)", "1"), ("print(get_node(B, 2, 5))", "None"), ("get_node(B, 4, 0)", "15")],
          r"On s'arrête dès que le nœud est trouvé ou que le niveau `lvl` est dépassé.", trees={"B": B}, src=TD, duree=10),
    ]},
    {"n": 10, "titre": "Tests sur les arbres", "notions": ["construction", "particuliers"], "exos": [
        w("a101", r"Écrire la fonction `degenerate(B)` : vrai si chaque nœud de `B` a au plus un fils (l'arbre vide est dégénéré).",
          "def degenerate(B):\n    while B != None and (B.left == None or B.right == None):\n        if B.left == None:\n            B = B.right\n        else:\n            B = B.left\n    return B == None",
          [("degenerate(None)", "True"), ("degenerate(T5)", "True"), ("degenerate(T4)", "False")],
          r"Un seul chemin à suivre : une boucle suffit. On sort sur `None` (dégénéré) ou sur un point double.",
          trees={"T5": T5, "T4": T4}, src=TD, duree=5),
        w("a102", r"Écrire la fonction `complete(B)` : vrai si `B` est complet, sans calculer la hauteur à part (un seul parcours).",
          "def _complete(B):\n    \"\"\"height of B if B is complete, -2 otherwise\"\"\"\n    if B == None:\n        return -1\n    hl = _complete(B.left)\n    if hl == -2:\n        return -2\n    hr = _complete(B.right)\n    if hr != hl:\n        return -2\n    return hl + 1\n\ndef complete(B):\n    return _complete(B) != -2",
          [("complete(None)", "True"), ("complete(T3)", "True"), ("complete(T4)", "False")],
          r"Complet : les deux sous-arbres sont complets et de même hauteur. La valeur $-2$ signale l'échec et coupe le parcours.",
          trees={"T3": T3, "T4": T4}, src=TD, duree=8),
        w("a103", r"Écrire la fonction `priority(B)` : vrai si l'arbre `B` (clés entières $>0$) est partiellement ordonné, chaque nœud étant inférieur ou égal à ses fils.",
          "def _test(B, p):\n    \"\"\"p: key of B's parent\"\"\"\n    if B == None:\n        return True\n    elif B.key < p:\n        return False\n    else:\n        return _test(B.left, B.key) and _test(B.right, B.key)\n\ndef priority(B):\n    return _test(B, 0)",
          [("priority(None)", "True"), ("priority(T3)", "True"), ("priority(T2)", "False")],
          r"Corrigé officiel : la clé du père descend en paramètre ($0$ pour la racine, les clés étant $>0$).",
          trees={"T3": T3, "T2": T2}, src=C20, duree=6),
    ]},
    {"n": 11, "titre": "Construire des arbres", "notions": ["construction"], "exos": [
        w("a111", r"Écrire la fonction `transpose(B)` : arbre dont la racine vaut $2r$, le sous-arbre gauche est le transposé de $D$ et le droit le transposé de $G$.",
          "def transpose(B):\n    if B == None:\n        return None\n    else:\n        return BinTree(2 * B.key, transpose(B.right), transpose(B.left))",
          [], r"Un nœud créé par appel ; les sous-arbres sont échangés.", trees={"B": T4}, outs=[("transpose(B)", (2, (6, None, 12), (4, 10, 8)))],
          fresh=True, src=TD, duree=4),
        w("a112", r"Écrire la fonction `from_hier(V)` qui construit l'arbre (`BinTree`) dont `V` est le vecteur hiérarchique (case $0$ inutilisée, `None` pour un nœud absent).",
          "def _build(V, i):\n    if i >= len(V) or V[i] == None:\n        return None\n    else:\n        return BinTree(V[i], _build(V, 2 * i), _build(V, 2 * i + 1))\n\ndef from_hier(V):\n    return _build(V, 1)",
          [], r"Le nœud $i$ a ses fils en $2i$ et $2i+1$ ; hors du vecteur, l'arbre est vide.",
          outs=[(f"from_hier({V_GAP!r})", GAP)], src=TD, duree=5),
        w("a113", r"Écrire la fonction `to_hier(B)` qui renvoie le vecteur hiérarchique de `B` (case $0$ à `None`, taille juste suffisante).",
          "def _hmax(B, i):\n    \"\"\"largest hierarchical number in B, whose root is number i\"\"\"\n    if B == None:\n        return 0\n    else:\n        return max(i, max(_hmax(B.left, 2 * i), _hmax(B.right, 2 * i + 1)))\n\ndef _fill(B, V, i):\n    if B != None:\n        V[i] = B.key\n        _fill(B.left, V, 2 * i)\n        _fill(B.right, V, 2 * i + 1)\n\ndef to_hier(B):\n    V = []\n    for i in range(_hmax(B, 1) + 1):\n        V.append(None)\n    _fill(B, V, 1)\n    return V",
          [("to_hier(None)", "[None]"), ("to_hier(T)", repr(V_T4))], r"D'abord la taille (plus grand numéro), puis le remplissage par un parcours.",
          trees={"T": T4}, src=TD, duree=8),
        w("a114", r"Écrire la fonction `copy_with_size(B)` qui renvoie une copie de `B` en `BinTreeSize(key, left, right, size)`, chaque nœud contenant la taille de son sous-arbre.",
          "def copy_with_size(B):\n    if B == None:\n        return None\n    else:\n        l = copy_with_size(B.left)\n        r = copy_with_size(B.right)\n        s = 1\n        if l != None:\n            s = s + l.size\n        if r != None:\n            s = s + r.size\n        return BinTreeSize(B.key, l, r, s)",
          [("C = copy_with_size(B)", None), ("C.size", str(m_B["T"])), ("C.left.size", str(len(pre(kids(B)[0])))), ("C.right.right.size", "3")],
          r"La taille d'un nœud se calcule après celles de ses fils (traitement suffixe), sans second parcours.",
          trees={"B": B}, src=TD, duree=6),
    ]},
    {"n": 12, "titre": "Chercher dans un arbre : numéros, parenté, codes", "notions": ["hierarchique", "profondeur"], "exos": [
        w("a121", r"Écrire la fonction `search_hier(B, x)` : numéro hiérarchique de `x` dans `B` (clés distinctes), `None` s'il est absent.",
          "def _sh(B, x, n):\n    if B == None:\n        return None\n    elif B.key == x:\n        return n\n    else:\n        r = _sh(B.left, x, 2 * n)\n        if r == None:\n            r = _sh(B.right, x, 2 * n + 1)\n        return r\n\ndef search_hier(B, x):\n    return _sh(B, x, 1)",
          [("print(search_hier(B, 10))", "None"), ("search_hier(B, 5)", "1"), ("search_hier(B, 15)", str(HN[15]))],
          r"Le numéro descend en paramètre ; on ne cherche à droite que si la gauche a échoué.", trees={"B": B}, src=TD, duree=6),
        w("a122", r"Le degré de parenté de deux nœuds est le nombre de liens qui les séparent. Écrire `get_kinship(B, x, y)` : degré de parenté des nœuds de clés `x` et `y` s'ils sont sur une même branche, $-1$ sinon (clés distinctes).",
          "def _find(B, x):\n    \"\"\"subtree of B whose root is x, None if absent\"\"\"\n    if B == None or B.key == x:\n        return B\n    else:\n        r = _find(B.left, x)\n        if r == None:\n            r = _find(B.right, x)\n        return r\n\ndef _depth(B, y):\n    \"\"\"depth of y in B, -1 if absent\"\"\"\n    if B == None:\n        return -1\n    elif B.key == y:\n        return 0\n    else:\n        d = _depth(B.left, y)\n        if d == -1:\n            d = _depth(B.right, y)\n        if d == -1:\n            return -1\n        return d + 1\n\ndef get_kinship(B, x, y):\n    A = _find(B, x)\n    if A != None:\n        d = _depth(A, y)\n        if d != -1:\n            return d\n    A = _find(B, y)\n    if A != None:\n        return _depth(A, x)\n    return -1",
          [("get_kinship(B, 4, 11)", "-1"), ("get_kinship(B, 42, 0)", "-1"), ("get_kinship(B, 12, 15)", "3"), ("get_kinship(B, -1, 5)", "2")],
          r"Même branche : l'un est ancêtre de l'autre. On cherche `y` sous `x`, sinon `x` sous `y`.", trees={"B": B}, src=TD, duree=10),
        o("a123", "Code préfixe : a = 0, f = 1100, H = 111, m = 1101, n = 101, u = 100. Décoder `1111001100110011010101`.",
          f"**{DECODED}**\n\nAucun code n'est préfixe d'un autre : on lit bit à bit jusqu'à reconnaître un code. L'arbre du code (gauche = 0, droite = 1) :\n\n{fig(('HT', HT))}",
          src=TD, duree=4),
        w("a124", r"L'arbre `HT` d'un code préfixe est localement complet, ses feuilles portent les lettres (gauche = 0, droite = 1). Écrire `search_code(T, c)` : code de la lettre `c`, `None` si elle est absente.",
          "def search_code(T, c):\n    if T.left == None:\n        if T.key == c:\n            return \"\"\n        else:\n            return None\n    else:\n        r = search_code(T.left, c)\n        if r != None:\n            return \"0\" + r\n        r = search_code(T.right, c)\n        if r != None:\n            return \"1\" + r\n        return None",
          [("search_code(HT, 'a')", "'0'"), ("search_code(HT, 'm')", "'1101'"), ("print(search_code(HT, 'w'))", "None")],
          r"Localement complet : un nœud sans fils gauche est une feuille. Le code se construit en remontant.", trees={"HT": HT}, src=TD, duree=8),
    ]},
    {"n": 13, "titre": "Arbres généraux", "notions": ["generaux", "mesures"], "exos": [
        o("a131", f"Donner l'arbre général $A$ sous forme binaire premier fils - frère droit.\n\n{gfig(('A', G1))}",
          fig(("", fcrs([G1]))) + "\n\nLien gauche : premier fils ; lien droit : frère suivant.", duree=4),
        o("a132", f"Donner les ordres préfixe, suffixe et hiérarchique de l'arbre général $A$.\n\n{gfig(('A', G1))}",
          f"Préfixe : {seq(gpre(G1))}\n\nSuffixe : {seq(gpost(G1))}\n\nHiérarchique : {seq(gbfs(G1))}\n\n"
          f"Sur la forme binaire, le préfixe est le même et le suffixe général est l'infixe : {seq(ino(fcrs([G1])))}.", duree=4),
        v("a133", f"Longueur de cheminement interne $LCI$ de l'arbre général $A$ ?\n\n{gfig(('A', G1))}", m_G1["LCI"],
          rf"Nœuds internes (au moins un fils) et leurs profondeurs : {', '.join(f'{k} ({d})' for k, d, c in _gwalk(G1) if c)}. Les mesures se prennent sur l'arbre général, pas sur sa forme binaire.", duree=3),
        o("a134", f"Dessiner l'arbre général $A$ dont la forme premier fils - frère droit est :\n\n{fig(('', A25_BIN))}",
          gfig(("A", A25)) + "\n\nLa racine $E$ n'a pas de frère ; ses fils sont $B$ et toute la chaîne des liens droits : $D$, $K$, $C$.", src=B25, duree=4),
        o("a135", "Les ordres préfixe et suffixe d'un arbre général sont : préfixe R S U V T W X Z Y, suffixe U V S T Z X Y W R. Dessiner l'arbre.",
          gfig(("A", G1)) + "\n\nLe préfixe donne la racine (R) puis son premier fils (S) ; dans le suffixe, ce qui précède S (U V) est le sous-arbre de S, et ainsi de suite.", duree=5),
    ]},
    {"n": 14, "titre": "Examen B3 du 12 mars 2024", "notions": ["largeur", "construction", "profondeur", "generaux"], "exos": [
        w("a141", r"**Exercice 1 (Croissant, 7 points).** Écrire la fonction `increasing(B)` qui vérifie que chaque niveau de l'arbre binaire `B` contient strictement plus de nœuds que le niveau précédent.",
          "def increasing(B):\n    if B == None:\n        return True\n    q = Queue()\n    q.enqueue(B)\n    q.enqueue(None)\n    (prev, cur) = (0, 0)\n    ok = True\n    while ok and not q.isempty():\n        B = q.dequeue()\n        if B == None:\n            ok = cur > prev\n            (prev, cur) = (cur, 0)\n            if not q.isempty():\n                q.enqueue(None)\n        else:\n            cur = cur + 1\n            if B.left != None:\n                q.enqueue(B.left)\n            if B.right != None:\n                q.enqueue(B.right)\n    return ok",
          [("increasing(None)", "True"), ("increasing(B4)", "True"), ("increasing(B5)", "False"), ("increasing(B6)", "True")],
          r"Parcours largeur avec marqueur de niveau ; on s'arrête au premier niveau qui ne grandit pas.",
          trees={"B4": (1, 2, 3), "B5": (1, 2, (3, 6, None)), "B6": (1, (2, 4, 5), (3, None, 7))}, src=B24, duree=15),
        w("a142", r"**Exercice 2 (Somme, 7 points).** Écrire la fonction `check_sum(B)` qui vérifie si chaque point double de l'arbre binaire `B` contient la somme des clés de ses deux fils. Le **parcours profondeur** doit obligatoirement être utilisé.",
          "def check_sum(B):\n    if B == None:\n        return True\n    elif B.left != None and B.right != None and B.key != B.left.key + B.right.key:\n        return False\n    else:\n        return check_sum(B.left) and check_sum(B.right)",
          [("check_sum(None)", "True"), ("check_sum(B1)", "True"), ("check_sum(B2)", "True"), ("check_sum(B3)", "False")],
          r"Un point simple n'est pas testé (dans `B2`, $6$ n'a qu'un fils). Arrêt au premier point double faux.",
          trees={"B1": (8, 6, 2), "B2": (8, (6, 5, None), (2, 1, 1)), "B3": (8, (6, 5, 3), (2, 1, 1))}, src=B24, duree=12),
        o("a143", f"**Exercice 3 (Mystery, 3 points).** Dessiner l'arbre résultat de l'application de `mystery(Bquid)`.\n\n{_py(MYST24)}\n\n{fig(('Bquid', BQUID))}",
          fig(("", MYST24_RES)) + "\n\n`mystery` recopie la forme de l'arbre ; chaque nœud reçoit le nombre de points doubles de son sous-arbre (le `b + 1` n'a lieu que si le nœud a deux fils).",
          src=B24, duree=8),
        o("a144", "**Exercice 4 (Arbre général, 3 points).** Les traitements préfixe et suffixe du parcours profondeur d'un arbre général A affichent : préfixe E D J I C H A B F G ; suffixe J I C D H B G F A E. Dessiner A, puis sa forme binaire premier fils - frère droit.",
          gfig(("A", A24)) + "\n\n" + fig(("premier fils - frère droit", fcrs([A24]))), src=B24, duree=8),
    ]},
    {"n": 15, "titre": "Examen B3 du 5 mars 2025", "notions": ["largeur", "profondeur", "generaux"], "exos": [
        w("a151", r"**Exercice 1 (Liste, 6 points).** Écrire la fonction `list_sum_limit(B, limit)` qui prend un arbre binaire `B` d'entiers positifs et un entier `limit`, et renvoie la liste des sommes des niveaux, chacune seulement si elle est strictement plus petite que `limit`.",
          "def list_sum_limit(B, limit):\n    L = []\n    if B != None:\n        q = Queue()\n        q.enqueue(B)\n        q.enqueue(None)\n        s = 0\n        while not q.isempty():\n            B = q.dequeue()\n            if B == None:\n                if s < limit:\n                    L.append(s)\n                s = 0\n                if not q.isempty():\n                    q.enqueue(None)\n            else:\n                s = s + B.key\n                if B.left != None:\n                    q.enqueue(B.left)\n                if B.right != None:\n                    q.enqueue(B.right)\n    return L",
          [("list_sum_limit(None, 42)", "[]"), ("list_sum_limit(B5, 5)", "[]"), ("list_sum_limit(B5, 8)", "[7]"), ("list_sum_limit(B5, 10)", "[8, 8, 7]"),
           ("list_sum_limit(B5, 12)", "[8, 8, 10, 7]"), ("list_sum_limit(B7, 13)", "[12, 11]"), ("list_sum_limit(B7, 40)", "[12, 20, 15, 11]")],
          r"Somme par niveau avec le marqueur `None` ; la somme est testée à la fin de chaque niveau.",
          trees={"B5": (8, (6, 5, None), (2, 1, (4, None, 7))), "B7": (12, (1, None, (10, 6, 5)), (19, None, 5))}, src=B25, duree=15),
        w("a152", r"**Exercice 2 (Point simple, 6 points).** Écrire la fonction `get_first_single(B)` qui renvoie la clé du premier point simple rencontré dans l'arbre binaire `B` (entiers positifs) et $-1$ s'il n'y en a pas. Le **parcours profondeur** doit obligatoirement être utilisé.",
          "def get_first_single(B):\n    if B == None:\n        return -1\n    elif (B.left == None) != (B.right == None):\n        return B.key\n    else:\n        k = get_first_single(B.left)\n        if k == -1:\n            k = get_first_single(B.right)\n        return k",
          [("get_first_single(None)", "-1"), ("get_first_single(B1)", "-1"), ("get_first_single(B2)", "6"), ("get_first_single(B4)", "2")],
          r"Premier rencontré : ordre préfixe. On ne descend à droite que si rien n'a été trouvé à gauche.",
          trees={"B1": (8, 6, 2), "B2": (8, (6, 5, None), (2, 1, 4)), "B4": (8, (6, 5, 3), (2, None, 4))}, src=B25, duree=12),
        w("a153", r"**Exercice 3 (Ordres, 4 points).** Écrire la fonction `get_root_order(B)` qui renvoie le rang de rencontre de la racine dans les trois ordres induits du parcours profondeur, sous la forme `(préfixe, infixe, suffixe)`, et `None` si l'arbre est vide.",
          SIZE + "\n\ndef get_root_order(B):\n    if B == None:\n        return None\n    else:\n        s = size(B.left)\n        return (1, s + 1, s + 1 + size(B.right))",
          [("print(get_root_order(None))", "None"), ("get_root_order(B1)", "(1, 2, 3)"), ("get_root_order(B2)", "(1, 3, 6)"), ("get_root_order(B3)", "(1, 4, 7)")],
          r"Préfixe : toujours $1$. Infixe : après tout le sous-arbre gauche. Suffixe : en dernier, rang $T(B)$.",
          trees={"B1": (8, 6, 2), "B2": (8, (6, 5, None), (2, 1, 4)), "B3": (8, (6, 5, 3), (2, 1, 4))}, src=B25, duree=8),
        o("a154", f"**Exercice 4 (Arbre général, 4 points).** Soit l'arbre général $A$ représenté sous la forme binaire premier fils - frère droit. Donner sa taille, sa hauteur, sa profondeur moyenne interne, ses ordres préfixe et suffixe.\n\n{fig(('A', A25_BIN))}",
          f"L'arbre général :\n\n{gfig(('A', A25))}\n\nTaille : ${m_A25['T']}$. Hauteur : ${m_A25['H']}$. "
          f"Nœuds internes {', '.join(f'{k} ({d})' for k, d, c in _gwalk(A25) if c)} : $PMI={frac_tex(m_A25['PMI'])}$.\n\n"
          f"Préfixe : {seq(gpre(A25))}\n\nSuffixe : {seq(gpost(A25))}\n\n"
          "Pas de corrigé officiel : $PMI$ suit la définition du cours, $LCI$ divisé par le nombre de nœuds internes.", src=B25, duree=8),
    ]},
    {"n": 16, "titre": "Examen B3 du 10 mars 2026", "notions": ["largeur", "construction", "recursion"], "exos": [
        w("a161", r"**Exercice 1 (5 points).** Écrire la fonction `size_levels(B, level, k)` qui renvoie `True` si le nombre de nœuds de `B` situés aux niveaux supérieurs ou égaux à `level` est strictement supérieur à `k`, `False` sinon (niveau de la racine : $0$).",
          "def _count(B, depth, level):\n    \"\"\"number of nodes of B at levels >= level, B's root being at depth\"\"\"\n    if B == None:\n        return 0\n    else:\n        c = _count(B.left, depth + 1, level) + _count(B.right, depth + 1, level)\n        if depth >= level:\n            c = c + 1\n        return c\n\ndef size_levels(B, level, k):\n    return _count(B, 0, level) > k",
          [("size_levels(None, 0, 0)", "False"), ("size_levels(B1, 0, 0)", "True"), ("size_levels(B1, 0, 5)", "True"), ("size_levels(B1, 0, 11)", "False"),
           ("size_levels(B1, 2, 5)", "True"), ("size_levels(B1, 2, 8)", "False"), ("size_levels(B1, 3, 0)", "True"), ("size_levels(B1, 3, 5)", "False")],
          r"Le niveau courant descend en paramètre. Plus économe : passer `k` et s'arrêter dès que le compte le dépasse.",
          trees={"B1": E26}, src=B26, duree=12),
        w("a162", r"**Exercice 2 (5 points).** Écrire la fonction `add_trees(B1, B2)` qui « additionne » deux arbres binaires d'entiers : si deux nœuds se superposent, le nœud résultat vaut leur somme ; sinon le nœud non vide est utilisé. Chaque nœud du nouvel arbre doit être créé (aucun nœud de `B1` ou `B2` réutilisé). Approche **récursive** obligatoire.",
          "def add_trees(B1, B2):\n    if B1 == None and B2 == None:\n        return None\n    elif B1 == None:\n        return BinTree(B2.key, add_trees(None, B2.left), add_trees(None, B2.right))\n    elif B2 == None:\n        return BinTree(B1.key, add_trees(B1.left, None), add_trees(B1.right, None))\n    else:\n        return BinTree(B1.key + B2.key, add_trees(B1.left, B2.left), add_trees(B1.right, B2.right))",
          [], r"Quand un seul arbre est non vide, on continue à le recopier nœud par nœud (`add_trees(None, …)`) : renvoyer directement `B2` réutiliserait ses nœuds.",
          trees={"B1": (-1, (2, (12, -1, None), (-8, None, -10)), 8), "B2": (-1, (2, None, (-8, None, -10)), (8, (15, None, 1), -5)), "B3": (2, 3, None)},
          outs=[("add_trees(B1, B2)", (-2, (4, (12, -1, None), (-16, None, -20)), (16, (15, None, 1), -5))),
                ("add_trees(B1, B3)", (1, (5, (12, -1, None), (-8, None, -10)), 8)),
                ("add_trees(B2, B3)", (1, (5, None, (-8, None, -10)), (8, (15, None, 1), -5)))],
          fresh=True, src=B26, duree=12),
        w("a163", r"**Exercice 3 (7 points).** Écrire la fonction `positive_sequence(B, k)` ($k>0$) qui renvoie `True` s'il n'existe **aucune** séquence successive de nœuds strictement positifs de longueur supérieure ou égale à `k` dans `B`, `False` sinon. Une séquence successive est un chemin d'un nœud vers l'un de ses descendants dont tous les nœuds sont strictement positifs. Approche **récursive** obligatoire.",
          "def _pos(B, cur, k):\n    \"\"\"cur: length of the positive sequence ending at B's parent\"\"\"\n    if B == None:\n        return True\n    if B.key > 0:\n        cur = cur + 1\n    else:\n        cur = 0\n    if cur >= k:\n        return False\n    return _pos(B.left, cur, k) and _pos(B.right, cur, k)\n\ndef positive_sequence(B, k):\n    return _pos(B, 0, k)",
          [("positive_sequence(B1, 1)", "False"), ("positive_sequence(B1, 2)", "False"), ("positive_sequence(B1, 3)", "True"),
           ("positive_sequence(B2, 1)", "False"), ("positive_sequence(B2, 2)", "False"), ("positive_sequence(B2, 3)", "False"), ("positive_sequence(B2, 4)", "True")],
          r"La longueur de la séquence en cours descend en paramètre et repart à $0$ sur un nœud négatif ou nul. Arrêt dès qu'elle atteint $k$.",
          trees={"B1": (-1, (2, (12, -1, None), (-8, None, -10)), 8), "B2": (-1, (2, None, (-8, None, -10)), (8, (15, None, 1), -5))}, src=B26, duree=12),
        o("a164", f"**Exercice 4 (Mystery, 3 points).** Dessiner l'arbre résultat de `mystery(B, 3)`.\n\n{_py(MYST26)}\n\n{fig(('B', E26))}",
          fig(("mystery(B, 3)", MYST26_RES)) + "\n\n`a` diminue de $1$ à chaque niveau. Sur un nœud du niveau $3$ (`a == 0`), une feuille est supprimée et un point simple est remplacé par son unique fils ; "
          "un point double est gardé (la descente continue avec `a` négatif, sans plus rien changer). Ici : $4$ et $11$ disparaissent, $-2$ est remplacé par $15$. "
          f"Avec `mystery(B, 2)`, c'est le niveau $2$ qui est touché :\n\n{fig(('mystery(B, 2)', MYST26_RES1))}", src=B26, duree=8),
    ]},
]

VARIANTS = {
    "a21": [vv(f"Combien l'arbre $T$ a-t-il de feuilles ?\n\n{fig(('T', T2))}", sum(1 for _, _, c in _walk(T2) if c == 0), "Nœuds sans fils.")],
    "a31": [vv(f"Hauteur de l'arbre $T$ ?\n\n{fig(('T', T1))}", m_T1["H"], "Profondeur de la feuille la plus basse.")],
    "a32": [vv(f"Longueur de cheminement $LC$ de l'arbre $T$ ?\n\n{fig(('T', T1))}", m_T1["LC"], _mes_sol(m_T1))],
    "a33": [vv(f"Profondeur moyenne externe $PME$ de l'arbre $T$ (fraction) ?\n\n{fig(('T', T2))}", frac(m_T2["PME"]), _mes_sol(m_T2))],
    "a41": [vv(r"Nombre de feuilles d'un arbre binaire complet de hauteur $6$ ?", 2 ** 6, r"$2^H$ feuilles.")],
    "a42": [vv(r"Hauteur d'un arbre binaire parfait de $1000$ nœuds ?", 9, r"$2^9=512\le1000<1024$.")],
    "a51": [vv(f"Numéro hiérarchique du nœud $11$ dans l'arbre $B$ ?\n\n{fig(('B', B))}", HN[11], r"Gauche, droite, droite : $1\to2\to5\to11$.")],
    "a53": [vv(r"Numéro hiérarchique du fils droit du fils gauche du nœud $9$ ?", 37, r"$2\times9=18$, puis $2\times18+1=37$.")],
    "a72": [wv(r"Écrire `height(B)` (arbre vide : $-1$).", HEIGHT, [("height(T)", "3")], trees={"T": T3})],
    "a81": [wv(r"Écrire `infix_list(B)` : clés de `B` en ordre infixe.",
               "def _infix(B, L):\n    if B != None:\n        _infix(B.left, L)\n        L.append(B.key)\n        _infix(B.right, L)\n\ndef infix_list(B):\n    L = []\n    _infix(B, L)\n    return L",
               [("infix_list(T)", repr(ino(T2)))], trees={"T": T2})],
}
for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["id"] in VARIANTS:
            _e["variants"] = VARIANTS[_e["id"]]

EXTRA_PARTS = []

QUIZ = [
    {"notion": "recursion", "type": "qcm", "q": r"Une fonction récursive dont la branche récursive n'a pas de `return` renvoie :", "choix": [r"`None`", r"le résultat de l'appel", r"`0`", r"une erreur à la compilation"], "bonne": 0},
    {"notion": "recursion", "type": "vf", "q": r"`nb_calls += 1` sur un paramètre entier modifie le compteur de l'appelant.", "bonne": False},
    {"notion": "vocabulaire", "type": "qcm", "q": r"Un nœud n'ayant qu'un fils gauche est :", "choix": [r"un point simple à gauche", r"une feuille", r"un point double", r"un nœud externe"], "bonne": 0},
    {"notion": "vocabulaire", "type": "vf", "q": r"Un arbre binaire a autant de branches que de feuilles.", "bonne": True},
    {"notion": "mesures", "type": "qcm", "q": r"$PMI$ vaut :", "choix": [r"$LCI$ / nombre de nœuds internes", r"$LCI$ / taille", r"$LC$ / nombre de feuilles", r"$LCE$ / nombre de nœuds internes"], "bonne": 0},
    {"notion": "mesures", "type": "vf", "q": r"La hauteur d'un arbre réduit à sa racine est $1$.", "bonne": False},
    {"notion": "particuliers", "type": "qcm", "q": r"Un arbre complet de hauteur $4$ a :", "choix": [r"$31$ nœuds", r"$16$ nœuds", r"$32$ nœuds", r"$15$ nœuds"], "bonne": 0},
    {"notion": "particuliers", "type": "vf", "q": r"Tout arbre parfait est complet.", "bonne": False},
    {"notion": "hierarchique", "type": "qcm", "q": r"Le père du nœud de numéro $27$ est :", "choix": [r"$13$", r"$14$", r"$26$", r"$54$"], "bonne": 0},
    {"notion": "hierarchique", "type": "vf", "q": r"L'occurrence $0110$ désigne un nœud de niveau $4$.", "bonne": True},
    {"notion": "profondeur", "type": "qcm", "q": r"Dans un arbre binaire de recherche, l'ordre qui donne les clés triées est :", "choix": [r"infixe", r"préfixe", r"suffixe", r"hiérarchique"], "bonne": 0},
    {"notion": "profondeur", "type": "vf", "q": r"En ordre suffixe, la racine est rencontrée en dernier.", "bonne": True},
    {"notion": "largeur", "type": "qcm", "q": r"Le parcours largeur utilise :", "choix": [r"une file", r"une pile", r"la récursion seule", r"un tri"], "bonne": 0},
    {"notion": "largeur", "type": "vf", "q": r"Avec un marqueur `None` de fin de niveau, on le réenfile même si la file est vide.", "bonne": False},
    {"notion": "construction", "type": "qcm", "q": r"`add_trees(B1, None)` doit renvoyer :", "choix": [r"une copie de `B1`", r"`B1` lui-même", r"`None`", r"une erreur"], "bonne": 0},
    {"notion": "construction", "type": "vf", "q": r"Pour tester qu'un arbre est partiellement ordonné, on peut passer la clé du père en paramètre.", "bonne": True},
    {"notion": "generaux", "type": "qcm", "q": r"Dans la forme premier fils - frère droit, le lien droit d'un nœud mène à :", "choix": [r"son frère suivant", r"son dernier fils", r"son père", r"son premier fils"], "bonne": 0},
    {"notion": "generaux", "type": "vf", "q": r"L'ordre suffixe d'un arbre général est l'ordre infixe de sa forme binaire premier fils - frère droit.", "bonne": True},
]

_FL = {
    1: r"cas d'arrêt · `return` dans chaque branche · couple `(valeur, compteur)` · accumulateur",
    2: r"point double : 2 fils · point simple : 1 fils · feuille : 0 fils · branches $=$ feuilles · $\langle r, G, D\rangle$",
    3: r"$H(\text{racine})=0$ · $LC=\sum H(x)=LCE+LCI$ · $PM=LC/T$ · $PME=LCE/N_e$ · $PMI=LCI/N_i$",
    4: r"complet : $T=2^{H+1}-1$, $2^H$ feuilles · parfait : $H=\lfloor\log_2 T\rfloor$ · dégénéré : $H=T-1$ · localement complet : $T=2N_e-1$",
    5: r"fils $2i$, $2i+1$ · père $\lfloor i/2\rfloor$ · niveau $\lfloor\log_2 i\rfloor$ · occurrence : $0$ gauche, $1$ droite",
    6: r"préfixe : r G D · infixe : G r D · suffixe : G D r · linéaire `(rGD)`, vide `()`",
    7: r"`size` : $1+T(G)+T(D)$ · `height` : $1+\max$, vide $-1$ · feuille : deux fils `None` · couple `(taille, LC)`",
    8: r"liste remplie par `append` dans une fonction auxiliaire · chaînes : `+` permis · `equal` : `and` paresseux",
    9: r"`Queue()`, `enqueue`, `dequeue`, `isempty` · marqueur `None` de fin de niveau, réenfilé si la file n'est pas vide",
    10: r"dégénéré : une boucle · complet : hauteurs égales, échec $-2$ · partiellement ordonné : clé du père en paramètre",
    11: r"`BinTree(k, f(G), f(D))` · vecteur hiérarchique : fils $2i$, $2i+1$ · taille calculée après les fils",
    12: r"numéro en paramètre ($2n$, $2n+1$) · chercher à droite seulement si échec à gauche · code : gauche $0$, droite $1$",
    13: r"gauche : premier fils · droite : frère droit · préfixe identique · suffixe $=$ infixe binaire · mesures sur l'arbre général",
    14: r"largeur par niveau (marqueur) · test récursif des points doubles · `mystery` : compter · préfixe + suffixe $\to$ arbre général",
    15: r"somme par niveau · premier point simple en préfixe · rangs $(1, T(G)+1, T(B))$ · premier fils - frère droit $\to$ arbre général",
    16: r"niveau en paramètre · nouveau nœud à chaque appel · longueur courante en paramètre · `a` diminue d'un niveau à l'autre",
}
FORMULES = {e["id"]: _FL[lvl["n"]] for lvl in LEVELS for e in lvl["exos"]}

assert len(CHECKED) == len(set(CHECKED)), "duplicate exercise id"
assert len({e["id"] for lvl in LEVELS for e in lvl["exos"]}) == sum(len(lvl["exos"]) for lvl in LEVELS)
