# Contrôle 2 (S2) — mars 2018 (corrigé, FR)

- Source : `raw/S2/Midterms/Maths PC/2022/midterm-2022-s2-maths-correction-fr.pdf` (scan, 3 pages)
- Date réelle : mars 2018 (Info-Sup 17/18, dossier promo 2022). Sujet : `midterm-2022-s2-maths-subject-fr.md`.
- Corrigé officiel.

## Exercice 1 (4,5 points)
Type : IPP et changement de variable · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/13
Formules : IPP : $\int_a^b uv' = [uv]_a^b - \int_a^b u'v$ ($u = \ln$, $v' = 1$) ; changement de variable : $x = \varphi(t)$, $dx = \varphi'(t)\,dt$, bornes transformées ; $t = \sqrt{1-x} \Rightarrow x = 1 - t^2$, $dx = -2t\,dt$ ; $t = e^{-x} \Rightarrow dx = -\frac{dt}t$ ; $\int \frac{dt}{1+t} = \ln(1+t)$ ; $\int t^n = \frac{t^{n+1}}{n+1}$

1. $u(x) = \ln(x + \sqrt{x^2+1})$, $v'(x) = 1$, $v(x) = x$ et $u'(x) = \dfrac1{x + \sqrt{x^2+1}} \times \Big(1 + \dfrac{x}{\sqrt{x^2+1}}\Big) = \dfrac1{\sqrt{x^2+1}}$.
   Donc $I = \big[x\ln(x + \sqrt{x^2+1})\big]_0^1 - \displaystyle\int_0^1 \frac{x}{\sqrt{x^2+1}}\,dx = \ln(1 + \sqrt2) - \big[\sqrt{x^2+1}\big]_0^1 = 1 - \sqrt2 + \ln(1 + \sqrt2)$.
2. $u = \sqrt t$, $t = u^2$, $dt = 2u\,du$ : $J = \displaystyle\int_1^{\sqrt3} \frac{2u}{u + u^3}\,du = 2\int_1^{\sqrt3} \frac{du}{1 + u^2} = 2\big[\arctan u\big]_1^{\sqrt3} = 2\Big(\frac\pi3 - \frac\pi4\Big) = \frac\pi6$.
3. $u = \ln t$, $du = \dfrac{dt}t$ : $K = \displaystyle\int_0^1 \frac{u}{1 + u^2}\,du = \frac12\big[\ln(1 + u^2)\big]_0^1 = \frac12\ln 2$.

## Exercice 2 (2 points)
Type : somme de suites convergentes ou divergentes · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/13
Formules : somme de deux suites convergentes : convergente, $\lim(u_n + v_n) = \lim u_n + \lim v_n$ ; convergente + divergente = divergente (par l'absurde, $v_n = w_n - u_n$) ; divergente + divergente : on ne peut rien dire (contre-exemples $n$ et $1 - n$)

1. $(w_n) = (u_n + v_n)$ est divergente. Par l'absurde : si $(w_n)$ convergeait, $(v_n) = (w_n - u_n)$ convergerait (différence de deux suites convergentes), ce qui contredit l'hypothèse.
2. On ne peut rien conclure. $(u_n) = (n)$ et $(v_n) = (1 - n)$ divergent et $(u_n + v_n) = (1)$ converge. $(u_n) = (n)$ et $(v_n) = (e^n)$ divergent et $(u_n + v_n) = (n + e^n)$ diverge.

## Exercice 3 (3,5 points)
Type : monotonie par quotient, majoration d'un produit, gendarmes · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/8
Formules : $u_n > 0$ : $\frac{u_{n+1}}{u_n} \leqslant 1 \Rightarrow (u_n)$ décroissante ; $(n+1)! = (n+1)\,n!$ ; décroissante minorée $\Rightarrow$ convergente ; $\frac{n!}{n^n} = \prod_{k=1}^n \frac kn$, facteurs $\leqslant 1$ ; gendarmes

1. $\dfrac{u_{n+1}}{u_n} = \dfrac{(n+1)!}{(n+1)^{n+1}} \times \dfrac{n^n}{n!} = \Big(\dfrac{n}{n+1}\Big)^n$ : $a = b = 1$.
2. Pour tout $n \in \mathbb{N}^*$, $\dfrac{u_{n+1}}{u_n} = \Big(\dfrac{n}{n+1}\Big)^n \leqslant 1$ et $u_n > 0$, donc $(u_n)$ est décroissante. Elle est de plus minorée par 0, donc convergente.
3. $u_n = \dfrac nn \times \dfrac{n-1}n \times \dfrac{n-2}n \times \dots \times \dfrac2n \times \dfrac1n$. Les $n - 1$ premiers facteurs sont positifs et $\leqslant 1$, donc $u_n \leqslant \dfrac1n$.
4. $0 \leqslant u_n \leqslant \dfrac1n \to 0$ : par gendarmes, $(u_n)$ converge vers 0.

## Exercice 4 (2 points)
Type : encadrement d'une somme, gendarmes · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/6
Formules : somme de $n$ termes : $n \times (\text{plus petit}) \leqslant \sum \leqslant n \times (\text{plus grand})$ ; gendarmes : $a_n \leqslant u_n \leqslant b_n$, $a_n, b_n \to \ell \Rightarrow u_n \to \ell$ ; $\frac{n^2}{n^2 + n} \to 1$

1. $u_n = \dfrac1{n^2+1} + \dfrac1{n^2+2} + \dots + \dfrac1{n^2+n}$ : somme de $n$ termes dont le plus grand est $\dfrac1{n^2+1}$. Ainsi $0 \leqslant u_n \leqslant \dfrac n{n^2+1} \to 0$ : par gendarmes, $(u_n)$ converge vers 0.
2. $nu_n$ est la somme de $n$ termes dont le plus grand est $\dfrac n{n^2+1}$ et le plus petit $\dfrac n{n^2+n}$. Ainsi $\dfrac{n^2}{n^2+n} \leqslant nu_n \leqslant \dfrac{n^2}{n^2+1}$. Les deux bornes tendent vers 1 : par gendarmes, $(nu_n)$ converge vers 1.

## Exercice 5 (3 points)
Type : développements limités, limite par équivalents · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/9
Formules : en 0 : $e^x = 1 + x + \frac{x^2}2 + \frac{x^3}6 + o(x^3)$ ; $\ln(1+x) = x - \frac{x^2}2 + o(x^2)$ ; $\cos x = 1 - \frac{x^2}2 + o(x^3)$ ; $\sin x = x - \frac{x^3}6 + o(x^3)$ ; $\frac1{1-x} = 1 + x + x^2 + x^3 + o(x^3)$ ; produit de DL tronqué à l'ordre ; $a^b = e^{b\ln a}$ ; $f \sim g \Rightarrow$ même limite

1. $n^2\left(\sqrt{1 + \ln\big(1 + \frac1{n^2}\big)} - 1\right) = n^2\left(\Big(1 + \frac1{n^2} + o\big(\frac1{n^2}\big)\Big)^{1/2} - 1\right) = n^2\left(1 + \frac1{2n^2} + o\big(\frac1{n^2}\big) - 1\right) = \frac12 + o(1)$. La limite vaut $\dfrac12$.
2. $\Big(\ln\big(e + \frac1n\big)\Big)^n = e^{n\ln(\ln(e + \frac1n))}$ et $\ln\big(e + \frac1n\big) = \ln(e) + \ln\big(1 + \frac1{en}\big) = 1 + \frac1{en} + o\big(\frac1n\big)$. Donc $n\ln\big(1 + \frac1{en} + o(\frac1n)\big) = n\big(\frac1{en} + o(\frac1n)\big) = \frac1e + o(1)$. La limite vaut $e^{1/e}$.

## Exercice 6 (3 points)
Type : suites adjacentes · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/9
Formules : adjacentes : $(u_n)$ croissante, $(v_n)$ décroissante, $v_n - u_n \to 0$ ; alors elles convergent vers la même limite ; $\frac1{(n+1)!} = \frac1{n!} \cdot \frac1{n+1}$

Soit $n \geqslant 1$. $u_{n+1} - u_n = \dfrac1{(n+1)^2} \geqslant 0$ : $(u_n)$ est croissante.

$v_{n+1} - v_n = u_{n+1} - u_n + \dfrac1{n+1} - \dfrac1n = \dfrac{n + n(n+1) - (n+1)^2}{n(n+1)^2} = -\dfrac1{n(n+1)^2} \leqslant 0$ : $(v_n)$ est décroissante.

$v_n - u_n = \dfrac1n \to 0$. Ainsi $(u_n)$ et $(v_n)$ sont adjacentes.

## Exercice 7 (3 points)
Type : reconnaître un sous-espace vectoriel · ECUE : EV · Niveau : maths-s2-ev/3
Formules : sev : contient 0, stable par addition et multiplication par un scalaire ; contre-exemple $\lambda u \notin E$ ; équation non linéaire ($z^2$) $\Rightarrow$ en général pas un sev ; $\mathrm{Vect}(\dots)$ est toujours un sev

1. $E$ est un $\mathbb{R}$-ev : c'est un sev de $\mathbb{R}[X]$. $E \subset \mathbb{R}[X]$, $E \neq \emptyset$ (le polynôme nul est dans $E$). Si $(P, Q) \in E^2$ et $\lambda \in \mathbb{R}$ : $(\lambda P + Q)(1) = \lambda P(1) + Q(1) = \lambda P'(2) + Q'(2) = (\lambda P + Q)'(2)$, donc $\lambda P + Q \in E$.
2. $F$ est un $\mathbb{R}$-ev : c'est un sev de $\mathbb{R}^2$. $F \subset \mathbb{R}^2$, $(0,0) \in F$. Si $u = (x,y)$, $v = (x',y')$ dans $F$ et $\lambda \in \mathbb{R}$ : $\sqrt\pi(\lambda x + x') - \ln(3)(\lambda y + y') = \lambda(\sqrt\pi x - \ln(3)y) + \sqrt\pi x' - \ln(3)y' = 0$, donc $\lambda u + v \in F$.
3. $G$ n'est pas un $\mathbb{R}$-ev : $(u_n) = ((-1)^n) \in G$, $(v_n) = (1 - (-1)^n) \in G$, mais $(u_n) + (v_n)$ est la suite constante égale à 1, qui n'est pas dans $G$ (et la suite nulle n'est pas dans $G$).
