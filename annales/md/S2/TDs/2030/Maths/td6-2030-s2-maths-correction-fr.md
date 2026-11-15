# Feuille de TD — Applications linéaires et matrices (S2 2026) (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (pas de corrigé officiel). Sujet : `td6-2030-s2-maths-subject-fr.md` (même dossier). Calculs vérifiés avec sympy. 

## Exercice 1.1
Type : application linéaire définie par l'image d'une base · ECUE : ALM · Niveau : maths-s2-alm/1
Formules : linéarité : $f(\alpha u + \beta v) = \alpha f(u) + \beta f(v)$ ; $u = \sum x_ie_i \Rightarrow f(u) = \sum x_if(e_i)$ ; une application linéaire est entièrement déterminée par l'image d'une base ; deux applications linéaires égales sur une base (ou une famille génératrice) sont égales ; si les vecteurs donnés sont liés, les images doivent vérifier la même relation ; s'ils n'engendrent pas l'espace, $f$ n'est pas déterminée

1. $f(1,-1,0)=f(e_1)-f(e_2)=(2,1)-(-1,1)=(3,0)\ne(3,1)$ : non.
2. $f(1,2,3)=(2,1)+2(-1,1)+3(1,7)=(3,24)$.
3. $f(x,y,z)=x(2,1)+y(-1,1)+z(1,7)=(2x-y+z,\ x+y+7z)$.

## Exercice 1.2
Type : application linéaire définie par l'image d'une base · ECUE : ALM · Niveau : maths-s2-alm/1
Formules : linéarité : $f(\alpha u + \beta v) = \alpha f(u) + \beta f(v)$ ; $u = \sum x_ie_i \Rightarrow f(u) = \sum x_if(e_i)$ ; une application linéaire est entièrement déterminée par l'image d'une base ; deux applications linéaires égales sur une base (ou une famille génératrice) sont égales ; si les vecteurs donnés sont liés, les images doivent vérifier la même relation ; s'ils n'engendrent pas l'espace, $f$ n'est pas déterminée

1. $(0,1,2)=2(0,1,1)-(0,1,0)$ donc $f(0,1,2)=2(2,1)-(-1,1)=(5,1)$.
2. $(1,0,2)$ a une première coordonnée non nulle : il n'est pas dans le plan $x=0$ engendré par les trois vecteurs donnés. Ces trois vecteurs ne forment pas une base de $\mathbb R^3$ (ils sont liés : $(0,-1,1)=(0,1,1)-2(0,1,0)$, compatible avec $f$), donc $f(1,0,2)$ n'est pas déterminée.

## Exercice 1.3
Type : application linéaire définie par l'image d'une base · ECUE : ALM · Niveau : maths-s2-alm/1
Formules : linéarité : $f(\alpha u + \beta v) = \alpha f(u) + \beta f(v)$ ; $u = \sum x_ie_i \Rightarrow f(u) = \sum x_if(e_i)$ ; une application linéaire est entièrement déterminée par l'image d'une base ; deux applications linéaires égales sur une base (ou une famille génératrice) sont égales ; si les vecteurs donnés sont liés, les images doivent vérifier la même relation ; s'ils n'engendrent pas l'espace, $f$ n'est pas déterminée

$(1,2,1)+(-1,1,1)=(0,3,2)$, donc par linéarité $f(0,3,2)=(1,1,1)+(-1,1,1)=(0,2,2)\ne(0,0,1)$ : les trois vecteurs sont liés, et les images données sont incompatibles.

## Exercice 1.4
Type : application linéaire définie par l'image d'une base · ECUE : ALM · Niveau : maths-s2-alm/1
Formules : linéarité : $f(\alpha u + \beta v) = \alpha f(u) + \beta f(v)$ ; $u = \sum x_ie_i \Rightarrow f(u) = \sum x_if(e_i)$ ; une application linéaire est entièrement déterminée par l'image d'une base ; deux applications linéaires égales sur une base (ou une famille génératrice) sont égales ; si les vecteurs donnés sont liés, les images doivent vérifier la même relation ; s'ils n'engendrent pas l'espace, $f$ n'est pas déterminée

1. (a) $f=g\iff\forall u\in E,\ f(u)=g(u)$. (b) ($\Rightarrow$) évident. ($\Leftarrow$) Pour $u=\sum\alpha_ie_i$, $f(u)=\sum\alpha_if(e_i)=\sum\alpha_ig(e_i)=g(u)$.
2. D'après 1, $f=g$ dès qu'elles coïncident sur une base. (a) Oui : $\mathbb N^2\ni(1,0),(0,1)$ (base canonique). (b) Oui : le disque contient $(\frac12,0)$ et $(0,\frac12)$ (base). (c) Non : une droite vectorielle ne contient pas de base de $\mathbb R^2$. (d) Oui : la droite contient $(0,1)$ et $(1,3)$, non colinéaires, donc une base.

## Exercice 1.5
Type : matrice d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/5
Formules : colonne $j$ = coordonnées de $f(e_j)$ dans la base d'arrivée ; base canonique de $\mathbb{R}_2[X]$ : $(1, X, X^2)$ ; de $\mathcal{M}_2(\mathbb{R})$ : $E_{11}, E_{12}, E_{21}, E_{22}$ ; taille (dim arrivée) $\times$ (dim départ)

1. (a) $f(x,y)=x(2,3)+y(-1,5)=(2x-y,\ 3x+5y)$. (b) $AU=\begin{pmatrix}2x-y\\3x+5y\end{pmatrix}$ : c'est $f(x,y)$.
2. (a) Oui : $(u_1,u_2)$ est une base. $(x,y)=-y\,u_1+(x+y)\,u_2$, donc $f(x,y)=-y(2,3)+(x+y)(-1,5)=(-x-3y,\ 5x+2y)$. (b) $A\cdot P^{-1}\cdot U$ avec $A=\begin{pmatrix}2&-1\\3&5\end{pmatrix}$ et $P=\begin{pmatrix}1&1\\-1&0\end{pmatrix}$ (matrice des coordonnées de $u_1,u_2$) : $AP^{-1}=\begin{pmatrix}-1&-3\\5&2\end{pmatrix}$.

## Exercice 2.6
Type : matrice d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/5
Formules : colonne $j$ = coordonnées de $f(e_j)$ dans la base d'arrivée ; base canonique de $\mathbb{R}_2[X]$ : $(1, X, X^2)$ ; de $\mathcal{M}_2(\mathbb{R})$ : $E_{11}, E_{12}, E_{21}, E_{22}$ ; taille (dim arrivée) $\times$ (dim départ)

1. $f(x,y)=(2x+y,x-y)$.
   (a) $\begin{pmatrix}2&1\\1&-1\end{pmatrix}$. (b) $f(e_1)=(2,1)=\frac32(1,1)+\frac12(1,-1)$, $f(e_2)=(1,-1)=0\cdot(1,1)+1\cdot(1,-1)$ : $\begin{pmatrix}\frac32&0\\\frac12&1\end{pmatrix}$. (c) $f(1,1)=(3,0)$, $f(1,-1)=(1,2)$ : $\begin{pmatrix}3&1\\0&2\end{pmatrix}$. (d) $f(1,-1)=(1,2)$, $f(1,1)=(3,0)$ : $\begin{pmatrix}1&3\\2&0\end{pmatrix}$. (e) $(3,0)=-3(0,1)+3(1,1)$ et $(1,2)=1(0,1)+1(1,1)$ : $\begin{pmatrix}-3&1\\3&1\end{pmatrix}$.
2. $g(x,y,z)=(3x-y+z,\ y-2z)$. (a) $\begin{pmatrix}3&-1&1\\0&1&-2\end{pmatrix}$. (b) $g(0,1,1)=(0,-1)$, $g(1,0,1)=(4,-2)$, $g(1,1,0)=(2,1)$. Dans la base $((1,-1),(1,1))$ : $(a,b)=\left(\frac{p-q}2,\frac{p+q}2\right)$ pour $(p,q)$ : $(\frac12,-\frac12)$, $(3,1)$, $(\frac12,\frac32)$. Matrice : $\begin{pmatrix}\frac12&3&\frac12\\-\frac12&1&\frac32\end{pmatrix}$.
3. (a) $\begin{pmatrix}1&-2&0&3\end{pmatrix}$. (b) Dans la base $(2)$ les coordonnées sont divisées par $2$ : $\begin{pmatrix}\frac12&-1&0&\frac32\end{pmatrix}$.
4. $\mathrm{Mat}(\ell)=(a_{ij})\in\mathcal M_{n,p}(\mathbb R)$ : la colonne $j$ est l'image de $e_j$.
5. $\varphi(1)=0$, $\varphi(X)=1$, $\varphi(X^2)=2X$, $\varphi(X^3)=3X^2$.
   (a) $\begin{pmatrix}0&1&0&0\\0&0&2&0\\0&0&0&3\\0&0&0&0\end{pmatrix}$. (b) $\varphi(X+1)=1$, $\varphi(X^2-1)=2X$, $\varphi(X^3+X)=3X^2+1$ : $\begin{pmatrix}0&1&0&1\\0&0&2&0\\0&0&0&3\\0&0&0&0\end{pmatrix}$. (c) Base d'arrivée $(1,X+1,X^2-1,X^3+X)$ : $\varphi(X)=1$, $\varphi(X^2)=2(X+1)-2\cdot1$, $\varphi(X^3)=3(X^2-1)+3\cdot1$ : $\begin{pmatrix}0&1&-2&3\\0&0&2&0\\0&0&0&3\\0&0&0&0\end{pmatrix}$.

## Exercice 2.7
Type : changement de base, formule $Y = AX$ · ECUE : ALM · Niveau : maths-s2-alm/9
Formules : $X = PX'$, $P$ = matrice de passage (colonnes = nouveaux vecteurs dans l'ancienne base) ; $X' = P^{-1}X$ ; $f(e_j) = \sum_i a_{i,j}\varepsilon_i$ ; coordonnées de l'image $Y = AX$ ; inverse $2 \times 2$ : $\frac1{ad - bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$

1. $A\in\mathcal M_{3,2}$ : $f\in\mathcal L(\mathbb R^2,\mathbb R^3)$, $f(x,y)=(x+2y,\ 3x+4y,\ 5x+6y)$.
2. $n=1$, $p=2$ : $g\in\mathcal L(\mathbb R_1[X],\mathbb R_2[X])$, $g(a+bX)=(a+2b)+(3a+4b)X+(5a+6b)X^2$.
3. $u=(3,1)=2u_1+u_2$, coordonnées $(2,1)$ : $h(u)=A\begin{pmatrix}2\\1\end{pmatrix}=(4,10,16)$.
4. $(4,6)=1\cdot(1,2)+1\cdot(3,4)$ : $A\begin{pmatrix}1\\1\end{pmatrix}=(3,7,11)$. $\varphi(u)=3+7(X+1)+11(X-1)^2=11X^2-15X+21$ : $a=11$, $b=-15$, $c=21$.

## Exercice 2.8
Type : opérations matricielles, produit, inverse · ECUE : ALM · Niveau : maths-s2-alm/6
Formules : $(\lambda A + \mu B)_{ij} = \lambda a_{ij} + \mu b_{ij}$ ; produit $AB$ défini si (colonnes de $A$) = (lignes de $B$), taille $n \times p$ par $p \times q$ donne $n \times q$ ; $(AB)_{ij} = \sum_k a_{ik}b_{kj}$ ; inverse par pivot de Gauss ; vérification $AA^{-1} = I$

1. $M_f=\begin{pmatrix}-2&4\\1&-1\end{pmatrix}$, $M_g=\begin{pmatrix}1&0&1\\3&-1&2\end{pmatrix}$. $M_fM_g$ est possible ($2\times2$ par $2\times3$) : $M_fM_g=\begin{pmatrix}10&-4&6\\-2&1&-1\end{pmatrix}$. $M_gM_f$ est impossible ($3\ne2$).
2. $f\circ g$ est possible ($\mathbb R^3\xrightarrow{g}\mathbb R^2\xrightarrow{f}\mathbb R^2$) : $f\circ g(x,y,z)=(10x-4y+6z,\ -2x+y-z)$, de matrice $M$. $g\circ f$ est impossible.
3. $M=M_f\times M_g$.

## Exercice 2.9
Type : opérations matricielles, produit, inverse · ECUE : ALM · Niveau : maths-s2-alm/6
Formules : $(\lambda A + \mu B)_{ij} = \lambda a_{ij} + \mu b_{ij}$ ; produit $AB$ défini si (colonnes de $A$) = (lignes de $B$), taille $n \times p$ par $p \times q$ donne $n \times q$ ; $(AB)_{ij} = \sum_k a_{ik}b_{kj}$ ; inverse par pivot de Gauss ; vérification $AA^{-1} = I$

1. (a) $I_n$ (la matrice identité : $\mathrm{id}(e_j)=e_j$). (b) $f\circ\mathrm{id}_E(u)=f(u)=\mathrm{id}_E\circ f(u)$ : $f\circ\mathrm{id}_E=\mathrm{id}_E\circ f=f$, d'où $AI_n=I_nA=A$.
2. (a) Possibles : $f\circ f$ ($\mathbb R^2\to\mathbb R^2$), $g\circ g$, $h\circ g$ ($\mathbb R^3\to\mathbb R^3\to\mathbb R^2$), $f\circ h$ ($\mathbb R^3\to\mathbb R^2\to\mathbb R^2$). Impossibles : $f\circ g$, $g\circ f$, $g\circ h$, $h\circ f$, $h\circ h$.
   (b) $A^2=\begin{pmatrix}7&10\\15&22\end{pmatrix}$ ; $B^2=\begin{pmatrix}8&17&11\\9&16&11\\9&17&10\end{pmatrix}$ ; $h\circ g$ : $CB=\begin{pmatrix}8&18&10\\12&26&16\end{pmatrix}$ ; $f\circ h$ : $AC=\begin{pmatrix}2&8&14\\4&18&32\end{pmatrix}$.

## Exercice 2.10
Type : noyau, image, rang ; matrice d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/5
Formules : $\mathrm{Ker} f$ : résoudre $f(P) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \dim\mathrm{Im} f$ ; injective $\iff \mathrm{Ker} = \{0\}$ ; $\dim\mathrm{Im} = \dim F \Rightarrow$ surjective ; colonne $j$ = coordonnées de $f(e_j)$ dans la base d'arrivée

1. (a) $u=\sum\alpha_ie_i$ donne $f(u)=\sum\alpha_if(e_i)$, donc $\mathrm{Im}(f)=\mathrm{Vect}(f(e_1),\dots,f(e_p))$. (b) $\mathrm{Mat}_{\mathcal B'}$ est linéaire et injective (coordonnées dans une base) : $\sum\alpha_if(e_i)=0_F\iff\sum\alpha_iC_i=0_{n,1}$. (c) Par (a) et (b), $\mathrm{Rg}(f)=\dim\mathrm{Vect}(f(e_i))=\dim\mathrm{Vect}(C_i)=\mathrm{Rg}(A)$ (les relations de dépendance sont les mêmes). (d) D'après (b), $f(\sum\alpha_ie_i)=0_F$ : $\sum\alpha_ie_i\in\mathrm{Ker}(f)$.
2. Rang $2$. $\mathrm{Im}(f)=\mathrm{Vect}(1+X+X^2,\ 2+X^2)$. $\mathrm{Ker}(f)=\mathrm{Vect}(-2+X+X^2)$ (colonne $(-2,1,1)$).
3. $B$ : rang $2$, $\mathrm{Ker}=\{0\}$, $\mathrm{Im}=\mathbb R^2$. $C$ : $h$ à valeurs dans $\mathbb R$, rang $1$, $\mathrm{Im}=\mathbb R$, $\mathrm{Ker}=\mathrm{Vect}(-2+X,\ 1+X^2)$ (colonnes $(-2,1,0)$ et $(1,0,1)$). $D$ : rang $2$, $\mathrm{Ker}=\{0\}$, $\mathrm{Im}=\mathrm{Vect}(1+X+X^2,\ 1+X^2)$.
4. La base $((1,1),(1,-1))$ : rang $1$. $\mathrm{Im}(\ell)$ : colonne $(3,-1)$ donne $3(1,1)-(1,-1)=(2,4)$ : $\mathrm{Im}=\mathrm{Vect}((1,2))$. $\mathrm{Ker}(\ell)$ : $\alpha(1,1)+\beta(1,-1)$ avec $3\alpha+3\beta=0$, soit $(\alpha,\beta)=(-1,1)$ : $-(1,1)+(1,-1)=(0,-2)$ : $\mathrm{Ker}(\ell)=\mathrm{Vect}((0,1))$.

## Exercice 2.11 (⋆)
Type : changement de base, diagonalisation, puissance d'une matrice · ECUE : ALM · Niveau : maths-s2-alm/9
Formules : $\mathrm{Mat}_{\mathcal{B}'}(f) = P^{-1}AP$ avec $P = \mathrm{Mat}_{\mathcal{B}', \mathcal{B}}(id)$ (colonnes = vecteurs de $\mathcal{B}'$ dans $\mathcal{B}$) ; $f(u_i) = \lambda_iu_i \Rightarrow D = \mathrm{diag}(\lambda_i)$ ; $D^n = \mathrm{diag}(\lambda_i^n)$ ; $A = PDP^{-1} \Rightarrow A^n = PD^nP^{-1}$

1. $fg=\begin{pmatrix}3&3\\3&3\end{pmatrix}$ et $gf=\begin{pmatrix}3&3\\3&3\end{pmatrix}$ (les deux composées ont la même matrice).
2. $g^2=2g$ donc $g^{k}=2^{k-1}g$ pour $k\ge1$ : $g^{10}=2^9\begin{pmatrix}1&1\\1&1\end{pmatrix}=512\begin{pmatrix}1&1\\1&1\end{pmatrix}$.
3. Dans la base $((1,1),(1,-1))$ : $g(1,1)=(2,2)=2(1,1)$ et $g(1,-1)=0$ : $\mathrm{diag}(2,0)$. $f(1,1)=(3,3)$ et $f(1,-1)=(-1,1)=-(1,-1)$ : $\mathrm{diag}(3,-1)$.
4. $g^0=I_2$ et $g^k=2^{k-1}\begin{pmatrix}1&1\\1&1\end{pmatrix}$ ($k\ge1$). $f^k=P\,\mathrm{diag}(3^k,(-1)^k)P^{-1}=\dfrac12\begin{pmatrix}3^k+(-1)^k&3^k-(-1)^k\\3^k-(-1)^k&3^k+(-1)^k\end{pmatrix}$ avec $P=\begin{pmatrix}1&1\\1&-1\end{pmatrix}$.

## Exercice 3.12
Type : inverse d'une matrice, application linéaire associée · ECUE : ALM · Niveau : maths-s2-alm/8
Formules : pivot de Gauss sur $AU = V$ ; $A$ inversible $\iff f$ bijective, $\mathrm{Mat}(f^{-1}) = A^{-1}$ ; colonnes de $A$ = images des vecteurs de la base de départ ; $g(aX^2 + bX + c) = ag(X^2) + bg(X) + cg(1)$

1. (a) $A=\begin{pmatrix}1&1&-2\\1&-1&1\\-2&1&-1\end{pmatrix}$, $\det A=1\ne0$ : $f$ est bijective. On résout $f(x,y,z)=(a,b,c)$ : $f^{-1}(a,b,c)=(-b-c,\ -a-5b-3c,\ -a-3b-2c)$.
   (b) $B=\begin{pmatrix}0&-1&-1\\-1&-5&-3\\-1&-3&-2\end{pmatrix}$ et $AB=BA=I_3$ : $B=A^{-1}$.
2. $C^{-1}=\begin{pmatrix}6&-2&3\\2&-1&0\\-5&2&-2\end{pmatrix}$ et $D^{-1}=\begin{pmatrix}0&-2&1\\2&17&-10\\-1&-10&6\end{pmatrix}$ (par le pivot de Gauss ; vérification $CC^{-1}=I_3$, $DD^{-1}=I_3$).

## Exercice 3.13
Type : changement de base, formule $Y = AX$ · ECUE : ALM · Niveau : maths-s2-alm/9
Formules : $X = PX'$, $P$ = matrice de passage (colonnes = nouveaux vecteurs dans l'ancienne base) ; $X' = P^{-1}X$ ; $f(e_j) = \sum_i a_{i,j}\varepsilon_i$ ; coordonnées de l'image $Y = AX$ ; inverse $2 \times 2$ : $\frac1{ad - bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$

1. Les colonnes de $P_{\mathcal B_1,\mathcal B_2}$ sont les coordonnées d'une base : elles sont libres, donc $P$ est inversible. $P^{-1}_{\mathcal B_1,\mathcal B_2}=P_{\mathcal B_2,\mathcal B_1}$ (matrice de passage de $\mathcal B_2$ vers $\mathcal B_1$).
2. (a) $P=\begin{pmatrix}1&0&1\\0&1&1\\1&0&0\end{pmatrix}$. (b) $X=PX'$ et $X'=P^{-1}X$ avec $P^{-1}=\begin{pmatrix}0&0&1\\-1&1&1\\1&0&-1\end{pmatrix}$. (c) $X=\begin{pmatrix}1\\2\\3\end{pmatrix}$ et $X'=P^{-1}X=\begin{pmatrix}3\\4\\-2\end{pmatrix}$ (vérification : $3(1,0,1)+4(0,1,0)-2(1,1,0)=(1,2,3)$).
3. Oui : les formules $X=PX'$ et $X'=P^{-1}X$ valent dans tout espace vectoriel de dimension finie, en utilisant les coordonnées dans deux bases.

## Exercice 3.14 (⋆)
Type : changement de base, formule $Y = AX$ · ECUE : ALM · Niveau : maths-s2-alm/9
Formules : $X = PX'$, $P$ = matrice de passage (colonnes = nouveaux vecteurs dans l'ancienne base) ; $X' = P^{-1}X$ ; $f(e_j) = \sum_i a_{i,j}\varepsilon_i$ ; coordonnées de l'image $Y = AX$ ; inverse $2 \times 2$ : $\frac1{ad - bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$

1. $P=\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ (colonnes : coordonnées des vecteurs de $\mathcal B'$ dans $\mathcal B$).
2. $X=PX'$ et $Y=PY'$. $A$ : $Y=AX$. $B$ (de $\mathcal B'$ vers $\mathcal B$) : $Y=BX'$. $C$ (de $\mathcal B$ vers $\mathcal B'$) : $Y'=CX$.
3. $Y=AX=APX'$ et $Y=BX'$ pour tout $X'$ : $B=AP$. $Y'=P^{-1}Y=P^{-1}AX$ et $Y'=CX$ pour tout $X$ : $C=P^{-1}A$.
4. $Y'=A'X'$ ; $Y'=P^{-1}Y=P^{-1}AX=P^{-1}APX'$ : $A'=P^{-1}AP$. Ici $A'=\begin{pmatrix}\frac32&\frac32\\\frac32&-\frac12\end{pmatrix}$.
