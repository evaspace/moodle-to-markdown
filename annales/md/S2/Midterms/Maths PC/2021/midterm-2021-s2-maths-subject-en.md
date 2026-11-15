# Midterm exam n°2 — February 2017 (subject, EN)

- Source : `raw/S2/Midterms/Maths PC/2021/midterm-2021-s2-maths-subject-en.pdf` (scan, 6 pages)
- Date réelle : février 2017 (Info-Sup 16/17, dossier promo 2021). Version anglaise de `midterm-2021-s2-maths-subject-fr.md` (même sujet). Corrigé : `midterm-2021-s2-maths-correction-en.md`.
- Duration: three hours. Documents and calculators not authorized. 21 points.

## Exercise 1 (4.5 points)
Type : IPP et changement de variable · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/13
Formules : IPP : $\int_a^b uv' = [uv]_a^b - \int_a^b u'v$ ($u = \ln$, $v' = 1$) ; changement de variable : $x = \varphi(t)$, $dx = \varphi'(t)\,dt$, bornes transformées ; $t = \sqrt{1-x} \Rightarrow x = 1 - t^2$, $dx = -2t\,dt$ ; $t = e^{-x} \Rightarrow dx = -\frac{dt}t$ ; $\int \frac{dt}{1+t} = \ln(1+t)$ ; $\int t^n = \frac{t^{n+1}}{n+1}$

1. Using a double integration by parts, compute $I = \displaystyle\int_1^e \sin(\ln(x))\,dx$.
2. Using an integration by parts, compute $J = \displaystyle\int_0^1 \arctan(x)\,dx$.
3. Using the substitution $u = \sqrt x$ and then an integration by parts, compute $K = \displaystyle\int_0^{\pi^2} \cos(\sqrt x)\,dx$.

## Exercise 2 (3 points)
Type : comparaison et limites · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/6
Formules : $u_n \leqslant v_n$ et $v_n \to -\infty \Rightarrow u_n \to -\infty$ ; $u_n \leqslant v_n$ et $u_n \to +\infty \Rightarrow v_n \to +\infty$ ; pour une limite finie, il faut deux gendarmes

Let $(u_n)$ and $(v_n)$ be two sequences of strictly positive real numbers such that for every $n \in \mathbb{N}$, $\dfrac{u_{n+1}}{u_n} \leqslant \dfrac{v_{n+1}}{v_n}$.
1. Show that if $v_n \to 0$ then $u_n \to 0$.
2. Show that if $u_n \to +\infty$ then $v_n \to +\infty$.

## Exercise 3 (3 points)
Type : propriétés de suites et suites extraites (vrac) · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/11
Formules : $q^n$ ($q > 1$) croissante non bornée ; $(-1)^n$ bornée divergente ; suite extraite d'une convergente converge vers la même limite ; $(u_{2n})$ et $(u_{2n+1})$ même limite $\Rightarrow (u_n)$ converge ; $(u_{3n})$, $(u_{3n+1})$ ne couvrent pas $(u_{3n+2})$

Circle the true statements (wrong answers do not remove points).
- a. Let $(u_n)$ be a sequence of real numbers and $\ell \in \mathbb{R}$. The assertion « if $(u_n)$ converges towards $\ell$ then, for every $n \in \mathbb{N}$, $u_n \leqslant \ell$ » is equivalent to « if there exists $n \in \mathbb{N}$ such that $u_n > \ell$, then $(u_n)$ does not converge towards $\ell$ ».
- b. If $(u_n)$ is a nonzero geometric sequence with common ratio $q \in \mathbb{R}^*$, then $\left(\frac1{u_n}\right)$ is a geometric sequence with common ratio $\frac1q$.
- c. If $(u_n)$ is a bounded numerical sequence, there exists a subsequence of $(u_n)$ that is convergent.
- d. $(u_{6n})$ is a subsequence of $(u_{2n})$.
- e. $(u_{3 \cdot 2^{n+1}})$ is a subsequence of $(u_{6n})$.
- f. None of the above.

## Exercise 4 (3 points)
Type : suites adjacentes · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/9
Formules : adjacentes : $(u_n)$ croissante, $(v_n)$ décroissante, $v_n - u_n \to 0$ ; alors elles convergent vers la même limite ; $\frac1{(n+1)!} = \frac1{n!} \cdot \frac1{n+1}$

Let $(u_n)$ and $(v_n)$ be defined for every $n \in \mathbb{N}$ by $u_n = \displaystyle\sum_{k=0}^{2n+1} \frac{(-1)^k}{(2k)!}$ and $v_n = u_n + \dfrac1{(4n+4)!}$. Show that $(u_n)$ and $(v_n)$ are adjacent sequences.

## Exercise 5 (2 points)
Type : comparaison et limites · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/6
Formules : $u_n \leqslant v_n$ et $v_n \to -\infty \Rightarrow u_n \to -\infty$ ; $u_n \leqslant v_n$ et $u_n \to +\infty \Rightarrow v_n \to +\infty$ ; pour une limite finie, il faut deux gendarmes

Let $(u_n)_{n \in \mathbb{N}^*}$ be defined by $u_n = \dfrac{\ln(n!)}{n^2}$.
1. Let $n \in \mathbb{N}^*$. Show (without induction) that $\ln(n!) \leqslant n\ln(n)$.
2. Deduce the limit of $(u_n)$.

## Exercise 6 (5.5 points)
Type : suites adjacentes ($\sum 1/k!$) · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/8
Formules : adjacentes : $(u_n)$ croissante, $(v_n)$ décroissante, $v_n - u_n \to 0$ ; $u_{n+1} - u_n = \frac1{(n+1)!}$ ; $\frac1{n!} = \frac{n+1}{(n+1)!}$ ; adjacentes $\Rightarrow$ convergentes ; convergente $\Rightarrow$ bornée

Let $(u_n)$ be defined for every $n \in \mathbb{N}$ by $u_n = \displaystyle\sum_{k=0}^n \frac1{k!}$.
1. Let $n \in \mathbb{N}^*$ and $q \in \mathbb{R} \setminus \{1\}$. What is $\sum_{k=1}^n q^{k-1}$?
2. Using the previous question, show (without induction) that $\sum_{k=1}^n \frac1{2^{k-1}} = 2 - \frac1{2^{n-1}}$.
3. Let $k \geqslant 2$. Show (without induction) that $\frac1{k!} = \frac1{2 \times 3 \times \dots \times k} \leqslant \frac1{2^{k-1}}$. Check that the inequality still holds for $k = 1$.
4. Show that $(u_n)$ is increasing.
5. Show (without induction), using questions 2 and 3, that for every $n$, $u_n \leqslant 3$.
6. Is $(u_n)$ convergent? Justify your answer.
