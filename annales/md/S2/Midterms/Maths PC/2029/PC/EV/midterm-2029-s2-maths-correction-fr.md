# Examen S2-B3 EV — mars 2025 (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (pas de corrigé officiel). Sujet : `midterm-2029-s2-maths-subject-fr.md` (même dossier). Calculs vérifiés avec sympy. Pas de corrigé officiel dans les annales.

## Exercice 1 : sous-espaces vectoriels (6 points)
Type : reconnaître un sous-espace vectoriel · ECUE : EV · Niveau : maths-s2-ev/3
Formules : sev : contient 0, stable par addition et multiplication par un scalaire ; contre-exemple $\lambda u \notin E$ ; équation non linéaire ($z^2$) $\Rightarrow$ en général pas un sev ; $\mathrm{Vect}(\dots)$ est toujours un sev

1. $F\subset E$ ; $0_E\in F$ ; $\forall(u,v)\in F^2,\ \forall\alpha\in\mathbb R,\ \alpha u+v\in F$.
2. (a) $F\subset\mathbb R^3$, $0\in F$, et si $u=(x,y,z)$, $u'=(x',y',z')\in F$, $\alpha\in\mathbb R$ : $2(\alpha x+x')+(\alpha y+y')=\alpha(2x+y)+(2x'+y')=0$. $F$ est un sev, donc un $\mathbb R$-ev.
   (b) $G$ n'est pas un ev : $f:x\mapsto x$ ($f(0)=0$) et $g:x\mapsto1-x$ ($g(1)=0$) sont dans $G$ mais $(f+g)(0)(f+g)(1)=1\cdot1=1\ne0$ : $f+g=1\notin G$ (non stable par addition).

## Exercice 2 : cours 1 sur les sev (3 points)
Type : sous-espaces, intersection, somme directe · ECUE : EV · Niveau : maths-s2-ev/9
Formules : $\mathrm{Vect}(u)$ : droite si $u \neq 0$ ; plan $ax + by + cz = 0$ : exprimer $z$, $G = \mathrm{Vect}(u, v)$ ; $u \in F \cap G$ : paramétrer par $F$ puis injecter l'équation de $G$ ; Grassmann $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $\dim F + \dim G = \dim E$

1. $F\cap G$ : Vrai. $F\cup G$ : Faux (en général). $F+G$ : Vrai.
2. $F\cap G\subset E$ ; $0_E\in F$ et $0_E\in G$ ; si $u,v\in F\cap G$ et $\alpha\in\mathbb R$ : $\alpha u+v\in F$ et $\alpha u+v\in G$ car $F$ et $G$ sont des sev, donc $\alpha u+v\in F\cap G$.

## Exercice 3 : somme de sous-espaces vectoriels (7 points)
Type : sous-espaces, intersection, somme directe · ECUE : EV · Niveau : maths-s2-ev/9
Formules : $\mathrm{Vect}(u)$ : droite si $u \neq 0$ ; plan $ax + by + cz = 0$ : exprimer $z$, $G = \mathrm{Vect}(u, v)$ ; $u \in F \cap G$ : paramétrer par $F$ puis injecter l'équation de $G$ ; Grassmann $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $\dim F + \dim G = \dim E$

1. $F$ et $G$ sont deux plans vectoriels de $\mathbb R^3$.
2. (a) $v$ : $y+(2y-x)+(x-3y)=0$ donc $v\in F$. $w$ : $(x-y)-(-y+x)=0$ donc $w\in G$.
   (b) $v+w=(y+x-y,\ 2y-x-y+x,\ x-3y+z+3y-x)=(x,y,z)=u$ : $u\in F+G$.
   (c) Tout $u\in\mathbb R^3$ est dans $F+G$ et $F+G\subset\mathbb R^3$ : $E=F+G$.
3. $E=F\oplus G\iff\forall u\in E,\ \exists!(v,w)\in F\times G,\ u=v+w$ (ou : $E=F+G$ et $F\cap G=\{0_E\}$).
4. Non : $(1,1,-2)\in F\cap G$ ($1+1-2=0$ et $1-1=0$), donc $F\cap G\ne\{0_E\}$ (et $\dim F+\dim G=4>3$).

## Exercice 4 : cours 2 sur les familles (4 points)
Type : familles libres, génératrices, bases · ECUE : EV · Niveau : maths-s2-ev/6
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \forall i, \lambda_i = 0$ ; génératrice : tout vecteur est combinaison linéaire ; base = libre + génératrice ; $\dim \mathbb{R}_n[X] = n + 1$ ; en dimension $n$ : plus de $n$ vecteurs $\Rightarrow$ liée, moins de $n$ $\Rightarrow$ non génératrice, $n$ vecteurs libres $\Rightarrow$ base ; degrés échelonnés $\Rightarrow$ libre

1. (a) $\forall(\alpha,\beta,\gamma)\in\mathbb R^3,\ \alpha P_1+\beta P_2+\gamma P_3=0\Rightarrow\alpha=\beta=\gamma=0$. (b) $\exists(\alpha,\beta,\gamma)\in\mathbb R^3\setminus\{(0,0,0)\},\ \alpha P_1+\beta P_2+\gamma P_3=0$. (c) $\forall P\in E,\ \exists(\alpha,\beta,\gamma)\in\mathbb R^3,\ P=\alpha P_1+\beta P_2+\gamma P_3$.
2. $\big((1,0,0),(0,1,0)\big)$.
3. $\big((1,0,0),(0,1,0),(1,1,0)\big)$.
