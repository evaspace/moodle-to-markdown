"""Level path: S1 algorithmics, Caml and recursion (purely functional Caml, recursion, lists, higher order).

Sources: the Moodle course « [algo] Caml et récursivité » (course sheet, « Conseils pour la récursivité »,
« Conseils pour les listes », « Hanoï », QCM programme) and the two past B1 exams of the Epidocs Past-Exams repo:
`S1/Midterms/Algo/2028/CAML` (B1 #1, October 2023, with a graded copy) and `S1/Midterms/Algo/2029/CAML`
(B1, 30 October 2024). Levels 13 and 14 are these two exams.

Every Caml phrase of this file is replayed in a real OCaml toplevel by `parcours/check_caml.py` (OCaml 4.14 in a
throwaway Alpine container): `CHECKS` holds (code, expected toplevel answer) pairs, built by the helpers below.
build.py itself cannot run OCaml; run the checker after any change here.
Exam rule kept in every model solution: no predefined function except failwith and invalid_arg.
"""

SUBJECT = {
    "id": "algo-s1-caml",
    "ordre": 610,
    "matiere": "algo",
    "semestre": "S1",
    "ecue": "Caml et récursivité",
    "titre": "Caml et récursivité : fonctions, filtrage, récursivité, listes",
    "chapitres_moodle": ["[algo] Caml et récursivité/01_🐫 Caml - Récursivité"],
    "td": "Séminaire (jours 1 à 8, 6 QCM), conseils pour la récursivité et les listes, Hanoï",
    "examens": ["Examen écrit B1 de Caml (1 h 30)"],
}

CHECKS = []  # (code, expected toplevel answer), replayed by parcours/check_caml.py


def _blk(s):
    return f"```\n{s}\n```"


def _ev(code, ans, sol, enonce):
    CHECKS.append((code, ans))
    return {"enonce": f"{enonce}\n\n{_blk(code)}", "sol": f"**Réponse de Caml :**\n\n{_blk(ans)}\n\n{sol}"}


EV = "Donner la réponse de Caml à chaque phrase :"


def ev(id, code, ans, sol, enonce=EV, src=None, duree=2):
    """« What does Caml answer? » exercise; the toplevel answer is checked by check_caml.py."""
    return {"id": id, "kind": "open", **_ev(code, ans, sol, enonce), "src": src or C, "duree": duree}


def evv(code, ans, sol, enonce=EV):
    """Variant of an ev() exercise, checked too."""
    return _ev(code, ans, sol, enonce)


def _session(tests):
    return "\n".join(f"# {p};;\n{a}" for p, a in tests)


def w(id, enonce, code, val, tests, sol="", src=None, duree=6):
    """« Write the function » exercise: the model code must give `val` then every example answer of `tests`."""
    CHECKS.append((code + ";;\n" + "\n".join(p + ";;" for p, _ in tests), val + "\n" + "\n".join(a for _, a in tests)))
    body = f"{_blk(code + ' ;;')}\n\n{_blk(val)}"
    return {"id": id, "kind": "open", "enonce": f"{enonce}\n\n{_blk(_session(tests))}",
            "sol": body + (f"\n\n{sol}" if sol else ""), "src": src or C, "duree": duree}


def v(id, enonce, calc, ans, sol, src=None, duree=2):
    return {"id": id, "kind": "value", "enonce": enonce, "calc": calc, "ans": ans, "sol": sol, "src": src or C, "duree": duree}


def o(id, enonce, sol, src=None, duree=3):
    return {"id": id, "kind": "open", "enonce": enonce, "sol": sol, "src": src or C, "duree": duree}


C = "Moodle Caml, fiche de cours et séminaire"
R = "Moodle Caml, « Conseils pour la récursivité »"
L = "Moodle Caml, « Conseils pour les listes »"
H = "Moodle Caml, « Hanoï »"
A23 = "Examen B1 Caml, octobre 2023 (Past-Exams 2028/CAML)"
A24 = "Examen B1 Caml, 30 octobre 2024 (Past-Exams 2029/CAML)"

# ---------------------------------------------------------------- course

NOTIONS = [
    {"id": "bases", "titre": "Expressions, types de base, définitions",
     "formule": r"`int` : `+ - * / mod` · `float` : `+. -. *. /.` · `string` : `^` · `bool` : `true false && || not` · `char` : `'a'` · comparaisons `= <> < > <= >=` · `let x = e ;;` (global) · `let x = e1 in e2` (local) · réponse : `- : type = valeur` ou `val x : type = valeur`",
     "exemple": r"`7 / 2 ;;` répond `- : int = 3` ; `1 + 2.5 ;;` est une erreur de type",
     "cours": r"Caml évalue chaque phrase terminée par `;;` et répond par son type puis sa valeur. Pas de conversion implicite : les opérateurs flottants ont un point (`+.`), `1 + 2.5` est refusé. `let` lie un nom à une valeur pour toute la suite ; `let … in` ne le lie que dans l'expression qui suit. Une liaison ne change jamais : redéfinir `x` crée une nouvelle liaison."},
    {"id": "fonctions", "titre": "Fonctions à un ou plusieurs paramètres",
     "formule": r"`let f x = e` $\equiv$ `let f = function x -> e` · type `t1 -> t2` · `let f x y = e` : `t1 -> t2 -> t3` · application prioritaire : `f 2 + 1` $=$ `(f 2) + 1` · application partielle : `f 2` est une fonction · `'a` : type quelconque (polymorphe)",
     "exemple": r"`let somme x y = x + y ;;` répond `val somme : int -> int -> int = <fun>` ; `somme 1` est de type `int -> int`",
     "cours": r"Une fonction est une valeur comme une autre, affichée `<fun>`. Une fonction à deux paramètres est une fonction qui renvoie une fonction : `int -> int -> int` se lit `int -> (int -> int)`. L'application se fait par simple juxtaposition et passe avant tous les opérateurs : il faut des parenthèses pour `f (n - 1)` ou `f (-2)`. Les valeurs libres d'une fonction sont celles connues à sa définition (liaison statique)."},
    {"id": "alternative", "titre": "Alternative et booléens",
     "formule": r"`if c then e1 else e2` : `c` booléen, `e1` et `e2` de même type · `&&`, `||` paresseux : `a && b` n'évalue pas `b` si `a` est faux · `not`",
     "exemple": r"`let abs x = if x < 0 then -x else x ;;`",
     "cours": r"L'alternative est une expression : elle a une valeur, donc ses deux branches ont le même type. `&&` et `||` évaluent de gauche à droite et s'arrêtent dès que le résultat est connu : `true || 1 / 0 = 0` vaut `true`. On s'en sert pour arrêter un calcul dès que la réponse est trouvée."},
    {"id": "exceptions", "titre": "Exceptions : failwith, invalid_arg",
     "formule": r"`failwith \"msg\"` : déclenche `Failure \"msg\"` · `invalid_arg \"msg\"` : déclenche `Invalid_argument \"msg\"` · type de `failwith` : `string -> 'a` · réponse : `Exception: Invalid_argument \"msg\".`",
     "exemple": r"`if n < 0 then invalid_arg \"fact: n < 0\" else …`",
     "cours": r"`invalid_arg` signale un paramètre hors domaine (n négatif, k nul…) ; `failwith` signale un échec du calcul (liste trop courte, élément absent). Comme elles ne rendent jamais de valeur, elles ont n'importe quel type et se placent dans une branche de `if` ou de `match` sans gêner le typage. À l'examen, ce sont les seules fonctions prédéfinies permises."},
    {"id": "filtrage", "titre": "Filtrage, n-uplets, fonctions anonymes",
     "formule": r"`match e with m1 -> e1 | m2 -> e2` · `function m1 -> e1 | …` (filtre le paramètre) · `_` : tout · `m when c` : garde · motifs testés dans l'ordre · n-uplet `(a, b)` : type `t1 * t2` · `fun x -> e` : fonction anonyme",
     "exemple": r"`let nom = function 1 -> \"un\" | _ -> \"autre\" ;;`",
     "cours": r"Le filtrage compare une valeur à des motifs, dans l'ordre, et prend la première branche qui correspond ; un motif peut nommer des morceaux (`(x, y)`, `e :: l`) et être complété par une garde `when`. Il doit être exhaustif (sinon avertissement, puis exception `Match_failure`). Un n-uplet regroupe des valeurs de types différents ; `fun x -> …` crée une fonction sans la nommer."},
    {"id": "recursivite", "titre": "Récursivité simple",
     "formule": r"`let rec f n = …` · cas d'arrêt d'abord · cas récursif : problème « plus petit » (`n - 1`, `n / 10`…) · les appels doivent tendre vers un cas d'arrêt · sans `rec` : `Error: Unbound value f`",
     "exemple": r"`let rec fact n = if n = 0 then 1 else n * fact (n - 1) ;;`",
     "cours": r"Méthode du cours : préciser ce que calcule la fonction, ses paramètres et son résultat (spécification) ; trouver les cas ; écrire l'« équation de récurrence » : cas de base (arrêt) et expression du problème en fonction du même problème plus petit ; vérifier que chaque appel se rapproche d'un cas d'arrêt."},
    {"id": "multiple", "titre": "Récursivité à plusieurs appels",
     "formule": r"plusieurs appels récursifs par cas · Fibonacci : $F_n=F_{n-1}+F_{n-2}$ · Pascal : $\binom np=\binom{n-1}{p-1}+\binom{n-1}{p}$ · Hanoï : $n-1$ disques vers l'intermédiaire, $1$ disque, $n-1$ disques vers la destination ; $2^n-1$ déplacements",
     "exemple": r"`let rec fibo n = if n < 2 then n else fibo (n - 1) + fibo (n - 2) ;;`",
     "cours": r"Quand un cas fait deux appels, le nombre d'appels peut exploser : `fibo` recalcule sans cesse les mêmes valeurs (nombre d'appels exponentiel). Hanoï, lui, a besoin de ses deux appels : on déplace $n-1$ disques sur le piquet intermédiaire, le grand disque sur la destination, puis les $n-1$ disques par-dessus ; le piquet intermédiaire vaut $6-$source$-$destination."},
    {"id": "optimisation", "titre": "Optimisation : fonctions chapeaux, accumulateurs",
     "formule": r"fonction chapeau : teste les paramètres une seule fois puis appelle la fonction récursive interne · accumulateur : paramètre en plus, renvoyé au cas d'arrêt · `let p = … in` : ne pas répéter un calcul · arrêter dès que la réponse est connue",
     "exemple": r"`let fact n = if n < 0 then invalid_arg \"…\" else let rec f = function 0 -> 1 | n -> n * f (n - 1) in f n ;;`",
     "cours": r"Règles du cours : éviter les calculs inutiles, ne pas répéter un calcul, s'arrêter dès qu'une réponse est donnée. La fonction chapeau vérifie la validité des paramètres avant la récursion (sinon le test est refait à chaque appel), élimine les cas particuliers et donne leur valeur initiale aux paramètres ajoutés (accumulateur, compteur)."},
    {"id": "listes", "titre": "Listes : parcours d'une liste",
     "formule": r"`[]` · `e :: l` · `[1; 2; 3]` $=$ `1 :: 2 :: 3 :: []` · type `'a list` (éléments de même type) · `@` : concaténation · motifs `[]` (arrêt) et `e :: l` · réponse pour `e :: l` en fonction de celle pour `l`",
     "exemple": r"`let rec length = function [] -> 0 | _ :: l -> 1 + length l ;;`",
     "cours": r"Une liste est vide (`[]`) ou formée d'une tête et d'une liste (`e :: l`). Le traitement est récursif : la liste vide est le cas d'arrêt ; pour `e :: l`, on cherche ce qu'il faut faire à la réponse sur `l` pour obtenir celle sur `e :: l`. Si le parcours peut s'arrêter avant la fin (élément trouvé, propriété fausse), il y a un autre cas d'arrêt. Attention : `[1, 2, 3]` est une liste d'un seul triplet."},
    {"id": "listes2", "titre": "Listes : deux listes, cas `e1 :: e2 :: l`, couples",
     "formule": r"deux listes : `([], [])`, `(l, [])`, `([], l)`, `(e1 :: l1, e2 :: l2)` · tête insuffisante : `[]`, `[e]`, `e1 :: e2 :: l` · éléments structurés : `(a, b) :: l` · accumulateur seulement si la récursion pure échoue",
     "exemple": r"`let rec croissante = function e1 :: (e2 :: _ as l) -> e1 <= e2 && croissante l | _ -> true ;;`",
     "cours": r"Le nombre de listes à parcourir donne les motifs. Avec deux listes, on se demande si on avance dans les deux à la fois ou dans une seule (alors au moins deux cas selon la liste dont on retire la tête, comme pour une fusion). Quand la tête ne suffit pas (liste croissante), on distingue la liste vide, un seul élément et au moins deux éléments."},
    {"id": "ordre_sup", "titre": "Fonctions d'ordre supérieur",
     "formule": r"fonction en paramètre : `('a -> 'b) -> 'a list -> 'b list` · `map f l` · `for_all p l`, `exists p l` · `filter p l` · `fold f acc l` · ordre en paramètre : `order : 'a -> 'a -> bool`",
     "exemple": r"`let rec map f = function [] -> [] | e :: l -> f e :: map f l ;;`",
     "cours": r"Une fonction peut prendre une fonction en paramètre (ou en renvoyer une). On écrit une seule fois un parcours général (appliquer, tester, filtrer, cumuler) et on lui donne le traitement à faire. Pour trier dans n'importe quel ordre, on passe la fonction de comparaison : `insert_x x order l` sert pour l'ordre croissant comme pour le décroissant."},
]

_S = "let somme x y = x + y"
_F = "let rec fact n = if n = 0 then 1 else n * fact (n - 1)"
_LEN = "let rec len_ok n = function\n    [] -> true\n  | _ :: l -> n > 0 && len_ok (n - 1) l"
_INS = "let rec insert_x x order = function\n    [] -> [x]\n  | e :: l -> if order x e then x :: e :: l else e :: insert_x x order l"
_RMX = "let rec remove_x x = function\n    [] -> []\n  | e :: l when e = x -> remove_x x l\n  | e :: l -> e :: remove_x x l"
_MYS = ("let mystery lst =\n  let rec tmp lst acc switch = match (lst, switch) with\n"
        "      ([], true) -> tmp [] acc false\n"
        "    | ([], false) -> (match acc with\n                        [] -> []\n                      | h :: acc -> h :: tmp lst acc true)\n"
        "    | (h :: t, true) -> h :: tmp t (h :: acc) true\n  in\n  tmp lst [] true")
_LT = "(function x -> function y -> x < y)"
_GT = "(function x -> function y -> x > y)"

LEVELS = [
    {"n": 1, "titre": "Expressions et types de base", "notions": ["bases"], "exos": [
        ev("k11", "3 + 4 * 2 ;;", "- : int = 11", r"`*` passe avant `+` : $3+8=11$.", duree=1),
        ev("k12", "7 / 2 ;;\n7 mod 2 ;;\n-7 / 2 ;;", "- : int = 3\n- : int = 1\n- : int = -3",
           r"`/` sur les entiers est la division entière (tronquée vers $0$) ; `mod` donne le reste."),
        ev("k13", "1.5 +. 2. ;;\n2. *. 3.5 ;;", "- : float = 3.5\n- : float = 7.", r"Opérateurs flottants avec un point ; `7.` est l'écriture Caml de $7{,}0$."),
        ev("k14", "1 + 2.5 ;;", "Error: This expression has type float but an expression was expected of type int",
           r"Pas de conversion implicite : `+` attend deux `int`. Il faut `1. +. 2.5` (ou `float_of_int 1 +. 2.5`)."),
        ev("k15", "\"Info\" ^ \"-\" ^ \"sup\" ;;\n'a' < 'b' ;;", "- : string = \"Info-sup\"\n- : bool = true",
           r"`^` concatène deux chaînes ; les caractères se comparent dans l'ordre du code ASCII."),
        ev("k16", "let x = 3 * 4 ;;\nlet y = x + 1 in y * 2 ;;\nx ;;", "val x : int = 12\n- : int = 26\n- : int = 12",
           r"`let … in` : `y` n'existe que dans `y * 2`, et Caml répond `-` (pas de nom global). `x` reste lié à $12$."),
        ev("k17", "let x = 5 ;;\nlet x = x * 2 ;;\nx = 10 ;;", "val x : int = 5\nval x : int = 10\n- : bool = true",
           r"La seconde définition crée une nouvelle liaison de `x` (calculée avec l'ancienne). Dans une expression, `=` est la comparaison."),
    ]},
    {"n": 2, "titre": "Fonctions à un paramètre", "notions": ["fonctions", "bases"], "exos": [
        ev("k21", "let double x = 2 * x ;;\ndouble 5 ;;", "val double : int -> int = <fun>\n- : int = 10",
           r"`2 * x` impose `x : int` et un résultat `int`.", duree=1),
        ev("k22", "let f = function x -> x +. 1. ;;\nf 2. ;;", "val f : float -> float = <fun>\n- : float = 3.",
           r"`let f = function x -> e` est la même définition que `let f x = e`."),
        ev("k23", "let carre x = x * x ;;\ncarre 2 + 1 ;;\ncarre (2 + 1) ;;", "val carre : int -> int = <fun>\n- : int = 5\n- : int = 9",
           r"L'application passe avant `+` : `carre 2 + 1` $=4+1$."),
        ev("k24", "let id x = x ;;\nid 'z' ;;\nid \"z\" ;;", "val id : 'a -> 'a = <fun>\n- : char = 'z'\n- : string = \"z\"",
           r"Rien ne contraint `x` : type polymorphe `'a`, la même fonction sert pour tout type."),
        ev("k25", "let est_pair n = n mod 2 = 0 ;;\nest_pair 7 ;;", "val est_pair : int -> bool = <fun>\n- : bool = false",
           r"Le corps est une comparaison : résultat `bool`. `mod` passe avant `=`."),
        w("k26", r"Écrire la fonction `cube x` qui renvoie $x^3$.", "let cube x = x * x * x", "val cube : int -> int = <fun>",
          [("cube 3", "- : int = 27"), ("cube (-2)", "- : int = -8")], r"`cube -2` serait lu `cube - 2` (soustraction) : il faut `cube (-2)`.", duree=3),
        ev("k27", "let a = 10 ;;\nlet ajoute x = x + a ;;\nlet a = 100 ;;\najoute 1 ;;",
           "val a : int = 10\nval ajoute : int -> int = <fun>\nval a : int = 100\n- : int = 11",
           r"Liaison statique : `ajoute` utilise le `a` connu à sa définition ($10$). Redéfinir `a` ensuite ne la change pas.", duree=3),
    ]},
    {"n": 3, "titre": "Plusieurs paramètres, application partielle", "notions": ["fonctions"], "exos": [
        ev("k31", _S + " ;;", "val somme : int -> int -> int = <fun>", r"Deux paramètres : `int -> int -> int`, à lire `int -> (int -> int)`.", duree=1),
        ev("k32", _S + " ;;\nlet incr = somme 1 ;;\nincr 41 ;;", "val somme : int -> int -> int = <fun>\nval incr : int -> int = <fun>\n- : int = 42",
           r"Application partielle : `somme 1` attend encore `y`, c'est une fonction `int -> int`."),
        ev("k33", "let moyenne a b = (a +. b) /. 2. ;;\nmoyenne 3. 4. ;;", "val moyenne : float -> float -> float = <fun>\n- : float = 3.5",
           r"`+.` et `/.` imposent des flottants partout."),
        ev("k34", "let f x y = x ^ y ;;\nf \"ab\" ;;", "val f : string -> string -> string = <fun>\n- : string -> string = <fun>",
           r"Un seul argument donné : la réponse est une fonction, pas une erreur."),
        ev("k35", _S + " ;;\nsomme 1 2 * 3 ;;\nsomme 1 (2 * 3) ;;", "val somme : int -> int -> int = <fun>\n- : int = 9\n- : int = 7",
           r"`somme 1 2 * 3` se lit `(somme 1 2) * 3`."),
        ev("k36", "let g = function x -> function y -> x - y ;;\ng 10 3 ;;", "val g : int -> int -> int = <fun>\n- : int = 7",
           r"Même type que `let g x y = x - y` : une fonction qui renvoie une fonction."),
        w("k37", r"Écrire la fonction `volume l w h` qui renvoie le volume d'un pavé de dimensions entières.", "let volume l w h = l * w * h",
          "val volume : int -> int -> int -> int = <fun>", [("volume 2 3 4", "- : int = 24"), ("volume 1 1 10", "- : int = 10")], duree=2),
    ]},
    {"n": 4, "titre": "Alternative et booléens", "notions": ["alternative"], "exos": [
        ev("k41", "let abs x = if x < 0 then -x else x ;;\nabs (-5) ;;", "val abs : int -> int = <fun>\n- : int = 5",
           r"Les deux branches sont des `int`.", duree=1),
        ev("k42", "if 3 > 2 then \"oui\" else 0 ;;", "Error: This expression has type int but an expression was expected of type string",
           r"Les deux branches d'un `if` doivent avoir le même type : la première impose `string`."),
        ev("k43", "true || 1 / 0 = 0 ;;\nfalse && 1 / 0 = 0 ;;", "- : bool = true\n- : bool = false",
           r"`||` et `&&` sont paresseux : la division par zéro n'est jamais évaluée."),
        ev("k44", "let f x = x > 0 && x mod 2 = 0 ;;\nf 4 ;;\nf (-2) ;;", "val f : int -> bool = <fun>\n- : bool = true\n- : bool = false",
           r"$-2$ est pair mais pas strictement positif."),
        w("k45", r"Écrire la fonction `max3 a b c` qui renvoie le plus grand de ses trois paramètres (sans fonction prédéfinie).",
          "let max3 a b c =\n  let m = if a > b then a else b in\n  if m > c then m else c", "val max3 : 'a -> 'a -> 'a -> 'a = <fun>",
          [("max3 1 5 3", "- : int = 5"), ("max3 'a' 'z' 'c'", "- : char = 'z'")], r"`>` compare toute valeur de même type : la fonction est polymorphe.", duree=4),
        w("k46", r"Écrire la fonction `signe x` qui renvoie $-1$, $0$ ou $1$ selon le signe de l'entier $x$.",
          "let signe x =\n  if x < 0 then -1\n  else if x = 0 then 0\n  else 1", "val signe : int -> int = <fun>",
          [("signe (-7)", "- : int = -1"), ("signe 0", "- : int = 0"), ("signe 3", "- : int = 1")], duree=3),
        ev("k47", "let bissextile a = (a mod 4 = 0 && a mod 100 <> 0) || a mod 400 = 0 ;;\nbissextile 1900 ;;\nbissextile 2024 ;;",
           "val bissextile : int -> bool = <fun>\n- : bool = false\n- : bool = true",
           r"$1900$ est divisible par $100$ mais pas par $400$ ; $2024$ est divisible par $4$ et pas par $100$.", duree=3),
    ]},
    {"n": 5, "titre": "Exceptions", "notions": ["exceptions", "alternative"], "exos": [
        ev("k51", "failwith \"oups\" ;;", "Exception: Failure \"oups\".", r"`failwith` déclenche l'exception `Failure`.", duree=1),
        ev("k52", "let inverse x = if x = 0. then failwith \"inverse: zero\" else 1. /. x ;;\ninverse 4. ;;\ninverse 0. ;;",
           "val inverse : float -> float = <fun>\n- : float = 0.25\nException: Failure \"inverse: zero\".",
           r"`failwith` a le type `string -> 'a` : la branche s'accorde avec `float`."),
        ev("k53", "invalid_arg \"f: n < 0\" ;;\n10 / 0 ;;", "Exception: Invalid_argument \"f: n < 0\".\nException: Division_by_zero.",
           r"`invalid_arg` déclenche `Invalid_argument` ; la division entière par zéro déclenche `Division_by_zero`."),
        w("k54", r"Écrire la fonction `div a b` (quotient entier) qui déclenche `Invalid_argument \"div: b = 0\"` si $b=0$.",
          "let div a b =\n  if b = 0 then invalid_arg \"div: b = 0\"\n  else a / b", "val div : int -> int -> int = <fun>",
          [("div 7 2", "- : int = 3"), ("div 1 0", "Exception: Invalid_argument \"div: b = 0\".")], duree=3),
        ev("k55", "let f x = if x then failwith \"non\" else 1 ;;\nf false ;;\nf true ;;",
           "val f : bool -> int = <fun>\n- : int = 1\nException: Failure \"non\".",
           r"La branche `failwith` prend le type de l'autre branche : `int`."),
        o("k56", r"Quand utiliser `invalid_arg` plutôt que `failwith` ?",
          r"`invalid_arg` : un paramètre est hors du domaine prévu par la spécification (entier négatif, $k$ nul…), l'appel n'aurait pas dû être fait. `failwith` : les paramètres sont valides mais le calcul échoue (liste trop courte, élément absent). Le message commence par le nom de la fonction, comme dans les annales : `\"nth: list too short\"`.", src=R, duree=2),
    ]},
    {"n": 6, "titre": "Filtrage, n-uplets, fonctions anonymes", "notions": ["filtrage"], "exos": [
        ev("k61", "let nom = function\n    1 -> \"un\"\n  | 2 -> \"deux\"\n  | _ -> \"beaucoup\" ;;\nnom 2 ;;\nnom 7 ;;",
           "val nom : int -> string = <fun>\n- : string = \"deux\"\n- : string = \"beaucoup\"", r"Les motifs sont essayés dans l'ordre ; `_` filtre tout le reste."),
        ev("k62", "let f x = match x with\n    0 -> \"nul\"\n  | n when n < 0 -> \"negatif\"\n  | _ -> \"positif\" ;;\nf (-3) ;;",
           "val f : int -> string = <fun>\n- : string = \"negatif\"", r"La garde `when` ajoute une condition au motif `n`."),
        ev("k63", "(1, 'a', \"b\") ;;\n[1, 2] ;;", "- : int * char * string = (1, 'a', \"b\")\n- : (int * int) list = [(1, 2)]",
           r"Un triplet a le type produit `int * char * string`. Dans une liste, la virgule fabrique un couple : `[1, 2]` est une liste d'un seul couple."),
        ev("k64", "let echange (a, b) = (b, a) ;;\nechange (1, true) ;;", "val echange : 'a * 'b -> 'b * 'a = <fun>\n- : bool * int = (true, 1)",
           r"Le motif `(a, b)` nomme les deux composantes ; elles peuvent avoir deux types différents."),
        ev("k65", "(fun x -> x * 3) 5 ;;\n(function (x, y) -> x + y) (2, 3) ;;", "- : int = 15\n- : int = 5",
           r"Fonctions anonymes appliquées directement."),
        w("k66", r"Écrire la fonction `xor a b` (ou exclusif) avec un filtrage sur le couple `(a, b)`.",
          "let xor a b = match (a, b) with\n    (true, false) | (false, true) -> true\n  | _ -> false", "val xor : bool -> bool -> bool = <fun>",
          [("xor true false", "- : bool = true"), ("xor true true", "- : bool = false")], duree=3),
        ev("k67", "let f = function\n    (x, 0) -> x\n  | (x, y) -> x / y ;;\nf (8, 0) ;;\nf (8, 2) ;;",
           "val f : int * int -> int = <fun>\n- : int = 8\n- : int = 4", r"Un seul paramètre : un couple d'entiers. Le premier motif traite $y=0$."),
    ]},
    {"n": 7, "titre": "Récursivité simple", "notions": ["recursivite"], "exos": [
        ev("k71", _F + " ;;\nfact 5 ;;", "val fact : int -> int = <fun>\n- : int = 120", r"$5\times4\times3\times2\times1\times1$.", duree=1),
        ev("k72", "let f n = if n = 0 then 1 else n * f (n - 1) ;;",
           "Error: Unbound value f\nHint: If this is a recursive definition,\nyou should add the 'rec' keyword on line 1",
           r"Sans `rec`, `f` n'est pas encore connu dans son propre corps."),
        w("k73", r"Écrire la fonction récursive `puissance x n` qui renvoie $x^n$ ($n\ge0$).",
          "let rec puissance x n =\n  if n = 0 then 1\n  else x * puissance x (n - 1)", "val puissance : int -> int -> int = <fun>",
          [("puissance 2 10", "- : int = 1024"), ("puissance 3 0", "- : int = 1")], r"Cas d'arrêt $x^0=1$ ; $x^n=x\times x^{n-1}$.", src=R, duree=4),
        w("k74", r"Écrire la fonction `somme_chiffres n` qui renvoie la somme des chiffres de l'entier $n\ge0$.",
          "let rec somme_chiffres n =\n  if n < 10 then n\n  else n mod 10 + somme_chiffres (n / 10)", "val somme_chiffres : int -> int = <fun>",
          [("somme_chiffres 1234", "- : int = 10"), ("somme_chiffres 7", "- : int = 7")], r"`n mod 10` est le dernier chiffre, `n / 10` le nombre sans lui.", src=R, duree=4),
        w("k75", r"Écrire la fonction `nb_chiffres n` qui renvoie le nombre de chiffres de l'entier $n\ge0$.",
          "let rec nb_chiffres n =\n  if n < 10 then 1\n  else 1 + nb_chiffres (n / 10)", "val nb_chiffres : int -> int = <fun>",
          [("nb_chiffres 0", "- : int = 1"), ("nb_chiffres 2024", "- : int = 4")], duree=4),
        w("k76", r"Écrire la fonction `pgcd a b` (algorithme d'Euclide, $a, b\ge0$).",
          "let rec pgcd a b =\n  if b = 0 then a\n  else pgcd b (a mod b)", "val pgcd : int -> int -> int = <fun>",
          [("pgcd 48 18", "- : int = 6"), ("pgcd 7 0", "- : int = 7")], r"$\mathrm{pgcd}(a, b)=\mathrm{pgcd}(b, a \bmod b)$ et $\mathrm{pgcd}(a, 0)=a$.", duree=4),
        v("k77", r"Avec `let rec fact n = if n = 0 then 1 else n * fact (n - 1)`, combien d'appels de `fact` (le premier compris) fait l'évaluation de `fact 5` ?",
          "6", "6", r"`fact 5`, `fact 4`, `fact 3`, `fact 2`, `fact 1`, `fact 0` : $6$ appels ($n+1$).", src=R),
    ]},
    {"n": 8, "titre": "Récursivité à plusieurs appels, Hanoï", "notions": ["multiple", "recursivite"], "exos": [
        w("k81", r"Écrire la fonction `fibo n` ($F_0=0$, $F_1=1$, $F_n=F_{n-1}+F_{n-2}$) directement d'après la définition.",
          "let rec fibo n =\n  if n < 2 then n\n  else fibo (n - 1) + fibo (n - 2)", "val fibo : int -> int = <fun>",
          [("fibo 10", "- : int = 55"), ("fibo 1", "- : int = 1")], r"Deux appels par cas récursif : simple à écrire, mais exponentiel (niveau suivant).", duree=4),
        v("k82", r"Combien d'appels de `fibo` (le premier compris) fait `fibo 5` avec la version à deux appels ?",
          "1 + (1 + (1 + (1 + 1 + 1) + 1) + (1 + 1 + 1)) + (1 + (1 + 1 + 1) + 1)", "15",
          r"$A(0)=A(1)=1$, $A(n)=1+A(n-1)+A(n-2)$ : $A(2)=3$, $A(3)=5$, $A(4)=9$, $A(5)=15$.", src=R, duree=3),
        v("k83", r"Hanoï : nombre minimal de déplacements pour une tour de $10$ disques ?", "2**10 - 1", "1023",
          r"$D(1)=1$, $D(n)=2D(n-1)+1$, donc $D(n)=2^n-1=1023$.", src=H),
        w("k84", r"Compléter la fonction `play n source destination` de `hanoi` (page « Hanoï » du Moodle) : elle affiche les déplacements, piquets $1$, $2$, $3$.",
          "let move source destination =\n  print_int source ;\n  print_string \" -> \" ;\n  print_int destination ;\n  print_newline () ;;\n"
          "let hanoi n =\n  let rec play n source destination =\n    if n > 0 then\n      begin\n        let inter = 6 - source - destination in\n"
          "        play (n - 1) source inter ;\n        move source destination ;\n        play (n - 1) inter destination\n      end\n  in\n"
          "  if n <= 0 then invalid_arg \"Hanoi: number of disks invalid\"\n  else play n 1 3",
          "val move : int -> int -> unit = <fun>\nval hanoi : int -> unit = <fun>",
          [("hanoi 2", "1 -> 2\n1 -> 3\n2 -> 3\n- : unit = ()"), ("hanoi 0", "Exception: Invalid_argument \"Hanoi: number of disks invalid\".")],
          r"Les piquets valent $1+2+3=6$ : l'intermédiaire est $6-$source$-$destination. $n-1$ disques vers l'intermédiaire, le grand vers la destination, puis les $n-1$ par-dessus.", src=H, duree=8),
        w("k85", r"Écrire la fonction `binom n p` ($0\le p\le n$) avec la relation de Pascal.",
          "let rec binom n p =\n  if p = 0 || p = n then 1\n  else binom (n - 1) (p - 1) + binom (n - 1) p", "val binom : int -> int -> int = <fun>",
          [("binom 5 2", "- : int = 10"), ("binom 6 0", "- : int = 1")], duree=4),
    ]},
    {"n": 9, "titre": "Optimisation : fonctions chapeaux et accumulateurs", "notions": ["optimisation", "exceptions", "recursivite"], "exos": [
        w("k91", r"Écrire `fact n` avec une fonction chapeau : le test $n<0$ n'est fait qu'une fois.",
          "let fact n =\n  if n < 0 then invalid_arg \"fact: n is not a natural\"\n  else\n    let rec fact_rec = function\n        0 -> 1\n      | n -> n * fact_rec (n - 1)\n    in\n    fact_rec n",
          "val fact : int -> int = <fun>", [("fact 5", "- : int = 120"), ("fact (-1)", "Exception: Invalid_argument \"fact: n is not a natural\".")],
          r"Version du cours. Sans chapeau, le test $n<0$ serait refait à chaque appel : $2n$ tests au lieu de $n$.", src=R, duree=5),
        v("k92", r"Version sans chapeau : `let rec fact n = if n < 0 then invalid_arg \"…\" else if n = 0 then 1 else n * fact (n - 1)`. Combien de tests `n < 0` fait `fact 10` ?",
          "11", "11", r"Un test par appel, de `fact 10` à `fact 0` : $11$. Avec la fonction chapeau : $1$.", src=R),
        w("k93", r"Écrire `fibo n` en temps linéaire : fonction chapeau et deux accumulateurs (les deux derniers termes).",
          "let fibo n =\n  let rec fib a b k =\n    if k = 0 then a\n    else fib b (a + b) (k - 1)\n  in\n  if n < 0 then invalid_arg \"fibo: n < 0\"\n  else fib 0 1 n",
          "val fibo : int -> int = <fun>", [("fibo 10", "- : int = 55"), ("fibo 50", "- : int = 12586269025")],
          r"`fib a b k` avance de $k$ termes en partant de $(F_i, F_{i+1})=(a, b)$ : $n+1$ appels au lieu d'un nombre exponentiel.", src=R, duree=6),
        w("k94", r"Écrire `puissance x n` en ne faisant qu'un appel récursif sur $n/2$ : $x^{2k}=(x^k)^2$, $x^{2k+1}=x(x^k)^2$.",
          "let rec puissance x n =\n  if n = 0 then 1\n  else\n    let p = puissance x (n / 2) in\n    if n mod 2 = 0 then p * p\n    else x * p * p",
          "val puissance : int -> int -> int = <fun>", [("puissance 2 10", "- : int = 1024"), ("puissance 3 5", "- : int = 243")],
          r"`let p = … in` : le calcul de $x^{n/2}$ n'est fait qu'une fois (écrire `puissance x (n / 2) * puissance x (n / 2)` referait tout deux fois).", src=R, duree=6),
        w("k95", r"Écrire `est_premier n` qui s'arrête dès qu'un diviseur est trouvé.",
          "let est_premier n =\n  let rec aux d = d * d > n || (n mod d <> 0 && aux (d + 1)) in\n  n >= 2 && aux 2",
          "val est_premier : int -> bool = <fun>", [("est_premier 97", "- : bool = true"), ("est_premier 91", "- : bool = false"), ("est_premier 1", "- : bool = false")],
          r"`&&` s'arrête au premier diviseur ; on ne teste que $d\le\sqrt n$.", src=R, duree=6),
        w("k96", r"La fonction `multiply` de la page « Conseils pour la récursivité » contient `mult_rec (x, y-1)`. Corriger la fonction.",
          "let multiply x y =\n  let rec mult_rec = function\n      0 -> 0\n    | y -> x + mult_rec (y - 1)\n  in\n  match x with\n      0 -> 0\n    | 1 -> y\n    | x -> if y < 0 then - mult_rec (-y) else mult_rec y",
          "val multiply : int -> int -> int = <fun>", [("multiply 3 (-4)", "- : int = -12"), ("multiply 0 5", "- : int = 0"), ("multiply 6 7", "- : int = 42")],
          r"`mult_rec` n'a qu'un paramètre, `y` (`x` est connu de la fonction chapeau) : l'appel est `mult_rec (y - 1)`. La version du Moodle est refusée par Caml (erreur de type).", src=R, duree=5),
    ]},
    {"n": 10, "titre": "Listes : parcourir une liste", "notions": ["listes"], "exos": [
        ev("ka1", "[1; 2; 3] ;;\n1 :: [2; 3] ;;\n[] ;;", "- : int list = [1; 2; 3]\n- : int list = [1; 2; 3]\n- : 'a list = []",
           r"`::` ajoute un élément en tête. La liste vide a le type polymorphe `'a list`.", src=L, duree=1),
        ev("ka2", "[1; 2] @ [3] ;;\n[[1]; []] ;;\n[1; 'a'] ;;",
           "- : int list = [1; 2; 3]\n- : int list list = [[1]; []]\nError: This expression has type char but an expression was expected of type int",
           r"`@` concatène. Les éléments d'une liste ont tous le même type.", src=L),
        w("ka3", r"Écrire la fonction `length lst` (nombre d'éléments).", "let rec length = function\n    [] -> 0\n  | _ :: l -> 1 + length l",
          "val length : 'a list -> int = <fun>", [("length [1; 2; 3]", "- : int = 3"), ("length []", "- : int = 0")],
          r"Réponse pour `e :: l` : celle pour `l` plus un.", src=L, duree=3),
        w("ka4", r"Écrire la fonction `sum lst` (somme d'une liste d'entiers).", "let rec sum = function\n    [] -> 0\n  | e :: l -> e + sum l",
          "val sum : int list -> int = <fun>", [("sum [1; 2; 3; 4]", "- : int = 10"), ("sum []", "- : int = 0")], src=L, duree=3),
        w("ka5", r"Écrire `count x lst` : nombre d'occurrences de `x` dans `lst`.",
          "let rec count x = function\n    [] -> 0\n  | e :: l -> if e = x then 1 + count x l else count x l",
          "val count : 'a -> 'a list -> int = <fun>", [("count 2 [2; 1; 2; 3]", "- : int = 2"), ("count 'z' ['a']", "- : int = 0")], src=L, duree=4),
        w("ka6", r"Écrire `mem x lst` (`x` est-il dans `lst` ?) qui s'arrête dès que `x` est trouvé.",
          "let rec mem x = function\n    [] -> false\n  | e :: l -> e = x || mem x l", "val mem : 'a -> 'a list -> bool = <fun>",
          [("mem 3 [1; 2; 3; 4]", "- : bool = true"), ("mem 5 [1; 2]", "- : bool = false")], r"`||` est paresseux : pas d'appel après avoir trouvé `x`.", src=L, duree=4),
        w("ka7", r"Écrire `nth lst k` : $k$-ième élément ($k\ge1$). `Invalid_argument \"nth: k <= 0\"` si $k\le0$, `Failure \"nth: list too short\"` si la liste est trop courte.",
          "let nth lst k =\n  let rec aux k = function\n      [] -> failwith \"nth: list too short\"\n    | e :: l -> if k = 1 then e else aux (k - 1) l\n  in\n  if k <= 0 then invalid_arg \"nth: k <= 0\"\n  else aux k lst",
          "val nth : 'a list -> int -> 'a = <fun>", [("nth ['a'; 'b'; 'c'] 2", "- : char = 'b'"), ("nth [1] 3", "Exception: Failure \"nth: list too short\"."),
                                                        ("nth [1] 0", "Exception: Invalid_argument \"nth: k <= 0\".")],
          r"Fonction chapeau pour le test de $k$ ; la récursion compte à rebours.", src=L, duree=6),
        w("ka8", r"Écrire `append l1 l2` (comme `l1 @ l2`, sans `@`).", "let rec append l1 l2 = match l1 with\n    [] -> l2\n  | e :: l -> e :: append l l2",
          "val append : 'a list -> 'a list -> 'a list = <fun>", [("append [1; 2] [3; 4]", "- : int list = [1; 2; 3; 4]"), ("append [] ['a']", "- : char list = ['a']")],
          r"On ne parcourt que `l1` : `l2` est recopiée telle quelle à la fin.", src=L, duree=4),
        w("ka9", r"Écrire `rev lst` (liste renversée) en temps linéaire, avec un accumulateur.",
          "let rev lst =\n  let rec aux acc = function\n      [] -> acc\n    | e :: l -> aux (e :: acc) l\n  in\n  aux [] lst",
          "val rev : 'a list -> 'a list = <fun>", [("rev [1; 2; 3]", "- : int list = [3; 2; 1]"), ("rev []", "- : 'a list = []")],
          r"Ici l'accumulateur est utile : on construit le résultat en avançant dans la liste (version récursive pure avec `@` : quadratique).", src=L, duree=5),
    ]},
    {"n": 11, "titre": "Listes : deux listes, `e1 :: e2 :: l`, couples", "notions": ["listes2", "listes"], "exos": [
        w("kb1", r"Écrire `croissante lst` : la liste est-elle triée par ordre croissant ?",
          "let rec croissante = function\n    [] | [_] -> true\n  | e1 :: e2 :: l -> e1 <= e2 && croissante (e2 :: l)",
          "val croissante : 'a list -> bool = <fun>", [("croissante [1; 2; 2; 5]", "- : bool = true"), ("croissante [3; 1]", "- : bool = false"), ("croissante []", "- : bool = true")],
          r"La tête seule ne suffit pas : trois cas (vide, un élément, au moins deux).", src=L, duree=5),
        w("kb2", r"Écrire `merge l1 l2` : fusion de deux listes croissantes en une liste croissante.",
          "let rec merge l1 l2 = match (l1, l2) with\n    ([], l) | (l, []) -> l\n  | (e1 :: r1, e2 :: r2) ->\n      if e1 <= e2 then e1 :: merge r1 l2\n      else e2 :: merge l1 r2",
          "val merge : 'a list -> 'a list -> 'a list = <fun>", [("merge [1; 4; 6] [2; 3; 7]", "- : int list = [1; 2; 3; 4; 6; 7]"), ("merge [] [5]", "- : int list = [5]")],
          r"Deux listes, un seul élément retiré à chaque appel : le cas non vide se divise selon la liste dont on prend la tête.", src=L, duree=6),
        w("kb3", r"Écrire `insert x lst` : insère `x` à sa place dans une liste croissante.",
          "let rec insert x = function\n    [] -> [x]\n  | e :: l -> if x <= e then x :: e :: l else e :: insert x l",
          "val insert : 'a -> 'a list -> 'a list = <fun>", [("insert 4 [1; 3; 5]", "- : int list = [1; 3; 4; 5]"), ("insert 9 []", "- : int list = [9]")],
          r"Arrêt dès que la place est trouvée : le reste de la liste est gardé tel quel.", src=L, duree=5),
        w("kb4", r"Écrire `combine l1 l2` : liste des couples ; `Invalid_argument \"combine: different lengths\"` si les longueurs diffèrent.",
          "let rec combine l1 l2 = match (l1, l2) with\n    ([], []) -> []\n  | (e1 :: r1, e2 :: r2) -> (e1, e2) :: combine r1 r2\n  | _ -> invalid_arg \"combine: different lengths\"",
          "val combine : 'a list -> 'b list -> ('a * 'b) list = <fun>",
          [("combine [1; 2] ['a'; 'b']", "- : (int * char) list = [(1, 'a'); (2, 'b')]"), ("combine [1] []", "Exception: Invalid_argument \"combine: different lengths\".")],
          r"Les deux listes avancent ensemble ; les deux cas `(l, [])` et `([], l)` non vides sont regroupés dans `_`.", src=L, duree=5),
        w("kb5", r"Écrire `sum_pairs lst` : pour une liste de couples d'entiers, la liste des sommes.",
          "let rec sum_pairs = function\n    [] -> []\n  | (a, b) :: l -> (a + b) :: sum_pairs l", "val sum_pairs : (int * int) list -> int list = <fun>",
          [("sum_pairs [(1, 2); (10, 5)]", "- : int list = [3; 15]")], r"Élément structuré : on filtre `(a, b) :: l` pour lire les deux valeurs.", src=L, duree=4),
        w("kb6", r"Écrire `last lst` : dernier élément ; `Invalid_argument \"last: empty list\"` si la liste est vide.",
          "let rec last = function\n    [] -> invalid_arg \"last: empty list\"\n  | [e] -> e\n  | _ :: l -> last l",
          "val last : 'a list -> 'a = <fun>", [("last [1; 2; 3]", "- : int = 3"), ("last []", "Exception: Invalid_argument \"last: empty list\".")],
          r"Le motif `[e]` (un seul élément) est l'arrêt normal ; il doit précéder `_ :: l`.", src=L, duree=4),
        ev("kb7", "let rec f = function\n    [] -> []\n  | [x] -> [x]\n  | x :: y :: l -> y :: x :: f l ;;\nf [1; 2; 3; 4; 5] ;;",
           "val f : 'a list -> 'a list = <fun>\n- : int list = [2; 1; 4; 3; 5]", r"Les éléments sont échangés deux à deux ; le dernier, seul, reste en place.", src=L, duree=3),
    ]},
    {"n": 12, "titre": "Fonctions d'ordre supérieur", "notions": ["ordre_sup", "listes"], "exos": [
        ev("kc1", "let applique f x = f (f x) ;;\napplique (fun x -> x * 2) 5 ;;", "val applique : ('a -> 'a) -> 'a -> 'a = <fun>\n- : int = 20",
           r"`f` est appliquée à son propre résultat : son type est `'a -> 'a`."),
        ev("kc2", "let compose f g x = f (g x) ;;", "val compose : ('a -> 'b) -> ('c -> 'a) -> 'c -> 'b = <fun>",
           r"`g x` est de type `'a` (le paramètre de `f`), `x` d'un type `'c` quelconque.", duree=3),
        w("kc3", r"Écrire `map f lst` : applique `f` à chaque élément.", "let rec map f = function\n    [] -> []\n  | e :: l -> f e :: map f l",
          "val map : ('a -> 'b) -> 'a list -> 'b list = <fun>", [("map (fun x -> x * x) [1; 2; 3]", "- : int list = [1; 4; 9]"), ("map (fun x -> x > 0) [-1; 2]", "- : bool list = [false; true]")], duree=4),
        w("kc4", r"Écrire `for_all p lst` : tous les éléments vérifient-ils le prédicat `p` ? (arrêt au premier qui échoue)",
          "let rec for_all p = function\n    [] -> true\n  | e :: l -> p e && for_all p l", "val for_all : ('a -> bool) -> 'a list -> bool = <fun>",
          [("for_all (fun x -> x mod 2 = 0) [2; 4; 6]", "- : bool = true"), ("for_all (fun x -> x > 0) [1; -1; 2]", "- : bool = false")], duree=4),
        w("kc5", r"Écrire `filter p lst` : les éléments qui vérifient `p`, dans l'ordre.",
          "let rec filter p = function\n    [] -> []\n  | e :: l -> if p e then e :: filter p l else filter p l", "val filter : ('a -> bool) -> 'a list -> 'a list = <fun>",
          [("filter (fun x -> x > 2) [1; 5; 2; 3]", "- : int list = [5; 3]")], duree=4),
        w("kc6", r"Écrire `fold f acc lst` : $f(\dots f(f(acc, e_1), e_2)\dots, e_n)$. Puis en déduire la somme d'une liste.",
          "let rec fold f acc = function\n    [] -> acc\n  | e :: l -> fold f (f acc e) l", "val fold : ('a -> 'b -> 'a) -> 'a -> 'b list -> 'a = <fun>",
          [("fold (fun a e -> a + e) 0 [1; 2; 3]", "- : int = 6"), ("fold (fun a e -> e :: a) [] [1; 2; 3]", "- : int list = [3; 2; 1]")],
          r"L'accumulateur porte le résultat partiel ; avec `e :: a`, `fold` renverse la liste.", duree=5),
        w("kc7", r"Écrire `count_if p lst` : nombre d'éléments qui vérifient `p`.",
          "let rec count_if p = function\n    [] -> 0\n  | e :: l -> (if p e then 1 else 0) + count_if p l", "val count_if : ('a -> bool) -> 'a list -> int = <fun>",
          [("count_if (fun c -> c = 'a') ['a'; 'b'; 'a']", "- : int = 2")], duree=4),
    ]},
    {"n": 13, "titre": "Niveau examen : B1 Caml octobre 2023", "notions": ["listes", "listes2", "optimisation", "exceptions", "ordre_sup"], "examen": True, "exos": [
        w("kx1", r"Exercice 1 (6,5 points). Écrire la fonction `insert_mult n x lst` qui insère l'élément `x` dans la liste `lst` après chaque groupe de `n` éléments. Elle déclenche `Invalid_argument` si `n` est négatif ou nul. Seules fonctions prédéfinies permises : `failwith` et `invalid_arg`.",
          "let insert_mult n x lst =\n  if n <= 0 then invalid_arg \"insert_mult: n must be > 0\"\n  else\n    let rec aux count = function\n        l when count = 0 -> x :: aux n l\n      | [] -> []\n      | e :: l -> e :: aux (count - 1) l\n    in\n    aux n lst",
          "val insert_mult : int -> 'a -> 'a list -> 'a list = <fun>",
          [("insert_mult 0 1 [1; 2; 3; 4; 5]", "Exception: Invalid_argument \"insert_mult: n must be > 0\"."), ("insert_mult 4 42 [10; 20; 30; 40]", "- : int list = [10; 20; 30; 40; 42]"),
           ("insert_mult 2 0 [1; 2; 3; 4; 5]", "- : int list = [1; 2; 0; 3; 4; 0; 5]"), ("insert_mult 3 'x' ['a'; 'b'; 'c'; 'd'; 'e'; 'f'; 'g']", "- : char list = ['a'; 'b'; 'c'; 'x'; 'd'; 'e'; 'f'; 'x'; 'g']"),
           ("insert_mult 1 42 []", "- : int list = []"), ("insert_mult 1 42 [10]", "- : int list = [10; 42]")],
          r"Fonction chapeau pour le test de `n` ; compteur `count` qui descend à $0$ : on insère `x` et on repart de `n`. Le cas `count = 0` passe avant `[]` : `x` est ajouté après un groupe complet même en fin de liste.", src=A23, duree=15),
        w("kx2", r"Exercice 2.1 (2 points). Écrire la fonction `remove_x x lst` qui supprime toutes les occurrences de `x` dans `lst`.",
          _RMX, "val remove_x : 'a -> 'a list -> 'a list = <fun>",
          [("remove_x 1 []", "- : int list = []"), ("remove_x \"apple\" [\"banana\"; \"apple\"; \"cherry\"; \"date\"; \"apple\"]", "- : string list = [\"banana\"; \"cherry\"; \"date\"]"),
           ("remove_x 5 [5; 5; 2; 3; 5; 1]", "- : int list = [2; 3; 1]"), ("remove_x true [true; false; true; false; true]", "- : bool list = [false; false]")],
          r"Parcours complet : un seul cas d'arrêt.", src=A23, duree=6),
        w("kx3", r"Exercice 2.2 (3 points). Écrire `remove_duplicates lst` qui supprime tous les doublons de `lst` (on garde la première occurrence). La fonction doit utiliser `remove_x`.",
          _RMX + " ;;\nlet rec remove_duplicates = function\n    [] -> []\n  | e :: l -> e :: remove_duplicates (remove_x e l)",
          "val remove_x : 'a -> 'a list -> 'a list = <fun>\nval remove_duplicates : 'a list -> 'a list = <fun>",
          [("remove_duplicates [3; 1; 2; 2; 3; 1; 4; 5; 5]", "- : int list = [3; 1; 2; 4; 5]"), ("remove_duplicates [42; 13; 42; 7; 7; 13; 42; 42]", "- : int list = [42; 13; 7]"),
           ("remove_duplicates [\"dog\"; \"cat\"; \"dog\"; \"rat\"; \"rat\"; \"bat\"]", "- : string list = [\"dog\"; \"cat\"; \"rat\"; \"bat\"]"),
           ("remove_duplicates [true; true; false; true; false; true; false]", "- : bool list = [true; false]")],
          r"On garde la tête et on retire ses autres occurrences avant de continuer.", src=A23, duree=8),
        w("kx4", r"Exercice 3 (8 points). Écrire `split sep lst` qui coupe `lst` en sous-listes dès que le prédicat `sep` est vérifié sur un élément. Ces éléments ne font partie d'aucune sous-liste ; les sous-listes restent dans l'ordre initial.",
          "let split sep lst =\n  let rec aux = function\n      [] -> [[]]\n    | e :: l ->\n        if sep e then [] :: aux l\n        else match aux l with\n            g :: r -> (e :: g) :: r\n          | [] -> [[e]]\n  in\n  if lst = [] then [] else aux lst",
          "val split : ('a -> bool) -> 'a list -> 'a list list = <fun>",
          [("split (function x -> x = ',') []", "- : char list list = []"), ("split (function x -> x = 3) [1; 2; 3; 4; 5]", "- : int list list = [[1; 2]; [4; 5]]"),
           ("split (function x -> x = 20) [10; 20; 30; 40; 50]", "- : int list list = [[10]; [30; 40; 50]]"), ("split (function x -> x = 0) [0; 1; 0; 2; 0; 3; 0; 4]", "- : int list list = [[]; [1]; [2]; [3]; [4]]")],
          r"Récursion pure : `aux` renvoie toujours au moins un groupe. Un séparateur ouvre un nouveau groupe vide ; un autre élément se place en tête du premier groupe. La fonction chapeau traite la liste vide. (Le cas `[] -> [[e]]` n'arrive jamais : il rend seulement le filtrage exhaustif.)", src=A23, duree=20),
    ]},
    {"n": 14, "titre": "Niveau examen : B1 Caml 30 octobre 2024", "notions": ["listes", "listes2", "ordre_sup", "exceptions", "filtrage"], "examen": True, "exos": [
        w("ky1", r"Exercice 1 (7 points). Écrire `check_list k lst` : `lst` (liste de listes) ne contient-elle que des listes de longueur $\le k$ ? `Invalid_argument` si $k<0$. Seules fonctions prédéfinies permises : `failwith` et `invalid_arg`.",
          "let check_list k lst =\n  " + _LEN.replace("\n", "\n  ") + "\n  in\n  let rec check = function\n      [] -> true\n    | l :: r -> len_ok k l && check r\n  in\n  if k < 0 then invalid_arg \"check_list: k < 0\"\n  else check lst",
          "val check_list : int -> 'a list list -> bool = <fun>",
          [("check_list 2 [[1; 2]; [4]; [5; 6]]", "- : bool = true"), ("check_list 3 [[1; 2; 3]; [4; 5; 6; 7]; [8; 9; 10]]", "- : bool = false"),
           ("check_list 1 [[]; [2]; [3]]", "- : bool = true"), ("check_list (-1) [[1]; [2]; []]", "Exception: Invalid_argument \"check_list: k < 0\".")],
          r"`len_ok n l` vérifie longueur$(l)\le n$ sans calculer la longueur : on s'arrête dès que $n$ éléments sont dépassés. `&&` arrête aussi `check` à la première liste trop longue.", src=A24, duree=15),
        w("ky2", r"Exercice 2.1 (tri insertion). Écrire `insert_x x order lst` qui insère `x` dans la liste `lst`, triée selon l'ordre induit par la fonction booléenne à deux paramètres `order`.",
          _INS, "val insert_x : 'a -> ('a -> 'a -> bool) -> 'a list -> 'a list = <fun>",
          [(f"insert_x 3 {_LT} []", "- : int list = [3]"), (f"insert_x 7 {_LT} [1; 3; 5; 9]", "- : int list = [1; 3; 5; 7; 9]"),
           (f"insert_x 5 {_GT} [10; 8; 6; 4; 2]", "- : int list = [10; 8; 6; 5; 4; 2]"), (f"insert_x 'c' {_LT} ['d'; 'e']", "- : char list = ['c'; 'd'; 'e']"),
           (f"insert_x 'c' {_GT} ['e']", "- : char list = ['e'; 'c']")],
          r"Arrêt dès que `order x e` est vrai : `x` se place devant `e`, le reste est déjà trié.", src=A24, duree=10),
        w("ky3", r"Exercice 2.2. Écrire `insertion_sort order lst` qui trie `lst` selon `order`, en utilisant `insert_x`.",
          _INS + " ;;\nlet rec insertion_sort order = function\n    [] -> []\n  | e :: l -> insert_x e order (insertion_sort order l)",
          "val insert_x : 'a -> ('a -> 'a -> bool) -> 'a list -> 'a list = <fun>\nval insertion_sort : ('a -> 'a -> bool) -> 'a list -> 'a list = <fun>",
          [(f"insertion_sort {_GT} []", "- : 'a list = []"), (f"insertion_sort {_LT} [5; 3; 8; 1; 4]", "- : int list = [1; 3; 4; 5; 8]"),
           (f"insertion_sort {_GT} [10; 20; 15; 5; 30]", "- : int list = [30; 20; 15; 10; 5]"), (f"insertion_sort {_LT} ['d'; 'a'; 'c'; 'b'; 'e']", "- : char list = ['a'; 'b'; 'c'; 'd'; 'e']"),
           (f"insertion_sort {_LT} [1.1; 3.3; 2.2; 5.5; 4.4]", "- : float list = [1.1; 2.2; 3.3; 4.4; 5.5]")],
          r"Récursion pure : on trie la fin, puis on y insère la tête.", src=A24, duree=8),
        ev("ky4", _MYS + " ;;\nmystery [1; 2; 8; 2; 1] ;;\nmystery [\"a\"; \"b\"; \"c\"; \"d\"; \"e\"; \"f\"] ;;",
           "val mystery : 'a list -> 'a list = <fun>\n- : int list = [1; 2; 8; 2; 1; 1; 2; 8; 2; 1]\n- : string list = [\"a\"; \"b\"; \"c\"; \"d\"; \"e\"; \"f\"; \"f\"; \"e\"; \"d\"; \"c\"; \"b\"; \"a\"]",
           r"Avec `switch = true`, chaque élément est recopié et empilé dans `acc` (à l'envers). À la fin de la liste, `switch` passe à `false` et les éléments de `acc` sont recopiés : la liste suivie de son miroir. (Le filtrage n'est pas exhaustif : Caml affiche un avertissement, le cas `(h :: t, false)` n'arrive jamais.)",
           enonce="Exercice 3 (4 points). Donner le type de `mystery`, puis la réponse de Caml aux deux évaluations :", src=A24, duree=10),
    ]},
]

VARIANTS = {
    "k11": [evv("2 * 3 + 4 * 5 ;;", "- : int = 26", r"$6+20$."), evv("(3 + 4) * 2 ;;", "- : int = 14", r"Parenthèses d'abord.")],
    "k12": [evv("17 / 5 ;;\n17 mod 5 ;;", "- : int = 3\n- : int = 2", r"$17=5\times3+2$.")],
    "k13": [evv("5. /. 2. ;;\n0.5 *. 4. ;;", "- : float = 2.5\n- : float = 2.", r"Opérateurs flottants.")],
    "k16": [evv("let x = 7 ;;\nlet x = 2 in x * x ;;\nx ;;", "val x : int = 7\n- : int = 4\n- : int = 7", r"Le `x` local masque le global dans `x * x` seulement.")],
    "k21": [evv("let triple x = 3 * x ;;\ntriple 4 ;;", "val triple : int -> int = <fun>\n- : int = 12", r"`3 * x` impose `int`.")],
    "k23": [evv("let succ x = x + 1 ;;\nsucc 2 * 3 ;;\nsucc (2 * 3) ;;", "val succ : int -> int = <fun>\n- : int = 9\n- : int = 7", r"`succ 2 * 3` $=(2+1)\times3$.")],
    "k32": [evv("let mult x y = x * y ;;\nlet double = mult 2 ;;\ndouble 21 ;;", "val mult : int -> int -> int = <fun>\nval double : int -> int = <fun>\n- : int = 42", r"Application partielle.")],
    "k35": [evv(_S + " ;;\nsomme 2 3 * 4 ;;", "val somme : int -> int -> int = <fun>\n- : int = 20", r"`(somme 2 3) * 4`.")],
    "k43": [evv("false && 1 / 0 = 0 ;;\ntrue && 2 > 1 ;;", "- : bool = false\n- : bool = true", r"`&&` s'arrête si le premier terme est faux.")],
    "k52": [evv("let racine x = if x < 0. then failwith \"racine: x < 0\" else sqrt x ;;\nracine 9. ;;\nracine (-1.) ;;",
                "val racine : float -> float = <fun>\n- : float = 3.\nException: Failure \"racine: x < 0\".", r"`sqrt` est la racine carrée des flottants.")],
    "k61": [evv("let nom = function\n    1 -> \"un\"\n  | 2 -> \"deux\"\n  | _ -> \"beaucoup\" ;;\nnom 1 ;;\nnom 0 ;;",
                "val nom : int -> string = <fun>\n- : string = \"un\"\n- : string = \"beaucoup\"", r"`0` n'est filtré que par `_`.")],
    "k64": [evv("let premier (a, b) = a ;;\npremier ('x', 3.) ;;", "val premier : 'a * 'b -> 'a = <fun>\n- : char = 'x'", r"`b` n'est pas utilisé : type quelconque `'b`.")],
    "k71": [evv(_F + " ;;\nfact 4 ;;", "val fact : int -> int = <fun>\n- : int = 24", r"$4\times3\times2\times1$.")],
    "k77": [{"enonce": r"Avec la même fonction `fact`, combien d'appels fait `fact 8` ?", "calc": "9", "ans": "9", "sol": r"De `fact 8` à `fact 0` : $9$ appels."}],
    "k82": [{"enonce": r"Combien d'appels de `fibo` (le premier compris) fait `fibo 4` avec la version à deux appels ?", "calc": "1 + (1 + (1 + 1 + 1) + 1) + (1 + 1 + 1)", "ans": "9",
             "sol": r"$A(4)=1+A(3)+A(2)=1+5+3=9$."}],
    "k83": [{"enonce": r"Hanoï : nombre minimal de déplacements pour $7$ disques ?", "calc": "2**7 - 1", "ans": "127", "sol": r"$2^7-1=127$."}],
    "k92": [{"enonce": r"Même version sans chapeau : combien de tests `n < 0` fait `fact 4` ?", "calc": "5", "ans": "5", "sol": r"Un par appel, de `fact 4` à `fact 0` : $5$."}],
    "ka1": [evv("'a' :: ['b'] ;;\n[[]] ;;", "- : char list = ['a'; 'b']\n- : 'a list list = [[]]", r"`[[]]` : une liste contenant une liste vide.")],
    "kb7": [evv("let rec f = function\n    [] -> []\n  | [x] -> [x]\n  | x :: y :: l -> y :: x :: f l ;;\nf ['a'; 'b'; 'c'; 'd'] ;;",
                "val f : 'a list -> 'a list = <fun>\n- : char list = ['b'; 'a'; 'd'; 'c']", r"Échange deux à deux.")],
    "kc1": [evv("let applique f x = f (f x) ;;\napplique (fun x -> x ^ \"!\") \"ok\" ;;", "val applique : ('a -> 'a) -> 'a -> 'a = <fun>\n- : string = \"ok!!\"", r"Deux applications.")],
}
for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["id"] in VARIANTS:
            _e["variants"] = VARIANTS[_e["id"]]

EXTRA_PARTS = []

QUIZ = [
    {"notion": "bases", "type": "qcm", "q": r"`7 / 2 ;;` répond :", "choix": [r"`- : int = 3`", r"`- : float = 3.5`", r"`- : int = 4`", r"une erreur de type"], "bonne": 0},
    {"notion": "bases", "type": "vf", "q": r"`1 + 2.5` est accepté par Caml et vaut `3.5`.", "bonne": False},
    {"notion": "fonctions", "type": "qcm", "q": r"Type de `let f x y = x + y` :", "choix": [r"`int -> int -> int`", r"`int * int -> int`", r"`(int -> int) -> int`", r"`'a -> 'a -> 'a`"], "bonne": 0},
    {"notion": "fonctions", "type": "vf", "q": r"`f 2 + 1` est évalué comme `f (2 + 1)`.", "bonne": False},
    {"notion": "alternative", "type": "qcm", "q": r"Dans `if c then e1 else e2` :", "choix": [r"`e1` et `e2` ont le même type", r"`e2` est facultatif quand `e1` est un entier", r"`c` peut être un entier", r"`e1` doit être un booléen"], "bonne": 0},
    {"notion": "alternative", "type": "vf", "q": r"`true || 1 / 0 = 0` déclenche `Division_by_zero`.", "bonne": False},
    {"notion": "exceptions", "type": "qcm", "q": r"Type de `failwith` :", "choix": [r"`string -> 'a`", r"`string -> unit`", r"`'a -> string`", r"`unit -> 'a`"], "bonne": 0},
    {"notion": "exceptions", "type": "vf", "q": r"`invalid_arg \"f\"` déclenche l'exception `Invalid_argument \"f\"`.", "bonne": True},
    {"notion": "filtrage", "type": "qcm", "q": r"`[1, 2, 3]` a le type :", "choix": [r"`(int * int * int) list`", r"`int list`", r"`int * int * int`", r"`int list list`"], "bonne": 0},
    {"notion": "filtrage", "type": "vf", "q": r"Les motifs d'un `match` sont essayés dans l'ordre d'écriture.", "bonne": True},
    {"notion": "recursivite", "type": "qcm", "q": r"`let f n = … f (n - 1) …` sans `rec` donne :", "choix": [r"`Error: Unbound value f`", r"une boucle infinie", r"`Exception: Stack_overflow`", r"une fonction correcte"], "bonne": 0},
    {"notion": "recursivite", "type": "vf", "q": r"Chaque appel récursif doit se rapprocher d'un cas d'arrêt.", "bonne": True},
    {"notion": "multiple", "type": "qcm", "q": r"Nombre minimal de déplacements pour Hanoï à $n$ disques :", "choix": [r"$2^n-1$", r"$2n-1$", r"$n^2$", r"$2^{n-1}$"], "bonne": 0},
    {"notion": "multiple", "type": "vf", "q": r"La version de `fibo` à deux appels récursifs fait un nombre d'appels linéaire en $n$.", "bonne": False},
    {"notion": "optimisation", "type": "qcm", "q": r"Une fonction chapeau sert à :", "choix": [r"tester les paramètres une seule fois avant la récursion", r"rendre une fonction polymorphe", r"éviter le mot-clé `rec`", r"afficher le résultat"], "bonne": 0},
    {"notion": "optimisation", "type": "vf", "q": r"`let p = puissance x (n / 2) in p * p` évite de refaire le même calcul.", "bonne": True},
    {"notion": "listes", "type": "qcm", "q": r"`1 :: [2; 3]` vaut :", "choix": [r"`[1; 2; 3]`", r"`[[1]; 2; 3]`", r"`[2; 3; 1]`", r"une erreur de type"], "bonne": 0},
    {"notion": "listes", "type": "vf", "q": r"`[1; 'a']` est une liste valide.", "bonne": False},
    {"notion": "listes2", "type": "qcm", "q": r"Pour tester qu'une liste est croissante, les motifs sont :", "choix": [r"`[]`, `[e]`, `e1 :: e2 :: l`", r"`[]`, `e :: l`", r"`e :: l` seulement", r"`([], [])`, `(e1 :: l1, e2 :: l2)`"], "bonne": 0},
    {"notion": "listes2", "type": "vf", "q": r"Le cours conseille d'essayer d'abord la récursion pure avant un accumulateur.", "bonne": True},
    {"notion": "ordre_sup", "type": "qcm", "q": r"Type de `map` :", "choix": [r"`('a -> 'b) -> 'a list -> 'b list`", r"`'a list -> 'b list`", r"`('a -> 'a) -> 'a list -> 'a`", r"`'a -> 'b -> 'a list`"], "bonne": 0},
    {"notion": "ordre_sup", "type": "vf", "q": r"Avec `order` en paramètre, la même fonction `insertion_sort` trie par ordre croissant ou décroissant.", "bonne": True},
]

_FL = {
    1: r"`+ - * / mod` (int) · `+. -. *. /.` (float) · `^` · `let x = e` · `let x = e1 in e2` · `- : type = valeur`",
    2: r"`let f x = e` $\equiv$ `let f = function x -> e` · `t1 -> t2` · application prioritaire · `'a` polymorphe · liaison statique",
    3: r"`let f x y = e` : `t1 -> t2 -> t3` · application partielle `f x` : `t2 -> t3`",
    4: r"`if c then e1 else e2` (même type) · `&&`, `||` paresseux · `not`",
    5: r"`failwith \"msg\"` : `Failure` · `invalid_arg \"msg\"` : `Invalid_argument` · `failwith : string -> 'a`",
    6: r"`match e with m -> e | _ -> e` · `function` · `when` · `(a, b)` : `t1 * t2` · `fun x -> e`",
    7: r"`let rec` · cas d'arrêt · appel sur un problème plus petit · `n mod 10`, `n / 10`",
    8: r"$F_n=F_{n-1}+F_{n-2}$ · $\binom np=\binom{n-1}{p-1}+\binom{n-1}{p}$ · Hanoï : $2^n-1$, intermédiaire $=6-s-d$",
    9: r"fonction chapeau · accumulateur · `let p = … in` · `&&`/`||` pour s'arrêter tôt",
    10: r"`[]` · `e :: l` · `@` · réponse pour `e :: l` à partir de celle pour `l` · accumulateur pour renverser",
    11: r"`[] | [_] | e1 :: e2 :: l` · deux listes : `([], l) | (l, []) | (e1 :: r1, e2 :: r2)` · `(a, b) :: l`",
    12: r"`map`, `for_all`, `filter`, `fold` · fonction en paramètre · `order : 'a -> 'a -> bool`",
    13: r"fonction chapeau · compteur · `remove_x` puis `remove_duplicates` · groupes construits en récursion pure",
    14: r"longueur $\le k$ sans `List.length` · `insert_x` avec `order` · tri insertion · `mystery` : liste puis son miroir",
}
FORMULES = {e["id"]: _FL[lvl["n"]] for lvl in LEVELS for e in lvl["exos"]}
