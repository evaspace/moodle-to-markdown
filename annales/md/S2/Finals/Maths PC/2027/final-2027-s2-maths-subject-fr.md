# Partiel S2 — mai 2023 (sujet, FR)

- Source : `raw/S2/Finals/Maths PC/2027/final-2027-s2-maths-subject-fr.pdf` (10 pages)
- Date réelle : mai 2023 (dossier promo 2027). Corrigé : `final-2027-s2-maths-correction-fr.md`.
- Durée : 3 heures. Barème sur 40 points divisé par 2. 6 exercices. Notation : si $\mathcal{F} = (u, v)$, le sev engendré est noté $\mathrm{Vect}(u, v)$.

## Exercice 1 : familles de vecteurs (6,5 points)
Type : familles libres, génératrices, bases ; coordonnées · ECUE : EV · Niveau : maths-s2-ev/7
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \lambda_i = 0$ ; en dimension $n$, une famille libre de $n$ vecteurs est une base ; plus de $n$ vecteurs $\Rightarrow$ liée ; coordonnées : résoudre $P = \alpha Q_1 + \beta Q_2 + \gamma Q_3$ en identifiant les coefficients

Les questions 1. et 2. sont indépendantes.
1. Dans $E = \mathbb{R}_2[X]$, on considère la famille $\mathcal{B} = (2, X - 3, (X + 4)^2)$.
   (a) Montrer proprement que $\mathcal{B}$ est une base de $E$.
   (b) Soit $A = -3X^2 - 25X - 39 \in E$. Trouver les coordonnées de $A$ dans $\mathcal{B}$.
2. Dans $E = \mathbb{R}^4$, on considère la famille $\mathcal{F}_1 = (u_1, u_2, u_3, u_4)$ formée par 4 vecteurs de $E$. On suppose de plus que $\mathcal{F}_1$ est une famille libre de $E$.
   (a) La famille $\mathcal{F}_2 = (u_1, 2u_2, u_3)$ est-elle une famille libre de $E$ ? Justifier.
   (b) La famille $\mathcal{F}_3 = (u_1 + 2u_2, 2u_1 - u_2, 3u_1 + u_2, u_4)$ est-elle une famille libre de $E$ ? Justifier.
   (c) Parmi les familles $\mathcal{F}_1$, $\mathcal{F}_2$ et $\mathcal{F}_3$, la(les)quelle(s) forme(nt) une base de $\mathbb{R}^4$ ? Justifier pour chaque famille.

## Exercice 2 : sev de dimension finie (7 points)
Type : sous-espaces, intersection, somme directe · ECUE : EV · Niveau : maths-s2-ev/9
Formules : $\mathrm{Vect}(u)$ : droite si $u \neq 0$ ; plan $ax + by + cz = 0$ : exprimer $z$, $G = \mathrm{Vect}(u, v)$ ; $u \in F \cap G$ : paramétrer par $F$ puis injecter l'équation de $G$ ; Grassmann $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $\dim F + \dim G = \dim E$

Dans $\mathbb{R}^3$, on considère les deux sous-espaces vectoriels suivants : $F = \mathrm{Vect}((1, 1, -1))$ et $G = \{(x, y, z) \in \mathbb{R}^3, 2x + y - z = 0\}$.
1. Trouver une base de $F$ ainsi que sa dimension. Vous justifierez soigneusement votre réponse.
2. Trouver une base de $G$ ainsi que sa dimension. Vous justifierez soigneusement votre réponse.
3. Que représentent géométriquement $F$ et $G$ ?
4. Trouver $F \cap G$.
5. Démontrer que $F \oplus G = \mathbb{R}^3$.

## Exercice 3 : application linéaire 1 (9,5 points)
Type : noyau, image, rang ; matrice d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/5
Formules : $\mathrm{Ker} f$ : résoudre $f(P) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \dim\mathrm{Im} f$ ; injective $\iff \mathrm{Ker} = \{0\}$ ; $\dim\mathrm{Im} = \dim F \Rightarrow$ surjective ; colonne $j$ = coordonnées de $f(e_j)$ dans la base d'arrivée

Dans cet exercice, la question 1. est indépendante des autres questions. Soit l'application linéaire $f : \mathbb{R}_2[X] \to \mathbb{R}^2,\ P = aX^2 + bX + c \mapsto (a + c, a + 2b + 3c)$.
1. (a) Donner la définition de $\mathrm{Ker}(f)$ adaptée à ce contexte. Écrire $\mathrm{Ker}(f)$ sous forme de Vect et justifier soigneusement que $\dim(\mathrm{Ker}(f)) = 1$.
   (b) Quelle est la dimension de l'image de $f$ ? Justifier.
   (c) Déterminer $\mathrm{Im}(f)$.
   (d) $f$ est-elle injective ? surjective ? Justifier.
2. Donner la matrice de $f$ dans la base canonique de $\mathbb{R}_2[X]$ au départ et la base canonique de $\mathbb{R}^2$ à l'arrivée. (Attention à l'ordre des vecteurs dans les bases.)
3. Donner la matrice de $f$ dans la base $\mathcal{B} = (1, X + 1, (2X - 3)^2)$ de $\mathbb{R}_2[X]$ au départ et la base canonique de $\mathbb{R}^2$ à l'arrivée.
4. Proposer une base $\mathcal{B}'$ de $\mathbb{R}^2$ telle que la matrice de $f$ dans la base canonique de $\mathbb{R}_2[X]$ au départ et la base $\mathcal{B}'$ à l'arrivée soit $M = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & -1 \end{pmatrix}$. Il n'est pas la peine de justifier que $\mathcal{B}'$ est une base de $\mathbb{R}^2$.

## Exercice 4 : inversion de matrice (5 points)
Type : inverse d'une matrice, application linéaire associée · ECUE : ALM · Niveau : maths-s2-alm/8
Formules : pivot de Gauss sur $AU = V$ ; $A$ inversible $\iff f$ bijective, $\mathrm{Mat}(f^{-1}) = A^{-1}$ ; colonnes de $A$ = images des vecteurs de la base de départ ; $g(aX^2 + bX + c) = ag(X^2) + bg(X) + cg(1)$

Soit $f \in \mathcal{L}(\mathbb{R}^3)$ tel que la matrice de $f$ dans la base canonique au départ et à l'arrivée est $A = \begin{pmatrix} 1 & -1 & 1 \\ 1 & 1 & -2 \\ -2 & 1 & -1 \end{pmatrix}$.
1. Inverser la matrice $A$. Vous ferez apparaître clairement les opérations sur les lignes que vous effectuerez.
2. Donner l'expression de $f^{-1}$.

## Exercice 5 : changements de bases (8 points)
Type : changement de base, formule $Y = AX$ · ECUE : ALM · Niveau : maths-s2-alm/9
Formules : $X = PX'$, $P$ = matrice de passage (colonnes = nouveaux vecteurs dans l'ancienne base) ; $X' = P^{-1}X$ ; $f(e_j) = \sum_i a_{i,j}\varepsilon_i$ ; coordonnées de l'image $Y = AX$ ; inverse $2 \times 2$ : $\frac1{ad - bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$

Dans cet exercice, les questions 1. et 2. sont indépendantes.
1. Dans $\mathbb{R}^2$, on note $\mathcal{B}_1 = ((1, 0), (0, 1))$ la base canonique et $\mathcal{B}_2 = ((1, 1), (1, 2))$ une autre base. Soit $u = (x, y) \in \mathbb{R}^2$. On note $X = \begin{pmatrix} x \\ y \end{pmatrix}$ la matrice colonne formée des coordonnées de $u$ dans la base $\mathcal{B}_1$ et $X' = \begin{pmatrix} x' \\ y' \end{pmatrix}$ celle formée des coordonnées de $u$ dans la base $\mathcal{B}_2$.
   (a) On suppose $X'$ connu. En écrivant $u$ comme combinaison linéaire de vecteurs de $\mathcal{B}_2$, trouver une relation matricielle qui donne $X$ en fonction de $X'$. En déduire aussi la relation matricielle qui donne $X'$ en fonction de $X$.
   (b) Application : prenons $u = (4, -5) \in \mathbb{R}^2$. Trouver $X$ et trouver $X'$.
2. Cette question est une adaptation de la démonstration de cours que vous deviez connaître. Considérons $E = \mathbb{R}_2[X]$ et $\mathcal{B} = (e_1, e_2, e_3)$ une base de $E$ ; $F = \mathbb{R}^2$ et $\mathcal{B}' = (\varepsilon_1, \varepsilon_2)$ une base de $F$ ; $f \in \mathcal{L}(E, F)$ dont la matrice dans la base $\mathcal{B}$ au départ et $\mathcal{B}'$ à l'arrivée est $A = \begin{pmatrix} a_{1,1} & a_{1,2} & a_{1,3} \\ a_{2,1} & a_{2,2} & a_{2,3} \end{pmatrix}$ ; soit $Q \in E$, on note $X = \begin{pmatrix} \lambda_1 \\ \lambda_2 \\ \lambda_3 \end{pmatrix}$ la matrice colonne des coordonnées de $Q$ dans $\mathcal{B}$ et $Y$ la matrice colonne des coordonnées de $f(Q)$ dans $\mathcal{B}'$.
   (a) Écrire $f(e_1)$, $f(e_2)$ et $f(e_3)$ en fonction de $\varepsilon_1$, $\varepsilon_2$ et des coefficients de la matrice $A$.
   (b) En déduire $f(Q)$ comme combinaison linéaire de $\varepsilon_1$ et $\varepsilon_2$.
   (c) En déduire alors la formule matricielle qui donne $Y$ en fonction de $A$ et de $X$.
   (d) Application : prenons $\mathcal{B} = (1, X, X^2)$, $\mathcal{B}' = ((1, 1), (2, 1))$ et $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}$ (même contexte que précédemment). Trouver les réels $x$ et $y$ tels que $f(1 + 4X - 4X^2) = (x, y)$.

## Exercice 6 : exemple d'application linéaire (4 points)
Type : application linéaire dans une base adaptée (lecture graphique) · ECUE : ALM · Niveau : maths-s2-alm/10
Formules : $u = \alpha v + \beta w$ (coordonnées dans $\mathcal{B}$) ; $f(u) = \alpha f(v) + \beta f(w)$ ; colonnes de $A$ : $f(v) = -v$, $f(w) = 2w$ ; décomposer $u$ graphiquement par parallèles à $F$ et $G$

Dans $\mathbb{R}^2$, soient $F = \mathrm{Vect}((1, 1))$ et $G = \mathrm{Vect}((1, -1))$. On admet que $F \oplus G = \mathbb{R}^2$ et que $\mathcal{B} = (v = (1, 1), w = (1, -1))$ est une base de $\mathbb{R}^2$. Soit $f \in \mathcal{L}(\mathbb{R}^2)$ dont la matrice dans la base $\mathcal{B}$ au départ et à l'arrivée est $A = \begin{pmatrix} -1 & 0 \\ 0 & 2 \end{pmatrix}$.
1. Soit $u \in \mathbb{R}^2$. On sait alors qu'il existe un unique couple $(\alpha, \beta) \in \mathbb{R}^2$ tel que $u = \alpha v + \beta w$. Donner $f(u)$ en fonction de $v$, $w$, $\alpha$ et $\beta$.
2. Dessiner $F$, $G$, $v$, $w$ et $u = (2, 4)$. Graphiquement, trouver $\alpha$, $\beta$ et $f(u)$ en faisant apparaître tous les traits de construction.
