# Correction examen S2PA-B4-CCISR — juin 2024

- Source : `raw/S2/Finals/Maths PC/2028/PA/S2PA_2024_B4_COR_CCISR.pdf` (4 pages, corrigé avec énoncés)
- Date réelle : juin 2024 (parcours PA, dossier promo 2028). Pas de sujet séparé. Contenu : intégrales et suites (APIS en 2031).

## Exercice 1 : une intégrale pour démarrer
Type : IPP avec ln · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/8
Formules : IPP : $\int_a^b uv' = [uv]_a^b - \int_a^b u'v$ avec $u = \ln x$, $u' = \frac1x$ ; $\int \frac{dx}{x^2} = -\frac1x$ ; $\ln e = 1$, $\ln 1 = 0$

Via une intégration par parties, calculer $I = \displaystyle\int_1^e \frac{\ln(x)}{x^2}\,dx$. Vous ferez clairement apparaître $u$, $u'$, $v$ et $v'$.
$u(x) = \ln x$, $v'(x) = \frac1{x^2}$, $u'(x) = \frac1x$, $v(x) = -\frac1x$ : $I = \left[-\dfrac{\ln x}x\right]_1^e - \displaystyle\int_1^e -\frac1{x^2}\,dx = -\frac1e - \left[\frac1x\right]_1^e = -e^{-1} - (e^{-1} - 1) = 1 - 2e^{-1}$.

## Exercice 2 : suites en vrac
Type : propriétés de suites et suites extraites (vrac) · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/11
Formules : $q^n$ ($q > 1$) croissante non bornée ; $(-1)^n$ bornée divergente ; suite extraite d'une convergente converge vers la même limite ; $(u_{2n})$ et $(u_{2n+1})$ même limite $\Rightarrow (u_n)$ converge ; $(u_{3n})$, $(u_{3n+1})$ ne couvrent pas $(u_{3n+2})$

Les deux questions sont indépendantes.
1. Avec les bouts de phrases « bornée - non bornée - monotone - non monotone - convergente - divergente », compléter chaque phrase avec 3 bouts différents pour la rendre vraie.
   (a) La suite $(4^n)$ est non bornée, monotone et divergente.
   (b) La suite $((-1)^n)$ est bornée, non monotone et divergente.
   (c) La suite $(n + (-1)^n)$ est non bornée, non monotone et divergente.
2. Avec « convergente vers 0 - 0 - $+\infty$ - divergente - on ne peut rien dire - convergente », compléter :
   (a) Si une suite $(u_n)$ est convergente alors $(u_{3n})$ est convergente.
   (b) Soit $(u_n)$ une suite. Si la limite de $(u_{2n})$ est 0 alors la limite de $(u_n)$ : on ne peut rien dire.
   (c) Si les suites $(u_{3n})$ et $(u_{3n+1})$ convergent vers 0 alors $(u_n)$ : on ne peut rien dire.
   (d) Si les suites $(u_{2n})$ et $(u_{2n+1})$ convergent vers 0 alors $(u_n)$ est convergente vers 0.

## Exercice 3 : suites adjacentes
Type : suites adjacentes via une suite géométrique · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/9
Formules : $w_{n+1} = qw_n \Rightarrow w_n = w_0q^n$ ; $|q| < 1 \Rightarrow q^n \to 0$ ; adjacentes : une croissante, l'autre décroissante, différence $\to 0$

Soient $(u_n)$ et $(v_n)$ définies par $u_0 = 5$, $v_0 = 15$ et $\forall n \in \mathbb{N}$, $u_{n+1} = \dfrac{3u_n + v_n}4$ et $v_{n+1} = \dfrac{u_n + 5v_n}6$. Soit $(w_n)$ définie par $w_n = v_n - u_n$.
1. (a) Montrer que $(w_n)$ est géométrique de raison $\frac7{12}$. $w_{n+1} = \dfrac{u_n + 5v_n}6 - \dfrac{3u_n + v_n}4 = \dfrac{2u_n + 10v_n - 9u_n - 3v_n}{12} = \dfrac7{12}(v_n - u_n)$.
   (b) En déduire $w_n$ en fonction de $n$. $w_n = \left(\frac7{12}\right)^n(v_0 - u_0) = 10\left(\frac7{12}\right)^n$.
   (c) Signe de $(w_n)$ : $w_n \geqslant 0$.
2. En utilisant la question précédente, montrer que $(u_n)$ et $(v_n)$ sont adjacentes. $u_{n+1} - u_n = \frac{v_n - u_n}4 = \frac14w_n \geqslant 0$ (croissante) ; $v_{n+1} - v_n = \frac{u_n - v_n}6 = -\frac16w_n \leqslant 0$ (décroissante) ; $v_n - u_n = 10\left(\frac7{12}\right)^n \to 0$ car $-1 < \frac7{12} < 1$.
3. La suite $(v_n)$ est-elle convergente ? Justifier en énonçant un théorème. Deux suites adjacentes convergent vers une même limite : $(v_n)$ converge.

## Exercice 4 : comparaison de suites
Type : comparaison de suites ($\sim$, $o$, $O$) · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/12
Formules : $u_n \sim v_n \iff \frac{u_n}{v_n} \to 1$ ; $u_n = o(v_n) \iff \frac{u_n}{v_n} \to 0$ ; $u_n = O(v_n) \iff \frac{u_n}{v_n}$ bornée ; convergente $\Rightarrow$ bornée, donc $\sim$ et $o$ impliquent $O$ ; croissances comparées : $\frac{\ln n}{n^a} \to 0$, $\frac{n^a}{e^n} \to 0$ ; $\frac{\sin n}{n} \to 0$ ; factoriser par le terme dominant

1. Soient $(u_n)$, $(v_n)$ ne s'annulant jamais. Deux définitions de $u_n \sim v_n$ : $\lim \frac{u_n}{v_n} = 1 \iff \exists (\varepsilon_n)$, $u_n = v_n(1 + \varepsilon_n)$, $\varepsilon_n \to 0$. De $u_n = o(v_n)$ : $\lim \frac{u_n}{v_n} = 0 \iff u_n = v_n\varepsilon_n$, $\varepsilon_n \to 0$.
2. Comparer avec $\sim$ ou $o(\cdot)$ :
   (a) $u_n = 1 - 3n^2$ et $v_n = -3n^2 + 2n - 4$ : $\dfrac{u_n}{v_n} = \dfrac{-\frac1{3n^2} + 1}{1 - \frac2{3n} + \frac4{3n^2}} \to 1$, donc $u_n \sim v_n$.
   (b) $u_n = e^{2n} - \sqrt n$ et $v_n = n + 1$ : $\dfrac{v_n}{u_n} = \dfrac{n}{e^{2n}} \times \dfrac{1 + \frac1n}{1 - \frac{\sqrt n}{e^{2n}}} \to 0$ (croissances comparées), donc $v_n = o(u_n)$.

## Exercice 5 : une suite
Type : monotonie et encadrement d'une somme · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/6
Formules : $u_{n+1} - u_n$ : écrire les deux sommes et simplifier les termes communs ($\frac1{2n} + \frac1{2n+1} - \frac1n$) ; $n \leqslant k \leqslant 2n-1 \Rightarrow \frac1{2n-1} \leqslant \frac1k \leqslant \frac1n$ ; somme de $n$ termes ; monotone bornée $\Rightarrow$ convergente ; passage à la limite dans les inégalités larges

Soit $(u_n)$ définie pour tout $n \in \mathbb{N}^*$ par $u_n = \displaystyle\sum_{k=1}^n \frac1{1 + \sqrt k}$.
1. Montrer que pour tout $n \in \mathbb{N}^*$, $u_n \geqslant \dfrac{n}{1 + \sqrt n}$. Pour $k \in [\![1, n]\!]$, $\frac1{1 + \sqrt k} \geqslant \frac1{1 + \sqrt n}$ ; on somme les $n$ termes.
2. En déduire le comportement de $(u_n)$ en $+\infty$. $\dfrac{n}{1 + \sqrt n} = \dfrac{\sqrt n}{\frac1{\sqrt n} + 1} \to +\infty$ ; par comparaison $u_n \to +\infty$.

## Exercice 6 : suite récurrente
Type : suite récurrente $u_{n+1} = f(u_n)$ · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/10
Formules : constante $\iff u_0 = f(u_0)$ ; tableau de variations via $f'$ ; $f$ croissante sur $I$ et $u_n \in I \Rightarrow f(a) < f(u_n) < f(b)$ (récurrence) ; signe de $u_{n+1} - u_n$ ; monotone bornée $\Rightarrow$ convergente ; $\ell = f(\ell)$

On considère $f : x \mapsto \dfrac{x^2 - x + 3}3$ et la suite $u_{n+1} = f(u_n)$, $u_0 \in \mathbb{R}^+$ donné.
1. Supposons que $(u_n)$ converge vers $\ell \in \mathbb{R}$. Valeurs possibles de $\ell$ : $f(\ell) = \ell \iff \ell^2 - 4\ell + 3 = 0 \iff (\ell - 1)(\ell - 3) = 0$ : $\ell = 1$ ou $\ell = 3$.
2. On suppose $u_0 = 2$. On admet le tableau de variations de $f$ : décroissante sur $[0, \frac12]$ de 1 à $\frac{11}{12}$, croissante sur $[\frac12, +\infty[$ avec $f(1) = 1$, $f(3) = 3$.
   (a) Montrer par récurrence que $\forall n$, $u_n \in ]1, 3[$. $u_0 = 2$ ; si $1 < u_n < 3$, $f$ strictement croissante sur $[\frac12, +\infty[$ donne $1 = f(1) < u_{n+1} < f(3) = 3$.
   (b) Montrer que $u_{n+1} - u_n = \dfrac{(u_n - 1)(u_n - 3)}3$ et en déduire la monotonie. $u_{n+1} - u_n = \dfrac{u_n^2 - 4u_n + 3}3 < 0$ car $u_n - 1 > 0$ et $u_n - 3 < 0$ : $(u_n)$ strictement décroissante.
   (c) Convergence et limite : décroissante et minorée par 1, elle converge vers $\ell \in \{1, 3\}$ ; $\ell \leqslant u_0 < 3$ donc $\ell = 1$.
