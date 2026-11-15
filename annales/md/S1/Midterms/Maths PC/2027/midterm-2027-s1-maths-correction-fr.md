# Correction du contrôle S1 — novembre 2022

- Source : `raw/S1/Midterms/Maths PC/2027/midterm-2027-s1-maths-correction-fr.pdf` (5 pages)
- Date réelle : novembre 2022 (dossier promo 2027). Sujet : `midterm-2027-s1-maths-subject.md`.

## Exercice 1 : intégrales
Type : primitive $u'/u^n$, IPP trigonométrique, changement de variable racine vers arctan · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/13
Formules : $\int \frac{u'}{u^n} = \frac{u^{1-n}}{1-n}$ ($n \neq 1$) ; IPP avec $v' = \sin(2x)$, $v = -\frac{\cos(2x)}2$ ; $\int \cos(2x) = \frac{\sin(2x)}2$ ; $t = \sqrt{x+2} \Rightarrow x = t^2 - 2$, $dx = 2t\,dt$ ; $\int \frac{dt}{1+t^2} = \arctan t$ ; $\arctan\sqrt3 = \frac\pi3$, $\arctan 1 = \frac\pi4$

1. $I = \dfrac12\displaystyle\int_0^1 \frac{4x^3 + 2}{(x^4 + 2x + 1)^3}\,dx$ : forme $\frac{u'}{u^3} = u'u^{-3}$, primitive $\frac{u^{-3+1}}{-3+1}$.
$I = \dfrac12\left[-\dfrac{1}{2(x^4 + 2x + 1)^2}\right]_0^1 = \dfrac12\left(-\dfrac1{2 \times 4^2} + \dfrac12\right) = -\dfrac1{64} + \dfrac14 = \dfrac{15}{64}$.
2. $u(x) = 2x + 1$, $v'(x) = \sin(2x)$, $u'(x) = 2$, $v(x) = -\frac{\cos(2x)}2$ :
$J = \left[-\dfrac{2x + 1}2\cos(2x)\right]_0^{\pi/4} + \displaystyle\int_0^{\pi/4} \cos(2x)\,dx = \frac12 + \left[\frac{\sin(2x)}2\right]_0^{\pi/4} = \frac12 + \frac12 = 1$.
3. $t = \sqrt{x + 2} \iff x = t^2 - 2$, $dx = 2t\,dt$ ; $x = -1 \to t = 1$, $x = 1 \to t = \sqrt3$.
$K = \displaystyle\int_1^{\sqrt3} \frac{2t\,dt}{(t^2 - 2 + 3)t} = \int_1^{\sqrt3} \frac{2\,dt}{t^2 + 1} = [2\arctan t]_1^{\sqrt3} = \frac{2\pi}3 - \frac{2\pi}4 = \frac\pi6$.

## Exercice 2 : ensembles et fonctions
Type : image directe et réciproque, injectivité, surjectivité, composée · ECUE : OBM · Niveau : maths-s1-obm/10
Formules : $f(A) = \{y \in F, \exists x \in A, y = f(x)\}$ ; $f^{-1}(B) = \{x \in E, f(x) \in B\}$ ; injective : $f(x) = f(x') \Rightarrow x = x'$ ; surjective : $\forall y, \exists x, y = f(x)$ ; $g \circ f$ injective si $f$, $g$ injectives ; surjective si $f$, $g$ surjectives

1. $f(A) = \{f(x), x \in A\} = \{y \in F, \exists x \in A, y = f(x)\}$ et $f^{-1}(B) = \{x \in E, f(x) \in B\}$.
2. $f([\![1,4]\!]) = \{10, 11, 13\}$, $f(\{3\}) = \{11\}$, $f^{-1}(\{10, 11\}) = \{1, 2, 3\}$ et $f^{-1}(\{12\}) = \emptyset$.
3. (a) Graphe en V de sommet $(0, 1)$.
(b) $g(1) = g(-1) = 2$ et $1 \neq -1$ : $g$ n'est pas injective. Avec $I_1 = \mathbb{R}^+$ et $J_1 = \mathbb{R}$, $g$ est injective (continue et strictement croissante).
(c) $0 = g(x)$ n'a pas de solution : 0 n'a pas d'antécédent, $g$ n'est pas surjective. Avec $I_2 = \mathbb{R}$ et $J_2 = [1, +\infty[$, $g$ est surjective ($\forall x$, $g(x) \geqslant 1$).
4. (a) $h = g \circ f : E \to G$.
(b) Soit $(x, x') \in E^2$ tel que $g(f(x)) = g(f(x'))$. $g$ injective donne $f(x) = f(x')$, puis $f$ injective donne $x = x'$.
(c) Soit $y \in G$. $g$ surjective : $\exists z \in F$, $y = g(z)$. $f$ surjective : $\exists x \in E$, $z = f(x)$. Donc $y = g(f(x))$ : $g \circ f$ surjective.

## Exercice 3 : logique et relations
Type : propriétés d'une relation, négation, contraposée · ECUE : OBM · Niveau : maths-s1-obm/11
Formules : réflexive $\forall x, x\mathcal Rx$ ; antisymétrique $x\mathcal Ry \wedge y\mathcal Rx \Rightarrow x = y$ ; transitive ; négation de $\forall(P \Rightarrow Q)$ : $\exists(P \wedge \neg Q)$ ; contraposée de $P \Rightarrow Q$ : $\neg Q \Rightarrow \neg P$ ; $\neg(A \wedge B) = \neg A \vee \neg B$ ; ordre = réflexive + antisymétrique + transitive

1. Réflexive : $\forall x \in E, x\,\mathcal{R}\,x$. Négation : $\exists x \in E, x\,\cancel{\mathcal{R}}\,x$.
2. Antisymétrique : $\forall (x,y) \in E^2, x\,\mathcal{R}\,y$ et $y\,\mathcal{R}\,x \implies x = y$. Négation : $\exists (x,y) \in E^2$ tel que $x\,\mathcal{R}\,y$ et $y\,\mathcal{R}\,x$ et $x \neq y$.
3. Transitive : $\forall (x,y,z) \in E^3, x\,\mathcal{R}\,y$ et $y\,\mathcal{R}\,z \implies x\,\mathcal{R}\,z$. Contraposée : $\forall (x,y,z) \in E^3, x\,\cancel{\mathcal{R}}\,z \implies x\,\cancel{\mathcal{R}}\,y$ ou $y\,\cancel{\mathcal{R}}\,z$.
4. Dans $\mathbb{R}$, $\leqslant$ est réflexive, antisymétrique et transitive : c'est une relation d'ordre.

## Exercice 4 : dénombrement
Type : combinaisons et arrangements avec contraintes · ECUE : DP · Niveau : maths-s1-dp/5
Formules : groupe sans ordre : $\binom nk$ ; postes distincts : principe multiplicatif $n(n-1)\dots$ ; « exactement $a$ de type 1 et $b$ de type 2 » : $\binom{n_1}a\binom{n_2}b$ ; « au moins » : somme des cas disjoints ; élément imposé : choisir parmi les restants ; disjonction de cas

1. (a) 3 élèves parmi 20 : $\binom{20}3$ comités.
(b) $\binom{12}2$ façons de choisir les deux garçons et $\binom81$ la fille : $\binom{12}2 \times 8$ comités.
(c) « Au moins deux filles » = exactement deux ou exactement trois : $\binom82\binom{12}1 + \binom83$.
(d) Il reste un élève à choisir parmi 18 : $\binom{18}1 = 18$ comités.
2. (a) 20 choix pour le chef, 19 pour le sous-chef, puis 2 assistants parmi 18 : $20 \times 19 \times \binom{18}2$.
(b) 8 choix pour la chef, 12 pour le sous-chef, puis 7 pour l'assistante et 11 pour l'assistant : $8 \times 12 \times 7 \times 11$.
(c) Marie chef : 19 choix de sous-chef et $\binom{18}2$ pour les assistants : $19 \times \binom{18}2$.
(d) Si Pierre est sous-chef : $\binom{18}2$ choix d'assistants. Sinon : 18 choix de sous-chef (ni Marie ni Pierre), Pierre est assistant et l'autre assistant est 1 parmi 17. Total : $\binom{18}2 + 18 \times 17$.

## Exercice 5 : variables aléatoires
Type : Bernoulli, binomiale, loi d'un rang d'apparition · ECUE : DP · Niveau : maths-s1-dp/14
Formules : Bernoulli $E = p$, $V = p(1-p)$ ; binomiale (tirages avec remise) $P(Y = k) = \binom nk p^k(1-p)^{n-k}$, $E = np$, $V = np(1-p)$ ; tirages sans remise : produit de probabilités conditionnelles ; $E(Z) = \sum kP(Z = k)$ ; $V = E(Z^2) - E(Z)^2$

1. On tire une boule ; $X = 1$ si elle est verte, 0 sinon. $P(X = 1) = \frac25$, $P(X = 0) = \frac35$ : Bernoulli de paramètre $p = \frac25$, $E(X) = \frac25$, $V(X) = p(1-p) = \frac6{25}$.
2. On tire successivement 5 boules avec remise ; $Y$ = nombre de boules vertes. $Y(\Omega) = [\![0,5]\!]$, $P(Y = k) = \binom5k\left(\frac25\right)^k\left(\frac35\right)^{5-k}$. $E(Y) = np = 2$, $V(Y) = np(1-p) = \frac65$.
3. (a) La première blanche sort au plus tard au 3e tirage (seulement 2 vertes) : $Z(\Omega) = \{1, 2, 3\}$.
(b) $P(Z = 1) = \frac35$ ; $P(Z = 2) = \frac25 \times \frac34 = \frac3{10}$ ; $P(Z = 3) = \frac25 \times \frac14 \times \frac33 = \frac1{10}$.
(c) $E(Z) = 1 \times \frac6{10} + 2 \times \frac3{10} + 3 \times \frac1{10} = \frac{15}{10} = \frac32$.
(d) $E(Z^2) = \frac6{10} + 4 \times \frac3{10} + 9 \times \frac1{10} = \frac{27}{10}$, $V(Z) = E(Z^2) - E(Z)^2 = \frac{27}{10} - \frac94 = \frac9{20}$.

## Exercice 6 : probabilités conditionnelles
Type : probabilités totales et Bayes · ECUE : DP · Niveau : maths-s1-dp/10
Formules : probabilités totales : $P(M) = P(M \mid V)P(V) + P(M \mid \bar V)P(\bar V)$ ; Bayes : $P(V \mid M) = \frac{P(M \mid V)P(V)}{P(M)}$ ; $P(\bar V) = 1 - P(V)$

1. $A$ : « la sucette provient de A », $B$ : « de B », $C$ : « au citron ». $\{A, B\}$ partition : $C = (C \cap A) \cup (C \cap B)$, disjointe.
$P(C) = P(C \mid A)P(A) + P(C \mid B)P(B) = \frac{10}{40} \times \frac12 + \frac{25}{40} \times \frac12 = \frac18 + \frac5{16} = \frac7{16}$.
2. $P(A \mid C) = \dfrac{P(C \mid A)P(A)}{P(C)} = \dfrac{1/8}{7/16} = \dfrac27$.

## Exercice 7 : une démonstration
Type : démonstration de cours ($E(aX+b)$) · ECUE : DP · Niveau : maths-s1-dp/13
Formules : $E(Y) = \sum_i y_iP(Y = y_i)$ ; $P(aX + b = ax_i + b) = P(X = x_i)$ ; $\sum_i P(X = x_i) = 1$ ; linéarité de $\sum$

« Voir cours » : $E(Y) = \sum_{i=1}^n (ax_i + b)P(X = x_i) = a\sum x_iP(X = x_i) + b\sum P(X = x_i) = aE(X) + b$.

## Exercice 8 : exercice original
Type : binôme de Newton et double comptage · ECUE : DP · Niveau : maths-s1-dp/6
Formules : $(a + b)^n = \sum_{k=0}^n \binom nk a^kb^{n-k}$ ; $a = 1$, $b = 3$ ; principe multiplicatif $4^n$ ; double comptage : compter le même ensemble de deux façons ; $\binom nk$ façons de choisir $k$ cases

1. Pour $n \in \mathbb{N}$ et $(a,b) \in \mathbb{R}^2$ : $(a + b)^n = \sum_{k=0}^n \binom nk a^kb^{n-k}$.
2. Avec $a = 1$, $b = 3$ : $4^n = (1 + 3)^n = \sum_{k=0}^n \binom nk 1^k3^{n-k} = \sum_{k=0}^n \binom nk 3^{n-k}$.
3. (a) On colorie les cases une par une, 4 couleurs possibles pour chacune : $4 \times 4 \times \dots \times 4 = 4^n$.
(b) Soit $k \in [\![0, n]\!]$. On choisit les $k$ cases coloriées en vert : $\binom nk$ façons. Les $n - k$ autres sont coloriées en bleu, rouge ou jaune : $3^{n-k}$ façons. Au total $\sum_{k=0}^n \binom nk 3^{n-k}$.
(c) On retrouve la formule du 2.
