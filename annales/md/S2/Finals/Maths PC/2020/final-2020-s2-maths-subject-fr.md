# Partiel 2 de mathématiques S2 — juin 2016 (sujet, FR)

- Source : `raw/S2/Finals/Phys/2020/final-2020-s2-phys-subject-fr.pdf`, pages 15 à 22 (le PDF de 56 pages regroupe toute la session de juin 2016 ; la version anglaise du sujet est aux pages 23 à 30, non transcrite). Pas de corrigé officiel.
- Date réelle : juin 2016 (EPITA Info-Sup 15/16, dossier promo 2020). Corrigé : `final-2020-s2-maths-correction-fr.md`.
- Durée : trois heures. Documents et calculatrices non autorisés.

## Exercice 1 (3 points)
Type : inverse d'une matrice · ECUE : ALM · Niveau : maths-s2-alm/8
Formules : $A$ inversible $\iff \det A \neq 0$ ; pivot de Gauss sur $(A \mid I_n) \to (I_n \mid A^{-1})$ ; ou $A^{-1} = \frac1{\det A}{}^t\mathrm{Com}(A)$ ; vérifier $AA^{-1} = I_n$ ; $2 \times 2$ : $\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1} = \frac1{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$

Soit $A = \begin{pmatrix}1&1&-2\\1&-1&1\\-2&1&-1\end{pmatrix}$. Déterminer la matrice $A^{-1}$ en prenant soin de vérifier (au brouillon) le résultat final.

## Exercice 2 (4,5 points)
Type : décomposition en éléments simples · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/8
Formules : si $\deg N \geqslant \deg D$ : division euclidienne, partie entière ; pôle simple $a$ : $\frac{c}{X - a}$ avec $c = \left[(X - a)F\right](a)$ ; pôle double : $\frac{c_1}{X-a} + \frac{c_2}{(X-a)^2}$ ; facteur irréductible $X^2 + 1$ : $\frac{bX + c}{X^2 + 1}$ ; identifier en évaluant (ex. $X = 0$) ou par limite de $xF(x)$ en $+\infty$

Décomposer en éléments simples dans $\mathbb{R}(X)$ les fractions rationnelles suivantes :
1. $F(X) = \dfrac{X + 1}{(X - 1)(X + 2)(X + 3)}$
2. $G(X) = \dfrac{X^3 + X^2 + 1}{(X - 1)(X + 2)}$
3. $H(X) = \dfrac{X^2 - X + 2}{(X - 1)(X^2 + 1)}$

## Exercice 3 (4 points)
Type : matrice d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/5
Formules : colonne $j$ = coordonnées de $f(e_j)$ dans la base d'arrivée ; base canonique de $\mathbb{R}_2[X]$ : $(1, X, X^2)$ ; de $\mathcal{M}_2(\mathbb{R})$ : $E_{11}, E_{12}, E_{21}, E_{22}$ ; taille (dim arrivée) $\times$ (dim départ)

Soient $E = \mathbb{R}_2[X]$ et $f : E \to E$ définie pour tout $P \in E$ par $f(P) = 2(X + 1)P - (X^2 + 1)P'$. Soient $\mathcal{B} = (1, X, X^2)$ et $\mathcal{B}' = (1, X - 1, (X + 1)^2)$ deux bases de $E$.
1. Déterminer $\mathrm{Mat}_{\mathcal{B}}(f)$, matrice de $f$ relativement à la base $\mathcal{B}$.
2. Déterminer $\mathrm{Mat}_{\mathcal{B}'}(f)$, matrice de $f$ relativement à la base $\mathcal{B}'$.
3. Déterminer $\mathrm{Mat}_{\mathcal{B},\mathcal{B}'}(f)$, matrice de $f$ relativement aux bases $\mathcal{B}$, $\mathcal{B}'$.
4. Déterminer $\mathrm{Mat}_{\mathcal{B}',\mathcal{B}}(f)$, matrice de $f$ relativement aux bases $\mathcal{B}'$, $\mathcal{B}$.

## Exercice 4 (4 points)
Type : puissance d'une matrice par polynôme annulateur · ECUE : ALM · Niveau : maths-s2-alm/12
Formules : $J^2 - J - 2I = 0 \Rightarrow J(J - I) = 2I$, donc $J^{-1} = \frac12(J - I)$ ; $JK = I \Rightarrow J^{-1} = K$ ; division euclidienne $X^n = (X^2 - X - 2)Q + aX + b$ ; évaluer en $2$ et $-1$ (racines) : $2^n = 2a + b$, $(-1)^n = -a + b$ ; substituer $J$ : $J^n = aJ + bI$

On note $I$ la matrice identité d'ordre 3. Soit $J = \begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix}$.
1. Vérifier que $J^2 - J - 2I = 0$. En déduire $J^{-1}$ en fonction de $I$ et $J$. N.B. : on rappelle que s'il existe $K \in \mathcal{M}_3(\mathbb{R})$ tel que $JK = I$ alors $J$ est inversible et $J^{-1} = K$.
2. Soit $n \in \mathbb{N}$. On effectue la division euclidienne de $X^n$ par $X^2 - X - 2$. Il existe donc $Q(X) \in \mathbb{R}[X]$ et $R(X) \in \mathbb{R}[X]$ tels que $X^n = (X^2 - X - 2)Q(X) + R(X)$ avec le degré de $R$ strictement inférieur à 2. Ainsi il existe $(a, b) \in \mathbb{R}^2$ tel que $X^n = (X^2 - X - 2)Q(X) + aX + b$. En remarquant que $2$ et $-1$ sont racines de $X^2 - X - 2$, déterminer $a$ et $b$.
3. Soit $n \in \mathbb{N}$. En déduire $J^n$ en fonction de $n$, $I$ et $J$. N.B. : on substituera $J$ à l'indéterminée $X$ de la question 2 (sachant que le polynôme 1 devient $I$). Par exemple, $X^4 + 2X^3 + 4$ devient après substitution $J^4 + 2J^3 + 4I$.

## Exercice 5 (5,5 points)
Type : endomorphisme de dérivation : base, matrice, puissance · ECUE : ALM · Niveau : maths-s2-alm/5
Formules : famille libre : $\sum \lambda_if_i = 0 \Rightarrow \lambda_i = 0$ (diviser par $e^{2x}$, polynôme nul) ; $d$ linéaire et $d(F) \subset F$ ; colonne $j$ = coordonnées de $d(f_j)$ ; $(e^{2x})^{(n)} = 2^ne^{2x}$ ; Leibniz $(uv)^{(n)} = \sum_k C_n^ku^{(k)}v^{(n-k)}$ ; $\mathrm{Mat}(d^n) = A^n$

Soit $E = C^\infty(\mathbb{R}, \mathbb{R})$ l'ensemble des fonctions de $\mathbb{R}$ dans $\mathbb{R}$ indéfiniment dérivables sur $\mathbb{R}$. Notons $f_0$, $f_1$ et $f_2$ les vecteurs de $E$ définis pour tout $x \in \mathbb{R}$ par $f_0(x) = e^{2x}$, $f_1(x) = xe^{2x}$ et $f_2(x) = x^2e^{2x}$. Notons $F = \mathrm{Vect}(f_0, f_1, f_2)$, c'est-à-dire le sous-espace vectoriel de $E$ engendré par $f_0$, $f_1$ et $f_2$.
1. Montrer que $B = (f_0, f_1, f_2)$ est une base de $F$.
2. Soit l'application $d$ définie pour tout $f \in F$ par $d(f) = f'$. Montrer que $d$ est un endomorphisme de $F$.
3. Déterminer $A$ la matrice de $d$ dans $B$.
4. Soit $n \in \mathbb{N}^*$. Calculer $d^n(f_0)$, $d^n(f_1)$ et $d^n(f_2)$ où pour tout $p \in \mathbb{N}^*$, $d^p = d \circ \dots \circ d$ ($p$ fois). N.B. : on pourra utiliser la formule $(uv)^{(n)} = \sum_{k=0}^n C_n^ku^{(k)}v^{(n-k)}$, avec la convention $u^{(0)} = u$ et où $C_n^k = \dfrac{n(n-1)\dots(n-k+1)}{k!}$.
5. En déduire $A^n$ en fonction de $n$ pour tout $n \in \mathbb{N}^*$.
