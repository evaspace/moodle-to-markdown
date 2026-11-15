# QCM 1 (S1 PA) — lundi 2 octobre 2023

- Source : `raw/S1/MCQs/2028/Maths PA/PA-mcq-maths-2028-s1-01-fr.pdf` (scan d'une copie annotée, 3 pages)
- Date réelle : 2 octobre 2023 (S1-PA 2023, dossier promo 2028). Questions 11 à 20 (partie maths).
- Réponses : vérifiées à la main (les annotations de la copie scannée contiennent des erreurs, elles ne sont pas reprises).

## Question 11
Type : suite récurrente, calcul de termes · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/1
Formules : $u_{n+1} = f(u_n, n)$ : calculer $u_1$ puis $u_2$ ; géométrique $\iff u_{n+1} = qu_n$

Soit la suite $(u_n)$ définie par $u_0 = -2$ et : $\forall n \in \mathbb{N}$, $u_{n+1} = u_n^2 + n$. On a
a. $u_2 = 17$ ; b. $u_2 = 27$ ; c. $\forall n \in \mathbb{N}$, $u_n \geqslant 0$ ; d. $(u_n)$ est une suite géométrique ; e. Aucune des autres réponses.

Réponse : a ($u_1 = 4$, $u_2 = 16 + 1 = 17$ ; c faux car $u_0 < 0$).

## Question 12
Type : somme des termes d'une suite géométrique · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/1
Formules : $\sum_{k=0}^{n} q^k = \frac{1 - q^{n+1}}{1 - q}$ ($q \neq 1$) ; nombre de termes = $n + 1$

Soit $(u_n)$ une suite géométrique de raison $q \in \mathbb{R}$, $q \neq 1$. On a
a. $\sum_{k=0}^n q^k = \frac{1 - q^n}{1 - q}$ ; b. $\sum_{k=0}^n q^k = \frac{1 - q^{n-1}}{1 - q}$ ; c. $\sum_{k=0}^n q^k = \frac{1 - q^{n+1}}{1 - q}$ ; d. Aucune des autres réponses.

Réponse : c.

## Question 13
Type : suite arithmétique · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/1
Formules : $u_{n+1} = u_n + r$ ; $u_n = u_p + (n - p)r$

Soit $(u_n)$ une suite arithmétique de raison 2 avec $u_5 = 3$. On a
a. $u_{20} = u_{19} + 5$ ; b. $u_{20} = u_{19} + 2$ ; c. $u_{20} = 43$ ; d. $u_{20} = 33$ ; e. Aucune des autres réponses.

Réponse : b et d ($u_{20} = u_5 + 15 \times 2 = 33$).

## Question 14
Type : formes indéterminées · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/5
Formules : formes indéterminées : $\infty - \infty$, $0 \times \infty$, $\frac\infty\infty$, $\frac00$ ; $\frac{+\infty}{0^+} = +\infty$ et $\frac{0^+}{+\infty} = 0$ ne sont pas indéterminées

Soient deux suites $(u_n)$ et $(v_n)$ telles que $\lim u_n = +\infty$ et $\lim v_n = 0^+$. On a
a. La limite en $+\infty$ de la suite $(u_n + v_n)$ est une forme indéterminée.
b. La limite en $+\infty$ de la suite $(u_n \times v_n)$ est une forme indéterminée.
c. La limite en $+\infty$ de la suite $\left(\frac{u_n}{v_n}\right)$ est une forme indéterminée.
d. Aucune des autres réponses.

Réponse : b ($\infty \times 0$) ; $\frac{+\infty}{0^+} = +\infty$ n'est pas indéterminé.

## Question 15
Type : limites usuelles (polynôme) · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/4
Formules : limite d'un polynôme en $\pm\infty$ = limite du terme de plus haut degré

La limite en $+\infty$ de la suite $(u_n) = (-3n^2 + n - 12)$ est égale à
a. $+\infty$ ; b. 0 ; c. $-\infty$ ; d. Aucune des autres réponses.

Réponse : c.

## Question 16
Type : limites usuelles (produit) · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/4
Formules : $\frac1{\sqrt n} \to 0$, $\frac1{n^2} \to 0$ ; produit : $(+\infty) \times \ell = -\infty$ si $\ell < 0$

La limite en $+\infty$ de la suite $(u_n)$ où, pour tout $n \in \mathbb{N}^*$, $u_n = \left(n^2 - \frac1{n^2}\right) \times \left(\frac1{\sqrt n} - 5\right)$ est égale à
a. $+\infty$ ; b. 0 ; c. $-\infty$ ; d. $-5$ ; e. Aucune des autres réponses.

Réponse : c ($+\infty \times (-5)$).

## Question 17
Type : comparaison et limites · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/6
Formules : $u_n \leqslant v_n$ et $v_n \to -\infty \Rightarrow u_n \to -\infty$ ; $u_n \leqslant v_n$ et $u_n \to +\infty \Rightarrow v_n \to +\infty$ ; pour une limite finie, il faut deux gendarmes

Soient $(u_n)$ et $(v_n)$ deux suites telles que $\forall n \in \mathbb{N}$, $u_n \leqslant v_n$. On a
a. Si $\lim v_n = 0$ alors $\lim u_n = 0$ ;
b. Si $\lim v_n = +\infty$ alors $\lim u_n = +\infty$ ;
c. Si $\lim v_n = -\infty$ alors $\lim u_n = -\infty$ ;
d. Aucune des autres réponses.

Réponse : c.

## Question 18
Type : limite de $q^n$ · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/4
Formules : $q > 1$ : $q^n \to +\infty$ ; $|q| < 1$ : $q^n \to 0$ ; $q = 1$ : 1 ; $q \leqslant -1$ : pas de limite

Soit $q \in \mathbb{R}$. $\lim_{n \to +\infty} q^n$ est égale à
a. 0 si $q > 1$ ; b. $+\infty$ si $q > 1$ ; c. 0 si $q < 1$ ; d. $+\infty$ si $q < 1$ ; e. Aucune des autres réponses.

Réponse : b (c faux pour $q \leqslant -1$).

## Question 19
Type : théorème de la limite monotone · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/8
Formules : croissante majorée $\Rightarrow$ convergente ; décroissante minorée $\Rightarrow$ convergente ; croissante non majorée $\Rightarrow +\infty$

Soit $(u_n)$ une suite telle que $\forall n \in \mathbb{N}$, $u_n \geqslant 5$. On a
a. Si $(u_n)$ est croissante alors $(u_n)$ converge.
b. Si $(u_n)$ est décroissante alors $(u_n)$ converge.
c. $(u_n)$ est majorée.
d. $(u_n)$ est minorée.
e. Aucune des autres réponses.

Réponse : b et d.

## Question 20
Type : suites croissantes, contre-exemple · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/8
Formules : croissante majorée converge (contre-exemple $-\frac1n$) ; croissante non majorée tend vers $+\infty$

L'affirmation « Toute suite strictement croissante tend vers $+\infty$ » est a. vraie ; b. fausse.

Réponse : b (contre-exemple : $u_n = -\frac1n$).
