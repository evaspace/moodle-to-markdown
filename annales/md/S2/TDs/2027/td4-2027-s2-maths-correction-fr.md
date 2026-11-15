# Contrôle de cours 2 (S2) — lundi 3 avril 2023 (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (pas de corrigé officiel). Sujet : `td4-2027-s2-maths-subject-fr.md` (même dossier). Calculs vérifiés avec sympy. 

## Cours 1 : familles de vecteurs (6 points)
Type : familles libres, génératrices, bases · ECUE : EV · Niveau : maths-s2-ev/6
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \forall i, \lambda_i = 0$ ; génératrice : tout vecteur est combinaison linéaire ; base = libre + génératrice ; $\dim \mathbb{R}_n[X] = n + 1$ ; en dimension $n$ : plus de $n$ vecteurs $\Rightarrow$ liée, moins de $n$ $\Rightarrow$ non génératrice, $n$ vecteurs libres $\Rightarrow$ base ; degrés échelonnés $\Rightarrow$ libre

1. (a) Libre : $\forall(\lambda_i)\in\mathbb R^n,\ \sum\lambda_ie_i=0_E\Rightarrow\lambda_1=\dots=\lambda_n=0$. (b) Liée : $\exists(\lambda_i)\in\mathbb R^n\setminus\{0\},\ \sum\lambda_ie_i=0_E$. (c) Libre : $(P_1,P_2,P_4)$ (degrés $0,1,2$). Liée : $(P_1,P_2,P_3)$ car $P_1=2(P_2-P_3)$.
2. (a) $\forall u\in E,\ \exists(\lambda_i)\in\mathbb R^n,\ u=\sum\lambda_ie_i$. (b) $(u_1,u_3)$ : $\det\begin{pmatrix}1&-1\\-2&1\end{pmatrix}=-1\ne0$.
3. $\supset$ : évident. $\subset$ : $e_1=ae_2+be_3+ce_4$, donc $\alpha_1e_1+\dots+\alpha_4e_4=(\alpha_1a+\alpha_2)e_2+(\alpha_1b+\alpha_3)e_3+(\alpha_1c+\alpha_4)e_4\in\mathrm{Vect}(e_2,e_3,e_4)$.

## Cours 2 : bases (3 points)
Type : familles libres, génératrices, bases ; coordonnées · ECUE : EV · Niveau : maths-s2-ev/7
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \lambda_i = 0$ ; en dimension $n$, une famille libre de $n$ vecteurs est une base ; plus de $n$ vecteurs $\Rightarrow$ liée ; coordonnées : résoudre $P = \alpha Q_1 + \beta Q_2 + \gamma Q_3$ en identifiant les coefficients

1. $\mathcal B$ base : $\forall u\in\mathbb R^3,\ \exists!(\alpha,\beta,\gamma)\in\mathbb R^3,\ u=\alpha e_1+\beta e_2+\gamma e_3$. Pour $(1,2,3)$ : $u=e_1+2e_2+3e_3=(1+3,\ 2+3,\ 1+2)=(4,5,3)$.
2. $(4,0,1)=(1,2,0)+(3,-2,1)$ : le troisième vecteur est combinaison des deux premiers, qui ne sont pas colinéaires : $\dim F=2$.

## Cours 3 : exemples d'applications linéaires (3 points)
Type : application linéaire (caractérisation) · ECUE : ALM · Niveau : maths-s2-alm/1
Formules : $f$ linéaire $\Rightarrow f(0) = 0$ et $f(2x) = 2f(x)$ (conditions nécessaires) ; réciproquement vérifier $f(\lambda x + y) = \lambda f(x) + f(y)$ ; les applications linéaires de $\mathbb{R}$ dans $\mathbb{R}$ sont $x \mapsto bx$

1) $f(x,y,z)=(z,0,0)$ ou l'identité. 2) $(x,y,z)\mapsto(x^2,y)$. 3) $(x,y,z)\mapsto x+yX+zX^2$.

## Cours 4 : noyau et image (8 points)
Type : noyau, image, injectivité, surjectivité (cours) · ECUE : ALM · Niveau : maths-s2-alm/2
Formules : sous-espace : contient 0 et stable par $\alpha u + v$ ; $f(\alpha u + v) = \alpha f(u) + f(v)$ ; injective $\iff \mathrm{Ker} f = \{0\}$ ; surjective $\iff \mathrm{Im} f = F$

1. $\mathrm{Ker}(f)=\{u\in E,\ f(u)=0_F\}$. 2. $\mathrm{Im}(f)=\{f(u),\ u\in E\}$.
3. $f$ injective $\iff\mathrm{Ker}(f)=\{0_E\}$. Preuve : ($\Rightarrow$) $f(u)=0=f(0)$ donne $u=0$. ($\Leftarrow$) $f(u)=f(v)$ donne $f(u-v)=0$, $u-v\in\mathrm{Ker}(f)=\{0\}$.
4. $f$ surjective $\iff\mathrm{Im}(f)=F$.
5. $f(x,y,z)=(2x+z,\ y,\ 0)$ : noyau $\{z=-2x,\ y=0\}=\mathrm{Vect}((1,0,-2))$.
