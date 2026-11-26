"""Teacher grading grids (« barème du prof ») for the « copie 20/20 » method mode.

One grid per method type, binary criteria summing to 20: after writing the copy on paper the student
ticks what the copy contains; every unticked criterion is a flagged mistake (event_log kind 'faute',
exo_id '<grid>:<index>') and is recalled on the next exercise of the same type.
Grids follow the APIS S1 official corrections (TD4 Suites 2031, finals 2020-2029): theorem named,
every sign justified, quantifiers written, conclusion sentence.
"""

# key -> (title, [(criterion, points, mistake flagged when unticked)])
GRILLES = {
    'definition': ("Définition avec quantificateurs", [
        ("Quantificateurs dans le bon ordre (par exemple $\\forall\\varepsilon > 0,\\ \\exists N\\in\\mathbb N,\\ \\forall n\\geqslant N$)", 6,
         "ordre des quantificateurs"),
        ("Chaque variable a son ensemble ($n\\in\\mathbb N$, $\\varepsilon > 0$, $\\ell\\in\\mathbb R$, $M\\in\\mathbb R$)", 4,
         "variable non quantifiée"),
        ("Inégalités strictes et larges exactes ($<$ ou $\\leqslant$ comme dans le cours)", 4, "strict et large confondus"),
        ("Exemple ou contre-exemple vérifié par un calcul, pas seulement donné", 4, "exemple non vérifié"),
        ("Cas particuliers séparés quand il y en a (par exemple $q=1$ et $q\\neq1$)", 2, "cas oublié"),
    ]),
    'ag': ("Suite arithmétique ou géométrique", [
        ("Nature justifiée : $u_{n+1}=u_n+r$ ou $u_{n+1}=q\\,u_n$ pour tout $n$", 4, "nature non justifiée"),
        ("Terme général écrit à partir du bon indice : $u_n=u_p+(n-p)r$ ou $u_n=u_pq^{n-p}$", 5, "décalage d'indice"),
        ("Somme : nombre de termes juste ($n-p+1$) et formule citée", 5, "nombre de termes faux"),
        ("Cas $q=1$ séparé de $q\\neq1$ (somme, limite, signe)", 2, "cas $q=1$ oublié"),
        ("Calcul mené jusqu'au bout et résultat encadré", 4, "résultat non encadré"),
    ]),
    'variation': ("Sens de variation", [
        ("Domaine écrit : « pour tout $n\\in\\mathbb N$ » (ou $n\\geqslant1$)", 2, "domaine oublié"),
        ("Méthode annoncée : différence $u_{n+1}-u_n$, quotient $\\frac{u_{n+1}}{u_n}$ ou $u_n=f(n)$", 2, "méthode non annoncée"),
        ("Méthode du quotient : $u_n > 0$ prouvé avant de comparer à $1$ (coche si tu as fait la différence)", 2,
         "quotient sans $u_n > 0$"),
        ("Calcul réduit jusqu'à une forme dont le signe se lit (même dénominateur, facteurs)", 5, "calcul non réduit"),
        ("Signe justifié facteur par facteur, pas seulement affirmé", 4, "signe affirmé sans preuve"),
        ("Tableau : signe de $u_{n+1}-u_n$ et flèches de $u_n$, avec le rang où le signe change", 3, "tableau de variations absent"),
        ("Conclusion : strictement ou au sens large, et à partir de quel rang", 2, "stricte et large confondues"),
    ]),
    'bornee': ("Suite bornée, encadrement", [
        ("But annoncé : trouver $m$ et $M$ réels avec $\\forall n,\\ m\\leqslant u_n\\leqslant M$", 3, "but non annoncé"),
        ("Chaque morceau encadré avec sa raison ($-1\\leqslant\\cos n\\leqslant1$, $n+1\\geqslant1$…)", 6, "encadrement non justifié"),
        ("Inégalités combinées légalement : on additionne, on ne soustrait pas, on multiplie par un positif", 5,
         "opération interdite sur des inégalités"),
        ("Bornes $m$ et $M$ explicites et indépendantes de $n$", 4, "borne qui dépend de $n$"),
        ("Conclusion « donc $(u_n)$ est bornée » (ou minorée, majorée)", 2, "conclusion absente"),
    ]),
    'limite': ("Calcul de limite", [
        ("Forme indéterminée nommée (« $\\frac\\infty\\infty$ », « $\\infty-\\infty$ », « $1^\\infty$ »)", 3, "forme indéterminée non nommée"),
        ("Bonne technique : terme dominant en facteur, quantité conjuguée, passage à $e^{n\\ln(\\cdot)}$", 6, "technique non montrée"),
        ("Limites usuelles et croissances comparées citées par leur nom", 5, "croissances comparées non citées"),
        ("Opérations sur les limites justifiées (somme, produit, quotient, composée)", 4, "opération non justifiée"),
        ("Résultat encadré : $\\lim u_n=\\dots$", 2, "résultat non encadré"),
    ]),
    'gendarmes': ("Gendarmes et comparaison", [
        ("Encadrement $a_n\\leqslant u_n\\leqslant b_n$ prouvé pour tout $n\\geqslant n_0$", 7, "encadrement non prouvé"),
        ("Limites de $a_n$ et $b_n$ calculées (égales), ou minorant qui tend vers $+\\infty$", 5, "limites des bornes non calculées"),
        ("Théorème nommé : gendarmes, ou minoration / majoration", 4, "théorème non nommé"),
        ("Le théorème donne l'existence de la limite : pas de « $\\lim u_n$ » écrit avant de l'avoir conclue", 2,
         "limite écrite avant d'exister"),
        ("Conclusion avec la valeur de la limite", 2, "conclusion absente"),
    ]),
    'arith_geo_rec': ("Suite arithmético-géométrique", [
        ("Point fixe : $\\ell=a\\ell+b$ résolu", 4, "point fixe non calculé"),
        ("$v_n=u_n-\\ell$ défini et $v_{n+1}=a\\,v_n$ calculé ligne à ligne", 6, "suite auxiliaire non prouvée géométrique"),
        ("$v_n=v_0a^n$ puis $u_n=\\ell+(u_0-\\ell)a^n$", 4, "retour à $u_n$ oublié"),
        ("Vérification sur $u_0$ ou $u_1$", 2, "formule non vérifiée"),
        ("Limite discutée selon $a$ ($|a| < 1$ : $u_n\\to\\ell$)", 4, "limite non discutée"),
    ]),
    'limite_monotone': ("Théorème de la limite monotone", [
        ("Monotonie prouvée (signe de $u_{n+1}-u_n$ justifié)", 6, "monotonie non prouvée"),
        ("Majorant (si croissante) ou minorant (si décroissante) prouvé, indépendant de $n$", 6, "majorant qui dépend de $n$"),
        ("Théorème de la limite monotone nommé", 4, "théorème non nommé"),
        ("Conclusion juste : $(u_n)$ converge et $\\ell\\leqslant M$, sans dire que la limite vaut le majorant", 4,
         "majorant pris pour la limite"),
    ]),
    'adjacentes': ("Suites adjacentes", [
        ("Définition rappelée : l'une croissante, l'autre décroissante, $v_n-u_n\\to0$", 3, "définition non rappelée"),
        ("Monotonie de $(u_n)$ prouvée", 5, "monotonie de $(u_n)$ non prouvée"),
        ("Monotonie de $(v_n)$ prouvée", 5, "monotonie de $(v_n)$ non prouvée"),
        ("$\\lim(v_n-u_n)=0$ calculée", 4, "limite de la différence oubliée"),
        ("Théorème nommé : même limite $\\ell$ et $u_n\\leqslant\\ell\\leqslant v_n$", 3, "conclusion du théorème absente"),
    ]),
    'recurrente': ("Suite récurrente $u_{n+1}=f(u_n)$", [
        ("Propriété $P(n)$ écrite en entier", 2, "$P(n)$ non écrite"),
        ("Initialisation vérifiée sur $u_0$", 2, "initialisation oubliée"),
        ("Hérédité : « soit $n\\in\\mathbb N$ tel que $P(n)$ », puis hypothèse utilisée et citée", 5,
         "« pour tout $n$ » supposé dans l'hérédité"),
        ("Passage de $u_n$ à $f(u_n)$ justifié (sens de variation de $f$ ou calcul)", 3, "passage à $f(u_n)$ non justifié"),
        ("Conclusion de la récurrence", 1, "récurrence non conclue"),
        ("Monotonie prouvée (signe de $u_{n+1}-u_n$)", 3, "monotonie non prouvée"),
        ("Limite : convergence établie d'abord, $f$ continue, $\\ell=f(\\ell)$, bon point fixe choisi grâce à l'encadrement", 4,
         "point fixe pris sans convergence"),
    ]),
    'extraites': ("Suites extraites", [
        ("Suites extraites choisies et exprimées ($u_{2n}$, $u_{2n+1}$…)", 6, "extraites mal exprimées"),
        ("Limite de chaque extraite calculée", 6, "limite d'une extraite oubliée"),
        ("Théorème cité : deux limites différentes, donc divergence ; même limite pour $u_{2n}$ et $u_{2n+1}$, donc convergence", 6,
         "théorème non cité"),
        ("Conclusion", 2, "conclusion absente"),
    ]),
    'landau': ("Comparaison : $o$, $O$, $\\sim$", [
        ("Critère annoncé : quotient $\\frac{u_n}{v_n}$, $v_n\\neq0$ à partir d'un rang", 3, "$v_n\\neq0$ non vérifié"),
        ("Termes dominants mis en facteur", 5, "terme dominant non factorisé"),
        ("Limite du quotient calculée", 5, "limite du quotient non calculée"),
        ("Toutes les relations conclues ($o$, $O$, $\\sim$, et $\\sim\\Rightarrow O$)", 5, "relation oubliée"),
        ("Aucune somme ni composée d'équivalents", 2, "somme d'équivalents"),
    ]),
    'demo': ("Démonstration du cours", [
        ("Hypothèses et but écrits avant de commencer", 3, "but non écrit"),
        ("Définition avec quantificateurs écrite puis utilisée", 5, "définition non utilisée"),
        ("Choix de $\\varepsilon$ ou de $N$ explicite et justifié", 5, "choix de $\\varepsilon$ ou $N$ non justifié"),
        ("Chaque implication justifiée", 5, "implication non justifiée"),
        ("Conclusion qui reprend l'énoncé", 2, "conclusion absente"),
    ]),
    # APIS intégrales
    'derivee': ("Dériver une composée", [
        ("Forme reconnue et nommée : $(u^n)'$, $(e^u)'$, $(\\ln u)'$, $(\\sqrt u)'$, $(g\\circ u)'$", 5, "forme non nommée"),
        ("$u$ et $u'$ écrits à part avant de calculer", 4, "$u'$ non écrit"),
        ("Domaine de dérivabilité précisé ($u > 0$ pour $\\ln u$ et $\\sqrt u$)", 3, "domaine oublié"),
        ("Résultat simplifié ou factorisé", 5, "résultat non simplifié"),
        ("Résultat encadré : $f'(x)=\\dots$", 3, "résultat non encadré"),
    ]),
    'primitive': ("Primitive", [
        ("Forme reconnue et écrite : $u'u^n$, $\\frac{u'}u$, $u'e^u$, $f(ax+b)$…", 6, "forme non reconnue"),
        ("Coefficient ajusté pour faire apparaître $u'$ exactement", 4, "coefficient oublié"),
        ("Intervalle précisé (là où $u$ ne s'annule pas, $u > 0$ pour $\\ln u$)", 3, "intervalle oublié"),
        ("Vérification en dérivant le résultat", 3, "primitive non vérifiée"),
        ("« $+C$ » ou bornes appliquées : $[F]_a^b=F(b)-F(a)$", 4, "constante ou bornes oubliées"),
    ]),
    'ipp': ("Intégration par parties", [
        ("$u$, $u'$, $v'$, $v$ écrits explicitement", 5, "$u$, $v$ non posés"),
        ("$u$ et $v$ de classe $C^1$ sur $[a,b]$ cité", 3, "hypothèse $C^1$ oubliée"),
        ("Formule écrite : $\\int_a^buv'=[uv]_a^b-\\int_a^bu'v$", 4, "formule non écrite"),
        ("Crochet $[uv]_a^b$ évalué séparément", 4, "crochet mal évalué"),
        ("Intégrale restante calculée et résultat encadré", 4, "calcul final faux"),
    ]),
    'changement': ("Changement de variable", [
        ("Changement posé : $t=\\varphi(x)$ ou $x=\\varphi(t)$, $\\varphi$ de classe $C^1$", 4, "changement non posé"),
        ("$dx$ exprimé en $dt$", 4, "$dx$ oublié"),
        ("Bornes transformées", 4, "bornes non changées"),
        ("Intégrale réécrite entièrement en $t$ (plus aucun $x$)", 4, "mélange de $x$ et $t$"),
        ("Calcul final et résultat encadré", 4, "résultat non encadré"),
    ]),
    # DP
    'denombrement': ("Dénombrement", [
        ("Ensemble des issues décrit (listes, parties, ordre ou non, répétition ou non)", 5, "modèle non décrit"),
        ("Bon outil justifié : $n^p$, $A_n^p$, $n!$, $\\binom np$", 5, "outil non justifié"),
        ("Principe multiplicatif ou additif cité aux étapes", 4, "principe non cité"),
        ("« Au moins un » traité par le complémentaire, sans double comptage", 3, "double comptage"),
        ("Résultat numérique encadré", 3, "résultat non encadré"),
    ]),
    'probas': ("Probabilités", [
        ("Événements nommés avec des lettres et définis en français", 4, "événements non nommés"),
        ("Hypothèse annoncée : équiprobabilité, indépendance, système complet", 4, "hypothèse non annoncée"),
        ("Formule nommée : probabilités totales, Bayes, $P(A\\cap B)=P(A)P_A(B)$", 5, "formule non nommée"),
        ("Arbre ou système complet écrit avec ses probabilités", 3, "arbre absent"),
        ("Résultat dans $[0,1]$, simplifié et encadré", 4, "résultat non vérifié dans $[0,1]$"),
    ]),
    'va': ("Variable aléatoire", [
        ("$X(\\Omega)$ donné", 3, "$X(\\Omega)$ oublié"),
        ("Loi en tableau, somme des probabilités égale à $1$ vérifiée", 5, "somme des probabilités non vérifiée"),
        ("Loi usuelle reconnue avec ses paramètres : $X\\sim\\mathcal B(n,p)$, épreuves indépendantes citées", 4,
         "loi non justifiée"),
        ("Formule écrite avant le calcul : $E(X)=\\sum x_iP(X=x_i)$, König-Huygens, linéarité", 4, "formule non écrite"),
        ("Résultat encadré", 4, "résultat non encadré"),
    ]),
    # OBM
    'table': ("Table de vérité", [
        ("$2^n$ lignes pour $n$ propositions", 5, "lignes manquantes"),
        ("Une colonne par sous-expression, de l'intérieur vers l'extérieur", 5, "colonnes intermédiaires absentes"),
        ("Implication fausse seulement pour V puis F", 4, "implication mal évaluée"),
        ("Colonnes finales comparées ligne à ligne", 3, "comparaison absente"),
        ("Phrase de conclusion : équivalentes ou non", 3, "conclusion absente"),
    ]),
    'raisonnement': ("Raisonnement : contraposée, absurde, cas", [
        ("Type de raisonnement annoncé en première ligne", 5, "raisonnement non annoncé"),
        ("Hypothèse de départ écrite (« supposons $\\neg Q$ »)", 4, "hypothèse non écrite"),
        ("Contraposée et non réciproque ; cas qui couvrent tout", 4, "réciproque prise pour contraposée"),
        ("Chaque étape justifiée", 4, "étape non justifiée"),
        ("Conclusion qui revient à l'énoncé", 3, "conclusion absente"),
    ]),
    'recurrence': ("Récurrence", [
        ("$P(n)$ écrite en entier", 3, "$P(n)$ non écrite"),
        ("Initialisation calculée au bon rang", 4, "initialisation oubliée"),
        ("« Soit $n$ tel que $P(n)$ », pas « pour tout $n$ »", 5, "« pour tout $n$ » supposé dans l'hérédité"),
        ("Hypothèse de récurrence utilisée et citée", 5, "hypothèse de récurrence non citée"),
        ("Conclusion « par récurrence… »", 3, "récurrence non conclue"),
    ]),
    'ensembles': ("Ensembles", [
        ("« Soit $x\\in A$ » puis « donc $x\\in B$ » pour chaque inclusion", 6, "inclusion par l'exemple"),
        ("Les deux inclusions pour une égalité", 5, "une seule inclusion"),
        ("$\\in$ et $\\subset$ jamais confondus", 4, "$\\in$ et $\\subset$ confondus"),
        ("Ensembles listés avec accolades complètes", 2, "accolades oubliées"),
        ("Conclusion", 3, "conclusion absente"),
    ]),
    'applications': ("Image directe, image réciproque", [
        ("Définition traduite : $y\\in f(A)\\iff\\exists x\\in A,\\ y=f(x)$ ou $x\\in f^{-1}(B)\\iff f(x)\\in B$", 6,
         "définition non traduite"),
        ("Calcul justifié (variations, résolution de $f(x)\\in B$)", 5, "calcul non justifié"),
        ("Ensemble et intervalle distingués : $\\{2,3\\}$ n'est pas $[2,3]$", 3, "accolades et crochets confondus"),
        ("$f^{-1}(B)$ calculée sans supposer $f$ bijective", 3, "$f$ supposée bijective"),
        ("Résultat encadré", 3, "résultat non encadré"),
    ]),
    'injsurj': ("Injection, surjection, bijection", [
        ("Injective : « soient $x,x'$ tels que $f(x)=f(x')$ » jusqu'à $x=x'$, ou contre-exemple chiffré", 6,
         "injectivité mal prouvée"),
        ("Surjective : « soit $y\\in F$ » et un antécédent explicite dans $E$, ou un $y$ sans antécédent", 6,
         "surjectivité mal prouvée"),
        ("Ensembles de départ et d'arrivée pris en compte", 3, "départ ou arrivée ignorés"),
        ("Bijection : antécédent unique et réciproque $f^{-1}$ donnée", 3, "réciproque oubliée"),
        ("Conclusion pour chaque propriété demandée", 2, "conclusion absente"),
    ]),
    'relations': ("Relations binaires", [
        ("Une propriété par paragraphe, titrée", 3, "propriétés mélangées"),
        ("Chaque propriété prouvée pour des éléments quelconques", 6, "preuve sur un exemple"),
        ("Antisymétrie et non-symétrie distinguées", 4, "antisymétrie mal comprise"),
        ("Conclusion : ordre ou équivalence, total ou non", 4, "nature non conclue"),
        ("Classes d'équivalence décrites quand demandé", 3, "classes oubliées"),
    ]),
}

# (subject, level) -> grid; exercise ids override (definitions inside method levels, exam exercises)
NIVEAUX = {
    ('maths-s1-apis-suites', 1): 'ag', ('maths-s1-apis-suites', 2): 'variation', ('maths-s1-apis-suites', 3): 'bornee',
    ('maths-s1-apis-suites', 4): 'limite', ('maths-s1-apis-suites', 5): 'limite', ('maths-s1-apis-suites', 6): 'gendarmes',
    ('maths-s1-apis-suites', 7): 'arith_geo_rec', ('maths-s1-apis-suites', 8): 'limite_monotone', ('maths-s1-apis-suites', 9): 'adjacentes',
    ('maths-s1-apis-suites', 10): 'recurrente', ('maths-s1-apis-suites', 11): 'extraites', ('maths-s1-apis-suites', 12): 'landau',
    ('maths-s1-apis-suites', 13): 'demo',
    ('maths-s1-apis-integrales', 1): 'derivee',
    **{('maths-s1-apis-integrales', k): 'primitive' for k in (2, 3, 4, 5)},
    **{('maths-s1-apis-integrales', k): 'ipp' for k in (6, 7, 8, 9)},
    **{('maths-s1-apis-integrales', k): 'changement' for k in (10, 11, 12)},
    **{('maths-s1-dp', k): 'denombrement' for k in range(1, 7)},
    **{('maths-s1-dp', k): 'probas' for k in range(7, 12)},
    **{('maths-s1-dp', k): 'va' for k in (12, 13, 14)},
    **{('maths-s1-obm', k): 'table' for k in (1,)},
    **{('maths-s1-obm', k): 'definition' for k in (2, 3, 4, 5)},
    ('maths-s1-obm', 6): 'raisonnement', ('maths-s1-obm', 7): 'recurrence', ('maths-s1-obm', 8): 'ensembles',
    ('maths-s1-obm', 9): 'applications', ('maths-s1-obm', 10): 'injsurj', ('maths-s1-obm', 11): 'relations',
}
EXOS = {
    'maths-s1-apis-suites': {
        **dict.fromkeys(('td1', 'td3', 'td4', 'td5', 'td6', 'td7', 'td8', 'td9', 'la1', 'lm4'), 'definition'),
        'bo3': 'demo', 'td13': 'arith_geo_rec', 'td14': 'recurrente',
        'sx1': 'adjacentes', 'sx2': 'limite_monotone', 'sx3': 'landau', 'sx4': 'recurrente', 'sx5': 'recurrente',
        'sx6': 'adjacentes', 'sh1': 'limite_monotone', 'sh2': 'recurrente', 'sh3': 'landau', 'sh4': 'adjacentes',
        'sh5': 'limite',
    },
}


def cle(subject, n, exo_id):
    """Grid key of an exercise, or None."""
    return EXOS.get(subject, {}).get(exo_id) or NIVEAUX.get((subject, n))


def pour(subject, n, exo_id):
    """{cle, titre, criteres: [(text, points, faute)]} for the exercise, or None."""
    k = cle(subject, n, exo_id)
    return k and {'cle': k, 'titre': GRILLES[k][0], 'criteres': GRILLES[k][1]}


def faute_texte(code):
    """'variation:5' -> mistake label, or None if unknown."""
    k, _, i = code.partition(':')
    try:
        return GRILLES[k][1][int(i)][2]
    except (KeyError, ValueError, IndexError):
        return None


def fautes_valides(k, indices):
    """Indices of unticked criteria sent by the browser, kept only if they exist in grid k."""
    n = len(GRILLES.get(k, ('', []))[1])
    return sorted({i for i in indices if isinstance(i, int) and 0 <= i < n})


assert all(sum(c[1] for c in g[1]) == 20 for g in GRILLES.values()), 'every grid is out of 20'
assert set(NIVEAUX.values()) | {v for e in EXOS.values() for v in e.values()} <= set(GRILLES)
