# Examen S2-B3 EV — mars 2024 (corrigé, FR)

- Source : `raw/S2/Midterms/Maths PC/2028/PC/EV/midterm-2028-s2-maths-correction-fr.pdf` (2 pages)
- Date réelle : mars 2024 (S2, bloc 3, espaces vectoriels, dossier promo 2028). Sujet : `midterm-2028-s2-maths-subject-fr.md` (même dossier).
- Corrigé officiel : énoncé rappelé, solution en citation.

## Exercice 1 : sous-espaces vectoriels
Type : reconnaître un sous-espace vectoriel · ECUE : EV · Niveau : maths-s2-ev/3
Formules : sev : contient 0, stable par addition et multiplication par un scalaire ; contre-exemple $\lambda u \notin E$ ; équation non linéaire ($z^2$) $\Rightarrow$ en général pas un sev ; $\mathrm{Vect}(\dots)$ est toujours un sev

1. Soient $E$ un $\mathbb{R}$-espace vectoriel et $F$ un ensemble. Donner les conditions mathématiques pour avoir : « $F$ est un sous-espace vectoriel de $E$ ».
> 1) $F \subset E$ ; 2) $0_E \in F$ ; 3) $\forall (u,v) \in F^2$, $\forall \alpha \in \mathbb{R}$, $\alpha u + v \in F$.

2. Dire si les ensembles suivants sont des $\mathbb{R}$-espaces vectoriels. Justifiez rigoureusement votre réponse.
   - (a) $F = \{P \in \mathbb{R}[X],\ P'(1) = 1\}$.
   - (b) $G = \{(x,y,z) \in \mathbb{R}^3,\ 2x = z\}$.
   - (c) $H = \{f \in \mathbb{R}^{\mathbb{R}},\ \exists (a,b) \in \mathbb{R}^2,\ \forall x \in \mathbb{R},\ f(x) = ax + b\}$ (ensemble des fonctions affines).
> (a) Le polynôme nul n'est pas dans $F$ (sa dérivée en 1 vaut $0 \neq 1$) : $F$ n'est pas un espace vectoriel.
> (b) $G \subset \mathbb{R}^3$ et $0_{\mathbb{R}^3} \in G$ ($2 \times 0 = 0$). Si $u = (x,y,z)$, $v = (x',y',z')$ dans $G$ et $\alpha \in \mathbb{R}$ : $2(\alpha x + x') = \alpha \times 2x + 2x' = \alpha z + z'$, donc $\alpha u + v \in G$. $G$ est un sev de $\mathbb{R}^3$, donc un $\mathbb{R}$-ev.
> (c) $H \subset \mathbb{R}^{\mathbb{R}}$ et la fonction nulle est dans $H$ ($0x + 0$). Si $f(x) = ax + b$, $g(x) = a'x + b'$ et $\alpha \in \mathbb{R}$ : $(\alpha f + g)(x) = (\alpha a + a')x + (\alpha b + b')$, donc $\alpha f + g \in H$. $H$ est un sev de $\mathbb{R}^{\mathbb{R}}$, donc un $\mathbb{R}$-ev.

3. Donner sans justifier :
   - (a) un sous-espace vectoriel de $E = \mathbb{R}[X]$ autre que $E$ et $\{0_E\}$ ;
   - (b) un sous-ensemble de $E = \mathbb{R}^2$ (autre qu'un singleton) qui ne soit pas un sous-espace vectoriel de $E$.
> (a) $\{P \in \mathbb{R}[X],\ P(1) = 0\}$. (b) $\{(x,y) \in \mathbb{R}^2,\ x + y = 1\}$.

## Exercice 2 : somme de sev
Type : sous-espaces, intersection, somme directe · ECUE : EV · Niveau : maths-s2-ev/9
Formules : $\mathrm{Vect}(u)$ : droite si $u \neq 0$ ; plan $ax + by + cz = 0$ : exprimer $z$, $G = \mathrm{Vect}(u, v)$ ; $u \in F \cap G$ : paramétrer par $F$ puis injecter l'équation de $G$ ; Grassmann $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $\dim F + \dim G = \dim E$

Dans $E = \mathbb{R}^3$, on considère les deux sous-espaces vectoriels $F = \{(x,y,z) \in \mathbb{R}^3,\ x = 0\}$ et $G = \{(x,y,z) \in \mathbb{R}^3,\ z = 0\}$.

1. Géométriquement, que représentent $F$ et $G$ ?
> Deux plans (vectoriels).

2. Soit $u = (x,y,z) \in \mathbb{R}^3$. Le vecteur $u$ appartient-il à $F + G$ ? Justifier.
> Oui : $u = (0,y,z) + (x,0,0)$ avec $(0,y,z) \in F$ et $(x,0,0) \in G$.

3. A-t-on $E = F + G$ ? Justifier.
> Tout $u \in \mathbb{R}^3$ est dans $F + G$, donc $\mathbb{R}^3 \subset F + G$. Or $F + G \subset \mathbb{R}^3$. Donc $F + G = \mathbb{R}^3$.

4. A-t-on $E = F \oplus G$ ? Justifier. Vous rappellerez avant la caractérisation mathématique avec les quantificateurs de $E = F \oplus G$.
> $E = F \oplus G \iff \forall u \in E$, $\exists!\,(u_1,u_2) \in F \times G$, $u = u_1 + u_2$. Ici la décomposition n'est pas unique : on a aussi $u = (0,0,z) + (x,y,0)$. Donc $E \neq F \oplus G$.

5. $F \cup G$ est-il un sous-espace vectoriel de $\mathbb{R}^3$ ? Justifier.
> Non : $u = (0,1,1) \in F$, $v = (1,1,0) \in G$, mais $u + v = (1,2,1)$ n'est ni dans $F$ ni dans $G$.

## Exercice 3 : les familles
Type : familles libres, génératrices, bases · ECUE : EV · Niveau : maths-s2-ev/6
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \forall i, \lambda_i = 0$ ; génératrice : tout vecteur est combinaison linéaire ; base = libre + génératrice ; $\dim \mathbb{R}_n[X] = n + 1$ ; en dimension $n$ : plus de $n$ vecteurs $\Rightarrow$ liée, moins de $n$ $\Rightarrow$ non génératrice, $n$ vecteurs libres $\Rightarrow$ base ; degrés échelonnés $\Rightarrow$ libre

Dans $\mathbb{R}^3$, on considère la famille de vecteurs $\mathcal{F} = (u,v,w)$.

1. Donner la définition mathématique (avec les quantificateurs) de « $\mathcal{F}$ est une famille libre de $\mathbb{R}^3$ ».
> $\forall (\alpha,\beta,\gamma) \in \mathbb{R}^3$, $(\alpha u + \beta v + \gamma w = 0_{\mathbb{R}^3} \Rightarrow \alpha = \beta = \gamma = 0)$.

2. Donner la définition mathématique (avec les quantificateurs) de « $\mathcal{F}$ est une famille liée de $\mathbb{R}^3$ ».
> $\exists (\alpha,\beta,\gamma) \in \mathbb{R}^3 \setminus \{(0,0,0)\}$, $\alpha u + \beta v + \gamma w = 0_{\mathbb{R}^3}$.

3. Donner la définition mathématique (avec les quantificateurs) de « $\mathcal{F}$ est une famille génératrice de $\mathbb{R}^3$ ».
> $\forall X \in \mathbb{R}^3$, $\exists (\alpha,\beta,\gamma) \in \mathbb{R}^3$, $X = \alpha u + \beta v + \gamma w$.

4. Donner, sans justifier, un exemple d'une famille libre de $\mathbb{R}^3$ composée de 3 vecteurs.
> $((1,0,0), (0,1,0), (0,0,1))$.

5. Donner, sans justifier, un exemple d'une famille liée de $\mathbb{R}^3$ composée de 3 vecteurs.
> $((1,0,0), (0,1,0), (1,1,0))$.
