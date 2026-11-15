# Corrigé du contrôle 1 — octobre 2016

- Source : `raw/S1/Midterms/Maths PC/2021/midterm-2021-s1-maths-correction-fr.pdf` (scan, 2 pages)
- Date réelle : octobre 2016 (S1 16/17, dossier promo 2021). Sujet absent du dépôt : les énoncés ci-dessous sont reconstitués d'après le corrigé.

## Exercice 1 (2 points)
Type : dériver une composée · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/1
Formules : $(g \circ u)' = u' \times g' \circ u$ ; $(e^u)' = u'e^u$ ; $(\sqrt u)' = \frac{u'}{2\sqrt u}$ ; $(u^n)' = nu'u^{n-1}$ ; $(\ln u)' = \frac{u'}u$

Énoncé reconstitué : dériver $f(x) = \dfrac1{\ln(\ln(\ln x))}$ et $g(x) = \sqrt{\sin^{2016}(x) + 2^x}$.

$f'(x) = -\dfrac{1}{\left(\ln(\ln(\ln x))\right)^2} \cdot \dfrac1{\ln(\ln x)} \cdot \dfrac1{\ln x} \cdot \dfrac1x$
$g'(x) = \dfrac{1}{2\sqrt{\sin^{2016}(x) + 2^x}}\left(2016\sin^{2015}(x)\cos(x) + \ln(2)\,2^x\right)$

## Exercice 2 (4 points)
Type : forme exponentielle, argument · ECUE : HP (nombres complexes, hors programme 2031)
Formules : $z = |z|e^{i\theta}$ ; $e^{i\theta}e^{i\varphi} = e^{i(\theta + \varphi)}$ ; $\frac{e^{i\theta}}{e^{i\varphi}} = e^{i(\theta - \varphi)}$ ; $(re^{i\theta})^n = r^ne^{in\theta}$ ; $-i = e^{-i\pi/2}$

Énoncé reconstitué : $z_1 = \sqrt6 - i\sqrt2$, $z_2 = 2 - 2i$ ; calculer $\frac{z_1}{z_2}$ sous forme algébrique puis exponentielle, en déduire $\cos\frac\pi{12}$ et $\sin\frac\pi{12}$.

1. $\dfrac{z_1}{z_2} = \dfrac{(\sqrt6 - i\sqrt2)(2 + 2i)}8 = \dfrac{\sqrt6 + \sqrt2}4 + i\dfrac{\sqrt6 - \sqrt2}4$.
2. $z_1 = \sqrt2(\sqrt3 - i) = 2\sqrt2 e^{-i\pi/6}$, $z_2 = 2\sqrt2\left(\frac{\sqrt2}2 - i\frac{\sqrt2}2\right) = 2\sqrt2 e^{-i\pi/4}$. Ainsi $\dfrac{z_1}{z_2} = e^{-i\pi/6 + i\pi/4} = e^{i\pi/12}$.
3. Donc $\cos\frac\pi{12} = \dfrac{\sqrt6 + \sqrt2}4$ et $\sin\frac\pi{12} = \dfrac{\sqrt6 - \sqrt2}4$.

## Exercice 3 (6 points)
Type : IPP et changement de variable · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/13
Formules : IPP : $\int_a^b uv' = [uv]_a^b - \int_a^b u'v$ ($u = \ln$, $v' = 1$) ; changement de variable : $x = \varphi(t)$, $dx = \varphi'(t)\,dt$, bornes transformées ; $t = \sqrt{1-x} \Rightarrow x = 1 - t^2$, $dx = -2t\,dt$ ; $t = e^{-x} \Rightarrow dx = -\frac{dt}t$ ; $\int \frac{dt}{1+t} = \ln(1+t)$ ; $\int t^n = \frac{t^{n+1}}{n+1}$

Énoncé reconstitué : calculer $I = \int_1^e \ln x\,dx$, $J = \int_1^e \ln^2 x\,dx$, $K = \int_0^1 x\sqrt{1-x}\,dx$ (poser $t = \sqrt{1-x}$), $L = \int_0^1 \frac{dx}{e^x + 1}$ (poser $t = e^{-x}$).

1. IPP avec $u(x) = \ln x$, $v'(x) = 1$ : $I = [x\ln x]_1^e - \int_1^e dx = e - [x]_1^e = 1$.
2. IPP avec $u(x) = \ln^2 x$, $v'(x) = 1$ : $J = [x\ln^2 x]_1^e - 2\int_1^e \ln x\,dx = e - 2$.
3. $t = \sqrt{1-x}$, $x = 1 - t^2$, $dx = -2t\,dt$ : $K = \int_1^0 (1-t^2)\,t\,(-2t)\,dt = 2\int_0^1 (t^2 - t^4)\,dt = \frac23 - \frac25 = \frac4{15}$.
4. $t = e^{-x}$, $x = -\ln t$, $dx = -\frac{dt}t$ : $L = \int_1^{1/e} \frac1{\frac1t + 1}\left(-\frac1t\right)dt = \int_{1/e}^1 \frac{dt}{1+t} = [\ln(1+t)]_{1/e}^1 = \ln 2 - \ln(1 + 1/e)$.

## Exercice 4 (3 points)
Type : équation du second degré à coefficients complexes · ECUE : HP (nombres complexes, hors programme 2031)
Formules : $\Delta = b^2 - 4ac$ ; racine carrée $\delta = a + ib$ de $\Delta$ : $a^2 - b^2 = \mathrm{Re}\,\Delta$, $a^2 + b^2 = |\Delta|$, $2ab = \mathrm{Im}\,\Delta$ ; $z = \frac{-b \pm \delta}{2a}$

Énoncé reconstitué : résoudre $z^2 - (4 + 3i)z + 1 + 5i = 0$.

1. $\Delta = (4 + 3i)^2 - 4(1 + 5i) = 3 + 4i$.
2. On cherche $\delta = a + ib$ avec $\delta^2 = 3 + 4i$ : $a^2 - b^2 = 3$, $a^2 + b^2 = \sqrt{3^2 + 4^2} = 5$, $2ab = 4$ ($ab > 0$). Donc $\delta = 2 + i$.
3. $z = \frac12(4 + 3i + 2 + i)$ ou $z = \frac12(4 + 3i - 2 - i)$ : $z = 3 + 2i$ ou $z = 1 + i$.

## Exercice 5 (4 points)
Type : développements limités, limite par équivalents · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/9
Formules : en 0 : $e^x = 1 + x + \frac{x^2}2 + \frac{x^3}6 + o(x^3)$ ; $\ln(1+x) = x - \frac{x^2}2 + o(x^2)$ ; $\cos x = 1 - \frac{x^2}2 + o(x^3)$ ; $\sin x = x - \frac{x^3}6 + o(x^3)$ ; $\frac1{1-x} = 1 + x + x^2 + x^3 + o(x^3)$ ; produit de DL tronqué à l'ordre ; $a^b = e^{b\ln a}$ ; $f \sim g \Rightarrow$ même limite

1. $\ln(1 - x) + e^{2x} = -x - \frac{x^2}2 + 1 + 2x + \frac{(2x)^2}{2!} + o(x^2) = 1 + x + \frac32x^2 + o(x^2)$.
2. $\dfrac{\cos(2x)}{1 - x} = \left(1 - \frac{(2x)^2}{2!} + o(x^3)\right)\left(1 + x + x^2 + x^3 + o(x^3)\right) = 1 + x - x^2 - x^3 + o(x^3)$.
3. $\dfrac{e^x - e^{-x}}{\ln(1+x)} = \dfrac{1 + x - (1 - x) + o(x)}{x + o(x)} \sim \dfrac{2x}x = 2$, donc $\lim_{x \to 0} \dfrac{e^x - e^{-x}}{\ln(1+x)} = 2$.

## Exercice 6 (2 points)
Type : théorème des valeurs intermédiaires · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/2
Formules : TVI : $f$ continue sur $[a,b]$, $k$ entre $f(a)$ et $f(b)$ $\Rightarrow \exists c \in [a,b]$, $f(c) = k$ ; si $f(a)f(b) < 0$, $\exists c \in ]a,b[$, $f(c) = 0$

Énoncé reconstitué : $f$ et $g$ continues sur $[a,b]$ avec $f(a) = g(b)$ et $f(b) = g(a)$ ; montrer qu'il existe $c \in [a,b]$ tel que $f(c) = g(c)$.

Soit $h = f - g$, continue sur $[a,b]$. $h(a) = g(b) - g(a)$ et $h(b) = g(a) - g(b) = -h(a)$ : $h(a)$ et $h(b)$ sont de signes contraires. Par le TVI, il existe $c \in [a,b]$ tel que $h(c) = 0$, i.e. $g(c) = f(c)$.
