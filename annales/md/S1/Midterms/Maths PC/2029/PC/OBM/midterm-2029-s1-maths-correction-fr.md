# Examen S1B1-OBM — octobre 2024 (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (le sujet n'avait pas de corrigé officiel). Sujet : `midterm-2029-s1-maths-subject-fr.md` (même dossier). Calculs vérifiés avec sympy ; l'exercice 6 (nombres complexes) est hors programme 2031.

## Exercice 1 : logique (10 points)
Type : conditions nécessaires et suffisantes, négations, contraposée, inclusion · ECUE : OBM · Niveau : maths-s1-obm/6
Formules : $x^2 > 4 \iff x < -2$ ou $x > 2$ ; $A \Rightarrow P$ vraie si l'ensemble de $A$ est inclus dans celui de $P$ ; $\neg(A \Rightarrow B) \iff A \wedge \neg B$ ; contraposée $\neg B \Rightarrow \neg A$ (même table de vérité) ; $\cos \in [-1, 1]$ ; $A \subset B \iff \forall x, x \in A \Rightarrow x \in B$ ; contre-exemple pour $B \not\subset A$

1. $x^2>4\iff x<-2$ ou $x>2$.
   (a) Implications « … $\Rightarrow P$ » vraies : (2), (4) et (5). (1) est fausse ($x=0$) et (3) est fausse ($x=1{,}95$ donne $x^2<4$).
   (b) Implications « $P\Rightarrow$ … » vraies : seulement $P\Rightarrow(5)$ (équivalence). $P\Rightarrow(1)$ est fausse ($x=-3$), $P\Rightarrow(2)$ aussi ($x=3$), $P\Rightarrow(3)$ aussi ($x=-3$), $P\Rightarrow(4)$ aussi ($x=2{,}5$).
   (c) $\neg(P\Rightarrow(5))\iff P\wedge\neg(5)$ : « $x^2>4$ et $-2\le x\le2$ » (condition jamais réalisée).
2. (a) $P$ est vraie : pour tout $x$, on prend $y=\cos x$. $Q$ est fausse : si $y$ est fixé, $x=\cos y+1$ ne vérifie pas $x=\cos y$ (ou : $x=2$ n'est jamais un cosinus). $R$ est vraie : $x=\pi$ et $y=0$ donnent $-1<1$.
   (b) $\neg P$ : $\exists x\in\mathbb R,\ \forall y\in\mathbb R,\ \cos x\ne y$. $\neg Q$ : $\forall y\in\mathbb R,\ \exists x\in\mathbb R,\ x\ne\cos y$. $\neg R$ : $\forall x,\forall y,\ \cos x\ge\cos y$.
3. (a) La contraposée de $A\Rightarrow B$ est $\neg B\Rightarrow\neg A$.
   (b) Table de vérité : $A\Rightarrow B$ est fausse seulement si $A$ est vraie et $B$ fausse. $\neg B\Rightarrow\neg A$ est fausse seulement si $\neg B$ est vraie et $\neg A$ fausse, c'est-à-dire $B$ fausse et $A$ vraie. Mêmes cas : équivalentes.
   (c) Contraposée : $a\ne0\Rightarrow\exists\varepsilon>0,\ |a|>\varepsilon$. Si $a\ne0$, $\varepsilon=\dfrac{|a|}2>0$ convient : $|a|>\dfrac{|a|}2$.
   (d) La réciproque est vraie : si $a=0$, alors $|a|=0\le\varepsilon$ pour tout $\varepsilon>0$.
4. (a) $A$ et $B$ sont des sous-ensembles de $\mathbb R^3$.
   (b) Soit $(x,y,z)\in A$ : $x=y=z$ donc $2x-y-z=2x-x-x=0$ : $(x,y,z)\in B$. Donc $A\subset B$.
   (c) Non : $(1,2,0)\in B$ car $2-2-0=0$, mais $(1,2,0)\notin A$ car $1\ne2$.

## Exercice 2 : ensembles et fonctions 1 (7 points)
Type : image directe et réciproque, injectivité, surjectivité, composée · ECUE : OBM · Niveau : maths-s1-obm/10
Formules : $f(A) = \{y \in F, \exists x \in A, y = f(x)\}$ ; $f^{-1}(B) = \{x \in E, f(x) \in B\}$ ; injective : $f(x) = f(x') \Rightarrow x = x'$ ; surjective : $\forall y, \exists x, y = f(x)$ ; $g \circ f$ injective si $f$, $g$ injectives ; surjective si $f$, $g$ surjectives

1. $f(I)=\{f(x),\ x\in I\}=\{b\in B,\ \exists x\in I,\ b=f(x)\}$ et $f^{-1}(J)=\{x\in A,\ f(x)\in J\}$.
2. (a)
   | $(x,y)$ | $(2,1)$ | $(2,2)$ | $(2,3)$ | $(3,1)$ | $(3,2)$ | $(3,3)$ | $(4,1)$ | $(4,2)$ | $(4,3)$ |
   |---|---|---|---|---|---|---|---|---|---|
   | $f$ | 3 | 4 | 5 | 4 | 5 | 6 | 5 | 6 | 7 |

   (b) $f(E\times F)=\{3,4,5,6,7\}$ ; $f(\{(2,2),(4,3)\})=\{4,7\}$ ; $f^{-1}(\{1\})=\emptyset$ ; $f^{-1}(\{6\})=\{(3,3),(4,2)\}$.
   (c) Injective : $\forall(u,u')\in(E\times F)^2,\ f(u)=f(u')\Rightarrow u=u'$. Non injective : $f(2,2)=f(3,1)=4$ avec $(2,2)\ne(3,1)$.
   (d) Surjective : $\forall n\in\mathbb N,\ \exists u\in E\times F,\ f(u)=n$. Non surjective : $0$ n'a pas d'antécédent (les valeurs sont dans $\{3,\dots,7\}$).
   (e) $I=\{(2,1),(2,2)\}$ et $J=\mathbb N$ : $f$ prend les valeurs $3$ et $4$ (distinctes), donc injective, et non surjective (par exemple $0$ n'est pas atteint).
   (f) $I'=\{(2,2),(3,1),(2,3)\}$ et $J'=\{4,5\}$ : surjective ($4$ et $5$ sont atteints), non injective ($f(2,2)=f(3,1)$).

## Exercice 3 : ensembles et fonctions 2 (3 points)
Type : image directe, image réciproque (lecture graphique) · ECUE : OBM · Niveau : maths-s1-obm/9
Formules : $f(A) = \{f(x), x \in A\}$ ; $f^{-1}(B) = \{x, f(x) \in B\}$ ; lire les valeurs prises (bornes ouvertes / fermées) ; $f(\mathbb{R})$ = ensemble des valeurs prises

| $f$ | $\exp:\mathbb R\to\mathbb R$ | $\cos:[0,\pi]\to\mathbb R$ |
|---|---|---|
| $f(\{0\})$ | $\{1\}$ | $\{1\}$ |
| $f\left(\left[0,\frac\pi2\right]\right)$ | $\left[1,e^{\pi/2}\right]$ | $[0,1]$ |
| $f^{-1}(\{0\})$ | $\emptyset$ | $\left\{\frac\pi2\right\}$ |
| $f^{-1}(\{-1\})$ | $\emptyset$ | $\{\pi\}$ |
| $f^{-1}(]-\infty,0])$ | $\emptyset$ | $\left[\frac\pi2,\pi\right]$ |

## Exercice 4 : relations (4 points)
Type : propriétés d'une relation, négation, contraposée · ECUE : OBM · Niveau : maths-s1-obm/11
Formules : réflexive $\forall x, x\mathcal Rx$ ; antisymétrique $x\mathcal Ry \wedge y\mathcal Rx \Rightarrow x = y$ ; transitive ; négation de $\forall(P \Rightarrow Q)$ : $\exists(P \wedge \neg Q)$ ; contraposée de $P \Rightarrow Q$ : $\neg Q \Rightarrow \neg P$ ; $\neg(A \wedge B) = \neg A \vee \neg B$ ; ordre = réflexive + antisymétrique + transitive

1. Réflexive : $\forall a,\ a\mathcal Ra$. Vrai : $|a|\le|a|$.
2. Symétrique : $\forall(a,b),\ a\mathcal Rb\Rightarrow b\mathcal Ra$. Faux : $1\mathcal R2$ ($1\le2$) mais pas $2\mathcal R1$.
3. Antisymétrique : $\forall(a,b),\ (a\mathcal Rb\wedge b\mathcal Ra)\Rightarrow a=b$. Faux : $1\mathcal R(-1)$ et $(-1)\mathcal R1$ mais $1\ne-1$. Négation utilisée : $\exists(a,b),\ a\mathcal Rb\wedge b\mathcal Ra\wedge a\ne b$.
4. Transitive : $\forall(a,b,c),\ (a\mathcal Rb\wedge b\mathcal Rc)\Rightarrow a\mathcal Rc$. Vrai : $|a|\le|b|$ et $|b|\le|c|$ donnent $|a|\le|c|$.

## Exercice 5 : intégrales (6 points)
Type : primitive $u'/u$, IPP trigonométrique, changement de variable vers arctan · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/13
Formules : $\int \frac{u'}u = \ln|u|$ ($2x + 2 = \frac12(4x + 4)$) ; IPP $\int_a^b uv' = [uv]_a^b - \int_a^b u'v$, $\int \cos\frac x3 = 3\sin\frac x3$ ; $t = \frac x{\sqrt3}$, $dx = \sqrt3\,dt$, $3 + x^2 = 3(1 + t^2)$ ; $\int \frac{dt}{1+t^2} = \arctan t$

1. $2x+2=\dfrac12(4x+4)$ et $(2x^2+4x+1)'=4x+4$ : $I=\dfrac12\Big[\ln|2x^2+4x+1|\Big]_0^1=\dfrac12(\ln7-\ln1)=\dfrac12\ln7$.
2. $u(x)=x+1$, $u'(x)=1$, $v'(x)=\cos\frac x3$, $v(x)=3\sin\frac x3$. $J=\Big[3(x+1)\sin\frac x3\Big]_0^\pi-3\int_0^\pi\sin\frac x3\,dx$. Le crochet vaut $3(\pi+1)\dfrac{\sqrt3}2$. L'intégrale : $-3\Big[-3\cos\frac x3\Big]_0^\pi=9\left(\cos\frac\pi3-1\right)=-\dfrac92$. Donc $J=\dfrac{3\sqrt3}2(\pi+1)-\dfrac92$.
3. $t=\dfrac x{\sqrt3}$, $dx=\sqrt3\,dt$, $3+x^2=3(1+t^2)$, bornes $0\to1$ : $K=\displaystyle\int_0^1\frac{\sqrt3\,dt}{3(1+t^2)}=\frac{\sqrt3}3\Big[\arctan t\Big]_0^1=\frac{\sqrt3}3\cdot\frac\pi4=\frac{\sqrt3\,\pi}{12}$.

## Exercice 6 : nombres complexes (10 points)
Type : nombres complexes (cours, forme algébrique, module, forme exponentielle, équation) · ECUE : HP (nombres complexes, hors programme 2031)
Formules : $i^2 = -1$ ; $z = a + ib$ (forme algébrique), $\bar z = a - ib$, $|z| = \sqrt{a^2 + b^2}$ ; $\cos\theta = \frac a{|z|}$, $\sin\theta = \frac b{|z|}$ ; $z = |z|(\cos\theta + i\sin\theta) = |z|e^{i\theta}$ ; $|zw| = |z||w|$ ; $\frac{e^{i\alpha}}{e^{i\beta}} = e^{i(\alpha - \beta)}$ ; $\Delta < 0 \Rightarrow z = \frac{-b \pm i\sqrt{-\Delta}}{2a}$

Partie 1.
1. $i^2=-1$. 2. forme algébrique. 3. $\mathbb C$. 4. $\bar z=a-ib$. 5. $|z|=\sqrt{a^2+b^2}$. 6. $\cos\theta=\dfrac a{|z|}$ et $\sin\theta=\dfrac b{|z|}$. 7. $z=|z|(\cos\theta+i\sin\theta)$. 8. $e^{i\theta}=\cos\theta+i\sin\theta$.
9. $M(-4,3)$ : $|z|=\sqrt{16+9}=5$, un argument est $\pi-\arctan\dfrac34$ (point dans le deuxième quadrant).

Partie 2.
1. $(3-i)(2-4i)=6-12i-2i+4i^2=2-14i$.
2. $|z_1|=\sqrt{16+9}=5$, $|z_2|=\sqrt{2+2}=2$, $|z_1\bar z_2|=|z_1||z_2|=10$.
3. $z_1=1-i=\sqrt2\,e^{-i\pi/4}$. $z_2=-\sqrt3-i$ : $|z_2|=2$, $\cos\theta=-\dfrac{\sqrt3}2$, $\sin\theta=-\dfrac12$ donc $z_2=2e^{-5i\pi/6}$. $\dfrac{z_1}{z_2}=\dfrac{\sqrt2}2e^{i(-\pi/4+5\pi/6)}=\dfrac{\sqrt2}2e^{7i\pi/12}$. $z_2^3=8e^{-5i\pi/2}=8e^{-i\pi/2}=-8i$.
4. $\Delta=9-12=-3<0$ : $z=\dfrac{3\pm i\sqrt3}2$.
