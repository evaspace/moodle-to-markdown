# Contrôle de cours 1 (S2) — lundi 30 janvier 2023 (sujet, FR)

- Source : `raw/S2/TDs/2027/td3-2027-s2-maths-subject-fr.pdf` (3 pages)
- Date réelle : 30 janvier 2023 (dossier promo 2027). Pas de corrigé dans les annales.
- Durée : 1 heure. Barème sur 20. Quatre questions de cours.

## Cours 1 : divisibilité et division euclidienne (3 points)
Type : degré, division euclidienne de polynômes, racine · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/2
Formules : $\deg(A+B) \leqslant \max(\deg A, \deg B)$ ; $\deg(AB) = \deg A + \deg B$ ; $\exists!\,(Q,R)$, $A = BQ + R$, $\deg R < \deg B$ ; $\alpha$ racine $\iff A(\alpha) = 0 \iff X - \alpha \mid A$

Soit $(E, F) \in (\mathbb{R}[X])^2$. On suppose de plus que $E$ n'est pas le polynôme nul.
1. Donner la définition mathématique de $E \mid F$ ainsi qu'un exemple avec $E = 2X - 1$ et $F$ de degré 2.
2. - (a) Énoncer soigneusement le théorème de la division euclidienne de $F$ par $E$.
   - (b) Trouver le quotient et le reste de la division euclidienne de $F = X^3 - 3X^2 + 5X - 7$ par $E = X - 1$.

## Cours 2 : racines (6 points)
Type : divisibilité de polynômes, multiplicité, factorisation dans $\mathbb{R}[X]$ et $\mathbb{C}[X]$ · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/9
Formules : $P(a) = 0 \iff X - a \mid P$ ; racine d'ordre $\geqslant 2$ $\iff P(a) = P'(a) = 0$ ; ordre exactement $m$ : $P^{(m)}(a) \neq 0$ ; $(X - a)^m \mid P$, $(X - a)^{m+1} \nmid P$ ; $X^2 + 1 = (X - i)(X + i)$ ; $\Delta < 0 \Rightarrow$ irréductible dans $\mathbb{R}[X]$

Les questions sont indépendantes.
1. Soit $P \in \mathbb{R}[X]$ de degré strictement supérieur à 3. Mettre les symboles $\Rightarrow$, $\Leftarrow$ ou $\iff$ à la place des pointillés. a) 1 racine de $P$ $\dots$ $(X-1) \mid P$. b) $(X-1)^2 \mid P$ $\dots$ $P(1) = 0$. c) $P(0) = 0$ $\dots$ $(X^2 - X) \mid P$.
2. Soient $P \in \mathbb{R}[X]$ et $a \in \mathbb{R}$ tels que $P(a) = P'(a) = P''(a) = 0$ et $P^{(3)}(a) \neq 0$. Quel est l'ordre exact de multiplicité de la racine $a$ ? À quoi cet énoncé est-il équivalent en termes de divisibilité ? Traduire ensuite à l'aide de quantificateurs ce que vous avez écrit.
3. Donner un exemple d'un polynôme de $\mathbb{R}[X]$, de degré 6, qui admet $-1$ comme racine d'ordre de multiplicité exactement 3 et tel que $P(0) = P'(0) = 0$. On ne vous demande pas de justifier.
4. Soit $P(X) = X^3(X+2)^2(X^2 - X - 6)(X^2 + X + 1)$.
   - (a) Donner le degré de $P$ en expliquant brièvement comment vous l'avez obtenu.
   - (b) Écrire $P$ comme produit de polynômes irréductibles dans $\mathbb{R}[X]$ (justifier brièvement). Donner ensuite toutes les racines réelles de $P$.

## Cours 3 : équations différentielles (7 points)
Type : démonstration de cours (solutions de $a(t)y' + b(t)y = 0$) · ECUE : APIS (EDO) · Niveau : maths-s1-apis-edo/4
Formules : $S_0 = \{t \mapsto ke^{-F(t)}, k \in \mathbb{R}\}$ avec $F$ primitive de $\frac ba$, $F' = \frac ba$ ; $z = y_0e^F \Rightarrow z' = (y_0' + \frac bay_0)e^F = 0 \Rightarrow z$ constante (inclusion $\subset$) ; réciproque : dériver $ke^{-F}$ et reporter (inclusion $\supset$) ; $\int \frac{u'}u = \ln|u|$, $e^{-\alpha\ln u} = u^{-\alpha}$

Soit l'équation différentielle $(E_0)$ : $a(t)y'(t) + b(t)y(t) = 0$ où $a$ et $b$ sont deux fonctions définies et continues sur $\mathbb{R}$. On suppose de plus que la fonction $a$ ne s'annule pas sur $\mathbb{R}$. On note $S_0$ l'ensemble de toutes les solutions de $(E_0)$. Un professeur demande à un élève d'expliciter précisément l'ensemble $S_0$ au tableau. L'élève note alors : $S_0 = \{ t \mapsto ke^{-F(t)},\ k \in \mathbb{R} \}$ (fonctions de $\mathbb{R}$ dans $\mathbb{R}$). Cette égalité est notée $(\star)$ par la suite.
1. Le professeur demande à l'élève d'être plus précis et d'écrire $F$ en fonction de $a$ et de $b$. Qu'écrit l'élève ? Vous donnerez aussi $F'$ en fonction de $a$ et de $b$.
2. Nous cherchons à présent à démontrer ce théorème rigoureusement.
   - (a) Soit $y_0 \in S_0$ une solution de $(E_0)$. On introduit la fonction dérivable sur $\mathbb{R}$ : $z : t \mapsto y_0(t)e^{F(t)}$. Calculer la dérivée de $z$ sur $\mathbb{R}$. En déduire que $z$ est une fonction constante et conclure sur la forme de $y_0$.
   - (b) Quelle inclusion de l'égalité $(\star)$ venez-vous de démontrer ?
   - (c) Montrer l'autre inclusion de l'égalité $(\star)$.
3. Résoudre $(E_0)$ : $(t^4 + 1)y' + 2t^3y = 0$ dans $\mathbb{R}$.

## Cours 4 : développements limités (4 points)
Type : développements limités usuels et composés · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/8
Formules : $e^u = \sum \frac{u^k}{k!}$ ; $\cos u = 1 - \frac{u^2}2 + \frac{u^4}{24}$ ; $\sin u = u - \frac{u^3}6$ ; $\ln(1+u) = u - \frac{u^2}2 + \frac{u^3}3 - \frac{u^4}4$ ; $\sqrt{1+u} = 1 + \frac u2 - \frac{u^2}8 + \frac{u^3}{16} - \frac{5u^4}{128}$ ; $(1+u)^\alpha = 1 + \alpha u + \frac{\alpha(\alpha-1)}2u^2$ ; produit tronqué ; composition : poser $u$, calculer $u^2$ à l'ordre voulu ; $1 + \cos 2x = 2\cos^2 x$

Donner les développements limités au voisinage de 0 à l'ordre 3 de :
1. $f(x) = e^x$
2. $g(x) = \cos(x)$
3. $h(x) = \sin(x)$
4. $i(x) = \ln(1 + x)$
