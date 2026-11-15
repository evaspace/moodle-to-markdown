# Examen S2-B4-EV (espaces vectoriels) — mai 2026 (sujet, FR)

- Source : `raw/S2/Finals/Maths PC/2030/PC/EV/final-2030-s2-ev-subject-fr.pdf` (7 pages)
- Date réelle : mai 2026 (dossier promo 2030, ECUE EV). Corrigé : `final-2030-s2-ev-correction-fr.md`.
- Durée : 2 heures. Barème sur 30 points ramené à 20. 5 exercices.

## Exercice 1 : sev ou pas (4 points)
Type : reconnaître un sous-espace vectoriel · ECUE : EV · Niveau : maths-s2-ev/3
Formules : sev : contient 0, stable par addition et multiplication par un scalaire ; contre-exemple $\lambda u \notin E$ ; équation non linéaire ($z^2$) $\Rightarrow$ en général pas un sev ; $\mathrm{Vect}(\dots)$ est toujours un sev

Les ensembles suivants sont-ils des $\mathbb{R}$-espaces vectoriels ?
1. $E = \{(x, y, z) \in \mathbb{R}^3, x - y = 0$ et $y - z^2 = 0\}$.
2. $F = \{(u_n) \in \mathbb{R}^{\mathbb{N}}, \exists (\alpha, \beta) \in \mathbb{R}^2, \forall n \in \mathbb{N}, u_n = \alpha \times 2^n + \beta \times 3^n\}$.

## Exercice 2 : bases ou pas (4 points)
Type : familles libres, génératrices, bases · ECUE : EV · Niveau : maths-s2-ev/6
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \forall i, \lambda_i = 0$ ; génératrice : tout vecteur est combinaison linéaire ; base = libre + génératrice ; $\dim \mathbb{R}_n[X] = n + 1$ ; en dimension $n$ : plus de $n$ vecteurs $\Rightarrow$ liée, moins de $n$ $\Rightarrow$ non génératrice, $n$ vecteurs libres $\Rightarrow$ base ; degrés échelonnés $\Rightarrow$ libre

On se place dans $\mathbb{R}^3$. On considère les familles $\mathcal{F}_1 = (u_1 = (1, -1, 2), u_2 = (1, -2, 1), u_3 = (-1, 3, 0))$ et $\mathcal{F}_2 = (v_1 = (1, 1, 1), v_2 = (2, 2, 1), v_3 = (2, 3, 2))$. $\mathcal{F}_1$ et $\mathcal{F}_2$ sont-elles des bases de $\mathbb{R}^3$ ?

## Exercice 3 : coordonnées (6 points)
Type : familles libres, génératrices, bases ; coordonnées · ECUE : EV · Niveau : maths-s2-ev/7
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \lambda_i = 0$ ; en dimension $n$, une famille libre de $n$ vecteurs est une base ; plus de $n$ vecteurs $\Rightarrow$ liée ; coordonnées : résoudre $P = \alpha Q_1 + \beta Q_2 + \gamma Q_3$ en identifiant les coefficients

1. On se place dans $E = \mathbb{R}_2[X]$. On considère la base $\mathcal{B} = (P_1 = 1 - X, P_2 = 1 + X, P_3 = (1 + X)^2)$ de $E$.
   (a) Soit $P \in E$ dont les coordonnées dans $\mathcal{B}$ sont $(1, 2, -1)$. Trouver les coordonnées de $P$ dans la base canonique de $E$.
   (b) Soit $Q = 2X^2 + 1$. Donner les coordonnées de $Q$ d'une part dans la base canonique de $E$, d'autre part dans $\mathcal{B}$.
2. Dans $E = \mathbb{R}^2$, on considère la base $\mathcal{B} = (u_1 = (3, 2), u_2 = (-1, 2))$.
   (a) Dessiner les deux repères (2 carreaux = 1 unité) formés d'une part par la base canonique de $\mathbb{R}^2$, d'autre part par $\mathcal{B}$. Soit $u = (-5, 2)$. Trouver graphiquement les coordonnées de $u$ dans la base $\mathcal{B}$. Vous ferez apparaître vos traits de construction.
   (b) Vérifier par le calcul ce que vous avez trouvé dans la question précédente.

## Exercice 4 : sev engendrés (6 points)
Type : sous-espaces engendrés, inclusion, dimension · ECUE : EV · Niveau : maths-s2-ev/4
Formules : $P \in \mathrm{Vect}(u_1, \dots) \iff P$ combinaison linéaire des $u_i$ ; $F \subset G$ si les générateurs de $F$ sont dans $G$ ; famille génératrice libre = base, $\dim$ = cardinal

Dans $\mathbb{R}_2[X]$, on considère les sous-espaces vectoriels $F = \mathrm{Vect}(X^2 + X)$ et $G = \mathrm{Vect}(X^2, X)$.
1. Donner un vecteur appartenant à $F$ et un vecteur n'appartenant pas à $F$. Ne pas justifier.
2. Donner un vecteur appartenant à $G$ et un vecteur n'appartenant pas à $G$. Ne pas justifier.
3. A-t-on $F \subset G$ ? $G \subset F$ ?
4. Trouver la dimension de $F$ et la dimension de $G$.

## Exercice 5 : sev supplémentaires ? (10 points)
Type : sous-espaces, intersection, somme directe · ECUE : EV · Niveau : maths-s2-ev/9
Formules : $\mathrm{Vect}(u)$ : droite si $u \neq 0$ ; plan $ax + by + cz = 0$ : exprimer $z$, $G = \mathrm{Vect}(u, v)$ ; $u \in F \cap G$ : paramétrer par $F$ puis injecter l'équation de $G$ ; Grassmann $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $\dim F + \dim G = \dim E$

On se place dans $E = \mathbb{R}^3$. On considère $F$ le sous-espace vectoriel engendré par $u_1 = (1, 2, -1)$ et $u_2 = (-2, -4, 2)$, et $G = \{(x, y, z) \in \mathbb{R}^3, 2x + y = 0\}$.
1. Trouver rigoureusement une base de $F$. En déduire la dimension de $F$.
2. Trouver rigoureusement une base de $G$. En déduire la dimension de $G$.
3. Montrer que $F \cap G = \{0_E\}$.
4. Rappeler la définition de $F \oplus G = E$. Est-ce le cas ici ?
5. Proposer $F'$ sous-espace vectoriel de $E$ tel que $F' \cap G \neq \{0_E\}$ mais $F' + G = E$. Vous préciserez ce que représente géométriquement $F'$ mais ne pas justifier votre choix.
6. Proposer $H$ sous-espace vectoriel de $E$ tel que $H \cap F = \{0_E\}$ mais $H + F \neq E$. Vous préciserez ce que représente géométriquement $H$ mais ne pas justifier votre choix.
