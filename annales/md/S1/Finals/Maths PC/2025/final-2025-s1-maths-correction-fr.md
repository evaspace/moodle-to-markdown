# Corrigé du partiel S1 — janvier 2021

- Source : `raw/S1/Finals/Maths PC/2025/final-2025-s1-maths-correction-fr.pdf` (4 pages)
- Date réelle : janvier 2021 (S1 20-21, dossier promo 2025). Sujet : `final-2025-s1-maths-subject-fr.md` (énoncés repris ici en abrégé).

## Exercice 1 (6 points)
Type : dénombrement de mains, probabilités totales et Bayes · ECUE : DP · Niveau : maths-s1-dp/10
Formules : équiprobabilité : $P(A) = \frac{|A|}{|\Omega|}$ ; $|\Omega| = \binom{32}{5}$ ; $\binom nk = \frac{n!}{k!(n-k)!}$ ; partition : $A_i$ deux à deux disjoints et $\bigsqcup A_i = \Omega$ ; probabilités totales : $P(B) = \sum P(B \mid A_i)P(A_i)$ ; Bayes : $P(A \mid B) = \frac{P(B \mid A)P(A)}{P(B)}$

a. Une main de 5 cartes : on choisit 5 cartes parmi 32. Une main avec exactement 3 valets : 3 valets parmi 4 et 2 cartes parmi les 28 autres. Équiprobabilité :
$$P(3V) = \frac{|3V|}{|\Omega|} = \frac{\binom43\binom{28}2}{\binom{32}5}.$$
b. Il faut obligatoirement le valet de pique, puis 2 valets parmi les 3 autres et 2 piques parmi les 7 autres :
$$P(3V3P) = \frac{\binom11\binom32\binom72}{\binom{32}5}.$$
c. $\{V_0, \dots, V_4\}$ partition de $\Omega$ $\iff$ les $V_i$ sont deux à deux disjoints et $V_0 \sqcup V_1 \sqcup V_2 \sqcup V_3 \sqcup V_4 = \Omega$.
d. $P(B_V) = \displaystyle\sum_{k=0}^{4} P(B_V \mid V_k)\,P(V_k)$.
e. $P(V_3 \mid B_V) = \dfrac{P(B_V \mid V_3)\,P(V_3)}{P(B_V)}$.

## Exercice 2 (3 points)
Type : loi binomiale et loi uniforme (espérance, variance) · ECUE : DP · Niveau : maths-s1-dp/14
Formules : $X \sim \mathcal{B}(n,p)$ : $P(X = k) = \binom nk p^k(1-p)^{n-k}$, $E(X) = np$, $V(X) = np(1-p)$ ; uniforme sur $[\![1,n]\!]$ : $P(Y = k) = \frac1n$, $E(Y) = \frac{n+1}2$ ; $\sum_{k=1}^n k = \frac{n(n+1)}2$

1. $E(X) = np = \frac52$, $V(X) = np(1-p) = \frac52 \times \frac34 = \frac{15}8$.
$P(X = 3) = \binom{10}{3}\left(\frac14\right)^3\left(\frac34\right)^7 = \dfrac{10! \times 3^7}{7! \times 3! \times 4^{10}} = \dfrac{10 \times 9 \times 8 \times 3^7}{3 \times 2 \times 4^{10}} = \dfrac{3^8 \times 5}{2^{17}}$.
2. $Y$ uniforme : $\forall n \in [\![1,10]\!]$, $P(Y = n) = \frac1{10}$. $E(Y) = \displaystyle\sum_{n=1}^{10} \frac{n}{10} = \frac1{10} \times \frac{10 \times 11}2 = \frac{11}2$.

## Exercice 3 (3 points)
Type : petit théorème de Fermat, reste d'une puissance · ECUE : HP (arithmétique)
Formules : Fermat : $p$ premier, $p \nmid a \Rightarrow a^{p-1} \equiv 1\,[p]$ ; $a \equiv b\,[n] \Rightarrow a^k \equiv b^k\,[n]$ ; $a^{q(p-1)+r} \equiv a^r\,[p]$

$2021 = 106 \times 19 + 7$ donc $2021 \equiv 7\,[19]$ et $19 \nmid 2021$.
Petit théorème de Fermat : pour $p$ premier et $p \nmid n$, $n^{p-1} \equiv 1\,[p]$. Ainsi $2021^{18} \equiv 1\,[19]$.
$2021^{362} = 2021^{18 \times 20} \times 2021^2 \equiv 7^2 \equiv 11\,[19]$, et $0 \leqslant 11 < 19$ : le reste est 11.

## Exercice 4 (5 points)
Type : équation diophantienne $ax+by=c$ (Euclide, Gauss) · ECUE : HP (arithmétique)
Formules : Euclide : $a = bq + r$, $a \wedge b = b \wedge r$ ; solutions $\iff (a \wedge b) \mid c$ ; diviser par $d = a \wedge b$ ; remonter Euclide : $au_0 + bv_0 = d$ puis multiplier par $c/d$ ; Gauss : $a \mid bc$ et $a \wedge b = 1 \Rightarrow a \mid c$ ; $a(x - x_0) = -b(y - y_0)$ donne $x = x_0 + \frac{b}{d}k$, $y = y_0 - \frac{a}{d}k$, $k \in \mathbb{Z}$ ; vérifier la réciproque

1. $(E)$ est simplifiable par 15 : $(E) \iff 42x - 13y = 2$.
$42 = 3 \times 13 + 3$, $13 = 4 \times 3 + 1$, $3 = 3 \times 1 + 0$, donc $42 \wedge 13 = 1$ et
$1 = 13 - 4 \times 3 = 13 - 4 \times (42 - 3 \times 13) = 13 \times 13 - 4 \times 42$.
$13 \times 13 - 4 \times 42 = 1 \iff 42 \times (-8) - 13 \times (-26) = 2$ : $(-8, -26)$ est une solution particulière.
2. $(E) \iff 42(x + 8) = 13(y + 26)$. Lemme de Gauss : $a \wedge b = 1$ et $a \mid bc \implies a \mid c$.
$42 \wedge 13 = 1$ et $42 \mid 13(y + 26)$ donc $42 \mid y + 26$ : $\exists k \in \mathbb{Z}$, $y = -26 + 42k$, puis $x + 8 = 13k$.
Réciproquement $42(-8 + 13k) - 13(-26 + 42k) = 2$.
$S = \{(-8 + 13k, -26 + 42k) ; k \in \mathbb{Z}\}$.

## Exercice 5 (3 points)
Type : divisibilité de polynômes, multiplicité d'une racine · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/4
Formules : $(X-a)(X-b) \mid P \iff P(a) = P(b) = 0$ ($a \neq b$) ; $\alpha$ racine d'ordre $m$ $\iff P(\alpha) = \dots = P^{(m-1)}(\alpha) = 0$, $P^{(m)}(\alpha) \neq 0$ ; $(X^n)' = nX^{n-1}$

1. $P(1) = n(0 - 1) + (0 - 1) + n + 1 = 0$ et $P(2) = n(1 - 2) + (1 - 2) + (n + 1) = 0$, donc $(X-1)(X-2) \mid P$.
2. $Q(-1) = -(2n+1) + (2n+3) + 0 - 2 = 0$.
$Q'(X) = (2n+3)\left[(2n+1)X^{2n+2} + (2n+2)X^{2n+1} + 1\right]$, $Q'(-1) = (2n+3)\left((2n+1) - (2n+2) + 1\right) = 0$.
$Q''(X) = (2n+3)(2n+2)(2n+1)\left[X^{2n+1} + X^{2n}\right]$, $Q''(-1) = 0$.
$Q^{(3)}(X) = (2n+3)(2n+2)(2n+1)\left[(2n+1)X^{2n} + 2nX^{2n-1}\right]$, $Q^{(3)}(-1) = (2n+3)(2n+2)(2n+1) \neq 0$.
Donc $-1$ est racine de $Q$ de multiplicité exactement 3.

## Exercice 6 (3 points)
Type : factorisation d'un polynôme dans $\mathbb{R}[X]$ · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/6
Formules : $P(a) = 0 \iff X - a \mid P$ ; division euclidienne $A = BQ + R$ ; $\Delta = b^2 - 4ac < 0 \Rightarrow aX^2 + bX + c$ irréductible dans $\mathbb{R}[X]$

1. $R(1) = 1 + 3 + 3 - 1 - 6 = 0$, $R(-2) = 16 - 24 + 12 + 2 - 6 = 0$, donc $(X-1)(X+2) \mid R$.
2. Division euclidienne par $(X-1)(X+2) = X^2 + X - 2$ : $R(X) = (X-1)(X+2)(X^2 + 2X + 3)$.
$\Delta = 4 - 12 = -8 < 0$ : $X^2 + 2X + 3$ est irréductible dans $\mathbb{R}[X]$. Décomposition : $R(X) = (X-1)(X+2)(X^2 + 2X + 3)$.

## Exercice 7 (4 points)
Type : suites adjacentes via une suite géométrique · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/9
Formules : $w_{n+1} = qw_n \Rightarrow w_n = w_0q^n$ ; $|q| < 1 \Rightarrow q^n \to 0$ ; adjacentes : une croissante, l'autre décroissante, différence $\to 0$

1. $w_{n+1} = \dfrac{4u_n + v_n}5 - \dfrac{u_n + 4v_n}5 = \dfrac{3}{5}w_n$ : $(w_n)$ est géométrique de raison $\frac35$, $w_n = \left(\frac35\right)^n$ (car $w_0 = 1$). $w_n > 0$ et, $0 < \frac35 < 1$, $\lim w_n = 0$.
2. $u_{n+1} - u_n = \dfrac{v_n - u_n}5 = -\dfrac{w_n}5 < 0$ : $(u_n)$ décroissante. $v_{n+1} - v_n = \dfrac{w_n}5 > 0$ : $(v_n)$ croissante. $\lim (u_n - v_n) = \lim w_n = 0$. Ainsi $(u_n)$ et $(v_n)$ sont adjacentes.

## Exercice 8 (3 points)
Type : comparaison de suites ($\sim$, $o$, $O$) · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/12
Formules : $u_n \sim v_n \iff \frac{u_n}{v_n} \to 1$ ; $u_n = o(v_n) \iff \frac{u_n}{v_n} \to 0$ ; $u_n = O(v_n) \iff \frac{u_n}{v_n}$ bornée ; convergente $\Rightarrow$ bornée, donc $\sim$ et $o$ impliquent $O$ ; croissances comparées : $\frac{\ln n}{n^a} \to 0$, $\frac{n^a}{e^n} \to 0$ ; $\frac{\sin n}{n} \to 0$ ; factoriser par le terme dominant

1. $\dfrac{u_n}{v_n} = \dfrac{n^2(1 + \frac3n)}{n^2(2 + \frac3{n^2})} \to \frac12$. Toute suite convergente est bornée, donc $u_n = O(v_n)$.
2. $\dfrac{v_n}{u_n} = \dfrac{\sin n}{n} \to 0$ donc $v_n = o(u_n)$ et $v_n = O(u_n)$.
3. $\dfrac{u_n}{v_n} = \dfrac{e^n\left(1 + \frac{\ln n}{e^n} + \frac{n}{e^n}\right)}{e^n\left(1 + \frac{2\ln n}{e^n} + \frac2{e^n}\right)} \to 1$ donc $u_n \sim v_n$ et $u_n = O(v_n)$.
