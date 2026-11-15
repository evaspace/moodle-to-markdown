# Contrôle de cours 2, mathématiques S1 — lundi 5 décembre 2022 (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (pas de corrigé officiel). Sujet : `td2-2027-s1-maths-subject-fr.md` (même dossier). Calculs vérifiés avec sympy. Exercices 1 à 4 (arithmétique) hors programme 2031.

## Exercice 1 : divisibilité et division euclidienne (3,5 points)
Type : division euclidienne dans $\mathbb{Z}$ · ECUE : HP (arithmétique)
Formules : $\exists!\,(q, r)$, $a = bq + r$, $0 \leqslant r < |b|$ ; ajuster : $a = bq + r = b(q+1) + (r - b)$ ; pour $-a$ : $-a = b(-q) - r = b(-q-1) + (b - r)$

1. (a) $n\mid m\iff\exists k\in\mathbb Z,\ m=nk$. (b) Diviseurs de $4$ dans $\mathbb Z$ : $\pm1,\pm2,\pm4$.
2. (a) Pour $n\in\mathbb Z$, $m\in\mathbb Z^*$ : il existe un unique couple $(q,r)\in\mathbb Z\times\mathbb N$ tel que $n=mq+r$ et $0\le r<|m|$.
   (b) (i) $-358=21\times(-18)+20$ avec $0\le20<21$ : $q_1=-18$, $r_1=20$. (ii) $r=20\ge|-18|$ n'est pas admissible : $20=18+2$ donc $-358=(-18)\times(21-1)+2=(-18)\times20+2$ avec $0\le2<18$ : $q_2=20$, $r_2=2$.

## Exercice 2 : congruence (5 points)
Type : congruences (définition, opérations) · ECUE : HP (arithmétique)
Formules : $a \equiv b\,[n] \iff n \mid a - b$ ; compatibilité avec $+$, $\times$, puissances ; $ab - cd = a(b - d) + d(a - c)$ ; réduire chaque nombre modulo $n$ ; reste dans $[\![0, n-1]\!]$

1. $a\equiv b\ [n]\iff n\mid a-b$.
2. $ab-cd=a(b-d)+d(a-c)$ est divisible par $n$ comme somme de multiples de $n$ : $ab\equiv cd\ [n]$.
3. $a+b\equiv c+d\ [n]$ et $a^8\equiv c^8\ [n]$.
4. $24\equiv3$ donc $24^3\equiv27\equiv6\ [7]$ ; $78=77+1\equiv1$. Donc $24^3+78\equiv7\equiv0\ [7]$ : oui, divisible par $7$ ($13902=7\times1986$).

## Exercice 3 : lemme de Gauss (3 points)
Type : Bézout, Euclide, lemme de Gauss (démonstrations) · ECUE : HP (arithmétique)
Formules : Bézout : $\exists (u,v), au + bv = a \wedge b$ ; $a \wedge b = 1 \iff \exists (u,v), au + bv = 1$ ; Euclide : $a = bq + r$, remonter les divisions ; Gauss : $a \mid bc$, $a \wedge b = 1 \Rightarrow a \mid c$ ; $a \mid c$, $b \mid c$, $a \wedge b = 1 \Rightarrow ab \mid c$

Lemme de Gauss : si $a\mid bc$ et $a\wedge b=1$ alors $a\mid c$. Preuve : Bézout donne $au+bv=1$, donc $c=acu+bcv$. $a$ divise $acu$ et $a$ divise $bcv$ (car $a\mid bc$), donc $a\mid c$.

## Exercice 4 : pgcd (2,5 points)
Type : PGCD par facteurs premiers, Fermat · ECUE : HP (arithmétique)
Formules : décomposition en facteurs premiers ; $a \wedge b = \prod p^{\min}$ ; Fermat : $p$ premier, $p \nmid a \Rightarrow a^{p-1} \equiv 1\,[p]$ ; premier : exactement deux diviseurs positifs

1. $a=2^3\times3\times21=2^3\times3^2\times7=504$ et $b=90=2\times3^2\times5$ : on garde le minimum des exposants : $a\wedge b=2\times3^2=18$.
2. $23$ est premier et $504=23\times21+21\equiv-2$ n'est pas multiple de $23$ : Fermat donne $a^{22}\equiv1\ [23]$. Le reste est $1$.

## Exercice 5 (6 points)
Type : définitions sur les suites, exemples, limite de $q^n$ · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/4
Formules : croissante $\forall n, u_n \leqslant u_{n+1}$ ; bornée $\exists M, \forall n, |u_n| \leqslant M$ ; exemples $(-1)^n$, $1 - \frac1n$, $\cos n$ ; $(q^n)$ converge $\iff -1 < q \leqslant 1$ (limite 0 si $|q| < 1$, 1 si $q = 1$)

1. (a) $\forall n\in\mathbb N,\ u_{n+1}\ge u_n$. (b) $\exists M\in\mathbb R,\ \forall n\in\mathbb N,\ |u_n|\le M$.
2. (a) $u_n=(-1)^n$ : deux suites extraites de limites $1$ et $-1$, donc divergente (ou $u_n=n$, non majorée). (b) $u_n=3-\dfrac1{n+1}$ : $u_n\le3$. (c) $u_n=1-\dfrac1{n+1}$ : strictement croissante (car $\frac1{n+1}$ décroît strictement), de limite $1$.
3. $(q^n)$ converge $\iff-1<q\le1$. Limite $0$ si $|q|<1$ et $1$ si $q=1$.
