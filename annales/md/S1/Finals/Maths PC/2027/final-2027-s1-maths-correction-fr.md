# Correction du partiel S1 — janvier 2023

- Source : `raw/S1/Finals/Maths PC/2027/final-2027-s1-maths-correction-fr.pdf` (5 pages)
- Date réelle : janvier 2023 (dossier promo 2027). Sujet : `final-2027-s1-maths-subject-fr.md`.

## Exercice 1 : encore des intégrales
Type : intégrale par primitive directe ($u'u^\alpha$, $u'/u$) · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/5
Formules : $\int u'u^\alpha = \frac{u^{\alpha+1}}{\alpha+1}$ ($\alpha \neq -1$) ; $\int \frac{u'}u = \ln|u|$ ; $\sqrt x = x^{1/2}$ ; $x\sqrt x = x^{3/2}$ ; $\ln 8 = 3\ln 2$

1. $I = \displaystyle\int_1^2 (x-1)^{3/2}\,dx = \left[\frac{(x-1)^{5/2}}{5/2}\right]_1^2 = \frac25\left(1^{5/2} - 0\right) = \frac25$.
2. $J = \dfrac13\displaystyle\int_0^1 \frac{3x^2 + 6}{x^3 + 6x + 1}\,dx = \frac13\left[\ln|x^3 + 6x + 1|\right]_0^1 = \frac13(\ln 8 - \ln 1) = \frac{3\ln 2}{3} = \ln 2$.

## Exercice 2 : cours sur les polynômes
Type : degré, division euclidienne de polynômes, racine · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/2
Formules : $\deg(A+B) \leqslant \max(\deg A, \deg B)$ ; $\deg(AB) = \deg A + \deg B$ ; $\exists!\,(Q,R)$, $A = BQ + R$, $\deg R < \deg B$ ; $\alpha$ racine $\iff A(\alpha) = 0 \iff X - \alpha \mid A$

1. $\deg(A + B) \leqslant \max(\deg A, \deg B)$ et $\deg(AB) = \deg A + \deg B$.
2. $\exists!\,(Q,R) \in (\mathbb{R}[X])^2$ tel que $A = BQ + R$ et $\deg R < \deg B$.
3. $2X^4 + X - 3 = (X^2 - X + 1)(2X^2 + 2X) - X - 3$ : quotient $2X^2 + 2X$, reste $-X - 3$.
4. $\alpha$ racine de $A \iff A(\alpha) = 0$. Exemple : $A = (X - 42)(X^2 + X + 1)$.

## Exercice 3 : nombres complexes
Type : équation dans $\mathbb{C}$, forme exponentielle · ECUE : HP (nombres complexes, hors programme 2031)
Formules : $AB = 0 \iff A = 0$ ou $B = 0$ ; $\Delta < 0$ : $z = \frac{-b \pm i\sqrt{-\Delta}}{2a}$ ; $z = |z|e^{i\theta}$, $|a + ib| = \sqrt{a^2 + b^2}$, $\cos\theta = \frac{a}{|z|}$, $\sin\theta = \frac{b}{|z|}$

1. $(E) \iff z + \sqrt3 - i = 0$ ou $z^2 - 2z + 2 = 0$. $z = -\sqrt3 + i$. Pour $z^2 - 2z + 2 = 0$, $\Delta = -4$, $z_1 = \frac{2 + 2i}2 = 1 + i$, $z_2 = \overline{z_1} = 1 - i$.
$S = \{-\sqrt3 + i, 1 + i, 1 - i\}$.
2. $-\sqrt3 + i = 2\left(-\frac{\sqrt3}2 + \frac12 i\right) = 2e^{i\frac{5\pi}6}$, $1 + i = \sqrt2\left(\frac{\sqrt2}2 + i\frac{\sqrt2}2\right) = \sqrt2 e^{i\frac\pi4}$, $1 - i = \sqrt2 e^{-i\frac\pi4}$.

## Exercice 4 : arithmétique
Type : inverse modulo un premier, Bézout, Gauss, Fermat · ECUE : HP (arithmétique)
Formules : $p$ premier : $p \wedge a \in \{1, p\}$ ; Bézout : $a \wedge p = 1 \iff \exists (b,v), ab + pv = 1$ ; Gauss ; $ab \equiv 0\,[p] \Rightarrow a \equiv 0$ ou $b \equiv 0\,[p]$ ; $a^2 - 1 = (a-1)(a+1)$ ; Fermat : $p \nmid a \Rightarrow a^{p-1} \equiv 1\,[p]$

1. (a) $p \wedge a \mid p$ et $p$ premier, donc $p \wedge a = 1$ ou $p \wedge a = p$ ; dans ce dernier cas, $p \wedge a \mid a$ donne $p \mid a$.
(b) Bézout : $p \wedge a = 1 \iff \exists (b,v) \in \mathbb{Z}^2, ab + pv = 1 \iff \exists b \in \mathbb{Z}, ab \equiv 1\,[p]$.
2. (a) $47 = 23 \times 2 + 1$ donc $23 \times (-2) + 47 \times 1 = 1$ : $(x_0, y_0) = (-2, 1)$.
(b) $23(x - x_0) = 47(y_0 - y)$ $(\star)$. $47 \mid 23(x - x_0)$ et $47 \wedge 23 = 1$, donc par Gauss $x = -2 + 47k$ ; en reportant, $y = 1 - 23k$. Réciproquement $23(-2 + 47k) + 47(1 - 23k) = 1$. $S_1 = \{(-2 + 47k, 1 - 23k), k \in \mathbb{Z}\}$.
(c) $23x \equiv 1\,[47] \iff \exists y \in \mathbb{Z}, 23x + 47y = 1$, donc $S = \{-2 + 47k, k \in \mathbb{Z}\}$ : les entiers congrus à $-2$ modulo 47. Dans $[\![1,46]\!]$, seule solution : $x = 45$.
3. (a) $\Leftarrow$ évident. $\Rightarrow$ : $47 \mid ab$ ; par 1.(a), soit $47 \mid a$, soit $47 \wedge a = 1$ et par Gauss $47 \mid b$.
(b) $\Leftarrow$ : $1^2 \equiv (-1)^2 \equiv 1$. $\Rightarrow$ : $(a-1)(a+1) \equiv 0\,[47]$ donc par (a) $a \equiv 1$ ou $a \equiv -1\,[47]$.
(c) Dans $[\![1,46]\!]$ : $a = 1$ et $a = 46$.
(d) $a^{46k} = (a^{46})^k$. $47 \nmid a$ et 47 premier : par Fermat $a^{46} \equiv 1\,[47]$, donc $a^{46k} \equiv 1\,[47]$. Le reste est 1.

## Exercice 5 : suites 1
Type : comparaison de suites ($\sim$, $o$, $O$) · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/12
Formules : $u_n \sim v_n \iff \frac{u_n}{v_n} \to 1$ ; $u_n = o(v_n) \iff \frac{u_n}{v_n} \to 0$ ; $u_n = O(v_n) \iff \frac{u_n}{v_n}$ bornée ; convergente $\Rightarrow$ bornée, donc $\sim$ et $o$ impliquent $O$ ; croissances comparées : $\frac{\ln n}{n^a} \to 0$, $\frac{n^a}{e^n} \to 0$ ; $\frac{\sin n}{n} \to 0$ ; factoriser par le terme dominant

1. $u_n \sim v_n \iff \lim \frac{u_n}{v_n} = 1$ ; $u_n = o(v_n) \iff \lim \frac{u_n}{v_n} = 0$ ; $u_n = O(v_n) \iff \left(\frac{u_n}{v_n}\right)$ bornée.
Ou : $u_n = v_n(1 + \varepsilon_n)$ avec $\varepsilon_n \to 0$ ; $u_n = v_n\varepsilon_n$ avec $\varepsilon_n \to 0$ ; $u_n = v_n b_n$ avec $(b_n)$ bornée.
2. (a) $\dfrac{u_n}{v_n} = \dfrac{n^2(1 + \frac1{n^2})}{e^n(1 - \frac{n}{e^n})} \to 0$ (croissances comparées) : $u_n = o(v_n)$ et $u_n = O(v_n)$.
(b) $\dfrac{u_n}{v_n} = \dfrac{1 - \frac1n + \frac1{n^2}}{1 - \frac1{n^2}} \to 1$ : $u_n \sim v_n$ et $u_n = O(v_n)$.
3. $u_n = -\dfrac1{2n} + \dfrac1n\varepsilon_n$ avec $\varepsilon_n \to 0$, donc $\dfrac{u_n}{-1/(2n)} = 1 - 2\varepsilon_n \to 1$ : $u_n \sim -\dfrac1{2n}$.

## Exercice 6 : suites 2
Type : suite récurrente $u_{n+1} = f(u_n)$ · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/10
Formules : constante $\iff u_0 = f(u_0)$ ; tableau de variations via $f'$ ; $f$ croissante sur $I$ et $u_n \in I \Rightarrow f(a) < f(u_n) < f(b)$ (récurrence) ; signe de $u_{n+1} - u_n$ ; monotone bornée $\Rightarrow$ convergente ; $\ell = f(\ell)$

1. $u_{n+1} = u_n \iff u_n^2 - 2u_n - 8 = 0 \iff (u_n - 4)(u_n + 2) = 0$ : constante pour $u_0 = 4$ ou $u_0 = -2$.
2. $f'(x) = \dfrac{2x + 6}8$, nulle en $-3$. $f$ décroît de $+\infty$ à $f(-3) = -\frac{17}8$ sur $]-\infty, -3]$, puis croît jusqu'à $+\infty$, avec $f(-2) = -2$ et $f(4) = 4$.
3. Récurrence : si $-2 < u_n < 4$, $f$ strictement croissante sur $[-2, 4]$ donne $-2 = f(-2) < u_{n+1} < f(4) = 4$.
4. $u_{n+1} - u_n = \dfrac{u_n^2 - 2u_n - 8}8 = \dfrac{(u_n - 4)(u_n + 2)}8 \leqslant 0$ : $(u_n)$ décroissante.
5. Décroissante et minorée par $-2$, elle converge vers $l$ avec $l = f(l)$, donc $l \in \{-2, 4\}$ ; $l \leqslant u_0 < 4$ donc $l = -2$.

## Exercice 7 : une démonstration
Type : démonstration de cours (convergente implique bornée) · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/13
Formules : $u_n \to \ell$ : $\forall \varepsilon > 0, \exists N, \forall n \geqslant N, |u_n - \ell| < \varepsilon$ ; bornée : $\exists M, \forall n, |u_n| \leqslant M$ ; inégalité triangulaire $|u_n| \leqslant |u_n - \ell| + |\ell|$ ; $M = \max(|u_0|, \dots, |u_{N-1}|, 1 + |\ell|)$ ; contre-exemple $(-1)^n$

1. $\forall \varepsilon > 0, \exists N \in \mathbb{N}, \forall n \in \mathbb{N}, n \geqslant N \implies |u_n - l| < \varepsilon$.
2. $\exists M \in \mathbb{R}, \forall n \in \mathbb{N}, |u_n| \leqslant M$.
3. Soit $\ell$ la limite. Pour $\varepsilon = 1$, il existe $N$ tel que $\forall n \geqslant N$, $|u_n - \ell| < 1$, d'où $|u_n| \leqslant |u_n - \ell| + |\ell| < 1 + |\ell|$. Avec $M = \max(|u_0|, \dots, |u_{N-1}|, 1 + |\ell|)$, $\forall n$, $|u_n| \leqslant M$.
4. $((-1)^n)$ est bornée par 1 mais diverge.

## Exercice 8 : exercice original
Type : suites extraites et gendarmes · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/11
Formules : gendarmes : $a_n \leqslant u_n \leqslant b_n$, $a_n, b_n \to \ell \Rightarrow u_n \to \ell$ ; $(u_{2n})$ et $(u_{2n+1})$ même limite $\Rightarrow (u_n)$ converge vers cette limite

- $p = q = n$ : $0 \leqslant u_{2n} \leqslant \dfrac{2n}{n^2} = \dfrac2n \to 0$, donc par les gendarmes $(u_{2n})$ converge vers 0.
- $p = n$, $q = n + 1$ : $0 \leqslant u_{2n+1} \leqslant \dfrac{2n+1}{n(n+1)} = \dfrac{2 + \frac1n}{n(1 + \frac1n)} \to 0$, donc $(u_{2n+1})$ converge vers 0.
- $(u_{2n})$ et $(u_{2n+1})$ convergent vers la même limite 0, donc $(u_n)$ converge vers 0.
