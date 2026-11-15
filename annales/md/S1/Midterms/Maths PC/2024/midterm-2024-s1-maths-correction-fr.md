# Corrigé du contrôle S1 — octobre 2019

- Source : `raw/S1/Midterms/Maths PC/2024/midterm-2024-s1-maths-correction-fr.pdf` (2 pages ; en-tête « novembre 2019 », le sujet est daté d'octobre 2019)
- Date réelle : octobre 2019 (S1 2019, dossier promo 2024). Sujet : `midterm-2024-s1-maths-subject-fr.md`.

## Exercice 1 (2 points)
Type : vérité d'une proposition quantifiée · ECUE : OBM · Niveau : maths-s1-obm/4
Formules : $\forall$ : une seule valeur contre-exemple suffit pour réfuter ; $\exists$ : un seul exemple suffit pour prouver ; $\forall x \exists y$ : $y$ peut dépendre de $x$ ; $y^2 \geqslant 0$

1. Fausse : prendre par exemple $x = y = 1$.
2. Fausse : prendre par exemple $x = 1$.
3. Vraie : il suffit de prendre $x = -y^2$.
4. Vraie : prendre $x = y = 0$.

## Exercice 2 (3,5 points)
Type : dérivée composée, double IPP, changement de variable · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/13
Formules : $(\arctan u)' = \frac{u'}{1+u^2}$ ; IPP : $\int_a^b uv' = [uv]_a^b - \int_a^b u'v$ (deux fois pour un polynôme de degré 2) ; $\int \cos\frac x2 = 2\sin\frac x2$, $\int \sin\frac x2 = -2\cos\frac x2$ ; $u = e^x \Rightarrow dx = \frac{du}u$ ; $\int \frac{du}{u+1} = \ln(u+1)$

1. $f'(x) = \dfrac{1}{\left(1 + \arctan^2(x)\right)(1 + x^2)}$.
2. IPP avec $u(x) = x^2 + x$ et $v'(x) = \cos\left(\frac x2\right)$ :
$J = 2\left[(x^2 + x)\sin\left(\frac x2\right)\right]_0^\pi - 2\displaystyle\int_0^\pi (2x + 1)\sin\left(\frac x2\right)dx = 2\left(\pi^2 + \pi - \int_0^\pi (2x + 1)\sin\left(\frac x2\right)dx\right)$.
Nouvelle IPP avec $u(x) = 2x + 1$ et $v'(x) = \sin\left(\frac x2\right)$ :
$\displaystyle\int_0^\pi (2x + 1)\sin\left(\frac x2\right)dx = -2\left[(2x + 1)\cos\left(\frac x2\right)\right]_0^\pi + 4\int_0^\pi \cos\left(\frac x2\right)dx = 2 + 8\left[\sin\left(\frac x2\right)\right]_0^\pi = 10$.
Finalement $J = 2(\pi^2 + \pi - 10)$.
3. $u = e^x$, $x = \ln u$, $dx = \frac{du}u$ : $K = \displaystyle\int_1^e \frac{1}{1 + \frac1u}\frac{du}u = \int_1^e \frac{du}{u + 1} = [\ln(u + 1)]_1^e = \ln(e + 1) - \ln 2$.

## Exercice 3 (2 points)
Type : injectivité / surjectivité, composées · ECUE : OBM · Niveau : maths-s1-obm/10
Formules : injective : $f(x) = f(y) \Rightarrow x = y$, contre-exemple $f(a) = f(b)$ avec $a \neq b$ ; surjective : $\forall y, \exists x, f(x) = y$ ; $(f \circ g)(x) = f(g(x))$

1. $f$ n'est pas surjective car 2 n'a pas d'antécédent par $f$. $f$ est injective car si $f(x) = f(y)$ alors $2x + 4 = 2y + 4$ donc $x = y$.
2. $g$ n'est pas surjective car 1 n'a pas d'antécédent par $g$. $g$ est injective car si $g(x) = g(y)$ alors $\frac x2 + 2 = \frac y2 + 2$ donc $x = y$.

## Exercice 4 (1,5 points)
Type : relation d'équivalence · ECUE : OBM · Niveau : maths-s1-obm/11
Formules : équivalence = réflexive ($x\mathcal Rx$), symétrique ($x\mathcal Ry \Rightarrow y\mathcal Rx$), transitive ($x\mathcal Ry$ et $y\mathcal Rz \Rightarrow x\mathcal Rz$)

Réflexive : $(a,b)\,\mathcal{R}\,(a,b)$ vu que $ab = ba$.
Symétrique : si $ab' = ba'$ alors $a'b = b'a$, d'où $(a',b')\,\mathcal{R}\,(a,b)$.
Transitive : si $ab' = ba'$ et $a'b'' = b'a''$, alors ($b, b', b'' \neq 0$) $\frac ab = \frac{a'}{b'}$ et $\frac{a'}{b'} = \frac{a''}{b''}$, donc $\frac ab = \frac{a''}{b''}$ et $(a,b)\,\mathcal{R}\,(a'',b'')$.

## Exercice 5 (3 points)
Type : dénombrement (p-listes, arrangements, anagrammes, parties) · ECUE : DP · Niveau : maths-s1-dp/3
Formules : $p$-listes (avec remise, ordre) : $n^p$ ; arrangements (sans remise, ordre) : $A_n^p = \frac{n!}{(n-p)!}$ ; permutations : $n!$ ; anagrammes avec lettres répétées : $\frac{n!}{k_1!k_2!\dots}$ ; nombre de parties d'un ensemble à $m$ éléments : $2^m$ ; principe multiplicatif

1. $n^p$.
2. $A_n^p = n(n-1)\dots(n-p+1)$.
3. Les anagrammes de « table » sont les permutations de $\{t, a, b, l, e\}$ : $5! = 120$. Pour « tableau », même principe mais la lettre « a » est répétée deux fois : le corrigé donne $\frac{5!}{2!} = 60$ ; « tableau » ayant 7 lettres, le bon compte est $\frac{7!}{2!} = 2520$.
4. $n$ façons de choisir le président, puis autant de façons de choisir les autres conseillers que de parties de l'ensemble des $n - 1$ autres membres : $n\,2^{n-1}$ bureaux.

## Exercice 6 (3 points)
Type : tirages simultanés, combinaisons · ECUE : DP · Niveau : maths-s1-dp/7
Formules : tirage simultané de $k$ parmi $n$ : $\binom nk$ ; « A ou B » incompatibles : additionner ; « A et B » : multiplier les $\binom{}{}$ ; contraire : $P(\bar A) = 1 - P(A)$ ; équiprobabilité

1. 3 rouges (parmi 5) ou 3 vertes (parmi 3) : $\dfrac{\binom53 + \binom33}{\binom{10}3} = \dfrac{11}{120}$.
2. 1 rouge et 1 verte et 1 blanche : $\dfrac{\binom51\binom31\binom21}{\binom{10}3} = \dfrac{30}{120} = \dfrac14$.
3. Contraire de « une seule couleur » : $1 - \dfrac{11}{120}$.

## Exercice 7 (2 points)
Type : indépendance et incompatibilité · ECUE : DP · Niveau : maths-s1-dp/11
Formules : indépendants $\iff P(A \cap B) = P(A)P(B) \iff P_B(A) = P(A)$ ; $P_B(A) = \frac{P(A \cap B)}{P(B)}$ ; incompatibles $\iff A \cap B = \emptyset$

$A$ : « $X$ pair », $B$ : « $X \leqslant 4$ ». $P(A) = 0{,}1 + 0{,}2 + 0{,}3 + 0{,}1 = 0{,}7$.
$P_B(A) = \dfrac{0{,}1 + 0{,}2}{0{,}4} = \dfrac34 \neq P(A)$ donc $A$ et $B$ ne sont pas indépendants (le corrigé divise par 0,7 au lieu de $P(B) = 0{,}4$ ; la conclusion ne change pas).
$A$ et $B$ ne sont pas incompatibles car $(X = 2) \subset A \cap B$.

## Exercice 8 (3 points)
Type : probabilités totales et Bayes · ECUE : DP · Niveau : maths-s1-dp/10
Formules : probabilités totales : $P(M) = P(M \mid V)P(V) + P(M \mid \bar V)P(\bar V)$ ; Bayes : $P(V \mid M) = \frac{P(M \mid V)P(V)}{P(M)}$ ; $P(\bar V) = 1 - P(V)$

$M$ : « atteinte de la grippe », $V$ : « vaccinée ». $P(V) = 0{,}6$, $P(M) = 0{,}1$, $P_M(V) = 0{,}06$.
1. a. $P_V(M) = \dfrac{P_M(V)P(M)}{P(V)} = \dfrac{0{,}06 \times 0{,}1}{0{,}6} = 0{,}01 = 1\,\%$.
   b. $P_{\bar V}(M) = \dfrac{P_M(\bar V)P(M)}{P(\bar V)} = \dfrac{0{,}94 \times 0{,}1}{0{,}4} = 0{,}235$ (le corrigé divise par 0,6 et trouve $\simeq 15{,}6\,\%$ : erreur, $P(\bar V) = 0{,}4$).
2. On veut $P(M) = \frac{500}{10000} = 0{,}05$. Avec $p = P(V)$ : $P(M) = P_V(M)p + P_{\bar V}(M)(1 - p)$, soit $0{,}05 = 0{,}01p + c(1 - p)$, donc $p = \dfrac{c - 0{,}05}{c - 0{,}01}$.
