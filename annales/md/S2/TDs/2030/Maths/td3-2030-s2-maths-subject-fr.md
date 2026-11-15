# Feuille de TD — Études locales de fonctions : Landau et développements limités (S2 2026) (sujet, FR)

- Source : `raw/S2/TDs/2030/Maths/td3-2030-s2-maths-subject-fr.pdf` (7 pages)
- Date réelle : S2 2026 (dossier promo 2030). Feuille de TD, ECUE APEF (bloc B3). Pas de corrigé dans les annales.
- Seuls les exercices sont transcrits, avec les définitions à connaître par cœur. Les exercices marqués ⋆ sont plus difficiles.

Définitions à connaître par cœur (au voisinage de $x_0 \in \mathbb{R} \cup \{-\infty, +\infty\}$) :
- Négligeabilité : $f(x) = o(g(x))$ s'il existe une fonction $\varepsilon$ tendant vers 0 quand $x \to x_0$ telle que $f(x) = g(x)\varepsilon(x)$. Si $g$ ne s'annule pas : $f(x) = o(g(x)) \iff \dfrac{f(x)}{g(x)} \to 0$.
- Domination : $f(x) = O(g(x))$ s'il existe une fonction $b$ bornée telle que $f(x) = g(x)b(x)$. Si $g$ ne s'annule pas : $f(x) = O(g(x)) \iff \dfrac fg$ est bornée.
- Équivalence : $f(x) \sim g(x)$ s'il existe une fonction $\varepsilon$ tendant vers 0 telle que $f(x) = g(x)(1 + \varepsilon(x))$. Si $g$ ne s'annule pas : $f(x) \sim g(x) \iff \dfrac{f(x)}{g(x)} \to 1$.
- Taylor-Young : si $f$ est de classe $C^n$ sur $I$ et $x_0 \in I$, alors $f(x) = f(x_0) + f'(x_0)(x - x_0) + \dfrac{f''(x_0)}2(x - x_0)^2 + \dots + \dfrac{f^{(n)}(x_0)}{n!}(x - x_0)^n + o((x - x_0)^n)$.

## Exercice 1.1
Type : petit o, grand O, équivalents (définitions et opérations) · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/3
Formules : $f = o(g) \iff \frac fg \to 0$ ; $f = O(g) \iff \frac fg$ bornée ; $f \sim g \iff \frac fg \to 1$ ; $f \sim \ell \neq 0 \iff f \to \ell$ (faux pour $\ell = 0$) ; $\sim$ compatible avec produit, quotient, puissance fixe, valeur absolue ; PAS avec somme, exponentielle, logarithme ; $o(x^p) + o(x^q) = o(x^{\min(p,q)})$ en 0 ; $o(x^p) \times o(x^q) = o(x^{p+q})$ ; croissances comparées : $\ln x = o(x)$ et $x = o(e^x)$ en $+\infty$

Soient trois fonctions $f$, $g$ et $h$ telles que, au voisinage de $x_0 = 0$, $f(x) = o(0)$, $g(x) = O(0)$ et $h(x) \sim 0$. Que peut-on dire de ces trois fonctions ?

## Exercice 1.2
Type : petit o, grand O, équivalents (définitions et opérations) · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/3
Formules : $f = o(g) \iff \frac fg \to 0$ ; $f = O(g) \iff \frac fg$ bornée ; $f \sim g \iff \frac fg \to 1$ ; $f \sim \ell \neq 0 \iff f \to \ell$ (faux pour $\ell = 0$) ; $\sim$ compatible avec produit, quotient, puissance fixe, valeur absolue ; PAS avec somme, exponentielle, logarithme ; $o(x^p) + o(x^q) = o(x^{\min(p,q)})$ en 0 ; $o(x^p) \times o(x^q) = o(x^{p+q})$ ; croissances comparées : $\ln x = o(x)$ et $x = o(e^x)$ en $+\infty$

Soient une fonction $f$ définie sur $\mathbb{R}$, $x_0 \in \mathbb{R} \cup \{-\infty, +\infty\}$ et $\ell \in \mathbb{R}$. On s'intéresse au comportement de $f$ au voisinage de $x_0$. La proposition $(P)$ suivante est-elle vraie ? $(P)$ : $f(x) \sim \ell \iff f(x) \xrightarrow[x \to x_0]{} \ell$.

## Exercice 1.3
Type : équivalents simples (polynômes, fonctions usuelles, produits) · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/4
Formules : polynôme : équivalent au terme de plus bas degré en 0, de plus haut degré en $\pm\infty$ ; $x^\alpha = o(x^\beta)$ en $+\infty$ $\iff \alpha < \beta$, en 0 $\iff \alpha > \beta$ ; en 0 : $\sin x \sim x$, $e^x - 1 \sim x$, $\ln(1+x) \sim x$, $e^x \sim 1$ ; équivalent d'un produit ou d'un quotient = produit ou quotient des équivalents ; pour une somme, revenir au terme dominant

1. Soit $(\alpha, \beta) \in \mathbb{R}^2$. À quelle condition sur $\alpha$ et $\beta$ a-t-on : (a) $x^\alpha = o(x^\beta)$ quand $x$ tend vers $+\infty$ ? (b) $x^\alpha = o(x^\beta)$ quand $x$ tend vers 0 ?
2. Soit la fonction $f$ définie sur $\mathbb{R}$ par $f(x) = 2x - x^2 - 4x^3$. (a) Donner un équivalent simple de $f(x)$ au voisinage de $+\infty$. (b) Donner un équivalent simple de $f(x)$ au voisinage de 0.

## Exercice 1.4
Type : petit o, grand O, équivalents (définitions et opérations) · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/3
Formules : $f = o(g) \iff \frac fg \to 0$ ; $f = O(g) \iff \frac fg$ bornée ; $f \sim g \iff \frac fg \to 1$ ; $f \sim \ell \neq 0 \iff f \to \ell$ (faux pour $\ell = 0$) ; $\sim$ compatible avec produit, quotient, puissance fixe, valeur absolue ; PAS avec somme, exponentielle, logarithme ; $o(x^p) + o(x^q) = o(x^{\min(p,q)})$ en 0 ; $o(x^p) \times o(x^q) = o(x^{p+q})$ ; croissances comparées : $\ln x = o(x)$ et $x = o(e^x)$ en $+\infty$

Comparer aux voisinages de 0 et de $+\infty$ :
1. $\ln(x)$ et $x$
2. $e^x$ et $x$
3. $2x^3 - x^2 - x$ et $x^2 + 1$

## Exercice 1.5
Type : équivalents simples (polynômes, fonctions usuelles, produits) · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/4
Formules : polynôme : équivalent au terme de plus bas degré en 0, de plus haut degré en $\pm\infty$ ; $x^\alpha = o(x^\beta)$ en $+\infty$ $\iff \alpha < \beta$, en 0 $\iff \alpha > \beta$ ; en 0 : $\sin x \sim x$, $e^x - 1 \sim x$, $\ln(1+x) \sim x$, $e^x \sim 1$ ; équivalent d'un produit ou d'un quotient = produit ou quotient des équivalents ; pour une somme, revenir au terme dominant

Donner des équivalents simples de :
1. $2x^8 - 3x^7 + 10$ aux voisinages de 0 et de $+\infty$
2. $2x^8 - 3x^7$ aux voisinages de 0 et de $+\infty$
3. $\sin(x)$ au voisinage de 0. Indice : chercher $\lim_{x \to 0} \dfrac{\sin(x)}x$.
4. $e^x$ au voisinage de 0.
5. $e^x - 1$ au voisinage de 0. Indice : chercher $\lim_{x \to 0} \dfrac{e^x - 1}x$.

## Exercice 1.6
Type : petit o, grand O, équivalents (définitions et opérations) · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/3
Formules : $f = o(g) \iff \frac fg \to 0$ ; $f = O(g) \iff \frac fg$ bornée ; $f \sim g \iff \frac fg \to 1$ ; $f \sim \ell \neq 0 \iff f \to \ell$ (faux pour $\ell = 0$) ; $\sim$ compatible avec produit, quotient, puissance fixe, valeur absolue ; PAS avec somme, exponentielle, logarithme ; $o(x^p) + o(x^q) = o(x^{\min(p,q)})$ en 0 ; $o(x^p) \times o(x^q) = o(x^{p+q})$ ; croissances comparées : $\ln x = o(x)$ et $x = o(e^x)$ en $+\infty$

Soient deux fonctions $f$ et $g$ telles que, au voisinage de 0, $f(x) = o(x)$ et $g(x) = o(x^2)$.
1. Trouver les comparaisons possibles, quand il y en a, entre : (a) $2f(x)$ et $x$ ; (b) $f(x)$ et $2x$ ; (c) $f(x)$ et $g(x)$.
2. Pour chacune des fonctions suivantes, existe-t-il $\alpha \in \mathbb{R}$ tel que la fonction soit $o(x^\alpha)$ ? Si oui, donner $\alpha$. (a) $f + g$ ; (b) $f - g$ ; (c) $fg$ ; (d) $\dfrac fg$ (en supposant que $g$ ne s'annule pas) ; (e) $xf$ ; (f) $\dfrac gx$.

## Exercice 1.7
Type : petit o, grand O, équivalents (définitions et opérations) · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/3
Formules : $f = o(g) \iff \frac fg \to 0$ ; $f = O(g) \iff \frac fg$ bornée ; $f \sim g \iff \frac fg \to 1$ ; $f \sim \ell \neq 0 \iff f \to \ell$ (faux pour $\ell = 0$) ; $\sim$ compatible avec produit, quotient, puissance fixe, valeur absolue ; PAS avec somme, exponentielle, logarithme ; $o(x^p) + o(x^q) = o(x^{\min(p,q)})$ en 0 ; $o(x^p) \times o(x^q) = o(x^{p+q})$ ; croissances comparées : $\ln x = o(x)$ et $x = o(e^x)$ en $+\infty$

Soient quatre fonctions $f$, $g$, $h$ et $k$ définies sur $\mathbb{R}$ telles que, au voisinage d'un $x_0 \in \mathbb{R} \cup \{-\infty, +\infty\}$, $f \sim g$ et $h \sim k$. Lesquelles des propriétés ci-dessous peut-on déduire ? Justifier vos réponses.
1. $f + h \sim g + k$
2. $fh \sim gk$
3. $\dfrac fh \sim \dfrac gk$ (en supposant que les fonctions $h$ et $k$ ne s'annulent pas)
4. $|f| \sim |g|$
5. pour tout $\alpha \in \mathbb{R}$, $f^\alpha \sim g^\alpha$
6. $e^f \sim e^g$
7. $\ln(f) \sim \ln(g)$ (en supposant que les fonctions $f$ et $g$ sont strictement positives)

## Exercice 1.8
Type : équivalents simples (polynômes, fonctions usuelles, produits) · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/4
Formules : polynôme : équivalent au terme de plus bas degré en 0, de plus haut degré en $\pm\infty$ ; $x^\alpha = o(x^\beta)$ en $+\infty$ $\iff \alpha < \beta$, en 0 $\iff \alpha > \beta$ ; en 0 : $\sin x \sim x$, $e^x - 1 \sim x$, $\ln(1+x) \sim x$, $e^x \sim 1$ ; équivalent d'un produit ou d'un quotient = produit ou quotient des équivalents ; pour une somme, revenir au terme dominant

Trouver des équivalents simples des fonctions suivantes :
1. $\dfrac{2x^3 - x + 6}{1 - x}$ au voisinage de 0, puis au voisinage de $+\infty$
2. $\sin(x) \times (e^x - 1) \times (3x^2 + 2x)$ au voisinage de 0
3. $\sin(x) + x^2$ au voisinage de 0, puis au voisinage de $+\infty$

## Exercice 1.9
Type : petit o, équivalents et développements limités (manipulation) · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/10
Formules : $f = o(x^n) \iff f(x) = x^n\varepsilon(x)$, $\varepsilon \to 0$ ; $o(x^3) \Rightarrow o(x^2)$ (pas l'inverse) ; $o(x^p) + o(x^q) = o(x^{\min(p,q)})$ ; $f \sim$ premier terme non nul du DL ; $f \sim g \iff f - g = o(g)$ ; $\lim \frac{f}{x^n} = a \neq 0 \iff f \sim ax^n$

1. Soit une fonction $f$ telle que, au voisinage de 0, $f(x) = 2x - \dfrac{x^3}2 + o(x^3)$. Peut-on en déduire des équivalents simples des fonctions suivantes ? (a) $f(x)$ ; (b) $f(x) - 2x$ ; (c) $f(x) - 2x + \dfrac{x^3}2$.
2. On suppose maintenant que $f(x) = 2x - \dfrac{x^3}2 + \dfrac{x^4}8 + o(x^4)$.
   - (a) Est-ce que cette nouvelle hypothèse contredit l'hypothèse de la partie 1 ?
   - (b) Répondre aux questions de la partie 1 à partir de cette nouvelle hypothèse.

## Exercice 2.10
Type : développements limités usuels et composés · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/8
Formules : $e^u = \sum \frac{u^k}{k!}$ ; $\cos u = 1 - \frac{u^2}2 + \frac{u^4}{24}$ ; $\sin u = u - \frac{u^3}6$ ; $\ln(1+u) = u - \frac{u^2}2 + \frac{u^3}3 - \frac{u^4}4$ ; $\sqrt{1+u} = 1 + \frac u2 - \frac{u^2}8 + \frac{u^3}{16} - \frac{5u^4}{128}$ ; $(1+u)^\alpha = 1 + \alpha u + \frac{\alpha(\alpha-1)}2u^2$ ; produit tronqué ; composition : poser $u$, calculer $u^2$ à l'ordre voulu ; $1 + \cos 2x = 2\cos^2 x$

Rappeler les développements limités au voisinage de 0 à l'ordre 4 des fonctions suivantes :
1. $f(x) = e^x$
2. $g(x) = \ln(1 + x)$
3. $h(x) = (1 + x)^\alpha$ où $\alpha \in \mathbb{R}^*$
4. $i(x) = \sin(x)$
5. $j(x) = \cos(x)$

## Exercice 2.11
Type : développements limités usuels et composés · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/8
Formules : $e^u = \sum \frac{u^k}{k!}$ ; $\cos u = 1 - \frac{u^2}2 + \frac{u^4}{24}$ ; $\sin u = u - \frac{u^3}6$ ; $\ln(1+u) = u - \frac{u^2}2 + \frac{u^3}3 - \frac{u^4}4$ ; $\sqrt{1+u} = 1 + \frac u2 - \frac{u^2}8 + \frac{u^3}{16} - \frac{5u^4}{128}$ ; $(1+u)^\alpha = 1 + \alpha u + \frac{\alpha(\alpha-1)}2u^2$ ; produit tronqué ; composition : poser $u$, calculer $u^2$ à l'ordre voulu ; $1 + \cos 2x = 2\cos^2 x$

Déterminer, au voisinage de 0, les développements limités des fonctions suivantes :
1. $f(x) = \dfrac1{1+x} - e^x$ à l'ordre 3.
2. $g(x) = e^x\cos(x)$ à l'ordre 4.
3. $h(x) = \sin(3x)\ln(1 - x)$ à l'ordre 3.
4. $i(x) = e^{\sin(x)}$ à l'ordre 4.
5. $j(x) = e^{\cos(x)}$ à l'ordre 3.
6. $k(x) = \sqrt{1 + 2x}$ à l'ordre 4.
7. $l(x) = \ln(2 + x)$ à l'ordre 3.
8. $m(x) = \ln(1 + e^x)$ à l'ordre 2.
9. $n(x) = (1 + x)^{\frac1x}$ à l'ordre 2.
10. $o(x) = \big(\cos(x)\big)^{\sin(x)}$ à l'ordre 4.

## Exercice 2.12 (⋆)
Type : développements limités usuels et composés · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/8
Formules : $e^u = \sum \frac{u^k}{k!}$ ; $\cos u = 1 - \frac{u^2}2 + \frac{u^4}{24}$ ; $\sin u = u - \frac{u^3}6$ ; $\ln(1+u) = u - \frac{u^2}2 + \frac{u^3}3 - \frac{u^4}4$ ; $\sqrt{1+u} = 1 + \frac u2 - \frac{u^2}8 + \frac{u^3}{16} - \frac{5u^4}{128}$ ; $(1+u)^\alpha = 1 + \alpha u + \frac{\alpha(\alpha-1)}2u^2$ ; produit tronqué ; composition : poser $u$, calculer $u^2$ à l'ordre voulu ; $1 + \cos 2x = 2\cos^2 x$

Même question pour : $f(x) = \dfrac1{\sqrt{2 + x}}$ à l'ordre 3, $g(x) = \ln(1 + \cos(x) + \sin(x))$ à l'ordre 3, $h(x) = \tan(x)$ à l'ordre 5.

## Exercice 2.13
Type : développements limités, limite par équivalents · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/9
Formules : en 0 : $e^x = 1 + x + \frac{x^2}2 + \frac{x^3}6 + o(x^3)$ ; $\ln(1+x) = x - \frac{x^2}2 + o(x^2)$ ; $\cos x = 1 - \frac{x^2}2 + o(x^3)$ ; $\sin x = x - \frac{x^3}6 + o(x^3)$ ; $\frac1{1-x} = 1 + x + x^2 + x^3 + o(x^3)$ ; produit de DL tronqué à l'ordre ; $a^b = e^{b\ln a}$ ; $f \sim g \Rightarrow$ même limite

Étudier l'existence des limites suivantes. Si elles existent, donner leurs valeurs.
1. $\displaystyle\lim_{x \to 0} \frac{e^x - \cos(x) - x}{x - \ln(1 + x)}$
2. $\displaystyle\lim_{x \to 0} \frac{e^x - \cos(x)}{x^2}$
3. $\displaystyle\lim_{x \to 0} \frac{e^x - e^{-x}}{\ln(1 + x)}$
4. $\displaystyle\lim_{x \to 0} \frac{\sin^2(x) - x\ln(1 + x)}{e^x + \cos(x) - \sin(x) - 2}$
5. $\displaystyle\lim_{x \to 0} \frac{(1 + x)^{\frac1x} - e}x$
6. $\displaystyle\lim_{x \to +\infty} \Big(1 + \frac ax\Big)^x$ où $a \in \mathbb{R}$
7. $\displaystyle\lim_{x \to +\infty} \Big(\cos\Big(\frac1x\Big)\Big)^{x^2}$
8. $\displaystyle\lim_{x \to +\infty} x^3\sin\Big(\frac1x\Big) - x^2$
9. $\displaystyle\lim_{n \to +\infty} \Big(\frac n{n - 42}\Big)^n$
