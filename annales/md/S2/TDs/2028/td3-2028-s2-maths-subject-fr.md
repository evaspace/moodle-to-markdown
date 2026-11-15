# Contrôle de cours APEF (S2) — lundi 19 février 2024 (sujet, FR)

- Source : `raw/S2/TDs/2028/td3-2028-s2-maths-subject-fr.pdf` (scan, 3 pages)
- Date réelle : 19 février 2024 (dossier promo 2028). Pas de corrigé dans les annales. Corrigé rédigé : `td3-2028-s2-maths-correction-fr.md` (même dossier).
- Durée : 1 heure. Barème sur 20 points.

## Cours 1 : divisibilité et division euclidienne (2,5 points)
Type : degré, division euclidienne de polynômes, racine · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/2
Formules : $\deg(A+B) \leqslant \max(\deg A, \deg B)$ ; $\deg(AB) = \deg A + \deg B$ ; $\exists!\,(Q,R)$, $A = BQ + R$, $\deg R < \deg B$ ; $\alpha$ racine $\iff A(\alpha) = 0 \iff X - \alpha \mid A$

Les questions sont indépendantes.
1. Soient $P$ et $B$ deux polynômes de $\mathbb{R}[X]$ tels que la division euclidienne de $P$ par $B$ se traduit par l'égalité suivante : $P(X) = (X+2)(X^3+1) + 2X^2 - X + 2$. Déterminer $B$ ainsi que le reste de cette division euclidienne dans ce cas. Justifier.
2. Trouver le quotient et le reste de la division euclidienne de $A(X) = -X^4 + 3X - 5$ par $B(X) = X^2 + 1$.

## Cours 2 : autour des racines (5,5 points)
Type : divisibilité de polynômes, multiplicité, factorisation dans $\mathbb{R}[X]$ et $\mathbb{C}[X]$ · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/9
Formules : $P(a) = 0 \iff X - a \mid P$ ; racine d'ordre $\geqslant 2$ $\iff P(a) = P'(a) = 0$ ; ordre exactement $m$ : $P^{(m)}(a) \neq 0$ ; $(X - a)^m \mid P$, $(X - a)^{m+1} \nmid P$ ; $X^2 + 1 = (X - i)(X + i)$ ; $\Delta < 0 \Rightarrow$ irréductible dans $\mathbb{R}[X]$

Les questions sont indépendantes. Pour les questions 2, 3 et 4, ce n'est pas la peine de donner les polynômes sous une forme développée.
1. Soit $P \in \mathbb{R}[X]$ de degré strictement supérieur à 3. Mettre les symboles $\Rightarrow$, $\Leftarrow$ ou $\iff$ à la place des pointillés.
   a) $-1$ racine de $P$ $\dots$ $(X+1) \mid P$. b) $(X-1)^2 \mid P$ $\dots$ $P(1) = 0$. c) $P(0) = 0$ $\dots$ $P(X) = X^4 + X$. d) $P(1) = P(2) = 0$ $\dots$ $(X-1)(X-2) \mid P$. e) $(X-1)^3 \mid P$ $\dots$ $P(1) = P'(1) = 0$.
2. Donner un exemple d'un polynôme $P \in \mathbb{R}[X]$, de degré 3, ayant $-1$ et 2 comme racines simples.
3. Donner un exemple d'un polynôme $Q \in \mathbb{R}[X]$, de degré 5, ayant $-2$ comme racine d'ordre de multiplicité exactement égal à 3.
4. Donner un exemple d'un polynôme $A \in \mathbb{R}[X]$, de degré 4, vérifiant $A(0) = 0$ et $A(-3) = A'(-3) = 0$.
5. Dans la liste de polynômes ci-dessous, entourer les polynômes irréductibles dans $\mathbb{R}[X]$ : a) $2X + 1$ ; b) $X^2 + X$ ; c) $X^3 + X + 1$ (scan flou : la conclusion ne dépend pas des coefficients, tout polynôme de degré 3 est réductible dans $\mathbb{R}[X]$) ; d) $X^2 - 1$ ; e) $X^2 + X + 1$.

## 2. Équations différentielles (6 points)
Type : démonstration de cours (structure des solutions de $a(t)y' + b(t)y = c(t)$) · ECUE : APIS (EDO) · Niveau : maths-s1-apis-edo/5
Formules : $S_0 = \{t \mapsto ke^{-F(t)}\}$, $F' = \frac ba$ ; $S = \{y_p + y_0,\ y_0 \in S_0\}$ ; linéarité : $a(y_p + y_0)' + b(y_p + y_0) = c + 0$ (inclusion $\supset$) ; si $y \in S$ alors $y - y_p \in S_0$ (inclusion $\subset$) ; retrouver l'équation : $y_0 = ke^{-F}$ donne $\frac ba = F'$, puis $c = ay_p' + by_p$

Soient $a$, $b$ et $c$ trois fonctions continues sur $\mathbb{R}$ telles que $\forall t \in \mathbb{R}$, $a(t) \neq 0$. On considère l'équation différentielle $(E)$ : $a(t)y'(t) + b(t)y(t) = c(t)$. On note $S$ l'ensemble des solutions de $(E)$ et $S_0$ l'ensemble des solutions de $(E_0)$, l'équation homogène associée à $(E)$.
1. Donner $S_0$.
2. Soit $y_p$ une solution particulière de $(E)$ sur $\mathbb{R}$. Notons $B = \{y_p + y_0 ;\ y_0 \in S_0\}$.
   - (a) Continuer naturellement les phrases incomplètes : « Soit $f \in B$. Pour tout $t \in \mathbb{R}$, on a $f(t) = \dots$ avec $y_0 \in S_0$. $f$ est dérivable sur $\mathbb{R}$ et $\forall t \in \mathbb{R}$, $f'(t) = \dots$ Ainsi, $\forall t \in \mathbb{R}$, $a(t)f'(t) + b(t)f(t) = \dots = \dots = \dots$ car $\dots$ Donc $f \in \dots$ »
   - (b) Entourer l'inclusion que vous venez de démontrer : a) $S \subset B$ ; b) $B \subset S$.
   - (c) Démontrer que $S = B$ en faisant l'autre inclusion.
3. Trouver $a$, $b$ et $c$ trois fonctions telles que l'équation $(E)$ : $a(t)y' + b(t)y = c(t)$ ait pour ensemble de solutions $S = \{ t \mapsto ke^{\arctan(t)} + 1,\ k \in \mathbb{R} \}$.

## 3. Développements limités usuels (6 points)
Type : développements limités usuels et composés · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/8
Formules : $e^u = \sum \frac{u^k}{k!}$ ; $\cos u = 1 - \frac{u^2}2 + \frac{u^4}{24}$ ; $\sin u = u - \frac{u^3}6$ ; $\ln(1+u) = u - \frac{u^2}2 + \frac{u^3}3 - \frac{u^4}4$ ; $\sqrt{1+u} = 1 + \frac u2 - \frac{u^2}8 + \frac{u^3}{16} - \frac{5u^4}{128}$ ; $(1+u)^\alpha = 1 + \alpha u + \frac{\alpha(\alpha-1)}2u^2$ ; produit tronqué ; composition : poser $u$, calculer $u^2$ à l'ordre voulu ; $1 + \cos 2x = 2\cos^2 x$

Donner pour chaque fonction ci-dessous le développement limité en 0 à l'ordre 3.
1. $e^x$
2. $\cos(x)$
3. $\ln(1+x)$
4. $\sin(x)$
5. Soit $\alpha \in \mathbb{R}$, $(1+x)^\alpha$
6. (Pour celui-là, vous détaillerez les calculs) $f : x \mapsto \sqrt{1+x}$
