# Examen S1B1-DP — octobre 2023 (sujet, FR)

- Source : `raw/S1/Midterms/Maths PC/2028/PC/DP/midterm-2028-s1-maths-subject-fr.pdf` (6 pages)
- Date réelle : octobre 2023 (dossier promo 2028, ECUE DP). Corrigés : `midterm-2028-s1-maths-correction-fr.md` (FR), `midterm-2028-s1-maths-correction-en.md` (EN).
- Durée : 2 heures. Barème sur 30 points ramené à 20. 6 exercices. Rigueur prise en compte, malus d'un point pour manque de propreté. Documents et calculatrices interdits.

## Exercice 1 : cardinal (3 points)
Type : cardinal d'une union, partition · ECUE : DP · Niveau : maths-s1-dp/1
Formules : $F \cap G = \emptyset \Rightarrow \mathrm{Card}(F \cup G) = \mathrm{Card}F + \mathrm{Card}G$ ; $A = (A \setminus B) \sqcup (A \cap B)$ ; $\mathrm{Card}(A \cup B) = \mathrm{Card}A + \mathrm{Card}B - \mathrm{Card}(A \cap B)$

1. Soient $F$ et $G$ deux ensembles finis et disjoints. Donner $\mathrm{Card}(F \cup G)$.
2. Soient $E$ un ensemble fini et $A$ et $B$ deux sous-ensembles de $E$ quelconques (non nécessairement disjoints).
   (a) En utilisant une partition de $A$, trouver une relation entre $\mathrm{Card}(A)$, $\mathrm{Card}(A \setminus B)$ et $\mathrm{Card}(A \cap B)$. Vous pouvez vous aider d'un dessin. N.B. : $A \setminus B = \{x \in E ; x \in A \wedge x \notin B\}$.
   (b) Donner $\mathrm{Card}(A \cup B)$.
   (c) En utilisant une partition de $A \cup B$ et la question 2.(a), démontrer le résultat précédent.

## Exercice 2 : podiums (7 points)
Type : arrangements, combinaisons, complémentaire · ECUE : DP · Niveau : maths-s1-dp/5
Formules : classement de $p$ parmi $n$ (ordre) : $n(n-1)\dots(n-p+1)$ ; sans ordre : $\binom np$ ; « au moins A ou B » = total $-$ « ni A ni B » ; place imposée : multiplier par le nombre de places possibles

Une course cycliste oppose 20 concurrents. Le podium est composé du classement des trois premiers arrivés. Pierre et Jade font partie des 20 concurrents. Vous justifierez brièvement vos réponses. Vous simplifierez vos résultats sans faire les calculs jusqu'au bout.
1. Combien y a-t-il de podiums possibles ?
2. Combien y a-t-il de podiums possibles dans lesquels Jade est première ?
3. Combien y a-t-il de podiums possibles sans Pierre ni Jade ?
4. Combien y a-t-il de podiums possibles dont Pierre fait partie mais pas Jade ?
5. Combien y a-t-il de podiums possibles dans lesquels il y a au moins Jade ou Pierre ?
6. L'organisateur souhaite récompenser, sans distinction, les trois premiers en leur offrant un vélo chacun. Combien y a-t-il de récompenses possibles ?

## Exercice 3 : dénombrement (5 points)
Type : formule de Vandermonde par double comptage · ECUE : DP · Niveau : maths-s1-dp/6
Formules : $\binom pi$ façons de choisir $i$ vertes, $\binom n{k-i}$ rouges ; somme sur les cas disjoints $i = 0..k$ ; Vandermonde $\sum_{i=0}^k \binom pi\binom n{k-i} = \binom{n+p}k$ ; $\binom{11}4 = 330$

Soit $(n, p) \in \mathbb{N}^2$. Une urne contient $p$ boules vertes et $n$ boules rouges indiscernables au toucher. Soit $k \in [\![0, n + p]\!]$ avec $k \leqslant n$ et $k \leqslant p$. On effectue un tirage simultané de $k$ boules de l'urne.
1. Combien y a-t-il de tirages possibles ?
2. Soit $i \in [\![0, k]\!]$. Combien y a-t-il de tirages (simultanés) ayant $i$ boules vertes et $k - i$ boules rouges ?
3. En déduire la formule $\displaystyle\sum_{i=0}^k \binom pi\binom n{k-i} = \binom{n+p}k$. Justifier proprement.
4. Application : calculer $\displaystyle\sum_{i=0}^4 \binom4i\binom7{4-i}$. Vous donnerez le résultat sous la forme d'un entier.

## Exercice 4 : probabilités conditionnelles (5 points)
Type : probabilités totales et Bayes · ECUE : DP · Niveau : maths-s1-dp/10
Formules : probabilités totales : $P(M) = P(M \mid V)P(V) + P(M \mid \bar V)P(\bar V)$ ; Bayes : $P(V \mid M) = \frac{P(M \mid V)P(V)}{P(M)}$ ; $P(\bar V) = 1 - P(V)$

Des cours de soutien en mathématiques sont proposés aux étudiants de S1 d'Epita. Pour la promotion actuelle, la probabilité qu'un élève vienne en soutien est de 10 %. Si un élève vient en soutien, la probabilité qu'il valide l'UE de maths du S1 est de 80 %, sinon, cette probabilité tombe à 30 %.
On notera $V$ l'événement « l'élève valide son UE de maths du S1 » et $S$ l'événement « l'élève vient en soutien ». Vous donnerez les résultats sous forme de fraction simplifiée. Ils doivent être justifiés proprement.
1. Traduire les informations données dans l'énoncé à l'aide de probabilités et des événements ci-dessus.
2. On choisit un élève au hasard dans la promo. Quelle est la probabilité qu'il valide l'UE de maths du S1 ?
3. On choisit un élève qui a validé. Quelle est la probabilité qu'il soit venu en soutien ?
4. On veut que la probabilité qu'un élève valide son UE de maths du S1 soit au moins de 75 %. Que faudrait-il prendre comme probabilité $p$ de venir en soutien ?

## Exercice 5 : cours (4 points)
Type : linéarité de l'espérance, formule de König-Huygens · ECUE : DP · Niveau : maths-s1-dp/13
Formules : $E(X + Y) = E(X) + E(Y)$ ; $E(aX + b) = aE(X) + b$ ; $V(X) = E((X - E(X))^2) = E(X^2) - E(X)^2$ ; $(a - b)^2 = a^2 - 2ab + b^2$

Soient $X$ et $Y$ deux variables aléatoires finies et $(a, b) \in \mathbb{R}^2$.
1. Rappeler les formules donnant $E(X + Y)$ et $E(aX + b)$.
2. En utilisant la question précédente, mise en évidence dans les calculs, montrer que $\mathrm{Var}(X) = E(X^2) - (E(X))^2$.

## Exercice 6 : variables aléatoires (6 points)
Type : loi de Bernoulli, loi binomiale, espérance et variance · ECUE : DP · Niveau : maths-s1-dp/14
Formules : Bernoulli $\mathcal{B}(p)$ : $E = p$, $V = p(1-p)$ ; binomiale $\mathcal{B}(n,p)$ : $P(Y = k) = \binom nk p^k(1-p)^{n-k}$, $E = np$, $V = np(1-p)$ ; $E(G) = \sum x_iP(G = x_i)$ ; $V(G) = E(G^2) - E(G)^2$ (König-Huygens)

Un étudiant passe un examen sous forme de QCM. L'examen contient 20 questions numérotées de 1 à 20. Chaque question est notée sur 1 point. La note totale de l'épreuve est donc une note sur 20. C'est un QCM sans point négatif, ni point intermédiaire : à chaque question, la note obtenue ne peut être que 0 ou 1.
L'étudiant s'est mal préparé à l'examen et choisit de répondre au hasard. Ses réponses sont indépendantes et, pour chaque question, il répond juste avec une probabilité de $\frac13$.
1. Soit $k \in [\![1, 20]\!]$. On considère la variable aléatoire $X_k$ égale à la note obtenue à la question $k$.
   (a) À $k$ fixé, donner la loi de $X_k$.
   (b) Calculer l'espérance et la variance de chaque $X_k$. Vous devez détailler tous vos calculs et ne surtout pas parachuter les résultats !
2. On considère maintenant la variable aléatoire $Y$ égale à la note finale obtenue par l'étudiant à l'épreuve.
   (a) Écrire $Y$ en fonction des $X_k$.
   (b) En justifiant proprement votre raisonnement, donner $P(Y = i)$ pour tout $i \in [\![0, 20]\!]$.
   (c) Vérifier que $\displaystyle\sum_{i=0}^{20} P(Y = i) = 1$.
   (d) En justifiant le calcul, donner l'espérance et la variance de $Y$.
