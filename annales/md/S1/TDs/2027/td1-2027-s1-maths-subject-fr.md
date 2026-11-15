# Contrôle de cours 1, mathématiques S1 — lundi 3 octobre 2022 (sujet, FR)

- Source : `raw/S1/TDs/2027/td1-2027-s1-maths-subject-fr.pdf` (3 pages)
- Date réelle : 3 octobre 2022 (dossier promo 2027). Pas de corrigé.
- Durée : 1 heure. Barème sur 20.

## Exercice 1 (3,5 points)
Type : négations, implications et équivalences · ECUE : OBM · Niveau : maths-s1-obm/2
Formules : $\neg(P \wedge Q) = \neg P \vee \neg Q$ ; $\neg(P \vee (Q \wedge R)) = \neg P \wedge (\neg Q \vee \neg R)$ ; $\neg(P \Rightarrow Q) = P \wedge \neg Q$ ; $P \Rightarrow Q \equiv \neg P \vee Q$ ; $x^2 + x - 6 = (x+3)(x-2)$ ; multiple de 6 $\Rightarrow$ multiple de 3 ; $\sqrt{x^2} = |x|$

1. Soient $P$, $Q$ et $R$ trois assertions. Donner la négation de « $P \wedge Q$ », « $P \vee (Q \wedge R)$ » et de « $P \Rightarrow Q$ ».
2. Soit $x \in \mathbb{R}$. Mettre les symboles $\Rightarrow$, $\Leftarrow$ ou $\iff$ à la place des pointillés.
   1) $x < 1 \ \dots\ x \leqslant 1$. 2) $x^2 + x - 6 > 0 \ \dots\ x > 2$. 3) $\ln(x) = 3 \ \dots\ x = e^3$. 4) $x$ multiple de 3 $\dots$ $x$ multiple de 6.

## Exercice 2 (6 points)
Type : injectivité, surjectivité, image directe et réciproque · ECUE : OBM · Niveau : maths-s1-obm/10
Formules : injective : $f(x) = f(y) \Rightarrow x = y$ (contre-exemple $f(1) = f(2)$) ; surjective : $\forall y, \exists x, f(x) = y$ ; $f(A) = \{f(x), x \in A\}$ ; $f^{-1}(B) = \{x, f(x) \in B\}$ (peut être vide)

Soient $E$ et $F$ deux ensembles et $f : E \to F$.
1. Donner la définition mathématique (avec les quantificateurs) de « $f$ est injective ».
2. Donner la définition mathématique (avec les quantificateurs) de « $f$ est surjective ».
3. Prenons le cas $E = F = [\![1, 5]\!]$.
   (a) Dessiner (graphe, patates…) une fonction $f : E \to F$ vérifiant $f(\{1, 2, 5\}) = \{1, 4\}$. Votre fonction $f$ est-elle injective ? surjective ? Justifiez.
   (b) Dessiner (graphe, patates…) une fonction $f : E \to F$ bijective telle que $f^{-1}(\{3, 5\}) = \{3, 4\}$.

## Exercice 3 (4,5 points)
Type : primitive $u'\sqrt u$, théorème d'intégration par parties · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/6
Formules : $\int u'u^{1/2} = \frac23u^{3/2}$ ($x = \frac12(x^2+1)'$) ; IPP : $u$, $v$ de classe $C^1$ sur $[a,b]$, $\int_a^b uv' = [uv]_a^b - \int_a^b u'v$ ; preuve : $(uv)' = u'v + uv'$ intégré sur $[a,b]$

1. Sans intégration par parties ni changement de variable, calculer $I = \displaystyle\int_0^1 x\sqrt{x^2 + 1}\,dx$.
2. Énoncer proprement le théorème d'intégration par parties sans oublier ses hypothèses.
3. Démontrer soigneusement la formule d'intégration par parties.

## Exercice 4 (2,5 points)
Type : dénombrement (p-listes, arrangements, anagrammes, parties) · ECUE : DP · Niveau : maths-s1-dp/4
Formules : $p$-listes (avec remise, ordre) : $n^p$ ; arrangements (sans remise, ordre) : $A_n^p = \frac{n!}{(n-p)!}$ ; permutations : $n!$ ; anagrammes avec lettres répétées : $\frac{n!}{k_1!k_2!\dots}$ ; nombre de parties d'un ensemble à $m$ éléments : $2^m$ ; principe multiplicatif

On considère l'ensemble $E = \{a, b, c, d, e\}$. Compléter la fin des phrases suivantes :
1. Le nombre de 5-uplets de $E$ sans répétition est …
2. Le nombre de 3-uplets de $E$ avec répétition est …
3. Le nombre de 4-uplets de $E$ sans répétition et commençant par $a$ est …
4. Le nombre de sous-ensembles de $E$ est …
5. Le nombre de sous-ensembles à 3 éléments de $E$ est …

## Exercice 5 (3,5 points)
Type : coefficients binomiaux (symétrie) · ECUE : DP · Niveau : maths-s1-dp/6
Formules : $\binom np = \frac{n!}{p!(n-p)!}$ ; $\binom np = \binom n{n-p}$ ; $\binom np$ = nombre de parties à $p$ éléments d'un ensemble à $n$ éléments ; bijection $A \mapsto \bar A$

Soient $n \in \mathbb{N}$ et $k \in [\![0, n]\!]$.
1. Rappeler l'expression de $\dbinom nk$ et rappeler ce que compte cette quantité.
2. Considérons un ensemble $E$ de cardinal $n$. Expliquer (d'un point de vue dénombrement) pourquoi il y a autant de sous-ensembles de $E$ à $k$ éléments que de sous-ensembles de $E$ à $n - k$ éléments. Démontrer ensuite cette affirmation par le calcul.
