# Correction examen S2-B4-EV — juin 2024

- Source : `raw/S2/Finals/Maths PC/2028/PC/EV/final-2028-s2-maths-correction-fr.pdf` (2 pages)
- Date réelle : juin 2024 (dossier promo 2028, ECUE EV). Sujet : `final-2028-s2-maths-subject-fr.md`.

## Exercice 1 : familles de vecteurs
Type : familles libres, génératrices, bases ; coordonnées · ECUE : EV · Niveau : maths-s2-ev/7
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \lambda_i = 0$ ; en dimension $n$, une famille libre de $n$ vecteurs est une base ; plus de $n$ vecteurs $\Rightarrow$ liée ; coordonnées : résoudre $P = \alpha Q_1 + \beta Q_2 + \gamma Q_3$ en identifiant les coefficients

1. (a) $\alpha u_1 + \beta u_2 + \gamma u_3 = 0 \iff \alpha + 2\beta + \gamma = 0$, $\alpha + \beta - \gamma = 0$, $\alpha + \beta + \gamma = 0$. Avec $L_2 \leftarrow L_2 - L_3$ et $L_1 \leftarrow L_1 - L_3$ : $\beta = 0$, $-2\gamma = 0$, $\alpha + \beta + \gamma = 0$, donc $\alpha = \beta = \gamma = 0$. Libre, et $\mathrm{Card}(\mathcal{F}) = 3 = \dim \mathbb{R}^3$ : base.
(b) $\alpha + 2\beta + \gamma = 3$, $\alpha + \beta - \gamma = 2$, $\alpha + \beta + \gamma = 0$ : $\beta = 3$, $\gamma = -1$, $\alpha = -2$. $v = -2u_1 + 3u_2 - u_3$, coordonnées $(-2, 3, -1)$.
2. (a) Oui : tout $P = a + bX + cX^2 = a \cdot 1 + bX + 0(X^2 + X) + cX^2$.
(b) Non : $2 \cdot 1 - X + (X - 2) + 0 \cdot X^2 = 0$.
(c) $Q = 1 \times 1 + 2(X - 1) - (X + 1)^2 = -2 + 0X - X^2$ : coordonnées $(-2, 0, -1)$ dans la base canonique.
3. $P_2 = P_1 - P_0$ et $P_3 = P_0 + P_1$ : $F = \mathrm{Vect}(P_0, P_1)$ ; $(P_0, P_1)$ libre (non colinéaires) : base, $\dim F = 2$.

## Exercice 2 : somme de sev
Type : sous-espaces, intersection, somme directe · ECUE : EV · Niveau : maths-s2-ev/9
Formules : $\mathrm{Vect}(u)$ : droite si $u \neq 0$ ; plan $ax + by + cz = 0$ : exprimer $z$, $G = \mathrm{Vect}(u, v)$ ; $u \in F \cap G$ : paramétrer par $F$ puis injecter l'équation de $G$ ; Grassmann $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $\dim F + \dim G = \dim E$

1. $F$ est un plan vectoriel, $G$ et $H$ sont deux droites vectorielles.
2. $F = \{(x, -2x, z)\} = \{x(1, -2, 0) + z(0, 0, 1)\} = \mathrm{Vect}(e_1, e_2)$, $e_1 = (1, -2, 0)$, $e_2 = (0, 0, 1)$ non colinéaires : base, $\dim F = 2$. $((1, 1, 0))$ est une base de $G$, $\dim G = 1$ ; de même $((-1, 2, 3))$ pour $H$.
3. $u \in H$ : $u = (-\alpha, 2\alpha, 3\alpha)$ et $2(-\alpha) + 2\alpha = 0$ donc $u \in F$. $H \subset F$ et $F \cap H = H \neq \{0_E\}$.
4. $u \in F \cap G$ : $u = (\alpha, \alpha, 0)$ et $2\alpha + \alpha = 0$, donc $\alpha = 0$ : $F \cap G = \{0_E\}$.
5. $F \oplus G = E$ signifie $F + G = E$ et $F \cap G = \{0_E\}$. $\dim(F + G) = 2 + 1 - 0 = 3 = \dim E$ et $F + G \subset E$, donc $F + G = E$ : oui, $F \oplus G = E$.
6. Par exemple $F' = \{(x, y, z) \in \mathbb{R}^3, x + y + z = 0\}$, plan vectoriel avec $F' \cap H = \{0_E\}$.
