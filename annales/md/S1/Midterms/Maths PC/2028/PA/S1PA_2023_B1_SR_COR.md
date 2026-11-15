# Correction examen B1-SR (S1 PA) — octobre 2023

- Source : `raw/S1/Midterms/Maths PC/2028/PA/S1PA_2023_B1_SR_COR.pdf` (2 pages, corrigé avec énoncés)
- Date réelle : octobre 2023 (parcours PA, dossier promo 2028). Pas de sujet séparé.

## Exercice 1 : en vrac
Type : monotonie d'une suite, somme géométrique · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/2
Formules : croissante : $\forall n, u_n \leqslant u_{n+1}$ ; signe de $u_{n+1} - u_n$ (même dénominateur) ; $\sum_{k=p}^{n} q^k = q^p\frac{1 - q^{n-p+1}}{1 - q}$

1. Soit $(u_n)$ une suite.
   (a) Rappeler la définition (avec les quantificateurs) de « $(u_n)$ est croissante » : $\forall n \in \mathbb{N}, u_n \leqslant u_{n+1}$.
   (b) Que signifie « $(u_n)$ est monotone » ? Croissante ou décroissante : $(\forall n, u_n \leqslant u_{n+1}) \vee (\forall n, u_{n+1} \leqslant u_n)$.
   (c) Étudier la monotonie de $(u_n)$ : $\forall n \in \mathbb{N}$, $u_n = \dfrac{-2n + 3}{n + 1}$.
   $u_{n+1} - u_n = \dfrac{-2n + 1}{n + 2} - \dfrac{-2n + 3}{n + 1} = \dfrac{(-2n + 1)(n + 1) - (-2n + 3)(n + 2)}{(n + 1)(n + 2)} = \dfrac{-5}{(n + 2)(n + 1)} \leqslant 0$ : $(u_n)$ décroissante.
2. Soit $S = 3^2 + 3^3 + 3^4 + \dots + 3^{12}$. Écrire $S$ à l'aide du symbole $\sum$. Calculer $S$.
$S = \displaystyle\sum_{k=2}^{12} 3^k = 3^2 \times \frac{1 - 3^{11}}{1 - 3} = -\frac92(1 - 3^{11}) = \frac92(3^{11} - 1)$.

## Exercice 2 : limite de suites
Type : formes indéterminées, croissances comparées · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/5
Formules : factoriser par le terme dominant ; $\frac{e^n}{n} \to +\infty$, $\frac{n}{e^n} \to 0$ ; $q^n \to +\infty$ si $q > 1$, $\to 0$ si $|q| < 1$ ; $\sqrt{n+1} = \sqrt n\sqrt{1 + \frac1n}$

Dans cet exercice, vous prendrez soin de votre rédaction.
1. Trouver $\lim_{n \to +\infty} -3n^3 + n^2 - 6e^{-n}$.
$-3n^3 + n^2 - 6e^{-n} = -3n^3\left(1 - \frac1{3n}\right) - 6e^{-n}$ ; $-3n^3 \to -\infty$, $1 - \frac1{3n} \to 1$, $6e^{-n} \to 0$ : limite $-\infty$.
2. Trouver $\lim_{n \to +\infty} \dfrac{\sqrt{n + 1}}{n + 2}$.
$\dfrac{\sqrt{n+1}}{n+2} = \dfrac{\sqrt n\sqrt{1 + \frac1n}}{n\left(1 + \frac2n\right)} = \dfrac{\sqrt{1 + \frac1n}}{\sqrt n\left(1 + \frac2n\right)} \to 0$.
3. Trouver $\lim_{n \to +\infty} \dfrac{e^n + n}{n + 1}$.
$\dfrac{e^n + n}{n + 1} = \dfrac{e^n}n \times \dfrac{1 + \frac n{e^n}}{1 + \frac1n}$ ; $\frac{e^n}n \to +\infty$ (croissances comparées), $\frac n{e^n} \to 0$ : limite $+\infty$.
4. Trouver $\lim_{n \to +\infty} 2^n - 4^n$.
$2^n - 4^n = 4^n\left(\left(\frac24\right)^n - 1\right) = 4^n\left(\frac1{2^n} - 1\right)$ ; $4^n \to +\infty$ et $\frac1{2^n} \to 0$ : limite $-\infty$.

## Exercice 3 : limite et comparaison
Type : comparaison et limites · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/6
Formules : $u_n \leqslant v_n$ et $v_n \to -\infty \Rightarrow u_n \to -\infty$ ; $u_n \leqslant v_n$ et $u_n \to +\infty \Rightarrow v_n \to +\infty$ ; pour une limite finie, il faut deux gendarmes

On considère la suite $(u_n)$ telle que, pour tout $n \in \mathbb{N}$, $u_n = (n + 1)^2 + (-1)^n \times n$.
1. Montrer (sans récurrence) que $\forall n \in \mathbb{N}$, $n^2 + n + 1 \leqslant u_n$.
$-1 \leqslant (-1)^n$ donc $-n \leqslant (-1)^n n$, d'où $(n+1)^2 - n \leqslant u_n$ et $(n+1)^2 - n = n^2 + n + 1$.
2. En déduire le comportement de $(u_n)$ en $+\infty$. $n^2 + n + 1 \to +\infty$ donc, par comparaison, $u_n \to +\infty$.

## Exercice 4 : étude d'une suite
Type : monotonie par quotient, récurrence, gendarmes · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/6
Formules : $u_n > 0$ et $\frac{u_{n+1}}{u_n} \leqslant 1 \Rightarrow$ décroissante ; $\frac{(n+1)!}{n!} = n + 1$ ; décroissante minorée $\Rightarrow$ convergente ; gendarmes $0 \leqslant u_n \leqslant v_n \to 0$ ; $|q| < 1 \Rightarrow q^n \to 0$

Soit $(u_n)$ définie pour tout $n \in \mathbb{N}^*$ par $u_n = \dfrac{2^n}{n!}$.
1. Étudier la monotonie de la suite $(u_n)$.
$u_n > 0$ et $\dfrac{u_{n+1}}{u_n} = \dfrac{2^{n+1}}{(n+1)!} \times \dfrac{n!}{2^n} = \dfrac2{n+1} \leqslant 1$ car $n + 1 \geqslant 2$ : $(u_n)$ décroissante.
2. Peut-on en déduire le comportement de $(u_n)$ en $+\infty$ ? $(u_n)$ est décroissante et minorée par 0 : elle converge.
3. Montrer par récurrence que pour tout entier naturel $n \geqslant 2$, $2 \times 3^{n-2} \leqslant n!$.
$n = 2$ : $2 \times 3^0 = 2 = 2!$. Si $2 \times 3^{n-2} \leqslant n!$, alors $(n+1)! = n!(n+1) \geqslant 2 \times 3^{n-2}(n + 1) \geqslant 2 \times 3^{n-2} \times 3 = 2 \times 3^{n-1}$ (car $n + 1 \geqslant 3$).
4. En déduire la limite de la suite $(u_n)$ en $+\infty$.
$\frac1{n!} \leqslant \frac1{2 \times 3^{n-2}}$, donc $0 \leqslant u_n \leqslant \frac{2^n}{2 \times 3^{n-2}} = \frac92\left(\frac23\right)^n$. Comme $\left|\frac23\right| < 1$, $\left(\frac23\right)^n \to 0$ : par les gendarmes, $u_n \to 0$.
