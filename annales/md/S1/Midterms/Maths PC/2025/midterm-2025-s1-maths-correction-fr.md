# Contrôle 1 S1 — novembre 2020 (fichier « correction », identique au sujet)

- Source : `raw/S1/Midterms/Maths PC/2025/midterm-2025-s1-maths-correction-fr.pdf` (8 pages). Malgré son nom, ce fichier est le sujet (texte identique à `midterm-2025-s1-maths-subject-fr.pdf`) : aucun corrigé.
- Date réelle : novembre 2020 (S1 2020, dossier promo 2025).
- Durée : 3 heures. Barème sur 30 points ramenés à 20. Documents et calculatrices interdits.

## Exercice 1 (3 points)
Type : traduire avec quantificateurs · ECUE : OBM · Niveau : maths-s1-obm/4
Formules : « tout » $= \forall$, « il existe » $= \exists$, « aucun » $= \forall \dots \neg$ ; l'ordre $\forall\exists$ / $\exists\forall$ change le sens ; $f$ s'annule : $\exists x, f(x) = 0$ ; minimum en $a$ : $\exists a, \forall x, f(x) \geqslant f(a)$ ; pair : $\exists k, n = 2k$

On appelle $C$ l'ensemble des élèves d'une classe. On définit sur $C$ la relation suivante : $\forall (e, e') \in C^2$, $e\,\mathcal{R}\,e' \iff$ « $e$ habite à moins de 5 mn de chez $e'$ ».
On notera $e\,\cancel{\mathcal{R}}\,e'$ si : « $e$ habite à strictement plus de 5 mn de chez $e'$ ».
Exprimer avec des quantificateurs les phrases suivantes.
Exemple : « Un des élèves de la classe est à moins de 5 mn de tous les autres élèves. » s'écrit : $\exists e \in C, \forall e' \in C, e\,\mathcal{R}\,e'$.
a. Tout élève a au moins un camarade à moins de 5 mn de chez lui.
b. Un des élèves n'a aucun camarade à moins de 5 mn de chez lui.
c. Si un élève $e$ habite à moins de 5 mn d'un élève $e'$ et que $e'$ habite à moins de 5 mn de $e''$, alors $e$ habite à moins de 5 mn de $e''$.

## Exercice 2 (4 points)
Type : relation d'ordre · ECUE : OBM · Niveau : maths-s1-obm/11
Formules : ordre = réflexive ($\forall x, x\mathcal Rx$), antisymétrique ($x\mathcal Ry$ et $y\mathcal Rx \Rightarrow x = y$), transitive ($x\mathcal Ry$ et $y\mathcal Rz \Rightarrow x\mathcal Rz$) ; contre-exemple pour réfuter ; $x^2 = y^2 \iff x = \pm y$

On s'intéresse de nouveau à la relation $\mathcal{R}$ décrite dans l'exercice 1. Citer les différentes propriétés qui définissent une relation d'ordre. Pour chacune d'elles, dire si la relation $\mathcal{R}$ la vérifie et justifier sa réponse.

## Exercice 3 (5 points)
Type : dérivée composée, changement de variable, IPP · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/13
Formules : $(\sin u)' = u'\cos u$ ; $(e^{3x})' = 3e^{3x}$ ; changement de variable $t = \sqrt{x^2+3}$ : $t\,dt = x\,dx$ ; IPP $u = \ln x$, $v' = \frac1{\sqrt x}$, $v = 2\sqrt x$ ; $\int \frac{1}{\sqrt x} = 2\sqrt x$

1. Sans vous préoccuper du domaine de définition, calculer la dérivée de la fonction : $f(x) = \sin(e^{3x} + 2)$.
2. Calculer l'intégrale $J = \displaystyle\int_0^1 \frac{x}{\sqrt{x^2 + 3}}\,dx$ en posant $t = \sqrt{x^2 + 3}$.
3. À l'aide d'une intégration par parties, calculer l'intégrale $K = \displaystyle\int_1^e \frac{\ln(x)}{\sqrt x}\,dx$.

## Exercice 4 (3 points)
Type : injectivité / surjectivité, restriction · ECUE : OBM · Niveau : maths-s1-obm/10
Formules : injective $\iff$ toute droite horizontale coupe le graphe au plus une fois ; surjective sur $F$ $\iff$ tout $y \in F$ est atteint ; $(x-2)^2 - 1 \geqslant -1$ ; restreindre le départ à $[2, +\infty[$ rend injective, l'arrivée à $[-1, +\infty[$ rend surjective

Soient $E = \mathbb{R}$, $F = \mathbb{R}$ et $f : E \to F,\ x \mapsto (x - 2)^2 - 1$ dont le graphe est donné (parabole de sommet $(2, -1)$).
a. $f$ est-elle injective ? Surjective ? Justifiez votre réponse.
b. Proposer un intervalle $I$ de $\mathbb{R}$ tel qu'en remplaçant un seul des ensembles $E$ ou $F$ par $I$, $f$ soit injective. Justifiez votre réponse.
c. Proposer un intervalle $J$ de $\mathbb{R}$ tel qu'en remplaçant un seul des ensembles $E$ ou $F$ par $J$, $f$ soit surjective. Justifiez votre réponse.

## Exercice 5 (4 points)
Type : coefficients binomiaux (symétrie) · ECUE : DP · Niveau : maths-s1-dp/6
Formules : $\binom np = \frac{n!}{p!(n-p)!}$ ; $\binom np = \binom n{n-p}$ ; $\binom np$ = nombre de parties à $p$ éléments d'un ensemble à $n$ éléments ; bijection $A \mapsto \bar A$

Soient $(n, p) \in \mathbb{N}^2$, $p \leqslant n$.
1. Quelle relation relie $\binom np$ et $\binom n{n-p}$ ?
2. Démontrer cette relation par le calcul.
3. Soit $E$ un ensemble à $n$ éléments. À quoi correspond le nombre $\binom np$ ? Comment justifier la relation du 1. ?

## Exercice 6 (4 points)
Type : récurrence (inégalité avec factorielle) · ECUE : OBM · Niveau : maths-s1-obm/7
Formules : récurrence ; $\frac{2^{n+1}}{(n+1)!} = \frac{2^n}{n!} \cdot \frac2{n+1}$ ; $n \geqslant 2 \Rightarrow \frac2{n+1} \leqslant \frac23$ ; initialisation $n = 2$ : $\frac{4}{2} = 2 = \frac92 \cdot \frac49$

Montrer par récurrence la proposition suivante : $\forall n \in \mathbb{N}$, $n \geqslant 2$, $\dfrac{2^n}{n!} \leqslant \dfrac92\left(\dfrac23\right)^n$.

## Exercice 7 (7 points)
Type : dénombrement (p-listes, arrangements, anagrammes, parties) · ECUE : DP · Niveau : maths-s1-dp/5
Formules : $p$-listes (avec remise, ordre) : $n^p$ ; arrangements (sans remise, ordre) : $A_n^p = \frac{n!}{(n-p)!}$ ; permutations : $n!$ ; anagrammes avec lettres répétées : $\frac{n!}{k_1!k_2!\dots}$ ; nombre de parties d'un ensemble à $m$ éléments : $2^m$ ; principe multiplicatif

Dans cet exercice, l'application numérique exacte n'est pas demandée : seule la formule appliquée aux données de l'exercice est attendue. Les questions sont indépendantes les unes des autres.
On considère l'ensemble $E = \{a, b, c, d, e, f, g, h, i, j, k, l\}$.
1. On appelle $M_5(E)$ l'ensemble des mots de cinq lettres construits à partir des lettres de $E$ avec répétition, comme par exemple : « kabke ».
   a. Quel est le cardinal de $M_5(E)$ ?
   b. Combien y a-t-il de mots contenant au moins une fois la lettre « l » dans $M_5(E)$ ?
   c. Combien y a-t-il d'anagrammes du mot « babab » ?
2. On appelle $N_5(E)$ l'ensemble des mots de 5 lettres sans répétition construits à partir des lettres de $E$. Exemple : « kgehj ».
   a. Quel est le cardinal de $N_5(E)$ ?
   b. Combien y a-t-il de mots se terminant par une voyelle dans $N_5(E)$ ?
   c. Combien y a-t-il de mots ne contenant aucune des lettres $\{a, d, e, f, h\}$ dans $N_5(E)$ ?
   d. Combien y a-t-il de mots contenant au moins une des lettres $\{a, d, e, f, h\}$ dans $N_5(E)$ ?
