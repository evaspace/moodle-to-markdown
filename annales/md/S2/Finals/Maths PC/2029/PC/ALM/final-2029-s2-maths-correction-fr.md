# Examen S2-B4-ALM (applications linéaires et matrices) — mai 2025 (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (pas de corrigé officiel). Sujet : `final-2029-s2-maths-subject-fr.md` (même dossier). Calculs vérifiés avec sympy. 

## Exercice 1 : opérations matricielles (8 points)
Type : opérations matricielles, produit, inverse · ECUE : ALM · Niveau : maths-s2-alm/6
Formules : $(\lambda A + \mu B)_{ij} = \lambda a_{ij} + \mu b_{ij}$ ; produit $AB$ défini si (colonnes de $A$) = (lignes de $B$), taille $n \times p$ par $p \times q$ donne $n \times q$ ; $(AB)_{ij} = \sum_k a_{ik}b_{kj}$ ; inverse par pivot de Gauss ; vérification $AA^{-1} = I$

1. $c_{11}=2x-4y=-6$ et $c_{22}=4x-12y=-8$. Alors $x=2y-3$ et $4(2y-3)-12y=-8$, soit $-4y=4$ : $y=-1$ et $x=-5$. $2A-4B=\begin{pmatrix}-6&10-28\\4&-8\end{pmatrix}=\begin{pmatrix}-6&-18\\4&-8\end{pmatrix}$.
2. $A\in\mathcal M_{2,1}$ et $B\in\mathcal M_{3,2}$ : $AB$ impossible (1 colonne de $A$ $\ne$ 3 lignes de $B$). $BA$ possible ($2$ colonnes de $B$ $=$ $2$ lignes de $A$) : $BA=\begin{pmatrix}1(-1)+2(-2)\\-3(-1)+4(-2)\\0+1(-2)\end{pmatrix}=\begin{pmatrix}-5\\-5\\-2\end{pmatrix}$.
3. (a) $\det A=1\cdot(3+9)-4\cdot(0+3)+1\cdot(0-1)=12-12-1=-1\ne0$. Matrice des cofacteurs transposée : $\mathrm{adj}(A)=\begin{pmatrix}12&9&13\\-3&-2&-3\\-1&-1&-1\end{pmatrix}$, donc $A^{-1}=\dfrac1{\det A}\mathrm{adj}(A)=\begin{pmatrix}-12&-9&-13\\3&2&3\\1&1&1\end{pmatrix}$.
   (b) On calcule $AA^{-1}$ (ou $A^{-1}A$) et on vérifie qu'on obtient $I_3$.

## Exercice 2 : application linéaire (10 points)
Type : noyau, image, rang d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/3
Formules : linéaire : $f(\lambda u + v) = \lambda f(u) + f(v)$ ; $\mathrm{Ker} f$ : résoudre $f(x) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \mathrm{rg} f$ ; $\mathrm{rg} f = \dim F \Rightarrow \mathrm{Im} f = F$ (surjective) ; $\mathrm{Im} f = \mathrm{Vect}(f(e_1), \dots, f(e_n))$

1. $f(aX^2+bX+c)=0\iff a=0$ et $b=c$ : $\mathrm{Ker}(f)=\{b(X+1)\}=\mathrm{Vect}(X+1)$, base $(X+1)$, dimension $1$.
2. Théorème du rang : pour $f\in\mathcal L(E,F)$ avec $E$ de dimension finie, $\dim E=\dim\mathrm{Ker}(f)+\dim\mathrm{Im}(f)$. Donc $\dim\mathrm{Im}(f)=3-1=2$.
3. Non : $\mathrm{Ker}(f)\ne\{0\}$ (il contient $X+1$).
4. Oui : $\mathrm{Im}(f)\subset\mathbb R^2$ et $\dim\mathrm{Im}(f)=2=\dim\mathbb R^2$, donc $\mathrm{Im}(f)=\mathbb R^2$.

## Exercice 3 : changement de bases (7 points)
Type : matrice d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/5
Formules : colonne $j$ = coordonnées de $f(e_j)$ dans la base d'arrivée ; base canonique de $\mathbb{R}_2[X]$ : $(1, X, X^2)$ ; de $\mathcal{M}_2(\mathbb{R})$ : $E_{11}, E_{12}, E_{21}, E_{22}$ ; taille (dim arrivée) $\times$ (dim départ)

1. $\mathrm{Mat}(f)=\begin{pmatrix}-2&-1&0\\0&-1&-2\\0&0&0\end{pmatrix}$.
2. $f(1,0,0)=(-2,0,0)$ ; $f(-1,1,0)=(2-1,-1,0)=(1,-1,0)$ ; $f(1,-2,1)=(-2+2,-2+2,0)=(0,0,0)$. Matrice : $\begin{pmatrix}-2&1&0\\0&-1&0\\0&0&0\end{pmatrix}$.
3. $f(\varepsilon_1)=-2\varepsilon_1$, $f(\varepsilon_2)=(1,-1,0)=-\varepsilon_2$ (car $-(-1,1,0)=(1,-1,0)$), $f(\varepsilon_3)=0$ : $A=\begin{pmatrix}-2&0&0\\0&-1&0\\0&0&0\end{pmatrix}$.
4. $\mathrm{Im}(f)$ est engendrée par les colonnes de $A$ (coordonnées dans $\mathcal B_1$, qui est une base) : deux colonnes non nulles et non colinéaires, une colonne nulle : rang $2$.
5. Théorème du rang : $\dim\mathrm{Ker}(f)=3-2=1$. $f(\varepsilon_3)=0$ avec $\varepsilon_3=(1,-2,1)\ne0$ : base $\big((1,-2,1)\big)$.

## Exercice 4 : projection (10 points)
Type : projecteur, noyau et image · ECUE : ALM · Niveau : maths-s2-alm/10
Formules : projecteur $\iff f \circ f = f$ ; $E = \mathrm{Ker} f \oplus \mathrm{Im} f$ ; $f = id$ sur $\mathrm{Im} f$, $0$ sur $\mathrm{Ker} f$ ; matrice dans une base adaptée $\mathrm{diag}(0, \dots, 0, 1, \dots, 1)$

1. $u\in F$ s'écrit $u=u+0_E$ avec $u\in F$, $0_E\in G$ : par unicité, $v=u$ et $p(u)=u$.
2. $u\in G$ s'écrit $u=0_E+u$ avec $0_E\in F$ : $v=0_E$ et $p(u)=0_E$.
3. $p(u)=v\in F$, donc par 1, $p(p(u))=p(v)=v=p(u)$.
4. (a) Les droites $F$ (direction $(2,1)$) et $G$ (direction $(-2,4)$) : on mène par $u=(3,4)$ la parallèle à $G$ qui coupe $F$ en $v$, et la parallèle à $F$ qui coupe $G$ en $w$. Par le calcul : $(3,4)=a(2,1)+b(-2,4)$ donne $a=2$, $b=\dfrac12$ : $v=2\varepsilon_1=(4,2)$, $w=\dfrac12\varepsilon_2=(-1,2)$, $p(u)=(4,2)$.
   (b) $\det\begin{pmatrix}2&-2\\1&4\end{pmatrix}=10\ne0$ : $\varepsilon_1,\varepsilon_2$ non colinéaires, deux vecteurs libres en dimension $2$ : base.
   (c) $p(\varepsilon_1)=\varepsilon_1$, $p(\varepsilon_2)=0$ : $\mathrm{Mat}_{\mathcal B}(p)=\begin{pmatrix}1&0\\0&0\end{pmatrix}$.

## Exercice 5 : une démonstration guidée (5 points)
Type : changement de base, formule $Y = AX$ · ECUE : ALM · Niveau : maths-s2-alm/9
Formules : $X = PX'$, $P$ = matrice de passage (colonnes = nouveaux vecteurs dans l'ancienne base) ; $X' = P^{-1}X$ ; $f(e_j) = \sum_i a_{i,j}\varepsilon_i$ ; coordonnées de l'image $Y = AX$ ; inverse $2 \times 2$ : $\frac1{ad - bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$

1. $f(e_1)=a_1\varepsilon_1+a_3\varepsilon_2+a_5\varepsilon_3$ et $f(e_2)=a_2\varepsilon_1+a_4\varepsilon_2+a_6\varepsilon_3$.
2. $f(u)=\alpha f(e_1)+\beta f(e_2)=(a_1\alpha+a_2\beta)\varepsilon_1+(a_3\alpha+a_4\beta)\varepsilon_2+(a_5\alpha+a_6\beta)\varepsilon_3$.
3. $V=AU$.
4. $(4,6)=\alpha(1,2)+\beta(3,4)$ : $\alpha+3\beta=4$, $2\alpha+4\beta=6$, donc $\alpha=\beta=1$, $U=\begin{pmatrix}1\\1\end{pmatrix}$. $V=AU=\begin{pmatrix}0\\1\\-2\end{pmatrix}$. $f(u)=0\cdot1+1\cdot(X+1)-2(X-1)^2=-2X^2+5X-1$ : $a=-2$, $b=5$, $c=-1$.
