# Contrôle de mi-semestre (S2) — mars 2021 (corrigé, FR)

- Source : `raw/S2/Midterms/Maths PC/2025/midterm-2025-s2-maths-correction-fr.pdf` (5 pages)
- Date réelle : mars 2021 (dossier promo 2025 ; l'en-tête du corrigé porte par erreur « Partiel – janvier 2021 »). Sujet : `midterm-2025-s2-maths-subject-fr.md`.
- Corrigé officiel.

## Exercice 1 (4 points)
Type : EDO linéaires 1er ordre (variation de la constante, solution particulière trigonométrique) · ECUE : APIS (EDO) · Niveau : maths-s1-apis-edo/5
Formules : $a(t)y' + b(t)y = 0 \Rightarrow y_0 = ke^{-\int \frac ba}$ ; solution générale = homogène + particulière ; variation de la constante : $y_p = k(t)y_0(t)$, les termes en $k$ s'annulent, reste $k'$ ; $\int \frac1{2\sqrt t} = \sqrt t$ ; second membre $\cos + \sin$ : $y_p = a\cos t + b\sin t$, identifier les coefficients de $\cos$ et $\sin$

a. $(E_1)$ : $(t+3)y' + y = \dfrac1{2\sqrt t}$ sur $\mathbb{R}_+^*$.
- Équation homogène $(E_0)$ : $(t+3)y' + y = 0$. $\dfrac ba = \dfrac1{t+3}$, de primitive $\ln(t+3)$. Solutions : $y_0 = ke^{-\ln(t+3)} = \dfrac k{t+3}$, $k \in \mathbb{R}$.
- Variation de la constante : $y_p = \dfrac{k(t)}{t+3}$, $y_p' = \dfrac{k'(t)}{t+3} - \dfrac{k(t)}{(t+3)^2}$. $y_p$ solution $\iff k'(t) - \dfrac{k(t)}{t+3} + \dfrac{k(t)}{t+3} = \dfrac1{2\sqrt t} \iff k'(t) = \dfrac1{2\sqrt t}$. On prend $k(t) = \sqrt t$ : $y_p = \dfrac{\sqrt t}{t+3}$.
- $\mathcal{S} = \Big\{ y = \dfrac{\sqrt t}{t+3} + \dfrac k{t+3},\ k \in \mathbb{R} \Big\}$.

b. $(E_2)$ : $y' + y = \cos(t) + 2\sin(t)$ sur $\mathbb{R}$.
- $(E_0)$ : $y' + y = 0$, solutions $y_0 = ke^{-t}$, $k \in \mathbb{R}$.
- $y_p = a\cos t + b\sin t$, $y_p' = -a\sin t + b\cos t$. $y_p' + y_p = (a+b)\cos t + (b-a)\sin t$, donc $a + b = 1$ et $b - a = 2$ : $a = -\frac12$, $b = \frac32$.
- $\mathcal{S} = \big\{ y = -\frac12\cos t + \frac32\sin t + ke^{-t},\ k \in \mathbb{R} \big\}$.

## Exercice 2 (3 points)
Type : théorème des valeurs intermédiaires · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/2
Formules : TVI : $f$ continue sur $[a,b]$, $k$ entre $f(a)$ et $f(b)$ $\Rightarrow \exists c \in [a,b]$, $f(c) = k$ ; si $f(a)f(b) < 0$, $\exists c \in ]a,b[$, $f(c) = 0$

a. $f(x) = x^3 - 3x + 6$ est continue (polynomiale). $f(-3) = -12$, $f(3) = 24$, donc $f(-3)f(3) < 0$. D'après le TVI, $\exists c \in\ ]-3,3[$, $f(c) = 0$.

b. $f'(x) = 3x^2 - 3 = 3(x-1)(x+1)$ s'annule en $-1$ et $1$.

| $x$ | $-3$ | | $-1$ | | $1$ | | $3$ |
|---|---|---|---|---|---|---|---|
| $f'$ | | $+$ | $0$ | $-$ | $0$ | $+$ | |
| $f$ | $-12$ | ↗ | $8$ | ↘ | $4$ | ↗ | $24$ |

Sur $[-1, 3]$, $f$ a pour minimum 4, donc est strictement positive. $f$ est strictement croissante sur $[-3, -1]$, donc ne s'y annule qu'une fois. Comme $f(-2) = 4 > 0$, $f$ s'annule sur $]-3, -2[$ : $(E)$ admet une unique racine $c$, avec $-3 < c < -2$.

## Exercice 3 (6 points)
Type : développements limités usuels et composés · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/8
Formules : $e^u = \sum \frac{u^k}{k!}$ ; $\cos u = 1 - \frac{u^2}2 + \frac{u^4}{24}$ ; $\sin u = u - \frac{u^3}6$ ; $\ln(1+u) = u - \frac{u^2}2 + \frac{u^3}3 - \frac{u^4}4$ ; $\sqrt{1+u} = 1 + \frac u2 - \frac{u^2}8 + \frac{u^3}{16} - \frac{5u^4}{128}$ ; $(1+u)^\alpha = 1 + \alpha u + \frac{\alpha(\alpha-1)}2u^2$ ; produit tronqué ; composition : poser $u$, calculer $u^2$ à l'ordre voulu ; $1 + \cos 2x = 2\cos^2 x$

1. $e^x = 1 + x + \frac{x^2}2 + o(x^2)$ ; $(1+x)^\alpha = 1 + \alpha x + \frac{\alpha(\alpha-1)}2x^2 + o(x^2)$, avec $\alpha = -\frac12$ : $(1+x)^{-\frac12} = 1 - \frac x2 + \frac38x^2 + o(x^2)$.
   $f(x) = \big(1 + x + \frac{x^2}2\big)\big(1 - \frac x2 + \frac38x^2\big) + o(x^2) = 1 + \dfrac x2 + \dfrac38x^2 + o(x^2)$.
2. $\cos x = 1 - \frac{x^2}2 + \frac{x^4}{24} + o(x^4)$, donc $g(x) = \ln\Big(2\big(1 - \frac{x^2}4 + \frac{x^4}{48} + o(x^4)\big)\Big) = \ln 2 + \ln(1 + X)$ avec $X = -\frac{x^2}4 + \frac{x^4}{48} + o(x^4) \to 0$.
   $\ln(1+X) = X - \frac{X^2}2 + o(X^2) = -\frac{x^2}4 + \frac{x^4}{48} - \frac12 \cdot \frac{x^4}{16} + o(x^4)$, donc $g(x) = \ln 2 - \dfrac{x^2}4 - \dfrac{x^4}{96} + o(x^4)$.
3. On pose $X = \frac1x \to 0$. $h(X) = (1 + 2\sin X)^{1/X} = e^{\frac1X\ln(1 + 2\sin X)} = e^{\frac1X\ln(1 + 2X + o(X))} = e^{\frac1X(2X + o(X))} = e^{2 + o(1)}$. La limite vaut $e^2$.

## Exercice 4 (4 points)
Type : reconnaître un sous-espace vectoriel · ECUE : EV · Niveau : maths-s2-ev/3
Formules : sev : contient 0, stable par addition et multiplication par un scalaire ; contre-exemple $\lambda u \notin E$ ; équation non linéaire ($z^2$) $\Rightarrow$ en général pas un sev ; $\mathrm{Vect}(\dots)$ est toujours un sev

a.
- $A$ : $A \subset E$, $0_E \in A$, et $\forall (u,v) \in A^2$, $\forall \lambda \in \mathbb{R}$, $\lambda u + v = 0_E \in A$. $A$ est un sev de $E$.
- $B$ : $u = (0,1) \in B$ mais pour $\lambda = -1$, $\lambda u = (0,-1) \notin B$. $B$ n'est pas stable par le produit externe : ce n'est pas un sev.
- $C$ : $0 - 2 \times 0 = 0$ donc $0_E \in C$. Pour $u = (x,y)$, $v = (x',y')$ dans $C$ et $\lambda \in \mathbb{R}$ : $(\lambda x + x') - 2(\lambda y + y') = \lambda(x - 2y) + (x' - 2y') = 0$, donc $\lambda u + v \in C$. $C$ est un sev de $E$.
- $D$ : $0 - 2 \times 0 = 0 \neq 1$ donc $0_E \notin D$. $D$ n'est pas un sev.

(Le corrigé officiel écrit la condition de $C$ sous la forme $2x - y = 0$ : coquille sans effet sur la conclusion.)

b. Les sous-espaces vectoriels de $\mathbb{R}^2$ sont $\{0_E\}$, les droites vectorielles (droites passant par l'origine) et le plan $\mathbb{R}^2$.

## Exercice 5 (3 points)
Type : sous-espaces, intersection, somme directe · ECUE : EV · Niveau : maths-s2-ev/9
Formules : $\mathrm{Vect}(u)$ : droite si $u \neq 0$ ; plan $ax + by + cz = 0$ : exprimer $z$, $G = \mathrm{Vect}(u, v)$ ; $u \in F \cap G$ : paramétrer par $F$ puis injecter l'équation de $G$ ; Grassmann $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $\dim F + \dim G = \dim E$

$F \oplus G = E \iff F \cap G = \{0_E\}$ et $F + G = E$.

- $\{0_E\} \subset F \cap G$ (deux sev). Si $u = (x,y,z) \in F \cap G$ : $u \in F \Rightarrow z = 0$ et $u \in G \Rightarrow x = y = z$, donc $u = (0,0,0)$. Ainsi $F \cap G = \{0_E\}$.
- $F = \mathrm{Vect}\{(1,0,0) ; (0,1,0)\}$, famille libre : $\dim F = 2$. $G = \mathrm{Vect}\{(1,1,1)\}$ : $\dim G = 1$. $\dim(F + G) = \dim F + \dim G - \dim(F \cap G) = 3 = \dim E$ et $F + G \subset E$, donc $F + G = E$.

Donc $F \oplus G = E$.

## Exercice 6 (3 points)
Type : familles libres, génératrices, bases ; coordonnées · ECUE : EV · Niveau : maths-s2-ev/7
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \lambda_i = 0$ ; en dimension $n$, une famille libre de $n$ vecteurs est une base ; plus de $n$ vecteurs $\Rightarrow$ liée ; coordonnées : résoudre $P = \alpha Q_1 + \beta Q_2 + \gamma Q_3$ en identifiant les coefficients

a. Si $\alpha u + \beta v + \gamma w = 0_E$ : $\alpha + \gamma = 0$, $\alpha + \beta = 0$, $\beta + \gamma = 0$, d'où $\alpha = -\gamma$, $-\gamma + \beta = 0$, $\beta + \gamma = 0$, donc $\alpha = \beta = \gamma = 0$ : $\mathcal{F}$ est libre. De plus $\mathrm{card}\,\mathcal{F} = 3 = \dim \mathbb{R}^3$ : $\mathcal{F}$ est une base de $\mathbb{R}^3$.

b. $\alpha u + \beta v + \gamma w = (1,3,0)$ : $\alpha + \gamma = 1$, $\alpha + \beta = 3$, $\beta + \gamma = 0$. Donc $\beta = -\gamma$, $\alpha - \gamma = 3$, $\alpha + \gamma = 1$ : $\alpha = 2$, $\gamma = -1$, $\beta = 1$. Coordonnées : $(2, 1, -1)$.

(Le corrigé officiel encadre $(2, -1, 1)$ : inversion de $\beta$ et $\gamma$ ; vérification : $2u + v - w = (1, 3, 0)$.)

## Exercice 7 (3 points)
Type : sous-espaces engendrés, inclusion, dimension · ECUE : EV · Niveau : maths-s2-ev/4
Formules : $P \in \mathrm{Vect}(u_1, \dots) \iff P$ combinaison linéaire des $u_i$ ; $F \subset G$ si les générateurs de $F$ sont dans $G$ ; famille génératrice libre = base, $\dim$ = cardinal

a. $y = z$ et $x = z - y = 0$ : $F = \{(0,y,y,t),\ (y,t) \in \mathbb{R}^2\} = \mathrm{Vect}\{(0,1,1,0) ; (0,0,0,1)\}$.

b. $\{(0,1,1,0) ; (0,0,0,1)\}$ est génératrice de $F$ et libre (deux vecteurs non colinéaires) : c'est une base de $F$, $\dim F = 2$.
$(-2,2,0,-2) = -2(1,-1,0,1)$ donc $G = \mathrm{Vect}\{(1,-1,0,1)\}$ ; un vecteur non nul forme une famille libre : $\dim G = 1$.

## Exercice 8 (4 points)
Type : familles libres, génératrices, bases · ECUE : EV · Niveau : maths-s2-ev/6
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \forall i, \lambda_i = 0$ ; génératrice : tout vecteur est combinaison linéaire ; base = libre + génératrice ; $\dim \mathbb{R}_n[X] = n + 1$ ; en dimension $n$ : plus de $n$ vecteurs $\Rightarrow$ liée, moins de $n$ $\Rightarrow$ non génératrice, $n$ vecteurs libres $\Rightarrow$ base ; degrés échelonnés $\Rightarrow$ libre

- $\mathcal{F}_1$ : $\alpha P + \beta Q + \gamma R = 0$ donne (coefficients de $X^3$, $X^2$, $X$, 1) : $-\alpha + 2\beta = 0$, $\alpha + 2\gamma = 0$, $2\alpha - \beta + 3\gamma = 0$, $-2\alpha + 3\beta - \gamma = 0$. D'où $\alpha = 2\beta$, $\gamma = -\beta$, et les deux dernières équations sont alors vérifiées. Avec $\beta = 1$ : $2P + Q - R = 0$. La famille $\mathcal{F}_1$ est liée.
- $\mathcal{F}_2$ : $\alpha(u_n) + \beta(v_n) + \gamma(w_n) = 0 \iff \forall n$, $\alpha n + \beta 2^n + \gamma\frac n{n+1} = 0$. $n = 0$ : $\beta = 0$. $n = 1$ : $\alpha + \frac12\gamma = 0$. $n = 2$ : $2\alpha + \frac23\gamma = 0$. Donc $\alpha = -\frac12\gamma = -\frac13\gamma$, d'où $\alpha = \beta = \gamma = 0$. La famille $\mathcal{F}_2$ est libre.
