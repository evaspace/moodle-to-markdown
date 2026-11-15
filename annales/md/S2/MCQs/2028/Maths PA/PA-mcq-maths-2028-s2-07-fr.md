# QCM 7 (S2 PA) — lundi 6 mai 2024

- Source : `raw/S2/MCQs/2028/Maths PA/PA-mcq-maths-2028-s2-07-fr.pdf` (scan d'une copie annotée, 3 pages)
- Date réelle : 6 mai 2024 (S2-PA 2024, dossier promo 2028). Questions 11 à 20.
- Réponses : vérifiées à la main.

## Question 11
Type : propriétés de suites avec quantificateurs · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/3
Formules : bornée : $\exists m, M, \forall n, m \leqslant u_n \leqslant M$ ; non bornée : $\forall m, M, \exists n, u_n < m$ ou $u_n > M$ ; croissante : $\forall n, u_{n+1} \geqslant u_n$ ; monotone : croissante ou décroissante

Dire que $(u_n)$ est minorée signifie a. $\forall n, \exists m \in \mathbb{R}, u_n \geqslant m$ ; b. $\exists m \in \mathbb{R}, \forall n \in \mathbb{N}, u_n \geqslant m$ ; c. $\exists m, \exists n, u_n \geqslant m$ ; d. $\exists n, \forall m, u_n \geqslant m$ ; e. Aucune des autres réponses.

Réponse : b.

## Question 12
Type : monotonie d'une suite, somme géométrique · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/2
Formules : croissante : $\forall n, u_n \leqslant u_{n+1}$ ; signe de $u_{n+1} - u_n$ (même dénominateur) ; $\sum_{k=p}^{n} q^k = q^p\frac{1 - q^{n-p+1}}{1 - q}$

Soit $(u_n)$ strictement positive. Pour étudier sa monotonie, on peut a. comparer $u_{n+1} - u_n$ à 1 ; b. comparer $u_{n+1} - u_n$ à 0 ; c. comparer $\frac{u_{n+1}}{u_n}$ à 0 ; d. Aucune des autres réponses.

Réponse : b (ou comparer $\frac{u_{n+1}}{u_n}$ à 1).

## Question 13
Type : monotonie d'une suite, somme géométrique · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/2
Formules : croissante : $\forall n, u_n \leqslant u_{n+1}$ ; signe de $u_{n+1} - u_n$ (même dénominateur) ; $\sum_{k=p}^{n} q^k = q^p\frac{1 - q^{n-p+1}}{1 - q}$

La suite $\left(\frac1n\right)_{n \in \mathbb{N}^*}$ est a. croissante ; b. décroissante ; c. non monotone.

Réponse : b.

## Question 14
Type : limites usuelles de suites · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/4
Formules : $\cos n$ diverge (suites extraites) ; $\ln(n^2 + n) \to +\infty$ ; $|q| < 1 \Rightarrow q^n \to 0$ ; $\frac1n \to 0$

Laquelle converge ? a. $(u_n)$ avec $\lim u_n = +\infty$ ; b. $(v_n)$ avec $\lim v_n = 3$ ; c. $(w_n)$ avec $\lim w_n = 0$ ; d. $(z_n)$ sans limite ; e. Aucune des autres réponses.

Réponse : b et c.

## Question 15
Type : propriétés de suites avec quantificateurs · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/4
Formules : bornée : $\exists m, M, \forall n, m \leqslant u_n \leqslant M$ ; non bornée : $\forall m, M, \exists n, u_n < m$ ou $u_n > M$ ; croissante : $\forall n, u_{n+1} \geqslant u_n$ ; monotone : croissante ou décroissante

$(u_n)$ vérifie $\forall A > 0, \exists N \in \mathbb{N}, \forall n \geqslant N, u_n > A$. Cela signifie que a. $(u_n)$ tend vers 0 ; b. vers $-\infty$ ; c. vers $+\infty$ ; d. n'a pas de limite ; e. Aucune des autres réponses.

Réponse : c.

## Question 16
Type : propriétés de suites avec quantificateurs · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/3
Formules : bornée : $\exists m, M, \forall n, m \leqslant u_n \leqslant M$ ; non bornée : $\forall m, M, \exists n, u_n < m$ ou $u_n > M$ ; croissante : $\forall n, u_{n+1} \geqslant u_n$ ; monotone : croissante ou décroissante

La suite $\left(\frac{n}{n+1}\right)$ est a. majorée, non minorée ; b. bornée ; c. minorée, non majorée ; d. ni minorée, ni majorée ; e. Aucune des autres réponses.

Réponse : b ($0 \leqslant \frac n{n+1} < 1$).

## Question 17
Type : comparaison et limites · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/6
Formules : $u_n \leqslant v_n$ et $v_n \to -\infty \Rightarrow u_n \to -\infty$ ; $u_n \leqslant v_n$ et $u_n \to +\infty \Rightarrow v_n \to +\infty$ ; pour une limite finie, il faut deux gendarmes

$\forall n$, $2 \leqslant u_n \leqslant v_n$. a. On peut avoir $\lim u_n = -\infty$ ; b. $\lim u_n = +\infty \Rightarrow \lim v_n = +\infty$ ; c. $\lim v_n = 3 \Rightarrow \lim u_n = 3$ ; d. Aucune des autres réponses.

Réponse : b.

## Question 18
Type : limite de $q^n$ · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/4
Formules : $q > 1$ : $q^n \to +\infty$ ; $|q| < 1$ : $q^n \to 0$ ; $q = 1$ : 1 ; $q \leqslant -1$ : pas de limite

Soit $q \in \mathbb{R}$. a. Si $q > 1$, $q^n \to 0$ ; b. Si $q < 1$, $q^n \to 0$ ; c. Si $q \leqslant -1$, $(q^n)$ n'a pas de limite ; d. Aucune des autres réponses.

Réponse : c.

## Question 19
Type : limite d'une fraction rationnelle · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/5
Formules : en $\pm\infty$ : quotient des termes de plus haut degré, $\frac{x - 1}{x + 1} \sim \frac xx = 1$

$\lim_{n \to +\infty} \frac{2n^2 - 1}{n^2 + 1} = 2$. a. Vrai ; b. Faux.

Réponse : a.

## Question 20
Type : limites usuelles de suites · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/4
Formules : $\cos n$ diverge (suites extraites) ; $\ln(n^2 + n) \to +\infty$ ; $|q| < 1 \Rightarrow q^n \to 0$ ; $\frac1n \to 0$

Cochez la (les) suite(s) qui converge(nt) : a. $(e^n)$ ; b. $(e^{-n})$ ; c. $(\ln n)$ ; d. $(n^2)$ ; e. Aucune des autres réponses.

Réponse : b.
