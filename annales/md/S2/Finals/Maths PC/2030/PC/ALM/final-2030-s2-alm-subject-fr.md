# Examen S2-B4-ALM (applications linéaires et matrices) — mai 2026 (sujet, FR)

- Source : `raw/S2/Finals/Maths PC/2030/PC/ALM/final-2030-s2-alm-subject-fr.pdf` (8 pages)
- Date réelle : mai 2026 (dossier promo 2030, ECUE ALM). Corrigé : `final-2030-s2-alm-correction-fr.md`.
- Durée : 2 heures. Barème sur 40 points divisé par 2. 5 exercices. Rigueur prise en compte, malus d'un point pour manque de propreté. Documents et calculatrices interdits.

## Exercice 1 : opérations matricielles (8 points)
Type : opérations matricielles, produit, inverse · ECUE : ALM · Niveau : maths-s2-alm/6
Formules : $(\lambda A + \mu B)_{ij} = \lambda a_{ij} + \mu b_{ij}$ ; produit $AB$ défini si (colonnes de $A$) = (lignes de $B$), taille $n \times p$ par $p \times q$ donne $n \times q$ ; $(AB)_{ij} = \sum_k a_{ik}b_{kj}$ ; inverse par pivot de Gauss ; vérification $AA^{-1} = I$

Les questions sont indépendantes.
1. Considérons les deux matrices à coefficients réels $A = \begin{pmatrix} -2 & 1 & 2 \\ -1 & 3 & -1 \end{pmatrix}$ et $B = \begin{pmatrix} 2 & 1 \\ 1 & -2 \end{pmatrix}$. Pour chacun des produits suivants, dire (en justifiant) s'il est bien défini ou non. En cas de réponse positive, effectuer le produit. (a) $AB$ ; (b) $BA$.
2. On considère les matrices $A = \begin{pmatrix} -3 & 7 & -1 \\ -1 & 2 & 0 \end{pmatrix}$ et $B = \begin{pmatrix} -2 & 5 \\ -1 & 3 \\ -2 & 6 \end{pmatrix}$.
   (a) Calculer $AB$.
   (b) La matrice $A$ est-elle inversible ? Justifier et, si votre réponse est positive, donner $A^{-1}$.
3. (a) Soit $A = \begin{pmatrix} 1 & 2 & 3 \\ 1 & 3 & 7 \\ -3 & -7 & -14 \end{pmatrix}$. On admet que $A$ est inversible. Trouver $A^{-1}$. Vous ferez apparaître tous les détails de vos calculs.
   (b) Expliquer comment vous pouvez vérifier le résultat obtenu à la question précédente.

## Exercice 2 : application linéaire (10 points)
Type : noyau, image, rang d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/3
Formules : linéaire : $f(\lambda u + v) = \lambda f(u) + f(v)$ ; $\mathrm{Ker} f$ : résoudre $f(x) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \mathrm{rg} f$ ; $\mathrm{rg} f = \dim F \Rightarrow \mathrm{Im} f = F$ (surjective) ; $\mathrm{Im} f = \mathrm{Vect}(f(e_1), \dots, f(e_n))$

On considère l'application linéaire $f : \mathbb{R}^3 \to \mathbb{R}_2[X],\ (a, b, c) \mapsto (a - b)X^2 + (a + b - c)X - 2a + 2b$.
1. Trouver proprement la dimension du noyau de $f$, en précisant une de ses bases.
2. Énoncer rigoureusement le théorème du rang. En déduire la dimension de l'image de $f$.
3. Trouver une base de $\mathrm{Im}(f)$.

## Exercice 3 : changement de bases (7 points)
Type : changement de base, formule $Y = AX$ · ECUE : ALM · Niveau : maths-s2-alm/9
Formules : $X = PX'$, $P$ = matrice de passage (colonnes = nouveaux vecteurs dans l'ancienne base) ; $X' = P^{-1}X$ ; $f(e_j) = \sum_i a_{i,j}\varepsilon_i$ ; coordonnées de l'image $Y = AX$ ; inverse $2 \times 2$ : $\frac1{ad - bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$

Les questions sont indépendantes.
1. On considère l'application linéaire $f : \mathbb{R}^2 \to \mathbb{R}^2,\ (x, y) \mapsto (2x - 3y, -2x + y)$. On note $\mathcal{B} = (e_1, e_2)$ la base canonique de $\mathbb{R}^2$. On admet que $\mathcal{B}' = (\varepsilon_1 = (2, 1), \varepsilon_2 = (1, 1))$ est une base de $\mathbb{R}^2$.
   (a) Écrire la matrice de $f$ dans la base $\mathcal{B}$ au départ et à l'arrivée.
   (b) Écrire la matrice de $f$ dans la base $\mathcal{B}'$ au départ et $\mathcal{B}$ à l'arrivée. Faire apparaître l'essentiel de vos calculs.
   (c) Écrire la matrice de $f$ dans la base $\mathcal{B}$ au départ et $\mathcal{B}'$ à l'arrivée. Faire apparaître l'essentiel de vos calculs.
2. Soient $\mathcal{B} = (u_1 = (1, 2), u_2 = (-1, -1))$ une base de $\mathbb{R}^2$ et $\mathcal{B}' = (P_1 = 2, P_2 = X - 1, P_3 = (X + 1)^2)$ une base de $\mathbb{R}_2[X]$. Soit $f \in \mathcal{L}(\mathbb{R}^2, \mathbb{R}_2[X])$ dont la matrice dans la base $\mathcal{B}$ au départ et $\mathcal{B}'$ à l'arrivée est $A = \begin{pmatrix} 1 & 2 \\ -1 & -4 \\ 0 & -2 \end{pmatrix}$. Soit $u = (0, 1) \in \mathbb{R}^2$. Trouver $(a, b, c) \in \mathbb{R}^3$ tel que $f(u) = aX^2 + bX + c$.

## Exercice 4 : un exemple (10 points)
Type : projecteur, noyau et image · ECUE : ALM · Niveau : maths-s2-alm/10
Formules : projecteur $\iff f \circ f = f$ ; $E = \mathrm{Ker} f \oplus \mathrm{Im} f$ ; $f = id$ sur $\mathrm{Im} f$, $0$ sur $\mathrm{Ker} f$ ; matrice dans une base adaptée $\mathrm{diag}(0, \dots, 0, 1, \dots, 1)$

On se place dans $E = \mathbb{R}^2$. Soient les sous-espaces vectoriels $F = \mathrm{Vect}(\varepsilon_1)$ et $G = \mathrm{Vect}(\varepsilon_2)$ avec $\varepsilon_1 = (2, 1)$ et $\varepsilon_2 = (-1, 2)$.
1. Montrer que $F \cap G = \{0_E\}$.
2. Soit $u = (x, y) \in E$. Montrer que $v = \left(\dfrac{2y + 4x}5, \dfrac{y + 2x}5\right) \in F$ et $w = \left(\dfrac{-2y + x}5, \dfrac{4y - 2x}5\right) \in G$.
3. En déduire que $E = F \oplus G$.
4. Soit $p$ la projection sur $F$ parallèlement à $G$.
   (a) Dans le quadrillage fourni (1 unité = 2 carreaux), dessiner les axes de $\mathbb{R}^2$, $F$, $G$ et $u = (3, 4)$. Graphiquement, trouver les coordonnées de $p(u)$ dans la base canonique d'une part et dans la base $\mathcal{B} = (\varepsilon_1, \varepsilon_2)$ d'autre part. Vous ferez apparaître tous les traits de construction.
   (b) Lire graphiquement $p(\varepsilon_1)$ et $p(\varepsilon_2)$ en fonction de $\varepsilon_1$ et $\varepsilon_2$.
   (c) Déterminer la matrice $A$ de $p$ dans la base $\mathcal{B} = (\varepsilon_1, \varepsilon_2)$ au départ et à l'arrivée.
   (d) Soit $u = (x, y) \in \mathbb{R}^2$. En vous aidant de la question 2., trouver l'expression de $p(u)$.

## Exercice 5 : matrice, image et noyau (5 points)
Type : noyau, image, rang d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/3
Formules : linéaire : $f(\lambda u + v) = \lambda f(u) + f(v)$ ; $\mathrm{Ker} f$ : résoudre $f(x) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \mathrm{rg} f$ ; $\mathrm{rg} f = \dim F \Rightarrow \mathrm{Im} f = F$ (surjective) ; $\mathrm{Im} f = \mathrm{Vect}(f(e_1), \dots, f(e_n))$

Soit $f \in \mathcal{L}(\mathbb{R}^3, \mathbb{R}_2[X])$ dont la matrice, dans la base canonique de $\mathbb{R}^3$ au départ et la base canonique de $\mathbb{R}_2[X]$ à l'arrivée, est $A = \begin{pmatrix} 1 & 2 & -1 \\ -2 & 1 & 2 \\ 1 & 0 & -1 \end{pmatrix}$. En raisonnant sur les colonnes de $A$, trouver le rang de $A$, une base de l'image et du noyau de $f$. Vous êtes libres de les obtenir dans l'ordre que vous voulez.
