# Correction du partiel S2 — mai 2022

- Source : `raw/S2/Finals/Maths PC/2026/final-2026-s2-maths-correction-fr.pdf` (5 pages)
- Date réelle : mai 2022 (dossier promo 2026). Sujet : `final-2026-s2-maths-subject-fr.md` (énoncés repris en abrégé).

## Exercice 1
Type : développements limités usuels et composés · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/8
Formules : $e^u = \sum \frac{u^k}{k!}$ ; $\cos u = 1 - \frac{u^2}2 + \frac{u^4}{24}$ ; $\sin u = u - \frac{u^3}6$ ; $\ln(1+u) = u - \frac{u^2}2 + \frac{u^3}3 - \frac{u^4}4$ ; $\sqrt{1+u} = 1 + \frac u2 - \frac{u^2}8 + \frac{u^3}{16} - \frac{5u^4}{128}$ ; $(1+u)^\alpha = 1 + \alpha u + \frac{\alpha(\alpha-1)}2u^2$ ; produit tronqué ; composition : poser $u$, calculer $u^2$ à l'ordre voulu ; $1 + \cos 2x = 2\cos^2 x$

1. En 0 : $e^u = 1 + u + \frac{u^2}{2!} + \frac{u^3}{3!} + \frac{u^4}{4!} + o(u^4)$ ; $\cos u = 1 - \frac{u^2}{2!} + \frac{u^4}{4!} + o(u^4)$ ; $\sin u = u - \frac{u^3}{3!} + o(u^4)$ ; $\ln(1 + u) = u - \frac{u^2}2 + \frac{u^3}3 - \frac{u^4}4 + o(u^4)$ ; $\sqrt{1 + u} = 1 + \frac u2 - \frac{u^2}8 + \frac{u^3}{16} - \frac{5u^4}{128} + o(u^4)$.
2. $f(x) = \left(-2x - 2x^2 - \frac83x^3 - 4x^4 + o(x^4)\right)\left(\frac x2 - \frac{x^3}{48} + o(x^4)\right) = -x^2 + \frac{x^4}{24} - x^3 - \frac{4x^4}3 + o(x^4) = -x^2 - x^3 - \frac{31x^4}{24} + o(x^4)$.
3. $g(x) = \sqrt{1 + 1 - 2x^2 + \frac{2x^4}3 + o(x^4)} = \sqrt2\sqrt{1 - x^2 + \frac{x^4}3 + o(x^4)}$. Avec $u = -x^2 + \frac{x^4}3$, $u^2 = x^4 + o(x^4)$ : $g(x) = \sqrt2\left(1 - \frac{x^2}2 + \frac{x^4}6 - \frac{x^4}8\right) + o(x^4) = \sqrt2 - \frac{\sqrt2x^2}2 + \frac{\sqrt2x^4}{24} + o(x^4)$.

## Exercice 2
Type : développements limités, limite par équivalents · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/9
Formules : en 0 : $e^x = 1 + x + \frac{x^2}2 + \frac{x^3}6 + o(x^3)$ ; $\ln(1+x) = x - \frac{x^2}2 + o(x^2)$ ; $\cos x = 1 - \frac{x^2}2 + o(x^3)$ ; $\sin x = x - \frac{x^3}6 + o(x^3)$ ; $\frac1{1-x} = 1 + x + x^2 + x^3 + o(x^3)$ ; produit de DL tronqué à l'ordre ; $a^b = e^{b\ln a}$ ; $f \sim g \Rightarrow$ même limite

1. $N(x) = \cos(2x^2) - 1 = -2x^4 + o(x^4) \sim -2x^4$ ; $D(x) = e^x - e^{-x} - 2x = \frac{x^3}3 + o(x^3) \sim \frac{x^3}3$. $\frac{N}{D} \sim -6x \to 0$ : la limite vaut 0.
2. $x^2\left(e^{1/x^2} - \cos\frac1x\right) = x^2\left(1 + \frac1{x^2} + o\left(\frac1{x^2}\right) - 1 + \frac1{2x^2} + o\left(\frac1{x^2}\right)\right) = \frac32 + o(1)$ : la limite vaut $\frac32$.

## Exercice 3
Type : inverse d'une matrice, application linéaire associée · ECUE : ALM · Niveau : maths-s2-alm/8
Formules : pivot de Gauss sur $AU = V$ ; $A$ inversible $\iff f$ bijective, $\mathrm{Mat}(f^{-1}) = A^{-1}$ ; colonnes de $A$ = images des vecteurs de la base de départ ; $g(aX^2 + bX + c) = ag(X^2) + bg(X) + cg(1)$

1. $AU = V$ ; $L_2 \leftarrow L_2 - 2L_1$, $L_3 \leftarrow 2L_3 + L_1$, puis $L_3 \leftarrow L_2 - L_3$ : système échelonné, d'où $x = -4X + 2Y - Z$, $y = -3X + Y - 2Z$, $z = 5X - 2Y + 2Z$.
$A^{-1} = \begin{pmatrix} -4 & 2 & -1 \\ -3 & 1 & -2 \\ 5 & -2 & 2 \end{pmatrix}$ (vérifier au brouillon).
2. $A$ inversible, donc $f$ bijective ; $f^{-1}(x, y, z) = (-4x + 2y - z, -3x + y - 2z, 5x - 2y + 2z)$.
3. Les colonnes de $A$ donnent $g(1) = (2, 4, -1)$, $g(X) = (2, 3, -2)$, $g(X^2) = (3, 5, -2)$. Pour $P = aX^2 + bX + c$ : $g(P) = (3a + 2b + 2c, 5a + 3b + 4c, -2a - 2b - c)$.

## Exercice 4
Type : familles libres, génératrices, bases ; coordonnées · ECUE : EV · Niveau : maths-s2-ev/7
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \lambda_i = 0$ ; en dimension $n$, une famille libre de $n$ vecteurs est une base ; plus de $n$ vecteurs $\Rightarrow$ liée ; coordonnées : résoudre $P = \alpha Q_1 + \beta Q_2 + \gamma Q_3$ en identifiant les coefficients

1. $-P_2 - 2P_1 = P_3$ : $\mathcal{F}_1$ liée, pas une base. Pour $\mathcal{F}_2$ : $\alpha Q_1 + \beta Q_2 + \gamma Q_3 = 0 \iff \alpha + \beta = 0$, $\beta - \gamma = 0$, $\beta + \gamma = 0 \iff \alpha = \beta = \gamma = 0$ ; libre de cardinal $3 = \dim E$ : base. $P = \alpha Q_1 + \beta Q_2 + \gamma Q_3$ : $\alpha + \beta = 5$, $\beta - \gamma = 7$, $\beta + \gamma = -1$, d'où $(2, 3, -4)$.
2. (a) $(u, v)$ génératrice de $G$ par définition ; $u$ et $v$ non colinéaires donc libre : base de $G$.
(b) $w = \alpha u + \beta v$ : $2\alpha + \beta = -15$, $3\alpha - \beta = 5$, $-\alpha - 2\beta = a$, d'où $\alpha = -2$, $\beta = -11$, $a = 24$.

## Exercice 5
Type : noyau, image, rang ; matrice d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/5
Formules : $\mathrm{Ker} f$ : résoudre $f(P) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \dim\mathrm{Im} f$ ; injective $\iff \mathrm{Ker} = \{0\}$ ; $\dim\mathrm{Im} = \dim F \Rightarrow$ surjective ; colonne $j$ = coordonnées de $f(e_j)$ dans la base d'arrivée

1. $\mathrm{Ker}(f) = \{aX^2 + bX + c, c = 0, 2a + b = 0\} = \{a(X^2 - 2X), a \in \mathbb{R}\} = \mathrm{Vect}(X^2 - 2X)$ ; $X^2 - 2X \neq 0$ : base, $\dim \mathrm{Ker}(f) = 1$.
2. Théorème du rang : $E$, $F$ $\mathbb{R}$-ev, $E$ de dimension finie, $f \in \mathcal{L}(E, F)$ : $\dim E = \dim \mathrm{Ker} f + \dim \mathrm{Im} f$. Ici $\dim \mathrm{Im}(f) = 3 - 1 = 2$.
3. $\mathrm{Ker}(f) \neq \{0\}$ : pas injective. $\dim \mathrm{Im}(f) = 2 = \dim \mathbb{R}^2$ : $\mathrm{Im}(f) = \mathbb{R}^2$, surjective.
4. $f(1) = (1, 0)$, $f(X) = (0, 1)$, $f(X^2) = (0, 2)$ : $\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 2 \end{pmatrix}$.
5. $f(1) = 1 \cdot (2, 1) + 1 \cdot (-1, -1)$, $f(X) = -1 \cdot (2, 1) - 2 \cdot (-1, -1)$, $f(X^2) = -2(2, 1) - 4(-1, -1)$ : $\begin{pmatrix} 1 & -1 & -2 \\ 1 & -2 & -4 \end{pmatrix}$.

## Exercice 6
Type : projecteur, noyau et image · ECUE : ALM · Niveau : maths-s2-alm/10
Formules : projecteur $\iff f \circ f = f$ ; $E = \mathrm{Ker} f \oplus \mathrm{Im} f$ ; $f = id$ sur $\mathrm{Im} f$, $0$ sur $\mathrm{Ker} f$ ; matrice dans une base adaptée $\mathrm{diag}(0, \dots, 0, 1, \dots, 1)$

1. $C_3 = C_1 + C_2$ : liée. $(C_1, C_2)$ non colinéaires : famille libre maximale.
2. $\mathrm{Im}(f) = \mathrm{Vect}(C_1, C_2)$, base $\mathcal{B}_1 = (C_1, C_2)$, dimension 2. Théorème du rang : $\dim \mathrm{Ker}(f) = 1$ ; $C_1 + C_2 - C_3 = 0$ donne $(1, 1, -1) \in \mathrm{Ker}(f)$, base $\mathcal{B}_2 = ((1, 1, -1))$.
3. Si $u \in \mathrm{Ker}(f) \cap \mathrm{Im}(f)$ : $u = \alpha C_1 + \beta C_2 = (\alpha + \beta, 2\beta, -\beta)$ et $u = \gamma(1, 1, -1)$, d'où $\alpha = \beta = \gamma = 0$. Puis $\dim(\mathrm{Ker} + \mathrm{Im}) = 1 + 2 - 0 = 3$ : $\mathrm{Im}(f) \oplus \mathrm{Ker}(f) = \mathbb{R}^3$.
4. $A^2 = A$ : $f \circ f = f$, $f$ est un projecteur (projection sur $\mathrm{Im}(f)$ parallèlement à $\mathrm{Ker}(f)$).
5. Si $v \in \mathrm{Im}(f)$, $v = f(v_1)$ et $f(v) = f^2(v_1) = v$. Si $u = v + w$ avec $v \in \mathrm{Im}(f)$, $w \in \mathrm{Ker}(f)$ : $f(u) = v$.
6. $f(C_1) = C_1$, $f(C_2) = C_2$, $f((1, 1, -1)) = 0$ : $\mathrm{Mat}_{\mathcal{B}}(f) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix}$.

## Exercice 7
Type : symétrie par rapport à un sous-espace · ECUE : ALM · Niveau : maths-s2-alm/10
Formules : $E = F \oplus G$ : $u = v + w$ unique ; projection sur $F$ : $u \mapsto v$ ; symétrie par rapport à $F$ parallèlement à $G$ : $u \mapsto v - w$, $s \circ s = id$

1. $u = (1, 3) = (2, 2) + (-1, 1)$ : $v = (2, 2)$, $w = (-1, 1)$, $s(u) = v - w = (3, 1)$.
2. Graphiquement : on projette $u$ sur $F$ parallèlement à $G$ (et inversement), puis $s(u) = v - w$. $s$ est la symétrie par rapport à $F$ parallèlement à $G$.
