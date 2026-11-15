# Partiel S1 — janvier 2020 (sujet, FR)

- Source : `raw/S1/Finals/Maths PC/2024/final-2024-s1-maths-subject-fr.pdf` (10 pages)
- Date réelle : janvier 2020 (S1 19/20, dossier promo 2024). Corrigé : `final-2024-s1-maths-correction-fr.md`.
- Barème : 20 points

## Exercice 1 (2 points)
Type : propriétés de suites avec quantificateurs · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/3
Formules : bornée : $\exists m, M, \forall n, m \leqslant u_n \leqslant M$ ; non bornée : $\forall m, M, \exists n, u_n < m$ ou $u_n > M$ ; croissante : $\forall n, u_{n+1} \geqslant u_n$ ; monotone : croissante ou décroissante

Soit $(u_n)$ une suite réelle. Écrire avec des quantificateurs les propriétés suivantes :
1. $(u_n)$ n'est pas bornée.
2. $(u_n)$ est monotone.

## Exercice 2 (3 points)
Type : suites extraites · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/11
Formules : toute suite extraite d'une suite convergente converge vers la même limite ; $(u_{6n})$ extraite de $(u_{2n})$ et de $(u_{3n})$ ; $(u_{2n})$ et $(u_{2n+1})$ convergent vers $\ell$ $\Rightarrow (u_n) \to \ell$

Soit $(u_n)$ une suite réelle telle que : $(u_{2n})$ converge vers un réel $l$ et $(u_{3n})$ converge vers un réel $l'$.
1. À l'aide d'une suite extraite bien choisie, montrer que $l = l'$.
2. Peut-on conclure sur la convergence de $(u_n)$ ? (Justifier votre réponse.)

## Exercice 3 (2 points)
Type : suite arithmético-géométrique · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/7
Formules : $u_{n+1} = au_n + b$ ; point fixe $\ell = a\ell + b$, $\ell = \frac{b}{1-a}$ ; $v_n = u_n - \ell$ géométrique de raison $a$ ; $v_n = v_0a^n$ ; $u_n = (u_0 - \ell)a^n + \ell$

On considère une suite $(u_n)_{n \in \mathbb{N}}$ qui vérifie la relation de récurrence $u_{n+1} = 10u_n + 27$.
1. Pour quelles valeurs de $u_0$ une telle suite est-elle constante ?
2. On note $\ell$ la valeur trouvée à la question précédente. Montrer que la suite $(v_n) = (u_n - \ell)$ est géométrique et préciser sa raison.
3. On prend $u_0 = 1$. Exprimer $u_n$ en fonction de $n$.

## Exercice 4 (2 points)
Type : suites adjacentes · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/9
Formules : adjacentes : $(u_n)$ croissante, $(v_n)$ décroissante, $v_n - u_n \to 0$ ; alors elles convergent vers la même limite ; $\frac1{(n+1)!} = \frac1{n!} \cdot \frac1{n+1}$

Soient $(u_n)_{n \in \mathbb{N}^*}$ et $(v_n)_{n \in \mathbb{N}^*}$ définies pour tout $n \in \mathbb{N}^*$ par $u_n = \displaystyle\sum_{k=0}^{n} \frac{1}{k!}$ et $v_n = \dfrac{1}{n!} + \displaystyle\sum_{k=0}^{n} \frac{1}{k!}$.
Montrer que $(u_n)_{n \in \mathbb{N}^*}$ et $(v_n)_{n \in \mathbb{N}^*}$ sont adjacentes.

## Exercice 5 (4,5 points)
Type : suite récurrente $u_{n+1} = f(u_n)$, intervalles stables · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/10
Formules : constante $\iff u_0 = f(u_0)$ ; $I$ stable : $f(I) \subset I$, alors $u_n \in I$ par récurrence ; signe de $u_{n+1} - u_n = f(u_n) - u_n$ ; monotone bornée $\Rightarrow$ convergente ; $f$ continue : $\ell = f(\ell)$

Soit $(u_n)$ la suite réelle définie par récurrence par : $u_0 \in \mathbb{R}_+$ et $\forall n \in \mathbb{N}$, $u_{n+1} = f(u_n)$ où $f(x) = \dfrac{x^2 + 8}{6}$.
1. Trouver les valeurs de $u_0$ pour lesquelles la suite est constante.
2. Montrer que les intervalles $I_1 = [0, 2[$, $I_2 = ]2, 4[$ et $I_3 = ]4, +\infty[$ sont stables par $f$, c'est-à-dire $f(I) \subset I$. En déduire que si $u_0$ appartient à un de ces intervalles, tous les termes de la suite sont dans cet intervalle.
3. On suppose que $u_0 \in I_2$. Déterminer le sens de variation de la suite $(u_n)$. En déduire qu'elle est convergente puis déterminer sa limite.

## Exercice 6 (3 points)
Type : équation diophantienne $ax+by=c$ (Euclide, Gauss) · ECUE : HP (arithmétique)
Formules : Euclide : $a = bq + r$, $a \wedge b = b \wedge r$ ; solutions $\iff (a \wedge b) \mid c$ ; diviser par $d = a \wedge b$ ; remonter Euclide : $au_0 + bv_0 = d$ puis multiplier par $c/d$ ; Gauss : $a \mid bc$ et $a \wedge b = 1 \Rightarrow a \mid c$ ; $a(x - x_0) = -b(y - y_0)$ donne $x = x_0 + \frac{b}{d}k$, $y = y_0 - \frac{a}{d}k$, $k \in \mathbb{Z}$ ; vérifier la réciproque

1. En utilisant l'algorithme d'Euclide, déterminer une solution particulière de l'équation $329x - 217y = 21$.
2. En utilisant obligatoirement le théorème de Gauss, déterminer l'ensemble des couples $(x,y) \in \mathbb{Z}^2$ tels que $329x - 217y = 21$.

## Exercice 7 (2 points)
Type : décomposition en facteurs premiers, PGCD · ECUE : HP (arithmétique)
Formules : critères de divisibilité (2, 3 : somme des chiffres, 5, 11) ; $a \wedge b = \prod p^{\min(\alpha_p, \beta_p)}$

1. Décomposer en facteurs premiers les nombres : $A = 12825$ et $B = 9240$.
2. Sans utiliser l'algorithme d'Euclide, en déduire leur pgcd.

## Exercice 8 (1,5 points)
Type : petit théorème de Fermat, reste d'une puissance · ECUE : HP (arithmétique)
Formules : Fermat : $p$ premier, $p \nmid a \Rightarrow a^{p-1} \equiv 1\,[p]$ ; $a \equiv b\,[n] \Rightarrow a^k \equiv b^k\,[n]$ ; $a^{q(p-1)+r} \equiv a^r\,[p]$

Déterminer le reste de la division euclidienne de $751^{157}$ par 11.
