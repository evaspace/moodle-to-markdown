# Correction du partiel S1 — janvier 2022

- Source : `raw/S1/Finals/Maths PC/2026/final-2026-s1-maths-correction-fr.pdf` (5 pages)
- Date réelle : janvier 2022 (dossier promo 2026). Sujet : `final-2026-s1-maths-subject-fr.md`.

## Exercice 1
Type : équation diophantienne $ax+by=c$ (Euclide, Gauss) · ECUE : HP (arithmétique)
Formules : Euclide : $a = bq + r$, $a \wedge b = b \wedge r$ ; solutions $\iff (a \wedge b) \mid c$ ; diviser par $d = a \wedge b$ ; remonter Euclide : $au_0 + bv_0 = d$ puis multiplier par $c/d$ ; Gauss : $a \mid bc$ et $a \wedge b = 1 \Rightarrow a \mid c$ ; $a(x - x_0) = -b(y - y_0)$ donne $x = x_0 + \frac{b}{d}k$, $y = y_0 - \frac{a}{d}k$, $k \in \mathbb{Z}$ ; vérifier la réciproque

1. Algorithme d'Euclide : $203 = 84 \times 2 + 35$ (3), $84 = 35 \times 2 + 14$ (2), $35 = 14 \times 2 + 7$ (1), $14 = 7 \times 2 + 0$.
$203 \wedge 84 = 7 = 35 - 14 \times 2 = 35 - (84 - 35 \times 2) \times 2 = 35 \times 5 - 84 \times 2 = (203 - 84 \times 2) \times 5 - 84 \times 2 = 203 \times 5 - 84 \times 12$.
Par conséquent $14 = 7 \times 2 = 203 \times 10 - 84 \times 24$ : $(10, 24)$ est une solution particulière de $(E)$.
2. Soit $(x,y)$ solution : $203x - 84y = 203 \times 10 - 84 \times 24$, d'où $203(x - 10) = 84(y - 24)$ $(*)$.
En divisant par $203 \wedge 84 = 7$ : $29(x - 10) = 12(y - 24)$. Ainsi $12 \mid 29(x - 10)$ et $12 \wedge 29 = 1$, d'où par Gauss $12 \mid x - 10$ : $x = 10 + 12k$, $k \in \mathbb{Z}$.
En reportant : $29 \times 12k = 12(y - 24)$, soit $y = 24 + 29k$.
Réciproquement $203(10 + 12k) - 84(24 + 29k) = 14 + 7 \times 29 \times 12k - 7 \times 12 \times 29k = 14$.
$S = \{(10 + 12k, 24 + 29k) ; k \in \mathbb{Z}\}$.

## Exercice 2
Type : congruences et Fermat, divisibilité · ECUE : HP (arithmétique)
Formules : $a \equiv b\,[n] \Rightarrow a^k \equiv b^k\,[n]$ ; Fermat : $p$ premier $\Rightarrow a^p \equiv a\,[p]$ ; $a^{mn+r} = (a^m)^n a^r$ ; $n \mid A \iff A \equiv 0\,[n]$

- $15 \equiv 4\,[11]$ d'où $15^{4n+2} \equiv 4^{4n+2}\,[11]$. Or $4^2 = 16 \equiv 5\,[11]$, d'où $4^4 = (4^2)^2 \equiv 25 \equiv 3\,[11]$. Par conséquent $4^{4n+2} = (4^4)^n \times 4^2 \equiv 3^n \times 5\,[11]$.
- $5^2 = 25 \equiv 3\,[11]$. De plus 11 est premier d'où, par Fermat, $5^{11} \equiv 5\,[11]$. Ainsi $5^{2n+11} = (5^2)^n \times 5^{11} \equiv 3^n \times 5\,[11]$.
- On en déduit $15^{4n+2} - 5^{2n+11} \equiv 0\,[11]$. Donc $11 \mid A_n$.

## Exercice 3
Type : Bézout (énoncé), diviseurs communs et PGCD · ECUE : HP (arithmétique)
Formules : Bézout : $a \wedge b = 1 \iff \exists (u,v), au + bv = 1$ ; corollaire : $\exists (u,v), au + bv = a \wedge b$ ; $d \mid a$ et $d \mid b \Rightarrow d \mid au + bv$ ; transitivité de $\mid$

1. Théorème de Bézout : $a \wedge b = 1 \iff \exists (u,v) \in \mathbb{Z}^2,\ au + bv = 1$. Corollaire : $\forall (a,b) \in (\mathbb{N}^*)^2, \exists (u,v) \in \mathbb{Z}^2,\ au + bv = a \wedge b$.
2. $\Leftarrow$ : si $d \mid a \wedge b$, comme $a \wedge b \mid a$, par transitivité $d \mid a$ ; de même $d \mid b$.
$\Rightarrow$ : si $d \mid a$ et $d \mid b$, alors $\forall (u,v) \in \mathbb{Z}^2$, $d \mid au + bv$. Par Bézout, $\exists (u_0,v_0)$, $a \wedge b = au_0 + bv_0$, donc $d \mid a \wedge b$.

## Exercice 4
Type : suites adjacentes, suites extraites $(u_{2n})$, $(u_{2n+1})$ · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/9
Formules : adjacentes : une croissante, l'autre décroissante, différence $\to 0$ ; $u_{2n+2} - u_{2n}$ = deux termes de la somme ; $\frac1{a^2} - \frac1{b^2} = \frac{(b-a)(b+a)}{a^2b^2}$ ; $(u_{2n})$ et $(u_{2n+1})$ même limite $\Rightarrow (u_n)$ converge

1. $(v_n)$ et $(w_n)$ sont adjacentes si $(v_n)$ est croissante, $(w_n)$ décroissante (ou l'inverse) et $v_n - w_n \to 0$.
2. $v_{n+1} - v_n = u_{2n+2} - u_{2n} = -\dfrac1{(2n+1)^2} + \dfrac1{(2n+2)^2} = \dfrac{-4n-3}{(2n+1)^2(2n+2)^2} \leqslant 0$ : $(v_n)$ décroissante.
$w_{n+1} - w_n = u_{2n+3} - u_{2n+1} = \dfrac1{(2n+2)^2} - \dfrac1{(2n+3)^2} = \dfrac{4n+5}{(2n+2)^2(2n+3)^2} \geqslant 0$ : $(w_n)$ croissante.
$v_n - w_n = u_{2n} - u_{2n+1} = -\dfrac{(-1)^{2n+1}}{(2n+1)^2} = \dfrac1{(2n+1)^2} \to 0$. Les suites $(u_{2n})$ et $(u_{2n+1})$ sont adjacentes.
3. Étant adjacentes, $(u_{2n})$ et $(u_{2n+1})$ convergent vers une même limite $l \in \mathbb{R}$ : $(u_n)$ converge vers $l$.

## Exercice 5
Type : suite récurrente $u_{n+1} = f(u_n)$ · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/10
Formules : constante $\iff u_0 = f(u_0)$ ; tableau de variations via $f'$ ; $f$ croissante sur $I$ et $u_n \in I \Rightarrow f(a) < f(u_n) < f(b)$ (récurrence) ; signe de $u_{n+1} - u_n$ ; monotone bornée $\Rightarrow$ convergente ; $\ell = f(\ell)$

1. $u_{n+1} = u_n \iff \dfrac{-u_n^2 - u_n - 4}4 = u_n \iff u_n^2 + 5u_n + 4 = 0 \iff (u_n + 1)(u_n + 4) = 0$. Pour $u_0 = -1$ ou $u_0 = -4$, la suite est constante.
2. Pour $x \in \mathbb{R}_-$, $f'(x) = \dfrac{-2x - 1}4$. $f$ est croissante sur $]-\infty, -\frac12]$ (de $-\infty$ à $f(-\frac12) = -\frac{15}{16}$, en passant par $f(-4) = -4$ et $f(-1) = -1$), puis décroissante sur $[-\frac12, 0]$ jusqu'à $f(0) = -1$.
3. Récurrence : $u_0 = -2 \in ]-4, -1[$. Si $-4 < u_n < -1$, $f$ étant strictement croissante entre $-4$ et $-1$, $f(-4) < f(u_n) < f(-1)$, soit $-4 < u_{n+1} < -1$. Donc $\forall n$, $u_n \in ]-4, -1[$.
4. $u_{n+1} - u_n = \dfrac{-u_n^2 - 5u_n - 4}4 = -\dfrac{(u_n + 1)(u_n + 4)}4$. Via 3., $u_n + 1 < 0$ et $u_n + 4 > 0$ donc $u_{n+1} - u_n \geqslant 0$ : $(u_n)$ est croissante.
5. Croissante et majorée par $-1$, $(u_n)$ converge vers $l$ avec $l = f(l)$, soit $l = -4$ ou $l = -1$. Comme $u_n \geqslant u_0 = -2$, $l \geqslant -2$ donc $l = -1$.

## Exercice 6
Type : comparaison de suites ($\sim$, $o$, $O$), développements · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/12
Formules : $u_n \sim v_n \iff \frac{u_n}{v_n} \to 1$ ; $o$ : quotient $\to 0$ ; $O$ : quotient borné ; $o(\frac1{n^2}) = \frac{\varepsilon_n}{n^2}$, $\varepsilon_n \to 0$ ; $u_n \sim$ premier terme non nul du développement ; croissances comparées $\frac{\ln n}n \to 0$

1. (a) $\dfrac{u_n}{v_n} = n \times \dfrac{-2 + \frac1{n^2} + \frac3{n^3}}{\frac1{n^2} - 1}$ et la fraction tend vers 2, donc $\dfrac{u_n}{v_n} \to +\infty$ et $\dfrac{v_n}{u_n} \to 0$ : $v_n = o(u_n)$ et aussi $v_n = O(u_n)$.
(b) $\dfrac{u_n}{v_n} = \dfrac{\frac{e^{-n}}{n} - \frac{\ln n}{n} + 1}{1 + \frac1n} \to 1$ (croissances comparées) : $u_n \sim v_n$ et $u_n = O(v_n)$.
2. (a) $o\!\left(\frac1{n^2}\right) = \frac1{n^2}\varepsilon_n$ avec $\lim \varepsilon_n = 0$.
(b) $\dfrac{u_n}{1/n} = 1 - \dfrac1{2n} + \dfrac{\varepsilon_n}n \to 1$, donc $u_n \sim \frac1n$.
(c) $v_n = -\dfrac1{2n^2}(1 - 2\varepsilon_n)$, donc $v_n \sim -\dfrac1{2n^2}$.

## Exercice 7
Type : divisibilité, $24 \mid p^2 - 1$ pour $p$ premier $\geqslant 5$ · ECUE : HP (arithmétique)
Formules : Bézout ; $a \wedge b = 1$, $a \mid c$, $b \mid c \Rightarrow ab \mid c$ ; division euclidienne par 3 : $d = 3q + r$, $r \in \{0,1,2\}$ ; $p^2 - 1 = (p-1)(p+1)$ ; $k(k+1)$ est pair ; $24 = 8 \times 3$, $8 \wedge 3 = 1$

1. (a) Par Bézout, $\exists (u,v)$, $au + bv = 1$, d'où $c = auc + bvc$. Avec $c = ak = bk'$ : $c = aubk' + bvak = ab(uk' + vk)$, donc $ab \mid c$.
(b) Si $a \mid b$, $b = ak$ et $bc = a(kc)$, donc $a \mid bc$. De même si $a \mid c$.
(c) $d = 3q + r$ avec $0 \leqslant r < 3$. Si $r = 0$, $3 \mid d$. Si $r = 1$, $d + 2 = 3(q+1)$. Si $r = 2$, $d + 1 = 3(q+1)$.
2. (a) $p$ premier $\geqslant 5$ est impair, donc $p - 1$ et $p + 1$ sont pairs.
(b) $p - 1 = 2k$, $p + 1 = 2(k+1)$, donc $p^2 - 1 = 4k(k+1)$. L'un de $k$, $k+1$ est pair, donc par 1b) $k(k+1) = 2k'$ et $p^2 - 1 = 8k'$ : $8 \mid p^2 - 1$.
(c) $p$ premier $\geqslant 5$ donc $3 \wedge p = 1$. Par 1c), 3 divise $p - 1$, $p$ ou $p + 1$ ; pas $p$, donc $3 \mid p - 1$ ou $3 \mid p + 1$, et par 1b) $3 \mid p^2 - 1$.
(d) $8 \mid p^2 - 1$, $3 \mid p^2 - 1$ et $8 \wedge 3 = 1$ : par 1a), $24 \mid p^2 - 1$.
