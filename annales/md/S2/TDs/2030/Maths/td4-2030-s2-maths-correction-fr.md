# Feuille de TD — Espaces vectoriels (S2 2026) (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (pas de corrigé officiel). Sujet : `td4-2030-s2-maths-subject-fr.md` (même dossier). Calculs vérifiés avec sympy. 

## Exercice 1.1
Type : vecteurs du plan, combinaisons linéaires (dessin) · ECUE : EV · Niveau : maths-s2-ev/1
Formules : $(x,y) + (x',y') = (x + x', y + y')$ ; $\alpha(x,y) = (\alpha x, \alpha y)$ ; $\{\alpha u\}$ : droite vectorielle dirigée par $u \neq 0$ ; $\{\alpha u + \beta v\}$ avec $u$, $v$ non colinéaires : le plan $\mathbb{R}^2$ (un plan vectoriel dans $\mathbb{R}^3$) ; relation de Chasles pour construire $u + v$

1. $u=(3,1)$ : flèche de $O$ au point $(3,1)$. 2. $2u=(6,2)$, $-u=(-3,-1)$, $-\frac12u=\left(-\frac32,-\frac12\right)$, $0u=(0,0)$. $D=\{\alpha u\}$ est la droite passant par $O$ de direction $u$.
3. $u+v=(1,2)$, $v-u=(-5,0)$, $2u+3v=(0,5)$. $u$ et $v$ ne sont pas colinéaires : $E=\mathbb R^2$ tout entier.
4. $(x,y)+(x',y')=(x+x',y+y')$ et $\alpha\cdot(x,y)=(\alpha x,\alpha y)$ (cohérent avec les constructions : addition = règle du parallélogramme, produit = dilatation).
5. Dans $\mathbb R^3$ : $D$ est une droite vectorielle et $E$ un plan vectoriel (passant par $O$).

## Exercice 1.2
Type : axiomes d'un espace vectoriel (loi externe non standard) · ECUE : EV · Niveau : maths-s2-ev/2
Formules : $\mathbb{R}$-ev : $(E,+)$ groupe commutatif ; $1.u = u$ ; $\alpha.(\beta.u) = (\alpha\beta).u$ ; $(\alpha + \beta).u = \alpha.u + \beta.u$ ; $\alpha.(u + v) = \alpha.u + \alpha.v$ ; un seul axiome en défaut (contre-exemple chiffré) suffit pour conclure que ce n'est pas un ev

1. $+$ : la matrice nulle $\begin{pmatrix}0&0\\0&0\end{pmatrix}$. $\cdot$ : le réel $1$ ($1\cdot A=A$).
2. $(E,+)$ est un groupe commutatif (addition terme à terme). $1\cdot A=A$ ; $\alpha\cdot(\beta\cdot A)=(\alpha\beta)\cdot A$ ; $(\alpha+\beta)\cdot A=\alpha\cdot A+\beta\cdot A$ ; $\alpha\cdot(A+B)=\alpha\cdot A+\alpha\cdot B$ : chaque propriété se vérifie coefficient par coefficient. $E$ est un $\mathbb R$-espace vectoriel ($=\mathcal M_2(\mathbb R)$).

## Exercice 1.3
Type : axiomes d'un espace vectoriel (loi externe non standard) · ECUE : EV · Niveau : maths-s2-ev/2
Formules : $\mathbb{R}$-ev : $(E,+)$ groupe commutatif ; $1.u = u$ ; $\alpha.(\beta.u) = (\alpha\beta).u$ ; $(\alpha + \beta).u = \alpha.u + \beta.u$ ; $\alpha.(u + v) = \alpha.u + \alpha.v$ ; un seul axiome en défaut (contre-exemple chiffré) suffit pour conclure que ce n'est pas un ev

1. $0_E$ est la fonction nulle $x\mapsto0$ sur $I$.
2. « Interne » : le résultat est dans $E$ comme les opérandes. $+:E\times E\to E$, $(f,g)\mapsto f+g$ avec $(f+g)(x)=f(x)+g(x)$.
3. $\alpha f:x\mapsto\alpha f(x)$. L'opération est externe car un des opérandes ($\alpha$) n'est pas dans $E$ : $\cdot:\mathbb R\times E\to E$, $(\alpha,f)\mapsto\alpha f$.
4. Oui : les huit axiomes se vérifient en chaque point $x\in I$ (ce sont ceux de $\mathbb R$). $\mathbb R^I$ est un $\mathbb R$-ev.

## Exercice 1.4
Type : axiomes d'un espace vectoriel (loi externe non standard) · ECUE : EV · Niveau : maths-s2-ev/2
Formules : $\mathbb{R}$-ev : $(E,+)$ groupe commutatif ; $1.u = u$ ; $\alpha.(\beta.u) = (\alpha\beta).u$ ; $(\alpha + \beta).u = \alpha.u + \beta.u$ ; $\alpha.(u + v) = \alpha.u + \alpha.v$ ; un seul axiome en défaut (contre-exemple chiffré) suffit pour conclure que ce n'est pas un ev

1. $1\cdot(u_n)=(1^nu_n)=(u_n)$ : l'élément neutre de la loi externe est le réel $1$.
2. Non. L'axiome $(\alpha+\beta)\cdot u=\alpha\cdot u+\beta\cdot u$ est faux : pour $u=(1,1,1,\dots)$, $\alpha=\beta=1$ au rang $n=2$ : $(\alpha+\beta)^2u_2=4$ alors que $\alpha^2u_2+\beta^2u_2=2$. Ce n'est pas un espace vectoriel.

## Exercice 1.5
Type : axiomes d'un espace vectoriel (loi externe non standard) · ECUE : EV · Niveau : maths-s2-ev/2
Formules : $\mathbb{R}$-ev : $(E,+)$ groupe commutatif ; $1.u = u$ ; $\alpha.(\beta.u) = (\alpha\beta).u$ ; $(\alpha + \beta).u = \alpha.u + \beta.u$ ; $\alpha.(u + v) = \alpha.u + \alpha.v$ ; un seul axiome en défaut (contre-exemple chiffré) suffit pour conclure que ce n'est pas un ev

$\mathbb R^n$ (addition terme à terme, $\alpha(x_i)=(\alpha x_i)$, vecteur nul $(0,\dots,0)$) ; $\mathbb R[X]$ et $\mathbb R_n[X]$ (addition des polynômes, multiplication par un réel, polynôme nul) ; $\mathcal M_{n,p}(\mathbb R)$ (matrice nulle) ; $\mathbb R^{\mathbb N}$ (suites, suite nulle) ; $\mathbb R^I$ et $\mathcal C^k(I,\mathbb R)$ (fonctions, fonction nulle).

## Exercice 2.6
Type : reconnaître un sous-espace vectoriel · ECUE : EV · Niveau : maths-s2-ev/3
Formules : sev : contient 0, stable par addition et multiplication par un scalaire ; contre-exemple $\lambda u \notin E$ ; équation non linéaire ($z^2$) $\Rightarrow$ en général pas un sev ; $\mathrm{Vect}(\dots)$ est toujours un sev

1. (a) $A=\{O\}$ : sev. $B$ : disque, pas un sev (non stable par multiplication : $2u$ sort du disque). $C$ : demi-plan $x\ge0$, pas un sev ($-u$ sort de $C$ si $x>0$). $D$ : axe des abscisses, sev. $E$ : droite $x+y=0$, sev. $F$ : droite $x+y=1$, pas un sev ($O\notin F$).
   (b) Non : tout sev contient $0_E$, deux sev ont toujours $0_E$ en commun.
   (c) $\{0\}$, les droites passant par $O$, et $\mathbb R^2$.
2. Dans $\mathbb R^3$ : $\{0\}$, les droites passant par $O$, les plans passant par $O$, et $\mathbb R^3$.

## Exercice 2.7
Type : reconnaître un sous-espace vectoriel · ECUE : EV · Niveau : maths-s2-ev/3
Formules : sev : contient 0, stable par addition et multiplication par un scalaire ; contre-exemple $\lambda u \notin E$ ; équation non linéaire ($z^2$) $\Rightarrow$ en général pas un sev ; $\mathrm{Vect}(\dots)$ est toujours un sev

1. $E=\mathbb R_2[X]$, polynômes de degré $\le2$. 2. $F=\{aX^2+bX+c,\ (a,b,c)\in\mathbb R^3,\ a\ne0\}$.
3. $F\subset E\subset\mathbb R[X]$ (et $E$ est un sev de $\mathbb R[X]$).
4. Le polynôme nul $0$ : $0\in E$ (pour $a=b=c=0$), $0\notin F$ (il n'est pas de degré exactement $2$).
5. $E$ est stable par $\cdot$ et par $+$. $F$ n'est stable ni par $\cdot$ ($0\cdot X^2=0\notin F$) ni par $+$ ($X^2+(-X^2)=0\notin F$).

## Exercice 2.8
Type : reconnaître un sous-espace vectoriel · ECUE : EV · Niveau : maths-s2-ev/3
Formules : sev : contient 0, stable par addition et multiplication par un scalaire ; contre-exemple $\lambda u \notin E$ ; équation non linéaire ($z^2$) $\Rightarrow$ en général pas un sev ; $\mathrm{Vect}(\dots)$ est toujours un sev

1. Oui. 2. Non ($0\notin F$). 3. Non : $(1,0,0)$ et $(0,1,0)\in F$ mais leur somme $(1,1,0)\notin F$. 4. Non : $(1,0,1)$ et $(1,0,-1)\in F$ mais leur somme $(2,0,0)\notin F$. 5. Oui (condition linéaire en $P$). 6. Oui. 7. Oui (somme et multiple de suites convergentes convergent). 8. Non (la suite nulle n'est pas solution : $0=3\cdot0-1$ est faux). 9. Non (la suite nulle converge). 10. Oui (relation linéaire). 11. Non (non linéaire : si $u$ est solution, $2u$ ne l'est pas en général). 12. Oui ($F=\mathrm{Vect}((2^n),(3^n),(4^n))$). 13. Non ($f$ croissante mais $-f$ décroissante). 14. Oui. 15. Oui. 16. Non (la fonction nulle n'a pas $+\infty$ pour limite). 17. Oui. 18. Oui (l'intégrale est linéaire).

## Exercice 2.9
Type : sous-espaces, intersection, somme directe · ECUE : EV · Niveau : maths-s2-ev/9
Formules : $\mathrm{Vect}(u)$ : droite si $u \neq 0$ ; plan $ax + by + cz = 0$ : exprimer $z$, $G = \mathrm{Vect}(u, v)$ ; $u \in F \cap G$ : paramétrer par $F$ puis injecter l'équation de $G$ ; Grassmann $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $\dim F + \dim G = \dim E$

($\Leftarrow$) Si $F\subset G$, $F\cup G=G$ est un sev (idem si $G\subset F$).
($\Rightarrow$) Si $F\not\subset G$ et $G\not\subset F$ : soit $u\in F\setminus G$ et $v\in G\setminus F$. Si $F\cup G$ est un sev, $u+v\in F\cup G$. Si $u+v\in F$ alors $v=(u+v)-u\in F$ : absurde. Si $u+v\in G$ alors $u\in G$ : absurde. Donc $F\subset G$ ou $G\subset F$. L'assertion est vraie.

## Exercice 2.10
Type : sous-espaces, intersection, somme directe · ECUE : EV · Niveau : maths-s2-ev/9
Formules : $\mathrm{Vect}(u)$ : droite si $u \neq 0$ ; plan $ax + by + cz = 0$ : exprimer $z$, $G = \mathrm{Vect}(u, v)$ ; $u \in F \cap G$ : paramétrer par $F$ puis injecter l'équation de $G$ ; Grassmann $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $\dim F + \dim G = \dim E$

1. $F=\mathrm{Vect}(u)$ : $0\in F$ et $\alpha u+\beta u=(\alpha+\beta)u$ : sev.
2. (a) Oui, comme $F$ ($G=\mathrm{Vect}(v)$, $H=\mathrm{Vect}(w)$). (b) $F$ : droite $y=2x$. $G$ : droite $y=\frac x3$. $H$ : droite $y=2x$ (car $w=-\frac12u$), donc $H=F$.
   (c) $\det(u,v)=2-12=-10\ne0$ : $F+G=\mathbb R^2$, donc $X\in F+G$ : $X=2u-2v$ (graphiquement : projeter $X$ sur $F$ selon la direction de $G$). $F+H=F$ est une droite et $X=(-2,6)\notin F$ ($6\ne2\times(-2)$) : $X\notin F+H$.
   (d) $F+G=\mathbb R^2$ ; $F+H=F=H$ (une droite).

## Exercice 2.11
Type : sous-espaces, intersection, somme directe · ECUE : EV · Niveau : maths-s2-ev/9
Formules : $\mathrm{Vect}(u)$ : droite si $u \neq 0$ ; plan $ax + by + cz = 0$ : exprimer $z$, $G = \mathrm{Vect}(u, v)$ ; $u \in F \cap G$ : paramétrer par $F$ puis injecter l'équation de $G$ ; Grassmann $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $\dim F + \dim G = \dim E$

Non. Dans $\mathbb R^2$ : $F=\mathrm{Vect}((2,4))$, $G=\mathrm{Vect}((3,1))$, $H=\mathrm{Vect}((1,0))$ : $F\oplus G=\mathbb R^2$ et $F\oplus H=\mathbb R^2$ (droites distinctes) mais $G\ne H$. Un supplémentaire n'est pas unique.

## Exercice 2.12
Type : sous-espaces, intersection, somme directe · ECUE : EV · Niveau : maths-s2-ev/9
Formules : $\mathrm{Vect}(u)$ : droite si $u \neq 0$ ; plan $ax + by + cz = 0$ : exprimer $z$, $G = \mathrm{Vect}(u, v)$ ; $u \in F \cap G$ : paramétrer par $F$ puis injecter l'équation de $G$ ; Grassmann $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $\dim F + \dim G = \dim E$

1. $F\cap G=\{(x,-x,0)\}\ne\{0\}$. $F\cap H$ : $(x,0,0)$ avec $x+0=0$ : $F\cap H=\{0\}$.
2. $F\oplus G\ne\mathbb R^3$ car $F\cap G\ne\{0\}$ (et $\dim F+\dim G=4>3$). $F\oplus H=\mathbb R^3$ : $F\cap H=\{0\}$ et $\dim F+\dim H=2+1=3$.

## Exercice 2.13 (⋆)
Type : sous-espaces supplémentaires (fonctions paires et impaires) · ECUE : EV · Niveau : maths-s2-ev/9
Formules : sev : non vide, stable par $\lambda f + g$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $F + G = E$ ; $f = \frac{f(x) + f(-x)}2 + \frac{f(x) - f(-x)}2$ ; paire et impaire $\Rightarrow f = 0$

1. $f$ paire : $\forall x,\ f(-x)=f(x)$ ; impaire : $\forall x,\ f(-x)=-f(x)$.
2. $\mathcal P\oplus\mathcal I=\mathbb R^{\mathbb R}$ : $f=\dfrac{f(x)+f(-x)}2+\dfrac{f(x)-f(-x)}2$, et si $f$ est à la fois paire et impaire alors $f=-f$, $f=0$.
3. $F_A=\{f\in\mathbb R^{\mathbb R},\ f=0\text{ sur }\mathbb R\setminus A\}$ : $f=f\mathbf 1_{\mathbb R\setminus A}+f\mathbf 1_A$ avec le premier terme dans $E_A$ et le second dans $F_A$, et une fonction nulle sur $A$ et hors de $A$ est nulle : $E_A\oplus F_A=\mathbb R^{\mathbb R}$.
4. Dans $\mathbb R[X]$ : polynômes pairs (puissances paires) $\oplus$ polynômes impairs. Dans $\mathbb R_3[X]$ : $\mathrm{Vect}(1,X^2)\oplus\mathrm{Vect}(X,X^3)$ ($2+2=4$).

## Exercice 3.14
Type : familles libres, génératrices, bases · ECUE : EV · Niveau : maths-s2-ev/6
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \forall i, \lambda_i = 0$ ; génératrice : tout vecteur est combinaison linéaire ; base = libre + génératrice ; $\dim \mathbb{R}_n[X] = n + 1$ ; en dimension $n$ : plus de $n$ vecteurs $\Rightarrow$ liée, moins de $n$ $\Rightarrow$ non génératrice, $n$ vecteurs libres $\Rightarrow$ base ; degrés échelonnés $\Rightarrow$ libre

1. Liée (3 vecteurs dans $\mathbb R^2$). 2. Liée : $v_3=v_1+v_2$. 3. Libre : $w_2$ n'est pas colinéaire à $w_1$ ($-8=-4\cdot2$ mais $12\ne-4\cdot3$). 4. Libre ($\det=-6\ne0$). 5. Libre ($\det=2\ne0$). 6. Liée : $R=2P-Q$. 7. Libre : $\alpha P+\beta Q+\gamma R=(\alpha+\beta+\gamma)+(\beta-\gamma)X+(\beta+\gamma)X^2=0$ donne $\beta+\gamma=0$, $\beta-\gamma=0$, puis $\alpha=0$. 8. Libre : en évaluant en $n=0,1,2$, le déterminant de Vandermonde $\det\begin{pmatrix}1&1&1\\2&3&4\\4&9&16\end{pmatrix}=2\ne0$. 9. Libre : $(\alpha+\beta x)e^{2x}+\gamma=0$ ; $x\to-\infty$ donne $\gamma=0$, puis $\alpha+\beta x=0$ pour tout $x$ donne $\alpha=\beta=0$.

## Exercice 3.15
Type : sous-espaces engendrés, inclusion, dimension · ECUE : EV · Niveau : maths-s2-ev/4
Formules : $P \in \mathrm{Vect}(u_1, \dots) \iff P$ combinaison linéaire des $u_i$ ; $F \subset G$ si les générateurs de $F$ sont dans $G$ ; famille génératrice libre = base, $\dim$ = cardinal

1. $C=\{\alpha_1e_1+\dots+\alpha_ne_n,\ (\alpha_i)\in\mathbb R^n\}$ est un sev de $E$, noté $\mathrm{Vect}(e_1,\dots,e_n)$.
2. (a) Oui, ce sont des ensembles de combinaisons linéaires. (b) $F=\mathrm{Vect}(u)$ : droite. $G=\mathrm{Vect}(u,v)$ : plan (non colinéaires). $H=\mathrm{Vect}(u,w)=\mathrm{Vect}(u)$ car $w=-2u$ : droite. (c) $F\subset G$ et $F=H$.
3. $\mathrm{Vect}((1,1))$ : droite $y=x$. $\mathrm{Vect}((-1,1))$ : droite $y=-x$. $\mathrm{Vect}((1,2),(3,4))=\mathbb R^2$. $\mathrm{Vect}((1,1),(2,2))$ : droite $y=x$. $\mathrm{Vect}((1,1),(-1,1),(3,4))=\mathbb R^2$.
4. Une droite ; un plan ; une droite (car $(2,2,0)=2(1,1,0)$).
5. $3=3\cdot1\in F$. $4+3X+4X^2\notin F$ (les coefficients de $X$ et $X^2$ doivent être égaux). $4+3X+3X^2=4\cdot1+3(X+X^2)\in F$. $F=\{a+bX+bX^2,\ (a,b)\in\mathbb R^2\}$.
6. $F=\mathrm{Vect}(1,x)$ est l'espace des fonctions affines $x\mapsto\alpha x+\beta$.

## Exercice 3.16
Type : sous-espaces engendrés, inclusion, dimension · ECUE : EV · Niveau : maths-s2-ev/4
Formules : $P \in \mathrm{Vect}(u_1, \dots) \iff P$ combinaison linéaire des $u_i$ ; $F \subset G$ si les générateurs de $F$ sont dans $G$ ; famille génératrice libre = base, $\dim$ = cardinal

1. $u_1+u_2=(0,3,3)=u_3$ : $\mathcal F$ est liée. $\mathcal F'=(u_1,u_2)$ est libre (non colinéaires), de taille maximale.
2. $u_3=u_1+u_2\in\mathrm{Vect}(u_1,u_2)$ donc $\mathrm{Vect}\,\mathcal F=\mathrm{Vect}\,\mathcal F'$.
3. $\dim=2$.

## Exercice 3.17
Type : écrire un sous-espace sous forme de Vect (système linéaire) · ECUE : EV · Niveau : maths-s2-ev/4
Formules : résoudre le système par pivot de Gauss ; exprimer les inconnues principales en fonction des inconnues libres ; factoriser chaque paramètre : $\{(x,y,z)\} = \{t\,u,\ t \in \mathbb{R}\} = \mathrm{Vect}(u)$ ; nombre de paramètres libres = dimension

1. $E=\mathrm{Vect}((2,1))$, $\dim1$. 2. $F=\mathrm{Vect}((1,1,0))$, $\dim1$. 3. $G=\{(x,x,z)\}=\mathrm{Vect}((1,1,0),(0,0,1))$, $\dim2$. 4. $H=\{(y-z,y,z)\}=\mathrm{Vect}((1,1,0),(-1,0,1))$, $\dim2$. 5. $x=z$ et $y=-3x$ : $I=\mathrm{Vect}((1,-3,1,0),(0,0,0,1))$, $\dim2$. 6. $t=z=-(x+y)$ : $J=\mathrm{Vect}((1,0,-1,-1),(0,1,-1,-1))$, $\dim2$. 7. $K=\mathrm{Vect}(X,X^2)$, $\dim2$. 8. $P=aX+bX^2$, $P'(1)=a+2b=0$ : $L=\mathrm{Vect}(X^2-2X)$, $\dim1$. 9. $M=\mathrm{Vect}(X^2,X^3)$, $\dim2$. (Dans chaque cas la famille génératrice trouvée est libre, donc c'est une base et sa taille donne la dimension.)

## Exercice 3.18
Type : familles libres, génératrices, bases · ECUE : EV · Niveau : maths-s2-ev/6
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \forall i, \lambda_i = 0$ ; génératrice : tout vecteur est combinaison linéaire ; base = libre + génératrice ; $\dim \mathbb{R}_n[X] = n + 1$ ; en dimension $n$ : plus de $n$ vecteurs $\Rightarrow$ liée, moins de $n$ $\Rightarrow$ non génératrice, $n$ vecteurs libres $\Rightarrow$ base ; degrés échelonnés $\Rightarrow$ libre

1. Base canonique de $\mathbb R^2$ : $((1,0),(0,1))$ ($\dim2$) ; de $\mathbb R^3$ : $((1,0,0),(0,1,0),(0,0,1))$ ($\dim3$) ; de $\mathbb R_n[X]$ : $(1,X,\dots,X^n)$ ($\dim n+1$).
2. Dans $\mathbb R^2$ : génératrice $\Rightarrow$ au moins $2$ vecteurs ; libre $\Rightarrow$ au plus $2$ ; plus de $2$ vecteurs $\Rightarrow$ liée. Cela se généralise en dimension $n$ : génératrice $\ge n$ vecteurs, libre $\le n$, plus de $n$ vecteurs $\Rightarrow$ liée, $n$ vecteurs libres (ou générateurs) forment une base.

## Exercice 3.19
Type : familles libres, génératrices, bases ; coordonnées · ECUE : EV · Niveau : maths-s2-ev/7
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \lambda_i = 0$ ; en dimension $n$, une famille libre de $n$ vecteurs est une base ; plus de $n$ vecteurs $\Rightarrow$ liée ; coordonnées : résoudre $P = \alpha Q_1 + \beta Q_2 + \gamma Q_3$ en identifiant les coefficients

1. $\det\begin{pmatrix}2&-1\\1&1\end{pmatrix}=3\ne0$ : deux vecteurs non colinéaires en dimension $2$ : base.
2. Graphiquement $u=2\varepsilon_1-\varepsilon_2$ : coordonnées $(2,-1)$.
3. $2(2,1)-(-1,1)=(4+1,2-1)=(5,1)$ ✓.

## Exercice 3.20
Type : familles libres, génératrices, bases ; coordonnées · ECUE : EV · Niveau : maths-s2-ev/7
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \lambda_i = 0$ ; en dimension $n$, une famille libre de $n$ vecteurs est une base ; plus de $n$ vecteurs $\Rightarrow$ liée ; coordonnées : résoudre $P = \alpha Q_1 + \beta Q_2 + \gamma Q_3$ en identifiant les coefficients

1. $\det(u_1,u_2,u_3)=4\ne0$ : base. $u=a u_1+bu_2+cu_3$ : $a=\dfrac32$, $b=\dfrac52$, $c=2$ (vérification : $\frac32(1,1,-1)+\frac52(-1,1,1)+2(1,-1,1)=(1,2,3)$).
2. $\mathcal F$ est libre (degrés $0,1,2$) avec $3=\dim\mathbb R_2[X]$ vecteurs : base. $P=X+2=1\cdot(X+1)+1\cdot1$ : coordonnées $(1,1,0)$.

## Exercice 3.21
Type : familles libres, génératrices, bases · ECUE : EV · Niveau : maths-s2-ev/6
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \forall i, \lambda_i = 0$ ; génératrice : tout vecteur est combinaison linéaire ; base = libre + génératrice ; $\dim \mathbb{R}_n[X] = n + 1$ ; en dimension $n$ : plus de $n$ vecteurs $\Rightarrow$ liée, moins de $n$ $\Rightarrow$ non génératrice, $n$ vecteurs libres $\Rightarrow$ base ; degrés échelonnés $\Rightarrow$ libre

a. libre ou liée (pas génératrice). b. génératrice ou liée (pas libre). c. liée. d. libre, génératrice ou liée.

## Exercice 3.22
Type : sous-espaces, intersection, somme directe · ECUE : EV · Niveau : maths-s2-ev/9
Formules : $\mathrm{Vect}(u)$ : droite si $u \neq 0$ ; plan $ax + by + cz = 0$ : exprimer $z$, $G = \mathrm{Vect}(u, v)$ ; $u \in F \cap G$ : paramétrer par $F$ puis injecter l'équation de $G$ ; Grassmann $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $\dim F + \dim G = \dim E$

1. $G=\mathrm{Vect}((1,1,1))$ et $1-1+1=1\ne0$ donc $G\cap F=\{0\}$ ; $\dim F+\dim G=2+1=3$ : supplémentaires.
2. $(1,1,0)\in F\cap G$ : $F\cap G\ne\{0\}$ : non supplémentaires ($2+2>3$).
3. $F=\mathrm{Vect}((1,1,0))$, $G=\mathrm{Vect}((1,0,1))$ : $\dim F+\dim G=2\ne3$ : $F+G\ne\mathbb R^3$, non supplémentaires.

## Exercice 3.23 (⋆)
Type : sous-espaces, intersection, somme directe · ECUE : EV · Niveau : maths-s2-ev/9
Formules : $\mathrm{Vect}(u)$ : droite si $u \neq 0$ ; plan $ax + by + cz = 0$ : exprimer $z$, $G = \mathrm{Vect}(u, v)$ ; $u \in F \cap G$ : paramétrer par $F$ puis injecter l'équation de $G$ ; Grassmann $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $\dim F + \dim G = \dim E$

1. Pour $(x,y,z)\in\mathbb R^3$ : $f=(0,z,z)\in F$ ($z=0+z$) et $(x,y,z)-f=(x,y-z,0)\in G$ : $F+G=\mathbb R^3$. Mais $(1,1,0)\in F\cap G$ : $F\cap G\ne\{0\}$, la somme n'est pas directe.
2. $F'=\mathrm{Vect}((0,1,1))\subset F$ : $F'\cap G=\{0\}$ (un vecteur $(0,t,t)$ de $G$ a $t=0$) et $\dim F'+\dim G=1+2=3$ : $F'\oplus G=\mathbb R^3$.
