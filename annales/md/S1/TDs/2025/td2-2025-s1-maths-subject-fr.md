# Contrôle TD 2 (S1) — distanciel, fin 2020 (sujet, FR)

- Source : `raw/S1/TDs/2025/td2-2025-s1-maths-subject-fr.pdf` (2 pages, mise en page Word)
- Date réelle : S1 2020-2021 (dossier promo 2025), date exacte non indiquée. Pas de corrigé ; réponses du QCM vérifiées à la main.

## Question de cours 1
Type : loi binomiale (QCM) · ECUE : DP · Niveau : maths-s1-dp/14
Formules : $\mathcal{B}(n, p)$ : $P(Y = k) = \binom nk p^k(1-p)^{n-k}$, $E = np$, $V = np(1-p)$ ; $P(Y > 1) = 1 - P(Y = 0) - P(Y = 1)$

Chaque réponse juste cochée rapporte des points, chaque réponse fausse cochée enlève des points. La note globale de la question QCM ne peut pas être négative.
On lance 5 dés équilibrés à 10 faces numérotées de 1 à 10. On gagne 1 point à chaque fois que le résultat d'un dé est inférieur ou égal à 2. On appelle $Y$ la variable aléatoire qui donne le score total obtenu, sachant que $Y$ suit une loi binomiale.
a) $P(Y = 2) = \dfrac{4^4}{2 \times 5^4}$ ; b) $V(Y) = \dfrac45$ ; c) $E(Y) = 2$ ; d) $P(Y > 1) = \dfrac{5^5 - 5 \times 2^8}{5^5}$.

Réponse : a et b ($Y \sim \mathcal{B}(5, \frac15)$ ; $E(Y) = 1$ ; $P(Y > 1) = \frac{5^5 - 9 \times 2^8}{5^5}$).

## Question de cours 2
Type : divisibilité, PGCD, Bézout, Gauss, Fermat (QCM) · ECUE : HP (arithmétique)
Formules : $a \mid b$ et $a \mid c \Rightarrow a \mid b - c$ ; $au + cv = d \Rightarrow (a \wedge c) \mid d$ ; Fermat $p \nmid a \Rightarrow a^{p-1} \equiv 1\,[p]$ ; $\mathrm{pgcd}$ = produit des facteurs communs à la plus petite puissance ; Gauss exige $a \wedge b = 1$

On considère trois entiers : $a = 2^2 \times 7 \times 12^5$, $b = 2 \times 7^2 \times 11^7$ et $c \in \mathbb{N}^*$.
a) $12 \mid (a - c) \implies 12 \mid c$ ; b) $\exists (u, v) \in \mathbb{Z}^2, au + cv = 3 \implies a \wedge c = 3$ ; c) $a^{10} \equiv 1\,[11]$ ; d) $a \wedge b = 2^2 \times 7^2$ ; e) $15 \mid ac \implies 15 \mid c$.

Réponse : a et c ($a = 2^{12} \times 3^5 \times 7$, $a \wedge b = 14$ ; b : on a seulement $a \wedge c \mid 3$ ; e : $a \wedge 15 = 3 \neq 1$).

## Exercice 1 : probabilités
Type : probabilités totales et Bayes · ECUE : DP · Niveau : maths-s1-dp/10
Formules : probabilités totales : $P(M) = P(M \mid V)P(V) + P(M \mid \bar V)P(\bar V)$ ; Bayes : $P(V \mid M) = \frac{P(M \mid V)P(V)}{P(M)}$ ; $P(\bar V) = 1 - P(V)$

On dispose d'une urne contenant 5 boules indiscernables au toucher : 2 vertes et 3 rouges. On dispose aussi d'un dé équilibré à 6 faces : 4 faces rouges et 2 faces vertes.
La règle du jeu est la suivante : au début du jeu on tire une boule au hasard pour déterminer la couleur gagnante. Si la boule tirée est verte, tout au long du jeu, on gagne un point à chaque lancer de dé où l'on obtient une face verte ; si la boule tirée est rouge, tout au long du jeu, on gagne un point à chaque lancer de dé où l'on obtient une face rouge.
1. Déterminer la probabilité de marquer un point lors du premier lancer de dé.
2. On suppose qu'on lance le dé 6 fois et que l'on gagne 6 points. Quelle est la probabilité d'avoir tiré une boule verte ?
Consigne : exprimer vos résultats (a) par une formule utilisant des probabilités conditionnelles ; (b) par une fraction simplifiée.

## Exercice 2 : arithmétique
Type : congruences et Fermat, divisibilité · ECUE : HP (arithmétique)
Formules : $a \equiv b\,[n] \Rightarrow a^k \equiv b^k\,[n]$ ; Fermat : $p$ premier $\Rightarrow a^p \equiv a\,[p]$ ; $a^{mn+r} = (a^m)^n a^r$ ; $n \mid A \iff A \equiv 0\,[n]$

Montrer que $11^{n+1} + n\,2^{7n}$ est divisible par 13 si et seulement si $n \equiv 2\,[13]$. N'oubliez pas de citer le lemme de Gauss quand vous l'utilisez.
Consigne : dans cet exercice, vous devez obligatoirement détailler vos calculs en justifiant pas à pas chaque étape.
