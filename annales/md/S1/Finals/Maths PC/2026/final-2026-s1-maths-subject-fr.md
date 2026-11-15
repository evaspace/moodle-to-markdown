# Partiel S1 — janvier 2022 (sujet, FR)

- Source : `raw/S1/Finals/Maths PC/2026/final-2026-s1-maths-subject-fr.pdf` (10 pages)
- Date réelle : janvier 2022 (dossier promo 2026). Corrigé : `final-2026-s1-maths-correction-fr.md`.
- Durée : 3 heures. Barème sur 30 points ramené à 20. 7 exercices. Documents et calculatrices interdits.

## Exercice 1 (4 points)
Type : équation diophantienne $ax+by=c$ (Euclide, Gauss) · ECUE : HP (arithmétique)
Formules : Euclide : $a = bq + r$, $a \wedge b = b \wedge r$ ; solutions $\iff (a \wedge b) \mid c$ ; diviser par $d = a \wedge b$ ; remonter Euclide : $au_0 + bv_0 = d$ puis multiplier par $c/d$ ; Gauss : $a \mid bc$ et $a \wedge b = 1 \Rightarrow a \mid c$ ; $a(x - x_0) = -b(y - y_0)$ donne $x = x_0 + \frac{b}{d}k$, $y = y_0 - \frac{a}{d}k$, $k \in \mathbb{Z}$ ; vérifier la réciproque

On considère l'équation $(E)$ $203x - 84y = 14$ d'inconnues $(x,y) \in \mathbb{Z}^2$.
1. À l'aide de l'algorithme d'Euclide, trouver une solution particulière de $(E)$.
2. En utilisant le lemme de Gauss, trouver l'ensemble des solutions de $(E)$.

## Exercice 2 (2,5 points)
Type : congruences et Fermat, divisibilité · ECUE : HP (arithmétique)
Formules : $a \equiv b\,[n] \Rightarrow a^k \equiv b^k\,[n]$ ; Fermat : $p$ premier $\Rightarrow a^p \equiv a\,[p]$ ; $a^{mn+r} = (a^m)^n a^r$ ; $n \mid A \iff A \equiv 0\,[n]$

Soient $n \in \mathbb{N}$ et $A_n = 15^{4n+2} - 5^{2n+11}$. Montrer, sans récurrence, que $11 \mid A_n$.

## Exercice 3 (3 points)
Type : Bézout (énoncé), diviseurs communs et PGCD · ECUE : HP (arithmétique)
Formules : Bézout : $a \wedge b = 1 \iff \exists (u,v), au + bv = 1$ ; corollaire : $\exists (u,v), au + bv = a \wedge b$ ; $d \mid a$ et $d \mid b \Rightarrow d \mid au + bv$ ; transitivité de $\mid$

Soit $(a,b) \in (\mathbb{N}^*)^2$.
1. Énoncer avec soin le théorème de Bézout ainsi que son corollaire.
2. Soit $d \in \mathbb{N}^*$. Montrer que $d \mid a$ et $d \mid b \iff d \mid a \wedge b$.

## Exercice 4 (5,5 points)
Type : suites adjacentes, suites extraites $(u_{2n})$, $(u_{2n+1})$ · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/9
Formules : adjacentes : une croissante, l'autre décroissante, différence $\to 0$ ; $u_{2n+2} - u_{2n}$ = deux termes de la somme ; $\frac1{a^2} - \frac1{b^2} = \frac{(b-a)(b+a)}{a^2b^2}$ ; $(u_{2n})$ et $(u_{2n+1})$ même limite $\Rightarrow (u_n)$ converge

On considère la suite $(u_n)$ définie pour tout $n \in \mathbb{N}^*$ par : $u_n = \displaystyle\sum_{k=1}^{n} \frac{(-1)^k}{k^2}$.
1. Rappeler la définition de : « Les suites $(v_n)$ et $(w_n)$ sont adjacentes ».
2. Montrer que les deux suites extraites $(v_n) = (u_{2n})$ et $(w_n) = (u_{2n+1})$ sont adjacentes.
3. La suite $(u_n)$ est-elle convergente ? Justifiez votre réponse.

## Exercice 5 (6 points)
Type : suite récurrente $u_{n+1} = f(u_n)$ · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/10
Formules : constante $\iff u_0 = f(u_0)$ ; tableau de variations via $f'$ ; $f$ croissante sur $I$ et $u_n \in I \Rightarrow f(a) < f(u_n) < f(b)$ (récurrence) ; signe de $u_{n+1} - u_n$ ; monotone bornée $\Rightarrow$ convergente ; $\ell = f(\ell)$

Considérons la fonction $f : x \mapsto \dfrac{-x^2 - x - 4}{4}$. On définit alors la suite $(u_n)$ par $u_{n+1} = f(u_n)$, $u_0 \in \mathbb{R}$ donné.
1. Pour quelle(s) valeur(s) de $u_0$ cette suite est-elle constante ?
2. Faire le tableau (complet) des variations de $f$ sur $]-\infty, 0]$.
3. Pour la suite de l'exercice, nous prendrons $u_0 = -2$. Montrer que $\forall n \in \mathbb{N}$, $u_n \in ]-4, -1[$.
4. Étudier la monotonie de $(u_n)$.
5. La suite $(u_n)$ est-elle convergente ? Si oui, donner sa limite.

## Exercice 6 (4,5 points)
Type : comparaison de suites ($\sim$, $o$, $O$), développements · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/12
Formules : $u_n \sim v_n \iff \frac{u_n}{v_n} \to 1$ ; $o$ : quotient $\to 0$ ; $O$ : quotient borné ; $o(\frac1{n^2}) = \frac{\varepsilon_n}{n^2}$, $\varepsilon_n \to 0$ ; $u_n \sim$ premier terme non nul du développement ; croissances comparées $\frac{\ln n}n \to 0$

1. Comparer en $+\infty$ les suites $(u_n)$ et $(v_n)$ suivantes à l'aide des comparateurs de Landau $\sim$, $= o(\cdot)$, $= O(\cdot)$ en citant toutes les comparaisons possibles et en justifiant vos réponses.
   (a) $u_n = -2n^3 + n + 3$ et $v_n = 1 - n^2$.
   (b) $u_n = e^{-n} - \ln(n) + n$ et $v_n = n + 1$.
2. On considère une suite $(u_n)$ telle qu'au voisinage de $+\infty$, $u_n = \dfrac1n - \dfrac1{2n^2} + o\!\left(\dfrac1{n^2}\right)$.
   (a) Comment peut-on réécrire $o\!\left(\frac1{n^2}\right)$ ?
   (b) Montrer que $u_n \sim \frac1n$ en $+\infty$.
   (c) Donner un équivalent en $+\infty$ de $v_n = u_n - \frac1n$.

## Exercice 7 (4,5 points)
Type : divisibilité, $24 \mid p^2 - 1$ pour $p$ premier $\geqslant 5$ · ECUE : HP (arithmétique)
Formules : Bézout ; $a \wedge b = 1$, $a \mid c$, $b \mid c \Rightarrow ab \mid c$ ; division euclidienne par 3 : $d = 3q + r$, $r \in \{0,1,2\}$ ; $p^2 - 1 = (p-1)(p+1)$ ; $k(k+1)$ est pair ; $24 = 8 \times 3$, $8 \wedge 3 = 1$

N.B. : Les questions de cet exercice sont interdépendantes. Si vous n'avez pas répondu à certaines d'entre elles, n'hésitez pas à admettre leurs résultats et à les réutiliser, si besoin, dans des questions ultérieures. La question 1.(a) est une question bonus que vous pouvez admettre mais le résultat sera utile ensuite.
1. Soient $a$, $b$ et $c$ trois entiers naturels non nuls.
   (a) (Bonus) Montrer que $(a \wedge b = 1,\ a \mid c$ et $b \mid c) \implies ab \mid c$.
   (b) Montrer que si $a \mid b$ ou $a \mid c$ alors $a \mid bc$.
   (c) Considérons trois entiers consécutifs $d$, $d+1$ et $d+2$ avec $d \in \mathbb{N}^*$ fixé. En discutant sur le reste de la division euclidienne de $d$ par 3, montrer que 3 divise l'un d'entre eux, c'est-à-dire : $3 \mid d$ ou $3 \mid d+1$ ou $3 \mid d+2$.
2. Soit $p$ un nombre premier supérieur ou égal à 5.
   (a) Expliquer pourquoi $2 \mid p-1$ et $2 \mid p+1$.
   (b) En déduire que $\exists k \in \mathbb{N}$ tel que $p - 1 = 2k$ et $p + 1 = 2(k+1)$ puis que $8 \mid p^2 - 1$.
   (c) Expliquer pourquoi $p$ est premier avec 3. Puis, en considérant les entiers $p-1$, $p$ et $p+1$, montrer que $3 \mid p^2 - 1$.
   (d) En déduire que $24 \mid p^2 - 1$.
