# Partiel 2 (S2) — mai 2018 (sujet, FR)

- Source : `raw/S2/Finals/Maths PC/2022/final-2022-s2-maths-subject-fr.pdf` (scan, 9 pages)
- Date réelle : mai 2018 (S2 17/18, dossier promo 2022). Corrigé : `final-2022-s2-maths-correction-fr.md`.
- Barème : 21 points.

## Exercice 1 (2 points)
Type : inverse d'une matrice · ECUE : ALM · Niveau : maths-s2-alm/8
Formules : $A$ inversible $\iff \det A \neq 0$ ; pivot de Gauss sur $(A \mid I_n) \to (I_n \mid A^{-1})$ ; ou $A^{-1} = \frac1{\det A}{}^t\mathrm{Com}(A)$ ; vérifier $AA^{-1} = I_n$ ; $2 \times 2$ : $\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1} = \frac1{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$

Soit $A = \begin{pmatrix} 1 & 2 & 3 \\ -1 & -1 & 1 \\ 2 & 4 & 5 \end{pmatrix}$. Déterminer la matrice $A^{-1}$ en prenant soin de vérifier (au brouillon) le résultat final.

## Exercice 2 (4 points)
Type : décomposition en éléments simples · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/8
Formules : si $\deg N \geqslant \deg D$ : division euclidienne, partie entière ; pôle simple $a$ : $\frac{c}{X - a}$ avec $c = \left[(X - a)F\right](a)$ ; pôle double : $\frac{c_1}{X-a} + \frac{c_2}{(X-a)^2}$ ; facteur irréductible $X^2 + 1$ : $\frac{bX + c}{X^2 + 1}$ ; identifier en évaluant (ex. $X = 0$) ou par limite de $xF(x)$ en $+\infty$

Décomposer en éléments simples dans $\mathbb{R}(X)$ les fractions rationnelles suivantes :
1. $F(X) = \dfrac{X^2 + X - 1}{(X - 1)(X - 2)(X + 2)}$ ;
2. $G(X) = \dfrac{X^4 + X^3 + X^2 + 2X + 2}{(X - 1)^2(X + 1)}$ ;
3. $H(X) = \dfrac{2X^2 - 1}{(X + 1)(X^2 + X + 1)}$.

## Exercice 3 (2 points)
Type : injectivité et noyau · ECUE : ALM · Niveau : maths-s2-alm/2
Formules : $f$ linéaire : $f(0) = 0$, $f(x) - f(y) = f(x - y)$ ; $f$ injective $\iff \mathrm{Ker} f = \{0\}$

Soient $E$, $F$ deux $\mathbb{R}$-ev et $f \in \mathcal{L}(E, F)$. Montrer que $f$ injective ssi $\mathrm{Ker}(f) = \{0\}$.

## Exercice 4 (3 points)
Type : matrice d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/5
Formules : colonne $j$ = coordonnées de $f(e_j)$ dans la base d'arrivée ; base canonique de $\mathbb{R}_2[X]$ : $(1, X, X^2)$ ; de $\mathcal{M}_2(\mathbb{R})$ : $E_{11}, E_{12}, E_{21}, E_{22}$ ; taille (dim arrivée) $\times$ (dim départ)

1. Soit $f : \mathbb{R}_2[X] \to \mathbb{R}_2[X]$ définie pour tout $P \in \mathbb{R}_2[X]$ par $f(P(X)) = 2XP(X) - X^2P'(X)$. Déterminer la matrice de $f$ relativement à la base canonique de $\mathbb{R}_2[X]$.
2. Soit $f \in \mathcal{L}(\mathcal{M}_2(\mathbb{R}))$ définie par $f : \begin{pmatrix} a & b \\ c & d \end{pmatrix} \mapsto \begin{pmatrix} d & -c \\ -b & a \end{pmatrix}$. Déterminer la matrice de $f$ relativement à la base canonique de $\mathcal{M}_2(\mathbb{R})$.

## Exercice 5 (2,5 points)
Type : noyau et image d'un endomorphisme (inclusions) · ECUE : ALM · Niveau : maths-s2-alm/12
Formules : $\mathrm{Ker} f = \{x, f(x) = 0\}$ ; $\mathrm{Im} f = \{f(x)\}$ ; $f(0) = 0$ ; $x \in \mathrm{Ker} f \Rightarrow f^2(x) = f(0) = 0$ ; $f^2(x) = f(f(x)) \in \mathrm{Im} f$ ; double implication par éléments

Soient $E$ un $\mathbb{R}$-ev et $u \in \mathcal{L}(E)$. On note $u^2 = u \circ u$. Montrer que $\mathrm{Ker}(u) \cap \mathrm{Im}(u) = \{0\} \iff \mathrm{Ker}(u) = \mathrm{Ker}(u^2)$.

## Exercice 6 (2,5 points)
Type : familles libres, génératrices, bases · ECUE : EV · Niveau : maths-s2-ev/6
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \forall i, \lambda_i = 0$ ; génératrice : tout vecteur est combinaison linéaire ; base = libre + génératrice ; $\dim \mathbb{R}_n[X] = n + 1$ ; en dimension $n$ : plus de $n$ vecteurs $\Rightarrow$ liée, moins de $n$ $\Rightarrow$ non génératrice, $n$ vecteurs libres $\Rightarrow$ base ; degrés échelonnés $\Rightarrow$ libre

Dans les deux questions suivantes, vos réponses doivent être justifiées.
1. Les vecteurs $u = (1, 1, 0)$, $v = (4, 1, 4)$ et $w = (2, -1, 4)$ forment-ils une base de $\mathbb{R}^3$ ?
2. Soient $E = \mathbb{R}^{\mathbb{R}}$ l'espace des fonctions de $\mathbb{R}$ dans $\mathbb{R}$, $(f, g) \in E^2$ définies pour tout $x \in \mathbb{R}$ par $f(x) = \dfrac{e^x + e^{-x}}2$, $g(x) = \dfrac{e^x - e^{-x}}2$, et $F = \mathrm{Vect}(f, g)$. Quelle est la dimension de $F$ ?

## Exercice 7 (5 points)
Type : changement de base, diagonalisation, puissance d'une matrice · ECUE : ALM · Niveau : maths-s2-alm/9
Formules : $\mathrm{Mat}_{\mathcal{B}'}(f) = P^{-1}AP$ avec $P = \mathrm{Mat}_{\mathcal{B}', \mathcal{B}}(id)$ (colonnes = vecteurs de $\mathcal{B}'$ dans $\mathcal{B}$) ; $f(u_i) = \lambda_iu_i \Rightarrow D = \mathrm{diag}(\lambda_i)$ ; $D^n = \mathrm{diag}(\lambda_i^n)$ ; $A = PDP^{-1} \Rightarrow A^n = PD^nP^{-1}$

Soient $f : \mathbb{R}^3 \to \mathbb{R}^3,\ \begin{pmatrix} x \\ y \\ z \end{pmatrix} \mapsto \begin{pmatrix} x + 2y \\ 3y \\ 2x - 4y + 2z \end{pmatrix}$ et $A$ la matrice de $f$ relativement à la base canonique $\mathcal{B}$ de $\mathbb{R}^3$.
1. Déterminer $A$.
2. Soient $u_1 = \begin{pmatrix} 1 \\ 1 \\ -2 \end{pmatrix}$, $u_2 = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$, $u_3 = \begin{pmatrix} 1 \\ 0 \\ -2 \end{pmatrix}$ et $\mathcal{B}' = (u_1, u_2, u_3)$ qui forme une base de $\mathbb{R}^3$. Déterminer la matrice de $f$ relativement à $\mathcal{B}'$.
3. Soit $P = \mathrm{Mat}_{\mathcal{B}', \mathcal{B}}(id)$ où $id$ est l'application identité de $\mathbb{R}^3$ dans $\mathbb{R}^3$. Déterminer $P^{-1}$ puis $D = P^{-1}AP$. Que remarquez-vous ?
4. Calculer $D^2$, $D^3$ et en déduire (sans récurrence) $D^n$ pour tout $n \in \mathbb{N}$.
5. En déduire (sans récurrence) $A^n$ en fonction de $P$ et $D$ pour tout $n \in \mathbb{N}$.
