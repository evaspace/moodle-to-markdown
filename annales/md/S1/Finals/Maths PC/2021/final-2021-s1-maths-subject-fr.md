# Partiel 1 — janvier 2017 (sujet, FR)

- Source : `raw/S1/Finals/Maths PC/2021/final-2021-s1-maths-subject-fr.pdf` (scan, 7 pages)
- Date réelle : janvier 2017 (Info-Sup 16/17, dossier promo 2021). Corrigé : `final-2021-s1-maths-correction-fr.md`.
- Durée : trois heures. Documents et calculatrices non autorisés. Barème : 21 points.

## Exercice 1 (2 points)
Type : nier une phrase · ECUE : OBM · Niveau : maths-s1-obm/3
Formules : $\neg(\forall x, P(x)) \iff \exists x, \neg P(x)$ ; $\neg(\exists x, P(x)) \iff \forall x, \neg P(x)$ ; $\neg(P \Rightarrow Q) \iff P \wedge \neg Q$ ; $\neg(P \wedge Q) \iff \neg P \vee \neg Q$ ; $\neg(P \vee Q) \iff \neg P \wedge \neg Q$ ; « aucun » = $\forall, \neg$

Écrire la négation des phrases suivantes :
1. « La racine carrée d'un entier pair est paire ».
2. « Dans n'importe quel triangle du plan, la somme des angles vaut 180° en géométrie euclidienne ».
3. « Certains étudiants n'auront pas vécu l'expérience internationale dès le S4 ».
4. « Certains étudiants auront vécu l'expérience internationale dès le S4 ».

## Exercice 2 (2 points)
Type : récurrence ($n! > 2^n$) · ECUE : OBM · Niveau : maths-s1-obm/7
Formules : récurrence : $P(n_0)$ et $P(n) \Rightarrow P(n+1)$ ; $(n+1)! = (n+1)\,n!$ ; $2^{n+1} = 2 \cdot 2^n$ ; $n + 1 > 2$

Montrer par récurrence que pour tout $n \geqslant 4$, $n! > 2^n$.

## Exercice 3 (2 points)
Type : traduire avec quantificateurs · ECUE : OBM · Niveau : maths-s1-obm/4
Formules : « tout » $= \forall$, « il existe » $= \exists$, « aucun » $= \forall \dots \neg$ ; l'ordre $\forall\exists$ / $\exists\forall$ change le sens ; $f$ s'annule : $\exists x, f(x) = 0$ ; minimum en $a$ : $\exists a, \forall x, f(x) \geqslant f(a)$ ; pair : $\exists k, n = 2k$

Soit $f$ une fonction de $\mathbb{R}$ vers $\mathbb{R}$. Écrire en langage mathématique (avec les quantificateurs) les phrases suivantes :
1. « la fonction $f$ s'annule au moins une fois ».
2. « $f$ n'est pas la fonction nulle ».
3. « $f$ est la fonction nulle ».
4. « $f$ présente un minimum sur $\mathbb{R}$ ».

## Exercice 4 (2 points)
Type : composée d'injections / surjections · ECUE : OBM · Niveau : maths-s1-obm/10
Formules : $(f \circ g)(x) = f(g(x))$ ; injective : $f(x) = f(y) \Rightarrow x = y$ ; surjective : $\forall y, \exists x, y = f(x)$ ; $g \circ f$ injective $\Rightarrow f$ injective ; $g \circ f$ surjective $\Rightarrow g$ surjective

Soient $E$ un ensemble, $f : E \to E$ et $g : E \to E$.
1. On suppose que $f$ et $g$ sont injectives. Montrer que $f \circ g$ est injective.
2. On suppose que $f$ et $g$ sont surjectives. Montrer que $f \circ g$ est surjective.
3. Montrer que $g \circ f$ injective $\Longrightarrow$ $f$ injective.
4. Montrer que $g \circ f$ surjective $\Longrightarrow$ $g$ surjective.

## Exercice 5 (3 points)
Type : équation diophantienne $ax+by=c$ (Euclide, Gauss) · ECUE : HP (arithmétique)
Formules : Euclide : $a = bq + r$, $a \wedge b = b \wedge r$ ; solutions $\iff (a \wedge b) \mid c$ ; diviser par $d = a \wedge b$ ; remonter Euclide : $au_0 + bv_0 = d$ puis multiplier par $c/d$ ; Gauss : $a \mid bc$ et $a \wedge b = 1 \Rightarrow a \mid c$ ; $a(x - x_0) = -b(y - y_0)$ donne $x = x_0 + \frac{b}{d}k$, $y = y_0 - \frac{a}{d}k$, $k \in \mathbb{Z}$ ; vérifier la réciproque

1. En utilisant l'algorithme d'Euclide, déterminer une solution particulière de l'équation $732x + 124y = 4$.
2. En utilisant obligatoirement le théorème de Gauss, déterminer l'ensemble des couples $(x,y) \in \mathbb{Z}^2$ tels que $732x + 124y = 4$.

## Exercice 6 (3 points)
Type : Bézout ($a+b$ et $ab$ premiers entre eux) · ECUE : HP (arithmétique)
Formules : Bézout : $a \wedge b = 1 \iff \exists (u,v) \in \mathbb{Z}^2, au + bv = 1$ ; $(au + bv)^2 = 1$ ; $a^2u^2 + b^2v^2 = (a+b)(au^2 + bv^2) - ab(u^2 + v^2)$

Soit $(a,b) \in \mathbb{N}^2$. Montrer que : $(a+b)$ et $ab$ premiers entre eux $\iff$ $a$ et $b$ premiers entre eux.

## Exercice 7 (2 points)
Type : congruences, reste d'une puissance · ECUE : HP (arithmétique)
Formules : $a \equiv b\,[n] \Rightarrow a^k \equiv b^k\,[n]$ ; chercher la période : $a^p \equiv 1\,[n]$ ; division euclidienne de l'exposant $N = pq + r$ : $a^N = (a^p)^q a^r$ ; le reste est dans $[\![0, n-1]\!]$

Quel est le reste de la division euclidienne de $12^{1527}$ par 5 ?

## Exercice 8 (2 points)
Type : multiplicité d'une racine d'un polynôme · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/4
Formules : $\alpha$ racine d'ordre $m$ $\iff P(\alpha) = P'(\alpha) = \dots = P^{(m-1)}(\alpha) = 0$ et $P^{(m)}(\alpha) \neq 0$ ; $(X^n)' = nX^{n-1}$

Déterminer l'ordre de multiplicité de la racine 1 du polynôme $P(X) = X^4 - 2X^3 + 2X - 1$.

## Exercice 9 (3 points)
Type : divisibilité de polynômes par les racines · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/3
Formules : $X - a \mid P \iff P(a) = 0$ ; $(X-a)(X-b) \mid P \iff P(a) = P(b) = 0$ ($a \neq b$) ; $(X-a)^2 \mid P \iff P(a) = P'(a) = 0$

Soit $n \in \mathbb{N}^*$.
1. Montrer que $X^2 + 2X$ divise $(X+1)^{2n} - 1$.
2. Montrer que $X^2$ divise $(X+1)^n - nX - 1$.
3. Montrer que $(X-1)^2$ divise $nX^{n+1} - (n+1)X^n + 1$.
