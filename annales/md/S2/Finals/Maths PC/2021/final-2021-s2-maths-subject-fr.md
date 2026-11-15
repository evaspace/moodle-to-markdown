# Partiel 2 (S2) — juin 2017 (sujet, FR)

- Source : `raw/S2/Finals/Maths PC/2021/final-2021-s2-maths-subject-fr.pdf` (scan, 10 pages)
- Date réelle : juin 2017 (S2 16/17, dossier promo 2021). Pas de corrigé.
- Barème : 21,5 points.

## Exercice 1 (2 points)
Type : inverse d'une matrice · ECUE : ALM · Niveau : maths-s2-alm/8
Formules : $A$ inversible $\iff \det A \neq 0$ ; pivot de Gauss sur $(A \mid I_n) \to (I_n \mid A^{-1})$ ; ou $A^{-1} = \frac1{\det A}{}^t\mathrm{Com}(A)$ ; vérifier $AA^{-1} = I_n$ ; $2 \times 2$ : $\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1} = \frac1{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$

Soit $A = \begin{pmatrix} -1 & 3 & -1 \\ 3 & -5 & 2 \\ -1 & 2 & -1 \end{pmatrix}$. Déterminer la matrice $A^{-1}$ en prenant soin de vérifier (au brouillon) le résultat final.

## Exercice 2 (4,5 points)
Type : décomposition en éléments simples · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/8
Formules : si $\deg N \geqslant \deg D$ : division euclidienne, partie entière ; pôle simple $a$ : $\frac{c}{X - a}$ avec $c = \left[(X - a)F\right](a)$ ; pôle double : $\frac{c_1}{X-a} + \frac{c_2}{(X-a)^2}$ ; facteur irréductible $X^2 + 1$ : $\frac{bX + c}{X^2 + 1}$ ; identifier en évaluant (ex. $X = 0$) ou par limite de $xF(x)$ en $+\infty$

Décomposer en éléments simples dans $\mathbb{R}(X)$ les fractions rationnelles suivantes :
1. $F(X) = \dfrac{X^2 + X + 1}{(X + 1)(X - 1)(X - 3)}$ ;
2. $G(X) = \dfrac{X^3 - X - 1}{(X + 1)(X + 3)}$ ;
3. $H(X) = \dfrac{X^2 - X - 1}{(X - 2)(X^2 + 1)}$.

## Exercice 3 (3 points)
Type : matrice d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/5
Formules : colonne $j$ = coordonnées de $f(e_j)$ dans la base d'arrivée ; base canonique de $\mathbb{R}_2[X]$ : $(1, X, X^2)$ ; de $\mathcal{M}_2(\mathbb{R})$ : $E_{11}, E_{12}, E_{21}, E_{22}$ ; taille (dim arrivée) $\times$ (dim départ)

1. Soit $f : \mathbb{R}_2[X] \to \mathbb{R}^2$ définie pour tout $P \in \mathbb{R}_2[X]$ par $f(P(X)) = (P(1), P(2))$. Déterminer la matrice de $f$ relativement aux bases canoniques de $\mathbb{R}_2[X]$ et $\mathbb{R}^2$.
2. Soit $u : \mathbb{R}^3 \to \mathcal{M}_2(\mathbb{R}),\ (x, y, z) \mapsto \begin{pmatrix} x + y & y + z \\ x + z & 0 \end{pmatrix}$. Déterminer la matrice de $u$ relativement aux bases canoniques de $\mathbb{R}^3$ et $\mathcal{M}_2(\mathbb{R})$.

## Exercice 4 (3 points)
Type : noyau et image d'un endomorphisme (inclusions) · ECUE : ALM · Niveau : maths-s2-alm/12
Formules : $\mathrm{Ker} f = \{x, f(x) = 0\}$ ; $\mathrm{Im} f = \{f(x)\}$ ; $f(0) = 0$ ; $x \in \mathrm{Ker} f \Rightarrow f^2(x) = f(0) = 0$ ; $f^2(x) = f(f(x)) \in \mathrm{Im} f$ ; double implication par éléments

Soient $E$ un $\mathbb{R}$-ev et $f \in \mathcal{L}(E)$. On note comme d'habitude $f^2 = f \circ f$.
1. Montrer que $\mathrm{Ker}(f) \subset \mathrm{Ker}(f^2)$.
2. Montrer que $\mathrm{Im}(f^2) \subset \mathrm{Im}(f)$.
3. Montrer que : $\mathrm{Im}(f) \cap \mathrm{Ker}(f) = \{0\} \iff \mathrm{Ker}(f) = \mathrm{Ker}(f^2)$.

## Exercice 5 (2 points)
Type : familles libres, génératrices, bases · ECUE : EV · Niveau : maths-s2-ev/6
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \forall i, \lambda_i = 0$ ; génératrice : tout vecteur est combinaison linéaire ; base = libre + génératrice ; $\dim \mathbb{R}_n[X] = n + 1$ ; en dimension $n$ : plus de $n$ vecteurs $\Rightarrow$ liée, moins de $n$ $\Rightarrow$ non génératrice, $n$ vecteurs libres $\Rightarrow$ base ; degrés échelonnés $\Rightarrow$ libre

On se place dans $\mathbb{R}_2[X]$. Dans les trois questions suivantes, vos réponses doivent être justifiées.
1. $\mathcal{B}_1 = \{X^2 + X ; X + 3\}$ engendre-t-elle $\mathbb{R}_2[X]$ ?
2. $\mathcal{B}_2 = \{2 ; X + 1 ; 2X^2 ; X^2 + 3\}$ est-elle une famille libre de $\mathbb{R}_2[X]$ ?
3. $\mathcal{B}_3 = \{1 ; X + 1 ; X^2 + 2X\}$ est-elle une base de $\mathbb{R}_2[X]$ ?

## Exercice 6 (3 points)
Type : puissance d'une matrice (binôme, nilpotente) · ECUE : ALM · Niveau : maths-s2-alm/12
Formules : $J$ nilpotente : $J^3 = 0$ ; si $AB = BA$ : $(A + B)^n = \sum_k \binom nk A^kB^{n-k}$ ; $I$ commute avec tout ; $(I + N)^n = I + nN + \binom n2 N^2$ si $N^3 = 0$

Soient $a$ et $b$ deux réels, $A = \begin{pmatrix} 1 & a & b \\ 0 & 1 & a \\ 0 & 0 & 1 \end{pmatrix}$ et $J = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$.
1. Calculer $J^2$ puis $J^k$ pour $k \geqslant 3$.
2. Exprimer $A$ en fonction de $I$, $J$ et $J^2$ où $I = I_3$.
3. En déduire $A^n$ pour tout entier naturel $n$ non nul.

## Exercice 7 (4 points)
Type : noyau, image, rang d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/3
Formules : linéaire : $f(\lambda u + v) = \lambda f(u) + f(v)$ ; $\mathrm{Ker} f$ : résoudre $f(x) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \mathrm{rg} f$ ; $\mathrm{rg} f = \dim F \Rightarrow \mathrm{Im} f = F$ (surjective) ; $\mathrm{Im} f = \mathrm{Vect}(f(e_1), \dots, f(e_n))$

Soit $f : \mathbb{R}^4 \to \mathbb{R}^3,\ (x, y, z, t) \mapsto (x + y, 2x + y + z, x + t)$.
1. Montrer que $f$ est linéaire.
2. Déterminer $\mathrm{Ker}(f)$ et donner sa dimension.
3. En déduire $\mathrm{Im}(f)$.
