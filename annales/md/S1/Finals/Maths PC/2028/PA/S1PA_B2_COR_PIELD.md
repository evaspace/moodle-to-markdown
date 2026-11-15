# Correction examen PAB2-PIELD (S1 PA) — janvier 2024

- Source : `raw/S1/Finals/Maths PC/2028/PA/S1PA_B2_COR_PIELD.pdf` (4 pages, corrigé avec énoncés)
- Date réelle : janvier 2024 (parcours PA, dossier promo 2028). Pas de sujet séparé.
- Figures (courbes) du sujet non reproduites.

## Exercice 1 : calculs de primitives et intégrales
Type : primitives usuelles et intégrales par primitive directe · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/5
Formules : $\int x^n = \frac{x^{n+1}}{n+1}$ ; $\int \frac1{x^2} = -\frac1x$ ; $\int \frac1x = \ln|x|$ ; $\int \sqrt x = \frac23x^{3/2}$ ; $\int \frac1{\sqrt x} = 2\sqrt x$ ; $\int e^x = e^x$ ; $\int \sin = -\cos$ ; $\int (1 + \tan^2) = \tan$ ; $\int u'u^n = \frac{u^{n+1}}{n+1}$ ; $\int \frac{u'}{u^2} = -\frac1u$ ; $\int u'e^u = e^u$ ; $\int \frac{u'}u = \ln|u|$ ; $\int u'\cos u = \sin u$ ; $\int f(ax+b) = \frac1aF(ax+b)$

1. Remplir le tableau ($f$ la fonction, $F$ une primitive de $f$, sans se soucier du domaine).

| $f(x)$ | $\frac1{x^2}$ | $\ln 2$ | $x^4 + 2x$ | $e^x$ | $\sin x$ | $1 + \tan^2 x$ | $\sqrt x$ | $\frac2x$ |
|---|---|---|---|---|---|---|---|---|
| $F(x)$ | $-\frac1x$ | $x\ln 2$ | $\frac{x^5}5 + x^2$ | $e^x$ | $-\cos x$ | $\tan x$ | $\frac23 x^{3/2}$ | $2\ln\lvert x\rvert$ |

2. Donner une primitive $F$ sur $I$ de :
   (a) $x \mapsto 6e^x - \dfrac{2}{3\sqrt x}$, $I = ]0, +\infty[$ : $F(x) = 6e^x - \dfrac{4\sqrt x}3$.
   (b) $x \mapsto \dfrac{x}{(x^2 + 1)^2}$, $I = \mathbb{R}$ : $F(x) = -\dfrac1{2(x^2 + 1)}$.
3. Donner la primitive sur $\mathbb{R}$ de $f : x \mapsto \sin(x)\cos^3(x)$ qui vaut 2 en $\frac\pi4$.
   $F(x) = -\dfrac{\cos^4 x}4 + c$ ; $F\left(\frac\pi4\right) = 2 \iff -\dfrac{(\sqrt2/2)^4}4 + c = 2 \iff c = \dfrac{33}{16}$. Réponse : $x \mapsto -\dfrac{\cos^4 x}4 + \dfrac{33}{16}$.
4. Calculer $I = \displaystyle\int_0^1 e^{2u+1}\,du = \left[\frac{e^{2u+1}}2\right]_0^1 = \frac{e^3 - e}2$.
5. Calculer $J = \displaystyle\int_0^1 \frac{dt}{3t + 1} = \left[\frac{\ln(3t+1)}3\right]_0^1 = \frac{\ln 4}3 = \frac{2\ln 2}3$.
6. Calculer $K = \displaystyle\int_0^{\sqrt{\pi/6}} x\cos(x^2)\,dx = \left[\frac12\sin(x^2)\right]_0^{\sqrt{\pi/6}} = \frac12\sin\frac\pi6 = \frac14$.

## Exercice 2 : aire sous la courbe
Type : intégrale comme aire, relation de Chasles · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/2
Formules : $f \geqslant 0$ : $\int_a^b f$ = aire sous la courbe ; rectangle $L \times l$, triangle $\frac{b \times h}2$ ; Chasles : $\int_a^c = \int_a^b + \int_b^c$ ; continue sur $I$ $\Rightarrow$ admet une primitive

On considère la fonction $f$ définie sur $[-2, 3]$ par $f(x) = 1$ si $x \in [-2, 0]$, $f(x) = x + 1$ si $x \in ]0, 1]$, $f(x) = -x + 3$ si $x \in ]1, 3]$.
1. Construire la courbe représentative de $f$ sur $[-2, 3]$.
2. La fonction $f$ est-elle continue sur $[-2, 3]$ ? $f$ admet-elle une primitive sur $[-2, 3]$ ? Justifier.
   $f$ est continue sur $[-2, 3]$ ; toute fonction continue sur un intervalle y admet une primitive.
3. Déterminer graphiquement $\int_{-2}^3 f(t)\,dt$.
   $f$ est positive : somme des aires $2 \times 1 + 1 \times 1 + \frac{1 \times 1}2 + \frac{2 \times 2}2 = \frac{11}2$.
4. Retrouver le résultat par un calcul détaillé.
   Chasles : $\displaystyle\int_{-2}^0 1\,dx + \int_0^1 (x+1)\,dx + \int_1^3 (-x+3)\,dx = 2 + \frac32 + 2 = \frac{11}2$.

## Exercice 3 : propriétés des intégrales
Type : Chasles, positivité, valeur moyenne · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/2
Formules : $\int_b^a = -\int_a^b$ ; Chasles ; $f \leqslant g$ sur $[a,b]$ $\Rightarrow \int_a^b f \leqslant \int_a^b g$ ; valeur moyenne $\mu = \frac1{b-a}\int_a^b f$ ; $\ln(2e^3) = \ln 2 + 3$, $\ln\sqrt2 = \frac12\ln2$

Les questions sont indépendantes.
1. Calculer $I = \displaystyle\int_2^3 \sqrt{e^{t^2} + 1}\,dt + \int_3^2 \sqrt{e^{x^2} + 1}\,dx$.
   $I = \displaystyle\int_2^3 \sqrt{e^{t^2} + 1}\,dt - \int_2^3 \sqrt{e^{x^2} + 1}\,dx = 0$.
2. Soit $f$ continue sur $\mathbb{R}$ avec $\displaystyle\int_1^8 f = \ln 8$, $\int_1^5 f = \ln(2e^3)$ et $\int_3^5 f = \ln\sqrt2 + 3$. Donner $I = \displaystyle\int_3^8 f(t)\,dt$ en fonction de $\ln 2$.
   Chasles : $I = \int_3^5 f + \int_1^8 f - \int_1^5 f = \frac12\ln 2 + 3 + 3\ln 2 - \ln 2 - 3 = \frac{5\ln 2}2$.
3. Montrer que pour tout $t \in [2, 4]$, $2t^2 - t^3 \leqslant 0$. En déduire, sans calcul, que $\int_2^4 2t^2\,dt \leqslant \int_2^4 t^3\,dt$.
   $2t^2 - t^3 = t^2(2 - t) \leqslant 0$ sur $[2,4]$, d'où le résultat par croissance de l'intégrale.
4. Soit $f : x \mapsto (x + 2)^2$ (courbe donnée, surface hachurée entre $-1$ et $1$).
   (a) Aire : $A = \displaystyle\int_{-1}^1 (x+2)^2\,dx = \left[\frac{(x+2)^3}3\right]_{-1}^1 = 9 - \frac13 = \frac{26}3$.
   (b) Valeur moyenne de $f$ sur $[-1, 1]$ : $\mu = \dfrac{A}{2} = \dfrac{13}3$.

## Exercice 4 : équations différentielles
Type : EDO linéaires 1er ordre (variation de la constante) et 2nd ordre · ECUE : APIS (EDO) · Niveau : maths-s1-apis-edo/5
Formules : $y' + a(x)y = 0 \Rightarrow y = ke^{-A(x)}$, $A' = a$ ; solution générale = homogène + particulière ; variation de la constante $y_p = k(x)y_0(x)$ ; $ay'' + by' + cy = 0$ : $ar^2 + br + c = 0$, racine double $r$ : $y = (k_1x + k_2)e^{rx}$ ; second membre $P(x)e^{rx}$ : $y_p = Q(x)e^{rx}$

1. Résoudre dans $]0, +\infty[$ l'équation $(E) : 4y' - \dfrac2x y = -\dfrac1x$.
   $(E_0)$ : $y' = \frac1{2x}y$, $y_0(x) = ke^{\frac12\ln x} = k\sqrt x$. Solution évidente $y_p = \frac12$.
   $S = \left\{x \mapsto k\sqrt x + \frac12 ; k \in \mathbb{R}\right\}$.
2. Résoudre dans $[0, +\infty[$ l'équation $(E) : (x+1)y' - y = (x+1)^2\sin(x)$.
   $(E_0)$ : $y_0(x) = ke^{\ln(x+1)} = k(x+1)$. Variation de la constante $y_p = k(x)(x+1)$ : $k'(x)(x+1)^2 = (x+1)^2\sin x$, $k'(x) = \sin x$, $k(x) = -\cos x$, $y_p(x) = -(x+1)\cos x$.
   $S = \{x \mapsto k(x+1) - (x+1)\cos x ; k \in \mathbb{R}\}$.
3. Résoudre dans $\mathbb{R}$ l'équation $(E) : y'' - 2y' + y = xe^x$.
   Équation caractéristique $(r-1)^2 = 0$ : $y_0(x) = (k_1x + k_2)e^x$. On cherche $y_p = Q(x)e^x$ : $Q'' = x$, $Q = \frac{x^3}6$, $y_p = \frac{x^3}6 e^x$.
   $S = \left\{x \mapsto (k_1x + k_2)e^x + \frac{x^3}6 e^x ; (k_1, k_2) \in \mathbb{R}^2\right\}$.
