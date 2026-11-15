# Corrigé du partiel 1 — janvier 2017

- Source : `raw/S1/Finals/Maths PC/2021/final-2021-s1-maths-correction-fr.pdf` (3 pages)
- Date réelle : janvier 2017 (Info-Sup 16/17, dossier promo 2021). Sujet : `final-2021-s1-maths-subject-fr.md`.

## Exercice 1 (2 points)
Type : nier une phrase · ECUE : OBM · Niveau : maths-s1-obm/3
Formules : $\neg(\forall x, P(x)) \iff \exists x, \neg P(x)$ ; $\neg(\exists x, P(x)) \iff \forall x, \neg P(x)$ ; $\neg(P \Rightarrow Q) \iff P \wedge \neg Q$ ; $\neg(P \wedge Q) \iff \neg P \vee \neg Q$ ; $\neg(P \vee Q) \iff \neg P \wedge \neg Q$ ; « aucun » = $\forall, \neg$

1. « Il existe un entier pair dont la racine carrée n'est pas un entier pair ».
2. « Il existe un triangle dont la somme des angles ne vaut pas 180° en géométrie euclidienne ».
3. « Tous les étudiants auront vécu l'expérience internationale dès le S4 ».
4. « Aucun étudiant n'aura vécu l'expérience internationale dès le S4 ».

## Exercice 2 (2 points)
Type : récurrence ($n! > 2^n$) · ECUE : OBM · Niveau : maths-s1-obm/7
Formules : récurrence : $P(n_0)$ et $P(n) \Rightarrow P(n+1)$ ; $(n+1)! = (n+1)\,n!$ ; $2^{n+1} = 2 \cdot 2^n$ ; $n + 1 > 2$

Pour $n = 4$ la propriété est vérifiée puisque $4! = 24 > 16$.
Supposons la propriété vérifiée pour un certain entier $n \geqslant 4$ et montrons-la au rang $n+1$.
Via cette hypothèse de récurrence et vu que $n \geqslant 4 > 1$, on a immédiatement $(n+1)! = n!(n+1) \geqslant 2^n(n+1) > 2^n \cdot 2$, c'est-à-dire $(n+1)! > 2^{n+1}$.
Donc si la propriété est vérifiée au rang $n$, elle est vérifiée au rang $n+1$. Ainsi, pour tout $n \geqslant 4$, $n! > 2^n$.

## Exercice 3 (2 points)
Type : traduire avec quantificateurs · ECUE : OBM · Niveau : maths-s1-obm/4
Formules : « tout » $= \forall$, « il existe » $= \exists$, « aucun » $= \forall \dots \neg$ ; l'ordre $\forall\exists$ / $\exists\forall$ change le sens ; $f$ s'annule : $\exists x, f(x) = 0$ ; minimum en $a$ : $\exists a, \forall x, f(x) \geqslant f(a)$ ; pair : $\exists k, n = 2k$

1. $\exists x \in \mathbb{R},\ f(x) = 0$.
2. $\exists x \in \mathbb{R},\ f(x) \neq 0$.
3. $\forall x \in \mathbb{R},\ f(x) = 0$.
4. $\exists a \in \mathbb{R}, \forall x \in \mathbb{R},\ f(x) \geqslant f(a)$.

## Exercice 4 (2 points)
Type : composée d'injections / surjections · ECUE : OBM · Niveau : maths-s1-obm/10
Formules : $(f \circ g)(x) = f(g(x))$ ; injective : $f(x) = f(y) \Rightarrow x = y$ ; surjective : $\forall y, \exists x, y = f(x)$ ; $g \circ f$ injective $\Rightarrow f$ injective ; $g \circ f$ surjective $\Rightarrow g$ surjective

1. Soit $(x,y) \in E^2$ tel que $(f \circ g)(x) = (f \circ g)(y)$. Alors $f(g(x)) = f(g(y))$. Or $f$ est injective donc $g(x) = g(y)$ et via l'injectivité de $g$, on a finalement $x = y$. Ainsi $f \circ g$ est injective.
2. Soit $y \in E$. Comme $f$ est surjective, il existe $x \in E$ tel que $y = f(x)$ et via la surjectivité de $g$, il existe $z \in E$ tel que $x = g(z)$. Finalement $y = f(g(z))$ donc $f \circ g$ est surjective.
3. Supposons $g \circ f$ injective et montrons que $f$ est injective. Soit $(x,y) \in E^2$ tel que $f(x) = f(y)$. Alors $g(f(x)) = g(f(y))$ donc via l'injectivité de $g \circ f$, $x = y$. Ainsi $f$ est injective.
4. Supposons $g \circ f$ surjective et montrons que $g$ est surjective. Soit $y \in E$. Via la surjectivité de $g \circ f$, il existe $x \in E$ tel que $y = g(f(x))$. Comme $f(x) \in E$, $g$ est surjective.

## Exercice 5 (3 points)
Type : équation diophantienne $ax+by=c$ (Euclide, Gauss) · ECUE : HP (arithmétique)
Formules : Euclide : $a = bq + r$, $a \wedge b = b \wedge r$ ; solutions $\iff (a \wedge b) \mid c$ ; diviser par $d = a \wedge b$ ; remonter Euclide : $au_0 + bv_0 = d$ puis multiplier par $c/d$ ; Gauss : $a \mid bc$ et $a \wedge b = 1 \Rightarrow a \mid c$ ; $a(x - x_0) = -b(y - y_0)$ donne $x = x_0 + \frac{b}{d}k$, $y = y_0 - \frac{a}{d}k$, $k \in \mathbb{Z}$ ; vérifier la réciproque

1. Notons $(*)$ l'équation $732x + 124y = 4$. Commençons par déterminer $732 \wedge 124$.

| a | b | quotients | restes |
|---|---|---|---|
| 732 | 124 | 5 | 112 |
| 124 | 112 | 1 | 12 |
| 112 | 12 | 9 | 4 |
| 12 | 4 | 3 | 0 |

Donc $732 \wedge 124 = 4$. Solution particulière en remontant l'algorithme d'Euclide :
$4 = 112 - 9 \times 12 = 112 - 9 \times (124 - 112) = 10 \times 112 - 9 \times 124 = 10 \times (732 - 5 \times 124) - 9 \times 124 = 732 \times 10 - 124 \times 59$.
Ainsi $(10, -59)$ est une solution particulière de l'équation $(*)$.

2. Soit $(x,y)$ solution de $(*)$. On a $732x + 124y = 4$ et $732 \times 10 - 124 \times 59 = 4$.
En soustrayant : $732(10 - x) = 124(59 + y)$, soit en divisant par le pgcd 4 : $183(10 - x) = 31(59 + y)$ $(**)$.
Ainsi $183 \mid 31(59 + y)$ et $183 \wedge 31 = 1$ donc, via le théorème de Gauss, $183 \mid 59 + y$ : il existe $k \in \mathbb{Z}$ tel que $y = 183k - 59$.
En reportant dans $(**)$ : $183(10 - x) = 31 \times 183k$ soit $x = 10 - 31k$.
Réciproquement, pour tout $k \in \mathbb{Z}$, $(10 - 31k, 183k - 59)$ est solution de $(*)$.
Finalement $S = \{(10 - 31k, 183k - 59) ; k \in \mathbb{Z}\}$.

## Exercice 6 (3 points)
Type : Bézout ($a+b$ et $ab$ premiers entre eux) · ECUE : HP (arithmétique)
Formules : Bézout : $a \wedge b = 1 \iff \exists (u,v) \in \mathbb{Z}^2, au + bv = 1$ ; $(au + bv)^2 = 1$ ; $a^2u^2 + b^2v^2 = (a+b)(au^2 + bv^2) - ab(u^2 + v^2)$

Supposons $(a+b)$ et $ab$ premiers entre eux. Via Bézout, il existe $(u,v) \in \mathbb{Z}^2$ tel que $(a+b)u + abv = 1$. Ainsi $au + b(u + av) = 1$ : via Bézout, $a$ et $b$ sont premiers entre eux.
Réciproquement, supposons $a$ et $b$ premiers entre eux : il existe $(u,v) \in \mathbb{Z}^2$ tel que $au + bv = 1$.
Donc $(au + bv)^2 = 1$, soit $a^2u^2 + b^2v^2 + 2abuv = 1$, soit $(a+b)(au^2 + bv^2) - ab(u^2 + v^2) + 2abuv = 1$, soit encore
$$(a+b)(au^2 + bv^2) + ab(2uv - u^2 - v^2) = 1.$$
Via Bézout ($au^2 + bv^2$ et $2uv - u^2 - v^2$ étant deux entiers), $a+b$ et $ab$ sont premiers entre eux.

## Exercice 7 (2 points)
Type : congruences, reste d'une puissance · ECUE : HP (arithmétique)
Formules : $a \equiv b\,[n] \Rightarrow a^k \equiv b^k\,[n]$ ; chercher la période : $a^p \equiv 1\,[n]$ ; division euclidienne de l'exposant $N = pq + r$ : $a^N = (a^p)^q a^r$ ; le reste est dans $[\![0, n-1]\!]$

$12 \equiv 2\,[5]$ donc $12^{1527} \equiv 2^{1527}\,[5]$. Or $2^2 \equiv 4$, $2^3 \equiv 3$ et $2^4 \equiv 1\,[5]$.
$1527 = 381 \times 4 + 3$, donc $2^{1527} = (2^4)^{381} \times 2^3 \equiv 3\,[5]$.
Le reste de la division euclidienne de $12^{1527}$ par 5 est 3.

## Exercice 8 (2 points)
Type : multiplicité d'une racine d'un polynôme · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/4
Formules : $\alpha$ racine d'ordre $m$ $\iff P(\alpha) = P'(\alpha) = \dots = P^{(m-1)}(\alpha) = 0$ et $P^{(m)}(\alpha) \neq 0$ ; $(X^n)' = nX^{n-1}$

$P(1) = 0$. $P'(X) = 4X^3 - 6X^2 + 2$ donc $P'(1) = 0$. $P''(X) = 12X^2 - 12X$ donc $P''(1) = 0$. $P'''(X) = 24X - 12$ donc $P'''(1) \neq 0$. Ainsi, 1 est une racine d'ordre 3 de $P$.

## Exercice 9 (3 points)
Type : divisibilité de polynômes par les racines · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/3
Formules : $X - a \mid P \iff P(a) = 0$ ; $(X-a)(X-b) \mid P \iff P(a) = P(b) = 0$ ($a \neq b$) ; $(X-a)^2 \mid P \iff P(a) = P'(a) = 0$

1. $P(X) = (X+1)^{2n} - 1$ et $X^2 + 2X = X(X+2)$. $P(0) = 0$ et $P(-2) = (-1)^{2n} - 1 = 0$ donc $X^2 + 2X$ divise $P$.
2. $Q(X) = (X+1)^n - nX - 1$. $Q(0) = 0$ et $Q'(X) = n(X+1)^{n-1} - n$, $Q'(0) = 0$. D'où $X^2$ divise $Q$.
3. $R(X) = nX^{n+1} - (n+1)X^n + 1$. $R(1) = 0$ et $R'(X) = n(n+1)X^n - n(n+1)X^{n-1}$, $R'(1) = 0$. Donc $(X-1)^2$ divise $R$.
