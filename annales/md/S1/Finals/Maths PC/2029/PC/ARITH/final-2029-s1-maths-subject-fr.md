# Examen S1B2-ARITH — janvier 2025 (sujet, FR)

- Source : `raw/S1/Finals/Maths PC/2029/PC/ARITH/final-2029-s1-maths-subject-fr.pdf` (8 pages)
- Date réelle : janvier 2025 (dossier promo 2029, ECUE arithmétique). Corrigé rédigé : `final-2029-s1-maths-correction-fr.md` (même dossier).
- Durée : 1 h 30. Barème sur 30 points ramené à 20. 5 exercices. Rigueur prise en compte, malus d'un point pour manque de propreté. Documents et calculatrices interdits.

## Exercice 1 : autour des nombres premiers (7 points)
Type : décomposition en facteurs premiers, diviseurs communs · ECUE : HP (arithmétique)
Formules : $a \wedge b = \prod p^{\min(\alpha_p, \beta_p)}$ ; $d \mid a$ et $d \mid b \iff d \mid a \wedge b$ (Bézout) ; diviseurs de $\prod p_i^{\gamma_i}$ : $\prod p_i^{\delta_i}$, $0 \leqslant \delta_i \leqslant \gamma_i$ ; nombre : $\prod(\gamma_i + 1)$

Soient $a = 3960$ et $b = 2^2 \times 3 \times 5^2 \times 7$.
1. Décomposer $a$ en produit de facteurs premiers.
2. Trouver la décomposition en facteurs premiers de $a \wedge b$ et le calculer.
3. Soit $d \in \mathbb{N}^*$.
   (a) Montrer que $d \mid a$ et $d \mid b \iff d \mid a \wedge b$.
   (b) En déduire la forme générale en produit de facteurs premiers d'un diviseur (positif) commun de $a$ et de $b$.
   (c) Trouver tous les diviseurs (positifs) communs de $a$ et de $b$. Combien en avez-vous obtenus ? Expliquer comment retrouver ce nombre via la question précédente.

## Exercice 2 : équation diophantienne (6 points)
Type : équation diophantienne $ax+by=c$ (Euclide, Gauss) · ECUE : HP (arithmétique)
Formules : Euclide : $a = bq + r$, $a \wedge b = b \wedge r$ ; solutions $\iff (a \wedge b) \mid c$ ; diviser par $d = a \wedge b$ ; remonter Euclide : $au_0 + bv_0 = d$ puis multiplier par $c/d$ ; Gauss : $a \mid bc$ et $a \wedge b = 1 \Rightarrow a \mid c$ ; $a(x - x_0) = -b(y - y_0)$ donne $x = x_0 + \frac{b}{d}k$, $y = y_0 - \frac{a}{d}k$, $k \in \mathbb{Z}$ ; vérifier la réciproque

On considère l'équation $(E) : 29x + 13y = 3$ d'inconnues $(x,y) \in \mathbb{Z}^2$. Le but de l'exercice est de trouver toutes les solutions de $(E)$.
1. Via l'algorithme d'Euclide, trouver $29 \wedge 13$. En déduire que $(E)$ admet des solutions.
2. Via la question précédente, trouver une solution particulière $(x_0, y_0)$ de $(E)$.
3. Soit $(x,y)$ une solution quelconque de $(E)$. En utilisant le lemme de Gauss, montrer qu'il existe $k \in \mathbb{Z}$ tel que $x = x_0 + 13k$ et $y = y_0 - 29k$.
4. Supposons que $x = x_0 + 13k$ et $y = y_0 - 29k$ avec $k \in \mathbb{Z}$. Montrer que $(x,y)$ est solution de $(E)$.
5. En déduire l'ensemble des solutions de $(E)$.

## Exercice 3 : autour du cours et de Bézout (6 points)
Type : Bézout (énoncé et applications) · ECUE : HP (arithmétique)
Formules : Bézout : $\exists (u,v), au + bv = a \wedge b$ ; $a \wedge b = 1 \iff \exists (u,v), au + bv = 1$ ; élever au carré / multiplier une relation de Bézout ; $2 \times (2n+1) \cdot 1 - \dots$ : $1 \cdot (2n+1) - 2 \cdot n = 1$ ; fraction irréductible $\iff$ numérateur et dénominateur premiers entre eux

1. Énoncer soigneusement le théorème de Bézout d'une part pour deux entiers quelconques, d'autre part pour deux entiers premiers entre eux.
2. Application 1 : soit $(a,b) \in \mathbb{N}^2$ non nuls. Montrer que $a$ et $b$ sont premiers entre eux si et seulement si $a$ et $b^2$ sont premiers entre eux.
3. Application 2 : soit $n \in \mathbb{N}$. Montrer que la fraction $F = \dfrac{n}{2n+1}$ est irréductible.

## Exercice 4 : autour du cours et de Fermat (7 points)
Type : petit théorème de Fermat (énoncé, démonstration, application) · ECUE : HP (arithmétique)
Formules : Fermat : $p$ premier $\Rightarrow \forall n, n^p \equiv n\,[p]$ ; si $p \nmid n$, $n^{p-1} \equiv 1\,[p]$ ; binôme $(n+1)^p = \sum_k \binom pk n^k$ et $p \mid \binom pk$ pour $1 \leqslant k \leqslant p-1$ (récurrence) ; Gauss pour simplifier par $n$ ; $a^{6q+r} \equiv a^r\,[7]$

Dans cet exercice, on admet que :
- si $p$ est un nombre premier et $n$ un entier naturel, alors soit $p \wedge n = 1$, soit $p \mid n$ ;
- si $p$ est un nombre premier et $k$ un entier dans $[\![1, p-1]\!]$ alors $p \mid \binom{p}{k}$.
1. Énoncer ET démontrer le petit théorème de Fermat pour tout $n \in \mathbb{N}$.
2. Énoncer ET démontrer le petit théorème de Fermat quand $p$ ne divise pas $n$.
3. Application : quel est le reste de la division euclidienne de $N = 11 \times 12^{43} - 128$ par 7 ? Justifier proprement.

## Exercice 5 : congruence (4 points)
Type : congruences modulo $n$, équation sans solution · ECUE : HP (arithmétique)
Formules : $a \equiv b\,[n] \Rightarrow a^2 \equiv b^2\,[n]$ ; $11 \equiv 1$, $7 \equiv 2\,[5]$ ; table des carrés modulo 5 : $0, 1, 4, 4, 1$ ; $x = 5k \Rightarrow x^2 = 25k^2$ ; $25 \mid$ membre de gauche mais $25 \nmid 5$

On considère l'équation $(E) : 11x^2 - 7y^2 = 5$ d'inconnues $(x,y) \in \mathbb{Z}^2$.
1. Montrer que si $(x,y)$ est une solution de $(E)$ alors $x^2 \equiv 2y^2\,[5]$.
2. Compléter le tableau suivant (vos réponses doivent être des entiers dans $[\![0, 4]\!]$) :

| Modulo 5, $x$ est congru à | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| Modulo 5, $x^2$ est congru à | | | | | |
| Modulo 5, $y$ est congru à | 0 | 1 | 2 | 3 | 4 |
| Modulo 5, $2y^2$ est congru à | | | | | |

3. En déduire que si $(x,y)$ est une solution de $(E)$ alors $x$ et $y$ sont multiples de 5.
4. Montrer que si $x$ et $y$ sont multiples de 5 alors $(x,y)$ n'est pas solution de $(E)$. Vous commencerez par traduire ce que vous supposez avec des quantificateurs.
5. Donner l'ensemble des solutions de $(E)$.
