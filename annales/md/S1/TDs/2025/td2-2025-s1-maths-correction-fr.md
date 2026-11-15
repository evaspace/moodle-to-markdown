# Contrôle TD 2 (S1) — distanciel, fin 2020 (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (pas de corrigé officiel). Sujet : `td2-2025-s1-maths-subject-fr.md` (même dossier). Calculs vérifiés avec sympy. Les questions et exercices d'arithmétique sont hors programme 2031.

## Question de cours 1
Type : loi binomiale (QCM) · ECUE : DP · Niveau : maths-s1-dp/14
Formules : $\mathcal{B}(n, p)$ : $P(Y = k) = \binom nk p^k(1-p)^{n-k}$, $E = np$, $V = np(1-p)$ ; $P(Y > 1) = 1 - P(Y = 0) - P(Y = 1)$

$Y\sim\mathcal B\left(5,\dfrac15\right)$ ($P(\text{dé}\le2)=\dfrac15$). a) $P(Y=2)=\dbinom52\dfrac{4^3}{5^5}=\dfrac{640}{3125}=\dfrac{4^4}{2\times5^4}$ : vrai. b) $V(Y)=5\cdot\dfrac15\cdot\dfrac45=\dfrac45$ : vrai. c) $E(Y)=1\ne2$ : faux. d) $P(Y>1)=1-\dfrac{4^5}{5^5}-5\cdot\dfrac{4^4}{5^5}=\dfrac{5^5-9\times2^8}{5^5}$ : l'énoncé donne $5\times2^8$ : faux. **Réponses : a et b.**

## Question de cours 2
Type : divisibilité, PGCD, Bézout, Gauss, Fermat (QCM) · ECUE : HP (arithmétique)
Formules : $a \mid b$ et $a \mid c \Rightarrow a \mid b - c$ ; $au + cv = d \Rightarrow (a \wedge c) \mid d$ ; Fermat $p \nmid a \Rightarrow a^{p-1} \equiv 1\,[p]$ ; $\mathrm{pgcd}$ = produit des facteurs communs à la plus petite puissance ; Gauss exige $a \wedge b = 1$

$a=2^{12}\times3^5\times7$, $a\wedge b=2\times7=14$. a) $12\mid a$, donc $12\mid a-c\Rightarrow12\mid c$ : vrai. b) $au+cv=3$ donne seulement $a\wedge c\mid3$ : faux. c) $11\nmid a$, Fermat : $a^{10}\equiv1\ [11]$ : vrai. d) $a\wedge b=14\ne2^2\times7^2$ : faux. e) $a\wedge15=3\ne1$ : faux (contre-exemple $c=5$). **Réponses : a et c.** (Le sujet d'origine indique « a et c ».)

## Exercice 1 : probabilités
Type : probabilités totales et Bayes · ECUE : DP · Niveau : maths-s1-dp/10
Formules : probabilités totales : $P(M) = P(M \mid V)P(V) + P(M \mid \bar V)P(\bar V)$ ; Bayes : $P(V \mid M) = \frac{P(M \mid V)P(V)}{P(M)}$ ; $P(\bar V) = 1 - P(V)$

$V$ : boule verte, $R$ : boule rouge, $P(V)=\dfrac25$, $P(R)=\dfrac35$. Dé : $P(\text{vert})=\dfrac13$, $P(\text{rouge})=\dfrac23$.
1. $P(\text{point})=P(V)\cdot\dfrac13+P(R)\cdot\dfrac23=\dfrac2{15}+\dfrac6{15}=\dfrac8{15}$.
2. $P(6\text{ points}\mid V)=\left(\dfrac13\right)^6$ et $P(6\text{ points}\mid R)=\left(\dfrac23\right)^6$. Bayes : $P(V\mid6\text{ points})=\dfrac{P(V)\left(\frac13\right)^6}{P(V)\left(\frac13\right)^6+P(R)\left(\frac23\right)^6}=\dfrac{\frac25}{\frac25+\frac35\cdot64}=\dfrac{2}{2+192}=\dfrac1{97}$.

## Exercice 2 : arithmétique
Type : congruences et Fermat, divisibilité · ECUE : HP (arithmétique)
Formules : $a \equiv b\,[n] \Rightarrow a^k \equiv b^k\,[n]$ ; Fermat : $p$ premier $\Rightarrow a^p \equiv a\,[p]$ ; $a^{mn+r} = (a^m)^n a^r$ ; $n \mid A \iff A \equiv 0\,[n]$

Modulo $13$ : $11\equiv-2$ et $2^7=128=13\times9+11\equiv-2$. Donc $11^{n+1}\equiv(-2)^{n+1}$ et $2^{7n}\equiv(-2)^n$. $11^{n+1}+n\,2^{7n}\equiv(-2)^n(-2+n)\ [13]$.
Si $n\equiv2\ [13]$ : le facteur $(n-2)$ est divisible par $13$, donc l'expression aussi.
Réciproquement, si $13$ divise l'expression : $13\mid(-2)^n(n-2)$. Comme $13$ est premier et ne divise pas $2$, $13\wedge(-2)^n=1$. Par le lemme de Gauss, $13\mid n-2$ : $n\equiv2\ [13]$.
