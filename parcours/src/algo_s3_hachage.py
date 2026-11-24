"""Level path: S3 algorithmics, hashing (course « [algo] Arbres et Recherches 2 », ECUE AR2, hashing part only).

Moodle chapters used: « Méthodes de hachage - Hashing Methods », « 1 - Hachage : principe et méthodes de base »
(fiche Hachage1), « 2 - Hachage : résolution des collisions par chaînage » (fiches Hachage_resolutionsIndirectes and
algo_hachage_coalescent), « 3 - Hachage : résolution des collisions par calcul » (fiches Hachage_resolutionsDirectes and
algo_hachage_calcul), and the QCM of the « Tests - Homework (DM) » folder that deal with hashing (functions, collision
resolution). General trees and B-trees are another path. Quadratic probing is not in the Moodle course: not covered.

Calibrated on the C3 / B5 midterms of `annales/raw/S3/Midterms/Algo` that contain hashing: 24 Oct 2016 (2020: linear d=4,
valid tables, questions), 7 Nov 2017 (2021) and 9 Nov 2020 (2024): coalescent / linear / double hashing on 11 keys with
h(x) = (2x+5) mod 11 (official corrections), 29 Oct 2018 (2022) and 23 Oct 2022 (2027): questions, 5 Mar 2019 (2023#):
linear d=5, 10 Mar 2020 (2024#) and 17 Mar 2021 (2025#): linear d=3 and separate chaining, 22 Oct 2024 (B5, 2028, no
correction on the server: « corrigé rédigé »). The finals contain no hashing exercise (text read; the three scanned finals
2025, 2027 and 2029 midterm were only skimmed).

Checks: `value` exercises are checked by build.py (sympy, plus the `hach` helper of build.py that simulates a hash table).
The tables written in the `open` solutions are produced below by independent reference engines (`_lin`, `_coal`, `_sep`),
asserted against the official corrections (CHECKED), so no table is typed by hand.
Convention used everywhere: no reserve for the coalescent hashing (free cell searched from the end of the table, the new
cell is linked after the last element of the collision list); separate chaining inserts at the end of the list.
Levels 1 and 2 are S1/S2 reminders (modulo, arrays, linked lists, complexity: `algo-s1-taa`, `obm`).
"""

SUBJECT = {
    "id": "algo-s3-hachage",
    "ordre": 680,
    "matiere": "algo",
    "semestre": "S3",
    "ecue": "AR2",
    "titre": "Hachage : fonctions, chaînage, hachage linéaire et double hachage",
    "chapitres_moodle": [
        "02_👨‍🏫 Méthodes de hachage - Hashing Methods",
        "03_1 - Hachage - principe et méthodes de base",
        "04_2 - Hachage - résolution des collisions par chaînage",
        "05_3 - Hachage - résolution des collisions par calcul",
        "01_💻 Tests - Homework (DM)",
    ],
    "td": "DM 1.1 (fonctions de hachage) et DM 2 (résolution des collisions), tests blancs, QCM « S'évaluer » du cours",
    "examens": ["Contrôle n°3 / Examen B5 d'algorithmique AR2 (octobre-novembre, Python et tables de hachage)"],
}

CHECKED = []


# ---------------------------------------------------------------- reference engines (tables of the open solutions)
def _lin(m, hs, steps):
    """Linear / double hashing: returns the table (index of the element or None) and the cells examined by each insertion."""
    T, paths = [None] * m, []
    for e, h in enumerate(hs):
        p = []
        for j in range(m):
            c = (h + steps[e] * j) % m
            p.append(c)
            if T[c] is None:
                T[c] = e
                break
        paths.append(p)
    return T, paths


def _coal(m, hs):
    """Coalescent hashing without reserve: table, links, collision kind and cells examined by each insertion."""
    T, L, info = [None] * m, [-1] * m, []
    for e, h in enumerate(hs):
        if T[h] is None:
            T[h] = e
            info.append((None, [h], None))
            continue
        kind = "primaire" if hs[T[h]] == h else "secondaire"
        c, p = h, [h]
        while L[c] != -1:
            c = L[c]
            p.append(c)
        r = m - 1
        while T[r] is not None:
            r -= 1
        T[r], L[c] = e, r
        info.append((kind, p, r))
    return T, L, info


def _sep(m, hs):
    lists = [[] for _ in range(m)]
    for e, h in enumerate(hs):
        lists[h].append(e)
    return lists


def _cell(T, names, c):
    return str(names[T[c]]) if T[c] is not None else "vide"


def _tab_open(m, T, names):
    return "```\n" + "\n".join(f"{c:>2}  {_cell(T, names, c)}" for c in range(m)) + "\n```"


def _tab_coal(m, T, L, names):
    return "```\ncase  elt   lien\n" + "\n".join(
        f"{c:>3}  {_cell(T, names, c) if T[c] is not None else '':<5} {L[c] if T[c] is not None else ''}" for c in range(m)) + "\n```"


def _tab_sep(m, lists, names):
    return "```\n" + "\n".join(f"{c:>2}  " + (" → ".join(str(names[e]) for e in lists[c]) if lists[c] else "vide")
                               for c in range(m)) + "\n```"


def _trace_open(names, hs, paths):
    rows = [f"- {names[e]} (h = {hs[e]}) : cases {', '.join(map(str, p[:-1]))} occupées, case {p[-1]} libre, on y place {names[e]}."
            for e, p in enumerate(paths) if len(p) > 1]
    return "\n".join(rows) if rows else "Aucune collision."


def _trace_coal(names, hs, info):
    rows = []
    for e, (kind, p, r) in enumerate(info):
        if kind:
            rows.append(f"- {names[e]} (h = {hs[e]}) : case {hs[e]} occupée, collision {kind}. Liste parcourue : {', '.join(map(str, p))}. "
                        f"Première case libre en partant de la fin : {r}, liée à la case {p[-1]}.")
    return "\n".join(rows) if rows else "Aucune collision."


def sol_lin(m, hs, names, step, intro=""):
    T, paths = _lin(m, hs, [step] * len(hs))
    return (f"{intro}Pas de décalage $d={step}$ : après la case $c$ on teste $(c+{step}) \\bmod {m}$.\n\n"
            f"{_trace_open(names, hs, paths)}\n\nLes autres clés vont directement dans leur case $h$.\n\nTable finale :\n\n{_tab_open(m, T, names)}"), T


def sol_dbl(m, hs, ds, names):
    T, paths = _lin(m, hs, ds)
    steps = ", ".join(f"{names[e]} : {ds[e]}" for e in range(len(hs)))
    return (f"Essai $i$ de $x$ : $(h(x)+d(x)\\times(i-1)) \\bmod {m}$. Pas $d(x)$ : {steps}.\n\n{_trace_open(names, hs, paths)}\n\n"
            f"Table finale :\n\n{_tab_open(m, T, names)}"), T


def sol_coal(m, hs, names, intro=""):
    T, L, info = _coal(m, hs)
    return (f"{intro}Sans réserve : la place de débordement est la première case libre en partant de la case {m - 1}.\n\n"
            f"{_trace_coal(names, hs, info)}\n\nTable finale :\n\n{_tab_coal(m, T, L, names)}"), (T, L)


def sol_sep(m, hs, names):
    lists = _sep(m, hs)
    return ("Chaque case contient la liste des clés de même valeur de hachage (insertion en fin de liste).\n\n"
            f"{_tab_sep(m, lists, names)}"), lists


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


# ---------------------------------------------------------------- data of the exams (hash values given by the subjects)
N20 = "data kirk neelix odo picard q quark sisko tuvok worf".split()
H20 = [4, 5, 3, 1, 7, 6, 2, 7, 1, 7]  # C3 24 Oct 2016 and C3 17 Mar 2021 (same table 1)
N23 = "aragog buck dobby fumseck missteigne nagini crockdur croutard kreattur hedwige".split()
H23 = [0, 1, 4, 0, 0, 5, 2, 4, 8, 8]  # C3 5 Mar 2019
N24 = "beck cale clapton hendrix hooker king richards vaughan winter young".split()
H24 = [10, 10, 4, 5, 6, 8, 3, 8, 1, 5]  # C3 10 Mar 2020
K21 = [12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5]  # C3 7 Nov 2017 and 9 Nov 2020
H21 = [(2 * k + 5) % 11 for k in K21]
D21 = [7 - k % 7 for k in K21]
K28 = [15, 24, 125, 4, 26, 6, 78, 55, 89]  # B5 22 Oct 2024
H28 = [k % 12 for k in K28]

# the official corrections (tables as printed), asserted against the engines
_OFF = {
    "lin20": ["sisko", "odo", "quark", "neelix", "data", "kirk", "q", "picard", "worf", "tuvok", None],
    "lin23": ["aragog", "buck", "crockdur", "croutard", "dobby", "fumseck", None, "hedwige", "kreattur", "nagini", "missteigne"],
    "lin24": ["vaughan", "winter", "cale", "richards", "clapton", "hendrix", "hooker", None, "king", "young", "beck"],
    "lin25": ["worf", "odo", "quark", "neelix", "data", "kirk", "q", "picard", "tuvok", None, "sisko"],
    "lin21": [11, 39, 20, 5, 16, 44, 88, 12, 23, 13, 94],
    "dbl21": [11, 23, 20, 16, 39, 44, 94, 12, 88, 13, 5],
    "coal21": [(5, -1), (20, -1), (16, 0), (39, -1), (11, 2), (44, 10), (94, 3), (12, 8), (23, -1), (13, -1), (88, 4)],
}


def _named(T, names):
    return [names[e] if e is not None else None for e in T]


assert _named(_lin(11, H20, [4] * 10)[0], N20) == _OFF["lin20"]
assert _named(_lin(11, H23, [5] * 10)[0], N23) == _OFF["lin23"]
assert _named(_lin(11, H24, [3] * 10)[0], N24) == _OFF["lin24"]
assert _named(_lin(11, H20, [3] * 10)[0], N20) == _OFF["lin25"]
assert _named(_lin(11, H21, [1] * 11)[0], K21) == _OFF["lin21"]
assert _named(_lin(11, H21, D21)[0], K21) == _OFF["dbl21"]
_T, _L, _ = _coal(11, H21)
assert [(K21[_T[c]], _L[c]) for c in range(11)] == _OFF["coal21"]
# C3 24 Oct 2016, exercise 2: only table C can result from linear insertions (d=1) of A..G (official correction: A-B-D impossible)
_HV = dict(A=2, B=0, C=0, D=4, E=4, F=4, G=2)
_VALID = set()
import itertools  # noqa: E402

for _p in itertools.permutations("ABCDEFG"):
    _t = _lin(7, [_HV[c] for c in _p], [1] * 7)[0]
    _VALID.add("".join(_p[_t[c]] for c in range(7)))
assert [t in _VALID for t in ("CGBADEF", "FGBDACE", "BCAGEDF", "GECADBF")] == [False, False, True, False]
CHECKED.append("official tables")

S20 = "Contrôle n°3 d'algo S3 du 24 octobre 2016 (annales S3/Midterms/Algo/2020, corrigé officiel)"
S21 = "Contrôle n°3 d'algo S3 du 7 novembre 2017 (annales S3/Midterms/Algo/2021, corrigé officiel)"
S22 = "Contrôle n°3 d'algo S3 du 29 octobre 2018 (annales S3/Midterms/Algo/2022, pas de corrigé de la partie hachage)"
S23 = "Contrôle n°3 d'algo S3# du 5 mars 2019 (annales S3/Midterms/Algo/2023#, corrigé officiel)"
S24 = "Contrôle n°3 d'algo S3# du 10 mars 2020 (annales S3/Midterms/Algo/2024#, corrigé officiel)"
S25 = "Contrôle n°3 d'algo S3# du 17 mars 2021 (annales S3/Midterms/Algo/2025#, corrigé officiel)"
S28 = "Examen B5 d'algo AR2 du 22 octobre 2024 (annales S3/Midterms/Algo/2028, sans corrigé officiel : corrigé rédigé)"

NOTIONS = [
    {"id": "modulo", "titre": "Division euclidienne et modulo (rappel S1)",
     "formule": r"$a=bq+r$ avec $0\le r<b$ · $r=a\bmod b$ · $(a+b)\bmod m=((a\bmod m)+(b\bmod m))\bmod m$",
     "exemple": r"$125=10\times12+5$ donc $125\bmod12=5$ ; $-7\bmod5=3$ car $-7=-2\times5+3$",
     "cours": r"Le reste est toujours entre $0$ et $b-1$, même pour un dividende négatif. On peut réduire chaque terme modulo $m$ avant de calculer. Toute la suite repose sur $\bmod m$ : une fonction de hachage ramène une clé dans $[0,m-1]$. Rappel S1 : parcours « Arithmétique » (`obm`)."},
    {"id": "tab", "titre": "Tableaux, listes chaînées et complexité (rappel S1/S2)",
     "formule": r"accès à $T[i]$ : $O(1)$ · recherche séquentielle : $O(n)$, $\frac{n+1}2$ comparaisons en moyenne si la clé est présente · insertion en tête d'une liste chaînée : $O(1)$",
     "exemple": r"liste de $1000$ éléments : au pire $1000$ comparaisons, en moyenne $500{,}5$ pour une clé présente",
     "cours": r"Un tableau donne accès direct par indice, mais insérer au début décale tous les éléments. Une liste chaînée insère en tête en $O(1)$, mais atteindre le $k$-ième maillon coûte $k-1$ liens suivis. Le hachage cherche à retrouver le « accès direct » d'un tableau pour des clés quelconques. Rappel S1 : parcours « Types algébriques abstraits » (`algo-s1-taa`)."},
    {"id": "principe", "titre": "Principe du hachage, collisions, propriétés",
     "formule": r"$h:\text{clés}\to[0,m-1]$ · uniforme, rapide à calculer, déterministe · pas de fonction universelle · collision : $x\ne y$ et $h(x)=h(y)$",
     "exemple": r"$h(x)=x\bmod11$ : $h(125)=4$ et $h(15)=4$, collision entre 125 et 15",
     "cours": r"On range les clés d'un univers très grand dans un tableau de $m$ cases, la valeur de hachage $h(x)$ donnant l'indice. Si $h$ est injective il n'y a pas de problème ; sinon plusieurs clés ont la même valeur de hachage primaire : c'est une collision (primaire). Il n'existe pas de fonction de hachage universelle : elle s'adapte aux données. Les méthodes de résolution sont dites directes (par calcul) ou indirectes (par chaînage)."},
    {"id": "division", "titre": "Fonction de hachage par division",
     "formule": r"$h(x)=x\bmod m$ · $m$ premier pour limiter les collisions · $h(x)=(ax+b)\bmod m$",
     "exemple": r"$m=11$, $h(x)=(2x+5)\bmod11$ : $h(88)=181\bmod11=5$",
     "cours": r"La valeur de hachage est le reste de la division entière de la clé par $m$. Facile à calculer, mais si $m$ a de petits diviseurs, des clés régulièrement espacées tombent dans peu de cases (clés multiples de 5 avec $m=10$ : seulement les cases 0 et 5). Prendre $m$ premier limite (sans éliminer) les collisions."},
    {"id": "multi-ext", "titre": "Multiplication et extraction",
     "formule": r"multiplication : $h(e)=\lfloor((e\,\theta)\bmod1)\times m\rfloor$ avec $0<\theta<1$ · extraction de $p$ bits : $h\in[0,2^p-1]$, $m=2^p$",
     "exemple": r"$\theta=0{,}6$, $m=10$, $e=7$ : $7\times0{,}6=4{,}2$, partie décimale $0{,}2$, $h=2$",
     "cours": r"Multiplication : on garde la partie décimale de $e\theta$ puis on l'étale sur $[0,m-1]$. Un $\theta$ trop proche de $0$ ou de $1$ accumule les clés aux extrémités. Extraction : on prend $p$ bits de la clé (par exemple les $p$ bits de poids faible, $x\bmod2^p$). Facile, mais une partie seulement de la clé est utilisée : à réserver aux données connues d'avance ou aux bits non significatifs."},
    {"id": "compression", "titre": "Compression (somme, OU exclusif)",
     "formule": r"découpage de la clé en sous-mots · combinaison par OU exclusif (ou somme des codes) · puis $\bmod m$ · deux anagrammes ont la même valeur",
     "exemple": r"$\text{AB}$ : $65+66=131$, $131\bmod11=10$",
     "cours": r"Les bits (ou caractères) de la clé sont découpés en sous-mots de même longueur combinés par des opérateurs sur les bits. ET donne des valeurs systématiquement plus petites, OU plus grandes : on préfère le OU exclusif. Défaut : toutes les permutations d'une clé (anagrammes) ont la même valeur. Remède : des décalages (rotations) qui dépendent de la position, qui peuvent toutefois créer d'autres collisions."},
    {"id": "charge", "titre": "Facteur de charge et coût de recherche",
     "formule": r"$\alpha=\frac nm$ · au moins $n-m$ collisions si $n>m$ · coût moyen d'une recherche réussie = $\frac{\text{somme des positions}}n$",
     "exemple": r"$n=15$ clés dans $m=20$ cases : $\alpha=\frac34$",
     "cours": r"Le facteur de charge $\alpha=\frac nm$ mesure le remplissage. Les méthodes par calcul rangent tout dans le tableau : il faut $n\le m$ ($\alpha\le1$). Le chaînage séparé accepte $\alpha>1$. Les méthodes sont à peu près équivalentes pour un faible $\alpha$. Le coût d'une recherche se compte en cases examinées : pour une recherche réussie, c'est le rang de la clé dans sa suite d'essais ou dans sa liste."},
    {"id": "sep", "titre": "Chaînage séparé",
     "formule": r"case $i$ = liste des clés de valeur $i$ · recherche séquentielle dans la liste · pas de collision secondaire",
     "exemple": r"$m=11$ : clés de valeurs $5,5,8$ : la case $5$ contient une liste de $2$ clés",
     "cours": r"Chaque case du tableau contient la liste (hors du tableau) des éléments de même valeur de hachage primaire. Recherche : on calcule $h(x)$ puis on parcourt la liste. Insertion avec ou sans redondance (avec : plus rapide, listes plus longues). Suppression directe dans la liste. C'est la méthode la plus performante, et la seule qui n'exige pas $m\ge n$."},
    {"id": "lin", "titre": "Hachage linéaire",
     "formule": r"$\text{essai}_i(x)=(h(x)+d\,(i-1))\bmod m$ · $d=1$ : cases suivantes · $d$ premier avec $m$ pour parcourir tout le tableau",
     "exemple": r"$m=11$, $h=7$, $d=4$ : essais $7,\ 0,\ 4,\ 8,\dots$",
     "cours": r"En cas de collision on teste les cases suivantes de $d$ en $d$ (en revenant au début après la dernière case) jusqu'à trouver une case vide. Les clés de même valeur de hachage ont la même suite d'essais ; les groupements d'éléments (clustering) grossissent : la probabilité qu'un groupement de $k$ éléments grandisse est $\frac{k+2}m$. Méthode très simple, mais la moins rapide."},
    {"id": "dbl", "titre": "Double hachage",
     "formule": r"$\text{essai}_i(x)=(h(x)+d(x)\,(i-1))\bmod m$ · $\gcd(d(x),m)=1$ : $m$ premier et $d\in[1,m-1]$, ou $m=2^p$ et $d$ impair",
     "exemple": r"$m=11$, $h(44)=5$, $d(44)=5$ : essais $5,\ 10,\ 4,\ 9,\dots$",
     "cours": r"Le pas dépend de la clé grâce à une deuxième fonction de hachage $d$, ce qui disperse les éléments en collision et évite le clustering du hachage linéaire. Pour que les $m$ essais visitent les $m$ cases il faut $\gcd(d(x),m)=1$ : $m$ premier, ou $m=2^p$ avec $d(x)=2d'(x)+1$ impair. Plus performant que le linéaire, mais deux fonctions à écrire."},
    {"id": "coal", "titre": "Hachage coalescent",
     "formule": r"chaînage dans le tableau (colonne lien) · débordement depuis la fin du tableau · collision primaire : $h(x)=h(y)$, secondaire : cases partagées",
     "exemple": r"$m=12$ : $125$ et $89$ ont $h=5$ : $89$ va en case $11$ ou plus bas, liée à la case $5$",
     "cours": r"Les éléments en collision sont chaînés à l'intérieur du tableau : chaque case contient l'élément et le lien vers le suivant ($-1$ s'il n'y en a pas). Sans réserve : on cherche la première case libre en partant de la fin du tableau, on la relie au dernier élément de la liste de collisions. Inconvénient : les collisions secondaires (une case de débordement utilisée par $y$ avec $h(y)\ne i$ gêne la prochaine clé de valeur $i$), les listes se mélangent. Méthode la plus efficace quand la zone mémoire est fixée à l'avance."},
    {"id": "suppr", "titre": "Suppression, cases libres et bilan des méthodes",
     "formule": r"case : vide · occupée · libre · recherche : on continue sur une case libre · insertion : on réutilise la première case libre rencontrée",
     "exemple": r"supprimer vraiment un élément casserait la suite d'essais des clés placées après lui",
     "cours": r"Sauf avec le chaînage séparé, on ne supprime pas réellement : on marque la case libre (elle a été occupée puis libérée). La recherche ne s'arrête pas sur une case libre, l'insertion garde la première case libre rencontrée mais vérifie d'abord que la clé n'est pas présente. Bilan : le chaînage séparé est le plus performant ; le coalescent est le meilleur pour une zone fixée à l'avance ; le linéaire est le plus simple et le moins rapide ; le double hachage est meilleur que le linéaire ; le marquage allonge les recherches. Les collisions secondaires n'existent qu'avec le coalescent, le clustering qu'avec le linéaire."},
]

LEVELS = [
    {"n": 1, "titre": "Rappel S1 : division euclidienne et modulo", "notions": ["modulo"], "exos": [
        v("m1", r"Calculer $125\bmod12$.", "125%12", "5", r"$125=10\times12+5$ donc le reste est $5$."),
        v("m2", r"Calculer $(7\times13+5)\bmod11$.", "(7*13+5)%11", "8", r"$7\times13+5=96=8\times11+8$ donc $96\bmod11=8$."),
        v("m3", r"Quel est le reste de la division euclidienne de $-7$ par $5$ ?", "(-7)%5", "3", r"Le reste est entre $0$ et $4$ : $-7=-2\times5+3$, donc $3$."),
        v("m4", r"Calculer $2^{10}\bmod7$.", "2**10%7", "2", r"$2^3=8\equiv1\pmod7$ donc $2^{10}=(2^3)^3\times2\equiv2$. Vérification : $1024=146\times7+2$."),
        v("m5", r"Calculer $(17+9\times3)\bmod11$.", "(17+9*3)%11", "0", r"$17+27=44=4\times11$ : le reste est $0$."),
    ]},
    {"n": 2, "titre": "Rappel S1/S2 : tableaux, listes chaînées, complexité", "notions": ["tab"], "exos": [
        v("t1", r"On cherche séquentiellement une clé présente dans une liste non triée de $n=1000$ éléments, chaque position étant équiprobable. Combien de comparaisons en moyenne ?", "Rational(1000+1,2)", "Rational(1001,2)", r"En moyenne $\frac{n+1}2=\frac{1001}2=500{,}5$ comparaisons."),
        v("t2", r"Combien de comparaisons au pire pour constater qu'une clé est absente d'une liste non triée de $250$ éléments ?", "250", "250", r"Il faut examiner tous les éléments : $250$."),
        v("t3", r"Un tableau contient $40$ éléments (il reste de la place). Combien d'éléments faut-il décaler pour insérer un nouvel élément en première position ?", "40", "40", r"Tous les éléments reculent d'une case : $40$ décalages. Dans une liste chaînée, l'insertion en tête ne déplace rien."),
        v("t4", r"Dans une liste simplement chaînée, combien de liens faut-il suivre depuis la tête pour atteindre le $9$-ème maillon ?", "9-1", "8", r"Le $1$-er maillon est la tête (aucun lien) : pour le $k$-ième il faut $k-1$ liens, donc $8$."),
    ]},
    {"n": 3, "titre": "Principe du hachage et fonction par division", "notions": ["principe", "division"], "exos": [
        v("d1", r"Avec $h(x)=x\bmod11$, quelle est la valeur de hachage de $125$ ?", "125%11", "4", r"$125=11\times11+4$ donc $h(125)=4$."),
        v("d2", r"Avec $m=11$ et $h(x)=(2x+5)\bmod11$, calculer $h(88)$.", "(2*88+5)%11", "5", r"$2\times88+5=181=16\times11+5$ donc $h(88)=5$."),
        v("d3", r"Table de taille $m=12$, $h(x)=x\bmod12$, clés $15,24,125,4,26,6,78,55,89$. Combien de clés arrivent dans une case déjà visée par une clé précédente (collisions) ?",
          "hach('sep',12,[3,0,5,4,2,6,6,7,5],'coll')", "2",
          r"Valeurs de hachage : $15\to3$, $24\to0$, $125\to5$, $4\to4$, $26\to2$, $6\to6$, $78\to6$, $55\to7$, $89\to5$. Les clés $78$ (case 6, déjà visée par $6$) et $89$ (case 5, déjà visée par $125$) sont en collision : $2$ collisions."),
        v("d4", r"Les clés $5,10,15,\dots,50$ (dix clés) sont rangées avec $h(x)=x\bmod10$. Combien de collisions ?",
          "hach('sep',10,[5,0,5,0,5,0,5,0,5,0],'coll')", "8",
          r"Les valeurs sont $5,0,5,0,\dots$ : seulement $2$ cases utilisées pour $10$ clés, donc $10-2=8$ collisions. Avec $m=11$ (premier) les dix valeurs seraient distinctes."),
        o("d5", r"Citer trois propriétés d'une bonne fonction de hachage. Pourquoi prend-on souvent $m$ premier pour la division ? Une fonction de hachage universelle existe-t-elle ?",
          r"Une bonne fonction de hachage est **uniforme** (les clés se répartissent le mieux possible dans le tableau), **facile et rapide à calculer** et **déterministe** (même clé, même valeur).\n\nAvec la division, si $m$ a de petits diviseurs, des clés régulièrement espacées tombent sur peu de cases : $m=10$ et des multiples de $5$ donnent seulement les cases $0$ et $5$. Un $m$ premier limite ces collisions (sans les éliminer).\n\nIl n'existe **pas** de fonction de hachage universelle : elle doit être adaptée aux données hachées et à l'application.".replace("\\n", "\n"), src=S20 + ", ex. 3", duree=4),
    ]},
    {"n": 4, "titre": "Multiplication et extraction de bits", "notions": ["multi-ext"], "exos": [
        v("x1", r"Méthode de multiplication, $\theta=0{,}6$, $m=10$ : calculer $h(7)=\lfloor((7\theta)\bmod1)\times m\rfloor$.", "floor((7*Rational(3,5))%1*10)", "2", r"$7\times0{,}6=4{,}2$, partie décimale $0{,}2$, $0{,}2\times10=2$ : $h(7)=2$."),
        v("x2", r"Méthode de multiplication, $\theta=0{,}618$, $m=16$ : calculer $h(25)$.", "floor((25*Rational(618,1000))%1*16)", "7", r"$25\times0{,}618=15{,}45$, partie décimale $0{,}45$, $0{,}45\times16=7{,}2$, partie entière $7$."),
        v("x3", r"On extrait les $3$ bits de poids faible de la clé $182=10110110_2$ ($m=2^3=8$). Valeur de hachage ?", "bits('10110110')%8", "6", r"Les trois derniers bits sont $110_2=6$ (de même $182\bmod8=6$)."),
        v("x4", r"On extrait les bits numérotés $3,4,5$ (le bit $0$ étant celui de poids faible) de la clé $10101101_2$. Valeur de hachage ?", "(bits('10101101')//2**3)%2**3", "5", r"On décale de $3$ bits : $10101_2$, puis on garde $3$ bits : $101_2=5$ (calcul : $173\div8$ donne $21$, et $21\bmod8=5$)."),
        v("x5", r"Multiplication avec $\theta=0{,}99$ (trop proche de $1$), $m=10$, clés $1,2,3,4,5$. Combien de collisions ?", "hach('sep',10,[9,9,9,9,9],'coll')", "4",
          r"$e\times0{,}99=e-0{,}01e$, partie décimale $1-0{,}01e\in[0{,}95;0{,}99]$, donc $h=9$ pour les cinq clés : $4$ collisions. Un $\theta$ trop proche de $0$ ou de $1$ accumule les clés aux extrémités du tableau."),
    ]},
    {"n": 5, "titre": "Compression : somme des codes et OU exclusif", "notions": ["compression"], "exos": [
        v("c1", r"Clé « AB » (codes $65$ et $66$), $m=11$ : $h=(\text{somme des codes})\bmod m$.", "(65+66)%11", "10", r"$65+66=131=11\times11+10$ : $h=10$."),
        v("c2", r"Clé « ECU » (E=69, C=67, U=85), $m=13$ : $h=(\text{somme des codes})\bmod13$.", "(69+67+85)%13", "0", r"$69+67+85=221=17\times13$ : $h=0$."),
        v("c3", r"Les clés RAT, ART et TAR (R=82, A=65, T=84) sont rangées avec $m=17$ et la somme des codes. Combien de collisions ?", "hach('sep',17,[10,10,10],'coll')", "2",
          r"Les trois ont pour somme $231=13\times17+10$ : même valeur $10$, donc $2$ collisions (anagrammes). La somme, comme le OU exclusif, hache de la même façon toutes les permutations d'une clé."),
        v("c4", r"Compression par OU exclusif de deux sous-mots de $4$ bits : $1011\oplus0110$. Donner le résultat en décimal.", "(1+0)%2*8+(0+1)%2*4+(1+1)%2*2+(1+0)%2", "13",
          r"Bit par bit : $1\oplus0=1$, $0\oplus1=1$, $1\oplus1=0$, $1\oplus0=1$, soit $1101_2=13$."),
        o("c5", r"Pourquoi préfère-t-on le OU exclusif au ET et au OU pour combiner les sous-mots ? Quel est le défaut de la compression et comment le corriger ?",
          "Un ET donne des résultats systématiquement plus petits (un bit n'est à 1 que si tous les sous-mots l'ont à 1), un OU des résultats systématiquement plus grands. Le OU exclusif ne favorise ni 0 ni 1.\n\nDéfaut : toutes les permutations d'une clé (les anagrammes) donnent la même valeur de hachage. Remède : introduire des décalages (rotations de bits) qui dépendent de la position du caractère. Cela peut supprimer les collisions entre anagrammes mais peut en créer de nouvelles.",
          duree=4),
    ]},
    {"n": 6, "titre": "Facteur de charge et coût moyen", "notions": ["charge"], "exos": [
        v("a1", r"$n=15$ clés sont rangées dans un tableau de $m=20$ cases. Quel est le facteur de charge $\alpha$ ?", "Rational(15,20)", "Rational(3,4)", r"$\alpha=\frac nm=\frac{15}{20}=\frac34$."),
        v("a2", r"$n=30$ clés dans $m=11$ cases. Donner $\alpha$ (quelle méthode de résolution reste possible ?).", "Rational(30,11)", "Rational(30,11)",
          r"$\alpha=\frac{30}{11}>1$ : les méthodes par calcul (linéaire, double hachage) rangent tout dans le tableau et sont impossibles ; seul le chaînage séparé accepte $\alpha>1$ (listes de longueur moyenne $\alpha$)."),
        v("a3", r"Un tableau de $m=17$ cases est rempli par hachage linéaire, sans suppression, après $12$ insertions. Combien de cases vides ?", "17-12", "5", r"Chaque insertion occupe une case : $17-12=5$ cases vides, $\alpha=\frac{12}{17}$."),
        v("a4", r"Chaînage séparé, $m=3$, insertion en fin de liste de $6$ clés de valeurs $0,1,0,2,0,1$. Coût moyen d'une recherche réussie (nombre moyen de clés examinées, chaque clé recherchée une fois) ?",
          "Rational(hach('sep',3,[0,1,0,2,0,1],'succ'),6)", "Rational(5,3)",
          r"Listes : case $0$ de longueur $3$ (rangs $1,2,3$ : total $6$), case $1$ de longueur $2$ (total $3$), case $2$ de longueur $1$ (total $1$). Total $10$ cases examinées pour $6$ clés : $\frac{10}6=\frac53$."),
        v("a5", r"Au minimum, combien de collisions (clé arrivant dans une case déjà utilisée) quand on range $n=20$ clés dans $m=15$ cases ?", "20-15", "5",
          r"Au plus $15$ cases peuvent être utilisées sans collision ; les $20-15=5$ autres clés arrivent forcément dans une case déjà utilisée. Minimum : $n-m=5$."),
    ]},
    {"n": 7, "titre": "Chaînage séparé", "notions": ["sep"], "exos": [
        v("s1", r"$m=11$, chaînage séparé, clés de valeurs $10,10,4,5,6,8,3,8,1,5$ (beck, cale, clapton, hendrix, hooker, king, richards, vaughan, winter, young). Longueur de la plus longue liste ?",
          "hach('sep',11,[10,10,4,5,6,8,3,8,1,5],'maxlen')", "2",
          r"Cases : $10$ : beck, cale ; $4$ : clapton ; $5$ : hendrix, young ; $6$ : hooker ; $8$ : king, vaughan ; $3$ : richards ; $1$ : winter. La plus longue liste a $2$ clés.", src=S24 + ", ex. 1 (question 2)"),
        v("s2", r"$m=11$, chaînage séparé, clés de valeurs $4,5,3,1,7,6,2,7,1,7$ (data, kirk, neelix, odo, picard, q, quark, sisko, tuvok, worf). Longueur de la plus longue liste ?",
          "hach('sep',11,[4,5,3,1,7,6,2,7,1,7],'maxlen')", "3",
          r"La case $7$ contient picard, sisko, worf ($3$ clés), la case $1$ contient odo et tuvok ; les autres cases ont au plus une clé.", src=S25 + ", ex. 1 (question 2)"),
        v("s3", r"Chaînage séparé, clés de valeurs de hachage ($10,10,4,5,6,8,3,8,1,5$, $m=11$, insertion en fin de liste). Nombre total de clés examinées pour retrouver chacune des $10$ clés une fois ?",
          "hach('sep',11,[10,10,4,5,6,8,3,8,1,5],'succ')", "13",
          r"Cases de longueur $1$ : $1,3,4,6$ donnent $1$ chacune ($4$ au total). Cases de longueur $2$ : $5,8,10$ donnent $1+2=3$ chacune ($9$ au total). Total $4+9=13$."),
        v("s4", r"Chaînage séparé ($m=11$, dix clés de valeurs $10,10,4,5,6,8,3,8,1,5$). Combien de cases ont une liste vide ?",
          "11-(10-hach('sep',11,[10,10,4,5,6,8,3,8,1,5],'coll'))", "4",
          r"$3$ clés arrivent dans une case déjà utilisée, donc $10-3=7$ cases sont non vides et $11-7=4$ cases sont vides (0, 2, 7 et 9)."),
    ]},
    {"n": 8, "titre": "Hachage linéaire", "notions": ["lin"], "exos": [
        v("l1", r"Hachage linéaire, $m=11$, décalage $d=4$. Une clé a $h=9$ : quelle est la case du $3$-ème essai ?", "(9+4*(3-1))%11", "6", r"$\text{essai}_3=(9+4\times2)\bmod11=17\bmod11=6$."),
        v("l2", r"Hachage linéaire, $m=11$, $d=4$. Les clés de valeurs $4,5,3,1,7,6,2$ sont déjà placées (dans cet ordre, table vide au départ). On insère sisko, de valeur $7$. Dans quelle case ?",
          "hach('lin',11,[4,5,3,1,7,6,2,7],'pos',d=4)", "0", r"La case $7$ est occupée (picard) ; essai suivant : $(7+4)\bmod11=0$, case libre : sisko va en case $0$.", src=S20 + ", ex. 1"),
        v("l3", r"Hachage linéaire, $m=11$, $d=4$, avec les dix clés de valeurs $4,5,3,1,7,6,2,7,1,7$ insérées dans cet ordre. Dans quelle case arrive la dernière (worf, de valeur $7$) ?",
          "hach('lin',11,H20,'pos',d=4)".replace("H20", "[4,5,3,1,7,6,2,7,1,7]"), "8",
          r"Sisko va en $0$ (voir ci-dessus), tuvok ($h=1$ occupée) en $(1+4)=5$ occupée puis $9$. Worf : $7$ occupée, $0$ occupée (sisko), $4$ occupée (data), $8$ libre : case $8$.", src=S20 + ", ex. 1"),
        v("l4", r"Hachage linéaire $m=11$, $d=3$, clés de valeurs $4,5,3,1,7,6,2,7,1,7$. Nombre total de cases examinées pour insérer les dix clés ?",
          "hach('lin',11,[4,5,3,1,7,6,2,7,1,7],'probes',d=3)", "22",
          r"Sept clés vont en une case ($7$ essais). Sisko : $7,10$ ($2$). Tuvok : $1,4,7,10,2,5,8$ ($7$). Worf : $7,10,2,5,8,0$ ($6$). Total $7+2+7+6=22$.", src=S25 + ", ex. 1 (question 1)"),
        v("l5", r"Hachage linéaire $m=11$, $d=5$, dix clés de valeurs $0,1,4,0,0,5,2,4,8,8$ (aragog à hedwige). Combien de clés trouvent leur case $h(x)$ déjà occupée ?",
          "hach('lin',11,[0,1,4,0,0,5,2,4,8,8],'coll',d=5)", "5",
          r"Les clés fumseck ($0$), missteigne ($0$), nagini ($5$, case prise par fumseck), croutard ($4$) et hedwige ($8$) trouvent leur case occupée : $5$ clés. Les autres ($0,1,4,2,8$ pour aragog, buck, dobby, crockdur, kreattur) vont directement dans leur case.", src=S23 + ", ex. 1"),
    ]},
    {"n": 9, "titre": "Double hachage", "notions": ["dbl"], "exos": [
        v("b1", r"$m=11$, $h(x)=(2x+5)\bmod11$ et $d(x)=7-(x\bmod7)$. Quelle est la case du $3$-ème essai de $x=44$ ?", "((2*44+5)%11+(7-44%7)*2)%11", "4",
          r"$h(44)=93\bmod11=5$, $d(44)=7-2=5$. Essai $3$ : $(5+5\times2)\bmod11=15\bmod11=4$.", src=S21 + ", ex. 1 (question 3)"),
        v("b2", r"Double hachage dans une table de $m=12$ cases : un pas $d(x)=8$ permet-il de visiter toutes les cases ? Combien de cases distinctes la suite d'essais visite-t-elle ?", "12/gcd(12,8)", "3",
          r"La suite $h,h+8,h+16,\dots\bmod12$ visite $\frac{m}{\gcd(m,d)}=\frac{12}4=3$ cases seulement : non. Il faut $\gcd(d,m)=1$ ($m$ premier, ou $m=2^p$ avec $d$ impair)."),
        v("b3", r"$m=11$, $h(x)=(2x+5)\bmod11$, $d(x)=7-(x\bmod7)$, clés insérées dans l'ordre $12,44,13,88,23,94,11,39,20,16,5$. Dans quelle case arrive la clé $5$ ?",
          "hach('dbl',11,[7,5,9,5,7,6,5,6,1,4,4],'pos',ds=[2,5,1,3,5,4,3,3,1,5,2])", "10",
          r"Valeurs $h$ : $7,5,9,5,7,6,5,6,1,4,4$ ; pas $d$ : $2,5,1,3,5,4,3,3,1,5,2$. Pour $x=5$ : $h=4$ occupée (16), $d=2$ donne $6$ (94) occupée, $8$ (88) occupée, $10$ libre : case $10$.", src=S21 + ", ex. 1 (question 3)"),
        v("b4", r"$m=11$, $h(x)=(2x+5)\bmod11$, $d(x)=7-(x\bmod7)$ (double hachage), clés insérées dans l'ordre $12,44,13,88,23,94,11,39,20,16,5$. Nombre total de cases examinées pour insérer les onze clés ?",
          "hach('dbl',11,[7,5,9,5,7,6,5,6,1,4,4],'probes',ds=[2,5,1,3,5,4,3,3,1,5,2])", "24",
          r"Nombres d'essais clé par clé : $1,1,1,2,2,1,3,4,2,3,4$ (par exemple $88$ : $5,8$ ; $94$ ne bouge pas ; $39$ : $6,9,1,4$ ; $5$ : $4,6,8,10$). Total $24$.", src=S21 + ", ex. 1 (question 3)"),
        v("b5", r"$m=16=2^4$, $h(x)=x\bmod16$ et $d(x)=2\,(x\bmod8)+1$ (toujours impair). Pour $x=21$, quelle est la case du $3$-ème essai ?", "(21%16+(2*(21%8)+1)*2)%16", "11",
          r"$h(21)=5$, $d(21)=2\times5+1=11$ (premier avec $16$). Essai $3$ : $(5+11\times2)\bmod16=27\bmod16=11$."),
    ]},
    {"n": 10, "titre": "Hachage coalescent", "notions": ["coal"], "exos": [
        v("k1", r"$m=12$, $h(x)=x\bmod12$, hachage coalescent sans réserve, clés $15,24,125,4,26,6,78,55,89$ dans cet ordre. Dans quelle case arrive $89$ ?",
          "hach('coal',12,[3,0,5,4,2,6,6,7,5],'pos')", "10",
          r"Valeurs : $3,0,5,4,2,6,6,7,5$. $78$ ($h=6$ occupée par $6$) va en $11$ (première case libre depuis la fin). $89$ ($h=5$ occupée par $125$) : $11$ prise, $10$ libre : case $10$, liée à $125$.", src=S28 + ", ex. 1"),
        v("k2", r"Hachage coalescent sans réserve, $m=12$, $h(x)=x\bmod12$, clés $15,24,125,4,26,6,78,55,89$ insérées dans cet ordre. Quelle est la valeur du lien de la case $6$ ?", "hach('coal',12,[3,0,5,4,2,6,6,7,5],'lien')[6]", "11",
          r"La clé $6$ (case $6$) est suivie dans sa liste de collisions par $78$, placé en case $11$ : le lien de la case $6$ vaut $11$.", src=S28 + ", ex. 1"),
        v("k3", r"$m=11$, $h(x)=(2x+5)\bmod11$, hachage coalescent, clés $12,44,13,88,23,94,11,39,20,16,5$. Combien de collisions secondaires ?",
          "hach('coal',11,[7,5,9,5,7,6,5,6,1,4,4],'sec')", "2",
          r"Une collision est secondaire quand la case visée contient une clé de valeur $h$ différente. Ici : $16$ ($h=4$) trouve la case $4$ occupée par $11$ ($h=5$, placé en réserve) et $5$ ($h=4$) trouve de même $11$. Les collisions de $88$, $23$, $11$, $39$ sont primaires : $2$ collisions secondaires.", src=S21 + ", ex. 1 (question 1)"),
        v("k4", r"Table coalescente de $m=23$ cases, sans réserve, clés $x_1,\dots,x_{23}$ de valeurs $5,11,17,8,2,20,7,15,5,8,16,11,16,21,9,14,6,7,19,2,5,8,18$ insérées dans cet ordre. Combien de collisions primaires ?",
          "hach('coal',23,[5,11,17,8,2,20,7,15,5,8,16,11,16,21,9,14,6,7,19,2,5,8,18],'prim')", "8",
          r"Il y a $12$ collisions au total ; $8$ sont primaires (la case visée contient une clé de même valeur : $x_9,x_{10},x_{12},x_{13},x_{18},x_{20},x_{21},x_{22}$) et $4$ sont secondaires. Calcul fait clé par clé."),
        v("k5", r"Hachage coalescent, $m=11$, clés de valeurs $4,5,3,1,7,6,2,7,1,7$. Dans quelle case arrive la dernière clé (valeur $7$) ?",
          "hach('coal',11,[4,5,3,1,7,6,2,7,1,7],'pos')", "8",
          r"Sisko ($h=7$, occupée par picard) va en $10$, tuvok ($h=1$, occupée par odo) en $9$. Worf : $7$ occupée, liste $7\to10$, première case libre depuis la fin : $10$, $9$ prises, $8$ libre : case $8$.", src=S25 + ", ex. 1 (données)"),
    ]},
    {"n": 11, "titre": "Coût de recherche : comparer les méthodes", "notions": ["charge", "sep", "lin", "dbl", "coal"], "exos": [
        v("u1", r"Onze clés ($m=11$, valeurs $7,5,9,5,7,6,5,6,1,4,4$). Hachage linéaire ($d=1$) : nombre total de cases examinées pour retrouver chacune des onze clés une fois ?",
          "hach('lin',11,[7,5,9,5,7,6,5,6,1,4,4],'succ',d=1)", "40",
          r"Pour une clé, le coût de recherche est son nombre d'essais à l'insertion. Nombres d'essais clé par clé (pas $1$) : $1,1,1,2,2,5,7,7,2,1,11$ ; total $40$."),
        v("u2", r"Onze clés ($m=11$, valeurs de hachage $7,5,9,5,7,6,5,6,1,4,4$), double hachage (pas $2,5,1,3,5,4,3,3,1,5,2$) : nombre total de cases examinées ?",
          "hach('dbl',11,[7,5,9,5,7,6,5,6,1,4,4],'succ',ds=[2,5,1,3,5,4,3,3,1,5,2])", "24", r"Calcul clé par clé : total $24$, nettement moins que le linéaire ($40$)."),
        v("u3", r"Onze clés ($m=11$, valeurs de hachage $7,5,9,5,7,6,5,6,1,4,4$), hachage coalescent : nombre total de cases examinées pour retrouver chaque clé (position dans sa liste de collisions) ?",
          "hach('coal',11,[7,5,9,5,7,6,5,6,1,4,4],'succ')", "19", r"Chaque clé est cherchée dans sa liste de collisions (rang dans la liste : $1$, $2$ ou $3$) : total $19$."),
        v("u4", r"Onze clés ($m=11$, valeurs de hachage $7,5,9,5,7,6,5,6,1,4,4$), chaînage séparé (insertion en fin de liste) : nombre total de clés examinées ?",
          "hach('sep',11,[7,5,9,5,7,6,5,6,1,4,4],'succ')", "17", r"Longueurs des listes : $3$ (case $5$), $2$ (cases $4,6,7$), $1$ (cases $1,9$). Total $6+3+3+3+1+1=17$. Classement : séparé ($17$) $<$ coalescent ($19$) $<$ double ($24$) $<$ linéaire ($40$)."),
    ]},
    {"n": 12, "titre": "Tables obtenues par insertions successives (annales)", "notions": ["sep", "lin", "coal"], "exos": [
        o("tl20", "Table de $m=11$ cases. Valeurs de hachage : data $4$, kirk $5$, neelix $3$, odo $1$, picard $7$, q $6$, quark $2$, sisko $7$, tuvok $1$, worf $7$. Représenter la table après l'ajout, dans cet ordre, de data jusqu'à worf, avec le hachage linéaire de décalage $d=4$.",
          sol_lin(11, H20, N20, 4)[0] + "\n\nCe tableau est celui du corrigé officiel.", src=S20 + ", ex. 1", duree=6),
        o("tl23", "Table de $m=11$ cases. Valeurs de hachage : aragog $0$, buck $1$, dobby $4$, fumseck $0$, missteigne $0$, nagini $5$, crockdur $2$, croutard $4$, kreattur $8$, hedwige $8$. Représenter la gestion des collisions pour l'ajout dans cet ordre (de aragog jusqu'à hedwige) avec le hachage linéaire de décalage $d=5$.",
          sol_lin(11, H23, N23, 5)[0] + "\n\nCe tableau est celui du corrigé officiel.", src=S23 + ", ex. 1", duree=6),
        o("tl24", "Table de $m=11$ cases. Valeurs de hachage : beck $10$, cale $10$, clapton $4$, hendrix $5$, hooker $6$, king $8$, richards $3$, vaughan $8$, winter $1$, young $5$. Représenter la table après l'ajout de beck jusqu'à young avec le hachage linéaire de décalage $d=3$.",
          sol_lin(11, H24, N24, 3)[0] + "\n\nCe tableau est celui du corrigé officiel.", src=S24 + ", ex. 1 (question 1)", duree=6),
        o("ts24", "Clés et valeurs de hachage (beck $10$, cale $10$, clapton $4$, hendrix $5$, hooker $6$, king $8$, richards $3$, vaughan $8$, winter $1$, young $5$, $m=11$). Représenter la table avec le hachage par chaînage séparé (insertion en fin de liste).",
          sol_sep(11, H24, N24)[0] + "\n\nL'ordre dans une liste dépend de la convention d'insertion (ici en fin de liste, ordre d'arrivée) ; les clés de chaque case sont celles du corrigé.", src=S24 + ", ex. 1 (question 2)", duree=4),
        o("tc28", r"Clés $15,24,125,4,26,6,78,55,89$, table de $m=12$ cases, $h(x)=x\bmod12$. 1. Donner les valeurs de hachage. 2. Remplir la table (colonnes elt et lien) après insertions successives dans cet ordre avec le hachage coalescent.",
          "**1.** Valeurs : " + ", ".join(f"$h({k})={h}$" for k, h in zip(K28, H28)) + ".\n\n**2.** " + sol_coal(12, H28, K28)[0]
          + "\n\nCorrigé rédigé (pas de corrigé officiel) : il a été produit par un simulateur contrôlé sur les corrigés officiels des contrôles de 2017 et 2020 (table coalescente de $11$ clés).", src=S28 + ", ex. 1", duree=6),
    ]},
    {"n": 13, "titre": "Questions de cours, tableaux valides et suppression", "notions": ["principe", "suppr"], "exos": [
        o("q1", r"1. Citer trois propriétés essentielles d'une fonction de hachage. 2. À quoi doit-on une collision secondaire ? 3. Collisions mises à part, quel phénomène provoque le hachage linéaire et que fait-on pour le résoudre ?",
          "1. Uniforme, déterministe, facile et rapide à calculer.\n\n2. Une collision secondaire vient de deux éléments qui se retrouvent en collision sur une case alors que leurs valeurs de hachage primaires sont différentes (hachage coalescent : une case de débordement est occupée par un élément d'une autre liste).\n\n3. Le hachage linéaire provoque le regroupement (accumulation d'éléments, clustering) ; on le résout avec le double hachage.",
          src=S20 + ", ex. 3", duree=4),
        o("q2", "1. Citer deux méthodes de hachage de base. 2. Quelle méthode de hachage génère des collisions secondaires ? 3. Quelle méthode résout le clustering du hachage linéaire ? 4. Citer une méthode utilisant une fonction d'essais successifs. 5. Quelle méthode de résolution des collisions n'exige pas un tableau de taille au moins égale au nombre de clés ?",
          "1. Parmi extraction, compression, division, multiplication (le corrigé officiel cite la quatrième sous un autre nom, le cours dit compression).\n\n2. Le hachage coalescent.\n\n3. Le double hachage.\n\n4. Le hachage linéaire ou le double hachage.\n\n5. Le chaînage séparé : les éléments en collision sont chaînés à l'extérieur du tableau, donc $n>m$ est possible.",
          src=S23 + ", ex. 2", duree=5),
        o("q3", r"Les clés A à G ont pour valeurs de hachage ($m=7$) : A $2$, B $0$, C $0$, D $4$, E $4$, F $4$, G $2$. On les insère dans un ordre quelconque, par hachage linéaire ($d=1$), dans un tableau vide de $7$ cases. Parmi les tableaux (A) C G B A D E F, (B) F G B D A C E, (C) B C A G E D F, (D) G E C A D B F (cases $0$ à $6$), lesquels ne peuvent pas résulter de ces insertions ?",
          "Seul (C) est possible ; (A), (B) et (D) sont impossibles.\n\n(C) : l'ordre B, E, A, C, D, F, G convient (B en 0, E en 4, A en 2, C en 0 puis 1, D en 4 puis 5, F en 4, 5 puis 6, G en 2 puis 3).\n\n(A) : G est en case $1$, valeur $2$ : il a examiné $2,3,4,5,6,0$ donc B (case 2, valeur $0$) était déjà placé. Mais B (valeur $0$) est en case $2$ : il a examiné $0$ et $1$, donc G (case $1$) était déjà placé. Contradiction.\n\n(B) : F (valeur $4$) est en case $0$ : il a examiné $4,5,6$ donc C (case $5$) était déjà placé. Mais C (valeur $0$) est en case $5$ : il a examiné $0,1,2,3,4$, donc F (case $0$) était déjà placé. Contradiction.\n\n(D) : E (valeur $4$) est en case $1$ : il a examiné $4,5,6,0$ donc B (case $5$) était déjà placé. Mais B (valeur $0$) est en case $5$ : il a examiné $0,1,2,3,4$, donc E (case $1$) était déjà placé. Contradiction.\n\nVérifié par énumération des $7!=5040$ ordres d'insertion (corrigé officiel : A, B, D impossibles).",
          src=S20 + ", ex. 2", duree=8),
        o("q4", r"Hachage linéaire ($d=1$), $m=7$, table vide. On insère A, B, C, D de valeurs $2,2,3,2$. On supprime B en marquant sa case « libre ». 1. Dessiner la table. 2. Combien de cases examine la recherche de D ? 3. Que se passerait-il si on avait rendu la case de B « vide » ? 4. On insère E de valeur $2$ : où va-t-il ?",
          "**1.** A en $2$ ; B ($h=2$ occupée) en $3$ ; C ($h=3$ occupée) en $4$ ; D ($h=2$) examine $2,3,4$ occupées puis $5$ : D en $5$. Table : case $2$ A, $3$ B, $4$ C, $5$ D, les autres vides. Après la suppression, la case $3$ est « libre ».\n\n**2.** D : $2$ (A, pas D), $3$ (libre : on continue), $4$ (C), $5$ (D trouvé) : $4$ cases.\n\n**3.** Avec une case « vide », la recherche de D s'arrêterait en $3$ et conclurait à tort que D est absent : on ne peut pas supprimer réellement (réorganisation nécessaire).\n\n**4.** On parcourt $2$ (A), $3$ (libre : on retient la première case libre), $4$, $5$ (D), $6$ (vide) : E n'est pas présent, on l'insère dans la première case libre rencontrée, la case $3$.\n\nLe marquage allonge les recherches : c'est le défaut de la suppression dans les méthodes par calcul et dans le coalescent ; seul le chaînage séparé supprime directement.",
          duree=6),
    ]},
]

# ------------------------------------------------ level 14: harder than the exam (own data, m = 13, three methods)
K14 = [18, 41, 22, 35, 9, 54, 67, 12, 26, 80]
H14 = [(5 * k + 3) % 13 for k in K14]
D14 = [1 + k % 12 for k in K14]
assert H14 == [2, 0, 9, 9, 9, 0, 0, 11, 3, 0]
_T14L = _lin(13, H14, [2] * 10)
_T14D = _lin(13, H14, D14)
_T14C = _coal(13, H14)
P14 = "Niveau au-dessus de l'examen (données de l'auteur, tables calculées par simulateur contrôlé sur les corrigés officiels)"

LEVELS += [
    {"n": 14, "titre": "Plus dur que l'examen : trois méthodes, collisions et coûts", "notions": ["lin", "dbl", "coal", "suppr", "charge"], "exos": [
        o("p1", r"Table de $m=13$ cases, $h(x)=(5x+3)\bmod13$, clés $18,41,22,35,9,54,67,12,26,80$ insérées dans cet ordre. 1. Donner les valeurs de hachage. 2. Dessiner la table obtenue avec le hachage linéaire de décalage $d=2$. 3. Même question avec le double hachage $d(x)=1+(x\bmod12)$. 4. Même question avec le hachage coalescent sans réserve ; combien de collisions primaires et secondaires ?",
          "**1.** " + ", ".join(f"$h({k})={h}$" for k, h in zip(K14, H14)) + ".\n\n**2. Linéaire ($d=2$).** " + sol_lin(13, H14, K14, 2)[0] + "\n\n**3. Double hachage.** " + sol_dbl(13, H14, D14, K14)[0] + "\n\n**4. Coalescent.** " + sol_coal(13, H14, K14)[0]
          + f"\n\nCollisions : {sum(1 for i in _T14C[2] if i[0] == 'primaire')} primaires et {sum(1 for i in _T14C[2] if i[0] == 'secondaire')} secondaire(s).", src=None, duree=12),
        v("p2", r"Table de $m=13$ cases, dix clés insérées dans cet ordre, de valeurs de hachage $2,0,9,9,9,0,0,11,3,0$. Hachage linéaire $d=2$ : coût moyen d'une recherche réussie (cases examinées, chaque clé cherchée une fois) ?",
          "Rational(hach('lin',13,[2,0,9,9,9,0,0,11,3,0],'succ',d=2),10)", "Rational(17,5)",
          r"Somme des rangs d'essai de chaque clé à l'insertion : $34$ cases examinées au total pour $10$ clés, soit $\frac{34}{10}=\frac{17}5$. En double hachage le total tombe à $20$ ($2$ en moyenne)."),
        v("p3", r"Table de $m=13$ cases, dix clés insérées dans cet ordre, de valeurs de hachage $2,0,9,9,9,0,0,11,3,0$, double hachage avec les pas $d(x)=7,6,11,12,10,7,8,1,3,9$ (dans l'ordre des clés). Dans quelle case arrive la dernière clé, $80$ ($h=0$) ?",
          "hach('dbl',13,[2,0,9,9,9,0,0,11,3,0],'pos',ds=[7,6,11,12,10,7,8,1,3,9])", "5",
          r"Pas de $80$ : $d=9$ (dernier pas de la liste). Essais : $0$ (occupée), $(0+9)\bmod13=9$ (occupée), $(0+18)\bmod13=5$ libre : case $5$ (en $3$ essais)."),
        o("p4", r"Hachage linéaire $d=1$, $m=11$, table vide. On insère, dans cet ordre, les clés $a,b,c,d,e$ de valeurs de hachage $3,3,4,3,5$. On supprime $b$ (case marquée libre), puis on cherche $d$, puis on insère $f$ de valeur $3$, enfin on cherche $e$. Pour chaque opération, donner les cases examinées et l'état de la table.",
          "**Insertions.** a en $3$ ; b ($h=3$ occupée) en $4$ ; c ($h=4$ occupée) en $5$ ; d ($h=3$) : $3,4,5$ occupées, en $6$ ; e ($h=5$) : $5,6$ occupées, en $7$. Table : $3$ a, $4$ b, $5$ c, $6$ d, $7$ e.\n\n**Suppression de b** : la case $4$ devient libre (pas vide).\n\n**Recherche de d** : $3$ (a), $4$ (libre, on continue), $5$ (c), $6$ (d trouvé) : $4$ cases.\n\n**Insertion de f** ($h=3$) : $3$ (a), $4$ (libre : première case libre retenue), $5$ (c), $6$ (d), $7$ (e), $8$ (vide) : f n'est pas présent, on l'insère dans la case libre $4$. Table : $3$ a, $4$ f, $5$ c, $6$ d, $7$ e. $6$ cases examinées.\n\n**Recherche de e** ($h=5$) : $5$ (c), $6$ (d), $7$ (e) : $3$ cases.",
          src=None, duree=10),
    ]},
]

# ------------------------------------------------ exam level: real exercises (multi), parts from levels or EXTRA_PARTS
EXTRA_PARTS = [
    o("ts25", "Valeurs de hachage : data $4$, kirk $5$, neelix $3$, odo $1$, picard $7$, q $6$, quark $2$, sisko $7$, tuvok $1$, worf $7$ ($m=11$). Représenter la table obtenue par chaînage séparé (insertion en fin de liste).",
      sol_sep(11, H20, N20)[0], src=S25 + ", ex. 1 (question 2)"),
    o("tl25", "Mêmes clés et valeurs que ci-dessus ($m=11$). Représenter la table après l'ajout de data jusqu'à worf avec le hachage linéaire de décalage $d=3$.",
      sol_lin(11, H20, N20, 3)[0] + "\n\nCe tableau est celui du corrigé officiel.", src=S25 + ", ex. 1 (question 1)"),
    o("tc21", r"$m=11$, $h(x)=(2x+5)\bmod11$, clés $12,44,13,88,23,94,11,39,20,16,5$. Représenter la table de hachage correspondante, les collisions étant résolues par hachage coalescent.",
      sol_coal(11, H21, K21)[0] + "\n\nCe tableau est celui du corrigé officiel.", src=S21 + ", ex. 1 (question 1)"),
    o("tl21", "Mêmes clés et même fonction $h(x)=(2x+5)\\bmod11$. Représenter la table obtenue par hachage linéaire (décalage $d=1$).",
      sol_lin(11, H21, K21, 1)[0] + "\n\nCe tableau est celui du corrigé officiel.", src=S21 + ", ex. 1 (question 2)"),
    o("td21", "Mêmes clés. Collisions résolues par double hachage avec $d(x)=7-(x\\bmod7)$ ; représenter la table obtenue.",
      sol_dbl(11, H21, D21, K21)[0] + "\n\nCe tableau est celui du corrigé officiel.", src=S21 + ", ex. 1 (question 3)"),
]

LEVELS += [
    {"n": 15, "titre": "Examens : annales de hachage", "notions": ["principe", "division", "sep", "lin", "dbl", "coal", "suppr"], "exos": [
        {"id": "ex1", "kind": "multi", "parts": ["tl20", "q3", "q1"], "enonce": "Contrôle n°3 d'algo S3 (24 octobre 2016), partie « Du hachage » : hachage linéaire sur dix clés, tableaux valides et questions de cours.", "src": S20},
        {"id": "ex2", "kind": "multi", "parts": ["tl23", "q2"], "enonce": "Contrôle n°3 d'algo S3# (5 mars 2019), hachage : table linéaire de décalage $d=5$ et questions de cours.", "src": S23},
        {"id": "ex3", "kind": "multi", "parts": ["tl24", "ts24"], "enonce": "Contrôle n°3 d'algo S3# (10 mars 2020), exercice 1 : une même série de clés rangée avec le hachage linéaire ($d=3$) puis le chaînage séparé.", "src": S24},
        {"id": "ex4", "kind": "multi", "parts": ["tl25", "ts25", "tc28"], "enonce": "Contrôle n°3 d'algo S3# (17 mars 2021, exercice 1) puis Examen B5 AR2 (22 octobre 2024, exercice 1) : linéaire $d=3$, chaînage séparé et hachage coalescent.", "src": S25 + " ; " + S28},
        {"id": "ex5", "kind": "multi", "parts": ["tc21", "tl21", "td21"], "enonce": "Contrôle n°3 d'algo S3 (7 novembre 2017), exercice 1 « Quelques résultats différents » : trois méthodes de résolution des collisions sur les mêmes onze clés.", "src": S21},
    ]},
]

VARIANTS = {
    "m1": [{"enonce": r"Calculer $200\bmod7$.", "calc": "200%7", "ans": "4", "sol": r"$200=28\times7+4$ donc $4$."}],
    "m2": [{"enonce": r"Calculer $(5\times9+3)\bmod7$.", "calc": "(5*9+3)%7", "ans": "6", "sol": r"$48=6\times7+6$ donc $6$."}],
    "m3": [{"enonce": r"Reste de la division euclidienne de $-9$ par $4$ ?", "calc": "(-9)%4", "ans": "3", "sol": r"$-9=-3\times4+3$ donc $3$."}],
    "m4": [{"enonce": r"Calculer $3^8\bmod5$.", "calc": "3**8%5", "ans": "1", "sol": r"$3^4=81\equiv1\pmod5$ donc $3^8\equiv1$."}],
    "m5": [{"enonce": r"Calculer $(25+4\times6)\bmod7$.", "calc": "(25+4*6)%7", "ans": "0", "sol": r"$25+24=49=7\times7$ donc $0$."}],
    "t1": [{"enonce": r"On cherche séquentiellement une clé présente dans une liste non triée de $n=99$ éléments, chaque position étant équiprobable. Combien de comparaisons en moyenne ?", "calc": "Rational(99+1,2)", "ans": "50", "sol": r"$\frac{99+1}2=50$."}],
    "t2": [{"enonce": r"Combien de comparaisons au pire pour constater qu'une clé est absente d'une liste non triée de $37$ éléments ?", "calc": "37", "ans": "37", "sol": r"Les $37$ éléments."}],
    "t3": [{"enonce": r"Un tableau contient $15$ éléments (il reste de la place). Combien d'éléments faut-il décaler pour insérer un nouvel élément en première position ?", "calc": "15", "ans": "15", "sol": r"$15$ décalages."}],
    "t4": [{"enonce": r"Combien de liens pour atteindre le $15$-ème maillon ?", "calc": "15-1", "ans": "14", "sol": r"$k-1=14$."}],
    "d1": [{"enonce": r"Avec $h(x)=x\bmod13$, calculer $h(200)$.", "calc": "200%13", "ans": "5", "sol": r"$200=15\times13+5$ donc $5$."}],
    "d2": [{"enonce": r"Avec $m=7$ et $h(x)=(3x+1)\bmod7$, calculer $h(50)$.", "calc": "(3*50+1)%7", "ans": "4", "sol": r"$151=21\times7+4$ donc $4$."}],
    "d3": [{"enonce": r"$m=10$, $h(x)=x\bmod10$, clés $13,23,33,14,25,35$. Combien de collisions ?", "calc": "hach('sep',10,[3,3,3,4,5,5],'coll')", "ans": "3",
            "sol": r"Valeurs $3,3,3,4,5,5$ : $4$ cases utilisées pour $6$ clés, $6-3=3$ collisions."}],
    "d4": [{"enonce": r"Les clés $3,6,9,\dots,30$ (dix clés) sont rangées avec $h(x)=x\bmod12$. Combien de collisions ?", "calc": "hach('sep',12,[3,6,9,0,3,6,9,0,3,6],'coll')", "ans": "6",
            "sol": r"Valeurs $3,6,9,0,3,6,9,0,3,6$ : seulement $4$ cases utilisées, $10-4=6$ collisions ($m=12$ a des diviseurs communs avec $3$)."}],
    "x1": [{"enonce": r"Multiplication, $\theta=0{,}7$, $m=10$ : calculer $h(9)$.", "calc": "floor((9*Rational(7,10))%1*10)", "ans": "3", "sol": r"$9\times0{,}7=6{,}3$, décimale $0{,}3$, $h=3$."}],
    "x2": [{"enonce": r"Multiplication, $\theta=0{,}37$, $m=20$ : calculer $h(18)$.", "calc": "floor((18*Rational(37,100))%1*20)", "ans": "13", "sol": r"$18\times0{,}37=6{,}66$, décimale $0{,}66$, $0{,}66\times20=13{,}2$ : $13$."}],
    "x3": [{"enonce": r"On extrait les $3$ bits de poids faible de la clé $11010101_2$. Valeur de hachage ?", "calc": "bits('11010101')%8", "ans": "5", "sol": r"Les trois derniers bits : $101_2=5$."}],
    "x4": [{"enonce": r"On extrait les bits $3,4,5$ de la clé $11100010_2$. Valeur de hachage ?", "calc": "(bits('11100010')//2**3)%2**3", "ans": "4", "sol": r"Décalage de $3$ bits : $11100_2$, puis $3$ bits : $100_2=4$."}],
    "x5": [{"enonce": r"$\theta=0{,}01$ (trop proche de $0$), $m=10$, clés $1,\dots,6$. Combien de collisions ?", "calc": "hach('sep',10,[0,0,0,0,0,0],'coll')", "ans": "5",
            "sol": r"$e\theta\le0{,}06$ donc $h=0$ pour les six clés : $5$ collisions."}],
    "c1": [{"enonce": r"Clé « CD » (codes $67$ et $68$), $m=13$, somme des codes.", "calc": "(67+68)%13", "ans": "5", "sol": r"$135=10\times13+5$ donc $5$."}],
    "c2": [{"enonce": r"Clé « OUI » (O=79, U=85, I=73), $m=7$, somme des codes.", "calc": "(79+85+73)%7", "ans": "6", "sol": r"$237=33\times7+6$ donc $6$."}],
    "c3": [{"enonce": r"Clés SEL et LES (S=83, E=69, L=76), $m=11$, somme des codes. Combien de collisions ?", "calc": "hach('sep',11,[8,8],'coll')", "ans": "1",
            "sol": r"Somme $228=20\times11+8$ pour les deux : $h=8$, une collision (anagrammes)."}],
    "c4": [{"enonce": r"Compression par OU exclusif : $1100\oplus1010$ en décimal ?", "calc": "(1+1)%2*8+(1+0)%2*4+(0+1)%2*2+(0+0)%2", "ans": "6", "sol": r"Bit par bit : $0,1,1,0$ soit $0110_2=6$."}],
    "a1": [{"enonce": r"$n=14$ clés dans $m=35$ cases : facteur de charge ?", "calc": "Rational(14,35)", "ans": "Rational(2,5)", "sol": r"$\alpha=\frac{14}{35}=\frac25$."}],
    "a2": [{"enonce": r"$n=45$ clés dans $m=12$ cases : facteur de charge ?", "calc": "Rational(45,12)", "ans": "Rational(15,4)", "sol": r"$\alpha=\frac{45}{12}=\frac{15}4>1$."}],
    "a3": [{"enonce": r"Table de $m=31$ cases après $20$ insertions (linéaire, sans suppression). Cases vides ?", "calc": "31-20", "ans": "11", "sol": r"$31-20=11$."}],
    "a4": [{"enonce": r"Chaînage séparé, $m=2$, cinq clés de valeurs $0,0,0,0,1$ (insertion en fin de liste). Coût moyen d'une recherche réussie ?", "calc": "Rational(hach('sep',2,[0,0,0,0,1],'succ'),5)", "ans": "Rational(11,5)",
            "sol": r"Liste de $4$ clés : $1+2+3+4=10$ ; liste de $1$ clé : $1$. Total $11$ pour $5$ clés : $\frac{11}5$."}],
    "a5": [{"enonce": r"Au minimum, combien de collisions pour $n=40$ clés dans $m=16$ cases ?", "calc": "40-16", "ans": "24", "sol": r"$n-m=24$."}],
    "s1": [{"enonce": r"$m=11$, chaînage séparé, clés de valeurs $2,5,2,9,5,2,0$. Longueur de la plus longue liste ?", "calc": "hach('sep',11,[2,5,2,9,5,2,0],'maxlen')", "ans": "3", "sol": r"La case $2$ contient $3$ clés."}],
    "s2": [{"enonce": r"$m=11$, chaînage séparé, clés de valeurs $7,5,9,5,7,6,5,6,1,4,4$. Longueur de la plus longue liste ?", "calc": "hach('sep',11,[7,5,9,5,7,6,5,6,1,4,4],'maxlen')", "ans": "3", "sol": r"La case $5$ contient $3$ clés."}],
    "s3": [{"enonce": r"Clés de valeurs $2,5,2,9,5,2,0$ ($m=11$, fin de liste). Nombre total de clés examinées pour retrouver chaque clé une fois ?", "calc": "hach('sep',11,[2,5,2,9,5,2,0],'succ')", "ans": "11", "sol": r"Case $2$ : $1+2+3=6$ ; case $5$ : $1+2=3$ ; cases $9$ et $0$ : $1$ chacune. Total $11$."}],
    "s4": [{"enonce": r"Clés de valeurs $2,5,2,9,5,2,0$, $m=11$. Combien de cases vides ?", "calc": "11-(7-hach('sep',11,[2,5,2,9,5,2,0],'coll'))", "ans": "7", "sol": r"$3$ collisions donc $4$ cases utilisées, $11-4=7$ vides."}],
    "l1": [{"enonce": r"Hachage linéaire $m=13$, $d=3$, $h=5$ : case du $4$-ème essai ?", "calc": "(5+3*(4-1))%13", "ans": "1", "sol": r"$(5+9)\bmod13=1$."}],
    "l2": [{"enonce": r"Hachage linéaire, $m=11$, $d=3$. Les clés de valeurs $4,5,3,1,7,6,2$ sont déjà placées (dans cet ordre, table vide au départ). On insère sisko, de valeur $7$. Dans quelle case ?", "calc": "hach('lin',11,[4,5,3,1,7,6,2,7],'pos',d=3)", "ans": "10", "sol": r"$7$ occupée, $(7+3)\bmod11=10$ libre."}],
    "l3": [{"enonce": r"Hachage linéaire, $m=11$, $d=3$, dix clés de valeurs $4,5,3,1,7,6,2,7,1,7$ insérées dans cet ordre. Dans quelle case arrive la dernière (worf, de valeur $7$) ?", "calc": "hach('lin',11,[4,5,3,1,7,6,2,7,1,7],'pos',d=3)", "ans": "0", "sol": r"Worf teste $7,10,2,5,8,0$ ($10$ est sisko) : case $0$ (voir la table du corrigé)."}],
    "l4": [{"enonce": r"Hachage linéaire $m=11$, $d=4$, clés de valeurs $4,5,3,1,7,6,2,7,1,7$. Nombre total de cases examinées pour insérer les dix clés ?", "calc": "hach('lin',11,[4,5,3,1,7,6,2,7,1,7],'probes',d=4)", "ans": "16", "sol": r"Sept clés : $7$ ; sisko $2$ ; tuvok : $1,5,9$ soit $3$ ; worf : $7,0,4,8$ soit $4$. Total $7+2+3+4=16$."}],
    "l5": [{"enonce": r"Valeurs $4,5,3,1,7,6,2,7,1,7$, $m=11$, $d=4$ : combien de clés trouvent leur case $h$ occupée ?", "calc": "hach('lin',11,[4,5,3,1,7,6,2,7,1,7],'coll',d=4)", "ans": "3", "sol": r"Sisko, tuvok, worf : $3$."}],
    "b1": [{"enonce": r"$m=11$, $h(x)=(2x+5)\bmod11$ et $d(x)=7-(x\bmod7)$ : case du $4$-ème essai de $x=39$ ?", "calc": "((2*39+5)%11+(7-39%7)*3)%11", "ans": "4", "sol": r"$h(39)=83\bmod11=6$, $d(39)=7-4=3$ ; $(6+9)\bmod11=4$."}],
    "b2": [{"enonce": r"$m=15$, $d(x)=6$ : combien de cases distinctes visitées ?", "calc": "15/gcd(15,6)", "ans": "5", "sol": r"$\frac{15}{\gcd(15,6)}=\frac{15}3=5$."}],
    "b3": [{"enonce": r"$m=7$, valeurs $3,3,3,5$, pas $1,2,3,1$ (double hachage). Où arrive la dernière clé ?", "calc": "hach('dbl',7,[3,3,3,5],'pos',ds=[1,2,3,1])", "ans": "0",
            "sol": r"Les trois premières en $3$, $5$ ($3+2$), $6$ ($3+3$). La dernière : $5$ occupée, $6$ occupée, $0$ libre."}],
    "b4": [{"enonce": r"$m=7$, valeurs de hachage $3,3,3,5$ insérées dans cet ordre, double hachage de pas $1,2,3,1$ : nombre total de cases examinées ?", "calc": "hach('dbl',7,[3,3,3,5],'probes',ds=[1,2,3,1])", "ans": "8", "sol": r"$1+2+2+3=8$."}],
    "b5": [{"enonce": r"$m=16$, $d(x)=2(x\bmod8)+1$ : case du $4$-ème essai de $x=30$ ?", "calc": "(30%16+(2*(30%8)+1)*3)%16", "ans": "5", "sol": r"$h=14$, $d=2\times6+1=13$ ; $(14+39)\bmod16=53\bmod16=5$."}],
    "k1": [{"enonce": r"Coalescent, $m=7$, valeurs $3,3,1,3,6$ : où arrive la dernière clé ?", "calc": "hach('coal',7,[3,3,1,3,6],'pos')", "ans": "4",
            "sol": r"2e clé en $6$ (lien de $3$), 3e en $1$, 4e en $5$ (lien de $6$). 5e ($h=6$ occupée) : $6,5$ occupées, $4$ libre : case $4$."}],
    "k2": [{"enonce": r"Hachage coalescent, $m=7$, valeurs $3,3,1,3,6$ insérées dans cet ordre : valeur du lien de la case $3$ ?", "calc": "hach('coal',7,[3,3,1,3,6],'lien')[3]", "ans": "6", "sol": r"Le premier suivant de la case $3$ est en case $6$."}],
    "k3": [{"enonce": r"Coalescent, $m=7$, valeurs $3,3,1,3,6$ : combien de collisions secondaires ?", "calc": "hach('coal',7,[3,3,1,3,6],'sec')", "ans": "1", "sol": r"La 5e clé ($h=6$) trouve la case $6$ occupée par une clé de valeur $3$ : $1$ secondaire (les deux autres collisions sont primaires)."}],
    "k4": [{"enonce": r"Coalescent, $m=7$, valeurs $1,1,2,2,1,3$. Combien de collisions primaires ?", "calc": "hach('coal',7,[1,1,2,2,1,3],'prim')", "ans": "3", "sol": r"Les clés $2,4,5$ trouvent une case occupée par une clé de même valeur : $3$ primaires, aucune secondaire."}],
    "k5": [{"enonce": r"Coalescent, $m=11$, valeurs $4,5,3,1,7,6,2,7,1,7$ : coût total de recherche (rang de chaque clé dans sa liste) ?", "calc": "hach('coal',11,[4,5,3,1,7,6,2,7,1,7],'succ')", "ans": "14",
            "sol": r"Les clés de la case $7$ ont les rangs $1,2,3$ ; celles de la case $1$ les rangs $1,2$ ; les cinq autres : $1$ chacune. Total $6+3+5=14$."}],
    "u1": [{"enonce": r"Valeurs $4,5,3,1,7,6,2,7,1,7$, $m=11$, linéaire $d=3$ : coût total pour retrouver chaque clé ?", "calc": "hach('lin',11,[4,5,3,1,7,6,2,7,1,7],'succ',d=3)", "ans": "22", "sol": r"Total des essais à l'insertion : $22$."}],
    "u2": [{"enonce": r"Valeurs $4,5,3,1,7,6,2,7,1,7$, $m=11$, double hachage avec les pas $1,1,1,1,1,1,1,3,2,4$ : coût total ?", "calc": "hach('dbl',11,[4,5,3,1,7,6,2,7,1,7],'succ',ds=[1,1,1,1,1,1,1,3,2,4])", "ans": "16",
            "sol": r"Sept clés : $7$ ; sisko : $7,10$ ($2$) ; tuvok : $1,3,5,7,9$ ($5$) ; worf : $7,0$ ($2$). Total $7+2+5+2=16$."}],
    "u3": [{"enonce": r"Valeurs $4,5,3,1,7,6,2,7,1,7$, $m=11$, coalescent : coût total ?", "calc": "hach('coal',11,[4,5,3,1,7,6,2,7,1,7],'succ')", "ans": "14", "sol": r"Total $14$ (voir exercice précédent)."}],
    "u4": [{"enonce": r"Valeurs $4,5,3,1,7,6,2,7,1,7$, $m=11$, chaînage séparé : coût total ?", "calc": "hach('sep',11,[4,5,3,1,7,6,2,7,1,7],'succ')", "ans": "14", "sol": r"Liste de $3$ : $6$ ; liste de $2$ : $3$ ; cinq listes de $1$ : $5$. Total $14$."}],
    "p2": [{"enonce": r"Table de $m=13$ cases, dix clés insérées dans cet ordre, de valeurs de hachage $2,0,9,9,9,0,0,11,3,0$, double hachage (pas $7,6,11,12,10,7,8,1,3,9$) : coût moyen ?", "calc": "Rational(hach('dbl',13,[2,0,9,9,9,0,0,11,3,0],'succ',ds=[7,6,11,12,10,7,8,1,3,9]),10)", "ans": "2", "sol": r"Total $20$ cases examinées pour $10$ clés : $2$."}],
    "p3": [{"enonce": r"Table de $m=13$ cases, dix clés insérées dans cet ordre, de valeurs de hachage $2,0,9,9,9,0,0,11,3,0$, hachage coalescent : dans quelle case arrive la dernière clé ($80$) ?", "calc": "hach('coal',13,[2,0,9,9,9,0,0,11,3,0],'pos')", "ans": "6", "sol": r"$80$ ($h=0$) : liste de la case $0$ : $0\to10\to8$, collision primaire ; première case libre depuis la fin : $6$."}],
}
for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["id"] in VARIANTS:
            _e["variants"] = VARIANTS[_e["id"]]

QUIZ = [
    {"notion": "modulo", "type": "qcm", "q": r"Le reste de la division euclidienne de $-7$ par $5$ est", "choix": [r"$3$", r"$-2$", r"$2$", r"$-3$"], "bonne": 0},
    {"notion": "modulo", "type": "vf", "q": r"$(a+b)\bmod m=((a\bmod m)+(b\bmod m))\bmod m$.", "bonne": True},
    {"notion": "tab", "type": "vf", "q": r"Insérer en première position d'un tableau de $n$ éléments coûte $O(1)$.", "bonne": False},
    {"notion": "tab", "type": "qcm", "q": r"Nombre moyen de comparaisons d'une recherche séquentielle réussie dans $n$ éléments (positions équiprobables)", "choix": [r"$\frac{n+1}2$", r"$n$", r"$\log_2n$", r"$1$"], "bonne": 0},
    {"notion": "principe", "type": "vf", "q": r"Une fonction de hachage doit être universelle.", "bonne": False},
    {"notion": "principe", "type": "qcm", "q": r"Parmi ces propriétés, lesquelles doit avoir une fonction de hachage ?", "choix": [r"uniforme, rapide à calculer, déterministe", r"universelle, injective, aléatoire", r"croissante, récursive, aléatoire", r"injective, universelle, lente"], "bonne": 0},
    {"notion": "principe", "type": "vf", "q": r"Une collision primaire correspond à deux clés différentes de même valeur de hachage.", "bonne": True},
    {"notion": "division", "type": "qcm", "q": r"Avec $h(x)=x\bmod11$, $h(125)=$", "choix": [r"$4$", r"$5$", r"$3$", r"$11$"], "bonne": 0},
    {"notion": "division", "type": "vf", "q": r"Avec $m=10$ et des clés multiples de $5$, la division n'utilise que deux cases.", "bonne": True},
    {"notion": "multi-ext", "type": "vf", "q": r"L'extraction utilise toute la représentation de la clé.", "bonne": False},
    {"notion": "multi-ext", "type": "qcm", "q": r"Dans la multiplication $h(e)=\lfloor((e\theta)\bmod1)\,m\rfloor$, un $\theta$ trop proche de $0$ ou de $1$", "choix": [r"accumule les clés aux extrémités du tableau", r"répartit parfaitement les clés", r"rend $h$ injective", r"rend $m$ inutile"], "bonne": 0},
    {"notion": "compression", "type": "qcm", "q": r"Le handicap majeur de la compression est de", "choix": [r"hacher de la même façon les anagrammes d'une clé", r"n'utiliser qu'une partie de la clé", r"nécessiter un majorant du nombre de clés", r"ne marcher que pour peu de données"], "bonne": 0},
    {"notion": "compression", "type": "vf", "q": r"On préfère le OU exclusif au ET et au OU pour combiner les sous-mots.", "bonne": True},
    {"notion": "charge", "type": "qcm", "q": r"$n=15$ clés dans $m=20$ cases : $\alpha=$", "choix": [r"$\frac34$", r"$\frac43$", r"$5$", r"$\frac15$"], "bonne": 0},
    {"notion": "charge", "type": "vf", "q": r"Avec $\alpha>1$, seul le chaînage séparé permet de ranger toutes les clés.", "bonne": True},
    {"notion": "sep", "type": "vf", "q": r"Le chaînage séparé peut produire des collisions secondaires.", "bonne": False},
    {"notion": "sep", "type": "qcm", "q": r"La méthode la plus performante est", "choix": [r"le chaînage séparé", r"le hachage linéaire", r"le double hachage", r"le hachage coalescent"], "bonne": 0},
    {"notion": "lin", "type": "qcm", "q": r"Le hachage linéaire de pas $d$, $m=11$, $h=7$, $d=4$ : le $2$-ème essai est la case", "choix": [r"$0$", r"$11$", r"$4$", r"$7$"], "bonne": 0},
    {"notion": "lin", "type": "vf", "q": r"Le hachage linéaire provoque un regroupement (clustering) des éléments.", "bonne": True},
    {"notion": "dbl", "type": "qcm", "q": r"Pour que les essais du double hachage visitent toutes les cases, il faut", "choix": [r"$\gcd(d(x),m)=1$", r"$d(x)=m$", r"$d(x)$ pair", r"$m$ pair"], "bonne": 0},
    {"notion": "dbl", "type": "vf", "q": r"Avec $m=2^p$, un pas $d(x)$ impair garantit que les $m$ essais sont distincts.", "bonne": True},
    {"notion": "coal", "type": "vf", "q": r"Seul le hachage coalescent génère des collisions secondaires.", "bonne": True},
    {"notion": "coal", "type": "qcm", "q": r"En coalescent sans réserve, une clé en collision est placée dans", "choix": [r"la première case libre en partant de la fin du tableau", r"la case suivante", r"la première case du tableau", r"une liste hors du tableau"], "bonne": 0},
    {"notion": "suppr", "type": "vf", "q": r"Pour supprimer en hachage linéaire, on rend la case « vide » pour libérer la place.", "bonne": False},
    {"notion": "suppr", "type": "qcm", "q": r"La méthode qui supporte le mieux les suppressions est", "choix": [r"le chaînage séparé", r"le hachage linéaire", r"le double hachage", r"le hachage coalescent"], "bonne": 0},
]

_LEVEL_FORMULES = {
    1: r"$a=bq+r$ · $0\le r<b$ · $(a+b)\bmod m$",
    2: r"accès $O(1)$ · recherche séquentielle $\frac{n+1}2$ en moyenne · liste chaînée : $k-1$ liens",
    3: r"$h(x)=x\bmod m$ · $h(x)=(ax+b)\bmod m$ · collision : $h(x)=h(y)$",
    4: r"$h(e)=\lfloor((e\theta)\bmod1)\,m\rfloor$ · extraction : $x\bmod2^p$",
    5: r"somme des codes $\bmod m$ · OU exclusif bit à bit · anagrammes",
    6: r"$\alpha=\frac nm$ · au moins $n-m$ collisions · coût moyen $=\frac{\text{somme des rangs}}n$",
    7: r"case $i$ : liste des clés de valeur $i$ · recherche séquentielle dans la liste",
    8: r"$\text{essai}_i=(h+d(i-1))\bmod m$ · case vide : on insère",
    9: r"$\text{essai}_i=(h(x)+d(x)(i-1))\bmod m$ · $\gcd(d,m)=1$",
    10: r"coalescent sans réserve : case libre depuis $m-1$ · collision primaire / secondaire · lien",
    11: r"coût = somme des rangs de recherche · séparé $<$ coalescent $<$ double $<$ linéaire",
    12: r"essais successifs · chaînage dans le tableau (elt, lien) · listes hors du tableau",
    13: r"case libre : on continue la recherche · insertion : première case libre retenue · uniforme, déterministe, rapide",
    14: r"$\alpha=\frac nm$ · linéaire · double hachage · coalescent · marquage des cases libres",
}
FORMULES = {e["id"]: _LEVEL_FORMULES[lvl["n"]] for lvl in LEVELS for e in lvl["exos"] if e["kind"] != "multi"}
FORMULES.update({
    "tl25": _LEVEL_FORMULES[12], "ts25": _LEVEL_FORMULES[12], "tc21": _LEVEL_FORMULES[12], "tl21": _LEVEL_FORMULES[12], "td21": _LEVEL_FORMULES[12],
    "d5": r"uniforme · rapide à calculer · déterministe · $m$ premier",
})
