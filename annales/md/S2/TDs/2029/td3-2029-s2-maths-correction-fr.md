# Contrôle de cours APEF (S2 B3) — lundi 10 février 2025 (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (pas de corrigé officiel). Sujet : `td3-2029-s2-maths-subject-fr.md` (même dossier). Calculs vérifiés avec sympy. 

## 1. Polynômes (7 points)
Type : divisibilité de polynômes, multiplicité, factorisation dans $\mathbb{R}[X]$ et $\mathbb{C}[X]$ · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/9
Formules : $P(a) = 0 \iff X - a \mid P$ ; racine d'ordre $\geqslant 2$ $\iff P(a) = P'(a) = 0$ ; ordre exactement $m$ : $P^{(m)}(a) \neq 0$ ; $(X - a)^m \mid P$, $(X - a)^{m+1} \nmid P$ ; $X^2 + 1 = (X - i)(X + i)$ ; $\Delta < 0 \Rightarrow$ irréductible dans $\mathbb{R}[X]$

1. Il existe un unique couple $(Q,R)\in(\mathbb R[X])^2$ tel que $A=BQ+R$ et $\deg R<\deg B$.
2. (a) $(X-a)^3\mid P$ et $(X-a)^4\nmid P$. (b) $P(a)=P'(a)=P''(a)=0$ et $P^{(3)}(a)\ne0$.
3. a) $\iff$. b) $\Rightarrow$. c) $\Leftarrow$. d) $\iff$. e) croix (aucune implication : $X^2-2X$ vérifie $P'(1)=0$ sans être divisible par $X-1$ ; $X-1$ divise $P$ sans que $P'(1)=0$ en général).
4. $P=(X-1)^4X(X-1)=X(X-1)^5$ : l'ordre de $1$ est $5$.
5. $P=(X+1)^3(X+3)^2(X-2)$ (degré $6$).
6. $(2X+4)^2=4(X+2)^2$, $X^2-5X+6=(X-2)(X-3)$, $X^2+X+3$ a $\Delta=-11<0$ : $P=4X^5(X+2)^2(X-2)(X-3)(X^2+X+3)$.

## 2. Équations différentielles linéaires du premier ordre (5,5 points)
Type : démonstration de cours (solutions de $a(t)y' + b(t)y = 0$) · ECUE : APIS (EDO) · Niveau : maths-s1-apis-edo/4
Formules : $S_0 = \{t \mapsto ke^{-F(t)}, k \in \mathbb{R}\}$ avec $F$ primitive de $\frac ba$, $F' = \frac ba$ ; $z = y_0e^F \Rightarrow z' = (y_0' + \frac bay_0)e^F = 0 \Rightarrow z$ constante (inclusion $\subset$) ; réciproque : dériver $ke^{-F}$ et reporter (inclusion $\supset$) ; $\int \frac{u'}u = \ln|u|$, $e^{-\alpha\ln u} = u^{-\alpha}$

1. $F(t)=\displaystyle\int\frac{b(t)}{a(t)}dt$ (une primitive), $F'=\dfrac ba$. $S_0=\{t\mapsto ke^{-F(t)}\}$.
2. Soit $y_0\in S_0$ et $z=y_0e^F$ : $z'=e^F\big(y_0'+\frac bay_0\big)=\dfrac{e^F}a(ay_0'+by_0)=0$, donc $z=k$ et $y_0=ke^{-F}$.
3. $S=\{y_p+y_0,\ y_0\in S_0\}$.
4. (a) $y=-2$. (b) $y=-1$ ($2\cdot0-x\cdot(-1)=x$).

## 3. Équations différentielles linéaires du second ordre (2 points)
Type : EDO 2nd ordre homogène (équation caractéristique, cours) · ECUE : APIS (EDO) · Niveau : maths-s1-apis-edo/8
Formules : $ay'' + by' + cy = 0$ : équation caractéristique $ar^2 + br + c = 0$ ; deux racines réelles $r_1 \neq r_2$ : $y = k_1e^{r_1x} + k_2e^{r_2x}$ ; racine double $r$ : $y = (k_1x + k_2)e^{rx}$ ; racines complexes $\alpha \pm i\beta$ : $y = e^{\alpha x}(k_1\cos(\beta x) + k_2\sin(\beta x))$

1. $(C)$ : $ar^2+br+c=0$.
2. $y(x)=\lambda e^{3x}+\mu e^{-4x}$.
3. $y(x)=e^{-2x}\big(\lambda\cos3x+\mu\sin3x\big)$.
4. $y(x)=(\lambda x+\mu)e^{-7x}$.

## 4. Étude locale de fonctions (5,5 points)
Type : petit o, équivalents et développements limités (manipulation) · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/10
Formules : $f = o(x^n) \iff f(x) = x^n\varepsilon(x)$, $\varepsilon \to 0$ ; $o(x^3) \Rightarrow o(x^2)$ (pas l'inverse) ; $o(x^p) + o(x^q) = o(x^{\min(p,q)})$ ; $f \sim$ premier terme non nul du DL ; $f \sim g \iff f - g = o(g)$ ; $\lim \frac{f}{x^n} = a \neq 0 \iff f \sim ax^n$

1. (a) $\ln(1+x)=x-\dfrac{x^2}2+\dfrac{x^3}3-\dfrac{x^4}4+o(x^4)$. (b) $\sin x=x-\dfrac{x^3}6+o(x^4)$.
2. (a) $f(x)\sim x$ et $g(x)-1\sim3x$. (b) $o(x^3)=x^3\varepsilon(x)$ avec $\varepsilon(x)\to0$ en $0$. (c) À l'ordre $2$ (précision limitée par $g$) : $f+g=1+4x-3x^2+o(x^2)$. (d) $f\times g=(x-2x^2)(1+3x)+o(x^2)=x+x^2+o(x^2)$.
