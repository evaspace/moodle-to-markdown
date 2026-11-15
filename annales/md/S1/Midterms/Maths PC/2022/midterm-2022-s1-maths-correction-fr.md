# Corrigé du contrôle 1 — novembre 2017

- Source : `raw/S1/Midterms/Maths PC/2022/midterm-2022-s1-maths-correction-fr.pdf` (scan, 3 pages ; couche OCR inexploitable)
- Date réelle : novembre 2017 (S1 17/18, dossier promo 2022). Sujet : `midterm-2022-s1-maths-subject-fr.md`.

## Exercice 1 (2 points)
Type : dériver une composée · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/1
Formules : $(g \circ u)' = u' \times g' \circ u$ ; $(e^u)' = u'e^u$ ; $(\sqrt u)' = \frac{u'}{2\sqrt u}$ ; $(u^n)' = nu'u^{n-1}$ ; $(\ln u)' = \frac{u'}u$

$f'(x) = \dfrac{1}{2\sqrt{\ln^{10}(\sin(x)) + 1}} \cdot 10\ln^9(\sin(x)) \cdot \dfrac1{\sin(x)} \cdot \cos(x)$
$g'(x) = \cos\left(\arctan(\sqrt x)\right) \cdot \dfrac1{1 + x} \cdot \dfrac1{2\sqrt x}$

## Exercice 2 (3 points)
Type : forme exponentielle, argument · ECUE : HP (nombres complexes, hors programme 2031)
Formules : $z = |z|e^{i\theta}$ ; $e^{i\theta}e^{i\varphi} = e^{i(\theta + \varphi)}$ ; $\frac{e^{i\theta}}{e^{i\varphi}} = e^{i(\theta - \varphi)}$ ; $(re^{i\theta})^n = r^ne^{in\theta}$ ; $-i = e^{-i\pi/2}$

1. $z^2 = 4\sqrt3 - 4i = 8\left(\frac{\sqrt3}2 - \frac i2\right) = 8e^{-i\pi/6}$.
2. $z = re^{i\theta}$ ($r$ module, $\theta$ argument). $z^2 = r^2e^{2i\theta}$ d'où $r^2 = 8$ et $2\theta = -\frac\pi6 + 2k\pi$, $k \in \mathbb{Z}$.
Comme $r > 0$, $\mathrm{Re}(z) > 0$ et $\mathrm{Im}(z) < 0$ : le module et un argument de $z$ sont $2\sqrt2$ et $-\frac\pi{12}$.

## Exercice 3 (6 points)
Type : intégrales (primitive directe, IPP, changement de variable) · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/13
Formules : $\int u'u = \frac{u^2}2$ ($u = \arctan$, $u' = \frac1{1+x^2}$) ; IPP : $\int uv' = [uv] - \int u'v$ avec $u = \ln x$, $v' = \frac1{x^2}$, $v = -\frac1x$ ; $u = \ln t \Rightarrow du = \frac{dt}t$ ; $u = \sqrt x \Rightarrow dx = 2u\,du$ ; $\int \frac{du}{1+u^2} = \arctan u$ ; $1 - u^2 = (1-u)(1+u)$

1. $I = \displaystyle\int_0^1 \frac{\arctan x}{1 + x^2}\,dx = \frac12\left[\arctan^2 x\right]_0^1 = \frac12\left(\frac\pi4\right)^2 = \frac{\pi^2}{32}$.
2. IPP avec $u(x) = \ln x$, $v'(x) = \frac1{x^2}$ : $J = \left[-\dfrac{\ln x}x\right]_1^e - \displaystyle\int_1^e -\frac1{x^2}\,dx = -\frac1e - \left[\frac1x\right]_1^e = 1 - \frac2e$.
3. $u = \ln t$, $du = \frac{dt}t$ : $K = \displaystyle\int_0^1 \frac{du}{1 + u^2} = [\arctan u]_0^1 = \frac\pi4$.
4. $u = \sqrt x$, $x = u^2$, $dx = 2u\,du$ : $L = \displaystyle\int_0^1 \frac{1 - u^2}{1 + u}\,2u\,du = 2\int_0^1 u(1 - u)\,du$ (car $1 - u^2 = (1+u)(1-u)$) $= 2\left[\frac{u^2}2 - \frac{u^3}3\right]_0^1 = \frac13$.

## Exercice 4 (4 points)
Type : équation du second degré à coefficients complexes · ECUE : HP (nombres complexes, hors programme 2031)
Formules : $\Delta = b^2 - 4ac$ ; racine carrée $\delta = a + ib$ de $\Delta$ : $a^2 - b^2 = \mathrm{Re}\,\Delta$, $a^2 + b^2 = |\Delta|$, $2ab = \mathrm{Im}\,\Delta$ ; $z = \frac{-b \pm \delta}{2a}$

1. $\Delta = (5 + 3i)^2 - 4(2 + 9i) = 8 - 6i$.
2. $\delta = a + ib$, $\delta^2 = 8 - 6i$ : $a^2 - b^2 = 8$, $a^2 + b^2 = \sqrt{8^2 + 6^2} = 10$, $2ab = -6$ ($ab < 0$). Donc $\delta = 3 - i$.
3. $z = \frac12(5 + 3i + 3 - i)$ ou $z = \frac12(5 + 3i - 3 + i)$ : $z = 4 + i$ ou $z = 1 + 2i$.

## Exercice 5 (4 points)
Type : développements limités, limite par équivalents · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/9
Formules : en 0 : $e^x = 1 + x + \frac{x^2}2 + \frac{x^3}6 + o(x^3)$ ; $\ln(1+x) = x - \frac{x^2}2 + o(x^2)$ ; $\cos x = 1 - \frac{x^2}2 + o(x^3)$ ; $\sin x = x - \frac{x^3}6 + o(x^3)$ ; $\frac1{1-x} = 1 + x + x^2 + x^3 + o(x^3)$ ; produit de DL tronqué à l'ordre ; $a^b = e^{b\ln a}$ ; $f \sim g \Rightarrow$ même limite

1. $e^x\ln(e + ex) = e^x\ln(e(1 + x)) = e^x(1 + \ln(1 + x)) = \left(1 + x + \frac{x^2}2 + o(x^2)\right)\left(1 + x - \frac{x^2}2 + o(x^2)\right) = 1 + 2x + x^2 + o(x^2)$.
2. $(1 + \sin x)^{1/x} = e^{\ln(1 + \sin x)/x} = e^{\ln(1 + x + o(x))/x} = e^{(x + o(x))/x} = e^{1 + o(1)}$, donc $\lim_{x \to 0} (1 + \sin x)^{1/x} = e$.
3. $\dfrac{e^x - \cos x - \sin x}{x^2} = \dfrac{1 + x + \frac{x^2}2 - \left(1 - \frac{x^2}2\right) - x + o(x^2)}{x^2} = \dfrac{x^2 + o(x^2)}{x^2} = 1 + o(1)$, donc la limite vaut 1.

## Exercice 6 (2 points)
Type : théorème des valeurs intermédiaires · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/2
Formules : TVI : $f$ continue sur $[a,b]$, $k$ entre $f(a)$ et $f(b)$ $\Rightarrow \exists c \in [a,b]$, $f(c) = k$ ; si $f(a)f(b) < 0$, $\exists c \in ]a,b[$, $f(c) = 0$

Soit $g(x) = f(x) - f\left(x + \frac12\right)$ pour $x \in [0, \frac12]$ ; $g$ est continue sur $[0, \frac12]$ car $f$ l'est sur $[0, \frac12]$ et sur $[\frac12, 1]$.
$g(0) = f(0) - f(\frac12)$ et $g(\frac12) = f(\frac12) - f(1) = f(\frac12) - f(0) = -g(0)$.
$g(0)$ et $g(\frac12)$ sont de signes contraires : par le TVI, il existe $c \in [0, \frac12]$ tel que $g(c) = 0$, c'est-à-dire $f(c) = f\left(c + \frac12\right)$.
