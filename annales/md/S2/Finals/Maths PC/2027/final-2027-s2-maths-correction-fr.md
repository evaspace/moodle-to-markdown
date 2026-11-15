# Correction du partiel S2 — mai 2023

- Source : `raw/S2/Finals/Maths PC/2027/final-2027-s2-maths-correction-fr.pdf` (5 pages)
- Date réelle : mai 2023 (dossier promo 2027). Sujet : `final-2027-s2-maths-subject-fr.md` (énoncés repris en abrégé).

## Exercice 1 : familles de vecteurs
Type : familles libres, génératrices, bases ; coordonnées · ECUE : EV · Niveau : maths-s2-ev/7
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \lambda_i = 0$ ; en dimension $n$, une famille libre de $n$ vecteurs est une base ; plus de $n$ vecteurs $\Rightarrow$ liée ; coordonnées : résoudre $P = \alpha Q_1 + \beta Q_2 + \gamma Q_3$ en identifiant les coefficients

1. (a) $\alpha \cdot 2 + \beta(X - 3) + \gamma(X + 4)^2 = 0 \iff (2\alpha - 3\beta + 16\gamma) + (\beta + 8\gamma)X + \gamma X^2 = 0$, d'où $\gamma = 0$, $\beta = 0$, $\alpha = 0$ : libre ; $\mathrm{Card}(\mathcal{B}) = 3 = \dim E$ : base.
(b) $2\alpha - 3\beta + 16\gamma = -39$, $\beta + 8\gamma = -25$, $\gamma = -3$ : $\gamma = -3$, $\beta = -1$, $\alpha = 3$. Coordonnées $(3, -1, -3)$.
2. (a) $\alpha u_1 + 2\beta u_2 + \gamma u_3 = 0$ ; $\mathcal{F}_1$ libre donc $\alpha = 2\beta = \gamma = 0$ : $\mathcal{F}_2$ libre.
(b) $(u_1 + 2u_2) + (2u_1 - u_2) - (3u_1 + u_2) + 0u_4 = 0$ : $\mathcal{F}_3$ liée.
(c) $\mathcal{F}_1$ libre de cardinal $4 = \dim \mathbb{R}^4$ : base. $\mathrm{Card}(\mathcal{F}_2) = 3 < 4$ : pas une base. $\mathcal{F}_3$ non libre : pas une base.

## Exercice 2 : sev de dimension finie
Type : sous-espaces, intersection, somme directe · ECUE : EV · Niveau : maths-s2-ev/9
Formules : $\mathrm{Vect}(u)$ : droite si $u \neq 0$ ; plan $ax + by + cz = 0$ : exprimer $z$, $G = \mathrm{Vect}(u, v)$ ; $u \in F \cap G$ : paramétrer par $F$ puis injecter l'équation de $G$ ; Grassmann $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $\dim F + \dim G = \dim E$

1. $(1, 1, -1)$ engendre $F$ et est non nul : base de $F$, $\dim F = 1$.
2. $G = \{(x, y, 2x + y)\} = \{x(1, 0, 2) + y(0, 1, 1)\} = \mathrm{Vect}(u, v)$ avec $u = (1, 0, 2)$, $v = (0, 1, 1)$ non colinéaires : base, $\dim G = 2$.
3. $F$ est une droite vectorielle et $G$ un plan vectoriel.
4. Si $u \in F \cap G$ : $u = (\alpha, \alpha, -\alpha)$ et $2\alpha + \alpha - (-\alpha) = 0$, donc $\alpha = 0$ : $F \cap G = \{0_{\mathbb{R}^3}\}$.
5. $F + G \subset \mathbb{R}^3$ et $\dim(F + G) = 1 + 2 - 0 = 3$ : $F + G = \mathbb{R}^3$ ; avec $F \cap G = \{0\}$, $F \oplus G = \mathbb{R}^3$.

## Exercice 3 : application linéaire 1
Type : noyau, image, rang ; matrice d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/5
Formules : $\mathrm{Ker} f$ : résoudre $f(P) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \dim\mathrm{Im} f$ ; injective $\iff \mathrm{Ker} = \{0\}$ ; $\dim\mathrm{Im} = \dim F \Rightarrow$ surjective ; colonne $j$ = coordonnées de $f(e_j)$ dans la base d'arrivée

1. (a) $\mathrm{Ker}(f) = \{aX^2 + bX + c \in \mathbb{R}_2[X], a + c = 0, a + 2b + 3c = 0\} = \{c = -a, a = b\} = \{a(X^2 + X - 1)\} = \mathrm{Vect}(X^2 + X - 1)$ ; vecteur non nul : base, $\dim = 1$.
(b) Théorème du rang : $\dim \mathrm{Im}(f) = 3 - 1 = 2$.
(c) $\mathrm{Im}(f) \subset \mathbb{R}^2$ et de dimension 2 : $\mathrm{Im}(f) = \mathbb{R}^2$.
(d) Pas injective ($\mathrm{Ker}(f) \neq \{0\}$) ; surjective ($\mathrm{Im}(f) = \mathbb{R}^2$).
2. $f(1) = (1, 3)$, $f(X) = (0, 2)$, $f(X^2) = (1, 1)$ : $\begin{pmatrix} 1 & 0 & 1 \\ 3 & 2 & 1 \end{pmatrix}$.
3. $f(X + 1) = (1, 5)$ et $f((2X - 3)^2) = f(4X^2 - 12X + 9) = (13, 7)$ : $\begin{pmatrix} 1 & 1 & 13 \\ 3 & 5 & 7 \end{pmatrix}$.
4. $\mathcal{B}' = ((1, 3), (0, 2))$ : $f(1) = (1, 3)$, $f(X) = (0, 2)$, $f(X^2) = (1, 1) = 1(1, 3) - 1(0, 2)$.

## Exercice 4 : inversion de matrice
Type : inverse d'une matrice, application linéaire associée · ECUE : ALM · Niveau : maths-s2-alm/8
Formules : pivot de Gauss sur $AU = V$ ; $A$ inversible $\iff f$ bijective, $\mathrm{Mat}(f^{-1}) = A^{-1}$ ; colonnes de $A$ = images des vecteurs de la base de départ ; $g(aX^2 + bX + c) = ag(X^2) + bg(X) + cg(1)$

1. $AU = V$ ; $L_2 \leftarrow L_2 + L_1$, $L_3 \leftarrow L_3 + L_1$ : $x - y + z = X$, $2x - z = X + Y$, $-x = Z + X$. En remontant : $y = -5X - Y - 3Z$, $z = -3X - Y - 2Z$, $x = -X - Z$.
$A^{-1} = \begin{pmatrix} -1 & 0 & -1 \\ -5 & -1 & -3 \\ -3 & -1 & -2 \end{pmatrix}$.
2. $f^{-1}(x, y, z) = (-x - z, -5x - y - 3z, -3x - y - 2z)$.

## Exercice 5 : changements de bases
Type : changement de base, formule $Y = AX$ · ECUE : ALM · Niveau : maths-s2-alm/9
Formules : $X = PX'$, $P$ = matrice de passage (colonnes = nouveaux vecteurs dans l'ancienne base) ; $X' = P^{-1}X$ ; $f(e_j) = \sum_i a_{i,j}\varepsilon_i$ ; coordonnées de l'image $Y = AX$ ; inverse $2 \times 2$ : $\frac1{ad - bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$

1. (a) $u = x'(1, 1) + y'(1, 2) = (x' + y', x' + 2y')$ ; par unicité des coordonnées, $X = PX'$ avec $P = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$, et $X' = P^{-1}X$.
(b) $X = \begin{pmatrix} 4 \\ -5 \end{pmatrix}$, $P^{-1} = \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix}$, $X' = P^{-1}X = \begin{pmatrix} 13 \\ -9 \end{pmatrix}$.
2. (a) $f(e_j) = a_{1,j}\varepsilon_1 + a_{2,j}\varepsilon_2$.
(b) $Q = \lambda_1e_1 + \lambda_2e_2 + \lambda_3e_3$ donc $f(Q) = (\lambda_1a_{1,1} + \lambda_2a_{1,2} + \lambda_3a_{1,3})\varepsilon_1 + (\lambda_1a_{2,1} + \lambda_2a_{2,2} + \lambda_3a_{2,3})\varepsilon_2$.
(c) $Y = AX$.
(d) $Q = 1 + 4X - 4X^2$, $X = (1, 4, -4)^T$, $Y = AX = (-3, 0)^T$, d'où $f(Q) = -3(1, 1) + 0(2, 1) = (-3, -3)$ : $x = y = -3$.

## Exercice 6 : exemple d'application linéaire
Type : application linéaire dans une base adaptée (lecture graphique) · ECUE : ALM · Niveau : maths-s2-alm/10
Formules : $u = \alpha v + \beta w$ (coordonnées dans $\mathcal{B}$) ; $f(u) = \alpha f(v) + \beta f(w)$ ; colonnes de $A$ : $f(v) = -v$, $f(w) = 2w$ ; décomposer $u$ graphiquement par parallèles à $F$ et $G$

1. $f(u) = \alpha f(v) + \beta f(w) = -\alpha v + 2\beta w$.
2. Graphiquement $\alpha = 3$, $\beta = -1$ : $u = 3(1, 1) - (1, -1)$. Puis $f(u) = -3(1, 1) - 2(1, -1) = (-5, -1)$.
