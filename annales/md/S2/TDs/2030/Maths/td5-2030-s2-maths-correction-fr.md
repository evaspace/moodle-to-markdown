# Feuille de TD — Applications linéaires (S2 2026) (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (pas de corrigé officiel). Sujet : `td5-2030-s2-maths-subject-fr.md` (même dossier). Calculs vérifiés avec sympy. 

## Exercice 1.1
Type : application linéaire (caractérisation) · ECUE : ALM · Niveau : maths-s2-alm/1
Formules : $f$ linéaire $\Rightarrow f(0) = 0$ et $f(2x) = 2f(x)$ (conditions nécessaires) ; réciproquement vérifier $f(\lambda x + y) = \lambda f(x) + f(y)$ ; les applications linéaires de $\mathbb{R}$ dans $\mathbb{R}$ sont $x \mapsto bx$

1. $f$ linéaire : $f(x)=ax$ ($\forall(u,v),\ f(u+v)=f(u)+f(v)$ et $f(\alpha u)=\alpha f(u)$). Représentation : une droite passant par l'origine.
2. $f(u+v)=f(u)+f(v)$, $f(\alpha u)=\alpha f(u)$, $f(0)=0$.
3. $g(x)=ax+b$ : $g(u+v)=a(u+v)+b\ne g(u)+g(v)$ si $b\ne0$ ; $g(\alpha u)\ne\alpha g(u)$ si $b\ne0$ ; $g(0)=b$. Droite ne passant pas par l'origine si $b\ne0$ : $g$ n'est linéaire que si $b=0$.
4. $h(x)=x^2$ : $h(u+v)=u^2+2uv+v^2\ne h(u)+h(v)$ en général, $h(\alpha u)=\alpha^2h(u)$, $h(0)=0$. Parabole : $h$ n'est pas linéaire.

## Exercice 1.2
Type : application linéaire (caractérisation) · ECUE : ALM · Niveau : maths-s2-alm/1
Formules : $f$ linéaire $\Rightarrow f(0) = 0$ et $f(2x) = 2f(x)$ (conditions nécessaires) ; réciproquement vérifier $f(\lambda x + y) = \lambda f(x) + f(y)$ ; les applications linéaires de $\mathbb{R}$ dans $\mathbb{R}$ sont $x \mapsto bx$

$f_1$ oui. $f_2$ non ($f_2(0,0,0)=(0,2)\ne0$). $f_3$ oui. $f_4$ non (terme $xy$ : $f_4(2(1,1))\ne2f_4(1,1)$). $f_5$ oui ($f_5(X)=AX$). $f_6$ oui (chaque coefficient est combinaison linéaire de $a,b,c,d$). $f_7$ oui. $f_8$ non ($f_8(-u)\ne-f_8(u)$ si $u_1\ne0$). $f_9$ non ($f_9(0)=-X^2\ne0$). $f_{10}$ oui. $\varphi$ oui (linéarité de l'intégrale).

## Exercice 2.3
Type : noyau, image, rang d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/3
Formules : linéaire : $f(\lambda u + v) = \lambda f(u) + f(v)$ ; $\mathrm{Ker} f$ : résoudre $f(x) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \mathrm{rg} f$ ; $\mathrm{rg} f = \dim F \Rightarrow \mathrm{Im} f = F$ (surjective) ; $\mathrm{Im} f = \mathrm{Vect}(f(e_1), \dots, f(e_n))$

1. $\mathrm{Ker}(f)=\{u\in E,\ f(u)=0_F\}$ et $\mathrm{Im}(f)=\{f(u),\ u\in E\}$. $\mathrm{Ker}(f)$ : $f(0)=0$, et si $f(u)=f(v)=0$, $f(\alpha u+v)=0$ : sev de $E$. $\mathrm{Im}(f)$ : $0=f(0)\in\mathrm{Im}(f)$ ; $\alpha f(u)+f(v)=f(\alpha u+v)\in\mathrm{Im}(f)$ : sev de $F$.
2. (a) $f(\lambda(x,y)+(x',y'))=(\lambda x+x'+\lambda y+y',0)=\lambda f(x,y)+f(x',y')$. (b) $\mathrm{Ker}(f)=\{x+y=0\}=\mathrm{Vect}((1,-1))$ : droite $y=-x$. (c) $\mathrm{Im}(f)=\{(t,0)\}=\mathrm{Vect}((1,0))$ : axe des abscisses. (d) Deux droites vectorielles.

## Exercice 2.4
Type : noyau, image, rang d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/3
Formules : linéaire : $f(\lambda u + v) = \lambda f(u) + f(v)$ ; $\mathrm{Ker} f$ : résoudre $f(x) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \mathrm{rg} f$ ; $\mathrm{rg} f = \dim F \Rightarrow \mathrm{Im} f = F$ (surjective) ; $\mathrm{Im} f = \mathrm{Vect}(f(e_1), \dots, f(e_n))$

$f_1$ : $\mathrm{Ker}=\mathrm{Vect}((1,1,-1))$, $\mathrm{Im}=\mathbb R^2$.
$f_2$ : $\mathrm{Ker}=\mathrm{Vect}((0,1,0))$, $\mathrm{Im}=\mathrm{Vect}((1,1,0),(0,1,1))$.
$f_3$ : $\mathrm{Ker}=\{0\}$, $\mathrm{Im}=\mathrm{Vect}((1,2,0),(0,1,3))$.
$f_4$ sur $\mathbb R_2[X]$ : $\mathrm{Ker}=\mathrm{Vect}(1)$ (constantes), $\mathrm{Im}=\mathbb R_1[X]=\mathrm{Vect}(1,X)$. Sur $\mathbb R[X]$ : $\mathrm{Ker}=\mathrm{Vect}(1)$, $\mathrm{Im}=\mathbb R[X]$ (tout polynôme a une primitive).
$f_5$ : $\mathrm{Ker}=\{P,\ P(0)=P(1)=0\}=\{X(X-1)Q,\ Q\in\mathbb R[X]\}$ (de dimension infinie), $\mathrm{Im}=\mathbb R^2$ ($P=a+(b-a)X$ donne $(a,b)$).

## Exercice 2.5
Type : injectivité et noyau · ECUE : ALM · Niveau : maths-s2-alm/2
Formules : $f$ linéaire : $f(0) = 0$, $f(x) - f(y) = f(x - y)$ ; $f$ injective $\iff \mathrm{Ker} f = \{0\}$

1. (a) $f(0)=0$ et $f$ injective : $f(u)=0=f(0)\Rightarrow u=0$. (b) $f(u)=f(v)\Rightarrow f(u-v)=0\Rightarrow u-v\in\mathrm{Ker}(f)=\{0\}\Rightarrow u=v$. (c) (a) donne $\Rightarrow$ (avec $0\in\mathrm{Ker}$) et (b) donne $\Leftarrow$.
2. $f$ surjective $\iff\forall y\in F,\ \exists x,\ y=f(x)\iff F\subset\mathrm{Im}(f)\iff\mathrm{Im}(f)=F$ (l'autre inclusion est toujours vraie).

## Exercice 2.6
Type : injectivité et noyau · ECUE : ALM · Niveau : maths-s2-alm/2
Formules : $f$ linéaire : $f(0) = 0$, $f(x) - f(y) = f(x - y)$ ; $f$ injective $\iff \mathrm{Ker} f = \{0\}$

$f_1$ : non injective, surjective. $f_2$ : non injective, non surjective. $f_3$ : injective, non surjective. $f_4$ sur $\mathbb R_2[X]$ : non injective, non surjective ; sur $\mathbb R[X]$ : non injective, surjective. $f_5$ : non injective, surjective.

## Exercice 3.7
Type : noyau, image, rang d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/3
Formules : linéaire : $f(\lambda u + v) = \lambda f(u) + f(v)$ ; $\mathrm{Ker} f$ : résoudre $f(x) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \mathrm{rg} f$ ; $\mathrm{rg} f = \dim F \Rightarrow \mathrm{Im} f = F$ (surjective) ; $\mathrm{Im} f = \mathrm{Vect}(f(e_1), \dots, f(e_n))$

$f_1$ : $3=1+2$. $f_2$ : $3=1+2$. $f_3$ : $2=0+2$. $f_4$ sur $\mathbb R_2[X]$ : $3=1+2$. Les cas $f_4$ sur $\mathbb R[X]$ et $f_5$ ont un espace de départ de dimension infinie : le théorème du rang (dimension finie) ne s'applique pas.

## Exercice 3.8
Type : noyau, image, rang d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/3
Formules : linéaire : $f(\lambda u + v) = \lambda f(u) + f(v)$ ; $\mathrm{Ker} f$ : résoudre $f(x) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \mathrm{rg} f$ ; $\mathrm{rg} f = \dim F \Rightarrow \mathrm{Im} f = F$ (surjective) ; $\mathrm{Im} f = \mathrm{Vect}(f(e_1), \dots, f(e_n))$

1. $f(P)=0\iff a+c=0$ et $a+2b+3c=0$, soit $a=-c$, $b=-c$ : $\mathrm{Ker}(f)=\mathrm{Vect}(-X^2-X+1)$, $\dim=1$.
2. Théorème du rang : $\dim\mathrm{Im}(f)=3-1=2$.
3. $\mathrm{Im}(f)\subset\mathbb R^2$ de dimension $2$ : $\mathrm{Im}(f)=\mathbb R^2$.
4. Non injective ($\mathrm{Ker}\ne\{0\}$), surjective, non bijective.

## Exercice 3.9
Type : noyau, image, rang d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/3
Formules : linéaire : $f(\lambda u + v) = \lambda f(u) + f(v)$ ; $\mathrm{Ker} f$ : résoudre $f(x) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \mathrm{rg} f$ ; $\mathrm{rg} f = \dim F \Rightarrow \mathrm{Im} f = F$ (surjective) ; $\mathrm{Im} f = \mathrm{Vect}(f(e_1), \dots, f(e_n))$

1. $f(x,y,z)=0\iff6x-4y-4z=0,\ 5x-3y-4z=0,\ x=y$ : $x=y$ puis $2x=4z$, $z=\frac x2$ : $\mathrm{Ker}(f)=\mathrm{Vect}((2,2,1))$, $\dim=1$.
2. $\dim\mathrm{Im}(f)=3-1=2$.
3. $u=(1,1,0)$ : $f(u)=(2,2,0)=2u$. $v=(0,1,-1)$ : $f(v)=(0,1,-1)=v$.
4. $f(u)=2u$ et $f(v)=v$ sont dans $\mathrm{Im}(f)$, donc $u,v\in\mathrm{Im}(f)$ ; ils ne sont pas colinéaires : famille libre de $2=\dim\mathrm{Im}(f)$ vecteurs : base.

## Exercice 3.10
Type : théorème du rang (conséquences : injectif, surjectif, bijectif) · ECUE : ALM · Niveau : maths-s2-alm/4
Formules : théorème du rang : $\dim E = \dim \mathrm{Ker}(f) + \dim \mathrm{Im}(f)$ ; injective $\iff \mathrm{Ker}(f) = \{0_E\}$ ; surjective $\iff \mathrm{Im}(f) = F$ ; si $\dim E = \dim F$ : injective $\iff$ surjective $\iff$ bijective ; $\dim E > \dim F \Rightarrow$ pas injective ; $\dim E < \dim F \Rightarrow$ pas surjective ; un polynôme de degré $\leqslant n$ ayant $n + 1$ racines est nul

1. (a) $f$ injective : $\dim\mathrm{Ker}=0$, donc $\dim\mathrm{Im}(f)=\dim E$ et $\mathrm{Im}(f)\subset E$ : $\mathrm{Im}(f)=E$. (b) $f$ surjective : $\dim\mathrm{Im}(f)=\dim E$, donc $\dim\mathrm{Ker}(f)=0$. (c) Par (a) et (b) : injective $\iff$ surjective $\iff$ bijective ; et injective $\iff\mathrm{Ker}=\{0\}$, surjective $\iff\mathrm{Im}=E$.
2. Si $\dim E>\dim F$ : $f$ n'est pas injective. Si $\dim E<\dim F$ : $f$ n'est pas surjective. Si $\dim E=\dim F$ : injective $\iff$ surjective $\iff$ bijective.

## Exercice 3.11 (⋆)
Type : théorème du rang (conséquences : injectif, surjectif, bijectif) · ECUE : ALM · Niveau : maths-s2-alm/4
Formules : théorème du rang : $\dim E = \dim \mathrm{Ker}(f) + \dim \mathrm{Im}(f)$ ; injective $\iff \mathrm{Ker}(f) = \{0_E\}$ ; surjective $\iff \mathrm{Im}(f) = F$ ; si $\dim E = \dim F$ : injective $\iff$ surjective $\iff$ bijective ; $\dim E > \dim F \Rightarrow$ pas injective ; $\dim E < \dim F \Rightarrow$ pas surjective ; un polynôme de degré $\leqslant n$ ayant $n + 1$ racines est nul

1. Si $f(P)=0$, $P$ (de degré $\le n$) a $n+1$ racines distinctes : $P=0$. Donc $f$ est injective ; $\dim\mathbb R_n[X]=n+1=\dim\mathbb R^{n+1}$ : bijective.
2. Étant donnés $n+1$ points d'abscisses distinctes $x_i$ et d'ordonnées $y_i$, il existe un unique $P\in\mathbb R_n[X]$ tel que $f(P)=(y_0,\dots,y_n)$ : interpolation de Lagrange.

## Exercice 3.12
Type : noyau, image, rang d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/3
Formules : linéaire : $f(\lambda u + v) = \lambda f(u) + f(v)$ ; $\mathrm{Ker} f$ : résoudre $f(x) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \mathrm{rg} f$ ; $\mathrm{rg} f = \dim F \Rightarrow \mathrm{Im} f = F$ (surjective) ; $\mathrm{Im} f = \mathrm{Vect}(f(e_1), \dots, f(e_n))$

1. $(\lambda P+Q)'=\lambda P'+Q'$ et $P'\in\mathbb R[X]$ : endomorphisme.
2. $\mathrm{Ker}(f)=\mathrm{Vect}(1)$ (constantes). $\mathrm{Im}(f)=\mathbb R[X]$ (tout polynôme a une primitive).
3. Non injective, surjective.
4. En dimension infinie, « surjective » n'entraîne pas « injective » : l'équivalence de l'exercice 3.10 est propre à la dimension finie.

## Exercice 4.13
Type : projecteur, noyau et image · ECUE : ALM · Niveau : maths-s2-alm/10
Formules : projecteur $\iff f \circ f = f$ ; $E = \mathrm{Ker} f \oplus \mathrm{Im} f$ ; $f = id$ sur $\mathrm{Im} f$, $0$ sur $\mathrm{Ker} f$ ; matrice dans une base adaptée $\mathrm{diag}(0, \dots, 0, 1, \dots, 1)$

1. $D_1=\mathrm{Vect}((1,1))$ et $D_2=\mathrm{Vect}((1,-2))$ sont deux droites vectorielles distinctes : $\mathbb R^2=D_1\oplus D_2$ (supplémentaires).
2. $v=(1,4)=a(1,1)+b(1,-2)$ : $a+b=1$, $a-2b=4$, donc $a=2$, $b=-1$. $v_1=(2,2)$, $v_2=(-1,2)$ et $v=v_1+v_2$.
3. $v_1=(2,2)$ et $v_2=(-1,2)$ : leur somme redonne $v$.
4. $p(v_1)=v_1$ (déjà dans $D_1$) et $p(v_2)=0$.
5. Le symétrique de $v$ par rapport à $D_1$ parallèlement à $D_2$ est $v_1-v_2=(3,0)$.

## Exercice 4.14
Type : projecteur, noyau et image · ECUE : ALM · Niveau : maths-s2-alm/10
Formules : projecteur $\iff f \circ f = f$ ; $E = \mathrm{Ker} f \oplus \mathrm{Im} f$ ; $f = id$ sur $\mathrm{Im} f$, $0$ sur $\mathrm{Ker} f$ ; matrice dans une base adaptée $\mathrm{diag}(0, \dots, 0, 1, \dots, 1)$

$p_1$ : $\mathrm{Ker}=\mathrm{Vect}((0,1))$, $\mathrm{Im}=\mathrm{Vect}((1,0))$. $p_2$ : $\mathrm{Ker}=\mathrm{Vect}((1,1))$, $\mathrm{Im}=\mathrm{Vect}((1,0))$.
2. Pour chacune, $\mathrm{Ker}$ et $\mathrm{Im}$ sont deux droites distinctes : somme directe égale à $\mathbb R^2$.
3. $p(v)=v$ ($v=p(x)\in\mathrm{Im}$ et $p\circ p=p$), $p(w)=0$ : $p(u)=v$ (le projeté de $u$ sur $\mathrm{Im}$ parallèlement à $\mathrm{Ker}$).
4. Elle projette $u$ sur $\mathrm{Im}(p)$ parallèlement à $\mathrm{Ker}(p)$.
5. $p_1(p_1(x,y))=p_1(x,0)=(x,0)$ ; $p_2(p_2(x,y))=p_2(x-y,0)=(x-y,0)$ : $p\circ p=p$.
6. $f(u)=2v-u=2v-v-w=v-w$ : symétrie par rapport à $\mathrm{Im}(p)$ parallèlement à $\mathrm{Ker}(p)$.

## Exercice 4.15
Type : projecteur, noyau et image · ECUE : ALM · Niveau : maths-s2-alm/10
Formules : projecteur $\iff f \circ f = f$ ; $E = \mathrm{Ker} f \oplus \mathrm{Im} f$ ; $f = id$ sur $\mathrm{Im} f$, $0$ sur $\mathrm{Ker} f$ ; matrice dans une base adaptée $\mathrm{diag}(0, \dots, 0, 1, \dots, 1)$

1. $f(f(x,y))=(4(4x-6y)-6(2x-3y),\ 2(4x-6y)-3(2x-3y))=(4x-6y,\ 2x-3y)=f(x,y)$.
2. $\mathrm{Ker}(f)$ : $4x=6y$, soit $\mathrm{Vect}((3,2))$. $\mathrm{Im}(f)=\mathrm{Vect}((4,2))=\mathrm{Vect}((2,1))$.
3. $(3,2)$ et $(2,1)$ ne sont pas colinéaires ($\det=-1\ne0$) : $\mathrm{Ker}\cap\mathrm{Im}=\{0\}$ et $1+1=2$ : $\mathrm{Ker}(f)\oplus\mathrm{Im}(f)=\mathbb R^2$.
4. $v=f(u)$ : $f(v)=f(f(u))=f(u)=v$.
5. $f(u)=f(v)+f(w)=v+0=v$.

## Exercice 4.16
Type : projecteur, noyau et image · ECUE : ALM · Niveau : maths-s2-alm/10
Formules : projecteur $\iff f \circ f = f$ ; $E = \mathrm{Ker} f \oplus \mathrm{Im} f$ ; $f = id$ sur $\mathrm{Im} f$, $0$ sur $\mathrm{Ker} f$ ; matrice dans une base adaptée $\mathrm{diag}(0, \dots, 0, 1, \dots, 1)$

$p_1$ : $p_1(x,y,z)=\frac{x+y+z}3(1,1,1)$ ; $\mathrm{Im}=\mathrm{Vect}((1,1,1))$ et $\mathrm{Ker}=\{x+y+z=0\}$ (plan) : projection sur la droite $\mathrm{Vect}((1,1,1))$ parallèlement au plan $x+y+z=0$ (on remplace chaque coordonnée par la moyenne).
$p_2$ : $\mathrm{Im}=\{(a,-a,z)\}=\mathrm{Vect}((1,-1,0),(0,0,1))$ (plan $x+y=0$), $\mathrm{Ker}=\mathrm{Vect}((1,1,0))$ : projection sur le plan $x+y=0$ parallèlement à la droite $\mathrm{Vect}((1,1,0))$. On vérifie $p\circ p=p$ dans les deux cas.
