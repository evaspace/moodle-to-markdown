"""Level path: S3 algorithmics, general trees and B-trees (ECUE ARB2, Arbres et Recherches 2, Python).

Moodle course « [algo] Arbres et Recherches 2 », chapters `06_🐍 Arbres généraux - General Trees` (implementations
tuple / premier fils - frère droit, methods) and `07_🐍 B-arbres - B-Trees` (split, merge, rotations, insertion and
deletion examples), TD 1 (arbres généraux) and TD 2 (B-arbres), DM « 1.2 - Arbres généraux ». Hashing (chapters 02 to 05)
is another path. Calibrated on the Epidocs midterms `annales/raw/S3/Midterms/Algo`: C3 of November 2019 (folder 2023:
average arity, B-tree insertions, `build` mystery), C3 of 9 November 2021 (folder 2025: morechildren, decrease, insertion
and deletion in degree 2, `mystery` = ordered B-tree test, official corrections) and exam B5 of 22 October 2024 (folder
2028, subject only: internal average depth, same arity, B-tree insertions/deletion, `what`; no official correction).
Levels 1 and 2 are reminders of S1/S2 (binary trees, BST, AVL) needed here.

Checks at import (build.py imports this module, so a wrong answer stops the build):
- B-trees are written as `N(keys, *children)` and every state shown (insertions, deletions, counts, heights) is computed by
  `insert`/`delete` below, which are first checked against the official answers of the 2019 and 2021 midterms;
- general trees are tuples `(key, [children])` (a bare key is a leaf); every measure/order is computed from the tuple;
- `wg()` runs the model code on `Tree` / `TreeAsBin` objects built from the figures and replays the `>>>` session;
- figures are SVG files in `static/arbres/` (same mechanism as the S2 path, B-tree nodes drawn as boxes of keys).
Conventions stated in every exercise: height of the root = 0, B-tree of degree t: t-1 to 2t-1 keys per node (root: 1 to
2t-1), insertion with « principe de précaution » (split on the way down), deletion with the left side preferred.
"""
import bisect
import collections
import contextlib
import hashlib
import html
import io
from fractions import Fraction

from .algo_abg import (FIG_DIR, FIG_URL, _gwalk, fig, gbfs, gch, gfig, gkey, gpost, gpre, key, kids, measures,
                       ino)
from .algo_python import _out, _py, _session

SUBJECT = {
    "id": "algo-s3-arbres",
    "ordre": 685,
    "matiere": "algo",
    "semestre": "S3",
    "ecue": "AR2",
    "titre": "Arbres généraux et B-arbres",
    "chapitres_moodle": ["06_🐍 Arbres généraux - General Trees", "07_🐍 B-arbres - B-Trees"],
    "td": "TD 1 arbres généraux et TD 2 B-arbres (S3 2026), DM 1.2 arbres généraux",
    "examens": ["Examen B5 d'algorithmique, Arbres et Recherches 2 (octobre, Python, 2 h)"],
}

CHECKED = []

# ---------------------------------------------------------------- general trees (classes of the exam annex)


class Tree:
    def __init__(self, key, children=None):
        self.key = key
        self.children = children if children is not None else []
        self.nbchildren = len(self.children)


class TreeAsBin:
    def __init__(self, key, child=None, sibling=None):
        self.key = key
        self.child = child
        self.sibling = sibling


class Queue:
    def __init__(self):
        self._d = collections.deque()

    def enqueue(self, e):
        self._d.append(e)

    def dequeue(self):
        return self._d.popleft()

    def isempty(self):
        return not self._d


def tree_obj(g):
    return Tree(gkey(g), [tree_obj(c) for c in gch(g)])


def _chain(cs):
    nxt = None
    for c in reversed(cs):
        nxt = TreeAsBin(gkey(c), _chain(gch(c)), nxt)
    return nxt


def tab_obj(g):
    return TreeAsBin(gkey(g), _chain(gch(g)), None)


def gsize(g):
    return len(gpre(g))


def gheight(g):
    return max(d for _, d, _ in _gwalk(g))


def garity(g):
    return max(c for _, _, c in _gwalk(g))


def gleaves(g):
    return sum(1 for _, _, c in _gwalk(g) if c == 0)


def glinear(g):
    return f"({gkey(g)}{''.join(glinear(c) for c in gch(g))})"


def g_from_linear(s):
    """Inverse of glinear (keys without spaces or parentheses): '(1(2)(3))' -> spec."""
    pos = 0

    def tree():
        nonlocal pos
        assert s[pos] == "("
        pos += 1
        j = pos
        while s[pos] not in "()":
            pos += 1
        k = int(s[j:pos])
        ch = []
        while s[pos] == "(":
            ch.append(tree())
        assert s[pos] == ")"
        pos += 1
        return (k, ch) if ch else k

    g = tree()
    assert pos == len(s)
    return g


def fcrs_bin(g):
    """First child - right sibling binary form (spec for algo_abg.fig) of a general tree."""
    def forest(cs):
        if not cs:
            return None
        c = cs[0]
        left, right = forest(gch(c)), forest(cs[1:])
        return gkey(c) if left is None and right is None else (gkey(c), left, right)
    return forest([g])


class BTree:
    degree = 2

    def __init__(self, keys, children=None):
        self.keys = list(keys)
        self.children = list(children or [])

    @property
    def nbkeys(self):
        return len(self.keys)


def btree_obj(n):
    return BTree(n.keys, [btree_obj(c) for c in n.ch])


def node_of(b):
    return Node(b.keys, [node_of(c) for c in b.children])


def binary_search_pos(L, x):
    """Annex function of the exam: position of x in the sorted list L, or where it should be."""
    return bisect.bisect_left(L, x)


def split(B, i):
    """Annex procedure of the exam: split the full child i of B (degree BTree.degree)."""
    t = BTree.degree
    c = B.children[i]
    right = BTree(c.keys[t:], c.children[t:])
    B.keys.insert(i, c.keys[t - 1])
    B.children.insert(i + 1, right)
    c.keys, c.children = c.keys[:t - 1], c.children[:t]


def _wg(enonce, code, tests, sol, trees, tabs, figs, btrees=None, check=None, extra=""):
    code = code.strip()
    ns = {"Tree": Tree, "TreeAsBin": TreeAsBin, "Queue": Queue, "BTree": BTree, "split": split,
          "binary_search_pos": binary_search_pos, "search_pos": binary_search_pos}
    ns.update({k: tree_obj(g) for k, g in trees.items()})
    ns.update({k: tab_obj(g) for k, g in tabs.items()})
    for k, (nd, deg) in (btrees or {}).items():
        BTree.degree = deg
        ns[k] = btree_obj(nd)
    exec(code + "\n\n" + extra, ns)
    for line, exp in tests:
        with contextlib.redirect_stdout(io.StringIO()):
            got = repr(eval(line, ns))
        assert got == exp, f"{line}: got {got}, expected {exp}\n{code}"
    if check:
        check(ns)
    text = enonce
    if figs:
        text += "\n\n" + figs
    if tests:
        text += f"\n\nExemples d'applications :\n\n{_out(_session(tests))}"
    return {"enonce": text, "sol": _py(code) + (f"\n\n{sol}" if sol else "")}


def wg(id, enonce, code, tests, sol="", trees=None, tabs=None, figs=None, src=None, duree=8, btrees=None, check=None, extra=""):
    """« Write the function » exercise on general trees / B-trees: the model code replays the session on the figures
    (`figs` = Markdown of the figure(s), built with gfig / bfig)."""
    CHECKED.append(id)
    d = {"id": id, "kind": "open", **_wg(enonce, code, tests, sol, trees or {}, tabs or {}, figs, btrees, check, extra)}
    if src:
        d["src"] = src
    d["duree"] = duree
    return d


# ---------------------------------------------------------------- B-trees


class Node:
    def __init__(self, keys, ch=None):
        self.keys = list(keys)
        self.ch = list(ch or [])

    def leaf(self):
        return not self.ch


def N(keys, *children):
    return Node(keys, children)


def cp(n):
    return Node(n.keys, [cp(c) for c in n.ch])


def _split(n, i, t, log):
    c = n.ch[i]
    assert len(c.keys) == 2 * t - 1
    right = Node(c.keys[t:], c.ch[t:])
    up = c.keys[t - 1]
    c.keys, c.ch = c.keys[:t - 1], c.ch[:t]
    n.keys.insert(i, up)
    n.ch.insert(i + 1, right)
    log.append(("split", up))


def _ins(n, x, t, log):
    i = bisect.bisect_left(n.keys, x)
    if i < len(n.keys) and n.keys[i] == x:
        return False
    if n.leaf():
        n.keys.insert(i, x)
        return True
    if len(n.ch[i].keys) == 2 * t - 1:
        if n.ch[i].keys[t - 1] == x:
            return False
        _split(n, i, t, log)
        if x > n.keys[i]:
            i += 1
    return _ins(n.ch[i], x, t, log)


def insert(root, x, t, log=None):
    """Insertion « à la descente » (principe de précaution): every full node met on the way down is split first."""
    log = [] if log is None else log
    if root is None:
        return N([x])
    root = cp(root)
    if len(root.keys) == 2 * t - 1:
        root = Node([], [root])
        _split(root, 0, t, log)
    _ins(root, x, t, log)
    return root


def _merge(n, i, log):
    """Merge children i and i+1 of n with the separator n.keys[i]."""
    a, b = n.ch[i], n.ch[i + 1]
    log.append(("merge", n.keys[i]))
    a.keys += [n.keys.pop(i)] + b.keys
    a.ch += b.ch
    n.ch.pop(i + 1)


def _fix(n, i, t, log):
    """Child i has t-1 keys: give it one more (rotation from the left sibling first, then the right one), else merge."""
    c = n.ch[i]
    if i > 0 and len(n.ch[i - 1].keys) >= t:
        s = n.ch[i - 1]
        down = n.keys[i - 1]
        c.keys.insert(0, down)
        n.keys[i - 1] = s.keys.pop()
        if s.ch:
            c.ch.insert(0, s.ch.pop())
        log.append(("rotate-right", down, n.keys[i - 1]))
        return i
    if i < len(n.ch) - 1 and len(n.ch[i + 1].keys) >= t:
        s = n.ch[i + 1]
        down = n.keys[i]
        c.keys.append(down)
        n.keys[i] = s.keys.pop(0)
        if s.ch:
            c.ch.append(s.ch.pop(0))
        log.append(("rotate-left", down, n.keys[i]))
        return i
    if i > 0:
        _merge(n, i - 1, log)
        return i - 1
    _merge(n, i, log)
    return i


def _del(n, x, t, log):
    i = bisect.bisect_left(n.keys, x)
    if i < len(n.keys) and n.keys[i] == x:
        if n.leaf():
            n.keys.pop(i)
            return True
        l, r = n.ch[i], n.ch[i + 1]
        if len(l.keys) >= t:
            m = l
            while m.ch:
                m = m.ch[-1]
            n.keys[i] = m.keys[-1]
            log.append(("pred", m.keys[-1]))
            return _del(l, m.keys[-1], t, log)
        if len(r.keys) >= t:
            m = r
            while m.ch:
                m = m.ch[0]
            n.keys[i] = m.keys[0]
            log.append(("succ", m.keys[0]))
            return _del(r, m.keys[0], t, log)
        _merge(n, i, log)
        return _del(n.ch[i], x, t, log)
    if n.leaf():
        return False
    if len(n.ch[i].keys) == t - 1:
        i = _fix(n, i, t, log)
    return _del(n.ch[i], x, t, log)


def delete(root, x, t, log=None):
    """Deletion « à la descente »: a child with t-1 keys is fed (rotation) or merged before the descent; left preferred."""
    log = [] if log is None else log
    root = cp(root)
    _del(root, x, t, log)
    if not root.keys and root.ch:
        root = root.ch[0]
    return root


def bkeys(n):
    if n.leaf():
        return list(n.keys)
    out = []
    for i, c in enumerate(n.ch):
        out += bkeys(c) + n.keys[i:i + 1]
    return out


def bheight(n):
    h = 0
    while n.ch:
        n, h = n.ch[0], h + 1
    return h


def bcount(n):
    return 1 + sum(bcount(c) for c in n.ch)


def bsize(n):
    return len(n.keys) + sum(bsize(c) for c in n.ch)


def bspec(n):
    return n.keys if n.leaf() else (n.keys, [bspec(c) for c in n.ch])


def btext(n):
    """One-line text form of a B-tree: [k1 k2 (child) (child) ...] ."""
    return "[" + " ".join(map(str, n.keys)) + "]" if n.leaf() else (
        "[" + " ".join(map(str, n.keys)) + " : " + " ".join(btext(c) for c in n.ch) + "]")


def levels_b(n):
    out, cur = [], [n]
    while cur:
        out.append(cur)
        cur = [c for x in cur for c in x.ch]
    return out


def valid(n, t, root=True):
    """B-tree of degree t: key counts, ordering, equal leaf depth."""
    ks = n.keys
    assert ks == sorted(ks) and len(set(ks)) == len(ks), "keys not sorted"
    assert len(ks) <= 2 * t - 1 and len(ks) >= (1 if root else t - 1), f"bad key count in {ks}"
    if n.leaf():
        return 0
    assert len(n.ch) == len(ks) + 1
    hs = {valid(c, t, False) for c in n.ch}
    assert len(hs) == 1, "leaves at different depths"
    for i, c in enumerate(n.ch):
        cs = bkeys(c)
        assert (i == 0 or cs[0] > ks[i - 1]) and (i == len(ks) or cs[-1] < ks[i]), "order broken"
    return hs.pop() + 1


def build_b(keys, t):
    r = None
    for k in keys:
        r = insert(r, k, t)
    valid(r, t)
    return r


def steps_ins(root, xs, t):
    """[(x, tree after, log)] for successive insertions."""
    out = []
    for x in xs:
        lg = []
        root = insert(root, x, t, lg)
        valid(root, t)
        out.append((x, root, lg))
    return out


def steps_del(root, xs, t):
    out = []
    for x in xs:
        assert x in bkeys(root), f"{x} absent"
        lg = []
        root = delete(root, x, t, lg)
        valid(root, t)
        out.append((x, root, lg))
    return out


# figures ---------------------------------------------------------------------------------------------

_CW, _GAP, _BH, _LV = 19, 10, 22, 46


def _bx(n, d, acc, cnt):
    """Layout: returns node index; leaves take consecutive slots, parents sit above their children."""
    w = len(n.keys) * _CW + 8
    idx = len(acc)
    acc.append(None)
    cis = [_bx(c, d + 1, acc, cnt) for c in n.ch]
    if cis:
        x = (acc[cis[0]][0] + acc[cis[-1]][0] + acc[cis[-1]][2] - w) / 2
    else:
        x = cnt[0]
        cnt[0] += w + _GAP
    acc[idx] = (x, d, w, n, cis)
    return idx


def bfig(*items):
    """Markdown image of one or more B-trees: items = (caption, root) pairs; key boxes, children hang below the separators."""
    parts, x0, y0, row_h, width = [], 8, 6, 0, 0
    for cap, root in items:
        acc = []
        cnt = [0]
        _bx(root, 0, acc, cnt)
        w = max(x + ww for x, _, ww, _, _ in acc)
        h = (max(d for _, d, _, _, _ in acc) + 1) * _LV + (22 if cap else 0)
        if x0 > 8 and x0 + w > 520:
            x0, y0, row_h = 8, y0 + row_h + 8, 0
        for x, d, ww, nd, cis in acc:
            bx, by = x0 + x, y0 + d * _LV
            parts.append(f'<rect x="{bx:.1f}" y="{by}" width="{ww}" height="{_BH}" rx="2"/>')
            for j, k in enumerate(nd.keys):
                parts.append(f'<text x="{bx + 4 + j * _CW + _CW / 2:.1f}" y="{by + 15}">{html.escape(str(k))}</text>')
                if j:
                    parts.append(f'<line class="s" x1="{bx + 4 + j * _CW:.1f}" y1="{by}" x2="{bx + 4 + j * _CW:.1f}" y2="{by + _BH}"/>')
            for j, ci in enumerate(cis):
                cx, cd, cw, _, _ = acc[ci]
                parts.append(f'<line x1="{bx + 4 + j * _CW:.1f}" y1="{by + _BH}" x2="{x0 + cx + cw / 2:.1f}" y2="{y0 + cd * _LV}"/>')
        if cap:
            parts.append(f'<text class="c" x="{x0 + w / 2:.1f}" y="{y0 + h - 4:.1f}">{html.escape(cap)}</text>')
        x0 += w + 24
        row_h = max(row_h, h)
        width = max(width, x0)
    W, H = int(width - 14), int(y0 + row_h + 6)
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
           'font-family="JetBrains Mono, Menlo, Consolas, monospace" font-size="13" text-anchor="middle">'
           '<style>line{stroke:#111;stroke-width:1.2}line.s{stroke-width:.8}rect{fill:#fff;stroke:#111;stroke-width:1.4}'
           'text{fill:#111}.c{font-size:14px;font-weight:700}</style>' + "".join(parts) + "</svg>")
    name = "bt-" + hashlib.sha1(svg.encode()).hexdigest()[:12] + ".svg"
    path = FIG_DIR / name
    if not path.exists() or path.read_text() != svg:
        FIG_DIR.mkdir(parents=True, exist_ok=True)
        path.write_text(svg)
    alt = " ; ".join((f"{c} = " if c else "") + btext(r) for c, r in items).replace("[", "(").replace("]", ")")
    return f"![{alt}]({FIG_URL}{name})"


# ---------------------------------------------------------------- binary trees, BST, AVL (S1/S2 reminders)


def _mk(k, l, r):
    return k if l is None and r is None else (k, l, r)


def bst_insert(s, x):
    if s is None:
        return x
    k, (l, r) = key(s), kids(s)
    return _mk(k, bst_insert(l, x), r) if x < k else _mk(k, l, bst_insert(r, x))


def bst(seq):
    s = None
    for x in seq:
        s = bst_insert(s, x)
    return s


def hb(s):
    return -1 if s is None else 1 + max(hb(kids(s)[0]), hb(kids(s)[1]))


ROT = [0]


def _avl_bal(k, l, r):
    if hb(l) - hb(r) > 1:
        ROT[0] += 1
        lk, (ll, lr) = key(l), kids(l)
        if hb(ll) >= hb(lr):
            return _mk(lk, ll, _mk(k, lr, r))
        ROT[0] += 1
        mk_, (a, b) = key(lr), kids(lr)
        return _mk(mk_, _mk(lk, ll, a), _mk(k, b, r))
    if hb(r) - hb(l) > 1:
        ROT[0] += 1
        rk, (rl, rr) = key(r), kids(r)
        if hb(rr) >= hb(rl):
            return _mk(rk, _mk(k, l, rl), rr)
        ROT[0] += 1
        mk_, (a, b) = key(rl), kids(rl)
        return _mk(mk_, _mk(k, l, a), _mk(rk, b, rr))
    return _mk(k, l, r)


def avl_insert(s, x):
    if s is None:
        return x
    k, (l, r) = key(s), kids(s)
    return _avl_bal(k, avl_insert(l, x), r) if x < k else _avl_bal(k, l, avl_insert(r, x))


def avl(seq):
    ROT[0] = 0
    s = None
    for x in seq:
        s = avl_insert(s, x)
    return s


def avl_min(h):
    a, b = 1, 2  # N(0), N(1)
    for _ in range(h - 1):
        a, b = b, a + b + 1
    return a if h == 0 else b


# ---------------------------------------------------------------- exercise builders

SRC_TD = "TD 1 arbres généraux, TD 2 B-arbres et exemples d'insertion/suppression (cours Moodle AR2, S3 2026)"


def tex(a):
    a = Fraction(a) if isinstance(a, Fraction) else a
    if isinstance(a, Fraction) and a.denominator != 1:
        return rf"\dfrac{{{a.numerator}}}{{{a.denominator}}}"
    return str(a)


def v(id, enonce, ans, sol, src=None, duree=3):
    """Value exercise; `ans` is computed (int, Fraction), never typed by hand."""
    a = str(ans)
    e = {"id": id, "kind": "value", "enonce": enonce, "calc": a, "ans": a, "sol": f"**Réponse :** ${tex(ans)}$\n\n{sol}",
         "duree": duree}
    if src:
        e["src"] = src
    return e


def vv(enonce, ans, sol):
    a = str(ans)
    return {"enonce": enonce, "calc": a, "ans": a, "sol": f"**Réponse :** ${tex(ans)}$\n\n{sol}"}


def o(id, enonce, sol, src=None, duree=6):
    e = {"id": id, "kind": "open", "enonce": enonce, "sol": sol, "duree": duree}
    if src:
        e["src"] = src
    return e


def kx(keys):
    return "$[" + r"\;".join(map(str, keys)) + "]$"


def lst(L):
    return ", ".join(map(str, L))


def depth_of(g, k):
    return next(d for kk, d, _ in _gwalk(g) if kk == k)


def gmeasure_sol(g):
    return (f"$T={gsize(g)}$ nœuds, $N_e={gleaves(g)}$ feuilles, $N_i={gsize(g) - gleaves(g)}$ nœuds internes, "
            f"hauteur ${gheight(g)}$, arité ${garity(g)}$.")


def explain(lg):
    out = []
    for e in lg:
        if e[0] == "split":
            out.append(f"éclatement d'un nœud plein : la clé ${e[1]}$ monte")
        elif e[0] == "rotate-right":
            out.append(f"rotation droite (emprunt au frère gauche) : ${e[1]}$ descend, ${e[2]}$ monte")
        elif e[0] == "rotate-left":
            out.append(f"rotation gauche (emprunt au frère droit) : ${e[1]}$ descend, ${e[2]}$ monte")
        elif e[0] == "merge":
            out.append(f"fusion des deux fils autour de ${e[1]}$ (la clé descend)")
        elif e[0] == "pred":
            out.append(f"clé interne remplacée par son prédécesseur ${e[1]}$")
        elif e[0] == "succ":
            out.append(f"clé interne remplacée par son successeur ${e[1]}$")
    return " ; ".join(out) if out else "aucune transformation, la clé est simplement ajoutée ou retirée dans une feuille"


def show_ins(start, xs, t):
    """Markdown of the successive states of insertions (each one computed by `insert`)."""
    out = []
    for x, r, lg in steps_ins(start, xs, t):
        out.append(f"**Insertion de ${x}$** : {explain(lg)}.\n\n{bfig(('', r))}")
    return "\n\n".join(out)


def show_del(start, xs, t):
    out, prev = [], start
    for x, r, lg in steps_del(start, xs, t):
        note = " ; la racine vide disparaît, la hauteur diminue de 1" if bheight(r) < bheight(prev) else ""
        out.append(f"**Suppression de ${x}$** : {explain(lg)}{note}.\n\n{bfig(('', r))}")
        prev = r
    return "\n\n".join(out)


def final_ins(start, xs, t):
    r = start
    for x in xs:
        r = insert(r, x, t)
    valid(r, t)
    return r


def final_del(start, xs, t):
    r = start
    for x in xs:
        r = delete(r, x, t)
    valid(r, t)
    return r


def count_ops(steps, kind):
    return sum(1 for _, _, lg in steps for e in lg if e[0] == kind)


CONV_B = (r"Conventions du cours : B-arbre de degré $t$ (un nœud porte de $t-1$ à $2t-1$ clés, la racine de $1$ à $2t-1$) ; "
          r"insertion et suppression « à la descente » (principe de précaution).")
CONV_D = (r"Pour une suppression, on préfère le côté gauche : rotation avec le frère gauche avant le frère droit, "
          r"prédécesseur avant successeur, fusion avec le frère gauche.")
CONV_H = r"Convention : la racine est à la profondeur $0$ ; la hauteur d'un arbre est la profondeur maximale de ses nœuds."

# ---------------------------------------------------------------- data

TB1 = (8, (3, 1, (6, 4, 7)), (10, None, (14, 13, None)))
TB2 = (20, (10, (5, 2, None), 15), (30, None, (40, 35, 50)))
TB3 = (1, (2, (4, 8, 9), 5), (3, 6, (7, None, 10)))

G1 = (1, [(2, [6, (7, [(14, [18]), 15])]), (3, [8]), (4, [9, 10, (11, [16, 17]), 12]), (5, [13])])  # C3 2019, ex. 2
G24 = (10, [(2, [0, 1, 9, 4]), 5, (8, [(7, [(6, [3, 11])])])])  # exam B5 2024, ex. 2
GA = (20, [(5, [1, 2]), (6, [(3, [7]), 8, 9]), 4])
GB = (1, [(2, [(5, [(9, [10])]), 6]), (3, [7]), 4])
GC = (7, [(1, [(2, [3, 4]), 5, (6, [8])]), 9])
GD = (50, [(10, [20, (30, [40, 60])]), (70, [80]), 90, (5, [15, 25])])
G_TD = g_from_linear("(12(2(25)(6)(-7))(0(18(1)(8))(9))(4(3)(11)))")  # TD 1, ex. 3.1
G_PS = ("A", [("B", ["E", "F"]), ("C", ["G", "H", "I"]), ("D", ["J"])])  # C3 2017, prefsuff

BTD = N([22], N([15], N([8, 12]), N([18, 19, 20])), N([27, 41], N([24, 25]), N([30, 35, 38]), N([45, 48])))  # TD 2 fig. 2
for _b, _t in ((BTD, 2),):
    valid(_b, _t)
BT_C3 = BTD  # C3 2019 figure 2 is the same tree
B21_INS = N([10, 21, 38], N([3, 7]), N([14, 17]), N([23, 25, 29]), N([40, 51]))  # C3 2021 fig. 3
B21_DEL = N([22], N([15], N([8]), N([18, 19, 20])), N([27, 41], N([24, 25]), N([30, 35, 38]), N([45, 48])))  # fig. 4
B21_MYS = N([20], N([8, 15], N([1, 2, 4, 5]), N([9, 13]), N([16, 18, 19])),
            N([26, 41, 53], N([23, 25]), N([27, 34, 35, 42]), N([43, 48, 51, 52]), N([62, 65, 77])))  # fig. 5 (degree 3), NOT ordered on purpose (42 > 41)
B24_INS = N([5, 40], N([0, 2, 4]), N([10, 12]), N([42, 45]))  # exam 2024 fig. 1
B24_DEL = N([41], N([22], N([15], N([8, 12]), N([18, 20])), N([27], N([24, 25]), N([30, 35]))),
            N([50], N([45, 48], N([44]), N([46]), N([49])), N([71], N([66]), N([80]))))  # exam 2024 fig. 2
B24_WHAT = N([40], N([7, 20, 35], N([2, 5, 6]), N([13, 14, 15, 16]), N([22, 27, 29, 30]), N([36, 39])),
             N([72, 83], N([42, 51]), N([79, 81]), N([87, 91, 93, 96, 99])))  # exam 2024 fig. 3 (degree 3)
for _b, _t in ((B21_INS, 2), (B21_DEL, 2), (B24_INS, 2), (B24_DEL, 2), (B24_WHAT, 3)):
    valid(_b, _t)

# official answers of the corrections (checked against `insert` / `delete`)
_o19 = N([22, 35], N([15], N([8, 12]), N([18, 19, 20])), N([27], N([24, 25]), N([30])), N([41], N([36, 38]), N([42, 45, 48])))
_o21i = N([21], N([10, 14], N([3, 7]), N([11]), N([17, 20])), N([25, 38], N([23]), N([29, 32]), N([40, 51])))
_o21d = N([27], N([18, 22], N([8]), N([19, 20]), N([24, 25])), N([41], N([30, 35, 38]), N([45, 48])))
assert btext(final_ins(BT_C3, [36, 42], 2)) == btext(_o19)
assert btext(final_ins(B21_INS, [11, 32, 20], 2)) == btext(_o21i)
assert btext(final_del(B21_DEL, [15], 2)) == btext(_o21d)


# ---------------------------------------------------------------- notions

NOTIONS = [
    {"id": "bin", "titre": "Rappel S2 : arbres binaires, mesures (taille, hauteur, feuilles)",
     "formule": r"$T$ : nombre de nœuds · hauteur : racine $=0$, arbre vide $=-1$ · feuille : aucun fils · au plus $2^{h+1}-1$ nœuds · $LC=\sum$ des profondeurs",
     "exemple": r"$\langle 8,\langle3,1,6\rangle,10\rangle$ : $T=5$, $h=2$, $N_e=3$ feuilles, $LC=0+1+1+2+2=6$",
     "cours": r"Rappel S2 : parcours « Arbres binaires et généraux » (`algo-s2-abg`). Un arbre binaire est vide ou formé d'une racine et de deux sous-arbres. La profondeur d'un nœud compte les liens depuis la racine ; la hauteur de l'arbre est la plus grande profondeur. Un arbre de hauteur $h$ a au plus $2^{h+1}-1$ nœuds."},
    {"id": "abr", "titre": "Rappel S1/S2 : arbres binaires de recherche et AVL",
     "formule": r"ABR : clés de $G$ $<$ racine $<$ clés de $D$, parcours infixe $=$ ordre croissant · AVL : $|h(G)-h(D)|\le1$ en tout nœud · $N(h)=N(h-1)+N(h-2)+1$ nœuds au minimum, $N(0)=1$, $N(1)=2$ · rotation : conserve l'ordre infixe",
     "exemple": r"Insertion de $4,2,6,1,3$ : racine $4$, infixe $1,2,3,4,6$ ; un AVL de hauteur $4$ a au moins $12$ nœuds",
     "cours": r"Un ABR s'obtient par insertions successives en feuille ; sa forme dépend de l'ordre des insertions. Un AVL se rééquilibre par rotations (simple ou double) quand le déséquilibre atteint $2$. Les B-arbres du cours généralisent l'ABR (plusieurs clés par nœud) et reprennent l'idée des rotations pour la suppression."},
    {"id": "gen-mes", "titre": "Arbres généraux : vocabulaire et mesures",
     "formule": r"arbre général $=$ racine $+$ liste de fils (jamais vide) · arité d'un nœud : nombre de fils · arité de l'arbre : maximum · $\text{arcs}=T-1=\sum\text{arités}$ · arité moyenne $=\frac{T-1}{N_i}$ · $PMI=\frac{LCI}{N_i}$",
     "exemple": r"Arbre à $18$ nœuds dont $8$ internes : $17$ arcs, arité moyenne $\frac{17}8=2{,}125$",
     "cours": r"Un arbre général n'est jamais vide. Un nœud interne a au moins un fils, une feuille aucun. La taille est le nombre de nœuds, la hauteur la profondeur maximale (racine à $0$). L'arité moyenne se calcule sur les nœuds internes seulement : on divise le nombre total de fils par $N_i$."},
    {"id": "gen-rep", "titre": "Représentations : n-uplets, premier fils - frère droit, forme linéaire",
     "formule": r"tuple : `T.key`, `T.children` (liste), `T.nbchildren` · premier fils - frère droit : `B.key`, `B.child`, `B.sibling` · linéaire : $A=\langle o,A_1,\dots,A_N\rangle\to$ `(o A1 ... AN)`",
     "exemple": r"$\langle1,2,\langle3,4\rangle\rangle$ s'écrit `(1(2)(3(4)))` ; en premier fils - frère droit, `B.child` $=2$, `2.sibling` $=3$, `3.child` $=4$",
     "cours": r"Les deux implémentations représentent le même arbre. Pour parcourir les fils : `for C in T.children` (n-uplets) ou `C = B.child` puis `C = C.sibling` jusqu'à `None` (premier fils - frère droit). Dans la forme binaire, `child` vaut `None` pour une feuille et `sibling` pour un dernier fils ; la racine n'a jamais de frère. Le nombre de `sibling` non vides est $T-1-N_i$."},
    {"id": "gen-par", "titre": "Parcours : préfixe, suffixe, largeur",
     "formule": r"préfixe : racine puis fils de gauche à droite · suffixe : fils puis racine · largeur : niveau par niveau (file) · $T$ lignes « fin » dans un parcours qui en imprime une par appel",
     "exemple": r"$\langle1,\langle2,5\rangle,3\rangle$ : préfixe $1,2,5,3$ ; suffixe $5,2,3,1$ ; largeur $1,2,3,5$",
     "cours": r"Parcours profondeur $=$ récursion : on exprime la solution à partir des sous-arbres. Largeur $=$ file ; pour repérer les changements de niveau, on enfile un marqueur (`None`) après chaque niveau et on ne le réenfile que si la file n'est pas vide. Le parcours suffixe d'un arbre général correspond au parcours infixe de sa forme binaire premier fils - frère droit."},
    {"id": "gen-code", "titre": "Écrire une fonction sur un arbre général",
     "formule": r"profondeur ou largeur ? · parcours interrompu ? · récupérer le résultat des appels · `taille` $=1+\sum$ tailles des fils · `hauteur` $=1+\max$ hauteurs des fils (feuille : $0$)",
     "exemple": r"`size(T)` : `1 + sum` des `size(C)` pour `C` dans `T.children` ; en premier fils - frère droit : boucle `C = B.child ... C = C.sibling`",
     "cours": r"Méthode du cours : (1) quel parcours ? un parcours profondeur donne une fonction récursive, la largeur une file ; (2) le parcours peut-il être interrompu (recherche, test de propriété) ? Dans ce cas on ne retourne jamais directement l'appel récursif : on teste son résultat et on s'arrête seulement quand la réponse est connue ; (3) un résultat retourné qui n'est pas utilisé est perdu. Il faut penser à passer en paramètre ce dont les fils ont besoin (profondeur, arité du père) et à renvoyer un couple quand on remonte deux valeurs."},
    {"id": "bt-def", "titre": "B-arbres : définition, nombre de clés, hauteur",
     "formule": r"degré $t$ : $t-1\le$ clés $\le2t-1$ par nœud (racine : $1$ à $2t-1$) · un nœud à $k$ clés a $k+1$ fils · feuilles toutes à la même profondeur · $n\ge2t^h-1$ donc $h\le\log_t\frac{n+1}2$ · au plus $(2t)^{h+1}-1$ clés",
     "exemple": r"$t=3$, $h=2$ : au plus $6^3-1=215$ clés, au moins $2\times3^2-1=17$",
     "cours": r"Un B-arbre de degré $t$ (ou ordre $t$) est un arbre de recherche équilibré : les clés d'un nœud sont triées, le fils $i$ contient les clés comprises entre les clés $i-1$ et $i$, et toutes les feuilles sont à la même profondeur. Un nœud à $2t-1$ clés est plein (un « $2t$-nœud »). Pour $t=2$ on retrouve l'arbre 2-3-4. Le minimum de clés pour une hauteur $h$ : racine à une clé, deux fils, puis chaque nœud a au moins $t$ fils, d'où $1+2(t-1)\frac{t^h-1}{t-1}=2t^h-1$. Valeur minimum : clé la plus à gauche de la feuille la plus à gauche ; maximum : la plus à droite de la feuille la plus à droite."},
    {"id": "bt-lect", "titre": "B-arbres : recherche, parcours croissant, prédécesseur",
     "formule": r"recherche : `i = binary_search_pos(B.keys, x)` puis clé trouvée ou fils `i` · parcours croissant : fils $0$, clé $0$, fils $1$, clé $1$, ... · prédécesseur de la clé $i$ d'un nœud interne : clé la plus à droite du fils $i$",
     "exemple": r"Racine $[40]$, fils gauche $[7\;20\;35]$ : le prédécesseur de $40$ est la dernière clé de la dernière feuille du fils gauche",
     "cours": r"Dans un nœud, la recherche dichotomique donne la position `i` de `x` ou celle où il devrait être. Si `x` n'est pas là, on descend dans `B.children[i]` ; une feuille sans `x` termine la recherche. Le parcours en ordre croissant intercale les clés et les fils (comme le parcours infixe). Le coût d'une recherche est au plus $h+1$ nœuds lus, d'où l'intérêt pour les disques : $h$ reste très petit."},
    {"id": "bt-ins", "titre": "B-arbres : insertion avec éclatement",
     "formule": r"éclater un $2t$-nœud : clé médiane (indice $t-1$) monte, deux nœuds à $t-1$ clés · à la descente : tout nœud plein rencontré est éclaté avant d'y entrer · racine pleine : nouvelle racine, hauteur $+1$ · insertion toujours dans une feuille non pleine",
     "exemple": r"$t=2$, nœud $[12\;14\;18]$ éclaté : $14$ monte, il reste $[12]$ et $[18]$",
     "cours": r"On insère dans une feuille. Si elle est pleine on ne peut pas ajouter : le principe de précaution consiste à éclater, en descendant, tout nœud plein (racine comprise) avant d'y entrer. Ainsi le père a toujours de la place pour recevoir la clé médiane. La hauteur n'augmente que si la racine est éclatée. Une clé déjà présente n'est pas insérée, mais des éclatements ont pu avoir lieu avant qu'on la trouve. Variante « à la remontée » (bonus du TD) : on n'éclate qu'en cas de besoin."},
    {"id": "bt-del", "titre": "B-arbres : suppression avec rotation et fusion",
     "formule": r"descendre dans un fils à $t-1$ clés : rotation (emprunt à un frère à $\ge t$ clés) sinon fusion avec un frère et le séparateur · clé interne : prédécesseur (fils gauche à $\ge t$ clés), sinon successeur, sinon fusion · racine vide : disparaît, hauteur $-1$",
     "exemple": r"$t=2$ : suppression de $9$ dans la feuille $[9]$ avec frère gauche $[6\;7]$ : rotation droite, $8$ descend, $7$ monte",
     "cours": r"À la descente, on garantit que le nœud où l'on entre a au moins $t$ clés (sauf la racine). Un fils à $t-1$ clés est donc complété : rotation gauche (le premier fils du frère droit remonte, le séparateur descend) ou rotation droite (symétrique), sinon fusion des deux fils avec le séparateur (la fusion de deux fils à $t-1$ clés donne $2t-1$ clés). Pour une clé interne on la remplace par son prédécesseur (ou son successeur) qu'on supprime ensuite dans une feuille. On préfère toujours le côté gauche. Même une clé absente peut entraîner des modifications (principe de précaution) ; la variante « à la remontée » modifie l'arbre seulement quand c'est nécessaire."},
]


# ---------------------------------------------------------------- levels 1 to 6: S2 reminders, general trees

from .algo_abg import _walk  # noqa: E402


def pmi(g):
    w = _gwalk(g)
    inner = [d for _, d, c in w if c > 0]
    return Fraction(sum(inner), len(inner))


def avg_arity(g):
    return Fraction(gsize(g) - 1, gsize(g) - gleaves(g))


def prefsuff(g):
    return [gkey(g)] + [k for c in gch(g) for k in prefsuff(c)] + [gkey(g)]


def count_siblings(g):
    """Number of non-empty `sibling` links in the first child - right sibling form."""
    b, n = [tab_obj(g)], 0
    while b:
        x = b.pop()
        n += x.sibling is not None
        b += [y for y in (x.child, x.sibling) if y is not None]
    return n


def deepest(s):
    k, d, _ = max(_walk(s), key=lambda e: e[1])
    return k, d


mb = {n: measures(s) for n, s in (("B1", TB1), ("B2", TB2), ("B3", TB3))}
assert count_siblings(G1) == gsize(G1) - 1 - (gsize(G1) - gleaves(G1))
BS1 = [50, 30, 70, 20, 40, 60, 80, 35, 45, 65]
BS2 = [8, 3, 10, 1, 6, 14, 4, 7, 13, 5]
BS3 = [40, 20, 60, 10, 30, 50, 70, 5, 25, 35, 45]

COUNT_PRINT = '''def count_print(B):
    if B.child == None:
        print("one")
    else:
        print("two")
        C = B.child
        while C.sibling != None:
            count_print(C)
            print("three")
            C = C.sibling
        count_print(C)
    print("four")'''


def prints(g):
    ns = {}
    exec(COUNT_PRINT, ns)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        ns["count_print"](tab_obj(g))
    out = buf.getvalue().split()
    return {w: out.count(w) for w in ("one", "two", "three", "four")}


def _cp_enonce(g, word):
    return (f"On applique `count_print(B)` à l'arbre $B$ ci-dessous, en implémentation premier fils - frère droit (`TreeAsBin`). "
            f"Combien de fois le mot « {word} » est-il affiché ?\n\n```python\n{COUNT_PRINT}\n```\n\n{gfig(('B', g))}")


def _cp_sol(g):
    p, ni = prints(g), gsize(g) - gleaves(g)
    return (f"Le code a été exécuté sur l'arbre. Affichages : « one » {p['one']} fois (une par feuille), « two » {p['two']} fois "
            f"(une par nœud interne, $N_i={ni}$), « four » {p['four']} fois (une par appel, soit $T={gsize(g)}$) et « three » "
            f"{p['three']} fois : un nœud interne à $a$ fils affiche « three » $a-1$ fois (tous les fils sauf le dernier), "
            f"d'où $\\sum(a-1)=(T-1)-N_i={gsize(g) - 1 - ni}$.")


LEVELS = []

LEVELS.append({"n": 1, "titre": "Rappel S2 : mesures d'un arbre binaire", "notions": ["bin"], "exos": [
    v("b11", f"{CONV_H} Quelle est la hauteur de l'arbre binaire $B$ ?\n\n{fig(('B', TB1))}", mb["B1"]["H"],
      f"Le nœud le plus profond est ${deepest(TB1)[0]}$, à la profondeur ${deepest(TB1)[1]}$."),
    v("b12", f"Combien l'arbre binaire $B$ a-t-il de feuilles ?\n\n{fig(('B', TB1))}", mb["B1"]["Nbe"],
      r"Une feuille est un nœud sans fils : on les compte."),
    v("b13", f"Longueur de cheminement $LC$ (somme des profondeurs des nœuds, racine à $0$) de $B$ ?\n\n{fig(('B', TB1))}", mb["B1"]["LC"],
      f"$LC=LCE+LCI={mb['B1']['LCE']}+{mb['B1']['LCI']}$ (feuilles puis nœuds internes)."),
    v("b14", r"Nombre maximal de nœuds d'un arbre binaire de hauteur $5$ (racine à la profondeur $0$) ?", 2 ** 6 - 1,
      r"Un niveau $p$ contient au plus $2^p$ nœuds : $\sum_{p=0}^{5}2^p=2^6-1$."),
]})

LEVELS.append({"n": 2, "titre": "Rappel S1/S2 : ABR et AVL", "notions": ["abr"], "exos": [
    v("r21", f"On insère successivement les clés ${lst(BS1)}$ dans un ABR initialement vide. Quelle est la hauteur de l'arbre obtenu ?",
      hb(bst(BS1)), f"Arbre obtenu :\n\n{fig(('ABR', bst(BS1)))}\n\nLe chemin le plus long est $50\\to30\\to40\\to35$ : hauteur ${hb(bst(BS1))}$."),
    v("r22", f"On insère successivement les clés ${lst(BS1)}$ dans un ABR vide. Quelle est la $6^e$ clé dans le parcours infixe ?",
      ino(bst(BS1))[5], f"Le parcours infixe d'un ABR donne les clés triées : ${lst(ino(bst(BS1)))}$. La $6^e$ est ${ino(bst(BS1))[5]}$."),
    v("r23", r"Nombre minimal de nœuds d'un AVL de hauteur $6$ (racine à $0$) ?", avl_min(6),
      r"$N(h)=N(h-1)+N(h-2)+1$ avec $N(0)=1$, $N(1)=2$ : $1,2,4,7,12,20,33$. Un AVL minimal a un sous-arbre de hauteur $h-1$ et un de hauteur $h-2$."),
    v("r24", r"On insère $1,2,3,4,5,6,7$ dans cet ordre dans un AVL vide. Quelle est la clé à la racine ?", key(avl(range(1, 8))),
      f"Chaque insertion ascendante déséquilibre à droite et déclenche une rotation gauche ({ROT[0]} rotations au total). Arbre final, parfait :\n\n{fig(('AVL', avl(range(1, 8))))}"),
]})

LEVELS.append({"n": 3, "titre": "Arbres généraux : mesures", "notions": ["gen-mes"], "exos": [
    v("g31", f"{CONV_H} Quelle est la hauteur de l'arbre général $T$ ?\n\n{gfig(('T', G1))}", gheight(G1),
      f"Le nœud le plus profond est $18$ (chemin $1\\to2\\to7\\to14\\to18$), à la profondeur ${depth_of(G1, 18)}$."),
    v("g32", f"Combien l'arbre général $T$ a-t-il de feuilles ?\n\n{gfig(('T', G1))}", gleaves(G1),
      f"Feuilles : ${lst(k for k, _, c in _gwalk(G1) if c == 0)}$. {gmeasure_sol(G1)}"),
    v("g33", f"Quelle est l'arité de l'arbre $T$ (arité maximale de ses nœuds) ?\n\n{gfig(('T', G1))}", garity(G1),
      r"Le nœud $1$ et le nœud $4$ ont chacun $4$ fils, aucun nœud n'en a davantage."),
    v("g34", f"Arité moyenne de $T$ : somme des nombres de fils divisée par le nombre de nœuds **internes** (fraction) ?\n\n{gfig(('T', G1))}",
      avg_arity(G1), f"{gmeasure_sol(G1)} Chaque nœud sauf la racine est le fils d'un nœud : $T-1={gsize(G1) - 1}$ fils au total, donc $\\frac{{{gsize(G1) - 1}}}{{{gsize(G1) - gleaves(G1)}}}$."),
    v("g35", f"Profondeur moyenne interne $PMI=\\frac{{LCI}}{{N_i}}$ de $T$ (racine à $0$, fraction) ?\n\n{gfig(('T', G24))}", pmi(G24),
      r"Nœuds internes et profondeurs : $10$ ($0$), $2$ ($1$), $8$ ($1$), $7$ ($2$), $6$ ($3$) : $LCI=7$, $N_i=5$.", src="Examen B5 ARB2 octobre 2024 (dossier 2028), ex. 2 (exemple de l'énoncé)"),
]})

LEVELS.append({"n": 4, "titre": "Représentations : n-uplets, premier fils - frère droit, forme linéaire", "notions": ["gen-rep"], "exos": [
    v("p41", f"On représente l'arbre général $T$ en premier fils - frère droit (arbre binaire : gauche $=$ `child`, droite $=$ `sibling`). Quelle est la hauteur de cet arbre binaire (racine à $0$) ?\n\n{gfig(('T', G1))}",
      measures(fcrs_bin(G1))["H"],
      f"L'arbre binaire est :\n\n{fig(('B', fcrs_bin(G1)))}\n\nLe nœud le plus profond est ${deepest(fcrs_bin(G1))[0]}$ : on descend d'un cran à gauche pour chaque niveau de l'arbre général et d'un cran à droite pour chaque frère à passer."),
    o("p42", f"Donner la représentation linéaire `(o A1 ... AN)` de l'arbre $T$ (clé de la racine suivie des représentations des fils, sans espace).\n\n{gfig(('T', G1))}",
      f"`{glinear(G1)}`\n\nChaque sous-arbre est parenthésé : une feuille $k$ s'écrit `(k)`, un nœud de clé $k$ et de fils $A_1,\\dots,A_N$ s'écrit `(k A1 ... AN)`. Les parenthèses sont bien équilibrées, et le nombre de `(` vaut la taille $T={gsize(G1)}$."),
    v("p43", "Quelle est la hauteur de l'arbre représenté par `(12(2(25)(6)(-7))(0(18(1)(8))(9))(4(3)(11)))` (racine à $0$) ?", gheight(G_TD),
      f"On lit : la racine $12$ a trois fils $2$, $0$, $4$ ; $2$ a pour fils $25,6,-7$ ; $0$ a pour fils $18$ (de fils $1,8$) et $9$ ; $4$ a pour fils $3,11$.\n\n{gfig(('T', G_TD))}"),
    v("p44", f"Dans la représentation premier fils - frère droit de $T$, combien de liens `sibling` sont différents de `None` ?\n\n{gfig(('T', G1))}",
      count_siblings(G1),
      f"Un nœud a un frère droit s'il n'est pas le dernier fils de son père. Il y a $T-1={gsize(G1) - 1}$ nœuds qui ne sont pas la racine, dont $N_i={gsize(G1) - gleaves(G1)}$ derniers fils (un par nœud interne) : ${gsize(G1) - 1}-{gsize(G1) - gleaves(G1)}={count_siblings(G1)}$."),
    o("p45", f"Dessiner l'arbre binaire premier fils - frère droit de $T$.\n\n{gfig(('T', G24))}",
      f"{fig(('B', fcrs_bin(G24)))}\n\nRègle : le fils gauche d'un nœud est son premier fils, le fils droit est son frère droit (jamais de frère pour la racine). Les feuilles de $T$ sont les nœuds sans fils gauche."),
]})

LEVELS.append({"n": 5, "titre": "Parcours : préfixe, suffixe, largeur", "notions": ["gen-par"], "exos": [
    v("q51", f"Rang (à partir de $1$) du nœud $14$ dans le parcours préfixe de $T$ ?\n\n{gfig(('T', G1))}", gpre(G1).index(14) + 1,
      f"Préfixe : ${lst(gpre(G1))}$."),
    v("q52", f"Rang (à partir de $1$) du nœud $4$ dans le parcours suffixe de $T$ ?\n\n{gfig(('T', G1))}", gpost(G1).index(4) + 1,
      f"Suffixe (fils puis père) : ${lst(gpost(G1))}$."),
    v("q53", f"Rang (à partir de $1$) du nœud $7$ dans le parcours en largeur de $T$ ?\n\n{gfig(('T', G24))}", gbfs(G24).index(7) + 1,
      f"Largeur, niveau par niveau et de gauche à droite : ${lst(gbfs(G24))}$."),
    v("q54", _cp_enonce(G1, "three"), prints(G1)["three"], _cp_sol(G1)),
    v("q55", f"Dans le vecteur construit en plaçant chaque clé deux fois (à la première rencontre, ordre préfixe, et à la dernière, ordre suffixe, du parcours profondeur), quel est le $9^e$ élément de l'arbre $T$ ?\n\n{gfig(('T', G24))}",
      prefsuff(G24)[8], f"Vecteur : ${lst(prefsuff(G24))}$ (longueur $2T={2 * gsize(G24)}$)."),
]})


# ---------------------------------------------------------------- level 6: functions on general trees

S_SIZE = '''def size(T):
    n = 1
    for C in T.children:
        n += size(C)
    return n


def size_bin(B):
    n = 1
    C = B.child
    while C != None:
        n += size_bin(C)
        C = C.sibling
    return n'''
S_HEIGHT = '''def height(T):
    h = 0
    for C in T.children:
        h = max(h, 1 + height(C))
    return h


def height_bin(B):
    h = 0
    C = B.child
    while C != None:
        h = max(h, 1 + height_bin(C))
        C = C.sibling
    return h'''
S_WIDTH = '''def width(T):
    """largest number of nodes on one level"""
    q = Queue()
    q.enqueue(T)
    q.enqueue(None)              # end-of-level marker
    best = cur = 0
    while not q.isempty():
        t = q.dequeue()
        if t == None:
            best = max(best, cur)
            cur = 0
            if not q.isempty():  # re-enqueue the marker only if a next level exists
                q.enqueue(None)
        else:
            cur += 1
            for C in t.children:
                q.enqueue(C)
    return best'''
S_LINEAR = '''def to_linear(T):
    s = "(" + str(T.key)
    for C in T.children:
        s += to_linear(C)
    return s + ")"'''
S_PREFSUFF = '''def _ps(B, L):
    L.append(B.key)              # first meeting: prefix
    C = B.child
    while C != None:
        _ps(C, L)
        C = C.sibling
    L.append(B.key)              # last meeting: suffix


def prefsuff(B):
    L = []
    _ps(B, L)
    return L'''


def width_of(g):
    lv, cur = [], [g]
    while cur:
        lv.append(len(cur))
        cur = [c for x in cur for c in gch(x)]
    return max(lv)


LEVELS.append({"n": 6, "titre": "Écrire des fonctions sur les arbres généraux (taille, hauteur, largeur, forme linéaire)", "notions": ["gen-code", "gen-rep"], "exos": [
    wg("c61", r"Écrire `size(T)` (arbre par n-uplets, classe `Tree`) et `size_bin(B)` (premier fils - frère droit, classe `TreeAsBin`) qui retournent la taille (nombre de nœuds) de l'arbre.",
       S_SIZE, [("size(T)", str(gsize(G1))), ("size(Tree(5))", "1"), ("size_bin(B)", str(gsize(G1)))],
       r"Parcours profondeur : la taille est $1+\sum$ des tailles des fils. Dans la version binaire, on parcourt la liste des fils par `C = C.sibling` ; on n'appelle jamais la fonction sur `B.sibling` directement depuis `B`, sinon on compterait aussi les frères de `B`.",
       trees={"T": G1}, tabs={"B": G1}, figs=gfig(("T", G1)), duree=6),
    wg("c62", r"Écrire `height(T)` (n-uplets) et `height_bin(B)` (premier fils - frère droit) qui retournent la hauteur de l'arbre (une feuille a la hauteur $0$).",
       S_HEIGHT, [("height(T)", str(gheight(G1))), ("height(Tree(5))", "0"), ("height_bin(B)", str(gheight(G1)))],
       r"La hauteur est le maximum des $1+$ hauteurs des fils. L'accumulateur `h` vaut $0$ pour une feuille car la boucle ne s'exécute pas. En version binaire, la hauteur de l'arbre général n'est **pas** celle de l'arbre binaire : on ne descend pas vers `B.sibling` comme vers un fils.",
       trees={"T": G1}, tabs={"B": G1}, figs=gfig(("T", G1)), duree=6),
    wg("c63", r"Écrire `width(T)` (arbre par n-uplets) qui retourne la largeur de l'arbre : le plus grand nombre de nœuds sur un même niveau. Utiliser un parcours en largeur avec la classe `Queue` (`enqueue`, `dequeue`, `isempty`).",
       S_WIDTH, [("width(T)", str(width_of(G1))), ("width(Tree(5))", "1"), ("width(U)", str(width_of(G24)))],
       r"Parcours largeur : on repère les changements de niveau avec un marqueur `None` enfilé après la racine, puis après chaque niveau terminé. Le marqueur n'est réenfilé que si la file n'est pas vide, sinon la boucle ne s'arrêterait jamais. Le compteur `cur` compte les nœuds du niveau en cours.",
       trees={"T": G1, "U": G24}, figs=gfig(("T", G1)), duree=8),
    wg("c64", r"Écrire `to_linear(T)` qui retourne la représentation linéaire de l'arbre (arbre par n-uplets) sous forme de chaîne : `(o A1 ... AN)` sans espace, par exemple `(1(2)(3))` pour une racine $1$ et deux feuilles $2$ et $3$.",
       S_LINEAR, [("to_linear(T)", repr(glinear(G1))), ("to_linear(Tree(7))", "'(7)'")],
       r"Parcours préfixe : on écrit la parenthèse ouvrante et la clé, puis la représentation de chaque fils dans l'ordre, puis la parenthèse fermante.",
       trees={"T": G1}, figs=gfig(("T", G1)), duree=6),
    wg("c65", r"Dans cet exercice on remplit une liste avec les clés d'un arbre général : chaque clé est placée deux fois, lors de la première rencontre (ordre préfixe) et lors de la dernière (ordre suffixe) du parcours profondeur. Écrire `prefsuff(B)` avec l'implémentation premier fils - frère droit.",
       S_PREFSUFF, [("prefsuff(B)", repr(prefsuff(G_PS)))],
       r"On ajoute la clé avant de parcourir les fils et après. Une feuille apparaît deux fois de suite. Vérifié par exécution sur l'exemple de l'énoncé (liste de $20$ éléments), corrigé rédigé.",
       tabs={"B": G_PS}, figs=gfig(("T", G_PS)), src="Contrôle C3 du 7 novembre 2017 (dossier 2021), ex. 2 : Préfixe - Suffixe", duree=8),
]})

# ---------------------------------------------------------------- levels 7 and 8: B-tree properties and reading


def keys_max_tree(t, h):
    return (2 * t) ** (h + 1) - 1


def keys_min_tree(t, h):
    return 1 + sum(2 * t ** (j - 1) * (t - 1) for j in range(1, h + 1))


def hmax(t, n):
    h = 0
    while keys_min_tree(t, h + 1) <= n:
        h += 1
    return h


def hmin(t, n):
    h = 0
    while keys_max_tree(t, h) < n:
        h += 1
    return h


assert keys_min_tree(3, 2) == 2 * 3 ** 2 - 1 == 17
assert all(keys_min_tree(t, h) == 2 * t ** h - 1 for t in (2, 3, 5) for h in range(5))


def search_path(n, x):
    out = []
    while True:
        out.append(n)
        i = bisect.bisect_left(n.keys, x)
        if i < len(n.keys) and n.keys[i] == x or n.leaf():
            return out
        n = n.ch[i]


def pred_of(n, x):
    ks = bkeys(n)
    return ks[ks.index(x) - 1] if ks.index(x) else None


LEVELS.append({"n": 7, "titre": "B-arbres : nombre de clés et de fils", "notions": ["bt-def"], "exos": [
    v("t71", r"Quel est le nombre maximal de clés d'un nœud d'un B-arbre de degré $t=5$ ?", 2 * 5 - 1,
      r"Un nœud porte au plus $2t-1$ clés (il est alors plein, c'est un $2t$-nœud à $2t$ fils) : $2\times5-1$."),
    v("t72", r"Quel est le nombre minimal de clés d'un nœud non racine d'un B-arbre de degré $t=6$ ?", 6 - 1,
      r"Un nœud non racine a au moins $t$ fils, donc au moins $t-1$ clés : $6-1$."),
    v("t73", r"Nombre maximal de clés d'un B-arbre de degré $t=3$ et de hauteur $2$ (racine à la profondeur $0$) ?", keys_max_tree(3, 2),
      r"Tous les nœuds sont pleins : $2t-1=5$ clés par nœud et $2t=6$ fils par nœud. Nœuds : $1+6+36=43$. Clés : $43\times5=215=(2t)^{h+1}-1=6^3-1$."),
    v("t74", r"Nombre minimal de clés d'un B-arbre de degré $t=3$ et de hauteur $2$ ?", keys_min_tree(3, 2),
      r"Racine à $1$ clé donc $2$ fils ; chaque autre nœud interne a $t=3$ fils et chaque nœud non racine $t-1=2$ clés. Nœuds : $1+2+2\times3=9$ ; clés : $1+8\times2=17=2t^h-1=2\times9-1$."),
    v("t75", r"Un nœud d'un B-arbre contient au plus $11$ clés. Quel est le degré $t$ ?", 6,
      r"$2t-1=11$ donc $t=6$ : un nœud porte alors de $5$ à $11$ clés."),
]})

LEVELS.append({"n": 8, "titre": "B-arbres : hauteur, recherche, parcours croissant, prédécesseur", "notions": ["bt-def", "bt-lect"], "exos": [
    v("u81", r"Un B-arbre de degré $t=3$ contient $n=1000$ clés. Quelle est sa hauteur maximale (racine à $0$) ?", hmax(3, 1000),
      f"Une hauteur $h$ exige au moins $2t^h-1$ clés : $2\\times3^h-1\\le1000$ donne $3^h\\le500{{,}}5$. $3^5=243$ convient, $3^6=729$ non : $h_{{\\max}}={hmax(3, 1000)}$ (soit $h\\le\\log_3\\frac{{n+1}}2$)."),
    v("u82", r"Un B-arbre de degré $t=2$ contient $n=100$ clés. Quelle est sa hauteur minimale ?", hmin(2, 100),
      r"Une hauteur $h$ permet au plus $(2t)^{h+1}-1=4^{h+1}-1$ clés. $4^3-1=63 < 100$ et $4^4-1=255\ge100$ : $h+1=4$, donc $h=3$."),
    v("u83", f"Combien de nœuds lit-on pour chercher la clé $38$ dans ce B-arbre de degré $2$ (racine comprise) ?\n\n{bfig(('B', BTD))}", len(search_path(BTD, 38)),
      r"On part de la racine $[22]$ : $38>22$, fils de droite $[27\;41]$ ; $38 > 27$ et $38 < 41$, fils du milieu $[30\;35\;38]$ où l'on trouve $38$. Trois nœuds lus : $h+1$ au plus."),
    v("u84", f"Quel est le prédécesseur de $40$ (plus grande clé strictement inférieure) dans ce B-arbre ?\n\n{bfig(('B', B24_WHAT))}", pred_of(B24_WHAT, 40),
      r"$40$ est à la racine, un nœud interne : son prédécesseur est la clé la plus à droite du fils gauche, donc on descend toujours par le dernier fils : $[7\;20\;35]$ puis la feuille $[36\;39]$, dont la dernière clé est $39$."),
    v("u85", f"Dans le parcours en ordre croissant de ce B-arbre, quelle est la $10^e$ clé ?\n\n{bfig(('B', BTD))}", bkeys(BTD)[9],
      f"Le parcours intercale fils et clés : ${lst(bkeys(BTD))}$. La $10^e$ est ${bkeys(BTD)[9]}$."),
]})


# ---------------------------------------------------------------- levels 9 to 12: insertion and deletion

SEQ_TD = [5, 15, 40, 25, 12, 14, 18, 16, 45, 38, 9]  # TD 2, ex. 2.3 (b)
DEL_TD1 = [27, 24, 25, 35]  # TD 2, ex. 2.4 (1 to 3)
DEL_TD2 = [35, 15, 22, 8, 20, 30, 18, 45, 12, 48, 19, 41]  # TD 2, ex. 2.4 (4) : the 35 is already gone, see below
AFTER_TD1 = final_del(BTD, DEL_TD1, 2)
DEL_REST = DEL_TD2[1:]
assert 35 not in bkeys(AFTER_TD1)

BI1 = N([30, 60], N([5, 10, 15, 20, 25]), N([40, 50]), N([70, 80, 90, 95, 99]))
valid(BI1, 3)
BI3 = N([10], N([3, 5, 7]), N([15, 20]))
valid(BI3, 2)
BD1 = N([20, 40], N([5, 10]), N([25, 30]), N([45, 50, 55]))
valid(BD1, 3)
BD3 = N([10], N([4]), N([15]))
valid(BD3, 2)

st_ins = steps_ins(BTD, [36, 42], 2)
st_ins2 = steps_ins(B21_INS, [11, 32, 20], 2)
st_seq = steps_ins(None, SEQ_TD, 2)
fin_seq = st_seq[-1][1]
st_asc = steps_ins(None, list(range(1, 16)), 2)
st_asc3 = steps_ins(None, list(range(1, 31)), 3)
st_d1 = steps_del(BTD, DEL_TD1, 2)
st_d2 = steps_del(AFTER_TD1, DEL_REST, 2)
st_d21 = steps_del(B21_DEL, [15], 2)
assert bcount(fin_seq) == 1 + count_ops(st_seq, 'split') + bheight(fin_seq)
assert bcount(st_asc3[-1][1]) == 1 + count_ops(st_asc3, 'split') + bheight(st_asc3[-1][1])

LEVELS.append({"n": 9, "titre": "B-arbres : insertion et éclatement", "notions": ["bt-ins"], "exos": [
    v("i91", f"{CONV_B} Combien d'éclatements (splits) a-t-on effectués après l'insertion successive de $36$ puis de $42$ dans ce B-arbre de degré $2$ ?\n\n{bfig(('B', BTD))}",
      count_ops(st_ins, "split"), f"{show_ins(BTD, [36, 42], 2)}\n\nUn éclatement pour chaque insertion (nœud plein rencontré à la descente)."),
    v("i92", r"On éclate un nœud plein d'un B-arbre de degré $t=3$ contenant les clés $[4\;9\;15\;21\;33]$. Quelle clé monte dans le père ?", 15,
      r"La clé médiane, d'indice $t-1=2$ (en comptant à partir de $0$) : $[4\;9]$ et $[21\;33]$ restent, $15$ monte."),
    o("i93", f"{CONV_B} Construire le B-arbre de degré $2$ (arbre 2-3-4) obtenu par insertions successives, dans un arbre vide, de ${lst(SEQ_TD)}$. Dessiner l'arbre après chaque insertion.",
      f"{show_ins(None, SEQ_TD, 2)}\n\nArbre final :\n\n{bfig(('final', fin_seq))}\n\nChaque état a été calculé par un programme de contrôle qui vérifie aussi les propriétés du B-arbre (nombre de clés, ordre, feuilles au même niveau).", duree=10),
    v("i94", f"Combien de nœuds a le B-arbre de degré $2$ obtenu par insertions successives de ${lst(SEQ_TD)}$ dans un arbre vide ?", bcount(fin_seq),
      f"Arbre final :\n\n{bfig(('final', fin_seq))}\n\nIl y a eu {count_ops(st_seq, 'split')} éclatements : chaque éclatement crée un nœud, et celui de la racine en crée deux (nouvelle racine et nouveau frère) : $1+{count_ops(st_seq, 'split')}+{bheight(fin_seq)}={bcount(fin_seq)}$."),
    v("i95", r"On insère $1,2,3,\dots,15$ dans cet ordre dans un B-arbre de degré $2$ initialement vide. Quelle est la hauteur finale (racine à $0$) ?", bheight(st_asc[-1][1]),
      f"Arbre final :\n\n{bfig(('B', st_asc[-1][1]))}\n\n{count_ops(st_asc, 'split')} éclatements au total. Une insertion croissante remplit toujours la feuille de droite, qui éclate dès qu'elle est pleine."),
]})

LEVELS.append({"n": 10, "titre": "B-arbres : insertions à la descente, cas délicats", "notions": ["bt-ins"], "exos": [
    o("i101", f"{CONV_B} Dessiner l'arbre (degré $3$) après l'insertion successive de $22$ puis de $97$.\n\n{bfig(('B', BI1))}",
      f"{show_ins(BI1, [22, 97], 3)}\n\nLa feuille {kx([5, 10, 15, 20, 25])} est pleine ($2t-1=5$) : on l'éclate à la descente, la médiane $15$ monte dans la racine, avant d'y insérer $22$. Même chose pour la feuille {kx([70, 80, 90, 95, 99])} avec la médiane $90$.", duree=8),
    o("i102", f"{CONV_B} Insérer successivement $1,2,3,\\dots,10$ dans un B-arbre de degré $2$ initialement vide. Dessiner l'arbre après chaque insertion. Quelle est la hauteur finale ?",
      f"{show_ins(None, list(range(1, 11)), 2)}\n\nHauteur finale : ${bheight(steps_ins(None, list(range(1, 11)), 2)[-1][1])}$. La racine n'est éclatée que lorsqu'elle est pleine ; la hauteur augmente alors de $1$, et c'est le seul cas.", duree=10),
    o("i103", f"{CONV_B} Insérer la clé $3$ dans ce B-arbre de degré $2$ alors qu'elle est **déjà présente**. L'arbre est-il modifié ?\n\n{bfig(('B', BI3))}",
      f"Oui, il est modifié. On descend dans le fils gauche {kx([3, 5, 7])}, plein ($2t-1=3$ clés), et on l'éclate **avant** de savoir que $3$ y est (la clé $3$ n'est pas la médiane, seule la médiane est testée avant l'éclatement) :\n\n{bfig(('après', insert(BI3, 3, 2)))}\n\nLa clé n'est pas ajoutée (pas de doublon), mais l'éclatement préventif a eu lieu. C'est le défaut du principe de précaution, corrigé par l'insertion « à la remontée » (bonus du TD).", duree=6),
    v("i104", r"On insère $1,2,\dots,30$ dans cet ordre dans un B-arbre de degré $3$ initialement vide. Combien d'éclatements a-t-on effectués au total ?", count_ops(st_asc3, "split"),
      f"Hauteur finale ${bheight(st_asc3[-1][1])}$, ${bcount(st_asc3[-1][1])}$ nœuds. Chaque éclatement crée un nœud, et celui de la racine en crée deux : nœuds $=1+$ éclatements $+h$, soit $1+{count_ops(st_asc3, 'split')}+{bheight(st_asc3[-1][1])}={bcount(st_asc3[-1][1])}$ (le nombre d'éclatements s'en déduit)."),
]})

LEVELS.append({"n": 11, "titre": "B-arbres : suppression, rotation et fusion", "notions": ["bt-del"], "exos": [
    o("d111", f"{CONV_B} {CONV_D} Dessiner l'arbre (degré $2$) après la suppression successive de ${lst(DEL_TD1)}$.\n\n{bfig(('B', BTD))}",
      f"{show_del(BTD, DEL_TD1, 2)}\n\nBilan : $27$ est une clé interne (prédécesseur ou successeur), puis deux rotations gauches, puis une fusion.", duree=10),
    v("d112", f"{CONV_D} Combien de rotations (gauches ou droites) effectue-t-on en supprimant successivement ${lst(DEL_TD1)}$ dans ce B-arbre de degré $2$ ?\n\n{bfig(('B', BTD))}",
      count_ops(st_d1, "rotate-left") + count_ops(st_d1, "rotate-right"), f"{show_del(BTD, DEL_TD1, 2)}"),
    v("d113", f"{CONV_D} Dans ce B-arbre de degré $2$ on supprime successivement ${lst(DEL_REST)}$. Combien de fusions effectue-t-on ?\n\n{bfig(('B', AFTER_TD1))}",
      count_ops(st_d2, "merge"), f"{show_del(AFTER_TD1, DEL_REST, 2)}"),
    o("d114", f"{CONV_B} {CONV_D} Dessiner l'arbre de degré $3$ après la suppression successive de $5$, $55$ puis $40$.\n\n{bfig(('B', BD1))}",
      f"{show_del(BD1, [5, 55, 40], 3)}\n\nAvec $t=3$ un nœud non racine garde au moins $2$ clés : la feuille {kx([5, 10])} n'a plus de clé à perdre et son frère {kx([25, 30])} non plus, donc fusion avec le séparateur $20$ (la fusion de deux nœuds à $t-1$ clés donne un nœud plein, $2t-1=5$ clés).", duree=8),
]})

LEVELS.append({"n": 12, "titre": "B-arbres : suppressions enchaînées, cas délicats", "notions": ["bt-del"], "exos": [
    o("d121", f"{CONV_B} {CONV_D} Dans ce B-arbre de degré $2$, supprimer successivement ${lst(DEL_REST)}$ en limitant les destructions de nœuds. Dessiner l'arbre après chaque suppression.\n\n{bfig(('B', AFTER_TD1))}",
      f"{show_del(AFTER_TD1, DEL_REST, 2)}\n\nL'arbre final est $[{bkeys(final_del(AFTER_TD1, DEL_REST, 2))[0]}]$ après deux diminutions de hauteur : chaque fois que la racine et ses deux fils n'ont que $t-1$ clés, la fusion vide la racine.", duree=15),
    o("d122", f"{CONV_B} {CONV_D} On supprime la clé $12$, **absente** de ce B-arbre de degré $2$. L'arbre est-il modifié ?\n\n{bfig(('B', BD3))}",
      f"Oui. La recherche descend vers le fils de droite $[15]$ qui n'a que $t-1=1$ clé : par précaution on le complète avant d'y entrer. Le frère gauche $[4]$ n'a que $t-1$ clés et ne peut pas prêter : fusion avec lui et le séparateur $10$ :\n\n{bfig(('après', delete(BD3, 12, 2)))}\n\nLa clé $12$ n'est pas dans la feuille et rien n'est supprimé, mais l'arbre a perdu un niveau. Avec la suppression « à la remontée » (exercice 2.6 du TD), on ne modifie l'arbre qu'au retour de la récursion, donc seulement quand une clé a vraiment été supprimée.", duree=8),
    v("d123", f"{CONV_D} Quelle est la hauteur de l'arbre après la suppression successive de ${lst(DEL_REST[:7])}$ dans ce B-arbre de degré $2$ (racine à $0$) ?\n\n{bfig(('B', AFTER_TD1))}",
      bheight(final_del(AFTER_TD1, DEL_REST[:7], 2)), f"{show_del(AFTER_TD1, DEL_REST[:7], 2)}"),
    v("d124", f"{CONV_D} Combien de rotations (gauches ou droites) effectue-t-on en supprimant successivement ${lst(DEL_REST)}$ dans ce B-arbre de degré $2$ ?\n\n{bfig(('B', AFTER_TD1))}",
      count_ops(st_d2, "rotate-left") + count_ops(st_d2, "rotate-right"), show_del(AFTER_TD1, DEL_REST, 2)),
]})


# ---------------------------------------------------------------- exam parts (EXTRA_PARTS)

EX28 = "Examen B5 ARB2 du 22 octobre 2024 (dossier 2028)"
EX25 = "Contrôle C3 du 9 novembre 2021 (dossier 2025)"
EX23 = "Contrôle C3 de novembre 2019 (dossier 2023)"

IAD = '''def _aux(T, d):
    """(number of internal nodes, sum of their depths) of the subtree T whose root is at depth d"""
    if T.children == []:
        return (0, 0)
    (n, s) = (1, d)
    for C in T.children:
        (nc, sc) = _aux(C, d + 1)
        n += nc
        s += sc
    return (n, s)


def internal_average_depth(T):
    (n, s) = _aux(T, 0)
    return s / n if n > 0 else 0'''
SAME = '''def _same(B, a):
    """a: arity already met on an internal node (0 if none yet).
    Returns the common arity (0 if no internal node), -1 if two arities differ."""
    if B.child == None:
        return a
    k = 0
    C = B.child
    while C != None:
        k += 1
        C = C.sibling
    if a != 0 and k != a:
        return -1
    a = k
    C = B.child
    while C != None and a != -1:
        a = _same(C, a)
        C = C.sibling
    return a


def same_arity(B):
    return _same(B, 0) != -1'''


def same_ar(g):
    return len({c for _, _, c in _gwalk(g) if c > 0}) <= 1


SA = [(1, [(2, [4, 5]), (3, [6, 7])]), (1, [2, (3, [4, 5])]), (1, [(2, [4]), 3]), G1, 7]
SA_T = {f"B{i}": g for i, g in enumerate(SA, 1)}

WHAT = '''def __aux(B, x, p):
    i = binary_search_pos(B.keys, x)
    f = i < B.nbkeys and B.keys[i] == x
    if B.children == []:
        if f:
            if i == 0:
                return p
            else:
                return B.keys[i - 1]
        else:
            return None
    else:
        if f:
            B = B.children[i]
            while B.children != []:
                B = B.children[B.nbkeys]
            return B.keys[B.nbkeys - 1]
        else:
            if i != 0:
                p = B.keys[i - 1]
            return __aux(B.children[i], x, p)


def what(B, x):
    if B != None:
        return __aux(B, x, None)
    else:
        return None'''
_ns = {"binary_search_pos": binary_search_pos}
exec(WHAT, _ns)
_bw = btree_obj(B24_WHAT)
WHAT_RES = [_ns["what"](_bw, x) for x in (2, 20, 40, 41, 42, 87)]
assert WHAT_RES == [None, 16, 39, None, 40, 83]

MORE = '''def morechildren(B, nbc=0):          # nbc: number of children of the father of B
    k = 0
    C = B.child
    while C:
        k += 1
        C = C.sibling
    if B.child and k <= nbc:
        return False
    else:
        C = B.child
        while C and morechildren(C, k):
            C = C.sibling
        return C == None'''
DECR = '''def __decrease(B, L):
    if B.children == []:
        for i in range(B.nbkeys - 1, -1, -1):
            L.append(B.keys[i])
    else:
        for i in range(B.nbkeys, 0, -1):
            __decrease(B.children[i], L)
            L.append(B.keys[i - 1])
        __decrease(B.children[0], L)


def decrease(B):
    L = []
    if B:
        __decrease(B, L)
    return L'''
MYST = '''def mystery(B, a, b):
    if B.keys[0] < a or B.keys[B.nbkeys - 1] > b:
        return False
    else:
        for i in range(B.nbkeys - 1):
            if B.keys[i] >= B.keys[i + 1]:
                return False
        if B.children == []:
            return True
        else:
            i = 0
            while i < B.nbkeys and mystery(B.children[i], a, B.keys[i]):
                a = B.keys[i]
                i += 1
            return i == B.nbkeys and mystery(B.children[B.nbkeys], a, b)'''


def run_mystery(n, a, b):
    cnt = [0]
    ns = {"CNT": cnt}
    exec(MYST.replace("def mystery(B, a, b):\n", "def mystery(B, a, b):\n    CNT[0] += 1\n"), ns)
    BTree.degree = 3
    return ns["mystery"](btree_obj(n), a, b), cnt[0]


MYS = [run_mystery(B21_DEL, 0, 92), run_mystery(B21_MYS, 0, 20), run_mystery(B21_MYS, 1, 99)]
assert MYS == [(True, 8), (False, 6), (False, 8)], MYS  # official correction

ARITY = '''def arity(B):
    if B.child == None:
        (links, nodes) = (0, 0)
    else:
        (lc, nc) = arity(B.child)
        (links, nodes) = (lc + 1, nc + 1)
    if B.sibling != None:
        (ls, ns) = arity(B.sibling)
        links += ls + 1
        nodes += ns
    return (links, nodes)


def average_arity(B):
    (links, nodes) = arity(B)
    return links / nodes if nodes else 0'''
INS_C3 = '''def __insert(B, x):
    i = search_pos(B.keys, x)
    if i < B.nbkeys and B.keys[i] == x:
        return False
    elif B.children == []:
        B.keys.insert(i, x)
        return True
    else:
        if B.children[i].nbkeys == 2 * B.degree - 1:
            if B.children[i].keys[B.degree - 1] == x:
                return False
            split(B, i)
            if x > B.keys[i]:
                i += 1
        return __insert(B.children[i], x)'''
INS_WRAP = '''def insert(B, x):
    if B == None:
        return (BTree([x]), True)
    else:
        if B.nbkeys == 2 * B.degree - 1:
            B = BTree([], [B])
            split(B, 0)
        ok = __insert(B, x)
        return (B, ok)'''


def _check_insert(ns):
    BTree.degree = 2
    for start, xs in ((BTD, [36, 42, 17, 21, 30, 100, 1, 12, 22]), (None, [3, 1, 2, 5, 4, 9, 8, 7, 6, 3])):
        ref, B = start, (btree_obj(start) if start else None)
        for x in xs:
            B, ok = ns["insert"](B, x)
            assert ok == (x not in (bkeys(ref) if ref else []))
            ref = insert(ref, x, 2)
            assert btext(node_of(B)) == btext(ref), (x, btext(node_of(B)), btext(ref))
            valid(node_of(B), 2)


BUILD = '''def build(nodes, degree):
    BTree.degree = degree
    B = BTree(nodes[0])
    end = B.nbkeys + 2
    q = Queue()
    q.enqueue((B, 1))
    while not q.isempty():
        (cur, pos) = q.dequeue()
        if pos < len(nodes):
            for i in range(pos, pos + cur.nbkeys + 1):
                new = BTree(nodes[i])
                cur.children.append(new)
                q.enqueue((new, end))
                end += new.nbkeys + 1
    return B'''
NODES = [lv.keys for lv in [n for L in levels_b(BTD) for n in L]]
_ns = {"BTree": BTree, "Queue": Queue}
exec(BUILD, _ns)
assert btext(node_of(_ns["build"](NODES, 2))) == btext(BTD)

T25_1 = (1, [(2, [4, 5, 6]), (3, [7, 8])])
T25_2 = (1, [(2, [4, 5, 6]), (3, [7, 8, 9])])


def show_ops(start, ops, t):
    out, r = [], start
    for k, x in ops:
        lg = []
        prev = r
        r = insert(r, x, t, lg) if k == "i" else delete(r, x, t, lg)
        valid(r, t)
        verb = "Insertion" if k == "i" else "Suppression"
        note = " ; la racine vide disparaît, la hauteur diminue de 1" if bheight(r) < bheight(prev) else (
            " ; la racine est éclatée, la hauteur augmente de 1" if bheight(r) > bheight(prev) else "")
        out.append(f"**{verb} de ${x}$** : {explain(lg)}{note}.\n\n{bfig(('', r))}")
    return "\n\n".join(out), r


def apply_ops(start, ops, t):
    r = start
    for k, x in ops:
        r = insert(r, x, t) if k == "i" else delete(r, x, t)
    valid(r, t)
    return r


EXTRA_PARTS = [
    wg("x28a", r"En utilisant **obligatoirement un parcours profondeur**, écrire la fonction `internal_average_depth(T)` qui retourne la profondeur moyenne interne de l'arbre `T` en implémentation par n-uplets (`Tree`) si `taille(T)` $> 1$, $0$ sinon (racine à la profondeur $0$).",
       IAD, [("internal_average_depth(T)", "1.4"), ("internal_average_depth(Tree(3))", "0")],
       f"Un parcours profondeur qui descend la profondeur `d` en paramètre et remonte le couple (nombre de nœuds internes, somme de leurs profondeurs) : un appel sur une feuille renvoie `(0, 0)`. Ici $\\frac{{LCI}}{{N_i}}=\\frac{{{sum(d for _, d, c in _gwalk(G24) if c)}}}{{{sum(1 for *_, c in _gwalk(G24) if c)}}}=1{{,}}4$. Pas de corrigé officiel : corrigé rédigé, vérifié par exécution sur l'arbre de l'énoncé.",
       trees={"T": G24}, figs=gfig(("T", G24)), src=f"{EX28}, ex. 2", duree=15),
    wg("x28b", r"Écrire la fonction `same_arity(B)` qui vérifie si tous les nœuds **internes** de l'arbre `B` en implémentation premier fils - frère droit (`TreeAsBin`) ont la même arité (l'arité d'un nœud est son nombre de fils).",
       SAME, [(f"same_arity(B{i})", repr(same_ar(g))) for i, g in enumerate(SA, 1)],
       r"Parcours profondeur interrompu : dès que deux arités différentes sont vues, on renvoie $-1$ et on cesse de parcourir les frères (`and a != -1`). L'arité est comptée en parcourant la liste des fils par `sibling`. Un arbre sans nœud interne a la propriété (arité $0$). Corrigé rédigé, vérifié par exécution sur cinq arbres dont la réponse est calculée indépendamment.",
       tabs=SA_T, figs=gfig(*[(f"B{i}", g) for i, g in enumerate(SA[:4], 1)]), src=f"{EX28}, ex. 3", duree=15),
    o("x28c", f"{CONV_B} Dessiner l'arbre après insertions successives des valeurs $25$, $3$ et $41$ dans ce B-arbre $B_1$ de degré $2$ (utiliser le principe « à la descente »).\n\n{bfig(('B1', B24_INS))}",
      f"{show_ins(B24_INS, [25, 3, 41], 2)}", src=f"{EX28}, ex. 4 (1)", duree=8),
    o("x28d", f"{CONV_B} Dessiner l'arbre après suppression de la valeur $50$ dans ce B-arbre $B_2$ de degré $2$ (principe « à la descente »).\n\n{bfig(('B2', B24_DEL))}",
      f"{show_del(B24_DEL, [50], 2)}\n\nCorrigé rédigé (le sujet n'a pas de corrigé officiel). Convention : on préfère le côté gauche (prédécesseur), comme au TD. Le sujet ne fixe pas ce choix : le successeur donnerait un autre B-arbre tout aussi valide, d'où l'intérêt d'indiquer la règle utilisée sur la copie.", src=f"{EX28}, ex. 4 (2)", duree=8),
    o("x28e", f"Soit la fonction `what`. Quel est le résultat de `what(BT, 2)`, `what(BT, 20)`, `what(BT, 40)`, `what(BT, 41)`, `what(BT, 42)`, `what(BT, 87)` avec ce B-arbre `BT` (degré $3$) ? Que calcule `what` ?\n\n{bfig(('BT', B24_WHAT))}\n\n```python\n{WHAT}\n```",
      "| appel | résultat |\n|---|---|\n" + "\n".join(f"| `what(BT, {x})` | `{r}` |" for x, r in zip((2, 20, 40, 41, 42, 87), WHAT_RES)) +
      "\n\n`what(B, x)` retourne le **prédécesseur** de `x` : la plus grande clé strictement inférieure à `x` dans le B-arbre, si `x` est présent et n'est pas le minimum ; `None` si `x` est absent ou si c'est la plus petite clé. Dans une feuille, c'est la clé précédente, ou à défaut `p`, la dernière clé « à gauche » rencontrée pendant la descente ; dans un nœud interne, c'est la clé la plus à droite du fils gauche. Le code a été exécuté pour obtenir le tableau (corrigé rédigé).",
      src=f"{EX28}, ex. 5", duree=12),
    wg("x25a", r"Écrire la fonction `morechildren(T)` qui vérifie si chaque nœud interne de l'arbre `T` a **strictement plus de fils que son père**, avec l'implémentation premier fils - frère droit.",
       MORE, [("morechildren(T1)", "False"), ("morechildren(T2)", "True")],
       r"On passe en paramètre le nombre de fils du père (`nbc`, $0$ pour la racine). Le nombre de fils s'obtient en parcourant les frères. Parcours interrompu : la boucle `while C and morechildren(C, k)` s'arrête dès qu'un fils échoue, et on retourne `C == None` (tous les fils ont réussi). Dans $T_1$, le nœud $3$ a $2$ fils comme son père $1$ : faux ; dans $T_2$ il en a $3$ : vrai.",
       tabs={"T1": T25_1, "T2": T25_2}, figs=gfig(("T1", T25_1), ("T2", T25_2)), src=f"{EX25}, ex. 2 : Famille nombreuse", duree=15),
    wg("x25b", r"Écrire la fonction `decrease(B)` qui construit la liste des clés du B-arbre `B` en **ordre décroissant**.",
       DECR, [("decrease(B1)", "[51, 40, 38, 29, 25, 23, 21, 17, 14, 10, 7, 3]")],
       r"Parcours en ordre croissant inversé : dans un nœud interne on parcourt le dernier fils, puis la dernière clé, puis l'avant-dernier fils... et enfin le fils $0$. Dans une feuille, on lit les clés à l'envers. Arbre vide : liste vide.",
       btrees={"B1": (B21_INS, 2)}, figs=bfig(("B1", B21_INS)), src=f"{EX25}, ex. 3 : Décroissant", duree=12),
    o("x25c", f"{CONV_B} Dessiner l'arbre (principe « à la descente », uniquement l'arbre final) après insertions successives des valeurs $11$, $32$, $20$ dans ce B-arbre $B_1$ de degré $2$.\n\n{bfig(('B1', B21_INS))}",
      f"Arbre final :\n\n{bfig(('final', apply_ops(B21_INS, [('i', 11), ('i', 32), ('i', 20)], 2)))}\n\nÉtapes :\n\n{show_ins(B21_INS, [11, 32, 20], 2)}\n\nRésultat identique au corrigé officiel du contrôle.", src=f"{EX25}, ex. 4 (1)", duree=8),
    o("x25d", f"{CONV_B} Dessiner l'arbre (principe « à la descente », uniquement l'arbre final) après suppression de la valeur $15$ dans ce B-arbre $B_2$ de degré $2$.\n\n{bfig(('B2', B21_DEL))}",
      f"Arbre final :\n\n{bfig(('final', apply_ops(B21_DEL, [('d', 15)], 2)))}\n\nÉtapes :\n\n{show_del(B21_DEL, [15], 2)}\n\nRésultat identique au corrigé officiel du contrôle : la racine $[22]$ n'a que $1$ clé et le fils $[15]$ aussi, mais le fils droit {kx([27, 41])} peut prêter.", src=f"{EX25}, ex. 4 (2)", duree=8),
    o("x25e", f"Soit la fonction `mystery`. Pour chaque appel, quel est le résultat retourné et combien d'appels à `mystery` ont été effectués ? (a) `mystery(B2, 0, 92)` avec $B_2$ (degré $2$) ; (b) `mystery(B3, 0, 20)` et (c) `mystery(B3, 1, 99)` avec $B_3$ (degré $3$). Que fait `mystery(B, a, b)` ?\n\n{bfig(('B2', B21_DEL), ('B3', B21_MYS))}\n\n```python\n{MYST}\n```",
      "| appel | résultat | nombre d'appels |\n|---|---|---|\n" + "\n".join(f"| {c} | `{r}` | {n} |" for c, (r, n) in zip(("(a)", "(b)", "(c)"), MYS)) +
      "\n\nLe code a été exécuté avec un compteur : ces valeurs sont celles du corrigé officiel. `mystery(B, a, b)` vérifie que `B` est bien « ordonné » : c'est un arbre de recherche dont toutes les clés sont dans l'intervalle $[a,b]$ (clés triées dans chaque nœud, clés du fils $i$ comprises entre la clé $i-1$ et la clé $i$). Dans $B_3$, la feuille $[27, 34, 35, 42]$ contient $42>41$ (borne donnée par le père) : l'arbre n'est pas ordonné. L'appel (c) le détecte sur cette feuille, après $8$ appels ; l'appel (b) échoue plus tôt, sur le fils droit de la racine dont les clés dépassent la borne $b=20$ (aucune feuille de droite n'est visitée).",
      src=f"{EX25}, ex. 5 : Mystery", duree=12),
    wg("x19a", r"On définit l'arité moyenne d'un arbre général comme la somme des nombres de fils par nœud divisée par le nombre de nœuds **internes**. Écrire `average_arity(T)` qui retourne l'arité moyenne de l'arbre `T` si `taille(T)` $> 1$, $0$ sinon, avec l'implémentation premier fils - frère droit. (Pour l'arbre de l'énoncé : $8$ nœuds internes et $17$ fils, soit $17/8=2{,}125$.)",
       ARITY, [("average_arity(T)", "2.125"), ("average_arity(TreeAsBin(5))", "0")],
       r"On remonte le couple (nombre de liens, nombre de nœuds internes). Dans la forme binaire, le lien `child` compte pour un fils et chaque lien `sibling` pour un fils de plus : au total $T-1$ liens. Corrigé officiel (une seule fonction récursive sur la forme binaire, qui traite aussi les frères).",
       tabs={"T": G1}, figs=gfig(("T", G1)), src=f"{EX23}, ex. 2 : Arité moyenne d'un arbre général", duree=15),
    o("x19b", f"{CONV_B} Insérer successivement les clés $36$ et $42$ dans ce B-arbre de degré $2$ en appliquant le principe de précaution. Dessiner l'arbre obtenu après chaque insertion.\n\n{bfig(('B', BT_C3))}",
      f"{show_ins(BT_C3, [36, 42], 2)}\n\nRésultat identique au corrigé officiel du contrôle.", src=f"{EX23}, ex. 3 (1)", duree=8),
    wg("x19c", r"Écrire la fonction récursive `__insert(B, x)` qui insère `x` dans le B-arbre **non vide** `B`, sauf si `x` est déjà présente. Elle retourne un booléen indiquant si l'insertion a eu lieu. Utiliser le principe de précaution (éclatement à la descente) avec la procédure `split(B, i)` (éclate le fils `i`, un $2t$-nœud, de `B`, qui n'est pas un $2t$-nœud) et la fonction `search_pos(L, x)` (position de `x` dans `L`, ou celle où il devrait être). La fonction sera appelée par `insert(B, x)`, qui éclate la racine si elle est pleine.",
       INS_C3, [], r"On cherche la position `i`. Clé présente : `False`. Feuille : insertion en position `i`. Sinon, si le fils `i` est plein, on teste d'abord si sa clé médiane est `x` (alors `x` est présente, aucun éclatement inutile), sinon on éclate ce fils ; la clé médiane est montée en position `i` dans `B` et il faut descendre à droite si `x` lui est supérieure (`i += 1`). Le code a été exécuté sur dix insertions et comparé, état par état, à la fonction de contrôle d'insertion du parcours.",
       btrees={"B": (BTD, 2)}, figs=bfig(("B", BTD)), check=_check_insert, extra=INS_WRAP, src=f"{EX23}, ex. 3 (2)", duree=20),
    o("x19d", f"On exécute `build(nodes, degree)` pour construire le B-arbre ci-dessous. Quels paramètres ont été passés ?\n\n{bfig(('B', BTD))}\n\n```python\n{BUILD}\n```",
      f"`degree = 2` et `nodes = {[list(k) for k in NODES]}`.\n\nLa fonction lit `nodes` comme les nœuds du B-arbre **en parcours en largeur** : `nodes[0]` est la racine ; la file contient des couples (nœud, position dans `nodes` de son premier fils) ; un nœud à $k$ clés reçoit les $k+1$ nœuds consécutifs suivants, et `end` repère le début des fils du prochain nœud défilé. Vérifié par exécution : `build(nodes, 2)` redonne exactement l'arbre de la figure.",
      src=f"{EX23}, ex. 4 : B-arbres et mystère", duree=10),
]

LEVELS.append({"n": 13, "titre": "Examens : arbres généraux et B-arbres", "notions": ["gen-code", "gen-par", "bt-ins", "bt-del", "bt-lect"], "exos": [
    {"id": "m28", "kind": "multi", "enonce": f"Reconstitution des exercices 2 à 5 de l'{EX28} (Arbres et Recherches 2, hachage exclu, Python, $2$ h).", "parts": ["x28a", "x28b", "x28c", "x28d", "x28e"],
     "src": f"{EX28}, ex. 2 à 5", "duree": 60},
    {"id": "m25", "kind": "multi", "enonce": f"Reconstitution des exercices 2 à 5 du {EX25} (arbres généraux, B-arbres, Python).", "parts": ["x25a", "x25b", "x25c", "x25d", "x25e"],
     "src": f"{EX25}, ex. 2 à 5", "duree": 60},
    {"id": "m23", "kind": "multi", "enonce": f"Reconstitution des exercices 2 à 4 du {EX23} (arbres généraux et B-arbres, Python).", "parts": ["x19a", "x19b", "x19c", "x19d"],
     "src": f"{EX23}, ex. 2 à 4", "duree": 60},
]})


# ---------------------------------------------------------------- harder parts (level 14, about 20 % above the exams)

KEYS_AFTER = '''def keys_after(T, x):
    q = Queue()
    q.enqueue(T)
    q.enqueue(None)                # end-of-level marker
    found = False
    res = []
    while not q.isempty():
        t = q.dequeue()
        if t == None:
            if found:              # the level of the first x is finished
                return res
            if not q.isempty():
                q.enqueue(None)
        else:
            if found:
                res.append(t.key)
            elif t.key == x:
                found = True
            for C in t.children:
                q.enqueue(C)
    return res'''


def brute_after(g, x):
    cur = [g]
    while cur:
        ks = [gkey(c) for c in cur]
        if x in ks:
            return ks[ks.index(x) + 1:]
        cur = [c for n in cur for c in gch(n)]
    return []


KA = [12, 2, 0, 4, 6, 42]
assert [brute_after(G_TD, x) for x in KA] == [[], [0, 4], [4], [], [-7, 18, 9, 3, 11], []]  # the six examples of TD 1, ex. 3.4

AVGSUB = '''def _avg(B):
    """(ok, sum of the keys, number of nodes) of the subtree rooted at B (B's siblings ignored)"""
    s = B.key
    n = 1
    C = B.child
    while C != None:
        (ok, sc, nc) = _avg(C)
        if not ok or sc > B.key * nc:     # mean of the subtree C greater than the key of its father
            return (False, 0, 0)
        s += sc
        n += nc
        C = C.sibling
    return (True, s, n)


def average_subtrees(B):
    return _avg(B)[0]'''


def _mean_gt(g):
    ks = lambda t: gpre(t)  # noqa: E731
    return all(sum(ks(c)) / len(ks(c)) <= gkey(g) for c in gch(g)) and all(_mean_gt(c) for c in gch(g))


AS = [(4, [(2, [9, 5]), 1]), (15, [2, (8, [(5, [1, 4]), 3, 7]), 6]), (10, [(3, [1, 2]), (20, [5])]), 5]
AS_T = {f"B{i}": g for i, g in enumerate(AS, 1)}
assert [_mean_gt(g) for g in AS] == [False, True, False, True]

ANCESTORS = '''def ancestors(T, x):
    if T.key == x:
        return [x]
    for C in T.children:
        p = ancestors(C, x)
        if p != None:
            return [T.key] + p     # the first answer found is returned, no further search
    return None'''


def brute_path(g, x, pre_=()):
    if gkey(g) == x:
        return list(pre_) + [x]
    for c in gch(g):
        p = brute_path(c, x, tuple(pre_) + (gkey(g),))
        if p:
            return p
    return None


COUNT_RANGE = '''def count_range(B, a, b):
    """number of keys k of the B-tree B with a <= k <= b (empty tree: 0), without visiting useless subtrees"""
    if B == None:
        return 0
    i = binary_search_pos(B.keys, a)        # first key >= a
    c = 0
    if B.children == []:
        while i < B.nbkeys and B.keys[i] <= b:
            c += 1
            i += 1
        return c
    c = count_range(B.children[i], a, b)
    while i < B.nbkeys and B.keys[i] <= b:
        c += 1 + count_range(B.children[i + 1], a, b)
        i += 1
    return c'''
CR = [(20, 80), (100, 200), (0, 1000), (36, 36), (41, 72), (3, 4)]


def brute_cr(n, a, b):
    return sum(1 for k in bkeys(n) if a <= k <= b)


MAXGAP = '''def maxgap(B):
    """largest difference between two consecutive keys of a same node (0 for the empty tree)"""
    if B == None:
        return 0
    g = 0
    for i in range(B.nbkeys - 1):
        g = max(g, B.keys[i + 1] - B.keys[i])
    for C in B.children:
        g = max(g, maxgap(C))
    return g'''


def brute_gap(n):
    own = max([b - a for a, b in zip(n.keys, n.keys[1:])], default=0)
    return max([own] + [brute_gap(c) for c in n.ch])


H2A = N([40, 80, 120], N([10, 20, 30], N([5]), N([15]), N([25]), N([35, 37, 39])), N([60], N([50]), N([70])),
        N([100], N([90]), N([110])), N([140], N([130]), N([150])))
H2B = N([40], N([20], N([10]), N([30])), N([60], N([50]), N([70])))
valid(H2A, 2)
valid(H2B, 2)
OPS_H3 = [("i", 6), ("i", 8), ("i", 11), ("d", 5), ("d", 40), ("d", 0)]
ops_txt = ", ".join(("insertion de " if k == "i" else "suppression de ") + str(x) for k, x in OPS_H3)
st_h2a = steps_ins(H2A, [38, 95], 2)
st_h2b = steps_del(H2B, [10, 70, 50], 2)
fin_h3 = apply_ops(B24_INS, OPS_H3, 2)
assert count_ops(st_h2a, "split") == 3 and bheight(st_h2a[0][1]) == bheight(H2A) + 1
assert bheight(st_h2b[0][1]) < bheight(H2B)

EXTRA_PARTS += [
    wg("h1a", r"Écrire la fonction `keys_after(T, x)` qui retourne la liste des clés de l'arbre général `T` (implémentation par n-uplets) se trouvant **après la première valeur `x` trouvée, sur le même niveau que `x`**, de gauche à droite (liste vide si `x` est absent ou si `x` est le dernier de son niveau). Le parcours doit s'arrêter dès que la réponse est connue.",
       KEYS_AFTER, [(f"keys_after(T, {x})", repr(brute_after(G_TD, x))) for x in KA],
       r"Il faut les niveaux : parcours en largeur avec marqueur `None`. Tant que `x` n'est pas trouvé on l'attend ; une fois trouvé, on range les clés suivantes du même niveau ; au marqueur de fin de niveau, on retourne (parcours interrompu : inutile de parcourir les niveaux suivants). La « première valeur `x` » est la première rencontrée en largeur, donc la plus haute puis la plus à gauche. Vérifié par exécution : les six résultats sont ceux de l'énoncé du TD 1.",
       trees={"T": G_TD}, figs=gfig(("T", G_TD)), duree=20),
    wg("h1b", r"Dans un arbre général, on cherche à savoir si **aucun** nœud n'a un sous-arbre (celui de l'un de ses fils) dont la moyenne des clés est strictement supérieure à la clé de ce nœud. Écrire `average_subtrees(B)` qui vérifie cette propriété avec l'implémentation premier fils - frère droit (`TreeAsBin`). Exemple : la propriété est fausse pour l'arbre de racine $4$ dont le premier fils $2$ a deux fils $9$ et $5$ (moyenne $\\frac{16}3>4$).",
       AVGSUB, [(f"average_subtrees(B{i})", repr(_mean_gt(g))) for i, g in enumerate(AS, 1)],
       r"Parcours profondeur interrompu qui remonte un triplet (propriété vraie ?, somme des clés, nombre de nœuds) du sous-arbre de chaque fils. On compare la moyenne du fils $\frac{s_c}{n_c}>$ clé du père sans diviser : `sc > B.key * nc`. Dès qu'un sous-arbre échoue, on arrête (le résultat d'un appel récursif ne doit pas être perdu : on le teste). Les frères sont parcourus par `C.sibling` et jamais inclus dans le sous-arbre du nœud courant. Les réponses attendues sont calculées indépendamment par un contrôle direct sur les arbres de l'énoncé.",
       tabs=AS_T, figs=gfig(*[(f"B{i}", g) for i, g in enumerate(AS[:3], 1)]), duree=25),
    wg("h1c", r"Écrire la fonction `ancestors(T, x)` qui retourne la liste des clés du chemin de la racine au premier nœud de clé `x` rencontré en parcours **préfixe** (racine et `x` inclus), ou `None` si `x` est absent. Le parcours est interrompu dès que `x` est trouvé.",
       ANCESTORS, [(f"ancestors(T, {x})", repr(brute_path(G1, x))) for x in (18, 1, 13, 42)],
       r"Parcours interrompu : on ne retourne **jamais** directement le résultat de l'appel récursif. On le range dans `p`, on le teste, et on ne s'arrête que si `p != None` ; sinon on essaie le fils suivant. Le chemin se construit au retour de la récursion en ajoutant la clé du nœud en tête.",
       trees={"T": G1}, figs=gfig(("T", G1)), duree=12),
    o("h2a", f"{CONV_B} Dans ce B-arbre de degré $2$, dessiner l'arbre après l'insertion successive de $38$ puis de $95$. Combien d'éclatements ?\n\n{bfig(('B', H2A))}",
      f"{show_ins(H2A, [38, 95], 2)}\n\nLa racine, un nœud du deuxième niveau et la feuille {kx([35, 37, 39])} sont tous pleins sur le chemin de $38$ : trois éclatements consécutifs dans la même descente (racine, puis nœud interne, puis feuille), et la hauteur passe de ${bheight(H2A)}$ à ${bheight(st_h2a[0][1])}$. L'insertion de $95$ ne déclenche rien.", duree=15),
    o("h2b", f"{CONV_B} {CONV_D} Dans ce B-arbre de degré $2$, dont tous les nœuds ont le minimum de clés, dessiner l'arbre après la suppression successive de $10$, $70$ puis $50$.\n\n{bfig(('B', H2B))}",
      f"{show_del(H2B, [10, 70, 50], 2)}\n\nTous les nœuds ont $t-1=1$ clé : la racine et ses deux fils fusionnent d'abord (la hauteur diminue), puis une deuxième fusion a lieu au niveau des feuilles avant de supprimer $10$. Chaque fusion de deux nœuds à $t-1$ clés fournit un nœud plein ($3$ clés), qui peut ensuite perdre une clé sans autre transformation.", duree=15),
    wg("h2c", r"Écrire la fonction `count_range(B, a, b)` qui retourne le nombre de clés $k$ du B-arbre `B` (éventuellement vide, `None`) telles que `a <= k <= b`, **sans visiter les sous-arbres inutiles** (utiliser `binary_search_pos(L, x)`, position de `x` dans la liste triée `L` ou celle où il devrait être).",
       COUNT_RANGE, [(f"count_range(B, {a}, {b})", str(brute_cr(B24_WHAT, a, b))) for a, b in CR] + [("count_range(None, 1, 2)", "0")],
       r"Comme pour une recherche, on saute au fils `i` où devrait se trouver `a`. On compte ensuite les clés tant qu'elles restent $\le b$, chacune accompagnée de tout son fils de droite ; dès qu'une clé dépasse $b$ on s'arrête : les fils suivants sont hors intervalle. Au plus un chemin de descente par borne : coût $O(h+k)$ lectures de nœuds pour $k$ résultats. Résultats vérifiés contre un comptage direct sur la liste triée des clés.",
       btrees={"B": (B24_WHAT, 3)}, figs=bfig(("B", B24_WHAT)), duree=25),
    o("h3a", f"{CONV_B} {CONV_D} Dans ce B-arbre de degré $2$ on effectue successivement : {ops_txt}. Dessiner l'arbre après chaque opération.\n\n{bfig(('B', B24_INS))}",
      show_ops(B24_INS, OPS_H3, 2)[0] + "\n\nLe suivi montre les deux sens de variation de la hauteur : un éclatement de la racine la fait croître, une fusion qui vide la racine la fait diminuer.", duree=20),
    v("h3b", f"{CONV_B} {CONV_D} Combien de nœuds a le B-arbre de degré $2$ obtenu après les opérations suivantes : {ops_txt} (à partir de l'arbre ci-dessous) ?\n\n{bfig(('B', B24_INS))}",
      bcount(fin_h3), f"Arbre final :\n\n{bfig(('final', fin_h3))}\n\n{show_ops(B24_INS, OPS_H3, 2)[0]}", duree=12),
    wg("h3c", r"On appelle **gap** d'un nœud d'un B-arbre l'écart maximum entre deux clés consécutives de ce nœud. Le gap maximum d'un B-arbre est le maximum des gaps de ses nœuds. Écrire `maxgap(B)` qui le calcule (arbre vide : $0$).",
       MAXGAP, [("maxgap(B)", str(brute_gap(B24_WHAT))), ("maxgap(None)", "0")],
       r"Un nœud à une seule clé a un gap nul. Parcours profondeur : maximum entre le gap du nœud et celui de chacun de ses fils. Résultat vérifié contre un calcul direct par un autre programme (sur l'arbre de l'énoncé, le gap maximum est celui du nœud interne $[7\;20\;35]$ : $35-20=15$).",
       btrees={"B": (B24_WHAT, 3)}, figs=bfig(("B", B24_WHAT)), duree=12),
]

LEVELS.append({"n": 14, "titre": "Plus dur que l'examen : arbres généraux, B-arbres, mélange", "notions": ["gen-code", "bt-lect", "bt-ins", "bt-del"], "exos": [
    {"id": "m31", "kind": "multi", "enonce": "Trois fonctions sur les arbres généraux, avec parcours interrompu (largeur, profondeur, propriété sur les sous-arbres).", "parts": ["h1a", "h1b", "h1c"], "duree": 60},
    {"id": "m32", "kind": "multi", "enonce": "B-arbres de degré 2 : insertion avec éclatements en cascade, suppression avec fusions jusqu'à la racine, et un comptage par intervalle.", "parts": ["h2a", "h2b", "h2c"], "duree": 60},
    {"id": "m33", "kind": "multi", "enonce": "B-arbres : suite d'opérations mélangées (insertions et suppressions), nombre de nœuds final et gap maximum.", "parts": ["h3a", "h3b", "h3c"], "duree": 60},
]})


# ---------------------------------------------------------------- variants, quiz, formulas

def _ops_sol(start, xs, t, kind):
    return show_ins(start, xs, t) if kind == "i" else show_del(start, xs, t)


_d1 = [15, 22, 8, 20, 30]
_d2 = [8, 12, 15, 18, 19, 20]
_d3 = [15, 22, 8, 20, 30, 18, 45]
_dd = [18, 20, 30]
_q = [10, 20, 30, 40, 50, 60, 70, 80]
_s2 = steps_ins(B21_INS, [11, 32, 20], 2)
_sq = steps_ins(None, _q, 2)
_a30 = steps_ins(None, list(range(1, 31)), 2)
_a40 = steps_ins(None, list(range(1, 41)), 2)
_dd1 = steps_del(BTD, _d1, 2)
_dd2 = steps_del(BTD, _d2, 2)
_dd3 = steps_del(BTD, _d3, 2)

VARIANTS = {
    "b11": [vv(f"{CONV_H} Quelle est la hauteur de l'arbre binaire $B$ ?\n\n{fig(('B', TB2))}", mb["B2"]["H"], f"Le nœud le plus profond est ${deepest(TB2)[0]}$, à la profondeur ${deepest(TB2)[1]}$.")],
    "b12": [vv(f"Combien l'arbre binaire $B$ a-t-il de feuilles ?\n\n{fig(('B', TB3))}", mb["B3"]["Nbe"], "Une feuille est un nœud sans fils : on les compte.")],
    "b13": [vv(f"Longueur de cheminement $LC$ de $B$ (racine à $0$) ?\n\n{fig(('B', TB2))}", mb["B2"]["LC"], f"$LC=LCE+LCI={mb['B2']['LCE']}+{mb['B2']['LCI']}$.")],
    "b14": [vv(r"Nombre maximal de nœuds d'un arbre binaire de hauteur $7$ (racine à $0$) ?", 2 ** 8 - 1, r"$\sum_{p=0}^{7}2^p=2^8-1$.")],
    "r21": [vv(f"On insère successivement les clés ${lst(BS2)}$ dans un ABR vide. Quelle est la hauteur de l'arbre obtenu ?", hb(bst(BS2)),
               f"Arbre obtenu :\n\n{fig(('ABR', bst(BS2)))}")],
    "r22": [vv(f"On insère successivement les clés ${lst(BS3)}$ dans un ABR vide. Quelle est la $7^e$ clé dans le parcours infixe ?", ino(bst(BS3))[6],
               f"Infixe $=$ ordre croissant : ${lst(ino(bst(BS3)))}$.")],
    "r23": [vv(r"Nombre minimal de nœuds d'un AVL de hauteur $7$ (racine à $0$) ?", avl_min(7), r"$N(7)=N(6)+N(5)+1=33+20+1$.")],
    "r24": [vv(r"On insère $1,2,\dots,15$ dans cet ordre dans un AVL vide. Quelle est la clé à la racine ?", key(avl(range(1, 16))),
               r"Insertions croissantes dans un AVL : l'arbre final est parfait, la racine est la clé médiane $8$.")],
    "g31": [vv(f"{CONV_H} Hauteur de l'arbre général $T$ ?\n\n{gfig(('T', GA))}", gheight(GA), gmeasure_sol(GA))],
    "g32": [vv(f"Combien l'arbre général $T$ a-t-il de feuilles ?\n\n{gfig(('T', GB))}", gleaves(GB), gmeasure_sol(GB))],
    "g33": [vv(f"Arité de l'arbre $T$ (maximum des arités des nœuds) ?\n\n{gfig(('T', GD))}", garity(GD), gmeasure_sol(GD))],
    "g34": [vv(f"Arité moyenne de $T$ (somme des nombres de fils divisée par le nombre de nœuds internes, fraction) ?\n\n{gfig(('T', GA))}", avg_arity(GA), gmeasure_sol(GA))],
    "g35": [vv(f"Profondeur moyenne interne $PMI$ de $T$ (racine à $0$, fraction) ?\n\n{gfig(('T', GD))}", pmi(GD), gmeasure_sol(GD))],
    "p41": [vv(f"Hauteur de l'arbre binaire premier fils - frère droit de $T$ (racine à $0$) ?\n\n{gfig(('T', GA))}", measures(fcrs_bin(GA))["H"],
               f"{fig(('B', fcrs_bin(GA)))}")],
    "p43": [vv(f"Quelle est la hauteur de l'arbre représenté par `{glinear(GC)}` (racine à $0$) ?", gheight(GC), f"{gfig(('T', GC))}")],
    "p44": [vv(f"Combien de liens `sibling` de la forme premier fils - frère droit de $T$ sont différents de `None` ?\n\n{gfig(('T', GD))}", count_siblings(GD),
               f"$T-1-N_i={gsize(GD) - 1}-{gsize(GD) - gleaves(GD)}$.")],
    "q51": [vv(f"Rang du nœud $6$ dans le parcours préfixe de $T$ ?\n\n{gfig(('T', GB))}", gpre(GB).index(6) + 1, f"Préfixe : ${lst(gpre(GB))}$.")],
    "q52": [vv(f"Rang du nœud $6$ dans le parcours suffixe de $T$ ?\n\n{gfig(('T', GA))}", gpost(GA).index(6) + 1, f"Suffixe : ${lst(gpost(GA))}$.")],
    "q53": [vv(f"Rang du nœud $80$ dans le parcours en largeur de $T$ ?\n\n{gfig(('T', GD))}", gbfs(GD).index(80) + 1, f"Largeur : ${lst(gbfs(GD))}$.")],
    "q54": [vv(_cp_enonce(GA, "three"), prints(GA)["three"], _cp_sol(GA))],
    "q55": [vv(f"$11^e$ élément du vecteur préfixe - suffixe (chaque clé placée à la première et à la dernière rencontre du parcours profondeur) de $T$ ?\n\n{gfig(('T', GD))}",
               prefsuff(GD)[10], f"Vecteur : ${lst(prefsuff(GD))}$.")],
    "t71": [vv(r"Nombre maximal de clés d'un nœud d'un B-arbre de degré $t=8$ ?", 15, r"$2t-1=15$.")],
    "t72": [vv(r"Nombre minimal de clés d'un nœud non racine d'un B-arbre de degré $t=9$ ?", 8, r"$t-1=8$.")],
    "t73": [vv(r"Nombre maximal de clés d'un B-arbre de degré $t=4$ et de hauteur $2$ ?", keys_max_tree(4, 2), r"$(2t)^{h+1}-1=8^3-1$.")],
    "t74": [vv(r"Nombre minimal de clés d'un B-arbre de degré $t=4$ et de hauteur $3$ ?", keys_min_tree(4, 3), r"$2t^h-1=2\times4^3-1$.")],
    "t75": [vv(r"Un nœud d'un B-arbre contient au plus $15$ clés. Quel est le degré $t$ ?", 8, r"$2t-1=15$.")],
    "u81": [vv(r"Hauteur maximale d'un B-arbre de degré $t=2$ contenant $500$ clés ?", hmax(2, 500), r"$2\times2^h-1\le500$ donne $2^h\le250{,}5$ : $h\le7$.")],
    "u82": [vv(r"Hauteur minimale d'un B-arbre de degré $t=3$ contenant $500$ clés ?", hmin(3, 500), r"$6^{h+1}-1\ge500$ : $6^3=216 < 501$, $6^4=1296$, donc $h+1=4$.")],
    "u83": [vv(f"Combien de nœuds lit-on pour chercher la clé $15$ dans ce B-arbre ?\n\n{bfig(('B', BTD))}", len(search_path(BTD, 15)), "La clé $15$ est dans le fils gauche de la racine.")],
    "u84": [vv(f"Prédécesseur de $87$ dans ce B-arbre ?\n\n{bfig(('B', B24_WHAT))}", pred_of(B24_WHAT, 87), "$87$ est la première clé de sa feuille : son prédécesseur est la clé du père qui la précède, $83$.")],
    "u85": [vv(f"$8^e$ clé du parcours croissant de ce B-arbre ?\n\n{bfig(('B', B21_INS))}", bkeys(B21_INS)[7], f"Parcours : ${lst(bkeys(B21_INS))}$.")],
    "i91": [vv(f"{CONV_B} Combien d'éclatements a-t-on effectués après l'insertion successive de $11$, $32$ puis $20$ dans ce B-arbre de degré $2$ ?\n\n{bfig(('B', B21_INS))}", count_ops(_s2, "split"), show_ins(B21_INS, [11, 32, 20], 2))],
    "i92": [vv(r"On éclate un nœud plein d'un B-arbre de degré $t=4$ contenant $[2\;5\;8\;11\;14\;17\;20]$. Quelle clé monte dans le père ?", 11, r"La médiane, d'indice $t-1=3$ : $11$.")],
    "i94": [vv(f"Combien de nœuds a le B-arbre de degré $2$ obtenu par insertions successives de ${lst(_q)}$ dans un arbre vide ?", bcount(_sq[-1][1]), f"{bfig(('final', _sq[-1][1]))}")],
    "i95": [vv(r"On insère $1,2,\dots,30$ dans cet ordre dans un B-arbre de degré $2$ vide. Quelle est la hauteur finale ?", bheight(_a30[-1][1]), f"{bfig(('final', _a30[-1][1]))}")],
    "i104": [vv(r"On insère $1,2,\dots,40$ dans cet ordre dans un B-arbre de degré $2$ initialement vide. Combien d'éclatements au total ?", count_ops(_a40, "split"),
                f"Hauteur finale ${bheight(_a40[-1][1])}$, ${bcount(_a40[-1][1])}$ nœuds : $1+\\text{{éclatements}}+h={bcount(_a40[-1][1])}$.")],
    "d112": [vv(f"{CONV_D} Combien de rotations effectue-t-on en supprimant successivement ${lst(_d2)}$ dans ce B-arbre de degré $2$ ?\n\n{bfig(('B', BTD))}",
                count_ops(_dd2, "rotate-left") + count_ops(_dd2, "rotate-right"), show_del(BTD, _d2, 2))],
    "d113": [vv(f"{CONV_D} Combien de fusions effectue-t-on en supprimant successivement ${lst(_d1)}$ dans ce B-arbre de degré $2$ ?\n\n{bfig(('B', BTD))}",
                count_ops(_dd1, "merge"), show_del(BTD, _d1, 2))],
    "d123": [vv(f"{CONV_D} Hauteur de l'arbre après suppression successive de ${lst(_d3)}$ dans ce B-arbre de degré $2$ ?\n\n{bfig(('B', BTD))}",
                bheight(final_del(BTD, _d3, 2)), show_del(BTD, _d3, 2))],
    "d124": [vv(f"{CONV_D} Combien de rotations effectue-t-on en supprimant successivement ${lst(_d3)}$ dans ce B-arbre de degré $2$ ?\n\n{bfig(('B', BTD))}",
                count_ops(_dd3, "rotate-left") + count_ops(_dd3, "rotate-right"), show_del(BTD, _d3, 2))],
}
_ops2 = [("d", 4), ("i", 3), ("i", 1), ("d", 45)]
VARIANTS["h3b"] = [vv(f"{CONV_B} {CONV_D} Combien de nœuds a le B-arbre de degré $2$ obtenu après : suppression de $4$, insertion de $3$, insertion de $1$, suppression de $45$ (à partir de l'arbre ci-dessous) ?\n\n{bfig(('B', B24_INS))}",
                        bcount(apply_ops(B24_INS, _ops2, 2)), show_ops(B24_INS, _ops2, 2)[0])]
for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["id"] in VARIANTS:
            _e["variants"] = VARIANTS[_e["id"]]
for _e in EXTRA_PARTS:
    if _e["id"] in VARIANTS:
        _e["variants"] = VARIANTS[_e["id"]]
assert all(i in {e["id"] for L in LEVELS for e in L["exos"]} | {e["id"] for e in EXTRA_PARTS} for i in VARIANTS)
assert not [e["id"] for L in LEVELS for e in L["exos"] if e["kind"] == "value" and "variants" not in e]
assert not [e["id"] for e in EXTRA_PARTS if e["kind"] == "value" and "variants" not in e]

QUIZ = [
    {"notion": "bin", "type": "qcm", "q": r"Nombre maximal de nœuds d'un arbre binaire de hauteur $h$ (racine à $0$) :", "choix": [r"$2^{h+1}-1$", r"$2^h$", r"$2h+1$", r"$2^{h}-1$"], "bonne": 0},
    {"notion": "bin", "type": "vf", "q": r"La hauteur d'un arbre binaire réduit à sa racine vaut $0$.", "bonne": True},
    {"notion": "abr", "type": "qcm", "q": r"Quel parcours d'un ABR donne les clés en ordre croissant ?", "choix": [r"infixe", r"préfixe", r"suffixe", r"largeur"], "bonne": 0},
    {"notion": "abr", "type": "vf", "q": r"Dans un AVL, les hauteurs des deux sous-arbres d'un nœud diffèrent d'au plus $1$.", "bonne": True},
    {"notion": "gen-mes", "type": "vf", "q": r"Un arbre général peut être vide.", "bonne": False},
    {"notion": "gen-mes", "type": "qcm", "q": r"Un arbre général a $T$ nœuds dont $N_i$ internes. Son arité moyenne vaut :", "choix": [r"$\frac{T-1}{N_i}$", r"$\frac{T}{N_i}$", r"$\frac{T-1}{T}$", r"$\frac{N_i}{T-1}$"], "bonne": 0},
    {"notion": "gen-rep", "type": "qcm", "q": r"Dans la forme premier fils - frère droit, une feuille a :", "choix": [r"`child == None`", r"`sibling == None`", r"`child` et `sibling` vides", r"un `sibling` non vide"], "bonne": 0},
    {"notion": "gen-rep", "type": "vf", "q": r"La racine d'un arbre en premier fils - frère droit a toujours `sibling == None`.", "bonne": True},
    {"notion": "gen-par", "type": "qcm", "q": r"Le parcours suffixe d'un arbre général visite :", "choix": [r"les fils puis la racine", r"la racine puis les fils", r"niveau par niveau", r"les feuilles seulement"], "bonne": 0},
    {"notion": "gen-par", "type": "vf", "q": r"Pour repérer les changements de niveau dans un parcours en largeur, on réenfile le marqueur même quand la file est vide.", "bonne": False},
    {"notion": "gen-code", "type": "vf", "q": r"Dans un parcours interrompu, on peut retourner directement le résultat de l'appel récursif.", "bonne": False},
    {"notion": "gen-code", "type": "qcm", "q": r"La hauteur d'un arbre général est :", "choix": [r"$\max(1+\text{hauteur d'un fils})$, $0$ pour une feuille", r"le nombre de nœuds", r"le nombre de feuilles", r"$1+$ la hauteur du premier fils"], "bonne": 0},
    {"notion": "bt-def", "type": "qcm", "q": r"Un nœud non racine d'un B-arbre de degré $t$ contient :", "choix": [r"de $t-1$ à $2t-1$ clés", r"de $t$ à $2t$ clés", r"de $1$ à $2t-1$ clés", r"exactement $t$ clés"], "bonne": 0},
    {"notion": "bt-def", "type": "vf", "q": r"Toutes les feuilles d'un B-arbre sont à la même profondeur.", "bonne": True},
    {"notion": "bt-def", "type": "qcm", "q": r"Nombre maximal de clés d'un B-arbre de degré $2$ et de hauteur $1$ :", "choix": [r"$15$", r"$7$", r"$3$", r"$16$"], "bonne": 0},
    {"notion": "bt-lect", "type": "qcm", "q": r"Où se trouve la plus grande clé d'un B-arbre ?", "choix": [r"dernière clé de la feuille la plus à droite", r"dernière clé de la racine", r"première clé de la dernière feuille", r"dans un nœud interne"], "bonne": 0},
    {"notion": "bt-lect", "type": "vf", "q": r"Pour un nœud interne, le prédécesseur de la clé $i$ est la clé la plus à droite du fils $i$.", "bonne": True},
    {"notion": "bt-ins", "type": "qcm", "q": r"Dans un B-arbre de degré $t$, on éclate un nœud plein. Quelle clé monte ?", "choix": [r"la médiane (indice $t-1$)", r"la plus petite", r"la plus grande", r"une clé au hasard"], "bonne": 0},
    {"notion": "bt-ins", "type": "vf", "q": r"La hauteur d'un B-arbre n'augmente que lorsque la racine est éclatée.", "bonne": True},
    {"notion": "bt-ins", "type": "vf", "q": r"Avec le principe de précaution, insérer une clé déjà présente ne modifie jamais l'arbre.", "bonne": False},
    {"notion": "bt-del", "type": "qcm", "q": r"On descend dans un fils à $t-1$ clés, un frère a $t$ clés. On fait :", "choix": [r"une rotation", r"une fusion", r"un éclatement", r"rien"], "bonne": 0},
    {"notion": "bt-del", "type": "vf", "q": r"La fusion de deux nœuds à $t-1$ clés avec le séparateur donne un nœud à $2t-1$ clés.", "bonne": True},
    {"notion": "bt-del", "type": "qcm", "q": r"Une suppression à la descente vide la racine. Alors :", "choix": [r"la hauteur diminue de $1$", r"la hauteur augmente de $1$", r"l'arbre est vide", r"on éclate un fils"], "bonne": 0},
]

for _i, _q_ in enumerate(QUIZ):  # spread the right answer over the four positions
    if _q_["type"] == "qcm":
        _ch = _q_["choix"][1:]
        _ch.insert(_i % 4, _q_["choix"][0])
        _q_["choix"], _q_["bonne"] = _ch, _i % 4

_LF = {
    1: r"$T$ · hauteur : racine $=0$ · feuille : aucun fils · au plus $2^{h+1}-1$ nœuds · $LC=\sum$ profondeurs",
    2: r"ABR : infixe $=$ ordre croissant · AVL : $|h(G)-h(D)|\le1$ · $N(h)=N(h-1)+N(h-2)+1$",
    3: r"arcs $=T-1=\sum$ arités · arité moyenne $=\frac{T-1}{N_i}$ · $PMI=\frac{LCI}{N_i}$ · hauteur : racine $=0$",
    4: r"tuple : `children` · binaire : `child`, `sibling` · `sibling` non vides $=T-1-N_i$ · linéaire `(o A1 ... AN)`",
    5: r"préfixe : racine, fils · suffixe : fils, racine · largeur : file · un affichage par appel $\Rightarrow T$",
    6: r"`taille` $=1+\sum$ · `hauteur` $=\max(1+h_{fils})$ · largeur : file + marqueur `None` · `C = C.sibling`",
    7: r"nœud : $t-1$ à $2t-1$ clés · $k$ clés $\Rightarrow k+1$ fils · max $(2t)^{h+1}-1$ · min $2t^h-1$",
    8: r"$n\ge2t^h-1$ donc $h\le\log_t\frac{n+1}2$ · $n\le(2t)^{h+1}-1$ · recherche : $\le h+1$ nœuds · prédécesseur : clé la plus à droite du fils gauche",
    9: r"éclater : médiane (indice $t-1$) monte · racine pleine : hauteur $+1$ · nœuds $=1+$ éclatements $+h$",
    10: r"éclatement à la descente · médiane vers le père · racine pleine : nouvelle racine · doublon : peut éclater",
    11: r"rotation gauche/droite si un frère a $\ge t$ clés · sinon fusion avec le séparateur · prédécesseur d'une clé interne",
    12: r"rotation, fusion, prédécesseur avant successeur · racine vide : hauteur $-1$ · clé absente : arbre peut changer",
}
FORMULES = {e["id"]: _LF[lvl["n"]] for lvl in LEVELS for e in lvl["exos"] if e["kind"] != "multi"}
FORMULES.update({
    "x28a": r"parcours profondeur · $PMI=\frac{LCI}{N_i}$ · couple (nombre internes, somme des profondeurs)",
    "x28b": r"arité par parcours des frères · parcours profondeur interrompu · `C = C.sibling`",
    "x28c": r"éclater les nœuds pleins à la descente · médiane vers le père · racine pleine : hauteur $+1$",
    "x28d": r"rotation si un frère a $\ge t$ clés · sinon fusion · prédécesseur d'une clé interne",
    "x28e": r"`binary_search_pos` · prédécesseur : clé la plus à droite du fils gauche · parcours en descente avec mémoire `p`",
    "x25a": r"nombre de fils du père en paramètre · `C = C.sibling` · parcours interrompu",
    "x25b": r"parcours croissant inversé · dernier fils d'abord · feuille : clés à l'envers",
    "x25c": r"éclater les nœuds pleins à la descente · médiane vers le père",
    "x25d": r"rotation gauche (frère droit à $\ge t$ clés) · prédécesseur ou successeur d'une clé interne",
    "x25e": r"arbre de recherche : clés triées dans $[a,b]$ · clé $i$ borne le fils $i$ · compte des appels",
    "x19a": r"arité moyenne $=\frac{T-1}{N_i}$ · liens $child$ et $sibling$ · couple (liens, nœuds internes)",
    "x19b": r"éclater les nœuds pleins à la descente · racine pleine : hauteur $+1$",
    "x19c": r"`search_pos` · éclater le fils plein avant d'y descendre · `i += 1` si $x>$ médiane",
    "x19d": r"parcours en largeur · $k$ clés $\Rightarrow k+1$ fils consécutifs · `end` = début des fils suivants",
    "h1a": r"largeur avec marqueur `None` · parcours interrompu · fin de niveau",
    "h1b": r"couple (ok, somme, nombre) · moyenne $>$ clé $\iff s_c>\text{clé}\times n_c$ · parcours des frères",
    "h1c": r"parcours interrompu : tester le résultat de l'appel · chemin reconstruit au retour",
    "h2a": r"éclatements en cascade · médiane vers le père · racine pleine : hauteur $+1$",
    "h2b": r"fusion si fils et frère à $t-1$ clés · racine vide : hauteur $-1$ · prédécesseur",
    "h2c": r"`binary_search_pos` · descente vers $a$ · arrêt dès une clé $>b$ · fils droit de chaque clé comptée",
    "h3a": r"éclatement à la descente · rotation, fusion · racine éclatée ou vide : hauteur $\pm1$",
    "h3b": r"nœuds $=1+$ éclatements $+h$ (insertions seules) · fusions : $-1$ nœud",
    "h3c": r"gap d'un nœud $=\max(k_{i+1}-k_i)$ · maximum sur tous les nœuds · arbre vide : $0$",
})

assert len(CHECKED) == len(set(CHECKED)), "duplicate exercise id"
_ids = [e["id"] for L in LEVELS for e in L["exos"]] + [e["id"] for e in EXTRA_PARTS]
assert len(_ids) == len(set(_ids)), "duplicate exercise id"
