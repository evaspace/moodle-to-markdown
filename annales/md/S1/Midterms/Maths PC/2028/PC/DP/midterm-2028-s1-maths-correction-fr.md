# Correction examen S1B1-DP — octobre 2023

- Source : `raw/S1/Midterms/Maths PC/2028/PC/DP/midterm-2028-s1-maths-correction-fr.pdf` (3 pages)
- Date réelle : octobre 2023 (dossier promo 2028). Sujet : `midterm-2028-s1-maths-subject-fr.md` (énoncés repris en abrégé).

## Exercice 1 : cardinal
Type : cardinal d'une union, partition · ECUE : DP · Niveau : maths-s1-dp/1
Formules : $F \cap G = \emptyset \Rightarrow \mathrm{Card}(F \cup G) = \mathrm{Card}F + \mathrm{Card}G$ ; $A = (A \setminus B) \sqcup (A \cap B)$ ; $\mathrm{Card}(A \cup B) = \mathrm{Card}A + \mathrm{Card}B - \mathrm{Card}(A \cap B)$

1. $\mathrm{Card}(F \cup G) = \mathrm{Card}(F) + \mathrm{Card}(G)$.
2. (a) $A = (A \setminus B) \cup (A \cap B)$, union disjointe : $\mathrm{Card}(A) = \mathrm{Card}(A \setminus B) + \mathrm{Card}(A \cap B)$.
(b) $\mathrm{Card}(A \cup B) = \mathrm{Card}(A) + \mathrm{Card}(B) - \mathrm{Card}(A \cap B)$.
(c) $A \cup B = (A \setminus B) \cup B$, union disjointe : $\mathrm{Card}(A \cup B) = \mathrm{Card}(A \setminus B) + \mathrm{Card}(B) = \mathrm{Card}(A) - \mathrm{Card}(A \cap B) + \mathrm{Card}(B)$ par 2.(a).

## Exercice 2 : podiums
Type : arrangements, combinaisons, complémentaire · ECUE : DP · Niveau : maths-s1-dp/5
Formules : classement de $p$ parmi $n$ (ordre) : $n(n-1)\dots(n-p+1)$ ; sans ordre : $\binom np$ ; « au moins A ou B » = total $-$ « ni A ni B » ; place imposée : multiplier par le nombre de places possibles

1. 20 possibilités pour le 1er, 19 pour le 2e, 18 pour le 3e : $20 \times 19 \times 18$ podiums.
2. Jade première : $19 \times 18$.
3. Sans Pierre ni Jade : 18 concurrents, $18 \times 17 \times 16$.
4. Pas de Jade (19 concurrents dont Pierre) ; Pierre est 1er, 2e ou 3e (3 places), puis $18 \times 17$ pour les deux autres places : $3 \times 18 \times 17$.
5. Complémentaire de « ni Jade ni Pierre » : $20 \times 19 \times 18 - 18 \times 17 \times 16$.
6. Choisir 3 personnes parmi 20 sans ordre : $\binom{20}3 = \frac{20!}{3!\,17!} = 3 \times 19 \times 20$.

## Exercice 3 : dénombrement
Type : formule de Vandermonde par double comptage · ECUE : DP · Niveau : maths-s1-dp/6
Formules : $\binom pi$ façons de choisir $i$ vertes, $\binom n{k-i}$ rouges ; somme sur les cas disjoints $i = 0..k$ ; Vandermonde $\sum_{i=0}^k \binom pi\binom n{k-i} = \binom{n+p}k$ ; $\binom{11}4 = 330$

1. $\binom{n+p}k$ tirages possibles.
2. $\binom pi$ façons de prendre les $i$ vertes et $\binom n{k-i}$ les $k - i$ rouges : $\binom pi\binom n{k-i}$ tirages.
3. Un tirage de $k$ boules contient 0, 1, …, ou $k$ vertes (cas disjoints) : $\sum_{i=0}^k \binom pi\binom n{k-i}$ tirages. Comme il y en a $\binom{n+p}k$ (question 1), on obtient $\sum_{i=0}^k \binom pi\binom n{k-i} = \binom{n+p}k$.
4. $k = 4$, $p = 4$, $n = 7$ : $\sum_{i=0}^4 \binom4i\binom7{4-i} = \binom{11}4 = \frac{11!}{4!\,7!} = \frac{8 \times 9 \times 10 \times 11}{2 \times 3 \times 4} = 330$.

## Exercice 4 : probabilités conditionnelles
Type : probabilités totales et Bayes · ECUE : DP · Niveau : maths-s1-dp/10
Formules : probabilités totales : $P(M) = P(M \mid V)P(V) + P(M \mid \bar V)P(\bar V)$ ; Bayes : $P(V \mid M) = \frac{P(M \mid V)P(V)}{P(M)}$ ; $P(\bar V) = 1 - P(V)$

1. $P(S) = 0{,}1$, $P(V \mid S) = 0{,}8$ et $P(V \mid \bar S) = 0{,}3$.
2. $\{S, \bar S\}$ partition de $\Omega$ : $V = (V \cap S) \cup (V \cap \bar S)$ (disjointe).
$P(V) = P(V \mid S)P(S) + P(V \mid \bar S)P(\bar S) = 0{,}8 \times 0{,}1 + 0{,}3 \times 0{,}9 = 0{,}35 = \frac7{20}$.
3. $P(S \mid V) = \dfrac{P(V \mid S)P(S)}{P(V)} = \dfrac{0{,}08}{0{,}35} = \dfrac8{35}$.
4. $P(V) = 0{,}8p + 0{,}3(1 - p) = 0{,}5p + 0{,}3 \geqslant 0{,}75 \iff p \geqslant 0{,}9$.

## Exercice 5 : cours
Type : linéarité de l'espérance, formule de König-Huygens · ECUE : DP · Niveau : maths-s1-dp/13
Formules : $E(X + Y) = E(X) + E(Y)$ ; $E(aX + b) = aE(X) + b$ ; $V(X) = E((X - E(X))^2) = E(X^2) - E(X)^2$ ; $(a - b)^2 = a^2 - 2ab + b^2$

Renvoi au cours : $E(X + Y) = E(X) + E(Y)$, $E(aX + b) = aE(X) + b$ ; $\mathrm{Var}(X) = E\left((X - E(X))^2\right) = E(X^2) - 2E(X)E(X) + E(X)^2 = E(X^2) - E(X)^2$.

## Exercice 6 : variables aléatoires
Type : loi de Bernoulli, loi binomiale, espérance et variance · ECUE : DP · Niveau : maths-s1-dp/14
Formules : Bernoulli $\mathcal{B}(p)$ : $E = p$, $V = p(1-p)$ ; binomiale $\mathcal{B}(n,p)$ : $P(Y = k) = \binom nk p^k(1-p)^{n-k}$, $E = np$, $V = np(1-p)$ ; $E(G) = \sum x_iP(G = x_i)$ ; $V(G) = E(G^2) - E(G)^2$ (König-Huygens)

1. (a) $X_k(\Omega) = \{0, 1\}$, $P(X_k = 1) = \frac13$, $P(X_k = 0) = \frac23$ : Bernoulli de paramètre $\frac13$.
(b) $E(X_k) = 0 \times \frac23 + 1 \times \frac13 = \frac13$ ; $E(X_k^2) = 0^2 \times \frac23 + 1^2 \times \frac13 = \frac13$ ; $V(X_k) = \frac13 - \frac19 = \frac29$.
2. (a) $Y = X_1 + X_2 + \dots + X_{20}$ (somme des points ; les $X_k$ sont indépendantes).
(b) Somme de 20 Bernoulli indépendantes de paramètre $\frac13$ : $Y \sim \mathcal{B}\left(20, \frac13\right)$, $P(Y = i) = \binom{20}i\left(\frac13\right)^i\left(\frac23\right)^{20-i}$.
(c) Binôme de Newton : $\sum_{i=0}^{20} \binom{20}i\left(\frac13\right)^i\left(\frac23\right)^{20-i} = \left(\frac13 + \frac23\right)^{20} = 1$.
(d) $E(Y) = E(X_1) + \dots + E(X_{20}) = \frac{20}3$ ; indépendance : $V(Y) = V(X_1) + \dots + V(X_{20}) = 20 \times \frac29 = \frac{40}9$.
