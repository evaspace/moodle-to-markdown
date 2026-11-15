# Midterm exam n°2 — February 2017 (correction, EN)

- Source : `raw/S2/Midterms/Maths PC/2021/midterm-2021-s2-maths-correction-en.pdf` (3 pages)
- Date réelle : février 2017 (Info-Sup 16/17, dossier promo 2021). Sujet : `midterm-2021-s2-maths-subject-fr.md`.
- Corrigé officiel, rédigé ici en français.

## Exercice 1 (4,5 points)
Type : IPP et changement de variable · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/13
Formules : IPP : $\int_a^b uv' = [uv]_a^b - \int_a^b u'v$ ($u = \ln$, $v' = 1$) ; changement de variable : $x = \varphi(t)$, $dx = \varphi'(t)\,dt$, bornes transformées ; $t = \sqrt{1-x} \Rightarrow x = 1 - t^2$, $dx = -2t\,dt$ ; $t = e^{-x} \Rightarrow dx = -\frac{dt}t$ ; $\int \frac{dt}{1+t} = \ln(1+t)$ ; $\int t^n = \frac{t^{n+1}}{n+1}$

1. IPP avec $u(x) = \sin(\ln x)$, $v'(x) = 1$ : $I = \big[x\sin(\ln x)\big]_1^e - \displaystyle\int_1^e \cos(\ln x)\,dx = e\sin(1) - \int_1^e \cos(\ln x)\,dx$.
   Seconde IPP avec $u(x) = \cos(\ln x)$, $v'(x) = 1$ : $I = e\sin(1) - \big[x\cos(\ln x)\big]_1^e - I$, donc $2I = 1 + e\sin(1) - e\cos(1)$ et $I = \dfrac{1 + e(\sin 1 - \cos 1)}2$.
   (Le corrigé officiel écrit $\cos(1)$ au lieu de $e\cos(1)$ : coquille, $\big[x\cos(\ln x)\big]_1^e = e\cos 1 - 1$.)
2. IPP avec $u(x) = \arctan x$, $v'(x) = 1$ : $J = \big[x\arctan x\big]_0^1 - \displaystyle\int_0^1 \frac{x}{1+x^2}\,dx = \frac\pi4 - \frac12\big[\ln(1+x^2)\big]_0^1 = \frac\pi4 - \frac{\ln 2}2$.
3. $u = \sqrt x$, $x = u^2$, $dx = 2u\,du$ : $K = 2\displaystyle\int_0^\pi u\cos u\,du$. IPP avec $\varphi(u) = u$, $\psi'(u) = \cos u$ : $K = 2\Big(\big[u\sin u\big]_0^\pi - \int_0^\pi \sin u\,du\Big) = -2\int_0^\pi \sin u\,du = -4$.

## Exercice 2 (3 points)
Type : comparaison et limites · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/6
Formules : $u_n \leqslant v_n$ et $v_n \to -\infty \Rightarrow u_n \to -\infty$ ; $u_n \leqslant v_n$ et $u_n \to +\infty \Rightarrow v_n \to +\infty$ ; pour une limite finie, il faut deux gendarmes

1. Pour $k = 1, \dots, n$ : $\dfrac{u_k}{u_{k-1}} \leqslant \dfrac{v_k}{v_{k-1}}$. En multipliant ces inégalités entre nombres positifs (produit télescopique) : $\dfrac{u_n}{u_0} \leqslant \dfrac{v_n}{v_0}$, soit $0 < u_n \leqslant \dfrac{u_0}{v_0}v_n$. Par le théorème des gendarmes, si $v_n \to 0$ alors $u_n \to 0$.
2. De même $v_n \geqslant \dfrac{v_0}{u_0}u_n$ ; par comparaison, si $u_n \to +\infty$ alors $v_n \to +\infty$.

## Exercice 3 (3 points)
Type : propriétés de suites et suites extraites (vrac) · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/11
Formules : $q^n$ ($q > 1$) croissante non bornée ; $(-1)^n$ bornée divergente ; suite extraite d'une convergente converge vers la même limite ; $(u_{2n})$ et $(u_{2n+1})$ même limite $\Rightarrow (u_n)$ converge ; $(u_{3n})$, $(u_{3n+1})$ ne couvrent pas $(u_{3n+2})$

Énoncés vrais : 1, 2, 3, 4 et 5.
1. Vrai : une implication équivaut à sa contraposée.
2. Vrai : $\dfrac1{u_{n+1}} = \dfrac1q \cdot \dfrac1{u_n}$.
3. Vrai : théorème de Bolzano-Weierstrass.
4. Vrai : $6n = 2 \times (3n)$ et $n \mapsto 3n$ est strictement croissante.
5. Vrai : $3 \cdot 2^{n+1} = 6 \times 2^n$ et $n \mapsto 2^n$ est strictement croissante.

## Exercice 4 (3 points)
Type : suites adjacentes · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/9
Formules : adjacentes : $(u_n)$ croissante, $(v_n)$ décroissante, $v_n - u_n \to 0$ ; alors elles convergent vers la même limite ; $\frac1{(n+1)!} = \frac1{n!} \cdot \frac1{n+1}$

$u_{n+1} - u_n = \dfrac{(-1)^{2n+2}}{(2(2n+2))!} + \dfrac{(-1)^{2n+3}}{(2(2n+3))!} = \dfrac1{(4n+4)!} - \dfrac1{(4n+6)!} > 0$ car $(4n+6)! > (4n+4)!$ : $(u_n)$ est strictement croissante.

$v_{n+1} - v_n = u_{n+1} - u_n + \dfrac1{(4n+8)!} - \dfrac1{(4n+4)!} = \dfrac1{(4n+8)!} - \dfrac1{(4n+6)!} < 0$ : $(v_n)$ est strictement décroissante.

Enfin $v_n - u_n = \dfrac1{(4n+4)!} \to 0$ : les suites sont adjacentes.

## Exercice 5 (2 points)
Type : comparaison et limites · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/6
Formules : $u_n \leqslant v_n$ et $v_n \to -\infty \Rightarrow u_n \to -\infty$ ; $u_n \leqslant v_n$ et $u_n \to +\infty \Rightarrow v_n \to +\infty$ ; pour une limite finie, il faut deux gendarmes

1. $\ln(n!) = \displaystyle\sum_{k=1}^n \ln k \leqslant n\ln n$ car $\ln$ est croissante ($\ln k \leqslant \ln n$).
2. Donc $0 \leqslant u_n \leqslant \dfrac{\ln n}n$. Par croissances comparées et gendarmes, $u_n \to 0$.

## Exercice 6 (5,5 points)
Type : suites adjacentes ($\sum 1/k!$) · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/8
Formules : adjacentes : $(u_n)$ croissante, $(v_n)$ décroissante, $v_n - u_n \to 0$ ; $u_{n+1} - u_n = \frac1{(n+1)!}$ ; $\frac1{n!} = \frac{n+1}{(n+1)!}$ ; adjacentes $\Rightarrow$ convergentes ; convergente $\Rightarrow$ bornée

1. $q \neq 1$ : $\displaystyle\sum_{k=1}^n q^{k-1} = \frac{1 - q^n}{1 - q}$.
2. Avec $q = \frac12$ : $\displaystyle\sum_{k=1}^n \frac1{2^{k-1}} = \frac{1 - \frac1{2^n}}{1 - \frac12} = 2\Big(1 - \frac1{2^n}\Big) = 2 - \frac1{2^{n-1}}$.
3. Pour $k \geqslant 2$ : chaque facteur $2, 3, \dots, k$ est $\geqslant 2$, donc $\frac12 \leqslant \frac12$, $\frac13 \leqslant \frac12$, …, $\frac1k \leqslant \frac12$ ; en multipliant ces $k-1$ inégalités, $\dfrac1{k!} \leqslant \dfrac1{2^{k-1}}$. Pour $k = 1$ : $\frac1{1!} = 1 \leqslant \frac1{2^0} = 1$.
4. $u_{n+1} - u_n = \dfrac1{(n+1)!} \geqslant 0$ : $(u_n)$ est croissante.
5. $u_n = 1 + \displaystyle\sum_{k=1}^n \frac1{k!} \leqslant 1 + \sum_{k=1}^n \frac1{2^{k-1}} = 1 + 2 - \frac1{2^{n-1}} \leqslant 3$.
6. $(u_n)$ est croissante et majorée, donc convergente.
