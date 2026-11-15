# Contrôle TD 4 (S2) — lundi 9 avril 2018 (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (pas de corrigé officiel). Sujet : `td4-2022-s2-maths-subject-fr.md` (même dossier). Calculs vérifiés avec sympy. 

## Question de cours
Type : noyau, image, injectivité, surjectivité (cours) · ECUE : ALM · Niveau : maths-s2-alm/2
Formules : sous-espace : contient 0 et stable par $\alpha u + v$ ; $f(\alpha u + v) = \alpha f(u) + f(v)$ ; injective $\iff \mathrm{Ker} f = \{0\}$ ; surjective $\iff \mathrm{Im} f = F$

a. $\mathrm{Ker}(\varphi)=\{u\in E,\ \varphi(u)=0_F\}$ et $\mathrm{Im}(\varphi)=\{\varphi(u),\ u\in E\}=\{v\in F,\ \exists u\in E,\ v=\varphi(u)\}$.
b. $\varphi$ injective $\iff\mathrm{Ker}(\varphi)=\{0_E\}$. $\varphi$ surjective $\iff\mathrm{Im}(\varphi)=F$.

## Exercice 1
Type : application linéaire (caractérisation) · ECUE : ALM · Niveau : maths-s2-alm/1
Formules : $f$ linéaire $\Rightarrow f(0) = 0$ et $f(2x) = 2f(x)$ (conditions nécessaires) ; réciproquement vérifier $f(\lambda x + y) = \lambda f(x) + f(y)$ ; les applications linéaires de $\mathbb{R}$ dans $\mathbb{R}$ sont $x \mapsto bx$

$\Delta(\lambda P+Q)=X(\lambda P'+Q')-2(\lambda P+Q)=\lambda(XP'-2P)+(XQ'-2Q)=\lambda\Delta(P)+\Delta(Q)$ : $\Delta$ est linéaire (et $\Delta(P)\in\mathbb R[X]$).

## Exercice 2
Type : sous-espaces, intersection, somme directe · ECUE : EV · Niveau : maths-s2-ev/9
Formules : $\mathrm{Vect}(u)$ : droite si $u \neq 0$ ; plan $ax + by + cz = 0$ : exprimer $z$, $G = \mathrm{Vect}(u, v)$ ; $u \in F \cap G$ : paramétrer par $F$ puis injecter l'équation de $G$ ; Grassmann $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $\dim F + \dim G = \dim E$

Intersection : si $v\in E\cap F$ : $v_n=an+b$ avec $v_0=b=0$ et $v_1=a+b=0$ : $a=b=0$, $v=0$.
Somme : soit $u\in\mathbb R^{\mathbb N}$. On pose $v_n=(u_1-u_0)n+u_0\in F$ : $v_0=u_0$, $v_1=u_1$. Alors $u-v$ a pour termes d'indice $0$ et $1$ nuls : $u-v\in E$ et $u=(u-v)+v$. Donc $E\oplus F=\mathbb R^{\mathbb N}$ : supplémentaires.

## Exercice 3
Type : écrire un sous-espace sous forme de Vect (système linéaire) · ECUE : EV · Niveau : maths-s2-ev/4
Formules : résoudre le système par pivot de Gauss ; exprimer les inconnues principales en fonction des inconnues libres ; factoriser chaque paramètre : $\{(x,y,z)\} = \{t\,u,\ t \in \mathbb{R}\} = \mathrm{Vect}(u)$ ; nombre de paramètres libres = dimension

Système de rang $2$. Les deux premières lignes donnent par différence $4y-4z=0$, donc $y=z$, puis $x=-3y+2z=-y$ ; la troisième ligne est vérifiée ($-x+3y-4z=y+3y-4y=0$). $E=\{(-z,z,z)\}=\mathrm{Vect}\big((-1,1,1)\big)$.
