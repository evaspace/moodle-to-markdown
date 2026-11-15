# Partiel 1 — janvier 2016 (sujet, FR)

- Source : `raw/S1/Finals/Maths PC/2020/final-2020-s1-maths-subject-fr.pdf` (scan, 8 pages)
- Date réelle : janvier 2016 (Info-Sup 15/16, dossier promo 2020). Corrigé rédigé : `final-2020-s1-maths-correction-fr.md` (même dossier).
- Durée : 3 heures. Documents et calculatrices non autorisés.
- Barème : 22 points

## Exercice 1 (4 points)
Type : nier une phrase · ECUE : OBM · Niveau : maths-s1-obm/3
Formules : $\neg(\forall x, P(x)) \iff \exists x, \neg P(x)$ ; $\neg(\exists x, P(x)) \iff \forall x, \neg P(x)$ ; $\neg(P \Rightarrow Q) \iff P \wedge \neg Q$ ; $\neg(P \wedge Q) \iff \neg P \vee \neg Q$ ; $\neg(P \vee Q) \iff \neg P \wedge \neg Q$ ; « aucun » = $\forall, \neg$

Écrire la négation des phrases suivantes :
1. « Aucun diplômé de l'EPITA n'aura un premier salaire brut annuel en dessous de 40 k€ ».
2. « Si j'intègre le laboratoire de recherche de l'EPITA, je pourrai m'orienter vers l'imagerie médicale ».
3. « Certains MiMo sont compliqués ».
4. « Tous vos gestes sur IONISx sont analysés ».

## Exercice 2 (2 points)
Type : récurrence (inégalité de Bernoulli) · ECUE : OBM · Niveau : maths-s1-obm/7
Formules : récurrence : $P(n_0)$ et $P(n) \Rightarrow P(n+1)$ ; $(1+x)^{n+1} = (1+x)^n(1+x)$ ; $(1+nx)(1+x) = 1 + (n+1)x + nx^2 \geqslant 1 + (n+1)x$

Soit $x \in \mathbb{R}_+^*$. Montrer par récurrence que pour tout $n \in \mathbb{N}^*$, $(1+x)^n \geqslant 1 + nx$.

## Exercice 3 (2 points)
Type : traduire avec quantificateurs · ECUE : OBM · Niveau : maths-s1-obm/4
Formules : « tout » $= \forall$, « il existe » $= \exists$, « aucun » $= \forall \dots \neg$ ; l'ordre $\forall\exists$ / $\exists\forall$ change le sens ; $f$ s'annule : $\exists x, f(x) = 0$ ; minimum en $a$ : $\exists a, \forall x, f(x) \geqslant f(a)$ ; pair : $\exists k, n = 2k$

Écrire en langage mathématique (avec les quantificateurs) les phrases suivantes (ne pas se préoccuper de la validité des phrases, certaines peuvent être vraies et d'autres fausses) :
1. « Tout réel est le cube d'un réel ».
2. « Il existe un réel qui est le cube de tout réel ».
3. « Tout entier naturel est pair ou impair ».
4. « Entre deux réels distincts, on peut toujours trouver un rationnel ».

## Exercice 4 (2 points)
Type : injectivité / surjectivité de $x \mapsto x^2$ · ECUE : OBM · Niveau : maths-s1-obm/10
Formules : injective : $f(x) = f(y) \Rightarrow x = y$ ; surjective : $\forall y \in F, \exists x \in E, y = f(x)$ ; $x^2 = y^2 \iff x = \pm y$ ; $x^2 \geqslant 0$

Dans chacune des questions suivantes, entourer les bonnes réponses (a. $f$ est injective ; b. $f$ n'est pas injective ; c. $f$ est surjective ; d. $f$ n'est pas surjective).
1. $f : \mathbb{R}_+ \to \mathbb{R},\ x \mapsto x^2$.
2. $f : \mathbb{R} \to \mathbb{R},\ x \mapsto x^2$.
3. $f : \mathbb{R} \to \mathbb{R}_+,\ x \mapsto x^2$.
4. $f : \mathbb{R}_+ \to \mathbb{R}_+,\ x \mapsto x^2$.

## Exercice 5 (3 points)
Type : équation diophantienne $ax+by=c$ (Euclide, Gauss) · ECUE : HP (arithmétique)
Formules : Euclide : $a = bq + r$, $a \wedge b = b \wedge r$ ; solutions $\iff (a \wedge b) \mid c$ ; diviser par $d = a \wedge b$ ; remonter Euclide : $au_0 + bv_0 = d$ puis multiplier par $c/d$ ; Gauss : $a \mid bc$ et $a \wedge b = 1 \Rightarrow a \mid c$ ; $a(x - x_0) = -b(y - y_0)$ donne $x = x_0 + \frac{b}{d}k$, $y = y_0 - \frac{a}{d}k$, $k \in \mathbb{Z}$ ; vérifier la réciproque

1. En utilisant l'algorithme d'Euclide, déterminer une solution particulière de l'équation $524x + 144y = 4$.
2. En utilisant obligatoirement le théorème de Gauss, déterminer l'ensemble des couples $(x,y) \in \mathbb{Z}^2$ tels que $524x + 144y = 4$.

## Exercice 6 (2 points)
Type : PGCD et Bézout (démonstration) · ECUE : HP (arithmétique)
Formules : $d \mid a$ et $d \mid b$ : $a = da'$, $b = db'$ ; $a' \wedge b' = 1$ ; Bézout : $a' \wedge b' = 1 \iff \exists (u,v), a'u + b'v = 1$ ; multiplier par $d$

Soient $a$ et $b$ deux entiers naturels non nuls et $d = a \wedge b$.
1. Montrer qu'il existe $(a',b') \in \mathbb{N}^{*2}$ tel que $a = da'$, $b = db'$ et $a' \wedge b' = 1$.
2. Via la question précédente et le théorème de Bézout, montrer qu'il existe $(u,v) \in \mathbb{Z}^2$ tel que $au + bv = d$.

## Exercice 7 (2 points)
Type : multiplicité d'une racine d'un polynôme · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/4
Formules : $\alpha$ racine d'ordre $m$ $\iff P(\alpha) = P'(\alpha) = \dots = P^{(m-1)}(\alpha) = 0$ et $P^{(m)}(\alpha) \neq 0$ ; $(X^n)' = nX^{n-1}$

Déterminer l'ordre de multiplicité de la racine 1 du polynôme $P(X) = X^4 - X^3 - 3X^2 + 5X - 2$.

## Exercice 8 (3 points)
Type : divisibilité et reste de division euclidienne de polynômes · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/5
Formules : $A = BQ + R$, $\deg R < \deg B$ ; $(X-a)(X-b) \mid P \iff P(a) = P(b) = 0$ ($a \neq b$) ; reste par $(X-a)(X-b)$ : $R = \alpha X + \beta$ avec $R(a) = P(a)$, $R(b) = P(b)$ ; reste par $(X-a)^2$ : $R(a) = P(a)$, $R'(a) = P'(a)$

Soit $n \geqslant 2$.
1. Montrer que le polynôme $P(X) = (X-2)^{2n} + (X-1)^n - 1$ est divisible par $X^2 - 3X + 2$.
2. Déterminer le reste de la division euclidienne de $Q(X) = (X-2)^{2n} + (X-1)^n - 2$ par
   a. $(X-2)(X-1)$ ;
   b. $(X-1)^2$.

## Exercice 9 (2 points)
Type : racine multiple d'un polynôme à paramètre · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/10
Formules : $\alpha$ racine au moins double $\iff Q(\alpha) = Q'(\alpha) = 0$ ; $((X+1)^7)' = 7(X+1)^6$ ; $(X+1)^6 = X^6 \iff X + 1 = \pm X$

Pour quelle(s) valeur(s) du réel $a$ le polynôme $Q(X) = (X+1)^7 - X^7 - a$ admet-il une racine réelle au moins double ?
