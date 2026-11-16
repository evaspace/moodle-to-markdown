# Partiel 2 de mathématiques S2 — juin 2016 (corrigé rédigé, FR)

- Source : `raw/S2/Finals/Phys/2020/final-2020-s2-phys-subject-fr.pdf`, pages 15 à 22 (le PDF de 56 pages regroupe toute la session de juin 2016 ; la version anglaise du sujet est aux pages 23 à 30, non transcrite). Pas de corrigé officiel : corrigé rédigé pour cette application, calculs vérifiés avec sympy.
- Date réelle : juin 2016 (EPITA Info-Sup 15/16, dossier promo 2020). Sujet : `final-2020-s2-maths-subject-fr.md`.
- Durée : trois heures. Documents et calculatrices non autorisés. Les lignes `> ` sont les solutions.

## Exercice 1 (3 points)
Type : inverse d'une matrice · ECUE : ALM · Niveau : maths-s2-alm/8
Formules : $A$ inversible $\iff \det A \neq 0$ ; pivot de Gauss sur $(A \mid I_n) \to (I_n \mid A^{-1})$ ; ou $A^{-1} = \frac1{\det A}{}^t\mathrm{Com}(A)$ ; vérifier $AA^{-1} = I_n$ ; $2 \times 2$ : $\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1} = \frac1{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$

Soit $A = \begin{pmatrix}1&1&-2\\1&-1&1\\-2&1&-1\end{pmatrix}$. Déterminer la matrice $A^{-1}$ en prenant soin de vérifier (au brouillon) le résultat final.
> $\det A = 1(1 - 1) - 1(-1 + 2) - 2(1 - 2) = 0 - 1 + 2 = 1 \neq 0$ : $A$ est inversible. Par le pivot de Gauss (ou les cofacteurs) : $A^{-1} = \begin{pmatrix}0&-1&-1\\-1&-5&-3\\-1&-3&-2\end{pmatrix}$.
> Vérification, première ligne de $A$ : $0 - 1 + 2 = 1$, $-1 - 5 + 6 = 0$, $-1 - 3 + 4 = 0$.

## Exercice 2 (4,5 points)
Type : décomposition en éléments simples · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/8
Formules : si $\deg N \geqslant \deg D$ : division euclidienne, partie entière ; pôle simple $a$ : $\frac{c}{X - a}$ avec $c = \left[(X - a)F\right](a)$ ; pôle double : $\frac{c_1}{X-a} + \frac{c_2}{(X-a)^2}$ ; facteur irréductible $X^2 + 1$ : $\frac{bX + c}{X^2 + 1}$ ; identifier en évaluant (ex. $X = 0$) ou par limite de $xF(x)$ en $+\infty$

Décomposer en éléments simples dans $\mathbb{R}(X)$ les fractions rationnelles suivantes :
1. $F(X) = \dfrac{X + 1}{(X - 1)(X + 2)(X + 3)}$
> Pôles simples. $F = \dfrac{a}{X - 1} + \dfrac{b}{X + 2} + \dfrac{c}{X + 3}$ avec $a = \dfrac{2}{3 \times 4} = \dfrac16$, $b = \dfrac{-1}{(-3)(1)} = \dfrac13$, $c = \dfrac{-2}{(-4)(-1)} = -\dfrac12$.
> $F(X) = \dfrac{1}{6(X - 1)} + \dfrac{1}{3(X + 2)} - \dfrac{1}{2(X + 3)}$.
2. $G(X) = \dfrac{X^3 + X^2 + 1}{(X - 1)(X + 2)}$
> $\deg N = 3 \geqslant 2$ : division de $X^3 + X^2 + 1$ par $X^2 + X - 2$ : quotient $X$, reste $2X + 1$. Puis $\dfrac{2X + 1}{(X - 1)(X + 2)} = \dfrac{a}{X - 1} + \dfrac{b}{X + 2}$ avec $a = \dfrac33 = 1$, $b = \dfrac{-3}{-3} = 1$.
> $G(X) = X + \dfrac{1}{X - 1} + \dfrac{1}{X + 2}$.
3. $H(X) = \dfrac{X^2 - X + 2}{(X - 1)(X^2 + 1)}$
> $H = \dfrac{a}{X - 1} + \dfrac{bX + c}{X^2 + 1}$. $a = \dfrac{1 - 1 + 2}{2} = 1$. Limite de $xH(x)$ en $+\infty$ : $1 = a + b$, donc $b = 0$. En $X = 0$ : $-2 = -a + c$, donc $c = -1$.
> $H(X) = \dfrac{1}{X - 1} - \dfrac{1}{X^2 + 1}$.

## Exercice 3 (4 points)
Type : matrice d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/5
Formules : colonne $j$ = coordonnées de $f(e_j)$ dans la base d'arrivée ; base canonique de $\mathbb{R}_2[X]$ : $(1, X, X^2)$ ; de $\mathcal{M}_2(\mathbb{R})$ : $E_{11}, E_{12}, E_{21}, E_{22}$ ; taille (dim arrivée) $\times$ (dim départ)

Soient $E = \mathbb{R}_2[X]$ et $f : E \to E$ définie pour tout $P \in E$ par $f(P) = 2(X + 1)P - (X^2 + 1)P'$. Soient $\mathcal{B} = (1, X, X^2)$ et $\mathcal{B}' = (1, X - 1, (X + 1)^2)$ deux bases de $E$.
1. Déterminer $\mathrm{Mat}_{\mathcal{B}}(f)$, matrice de $f$ relativement à la base $\mathcal{B}$.
> $f(1) = 2X + 2$, $f(X) = 2X^2 + 2X - X^2 - 1 = X^2 + 2X - 1$, $f(X^2) = 2X^3 + 2X^2 - 2X^3 - 2X = 2X^2 - 2X$.
> $\mathrm{Mat}_{\mathcal{B}}(f) = \begin{pmatrix}2&-1&0\\2&2&-2\\0&1&2\end{pmatrix}$.
2. Déterminer $\mathrm{Mat}_{\mathcal{B}'}(f)$, matrice de $f$ relativement à la base $\mathcal{B}'$.
> $f(1) = 2X + 2 = 4 \cdot 1 + 2(X - 1)$ ; $f(X - 1) = f(X) - f(1) = X^2 - 3 = -6 \cdot 1 - 2(X - 1) + (X + 1)^2$ ; $f((X + 1)^2) = f(X^2) + 2f(X) + f(1) = 4X^2 + 4X = -8 \cdot 1 - 4(X - 1) + 4(X + 1)^2$.
> $\mathrm{Mat}_{\mathcal{B}'}(f) = \begin{pmatrix}4&-6&-8\\2&-2&-4\\0&1&4\end{pmatrix}$.
3. Déterminer $\mathrm{Mat}_{\mathcal{B},\mathcal{B}'}(f)$, matrice de $f$ relativement aux bases $\mathcal{B}$, $\mathcal{B}'$.
> Départ $\mathcal{B}$, arrivée $\mathcal{B}'$ : on écrit $f(1)$, $f(X)$, $f(X^2)$ dans $\mathcal{B}'$. $2X + 2 = 4 + 2(X - 1)$ ; $X^2 + 2X - 1 = -2 + (X + 1)^2$ ; $2X^2 - 2X = -8 - 6(X - 1) + 2(X + 1)^2$.
> $\mathrm{Mat}_{\mathcal{B},\mathcal{B}'}(f) = \begin{pmatrix}4&-2&-8\\2&0&-6\\0&1&2\end{pmatrix}$.
4. Déterminer $\mathrm{Mat}_{\mathcal{B}',\mathcal{B}}(f)$, matrice de $f$ relativement aux bases $\mathcal{B}'$, $\mathcal{B}$.
> Départ $\mathcal{B}'$, arrivée $\mathcal{B}$ : $f(1) = 2 + 2X$, $f(X - 1) = -3 + X^2$, $f((X + 1)^2) = 4X + 4X^2$.
> $\mathrm{Mat}_{\mathcal{B}',\mathcal{B}}(f) = \begin{pmatrix}2&-3&0\\2&0&4\\0&1&4\end{pmatrix}$.

## Exercice 4 (4 points)
Type : puissance d'une matrice par polynôme annulateur · ECUE : ALM · Niveau : maths-s2-alm/12
Formules : $J^2 - J - 2I = 0 \Rightarrow J(J - I) = 2I$, donc $J^{-1} = \frac12(J - I)$ ; $JK = I \Rightarrow J^{-1} = K$ ; division euclidienne $X^n = (X^2 - X - 2)Q + aX + b$ ; évaluer en $2$ et $-1$ (racines) : $2^n = 2a + b$, $(-1)^n = -a + b$ ; substituer $J$ : $J^n = aJ + bI$

On note $I$ la matrice identité d'ordre 3. Soit $J = \begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix}$.
1. Vérifier que $J^2 - J - 2I = 0$. En déduire $J^{-1}$ en fonction de $I$ et $J$. N.B. : on rappelle que s'il existe $K \in \mathcal{M}_3(\mathbb{R})$ tel que $JK = I$ alors $J$ est inversible et $J^{-1} = K$.
> $J^2 = \begin{pmatrix}2&1&1\\1&2&1\\1&1&2\end{pmatrix} = J + 2I$, donc $J^2 - J - 2I = 0$.
> Alors $J(J - I) = 2I$, soit $J \cdot \dfrac12(J - I) = I$ : $J$ est inversible et $J^{-1} = \dfrac12(J - I)$.
2. Soit $n \in \mathbb{N}$. On effectue la division euclidienne de $X^n$ par $X^2 - X - 2$. Il existe donc $Q(X) \in \mathbb{R}[X]$ et $R(X) \in \mathbb{R}[X]$ tels que $X^n = (X^2 - X - 2)Q(X) + R(X)$ avec le degré de $R$ strictement inférieur à 2. Ainsi il existe $(a, b) \in \mathbb{R}^2$ tel que $X^n = (X^2 - X - 2)Q(X) + aX + b$. En remarquant que $2$ et $-1$ sont racines de $X^2 - X - 2$, déterminer $a$ et $b$.
> En $X = 2$ : $2^n = 2a + b$. En $X = -1$ : $(-1)^n = -a + b$. Par différence, $3a = 2^n - (-1)^n$.
> $a = \dfrac{2^n - (-1)^n}{3}$ et $b = (-1)^n + a = \dfrac{2^n + 2(-1)^n}{3}$.
3. Soit $n \in \mathbb{N}$. En déduire $J^n$ en fonction de $n$, $I$ et $J$. N.B. : on substituera $J$ à l'indéterminée $X$ de la question 2 (sachant que le polynôme 1 devient $I$). Par exemple, $X^4 + 2X^3 + 4$ devient après substitution $J^4 + 2J^3 + 4I$.
> $J^n = (J^2 - J - 2I)Q(J) + aJ + bI$ et $J^2 - J - 2I = 0$, donc $J^n = \dfrac{2^n - (-1)^n}{3}J + \dfrac{2^n + 2(-1)^n}{3}I$.
> Contrôle : $n = 2$ donne $J + 2I$.

## Exercice 5 (5,5 points)
Type : endomorphisme de dérivation : base, matrice, puissance · ECUE : ALM · Niveau : maths-s2-alm/5
Formules : famille libre : $\sum \lambda_if_i = 0 \Rightarrow \lambda_i = 0$ (diviser par $e^{2x}$, polynôme nul) ; $d$ linéaire et $d(F) \subset F$ ; colonne $j$ = coordonnées de $d(f_j)$ ; $(e^{2x})^{(n)} = 2^ne^{2x}$ ; Leibniz $(uv)^{(n)} = \sum_k C_n^ku^{(k)}v^{(n-k)}$ ; $\mathrm{Mat}(d^n) = A^n$

Soit $E = C^\infty(\mathbb{R}, \mathbb{R})$ l'ensemble des fonctions de $\mathbb{R}$ dans $\mathbb{R}$ indéfiniment dérivables sur $\mathbb{R}$. Notons $f_0$, $f_1$ et $f_2$ les vecteurs de $E$ définis pour tout $x \in \mathbb{R}$ par $f_0(x) = e^{2x}$, $f_1(x) = xe^{2x}$ et $f_2(x) = x^2e^{2x}$. Notons $F = \mathrm{Vect}(f_0, f_1, f_2)$, c'est-à-dire le sous-espace vectoriel de $E$ engendré par $f_0$, $f_1$ et $f_2$.
1. Montrer que $B = (f_0, f_1, f_2)$ est une base de $F$.
> $B$ engendre $F$ par définition. Libre : si $\lambda_0f_0 + \lambda_1f_1 + \lambda_2f_2 = 0$, alors pour tout $x$, $(\lambda_0 + \lambda_1x + \lambda_2x^2)e^{2x} = 0$, et $e^{2x} \neq 0$ : le polynôme $\lambda_0 + \lambda_1X + \lambda_2X^2$ a une infinité de racines, il est nul, donc $\lambda_0 = \lambda_1 = \lambda_2 = 0$. $B$ est une base de $F$.
2. Soit l'application $d$ définie pour tout $f \in F$ par $d(f) = f'$. Montrer que $d$ est un endomorphisme de $F$.
> Linéaire : $(\lambda f + \mu g)' = \lambda f' + \mu g'$. Stabilité : $f_0' = 2f_0$, $f_1' = f_0 + 2f_1$, $f_2' = 2f_1 + 2f_2$ sont dans $F$ ; par linéarité, $d(F) \subset F$. Donc $d$ est un endomorphisme de $F$.
3. Déterminer $A$ la matrice de $d$ dans $B$.
> Colonnes $d(f_0)$, $d(f_1)$, $d(f_2)$ : $A = \begin{pmatrix}2&1&0\\0&2&2\\0&0&2\end{pmatrix}$.
4. Soit $n \in \mathbb{N}^*$. Calculer $d^n(f_0)$, $d^n(f_1)$ et $d^n(f_2)$ où pour tout $p \in \mathbb{N}^*$, $d^p = d \circ \dots \circ d$ ($p$ fois). N.B. : on pourra utiliser la formule $(uv)^{(n)} = \sum_{k=0}^n C_n^ku^{(k)}v^{(n-k)}$, avec la convention $u^{(0)} = u$ et où $C_n^k = \dfrac{n(n-1)\dots(n-k+1)}{k!}$.
> $d^n(f_0) = 2^ne^{2x} = 2^nf_0$.
> Leibniz avec $u = x$ (seuls $k = 0, 1$ comptent) : $d^n(f_1) = x2^ne^{2x} + n2^{n-1}e^{2x} = n2^{n-1}f_0 + 2^nf_1$.
> Avec $u = x^2$ ($k = 0, 1, 2$) : $d^n(f_2) = x^22^ne^{2x} + n \cdot 2x \cdot 2^{n-1}e^{2x} + \dfrac{n(n-1)}{2} \cdot 2 \cdot 2^{n-2}e^{2x} = n(n-1)2^{n-2}f_0 + n2^nf_1 + 2^nf_2$.
5. En déduire $A^n$ en fonction de $n$ pour tout $n \in \mathbb{N}^*$.
> $A^n = \mathrm{Mat}_B(d^n)$, colonnes = coordonnées de la question 4 : $A^n = \begin{pmatrix}2^n&n2^{n-1}&n(n-1)2^{n-2}\\0&2^n&n2^n\\0&0&2^n\end{pmatrix}$.
> Contrôle $n = 1$ : on retrouve $A$.
