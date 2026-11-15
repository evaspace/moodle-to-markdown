# Partiel S2 — juin 2021 (sujet, FR)

- Source : `raw/S2/Finals/Maths PC/2025/final-2025-s2-maths-subject-fr.pdf` (scan, 10 pages)
- Date réelle : juin 2021 (S2 2021, dossier promo 2025). Barème sur 30.
- Attention : ce sujet FR est une autre version que celle du corrigé (`final-2025-s2-maths-correction-fr.md`) et du sujet EN : mêmes exercices, données différentes (familles de l'exercice 1, applications des exercices 4 à 8). Le corrigé sert de modèle de méthode.
- Tout au long de ce partiel, chaque réponse doit être soigneusement justifiée.

## Exercice 1 (4,5 points)
Type : familles libres, génératrices, bases ; coordonnées · ECUE : EV · Niveau : maths-s2-ev/7
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \lambda_i = 0$ ; en dimension $n$, une famille libre de $n$ vecteurs est une base ; plus de $n$ vecteurs $\Rightarrow$ liée ; coordonnées : résoudre $P = \alpha Q_1 + \beta Q_2 + \gamma Q_3$ en identifiant les coefficients

Soit $E = \mathbb{R}_2[X]$.
a. Déterminer pour chacune des familles suivantes s'il s'agit d'une base de $E$.
$\mathcal{F}_1 = \{P_1(X) = 2X + 2,\ P_2(X) = X^2 + X + 1\}$ ;
$\mathcal{F}_2 = \{Q_1(X) = X^2 + 2,\ Q_2(X) = X^2 + 4X,\ Q_3(X) = X^2 + 2X + 1\}$ ;
$\mathcal{F}_3 = \{R_1(X) = X^2 + 2,\ R_2(X) = X^2 + 4X,\ R_3(X) = X^2 + 3X + 2\}$.
b. Déterminer les coordonnées du polynôme $P(X) = 2X^2 + X + 8$ dans chacune des bases identifiées ci-dessus.

## Exercice 2 (2,5 points)
Type : application linéaire (caractérisation) · ECUE : ALM · Niveau : maths-s2-alm/1
Formules : $f$ linéaire $\Rightarrow f(0) = 0$ et $f(2x) = 2f(x)$ (conditions nécessaires) ; réciproquement vérifier $f(\lambda x + y) = \lambda f(x) + f(y)$ ; les applications linéaires de $\mathbb{R}$ dans $\mathbb{R}$ sont $x \mapsto bx$

Soient $(a, b, c) \in \mathbb{R}^3$ et $\varphi : \mathbb{R} \to \mathbb{R},\ x \mapsto ax^2 + bx + c$. Déterminer les conditions nécessaires et suffisantes sur $(a, b, c)$ pour que $\varphi$ soit linéaire. Démontrez votre réponse.

## Exercice 3 (5 points)
Type : sous-espaces supplémentaires (fonctions paires et impaires) · ECUE : EV · Niveau : maths-s2-ev/9
Formules : sev : non vide, stable par $\lambda f + g$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $F + G = E$ ; $f = \frac{f(x) + f(-x)}2 + \frac{f(x) - f(-x)}2$ ; paire et impaire $\Rightarrow f = 0$

On considère $E = \mathbb{R}^{\mathbb{R}}$, le $\mathbb{R}$-ev des fonctions de $\mathbb{R}$ dans $\mathbb{R}$ et deux sous-ensembles de $E$ : $\mathcal{P}$ l'ensemble des fonctions paires ($\forall x \in \mathbb{R}, f(-x) = f(x)$) et $\mathcal{I}$ l'ensemble des fonctions impaires ($\forall x \in \mathbb{R}, f(-x) = -f(x)$).
a. Montrer que $\mathcal{P}$ est un sev de $E$. (On admettra que $\mathcal{I}$ est aussi un sev de $E$.)
b. Montrer à l'aide d'un contre-exemple que $\mathcal{P} \cup \mathcal{I} \neq E$.
c. À partir d'une fonction $f \in E$, on définit les deux fonctions $f_p : x \mapsto \dfrac{f(x) + f(-x)}2$ et $f_i : x \mapsto \dfrac{f(x) - f(-x)}2$. Montrer que $f_p$ est paire et $f_i$ impaire. Calculer $f_p + f_i$.
d. Montrer que $\mathcal{P}$ et $\mathcal{I}$ sont supplémentaires dans $E$.

## Exercice 4 (4 points)
Type : noyau, image, rang d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/3
Formules : linéaire : $f(\lambda u + v) = \lambda f(u) + f(v)$ ; $\mathrm{Ker} f$ : résoudre $f(x) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \mathrm{rg} f$ ; $\mathrm{rg} f = \dim F \Rightarrow \mathrm{Im} f = F$ (surjective) ; $\mathrm{Im} f = \mathrm{Vect}(f(e_1), \dots, f(e_n))$

Soit $f : \mathbb{R}^3 \to \mathbb{R}[X],\ (a, b, c) \mapsto (a - b)X^4 + (2a + c)X^2 + (a + b + c)$.
a. Déterminer $\mathrm{Ker} f$, $\dim \mathrm{Ker} f$ et $\dim \mathrm{Im} f$.
b. $f$ est-elle injective ?
c. $f$ est-elle surjective ?

## Exercice 5 (4 points)
Type : matrice d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/5
Formules : colonne $j$ = coordonnées de $f(e_j)$ dans la base d'arrivée ; base canonique de $\mathbb{R}_2[X]$ : $(1, X, X^2)$ ; de $\mathcal{M}_2(\mathbb{R})$ : $E_{11}, E_{12}, E_{21}, E_{22}$ ; taille (dim arrivée) $\times$ (dim départ)

Soit $g \in \mathcal{L}(\mathbb{R}^3, \mathbb{R}^4)$ l'application linéaire associée à la matrice $\begin{pmatrix} 1 & 0 & 1 \\ 2 & 3 & 0 \\ 1 & 0 & 0 \\ 2 & 3 & 1 \end{pmatrix}$ dans les bases canoniques au départ et à l'arrivée. On note $\mathcal{B}_3 = \{e_1, e_2, e_3\}$ la base canonique de $\mathbb{R}^3$ et $\mathcal{B}_4$ la base canonique de $\mathbb{R}^4$.
On définit $\mathcal{D}_3 = \{u_1, u_2, u_3\}$ base de $\mathbb{R}^3$ où $u_1 = (1, 0, 1)$, $u_2 = (1, -1, 0)$, $u_3 = (0, 1, -1)$ et $\mathcal{D}_4 = \{v_1, v_2, v_3, v_4\}$ base de $\mathbb{R}^4$ où $v_1 = (1, 2, 1, 2)$, $v_2 = (0, 3, 0, 3)$, $v_3 = (1, 0, 0, 1)$, $v_4 = (0, 0, 0, 1)$.
a. Quelle est l'image des vecteurs de $\mathcal{B}_3$ par $g$ ?
b. Soit $(x, y, z) \in \mathbb{R}^3$, calculer $g((x, y, z))$.
c. Déterminer la matrice de $g$ dans la base $\mathcal{B}_3$ au départ et $\mathcal{D}_4$ à l'arrivée.
d. Déterminer la matrice de $g$ dans la base $\mathcal{D}_3$ au départ et $\mathcal{D}_4$ à l'arrivée.

## Exercice 6 (4 points)
Type : noyau, image, rang d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/3
Formules : linéaire : $f(\lambda u + v) = \lambda f(u) + f(v)$ ; $\mathrm{Ker} f$ : résoudre $f(x) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \mathrm{rg} f$ ; $\mathrm{rg} f = \dim F \Rightarrow \mathrm{Im} f = F$ (surjective) ; $\mathrm{Im} f = \mathrm{Vect}(f(e_1), \dots, f(e_n))$

Soit $h : \mathbb{R}^3 \to \mathbb{R}^3,\ (x, y, z) \mapsto (2x + y + 3z, x - y, x + z)$.
a. Déterminer la matrice $M$ associée à $h$ dans la base canonique au départ et à l'arrivée.
b. On appelle $C_1, C_2, C_3$ les vecteurs colonnes de cette matrice. La famille $\{C_1, C_2, C_3\}$ est-elle libre ? Sinon, en extraire une famille libre maximale.
c. En déduire $\mathrm{Im}\,h$, $\mathrm{rg}(h)$ et $\mathrm{Ker}\,h$.

## Exercice 7 (3 points)
Type : inverse d'une matrice · ECUE : ALM · Niveau : maths-s2-alm/8
Formules : $A$ inversible $\iff \det A \neq 0$ ; pivot de Gauss sur $(A \mid I_n) \to (I_n \mid A^{-1})$ ; ou $A^{-1} = \frac1{\det A}{}^t\mathrm{Com}(A)$ ; vérifier $AA^{-1} = I_n$ ; $2 \times 2$ : $\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1} = \frac1{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$

Soit $\mathcal{B}$ la base canonique de $\mathbb{R}^3$ et $\mathcal{B}' = \{(1, 0, -1) ; (4, -1, -3) ; (1, 3, -3)\}$ une autre base de $\mathbb{R}^3$. Soit $f$ l'application linéaire associée à la matrice $P = \begin{pmatrix} 1 & 4 & 1 \\ 0 & -1 & 3 \\ -1 & -3 & -3 \end{pmatrix}$ dans la base canonique au départ et à l'arrivée.
a. Sans aucun calcul, que peut-on dire du rang de $f$ ? Comment appelle-t-on la matrice $P$ ?
b. Déterminer $P^{-1}$ la matrice inverse de $P$, sans oublier de vérifier votre résultat.

## Exercice 8 (4 points)
Type : projecteur, noyau et image · ECUE : ALM · Niveau : maths-s2-alm/10
Formules : projecteur $\iff f \circ f = f$ ; $E = \mathrm{Ker} f \oplus \mathrm{Im} f$ ; $f = id$ sur $\mathrm{Im} f$, $0$ sur $\mathrm{Ker} f$ ; matrice dans une base adaptée $\mathrm{diag}(0, \dots, 0, 1, \dots, 1)$

Soit $f : \mathbb{R}^3 \to \mathbb{R}^3,\ (x, y, z) \mapsto \left(x, \frac12(y - z), \frac12(z - y)\right)$.
a. Montrer que $f$ est un projecteur.
b. Déterminer $\mathrm{Ker} f$ et $\mathrm{Im} f$ sous forme d'espaces vectoriels engendrés et en déduire une base $\mathcal{B}_1$ de $\mathrm{Ker} f$ et une base $\mathcal{B}_2$ de $\mathrm{Im} f$.
c. On admet que la réunion des vecteurs de ces deux bases $\mathcal{B} = \mathcal{B}_1 \cup \mathcal{B}_2$ est une base de $\mathbb{R}^3$. Déterminer la matrice de $f$ dans la base $\mathcal{B}$ au départ et à l'arrivée.
