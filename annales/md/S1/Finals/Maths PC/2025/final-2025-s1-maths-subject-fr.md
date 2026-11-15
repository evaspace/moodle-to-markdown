# Partiel S1 — janvier 2021 (sujet, FR)

- Source : `raw/S1/Finals/Maths PC/2025/final-2025-s1-maths-subject-fr.pdf` (10 pages)
- Date réelle : janvier 2021 (S1 20-21, dossier promo 2025). Corrigé : `final-2025-s1-maths-correction-fr.md`.
- Durée : 3 heures. Barème sur 30 points ramenés à 20. Documents et calculatrices interdits.

## Exercice 1 (6 points)
Type : dénombrement de mains, probabilités totales et Bayes · ECUE : DP · Niveau : maths-s1-dp/10
Formules : équiprobabilité : $P(A) = \frac{|A|}{|\Omega|}$ ; $|\Omega| = \binom{32}{5}$ ; $\binom nk = \frac{n!}{k!(n-k)!}$ ; partition : $A_i$ deux à deux disjoints et $\bigsqcup A_i = \Omega$ ; probabilités totales : $P(B) = \sum P(B \mid A_i)P(A_i)$ ; Bayes : $P(A \mid B) = \frac{P(B \mid A)P(A)}{P(B)}$

A et B jouent avec un jeu de 32 cartes au jeu suivant : A tire une main de 5 cartes au hasard dans le jeu, puis B tire une carte au hasard parmi les 5 cartes de la main de A. B gagne s'il tire un valet. On appelle $\Omega$ l'univers des possibles.
Si les probabilités trouvées s'expriment avec des combinaisons ou des arrangements, il ne vous est pas demandé de les calculer.

a. Déterminer la probabilité que la main tirée par A contienne exactement 3 valets.
b. Déterminer la probabilité que la main tirée par A contienne exactement 3 valets et 3 piques.
c. Soit $k \in [\![0, 4]\!]$. On appelle $V_k$ l'évènement : « La main tirée par A contient exactement $k$ valet(s) ». Rappeler, sans la démontrer, ce que signifie l'affirmation : $\{V_0, V_1, V_2, V_3, V_4\}$ forment une partition de $\Omega$.

Dans les questions d. et e., seule la formule théorique est attendue et pas d'application numérique.

d. On appelle $B_V$ l'évènement : « B tire un valet ». En utilisant la partition ci-dessus, écrire la formule des probabilités totales pour $P(B_V)$.
e. À l'aide de la formule de Bayes, exprimer la probabilité qu'il y ait eu exactement 3 valets parmi les 5 cartes tirées par A, sachant que B tire un valet.

## Exercice 2 (3 points)
Type : loi binomiale et loi uniforme (espérance, variance) · ECUE : DP · Niveau : maths-s1-dp/14
Formules : $X \sim \mathcal{B}(n,p)$ : $P(X = k) = \binom nk p^k(1-p)^{n-k}$, $E(X) = np$, $V(X) = np(1-p)$ ; uniforme sur $[\![1,n]\!]$ : $P(Y = k) = \frac1n$, $E(Y) = \frac{n+1}2$ ; $\sum_{k=1}^n k = \frac{n(n+1)}2$

Soient $(\Omega, \mathcal{P}(\Omega), P)$ un espace probabilisé, et $X$ et $Y$ deux variables aléatoires finies définies sur $\Omega$.
1. $X$ suit une loi binomiale de paramètres $n = 10$ et $p = \frac14$. Déterminer son espérance, sa variance ainsi que $P(X = 3)$ sous forme de fraction simplifiée.
2. $Y$ suit une loi uniforme sur $[\![1, 10]\!]$. Déterminer son espérance.

## Exercice 3 (3 points)
Type : petit théorème de Fermat, reste d'une puissance · ECUE : HP (arithmétique)
Formules : Fermat : $p$ premier, $p \nmid a \Rightarrow a^{p-1} \equiv 1\,[p]$ ; $a \equiv b\,[n] \Rightarrow a^k \equiv b^k\,[n]$ ; $a^{q(p-1)+r} \equiv a^r\,[p]$

En utilisant le petit théorème de Fermat dont vous rappellerez l'énoncé, déterminer le reste de la division euclidienne de $2021^{362}$ par 19.

## Exercice 4 (5 points)
Type : équation diophantienne $ax+by=c$ (Euclide, Gauss) · ECUE : HP (arithmétique)
Formules : Euclide : $a = bq + r$, $a \wedge b = b \wedge r$ ; solutions $\iff (a \wedge b) \mid c$ ; diviser par $d = a \wedge b$ ; remonter Euclide : $au_0 + bv_0 = d$ puis multiplier par $c/d$ ; Gauss : $a \mid bc$ et $a \wedge b = 1 \Rightarrow a \mid c$ ; $a(x - x_0) = -b(y - y_0)$ donne $x = x_0 + \frac{b}{d}k$, $y = y_0 - \frac{a}{d}k$, $k \in \mathbb{Z}$ ; vérifier la réciproque

On appelle $(E)$ l'équation : « $630x - 195y = 30$ ; $(x,y) \in \mathbb{Z}^2$ ».
1. À l'aide de l'algorithme d'Euclide, déterminer une solution particulière de $(E)$.
2. En utilisant le lemme de Gauss, déterminer l'ensemble des solutions de $(E)$.

## Exercice 5 (3 points)
Type : divisibilité de polynômes, multiplicité d'une racine · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/4
Formules : $(X-a)(X-b) \mid P \iff P(a) = P(b) = 0$ ($a \neq b$) ; $\alpha$ racine d'ordre $m$ $\iff P(\alpha) = \dots = P^{(m-1)}(\alpha) = 0$, $P^{(m)}(\alpha) \neq 0$ ; $(X^n)' = nX^{n-1}$

Soit $n \in \mathbb{N}^*$.
1. Montrer que $(X-1)(X-2)$ divise $P(X) = n\left((X-1)^{n+1} - X\right) + \left((X-1)^n - X\right) + (n+1)$.
2. Montrer que $-1$ est racine de $Q(X) = (2n+1)X^{2n+3} + (2n+3)X^{2n+2} + (2n+3)(X+1) - 2$. Déterminer sa multiplicité exacte.

## Exercice 6 (3 points)
Type : factorisation d'un polynôme dans $\mathbb{R}[X]$ · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/6
Formules : $P(a) = 0 \iff X - a \mid P$ ; division euclidienne $A = BQ + R$ ; $\Delta = b^2 - 4ac < 0 \Rightarrow aX^2 + bX + c$ irréductible dans $\mathbb{R}[X]$

On considère le polynôme $R(X) = X^4 + 3X^3 + 3X^2 - X - 6$.
1. Montrer que 1 et $-2$ sont racines de $R$.
2. En vous aidant d'une division euclidienne, factoriser $R$ en produit de polynômes irréductibles dans $\mathbb{R}[X]$.

## Exercice 7 (4 points)
Type : suites adjacentes via une suite géométrique · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/9
Formules : $w_{n+1} = qw_n \Rightarrow w_n = w_0q^n$ ; $|q| < 1 \Rightarrow q^n \to 0$ ; adjacentes : une croissante, l'autre décroissante, différence $\to 0$

Soient $(u_n)_{n \in \mathbb{N}}$ et $(v_n)_{n \in \mathbb{N}}$ deux suites définies par :
$u_0 = 1$, $\forall n \in \mathbb{N}$, $u_{n+1} = \dfrac{4u_n + v_n}{5}$ et $v_0 = 0$, $\forall n \in \mathbb{N}$, $v_{n+1} = \dfrac{u_n + 4v_n}{5}$.
1. Soit $(w_n)_{n \in \mathbb{N}}$ définie par : $\forall n \in \mathbb{N}$, $w_n = u_n - v_n$. Montrer que $(w_n)$ est géométrique, déterminer $w_n$ en fonction de $n$, déterminer son signe et sa limite en $+\infty$.
2. Montrer que $(u_n)$ et $(v_n)$ sont adjacentes.

## Exercice 8 (3 points)
Type : comparaison de suites ($\sim$, $o$, $O$) · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/12
Formules : $u_n \sim v_n \iff \frac{u_n}{v_n} \to 1$ ; $u_n = o(v_n) \iff \frac{u_n}{v_n} \to 0$ ; $u_n = O(v_n) \iff \frac{u_n}{v_n}$ bornée ; convergente $\Rightarrow$ bornée, donc $\sim$ et $o$ impliquent $O$ ; croissances comparées : $\frac{\ln n}{n^a} \to 0$, $\frac{n^a}{e^n} \to 0$ ; $\frac{\sin n}{n} \to 0$ ; factoriser par le terme dominant

Comparer les couples suivants, à l'aide des comparateurs de Landau $\sim$, $= o(\cdot)$, $= O(\cdot)$, en citant toutes les comparaisons possibles. Justifiez vos réponses.
1. $u_n = n^2 + 3n$ et $v_n = 2n^2 + 3$.
2. $u_n = n^2$ et $v_n = n\sin(n)$.
3. $u_n = \ln(n) + e^n + n$ et $v_n = \ln(n^2) + e^n + 2$.
