# Partiel S1 — janvier 2018 (sujet, FR)

- Source : `raw/S1/Finals/Maths PC/2022/final-2022-s1-maths-subject-fr.pdf` (scan, 7 pages ; la page 2 du sujet manque dans le PDF, la numérotation passe de 1 à 3)
- Date réelle : janvier 2018 (S1 17/18, dossier promo 2022). Corrigé (rédigé par un étudiant) : `final-2022-s1-maths-correction-fr.md`.
- Barème : 21 points

## Exercice 1 (2 points)
Type : nier une phrase · ECUE : OBM · Niveau : maths-s1-obm/3
Formules : $\neg(\forall x, P(x)) \iff \exists x, \neg P(x)$ ; $\neg(\exists x, P(x)) \iff \forall x, \neg P(x)$ ; $\neg(P \Rightarrow Q) \iff P \wedge \neg Q$ ; $\neg(P \wedge Q) \iff \neg P \vee \neg Q$ ; $\neg(P \vee Q) \iff \neg P \wedge \neg Q$ ; « aucun » = $\forall, \neg$

Écrire la négation des phrases suivantes :
1. « Certains étudiants aiment bien organiser des soirées festives ».
2. « Certains étudiants ne partiront pas dans la destination de leur choix au S4 ».
3. « Tous les étudiants de l'EPITA s'investissent dans leurs projets de prépas ».
4. « Aucun diplômé de l'EPITA n'est déçu par la formation de l'école axée sur le savoir-faire ».

## Exercice 2 (2 points)
Type : récurrence (dérivée $n$-ième) · ECUE : OBM · Niveau : maths-s1-obm/7
Formules : récurrence ; $(\ln(1+x))' = \frac1{1+x}$ ; $((1+x)^{-n})' = -n(1+x)^{-n-1}$ ; $(n-1)! \cdot n = n!$

Soit $f : \left]-1,+\infty\right[ \to \mathbb{R},\ x \mapsto \ln(1+x)$.
Soit $x \in \left]-1,+\infty\right[$. Montrer, par récurrence, que pour tout $n \in \mathbb{N}^*$, $f^{(n)}(x) = \dfrac{(-1)^{n-1}(n-1)!}{(1+x)^n}$.

## Exercice 3 (2 points)
Type : traduire avec quantificateurs · ECUE : OBM · Niveau : maths-s1-obm/4
Formules : « tout » $= \forall$, « il existe » $= \exists$, « aucun » $= \forall \dots \neg$ ; l'ordre $\forall\exists$ / $\exists\forall$ change le sens ; $f$ s'annule : $\exists x, f(x) = 0$ ; minimum en $a$ : $\exists a, \forall x, f(x) \geqslant f(a)$ ; pair : $\exists k, n = 2k$

Écrire en langage mathématique (avec les quantificateurs) les phrases suivantes :
1. « Certains réels sont strictement supérieurs à leur carré ».
2. « Il existe un entier naturel multiple de tous les autres ».
3. « Aucun entier naturel n'est supérieur ou égal à tous les autres ».
4. « Tout réel possède une racine carrée dans $\mathbb{R}$ ».

## Exercice 4 (4 points)
Type : injectivité / surjectivité, composées sur $\mathbb{N}$ · ECUE : OBM · Niveau : maths-s1-obm/10
Formules : injective : $f(x) = f(y) \Rightarrow x = y$ (contre-exemple : $f(a) = f(b)$, $a \neq b$) ; surjective : $\forall y, \exists x, y = f(x)$ (contre-exemple : un $y$ sans antécédent) ; $(g \circ f)(n) = g(f(n))$

Soient $f : \mathbb{N} \to \mathbb{N},\ n \mapsto n+1$ et $g : \mathbb{N} \to \mathbb{N},\ p \mapsto \begin{cases} 0 & \text{si } p = 0 \\ p-1 & \text{si } p \geqslant 1 \end{cases}$.
1. $f$ et $g$ sont-elles injectives ? Surjectives ? Justifier votre réponse.
2. Donner l'expression de $g \circ f$ et $f \circ g$.

## Exercice 5 (3 points)
Type : équation diophantienne $ax+by=c$ (Euclide, Gauss) · ECUE : HP (arithmétique)
Formules : Euclide : $a = bq + r$, $a \wedge b = b \wedge r$ ; solutions $\iff (a \wedge b) \mid c$ ; diviser par $d = a \wedge b$ ; remonter Euclide : $au_0 + bv_0 = d$ puis multiplier par $c/d$ ; Gauss : $a \mid bc$ et $a \wedge b = 1 \Rightarrow a \mid c$ ; $a(x - x_0) = -b(y - y_0)$ donne $x = x_0 + \frac{b}{d}k$, $y = y_0 - \frac{a}{d}k$, $k \in \mathbb{Z}$ ; vérifier la réciproque

1. En utilisant l'algorithme d'Euclide, déterminer une solution particulière de l'équation $972x + 504y = 72$.
2. En utilisant le théorème de Gauss, déterminer l'ensemble des couples $(x,y) \in \mathbb{Z}^2$ tels que $972x + 504y = 72$.

## Exercice 6 (2 points)
Type : division euclidienne (énigme) · ECUE : HP (arithmétique)
Formules : $n = bq + r$, $0 \leqslant r < b$ ; égaliser les deux écritures

« Je suis un entier naturel. Quand on me divise par 4, le reste est 3, mais quand on me divise par 5, le reste est 1 et le quotient inchangé. Qui suis-je ? »

## Exercice 7 (2 points)
Type : congruences, reste d'une puissance · ECUE : HP (arithmétique)
Formules : $a \equiv b\,[n] \Rightarrow a^k \equiv b^k\,[n]$ ; chercher la période : $a^p \equiv 1\,[n]$ ; division euclidienne de l'exposant $N = pq + r$ : $a^N = (a^p)^q a^r$ ; le reste est dans $[\![0, n-1]\!]$

Quel est le reste de la division euclidienne de $1357^{2013}$ par 5 ?

## Exercice 8 (2 points)
Type : multiplicité d'une racine d'un polynôme · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/4
Formules : $\alpha$ racine d'ordre $m$ $\iff P(\alpha) = P'(\alpha) = \dots = P^{(m-1)}(\alpha) = 0$ et $P^{(m)}(\alpha) \neq 0$ ; $(X^n)' = nX^{n-1}$

Déterminer l'ordre de multiplicité de la racine 1 du polynôme $P(X) = X^4 - 5X^3 + 9X^2 - 7X + 2$.

## Exercice 9 (2 points)
Type : lemme de Gauss et Bézout (démonstration) · ECUE : HP (arithmétique)
Formules : Bézout : $a \wedge b = 1 \iff \exists (u,v), au + bv = 1$ ; multiplier par $c$ : $acu + bcv = c$ ; $a \mid bc \Rightarrow bc = ak$ ; produit de deux relations de Bézout

Les deux questions sont indépendantes. Vous devez obligatoirement utiliser le théorème de Bézout dans les deux questions.
Soit $(a,b,c) \in \mathbb{N}^{*3}$.
1. On suppose $a \wedge b = 1$ et $a \mid bc$. Montrer que $a \mid c$.
2. On suppose $a \wedge b = 1$ et $a \wedge c = 1$. Montrer que $a \wedge (bc) = 1$.
