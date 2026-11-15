# Examen S2-B4-EV (espaces vectoriels) — mai 2025 (sujet, FR)

- Source : `raw/S2/Finals/Maths PC/2029/PC/EV/midterm-2029-s2-maths-subject-fr.pdf` (6 pages ; rangé dans « Finals » malgré le nom « midterm »)
- Date réelle : mai 2025 (dossier promo 2029, ECUE EV). Corrigé rédigé : `midterm-2029-s2-maths-correction-fr.md` (même dossier).
- Durée : 1 heure. Barème sur 20 points. 2 exercices.

## Exercice 1 : familles de vecteurs (10 points)
Type : familles libres, génératrices, bases ; coordonnées · ECUE : EV · Niveau : maths-s2-ev/7
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \lambda_i = 0$ ; en dimension $n$, une famille libre de $n$ vecteurs est une base ; plus de $n$ vecteurs $\Rightarrow$ liée ; coordonnées : résoudre $P = \alpha Q_1 + \beta Q_2 + \gamma Q_3$ en identifiant les coefficients

Les questions sont indépendantes.
1. Dans $E = \mathbb{R}_2[X]$, on considère la famille $\mathcal{F} = (P_1 = 1, P_2 = X^2 + X + 1, P_3 = X^2 - X + 1)$.
   (a) Montrer que $\mathcal{F}$ est une base de $\mathbb{R}_2[X]$.
   (b) Quelles sont les coordonnées de $Q = 2X^2 + 4X + 4$ dans la base $\mathcal{F}$ ?
2. On se place dans $E = \mathbb{R}^n$. Soient $\varepsilon_1$, $\varepsilon_2$, $\varepsilon_3$ et $\varepsilon_4$ quatre vecteurs non nuls de $E$. On admet que la famille $\mathcal{F} = (\varepsilon_1, \varepsilon_2, \varepsilon_3, \varepsilon_4)$ est libre.
   (a) La famille $\mathcal{F}_1 = (\varepsilon_1, 2\varepsilon_2, \varepsilon_3)$ est-elle libre ? Faire la preuve de ce que vous affirmez.
   (b) Soit $F = \mathrm{Vect}(\mathcal{F}_1)$. Donner une base $\mathcal{B}$ de $F$. Justifier.
   (c) Justifier que $u = \varepsilon_1 + \varepsilon_2 \in F$ et donner ses coordonnées dans la base $\mathcal{B}$.
3. Dans $E = \mathbb{R}^2$, on considère la base $\mathcal{B} = (u_1 = (2, 1), u_2 = (-1, 1))$.
   (a) Dessiner les deux repères (2 carreaux = 1 unité) formés d'une part par la base canonique de $\mathbb{R}^2$, d'autre part par $\mathcal{B}$. Soit $u = (5, 1)$. Trouver graphiquement les coordonnées de $u$ dans la base $\mathcal{B}$. Vous ferez apparaître vos traits de construction.
   (b) Vérifier par le calcul ce que vous avez trouvé dans la question précédente.

## Exercice 2 : somme de sev (10 points)
Type : sous-espaces, intersection, somme directe · ECUE : EV · Niveau : maths-s2-ev/9
Formules : $\mathrm{Vect}(u)$ : droite si $u \neq 0$ ; plan $ax + by + cz = 0$ : exprimer $z$, $G = \mathrm{Vect}(u, v)$ ; $u \in F \cap G$ : paramétrer par $F$ puis injecter l'équation de $G$ ; Grassmann $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $\dim F + \dim G = \dim E$

On se place dans $E = \mathbb{R}^3$. On considère les deux sous-espaces vectoriels $F = \mathrm{Vect}(u = (1, 0, -2), v = (0, 1, 1), w = (1, 1, -1))$ et $G = \left\{(x, y, z) \in E, \begin{cases} x + y + z = 0 \\ x - 2y + z = 0 \end{cases}\right\}$.
1. Trouver rigoureusement une base de $F$. En déduire la dimension de $F$.
2. Trouver rigoureusement une base de $G$. En déduire la dimension de $G$.
3. Montrer que $F \cap G = \{0_E\}$.
4. Rappeler la définition de $F \oplus G = E$. Est-ce le cas ici ? Justifier votre réponse.
