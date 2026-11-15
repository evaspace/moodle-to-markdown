# Partiel Sup S2# — janvier 2020 (sujet, FR)

- Source : `raw/S2/Finals/Maths PC/2024#/final-2024#-s2-maths-subject-fr.pdf` (2 pages)
- Date réelle : janvier 2020 (Sup S2#, semestre décalé, dossier promo 2024#). Corrigé : `final-2024#-s2-maths-correction-fr.md`.
- Durée : trois heures. Documents et calculatrices non autorisés. Barème : 21 points.

## Exercice 1 (2 points)
Type : inverse d'une matrice · ECUE : ALM · Niveau : maths-s2-alm/8
Formules : $A$ inversible $\iff \det A \neq 0$ ; pivot de Gauss sur $(A \mid I_n) \to (I_n \mid A^{-1})$ ; ou $A^{-1} = \frac1{\det A}{}^t\mathrm{Com}(A)$ ; vérifier $AA^{-1} = I_n$ ; $2 \times 2$ : $\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1} = \frac1{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$

Soit $A = \begin{pmatrix} 1 & 1 & -1 \\ -3 & -3 & 4 \\ 3 & 2 & -3 \end{pmatrix}$. Déterminer la matrice $A^{-1}$ en prenant soin de vérifier (au brouillon) le résultat final.

## Exercice 2 (3 points)
Type : familles libres, génératrices, bases · ECUE : EV · Niveau : maths-s2-ev/6
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \forall i, \lambda_i = 0$ ; génératrice : tout vecteur est combinaison linéaire ; base = libre + génératrice ; $\dim \mathbb{R}_n[X] = n + 1$ ; en dimension $n$ : plus de $n$ vecteurs $\Rightarrow$ liée, moins de $n$ $\Rightarrow$ non génératrice, $n$ vecteurs libres $\Rightarrow$ base ; degrés échelonnés $\Rightarrow$ libre

On se place dans $\mathbb{R}_2[X]$. Dans les trois questions suivantes, vos réponses doivent être justifiées.
1. $\mathcal{B}_1 = (X^2 + X, X + 3)$ engendre-t-elle $\mathbb{R}_2[X]$ ?
2. $\mathcal{B}_2 = (2, X + 1, 2X^2, X^2 + 3)$ est-elle une famille libre de $\mathbb{R}_2[X]$ ?
3. $\mathcal{B}_3 = (1, X + 1, X^2 + 2X)$ est-elle une base de $\mathbb{R}_2[X]$ ?

## Exercice 3 (3 points)
Type : noyau, image, injectivité, surjectivité (cours) · ECUE : ALM · Niveau : maths-s2-alm/2
Formules : sous-espace : contient 0 et stable par $\alpha u + v$ ; $f(\alpha u + v) = \alpha f(u) + f(v)$ ; injective $\iff \mathrm{Ker} f = \{0\}$ ; surjective $\iff \mathrm{Im} f = F$

Soient $E$, $F$ deux $\mathbb{R}$-ev et $f \in \mathcal{L}(E, F)$.
1. Montrer que $\mathrm{Ker}(f)$ et $\mathrm{Im}(f)$ sont des $\mathbb{R}$-ev.
2. Montrer que $f$ est injective si et seulement si $\mathrm{Ker}(f) = \{0\}$.
3. Montrer que $f$ est surjective si et seulement si $\mathrm{Im}(f) = F$.

## Exercice 4 (3 points)
Type : noyau, image, rang d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/3
Formules : linéaire : $f(\lambda u + v) = \lambda f(u) + f(v)$ ; $\mathrm{Ker} f$ : résoudre $f(x) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \mathrm{rg} f$ ; $\mathrm{rg} f = \dim F \Rightarrow \mathrm{Im} f = F$ (surjective) ; $\mathrm{Im} f = \mathrm{Vect}(f(e_1), \dots, f(e_n))$

Soit $f : \mathbb{R}^3 \to \mathbb{R}^2,\ (x, y, z) \mapsto (x + y - z, x - y - 3z)$.
1. Montrer que $f$ est linéaire.
2. Déterminer le noyau de $f$ et exhiber une de ses bases.
3. En déduire, via le théorème du rang, la dimension de l'image de $f$ puis en déduire l'image de $f$.

## Exercice 5 (3 points)
Type : familles libres, génératrices, bases · ECUE : EV · Niveau : maths-s2-ev/6
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \forall i, \lambda_i = 0$ ; génératrice : tout vecteur est combinaison linéaire ; base = libre + génératrice ; $\dim \mathbb{R}_n[X] = n + 1$ ; en dimension $n$ : plus de $n$ vecteurs $\Rightarrow$ liée, moins de $n$ $\Rightarrow$ non génératrice, $n$ vecteurs libres $\Rightarrow$ base ; degrés échelonnés $\Rightarrow$ libre

Les familles suivantes sont-elles libres ? Justifiez votre réponse.
1. Dans $\mathbb{R}^3$ : $((1, -2, 3), (-1, -2, 1), (5, 2, 3))$.
2. Dans $\mathbb{R}^{\mathbb{R}}$ : $(f : x \mapsto x,\ g : x \mapsto x^2,\ h : x \mapsto e^{2x})$.
3. Dans $\mathcal{M}_2(\mathbb{R})$ : $(A, B)$ où $A = \begin{pmatrix} 1 & 1 \\ -3 & 4 \end{pmatrix}$ et $B = \begin{pmatrix} 6 & -2 \\ 1 & 4 \end{pmatrix}$.

## Exercice 6 (4 points)
Type : changement de base, diagonalisation, puissance d'une matrice · ECUE : ALM · Niveau : maths-s2-alm/9
Formules : $\mathrm{Mat}_{\mathcal{B}'}(f) = P^{-1}AP$ avec $P = \mathrm{Mat}_{\mathcal{B}', \mathcal{B}}(id)$ (colonnes = vecteurs de $\mathcal{B}'$ dans $\mathcal{B}$) ; $f(u_i) = \lambda_iu_i \Rightarrow D = \mathrm{diag}(\lambda_i)$ ; $D^n = \mathrm{diag}(\lambda_i^n)$ ; $A = PDP^{-1} \Rightarrow A^n = PD^nP^{-1}$

Soit $f : \mathbb{R}^2 \to \mathbb{R}^2,\ (x, y) \mapsto (3x - 5y, -2y)$. On note $\mathcal{B}_1$ la base canonique de $\mathbb{R}^2$ et $\mathcal{B}_2 = ((1, 1), (-1, 0))$ une autre base de $\mathbb{R}^2$. On note $id$ l'endomorphisme identité de $\mathbb{R}^2$.
1. Déterminer $A = \mathrm{Mat}_{\mathcal{B}_1}(f)$.
2. Déterminer $D = \mathrm{Mat}_{\mathcal{B}_2}(f)$.
3. Expliquer pourquoi $\mathrm{Mat}_{\mathcal{B}_2, \mathcal{B}_1}(id) = \begin{pmatrix} 1 & -1 \\ 1 & 0 \end{pmatrix}$. On note $P$ cette matrice.
4. Inverser $P$ puis calculer $P^{-1}AP$. Que remarquez-vous ?

## Exercice 7 (3 points)
Type : calcul matriciel, transposée · ECUE : ALM · Niveau : maths-s2-alm/6
Formules : $({}^tA)_{i,j} = a_{j,i}$ ; ${}^t(AB) = {}^tB\,{}^tA$ ; ${}^tUU = \sum x_i^2$ (scalaire) ; $U\,{}^tU$ matrice $n \times n$ ; associativité $(AB)C = A(BC)$ ; produit $(AB)_{ij} = \sum_k a_{ik}b_{kj}$

Soit $(x, y, z) \in \mathbb{R}^3$ tel que $x^2 + y^2 + z^2 = 1$. Posons $U = \begin{pmatrix} x \\ y \\ z \end{pmatrix}$, $M = \begin{pmatrix} 0 & z & -y \\ -z & 0 & x \\ y & -x & 0 \end{pmatrix}$ et $P = U\,{}^tU$.
N.B. : soit $A = (a_{i,j}) \in \mathcal{M}_{n,p}(\mathbb{R})$. On appelle transposée de $A$ la matrice ${}^tA = (b_{i,j}) \in \mathcal{M}_{p,n}(\mathbb{R})$ obtenue en échangeant les lignes et les colonnes de $A$ : $b_{i,j} = a_{j,i}$. Par exemple, la transposée de $\begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}$ est $\begin{pmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{pmatrix}$.
1. Calculer ${}^tUU$ et en déduire que $P^2 = P$.
2. Montrer que $MP = 0$ et $PM = 0$.
