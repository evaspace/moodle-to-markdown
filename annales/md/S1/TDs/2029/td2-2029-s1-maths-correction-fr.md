# Contrôle de cours ECUE ARITH, mathématiques S1 — lundi 25 novembre 2024 (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (pas de corrigé officiel). Sujet : `td2-2029-s1-maths-subject-fr.md` (même dossier). Calculs vérifiés avec sympy. ARITH hors programme 2031.

## Cours 1 : divisibilité et division euclidienne (5 points)
Type : divisibilité et division euclidienne (vrai/faux) · ECUE : HP (arithmétique)
Formules : $a \mid b \iff \exists k \in \mathbb{Z}, b = ka$ ; $a \mid b$ et $b \mid a \Rightarrow a = \pm b$ ; $a \mid b$, $a \mid c \Rightarrow a \mid bu + cv$ ; contre-exemple $2 \mid 4$, $4 \mid 4$, $8 \nmid 4$ ; $a \mid bc \not\Rightarrow a \mid b$ ou $a \mid c$ ($6 \mid 2 \times 3$) ; division euclidienne $0 \leqslant r < |b|$

1. $a$ multiple de $b\iff\exists k\in\mathbb Z,\ a=bk$.
2. $a\in\{-6,-3,-2,-1,1,2,3,6\}$.
3. $\forall a\in\mathbb Z$, il existe un unique $(q,r)\in\mathbb Z\times\mathbb N$ tel que $a=-18q+r$ et $0\le r<18$.
4. (a) Vrai (transitivité) : $b=ak$, $c=bh$ donc $c=a(kh)$. (b) Faux : $a=6$, $b=2$, $c=3$. (c) Vrai : le reste de la division euclidienne de $a$ par $7$ est le seul $n\in[\![0,6]\!]$ avec $7\mid a-n$. (d) Faux : $a=1$, $b=-1$.

## Cours 2 : congruence (6,5 points)
Type : congruences (définition, opérations) · ECUE : HP (arithmétique)
Formules : $a \equiv b\,[n] \iff n \mid a - b$ ; compatibilité avec $+$, $\times$, puissances ; $ab - cd = a(b - d) + d(a - c)$ ; réduire chaque nombre modulo $n$ ; reste dans $[\![0, n-1]\!]$

1. $a\equiv b\ [n]\iff n\mid a-b$.
2. a) $87\equiv2\ [5]$. b) $24\equiv3\ [7]$. c) $-15\equiv3\ [6]$. d) $-13\equiv9\ [11]$.
3. a) $-2a+3c\equiv-2b+3d$. b) $ac\equiv bd$. c) $a^{13}\equiv b^{13}$.
   | $a$ | $-2$ | $1$ | $28$ |
   |---|---|---|---|
   | $b$ | $3$ | $4$ | $14$ |
   | $a\ [6]$ | $4$ | $1$ | $4$ |
   | $b\ [6]$ | $3$ | $4$ | $2$ |
   | $a^3-2b\ [6]$ | $4$ | $5$ | $0$ |
4. (a) Si $p$ est premier : $\forall n\in\mathbb Z,\ n^p\equiv n\ [p]$. Corollaire : si $p\nmid n$, $n^{p-1}\equiv1\ [p]$.
   (b) i. $4^{13}\equiv0\ [11]$. ii. $11\nmid4$ donc $4^{10}\equiv1\ [11]$ et $4^{13}\equiv4^3=64\equiv9\ [11]$ : $9\ne0$, donc $11\nmid4^{13}$.

## Cours 3 : autour de Bézout (6,5 points)
Type : Bézout, Euclide, lemme de Gauss (démonstrations) · ECUE : HP (arithmétique)
Formules : Bézout : $\exists (u,v), au + bv = a \wedge b$ ; $a \wedge b = 1 \iff \exists (u,v), au + bv = 1$ ; Euclide : $a = bq + r$, remonter les divisions ; Gauss : $a \mid bc$, $a \wedge b = 1 \Rightarrow a \mid c$ ; $a \mid c$, $b \mid c$, $a \wedge b = 1 \Rightarrow ab \mid c$

1. Pour $(a,b)\in\mathbb Z^2$ : $\exists(u,v)\in\mathbb Z^2,\ au+bv=a\wedge b$. Pour $a,b$ premiers entre eux : $a\wedge b=1\iff\exists(u,v),\ au+bv=1$.
2. a) Vrai : $a\wedge b$ divise $ac+bd=1$. b) Vrai : $a\wedge d$ divise $a$ et $d$, donc $ac+bd=1$. c) Faux : $a=b=c=d=1$ donnent $\alpha=2$ et $c\wedge d=1\ne2$.
3. Gauss : si $a\mid bc$ et $a\wedge b=1$ alors $a\mid c$. Preuve : $au+bv=1$ donc $c=acu+bcv$, divisible par $a$.

## Cours 4 : nombres premiers et pgcd (2 points)
Type : PGCD par facteurs premiers, Fermat · ECUE : HP (arithmétique)
Formules : décomposition en facteurs premiers ; $a \wedge b = \prod p^{\min}$ ; Fermat : $p$ premier, $p \nmid a \Rightarrow a^{p-1} \equiv 1\,[p]$ ; premier : exactement deux diviseurs positifs

1. $p$ premier : $p\ge2$ et ses seuls diviseurs positifs sont $1$ et $p$.
2. $300=2^2\times3\times5^2$.
3. $a\wedge b=2^2\times3\times5=60$.
