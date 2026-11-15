# Contrôle S2 — mars 2022 (sujet, FR)

- Source : `raw/S2/Midterms/Maths PC/2026/midterm-2026-s2-maths-subject-fr.pdf` (9 pages)
- Date réelle : mars 2022 (dossier promo 2026). Corrigé : `midterm-2026-s2-maths-correction-fr.md`.
- Durée : 3 heures. Documents et calculatrices interdits. Barème sur 35 points, ramené à 20. 7 exercices.

## Exercice 1 (5,5 points)
Type : EDO linéaires 1er ordre (variation de la constante) et 2nd ordre · ECUE : APIS (EDO) · Niveau : maths-s1-apis-edo/11
Formules : $y' + a(x)y = 0 \Rightarrow y = ke^{-A(x)}$, $A' = a$ ; solution générale = homogène + particulière ; variation de la constante $y_p = k(x)y_0(x)$ ; $ay'' + by' + cy = 0$ : $ar^2 + br + c = 0$, racine double $r$ : $y = (k_1x + k_2)e^{rx}$ ; second membre $P(x)e^{rx}$ : $y_p = Q(x)e^{rx}$

1. Résoudre sur $I = ]0, +\infty[$ l'équation différentielle $(E)$ : $xy' + \dfrac12y = -2$.
2. Résoudre dans $\mathbb{R}$ l'équation différentielle $(E)$ : $2y'' + 8y' + 8y = 3e^{-2x}$.

## Exercice 2 (5 points)
Type : petit o, équivalents et développements limités (manipulation) · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/10
Formules : $f = o(x^n) \iff f(x) = x^n\varepsilon(x)$, $\varepsilon \to 0$ ; $o(x^3) \Rightarrow o(x^2)$ (pas l'inverse) ; $o(x^p) + o(x^q) = o(x^{\min(p,q)})$ ; $f \sim$ premier terme non nul du DL ; $f \sim g \iff f - g = o(g)$ ; $\lim \frac{f}{x^n} = a \neq 0 \iff f \sim ax^n$

Dans cet exercice, les questions sont indépendantes.
1. Soient $f$ et $g$ deux fonctions telles qu'au voisinage de 0 : $f(x) = o(x^3)$ et $g(x) = x^2\varepsilon(x)$ avec $\lim_{x \to 0} \varepsilon(x) = 0$.
   - (a) A-t-on $f(x) = o(x^2)$ au voisinage de 0 ? $f(x) = o(x^4)$ au voisinage de 0 ? Justifier.
   - (b) Déterminer le plus grand entier naturel $n$ pour lequel on peut affirmer que $f(x) - 2g(x) = o(x^n)$ au voisinage de 0.
2. Soient $f$ et $g$ deux fonctions telles qu'au voisinage de 0 : $f(x) = 1 + x + x^2 + o(x^3)$ et $g(x) = 2x + x^2 - x^3 + o(x^3)$. Donner des équivalents simples en 0 de $f(x)$, $g(x)$ et $2xf(x) - g(x)$.
3. Proposer un développement limité en 0 à l'ordre 3 d'une fonction $h$ non nulle qui vérifierait en 0 : $h(x) \sim -3x$ et $h(x) + 3x \sim 5x^2$.
4. Proposer un développement limité en 0 à l'ordre 4 d'une fonction $i$ non nulle qui vérifierait en 0 : $i(x) = o(x^3)$ et $\lim_{x \to 0} \dfrac{i(x)}{x^4} = 2$.

## Exercice 3 (5 points)
Type : développements limités usuels et composés · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/8
Formules : $e^u = \sum \frac{u^k}{k!}$ ; $\cos u = 1 - \frac{u^2}2 + \frac{u^4}{24}$ ; $\sin u = u - \frac{u^3}6$ ; $\ln(1+u) = u - \frac{u^2}2 + \frac{u^3}3 - \frac{u^4}4$ ; $\sqrt{1+u} = 1 + \frac u2 - \frac{u^2}8 + \frac{u^3}{16} - \frac{5u^4}{128}$ ; $(1+u)^\alpha = 1 + \alpha u + \frac{\alpha(\alpha-1)}2u^2$ ; produit tronqué ; composition : poser $u$, calculer $u^2$ à l'ordre voulu ; $1 + \cos 2x = 2\cos^2 x$

Dans cet exercice, vous prendrez soin de mettre en évidence les développements limités usuels que vous utiliserez au fur et à mesure.
1. Donner le développement limité en 0 à l'ordre 3 de $f(x) = \sin(2x)e^{-x}$.
2. Donner le développement limité en 0 à l'ordre 3 de $g(x) = \ln(1 + x + \cos(x))$.

## Exercice 4 (5 points)
Type : développements limités, limite par équivalents · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/9
Formules : en 0 : $e^x = 1 + x + \frac{x^2}2 + \frac{x^3}6 + o(x^3)$ ; $\ln(1+x) = x - \frac{x^2}2 + o(x^2)$ ; $\cos x = 1 - \frac{x^2}2 + o(x^3)$ ; $\sin x = x - \frac{x^3}6 + o(x^3)$ ; $\frac1{1-x} = 1 + x + x^2 + x^3 + o(x^3)$ ; produit de DL tronqué à l'ordre ; $a^b = e^{b\ln a}$ ; $f \sim g \Rightarrow$ même limite

1. Calculer $\displaystyle\lim_{x \to 0} \frac{\sqrt{1 + 2x^2} - \cos(2x^2) - x^2}{e^{-x} + \sin(x) - 1}$.
2. Calculer $\displaystyle\lim_{x \to +\infty} \left(x\sin\Big(\frac1x\Big)\right)^{x^2}$.

## Exercice 5 (6 points)
Type : reconnaître un sous-espace vectoriel · ECUE : EV · Niveau : maths-s2-ev/3
Formules : sev : contient 0, stable par addition et multiplication par un scalaire ; contre-exemple $\lambda u \notin E$ ; équation non linéaire ($z^2$) $\Rightarrow$ en général pas un sev ; $\mathrm{Vect}(\dots)$ est toujours un sev

Les ensembles suivants sont-ils des $\mathbb{R}$-espaces vectoriels ? Justifiez rigoureusement votre réponse.
1. $E = \{(u_n) \in \mathbb{R}^{\mathbb{N}},\ \forall n \in \mathbb{N},\ u_n \geqslant -1\}$.
2. $F = \{u \in \mathbb{R}^3,\ u = \alpha e_1 + \beta e_2 ;\ (\alpha, \beta) \in \mathbb{R}^2\}$ où $e_1 = (1,1,0)$ et $e_2 = (0,5,3)$.
3. $G = \{f : \mathbb{R} \to \mathbb{R},\ f(x) = o(x) \text{ au voisinage de } 0\}$.

## Exercice 6 (4,5 points)
Type : divisibilité de polynômes, multiplicité, factorisation dans $\mathbb{R}[X]$ et $\mathbb{C}[X]$ · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/9
Formules : $P(a) = 0 \iff X - a \mid P$ ; racine d'ordre $\geqslant 2$ $\iff P(a) = P'(a) = 0$ ; ordre exactement $m$ : $P^{(m)}(a) \neq 0$ ; $(X - a)^m \mid P$, $(X - a)^{m+1} \nmid P$ ; $X^2 + 1 = (X - i)(X + i)$ ; $\Delta < 0 \Rightarrow$ irréductible dans $\mathbb{R}[X]$

Soit un entier $n \geqslant 5$. On considère le polynôme $P_n(X) = X^{n+1} - 2X^n + 2X^{n-1} - 2X^{n-2} + X^{n-3}$.
1. Vérifier que 0 est une racine de $P$ et donner, sans calcul, son ordre exact de multiplicité en justifiant.
2. Montrer que 1 est une racine de $P$. Trouver son ordre exact de multiplicité.
3. On prend dans cette question $n = 11$. Ainsi, $P_{11}(X) = X^{12} - 2X^{11} + 2X^{10} - 2X^9 + X^8$. En vous aidant des questions précédentes, trouver la factorisation de $P_{11}$ en polynômes irréductibles dans $\mathbb{R}[X]$.

## Exercice 7 (4 points)
Type : divisibilité de polynômes, multiplicité d'une racine · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/4
Formules : $(X-a)(X-b) \mid P \iff P(a) = P(b) = 0$ ($a \neq b$) ; $\alpha$ racine d'ordre $m$ $\iff P(\alpha) = \dots = P^{(m-1)}(\alpha) = 0$, $P^{(m)}(\alpha) \neq 0$ ; $(X^n)' = nX^{n-1}$

Le but de l'exercice est de trouver tous les polynômes $P$ de degré 3 tels que $(X-1)^2 \mid P(X) - 1$ et $(X+1)^2 \mid P(X) + 1$. Considérons pour cela $P(X) = aX^3 + bX^2 + cX + d$ avec $(a,b,c,d) \in \mathbb{R}^4$ vérifiant l'hypothèse $(H)$ : $(X-1)^2 \mid P(X) - 1$ et $(X+1)^2 \mid P(X) + 1$. Introduisons aussi les deux polynômes $A(X) = P(X) - 1$ et $B(X) = P(X) + 1$.
1. Citer toutes les informations concernant les polynômes $A$ et $B$ que l'on peut déduire de $(H)$.
2. En déduire $P(1)$, $P'(1)$, $P(-1)$ et $P'(-1)$.
3. En déduire tous les polynômes $P$ de degré 3 vérifiant $(H)$.
