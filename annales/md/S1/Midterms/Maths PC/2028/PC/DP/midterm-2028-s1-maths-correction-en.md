# Correction S1B1-DP exam — October 2023 (EN)

- Source : `raw/S1/Midterms/Maths PC/2028/PC/DP/midterm-2028-s1-maths-correction-en.pdf` (4 pages)
- Date réelle : octobre 2023 (dossier promo 2028). Version anglaise de `midterm-2028-s1-maths-correction-fr.md` (mêmes exercices, mêmes résultats ; Pierre s'appelle Peter). Sujet : `midterm-2028-s1-maths-subject-fr.md`.

## Exercise 1: cardinal numbers
Type : cardinal d'une union, partition · ECUE : DP · Niveau : maths-s1-dp/1
Formules : $F \cap G = \emptyset \Rightarrow \mathrm{Card}(F \cup G) = \mathrm{Card}F + \mathrm{Card}G$ ; $A = (A \setminus B) \sqcup (A \cap B)$ ; $\mathrm{Card}(A \cup B) = \mathrm{Card}A + \mathrm{Card}B - \mathrm{Card}(A \cap B)$

1. $F$, $G$ finite disjoint sets: $\mathrm{Card}(F \cup G) = \mathrm{Card}(F) + \mathrm{Card}(G)$.
2. $A$, $B$ subsets of a finite set $E$. (a) $A = (A \setminus B) \cup (A \cap B)$ (disjoint), so $\mathrm{Card}(A) = \mathrm{Card}(A \setminus B) + \mathrm{Card}(A \cap B)$. (b) $\mathrm{Card}(A \cup B) = \mathrm{Card}(A) + \mathrm{Card}(B) - \mathrm{Card}(A \cap B)$. (c) $A \cup B = (A \setminus B) \cup B$ (disjoint), then use (a).

## Exercise 2: podiums
Type : arrangements, combinaisons, complémentaire · ECUE : DP · Niveau : maths-s1-dp/5
Formules : classement de $p$ parmi $n$ (ordre) : $n(n-1)\dots(n-p+1)$ ; sans ordre : $\binom np$ ; « au moins A ou B » = total $-$ « ni A ni B » ; place imposée : multiplier par le nombre de places possibles

In a cycling race there are 20 competitors; the podium is the ranking of the best three. Peter and Jade are competitors.
1. Possible podiums: $20 \times 19 \times 18$.
2. Jade ranked first: $19 \times 18$.
3. Neither Peter nor Jade: $18 \times 17 \times 16$.
4. Peter but not Jade: $3 \times 18 \times 17$.
5. At least Jade or Peter (complement): $20 \times 19 \times 18 - 18 \times 17 \times 16$.
6. Same reward for the best three (no order): $\binom{20}3 = 3 \times 19 \times 20$.

## Exercise 3: counting
Type : formule de Vandermonde par double comptage · ECUE : DP · Niveau : maths-s1-dp/6
Formules : $\binom pi$ façons de choisir $i$ vertes, $\binom n{k-i}$ rouges ; somme sur les cas disjoints $i = 0..k$ ; Vandermonde $\sum_{i=0}^k \binom pi\binom n{k-i} = \binom{n+p}k$ ; $\binom{11}4 = 330$

An urn contains $p$ green and $n$ red balls; $k$ balls are picked simultaneously ($k \leqslant n$, $k \leqslant p$).
1. $\binom{n+p}k$ ways. 2. With $i$ green and $k - i$ red balls: $\binom pi\binom n{k-i}$. 3. Summing over $i$: $\sum_{i=0}^k \binom pi\binom n{k-i} = \binom{n+p}k$. 4. $\sum_{i=0}^4 \binom4i\binom7{4-i} = \binom{11}4 = 330$.

## Exercise 4: conditional probabilities
Type : probabilités totales et Bayes · ECUE : DP · Niveau : maths-s1-dp/10
Formules : probabilités totales : $P(M) = P(M \mid V)P(V) + P(M \mid \bar V)P(\bar V)$ ; Bayes : $P(V \mid M) = \frac{P(M \mid V)P(V)}{P(M)}$ ; $P(\bar V) = 1 - P(V)$

Support sessions: $P(S) = 0{,}1$, $P(V \mid S) = 0{,}8$, $P(V \mid \bar S) = 0{,}3$ ($V$: validates the S1 maths module).
$P(V) = 0{,}8 \times 0{,}1 + 0{,}3 \times 0{,}9 = \frac7{20}$ ; $P(S \mid V) = \frac{0{,}08}{0{,}35} = \frac8{35}$ ; $P(V) = 0{,}5p + 0{,}3 \geqslant 0{,}75 \iff p \geqslant 0{,}9$.

## Exercise 5: lecture questions
Type : linéarité de l'espérance, formule de König-Huygens · ECUE : DP · Niveau : maths-s1-dp/13
Formules : $E(X + Y) = E(X) + E(Y)$ ; $E(aX + b) = aE(X) + b$ ; $V(X) = E((X - E(X))^2) = E(X^2) - E(X)^2$ ; $(a - b)^2 = a^2 - 2ab + b^2$

$E(X + Y) = E(X) + E(Y)$, $E(aX + b) = aE(X) + b$, hence $\mathrm{Var}(X) = E\left((X - E(X))^2\right) = E(X^2) - (E(X))^2$.

## Exercise 6: random variables
Type : loi de Bernoulli, loi binomiale, espérance et variance · ECUE : DP · Niveau : maths-s1-dp/14
Formules : Bernoulli $\mathcal{B}(p)$ : $E = p$, $V = p(1-p)$ ; binomiale $\mathcal{B}(n,p)$ : $P(Y = k) = \binom nk p^k(1-p)^{n-k}$, $E = np$, $V = np(1-p)$ ; $E(G) = \sum x_iP(G = x_i)$ ; $V(G) = E(G^2) - E(G)^2$ (König-Huygens)

20-question MCQ, 1 point each, random answers, each correct with probability $\frac13$, independent.
1. $X_k \sim$ Bernoulli$\left(\frac13\right)$, $E(X_k) = \frac13$, $E(X_k^2) = \frac13$, $V(X_k) = \frac29$.
2. $Y = X_1 + \dots + X_{20} \sim \mathcal{B}\left(20, \frac13\right)$, $P(Y = i) = \binom{20}i\left(\frac13\right)^i\left(\frac23\right)^{20-i}$, $\sum_i P(Y = i) = \left(\frac13 + \frac23\right)^{20} = 1$, $E(Y) = \frac{20}3$, $V(Y) = \frac{40}9$.
