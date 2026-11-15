# Midterm exam (S1) — November 2017 (subject, EN)

- Source : `raw/S1/Midterms/Maths PC/2022/midterm-2022-s1-maths-subject-en.pdf` (scan, 8 pages)
- Date réelle : novembre 2017 (S1 17/18, dossier promo 2022). Version anglaise de `midterm-2022-s1-maths-subject-fr.md` ; corrigé : `midterm-2022-s1-maths-correction-fr.md`.
- Duration: three hours. Documents and calculators not allowed.

## Exercise 1 (2 points)
Type : dériver une composée · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/1
Formules : $(g \circ u)' = u' \times g' \circ u$ ; $(e^u)' = u'e^u$ ; $(\sqrt u)' = \frac{u'}{2\sqrt u}$ ; $(u^n)' = nu'u^{n-1}$ ; $(\ln u)' = \frac{u'}u$

Let $f$ and $g$ be the functions defined by $f(x) = \sqrt{\ln^{10}(\sin(x)) + 1}$ and $g(x) = \sin\left(\arctan(\sqrt x)\right)$.
Calculate $f'(x)$ and $g'(x)$ (no need to refer to domains of definition). N.B.: do not try to simplify the results.

## Exercise 2 (3 points)
Type : forme exponentielle, argument · ECUE : HP (nombres complexes, hors programme 2031)
Formules : $z = |z|e^{i\theta}$ ; $e^{i\theta}e^{i\varphi} = e^{i(\theta + \varphi)}$ ; $\frac{e^{i\theta}}{e^{i\varphi}} = e^{i(\theta - \varphi)}$ ; $(re^{i\theta})^n = r^ne^{in\theta}$ ; $-i = e^{-i\pi/2}$

Let $z = 1 + \sqrt3 + i(1 - \sqrt3)$.
1. Determine $z^2$ in exponential form.
2. Deduce from this the modulus and an argument of $z$.

## Exercise 3 (6 points)
Type : intégrales (primitive directe, IPP, changement de variable) · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/13
Formules : $\int u'u = \frac{u^2}2$ ($u = \arctan$, $u' = \frac1{1+x^2}$) ; IPP : $\int uv' = [uv] - \int u'v$ avec $u = \ln x$, $v' = \frac1{x^2}$, $v = -\frac1x$ ; $u = \ln t \Rightarrow du = \frac{dt}t$ ; $u = \sqrt x \Rightarrow dx = 2u\,du$ ; $\int \frac{du}{1+u^2} = \arctan u$ ; $1 - u^2 = (1-u)(1+u)$

1. Determine, using neither an integration by parts nor a substitution, $I = \displaystyle\int_0^1 \frac{\arctan(x)}{1 + x^2}\,dx$.
2. Using an integration by parts, determine $J = \displaystyle\int_1^e \frac{\ln(x)}{x^2}\,dx$.
3. Using the substitution $u = \ln(t)$, determine $K = \displaystyle\int_1^e \frac{dt}{t(1 + \ln^2(t))}$.
4. Using the substitution $u = \sqrt x$, determine $L = \displaystyle\int_0^1 \frac{1 - x}{1 + \sqrt x}\,dx$.

## Exercise 4 (4 points)
Type : équation du second degré à coefficients complexes · ECUE : HP (nombres complexes, hors programme 2031)
Formules : $\Delta = b^2 - 4ac$ ; racine carrée $\delta = a + ib$ de $\Delta$ : $a^2 - b^2 = \mathrm{Re}\,\Delta$, $a^2 + b^2 = |\Delta|$, $2ab = \mathrm{Im}\,\Delta$ ; $z = \frac{-b \pm \delta}{2a}$

Let $(E)$ be the following equation: $z^2 - (5 + 3i)z + 2 + 9i = 0$.
1. Show that $\Delta = 8 - 6i$.
2. Determine a square root of $\Delta$.
3. Deduce from this the solutions in $\mathbb{C}$ of the equation $(E)$.

## Exercise 5 (4 points)
Type : développements limités, limite par équivalents · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/9
Formules : en 0 : $e^x = 1 + x + \frac{x^2}2 + \frac{x^3}6 + o(x^3)$ ; $\ln(1+x) = x - \frac{x^2}2 + o(x^2)$ ; $\cos x = 1 - \frac{x^2}2 + o(x^3)$ ; $\sin x = x - \frac{x^3}6 + o(x^3)$ ; $\frac1{1-x} = 1 + x + x^2 + x^3 + o(x^3)$ ; produit de DL tronqué à l'ordre ; $a^b = e^{b\ln a}$ ; $f \sim g \Rightarrow$ même limite

1. Determine the Taylor expansion at 0 at order 2 of $e^x\ln(e + ex)$.
2. Determine $\lim_{x \to 0} \left(1 + \sin(x)\right)^{1/x}$.
3. Determine $\lim_{x \to 0} \dfrac{e^x - \cos(x) - \sin(x)}{x^2}$.

## Exercise 6 (2 points)
Type : théorème des valeurs intermédiaires · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/2
Formules : TVI : $f$ continue sur $[a,b]$, $k$ entre $f(a)$ et $f(b)$ $\Rightarrow \exists c \in [a,b]$, $f(c) = k$ ; si $f(a)f(b) < 0$, $\exists c \in ]a,b[$, $f(c) = 0$

Let $f : [0, 1] \to \mathbb{R}$ be continuous such that $f(0) = f(1)$. Show that there exists $c \in \left[0, \frac12\right]$ such that $f(c) = f\left(c + \frac12\right)$.
