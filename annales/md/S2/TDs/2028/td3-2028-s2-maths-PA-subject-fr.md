# Contrôle de cours EFDP (S2 PA) — lundi 19 février 2024 (sujet, FR)

- Source : `raw/S2/TDs/2028/td3-2028-s2-maths-PA-subject-fr.pdf` (scan d'une copie annotée, 3 pages)
- Date réelle : 19 février 2024 (S2 PA, dossier promo 2028). Les réponses manuscrites de la copie ne sont pas reprises.
- Durée : 1 heure. Barème sur 30, ramené à 20.

## Cours 1 : ensembles (4 points)
Type : ensembles (appartenance, inclusion, union, intersection, produit, complémentaire) · ECUE : OBM · Niveau : maths-s1-obm/8
Formules : $x \in A$ ; $A \subset B$ ; $A \cup B$, $A \cap B$ ; $A \times B = \{(a, b), a \in A, b \in B\}$ ; complémentaire $\bar B = E \setminus B$ ; $B = [\![0, 7]\!]$

On considère les ensembles $A = \{x \in \mathbb{R},\ -2 < x \leqslant 5\}$ et $B = \{n \in \mathbb{N},\ n < 13\}$.
1. De quel ensemble commun $A$ et $B$ sont-ils deux sous-ensembles ?
2. Dans chacune des phrases suivantes, remplacer les pointillés afin de la rendre vraie (remplacer les pointillés par $\emptyset$ est interdit). Exemple : pour $\dots \in B$, on peut remplacer les pointillés par 2 car $2 \in B$.
   a) $\dots \subset A$ ; b) $\dots \notin A \cup B$ ; c) $\dots \subset A \cup B$ ; d) $\dots \in A \cap B$ ; e) $\dots \in A \times B$.
3. $A$ et $B$ sont-ils de cardinal fini ? Si oui, préciser le cardinal de l'ensemble.

## Cours 2 : ensembles et fonctions - partie 1 (5,5 points)
Type : injectivité, surjectivité, image directe et réciproque · ECUE : OBM · Niveau : maths-s1-obm/9
Formules : injective : $f(x) = f(y) \Rightarrow x = y$ (contre-exemple $f(1) = f(2)$) ; surjective : $\forall y, \exists x, f(x) = y$ ; $f(A) = \{f(x), x \in A\}$ ; $f^{-1}(B) = \{x, f(x) \in B\}$ (peut être vide)

Soient $E$ et $F$ deux ensembles et une fonction $f : E \to F$.
1. Soit $A \subset E$. Donner la définition mathématique de $f(A)$.
2. Soit $B \subset F$. Donner la définition mathématique de $f^{-1}(B)$.
3. On suppose dans cette question que $E = \{a,b,c,d\}$ et $F = [\![1,5]\!]$. Dessiner (patates) une fonction $f$ qui vérifie à la fois $f(\{b,c\}) = \{2,3\}$ et $f^{-1}(\{2\}) = \{a,b\}$.
4. On suppose dans cette question que $E = F = \mathbb{R}$ et $f : x \mapsto x^2$.
   - (a) Donner $f(\{-4, 2\})$ et $f([-3, 1])$.
   - (b) Donner $f^{-1}(\{4\})$ et $f^{-1}([0, 2])$.

## Cours 3 : ensembles et fonctions - partie 2 (5 points)
Type : injectivité, surjectivité, image directe et réciproque · ECUE : OBM · Niveau : maths-s1-obm/10
Formules : injective : $f(x) = f(y) \Rightarrow x = y$ (contre-exemple $f(1) = f(2)$) ; surjective : $\forall y, \exists x, f(x) = y$ ; $f(A) = \{f(x), x \in A\}$ ; $f^{-1}(B) = \{x, f(x) \in B\}$ (peut être vide)

Soient $E$ et $F$ deux ensembles et une fonction $f : E \to F$.
1. Donner la définition mathématique de : « $f$ est injective de $E$ vers $F$ ».
2. Donner la définition mathématique de : « $f$ est surjective de $E$ vers $F$ ».
3. Supposons $E = [\![1,4]\!]$ et $F = [\![1,3]\!]$. Est-il possible de définir une fonction $f$ surjective de $E$ vers $F$ dans ce cas-là ? Si oui, dessiner (patates) une de ces fonctions.
4. Supposons $E = [\![1,4]\!]$ et $F = [\![1,3]\!]$. Est-il possible de définir une fonction $f$ injective de $E$ vers $F$ dans ce cas-là ? Si oui, dessiner (patates) une de ces fonctions.

## Cours 4 : dénombrement 1 (6 points)
Type : dénombrement de mains de cartes · ECUE : DP · Niveau : maths-s1-dp/4
Formules : $|\Omega| = \binom{32}5$ ; « au moins un » : complémentaire $P(A) = 1 - P(\bar A)$ ; $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ ; principe multiplicatif (choisir chaque catégorie séparément) ; équiprobabilité $P = \frac{|A|}{|\Omega|}$

Dans un jeu classique de 32 cartes, on tire 5 cartes. Les calculs ne sont pas à faire jusqu'au bout. Si la réponse est une combinaison ou un arrangement, donner son expression avec les factorielles.
1. Si le tirage est successif et sans remise, le nombre de tirages possibles est $\dots$
2. Si le tirage est simultané, le nombre de tirages possibles est $\dots$
3. Si le tirage est successif et avec remise, le nombre de tirages possibles est $\dots$
4. Si le tirage est simultané et qu'on obtient la dame de cœur, le nombre de tirages possibles est $\dots$
5. Le tirage des 5 cartes est fait. On a obtenu un 7, deux 9 et deux 8. Combien peut-on écrire de nombres (à 5 chiffres) avec les chiffres obtenus à ce tirage ? Justifier brièvement. Exemple : on peut obtenir le nombre 79988.

## Cours 5 : dénombrement 2 (5,5 points)
Type : coefficients binomiaux (symétrie) · ECUE : DP · Niveau : maths-s1-dp/6
Formules : $\binom np = \frac{n!}{p!(n-p)!}$ ; $\binom np = \binom n{n-p}$ ; $\binom np$ = nombre de parties à $p$ éléments d'un ensemble à $n$ éléments ; bijection $A \mapsto \bar A$

Soient $n \in \mathbb{N}^*$, $k \in [\![0,n]\!]$ et $E$ un ensemble tel que $\mathrm{Card}(E) = n$.
1. Donner l'expression de $\binom nk$. Que compte-t-il dans $E$ ?
2. Comparer, par le calcul, $\binom nk$ et $\binom n{n-k}$.
3. En utilisant un raisonnement de dénombrement, expliquer la formule que vous avez trouvée à la question précédente.

## Cours 6 : variable aléatoire (4 points)
Type : loi d'une variable aléatoire finie, espérance, variance · ECUE : DP · Niveau : maths-s1-dp/12
Formules : $\sum_k P(X = k) = 1$ ; $E(X) = \sum_k kP(X = k)$ ; $V(X) = E\big((X - E(X))^2\big) = \sum_k (k - E(X))^2P(X = k)$ ; König-Huygens : $V(X) = E(X^2) - E(X)^2$, $E(X^2) = \sum_k k^2P(X = k)$

Soit $X$ une variable aléatoire prenant les valeurs 0, 1 et 2 telle que $P(X = 0) = \dfrac12$ et $P(X = 1) = \dfrac13$.
1. Calculer $P(X = 2)$.
2. Calculer l'espérance de $X$. Vous rappellerez avant la formule.
3. Donner deux formules permettant de calculer la variance de $X$.
