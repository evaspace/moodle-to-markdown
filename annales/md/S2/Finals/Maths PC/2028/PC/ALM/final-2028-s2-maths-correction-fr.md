# Correction examen S2-B4-ALM — juin 2024

- Source : `raw/S2/Finals/Maths PC/2028/PC/ALM/final-2028-s2-maths-correction-fr.pdf` (3 pages, corrigé avec énoncés)
- Date réelle : juin 2024 (dossier promo 2028, ECUE ALM). Sujet : `final-2028-s2-maths-subject-fr.md`.

## Exercice 1 : inversion de matrice
Type : inverse d'une matrice · ECUE : ALM · Niveau : maths-s2-alm/8
Formules : $A$ inversible $\iff \det A \neq 0$ ; pivot de Gauss sur $(A \mid I_n) \to (I_n \mid A^{-1})$ ; ou $A^{-1} = \frac1{\det A}{}^t\mathrm{Com}(A)$ ; vérifier $AA^{-1} = I_n$ ; $2 \times 2$ : $\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1} = \frac1{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$

Soit $A = \begin{pmatrix} 2 & 1 & 1 \\ 2 & -1 & 2 \\ -1 & 1 & -1 \end{pmatrix}$. On admet que $A$ est inversible. Trouvez $A^{-1}$.
$AU = V \iff \begin{cases} 2x + y + z = X \\ 2x - y + 2z = Y \\ -x + y - z = Z \end{cases}$ ; $L_2 \leftarrow L_2 + L_1$, $L_3 \leftarrow L_3 - L_1$ : $4x + 3z = X + Y$, $-3x - 2z = Z - X$ ; $L_3 \leftarrow 4L_3 + 3L_2$ : $z = -X + 3Y + 4Z$. En remontant : $x = X - 2Y - 3Z$, $y = Y + 2Z$.
$A^{-1} = \begin{pmatrix} 1 & -2 & -3 \\ 0 & 1 & 2 \\ -1 & 3 & 4 \end{pmatrix}$.

## Exercice 2 : application linéaire
Type : noyau, image, rang ; matrice d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/5
Formules : $\mathrm{Ker} f$ : résoudre $f(P) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \dim\mathrm{Im} f$ ; injective $\iff \mathrm{Ker} = \{0\}$ ; $\dim\mathrm{Im} = \dim F \Rightarrow$ surjective ; colonne $j$ = coordonnées de $f(e_j)$ dans la base d'arrivée

On considère $f : \mathbb{R}_2[X] \to \mathbb{R}^2,\ P \mapsto (P(0), P'(-1))$.
1. Matrice de $f$ dans la base canonique $(1, X, X^2)$ au départ et $((1, 0), (0, 1))$ à l'arrivée : $f(1) = (1, 0)$, $f(X) = (0, 1)$, $f(X^2) = (0, -2)$, donc $\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & -2 \end{pmatrix}$.
2. Montrer proprement que la dimension du noyau de $f$ est égale à 1. $\mathrm{Ker}(f) = \{a + bX + cX^2, a = 0, -2c + b = 0\} = \{c(2X + X^2), c \in \mathbb{R}\} = \mathrm{Vect}(2X + X^2)$ ; $2X + X^2 \neq 0$ : base, $\dim = 1$.
3. Énoncer rigoureusement le théorème du rang et en déduire la dimension de l'image. $f \in \mathcal{L}(E, F)$, $E$ de dimension finie : $\dim E = \dim \mathrm{Ker} f + \dim \mathrm{Im} f$. $\dim \mathrm{Im}(f) = 3 - 1 = 2$.
4. $f$ est-elle injective ? Non : $\dim \mathrm{Ker}(f) = 1 \neq 0$.
5. $f$ est-elle surjective ? Oui : $\mathrm{Im}(f) \subset \mathbb{R}^2$ et $\dim \mathrm{Im}(f) = 2$.

## Exercice 3 : changement de bases
Type : matrice d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/5
Formules : colonne $j$ = coordonnées de $f(e_j)$ dans la base d'arrivée ; base canonique de $\mathbb{R}_2[X]$ : $(1, X, X^2)$ ; de $\mathcal{M}_2(\mathbb{R})$ : $E_{11}, E_{12}, E_{21}, E_{22}$ ; taille (dim arrivée) $\times$ (dim départ)

On considère $f : \mathbb{R}^2 \to \mathbb{R}_1[X],\ (a, b) \mapsto (-3a + 5b)X - 4a + 6b$.
1. Matrice de $f$ dans les bases canoniques de $\mathbb{R}^2$ et de $\mathbb{R}_1[X]$ : $f((1, 0)) = -3X - 4$, $f((0, 1)) = 5X + 6$, donc $A = \begin{pmatrix} -4 & 6 \\ -3 & 5 \end{pmatrix}$.
2. Matrice de $f$ dans $\mathcal{B}_1 = ((1, 1), (2, 1))$ au départ et $\mathcal{B}_2 = (X + 1, X + 2)$ à l'arrivée : $f((1, 1)) = 2X + 2 = 2(X + 1)$, $f((2, 1)) = -X - 2 = -(X + 2)$, donc $\begin{pmatrix} 2 & 0 \\ 0 & -1 \end{pmatrix}$.
3. La base d'arrivée étant la base canonique de $\mathbb{R}_1[X]$, quelle base de départ donne $B = \begin{pmatrix} 2 & -4 \\ 2 & -3 \end{pmatrix}$ ? La deuxième colonne de $B$ est la première de $A$ : le deuxième vecteur est $(1, 0)$ ; et $f((1, 1)) = 2 + 2X$. Base cherchée : $((1, 1), (1, 0))$.

## Exercice 4 : projection
Type : projecteur, noyau et image · ECUE : ALM · Niveau : maths-s2-alm/10
Formules : projecteur $\iff f \circ f = f$ ; $E = \mathrm{Ker} f \oplus \mathrm{Im} f$ ; $f = id$ sur $\mathrm{Im} f$, $0$ sur $\mathrm{Ker} f$ ; matrice dans une base adaptée $\mathrm{diag}(0, \dots, 0, 1, \dots, 1)$

On considère $p : \mathbb{R}^2 \to \mathbb{R}^2,\ (x, y) \mapsto (0, x + y)$. On admet $\mathrm{Ker}(p) = \mathrm{Vect}((1, -1))$ et $\mathrm{Im}(p) = \mathrm{Vect}((0, 1))$.
1. Dessiner $\mathbb{R}^2$, $\mathrm{Ker}(p)$ et $\mathrm{Im}(p)$ : les droites d'équations $y = -x$ et $x = 0$.
2. En quoi le dessin montre-t-il que $\mathrm{Ker}(p) \oplus \mathrm{Im}(p) = \mathbb{R}^2$ ? $\mathrm{Ker}(p) \cap \mathrm{Im}(p) = \{0\}$, puis $\dim(\mathrm{Ker} + \mathrm{Im}) = 1 + 1 - 0 = 2$.
3. Soit $u = u_1 + u_2$ avec $(u_1, u_2) \in \mathrm{Ker}(p) \times \mathrm{Im}(p)$ (unique). Que valent $p(u_1)$, $p(u_2)$ ? En déduire $p(u)$. $p(u_1) = 0$ ; $u_2 = (0, \alpha)$, $p(u_2) = (0, \alpha) = u_2$ ; $p(u) = u_2$.
4. Dessiner $u = (-1, -2)$ et trouver graphiquement $p(u)$ : $u_1 = (-1, 1)$, $u_2 = (0, -3)$, $p(u) = (0, -3)$.
5. Vérifier que $p \circ p = p$ : $p(p(x, y)) = p((0, x + y)) = (0, x + y) = p(x, y)$.
6. On admet que $\mathcal{B} = ((1, -1), (0, 1))$ est une base. Matrice de $p$ dans cette base au départ et à l'arrivée : $p((1, -1)) = 0$, $p((0, 1)) = (0, 1)$, donc $\begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$.

## Exercice 5 : matrices
Type : changement de base, formule $Y = AX$ · ECUE : ALM · Niveau : maths-s2-alm/9
Formules : $X = PX'$, $P$ = matrice de passage (colonnes = nouveaux vecteurs dans l'ancienne base) ; $X' = P^{-1}X$ ; $f(e_j) = \sum_i a_{i,j}\varepsilon_i$ ; coordonnées de l'image $Y = AX$ ; inverse $2 \times 2$ : $\frac1{ad - bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$

Les deux questions sont indépendantes.
1. Soit $f \in \mathcal{L}(\mathbb{R}_2[X])$ de matrice $A = \begin{pmatrix} 1 & -1 & 2 \\ 0 & 2 & 4 \\ 1 & 2 & 1 \end{pmatrix}$ dans la base canonique $\mathcal{B} = (1, X, X^2)$.
   (a) Soit $P = -3 + 2X - 4X^2$ : $U = (-3, 2, -4)^T$.
   (b) $AU = (-13, -12, -3)^T$, donc $f(P) = -13 - 12X - 3X^2$.
2. Dans $\mathbb{R}^3$, base canonique $\mathcal{B}$ et $\mathcal{B}' = (u_1 = (2, 0, 0), u_2 = (-3, 1, 0), u_3 = (16, 8, 1))$ ; $X$ et $X'$ coordonnées de $u$ dans $\mathcal{B}$ et $\mathcal{B}'$.
   (a) Matrice de passage $P = \begin{pmatrix} 2 & -3 & 16 \\ 0 & 1 & 8 \\ 0 & 0 & 1 \end{pmatrix}$.
   (b) Soit $u = 2u_1 + 3u_2 - 4u_3$. $X' = (2, 3, -4)^T$ est immédiat ; $X = PX' = (-69, -29, -4)^T$. Vérification : $2(2, 0, 0) + 3(-3, 1, 0) - 4(16, 8, 1) = (-69, -29, -4)$.
