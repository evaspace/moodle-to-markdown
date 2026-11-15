# Corrigé du partiel S1 — janvier 2020

- Source : `raw/S1/Finals/Maths PC/2024/final-2024-s1-maths-correction-fr.pdf` (3 pages)
- Date réelle : janvier 2020 (S1 2019, dossier promo 2024). Sujet : `final-2024-s1-maths-subject-fr.md`.
- Durée : trois heures. Documents et calculatrices non autorisés.

## Exercice 1 (2 points)
Type : propriétés de suites avec quantificateurs · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/3
Formules : bornée : $\exists m, M, \forall n, m \leqslant u_n \leqslant M$ ; non bornée : $\forall m, M, \exists n, u_n < m$ ou $u_n > M$ ; croissante : $\forall n, u_{n+1} \geqslant u_n$ ; monotone : croissante ou décroissante

Soit $(u_n)$ une suite réelle.
1. $(u_n)$ bornée : $\exists M, m \in \mathbb{R}, \forall n \in \mathbb{N},\ m \leqslant u_n \leqslant M$.
   $(u_n)$ n'est pas bornée : $\forall M, m \in \mathbb{R}, \exists n \in \mathbb{N},\ u_n < m$ ou $u_n > M$.
2. $(u_n)$ est monotone : $\forall n \in \mathbb{N},\ u_{n+1} \leqslant u_n$ ou $\forall n \in \mathbb{N},\ u_{n+1} \geqslant u_n$.

## Exercice 2 (3 points)
Type : suites extraites · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/11
Formules : toute suite extraite d'une suite convergente converge vers la même limite ; $(u_{6n})$ extraite de $(u_{2n})$ et de $(u_{3n})$ ; $(u_{2n})$ et $(u_{2n+1})$ convergent vers $\ell$ $\Rightarrow (u_n) \to \ell$

1. $(u_{6n}) = (u_{2(3n)})$ est une suite extraite de $(u_{2n})$ donc $(u_{6n})$ converge vers $l$.
   $(u_{6n}) = (u_{3(2n)})$ est une suite extraite de $(u_{3n})$ donc $(u_{6n})$ converge vers $l'$. On en conclut que $l = l'$.
2. Au-delà de n'importe quel rang, on peut trouver des termes de $(u_n)$ qui n'appartiennent ni à $(u_{2n})$ ni à $(u_{3n})$ (en particulier les termes de la suite $(u_{6n+1})$), donc on ne peut pas conclure sur la convergence de $(u_n)$.

## Exercice 3 (2 points)
Type : suite arithmético-géométrique · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/7
Formules : $u_{n+1} = au_n + b$ ; point fixe $\ell = a\ell + b$, $\ell = \frac{b}{1-a}$ ; $v_n = u_n - \ell$ géométrique de raison $a$ ; $v_n = v_0a^n$ ; $u_n = (u_0 - \ell)a^n + \ell$

1. $u_0 = 10u_0 + 27 \iff u_0 = -3$. La suite est constante si $u_0 = -3$.
2. $\forall n \in \mathbb{N}$, $v_{n+1} = u_{n+1} + 3 = 10u_n + 27 + 3 = 10(u_n + 3) = 10v_n$ donc $(v_n)$ est géométrique de raison 10.
3. $u_0 = 1 \implies v_0 = 1 + 3 = 4$ donc $v_n = 4 \cdot 10^n$ et $u_n = v_n - 3 = 4 \cdot 10^n - 3$.

## Exercice 4 (2 points)
Type : suites adjacentes · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/9
Formules : adjacentes : $(u_n)$ croissante, $(v_n)$ décroissante, $v_n - u_n \to 0$ ; alors elles convergent vers la même limite ; $\frac1{(n+1)!} = \frac1{n!} \cdot \frac1{n+1}$

$u_{n+1} - u_n = \dfrac{1}{(n+1)!} > 0$ donc $(u_n)$ est croissante.
$v_{n+1} - v_n = \dfrac{1}{(n+1)!} + \dfrac{1}{(n+1)!} - \dfrac{1}{n!} = \dfrac{2 - (n+1)}{(n+1)!} \leqslant 0$ car $n \geqslant 1$, donc $(v_n)$ est décroissante.
$v_n - u_n = \dfrac{1}{n!} \xrightarrow[+\infty]{} 0$. $(u_n)$ et $(v_n)$ sont adjacentes.

## Exercice 5 (4,5 points)
Type : suite récurrente $u_{n+1} = f(u_n)$, intervalles stables · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/10
Formules : constante $\iff u_0 = f(u_0)$ ; $I$ stable : $f(I) \subset I$, alors $u_n \in I$ par récurrence ; signe de $u_{n+1} - u_n = f(u_n) - u_n$ ; monotone bornée $\Rightarrow$ convergente ; $f$ continue : $\ell = f(\ell)$

1. $u_n$ est constante ssi $u_0 = \dfrac{u_0^2 + 8}{6} \iff u_0^2 - 6u_0 + 8 = 0 \iff (u_0 - 2)(u_0 - 4) = 0 \iff u_0 = 2$ ou $u_0 = 4$.
2. Tableau de variation : $f' \geqslant 0$ sur $\mathbb{R}_+$ ($f'(0) = 0$), $f$ croissante de $f(0) = \frac43$ à $+\infty$, avec $f(2) = 2$ et $f(4) = 4$.
   On voit que $f(I_1) = [\frac43, 2[ \subset I_1$, $f(I_2) = ]2, 4[ = I_2$ et $f(I_3) = ]4, +\infty[ = I_3$, donc $I_1$, $I_2$ et $I_3$ sont stables par $f$.
   Si $u_0$ appartient à un de ces intervalles $I$ : $u_0 \in I$ et $\forall n \in \mathbb{N}$, $u_n \in I \implies u_{n+1} = f(u_n) \in I$, donc par récurrence $\forall n \in \mathbb{N}$, $u_n \in I$.
3. $u_0 \in I_2$ donc, d'après 2., $\forall n \in \mathbb{N}$, $u_n \in I_2$.
   $u_{n+1} - u_n = \dfrac{u_n^2 - 6u_n + 8}{6} < 0$ car $u_n$ est compris entre les deux racines du polynôme.
   $(u_n)$ est bornée et décroissante donc convergente. Soit $l$ sa limite : $f(l) = l$ donc $l = 2$ ou $l = 4$.
   Comme $(u_n)$ est décroissante : $\forall n \in \mathbb{N}$, $2 < u_n \leqslant u_0 < 4 \implies 2 \leqslant l \leqslant u_0 < 4$ donc $l = 2$.

## Exercice 6 (3 points)
Type : équation diophantienne $ax+by=c$ (Euclide, Gauss) · ECUE : HP (arithmétique)
Formules : Euclide : $a = bq + r$, $a \wedge b = b \wedge r$ ; solutions $\iff (a \wedge b) \mid c$ ; diviser par $d = a \wedge b$ ; remonter Euclide : $au_0 + bv_0 = d$ puis multiplier par $c/d$ ; Gauss : $a \mid bc$ et $a \wedge b = 1 \Rightarrow a \mid c$ ; $a(x - x_0) = -b(y - y_0)$ donne $x = x_0 + \frac{b}{d}k$, $y = y_0 - \frac{a}{d}k$, $k \in \mathbb{Z}$ ; vérifier la réciproque

1. Algorithme d'Euclide étendu pour $(E) : 329x - 217y = 21$ :

| q | r | u | v |
|---|---|---|---|
| | 329 | 1 | 0 |
| | 217 | 0 | 1 |
| 1 | 112 | 1 | −1 |
| 1 | 105 | −1 | 2 |
| 1 | 7 | 2 | −3 |
| 15 | 0 | | |

Donc $329 \wedge 217 = 7$ et $(E_p) : 329 \times 2 - 217 \times 3 = 7$.
En divisant tout par 7 : $(E) \iff 47x - 31y = 3$ avec $47 \wedge 31 = 1$.
$(E_p) \iff 47 \times 2 - 31 \times 3 = 1 \iff 47 \times 6 - 31 \times 9 = 3$. Une solution particulière de $(E)$ est $(6, 9)$.
2. En soustrayant $(E_p)$ à $(E)$ : $(E) \iff 47(x - 6) = 31(y - 9)$.
   Donc $47 \mid 31(y - 9)$ et $47 \wedge 31 = 1 \implies$ (Gauss) $47 \mid (y - 9) \iff \exists k \in \mathbb{Z}$, $y - 9 = 47k$.
   En remplaçant dans $(E)$ : $47(x - 6) = 31 \times 47k \implies x - 6 = 31k$.
   On vérifie que toutes les paires $(6 + 31k, 9 + 47k)$, $k \in \mathbb{Z}$, sont solutions : $47(6 + 31k) - 31(9 + 47k) = 47 \times 6 - 31 \times 9 = 3$.
   $S = \{(6 + 31k, 9 + 47k), k \in \mathbb{Z}\}$.

## Exercice 7 (2 points)
Type : décomposition en facteurs premiers, PGCD · ECUE : HP (arithmétique)
Formules : critères de divisibilité (2, 3 : somme des chiffres, 5, 11) ; $a \wedge b = \prod p^{\min(\alpha_p, \beta_p)}$

Avec les critères de divisibilité : $A = 12825 = 19 \times 5^2 \times 3^3$ et $B = 9240 = 11 \times 7 \times 5 \times 3 \times 2^3$. Le pgcd de $A$ et $B$ est 15.

## Exercice 8 (1,5 points)
Type : petit théorème de Fermat, reste d'une puissance · ECUE : HP (arithmétique)
Formules : Fermat : $p$ premier, $p \nmid a \Rightarrow a^{p-1} \equiv 1\,[p]$ ; $a \equiv b\,[n] \Rightarrow a^k \equiv b^k\,[n]$ ; $a^{q(p-1)+r} \equiv a^r\,[p]$

Par les critères de divisibilité ou une division euclidienne : $751 \equiv 3\,[11]$.
11 est premier, donc (petit théorème de Fermat) $751^{10} \equiv 1\,[11]$.
Ainsi $751^{157} = 751^{150} \times 751^7 \equiv 1 \times 3^7\,[11]$. Or $3^5 \equiv 1\,[11]$ donc $751^{157} \equiv 3^5 \times 3^2 \equiv 9\,[11]$.
Comme $0 \leqslant 9 < 11$, le reste de la division de $751^{157}$ par 11 est 9.
