# Contrôle de cours 1, mathématiques S1PA — lundi 9 octobre 2023 (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (pas de corrigé officiel). Sujet : `td2-2028-s1-maths_PA-subject-fr.md` (même dossier). Calculs vérifiés avec sympy. 

## Cours 1 : définitions et théorèmes à énoncer (5 points)
Type : énoncés de cours sur les suites (récurrence, gendarmes, majorée) · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/13
Formules : récurrence : $P(n_0)$ et $\forall n \geqslant n_0, P(n) \Rightarrow P(n+1)$ donnent $\forall n \geqslant n_0, P(n)$ ; gendarmes $v_n \leqslant u_n \leqslant w_n$, $v_n, w_n \to \ell \Rightarrow u_n \to \ell$ ; majorée : $\exists M, \forall n, u_n \leqslant M$

1. Si $P(n_0)$ est vraie et si $\forall n\ge n_0,\ P(n)\Rightarrow P(n+1)$, alors $P(n)$ est vraie pour tout $n\ge n_0$.
2. Si $u_n\le v_n\le w_n$ à partir d'un certain rang et si $u_n\to\ell$ et $w_n\to\ell$ (même limite finie $\ell$), alors $v_n\to\ell$.
3. $(u_n)$ majorée : $\exists M\in\mathbb R,\ \forall n\in\mathbb N,\ u_n\le M$.

## Cours 2 : exemple des suites géométriques (4 points)
Type : suites géométriques (terme général, somme, limite de $q^n$) · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/1
Formules : $u_n = u_0q^n$ ; $\sum_{k=p}^n q^k = q^p\frac{1 - q^{n-p+1}}{1 - q}$ ; $\sum_{k=2}^8 \frac1{2^k} = \frac14 \cdot \frac{1 - (1/2)^7}{1/2}$ ; $q^n \to +\infty$ ($q > 1$), $1$ ($q = 1$), $0$ ($|q| < 1$), pas de limite ($q \leqslant -1$)

1. $u_n=u_0q^n$.
2. (a) $\displaystyle\sum_{k=p}^nq^k=\dfrac{q^p-q^{n+1}}{1-q}$. (b) $S=\dfrac{\left(\frac12\right)^2-\left(\frac12\right)^9}{1-\frac12}=2\left(\dfrac14-\dfrac1{512}\right)=\dfrac12-\dfrac1{256}=\dfrac{127}{256}$.
3. $q^n\to0$ si $|q|<1$ ; $1$ si $q=1$ ; $+\infty$ si $q>1$ ; pas de limite si $q\le-1$.

## Cours 3 : limites de suites (6 points)
Type : opérations sur les limites, formes indéterminées · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/5
Formules : $\frac{\ell}{\ell'}$ ; $\frac{\ell > 0}{0^+} = +\infty$ ; $\frac{\pm\infty}{\ell'}$ selon le signe ; $\frac\infty\infty$ indéterminée ; $\frac{+\infty}{0^+} = +\infty$ ; $\frac{0^-}{0^+}$ indéterminée ; factoriser par le terme dominant

1. | $\lim u_n$ | $\ell$ | $\ell>0$ | $-\infty$ | $+\infty$ | $+\infty$ | $\ell<0$ | $0^-$ |
   |---|---|---|---|---|---|---|---|
   | $\lim v_n$ | $\ell'\ne0$ | $0^+$ | $\ell'<0$ | $-\infty$ | $0^+$ | $0^-$ | $0^+$ |
   | $\lim\frac{u_n}{v_n}$ | $\frac\ell{\ell'}$ | $+\infty$ | $+\infty$ | forme indéterminée | $+\infty$ | $+\infty$ | forme indéterminée |
2. (a) Numérateur : $-2n^2+\frac1{\sqrt n}\to-\infty$. Dénominateur : $e^{-n}-3\to-3$. Donc $u_n\to+\infty$.
   (b) $u_n=\dfrac{n^3\left(6-\frac2n+\frac3{n^3}\right)}{n^2\left(1+\frac1{n^2}\right)}=n\cdot\dfrac{6-\frac2n+\frac3{n^3}}{1+\frac1{n^2}}\to+\infty$.

## Cours 4 : comparaisons (3 points)
Type : comparaison et limites · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/6
Formules : $u_n \leqslant v_n$ et $v_n \to -\infty \Rightarrow u_n \to -\infty$ ; $u_n \leqslant v_n$ et $u_n \to +\infty \Rightarrow v_n \to +\infty$ ; pour une limite finie, il faut deux gendarmes

1. $0\le u_n\le\dfrac1{\sqrt{n+1}}\to0$ : par le théorème des gendarmes, $u_n\to0$ : convergente.
2. $e^n-2n^2=e^n\left(1-2n^2e^{-n}\right)$ avec $n^2e^{-n}\to0$ (croissances comparées) : la limite est $+\infty$.
3. Oui : $v_n\ge e^n-2n^2\to+\infty$ donc $v_n\to+\infty$ (théorème de minoration).

## Cours 5 : convergence ou divergence (2 points)
Type : théorème de la limite monotone · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/8
Formules : croissante majorée $\Rightarrow$ convergente ; décroissante minorée $\Rightarrow$ convergente ; croissante non majorée $\Rightarrow +\infty$

1. Vrai : théorème de la limite monotone : toute suite décroissante et minorée converge.
2. Faux : $u_n=(-1)^n$ est bornée et diverge.
