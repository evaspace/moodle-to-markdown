# Contrôle 1 S1 — octobre 2018 (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (pas de corrigé officiel). Sujet : `midterm-2023-s1-maths-subject-fr.md` (même dossier). Calculs vérifiés avec sympy. Exercice 5 (complexes) hors programme 2031.

## Exercice 1 (2,5 points)
Type : image directe, image réciproque (lecture graphique) · ECUE : OBM · Niveau : maths-s1-obm/9
Formules : $f(A) = \{f(x), x \in A\}$ ; $f^{-1}(B) = \{x, f(x) \in B\}$ ; lire les valeurs prises (bornes ouvertes / fermées) ; $f(\mathbb{R})$ = ensemble des valeurs prises

$f=\lfloor x/2\rfloor$ sur la portion tracée $[-6,6[$.
- $f([0,4])=\{0,1,2\}$ ($x\in[0,2[\mapsto0$, $[2,4[\mapsto1$, $x=4\mapsto2$).
- $f^{-1}([0,1])=[0,4[$.
- $f^{-1}(\{0,1\})=[0,4[$ (la fonction ne prend que des valeurs entières).
- $f(\mathbb R)=\{-3,-2,-1,0,1,2\}$ sur la portion tracée (si $f=\lfloor x/2\rfloor$ sur tout $\mathbb R$ : $f(\mathbb R)=\mathbb Z$).
- $f^{-1}([-1,1])=[-2,4[$.

## Exercice 2 (1,5 points)
Type : image réciproque d'un singleton · ECUE : OBM · Niveau : maths-s1-obm/9
Formules : $f^{-1}(\{b\}) = \{x, f(x) = b\}$ ; séparer les cas $n$ pair ($n = 2k$) et impair

- $f^{-1}(\{0\})$ : $n$ pair avec $n/2=0$ donne $n=0$ ; $n$ impair donne toujours $0$. Donc $f^{-1}(\{0\})=\{0\}\cup\{\text{entiers impairs}\}$.
- $f^{-1}(\{1\})=\{2\}$ ($n$ pair, $n/2=1$ ; un impair donne $0\ne1$).
- $f^{-1}(\{2\})=\{4\}$.

## Exercice 3 (2 points)
Type : dériver une composée · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/1
Formules : $(g \circ u)' = u' \times g' \circ u$ ; $(e^u)' = u'e^u$ ; $(\sqrt u)' = \frac{u'}{2\sqrt u}$ ; $(u^n)' = nu'u^{n-1}$ ; $(\ln u)' = \frac{u'}u$

$f(x)=\sqrt{\arctan(\sqrt x)}$ : $f'(x)=\dfrac1{2\sqrt{\arctan\sqrt x}}\cdot\dfrac1{1+x}\cdot\dfrac1{2\sqrt x}$.
$g(x)=x^x=e^{x\ln x}$ : $g'(x)=(\ln x+1)\,x^x$.

## Exercice 4 (4 points)
Type : intégrales (primitive directe, IPP, changement de variable) · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/13
Formules : $\int u'u = \frac{u^2}2$ ($u = \arctan$, $u' = \frac1{1+x^2}$) ; IPP : $\int uv' = [uv] - \int u'v$ avec $u = \ln x$, $v' = \frac1{x^2}$, $v = -\frac1x$ ; $u = \ln t \Rightarrow du = \frac{dt}t$ ; $u = \sqrt x \Rightarrow dx = 2u\,du$ ; $\int \frac{du}{1+u^2} = \arctan u$ ; $1 - u^2 = (1-u)(1+u)$

1. $u=x^2+3x+4$, $u'=2x+3$ : $\int\dfrac{u'}{u^2}=-\dfrac1u$. $I=\Big[-\dfrac1{x^2+3x+4}\Big]_0^1=-\dfrac18+\dfrac14=\dfrac18$.
2. $J$ : $u=\ln x$, $v'=1$, $v=x$ : $J=[x\ln x]_1^e-\int_1^e1\,dx=e-(e-1)=1$.
   $K$ : $u=\ln^2x$, $v'=1$ : $K=[x\ln^2x]_1^e-2\int_1^e\ln x\,dx=e-2J=e-2$.
3. $u=\sqrt x$, $dx=2u\,du$, $\dfrac{dx}{\sqrt x}=2\,du$, bornes $1\to2$ : $L=\displaystyle\int_1^22(1+e^u)\,du=2\big[u+e^u\big]_1^2=2(1+e^2-e)$.

## Exercice 5 (3 points)
Type : équation du second degré à coefficients complexes · ECUE : HP (nombres complexes, hors programme 2031)
Formules : $\Delta = b^2 - 4ac$ ; racine carrée $\delta = a + ib$ de $\Delta$ : $a^2 - b^2 = \mathrm{Re}\,\Delta$, $a^2 + b^2 = |\Delta|$, $2ab = \mathrm{Im}\,\Delta$ ; $z = \frac{-b \pm \delta}{2a}$

1. $\Delta=25-4(5-3i)=5+12i$.
2. $\delta=a+ib$ avec $a^2-b^2=5$, $a^2+b^2=|\Delta|=13$, $2ab=12$ : $a^2=9$, $b^2=4$, $ab>0$ : $\delta=3+2i$.
3. $z=\dfrac{5\pm(3+2i)}2$ : $z=4+i$ ou $z=1-i$ (contrôle : somme $5$, produit $(4+i)(1-i)=5-3i$).

## Exercice 6 (3 points)
Type : injectivité / surjectivité, composées · ECUE : OBM · Niveau : maths-s1-obm/10
Formules : injective : $f(x) = f(y) \Rightarrow x = y$, contre-exemple $f(a) = f(b)$ avec $a \neq b$ ; surjective : $\forall y, \exists x, f(x) = y$ ; $(f \circ g)(x) = f(g(x))$

1. $f$ n'est pas injective : $f(1,0)=f(2,0)=0$. $f$ est surjective : $y=f(y,1)$.
2. $g$ est injective : $g(x)=g(x')\Rightarrow x=x'$ (première coordonnée). $g$ n'est pas surjective : $(0,1)$ n'a pas d'antécédent ($x=0$ donne $x^2=0$).
3. $f\circ g:\mathbb R\to\mathbb R,\ x\mapsto x\cdot x^2=x^3$. $g\circ f:\mathbb R^2\to\mathbb R^2,\ (x,y)\mapsto(xy,\ x^2y^2)$.

## Exercice 7 (2 points)
Type : dénombrement de mains de cartes · ECUE : DP · Niveau : maths-s1-dp/5
Formules : $|\Omega| = \binom{32}5$ ; « au moins un » : complémentaire $P(A) = 1 - P(\bar A)$ ; $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ ; principe multiplicatif (choisir chaque catégorie séparément) ; équiprobabilité $P = \frac{|A|}{|\Omega|}$

$|\Omega|=\dbinom{32}5=201376$.
- Aucun As : $\dbinom{28}5=98280$. $P(\text{au moins un As})=1-\dfrac{98280}{201376}=\dfrac{1841}{3596}\approx0{,}51$.
- Interprétation retenue : la main est le roi de carreau, 3 trèfles dont l'As de trèfle, et une cinquième carte qui n'est pas un trèfle. Il reste 2 trèfles à choisir parmi 7 : $\dbinom72=21$. Cinquième carte : $24$ cartes non trèfle moins le roi de carreau déjà pris : $23$. Cas favorables $21\times23=483$, $P=\dfrac{483}{201376}=\dfrac{69}{28768}$. L'énoncé est ambigu (cinquième carte) : une autre lecture est possible.

## Exercice 8 (3 points)
Type : probabilités totales et Bayes · ECUE : DP · Niveau : maths-s1-dp/10
Formules : probabilités totales : $P(M) = P(M \mid V)P(V) + P(M \mid \bar V)P(\bar V)$ ; Bayes : $P(V \mid M) = \frac{P(M \mid V)P(V)}{P(M)}$ ; $P(\bar V) = 1 - P(V)$

$V$ : vacciné, $M$ : malade. $P(V)=0{,}6$, $P(M\mid V)=0{,}001$, $P(M\mid\bar V)=0{,}1$.
1. $P(M)=0{,}6\times0{,}001+0{,}4\times0{,}1=0{,}0006+0{,}04=0{,}0406$ : $4{,}06\ \%$.
2. $P(V\mid M)=\dfrac{P(M\mid V)P(V)}{P(M\mid V)P(V)+P(M\mid\bar V)P(\bar V)}=\dfrac{0{,}001\times0{,}6}{0{,}001\times0{,}6+0{,}1\times0{,}4}$ ($=\dfrac3{203}\approx1{,}5\ \%$).
