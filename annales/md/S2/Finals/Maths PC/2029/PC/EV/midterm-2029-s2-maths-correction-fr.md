# Examen S2-B4-EV (espaces vectoriels) — mai 2025 (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (pas de corrigé officiel). Sujet : `midterm-2029-s2-maths-subject-fr.md` (même dossier). Calculs vérifiés avec sympy. 

## Exercice 1 : familles de vecteurs (10 points)
Type : familles libres, génératrices, bases ; coordonnées · ECUE : EV · Niveau : maths-s2-ev/7
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \lambda_i = 0$ ; en dimension $n$, une famille libre de $n$ vecteurs est une base ; plus de $n$ vecteurs $\Rightarrow$ liée ; coordonnées : résoudre $P = \alpha Q_1 + \beta Q_2 + \gamma Q_3$ en identifiant les coefficients

1. (a) $\alpha+\beta(X^2+X+1)+\gamma(X^2-X+1)=0$ donne : $X^2$ : $\beta+\gamma=0$ ; $X$ : $\beta-\gamma=0$ ; donc $\beta=\gamma=0$ puis $\alpha=0$ : famille libre de 3 vecteurs dans $\mathbb R_2[X]$ (dimension $3$) : base.
   (b) $Q=\alpha+\beta P_2+\gamma P_3$ : $\beta+\gamma=2$, $\beta-\gamma=4$, $\alpha+\beta+\gamma=4$ : $\beta=3$, $\gamma=-1$, $\alpha=2$. Coordonnées $(2,3,-1)$.
2. (a) Oui : si $a\varepsilon_1+b(2\varepsilon_2)+c\varepsilon_3=0$, comme $\mathcal F$ est libre, $a=2b=c=0$, donc $a=b=c=0$.
   (b) $\mathcal F_1$ est libre et engendre $F$ : $\mathcal B=\mathcal F_1$ est une base de $F$, $\dim F=3$.
   (c) $u=\varepsilon_1+\varepsilon_2=1\cdot\varepsilon_1+\dfrac12(2\varepsilon_2)+0\cdot\varepsilon_3\in F$ : coordonnées $\left(1,\dfrac12,0\right)$.
3. (a) On lit sur le quadrillage les coordonnées $(2,-1)$ : $u=2u_1-u_2$. (b) $2(2,1)-(-1,1)=(4+1,2-1)=(5,1)$ ✓.

## Exercice 2 : somme de sev (10 points)
Type : sous-espaces, intersection, somme directe · ECUE : EV · Niveau : maths-s2-ev/9
Formules : $\mathrm{Vect}(u)$ : droite si $u \neq 0$ ; plan $ax + by + cz = 0$ : exprimer $z$, $G = \mathrm{Vect}(u, v)$ ; $u \in F \cap G$ : paramétrer par $F$ puis injecter l'équation de $G$ ; Grassmann $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $\dim F + \dim G = \dim E$

1. $w=(1,1,-1)=u+v$. $(u,v)$ est libre (non colinéaires) et engendre $F$ : base $(u,v)$, $\dim F=2$.
2. $x+y+z=0$ et $x-2y+z=0$ donnent $3y=0$ puis $z=-x$ : $G=\{(x,0,-x)\}=\mathrm{Vect}\big((1,0,-1)\big)$, base $\big((1,0,-1)\big)$, $\dim G=1$.
3. $(\lambda,0,-\lambda)\in F$ : $=au+bv=(a,b,-2a+b)$ donne $a=\lambda$, $b=0$, et $-2\lambda=-\lambda$, donc $\lambda=0$ : $F\cap G=\{0_E\}$.
4. $F\oplus G=E\iff F\cap G=\{0\}$ et $F+G=E$. Ici $\dim F+\dim G-\dim(F\cap G)=2+1-0=3=\dim E$ et $F+G\subset E$ : $F+G=E$. Donc $F\oplus G=E$.
