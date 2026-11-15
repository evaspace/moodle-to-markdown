# Feuille de TD — Études locales de fonctions : Landau et développements limités (S2 2026) (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (pas de corrigé officiel). Sujet : `td3-2030-s2-maths-subject-fr.md` (même dossier). Calculs vérifiés avec sympy. 

## Exercice 1.1
Type : petit o, grand O, équivalents (définitions et opérations) · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/3
Formules : $f = o(g) \iff \frac fg \to 0$ ; $f = O(g) \iff \frac fg$ bornée ; $f \sim g \iff \frac fg \to 1$ ; $f \sim \ell \neq 0 \iff f \to \ell$ (faux pour $\ell = 0$) ; $\sim$ compatible avec produit, quotient, puissance fixe, valeur absolue ; PAS avec somme, exponentielle, logarithme ; $o(x^p) + o(x^q) = o(x^{\min(p,q)})$ en 0 ; $o(x^p) \times o(x^q) = o(x^{p+q})$ ; croissances comparées : $\ln x = o(x)$ et $x = o(e^x)$ en $+\infty$

$f=o(0)$ signifie $f=0\cdot\varepsilon$, $g=O(0)$ signifie $g=0\cdot b$ et $h\sim0$ signifie $h=0\cdot(1+\varepsilon)$ : les trois fonctions sont identiquement nulles au voisinage de $0$.

## Exercice 1.2
Type : petit o, grand O, équivalents (définitions et opérations) · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/3
Formules : $f = o(g) \iff \frac fg \to 0$ ; $f = O(g) \iff \frac fg$ bornée ; $f \sim g \iff \frac fg \to 1$ ; $f \sim \ell \neq 0 \iff f \to \ell$ (faux pour $\ell = 0$) ; $\sim$ compatible avec produit, quotient, puissance fixe, valeur absolue ; PAS avec somme, exponentielle, logarithme ; $o(x^p) + o(x^q) = o(x^{\min(p,q)})$ en 0 ; $o(x^p) \times o(x^q) = o(x^{p+q})$ ; croissances comparées : $\ln x = o(x)$ et $x = o(e^x)$ en $+\infty$

$(P)$ est vraie si $\ell\ne0$ ($\frac{f}{\ell}\to1\iff f\to\ell$). Elle est fausse si $\ell=0$ : $f\sim0$ signifie $f=0$ au voisinage de $x_0$, alors que $f\to0$ n'impose pas $f=0$ (exemple $f(x)=x$ en $0$).

## Exercice 1.3
Type : équivalents simples (polynômes, fonctions usuelles, produits) · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/4
Formules : polynôme : équivalent au terme de plus bas degré en 0, de plus haut degré en $\pm\infty$ ; $x^\alpha = o(x^\beta)$ en $+\infty$ $\iff \alpha < \beta$, en 0 $\iff \alpha > \beta$ ; en 0 : $\sin x \sim x$, $e^x - 1 \sim x$, $\ln(1+x) \sim x$, $e^x \sim 1$ ; équivalent d'un produit ou d'un quotient = produit ou quotient des équivalents ; pour une somme, revenir au terme dominant

1. (a) $x^\alpha=o(x^\beta)$ en $+\infty\iff\alpha<\beta$. (b) En $0$ : $\iff\alpha>\beta$.
2. (a) $f(x)\sim-4x^3$ en $+\infty$. (b) $f(x)\sim2x$ en $0$.

## Exercice 1.4
Type : petit o, grand O, équivalents (définitions et opérations) · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/3
Formules : $f = o(g) \iff \frac fg \to 0$ ; $f = O(g) \iff \frac fg$ bornée ; $f \sim g \iff \frac fg \to 1$ ; $f \sim \ell \neq 0 \iff f \to \ell$ (faux pour $\ell = 0$) ; $\sim$ compatible avec produit, quotient, puissance fixe, valeur absolue ; PAS avec somme, exponentielle, logarithme ; $o(x^p) + o(x^q) = o(x^{\min(p,q)})$ en 0 ; $o(x^p) \times o(x^q) = o(x^{p+q})$ ; croissances comparées : $\ln x = o(x)$ et $x = o(e^x)$ en $+\infty$

1. $+\infty$ : $\ln x=o(x)$. $0^+$ : $x=o(\ln x)$ (car $\ln x\to-\infty$ et $x\to0$).
2. $+\infty$ : $x=o(e^x)$. $0$ : $e^x\to1$ et $x\to0$ : $x=o(e^x)$.
3. $+\infty$ : $2x^3-x^2-x\sim2x^3$ et $x^2+1\sim x^2$ : $x^2+1=o(2x^3-x^2-x)$. $0$ : $2x^3-x^2-x\sim-x=o(x^2+1)$ ($x^2+1\to1$).

## Exercice 1.5
Type : équivalents simples (polynômes, fonctions usuelles, produits) · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/4
Formules : polynôme : équivalent au terme de plus bas degré en 0, de plus haut degré en $\pm\infty$ ; $x^\alpha = o(x^\beta)$ en $+\infty$ $\iff \alpha < \beta$, en 0 $\iff \alpha > \beta$ ; en 0 : $\sin x \sim x$, $e^x - 1 \sim x$, $\ln(1+x) \sim x$, $e^x \sim 1$ ; équivalent d'un produit ou d'un quotient = produit ou quotient des équivalents ; pour une somme, revenir au terme dominant

1. $0$ : $\sim10$ ; $+\infty$ : $\sim2x^8$. 2. $0$ : $\sim-3x^7$ ; $+\infty$ : $\sim2x^8$.
3. $\dfrac{\sin x}x\to1$ : $\sin x\sim x$. 4. $e^x\sim1$. 5. $\dfrac{e^x-1}x\to1$ : $e^x-1\sim x$.

## Exercice 1.6
Type : petit o, grand O, équivalents (définitions et opérations) · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/3
Formules : $f = o(g) \iff \frac fg \to 0$ ; $f = O(g) \iff \frac fg$ bornée ; $f \sim g \iff \frac fg \to 1$ ; $f \sim \ell \neq 0 \iff f \to \ell$ (faux pour $\ell = 0$) ; $\sim$ compatible avec produit, quotient, puissance fixe, valeur absolue ; PAS avec somme, exponentielle, logarithme ; $o(x^p) + o(x^q) = o(x^{\min(p,q)})$ en 0 ; $o(x^p) \times o(x^q) = o(x^{p+q})$ ; croissances comparées : $\ln x = o(x)$ et $x = o(e^x)$ en $+\infty$

1. (a) $2f=o(x)$ (b) $f=o(2x)$, donc $f=o(x)$ (c) Aucune comparaison n'est possible en général entre $f$ et $g$ : $f=x^{3/2}$, $g=x^3$ donne $g=o(f)$, alors que $f=x^3$, $g=x^{5/2}$ donne $f=o(g)$.
2. (a) $f+g=o(x)$. (b) $f-g=o(x)$. (c) $fg=o(x^3)$. (d) $\dfrac fg$ : aucun $\alpha$ en général. (e) $xf=o(x^2)$. (f) $\dfrac gx=o(x)$.

## Exercice 1.7
Type : petit o, grand O, équivalents (définitions et opérations) · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/3
Formules : $f = o(g) \iff \frac fg \to 0$ ; $f = O(g) \iff \frac fg$ bornée ; $f \sim g \iff \frac fg \to 1$ ; $f \sim \ell \neq 0 \iff f \to \ell$ (faux pour $\ell = 0$) ; $\sim$ compatible avec produit, quotient, puissance fixe, valeur absolue ; PAS avec somme, exponentielle, logarithme ; $o(x^p) + o(x^q) = o(x^{\min(p,q)})$ en 0 ; $o(x^p) \times o(x^q) = o(x^{p+q})$ ; croissances comparées : $\ln x = o(x)$ et $x = o(e^x)$ en $+\infty$

1. Faux en général : $f=x^2+x\sim g=x^2$ et $h=-x^2\sim k=-x^2-x$ en $+\infty$, mais $f+h=x$ et $g+k=-x$ ne sont pas équivalents.
2. Vrai : $\dfrac{fh}{gk}=\dfrac fg\cdot\dfrac hk\to1$. 3. Vrai : $\dfrac{f/h}{g/k}=\dfrac fg\cdot\dfrac kh\to1$. 4. Vrai : $\left|\dfrac fg\right|\to1$. 5. Vrai (pour $f,g>0$ ou quand $f^\alpha$ est défini) : $\left(\dfrac fg\right)^\alpha\to1$.
6. Faux : $f=x+1$, $g=x$ en $+\infty$ : $e^f/e^g=e\ne1$. 7. Faux : $f=1+x$, $g=1+2x$ en $0$ : $f\sim g$ mais $\ln f\sim x$ et $\ln g\sim2x$ ne sont pas équivalents.

## Exercice 1.8
Type : équivalents simples (polynômes, fonctions usuelles, produits) · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/4
Formules : polynôme : équivalent au terme de plus bas degré en 0, de plus haut degré en $\pm\infty$ ; $x^\alpha = o(x^\beta)$ en $+\infty$ $\iff \alpha < \beta$, en 0 $\iff \alpha > \beta$ ; en 0 : $\sin x \sim x$, $e^x - 1 \sim x$, $\ln(1+x) \sim x$, $e^x \sim 1$ ; équivalent d'un produit ou d'un quotient = produit ou quotient des équivalents ; pour une somme, revenir au terme dominant

1. $0$ : $\dfrac{2x^3-x+6}{1-x}\sim6$. $+\infty$ : $\sim\dfrac{2x^3}{-x}=-2x^2$.
2. $\sin x\sim x$, $e^x-1\sim x$, $3x^2+2x\sim2x$ : produit $\sim2x^3$.
3. $0$ : $\sin x+x^2\sim x$. $+\infty$ : $\sim x^2$.

## Exercice 1.9
Type : petit o, équivalents et développements limités (manipulation) · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/10
Formules : $f = o(x^n) \iff f(x) = x^n\varepsilon(x)$, $\varepsilon \to 0$ ; $o(x^3) \Rightarrow o(x^2)$ (pas l'inverse) ; $o(x^p) + o(x^q) = o(x^{\min(p,q)})$ ; $f \sim$ premier terme non nul du DL ; $f \sim g \iff f - g = o(g)$ ; $\lim \frac{f}{x^n} = a \neq 0 \iff f \sim ax^n$

1. (a) $f\sim2x$. (b) $f-2x=-\dfrac{x^3}2+o(x^3)\sim-\dfrac{x^3}2$. (c) $f-2x+\dfrac{x^3}2=o(x^3)$ : on ne peut pas donner d'équivalent.
2. (a) Non : $\dfrac{x^4}8+o(x^4)=o(x^3)$, les deux hypothèses sont compatibles. (b) (a) $f\sim2x$ ; (b) $f-2x\sim-\dfrac{x^3}2$ ; (c) $f-2x+\dfrac{x^3}2=\dfrac{x^4}8+o(x^4)\sim\dfrac{x^4}8$.

## Exercice 2.10
Type : développements limités usuels et composés · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/8
Formules : $e^u = \sum \frac{u^k}{k!}$ ; $\cos u = 1 - \frac{u^2}2 + \frac{u^4}{24}$ ; $\sin u = u - \frac{u^3}6$ ; $\ln(1+u) = u - \frac{u^2}2 + \frac{u^3}3 - \frac{u^4}4$ ; $\sqrt{1+u} = 1 + \frac u2 - \frac{u^2}8 + \frac{u^3}{16} - \frac{5u^4}{128}$ ; $(1+u)^\alpha = 1 + \alpha u + \frac{\alpha(\alpha-1)}2u^2$ ; produit tronqué ; composition : poser $u$, calculer $u^2$ à l'ordre voulu ; $1 + \cos 2x = 2\cos^2 x$

1. $e^x=1+x+\dfrac{x^2}2+\dfrac{x^3}6+\dfrac{x^4}{24}+o(x^4)$.
2. $\ln(1+x)=x-\dfrac{x^2}2+\dfrac{x^3}3-\dfrac{x^4}4+o(x^4)$.
3. $(1+x)^\alpha=1+\alpha x+\dfrac{\alpha(\alpha-1)}2x^2+\dfrac{\alpha(\alpha-1)(\alpha-2)}6x^3+\dfrac{\alpha(\alpha-1)(\alpha-2)(\alpha-3)}{24}x^4+o(x^4)$.
4. $\sin x=x-\dfrac{x^3}6+o(x^4)$. 5. $\cos x=1-\dfrac{x^2}2+\dfrac{x^4}{24}+o(x^4)$.

## Exercice 2.11
Type : développements limités usuels et composés · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/8
Formules : $e^u = \sum \frac{u^k}{k!}$ ; $\cos u = 1 - \frac{u^2}2 + \frac{u^4}{24}$ ; $\sin u = u - \frac{u^3}6$ ; $\ln(1+u) = u - \frac{u^2}2 + \frac{u^3}3 - \frac{u^4}4$ ; $\sqrt{1+u} = 1 + \frac u2 - \frac{u^2}8 + \frac{u^3}{16} - \frac{5u^4}{128}$ ; $(1+u)^\alpha = 1 + \alpha u + \frac{\alpha(\alpha-1)}2u^2$ ; produit tronqué ; composition : poser $u$, calculer $u^2$ à l'ordre voulu ; $1 + \cos 2x = 2\cos^2 x$

1. $\dfrac1{1+x}-e^x=-2x+\dfrac{x^2}2-\dfrac{7x^3}6+o(x^3)$.
2. $e^x\cos x=1+x-\dfrac{x^3}3-\dfrac{x^4}6+o(x^4)$.
3. $\sin3x\ln(1-x)=(3x+o(x^2))\left(-x-\dfrac{x^2}2+o(x^2)\right)=-3x^2-\dfrac32x^3+o(x^3)$.
4. $e^{\sin x}=1+x+\dfrac{x^2}2-\dfrac{x^4}8+o(x^4)$.
5. $e^{\cos x}=e\cdot e^{-x^2/2+o(x^3)}=e-\dfrac e2x^2+o(x^3)$.
6. $\sqrt{1+2x}=1+x-\dfrac{x^2}2+\dfrac{x^3}2-\dfrac{5x^4}8+o(x^4)$.
7. $\ln(2+x)=\ln2+\ln\left(1+\dfrac x2\right)=\ln2+\dfrac x2-\dfrac{x^2}8+\dfrac{x^3}{24}+o(x^3)$.
8. $\ln(1+e^x)=\ln2+\ln\left(1+\dfrac{e^x-1}2\right)=\ln2+\dfrac x2+\dfrac{x^2}8+o(x^2)$.
9. $(1+x)^{1/x}=\exp\left(\dfrac{\ln(1+x)}x\right)=\exp\left(1-\dfrac x2+\dfrac{x^2}3\right)=e-\dfrac e2x+\dfrac{11e}{24}x^2+o(x^2)$.
10. $\cos(x)^{\sin x}=\exp(\sin x\ln\cos x)=\exp\left(-\dfrac{x^3}2+o(x^4)\right)=1-\dfrac{x^3}2+o(x^4)$.

## Exercice 2.12 (⋆)
Type : développements limités usuels et composés · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/8
Formules : $e^u = \sum \frac{u^k}{k!}$ ; $\cos u = 1 - \frac{u^2}2 + \frac{u^4}{24}$ ; $\sin u = u - \frac{u^3}6$ ; $\ln(1+u) = u - \frac{u^2}2 + \frac{u^3}3 - \frac{u^4}4$ ; $\sqrt{1+u} = 1 + \frac u2 - \frac{u^2}8 + \frac{u^3}{16} - \frac{5u^4}{128}$ ; $(1+u)^\alpha = 1 + \alpha u + \frac{\alpha(\alpha-1)}2u^2$ ; produit tronqué ; composition : poser $u$, calculer $u^2$ à l'ordre voulu ; $1 + \cos 2x = 2\cos^2 x$

1. $\dfrac1{\sqrt{2+x}}=\dfrac1{\sqrt2}\left(1+\dfrac x2\right)^{-1/2}$, d'où $\dfrac{\sqrt2}2-\dfrac{\sqrt2}8x+\dfrac{3\sqrt2}{64}x^2-\dfrac{5\sqrt2}{256}x^3+o(x^3)$.
2. $\ln(1+\cos x+\sin x)=\ln2+\dfrac x2-\dfrac38x^2+\dfrac1{12}x^3+o(x^3)$ (on écrit $1+\cos x+\sin x=2\left(1+\frac x2-\frac{x^2}4-\frac{x^3}{12}\right)+o(x^3)$ puis $\ln(1+u)=u-\frac{u^2}2+\frac{u^3}3$).
3. $\tan x=\dfrac{\sin x}{\cos x}=x+\dfrac{x^3}3+\dfrac{2x^5}{15}+o(x^5)$.

## Exercice 2.13
Type : développements limités, limite par équivalents · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/9
Formules : en 0 : $e^x = 1 + x + \frac{x^2}2 + \frac{x^3}6 + o(x^3)$ ; $\ln(1+x) = x - \frac{x^2}2 + o(x^2)$ ; $\cos x = 1 - \frac{x^2}2 + o(x^3)$ ; $\sin x = x - \frac{x^3}6 + o(x^3)$ ; $\frac1{1-x} = 1 + x + x^2 + x^3 + o(x^3)$ ; produit de DL tronqué à l'ordre ; $a^b = e^{b\ln a}$ ; $f \sim g \Rightarrow$ même limite

1. $e^x-\cos x-x=x^2+\dfrac{x^3}6+\dots$ et $x-\ln(1+x)=\dfrac{x^2}2-\dots$ : limite $2$.
2. $e^x-\cos x=x+x^2+o(x^2)$ donc le quotient vaut $\dfrac1x+1+o(1)$ : pas de limite (elle diverge vers $+\infty$ à droite et $-\infty$ à gauche).
3. $\dfrac{2x+o(x)}{x+o(x)}\to2$.
4. Numérateur : $\sin^2x-x\ln(1+x)=\dfrac{x^3}2+o(x^3)$. Dénominateur : $\dfrac{x^3}3+o(x^3)$. Limite $\dfrac32$.
5. $(1+x)^{1/x}-e=-\dfrac e2x+o(x)$ : limite $-\dfrac e2$.
6. $\left(1+\dfrac ax\right)^x=\exp\big(x\ln(1+\tfrac ax)\big)\to e^a$.
7. $\exp\big(x^2\ln\cos\tfrac1x\big)\to e^{-1/2}$.
8. $x^3\sin\dfrac1x=x^2-\dfrac16+o(1)$ donc la limite est $-\dfrac16$.
9. $\left(\dfrac n{n-42}\right)^n=\exp\left(-n\ln\left(1-\dfrac{42}n\right)\right)\to e^{42}$.
