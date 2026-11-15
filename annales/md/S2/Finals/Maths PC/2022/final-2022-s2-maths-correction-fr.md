# Corrigé du partiel 2 (S2) — mai 2018

- Source : `raw/S2/Finals/Maths PC/2022/final-2022-s2-maths-correction-fr.pdf` (3 pages)
- Date réelle : mai 2018 (Info-Sup 17/18, dossier promo 2022). Sujet : `final-2022-s2-maths-subject-fr.md`.

## Exercice 1 (2 points)
Type : inverse d'une matrice · ECUE : ALM · Niveau : maths-s2-alm/8
Formules : $A$ inversible $\iff \det A \neq 0$ ; pivot de Gauss sur $(A \mid I_n) \to (I_n \mid A^{-1})$ ; ou $A^{-1} = \frac1{\det A}{}^t\mathrm{Com}(A)$ ; vérifier $AA^{-1} = I_n$ ; $2 \times 2$ : $\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1} = \frac1{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$

Soient $U = (x, y, z)^T$ et $V = (X, Y, Z)^T$. $AU = V \iff U = A^{-1}V$.
$AU = V \iff \begin{cases} x + 2y + 3z = X & (1) \\ -x - y + z = Y & (2) \\ 2x + 4y + 5z = Z & (3) \end{cases} \iff \begin{cases} x + 2y + 3z = X \\ y + 4z = X + Y \\ -z = Z - 2X \end{cases}$ ($(2) \leftarrow (2) + (1)$, $(3) \leftarrow (3) - 2(1)$)
$\iff \begin{cases} x = 9X - 2Y - 5Z \\ y = -7X + Y + 4Z \\ z = 2X - Z \end{cases}$. Ainsi $A^{-1} = \begin{pmatrix} 9 & -2 & -5 \\ -7 & 1 & 4 \\ 2 & 0 & -1 \end{pmatrix}$.

## Exercice 2 (4 points)
Type : décomposition en éléments simples · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/8
Formules : si $\deg N \geqslant \deg D$ : division euclidienne, partie entière ; pôle simple $a$ : $\frac{c}{X - a}$ avec $c = \left[(X - a)F\right](a)$ ; pôle double : $\frac{c_1}{X-a} + \frac{c_2}{(X-a)^2}$ ; facteur irréductible $X^2 + 1$ : $\frac{bX + c}{X^2 + 1}$ ; identifier en évaluant (ex. $X = 0$) ou par limite de $xF(x)$ en $+\infty$

1. $F(X) = \dfrac{a}{X - 1} + \dfrac{b}{X - 2} + \dfrac{c}{X + 2}$. En multipliant par $X - 1$ puis $X = 1$ : $a = -\frac13$ ; par $X - 2$ puis $X = 2$ : $b = \frac54$ ; par $X + 2$ puis $X = -2$ : $c = \frac1{12}$.
$F(X) = -\dfrac1{3(X - 1)} + \dfrac5{4(X - 2)} + \dfrac1{12(X + 2)}$.
2. Division euclidienne par $(X - 1)^2(X + 1) = X^3 - X^2 - X + 1$ : $X^4 + X^3 + X^2 + 2X + 2 = (X^3 - X^2 - X + 1)(X + 2) + 4X^2 + 3X$, donc $G(X) = X + 2 + \dfrac{4X^2 + 3X}{(X - 1)^2(X + 1)}$.
$R(X) = \dfrac{4X^2 + 3X}{(X - 1)^2(X + 1)} = \dfrac{a}{X + 1} + \dfrac{b}{X - 1} + \dfrac{c}{(X - 1)^2}$ : avec $X + 1$ et $X = -1$, $a = \frac14$ ; avec $(X - 1)^2$ et $X = 1$, $c = \frac72$ ; en $X = 0$, $b = \frac{15}4$.
$G(X) = X + 2 + \dfrac1{4(X + 1)} + \dfrac{15}{4(X - 1)} + \dfrac7{2(X - 1)^2}$.
3. $H(X) = \dfrac{a}{X + 1} + \dfrac{bX + c}{X^2 + X + 1}$. Avec $X + 1$ et $X = -1$ : $a = 1$. En $X = 0$ : $-1 = 1 + c$, $c = -2$. Limite en $+\infty$ de $XH(X)$ : $2 = 1 + b$, $b = 1$.
$H(X) = \dfrac1{X + 1} + \dfrac{X - 2}{X^2 + X + 1}$.

## Exercice 3 (2 points)
Type : injectivité et noyau · ECUE : ALM · Niveau : maths-s2-alm/2
Formules : $f$ linéaire : $f(0) = 0$, $f(x) - f(y) = f(x - y)$ ; $f$ injective $\iff \mathrm{Ker} f = \{0\}$

Supposons $f$ injective. $\{0\} \subset \mathrm{Ker}(f)$ est immédiat. Soit $x \in \mathrm{Ker}(f)$ : $f(x) = 0 = f(0)$, et $f$ injective donne $x = 0$.
Supposons $\mathrm{Ker}(f) = \{0\}$. Si $f(x) = f(y)$, par linéarité $f(x - y) = 0$, donc $x - y \in \mathrm{Ker}(f) = \{0\}$ et $x = y$ : $f$ injective.

## Exercice 4 (3 points)
Type : matrice d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/5
Formules : colonne $j$ = coordonnées de $f(e_j)$ dans la base d'arrivée ; base canonique de $\mathbb{R}_2[X]$ : $(1, X, X^2)$ ; de $\mathcal{M}_2(\mathbb{R})$ : $E_{11}, E_{12}, E_{21}, E_{22}$ ; taille (dim arrivée) $\times$ (dim départ)

1. $\mathcal{B} = (1, X, X^2)$. $f(1) = 2X$, $f(X) = X^2$, $f(X^2) = 0$, donc $\mathrm{Mat}_{\mathcal{B}}(f) = \begin{pmatrix} 0 & 0 & 0 \\ 2 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}$.
2. $\mathcal{B} = (E_{11}, E_{12}, E_{21}, E_{22})$. $f(E_{11}) = E_{22}$, $f(E_{12}) = -E_{21}$, $f(E_{21}) = -E_{12}$, $f(E_{22}) = E_{11}$, donc $\mathrm{Mat}_{\mathcal{B}}(f) = \begin{pmatrix} 0 & 0 & 0 & 1 \\ 0 & 0 & -1 & 0 \\ 0 & -1 & 0 & 0 \\ 1 & 0 & 0 & 0 \end{pmatrix}$.

## Exercice 5 (2,5 points)
Type : noyau et image d'un endomorphisme (inclusions) · ECUE : ALM · Niveau : maths-s2-alm/12
Formules : $\mathrm{Ker} f = \{x, f(x) = 0\}$ ; $\mathrm{Im} f = \{f(x)\}$ ; $f(0) = 0$ ; $x \in \mathrm{Ker} f \Rightarrow f^2(x) = f(0) = 0$ ; $f^2(x) = f(f(x)) \in \mathrm{Im} f$ ; double implication par éléments

$\Rightarrow$ : supposons $\mathrm{Ker}(u) \cap \mathrm{Im}(u) = \{0\}$. $\mathrm{Ker}(u) \subset \mathrm{Ker}(u^2)$ est immédiat. Soit $x \in \mathrm{Ker}(u^2)$ : $u(u(x)) = 0$, donc $u(x) \in \mathrm{Ker}(u) \cap \mathrm{Im}(u) = \{0\}$, d'où $x \in \mathrm{Ker}(u)$.
$\Leftarrow$ : supposons $\mathrm{Ker}(u) = \mathrm{Ker}(u^2)$. Soit $x \in \mathrm{Ker}(u) \cap \mathrm{Im}(u)$ : $u(x) = 0$ et $x = u(z)$. Alors $u^2(z) = u(x) = 0$, donc $z \in \mathrm{Ker}(u^2) = \mathrm{Ker}(u)$ et $x = u(z) = 0$.

## Exercice 6 (2,5 points)
Type : familles libres, génératrices, bases · ECUE : EV · Niveau : maths-s2-ev/6
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \forall i, \lambda_i = 0$ ; génératrice : tout vecteur est combinaison linéaire ; base = libre + génératrice ; $\dim \mathbb{R}_n[X] = n + 1$ ; en dimension $n$ : plus de $n$ vecteurs $\Rightarrow$ liée, moins de $n$ $\Rightarrow$ non génératrice, $n$ vecteurs libres $\Rightarrow$ base ; degrés échelonnés $\Rightarrow$ libre

1. $v - w = 2u$ : $u$, $v$, $w$ sont liés et ne forment pas une base de $\mathbb{R}^3$.
2. Soit $(\alpha, \beta)$ tel que $\alpha f + \beta g = 0$ : $\forall x$, $(\alpha + \beta)e^x + (\alpha - \beta)e^{-x} = 0$. En $x = 0$ : $\alpha = 0$. En $x = \ln 2$ : $2(\alpha + \beta) + \frac{\alpha - \beta}2 = 0$, d'où $\beta = 0$. $(f, g)$ libre et génératrice de $F$ : base, $\dim F = 2$.

## Exercice 7 (5 points)
Type : changement de base, diagonalisation, puissance d'une matrice · ECUE : ALM · Niveau : maths-s2-alm/9
Formules : $\mathrm{Mat}_{\mathcal{B}'}(f) = P^{-1}AP$ avec $P = \mathrm{Mat}_{\mathcal{B}', \mathcal{B}}(id)$ (colonnes = vecteurs de $\mathcal{B}'$ dans $\mathcal{B}$) ; $f(u_i) = \lambda_iu_i \Rightarrow D = \mathrm{diag}(\lambda_i)$ ; $D^n = \mathrm{diag}(\lambda_i^n)$ ; $A = PDP^{-1} \Rightarrow A^n = PD^nP^{-1}$

1. $A = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 3 & 0 \\ 2 & -4 & 2 \end{pmatrix}$.
2. $f(u_1) = (3, 3, -6) = 3u_1$, $f(u_2) = (0, 0, 2) = 2u_2$, $f(u_3) = (1, 0, -2) = u_3$, donc $\mathrm{Mat}_{\mathcal{B}'}(f) = \begin{pmatrix} 3 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{pmatrix}$.
3. $P = \begin{pmatrix} 1 & 0 & 1 \\ 1 & 0 & 0 \\ -2 & 1 & -2 \end{pmatrix}$, $P^{-1} = \mathrm{Mat}_{\mathcal{B}, \mathcal{B}'}(id) = \begin{pmatrix} 0 & 1 & 0 \\ 2 & 0 & 1 \\ 1 & -1 & 0 \end{pmatrix}$, $D = P^{-1}AP = \begin{pmatrix} 3 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \mathrm{Mat}_{\mathcal{B}'}(f)$.
4. $D^2 = \mathrm{diag}(9, 4, 1)$, $D^3 = \mathrm{diag}(27, 8, 1)$, donc $D^n = \mathrm{diag}(3^n, 2^n, 1)$.
5. $A = PDP^{-1}$ donc $A^2 = PDP^{-1}PDP^{-1} = PD^2P^{-1}$ et $A^n = PD^nP^{-1}$.
