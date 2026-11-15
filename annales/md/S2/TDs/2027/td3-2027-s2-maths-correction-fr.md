# Contrôle de cours 1 (S2) — lundi 30 janvier 2023 (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (pas de corrigé officiel). Sujet : `td3-2027-s2-maths-subject-fr.md` (même dossier). Calculs vérifiés avec sympy. 

## Cours 1 : divisibilité et division euclidienne (3 points)
Type : degré, division euclidienne de polynômes, racine · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/2
Formules : $\deg(A+B) \leqslant \max(\deg A, \deg B)$ ; $\deg(AB) = \deg A + \deg B$ ; $\exists!\,(Q,R)$, $A = BQ + R$, $\deg R < \deg B$ ; $\alpha$ racine $\iff A(\alpha) = 0 \iff X - \alpha \mid A$

1. $E\mid F\iff\exists Q\in\mathbb R[X],\ F=EQ$. Exemple : $E=2X-1$, $F=(2X-1)(X+1)=2X^2+X-1$.
2. (a) Il existe un unique couple $(Q,R)\in(\mathbb R[X])^2$ tel que $F=EQ+R$ et $\deg R<\deg E$. (b) Horner en $1$ avec les coefficients $1,-3,5,-7$ : $1,-2,3,-4$. Quotient $X^2-2X+3$, reste $-4$.

## Cours 2 : racines (6 points)
Type : divisibilité de polynômes, multiplicité, factorisation dans $\mathbb{R}[X]$ et $\mathbb{C}[X]$ · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/9
Formules : $P(a) = 0 \iff X - a \mid P$ ; racine d'ordre $\geqslant 2$ $\iff P(a) = P'(a) = 0$ ; ordre exactement $m$ : $P^{(m)}(a) \neq 0$ ; $(X - a)^m \mid P$, $(X - a)^{m+1} \nmid P$ ; $X^2 + 1 = (X - i)(X + i)$ ; $\Delta < 0 \Rightarrow$ irréductible dans $\mathbb{R}[X]$

1. a) $\iff$ : $1$ racine de $P\iff(X-1)\mid P$. b) $(X-1)^2\mid P\Rightarrow P(1)=0$ : $\Rightarrow$. c) $(X^2-X)\mid P\Rightarrow P(0)=0$ : $P(0)=0\Leftarrow(X^2-X)\mid P$ : $\Leftarrow$.
2. Ordre exactement $3$ : $(X-a)^3\mid P$ et $(X-a)^4\nmid P$. Avec des quantificateurs : $\exists Q\in\mathbb R[X],\ P=(X-a)^3Q$ et $Q(a)\ne0$.
3. $P=(X+1)^3X^2(X-1)$ (degré $6$ ; $-1$ est d'ordre exactement $3$ car $X^2(X-1)$ vaut $-2\ne0$ en $-1$ ; $0$ est racine double donc $P(0)=P'(0)=0$).
4. (a) $\deg P=3+2+2+2=9$ (le degré d'un produit est la somme des degrés). (b) $X^2-X-6=(X-3)(X+2)$ et $X^2+X+1$ a $\Delta=-3<0$ : $P=X^3(X+2)^3(X-3)(X^2+X+1)$. Racines réelles : $0$ (ordre $3$), $-2$ (ordre $3$), $3$.

## Cours 3 : équations différentielles (7 points)
Type : démonstration de cours (solutions de $a(t)y' + b(t)y = 0$) · ECUE : APIS (EDO) · Niveau : maths-s1-apis-edo/4
Formules : $S_0 = \{t \mapsto ke^{-F(t)}, k \in \mathbb{R}\}$ avec $F$ primitive de $\frac ba$, $F' = \frac ba$ ; $z = y_0e^F \Rightarrow z' = (y_0' + \frac bay_0)e^F = 0 \Rightarrow z$ constante (inclusion $\subset$) ; réciproque : dériver $ke^{-F}$ et reporter (inclusion $\supset$) ; $\int \frac{u'}u = \ln|u|$, $e^{-\alpha\ln u} = u^{-\alpha}$

1. $F$ primitive de $\dfrac ba$ : $F(t)=\displaystyle\int\frac{b(t)}{a(t)}\,dt$, $F'=\dfrac ba$ ; $S_0=\{t\mapsto ke^{-F(t)}\}$.
2. (a) $z'=y_0'e^F+y_0F'e^F=\dfrac{e^F}a\big(ay_0'+by_0\big)=0$ car $y_0\in S_0$. Donc $z$ est constante, $z=k$, et $y_0=ke^{-F}$. (b) L'inclusion $S_0\subset\{ke^{-F}\}$. (c) Si $y=ke^{-F}$ : $y'=-F'y=-\dfrac bay$ donc $ay'+by=0$ : $y\in S_0$.
3. $a=t^4+1$, $b=2t^3$ : $F=\dfrac12\ln(t^4+1)$ et $y(t)=\dfrac k{\sqrt{t^4+1}}$, $k\in\mathbb R$.

## Cours 4 : développements limités (4 points)
Type : développements limités usuels et composés · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/8
Formules : $e^u = \sum \frac{u^k}{k!}$ ; $\cos u = 1 - \frac{u^2}2 + \frac{u^4}{24}$ ; $\sin u = u - \frac{u^3}6$ ; $\ln(1+u) = u - \frac{u^2}2 + \frac{u^3}3 - \frac{u^4}4$ ; $\sqrt{1+u} = 1 + \frac u2 - \frac{u^2}8 + \frac{u^3}{16} - \frac{5u^4}{128}$ ; $(1+u)^\alpha = 1 + \alpha u + \frac{\alpha(\alpha-1)}2u^2$ ; produit tronqué ; composition : poser $u$, calculer $u^2$ à l'ordre voulu ; $1 + \cos 2x = 2\cos^2 x$

1. $e^x=1+x+\dfrac{x^2}2+\dfrac{x^3}6+o(x^3)$. 2. $\cos x=1-\dfrac{x^2}2+o(x^3)$. 3. $\sin x=x-\dfrac{x^3}6+o(x^3)$. 4. $\ln(1+x)=x-\dfrac{x^2}2+\dfrac{x^3}3+o(x^3)$.
