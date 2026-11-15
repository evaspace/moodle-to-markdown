# Contrôle TD 3 (S2) — lundi 29 janvier 2018 (sujet, FR)

- Source : `raw/S2/TDs/2022/td3-2022-s2-maths-subject-fr.pdf` (scan, 2 pages)
- Date réelle : 29 janvier 2018 (dossier promo 2022). Pas de corrigé dans les annales.
- Durée : 45 minutes.

## Question de cours
Type : suites extraites · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/11
Formules : toute suite extraite d'une suite convergente converge vers la même limite ; $(u_{6n})$ extraite de $(u_{2n})$ et de $(u_{3n})$ ; $(u_{2n})$ et $(u_{2n+1})$ convergent vers $\ell$ $\Rightarrow (u_n) \to \ell$

Soit $(u_n)$ une suite réelle. Donner la définition d'une suite extraite de $(u_n)$.

## Questions de cours
Type : sommes de termes consécutifs (suites arithmétiques et géométriques) · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/1
Formules : arithmétique : $\sum_{k=p}^n u_k = (n - p + 1)\frac{u_p + u_n}2$ (nombre de termes × moyenne des extrêmes) ; géométrique, $q \neq 1$ : $\sum_{k=p}^n u_k = u_p\frac{1 - q^{n-p+1}}{1 - q}$ (premier terme × $\frac{1 - q^{\text{nb de termes}}}{1 - q}$)

1. Soient $(u_n)$ une suite arithmétique, $p \in \mathbb{N}$ et $n \geqslant p$. Que vaut $\displaystyle\sum_{k=p}^n u_k = u_p + u_{p+1} + \dots + u_n$ ?
2. Soient $(u_n)$ une suite géométrique de raison $q \neq 1$, $p \in \mathbb{N}$ et $n \geqslant p$. Que vaut $\displaystyle\sum_{k=p}^n u_k = u_p + u_{p+1} + \dots + u_n$ ?

## Exercice 1
Type : suites extraites et divergence · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/11
Formules : $\sin(k\pi) = 0$ ; $\sin\left(2k\pi + \frac\pi3\right) = \frac{\sqrt3}2$ ; si $u_n \to \ell$, toute suite extraite tend vers $\ell$ ; deux suites extraites de limites différentes $\Rightarrow (u_n)$ diverge

Soit $(u_n)$ la suite définie pour tout $n \in \mathbb{N}^*$ par $u_n = \displaystyle\sum_{k=1}^n \frac1k$.
1. Montrer (sans récurrence) que pour tout $n \in \mathbb{N}^*$, $u_{2n} - u_n \geqslant \dfrac12$.
2. En déduire que $(u_n)$ est divergente.

## Exercice 2
Type : suites adjacentes, suites extraites $(u_{2n})$, $(u_{2n+1})$ · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/9
Formules : adjacentes : une croissante, l'autre décroissante, différence $\to 0$ ; $u_{2n+2} - u_{2n}$ = deux termes de la somme ; $\frac1{a^2} - \frac1{b^2} = \frac{(b-a)(b+a)}{a^2b^2}$ ; $(u_{2n})$ et $(u_{2n+1})$ même limite $\Rightarrow (u_n)$ converge

Soient $(u_n)$, $(v_n)$ et $(w_n)$ les suites définies pour tout $n \in \mathbb{N}$ par $u_n = \displaystyle\sum_{k=0}^n \frac{(-1)^k}{1+k}$, $v_n = u_{2n}$ et $w_n = u_{2n+1}$.
1. Étudier la monotonie de $(v_n)$.
2. Étudier la monotonie de $(w_n)$.
3. Soit $n \in \mathbb{N}$. Déterminer $v_n - w_n$.
4. Nature de $(u_n)$ ? Justifiez votre réponse.
