# Examen S2-B4-ALM (applications linéaires et matrices) — juin 2024 (sujet, FR)

- Source : `raw/S2/Finals/Maths PC/2028/PC/ALM/final-2028-s2-maths-subject-fr.pdf` (7 pages)
- Date réelle : juin 2024 (dossier promo 2028, ECUE ALM). Corrigé : `final-2028-s2-maths-correction-fr.md`.
- Durée : 2 heures. Barème sur 30 points ramené à 20. 5 exercices. Rigueur prise en compte, malus d'un point pour manque de propreté. Documents et calculatrices interdits.

## Exercice 1 : inversion de matrice (4 points)
Type : inverse d'une matrice · ECUE : ALM · Niveau : maths-s2-alm/8
Formules : $A$ inversible $\iff \det A \neq 0$ ; pivot de Gauss sur $(A \mid I_n) \to (I_n \mid A^{-1})$ ; ou $A^{-1} = \frac1{\det A}{}^t\mathrm{Com}(A)$ ; vérifier $AA^{-1} = I_n$ ; $2 \times 2$ : $\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1} = \frac1{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$

Soit $A = \begin{pmatrix} 2 & 1 & 1 \\ 2 & -1 & 2 \\ -1 & 1 & -1 \end{pmatrix}$. On admet que $A$ est inversible. Trouvez $A^{-1}$. Vous ferez apparaître tous les détails de vos calculs.

## Exercice 2 : application linéaire (9 points)
Type : noyau, image, rang ; matrice d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/5
Formules : $\mathrm{Ker} f$ : résoudre $f(P) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \dim\mathrm{Im} f$ ; injective $\iff \mathrm{Ker} = \{0\}$ ; $\dim\mathrm{Im} = \dim F \Rightarrow$ surjective ; colonne $j$ = coordonnées de $f(e_j)$ dans la base d'arrivée

On considère l'application linéaire $f : \mathbb{R}_2[X] \to \mathbb{R}^2,\ P \mapsto (P(0), P'(-1))$.
1. Donner la matrice de $f$ dans la base canonique $(1, X, X^2)$ au départ et la base canonique $((1, 0), (0, 1))$ à l'arrivée.
2. Montrer proprement que la dimension du noyau de $f$ est égale à 1.
3. Énoncer rigoureusement le théorème du rang et en déduire la dimension du noyau (de l'image) de $f$.
4. $f$ est-elle injective ? Justifier.
5. $f$ est-elle surjective ? Justifier.

## Exercice 3 : changement de bases (3 points)
Type : matrice d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/5
Formules : colonne $j$ = coordonnées de $f(e_j)$ dans la base d'arrivée ; base canonique de $\mathbb{R}_2[X]$ : $(1, X, X^2)$ ; de $\mathcal{M}_2(\mathbb{R})$ : $E_{11}, E_{12}, E_{21}, E_{22}$ ; taille (dim arrivée) $\times$ (dim départ)

On considère l'application linéaire $f : \mathbb{R}^2 \to \mathbb{R}_1[X],\ (a, b) \mapsto (-3a + 5b)X - 4a + 6b$.
1. Donner la matrice de $f$ dans la base canonique de $\mathbb{R}^2$ au départ et la base canonique de $\mathbb{R}_1[X]$ à l'arrivée.
2. Donner la matrice de $f$ dans la base $\mathcal{B}_1 = ((1, 1), (2, 1))$ au départ et la base $\mathcal{B}_2 = (X + 1, X + 2)$ à l'arrivée.
3. Sachant que la base d'arrivée est la base canonique de $\mathbb{R}_1[X]$, qu'a-t-on pris comme base de départ pour obtenir $B = \begin{pmatrix} 2 & -4 \\ 2 & -3 \end{pmatrix}$ comme matrice de $f$ dans ces bases ?

## Exercice 4 : projection (8 points)
Type : projecteur, noyau et image · ECUE : ALM · Niveau : maths-s2-alm/10
Formules : projecteur $\iff f \circ f = f$ ; $E = \mathrm{Ker} f \oplus \mathrm{Im} f$ ; $f = id$ sur $\mathrm{Im} f$, $0$ sur $\mathrm{Ker} f$ ; matrice dans une base adaptée $\mathrm{diag}(0, \dots, 0, 1, \dots, 1)$

On considère l'application linéaire $p : \mathbb{R}^2 \to \mathbb{R}^2,\ (x, y) \mapsto (0, x + y)$. On admet que $\mathrm{Ker}(p) = \mathrm{Vect}((1, -1))$ et $\mathrm{Im}(p) = \mathrm{Vect}((0, 1))$.
1. Dans le quadrillage fourni, dessiner $\mathbb{R}^2$, $\mathrm{Ker}(p)$ et $\mathrm{Im}(p)$.
2. En quoi votre dessin montre-t-il que $\mathrm{Ker}(p) \oplus \mathrm{Im}(p) = \mathbb{R}^2$ ?
3. Soit $u \in \mathbb{R}^2$. On sait alors que $\exists!\,(u_1, u_2) \in \mathrm{Ker}(p) \times \mathrm{Im}(p)$ tel que $u = u_1 + u_2$. Que vaut $p(u_1)$ ? Que vaut $p(u_2)$ ? En déduire $p(u)$ en fonction de $u_1$ et/ou $u_2$.
4. Dessiner dans le quadrillage $u = (-1, -2)$. Graphiquement, trouver $p(u)$ en faisant apparaître tous les traits de construction.
5. Vérifier que $p \circ p = p$.
6. On admet que $\mathcal{B} = ((1, -1), (0, 1))$ est une base de $\mathbb{R}^2$. Déterminer la matrice de $p$ dans cette base au départ et à l'arrivée.

## Exercice 5 : matrices (6 points)
Type : changement de base, formule $Y = AX$ · ECUE : ALM · Niveau : maths-s2-alm/9
Formules : $X = PX'$, $P$ = matrice de passage (colonnes = nouveaux vecteurs dans l'ancienne base) ; $X' = P^{-1}X$ ; $f(e_j) = \sum_i a_{i,j}\varepsilon_i$ ; coordonnées de l'image $Y = AX$ ; inverse $2 \times 2$ : $\frac1{ad - bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$

Les deux questions sont indépendantes.
1. Soit $f \in \mathcal{L}(\mathbb{R}_2[X])$ dont la matrice dans la base canonique $\mathcal{B} = (1, X, X^2)$ au départ et à l'arrivée est $A = \begin{pmatrix} 1 & -1 & 2 \\ 0 & 2 & 4 \\ 1 & 2 & 1 \end{pmatrix}$.
   (a) Soit $P = -3 + 2X - 4X^2$. Trouver $U$ la matrice colonne formée des coordonnées de $P$ dans la base canonique $\mathcal{B}$.
   (b) En vous aidant d'un produit matriciel, calculer $f(P)$.
2. Dans $\mathbb{R}^3$, on considère la base canonique $\mathcal{B} = (e_1, e_2, e_3)$ et la base $\mathcal{B}' = (u_1 = (2, 0, 0), u_2 = (-3, 1, 0), u_3 = (16, 8, 1))$. Pour $u = (x, y, z) \in \mathbb{R}^3$, on note $X$ la matrice colonne des coordonnées de $u$ dans $\mathcal{B}$ et $X'$ celle dans $\mathcal{B}'$.
   (a) Écrire la matrice de passage $P$ de $\mathcal{B}$ vers $\mathcal{B}'$.
   (b) Soit $u \in \mathbb{R}^3$ tel que $u = 2u_1 + 3u_2 - 4u_3$. Entre $X$ et $X'$, laquelle est-elle immédiate à donner ? Donner-la et trouver l'autre via un calcul matriciel. Vérifier ensuite votre calcul « à la main ».
