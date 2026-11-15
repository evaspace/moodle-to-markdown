# Final exam n°1 — January 2016 (subject, EN)

- Source : `raw/S1/Finals/Maths PC/2020/final-2020-s1-maths-subject-en.pdf` (scan, 8 pages)
- Date réelle : janvier 2016 (Info-Sup 15/16, dossier promo 2020). Version anglaise de `final-2020-s1-maths-subject-fr.md` (même sujet).
- Duration: three hours. Documents and calculators not authorized.

## Exercise 1 (4 points)
Type : nier une phrase · ECUE : OBM · Niveau : maths-s1-obm/3
Formules : $\neg(\forall x, P(x)) \iff \exists x, \neg P(x)$ ; $\neg(\exists x, P(x)) \iff \forall x, \neg P(x)$ ; $\neg(P \Rightarrow Q) \iff P \wedge \neg Q$ ; $\neg(P \wedge Q) \iff \neg P \vee \neg Q$ ; $\neg(P \vee Q) \iff \neg P \wedge \neg Q$ ; « aucun » = $\forall, \neg$

Write the negation of the following sentences:
1. « No graduate of EPITA will have a first gross annual salary below 40 k€ ».
2. « If I join the research lab of EPITA, I'll be in a position to work in the medical imaging sector ».
3. « Some MiMo are complicated ».
4. « All your movements on IONISx are analyzed ».

## Exercise 2 (2 points)
Type : récurrence (inégalité de Bernoulli) · ECUE : OBM · Niveau : maths-s1-obm/7
Formules : récurrence : $P(n_0)$ et $P(n) \Rightarrow P(n+1)$ ; $(1+x)^{n+1} = (1+x)^n(1+x)$ ; $(1+nx)(1+x) = 1 + (n+1)x + nx^2 \geqslant 1 + (n+1)x$

Let $x \in \mathbb{R}_+^*$. Prove by induction that for all $n \in \mathbb{N}^*$, $(1+x)^n \geqslant 1 + nx$.

## Exercise 3 (2 points)
Type : traduire avec quantificateurs · ECUE : OBM · Niveau : maths-s1-obm/4
Formules : « tout » $= \forall$, « il existe » $= \exists$, « aucun » $= \forall \dots \neg$ ; l'ordre $\forall\exists$ / $\exists\forall$ change le sens ; $f$ s'annule : $\exists x, f(x) = 0$ ; minimum en $a$ : $\exists a, \forall x, f(x) \geqslant f(a)$ ; pair : $\exists k, n = 2k$

Write in mathematic language (using quantifiers) the following sentences (disregard the validity of the sentences, they may be true or false):
1. « Any real number is the cube of a real number ».
2. « There exists a real number which is the cube of all the real numbers ».
3. « Any natural number is even or odd ».
4. « Between two distinct real numbers, one can always find a rational number ».

## Exercise 4 (2 points)
Type : injectivité / surjectivité de $x \mapsto x^2$ · ECUE : OBM · Niveau : maths-s1-obm/10
Formules : injective : $f(x) = f(y) \Rightarrow x = y$ ; surjective : $\forall y \in F, \exists x \in E, y = f(x)$ ; $x^2 = y^2 \iff x = \pm y$ ; $x^2 \geqslant 0$

For each of the following questions, circle the correct answers (a. $f$ is injective; b. $f$ is not injective; c. $f$ is surjective; d. $f$ is not surjective).
1. $f : \mathbb{R}_+ \to \mathbb{R},\ x \mapsto x^2$.
2. $f : \mathbb{R} \to \mathbb{R},\ x \mapsto x^2$.
3. $f : \mathbb{R} \to \mathbb{R}_+,\ x \mapsto x^2$.
4. $f : \mathbb{R}_+ \to \mathbb{R}_+,\ x \mapsto x^2$.

## Exercise 5 (3 points)
Type : équation diophantienne $ax+by=c$ (Euclide, Gauss) · ECUE : HP (arithmétique)
Formules : Euclide : $a = bq + r$, $a \wedge b = b \wedge r$ ; solutions $\iff (a \wedge b) \mid c$ ; diviser par $d = a \wedge b$ ; remonter Euclide : $au_0 + bv_0 = d$ puis multiplier par $c/d$ ; Gauss : $a \mid bc$ et $a \wedge b = 1 \Rightarrow a \mid c$ ; $a(x - x_0) = -b(y - y_0)$ donne $x = x_0 + \frac{b}{d}k$, $y = y_0 - \frac{a}{d}k$, $k \in \mathbb{Z}$ ; vérifier la réciproque

1. Using Euclid's algorithm, determine a particular solution of the equation $524x + 144y = 4$.
2. Using imperatively Gauss's theorem, determine the set of all the ordered pairs $(x,y) \in \mathbb{Z}^2$ such that $524x + 144y = 4$.

## Exercise 6 (2 points)
Type : PGCD et Bézout (démonstration) · ECUE : HP (arithmétique)
Formules : $d \mid a$ et $d \mid b$ : $a = da'$, $b = db'$ ; $a' \wedge b' = 1$ ; Bézout : $a' \wedge b' = 1 \iff \exists (u,v), a'u + b'v = 1$ ; multiplier par $d$

Let $a$ and $b$ be two non-zero natural numbers and $d = a \wedge b$.
1. Show that there exists $(a',b') \in \mathbb{N}^{*2}$ such that $a = da'$, $b = db'$ and $a' \wedge b' = 1$.
2. Using the previous question and Bézout's theorem, show that there exists $(u,v) \in \mathbb{Z}^2$ such that $au + bv = d$.

## Exercise 7 (2 points)
Type : multiplicité d'une racine d'un polynôme · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/4
Formules : $\alpha$ racine d'ordre $m$ $\iff P(\alpha) = P'(\alpha) = \dots = P^{(m-1)}(\alpha) = 0$ et $P^{(m)}(\alpha) \neq 0$ ; $(X^n)' = nX^{n-1}$

Determine the order of multiplicity of the root 1 of the polynomial $P(X) = X^4 - X^3 - 3X^2 + 5X - 2$.

## Exercise 8 (3 points)
Type : divisibilité et reste de division euclidienne de polynômes · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/5
Formules : $A = BQ + R$, $\deg R < \deg B$ ; $(X-a)(X-b) \mid P \iff P(a) = P(b) = 0$ ($a \neq b$) ; reste par $(X-a)(X-b)$ : $R = \alpha X + \beta$ avec $R(a) = P(a)$, $R(b) = P(b)$ ; reste par $(X-a)^2$ : $R(a) = P(a)$, $R'(a) = P'(a)$

Let $n \geqslant 2$.
1. Show that the polynomial $P(X) = (X-2)^{2n} + (X-1)^n - 1$ is divisible by $X^2 - 3X + 2$.
2. Determine the remainder of the euclidean division of $Q(X) = (X-2)^{2n} + (X-1)^n - 2$ by:
   a. $(X-2)(X-1)$;
   b. $(X-1)^2$.

## Exercise 9 (2 points)
Type : racine multiple d'un polynôme à paramètre · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/10
Formules : $\alpha$ racine au moins double $\iff Q(\alpha) = Q'(\alpha) = 0$ ; $((X+1)^7)' = 7(X+1)^6$ ; $(X+1)^6 = X^6 \iff X + 1 = \pm X$

For which value(s) of $a \in \mathbb{R}$ does the polynomial $Q(X) = (X+1)^7 - X^7 - a$ have a real root which is at least of order two?
