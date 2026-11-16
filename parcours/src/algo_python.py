"""Level path: S1 algorithmics, Python part (lists with append/pop/len/range, searching, dichotomy, sorting).

Sources: the Moodle course « Python et Environnement de Travail » only links to prepa.pages.epita.fr (GitLab login),
so this path is calibrated on the past exams of the Epidocs Past-Exams repo, `S1/Finals/Algo/*` (PDFs in
`annales/raw`): partiel P1 of 8 January 2019 (folder 2023), 18 January 2021 (2025), 4 January 2022 (2026) and the
B2 exam of 7 January 2025 (`2029/PYTHON`), plus folders 2021/2022/2024 (official corrections). Levels 13 to 15 are
the 2021, 2022 and 2025 exams.

Every model solution and every « what does it print » program is run when this module is imported (build.py
imports it, so a wrong hand-written answer stops the build):
- `w()` replays the `>>>` session of the statement on the model code (repr of each value, or `Exception: msg`);
- `_api()` rejects any model that breaks the exam rule (annex of the subjects): only `len`, `range`, `append`,
  `pop()` without argument and `raise Exception(...)`, no slice, no `in` test, no operator on lists;
- dichotomy counts come from `_steps()`, the version of the official decision tree (correction of January 2018:
  inclusive bounds, middle (left + right) // 2, stop when the bounds are equal or cross; every node met, leaves
  included, costs two element comparisons), which gives the official answers (8 for λ, 32 for 32768). The official
  answer « 65536 » to « longest list giving k + 2 comparisons » only doubles the length: with this version every
  length up to 2^17 - 1 = 131071 gives 34 comparisons, so the exercise asks for 131071 and says why.
"""
import ast
import contextlib
import io

SUBJECT = {
    "id": "algo-s1-python",
    "ordre": 620,
    "matiere": "algo",
    "semestre": "S1",
    "ecue": "Algorithmique Python",
    "titre": "Algorithmique en Python : listes, recherche, dichotomie, tris",
    "chapitres_moodle": [],
    "td": "Calé sur les partiels P1 (janvier 2019, 2021, 2022) et l'examen B2 du 7 janvier 2025 : cours Moodle = liens GitLab seulement",
    "examens": ["Examen écrit B2 d'algorithmique Python (1 h 30, début janvier)"],
}

ALLOWED = {"len", "range", "Exception"}
CHECKED = []  # ids of exercises whose code ran, for the self-check at the end


def _api(code):
    """Exam rule: only len, range, append, pop() and raise Exception; no slice, no `in` test, no list operator."""
    tree = ast.parse(code)
    defined = {n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}
    for n in ast.walk(tree):
        bad = None
        if isinstance(n, ast.Call):
            f = n.func
            if isinstance(f, ast.Name) and f.id not in ALLOWED | defined:
                bad = f"function {f.id}"
            elif isinstance(f, ast.Attribute) and (f.attr not in ("append", "pop") or (f.attr == "pop" and n.args)):
                bad = f"method {f.attr}"
        elif isinstance(n, ast.Slice):
            bad = "slice"
        elif isinstance(n, ast.Compare) and any(isinstance(op, (ast.In, ast.NotIn)) for op in n.ops):
            bad = "`in` test"
        # shortcut: only list literals are seen as lists (`L + M` with two names passes), review models by eye
        elif isinstance(n, ast.BinOp) and (isinstance(n.left, ast.List) or isinstance(n.right, ast.List)):
            bad = "operator on a list"
        elif isinstance(n, (ast.ListComp, ast.GeneratorExp, ast.Import, ast.ImportFrom, ast.Lambda)):
            bad = type(n).__name__
        assert not bad, f"exam rule broken ({bad}) in:\n{code}"


def _run(code, tests):
    ns = {}
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


def _stdout(code):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        exec(code, {})
    return buf.getvalue()


def _py(s):
    return f"```python\n{s}\n```"


def _out(s):
    return f"```\n{s}\n```"


def _session(tests):
    return "\n".join(f">>> {line}" + ("" if exp is None else f"\n{exp}") for line, exp in tests)


def _w(enonce, code, tests, sol, api=True):
    code = code.strip()
    if api:
        _api(code)
    _run(code, tests)
    return {"enonce": f"{enonce}\n\nExemples d'applications :\n\n{_out(_session(tests))}",
            "sol": _py(code) + (f"\n\n{sol}" if sol else "")}


def w(id, enonce, code, tests, sol="", src=None, duree=6, api=True):
    """« Write the function » exercise: the model code must replay the whole `>>>` session."""
    CHECKED.append(id)
    return {"id": id, "kind": "open", **_w(enonce, code, tests, sol, api), "src": src or S, "duree": duree}


def wv(enonce, code, tests, sol=""):
    """Variant of a w() exercise, checked too."""
    return _w(enonce, code, tests, sol)


def _pr(code, out, sol, enonce):
    code = code.strip()
    got = _stdout(code)
    assert " ".join(got.split()) == " ".join(out.split()), f"printed {got!r}, expected {out!r}\n{code}"
    return {"enonce": f"{enonce}\n\n{_py(code)}", "sol": f"**Affichage :**\n\n{_out(out)}\n\n{sol}"}


PR = "Qu'affiche ce programme ? (donner exactement la sortie)"


def pr(id, code, out, sol, enonce=PR, src=None, duree=2):
    """« What does it print? » exercise; the output is checked by running the program."""
    CHECKED.append(id)
    return {"id": id, "kind": "open", **_pr(code, out, sol, enonce), "src": src or S, "duree": duree}


def prv(code, out, sol, enonce=PR):
    return _pr(code, out, sol, enonce)


def v(id, enonce, calc, ans, sol, src=None, duree=2):
    return {"id": id, "kind": "value", "enonce": enonce, "calc": calc, "ans": ans, "sol": sol, "src": src or S, "duree": duree}


def o(id, enonce, sol, src=None, duree=4):
    return {"id": id, "kind": "open", "enonce": enonce, "sol": sol, "src": src or S, "duree": duree}


def _steps(L, x):
    """Course dichotomy on sorted L: number of nodes met (2 element comparisons each) and their values."""
    left, right, met = 0, len(L) - 1, []
    while left <= right:
        mid = (left + right) // 2
        met.append(L[mid])
        if left == right or x == L[mid]:
            break
        if x < L[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return len(met), met


def _worst(n):
    """Worst number of steps of a negative search in a list of n elements (search after every element)."""
    L = list(range(0, 2 * n, 2))
    return max(_steps(L, x)[0] for x in range(-1, 2 * n, 2))


def _path_ok(seq, x):
    """Can `seq` be the values met by a dichotomic search of x? Each value bounds every later one on x's side."""
    return all((x < a) == (b < a) for i, a in enumerate(seq) for b in seq[i + 1:] if a != x)


def _garage_ok(moves):
    """One stack (entrance side does not matter): never more exits than entries, empty at the end."""
    n = 0
    for m in moves:
        n += -1 if m == "s" else 1
        if n < 0:
            return False
    return n == 0


S = "Calé sur les partiels P1 d'algorithmique Python (Past-Exams S1/Finals/Algo)"
P19 = "Partiel P1 algo, 8 janvier 2019 (Past-Exams S1/Finals/Algo/2023)"
P21 = "Partiel P1 algo, 18 janvier 2021 (Past-Exams S1/Finals/Algo/2025)"
P22 = "Partiel P1 algo, 4 janvier 2022 (Past-Exams S1/Finals/Algo/2026)"
P17 = "Partiel P1 algo, promo 2021 (Past-Exams S1/Finals/Algo/2021 et 2024, corrigé officiel)"
P2022 = "Partiel P1 algo, promo 2022 (Past-Exams S1/Finals/Algo/2022, corrigé officiel)"
B25 = "Examen B2 algo Python, 7 janvier 2025 (Past-Exams S1/Finals/Algo/2029/PYTHON)"
RULE = "Seuls `len`, `range`, `append`, `pop()` (sans argument) et `raise Exception(…)` sont permis ; aucun opérateur sur les listes."

# ---------------------------------------------------------------- course

NOTIONS = [
    {"id": "bases", "titre": "Variables, opérateurs, conditions",
     "formule": r"`//` quotient entier · `%` reste · `/` division réelle · `**` puissance · `a, b = b, a` · `if … elif … else` · `and`, `or` paresseux · `==`, `!=`, `<`, `<=`",
     "exemple": r"`17 // 5` vaut `3`, `17 % 5` vaut `2`, `17 / 5` vaut `3.4`",
     "cours": r"Le bloc d'un `if`, d'une boucle ou d'une fonction est donné par l'indentation : un code non indenté n'est pas corrigé. `and` et `or` évaluent de gauche à droite et s'arrêtent dès que le résultat est connu : `i < n and L[i] != x` ne lit jamais `L[n]`. C'est la base de toutes les boucles de recherche."},
    {"id": "boucles", "titre": "Boucles `while` et `for … in range`",
     "formule": r"`range(n)` : $0..n-1$ · `range(a, b)` : $a..b-1$ · `range(a, b, p)` : pas $p$ · `while cond:` · chiffres : `n % 10` puis `n = n // 10`",
     "exemple": r"`for i in range(1, 10, 3):` donne `i` = 1, 4, 7",
     "cours": r"`for` sert quand on connaît le nombre de tours (parcours complet). `while` sert quand on peut s'arrêter avant la fin (recherche, propriété fausse) : la condition contient le test de fin de liste et le test d'arrêt. L'optimisation est notée à l'examen : une boucle qui continue alors que la réponse est connue coûte des points."},
    {"id": "fonctions", "titre": "Fonctions, `return`, paramètres",
     "formule": r"`def f(x, y):` · `return v` termine la fonction · sans `return` : `None` · une liste passée en paramètre est modifiée en place par `append`, `pop`, `L[i] = …` · `raise Exception(\"msg\")`",
     "exemple": r"`def f(L): L.append(0)` modifie la liste de l'appelant",
     "cours": r"La dernière fonction écrite doit être celle qui répond à la question ; les fonctions intermédiaires sont permises si on donne leur spécification. Une liste n'est jamais copiée par un appel ni par `B = A` : les deux noms désignent la même liste. En revanche `L = …` dans la fonction ne fait que changer ce que désigne le nom local."},
    {"id": "listes", "titre": "Listes : indices, `len`, `append`, `pop`",
     "formule": r"`L[0]` … `L[len(L) - 1]` · `L.append(x)` : ajoute à la fin · `L.pop()` : retire et renvoie le dernier · `L[i] = x` · couples : `(a, b) = L[i]`, `L.append((a, b))` · interdit : `+`, `*`, `==` entre listes, `in`, tranches, `min`, `max`, `sum`, `sort`",
     "exemple": r"`L = []` puis `for i in range(5): L.append(i)` donne `[0, 1, 2, 3, 4]`",
     "cours": r"À l'examen, l'annexe ne permet que `len`, `range`, `append`, `pop()` sans argument et `raise`. Tout le reste se réécrit avec des boucles : copier, renverser, chercher, supprimer. Supprimer l'élément d'indice $i$ : décaler `L[j] = L[j + 1]` pour $j$ de $i$ à la fin, puis `L.pop()`. Insérer : `L.append(…)` puis décaler vers la droite."},
    {"id": "parcours", "titre": "Parcours complet : somme, compte, extremum",
     "formule": r"accumulateur initialisé avant la boucle · `for e in L:` (valeurs) · `for i in range(len(L)):` (indices) · maximum : partir de `L[0]`, pas de $0$ · liste vide : `raise Exception(\"Empty list\")`",
     "exemple": r"`s = 0` puis `for e in L: s = s + e`",
     "cours": r"Un parcours complet visite chaque élément une fois. Pour un maximum ou un minimum, on part du premier élément (une liste de négatifs aurait $0$ pour faux maximum) ; une liste vide n'a pas d'extremum : exception. On peut calculer plusieurs résultats dans la même boucle (minimum et maximum)."},
    {"id": "recherche", "titre": "Recherche séquentielle, liste triée",
     "formule": r"`while i < n and L[i] != x: i += 1` · trouvé si `i < n` · liste croissante : `while i < n and L[i] < x`, puis tester `L[i] == x` · comparaisons comptées : une par élément visité",
     "exemple": r"chercher $40$ dans $\lambda$ ($13$ valeurs) : $13$ comparaisons sans l'ordre, $9$ avec l'ordre",
     "cours": r"Sans ordre, une recherche négative visite toute la liste. Dans une liste triée en ordre croissant, on s'arrête au premier élément $\ge x$ : $x$ est là ou nulle part. Le test `i < n` vient toujours en premier, grâce à `and` paresseux."},
    {"id": "dichotomie", "titre": "Recherche dichotomique",
     "formule": r"bornes incluses `left = 0`, `right = len(L) - 1` · `mid = (left + right) // 2` · `x == L[mid]` : trouvé · `x < L[mid]` : `right = mid - 1` · sinon `left = mid + 1` · arrêt quand les bornes sont égales ou se croisent · au pire $\lfloor\log_2 n\rfloor+1$ nœuds, $2$ comparaisons par nœud",
     "exemple": r"$n=32768=2^{15}$ : $16$ étapes, $2\times16=32$ comparaisons pour une recherche négative",
     "cours": r"Version du cours (arbre de décision du corrigé) : l'intervalle de recherche est `[left, right]`, chaque nœud de l'arbre est un intervalle et son milieu ; chaque étape compare $x$ à l'élément du milieu (égalité, puis infériorité) et garde une moitié. Le chemin de recherche est la suite des valeurs rencontrées : chaque valeur est une borne pour toutes les suivantes (si $42$ est plus petit que $50$, toutes les valeurs suivantes sont plus petites que $50$). Doubler la longueur ajoute une étape, donc deux comparaisons."},
    {"id": "construction", "titre": "Construire une liste",
     "formule": r"résultat `R = []` puis `R.append(…)` · chiffres de $n$ : `n % 10`, `n // 10` · nombre à partir des chiffres : `v = v * 10 + d` · groupes de valeurs égales : compteur remis à $1$ à chaque changement",
     "exemple": r"`int_to_list(1234, 6)` donne `[4, 3, 2, 1, 0, 0]`",
     "cours": r"On construit le résultat en avançant, avec `append`. Pour regrouper des valeurs consécutives égales (RLE, stock), on garde la valeur courante et son compteur ; on ajoute le groupe quand la valeur change, et on n'oublie pas le dernier groupe après la boucle (s'il existe)."},
    {"id": "en_place", "titre": "Modifier une liste en place",
     "formule": r"supprimer en $i$ : `for j in range(i, n - 1): L[j] = L[j + 1]` puis `L.pop()` · insérer : `L.append(x)` puis décaler vers la droite · renverser : échanger `L[i]` et `L[n - 1 - i]` pour $i < n // 2$",
     "exemple": r"`delete(L, 7)` sur `[1, 4, 5, 7, 8]` : `L` devient `[1, 4, 5, 8]`, renvoie `True`",
     "cours": r"La fonction ne renvoie pas de nouvelle liste : elle modifie celle de l'appelant et renvoie souvent un booléen (suppression faite ou non). Dans une liste triée, on cherche la place en s'arrêtant tôt, puis on décale une seule fois."},
    {"id": "couples", "titre": "Listes de couples",
     "formule": r"`(obj, q) = L[i]` · `for (obj, q) in L:` · un couple ne se modifie pas : `L[i] = (obj, q - r)` · `L.append((a, b))`",
     "exemple": r"stock `[('B', 4), ('M', 5)]` : objet `'B'`, quantité $4$",
     "cours": r"Un couple (tuple) se lit par déconstruction et se remplace en entier. Quand la liste est triée sur la première composante, la recherche d'un objet s'arrête au premier objet $\ge$ à celui cherché, comme pour une liste d'entiers."},
    {"id": "tris", "titre": "Tris : histogramme, sélection, fusion",
     "formule": r"histogramme : `H[e] += 1` · tri par comptage : `H[i]` fois la valeur $i$ · sélection : échanger `L[i]` et le minimum de `L[i:]` · fusion de deux listes triées : avancer dans celle qui a le plus petit élément, puis recopier le reste",
     "exemple": r"`hist([1, 3, 1])` donne `[0, 2, 0, 1, 0, 0, 0, 0, 0, 0]`",
     "cours": r"Le tri par comptage est linéaire mais ne sert que pour des petits entiers. Le tri par sélection fait $n(n-1)/2$ comparaisons. Le tri fusion coupe la liste en deux, trie chaque moitié récursivement et fusionne : $n\log_2 n$ comparaisons environ."},
]

# ---------------------------------------------------------------- shared model code

_SEARCH = '''def search(x, L):
    n = len(L)
    i = 0
    while i < n and L[i] != x:
        i = i + 1
    if i < n:
        return i
    else:
        return -1'''

_BIN = '''def binary_search(x, L):
    left = 0
    right = len(L) - 1
    while left <= right:
        mid = (left + right) // 2
        if x == L[mid]:
            return mid
        elif x < L[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1'''

_HIST = '''def hist(L):
    H = []
    for i in range(10):
        H.append(0)
    for e in L:
        H[e] += 1
    return H'''

_MERGE = '''def merge(L1, L2):
    R = []
    (i, j) = (0, 0)
    (n1, n2) = (len(L1), len(L2))
    while i < n1 and j < n2:
        if L1[i] <= L2[j]:
            R.append(L1[i])
            i += 1
        else:
            R.append(L2[j])
            j += 1
    while i < n1:
        R.append(L1[i])
        i += 1
    while j < n2:
        R.append(L2[j])
        j += 1
    return R'''

_GET = '''def get_stock(stock, obj, request):
    n = len(stock)
    i = 0
    while i < n and stock[i][0] < obj:
        i += 1
    if i == n or stock[i][0] != obj:
        return False
    (o, q) = stock[i]
    if q > request:
        stock[i] = (o, q - request)
        return True
    for j in range(i, n - 1):
        stock[j] = stock[j + 1]
    stock.pop()
    return False'''

_WHAT = '''def what(L):
    me = 0
    for e in L:
        if e > me:
            me = e
    X = []
    for i in range(me + 1):
        X.append(0)
    for e in L:
        X[e] += 1
    LT = []
    for i in range(me + 1):
        for j in range(X[i]):
            LT.append(i)
    return LT'''

LAMBDA = [1, 5, 7, 16, 21, 30, 33, 34, 42, 49, 72, 81, 99]
assert _steps(LAMBDA, 40)[0] == 4  # official answer: 8 = 2 x 4
assert _worst(16) == 5 and _worst(32768) == 16 and _worst(131071) == 17 and _worst(131072) == 18  # official: 32
assert [_path_ok(s, 42) for s in ([50, 15, 48, 22, 46, 42], [48, 15, 45, 22, 47, 42],
                                  [15, 22, 45, 43, 35, 42], [22, 45, 43, 15, 35, 42])] == [True, False, True, False]
_GA = [1, 1, 1, "s", "s", 2, 1, "s", "s", "s", 2, "s"]
_GB = [1, 2, "s", 2, "s", "s", "s", 1, 2, "s", 1, 2, "s", "s"]
assert _garage_ok(_GA) and not _garage_ok(_GB)

# ---------------------------------------------------------------- levels

LEVELS = [
    {"n": 1, "titre": "Bases : opérateurs, conditions, booléens", "notions": ["bases"], "exos": [
        pr("p11", "a = 17\nb = 5\nprint(a // b, a % b, a / b)", "3 2 3.4",
           r"`//` : quotient entier, `%` : reste ($17=5\times3+2$), `/` : division réelle.", duree=1),
        pr("p12", "x = 7\nif x % 2 == 0:\n    print(\"pair\")\nelif x > 5:\n    print(\"impair et grand\")\nelse:\n    print(\"impair\")",
           "impair et grand", r"Seule la première condition vraie est exécutée."),
        pr("p13", "a, b = 3, 8\na, b = b, a + b\nprint(a, b)", "8 11",
           r"Les deux valeurs de droite sont calculées avant l'affectation : `b, a + b` vaut `8, 11`."),
        pr("p14", "print(2 ** 10, -7 // 2, -7 % 2)", "1024 -4 1",
           r"`//` arrondit vers le bas : $-7=2\times(-4)+1$, et le reste est positif."),
        pr("p15", "L = []\nprint(len(L) > 0 and L[0] == 3)\nprint(len(L) == 0 or L[0] == 3)", "False\nTrue",
           r"`and` s'arrête sur `False`, `or` sur `True` : `L[0]` n'est jamais lu, donc pas d'`IndexError`."),
    ]},
    {"n": 2, "titre": "Boucles while et for", "notions": ["boucles", "bases"], "exos": [
        pr("p21", "for i in range(1, 10, 3):\n    print(i, end=\" \")", "1 4 7", r"De $1$ à $9$ par pas de $3$ ; $10$ est exclu.", duree=1),
        pr("p22", "n = 1234\ns = 0\nwhile n != 0:\n    s = s + n % 10\n    n = n // 10\nprint(s)", "10",
           r"`n % 10` est le dernier chiffre, `n // 10` l'enlève : $4+3+2+1$."),
        pr("p23", "c = 0\nfor i in range(4):\n    for j in range(i):\n        c += 1\nprint(c)", "6",
           r"$0+1+2+3$ tours de la boucle interne."),
        w("p24", r"Écrire la fonction `nb_digits(n)` qui renvoie le nombre de chiffres de l'entier $n\ge0$.",
          "def nb_digits(n):\n    c = 1\n    while n >= 10:\n        n = n // 10\n        c = c + 1\n    return c",
          [("nb_digits(0)", "1"), ("nb_digits(7)", "1"), ("nb_digits(2025)", "4")],
          r"On part de $1$ : $0$ a un chiffre. On enlève un chiffre tant qu'il en reste au moins deux.", duree=4),
        w("p25", r"Écrire la fonction `power(x, n)` qui renvoie $x^n$ ($n\ge0$) sans `**`.",
          "def power(x, n):\n    p = 1\n    for i in range(n):\n        p = p * x\n    return p",
          [("power(2, 10)", "1024"), ("power(5, 0)", "1"), ("power(-3, 3)", "-27")], duree=3),
    ]},
    {"n": 3, "titre": "Fonctions : return, None, paramètres", "notions": ["fonctions"], "exos": [
        pr("p31", "def f(x):\n    if x > 0:\n        return 1\n    return -1\n\nprint(f(3), f(0))", "1 -1",
           r"`return` termine la fonction : la ligne suivante n'est atteinte que si $x\le0$."),
        pr("p32", "def g(x):\n    x = x + 1\n\nprint(g(2))", "None", r"Sans `return`, une fonction renvoie `None`."),
        pr("p33", "def h(L):\n    L.append(4)\n    L = [0]\n    L.append(5)\n\nM = [1]\nh(M)\nprint(M)", "[1, 4]",
           r"`append(4)` modifie la liste de l'appelant ; `L = [0]` fait désigner une autre liste au nom local, `M` n'est plus touchée."),
        w("p34", r"Écrire la fonction `gcd(a, b)` (algorithme d'Euclide, $a, b\ge0$ non tous deux nuls).",
          "def gcd(a, b):\n    while b != 0:\n        (a, b) = (b, a % b)\n    return a",
          [("gcd(12, 18)", "6"), ("gcd(7, 0)", "7"), ("gcd(17, 5)", "1")], r"$\gcd(a,b)=\gcd(b, a \bmod b)$, et $\gcd(a,0)=a$.", duree=4),
        w("p35", r"Écrire la fonction `is_prime(n)` ($n\ge0$) qui s'arrête dès qu'un diviseur est trouvé.",
          "def is_prime(n):\n    if n < 2:\n        return False\n    d = 2\n    while d * d <= n and n % d != 0:\n        d = d + 1\n    return d * d > n",
          [("is_prime(1)", "False"), ("is_prime(2)", "True"), ("is_prime(91)", "False"), ("is_prime(97)", "True")],
          r"Un diviseur $d\ge2$ existe au plus tard pour $d\le\sqrt n$. La boucle s'arrête sur le premier diviseur.", duree=5),
    ]},
    {"n": 4, "titre": "Listes : indices, len, append, pop", "notions": ["listes"], "exos": [
        pr("p41", "L = []\nfor i in range(5):\n    L.append(i * i)\nprint(L, len(L), L[2])\nx = L.pop()\nprint(x, L)",
           "[0, 1, 4, 9, 16] 5 4\n16 [0, 1, 4, 9]", r"`pop()` retire et renvoie le dernier élément."),
        pr("p42", "A = [1, 2, 3]\nB = A\nB.append(4)\nprint(A)", "[1, 2, 3, 4]",
           r"`B = A` ne copie pas : `A` et `B` désignent la même liste."),
        pr("p43", "L = [(6, 'grr'), (4, 'z')]\n(first, second) = L[0]\nL.append((5, 'a'))\nprint(first, second, len(L))", "6 grr 3",
           r"Déconstruction d'un couple, comme dans l'annexe du partiel de janvier 2022.", src=P22),
        w("p44", r"Écrire `copy(L)` qui renvoie une nouvelle liste égale à `L`. " + RULE,
          "def copy(L):\n    R = []\n    for e in L:\n        R.append(e)\n    return R",
          [("A = [1, 2]", None), ("B = copy(A)", None), ("B.append(3)", None), ("A", "[1, 2]"), ("B", "[1, 2, 3]")],
          r"Sans tranche ni `list(…)`, on recopie élément par élément.", duree=3),
        w("p45", r"Écrire `reverse(L)` qui renvoie une nouvelle liste : `L` à l'envers. " + RULE,
          "def reverse(L):\n    R = []\n    for i in range(len(L) - 1, -1, -1):\n        R.append(L[i])\n    return R",
          [("reverse([1, 2, 3])", "[3, 2, 1]"), ("reverse([])", "[]")], r"On parcourt les indices de $n-1$ à $0$.", duree=4),
    ]},
    {"n": 5, "titre": "Parcours : somme, compte, minimum et maximum", "notions": ["parcours", "listes"], "exos": [
        w("p51", r"Écrire `sum_list(L)` : somme des éléments de `L`.", "def sum_list(L):\n    s = 0\n    for e in L:\n        s = s + e\n    return s",
          [("sum_list([3, 1, 4])", "8"), ("sum_list([])", "0")], duree=2),
        w("p52", r"Écrire `count(x, L)` : nombre d'occurrences de `x` dans `L`.",
          "def count(x, L):\n    c = 0\n    for e in L:\n        if e == x:\n            c = c + 1\n    return c",
          [("count(2, [2, 1, 2, 3])", "2"), ("count('z', ['a'])", "0")], duree=3),
        w("p53", r"Écrire `maximum(L)` : plus grand élément. Si `L` est vide, déclencher `Exception(\"Empty list\")`.",
          "def maximum(L):\n    if len(L) == 0:\n        raise Exception(\"Empty list\")\n    m = L[0]\n    for i in range(1, len(L)):\n        if L[i] > m:\n            m = L[i]\n    return m",
          [("maximum([-3, -1, -7])", "-1"), ("maximum([])", "Exception: Empty list")],
          r"On part de `L[0]` : avec $0$, `[-3, -1, -7]` donnerait un faux maximum.", duree=4),
        w("p54", r"Écrire `minimaxi(L)` qui renvoie le couple (minimum, maximum) de la liste non vide `L` en un seul parcours.",
          "def minimaxi(L):\n    (mini, maxi) = (L[0], L[0])\n    for e in L:\n        if e < mini:\n            mini = e\n        elif e > maxi:\n            maxi = e\n    return (mini, maxi)",
          [("minimaxi([5, 2, 9, 4])", "(2, 9)"), ("minimaxi([3])", "(3, 3)")],
          r"Un élément plus petit que le minimum ne peut pas dépasser le maximum : `elif` économise une comparaison.", src=P2022, duree=5),
    ]},
    {"n": 6, "titre": "Recherche séquentielle", "notions": ["recherche", "boucles"], "exos": [
        w("p61", r"Écrire `search(x, L)` : indice de la première occurrence de `x` dans `L`, $-1$ si absent. S'arrêter dès que `x` est trouvé.",
          _SEARCH, [("search(3, [1, 3, 5, 3])", "1"), ("search(4, [1, 3])", "-1"), ("search(1, [])", "-1")],
          r"`i < n` d'abord : `L[i]` n'est lu que si `i` est un indice valide.", duree=5),
        pr("p62", "def test(x, L):\n    i = len(L) - 1\n    while i >= 0 and L[i] != x:\n        i = i - 1\n    return i >= 0\n\nprint(test(3, [1, 3, 5]), test(4, [1, 3, 5]), test(1, []))",
           "True False False", r"`test(x, L)` vérifie si `x` est présent dans `L`, en partant de la fin.", src=P17, duree=3),
        w("p63", r"Écrire `search_sorted(x, L)` pour une liste triée en ordre croissant : `True` si `x` est présent. S'arrêter au premier élément $\ge x$.",
          "def search_sorted(x, L):\n    n = len(L)\n    i = 0\n    while i < n and L[i] < x:\n        i = i + 1\n    return i < n and L[i] == x",
          [("search_sorted(7, [1, 5, 7, 16])", "True"), ("search_sorted(6, [1, 5, 7, 16])", "False"), ("search_sorted(20, [1, 5, 7, 16])", "False")],
          r"Après la boucle, `L[i]` est le premier élément $\ge x$ (s'il existe) : `x` est là ou nulle part.", duree=5),
        v("p64", r"$\lambda = [1, 5, 7, 16, 21, 30, 33, 34, 42, 49, 72, 81, 99]$. On cherche $40$ par recherche séquentielle **sans** tenir compte de l'ordre : combien de comparaisons entre $40$ et un élément ?",
          "13", "13", r"Recherche négative sans ordre : tous les éléments sont comparés.", src=P19),
        v("p65", r"Même liste $\lambda$, même valeur $40$, recherche séquentielle **en tenant compte** de l'ordre : combien de comparaisons ?",
          "9", "9", r"On compare $1, 5, 7, 16, 21, 30, 33, 34$ puis $42 > 40$ : arrêt, $9$ comparaisons.", src=P19),
    ]},
    {"n": 7, "titre": "Vérifier une propriété : tri, progression, palindrome", "notions": ["recherche", "boucles"], "exos": [
        w("p71", r"Écrire `is_sorted(L)` : `L` est-elle triée en ordre croissant ? S'arrêter à la première paire mal rangée.",
          "def is_sorted(L):\n    i = 0\n    n = len(L)\n    while i < n - 1 and L[i] <= L[i + 1]:\n        i = i + 1\n    return i >= n - 1",
          [("is_sorted([1, 2, 2, 5])", "True"), ("is_sorted([1, 3, 2])", "False"), ("is_sorted([])", "True")],
          r"Corrigé officiel : `i >= n - 1` (et non `==`) gère aussi la liste vide.", src=P2022, duree=5),
        w("p72", r"Écrire `arithmetic(L)` : si `L` a au moins deux éléments et suit une progression arithmétique de raison non nulle, renvoyer la raison ; sinon $0$.",
          "def arithmetic(L):\n    n = len(L)\n    if n < 2:\n        return 0\n    r = L[1] - L[0]\n    i = 1\n    while i < n - 1 and L[i + 1] - L[i] == r:\n        i = i + 1\n    if i == n - 1:\n        return r\n    else:\n        return 0",
          [("arithmetic([1, 2, 3, 4, 5, 6, 7])", "1"), ("arithmetic([1, 1, 1, 1, 1])", "0"), ("arithmetic([12])", "0"), ("arithmetic([5, 8, 11, 14, 17])", "3"), ("arithmetic([1, 2, 4])", "0")],
          r"Raison nulle : la boucle va au bout et renvoie $r=0$, ce qui est la réponse demandée.", src=P19, duree=8),
        w("p73", r"Écrire `palindrome(L)` : `L` se lit-elle pareil dans les deux sens ?",
          "def palindrome(L):\n    i = 0\n    j = len(L) - 1\n    while i < j and L[i] == L[j]:\n        i = i + 1\n        j = j - 1\n    return i >= j",
          [("palindrome([1, 2, 1])", "True"), ("palindrome([1, 2, 2, 3])", "False"), ("palindrome([])", "True")],
          r"Deux indices qui se rapprochent ; arrêt à la première différence.", duree=5),
    ]},
    {"n": 8, "titre": "Recherche dichotomique", "notions": ["dichotomie"], "exos": [
        w("p81", r"Écrire `binary_search(x, L)` (liste croissante) : indice de `x` ou $-1$, avec la version du cours (bornes incluses).",
          _BIN, [("binary_search(42, [1, 5, 7, 16, 21, 30, 33, 34, 42, 49, 72, 81, 99])", "8"), ("binary_search(40, [1, 5, 7, 16])", "-1"), ("binary_search(3, [])", "-1")],
          r"À chaque étape l'intervalle `[left, right]` est divisé par deux ; arrêt quand les bornes se croisent.", duree=6),
        v("p82", r"Recherche dichotomique de $40$ dans $\lambda = [1, 5, 7, 16, 21, 30, 33, 34, 42, 49, 72, 81, 99]$ : combien de comparaisons d'éléments (2 par étape) ?",
          f"2*{_steps(LAMBDA, 40)[0]}", "8", r"Valeurs rencontrées : $33$ (indices 0 à 12), $49$ (7 à 12), $34$ (7 à 8), $42$ (bornes égales : arrêt). $4$ étapes, $8$ comparaisons (corrigé officiel : $8=2\times4$).", src=P19, duree=3),
        o("p83", r"Recherche dichotomique de $42$ dans des listes croissantes. Parmi ces suites de valeurs rencontrées, lesquelles sont possibles ?"
          "\n\n1. $50 - 15 - 48 - 22 - 46 - 42$\n2. $48 - 15 - 45 - 22 - 47 - 42$\n3. $15 - 22 - 45 - 43 - 35 - 42$\n4. $22 - 45 - 43 - 15 - 35 - 42$",
          r"**1 et 3** (corrigé officiel). Chaque valeur rencontrée borne toutes les suivantes du côté de $42$. En 2, après $45$ (et $42 < 45$) on ne peut plus rencontrer $47$. En 4, après $22$ (et $42 > 22$) on ne peut plus rencontrer $15$.",
          src=P19, duree=4),
        v("p84", r"Version du cours, liste de $1024$ éléments : nombre de comparaisons d'éléments au pire, pour une recherche négative ?",
          f"2*{_worst(1024)}", "22", r"$1024=2^{10}$ : $10+1=11$ nœuds au pire (comme l'arbre de $16=2^4$ éléments a $5$ niveaux), $2$ comparaisons chacun.", duree=3),
        v("p85", r"Même question pour une liste de $1000$ éléments.", f"2*{_worst(1000)}", "20",
          r"$2^9 \le 1000 < 2^{10}$ : $\lfloor\log_2 1000\rfloor+1=10$ étapes, $20$ comparaisons.", duree=3),
        w("p86", r"Écrire `first_index(x, L)` (liste croissante, valeurs répétées possibles) : indice de la **première** occurrence de `x`, $-1$ si absent, par dichotomie.",
          "def first_index(x, L):\n    left = 0\n    right = len(L)\n    while left < right:\n        mid = (left + right) // 2\n        if L[mid] < x:\n            left = mid + 1\n        else:\n            right = mid\n    if left < len(L) and L[left] == x:\n        return left\n    return -1",
          [("first_index(4, [1, 4, 4, 4, 9])", "1"), ("first_index(5, [1, 4, 9])", "-1"), ("first_index(9, [1, 4, 9])", "2")],
          r"On ne s'arrête pas sur une égalité : on continue à gauche (`right = mid`). À la fin, `left` est la place du premier élément $\ge x$.", duree=8),
    ]},
    {"n": 9, "titre": "Construire une liste", "notions": ["construction", "boucles"], "exos": [
        w("p91", r"Écrire `syracuse(n)` : liste des valeurs de la suite de Syracuse depuis $n$ jusqu'à $1$ (si $n$ pair : $n/2$, sinon $3n+1$). Si $n\le0$, renvoyer `[]`.",
          "def syracuse(n):\n    L = []\n    if n > 0:\n        L.append(n)\n        while n != 1:\n            if n % 2 == 0:\n                n = n // 2\n            else:\n                n = 3 * n + 1\n            L.append(n)\n    return L",
          [("syracuse(14)", "[14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]"), ("syracuse(1)", "[1]"), ("syracuse(0)", "[]")],
          src=P19, duree=6),
        w("p92", r"Écrire `int_to_list(n, p)` : liste des $p$ chiffres de l'entier $n$ ($n$ a au plus $p$ chiffres), des unités vers la gauche, complétée par des $0$.",
          "def int_to_list(n, p):\n    L = []\n    while p > 0:\n        L.append(n % 10)\n        n = n // 10\n        p -= 1\n    return L",
          [("int_to_list(1234, 6)", "[4, 3, 2, 1, 0, 0]"), ("int_to_list(0, 2)", "[0, 0]")],
          r"Corrigé officiel (version 2) : $p$ tours exactement, les $0$ viennent d'eux-mêmes.", src=P17, duree=5),
        w("p93", r"Écrire `list_to_ints(L)` : pour `L` $=[d_1, \dots, d_p]$, renvoyer le couple ($d_1d_2\dots d_p$, $d_p\dots d_2d_1$).",
          "def list_to_ints(L):\n    left = 0\n    right = 0\n    n = len(L)\n    for i in range(n):\n        left = left * 10 + L[i]\n        right = right * 10 + L[n - i - 1]\n    return (left, right)",
          [("list_to_ints([1, 2, 3])", "(123, 321)"), ("list_to_ints([0, 4])", "(4, 40)")], src=P17, duree=5),
        w("p94", r"Écrire `unique(L)` : à partir d'une liste triée, renvoyer une nouvelle liste sans doublon.",
          "def unique(L):\n    R = []\n    for e in L:\n        if len(R) == 0 or R[len(R) - 1] != e:\n            R.append(e)\n    return R",
          [("unique([1, 1, 2, 5, 5, 5])", "[1, 2, 5]"), ("unique([])", "[]")],
          r"Liste triée : un doublon est forcément égal au dernier élément ajouté.", duree=5),
    ]},
    {"n": 10, "titre": "Modifier une liste en place", "notions": ["en_place", "recherche"], "exos": [
        w("p101", r"Écrire `delete(L, x)` qui supprime la valeur `x`, si elle existe, de la liste `L` strictement croissante, et renvoie un booléen (suppression faite ou non). " + RULE,
          "def delete(L, x):\n    n = len(L)\n    i = 0\n    while i < n and L[i] < x:\n        i += 1\n    if i == n or L[i] != x:\n        return False\n    for j in range(i, n - 1):\n        L[j] = L[j + 1]\n    L.pop()\n    return True",
          [("L = [1, 4, 5, 7, 8, 12, 15]", None), ("delete(L, 7)", "True"), ("L", "[1, 4, 5, 8, 12, 15]"), ("delete(L, 11)", "False"), ("L", "[1, 4, 5, 8, 12, 15]")],
          r"Recherche qui s'arrête au premier élément $\ge x$, puis décalage vers la gauche et `pop()`.", src=P19, duree=8),
        w("p102", r"Écrire `insert(L, x)` qui insère `x` à sa place dans la liste croissante `L` (en place).",
          "def insert(L, x):\n    L.append(x)\n    i = len(L) - 1\n    while i > 0 and L[i - 1] > x:\n        L[i] = L[i - 1]\n        i = i - 1\n    L[i] = x",
          [("L = [1, 4, 9]", None), ("insert(L, 5)", None), ("L", "[1, 4, 5, 9]"), ("insert(L, 0)", None), ("L", "[0, 1, 4, 5, 9]")],
          r"`append` agrandit la liste, puis on décale vers la droite tant que l'élément précédent est plus grand.", duree=6),
        w("p103", r"Écrire `reverse_in_place(L)` qui renverse `L` sans créer de liste.",
          "def reverse_in_place(L):\n    n = len(L)\n    for i in range(n // 2):\n        (L[i], L[n - 1 - i]) = (L[n - 1 - i], L[i])",
          [("L = [1, 2, 3, 4, 5]", None), ("reverse_in_place(L)", None), ("L", "[5, 4, 3, 2, 1]")],
          r"Seulement $n/2$ échanges : au-delà, on remettrait les éléments en place.", duree=5),
        w("p104", r"Écrire `remove_all(L, x)` qui retire toutes les occurrences de `x` de `L` (en place, en un parcours) et renvoie leur nombre.",
          "def remove_all(L, x):\n    k = 0\n    for i in range(len(L)):\n        if L[i] != x:\n            L[k] = L[i]\n            k = k + 1\n    c = len(L) - k\n    for j in range(c):\n        L.pop()\n    return c",
          [("L = [3, 1, 3, 3, 2]", None), ("remove_all(L, 3)", "3"), ("L", "[1, 2]")],
          r"`k` est la place du prochain élément gardé ; à la fin on retire les `len(L) - k` cases en trop.", duree=8),
    ]},
    {"n": 11, "titre": "Listes de couples", "notions": ["couples", "recherche"], "exos": [
        pr("p111", "stock = [('B', 4), ('M', 5), ('O', 1)]\nt = 0\nfor (obj, q) in stock:\n    t = t + q\nprint(t, stock[1][0])", "10 M",
           r"`stock[1]` est le couple `('M', 5)`, `stock[1][0]` sa première composante.", src=B25),
        w("p112", r"Un stock est une liste de couples (objet, quantité) triée par objets croissants. Écrire `quantity(stock, obj)` : quantité de `obj`, $0$ s'il est absent. S'arrêter dès que possible.",
          "def quantity(stock, obj):\n    n = len(stock)\n    i = 0\n    while i < n and stock[i][0] < obj:\n        i += 1\n    if i < n and stock[i][0] == obj:\n        return stock[i][1]\n    return 0",
          [("quantity([('B', 4), ('M', 5), ('O', 1)], 'M')", "5"), ("quantity([('B', 4), ('M', 5)], 'C')", "0")], src=B25, duree=5),
        w("p113", r"Écrire `unzip(L)` : à partir d'une liste de couples, renvoyer le couple de listes (premières composantes, secondes composantes).",
          "def unzip(L):\n    (A, B) = ([], [])\n    for (a, b) in L:\n        A.append(a)\n        B.append(b)\n    return (A, B)",
          [("unzip([(1, 'a'), (2, 'b')])", "([1, 2], ['a', 'b'])"), ("unzip([])", "([], [])")], duree=3),
        w("p114", r"Écrire `add(stock, obj, q)` : ajoute $q > 0$ unités de `obj` au stock trié (met à jour la quantité ou insère le couple à sa place).",
          "def add(stock, obj, q):\n    n = len(stock)\n    i = 0\n    while i < n and stock[i][0] < obj:\n        i += 1\n    if i < n and stock[i][0] == obj:\n        stock[i] = (obj, stock[i][1] + q)\n    else:\n        stock.append((obj, q))\n        for j in range(n, i, -1):\n            stock[j] = stock[j - 1]\n        stock[i] = (obj, q)",
          [("s = [('B', 4), ('O', 1)]", None), ("add(s, 'B', 2)", None), ("s", "[('B', 6), ('O', 1)]"), ("add(s, 'M', 5)", None), ("s", "[('B', 6), ('M', 5), ('O', 1)]")],
          r"Un couple ne se modifie pas : on le remplace. Insertion : `append` puis décalage vers la droite.", src=B25, duree=8),
    ]},
    {"n": 12, "titre": "Tris : histogramme, sélection, fusion", "notions": ["tris", "construction"], "exos": [
        w("p121", r"Écrire `hist(L)` : `L` ne contient que des chiffres ; renvoyer la liste `H` de longueur $10$ où `H[i]` est le nombre de `i` dans `L`.",
          _HIST, [("hist([1, 3, 1])", "[0, 2, 0, 1, 0, 0, 0, 0, 0, 0]")], src=P17, duree=4),
        w("p122", r"Écrire `sort(L)` : liste de chiffres `L` triée en ordre croissant, à l'aide de `hist`.",
          _HIST + "\n\ndef sort(L):\n    H = hist(L)\n    R = []\n    for i in range(10):\n        for nb in range(H[i]):\n            R.append(i)\n    return R",
          [("sort([3, 1, 4, 1, 5, 9, 2, 6])", "[1, 1, 2, 3, 4, 5, 6, 9]")], r"Tri par comptage : linéaire.", src=P17, duree=5),
        pr("p123", _WHAT + "\n\nprint(what([1, 3, 2, 8, 7, 2, 5, 4, 0, 6, 2, 15]))", "[0, 1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 15]",
           r"`me` est le maximum, `X` l'histogramme des valeurs : `what` renvoie une copie de `L` triée (tri par comptage). Complexité $3n+$`me`.",
           enonce="Qu'affiche ce programme ? Que fait `what(L)` pour une liste d'entiers naturels ?", src=P19, duree=6),
        w("p124", r"Écrire `select_sort(L)` : tri par sélection en place (ordre croissant).",
          "def select_sort(L):\n    n = len(L)\n    for i in range(n - 1):\n        m = i\n        for j in range(i + 1, n):\n            if L[j] < L[m]:\n                m = j\n        (L[i], L[m]) = (L[m], L[i])",
          [("L = [5, 3, 8, 1, 4]", None), ("select_sort(L)", None), ("L", "[1, 3, 4, 5, 8]")],
          r"À l'étape $i$, on place le minimum de `L[i…n-1]` en position $i$.", duree=7),
        w("p125", r"Écrire `merge(L1, L2)` : fusion de deux listes croissantes en une nouvelle liste croissante.",
          _MERGE, [("merge([1, 4, 9], [2, 3, 10, 12])", "[1, 2, 3, 4, 9, 10, 12]"), ("merge([], [5])", "[5]")],
          r"Quand une liste est épuisée, on recopie le reste de l'autre.", duree=7),
        w("p126", r"Écrire `merge_sort(L)` (tri fusion, renvoie une nouvelle liste), en utilisant `merge`.",
          _MERGE + "\n\ndef merge_sort(L):\n    n = len(L)\n    if n <= 1:\n        return L\n    (A, B) = ([], [])\n    for i in range(n // 2):\n        A.append(L[i])\n    for i in range(n // 2, n):\n        B.append(L[i])\n    return merge(merge_sort(A), merge_sort(B))",
          [("merge_sort([5, 3, 8, 1, 4, 2])", "[1, 2, 3, 4, 5, 8]"), ("merge_sort([])", "[]")],
          r"Couper en deux (sans tranche : deux boucles), trier chaque moitié, fusionner.", src=P2022, duree=10),
    ]},
    {"n": 13, "titre": "Niveau examen : partiel P1 du 18 janvier 2021", "notions": ["dichotomie", "recherche", "tris", "construction"], "examen": True, "exos": [
        o("p131", r"Exercice 1 (Double garage, 3 points). Un garage a deux entrées $e_1$, $e_2$ et une seule sortie $s$ ; une voiture ne peut ressortir que si elle est la dernière entrée (peu importe l'entrée). Le garage est vide au départ et à la fin. Ces séquences sont-elles valides ?"
          "\n\n(a) $(v_1,e_1), (v_2,e_1), (v_3,e_1), s, s, (v_4,e_2), (v_5,e_1), s, s, s, (v_6,e_2), s$\n\n(b) $(v_1,e_1), (v_2,e_2), s, (v_3,e_2), s, s, s, (v_4,e_1), (v_5,e_2), s, (v_6,e_1), (v_7,e_2), s, s$\n\nDonner une règle générale.",
          r"Le garage est une pile : les deux entrées mènent au même sommet. (a) **valide** (nombre de voitures : 3, 1, 3, 0, 1, 0). (b) **non valide** : au 7e mouvement, $s$ alors que le garage est vide ($v_1, v_2, v_3$ sont déjà sorties). Règle : dans tout début de séquence, le nombre de $s$ est $\le$ au nombre d'entrées, et il y a autant de $s$ que d'entrées au total.",
          src=P21, duree=6),
        v("p132", r"Exercice 2 (Dichotomie). Version du cours (arrêt quand les bornes se croisent ou sont égales). Liste de $32768$ éléments triés : nombre de comparaisons d'éléments au pire, pour une recherche négative ?",
          f"2*{_worst(32768)}", "32", r"$32768=2^{15}$ : $16$ étapes, $2\times(15+1)=32$ (corrigé officiel).", src=P21, duree=3),
        v("p133", r"Soit $k$ la réponse précédente. Longueur maximale d'une liste qui génère $k+2$ comparaisons lors d'une recherche négative ?",
          f"2**{_worst(131071)} - 1", "131071",
          r"$k+2=34$ comparaisons : $17$ niveaux dans l'arbre. Un arbre à $17$ niveaux couvre jusqu'à $2^{17}-1=131071$ éléments ($2^{17}$ en demande $18$). Le corrigé officiel répond $65536$ ($32768\times2$) : cette longueur donne bien $34$ comparaisons, mais ce n'est pas le maximum.",
          src=P21, duree=4),
        w("p134", r"Exercice 3 (3,5 points). Écrire `search_indexes(L, val)` : couple (premier indice, dernier indice) de `val` dans la liste croissante `L`, `(-1, -1)` si absent.",
          "def search_indexes(L, val):\n    n = len(L)\n    i = 0\n    while i < n and L[i] < val:\n        i += 1\n    if i == n or L[i] != val:\n        return (-1, -1)\n    j = i\n    while j < n - 1 and L[j + 1] == val:\n        j += 1\n    return (i, j)",
          [("search_indexes([1, 4, 12, 12, 42], 4)", "(1, 1)"), ("search_indexes([1, 4, 12, 12, 42], 15)", "(-1, -1)"),
           ("search_indexes([1, 4, 12, 12, 42], 12)", "(2, 3)"), ("search_indexes([4, 4, 4], 4)", "(0, 2)")],
          r"Liste triée : arrêt au premier élément $\ge$ `val`, puis on avance tant que l'élément suivant vaut `val`.", src=P21, duree=10),
        w("p135", r"Exercice 4 (4,5 points). Écrire `consecutive_sum(L, S)` ($S>0$, `L` d'entiers $\ge0$) : existe-t-il des éléments consécutifs de `L` de somme $S$ ?",
          "def consecutive_sum(L, S):\n    n = len(L)\n    (i, s) = (0, 0)\n    j = 0\n    while j < n and s != S:\n        s = s + L[j]\n        j += 1\n        while s > S:\n            s = s - L[i]\n            i += 1\n    return s == S",
          [("consecutive_sum([3, 1, 4, 2, 4], 10)", "True"), ("consecutive_sum([3, 7, 6], 6)", "True"),
           ("consecutive_sum([], 6)", "False"), ("consecutive_sum([3, 7, 6], 9)", "False")],
          r"Fenêtre glissante `L[i…j-1]` de somme `s` : on ajoute à droite, on retire à gauche tant que `s > S`. Valeurs $\ge0$ : chaque élément entre et sort au plus une fois, d'où un coût linéaire.", src=P21, duree=12),
        w("p136", r"Exercice 5 (6 points). Écrire `separate(L1, L2, n)` : `L1`, `L2` croissantes ; renvoyer le couple de listes croissantes (éléments $< n$, éléments $\ge n$) des deux listes.",
          "def separate(L1, L2, n):\n    (A, B) = ([], [])\n    (i, j) = (0, 0)\n    (n1, n2) = (len(L1), len(L2))\n    while i < n1 or j < n2:\n        if j == n2 or (i < n1 and L1[i] <= L2[j]):\n            e = L1[i]\n            i += 1\n        else:\n            e = L2[j]\n            j += 1\n        if e < n:\n            A.append(e)\n        else:\n            B.append(e)\n    return (A, B)",
          [("separate([1, 3, 12, 31, 42], [5, 16, 28], 12)", "([1, 3, 5], [12, 16, 28, 31, 42])"),
           ("separate([1, 3, 12, 31, 42], [5, 16, 28], 42)", "([1, 3, 5, 12, 16, 28, 31], [42])"),
           ("separate([1, 2, 3], [2, 5, 12, 42], 1)", "([], [1, 2, 2, 3, 5, 12, 42])"),
           ("separate([], [2, 5, 12, 42], 6)", "([2, 5], [12, 42])")],
          r"Une fusion : on prend toujours le plus petit des deux éléments courants, et on l'envoie dans la bonne liste. Les deux résultats sont croissants d'eux-mêmes.", src=P21, duree=15),
    ]},
    {"n": 14, "titre": "Niveau examen : partiel P1 du 4 janvier 2022", "notions": ["recherche", "en_place", "construction", "couples"], "examen": True, "exos": [
        w("p141", r"Exercice 1 (Colline, 4 points). Une liste non vide est une colline si elle est une suite (éventuellement vide) strictement croissante suivie d'une suite (éventuellement vide) strictement décroissante. Écrire `hill(L)` (entiers $\ge0$) : le point culminant si `L` est une colline, $-1$ sinon ; exception si `L` est vide.",
          "def hill(L):\n    if len(L) == 0:\n        raise Exception(\"Empty list\")\n    i = 0\n    n = len(L)\n    while i < n - 1 and L[i] < L[i + 1]:\n        i = i + 1\n    top = L[i]\n    i = i + 1\n    while i < n - 1 and L[i] > L[i + 1]:\n        i = i + 1\n    if i >= n - 1:\n        return top\n    else:\n        return -1",
          [("hill([1, 4, 8, 12, 12, 5, 2])", "12"), ("hill([12, 25, 40, 52])", "52"), ("hill([15, 8, 3])", "15"),
           ("hill([1, 5, 10, 8, 6, 12])", "-1"), ("hill([15, 12, 11, 9, 10, 14, 16])", "-1"), ("hill([])", "Exception: Empty list")],
          r"Corrigé officiel. On monte tant que c'est strictement croissant, on note le sommet, on saute un élément (le sommet ou son égal : `12, 12` est accepté par l'énoncé) puis on descend. Colline si on atteint la fin.", src=P22, duree=10),
        w("p142", r"Exercice 2 (4 points). Écrire `delete(L, x)` qui supprime `x`, s'il existe, de la liste `L` **strictement décroissante** et renvoie un booléen.",
          "def delete(L, x):\n    n = len(L)\n    i = 0\n    while i < n and x < L[i]:\n        i += 1\n    if i == n or L[i] != x:\n        return False\n    else:\n        for j in range(i, n - 1):\n            L[j] = L[j + 1]\n        L.pop()\n        return True",
          [("L = [12, 8, 5, 4, -3, -7]", None), ("delete(L, 5)", "True"), ("L", "[12, 8, 4, -3, -7]"), ("delete(L, 12)", "True"),
           ("L", "[8, 4, -3, -7]"), ("delete(L, 1)", "False"), ("L", "[8, 4, -3, -7]")],
          r"Corrigé officiel : comme pour une liste croissante, avec le test `x < L[i]`.", src=P22, duree=8),
        w("p143", r"Exercice 3.1 (RLE). Un flux encodé est une liste de couples (nombre non nul d'éléments consécutifs identiques, élément). Écrire `decodeRLE(L)`.",
          "def decodeRLE(L):\n    R = []\n    for (n, val) in L:\n        for _ in range(n):\n            R.append(val)\n    return R",
          [("decodeRLE([(6, 'grr')])", "['grr', 'grr', 'grr', 'grr', 'grr', 'grr']"),
           ("decodeRLE([(5, 'a'), (1, 'b'), (3, 'c'), (2, 'd'), (1, 'e')])", "['a', 'a', 'a', 'a', 'a', 'b', 'c', 'c', 'c', 'd', 'd', 'e']")],
          src=P22, duree=5),
        w("p144", r"Exercice 3.2 (RLE). Écrire `encodeRLE(L)` qui compresse une liste.",
          "def encodeRLE(L):\n    R = []\n    if len(L) > 0:\n        (nb, val) = (1, L[0])\n        for i in range(1, len(L)):\n            if L[i] == val:\n                nb += 1\n            else:\n                R.append((nb, val))\n                (nb, val) = (1, L[i])\n        R.append((nb, val))\n    return R",
          [("encodeRLE(['grr', 'grr', 'grr', 'grr', 'grr', 'grr'])", "[(6, 'grr')]"),
           ("encodeRLE(['a', 'a', 'a', 'a', 'a', 'b', 'c', 'c', 'c', 'd', 'd', 'e'])", "[(5, 'a'), (1, 'b'), (3, 'c'), (2, 'd'), (1, 'e')]"),
           ("encodeRLE([])", "[]")],
          r"Corrigé officiel : le dernier groupe est ajouté après la boucle, seulement si la liste n'est pas vide.", src=P22, duree=10),
    ]},
    {"n": 15, "titre": "Niveau examen : examen B2 du 7 janvier 2025", "notions": ["couples", "en_place", "construction", "recherche"], "examen": True, "exos": [
        w("p151", r"Un stock est une liste de couples (objet, quantité $>0$) triée par objets croissants, sans doublon. Exercice 1 (4 points). Écrire `check_stock(stock, capacity)` : le stock contient-il au plus `capacity` objets (somme des quantités) ? " + RULE,
          "def check_stock(stock, capacity):\n    total = 0\n    i = 0\n    n = len(stock)\n    while i < n and total <= capacity:\n        total = total + stock[i][1]\n        i += 1\n    return total <= capacity",
          [("check_stock([], 0)", "True"), ("check_stock([('B', 4), ('M', 5), ('O', 1)], 10)", "True"), ("check_stock([('B', 4), ('M', 5), ('O', 1)], 9)", "False")],
          r"L'optimisation est notée : on s'arrête dès que la capacité est dépassée (quantités positives, le total ne peut que croître).", src=B25, duree=8),
        w("p152", r"Exercice 2 (6 points). Écrire `build_stock(L)` : `L` est une liste d'objets triée ; construire et renvoyer le stock valide correspondant.",
          "def build_stock(L):\n    stock = []\n    n = len(L)\n    i = 0\n    while i < n:\n        obj = L[i]\n        q = 0\n        while i < n and L[i] == obj:\n            q += 1\n            i += 1\n        stock.append((obj, q))\n    return stock",
          [("build_stock([])", "[]"), ("build_stock(['A', 'A', 'A', 'D', 'O', 'O'])", "[('A', 3), ('D', 1), ('O', 2)]"), ("build_stock(['C', 'C', 'C', 'C'])", "[('C', 4)]")],
          r"Pour chaque groupe d'objets égaux consécutifs (la liste est triée), on compte puis on ajoute le couple.", src=B25, duree=10),
        w("p153", r"Exercice 3.1 (Get). Écrire `get_stock(stock, obj, request)` ($request>0$) : retire `request` unités de `obj` s'il est présent ; si la quantité est $\le$ `request`, l'objet est supprimé du stock. Renvoie `True` si `obj` est encore dans le stock après modification.",
          _GET,
          [("get_stock([], 'Y', 24)", "False"), ("stock = [('B', 4), ('M', 5), ('O', 1), ('Z', 10)]", None),
           ("get_stock(stock, 'Y', 24)", "False"), ("stock", "[('B', 4), ('M', 5), ('O', 1), ('Z', 10)]"),
           ("get_stock(stock, 'M', 3)", "True"), ("stock", "[('B', 4), ('M', 2), ('O', 1), ('Z', 10)]"),
           ("get_stock(stock, 'O', 5)", "False"), ("stock", "[('B', 4), ('M', 2), ('Z', 10)]"),
           ("get_stock(stock, 'B', 4)", "False"), ("stock", "[('M', 2), ('Z', 10)]")],
          r"Recherche qui s'arrête au premier objet $\ge$ `obj` ; mise à jour en remplaçant le couple ; suppression par décalage puis `pop()`.", src=B25, duree=12),
        w("p154", r"Exercice 3.2. Écrire `shopping(stock, requests)` : pour chaque couple (obj, request) de `requests`, retire les unités tant que c'est possible ; renvoie `False` dès qu'un objet était absent ou a été supprimé du stock, `True` sinon. Utiliser `get_stock`.",
          _GET + "\n\ndef shopping(stock, requests):\n    i = 0\n    n = len(requests)\n    while i < n:\n        (obj, request) = requests[i]\n        if not get_stock(stock, obj, request):\n            return False\n        i += 1\n    return True",
          [("stock = [('B', 4), ('M', 5), ('O', 1)]", None), ("shopping(stock, [])", "True"),
           ("shopping(stock, [('M', 1)])", "True"), ("stock", "[('B', 4), ('M', 4), ('O', 1)]"),
           ("shopping(stock, [('B', 1), ('M', 1), ('M', 1)])", "True"), ("stock", "[('B', 3), ('M', 2), ('O', 1)]"),
           ("shopping(stock, [('M', 4), ('B', 1), ('O', 2)])", "False"), ("stock", "[('B', 3), ('O', 1)]"),
           ("shopping(stock, [('Z', 4)])", "False"), ("stock", "[('B', 3), ('O', 1)]")],
          r"Les exemples montrent qu'on s'arrête à la première requête qui échoue : `('B', 1)` et `('O', 2)` ne sont pas traitées après la suppression de `'M'`.", src=B25, duree=8),
    ]},
]

VARIANTS = {
    "p11": [prv("print(23 // 4, 23 % 4, 23 / 4)", "5 3 5.75", r"$23=4\times5+3$.")],
    "p13": [prv("a, b = 2, 5\na, b = b - a, a\nprint(a, b)", "3 2", r"`b - a, a` vaut `3, 2`.")],
    "p22": [prv("n = 507\nc = 0\nwhile n != 0:\n    n = n // 10\n    c = c + 1\nprint(c)", "3", r"Trois chiffres enlevés.")],
    "p23": [prv("c = 0\nfor i in range(3):\n    for j in range(i, 3):\n        c += 1\nprint(c)", "6", r"$3+2+1$.")],
    "p42": [prv("A = [1]\nB = A\nA.append(2)\nB.pop()\nprint(A, B)", "[1] [1]", r"Une seule liste, deux noms.")],
    "p51": [wv(r"Écrire `nb_even(L)` : nombre d'éléments pairs.", "def nb_even(L):\n    c = 0\n    for e in L:\n        if e % 2 == 0:\n            c = c + 1\n    return c",
               [("nb_even([1, 2, 4, 7])", "2"), ("nb_even([])", "0")])],
    "p53": [wv(r"Écrire `minimum(L)`, avec `Exception(\"Empty list\")` si `L` est vide.",
               "def minimum(L):\n    if len(L) == 0:\n        raise Exception(\"Empty list\")\n    m = L[0]\n    for e in L:\n        if e < m:\n            m = e\n    return m",
               [("minimum([4, 2, 9])", "2"), ("minimum([])", "Exception: Empty list")])],
    "p61": [wv(r"Écrire `last_index(x, L)` : indice de la dernière occurrence de `x`, $-1$ si absent ; partir de la fin.",
               "def last_index(x, L):\n    i = len(L) - 1\n    while i >= 0 and L[i] != x:\n        i = i - 1\n    return i",
               [("last_index(3, [1, 3, 5, 3])", "3"), ("last_index(4, [1, 3])", "-1")], r"Si `x` est absent, la boucle s'arrête à $-1$.")],
    "p65": [{"enonce": r"Même liste $\lambda$, recherche séquentielle en tenant compte de l'ordre de la valeur $80$ : combien de comparaisons ?",
             "calc": "12", "ans": "12", "sol": r"$1, 5, \dots, 72$ (11 valeurs) puis $81 > 80$ : $12$."}],
    "p82": [{"enonce": r"Recherche dichotomique de $80$ dans $\lambda$ : combien de comparaisons d'éléments (2 par étape) ?",
             "calc": f"2*{_steps(LAMBDA, 80)[0]}", "ans": "8", "sol": r"Valeurs rencontrées : $33, 49, 81, 72$ (bornes égales) : $4$ étapes, $8$ comparaisons."}],
    "p84": [{"enonce": r"Version du cours, liste de $4096$ éléments : comparaisons au pire pour une recherche négative ?",
             "calc": f"2*{_worst(4096)}", "ans": "26", "sol": r"$4096=2^{12}$ : $13$ étapes, $26$ comparaisons."}],
    "p91": [wv(r"Écrire `divisors(n)` ($n\ge1$) : liste croissante des diviseurs de $n$.",
               "def divisors(n):\n    L = []\n    for d in range(1, n + 1):\n        if n % d == 0:\n            L.append(d)\n    return L",
               [("divisors(12)", "[1, 2, 3, 4, 6, 12]"), ("divisors(1)", "[1]")])],
    "p101": [wv(r"Écrire `delete_index(L, i)` : supprime l'élément d'indice `i` (valide) de `L`, en place.",
                "def delete_index(L, i):\n    for j in range(i, len(L) - 1):\n        L[j] = L[j + 1]\n    L.pop()",
                [("L = [5, 6, 7, 8]", None), ("delete_index(L, 1)", None), ("L", "[5, 7, 8]")])],
    "p124": [wv(r"Écrire `insertion_sort(L)` : tri par insertion en place.",
                "def insertion_sort(L):\n    for i in range(1, len(L)):\n        x = L[i]\n        j = i\n        while j > 0 and L[j - 1] > x:\n            L[j] = L[j - 1]\n            j = j - 1\n        L[j] = x",
                [("L = [5, 3, 8, 1]", None), ("insertion_sort(L)", None), ("L", "[1, 3, 5, 8]")])],
}
assert _steps(LAMBDA, 40)[1] == [33, 49, 34, 42] and _steps(LAMBDA, 80)[1] == [33, 49, 81, 72]
for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["id"] in VARIANTS:
            _e["variants"] = VARIANTS[_e["id"]]

EXTRA_PARTS = []

QUIZ = [
    {"notion": "bases", "type": "qcm", "q": r"`17 // 5` vaut :", "choix": [r"`3`", r"`3.4`", r"`2`", r"`4`"], "bonne": 0},
    {"notion": "bases", "type": "vf", "q": r"`i < n and L[i] != x` peut déclencher `IndexError` quand `i == n`.", "bonne": False},
    {"notion": "boucles", "type": "qcm", "q": r"`range(2, 8, 2)` donne :", "choix": [r"`2, 4, 6`", r"`2, 4, 6, 8`", r"`2, 3, …, 7`", r"`4, 6, 8`"], "bonne": 0},
    {"notion": "boucles", "type": "vf", "q": r"Pour une recherche qui peut s'arrêter avant la fin, on préfère `while` à `for`.", "bonne": True},
    {"notion": "fonctions", "type": "qcm", "q": r"Une fonction sans `return` renvoie :", "choix": [r"`None`", r"`0`", r"`False`", r"une erreur"], "bonne": 0},
    {"notion": "fonctions", "type": "vf", "q": r"`B = A` crée une copie de la liste `A`.", "bonne": False},
    {"notion": "listes", "type": "qcm", "q": r"À l'examen, lequel est permis sur les listes ?", "choix": [r"`L.pop()`", r"`L + [x]`", r"`x in L`", r"`L[1:3]`"], "bonne": 0},
    {"notion": "listes", "type": "vf", "q": r"`L.pop()` retire et renvoie le premier élément.", "bonne": False},
    {"notion": "parcours", "type": "qcm", "q": r"Pour chercher le maximum d'une liste non vide, on initialise avec :", "choix": [r"`L[0]`", r"`0`", r"`-1`", r"`len(L)`"], "bonne": 0},
    {"notion": "parcours", "type": "vf", "q": r"Le maximum d'une liste vide doit déclencher une exception.", "bonne": True},
    {"notion": "recherche", "type": "qcm", "q": r"Recherche séquentielle de $x$ dans une liste croissante : on s'arrête au premier élément :", "choix": [r"$\ge x$", r"$> x$ seulement", r"$= x$ seulement", r"on ne s'arrête jamais"], "bonne": 0},
    {"notion": "recherche", "type": "vf", "q": r"Sans tenir compte de l'ordre, une recherche négative compare $x$ à tous les éléments.", "bonne": True},
    {"notion": "dichotomie", "type": "qcm", "q": r"Recherche négative dans $32768$ éléments (version du cours) : comparaisons au pire ?", "choix": [r"$32$", r"$15$", r"$16$", r"$30$"], "bonne": 0},
    {"notion": "dichotomie", "type": "vf", "q": r"Doubler la longueur de la liste double le nombre de comparaisons de la dichotomie.", "bonne": False},
    {"notion": "construction", "type": "qcm", "q": r"`v = v * 10 + d` pour `d` dans `[1, 2, 3]`, en partant de `v = 0`, donne :", "choix": [r"`123`", r"`321`", r"`6`", r"`60`"], "bonne": 0},
    {"notion": "construction", "type": "vf", "q": r"En codage RLE, le dernier groupe doit être ajouté après la boucle.", "bonne": True},
    {"notion": "en_place", "type": "qcm", "q": r"Pour supprimer l'élément d'indice $i$ avec seulement `pop()` :", "choix": [r"décaler `L[j] = L[j + 1]` puis `pop()`", r"`L.pop(i)`", r"`del L[i]`", r"`L = L[:i]`"], "bonne": 0},
    {"notion": "en_place", "type": "vf", "q": r"Renverser une liste en place demande $n$ échanges.", "bonne": False},
    {"notion": "couples", "type": "qcm", "q": r"Pour retirer $3$ unités du couple `stock[i] = ('M', 5)` :", "choix": [r"`stock[i] = ('M', 2)`", r"`stock[i][1] -= 3`", r"`stock[i][1] = 2`", r"`stock.pop(i)`"], "bonne": 0},
    {"notion": "couples", "type": "vf", "q": r"Un couple (tuple) se modifie composante par composante.", "bonne": False},
    {"notion": "tris", "type": "qcm", "q": r"Fusionner `[1, 4]` et `[2, 3]` donne :", "choix": [r"`[1, 2, 3, 4]`", r"`[1, 4, 2, 3]`", r"`[2, 3, 1, 4]`", r"`[1, 2, 4, 3]`"], "bonne": 0},
    {"notion": "tris", "type": "vf", "q": r"Le tri par comptage (histogramme) convient pour n'importe quelles valeurs réelles.", "bonne": False},
]

_FL = {
    1: r"`//`, `%`, `/`, `**` · `a, b = b, a` · `if/elif/else` · `and`, `or` paresseux",
    2: r"`range(a, b, p)` · `while cond:` · `n % 10`, `n // 10`",
    3: r"`def`, `return` · sans `return` : `None` · liste modifiée en place par l'appelé",
    4: r"`L[i]`, `len(L)`, `L.append(x)`, `L.pop()` · `(a, b) = L[i]` · `B = A` ne copie pas",
    5: r"accumulateur avant la boucle · extremum : partir de `L[0]` · `raise Exception(\"Empty list\")`",
    6: r"`while i < n and L[i] != x` · liste croissante : arrêt au premier élément $\ge x$",
    7: r"`while i < n - 1 and L[i] <= L[i + 1]` · `return i >= n - 1` · deux indices `i`, `j`",
    8: r"bornes incluses `[left, right]` · `mid = (left + right) // 2` · $\lfloor\log_2 n\rfloor+1$ nœuds au pire, $2$ comparaisons par nœud",
    9: r"`R = []`, `R.append(…)` · chiffres · `v = v * 10 + d` · Syracuse",
    10: r"supprimer : décaler puis `pop()` · insérer : `append` puis décaler · échanges pour renverser",
    11: r"`(obj, q) = stock[i]` · `stock[i] = (obj, q2)` · recherche arrêtée au premier objet $\ge$",
    12: r"`H[e] += 1` · sélection : minimum de `L[i…]` · fusion · tri fusion",
    13: r"pile (garage) · dichotomie $2(\log_2 n+1)$ · premier/dernier indice · fenêtre glissante · fusion-séparation",
    14: r"colline : monter puis descendre · suppression dans liste décroissante · RLE encode/décode",
    15: r"stock trié de couples · arrêt dès que la capacité est dépassée · groupes · suppression par décalage + `pop()`",
}
FORMULES = {e["id"]: _FL[lvl["n"]] for lvl in LEVELS for e in lvl["exos"]}

assert len(CHECKED) == len(set(CHECKED)), "duplicate exercise id"
