# QCM 2 (S2 PA) — lundi 5 février 2024

- Source : `raw/S2/MCQs/2028/Maths PA/PA-mcq-maths-2028-s2-02-fr.pdf` (scan d'une copie annotée, 3 pages)
- Date réelle : 5 février 2024 (S2-PA 2024, dossier promo 2028). Questions 11 à 20.
- Réponses : vérifiées à la main.

## Question 11
Type : coefficients binomiaux (symétrie) · ECUE : DP · Niveau : maths-s1-dp/4
Formules : $\binom np = \frac{n!}{p!(n-p)!}$ ; $\binom np = \binom n{n-p}$ ; $\binom np$ = nombre de parties à $p$ éléments d'un ensemble à $n$ éléments ; bijection $A \mapsto \bar A$

Soient $n \in \mathbb{N}$ et $p \in [\![0, n]\!]$. $\binom np$ est égal à a. $\frac{n!}{p!}$ ; b. $\frac{p!}{n!}$ ; c. $\frac{n!}{p!(n-p)!}$ ; d. $\frac{n!}{(n-p)!}$ ; e. Aucune des autres réponses.

Réponse : c.

## Question 12
Type : interpréter une formule de dénombrement · ECUE : DP · Niveau : maths-s1-dp/4
Formules : $\frac{n!}{(n-p)!} = A_n^p$ : tirage successif sans remise (ordre) ; $\binom np$ : tirage simultané ; $\binom{8}{3}\binom{8}{2}$ : 3 cartes d'une couleur et 2 d'une autre ; $\binom{7}{1}\binom{24}{3}$ : exactement 1 parmi 7, le reste parmi 24 (catégories disjointes)

Une urne contient 7 boules numérotées de 1 à 7. À quoi peut correspondre la réponse « $\binom74$ » ? a. Nombre de façons de tirer 4 boules avec remise ; b. sans remise (successivement) ; c. simultanément ; d. Rien de ce qui précède.

Réponse : c.

## Question 13
Type : dénombrement (p-listes, arrangements, anagrammes, parties) · ECUE : DP · Niveau : maths-s1-dp/3
Formules : $p$-listes (avec remise, ordre) : $n^p$ ; arrangements (sans remise, ordre) : $A_n^p = \frac{n!}{(n-p)!}$ ; permutations : $n!$ ; anagrammes avec lettres répétées : $\frac{n!}{k_1!k_2!\dots}$ ; nombre de parties d'un ensemble à $m$ éléments : $2^m$ ; principe multiplicatif

a. Le nombre d'anagrammes de « MATH » est 4 ; b. il est $4!$ ; c. Le nombre d'anagrammes de « ASSEZ » est 5 ; d. il est 60 ; e. Aucune des autres réponses.

Réponse : b et d.

## Question 14
Type : binôme de Newton et double comptage · ECUE : DP · Niveau : maths-s1-dp/6
Formules : $(a + b)^n = \sum_{k=0}^n \binom nk a^kb^{n-k}$ ; $a = 1$, $b = 3$ ; principe multiplicatif $4^n$ ; double comptage : compter le même ensemble de deux façons ; $\binom nk$ façons de choisir $k$ cases

Soient $n \in \mathbb{N}^*$ et $x$, $y$ deux réels non nuls. On a $(x + y)^n = \sum_{k=0}^n x^ky^{n-k}$. a. Vrai ; b. Faux.

Réponse : b (il manque $\binom nk$).

## Question 15
Type : coefficients binomiaux (symétrie) · ECUE : DP · Niveau : maths-s1-dp/6
Formules : $\binom np = \frac{n!}{p!(n-p)!}$ ; $\binom np = \binom n{n-p}$ ; $\binom np$ = nombre de parties à $p$ éléments d'un ensemble à $n$ éléments ; bijection $A \mapsto \bar A$

Soit $E$ un ensemble à 8 éléments. a. Dans $E$, il y a autant de sous-ensembles à 3 éléments que de sous-ensembles à 5 éléments ; b. le nombre de sous-ensembles à 3 éléments est $4 \times 5 \times 6 \times 7 \times 8$ ; c. il est $\binom83$ ; d. Aucune des autres réponses.

Réponse : a et c.

## Question 16
Type : formules de base des probabilités · ECUE : DP · Niveau : maths-s1-dp/7
Formules : $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ ; $P(\Omega) = 1$ ; $P(\emptyset) = 0$ ; $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$ ; indépendants $\iff P(A \cap B) = P(A)P(B)$ ; partition : deux à deux disjoints, union $= \Omega$ (non vides)

Soient $A$ et $B$ deux événements. a. Si $A$ et $B$ sont disjoints, $P(A \cup B) = P(A) \times P(B)$ ; b. Si $A$ et $B$ sont disjoints, $P(A \cup B) = P(A) + P(B)$ ; c. $P(A + B) = P(A) \cup P(B)$ ; d. $P(A \cup B) = P(A) + P(B) + P(A \cap B)$ ; e. Aucune des autres réponses.

Réponse : b.

## Question 17
Type : formules de base des probabilités · ECUE : DP · Niveau : maths-s1-dp/7
Formules : $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ ; $P(\Omega) = 1$ ; $P(\emptyset) = 0$ ; $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$ ; indépendants $\iff P(A \cap B) = P(A)P(B)$ ; partition : deux à deux disjoints, union $= \Omega$ (non vides)

On lance un dé à 6 faces, $\Omega = [\![1, 6]\!]$. On peut définir un espace probabilisé en posant : a. $P(\{1\}) = 0{,}3$ et $\forall k \in [\![2, 6]\!]$, $P(\{k\}) = 0{,}1$ ; b. $P(\{1\}) = 0{,}5$ et $P(\{k\}) = 0{,}1$ ; c. $P(\{1\}) = 0{,}3$ et $P(\{k\}) = \frac{0{,}7}4$ ; d. Aucune des autres réponses.

Réponse : b (la somme doit valoir 1 : a donne 0,8, c donne 1,175).

## Question 18
Type : formules de base des probabilités · ECUE : DP · Niveau : maths-s1-dp/7
Formules : $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ ; $P(\Omega) = 1$ ; $P(\emptyset) = 0$ ; $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$ ; indépendants $\iff P(A \cap B) = P(A)P(B)$ ; partition : deux à deux disjoints, union $= \Omega$ (non vides)

On lance un dé équilibré à 6 faces. La probabilité d'avoir un multiple de 3 est a. 2 ; b. $\frac13$ ; c. 3 ; d. $\frac12$ ; e. Aucune des autres réponses.

Réponse : b.

## Question 19
Type : image directe, image réciproque (lecture graphique) · ECUE : OBM · Niveau : maths-s1-obm/9
Formules : $f(A) = \{f(x), x \in A\}$ ; $f^{-1}(B) = \{x, f(x) \in B\}$ ; lire les valeurs prises (bornes ouvertes / fermées) ; $f(\mathbb{R})$ = ensemble des valeurs prises

Soit $f : \mathbb{R} \to \mathbb{R}$, $f(x) = |x|$. a. $f(\{1\}) = \{-1, 1\}$ ; b. $f(\{-1, 1\}) = \{1\}$ ; c. $f^{-1}([-3, -1]) = \emptyset$ ; d. $f^{-1}(\{0\}) = \emptyset$ ; e. Aucune des autres réponses.

Réponse : b et c.

## Question 20
Type : injectivité / surjectivité, restriction · ECUE : OBM · Niveau : maths-s1-obm/10
Formules : injective $\iff$ toute droite horizontale coupe le graphe au plus une fois ; surjective sur $F$ $\iff$ tout $y \in F$ est atteint ; $(x-2)^2 - 1 \geqslant -1$ ; restreindre le départ à $[2, +\infty[$ rend injective, l'arrivée à $[-1, +\infty[$ rend surjective

Soit $f : \mathbb{R} \to \mathbb{R}$, $f(x) = |x|$. a. injective, non surjective ; b. surjective, non injective ; c. bijective ; d. ni injective, ni surjective.

Réponse : d.
