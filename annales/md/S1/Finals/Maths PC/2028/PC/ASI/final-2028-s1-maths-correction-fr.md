# Correction examen S1B2-ASI — janvier 2024

- Source : `raw/S1/Finals/Maths PC/2028/PC/ASI/final-2028-s1-maths-correction-fr.pdf` (3 pages)
- Date réelle : janvier 2024 (dossier promo 2028). Sujet : `final-2028-s1-maths-subject-fr.md`.

## Exercice 1 : intégrales
Type : primitives usuelles, IPP, changement de variable vers arctan · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/13
Formules : primitives usuelles ($\int \frac{u'}{\sqrt u}$-type : $\int \frac{e^{\sqrt x}}{\sqrt x} = 2e^{\sqrt x}$, $\int \frac{u'}u = \ln|u|$) ; IPP : $\int_a^b uv' = [uv]_a^b - \int_a^b u'v$ ; changement de variable $x = \varphi(t)$, $dt = \frac{dx}{x}$ pour $x = e^t$, bornes transformées ; $\int \frac{dx}{1+x^2} = \arctan x$ ; $\arctan\sqrt3 = \frac\pi3$, $\arctan 1 = \frac\pi4$

1. Tableau :

| $f(x)$ | $\ln 2$ | $x^4 + 2x$ | $\frac{e^{\sqrt x}}{\sqrt x}$ | $\frac1{x^2}$ | $\sin x$ | $1 + \tan^2 x$ | $\sqrt x$ | $\frac{x^5}{x^6 + 1}$ |
|---|---|---|---|---|---|---|---|---|
| $F(x)$ | $x\ln 2$ | $\frac{x^5}5 + x^2$ | $2e^{\sqrt x}$ | $-\frac1x$ | $-\cos x$ | $\tan x$ | $\frac23 x^{3/2}$ | $\frac16\ln(x^6 + 1)$ |

2. IPP : $\int_a^b u v' = [uv]_a^b - \int_a^b u'v$. On pose $u(x) = 3x + 1$, $v'(x) = e^{2x}$, $u'(x) = 3$, $v(x) = \frac{e^{2x}}2$.
$J = \left[\dfrac{(3x+1)e^{2x}}2\right]_0^1 - \dfrac32\displaystyle\int_0^1 e^{2x}\,dx = 2e^2 - \frac12 - \frac32\left[\frac{e^{2x}}2\right]_0^1 = 2e^2 - \frac12 - \frac{3e^2}4 + \frac34 = \frac{5e^2 + 1}4$.
3. $x = e^t \iff t = \ln x$, $dt = \frac{dx}x$ ; $t = 0 \to x = 1$, $t = \ln\sqrt3 \to x = \sqrt3$.
$K = \displaystyle\int_1^{\sqrt3} \frac{1}{\frac1x + x} \cdot \frac{dx}x = \int_1^{\sqrt3} \frac{dx}{1 + x^2} = [\arctan x]_1^{\sqrt3} = \frac\pi3 - \frac\pi4 = \frac\pi{12}$.

## Exercice 2 : suites adjacentes
Type : suites adjacentes ($\sum 1/k!$) · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/9
Formules : adjacentes : $(u_n)$ croissante, $(v_n)$ décroissante, $v_n - u_n \to 0$ ; $u_{n+1} - u_n = \frac1{(n+1)!}$ ; $\frac1{n!} = \frac{n+1}{(n+1)!}$ ; adjacentes $\Rightarrow$ convergentes ; convergente $\Rightarrow$ bornée

1. $(u_n)$ et $(v_n)$ sont adjacentes si $(u_n)$ est croissante, $(v_n)$ décroissante et $\lim (v_n - u_n) = 0$.
- $u_{n+1} - u_n = \frac1{(n+1)!} \geqslant 0$ : $(u_n)$ croissante.
- $v_{n+1} - v_n = \dfrac1{(n+1)!} + \dfrac1{(n+1)!} - \dfrac1{n!} = \dfrac{2 - (n+1)}{(n+1)!} = \dfrac{1 - n}{(n+1)!} \leqslant 0$ car $n \geqslant 2$ : $(v_n)$ décroissante.
- $v_n - u_n = \frac1{n!} \to 0$. Les suites sont adjacentes.
2. Adjacentes, elles convergent (vers une même limite) : $(u_n)$ converge.
3. Toute suite convergente est bornée, donc $(u_n)$ est majorée.

## Exercice 3 : comparaison de suites
Type : comparaison de suites ($\sim$, $o$, $O$) · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/12
Formules : $u_n \sim v_n \iff \frac{u_n}{v_n} \to 1$ ; $u_n = o(v_n) \iff \frac{u_n}{v_n} \to 0$ ; $u_n = O(v_n) \iff \frac{u_n}{v_n}$ bornée ; convergente $\Rightarrow$ bornée, donc $\sim$ et $o$ impliquent $O$ ; croissances comparées : $\frac{\ln n}{n^a} \to 0$, $\frac{n^a}{e^n} \to 0$ ; $\frac{\sin n}{n} \to 0$ ; factoriser par le terme dominant

1. $\dfrac{u_n}{v_n} = \dfrac{1 - \frac1{2n^2}}{1 - \frac1{2n} + \frac3{2n^2}} \to 1$ : $u_n \sim v_n$ et $u_n = O(v_n)$.
2. $\dfrac{u_n}{v_n} = \dfrac{e^{2n}}n \times \dfrac{1 - \frac{\sqrt n}{e^{2n}}}{1 + \frac1n} \to +\infty$ (croissances comparées), donc $\frac{v_n}{u_n} \to 0$ : $v_n = o(u_n)$ et $v_n = O(u_n)$.
3. $\dfrac{u_n}{v_n} = \left(\dfrac45\right)^n + \dfrac1{5^n} \to 0$ : $u_n = o(v_n)$ et $u_n = O(v_n)$.

## Exercice 4 : cours
Type : démonstration de cours (théorème des gendarmes) · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/13
Formules : gendarmes : $\forall n \geqslant N_0$, $a_n \leqslant u_n \leqslant b_n$, $a_n \to \ell$, $b_n \to \ell \Rightarrow u_n \to \ell$ ; définition $\forall \varepsilon, \exists N, n \geqslant N \Rightarrow |u_n - \ell| < \varepsilon$ ; prendre $N = \max(N_0, N_1, N_2)$ : $\ell - \varepsilon < a_n \leqslant u_n \leqslant b_n < \ell + \varepsilon$

Renvoi au document des démonstrations de cours.

## Exercice 5 : étude d'une suite
Type : suite homographique, suite auxiliaire géométrique · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/10
Formules : récurrence pour le signe ; $\ell = f(\ell)$ si $f$ continue ; signe de $u_{n+1} - u_n$ ; décroissante minorée $\Rightarrow$ convergente ; $v_{n+1} = qv_n \Rightarrow v_n = v_0q^n$ ; $q > 1 \Rightarrow q^n \to +\infty$

1. (a) $u_0 = 1 > 0$ ; si $u_n > 0$, $u_{n+1} = \frac{u_n}{u_n + 8} > 0$. Donc $\forall n$, $u_n > 0$.
(b) $f : x \mapsto \frac{x}{x+8}$ continue sur $\mathbb{R}_+^*$, donc $\ell = f(\ell)$ : $\ell^2 + 8\ell = \ell \iff \ell(\ell + 7) = 0$, $\ell = 0$ ou $\ell = -7$.
(c) $u_{n+1} - u_n = \dfrac{u_n - u_n(u_n + 8)}{u_n + 8} = -\dfrac{u_n(u_n + 7)}{u_n + 8} \leqslant 0$ : $(u_n)$ décroissante.
(d) Décroissante et minorée par 0, elle converge vers $\ell \in \{0, -7\}$ avec $\ell \geqslant 0$ : $\ell = 0$.
2. (a) $v_{n+1} = 1 + \dfrac{7(u_n + 8)}{u_n} = 8 + \dfrac{56}{u_n} = 8\left(1 + \dfrac7{u_n}\right) = 8v_n$ : géométrique de raison 8, $v_n = v_0 8^n = 8^{n+1}$.
(b) $u_n = \dfrac7{v_n - 1} = \dfrac7{8^{n+1} - 1}$.
(c) $8^{n+1} \to +\infty$ donc $u_n \to 0$ : on retrouve 1.(d).

## Exercice 6 : suites extraites
Type : suites extraites $(u_{2n})$, $(u_{2n+1})$ · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/11
Formules : $\sum_{k=0}^{n-1} q^k = \frac{1 - q^n}{1 - q}$ ($q \neq 1$) ; $(-1)^{2n} = 1$, $(-1)^{2n+1} = -1$ ; $(u_{2n})$ et $(u_{2n+1})$ même limite $\Rightarrow (u_n)$ converge

1. Somme géométrique de raison $-1$ : $u_n = \dfrac1n \times \dfrac{1 - (-1)^n}{2}$. Ainsi $u_{2n} = 0$ et $u_{2n+1} = \dfrac2{2(2n+1)} = \dfrac1{2n+1}$.
2. $(u_{2n})$ et $(u_{2n+1})$ convergent vers 0, donc $(u_n)$ converge vers 0.
