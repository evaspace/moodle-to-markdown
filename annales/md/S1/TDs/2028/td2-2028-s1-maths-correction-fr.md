# Contrôle de cours, mathématiques S1 — lundi 27 novembre 2023 (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (pas de corrigé officiel). Sujet : `td2-2028-s1-maths-subject-fr.md` (même dossier). Calculs vérifiés avec sympy. Les parties ARITH sont hors programme 2031.

## Partie ARITH, cours 1 : divisibilité et division euclidienne (7 points)
Type : divisibilité et division euclidienne (vrai/faux) · ECUE : HP (arithmétique)
Formules : $a \mid b \iff \exists k \in \mathbb{Z}, b = ka$ ; $a \mid b$ et $b \mid a \Rightarrow a = \pm b$ ; $a \mid b$, $a \mid c \Rightarrow a \mid bu + cv$ ; contre-exemple $2 \mid 4$, $4 \mid 4$, $8 \nmid 4$ ; $a \mid bc \not\Rightarrow a \mid b$ ou $a \mid c$ ($6 \mid 2 \times 3$) ; division euclidienne $0 \leqslant r < |b|$

1. $c\mid d\iff\exists k\in\mathbb Z,\ d=ck$.
2. (a) Faux : $a=1$, $b=-1$. (b) Vrai : $b=ak$, $c=ah$ donc $bu+cv=a(ku+hv)$. (c) Faux : $a=c=2$, $b=2$ : $ac=4\nmid2$.
3. (a) Il existe un unique $(q,r)\in\mathbb Z\times\mathbb N$ tel que $a=bq+r$ et $0\le r<|b|$. (b) $1034=148\times7-2=147\times7+5$ : $q=147$, $r=5$.

## Partie ARITH, cours 2 : autour de Bézout (5 points)
Type : Bézout (énoncé et applications) · ECUE : HP (arithmétique)
Formules : Bézout : $\exists (u,v), au + bv = a \wedge b$ ; $a \wedge b = 1 \iff \exists (u,v), au + bv = 1$ ; élever au carré / multiplier une relation de Bézout ; $2 \times (2n+1) \cdot 1 - \dots$ : $1 \cdot (2n+1) - 2 \cdot n = 1$ ; fraction irréductible $\iff$ numérateur et dénominateur premiers entre eux

1. ($\Leftarrow$) Bézout. ($\Rightarrow$) Si $au+bv=1$, $a\wedge b$ divise $au+bv=1$ donc $a\wedge b=1$.
2. Non : ($\Leftarrow$) est vraie (Bézout) mais ($\Rightarrow$) est fausse : $a=1$, $b=0$ donnent $au+bv=3$ avec $u=3$ et $a\wedge b=1\ne3$.

## Partie ARITH, cours 3 : congruence (8 points)
Type : congruences (définition, opérations) · ECUE : HP (arithmétique)
Formules : $a \equiv b\,[n] \iff n \mid a - b$ ; compatibilité avec $+$, $\times$, puissances ; $ab - cd = a(b - d) + d(a - c)$ ; réduire chaque nombre modulo $n$ ; reste dans $[\![0, n-1]\!]$

1. La division euclidienne de $a$ par $n$ donne $a=nq+r$ avec $0\le r\le n-1$, donc $a\equiv r\ [n]$. Unicité : si $r,r'$ conviennent, $n\mid r-r'$ avec $|r-r'|<n$, donc $r=r'$.
2. (i) $a\equiv b\ [n]\iff n\mid a-b$. (ii) $a+c\equiv b+d$. (iii) $ac\equiv bd$. (iv) $a^k\equiv b^k$.
3. (a) $224=11\times20+4$ : $a\equiv4$. $85=11\times7+8$ : $c\equiv8$. (b) $a+c\equiv12\equiv1$ ; $2a-c\equiv8-8=0$ ; $ac\equiv32\equiv10$ ; $a^3\equiv64\equiv9$.

## Partie ASI, cours 1 : définitions (5 points)
Type : définitions sur les suites, exemples, limite de $q^n$ · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/3
Formules : croissante $\forall n, u_n \leqslant u_{n+1}$ ; bornée $\exists M, \forall n, |u_n| \leqslant M$ ; exemples $(-1)^n$, $1 - \frac1n$, $\cos n$ ; $(q^n)$ converge $\iff -1 < q \leqslant 1$ (limite 0 si $|q| < 1$, 1 si $q = 1$)

1. (a) $\exists M\in\mathbb R,\ \forall n\in\mathbb N,\ |u_n|\le M$. (b) $u_n=\dfrac1{n+1}$.
2. (a) $\forall n\in\mathbb N,\ u_{n+1}\ge u_n$. (b) $(u_n)$ est croissante ou décroissante. (c) $u_n=(-1)^n$.

## Partie ASI, cours 2 : convergence ou divergence (5 points)
Type : limites usuelles de suites · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/4
Formules : $\cos n$ diverge (suites extraites) ; $\ln(n^2 + n) \to +\infty$ ; $|q| < 1 \Rightarrow q^n \to 0$ ; $\frac1n \to 0$

1. $(\cos n)$ diverge. Si $\cos n\to\ell$, alors $\cos(n+1)+\cos(n-1)=2\cos n\cos1$ donne $2\ell=2\ell\cos1$, donc $\ell=0$. Or $\cos(n+1)=\cos n\cos1-\sin n\sin1$ donne $\sin n=\dfrac{\cos n\cos1-\cos(n+1)}{\sin1}\to0$. Alors $\cos^2n+\sin^2n\to0\ne1$ : contradiction.
2. $n^2+n\to+\infty$ donc $v_n=\ln(n^2+n)\to+\infty$ : divergente (limite infinie).
3. $|q|=\frac23<1$ : $w_n\to0$, convergente.
4. $x_n\to1$ : convergente.
5. $u_n=2+\dfrac1n$.
