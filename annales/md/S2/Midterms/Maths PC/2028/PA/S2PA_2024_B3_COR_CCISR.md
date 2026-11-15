# Examen S2PA-B3 CCISR — mars 2024 (corrigé, FR)

- Source : `raw/S2/Midterms/Maths PC/2028/PA/S2PA_2024_B3_COR_CCISR.pdf` (1 page)
- Date réelle : mars 2024 (S2 PA, bloc 3, dossier promo 2028). Pas de sujet séparé.
- Corrigé officiel : énoncé rappelé, solution en citation. Barème : 10 points.

## Exercice (10 points)
Type : intégrales (primitive directe, IPP, changement de variable) · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/13
Formules : $\int u'u = \frac{u^2}2$ ($u = \arctan$, $u' = \frac1{1+x^2}$) ; IPP : $\int uv' = [uv] - \int u'v$ avec $u = \ln x$, $v' = \frac1{x^2}$, $v = -\frac1x$ ; $u = \ln t \Rightarrow du = \frac{dt}t$ ; $u = \sqrt x \Rightarrow dx = 2u\,du$ ; $\int \frac{du}{1+u^2} = \arctan u$ ; $1 - u^2 = (1-u)(1+u)$

Les questions sont indépendantes.

1. (2 points) Calculer directement $I = \displaystyle\int_0^1 \frac{t^2 + 1}{2\sqrt{t^3 + 3t}}\,dt$.
> $I = \dfrac13\displaystyle\int_0^1 \frac{3t^2 + 3}{2\sqrt{t^3 + 3t}}\,dt$, de la forme $\dfrac{u'}{2\sqrt u}$. $I = \dfrac13\big[\sqrt{t^3 + 3t}\big]_0^1 = \dfrac13(\sqrt4 - \sqrt0) = \dfrac23$.

2. (4 points) Via une intégration par parties dont vous rappellerez la formule générale, calculer $J = \displaystyle\int_0^{\frac\pi{12}} x\sin(3x)\,dx$.
> Pour $u$, $v$ de classe $C^1$ sur $[a,b]$ : $\int_a^b u(x)v'(x)\,dx = [u(x)v(x)]_a^b - \int_a^b u'(x)v(x)\,dx$. On pose $u(x) = x$, $v'(x) = \sin(3x)$, $u'(x) = 1$, $v(x) = -\frac13\cos(3x)$.
> $J = \Big[-\dfrac x3\cos(3x)\Big]_0^{\frac\pi{12}} + \dfrac13\displaystyle\int_0^{\frac\pi{12}} \cos(3x)\,dx = -\dfrac\pi{36} \times \dfrac{\sqrt2}2 + \dfrac13\Big[\dfrac{\sin(3x)}3\Big]_0^{\frac\pi{12}} = -\dfrac{\sqrt2\,\pi}{72} + \dfrac{\sqrt2}{18}$.

3. (4 points) Calculer $K = \displaystyle\int_0^{\ln(\sqrt3)} \frac1{e^{-t} + e^t}\,dt$ en posant $x = e^t$.
> $x = e^t \iff t = \ln x$, $dt = \dfrac{dx}x$. $t = 0 \Rightarrow x = 1$ ; $t = \ln\sqrt3 \Rightarrow x = \sqrt3$. $K = \displaystyle\int_1^{\sqrt3} \frac1{\frac1x + x} \times \frac1x\,dx = \int_1^{\sqrt3} \frac{dx}{1 + x^2} = \big[\arctan x\big]_1^{\sqrt3} = \frac\pi3 - \frac\pi4 = \frac\pi{12}$.
