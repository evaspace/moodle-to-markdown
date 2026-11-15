# Partiel S1 — janvier 2023 (sujet, FR)

- Source : `raw/S1/Finals/Maths PC/2027/final-2027-s1-maths-subject-fr.pdf` (10 pages)
- Date réelle : janvier 2023 (dossier promo 2027). Corrigé : `final-2027-s1-maths-correction-fr.md`.
- Durée : 3 heures. Barème sur 40 points, divisé par 2. 8 exercices. Rigueur de rédaction prise en compte ; malus d'un point pour les copies manquant de propreté. Documents et calculatrices interdits.

## Exercice 1 : encore des intégrales (3 points)
Type : intégrale par primitive directe ($u'u^\alpha$, $u'/u$) · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/5
Formules : $\int u'u^\alpha = \frac{u^{\alpha+1}}{\alpha+1}$ ($\alpha \neq -1$) ; $\int \frac{u'}u = \ln|u|$ ; $\sqrt x = x^{1/2}$ ; $x\sqrt x = x^{3/2}$ ; $\ln 8 = 3\ln 2$

1. Sans intégration par parties ni changement de variable, calculer $I = \displaystyle\int_1^2 (x-1)\sqrt{x-1}\,dx$.
2. Sans intégration par parties ni changement de variable, calculer $J = \displaystyle\int_0^1 \frac{x^2 + 2}{x^3 + 6x + 1}\,dx$.

## Exercice 2 : cours sur les polynômes (4 points)
Type : degré, division euclidienne de polynômes, racine · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/2
Formules : $\deg(A+B) \leqslant \max(\deg A, \deg B)$ ; $\deg(AB) = \deg A + \deg B$ ; $\exists!\,(Q,R)$, $A = BQ + R$, $\deg R < \deg B$ ; $\alpha$ racine $\iff A(\alpha) = 0 \iff X - \alpha \mid A$

Soient $A$ et $B$ deux polynômes à coefficients réels.
1. Que savez-vous du degré de $A + B$ et de $A \times B$ ?
2. Un étudiant doit énoncer le théorème de la division euclidienne de $A$ par $B$. Il écrit sur sa copie : « $\exists (Q,R) \in (\mathbb{R}[X])^2$ tel que $A = BQ + R$ et $0 \leqslant R < B$ ». Son professeur lui compte faux. Rectifier correctement l'énoncé ci-dessus pour qu'il corresponde effectivement au théorème demandé (et avoir tous les points).
3. Effectuer la division euclidienne de $A = 2X^4 + X - 3$ par $B = X^2 - X + 1$.
4. Soit $\alpha \in \mathbb{R}$. Que signifie que $\alpha$ est une racine de $A$ ? Donner un exemple d'un polynôme $A$ de degré 3 qui admet 42 comme racine.

## Exercice 3 : nombres complexes (3 points)
Type : équation dans $\mathbb{C}$, forme exponentielle · ECUE : HP (nombres complexes, hors programme 2031)
Formules : $AB = 0 \iff A = 0$ ou $B = 0$ ; $\Delta < 0$ : $z = \frac{-b \pm i\sqrt{-\Delta}}{2a}$ ; $z = |z|e^{i\theta}$, $|a + ib| = \sqrt{a^2 + b^2}$, $\cos\theta = \frac{a}{|z|}$, $\sin\theta = \frac{b}{|z|}$

Considérons l'équation $(E)$ $(z + \sqrt3 - i)(z^2 - 2z + 2) = 0$ d'inconnue $z \in \mathbb{C}$.
1. Résoudre $(E)$ dans $\mathbb{C}$.
2. Donner la forme exponentielle de chacune des solutions de $(E)$.

## Exercice 4 : arithmétique (11 points)
Type : inverse modulo un premier, Bézout, Gauss, Fermat · ECUE : HP (arithmétique)
Formules : $p$ premier : $p \wedge a \in \{1, p\}$ ; Bézout : $a \wedge p = 1 \iff \exists (b,v), ab + pv = 1$ ; Gauss ; $ab \equiv 0\,[p] \Rightarrow a \equiv 0$ ou $b \equiv 0\,[p]$ ; $a^2 - 1 = (a-1)(a+1)$ ; Fermat : $p \nmid a \Rightarrow a^{p-1} \equiv 1\,[p]$

Les parties sont indépendantes. Les résultats de la question 1. peuvent être admis et utilisés par la suite.
1. Soient $p$ un nombre premier et $a \in \mathbb{Z}$.
   (a) Montrer que $p \wedge a = 1$ ou $p \mid a$.
   (b) Montrer que $p \wedge a = 1$ si et seulement si $\exists b \in \mathbb{Z}$ tel que $ab \equiv 1\,[p]$.
2. Considérons le nombre premier $p = 47$. On cherche à résoudre l'équation $(E)$ $23x \equiv 1\,[47]$ d'inconnue $x \in [\![1, 46]\!]$.
   (a) Trouver dans $\mathbb{Z}^2$ une solution particulière $(x_0, y_0)$ à l'équation $(E_1)$ $23x + 47y = 1$.
   (b) Résoudre $(E_1)$ dans $\mathbb{Z}^2$.
   (c) En déduire toutes les solutions dans $\mathbb{Z}$ de $(E)$. En déduire les solutions de $(E)$ dans $[\![1, 46]\!]$.
3. Soit $(a,b) \in \mathbb{Z}^2$.
   (a) Montrer que $ab \equiv 0\,[47] \iff a \equiv 0\,[47]$ ou $b \equiv 0\,[47]$.
   (b) En déduire que $a^2 \equiv 1\,[47] \iff a \equiv 1\,[47]$ ou $a \equiv -1\,[47]$.
   (c) Trouver tous les $a \in [\![1, 46]\!]$ tels que $a^2 \equiv 1\,[47]$.
   (d) Soient $a \in [\![1, 46]\!]$ et $k \in \mathbb{N}$. Quel est le reste de la division euclidienne de $a^{46k}$ par 47 ? Justifier.

## Exercice 5 : suites 1 (4,5 points)
Type : comparaison de suites ($\sim$, $o$, $O$) · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/12
Formules : $u_n \sim v_n \iff \frac{u_n}{v_n} \to 1$ ; $u_n = o(v_n) \iff \frac{u_n}{v_n} \to 0$ ; $u_n = O(v_n) \iff \frac{u_n}{v_n}$ bornée ; convergente $\Rightarrow$ bornée, donc $\sim$ et $o$ impliquent $O$ ; croissances comparées : $\frac{\ln n}{n^a} \to 0$, $\frac{n^a}{e^n} \to 0$ ; $\frac{\sin n}{n} \to 0$ ; factoriser par le terme dominant

1. Soient $(u_n)$ et $(v_n)$ deux suites ne s'annulant pas. Rappeler la définition de : $u_n \sim v_n$, $u_n = o(v_n)$ et $u_n = O(v_n)$ en $+\infty$.
2. Comparer en $+\infty$ les suites $(u_n)$ et $(v_n)$ suivantes à l'aide des comparateurs de Landau $\sim$, $= o(\cdot)$, $= O(\cdot)$ en citant toutes les comparaisons possibles et en justifiant vos réponses.
   (a) $u_n = n^2 + 1$ et $v_n = e^n - n$.
   (b) $u_n = n^2 - n + 1$ et $v_n = n^2 - 1$.
3. Soit $(u_n)$ une suite telle que $u_n = \dfrac{-1}{2n} + o\!\left(\dfrac1n\right)$ au voisinage de $+\infty$. Donner un équivalent simple de $(u_n)$ en $+\infty$. Justifier.

## Exercice 6 : suites 2 (5,5 points)
Type : suite récurrente $u_{n+1} = f(u_n)$ · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/10
Formules : constante $\iff u_0 = f(u_0)$ ; tableau de variations via $f'$ ; $f$ croissante sur $I$ et $u_n \in I \Rightarrow f(a) < f(u_n) < f(b)$ (récurrence) ; signe de $u_{n+1} - u_n$ ; monotone bornée $\Rightarrow$ convergente ; $\ell = f(\ell)$

Considérons la fonction $f : x \mapsto \dfrac{x^2 + 6x - 8}{8}$ définie sur $\mathbb{R}$ et la suite $(u_n)$ définie par $u_{n+1} = f(u_n)$, $u_0 \in \mathbb{R}$ donné.
1. Pour quelle(s) valeur(s) de $u_0$ cette suite est-elle constante ?
2. Faire le tableau (complet) des variations de $f$ sur $\mathbb{R}$.
3. Pour la suite de l'exercice, nous prendrons $u_0 \in ]-2, 4[$. Montrer que $\forall n \in \mathbb{N}$, $u_n \in ]-2, 4[$.
4. Étudier la monotonie de $(u_n)$.
5. La suite $(u_n)$ est-elle convergente ? Si oui, donner sa limite.

## Exercice 7 : une démonstration (4 points)
Type : démonstration de cours (convergente implique bornée) · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/13
Formules : $u_n \to \ell$ : $\forall \varepsilon > 0, \exists N, \forall n \geqslant N, |u_n - \ell| < \varepsilon$ ; bornée : $\exists M, \forall n, |u_n| \leqslant M$ ; inégalité triangulaire $|u_n| \leqslant |u_n - \ell| + |\ell|$ ; $M = \max(|u_0|, \dots, |u_{N-1}|, 1 + |\ell|)$ ; contre-exemple $(-1)^n$

Soit $(u_n)$ une suite.
1. Soit $l \in \mathbb{R}$. Rappeler la définition avec les quantificateurs de « $(u_n)$ converge vers $l$ ».
2. Rappeler la définition avec les quantificateurs de « $(u_n)$ est bornée ».
3. Montrer que si $(u_n)$ converge alors $(u_n)$ est bornée.
4. Expliquer pourquoi la réciproque est fausse.

## Exercice 8 : exercice original (5 points)
Type : suites extraites et gendarmes · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/11
Formules : gendarmes : $a_n \leqslant u_n \leqslant b_n$, $a_n, b_n \to \ell \Rightarrow u_n \to \ell$ ; $(u_{2n})$ et $(u_{2n+1})$ même limite $\Rightarrow (u_n)$ converge vers cette limite

Soit $(u_n)$ une suite réelle. On suppose que
$$\forall (p,q) \in (\mathbb{N}^*)^2,\quad 0 \leqslant u_{p+q} \leqslant \frac{p+q}{pq}.$$
En considérant des suites extraites de $(u_n)$, étudier le comportement de $(u_n)$ en $+\infty$ (convergence ou divergence). Justifier avec soin.
