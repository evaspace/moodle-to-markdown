# Examen S2-B3 APEF — mars 2026 (corrigé, FR)

- Source : `raw/S2/Midterms/Maths PC/2030/PC/APEF/midterms-2030-s2-apef-correction-fr.pdf` (4 pages)
- Date réelle : mars 2026 (S2, bloc 3, dossier promo 2030). Pas de sujet séparé.
- Corrigé officiel : énoncé rappelé, solution en citation.

## Exercice 1 : polynômes
Type : divisibilité de polynômes, multiplicité, factorisation dans $\mathbb{R}[X]$ et $\mathbb{C}[X]$ · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/9
Formules : $P(a) = 0 \iff X - a \mid P$ ; racine d'ordre $\geqslant 2$ $\iff P(a) = P'(a) = 0$ ; ordre exactement $m$ : $P^{(m)}(a) \neq 0$ ; $(X - a)^m \mid P$, $(X - a)^{m+1} \nmid P$ ; $X^2 + 1 = (X - i)(X + i)$ ; $\Delta < 0 \Rightarrow$ irréductible dans $\mathbb{R}[X]$

Les deux questions sont indépendantes.

1. Soit $A(X) = X^4 + 2X^2 + 8X + 5$.
   - (a) Montrer que $-1$ est une racine de $A$. Trouver $\alpha \in \mathbb{N}$ tel que $(X+1)^\alpha$ divise $A$ et $(X+1)^{\alpha+1}$ ne divise pas $A$.
   - (b) Après avoir effectué la division euclidienne de $A$ par $(X+1)^\alpha$, écrire $A$ comme produit de polynômes irréductibles d'une part dans $\mathbb{R}[X]$, d'autre part dans $\mathbb{C}[X]$.
> (a) $A(-1) = 1 + 2 - 8 + 5 = 0$. $A'(X) = 4X^3 + 4X + 8$, $A'(-1) = 0$. $A''(X) = 12X^2 + 4$, $A''(-1) = 16 \neq 0$. $-1$ est racine d'ordre exactement 2 : $\alpha = 2$.
> (b) $A(X) = (X+1)^2(X^2 - 2X + 5)$. Le discriminant de $X^2 - 2X + 5$ vaut $-16 < 0$ : irréductible dans $\mathbb{R}[X]$. Dans $\mathbb{C}[X]$ : $A(X) = (X+1)^2(X - 1 - 2i)(X - 1 + 2i)$.

2. Soit $P \in \mathbb{R}[X]$, de degré 3, vérifiant $(X-1)^2 \mid (P(X) + 1)$ et $X^2 \mid (P(X) - 1)$.
   - (a) Que signifient les deux affirmations précédentes ? En déduire que $P(1) = -1$ et $P(0) = 1$.
   - (b) Expliquer pourquoi $X \mid P'$ et $(X-1) \mid P'$. En déduire que $X(X-1) \mid P'$.
   - (c) De ce qui précède, en déduire que $P'(X) = aX^2 - aX$ avec $a \in \mathbb{R}$.
   - (d) En déduire : $\exists b \in \mathbb{R}$ tel que $P(X) = a\dfrac{X^3}3 - a\dfrac{X^2}2 + b$. En utilisant la question 2.(a), trouver $a$ et $b$.
> (a) $\exists (Q_1, Q_2) \in \mathbb{R}[X]^2$, $P(X) + 1 = (X-1)^2Q_1(X)$ et $P(X) - 1 = X^2Q_2(X)$. En $X = 1$ : $P(1) = -1$. En $X = 0$ : $P(0) = 1$.
> (b) 1 est racine d'ordre au moins 2 de $P + 1$, donc racine de sa dérivée $P'$ : $(X-1) \mid P'$. De même 0 est racine de $(P - 1)' = P'$ : $X \mid P'$. Racines distinctes : $X(X-1) \mid P'$.
> (c) $P'(X) = X(X-1)Q_3(X)$ et $\deg P' = 2$, donc $\deg Q_3 = 0$ : $P'(X) = aX(X-1) = aX^2 - aX$.
> (d) En primitivant : $P(X) = a\frac{X^3}3 - a\frac{X^2}2 + b$. $P(0) = 1$ donne $b = 1$. $P(1) = -1$ donne $\frac a3 - \frac a2 + 1 = -1$, soit $a = 12$. $P(X) = 4X^3 - 6X^2 + 1$.

## Exercice 2 : équations différentielles
Type : EDO linéaires 1er ordre (variation de la constante) et 2nd ordre · ECUE : APIS (EDO) · Niveau : maths-s1-apis-edo/11
Formules : $y' + a(x)y = 0 \Rightarrow y = ke^{-A(x)}$, $A' = a$ ; solution générale = homogène + particulière ; variation de la constante $y_p = k(x)y_0(x)$ ; $ay'' + by' + cy = 0$ : $ar^2 + br + c = 0$, racine double $r$ : $y = (k_1x + k_2)e^{rx}$ ; second membre $P(x)e^{rx}$ : $y_p = Q(x)e^{rx}$

Les questions sont indépendantes.

1. Résoudre dans $\mathbb{R}$ l'équation différentielle $(E)$ : $\dfrac12y'' - y' + 5y = -\pi$.
> Équation caractéristique $\frac12r^2 - r + 5 = 0$, $\Delta = 1 - 10 = -9$, racines $1 \pm 3i$. Solution particulière évidente $y_p : x \mapsto -\frac\pi5$. $S = \big\{ x \mapsto e^x(k_1\cos(3x) + k_2\sin(3x)) - \frac\pi5,\ (k_1,k_2) \in \mathbb{R}^2 \big\}$.

2. Résoudre, sur $I = ]-1, +\infty[$, $(E)$ : $(x+1)y' - 2y = (x+1)^3\cos(3x)$.
> $(E_0)$ : $y_0(x) = ke^{-\int \frac{-2}{x+1}dx} = ke^{2\ln|x+1|} = k(x+1)^2$. Variation de la constante : $y_p(x) = k(x)(x+1)^2$, $y_p'(x) = k'(x)(x+1)^2 + 2k(x)(x+1)$ ; en reportant, $(x+1)^3k'(x) = (x+1)^3\cos(3x)$, donc $k'(x) = \cos(3x)$, $k(x) = \frac{\sin(3x)}3$. $S = \big\{ x \mapsto k(x+1)^2 + (x+1)^2\frac{\sin(3x)}3,\ k \in \mathbb{R} \big\}$.

## Exercice 3 : étude locale de fonctions
Type : petit o, équivalents et développements limités (manipulation) · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/10
Formules : $f = o(x^n) \iff f(x) = x^n\varepsilon(x)$, $\varepsilon \to 0$ ; $o(x^3) \Rightarrow o(x^2)$ (pas l'inverse) ; $o(x^p) + o(x^q) = o(x^{\min(p,q)})$ ; $f \sim$ premier terme non nul du DL ; $f \sim g \iff f - g = o(g)$ ; $\lim \frac{f}{x^n} = a \neq 0 \iff f \sim ax^n$

Les questions sont indépendantes.

1. Soient $x_0 \in \mathbb{R} \cup \{+\infty, -\infty\}$ et $f$ et $g$ deux fonctions définies au voisinage de $x_0$ et ne s'y annulant pas. Donner deux définitions mathématiques de chacune des notations $f = o(g)$ et $f \sim g$ au voisinage de $x_0$.
> $f \sim g \iff \lim_{x \to x_0}\frac{f(x)}{g(x)} = 1 \iff f(x) = g(x)(1 + \varepsilon(x))$ avec $\lim_{x \to x_0}\varepsilon(x) = 0$.
> $f = o(g) \iff \lim_{x \to x_0}\frac{f(x)}{g(x)} = 0 \iff f(x) = g(x)\varepsilon(x)$ avec $\lim_{x \to x_0}\varepsilon(x) = 0$.

2. La notation $f(x) = o(g(x))$ peut s'écrire aussi $f(x) \ll g(x)$. Compléter par un des symboles $\ll$, $\gg$ ou $\sim$ : $2x^2 \dots x$, $(x^3 - 3x^2 + x) \dots x$ et $(x^3 - 3x^2 + x) \dots x^3$, au voisinage de 0 puis au voisinage de $+\infty$.
> En 0 : $2x^2 \ll x$, $(x^3 - 3x^2 + x) \sim x$, $(x^3 - 3x^2 + x) \gg x^3$.
> En $+\infty$ : $2x^2 \gg x$, $(x^3 - 3x^2 + x) \gg x$, $(x^3 - 3x^2 + x) \sim x^3$.

3. Soient $f$ et $g$ deux fonctions telles qu'au voisinage de 0 : $f(x) = x - \dfrac{x^2}2 + o(x^2)$ et $g(x) = -1 + x + 3x^2 - x^3 + o(x^3)$.
   - (a) Donner un équivalent (le plus simple possible) en 0 de $f(x)$. Justifier brièvement en repartant de la définition.
   - (b) Donner un équivalent (autre que la fonction elle-même) en 0 de $g(x) + 1$ et de $h(x) = \sin(x) \times f(x) \times (g(x) + 1)$.
   - (c) A-t-on assez d'informations pour donner le développement limité en 0 de $f(x) + g(x)$ à l'ordre 1 ? À l'ordre 2 ? À l'ordre 3 ? Donner le développement limité à l'ordre indiqué quand la réponse est oui.
> (a) $f(x) = x - \frac{x^2}2 + x^2\varepsilon(x)$, donc $\frac{f(x)}x = 1 - \frac x2 + x\varepsilon(x) \to 1$ : $f(x) \sim x$.
> (b) $g(x) + 1 \sim x$ ; $h(x) \sim x \times x \times x = x^3$.
> (c) Ordre 1 : $f(x) + g(x) = -1 + 2x + o(x)$. Ordre 2 : $f(x) + g(x) = -1 + 2x + \frac{5x^2}2 + o(x^2)$. Ordre 3 : non, on ne connaît pas le DL de $f$ à l'ordre 3.

## Exercice 4 : développements limités
Type : développements limités usuels et composés · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/8
Formules : $e^u = \sum \frac{u^k}{k!}$ ; $\cos u = 1 - \frac{u^2}2 + \frac{u^4}{24}$ ; $\sin u = u - \frac{u^3}6$ ; $\ln(1+u) = u - \frac{u^2}2 + \frac{u^3}3 - \frac{u^4}4$ ; $\sqrt{1+u} = 1 + \frac u2 - \frac{u^2}8 + \frac{u^3}{16} - \frac{5u^4}{128}$ ; $(1+u)^\alpha = 1 + \alpha u + \frac{\alpha(\alpha-1)}2u^2$ ; produit tronqué ; composition : poser $u$, calculer $u^2$ à l'ordre voulu ; $1 + \cos 2x = 2\cos^2 x$

Dans cet exercice, vous prendrez soin de rappeler les développements limités usuels que vous utiliserez.

1. Donner le développement limité en 0 à l'ordre 3 de $f(x) = \cos(x)e^{-2x}$.
> $f(x) = \big(1 - \frac{x^2}2 + o(x^3)\big)\big(1 - 2x + 2x^2 - \frac43x^3 + o(x^3)\big) = 1 - 2x + \dfrac{3x^2}2 - \dfrac{x^3}3 + o(x^3)$.

2. - (a) Donner le développement limité en 0 à l'ordre 4 de $g(x) = \dfrac1{\sqrt{1 + x^2}}$.
   - (b) Donner le développement limité en 0 à l'ordre 4 de $h(x) = \ln(1 + g(x))$.
> (a) $g(x) = (1 + x^2)^{-\frac12} = 1 - \frac12x^2 + \frac{-\frac12(-\frac12 - 1)}2x^4 + o(x^4) = 1 - \dfrac{x^2}2 + \dfrac{3x^4}8 + o(x^4)$.
> (b) $h(x) = \ln\big(2 - \frac{x^2}2 + \frac{3x^4}8 + o(x^4)\big) = \ln 2 + \ln\big(1 - \frac{x^2}4 + \frac{3x^4}{16} + o(x^4)\big)$. Avec $u = -\frac{x^2}4 + \frac{3x^4}{16} + o(x^4) \to 0$ et $u^2 = \frac{x^4}{16} + o(x^4)$ : $h(x) = \ln 2 - \dfrac{x^2}4 + \dfrac{3x^4}{16} - \dfrac{x^4}{32} + o(x^4) = \ln 2 - \dfrac{x^2}4 + \dfrac{5x^4}{32} + o(x^4)$.

## Exercice 5 : calcul de limites
Type : développements limités, limite par équivalents · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/9
Formules : en 0 : $e^x = 1 + x + \frac{x^2}2 + \frac{x^3}6 + o(x^3)$ ; $\ln(1+x) = x - \frac{x^2}2 + o(x^2)$ ; $\cos x = 1 - \frac{x^2}2 + o(x^3)$ ; $\sin x = x - \frac{x^3}6 + o(x^3)$ ; $\frac1{1-x} = 1 + x + x^2 + x^3 + o(x^3)$ ; produit de DL tronqué à l'ordre ; $a^b = e^{b\ln a}$ ; $f \sim g \Rightarrow$ même limite

1. Calculer $\displaystyle\lim_{x \to 0} \frac{-1 + x + \ln(1 - x) + \cos(x)}{1 - (1 - x)^\pi}$. Vous prendrez soin de votre rédaction.
> $N(x) = -1 + x - x - \frac{x^2}2 + 1 - \frac{x^2}2 + o(x^2) = -x^2 + o(x^2) \sim -x^2$. $D(x) = 1 - (1 - \pi x + o(x)) = \pi x + o(x) \sim \pi x$. $\frac{N(x)}{D(x)} \sim -\frac x\pi \to 0$ : la limite vaut 0.

2. Calculer $\displaystyle\lim_{x \to +\infty} \left(1 + \sin\Big(\frac1x\Big)\right)^x$. Vous prendrez soin de votre rédaction.
> $\big(1 + \sin\frac1x\big)^x = e^{x\ln(1 + \sin\frac1x)} = e^{x\ln(1 + \frac1x + o(\frac1x))} = e^{x(\frac1x + o(\frac1x))} = e^{1 + o(1)}$. La limite vaut $e$. (Autre rédaction : poser $X = \frac1x \to 0$ et calculer $\lim_{X \to 0}(1 + \sin X)^{1/X}$.)
