# Feuille de TD — Espaces vectoriels (S2 2026) (sujet, FR)

- Source : `raw/S2/TDs/2030/Maths/td4-2030-s2-maths-subject-fr.pdf` (11 pages)
- Date réelle : S2 2026 (dossier promo 2030). Feuille de TD, ECUE EV. Pas de corrigé dans les annales. Corrigé rédigé : `td4-2030-s2-maths-correction-fr.md` (même dossier).
- Seuls les exercices sont transcrits, avec les définitions à connaître. Les exercices marqués ⋆ sont plus difficiles.

Définitions à connaître (somme directe, supplémentaires). Soient $E$ un $\mathbb{R}$-espace vectoriel et $F$, $G$ deux sous-espaces vectoriels de $E$.
- $F$ et $G$ sont en somme directe si $F \cap G = \{0_E\}$.
- $F$ et $G$ sont supplémentaires dans $E$ si $E = F + G$ et si $F$ et $G$ sont en somme directe. On note alors $E = F \oplus G$ : $E = F \oplus G \iff (E = F + G \text{ et } F \cap G = \{0_E\})$.
- $E = F \oplus G \iff \forall u \in E,\ \exists!\,(v,w) \in F \times G,\ u = v + w$.

## Exercice 1.1
Type : vecteurs du plan, combinaisons linéaires (dessin) · ECUE : EV · Niveau : maths-s2-ev/1
Formules : $(x,y) + (x',y') = (x + x', y + y')$ ; $\alpha(x,y) = (\alpha x, \alpha y)$ ; $\{\alpha u\}$ : droite vectorielle dirigée par $u \neq 0$ ; $\{\alpha u + \beta v\}$ avec $u$, $v$ non colinéaires : le plan $\mathbb{R}^2$ (un plan vectoriel dans $\mathbb{R}^3$) ; relation de Chasles pour construire $u + v$

On se place dans l'espace vectoriel $\mathbb{R}^2$. On cherche dans cet exercice à dessiner (quadrillage, 2 carreaux = 1 unité).
1. Dessiner les axes du plan $\mathbb{R}^2$ et représenter le vecteur $u = (3,1)$.
2. Représenter les vecteurs $2u$, $-u$, $-\frac12u$ et $0u$. Lire graphiquement leurs coordonnées. À votre avis, que représente l'ensemble $D = \{\alpha u,\ \alpha \in \mathbb{R}\}$ ?
3. Ajouter sur le dessin le vecteur $v = (-2,1)$. Construire alors les vecteurs $u + v$, $v - u$, $2u + 3v$. Lire graphiquement leurs coordonnées. À votre avis, que représente l'ensemble $E = \{\alpha u + \beta v,\ (\alpha,\beta) \in \mathbb{R}^2\}$ ?
4. Définir l'addition interne $+$ et la multiplication externe $\cdot$ du $\mathbb{R}$-espace vectoriel $\mathbb{R}^2$. Vérifier la cohérence avec vos résultats graphiques.
5. À votre avis, que représentent les ensembles $D$ et $E$ si $u$ et $v$ sont des vecteurs de $\mathbb{R}^3$ ?

## Exercice 1.2
Type : axiomes d'un espace vectoriel (loi externe non standard) · ECUE : EV · Niveau : maths-s2-ev/2
Formules : $\mathbb{R}$-ev : $(E,+)$ groupe commutatif ; $1.u = u$ ; $\alpha.(\beta.u) = (\alpha\beta).u$ ; $(\alpha + \beta).u = \alpha.u + \beta.u$ ; $\alpha.(u + v) = \alpha.u + \alpha.v$ ; un seul axiome en défaut (contre-exemple chiffré) suffit pour conclure que ce n'est pas un ev

(Travail personnel) On s'intéresse à l'ensemble $E$ des tableaux de réels répartis en 2 lignes et 2 colonnes sous la forme $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ où $a$, $b$, $c$ et $d$ sont réels. On définit sur $E$ deux opérations notées $+$ et $\cdot$ : pour $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ et $B = \begin{pmatrix} a' & b' \\ c' & d' \end{pmatrix}$, $A + B = \begin{pmatrix} a + a' & b + b' \\ c + c' & d + d' \end{pmatrix}$ ; et pour tout $\alpha \in \mathbb{R}$, $\alpha \cdot A = \begin{pmatrix} \alpha a & \alpha b \\ \alpha c & \alpha d \end{pmatrix}$.
1. Quel serait l'élément neutre pour chacune des lois $+$ et $\cdot$ ainsi définies sur $E$ ?
2. Vérifiez que les propriétés qui font de $E$ un espace vectoriel sur $\mathbb{R}$ sont bien satisfaites.

## Exercice 1.3
Type : axiomes d'un espace vectoriel (loi externe non standard) · ECUE : EV · Niveau : maths-s2-ev/2
Formules : $\mathbb{R}$-ev : $(E,+)$ groupe commutatif ; $1.u = u$ ; $\alpha.(\beta.u) = (\alpha\beta).u$ ; $(\alpha + \beta).u = \alpha.u + \beta.u$ ; $\alpha.(u + v) = \alpha.u + \alpha.v$ ; un seul axiome en défaut (contre-exemple chiffré) suffit pour conclure que ce n'est pas un ev

Soient $f$ et $g$ deux fonctions numériques définies sur un intervalle $I$ de $\mathbb{R}$.
1. On note $E$ l'ensemble des fonctions de $I$ dans $\mathbb{R}$. Que signifie $0_E$ ?
2. On dit que l'addition des fonctions est une opération interne sur l'ensemble $E$. Que signifie interne dans cette appellation ? Définissez cette opération comme une application en précisant bien les ensembles de départ et d'arrivée.
3. Soit $\alpha$ un réel quelconque, qu'est-ce que la fonction $\alpha f$ ? On dit que la multiplication des fonctions par un réel est une opération externe. Selon vous pourquoi ? Définissez cette opération comme une application en précisant bien les ensembles de départ et d'arrivée.
4. $E$ se note aussi $\mathbb{R}^I$. À votre avis, muni des deux opérations définies précédemment, $\mathbb{R}^I$ est-il un $\mathbb{R}$-espace vectoriel ?

## Exercice 1.4
Type : axiomes d'un espace vectoriel (loi externe non standard) · ECUE : EV · Niveau : maths-s2-ev/2
Formules : $\mathbb{R}$-ev : $(E,+)$ groupe commutatif ; $1.u = u$ ; $\alpha.(\beta.u) = (\alpha\beta).u$ ; $(\alpha + \beta).u = \alpha.u + \beta.u$ ; $\alpha.(u + v) = \alpha.u + \alpha.v$ ; un seul axiome en défaut (contre-exemple chiffré) suffit pour conclure que ce n'est pas un ev

On s'intéresse à l'ensemble des suites réelles $\mathbb{R}^{\mathbb{N}}$. On définit sur $\mathbb{R}^{\mathbb{N}}$ l'opération externe donnée pour tout $\alpha \in \mathbb{R}$ et $(u_n)_{n \in \mathbb{N}}$ par $\alpha \cdot (u_n) = (\alpha^nu_n) = (u_0, \alpha u_1, \alpha^2u_2, \alpha^3u_3, \dots)$.
1. Quel serait l'élément neutre d'une telle opération ?
2. Si l'on munit $\mathbb{R}^{\mathbb{N}}$ de l'opération interne d'addition, obtient-on un espace vectoriel sur $\mathbb{R}$ ?

## Exercice 1.5
Type : axiomes d'un espace vectoriel (loi externe non standard) · ECUE : EV · Niveau : maths-s2-ev/2
Formules : $\mathbb{R}$-ev : $(E,+)$ groupe commutatif ; $1.u = u$ ; $\alpha.(\beta.u) = (\alpha\beta).u$ ; $(\alpha + \beta).u = \alpha.u + \beta.u$ ; $\alpha.(u + v) = \alpha.u + \alpha.v$ ; un seul axiome en défaut (contre-exemple chiffré) suffit pour conclure que ce n'est pas un ev

Faire la liste de tous les $\mathbb{R}$-espaces vectoriels de référence, en précisant pour chacun d'entre eux les deux opérations $+$ et $\cdot$ ainsi que le vecteur nul.

## Exercice 2.6
Type : reconnaître un sous-espace vectoriel · ECUE : EV · Niveau : maths-s2-ev/3
Formules : sev : contient 0, stable par addition et multiplication par un scalaire ; contre-exemple $\lambda u \notin E$ ; équation non linéaire ($z^2$) $\Rightarrow$ en général pas un sev ; $\mathrm{Vect}(\dots)$ est toujours un sev

On s'intéresse aux sous-espaces vectoriels de $\mathbb{R}^2$ et $\mathbb{R}^3$.
1. On se focalise pour commencer sur le cas de $\mathbb{R}^2$. Vous êtes à nouveau invités à dessiner.
   - (a) Dessiner les sous-ensembles de $\mathbb{R}^2$ ci-dessous et indiquer ceux qui représentent un sous-espace vectoriel. Pour ceux qui n'en sont pas, en indiquer la raison. On appelle $O$ le point de coordonnées $(0,0)$. $A$ : le singleton $\{O\}$ ; $B$ : disque de rayon 1 et de centre $O$ ; $C$ : demi-plan $x \geqslant 0$ ; $D$ : axe des abscisses ; $E$ : droite $x + y = 0$ ; $F$ : droite $x + y = 1$.
   - (b) Est-il possible d'avoir deux sous-espaces vectoriels d'un même espace vectoriel qui soient disjoints ?
   - (c) À votre avis, quels sont les sous-espaces vectoriels de $\mathbb{R}^2$ ?
2. Décrire les sous-espaces vectoriels de $\mathbb{R}^3$.

## Exercice 2.7
Type : reconnaître un sous-espace vectoriel · ECUE : EV · Niveau : maths-s2-ev/3
Formules : sev : contient 0, stable par addition et multiplication par un scalaire ; contre-exemple $\lambda u \notin E$ ; équation non linéaire ($z^2$) $\Rightarrow$ en général pas un sev ; $\mathrm{Vect}(\dots)$ est toujours un sev

1. Que représente l'ensemble $E = \{aX^2 + bX + c,\ (a,b,c) \in \mathbb{R}^3\}$ ?
2. En utilisant une écriture similaire en compréhension, décrire l'ensemble $F$ des polynômes de degré deux exactement.
3. Quel est le lien entre $E$ et $F$ ? Dans quel espace vectoriel de référence sont-ils inclus ?
4. Qu'est-ce que le polynôme nul ? Appartient-il à $E$ ? à $F$ ?
5. $E$ et $F$ sont-ils stables pour le produit externe $\cdot$ ? pour l'opération interne $+$ ?

## Exercice 2.8
Type : reconnaître un sous-espace vectoriel · ECUE : EV · Niveau : maths-s2-ev/3
Formules : sev : contient 0, stable par addition et multiplication par un scalaire ; contre-exemple $\lambda u \notin E$ ; équation non linéaire ($z^2$) $\Rightarrow$ en général pas un sev ; $\mathrm{Vect}(\dots)$ est toujours un sev

Les ensembles suivants sont-ils des $\mathbb{R}$-ev ?
1. $F = \{(x,y,z) \in \mathbb{R}^3,\ x + y + z = 0\}$
2. $F = \{(x,y,z) \in \mathbb{R}^3,\ x + y + z = 1\}$
3. (Travail personnel) $F = \{(x,y,z) \in \mathbb{R}^3,\ xy = 0\}$
4. $F = \{(x,y,z) \in \mathbb{R}^3,\ x^2 = z^2\}$
5. $F = \{P \in \mathbb{R}[X],\ XP'' - 3P = 0\}$
6. $F = \{P \in \mathbb{R}[X],\ P'(3) = 0\}$
7. (Travail personnel) $F = \{(u_n) \in \mathbb{R}^{\mathbb{N}},\ (u_n) \text{ convergente}\}$
8. $F = \{(u_n) \in \mathbb{R}^{\mathbb{N}},\ \forall n \in \mathbb{N},\ u_{n+1} = 3u_n - 1\}$
9. $F = \{(u_n) \in \mathbb{R}^{\mathbb{N}},\ (u_n) \text{ divergente}\}$
10. $F = \{(u_n) \in \mathbb{R}^{\mathbb{N}},\ \forall n \in \mathbb{N},\ u_{n+2} = 2u_{n+1} - u_n\}$
11. $F = \{(u_n) \in \mathbb{R}^{\mathbb{N}},\ \forall n \in \mathbb{N},\ u_{n+2} = 2u_{n+1} - u_n^2\}$
12. (Travail personnel) $F = \{(u_n) \in \mathbb{R}^{\mathbb{N}},\ \exists (\alpha,\beta,\gamma) \in \mathbb{R}^3,\ \forall n \in \mathbb{N},\ u_n = \alpha 2^n + \beta 3^n + \gamma 4^n\}$
13. $F = \{f \in \mathbb{R}^{\mathbb{R}},\ f \text{ croissante}\}$
14. $F = \{f \in \mathbb{R}^{\mathbb{R}},\ f(0) = 0\}$
15. (Travail personnel) $F = \{f \in \mathbb{R}^{\mathbb{R}},\ f \text{ paire}\}$
16. $F = \{f \in \mathbb{R}^{\mathbb{R}},\ \lim_{+\infty} f = +\infty\}$
17. (Travail personnel) $F = \{f \in \mathbb{R}^{\mathbb{R}},\ f \text{ continue}\}$
18. $F = \{f \in C^0([a,b], \mathbb{R}),\ \int_a^b f(t)\,dt = 0\}$

## Exercice 2.9
Type : sous-espaces, intersection, somme directe · ECUE : EV · Niveau : maths-s2-ev/9
Formules : $\mathrm{Vect}(u)$ : droite si $u \neq 0$ ; plan $ax + by + cz = 0$ : exprimer $z$, $G = \mathrm{Vect}(u, v)$ ; $u \in F \cap G$ : paramétrer par $F$ puis injecter l'équation de $G$ ; Grassmann $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $\dim F + \dim G = \dim E$

Soient $F$ et $G$ deux sev d'un $\mathbb{R}$-ev $E$. Étudier l'assertion : $F \cup G$ sev de $E$ $\iff$ $F \subset G$ ou $G \subset F$.

## Exercice 2.10
Type : sous-espaces, intersection, somme directe · ECUE : EV · Niveau : maths-s2-ev/9
Formules : $\mathrm{Vect}(u)$ : droite si $u \neq 0$ ; plan $ax + by + cz = 0$ : exprimer $z$, $G = \mathrm{Vect}(u, v)$ ; $u \in F \cap G$ : paramétrer par $F$ puis injecter l'équation de $G$ ; Grassmann $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $\dim F + \dim G = \dim E$

Dans l'espace vectoriel $E = \mathbb{R}^2$, on considère les vecteurs $u = (2,4)$, $v = (3,1)$ et $w = (-1,-2)$.
1. Soit l'ensemble $F = \{(x,y) \in \mathbb{R}^2,\ \exists \alpha \in \mathbb{R},\ (x,y) = \alpha u\}$. Montrer que $F$ est un sous-espace vectoriel de $\mathbb{R}^2$.
2. On considère de plus les ensembles $G = \{(x,y) \in \mathbb{R}^2,\ \exists \alpha \in \mathbb{R},\ (x,y) = \alpha v\}$ et $H = \{(x,y) \in \mathbb{R}^2,\ \exists \alpha \in \mathbb{R},\ (x,y) = \alpha w\}$.
   - (a) À votre avis, $G$ et $H$ sont-ils des $\mathbb{R}$-espaces vectoriels ?
   - (b) Que représentent géométriquement ces 3 ensembles ? Les dessiner.
   - (c) Soit $X = (-2, 6)$. Graphiquement, voir si $X \in F + G$ et si $X \in F + H$.
   - (d) Que peut-on dire de $F + G$ et de $F + H$ ?

## Exercice 2.11
Type : sous-espaces, intersection, somme directe · ECUE : EV · Niveau : maths-s2-ev/9
Formules : $\mathrm{Vect}(u)$ : droite si $u \neq 0$ ; plan $ax + by + cz = 0$ : exprimer $z$, $G = \mathrm{Vect}(u, v)$ ; $u \in F \cap G$ : paramétrer par $F$ puis injecter l'équation de $G$ ; Grassmann $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $\dim F + \dim G = \dim E$

Soient $E$ un $\mathbb{R}$-ev et $F$, $G$ et $H$ trois sev de $E$ tels que $F \oplus G = E$ et $F \oplus H = E$. Peut-on en conclure que $G = H$ ? Justifier votre réponse en vous inspirant de l'exercice précédent.

## Exercice 2.12
Type : sous-espaces, intersection, somme directe · ECUE : EV · Niveau : maths-s2-ev/9
Formules : $\mathrm{Vect}(u)$ : droite si $u \neq 0$ ; plan $ax + by + cz = 0$ : exprimer $z$, $G = \mathrm{Vect}(u, v)$ ; $u \in F \cap G$ : paramétrer par $F$ puis injecter l'équation de $G$ ; Grassmann $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $\dim F + \dim G = \dim E$

Dans $E = \mathbb{R}^3$, on considère les trois sous-espaces vectoriels $F = \{(x,y,z) \in \mathbb{R}^3,\ x + y = 0\}$, $G = \{(x,y,z) \in \mathbb{R}^3,\ z = 0\}$ et $H = \{(x,y,z) \in \mathbb{R}^3,\ y = z = 0\}$.
1. A-t-on $F \cap G = \{0_E\}$ et $F \cap H = \{0_E\}$ ?
2. A-t-on $F \oplus G = \mathbb{R}^3$ et $F \oplus H = \mathbb{R}^3$ ? Justifier.

## Exercice 2.13 (⋆)
Type : sous-espaces supplémentaires (fonctions paires et impaires) · ECUE : EV · Niveau : maths-s2-ev/9
Formules : sev : non vide, stable par $\lambda f + g$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $F + G = E$ ; $f = \frac{f(x) + f(-x)}2 + \frac{f(x) - f(-x)}2$ ; paire et impaire $\Rightarrow f = 0$

On se place dans le cas de l'espace vectoriel des fonctions réelles $\mathbb{R}^{\mathbb{R}}$.
1. Rappeler la définition de la parité d'une fonction.
2. On note respectivement $\mathcal{P}$ et $\mathcal{I}$ les espaces des fonctions dans $\mathbb{R}^{\mathbb{R}}$ paires et impaires. Ce sont deux sous-espaces vectoriels de $\mathbb{R}^{\mathbb{R}}$. Que pouvez-vous dire de leur somme ?
3. On note $A$ une partie de $\mathbb{R}$ et $E_A \subset \mathbb{R}^{\mathbb{R}}$ le sous-ensemble des fonctions qui s'annulent sur $A$. Trouver un supplémentaire de $E_A$ dans $\mathbb{R}^{\mathbb{R}}$.
4. Comment adapter les notions précédentes aux cas de $\mathbb{R}[X]$ et de $\mathbb{R}_3[X]$ ?

## Exercice 3.14
Type : familles libres, génératrices, bases · ECUE : EV · Niveau : maths-s2-ev/6
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \forall i, \lambda_i = 0$ ; génératrice : tout vecteur est combinaison linéaire ; base = libre + génératrice ; $\dim \mathbb{R}_n[X] = n + 1$ ; en dimension $n$ : plus de $n$ vecteurs $\Rightarrow$ liée, moins de $n$ $\Rightarrow$ non génératrice, $n$ vecteurs libres $\Rightarrow$ base ; degrés échelonnés $\Rightarrow$ libre

Pour chacune des familles de vecteurs suivantes, dire si elle est libre ou liée :
1. $\mathcal{F}_1 = (u = (1,0),\ v = (0,2),\ w = (-3,4))$ dans $\mathbb{R}^2$.
2. $\mathcal{F}_2 = (v_1, v_2, v_3)$ avec $v_1 = (1,-1,1)$, $v_2 = (0,1,2)$ et $v_3 = (1,0,3)$ dans $\mathbb{R}^3$.
3. $\mathcal{F}_3 = (w_1, w_2)$ avec $w_1 = (2,-1,3)$ et $w_2 = (-8,4,12)$ dans $\mathbb{R}^3$.
4. $\mathcal{F}_4 = (u_1, u_2, u_3)$ avec $u_1 = (5,2,-11)$, $u_2 = (1,1,2)$, $u_3 = (-1,0,3)$ dans $\mathbb{R}^3$.
5. (Travail personnel) $\mathcal{F}_5 = (u_1, u_2, u_3)$ avec $u_1 = (1,1,1)$, $u_2 = (1,-1,0)$, $u_3 = (-1,1,-1)$ dans $\mathbb{R}^3$.
6. $\mathcal{F}_6 = (P, Q, R)$ dans $\mathbb{R}[X]$ où $P(X) = 1 - X + X^2$, $Q(X) = 3 + X - 2X^2$, $R(X) = -1 - 3X + 4X^2$.
7. (Travail personnel) $\mathcal{F}_7 = (P, Q, R)$ dans $\mathbb{R}[X]$ où $P(X) = 1$, $Q(X) = X^2 + X + 1$, $R(X) = X^2 - X + 1$.
8. (⋆) $\mathcal{F}_8 = ((u_n), (v_n), (w_n))$ dans $\mathbb{R}^{\mathbb{N}}$ où $(u_n) = (2^n)$, $(v_n) = (3^n)$ et $(w_n) = (4^n)$.
9. (⋆) $\mathcal{F}_9 = (f, g, h)$ dans $\mathbb{R}^{\mathbb{R}}$ définies par : $\forall x \in \mathbb{R}$, $f(x) = e^x$, $g(x) = xe^x$ et $h(x) = e^{-x}$.

## Exercice 3.15
Type : sous-espaces engendrés, inclusion, dimension · ECUE : EV · Niveau : maths-s2-ev/4
Formules : $P \in \mathrm{Vect}(u_1, \dots) \iff P$ combinaison linéaire des $u_i$ ; $F \subset G$ si les générateurs de $F$ sont dans $G$ ; famille génératrice libre = base, $\dim$ = cardinal

1. Soient $E$ un $\mathbb{R}$-espace vectoriel et $\mathcal{F} = (e_1, e_2, \dots, e_n)$ une famille de $n$ vecteurs non nuls. Écrire mathématiquement l'ensemble $C$ des combinaisons linéaires des vecteurs de $\mathcal{F}$. À votre avis, $C$ est-il un sous-espace vectoriel de $E$ ? Comment « note-t-on » $C$ dans la théorie des ev ?
2. Dans $\mathbb{R}^3$, soient $u = (1,1,0)$, $v = (-1,2,1)$ et $w = (-2,-2,0)$ et les ensembles $F = \{\alpha u,\ \alpha \in \mathbb{R}\}$, $G = \{\alpha u + \beta v,\ (\alpha,\beta) \in \mathbb{R}^2\}$ et $H = \{\alpha u + \beta w,\ (\alpha,\beta) \in \mathbb{R}^2\}$.
   - (a) $F$, $G$ et $H$ sont-ils des $\mathbb{R}$-espaces vectoriels ?
   - (b) Écrire $F$, $G$ et $H$ sous forme de Vect. Dire géométriquement ce qu'ils représentent.
   - (c) Comparer (au sens de l'inclusion) $F$ et $G$ d'une part et $F$ et $H$ d'autre part.
3. Dans $\mathbb{R}^2$, dessiner $\mathrm{Vect}((1,1))$, $\mathrm{Vect}((-1,1))$, $\mathrm{Vect}((1,2),(3,4))$, $\mathrm{Vect}((1,1),(2,2))$ et $\mathrm{Vect}((1,1),(-1,1),(3,4))$.
4. Dans $\mathbb{R}^3$, géométriquement que représentent : $\mathrm{Vect}((1,1,1))$ ? $\mathrm{Vect}((1,2,0),(0,3,4))$ ? $\mathrm{Vect}((1,1,0),(2,2,0))$ ?
5. Dans $\mathbb{R}_3[X]$, on note $F = \mathrm{Vect}(1, X + X^2)$. A-t-on $3 \in F$ ? $4 + 3X + 4X^2 \in F$ ? $4 + 3X + 3X^2 \in F$ ? Réécrire $F$ en compréhension.
6. (⋆) Dans $\mathbb{R}^{\mathbb{R}}$, on considère $f : x \mapsto 1$ et $g : x \mapsto x$. Comment se nomme $F = \mathrm{Vect}((f,g))$ ?

## Exercice 3.16
Type : sous-espaces engendrés, inclusion, dimension · ECUE : EV · Niveau : maths-s2-ev/4
Formules : $P \in \mathrm{Vect}(u_1, \dots) \iff P$ combinaison linéaire des $u_i$ ; $F \subset G$ si les générateurs de $F$ sont dans $G$ ; famille génératrice libre = base, $\dim$ = cardinal

Dans $\mathbb{R}^3$, on considère la famille $\mathcal{F} = (u_1 = (1,-1,2),\ u_2 = (-1,4,1),\ u_3 = (0,3,3))$.
1. Montrer que $\mathcal{F}$ est liée. En extraire une sous-famille libre maximale qu'on notera $\mathcal{F}'$.
2. Montrer que $\mathrm{Vect}\,\mathcal{F} = \mathrm{Vect}\,\mathcal{F}'$.
3. Que vaut $\dim(\mathrm{Vect}\,\mathcal{F}')$ ?

## Exercice 3.17
Type : écrire un sous-espace sous forme de Vect (système linéaire) · ECUE : EV · Niveau : maths-s2-ev/4
Formules : résoudre le système par pivot de Gauss ; exprimer les inconnues principales en fonction des inconnues libres ; factoriser chaque paramètre : $\{(x,y,z)\} = \{t\,u,\ t \in \mathbb{R}\} = \mathrm{Vect}(u)$ ; nombre de paramètres libres = dimension

Déterminer une famille génératrice des sous-espaces vectoriels suivants ; en déduire, proprement, la dimension du sous-espace vectoriel.
1. $E = \{(x,y) \in \mathbb{R}^2 \text{ tel que } x - 2y = 0\}$
2. $F = \{(x,y,z) \in \mathbb{R}^3 \text{ tel que } x - y = 0 \text{ et } z = 0\}$
3. $G = \{(x,y,z) \in \mathbb{R}^3 \text{ tel que } x - y = 0\}$
4. $H = \{(x,y,z) \in \mathbb{R}^3 \text{ tel que } x - y + z = 0\}$
5. $I = \{(x,y,z,t) \in \mathbb{R}^4 \text{ tel que } x - z = 0 \text{ et } 3x + 2y + 3z = 0\}$
6. (Travail personnel) $J = \{(x,y,z,t) \in \mathbb{R}^4 \text{ tel que } x + y + t = 0 \text{ et } x + y + z = 0\}$
7. $K = \{P \in \mathbb{R}_2[X],\ P(0) = 0\}$
8. $L = \{P \in \mathbb{R}_2[X],\ P(0) = 0 \text{ et } P'(1) = 0\}$
9. (Travail personnel) $M = \{P \in \mathbb{R}_3[X],\ X^2 \mid P\}$

## Exercice 3.18
Type : familles libres, génératrices, bases · ECUE : EV · Niveau : maths-s2-ev/6
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \forall i, \lambda_i = 0$ ; génératrice : tout vecteur est combinaison linéaire ; base = libre + génératrice ; $\dim \mathbb{R}_n[X] = n + 1$ ; en dimension $n$ : plus de $n$ vecteurs $\Rightarrow$ liée, moins de $n$ $\Rightarrow$ non génératrice, $n$ vecteurs libres $\Rightarrow$ base ; degrés échelonnés $\Rightarrow$ libre

1. Rappeler ce qu'est la base canonique de $\mathbb{R}^2$, de $\mathbb{R}^3$ et de $\mathbb{R}_n[X]$. Quelle est la dimension de ces espaces vectoriels ?
2. Dans $\mathbb{R}^2$, que peut-on dire du cardinal d'une famille génératrice ? d'une famille libre ? d'une famille liée ? Ces résultats se généralisent-ils à un espace vectoriel de dimension $n$ ?

## Exercice 3.19
Type : familles libres, génératrices, bases ; coordonnées · ECUE : EV · Niveau : maths-s2-ev/7
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \lambda_i = 0$ ; en dimension $n$, une famille libre de $n$ vecteurs est une base ; plus de $n$ vecteurs $\Rightarrow$ liée ; coordonnées : résoudre $P = \alpha Q_1 + \beta Q_2 + \gamma Q_3$ en identifiant les coefficients

1. Justifier que $\mathcal{B} = (\varepsilon_1 = (2,1),\ \varepsilon_2 = (-1,1))$ est une base de $\mathbb{R}^2$.
2. Soit $u = (5,1)$. Trouver graphiquement les coordonnées de $u$ dans la base $\mathcal{B}$. Vous ferez apparaître vos traits de construction.
3. Vérifiez ensuite votre résultat par le calcul.

## Exercice 3.20
Type : familles libres, génératrices, bases ; coordonnées · ECUE : EV · Niveau : maths-s2-ev/7
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \lambda_i = 0$ ; en dimension $n$, une famille libre de $n$ vecteurs est une base ; plus de $n$ vecteurs $\Rightarrow$ liée ; coordonnées : résoudre $P = \alpha Q_1 + \beta Q_2 + \gamma Q_3$ en identifiant les coefficients

1. Dans $E = \mathbb{R}^3$, la famille $\mathcal{F} = (u_1 = (1,1,-1),\ u_2 = (-1,1,1),\ u_3 = (1,-1,1))$ est-elle une base de $E$ ? Si oui, trouver les coordonnées du vecteur $u = (1,2,3)$ dans cette base.
2. Dans $E = \mathbb{R}_2[X]$, montrer que $\mathcal{F} = (P_1 = 1,\ P_2 = X + 1,\ P_3 = (X+1)^2)$ est une base. Quelles sont les coordonnées de $P = X + 2$ dans cette base ?

## Exercice 3.21
Type : familles libres, génératrices, bases · ECUE : EV · Niveau : maths-s2-ev/6
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \forall i, \lambda_i = 0$ ; génératrice : tout vecteur est combinaison linéaire ; base = libre + génératrice ; $\dim \mathbb{R}_n[X] = n + 1$ ; en dimension $n$ : plus de $n$ vecteurs $\Rightarrow$ liée, moins de $n$ $\Rightarrow$ non génératrice, $n$ vecteurs libres $\Rightarrow$ base ; degrés échelonnés $\Rightarrow$ libre

Soit $E$ un $\mathbb{R}$-espace vectoriel de dimension finie égale à 4. Soit $\mathcal{F}$ une famille de vecteurs de $E$. Dans les phrases suivantes, entourer toutes les réponses plausibles parmi les mots « libre », « génératrice » et « liée ».
- a. Si $\mathrm{Card}(\mathcal{F}) = 3$ alors $\mathcal{F}$ peut être : libre / génératrice / liée.
- b. Si $\mathrm{Card}(\mathcal{F}) = 5$ alors $\mathcal{F}$ peut être : libre / génératrice / liée.
- c. Si $\mathrm{Card}(\mathcal{F}) = 6$ alors $\mathcal{F}$ est forcément : libre / génératrice / liée.
- d. Si $\mathrm{Card}(\mathcal{F}) = 4$ alors $\mathcal{F}$ peut être : libre / génératrice / liée.

## Exercice 3.22
Type : sous-espaces, intersection, somme directe · ECUE : EV · Niveau : maths-s2-ev/9
Formules : $\mathrm{Vect}(u)$ : droite si $u \neq 0$ ; plan $ax + by + cz = 0$ : exprimer $z$, $G = \mathrm{Vect}(u, v)$ ; $u \in F \cap G$ : paramétrer par $F$ puis injecter l'équation de $G$ ; Grassmann $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $\dim F + \dim G = \dim E$

Dans les exemples suivants, $E$ est un $\mathbb{R}$-ev, $F$ et $G$ deux sous-espaces vectoriels de $E$. $F$ et $G$ sont-ils supplémentaires ?
1. $E = \mathbb{R}^3$, $F = \{(x,y,z) \in \mathbb{R}^3,\ x - y + z = 0\}$, $G = \{(x,y,z) \in \mathbb{R}^3,\ x = y = z\}$
2. $E = \mathbb{R}^3$, $F = \{(x,y,z) \in \mathbb{R}^3,\ x - y + z = 0\}$, $G = \{(x,y,z) \in \mathbb{R}^3,\ z = 0\}$
3. $E = \mathbb{R}^3$, $F = \{(x,y,z) \in \mathbb{R}^3,\ x - y = z = 0\}$, $G = \{(x,y,z) \in \mathbb{R}^3,\ x - z = y = 0\}$

## Exercice 3.23 (⋆)
Type : sous-espaces, intersection, somme directe · ECUE : EV · Niveau : maths-s2-ev/9
Formules : $\mathrm{Vect}(u)$ : droite si $u \neq 0$ ; plan $ax + by + cz = 0$ : exprimer $z$, $G = \mathrm{Vect}(u, v)$ ; $u \in F \cap G$ : paramétrer par $F$ puis injecter l'équation de $G$ ; Grassmann $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $\dim F + \dim G = \dim E$

Soient $F = \{(x,y,z) \in \mathbb{R}^3,\ y = x + z\}$ et $G = \{(x,y,z) \in \mathbb{R}^3,\ z = 0\}$ deux sev de $\mathbb{R}^3$.
1. Montrer que $F + G = \mathbb{R}^3$, mais que $F$ et $G$ ne sont pas supplémentaires.
2. Trouver $F'$ tel que $F' \subset F$ et $F' \oplus G = \mathbb{R}^3$.
