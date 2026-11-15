# Feuille de TD — Les polynômes (S2 2026) (sujet, FR)

- Source : `raw/S2/TDs/2030/Maths/td1-2030-s2-maths-subject-fr.pdf` (6 pages)
- Date réelle : S2 2026 (dossier promo 2030). Feuille de TD d'une semaine, ECUE APEF (bloc B3). Pas de corrigé dans les annales. Corrigé rédigé : `td1-2030-s2-maths-correction-fr.md` (même dossier).
- Prérequis : OBM du séminaire, développer un produit de polynômes, résoudre une équation du second degré. Seuls les exercices sont transcrits (ni la motivation ni les résumés de cours). Les exercices marqués ⋆ sont plus difficiles.

Attendus : déterminer le degré d'une somme ou d'un produit ; énoncer et faire une division euclidienne ; relier racine et factorisation ; relier racine et dérivées successives ; déterminer l'ordre de multiplicité d'une racine ; factoriser en produit d'irréductibles dans $\mathbb{C}[X]$ ou $\mathbb{R}[X]$.

## Exercice 1.1
Type : degré, division euclidienne de polynômes, racine · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/2
Formules : $\deg(A+B) \leqslant \max(\deg A, \deg B)$ ; $\deg(AB) = \deg A + \deg B$ ; $\exists!\,(Q,R)$, $A = BQ + R$, $\deg R < \deg B$ ; $\alpha$ racine $\iff A(\alpha) = 0 \iff X - \alpha \mid A$

1. Soient $P(X) = -2X^3 + 3X - 4$, $Q(X) = 3X^2 + 6X - 2$ et $R(X) = 1 + 2X^3$. Donner $P(X) + Q(X)$, $P(X) + R(X)$ et $Q(X) + R(X)$. En déduire une formule sur le degré de la somme de 2 polynômes.
2. Donner le degré ainsi que le terme de plus haut degré de $A(X) = X^2(X^3 - 4)(2X + 1)^2$. Même question pour $B(X) = (5X^2 + X - 3)^2 - X^3 + 2$.

## Exercice 1.2
Type : formule de Taylor pour les polynômes · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/7
Formules : $P = \sum a_kX^k \Rightarrow a_k = \frac{P^{(k)}(0)}{k!}$ ; $P(X) = \sum_{k=0}^{\deg P} \frac{P^{(k)}(0)}{k!}X^k$ ; en $a$ : $P(X) = \sum_{k=0}^{\deg P} \frac{P^{(k)}(a)}{k!}(X - a)^k$ ; $(X^n)^{(k)} = \frac{n!}{(n-k)!}X^{n-k}$

On considère le polynôme $P(X) = 3X^3 - 2X^2 - 7X + 6 = \displaystyle\sum_{k=0}^3 a_kX^k$.
1. Donner $a_0$, $a_1$, $a_2$ et $a_3$.
2. Calculer toutes les dérivées successives de $P$ en 0.
3. Trouver le lien entre $P(0)$ et les coefficients de $P$.
4. Faire de même pour $P'(0)$, $P''(0)$ et $P^{(3)}(0)$.
5. Proposer une formule générale reliant les dérivées successives de $P$ en 0 aux coefficients de $P$. En déduire une nouvelle écriture de $P$.
6. (⋆) Posons $Y = X - 1$.
   - (a) Expliquer pourquoi $P(X)$ peut prendre la forme $Q(Y) = \displaystyle\sum_{k=0}^3 b_kY^k$ où pour $k \in [\![0,3]\!]$, $b_k = \dfrac{Q^{(k)}(0)}{k!}$.
   - (b) En déduire qu'on a aussi $P(X) = \displaystyle\sum_{k=0}^3 \frac{P^{(k)}(1)}{k!}(X-1)^k$.

## Exercice 2.3
Type : degré, division euclidienne de polynômes, racine · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/2
Formules : $\deg(A+B) \leqslant \max(\deg A, \deg B)$ ; $\deg(AB) = \deg A + \deg B$ ; $\exists!\,(Q,R)$, $A = BQ + R$, $\deg R < \deg B$ ; $\alpha$ racine $\iff A(\alpha) = 0 \iff X - \alpha \mid A$

1. Effectuer la division euclidienne de $2X^4 - X^2 + X - 5$ par $X^2 + X - 2$.
2. Effectuer la division euclidienne de $X^3 + X + 1$ par $2X + 1$.

## Exercice 2.4
Type : division euclidienne et primitive d'une fraction rationnelle · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/8
Formules : $A = BQ + R$, $\deg R < \deg B$ $\Rightarrow \frac AB = Q + \frac RB$ ; $\int x^n = \frac{x^{n+1}}{n+1}$ ; $\int \frac{u'}u = \ln|u|$ ; $\int \frac{dx}{1+x^2} = \arctan x$

1. Effectuer la division euclidienne de $X^4 + 2X^3 + X$ par $X^2 + 1$.
2. En déduire une primitive sur $\mathbb{R}$ de la fonction $x \mapsto \dfrac{x^4 + 2x^3 + x}{x^2 + 1}$.

## Exercice 3.5
Type : divisibilité de polynômes par les racines · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/3
Formules : $X - a \mid P \iff P(a) = 0$ ; $(X-a)(X-b) \mid P \iff P(a) = P(b) = 0$ ($a \neq b$) ; $(X-a)^2 \mid P \iff P(a) = P'(a) = 0$

1. Soit $P \in \mathbb{K}[X]$ avec $\mathbb{K} = \mathbb{R}$ ou $\mathbb{C}$, et $a \in \mathbb{K}$. Quel est le reste dans la division euclidienne de $P$ par $X - a$ ?
2. En déduire la propriété suivante : $(X - a) \mid P \iff P(a) = 0$.
3. Soient $P \in \mathbb{R}[X]$ et $(a,b) \in \mathbb{R}^2$ tels que $a \neq b$. Montrer que $(X-a)(X-b) \mid P \iff P(a) = P(b) = 0$.

## Exercice 3.6
Type : divisibilité de polynômes, multiplicité, factorisation dans $\mathbb{R}[X]$ et $\mathbb{C}[X]$ · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/9
Formules : $P(a) = 0 \iff X - a \mid P$ ; racine d'ordre $\geqslant 2$ $\iff P(a) = P'(a) = 0$ ; ordre exactement $m$ : $P^{(m)}(a) \neq 0$ ; $(X - a)^m \mid P$, $(X - a)^{m+1} \nmid P$ ; $X^2 + 1 = (X - i)(X + i)$ ; $\Delta < 0 \Rightarrow$ irréductible dans $\mathbb{R}[X]$

Soient $\mathbb{K} = \mathbb{R}$ ou $\mathbb{C}$, $P \in \mathbb{K}[X]$, $a \in \mathbb{K}$ et $\alpha \in \mathbb{N}^*$.
1. - (a) Rappeler ce que signifie (en termes de divisibilité) « $a$ est une racine d'ordre de multiplicité au moins $\alpha$ de $P$ » et « $a$ est une racine d'ordre de multiplicité exactement $\alpha$ de $P$ ».
   - (b) Application : prenons $P(X) = (X^2 - X)(X - 1)^2(-1 - X) \in \mathbb{R}[X]$. Donner les racines de $P$ ainsi que leurs ordres exacts de multiplicité.
2. - (a) Rappeler le lien entre l'ordre de multiplicité d'une racine d'un polynôme et ses dérivées successives en cette racine.
   - (b) On admet que le polynôme $P$ ci-dessus s'écrit aussi $P(X) = -X^5 + 2X^4 - 2X^2 + X$. Retrouver les résultats de la question 1.(b) en utilisant les dérivées successives de $P$.
3. - (a) Que signifie qu'un polynôme $P$ est irréductible dans $\mathbb{K}[X]$ ? Quels sont les polynômes irréductibles de $\mathbb{R}[X]$ et $\mathbb{C}[X]$ ?
   - (b) Prenons $P(X) = (X^3 + X)(X^2 - 2X)$. Écrire $P$ en produit de polynômes irréductibles dans $\mathbb{R}[X]$ et dans $\mathbb{C}[X]$.

## Exercice 3.7
Type : divisibilité de polynômes, multiplicité, factorisation dans $\mathbb{R}[X]$ et $\mathbb{C}[X]$ · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/9
Formules : $P(a) = 0 \iff X - a \mid P$ ; racine d'ordre $\geqslant 2$ $\iff P(a) = P'(a) = 0$ ; ordre exactement $m$ : $P^{(m)}(a) \neq 0$ ; $(X - a)^m \mid P$, $(X - a)^{m+1} \nmid P$ ; $X^2 + 1 = (X - i)(X + i)$ ; $\Delta < 0 \Rightarrow$ irréductible dans $\mathbb{R}[X]$

1. On considère le polynôme $P(X) = X^4 + 2X^3 - X - 2$.
   - (a) Montrer que 1 et $-2$ sont racines de $P$. Qu'en déduit-on en termes de divisibilité ?
   - (b) En vous aidant d'une division euclidienne, factoriser $P$ en produit de polynômes irréductibles dans $\mathbb{R}[X]$ et dans $\mathbb{C}[X]$.
2. (Travail personnel) On considère le polynôme $Q(X) = X^4 - 2X^3 - 3X^2 + 8X - 4$.
   - (a) Montrer que 2 et $-2$ sont racines de $Q$. Qu'en déduit-on en termes de divisibilité ?
   - (b) En vous aidant d'une division euclidienne, factoriser $Q$ en produit de polynômes irréductibles dans $\mathbb{R}[X]$ et dans $\mathbb{C}[X]$.
3. On considère le polynôme $R(X) = X^4 - 3X^3 - 3X^2 + 11X - 6$.
   - (a) Montrer que 1 est racine de $R$. Quelle est sa multiplicité ? Qu'en déduit-on en termes de divisibilité ?
   - (b) En vous aidant d'une division euclidienne, factoriser $R$ en produit de polynômes irréductibles dans $\mathbb{R}[X]$ et dans $\mathbb{C}[X]$.

## Exercice 3.8
Type : divisibilité de polynômes, multiplicité d'une racine · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/4
Formules : $(X-a)(X-b) \mid P \iff P(a) = P(b) = 0$ ($a \neq b$) ; $\alpha$ racine d'ordre $m$ $\iff P(\alpha) = \dots = P^{(m-1)}(\alpha) = 0$, $P^{(m)}(\alpha) \neq 0$ ; $(X^n)' = nX^{n-1}$

Soit $n \geqslant 2$.
1. Montrer que le polynôme $P(X) = (X+1)^{2n} - 1$ est divisible par $X^2 + 2X$.
2. Montrer que $(X-1)^2$ divise $nX^{n+1} - (n+1)X^n + 1$.
3. Montrer que 1 est racine du polynôme $nX^{n+2} - (n+2)X^{n+1} + (n+2)X - n$. Quelle est sa multiplicité ?

## Exercice 3.9
Type : divisibilité et reste de division euclidienne de polynômes · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/5
Formules : $A = BQ + R$, $\deg R < \deg B$ ; $(X-a)(X-b) \mid P \iff P(a) = P(b) = 0$ ($a \neq b$) ; reste par $(X-a)(X-b)$ : $R = \alpha X + \beta$ avec $R(a) = P(a)$, $R(b) = P(b)$ ; reste par $(X-a)^2$ : $R(a) = P(a)$, $R'(a) = P'(a)$

Déterminer le reste de la division euclidienne de $Q(X) = (X-2)^{2n} + (X-1)^n - 2$ par :
1. $(X-2)(X-1)$.
2. $(X-1)^2$.

## Exercice 3.10 (⋆)
Type : divisibilité et reste de division euclidienne de polynômes · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/5
Formules : $A = BQ + R$, $\deg R < \deg B$ ; $(X-a)(X-b) \mid P \iff P(a) = P(b) = 0$ ($a \neq b$) ; reste par $(X-a)(X-b)$ : $R = \alpha X + \beta$ avec $R(a) = P(a)$, $R(b) = P(b)$ ; reste par $(X-a)^2$ : $R(a) = P(a)$, $R'(a) = P'(a)$

Trouver tous les polynômes unitaires de degré 3, divisibles par $X - 1$ et dont les restes lors des divisions par $X - 2$, $X - 3$ et $X - 4$ sont égaux.
