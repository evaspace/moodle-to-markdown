# Contrôle de cours 2 (S2) — lundi 3 avril 2023 (sujet, FR)

- Source : `raw/S2/TDs/2027/td4-2027-s2-maths-subject-fr.pdf` (3 pages)
- Date réelle : 3 avril 2023 (dossier promo 2027). Pas de corrigé dans les annales.
- Durée : 1 heure. Barème sur 20. Quatre questions de cours.

## Cours 1 : familles de vecteurs (6 points)
Type : familles libres, génératrices, bases · ECUE : EV · Niveau : maths-s2-ev/6
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \forall i, \lambda_i = 0$ ; génératrice : tout vecteur est combinaison linéaire ; base = libre + génératrice ; $\dim \mathbb{R}_n[X] = n + 1$ ; en dimension $n$ : plus de $n$ vecteurs $\Rightarrow$ liée, moins de $n$ $\Rightarrow$ non génératrice, $n$ vecteurs libres $\Rightarrow$ base ; degrés échelonnés $\Rightarrow$ libre

Soient $E$ un espace vectoriel sur $\mathbb{R}$ et $\mathcal{F} = (e_1, \dots, e_n)$ une famille de $n$ vecteurs de $E$ ($n \in \mathbb{N}^*$).
1. - (a) Donner la définition mathématique de : $\mathcal{F}$ est une famille libre de $E$.
   - (b) Donner la définition mathématique de : $\mathcal{F}$ est une famille liée de $E$.
   - (c) Dans cette question uniquement, $E = \mathbb{R}_2[X]$. Parmi les vecteurs $P_1 = 2$, $P_2 = X + 1$, $P_3 = X$, $P_4 = X^2 + X$ et $P_5 = X^2 + 2X + 2$, donner sans justifier d'une part une famille libre de $E$ composée de 3 vecteurs et d'autre part une famille liée de $E$ composée de 3 vecteurs.
2. On suppose que $\mathcal{F}$ est une famille génératrice de $E$.
   - (a) Que cela signifie-t-il ? Vous devez répondre en utilisant des quantificateurs.
   - (b) Dans cette question uniquement, $E = \mathbb{R}^2$. Proposer sans justifier une famille génératrice de $E$ parmi les vecteurs $u_1 = (1,-2)$, $u_2 = (-2,4)$, $u_3 = (-1,1)$ et $u_4 = (-1,-2)$.
3. On suppose que $e_1$ est une combinaison linéaire de $e_2$, $e_3$ et $e_4$. Montrer rigoureusement que $\mathrm{Vect}((e_1,e_2,e_3,e_4)) = \mathrm{Vect}((e_2,e_3,e_4))$.

## Cours 2 : bases (3 points)
Type : familles libres, génératrices, bases ; coordonnées · ECUE : EV · Niveau : maths-s2-ev/7
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \lambda_i = 0$ ; en dimension $n$, une famille libre de $n$ vecteurs est une base ; plus de $n$ vecteurs $\Rightarrow$ liée ; coordonnées : résoudre $P = \alpha Q_1 + \beta Q_2 + \gamma Q_3$ en identifiant les coefficients

Les deux questions sont indépendantes.
1. Dans $\mathbb{R}^3$, on considère la base $\mathcal{B} = (e_1 = (1,0,1),\ e_2 = (0,1,1),\ e_3 = (1,1,0))$. Rappeler à l'aide de quantificateurs ce que signifie « $\mathcal{B}$ base de $\mathbb{R}^3$ ». Soit $u = (x,y,z) \in \mathbb{R}^3$ de coordonnées 1, 2 et 3 dans la base $\mathcal{B}$ (en respectant l'ordre des vecteurs de $\mathcal{B}$). Trouver $x$, $y$ et $z$.
2. Dans $\mathbb{R}^3$, on considère $F = \mathrm{Vect}(((1,2,0), (3,-2,1), (4,0,1)))$. Trouver la dimension de $F$. Justifier soigneusement.

## Cours 3 : exemples d'applications linéaires (3 points)
Type : application linéaire (caractérisation) · ECUE : ALM · Niveau : maths-s2-alm/1
Formules : $f$ linéaire $\Rightarrow f(0) = 0$ et $f(2x) = 2f(x)$ (conditions nécessaires) ; réciproquement vérifier $f(\lambda x + y) = \lambda f(x) + f(y)$ ; les applications linéaires de $\mathbb{R}$ dans $\mathbb{R}$ sont $x \mapsto bx$

Donner, sans justifier, un exemple : 1) d'un endomorphisme non nul de $\mathbb{R}^3$ ; 2) d'une application non linéaire de $\mathbb{R}^3$ vers $\mathbb{R}^2$ ; 3) d'une application linéaire non nulle de $\mathbb{R}^3$ vers $\mathbb{R}[X]$.

## Cours 4 : noyau et image (8 points)
Type : noyau, image, injectivité, surjectivité (cours) · ECUE : ALM · Niveau : maths-s2-alm/2
Formules : sous-espace : contient 0 et stable par $\alpha u + v$ ; $f(\alpha u + v) = \alpha f(u) + f(v)$ ; injective $\iff \mathrm{Ker} f = \{0\}$ ; surjective $\iff \mathrm{Im} f = F$

Soient $E$ et $F$ deux $\mathbb{R}$-espaces vectoriels et $f \in \mathcal{L}(E,F)$.
1. Donner la définition mathématique de $\mathrm{Ker}(f)$.
2. Donner la définition mathématique de $\mathrm{Im}(f)$.
3. Donner et démontrer une condition nécessaire et suffisante sur $\mathrm{Ker}(f)$ et/ou $\mathrm{Im}(f)$ pour « $f$ injective ».
4. Donner une condition nécessaire et suffisante sur $\mathrm{Ker}(f)$ et/ou $\mathrm{Im}(f)$ pour « $f$ surjective ».
5. Donner sans justifier un exemple d'une application linéaire de $\mathbb{R}^3$ vers $\mathbb{R}^3$ telle que $\mathrm{Ker}(f) = \mathrm{Vect}(((1,0,-2)))$.
