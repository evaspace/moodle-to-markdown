# Correction examen S2PA-B4-ARITH — juin 2024

- Source : `raw/S2/Finals/Maths PC/2028/PA/S2PA_2024_B4_COR_ARITH_Exam.pdf` (3 pages, corrigé avec énoncés)
- Date réelle : juin 2024 (parcours PA, dossier promo 2028). Pas de sujet séparé.

## Exercice 1 : décomposition des entiers
Type : décomposition en facteurs premiers, nombre de diviseurs, PGCD · ECUE : HP (arithmétique)
Formules : diviseur de $\prod p_i^{\alpha_i}$ : $\prod p_i^{\beta_i}$, $0 \leqslant \beta_i \leqslant \alpha_i$ ; nombre de diviseurs $\prod(\alpha_i + 1)$ ; $a \wedge b = \prod p^{\min}$

1. Trouver la décomposition en produits de facteurs premiers de $a = 792$. $a = 2 \times 396 = 2^3 \times 99 = 2^3 \times 3^2 \times 11$.
2. Soit $d \in \mathbb{N}^*$ tel que $d$ divise $a$. Quelle est la forme générale de la décomposition en facteurs premiers de $d$ ? $d = 2^i \times 3^j \times 11^k$ avec $i \in [\![0, 3]\!]$, $j \in [\![0, 2]\!]$, $k \in [\![0, 1]\!]$.
3. En déduire le nombre de diviseurs positifs de $a$. $4 \times 3 \times 2 = 24$.
4. Décomposer 36 en produits de facteurs premiers. $36 = 2^2 \times 3^2$.
5. Trouver un $b \in \mathbb{N}$, $b > 100$, tel que $a \wedge b = 36$. Justifiez votre choix. $b$ doit avoir comme diviseurs $2^2$ et $3^2$ mais pas $2^3$, $3^3$ ni 11 ; le corrigé propose $b = 2^5 \times 3^4 = 576$, mais alors $a \wedge b = 2^3 \times 3^2 = 72$. Un bon choix : $b = 2^2 \times 3^2 \times 5 = 180$.

## Exercice 2 : congruence
Type : congruences, Fermat, reste d'une puissance · ECUE : HP (arithmétique)
Formules : reste de la division par 4 : $r \in \{0,1,2,3\}$ ; $a \equiv b\,[n] \Rightarrow a^k \equiv b^k\,[n]$ ; Fermat : $p$ premier, $p \nmid a \Rightarrow a^{p-1} \equiv 1\,[p]$ ; $a^{q(p-1)+r} \equiv a^r\,[p]$

Les questions sont indépendantes.
1. Remplir le tableau suivant (entiers entre 0 et 10) :

| $a$ | $-2$ | 1 | 28 | 36 | 35 |
|---|---|---|---|---|---|
| $b$ | 3 | 4 | 14 | $-4$ | 49 |
| $a\,[11]$ | 9 | 1 | 6 | 3 | 2 |
| $b\,[11]$ | 3 | 4 | 3 | 7 | 5 |
| $a^3 - 2b\,[11]$ | 8 | 4 | 1 | 2 | 9 |

2. Énoncer rigoureusement les deux versions du petit théorème de Fermat. $p$ premier : $\forall n \in \mathbb{N}$, $n^p \equiv n\,[p]$ ; $\forall n \in \mathbb{N}$ tel que $p \nmid n$, $n^{p-1} \equiv 1\,[p]$.
3. Le nombre $N = 4 \times 6^{43} - 128$ est-il divisible par 7 ? Justifier. $128 = 7 \times 18 + 2$ donc $128 \equiv 2\,[7]$. 7 premier, $7 \nmid 6$ : $6^6 \equiv 1\,[7]$, $6^{43} = (6^6)^7 \times 6 \equiv 6\,[7]$, $4 \times 6^{43} \equiv 24 \equiv 3\,[7]$. $N \equiv 3 - 2 \equiv 1\,[7]$ : 7 ne divise pas $N$.

## Exercice 3 : autour de Bézout et Gauss
Type : Bézout, Euclide, lemme de Gauss (démonstrations) · ECUE : HP (arithmétique)
Formules : Bézout : $\exists (u,v), au + bv = a \wedge b$ ; $a \wedge b = 1 \iff \exists (u,v), au + bv = 1$ ; Euclide : $a = bq + r$, remonter les divisions ; Gauss : $a \mid bc$, $a \wedge b = 1 \Rightarrow a \mid c$ ; $a \mid c$, $b \mid c$, $a \wedge b = 1 \Rightarrow ab \mid c$

Soient $a$ et $b$ deux entiers non nuls.
1. Énoncer le théorème de Bézout. $\forall (a, b), \exists (u, v), au + bv = a \wedge b$ ; $a \wedge b = 1 \iff \exists (u, v), au + bv = 1$.
2. Énoncer ET démontrer le théorème de Gauss. $a \mid bc$ et $a \wedge b = 1 \implies a \mid c$. Preuve : $bc = ak$ et $au + bv = 1$, donc $c = cau + cbv = a(cu + kv)$.
3. En utilisant obligatoirement l'algorithme d'Euclide, trouver un couple $(u, v) \in \mathbb{Z}^2$ tel que $50u + 18v = 2$. $50 = 18 \times 2 + 14$, $18 = 14 \times 1 + 4$, $14 = 4 \times 3 + 2$, $4 = 2 \times 2$ ; $2 = 14 - 4 \times 3 = 14 \times 4 - 18 \times 3 = 50 \times 4 + 18 \times (-11)$ : $(u, v) = (4, -11)$.
4. Soit $(E)$ (énoncé du corrigé : « $25x + 9y = 6$ », alors que la résolution porte sur $50x + 18y = 2$, c'est-à-dire $25x + 9y = 1$). En utilisant le théorème de Gauss, trouver toutes les solutions. Avec $50 \times 4 + 18 \times (-11) = 2$ : $25(x - 4) = 9(-11 - y)$, $25 \wedge 9 = 1$, Gauss : $x = 4 + 9k$, $y = -11 - 25k$ ; réciproque vérifiée. $S = \{(4 + 9k, -11 - 25k), k \in \mathbb{Z}\}$.

## Exercice 4 : polynômes
Type : divisibilité de polynômes, multiplicité, factorisation dans $\mathbb{R}[X]$ et $\mathbb{C}[X]$ · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/9
Formules : $P(a) = 0 \iff X - a \mid P$ ; racine d'ordre $\geqslant 2$ $\iff P(a) = P'(a) = 0$ ; ordre exactement $m$ : $P^{(m)}(a) \neq 0$ ; $(X - a)^m \mid P$, $(X - a)^{m+1} \nmid P$ ; $X^2 + 1 = (X - i)(X + i)$ ; $\Delta < 0 \Rightarrow$ irréductible dans $\mathbb{R}[X]$

Les questions sont indépendantes.
1. Soient $n \geqslant 2$ et $A_n(X) = 5X^{2n+1} - X^3 - 4X$. Montrer que $X^2 + X \mid A_n$. $A_n(0) = 0$ et $A_n(-1) = -5 + 1 + 4 = 0$, donc $X(X + 1) \mid A_n$.
2. Soit $B(X) = X^4 + X^3 + aX^2 + bX + 1$. Trouver $a$ et $b$ pour que $-1$ soit racine d'ordre au moins 2 de $B$. $B(-1) = a - b + 1 = 0$, $B'(-1) = -1 - 2a + b = 0$ : $a = 0$, $b = 1$, $B = X^4 + X^3 + X + 1$.
3. Soit $P(X) = X^4 + 4X^3 + 5X^2 + 4X + 4$.
   (a) Montrer que $-2$ est une racine d'ordre exactement 2. $P(-2) = 0$, $P'(X) = 4X^3 + 12X^2 + 10X + 4$, $P'(-2) = 0$, $P''(X) = 12X^2 + 24X + 10$, $P''(-2) = 10 \neq 0$.
   (b) Interpréter en termes de divisibilité. $(X + 2)^2 \mid P$ et $(X + 2)^3 \nmid P$.
   (c) Factoriser $P$ en irréductibles dans $\mathbb{R}[X]$ et $\mathbb{C}[X]$ avec une seule division euclidienne. $P = (X + 2)^2(X^2 + 1)$ dans $\mathbb{R}[X]$ ($\Delta < 0$) ; $P = (X + 2)^2(X - i)(X + i)$ dans $\mathbb{C}[X]$.
