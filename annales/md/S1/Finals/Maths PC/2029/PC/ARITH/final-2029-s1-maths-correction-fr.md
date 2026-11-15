# Examen S1B2-ARITH — janvier 2025 (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (pas de corrigé officiel). Sujet : `final-2029-s1-maths-subject-fr.md` (même dossier). Calculs vérifiés avec sympy. Hors programme 2031 (arithmétique).

## Exercice 1 : autour des nombres premiers (7 points)
Type : décomposition en facteurs premiers, diviseurs communs · ECUE : HP (arithmétique)
Formules : $a \wedge b = \prod p^{\min(\alpha_p, \beta_p)}$ ; $d \mid a$ et $d \mid b \iff d \mid a \wedge b$ (Bézout) ; diviseurs de $\prod p_i^{\gamma_i}$ : $\prod p_i^{\delta_i}$, $0 \leqslant \delta_i \leqslant \gamma_i$ ; nombre : $\prod(\gamma_i + 1)$

1. $3960=2^3\times3^2\times5\times11$.
2. On prend le minimum de chaque exposant : $a\wedge b=2^2\times3\times5=60$.
3. (a) Si $d\mid a$ et $d\mid b$ : Bézout donne $u,v$ avec $au+bv=a\wedge b$, donc $d\mid a\wedge b$. Réciproquement $a\wedge b$ divise $a$ et $b$, donc $d\mid a\wedge b$ implique $d\mid a$ et $d\mid b$.
   (b) Les diviseurs communs sont les diviseurs de $60$ : $d=2^\alpha3^\beta5^\gamma$ avec $0\le\alpha\le2$, $0\le\beta\le1$, $0\le\gamma\le1$.
   (c) $1,2,3,4,5,6,10,12,15,20,30,60$ : $12$ diviseurs, et $(2+1)(1+1)(1+1)=12$.

## Exercice 2 : équation diophantienne (6 points)
Type : équation diophantienne $ax+by=c$ (Euclide, Gauss) · ECUE : HP (arithmétique)
Formules : Euclide : $a = bq + r$, $a \wedge b = b \wedge r$ ; solutions $\iff (a \wedge b) \mid c$ ; diviser par $d = a \wedge b$ ; remonter Euclide : $au_0 + bv_0 = d$ puis multiplier par $c/d$ ; Gauss : $a \mid bc$ et $a \wedge b = 1 \Rightarrow a \mid c$ ; $a(x - x_0) = -b(y - y_0)$ donne $x = x_0 + \frac{b}{d}k$, $y = y_0 - \frac{a}{d}k$, $k \in \mathbb{Z}$ ; vérifier la réciproque

1. $29=2\cdot13+3$, $13=4\cdot3+1$, $3=3\cdot1$ : $29\wedge13=1$, qui divise $3$ : $(E)$ a des solutions.
2. $1=13-4\cdot3=13-4(29-2\cdot13)=9\cdot13-4\cdot29$. Multiplié par $3$ : $3=27\cdot13-12\cdot29$ : $(x_0,y_0)=(-12,27)$.
3. $29x+13y=3=29x_0+13y_0$ donne $29(x-x_0)=-13(y-y_0)$. Donc $13\mid29(x-x_0)$ et $13\wedge29=1$ : Gauss donne $13\mid x-x_0$, $x=x_0+13k$. Alors $29\cdot13k=-13(y-y_0)$ et $y=y_0-29k$.
4. $29(x_0+13k)+13(y_0-29k)=29x_0+13y_0+(29\cdot13-13\cdot29)k=3$.
5. $S=\{(-12+13k,\ 27-29k),\ k\in\mathbb Z\}$.

## Exercice 3 : autour du cours et de Bézout (6 points)
Type : Bézout (énoncé et applications) · ECUE : HP (arithmétique)
Formules : Bézout : $\exists (u,v), au + bv = a \wedge b$ ; $a \wedge b = 1 \iff \exists (u,v), au + bv = 1$ ; élever au carré / multiplier une relation de Bézout ; $2 \times (2n+1) \cdot 1 - \dots$ : $1 \cdot (2n+1) - 2 \cdot n = 1$ ; fraction irréductible $\iff$ numérateur et dénominateur premiers entre eux

1. Pour $a,b\in\mathbb Z$ : il existe $(u,v)\in\mathbb Z^2$ tel que $au+bv=a\wedge b$. Pour $a,b$ premiers entre eux : $a\wedge b=1\iff\exists(u,v)\in\mathbb Z^2,\ au+bv=1$.
2. Si $a\wedge b=1$ : $au+bv=1$, donc $bv=1-au$, et $b^2v^2=(1-au)^2=1-a(2u-au^2)$. Donc $a(2u-au^2)+b^2v^2=1$ : $a\wedge b^2=1$. Réciproquement, si $au+b^2v=1$, alors $au+b(bv)=1$ : $a\wedge b=1$.
3. $(2n+1)\cdot1+n\cdot(-2)=1$ : relation de Bézout, donc $n\wedge(2n+1)=1$ et la fraction est irréductible.

## Exercice 4 : autour du cours et de Fermat (7 points)
Type : petit théorème de Fermat (énoncé, démonstration, application) · ECUE : HP (arithmétique)
Formules : Fermat : $p$ premier $\Rightarrow \forall n, n^p \equiv n\,[p]$ ; si $p \nmid n$, $n^{p-1} \equiv 1\,[p]$ ; binôme $(n+1)^p = \sum_k \binom pk n^k$ et $p \mid \binom pk$ pour $1 \leqslant k \leqslant p-1$ (récurrence) ; Gauss pour simplifier par $n$ ; $a^{6q+r} \equiv a^r\,[7]$

1. Énoncé : $p$ premier, alors $\forall n\in\mathbb N,\ n^p\equiv n\ [p]$. Récurrence : $n=0$ : $0\equiv0$. Si $n^p\equiv n$, alors $(n+1)^p=\sum_{k=0}^p\binom pkn^k\equiv n^p+1\ [p]$ (les $\binom pk$, $1\le k\le p-1$, sont divisibles par $p$), donc $(n+1)^p\equiv n+1\ [p]$.
2. Énoncé : $p$ premier ne divisant pas $n$ : $n^{p-1}\equiv1\ [p]$. Preuve : $n^p\equiv n$ donc $p\mid n(n^{p-1}-1)$ ; $p\wedge n=1$ donc par Gauss $p\mid n^{p-1}-1$.
3. Modulo $7$ : $12\equiv5$ et $5^6\equiv1$ (Fermat). $43=6\times7+1$ donc $12^{43}\equiv5^{43}\equiv5$. $11\equiv4$ donc $11\times12^{43}\equiv20\equiv6$. $128=7\times18+2$ donc $128\equiv2$. $N\equiv6-2=4\ [7]$ : le reste est $4$.

## Exercice 5 : congruence (4 points)
Type : congruences modulo $n$, équation sans solution · ECUE : HP (arithmétique)
Formules : $a \equiv b\,[n] \Rightarrow a^2 \equiv b^2\,[n]$ ; $11 \equiv 1$, $7 \equiv 2\,[5]$ ; table des carrés modulo 5 : $0, 1, 4, 4, 1$ ; $x = 5k \Rightarrow x^2 = 25k^2$ ; $25 \mid$ membre de gauche mais $25 \nmid 5$

1. Modulo $5$ : $11\equiv1$ et $7\equiv2$, donc $x^2-2y^2\equiv5\equiv0$, soit $x^2\equiv2y^2\ [5]$.
2. | $x$ | 0 | 1 | 2 | 3 | 4 |
   |---|---|---|---|---|---|
   | $x^2$ | 0 | 1 | 4 | 4 | 1 |
   | $y$ | 0 | 1 | 2 | 3 | 4 |
   | $2y^2$ | 0 | 2 | 3 | 3 | 2 |
3. $x^2\in\{0,1,4\}$ et $2y^2\in\{0,2,3\}$ : seule valeur commune $0$. Donc $x^2\equiv0$ et $2y^2\equiv0$ : $x\equiv0$ et $y\equiv0\ [5]$.
4. Supposons $\exists(a,b)\in\mathbb Z^2,\ x=5a,\ y=5b$ et $11x^2-7y^2=5$. Alors $25(11a^2-7b^2)=5$ : $25\mid5$, absurde.
5. D'après 3 et 4, il n'y a pas de solution : $S=\emptyset$.
