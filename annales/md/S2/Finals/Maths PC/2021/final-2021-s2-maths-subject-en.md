# Final exam 2 (S2) — June 2017 (subject, EN)

- Source : `raw/S2/Finals/Maths PC/2021/final-2021-s2-maths-subject-en.pdf` (scan, 10 pages)
- Date réelle : juin 2017 (S2 16/17, dossier promo 2021). Version anglaise de `final-2021-s2-maths-subject-fr.md` (mêmes exercices, mêmes données).

## Exercise 1 (2 points)
Type : inverse d'une matrice · ECUE : ALM · Niveau : maths-s2-alm/8
Formules : $A$ inversible $\iff \det A \neq 0$ ; pivot de Gauss sur $(A \mid I_n) \to (I_n \mid A^{-1})$ ; ou $A^{-1} = \frac1{\det A}{}^t\mathrm{Com}(A)$ ; vérifier $AA^{-1} = I_n$ ; $2 \times 2$ : $\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1} = \frac1{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$

Let $A = \begin{pmatrix} -1 & 3 & -1 \\ 3 & -5 & 2 \\ -1 & 2 & -1 \end{pmatrix}$. Determine the matrix $A^{-1}$ (check the final result carefully on your draft).

## Exercise 2 (4,5 points)
Type : décomposition en éléments simples · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/8
Formules : si $\deg N \geqslant \deg D$ : division euclidienne, partie entière ; pôle simple $a$ : $\frac{c}{X - a}$ avec $c = \left[(X - a)F\right](a)$ ; pôle double : $\frac{c_1}{X-a} + \frac{c_2}{(X-a)^2}$ ; facteur irréductible $X^2 + 1$ : $\frac{bX + c}{X^2 + 1}$ ; identifier en évaluant (ex. $X = 0$) ou par limite de $xF(x)$ en $+\infty$

Expand into partial fractions of $\mathbb{R}(X)$ the following rational fractions:
1. $F(X) = \dfrac{X^2 + X + 1}{(X + 1)(X - 1)(X - 3)}$; 2. $G(X) = \dfrac{X^3 - X - 1}{(X + 1)(X + 3)}$; 3. $H(X) = \dfrac{X^2 - X - 1}{(X - 2)(X^2 + 1)}$.

## Exercise 3 (3 points)
Type : matrice d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/5
Formules : colonne $j$ = coordonnées de $f(e_j)$ dans la base d'arrivée ; base canonique de $\mathbb{R}_2[X]$ : $(1, X, X^2)$ ; de $\mathcal{M}_2(\mathbb{R})$ : $E_{11}, E_{12}, E_{21}, E_{22}$ ; taille (dim arrivée) $\times$ (dim départ)

1. Let $f : \mathbb{R}_2[X] \to \mathbb{R}^2$, $f(P(X)) = (P(1), P(2))$. Determine the matrix of $f$ with respect to the canonical bases of $\mathbb{R}_2[X]$ and $\mathbb{R}^2$.
2. Let $u : \mathbb{R}^3 \to \mathcal{M}_2(\mathbb{R}),\ (x, y, z) \mapsto \begin{pmatrix} x + y & y + z \\ x + z & 0 \end{pmatrix}$. Determine the matrix of $u$ with respect to the canonical bases of $\mathbb{R}^3$ and $\mathcal{M}_2(\mathbb{R})$.

## Exercise 4 (3 points)
Type : noyau et image d'un endomorphisme (inclusions) · ECUE : ALM · Niveau : maths-s2-alm/12
Formules : $\mathrm{Ker} f = \{x, f(x) = 0\}$ ; $\mathrm{Im} f = \{f(x)\}$ ; $f(0) = 0$ ; $x \in \mathrm{Ker} f \Rightarrow f^2(x) = f(0) = 0$ ; $f^2(x) = f(f(x)) \in \mathrm{Im} f$ ; double implication par éléments

Let $E$ be a real vector space and $f \in \mathcal{L}(E)$, $f^2 = f \circ f$.
1. Show that $\mathrm{Ker}(f) \subset \mathrm{Ker}(f^2)$. 2. Show that $\mathrm{Im}(f^2) \subset \mathrm{Im}(f)$. 3. Show that $\mathrm{Im}(f) \cap \mathrm{Ker}(f) = \{0\} \iff \mathrm{Ker}(f) = \mathrm{Ker}(f^2)$.

## Exercise 5 (2 points)
Type : familles libres, génératrices, bases · ECUE : EV · Niveau : maths-s2-ev/6
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \forall i, \lambda_i = 0$ ; génératrice : tout vecteur est combinaison linéaire ; base = libre + génératrice ; $\dim \mathbb{R}_n[X] = n + 1$ ; en dimension $n$ : plus de $n$ vecteurs $\Rightarrow$ liée, moins de $n$ $\Rightarrow$ non génératrice, $n$ vecteurs libres $\Rightarrow$ base ; degrés échelonnés $\Rightarrow$ libre

In $\mathbb{R}_2[X]$ (justify your answers):
1. Does $\mathcal{B}_1 = \{X^2 + X ; X + 3\}$ span $\mathbb{R}_2[X]$? 2. Is $\mathcal{B}_2 = \{2 ; X + 1 ; 2X^2 ; X^2 + 3\}$ linearly independent? 3. Is $\mathcal{B}_3 = \{1 ; X + 1 ; X^2 + 2X\}$ a basis of $\mathbb{R}_2[X]$?

## Exercise 6 (3 points)
Type : puissance d'une matrice (binôme, nilpotente) · ECUE : ALM · Niveau : maths-s2-alm/12
Formules : $J$ nilpotente : $J^3 = 0$ ; si $AB = BA$ : $(A + B)^n = \sum_k \binom nk A^kB^{n-k}$ ; $I$ commute avec tout ; $(I + N)^n = I + nN + \binom n2 N^2$ si $N^3 = 0$

Let $a, b \in \mathbb{R}$, $A = \begin{pmatrix} 1 & a & b \\ 0 & 1 & a \\ 0 & 0 & 1 \end{pmatrix}$, $J = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$.
1. Compute $J^2$ then $J^k$ for $k \geqslant 3$. 2. Express $A$ in terms of $I$, $J$ and $J^2$. 3. Deduce $A^n$ for every non-zero natural number $n$.

## Exercise 7 (4 points)
Type : noyau, image, rang d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/3
Formules : linéaire : $f(\lambda u + v) = \lambda f(u) + f(v)$ ; $\mathrm{Ker} f$ : résoudre $f(x) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \mathrm{rg} f$ ; $\mathrm{rg} f = \dim F \Rightarrow \mathrm{Im} f = F$ (surjective) ; $\mathrm{Im} f = \mathrm{Vect}(f(e_1), \dots, f(e_n))$

Let $f : \mathbb{R}^4 \to \mathbb{R}^3,\ (x, y, z, t) \mapsto (x + y, 2x + y + z, x + t)$.
1. Show that $f$ is linear. 2. Determine $\mathrm{Ker}(f)$ and its dimension. 3. Deduce $\mathrm{Im}(f)$.
