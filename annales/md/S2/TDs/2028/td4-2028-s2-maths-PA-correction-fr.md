# Contrôle de cours ARITH (S2 PA) — lundi 6 mai 2024 (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (pas de corrigé officiel). Sujet : `td4-2028-s2-maths-PA-subject-fr.md` (même dossier). Calculs vérifiés avec sympy. Cours 1 à 3 (arithmétique) hors programme 2031.

## Cours 1 : divisibilité et division euclidienne (4 points)
Type : division euclidienne dans $\mathbb{Z}$ · ECUE : HP (arithmétique)
Formules : $\exists!\,(q, r)$, $a = bq + r$, $0 \leqslant r < |b|$ ; ajuster : $a = bq + r = b(q+1) + (r - b)$ ; pour $-a$ : $-a = b(-q) - r = b(-q-1) + (b - r)$

1. $a\mid b\iff\exists k\in\mathbb Z,\ b=ak$. 2. $\{1,2,3,6\}$.
3. $\forall a\in\mathbb Z$, $b\in\mathbb Z^*$ : il existe un unique $(q,r)\in\mathbb Z\times\mathbb N$ tel que $a=bq+r$ et $0\le r<|b|$.

## Cours 2 : congruences (11,5 points)
Type : congruences, Fermat, reste d'une puissance · ECUE : HP (arithmétique)
Formules : reste de la division par 4 : $r \in \{0,1,2,3\}$ ; $a \equiv b\,[n] \Rightarrow a^k \equiv b^k\,[n]$ ; Fermat : $p$ premier, $p \nmid a \Rightarrow a^{p-1} \equiv 1\,[p]$ ; $a^{q(p-1)+r} \equiv a^r\,[p]$

1. $b=ak$, $c=ah$ donnent $bu+cv=a(ku+hv)$ : $a\mid bu+cv$.
2. $n\mid a-b$ et $n\mid c-d$. Somme : $(a+c)-(b+d)=(a-b)+(c-d)$ est divisible par $n$. Produit : $ac-bd=a(c-d)+d(a-b)$ est divisible par $n$ d'après la question 1.
3. $a=18\equiv2$, $c=31\equiv7$, $a-c\equiv2-7=-5\equiv3$, $ac\equiv14\equiv6$, $a^5\equiv2^5=32\equiv0\ [8]$.
4. (a) $p$ premier : $\forall n\in\mathbb Z,\ n^p\equiv n\ [p]$ ; si $p\nmid n$ : $n^{p-1}\equiv1\ [p]$. (b) $15\equiv4\ [11]$ et $4^{10}\equiv1$ : $15^{14}\equiv4^{14}=4^{10}\cdot4^4\equiv4^4=256=11\times23+3$. Le reste est $3$.

## Cours 3 : nombres premiers et pgcd (2 points)
Type : décomposition en facteurs premiers, PGCD · ECUE : HP (arithmétique)
Formules : critères de divisibilité (2, 3 : somme des chiffres, 5, 11) ; $a \wedge b = \prod p^{\min(\alpha_p, \beta_p)}$

1. $700=2^2\times5^2\times7$. 2. Minimum des exposants : $a\wedge b=2\times5^2\times7=350$.

## Cours 4 : polynômes 1 (2,5 points)
Type : degré, division euclidienne de polynômes, racine · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/2
Formules : $\deg(A+B) \leqslant \max(\deg A, \deg B)$ ; $\deg(AB) = \deg A + \deg B$ ; $\exists!\,(Q,R)$, $A = BQ + R$, $\deg R < \deg B$ ; $\alpha$ racine $\iff A(\alpha) = 0 \iff X - \alpha \mid A$

$X^5-X^3+2X^2-4=(X^3+X+1)(X^2-2)+(X^2+2X-2)$, avec $\deg(X^2+2X-2)=2<3$ : quotient $X^2-2$, reste $X^2+2X-2$.

## Cours 5 : polynômes 2 (10 points)
Type : divisibilité de polynômes, multiplicité, factorisation dans $\mathbb{R}[X]$ et $\mathbb{C}[X]$ · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/9
Formules : $P(a) = 0 \iff X - a \mid P$ ; racine d'ordre $\geqslant 2$ $\iff P(a) = P'(a) = 0$ ; ordre exactement $m$ : $P^{(m)}(a) \neq 0$ ; $(X - a)^m \mid P$, $(X - a)^{m+1} \nmid P$ ; $X^2 + 1 = (X - i)(X + i)$ ; $\Delta < 0 \Rightarrow$ irréductible dans $\mathbb{R}[X]$

1. a) $\iff$. b) $\Leftarrow$ ($(X-3)^2\mid P\Rightarrow P(3)=0$). c) $\Leftarrow$ (le membre de droite est plus fort). d) $\Rightarrow$.
2. $P=X^2(X^3-3X^2+1)$ et $X^3-3X^2+1$ vaut $1\ne0$ en $0$ : $0$ est racine d'ordre exactement $2$.
3. $Q=(X+2)^3X^2$.
4. $A=(X-1)(X+3)^2X$.
5. a) $X(X+1)$ : NON. b) $X^2+1$ ($\Delta=-4<0$) : OUI. c) $X^3+X+1$ : degré $3$, a une racine réelle : NON. d) $(X-1)(X-2)$ : NON. e) $X^2+X+1$ ($\Delta=-3<0$) : OUI.
