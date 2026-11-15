# Examen S1B1-DP — octobre 2024 (sujet, FR)

- Source : `raw/S1/Midterms/Maths PC/2029/PC/DP/midterm-2029-s1-maths-subject-fr.pdf` (9 pages)
- Date réelle : octobre 2024 (dossier promo 2029, ECUE DP). Pas de corrigé.
- Durée : 2 heures. Barème sur 40 points divisé par 2. 6 exercices. Rigueur prise en compte, malus d'un point pour manque de propreté. Documents et calculatrices interdits.

## Exercice 1 : autour du cours et du TD (4 points)
Type : interpréter une formule de dénombrement · ECUE : DP · Niveau : maths-s1-dp/5
Formules : $\frac{n!}{(n-p)!} = A_n^p$ : tirage successif sans remise (ordre) ; $\binom np$ : tirage simultané ; $\binom{8}{3}\binom{8}{2}$ : 3 cartes d'une couleur et 2 d'une autre ; $\binom{7}{1}\binom{24}{3}$ : exactement 1 parmi 7, le reste parmi 24 (catégories disjointes)

Dans un jeu de 32 cartes, on tire 5 cartes. Proposer une situation simple afin que la réponse à la question « Quel est le nombre de tirages possibles ? » soit :
1. « Il y a $\dfrac{32!}{27!}$ tirages possibles ».
2. « Il y a $\dbinom{32}5$ tirages possibles ».
3. « Il y a $\dbinom83 \times \dbinom82$ tirages possibles ».
4. « Il y a $\dbinom71 \times \dbinom{24}3$ tirages possibles ».

## Exercice 2 : dénombrement 1 (6 points)
Type : p-listes, arrangements, complémentaire (digicode) · ECUE : DP · Niveau : maths-s1-dp/5
Formules : principe multiplicatif ; chiffres distincts : $10 \times 9 \times 8$ ; avec répétition : $10^3$ ; permutations de 3 chiffres connus : $3!$ ; « au moins un 4 » = total $-$ « aucun 4 » : $10^3 - 9^3$

Un digicode à l'entrée d'un immeuble est constitué d'un clavier de 13 touches marquées de 3 lettres A, B et C et des dix chiffres de 0 à 9. Un code est formé d'une lettre suivie de 3 chiffres.
N.B. : vous donnerez vos résultats sous la forme d'un nombre entier.
1. Combien y a-t-il de codes possibles dont les chiffres sont distincts ? Justifier brièvement.
2. Combien y a-t-il de codes possibles dont les chiffres peuvent se répéter ? Justifier brièvement.
3. Paul arrive devant l'immeuble mais a oublié le code. Il se souvient juste de la lettre et sait que les chiffres sont distincts et impairs. Combien a-t-il de possibilités pour trouver le code ? Justifier brièvement.
4. Le lendemain, Paul revient mais le code a changé, y compris la lettre. On lui a précisé uniquement que les trois chiffres du code sont 6, 2 et 9. Combien a-t-il de possibilités pour trouver le code ? Justifier brièvement.
5. Le surlendemain, Paul veut à nouveau rentrer chez lui mais le code a une nouvelle fois changé (y compris la lettre). Cette fois-ci, il sait juste que les chiffres du code peuvent se répéter et qu'il y a au moins une fois le chiffre 4. Combien a-t-il de possibilités pour trouver le code ? Justifier brièvement.

## Exercice 3 : dénombrement 2 (8,5 points)
Type : double comptage, $\binom np\binom pk = \binom nk\binom{n-k}{p-k}$ · ECUE : DP · Niveau : maths-s1-dp/6
Formules : choisir $p$ puis $k$ parmi eux = choisir les $k$ puis $p - k$ parmi les $n - k$ restants ; $\binom nk = \frac{n!}{k!(n-k)!}$ ; $\sum_{k=0}^p \binom pk = 2^p$, donc $S_p = \binom np 2^p$

1. Teddy s'ennuie et cherche à s'occuper. Il découpe un hexagone et un triangle en papier et colle le triangle dans l'hexagone (figure du sujet). Teddy trouve alors 9 jetons numérotés de 1 à 9 et se lance le défi de placer 5 jetons dans l'hexagone dont 2 dans le triangle. Pour cela, il décide de procéder de deux façons différentes :
   - Choix 1 : Teddy choisit 2 jetons à mettre dans le triangle puis il choisit 3 jetons à placer en dehors du triangle (mais dans l'hexagone !).
   - Choix 2 : Teddy choisit 5 jetons à placer dans l'hexagone et choisit parmi ceux-ci 2 jetons à placer dans le triangle.
   (a) Quel est le nombre $N_1$ de répartitions possibles si Teddy fait le choix 1 ? Vous donnerez votre résultat sous la forme de produits d'entiers.
   (b) Quel est le nombre $N_2$ de répartitions possibles si Teddy fait le choix 2 ? Vous donnerez votre résultat sous la forme de produits d'entiers.
   (c) Que constatez-vous ?
2. Généralisation : soient 3 entiers naturels $n$, $p$ et $k$ tels que $0 \leqslant k \leqslant p \leqslant n$. En vous inspirant des choix faits par Teddy, expliquez, sans calcul, la formule suivante : $\dbinom np\dbinom pk = \dbinom nk\dbinom{n-k}{p-k}$.
3. Redémontrer la formule précédente par le calcul.
4. Donner la valeur de : $S_p = \displaystyle\sum_{k=0}^p \binom nk\binom{n-k}{p-k}$.

## Exercice 4 : probabilités conditionnelles (6,5 points)
Type : probabilités totales et Bayes · ECUE : DP · Niveau : maths-s1-dp/10
Formules : probabilités totales : $P(M) = P(M \mid V)P(V) + P(M \mid \bar V)P(\bar V)$ ; Bayes : $P(V \mid M) = \frac{P(M \mid V)P(V)}{P(M)}$ ; $P(\bar V) = 1 - P(V)$

Dans une promotion d'élèves à Epita, on considère que seuls 40 % apprennent leur cours de maths. Pour ceux qui apprennent le cours, la probabilité de valider l'année est de 80 %. Pour les autres, celle-ci tombe à 20 %. On note $C$ l'événement « apprendre son cours » et $V$ l'événement « valider l'année ». Vous donnerez les résultats sous forme de fraction simplifiée.
1. Traduire l'énoncé en termes de probabilités.
2. On choisit un élève au hasard, quelle est sa probabilité de valider ?
3. On choisit un élève qui valide l'année, au hasard. Quelle est la probabilité qu'il ait appris son cours ?
4. Quelle proportion minimale $p$ d'élèves qui apprennent leur cours faudrait-il pour que 60 % de la promotion valide ?

## Exercice 5 : cours (6 points)
Type : démonstration de cours ($E(aX+b)$, $V(aX+b)$) · ECUE : DP · Niveau : maths-s1-dp/13
Formules : $E(X) = \sum x_iP(X = x_i)$ ; $V(X) = \sum (x_i - E(X))^2P(X = x_i)$ ; $E(aX + b) = aE(X) + b$ ; $V(aX + b) = a^2V(X)$ ; $\sum P(X = x_i) = 1$

Soient $X$ une variable aléatoire finie telle que $X(\Omega) = \{x_1, x_2, \dots, x_n\}$ et $(a, b) \in \mathbb{R}^2$.
1. Rappeler les formules donnant l'espérance et la variance de $X$, respectivement notées $E(X)$ et $\mathrm{Var}(X)$.
2. Exprimer $E(aX + b)$ en fonction de $a$, $b$ et $E(X)$. Démontrer cette formule.
3. Exprimer $\mathrm{Var}(aX + b)$ en fonction de $a$, $b$ et $\mathrm{Var}(X)$. Démontrer cette formule.

## Exercice 6 : variables aléatoires (9 points)
Type : loi d'une variable, Bernoulli, binomiale (somme d'indépendantes) · ECUE : DP · Niveau : maths-s1-dp/14
Formules : $P(X = x) = \frac{\text{nb de boules } x}{\text{nb total}}$ ; $E(X) = \sum xP(X = x)$ ; $V = E(X^2) - E(X)^2$ ; Bernoulli $E = p$, $V = p(1-p)$ ; somme de $n$ Bernoulli indépendantes de paramètre $p$ : $\mathcal{B}(n, p)$, $E = np$, $V = np(1-p)$ ; binôme pour $\sum P = 1$

Dans une urne, il y a quatre boules, indiscernables au toucher, numérotées 0, 1, 1 et 2. On tire au hasard successivement et avec remise 20 boules de l'urne. Les tirages sont indépendants.
N.B. : tous vos résultats seront donnés sous la forme d'une fraction simplifiée.
1. Soit $k \in [\![1, 20]\!]$ fixé. On note $X_k$ la variable aléatoire égale au numéro de la boule obtenue au $k$-ième tirage.
   (a) Donner la loi de chaque $X_k$.
   (b) Calculer l'espérance de $X_k$ (vous détaillerez vos calculs).
   (c) Calculer la variance de $X_k$ (vous détaillerez vos calculs).
2. Pour chaque tirage, on gagne un euro si la boule tirée porte le numéro 0 ou 1, sinon on ne gagne rien. On considère $Y_k$ la variable aléatoire égale au gain obtenu au $k$-ième tirage ($k$ fixé).
   (a) Donner la loi de $Y_k$. Justifier.
   (b) Donner son espérance et sa variance.
3. Soit $Z$ la variable aléatoire égale au gain obtenu sur les 20 tirages.
   (a) Écrire $Z$ en fonction des $Y_k$ en expliquant brièvement.
   (b) En déduire, pour tout $i \in Z(\Omega)$, $P(Z = i)$. Justifier.
   (c) Vérifier que $\displaystyle\sum_{i=0}^{20} P(Z = i) = 1$.
   (d) Calculer $E(Z)$ et $\mathrm{Var}(Z)$ en justifiant.
