"""Copie 20/20, stages 2 to 4 of PLAN_BETA step 4: one hand-written skeleton per exercise type.

Each skeleton is the order of the official correction it cites (`source` = key of
parcours/baremes.json, checked by tests/test_squelettes.py): no step without an official copy behind it.
Learning order (worked examples then fading, Renkl et al. 2002; Sweller 1985):
complete official copy, then the skeleton with holes, then the skeleton alone, then nothing
(the skeleton becomes the checklist read after the correction). `{}` is a hole.
"""

# (step label, step with holes)
SQUELETTES = {
    'suite_nature': {
        'titre': 'Suite arithmétique ou géométrique',
        'source': ['maths-s1-apis-suites/7', 'maths-s1-apis-suites/10'],
        'etapes': [
            ('Calcul pour tout n', '$\\forall n \\in \\mathbb{N}$, $u_{n+1} - u_n =$ {} (ou $u_{n+1} = q\\,u_n$ avec $q =$ {}).'),
            ('Nature et raison', 'Donc $(u_n)$ est {} de raison {}.'),
            ('Terme général', '$u_n = u_0 + nr =$ {} (ou $u_n = u_0 q^n =$ {}).'),
        ],
    },
    'monotonie': {
        'titre': 'Sens de variation',
        'source': ['maths-s1-apis-suites/2'],
        'etapes': [
            ('Différence pour tout n', '$\\forall n \\in \\mathbb{N}$, $u_{n+1} - u_n =$ {} (même dénominateur).'),
            ('Forme factorisée', '$u_{n+1} - u_n =$ {}.'),
            ('Signe justifié', 'Le numérateur est {} et le dénominateur {}, donc $u_{n+1} - u_n$ {} $0$.'),
            ('Conclusion', 'Donc $(u_n)$ est {}.'),
        ],
    },
    'bornee': {
        'titre': 'Suite bornée, définition avec quantificateurs',
        'source': ['maths-s1-apis-suites/3'],
        'etapes': [
            ('Définition', '$\\exists m, M \\in \\mathbb{R}, \\forall n \\in \\mathbb{N},\\ m \\leqslant u_n \\leqslant M$.'),
            ('Encadrement', 'Pour tout $n$ : {} $\\leqslant u_n \\leqslant$ {}, car {}.'),
            ('Conclusion', 'Donc $(u_n)$ est bornée (ou : négation, $\\forall m, M, \\exists n$, {}).'),
        ],
    },
    'limite': {
        'titre': 'Limite, forme indéterminée',
        'source': ['maths-s1-apis-suites/5'],
        'etapes': [
            ('Factoriser par le terme dominant', 'Expression $=$ {} $\\times$ {}.'),
            ('Limite de chaque facteur', '{} $\\to$ {} et {} $\\to$ {} (croissances comparées si besoin, à nommer).'),
            ('Conclusion', 'Par produit (ou quotient), la limite est {}.'),
        ],
    },
    'comparaison': {
        'titre': 'Comparaison, gendarmes',
        'source': ['maths-s1-apis-suites/6', 'maths-s1-apis-suites/8'],
        'etapes': [
            ('Inégalité de départ', '{} $\\leqslant$ {} (fait connu, par exemple $-1 \\leqslant (-1)^n \\leqslant 1$).'),
            ('Encadrement de la suite', 'Donc {} $\\leqslant u_n \\leqslant$ {}.'),
            ('Limites des bornes', '{} $\\to$ {}.'),
            ('Théorème nommé', 'Par comparaison (ou par le théorème des gendarmes), $u_n \\to$ {}.'),
        ],
    },
    'arith_geo': {
        'titre': 'Suite arithmético-géométrique',
        'source': ['maths-s1-apis-suites/7'],
        'etapes': [
            ('Point fixe', '$\\ell = a\\ell + b \\iff \\ell =$ {}.'),
            ('Suite auxiliaire géométrique', '$\\forall n$, $v_{n+1} = u_{n+1} - \\ell =$ {} $= a\\,v_n$ : $(v_n)$ géométrique de raison {}.'),
            ('Premier terme', '$v_0 = u_0 - \\ell =$ {}.'),
            ('Terme général', '$v_n =$ {}, donc $u_n = v_n + \\ell =$ {}.'),
        ],
    },
    'limite_monotone': {
        'titre': 'Théorème de la limite monotone',
        'source': ['maths-s1-apis-suites/8'],
        'etapes': [
            ('Sens de variation', '$\\forall n$, $\\dfrac{u_{n+1}}{u_n} =$ {} $\\leqslant 1$ et $u_n > 0$ (ou $u_{n+1} - u_n =$ {}), donc $(u_n)$ est {}.'),
            ('Borne', '$(u_n)$ est {} par {}.'),
            ('Théorème nommé', 'Décroissante et minorée (ou croissante et majorée), donc convergente.'),
        ],
    },
    'adjacentes': {
        'titre': 'Suites adjacentes',
        'source': ['maths-s1-apis-suites/9'],
        'etapes': [
            ('Définition', '$(u_n)$ croissante, $(v_n)$ décroissante et $\\lim (v_n - u_n) = 0$.'),
            ('Première suite', '$u_{n+1} - u_n =$ {} $\\geqslant 0$ : $(u_n)$ croissante.'),
            ('Deuxième suite', '$v_{n+1} - v_n =$ {} $\\leqslant 0$ car {} : $(v_n)$ décroissante.'),
            ('Différence', '$v_n - u_n =$ {} $\\to 0$.'),
            ('Conclusion', 'Les suites sont adjacentes, donc elles convergent vers une même limite.'),
        ],
    },
    'recurrente': {
        'titre': 'Suite récurrente $u_{n+1} = f(u_n)$',
        'source': ['maths-s1-apis-suites/10'],
        'etapes': [
            ('Récurrence', 'Initialisation : $u_0 =$ {}. Hérédité : si {}, alors $u_{n+1} =$ {}, donc {}.'),
            ('Limites possibles', '$f$ est continue sur {}, donc $\\ell = f(\\ell) \\iff$ {}.'),
            ('Sens de variation', '$u_{n+1} - u_n =$ {}, donc $(u_n)$ est {}.'),
            ('Conclusion', '{} et {}, donc $(u_n)$ converge vers $\\ell \\in$ {} ; comme {}, $\\ell =$ {}.'),
        ],
    },
    'extraites': {
        'titre': 'Suites extraites',
        'source': ['maths-s1-apis-suites/11'],
        'etapes': [
            ('Termes pairs et impairs', '$u_{2n} =$ {} et $u_{2n+1} =$ {}.'),
            ('Limites', '$u_{2n} \\to$ {} et $u_{2n+1} \\to$ {}.'),
            ('Conclusion', 'Même limite, donc $(u_n)$ converge vers {} (limites différentes : $(u_n)$ diverge).'),
        ],
    },
    'comparaison_o': {
        'titre': 'Comparaison : o, O, équivalents',
        'source': ['maths-s1-apis-suites/12'],
        'etapes': [
            ('Quotient', '$\\dfrac{u_n}{v_n} =$ {} (factorisé par les termes dominants).'),
            ('Limite du quotient', '$\\dfrac{u_n}{v_n} \\to$ {} (croissances comparées si besoin, à nommer).'),
            ('Conclusion', 'Limite 1 : $u_n \\sim v_n$ ; limite 0 : $u_n = o(v_n)$ ; dans les deux cas, $u_n = O(v_n)$. Ici : {}.'),
        ],
    },
    'derivee': {
        'titre': 'Dériver une composée',
        'source': ['maths-s1-apis-integrales/1'],
        'etapes': [
            ('Forme reconnue', '$f$ est de la forme {} (produit, $u^n$, $\\sqrt u$, $e^u$…).'),
            ('Formule appliquée', '$f\'(x) =$ {}.'),
            ('Forme simplifiée', '$f\'(x) =$ {} (facteur commun sorti).'),
        ],
    },
    'primitive': {
        'titre': 'Primitive',
        'source': ['maths-s1-apis-integrales/5', 'maths-s1-apis-integrales/2'],
        'etapes': [
            ('Intervalle', 'Sur $I =$ {}, $f$ est continue, donc elle admet une primitive.'),
            ('Forme reconnue', '$f(x) =$ {} $\\times u\'(x)\\,$ {} avec $u(x) =$ {}.'),
            ('Primitive', '$F(x) =$ {}.'),
            ('Condition donnée', 'Si une valeur est imposée : $F(x_0) =$ {} donne la constante $C =$ {}.'),
        ],
    },
    'ipp': {
        'titre': 'Intégration par parties',
        'source': ['maths-s1-apis-integrales/8', 'maths-s1-apis-integrales/7'],
        'etapes': [
            ('Formule', '$\\displaystyle\\int_a^b u v\' = [uv]_a^b - \\int_a^b u\'v$.'),
            ('u, u\', v, v\' posés', '$u(x) =$ {}, $u\'(x) =$ {}, $v\'(x) =$ {}, $v(x) =$ {}.'),
            ('Report', '$I = \\big[$ {} $\\big]_a^b - \\displaystyle\\int_a^b$ {}.'),
            ('Calcul', 'Crochet $=$ {}, intégrale restante $=$ {}.'),
            ('Résultat', '$I =$ {}.'),
        ],
    },
    'changement_variable': {
        'titre': 'Changement de variable',
        'source': ['maths-s1-apis-integrales/13'],
        'etapes': [
            ('Changement posé', '$x =$ {} $\\iff t =$ {}, $dx =$ {}.'),
            ('Bornes', '$t =$ {} $\\to x =$ {} ; $t =$ {} $\\to x =$ {}.'),
            ('Nouvelle intégrale', '$I = \\displaystyle\\int$ {} $=$ {}.'),
            ('Résultat', '$I =$ {}.'),
        ],
    },
    'edo1_homogene': {
        'titre': 'Équation homogène du premier ordre',
        'source': ['maths-s1-apis-edo/4'],
        'etapes': [
            ('Équation homogène', '$(E_0)$ : {} $= 0$ sur $I =$ {}.'),
            ('Primitive', '$\\dfrac ba =$ {}, de primitive {}.'),
            ('Solutions', '$S_0 = \\{ x \\mapsto k e^{-A(x)},\\ k \\in \\mathbb{R} \\}$ avec $A(x) =$ {}, soit $y_0(x) =$ {}.'),
        ],
    },
    'edo1_complete': {
        'titre': 'Équation complète du premier ordre',
        'source': ['maths-s1-apis-edo/5', 'maths-s1-apis-edo/4'],
        'etapes': [
            ('Équation homogène', '$y_0(x) = k e^{-A(x)} =$ {}, $k \\in \\mathbb{R}$.'),
            ('Solution particulière', 'Évidente : $y_p =$ {} (vérifiée en reportant). Sinon, variation de la constante : $y_p(x) = k(x)y_0(x)$, en reportant $k\'(x) =$ {}, $k(x) =$ {}.'),
            ('Solutions', '$S = \\{ x \\mapsto$ {} $,\\ k \\in \\mathbb{R} \\}$.'),
        ],
    },
    'edo1_ci': {
        'titre': 'Condition initiale, premier ordre',
        'source': ['maths-s1-apis-edo/11'],
        'etapes': [
            ('Solution générale', '$y(x) =$ {}, $k \\in \\mathbb{R}$.'),
            ('Condition', '$y(x_0) =$ {} $\\iff k =$ {}.'),
            ('Conclusion', 'Unique solution : $y(x) =$ {}.'),
        ],
    },
    'edo2': {
        'titre': 'Équation du second ordre à coefficients constants',
        'source': ['maths-s1-apis-edo/11'],
        'etapes': [
            ('Équation caractéristique', '{} $= 0$, $\\Delta =$ {}.'),
            ('Racines', '$r =$ {} (deux réelles, double ou complexes $\\alpha \\pm i\\beta$).'),
            ('Solutions homogènes', '$y_0(x) =$ {}, $(k_1, k_2) \\in \\mathbb{R}^2$.'),
            ('Solution particulière', '$y_p(x) =$ {} (cherchée de la forme du second membre, vérifiée).'),
            ('Solutions', '$S = \\{ x \\mapsto$ {} $,\\ (k_1, k_2) \\in \\mathbb{R}^2 \\}$.'),
        ],
    },
    'denombrement': {
        'titre': 'Dénombrement',
        'source': ['maths-s1-dp/2', 'maths-s1-dp/5', 'maths-s1-dp/3'],
        'etapes': [
            ('Modèle', 'On compte des {} : ordre {}, répétition {}.'),
            ('Formule nommée', '{} ($n^p$ pour les $p$-listes, $A_n^p$ pour les arrangements, $n!$ pour les permutations, $\\binom np$ sans ordre).'),
            ('Contrainte', 'Choix successifs ({} $\\times$ {}) ou complémentaire : total $-$ {}.'),
            ('Résultat', '{} possibilités.'),
        ],
    },
    'cardinaux': {
        'titre': 'Cardinaux',
        'source': ['maths-s1-dp/1'],
        'etapes': [
            ('Union disjointe écrite', '{} $=$ {} $\\cup$ {}, union disjointe.'),
            ('Cardinal', '$\\mathrm{Card}$ {} $= \\mathrm{Card}$ {} $+ \\mathrm{Card}$ {}.'),
            ('Résultat', '{} (question précédente citée si elle sert).'),
        ],
    },
    'double_comptage': {
        'titre': 'Double comptage',
        'source': ['maths-s1-dp/6'],
        'etapes': [
            ('Premier compte', 'Directement : {} tirages.'),
            ('Second compte par cas disjoints', 'Selon {} $= 0, 1, \\dots$ : $\\sum$ {} tirages.'),
            ('Égalité', 'Les deux comptes portent sur le même ensemble, donc {} $=$ {}.'),
        ],
    },
    'equiprobabilite': {
        'titre': 'Équiprobabilité',
        'source': ['maths-s1-dp/7'],
        'etapes': [
            ('Univers', '$\\Omega$ : {}, tirages équiprobables, $\\mathrm{Card}(\\Omega) =$ {}.'),
            ('Événement', '$\\mathrm{Card}(A) =$ {} (cas disjoints additionnés).'),
            ('Probabilité', '$P(A) = \\dfrac{\\mathrm{Card}(A)}{\\mathrm{Card}(\\Omega)} =$ {} (ou $1 - P(\\bar A)$).'),
        ],
    },
    'proba_totales': {
        'titre': 'Probabilités totales, Bayes',
        'source': ['maths-s1-dp/10'],
        'etapes': [
            ('Événements et données', '$P(S) =$ {}, $P(V \\mid S) =$ {}, $P(V \\mid \\bar S) =$ {}.'),
            ('Partition', '$\\{S, \\bar S\\}$ partition de $\\Omega$ : $V = (V \\cap S) \\cup (V \\cap \\bar S)$, union disjointe.'),
            ('Probabilités totales', '$P(V) = P(V \\mid S)P(S) + P(V \\mid \\bar S)P(\\bar S) =$ {}.'),
            ('Bayes', '$P(S \\mid V) = \\dfrac{P(V \\mid S)P(S)}{P(V)} =$ {}.'),
        ],
    },
    'independance': {
        'titre': 'Indépendance',
        'source': ['maths-s1-dp/11'],
        'etapes': [
            ('Événements nommés', '$A$ : « {} », $B$ : « {} ».'),
            ('Probabilités', '$P(A) =$ {}, $P(B) =$ {}, $P(A \\cap B) =$ {}.'),
            ('Comparaison', '$P(A \\cap B)$ {} $P(A)P(B)$ (ou $P_B(A)$ {} $P(A)$).'),
            ('Conclusion', '$A$ et $B$ {} indépendants. Incompatibles seulement si $A \\cap B = \\emptyset$ : {}.'),
        ],
    },
    'loi_va': {
        'titre': 'Loi, espérance, variance',
        'source': ['maths-s1-dp/14', 'maths-s1-dp/13'],
        'etapes': [
            ('Valeurs', '$X(\\Omega) =$ {}.'),
            ('Loi', '$P(X = k) =$ {} pour chaque $k$ (somme $= 1$).'),
            ('Espérance', '$E(X) = \\sum k\\,P(X = k) =$ {}.'),
            ('Variance', '$E(X^2) =$ {}, $V(X) = E(X^2) - E(X)^2 =$ {} (König-Huygens).'),
        ],
    },
    'binomiale': {
        'titre': 'Loi binomiale',
        'source': ['maths-s1-dp/14'],
        'etapes': [
            ('Épreuve de Bernoulli', '$X_k(\\Omega) = \\{0, 1\\}$, $P(X_k = 1) =$ {} : Bernoulli de paramètre {}.'),
            ('Somme', '$Y = X_1 + \\dots + X_n$, les $X_k$ sont indépendantes et de même paramètre.'),
            ('Loi', '$Y \\sim \\mathcal{B}($ {} $,$ {} $)$, $P(Y = i) = \\binom ni p^i(1 - p)^{n-i} =$ {}.'),
            ('Espérance et variance', '$E(Y) = np =$ {} ; par indépendance, $V(Y) = np(1 - p) =$ {}.'),
        ],
    },
    'negation': {
        'titre': 'Nier une phrase',
        'source': ['maths-s1-obm/5', 'maths-s1-obm/3'],
        'etapes': [
            ('Phrase avec quantificateurs', '$P$ : {}.'),
            ('Règles', '$\\forall$ devient $\\exists$, $\\exists$ devient $\\forall$, « ou » devient « et », $A \\Rightarrow B$ devient $A \\wedge \\neg B$, les ensembles restent.'),
            ('Négation', '$\\neg P$ : {}.'),
        ],
    },
    'quantificateurs': {
        'titre': 'Écrire avec des quantificateurs',
        'source': ['maths-s1-obm/4'],
        'etapes': [
            ('Variables et ensembles', '{} $\\in$ {}, {} $\\in$ {}.'),
            ('Ordre des quantificateurs', '$\\forall$ {}, $\\exists$ {} (l\'élément choisi après dépend de ceux d\'avant).'),
            ('Phrase', '{}.'),
        ],
    },
    'contraposee': {
        'titre': 'Contraposée, vrai ou faux',
        'source': ['maths-s1-obm/6'],
        'etapes': [
            ('Vrai ou faux justifié', 'Calcul : {} ; contre-exemple si faux : $x =$ {}.'),
            ('Négation', '$\\neg P$ : « $\\exists$ {} $, A \\wedge \\neg B$ ».'),
            ('Contraposée', '« $\\forall$ {} $, \\neg B \\implies \\neg A$ » : {}.'),
        ],
    },
    'recurrence': {
        'titre': 'Récurrence',
        'source': ['maths-s1-obm/7'],
        'etapes': [
            ('Propriété', '$\\mathcal{P}(n)$ : « {} ».'),
            ('Initialisation', '$n =$ {} : {} $=$ {}, donc $\\mathcal{P}($ {} $)$ vraie.'),
            ('Hérédité', 'Supposons $\\mathcal{P}(n)$. Alors {} $=$ {} (hypothèse utilisée), donc $\\mathcal{P}(n+1)$.'),
            ('Conclusion', 'Par récurrence, $\\forall n \\geqslant$ {}, $\\mathcal{P}(n)$.'),
        ],
    },
    'image': {
        'titre': 'Image directe, image réciproque',
        'source': ['maths-s1-obm/9'],
        'etapes': [
            ('Définitions', '$f(A) = \\{f(x) ; x \\in A\\}$, $f^{-1}(B) = \\{x \\in E ; f(x) \\in B\\}$.'),
            ('Calcul', '$f(A) =$ {}, $f^{-1}(B) =$ {}.'),
        ],
    },
    'injection': {
        'titre': 'Injection, surjection',
        'source': ['maths-s1-obm/10', 'maths-s1-obm/9'],
        'etapes': [
            ('Définition', 'Injective : $\\forall x, x\', f(x) = f(x\') \\implies x = x\'$. Surjective : $\\forall y \\in F, \\exists x \\in E, f(x) = y$.'),
            ('Preuve ou contre-exemple', '{} : $f$ {} $=$ $f$ {} avec {} $\\neq$ {} (non injective), ou {} n\'a pas d\'antécédent (non surjective).'),
            ('Conclusion', '$f$ {} injective, {} surjective.'),
        ],
    },
    'relation': {
        'titre': 'Relation binaire',
        'source': ['maths-s1-obm/11'],
        'etapes': [
            ('Réflexive', '{} donc $a\\,\\mathcal{R}\\,a$.'),
            ('Symétrique', 'Preuve, ou contre-exemple : {}.'),
            ('Antisymétrique', '$a\\,\\mathcal{R}\\,b$ et $b\\,\\mathcal{R}\\,a$ donnent {}, donc $a = b$.'),
            ('Transitive', '$a\\,\\mathcal{R}\\,b$ et $b\\,\\mathcal{R}\\,c$ donnent {}, donc $a\\,\\mathcal{R}\\,c$.'),
            ('Conclusion', 'Relation d\'ordre (réflexive, antisymétrique, transitive) ou d\'équivalence (réflexive, symétrique, transitive) : {}.'),
        ],
    },
}

# one level = one exercise type; the exam levels mix types and have no skeleton
NIVEAUX = {
    'maths-s1-apis-suites/1': 'suite_nature',
    'maths-s1-apis-suites/2': 'monotonie',
    'maths-s1-apis-suites/3': 'bornee',
    'maths-s1-apis-suites/4': 'limite',
    'maths-s1-apis-suites/5': 'limite',
    'maths-s1-apis-suites/6': 'comparaison',
    'maths-s1-apis-suites/7': 'arith_geo',
    'maths-s1-apis-suites/8': 'limite_monotone',
    'maths-s1-apis-suites/9': 'adjacentes',
    'maths-s1-apis-suites/10': 'recurrente',
    'maths-s1-apis-suites/11': 'extraites',
    'maths-s1-apis-suites/12': 'comparaison_o',
    'maths-s1-apis-integrales/1': 'derivee',
    'maths-s1-apis-integrales/2': 'primitive',
    'maths-s1-apis-integrales/3': 'primitive',
    'maths-s1-apis-integrales/4': 'primitive',
    'maths-s1-apis-integrales/5': 'primitive',
    'maths-s1-apis-integrales/6': 'ipp',
    'maths-s1-apis-integrales/7': 'ipp',
    'maths-s1-apis-integrales/8': 'ipp',
    'maths-s1-apis-integrales/9': 'ipp',
    'maths-s1-apis-integrales/10': 'changement_variable',
    'maths-s1-apis-integrales/11': 'changement_variable',
    'maths-s1-apis-integrales/12': 'changement_variable',
    'maths-s1-apis-edo/1': 'edo1_homogene',
    'maths-s1-apis-edo/4': 'edo1_homogene',
    'maths-s1-apis-edo/2': 'edo1_complete',
    'maths-s1-apis-edo/3': 'edo1_complete',
    'maths-s1-apis-edo/5': 'edo1_complete',
    'maths-s1-apis-edo/6': 'edo1_ci',
    'maths-s1-apis-edo/7': 'edo2',
    'maths-s1-apis-edo/8': 'edo2',
    'maths-s1-apis-edo/9': 'edo2',
    'maths-s1-apis-edo/10': 'edo2',
    'maths-s1-dp/1': 'cardinaux',
    'maths-s1-dp/2': 'denombrement',
    'maths-s1-dp/3': 'denombrement',
    'maths-s1-dp/5': 'denombrement',
    'maths-s1-dp/6': 'double_comptage',
    'maths-s1-dp/7': 'equiprobabilite',
    'maths-s1-dp/9': 'proba_totales',
    'maths-s1-dp/10': 'proba_totales',
    'maths-s1-dp/11': 'independance',
    'maths-s1-dp/12': 'loi_va',
    'maths-s1-dp/13': 'loi_va',
    'maths-s1-dp/14': 'binomiale',
    'maths-s1-obm/3': 'negation',
    'maths-s1-obm/5': 'negation',
    'maths-s1-obm/4': 'quantificateurs',
    'maths-s1-obm/6': 'contraposee',
    'maths-s1-obm/7': 'recurrence',
    'maths-s1-obm/9': 'image',
    'maths-s1-obm/10': 'injection',
    'maths-s1-obm/11': 'relation',
}

# exercises already done on the type -> stage (1: full copy, 2: holes, 3: skeleton alone, 4: checklist after)
PALIERS = ((0, 1), (1, 2), (3, 3), (6, 4))


def niveaux_du_type(key):
    """(subject, n) of every level sharing skeleton `key`."""
    return [(k.rsplit('/', 1)[0], int(k.rsplit('/', 1)[1])) for k, v in NIVEAUX.items() if v == key]


def palier(faits):
    return max(p for seuil, p in PALIERS if faits >= seuil)


def pour(subject, n, faits):
    """Skeleton of level `subject/n` at the stage reached after `faits` exercises of its type, or None."""
    key = NIVEAUX.get(f'{subject}/{n}')
    if not key:
        return None
    s = SQUELETTES[key]
    return {'cle': key, 'titre': s['titre'], 'palier': palier(faits), 'etapes': s['etapes']}
