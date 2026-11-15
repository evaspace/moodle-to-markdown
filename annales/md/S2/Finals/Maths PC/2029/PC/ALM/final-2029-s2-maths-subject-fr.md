# Examen S2-B4-ALM (applications linéaires et matrices) — mai 2025 (sujet, FR)

- Source : `raw/S2/Finals/Maths PC/2029/PC/ALM/final-2029-s2-maths-subject-fr.pdf` (8 pages)
- Date réelle : mai 2025 (dossier promo 2029, ECUE ALM). Corrigé rédigé : `final-2029-s2-maths-correction-fr.md` (même dossier).
- Durée : 2 heures. Barème sur 40 points divisé par 2. 5 exercices. Rigueur prise en compte, malus d'un point pour manque de propreté. Documents et calculatrices interdits.

## Exercice 1 : opérations matricielles (8 points)
Type : opérations matricielles, produit, inverse · ECUE : ALM · Niveau : maths-s2-alm/6
Formules : $(\lambda A + \mu B)_{ij} = \lambda a_{ij} + \mu b_{ij}$ ; produit $AB$ défini si (colonnes de $A$) = (lignes de $B$), taille $n \times p$ par $p \times q$ donne $n \times q$ ; $(AB)_{ij} = \sum_k a_{ik}b_{kj}$ ; inverse par pivot de Gauss ; vérification $AA^{-1} = I$

Les questions sont indépendantes.
1. Considérons les deux matrices à coefficients réels $A = \begin{pmatrix} x & 5 \\ 0 & 2x \end{pmatrix}$ et $B = \begin{pmatrix} y & 7 \\ -1 & 3y \end{pmatrix}$. On pose $2A - 4B = (c_{i,j}) \in \mathcal{M}_2(\mathbb{R})$. Trouver les deux réels $x$ et $y$ tels que $c_{1,1} = -6$ et $c_{2,2} = -8$. Calculer alors $2A - 4B$.
2. On se donne $A = \begin{pmatrix} -1 \\ -2 \end{pmatrix}$ et $B = \begin{pmatrix} 1 & 2 \\ -3 & 4 \\ 0 & 1 \end{pmatrix}$. Peut-on faire le produit $AB$ ? $BA$ ? Justifier dans tous les cas. Si oui, effectuer ce produit en détaillant vos calculs intermédiaires.
3. Soit $A = \begin{pmatrix} 1 & 4 & 1 \\ 0 & -1 & 3 \\ -1 & -3 & -3 \end{pmatrix}$.
   (a) On admet que $A$ est inversible. Trouvez $A^{-1}$. Vous ferez apparaître tous les détails de vos calculs.
   (b) Expliquez comment vous pouvez vérifier le résultat obtenu à la question précédente.

## Exercice 2 : application linéaire (10 points)
Type : noyau, image, rang d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/3
Formules : linéaire : $f(\lambda u + v) = \lambda f(u) + f(v)$ ; $\mathrm{Ker} f$ : résoudre $f(x) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \mathrm{rg} f$ ; $\mathrm{rg} f = \dim F \Rightarrow \mathrm{Im} f = F$ (surjective) ; $\mathrm{Im} f = \mathrm{Vect}(f(e_1), \dots, f(e_n))$

On considère l'application linéaire $f : \mathbb{R}_2[X] \to \mathbb{R}^2,\ aX^2 + bX + c \mapsto (2a - b + c, a)$.
1. Trouver proprement la dimension du noyau de $f$, en précisant une de ses bases.
2. Énoncer rigoureusement le théorème du rang. En déduire la dimension de l'image de $f$.
3. $f$ est-elle injective ? Justifier.
4. $f$ est-elle surjective ? Justifier.

## Exercice 3 : changement de bases (7 points)
Type : matrice d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/5
Formules : colonne $j$ = coordonnées de $f(e_j)$ dans la base d'arrivée ; base canonique de $\mathbb{R}_2[X]$ : $(1, X, X^2)$ ; de $\mathcal{M}_2(\mathbb{R})$ : $E_{11}, E_{12}, E_{21}, E_{22}$ ; taille (dim arrivée) $\times$ (dim départ)

On considère l'application linéaire $f : \mathbb{R}^3 \to \mathbb{R}^3,\ (x, y, z) \mapsto (-2x - y, -2z - y, 0)$.
1. Donner la matrice de $f$ dans la base canonique de $\mathbb{R}^3$ au départ et à l'arrivée. Inutile de justifier.
2. Donner la matrice de $f$ dans la base $\mathcal{B}_1 = ((1, 0, 0), (-1, 1, 0), (1, -2, 1))$ au départ et la base canonique à l'arrivée. Faire apparaître vos calculs.
3. Donner la matrice de $f$ dans la base $\mathcal{B}_1$ au départ et à l'arrivée. On notera $A$ cette matrice. Inutile de justifier.
4. Expliquer pourquoi « en regardant » la matrice $A$, vous pouvez en déduire que $\dim(\mathrm{Im}(f)) = 2$.
5. En déduire $\dim(\mathrm{Ker}(f))$. En déduire aussi une base. Justifier.

## Exercice 4 : projection (10 points)
Type : projecteur, noyau et image · ECUE : ALM · Niveau : maths-s2-alm/10
Formules : projecteur $\iff f \circ f = f$ ; $E = \mathrm{Ker} f \oplus \mathrm{Im} f$ ; $f = id$ sur $\mathrm{Im} f$, $0$ sur $\mathrm{Ker} f$ ; matrice dans une base adaptée $\mathrm{diag}(0, \dots, 0, 1, \dots, 1)$

Soient $E$ un $\mathbb{R}$-espace vectoriel de dimension finie et $F$ et $G$ deux sous-espaces vectoriels de $E$. On suppose que $F \oplus G = E$. Ainsi, $\forall u \in E$, $\exists!\,(v, w) \in F \times G$ tel que $u = v + w$. Considérons l'application linéaire $p : E \to E,\ u \mapsto v$. La question 4 peut être traitée en admettant les questions précédentes.
1. Supposons $u \in F$. Expliquer pourquoi $p(u) = u$.
2. Supposons $u \in G$. Expliquer pourquoi $p(u) = 0_E$.
3. Soit $u \in E$ quelconque. Montrer que $p \circ p(u) = p(u)$.
4. On suppose ici que $E = \mathbb{R}^2$, $F = \mathrm{Vect}(\varepsilon_1)$ et $G = \mathrm{Vect}(\varepsilon_2)$ où $\varepsilon_1 = (2, 1)$ et $\varepsilon_2 = (-2, 4)$.
   (a) Dans le quadrillage fourni (1 unité = 2 carreaux), dessiner les axes de $\mathbb{R}^2$, $F$, $G$ et $u = (3, 4)$. Graphiquement, trouver $v \in F$ et $w \in G$ tels que $u = v + w$. Lire graphiquement les coordonnées de $p(u)$. Vous ferez apparaître tous les traits de construction.
   (b) Justifier que $\mathcal{B} = (\varepsilon_1, \varepsilon_2)$ est une base de $\mathbb{R}^2$.
   (c) Déterminer la matrice de $p$ dans la base $\mathcal{B}$ au départ et à l'arrivée.

## Exercice 5 : une démonstration guidée (5 points)
Type : changement de base, formule $Y = AX$ · ECUE : ALM · Niveau : maths-s2-alm/9
Formules : $X = PX'$, $P$ = matrice de passage (colonnes = nouveaux vecteurs dans l'ancienne base) ; $X' = P^{-1}X$ ; $f(e_j) = \sum_i a_{i,j}\varepsilon_i$ ; coordonnées de l'image $Y = AX$ ; inverse $2 \times 2$ : $\frac1{ad - bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$

Soient $E$ un $\mathbb{R}$-espace vectoriel de dimension 2 et $F$ un $\mathbb{R}$-espace vectoriel de dimension 3. Soient $f \in \mathcal{L}(E, F)$ et $u \in E$. On note :
- $\mathcal{B} = (e_1, e_2)$ une base de $E$ et $\mathcal{B}' = (\varepsilon_1, \varepsilon_2, \varepsilon_3)$ une base de $F$ (pas forcément canoniques) ;
- $A = \begin{pmatrix} a_1 & a_2 \\ a_3 & a_4 \\ a_5 & a_6 \end{pmatrix}$ la matrice de $f$ dans la base $\mathcal{B}$ au départ et $\mathcal{B}'$ à l'arrivée ;
- $U = \begin{pmatrix} \alpha \\ \beta \end{pmatrix}$ la matrice colonne des coordonnées de $u$ dans $\mathcal{B}$, c'est-à-dire $u = \alpha e_1 + \beta e_2$ ;
- $V$ la matrice colonne des coordonnées de $f(u)$ dans $\mathcal{B}'$.
1. Écrire $f(e_1)$ et $f(e_2)$ en fonction de $\varepsilon_1$, $\varepsilon_2$, $\varepsilon_3$ et des coefficients de $A$.
2. En déduire $f(u)$ comme combinaison linéaire de $\varepsilon_1$, $\varepsilon_2$ et $\varepsilon_3$.
3. En déduire une formule matricielle qui donne $V$ en fonction de $A$ et $U$.
4. Application. Prenons $E = \mathbb{R}^2$, $F = \mathbb{R}_2[X]$, $\mathcal{B} = ((1, 2), (3, 4))$, $\mathcal{B}' = (1, X + 1, (X - 1)^2)$ et $A = \begin{pmatrix} 1 & -1 \\ -2 & 3 \\ -3 & 1 \end{pmatrix} = \mathrm{Mat}_{\mathcal{B}, \mathcal{B}'}(f)$. Soit $u = (4, 6) \in \mathbb{R}^2$. Trouver $(a, b, c) \in \mathbb{R}^3$ tel que $f(u) = aX^2 + bX + c$.
