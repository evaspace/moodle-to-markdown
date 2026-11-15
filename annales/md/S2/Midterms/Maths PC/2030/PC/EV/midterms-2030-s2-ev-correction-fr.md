# Examen S2-B3 EV — mars 2026 (corrigé, FR)

- Source : `raw/S2/Midterms/Maths PC/2030/PC/EV/midterms-2030-s2-ev-correction-fr.pdf` (4 pages)
- Date réelle : mars 2026 (S2, bloc 3, espaces vectoriels, dossier promo 2030). Pas de sujet séparé.
- Corrigé officiel : énoncé rappelé, solution en citation.

## Exercice 1 : espace vectoriel ?
Type : axiomes d'un espace vectoriel (loi externe non standard) · ECUE : EV · Niveau : maths-s2-ev/2
Formules : $\mathbb{R}$-ev : $(E,+)$ groupe commutatif ; $1.u = u$ ; $\alpha.(\beta.u) = (\alpha\beta).u$ ; $(\alpha + \beta).u = \alpha.u + \beta.u$ ; $\alpha.(u + v) = \alpha.u + \alpha.v$ ; un seul axiome en défaut (contre-exemple chiffré) suffit pour conclure que ce n'est pas un ev

On munit l'ensemble $\mathbb{R}^2$ de l'opération interne $+$ et de l'opération externe $*$ suivantes : pour tout $u = (x,y) \in \mathbb{R}^2$, $v = (x',y') \in \mathbb{R}^2$ et $\alpha \in \mathbb{R}$, $u + v = (x + x', y + y')$, $\alpha * u = (\alpha x, \alpha^{-1}y)$ si $\alpha \neq 0$ et $0 * u = (0,0)$.

1. Soient $u = (x,y) \in \mathbb{R}^2$ et $\alpha \in \mathbb{R}$ non nul. Montrer que $\alpha * u = 0_{\mathbb{R}^2} \iff u = 0_{\mathbb{R}^2}$.
> Si $\alpha * u = 0_{\mathbb{R}^2}$ : $\alpha x = 0$ et $\alpha^{-1}y = 0$ avec $\alpha \neq 0$, $\alpha^{-1} \neq 0$, donc $x = y = 0$. Réciproquement, si $u = 0_{\mathbb{R}^2}$ : $\alpha * u = (\alpha \times 0, \alpha^{-1} \times 0) = (0,0)$.

2. Soient $u = (-1, 30)$ et $v = (2, -7)$. Calculer : (a) $u + v$ ; (b) $1 * u$ ; (c) $2 * u$ ; (d) $3 * u$ ; (e) $5 * u$.
> (a) $(1, 23)$ ; (b) $(-1, 30)$ ; (c) $(-2, 15)$ ; (d) $(-3, 10)$ ; (e) $(-5, 6)$.

3. Muni de ces deux opérations, $\mathbb{R}^2$ est-il un $\mathbb{R}$-espace vectoriel ? Justifier.
> Non. Pour $u = (-1, 30)$ : $2 * u + 3 * u = (-5, 25) \neq (-5, 6) = 5 * u = (2 + 3) * u$. La distributivité $(\alpha + \beta).u = \alpha.u + \beta.u$ n'est pas vérifiée.

## Exercice 2 : sous-espaces vectoriels
Type : reconnaître un sous-espace vectoriel · ECUE : EV · Niveau : maths-s2-ev/3
Formules : sev : contient 0, stable par addition et multiplication par un scalaire ; contre-exemple $\lambda u \notin E$ ; équation non linéaire ($z^2$) $\Rightarrow$ en général pas un sev ; $\mathrm{Vect}(\dots)$ est toujours un sev

1. Soient $E$ un $\mathbb{R}$-espace vectoriel et $F$ un ensemble. Donner TOUTES les conditions mathématiques pour avoir : « $F$ est un sous-espace vectoriel de $E$ ».
> $F \subset E$ ; $0_E \in F$ ; $\forall (u,v) \in F^2$, $\forall \alpha \in \mathbb{R}$, $\alpha u + v \in F$.

2. Dire si les ensembles suivants sont des $\mathbb{R}$-espaces vectoriels. Justifiez rigoureusement votre réponse.
   - (a) $F = \{(x,y,z) \in \mathbb{R}^3,\ x - y = 0 \text{ et } x - z^2 = 0\}$.
   - (b) $G = \{P \in \mathbb{R}[X],\ P(1) + P'(1) = 0\}$.
> (a) $u = (4,4,2) \in F$ et $v = (4,4,-2) \in F$, mais $u + v = (8,8,0) \notin F$ car $8 \neq 0^2$. $F$ n'est pas un $\mathbb{R}$-ev.
> (b) $G \subset \mathbb{R}[X]$ et le polynôme nul est dans $G$. Si $(P,Q) \in G^2$ et $\alpha \in \mathbb{R}$ : $(\alpha P + Q)'(1) + (\alpha P + Q)(1) = \alpha(P'(1) + P(1)) + (Q'(1) + Q(1)) = 0$, donc $\alpha P + Q \in G$. $G$ est un sev de $\mathbb{R}[X]$, donc un $\mathbb{R}$-ev.

## Exercice 3 : cours sur les sev
Type : sous-espaces, intersection, somme directe · ECUE : EV · Niveau : maths-s2-ev/9
Formules : $\mathrm{Vect}(u)$ : droite si $u \neq 0$ ; plan $ax + by + cz = 0$ : exprimer $z$, $G = \mathrm{Vect}(u, v)$ ; $u \in F \cap G$ : paramétrer par $F$ puis injecter l'équation de $G$ ; Grassmann $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $\dim F + \dim G = \dim E$

Soient $E$ un $\mathbb{R}$-espace vectoriel et $F$ et $G$ deux sous-espaces vectoriels de $E$.

1. Vrai ou faux : $F + G$ est un sous-espace vectoriel de $E$ ; $F \cup G$ est un sous-espace vectoriel de $E$ ; $F \cap G$ est un sous-espace vectoriel de $E$.
> $F + G$ : vrai. $F \cup G$ : faux. $F \cap G$ : vrai.

2. Justifier votre réponse pour $F \cap G$ (preuve si « vrai », contre-exemple sinon).
> $F \cap G \subset E$. $0_E \in F$ et $0_E \in G$ donc $0_E \in F \cap G$. Si $(u,v) \in (F \cap G)^2$ et $\alpha \in \mathbb{R}$ : $\alpha u + v \in F$ ($F$ sev) et $\alpha u + v \in G$ ($G$ sev), donc $\alpha u + v \in F \cap G$.

3. Donner la définition mathématique de $F + G$. Sur un quadrillage sont représentés deux sous-espaces vectoriels $F$ et $G$ de $\mathbb{R}^2$ (deux droites vectorielles ; d'après le corrigé, $F$ est dirigée par $(1,1)$ et $G$ par $(1,-2)$). Dessiner le vecteur $u = (3,-3)$ et trouver graphiquement la décomposition de $u$ dans $F + G$, en faisant apparaître les traits de construction.
> $F + G = \{u \in E,\ \exists (v,w) \in F \times G,\ u = v + w\}$. Graphiquement (parallèles à $F$ et à $G$ passant par l'extrémité de $u$) : $u = v + w$ avec $v = (1,1) \in F$ et $w = (2,-4) \in G$ ; vérification : $(1,1) + (2,-4) = (3,-3)$.

## Exercice 4 : somme de sous-espaces vectoriels
Type : sous-espaces, intersection, somme directe · ECUE : EV · Niveau : maths-s2-ev/9
Formules : $\mathrm{Vect}(u)$ : droite si $u \neq 0$ ; plan $ax + by + cz = 0$ : exprimer $z$, $G = \mathrm{Vect}(u, v)$ ; $u \in F \cap G$ : paramétrer par $F$ puis injecter l'équation de $G$ ; Grassmann $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $\dim F + \dim G = \dim E$

Dans $E = \mathbb{R}^3$, on considère les deux sev $F = \{(x,y,z) \in \mathbb{R}^3,\ x + y - z = 0\}$ et $G = \{(x,y,z) \in \mathbb{R}^3,\ x + z = 0\}$.

1. Géométriquement, que représentent $F$ et $G$ ?
> Deux plans de $\mathbb{R}^3$.

2. Soit $u = (x,y,z) \in E$.
   - (a) Soient $v = (0, x+z, x+z)$ et $w = (x, -x+y-z, -x)$. Montrer que $v \in F$ et $w \in G$.
   - (b) A-t-on $E = F + G$ ? Justifier.
> (a) $0 + (x+z) - (x+z) = 0$ donc $v \in F$. $x + (-x) = 0$ donc $w \in G$.
> (b) $v + w = (x, y, z) = u$ : tout $u \in E$ est dans $F + G$, donc $E \subset F + G$. Or $F + G \subset E$. Donc $E = F + G$.

3. Donner la définition mathématique de $E = F \oplus G$.
> $E = F \oplus G \iff F \cap G = \{0_E\}$ et $E = F + G$.

4. A-t-on ici $E = F \oplus G$ ? Justifier.
> $X = (-1, 2, 1)$ est dans $F$ ($-1 + 2 - 1 = 0$) et dans $G$ ($-1 + 1 = 0$). Donc $F \cap G \neq \{0_E\}$ et $E \neq F \oplus G$.

## Exercice 5 : cours 2 sur les familles
Type : familles libres, génératrices, bases · ECUE : EV · Niveau : maths-s2-ev/6
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \forall i, \lambda_i = 0$ ; génératrice : tout vecteur est combinaison linéaire ; base = libre + génératrice ; $\dim \mathbb{R}_n[X] = n + 1$ ; en dimension $n$ : plus de $n$ vecteurs $\Rightarrow$ liée, moins de $n$ $\Rightarrow$ non génératrice, $n$ vecteurs libres $\Rightarrow$ base ; degrés échelonnés $\Rightarrow$ libre

1. Soient $E$ un espace vectoriel sur $\mathbb{R}$ et $\mathcal{F} = (u_1, \dots, u_n)$ une famille de $E$ ($n \in \mathbb{N}^*$).
   - (a) Donner la définition mathématique (avec les quantificateurs) de « $\mathcal{F}$ est une famille libre de $E$ ».
   - (b) Donner la définition mathématique (avec les quantificateurs) de « $\mathcal{F}$ est une famille liée de $E$ ».
   - (c) Donner la définition mathématique (avec les quantificateurs) de « $\mathcal{F}$ est une famille génératrice de $E$ ».
   - (d) Écrire $\mathrm{Vect}(\mathcal{F})$ sous la forme d'un ensemble.
> (a) $\forall (\alpha_1, \dots, \alpha_n) \in \mathbb{R}^n$, $(\alpha_1u_1 + \dots + \alpha_nu_n = 0_E \Rightarrow \alpha_1 = \dots = \alpha_n = 0)$.
> (b) $\exists (\alpha_1, \dots, \alpha_n) \in \mathbb{R}^n$ non tous nuls, $\alpha_1u_1 + \dots + \alpha_nu_n = 0_E$.
> (c) $\forall u \in E$, $\exists (\alpha_1, \dots, \alpha_n) \in \mathbb{R}^n$, $u = \alpha_1u_1 + \dots + \alpha_nu_n$.
> (d) $\mathrm{Vect}(\mathcal{F}) = \{\alpha_1u_1 + \dots + \alpha_nu_n,\ (\alpha_1, \dots, \alpha_n) \in \mathbb{R}^n\}$.

2. Dans $E = \mathbb{R}[X]$, la famille $\mathcal{F} = (0_{\mathbb{R}[X]},\ X - 1,\ X^2 + 3)$ est-elle libre ou liée ? Justifier.
> $46 \cdot 0_{\mathbb{R}[X]} + 0 \cdot (X - 1) + 0 \cdot (X^2 + 3) = 0_{\mathbb{R}[X]}$ avec $(46, 0, 0)$ non tous nuls : la famille est liée (toute famille contenant le vecteur nul est liée).
