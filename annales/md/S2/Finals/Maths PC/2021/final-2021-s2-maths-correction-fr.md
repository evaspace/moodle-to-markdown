# Partiel 2 (S2) — juin 2017 (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (pas de corrigé officiel). Sujet : `final-2021-s2-maths-subject-fr.md` (même dossier). Calculs vérifiés avec sympy. 

## Exercice 1 (2 points)
Type : inverse d'une matrice · ECUE : ALM · Niveau : maths-s2-alm/8
Formules : $A$ inversible $\iff \det A \neq 0$ ; pivot de Gauss sur $(A \mid I_n) \to (I_n \mid A^{-1})$ ; ou $A^{-1} = \frac1{\det A}{}^t\mathrm{Com}(A)$ ; vérifier $AA^{-1} = I_n$ ; $2 \times 2$ : $\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1} = \frac1{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$

$\det A=1$ et, par la méthode du pivot (ou des cofacteurs) : $A^{-1}=\begin{pmatrix}1&1&1\\1&0&-1\\1&-1&-4\end{pmatrix}$. Vérification : $AA^{-1}=I_3$ (première ligne : $-1+3-1=1$, $-1+0+1=0$, $-1-3+4=0$).

## Exercice 2 (4,5 points)
Type : décomposition en éléments simples · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/8
Formules : si $\deg N \geqslant \deg D$ : division euclidienne, partie entière ; pôle simple $a$ : $\frac{c}{X - a}$ avec $c = \left[(X - a)F\right](a)$ ; pôle double : $\frac{c_1}{X-a} + \frac{c_2}{(X-a)^2}$ ; facteur irréductible $X^2 + 1$ : $\frac{bX + c}{X^2 + 1}$ ; identifier en évaluant (ex. $X = 0$) ou par limite de $xF(x)$ en $+\infty$

1. $F=\dfrac a{X+1}+\dfrac b{X-1}+\dfrac c{X-3}$ : $a=\dfrac{1}{(-2)(-4)}=\dfrac18$, $b=\dfrac{3}{2\cdot(-2)}=-\dfrac34$, $c=\dfrac{13}{4\cdot2}=\dfrac{13}8$. $F=\dfrac1{8(X+1)}-\dfrac3{4(X-1)}+\dfrac{13}{8(X-3)}$.
2. Division euclidienne ($\deg$ numérateur $>$ dénominateur) : $X^3-X-1=(X^2+4X+3)(X-4)+12X+11$, d'où $G=X-4+\dfrac{12X+11}{(X+1)(X+3)}=X-4-\dfrac1{2(X+1)}+\dfrac{25}{2(X+3)}$.
3. $H=\dfrac a{X-2}+\dfrac{bX+c}{X^2+1}$ : $a=\dfrac{4-2-1}{5}=\dfrac15$, puis $b=-a+1=\dfrac45$ et $c=\dfrac35$. $H=\dfrac1{5(X-2)}+\dfrac{4X+3}{5(X^2+1)}$.

## Exercice 3 (3 points)
Type : matrice d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/5
Formules : colonne $j$ = coordonnées de $f(e_j)$ dans la base d'arrivée ; base canonique de $\mathbb{R}_2[X]$ : $(1, X, X^2)$ ; de $\mathcal{M}_2(\mathbb{R})$ : $E_{11}, E_{12}, E_{21}, E_{22}$ ; taille (dim arrivée) $\times$ (dim départ)

1. Pour $P=a+bX+cX^2$ : $f(P)=(a+b+c,\ a+2b+4c)$ : $\mathrm{Mat}(f)=\begin{pmatrix}1&1&1\\1&2&4\end{pmatrix}$.
2. Avec la base canonique $(E_{11},E_{12},E_{21},E_{22})$ de $\mathcal M_2(\mathbb R)$ : $u(x,y,z)=(x+y,\ y+z,\ x+z,\ 0)$ : $\mathrm{Mat}(u)=\begin{pmatrix}1&1&0\\0&1&1\\1&0&1\\0&0&0\end{pmatrix}$.

## Exercice 4 (3 points)
Type : noyau et image d'un endomorphisme (inclusions) · ECUE : ALM · Niveau : maths-s2-alm/12
Formules : $\mathrm{Ker} f = \{x, f(x) = 0\}$ ; $\mathrm{Im} f = \{f(x)\}$ ; $f(0) = 0$ ; $x \in \mathrm{Ker} f \Rightarrow f^2(x) = f(0) = 0$ ; $f^2(x) = f(f(x)) \in \mathrm{Im} f$ ; double implication par éléments

1. Si $f(x)=0$ alors $f^2(x)=f(0)=0$.
2. Si $y=f^2(x)=f(f(x))$ alors $y=f(z)$ avec $z=f(x)$ : $y\in\mathrm{Im}(f)$.
3. ($\Rightarrow$) Soit $x\in\mathrm{Ker}(f^2)$ : $f(x)\in\mathrm{Ker}(f)\cap\mathrm{Im}(f)=\{0\}$, donc $x\in\mathrm{Ker}(f)$. Avec la question 1 : égalité. ($\Leftarrow$) Soit $y\in\mathrm{Im}(f)\cap\mathrm{Ker}(f)$ : $y=f(x)$ et $f(y)=f^2(x)=0$, donc $x\in\mathrm{Ker}(f^2)=\mathrm{Ker}(f)$ et $y=f(x)=0$.

## Exercice 5 (2 points)
Type : familles libres, génératrices, bases · ECUE : EV · Niveau : maths-s2-ev/6
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \forall i, \lambda_i = 0$ ; génératrice : tout vecteur est combinaison linéaire ; base = libre + génératrice ; $\dim \mathbb{R}_n[X] = n + 1$ ; en dimension $n$ : plus de $n$ vecteurs $\Rightarrow$ liée, moins de $n$ $\Rightarrow$ non génératrice, $n$ vecteurs libres $\Rightarrow$ base ; degrés échelonnés $\Rightarrow$ libre

1. Non : $\dim\mathbb R_2[X]=3$ et une famille de 2 vecteurs ne peut pas l'engendrer.
2. Non : 4 vecteurs dans un espace de dimension 3 forment une famille liée (explicitement $2X^2=2(X^2+3)-6=2(X^2+3)-3\cdot2$).
3. Oui : degrés échelonnés $0,1,2$, donc libre ; 3 vecteurs libres en dimension 3 : base.

## Exercice 6 (3 points)
Type : puissance d'une matrice (binôme, nilpotente) · ECUE : ALM · Niveau : maths-s2-alm/12
Formules : $J$ nilpotente : $J^3 = 0$ ; si $AB = BA$ : $(A + B)^n = \sum_k \binom nk A^kB^{n-k}$ ; $I$ commute avec tout ; $(I + N)^n = I + nN + \binom n2 N^2$ si $N^3 = 0$

1. $J^2=\begin{pmatrix}0&0&1\\0&0&0\\0&0&0\end{pmatrix}$ et $J^k=0$ pour $k\ge3$ ($J^3=J\cdot J^2=0$).
2. $A=I+aJ+bJ^2$.
3. $I$ et $N=aJ+bJ^2$ commutent. $N^2=a^2J^2$ et $N^k=0$ pour $k\ge3$. Binôme : $A^n=I+nN+\dbinom n2N^2=I+naJ+\left(nb+\dfrac{n(n-1)}2a^2\right)J^2$, soit $A^n=\begin{pmatrix}1&na&nb+\frac{n(n-1)}2a^2\\0&1&na\\0&0&1\end{pmatrix}$.

## Exercice 7 (4 points)
Type : noyau, image, rang d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/3
Formules : linéaire : $f(\lambda u + v) = \lambda f(u) + f(v)$ ; $\mathrm{Ker} f$ : résoudre $f(x) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \mathrm{rg} f$ ; $\mathrm{rg} f = \dim F \Rightarrow \mathrm{Im} f = F$ (surjective) ; $\mathrm{Im} f = \mathrm{Vect}(f(e_1), \dots, f(e_n))$

1. Chaque coordonnée est combinaison linéaire de $(x,y,z,t)$ : $f(\lambda u+v)=\lambda f(u)+f(v)$.
2. $f(x,y,z,t)=0\iff y=-x,\ z=-2x-y=-x,\ t=-x$ : $\mathrm{Ker}(f)=\mathrm{Vect}\big((1,-1,-1,-1)\big)$, $\dim\mathrm{Ker}(f)=1$.
3. Rang : $\dim\mathrm{Im}(f)=4-1=3=\dim\mathbb R^3$ : $\mathrm{Im}(f)=\mathbb R^3$ ($f$ est surjective).
