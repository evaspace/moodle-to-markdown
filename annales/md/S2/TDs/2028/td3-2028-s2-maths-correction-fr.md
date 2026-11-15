# Contrôle de cours APEF (S2) — lundi 19 février 2024 (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (pas de corrigé officiel). Sujet : `td3-2028-s2-maths-subject-fr.md` (même dossier). Calculs vérifiés avec sympy. 

## Cours 1 : divisibilité et division euclidienne (2,5 points)
Type : degré, division euclidienne de polynômes, racine · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/2
Formules : $\deg(A+B) \leqslant \max(\deg A, \deg B)$ ; $\deg(AB) = \deg A + \deg B$ ; $\exists!\,(Q,R)$, $A = BQ + R$, $\deg R < \deg B$ ; $\alpha$ racine $\iff A(\alpha) = 0 \iff X - \alpha \mid A$

1. Le reste $2X^2-X+2$ est de degré $2$ et doit être de degré $<\deg B$ : $\deg B\ge3$, donc $B=X^3+1$ (le quotient est $X+2$). Reste : $2X^2-X+2$.
2. $-X^4+3X-5=(X^2+1)(-X^2+1)+3X-6$ : quotient $-X^2+1$, reste $3X-6$.

## Cours 2 : autour des racines (5,5 points)
Type : divisibilité de polynômes, multiplicité, factorisation dans $\mathbb{R}[X]$ et $\mathbb{C}[X]$ · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/9
Formules : $P(a) = 0 \iff X - a \mid P$ ; racine d'ordre $\geqslant 2$ $\iff P(a) = P'(a) = 0$ ; ordre exactement $m$ : $P^{(m)}(a) \neq 0$ ; $(X - a)^m \mid P$, $(X - a)^{m+1} \nmid P$ ; $X^2 + 1 = (X - i)(X + i)$ ; $\Delta < 0 \Rightarrow$ irréductible dans $\mathbb{R}[X]$

1. a) $\iff$. b) $\Rightarrow$. c) $\Leftarrow$ ($P=X^4+X$ implique $P(0)=0$ mais pas l'inverse). d) $\iff$. e) $\Rightarrow$.
2. $P=(X+1)(X-2)X$.
3. $Q=(X+2)^3X^2$ (degré $5$, $-2$ racine d'ordre exactement $3$).
4. $A=X(X+3)^2(X-1)$ (degré $4$, $A(0)=0$, $-3$ racine double donc $A(-3)=A'(-3)=0$).
5. Irréductibles : a) $2X+1$ et e) $X^2+X+1$ ($\Delta=-3<0$). Non irréductibles : b) $X(X+1)$, d) $(X-1)(X+1)$, c) $X^3+X+1$ (degré $3$ : a une racine réelle).

## 2. Équations différentielles (6 points)
Type : démonstration de cours (structure des solutions de $a(t)y' + b(t)y = c(t)$) · ECUE : APIS (EDO) · Niveau : maths-s1-apis-edo/5
Formules : $S_0 = \{t \mapsto ke^{-F(t)}\}$, $F' = \frac ba$ ; $S = \{y_p + y_0,\ y_0 \in S_0\}$ ; linéarité : $a(y_p + y_0)' + b(y_p + y_0) = c + 0$ (inclusion $\supset$) ; si $y \in S$ alors $y - y_p \in S_0$ (inclusion $\subset$) ; retrouver l'équation : $y_0 = ke^{-F}$ donne $\frac ba = F'$, puis $c = ay_p' + by_p$

1. $S_0=\{t\mapsto ke^{-F(t)},\ k\in\mathbb R\}$ avec $F'=\dfrac ba$.
2. (a) $f=y_p+y_0$, $y_0\in S_0$. $f'=y_p'+y_0'$. $af'+bf=(ay_p'+by_p)+(ay_0'+by_0)=c+0=c$ car $y_p$ solution de $(E)$ et $y_0$ de $(E_0)$. Donc $f\in S$. (b) $B\subset S$. (c) Soit $y\in S$ : $a(y-y_p)'+b(y-y_p)=c-c=0$, donc $y-y_p\in S_0$ et $y=y_p+(y-y_p)\in B$ : $S\subset B$.
3. $y_0:t\mapsto e^{\arctan t}$ a pour dérivée $\dfrac{y_0}{1+t^2}$ : $(1+t^2)y'-y=0$ est vérifiée par $y_0$. Avec $y_p=1$ : $(1+t^2)\cdot0-1=-1$. Donc $a=1+t^2$, $b=-1$, $c=-1$ : $(1+t^2)y'-y=-1$.

## 3. Développements limités usuels (6 points)
Type : développements limités usuels et composés · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/8
Formules : $e^u = \sum \frac{u^k}{k!}$ ; $\cos u = 1 - \frac{u^2}2 + \frac{u^4}{24}$ ; $\sin u = u - \frac{u^3}6$ ; $\ln(1+u) = u - \frac{u^2}2 + \frac{u^3}3 - \frac{u^4}4$ ; $\sqrt{1+u} = 1 + \frac u2 - \frac{u^2}8 + \frac{u^3}{16} - \frac{5u^4}{128}$ ; $(1+u)^\alpha = 1 + \alpha u + \frac{\alpha(\alpha-1)}2u^2$ ; produit tronqué ; composition : poser $u$, calculer $u^2$ à l'ordre voulu ; $1 + \cos 2x = 2\cos^2 x$

1. $e^x=1+x+\dfrac{x^2}2+\dfrac{x^3}6+o(x^3)$. 2. $\cos x=1-\dfrac{x^2}2+o(x^3)$. 3. $\ln(1+x)=x-\dfrac{x^2}2+\dfrac{x^3}3+o(x^3)$. 4. $\sin x=x-\dfrac{x^3}6+o(x^3)$.
5. $(1+x)^\alpha=1+\alpha x+\dfrac{\alpha(\alpha-1)}2x^2+\dfrac{\alpha(\alpha-1)(\alpha-2)}6x^3+o(x^3)$.
6. $\alpha=\dfrac12$ : $\dfrac{\alpha(\alpha-1)}2=-\dfrac18$, $\dfrac{\alpha(\alpha-1)(\alpha-2)}6=\dfrac{\frac12\cdot(-\frac12)\cdot(-\frac32)}6=\dfrac1{16}$ : $\sqrt{1+x}=1+\dfrac x2-\dfrac{x^2}8+\dfrac{x^3}{16}+o(x^3)$.
