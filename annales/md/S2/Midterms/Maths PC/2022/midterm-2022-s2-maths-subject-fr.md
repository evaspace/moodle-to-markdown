# Contrôle 2 (S2) — mars 2018 (sujet, FR)

- Source : `raw/S2/Midterms/Maths PC/2022/midterm-2022-s2-maths-subject-fr.pdf` (scan, 9 pages)
- Date réelle : mars 2018 (Info-Sup 17/18, dossier promo 2022). Corrigé : `midterm-2022-s2-maths-correction-fr.md`.
- Durée : trois heures. Documents et calculatrices non autorisés. Barème : 21 points.

## Exercice 1 (4,5 points)
Type : IPP et changement de variable · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/13
Formules : IPP : $\int_a^b uv' = [uv]_a^b - \int_a^b u'v$ ($u = \ln$, $v' = 1$) ; changement de variable : $x = \varphi(t)$, $dx = \varphi'(t)\,dt$, bornes transformées ; $t = \sqrt{1-x} \Rightarrow x = 1 - t^2$, $dx = -2t\,dt$ ; $t = e^{-x} \Rightarrow dx = -\frac{dt}t$ ; $\int \frac{dt}{1+t} = \ln(1+t)$ ; $\int t^n = \frac{t^{n+1}}{n+1}$

1. Via une intégration par parties, calculer $I = \displaystyle\int_0^1 \ln\big(x + \sqrt{x^2+1}\big)\,dx$.
2. Via le changement de variable $u = \sqrt t$, déterminer $J = \displaystyle\int_1^3 \frac{dt}{\sqrt t + \sqrt{t^3}}$.
3. Via le changement de variable $u = \ln(t)$, déterminer $K = \displaystyle\int_1^e \frac{\ln(t)}{t(1 + \ln^2(t))}\,dt$.

## Exercice 2 (2 points)
Type : somme de suites convergentes ou divergentes · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/13
Formules : somme de deux suites convergentes : convergente, $\lim(u_n + v_n) = \lim u_n + \lim v_n$ ; convergente + divergente = divergente (par l'absurde, $v_n = w_n - u_n$) ; divergente + divergente : on ne peut rien dire (contre-exemples $n$ et $1 - n$)

Soient $(u_n)$ et $(v_n)$ deux suites réelles.
1. On suppose $(u_n)$ convergente et $(v_n)$ divergente. Peut-on conclure quant à la convergence ou la divergence de $(u_n + v_n)$ ? Justifier votre réponse.
2. On suppose $(u_n)$ et $(v_n)$ divergentes. Peut-on conclure quant à la convergence ou la divergence de $(u_n + v_n)$ ? Justifier votre réponse.

## Exercice 3 (3,5 points)
Type : monotonie par quotient, majoration d'un produit, gendarmes · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/8
Formules : $u_n > 0$ : $\frac{u_{n+1}}{u_n} \leqslant 1 \Rightarrow (u_n)$ décroissante ; $(n+1)! = (n+1)\,n!$ ; décroissante minorée $\Rightarrow$ convergente ; $\frac{n!}{n^n} = \prod_{k=1}^n \frac kn$, facteurs $\leqslant 1$ ; gendarmes

Soit $(u_n)$ définie pour tout $n \in \mathbb{N}^*$ par $u_n = \dfrac{n!}{n^n}$.
1. Montrer que $\dfrac{u_{n+1}}{u_n} = \left(\dfrac{an}{bn+1}\right)^n$ où $a$ et $b$ sont deux entiers à déterminer.
2. En déduire la monotonie de $(u_n)$. Peut-on en conclure que $(u_n)$ est convergente ? Justifier votre réponse.
3. Montrer (sans récurrence) que $u_n \leqslant \dfrac1n$.
4. En déduire la limite de $(u_n)$.

## Exercice 4 (2 points)
Type : encadrement d'une somme, gendarmes · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/6
Formules : somme de $n$ termes : $n \times (\text{plus petit}) \leqslant \sum \leqslant n \times (\text{plus grand})$ ; gendarmes : $a_n \leqslant u_n \leqslant b_n$, $a_n, b_n \to \ell \Rightarrow u_n \to \ell$ ; $\frac{n^2}{n^2 + n} \to 1$

On considère la suite $(u_n)$ définie pour tout $n \in \mathbb{N}^*$ par $u_n = \displaystyle\sum_{k=1}^n \frac1{n^2 + k}$.
1. Montrer que $(u_n)$ est convergente en précisant sa limite.
2. Montrer que $(nu_n)$ est convergente en précisant sa limite.

## Exercice 5 (3 points)
Type : développements limités, limite par équivalents · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/9
Formules : en 0 : $e^x = 1 + x + \frac{x^2}2 + \frac{x^3}6 + o(x^3)$ ; $\ln(1+x) = x - \frac{x^2}2 + o(x^2)$ ; $\cos x = 1 - \frac{x^2}2 + o(x^3)$ ; $\sin x = x - \frac{x^3}6 + o(x^3)$ ; $\frac1{1-x} = 1 + x + x^2 + x^3 + o(x^3)$ ; produit de DL tronqué à l'ordre ; $a^b = e^{b\ln a}$ ; $f \sim g \Rightarrow$ même limite

Déterminer les limites suivantes :
1. $\displaystyle\lim_{n \to +\infty} n^2\left(\sqrt{1 + \ln\Big(1 + \frac1{n^2}\Big)} - 1\right)$.
2. $\displaystyle\lim_{n \to +\infty} \left(\ln\Big(e + \frac1n\Big)\right)^n$.

## Exercice 6 (3 points)
Type : suites adjacentes · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/9
Formules : adjacentes : $(u_n)$ croissante, $(v_n)$ décroissante, $v_n - u_n \to 0$ ; alors elles convergent vers la même limite ; $\frac1{(n+1)!} = \frac1{n!} \cdot \frac1{n+1}$

Soient $(u_n)$ et $(v_n)$ définies pour tout $n \in \mathbb{N}^*$ par $u_n = \displaystyle\sum_{k=1}^n \frac1{k^2}$ et $v_n = u_n + \dfrac1n$. Montrer que $(u_n)$ et $(v_n)$ sont adjacentes.

## Exercice 7 (3 points)
Type : reconnaître un sous-espace vectoriel · ECUE : EV · Niveau : maths-s2-ev/3
Formules : sev : contient 0, stable par addition et multiplication par un scalaire ; contre-exemple $\lambda u \notin E$ ; équation non linéaire ($z^2$) $\Rightarrow$ en général pas un sev ; $\mathrm{Vect}(\dots)$ est toujours un sev

Les ensembles suivants sont-ils des $\mathbb{R}$-ev ? Justifiez votre réponse.
1. $E = \{P \in \mathbb{R}[X],\ P(1) = P'(2)\}$.
2. $F = \{(x,y) \in \mathbb{R}^2,\ \sqrt\pi\,x - \ln(3)\,y = 0\}$.
3. $G = \{(u_n) \in \mathbb{R}^{\mathbb{N}},\ (u_n) \text{ n'a pas de limite}\}$.
