# Examen S2-B3 EV — mars 2025 (sujet, FR)

- Source : `raw/S2/Midterms/Maths PC/2029/PC/EV/midterm-2029-s2-maths-subject-fr.pdf` (6 pages)
- Date réelle : mars 2025 (S2, bloc 3, espaces vectoriels, dossier promo 2029). Pas de corrigé officiel dans les annales. Corrigé rédigé : `midterm-2029-s2-maths-correction-fr.md` (même dossier).
- Durée : 1 heure. Documents et calculatrices interdits. Barème sur 20 points. Dans le sujet, sev signifie sous-espace vectoriel et deg signifie degré.

## Exercice 1 : sous-espaces vectoriels (6 points)
Type : reconnaître un sous-espace vectoriel · ECUE : EV · Niveau : maths-s2-ev/3
Formules : sev : contient 0, stable par addition et multiplication par un scalaire ; contre-exemple $\lambda u \notin E$ ; équation non linéaire ($z^2$) $\Rightarrow$ en général pas un sev ; $\mathrm{Vect}(\dots)$ est toujours un sev

1. Soient $E$ un $\mathbb{R}$-espace vectoriel et $F$ un ensemble. Donner les conditions mathématiques pour avoir : « $F$ est un sous-espace vectoriel de $E$ ».
2. Dire si les ensembles suivants sont des $\mathbb{R}$-espaces vectoriels. Justifiez rigoureusement votre réponse.
   - (a) $F = \{(x,y,z) \in \mathbb{R}^3,\ 2x + y = 0\}$.
   - (b) $G = \{f \in \mathbb{R}^{\mathbb{R}},\ f(0) \times f(1) = 0\}$.

## Exercice 2 : cours 1 sur les sev (3 points)
Type : sous-espaces, intersection, somme directe · ECUE : EV · Niveau : maths-s2-ev/9
Formules : $\mathrm{Vect}(u)$ : droite si $u \neq 0$ ; plan $ax + by + cz = 0$ : exprimer $z$, $G = \mathrm{Vect}(u, v)$ ; $u \in F \cap G$ : paramétrer par $F$ puis injecter l'équation de $G$ ; Grassmann $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $\dim F + \dim G = \dim E$

Soient $E$ un $\mathbb{R}$-espace vectoriel et $F$ et $G$ deux sous-espaces vectoriels de $E$.

1. Compléter par « Vrai » ou « Faux » : $F \cap G$ est un sous-espace vectoriel de $E$ ; $F \cup G$ est un sous-espace vectoriel de $E$ ; $F + G$ est un sous-espace vectoriel de $E$.
2. Justifier votre réponse pour $F \cap G$ (si vous avez répondu « Vrai », faire une preuve, sinon donner un contre-exemple).

## Exercice 3 : somme de sous-espaces vectoriels (7 points)
Type : sous-espaces, intersection, somme directe · ECUE : EV · Niveau : maths-s2-ev/9
Formules : $\mathrm{Vect}(u)$ : droite si $u \neq 0$ ; plan $ax + by + cz = 0$ : exprimer $z$, $G = \mathrm{Vect}(u, v)$ ; $u \in F \cap G$ : paramétrer par $F$ puis injecter l'équation de $G$ ; Grassmann $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $\dim F + \dim G = \dim E$

Dans $E = \mathbb{R}^3$, on considère les deux sev $F = \{(x,y,z) \in \mathbb{R}^3,\ x + y + z = 0\}$ et $G = \{(x,y,z) \in \mathbb{R}^3,\ x - y = 0\}$.

1. Géométriquement, que représentent $F$ et $G$ ?
2. Soit $u = (x,y,z) \in E$.
   - (a) Soient $v = (y, 2y - x, x - 3y)$ et $w = (x - y, -y + x, z + 3y - x)$. Montrer que $v \in F$ et $w \in G$.
   - (b) En déduire que $u \in F + G$.
   - (c) A-t-on $E = F + G$ ? Justifier.
3. Donner la définition de $E = F \oplus G$.
4. A-t-on ici $E = F \oplus G$ ? Justifier.

## Exercice 4 : cours 2 sur les familles (4 points)
Type : familles libres, génératrices, bases · ECUE : EV · Niveau : maths-s2-ev/6
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \forall i, \lambda_i = 0$ ; génératrice : tout vecteur est combinaison linéaire ; base = libre + génératrice ; $\dim \mathbb{R}_n[X] = n + 1$ ; en dimension $n$ : plus de $n$ vecteurs $\Rightarrow$ liée, moins de $n$ $\Rightarrow$ non génératrice, $n$ vecteurs libres $\Rightarrow$ base ; degrés échelonnés $\Rightarrow$ libre

1. Dans $E = \mathbb{R}_2[X] = \{P \in \mathbb{R}[X],\ \deg(P) \leqslant 2\}$, on considère la famille de vecteurs $\mathcal{F} = (P_1, P_2, P_3)$.
   - (a) Donner la définition mathématique (avec les quantificateurs) de « $\mathcal{F}$ est une famille libre de $E$ ».
   - (b) Donner la définition mathématique (avec les quantificateurs) de « $\mathcal{F}$ est une famille liée de $E$ ».
   - (c) Donner la définition mathématique (avec les quantificateurs) de « $\mathcal{F}$ est une famille génératrice de $E$ ».
2. Donner, sans justifier, un exemple d'une famille libre de $\mathbb{R}^3$ composée de 2 vecteurs.
3. Donner, sans justifier, un exemple d'une famille liée de $\mathbb{R}^3$ composée de 3 vecteurs.
