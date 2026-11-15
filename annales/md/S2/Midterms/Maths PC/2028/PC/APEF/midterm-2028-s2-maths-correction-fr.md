# Examen S2-B3 APEF — mars 2024 (corrigé, FR)

- Source : `raw/S2/Midterms/Maths PC/2028/PC/APEF/midterm-2028-s2-maths-correction-fr.pdf` (4 pages)
- Date réelle : mars 2024 (S2, bloc 3, dossier promo 2028). Sujet : `midterm-2028-s2-maths-subject-fr.md` (même dossier).
- Corrigé officiel : énoncé rappelé, solution en citation.

## Exercice 1 : polynômes 1
Type : divisibilité de polynômes, multiplicité, factorisation dans $\mathbb{R}[X]$ et $\mathbb{C}[X]$ · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/9
Formules : $P(a) = 0 \iff X - a \mid P$ ; racine d'ordre $\geqslant 2$ $\iff P(a) = P'(a) = 0$ ; ordre exactement $m$ : $P^{(m)}(a) \neq 0$ ; $(X - a)^m \mid P$, $(X - a)^{m+1} \nmid P$ ; $X^2 + 1 = (X - i)(X + i)$ ; $\Delta < 0 \Rightarrow$ irréductible dans $\mathbb{R}[X]$

On considère $P(X) = X^5 + 4X^4 + 7X^3 + 6X^2 + 2X \in \mathbb{R}[X]$.

1. Sans utiliser la notion de dérivée, montrer que 0 est une racine d'ordre de multiplicité exactement 1 de $P$.
> $P(X) = X(X^4 + 4X^3 + 7X^2 + 6X + 2) = XQ(X)$ avec $Q(0) = 2 \neq 0$ : 0 est racine simple.

2. Montrer que $-1$ est une racine d'ordre de multiplicité exactement 2 de $P$.
> $P(-1) = -1 + 4 - 7 + 6 - 2 = 0$. $P'(X) = 5X^4 + 16X^3 + 21X^2 + 12X + 2$, $P'(-1) = 5 - 16 + 21 - 12 + 2 = 0$. $P''(X) = 20X^3 + 48X^2 + 42X + 12$, $P''(-1) = -20 + 48 - 42 + 12 = -2 \neq 0$.

3. En déduire que $X^3 + 2X^2 + X \mid P$.
> $X \mid P$ et $(X+1)^2 \mid P$, racines distinctes, donc $X(X+1)^2 = X^3 + 2X^2 + X \mid P$.

4. En vous servant d'une division euclidienne que vous poserez, écrire $P$ comme produit de polynômes irréductibles dans $\mathbb{R}[X]$ et dans $\mathbb{C}[X]$.
> Division de $P$ par $X^3 + 2X^2 + X$ : quotient $X^2 + 2X + 2$, reste nul. $X^2 + 2X + 2$ a pour discriminant $-4 < 0$ : irréductible dans $\mathbb{R}[X]$. Dans $\mathbb{R}[X]$ : $P(X) = X(X+1)^2(X^2 + 2X + 2)$. Racines complexes de $X^2 + 2X + 2$ : $-1 \pm i$. Dans $\mathbb{C}[X]$ : $P(X) = X(X+1)^2(X + 1 - i)(X + 1 + i)$.

## Exercice 2 : polynômes 2
Type : multiplicité d'une racine d'un polynôme · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/4
Formules : $\alpha$ racine d'ordre $m$ $\iff P(\alpha) = P'(\alpha) = \dots = P^{(m-1)}(\alpha) = 0$ et $P^{(m)}(\alpha) \neq 0$ ; $(X^n)' = nX^{n-1}$

Dans $\mathbb{R}[X]$, on considère un polynôme $P$ de la forme $P(X) = Q(X) \times (X-1)^n$ avec $n \in \mathbb{N}^*$ et $Q$ un polynôme de degré 2. On suppose de plus que $Q(0) = 0$, $Q(-1) = 0$, $Q(1) = 2$, $P(1) = P'(1) = P''(1) = 0$ et $P^{(3)}(1) \neq 0$. Trouver $P$ sous une forme factorisée. Expliquez brièvement votre raisonnement.
> $Q$ de degré 2 avec $Q(0) = Q(-1) = 0$ : $Q(X) = \alpha X(X+1)$. $Q(1) = 2\alpha = 2$ donc $\alpha = 1$. $P(1) = P'(1) = P''(1) = 0$ et $P^{(3)}(1) \neq 0$ : 1 est racine d'ordre exactement 3, et $Q(1) \neq 0$, donc $n = 3$. $P(X) = X(X+1)(X-1)^3$.

## Exercice 3 : équations différentielles
Type : EDO linéaires 1er ordre (variation de la constante) et 2nd ordre · ECUE : APIS (EDO) · Niveau : maths-s1-apis-edo/11
Formules : $y' + a(x)y = 0 \Rightarrow y = ke^{-A(x)}$, $A' = a$ ; solution générale = homogène + particulière ; variation de la constante $y_p = k(x)y_0(x)$ ; $ay'' + by' + cy = 0$ : $ar^2 + br + c = 0$, racine double $r$ : $y = (k_1x + k_2)e^{rx}$ ; second membre $P(x)e^{rx}$ : $y_p = Q(x)e^{rx}$

1. Trouver une solution particulière pour chaque équation différentielle suivante. Vous justifierez brièvement.
   - (a) $(E)$ : $2y' + 6y = -3$ sur $\mathbb{R}$.
   - (b) $(E)$ : $y' + y = e^x$ sur $\mathbb{R}$.
   - (c) $(E)$ : $y'' + y' + y = x + 1$ sur $\mathbb{R}$.
> (a) $y_p : x \mapsto -\frac12$ : $2 \times 0 + 6 \times (-\frac12) = -3$.
> (b) $y_p : x \mapsto \frac{e^x}2$ : $\frac{e^x}2 + \frac{e^x}2 = e^x$.
> (c) $y_p : x \mapsto x$ : $0 + 1 + x = x + 1$.

2. Résoudre dans $\mathbb{R}$, $(E)$ : $y'' + y' + y = x + 1$.
> Équation caractéristique $r^2 + r + 1 = 0$ : racines $-\frac12 \pm i\frac{\sqrt3}2$. Avec $y_p(x) = x$ : $S = \Big\{ x \mapsto e^{-\frac x2}\Big(k_1\cos\big(\tfrac{\sqrt3}2x\big) + k_2\sin\big(\tfrac{\sqrt3}2x\big)\Big) + x,\ (k_1,k_2) \in \mathbb{R}^2 \Big\}$.

3. Résoudre, dans $\mathbb{R}$, $(E)$ : $(e^x + 1)y' + e^xy = \cos(3x)$.
> $(E_0)$ : $y_0(x) = ke^{-\int \frac{e^x}{e^x+1}dx} = ke^{-\ln(e^x+1)} = \dfrac k{e^x+1}$, $k \in \mathbb{R}$.
> Variation de la constante : $y_p(x) = \dfrac{k(x)}{e^x+1}$. $(e^x+1)\dfrac{k'(x)(e^x+1) - e^xk(x)}{(e^x+1)^2} + e^x\dfrac{k(x)}{e^x+1} = \cos(3x) \iff k'(x) = \cos(3x)$. On prend $k(x) = \frac13\sin(3x)$ : $y_p(x) = \dfrac{\sin(3x)}{3(e^x+1)}$.
> $S = \Big\{ x \mapsto \dfrac k{e^x+1} + \dfrac{\sin(3x)}{3(e^x+1)},\ k \in \mathbb{R} \Big\}$.

## Exercice 4 : étude locale de fonctions
Type : petit o, équivalents et développements limités (manipulation) · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/10
Formules : $f = o(x^n) \iff f(x) = x^n\varepsilon(x)$, $\varepsilon \to 0$ ; $o(x^3) \Rightarrow o(x^2)$ (pas l'inverse) ; $o(x^p) + o(x^q) = o(x^{\min(p,q)})$ ; $f \sim$ premier terme non nul du DL ; $f \sim g \iff f - g = o(g)$ ; $\lim \frac{f}{x^n} = a \neq 0 \iff f \sim ax^n$

Les questions sont indépendantes.

1. Soient $x_0 \in \mathbb{R} \cup \{+\infty, -\infty\}$ et $f$ et $g$ deux fonctions définies au voisinage de $x_0$ et ne s'y annulant pas. Donner deux définitions mathématiques de chacune des notations $f = o(g)$ et $f \sim g$ au voisinage de $x_0$.
> $f = o(g)$ en $x_0$ $\iff$ $f(x) = g(x)\varepsilon(x)$ avec $\lim_{x \to x_0}\varepsilon(x) = 0$ $\iff$ $\lim_{x \to x_0}\frac{f(x)}{g(x)} = 0$.
> $f \sim g$ en $x_0$ $\iff$ $f(x) = g(x)(1 + \varepsilon(x))$ avec $\lim_{x \to x_0}\varepsilon(x) = 0$ $\iff$ $\lim_{x \to x_0}\frac{f(x)}{g(x)} = 1$.

2. Donner un équivalent en 0 ET en $+\infty$ de $P(x) = 2x^3 - x^2 + 6x$. Justifiez vos réponses.
> $\frac{P(x)}{2x^3} = 1 - \frac1{2x} + \frac3{x^2} \to 1$ en $+\infty$ : $P(x) \sim 2x^3$ en $+\infty$. $\frac{P(x)}{6x} = \frac{x^2}3 - \frac x6 + 1 \to 1$ en 0 : $P(x) \sim 6x$ en 0.

3. - (a) Donner un équivalent en 0 de $f(x) = \sin(2x)$. Justifier brièvement.
   - (b) Donner un équivalent en 0 de $g(x) = 1 - e^{-2x}$. Justifier brièvement.
   - (c) Donner un équivalent en 0 de $h(x) = f(x) \times g(x)$.
   - (d) Donner un équivalent en 0 de $k(x) = f(x) - g(x)$. Justifier.
> (a) $\sin(2x) = 2x + o(x)$ : $f(x) \sim 2x$.
> (b) $g(x) = 1 - (1 - 2x + o(x)) = 2x + o(x)$ : $g(x) \sim 2x$.
> (c) $h(x) \sim 2x \times 2x = 4x^2$.
> (d) Il faut pousser les DL : $k(x) = 2x + o(x^2) - \Big(1 - \big(1 - 2x + \frac{4x^2}2 + o(x^2)\big)\Big) = 2x^2 + o(x^2)$ : $k(x) \sim 2x^2$.

4. Soit $\alpha \in \mathbb{R}$. Trouver une condition nécessaire et suffisante sur $\alpha$ pour avoir $\dfrac{\ln(x)}{x^2} = o\Big(\dfrac1{x^\alpha}\Big)$ en $+\infty$.
> $\dfrac{\ln(x)/x^2}{1/x^\alpha} = x^{\alpha-2}\ln(x)$. Si $\alpha > 2$ : limite $+\infty$. Si $\alpha = 2$ : $\ln x \to +\infty$. Si $\alpha < 2$ : limite 0 par croissances comparées. Condition : $\alpha < 2$.

5. Donner le développement limité à l'ordre 3 en 0 d'une fonction $f$ vérifiant $f(x) \sim -2x$ en 0 ET $f(x) + 2x = o(x^3)$ en 0.
> $f(x) = -2x + o(x^3)$.

## Exercice 5 : développements limités
Type : développements limités usuels et composés · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/8
Formules : $e^u = \sum \frac{u^k}{k!}$ ; $\cos u = 1 - \frac{u^2}2 + \frac{u^4}{24}$ ; $\sin u = u - \frac{u^3}6$ ; $\ln(1+u) = u - \frac{u^2}2 + \frac{u^3}3 - \frac{u^4}4$ ; $\sqrt{1+u} = 1 + \frac u2 - \frac{u^2}8 + \frac{u^3}{16} - \frac{5u^4}{128}$ ; $(1+u)^\alpha = 1 + \alpha u + \frac{\alpha(\alpha-1)}2u^2$ ; produit tronqué ; composition : poser $u$, calculer $u^2$ à l'ordre voulu ; $1 + \cos 2x = 2\cos^2 x$

1. Donner le développement limité en 0 à l'ordre 4 de $f(x) = \cos(x) \times \sqrt{1 - x^2}$.
> $f(x) = \Big(1 - \frac{x^2}2 + \frac{x^4}{24} + o(x^4)\Big)\Big(1 + \frac12(-x^2) + \frac{\frac12(\frac12 - 1)}2(-x^2)^2 + o(x^4)\Big) = \Big(1 - \frac{x^2}2 + \frac{x^4}{24}\Big)\Big(1 - \frac{x^2}2 - \frac{x^4}8\Big) + o(x^4) = 1 - x^2 + \dfrac{x^4}6 + o(x^4)$.

2. Donner le développement limité en 0 à l'ordre 3 de $g(x) = \ln(2 - \sin(x))$.
> $g(x) = \ln\Big(2 - x + \frac{x^3}6 + o(x^3)\Big) = \ln 2 + \ln\Big(1 - \frac x2 + \frac{x^3}{12} + o(x^3)\Big)$. Avec $u = -\frac x2 + \frac{x^3}{12} + o(x^3) \to 0$, $u^2 = \frac{x^2}4 + o(x^3)$, $u^3 = -\frac{x^3}8 + o(x^3)$ et $\ln(1+u) = u - \frac{u^2}2 + \frac{u^3}3 + o(u^3)$ : $g(x) = \ln 2 - \dfrac x2 - \dfrac{x^2}8 + \dfrac{x^3}{24} + o(x^3)$.

## Exercice 6 : calcul de limites
Type : développements limités, limite par équivalents · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/9
Formules : en 0 : $e^x = 1 + x + \frac{x^2}2 + \frac{x^3}6 + o(x^3)$ ; $\ln(1+x) = x - \frac{x^2}2 + o(x^2)$ ; $\cos x = 1 - \frac{x^2}2 + o(x^3)$ ; $\sin x = x - \frac{x^3}6 + o(x^3)$ ; $\frac1{1-x} = 1 + x + x^2 + x^3 + o(x^3)$ ; produit de DL tronqué à l'ordre ; $a^b = e^{b\ln a}$ ; $f \sim g \Rightarrow$ même limite

1. Calculer $\displaystyle\lim_{x \to +\infty} \left(1 + \sin\Big(\frac1x\Big)\right)^x$. Vous prendrez soin de votre rédaction.
> $\big(1 + \sin\frac1x\big)^x = e^{x\ln(1 + \sin\frac1x)} = e^{x\ln(1 + \frac1x + o(\frac1x))} = e^{x(\frac1x + o(\frac1x))} = e^{1 + o(1)}$. La limite vaut $e$.

2. Soient $f$, $g$ et $h$ trois fonctions telles qu'au voisinage de 0 : $f(x) = 1 - 3x + \dfrac{x^3}4 + o(x^3)$, $g(x) = -3 - x^2 + o(x^2)$ et $h(x) = 1 + 3x + o(x)$. Donner $\displaystyle\lim_{x \to 0} \frac{f(x) - xg(x) - 1}{h(x) - 1}$. Vous prendrez soin de votre rédaction.
> $f(x) - xg(x) - 1 = 1 - 3x + \frac{x^3}4 + 3x + x^3 - 1 + o(x^3) = \frac{5x^3}4 + o(x^3) \sim \frac{5x^3}4$. $h(x) - 1 = 3x + o(x) \sim 3x$. Le quotient est équivalent à $\frac{5x^2}{12} \to 0$ : la limite vaut 0.
