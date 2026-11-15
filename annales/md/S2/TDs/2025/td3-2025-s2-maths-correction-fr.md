# Contrôle TD 1 (S2) — lundi 15 février 2021 (corrigé, FR)

- Source : `raw/S2/TDs/2025/td3-2025-s2-maths-correction-fr.pdf` (2 pages)
- Date réelle : 15 février 2021 (dossier promo 2025 ; le fichier s'appelle td3 mais le document est le « Contrôle TD 1 » du S2). Sujet : `td3-2025-s2-maths-subject-fr.md`.
- Corrigé officiel : énoncé rappelé, solution en citation.

## Question de cours
Type : théorème des valeurs intermédiaires · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/2
Formules : TVI : $f$ continue sur $[a,b]$, $k$ entre $f(a)$ et $f(b)$ $\Rightarrow \exists c \in [a,b]$, $f(c) = k$ ; si $f(a)f(b) < 0$, $\exists c \in ]a,b[$, $f(c) = 0$

Soit $(a,b) \in \mathbb{R}^2$, $a < b$. Énoncer le théorème des valeurs intermédiaires pour une fonction $f$ définie sur l'intervalle $[a,b]$.
> Si $f$ est continue sur l'intervalle $[a,b]$ et si $f(a)f(b) \leqslant 0$ alors $\exists c \in [a,b]$, $f(c) = 0$.

## Exercice 1
Type : suite récurrente $u_{n+1} = f(u_n)$, intervalles stables · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/10
Formules : constante $\iff u_0 = f(u_0)$ ; $I$ stable : $f(I) \subset I$, alors $u_n \in I$ par récurrence ; signe de $u_{n+1} - u_n = f(u_n) - u_n$ ; monotone bornée $\Rightarrow$ convergente ; $f$ continue : $\ell = f(\ell)$

Soient $f$ la fonction définie sur $\mathbb{R}$ par $f(x) = \dfrac14(x^2 - x + 6)$ et $(u_n)$ la suite définie par $u_0 = x \in \mathbb{R}$ et $\forall n \in \mathbb{N}$, $u_{n+1} = f(u_n)$.

a. Déterminer les valeurs de $x$ pour lesquelles la suite $(u_n)$ est constante.
> $(u_n)$ constante $\iff f(x) = x \iff x^2 - x + 6 = 4x \iff x^2 - 5x + 6 = 0$. $\Delta = 1$, $x_1 = 2$, $x_2 = 3$. Donc $x \in \{2, 3\}$.

b. Établir le tableau de variations de $f$ et montrer que l'intervalle $]2, 3[$ est stable par $f$.
> $f'(x) = \frac14(2x - 1)$, nul en $x = \frac12$ : $f$ décroît sur $]-\infty, \frac12]$ puis croît sur $[\frac12, +\infty[$, avec $f(\frac12) = \frac{23}{16}$, $f(2) = 2$, $f(3) = 3$, $\lim_{+\infty} f = +\infty$. $f$ est strictement croissante sur $[2,3]$, $f(2) = 2$ et $f(3) = 3$, donc $f(]2,3[) = ]2,3[$ : l'intervalle est stable par $f$.

c. On suppose que $(u_n)$ converge vers $l \in \mathbb{R}$. Quelles sont les valeurs possibles de $l$ ? Justifiez votre réponse.
> Si $u_{n+1} = f(u_n)$ avec $f$ continue et si $(u_n)$ converge, sa limite est un point fixe de $f$ : $f(l) = l$. Donc $l \in \{2, 3\}$.

## Exercice 2
Type : développements limités usuels et composés · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/8
Formules : $e^u = \sum \frac{u^k}{k!}$ ; $\cos u = 1 - \frac{u^2}2 + \frac{u^4}{24}$ ; $\sin u = u - \frac{u^3}6$ ; $\ln(1+u) = u - \frac{u^2}2 + \frac{u^3}3 - \frac{u^4}4$ ; $\sqrt{1+u} = 1 + \frac u2 - \frac{u^2}8 + \frac{u^3}{16} - \frac{5u^4}{128}$ ; $(1+u)^\alpha = 1 + \alpha u + \frac{\alpha(\alpha-1)}2u^2$ ; produit tronqué ; composition : poser $u$, calculer $u^2$ à l'ordre voulu ; $1 + \cos 2x = 2\cos^2 x$

Déterminer le développement limité à l'ordre 4 en 0 de $f(x) = e^{-x}\sin(x)$.
> $e^{-x} = 1 - x + \frac{x^2}2 - \frac{x^3}6 + \frac{x^4}{24} + o(x^4)$ et $\sin x = x - \frac{x^3}6 + o(x^4)$. $f(x) = x - \frac{x^3}6 - x^2 + \frac{x^4}6 + \frac{x^3}2 - \frac{x^4}6 + o(x^4) = x - x^2 + \dfrac{x^3}3 + o(x^4)$.

## Exercice 3
Type : EDO linéaire 1er ordre à coefficient variable, solution particulière constante · ECUE : APIS (EDO) · Niveau : maths-s1-apis-edo/4
Formules : $a(t)y' + b(t)y = c$ : homogène $y_0 = ke^{-\int \frac ba}$ ; $e^{-\alpha\ln u} = u^{-\alpha}$ ; solution particulière constante $y_p = \frac cb$ si $b$ constant ($y_p' = 0$) ; solution générale $y = y_p + y_0$

Déterminer l'ensemble des solutions de l'équation $(E)$ : $2(1+t)y' + y = 3$ sur $]-1, +\infty[$.
> $(E_0)$ : $2(1+t)y' + y = 0$. $\frac ba = \frac1{2(1+t)}$, de primitive $\frac12\ln(1+t)$. $S_0 = \big\{ y_0 = ke^{-\frac12\ln(1+t)} = \frac k{\sqrt{1+t}},\ k \in \mathbb{R} \big\}$. Solution particulière : $y_p = 3$. $S = \Big\{ y = 3 + \dfrac k{\sqrt{1+t}},\ k \in \mathbb{R} \Big\}$.
