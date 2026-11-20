"""Level path: S3 algorithmics, théorie des langages rationnels (THLR, Moodle course « 2030_Théorie des langage rationnels »).

Moodle sources: `01_Supports` (slides « Théorie des Langages Rationnels », A. Pommellet, 2026: words, languages, regular
expressions, finite automata, Thompson, backward removal of ε-transitions, pruning, determinization, pumping lemma,
Moore minimization, Brzozowski-McCluskey, stability and decidability; TD 1-5 in French and English; the 2021 lecture
notes, chapters 2-4, only for the vocabulary) and `02_Devoirs - Homework` (five Moodle quizzes). The midterm is a Moodle
quiz on the first two lectures (words and languages), the final (60 min, 23 October 2026) covers the last three weeks.
Past exams: no THLR exam in `annales/raw/S3/Finals|Midterms/Algo` (those are trees and graphs); the only THLR material in
`annales/raw/S3/THLR` is the 2016-2017 TD 1-5, DM 1-4 and TP 1-3 subjects (same exercises as the 2026 TDs), so the exam
levels reuse exercises of TD 2, TD 3, TD 4, TD 5 and DM 3 (cited in `src`). Levels 1 and 2 are S1/S2 reminders (sets, power
sets, induction, equivalence relations, lists as words: see `obm.py`, `algo_taa.py`).

Every answer that can be computed is computed at import (build.py imports this module, so a wrong answer stops the build):
- `Aut` is a small automaton library (ε-closure, backward removal, subset construction, completion, complement, pruning,
  synchronized product, Moore partitions, exact equivalence with a shortest counter-example); regular expressions are parsed
  by `parse`, translated to Python `re` for an independent brute-force check, and to ε-NFA by `thompson` (Thompson's algorithm);
- `value` exercises: `calc` is the library result (written as a literal), `ans` is the hand-derived answer, build.py compares;
- `open` exercises with an expression or an automaton as the answer are checked by `check_rx` / `check_aut` against a Python
  predicate on every word up to a length bound, and by `Aut.equivalent` (exact) when the answer is compared with another model;
- automata are drawn as SVG files in `static/automates/` (name = hash of the drawing), shown as Markdown images with a
  text description (alt); Thompson automata are given as transition lists, never as a hand-placed drawing.
"""
import collections
import hashlib
import html
import itertools
import re
from math import comb
from pathlib import Path

SUBJECT = {
    "id": "algo-s3-thlr",
    "ordre": 695,
    "matiere": "algo",
    "semestre": "S3",
    "ecue": "THLR",
    "titre": "Théorie des langages rationnels : mots, expressions rationnelles, automates",
    "chapitres_moodle": [
        "01_Supports",
        "02_Devoirs - Homework",
    ],
    "td": "TD 1 à 5 de THLR (supports de cours, version 2026), devoirs Moodle 1 à 5",
    "examens": ["Mi-parcours THLR (QCM Moodle, 30 min)", "Examen final THLR (60 min, 23 octobre 2026)"],
}

CHECKED = []
FIG_DIR = Path(__file__).resolve().parents[2] / "static" / "automates"
FIG_URL = "/static/automates/"

# ---------------------------------------------------------------- regular expressions: parse, translate, Thompson

EPS_T, EMPTY_T = ("e",), ("0",)


def parse(s):
    """Course syntax -> tree. Letters, ε, ∅, `+` (union), juxtaposition, `*`, parentheses."""
    toks = [c for c in s if not c.isspace()]
    pos = [0]

    def peek():
        return toks[pos[0]] if pos[0] < len(toks) else None

    def alt():
        x = cat()
        while peek() == "+":
            pos[0] += 1
            x = ("+", x, cat())
        return x

    def cat():
        x = star()
        while peek() not in (None, "+", ")"):
            x = (".", x, star())
        return x

    def star():
        x = atom()
        while peek() == "*":
            pos[0] += 1
            x = ("*", x)
        return x

    def atom():
        c = peek()
        pos[0] += 1
        if c == "(":
            x = alt()
            assert peek() == ")", s
            pos[0] += 1
            return x
        assert c not in (None, ")", "+", "*"), f"bad expression {s!r}"
        return EPS_T if c == "ε" else EMPTY_T if c == "∅" else ("s", c)

    t = alt()
    assert pos[0] == len(toks), f"bad expression {s!r}"
    return t


def to_re(t):
    k = t[0]
    if k == "s":
        return re.escape(t[1])
    if k == "e":
        return ""
    if k == "0":
        return "(?!)"
    if k == ".":
        return to_re(t[1]) + to_re(t[2])
    if k == "+":
        return f"(?:{to_re(t[1])}|{to_re(t[2])})"
    return f"(?:{to_re(t[1])})*"


def tex(t, prec=0):
    """Tree -> LaTeX (union 0 < concatenation 1 < star 2)."""
    if isinstance(t, str):
        t = parse(t)
    k = t[0]
    if k == "s":
        return t[1] if t[1] not in "-." else r"\text{" + t[1] + "}"
    if k == "e":
        return r"\varepsilon"
    if k == "0":
        return r"\emptyset"
    if k == "*":
        return tex(t[1], 3) + "^*"
    if k == ".":
        out = tex(t[1], 1) + tex(t[2], 2)
        return out if prec <= 1 else f"({out})"
    out = tex(t[1], 0) + "+" + tex(t[2], 1)
    return out if prec == 0 else f"({out})"


def rx_match(e, w):
    return re.fullmatch(to_re(parse(e)), w) is not None


def words(sigma, n):
    for k in range(n + 1):
        for t in itertools.product(sigma, repeat=k):
            yield "".join(t)


def W(w):
    """Word -> LaTeX."""
    return r"\varepsilon" if w == "" else r"\mathtt{" + w + "}"


def LANG(ws):
    """Finite language -> LaTeX set."""
    return r"\{" + ",".join(W(w) for w in sorted(ws, key=lambda x: (len(x), x))) + r"\}"


def check_rx(e, pred, sigma, n):
    """The expression `e` matches exactly the words <= n letters that satisfy `pred` (independent Python `re` check)."""
    rx = re.compile(to_re(parse(e)))
    for w in words(sigma, n):
        assert (rx.fullmatch(w) is not None) == bool(pred(w)), f"{e!r} vs spec on {w!r}"
    return e


def lang_upto(e, sigma, n):
    rx = re.compile(to_re(parse(e)))
    return {w for w in words(sigma, n) if rx.fullmatch(w)}


# ---------------------------------------------------------------- automata

class Aut:
    """Finite automaton (A = (Q, Σ, δ, I, F)); the empty string "" labels a spontaneous (ε) transition."""

    def __init__(self, sigma, trans, init, final, states=None):
        self.sigma = tuple(sigma)
        self.d = collections.defaultdict(set)
        for p, a, q in trans:
            self.d[(p, a)].add(q)
        self.init, self.final = frozenset(init), frozenset(final)
        seen = list(states or [])
        for p, a, q in trans:
            seen += [p, q]
        seen += list(init) + list(final)
        self.Q = list(dict.fromkeys(seen)) if states else sorted(set(seen), key=str if not all(isinstance(x, int) for x in seen) else None)
        self.ix = {q: i for i, q in enumerate(self.Q)}

    def trans(self):
        order = {a: i for i, a in enumerate(("",) + self.sigma)}
        return sorted(((p, a, q) for (p, a), qs in self.d.items() for q in qs),
                      key=lambda t: (self.ix[t[0]], order[t[1]], self.ix[t[2]]))

    def has_eps(self):
        return any(a == "" for _, a, _ in self.trans())

    def closure(self, S):
        S, todo = set(S), list(S)
        while todo:
            for r in self.d.get((todo.pop(), ""), ()):
                if r not in S:
                    S.add(r)
                    todo.append(r)
        return frozenset(S)

    def step(self, S, a):
        return self.closure({r for p in S for r in self.d.get((p, a), ())})

    def accepts(self, w):
        S = self.closure(self.init)
        for c in w:
            S = self.step(S, c)
        return bool(S & self.final)

    def run(self, w):
        """State reached after reading w (DFA only)."""
        q = next(iter(self.init))
        for c in w:
            q = next(iter(self.d[(q, c)]))
        return q

    def paths(self, w):
        """(paths labelled by w, accepting ones) from an initial state; ε-free automata."""
        cnt = collections.Counter({q: 1 for q in self.init})
        for c in w:
            nxt = collections.Counter()
            for p, k in cnt.items():
                for r in self.d.get((p, c), ()):
                    nxt[r] += k
            cnt = nxt
        return sum(cnt.values()), sum(k for q, k in cnt.items() if q in self.final)

    def is_dfa(self):
        return len(self.init) == 1 and not self.has_eps() and all(len(qs) <= 1 for qs in self.d.values())

    def is_complete(self):
        return all(self.d.get((q, a)) for q in self.Q for a in self.sigma)

    def lang(self, n):
        return {w for w in words(self.sigma, n) if self.accepts(w)}

    def remove_eps(self):
        """Backward removal: q -a-> r when p -a-> r for some p in the ε-closure of q; q becomes final if its closure meets F."""
        cl = {q: self.closure([q]) for q in self.Q}
        tr = [(q, a, r) for q in self.Q for p in cl[q] for a in self.sigma for r in self.d.get((p, a), ())]
        return Aut(self.sigma, tr, self.init, [q for q in self.Q if cl[q] & self.final], self.Q)

    def determinize(self):
        """Subset construction of an ε-free NFA: DFA whose states are frozensets, in discovery order (∅ is a state if reached)."""
        assert not self.has_eps()
        start = frozenset(self.init)
        order, tr, todo = [start], [], collections.deque([start])
        while todo:
            S = todo.popleft()
            for a in self.sigma:
                T = frozenset(r for p in S for r in self.d.get((p, a), ()))
                tr.append((S, a, T))
                if T not in order:
                    order.append(T)
                    todo.append(T)
        return Aut(self.sigma, tr, [start], [S for S in order if S & self.final], order)

    def complete(self):
        if self.is_complete():
            return self
        sink = max(self.Q) + 1
        tr = self.trans() + [(q, a, sink) for q in self.Q + [sink] for a in self.sigma if not self.d.get((q, a))]
        return Aut(self.sigma, tr, self.init, self.final, self.Q + [sink])

    def complement(self):
        assert self.is_dfa() and self.is_complete()
        return Aut(self.sigma, self.trans(), self.init, [q for q in self.Q if q not in self.final], self.Q)

    def accessible(self):
        S, todo = set(self.init), list(self.init)
        while todo:
            p = todo.pop()
            for a in ("",) + self.sigma:
                for r in self.d.get((p, a), ()):
                    if r not in S:
                        S.add(r)
                        todo.append(r)
        return S

    def coaccessible(self):
        S, todo = set(self.final), list(self.final)
        while todo:
            r = todo.pop()
            for p, a, q in self.trans():
                if q == r and p not in S:
                    S.add(p)
                    todo.append(p)
        return S

    def useful(self):
        return self.accessible() & self.coaccessible()

    def prune(self):
        U = self.useful()
        keep = [q for q in self.Q if q in U] or sorted(self.init)
        return Aut(self.sigma, [t for t in self.trans() if t[0] in U and t[2] in U], self.init, self.final & U, keep)

    def renamed(self, f):
        return Aut(self.sigma, [(f(p), a, f(q)) for p, a, q in self.trans()], [f(q) for q in self.init],
                   [f(q) for q in self.final], [f(q) for q in self.Q])

    def product(self, other, mode="and"):
        """Synchronized product of two complete DFA (reachable part); final iff both (and) / one (or) / only the first (minus)."""
        assert self.is_dfa() and other.is_dfa() and self.is_complete() and other.is_complete()
        start = (next(iter(self.init)), next(iter(other.init)))
        order, tr, todo = [start], [], [start]
        while todo:
            p, q = todo.pop(0)
            for a in self.sigma:
                t = (next(iter(self.d[(p, a)])), next(iter(other.d[(q, a)])))
                tr.append(((p, q), a, t))
                if t not in order:
                    order.append(t)
                    todo.append(t)
        op = {"and": lambda x, y: x and y, "or": lambda x, y: x or y, "minus": lambda x, y: x and not y}[mode]
        return Aut(self.sigma, tr, [start], [s for s in order if op(s[0] in self.final, s[1] in other.final)], order)

    def moore(self):
        """Partition refinement of a complete DFA: list of partitions (lists of sorted tuples), first = {F, Q\\F}, last = stable."""
        assert self.is_dfa() and self.is_complete()
        cls = {q: (q in self.final) for q in self.Q}
        hist = []
        while True:
            groups = collections.defaultdict(list)
            for q in self.Q:
                groups[cls[q]].append(q)
            hist.append(sorted((tuple(g) for g in groups.values()), key=lambda g: self.ix[g[0]]))
            sig = {q: (cls[q], tuple(cls[next(iter(self.d[(q, a)]))] for a in self.sigma)) for q in self.Q}
            ids = {s: i for i, s in enumerate(dict.fromkeys(sig[q] for q in self.Q))}
            new = {q: ids[sig[q]] for q in self.Q}
            if len(set(new.values())) == len(set(cls.values())):
                return hist
            cls = new

    def minimal(self):
        """Minimal complete DFA (accessible part, Moore); states are the class indices 0.. in order of first member."""
        A = self.complete() if not self.is_complete() else self
        A = Aut(A.sigma, [t for t in A.trans() if t[0] in A.accessible()], A.init, A.final & A.accessible(),
                [q for q in A.Q if q in A.accessible()])
        part = A.moore()[-1]
        of = {q: i for i, g in enumerate(part) for q in g}
        return A.renamed(lambda q: of[q])

    def shortest(self):
        """Shortest accepted word (None if empty language)."""
        A = self.remove_eps().determinize()
        seen, todo = {next(iter(A.init)): ""}, collections.deque(A.init)
        while todo:
            S = todo.popleft()
            if S in A.final:
                return seen[S]
            for a in A.sigma:
                T = next(iter(A.d[(S, a)]))
                if T not in seen:
                    seen[T] = seen[S] + a
                    todo.append(T)
        return None

    def equivalent(self, other):
        """(True, None) or (False, shortest word accepted by exactly one of the automata)."""
        A, B = self.remove_eps().determinize(), other.remove_eps().determinize()
        s = (next(iter(A.init)), next(iter(B.init)))
        seen, todo = {s: ""}, collections.deque([s])
        while todo:
            p, q = todo.popleft()
            if (p in A.final) != (q in B.final):
                return False, seen[(p, q)]
            for a in self.sigma:
                t = (next(iter(A.d[(p, a)])), next(iter(B.d[(q, a)])))
                if t not in seen:
                    seen[t] = seen[(p, q)] + a
                    todo.append(t)
        return True, None


def thompson(e, sigma):
    """Thompson's ε-NFA of an expression (string or tree): one initial state, one distinct final state, 2n states."""
    t = parse(e) if isinstance(e, str) else e
    tr, cnt = [], [0]

    def new():
        cnt[0] += 1
        return cnt[0] - 1

    def go(t):
        k = t[0]
        if k in ("s", "e", "0"):
            i, f = new(), new()
            if k != "0":
                tr.append((i, t[1] if k == "s" else "", f))
            return i, f
        if k == ".":
            i1, f1 = go(t[1])
            i2, f2 = go(t[2])
            tr.append((f1, "", i2))
            return i1, f2
        if k == "+":
            i1, f1 = go(t[1])
            i2, f2 = go(t[2])
            i, f = new(), new()
            tr.extend([(i, "", i1), (i, "", i2), (f1, "", f), (f2, "", f)])
            return i, f
        i1, f1 = go(t[1])
        i, f = new(), new()
        tr.extend([(i, "", i1), (f1, "", f), (i, "", f), (f1, "", i1)])
        return i, f

    i, f = go(t)
    return Aut(sigma, tr, [i], [f], list(range(cnt[0])))


def nops(t):
    """Number of occurrences of letters, ε, ∅, + and * (concatenations excluded): Thompson has exactly 2n states."""
    if isinstance(t, str):
        t = parse(t)
    return (t[0] != ".") + sum(nops(x) for x in t[1:] if isinstance(x, tuple))


def aut_of(e, sigma):
    return thompson(e, sigma)


def check_aut(A, pred, n, dfa=False, complete=False):
    """The automaton accepts exactly the words <= n letters satisfying pred."""
    if dfa:
        assert A.is_dfa(), "not deterministic"
    if complete:
        assert A.is_complete(), "not complete"
    for w in words(A.sigma, n):
        assert A.accepts(w) == bool(pred(w)), f"automaton vs spec on {w!r}"
    return A


def check_eq(A, e):
    """Exact: the automaton and the expression denote the same language."""
    ok, w = A.equivalent(thompson(e, A.sigma))
    assert ok, f"{e!r} differs from the automaton on {w!r}"
    return e


# ---- state elimination (Brzozowski-McCluskey)

def _alt(x, y):
    if x == y or y == EMPTY_T:
        return x
    return y if x == EMPTY_T else ("+", x, y)


def _cat(x, y):
    if EMPTY_T in (x, y):
        return EMPTY_T
    return y if x == EPS_T else x if y == EPS_T else (".", x, y)


def _star(x):
    return EPS_T if x in (EMPTY_T, EPS_T) else x if x[0] == "*" else ("*", x)


def bmc(A, order):
    """State elimination: returns (tree of the language, log). New initial i='i' and final f='f' are always added."""
    E = {}
    for p, a, q in A.trans():
        E[(p, q)] = _alt(E.get((p, q), EMPTY_T), EPS_T if a == "" else ("s", a))
    for q in A.init:
        E[("i", q)] = EPS_T
    for q in A.final:
        E[(q, "f")] = _alt(E.get((q, "f"), EMPTY_T), EPS_T)
    log = []
    for q in order:
        loop = _star(E.pop((q, q), EMPTY_T))
        ins = [(p, e) for (p, r), e in list(E.items()) if r == q]
        outs = [(r, e) for (p, r), e in list(E.items()) if p == q]
        for p, _ in ins:
            del E[(p, q)]
        for r, _ in outs:
            del E[(q, r)]
        news = []
        for p, e1 in ins:
            for r, e2 in outs:
                new = _cat(_cat(e1, loop), e2)
                E[(p, r)] = _alt(E.get((p, r), EMPTY_T), new)
                news.append((p, r, E[(p, r)]))
        log.append((q, news))
    return E.get(("i", "f"), EMPTY_T), log


# ---------------------------------------------------------------- figures (states, labelled arrows, initial arrow, double circles)

_DX, _DY, _R = 82, 74, 17


def _lab(a):
    return "ε" if a == "" else a


def fig(A, pos, bend=None, loops=None, names=None, cap=""):
    """Markdown image of an automaton. pos = {state: (column, row)}; bend = {(p, q): pixels} to curve an arrow (positive side
    = left of the direction p -> q turned clockwise on screen); loops = {state: 'down'} to put a loop under the state."""
    bend, loops, names = bend or {}, loops or {}, names or {}
    assert set(pos) == set(A.Q), f"positions {set(pos) ^ set(A.Q)}"
    P = {q: (45 + x * _DX, 50 + y * _DY) for q, (x, y) in pos.items()}
    groups = collections.OrderedDict()
    for p, a, q in A.trans():
        groups.setdefault((p, q), []).append(_lab(a))
    parts, xs, ys = [], [], []

    def box(x, y):
        xs.append(x)
        ys.append(y)

    for q, (x, y) in P.items():
        box(x - _R, y - _R)
        box(x + _R, y + _R)
    for (p, q), labs in groups.items():
        lab = html.escape(",".join(labs))
        (x1, y1), (x2, y2) = P[p], P[q]
        if p == q:
            s = -1 if loops.get(p) != "down" else 1
            parts.append(f'<path d="M{x1 - 9:.1f},{y1 + s * 14.5:.1f} C{x1 - 26:.1f},{y1 + s * 48:.1f} {x1 + 26:.1f},{y1 + s * 48:.1f} '
                         f'{x1 + 9:.1f},{y1 + s * 14.5:.1f}" marker-end="url(#h)"/>')
            parts.append(f'<text x="{x1:.1f}" y="{y1 + s * 41 + (4 if s > 0 else 0):.1f}">{lab}</text>')
            box(x1 - 26, y1 + s * 52)
            box(x1 - len(lab) * 4.5, y1 + s * 41)
            box(x1 + len(lab) * 4.5, y1 + s * 41)
            continue
        dx, dy = x2 - x1, y2 - y1
        L = (dx * dx + dy * dy) ** 0.5
        ux, uy = dx / L, dy / L
        nx, ny = -uy, ux
        b = bend.get((p, q), 22 if (q, p) in groups else 0)
        cx, cy = (x1 + x2) / 2 + 2 * b * nx, (y1 + y2) / 2 + 2 * b * ny
        def clip(px, py, tx, ty):
            d = ((tx - px) ** 2 + (ty - py) ** 2) ** 0.5
            return px + _R * (tx - px) / d, py + _R * (ty - py) / d
        sx, sy = clip(x1, y1, cx, cy)
        ex, ey = clip(x2, y2, cx, cy)
        parts.append(f'<path d="M{sx:.1f},{sy:.1f} Q{cx:.1f},{cy:.1f} {ex:.1f},{ey:.1f}" marker-end="url(#h)"/>')
        sgn = -1 if b == 0 else (1 if b > 0 else -1)
        mx, my = (x1 + x2) / 2 + b * nx + sgn * 11 * nx, (y1 + y2) / 2 + b * ny + sgn * 11 * ny
        if b == 0 and abs(uy) < 0.3:
            my = (y1 + y2) / 2 - 8 * (1 if ny < 0 else -1) * -1 - 0
            my = (y1 + y2) / 2 - 9
        parts.append(f'<text x="{mx:.1f}" y="{my + 4:.1f}">{lab}</text>')
        box(cx, cy)
        box(mx - len(lab) * 4.5 - 3, my - 9)
        box(mx + len(lab) * 4.5 + 3, my + 9)
    for q, (x, y) in P.items():
        label = html.escape(str(names.get(q, q)))
        parts.append(f'<circle cx="{x}" cy="{y}" r="{_R}"/>')
        if q in A.final:
            parts.append(f'<circle cx="{x}" cy="{y}" r="{_R - 4}"/>')
        parts.append(f'<text x="{x}" y="{y + 4.5}"{" class=s" if len(label) > 3 else ""}>{label}</text>')
    for q in A.init:
        x, y = P[q]
        parts.append(f'<path d="M{x - _R - 26},{y} L{x - _R},{y}" marker-end="url(#h)"/>')
        box(x - _R - 28, y)
    if cap:
        parts.append(f'<text class="c" x="{(min(xs) + max(xs)) / 2:.1f}" y="{max(ys) + 22:.1f}">{html.escape(cap)}</text>')
        ys.append(max(ys) + 28)
    x0, y0 = min(xs) - 8, min(ys) - 8
    Wd, Ht = int(max(xs) + 8 - x0), int(max(ys) + 8 - y0)
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{Wd}" height="{Ht}" viewBox="{x0:.0f} {y0:.0f} {Wd} {Ht}" '
           'font-family="JetBrains Mono, Menlo, Consolas, monospace" font-size="14" text-anchor="middle">'
           '<defs><marker id="h" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
           '<path d="M0,0 L10,5 L0,10 z" fill="#111" stroke="none"/></marker></defs>'
           f'<rect x="{x0:.0f}" y="{y0:.0f}" width="{Wd}" height="{Ht}" fill="#fff"/>'
           '<style>path,circle{stroke:#111;stroke-width:1.5;fill:none}#h path{fill:#111;stroke:none}circle{fill:#fff}text{fill:#111}.s{font-size:10px}'
           '.c{font-size:14px;font-weight:700}</style>' + "".join(parts) + "</svg>")
    name = "thlr-" + hashlib.sha1(svg.encode()).hexdigest()[:12] + ".svg"
    path = FIG_DIR / name
    if not path.exists() or path.read_text() != svg:
        FIG_DIR.mkdir(parents=True, exist_ok=True)
        path.write_text(svg)
    alt = (f"Automate sur {{{','.join(A.sigma)}}}, état initial {','.join(str(names.get(q, q)) for q in sorted(A.init, key=A.ix.get))}, "
           f"états finaux {','.join(str(names.get(q, q)) for q in sorted(A.final, key=A.ix.get)) or 'aucun'}. Transitions : "
           + " ; ".join(f"{names.get(p, p)} -{_lab(a)}-> {names.get(q, q)}" for p, a, q in A.trans()))
    alt = alt.replace("[", "(").replace("]", ")")
    return f"![{alt}]({FIG_URL}{name})"


# ---------------------------------------------------------------- tables (LaTeX arrays) and exercise builders

def sset(S):
    return r"\{" + ",".join(str(x) for x in sorted(S, key=str)) + r"\}" if S else r"\varnothing"


def sname(q):
    return sset(q) if isinstance(q, frozenset) else str(q)


def table(A, eps=False):
    """Transition table of any automaton as a LaTeX array (→ initial, * final); a cell lists the successors."""
    cols = (("",) if eps else ()) + A.sigma
    head = " & ".join([r"\text{état}"] + [r"\varepsilon" if c == "" else c for c in cols])
    rows = []
    for q in A.Q:
        mark = (r"\rightarrow" if q in A.init else "") + ("*" if q in A.final else "")
        cells = []
        for c in cols:
            T = A.d.get((q, c), set())
            cells.append(sname(next(iter(T))) if A.is_dfa() and T else sset(T))
        rows.append(" & ".join([f"{mark}\\;{sname(q)}"] + cells))
    return r"$$\begin{array}{l|" + "c" * len(cols) + "}" + head + r"\\\hline " + r"\\ ".join(rows) + r"\end{array}$$"


def trans_list(A):
    """Transitions as a LaTeX list (for ε-NFA built by Thompson)."""
    return ", ".join(f"{p}\\xrightarrow{{{r'\varepsilon' if a == '' else a}}}{q}" for p, a, q in A.trans())


def v(id, enonce, calc, ans, sol, src=None, duree=None):
    CHECKED.append(id)
    e = {"id": id, "kind": "value", "enonce": enonce, "calc": str(calc), "ans": str(ans), "sol": f"**Réponse :** ${ans}$\n\n{sol}"}
    if src:
        e["src"] = src
    if duree:
        e["duree"] = duree
    return e


def o(id, enonce, sol, src=None, duree=None):
    CHECKED.append(id)
    e = {"id": id, "kind": "open", "enonce": enonce, "sol": sol}
    if src:
        e["src"] = src
    if duree:
        e["duree"] = duree
    return e


def _v(enonce, calc, ans, sol):
    return {"enonce": enonce, "calc": str(calc), "ans": str(ans), "sol": f"**Réponse :** ${ans}$\n\n{sol}"}


# ---------------------------------------------------------------- notions

NOTIONS = [
    {"id": "ens", "titre": "Rappel S1/S2 : ensembles, parties, produit cartésien",
     "formule": r"$|A\cup B|=|A|+|B|-|A\cap B|$ · $|A\times B|=|A||B|$ · $|\mathcal P(E)|=2^{|E|}$ · $\binom n2=\frac{n(n-1)}2$",
     "exemple": r"$|E|=5$ : $E$ a $2^5=32$ parties (c'est la borne de la déterminisation)",
     "cours": r"Un automate à $n$ états a $2^n$ ensembles d'états possibles. Un ensemble est une collection d'éléments distincts : $\{0,0,1\}$ n'est pas un ensemble. Rappel S1 : parcours « Ensembles » (`obm`)."},
    {"id": "rec", "titre": "Rappel S1/S2 : récurrence, relations d'équivalence, listes",
     "formule": r"$\sum_{k=0}^n2^k=2^{n+1}-1$ · classes d'équivalence = partition · un mot est une liste de lettres · $k^n$ mots de longueur $n$ sur $k$ lettres",
     "exemple": r"Mots de longueur $\le3$ sur $\{a,b\}$ : $1+2+4+8=15$",
     "cours": r"Récurrence : cas de base, puis hérédité. Une relation d'équivalence (réflexive, symétrique, transitive) découpe l'ensemble en classes disjointes : c'est ce que fera l'indistinguabilité des états. Principe des tiroirs : $n+1$ objets dans $n$ boîtes, une boîte en contient deux (base du lemme de l'étoile). Rappel : parcours `algo-s1-taa` (listes)."},
    {"id": "mots", "titre": "Alphabet, mots, longueur, concaténation, puissance",
     "formule": r"$|uv|=|u|+|v|$ · $|w^k|=k|w|$ · $|w|_a$ = nombre de $a$ · $w^R$ miroir · $\varepsilon$ neutre, $uv\neq vu$",
     "exemple": r"$w=011101$ : $|w|=6$, $|w|_1=4$",
     "cours": r"Un alphabet $\Sigma$ est un ensemble fini de lettres, un mot une suite finie de lettres, $\Sigma^*$ l'ensemble de tous les mots. La concaténation est associative, non commutative, de neutre $\varepsilon$. Un palindrome vérifie $w=w^R$."},
    {"id": "pref", "titre": "Préfixes, suffixes et facteurs",
     "formule": r"$w=xy$ : $x\in\mathrm{Pref}(w)$ · $w=yz$ : $z\in\mathrm{Suff}(w)$ · $w=xyz$ : $y\in\mathrm{Fact}(w)$ · $\mathrm{Fact}(w)=\mathrm{Pref}(\mathrm{Suff}(w))$",
     "exemple": r"$\mathrm{Pref}(SUP)=\{\varepsilon,S,SU,SUP\}$",
     "cours": r"$\varepsilon$ et $w$ sont toujours préfixe, suffixe et facteur de $w$. Les préfixes ont des longueurs toutes différentes : $|\mathrm{Pref}(w)|=|w|+1$, de même pour les suffixes. Pour les facteurs il peut y avoir des doublons (dans $abab$, $ab$ apparaît deux fois), donc $|\mathrm{Fact}(w)|\le\frac{|w|(|w|+1)}2+1$."},
    {"id": "dist", "titre": "Distance d'édition",
     "formule": r"$d_e(u,v)$ = nombre minimal d'insertions et suppressions de lettres · $d_e(u,v)=|u|+|v|-2|\mathrm{PLSC}(u,v)|$",
     "exemple": r"$d_e(dog,bugs)=5$",
     "cours": r"Séparation, symétrie, inégalité triangulaire : c'est une distance. On l'obtient par programmation dynamique : si les dernières lettres sont égales, $d(i,j)=d(i-1,j-1)$, sinon $1+\min(d(i-1,j),d(i,j-1))$. PLSC : plus longue sous-suite commune."},
    {"id": "lang", "titre": "Opérations sur les langages",
     "formule": r"$L_1L_2=\{uv\mid u\in L_1,v\in L_2\}$ · $L^0=\{\varepsilon\}$ · $L^*=\bigcup_{n\ge0}L^n$ · $\varepsilon\in L^*$ toujours · $\varnothing^*=\{\varepsilon\}$",
     "exemple": r"$\{ab,ac\}\{cd,de\}=\{abcd,abde,accd,acde\}$",
     "cours": r"Un langage est un ensemble de mots ($L\subseteq\Sigma^*$). $L^k\neq\{u^k\mid u\in L\}$ : on concatène $k$ mots éventuellement différents. $L^+=LL^*$ ne contient $\varepsilon$ que si $\varepsilon\in L$."},
    {"id": "rx-sem", "titre": "Expressions rationnelles : syntaxe et sémantique",
     "formule": r"$L(\varnothing)=\varnothing$ · $L(\varepsilon)=\{\varepsilon\}$ · $L(a)=\{a\}$ · $L(e+f)=L(e)\cup L(f)$ · $L(ef)=L(e)L(f)$ · $L(e^*)=L(e)^*$",
     "exemple": r"$L((a+b)^*b)$ = mots terminant par $b$",
     "cours": r"Priorités : étoile, puis concaténation, puis $+$. Sucre : $e?=\varepsilon+e$, $e^+=ee^*$, $[a\text{-}c]=a+b+c$. Pas d'intersection ni de complément dans la syntaxe. Un langage est rationnel s'il est décrit par une expression."},
    {"id": "rx-desc", "titre": "Équivalences d'expressions rationnelles",
     "formule": r"$(ef)^*e\equiv e(fe)^*$ · $e^{**}\equiv e^*$ · $(e^*f^*)^*\equiv(e+f)^*\equiv(e^*+f)^*$ · $e\varnothing\equiv\varnothing$ · $e\varepsilon\equiv e$ · $e(f+g)\equiv ef+eg$",
     "exemple": r"$((abc)^*(acb)^*)^*\equiv(abc+acb)^*$",
     "cours": r"Pour comparer deux expressions : chercher un mot dans l'une et pas l'autre (souvent $\varepsilon$ ou un mot court) pour prouver qu'elles diffèrent ; sinon réécrire avec les identités. Les relations possibles : égalité, inclusion stricte dans un sens ou dans l'autre, incomparables."},
    {"id": "rx-ecr", "titre": "Écrire l'expression rationnelle d'un langage",
     "formule": r"mots de longueur paire : $((a+b)(a+b))^*$ · finissant par $ab$ : $(a+b)^*ab$ · sans facteur $aa$ : $(b+ab)^*(\varepsilon+a)$",
     "exemple": r"exactement deux $a$ : $b^*ab^*ab^*$",
     "cours": r"Méthode : découper le langage en blocs concaténés ; une disjonction de cas devient $+$, une répétition devient une étoile. Vérifier avec des mots courts, dont $\varepsilon$ et un mot juste hors du langage."},
    {"id": "afd", "titre": "Automates finis : mot accepté, DFA et NFA",
     "formule": r"$A=(Q,\Sigma,\delta,I,F)$ · $w$ accepté s'il existe un chemin de $I$ vers $F$ étiqueté $w$ · DFA : un seul état initial, au plus une arête par lettre et état",
     "exemple": r"un NFA peut avoir plusieurs chemins étiquetés par $w$ : un seul chemin acceptant suffit",
     "cours": r"Deux façons de refuser un mot : un chemin existe mais finit hors de $F$, ou aucun chemin n'existe (arête manquante). Dans un DFA, un mot a au plus un chemin. Deux automates sont équivalents s'ils reconnaissent le même langage."},
    {"id": "afd-build", "titre": "Construire un automate pour un langage",
     "formule": r"un état = ce qu'il faut retenir de la partie lue · multiples de 3 en binaire : $r\mapsto(2r+c)\bmod3$ · « avant-dernière lettre $a$ » : NFA à 3 états",
     "exemple": r"mots terminant par $ab$ : NFA à 3 états, boucle sur $0$, puis $a$, puis $b$",
     "cours": r"Décider ce que la mémoire finie doit retenir (reste, parité, dernier motif lu) : chaque valeur possible est un état. Pour un NFA on devine l'endroit où le motif commence. Toujours tester sur des mots acceptés et refusés."},
    {"id": "compl", "titre": "Complétion et complément",
     "formule": r"complet : $\forall q,\forall a$, une arête au moins · complétion : état puits · complément : échanger $F$ et $Q\setminus F$ (DFA complet seulement)",
     "exemple": r"un DFA à $n$ états sur $k$ lettres, complété, a au plus $(n+1)k$ transitions",
     "cours": r"Le complément d'un langage rationnel est rationnel. Il faut un DFA complet : sinon un mot sans chemin resterait refusé des deux côtés ; il faut un DFA : sinon un mot avec un chemin acceptant et un chemin refusant serait accepté des deux côtés."},
    {"id": "thompson", "titre": "ε-NFA et algorithme de Thompson",
     "formule": r"un seul état initial $i$, un seul état final $f$ distinct · atomes $a$, $\varepsilon$, $\varnothing$ · $e_1e_2$ : $f_1\xrightarrow\varepsilon i_2$ · $e_1+e_2$ et $e^*$ : deux nouveaux états · $2n$ états",
     "exemple": r"$(a+b)^*abb$ : $n=7$ (5 lettres, un $+$, une étoile) donc 14 états",
     "cours": r"Théorème de Kleene (sens expression $\to$ automate) : toute expression a un ε-NFA équivalent. Ne pas fusionner $f_1$ et $i_2$ à la concaténation (contre-exemple $a(ba)^*a(ba)^*$). L'étoile ajoute les ε-arêtes $i\to i_1$, $f_1\to f$, $i\to f$ (mot vide) et $f_1\to i_1$ (répétition)."},
    {"id": "eps", "titre": "Suppression des ε-transitions (retour arrière)",
     "formule": r"$\varepsilon\text{-clôture}(q)=\{p\mid q\xrightarrow{\varepsilon^*}p\}$ · $q\xrightarrow a r$ si $p\xrightarrow ar$ avec $p\in$ clôture$(q)$ · $q$ final si clôture$(q)\cap F\ne\varnothing$",
     "exemple": r"$a^*b^*c^*$ : clôture$(0)=\{0,1,2\}$",
     "cours": r"On calcule les clôtures par point fixe : colonne 0 = $q$ et ses successeurs par $\varepsilon$, colonne $i+1$ = union des cellules des éléments de la colonne $i$, jusqu'à stabilité. Même nombre d'états, aucune ε-transition. Ne pas oublier les nouveaux états finaux."},
    {"id": "emond", "titre": "Émondage",
     "formule": r"accessible : atteint depuis $I$ · co-accessible : atteint $F$ · utile = les deux · l'automate émondé garde les états utiles",
     "exemple": r"un état puits est accessible mais pas co-accessible : il disparaît",
     "cours": r"Accessibles : parcours depuis $I$. Co-accessibles : parcours depuis $F$ en inversant les arêtes. Le langage ne change pas. Un DFA complet émondé perd son état puits : il redevient incomplet."},
    {"id": "det", "titre": "Déterminisation (construction des sous-ensembles)",
     "formule": r"état = ensemble d'états · initial $I$ · $S\xrightarrow aS_a=\{q\mid\exists p\in S,p\xrightarrow aq\}$ · final si $S\cap F\ne\varnothing$ · au plus $2^n$ états",
     "exemple": r"avant-dernière lettre $a$ : NFA à 3 états, DFA à 4 états",
     "cours": r"Table : une ligne par ensemble découvert, une colonne par lettre ; on commence par $I$ et on ajoute tout nouvel ensemble jusqu'à stabilité. L'ensemble vide est un état (puits). On applique d'abord la suppression des ε. Le DFA est complet. Le « $n$-ième symbole avant la fin est $a$ » donne $2^n$ états : l'explosion est atteinte."},
    {"id": "min", "titre": "Minimisation (Moore) et Myhill-Nerode",
     "formule": r"$p\sim q$ si $\forall w$ ($pw\in F\iff qw\in F$) · classes initiales $F$ et $Q\setminus F$ · séparer si les successeurs sont dans des classes différentes · un état = une classe",
     "exemple": r"6 états $\to$ 4 classes",
     "cours": r"On part d'un DFA complet accessible. Moore : raffiner la partition tant qu'une cellule contient deux états dont les successeurs par une lettre sont dans des classes différentes. Le DFA minimal est unique (Myhill-Nerode) : son nombre d'états est le nombre de classes d'indistinguabilité. Un mot distingue deux états si l'un l'accepte et pas l'autre."},
    {"id": "pomp", "titre": "Lemme de l'étoile (lemme de pompage)",
     "formule": r"$L$ rationnel $\Rightarrow\exists n_0,\forall w\in L,|w|\ge n_0,\ w=xyz,\ y\ne\varepsilon,\ xy^*z\subseteq L$ · DFA à $n$ états : tout mot de longueur $\ge n$ repasse par un état",
     "exemple": r"$\{a^nb^n\}$ n'est pas rationnel (prendre $w=a^{n_0}b^{n_0}$)",
     "cours": r"Pour prouver qu'un langage n'est pas rationnel : par l'absurde, fixer $n_0$, choisir un mot $w$ de $L$ de longueur $\ge n_0$ (en fonction de $n_0$), considérer **toute** décomposition $w=xyz$ avec $y\ne\varepsilon$ (et $|xy|\le n_0$ si on l'utilise), et trouver $k$ avec $xy^kz\notin L$. Le lemme est une condition nécessaire, jamais suffisante. Pour prouver qu'un langage est rationnel, on donne un automate."},
    {"id": "bmc", "titre": "Élimination d'états (Brzozowski-McCluskey)",
     "formule": r"étiquettes = expressions · $p\xrightarrow xq\xrightarrow yr$ avec boucle $z$ sur $q$ : $p\xrightarrow{xz^*y}r$ · $(\text{entrantes})\times(\text{sortantes})$ nouvelles arêtes · arêtes parallèles : $+$",
     "exemple": r"$p\xrightarrow aq\xrightarrow cr$ avec boucle $b$ sur $q$ : $p\xrightarrow{ab^*c}r$",
     "cours": r"On ajoute un état initial $i$ sans arête entrante et un état final $f$ sans arête sortante (liés par $\varepsilon$), puis on supprime les autres états un par un. À la fin il reste une arête $i\to f$ étiquetée par $e$. Le résultat dépend de l'ordre mais le langage est le même. C'est l'autre sens du théorème de Kleene : automate $\to$ expression."},
    {"id": "stab", "titre": "Stabilité et décidabilité des langages rationnels",
     "formule": r"stables par $\cup,\cdot,{}^*$, complément, $\cap=\overline{\overline{L_1}\cup\overline{L_2}}$, miroir, Pref, Suff, Fact · produit synchronisé : $\le n_1n_2$ états · $L=\varnothing$ ? parcours · $L_1=L_2$ ? vide$(L_1\cap\overline{L_2})$ et vide$(L_2\cap\overline{L_1})$",
     "exemple": r"$L_1\setminus L_2=L_1\cap\overline{L_2}$ est rationnel",
     "cours": r"Produit synchronisé de deux DFA complets : états $(p,q)$, $(p,q)\xrightarrow a(p',q')$, final si les deux composantes sont finales (intersection). Si les langages diffèrent, la recherche du vide renvoie un contre-exemple. Pour montrer qu'un langage n'est pas rationnel on peut aussi l'intersecter avec un rationnel ($a^*b^*$) et obtenir un langage connu non rationnel."},
]


# ---------------------------------------------------------------- small computations used by the checks

def pref(w):
    return {w[:i] for i in range(len(w) + 1)}


def suff(w):
    return {w[i:] for i in range(len(w) + 1)}


def fact(w):
    return {w[i:j] for i in range(len(w) + 1) for j in range(i, len(w) + 1)}


def de(u, v):
    """Edit distance with insertions and deletions only (dynamic programming), checked against |u|+|v|-2 PLSC."""
    D = [[0] * (len(v) + 1) for _ in range(len(u) + 1)]
    for i in range(len(u) + 1):
        for j in range(len(v) + 1):
            if i == 0 or j == 0:
                D[i][j] = i + j
            elif u[i - 1] == v[j - 1]:
                D[i][j] = D[i - 1][j - 1]
            else:
                D[i][j] = 1 + min(D[i - 1][j], D[i][j - 1])
    L = [[0] * (len(v) + 1) for _ in range(len(u) + 1)]
    for i in range(1, len(u) + 1):
        for j in range(1, len(v) + 1):
            L[i][j] = L[i - 1][j - 1] + 1 if u[i - 1] == v[j - 1] else max(L[i - 1][j], L[i][j - 1])
    assert D[-1][-1] == len(u) + len(v) - 2 * L[-1][-1]
    return D[-1][-1]


def lcat(L1, L2):
    return {u + w for u in L1 for w in L2}


def lpow(L, k):
    out = {""}
    for _ in range(k):
        out = lcat(out, L)
    return out


def in_star(w, L):
    ok = [True] + [False] * len(w)
    for j in range(1, len(w) + 1):
        ok[j] = any(ok[j - len(u)] and w[j - len(u):j] == u for u in L if 0 < len(u) <= j)
    return ok[-1]


def rel(e, f, sigma):
    """Relation between L(e) and L(f): '=', '<' (strict inclusion), '>' or '||' (incomparable), exact (Thompson + subset + product)."""
    def det(x):
        return thompson(x, sigma).remove_eps().determinize()
    A, B = det(e), det(f)
    ab = A.product(B, "minus").shortest() is None   # L(e) included in L(f)
    ba = B.product(A, "minus").shortest() is None
    return "=" if ab and ba else "<" if ab else ">" if ba else "||"


# ---------------------------------------------------------------- levels 1 to 9 (reminders, words, languages, expressions)

PAIRS = [("a*b(ab)*", "a*(bab)*"), ("a(bb)*", "ab*"), ("a(a+b)*b", "a*(a+b)*b*"), ("abc+acb", "a(b+c)(c+b)"), ("a*bc+a*cb", "a*(bc+a*cb)"), ("(abc+acb)*", "((abc)*(acb)*)*"), ("(abc+acb)(abc+acb)*", "((abc)*(acb)*)((abc)*(acb)*)*"), ("(abc+acb)*", "(abc(acb)*)*"), ("(abc+acb)*", "(a(bc)*(cb)*)*")]
# ---------------------------------------------------------------- the automata of the exercises (with their drawing)

def _has_run(A, w):
    S = set(A.init)
    for c in w:
        S = {r for p in S for r in A.d.get((p, c), ())}
        if not S:
            return False
    return True


def row(n, y=0):
    return {i: (i, y) for i in range(n)}


DAB = Aut("ab", [(0, "a", 1), (0, "b", 0), (1, "a", 1), (1, "b", 2), (2, "a", 1), (2, "b", 0)], [0], [2])      # finit par ab
P_DAB, B_DAB = row(3), {(2, 0): -52}
NABA = Aut("ab", [(0, "a", 0), (0, "b", 0), (0, "a", 1), (1, "b", 2), (2, "a", 3)], [0], [3])                    # finit par aba
P_NABA = row(4)
AREF = Aut("abc", [(0, "a", 1), (1, "b", 2), (1, "c", 3), (3, "a", 0)], [0], [2])
P_AREF = {0: (0, 0), 1: (1, 0), 2: (2, 0), 3: (1, 1.3)}
B1 = Aut("ab", [(0, "a", 1), (0, "b", 3), (1, "b", 2), (1, "a", 3), (2, "a", 2), (2, "b", 2), (3, "a", 3), (3, "b", 3)], [0], [2])
P_B1 = {0: (0, 0), 1: (1, 0), 2: (2, 0), 3: (1, 1.3)}
L_B1 = {3: "down"}
B2 = Aut("ab", [(0, "a", 0), (0, "b", 0), (0, "a", 1), (1, "b", 2)], [0], [2])
P_B2 = row(3)
N2 = Aut("ab", [(0, "a", 0), (0, "b", 0), (0, "a", 1), (1, "a", 2), (1, "b", 2)], [0], [2])                      # avant-dernière lettre a
P_N2 = row(3)
N3 = Aut("ab", [(0, "a", 0), (0, "b", 0), (0, "a", 1), (1, "a", 2), (1, "b", 2), (2, "a", 3), (2, "b", 3)], [0], [3])  # 3e avant la fin
P_N3 = row(4)
N4 = Aut("ab", N3.trans() + [(3, "a", 4), (3, "b", 4)], [0], [4])
P_N4 = row(5)
D3 = Aut("01", [(0, "0", 0), (0, "1", 1), (1, "0", 2), (1, "1", 0), (2, "0", 1), (2, "1", 2)], [0], [0])
P_D3, B_D3 = row(3), {}
B5 = Aut("ab", [(0, "a", 1), (1, "a", 0), (2, "a", 3), (3, "a", 2), (0, "b", 2), (2, "b", 0), (1, "b", 3), (3, "b", 1)], [0], [2])
N_B5 = {0: "00", 1: "10", 2: "01", 3: "11"}
P_B5, B_B5 = {0: (0, 0), 1: (1.3, 0), 2: (0, 1.5), 3: (1.3, 1.5)}, {}
I1 = Aut("ab", [(0, "a", 1), (1, "a", 1), (1, "b", 2)], [0], [2])                                                  # incomplet, a^+ b
P_I1 = row(3)
I2 = Aut("ab", [(0, "a", 1), (1, "b", 1)], [0], [1])                                                                # incomplet, a b*
P_I2 = row(2)
E2 = Aut("abc", [(0, "a", 0), (0, "", 1), (1, "b", 1), (1, "", 2), (2, "c", 2)], [0], [2])                          # a* b* c*
P_E2 = row(3)
E3 = Aut("a", [(0, "", 1), (0, "", 3), (1, "", 2), (2, "", 3), (3, "", 0)], [0], [3])
E4 = Aut("a", [(0, "", 1), (1, "a", 2), (2, "", 3)], [0], [3])
P_E4 = row(4)
E5 = Aut("a", [(0, "", 1), (1, "", 2), (2, "", 0)], [0], [2])
P1 = Aut("ab", [(0, "a", 1), (1, "b", 2), (2, "a", 4), (4, "b", 1), (0, "b", 3), (3, "a", 3), (5, "a", 4)], [0], [4])
P_P1, B_P1, L_P1 = {0: (0, 0), 1: (1, 0), 2: (2, 0), 4: (3, 0), 3: (0, 1.4), 5: (3, 1.4)}, {(4, 1): 45}, {3: "down"}
P2 = Aut("ab", [(0, "a", 1), (1, "a", 2), (2, "b", 2), (0, "b", 3), (3, "b", 3), (4, "a", 2)], [0], [2])
P_P2, B_P2, L_P2 = {0: (0, 0), 1: (1, 0), 2: (2, 0), 3: (0, 1.4), 4: (2, 1.4)}, {}, {3: "down"}
NABAB = Aut("abc", [(0, "a", 0), (0, "b", 0), (0, "c", 0), (0, "a", 1), (1, "b", 2), (2, "a", 3), (3, "b", 4)], [0], [4])
P_NABAB = row(5)
NC = Aut("abc", [(0, "a", 0), (0, "a", 1), (0, "c", 0), (1, "b", 2), (1, "c", 1), (2, "a", 2)], [0], [2])
P_NC = row(3)
M1 = Aut("ab", [(0, "a", 1), (0, "b", 3), (1, "a", 0), (1, "b", 2), (3, "a", 0), (3, "b", 4), (2, "a", 4), (2, "b", 5), (4, "a", 2), (4, "b", 5),
                (5, "a", 5), (5, "b", 5)], [0], [5])
P_M1 = {0: (0, 0), 1: (1, 0), 3: (1, 1.5), 2: (2.2, 0), 4: (2.2, 1.5), 5: (3.4, 0.75)}
M2 = Aut("ab", [(0, "a", 1), (0, "b", 3), (1, "a", 1), (1, "b", 2), (2, "a", 1), (2, "b", 0), (3, "a", 1), (3, "b", 0)], [0], [2])   # état 3 redondant
P_M2, B_M2 = {0: (0, 0), 1: (1.2, 0), 2: (2.4, 0), 3: (0, 1.4)}, {(2, 0): -52}
K1 = Aut("ab", [(0, "a", 1), (1, "a", 0), (0, "b", 0), (1, "b", 1)], [0], [0])                                      # nombre pair de a
P_K1, B_K1 = row(2), {}
K2 = Aut("ab", [(0, "a", 1), (0, "b", 0), (1, "a", 1), (1, "b", 0)], [0], [1])                                      # finit par a
P_K2, B_K2 = row(2), {}
K4 = Aut("abc", [(0, "a", 1), (1, "b", 1), (1, "c", 2), (2, "a", 1)], [0], [2])
P_K4 = row(3)
PB = Aut("ab", [(0, "a", 0), (0, "b", 1), (1, "a", 0), (1, "b", 1)], [0], [1])                                      # finit par b
P_PB = row(2)
Y0 = Aut("ab", [(0, "a", 0), (0, "b", 1), (1, "a", 1), (1, "b", 2), (2, "a", 2), (2, "b", 0)], [0], [0])            # |w|_b multiple de 3
P_Y0, B_Y0 = row(3), {(2, 0): -52}


def dfa_names(D):
    return {i: chr(65 + i) for i in range(len(D.Q))}


def dfa_fig(D, pos=None, bend=None, loops=None):
    """Drawing of a determinized automaton: states renamed A, B, C... (the legend lists their contents)."""
    R = D.renamed(lambda S: D.ix[S])
    n = len(D.Q)
    pos = pos or {i: (i % 4 * 1.0, i // 4 * 1.5) for i in range(n)}
    return fig(R, pos, bend, loops, names=dfa_names(D)), ", ".join(f"${chr(65 + i)}={sset(S)}$" for i, S in enumerate(D.Q))


def det_sol(N, pos=None, bend=None, loops=None, intro=""):
    D = N.determinize()
    ok, w = N.equivalent(D)
    assert ok and D.is_dfa() and D.is_complete(), w
    out = intro + "Table des sous-ensembles (on part de $I$, on ajoute chaque ensemble nouveau) :\n" + table(D)
    out += f"Le DFA est **complet** et a **{len(D.Q)} états**."
    if pos:
        f, legend = dfa_fig(D, pos, bend, loops)
        out += f"\n\n{f}\n\nLégende : {legend}."
    return out


def closure_cols(A):
    cols = [{q: frozenset([q]) | frozenset(A.d.get((q, ""), ())) for q in A.Q}]
    while True:
        c = cols[-1]
        nxt = {q: frozenset().union(*(c[p] for p in c[q])) for q in A.Q}
        cols.append(nxt)
        if nxt == c:
            return cols


def fix_step(A):
    return len(closure_cols(A)) - 2


def distinguish(A, p, q):
    """Shortest word accepted from exactly one of p, q (complete DFA)."""
    seen, todo = {(p, q): ""}, collections.deque([(p, q)])
    while todo:
        x, y = todo.popleft()
        if (x in A.final) != (y in A.final):
            return seen[(x, y)]
        for a in A.sigma:
            t = (next(iter(A.d[(x, a)])), next(iter(A.d[(y, a)])))
            if t not in seen:
                seen[t] = seen[(x, y)] + a
                todo.append(t)
    return None


def ntrans(A):
    return len(A.trans())



def _thompson_sol(e, sigma):
    """Model answer of a Thompson exercise: construction summary, transition list, checked against the expression."""
    T = thompson(e, sigma)
    for w in words(sigma, 7):
        assert T.accepts(w) == rx_match(e, w), (e, w)
    n = nops(e)
    i, f = next(iter(T.init)), next(iter(T.final))
    return (f"Expression $e={tex(e)}$ : $n={n}$ (lettres, $\\varepsilon$, $\\varnothing$, $+$, $*$, sans les concaténations), donc l'automate a $2n={2 * n}$ états. "
            "On construit chaque sous-expression avec deux nouveaux états (entrée, sortie), on relie par $\\varepsilon$ la sortie de $e_1$ à l'entrée de $e_2$ pour une concaténation, "
            "et on ajoute deux états et quatre $\\varepsilon$ pour $+$ et $*$ (l'étoile ajoute $i\\to f$ pour le mot vide et $f_1\\to i_1$ pour répéter). "
            f"États numérotés dans l'ordre de construction.\n\nÉtat initial ${i}$, état final ${f}$. Transitions : ${trans_list(T)}$.\n\n"
            f"Vérifié : cet automate accepte exactement les mots de $L(e)$ de longueur $\\le7$ (comparaison avec `re`), et $|Q|={len(T.Q)}=2n$.")



def _bmc_sol(A, order, pred, sigma, n):
    """Model answer of a state-elimination exercise; the expression is checked exactly and against the specification."""
    t, log = bmc(A, order)
    e = tex(t)
    check_eq(A, _plain(t))
    assert all(bool(pred(w)) == rx_match(_plain(t), w) for w in words(sigma, n))
    lines = [f"- On supprime l'état ${q}$ : " + (", ".join(f"${p}\\to {r}$ : ${tex(x)}$" for p, r, x in news) or "aucune nouvelle arête") for q, news in log]
    return ("On ajoute un état initial $i$ (lié par $\\varepsilon$ à l'état initial) et un état final $f$ (lié par $\\varepsilon$ depuis le final), puis on supprime les états "
            + ", ".join(f"${q}$" for q in order) + " dans cet ordre. Un état $q$ de boucle $z$ relie $p\\xrightarrow xq\\xrightarrow yr$ en $p\\xrightarrow{xz^*y}r$.\n\n"
            + "\n".join(lines) + f"\n\n**Résultat :** $e={e}$.\n\nVérifié : $e$ est équivalent à l'automate (équivalence exacte) et décrit le langage attendu sur tous les mots de longueur $\\le{n}$. L'ordre de suppression change l'écriture, pas le langage.")


def _plain(t):
    """Tree -> course syntax string (for parse/check)."""
    k = t[0]
    if k == "s":
        return t[1]
    if k == "e":
        return "ε"
    if k == "0":
        return "∅"
    if k == "*":
        return "(" + _plain(t[1]) + ")*"
    if k == ".":
        return "(" + _plain(t[1]) + ")(" + _plain(t[2]) + ")"
    return "(" + _plain(t[1]) + "+" + _plain(t[2]) + ")"


FAILED = None  # referenced only when a check above failed: raises a clear error in the sentence that uses it

LEVELS = [
    {"n": 1, "titre": "Rappel S1/S2 : ensembles, parties, produit cartésien", "notions": ["ens"], "exos": [
        v("n1", r"$|A|=12$, $|B|=9$ et $|A\cap B|=4$. Que vaut $|A\cup B|$ ?", "12+9-4", "17", r"$|A\cup B|=|A|+|B|-|A\cap B|=12+9-4=17$."),
        v("n2", r"Un ensemble $E$ a $6$ éléments. Combien de parties (sous-ensembles) a-t-il ?", sum(comb(6, k) for k in range(7)), "64", r"Chaque élément est dedans ou dehors : $2^6=64$. C'est la borne du nombre d'états d'un automate déterminisé."),
        v("n3", r"$|A|=5$ et $|B|=4$. Que vaut $|A\times B|$ ?", len(list(itertools.product(range(5), range(4)))), "20", r"$|A\times B|=|A|\times|B|=5\times4=20$."),
        v("n4", r"Combien de sous-ensembles à $2$ éléments un ensemble à $7$ éléments a-t-il ?", len(list(itertools.combinations(range(7), 2))), "21", r"$\binom72=\frac{7\times6}2=21$."),
        v("n5", r"Un automate a $3$ états et un alphabet à $2$ lettres. Combien de triplets (état, lettre, état) existe-t-il, c'est-à-dire quelle est la taille maximale de $\delta\subseteq Q\times\Sigma\times Q$ ?", len(list(itertools.product(range(3), "ab", range(3)))), "18", r"$|Q\times\Sigma\times Q|=3\times2\times3=18$."),
        v("n6", r"Combien d'entiers de $1$ à $20$ sont multiples de $2$ ou de $3$ ?", len([x for x in range(1, 21) if x % 2 == 0 or x % 3 == 0]), "13", r"$10$ multiples de $2$, $6$ de $3$, $3$ de $6$ : $10+6-3=13$."),
    ]},
    {"n": 2, "titre": "Rappel S1/S2 : récurrence, relations d'équivalence, listes", "notions": ["rec"], "exos": [
        v("r1", r"Calculer $\sum_{k=0}^{5}2^k$ (nombre de mots de longueur $\le5$ sur $\{a,b\}$).", sum(2 ** k for k in range(6)), "63", r"$\sum_{k=0}^n2^k=2^{n+1}-1=2^6-1=63$."),
        v("r2", r"Sur $\{0,\dots,15\}$, $x\sim y$ si $x\equiv y\pmod4$ (relation d'équivalence). Combien de couples $(x,y)$ vérifient $x\sim y$ ?", sum(1 for x in range(16) for y in range(16) if (x - y) % 4 == 0), "64", r"Il y a $4$ classes de $4$ éléments ; chaque classe fournit $4\times4=16$ couples : $4\times16=64$."),
        v("r3", r"Un mot est une liste de lettres. Combien de listes de longueur $4$ peut-on former avec l'alphabet $\{a,b,c\}$ ?", len(list(itertools.product("abc", repeat=4))), "81", r"$3$ choix par position : $3^4=81$."),
        o("r4", r"Démontrer par récurrence : $\forall n\ge0$, $\sum_{k=0}^n2^k=2^{n+1}-1$.",
          r"**Base** $n=0$ : $2^0=1=2^1-1$. **Hérédité** : si $\sum_{k=0}^n2^k=2^{n+1}-1$, alors $\sum_{k=0}^{n+1}2^k=2^{n+1}-1+2^{n+1}=2\cdot2^{n+1}-1=2^{n+2}-1$. La propriété est vraie pour tout $n$ (il y a donc $2^{n+1}-1$ mots de longueur $\le n$ sur $\{a,b\}$)."),
        o("r5", r"Montrer par récurrence sur $n$ qu'il y a $k^n$ mots de longueur $n$ sur un alphabet à $k$ lettres.",
          r"**Base** $n=0$ : un seul mot, $\varepsilon$, et $k^0=1$. **Hérédité** : un mot de longueur $n+1$ s'écrit de façon unique $wa$ avec $|w|=n$ ($k^n$ choix par hypothèse) et $a\in\Sigma$ ($k$ choix) : $k^n\cdot k=k^{n+1}$."),
        o("r6", r"Principe des tiroirs : un chemin de $m$ arêtes dans un graphe à $n$ sommets visite $m+1$ sommets. Montrer que si $m\ge n$ un sommet est visité deux fois.",
          r"Le chemin visite $m+1\ge n+1$ sommets (avec répétition) pris parmi $n$ sommets distincts : par le principe des tiroirs, deux positions du chemin portent le même sommet. Le morceau entre ces deux positions est une boucle. C'est l'idée du lemme de l'étoile (un mot de longueur $\ge n$ lu par un automate à $n$ états passe deux fois par un même état)."),
    ]},
    {"n": 3, "titre": "Mots : longueur, occurrences, puissance, miroir", "notions": ["mots"], "exos": [
        v("m1", r"Quelle est la longueur du mot $w=\mathtt{CatCatDog}$ (alphabet latin) ?", len("CatCatDog"), "9", r"Neuf lettres : $\mathtt{C,a,t,C,a,t,D,o,g}$."),
        v("m2", r"Soit $w=011101$. Que vaut $|w|_1$ (nombre de $1$) ?", "011101".count("1"), "4", r"Les positions $2,3,4,6$ valent $1$ : $|w|_1=4$ (et $|w|_0=2$, $|w|=6$)."),
        v("m3", r"Soit $w=\mathtt{abca}$. Que vaut $|w^5|$ ?", len("abca" * 5), "20", r"$|w^k|=k|w|=5\times4=20$."),
        v("m4", r"Le mot $w=\mathtt{radar}$ est-il un palindrome ($w=w^R$) ? Répondre $1$ si oui, $0$ sinon.", int("radar" == "radar"[::-1]), "1", r"$w^R=\mathtt{radar}=w$ : oui."),
        v("m5", r"Combien de mots de longueur $4$ sur $\{0,1\}$ contiennent exactement deux $1$ ?", len([w for w in words("01", 4) if len(w) == 4 and w.count("1") == 2]), "6", r"On choisit les positions des deux $1$ : $\binom42=6$."),
        v("m6", r"Soient $u=\mathtt{abc}$ et $v=\mathtt{de}$. Quelle est la longueur de $u\cdot v\cdot u^R$ ?", len("abc" + "de" + "abc"[::-1]), "8", r"$|uvu^R|=|u|+|v|+|u|=3+2+3=8$ (la longueur est additive)."),
    ]},
    {"n": 4, "titre": "Préfixes, suffixes et facteurs", "notions": ["pref"], "exos": [
        v("p1", r"Combien de préfixes (distincts, $\varepsilon$ compris) le mot $\mathtt{SUP}$ a-t-il ?", len(pref("SUP")), "4", r"$\mathrm{Pref}(SUP)=\{\varepsilon,S,SU,SUP\}$ : $|w|+1=4$."),
        v("p2", r"Combien de suffixes distincts le mot $\mathtt{abcabc}$ a-t-il ?", len(suff("abcabc")), "7", r"Les suffixes ont des longueurs $0$ à $6$, donc sont distincts : $7$."),
        v("p3", r"Combien de facteurs distincts (mot vide compris) le mot $\mathtt{abab}$ a-t-il ?", len(fact("abab")), "8", r"$\varepsilon,a,b,ab,ba,aba,bab,abab$. Les facteurs $a$, $b$, $ab$ apparaissent deux fois mais comptent une fois."),
        v("p4", r"Le mot $\mathtt{ba}$ est-il un facteur de $\mathtt{aabba}$ ? Répondre $1$ si oui, $0$ sinon.", int("ba" in fact("aabba")), "1", r"$\mathtt{aabba}=\mathtt{aab}\cdot\mathtt{ba}$ : c'est même un suffixe."),
        v("p5", r"On appelle facteurs propres de $w$ ceux qui ne sont ni préfixes ni suffixes de $w$. Combien $\mathtt{aaabbb}$ en a-t-il ?", len(fact("aaabbb") - pref("aaabbb") - suff("aaabbb")), "4", r"Facteurs de $a^3b^3$ : $\varepsilon$, $a^i$, $b^j$, $a^ib^j$ ($1\le i,j\le3$) soit $16$. Préfixes et suffixes réunis : $12$. Reste $\mathtt{ab},\mathtt{aab},\mathtt{abb},\mathtt{aabb}$ : $4$.", src=None),
        o("p6", r"Montrer que $\mathrm{Fact}(w)=\mathrm{Pref}(\mathrm{Suff}(w))$, puis que l'égalité $\mathrm{Fact}(L)=\mathrm{Pref}(L)\cup\mathrm{Suff}(L)$ est fausse en général.",
          r"**Première égalité.** Si $y\in\mathrm{Fact}(w)$, $w=xyz$ ; $yz$ est un suffixe de $w$ et $y$ est un préfixe de $yz$, donc $y\in\mathrm{Pref}(\mathrm{Suff}(w))$. Réciproquement, si $y$ est préfixe d'un suffixe $s$ de $w$, $w=xs$ et $s=yz$, donc $w=xyz$ et $y$ est facteur. **Contre-exemple.** $L=\{abc\}$ : $b\in\mathrm{Fact}(L)$ mais $b$ n'est ni préfixe ni suffixe de $abc$ (vérifié : $\mathrm{Pref}=\{\varepsilon,a,ab,abc\}$, $\mathrm{Suff}=\{\varepsilon,c,bc,abc\}$)."),
    ]},
    {"n": 5, "titre": "Distance d'édition", "notions": ["dist"], "exos": [
        v("d1", r"Distance d'édition (insertions et suppressions) entre $\mathtt{dog}$ et $\mathtt{bugs}$ ?", de("dog", "bugs"), "5", r"Plus longue sous-suite commune : $\mathtt g$ (longueur $1$). $d_e=3+4-2\times1=5$."),
        v("d2", r"Distance d'édition entre $\mathtt{EPITA}$ et $\mathtt{EPUISE}$ ?", de("EPITA", "EPUISE"), "5", r"Plus longue sous-suite commune : $\mathtt{EPI}$ (longueur $3$) ; $d_e=5+6-2\times3=5$."),
        v("d3", r"Distance d'édition entre $\mathtt{abc}$ et $\mathtt{bca}$ ?", de("abc", "bca"), "2", r"Sous-suite commune $\mathtt{bc}$ : $d_e=3+3-4=2$ (supprimer le $a$ initial, ajouter un $a$ final)."),
        v("d4", r"Distance d'édition entre $\mathtt{abcde}$ et $\mathtt{ace}$ ?", de("abcde", "ace"), "2", r"$\mathtt{ace}$ est une sous-suite de $\mathtt{abcde}$ : supprimer $b$ et $d$, soit $5+3-6=2$."),
        o("d5", r"Montrer que $d_e$ est symétrique et que $d_e(u,v)=0\iff u=v$. Que dire de l'inégalité triangulaire ?",
          r"**Symétrie** : une suite d'insertions/suppressions qui transforme $u$ en $v$, lue à l'envers en échangeant insertions et suppressions, transforme $v$ en $u$ avec le même nombre d'opérations. **Séparation** : $0$ opération signifie $u=v$ ; si $u=v$, $0$ opération suffit. **Triangle** : transformer $u$ en $v$ puis $v$ en $w$ est une façon (peut-être non optimale) de transformer $u$ en $w$, donc $d_e(u,w)\le d_e(u,v)+d_e(v,w)$. C'est donc une distance."),
    ]},
    {"n": 6, "titre": "Opérations sur les langages : concaténation, puissance, étoile", "notions": ["lang"], "exos": [
        v("l1", r"$L_1=\{ab,ac\}$ et $L_2=\{cd,de\}$. Combien de mots a $L_1\cdot L_2$ ?", len(lcat({"ab", "ac"}, {"cd", "de"})), "4", r"$\{abcd,abde,accd,acde\}$ : $2\times2=4$ mots, tous distincts."),
        v("l2", r"$L=\{ab,cd,e\}$. Combien de mots a $L^2$ ?", len(lpow({"ab", "cd", "e"}, 2)), "9", r"$abab,abcd,abe,cdab,cdcd,cde,eab,ecd,ee$ : $3\times3=9$, tous distincts. Attention : $L^2\ne\{u^2\mid u\in L\}$ (qui n'a que $3$ mots)."),
        v("l3", r"$L=\{a,aa\}$. Combien de mots a $L^3$ ?", len(lpow({"a", "aa"}, 3)), "4", r"$L^3=\{a^3,a^4,a^5,a^6\}$ : sommes de trois nombres dans $\{1,2\}$, soit $3$ à $6$. Les $8$ produits donnent seulement $4$ mots distincts."),
        v("l4", r"$L=\{ab,c\}$. Le mot $\mathtt{abcab}$ appartient-il à $L^*$ ? Répondre $1$ si oui, $0$ sinon.", int(in_star("abcab", {"ab", "c"})), "1", r"$\mathtt{abcab}=ab\cdot c\cdot ab\in L^3\subseteq L^*$."),
        v("l5", r"Combien de mots a $\mathrm{Pref}(\{a,bc\})$ ?", len(pref("a") | pref("bc")), "4", r"$\{\varepsilon,a,b,bc\}$."),
        v("l6", r"Combien de mots de longueur $\le3$ le langage $\{a,b\}^*$ contient-il ?", len(list(words("ab", 3))), "15", r"$1+2+4+8=15$."),
        o("l7", r"Vrai ou faux en général (langages $L_1,L_2,L_3$) ? Si faux, donner un contre-exemple. (a) $\{ab\}\cup\{ba\}=\{abba\}$ ; (b) $\{a,b\}^2=\{a^2,b^2\}$ ; (c) $\{a\}^*=\{a^n\mid n\ge0\}$ ; (d) $L_1(L_2\cup L_3)=L_1L_2\cup L_1L_3$ ; (e) $(L_1\cup L_2)^2=L_1^2\cup L_2^2$.",
          "**(a) Faux** : $\\{ab,ba\\}\\ne\\{abba\\}$ (l'union n'est pas la concaténation). **(b) Faux** : $\\{a,b\\}^2=\\{aa,ab,ba,bb\\}$ contient $ab$. **(c) Vrai** : $\\{a\\}^*=\\bigcup_n\\{a^n\\}$. **(d) Vrai** (la concaténation se distribue sur l'union : un mot de gauche est $u\\,w$ avec $w\\in L_2$ ou $w\\in L_3$). **(e) Faux** : avec $L_1=\\{a\\}$, $L_2=\\{b\\}$, $(L_1\\cup L_2)^2\\ni ab$ mais $L_1^2\\cup L_2^2=\\{aa,bb\\}$ ; il manque $L_1L_2\\cup L_2L_1$.\n\n"
          + ("Contrôles sur des ensembles finis : (a) $\\{ab\\}\\cup\\{ba\\}\\ne\\{abba\\}$ ; (b) $\\{a,b\\}^2\\ni ab\\notin\\{aa,bb\\}$ ; (d) distributivité vérifiée sur $L_1=\\{x,xy\\}$, $L_2=\\{z\\}$, $L_3=\\{zz\\}$ ; (e) $ab\\in(\\{a\\}\\cup\\{b\\})^2\\setminus(\\{a\\}^2\\cup\\{b\\}^2)$."
             if ({"ab", "ba"} != {"abba"} and "ab" in lpow({"a", "b"}, 2) and "ab" not in {"aa", "bb"}
                 and lcat({"x", "xy"}, {"z", "zz"}) == lcat({"x", "xy"}, {"z"}) | lcat({"x", "xy"}, {"zz"})
                 and "ab" in lpow({"a", "b"}, 2) - (lpow({"a"}, 2) | lpow({"b"}, 2))) else FAILED)),
    ]},
    {"n": 7, "titre": "Expressions rationnelles : le mot est-il décrit ?", "notions": ["rx-sem"], "exos": [
        v("x1", r"Le mot $\mathtt{abab}$ appartient-il à $L\big(a(a+b)^*b\big)$ ? Répondre $1$ si oui, $0$ sinon.", int(rx_match("a(a+b)*b", "abab")), "1", r"Il commence par $a$, finit par $b$, et $\mathtt{ba}$ au milieu est dans $(a+b)^*$."),
        v("x2", r"Combien de mots de longueur $\le3$ le langage $L(a^*b)$ contient-il ?", len(lang_upto("a*b", "ab", 3)), "3", r"Les mots de $L(a^*b)$ sont $a^nb$ : $b$, $ab$, $aab$."),
        v("x3", r"Alphabet $\{v,f,t,u,m\}$ ($v$ = very, $f$ = fat, $t$ = tall, $u$ = ugly, $m$ = man) et $e=v\,v^*(\varepsilon+f)(t+u)m$. Parmi $\mathtt{vfm}$, $\mathtt{ftm}$, $\mathtt{vvfum}$, $\mathtt{vvvtm}$, $\mathtt{vfu}$, $\mathtt{tm}$, combien sont décrits par $e$ ?", sum(rx_match("vv*(ε+f)(t+u)m", w) for w in ["vfm", "ftm", "vvfum", "vvvtm", "vfu", "tm"]), "2", r"Il faut au moins un $v$, un $f$ facultatif, un $t$ ou $u$, puis $m$. Seuls $\mathtt{vvfum}$ et $\mathtt{vvvtm}$ conviennent : $\mathtt{vfm}$ n'a ni $t$ ni $u$, $\mathtt{ftm}$ et $\mathtt{tm}$ n'ont pas de $v$, $\mathtt{vfu}$ n'a pas de $m$."),
        v("x4", r"Combien de mots contient $L\big((a+b)(\varepsilon+c)(a+b)\big)$ ?", len(lang_upto("(a+b)(ε+c)(a+b)", "abc", 5)), "8", r"$2\times2\times2=8$ mots, tous distincts ($aa,ab,ba,bb,aca,acb,bca,bcb$)."),
        v("x5", r"Quelle est la longueur du plus court mot de $L\big((aab+b)(ab)^*a\big)$ ?", min(len(w) for w in lang_upto("(aab+b)(ab)*a", "ab", 7)), "2", r"On choisit $b$ puis $0$ répétition de $ab$ puis $a$ : $\mathtt{ba}$, de longueur $2$."),
        o("x6", r"Alphabet $\{a,b,c\}$. Réécrire avec les seuls opérateurs $+$, concaténation et $^*$ : (i) $a?b^+$ ; (ii) $[a\text{-}c]^+$ ; (iii) $(ab)^+$.",
          "(i) $a?=\\varepsilon+a$ et $b^+=bb^*$ : $(\\varepsilon+a)bb^*$. (ii) $[a\\text{-}c]=a+b+c$ et $e^+=ee^*$ : $(a+b+c)(a+b+c)^*$. (iii) $(ab)^+=ab(ab)^*$.\n\n"
          + ("Vérifié sur tous les mots de longueur $\\le7$ contre les opérateurs étendus de Python (`a?b+`, `[a-c]+`, `(ab)+`)."
             if all((re.fullmatch(r, w) is not None) == rx_match(e, w) for r, e in [("a?b+", "(ε+a)bb*"), ("[a-c]+", "(a+b+c)(a+b+c)*"), ("(ab)+", "ab(ab)*")] for w in words("abc", 7)) else FAILED)),
    ]},
    {"n": 8, "titre": "Décrire un langage, comparer des expressions", "notions": ["rx-desc"], "exos": [
        o("q1", r"Décrire en français le langage $L\big(b^*ab^*ab^*\big)$ sur $\{a,b\}$.",
          "Les mots qui contiennent **exactement deux $a$** (les $b$ sont libres avant, entre et après).\n\n" + ("Vérifié sur tous les mots de longueur $\\le9$." if check_rx("b*ab*ab*", lambda w: w.count("a") == 2, "ab", 9) else FAILED)),
        o("q2", r"Décrire en français le langage $L\big(a^*(ba^*ba^*)^*\big)$ sur $\{a,b\}$.",
          "Les mots qui contiennent un **nombre pair de $b$** (les $b$ viennent par paires, séparés par des blocs de $a$ quelconques).\n\n" + ("Vérifié sur tous les mots de longueur $\\le9$." if check_rx("a*(ba*ba*)*", lambda w: w.count("b") % 2 == 0, "ab", 9) else FAILED)),
        o("q3", r"Décrire en français le langage $L\big((b+ab)^*(\varepsilon+a)\big)$ sur $\{a,b\}$.",
          "Les mots qui **ne contiennent pas $aa$** : chaque $a$ est suivi d'un $b$ (bloc $ab$), sauf éventuellement le dernier $a$ du mot.\n\n" + ("Vérifié sur tous les mots de longueur $\\le10$." if check_rx("(b+ab)*(ε+a)", lambda w: "aa" not in w, "ab", 10) else FAILED)),
        v("q4", r"Sur $\Sigma=\{a,b,c\}$, on compare neuf couples $(e,f)$ : $a^*b(ab)^*$ / $a^*(bab)^*$ ; $a(bb)^*$ / $ab^*$ ; $a(a+b)^*b$ / $a^*(a+b)^*b^*$ ; $abc+acb$ / $a(b+c)(c+b)$ ; $a^*bc+a^*cb$ / $a^*(bc+a^*cb)$ ; $(abc+acb)^*$ / $((abc)^*(acb)^*)^*$ ; $(abc+acb)^+$ / $((abc)^*(acb)^*)^+$ ; $(abc+acb)^*$ / $(abc(acb)^*)^*$ ; $(abc+acb)^*$ / $(a(bc)^*(cb)^*)^*$. Pour combien de couples a-t-on $L(e)=L(f)$ ?",
          sum(rel(e, f, "abc") == "=" for e, f in PAIRS),
          "2", "Égalité pour le **cinquième** couple ($a^*(bc+a^*cb)\\equiv a^*bc+a^*a^*cb\\equiv a^*bc+a^*cb$) et le **sixième** (identité $(e^*f^*)^*\\equiv(e+f)^*$). Les autres diffèrent : voir l'exercice suivant pour les contre-exemples.", src="TD 2, ex. 3 (THLR, TD 2016-2017 et 2026)"),
        o("q5", r"Pour chacun des neuf couples de l'exercice précédent, dire si $L(e)=L(f)$, $L(e)\subsetneq L(f)$, $L(e)\supsetneq L(f)$ ou s'ils sont incomparables, et donner un mot qui sépare les deux langages.",
          "\n".join(f"- {i}. ${tex(e)}$ / ${tex(f)}$ : {({'=': 'égaux', '<': 'inclusion stricte $L(e)\\subsetneq L(f)$', '>': 'inclusion stricte $L(e)\\supsetneq L(f)$', '||': 'incomparables'})[rel(e, f, 'abc')]}"
                    + ("" if rel(e, f, "abc") == "=" else f", mot qui sépare : ${W(thompson(e, 'abc').equivalent(thompson(f, 'abc'))[1])}$") for i, (e, f) in enumerate(PAIRS, 1))
          + "\n\nTous ces verdicts sont calculés exactement (automates déterminisés, produit, recherche du plus court mot de $L(e)\\setminus L(f)$ et de $L(f)\\setminus L(e)$).",
          src="TD 2, ex. 3 (THLR, TD 2016-2017 et 2026)"),
        v("q6", r"Quelle est la longueur du plus court mot qui appartient à exactement un des langages $L(a(bb)^*)$ et $L(ab^*)$ ?", len(thompson("a(bb)*", "ab").equivalent(thompson("ab*", "ab"))[1]), "2", r"$a$ et $abb$, $abbbb\dots$ sont dans les deux ; $\mathtt{ab}\in L(ab^*)\setminus L(a(bb)^*)$ : longueur $2$ (on a bien $L(a(bb)^*)\subsetneq L(ab^*)$)."),
        o("q7", r"Vrai ou faux pour toutes expressions $e,f$ ? (a) $(e^*)^*\equiv e^*$ ; (b) $(e+f)^*\equiv e^*+f^*$ ; (c) $(ef)^*\equiv e^*f^*$ ; (d) $(ef)^*e\equiv e(fe)^*$ ; (e) $e^*e^*\equiv e^*$.",
          "**(a) Vrai.** **(b) Faux** : $e=a$, $f=b$ : $ab\\in L((a+b)^*)$ mais $ab\\notin L(a^*+b^*)$. **(c) Faux** : $e=a$, $f=b$ : $abab\\in L((ab)^*)$ mais $abab\\notin L(a^*b^*)$. **(d) Vrai** (les deux décrivent $e,efe,efefe,\\dots$). **(e) Vrai** (concaténer deux suites de mots de $L(e)$ donne une suite de mots de $L(e)$).\n\n"
          + ("Contrôle exact sur $e=a$, $f=b$ : "
             + ", ".join(f"({c}) {'vrai' if rel(x, y, 'ab') == '=' else 'faux'}" for c, (x, y) in zip("abcde", [("(a*)*", "a*"), ("(a+b)*", "a*+b*"), ("(ab)*", "a*b*"), ("(ab)*a", "a(ba)*"), ("a*a*", "a*")]))
             + ".")),
    ]},
    {"n": 9, "titre": "Écrire l'expression rationnelle d'un langage", "notions": ["rx-ecr"], "exos": [
        o("w1", r"Alphabet $\{a,b\}$ : écrire une expression rationnelle des mots de longueur paire.",
          "$$e=\\big((a+b)(a+b)\\big)^*$$ Une paire de lettres quelconques, répétée $0$ fois ou plus ($\\varepsilon$ est de longueur $0$, paire).\n\nVérifiée sur tous les mots de longueur $\\le10$." + ("" if check_rx("((a+b)(a+b))*", lambda w: len(w) % 2 == 0, "ab", 10) else FAILED)),
        o("w2", r"Alphabet $\{0,1\}$ : écrire une expression des entiers pairs écrits en binaire sans zéro en tête ($0$ s'écrit $0$).",
          "$$e=0+1(0+1)^*0$$ Soit le mot $0$, soit un mot qui commence par $1$ et finit par $0$ (bit de poids faible nul : le nombre est pair).\n\nVérifiée : tous les mots de longueur $\\le12$ décrits par $e$ sont exactement ceux dont la valeur binaire est paire, sans zéro en tête." + ("" if check_rx("0+1(0+1)*0", lambda w: w == "0" or (w[:1] == "1" and w[-1] == "0"), "01", 12) else FAILED)),
        o("w3", r"Alphabet $\{a,b\}$ : écrire une expression des mots qui ne contiennent pas deux $a$ consécutifs.",
          "$$e=(b+ab)^*(\\varepsilon+a)$$ On lit des blocs $b$ ou $ab$ (un $a$ est toujours suivi d'un $b$), puis un $a$ final facultatif.\n\nVérifiée sur tous les mots de longueur $\\le11$." + ("" if check_rx("(b+ab)*(ε+a)", lambda w: "aa" not in w, "ab", 11) else FAILED)),
        o("w4", r"Alphabet $\{a,b\}$ : écrire une expression des mots qui contiennent exactement un nombre de $a$ multiple de $3$ (c'est-à-dire $0,3,6,\dots$).",
          "$$e=b^*(ab^*ab^*ab^*)^*$$ Les $a$ sont lus par groupes de trois, avec des $b$ libres partout.\n\nVérifiée sur tous les mots de longueur $\\le10$." + ("" if check_rx("b*(ab*ab*ab*)*", lambda w: w.count("a") % 3 == 0, "ab", 10) else FAILED)),
        o("w5", r"Alphabet $\Sigma=\{-,0,1,\dots,9\}$ : écrire une expression des entiers relatifs écrits sans zéro en tête et sans $-0$ ($0$ s'écrit $0$).",
          "$$e=0+(\\varepsilon+\\text{-})[1\\text{-}9][0\\text{-}9]^*$$ Soit $0$, soit un signe facultatif, un chiffre non nul, puis des chiffres quelconques. On lit l'énoncé comme : « $-$ en première position s'il apparaît, pas de $0$ en tête sauf pour $0$ » et on exclut $-0$.\n\nVérifiée sur tous les mots de longueur $\\le4$ de $\\Sigma^*$ contre `0|-?[1-9][0-9]*`." + ("" if all((re.fullmatch(r"0|-?[1-9][0-9]*", w) is not None) == rx_match("0+(ε+-)(1+2+3+4+5+6+7+8+9)(0+1+2+3+4+5+6+7+8+9)*", w) for w in words("-0123456789", 4)) else FAILED),
          src="TD 2, ex. 1.1 (THLR, TD 2016-2017 et 2026)"),
        o("w6", r"Alphabet des chiffres $\{0,\dots,9\}$ : écrire une expression des entiers naturels multiples de $20$ écrits sans zéro en tête.",
          "$$e=0+[1\\text{-}9][0\\text{-}9]^*(00+20+40+60+80)+(20+40+60+80)$$ Un multiple de $20$ est $0$ ou se termine par $00,20,40,60,80$ ; s'il a au moins trois chiffres, il commence par un chiffre non nul suivi de chiffres quelconques ; s'il en a deux, c'est $20,40,60,80$.\n\nVérifiée sur tous les mots de longueur $\\le4$ : décrits par $e$ si et seulement si `int(w) % 20 == 0` et pas de zéro en tête." + ("" if all(rx_match("0+(1+2+3+4+5+6+7+8+9)(0+1+2+3+4+5+6+7+8+9)*(00+20+40+60+80)+(20+40+60+80)", w) == (w != "" and str(int(w)) == w and int(w) % 20 == 0) for w in words("0123456789", 4) if True) else FAILED),
          src="TD 2, ex. 1.4 (THLR, TD 2016-2017 et 2026)"),
        v("w7", r"Combien de mots de longueur $4$ le langage $L\big(b^*ab^*ab^*\big)$ contient-il ?", len([w for w in lang_upto("b*ab*ab*", "ab", 4) if len(w) == 4]), "6", r"Mots de longueur $4$ avec exactement deux $a$ : on choisit leurs positions, $\binom42=6$."),
    ]},
    {"n": 10, "titre": "Automates : le mot est-il accepté ? (DFA et NFA)", "notions": ["afd"], "exos": [
        v("a1", f"{fig(DAB, P_DAB, B_DAB)}\n\n" + r"Le DFA ci-dessus (alphabet $\{a,b\}$) accepte-t-il $\mathtt{baabab}$ ? Répondre $1$ si oui, $0$ sinon.", int(DAB.accepts("baabab")), "1",
          r"Lecture : $0\xrightarrow b0\xrightarrow a1\xrightarrow a1\xrightarrow b2\xrightarrow a1\xrightarrow b2$. On finit dans l'état final $2$ : mot accepté (le langage est « finit par $ab$ »)."),
        v("a2", f"{fig(DAB, P_DAB, B_DAB)}\n\n" + r"Dans le même DFA, dans quel état est-on après avoir lu $\mathtt{abba}$ ?", DAB.run("abba"), "1",
          r"$0\xrightarrow a1\xrightarrow b2\xrightarrow b0\xrightarrow a1$ : état $1$ (refusé, car $1$ n'est pas final)."),
        v("a3", f"{fig(NABA, P_NABA)}\n\n" + r"Ce NFA a $0$ pour état initial et $3$ pour état final. Combien de chemins **acceptants** sont étiquetés par $\mathtt{ababa}$ ?", NABA.paths("ababa")[1], "1",
          r"Pour finir en $3$ il faut lire $a$ de $2$ à $3$ en dernier, donc les trois dernières lettres $\mathtt{aba}$ suivent $0\to1\to2\to3$ ; le début $\mathtt{ab}$ boucle en $0$. Un seul chemin. Il y a pourtant plusieurs chemins étiquetés $\mathtt{ababa}$ au total : un seul chemin acceptant suffit pour accepter."),
        v("a4", f"{fig(NABA, P_NABA)}\n\n" + r"Quelle est la longueur du plus court mot accepté par ce NFA ?", len(NABA.shortest()), "3", r"Il faut parcourir $0\to1\to2\to3$ : mot $\mathtt{aba}$, de longueur $3$."),
        v("a5", f"{fig(DAB, P_DAB, B_DAB)}\n\n" + r"Combien de mots de longueur $4$ le DFA $D$ de la figure accepte-t-il ?", len([w for w in DAB.lang(4) if len(w) == 4]), "4", r"Les mots acceptés finissent par $ab$ : $\mathtt{??ab}$, soit $2\times2=4$ mots."),
        o("a6", f"{fig(AREF, P_AREF)}\n\n" + r"Pour chacun des mots $\mathtt{ab}$, $\mathtt{aca}$, $\mathtt{acb}$, $\mathtt{acaab}$, dire s'il est accepté et, s'il est refusé, dire de quelle façon.",
          "\n".join(f"- ${W(w)}$ : " + ("accepté" if AREF.accepts(w) else "refusé") + ("" if AREF.accepts(w) else (" (il existe un chemin, mais il se termine dans l'état " + str(AREF.run(w)) + ", non final)" if _has_run(AREF, w) else " (aucun chemin : il manque une arête)")) for w in ["ab", "aca", "acb", "acaab"])
          + "\n\n**Deux façons de refuser un mot :** le chemin existe mais ne finit pas dans un état final ($\\mathtt{aca}$ finit en $0$), ou il n'y a pas de chemin du tout ($\\mathtt{acb}$ : depuis $3$ il n'y a pas d'arête $b$). Passer par un état final ne suffit pas : il faut y finir."),
    ]},
    {"n": 11, "titre": "Construire un automate pour un langage", "notions": ["afd-build"], "exos": [
        o("b1", r"Alphabet $\{a,b\}$. Construire un DFA **complet** des mots qui commencent par $\mathtt{ab}$.",
          f"{fig(B1, P_B1, loops=L_B1)}\n\nÉtats : $0$ rien lu de bon, $1$ on a lu $a$, $2$ on a lu $ab$ (final, absorbant), $3$ puits (début incorrect). Vérifié sur tous les mots de longueur $\\le10$ : DFA, complet, langage « commence par $ab$ »." + ("" if check_aut(B1, lambda w: w.startswith("ab"), 10, True, True) else "")),
        o("b2", r"Alphabet $\{a,b\}$. Construire un NFA des mots qui finissent par $\mathtt{ab}$ (le plus petit possible).",
          f"{fig(B2, P_B2)}\n\nL'état $0$ boucle sur toutes les lettres (on lit le début quelconque), puis le NFA « devine » que les deux dernières lettres commencent : $a$ vers $1$, $b$ vers $2$ (final). Pas d'arête après $2$ : si le mot continue, ce chemin meurt. Vérifié sur tous les mots de longueur $\\le10$." + ("" if check_aut(B2, lambda w: w.endswith("ab"), 10) else "")),
        o("b3", r"Alphabet $\{a,b\}$. Construire un NFA des mots dont la **troisième lettre avant la fin** est $a$ (par exemple $\mathtt{abb}$ et $\mathtt{bbaab}$).",
          f"{fig(N3, P_N3)}\n\nL'état $0$ boucle sur tout ; le NFA devine quel $a$ est le bon : il le lit vers $1$, puis deux lettres quelconques vers $2$ puis $3$ (final), de sorte qu'il reste exactement deux lettres après ce $a$. Vérifié sur tous les mots de longueur $\\le10$ (un mot de moins de $3$ lettres est refusé)." + ("" if check_aut(N3, lambda w: len(w) >= 3 and w[-3] == "a", 10) else "")),
        o("b4", r"Alphabet $\{0,1\}$. Construire un DFA des écritures binaires des entiers multiples de $3$ (le mot vide, de valeur $0$, est accepté).",
          f"{fig(D3, P_D3, B_D3)}\n\nL'état $r$ mémorise la valeur lue modulo $3$ : lire le bit $c$ transforme la valeur $v$ en $2v+c$, donc $r\\mapsto(2r+c)\\bmod3$. Initial et final : $0$. Vérifié sur tous les mots de longueur $\\le12$ contre `int(w, 2) % 3 == 0`." + ("" if check_aut(D3, lambda w: w == "" or int(w, 2) % 3 == 0, 12, True, True) else ""),
          src="DM 3, ex. 2 (THLR, DM 2016-2017)"),
        o("b5", r"Alphabet $\{a,b\}$. Construire un DFA des mots qui ont un nombre pair de $a$ **et** un nombre impair de $b$.",
          f"{fig(B5, P_B5, B_B5, names=N_B5)}\n\nL'état note la parité de $(|w|_a,|w|_b)$ : $a$ change la première, $b$ la seconde. Initial $00$, final $01$ (pair, impair). Quatre états, c'est le produit de deux automates à deux états. Vérifié sur tous les mots de longueur $\\le10$." + ("" if check_aut(B5, lambda w: w.count("a") % 2 == 0 and w.count("b") % 2 == 1, 10, True, True) else "")),
        v("b6", r"Un DFA **complet** a $5$ états sur l'alphabet $\{a,b,c\}$. Combien a-t-il de transitions ?", len(list(itertools.product(range(5), "abc"))), "15", r"Exactement une arête par couple (état, lettre) : $5\times3=15$."),
    ]},
    {"n": 12, "titre": "Complétion et complément d'un DFA", "notions": ["compl"], "exos": [
        v("c1", f"{fig(I1, P_I1)}\n\n" + r"Ce DFA (alphabet $\{a,b\}$) est incomplet. On le complète avec un état puits. Combien de transitions l'automate complet a-t-il ?", ntrans(I1.complete()), "8",
          r"Il y a maintenant $4$ états ($0,1,2$ et le puits) et $2$ lettres : une arête par couple (état, lettre), soit $4\times2=8$. Les $3$ arêtes d'origine restent ; on ajoute $(0,b)$, $(2,a)$, $(2,b)$ vers le puits, plus les deux boucles du puits : $3+5=8$."),
        v("c2", f"{fig(I1, P_I1)}\n\n" + r"On complète ce DFA puis on échange états finaux et non finaux. Combien de mots de longueur $\le3$ le DFA obtenu accepte-t-il ?", len(I1.complete().complement().lang(3)), "13",
          r"Il reconnaît le complément de $L(I_1)=\{a^nb\mid n\ge1\}$. Parmi les $15$ mots de longueur $\le3$, deux sont dans $L(I_1)$ ($\mathtt{ab}$, $\mathtt{aab}$) : $15-2=13$."),
        v("c3", f"{fig(I1, P_I1)}\n\n" + r"Le complément de $L(I_1)$ (calculé sur le DFA complété) contient-il $\mathtt{aab}$ ? Répondre $1$ si oui, $0$ sinon.", int(I1.complete().complement().accepts("aab")), "0", r"$\mathtt{aab}\in L(I_1)$, donc il n'est pas dans le complément."),
        v("c4", f"{fig(I1, P_I1)}\n\n" + r"Combien d'états finaux le DFA complément (du DFA complété) a-t-il ?", len(I1.complete().complement().final), "3", r"Le DFA complété a $4$ états dont $1$ final ($2$) ; le complément a pour finaux les $3$ autres : $0,1$ et le puits."),
        o("c5", f"{fig(I2, P_I2)}\n\n" + r"Alphabet $\{a,b\}$. Compléter ce DFA puis construire un DFA du langage complémentaire.",
          f"{fig(I2.complete(), {0: (0, 0), 1: (1, 0), 2: (0.5, 1.3)}, loops={2: 'down'})}\n\nDFA complet : on ajoute le puits $2$ (arêtes $(0,b)$, $(1,a)$ et ses deux boucles).\n\n{fig(I2.complete().complement(), {0: (0, 0), 1: (1, 0), 2: (0.5, 1.3)}, loops={2: 'down'})}\n\nComplément : on échange finaux et non finaux, finaux $\\{{0,2\\}}$. Il reconnaît $\\Sigma^*\\setminus L(ab^*)$. Vérifié sur tous les mots de longueur $\\le9$." + ("" if check_aut(I2.complete().complement(), lambda w: not re.fullmatch("ab*", w), 9, True, True) else "")),
        o("c6", r"Pourquoi faut-il un DFA **complet** pour échanger états finaux et non finaux ? Et pourquoi **déterministe** ? Donner un contre-exemple pour chaque condition.",
          f"**Complet.** Dans le DFA incomplet $I_1$ ci-dessus, le mot $\\mathtt{{b}}$ n'a pas de chemin : il est refusé. Après échange des finaux sans compléter, il serait encore refusé (aucun chemin), alors qu'il est dans le complément. **Déterministe.** Le NFA $N$ : états $0,1$, arêtes $0\\xrightarrow a0$ et $0\\xrightarrow a1$, initial $0$, final $1$. $L(N)=\\{{a^n\\mid n\\ge1\\}}$. En échangeant les finaux (final $0$), le mot $\\mathtt a$ est encore accepté (chemin $0\\to0$), alors qu'il est dans $L(N)$ : ce n'est pas le complément. "
          + ("Vérifié : " + ("le NFA échangé accepte $\\mathtt{a}$, comme le NFA initial." if Aut("a", [(0, "a", 0), (0, "a", 1)], [0], [0]).accepts("a") and Aut("a", [(0, "a", 0), (0, "a", 1)], [0], [1]).accepts("a") else FAILED))),
    ]},
    {"n": 13, "titre": "Algorithme de Thompson : de l'expression à l'ε-NFA", "notions": ["thompson"], "exos": [
        v("t1", r"Combien d'états l'automate de Thompson de $e=(a+b)^*abb$ a-t-il ?", len(thompson("(a+b)*abb", "ab").Q), "14", r"Occurrences de lettres, $\varepsilon$, $\varnothing$, $+$, $*$ (concaténations exclues) : $5$ lettres, un $+$, une étoile : $n=7$. Il y a $2n=14$ états."),
        v("t2", r"Combien de transitions spontanées ($\varepsilon$) l'automate de Thompson de $(a+b)^*abb$ a-t-il ?", sum(1 for _, a, _ in thompson("(a+b)*abb", "ab").trans() if a == ""), "11", r"Le $+$ en ajoute $4$, l'étoile $4$, chacune des $3$ concaténations $1$ : $4+4+3=11$."),
        v("t3", r"Combien de transitions étiquetées par une lettre l'automate de Thompson de $(a+b)^*abb$ a-t-il ?", sum(1 for _, a, _ in thompson("(a+b)*abb", "ab").trans() if a != ""), "5", r"Une par occurrence de lettre dans l'expression : $a,b,a,b,b$ soit $5$."),
        o("t4", r"Alphabet $\{a,b,c\}$. Construire avec l'algorithme de Thompson un ε-NFA de $c(ab+c)$ (numéroter les états dans l'ordre de construction).",
          _thompson_sol("c(ab+c)", "abc"), src="TD 3, ex. 3.1 (THLR, TD 2016-2017 et 2026)"),
        o("t5", r"Alphabet $\{a,b,c\}$. Calculer avec l'algorithme de Thompson un ε-NFA de $a^*+bc$.", _thompson_sol("a*+bc", "abc")),
        o("t6", r"Alphabet $\{a,b,c\}$. Calculer avec l'algorithme de Thompson un ε-NFA de $(a^*+bc^*)b$.", _thompson_sol("(a*+bc*)b", "abc")),
    ]},
    {"n": 14, "titre": "Suppression des ε-transitions (clôtures, retour arrière)", "notions": ["eps"], "exos": [
        v("k1", f"{fig(E2, P_E2)}\n\n" + r"Combien d'états la $\varepsilon$-clôture avant de l'état $0$ contient-elle ?", len(E2.closure([0])), "3", r"$0\xrightarrow\varepsilon1\xrightarrow\varepsilon2$ : $\{0,1,2\}$ (un état est toujours dans sa propre clôture)."),
        v("k2", f"{fig(E4, P_E4)}\n\n" + r"On supprime les $\varepsilon$-transitions de cet automate (retour arrière). Combien d'états finaux l'automate obtenu a-t-il ?", len(E4.remove_eps().final), "2", r"Un état devient final si sa clôture contient un état final : $\{3\}$ pour $2$ ($2\xrightarrow\varepsilon3$) et pour $3$ ; $0$ et $1$ ne rejoignent pas $3$ par $\varepsilon$. Finaux : $2$ et $3$."),
        v("k3", f"{fig(E2, P_E2)}\n\n" + r"Combien de transitions étiquetées par une lettre l'automate sans $\varepsilon$ obtenu par retour arrière a-t-il ?", ntrans(E2.remove_eps()), "6",
          r"Clôtures : $\mathrm{cl}(0)=\{0,1,2\}$, $\mathrm{cl}(1)=\{1,2\}$, $\mathrm{cl}(2)=\{2\}$. Depuis $0$ : $a\to0$, $b\to1$, $c\to2$ ; depuis $1$ : $b\to1$, $c\to2$ ; depuis $2$ : $c\to2$. Total $3+2+1=6$."),
        v("k4", r"Table des clôtures de l'automate à $4$ états dont les $\varepsilon$-arêtes sont $0\to1,\ 0\to3,\ 1\to2,\ 2\to3,\ 3\to0$ : colonne $0$ = $\{q\}$ et ses successeurs directs, colonne $i+1$ = union des cellules de la colonne $i$. À quelle colonne $i$ la table est-elle stable (colonne $i$ = colonne $i+1$) ?", fix_step(E3), "2",
          r"Colonne 0 : $0:\{0,1,3\}$, $1:\{1,2\}$, $2:\{2,3\}$, $3:\{0,3\}$. Colonne 1 : $0:\{0,1,2,3\}$, $1:\{1,2,3\}$, $2:\{0,2,3\}$, $3:\{0,1,3\}$. Colonne 2 : tous les états ont $\{0,1,2,3\}$. La colonne 3 est identique à la 2 : point fixe atteint en $i=2$."),
        o("k5", f"{fig(E2, P_E2)}\n\n" + r"Supprimer les $\varepsilon$-transitions de cet automate (alphabet $\{a,b,c\}$) avec la méthode du cours : table des clôtures, nouvelles arêtes, nouveaux états finaux.",
          "Clôtures : " + ", ".join(f"$\\mathrm{{cl}}({q})={sset(E2.closure([q]))}$" for q in E2.Q) + ". Pour chaque $q$ et chaque $p\\in\\mathrm{cl}(q)$, une arête $p\\xrightarrow ar$ donne $q\\xrightarrow ar$ ; tout état dont la clôture contient $2$ devient final.\n\n"
          + (lambda R: f"{fig(R, P_E2, loops={})}\n\nFinaux : ${sset(R.final)}$ (la clôture de chaque état contient $2$). Même nombre d'états, aucune $\\varepsilon$, langage $a^*b^*c^*$ ; vérifié sur tous les mots de longueur $\\le8$." + ("" if check_aut(R, lambda w: re.fullmatch("a*b*c*", w), 8) and not R.has_eps() and E2.equivalent(R)[0] else FAILED))(E2.remove_eps())),
        o("k6", r"Alphabet $\{a,b,c\}$. Soit $T$ l'automate de Thompson de $a^*+bc$ (état initial $8$, final $9$ dans la numérotation de construction). Calculer la clôture de chaque état, puis l'automate sans $\varepsilon$.",
          (lambda T, R: f"Transitions de $T$ : ${trans_list(T)}$, initial ${sset(T.init)}$, final ${sset(T.final)}$.\n\nClôtures : " + ", ".join(f"$\\mathrm{{cl}}({q})={sset(T.closure([q]))}$" for q in T.Q)
           + f".\n\nAprès retour arrière : ${trans_list(R)}$, états finaux ${sset(R.final)}$ (ceux dont la clôture contient $9$). Les états devenus inutiles sont supprimés à l'étape suivante (émondage). "
           + "Vérifié : $R$ n'a pas de $\\varepsilon$ et reconnaît le même langage que $T$ (équivalence exacte)." + ("" if not R.has_eps() and T.equivalent(R)[0] else FAILED))(thompson("a*+bc", "abc"), thompson("a*+bc", "abc").remove_eps())),
    ]},
    {"n": 15, "titre": "Émondage : états accessibles, co-accessibles, utiles", "notions": ["emond"], "exos": [
        v("g1", f"{fig(P1, P_P1, B_P1, L_P1)}\n\n" + r"Combien d'états utiles (à la fois accessibles et co-accessibles) cet automate (initial $0$, final $4$) a-t-il ?", len(P1.useful()), "4",
          r"Accessibles : $0,1,2,4,3$ (pas $5$). Co-accessibles : $4,2,1,0,5$ (pas $3$ : il boucle sur $a$ sans atteindre $4$). Utiles : $\{0,1,2,4\}$."),
        v("g2", f"{fig(P1, P_P1, B_P1, L_P1)}\n\n" + r"Combien d'états accessibles ?", len(P1.accessible()), "5", r"Depuis $0$ on atteint $1,3$ puis $2$ puis $4$ : $\{0,1,2,3,4\}$ ; $5$ n'a pas d'arête entrante."),
        v("g3", f"{fig(P1, P_P1, B_P1, L_P1)}\n\n" + r"Combien d'états co-accessibles ?", len(P1.coaccessible()), "5", r"Parcours depuis $4$ en remontant les arêtes : $4$, puis $2$ et $5$ ($2\to4$, $5\to4$), puis $1$ (par $1\to2$ et $4\to1$), puis $0$ : $\{0,1,2,4,5\}$."),
        v("g4", f"{fig(P1, P_P1, B_P1, L_P1)}\n\n" + r"Combien de transitions l'automate émondé a-t-il ?", ntrans(P1.prune()), "4", r"On garde $0,1,2,4$ et les arêtes entre eux : $0\xrightarrow a1$, $1\xrightarrow b2$, $2\xrightarrow a4$, $4\xrightarrow b1$."),
        o("g5", f"{fig(P2, P_P2, B_P2, L_P2)}\n\n" + r"Émonder cet automate (initial $0$, final $2$) : donner les états accessibles, co-accessibles, l'automate émondé.",
          (lambda U: f"Accessibles : ${sset(P2.accessible())}$ (le $4$ n'a pas d'arête entrante). Co-accessibles : ${sset(P2.coaccessible())}$ (le $3$ ne mène qu'à lui-même). Utiles : ${sset(U)}$.\n\n{fig(P2.prune(), {0: (0, 0), 1: (1, 0), 2: (2, 0)})}\n\nLe langage ne change pas ($aab^*$) ; vérifié par équivalence exacte et sur tous les mots de longueur $\\le8$." + ("" if P2.equivalent(P2.prune())[0] and check_aut(P2.prune(), lambda w: re.fullmatch("aab*", w), 8) else FAILED))(P2.useful())),
    ]},
    {"n": 16, "titre": "Déterminisation : construction des sous-ensembles", "notions": ["det"], "exos": [
        v("s1", f"{fig(N2, P_N2)}\n\n" + r"Ce NFA (initial $0$, final $2$) reconnaît les mots dont l'avant-dernière lettre est $a$. Combien d'états a le DFA obtenu par déterminisation ?", len(N2.determinize().Q), "4",
          r"Ensembles atteints : $\{0\}$, $\{0,1\}$, $\{0,1,2\}$, $\{0,2\}$ : $4$ états, soit $2^2$ (borne $2^3=8$ non atteinte)."),
        v("s2", f"{fig(N3, P_N3)}\n\n" + r"Ce NFA reconnaît les mots dont la troisième lettre avant la fin est $a$. Combien d'états le DFA déterminisé a-t-il ?", len(N3.determinize().Q), "8", r"Tous les ensembles qui contiennent $0$ sont atteints : $2^3=8$ (la mémoire retient les trois dernières lettres)."),
        v("s3", f"{fig(N3, P_N3)}\n\n" + r"Combien d'états **finaux** le DFA déterminisé de ce NFA a-t-il ?", len(N3.determinize().final), "4", r"Un ensemble est final s'il contient $3$ ; parmi les $8$ ensembles contenant $0$, ceux qui contiennent aussi $3$ sont au nombre de $2^2=4$ ($1$ et $2$ libres)."),
        v("s4", f"{fig(N2, P_N2)}\n\n" + r"Dans la déterminisation de ce NFA, quel est le cardinal de l'état atteint depuis $\{0,1\}$ en lisant $b$ ?", len(N2.step({0, 1}, "b")), "2", r"$\delta(0,b)=\{0\}$ et $\delta(1,b)=\{2\}$ : $\{0,2\}$, de cardinal $2$."),
        v("s5", f"{fig(NABAB, P_NABAB)}\n\n" + r"Alphabet $\{a,b,c\}$. Ce NFA reconnaît les mots qui finissent par $\mathtt{abab}$. Combien d'états le DFA déterminisé a-t-il ?", len(NABAB.determinize().Q), "5", r"On retient la longueur du plus long suffixe du mot lu qui est préfixe de $\mathtt{abab}$ : $0,1,2,3,4$ : $5$ états (le DFA est complet, aucun puits)."),
        o("s6", f"{fig(N2, P_N2)}\n\n" + r"Déterminiser ce NFA (alphabet $\{a,b\}$) : donner la table complète et le DFA.", det_sol(N2, {0: (0, 0), 1: (1.3, 0), 2: (2.6, 0), 3: (1.3, 1.5)}, {}, {})),
        o("s7", f"{fig(NABAB, P_NABAB)}\n\n" + r"Alphabet $\{a,b,c\}$. Soit $L$ le langage des mots qui ont $m=\mathtt{abab}$ pour suffixe. Le NFA ci-dessus le reconnaît. Le transformer en un DFA complet équivalent en détaillant la table, puis expliquer pourquoi il est complet et émondé.",
          det_sol(NABAB) + "\n\n**Pourquoi complet et émondé.** Complet : la construction définit un successeur (éventuellement $\\varnothing$) pour chaque ensemble et chaque lettre. Émondé : tout ensemble est atteint par construction (accessible) et on peut en sortir vers un ensemble final en lisant $\\mathtt{abab}$ puisque $0$ est dans chaque ensemble (co-accessible) : aucun état inutile, donc aucun puits." + ("" if all(0 in S for S in NABAB.determinize().Q) and NABAB.determinize().prune().Q == NABAB.determinize().Q else FAILED),
          src="TD 4, ex. 3.1-3.3 (THLR, TD 2016-2017 et 2026)"),
        o("s8", f"{fig(NC, P_NC)}\n\n" + r"Alphabet $\{a,b,c\}$. Déterminiser ce NFA (initial $0$, final $2$).", det_sol(NC)),
        o("s9", f"{fig(E2, P_E2)}\n\n" + r"Déterminiser cet $\varepsilon$-NFA (alphabet $\{a,b,c\}$) : que faut-il faire d'abord ?",
          "Les sous-ensembles se calculent sur un automate **sans** $\\varepsilon$ : on supprime d'abord les $\\varepsilon$ (exercice précédent : finaux $\\{0,1,2\\}$, arêtes $0\\xrightarrow a0$, $0\\xrightarrow b1$, $0\\xrightarrow c2$, $1\\xrightarrow b1$, $1\\xrightarrow c2$, $2\\xrightarrow c2$), puis on applique la table.\n\n" + det_sol(E2.remove_eps()) + f"\n\nLangage $a^*b^*c^*$ : vérifié sur tous les mots de longueur $\\le8$." + ("" if check_aut(E2.remove_eps().determinize(), lambda w: re.fullmatch("a*b*c*", w), 8) else FAILED)),
        v("s10", r"Combien d'états le DFA **minimal** du langage « la troisième lettre avant la fin est $a$ » (alphabet $\{a,b\}$) a-t-il ?", len(N3.determinize().minimal().Q), "8", r"Le DFA déterminisé a $8$ états ; deux ensembles distincts sont distingués par une suite de $3$ lettres bien choisie, donc il est déjà minimal : $8=2^3$. Pour « la $n$-ième lettre avant la fin », $2^n$ : un NFA à $n+1$ états donne un DFA à $2^n$ états, l'explosion est inévitable."),
    ]},
    {"n": 17, "titre": "Minimisation d'un DFA (Moore)", "notions": ["min"], "exos": [
        v("h1", f"{fig(M1, P_M1)}\n\n" + r"Ce DFA complet (initial $0$, final $5$) est accessible. Combien de classes d'indistinguabilité a-t-il (nombre d'états du DFA minimal) ?", len(M1.moore()[-1]), "4",
          r"Moore : $\{0,1,2,3,4\},\{5\}$ puis $\{0,1,3\},\{2,4\},\{5\}$ (car $2$ et $4$ vont en $5$ par $b$) puis $\{0\},\{1,3\},\{2,4\},\{5\}$ (car $1,3$ vont par $b$ en $\{2,4\}$ alors que $0$ va en $3$). Stable : $4$ classes."),
        v("h2", f"{fig(M1, P_M1)}\n\n" + r"Quelle est la longueur du plus court mot qui distingue les états $0$ et $1$ (accepté depuis l'un, refusé depuis l'autre) ?", len(distinguish(M1, 0, 1)), "2", r"Depuis $0$ ou $1$, ni $\varepsilon$, ni $a$, ni $b$, ni $ab$ n'aboutit à un état final de manière différente ; $\mathtt{bb}$ : $1\to2\to5$ (accepté) mais $0\to3\to4$ (refusé). Longueur $2$."),
        v("h3", f"{fig(M2, P_M2, B_M2)}\n\n" + r"Ce DFA complet (initial $0$, final $2$) a un état redondant. Combien d'états le DFA minimal a-t-il ?", len(M2.minimal().Q), "3", r"$0$ et $3$ ont les mêmes successeurs ($a\to1$, $b\to$ classe de $0$) : indistinguables. Classes $\{0,3\},\{1\},\{2\}$ : $3$ états (c'est le DFA des mots finissant par $ab$)."),
        v("h4", r"Combien d'états le DFA minimal du langage des mots de longueur multiple de $3$ sur $\{a,b\}$ a-t-il ?", len(thompson("((a+b)(a+b)(a+b))*", "ab").remove_eps().determinize().minimal().Q), "3", r"Il suffit de retenir la longueur modulo $3$ : $3$ états ; les trois restes sont deux à deux distingués par $\varepsilon$ et par des mots de longueur $1$ ou $2$."),
        o("h5", f"{fig(M1, P_M1)}\n\n" + r"Minimiser ce DFA avec l'algorithme de Moore : donner les partitions successives, puis le DFA minimal.",
          (lambda H, Mn: "Partitions : " + " ; puis ".join("$" + ",\\ ".join(sset(g) for g in part) + "$" for part in H) + ". Un état est mis à part quand ses successeurs par une lettre sont dans des classes différentes de ceux de son voisin.\n\n"
           + f"DFA minimal (classes numérotées dans l'ordre) : ${len(Mn.Q)}$ états.\n\n{fig(Mn, {0: (0, 0), 1: (1.3, 0), 2: (2.6, 0), 3: (3.9, 0)})}\n\nVérifié : équivalent à l'automate de départ (équivalence exacte) et minimal (aucun couple d'états indistinguable)." + ("" if M1.equivalent(Mn)[0] and len(Mn.moore()[-1]) == len(Mn.Q) else FAILED))(M1.moore(), M1.minimal())),
        o("h6", f"{fig(M2, P_M2, B_M2)}\n\n" + r"Minimiser ce DFA complet.",
          (lambda H, Mn: "Partitions : " + " ; puis ".join("$" + ",\\ ".join(sset(g) for g in part) + "$" for part in H) + f".\n\nLe DFA minimal a ${len(Mn.Q)}$ états :\n\n{fig(Mn, {0: (0, 0), 1: (1.2, 0), 2: (2.4, 0)}, {(2, 0): -52})}\n\nVérifié : équivalent à l'automate de départ et au DFA « finit par $ab$ » ($\\mathtt{{DAB}}$)." + ("" if M2.equivalent(Mn)[0] and DAB.equivalent(Mn)[0] else FAILED))(M2.moore(), M2.minimal())),
        o("h7", r"Soient $p$ et $p'$ deux états indistinguables d'un DFA, avec $p\xrightarrow aq$ et $p'\xrightarrow aq'$. Montrer que $q$ et $q'$ sont indistinguables. En quoi cette propriété justifie-t-elle l'algorithme de Moore ?",
          r"Par l'absurde : si un mot $w$ distingue $q$ et $q'$ (accepté depuis l'un, refusé depuis l'autre), alors $aw$ distingue $p$ et $p'$ (car $p\xrightarrow aq\xrightarrow w$ et $p'\xrightarrow aq'\xrightarrow w$), contradiction. **Conséquence :** dans une classe, les successeurs par chaque lettre doivent tomber dans une même classe ; si ce n'est pas le cas, les états ne sont pas indistinguables et on sépare la classe. On raffine jusqu'à ce que la propriété soit vérifiée : la partition obtenue est alors l'indistinguabilité."),
    ]},
    {"n": 18, "titre": "Lemme de l'étoile et langages non rationnels", "notions": ["pomp"], "exos": [
        v("u1", r"Un DFA a $6$ états. Quelle est la plus petite longueur $m$ telle que tout chemin de $m$ arêtes visite forcément deux fois le même état ?", len(range(6)) - 1 + 1, "6", r"Un chemin de $m$ arêtes visite $m+1$ états ; sans répétition il en faut au plus $6$ distincts, donc $m\le5$ sans répétition possible. À $m=6$ ($7$ états visités) un état se répète : tout mot de longueur $\ge6$ passe par une boucle. Le seuil de pompage $n_0=n+1=7$ du cours convient donc a fortiori."),
        o("u2", r"Montrer que $L=\{a^nb^n\mid n\ge0\}$ n'est pas rationnel.",
          r"Supposons $L$ rationnel et soit $n_0$ son seuil de pompage. Posons $w=a^{n_0}b^{n_0}\in L$, de longueur $2n_0\ge n_0$. Il existe $w=xyz$, $y\ne\varepsilon$, avec $xy^*z\subseteq L$ (et $|xy|\le n_0$ : la boucle se forme dans les $n_0$ premières lettres). Alors $y=a^k$, $k\ge1$ : trois cas selon le cours (plus de $a$ que de $b$ dans $y$, autant, plus de $b$) se réduisent ici au premier, car $y$ ne contient que des $a$. Le mot $xy^2z=a^{n_0+k}b^{n_0}$ a plus de $a$ que de $b$, donc n'est pas dans $L$ : contradiction. (Sans la borne $|xy|\le n_0$ : si $y=a^ub^v$ avec $u>v$, $xy^2z$ a $n_0+u$ $a$ et $n_0+v$ $b$ ; si $u=v\ge1$, $xy^2z$ contient $ba$ ; si $u < v$, trop de $b$.) Donc $L$ n'est pas rationnel : un automate fini ne peut pas compter jusqu'à $n$ pour $n$ non borné.", duree=10),
        o("u3", r"Montrer que $L=\{a^{n^2}\mid n\ge0\}$ (mots de longueur un carré parfait) n'est pas rationnel.",
          "Supposons $L$ rationnel, de seuil $n_0$ (avec la forme $|xy|\\le n_0$, qui découle du DFA : la boucle apparaît dans les $n_0$ premières lettres). Posons $w=a^{n_0^2}$ avec $n_0\\ge2$ et $w=xyz$, $y=a^k$, $1\\le k\\le n_0$. Alors $|xy^2z|=n_0^2+k$ avec $n_0^2 < n_0^2+k\\le n_0^2+n_0 < (n_0+1)^2$ : ce n'est pas un carré parfait, donc $xy^2z\\notin L$. Contradiction.\n\n"
          + ("Vérifié par calcul pour $n_0=2,\\dots,8$ : aucune décomposition $w=xyz$ avec $|xy|\\le n_0$ et $y\\ne\\varepsilon$ ne donne un mot de $xy^2z$ de longueur carrée." if all(int((n0 * n0 + k) ** 0.5) ** 2 != n0 * n0 + k for n0 in range(2, 9) for k in range(1, n0 + 1)) else FAILED), duree=12),
        o("u4", r"Alphabet $\{0,\dots,9\}$. Montrer que l'ensemble des écritures décimales des multiples de $3$ (avec zéros en tête autorisés, mot vide accepté) est rationnel.",
          (lambda D: f"Un nombre est multiple de $3$ si et seulement si la somme de ses chiffres l'est. Le DFA retient la somme modulo $3$ :\n\n{fig(D, {0: (0, 0), 1: (2.6, 0), 2: (5.2, 0)}, {}, {})}\n\nL'état $r$ lit le chiffre $d$ et passe à $(r+d)\\bmod3$ ; les étiquettes regroupent les chiffres de même reste. Initial et final : $0$. Vérifié sur tous les mots de longueur $\\le4$ contre `int(w) % 3 == 0`." + ("" if check_aut(D, lambda w: w == "" or int(w) % 3 == 0, 4, True, True) else FAILED))(Aut("0123456789", [(r, d, (r + int(d)) % 3) for r in range(3) for d in "0123456789"], [0], [0]))),
        o("u5", r"Montrer que $L=\{a^nb^m\mid n\ge m\ge0\}$ n'est pas rationnel.",
          r"Par l'absurde, soit $n_0$ le seuil de pompage et $w=a^{n_0}b^{n_0}\in L$. Soit $w=xyz$ avec $y\ne\varepsilon$ et $|xy|\le n_0$ : $y=a^k$, $k\ge1$. Pompons vers le bas : $xy^0z=a^{n_0-k}b^{n_0}$ a moins de $a$ que de $b$, donc n'est pas dans $L$ : contradiction. (Pomper vers le haut ne suffit pas : $a^{n_0+k}b^{n_0}\in L$. Choisir le bon $i$ dans $xy^iz$ est la clé.)", duree=10),
    ]},
    {"n": 19, "titre": "Élimination d'états : de l'automate à l'expression (BMC)", "notions": ["bmc"], "exos": [
        v("y1", r"On supprime un état $q$ qui a $2$ arêtes entrantes (venant de $2$ états distincts, différents de $q$) et $3$ arêtes sortantes (vers $3$ états distincts, différents de $q$). Combien de nouvelles arêtes crée-t-on ?", len(bmc(Aut("ab", [(0, "a", 5), (1, "b", 5), (5, "a", 2), (5, "b", 3), (5, "a", 4)], [0, 1], [2, 3, 4]), [5])[1][0][1]), "6", r"Un chemin $p\to q\to r$ par couple (entrante, sortante) : $2\times3=6$ nouvelles arêtes, éventuellement fusionnées avec des arêtes existantes par $+$."),
        o("y2", f"{fig(K1, P_K1)}\n\n" + r"Appliquer l'algorithme de Brzozowski-McCluskey à ce DFA (alphabet $\{a,b\}$) : donner une expression rationnelle de son langage.", _bmc_sol(K1, [1, 0], lambda w: w.count("a") % 2 == 0, "ab", 10)),
        o("y3", f"{fig(K2, P_K2)}\n\n" + r"Appliquer l'algorithme de Brzozowski-McCluskey à ce DFA (alphabet $\{a,b\}$).", _bmc_sol(K2, [0, 1], lambda w: w.endswith("a"), "ab", 10)),
        o("y4", f"{fig(K4, P_K4)}\n\n" + r"Appliquer l'algorithme à cet automate (alphabet $\{a,b,c\}$). Attention : il y a une arête de retour $2\to1$ ; la boucle de $1$ est facultative.", _bmc_sol(K4, [1, 2, 0], lambda w: re.fullmatch("ab*c(ab*c)*", w), "abc", 8)),
        o("y5", f"{fig(D3, P_D3)}\n\n" + r"Alphabet $\{0,1\}$. Appliquer l'algorithme à ce DFA des multiples de $3$ en binaire (supprimer $1$ puis $2$ puis $0$).", _bmc_sol(D3, [1, 2, 0], lambda w: w == "" or int(w, 2) % 3 == 0, "01", 10)),
    ]},
    {"n": 20, "titre": "Stabilité, produit synchronisé et décidabilité", "notions": ["stab"], "exos": [
        v("z1", f"{fig(K1, P_K1)}\n\n{fig(PB, P_PB)}\n\n" + r"Ces deux DFA complets (« nombre pair de $a$ » et « finit par $b$ ») ont $2$ états chacun. Combien d'états le produit synchronisé (partie accessible depuis le couple des états initiaux) a-t-il ?", len(K1.product(PB).Q), "4", r"Depuis $(0,0)$ : $a\to(1,0)$, $b\to(0,1)$ ; $(1,0)$ : $a\to(0,0)$, $b\to(1,1)$ ; $(0,1)$ : $a\to(1,0)$, $b\to(0,1)$ ; $(1,1)$ : $a\to(0,0)$, $b\to(1,1)$. Les $4=2\times2$ couples sont accessibles."),
        v("z2", f"{fig(K1, P_K1)}\n\n{fig(PB, P_PB)}\n\n" + r"Combien d'états finaux le produit synchronisé de ces deux DFA a-t-il pour **l'intersection** (les deux composantes finales) ?", len(K1.product(PB).final), "1", r"Final dans le premier : $0$ ; final dans le second : $1$. Le seul couple final est $(0,1)$."),
        v("z3", f"{fig(PB, P_PB)}\n\n{fig(K2, P_K2)}\n\n" + r"Le premier DFA reconnaît « finit par $b$ », le second « finit par $a$ ». L'intersection $L_1\cap L_2$ est-elle vide ? Répondre $1$ si oui, $0$ sinon.", int(PB.product(K2).shortest() is None), "1", r"Un mot ne peut pas finir à la fois par $a$ et par $b$ (ni être vide : $\varepsilon$ n'est dans aucun des deux) ; dans le produit, aucun état final n'est accessible. On décide le vide par un parcours."),
        v("z4", f"{fig(PB, P_PB)}\n\n{fig(K1, P_K1)}\n\n" + r"Premier DFA : « finit par $b$ ». Second : « nombre pair de $a$ ». Quelle est la longueur du plus court mot de $L_1\setminus L_2$ ?", len(PB.product(K1, "minus").shortest()), "2", r"On cherche un mot qui finit par $b$ avec un nombre impair de $a$ : le plus court est $\mathtt{ab}$ (le parcours en largeur du produit $L_1\cap\overline{L_2}$ le trouve). Longueur $2$."),
        o("z5", r"Posons $\Sigma=\{a,b\}$ et $L=L\big(a^*(ba^*ba^*ba^*)^*\big)$. On veut une expression rationnelle du complémentaire $\overline L=\Sigma^*\setminus L$. (1) $\overline L$ est-il rationnel ? (2) Donner un DFA de $L$. (3) En déduire un DFA de $\overline L$. (4) Appliquer BMC. (5) Que changer si $\Sigma=\{a,b,c\}$ ?",
          "**(1) Oui** : les langages rationnels sont stables par complément. **(2)** $L$ = mots dont le nombre de $b$ est multiple de $3$. DFA à $3$ états (nombre de $b$ modulo $3$) :\n\n"
          + f"{fig(Y0, P_Y0, B_Y0)}\n\n**(3)** DFA complet : on échange les finaux, finaux $\\{{1,2\\}}$ (nombre de $b$ non multiple de $3$).\n\n"
          + (lambda C: f"{fig(C, P_Y0, B_Y0)}\n\n" + _bmc_sol(C, [0, 1, 2], lambda w: w.count("b") % 3 != 0, "ab", 10))(Y0.complement())
          + "\n\n**(5)** Avec $\\Sigma=\\{a,b,c\\}$ le DFA doit lire $c$ : il faut le compléter (puits atteint par $c$, boucle sur toute lettre) **avant** d'échanger les finaux ; le puits devient alors final : tout mot contenant un $c$ est dans le complémentaire. Sinon l'expression ne décrirait que le complémentaire dans $\\{a,b\\}^*$." + ("" if Y0.complement().equivalent(Y0)[0] is False and check_aut(Y0, lambda w: w.count("b") % 3 == 0, 10, True, True) else FAILED),
          src="TD 5, ex. 1 (THLR, TD 2016-2017 et 2026)", duree=12),
        o("z6", r"(1) $L_2\subset L_1$ rationnels : $L_1\setminus L_2$ est-il rationnel ? (2) $L_2\subset L_1$ avec $L_2$ rationnel : $L_1$ est-il forcément rationnel ?",
          r"**(1) Oui** : $L_1\setminus L_2=L_1\cap\overline{L_2}$ ; $\overline{L_2}$ est rationnel (complément) et l'intersection de deux rationnels l'est (produit synchronisé, ou $\overline{\overline{A}\cup\overline{B}}$). **(2) Non** : $L_2=\varnothing$ est rationnel et inclus dans $L_1=\{a^nb^n\mid n\ge0\}$, non rationnel (lemme de l'étoile). Un sous-langage rationnel ne dit rien du langage qui le contient.",
          src="TD 5, ex. 2 (THLR, TD 2016-2017 et 2026)"),
        o("z7", f"{fig(K1, P_K1)}\n\n{fig(PB, P_PB)}\n\n" + r"Donner le produit synchronisé de ces deux DFA (table, états finaux pour l'intersection). En déduire le langage $L_1\cap L_2$ et décider s'il est vide.",
          (lambda Pr: "Table du produit ($(p,q)$ : $p$ état du premier DFA, $q$ du second) :\n" + table(Pr.renamed(lambda s: "".join(map(str, s)))) + f"\nÉtat initial $00$. L'unique état final est $01$ (premier final en $0$, second final en $1$). Le produit a ${len(Pr.Q)}\\le2\\times2$ états. $L_1\\cap L_2$ = mots avec un nombre pair de $a$ **et** qui finissent par $b$ : non vide (plus court mot : ${W(Pr.shortest())}$). Vérifié sur tous les mots de longueur $\\le10$." + ("" if check_aut(Pr, lambda w: w.count("a") % 2 == 0 and w.endswith("b"), 10, True, True) else FAILED))(K1.product(PB))),
    ]},
    {"n": 21, "titre": "Niveau examen : enchaîner expression, automate, DFA, complément", "notions": ["thompson", "eps", "emond", "det", "min", "stab", "afd-build"], "examen": True, "exos": [
        {"id": "mx1", "kind": "multi", "src": "TD 3, ex. 3 et TD 4, ex. 2 (THLR 2016-2017 et 2026) : chaîne du cours",
         "enonce": r"Alphabet $\{a,b,c\}$, expression $e=c(ab+c)$." "\n" r"1. Construire l'ε-NFA de Thompson. 2. Supprimer les $\varepsilon$-transitions. 3. Émonder. 4. Déterminiser (table complète). 5. Combien d'états a le DFA complet minimal ?",
         "parts": ["t4", "ea2", "ea3", "ea4", "ea5"]},
        {"id": "mx2", "kind": "multi", "src": "TD 4, ex. 3 (THLR 2016-2017 et 2026) : recherche de motifs",
         "enonce": r"Alphabet $\{a,b,c\}$. $L$ est le langage des mots qui ont $m=\mathtt{abab}$ pour suffixe." "\n" r"1. Donner un NFA de $L$. 2. Le déterminiser en un DFA complet (table). 3. On exécute le DFA sur $u=\mathtt{abababc}$ en comptant $c\leftarrow c+1$ à chaque fois qu'on se trouve dans un état final après une lettre : que vaut $c$ à la fin ? 4. Que calcule cet algorithme, avec quelle complexité ?",
         "parts": ["eb1", "s7", "eb3", "eb4"]},
        {"id": "mx3", "kind": "multi", "src": "DM 3, ex. 2 (THLR, DM 2016-2017) : multiples de 3 et de 7",
         "enonce": r"Soit $D_3$ le DFA à $3$ états des écritures binaires des multiples de $3$ (états $0,1,2$ = reste ; $\delta(r,c)=(2r+c)\bmod3$ ; initial et final $0$)." "\n" r"1. $D_3$ accepte-t-il $101010$ ? (répondre $1$ ou $0$). 2. Justifier que $D_3$ reconnaît les multiples de $3$. 3. Construire $D_7$ pour les multiples de $7$ (alphabet $\{0,1\}$). 4. Combien d'états le DFA minimal de $D_7$ a-t-il ?",
         "parts": ["ec1", "ec2", "ec4", "ec3"]},
        {"id": "mx4", "kind": "multi", "src": "TD 5, ex. 1 et 2 (THLR 2016-2017 et 2026) : complément et stabilité",
         "enonce": r"Alphabet $\{a,b\}$." "\n" r"1. Écrire une expression rationnelle du complémentaire de $L(a^*(ba^*ba^*ba^*)^*)$ (DFA, complément, BMC). 2. Si $L_2\subset L_1$ sont rationnels, $L_1\setminus L_2$ l'est-il ? Si $L_2$ seul est rationnel, $L_1$ l'est-il ?",
         "parts": ["z5", "z6"]},
    ]},
    {"n": 22, "titre": "Plus dur que l'examen (+20 %)", "notions": ["pomp", "stab", "min", "rx-desc"], "examen": True, "exos": [
        o("ex1", r"Montrer que le langage $L=\{w\in\{a,b\}^*\mid|w|_a=|w|_b\}$ n'est pas rationnel **sans** refaire de lemme de l'étoile sur $L$ lui-même (on connaît déjà $\{a^nb^n\}$).",
          "Par l'absurde : si $L$ était rationnel, comme $a^*b^*$ l'est aussi, $L\\cap a^*b^*$ serait rationnel (stabilité par intersection : produit synchronisé de deux automates). Or un mot $a^ib^j$ a autant de $a$ que de $b$ si et seulement si $i=j$ : $L\\cap a^*b^*=\\{a^nb^n\\mid n\\ge0\\}$, non rationnel (lemme de l'étoile). Contradiction.\n\n"
          + ("Vérifié sur tous les mots de longueur $\\le12$ : $L\\cap a^*b^*=\\{a^nb^n\\}$." if all(((re.fullmatch("a*b*", w) is not None) and w.count("a") == w.count("b")) == (len(w) % 2 == 0 and w == "a" * (len(w) // 2) + "b" * (len(w) // 2)) for w in words("ab", 12)) else FAILED), duree=12),
        o("ex2", r"Montrer que $L=\{a^nb^m\mid n\ne m\}$ n'est pas rationnel.",
          "Par l'absurde : si $L$ était rationnel, $\\overline L$ le serait (complément) et $\\overline L\\cap a^*b^*$ aussi (intersection avec un rationnel). Or les mots de $a^*b^*$ qui ne sont pas dans $L$ sont ceux avec $n=m$ : $\\overline L\\cap a^*b^*=\\{a^nb^n\\}$, non rationnel. Contradiction. (Attention : $\\overline L$ contient aussi des mots hors $a^*b^*$, comme $\\mathtt{ba}$ ; c'est l'intersection qui les retire.)\n\n"
          + ("Vérifié sur tous les mots de longueur $\\le12$ : $a^*b^*\\setminus L=\\{a^nb^n\\}$." if all(((re.fullmatch("a*b*", w) is not None) and w.count("a") == w.count("b")) == (len(w) % 2 == 0 and w == "a" * (len(w) // 2) + "b" * (len(w) // 2)) for w in words("ab", 12)) else FAILED), duree=12),
        v("ex3", r"Alphabet $\{a,b\}$. Combien d'états le DFA complet minimal du langage des mots qui **contiennent** $\mathtt{abab}$ comme facteur a-t-il ?", len(thompson("(a+b)*abab(a+b)*", "ab").remove_eps().determinize().minimal().Q), "5",
          r"On retient la longueur du plus long préfixe de $\mathtt{abab}$ qui est suffixe du mot lu : $0,1,2,3$ ; l'état $4$ (motif trouvé) est final et absorbant. Ces $5$ états sont deux à deux distingués (par des suffixes de $\mathtt{abab}$) : le minimal en a $5$.", duree=8),
        o("ex4", r"Décrire un algorithme qui décide si deux expressions rationnelles $e$ et $f$ sont équivalentes (en renvoyant un contre-exemple sinon), puis l'appliquer à $e=(a+ab)^*$ et $f=(a+ba)^*$ sur $\{a,b\}$.",
          (lambda w: f"**Algorithme.** (1) Calculer deux DFA complets $A_e$, $A_f$ (Thompson, suppression des $\\varepsilon$, déterminisation). (2) Calculer les compléments $\\overline{{A_e}}$, $\\overline{{A_f}}$ et les produits $A_e\\times\\overline{{A_f}}$, $A_f\\times\\overline{{A_e}}$. (3) Parcours en largeur de chaque produit depuis l'état initial : un état final accessible fournit un mot $w$ qui est dans $L(e)\\setminus L(f)$ (ou l'inverse) ; si aucun n'est accessible, $L(e)=L(f)$.\n\n**Application.** $L(e)$ : mots sans $bb$ qui ne commencent pas par $b$ ; $L(f)$ : mots sans $bb$ qui ne finissent pas par $b$. Le plus court mot qui les sépare a pour longueur ${len(w)}$ : ${W(w)}$, qui est dans $L({'e' if rx_match('(a+ab)*', w) else 'f'})$ et pas dans l'autre. Les deux langages ne sont donc pas équivalents. Vérifié : calcul exact par produit." + ("" if rx_match("(a+ab)*", w) != rx_match("(a+ba)*", w) else FAILED))(thompson("(a+ab)*", "ab").equivalent(thompson("(a+ba)*", "ab"))[1])),
        v("ex5", r"Alphabet $\{a,b\}$. Combien d'états le DFA complet minimal du langage « la quatrième lettre avant la fin est $a$ » a-t-il ?", len(N4.determinize().minimal().Q), "16", r"Un NFA à $5$ états ; le DFA déterminisé a $2^4=16$ états (on retient les $4$ dernières lettres), tous distinguables : $16$. La déterminisation peut être exponentielle."),
    ]},
]


# ---------------------------------------------------------------- parts of the exam-level chains (EXTRA_PARTS)

CH_E = "c(ab+c)"
CH_T = thompson(CH_E, "abc")
CH_R = CH_T.remove_eps()
CH_P = CH_R.prune()
CH_D = CH_P.determinize()
CH_M = CH_D.minimal()
for _A in (CH_R, CH_P, CH_D, CH_M):
    assert CH_T.equivalent(_A)[0]
assert not CH_R.has_eps() and CH_D.is_dfa() and CH_D.is_complete()


def mult(k):
    """DFA of the binary writings of the multiples of k: state = value mod k."""
    return Aut("01", [(r, c, (2 * r + int(c)) % k) for r in range(k) for c in "01"], [0], [0])


def occ(D, u):
    """Value of the counter c of TD 4 ex. 3.5: number of letters after which the DFA is in a final state."""
    q, c = next(iter(D.init)), 0
    for x in u:
        q = next(iter(D.d[(q, x)]))
        c += q in D.final
    return c


_DM = NABAB.determinize()
assert occ(_DM, "abababc") == sum(1 for i in range(len("abababc")) if "abababc"[:i + 1].endswith("abab"))
assert occ(_DM, "cabbababababc") == sum(1 for i in range(13) if "cabbababababc"[:i + 1].endswith("abab"))
D7 = mult(7)

EXTRA_PARTS = [
    o("ea2", r"Suppression des $\varepsilon$-transitions de l'automate de Thompson de $c(ab+c)$.",
      f"Transitions de $T$ : ${trans_list(CH_T)}$ ; initial ${sset(CH_T.init)}$, final ${sset(CH_T.final)}$.\n\nClôtures : " + ", ".join(f"$\\mathrm{{cl}}({q})={sset(CH_T.closure([q]))}$" for q in CH_T.Q)
      + f".\n\nRetour arrière : ${trans_list(CH_R)}$ ; états finaux ${sset(CH_R.final)}$ (clôture contenant l'état final de $T$).\n\nVérifié : aucun $\\varepsilon$ et langage inchangé (équivalence exacte avec $T$).", src="TD 3, ex. 3.1 (THLR 2016-2017 et 2026)"),
    o("ea3", r"Émonder l'automate précédent.",
      f"Accessibles : ${sset(CH_R.accessible())}$. Co-accessibles : ${sset(CH_R.coaccessible())}$. États utiles : ${sset(CH_P.Q)}$ ({len(CH_P.Q)} états).\n\nAutomate émondé : ${trans_list(CH_P)}$, initial ${sset(CH_P.init)}$, finals ${sset(CH_P.final)}$. Langage : $\\{{cab,cc\\}}$.\n\n"
      + ("Vérifié : équivalent à l'automate de Thompson ; langage $\\{cab,cc\\}$ sur tous les mots de longueur $\\le6$." if check_aut(CH_P, lambda w: w in ("cab", "cc"), 6) else FAILED), src="TD 3, ex. 3.1 (THLR 2016-2017 et 2026)"),
    o("ea4", r"Déterminiser l'automate émondé (table complète).", det_sol(CH_P), src="TD 4, ex. 2 (THLR 2016-2017 et 2026)"),
    v("ea5", r"Combien d'états le DFA complet **minimal** de $L=\{cab,cc\}$ a-t-il ?", len(CH_M.Q), "5",
      r"$L=\{cab,cc\}$. États : $0$ (début), $1$ (lu $c$), $2$ (lu $ca$), $3$ (mot de $L$ lu, final), $4$ (puits). Transitions : $0\xrightarrow c1$, $1\xrightarrow a2$, $1\xrightarrow c3$, $2\xrightarrow b3$, le reste va au puits. Ces $5$ états sont deux à deux distingués. Le DFA déterminisé en a " + str(len(CH_D.Q)) + " avant minimisation (Moore)."),
    o("eb1", f"{fig(NABAB, P_NABAB)}\n\n" + r"Alphabet $\{a,b,c\}$. Prouver que $L=\{um\mid u\in\Sigma^*\}$ avec $m=\mathtt{abab}$ est rationnel en donnant un NFA, et justifier la construction.",
      f"Le NFA ci-dessus : $0$ boucle sur toutes les lettres ($u$), puis il lit $m=\\mathtt{{abab}}$ lettre par lettre vers $1,2,3,4$ (final). Il reconnaît $L$ ; un langage reconnu par un automate fini est rationnel (théorème de Kleene). Vérifié sur tous les mots de longueur $\\le9$." + ("" if check_aut(NABAB, lambda w: w.endswith("abab"), 9) else FAILED),
      src="TD 4, ex. 3.1 (THLR 2016-2017 et 2026)"),
    v("eb3", r"Le DFA complet des mots finissant par $\mathtt{abab}$ (alphabet $\{a,b,c\}$) lit $u=\mathtt{abababc}$ ; un compteur $c$ augmente de $1$ chaque fois qu'on est dans un état final après une lettre. Que vaut $c$ à la fin ?", occ(_DM, "abababc"), "2",
      r"Les préfixes $\mathtt{abab}$ (longueur $4$) et $\mathtt{ababab}$ (longueur $6$) finissent par $\mathtt{abab}$ : on est en état final après la $4^e$ et la $6^e$ lettre. Après le $c$ final, non. Donc $c=2$ (occurrences chevauchantes comprises).", src="TD 4, ex. 3.5 (THLR 2016-2017 et 2026)"),
    o("eb4", r"Que calcule l'algorithme du compteur $c$ en général, avec quelle complexité ? Que vaut $c$ pour $u=\mathtt{cabbababababc}$ ? Comment compter seulement les occurrences disjointes ?",
      f"Il compte les **occurrences de $m$ dans $u$** (une par position où un préfixe de $u$ finit par $m$), chevauchements compris. Complexité : une transition (accès à un tableau) par lettre, soit $O(|u|)$ (le DFA est fixé). Pour $u=\\mathtt{{cabbababababc}}$ : $c={occ(_DM, 'cabbababababc')}$ (les occurrences $\\mathtt{{abab}}$ en positions $5,7,9$ se chevauchent). Pour les occurrences disjointes : après un état final, on reprend depuis l'état initial (on redirige les arêtes sortantes d'un état final comme celles de l'état initial). Vérifié par parcours du DFA et par recherche naïve.",
      src="TD 4, ex. 3.5 (THLR 2016-2017 et 2026)"),
    v("ec1", f"{fig(D3, P_D3)}\n\n" + r"$D_3$ accepte-t-il le mot binaire $\mathtt{101010}$ ? Répondre $1$ si oui, $0$ sinon.", int(D3.accepts("101010")), "1", r"$\mathtt{101010}=42=3\times14$ : on lit $0\to1\to2\to2\to1\to0\to0$ ; final.", src="DM 3, ex. 2.1 (THLR, DM 2016-2017)"),
    o("ec2", r"Montrer que $D_3$ reconnaît exactement les écritures binaires des multiples de $3$.",
      "**Invariant :** après avoir lu le mot $w$ (de valeur binaire $\\mathrm{val}(w)$, $\\mathrm{val}(\\varepsilon)=0$), l'état est $\\mathrm{val}(w)\\bmod3$. Base : $\\varepsilon$, état $0$. Hérédité : $\\mathrm{val}(wc)=2\\,\\mathrm{val}(w)+c$, et $\\delta(r,c)=(2r+c)\\bmod3$, donc l'état après $wc$ est $(2\\,\\mathrm{val}(w)+c)\\bmod3$. Le mot est accepté si l'état final $0$ est atteint, c'est-à-dire si $3\\mid\\mathrm{val}(w)$. Vérifié par calcul sur tous les mots de longueur $\\le12$." + ("" if check_aut(D3, lambda w: w == "" or int(w, 2) % 3 == 0, 12, True, True) else FAILED), src="DM 3, ex. 2.2 (THLR, DM 2016-2017)"),
    o("ec4", r"Construire $D_7$ pour les multiples de $7$ en binaire.",
      "Même idée : $7$ états $0,\\dots,6$, $\\delta(r,c)=(2r+c)\\bmod7$, initial et final $0$.\n" + table(D7) + "Vérifié sur tous les mots de longueur $\\le12$ contre `int(w, 2) % 7 == 0`." + ("" if check_aut(D7, lambda w: w == "" or int(w, 2) % 7 == 0, 12, True, True) else FAILED), src="DM 3, ex. 2.3 (THLR, DM 2016-2017)"),
    v("ec3", r"Combien d'états le DFA minimal des multiples de $7$ en binaire a-t-il ?", len(D7.minimal().Q), "7", r"Deux restes différents $r\ne r'$ sont distingués par un mot binaire $w$ tel que $r\cdot2^{|w|}+\mathrm{val}(w)\equiv0\pmod7$ pour l'un seul ; le DFA à $7$ états est donc minimal.", src="DM 3, ex. 2.3 (THLR, DM 2016-2017)"),
]


# ---------------------------------------------------------------- variants (same method, other data; each one is checked like the exercise)

def _fa(A, pos, bend=None, loops=None, names=None):
    return fig(A, pos, bend, loops, names=names) + "\n\n"


NABA3 = Aut("abc", [(0, "a", 0), (0, "b", 0), (0, "c", 0), (0, "a", 1), (1, "b", 2), (2, "a", 3)], [0], [3])
_E5 = "(ab+c)(d+g)(ε+f)"
_PAIR8 = PAIRS[7]
_PC = [rel(e, f, "abc") for e, f in PAIRS]
assert _PC.count("<") == 5, _PC

VARIANTS = {
    "n1": [_v(r"$|A|=15$, $|B|=8$ et $|A\cap B|=5$. Que vaut $|A\cup B|$ ?", "15+8-5", "18", r"$15+8-5=18$.")],
    "n2": [_v(r"Un ensemble $E$ a $8$ éléments. Combien de parties a-t-il ?", sum(comb(8, k) for k in range(9)), "256", r"$2^8=256$.")],
    "n3": [_v(r"$|A|=6$ et $|B|=7$. Que vaut $|A\times B|$ ?", len(list(itertools.product(range(6), range(7)))), "42", r"$6\times7=42$.")],
    "n4": [_v(r"Combien de sous-ensembles à $2$ éléments un ensemble à $9$ éléments a-t-il ?", len(list(itertools.combinations(range(9), 2))), "36", r"$\binom92=36$.")],
    "n5": [_v(r"Un automate a $4$ états et $3$ lettres. Combien de triplets (état, lettre, état) existe-t-il ?", len(list(itertools.product(range(4), "abc", range(4)))), "48", r"$4\times3\times4=48$.")],
    "n6": [_v(r"Combien d'entiers de $1$ à $30$ sont multiples de $2$ ou de $5$ ?", len([x for x in range(1, 31) if x % 2 == 0 or x % 5 == 0]), "18", r"$15+6-3=18$.")],
    "r1": [_v(r"Calculer $\sum_{k=0}^{7}2^k$.", sum(2 ** k for k in range(8)), "255", r"$2^8-1=255$.")],
    "r2": [_v(r"Sur $\{0,\dots,11\}$, $x\sim y$ si $x\equiv y\pmod3$. Combien de couples $(x,y)$ vérifient $x\sim y$ ?", sum(1 for x in range(12) for y in range(12) if (x - y) % 3 == 0), "48", r"$3$ classes de $4$ éléments : $3\times16=48$.")],
    "r3": [_v(r"Combien de listes de longueur $3$ avec l'alphabet $\{a,b,c,d\}$ ?", len(list(itertools.product("abcd", repeat=3))), "64", r"$4^3=64$.")],
    "m1": [_v(r"Longueur du mot $w=\mathtt{EPITAEPITA}$ ?", len("EPITAEPITA"), "10", r"Dix lettres.")],
    "m2": [_v(r"Soit $w=1001011$. Que vaut $|w|_0$ ?", "1001011".count("0"), "3", r"Les positions $2,3,5$ valent $0$.")],
    "m3": [_v(r"Soit $w=\mathtt{bca}$. Que vaut $|w^6|$ ?", len("bca" * 6), "18", r"$6\times3=18$.")],
    "m4": [_v(r"Le mot $\mathtt{abca}$ est-il un palindrome ? ($1$ oui, $0$ non)", int("abca" == "abca"[::-1]), "0", r"$w^R=\mathtt{acba}\ne w$.")],
    "m5": [_v(r"Combien de mots de longueur $5$ sur $\{0,1\}$ contiennent exactement trois $1$ ?", len([w for w in words("01", 5) if len(w) == 5 and w.count("1") == 3]), "10", r"$\binom53=10$.")],
    "m6": [_v(r"Soient $u=\mathtt{ab}$ et $v=\mathtt{cde}$. Longueur de $u\cdot v\cdot u^R$ ?", len("ab" + "cde" + "ab"[::-1]), "7", r"$2+3+2=7$.")],
    "p1": [_v(r"Combien de préfixes distincts le mot $\mathtt{EPITA}$ a-t-il ?", len(pref("EPITA")), "6", r"$|w|+1=6$.")],
    "p2": [_v(r"Combien de suffixes distincts le mot $\mathtt{banana}$ a-t-il ?", len(suff("banana")), "7", r"Longueurs $0$ à $6$ : $7$.")],
    "p3": [_v(r"Combien de facteurs distincts le mot $\mathtt{aaaa}$ a-t-il ?", len(fact("aaaa")), "5", r"$\varepsilon,a,aa,aaa,aaaa$ : un par longueur.")],
    "p4": [_v(r"Le mot $\mathtt{bb}$ est-il un facteur de $\mathtt{ababa}$ ? ($1$ oui, $0$ non)", int("bb" in fact("ababa")), "0", r"$\mathtt{ababa}$ n'a pas deux $b$ consécutifs.")],
    "p5": [_v(r"Combien de facteurs propres (ni préfixes ni suffixes) le mot $\mathtt{aabb}$ a-t-il ?", len(fact("aabb") - pref("aabb") - suff("aabb")), "1", r"Facteurs : $9$ ; préfixes et suffixes réunis : $8$ ; reste $\mathtt{ab}$.")],
    "d1": [_v(r"Distance d'édition entre $\mathtt{cat}$ et $\mathtt{cart}$ ?", de("cat", "cart"), "1", r"Insérer $r$ : $3+4-2\times3=1$.")],
    "d2": [_v(r"Distance d'édition entre $\mathtt{EPITA}$ et $\mathtt{PITA}$ ?", de("EPITA", "PITA"), "1", r"Supprimer le $E$.")],
    "d3": [_v(r"Distance d'édition entre $\mathtt{abcd}$ et $\mathtt{dcba}$ ?", de("abcd", "dcba"), "6", r"Plus longue sous-suite commune de longueur $1$ : $4+4-2=6$.")],
    "d4": [_v(r"Distance d'édition entre $\mathtt{aab}$ et $\mathtt{abb}$ ?", de("aab", "abb"), "2", r"Sous-suite commune $\mathtt{ab}$ : $3+3-4=2$.")],
    "l1": [_v(r"$L_1=\{a,ab\}$ et $L_2=\{b,bb\}$. Combien de mots a $L_1L_2$ ?", len(lcat({"a", "ab"}, {"b", "bb"})), "3", r"$ab,abb,abb,abbb$ : $3$ mots distincts (deux produits donnent $abb$).")],
    "l2": [_v(r"$L=\{a,ab,b\}$. Combien de mots a $L^2$ ?", len(lpow({"a", "ab", "b"}, 2)), "9", r"$aa,aab,ab,aba,abab,abb,ba,bab,bb$ : $9$ produits, tous distincts.")],
    "l3": [_v(r"$L=\{a,aaa\}$. Combien de mots a $L^2$ ?", len(lpow({"a", "aaa"}, 2)), "3", r"$aa,aaaa,aaaaaa$ ($a\cdot aaa$ et $aaa\cdot a$ coïncident).")],
    "l4": [_v(r"$L=\{ab,c\}$. Le mot $\mathtt{abca}$ est-il dans $L^*$ ? ($1$ oui, $0$ non)", int(in_star("abca", {"ab", "c"})), "0", r"Après $ab\cdot c$ reste $a$, qui n'est pas un mot de $L$.")],
    "l5": [_v(r"Combien de mots a $\mathrm{Pref}(\{ab,c,ba\})$ ?", len(pref("ab") | pref("c") | pref("ba")), "6", r"$\{\varepsilon,a,ab,c,b,ba\}$.")],
    "l6": [_v(r"Combien de mots de longueur $\le2$ le langage $\{a,b,c\}^*$ contient-il ?", len(list(words("abc", 2))), "13", r"$1+3+9=13$.")],
    "x1": [_v(r"Le mot $\mathtt{abba}$ appartient-il à $L\big(a(a+b)^*b\big)$ ? ($1$ oui, $0$ non)", int(rx_match("a(a+b)*b", "abba")), "0", r"Il finit par $a$.")],
    "x2": [_v(r"Combien de mots de longueur $\le3$ le langage $L(a^*bb^*)$ contient-il ?", len(lang_upto("a*bb*", "ab", 3)), "6", r"$a^ib^j$, $j\ge1$, $i+j\le3$ : $b,bb,bbb,ab,abb,aab$.")],
    "x3": [_v(r"Même alphabet et même expression $e=v\,v^*(\varepsilon+f)(t+u)m$. Parmi $\mathtt{vtm}$, $\mathtt{vfum}$, $\mathtt{tm}$, $\mathtt{vvm}$, $\mathtt{vftm}$, $\mathtt{vfm}$, combien sont décrits par $e$ ?", sum(rx_match("vv*(ε+f)(t+u)m", w) for w in ["vtm", "vfum", "tm", "vvm", "vftm", "vfm"]), "3", r"Conviennent $\mathtt{vtm}$, $\mathtt{vfum}$, $\mathtt{vftm}$ ; $\mathtt{tm}$ n'a pas de $v$, $\mathtt{vvm}$ et $\mathtt{vfm}$ n'ont ni $t$ ni $u$.")],
    "x4": [_v(r"Combien de mots contient $L\big((a+b+c)(\varepsilon+d)\big)$ ?", len(lang_upto("(a+b+c)(ε+d)", "abcd", 3)), "6", r"$3\times2=6$.")],
    "x5": [_v(r"Quelle est la longueur du plus court mot de $L\big((ab+c)(d+g)(\varepsilon+f)\big)$ ?", min(len(w) for w in lang_upto(_E5, "abcdgf", 5)), "2", r"$c\cdot d\cdot\varepsilon=\mathtt{cd}$, longueur $2$.")],
    "q4": [_v(r"Même liste de neuf couples. Pour combien de couples a-t-on $L(e)\subsetneq L(f)$ (inclusion stricte dans ce sens) ?", _PC.count("<"), "5", r"Couples $2,3,4,7,9$ ; le couple $8$ est l'inclusion inverse ($f\subsetneq e$) et le couple $1$ est incomparable.")],
    "q6": [_v(r"Quelle est la longueur du plus court mot qui appartient à exactement un des langages $L\big((abc+acb)^*\big)$ et $L\big((abc(acb)^*)^*\big)$ ?", len(thompson(_PAIR8[0], "abc").equivalent(thompson(_PAIR8[1], "abc"))[1]), "3", r"$\mathtt{acb}$ est dans le premier et pas dans le second (qui ne peut commencer que par $abc$) ; aucun mot plus court ne les sépare.")],
    "w7": [_v(r"Combien de mots de longueur $5$ le langage $L\big(b^*ab^*ab^*\big)$ contient-il ?", len([w for w in lang_upto("b*ab*ab*", "ab", 5) if len(w) == 5]), "10", r"$\binom52=10$.")],
    "a1": [_v(f"{fig(DAB, P_DAB, B_DAB)}\n\n" + r"Le même DFA accepte-t-il $\mathtt{abba}$ ? ($1$ oui, $0$ non)", int(DAB.accepts("abba")), "0", r"$0\to1\to2\to0\to1$ : état $1$ non final.")],
    "a2": [_v(f"{fig(DAB, P_DAB, B_DAB)}\n\n" + r"Dans quel état est-on après avoir lu $\mathtt{abab}$ ?", DAB.run("abab"), "2", r"$0\to1\to2\to1\to2$.")],
    "a3": [_v(f"{fig(NABA, P_NABA)}\n\n" + r"Combien de chemins acceptants sont étiquetés par $\mathtt{abab}$ ?", NABA.paths("abab")[1], "0", r"Pour finir en $3$ il faut finir par $\mathtt{aba}$ ; $\mathtt{abab}$ finit par $\mathtt{bab}$ : aucun.")],
    "a4": [_v(f"{fig(DAB, P_DAB, B_DAB)}\n\n" + r"Quelle est la longueur du plus court mot accepté par ce DFA ?", len(DAB.shortest()), "2", r"$\mathtt{ab}$.")],
    "a5": [_v(f"{fig(DAB, P_DAB, B_DAB)}\n\n" + r"Combien de mots de longueur $5$ ce DFA accepte-t-il ?", len([w for w in DAB.lang(5) if len(w) == 5]), "8", r"$\mathtt{???ab}$ : $2^3=8$.")],
    "b6": [_v(r"Un DFA **complet** a $7$ états sur $\{a,b\}$. Combien a-t-il de transitions ?", len(list(itertools.product(range(7), "ab"))), "14", r"$7\times2=14$.")],
    "c1": [_v(f"{fig(I2, P_I2)}\n\n" + r"On complète ce DFA avec un puits. Combien de transitions l'automate complet a-t-il ?", ntrans(I2.complete()), "6", r"$3$ états $\times$ $2$ lettres.")],
    "c2": [_v(f"{fig(I2, P_I2)}\n\n" + r"On complète puis on prend le complément. Combien de mots de longueur $\le3$ ce DFA accepte-t-il ?", len(I2.complete().complement().lang(3)), "12", r"$L(I_2)=\{ab^n\}$ : $a,ab,abb$ de longueur $\le3$ ; $15-3=12$.")],
    "c3": [_v(f"{fig(I2, P_I2)}\n\n" + r"Le complément de $L(I_2)$ contient-il $\mathtt b$ ? ($1$ oui, $0$ non)", int(I2.complete().complement().accepts("b")), "1", r"$\mathtt b\notin L(ab^*)$, donc il est dans le complément.")],
    "c4": [_v(f"{fig(I2, P_I2)}\n\n" + r"Combien d'états finaux le DFA complément (du DFA complété) a-t-il ?", len(I2.complete().complement().final), "2", r"$3$ états dont $1$ final ; le complément a $2$ finaux.")],
    "t1": [_v(r"Combien d'états l'automate de Thompson de $(ab+c)^*a$ a-t-il ?", len(thompson("(ab+c)*a", "abc").Q), "12", r"$4$ lettres, un $+$, une étoile : $n=6$, soit $12$ états.")],
    "t2": [_v(r"Combien de transitions spontanées l'automate de Thompson de $(ab+c)^*a$ a-t-il ?", sum(1 for _, a, _ in thompson("(ab+c)*a", "abc").trans() if a == ""), "10", r"$4$ ($+$) $+4$ (étoile) $+2$ concaténations (entre $a$ et $b$, entre l'étoile et $a$) $=10$.")],
    "t3": [_v(r"Combien de transitions étiquetées par une lettre l'automate de Thompson de $(ab+c)^*a$ a-t-il ?", sum(1 for _, a, _ in thompson("(ab+c)*a", "abc").trans() if a != ""), "4", r"Une par lettre : $a,b,c,a$.")],
    "k1": [_v(f"{fig(E2, P_E2)}\n\n" + r"Combien d'états la $\varepsilon$-clôture avant de l'état $1$ contient-elle ?", len(E2.closure([1])), "2", r"$\{1,2\}$.")],
    "k2": [_v(f"{fig(E2, P_E2)}\n\n" + r"On supprime les $\varepsilon$-transitions (retour arrière). Combien d'états finaux l'automate obtenu a-t-il ?", len(E2.remove_eps().final), "3", r"Chaque clôture contient l'état final $2$ : $0,1,2$ deviennent finals.")],
    "k3": [_v(f"{fig(E4, P_E4)}\n\n" + r"Combien de transitions étiquetées par une lettre l'automate sans $\varepsilon$ obtenu a-t-il ?", ntrans(E4.remove_eps()), "2", r"$\mathrm{cl}(0)=\{0,1\}$ donne $0\xrightarrow a2$ ; $1\xrightarrow a2$ existe déjà ; $\mathrm{cl}(2)=\{2,3\}$ ne donne rien : $2$ arêtes.")],
    "k4": [_v(r"Même question pour l'automate à $3$ états dont les $\varepsilon$-arêtes sont $0\to1$, $1\to2$, $2\to0$ : à quelle colonne $i$ la table des clôtures est-elle stable ?", fix_step(E5), "1", r"Colonne 0 : $\{0,1\},\{1,2\},\{2,0\}$ ; colonne 1 : tous les états ont $\{0,1,2\}$ ; la colonne 2 est identique : $i=1$.")],
    "g1": [_v(f"{fig(P2, P_P2, B_P2, L_P2)}\n\n" + r"Combien d'états utiles cet automate (initial $0$, final $2$) a-t-il ?", len(P2.useful()), "3", r"Accessibles $0,1,2,3$ ; co-accessibles $0,1,2,4$ ; utiles $0,1,2$.")],
    "g2": [_v(f"{fig(P2, P_P2, B_P2, L_P2)}\n\n" + r"Combien d'états accessibles ?", len(P2.accessible()), "4", r"$\{0,1,2,3\}$ ($4$ n'a pas d'arête entrante).")],
    "g3": [_v(f"{fig(P2, P_P2, B_P2, L_P2)}\n\n" + r"Combien d'états co-accessibles ?", len(P2.coaccessible()), "4", r"$\{0,1,2,4\}$ ($3$ ne mène qu'à lui-même).")],
    "g4": [_v(f"{fig(P2, P_P2, B_P2, L_P2)}\n\n" + r"Combien de transitions l'automate émondé a-t-il ?", ntrans(P2.prune()), "3", r"$0\xrightarrow a1$, $1\xrightarrow a2$, $2\xrightarrow b2$.")],
    "s1": [_v(f"{fig(NABA, P_NABA)}\n\n" + r"Ce NFA reconnaît les mots (alphabet $\{a,b\}$) qui finissent par $\mathtt{aba}$. Combien d'états le DFA déterminisé a-t-il ?", len(NABA.determinize().Q), "4", r"On retient la longueur du plus long suffixe qui est préfixe de $\mathtt{aba}$ : $0,1,2,3$ : $4$ états.")],
    "s2": [_v(f"{fig(N4, P_N4)}\n\n" + r"Ce NFA reconnaît les mots dont la quatrième lettre avant la fin est $a$. Combien d'états le DFA déterminisé a-t-il ?", len(N4.determinize().Q), "16", r"$2^4=16$ : on retient les quatre dernières lettres.")],
    "s3": [_v(f"{fig(N2, P_N2)}\n\n" + r"Combien d'états finaux le DFA déterminisé de ce NFA (final $2$) a-t-il ?", len(N2.determinize().final), "2", r"Les ensembles qui contiennent $2$ : $\{0,1,2\}$ et $\{0,2\}$.")],
    "s4": [_v(f"{fig(N2, P_N2)}\n\n" + r"Quel est le cardinal de l'état atteint depuis $\{0,1,2\}$ en lisant $a$ ?", len(N2.step({0, 1, 2}, "a")), "3", r"$\delta(0,a)=\{0,1\}$, $\delta(1,a)=\{2\}$, $\delta(2,a)=\varnothing$ : $\{0,1,2\}$.")],
    "s5": [_v(f"{fig(NABA3, P_NABAB if False else row(4))}\n\n" + r"Alphabet $\{a,b,c\}$ ; ce NFA reconnaît les mots qui finissent par $\mathtt{aba}$. Combien d'états le DFA déterminisé a-t-il ?", len(NABA3.determinize().Q), "4", r"Longueur du plus long suffixe qui est préfixe de $\mathtt{aba}$ : $4$ états.")],
    "s10": [_v(r"Combien d'états le DFA complet minimal du langage « la quatrième lettre avant la fin est $a$ » a-t-il ?", len(N4.determinize().minimal().Q), "16", r"$2^4=16$.")],
    "h1": [_v(f"{fig(M2, P_M2, B_M2)}\n\n" + r"Combien de classes d'indistinguabilité ce DFA complet accessible a-t-il ?", len(M2.moore()[-1]), "3", r"$\{0,3\},\{1\},\{2\}$.")],
    "h2": [_v(f"{fig(M1, P_M1)}\n\n" + r"Quelle est la longueur du plus court mot qui distingue les états $3$ et $4$ ?", len(distinguish(M1, 3, 4)), "1", r"$\mathtt b$ : $4\xrightarrow b5$ (final), $3\xrightarrow b4$ (non final).")],
    "h3": [_v(f"{fig(M1, P_M1)}\n\n" + r"Combien d'états le DFA minimal a-t-il ?", len(M1.minimal().Q), "4", r"$\{0\},\{1,3\},\{2,4\},\{5\}$.")],
    "h4": [_v(r"Combien d'états le DFA minimal des mots de longueur multiple de $4$ sur $\{a,b\}$ a-t-il ?", len(thompson("((a+b)(a+b)(a+b)(a+b))*", "ab").remove_eps().determinize().minimal().Q), "4", r"La longueur modulo $4$ : $4$ états.")],
    "u1": [_v(r"Un DFA a $9$ états. Quelle est la plus petite longueur $m$ telle que tout chemin de $m$ arêtes repasse par un état ?", len(range(9)) - 1 + 1, "9", r"$m+1>9$ états visités dès $m=9$.")],
    "y1": [_v(r"On supprime un état qui a $3$ arêtes entrantes (de $3$ états distincts) et $4$ sortantes (vers $4$ états distincts). Combien de nouvelles arêtes crée-t-on ?", len(bmc(Aut("ab", [(0, "a", 5), (1, "b", 5), (6, "a", 5), (5, "a", 2), (5, "b", 3), (5, "a", 4), (5, "b", 7)], [0, 1, 6], [2, 3, 4, 7]), [5])[1][0][1]), "12", r"$3\times4=12$.")],
    "z1": [_v(f"{fig(K2, P_K2)}\n\n{fig(PB, P_PB)}\n\n" + r"DFA « finit par $a$ » et « finit par $b$ ». Combien d'états le produit synchronisé (partie accessible) a-t-il ?", len(K2.product(PB).Q), "3", r"$(0,0)\xrightarrow a(1,0)$, $(0,0)\xrightarrow b(0,1)$ ; depuis ces deux couples on revient sur eux : $3$ états ($(1,1)$ n'est pas accessible).")],
    "z2": [_v(f"{fig(K2, P_K2)}\n\n{fig(PB, P_PB)}\n\n" + r"Combien d'états finaux le produit (intersection) a-t-il parmi les états accessibles ?", len(K2.product(PB).final), "0", r"Il faudrait $(1,1)$, qui n'est pas accessible : l'intersection est vide.")],
    "z3": [_v(f"{fig(K1, P_K1)}\n\n{fig(K2, P_K2)}\n\n" + r"« nombre pair de $a$ » $\cap$ « finit par $a$ » est-il vide ? ($1$ oui, $0$ non)", int(K1.product(K2).shortest() is None), "0", r"$\mathtt{aa}$ appartient aux deux.")],
    "z4": [_v(f"{fig(K2, P_K2)}\n\n{fig(PB, P_PB)}\n\n" + r"Premier DFA « finit par $a$ », second « finit par $b$ ». Longueur du plus court mot de $L_1\setminus L_2$ ?", len(K2.product(PB, "minus").shortest()), "1", r"$\mathtt a$.")],
    "ex3": [_v(r"Alphabet $\{a,b\}$. Combien d'états le DFA complet minimal des mots qui contiennent $\mathtt{aba}$ comme facteur a-t-il ?", len(thompson("(a+b)*aba(a+b)*", "ab").remove_eps().determinize().minimal().Q), "4", r"On retient la longueur du plus long préfixe de $\mathtt{aba}$ suffixe du mot lu : $0,1,2$ ; l'état $3$ est final absorbant : $4$ états.")],
    "ex5": [_v(r"Combien d'états le DFA complet minimal de « la troisième lettre avant la fin est $a$ » a-t-il ?", len(N3.determinize().minimal().Q), "8", r"$2^3=8$.")],
    "ea5": [_v(r"Combien d'états le DFA complet minimal de $L=\{abc,cc\}$ a-t-il ?", len(thompson("abc+cc", "abc").remove_eps().determinize().minimal().Q), "5", r"États : début ; $a$ lu (attend $b$) ; $ab$ ou $c$ lu (les deux attendent $c$ : indistinguables) ; final ; puits : $5$.")],
    "eb3": [_v(r"Même algorithme sur $u=\mathtt{cabbababababc}$ : que vaut $c$ ?", occ(_DM, "cabbababababc"), "3", r"$\mathtt{abab}$ commence aux positions $5,7,9$ (chevauchements compris).")],
    "ec1": [_v(f"{fig(D3, P_D3)}\n\n" + r"$D_3$ accepte-t-il $\mathtt{11111}$ ? ($1$ oui, $0$ non)", int(D3.accepts("11111")), "0", r"$\mathtt{11111}=31=3\times10+1$ : on finit en l'état $1$.")],
    "ec3": [_v(r"Combien d'états le DFA minimal des multiples de $5$ en binaire a-t-il ?", len(mult(5).minimal().Q), "5", r"Le reste modulo $5$ : $5$ états, deux à deux distingués.")],
}
for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["id"] in VARIANTS:
            _e["variants"] = VARIANTS[_e["id"]]
for _e in EXTRA_PARTS:
    if _e["id"] in VARIANTS:
        _e["variants"] = VARIANTS[_e["id"]]


def _vf(notion, q, bonne):
    return {"notion": notion, "type": "vf", "q": q, "bonne": bonne}


def _qcm(notion, q, choix, bonne=0):
    return {"notion": notion, "type": "qcm", "q": q, "choix": choix, "bonne": bonne}


QUIZ = [
    _vf("ens", r"Un ensemble à $n$ éléments a $2^n$ parties.", True),
    _qcm("ens", r"$|A|=7$, $|B|=5$, $|A\cap B|=2$ : $|A\cup B|=$", [r"$10$", r"$12$", r"$14$", r"$9$"]),
    _vf("rec", r"Une récurrence demande un cas de base et une hérédité.", True),
    _qcm("rec", r"Nombre de mots de longueur $3$ sur $\{a,b\}$ :", [r"$8$", r"$6$", r"$9$", r"$3$"]),
    _vf("mots", r"La concaténation de mots est commutative.", False),
    _qcm("mots", r"$|w^k|=$", [r"$k|w|$", r"$|w|^k$", r"$|w|+k$", r"$k$"]),
    _vf("pref", r"$\varepsilon$ est préfixe, suffixe et facteur de tout mot.", True),
    _qcm("pref", r"Nombre de préfixes distincts de $\mathtt{abcd}$ (avec $\varepsilon$) :", [r"$5$", r"$4$", r"$10$", r"$11$"]),
    _vf("dist", r"La distance d'édition (insertions et suppressions) est symétrique.", True),
    _qcm("dist", r"$d_e(\mathtt{dog},\mathtt{bugs})=$", [r"$5$", r"$3$", r"$4$", r"$7$"]),
    _vf("lang", r"$\varepsilon\in L^*$ pour tout langage $L$.", True),
    _qcm("lang", r"$L=\{a,bc\}$ : $\mathrm{Pref}(L)=$", [r"$\{\varepsilon,a,b,bc\}$", r"$\{a,b,bc\}$", r"$\{\varepsilon,a,bc\}$", r"$\{a,bc\}$"]),
    _vf("rx-sem", r"L'intersection est un opérateur de la syntaxe des expressions rationnelles.", False),
    _qcm("rx-sem", r"$e^+$ est une abréviation de", [r"$ee^*$", r"$e^*e^*$", r"$\varepsilon+e$", r"$e+e$"]),
    _vf("rx-desc", r"$(a+b)^*\equiv a^*+b^*$.", False),
    _vf("rx-desc", r"$(e^*f^*)^*\equiv(e+f)^*$.", True),
    _qcm("rx-ecr", r"Une expression des mots de longueur paire sur $\{a,b\}$ :", [r"$((a+b)(a+b))^*$", r"$(a+b)^*$", r"$(a+b)(a+b)^*$", r"$(aa+bb)^*$"]),
    _vf("rx-ecr", r"$b^*ab^*ab^*$ décrit les mots avec exactement deux $a$.", True),
    _vf("afd", r"Dans un NFA, un seul chemin acceptant suffit pour accepter un mot.", True),
    _qcm("afd", r"Un DFA vérifie :", [r"un seul état initial et au plus une arête par lettre et état", r"aucune boucle", r"un seul état final", r"toutes les lettres sont utilisées"]),
    _vf("afd-build", r"Pour les multiples de $3$ en binaire, un DFA à $3$ états suffit.", True),
    _qcm("afd-build", r"Dans $D_3$ (multiples de $3$), $\delta(r,c)=$", [r"$(2r+c)\bmod3$", r"$(r+c)\bmod3$", r"$(r+2c)\bmod3$", r"$(2r)\bmod3$"]),
    _vf("compl", r"Pour échanger finaux et non finaux, le DFA doit être complet.", True),
    _qcm("compl", r"Un DFA complet à $n$ états sur $k$ lettres a", [r"$nk$ transitions", r"$n+k$ transitions", r"$k^n$ transitions", r"au plus $n$ transitions"]),
    _vf("thompson", r"L'automate de Thompson d'une expression à $n$ occurrences (lettres, $\varepsilon$, $\varnothing$, $+$, $*$) a $2n$ états.", True),
    _qcm("thompson", r"Dans l'automate de Thompson, l'étoile ajoute", [r"$i\to i_1$, $f_1\to f$, $i\to f$, $f_1\to i_1$", r"seulement $f_1\to i_1$", r"deux boucles", r"un état puits"]),
    _vf("eps", r"Après suppression des $\varepsilon$, le nombre d'états ne change pas.", True),
    _qcm("eps", r"$q$ devient final si", [r"sa $\varepsilon$-clôture contient un état final", r"il a une boucle", r"il est accessible", r"il est initial"]),
    _vf("emond", r"Un état utile est accessible et co-accessible.", True),
    _qcm("emond", r"Un état puits est", [r"accessible mais pas co-accessible", r"co-accessible mais pas accessible", r"utile", r"final"]),
    _vf("det", r"L'ensemble vide peut être un état du DFA déterminisé.", True),
    _qcm("det", r"Un NFA à $n$ états donne un DFA d'au plus", [r"$2^n$ états", r"$n^2$ états", r"$2n$ états", r"$n!$ états"]),
    _vf("min", r"Le DFA minimal d'un langage rationnel est unique (à renommage près).", True),
    _qcm("min", r"On commence l'algorithme de Moore avec les classes", [r"$F$ et $Q\setminus F$", r"une classe par état", r"$I$ et $Q\setminus I$", r"une seule classe"]),
    _vf("pomp", r"Un langage qui vérifie la conclusion du lemme de l'étoile est forcément rationnel.", False),
    _qcm("pomp", r"Pour prouver que $\{a^nb^n\}$ n'est pas rationnel, on pompe le mot", [r"$a^{n_0}b^{n_0}$", r"$a^{n_0}$", r"$b^{n_0}a^{n_0}$", r"$(ab)^{n_0}$"]),
    _vf("bmc", r"Lors de la suppression d'un état de boucle $z$, on insère $z^*$ entre l'arête entrante et l'arête sortante.", True),
    _qcm("bmc", r"Supprimer un état avec $2$ arêtes entrantes et $3$ sortantes crée", [r"$6$ arêtes", r"$5$ arêtes", r"$2$ arêtes", r"$3$ arêtes"]),
    _vf("stab", r"Le complément d'un langage rationnel est rationnel.", True),
    _qcm("stab", r"Dans le produit synchronisé de deux DFA complets, les états finaux de l'intersection sont les couples", [r"dont les deux composantes sont finales", r"dont une composante est finale", r"initiaux", r"dont aucune composante n'est finale"]),
]

_FL = {
    1: r"$|A\cup B|=|A|+|B|-|A\cap B|$ · $|A\times B|=|A||B|$ · $|\mathcal P(E)|=2^{|E|}$ · $\binom n2$",
    2: r"$\sum_{k=0}^n2^k=2^{n+1}-1$ · $k^n$ mots de longueur $n$ · principe des tiroirs",
    3: r"$|uv|=|u|+|v|$ · $|w^k|=k|w|$ · $|w|_a$ · $w^R$ · $\binom nk$ pour placer des lettres",
    4: r"$\mathrm{Pref}$, $\mathrm{Suff}$, $\mathrm{Fact}$ · $|\mathrm{Pref}(w)|=|w|+1$ · $\mathrm{Fact}(w)=\mathrm{Pref}(\mathrm{Suff}(w))$",
    5: r"$d_e(u,v)=|u|+|v|-2|\mathrm{PLSC}(u,v)|$ · séparation, symétrie, triangle",
    6: r"$L_1L_2=\{uv\}$ · $L^0=\{\varepsilon\}$ · $L^*=\bigcup L^n$ · $\mathrm{Pref}(L)$ · distributivité sur $\cup$",
    7: r"$L(e+f)=L(e)\cup L(f)$ · $L(ef)=L(e)L(f)$ · $L(e^*)=L(e)^*$ · $e^+=ee^*$ · $e?=\varepsilon+e$",
    8: r"$(ef)^*e\equiv e(fe)^*$ · $(e^*f^*)^*\equiv(e+f)^*$ · $e^{**}\equiv e^*$ · mot séparateur",
    9: r"blocs concaténés · $+$ pour les cas · $^*$ pour les répétitions · test sur mots courts et $\varepsilon$",
    10: r"chemin de $I$ à $F$ étiqueté $w$ · DFA : un chemin au plus · deux façons de refuser",
    11: r"un état = une information retenue · $(2r+c)\bmod3$ · NFA : deviner le début du motif",
    12: r"complet : $(n+1)k$ transitions avec puits · complément : échanger $F$ et $Q\setminus F$ (DFA complet)",
    13: r"atomes $a$, $\varepsilon$, $\varnothing$ · concaténation $f_1\xrightarrow\varepsilon i_2$ · $+$ et $*$ : 2 états, 4 $\varepsilon$ · $2n$ états",
    14: r"clôture$(q)=\{p\mid q\xrightarrow{\varepsilon^*}p\}$ · $q\xrightarrow ar$ si $p\xrightarrow ar$, $p\in$ clôture$(q)$ · final si clôture $\cap F\ne\varnothing$ · point fixe",
    15: r"accessible · co-accessible · utile = les deux · l'émondé garde les utiles",
    16: r"$S\xrightarrow aS_a$ · initial $I$ · final si $S\cap F\ne\varnothing$ · au plus $2^n$ états · $\varnothing$ est un état",
    17: r"partition initiale $F$, $Q\setminus F$ · raffiner selon les classes des successeurs · classes = états minimaux · mot distingueur",
    18: r"$xy^*z\subseteq L$, $y\ne\varepsilon$, $|xy|\le n_0$ · choisir $w$ puis $i$ tel que $xy^iz\notin L$ · principe des tiroirs",
    19: r"$p\xrightarrow xq\xrightarrow yr$, boucle $z$ : $p\xrightarrow{xz^*y}r$ · entrantes $\times$ sortantes · $+$ pour les arêtes parallèles",
    20: r"produit synchronisé $(p,q)$ · $\cap$ : les deux finaux · vide : parcours · $L_1\setminus L_2=L_1\cap\overline{L_2}$",
    21: r"Thompson $\to$ retour arrière $\to$ émondage $\to$ sous-ensembles $\to$ Moore · BMC · produit",
    22: r"intersection avec $a^*b^*$ · complément · produit et parcours en largeur · $2^n$ états",
}
FORMULES = {e["id"]: _FL[lvl["n"]] for lvl in LEVELS for e in lvl["exos"] if e["kind"] != "multi"}
FORMULES.update({
    "ea2": _FL[14], "ea3": _FL[15], "ea4": _FL[16], "ea5": _FL[17], "eb1": _FL[11], "eb3": _FL[16], "eb4": _FL[16],
    "ec1": _FL[11], "ec2": r"invariant : état $=\mathrm{val}(w)\bmod3$ · $\mathrm{val}(wc)=2\,\mathrm{val}(w)+c$", "ec3": _FL[17], "ec4": _FL[11],
})

assert len(CHECKED) == len(set(CHECKED)), "duplicate exercise id"
