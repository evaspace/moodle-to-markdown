# Feuille de TD — Les polynômes (S2 2026) (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (pas de corrigé officiel). Sujet : `td1-2030-s2-maths-subject-fr.md` (même dossier). Calculs vérifiés avec sympy. 

## Exercice 1.1
Type : degré, division euclidienne de polynômes, racine · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/2
Formules : $\deg(A+B) \leqslant \max(\deg A, \deg B)$ ; $\deg(AB) = \deg A + \deg B$ ; $\exists!\,(Q,R)$, $A = BQ + R$, $\deg R < \deg B$ ; $\alpha$ racine $\iff A(\alpha) = 0 \iff X - \alpha \mid A$

1. $P+Q=-2X^3+3X^2+9X-6$ ; $P+R=3X-3$ ; $Q+R=2X^3+3X^2+6X-1$. Formule : $\deg(P+Q)\le\max(\deg P,\deg Q)$, avec égalité si les degrés sont différents ou si les coefficients dominants ne s'annulent pas (ici $P+R$ est de degré $1<3$).
2. $A$ : $\deg A=2+3+2=7$, terme dominant $X^2\cdot X^3\cdot4X^2=4X^7$. $B$ : $(5X^2+X-3)^2$ est de degré $4$, de terme dominant $25X^4$, et $-X^3+2$ est de degré $3$ : $\deg B=4$, terme dominant $25X^4$.

## Exercice 1.2
Type : formule de Taylor pour les polynômes · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/7
Formules : $P = \sum a_kX^k \Rightarrow a_k = \frac{P^{(k)}(0)}{k!}$ ; $P(X) = \sum_{k=0}^{\deg P} \frac{P^{(k)}(0)}{k!}X^k$ ; en $a$ : $P(X) = \sum_{k=0}^{\deg P} \frac{P^{(k)}(a)}{k!}(X - a)^k$ ; $(X^n)^{(k)} = \frac{n!}{(n-k)!}X^{n-k}$

1. $a_0=6$, $a_1=-7$, $a_2=-2$, $a_3=3$.
2. $P(0)=6$, $P'=9X^2-4X-7$ : $P'(0)=-7$, $P''=18X-4$ : $P''(0)=-4$, $P^{(3)}=18$.
3. $P(0)=a_0$. 4. $P'(0)=a_1$, $P''(0)=2a_2$, $P^{(3)}(0)=6a_3$.
5. $a_k=\dfrac{P^{(k)}(0)}{k!}$, donc $P(X)=\displaystyle\sum_{k=0}^3\frac{P^{(k)}(0)}{k!}X^k$.
6. (a) $X=Y+1$ : $P(X)=P(Y+1)=:Q(Y)$ est un polynôme de degré $3$ en $Y$, et la question 5 s'applique à $Q$. (b) $Q^{(k)}(Y)=P^{(k)}(Y+1)$ (dérivation d'une composée par $Y\mapsto Y+1$), donc $Q^{(k)}(0)=P^{(k)}(1)$ et $P(X)=\sum\dfrac{P^{(k)}(1)}{k!}(X-1)^k$.

## Exercice 2.3
Type : degré, division euclidienne de polynômes, racine · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/2
Formules : $\deg(A+B) \leqslant \max(\deg A, \deg B)$ ; $\deg(AB) = \deg A + \deg B$ ; $\exists!\,(Q,R)$, $A = BQ + R$, $\deg R < \deg B$ ; $\alpha$ racine $\iff A(\alpha) = 0 \iff X - \alpha \mid A$

1. $(X^2+X-2)(2X^2-2X+5)=2X^4-X^2+9X-10$, donc $2X^4-X^2+X-5=(X^2+X-2)(2X^2-2X+5)+(-8X+5)$. Quotient $2X^2-2X+5$, reste $-8X+5$.
2. $X^3+X+1=(2X+1)\left(\dfrac{X^2}2-\dfrac X4+\dfrac58\right)+\dfrac38$.

## Exercice 2.4
Type : division euclidienne et primitive d'une fraction rationnelle · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/8
Formules : $A = BQ + R$, $\deg R < \deg B$ $\Rightarrow \frac AB = Q + \frac RB$ ; $\int x^n = \frac{x^{n+1}}{n+1}$ ; $\int \frac{u'}u = \ln|u|$ ; $\int \frac{dx}{1+x^2} = \arctan x$

1. $X^4+2X^3+X=(X^2+1)(X^2+2X-1)+(1-X)$.
2. $\dfrac{x^4+2x^3+x}{x^2+1}=x^2+2x-1+\dfrac{1-x}{x^2+1}$. Primitive sur $\mathbb R$ : $\dfrac{x^3}3+x^2-x-\dfrac12\ln(x^2+1)+\arctan x$.

## Exercice 3.5
Type : divisibilité de polynômes par les racines · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/3
Formules : $X - a \mid P \iff P(a) = 0$ ; $(X-a)(X-b) \mid P \iff P(a) = P(b) = 0$ ($a \neq b$) ; $(X-a)^2 \mid P \iff P(a) = P'(a) = 0$

1. Le reste est le polynôme constant $P(a)$ ($P=(X-a)Q+r$, on évalue en $a$).
2. $(X-a)\mid P\iff r=0\iff P(a)=0$.
3. ($\Rightarrow$) évident. ($\Leftarrow$) $P(a)=0$ donne $P=(X-a)Q$. Alors $P(b)=(b-a)Q(b)=0$ avec $b\ne a$ : $Q(b)=0$, donc $Q=(X-b)R$ et $P=(X-a)(X-b)R$.

## Exercice 3.6
Type : divisibilité de polynômes, multiplicité, factorisation dans $\mathbb{R}[X]$ et $\mathbb{C}[X]$ · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/9
Formules : $P(a) = 0 \iff X - a \mid P$ ; racine d'ordre $\geqslant 2$ $\iff P(a) = P'(a) = 0$ ; ordre exactement $m$ : $P^{(m)}(a) \neq 0$ ; $(X - a)^m \mid P$, $(X - a)^{m+1} \nmid P$ ; $X^2 + 1 = (X - i)(X + i)$ ; $\Delta < 0 \Rightarrow$ irréductible dans $\mathbb{R}[X]$

1. (a) Au moins $\alpha$ : $(X-a)^\alpha\mid P$. Exactement $\alpha$ : $(X-a)^\alpha\mid P$ et $(X-a)^{\alpha+1}\nmid P$. (b) $P=-X(X-1)^3(X+1)$ : $0$ (ordre $1$), $1$ (ordre $3$), $-1$ (ordre $1$).
2. (a) $a$ est racine d'ordre exactement $m$ $\iff P(a)=P'(a)=\dots=P^{(m-1)}(a)=0$ et $P^{(m)}(a)\ne0$. (b) $P(0)=0$, $P'(0)=1\ne0$ : simple. $P'=-5X^4+8X^3-4X+1$, $P''=-20X^3+24X^2-4$, $P^{(3)}=-60X^2+48X$ : $P(1)=P'(1)=P''(1)=0$, $P^{(3)}(1)=-12\ne0$ : ordre $3$. $P(-1)=0$ et $P'(-1)=-8\ne0$ : simple.
3. (a) $P$ non constant est irréductible si ses seuls diviseurs sont les constantes et ses multiples par une constante. Dans $\mathbb C[X]$ : les polynômes de degré $1$. Dans $\mathbb R[X]$ : degré $1$ ou degré $2$ de discriminant $<0$. (b) $P=X^2(X-2)(X^2+1)$ dans $\mathbb R[X]$ ; $P=X^2(X-2)(X-i)(X+i)$ dans $\mathbb C[X]$.

## Exercice 3.7
Type : divisibilité de polynômes, multiplicité, factorisation dans $\mathbb{R}[X]$ et $\mathbb{C}[X]$ · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/9
Formules : $P(a) = 0 \iff X - a \mid P$ ; racine d'ordre $\geqslant 2$ $\iff P(a) = P'(a) = 0$ ; ordre exactement $m$ : $P^{(m)}(a) \neq 0$ ; $(X - a)^m \mid P$, $(X - a)^{m+1} \nmid P$ ; $X^2 + 1 = (X - i)(X + i)$ ; $\Delta < 0 \Rightarrow$ irréductible dans $\mathbb{R}[X]$

1. (a) $P(1)=1+2-1-2=0$, $P(-2)=16-16+2-2=0$ : $(X-1)(X+2)=X^2+X-2$ divise $P$. (b) $P=(X^2+X-2)(X^2+X+1)$. $X^2+X+1$ ($\Delta=-3$) : irréductible dans $\mathbb R[X]$ ; dans $\mathbb C[X]$ : $P=(X-1)(X+2)\left(X+\frac12-\frac{i\sqrt3}2\right)\left(X+\frac12+\frac{i\sqrt3}2\right)$.
2. (a) $Q(2)=16-16-12+16-4=0$, $Q(-2)=16+16-12-16-4=0$ : $(X^2-4)\mid Q$. (b) $Q=(X-2)(X+2)(X-1)^2$ (division par $X^2-4$ : quotient $X^2-2X+1$), déjà irréductible dans $\mathbb R[X]$ et $\mathbb C[X]$.
3. (a) $R(1)=1-3-3+11-6=0$, $R'(1)=4-9-6+11=0$, $R''(1)=12-18-6=-12\ne0$ : multiplicité $2$, donc $(X-1)^2\mid R$. (b) $R=(X-1)^2(X^2-X-6)=(X-1)^2(X-3)(X+2)$, identique dans $\mathbb R[X]$ et $\mathbb C[X]$.

## Exercice 3.8
Type : divisibilité de polynômes, multiplicité d'une racine · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/4
Formules : $(X-a)(X-b) \mid P \iff P(a) = P(b) = 0$ ($a \neq b$) ; $\alpha$ racine d'ordre $m$ $\iff P(\alpha) = \dots = P^{(m-1)}(\alpha) = 0$, $P^{(m)}(\alpha) \neq 0$ ; $(X^n)' = nX^{n-1}$

1. $X^2+2X=X(X+2)$, $P(0)=1-1=0$ et $P(-2)=(-1)^{2n}-1=0$ : $X$ et $X+2$ premiers entre eux divisent $P$, donc $X(X+2)\mid P$.
2. $f=nX^{n+1}-(n+1)X^n+1$ : $f(1)=n-(n+1)+1=0$ et $f'=n(n+1)X^n-n(n+1)X^{n-1}$ : $f'(1)=0$. Donc $1$ est racine au moins double : $(X-1)^2\mid f$.
3. $g=nX^{n+2}-(n+2)X^{n+1}+(n+2)X-n$ : $g(1)=n-(n+2)+(n+2)-n=0$. $g'=n(n+2)X^{n+1}-(n+1)(n+2)X^n+(n+2)$ : $g'(1)=(n+2)(n-(n+1)+1)=0$. $g''=n(n+1)(n+2)X^n-n(n+1)(n+2)X^{n-1}$ : $g''(1)=0$. $g^{(3)}=n(n+1)(n+2)\big(nX^{n-1}-(n-1)X^{n-2}\big)$ : $g^{(3)}(1)=n(n+1)(n+2)\ne0$. La multiplicité est exactement $3$.

## Exercice 3.9
Type : divisibilité et reste de division euclidienne de polynômes · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/5
Formules : $A = BQ + R$, $\deg R < \deg B$ ; $(X-a)(X-b) \mid P \iff P(a) = P(b) = 0$ ($a \neq b$) ; reste par $(X-a)(X-b)$ : $R = \alpha X + \beta$ avec $R(a) = P(a)$, $R(b) = P(b)$ ; reste par $(X-a)^2$ : $R(a) = P(a)$, $R'(a) = P'(a)$

$Q(1)=1+0-2=-1$ et $Q(2)=0+1-2=-1$.
1. Reste $R=\alpha X+\beta$ avec $R(1)=R(2)=-1$ : $R=-1$.
2. Reste $R=\alpha X+\beta$ avec $R(1)=Q(1)=-1$ et $R'(1)=Q'(1)=2n(X-2)^{2n-1}+n(X-1)^{n-1}$ en $1$ $=-2n$ (car $n\ge2$) : $R=-2nX+2n-1$.

## Exercice 3.10 (⋆)
Type : divisibilité et reste de division euclidienne de polynômes · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/5
Formules : $A = BQ + R$, $\deg R < \deg B$ ; $(X-a)(X-b) \mid P \iff P(a) = P(b) = 0$ ($a \neq b$) ; reste par $(X-a)(X-b)$ : $R = \alpha X + \beta$ avec $R(a) = P(a)$, $R(b) = P(b)$ ; reste par $(X-a)^2$ : $R(a) = P(a)$, $R'(a) = P'(a)$

$P=X^3+aX^2+bX+c$ unitaire de degré $3$. Si les restes par $X-2$, $X-3$, $X-4$ valent $r$ : $P(2)=P(3)=P(4)=r$, donc $P-r$ (unitaire de degré $3$) s'annule en $2,3,4$ : $P-r=(X-2)(X-3)(X-4)$. $P(1)=0$ donne $-6+r=0$, $r=6$. $P=(X-2)(X-3)(X-4)+6=X^3-9X^2+26X-18$ (le seul polynôme).
