# Examen S2-B3 APEF — mars 2025 (sujet, FR)

- Source : `raw/S2/Midterms/Maths PC/2029/PC/APEF/midterm-2029-s2-maths-subject-fr.pdf` (8 pages)
- Date réelle : mars 2025 (S2, bloc 3, dossier promo 2029). Pas de corrigé officiel dans les annales. Corrigé rédigé : `midterm-2029-s2-maths-correction-fr.md` (même dossier).
- Durée : 2 heures. Documents et calculatrices interdits. Barème sur 40 points, ramené à 20.

## Exercice 1 : polynômes (10 points)
Type : divisibilité de polynômes, multiplicité, factorisation dans $\mathbb{R}[X]$ et $\mathbb{C}[X]$ · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/9
Formules : $P(a) = 0 \iff X - a \mid P$ ; racine d'ordre $\geqslant 2$ $\iff P(a) = P'(a) = 0$ ; ordre exactement $m$ : $P^{(m)}(a) \neq 0$ ; $(X - a)^m \mid P$, $(X - a)^{m+1} \nmid P$ ; $X^2 + 1 = (X - i)(X + i)$ ; $\Delta < 0 \Rightarrow$ irréductible dans $\mathbb{R}[X]$

Les questions sont indépendantes.

1. Soit $P_1(X) = 2X^2 - X^3 + 6X^4 + 3X^6$. Sans utiliser la notion de dérivée, montrer que 0 est une racine de $P_1$ et trouver son ordre exact de multiplicité. Justifier.
2. Soit $P_2(X) = X^5 + 2X^4 + 2X^3 - 8X^2 - 19X - 10$. On admet que 2 est une racine simple de $P_2$.
   - (a) Montrer que $-1$ est une racine de $P_2$ et trouver son ordre exact de multiplicité, noté $\alpha$.
   - (b) Expliquer pourquoi le reste de la division euclidienne de $P_2$ par $(X-2)(X+1)^\alpha$ est nul puis effectuer cette division.
   - (c) En déduire l'écriture de $P_2$ comme produit de polynômes irréductibles dans $\mathbb{R}[X]$ et dans $\mathbb{C}[X]$. Justifier dans $\mathbb{R}[X]$.

## Exercice 2 : équations différentielles (10 points)
Type : EDO linéaires 1er ordre (variation de la constante) et 2nd ordre · ECUE : APIS (EDO) · Niveau : maths-s1-apis-edo/11
Formules : $y' + a(x)y = 0 \Rightarrow y = ke^{-A(x)}$, $A' = a$ ; solution générale = homogène + particulière ; variation de la constante $y_p = k(x)y_0(x)$ ; $ay'' + by' + cy = 0$ : $ar^2 + br + c = 0$, racine double $r$ : $y = (k_1x + k_2)e^{rx}$ ; second membre $P(x)e^{rx}$ : $y_p = Q(x)e^{rx}$

Les questions sont indépendantes.

1. On considère l'équation différentielle $(E)$ : $y'' - 6y' + 9y = 3$.
   - (a) Trouver une solution particulière (évidente) de $(E)$.
   - (b) Résoudre $(E)$ dans $\mathbb{R}$.
2. Résoudre, dans $]0, \pi[$, $(E)$ : $\sin(x)y' - \cos(x)y = x\sin^2(x)e^{-x}$.

## Exercice 3 : étude locale de fonctions (10 points)
Type : petit o, équivalents et développements limités (manipulation) · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/10
Formules : $f = o(x^n) \iff f(x) = x^n\varepsilon(x)$, $\varepsilon \to 0$ ; $o(x^3) \Rightarrow o(x^2)$ (pas l'inverse) ; $o(x^p) + o(x^q) = o(x^{\min(p,q)})$ ; $f \sim$ premier terme non nul du DL ; $f \sim g \iff f - g = o(g)$ ; $\lim \frac{f}{x^n} = a \neq 0 \iff f \sim ax^n$

Les questions sont indépendantes.

1. Soient $x_0 \in \mathbb{R} \cup \{+\infty, -\infty\}$ et $f$ et $g$ deux fonctions définies au voisinage de $x_0$ et ne s'y annulant pas. Donner deux définitions mathématiques de chacune des notations $f = o(g)$ et $f \sim g$ au voisinage de $x_0$.
2. Donner un équivalent en 0 ET en $+\infty$ de $P(x) = -x^4 + x^2 - 3x$.
3. Soient $f$ et $g$ deux fonctions telles qu'au voisinage de 0 : $f(x) = 2x - x^2 + o(x^2)$ et $g(x) = 2 - 3x^2 + x^3 + o(x^3)$.
   - (a) Donner un équivalent en 0 de $f$. Justifier brièvement en repartant de la définition.
   - (b) Donner un équivalent en 0 de $g$.
   - (c) Donner un équivalent en 0 de $h(x) = f(x) \times g(x)$.
   - (d) Donner un équivalent en 0 de $k(x) = f(x) - xg(x)$.
4. Soit $f$ une fonction dérivable une infinité de fois sur $\mathbb{R}$, telle qu'au voisinage de 0, $f(x) = 2x + 6x^3 + o(x^3)$.
   - (a) Remplacer les pointillés : $f(x) = \dots + o(x^2)$, $xf(x) = \dots + o(x^3)$, $xf(x) = \dots + o(x^4)$.
   - (b) Donner $f(0)$ ainsi que toutes les dérivées successives de $f$ en 0 que l'énoncé permet de connaître.

## Exercice 4 : développements limités (6 points)
Type : développements limités usuels et composés · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/8
Formules : $e^u = \sum \frac{u^k}{k!}$ ; $\cos u = 1 - \frac{u^2}2 + \frac{u^4}{24}$ ; $\sin u = u - \frac{u^3}6$ ; $\ln(1+u) = u - \frac{u^2}2 + \frac{u^3}3 - \frac{u^4}4$ ; $\sqrt{1+u} = 1 + \frac u2 - \frac{u^2}8 + \frac{u^3}{16} - \frac{5u^4}{128}$ ; $(1+u)^\alpha = 1 + \alpha u + \frac{\alpha(\alpha-1)}2u^2$ ; produit tronqué ; composition : poser $u$, calculer $u^2$ à l'ordre voulu ; $1 + \cos 2x = 2\cos^2 x$

1. Soient $f : x \mapsto \dfrac1{1 + x^2}$ et $g : x \mapsto \dfrac{\sin(x)}{1 + x^2}$.
   - (a) Donner le développement limité en 0 à l'ordre 4 de $f$.
   - (b) Donner le développement limité en 0 à l'ordre 4 de $g$.
2. Soit $h : x \mapsto \ln(1 + \cos(x))$.
   - (a) Quel sera le premier terme du développement limité de $h$ en 0 ?
   - (b) Trouver le développement limité de $h$ en 0 à l'ordre 4 après avoir pris soin de rappeler les DL des fonctions usuelles utilisées.

## Exercice 5 : calcul de limites (4 points)
Type : développements limités, limite par équivalents · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/9
Formules : en 0 : $e^x = 1 + x + \frac{x^2}2 + \frac{x^3}6 + o(x^3)$ ; $\ln(1+x) = x - \frac{x^2}2 + o(x^2)$ ; $\cos x = 1 - \frac{x^2}2 + o(x^3)$ ; $\sin x = x - \frac{x^3}6 + o(x^3)$ ; $\frac1{1-x} = 1 + x + x^2 + x^3 + o(x^3)$ ; produit de DL tronqué à l'ordre ; $a^b = e^{b\ln a}$ ; $f \sim g \Rightarrow$ même limite

1. Calculer $\displaystyle\lim_{x \to 0} \frac{e^{2x} - 2\sin(x) - 1}{1 - \sqrt{1 - x}}$. Vous prendrez soin de votre rédaction.
2. Calculer $\displaystyle\lim_{x \to +\infty} \left(\cos\Big(\frac1x\Big)\right)^{x^2}$. Vous prendrez soin de votre rédaction.
