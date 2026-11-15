# Contrôle de mi-semestre (S2) — mars 2021 (sujet, FR)

- Source : `raw/S2/Midterms/Maths PC/2025/midterm-2025-s2-maths-subject-fr.pdf` (10 pages)
- Date réelle : mars 2021 (S2 2020-2021, dossier promo 2025). Corrigé : `midterm-2025-s2-maths-correction-fr.md`.
- Durée : 3 heures. Documents et calculatrices interdits. Barème sur 30 points, ramené à 20.

## Exercice 1 (4 points)
Type : EDO linéaires 1er ordre (variation de la constante, solution particulière trigonométrique) · ECUE : APIS (EDO) · Niveau : maths-s1-apis-edo/5
Formules : $a(t)y' + b(t)y = 0 \Rightarrow y_0 = ke^{-\int \frac ba}$ ; solution générale = homogène + particulière ; variation de la constante : $y_p = k(t)y_0(t)$, les termes en $k$ s'annulent, reste $k'$ ; $\int \frac1{2\sqrt t} = \sqrt t$ ; second membre $\cos + \sin$ : $y_p = a\cos t + b\sin t$, identifier les coefficients de $\cos$ et $\sin$

Résoudre les équations différentielles suivantes :
- a. $(E_1)$ : $(t+3)y' + y = \dfrac1{2\sqrt t}$ sur $\mathbb{R}_+^*$, en cherchant une solution particulière grâce à une variation de la constante.
- b. $(E_2)$ : $y' + y = \cos(t) + 2\sin(t)$ sur $\mathbb{R}$, en cherchant une solution particulière de la forme $y_p = a\cos(t) + b\sin(t)$, $(a,b) \in \mathbb{R}^2$.

## Exercice 2 (3 points)
Type : théorème des valeurs intermédiaires · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/2
Formules : TVI : $f$ continue sur $[a,b]$, $k$ entre $f(a)$ et $f(b)$ $\Rightarrow \exists c \in [a,b]$, $f(c) = k$ ; si $f(a)f(b) < 0$, $\exists c \in ]a,b[$, $f(c) = 0$

- a. Montrer, en rédigeant soigneusement votre réponse, que l'équation $(E)$ : $x^3 - 3x + 6 = 0$ admet une solution sur l'intervalle $]-3, 3[$.
- b. Établir le tableau de variation de $f(x) = x^3 - 3x + 6$ sur $[-3, 3]$. En déduire que cette racine est unique et en donner un encadrement entre deux entiers consécutifs.

## Exercice 3 (6 points)
Type : développements limités usuels et composés · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/8
Formules : $e^u = \sum \frac{u^k}{k!}$ ; $\cos u = 1 - \frac{u^2}2 + \frac{u^4}{24}$ ; $\sin u = u - \frac{u^3}6$ ; $\ln(1+u) = u - \frac{u^2}2 + \frac{u^3}3 - \frac{u^4}4$ ; $\sqrt{1+u} = 1 + \frac u2 - \frac{u^2}8 + \frac{u^3}{16} - \frac{5u^4}{128}$ ; $(1+u)^\alpha = 1 + \alpha u + \frac{\alpha(\alpha-1)}2u^2$ ; produit tronqué ; composition : poser $u$, calculer $u^2$ à l'ordre voulu ; $1 + \cos 2x = 2\cos^2 x$

1. Déterminer le développement limité à l'ordre 2 en zéro de $f(x) = e^x(1+x)^{-\frac12}$.
2. Déterminer le développement limité à l'ordre 4 en zéro de $g(x) = \ln(1 + \cos(x))$.
3. Calculer $\displaystyle\lim_{x \to +\infty} \left(1 + 2\sin\Big(\frac1x\Big)\right)^x$ en détaillant chaque étape de calcul.

## Exercice 4 (4 points)
Type : reconnaître un sous-espace vectoriel · ECUE : EV · Niveau : maths-s2-ev/3
Formules : sev : contient 0, stable par addition et multiplication par un scalaire ; contre-exemple $\lambda u \notin E$ ; équation non linéaire ($z^2$) $\Rightarrow$ en général pas un sev ; $\mathrm{Vect}(\dots)$ est toujours un sev

- a. Soit $E = \mathbb{R}^2$. Les ensembles suivants sont-ils des sous-espaces vectoriels de $E$ ? Justifiez vos réponses par une démonstration en cas de réponse positive, en montrant précisément ce qui ne marche pas sinon.
  - $A$ : le singleton $A = \{0_E\}$.
  - $B$ : demi-plan $y \geqslant 0$ : $B = \{(x,y) \in \mathbb{R}^2,\ y \geqslant 0\}$.
  - $C$ : droite $C = \{(x,y) \in \mathbb{R}^2,\ x - 2y = 0\}$.
  - $D$ : droite $D = \{(x,y) \in \mathbb{R}^2,\ x - 2y = 1\}$.
- b. Citer, sans démonstration, les sous-espaces vectoriels de $\mathbb{R}^2$.

## Exercice 5 (3 points)
Type : sous-espaces, intersection, somme directe · ECUE : EV · Niveau : maths-s2-ev/9
Formules : $\mathrm{Vect}(u)$ : droite si $u \neq 0$ ; plan $ax + by + cz = 0$ : exprimer $z$, $G = \mathrm{Vect}(u, v)$ ; $u \in F \cap G$ : paramétrer par $F$ puis injecter l'équation de $G$ ; Grassmann $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $\dim F + \dim G = \dim E$

On pose $E = \mathbb{R}^3$ et $F = \{(a,b,0) ;\ (a,b) \in \mathbb{R}^2\}$, $G = \{(c,c,c),\ c \in \mathbb{R}\}$, deux sous-espaces vectoriels de $E$. Rappeler à quelles conditions $F$ et $G$ sont supplémentaires dans $E$ puis montrer que $F \oplus G = E$.

## Exercice 6 (3 points)
Type : familles libres, génératrices, bases ; coordonnées · ECUE : EV · Niveau : maths-s2-ev/7
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \lambda_i = 0$ ; en dimension $n$, une famille libre de $n$ vecteurs est une base ; plus de $n$ vecteurs $\Rightarrow$ liée ; coordonnées : résoudre $P = \alpha Q_1 + \beta Q_2 + \gamma Q_3$ en identifiant les coefficients

Soit $\mathcal{F} = \{u = (1,1,0) ;\ v = (0,1,1) ;\ w = (1,0,1)\}$ une famille de vecteurs de $\mathbb{R}^3$.
- a. Montrer que $\mathcal{F}$ est une base de $\mathbb{R}^3$.
- b. Donner les coordonnées du vecteur $(1,3,0)$ dans la base $\mathcal{F}$.

## Exercice 7 (3 points)
Type : sous-espaces engendrés, inclusion, dimension · ECUE : EV · Niveau : maths-s2-ev/4
Formules : $P \in \mathrm{Vect}(u_1, \dots) \iff P$ combinaison linéaire des $u_i$ ; $F \subset G$ si les générateurs de $F$ sont dans $G$ ; famille génératrice libre = base, $\dim$ = cardinal

On considère l'espace vectoriel $E = \mathbb{R}^4$. Soient $F$ et $G$ les deux sous-espaces vectoriels de $E$ définis par $F = \{(x,y,z,t) \in \mathbb{R}^4,\ y - z = 0 \text{ et } x + y - z = 0\}$ et $G = \mathrm{Vect}(\{(1,-1,0,1) ;\ (-2,2,0,-2)\})$.
- a. Écrire $F$ sous forme de Vect.
- b. Déterminer les dimensions de $F$ et $G$ en justifiant soigneusement vos réponses.

## Exercice 8 (4 points)
Type : familles libres, génératrices, bases · ECUE : EV · Niveau : maths-s2-ev/6
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \forall i, \lambda_i = 0$ ; génératrice : tout vecteur est combinaison linéaire ; base = libre + génératrice ; $\dim \mathbb{R}_n[X] = n + 1$ ; en dimension $n$ : plus de $n$ vecteurs $\Rightarrow$ liée, moins de $n$ $\Rightarrow$ non génératrice, $n$ vecteurs libres $\Rightarrow$ base ; degrés échelonnés $\Rightarrow$ libre

Pour chacune des familles de vecteurs suivantes, montrer si la famille est libre ou liée.
- $\mathcal{F}_1 = \{P, Q, R\}$ dans $\mathbb{R}[X]$ où $P(X) = -X^3 + X^2 + 2X - 2$, $Q(X) = 2X^3 - X + 3$, $R(X) = 2X^2 + 3X - 1$.
- $\mathcal{F}_2 = \{(u_n), (v_n), (w_n)\}$ dans $\mathbb{R}^{\mathbb{N}}$ où, pour tout $n \in \mathbb{N}$, $u_n = n$, $v_n = 2^n$ et $w_n = \dfrac n{n+1}$.
