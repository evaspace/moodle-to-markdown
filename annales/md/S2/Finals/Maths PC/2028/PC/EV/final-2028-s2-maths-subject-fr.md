# Examen S2-B4-EV (espaces vectoriels) — juin 2024 (sujet, FR)

- Source : `raw/S2/Finals/Maths PC/2028/PC/EV/final-2028-s2-maths-subject-fr.pdf` (6 pages)
- Date réelle : juin 2024 (dossier promo 2028, ECUE EV). Corrigé : `final-2028-s2-maths-correction-fr.md`.
- Durée : 1 heure. Barème sur 20 points. 2 exercices. Rigueur prise en compte.

## Exercice 1 : familles de vecteurs (10 points)
Type : familles libres, génératrices, bases ; coordonnées · ECUE : EV · Niveau : maths-s2-ev/7
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \lambda_i = 0$ ; en dimension $n$, une famille libre de $n$ vecteurs est une base ; plus de $n$ vecteurs $\Rightarrow$ liée ; coordonnées : résoudre $P = \alpha Q_1 + \beta Q_2 + \gamma Q_3$ en identifiant les coefficients

Les questions sont indépendantes.
1. Dans $\mathbb{R}^3$, on considère la famille $\mathcal{F} = (u_1 = (1, 1, 1), u_2 = (2, 1, 1), u_3 = (1, -1, 1))$.
   (a) Montrer que $\mathcal{F}$ est une base de $\mathbb{R}^3$.
   (b) Quelles sont les coordonnées de $v = (3, 2, 0)$ dans la base $\mathcal{F}$ ?
2. On se place dans $E = \mathbb{R}_2[X]$.
   (a) La famille $\mathcal{F}_1 = (1, X, X^2 + X, X^2)$ est-elle génératrice de $E$ ? Justifiez votre réponse.
   (b) La famille $\mathcal{F}_2 = (1, X, X - 2, X^2)$ est-elle une famille libre de $E$ ? Justifiez votre réponse.
   (c) On admet que la famille $\mathcal{F}_3 = (1, X - 1, (X + 1)^2)$ est une base de $E$. Soit $Q \in E$ le polynôme de coordonnées 1, 2 et $-1$ dans la base $\mathcal{F}_3$. Quelles sont les coordonnées de $Q$ dans la base canonique de $E$ ?
3. Dans $\mathbb{R}[X]$, on considère $P_0 = 1$, $P_1 = X$, $P_2 = X - 1$ et $P_3 = X + 1$. Soit le sous-espace vectoriel $F = \mathrm{Vect}((P_0, P_1, P_2, P_3))$. Trouver la dimension de $F$, en justifiant soigneusement votre raisonnement.

## Exercice 2 : somme de sev (10 points)
Type : sous-espaces, intersection, somme directe · ECUE : EV · Niveau : maths-s2-ev/9
Formules : $\mathrm{Vect}(u)$ : droite si $u \neq 0$ ; plan $ax + by + cz = 0$ : exprimer $z$, $G = \mathrm{Vect}(u, v)$ ; $u \in F \cap G$ : paramétrer par $F$ puis injecter l'équation de $G$ ; Grassmann $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $\dim F + \dim G = \dim E$

On se place dans $E = \mathbb{R}^3$. On considère les trois sous-espaces vectoriels $F = \{(x, y, z) \in \mathbb{R}^3, 2x + y = 0\}$, $G = \mathrm{Vect}((1, 1, 0))$ et $H = \mathrm{Vect}((-1, 2, 3))$.
1. Que représentent géométriquement $F$, $G$ et $H$ ?
2. Trouver rigoureusement une base de $F$, de $G$ et de $H$.
3. Montrer que $H \subset F$. En déduire que $F \cap H \neq \{0_E\}$.
4. Montrer que $F \cap G = \{0_E\}$.
5. Rappeler la définition de $F \oplus G = E$. Est-ce le cas ici ? Démontrer votre réponse.
6. Proposer un supplémentaire de $H$ dans $E$. Justification non demandée.
