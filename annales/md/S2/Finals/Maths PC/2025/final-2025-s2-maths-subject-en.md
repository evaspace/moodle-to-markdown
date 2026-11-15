# S2 final exam — June 2021 (subject, EN)

- Source : `raw/S2/Finals/Maths PC/2025/final-2025-s2-maths-subject-en.pdf` (10 pages)
- Date réelle : juin 2021 (S2 2021, dossier promo 2025). Même version que le corrigé `final-2025-s2-maths-correction-fr.md` (le sujet FR `final-2025-s2-maths-subject-fr.md` a d'autres données).
- Duration: 3 hours. Marked out of 30, re-scaled to 20. Documents and pocket calculators are not allowed. Each answer must be accurately justified.

## Exercise 1 (4,5 points)
Type : familles libres, génératrices, bases ; coordonnées · ECUE : EV · Niveau : maths-s2-ev/7
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \lambda_i = 0$ ; en dimension $n$, une famille libre de $n$ vecteurs est une base ; plus de $n$ vecteurs $\Rightarrow$ liée ; coordonnées : résoudre $P = \alpha Q_1 + \beta Q_2 + \gamma Q_3$ en identifiant les coefficients

Let $E = \mathbb{R}_2[X]$.
a. For each of the families below, say whether it is a basis of $E$ or not.
$\mathcal{F}_1 = \{P_1 = 2X + 1, P_2 = X^2 + X + 2, P_3 = X^2 + X + 1, P_4 = 2X^2 + 3\}$ ; $\mathcal{F}_2 = \{Q_1 = X^2 + 2, Q_2 = X^2 + 4X, Q_3 = X^2 + 3X + 2\}$ ; $\mathcal{F}_3 = \{R_1 = -X^2 + 2, R_2 = X^2 - 4X, R_3 = X^2 - 2X - 1\}$.
b. Find the coordinates of the polynomial $P(X) = 2X^2 + X + 8$ in each basis that you have found at question a.

## Exercise 2 (2,5 points)
Type : application linéaire (caractérisation) · ECUE : ALM · Niveau : maths-s2-alm/1
Formules : $f$ linéaire $\Rightarrow f(0) = 0$ et $f(2x) = 2f(x)$ (conditions nécessaires) ; réciproquement vérifier $f(\lambda x + y) = \lambda f(x) + f(y)$ ; les applications linéaires de $\mathbb{R}$ dans $\mathbb{R}$ sont $x \mapsto bx$

Let $(a, b, c) \in \mathbb{R}^3$ and $\varphi : \mathbb{R} \to \mathbb{R},\ x \mapsto ax^2 + bx + c$. Determine necessary and sufficient conditions on $(a, b, c)$ for $\varphi$ to be a linear map. Prove your answer.

## Exercise 3 (5 points)
Type : sous-espaces supplémentaires (fonctions paires et impaires) · ECUE : EV · Niveau : maths-s2-ev/9
Formules : sev : non vide, stable par $\lambda f + g$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $F + G = E$ ; $f = \frac{f(x) + f(-x)}2 + \frac{f(x) - f(-x)}2$ ; paire et impaire $\Rightarrow f = 0$

Consider $\mathbb{R}^{\mathbb{R}}$ and its subsets $\mathcal{E}$ (even functions) and $\mathcal{O}$ (odd functions).
a. Show that $\mathcal{E}$ is a linear subspace of $\mathbb{R}^{\mathbb{R}}$ (we accept that $\mathcal{O}$ is one too).
b. Using an example, show that $\mathcal{E} \cup \mathcal{O} \neq \mathbb{R}^{\mathbb{R}}$.
c. For $f \in \mathbb{R}^{\mathbb{R}}$ let $f_e(x) = \frac{f(x) + f(-x)}2$ and $f_o(x) = \frac{f(x) - f(-x)}2$. Show that $f_e$ is even and $f_o$ is odd. Compute $f_e + f_o$.
d. Show that $\mathcal{E}$ and $\mathcal{O}$ are supplementary in $\mathbb{R}^{\mathbb{R}}$.

## Exercise 4 (4 points)
Type : noyau, image, rang d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/3
Formules : linéaire : $f(\lambda u + v) = \lambda f(u) + f(v)$ ; $\mathrm{Ker} f$ : résoudre $f(x) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \mathrm{rg} f$ ; $\mathrm{rg} f = \dim F \Rightarrow \mathrm{Im} f = F$ (surjective) ; $\mathrm{Im} f = \mathrm{Vect}(f(e_1), \dots, f(e_n))$

Consider $f : \mathbb{R}^3 \to \mathbb{R}[X],\ (a, b, c) \mapsto (a + b)X^4 + (2a - c)X^2 + (a + b + c)$.
a. Determine $\mathrm{Ker} f$, $\dim \mathrm{Ker} f$ and $\dim \mathrm{Im} f$. b. Is $f$ injective? c. Is $f$ surjective?

## Exercise 5 (4 points)
Type : matrice d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/5
Formules : colonne $j$ = coordonnées de $f(e_j)$ dans la base d'arrivée ; base canonique de $\mathbb{R}_2[X]$ : $(1, X, X^2)$ ; de $\mathcal{M}_2(\mathbb{R})$ : $E_{11}, E_{12}, E_{21}, E_{22}$ ; taille (dim arrivée) $\times$ (dim départ)

Let $g \in \mathcal{L}(\mathbb{R}^3, \mathbb{R}^4)$ be associated to $\begin{pmatrix} 1 & 0 & 1 \\ 2 & 3 & 0 \\ 1 & 0 & 0 \\ 2 & 3 & 1 \end{pmatrix}$ in the standard bases $\mathcal{B}_3 = \{e_1, e_2, e_3\}$, $\mathcal{B}_4$. Bases $\mathcal{D}_3 = \{u_1 = (1, -1, 0), u_2 = (1, 0, 1), u_3 = (0, 1, -1)\}$ and $\mathcal{D}_4 = \{v_1 = (0, 0, 0, 1), v_2 = (1, 0, 0, 1), v_3 = (1, 2, 1, 2), v_4 = (0, 3, 0, 3)\}$.
a. Images of the vectors of $\mathcal{B}_3$ by $g$? b. Compute $g(x, y, z)$. c. Matrix of $g$ from $\mathcal{B}_3$ to $\mathcal{D}_4$. d. Matrix of $g$ from $\mathcal{D}_3$ to $\mathcal{D}_4$.

## Exercise 6 (4 points)
Type : noyau, image, rang d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/3
Formules : linéaire : $f(\lambda u + v) = \lambda f(u) + f(v)$ ; $\mathrm{Ker} f$ : résoudre $f(x) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \mathrm{rg} f$ ; $\mathrm{rg} f = \dim F \Rightarrow \mathrm{Im} f = F$ (surjective) ; $\mathrm{Im} f = \mathrm{Vect}(f(e_1), \dots, f(e_n))$

Let $h : \mathbb{R}^3 \to \mathbb{R}^3,\ (x, y, z) \mapsto (2x + 3y + z, x - z, x + y)$.
a. Determine the matrix $M$ of $h$ in the standard basis. b. Is the family of columns $\{C_1, C_2, C_3\}$ linearly independent? If not, find a maximal independent subfamily. c. Deduce $\mathrm{Im}\,h$, $\mathrm{rank}(h)$ and $\mathrm{Ker}\,h$.

## Exercise 7 (3 points)
Type : inverse d'une matrice · ECUE : ALM · Niveau : maths-s2-alm/8
Formules : $A$ inversible $\iff \det A \neq 0$ ; pivot de Gauss sur $(A \mid I_n) \to (I_n \mid A^{-1})$ ; ou $A^{-1} = \frac1{\det A}{}^t\mathrm{Com}(A)$ ; vérifier $AA^{-1} = I_n$ ; $2 \times 2$ : $\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1} = \frac1{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$

$\mathcal{B}$ standard basis of $\mathbb{R}^3$, $\mathcal{B}' = \{(1, 3, -3) ; (6, 2, -7) ; (1, 0, -1)\}$, $f$ associated to $P = \begin{pmatrix} 1 & 6 & 1 \\ 3 & 2 & 0 \\ -3 & -7 & -1 \end{pmatrix}$.
a. Without computation, what is the rank of $f$? How is $P$ called? b. Determine $P^{-1}$ and check your result.

## Exercise 8 (4 points)
Type : projecteur, noyau et image · ECUE : ALM · Niveau : maths-s2-alm/10
Formules : projecteur $\iff f \circ f = f$ ; $E = \mathrm{Ker} f \oplus \mathrm{Im} f$ ; $f = id$ sur $\mathrm{Im} f$, $0$ sur $\mathrm{Ker} f$ ; matrice dans une base adaptée $\mathrm{diag}(0, \dots, 0, 1, \dots, 1)$

Let $f : \mathbb{R}^3 \to \mathbb{R}^3,\ (x, y, z) \mapsto \left(\frac12(x - z), y, \frac12(z - x)\right)$.
a. Show that $f$ is a projector. b. Determine $\mathrm{Ker} f$ and $\mathrm{Im} f$ as spans, then bases $\mathcal{B}_1$ of $\mathrm{Ker} f$ and $\mathcal{B}_2$ of $\mathrm{Im} f$. c. $\mathcal{B} = \mathcal{B}_1 \cup \mathcal{B}_2$ is a basis of $\mathbb{R}^3$ (admitted): find the matrix of $f$ in $\mathcal{B}$.
