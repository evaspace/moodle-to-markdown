# Contrôle 1 S1 — novembre 2017 (sujet, FR)

- Source : `raw/S1/Midterms/Maths PC/2022/midterm-2022-s1-maths-subject-fr.pdf` (scan, 8 pages)
- Date réelle : novembre 2017 (S1 17/18, dossier promo 2022). Corrigé : `midterm-2022-s1-maths-correction-fr.md`.
- Durée : trois heures. Documents et calculatrices non autorisés. Barème : 21 points.

## Exercice 1 (2 points)
Type : dériver une composée · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/1
Formules : $(g \circ u)' = u' \times g' \circ u$ ; $(e^u)' = u'e^u$ ; $(\sqrt u)' = \frac{u'}{2\sqrt u}$ ; $(u^n)' = nu'u^{n-1}$ ; $(\ln u)' = \frac{u'}u$

Soient $f$ et $g$ les fonctions définies par $f(x) = \sqrt{\ln^{10}(\sin(x)) + 1}$ et $g(x) = \sin\left(\arctan(\sqrt x)\right)$.
Calculer $f'(x)$ et $g'(x)$ (sans se préoccuper du domaine de définition). N.B. : n'essayez pas de simplifier les résultats.

## Exercice 2 (3 points)
Type : forme exponentielle, argument · ECUE : HP (nombres complexes, hors programme 2031)
Formules : $z = |z|e^{i\theta}$ ; $e^{i\theta}e^{i\varphi} = e^{i(\theta + \varphi)}$ ; $\frac{e^{i\theta}}{e^{i\varphi}} = e^{i(\theta - \varphi)}$ ; $(re^{i\theta})^n = r^ne^{in\theta}$ ; $-i = e^{-i\pi/2}$

Soit $z = 1 + \sqrt3 + i(1 - \sqrt3)$.
1. Déterminer $z^2$ sous forme exponentielle.
2. En déduire le module et un argument de $z$.

## Exercice 3 (6 points)
Type : intégrales (primitive directe, IPP, changement de variable) · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/13
Formules : $\int u'u = \frac{u^2}2$ ($u = \arctan$, $u' = \frac1{1+x^2}$) ; IPP : $\int uv' = [uv] - \int u'v$ avec $u = \ln x$, $v' = \frac1{x^2}$, $v = -\frac1x$ ; $u = \ln t \Rightarrow du = \frac{dt}t$ ; $u = \sqrt x \Rightarrow dx = 2u\,du$ ; $\int \frac{du}{1+u^2} = \arctan u$ ; $1 - u^2 = (1-u)(1+u)$

1. Déterminer, sans intégration par parties ni changement de variable, $I = \displaystyle\int_0^1 \frac{\arctan(x)}{1 + x^2}\,dx$.
2. Via une intégration par parties, déterminer $J = \displaystyle\int_1^e \frac{\ln(x)}{x^2}\,dx$.
3. Via le changement de variable $u = \ln(t)$, déterminer $K = \displaystyle\int_1^e \frac{dt}{t(1 + \ln^2(t))}$.
4. Via le changement de variable $u = \sqrt x$, déterminer $L = \displaystyle\int_0^1 \frac{1 - x}{1 + \sqrt x}\,dx$.

## Exercice 4 (4 points)
Type : équation du second degré à coefficients complexes · ECUE : HP (nombres complexes, hors programme 2031)
Formules : $\Delta = b^2 - 4ac$ ; racine carrée $\delta = a + ib$ de $\Delta$ : $a^2 - b^2 = \mathrm{Re}\,\Delta$, $a^2 + b^2 = |\Delta|$, $2ab = \mathrm{Im}\,\Delta$ ; $z = \frac{-b \pm \delta}{2a}$

Soit l'équation $(E)$ suivante : $z^2 - (5 + 3i)z + 2 + 9i = 0$.
1. Montrer que $\Delta = 8 - 6i$.
2. Déterminer une racine carrée de $\Delta$.
3. En déduire les solutions dans $\mathbb{C}$ de l'équation $(E)$.

## Exercice 5 (4 points)
Type : développements limités, limite par équivalents · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/9
Formules : en 0 : $e^x = 1 + x + \frac{x^2}2 + \frac{x^3}6 + o(x^3)$ ; $\ln(1+x) = x - \frac{x^2}2 + o(x^2)$ ; $\cos x = 1 - \frac{x^2}2 + o(x^3)$ ; $\sin x = x - \frac{x^3}6 + o(x^3)$ ; $\frac1{1-x} = 1 + x + x^2 + x^3 + o(x^3)$ ; produit de DL tronqué à l'ordre ; $a^b = e^{b\ln a}$ ; $f \sim g \Rightarrow$ même limite

1. Déterminer le développement limité en 0 à l'ordre 2 de $e^x\ln(e + ex)$.
2. Déterminer $\lim_{x \to 0} \left(1 + \sin(x)\right)^{1/x}$.
3. Déterminer $\lim_{x \to 0} \dfrac{e^x - \cos(x) - \sin(x)}{x^2}$.

## Exercice 6 (2 points)
Type : théorème des valeurs intermédiaires · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/2
Formules : TVI : $f$ continue sur $[a,b]$, $k$ entre $f(a)$ et $f(b)$ $\Rightarrow \exists c \in [a,b]$, $f(c) = k$ ; si $f(a)f(b) < 0$, $\exists c \in ]a,b[$, $f(c) = 0$

Soit $f : [0, 1] \to \mathbb{R}$ continue telle que $f(0) = f(1)$. Montrer qu'il existe $c \in \left[0, \frac12\right]$ tel que $f(c) = f\left(c + \frac12\right)$.
