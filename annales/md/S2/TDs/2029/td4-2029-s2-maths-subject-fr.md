# Contrôle de cours EV et ALM (S2 B4) — lundi 7 avril 2025 (sujet, FR)

- Source : `raw/S2/TDs/2029/td4-2029-s2-maths-subject-fr.pdf` (4 pages)
- Date réelle : 7 avril 2025 (dossier promo 2029). Pas de corrigé dans les annales. Corrigé rédigé : `td4-2029-s2-maths-correction-fr.md` (même dossier).
- Durée : 1 heure. Deux parties distinctes (ECUE EV et ALM), 30 minutes chacune, chacune sur 20 points (deux notes).

## EV — Cours 1 : familles de vecteurs (12 points)
Type : familles libres, génératrices, bases ; coordonnées · ECUE : EV · Niveau : maths-s2-ev/7
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \lambda_i = 0$ ; en dimension $n$, une famille libre de $n$ vecteurs est une base ; plus de $n$ vecteurs $\Rightarrow$ liée ; coordonnées : résoudre $P = \alpha Q_1 + \beta Q_2 + \gamma Q_3$ en identifiant les coefficients

1. Soient $E$ un espace vectoriel sur $\mathbb{R}$ et $\mathcal{F} = (u_1, \dots, u_n)$ une famille de $n$ vecteurs de $E$ ($n \in \mathbb{N}^*$).
   - (a) Donner la définition mathématique, avec les quantificateurs, de : « $\mathcal{F}$ est une famille libre de $E$ ».
   - (b) Donner la caractérisation mathématique, avec les quantificateurs, de : « $\mathcal{F}$ est une base de $E$ ».
   - (c) Donner un exemple d'une famille libre de $E = \mathbb{R}^3$ qui ne soit pas une base. Ne pas justifier.
   - (d) Donner un exemple d'une base de $E = \mathbb{R}^2$ autre que la base canonique. Ne pas justifier.
2. Soit $E$ un $\mathbb{R}$-espace vectoriel de dimension finie égale à 4. Soit $\mathcal{F}$ une famille de vecteurs de $E$. Dans les phrases suivantes, entourer toutes les réponses plausibles parmi les mots « libre », « génératrice » et « liée ».
   - a. Si $\mathrm{Card}(\mathcal{F}) = 3$ alors $\mathcal{F}$ peut être : libre / génératrice / liée.
   - b. Si $\mathrm{Card}(\mathcal{F}) = 5$ alors $\mathcal{F}$ peut être : libre / génératrice / liée.
   - c. Si $\mathrm{Card}(\mathcal{F}) = 6$ alors $\mathcal{F}$ est forcément : libre / génératrice / liée.
   - d. Si $\mathrm{Card}(\mathcal{F}) = 4$ alors $\mathcal{F}$ peut être : libre / génératrice / liée.
3. On se place dans $E = \mathbb{R}_2[X]$. On admet que la famille $\mathcal{B} = (P_1 = 1,\ P_2 = X + 1,\ P_3 = X^2 - X)$ est une famille libre de $E$.
   - (a) Justifier que $\mathcal{B}$ est une base de $E$.
   - (b) Donner $Q \in E$ dont les coordonnées dans la base $\mathcal{B}$ sont 1, 2 et 3 (en respectant l'ordre des vecteurs de $\mathcal{B}$).
   - (c) Rappeler ce qu'est $\mathcal{B}_c$, la base canonique de $E$. Donner les coordonnées de $P_3$ d'une part dans la base $\mathcal{B}$, d'autre part dans la base $\mathcal{B}_c$.

## EV — Cours 2 : autour du Vect (8 points)
Type : sous-espaces engendrés, inclusion, dimension · ECUE : EV · Niveau : maths-s2-ev/4
Formules : $P \in \mathrm{Vect}(u_1, \dots) \iff P$ combinaison linéaire des $u_i$ ; $F \subset G$ si les générateurs de $F$ sont dans $G$ ; famille génératrice libre = base, $\dim$ = cardinal

Les questions sont indépendantes.
1. Dans $\mathbb{R}^2$, on considère $F = \mathrm{Vect}((1,2))$. Écrire cet ensemble avec une autre notation ensembliste et le dessiner dans le plan.
2. Dans $\mathbb{R}^3$, on considère deux vecteurs non nuls $u_1$ et $u_2$. Soit $F = \{\alpha u_1 + \beta u_2,\ (\alpha,\beta) \in \mathbb{R}^2\}$. Comment peut-on réécrire $F$ ? Que représente-t-il géométriquement dans $\mathbb{R}^3$ ? Soyez précis.
3. On se place dans $\mathbb{R}_2[X]$. Soit $F = \mathrm{Vect}(P_1 = 1,\ P_2 = X^2 - X,\ P_3 = X^2 - X - 1)$. Dire si $Q = 2X^2 - 2X - 5$ et $R = X^2$ sont des éléments de $F$. Justifier.

## ALM — Cours 1 : définitions et propriétés (12 points)
Type : noyau, image, injectivité, surjectivité (cours) · ECUE : ALM · Niveau : maths-s2-alm/2
Formules : sous-espace : contient 0 et stable par $\alpha u + v$ ; $f(\alpha u + v) = \alpha f(u) + f(v)$ ; injective $\iff \mathrm{Ker} f = \{0\}$ ; surjective $\iff \mathrm{Im} f = F$

Soient $E$ et $F$ deux $\mathbb{R}$-espaces vectoriels et $f : E \to F$.
1. Donner la définition mathématique de : $f$ est linéaire de $E$ vers $F$.
2. Donner la définition mathématique du noyau de $f$ dans le contexte précis où $E = \mathbb{R}_2[X]$ et $F = \mathbb{R}^2$.
3. Donner la définition mathématique de l'image de $f$ dans le contexte précis où $E = \mathbb{R}_2[X]$ et $F = \mathbb{R}^2$.
4. Soit $f \in \mathcal{L}(E,F)$ ($E$ et $F$ quelconques).
   - (a) Compléter la phrase suivante : $\mathrm{Ker}(f)$ est un sous-espace vectoriel de $\dots$ et $\mathrm{Im}(f)$ est un sous-espace vectoriel de $\dots$
   - (b) Rappeler la définition mathématique (celle du séminaire, avec les quantificateurs) de « $f$ surjective de $E$ vers $F$ » et donner proprement une condition nécessaire et suffisante reliant le noyau et/ou l'image de $f$ à cette notion.
   - (c) Rappeler la définition mathématique (celle du séminaire, avec les quantificateurs) de « $f$ injective de $E$ vers $F$ », donner et démontrer proprement une condition nécessaire et suffisante reliant le noyau et/ou l'image de $f$ à cette notion.

## ALM — Cours 2 : exemples (8 points)
Type : noyau, image, rang d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/3
Formules : linéaire : $f(\lambda u + v) = \lambda f(u) + f(v)$ ; $\mathrm{Ker} f$ : résoudre $f(x) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \mathrm{rg} f$ ; $\mathrm{rg} f = \dim F \Rightarrow \mathrm{Im} f = F$ (surjective) ; $\mathrm{Im} f = \mathrm{Vect}(f(e_1), \dots, f(e_n))$

Les questions sont indépendantes.
1. Proposer une application non linéaire de $\mathbb{R}^3$ vers $\mathbb{R}^2$. Ne pas justifier.
2. Trouver rigoureusement une base du noyau de l'application linéaire $f : \mathbb{R}^3 \to \mathbb{R}^3$, $(x,y,z) \mapsto (x - z,\ 0,\ x - z)$.
3. Proposer une application linéaire $g$ de $\mathbb{R}^2$ vers $\mathbb{R}^2$ telle que $\mathrm{Im}(g) = \mathrm{Vect}((1,2))$. Justification non demandée.
