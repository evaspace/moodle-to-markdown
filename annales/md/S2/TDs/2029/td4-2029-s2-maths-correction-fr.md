# Contrôle de cours EV et ALM (S2 B4) — lundi 7 avril 2025 (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (pas de corrigé officiel). Sujet : `td4-2029-s2-maths-subject-fr.md` (même dossier). Calculs vérifiés avec sympy. 

## EV — Cours 1 : familles de vecteurs (12 points)
Type : familles libres, génératrices, bases ; coordonnées · ECUE : EV · Niveau : maths-s2-ev/7
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \lambda_i = 0$ ; en dimension $n$, une famille libre de $n$ vecteurs est une base ; plus de $n$ vecteurs $\Rightarrow$ liée ; coordonnées : résoudre $P = \alpha Q_1 + \beta Q_2 + \gamma Q_3$ en identifiant les coefficients

1. (a) $\forall(\lambda_i)\in\mathbb R^n,\ \sum\lambda_iu_i=0_E\Rightarrow\lambda_1=\dots=\lambda_n=0$. (b) $\forall u\in E,\ \exists!(\lambda_i)\in\mathbb R^n,\ u=\sum\lambda_iu_i$. (c) $\big((1,0,0),(0,1,0)\big)$. (d) $\big((1,1),(1,-1)\big)$.
2. a. libre ou liée (pas génératrice). b. génératrice ou liée (pas libre). c. liée. d. libre, génératrice ou liée (libre $\iff$ génératrice $\iff$ base).
3. (a) $\mathcal B$ est libre avec $3=\dim\mathbb R_2[X]$ vecteurs : c'est une base. (b) $Q=1+2(X+1)+3(X^2-X)=3X^2-X+3$. (c) $\mathcal B_c=(1,X,X^2)$. $P_3=X^2-X$ : coordonnées $(0,0,1)$ dans $\mathcal B$ et $(0,-1,1)$ dans $\mathcal B_c$.

## EV — Cours 2 : autour du Vect (8 points)
Type : sous-espaces engendrés, inclusion, dimension · ECUE : EV · Niveau : maths-s2-ev/4
Formules : $P \in \mathrm{Vect}(u_1, \dots) \iff P$ combinaison linéaire des $u_i$ ; $F \subset G$ si les générateurs de $F$ sont dans $G$ ; famille génératrice libre = base, $\dim$ = cardinal

1. $F=\{\lambda(1,2),\ \lambda\in\mathbb R\}=\{(x,y),\ y=2x\}$ : la droite vectorielle de pente $2$ passant par l'origine.
2. $F=\mathrm{Vect}(u_1,u_2)$ : un plan vectoriel de $\mathbb R^3$ si $u_1,u_2$ ne sont pas colinéaires ; une droite vectorielle s'ils sont colinéaires.
3. $P_3=P_2-P_1$ donc $F=\mathrm{Vect}(1,X^2-X)$. $Q=2(X^2-X)-5\cdot1\in F$. $R=X^2=a+b(X^2-X)$ donnerait $b=1$ (coefficient de $X^2$) et $-b=0$ (coefficient de $X$) : impossible, $R\notin F$.

## ALM — Cours 1 : définitions et propriétés (12 points)
Type : noyau, image, injectivité, surjectivité (cours) · ECUE : ALM · Niveau : maths-s2-alm/2
Formules : sous-espace : contient 0 et stable par $\alpha u + v$ ; $f(\alpha u + v) = \alpha f(u) + f(v)$ ; injective $\iff \mathrm{Ker} f = \{0\}$ ; surjective $\iff \mathrm{Im} f = F$

1. $\forall(u,v)\in E^2,\ \forall\lambda\in\mathbb R,\ f(\lambda u+v)=\lambda f(u)+f(v)$.
2. $\mathrm{Ker}(f)=\{P\in\mathbb R_2[X],\ f(P)=(0,0)\}$.
3. $\mathrm{Im}(f)=\{f(P),\ P\in\mathbb R_2[X]\}=\{(a,b)\in\mathbb R^2,\ \exists P\in\mathbb R_2[X],\ f(P)=(a,b)\}$.
4. (a) $\mathrm{Ker}(f)$ est un sev de $E$ et $\mathrm{Im}(f)$ un sev de $F$. (b) Surjective : $\forall y\in F,\ \exists x\in E,\ f(x)=y$ ; équivalent à $\mathrm{Im}(f)=F$. (c) Injective : $\forall(x,x')\in E^2,\ f(x)=f(x')\Rightarrow x=x'$ ; équivalent à $\mathrm{Ker}(f)=\{0_E\}$. Preuve : ($\Rightarrow$) $f(x)=0=f(0)$ donne $x=0$. ($\Leftarrow$) $f(x)=f(x')$ donne $f(x-x')=0$, donc $x-x'=0$.

## ALM — Cours 2 : exemples (8 points)
Type : noyau, image, rang d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/3
Formules : linéaire : $f(\lambda u + v) = \lambda f(u) + f(v)$ ; $\mathrm{Ker} f$ : résoudre $f(x) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \mathrm{rg} f$ ; $\mathrm{rg} f = \dim F \Rightarrow \mathrm{Im} f = F$ (surjective) ; $\mathrm{Im} f = \mathrm{Vect}(f(e_1), \dots, f(e_n))$

1. $(x,y,z)\mapsto(x^2,y)$.
2. $f(x,y,z)=0\iff x=z$ : $\mathrm{Ker}(f)=\{(x,y,x)\}=\mathrm{Vect}\big((1,0,1),(0,1,0)\big)$ ; ces deux vecteurs ne sont pas colinéaires donc forment une base.
3. $g(x,y)=(x,2x)$ : $\mathrm{Im}(g)=\{(x,2x)\}=\mathrm{Vect}((1,2))$.
