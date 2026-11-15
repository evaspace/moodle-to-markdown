# Partiel corrigé S2 — juin 2021

- Source : `raw/S2/Finals/Maths PC/2025/final-2025-s2-maths-correction-fr.pdf` (scan, 5 pages, énoncés en gras et corrections)
- Date réelle : juin 2021 (S2 2021, dossier promo 2025). Sujet : `final-2025-s2-maths-subject-fr.md`.

## Exercice 1 (4,5 points)
Type : familles libres, génératrices, bases ; coordonnées · ECUE : EV · Niveau : maths-s2-ev/7
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \lambda_i = 0$ ; en dimension $n$, une famille libre de $n$ vecteurs est une base ; plus de $n$ vecteurs $\Rightarrow$ liée ; coordonnées : résoudre $P = \alpha Q_1 + \beta Q_2 + \gamma Q_3$ en identifiant les coefficients

Soit $E = \mathbb{R}_2[X]$.
a. Pour chacune des familles suivantes, dire s'il s'agit d'une base de $E$ : $\mathcal{F}_1 = \{2X + 1, X^2 + X + 2, X^2 + X + 1, 2X^2 + 3\}$ ; $\mathcal{F}_2 = \{Q_1 = X^2 + 2, Q_2 = X^2 + 4X, Q_3 = X^2 + 3X + 2\}$ ; $\mathcal{F}_3 = \{R_1 = -X^2 + 2, R_2 = X^2 - 4X, R_3 = X^2 - 2X - 1\}$.
- $\mathcal{F}_1$ : $\dim \mathbb{R}_2[X] = 3$, toutes les bases ont 3 éléments ; $\mathrm{card}\,\mathcal{F}_1 = 4$ : pas une base.
- $\mathcal{F}_2$ : $\alpha Q_1 + \beta Q_2 + \gamma Q_3 = 0 \iff \alpha + \beta + \gamma = 0$, $4\beta + 3\gamma = 0$, $2\alpha + 2\gamma = 0 \iff \alpha = \beta = \gamma = 0$. Libre et $\mathrm{card} = 3 = \dim$ : base.
- $\mathcal{F}_3$ : $\alpha R_1 + \beta R_2 + \gamma R_3 = 0 \iff -\alpha + \beta + \gamma = 0$, $-4\beta - 2\gamma = 0$, $2\alpha - \gamma = 0 \iff \beta = -\alpha$, $\gamma = 2\alpha$. $(1, -1, 2)$ est solution non nulle : $R_1 - R_2 + 2R_3 = 0$, pas libre, pas une base.
b. Coordonnées de $P(X) = 2X^2 + X + 8$ dans la base $\mathcal{F}_2$ : $\alpha + \beta + \gamma = 2$, $4\beta + 3\gamma = 1$, $2\alpha + 2\gamma = 8$, d'où $(\alpha, \beta, \gamma) = (1, -2, 3)$ : $P = Q_1 - 2Q_2 + 3Q_3$.

## Exercice 2 (2,5 points)
Type : application linéaire (caractérisation) · ECUE : ALM · Niveau : maths-s2-alm/1
Formules : $f$ linéaire $\Rightarrow f(0) = 0$ et $f(2x) = 2f(x)$ (conditions nécessaires) ; réciproquement vérifier $f(\lambda x + y) = \lambda f(x) + f(y)$ ; les applications linéaires de $\mathbb{R}$ dans $\mathbb{R}$ sont $x \mapsto bx$

Soient $(a, b, c) \in \mathbb{R}^3$ et $\varphi : \mathbb{R} \to \mathbb{R},\ x \mapsto ax^2 + bx + c$. Déterminer les conditions nécessaires et suffisantes sur $(a, b, c)$ pour que $\varphi$ soit linéaire.
$\Rightarrow$ : $\varphi(0) = 0 \Rightarrow c = 0$ ; $\varphi(2 \times 1) = 2\varphi(1) \Rightarrow 4a + 2b = 2a + 2b \Rightarrow a = 0$.
$\Leftarrow$ : si $a = c = 0$, $\varphi(x) = bx$ et $\varphi(\lambda x + y) = \lambda\varphi(x) + \varphi(y)$. $\varphi$ linéaire ssi $a = c = 0$.

## Exercice 3 (5 points)
Type : sous-espaces supplémentaires (fonctions paires et impaires) · ECUE : EV · Niveau : maths-s2-ev/9
Formules : sev : non vide, stable par $\lambda f + g$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $F + G = E$ ; $f = \frac{f(x) + f(-x)}2 + \frac{f(x) - f(-x)}2$ ; paire et impaire $\Rightarrow f = 0$

$E = \mathbb{R}^{\mathbb{R}}$, $\mathcal{P}$ l'ensemble des fonctions paires, $\mathcal{I}$ l'ensemble des fonctions impaires.
a. Montrer que $\mathcal{P}$ est un sev de $E$ (on admet que $\mathcal{I}$ en est un). Pour $(f, g) \in \mathcal{P}^2$, $\lambda \in \mathbb{R}$ : $(\lambda f + g)(-x) = \lambda f(x) + g(x)$ : stable par combinaison linéaire.
b. Montrer à l'aide d'un contre-exemple que $\mathcal{P} \cup \mathcal{I} \neq E$. $f(x) = x + 1$ : $f(-x) = -x + 1 \neq f(x)$ et $\neq -f(x)$, donc $f \notin \mathcal{P} \cup \mathcal{I}$.
c. Pour $f \in E$, $f_p(x) = \frac{f(x) + f(-x)}2$ et $f_i(x) = \frac{f(x) - f(-x)}2$. Montrer que $f_p$ est paire, $f_i$ impaire ; calculer $f_p + f_i$. $f_p(-x) = f_p(x)$, $f_i(-x) = -f_i(x)$, $f = f_p + f_i$.
d. Montrer que $\mathcal{P}$ et $\mathcal{I}$ sont supplémentaires dans $E$. $\mathcal{P} \oplus \mathcal{I} = E \iff \mathcal{P} \cap \mathcal{I} = \{0_E\}$ et $\mathcal{P} + \mathcal{I} = E$. Si $f \in \mathcal{P} \cap \mathcal{I}$, $f(x) = f(-x) = -f(x)$ donc $f = 0$. Et tout $f$ s'écrit $f_p + f_i$.

## Exercice 4 (4 points)
Type : noyau, image, rang d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/3
Formules : linéaire : $f(\lambda u + v) = \lambda f(u) + f(v)$ ; $\mathrm{Ker} f$ : résoudre $f(x) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \mathrm{rg} f$ ; $\mathrm{rg} f = \dim F \Rightarrow \mathrm{Im} f = F$ (surjective) ; $\mathrm{Im} f = \mathrm{Vect}(f(e_1), \dots, f(e_n))$

Soit $f : \mathbb{R}^3 \to \mathbb{R}[X],\ (a, b, c) \mapsto (a + b)X^4 + (2a - c)X^2 + (a + b + c)$.
a. Déterminer $\mathrm{Ker} f$, $\dim \mathrm{Ker} f$ et $\dim \mathrm{Im} f$. $a + b = 0$, $2a - c = 0$, $a + b + c = 0 \iff a = b = c = 0$ : $\mathrm{Ker} f = \{0\}$, $\dim \mathrm{Ker} f = 0$, théorème du rang : $\dim \mathrm{Im} f = 3$.
b. $f$ est-elle injective ? Oui, $\dim \mathrm{Ker} f = 0$.
c. $f$ est-elle surjective ? Non : $\dim \mathrm{Im} f = 3$ et $\mathbb{R}[X]$ est de dimension infinie.

## Exercice 5 (4 points)
Type : matrice d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/5
Formules : colonne $j$ = coordonnées de $f(e_j)$ dans la base d'arrivée ; base canonique de $\mathbb{R}_2[X]$ : $(1, X, X^2)$ ; de $\mathcal{M}_2(\mathbb{R})$ : $E_{11}, E_{12}, E_{21}, E_{22}$ ; taille (dim arrivée) $\times$ (dim départ)

Soit $g \in \mathcal{L}(\mathbb{R}^3, \mathbb{R}^4)$ associée à la matrice $\begin{pmatrix} 1 & 0 & 1 \\ 2 & 3 & 0 \\ 1 & 0 & 0 \\ 2 & 3 & 1 \end{pmatrix}$ dans les bases canoniques $\mathcal{B}_3 = (e_1, e_2, e_3)$ et $\mathcal{B}_4$. On définit $\mathcal{D}_3 = (u_1, u_2, u_3)$ base de $\mathbb{R}^3$ avec $u_1 = (1, -1, 0)$, $u_2 = (1, 0, 1)$, $u_3 = (0, 1, -1)$, et $\mathcal{D}_4 = (v_1, v_2, v_3, v_4)$ base de $\mathbb{R}^4$ avec $v_1 = (0, 0, 0, 1)$, $v_2 = (1, 0, 0, 1)$, $v_3 = (1, 2, 1, 2)$, $v_4 = (0, 3, 0, 3)$.
a. Image des vecteurs de $\mathcal{B}_3$ : $g(e_1) = (1, 2, 1, 2)$, $g(e_2) = (0, 3, 0, 3)$, $g(e_3) = (1, 0, 0, 1)$.
b. $g(x, y, z) = (x + z, 2x + 3y, x, 2x + 3y + z)$.
c. Matrice de $g$ de $\mathcal{B}_3$ vers $\mathcal{D}_4$ : $g(e_1) = v_3$, $g(e_2) = v_4$, $g(e_3) = v_2$, donc $\begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}$.
d. Matrice de $g$ de $\mathcal{D}_3$ vers $\mathcal{D}_4$ : $g(u_1) = v_3 - v_4$, $g(u_2) = v_3 + v_2$, $g(u_3) = v_4 - v_2$, donc $\begin{pmatrix} 0 & 0 & 0 \\ 0 & 1 & -1 \\ 1 & 1 & 0 \\ -1 & 0 & 1 \end{pmatrix}$.

## Exercice 6 (4 points)
Type : noyau, image, rang d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/3
Formules : linéaire : $f(\lambda u + v) = \lambda f(u) + f(v)$ ; $\mathrm{Ker} f$ : résoudre $f(x) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \mathrm{rg} f$ ; $\mathrm{rg} f = \dim F \Rightarrow \mathrm{Im} f = F$ (surjective) ; $\mathrm{Im} f = \mathrm{Vect}(f(e_1), \dots, f(e_n))$

Soit $h : \mathbb{R}^3 \to \mathbb{R}^3,\ (x, y, z) \mapsto (2x + 3y + z, x - z, x + y)$.
a. Matrice $M$ de $h$ dans la base canonique : $M = \begin{pmatrix} 2 & 3 & 1 \\ 1 & 0 & -1 \\ 1 & 1 & 0 \end{pmatrix}$.
b. Les colonnes $C_1, C_2, C_3$ sont-elles libres ? Sinon, en extraire une famille libre maximale. $C_1 + C_3 = C_2$ : liée. $\{C_1, C_3\}$ est libre (non colinéaires) : famille libre maximale.
c. En déduire $\mathrm{Im}\,h$, $\mathrm{rg}(h)$ et $\mathrm{Ker}\,h$. $\mathrm{Im}\,h = \mathrm{Vect}(C_1, C_3)$, $\mathrm{rg}\,h = 2$ ; théorème du rang : $\dim \mathrm{Ker}\,h = 1$. $C_1 - C_2 + C_3 = 0$ donne $(1, -1, 1) \in \mathrm{Ker}\,h$, donc $\mathrm{Ker}\,h = \mathrm{Vect}((1, -1, 1))$.

## Exercice 7 (3 points)
Type : inverse d'une matrice · ECUE : ALM · Niveau : maths-s2-alm/8
Formules : $A$ inversible $\iff \det A \neq 0$ ; pivot de Gauss sur $(A \mid I_n) \to (I_n \mid A^{-1})$ ; ou $A^{-1} = \frac1{\det A}{}^t\mathrm{Com}(A)$ ; vérifier $AA^{-1} = I_n$ ; $2 \times 2$ : $\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1} = \frac1{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$

Soient $\mathcal{B}$ la base canonique de $\mathbb{R}^3$ et $\mathcal{B}' = \{(1, 3, -3), (6, 2, -7), (1, 0, -1)\}$ une autre base de $\mathbb{R}^3$. Soit $f$ l'application linéaire associée à $P = \begin{pmatrix} 1 & 6 & 1 \\ 3 & 2 & 0 \\ -3 & -7 & -1 \end{pmatrix}$ dans la base canonique.
a. Sans calcul, que dire du rang de $f$ ? Comment appelle-t-on $P$ ? $\mathrm{Im} f = \mathrm{Vect}\,\mathcal{B}' = \mathbb{R}^3$ donc $\mathrm{rg} f = 3$. $P$ est la matrice de passage de $\mathcal{B}$ à $\mathcal{B}'$.
b. Déterminer $P^{-1}$ et vérifier. $P^{-1} = \begin{pmatrix} -2 & -1 & -2 \\ 3 & 2 & 3 \\ -15 & -11 & -16 \end{pmatrix}$, on vérifie $P^{-1}P = I_3$.

## Exercice 8 (4 points)
Type : projecteur, noyau et image · ECUE : ALM · Niveau : maths-s2-alm/10
Formules : projecteur $\iff f \circ f = f$ ; $E = \mathrm{Ker} f \oplus \mathrm{Im} f$ ; $f = id$ sur $\mathrm{Im} f$, $0$ sur $\mathrm{Ker} f$ ; matrice dans une base adaptée $\mathrm{diag}(0, \dots, 0, 1, \dots, 1)$

Soit $f : \mathbb{R}^3 \to \mathbb{R}^3,\ (x, y, z) \mapsto \left(\frac12(x - z), y, \frac12(z - x)\right)$.
a. Montrer que $f$ est un projecteur. $f \circ f = f$ : $f(f(x, y, z)) = \left(\frac12\left(\frac12(x - z) - \frac12(z - x)\right), y, \dots\right) = f(x, y, z)$.
b. Déterminer $\mathrm{Ker} f$ et $\mathrm{Im} f$ et une base de chacun. $\mathrm{Ker} f = \mathrm{Vect}((1, 0, 1))$, base $\mathcal{B}_1 = \{(1, 0, 1)\}$ ; $\mathrm{Im} f = \mathrm{Vect}\left(\left(\frac12, 0, -\frac12\right), (0, 1, 0)\right)$, base $\mathcal{B}_2$.
c. On admet que $\mathcal{B} = \mathcal{B}_1 \cup \mathcal{B}_2$ est une base de $\mathbb{R}^3$. Matrice de $f$ dans $\mathcal{B}$ : $f((1, 0, 1)) = 0$, $f\left(\left(\frac12, 0, -\frac12\right)\right) = \left(\frac12, 0, -\frac12\right)$, $f((0, 1, 0)) = (0, 1, 0)$, donc $\mathcal{M}_{\mathcal{B}}(f) = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$.
