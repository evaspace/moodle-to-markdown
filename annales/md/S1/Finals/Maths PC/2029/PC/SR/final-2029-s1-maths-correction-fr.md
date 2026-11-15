# Examen S1B2-SR (suites réelles) — janvier 2025 (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (pas de corrigé officiel). Sujet : `final-2029-s1-maths-subject-fr.md` (même dossier). Calculs vérifiés avec sympy. 

## Exercice 1 : suites adjacentes (7 points)
Type : suites adjacentes via une suite géométrique · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/9
Formules : $w_{n+1} = qw_n \Rightarrow w_n = w_0q^n$ ; $|q| < 1 \Rightarrow q^n \to 0$ ; adjacentes : une croissante, l'autre décroissante, différence $\to 0$

1. (a) $w_{n+1}=v_{n+1}-u_{n+1}=\dfrac{(2u_n+3v_n)-(3u_n+2v_n)}5=\dfrac{v_n-u_n}5=\dfrac{w_n}5$ : géométrique de raison $\dfrac15$.
   (b) $w_0=3-2=1$ donc $w_n=\left(\dfrac15\right)^n$.
   (c) $w_n>0$ pour tout $n$.
2. $u_{n+1}-u_n=\dfrac{2(v_n-u_n)}5=\dfrac{2w_n}5>0$ : $(u_n)$ croissante. $v_{n+1}-v_n=\dfrac{2(u_n-v_n)}5=-\dfrac{2w_n}5<0$ : $(v_n)$ décroissante. $v_n-u_n=w_n\to0$ car $\left|\dfrac15\right|<1$. Les suites sont adjacentes.
3. Deux suites adjacentes convergent vers la même limite $\ell$, et $u_n\le\ell\le v_n$.
4. (a) $x_{n+1}=u_{n+1}+v_{n+1}=\dfrac{5u_n+5v_n}5=x_n$ : $(x_n)$ est constante, $x_n=x_0=5$.
   (b) $u_n\to\ell$ et $v_n\to\ell$ donc $2\ell=5$ : les deux limites valent $\dfrac52$.

## Exercice 2 : étude d'une suite (5 points)
Type : monotonie et encadrement d'une somme · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/8
Formules : $u_{n+1} - u_n$ : écrire les deux sommes et simplifier les termes communs ($\frac1{2n} + \frac1{2n+1} - \frac1n$) ; $n \leqslant k \leqslant 2n-1 \Rightarrow \frac1{2n-1} \leqslant \frac1k \leqslant \frac1n$ ; somme de $n$ termes ; monotone bornée $\Rightarrow$ convergente ; passage à la limite dans les inégalités larges

1. $u_{n+1}=\displaystyle\sum_{k=n+1}^{2n+1}\frac1k$ donc $u_{n+1}-u_n=\dfrac1{2n}+\dfrac1{2n+1}-\dfrac1n=\dfrac1{2n+1}-\dfrac1{2n}=-\dfrac1{2n(2n+1)}<0$. La suite est strictement décroissante.
2. Pour $n\le k\le2n-1$ : $\dfrac1{2n-1}\le\dfrac1k\le\dfrac1n$. La somme a $n$ termes : $\dfrac n{2n-1}\le u_n\le n\cdot\dfrac1n=1$.
3. $\dfrac n{2n-1}>\dfrac12$ (car $2n>2n-1$) : minorant $\dfrac12$, majorant $1$.
4. Décroissante et minorée : $(u_n)$ converge vers $\ell$. Par passage à la limite dans les inégalités larges ($\dfrac n{2n-1}\to\dfrac12$) : $\dfrac12\le\ell\le1$.

## Exercice 3 : comparaison de suites (7,5 points)
Type : comparaison de suites ($\sim$, $o$, $O$) · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/12
Formules : $u_n \sim v_n \iff \frac{u_n}{v_n} \to 1$ ; $u_n = o(v_n) \iff \frac{u_n}{v_n} \to 0$ ; $u_n = O(v_n) \iff \frac{u_n}{v_n}$ bornée ; convergente $\Rightarrow$ bornée, donc $\sim$ et $o$ impliquent $O$ ; croissances comparées : $\frac{\ln n}{n^a} \to 0$, $\frac{n^a}{e^n} \to 0$ ; $\frac{\sin n}{n} \to 0$ ; factoriser par le terme dominant

1. $u_n=o(v_n)\iff\dfrac{u_n}{v_n}\to0$ ; $u_n=O(v_n)\iff\dfrac{u_n}{v_n}$ est bornée ; $u_n\sim v_n\iff\dfrac{u_n}{v_n}\to1$.
2. (a) $u_n\sim-n^3$, $v_n\sim-2n^2$, $\dfrac{u_n}{v_n}\sim\dfrac n2\to+\infty$. Donc $v_n=o(u_n)$, et $v_n=O(u_n)$. Pas de $u_n=O(v_n)$, pas d'équivalence.
   (b) $u_n\sim e^n$ car $\dfrac{\sqrt n}{e^n}\to0$ ; $v_n\sim e^n$. Donc $u_n\sim v_n$, et par suite $u_n=O(v_n)$ et $v_n=O(u_n)$. Pas de $o$.
   (c) $u_n\sim3^n$, $v_n\sim5^n$, $\dfrac{u_n}{v_n}\sim\left(\dfrac35\right)^n\to0$. Donc $u_n=o(v_n)$ et $u_n=O(v_n)$.

## Exercice 4 : cours (3 points)
Type : démonstration de cours (convergente implique bornée) · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/13
Formules : $u_n \to \ell$ : $\forall \varepsilon > 0, \exists N, \forall n \geqslant N, |u_n - \ell| < \varepsilon$ ; bornée : $\exists M, \forall n, |u_n| \leqslant M$ ; inégalité triangulaire $|u_n| \leqslant |u_n - \ell| + |\ell|$ ; $M = \max(|u_0|, \dots, |u_{N-1}|, 1 + |\ell|)$ ; contre-exemple $(-1)^n$

1. $(u_n)$ bornée $\iff\exists M\in\mathbb R,\ \forall n,\ |u_n|\le M$.
2. Soit $\ell=\lim u_n$. Avec $\varepsilon=1$ : $\exists N,\ \forall n\ge N,\ |u_n-\ell|<1$ donc $|u_n|\le|u_n-\ell|+|\ell|<1+|\ell|$. Alors $M=\max(|u_0|,\dots,|u_{N-1}|,1+|\ell|)$ majore $|u_n|$ pour tout $n$.
3. Faux : $\big((-1)^n\big)$ est bornée (par $1$) mais ne converge pas.
4. Contraposée : $(u_n)$ non bornée $\Rightarrow(u_n)$ diverge.

## Exercice 5 : suite récurrente (4,5 points)
Type : suite récurrente $u_{n+1} = f(u_n)$ · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/10
Formules : constante $\iff u_0 = f(u_0)$ ; tableau de variations via $f'$ ; $f$ croissante sur $I$ et $u_n \in I \Rightarrow f(a) < f(u_n) < f(b)$ (récurrence) ; signe de $u_{n+1} - u_n$ ; monotone bornée $\Rightarrow$ convergente ; $\ell = f(\ell)$

1. $u_{n+1}-u_n=1+\dfrac{u_n^2}4-u_n=\dfrac{(u_n-2)^2}4\ge0$ : $(u_n)$ est croissante.
2. $f(x)=1+\dfrac{x^2}4$ est croissante sur $\mathbb R_+$. Initialisation : $u_0=\dfrac32\in]1,2[$. Hérédité : si $1<u_n<2$ alors $f(1)<u_{n+1}<f(2)$, soit $\dfrac54<u_{n+1}<2$, donc $1<u_{n+1}<2$.
3. $(u_n)$ est croissante et majorée par $2$ : elle converge vers $\ell$ avec $\ell=1+\dfrac{\ell^2}4$, soit $(\ell-2)^2=0$ : $\ell=2$.

## Exercice 6 : suites extraites (3 points)
Type : suites extraites et divergence · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/11
Formules : $\sin(k\pi) = 0$ ; $\sin\left(2k\pi + \frac\pi3\right) = \frac{\sqrt3}2$ ; si $u_n \to \ell$, toute suite extraite tend vers $\ell$ ; deux suites extraites de limites différentes $\Rightarrow (u_n)$ diverge

1. $u_{3n}=\sin(n\pi)=0$ : suite constante nulle.
2. $u_{6n+1}=\sin\left(2n\pi+\dfrac\pi3\right)=\dfrac{\sqrt3}2$ : suite constante qui converge vers $\dfrac{\sqrt3}2$.
3. Non : si $(u_n)$ convergeait vers $\ell$, toute suite extraite convergerait vers $\ell$. Or $(u_{3n})$ tend vers $0$ et $(u_{6n+1})$ vers $\dfrac{\sqrt3}2\ne0$ : $(u_n)$ diverge.
