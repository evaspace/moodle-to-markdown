"""Level path: S2 algorithmics, search trees (Algo-S2-AR: heaps, binary search trees, AVL; exam B4 in May, Python, 2 h).

Sources: no Moodle course for S2 algo on the server; calibrated on Epidocs Past-Exams (PDFs in `annales/raw/S2`):
TDs of March-April 2026 (`TDs/2030/Algo/B4`: td1 heaps, td2 BST, td « AVL » with its official correction), the B4
exam of 11 May 2026 (`Finals/Algo/2030`, scan, no correction), the P2 exams of 30 May 2018 (`Finals/Algo/2022`) and
22 May 2019 (`Finals/Algo/2023`) with their official corrections. Figures were read from the PDFs and typed as
tuple specs (see `algo_abg`).

Checks at import (build.py imports this module, so a wrong answer stops the build):
- every answer about a figure (heap vectors, BST built by leaf or root insertion, deletions, AVL built or modified,
  rotations applied, 2-3-4 validity, mystery results) is computed by the reference engines below, never typed;
- the rotation lists printed by the official corrections are asserted against the AVL engine;
- `w()` runs the model code on BinTree / BinTreeSize / AVL objects built from the figures and replays the `>>>`
  session; returned trees are compared node by node, sizes and balance factors are checked on every node;
- `algo_abg._api` enforces the exam annex (plus `abs`, `AVL`, the rotations and `pop` where the annex gives them).
The official AVL deletion (td « AVL » correction, line 37) tests `A.right.bal == -1` after a deletion on the right:
it must be `A.left.bal == -1` (asserted below: the official code crashes on 3(1(., 2), 4) minus 4); the path teaches the fixed test.
"""
from . import algo_abg as abg
from .algo_python import _out, _py, _session

SUBJECT = {
    "id": "algo-s2-recherche",
    "ordre": 640,
    "matiere": "algo",
    "semestre": "S2",
    "ecue": "Arbres de recherche",
    "titre": "Arbres de recherche : tas, arbres binaires de recherche, AVL",
    "chapitres_moodle": [],
    "td": "TD Algo-S2-AR de mars-avril 2026 (tas, ABR, AVL), examen B4 de mai 2026, partiels P2 de 2018 et 2019",
    "examens": ["Examen écrit B4 d'algorithmique, arbres de recherche (Python, 2 h, mai)"],
}

CHECKED = []
S = "Calé sur les TD Algo-S2-AR 2026 et l'examen B4 du 11 mai 2026 (Past-Exams S2/TDs/2030/Algo/B4, S2/Finals/Algo/2030)"
TD1 = "TD 1 Algo-S2-AR, tas, mars 2026 (Past-Exams S2/TDs/2030/Algo/B4)"
TD2 = "TD 2 Algo-S2-AR, arbres binaires de recherche, mars 2026 (Past-Exams S2/TDs/2030/Algo/B4)"
TD3 = "TD Algo-S2-AR « AVL », avril 2026, et son corrigé officiel (Past-Exams S2/TDs/2030/Algo/B4)"
P18 = "Partiel P2 du 30 mai 2018, corrigé officiel (Past-Exams S2/Finals/Algo/2022)"
P19 = "Partiel P2 du 22 mai 2019, corrigé officiel (Past-Exams S2/Finals/Algo/2023)"
B26 = "Examen B4 du 11 mai 2026 (Past-Exams S2/Finals/Algo/2030, scan), pas de corrigé officiel"
RULE = ("Annexe de l'examen : arbre vide `None`, sinon `BinTree(key, left, right)` (ou `BinTreeSize` avec `size`, "
        "`AVL` avec `bal`) ; seuls `len`, `range`, `append`, `min`/`max` à deux valeurs ; aucun opérateur sur les listes.")
AVL_RULE = "Annexe : rotations avec mise à jour des déséquilibres `lr` (gauche), `rr` (droite), `lrr` (gauche-droite), `rlr` (droite-gauche)."

# ---------------------------------------------------------------- annex classes and reference engines


class AVL:
    def __init__(self, key, left, right, bal):
        self.key = key
        self.left = left
        self.right = right
        self.bal = bal


def _h(B):
    return -1 if B is None else 1 + max(_h(B.left), _h(B.right))


class _N:
    def __init__(self, key, left=None, right=None):
        self.key, self.left, self.right = key, left, right


def _node(s):
    if s is None:
        return None
    left, right = abg.kids(s)
    return _N(abg.key(s), _node(left), _node(right))


def bst_leaf(keys, s=None):
    """BST built by leaf insertion (equal keys go left)."""
    def ins(n, x):
        if n is None:
            return _N(x)
        if x <= n.key:
            n.left = ins(n.left, x)
        else:
            n.right = ins(n.right, x)
        return n
    n = _node(s)
    for x in keys:
        n = ins(n, x)
    return abg.spec(n)


def bst_root(keys, s=None):
    """BST built by root insertion (cut into keys <= x and keys > x)."""
    def cut(n, x):
        if n is None:
            return None, None
        if x < n.key:
            left, right = cut(n.left, x)
            n.left = right
            return left, n
        left, right = cut(n.right, x)
        n.right = left
        return n, right
    n = _node(s)
    for x in keys:
        left, right = cut(n, x)
        n = _N(x, left, right)
    return abg.spec(n)


def _maxn(n):
    while n.right is not None:
        n = n.right
    return n.key


def bst_del(s, keys):
    """BST deletion; a double node takes the maximum of its left subtree."""
    def d(n, x):
        if n is None:
            return None
        if x == n.key:
            if n.left is None:
                return n.right
            if n.right is None:
                return n.left
            n.key = _maxn(n.left)
            n.left = d(n.left, n.key)
        elif x < n.key:
            n.left = d(n.left, x)
        else:
            n.right = d(n.right, x)
        return n
    n = _node(s)
    for x in keys:
        n = d(n, x)
    return abg.spec(n)


def _bal(n):
    return _h(n.left) - _h(n.right)


def _rg(n):
    r = n.right
    n.right, r.left = r.left, n
    return r


def _rd(n):
    lft = n.left
    n.left, lft.right = lft.right, n
    return lft


def _fix(n, log):
    b = _bal(n)
    if b == 2:
        if _bal(n.left) == -1:
            log.append(f"rgd({n.key})")
            n.left = _rg(n.left)
        else:
            log.append(f"rd({n.key})")
        return _rd(n)
    if b == -2:
        if _bal(n.right) == 1:
            log.append(f"rdg({n.key})")
            n.right = _rd(n.right)
        else:
            log.append(f"rg({n.key})")
        return _rg(n)
    return n


def avl_ins(keys, s=None, log=None):
    """AVL built by leaf insertions with rebalancing on the way up; rotations appended to `log` (French names)."""
    log = [] if log is None else log

    def ins(n, x):
        if n is None:
            return _N(x)
        if x < n.key:
            n.left = ins(n.left, x)
        elif x > n.key:
            n.right = ins(n.right, x)
        return _fix(n, log)
    n = _node(s)
    for x in keys:
        n = ins(n, x)
    return abg.spec(n)


def avl_del(s, keys, log=None):
    """AVL deletion (double node: maximum of the left subtree), rebalancing on the way up."""
    log = [] if log is None else log

    def d(n, x):
        if n is None:
            return None
        if x == n.key:
            if n.left is None:
                return n.right
            if n.right is None:
                return n.left
            n.key = _maxn(n.left)
            n.left = d(n.left, n.key)
        elif x < n.key:
            n.left = d(n.left, x)
        else:
            n.right = d(n.right, x)
        return _fix(n, log)
    n = _node(s)
    for x in keys:
        n = d(n, x)
    return abg.spec(n)


def is_avl(s):
    n = _node(s)

    def ok(m):
        return m is None or (abs(_bal(m)) <= 1 and ok(m.left) and ok(m.right))
    return ok(n) and abg.ino(s) == sorted(abg.ino(s))


def bals(s):
    """Balance factors in prefix order, as text."""
    out = []

    def go(m):
        if m is not None:
            b = _bal(m)
            out.append(f"{m.key} : {'+' if b > 0 else ''}{b}")
            go(m.left)
            go(m.right)
    go(_node(s))
    return " · ".join(out)


def heap_spec(H, i=1):
    """Values of a heap vector (index 0 unused) as a tree spec."""
    if i >= len(H):
        return None
    left, right = heap_spec(H, 2 * i), heap_spec(H, 2 * i + 1)
    return H[i][0] if left is None and right is None else (H[i][0], left, right)


def is234(t, lo=None, hi=None):
    """(keys, children) 2-3-4 node: 1-3 sorted keys in (lo, hi), 0 or len(keys)+1 children, leaves on one level."""
    def depths(t, d=0):
        return {d} if not t[1] else {x for c in t[1] for x in depths(c, d + 1)}

    def ok(t, lo, hi):
        ks, ch = t
        if not 1 <= len(ks) <= 3 or list(ks) != sorted(ks) or len(set(ks)) != len(ks):
            return False
        if any((lo is not None and k <= lo) or (hi is not None and k >= hi) for k in ks):
            return False
        if not ch:
            return True
        if len(ch) != len(ks) + 1:
            return False
        bounds = [lo, *ks, hi]
        return all(ok(c, bounds[i], bounds[i + 1]) for i, c in enumerate(ch))
    return ok(t, lo, hi) and len(depths(t)) == 1


def t234(t, ind=0):
    """2-3-4 tree as indented text."""
    ks, ch = t
    return "\n".join([" " * ind + "[" + " ".join(map(str, ks)) + "]"] + [t234(c, ind + 4) for c in ch])


# ---------------------------------------------------------------- exercise builders


def _build(s, kind):
    if s is None:
        return None
    left, right = abg.kids(s)
    L, R = _build(left, kind), _build(right, kind)
    k = abg.key(s)
    if kind == "size":
        return abg.BinTreeSize(k, L, R, 1 + (L.size if L else 0) + (R.size if R else 0))
    if kind == "avl":
        return AVL(k, L, R, _h(L) - _h(R))
    return abg.BinTree(k, L, R)


def _check(B, kind, balanced):
    if B is None:
        return
    if kind == "size":
        assert B.size == 1 + (B.left.size if B.left else 0) + (B.right.size if B.right else 0), f"wrong size at {B.key}"
    if kind == "avl":
        assert B.bal == _h(B.left) - _h(B.right), f"wrong bal at {B.key}: {B.bal}"
        assert not balanced or abs(B.bal) <= 1, f"unbalanced at {B.key}"
    _check(B.left, kind, balanced)
    _check(B.right, kind, balanced)


ROT = '''def lr(A):
    """left rotation, balance factors updated"""
    B = A.right
    A.right = B.left
    B.left = A
    A.bal = A.bal + 1 - min(B.bal, 0)
    B.bal = B.bal + 1 + max(A.bal, 0)
    return B

def rr(A):
    """right rotation, balance factors updated"""
    B = A.left
    A.left = B.right
    B.right = A
    A.bal = A.bal - 1 - max(B.bal, 0)
    B.bal = B.bal - 1 + min(A.bal, 0)
    return B

def lrr(A):
    """left-right rotation"""
    A.left = lr(A.left)
    return rr(A)

def rlr(A):
    """right-left rotation"""
    A.right = rr(A.right)
    return lr(A)'''
ANNEX = ("AVL", "abs", "lr", "rr", "lrr", "rlr")


def _w(enonce, code, tests, sol, trees, outs, kind, balanced, figs, methods):
    code = code.strip()
    abg._api(code, extra=ANNEX, methods=methods)
    ns = {"BinTree": abg.BinTree, "BinTreeSize": abg.BinTreeSize, "AVL": AVL}
    if kind == "avl":
        exec(ROT, ns)
    ns.update({k: _build(s, kind) for k, s in trees.items()})
    exec(code, ns)
    for line, exp in tests:
        if exp is None:
            exec(line, ns)
            continue
        try:
            got = repr(eval(line, ns))
        except Exception as e:  # noqa: BLE001 - the statement shows the exception message
            got = f"Exception: {e}"
        assert got == exp, f"{line}: got {got}, expected {exp}\n{code}"
    shown = []
    for cap, expr, exp in outs:
        res = eval(expr, ns)
        assert abg.spec(res) == exp, f"{expr}: got {abg.spec(res)}, expected {exp}"
        _check(res, kind, balanced)
        shown.append((cap, exp))
    text = enonce
    if figs is None:
        figs = list(trees.items())
    if figs:
        text += "\n\n" + abg.fig(*figs)
    if tests:
        text += f"\n\nExemples d'applications :\n\n{_out(_session(tests))}"
    if shown:
        text += "\n\nRésultats attendus :\n\n" + abg.fig(*shown)
    return {"enonce": text, "sol": _py(code) + (f"\n\n{sol}" if sol else "")}


def w(id, enonce, code, tests, sol="", trees=None, outs=(), kind="bin", balanced=True, src=None, duree=8, figs=None, methods=()):
    """« Write the function »: model replayed on the figures' trees; outs = (caption, expr, expected spec)."""
    CHECKED.append(id)
    return {"id": id, "kind": "open", **_w(enonce, code, tests, sol, trees or {}, outs, kind, balanced, figs, methods),
            "src": src or S, "duree": duree}


def o(id, enonce, sol, src=None, duree=4):
    return {"id": id, "kind": "open", "enonce": enonce, "sol": sol, "src": src or S, "duree": duree}


def v(id, enonce, ans, sol, src=None, duree=2):
    a = str(ans)
    return {"id": id, "kind": "value", "enonce": enonce, "calc": a, "ans": a, "sol": f"**Réponse :** ${a}$\n\n{sol}",
            "src": src or S, "duree": duree}


def run(code, expr, ns=None):
    ns = dict(ns or {})
    exec(code, ns)
    return eval(expr, ns)


def seq(L):
    return ", ".join(map(str, L))


# ---------------------------------------------------------------- heaps (td1)

HEAP_PUSH = '''def heap_push(H, val, elt):
    H.append((val, elt))
    i = len(H) - 1
    while i > 1 and H[i // 2][0] > val:
        H[i] = H[i // 2]
        i = i // 2
    H[i] = (val, elt)'''

HEAP_POP = '''def heap_pop(H):
    n = len(H) - 1
    if n == 0:
        raise Exception("empty heap")
    top = H[1]
    last = H.pop()
    n = n - 1
    if n > 0:
        i = 1
        ok = False
        while 2 * i <= n and not ok:
            j = 2 * i
            if j + 1 <= n and H[j + 1][0] < H[j][0]:
                j = j + 1
            if H[j][0] < last[0]:
                H[i] = H[j]
                i = j
            else:
                ok = True
        H[i] = last
    return top'''

HEAP_UPDATE = '''def heap_update(H, pos, newval):
    n = len(H) - 1
    if pos < 1 or pos > n:
        raise Exception("invalid position")
    e = (newval, H[pos][1])
    i = pos
    while i > 1 and H[i // 2][0] > newval:      # value decreased: up
        H[i] = H[i // 2]
        i = i // 2
    ok = False
    while 2 * i <= n and not ok:                # value increased: down
        j = 2 * i
        if j + 1 <= n and H[j + 1][0] < H[j][0]:
            j = j + 1
        if H[j][0] < newval:
            H[i] = H[j]
            i = j
        else:
            ok = True
    H[i] = e'''

HEAP_SORT = HEAP_PUSH + "\n\n" + HEAP_POP + '''

def heap_sort(L):
    H = [None]
    for i in range(len(L)):
        heap_push(H, L[i][0], L[i][1])
    R = []
    for i in range(len(L)):
        R.append(heap_pop(H))
    return R'''

HEAPIFY = '''def sift_down(T, i, n):
    """moves T[i] down until its sons are greater (T[1..n] perfect tree)"""
    e = T[i]
    ok = False
    while 2 * i <= n and not ok:
        j = 2 * i
        if j + 1 <= n and T[j + 1][0] < T[j][0]:
            j = j + 1
        if T[j][0] < e[0]:
            T[i] = T[j]
            i = j
        else:
            ok = True
    T[i] = e

def heapify(T):
    n = len(T) - 1
    for i in range(n // 2, 0, -1):
        sift_down(T, i, n)'''

ELT = dict(zip([2, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32], "ABCDEFGHIJKLM"))
FIG_HEAP = [2, 12, 10, 24, 16, 14, 18, 30, 26, 20, 32, 28, 22]  # td1 figure 1, hierarchical order
H0 = [None] + [(x, ELT[x]) for x in FIG_HEAP]
H1 = run(HEAP_PUSH + "\nheap_push(H, 5, 'N')\nheap_push(H, 15, 'O')\nheap_push(H, 1, 'P')", "H", {"H": list(H0)})
H2 = run(HEAP_POP + "\nheap_pop(H)", "H", {"H": list(H1)})
POS_M = [i for i in range(1, len(H2)) if H2[i][1] == "M"][0]
H3 = run(HEAP_UPDATE + f"\nheap_update(H, {POS_M}, 4)", "H", {"H": list(H2)})
T2 = [None, (20, 'G'), (18, 'F'), (28, 'K'), (16, 'E'), (24, 'I'), (2, 'A'), (14, 'D'), (32, 'M'), (30, 'L'), (22, 'H'), (10, 'B'), (26, 'J'), (12, 'C')]
T2_TD = [None, (2, 'A'), (10, 'B'), (12, 'C'), (16, 'E'), (18, 'F'), (20, 'G'), (14, 'D'), (32, 'M'), (30, 'L'), (22, 'H'), (24, 'I'), (26, 'J'), (28, 'K')]
T2_OUT = run(HEAPIFY + "\nheapify(T)", "T", {"T": list(T2)})


def is_heap(H):
    return all(H[i // 2][0] <= H[i][0] for i in range(2, len(H)))


assert T2_OUT == T2_TD
assert is_heap(H0) and is_heap(H1) and is_heap(H2) and is_heap(H3) and is_heap(T2_TD) and is_heap(T2_OUT)
assert sorted(T2_OUT[1:]) == sorted(T2[1:])


def vec(H):
    return _out(repr(H))


# ---------------------------------------------------------------- BST figures (td2, exams)

B1 = (15, (8, 1, (12, 10, None)), (28, (20, None, 23), (42, 35, 66)))  # td2 figures 1 and 4, B4 exam 2026
B2 = (13, (5, (1, None, 4), (10, 7, 12)), (20, (15, None, 18), (25, 21, 27)))  # td2 figure 2, P2 2019 figure 1
B3 = (12, (2, None, (4, 3, 5)), (21, 18, None))  # td2 figure 3
B18 = (21, (7, (5, (1, None, 4), None), (17, (9, None, 15), 20)), (33, (26, None, 31), (47, 42, 53)))  # P2 2018 figure 2
SEQ = [13, 20, 5, 1, 15, 10, 18, 25, 4, 21, 27, 7, 12]
LEAF = bst_leaf(SEQ)
ROOT = bst_root(SEQ)
assert LEAF == B2  # td2: the leaf insertion of the sequence gives the tree B2 of exercise 2.1
assert abg.ino(ROOT) == sorted(SEQ) and abg.key(ROOT) == 12
DEL15 = bst_del(B1, [15])
DEL15_28 = bst_del(B1, [15, 28])

MINMAX = '''def minBST(B):
    if B.left == None:
        return B.key
    else:
        return minBST(B.left)

def maxBST(B):
    while B.right != None:
        B = B.right
    return B.key'''

SEARCH_REC = '''def searchBST(B, x):
    if B == None or x == B.key:
        return B
    elif x < B.key:
        return searchBST(B.left, x)
    else:
        return searchBST(B.right, x)'''

SEARCH_IT = '''def searchBST_iter(B, x):
    while B != None and x != B.key:
        if x < B.key:
            B = B.left
        else:
            B = B.right
    return B'''

ADD_REC = '''def addBST(x, B):
    if B == None:
        return BinTree(x, None, None)
    if x <= B.key:
        B.left = addBST(x, B.left)
    else:
        B.right = addBST(x, B.right)
    return B'''

ADD_IT = '''def addBST_iter(x, B):
    new = BinTree(x, None, None)
    (P, C) = (None, B)
    while C != None:
        P = C
        if x <= C.key:
            C = C.left
        else:
            C = C.right
    if P == None:
        return new
    if x <= P.key:
        P.left = new
    else:
        P.right = new
    return B'''

DEL = '''def maxBST(B):
    while B.right != None:
        B = B.right
    return B.key

def delBST(x, B):
    if B == None:
        return None
    if x == B.key:
        if B.left == None:
            return B.right
        if B.right == None:
            return B.left
        B.key = maxBST(B.left)
        B.left = delBST(B.key, B.left)
    elif x < B.key:
        B.left = delBST(x, B.left)
    else:
        B.right = delBST(x, B.right)
    return B'''

ROOT_ADD = '''def cut(x, B):
    """splits the BST B into (L, R): keys <= x in L, keys > x in R"""
    if B == None:
        return (None, None)
    if x < B.key:
        (L, R) = cut(x, B.left)
        B.left = R
        return (L, B)
    else:
        (L, R) = cut(x, B.right)
        B.right = L
        return (B, R)

def addRoot(x, B):
    (L, R) = cut(x, B)
    return BinTree(x, L, R)'''

SECOND = '''def second_min(B):
    if B == None:
        return None
    P = None
    while B.left != None:
        P = B
        B = B.left
    if B.right != None:
        B = B.right
        while B.left != None:
            B = B.left
        return B.key
    elif P != None:
        return P.key
    else:
        return None'''

BOTH = '''def size(B):
    if B == None:
        return 0
    return 1 + size(B.left) + size(B.right)

def both_x(B, x):
    if B == None:
        return (0, 0)
    if x <= B.key:
        (inf, sup) = both_x(B.left, x)
        return (inf, sup + 1 + size(B.right))
    else:
        (inf, sup) = both_x(B.right, x)
        return (inf + 1 + size(B.left), sup)'''

LCA = '''def lca(B, x, y):
    while (x < B.key and y < B.key) or (x > B.key and y > B.key):
        if x < B.key:
            B = B.left
        else:
            B = B.right
    return B.key'''

NTH = '''def nthBST(B, k):
    if B.left == None:
        leftSize = 0
    else:
        leftSize = B.left.size
    if k == leftSize + 1:
        return B
    elif k <= leftSize:
        return nthBST(B.left, k)
    else:
        return nthBST(B.right, k - leftSize - 1)'''

MEDIAN = NTH + '''

def median(B):
    if B == None:
        return None
    return nthBST(B, (B.size + 1) // 2).key'''

COPY_SIZE = '''def __copySize(B):
    """returns (copy of B with sizes, size of B)"""
    if B == None:
        return (None, 0)
    (left, s1) = __copySize(B.left)
    (right, s2) = __copySize(B.right)
    size = 1 + s1 + s2
    return (BinTreeSize(B.key, left, right, size), size)

def copyWithSize(B):
    (C, size) = __copySize(B)
    return C'''

ADD_SIZE = '''def addBSTSize(x, A):
    """adds x in leaf if absent: returns (tree, True if x was added)"""
    if A == None:
        return (BinTreeSize(x, None, None, 1), True)
    if x < A.key:
        (A.left, insert) = addBSTSize(x, A.left)
    elif x > A.key:
        (A.right, insert) = addBSTSize(x, A.right)
    else:
        insert = False
    if insert:
        A.size = A.size + 1
    return (A, insert)'''

BST_MYST = '''def bstMystery(x, B):
    # first part
    P = None
    while B != None and x != B.key:
        if x < B.key:
            P = B
            B = B.left
        else:
            B = B.right
    if B == None:
        return None
    # second part
    if B.right == None:
        return P
    else:
        B = B.right
        while B.left != None:
            B = B.left
        return B

def call(x, B):
    p = bstMystery(x, B)
    if p == None:
        return None
    else:
        return p.key'''
CALLS18 = {x: run(BST_MYST, f"call({x}, B)", {"B": abg.bt(B18)}) for x in (25, 21, 20, 9, 53)}
assert CALLS18 == {25: None, 21: 26, 20: 21, 9: 15, 53: None}  # official correction

# ---------------------------------------------------------------- AVL (td « AVL », exams)

TD3_AVL = (17, (9, (3, 1, 8), (13, 11, None)), (29, 23, (40, None, 42)))
assert is_avl(TD3_AVL)
LOG = []
INS_STEPS = []
_t = TD3_AVL
for _x in (4, 48, 7, 5, 6):
    _t = avl_ins([_x], _t, LOG)
    INS_STEPS.append((_x, _t, list(LOG)))
assert LOG[:3] == ["rg(40)", "rgd(8)", "rdg(3)"]  # official correction: insertions of 4, 48, 7, 5
DLOG = []
DEL_STEPS = []
_t = TD3_AVL
for _x in (23, 17, 11, 1):
    _t = avl_del(_t, [_x], DLOG)
    DEL_STEPS.append((_x, _t, list(DLOG)))
assert DLOG == ["rg(29)", "rd(9)", "rdg(3)"]  # official correction: deletions of 23, 17, 11, 1

LOG18 = []
AVL18 = avl_ins([25, 60, 35, 10, 20, 5, 70, 65, 45], None, LOG18)
assert LOG18 == ["rdg(25)", "rgd(25)", "rd(35)", "rdg(60)", "rdg(35)"]  # official correction, exercise 1
LOG19A, LOG19 = [], []
AVL19_1 = avl_ins([5, 15, 20, 2, 4, 1], None, LOG19A)
AVL19 = avl_ins([5, 15, 20, 2, 4, 1, 32, 25, 22], None, LOG19)
LOG26A, LOG26 = [], []
AVL26_6 = avl_ins([10, 5, 15, 2, 1, 7], None, LOG26A)
AVL26 = avl_ins([10, 5, 15, 2, 1, 7, 6, 0, 9, 8], None, LOG26)
FIG26 = (30, (20, (10, 5, 15), (25, 22, (27, None, 28))), (40, 35, (50, 45, None)))
assert is_avl(FIG26)
LOG26D = []
DEL26 = avl_del(FIG26, [40], LOG26D)
for _s in (AVL18, AVL19_1, AVL19, AVL26_6, AVL26, DEL26):
    assert is_avl(_s)

HBAL = '''def __hb(B):
    """returns (height of B, True if B is h-balanced)"""
    if B == None:
        return (-1, True)
    (hl, okl) = __hb(B.left)
    (hr, okr) = __hb(B.right)
    ok = okl and okr and -1 <= hl - hr and hl - hr <= 1
    return (1 + max(hl, hr), ok)

def is_hbalanced(B):
    (h, ok) = __hb(B)
    return ok'''

INSERT = '''def __insertAVL(x, A):
    """returns (A with x inserted, True if the height of A has changed)"""
    if A == None:
        return (AVL(x, None, None, 0), True)
    elif x == A.key:
        return (A, False)
    elif x < A.key:
        (A.left, dh) = __insertAVL(x, A.left)
        if not dh:
            return (A, False)
        A.bal = A.bal + 1
        if A.bal == 2:
            if A.left.bal == 1:
                A = rr(A)
            else:
                A = lrr(A)
        return (A, A.bal == 1)
    else:
        (A.right, dh) = __insertAVL(x, A.right)
        if not dh:
            return (A, False)
        A.bal = A.bal - 1
        if A.bal == -2:
            if A.right.bal == -1:
                A = lr(A)
            else:
                A = rlr(A)
        return (A, A.bal == -1)

def insertAVL(x, A):
    (A, dh) = __insertAVL(x, A)
    return A'''

_DELETE = '''def maxBST(B):
    while B.right != None:
        B = B.right
    return B.key

def __deleteAVL(x, A):
    """returns (A without x, True if the height of A has changed)"""
    if A == None:
        return (None, False)
    if x == A.key:
        if A.left != None and A.right != None:
            A.key = maxBST(A.left)
            x = A.key       # deleted below, in the left subtree
        elif A.left == None:
            return (A.right, True)
        else:
            return (A.left, True)
    if x <= A.key:
        (A.left, dh) = __deleteAVL(x, A.left)
        if not dh:
            return (A, False)
        A.bal = A.bal - 1
        if A.bal == -2:
            if A.right.bal == 1:
                A = rlr(A)
            else:
                A = lr(A)
        return (A, A.bal == 0)
    else:
        (A.right, dh) = __deleteAVL(x, A.right)
        if not dh:
            return (A, False)
        A.bal = A.bal + 1
        if A.bal == 2:
            if A.left.bal == {TEST}:
                A = lrr(A)
            else:
                A = rr(A)
        return (A, A.bal == 0)

def deleteAVL(x, A):
    (A, dh) = __deleteAVL(x, A)
    return A'''
DELETE = _DELETE.replace("{TEST}", "-1")
DELETE_OFFICIAL = _DELETE.replace("A.left.bal == {TEST}", "A.right.bal == -1")


def _official_breaks():
    """The official right-side test reads the wrong son: deleting 4 from 3(1(·,2),4) crashes (A.right is None)."""
    ns = {"AVL": AVL}
    exec(ROT, ns)
    exec(DELETE_OFFICIAL, ns)
    try:
        ns["deleteAVL"](4, _build((3, (1, None, 2), 4), "avl"))
    except AttributeError:
        return True
    return False


assert _official_breaks()

DEL_MIN = '''def del_min_avl(A):
    """A not empty: returns (A without its minimum, True if the height of A has changed)"""
    if A.left == None:
        return (A.right, True)
    (A.left, dh) = del_min_avl(A.left)
    if not dh:
        return (A, False)
    A.bal = A.bal - 1
    if A.bal == -2:
        if A.right.bal == 1:
            A = rlr(A)
        else:
            A = lr(A)
    return (A, A.bal == 0)'''

LIST2AVL = '''def __list2avl(L, left, right):
    """AVL of L[left..right], and its height"""
    if left > right:
        return (None, -1)
    mid = (left + right) // 2
    B = AVL(L[mid], None, None, 0)
    (B.left, hl) = __list2avl(L, left, mid - 1)
    (B.right, hr) = __list2avl(L, mid + 1, right)
    B.bal = hl - hr
    return (B, 1 + max(hl, hr))

def list2avl(L):
    (A, h) = __list2avl(L, 0, len(L) - 1)
    return A'''
L18 = [1, 4, 5, 7, 10, 12, 13, 15, 18, 20, 21, 25]


def _mid_tree(L):
    if not L:
        return None
    m = (len(L) - 1) // 2
    left, right = _mid_tree(L[:m]), _mid_tree(L[m + 1:])
    return L[m] if left is None and right is None else (L[m], left, right)


L18_AVL = _mid_tree(L18)
assert is_avl(L18_AVL)

REBAL = '''def rebalancing(A):
    """A not empty, A.bal in [-2, 2]: rotation if needed;
    returns (tree, True if the rotation changed the height)"""
    if abs(A.bal) < 2:
        return (A, False)
    if A.bal == 2:
        if A.left.bal == 1:
            return (rr(A), True)
        elif A.left.bal == 0:
            return (rr(A), False)
        else:
            return (lrr(A), True)
    else:
        if A.right.bal == -1:
            return (lr(A), True)
        elif A.right.bal == 0:
            return (lr(A), False)
        else:
            return (rlr(A), True)'''


def fibo(n):
    """Fibonacci tree A_n, nodes labelled with their balance factor."""
    if n == 0:
        return None
    if n == 1:
        return 0
    return (1, fibo(n - 1), fibo(n - 2))


def _fsize(s):
    return 0 if s is None else 1 + _fsize(abg.kids(s)[0]) + _fsize(abg.kids(s)[1])


def _fh(s):
    return -1 if s is None else 1 + max(_fh(abg.kids(s)[0]), _fh(abg.kids(s)[1]))


assert all(_fh(fibo(n)) == n - 1 for n in range(1, 12))
NMIN4 = _fsize(fibo(5))  # fewest nodes of an AVL of height 4 = size of A_5

INS_DEPTH = '''def insert_before_depth(B, x, d):
    if B == None:
        if d < 0:
            return (None, False)
        return (BinTree(x, None, None), True)
    if d == 0:          # the new leaf would be deeper than d
        return (B, False)
    if x <= B.key:
        (B.left, res) = insert_before_depth(B.left, x, d - 1)
    else:
        (B.right, res) = insert_before_depth(B.right, x, d - 1)
    return (B, res)'''

CHECK_LIST = '''def check_list(L, B, x):
    (i, n) = (0, len(L))
    ok = True
    while B != None and ok:
        ok = i < n and L[i] == B.key
        i = i + 1
        if x == B.key:
            B = None
        elif x < B.key:
            B = B.left
        else:
            B = B.right
    return ok and i == n'''

MYST26 = '''def myst(B, a):
    if B == None:
        return 0
    else:
        b = myst(B.right, a)
        if b == 0:
            B.key = B.key + a
        B.key = B.key + b
        b = myst(B.left, B.key)
        if b == 0:
            return B.key
        else:
            return b

def mystery(B):
    myst(B, 0)'''
FIG_MYST = (4, (1, 0, (2, None, 3)), (3, 3, (1, None, 2)))
MYST_RES = abg.spec(run(MYST26 + "\nmystery(B)", "B", {"B": abg.bt(FIG_MYST)}))
_in = abg.ino(FIG_MYST)
assert abg.ino(MYST_RES) == [sum(_in[i:]) for i in range(len(_in))]  # suffix sums of the in-order

T234 = {
    "B1": ((20,), [((10,), [((5,), []), ((15,), [])]), ((30, 40), [((18, 25), []), ((35,), []), ((45,), [])])]),
    "B2": ((50, 70), [((20, 30), [((10,), []), ((25,), []), ((35,), [])]), ((60,), [((55,), []), ((65,), [])]),
                      ((80, 90), [((75,), []), ((85,), []), ((95,), [])])]),
    "B3": ((40,), [((20,), [((10,), []), ((30,), [])]), ((60, 80), [((50,), []), ((70,), []), ((90,), [])])]),
    "B4": ((25, 50), [((10,), [((5,), []), ((15,), [])]), ((35,), [((30,), []), ((40,), [])]), ((70,), [((80,), [])])]),
}
OK234 = [k for k, t in T234.items() if is234(t)]
assert OK234 == ["B2", "B3"]


def steps(items):
    return abg.fig(*items)


# ---------------------------------------------------------------- course

NOTIONS = [
    {"id": "tas", "titre": "Tas : arbre parfait dans un vecteur",
     "formule": r"racine `H[1]` (case $0$ inutilisée) · fils de $i$ : $2i$ et $2i+1$ · père : $i\,//\,2$ · feuille : $2i>n$ · point simple : $2i=n$ · valeur d'un nœud $\le$ celles de ses sous-arbres",
     "exemple": r"$n=13$ : le père de $11$ est $5$, les feuilles sont $7\dots13$",
     "cours": r"Un tas représente un arbre binaire parfait partiellement ordonné : le minimum est en racine. La numérotation hiérarchique évite tout pointeur."},
    {"id": "tas_ops", "titre": "Ajout, suppression, modification dans un tas",
     "formule": r"ajout : en case $n+1$ puis remonter tant que le père est plus grand · suppression du minimum : le dernier remplace la racine puis descend vers le plus petit fils · coût $O(\log n)$ · tri par tas $O(n\log n)$",
     "exemple": r"`heap_push(H, 1, 'C')` sur `[None, (8, 'A'), (9, 'D')]` donne `[None, (1, 'C'), (9, 'D'), (8, 'A')]`",
     "cours": r"L'arbre reste parfait (on ajoute et retire toujours la dernière case) ; l'ordre se répare en remontant ou en descendant un seul chemin."},
    {"id": "abr", "titre": "Arbre binaire de recherche",
     "formule": r"clés du sous-arbre gauche $\le$ clé $<$ clés du droit · infixe = ordre croissant · minimum : tout à gauche · maximum : tout à droite · recherche : un seul chemin, $O(h)$",
     "exemple": r"plus proche ancêtre commun : premier nœud où $x$ et $y$ se séparent",
     "cours": r"Toute recherche descend un seul chemin : on compare et on choisit un côté. On ne parcourt jamais tout l'arbre si l'ordre suffit."},
    {"id": "abr_ajout", "titre": "Ajout en feuille, ajout en racine",
     "formule": r"feuille : descendre jusqu'à `None` et y créer le nœud · racine : couper l'arbre en $(G, D)$ (clés $\le x$, clés $>x$) puis `BinTree(x, G, D)`",
     "exemple": r"$13, 20, 5, 1, 15, 10, 18, 25, 4, 21, 27, 7, 12$ en feuille : racine $13$",
     "cours": r"L'ajout en feuille ne modifie qu'un lien. L'ajout en racine coupe l'arbre le long du chemin de recherche de $x$."},
    {"id": "abr_supp", "titre": "Suppression dans un ABR",
     "formule": r"feuille : on l'enlève · point simple : remplacé par son fils · point double : clé remplacée par le maximum du sous-arbre gauche, qu'on supprime ensuite",
     "exemple": r"supprimer $15$ dans B1 : $12$ monte en racine",
     "cours": r"Le maximum du sous-arbre gauche n'a pas de fils droit : le supprimer revient à un des deux cas simples."},
    {"id": "abr_taille", "titre": "ABR avec taille en chaque nœud",
     "formule": r"`size` $=1+$ taille gauche $+$ taille droite · $k$-ième : $g=$ taille gauche ; $k=g+1$ : racine ; $k\le g$ : à gauche ; sinon $(k-g-1)$-ième à droite · médiane : rang $(n+1)\,//\,2$",
     "exemple": r"si le $k$-ième est en racine : $k-1$ éléments à gauche, $n-k$ à droite",
     "cours": r"Stocker la taille permet de trouver le $k$-ième en $O(h)$. Un ajout incrémente la taille de chaque nœud du chemin, seulement si l'élément a vraiment été ajouté."},
    {"id": "avl", "titre": "AVL : arbres h-équilibrés",
     "formule": r"déséquilibre $=h(G)-h(D)$ · AVL : ABR où chaque déséquilibre vaut $-1$, $0$ ou $1$ · $h(\text{vide})=-1$ · hauteur $O(\log n)$ · nombre minimal de nœuds : $N_h=N_{h-1}+N_{h-2}+1$",
     "exemple": r"arbres de Fibonacci : tous les nœuds internes ont un déséquilibre de $1$, $h_n=n-1$",
     "cours": r"La hauteur d'un AVL reste logarithmique : recherche, ajout et suppression coûtent $O(\log n)$."},
    {"id": "rotations", "titre": "Rotations",
     "formule": r"déséquilibre $+2$ : fils gauche à $-1$ : `lrr` (rgd), sinon `rr` (rd) · $-2$ : fils droit à $+1$ : `rlr` (rdg), sinon `lr` (rg) · `lr` : `A.bal += 1 - min(B.bal, 0)` puis `B.bal += 1 + max(A.bal, 0)`",
     "exemple": r"chaîne $1, 2, 3$ insérée : rotation gauche sur $1$",
     "cours": r"Une rotation garde l'ordre infixe et change la racine du sous-arbre. Les rotations doubles enchaînent deux simples."},
    {"id": "avl_modif", "titre": "Ajout et suppression dans un AVL",
     "formule": r"ajout : la hauteur a augmenté si le nouveau déséquilibre vaut $\pm1$ ; après une rotation, plus de changement · suppression : la hauteur a diminué si le nouveau déséquilibre vaut $0$ (aussi après rotation) · rééquilibrage à la remontée",
     "exemple": r"suppression avec fils à $0$ : rotation simple, hauteur inchangée",
     "cours": r"La fonction récursive renvoie l'arbre et un booléen « la hauteur a changé » ; le père met à jour son déséquilibre ($\pm1$) seulement si ce booléen est vrai."},
]

# ---------------------------------------------------------------- levels

LEVELS = [
    {"n": 1, "titre": "Tas : arbre parfait dans un vecteur", "notions": ["tas"], "exos": [
        o("r11", r"Soit `H` le vecteur d'un arbre binaire parfait de taille $n$ (numérotation hiérarchique, case $0$ inutilisée). Où est la racine ? Comment trouver les fils, le père d'un nœud $i$ ? Comment savoir si $i$ est une feuille, un point simple ?",
          r"Racine : `H[1]`. Fils de $i$ : $2i$ et $2i+1$ (s'ils sont $\le n$). Père : $i\,//\,2$ pour $i>1$. Feuille : $2i>n$. Point simple : $2i=n$ (un seul fils, le gauche : au plus un tel nœud, quand $n$ est pair).",
          src=TD1, duree=4),
        v("r12", r"Tas de taille $n=13$ : indice du père du nœud $11$ ?", 11 // 2, r"$11\,//\,2=5$.", src=TD1, duree=1),
        v("r13", r"Combien de feuilles dans un tas de taille $13$ ?", 13 - 13 // 2,
          r"Les nœuds $i$ avec $2i>13$ : $i=7\dots13$, soit $n-n\,//\,2=7$.", duree=2),
        o("r14", r"Donner la représentation par tas (vecteur de couples `(valeur, élément)`) de l'arbre ci-dessous. Éléments : " + ", ".join(f"{e} = {x}" for x, e in ELT.items()) + ".\n\n" + abg.fig(("", heap_spec(H0))),
          vec(H0) + "\n\nOn lit l'arbre niveau par niveau, de gauche à droite.", src=TD1, duree=4),
    ]},
    {"n": 2, "titre": "Tas : ajout et suppression du minimum", "notions": ["tas_ops", "tas"], "exos": [
        o("r21", "Ajouter au tas ci-dessous N de valeur $5$, puis O de valeur $15$, enfin P de valeur $1$. Donner l'arbre et le vecteur.\n\n" + abg.fig(("", heap_spec(H0))),
          abg.fig(("", heap_spec(H1))) + "\n\n" + vec(H1) + "\n\nChaque nouvel élément entre en dernière case puis remonte tant que son père est plus grand ; P (valeur $1$) remonte jusqu'à la racine.",
          src=TD1, duree=6),
        w("r22", r"Écrire la fonction `heap_push(H, val, elt)` qui ajoute la paire `(val, elt)` au tas `H` (modifié en place).", HEAP_PUSH,
          [("H = [None]", None), ("heap_push(H, 8, 'A')", None), ("H", "[None, (8, 'A')]"), ("heap_push(H, 9, 'D')", None), ("H", "[None, (8, 'A'), (9, 'D')]"),
           ("heap_push(H, 1, 'C')", None), ("H", "[None, (1, 'C'), (9, 'D'), (8, 'A')]"), ("heap_push(H, 2, 'B')", None), ("H", "[None, (1, 'C'), (2, 'B'), (8, 'A'), (9, 'D')]")],
          r"On fait descendre les pères plutôt que d'échanger : une seule affectation de la nouvelle paire à la fin.", src=TD1, duree=8),
        o("r23", "Supprimer le plus petit élément du tas obtenu (ci-dessous). Donner l'arbre et le vecteur.\n\n" + abg.fig(("", heap_spec(H1))),
          abg.fig(("", heap_spec(H2))) + "\n\n" + vec(H2) + "\n\nLa dernière case remplace la racine puis descend du côté du plus petit fils tant qu'il est plus petit qu'elle.",
          src=TD1, duree=6),
        w("r24", r"Écrire `heap_pop(H)` qui supprime et renvoie la paire de plus petite valeur du tas `H` (modifié en place). Elle lève une `Exception` si le tas est vide.", HEAP_POP,
          [("H = [None, (1, 'C'), (2, 'B'), (8, 'A'), (9, 'D')]", None), ("heap_pop(H)", "(1, 'C')"), ("H", "[None, (2, 'B'), (9, 'D'), (8, 'A')]"),
           ("heap_pop(H)", "(2, 'B')"), ("H", "[None, (8, 'A'), (9, 'D')]"), ("heap_pop([None])", "Exception: empty heap")],
          r"`H.pop()` retire la dernière case : l'arbre reste parfait. Attention au tas qui devient vide (rien à faire descendre).",
          src=TD1, duree=10, methods=("pop",)),
    ]},
    {"n": 3, "titre": "Tas : modification, tri, heapify", "notions": ["tas_ops"], "exos": [
        o("r31", f"Dans le tas ci-dessous, la valeur de M (case ${POS_M}$) passe à $4$. Donner le nouveau tas.\n\n" + abg.fig(("", heap_spec(H2))),
          abg.fig(("", heap_spec(H3))) + "\n\n" + vec(H3) + "\n\nLa valeur a diminué : M remonte tant que son père est plus grand.", src=TD1, duree=5),
        w("r32", r"Écrire `heap_update(H, pos, newval)` qui remplace la valeur de l'élément en position `pos` par `newval` (tas modifié en place). Elle lève une exception si `pos` n'est pas valide.", HEAP_UPDATE,
          [("H = [None, (1, 'C'), (2, 'B'), (8, 'A'), (9, 'D')]", None), ("heap_update(H, 3, 0)", None), ("H", "[None, (0, 'A'), (2, 'B'), (1, 'C'), (9, 'D')]"),
           ("heap_update(H, 1, 10)", None), ("H", "[None, (1, 'C'), (2, 'B'), (10, 'A'), (9, 'D')]"), ("heap_update(H, 5, 3)", "Exception: invalid position")],
          r"Une valeur qui diminue remonte, une valeur qui augmente descend : un seul des deux `while` déplace l'élément.", src=TD1, duree=10),
        o("r33", r"Quelle est la complexité de la recherche de la position d'un élément quelconque dans un tas ? Que faut-il ajouter pour modifier un élément quelconque en restant en $O(\log n)$ ?",
          r"Le tas n'est pas ordonné de gauche à droite : trouver un élément demande un parcours de tout le vecteur, $O(n)$. On ajoute une table des positions (élément $\to$ indice dans le vecteur), mise à jour à chaque déplacement ; `heap_update` coûte alors $O(\log n)$.",
          src=TD1, duree=3),
        w("r34", r"Écrire `heap_sort(L)` qui trie (pas en place) la liste de paires `(val, elt)` en ordre croissant à l'aide d'un tas.", HEAP_SORT,
          [("L = [(1, 'C'), (8, 'A'), (9, 'D'), (2, 'B')]", None), ("heap_sort(L)", "[(1, 'C'), (2, 'B'), (8, 'A'), (9, 'D')]"), ("L", "[(1, 'C'), (8, 'A'), (9, 'D'), (2, 'B')]")],
          r"$n$ ajouts puis $n$ suppressions du minimum : $O(n\log n)$.", src=TD1, duree=6, methods=("pop",)),
        w("r35", r"Soit `T` un arbre binaire parfait (numérotation hiérarchique). Écrire `heapify(T)` qui le transforme en tas en place.", HEAPIFY,
          [("T1 = [None, (3, 'A'), (2, 'B'), (1, 'C')]", None), ("heapify(T1)", None), ("T1", "[None, (1, 'C'), (2, 'B'), (3, 'A')]"),
           (f"T2 = {T2!r}", None), ("heapify(T2)", None), ("T2", repr(T2_OUT))],
          r"On fait descendre chaque nœud interne, du dernier ($n\,//\,2$) jusqu'à la racine : coût $O(n)$. C'est le résultat du TD ; d'autres tas sont possibles.",
          src=TD1, duree=10),
    ]},
    {"n": 4, "titre": "ABR : minimum, maximum, recherche", "notions": ["abr"], "exos": [
        o("r41", r"Où se trouvent les valeurs minimum et maximum d'un arbre binaire de recherche non vide ?",
          r"Le minimum est le nœud le plus à gauche (on suit les fils gauches jusqu'à un nœud sans fils gauche), le maximum le plus à droite. Ce ne sont pas forcément des feuilles.", src=TD2, duree=2),
        w("r42", r"Écrire `minBST(B)` (récursif) et `maxBST(B)` (itératif), avec `B` un ABR non vide.", MINMAX,
          [("minBST(B1)", "1"), ("maxBST(B1)", "66")], trees={"B1": B1}, src=TD2, duree=5),
        w("r43", r"Écrire la fonction récursive `searchBST(B, x)` qui renvoie l'arbre de racine $x$ si $x$ est dans l'ABR `B`, `None` sinon.", SEARCH_REC,
          [("searchBST(B1, 12).key", "12"), ("searchBST(B1, 13)", "None")], trees={"B1": B1}, src=TD2, duree=4),
        w("r44", r"Même question en itératif : `searchBST_iter(B, x)`.", SEARCH_IT,
          [("searchBST_iter(B1, 35).key", "35"), ("searchBST_iter(B1, 30)", "None")], trees={"B1": B1}, src=TD2, duree=4),
    ]},
    {"n": 5, "titre": "ABR : ajout en feuille", "notions": ["abr_ajout", "abr"], "exos": [
        o("r51", f"Ajout aux feuilles : construire, à partir d'un arbre vide, l'ABR obtenu après ajouts successifs de ${seq(SEQ)}$.",
          abg.fig(("", LEAF)) + "\n\nChaque valeur descend depuis la racine $13$ et devient une feuille. C'est l'arbre B2 de l'exercice « second minimum ».",
          src=TD2, duree=5),
        w("r52", r"Écrire la fonction récursive `addBST(x, B)` qui ajoute $x$ en feuille dans l'ABR `B` et renvoie l'arbre.", ADD_REC,
          [("B1 = addBST(11, B1)", None), ("B1.left.right.left.right.key", "11")], trees={"B1": B1},
          outs=[("addBST(40, B1)", "addBST(40, B1)", bst_leaf([11, 40], B1))],
          sol=r"L'arbre vide devient une feuille ; sinon on raccroche le sous-arbre modifié. Coût $O(h)$.", src=TD2, duree=5),
        w("r53", r"Bonus : écrire l'ajout en feuille en itératif, `addBST_iter(x, B)`.", ADD_IT,
          [("addBST_iter(5, None).key", "5")], trees={"B1": B1}, outs=[("addBST_iter(30, B1)", "addBST_iter(30, B1)", bst_leaf([30], B1))],
          sol=r"On garde le père `P` du nœud courant : c'est sous lui qu'on accroche la nouvelle feuille.", src=TD2, duree=7),
    ]},
    {"n": 6, "titre": "ABR : suppression", "notions": ["abr_supp"], "exos": [
        o("r61", "Dans l'ABR ci-dessous, supprimer $15$ puis $28$ (un point double prend le maximum de son sous-arbre gauche).\n\n" + abg.fig(("B1", B1)),
          steps([("sans 15", DEL15), ("puis sans 28", DEL15_28)]) + "\n\n$15$ est remplacé par $12$ (maximum à gauche), puis $28$ par $23$.", src=TD2, duree=5),
        w("r62", r"Écrire la fonction récursive `delBST(x, B)` qui supprime $x$ de l'ABR `B` et renvoie l'arbre.", DEL,
          [("delBST(7, None)", "None")], trees={"B1": B1},
          outs=[("delBST(15, B1)", "delBST(15, B1)", DEL15), ("puis delBST(10, B1)", "delBST(10, B1)", bst_del(DEL15, [10]))],
          sol=r"Trois cas : feuille ou point simple (on renvoie l'autre fils), point double (on remplace par le maximum du sous-arbre gauche puis on le supprime à gauche).",
          src=TD2, duree=10),
        w("r63", r"Écrire `delMin(B)` qui supprime le minimum de l'ABR non vide `B` et renvoie l'arbre.",
          "def delMin(B):\n    if B.left == None:\n        return B.right\n    B.left = delMin(B.left)\n    return B",
          [("delMin(BinTree(3, None, None))", "None")], trees={"B1": B1}, outs=[("delMin(B1)", "delMin(B1)", bst_del(B1, [1]))],
          sol=r"Le minimum n'a pas de fils gauche : on le remplace par son fils droit (cas du point simple ou de la feuille).", duree=5),
    ]},
    {"n": 7, "titre": "ABR : ajout en racine", "notions": ["abr_ajout"], "exos": [
        o("r71", f"Ajout en racine : construire, à partir d'un arbre vide, l'ABR obtenu après ajouts successifs de ${seq(SEQ)}$.",
          abg.fig(("", ROOT)) + "\n\nLa dernière valeur ajoutée, $12$, est en racine ; chaque ajout coupe l'arbre précédent en (clés $\\le x$, clés $>x$).",
          src=TD2, duree=8),
        w("r72", r"Écrire `addRoot(x, B)` qui ajoute $x$ en racine dans l'ABR `B`.", ROOT_ADD,
          [("addRoot(3, None).key", "3")], trees={"B1": B1},
          outs=[("addRoot(13, B1)", "addRoot(13, B1)", bst_root([13], B1))],
          sol=r"`cut` suit le chemin de recherche de $x$ : chaque nœud rencontré part à gauche (clé $\le x$) ou à droite, et récupère la partie coupée de son sous-arbre.",
          src=TD2, duree=10),
        o("r73", "Ajouter $25$ en racine dans l'ABR ci-dessous. Dessiner le résultat.\n\n" + abg.fig(("B1", B1)),
          abg.fig(("", bst_root([25], B1))) + "\n\nLe chemin de recherche de $25$ ($15$, $28$, $20$, $23$) est coupé : $15$, $20$, $23$ (clés $\\le 25$) partent à gauche, $28$ à droite.",
          duree=5),
    ]},
    {"n": 8, "titre": "ABR : second minimum, comptages, ancêtre commun", "notions": ["abr"], "exos": [
        w("r81", r"Écrire `second_min(B)` qui renvoie la deuxième plus petite valeur de l'ABR `B` (clés distinctes), ou `None` si elle n'existe pas.", SECOND,
          [("second_min(B1)", "8"), ("second_min(B2)", "4"), ("second_min(B3)", "3"), ("second_min(None)", "None")],
          trees={"B1": B1, "B2": B2, "B3": B3},
          sol=r"Après le minimum : le minimum de son sous-arbre droit s'il existe, sinon son père.", src=TD2, duree=8),
        w("r82", r"Écrire `both_x(B, x)` qui renvoie `(inf, sup)` : nombres d'éléments de l'ABR `B` inférieurs à $x$, et supérieurs ou égaux à $x$.", BOTH,
          [("both_x(B2, 20)", "(9, 4)"), ("both_x(B2, 27)", "(12, 1)"), ("both_x(B2, 21)", "(10, 3)"), ("both_x(B3, 12)", "(4, 3)"), ("both_x(B3, 23)", "(7, 0)"), ("both_x(B3, 7)", "(4, 3)")],
          trees={"B2": B2, "B3": B3},
          sol=r"Si $x\le$ racine, la racine et tout le sous-arbre droit sont $\ge x$ : on les compte d'un coup et on descend à gauche (et symétriquement).", src=TD2, duree=10),
        w("r83", r"Écrire `lca(B, x, y)` : clé du plus proche ancêtre commun des nœuds $x$ et $y$ ($x\ne y$, présents dans l'ABR `B`, un nœud est son propre ancêtre).", LCA,
          [("lca(B1, 10, 15)", "15"), ("lca(B1, 20, 66)", "28"), ("lca(B1, 8, 10)", "8"), ("lca(B1, 10, 42)", "15")], trees={"B1": B1},
          sol=r"Tant que $x$ et $y$ sont du même côté, on descend ; le premier nœud qui les sépare (ou qui vaut l'un d'eux) est l'ancêtre.", src=TD2, duree=6),
    ]},
    {"n": 9, "titre": "ABR avec taille : k-ième élément", "notions": ["abr_taille"], "exos": [
        o("r91", r"Soit `B` un ABR de $n$ éléments. Si le $k$-ième élément ($1\le k\le n$, ordre croissant) est en racine, combien d'éléments contiennent ses sous-arbres ?",
          r"$k-1$ à gauche (les plus petits), $n-k$ à droite.", src=P19, duree=2),
        o("r92", r"On ajoute aux arbres binaires l'opération `taille` : `taille(arbrevide) = 0`, `taille(<o, G, D>) = 1 + taille(G) + taille(D)`. Donner une définition abstraite de `kieme : ArbreBinaire × Entier → Élément` (utilisant `taille`).",
          r"Pour $1\le k\le$ `taille(<o, G, D>)` :" + "\n\n" + r"- `kieme(<o, G, D>, k) = contenu(o)` si $k=$ `taille(G)` $+1$" + "\n" + r"- `kieme(<o, G, D>, k) = kieme(G, k)` si $k\le$ `taille(G)`" + "\n" + r"- `kieme(<o, G, D>, k) = kieme(D, k - taille(G) - 1)` si $k>$ `taille(G)` $+1$",
          src=TD2, duree=5),
        w("r93", r"Avec `BinTreeSize` (attribut `size` en chaque nœud), écrire `nthBST(B, k)` qui renvoie l'arbre dont la racine est le $k$-ième élément ($1\le k\le$ `B.size`).", NTH,
          [("nthBST(B1, 3).key", "10"), ("nthBST(B1, 1).key", "1"), ("nthBST(B1, 11).key", "66")], trees={"B1": B1}, kind="size",
          sol=r"Un seul chemin descendu : $O(h)$, sans parcours infixe.", src=TD2, duree=8),
        w("r94", r"Écrire `median(B)` : valeur médiane (rang $(n+1)\,//\,2$) de l'ABR avec taille `B`, `None` s'il est vide.", MEDIAN,
          [("median(B1)", "20"), ("median(None)", "None")], trees={"B1": B1}, kind="size", src=TD2, duree=4),
    ]},
    {"n": 10, "titre": "AVL : déséquilibres et rotations", "notions": ["avl", "rotations"], "exos": [
        o("r101", r"Indiquer le déséquilibre de chaque nœud de l'arbre ci-dessous. Est-ce un AVL ?" + "\n\n" + abg.fig(("", TD3_AVL)),
          f"Déséquilibres ($h(G)-h(D)$) : {bals(TD3_AVL)}.\n\nC'est un ABR et tous les déséquilibres sont dans $\\{{-1, 0, 1\\}}$ : c'est un AVL.", src=TD3, duree=4),
        w("r102", r"Écrire `is_hbalanced(B)` qui vérifie si l'arbre binaire `B` (`BinTree`) est h-équilibré.", HBAL,
          [("is_hbalanced(A)", "True"), ("is_hbalanced(C)", "False"), ("is_hbalanced(None)", "True")], trees={"A": TD3_AVL, "C": (1, None, (2, None, 3))},
          sol=r"La fonction auxiliaire renvoie la hauteur avec le booléen : un seul parcours, $O(n)$ (recalculer la hauteur en chaque nœud coûterait $O(n^2)$).", src=TD3, duree=8),
        o("r103", r"Pour un déséquilibre de $+2$ ou $-2$ en racine, quelle rotation appliquer selon le déséquilibre du fils concerné ? Quelle variation de hauteur ?",
          "| racine | fils | rotation | $\\Delta H$ |\n|---|---|---|---|\n| $-2$ | droit $-1$ | gauche `lr` (rg) | $-1$ |\n| $-2$ | droit $0$ | gauche `lr` (rg) | $0$ |\n| $-2$ | droit $+1$ | droite-gauche `rlr` (rdg) | $-1$ |\n| $+2$ | gauche $+1$ | droite `rr` (rd) | $-1$ |\n| $+2$ | gauche $0$ | droite `rr` (rd) | $0$ |\n| $+2$ | gauche $-1$ | gauche-droite `lrr` (rgd) | $-1$ |\n\nLe cas du fils à $0$ n'arrive qu'après une suppression.",
          src=TD3, duree=5),
        w("r104", r"Écrire les quatre rotations `lr`, `rr`, `lrr`, `rlr` sur la classe `AVL` (attribut `bal` = déséquilibre), avec mise à jour des déséquilibres.", ROT,
          [], trees={"A": (1, None, (2, None, 3)), "C": (3, (1, None, 2), None), "D": (5, (3, 2, 4), None)}, kind="avl", balanced=False,
          outs=[("lr(A)", "lr(A)", (2, 1, 3)), ("lrr(C)", "lrr(C)", (2, 1, 3)), ("rr(D)", "rr(D)", (3, 2, (5, 4, None)))],
          sol=r"Formules générales : après `lr`, l'ancienne racine gagne $1$ (plus $-\min$ du déséquilibre du fils), puis la nouvelle racine gagne $1$ (plus $\max$ du nouveau déséquilibre de l'ancienne). Avec ces formules, les rotations doubles se composent des simples ; avec des mises à jour « cas par cas » (TD), elles doivent être écrites à part.",
          src=TD3, duree=12),
    ]},
    {"n": 11, "titre": "AVL : ajout", "notions": ["avl_modif", "rotations"], "exos": [
        o("r111", r"Insérer successivement $4$, $48$, $7$, $5$ et $6$ dans l'AVL ci-dessous. Indiquer les rotations." + "\n\n" + abg.fig(("", TD3_AVL)),
          steps([(f"+{x}", t) for x, t, _ in INS_STEPS]) + "\n\nRotations, dans l'ordre : " + ", ".join(LOG) + ".\n\nLe corrigé officiel donne les trois premières (insertions de $4$, $48$, $7$, $5$).",
          src=TD3, duree=10),
        w("r112", r"Écrire `insertAVL(x, A)` qui insère $x$ dans l'AVL `A` (sauf si la clé est déjà présente) et renvoie l'arbre. " + AVL_RULE, INSERT,
          [("A = insertAVL(4, A)", None), ("A = insertAVL(48, A)", None), ("A = insertAVL(7, A)", None), ("A = insertAVL(5, A)", None), ("A.left.key", "9")],
          trees={"A": TD3_AVL}, kind="avl", outs=[("A", "A", INS_STEPS[3][1])],
          sol=r"La fonction auxiliaire renvoie aussi « la hauteur a augmenté ». Après une rotation, le déséquilibre est $0$ : la hauteur revient à sa valeur avant insertion (raccourci `A.bal == 1`).",
          src=TD3, duree=12),
        v("r113", r"Nombre minimal de nœuds d'un AVL de hauteur $4$ ?", NMIN4,
          r"$N_0=1$, $N_1=2$, $N_h=N_{h-1}+N_{h-2}+1$ : $4$, $7$, puis $12$. C'est la taille de l'arbre de Fibonacci $A_5$."),
    ]},
    {"n": 12, "titre": "AVL : suppression", "notions": ["avl_modif", "rotations"], "exos": [
        o("r121", r"Supprimer successivement $23$, $17$, $11$ et $1$ dans l'AVL ci-dessous (point double : maximum du sous-arbre gauche). Indiquer les rotations." + "\n\n" + abg.fig(("", TD3_AVL)),
          steps([(f"-{x}", t) for x, t, _ in DEL_STEPS]) + "\n\nRotations : " + ", ".join(DLOG) + ". $17$ est remplacé par $13$, qui est remplacé à son tour par $11$ dans son ancien nœud.",
          src=TD3, duree=10),
        o("r122", r"Après une suppression dans le sous-arbre gauche qui a diminué sa hauteur, que devient la hauteur de l'arbre selon son ancien déséquilibre ($+1$, $0$, $-1$) ?",
          r"Ancien $+1$, nouveau $0$ : la hauteur diminue. Ancien $0$, nouveau $-1$ : inchangée. Ancien $-1$, nouveau $-2$ : rotation ; fils droit à $-1$ : `lr`, hauteur diminuée ; à $0$ : `lr`, inchangée ; à $+1$ : `rlr`, diminuée. Bilan : la hauteur a changé si le déséquilibre final vaut $0$.",
          src=TD3, duree=5),
        w("r123", r"Écrire `deleteAVL(x, A)` qui supprime $x$ de l'AVL `A` et renvoie l'arbre. " + AVL_RULE, DELETE,
          [("A = deleteAVL(23, A)", None), ("A = deleteAVL(17, A)", None), ("A = deleteAVL(11, A)", None), ("A.key", "13")],
          trees={"A": TD3_AVL}, kind="avl", outs=[("A", "A", DEL_STEPS[2][1]), ("deleteAVL(1, A)", "deleteAVL(1, A)", DEL_STEPS[3][1])],
          sol=r"Point double : on remonte le maximum du sous-arbre gauche puis on le supprime à gauche (`x <= A.key`). Le corrigé officiel teste `A.right.bal == -1` après une suppression à droite : c'est le fils **gauche** qu'il faut tester (sinon, supprimer $4$ dans $3(1(\cdot, 2), 4)$ plante : `A.right` vaut `None`).",
          src=TD3, duree=15),
    ]},
    {"n": 13, "titre": "Partiel du 30 mai 2018", "notions": ["avl_modif", "avl", "abr"], "exos": [
        o("r131", r"**Exercice 1 (AVL, 3 points).** À partir d'un arbre vide, construire l'AVL en insérant $25, 60, 35, 10, 20, 5, 70, 65, 45$. Dessiner l'arbre final et indiquer les rotations, dans l'ordre (par exemple `rg(42)`).",
          abg.fig(("", AVL18)) + "\n\nRotations : " + ", ".join(LOG18) + ".", src=P18, duree=8),
        o("r132", r"**Exercice 2 (Arbres de Léonard, 3 points).** $A_0$ est vide, $A_1=\langle o, \emptyset, \emptyset\rangle$, $A_n=\langle o, A_{n-1}, A_{n-2}\rangle$. Dessiner $A_5$. Exprimer la hauteur $h_n$ ($n\ge2$) et montrer que $A_n$ est h-équilibré.",
          abg.fig(("A5 (nœuds = déséquilibres)", fibo(5))) + "\n\n$h_n=n-1$. Par récurrence, les sous-arbres $A_{n-1}$ et $A_{n-2}$ ont pour hauteurs $n-2$ et $n-3$ : la racine a un déséquilibre de $1$, et les sous-arbres sont h-équilibrés.",
          src=P18, duree=6),
        w("r133", r"**Exercice 3 (List → AVL, 5 points).** Écrire `list2avl(L)` qui renvoie un AVL (classe `AVL`, déséquilibres renseignés) créé à partir de la liste `L` strictement croissante.", LIST2AVL,
          [], kind="avl", outs=[(f"list2avl({L18})", f"list2avl({L18!r})", L18_AVL)],
          sol=r"Corrigé officiel : le milieu en racine, récursivement ; la fonction auxiliaire renvoie la hauteur pour calculer le déséquilibre. Coût $O(n)$.",
          src=P18, duree=12),
        w("r134", r"**Exercice 4 (AVL, suppression du minimum, 6 points).** Écrire la fonction récursive `del_min_avl(A)` qui supprime le minimum de l'AVL non vide `A` et renvoie le couple (arbre, la hauteur a changé). " + AVL_RULE, DEL_MIN,
          [("(A, dh) = del_min_avl(A)", None), ("dh", "False"), ("(A, dh) = del_min_avl(A)", None), ("dh", "False"),
           ("(A, dh) = del_min_avl(A)", None), ("dh", "True")],
          trees={"A": AVL18}, kind="avl", outs=[("A", "A", avl_del(AVL18, [5, 10, 20]))],
          sol=r"Après la suppression du minimum, seul le déséquilibre $-2$ est possible : fils droit à $-1$ : rg, hauteur diminuée ; à $0$ : rg, inchangée ; à $+1$ : rdg, diminuée.",
          src=P18, duree=12),
        o("r135", r"**Exercice 5 (ABR et mystère, 4 points).** Pour chaque appel, donner le résultat : `call(25, B1)`, `call(21, B1)`, `call(20, B1)`, `call(9, B1)`, `call(53, B1)`. Que fait `call(x, B)` ?" + "\n\n" + _py(BST_MYST) + "\n\n" + abg.fig(("B1", B18)),
          " · ".join(f"`call({x}, B1)` : {r}" for x, r in CALLS18.items()) + "\n\nÀ la fin de la première partie, `B` est le nœud de $x$ (ou `None`) et `P` le dernier nœud depuis lequel on est descendu à gauche. `call(x, B)` renvoie la valeur immédiatement supérieure à $x$ (le successeur), `None` si $x$ est absent ou maximal.",
          src=P18, duree=8),
    ]},
    {"n": 14, "titre": "Partiel du 22 mai 2019", "notions": ["abr_taille", "avl_modif"], "exos": [
        w("r141", r"**Exercice 1 (La taille en plus, 4 points).** Écrire `copyWithSize(B)` qui renvoie une copie de l'arbre `BinTree` `B` en `BinTreeSize` (taille renseignée en chaque nœud).", COPY_SIZE,
          [("copyWithSize(B1).size", "13"), ("copyWithSize(B1).left.size", "6"), ("copyWithSize(None)", "None")], trees={"B1": B2},
          outs=[("copyWithSize(B1)", "copyWithSize(B1)", B2)],
          sol=r"Corrigé officiel : l'auxiliaire renvoie la copie et sa taille, pour ne jamais recalculer une taille.", src=P19, duree=8),
        w("r142", r"**Exercice 2 (Ajout avec mise à jour de la taille, 4 points).** Écrire une fonction récursive qui ajoute un élément en feuille dans un ABR `BinTreeSize`, sauf s'il est déjà présent, en mettant à jour les tailles.", ADD_SIZE,
          [("(B1, ok) = addBSTSize(11, B1)", None), ("ok", "True"), ("B1.size", "14"), ("(B1, ok) = addBSTSize(13, B1)", None), ("ok", "False"), ("B1.size", "14")],
          trees={"B1": B2}, kind="size", outs=[("B1", "B1", bst_leaf([11], B2))],
          sol=r"La taille d'un nœud n'augmente que si l'élément a été ajouté : le booléen remonte.", src=P19, duree=8),
        w("r143", r"**Exercice 3 (Médian, 7 points).** Avec `BinTreeSize`, écrire `nthBST(B, k)` (arbre dont la racine est le $k$-ième élément) puis `median(B)` (valeur de rang $(n+1)\,//\,2$, `None` si `B` est vide).", MEDIAN,
          [("nthBST(B1, 3).key", "5"), ("nthBST(B1, 9).key", "18"), ("median(B1)", "13")], trees={"B1": B2}, kind="size",
          sol=r"Corrigé officiel. Un peu d'aide de l'énoncé : si le $k$-ième est en racine, $k-1$ éléments à gauche et $n-k$ à droite.", src=P19, duree=12),
        o("r144", r"**Exercice 4 (Construction, 3 points).** À partir d'un arbre vide, construire l'AVL en insérant $5, 15, 20, 2, 4, 1, 32, 25, 22$. Dessiner l'arbre après l'insertion de $1$, puis l'arbre final.",
          steps([("après 1", AVL19_1), ("final", AVL19)]) + "\n\nRotations : " + ", ".join(LOG19) + ".", src=P19, duree=8),
        w("r145", r"**Exercice 5 (Rééquilibrage, 3 points).** Écrire `rebalancing(A)` qui rééquilibre si nécessaire l'AVL `A` après la mise à jour du déséquilibre de sa racine ($-2\le$ `A.bal` $\le2$), et renvoie le couple (arbre, la rotation a changé la hauteur). " + AVL_RULE, REBAL,
          [("(T, dh) = rebalancing(C)", None), ("dh", "True"), ("(T, dh) = rebalancing(D)", None), ("dh", "False"), ("rebalancing(E)[1]", "True")],
          trees={"C": (3, (2, 1, None), None), "D": (5, (3, 2, 4), None), "E": (3, (1, None, 2), None)}, kind="avl",
          sol=r"Corrigé officiel. Seul le cas du fils à $0$ (après une suppression) laisse la hauteur inchangée.", src=P19, duree=8),
    ]},
    {"n": 15, "titre": "Examen B4 du 11 mai 2026", "notions": ["abr", "abr_ajout", "avl_modif"], "exos": [
        w("r151", r"**Exercice 1 (6 points).** Écrire `insert_before_depth(B, x, d)` : insère $x$ en feuille dans l'ABR `B` (chemin d'insertion standard) **seulement si la profondeur d'insertion est $\le d$** (racine à la profondeur $0$). Renvoie le couple `(root, res)`, `res` vrai si $x$ a été inséré.", INS_DEPTH,
          [("(B, res) = insert_before_depth(B, 9, 3)", None), ("res", "False"), ("(B, res) = insert_before_depth(B, 13, 3)", None), ("res", "True"),
           ("(T, res) = insert_before_depth(None, 5, 0)", None), ("res", "True")],
          trees={"B": B1}, outs=[("B", "B", bst_leaf([13], B1))],
          sol=r"On s'arrête dès que la profondeur restante est nulle sur un nœud non vide : inutile de descendre plus bas (optimisation notée).", src=B26, duree=12),
        w("r152", r"**Exercice 2 (6 points).** Écrire `check_list(L, B, x)` : vrai si la liste `L` est exactement la suite des nœuds rencontrés lors de la recherche de $x$ dans l'ABR `B`.", CHECK_LIST,
          [("check_list([], None, 42)", "True"), ("check_list([15, 28, 20, 23], B, 23)", "True"), ("check_list([15, 28, 23], B, 23)", "False"),
           ("check_list([15, 28, 20, 23], B, 22)", "True"), ("check_list([15, 8, 12, 10], B, 10)", "True"), ("check_list([15, 8, 10], B, 10)", "False"), ("check_list([15], B, 15)", "True")],
          trees={"B": B1},
          sol=r"On descend le chemin de recherche en avançant dans `L` ; à la fin, toute la liste doit avoir été lue. Si $x$ est absent, le chemin s'arrête sur `None` (exemple avec $22$).", src=B26, duree=12),
        o("r153", r"**Exercice 3.1 (Dessins).** Construire l'AVL des ajouts successifs de $10, 5, 15, 2, 1, 7, 6, 0, 9, 8$ à partir de l'arbre vide. Dessiner l'arbre après le 6e ajout, puis l'arbre final ; indiquer les rotations dans l'ordre (`rg(42)`, `rdg(42)`…).",
          steps([("après 6 ajouts", AVL26_6), ("final", AVL26)]) + "\n\nRotations : " + ", ".join(LOG26) + ".", src=B26, duree=10),
        o("r154", r"**Exercice 3.2.** Dans l'AVL ci-dessous, supprimer $40$ (point double : maximum du sous-arbre gauche). Indiquer les rotations." + "\n\n" + abg.fig(("", FIG26)),
          abg.fig(("", DEL26)) + "\n\nRotations : " + ", ".join(LOG26D) + ". $35$ remplace $40$ ; le nœud passe à $-2$, puis la racine à $+2$.", src=B26, duree=8),
        o("r155", r"**Exercice 4 (2 points).** Lesquels de ces arbres sont des arbres 2-3-4 ? (Un nœud entre crochets, ses fils en dessous, décalés.)" + "\n\n" + "\n\n".join(f"{k} :\n\n{_out(t234(t))}" for k, t in T234.items()),
          f"Arbres 2-3-4 : {', '.join(OK234)}.\n\nB1 : $18$ est dans le sous-arbre droit de $20$ (ordre faux). B4 : le nœud $[70]$ a une clé mais un seul fils (il en faut $2$).",
          src=B26, duree=4),
        o("r156", r"**Exercice 5 (Mystery, 2 points).** Dessiner l'arbre `B` après `mystery(B)`." + "\n\n" + _py(MYST26) + "\n\n" + abg.fig(("B", FIG_MYST)),
          abg.fig(("après mystery", MYST_RES)) + "\n\nParcours infixe inversé (droite, racine, gauche) : chaque clé devient la somme d'elle-même et de toutes les clés qui la suivent dans l'ordre infixe.",
          src=B26, duree=8),
    ]},
]

EXTRA_PARTS = []

QUIZ = [
    {"notion": "tas", "type": "qcm", "q": r"Dans un tas (case $0$ inutilisée), le père du nœud $i$ est :", "choix": [r"$i\,//\,2$", r"$2i$", r"$i-1$", r"$(i+1)\,//\,2$"], "bonne": 0},
    {"notion": "tas", "type": "vf", "q": r"Dans un tas de valeurs distinctes, le maximum est une feuille.", "bonne": True},
    {"notion": "tas_ops", "type": "qcm", "q": r"Coût de la suppression du minimum dans un tas de $n$ éléments :", "choix": [r"$O(\log n)$", r"$O(1)$", r"$O(n)$", r"$O(n\log n)$"], "bonne": 0},
    {"notion": "tas_ops", "type": "vf", "q": r"Pour supprimer le minimum, on met le dernier élément en racine puis on le fait descendre du côté du plus grand fils.", "bonne": False},
    {"notion": "abr", "type": "qcm", "q": r"Le parcours qui donne les clés d'un ABR en ordre croissant :", "choix": [r"infixe", r"préfixe", r"suffixe", r"en largeur"], "bonne": 0},
    {"notion": "abr", "type": "vf", "q": r"Le minimum d'un ABR non vide est toujours une feuille.", "bonne": False},
    {"notion": "abr_ajout", "type": "qcm", "q": r"Ajout en racine de $x$ : on coupe l'arbre en :", "choix": [r"clés $\le x$ et clés $>x$", r"sous-arbre gauche et droit de la racine", r"deux moitiés de même taille", r"feuilles et nœuds internes"], "bonne": 0},
    {"notion": "abr_ajout", "type": "vf", "q": r"Après des ajouts en feuille, la première valeur ajoutée est la racine.", "bonne": True},
    {"notion": "abr_supp", "type": "qcm", "q": r"Suppression d'un point double : la clé est remplacée par :", "choix": [r"le maximum du sous-arbre gauche", r"le minimum du sous-arbre gauche", r"le maximum du sous-arbre droit", r"la clé du père"], "bonne": 0},
    {"notion": "abr_supp", "type": "vf", "q": r"Le maximum du sous-arbre gauche n'a pas de fils droit.", "bonne": True},
    {"notion": "abr_taille", "type": "qcm", "q": r"Taille gauche $g$, on cherche le $k$-ième avec $k>g+1$ : on cherche à droite le :", "choix": [r"$(k-g-1)$-ième", r"$k$-ième", r"$(k-g)$-ième", r"$(k-1)$-ième"], "bonne": 0},
    {"notion": "abr_taille", "type": "vf", "q": r"Dans `addBSTSize`, on incrémente la taille de chaque nœud du chemin même si la clé était déjà présente.", "bonne": False},
    {"notion": "avl", "type": "qcm", "q": r"Déséquilibre d'un nœud :", "choix": [r"$h(G)-h(D)$", r"$h(D)-h(G)$", r"taille$(G)-$taille$(D)$", r"$|h(G)-h(D)|$"], "bonne": 0},
    {"notion": "avl", "type": "vf", "q": r"Un arbre de Fibonacci est un AVL.", "bonne": True},
    {"notion": "rotations", "type": "qcm", "q": r"Racine à $+2$, fils gauche à $-1$ :", "choix": [r"rotation gauche-droite", r"rotation droite", r"rotation gauche", r"rotation droite-gauche"], "bonne": 0},
    {"notion": "rotations", "type": "vf", "q": r"Une rotation change l'ordre infixe des clés.", "bonne": False},
    {"notion": "avl_modif", "type": "qcm", "q": r"Après un ajout et une rotation, la hauteur du sous-arbre :", "choix": [r"redevient celle d'avant l'ajout", r"augmente de 1", r"diminue de 1", r"dépend du fils"], "bonne": 0},
    {"notion": "avl_modif", "type": "vf", "q": r"Une suppression dans un AVL peut demander plusieurs rotations.", "bonne": True},
]

_FL = {
    1: r"racine `H[1]` · fils $2i$, $2i+1$ · père $i\,//\,2$ · feuille $2i>n$ · point simple $2i=n$",
    2: r"ajout : `append` puis remonter · suppression : dernier en racine puis descendre vers le plus petit fils",
    3: r"diminution : remonter · augmentation : descendre · heapify : descendre de $n\,//\,2$ à $1$ · tri $O(n\log n)$",
    4: r"min tout à gauche, max tout à droite · recherche : `while B != None and x != B.key`",
    5: r"`if x <= B.key: B.left = addBST(x, B.left)` · itératif : garder le père",
    6: r"feuille/point simple : renvoyer l'autre fils · point double : `B.key = maxBST(B.left)` puis supprimer à gauche",
    7: r"`cut` : clés $\le x$ / $>x$ le long du chemin · `BinTree(x, L, R)`",
    8: r"second min : min du droit du minimum, sinon son père · $x\le$ racine : racine $+$ droit $\ge x$ · lca : séparer $x$ et $y$",
    9: r"$g$ = taille gauche · $k=g+1$ racine · $k\le g$ gauche · sinon $(k-g-1)$ à droite · médiane $(n+1)\,//\,2$",
    10: r"déséq. $h(G)-h(D)$ · $+2$ : gauche à $-1$ : `lrr`, sinon `rr` · $-2$ : droit à $+1$ : `rlr`, sinon `lr`",
    11: r"ajout : hauteur changée si déséq. $\pm1$ · après rotation : inchangée · $N_h=N_{h-1}+N_{h-2}+1$",
    12: r"suppression : hauteur changée si déséq. $0$ · fils à $0$ : rotation simple, hauteur inchangée",
    13: r"rotations notées rg, rd, rgd, rdg · $h_n=n-1$ · milieu en racine · successeur",
    14: r"auxiliaire (copie, taille) · taille $+1$ si ajouté · `nthBST` · `rebalancing` renvoie (arbre, hauteur changée)",
    15: r"profondeur restante · chemin de recherche · max à gauche · 2-3-4 : $k$ clés, $k+1$ fils, feuilles au même niveau",
}
FORMULES = {e["id"]: _FL[lvl["n"]] for lvl in LEVELS for e in lvl["exos"]}

assert len(CHECKED) == len(set(CHECKED)), "duplicate exercise id"
