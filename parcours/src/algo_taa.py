"""Level path: S1 algorithmics, abstract algebraic types (TAA): signature, hierarchy, axioms, lists, stacks, queues, sets.

Sources: the Moodle course « [algo] TAA - Types algébriques abstraits » (course sheet, [doc] pages of the full abstract
types, « Exercice d'application » on booleans) and the public EPITA algorithmics wiki the course links to
(https://algo.infoprepa.epita.fr, pages « Types abstraits », « Structures séquentielles », « Ensembles »).
Exam levels come from Past-Exams (Epidocs): B1 of 30 Oct 2024 (S1/Midterms/Algo/2029/TAA), B2 of 9 Jan 2024
(S1/Finals/Algo/2028/TAA, scan; the « correction » file there is a student copy marked 9/10, used as the reference) and
B2 of 7 Jan 2025 (S1/Finals/Algo/2029/TAA, no correction). The B2 also tests stacks/queues output orders and searching,
so level 13 trains those. Their answers are computed below (`_out_bad`, `_calls`, `_path_bad`) and asserted.

Every « evaluate this term » exercise is checked by a small model of the types below (`_NS`): build.py imports this
module, so a wrong hand-written answer stops the build (assert). Conventions of the Moodle course: cons(e, l) puts e in
front; a stack is written with nested empiler, a queue with nested enfiler, an iterative list as ⟨a, b, c⟩.
« indéfini » is the answer when a precondition is violated.
"""

SUBJECT = {
    "id": "algo-s1-taa",
    "ordre": 600,
    "matiere": "algo",
    "semestre": "S1",
    "ecue": "Types algébriques abstraits",
    "titre": "Types algébriques abstraits : listes, piles, files, ensembles",
    "chapitres_moodle": [
        "[algo] TAA - Types algébriques abstraits/04_👨‍🏫 I - Types abstraits [FR]",
        "[algo] TAA - Types algébriques abstraits/05_👨‍🏫 II - Les listes [FR]",
        "[algo] TAA - Types algébriques abstraits/06_👨‍🏫 II - Les piles - files et ensembles [FR]",
    ],
    "td": "MiMos et questions du cours, exercice d'application (booléen)",
    "examens": ["Examen B1 de TAA (fin octobre, 30 min)", "Examen B2 de TAA (janvier, 30 min)"],
}

# ---------------------------------------------------------------- model of the abstract types (build-time check)


class Undefined(Exception):
    pass


def _need(cond):
    if not cond:
        raise Undefined


def _place_content(p):
    _need(0 <= p[1] < len(p[0]))
    return p[0][p[1]]


def _remove_one(x, me):
    if x not in me:
        return me
    i = me.index(x)
    return me[:i] + me[i + 1:]


_COMMON = {"Vrai": True, "Faux": False}
_NS = {
    "pile": {"pilevide": (), "empiler": lambda p, e: p + (e,), "dépiler": lambda p: (_need(p), p[:-1])[1],
             "sommet": lambda p: (_need(p), p[-1])[1], "estvide": lambda p: not p, "hauteur": len},
    "file": {"filevide": (), "enfiler": lambda f, e: f + (e,), "défiler": lambda f: (_need(f), f[1:])[1],
             "premier": lambda f: (_need(f), f[0])[1], "estvide": lambda f: not f},
    "lrec": {"listevide": (), "cons": lambda e, l: (e,) + l, "fin": lambda l: (_need(l), l[1:])[1],
             "premier": lambda l: (_need(l), l[0])[1], "tête": lambda l: (_need(l), (l, 0))[1],
             "contenu": _place_content, "succ": lambda p: (p[0], p[1] + 1),
             "concaténer": lambda a, b: a + b, "existe": lambda e, l: e in l, "longueur": len},
    "liter": {"listevide": (), "longueur": len,
              "ième": lambda l, k: (_need(1 <= k <= len(l)), l[k - 1])[1],
              "insérer": lambda l, k, e: (_need(1 <= k <= len(l) + 1), l[:k - 1] + (e,) + l[k - 1:])[1],
              "supprimer": lambda l, k: (_need(1 <= k <= len(l)), l[:k - 1] + l[k:])[1],
              "accès": lambda l, k: (_need(1 <= k <= len(l)), (l, k - 1))[1],
              "contenu": _place_content, "succ": lambda p: (p[0], p[1] + 1)},
    "ens": {"ensemblevide": frozenset(), "ajouter": lambda x, e: e | {x}, "supprimer": lambda x, e: e - {x},
            "appartient": lambda x, e: x in e, "card": len},
    "multi": {"multiensemblevide": (), "ajouter": lambda x, me: me + (x,), "supprimer": _remove_one,
              "appartient": lambda x, me: x in me, "card": len, "nboccurrences": lambda x, me: me.count(x)},
}


def _show(ns, r):
    if isinstance(r, bool):
        return "Vrai" if r else "Faux"
    if isinstance(r, int):
        return str(r)
    if ns == "pile":
        out = "pilevide"
        for e in r:
            out = f"empiler({out}, {e})"
        return out
    if ns == "file":
        out = "filevide"
        for e in r:
            out = f"enfiler({out}, {e})"
        return out
    if ns == "lrec":
        out = "listevide"
        for e in reversed(r):
            out = f"cons({e}, {out})"
        return out
    if ns == "liter":
        return "⟨" + ", ".join(map(str, r)) + "⟩" if r else "listevide"
    if ns == "ens":
        return "{" + ", ".join(map(str, sorted(r))) + "}" if r else "ensemblevide"
    if ns == "multi":
        return "⟦" + ", ".join(map(str, sorted(r))) + "⟧" if r else "multiensemblevide"
    raise TypeError(r)


def ev(ns, term):
    """Value of `term` in the model, as written in the answers ('indéfini' if a precondition fails)."""
    try:
        return _show(ns, eval(term, {"__builtins__": {}}, {**_COMMON, **_NS[ns]}))
    except Undefined:
        return "indéfini"


def _t(ns, term, ans, sol, enonce=None):
    got = ev(ns, term)
    assert got == ans, f"{term}: model gives {got}, answer says {ans}"
    e = {"enonce": (enonce or "Évaluer :") + f"\n\n{term}"}
    if got.lstrip("-").isdigit():
        e |= {"kind": "value", "calc": got, "ans": ans, "sol": f"**Réponse :** ${ans}$\n\n{sol}"}
    else:
        e |= {"kind": "open", "sol": f"**Réponse :** {ans}\n\n{sol}"}
    return e


def t(id, ns, term, ans, sol, enonce=None, src=None, duree=2):
    """Evaluate a term of type `ns`; the model checks `ans`."""
    e = {"id": id, **_t(ns, term, ans, sol, enonce), "duree": duree}
    if src:
        e["src"] = src
    return e


def tv(ns, term, ans, sol, enonce=None):
    """Variant of an evaluation exercise (same kind, other values), checked by the model too."""
    e = _t(ns, term, ans, sol, enonce)
    e.pop("kind")
    return e


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


# ---------------------------------------------------------------- exam helpers (B2: output orders, searching)


def _out_bad(push, out, stack=True):
    """First value of `out` a stack (or a queue) fed with `push` in that order cannot produce; None if possible."""
    if not stack:
        return next((b for a, b in zip(push, out) if a != b), None)
    pend, st = list(push), []
    for c in out:
        while (not st or st[-1] != c) and pend:
            st.append(pend.pop(0))
        if not st or st[-1] != c:
            return c
        st.pop()
    return None


def _calls(L, x):
    """Calls (left, right, middle) of the course dichotomy (bounds included, stops when left == right or found)."""
    g, d, r = 0, len(L) - 1, []
    while g <= d:
        m = (g + d) // 2
        r.append((g, d, m))
        if g == d or L[m] == x:
            return r
        if x < L[m]:
            d = m - 1
        else:
            g = m + 1
    return r + [(g, d, None)]


def _path_bad(seq, x):
    """First value of `seq` that cannot follow the earlier ones in a dichotomic search of x; None if possible."""
    return next((b for j, b in enumerate(seq) if any(a != x and (x < a) != (b < a) for a in seq[:j])), None)


def _pf(push, outs):
    """Answer « pile / file / les deux / aucune » for each output order."""
    r = []
    for o in outs:
        p, f = _out_bad(push, o) is None, _out_bad(push, o, False) is None
        r.append(f"{' '.join(o)} : " + ("pile et file" if p and f else "pile" if p else "file" if f else f"aucune (pile bloquée sur {_out_bad(push, o)})"))
    return r


def _tab(calls):
    return "\n\n".join(f"Appel {i} : g = {g}, d = {d}" + (f", milieu = {m}" if m is not None else " (g > d : arrêt)")
                     for i, (g, d, m) in enumerate(calls[1:], 1)) or "Aucun appel"


# sanity checks against the student copy marked by the teacher (B2, 9 Jan 2024)
_LI = "ACDEFHIJLMNPQRTVXZ"
assert _calls(_LI, "B") == [(0, 17, 8), (0, 7, 3), (0, 2, 1), (0, 0, 0)]
assert _calls(_LI, "P") == [(0, 17, 8), (9, 17, 13), (9, 12, 10), (11, 12, 11)]
assert _pf("DCAFBE", ["EBFACD", "DCAFBE", "ABFEDC", "ACBEFD"]) == [
    "E B F A C D : pile", "D C A F B E : pile et file", "A B F E D C : aucune (pile bloquée sur D)", "A C B E F D : pile"]

# ---------------------------------------------------------------- course

NOTIONS = [
    {"id": "signature", "titre": "Signature d'un type abstrait",
     "formule": r"type abstrait $=$ signature $+$ axiomes · signature $=$ types $+$ opérations · profil : nom : type$_1$ x type$_2$ $\to$ type du résultat · opération sans argument $=$ constante · le _ marque la place d'un argument",
     "exemple": r"insérer : liste x entier x élément $\to$ liste ; s'utilise insérer(l, i, e)",
     "cours": r"Les types nomment les ensembles de valeurs que l'on définit (pile, liste…). Chaque opération a un nom et un profil : le type de ses arguments, puis celui de son résultat. Dans un nom, le caractère _ indique où se placent les arguments : _! s'écrit x!, _^_ s'écrit x^y. Une opération sans argument (vrai : $\to$ booléen) est une constante."},
    {"id": "hierarchie", "titre": "Hiérarchie : types définis, prédéfinis, opérations internes, observateurs",
     "formule": r"défini : déclaré dans types (en conception) · prédéfini : déclaré dans utilise (déjà conçu) · opération interne : résultat de type défini · observateur : au moins un argument de type défini, résultat de type prédéfini",
     "exemple": r"vecteur : modifième est interne ; ième, borneinf, bornesup sont des observateurs",
     "cours": r"Un type réutilise des types déjà définis (entier, booléen, élément) listés après utilise ; sa signature est l'union de leurs signatures et des nouvelles opérations. Les opérations internes construisent ou modifient une valeur du type défini ; les observateurs la regardent et renvoient une valeur d'un type prédéfini."},
    {"id": "axiomes", "titre": "Axiomes, préconditions, consistance, complétude",
     "formule": r"axiomes : observateurs appliqués aux opérations internes · opération partielle : précondition « est-défini-ssi » · consistance : aucun axiome contradictoire · complétude : une valeur pour tout observateur appliqué à toute opération interne",
     "exemple": r"sommet(empiler(p, e)) $=$ e ; sommet(p) est-défini-ssi estvide(p) $=$ Faux",
     "cours": r"Pour savoir ce que fait une opération interne, on lui applique chaque observateur : chaque combinaison donne un axiome. Une opération qui n'est pas définie partout est partielle ; on précise son domaine par une précondition avant d'écrire ses axiomes, parfois à l'aide d'une opération auxiliaire (estinitialisé pour le vecteur, existe pour rechercher)."},
    {"id": "lrec", "titre": "Liste récursive",
     "formule": r"listevide · cons : élément x liste $\to$ liste · fin · tête : liste $\to$ place · contenu : place $\to$ élément · premier · succ : place $\to$ place · premier(l) $=$ contenu(tête(l)) · fin(cons(e, l)) $=$ l · premier(cons(e, l)) $=$ e · succ(tête(l)) $=$ tête(fin(l)) · fin, tête, premier : l $\neq$ listevide",
     "exemple": r"premier(fin(cons(3, cons(5, listevide)))) $=5$",
     "cours": r"La liste récursive se manipule par sa tête : cons ajoute un élément devant, fin retire le premier, premier lit le premier. tête renvoie la première place, succ passe à la place suivante, contenu lit l'élément d'une place. fin, tête et premier sont partielles (liste non vide)."},
    {"id": "liter", "titre": "Liste itérative",
     "formule": r"accès(l, k) : $k$-ième place · ième(l, k) · longueur · insérer(l, k, e) · supprimer(l, k) · insérer : $1\le k\le$ longueur(l)$+1$ · supprimer, accès : $1\le k\le$ longueur(l) · longueur(insérer(l, k, e)) $=$ longueur(l)$+1$ · ième(insérer(l, k, e), k) $=$ e · contenu(accès(l, k)) $=$ ième(l, k)",
     "exemple": r"insérer(insérer(listevide, 1, 5), 1, 8) $=\langle 8, 5\rangle$",
     "cours": r"La liste itérative décrit la même donnée, mais l'opération de base est l'accès à la $k$-ième place. Insérer en $k$ décale d'un rang les éléments de rang $\ge k$ ; supprimer en $k$ ramène d'un rang les éléments de rang $> k$. Les rangs commencent à $1$."},
    {"id": "conversion", "titre": "Extensions : concaténer, existe, rechercher ; passage récursif $\\leftrightarrow$ itératif",
     "formule": r"tête(l) $=$ accès(l, 1) · premier(l) $=$ ième(l, 1) · fin(l) $=$ supprimer(l, 1) · cons(e, l) $=$ insérer(l, 1, e) · concaténer(listevide, l) $=$ l · concaténer(cons(e, l), l2) $=$ cons(e, concaténer(l, l2)) · rechercher(e, l) est-défini-ssi existe(e, l) $=$ vrai",
     "exemple": r"concaténer(cons(1, listevide), cons(2, listevide)) $=$ cons(1, cons(2, listevide))",
     "cours": r"Une extension ajoute des opérations à un type supposé connu : on donne leur profil, leurs préconditions et leurs axiomes, sans réécrire le type. Les deux listes décrivent la même donnée : chaque opération de l'une s'écrit avec celles de l'autre (parfois avec une boucle et une liste auxiliaire)."},
    {"id": "pile", "titre": "Piles (LIFO)",
     "formule": r"pilevide · empiler : pile x élément $\to$ pile · dépiler · sommet · estvide · dépiler(empiler(p, e)) $=$ p · sommet(empiler(p, e)) $=$ e · estvide(pilevide) $=$ Vrai · estvide(empiler(p, e)) $=$ Faux · dépiler, sommet : estvide(p) $=$ Faux",
     "exemple": r"sommet(dépiler(empiler(empiler(pilevide, 3), 5))) $=3$",
     "cours": r"Dernier entré, premier sorti : les entrées et les sorties se font du même côté, le sommet. dépiler et sommet sont partielles."},
    {"id": "file", "titre": "Files (FIFO)",
     "formule": r"filevide · enfiler · défiler · premier · estvide · estvide(f) $=$ Vrai $\Rightarrow$ premier(enfiler(f, e)) $=$ e · estvide(f) $=$ Faux $\Rightarrow$ premier(enfiler(f, e)) $=$ premier(f) · estvide(f) $=$ Vrai $\Rightarrow$ défiler(enfiler(f, e)) $=$ filevide · estvide(f) $=$ Faux $\Rightarrow$ défiler(enfiler(f, e)) $=$ enfiler(défiler(f), e)",
     "exemple": r"premier(défiler(enfiler(enfiler(filevide, 3), 5))) $=5$",
     "cours": r"Premier entré, premier sorti : on enfile en queue, on défile en tête. Les axiomes de premier et de défiler distinguent la file vide de la file non vide : on ne voit le nouvel élément en tête que si la file était vide."},
    {"id": "repr", "titre": "Représentations statique et dynamique",
     "formule": r"statique : tableau de Nbmax éléments $+$ longueur (ou sommet, ou tête et queue) · dynamique : enregistrements chaînés par pointeurs, NUL $=$ fin · file statique circulaire : indice suivant $=(i \bmod \text{Nbmax})+1$",
     "exemple": r"Nbmax $=8$, queue $=8$ : après un enfilage, queue $=1$",
     "cours": r"Le tableau impose un surdimensionnement et des décalages pour insérer ou supprimer au milieu, mais donne l'accès direct au $k$-ième élément. Les pointeurs ne stockent que les éléments présents et insèrent sans décaler, mais l'accès au $k$-ième élément impose un parcours. Variantes : sentinelle en tête (pas de cas particulier devant le premier), liste circulaire (le pointeur repère le dernier), liste doublement chaînée (pointeurs de tête et de queue, retour en arrière)."},
    {"id": "recherche", "titre": "Ordres de sortie, recherche séquentielle et dichotomique",
     "formule": r"pile : une valeur sort si elle est au sommet · file : sortie $=$ ordre d'entrée · séquentielle : une comparaison par élément visité · triée : arrêt au premier élément $\ge x$ · dichotomie : milieu $=\lfloor (g+d)/2\rfloor$, $x <$ milieu : $d=$ milieu$-1$, sinon $g=$ milieu$+1$, arrêt si trouvé ou $g=d$",
     "exemple": r"on empile A, B, C : B A C est possible, C A B ne l'est pas (A est sous B)",
     "cours": r"Pour tester un ordre de sortie d'une pile, on rejoue : on empile jusqu'à ce que la valeur voulue soit au sommet ; si elle est déjà dans la pile mais pas au sommet, l'ordre est impossible et c'est la valeur qui pose problème. Une file rend les valeurs dans l'ordre d'entrée. En recherche dichotomique, chaque valeur rencontrée borne toutes les suivantes : après $67$ en cherchant $66$, plus aucune valeur $\ge 67$."},
    {"id": "ensemble", "titre": "Ensembles et multi-ensembles",
     "formule": r"ensemblevide · ajouter(x, e) · supprimer(x, e) · x $\in$ e · card · choisir · x $\in$ ensemblevide $=$ faux · x $\in$ e $=$ vrai $\Rightarrow$ card(ajouter(x, e)) $=$ card(e) · x $\in$ e $=$ faux $\Rightarrow$ card(ajouter(x, e)) $=$ card(e)$+1$ · multi-ensemble : card(ajouter(x, me)) $=$ card(me)$+1$, nboccurrences",
     "exemple": r"card(ajouter(3, ajouter(3, ensemblevide))) $=1$ ; dans un multi-ensemble, $2$",
     "cours": r"Un ensemble ne contient pas de doublon et n'a pas d'ordre : ajouter un élément déjà présent ne change rien. choisir renvoie un élément quelconque d'un ensemble non vide. Un multi-ensemble garde les répétitions : nboccurrences compte les exemplaires, supprimer en retire un seul."},
]

C = "Cours TAA (MiMos)"
W = "Cours d'algo EPITA (wiki), « Structures séquentielles »"
WT = "Cours d'algo EPITA (wiki), « Types abstraits »"
WE = "Cours d'algo EPITA (wiki), « Ensembles »"
M = "Moodle TAA, exercice d'application"

_L = "cons(3, cons(5, cons(7, listevide)))"
B1_24 = "Examen B1 TAA, 30 octobre 2024 (Past-Exams S1/Midterms/Algo/2029/TAA)"
B2_24 = "Examen B2 TAA, 9 janvier 2024 (Past-Exams S1/Finals/Algo/2028/TAA)"
B2_25 = "Examen B2 TAA, 7 janvier 2025 (Past-Exams S1/Finals/Algo/2029/TAA, sans corrigé)"
_B1L = [1, 1, 2, 3, 5, 5, 8, 9, 9]
_SQ = [2, 5, 9, 14, 20, 27, 31]


def _mys(args):
    return "\n\n".join(f"mystère($\\lambda$,{x},{y}) $=\\{{{', '.join(map(str, _B1L[:x - 1] + _B1L[y:]))}\\}}$" for x, y in args)


_LB = [1, 3, 8, 15, 23, 29, 32, 35, 38, 42, 47, 51, 55]


LEVELS = [
    {"n": 1, "titre": "Signature : profils et constantes", "notions": ["signature"], "exos": [
        o("t11", r"Donner le profil de l'opération insérer d'une liste itérative (insérer un élément à la $k$-ième place).",
          r"insérer : liste x entier x élément $\to$ liste. Les arguments sont la liste, le rang et l'élément ; le résultat est la nouvelle liste.", src=W, duree=2),
        v("t12", r"Combien d'arguments a l'opération Δ : entier x entier x entier $\to$ entier ?", "3", "3", r"Trois entiers avant la flèche : $3$ arguments.", src=WT, duree=1),
        v("t13", r"Dans la signature du type booléen (vrai, faux, non, et, ou), combien d'opérations sont des constantes ?", "2", "2", r"vrai : $\to$ booléen et faux : $\to$ booléen n'ont pas d'argument : ce sont des constantes. $2$.", src=WT, duree=1),
        o("t14", r"L'opération puissance est déclarée _^_ : entier x entier $\to$ entier. Comment l'appliquer à x et y ? Que vaut l'écriture x^y! avec _! la factorielle ?",
          r"Les arguments remplacent les _ dans l'ordre : x^y. L'écriture x^y! est ambiguë ; le cours la lit x^(y!) et impose des parenthèses, (x^y)!, pour la factorielle de la puissance.", src=WT, duree=3),
        o("t15", r"Écrire la signature complète du type booléen.",
          "```\ntypes\n   booléen\nopérations\n   vrai : → booléen\n   faux : → booléen\n    non : booléen → booléen\n     et : booléen x booléen → booléen\n     ou : booléen x booléen → booléen\n```", src=WT, duree=3),
        v("t16", r"Signature de la pile (pilevide, empiler, dépiler, sommet, estvide) : combien d'opérations ont un résultat de type pile ?", "3", "3", r"pilevide, empiler et dépiler renvoient une pile ; sommet renvoie un élément, estvide un booléen. $3$.", src=C, duree=2),
        o("t17", r"Quels caractères sont interdits dans le nom d'une opération, et pourquoi ?",
          r"L'espace (séparateur), les parenthèses (elles forcent les priorités) et _ (il marque la place des arguments). Tous les autres glyphes sont permis : Δ, !, ^…", src=WT, duree=2),
    ]},
    {"n": 2, "titre": "Hiérarchie : défini, prédéfini, interne, observateur", "notions": ["hierarchie", "signature"], "exos": [
        o("t21", r"Type pile : quels sont les types définis et prédéfinis ?",
          r"Défini : pile (déclaré dans types). Prédéfinis : booléen et élément (déclarés dans utilise).", src=C, duree=2),
        v("t22", r"Type vecteur (vect, modifième, ième, estinitialisé, bornesup, borneinf) : combien d'observateurs ?", "4", "4",
          r"ième (élément), estinitialisé (booléen), bornesup et borneinf (entier) prennent un vecteur et renvoient un type prédéfini : $4$. vect et modifième renvoient un vecteur : opérations internes.", src=WT, duree=2),
        v("t23", r"Liste récursive (listevide, cons, fin, tête, contenu, premier, succ) : combien d'observateurs ?", "2", "2",
          r"Types définis : liste et place. contenu (place $\to$ élément) et premier (liste $\to$ élément) sont des observateurs. tête et succ sont internes (résultat place), listevide, cons, fin aussi (résultat liste). $2$.", src=W, duree=3),
        o("t24", r"Classer les opérations de la file : internes ou observateurs ?",
          r"Internes (résultat file) : filevide, enfiler, défiler. Observateurs : premier (élément) et estvide (booléen).", src=C, duree=2),
        v("t25", r"Liste itérative (listevide, accès, contenu, ième, longueur, supprimer, insérer, succ) : combien d'opérations internes ?", "5", "5",
          r"Internes : listevide, supprimer, insérer (résultat liste), accès et succ (résultat place). Observateurs : contenu, ième, longueur. $5$.", src=W, duree=3),
        o("t26", r"À quoi sert la rubrique utilise ? Donner la signature du vecteur qu'elle permet d'écrire.",
          r"Elle réutilise des types déjà conçus au lieu de les redéfinir : la signature du type défini est l'union de leurs signatures et de ses nouvelles opérations. Pour vecteur : utilise entier, élément ; on peut alors écrire ième(v, i+2), car l'addition des entiers est disponible.", src=WT, duree=3),
        o("t27", r"Type ensemble (ensemblevide, ajouter, supprimer, _∈_, card, choisir) : classer les opérations.",
          r"Internes (résultat ensemble) : ensemblevide, ajouter, supprimer. Observateurs : _∈_ (booléen), card (entier), choisir (élément).", src=WE, duree=2),
    ]},
    {"n": 3, "titre": "Axiomes, préconditions, consistance, complétude", "notions": ["axiomes", "hierarchie"], "exos": [
        o("t31", r"Rédiger les axiomes du type booléen : vrai, faux : $\to$ booléen ; non : booléen $\to$ booléen ; _ et _, _ ou _ : booléen x booléen $\to$ booléen.",
          "```\naxiomes\n   non(vrai) = faux\n   non(faux) = vrai\n   vrai et b = b\n   faux et b = faux\n   vrai ou b = vrai\n   faux ou b = b\navec\n   booléen b\n```\nOn applique chaque opération aux deux constructeurs vrai et faux : pour et et ou, il suffit de distinguer le premier argument.", src=M, duree=6),
        o("t32", r"Définir la consistance et la complétude d'un ensemble d'axiomes.",
          r"Consistance : aucun axiome n'en contredit un autre (une même opération sur les mêmes arguments ne rend jamais deux valeurs différentes). Complétude : assez d'axiomes pour déduire une valeur de tout observateur appliqué à toute opération interne.", src=WT, duree=3),
        o("t33", r"Qu'est-ce qu'une opération partielle ? Lesquelles le sont dans la pile ? Écrire leurs préconditions.",
          "Une opération qui n'est pas définie partout ; son domaine est donné par une précondition.\n\n```\ndépiler(p) est-défini-ssi estvide(p) = Faux\n sommet(p) est-défini-ssi estvide(p) = Faux\n```", src=C, duree=3),
        o("t34", r"Comment trouve-t-on les axiomes d'un type ?",
          r"On applique chaque observateur à chaque opération interne : la valeur obtenue décrit ce que fait l'opération interne. Exemple pour la pile : sommet et estvide appliqués à pilevide et à empiler, puis dépiler appliqué à empiler.", src=WT, duree=3),
        o("t35", r"Pourquoi le type vecteur a-t-il besoin de l'opération estinitialisé ?",
          r"ième n'est pas définie sur une case jamais remplie par modifième. Pour écrire la précondition de ième, il faut pouvoir dire qu'une case est remplie : estinitialisé est une opération auxiliaire créée pour cela. ième(v, i) est-défini-ssi borneinf(v) $\le$ i $\le$ bornesup(v) & estinitialisé(v, i) $=$ vrai.", src=WT, duree=3),
        o("t36", r"Expliquer les deux axiomes : borneinf(v) $\le$ i $\le$ bornesup(v) $\Rightarrow$ ième(modifième(v, i, e), i) $=$ e, et, pour $i\neq j$ dans les bornes, ième(modifième(v, i, e), j) $=$ ième(v, j).",
          r"Le premier : après modifième, la case $i$ contient e. Le second : les autres cases ($j\neq i$) gardent leur contenu. Ensemble, ils disent que modifième ne change que la case $i$.", src=WT, duree=3),
        v("t37", r"Pour la pile, combien d'axiomes faut-il pour estvide (observateur appliqué aux opérations qui construisent une pile : pilevide et empiler) ?", "2", "2",
          r"estvide(pilevide) $=$ Vrai et estvide(empiler(p, e)) $=$ Faux : $2$.", src=C, duree=2),
    ]},
    {"n": 4, "titre": "Liste récursive : évaluer", "notions": ["lrec"], "exos": [
        t("t41", "lrec", "premier(cons(3, cons(5, listevide)))", "3", r"premier(cons(e, l)) $=$ e.", src=C, duree=1),
        t("t42", "lrec", f"premier(fin({_L}))", "5", r"fin retire $3$ ; le premier de cons(5, cons(7, listevide)) est $5$.", src=C),
        t("t43", "lrec", "contenu(succ(succ(tête(cons(2, cons(4, cons(6, listevide)))))))", "6",
          r"tête donne la place de $2$, chaque succ avance d'une place : $4$ puis $6$. contenu lit $6$.", src=C, duree=3),
        t("t44", "lrec", f"fin(fin({_L}))", "cons(7, listevide)", r"fin(cons(e, l)) $=$ l, deux fois.", src=C),
        t("t45", "lrec", "fin(cons(4, listevide))", "listevide", r"fin(cons(e, l)) $=$ l avec l $=$ listevide.", src=C, duree=1),
        t("t46", "lrec", "premier(fin(cons(9, listevide)))", "indéfini",
          r"fin(cons(9, listevide)) $=$ listevide et premier(l) est-défini-ssi l $\neq$ listevide.", src=C),
        o("t47", r"Expliquer l'axiome succ(tête(l)) $=$ tête(fin(l)).",
          r"La place qui suit la première place de l est la première place de la liste privée de son premier élément : avancer d'une place revient à regarder la tête de la fin.", src=C, duree=3),
    ]},
    {"n": 5, "titre": "Liste itérative : évaluer", "notions": ["liter"], "exos": [
        t("t51", "liter", "longueur(insérer(insérer(listevide, 1, 5), 1, 8))", "2", r"Chaque insérer ajoute $1$ à la longueur.", src=C, duree=1),
        t("t52", "liter", "ième(insérer(insérer(listevide, 1, 5), 1, 8), 1)", "8", r"$\langle 5\rangle$ puis on insère $8$ au rang $1$ : $\langle 8, 5\rangle$.", src=C),
        t("t53", "liter", "insérer(insérer(insérer(listevide, 1, 3), 2, 7), 2, 9)", "⟨3, 9, 7⟩",
          r"$\langle 3\rangle$, $\langle 3, 7\rangle$, puis $9$ au rang $2$ décale $7$ au rang $3$.", src=C),
        t("t54", "liter", "supprimer(insérer(insérer(insérer(listevide, 1, 3), 2, 7), 3, 9), 2)", "⟨3, 9⟩",
          r"$\langle 3, 7, 9\rangle$ ; supprimer le rang $2$ ramène $9$ au rang $2$.", src=C),
        t("t55", "liter", "contenu(succ(accès(insérer(insérer(listevide, 1, 4), 2, 6), 1)))", "6",
          r"$\langle 4, 6\rangle$ ; succ(accès(l, 1)) $=$ accès(l, 2) et contenu(accès(l, 2)) $=$ ième(l, 2) $=6$.", src=C, duree=3),
        t("t56", "liter", "insérer(listevide, 2, 5)", "indéfini",
          r"insérer(l, k, e) est-défini-ssi $1\le k\le$ longueur(l)$+1=1$ : $k=2$ est hors domaine.", src=C),
        o("t57", r"$l=\langle a, b, c, d\rangle$. Que vaut ième(supprimer(l, 2), 3) ? Citer l'axiome utilisé.",
          r"$k=2\le i=3\le$ longueur(l)$-1=3$, donc ième(supprimer(l, 2), 3) $=$ ième(l, 4) $=$ d (axiome $k\le i\le$ longueur(l)$-1\Rightarrow$ ième(supprimer(l, k), i) $=$ ième(l, i$+1$)).", src=C, duree=3),
    ]},
    {"n": 6, "titre": "Extensions et passage récursif ↔ itératif", "notions": ["conversion", "lrec", "liter"], "exos": [
        o("t61", r"Écrire tête, premier, fin et cons de la liste récursive avec les opérations de la liste itérative.",
          r"tête(l) $=$ accès(l, 1) ; premier(l) $=$ ième(l, 1) ; fin(l) $=$ supprimer(l, 1) ; cons(e, l) $=$ insérer(l, 1, e).", src=W, duree=3),
        o("t62", r"Écrire supprimer(l, i) (liste itérative) avec les seules opérations de la liste récursive (listevide, cons, fin, premier).",
          "```\nl2 ← listevide\n(i-1) fois { l2 ← cons(premier(l), l2)\n             l ← fin(l) }\nl ← fin(l)\n(i-1) fois { l ← cons(premier(l2), l)\n             l2 ← fin(l2) }\n```\nOn met de côté les $i-1$ premiers éléments, on retire le $i$-ème, puis on remet les éléments mis de côté (comme insérer, avec fin à la place de cons(e, l)).", src=W, duree=6),
        t("t63", "lrec", "concaténer(cons(1, cons(2, listevide)), cons(3, listevide))", "cons(1, cons(2, cons(3, listevide)))",
          r"concaténer(cons(e, l), l2) $=$ cons(e, concaténer(l, l2)) deux fois, puis concaténer(listevide, l2) $=$ l2.", src=W),
        t("t64", "lrec", "existe(4, cons(1, cons(4, listevide)))", "Vrai", r"$1\neq4$ : on regarde la suite ; $4=4$ : vrai.", src=W, duree=1),
        t("t65", "lrec", "existe(5, concaténer(cons(1, listevide), cons(2, listevide)))", "Faux",
          r"La liste est cons(1, cons(2, listevide)) ; $5$ n'y est pas : on atteint existe(5, listevide) $=$ faux.", src=W),
        o("t66", r"Écrire le profil et les axiomes de concaténer pour la liste récursive.",
          "```\nconcaténer : liste x liste → liste\nconcaténer(listevide, l) = l\nconcaténer(cons(e, l), l2)\n      = cons(e, concaténer(l, l2))\n```", src=W, duree=4),
        o("t67", r"Pourquoi l'opération rechercher : élément x liste $\to$ place a-t-elle une précondition, et comment l'écrire ?",
          r"La place d'un élément absent n'existe pas : rechercher est partielle. On ajoute l'opération auxiliaire existe : élément x liste $\to$ booléen, puis rechercher(e, l) est-défini-ssi existe(e, l) $=$ vrai, et l'axiome existe(e, l) $=$ vrai $\Rightarrow$ contenu(rechercher(e, l)) $=$ e.", src=W, duree=4),
    ]},
    {"n": 7, "titre": "Piles : évaluer", "notions": ["pile"], "exos": [
        t("t71", "pile", "sommet(empiler(empiler(pilevide, 3), 5))", "5", r"sommet(empiler(p, e)) $=$ e.", src=C, duree=1),
        t("t72", "pile", "sommet(dépiler(empiler(empiler(pilevide, 3), 5)))", "3", r"dépiler(empiler(p, e)) $=$ p, puis sommet $=3$.", src=C),
        t("t73", "pile", "dépiler(empiler(dépiler(empiler(pilevide, 1)), 2))", "pilevide",
          r"dépiler(empiler(pilevide, 1)) $=$ pilevide ; on empile $2$ puis on le dépile.", src=C),
        t("t74", "pile", "estvide(dépiler(empiler(pilevide, 7)))", "Vrai", r"dépiler(empiler(pilevide, 7)) $=$ pilevide.", src=C, duree=1),
        t("t75", "pile", "sommet(dépiler(empiler(pilevide, 4)))", "indéfini", r"On demande le sommet de pilevide : précondition fausse.", src=C),
        t("t76", "pile", "empiler(dépiler(empiler(empiler(pilevide, 1), 2)), 3)", "empiler(empiler(pilevide, 1), 3)",
          r"dépiler retire $2$ ; on empile $3$ sur $1$.", src=C),
        o("t77", r"Pourquoi dit-on qu'une pile est LIFO ? Donner les axiomes qui le traduisent.",
          r"Last In First Out : le dernier élément empilé est le premier lu et retiré, au sommet. dépiler(empiler(p, e)) $=$ p et sommet(empiler(p, e)) $=$ e : on retrouve d'abord le dernier élément ajouté.", src=C, duree=3),
    ]},
    {"n": 8, "titre": "Files : évaluer", "notions": ["file"], "exos": [
        t("t81", "file", "premier(enfiler(enfiler(filevide, 3), 5))", "3",
          r"enfiler(filevide, 3) n'est pas vide : premier(enfiler(f, 5)) $=$ premier(f) $=3$.", src=C, duree=1),
        t("t82", "file", "premier(défiler(enfiler(enfiler(filevide, 3), 5)))", "5", r"On défile $3$, il reste $5$.", src=C),
        t("t83", "file", "défiler(enfiler(enfiler(filevide, 1), 2))", "enfiler(filevide, 2)",
          r"f $=$ enfiler(filevide, 1) non vide : défiler(enfiler(f, 2)) $=$ enfiler(défiler(f), 2) $=$ enfiler(filevide, 2).", src=C, duree=3),
        t("t84", "file", "estvide(défiler(enfiler(filevide, 9)))", "Vrai", r"défiler(enfiler(filevide, 9)) $=$ filevide.", src=C, duree=1),
        t("t85", "file", "premier(défiler(enfiler(défiler(enfiler(enfiler(filevide, 1), 2)), 3)))", "3",
          r"File $1, 2$ ; on défile $1$ : $2$ ; on enfile $3$ : $2, 3$ ; on défile $2$ : il reste $3$.", src=C, duree=3),
        o("t86", r"Démontrer avec les axiomes que défiler(enfiler(enfiler(filevide, a), b)) $=$ enfiler(filevide, b).",
          r"f $=$ enfiler(filevide, a) n'est pas vide (estvide(enfiler(f, e)) $=$ Faux), donc défiler(enfiler(f, b)) $=$ enfiler(défiler(f), b). filevide est vide, donc défiler(enfiler(filevide, a)) $=$ filevide. D'où enfiler(filevide, b).", src=C, duree=5),
        o("t87", r"Pourquoi les axiomes de premier et défiler distinguent-ils la file vide, alors que ceux de la pile non ?",
          r"Dans une file, on ajoute en queue et on lit en tête : le nouvel élément n'est en tête que si la file était vide. Dans une pile, on ajoute et on lit au même endroit, le sommet : le nouvel élément est toujours visible.", src=C, duree=3),
    ]},
    {"n": 9, "titre": "Écrire les axiomes d'une extension", "notions": ["axiomes", "lrec", "pile", "conversion"], "exos": [
        o("t91", r"Extension longueur : liste $\to$ entier pour la liste récursive. Écrire ses axiomes.",
          "```\nlongueur(listevide) = 0\nlongueur(cons(e, l)) = longueur(l) + 1\n```", src=C, duree=3),
        o("t92", r"Extension hauteur : pile $\to$ entier (nombre d'éléments). Écrire ses axiomes.",
          "```\nhauteur(pilevide) = 0\nhauteur(empiler(p, e)) = hauteur(p) + 1\n```", src=C, duree=3),
        o("t93", r"Extension dernier : liste $\to$ élément (dernier élément d'une liste récursive). Précondition et axiomes.",
          "```\ndernier(l) est-défini-ssi l ≠ listevide\ndernier(cons(e, listevide)) = e\nl ≠ listevide ⇒ dernier(cons(e, l)) = dernier(l)\n```", src=C, duree=4),
        o("t94", r"Extension nbocc : élément x liste $\to$ entier (nombre d'occurrences dans une liste récursive). Écrire ses axiomes.",
          "```\nnbocc(x, listevide) = 0\nx = e ⇒ nbocc(x, cons(e, l)) = nbocc(x, l) + 1\nx ≠ e ⇒ nbocc(x, cons(e, l)) = nbocc(x, l)\n```", src=C, duree=4),
        o("t95", r"Extension ajouterqueue : liste x élément $\to$ liste (ajoute à la fin d'une liste récursive). Écrire ses axiomes.",
          "```\najouterqueue(listevide, e) = cons(e, listevide)\najouterqueue(cons(x, l), e)\n      = cons(x, ajouterqueue(l, e))\n```", src=C, duree=4),
        t("t96", "lrec", "longueur(concaténer(cons(1, listevide), cons(2, cons(3, listevide))))", "3",
          r"La concaténation contient $1, 2, 3$ : longueur(cons(e, l)) $=$ longueur(l)$+1$ trois fois.", src=C),
        o("t97", r"Extension fond : pile $\to$ élément (l'élément le plus ancien de la pile). Précondition et axiomes.",
          "```\nfond(p) est-défini-ssi estvide(p) = Faux\nestvide(p) = Vrai ⇒ fond(empiler(p, e)) = e\nestvide(p) = Faux ⇒ fond(empiler(p, e)) = fond(p)\n```", src=C, duree=4),
    ]},
    {"n": 10, "titre": "Représentations statique et dynamique", "notions": ["repr", "pile", "file"], "exos": [
        v("t101", r"File statique circulaire, Nbmax $=8$, indices de $1$ à $8$. La queue vaut $8$ ; on enfile un élément. Nouvelle queue ?", "(8 % 8) + 1", "1",
          r"Après $8$ on revient à $1$ : $(8 \bmod 8)+1=1$.", src=W, duree=2),
        v("t102", r"Même file (Nbmax $=8$). La queue vaut $6$ ; on enfile $4$ éléments. Nouvelle queue ?", "((6 + 4 - 1) % 8) + 1", "2",
          r"$7, 8, 1, 2$ : la queue vaut $2$.", src=W, duree=2),
        v("t103", r"Pile statique, sommet $=0$ pour la pile vide. On empile $5$ éléments, on dépile $2$ fois, on empile $3$ éléments. Sommet ?", "5 - 2 + 3", "6",
          r"Le sommet compte les éléments : $5-2+3=6$.", src=W, duree=2),
        v("t104", r"Liste statique de longueur $12$ (Nbmax $=20$). Supprimer l'élément de rang $3$ oblige à décaler combien d'éléments ?", "12 - 3", "9",
          r"Les éléments de rang $4$ à $12$ reculent d'une case : $12-3=9$.", src=W, duree=2),
        o("t105", r"Comparer les représentations statique et dynamique d'une liste.",
          r"Statique (tableau $+$ longueur) : accès direct au $k$-ième élément, mais tableau surdimensionné et décalages pour insérer ou supprimer au milieu. Dynamique (enregistrements chaînés, NUL en fin) : exactement le nombre d'éléments, insertion et suppression sans décalage, concaténation facile, bien adaptée au récursif ; mais pas d'accès direct au $k$-ième élément et un pointeur par élément.", src=W, duree=5),
        o("t106", r"Qu'apportent la sentinelle en tête, la liste circulaire et la liste doublement chaînée ?",
          r"Sentinelle : un enregistrement fixe en tête, plus de cas particulier pour insérer devant le premier élément. Circulaire : le dernier pointe sur le premier, le pointeur de liste repère le dernier (le premier est à un lien). Doublement chaînée : un lien vers le précédent en plus, on peut revenir en arrière ; il faut des pointeurs de tête et de queue.", src=W, duree=5),
        o("t107", r"Pourquoi la représentation statique convient-elle bien à une pile ?",
          r"On n'ajoute et ne retire qu'au sommet : l'indice sommet avance ou recule, sans aucun décalage dans le tableau. Seule la taille maximale (Nbmax) limite la pile.", src=W, duree=3),
    ]},
    {"n": 11, "titre": "Ensembles et multi-ensembles", "notions": ["ensemble"], "exos": [
        t("t111", "ens", "card(ajouter(3, ajouter(5, ajouter(3, ensemblevide))))", "2",
          r"$3$ est déjà présent au dernier ajout : card ne change pas. Ensemble $\{3, 5\}$.", src=WE),
        t("t112", "ens", "appartient(5, supprimer(5, ajouter(5, ajouter(5, ensemblevide))))", "Faux",
          r"x $=$ y $\Rightarrow$ (x $\in$ supprimer(y, e)) $=$ faux, même après deux ajouts.", src=WE, enonce="Évaluer (appartient(x, e) est noté x ∈ e dans le cours) :"),
        t("t113", "ens", "card(supprimer(4, ajouter(2, ensemblevide)))", "1",
          r"$4\notin\{2\}$ : card(supprimer(x, e)) $=$ card(e) $=1$.", src=WE),
        t("t114", "multi", "card(ajouter(3, ajouter(3, multiensemblevide)))", "2",
          r"Dans un multi-ensemble, card(ajouter(x, me)) $=$ card(me)$+1$ toujours.", src=C, enonce="Évaluer (multi-ensemble) :"),
        t("t115", "multi", "nboccurrences(3, supprimer(3, ajouter(3, ajouter(3, ajouter(1, multiensemblevide)))))", "1",
          r"Deux exemplaires de $3$ ; supprimer en retire un seul : $1$.", src=C, enonce="Évaluer (multi-ensemble) :"),
        o("t116", r"Pourquoi choisir : ensemble $\to$ élément a-t-elle une précondition, et quel axiome la décrit ?",
          r"On ne peut pas choisir un élément dans l'ensemble vide : choisir(e) est-défini-ssi e $\neq$ ensemblevide. Axiome : choisir(e) $\in$ e $=$ vrai (l'élément choisi appartient à l'ensemble, sans dire lequel).", src=WE, duree=3),
        o("t117", r"Écrire les axiomes de card pour le type ensemble.",
          "```\ncard(ensemblevide) = 0\nx ∈ e = vrai ⇒ card(ajouter(x, e)) = card(e)\nx ∈ e = faux ⇒ card(ajouter(x, e)) = card(e) + 1\nx ∈ e = vrai ⇒ card(supprimer(x, e)) = card(e) - 1\nx ∈ e = faux ⇒ card(supprimer(x, e)) = card(e)\n```\n(La fiche Moodle écrit « x ∈ = faux » dans le dernier axiome : il manque e.)", src=C, duree=5),
    ]},
    {"n": 12, "titre": "Niveau examen : examen B1 du 30 octobre 2024", "notions": ["liter", "lrec", "axiomes", "conversion"], "examen": True, "exos": [
        o("tx1", r"Exercice 1 (5 points). Liste itérative. mystère : liste x entier x entier $\to$ liste, défini ssi $1\le x\le y\le$ longueur($\lambda$). Axiomes : longueur(mystère($\lambda$, x, y)) $=$ longueur($\lambda$) $- y + x - 1$ ; $1\le i<x \Rightarrow$ ième(mystère($\lambda$, x, y), i) $=$ ième($\lambda$, i) ; $x\le i\le$ longueur($\lambda$)$-y+x-1 \Rightarrow$ ième(mystère($\lambda$, x, y), i) $=$ ième($\lambda$, i$+y-x+1$). Avec $\lambda=\{1,1,2,3,5,5,8,9,9\}$, donner mystère($\lambda$,3,5), mystère($\lambda$,1,4), mystère($\lambda$,6,9).",
          "mystère supprime les éléments des rangs $x$ à $y$.\n\n" + _mys([(3, 5), (1, 4), (6, 9)]), src=B1_24, duree=7),
        o("tx1b", r"Exercice 1, suite. Même opération mystère, même $\lambda=\{1,1,2,3,5,5,8,9,9\}$ : donner mystère($\lambda$,8,8) et mystère($\lambda$,1,9).",
          _mys([(8, 8), (1, 9)]) + "\n\n$x=y$ supprime un seul élément ; $x=1$, $y=$ longueur($\\lambda$) vide la liste (longueur $9-9+1-1=0$).", src=B1_24, duree=5),
        o("tx2", r"Exercice 2 (5 points). Liste récursive (listevide, cons, premier, fin, tête, contenu, succ). On ajoute supprime-sup : liste x élément $\to$ liste, qui supprime tous les éléments strictement supérieurs à x. Donner ses axiomes et ses préconditions.",
          "Aucune précondition : supprime-sup est totale.\n```\nsupprime-sup(listevide, x) = listevide\ne > x ⇒ supprime-sup(cons(e, λ), x) = supprime-sup(λ, x)\ne ≤ x ⇒ supprime-sup(cons(e, λ), x) = cons(e, supprime-sup(λ, x))\n```\navec λ : liste ; e, x : élément. Un axiome par opération interne qui construit la liste (listevide, cons) ; cons se découpe selon la comparaison de e et x.",
          src=B1_24, duree=12),
    ]},
    {"n": 13, "titre": "Ordres de sortie, recherches séquentielle et dichotomique", "notions": ["recherche", "pile", "file"], "exos": [
        o("t131", r"On empile, dans cet ordre, A, B, C, D. Ces ordres de sortie sont-ils possibles ? Sinon, quelle est la première valeur qui pose problème ? (a) B A D C (b) D A B C (c) C D B A (d) A D B C",
          "\n\n".join(f"({k}) {' '.join(w)} : " + ("possible" if _out_bad("ABCD", w) is None else f"impossible, {_out_bad('ABCD', w)}") for k, w in zip("abcd", ["BADC", "DABC", "CDBA", "ADBC"]))
          + "\n\nOn rejoue : on empile jusqu'à avoir la valeur voulue au sommet. Une valeur déjà empilée mais pas au sommet bloque.", src=B2_25, duree=4),
        o("t132", r"On ajoute, dans cet ordre, 1, 2, 3, 4 à une structure linéaire vide. Pour chaque ordre de sortie, la structure peut-elle être une pile, une file, les deux, aucune ? 1234, 4321, 2143, 3142.",
          "\n\n".join(_pf("1234", ["1234", "4321", "2143", "3142"])) + "\n\n1234 : chaque valeur sort aussitôt entrée, la pile convient aussi.", src=B2_24, duree=4),
        v("t133", r"$\lambda=[2, 5, 9, 14, 20, 27, 31]$. Recherche séquentielle de $20$ **sans** tenir compte de l'ordre : nombre de comparaisons entre $20$ et un élément ?",
          str(_SQ.index(20) + 1), str(_SQ.index(20) + 1), r"On compare $2, 5, 9, 14$ puis $20$ : trouvé.", src=B2_25, duree=2),
        v("t134", r"Même $\lambda$. Recherche séquentielle de $15$ **en tenant compte** de l'ordre : nombre de comparaisons ?",
          str(sum(e < 15 for e in _SQ) + 1), str(sum(e < 15 for e in _SQ) + 1), r"$2, 5, 9, 14$ puis $20 > 15$ : arrêt, $5$ comparaisons (sans l'ordre : $7$).", src=B2_25, duree=2),
        o("t135", r"Liste triée LI $=$ B D F G K M P S V Y (indices $0$ à $9$). Recherche dichotomique récursive de S entre g et d compris. Départ : g $=0$, d $=9$, milieu $=4$. Donner g, d, milieu à chaque appel.",
          _tab(_calls("BDFGKMPSVY", "S")) + "\n\nmilieu $=\\lfloor (g+d)/2\\rfloor$ ; trouvé au dernier appel.", src=B2_24, duree=5),
        o("t136", r"Même LI. Recherche de C (absente) : g, d, milieu à chaque appel ?",
          _tab(_calls("BDFGKMPSVY", "C")) + "\n\nLes bornes sont égales au dernier appel : arrêt, C n'est pas dans LI (version du cours, comme dans le corrigé du B2 de janvier 2024).", src=B2_24, duree=5),
        o("t137", r"Recherche dichotomique de $40$ dans des listes croissantes. Ces suites de valeurs rencontrées sont-elles possibles ? Sinon, première valeur qui pose problème. (a) 90 20 60 30 45 40 (b) 10 80 50 35 55 40 (c) 70 25 65 38 41 40",
          "\n\n".join(f"({k}) {s} : " + ("possible" if _path_bad([int(t) for t in s.split()], 40) is None else f"impossible, {_path_bad([int(t) for t in s.split()], 40)}") for k, s in zip("abc", ["90 20 60 30 45 40", "10 80 50 35 55 40", "70 25 65 38 41 40"]))
          + "\n\nChaque valeur borne les suivantes : après $50 > 40$, toutes les valeurs sont $< 50$.", src=B2_25, duree=4),
    ]},
    {"n": 14, "titre": "Niveau examen : examen B2 du 9 janvier 2024", "notions": ["recherche", "pile", "file"], "examen": True, "exos": [
        o("tx3", r"Exercice 1 (Pile ou file ? 3 points). On ajoute, dans cet ordre, D, C, A, F, B, E à une structure linéaire vide. Pour chaque ordre de sortie, la structure peut-elle être une pile, une file (ce peut être les deux), ou aucune des deux ? E B F A C D ; D C A F B E ; A B F E D C ; A C B E F D.",
          "\n\n".join(_pf("DCAFBE", ["EBFACD", "DCAFBE", "ABFEDC", "ACBEFD"])), src=B2_24, duree=5),
        o("tx4", r"Exercice 2 (Recherche dichotomique, 7 points). LI $=$ A C D E F H I J L M N P Q R T V X Z (indices $0$ à $17$). Version récursive, bornes g et d comprises. Départ : g $=0$, d $=17$, milieu $=8$. Donner g, d et milieu à chaque appel pour la recherche de B.",
          _tab(_calls(_LI, "B")) + "\n\nÀ l'appel 3, g $=$ d : arrêt, B est absente. La copie notée 9/10 qui ajoute un appel 4 (g $=1$, d $=0$) perd ce point.", src=B2_24, duree=5),
        o("tx4b", r"Exercice 2, suite. Même LI, même départ : g, d et milieu à chaque appel pour la recherche de P.",
          _tab(_calls(_LI, "P")) + "\n\nP est à l'indice $11$ : trouvée à l'appel 3.", src=B2_24, duree=5),
    ]},
    {"n": 15, "titre": "Niveau examen : examen B2 du 7 janvier 2025", "notions": ["recherche", "pile"], "examen": True, "exos": [
        o("tx5", r"Exercice 1 (Pile, 3 points). On empile, dans cet ordre, A, B, C, D, E, F. Chaque séquence peut-elle être un ordre de sortie ? Sinon, première valeur qui pose problème. CBEFDA ; DEBCFA ; BDEFAC ; CEDFBA.",
          "\n\n".join(f"{w} : " + ("oui" if _out_bad("ABCDEF", w) is None else f"non, {_out_bad('ABCDEF', w)}") for w in ["CBEFDA", "DEBCFA", "BDEFAC", "CEDFBA"]), src=B2_25, duree=5),
        o("tx6", r"Exercice 2 (Recherches, 4 points). $\lambda=\{1, 3, 8, 15, 23, 29, 32, 35, 38, 42, 47, 51, 55\}$. Nombre de comparaisons entre la valeur cherchée et un élément, pour $36$ et pour $42$ : (a) recherche séquentielle sans tenir compte de l'ordre ; (b) en tenant compte de l'ordre ; (c) recherche dichotomique.",
          f"(a) $36$ : ${len(_LB)}$ (absente, toute la liste) ; $42$ : ${_LB.index(42) + 1}$.\n\n"
          f"(b) $36$ : ${sum(e < 36 for e in _LB) + 1}$ (arrêt sur $38$) ; $42$ : ${sum(e < 42 for e in _LB) + 1}$.\n\n"
          f"(c) $36$ : valeurs rencontrées {', '.join(str(_LB[m]) for _, _, m in _calls(_LB, 36))}, ${len(_calls(_LB, 36))}$ étapes de $2$ comparaisons : ${2 * len(_calls(_LB, 36))}$. "
          f"$42$ : {', '.join(str(_LB[m]) for _, _, m in _calls(_LB, 42))} : $2$ comparaisons sur $32$, puis l'égalité avec $42$ : $3$ ($4$ si l'on compte $2$ comparaisons par étape).\n\n"
          "Pas de corrigé officiel : convention du cours, égalité testée d'abord.", src=B2_25, duree=8),
        o("tx7", r"Exercice 3 (Chemin de dichotomie, 3 points). Recherche dichotomique de $66$ dans des listes croissantes. Ces suites de valeurs rencontrées sont-elles possibles ? Sinon, première valeur qui pose problème. 82-29-47-67-75-66 ; 85-45-68-55-58-66 ; 87-35-62-75-70-66 ; 37-67-54-61-68-66.",
          "\n\n".join(f"{s} : " + ("oui" if _path_bad([int(t) for t in s.split("-")], 66) is None else f"non, {_path_bad([int(t) for t in s.split('-')], 66)}") for s in ["82-29-47-67-75-66", "85-45-68-55-58-66", "87-35-62-75-70-66", "37-67-54-61-68-66"])
          + "\n\nAprès $67 > 66$, toutes les valeurs suivantes sont $< 67$ : $75$ et $68$ sont impossibles.", src=B2_25, duree=5),
    ]},
]

VARIANTS = {
    "t41": [tv("lrec", "premier(cons(8, cons(1, listevide)))", "8", r"premier(cons(e, l)) $=$ e.")],
    "t42": [tv("lrec", "premier(fin(cons(4, cons(9, cons(2, listevide)))))", "9", r"fin retire $4$ ; premier $=9$.")],
    "t43": [tv("lrec", "contenu(succ(tête(cons(5, cons(1, cons(8, listevide))))))", "1", r"tête : place de $5$ ; succ : place de $1$.")],
    "t44": [tv("lrec", "fin(cons(2, cons(4, listevide)))", "cons(4, listevide)", r"fin(cons(e, l)) $=$ l.")],
    "t51": [tv("liter", "longueur(supprimer(insérer(insérer(listevide, 1, 5), 2, 8), 1))", "1", r"$+1$, $+1$, $-1$.")],
    "t52": [tv("liter", "ième(insérer(insérer(listevide, 1, 2), 2, 7), 2)", "7", r"$\langle 2, 7\rangle$.")],
    "t53": [tv("liter", "insérer(insérer(insérer(listevide, 1, 1), 1, 2), 3, 3)", "⟨2, 1, 3⟩", r"$\langle 1\rangle$, $\langle 2, 1\rangle$, puis $3$ au rang $3$.")],
    "t54": [tv("liter", "supprimer(insérer(insérer(insérer(listevide, 1, 4), 2, 5), 3, 6), 1)", "⟨5, 6⟩", r"$\langle 4, 5, 6\rangle$ sans le rang $1$.")],
    "t63": [tv("lrec", "concaténer(cons(5, listevide), cons(6, cons(7, listevide)))", "cons(5, cons(6, cons(7, listevide)))", r"cons(5, concaténer(listevide, l2)) $=$ cons(5, l2).")],
    "t71": [tv("pile", "sommet(empiler(empiler(pilevide, 8), 2))", "2", r"sommet(empiler(p, e)) $=$ e.")],
    "t72": [tv("pile", "sommet(dépiler(empiler(empiler(empiler(pilevide, 1), 2), 3)))", "2", r"On retire $3$ ; sommet $2$.")],
    "t76": [tv("pile", "empiler(dépiler(empiler(empiler(pilevide, 4), 6)), 8)", "empiler(empiler(pilevide, 4), 8)", r"dépiler retire $6$ ; on empile $8$.")],
    "t81": [tv("file", "premier(enfiler(enfiler(filevide, 9), 1))", "9", r"Premier enfilé, premier lu.")],
    "t82": [tv("file", "premier(défiler(enfiler(enfiler(enfiler(filevide, 1), 2), 3)))", "2", r"On défile $1$.")],
    "t83": [tv("file", "défiler(enfiler(enfiler(filevide, 6), 4))", "enfiler(filevide, 4)", r"On retire $6$, il reste $4$.")],
    "t85": [tv("file", "premier(enfiler(défiler(enfiler(enfiler(filevide, 5), 6)), 7))", "6", r"$5, 6$ ; on défile : $6$ ; on enfile $7$ : $6, 7$.")],
    "t101": [{"enonce": r"File statique circulaire, Nbmax $=6$, indices de $1$ à $6$. La queue vaut $6$ ; on enfile un élément. Nouvelle queue ?", "calc": "(6 % 6) + 1", "ans": "1", "sol": r"Après $6$ on revient à $1$."}],
    "t102": [{"enonce": r"File statique circulaire, Nbmax $=8$. La tête vaut $7$ ; on défile $3$ éléments. Nouvelle tête ?", "calc": "((7 + 3 - 1) % 8) + 1", "ans": "2", "sol": r"$8, 1, 2$ : la tête vaut $2$."}],
    "t103": [{"enonce": r"Pile statique, sommet $=0$ pour la pile vide. On empile $4$ éléments, on dépile $3$ fois, on empile $2$ éléments. Sommet ?", "calc": "4 - 3 + 2", "ans": "3", "sol": r"$4-3+2=3$."}],
    "t104": [{"enonce": r"Liste statique de longueur $10$. Insérer un élément au rang $4$ oblige à décaler combien d'éléments ?", "calc": "10 - 4 + 1", "ans": "7", "sol": r"Les rangs $4$ à $10$ avancent d'une case : $7$."}],
    "t111": [tv("ens", "card(ajouter(1, ajouter(2, ajouter(2, ensemblevide))))", "2", r"$\{1, 2\}$.")],
    "t114": [tv("multi", "card(supprimer(4, ajouter(3, ajouter(3, multiensemblevide))))", "2", r"$4$ absent : card inchangé.", enonce="Évaluer (multi-ensemble) :")],
}
for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["id"] in VARIANTS:
            _e["variants"] = VARIANTS[_e["id"]]

EXTRA_PARTS = []

QUIZ = [
    {"notion": "signature", "type": "qcm", "q": r"Une opération sans argument, comme vrai : $\to$ booléen, est :", "choix": [r"une constante", r"un observateur", r"une précondition", r"un axiome"], "bonne": 0},
    {"notion": "signature", "type": "vf", "q": r"Dans le nom _^_, les _ marquent la place des arguments.", "bonne": True},
    {"notion": "hierarchie", "type": "qcm", "q": r"Un observateur :", "choix": [r"a un argument de type défini et un résultat de type prédéfini", r"renvoie toujours le type défini", r"n'a pas d'argument", r"est toujours partiel"], "bonne": 0},
    {"notion": "hierarchie", "type": "vf", "q": r"Dans le type pile, sommet est une opération interne.", "bonne": False},
    {"notion": "axiomes", "type": "qcm", "q": r"La complétude d'un ensemble d'axiomes signifie :", "choix": [r"on peut déduire tout observateur appliqué à toute opération interne", r"aucun axiome n'en contredit un autre", r"toutes les opérations sont totales", r"il y a un axiome par opération"], "bonne": 0},
    {"notion": "axiomes", "type": "vf", "q": r"Une opération partielle reçoit une précondition « est-défini-ssi ».", "bonne": True},
    {"notion": "lrec", "type": "qcm", "q": r"premier(fin(cons(1, cons(2, listevide)))) vaut :", "choix": [r"$2$", r"$1$", r"listevide", r"indéfini"], "bonne": 0},
    {"notion": "lrec", "type": "vf", "q": r"fin(listevide) $=$ listevide.", "bonne": False},
    {"notion": "liter", "type": "qcm", "q": r"insérer(l, k, e) est défini pour :", "choix": [r"$1\le k\le$ longueur(l)$+1$", r"$1\le k\le$ longueur(l)", r"$0\le k\le$ longueur(l)", r"tout $k$"], "bonne": 0},
    {"notion": "liter", "type": "vf", "q": r"longueur(supprimer(l, k)) $=$ longueur(l)$-1$.", "bonne": True},
    {"notion": "conversion", "type": "qcm", "q": r"cons(e, l) s'écrit en liste itérative :", "choix": [r"insérer(l, 1, e)", r"insérer(l, longueur(l)$+1$, e)", r"accès(l, 1)", r"supprimer(l, 1)"], "bonne": 0},
    {"notion": "conversion", "type": "vf", "q": r"concaténer(listevide, l) $=$ l.", "bonne": True},
    {"notion": "pile", "type": "qcm", "q": r"sommet(dépiler(empiler(empiler(pilevide, 1), 2))) vaut :", "choix": [r"$1$", r"$2$", r"pilevide", r"indéfini"], "bonne": 0},
    {"notion": "pile", "type": "vf", "q": r"Une pile est une structure FIFO.", "bonne": False},
    {"notion": "file", "type": "qcm", "q": r"premier(enfiler(enfiler(filevide, 1), 2)) vaut :", "choix": [r"$1$", r"$2$", r"filevide", r"indéfini"], "bonne": 0},
    {"notion": "file", "type": "vf", "q": r"estvide(f) $=$ Faux $\Rightarrow$ défiler(enfiler(f, e)) $=$ enfiler(défiler(f), e).", "bonne": True},
    {"notion": "repr", "type": "qcm", "q": r"La représentation dynamique d'une liste permet :", "choix": [r"d'insérer sans décaler", r"l'accès direct au $k$-ième élément", r"d'éviter tout pointeur", r"de connaître la longueur sans parcours"], "bonne": 0},
    {"notion": "repr", "type": "vf", "q": r"Dans une file statique circulaire, l'indice suivant se calcule avec un modulo Nbmax.", "bonne": True},
    {"notion": "recherche", "type": "qcm", "q": r"On empile A, B, C dans cet ordre. Quel ordre de sortie est impossible ?", "choix": [r"C A B", r"B A C", r"A B C", r"C B A"], "bonne": 0},
    {"notion": "recherche", "type": "vf", "q": r"En dichotomie, après avoir rencontré $67$ en cherchant $66$, on ne peut plus rencontrer $68$.", "bonne": True},
    {"notion": "ensemble", "type": "qcm", "q": r"card(ajouter(2, ajouter(2, ensemblevide))) vaut :", "choix": [r"$1$", r"$2$", r"$0$", r"indéfini"], "bonne": 0},
    {"notion": "ensemble", "type": "vf", "q": r"Dans un multi-ensemble, card(ajouter(x, me)) $=$ card(me)$+1$ même si x est déjà présent.", "bonne": True},
]

_F = {
    1: r"nom : type$_1$ x type$_2$ $\to$ résultat · sans argument : constante · _ : place d'un argument",
    2: r"défini : types · prédéfini : utilise · interne : résultat de type défini · observateur : résultat prédéfini",
    3: r"axiomes : observateurs $\circ$ opérations internes · partielle : est-défini-ssi · consistance · complétude",
    4: r"fin(cons(e, l)) $=$ l · premier(cons(e, l)) $=$ e · succ(tête(l)) $=$ tête(fin(l)) · premier(l) $=$ contenu(tête(l))",
    5: r"insérer décale les rangs $\ge k$ · supprimer ramène les rangs $> k$ · insérer : $1\le k\le$ longueur$+1$ · contenu(accès(l, k)) $=$ ième(l, k)",
    6: r"tête(l) $=$ accès(l, 1) · fin(l) $=$ supprimer(l, 1) · cons(e, l) $=$ insérer(l, 1, e) · concaténer(cons(e, l), l2) $=$ cons(e, concaténer(l, l2))",
    7: r"dépiler(empiler(p, e)) $=$ p · sommet(empiler(p, e)) $=$ e · estvide(pilevide) $=$ Vrai",
    8: r"f vide : premier(enfiler(f, e)) $=$ e · f non vide : premier(enfiler(f, e)) $=$ premier(f) · défiler(enfiler(f, e)) $=$ enfiler(défiler(f), e)",
    9: r"un axiome par opération interne qui construit la valeur · cas de base $+$ cas récursif",
    10: r"suivant $=(i \bmod \text{Nbmax})+1$ · statique : décalages · dynamique : chaînage",
    11: r"x $\in$ e : card inchangé par ajouter · multi-ensemble : card$+1$ · nboccurrences",
    12: r"mystère : supprime les rangs x à y · supprime-sup : listevide, puis cons selon e > x ou e $\le$ x",
    13: r"pile : sortie seulement du sommet · file : ordre d'entrée · séquentielle triée : arrêt au premier $\ge x$ · milieu $=\lfloor (g+d)/2\rfloor$, arrêt si trouvé ou g $=$ d",
    14: r"pile ou file : rejouer les entrées · dichotomie : g, d, milieu à chaque appel, arrêt si g $=$ d",
    15: r"ordre de sortie d'une pile · comparaisons : séquentielle, triée, dichotomie ($2$ par étape) · chemin : chaque valeur borne les suivantes",
}
FORMULES = {e["id"]: _F[lvl["n"]] for lvl in LEVELS for e in lvl["exos"]}
