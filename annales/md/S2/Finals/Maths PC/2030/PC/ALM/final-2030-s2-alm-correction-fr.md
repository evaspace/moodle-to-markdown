# Correction examen S2-B4-ALM — mai 2026

- Source : `raw/S2/Finals/Maths PC/2030/PC/ALM/final-2030-s2-alm-correction-fr.pdf` (4 pages)
- Date réelle : mai 2026 (dossier promo 2030, ECUE ALM). Sujet : `final-2030-s2-alm-subject-fr.md` (énoncés repris en abrégé).

## Exercice 1 : opérations matricielles
Type : opérations matricielles, produit, inverse · ECUE : ALM · Niveau : maths-s2-alm/6
Formules : $(\lambda A + \mu B)_{ij} = \lambda a_{ij} + \mu b_{ij}$ ; produit $AB$ défini si (colonnes de $A$) = (lignes de $B$), taille $n \times p$ par $p \times q$ donne $n \times q$ ; $(AB)_{ij} = \sum_k a_{ik}b_{kj}$ ; inverse par pivot de Gauss ; vérification $AA^{-1} = I$

1. (a) $A$ a 3 colonnes et $B$ 2 lignes : $AB$ n'est pas défini.
(b) $B$ a 2 colonnes et $A$ 2 lignes : $BA$ est défini (2 lignes, 3 colonnes), $BA = \begin{pmatrix} -5 & 5 & 3 \\ 0 & -5 & 4 \end{pmatrix}$.
2. (a) $AB = I_2$. (b) $A$ n'est pas carrée : elle n'est pas inversible.
3. (a) $AU = V$ ; $L_2 \leftarrow L_2 - L_1$, $L_3 \leftarrow L_3 + 3L_1$ : $y + 4z = Y - X$, $-y - 5z = Z + 3X$ ; $L_3 \leftarrow L_3 + L_2$ : $-z = 2X + Y + Z$. En remontant : $x = -7X - 7Y - 5Z$, $y = 7X + 5Y + 4Z$, $z = -2X - Y - Z$.
$A^{-1} = \begin{pmatrix} -7 & -7 & -5 \\ 7 & 5 & 4 \\ -2 & -1 & -1 \end{pmatrix}$.
(b) On vérifie que $AA^{-1} = I_3$.

## Exercice 2 : application linéaire
Type : noyau, image, rang d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/3
Formules : linéaire : $f(\lambda u + v) = \lambda f(u) + f(v)$ ; $\mathrm{Ker} f$ : résoudre $f(x) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \mathrm{rg} f$ ; $\mathrm{rg} f = \dim F \Rightarrow \mathrm{Im} f = F$ (surjective) ; $\mathrm{Im} f = \mathrm{Vect}(f(e_1), \dots, f(e_n))$

1. $\mathrm{Ker}(f) = \{(a, b, c), a - b = 0, a + b - c = 0, -2a + 2b = 0\} = \{(a, a, 2a)\} = \mathrm{Vect}(u = (1, 1, 2))$ ; $u \neq 0$ : base, $\dim = 1$.
2. Théorème du rang : $E$ de dimension finie, $f \in \mathcal{L}(E, F)$ : $\dim E = \dim \mathrm{Ker} f + \dim \mathrm{Im} f$. Ici $\dim \mathrm{Im}(f) = 3 - 1 = 2$.
3. $\mathrm{Im}(f) = \{a(X^2 + X - 2) + b(-X^2 + X + 2) + c(-X)\} = \mathrm{Vect}(P_1, P_2, P_3)$ avec $P_1 + P_2 = -2P_3$, donc $= \mathrm{Vect}(P_1, P_2)$ ; génératrice de cardinal $2 = \dim$ : $(P_1 = X^2 + X - 2, P_2 = -X^2 + X + 2)$ est une base.

## Exercice 3 : changement de bases
Type : changement de base, formule $Y = AX$ · ECUE : ALM · Niveau : maths-s2-alm/9
Formules : $X = PX'$, $P$ = matrice de passage (colonnes = nouveaux vecteurs dans l'ancienne base) ; $X' = P^{-1}X$ ; $f(e_j) = \sum_i a_{i,j}\varepsilon_i$ ; coordonnées de l'image $Y = AX$ ; inverse $2 \times 2$ : $\frac1{ad - bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$

1. (a) $\mathrm{Mat}_{\mathcal{B}}(f) = \begin{pmatrix} 2 & -3 \\ -2 & 1 \end{pmatrix}$.
(b) $f(\varepsilon_1) = (1, -3)$, $f(\varepsilon_2) = (-1, -1)$ : $\mathrm{Mat}_{\mathcal{B}', \mathcal{B}}(f) = \begin{pmatrix} 1 & -1 \\ -3 & -1 \end{pmatrix}$.
(c) $f(e_1) = (2, -2) = 4\varepsilon_1 - 6\varepsilon_2$, $f(e_2) = (-3, 1) = -4\varepsilon_1 + 5\varepsilon_2$ : $\mathrm{Mat}_{\mathcal{B}, \mathcal{B}'}(f) = \begin{pmatrix} 4 & -4 \\ -6 & 5 \end{pmatrix}$.
2. $u = (0, 1) = u_1 + u_2$, $U = (1, 1)^T$, $AU = (3, -5, -2)^T$ : $f(u) = 3P_1 - 5P_2 - 2P_3 = 6 - 5(X - 1) - 2(X + 1)^2 = -2X^2 - 9X + 9$. $a = -2$, $b = -9$, $c = 9$.

## Exercice 4 : un exemple
Type : projecteur, noyau et image · ECUE : ALM · Niveau : maths-s2-alm/10
Formules : projecteur $\iff f \circ f = f$ ; $E = \mathrm{Ker} f \oplus \mathrm{Im} f$ ; $f = id$ sur $\mathrm{Im} f$, $0$ sur $\mathrm{Ker} f$ ; matrice dans une base adaptée $\mathrm{diag}(0, \dots, 0, 1, \dots, 1)$

1. $u \in F \cap G$ : $u = (2\alpha, \alpha) = (-\beta, 2\beta)$, d'où $\alpha = \beta = 0$ : $F \cap G = \{0_E\}$.
2. $v = \frac{y + 2x}5(2, 1) = \frac{y + 2x}5\varepsilon_1 \in F$ et $w = \frac{2y - x}5(-1, 2) = \frac{2y - x}5\varepsilon_2 \in G$.
3. $u = v + w$ donc $E = F + G$, et $F \cap G = \{0_E\}$ : $E = F \oplus G$.
4. (a) Graphiquement $p(u) = (4, 2)$ dans la base canonique, $(2, 0)$ dans $\mathcal{B}$.
(b) $p(\varepsilon_1) = \varepsilon_1$ et $p(\varepsilon_2) = 0_E$.
(c) $\mathrm{Mat}_{\mathcal{B}}(p) = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$.
(d) $p(x, y) = v = \left(\frac{2y + 4x}5, \frac{y + 2x}5\right)$.

## Exercice 5 : matrice, image et noyau
Type : noyau, image, rang d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/3
Formules : linéaire : $f(\lambda u + v) = \lambda f(u) + f(v)$ ; $\mathrm{Ker} f$ : résoudre $f(x) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \mathrm{rg} f$ ; $\mathrm{rg} f = \dim F \Rightarrow \mathrm{Im} f = F$ (surjective) ; $\mathrm{Im} f = \mathrm{Vect}(f(e_1), \dots, f(e_n))$

$C_3 = -C_1$, donc $\mathrm{Im}(f) = \mathrm{Vect}(C_1, C_2)$, soit $\mathrm{Vect}(1 - 2X + X^2, 2 + X)$ ; ces deux polynômes ne sont pas colinéaires : base de $\mathrm{Im}(f)$, rang 2. Théorème du rang : $\dim \mathrm{Ker}(f) = 1$. $C_1 + C_3 = 0$ donne $u = (1, 0, 1) \in \mathrm{Ker}(f)$, non nul : base de $\mathrm{Ker}(f)$.
