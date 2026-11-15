# Correction examen S2-B4-EV — mai 2026

- Source : `raw/S2/Finals/Maths PC/2030/PC/EV/final-2030-s2-ev-correction-fr.pdf` (3 pages)
- Date réelle : mai 2026 (dossier promo 2030, ECUE EV). Sujet : `final-2030-s2-ev-subject-fr.md` (énoncés repris en abrégé).

## Exercice 1 : sev ou pas
Type : reconnaître un sous-espace vectoriel · ECUE : EV · Niveau : maths-s2-ev/3
Formules : sev : contient 0, stable par addition et multiplication par un scalaire ; contre-exemple $\lambda u \notin E$ ; équation non linéaire ($z^2$) $\Rightarrow$ en général pas un sev ; $\mathrm{Vect}(\dots)$ est toujours un sev

1. $u = (1, 1, 1) \in E$ mais $2u = (2, 2, 2) \notin E$ car $2 - 2^2 = -2 \neq 0$ : $E$ n'est pas stable par multiplication externe, ce n'est pas un $\mathbb{R}$-ev.
2. $F = \mathrm{Vect}((2^n), (3^n))$ : sous-espace vectoriel de $\mathbb{R}^{\mathbb{N}}$, donc un $\mathbb{R}$-ev.

## Exercice 2 : bases ou pas
Type : familles libres, génératrices, bases · ECUE : EV · Niveau : maths-s2-ev/6
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \forall i, \lambda_i = 0$ ; génératrice : tout vecteur est combinaison linéaire ; base = libre + génératrice ; $\dim \mathbb{R}_n[X] = n + 1$ ; en dimension $n$ : plus de $n$ vecteurs $\Rightarrow$ liée, moins de $n$ $\Rightarrow$ non génératrice, $n$ vecteurs libres $\Rightarrow$ base ; degrés échelonnés $\Rightarrow$ libre

- $\mathcal{F}_1$ : $u_1 - 2u_2 = u_3$, famille liée : pas une base.
- $\mathcal{F}_2$ : $\alpha v_1 + \beta v_2 + \gamma v_3 = 0 \iff \alpha + 2\beta + 2\gamma = 0$ $(L_1)$, $\alpha + 2\beta + 3\gamma = 0$ $(L_2)$, $\alpha + \beta + 2\gamma = 0$ $(L_3)$. $L_2 - L_1$ : $\gamma = 0$ ; $L_3 - L_1$ : $\beta = 0$ ; d'où $\alpha = 0$. Libre et $\mathrm{Card} = 3 = \dim \mathbb{R}^3$ : base.

## Exercice 3 : coordonnées
Type : familles libres, génératrices, bases ; coordonnées · ECUE : EV · Niveau : maths-s2-ev/7
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \lambda_i = 0$ ; en dimension $n$, une famille libre de $n$ vecteurs est une base ; plus de $n$ vecteurs $\Rightarrow$ liée ; coordonnées : résoudre $P = \alpha Q_1 + \beta Q_2 + \gamma Q_3$ en identifiant les coefficients

1. (a) $P = P_1 + 2P_2 - P_3 = 1 - X + 2(1 + X) - (1 + X)^2 = 2 - X - X^2$ : coordonnées $(2, -1, -1)$ dans la base canonique $(1, X, X^2)$.
(b) $Q = 2X^2 + 1$ : $(1, 0, 2)$ dans la base canonique. $\alpha P_1 + \beta P_2 + \gamma P_3 = Q \iff \alpha + \beta + \gamma = 1$, $-\alpha + \beta + 2\gamma = 0$, $\gamma = 2$ : $\alpha = \frac32$, $\beta = -\frac52$, $\gamma = 2$.
2. (a) Graphiquement, $u = -u_1 + 2u_2$ : coordonnées $(-1, 2)$.
(b) $-u_1 + 2u_2 = -(3, 2) + 2(-1, 2) = (-5, 2)$.

## Exercice 4 : sev engendrés
Type : sous-espaces engendrés, inclusion, dimension · ECUE : EV · Niveau : maths-s2-ev/4
Formules : $P \in \mathrm{Vect}(u_1, \dots) \iff P$ combinaison linéaire des $u_i$ ; $F \subset G$ si les générateurs de $F$ sont dans $G$ ; famille génératrice libre = base, $\dim$ = cardinal

1. $P = 2(X^2 + X) \in F$ et $Q = 2X^2 + 3X \notin F$.
2. $Q = 2X^2 + 3X \in G$ et $R = 2X^2 + 3X + 2 \notin G$.
3. $Q \in G$, $Q \notin F$ : $G \not\subset F$. Si $P \in F$, $P = \alpha X^2 + \alpha X \in G$ : $F \subset G$.
4. $(X^2 + X)$ non nul : base de $F$, $\dim F = 1$. $(X^2, X)$ non colinéaires : base de $G$, $\dim G = 2$.

## Exercice 5 : sev supplémentaires ?
Type : sous-espaces, intersection, somme directe · ECUE : EV · Niveau : maths-s2-ev/9
Formules : $\mathrm{Vect}(u)$ : droite si $u \neq 0$ ; plan $ax + by + cz = 0$ : exprimer $z$, $G = \mathrm{Vect}(u, v)$ ; $u \in F \cap G$ : paramétrer par $F$ puis injecter l'équation de $G$ ; Grassmann $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $\dim F + \dim G = \dim E$

1. $u_2 = -2u_1$ donc $F = \mathrm{Vect}(u_1)$ ; $u_1 \neq 0$ : base $(u_1)$, $\dim F = 1$.
2. $G = \{(x, -2x, z)\} = \mathrm{Vect}(v_1 = (1, -2, 0), v_2 = (0, 0, 1))$ ; non colinéaires : base, $\dim G = 2$.
3. $u \in F \cap G$ : $u = (\alpha, 2\alpha, -\alpha)$ et $2\alpha + 2\alpha = 0$, donc $\alpha = 0$ : $F \cap G = \{0_E\}$.
4. $F \oplus G = E \iff E = F + G$ et $F \cap G = \{0_E\}$. $\dim(F + G) = 1 + 2 - 0 = 3$ et $F + G \subset E$ : $F \oplus G = E$.
5. $F'$ doit être un plan vectoriel différent de $G$, par exemple $F' = \{(x, y, z), y = 0\}$.
6. $H$ doit être une droite vectorielle, par exemple $H = \{(x, y, z), x = y = 0\}$.
