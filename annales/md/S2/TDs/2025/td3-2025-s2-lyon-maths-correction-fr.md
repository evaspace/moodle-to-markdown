# Contrôle TD 1 Lyon (S2) — lundi 22 février 2021 (corrigé, FR)

- Source : `raw/S2/TDs/2025/td3-2025-s2-lyon-maths-correction-fr.pdf` (2 pages)
- Date réelle : 22 février 2021 (campus de Lyon, dossier promo 2025). Pas de sujet séparé.
- Corrigé officiel : énoncé rappelé, solution en citation.

## Exercice 1
Type : théorème des valeurs intermédiaires · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/2
Formules : TVI : $f$ continue sur $[a,b]$, $k$ entre $f(a)$ et $f(b)$ $\Rightarrow \exists c \in [a,b]$, $f(c) = k$ ; si $f(a)f(b) < 0$, $\exists c \in ]a,b[$, $f(c) = 0$

Soient $(a,b) \in \mathbb{R}^2$, $a < b$, $f$ et $g$ deux fonctions continues sur $[a,b]$ telles que $f(a) = -g(b)$ et $f(b) = -g(a)$. Montrer que : $\exists c \in [a,b]$, $f(c) + g(c) = 0$.
> Soit $\varphi(x) = f(x) + g(x)$ sur $[a,b]$, continue comme somme de fonctions continues. $\varphi(a)\varphi(b) = (f(a) + g(a))(f(b) + g(b)) = (f(a) - f(b))(f(b) - f(a)) = -(f(a) - f(b))^2 \leqslant 0$. D'après le TVI, $\exists c \in [a,b]$, $\varphi(c) = f(c) + g(c) = 0$.

## Exercice 2
Type : suite récurrente $u_{n+1} = f(u_n)$, intervalles stables · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/10
Formules : constante $\iff u_0 = f(u_0)$ ; $I$ stable : $f(I) \subset I$, alors $u_n \in I$ par récurrence ; signe de $u_{n+1} - u_n = f(u_n) - u_n$ ; monotone bornée $\Rightarrow$ convergente ; $f$ continue : $\ell = f(\ell)$

Soient $f$ la fonction définie sur $\mathbb{R}$ par $f(x) = \dfrac14(x^2 - x + 4)$ et $(u_n)$ la suite définie par $u_0 = x \in \mathbb{R}$ et $\forall n \in \mathbb{N}$, $u_{n+1} = f(u_n)$.

a. Déterminer les valeurs de $x$ pour lesquelles la suite $(u_n)$ est constante.
> $(u_n)$ constante $\iff f(x) = x \iff x^2 - x + 4 = 4x \iff x^2 - 5x + 4 = 0$. $\Delta = 9$, $x_1 = 1$, $x_2 = 4$. Donc $x \in \{1, 4\}$.

b. Établir le tableau de variations de $f$ et montrer que l'intervalle $]4, +\infty[$ est stable par $f$.
> $f'(x) = \frac14(2x - 1)$, nul en $x = \frac12$ : $f$ décroît sur $]-\infty, \frac12]$ puis croît sur $[\frac12, +\infty[$, avec $f(\frac12) = \frac{15}{16}$, $f(1) = 1$, $f(4) = 4$, $\lim_{+\infty} f = +\infty$. $f$ est strictement croissante sur $]4, +\infty[$, $f(4) = 4$ et $\lim_{+\infty} f = +\infty$, donc $f(]4, +\infty[) = ]4, +\infty[$ : l'intervalle est stable par $f$.

c. On suppose que $(u_n)$ converge vers $l \in \mathbb{R}$. Quelles sont les valeurs possibles de $l$ ? Justifiez votre réponse.
> Si $u_{n+1} = f(u_n)$ avec $f$ continue et si $(u_n)$ converge, sa limite est un point fixe de $f$ : $f(l) = l$. Donc $l \in \{1, 4\}$.

## Exercice 3
Type : développements limités usuels et composés · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/8
Formules : $e^u = \sum \frac{u^k}{k!}$ ; $\cos u = 1 - \frac{u^2}2 + \frac{u^4}{24}$ ; $\sin u = u - \frac{u^3}6$ ; $\ln(1+u) = u - \frac{u^2}2 + \frac{u^3}3 - \frac{u^4}4$ ; $\sqrt{1+u} = 1 + \frac u2 - \frac{u^2}8 + \frac{u^3}{16} - \frac{5u^4}{128}$ ; $(1+u)^\alpha = 1 + \alpha u + \frac{\alpha(\alpha-1)}2u^2$ ; produit tronqué ; composition : poser $u$, calculer $u^2$ à l'ordre voulu ; $1 + \cos 2x = 2\cos^2 x$

a. Déterminer le développement limité à l'ordre 4 en 0 de $f(x) = \dfrac1{1+x}\cos(x)$.
> $\frac1{1+x} = 1 - x + x^2 - x^3 + x^4 + o(x^4)$ et $\cos x = 1 - \frac{x^2}2 + \frac{x^4}{24} + o(x^4)$. $f(x) = 1 - x + x^2 - x^3 + x^4 - \frac{x^2}2 + \frac{x^3}2 - \frac{x^4}2 + \frac{x^4}{24} + o(x^4) = 1 - x + \dfrac{x^2}2 - \dfrac{x^3}2 + \dfrac{13x^4}{24} + o(x^4)$.

## Exercice 4
Type : EDO linéaire 1er ordre à coefficient variable, solution particulière constante · ECUE : APIS (EDO) · Niveau : maths-s1-apis-edo/4
Formules : $a(t)y' + b(t)y = c$ : homogène $y_0 = ke^{-\int \frac ba}$ ; $e^{-\alpha\ln u} = u^{-\alpha}$ ; solution particulière constante $y_p = \frac cb$ si $b$ constant ($y_p' = 0$) ; solution générale $y = y_p + y_0$

Déterminer l'ensemble des solutions de l'équation $(E)$ : $(1+t)y' + 3y = 3$ sur $]-1, +\infty[$.
> $(E_0)$ : $(1+t)y' + 3y = 0$. $\frac ba = \frac3{1+t}$, de primitive $3\ln(1+t)$. $S_0 = \big\{ y_0 = ke^{-3\ln(1+t)} = \frac k{(1+t)^3},\ k \in \mathbb{R} \big\}$. Solution particulière : $y_p = 1$ ($y' = 0$, $(1+t) \times 0 + 3 = 3$). $S = \Big\{ y = 1 + \dfrac k{(1+t)^3},\ k \in \mathbb{R} \Big\}$.
