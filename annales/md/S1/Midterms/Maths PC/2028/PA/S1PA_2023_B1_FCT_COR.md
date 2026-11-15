# Correction examen B1-FCT (S1 PA) — octobre 2023

- Source : `raw/S1/Midterms/Maths PC/2028/PA/S1PA_2023_B1_FCT_COR.pdf` (3 pages, corrigé avec énoncés)
- Date réelle : octobre 2023 (parcours PA, dossier promo 2028). Pas de sujet séparé. Courbes du corrigé non reproduites.

## Exercice 1 : calculs de limites
Type : limites de fonctions (croissances comparées, comparaison, asymptotes) · ECUE : APEF (fonctions)
Formules : $\lim_{+\infty} xe^{-x} = 0$ ; $-1 \leqslant \cos \leqslant 1$ ; $f \geqslant g$ et $g \to +\infty \Rightarrow f \to +\infty$ ; fraction rationnelle : factoriser par le terme dominant ; $\frac{a}{0^\pm} = \pm\infty$ selon les signes ; $\lim_a f = \pm\infty$ : asymptote $x = a$ ; $\lim_{\pm\infty} f = \ell$ : asymptote $y = \ell$

1. Calculer $\lim_{x \to +\infty} \sqrt{xe^{-x} + 1} - \dfrac{e^{-2x}}{(x+2)^4}$ en justifiant proprement.
Par croissance comparée, $\lim xe^{-x} = 0$ ; $\lim e^{-2x} = 0$ et $\lim (x+2)^4 = +\infty$. Donc la limite vaut $\sqrt1 = 1$.
2. Calculer $\lim_{x \to +\infty} x^2 + \cos(\sqrt x)$ en justifiant proprement.
Pour tout $x$, $-1 \leqslant \cos(\sqrt x) \leqslant 1$, donc $x^2 - 1 \leqslant x^2 + \cos(\sqrt x)$. Comme $x^2 - 1 \to +\infty$, par comparaison la limite vaut $+\infty$.
3. Soit $f : x \mapsto \dfrac{2x - 1}{x + 2}$. Calculer la limite de $f$ en $+\infty$, en $(-2)^-$ et $(-2)^+$ en justifiant proprement. Peut-on en déduire des asymptotes à la courbe représentative de $f$ ? Si oui, donner leurs équations.
- En $+\infty$ : $f(x) = \dfrac{x(2 - \frac1x)}{x(1 + \frac2x)} \to 2$ : asymptote $y = 2$.
- En $(-2)^-$ : $2x - 1 \to -5$ et $x + 2 \to 0^-$, donc $f \to +\infty$ : asymptote $x = -2$.
- En $(-2)^+$ : $2x - 1 \to -5$ et $x + 2 \to 0^+$, donc $f \to -\infty$ : asymptote $x = -2$.

## Exercice 2 : continuité
Type : continuité d'une fonction définie par morceaux · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/1
Formules : continue en $a$ $\iff \lim_{a^-} f = \lim_{a^+} f = f(a)$ ; continue à gauche : $\lim_{a^-} f = f(a)$ ; fonctions usuelles continues sur leur domaine

Soit $f$ définie sur $\mathbb{R}$ par $f(x) = 3x + 5$ si $x < -2$, $f(-2) = 4$, $f(x) = x^2$ si $x > -2$.
1. Tracer la courbe représentative de $f$ et conjecturer la continuité de $f$ sur $\mathbb{R}$.
Conjecture : $f$ est continue à droite en $-2$ mais pas à gauche ; continue sur $]-\infty, -2[$ et $]-2, +\infty[$.
2. Démontrer proprement votre conjecture.
$\lim_{(-2)^-} f = \lim 3x + 5 = -1 \neq f(-2)$ : pas continue à gauche en $-2$. $\lim_{(-2)^+} f = \lim x^2 = 4 = f(-2)$ : continue à droite. Sur $]-\infty, -2[$ et $]-2, +\infty[$, $f$ est continue (fonctions usuelles).

## Exercice 3 : dérivées
Type : dériver une composée · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/1
Formules : $(g \circ u)' = u' \times g' \circ u$ ; $(e^u)' = u'e^u$ ; $(\sqrt u)' = \frac{u'}{2\sqrt u}$ ; $(u^n)' = nu'u^{n-1}$ ; $(\ln u)' = \frac{u'}u$

Sans se soucier des domaines de définition, dériver :
1. $f : x \mapsto 2xe^{-x^3}$ : $f'(x) = 2e^{-x^3} + 2x \times (-3x^2)e^{-x^3} = e^{-x^3}(2 - 6x^3)$.
2. $g : x \mapsto \sqrt{6x^4 + x^2 + 1}$ : $g'(x) = \dfrac{24x^3 + 2x}{2\sqrt{6x^4 + x^2 + 1}} = \dfrac{12x^3 + x}{\sqrt{6x^4 + x^2 + 1}}$.
3. $h : x \mapsto \cos^4(x) + \tan(2x)$ : $h'(x) = 4\cos^3(x) \times (-\sin x) + 2(1 + \tan^2(2x))$.

## Exercice 4 : étude de fonction complète
Type : étude de fonction (parité, variations, asymptote, tangente) · ECUE : APEF (fonctions)
Formules : paire : $f(-x) = f(x)$ ; $(e^u)' = u'e^u$ ; signe de $f'$ donne les variations ; tangente en $a$ : $y = f'(a)(x - a) + f(a)$ ; $\lim_{+\infty} e^{-x^2/2} = 0$ : asymptote $y = 0$ ; paire : symétrie par rapport à l'axe des ordonnées

On considère $f$ définie sur $\mathbb{R}$ par $f(x) = e^{-\frac{x^2}2}$, de courbe $\mathcal{C}_f$.
1. Montrer que $f$ est paire. $f(-x) = e^{-\frac{(-x)^2}2} = f(x)$.
2. Trouver $f'$ et étudier son signe sur $[0, +\infty[$. $f'(x) = -xe^{-\frac{x^2}2} \leqslant 0$ sur $[0, +\infty[$.
3. Faire le tableau (complet) de variations de $f$ sur $[0, +\infty[$. $f$ décroît de $f(0) = 1$ vers $0$ en $+\infty$.
4. En déduire les éventuelles asymptotes à $\mathcal{C}_f$. La droite $y = 0$ est asymptote en $+\infty$.
5. Quelle est l'équation de la tangente à $\mathcal{C}_f$ au point d'abscisse 0 ? $y = f'(0)(x - 0) + f(0) = 1$ : tangente horizontale.
6. Donner l'allure de $\mathcal{C}_f$ sur $\mathbb{R}^+$, puis sur $\mathbb{R}$ (asymptotes et tangentes). Sur $\mathbb{R}$, par parité, l'axe des ordonnées est axe de symétrie (courbe en cloche).

## Exercice 5 : fonctions trigonométriques
Type : parité, périodicité, TVI pour une fonction trigonométrique · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/2
Formules : $\sin(-x) = -\sin x$, $\cos(-x) = \cos x$ ; $\sin$, $\cos$ $2\pi$-périodiques ; $\cos\frac{2\pi}3 = -\frac12$, $\sin\frac{2\pi}3 = \frac{\sqrt3}2$ ; TVI : $f$ continue et $f(a)f(b) < 0 \Rightarrow \exists \alpha \in ]a,b[$, $f(\alpha) = 0$

Soit $f$ définie sur $\mathbb{R}$ par $f(x) = \dfrac{\sin^2(x)}2 - \dfrac{\cos(x)}2$.
1. Montrer que $f$ est paire et $2\pi$-périodique.
$f(-x) = \frac{(-\sin x)^2}2 - \frac{\cos x}2 = f(x)$ ; $f(x + 2\pi) = \frac{\sin^2(x + 2\pi)}2 - \frac{\cos(x + 2\pi)}2 = f(x)$.
2. Montrer que $f$ est continue sur $\mathbb{R}$. $\sin$ et $\cos$ sont continues sur $\mathbb{R}$ ; $f$ est continue comme produit et différence de fonctions continues.
3. Compléter le tableau des variations de $f$ sur $[0, \pi]$ ($f$ croissante sur $[0, \frac{2\pi}3]$, décroissante sur $[\frac{2\pi}3, \pi]$).
$f(0) = -\frac12$, $f(\pi) = -\frac{-1}2 = \frac12$ et $f\left(\frac{2\pi}3\right) = \dfrac{(\sqrt3/2)^2}2 - \dfrac{-1/2}2 = \frac38 + \frac14 = \frac58$.
4. Justifier proprement que l'équation $f(x) = 0$ admet au moins une solution $\alpha$ dans $[0, \pi]$. Donner un intervalle $]a, b[$ strictement inclus dans $[0, \pi]$ tel que $\alpha \in ]a, b[$.
$f$ est continue sur $[0, \pi]$, $f(0) < 0$ et $f\left(\frac{2\pi}3\right) > 0$ : par le TVI, $\exists \alpha \in \left]0, \frac{2\pi}3\right[$, $f(\alpha) = 0$.
5. L'équation $f(x) = 0$ a-t-elle une infinité de solutions sur $\mathbb{R}$ ? Oui : $f$ étant $2\pi$-périodique (et paire), elle s'annule une infinité de fois.
