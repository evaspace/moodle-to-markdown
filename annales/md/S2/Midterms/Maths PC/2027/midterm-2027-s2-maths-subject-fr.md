# Contrôle S2 — février 2023 (sujet, FR)

- Source : `raw/S2/Midterms/Maths PC/2027/midterm-2027-s2-maths-subject-fr.pdf` (scan, 10 pages)
- Date réelle : février 2023 (dossier promo 2027). Corrigé : `midterm-2027-s2-maths-correction-fr.md`. Durée : 3 heures. Documents et calculatrices interdits. Barème sur 40 points, ramené à 20. 7 exercices.

## Exercice 1 : polynômes
Type : divisibilité de polynômes, multiplicité, factorisation dans $\mathbb{R}[X]$ et $\mathbb{C}[X]$ · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/9
Formules : $P(a) = 0 \iff X - a \mid P$ ; racine d'ordre $\geqslant 2$ $\iff P(a) = P'(a) = 0$ ; ordre exactement $m$ : $P^{(m)}(a) \neq 0$ ; $(X - a)^m \mid P$, $(X - a)^{m+1} \nmid P$ ; $X^2 + 1 = (X - i)(X + i)$ ; $\Delta < 0 \Rightarrow$ irréductible dans $\mathbb{R}[X]$

On considère le polynôme $P(X) = X^6 - X^5 - 3X^4 + 7X^3 + 14X^2 + 6X$.

1. Montrer que $-1$ est une racine de $P$ et trouver son ordre exact de multiplicité.

2. Que peut-on en déduire en termes de divisibilité ?

3. En vous aidant d'une seule division euclidienne, factoriser $P$ en produit de polynômes irréductibles dans $\mathbb{R}[X]$. Rappel : les polynômes irréductibles dans $\mathbb{R}[X]$ sont uniquement ceux de degré 1 et ceux de degré 2 à discriminant strictement négatif.

## Exercice 2 : équations différentielles
Type : EDO linéaires 1er ordre (variation de la constante) et 2nd ordre · ECUE : APIS (EDO) · Niveau : maths-s1-apis-edo/11
Formules : $y' + a(x)y = 0 \Rightarrow y = ke^{-A(x)}$, $A' = a$ ; solution générale = homogène + particulière ; variation de la constante $y_p = k(x)y_0(x)$ ; $ay'' + by' + cy = 0$ : $ar^2 + br + c = 0$, racine double $r$ : $y = (k_1x + k_2)e^{rx}$ ; second membre $P(x)e^{rx}$ : $y_p = Q(x)e^{rx}$

Dans cet exercice, les questions sont indépendantes.

1. On considère l'équation différentielle $(E_1)$ : $(x+1)y' - 2y = (x+1)^3\cos(3x)$ sur $I = ]-1, +\infty[$.
   - (a) Résoudre $(E_1)$ sur $I$.
   - (b) Trouver les solutions de $(E_1)$ telles que $y(0) = 1$.

2. Soit $(E_2)$ : $y'' + 4y' + 13y = (25x^2 + 16x + 2)e^{2x}$ sur $J = \mathbb{R}$.
   - (a) Montrer que $y_p : x \mapsto x^2e^{2x}$ est une solution particulière de $(E_2)$.
   - (b) Trouver toutes les solutions de $(E_2)$.

## Exercice 3 : études locales
Type : petit o, équivalents et développements limités (manipulation) · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/10
Formules : $f = o(x^n) \iff f(x) = x^n\varepsilon(x)$, $\varepsilon \to 0$ ; $o(x^3) \Rightarrow o(x^2)$ (pas l'inverse) ; $o(x^p) + o(x^q) = o(x^{\min(p,q)})$ ; $f \sim$ premier terme non nul du DL ; $f \sim g \iff f - g = o(g)$ ; $\lim \frac{f}{x^n} = a \neq 0 \iff f \sim ax^n$

1. Soient $f$ et $g$ deux fonctions définies sur $\mathbb{R}$. Soit $a \in \mathbb{R} \cup \{+\infty, -\infty\}$. Rappeler les définitions mathématiques de $f(x) \sim g(x)$ et $f(x) = o(g(x))$ au voisinage de $a$.

2. Donner, en justifiant, un équivalent simple (autre que la fonction elle-même) de $f(x) = 3x^3 - 2x^2 + 6x$ en $a = 0$ ET en $a = +\infty$.

3. Soient $h$ et $k$ deux fonctions telles qu'au voisinage de 0 : $h(x) = 1 + 2x + x^2 - 3x^3 + o(x^3)$ et $k(x) = -x + 3x^2 + o(x^2)$.
   - (a) Donner un équivalent le plus simple possible en 0 de : $h(x)$ (sans justifier), $k(x)$ (sans justifier) et $xh(x) + k(x)$ (en justifiant).
   - (b) A-t-on assez d'informations pour donner le développement limité de $h(x) + k(x)$ à l'ordre 1 ? À l'ordre 2 ? À l'ordre 3 ? Donner le développement limité quand la réponse est oui.

## Exercice 4 : développements limités
Type : développements limités usuels et composés · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/8
Formules : $e^u = \sum \frac{u^k}{k!}$ ; $\cos u = 1 - \frac{u^2}2 + \frac{u^4}{24}$ ; $\sin u = u - \frac{u^3}6$ ; $\ln(1+u) = u - \frac{u^2}2 + \frac{u^3}3 - \frac{u^4}4$ ; $\sqrt{1+u} = 1 + \frac u2 - \frac{u^2}8 + \frac{u^3}{16} - \frac{5u^4}{128}$ ; $(1+u)^\alpha = 1 + \alpha u + \frac{\alpha(\alpha-1)}2u^2$ ; produit tronqué ; composition : poser $u$, calculer $u^2$ à l'ordre voulu ; $1 + \cos 2x = 2\cos^2 x$

Dans cet exercice, vous prendrez soin de rappeler les développements limités usuels que vous devez utiliser.

1. Trouver le développement limité en 0 à l'ordre 3 de $f(x) = \cos(x)e^{-2x}$.

2. Calculer le développement limité en 0 à l'ordre 2 de $g(x) = \sqrt{1+x}$ à partir d'un des cinq DL usuels.

3. Trouver le développement limité en 0 à l'ordre 2 de $h(x) = \ln\big(1 + \sqrt{1+x}\big)$.

## Exercice 5 : calculs de limites
Type : développements limités, limite par équivalents · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/9
Formules : en 0 : $e^x = 1 + x + \frac{x^2}2 + \frac{x^3}6 + o(x^3)$ ; $\ln(1+x) = x - \frac{x^2}2 + o(x^2)$ ; $\cos x = 1 - \frac{x^2}2 + o(x^3)$ ; $\sin x = x - \frac{x^3}6 + o(x^3)$ ; $\frac1{1-x} = 1 + x + x^2 + x^3 + o(x^3)$ ; produit de DL tronqué à l'ordre ; $a^b = e^{b\ln a}$ ; $f \sim g \Rightarrow$ même limite

1. Calculer $\displaystyle\lim_{x \to 0} \frac{e^x + e^{-x} - 2}{\sin\big(\frac x2\big)}$. Vous devez utiliser les DL !

2. Calculer $\displaystyle\lim_{x \to +\infty} \left(1 + \ln\Big(1 + \frac1x\Big)\right)^x$. Vous devez utiliser les DL.

## Exercice 6 : espaces vectoriels 1
Type : reconnaître un sous-espace vectoriel · ECUE : EV · Niveau : maths-s2-ev/3
Formules : sev : contient 0, stable par addition et multiplication par un scalaire ; contre-exemple $\lambda u \notin E$ ; équation non linéaire ($z^2$) $\Rightarrow$ en général pas un sev ; $\mathrm{Vect}(\dots)$ est toujours un sev

1. Les ensembles suivants sont-ils des $\mathbb{R}$-espaces vectoriels ? Justifiez rigoureusement votre réponse.
   - (a) $E = \{(x,y) \in \mathbb{R}^2,\ x \leqslant y\}$.
   - (b) $F = \{(x,y,z) \in \mathbb{R}^3,\ x - y = 0\}$.
   - (c) $G = \{P \in \mathbb{R}[X],\ X \mid P\}$.

2. Dans cette question, il n'est pas demandé de justifier les réponses. Donner un sous-espace vectoriel de $E$ (autre que $E$ et $\{0_E\}$) dans les cas suivants :
   - (a) $E = \mathbb{R}^4$.
   - (b) $E = \mathbb{R}^{\mathbb{R}}$.
   - (c) $E = \{(u_n) \in \mathbb{R}^{\mathbb{N}},\ (u_n) \text{ converge}\}$.

## Exercice 7 : espaces vectoriels 2
Type : sous-espaces, intersection, somme directe · ECUE : EV · Niveau : maths-s2-ev/9
Formules : $\mathrm{Vect}(u)$ : droite si $u \neq 0$ ; plan $ax + by + cz = 0$ : exprimer $z$, $G = \mathrm{Vect}(u, v)$ ; $u \in F \cap G$ : paramétrer par $F$ puis injecter l'équation de $G$ ; Grassmann $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $\dim F + \dim G = \dim E$

Les deux questions sont indépendantes.

1. Dans $\mathbb{R}^3$, on considère les sous-espaces vectoriels $F = \{(x,y,z) \in \mathbb{R}^3,\ x = 0\}$ et $G = \{(x,y,z) \in \mathbb{R}^3,\ x = y\}$.
   - (a) A-t-on $F \cap G = \{0_{\mathbb{R}^3}\}$ ? Justifier.
   - (b) Rappeler la définition mathématique de l'ensemble $F + G$.
   - (c) Le vecteur $u = (1,2,3)$ appartient-il à $F + G$ ? Justifier.
   - (d) La décomposition que vous avez trouvée est-elle unique ? Justifier. Pourquoi en étiez-vous certain avant même de faire le moindre calcul ?

2. Soient $E$ un $\mathbb{R}$-espace vectoriel et $\mathcal{F} = (u_1, u_2, \dots, u_n) \in E^n$ une famille de $n$ vecteurs de $E$ ($n \in \mathbb{N}^*$).
   - (a) Donner la définition mathématique de : $\mathcal{F}$ est une famille libre de $E$.
   - (b) Donner la définition mathématique de : $\mathcal{F}$ est une famille génératrice de $E$.
   - (c) Dans $E = \mathbb{R}^3$, donner un exemple d'une famille libre composée de 2 vecteurs et un exemple d'une famille liée composée de 3 vecteurs. Justification non demandée.
   - (d) Dans $E = \mathbb{R}^2$, donner un exemple d'une famille génératrice de $E$. Justification non demandée.
