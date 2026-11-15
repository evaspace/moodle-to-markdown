# Examen S2-B3 EV — mars 2024 (sujet, FR)

- Source : `raw/S2/Midterms/Maths PC/2028/PC/EV/midterm-2028-s2-maths-subject-fr.pdf` (5 pages)
- Date réelle : mars 2024 (S2, bloc 3, espaces vectoriels, dossier promo 2028). Corrigé : `midterm-2028-s2-maths-correction-fr.md` (même dossier). Durée : 1 heure. Documents et calculatrices interdits. Barème sur 20 points.

## Exercice 1 : sous-espaces vectoriels (10 points)
Type : reconnaître un sous-espace vectoriel · ECUE : EV · Niveau : maths-s2-ev/3
Formules : sev : contient 0, stable par addition et multiplication par un scalaire ; contre-exemple $\lambda u \notin E$ ; équation non linéaire ($z^2$) $\Rightarrow$ en général pas un sev ; $\mathrm{Vect}(\dots)$ est toujours un sev

1. Soient $E$ un $\mathbb{R}$-espace vectoriel et $F$ un ensemble. Donner les conditions mathématiques pour avoir : « $F$ est un sous-espace vectoriel de $E$ ».

2. Dire si les ensembles suivants sont des $\mathbb{R}$-espaces vectoriels. Justifiez rigoureusement votre réponse.
   - (a) $F = \{P \in \mathbb{R}[X],\ P'(1) = 1\}$.
   - (b) $G = \{(x,y,z) \in \mathbb{R}^3,\ 2x = z\}$.
   - (c) $H = \{f \in \mathbb{R}^{\mathbb{R}},\ \exists (a,b) \in \mathbb{R}^2,\ \forall x \in \mathbb{R},\ f(x) = ax + b\}$ (ensemble des fonctions affines).

3. Donner sans justifier :
   - (a) un sous-espace vectoriel de $E = \mathbb{R}[X]$ autre que $E$ et $\{0_E\}$ ;
   - (b) un sous-ensemble de $E = \mathbb{R}^2$ (autre qu'un singleton) qui ne soit pas un sous-espace vectoriel de $E$.

## Exercice 2 : somme de sev (5 points)
Type : sous-espaces, intersection, somme directe · ECUE : EV · Niveau : maths-s2-ev/9
Formules : $\mathrm{Vect}(u)$ : droite si $u \neq 0$ ; plan $ax + by + cz = 0$ : exprimer $z$, $G = \mathrm{Vect}(u, v)$ ; $u \in F \cap G$ : paramétrer par $F$ puis injecter l'équation de $G$ ; Grassmann $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $\dim F + \dim G = \dim E$

Dans $E = \mathbb{R}^3$, on considère les deux sous-espaces vectoriels $F = \{(x,y,z) \in \mathbb{R}^3,\ x = 0\}$ et $G = \{(x,y,z) \in \mathbb{R}^3,\ z = 0\}$.

1. Géométriquement, que représentent $F$ et $G$ ?

2. Soit $u = (x,y,z) \in \mathbb{R}^3$. Le vecteur $u$ appartient-il à $F + G$ ? Justifier.

3. A-t-on $E = F + G$ ? Justifier.

4. A-t-on $E = F \oplus G$ ? Justifier. Vous rappellerez avant la caractérisation mathématique avec les quantificateurs de $E = F \oplus G$.

5. $F \cup G$ est-il un sous-espace vectoriel de $\mathbb{R}^3$ ? Justifier.

## Exercice 3 : les familles (5 points)
Type : familles libres, génératrices, bases · ECUE : EV · Niveau : maths-s2-ev/6
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \forall i, \lambda_i = 0$ ; génératrice : tout vecteur est combinaison linéaire ; base = libre + génératrice ; $\dim \mathbb{R}_n[X] = n + 1$ ; en dimension $n$ : plus de $n$ vecteurs $\Rightarrow$ liée, moins de $n$ $\Rightarrow$ non génératrice, $n$ vecteurs libres $\Rightarrow$ base ; degrés échelonnés $\Rightarrow$ libre

Dans $\mathbb{R}^3$, on considère la famille de vecteurs $\mathcal{F} = (u,v,w)$.

1. Donner la définition mathématique (avec les quantificateurs) de « $\mathcal{F}$ est une famille libre de $\mathbb{R}^3$ ».

2. Donner la définition mathématique (avec les quantificateurs) de « $\mathcal{F}$ est une famille liée de $\mathbb{R}^3$ ».

3. Donner la définition mathématique (avec les quantificateurs) de « $\mathcal{F}$ est une famille génératrice de $\mathbb{R}^3$ ».

4. Donner, sans justifier, un exemple d'une famille libre de $\mathbb{R}^3$ composée de 3 vecteurs.

5. Donner, sans justifier, un exemple d'une famille liée de $\mathbb{R}^3$ composée de 3 vecteurs.
