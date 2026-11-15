# Examen S1B2-ARITH — janvier 2024 (sujet, FR)

- Source : `raw/S1/Finals/Maths PC/2028/PC/ARITH/final-2028-s1-maths-subject-fr.pdf` (4 pages)
- Date réelle : janvier 2024 (dossier promo 2028, ECUE arithmétique). Corrigé : `final-2028-s1-maths-correction-fr.md`.
- Durée : 1 heure. Barème sur 20 points. 3 exercices. Rigueur prise en compte, malus d'un point pour manque de propreté. Documents et calculatrices interdits.

## Exercice 1 : nombres premiers et pgcd (4 points)
Type : décomposition en facteurs premiers, nombre de diviseurs, PGCD · ECUE : HP (arithmétique)
Formules : diviseur de $\prod p_i^{\alpha_i}$ : $\prod p_i^{\beta_i}$, $0 \leqslant \beta_i \leqslant \alpha_i$ ; nombre de diviseurs $\prod(\alpha_i + 1)$ ; $a \wedge b = \prod p^{\min}$

On se donne trois entiers naturels : $a = 300$, $b = 2^2 \times 3^3 \times 5 \times 11$ et $c = 2 \times 5^2 \times 9 \times 11$.
1. Donner la décomposition de $a$ en produit de facteurs premiers.
2. Soit $d \in \mathbb{N}^*$ un diviseur de $b$. Quelle est la forme générale de la décomposition de $d$ en facteurs premiers ? En déduire le nombre de diviseurs positifs distincts de $b$.
3. Trouver $b \wedge c$. Vous détaillerez votre calcul.

## Exercice 2 : congruence (7 points)
Type : congruences, Fermat, reste d'une puissance · ECUE : HP (arithmétique)
Formules : reste de la division par 4 : $r \in \{0,1,2,3\}$ ; $a \equiv b\,[n] \Rightarrow a^k \equiv b^k\,[n]$ ; Fermat : $p$ premier, $p \nmid a \Rightarrow a^{p-1} \equiv 1\,[p]$ ; $a^{q(p-1)+r} \equiv a^r\,[p]$

Les questions 1. et 2. sont indépendantes.
1. Soit $n$ un entier naturel non nul premier avec 4, c'est-à-dire $n \wedge 4 = 1$.
   (a) Quelles sont les valeurs possibles du reste de la division euclidienne de $n$ par 4 ? Justifier.
   (b) En déduire que $n^2 - 1 \equiv 0\,[4]$.
2. Quel est le reste de la division euclidienne de $N = 17^9 - 8^{2023}$ par 7 ? Justifier.

## Exercice 3 : autour de Bézout et Gauss (9 points)
Type : Bézout, Euclide, lemme de Gauss (démonstrations) · ECUE : HP (arithmétique)
Formules : Bézout : $\exists (u,v), au + bv = a \wedge b$ ; $a \wedge b = 1 \iff \exists (u,v), au + bv = 1$ ; Euclide : $a = bq + r$, remonter les divisions ; Gauss : $a \mid bc$, $a \wedge b = 1 \Rightarrow a \mid c$ ; $a \mid c$, $b \mid c$, $a \wedge b = 1 \Rightarrow ab \mid c$

1. Théorème de Bézout. Soit $(a,b) \in \mathbb{Z}^2$. Les questions (b) et (c) sont indépendantes.
   (a) Énoncer rigoureusement les deux versions du théorème de Bézout (d'une part quand $a \wedge b$ est quelconque et, d'autre part, quand $a \wedge b = 1$).
   (b) L'affirmation « Si $a$ et $b$ sont premiers entre eux alors $\exists (u,v) \in \mathbb{Z}^2$ tel que $au + bv = 2$ » est-elle vraie ou fausse ? Justifier.
   (c) En utilisant obligatoirement l'algorithme d'Euclide, montrer que 39 et 47 sont premiers entre eux. Trouver alors $(u,v) \in \mathbb{Z}^2$ tel que $39u + 47v = 1$.
2. Lemme de Gauss. Soit $(a,b,c) \in \mathbb{Z}^3$.
   (a) Montrer que $a \mid bc$ et $a \wedge b = 1 \implies a \mid c$ (lemme de Gauss).
   (b) On considère l'équation $(E) : 5(x - 1) = 7y$ d'inconnues $(x,y) \in \mathbb{Z}^2$. À l'aide de la question précédente, montrer que si $(x,y)$ est solution de $(E)$ alors $x = 1 + 7k$ et $y = 5k$ avec $k \in \mathbb{Z}$.
3. Soit $(a,b,c) \in \mathbb{Z}^3$. En utilisant soit le théorème de Bézout, soit le lemme de Gauss, montrer que si $a \mid c$, $b \mid c$ et $a \wedge b = 1$ alors $ab \mid c$.
