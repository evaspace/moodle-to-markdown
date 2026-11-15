# Examen S1B2-ASI (suites et intégrales) — janvier 2024 (sujet, FR)

- Source : `raw/S1/Finals/Maths PC/2028/PC/ASI/final-2028-s1-maths-subject-fr.pdf` (6 pages)
- Date réelle : janvier 2024 (dossier promo 2028, ECUE ASI = APIS 2031). Corrigé : `final-2028-s1-maths-correction-fr.md`.
- Durée : 2 heures. Barème sur 40 points divisé par 2. 6 exercices. Rigueur prise en compte, malus d'un point pour manque de propreté. Documents et calculatrices interdits.

## Exercice 1 : intégrales (10 points)
Type : primitives usuelles, IPP, changement de variable vers arctan · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/13
Formules : primitives usuelles ($\int \frac{u'}{\sqrt u}$-type : $\int \frac{e^{\sqrt x}}{\sqrt x} = 2e^{\sqrt x}$, $\int \frac{u'}u = \ln|u|$) ; IPP : $\int_a^b uv' = [uv]_a^b - \int_a^b u'v$ ; changement de variable $x = \varphi(t)$, $dt = \frac{dx}{x}$ pour $x = e^t$, bornes transformées ; $\int \frac{dx}{1+x^2} = \arctan x$ ; $\arctan\sqrt3 = \frac\pi3$, $\arctan 1 = \frac\pi4$

1. Remplir le tableau ci-dessous (sans se soucier du domaine de définition des fonctions). $f$ désigne la fonction et $F$ est une primitive de $f$.

| $f(x)$ | $\ln 2$ | $x^4 + 2x$ | $\frac{e^{\sqrt x}}{\sqrt x}$ | $\frac1{x^2}$ | $\sin x$ | $1 + \tan^2 x$ | $\sqrt x$ | $\frac{x^5}{x^6 + 1}$ |
|---|---|---|---|---|---|---|---|---|
| $F(x)$ | | | | | | | | |

2. Via une intégration par parties dont vous énoncerez la formule générale, calculer $J = \displaystyle\int_0^1 (3x + 1)e^{2x}\,dx$.
3. Calculer $K = \displaystyle\int_0^{\ln\sqrt3} \frac{dt}{e^{-t} + e^t}$ en posant $x = e^t$.

## Exercice 2 : suites adjacentes (6 points)
Type : suites adjacentes ($\sum 1/k!$) · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/9
Formules : adjacentes : $(u_n)$ croissante, $(v_n)$ décroissante, $v_n - u_n \to 0$ ; $u_{n+1} - u_n = \frac1{(n+1)!}$ ; $\frac1{n!} = \frac{n+1}{(n+1)!}$ ; adjacentes $\Rightarrow$ convergentes ; convergente $\Rightarrow$ bornée

Soient $(u_n)$ et $(v_n)$ deux suites définies pour tout entier naturel $n \geqslant 2$ par : $u_n = \displaystyle\sum_{k=0}^{n} \frac1{k!}$ et $v_n = u_n + \dfrac1{n!}$.
1. Après avoir rappelé la définition, montrer que les suites $(u_n)$ et $(v_n)$ sont adjacentes.
2. La suite $(u_n)$ est-elle convergente ? Justifiez votre réponse.
3. La suite $(u_n)$ est-elle majorée ? Justifier.

## Exercice 3 : comparaison de suites (6 points)
Type : comparaison de suites ($\sim$, $o$, $O$) · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/12
Formules : $u_n \sim v_n \iff \frac{u_n}{v_n} \to 1$ ; $u_n = o(v_n) \iff \frac{u_n}{v_n} \to 0$ ; $u_n = O(v_n) \iff \frac{u_n}{v_n}$ bornée ; convergente $\Rightarrow$ bornée, donc $\sim$ et $o$ impliquent $O$ ; croissances comparées : $\frac{\ln n}{n^a} \to 0$, $\frac{n^a}{e^n} \to 0$ ; $\frac{\sin n}{n} \to 0$ ; factoriser par le terme dominant

Comparer en $+\infty$ les suites $(u_n)$ et $(v_n)$ suivantes à l'aide des comparateurs de Landau $\sim$, $= o(\cdot)$, $= O(\cdot)$ en citant toutes les comparaisons possibles et en justifiant vos réponses.
1. $u_n = 1 - 2n^2$ et $v_n = -2n^2 + n - 3$.
2. $u_n = e^{2n} - \sqrt n$ et $v_n = n + 1$.
3. $u_n = 4^n + 1$ et $v_n = 5^n$.

## Exercice 4 : cours (5 points)
Type : démonstration de cours (théorème des gendarmes) · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/13
Formules : gendarmes : $\forall n \geqslant N_0$, $a_n \leqslant u_n \leqslant b_n$, $a_n \to \ell$, $b_n \to \ell \Rightarrow u_n \to \ell$ ; définition $\forall \varepsilon, \exists N, n \geqslant N \Rightarrow |u_n - \ell| < \varepsilon$ ; prendre $N = \max(N_0, N_1, N_2)$ : $\ell - \varepsilon < a_n \leqslant u_n \leqslant b_n < \ell + \varepsilon$

1. Énoncer rigoureusement le théorème des gendarmes.
2. Démontrer le théorème des gendarmes.

## Exercice 5 : étude d'une suite (10 points)
Type : suite homographique, suite auxiliaire géométrique · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/10
Formules : récurrence pour le signe ; $\ell = f(\ell)$ si $f$ continue ; signe de $u_{n+1} - u_n$ ; décroissante minorée $\Rightarrow$ convergente ; $v_{n+1} = qv_n \Rightarrow v_n = v_0q^n$ ; $q > 1 \Rightarrow q^n \to +\infty$

Soit $(u_n)$ définie par $u_0 = 1$ et $\forall n \in \mathbb{N}$, $u_{n+1} = \dfrac{u_n}{u_n + 8}$.
N.B. : les questions 1. et 2. sont indépendantes.
1. (a) Montrer (par récurrence) que pour tout $n \in \mathbb{N}$, $u_n > 0$.
   (b) Supposons que la suite $(u_n)$ converge vers un réel $\ell$. Quelles sont les valeurs possibles de $\ell$ ?
   (c) Étudier la monotonie de la suite $(u_n)$.
   (d) La suite $(u_n)$ est-elle convergente ? Si oui, préciser sa limite.
2. Soit la suite $(v_n)$ définie pour tout $n \in \mathbb{N}$ par $v_n = 1 + \dfrac7{u_n}$.
   (a) Montrer que la suite $(v_n)$ est géométrique de raison 8. En déduire l'expression de $v_n$ en fonction de $n$.
   (b) En déduire l'expression de $u_n$ en fonction de $n$.
   (c) En utilisant la question précédente, retrouvez-vous le résultat obtenu dans la question 1.(d) ?

## Exercice 6 : suites extraites (3 points)
Type : suites extraites $(u_{2n})$, $(u_{2n+1})$ · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/11
Formules : $\sum_{k=0}^{n-1} q^k = \frac{1 - q^n}{1 - q}$ ($q \neq 1$) ; $(-1)^{2n} = 1$, $(-1)^{2n+1} = -1$ ; $(u_{2n})$ et $(u_{2n+1})$ même limite $\Rightarrow (u_n)$ converge

Soit $(u_n)$ définie pour tout $n \in \mathbb{N}^*$ par $u_n = \dfrac1n\displaystyle\sum_{k=0}^{n-1} (-1)^k$.
1. Trouver les expressions de $u_{2n}$ et $u_{2n+1}$ en fonction de $n$.
2. La suite $(u_n)$ est-elle convergente ? Si oui, donner sa limite.
