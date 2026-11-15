# Final exam 1 — January 2017 (subject, EN)

- Source : `raw/S1/Finals/Maths PC/2021/final-2021-s1-maths-subject-en.pdf` (scan, 7 pages)
- Date réelle : janvier 2017 (S1 16/17, dossier promo 2021). Version anglaise de `final-2021-s1-maths-subject-fr.md` ; corrigé : `final-2021-s1-maths-correction-fr.md`.
- Duration: three hours. Documents and calculators not allowed.

## Exercise 1 (2 points)
Type : nier une phrase · ECUE : OBM · Niveau : maths-s1-obm/3
Formules : $\neg(\forall x, P(x)) \iff \exists x, \neg P(x)$ ; $\neg(\exists x, P(x)) \iff \forall x, \neg P(x)$ ; $\neg(P \Rightarrow Q) \iff P \wedge \neg Q$ ; $\neg(P \wedge Q) \iff \neg P \vee \neg Q$ ; $\neg(P \vee Q) \iff \neg P \wedge \neg Q$ ; « aucun » = $\forall, \neg$

Write the negation of the following sentences:
1. « The square root of an even natural number is even ».
2. « For any triangle in the plane, the sum of the angles is equal to 180° in Euclidean geometry ».
3. « Some students will not leave for their semester abroad in S4 ».
4. « Some students will leave for their semester abroad in S4 ».

## Exercise 2 (2 points)
Type : récurrence ($n! > 2^n$) · ECUE : OBM · Niveau : maths-s1-obm/7
Formules : récurrence : $P(n_0)$ et $P(n) \Rightarrow P(n+1)$ ; $(n+1)! = (n+1)\,n!$ ; $2^{n+1} = 2 \cdot 2^n$ ; $n + 1 > 2$

Prove by induction that for any $n \geqslant 4$, $n! > 2^n$.

## Exercise 3 (2 points)
Type : traduire avec quantificateurs · ECUE : OBM · Niveau : maths-s1-obm/4
Formules : « tout » $= \forall$, « il existe » $= \exists$, « aucun » $= \forall \dots \neg$ ; l'ordre $\forall\exists$ / $\exists\forall$ change le sens ; $f$ s'annule : $\exists x, f(x) = 0$ ; minimum en $a$ : $\exists a, \forall x, f(x) \geqslant f(a)$ ; pair : $\exists k, n = 2k$

Let $f$ be a function from $\mathbb{R}$ to $\mathbb{R}$. Write in mathematical language (using quantifiers) the following sentences:
1. « the function $f$ has at least one root ».
2. « $f$ is not the zero function ».
3. « $f$ is the zero function ».
4. « $f$ admits a minimum on $\mathbb{R}$ ».

## Exercise 4 (2 points)
Type : composée d'injections / surjections · ECUE : OBM · Niveau : maths-s1-obm/10
Formules : $(f \circ g)(x) = f(g(x))$ ; injective : $f(x) = f(y) \Rightarrow x = y$ ; surjective : $\forall y, \exists x, y = f(x)$ ; $g \circ f$ injective $\Rightarrow f$ injective ; $g \circ f$ surjective $\Rightarrow g$ surjective

Let $E$ be a set, $f : E \to E$ and $g : E \to E$.
1. We suppose that both $f$ and $g$ are injective. Show that $f \circ g$ is injective.
2. We suppose that both $f$ and $g$ are surjective. Show that $f \circ g$ is surjective.
3. Show that $g \circ f$ injective $\Longrightarrow$ $f$ injective.
4. Show that $g \circ f$ surjective $\Longrightarrow$ $g$ surjective.

## Exercise 5 (3 points)
Type : équation diophantienne $ax+by=c$ (Euclide, Gauss) · ECUE : HP (arithmétique)
Formules : Euclide : $a = bq + r$, $a \wedge b = b \wedge r$ ; solutions $\iff (a \wedge b) \mid c$ ; diviser par $d = a \wedge b$ ; remonter Euclide : $au_0 + bv_0 = d$ puis multiplier par $c/d$ ; Gauss : $a \mid bc$ et $a \wedge b = 1 \Rightarrow a \mid c$ ; $a(x - x_0) = -b(y - y_0)$ donne $x = x_0 + \frac{b}{d}k$, $y = y_0 - \frac{a}{d}k$, $k \in \mathbb{Z}$ ; vérifier la réciproque

1. Using Euclid's algorithm, determine a particular solution of the equation $732x + 124y = 4$.
2. Using imperatively Gauss's theorem, determine the set of all the ordered pairs $(x,y) \in \mathbb{Z}^2$ such that $732x + 124y = 4$.

## Exercise 6 (3 points)
Type : Bézout ($a+b$ et $ab$ premiers entre eux) · ECUE : HP (arithmétique)
Formules : Bézout : $a \wedge b = 1 \iff \exists (u,v) \in \mathbb{Z}^2, au + bv = 1$ ; $(au + bv)^2 = 1$ ; $a^2u^2 + b^2v^2 = (a+b)(au^2 + bv^2) - ab(u^2 + v^2)$

Let $(a,b) \in \mathbb{N}^2$. Show that: $(a+b)$ and $ab$ are coprime $\iff$ $a$ and $b$ are coprime.

## Exercise 7 (2 points)
Type : congruences, reste d'une puissance · ECUE : HP (arithmétique)
Formules : $a \equiv b\,[n] \Rightarrow a^k \equiv b^k\,[n]$ ; chercher la période : $a^p \equiv 1\,[n]$ ; division euclidienne de l'exposant $N = pq + r$ : $a^N = (a^p)^q a^r$ ; le reste est dans $[\![0, n-1]\!]$

What is the remainder of the Euclidean division of $12^{1527}$ by 5?

## Exercise 8 (2 points)
Type : multiplicité d'une racine d'un polynôme · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/4
Formules : $\alpha$ racine d'ordre $m$ $\iff P(\alpha) = P'(\alpha) = \dots = P^{(m-1)}(\alpha) = 0$ et $P^{(m)}(\alpha) \neq 0$ ; $(X^n)' = nX^{n-1}$

Determine the order of multiplicity of the root 1 of the polynomial $P(X) = X^4 - 2X^3 + 2X - 1$.

## Exercise 9 (3 points)
Type : divisibilité de polynômes par les racines · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/3
Formules : $X - a \mid P \iff P(a) = 0$ ; $(X-a)(X-b) \mid P \iff P(a) = P(b) = 0$ ($a \neq b$) ; $(X-a)^2 \mid P \iff P(a) = P'(a) = 0$

Let $n \in \mathbb{N}^*$.
1. Show that $X^2 + 2X$ divides $(X+1)^{2n} - 1$.
2. Show that $X^2$ divides $(X+1)^n - nX - 1$.
3. Show that $(X-1)^2$ divides $nX^{n+1} - (n+1)X^n + 1$.
