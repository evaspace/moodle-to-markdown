# Contrôle TD 3 (S2) — lundi 29 janvier 2018 (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (pas de corrigé officiel). Sujet : `td3-2022-s2-maths-subject-fr.md` (même dossier). Calculs vérifiés avec sympy. 

## Question de cours
Type : suites extraites · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/11
Formules : toute suite extraite d'une suite convergente converge vers la même limite ; $(u_{6n})$ extraite de $(u_{2n})$ et de $(u_{3n})$ ; $(u_{2n})$ et $(u_{2n+1})$ convergent vers $\ell$ $\Rightarrow (u_n) \to \ell$

Une suite extraite de $(u_n)$ est une suite $(u_{\varphi(n)})_{n\in\mathbb N}$ où $\varphi:\mathbb N\to\mathbb N$ est strictement croissante.

## Questions de cours
Type : sommes de termes consécutifs (suites arithmétiques et géométriques) · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/1
Formules : arithmétique : $\sum_{k=p}^n u_k = (n - p + 1)\frac{u_p + u_n}2$ (nombre de termes × moyenne des extrêmes) ; géométrique, $q \neq 1$ : $\sum_{k=p}^n u_k = u_p\frac{1 - q^{n-p+1}}{1 - q}$ (premier terme × $\frac{1 - q^{\text{nb de termes}}}{1 - q}$)

1. Suite arithmétique : $\displaystyle\sum_{k=p}^nu_k=(n-p+1)\,\frac{u_p+u_n}2$.
2. Suite géométrique de raison $q\ne1$ : $\displaystyle\sum_{k=p}^nu_k=u_p\,\frac{1-q^{n-p+1}}{1-q}$.

## Exercice 1
Type : suites extraites et divergence · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/11
Formules : $\sin(k\pi) = 0$ ; $\sin\left(2k\pi + \frac\pi3\right) = \frac{\sqrt3}2$ ; si $u_n \to \ell$, toute suite extraite tend vers $\ell$ ; deux suites extraites de limites différentes $\Rightarrow (u_n)$ diverge

1. $u_{2n}-u_n=\displaystyle\sum_{k=n+1}^{2n}\frac1k$ : $n$ termes, chacun $\ge\dfrac1{2n}$ (car $k\le2n$). Donc $u_{2n}-u_n\ge n\cdot\dfrac1{2n}=\dfrac12$.
2. Si $(u_n)$ convergeait vers $\ell$, $(u_{2n})$ aussi, donc $u_{2n}-u_n\to0$, ce qui contredit $u_{2n}-u_n\ge\frac12$. $(u_n)$ diverge (en fait $u_n\to+\infty$ car croissante non majorée).

## Exercice 2
Type : suites adjacentes, suites extraites $(u_{2n})$, $(u_{2n+1})$ · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/9
Formules : adjacentes : une croissante, l'autre décroissante, différence $\to 0$ ; $u_{2n+2} - u_{2n}$ = deux termes de la somme ; $\frac1{a^2} - \frac1{b^2} = \frac{(b-a)(b+a)}{a^2b^2}$ ; $(u_{2n})$ et $(u_{2n+1})$ même limite $\Rightarrow (u_n)$ converge

1. $v_{n+1}-v_n=u_{2n+2}-u_{2n}=-\dfrac1{2n+2}+\dfrac1{2n+3}<0$ : $(v_n)$ est strictement décroissante.
2. $w_{n+1}-w_n=u_{2n+3}-u_{2n+1}=\dfrac1{2n+3}-\dfrac1{2n+4}>0$ : $(w_n)$ est strictement croissante.
3. $v_n-w_n=u_{2n}-u_{2n+1}=-\dfrac{(-1)^{2n+1}}{2n+2}=\dfrac1{2n+2}$.
4. $v_n-w_n>0$ tend vers $0$, $(v_n)$ décroît et $(w_n)$ croît : suites adjacentes, donc elles convergent vers la même limite $\ell$. Les suites extraites paires et impaires ont la même limite : $(u_n)$ converge (vers $\ln2$).
