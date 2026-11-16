"""Level path: S2 algorithmics, matrices as lists of lists in Python (Algo-S2-Mat, exam B3 in March, 45 min).

Sources: no Moodle course for S2 algo on the server; calibrated on Epidocs Past-Exams (PDFs in `annales/raw/S2`):
B3 « Matrices » exams of 12 March 2024 (`Midterms/Algo/2028/MATRICES`, scan) and 5 March 2025
(`Midterms/Algo/2029/MATRICES`), and the official corrections of the older C2 tests: 22 February 2017 (folder 2021:
maxGapMatrix, dungeon), 4 March 2019 (2023: maxgap, searchMatrix), 2 March 2020 (2024: Siamese, sub_line), the 2020
English test (2020: minimax, posMinimax) and the S2# tests (2021#: isSymmetric; 2025: matrix_sorted).

Checks at import (build.py imports this module): every model solution replays the statement's `>>>` session and
passes the exam annex check of `algo_abg._api` (only `len`, `range`, `append`, two-value `min`/`max`; no slice, no
`in` test, no list operator); every « what does it print » program is run (`algo_python.pr`). Matrices in statements
are printed as aligned text (`mat()`).
The official `sub_line` (first version, 2020) loops `while j < colM - n`: it misses a list placed at the end of a row
(asserted below); the path teaches the `<=` bound.
"""
from . import algo_abg as abg
from .algo_python import _out, _py, prv
from .algo_python import pr as _pr

SUBJECT = {
    "id": "algo-s2-matrices",
    "ordre": 625,
    "matiere": "algo",
    "semestre": "S2",
    "ecue": "Matrices",
    "titre": "Matrices en Python : listes de listes, parcours, recherches, constructions",
    "chapitres_moodle": [],
    "td": "Examens B3 Matrices de mars 2024 et mars 2025, corrigés officiels des contrôles C2 de 2017 à 2020",
    "examens": ["Examen écrit B3 d'algorithmique, matrices (Python, 45 min, début mars)"],
}

CHECKED = []
S = "Calé sur les examens B3 Matrices (Past-Exams S2/Midterms/Algo/2028|2029/MATRICES)"
C17 = "Contrôle C2, 22 février 2017, corrigé officiel (Past-Exams S2/Midterms/Algo/2021)"
C19 = "Contrôle C2, 4 mars 2019, corrigé officiel (Past-Exams S2/Midterms/Algo/2023)"
C20 = "Contrôle C2, 2 mars 2020, corrigé officiel (Past-Exams S2/Midterms/Algo/2024)"
C20E = "Test #2, 2020, corrigé officiel en anglais (Past-Exams S2/Midterms/Algo/2020)"
CS = "Contrôle C2 S2#, corrigé officiel (Past-Exams S2/Midterms/Algo/2021#)"
C25 = "Contrôle C2, corrigé officiel (Past-Exams S2/Midterms/Algo/2025)"
B24 = "Examen B3 Matrices, 12 mars 2024 (Past-Exams S2/Midterms/Algo/2028/MATRICES), pas de corrigé officiel"
B25 = "Examen B3 Matrices, 5 mars 2025 (Past-Exams S2/Midterms/Algo/2029/MATRICES), pas de corrigé officiel"
RULE = "Annexe de l'examen : seuls `append`, `len` et `range` ; aucun opérateur sur les listes (`+`, `*`, `==`…)."


def pr(id, code, out, sol, src=None, duree=2):
    """« What does it print? » (algo_python.pr) with this path's source by default."""
    return _pr(id, code, out, sol, src=src or S, duree=duree)


def mat(M):
    """Matrix as aligned text in a code block."""
    w = max(len(str(x)) for row in M for x in row)
    return _out("\n".join(" ".join(str(x).rjust(w) for x in row) for row in M))


def w(id, enonce, code, tests, sol="", src=None, duree=8):
    """« Write the function »: the model replays the session and passes the exam annex check."""
    CHECKED.append(id)
    return {"id": id, "kind": "open", **abg._w(enonce, code, tests, sol, {}, (), False, True, []), "src": src or S, "duree": duree}


def wv(enonce, code, tests, sol=""):
    return abg._w(enonce, code, tests, sol, {}, (), False, True, [])


def o(id, enonce, sol, src=None, duree=4):
    return {"id": id, "kind": "open", "enonce": enonce, "sol": sol, "src": src or S, "duree": duree}


def v(id, enonce, ans, sol, src=None, duree=2):
    a = str(ans)
    return {"id": id, "kind": "value", "enonce": enonce, "calc": a, "ans": a, "sol": f"**Réponse :** ${a}$\n\n{sol}",
            "src": src or S, "duree": duree}


def run(code, expr):
    """Value of `expr` after running `code` (namespace of the exam: plain Python)."""
    ns = {}
    exec(code, ns)
    return eval(expr, ns)


# ---------------------------------------------------------------- model code

INIT = '''def init(l, c, val):
    M = []
    for i in range(l):
        L = []
        for j in range(c):
            L.append(val)
        M.append(L)
    return M'''

SIAMESE = INIT + '''

def Siamese(n):
    """n odd, n > 2"""
    S = init(n, n, 0)
    (i, j) = (n - 1, n // 2)
    for val in range(1, n * n + 1):
        S[i][j] = val
        if val % n == 0:
            i = i - 1
            if i == -1:
                i = n - 1
        else:
            (i, j) = ((i + 1) % n, (j + 1) % n)
    return S'''

MAGIC = '''def is_magic(M):
    n = len(M)
    target = 0
    for j in range(n):
        target = target + M[0][j]
    (d1, d2) = (0, 0)
    for i in range(n):
        d1 = d1 + M[i][i]
        d2 = d2 + M[i][n - 1 - i]
    ok = d1 == target and d2 == target
    i = 0
    while i < n and ok:
        (row, col) = (0, 0)
        for j in range(n):
            row = row + M[i][j]
            col = col + M[j][i]
        ok = row == target and col == target
        i = i + 1
    return ok'''

SUB_OFFICIAL_1 = '''def sub_line(M, L):
    (lineM, colM) = (len(M), len(M[0]))
    n = len(L)
    if n > colM:
        return False
    else:
        i = 0
        ok = False
        while i < lineM and not ok:
            j = 0
            while j < colM - n and not ok:
                k = 0
                while k < n and L[k] == M[i][j + k]:
                    k += 1
                ok = (k == n)
                j += 1
            i += 1
        return ok'''

SUB = '''def sub_line(M, L):
    (lineM, colM, n) = (len(M), len(M[0]), len(L))
    ok = False
    i = 0
    while i < lineM and not ok:
        j = 0
        while j <= colM - n and not ok:
            k = 0
            while k < n and L[k] == M[i][j + k]:
                k += 1
            ok = (k == n)
            j += 1
        i += 1
    return ok'''

MAT1 = [[1, 1, 10, 10, 7], [10, 0, 9, 3, 8], [3, 1, 4, 7, 5], [0, 8, 1, 1, 1], [4, 5, 1, 8, 9], [12, 11, 7, 8, 1], [6, 2, 10, 9, 8]]
assert run(SUB_OFFICIAL_1, f"sub_line({MAT1!r}, [10, 7])") is False  # the official bound misses the end of a row
assert run(SUB, f"sub_line({MAT1!r}, [10, 7])") is True

MYST25 = '''def mystery(L):
    res = []
    max_col = 0
    for i in range(len(L)):
        line, col = L[i]
        n = len(res)
        for j in range(n, line + 1):
            res.append([])
        nline = len(res[line])
        for j in range(nline, col + 1):
            res[line].append(-1)
        res[line][col] = i
        if col > max_col:
            max_col = col
    for i in range(len(res)):
        for j in range(len(res[i]), max_col + 1):
            res[i].append(-1)
    return res'''
MYST25_RES = run(MYST25, "mystery([(8, 2), (7, 2), (2, 5)])")
MYST25_B = run(MYST25, "mystery([(1, 3), (0, 0), (2, 1)])")

MAGIC5 = run(SIAMESE, "Siamese(5)")
assert run(MAGIC, f"is_magic({MAGIC5!r})")

DUNGEON = [[0, 2, 3], [2, 10, 0], [3, 0, 1]]
GAPMAT = [[1, 10, 3, 0, -3, 2, 8], [-1, 0, 1, 8, 5, 0, -4], [10, 9, 14, 1, 4, -5, 1], [10, -3, 7, 11, 6, 3, 0], [7, 8, -5, 1, 5, 4, 10]]
MS = [[19, 13, -6, -7, -1], [8, 20, 17, -2, 2], [-5, 15, -5, 7, -3]]

# ---------------------------------------------------------------- course

NOTIONS = [
    {"id": "listes", "titre": "Matrice = liste de lignes",
     "formule": r"`M[i][j]` : ligne $i$, colonne $j$ · lignes : `len(M)` · colonnes : `len(M[0])` · `M[i]` est une liste (la ligne) · deux noms pour une même liste : modifier l'un modifie l'autre",
     "exemple": r"`M = [[1, 2, 3], [4, 5, 6]]` : `len(M) == 2`, `M[1][2] == 6`",
     "cours": r"En Python, une matrice est une liste de lignes de même longueur. Ajouter deux fois la même liste `L` à `M` crée deux lignes qui sont le même objet."},
    {"id": "construction", "titre": "Construire une matrice",
     "formule": r"une nouvelle liste `L = []` par ligne · `L.append(val)` $c$ fois · `M.append(L)` · jamais deux fois la même ligne · copie : recopier élément par élément",
     "exemple": r"`init(2, 3, 0)` donne `[[0, 0, 0], [0, 0, 0]]`",
     "cours": r"À l'examen, ni `*` ni `+` sur les listes : on construit chaque ligne par une boucle d'`append`. Construire « une nouvelle matrice » impose de recopier les valeurs, pas les lignes."},
    {"id": "parcours", "titre": "Parcours complets",
     "formule": r"`for i in range(len(M)):` puis `for j in range(len(M[0])):` · accumulateur initialisé avant les boucles · extremum : partir de `M[0][0]` ou de `L[0]`",
     "exemple": r"somme : `s = s + M[i][j]` pour tout $(i, j)$",
     "cours": r"Un parcours complet visite les $l\times c$ cases, ligne par ligne. Une fonction auxiliaire sur une ligne (gap, maximum) simplifie souvent l'écriture."},
    {"id": "recherche", "titre": "Recherches avec arrêt",
     "formule": r"`while i < l and not found:` · boucle interne `while j < c and M[i][j] != x:` · trouvé si `j < c` · `(-1, -1)` si absent",
     "exemple": r"première position de $x$ ligne par ligne",
     "cours": r"Dès qu'on peut conclure, on s'arrête : l'optimisation est notée. Les booléens d'arrêt se testent dans la condition du `while`, pas avec `break`."},
    {"id": "lignes", "titre": "Lignes, colonnes, diagonales",
     "formule": r"colonne $j$ : `M[i][j]` pour $i$ variant · diagonale : `M[i][i]` · antidiagonale : `M[i][n - 1 - i]` · symétrique : `M[i][j] == M[j][i]` · axe vertical : `M[i][j] == M[i][c - 1 - j]`",
     "exemple": r"minimax : minimum des maximums des lignes",
     "cours": r"Pour une colonne, on fixe $j$ et on fait varier $i$. Une matrice symétrique est carrée ; il suffit de tester $j<i$, mais le corrigé teste toutes les cases."},
    {"id": "tests", "titre": "Tester une propriété",
     "formule": r"booléen `ok` initialisé à `True` · boucle `while i < l and ok` · liste triée : `while i < n - 1 and L[i] <= L[i + 1]` puis `i == n - 1` · sous-liste : départs $j$ de $0$ à $c-n$ inclus",
     "exemple": r"`matrix_sorted` : chaque ligne triée et `M[i - 1][c - 1] < M[i][0]`",
     "cours": r"On cherche un contre-exemple et on s'arrête au premier. Attention aux bornes : une sous-liste de longueur $n$ peut commencer jusqu'à l'indice $c-n$ inclus."},
    {"id": "calcul", "titre": "Transposée, produit, rotations",
     "formule": r"transposée : `T[j][i] = M[i][j]`, taille $c\times l$ · produit : `C[i][j]` $=\sum_k$ `A[i][k] * B[k][j]` · rotation d'un quart de tour horaire : `R[i][j] = M[l - 1 - j][i]` · décalage de $k$ vers la droite : `L[(j - k) % n]`",
     "exemple": r"`[[1, 2], [3, 4]]` tourné : `[[3, 1], [4, 2]]`",
     "cours": r"Une transformation se construit case par case : on écrit d'abord la formule de la case d'arrivée en fonction de la case de départ, puis la double boucle sur la matrice d'arrivée."},
    {"id": "magique", "titre": "Carré magique, méthode siamoise",
     "formule": r"somme magique $n(n^2+1)/2$ · siamoise ($n$ impair) : $1$ en bas au milieu · si la valeur est multiple de $n$, monter d'une case · sinon descendre d'une case vers la droite, modulo $n$",
     "exemple": r"ordre $3$ : somme magique $15$",
     "cours": r"Les lignes, les colonnes et les deux diagonales d'un carré magique ont la même somme. Les indices circulaires se gèrent avec `% n`."},
    {"id": "dynamique", "titre": "Chemins dans une grille",
     "formule": r"déplacements droite ou bas · `M[0][j] += M[0][j - 1]`, `M[i][0] += M[i - 1][0]` · `M[i][j] += min(M[i - 1][j], M[i][j - 1])` · réponse dans `M[l - 1][c - 1]`",
     "exemple": r"donjon : points de vie minimum $=$ coût minimal $+1$",
     "cours": r"Le meilleur chemin vers une case vient de celle du dessus ou de celle de gauche : on remplit la grille ligne par ligne, chaque case ne dépend que de cases déjà calculées."},
]

# ---------------------------------------------------------------- levels

LEVELS = [
    {"n": 1, "titre": "Listes de listes : indices, dimensions, alias", "notions": ["listes"], "exos": [
        pr("m11", "M = [[1, 2, 3], [4, 5, 6]]\nprint(len(M), len(M[0]), M[1][2])", "2 3 6",
           r"`len(M)` compte les lignes, `len(M[0])` les colonnes.", duree=1),
        pr("m12", "L = [0, 0]\nM = []\nfor i in range(3):\n    M.append(L)\nM[0][1] = 5\nprint(M)", "[[0, 5], [0, 5], [0, 5]]",
           r"Les trois lignes sont la même liste `L` : une modification se voit partout. Il faut créer une nouvelle liste par ligne."),
        pr("m13", "M = [[1, 2], [3, 4], [5, 6]]\nfor j in range(len(M[0])):\n    for i in range(len(M)):\n        print(M[i][j], end=\" \")",
           "1 3 5 2 4 6", r"Boucle externe sur les colonnes : on lit la matrice colonne par colonne."),
        pr("m14", "M = [[1, 2], [3, 4]]\nR = M[1]\nR.append(9)\nprint(len(M[1]), M)", "3 [[1, 2], [3, 4, 9]]",
           r"`R` est la ligne elle-même, pas une copie."),
    ]},
    {"n": 2, "titre": "Construire une matrice", "notions": ["construction", "listes"], "exos": [
        w("m21", r"Écrire la fonction `init(l, c, val)` qui renvoie une nouvelle matrice de $l$ lignes et $c$ colonnes remplie de `val`.", INIT,
          [("init(2, 3, 0)", "[[0, 0, 0], [0, 0, 0]]"), ("M = init(2, 2, 1)", None), ("M[0][0] = 7", None), ("M", "[[7, 1], [1, 1]]")],
          r"Une nouvelle liste par ligne : modifier `M[0][0]` ne touche pas la ligne $1$. " + RULE, duree=4),
        w("m22", r"Écrire la fonction `identity(n)` qui renvoie la matrice identité de taille $n$.",
          "def identity(n):\n    M = []\n    for i in range(n):\n        L = []\n        for j in range(n):\n            if i == j:\n                L.append(1)\n            else:\n                L.append(0)\n        M.append(L)\n    return M",
          [("identity(3)", "[[1, 0, 0], [0, 1, 0], [0, 0, 1]]")], duree=4),
        w("m23", r"Écrire la fonction `copy(M)` qui renvoie une copie de la matrice `M` (aucune ligne partagée).",
          "def copy(M):\n    C = []\n    for i in range(len(M)):\n        L = []\n        for j in range(len(M[i])):\n            L.append(M[i][j])\n        C.append(L)\n    return C",
          [("M = [[1, 2], [3, 4]]", None), ("C = copy(M)", None), ("C[0][0] = 9", None), ("M", "[[1, 2], [3, 4]]"), ("C", "[[9, 2], [3, 4]]")],
          r"Sans `[:]` ni `+` : chaque élément est recopié dans une nouvelle ligne.", duree=4),
        w("m24", r"Écrire la fonction `table(n)` qui renvoie la table de multiplication $n\times n$ : case $(i, j)$ égale à $(i+1)(j+1)$.",
          "def table(n):\n    M = []\n    for i in range(n):\n        L = []\n        for j in range(n):\n            L.append((i + 1) * (j + 1))\n        M.append(L)\n    return M",
          [("table(3)", "[[1, 2, 3], [2, 4, 6], [3, 6, 9]]")], duree=3),
    ]},
    {"n": 3, "titre": "Parcours complets", "notions": ["parcours"], "exos": [
        w("m31", r"Écrire la fonction `sum_matrix(M)` : somme des éléments de la matrice `M`.",
          "def sum_matrix(M):\n    s = 0\n    for i in range(len(M)):\n        for j in range(len(M[0])):\n            s = s + M[i][j]\n    return s",
          [("sum_matrix([[1, 2, 3], [4, 5, 6]])", "21"), ("sum_matrix([[-1]])", "-1")], duree=3),
        w("m32", r"Le gap d'une liste est l'écart maximum entre deux de ses valeurs. Écrire la fonction `maxgap(M)` qui renvoie le gap maximum des lignes de la matrice non vide `M`.",
          "def gaplist(L):\n    \"\"\"gap of the non empty list L\"\"\"\n    (valMin, valMax) = (L[0], L[0])\n    for i in range(1, len(L)):\n        valMin = min(valMin, L[i])\n        valMax = max(valMax, L[i])\n    return valMax - valMin\n\ndef maxgap(M):\n    mgap = gaplist(M[0])\n    for i in range(1, len(M)):\n        mgap = max(mgap, gaplist(M[i]))\n    return mgap",
          [(f"maxgap({GAPMAT!r})", "19")], r"Corrigé officiel : le gap d'une ligne est max $-$ min, en un seul passage ($19=14-(-5)$, ligne du milieu).", src=C19, duree=6),
        w("m33", r"Écrire la fonction `minimax(M)` : minimum des maximums des lignes de la matrice d'entiers `M` (non vide).",
          "def maxList(L):\n    \"\"\"maximum of the non empty list L\"\"\"\n    m = L[0]\n    for i in range(1, len(L)):\n        m = max(m, L[i])\n    return m\n\ndef minimax(M):\n    m = maxList(M[0])\n    for i in range(1, len(M)):\n        m = min(m, maxList(M[i]))\n    return m",
          [("minimax([[1, 9, 2], [4, 5, 3], [7, 0, 8]])", "5")], r"Maximums des lignes : $9, 5, 8$ ; leur minimum : $5$.", src=C20E, duree=5),
        w("m34", r"Écrire `pos_minimax(M)` : position `(i, j)` de la valeur de `minimax(M)` (premier maximum de la ligne, première ligne en cas d'égalité).",
          "def posMaxList(L):\n    \"\"\"position of the first maximum of the non empty list L\"\"\"\n    p = 0\n    for i in range(1, len(L)):\n        if L[i] > L[p]:\n            p = i\n    return p\n\ndef pos_minimax(M):\n    (min_i, min_j) = (0, posMaxList(M[0]))\n    for i in range(1, len(M)):\n        max_j = posMaxList(M[i])\n        if M[i][max_j] < M[min_i][min_j]:\n            (min_i, min_j) = (i, max_j)\n    return (min_i, min_j)",
          [("pos_minimax([[1, 9, 2], [4, 5, 3], [7, 0, 8]])", "(1, 1)")], r"Corrigé officiel : on garde des positions, la valeur se relit dans `M`.", src=C20E, duree=6),
    ]},
    {"n": 4, "titre": "Recherches avec arrêt", "notions": ["recherche"], "exos": [
        w("m41", r"Écrire la fonction `search_matrix(M, x)` qui renvoie la position `(i, j)` de la première valeur `x` trouvée (ligne par ligne) dans la matrice non vide `M`, ou `(-1, -1)`.",
          "def search_matrix(M, x):\n    (i, lin, col) = (0, len(M), len(M[0]))\n    found = -1\n    while i < lin and found == -1:\n        j = 0\n        while j < col and M[i][j] != x:\n            j += 1\n        if j != col:\n            found = j\n        i += 1\n    if found != -1:\n        return (i - 1, found)\n    else:\n        return (-1, -1)",
          [("search_matrix([[1, 2], [3, 4], [3, 5]], 3)", "(1, 0)"), ("search_matrix([[1, 2]], 7)", "(-1, -1)")],
          r"Corrigé officiel : `i` a déjà été incrémenté à la sortie, d'où `i - 1`.", src=C19, duree=6),
        w("m42", r"Écrire la fonction `zero_line(M)` qui renvoie l'indice de la première ligne de `M` entièrement nulle, $-1$ s'il n'y en a pas. Chaque ligne est abandonnée dès qu'un élément non nul est vu.",
          "def zero_line(M):\n    (l, c) = (len(M), len(M[0]))\n    i = 0\n    found = False\n    while i < l and not found:\n        j = 0\n        while j < c and M[i][j] == 0:\n            j += 1\n        found = j == c\n        i += 1\n    if found:\n        return i - 1\n    return -1",
          [("zero_line([[0, 1], [0, 0], [0, 0]])", "1"), ("zero_line([[1, 0], [0, 2]])", "-1")],
          r"Optimisation notée : arrêt dans la ligne au premier non nul, et arrêt global à la première ligne nulle.", duree=5),
        w("m43", r"Écrire la fonction `count_lines(M, x)` : nombre de lignes de `M` contenant au moins une fois `x` (on passe à la ligne suivante dès que `x` est trouvé).",
          "def count_lines(M, x):\n    n = 0\n    for i in range(len(M)):\n        j = 0\n        while j < len(M[i]) and M[i][j] != x:\n            j += 1\n        if j < len(M[i]):\n            n = n + 1\n    return n",
          [("count_lines([[1, 2, 1], [3, 4, 5], [1, 0, 0]], 1)", "2")], duree=5),
    ]},
    {"n": 5, "titre": "Lignes, colonnes, diagonales", "notions": ["lignes"], "exos": [
        w("m51", r"Écrire la fonction `col_sums(M)` : liste des sommes des colonnes de `M`.",
          "def col_sums(M):\n    R = []\n    for j in range(len(M[0])):\n        s = 0\n        for i in range(len(M)):\n            s = s + M[i][j]\n        R.append(s)\n    return R",
          [("col_sums([[1, 2, 3], [4, 5, 6]])", "[5, 7, 9]")], r"Colonne fixée dans la boucle externe.", duree=4),
        w("m52", r"Écrire la fonction `is_symmetric(A)` : vrai si la matrice `A` est carrée et symétrique ($A_{ij}=A_{ji}$).",
          "def is_symmetric(A):\n    (l, c) = (len(A), len(A[0]))\n    if l != c:\n        return False\n    (i, sym) = (0, True)\n    while i < l and sym:\n        j = 0\n        while j < l and sym:\n            sym = A[i][j] == A[j][i]\n            j += 1\n        i += 1\n    return sym",
          [("is_symmetric([[1, 2], [2, 3]])", "True"), ("is_symmetric([[1, 2], [3, 1]])", "False"), ("is_symmetric([[1, 2]])", "False")],
          r"Corrigé officiel. Il suffirait de tester $j<i$ : chaque paire est vue deux fois ici.", src=CS, duree=5),
        w("m53", r"Écrire la fonction `vertical_axis(M)` : vrai si chaque ligne de `M` est un palindrome (axe de symétrie vertical).",
          "def vertical_axis(M):\n    (l, c) = (len(M), len(M[0]))\n    (i, ok) = (0, True)\n    while i < l and ok:\n        j = 0\n        while j < c // 2 and M[i][j] == M[i][c - 1 - j]:\n            j += 1\n        ok = j == c // 2\n        i += 1\n    return ok",
          [("vertical_axis([[1, 2, 1], [5, 0, 5]])", "True"), ("vertical_axis([[1, 2, 2, 1], [1, 2, 3, 1]])", "False")],
          r"Case $(i, j)$ face à $(i, c-1-j)$ ; la colonne du milieu (si $c$ impair) n'a pas à être testée.", src=C20E, duree=6),
        w("m54", r"Écrire la fonction `trace(M)` : somme de la diagonale de la matrice carrée `M`, puis `anti_trace(M)` pour l'autre diagonale.",
          "def trace(M):\n    s = 0\n    for i in range(len(M)):\n        s = s + M[i][i]\n    return s\n\ndef anti_trace(M):\n    n = len(M)\n    s = 0\n    for i in range(n):\n        s = s + M[i][n - 1 - i]\n    return s",
          [("trace([[1, 2, 3], [4, 5, 6], [7, 8, 9]])", "15"), ("anti_trace([[1, 2, 3], [4, 5, 6], [7, 8, 9]])", "15")], duree=3),
    ]},
    {"n": 6, "titre": "Tester une propriété", "notions": ["tests"], "exos": [
        w("m61", r"Écrire `list_sorted(L, n)` (liste non vide de longueur $n$ triée en ordre croissant ?) puis `matrix_sorted(M)` : chaque ligne triée, et tout élément d'une ligne (sauf la première) strictement supérieur à tous ceux de la ligne précédente.",
          "def list_sorted(L, n):\n    i = 0\n    while i < n - 1 and L[i] <= L[i + 1]:\n        i += 1\n    return i == n - 1\n\ndef matrix_sorted(M):\n    (l, c) = (len(M), len(M[0]))\n    ok = list_sorted(M[0], c)\n    i = 1\n    while i < l and ok:\n        ok = M[i - 1][c - 1] < M[i][0] and list_sorted(M[i], c)\n        i += 1\n    return ok",
          [("matrix_sorted([[1, 2, 3]])", "True"), ("matrix_sorted([[1, 2, 3], [40, 5, 6]])", "False"), ("matrix_sorted([[1, 2, 3], [7, 8, 9], [4, 5, 6]])", "False"),
           ("matrix_sorted([[1, 2, 3], [4, 5, 6], [7, 8, 9]])", "True"), ("matrix_sorted([[1, -1, 3], [4, 5, 6], [7, 8, 9]])", "False")],
          r"Les lignes étant triées, comparer le dernier de la ligne précédente au premier de la ligne suffit.", src=C25, duree=8),
        w("m62", r"Écrire la fonction `sub_line(M, L)` qui vérifie si la liste `L` apparaît (éléments consécutifs) dans une des lignes de la matrice non vide `M`.",
          SUB, [(f"sub_line({MAT1!r}, [1, 10])", "True"), (f"sub_line({MAT1!r}, [1, 10, 7])", "False"), (f"sub_line({MAT1!r}, [10, 7])", "True"), (f"sub_line({MAT1!r}, [1, 1, 1, 1])", "False")],
          r"Départs possibles : $j$ de $0$ à $c-n$ **inclus**. Le premier corrigé officiel boucle `while j < colM - n` et rate `[10, 7]` en fin de première ligne ; sa seconde version utilise bien `<=`.",
          src=C20, duree=10),
        w("m63", r"Écrire la fonction `is_matrix(L)` : vrai si la liste de listes non vide `L` est une matrice (toutes les lignes ont la même longueur).",
          "def is_matrix(L):\n    c = len(L[0])\n    i = 1\n    while i < len(L) and len(L[i]) == c:\n        i += 1\n    return i == len(L)",
          [("is_matrix([[1, 2], [3, 4]])", "True"), ("is_matrix([[1, 2], [3]])", "False")], duree=3),
    ]},
    {"n": 7, "titre": "Transposée, produit, rotations", "notions": ["calcul", "construction"], "exos": [
        w("m71", r"Écrire la fonction `transpose(M)` qui renvoie la transposée de `M` ($c$ lignes, $l$ colonnes).",
          "def transpose(M):\n    T = []\n    for j in range(len(M[0])):\n        L = []\n        for i in range(len(M)):\n            L.append(M[i][j])\n        T.append(L)\n    return T",
          [("transpose([[1, 2, 3], [4, 5, 6]])", "[[1, 4], [2, 5], [3, 6]]")], duree=4),
        w("m72", r"Écrire la fonction `product(A, B)` : produit des matrices $A$ ($n\times p$) et $B$ ($p\times q$).",
          "def product(A, B):\n    (n, p, q) = (len(A), len(B), len(B[0]))\n    C = []\n    for i in range(n):\n        L = []\n        for j in range(q):\n            s = 0\n            for k in range(p):\n                s = s + A[i][k] * B[k][j]\n            L.append(s)\n        C.append(L)\n    return C",
          [("product([[1, 2], [3, 4]], [[5, 6], [7, 8]])", "[[19, 22], [43, 50]]"), ("product([[1, 2, 3]], [[1], [0], [2]])", "[[7]]")], duree=6),
        w("m73", r"Écrire la fonction `rotate(M)` qui renvoie la matrice `M` tournée d'un quart de tour dans le sens horaire.",
          "def rotate(M):\n    (l, c) = (len(M), len(M[0]))\n    R = []\n    for i in range(c):\n        L = []\n        for j in range(l):\n            L.append(M[l - 1 - j][i])\n        R.append(L)\n    return R",
          [("rotate([[1, 2], [3, 4]])", "[[3, 1], [4, 2]]"), ("rotate([[1, 2, 3], [4, 5, 6]])", "[[4, 1], [5, 2], [6, 3]]")],
          r"La première ligne du résultat est la première colonne lue de bas en haut : `R[i][j] = M[l - 1 - j][i]`.", duree=6),
    ]},
    {"n": 8, "titre": "Carré magique", "notions": ["magique", "lignes"], "exos": [
        v("m81", r"Somme magique d'un carré magique d'ordre $5$ contenant les entiers de $1$ à $25$ ?", 65,
          r"La somme totale $\frac{25\times26}{2}=325$ se répartit sur $5$ lignes : $n(n^2+1)/2=65$."),
        o("m82", "Construire à la main le carré magique d'ordre 3 par la méthode siamoise : 1 en bas au milieu ; si la valeur est un multiple de 3, on remonte d'une case, sinon on descend d'une case vers la droite (indices modulo 3).",
          mat(run(SIAMESE, "Siamese(3)")) + "\n\nChaque ligne, colonne et diagonale vaut $15$.", src=C20, duree=5),
        w("m83", r"Écrire la fonction `Siamese(n)` qui construit le carré magique d'ordre $n$ (impair, $>2$) par la méthode siamoise.",
          SIAMESE, [("Siamese(3)", repr(run(SIAMESE, "Siamese(3)"))), ("Siamese(5)[4]", repr(MAGIC5[4]))],
          r"Corrigé officiel (avec `init` à la place de `matrix.init`). Le modulo gère la sortie à droite et en bas ; la remontée gère la ligne $-1$.", src=C20, duree=10),
        w("m84", r"Écrire la fonction `is_magic(M)` qui teste si la matrice carrée `M` est un carré magique (lignes, colonnes et diagonales de même somme).",
          MAGIC, [(f"is_magic({MAGIC5!r})", "True"), ("is_magic([[1, 2], [3, 4]])", "False")],
          r"Somme de référence : la première ligne. Lignes et colonnes testées dans la même boucle, arrêt au premier écart.", duree=8),
    ]},
    {"n": 9, "titre": "Chemins dans une grille et traces", "notions": ["dynamique", "listes"], "exos": [
        w("m91", r"Donjon : la princesse part en haut à gauche, le chevalier est en bas à droite, chaque case contient les points de vie perdus en y entrant ($\ge0$). Elle va seulement à droite ou en bas et meurt à $0$ point. Écrire `dungeon(M)` : points de vie minimum pour sauver le chevalier (`M` peut être modifiée).",
          "def dungeon(M):\n    (l, c) = (len(M), len(M[0]))\n    for j in range(1, c):\n        M[0][j] += M[0][j - 1]\n    for i in range(1, l):\n        M[i][0] += M[i - 1][0]\n    for i in range(1, l):\n        for j in range(1, c):\n            M[i][j] += min(M[i - 1][j], M[i][j - 1])\n    return M[l - 1][c - 1] + 1",
          [(f"dungeon({DUNGEON!r})", "7")],
          r"Corrigé officiel : chaque case reçoit le coût minimal pour l'atteindre (dessus ou gauche). Le chemin droite, droite, bas, bas coûte $6$ : il faut $7$ points.", src=C17, duree=10),
        o("m92", f"Dessiner la matrice résultat de `mystery([(1, 3), (0, 0), (2, 1)])`.\n\n{_py(MYST25)}",
          mat(MYST25_B) + "\n\nLe couple d'indice `i` place la valeur `i` en `(ligne, colonne)` ; les lignes sont créées et complétées par $-1$, puis toutes sont allongées jusqu'à la plus grande colonne.", duree=6),
        pr("m93", "M = []\nfor i in range(3):\n    M.append([])\n    for j in range(i + 1):\n        M[i].append(j)\nprint(M)", "[[0], [0, 1], [0, 1, 2]]",
                     r"Matrice « triangulaire » : les lignes n'ont pas la même longueur (ce n'est pas une matrice au sens strict)."),
    ]},
    {"n": 10, "titre": "Examen B3 Matrices du 12 mars 2024", "notions": ["tests", "calcul"], "exos": [
        w("m101", r"**Exercice 1 (Double, 6 points).** Écrire la fonction `check_mat(L)` avec `L` une liste de listes supposée non vide, qui vérifie que `L` est une matrice et que chaque ligne est le « double » de la précédente (chaque élément est le double de celui à la même place de la ligne précédente).",
          "def check_mat(L):\n    c = len(L[0])\n    ok = True\n    i = 1\n    while i < len(L) and ok:\n        if len(L[i]) != c:\n            ok = False\n        else:\n            j = 0\n            while j < c and L[i][j] == 2 * L[i - 1][j]:\n                j += 1\n            ok = j == c\n        i += 1\n    return ok",
          [("check_mat([[1, -1, 120, 10, -7], [2, -2, 240, 20, -14], [4, -4, 480, 40, -28]])", "True"),
           ("check_mat([[1, -1, 120, 10, -7], [4, -4, 480, 40, -28], [2, -2, 240, 20, -14]])", "False"),
           ("check_mat([[1, -1, 120, 10, -7], [2, -2, 240, 20, -14], [4, -4, 480]])", "False")],
          r"Longueur vérifiée avant de lire la ligne (sinon `IndexError`). Arrêt au premier écart.", src=B24, duree=12),
        w("m102", r"**Exercice 2 (Rotation, 4 points).** Écrire la fonction `build_rotation(L, k)` ($L$ liste d'entiers de longueur $n>0$, $0<k<n$) qui construit la matrice carrée dont la première ligne est `L` et dont chaque autre ligne contient les éléments de la précédente décalés de $k$ positions vers la droite.",
          "def build_rotation(L, k):\n    n = len(L)\n    M = []\n    for i in range(n):\n        R = []\n        for j in range(n):\n            R.append(L[(j - i * k) % n])\n        M.append(R)\n    return M",
          [("build_rotation([1, 2, 3, 4], 1)", "[[1, 2, 3, 4], [4, 1, 2, 3], [3, 4, 1, 2], [2, 3, 4, 1]]"),
           ("build_rotation([1, 2, 3, 4], 2)", "[[1, 2, 3, 4], [3, 4, 1, 2], [1, 2, 3, 4], [3, 4, 1, 2]]"),
           ("build_rotation([1, 2, 3, 4], 3)", "[[1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3]]")],
          r"La ligne $i$ est décalée de $ik$ : la case $j$ reçoit `L[(j - i * k) % n]`. Python donne un modulo positif même si `j - i * k` est négatif.",
          src=B24, duree=10),
        o("m103", "Donner `build_rotation([5, 6, 7, 8, 9], 2)` (examen du 12 mars 2024, exercice 2).",
          mat(run("def build_rotation(L, k):\n    n = len(L)\n    return [[L[(j - i * k) % n] for j in range(n)] for i in range(n)]", "build_rotation([5, 6, 7, 8, 9], 2)"))
          + "\n\nChaque ligne est la précédente décalée de $2$ vers la droite.", src=B24, duree=3),
    ]},
    {"n": 11, "titre": "Examen B3 Matrices du 5 mars 2025", "notions": ["recherche", "construction", "listes"], "exos": [
        w("m111", r"**Exercice 1 (Négatif, 4 points).** Écrire la fonction `detect_neg(M)` avec `M` une matrice d'entiers non vide qui renvoie `True` si `M` contient au moins un nombre négatif, `False` sinon.",
          "def detect_neg(M):\n    (l, c) = (len(M), len(M[0]))\n    i = 0\n    found = False\n    while i < l and not found:\n        j = 0\n        while j < c and not found:\n            found = M[i][j] < 0\n            j += 1\n        i += 1\n    return found",
          [("detect_neg([[1, 2, 3], [4, 5, 6]])", "False"), ("detect_neg([[1, 2, 3], [-4, 5, 6]])", "True")],
          r"Double `while` avec le même booléen d'arrêt : l'optimisation est notée.", src=B25, duree=8),
        w("m112", r"**Exercice 2 (Symétrique, 4 points).** Écrire la fonction `build_symmetric(M)` qui construit une nouvelle matrice : les lignes de la matrice non vide `M` en haut, puis les mêmes lignes dans l'ordre inverse en bas (l'énoncé écrit `build_symetric` dans l'exemple).",
          "def build_symmetric(M):\n    l = len(M)\n    R = []\n    for i in range(2 * l):\n        if i < l:\n            src = M[i]\n        else:\n            src = M[2 * l - 1 - i]\n        L = []\n        for j in range(len(src)):\n            L.append(src[j])\n        R.append(L)\n    return R",
          [(f"build_symmetric({MS!r})", repr(MS + MS[::-1]))],
          r"Nouvelle matrice : chaque ligne est recopiée, aucune n'est partagée avec `M`. La ligne $i\ge l$ du bas est la ligne $2l-1-i$.",
          src=B25, duree=8),
        o("m113", f"**Exercice 3 (Mystery, 2 points).** Dessiner la matrice résultat de `mystery([(8, 2), (7, 2), (2, 5)])`.\n\n{_py(MYST25)}",
          mat(MYST25_RES) + "\n\n$9$ lignes (jusqu'à la ligne $8$) et $6$ colonnes (jusqu'à la colonne $5$) ; seules les cases $(8, 2)$, $(7, 2)$ et $(2, 5)$ reçoivent les indices $0$, $1$, $2$.",
          src=B25, duree=6),
    ]},
]

VARIANTS = {
    "m11": [prv("M = [[7, 8], [9, 10], [11, 12]]\nprint(len(M), len(M[1]), M[2][0])", "3 2 11", r"$3$ lignes, $2$ colonnes.")],
    "m12": [prv("L = []\nM = [L, L]\nL.append(1)\nprint(M)", "[[1], [1]]", r"Deux fois la même liste.")],
    "m31": [wv(r"Écrire `count(M, x)` : nombre d'occurrences de `x` dans `M`.",
               "def count(M, x):\n    n = 0\n    for i in range(len(M)):\n        for j in range(len(M[0])):\n            if M[i][j] == x:\n                n = n + 1\n    return n",
               [("count([[1, 2], [2, 2]], 2)", "3")])],
    "m51": [wv(r"Écrire `row_sums(M)` : liste des sommes des lignes.",
               "def row_sums(M):\n    R = []\n    for i in range(len(M)):\n        s = 0\n        for j in range(len(M[0])):\n            s = s + M[i][j]\n        R.append(s)\n    return R",
               [("row_sums([[1, 2, 3], [4, 5, 6]])", "[6, 15]")])],
    "m81": [{"enonce": r"Somme magique d'un carré magique d'ordre $7$ (entiers de $1$ à $49$) ?", "calc": "175", "ans": "175",
             "sol": r"**Réponse :** $175$" + "\n\n" + r"$7\times50/2=175$."}],
}
for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["id"] in VARIANTS:
            _e["variants"] = VARIANTS[_e["id"]]

EXTRA_PARTS = []

QUIZ = [
    {"notion": "listes", "type": "qcm", "q": r"Nombre de colonnes de la matrice `M` :", "choix": [r"`len(M[0])`", r"`len(M)`", r"`len(M[1][0])`", r"`M.len()`"], "bonne": 0},
    {"notion": "listes", "type": "vf", "q": r"Après `M.append(L)` deux fois avec la même `L`, modifier `M[0][0]` modifie aussi `M[1][0]`.", "bonne": True},
    {"notion": "construction", "type": "qcm", "q": r"À l'examen, pour créer une ligne de $c$ zéros :", "choix": [r"boucle de `L.append(0)`", r"`[0] * c`", r"`L + [0]`", r"`list(range(c))`"], "bonne": 0},
    {"notion": "construction", "type": "vf", "q": r"`R.append(M[i])` recopie la ligne `M[i]`.", "bonne": False},
    {"notion": "parcours", "type": "qcm", "q": r"Pour le maximum d'une ligne non vide, on initialise avec :", "choix": [r"`L[0]`", r"`0`", r"`-1`", r"`len(L)`"], "bonne": 0},
    {"notion": "parcours", "type": "vf", "q": r"Le gap d'une liste est la différence entre son maximum et son minimum.", "bonne": True},
    {"notion": "recherche", "type": "qcm", "q": r"Recherche de $x$ dans une ligne : condition de la boucle interne ?", "choix": [r"`j < c and M[i][j] != x`", r"`M[i][j] != x and j < c`", r"`j <= c and M[i][j] != x`", r"`j < c or M[i][j] != x`"], "bonne": 0},
    {"notion": "recherche", "type": "vf", "q": r"Un parcours complet est noté comme une recherche optimisée.", "bonne": False},
    {"notion": "lignes", "type": "qcm", "q": r"Élément de l'antidiagonale de la ligne $i$ (matrice $n\times n$) :", "choix": [r"`M[i][n - 1 - i]`", r"`M[i][n - i]`", r"`M[n - i][i]`", r"`M[i][i]`"], "bonne": 0},
    {"notion": "lignes", "type": "vf", "q": r"Une matrice symétrique est forcément carrée.", "bonne": True},
    {"notion": "tests", "type": "qcm", "q": r"Sous-liste de longueur $n$ dans une ligne de longueur $c$ : derniers indice de départ possible :", "choix": [r"$c-n$", r"$c-n-1$", r"$c-1$", r"$n$"], "bonne": 0},
    {"notion": "tests", "type": "vf", "q": r"Pour tester qu'une matrice est triée (lignes triées), comparer `M[i - 1][c - 1]` à `M[i][0]` suffit entre deux lignes.", "bonne": True},
    {"notion": "calcul", "type": "qcm", "q": r"Taille de la transposée d'une matrice $3\times5$ :", "choix": [r"$5\times3$", r"$3\times5$", r"$5\times5$", r"$3\times3$"], "bonne": 0},
    {"notion": "calcul", "type": "vf", "q": r"Le produit $A\times B$ existe si le nombre de colonnes de $A$ égale le nombre de lignes de $B$.", "bonne": True},
    {"notion": "magique", "type": "qcm", "q": r"Somme magique d'ordre $3$ :", "choix": [r"$15$", r"$45$", r"$9$", r"$12$"], "bonne": 0},
    {"notion": "magique", "type": "vf", "q": r"La méthode siamoise marche pour tout $n$ pair.", "bonne": False},
    {"notion": "dynamique", "type": "qcm", "q": r"Déplacements droite/bas : le meilleur coût pour atteindre $(i, j)$ dépend de :", "choix": [r"$(i-1, j)$ et $(i, j-1)$", r"$(i+1, j)$ et $(i, j+1)$", r"toute la ligne $i$", r"la diagonale"], "bonne": 0},
    {"notion": "dynamique", "type": "vf", "q": r"Dans `dungeon`, la première ligne se remplit par sommes cumulées.", "bonne": True},
]

_FL = {
    1: r"`M[i][j]` · `len(M)` lignes, `len(M[0])` colonnes · même liste ajoutée deux fois : alias",
    2: r"`L = []` par ligne · `L.append(val)` · `M.append(L)` · copie élément par élément",
    3: r"double boucle `range(len(M))`, `range(len(M[0]))` · gap $=\max-\min$ · minimax : min des max des lignes",
    4: r"`while i < l and not found` · `while j < c and M[i][j] != x` · trouvé si `j < c`",
    5: r"colonne : $j$ fixé · diagonale `M[i][i]` · antidiagonale `M[i][n - 1 - i]` · symétrique `M[i][j] == M[j][i]` · axe `M[i][c - 1 - j]`",
    6: r"`while i < n - 1 and L[i] <= L[i + 1]` · départs $0\dots c-n$ inclus · longueur des lignes testée d'abord",
    7: r"`T[j][i] = M[i][j]` · `C[i][j]` $=\sum_k$ `A[i][k] * B[k][j]` · rotation `R[i][j] = M[l - 1 - j][i]`",
    8: r"somme magique $n(n^2+1)/2$ · siamoise : départ $(n-1, n//2)$, multiple de $n$ : monter, sinon $(i+1, j+1)$ modulo $n$",
    9: r"`M[i][j] += min(M[i - 1][j], M[i][j - 1])` · lignes de longueurs différentes : `len(M[i])`",
    10: r"`len(L[i]) != c` avant de lire · `L[(j - i * k) % n]`",
    11: r"double `while` avec booléen · recopie des lignes · ligne du bas $2l-1-i$",
}
FORMULES = {e["id"]: _FL[lvl["n"]] for lvl in LEVELS for e in lvl["exos"]}

assert len(CHECKED) == len(set(CHECKED)), "duplicate exercise id"
