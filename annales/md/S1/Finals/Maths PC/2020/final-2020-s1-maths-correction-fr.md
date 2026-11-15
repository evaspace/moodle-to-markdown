# Partiel 1 — janvier 2016 (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (pas de corrigé officiel). Sujet : `final-2020-s1-maths-subject-fr.md` (même dossier). Calculs vérifiés avec sympy. Exercices 5 et 6 (arithmétique) hors programme 2031.

## Exercice 1 (4 points)
Type : nier une phrase · ECUE : OBM · Niveau : maths-s1-obm/3
Formules : $\neg(\forall x, P(x)) \iff \exists x, \neg P(x)$ ; $\neg(\exists x, P(x)) \iff \forall x, \neg P(x)$ ; $\neg(P \Rightarrow Q) \iff P \wedge \neg Q$ ; $\neg(P \wedge Q) \iff \neg P \vee \neg Q$ ; $\neg(P \vee Q) \iff \neg P \wedge \neg Q$ ; « aucun » = $\forall, \neg$

1. Il existe un diplômé de l'EPITA dont le premier salaire brut annuel est en dessous de 40 k€.
2. J'intègre le laboratoire de recherche de l'EPITA et je ne pourrai pas m'orienter vers l'imagerie médicale.
3. Aucun MiMo n'est compliqué.
4. Au moins un de vos gestes sur IONISx n'est pas analysé.

## Exercice 2 (2 points)
Type : récurrence (inégalité de Bernoulli) · ECUE : OBM · Niveau : maths-s1-obm/7
Formules : récurrence : $P(n_0)$ et $P(n) \Rightarrow P(n+1)$ ; $(1+x)^{n+1} = (1+x)^n(1+x)$ ; $(1+nx)(1+x) = 1 + (n+1)x + nx^2 \geqslant 1 + (n+1)x$

Initialisation : $n=1$ : $(1+x)^1=1+x\ge1+x$.
Hérédité : on suppose $(1+x)^n\ge1+nx$. Comme $1+x>0$ : $(1+x)^{n+1}=(1+x)^n(1+x)\ge(1+nx)(1+x)=1+(n+1)x+nx^2\ge1+(n+1)x$ car $nx^2\ge0$. La propriété est vraie au rang $n+1$ ; elle est vraie pour tout $n\in\mathbb N^*$.

## Exercice 3 (2 points)
Type : traduire avec quantificateurs · ECUE : OBM · Niveau : maths-s1-obm/4
Formules : « tout » $= \forall$, « il existe » $= \exists$, « aucun » $= \forall \dots \neg$ ; l'ordre $\forall\exists$ / $\exists\forall$ change le sens ; $f$ s'annule : $\exists x, f(x) = 0$ ; minimum en $a$ : $\exists a, \forall x, f(x) \geqslant f(a)$ ; pair : $\exists k, n = 2k$

1. $\forall y\in\mathbb R,\ \exists x\in\mathbb R,\ y=x^3$.
2. $\exists x\in\mathbb R,\ \forall y\in\mathbb R,\ x=y^3$.
3. $\forall n\in\mathbb N,\ \big(\exists k\in\mathbb N,\ n=2k\big)\ \text{ou}\ \big(\exists k\in\mathbb N,\ n=2k+1\big)$.
4. $\forall(a,b)\in\mathbb R^2,\ a<b\Rightarrow\exists q\in\mathbb Q,\ a<q<b$.

## Exercice 4 (2 points)
Type : injectivité / surjectivité de $x \mapsto x^2$ · ECUE : OBM · Niveau : maths-s1-obm/10
Formules : injective : $f(x) = f(y) \Rightarrow x = y$ ; surjective : $\forall y \in F, \exists x \in E, y = f(x)$ ; $x^2 = y^2 \iff x = \pm y$ ; $x^2 \geqslant 0$

1. $\mathbb R_+\to\mathbb R$ : injective, non surjective (les valeurs négatives ne sont pas atteintes) : **a** et **d**.
2. $\mathbb R\to\mathbb R$ : non injective ($f(-1)=f(1)$), non surjective : **b** et **d**.
3. $\mathbb R\to\mathbb R_+$ : non injective, surjective ($y=f(\sqrt y)$) : **b** et **c**.
4. $\mathbb R_+\to\mathbb R_+$ : injective et surjective : **a** et **c**.

## Exercice 5 (3 points)
Type : équation diophantienne $ax+by=c$ (Euclide, Gauss) · ECUE : HP (arithmétique)
Formules : Euclide : $a = bq + r$, $a \wedge b = b \wedge r$ ; solutions $\iff (a \wedge b) \mid c$ ; diviser par $d = a \wedge b$ ; remonter Euclide : $au_0 + bv_0 = d$ puis multiplier par $c/d$ ; Gauss : $a \mid bc$ et $a \wedge b = 1 \Rightarrow a \mid c$ ; $a(x - x_0) = -b(y - y_0)$ donne $x = x_0 + \frac{b}{d}k$, $y = y_0 - \frac{a}{d}k$, $k \in \mathbb{Z}$ ; vérifier la réciproque

1. Euclide : $524=3\cdot144+92$, $144=1\cdot92+52$, $92=1\cdot52+40$, $52=1\cdot40+12$, $40=3\cdot12+4$, $12=3\cdot4$ : $524\wedge144=4$, qui divise $4$. En remontant : $4=40-3\cdot12=4\cdot40-3\cdot52=4\cdot92-7\cdot52=11\cdot92-7\cdot144=11\cdot524-40\cdot144$. Solution particulière : $(x_0,y_0)=(11,-40)$.
2. On divise par $4$ : $131x+36y=1$, avec $131\wedge36=1$. Si $(x,y)$ est solution, par différence avec $(11,-40)$ : $131(x-11)=-36(y+40)$. Donc $36\mid131(x-11)$ et $131\wedge36=1$ : par Gauss, $36\mid x-11$, soit $x=11+36k$, $k\in\mathbb Z$. Alors $y=-40-131k$. Réciproquement ces couples sont solutions. $S=\{(11+36k,\ -40-131k),\ k\in\mathbb Z\}$.

## Exercice 6 (2 points)
Type : PGCD et Bézout (démonstration) · ECUE : HP (arithmétique)
Formules : $d \mid a$ et $d \mid b$ : $a = da'$, $b = db'$ ; $a' \wedge b' = 1$ ; Bézout : $a' \wedge b' = 1 \iff \exists (u,v), a'u + b'v = 1$ ; multiplier par $d$

1. $d$ divise $a$ et $b$ : $a=da'$, $b=db'$ avec $a',b'\in\mathbb N^*$. Si $e=a'\wedge b'$, alors $de$ divise $a$ et $b$, donc $de\mid d$ (car $d=a\wedge b$) et $e=1$.
2. $a'\wedge b'=1$, donc par Bézout $\exists(u,v)\in\mathbb Z^2,\ a'u+b'v=1$. En multipliant par $d$ : $au+bv=d$.

## Exercice 7 (2 points)
Type : multiplicité d'une racine d'un polynôme · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/4
Formules : $\alpha$ racine d'ordre $m$ $\iff P(\alpha) = P'(\alpha) = \dots = P^{(m-1)}(\alpha) = 0$ et $P^{(m)}(\alpha) \neq 0$ ; $(X^n)' = nX^{n-1}$

$P(1)=1-1-3+5-2=0$, $P'(X)=4X^3-3X^2-6X+5$ : $P'(1)=0$, $P''(X)=12X^2-6X-6$ : $P''(1)=0$, $P'''(X)=24X-6$ : $P'''(1)=18\ne0$. La racine $1$ est d'ordre $3$ ($P=(X-1)^3(X+2)$).

## Exercice 8 (3 points)
Type : divisibilité et reste de division euclidienne de polynômes · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/5
Formules : $A = BQ + R$, $\deg R < \deg B$ ; $(X-a)(X-b) \mid P \iff P(a) = P(b) = 0$ ($a \neq b$) ; reste par $(X-a)(X-b)$ : $R = \alpha X + \beta$ avec $R(a) = P(a)$, $R(b) = P(b)$ ; reste par $(X-a)^2$ : $R(a) = P(a)$, $R'(a) = P'(a)$

1. $X^2-3X+2=(X-1)(X-2)$. $P(1)=(-1)^{2n}+0-1=0$ et $P(2)=0+1-1=0$ : $P$ s'annule en $1$ et $2$, donc est divisible par $(X-1)(X-2)$.
2. a. $Q(1)=1-2=-1$ et $Q(2)=0+1-2=-1$. Le reste $R=\alpha X+\beta$ vérifie $R(1)=R(2)=-1$ : $R=-1$.
   b. $R=\alpha X+\beta$ avec $R(1)=Q(1)=-1$ et $R'(1)=Q'(1)$. $Q'(X)=2n(X-2)^{2n-1}+n(X-1)^{n-1}$ donc $Q'(1)=-2n+0=-2n$ (car $n\ge2$). $\alpha=-2n$ et $\beta=-1+2n$ : $R=-2nX+2n-1$.

## Exercice 9 (2 points)
Type : racine multiple d'un polynôme à paramètre · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/10
Formules : $\alpha$ racine au moins double $\iff Q(\alpha) = Q'(\alpha) = 0$ ; $((X+1)^7)' = 7(X+1)^6$ ; $(X+1)^6 = X^6 \iff X + 1 = \pm X$

$Q'(X)=7\big((X+1)^6-X^6\big)$. $Q'(\alpha)=0\iff(\alpha+1)^6=\alpha^6\iff\alpha+1=\pm\alpha$, soit $\alpha=-\dfrac12$ (le cas $\alpha+1=\alpha$ est impossible). $Q\left(-\dfrac12\right)=\dfrac1{2^7}+\dfrac1{2^7}-a=\dfrac1{64}-a$. Racine réelle au moins double $\iff a=\dfrac1{64}$.
