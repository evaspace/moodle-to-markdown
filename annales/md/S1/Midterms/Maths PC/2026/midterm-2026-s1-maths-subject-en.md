# Midterm exam S1 — November 2021 (subject, EN)

- Source : `raw/S1/Midterms/Maths PC/2026/midterm-2026-s1-maths-subject-en.pdf` (9 pages)
- Date réelle : novembre 2021 (dossier promo 2026). Version anglaise de `midterm-2026-s1-maths-subject-fr.md` ; corrigé : `midterm-2026-s1-maths-correction-fr.md`.
- Duration: 3 hours. Marked out of 30, re-scaled to 20. Documents and pocket calculators are not allowed.

## Exercise 1 (3 points)
Type : relation d'ordre · ECUE : OBM · Niveau : maths-s1-obm/11
Formules : ordre = réflexive ($\forall x, x\mathcal Rx$), antisymétrique ($x\mathcal Ry$ et $y\mathcal Rx \Rightarrow x = y$), transitive ($x\mathcal Ry$ et $y\mathcal Rz \Rightarrow x\mathcal Rz$) ; contre-exemple pour réfuter ; $x^2 = y^2 \iff x = \pm y$

Consider the relation defined on $\mathbb{R}$ by: $\forall (x,y) \in \mathbb{R}^2$, $x\,\mathcal{R}\,y \iff x^2 \leqslant y^2$.
Enumerate the different properties (with the quantifiers) which define an order relation. For each property, say whether it is satisfied or not by the relation defined above. Justify your answer.

## Exercise 2 (3 points)
Type : traduire avec quantificateurs · ECUE : OBM · Niveau : maths-s1-obm/4
Formules : « tout » $= \forall$, « il existe » $= \exists$, « aucun » $= \forall \dots \neg$ ; l'ordre $\forall\exists$ / $\exists\forall$ change le sens ; $f$ s'annule : $\exists x, f(x) = 0$ ; minimum en $a$ : $\exists a, \forall x, f(x) \geqslant f(a)$ ; pair : $\exists k, n = 2k$

Express in mathematical language, with the quantifiers, the following properties.
1. Every positive real number is the square of a real number.
2. If the product of two real numbers is zero, then at least one of these two numbers is zero.
3. Every natural number is even or odd. (Using the congruence relation is not allowed.)

## Exercise 3 (4,5 points)
Type : primitive directe $u'u^\alpha$, IPP, changement de variable affine vers arctan · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/13
Formules : $\int u'u^\alpha = \frac{u^{\alpha+1}}{\alpha+1}$ ($\alpha = \frac12$ : $\frac23u^{3/2}$) ; IPP $\int uv' = [uv] - \int u'v$ ; $\int e^{2x} = \frac{e^{2x}}2$ ; $x = 2t + 1$, $dx = 2\,dt$, bornes transformées ; $\int \frac{dt}{1 + t^2} = \arctan t$ ; $\arctan\sqrt3 = \frac\pi3$

1. Using a primitive (anti-derivative), compute $I = \displaystyle\int_0^1 (x^2 + 1)\sqrt{x^3 + 3x + 1}\,dx$.
2. Using an integration by parts, compute $J = \displaystyle\int_0^1 (2x + 1)e^{2x}\,dx$.
3. Using the substitution $x = 2t + 1$, compute $K = \displaystyle\int_1^{2\sqrt3 + 1} \frac{dx}{(x - 1)^2 + 4}$.

## Exercise 4 (3,5 points)
Type : injectivité, surjectivité, image directe et réciproque · ECUE : OBM · Niveau : maths-s1-obm/10
Formules : injective : $f(x) = f(y) \Rightarrow x = y$ (contre-exemple $f(1) = f(2)$) ; surjective : $\forall y, \exists x, f(x) = y$ ; $f(A) = \{f(x), x \in A\}$ ; $f^{-1}(B) = \{x, f(x) \in B\}$ (peut être vide)

Consider $f : \mathbb{N} \to \mathbb{N}$ defined by $f(n) = \frac n2$ if $n$ is even and $f(n) = n$ otherwise.
1. Is $f$ injective? Justify.
2. Is $f$ surjective? Justify.
3. In this question, the domain of $f$ is restricted to $E = \{0, 1, 2, 3, 4, 5, 6\}$. Give $f(\{0, 1, 2, 3\})$, $f^{-1}(\{1, 3\})$ and $f^{-1}(\{4\})$.

## Exercise 5 (5 points)
Type : combinaisons, formule de Pascal · ECUE : DP · Niveau : maths-s1-dp/6
Formules : tirage simultané : $\binom nk$ ; contenant un élément fixé : $\binom{n-1}{k-1}$ ; ne le contenant pas : $\binom{n-1}k$ ; Pascal : $\binom{n-1}{k-1} + \binom{n-1}{k} = \binom nk$ ; $\binom nk = \frac{n!}{k!(n-k)!}$ ; mettre au même dénominateur $k!(n-k)!$

An urn contains $n$ balls, indistinguishable to the touch and numbered from 1 to $n$. For a natural number $k \leqslant n$, $k$ balls are drawn simultaneously from the urn.
1. What is the number of possible draws? Justify briefly.
2. What is the number of draws containing the ball numbered 1? Justify briefly.
3. What is the number of draws not containing the ball numbered 1? Justify briefly.
4. Explain how the previous results prove the formula $(P)$: $\dbinom{n-1}{k-1} + \dbinom{n-1}{k} = \dbinom nk$.
5. Prove formula $(P)$ again using the expression of binomial coefficients with factorials.

## Exercise 6 (5 points)
Type : loi de Bernoulli, loi binomiale, espérance et variance · ECUE : DP · Niveau : maths-s1-dp/14
Formules : Bernoulli $\mathcal{B}(p)$ : $E = p$, $V = p(1-p)$ ; binomiale $\mathcal{B}(n,p)$ : $P(Y = k) = \binom nk p^k(1-p)^{n-k}$, $E = np$, $V = np(1-p)$ ; $E(G) = \sum x_iP(G = x_i)$ ; $V(G) = E(G^2) - E(G)^2$ (König-Huygens)

We have a fair six-sided die numbered from 1 to 6.
1. Propose a simple experiment giving a random variable $X$ following a Bernoulli distribution with parameter $p = \frac16$. Recall the expectation and the variance of $X$ in terms of $p$.
2. Propose a simple experiment giving a random variable $Y$ following a binomial distribution with parameters $n = 10$ and $p = \frac16$. Recall the expectation and the variance of $Y$ in terms of $n$ and $p$.
3. The die is rolled once. You win 5 points if the die shows a multiple of 3, 3 points if it shows 1 or 2, and zero points otherwise. Let $G$ be the number of points won. Give the distribution of $G$ and compute its expectation and variance.

## Exercise 7 (4 points)
Type : probabilités totales et Bayes · ECUE : DP · Niveau : maths-s1-dp/10
Formules : probabilités totales : $P(M) = P(M \mid V)P(V) + P(M \mid \bar V)P(\bar V)$ ; Bayes : $P(V \mid M) = \frac{P(M \mid V)P(V)}{P(M)}$ ; $P(\bar V) = 1 - P(V)$

A virus affects people all over the world. Screening tests are sold; the instructions state that:
- if a person is not ill, the test is reliable in 80 % of cases;
- if a person is ill, the test is reliable in 99 % of cases.
The virus affects 25 % of the French population. A person is chosen at random and tested. Let $M$: « the person is ill » and $T$: « the test is positive ».
1. Give a partition of the event $T$ in terms of $M$. Give the literal formula computing $P(T)$ and the numerical value of each probability appearing in it (without finishing the computation).
2. Explain how to compute the probability that a person is ill given that the test is positive (the final value is not required).

## Exercise 8 (2 points)
Type : récurrence (somme géométrique) · ECUE : OBM · Niveau : maths-s1-obm/7
Formules : récurrence ; $S_{n+1} = S_n + q^{n+1}$ ; $\sum_{k=0}^n q^k = \frac{1 - q^{n+1}}{1 - q}$ ($q \neq 1$), $= n + 1$ si $q = 1$

Let $q \in \mathbb{R}$. For all $n \in \mathbb{N}$, consider $S_n = \displaystyle\sum_{k=0}^n q^k = q^0 + q^1 + \dots + q^n$.
1. What is $S_n$ when $q = 1$?
2. Assume $q \neq 1$. Prove by induction that for all $n \in \mathbb{N}$, $S_n = \dfrac{1 - q^{n+1}}{1 - q}$.
