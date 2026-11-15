# Correction du partiel de maths — janvier 2018

- Source : `raw/S1/Finals/Maths PC/2022/final-2022-s1-maths-correction-fr.pdf` (3 pages, corrigé rédigé par un étudiant ; accents restaurés)
- Date réelle : janvier 2018 (dossier promo 2022, titré « Partiel de Maths 2022 »). Sujet : `final-2022-s1-maths-subject-fr.md`.
- L'exercice 8 n'est pas corrigé dans le document.

## Exercice 1
Type : nier une phrase · ECUE : OBM · Niveau : maths-s1-obm/3
Formules : $\neg(\forall x, P(x)) \iff \exists x, \neg P(x)$ ; $\neg(\exists x, P(x)) \iff \forall x, \neg P(x)$ ; $\neg(P \Rightarrow Q) \iff P \wedge \neg Q$ ; $\neg(P \wedge Q) \iff \neg P \vee \neg Q$ ; $\neg(P \vee Q) \iff \neg P \wedge \neg Q$ ; « aucun » = $\forall, \neg$

1. Aucun étudiant n'aime organiser des soirées festives.
2. Tous les étudiants partiront dans la destination de leur choix au S4.
3. Certains étudiants de l'EPITA ne s'investissent pas dans leurs projets de prépas.
4. Certains étudiants de l'EPITA sont déçus par la formation de l'école axée sur le savoir-faire.

## Exercice 2
Type : récurrence (dérivée $n$-ième) · ECUE : OBM · Niveau : maths-s1-obm/7
Formules : récurrence ; $(\ln(1+x))' = \frac1{1+x}$ ; $((1+x)^{-n})' = -n(1+x)^{-n-1}$ ; $(n-1)! \cdot n = n!$

Soit $P(n)$ la proposition « $f^{(n)}(x) = \dfrac{(-1)^{n-1}(n-1)!}{(x+1)^n}$ » pour tout $n \in \mathbb{N}^*$.

Initialisation : $f^{(1)}(x) = (\ln(x+1))' = \dfrac{1}{x+1} = \dfrac{(-1)^0 (1-1)!}{(x+1)^1}$. $P(1)$ est vraie.

Hérédité : supposons que $f^{(n)}(x) = (-1)^{n-1}(n-1)!\,(x+1)^{-n}$. On dérive par rapport à $x$ :
$\left(f^{(n)}(x)\right)' = (-1)^{n-1}(n-1)!\,\left((x+1)^{-n}\right)'$. On reconnaît la forme $u^n$, de dérivée $n u' u^{n-1}$, d'où
$f^{(n+1)}(x) = (-1)^{n-1}(n-1)!\,(-n)(x+1)^{-n-1} = \dfrac{(-1)^n\, n!}{(x+1)^{n+1}}$. Donc $P(n+1)$ est vraie.

Conclusion : pour tout $n \in \mathbb{N}^*$, $f^{(n)}(x) = \dfrac{(-1)^{n-1}(n-1)!}{(x+1)^n}$.

## Exercice 3
Type : traduire avec quantificateurs · ECUE : OBM · Niveau : maths-s1-obm/4
Formules : « tout » $= \forall$, « il existe » $= \exists$, « aucun » $= \forall \dots \neg$ ; l'ordre $\forall\exists$ / $\exists\forall$ change le sens ; $f$ s'annule : $\exists x, f(x) = 0$ ; minimum en $a$ : $\exists a, \forall x, f(x) \geqslant f(a)$ ; pair : $\exists k, n = 2k$

1. $\exists x \in \mathbb{R},\ x^2 < x$.
2. $\exists n \in \mathbb{N}, \forall m \in \mathbb{N}, \exists k \in \mathbb{Z},\ n = km$ (le corrigé écrit $m = k\,n$, ce qui traduit « diviseur de tous les autres » ; la phrase demande un multiple).
3. $\nexists n \in \mathbb{N}, \forall m \in \mathbb{N},\ m \leqslant n$, ou $\forall n \in \mathbb{N}, \exists m \in \mathbb{N},\ n < m$.
4. $\forall x \in \mathbb{R}, \exists y \in \mathbb{R},\ y = \sqrt{x}$ (mieux : $\forall x \in \mathbb{R}, \exists y \in \mathbb{R},\ y^2 = x$).

## Exercice 4
Type : injectivité / surjectivité, composées sur $\mathbb{N}$ · ECUE : OBM · Niveau : maths-s1-obm/10
Formules : injective : $f(x) = f(y) \Rightarrow x = y$ (contre-exemple : $f(a) = f(b)$, $a \neq b$) ; surjective : $\forall y, \exists x, y = f(x)$ (contre-exemple : un $y$ sans antécédent) ; $(g \circ f)(n) = g(f(n))$

1. $\forall (n,m) \in \mathbb{N}^2$, si $n \neq m$, $n + 1 \neq m + 1$ donc $f$ est injective. $0 \in \mathbb{N}$ or $\nexists n \in \mathbb{N}$ tel que $n + 1 = 0$, donc $f$ n'est pas surjective.
$g(0) = 0$ et $g(1) = 1 - 1 = 0$ donc $g$ n'est pas injective. $\forall n \in \mathbb{N}$, $g(n+1) = n$ donc tout entier $n$ a au moins un antécédent par $g$ : $g$ est surjective.
2. $g \circ f : \mathbb{N} \to \mathbb{N},\ n \mapsto n$ et $f \circ g : \mathbb{N} \to \mathbb{N},\ n \mapsto \begin{cases} 1 & \text{si } n = 0 \\ n & \text{si } n \geqslant 1 \end{cases}$.

## Exercice 5
Type : équation diophantienne $ax+by=c$ (Euclide, Gauss) · ECUE : HP (arithmétique)
Formules : Euclide : $a = bq + r$, $a \wedge b = b \wedge r$ ; solutions $\iff (a \wedge b) \mid c$ ; diviser par $d = a \wedge b$ ; remonter Euclide : $au_0 + bv_0 = d$ puis multiplier par $c/d$ ; Gauss : $a \mid bc$ et $a \wedge b = 1 \Rightarrow a \mid c$ ; $a(x - x_0) = -b(y - y_0)$ donne $x = x_0 + \frac{b}{d}k$, $y = y_0 - \frac{a}{d}k$, $k \in \mathbb{Z}$ ; vérifier la réciproque

1. $972x + 504y = 72 \iff 36 \cdot 27x + 36 \cdot 14y = 36 \cdot 2 \iff 27x + 14y = 2$.
$27 = 14 \times 1 + 13$, $14 = 13 \times 1 + 1$, $13 = 13 \times 1 + 0$ : le PGCD vaut 1 et divise 2, il y a des solutions.
$1 = 14 - 13 = 14 - (27 - 14) = 14 \times 2 + 27 \times (-1)$, donc $2 = 27 \times (-2) + 14 \times 4$.
Une solution particulière est $(-2, 4)$.
2. Soient $x_0 = -2$, $y_0 = 4$. $27x + 14y = 2 \iff 27(x - x_0) = 14(y_0 - y)$.
$14 \mid 27(x - x_0)$ et $14 \wedge 27 = 1$ donc (Gauss) $14 \mid x - x_0$ : $\exists k \in \mathbb{Z}$, $x = 14k + x_0$.
Alors $27 \times 14k = 14(y_0 - y)$, soit $y = y_0 - 27k$.
Ensemble des solutions : $\{(14k - 2,\ 4 - 27k) ; k \in \mathbb{Z}\}$.

## Exercice 6
Type : division euclidienne (énigme) · ECUE : HP (arithmétique)
Formules : $n = bq + r$, $0 \leqslant r < b$ ; égaliser les deux écritures

Soit $n$ le nombre mystère : $n = 4q + 3$ et $n = 5q + 1$ ($q \in \mathbb{N}$, même quotient).
$4q + 3 = 5q + 1 \iff q = 2$, d'où $n = 5 \times 2 + 1 = 11$.

## Exercice 7
Type : congruences, reste d'une puissance · ECUE : HP (arithmétique)
Formules : $a \equiv b\,[n] \Rightarrow a^k \equiv b^k\,[n]$ ; chercher la période : $a^p \equiv 1\,[n]$ ; division euclidienne de l'exposant $N = pq + r$ : $a^N = (a^p)^q a^r$ ; le reste est dans $[\![0, n-1]\!]$

$1357 \equiv 2\,[5]$ donc $1357^{2013} \equiv 2^{2013} \equiv 2 \times 2^{2012} \equiv 2 \times 4^{1006} \equiv 2 \times (-1)^{1006}\,[5]$.
1006 est pair donc $(-1)^{1006} = 1$ : $1357^{2013} \equiv 2\,[5]$. Le reste est 2.

## Exercice 9
Type : lemme de Gauss et Bézout (démonstration) · ECUE : HP (arithmétique)
Formules : Bézout : $a \wedge b = 1 \iff \exists (u,v), au + bv = 1$ ; multiplier par $c$ : $acu + bcv = c$ ; $a \mid bc \Rightarrow bc = ak$ ; produit de deux relations de Bézout

1. $a \wedge b = 1$ donc d'après Bézout $\exists (u,v) \in \mathbb{Z}^2$, $au + bv = 1$, d'où $auc + bcv = c$.
Or $a \mid bc$ donc $\exists k \in \mathbb{Z}$, $ak = bc$, d'où $auc + kav = c$, soit $a(uc + kv) = c$. $uc + kv$ est un entier donc $a \mid c$.
2. $a \wedge b = 1$ et $a \wedge c = 1$ : $\exists (u_1,v_1), (u_2,v_2) \in \mathbb{Z}^2$, $au_1 + bv_1 = 1$ et $au_2 + cv_2 = 1$.
D'où $(au_1 + bv_1)(au_2 + cv_2) = 1 \iff a(au_1u_2 + bu_2v_1 + cu_1v_2) + bc(v_1v_2) = 1$.
Il existe donc deux entiers $U$ et $V$ tels que $aU + bcV = 1$, soit $a \wedge (bc) = 1$.
