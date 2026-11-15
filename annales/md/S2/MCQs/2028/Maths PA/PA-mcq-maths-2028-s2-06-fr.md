# QCM 6 (S2 PA) — lundi 15 avril 2024

- Source : `raw/S2/MCQs/2028/Maths PA/PA-mcq-maths-2028-s2-06-fr.pdf` (scan d'une copie annotée, 3 pages)
- Date réelle : 15 avril 2024 (S2-PA 2024, dossier promo 2028). Questions 11 à 20.
- Réponses : vérifiées à la main.

## Question 11
Type : divisibilité et division euclidienne (vrai/faux) · ECUE : HP (arithmétique)
Formules : $a \mid b \iff \exists k \in \mathbb{Z}, b = ka$ ; $a \mid b$ et $b \mid a \Rightarrow a = \pm b$ ; $a \mid b$, $a \mid c \Rightarrow a \mid bu + cv$ ; contre-exemple $2 \mid 4$, $4 \mid 4$, $8 \nmid 4$ ; $a \mid bc \not\Rightarrow a \mid b$ ou $a \mid c$ ($6 \mid 2 \times 3$) ; division euclidienne $0 \leqslant r < |b|$

Soit $(a, b, c) \in \mathbb{Z}^3$ tel que $a \mid b$ et $a \mid c$. a. $a \mid -2b + 3c$ ; b. $a \mid bc$ ; c. $a$ est un diviseur de $b$ ; d. $a$ est un multiple de $b$ ; e. Aucune des autres réponses.

Réponse : a, b et c.

## Question 12
Type : division euclidienne dans $\mathbb{Z}$ · ECUE : HP (arithmétique)
Formules : $\exists!\,(q, r)$, $a = bq + r$, $0 \leqslant r < |b|$ ; ajuster : $a = bq + r = b(q+1) + (r - b)$ ; pour $-a$ : $-a = b(-q) - r = b(-q-1) + (b - r)$

$295 = 7 \times 41 + 8$. a. Le quotient de la division euclidienne de 295 par 7 est 41 ; b. il est 42 ; c. Aucune des autres réponses.

Réponse : b ($295 = 7 \times 42 + 1$).

## Question 13
Type : congruences (définition, opérations) · ECUE : HP (arithmétique)
Formules : $a \equiv b\,[n] \iff n \mid a - b$ ; compatibilité avec $+$, $\times$, puissances ; $ab - cd = a(b - d) + d(a - c)$ ; réduire chaque nombre modulo $n$ ; reste dans $[\![0, n-1]\!]$

a. $28 \equiv 4\,[12]$ ; b. $28 \equiv -4\,[12]$ ; c. $12^3 \equiv 3\,[9]$ ; d. $12^3 \equiv 0\,[9]$ ; e. Aucune des autres réponses.

Réponse : a et d.

## Question 14
Type : Bézout (énoncé), diviseurs communs et PGCD · ECUE : HP (arithmétique)
Formules : Bézout : $a \wedge b = 1 \iff \exists (u,v), au + bv = 1$ ; corollaire : $\exists (u,v), au + bv = a \wedge b$ ; $d \mid a$ et $d \mid b \Rightarrow d \mid au + bv$ ; transitivité de $\mid$

Soit $(a, b) \in \mathbb{Z}^2$ tel que $3a + 2b = 7$. Alors $a \wedge b = 7$. a. Vrai ; b. Faux.

Réponse : b (seulement $a \wedge b \mid 7$ ; ex. $a = 1$, $b = 2$).

## Question 15
Type : petit théorème de Fermat (énoncé, démonstration, application) · ECUE : HP (arithmétique)
Formules : Fermat : $p$ premier $\Rightarrow \forall n, n^p \equiv n\,[p]$ ; si $p \nmid n$, $n^{p-1} \equiv 1\,[p]$ ; binôme $(n+1)^p = \sum_k \binom pk n^k$ et $p \mid \binom pk$ pour $1 \leqslant k \leqslant p-1$ (récurrence) ; Gauss pour simplifier par $n$ ; $a^{6q+r} \equiv a^r\,[7]$

Soient $(n, p) \in \mathbb{N}^2$ avec $p$ premier. a. $p^n \equiv p\,[n]$ ; b. $n^p \equiv n\,[p]$ ; c. $p^{n-1} \equiv p\,[n]$ ; d. $n^{p-1} \equiv n\,[p]$ ; e. Aucune des autres réponses.

Réponse : b.

## Question 16
Type : décomposition en facteurs premiers, diviseurs communs · ECUE : HP (arithmétique)
Formules : $a \wedge b = \prod p^{\min(\alpha_p, \beta_p)}$ ; $d \mid a$ et $d \mid b \iff d \mid a \wedge b$ (Bézout) ; diviseurs de $\prod p_i^{\gamma_i}$ : $\prod p_i^{\delta_i}$, $0 \leqslant \delta_i \leqslant \gamma_i$ ; nombre : $\prod(\gamma_i + 1)$

Soit $a = 2^3 \times 3^2 \times 7$. a. $16 \mid a$ ; b. $24 \mid a$ ; c. $28 \mid a$ ; d. Aucune des autres réponses.

Réponse : b et c.

## Question 17
Type : degré, division euclidienne de polynômes, racine · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/2
Formules : $\deg(A+B) \leqslant \max(\deg A, \deg B)$ ; $\deg(AB) = \deg A + \deg B$ ; $\exists!\,(Q,R)$, $A = BQ + R$, $\deg R < \deg B$ ; $\alpha$ racine $\iff A(\alpha) = 0 \iff X - \alpha \mid A$

Le degré de $P(X) = X^2(X + 2)^5$ est a. 10 ; b. 7 ; c. 2 ; d. Aucune des autres réponses.

Réponse : b.

## Question 18
Type : degré, division euclidienne de polynômes, racine · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/2
Formules : $\deg(A+B) \leqslant \max(\deg A, \deg B)$ ; $\deg(AB) = \deg A + \deg B$ ; $\exists!\,(Q,R)$, $A = BQ + R$, $\deg R < \deg B$ ; $\alpha$ racine $\iff A(\alpha) = 0 \iff X - \alpha \mid A$

$A$, $B \in \mathbb{R}[X]$, $B \neq 0$. Faire la division euclidienne de $A$ par $B$, c'est trouver $Q$ et $R$ tels que a. $A = BQ + R$ ; b. $A = BQ + R$ avec $R < B$ ; c. $A = BQ + R$ avec $0 \leqslant R < B$ ; d. Aucune des autres réponses.

Réponse : d (il faut $\deg R < \deg B$).

## Question 19
Type : degré, division euclidienne de polynômes, racine · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/2
Formules : $\deg(A+B) \leqslant \max(\deg A, \deg B)$ ; $\deg(AB) = \deg A + \deg B$ ; $\exists!\,(Q,R)$, $A = BQ + R$, $\deg R < \deg B$ ; $\alpha$ racine $\iff A(\alpha) = 0 \iff X - \alpha \mid A$

Soit $P(X) = 2X(X + 1)^4$. a. 0 est une racine de $P$ ; b. 1 est une racine de $P$ ; c. $P$ n'a pas de racine réelle ; d. Aucune des autres réponses.

Réponse : a.

## Question 20
Type : degré, division euclidienne de polynômes, racine · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/2
Formules : $\deg(A+B) \leqslant \max(\deg A, \deg B)$ ; $\deg(AB) = \deg A + \deg B$ ; $\exists!\,(Q,R)$, $A = BQ + R$, $\deg R < \deg B$ ; $\alpha$ racine $\iff A(\alpha) = 0 \iff X - \alpha \mid A$

Cochez le(s) polynôme(s) de $\mathbb{R}[X]$ : a. $X + \sqrt X$ ; b. $-X^5 + X^4 + 9X - 8$ ; c. $\ln(X)$ ; d. $X^{-1} + 2X$ ; e. Aucune des autres réponses.

Réponse : b.
