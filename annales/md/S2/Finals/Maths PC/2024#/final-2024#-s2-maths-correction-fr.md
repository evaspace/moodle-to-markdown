# Correction du partiel Sup S2# — janvier 2020

- Source : `raw/S2/Finals/Maths PC/2024#/final-2024#-s2-maths-correction-fr.pdf` (2 pages)
- Date réelle : janvier 2020 (Sup S2#, dossier promo 2024#). Sujet : `final-2024#-s2-maths-subject-fr.md`.

## Exercice 1
Type : inverse d'une matrice · ECUE : ALM · Niveau : maths-s2-alm/8
Formules : $A$ inversible $\iff \det A \neq 0$ ; pivot de Gauss sur $(A \mid I_n) \to (I_n \mid A^{-1})$ ; ou $A^{-1} = \frac1{\det A}{}^t\mathrm{Com}(A)$ ; vérifier $AA^{-1} = I_n$ ; $2 \times 2$ : $\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1} = \frac1{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$

$AU = V \iff \begin{cases} x + y - z = X \\ -3x - 3y + 4z = Y \\ 3x + 2y - 3z = Z \end{cases}$ ; avec $L_2 \leftarrow L_2 + 3L_1$, $L_3 \leftarrow L_3 - 3L_1$ : $\begin{cases} x + y - z = X \\ z = Y + 3X \\ -y = Z - 3X \end{cases} \iff \begin{cases} x = X + Y + Z \\ y = 3X - Z \\ z = 3X + Y \end{cases}$.
$A^{-1} = \begin{pmatrix} 1 & 1 & 1 \\ 3 & 0 & -1 \\ 3 & 1 & 0 \end{pmatrix}$.

## Exercice 2
Type : familles libres, génératrices, bases · ECUE : EV · Niveau : maths-s2-ev/6
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \forall i, \lambda_i = 0$ ; génératrice : tout vecteur est combinaison linéaire ; base = libre + génératrice ; $\dim \mathbb{R}_n[X] = n + 1$ ; en dimension $n$ : plus de $n$ vecteurs $\Rightarrow$ liée, moins de $n$ $\Rightarrow$ non génératrice, $n$ vecteurs libres $\Rightarrow$ base ; degrés échelonnés $\Rightarrow$ libre

$\dim \mathbb{R}_2[X] = 3$.
1. $\mathrm{Card}(\mathcal{B}_1) = 2 < 3$ : $\mathcal{B}_1$ n'engendre pas $\mathbb{R}_2[X]$.
2. $\mathrm{Card}(\mathcal{B}_2) = 4 > 3$ : $\mathcal{B}_2$ n'est pas libre.
3. $\alpha \cdot 1 + \beta(X + 1) + \gamma(X^2 + 2X) = 0 \iff \gamma X^2 + (\beta + 2\gamma)X + \alpha + \beta = 0$, donc $\alpha = \beta = \gamma = 0$ : libre, et $\mathrm{Card} = 3 = \dim$ : c'est une base.

## Exercice 3
Type : noyau, image, injectivité, surjectivité (cours) · ECUE : ALM · Niveau : maths-s2-alm/2
Formules : sous-espace : contient 0 et stable par $\alpha u + v$ ; $f(\alpha u + v) = \alpha f(u) + f(v)$ ; injective $\iff \mathrm{Ker} f = \{0\}$ ; surjective $\iff \mathrm{Im} f = F$

1. $\mathrm{Ker}(f) \subset E$ et $0 \in \mathrm{Ker}(f)$ ; si $u, v \in \mathrm{Ker}(f)$, $f(\alpha u + v) = \alpha f(u) + f(v) = 0$ : sous-espace vectoriel de $E$. $\mathrm{Im}(f) \subset F$, $0 = f(0) \in \mathrm{Im}(f)$ ; si $u = f(u_1)$, $v = f(v_1)$, $\alpha u + v = f(\alpha u_1 + v_1) \in \mathrm{Im}(f)$.
2. Si $f$ injective et $u \in \mathrm{Ker}(f)$ : $f(u) = 0 = f(0)$ donc $u = 0$. Si $\mathrm{Ker}(f) = \{0\}$ et $f(u) = f(v)$ : $f(u - v) = 0$, $u = v$.
3. $\mathrm{Im}(f) = F \iff \forall v \in F, \exists u \in E, v = f(u) \iff f$ surjective.

## Exercice 4
Type : noyau, image, rang d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/3
Formules : linéaire : $f(\lambda u + v) = \lambda f(u) + f(v)$ ; $\mathrm{Ker} f$ : résoudre $f(x) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \mathrm{rg} f$ ; $\mathrm{rg} f = \dim F \Rightarrow \mathrm{Im} f = F$ (surjective) ; $\mathrm{Im} f = \mathrm{Vect}(f(e_1), \dots, f(e_n))$

1. $f(\alpha u + v) = \alpha f(u) + f(v)$ par calcul direct sur les coordonnées.
2. $\mathrm{Ker}(f) = \{(x, y, z), x + y - z = 0, x - y - 3z = 0\} = \{(x, y, z), x = 2z, y = -z\} = \mathrm{Vect}((2, -1, 1))$ ; $u = (2, -1, 1) \neq 0$ est une base de $\mathrm{Ker}(f)$.
3. Théorème du rang : $\dim \mathrm{Im}(f) = 3 - 1 = 2 = \dim \mathbb{R}^2$ et $\mathrm{Im}(f) \subset \mathbb{R}^2$, donc $\mathrm{Im}(f) = \mathbb{R}^2$.

## Exercice 5
Type : familles libres, génératrices, bases · ECUE : EV · Niveau : maths-s2-ev/6
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \forall i, \lambda_i = 0$ ; génératrice : tout vecteur est combinaison linéaire ; base = libre + génératrice ; $\dim \mathbb{R}_n[X] = n + 1$ ; en dimension $n$ : plus de $n$ vecteurs $\Rightarrow$ liée, moins de $n$ $\Rightarrow$ non génératrice, $n$ vecteurs libres $\Rightarrow$ base ; degrés échelonnés $\Rightarrow$ libre

1. $2(1, -2, 3) - 3(-1, -2, 1) - (5, 2, 3) = (0, 0, 0)$ (coquille $(1, -1, 3)$ dans le corrigé) : la famille est liée.
2. $af + bg + ch = 0$ : $x = 0$ donne $c = 0$ ; $x = 1$ et $x = -1$ donnent $a + b = 0$ et $-a + b = 0$, d'où $a = b = 0$ : libre.
3. $aA + bB = 0$ : $a + 6b = 0$, $a - 2b = 0$, $-3a + b = 0$, $4a + 4b = 0$, d'où $a = b = 0$ : libre.

## Exercice 6
Type : changement de base, diagonalisation, puissance d'une matrice · ECUE : ALM · Niveau : maths-s2-alm/9
Formules : $\mathrm{Mat}_{\mathcal{B}'}(f) = P^{-1}AP$ avec $P = \mathrm{Mat}_{\mathcal{B}', \mathcal{B}}(id)$ (colonnes = vecteurs de $\mathcal{B}'$ dans $\mathcal{B}$) ; $f(u_i) = \lambda_iu_i \Rightarrow D = \mathrm{diag}(\lambda_i)$ ; $D^n = \mathrm{diag}(\lambda_i^n)$ ; $A = PDP^{-1} \Rightarrow A^n = PD^nP^{-1}$

$\mathcal{B}_1 = (i, j)$, $\mathcal{B}_2 = ((1, 1), (-1, 0)) = (e_1, e_2)$.
1. $A = \begin{pmatrix} 3 & -5 \\ 0 & -2 \end{pmatrix}$. 2. $D = \begin{pmatrix} -2 & 0 \\ 0 & 3 \end{pmatrix}$ ($f(e_1) = -2e_1$, $f(e_2) = 3e_2$).
3. $id(e_1) = (1, 1) = i + j$ et $id(e_2) = (-1, 0) = -i$ : colonnes de $P$.
4. $P^{-1} = \begin{pmatrix} 0 & 1 \\ -1 & 1 \end{pmatrix}$ et $P^{-1}AP = D$.

## Exercice 7
Type : calcul matriciel, transposée · ECUE : ALM · Niveau : maths-s2-alm/6
Formules : $({}^tA)_{i,j} = a_{j,i}$ ; ${}^t(AB) = {}^tB\,{}^tA$ ; ${}^tUU = \sum x_i^2$ (scalaire) ; $U\,{}^tU$ matrice $n \times n$ ; associativité $(AB)C = A(BC)$ ; produit $(AB)_{ij} = \sum_k a_{ik}b_{kj}$

1. ${}^tUU = x^2 + y^2 + z^2 = 1$. Ainsi $P^2 = U({}^tUU){}^tU = U\,{}^tU = P$.
2. $P = \begin{pmatrix} x^2 & xy & xz \\ xy & y^2 & yz \\ xz & yz & z^2 \end{pmatrix}$ ; on vérifie par le calcul que $MP = PM = 0$ (par exemple $MU = 0$).
