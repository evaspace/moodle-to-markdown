# QCM 3 (S2 PA) — lundi 12 février 2024

- Source : `raw/S2/MCQs/2028/Maths PA/PA-mcq-maths-2028-s2-04-fr.pdf` (scan d'une copie annotée, 3 pages ; le fichier « 04 » contient le QCM 3)
- Date réelle : 12 février 2024 (S2-PA 2024, dossier promo 2028). Questions 11 à 20.
- Réponses : vérifiées à la main.

## Question 11
Type : formules de base des probabilités · ECUE : DP · Niveau : maths-s1-dp/7
Formules : $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ ; $P(\Omega) = 1$ ; $P(\emptyset) = 0$ ; $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$ ; indépendants $\iff P(A \cap B) = P(A)P(B)$ ; partition : deux à deux disjoints, union $= \Omega$ (non vides)

a. Si $A$ et $B$ sont disjoints, $P(A \cup B) = P(A) \times P(B)$ ; b. Si $A$ et $B$ sont disjoints, $P(A \cup B) = P(A) + P(B)$ ; c. $P(A + B) = P(A) \cup P(B)$ ; d. $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ ; e. Aucune des autres réponses.

Réponse : b et d.

## Question 12
Type : formules de base des probabilités · ECUE : DP · Niveau : maths-s1-dp/7
Formules : $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ ; $P(\Omega) = 1$ ; $P(\emptyset) = 0$ ; $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$ ; indépendants $\iff P(A \cap B) = P(A)P(B)$ ; partition : deux à deux disjoints, union $= \Omega$ (non vides)

Soit $A$ un événement. a. $0 < P(A) < 1$ ; b. $P(\Omega) = 1$ ; c. $P(\emptyset) = 0$ ; d. Aucune des autres réponses.

Réponse : b et c.

## Question 13
Type : équiprobabilité (deux dés) · ECUE : DP · Niveau : maths-s1-dp/7
Formules : $|\Omega| = 36$ ; « exactement un 6 » : $2 \times \frac16 \times \frac56 = \frac{10}{36}$ ; « au moins un 6 » $= 1 - P(\text{aucun}) = 1 - \left(\frac56\right)^2$

On lance deux dés équilibrés à 6 faces. La probabilité d'obtenir exactement un 6 est a. $\frac5{36}$ ; b. $\frac5{18}$ ; c. $\frac{11}{36}$ ; d. Aucune des autres réponses.

Réponse : b ($2 \times \frac16 \times \frac56$).

## Question 14
Type : équiprobabilité (deux dés) · ECUE : DP · Niveau : maths-s1-dp/7
Formules : $|\Omega| = 36$ ; « exactement un 6 » : $2 \times \frac16 \times \frac56 = \frac{10}{36}$ ; « au moins un 6 » $= 1 - P(\text{aucun}) = 1 - \left(\frac56\right)^2$

On lance deux dés équilibrés. La probabilité d'obtenir au moins un 6 est a. $\frac5{36}$ ; b. $\frac5{18}$ ; c. $\frac{11}{36}$ ; d. Aucune des autres réponses.

Réponse : c ($1 - \frac{25}{36}$).

## Question 15
Type : formules de base des probabilités · ECUE : DP · Niveau : maths-s1-dp/8
Formules : $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ ; $P(\Omega) = 1$ ; $P(\emptyset) = 0$ ; $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$ ; indépendants $\iff P(A \cap B) = P(A)P(B)$ ; partition : deux à deux disjoints, union $= \Omega$ (non vides)

$A$, $B$ de probabilités non nulles. a. $P(A \mid B) = \frac{P(A \cup B)}{P(B)}$ ; b. $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$ ; c. $\frac{P(A \cup B)}{P(A)}$ ; d. $\frac{P(A \cap B)}{P(A)}$ ; e. Aucune des autres réponses.

Réponse : b.

## Question 16
Type : indépendance et incompatibilité · ECUE : DP · Niveau : maths-s1-dp/11
Formules : indépendants $\iff P(A \cap B) = P(A)P(B) \iff P_B(A) = P(A)$ ; $P_B(A) = \frac{P(A \cap B)}{P(B)}$ ; incompatibles $\iff A \cap B = \emptyset$

$A$ et $B$ indépendants, $P(A) = \frac16$ et $P(B) = \frac23$. a. $P(A \cap B) = \frac56$ ; b. $P(A \cap B) = \frac19$ ; c. On ne peut pas savoir ; d. Aucune des autres réponses.

Réponse : b.

## Question 17
Type : formules de base des probabilités · ECUE : DP · Niveau : maths-s1-dp/8
Formules : $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ ; $P(\Omega) = 1$ ; $P(\emptyset) = 0$ ; $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$ ; indépendants $\iff P(A \cap B) = P(A)P(B)$ ; partition : deux à deux disjoints, union $= \Omega$ (non vides)

$A$, $B$ de probabilités non nulles. a. $P(A \mid B)P(B) = P(B \mid A)P(A)$ ; b. $P(A \mid B)P(A) = P(B \mid A)P(B)$ ; c. $P(A \mid B) = P(B)$ ; d. $P(A \mid B) = P(A)$ ; e. Aucune des autres réponses.

Réponse : a (d seulement si indépendants).

## Question 18
Type : interpréter une formule de dénombrement · ECUE : DP · Niveau : maths-s1-dp/2
Formules : $\frac{n!}{(n-p)!} = A_n^p$ : tirage successif sans remise (ordre) ; $\binom np$ : tirage simultané ; $\binom{8}{3}\binom{8}{2}$ : 3 cartes d'une couleur et 2 d'une autre ; $\binom{7}{1}\binom{24}{3}$ : exactement 1 parmi 7, le reste parmi 24 (catégories disjointes)

Une urne contient 7 boules numérotées. À quoi peut correspondre « $7^4$ » ? a. Tirer 4 boules avec remise ; b. sans remise ; c. simultanément ; d. Rien de ce qui précède.

Réponse : a.

## Question 19
Type : binôme de Newton et double comptage · ECUE : DP · Niveau : maths-s1-dp/6
Formules : $(a + b)^n = \sum_{k=0}^n \binom nk a^kb^{n-k}$ ; $a = 1$, $b = 3$ ; principe multiplicatif $4^n$ ; double comptage : compter le même ensemble de deux façons ; $\binom nk$ façons de choisir $k$ cases

$(x + y)^n = \sum_{k=0}^n \binom nk x^ky^k$. a. Vrai ; b. Faux.

Réponse : b (c'est $x^ky^{n-k}$).

## Question 20
Type : dénombrement (p-listes, arrangements, anagrammes, parties) · ECUE : DP · Niveau : maths-s1-dp/3
Formules : $p$-listes (avec remise, ordre) : $n^p$ ; arrangements (sans remise, ordre) : $A_n^p = \frac{n!}{(n-p)!}$ ; permutations : $n!$ ; anagrammes avec lettres répétées : $\frac{n!}{k_1!k_2!\dots}$ ; nombre de parties d'un ensemble à $m$ éléments : $2^m$ ; principe multiplicatif

a. Le nombre d'anagrammes de « TRAVAIL » est $7!$ ; b. il est $6!$ ; c. Le nombre d'anagrammes de « ASSEZ » est 5 ; d. il est $\frac{5!}2$ ; e. Aucune des autres réponses.

Réponse : d (« TRAVAIL » : $\frac{7!}{2!}$).
