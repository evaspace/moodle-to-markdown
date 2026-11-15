# Contrôle de cours, mathématiques S1 — lundi 27 novembre 2023 (sujet, FR)

- Source : `raw/S1/TDs/2028/td2-2028-s1-maths-subject-fr.pdf` (3 pages)
- Date réelle : 27 novembre 2023 (dossier promo 2028). Corrigé rédigé : `td2-2028-s1-maths-correction-fr.md` (même dossier).
- Durée : 1 heure. Deux parties : ARITH (environ 45 min, sur 20) et ASI (environ 15 min, sur 10, note doublée).

## Partie ARITH, cours 1 : divisibilité et division euclidienne (7 points)
Type : divisibilité et division euclidienne (vrai/faux) · ECUE : HP (arithmétique)
Formules : $a \mid b \iff \exists k \in \mathbb{Z}, b = ka$ ; $a \mid b$ et $b \mid a \Rightarrow a = \pm b$ ; $a \mid b$, $a \mid c \Rightarrow a \mid bu + cv$ ; contre-exemple $2 \mid 4$, $4 \mid 4$, $8 \nmid 4$ ; $a \mid bc \not\Rightarrow a \mid b$ ou $a \mid c$ ($6 \mid 2 \times 3$) ; division euclidienne $0 \leqslant r < |b|$

1. Soit $(c, d) \in \mathbb{Z}^2$. Donner la définition mathématique (avec les quantificateurs) de « $c$ divise $d$ ».
2. Soit $(a, b, c) \in \mathbb{Z}^3$. Les affirmations suivantes sont-elles vraies ou fausses ? Justifier par une preuve si oui, donner un contre-exemple si non.
   (a) « Si $a \mid b$ et $b \mid a$ alors $a = b$ »
   (b) « Si $a \mid b$ et $a \mid c$ alors $\forall (u, v) \in \mathbb{Z}^2$, $a \mid bu + cv$ »
   (c) « $a \mid b$ et $c \mid b \implies ac \mid b$ »
3. Soit $(a, b) \in \mathbb{Z} \times \mathbb{Z}^*$.
   (a) Énoncer le théorème de la division euclidienne de $a$ par $b$.
   (b) On donne l'égalité $1034 = 148 \times 7 - 2$. Quels sont le quotient et le reste de la division euclidienne de 1034 par 7 ?

## Partie ARITH, cours 2 : autour de Bézout (5 points)
Type : Bézout (énoncé et applications) · ECUE : HP (arithmétique)
Formules : Bézout : $\exists (u,v), au + bv = a \wedge b$ ; $a \wedge b = 1 \iff \exists (u,v), au + bv = 1$ ; élever au carré / multiplier une relation de Bézout ; $2 \times (2n+1) \cdot 1 - \dots$ : $1 \cdot (2n+1) - 2 \cdot n = 1$ ; fraction irréductible $\iff$ numérateur et dénominateur premiers entre eux

On admet que pour tout $(a, b) \in \mathbb{Z}^2$, $\exists (u, v) \in \mathbb{Z}^2$ tel que $au + bv = a \wedge b$.
1. Soit $(a, b) \in \mathbb{Z}^2$. Montrer que : $\exists (u, v) \in \mathbb{Z}^2$ tel que $au + bv = 1 \iff a \wedge b = 1$.
2. Soit $(a, b) \in \mathbb{Z}^2$. A-t-on « $\exists (u, v) \in \mathbb{Z}^2$ tel que $au + bv = 3 \iff a \wedge b = 3$ » ? Justifier.

## Partie ARITH, cours 3 : congruence (8 points)
Type : congruences (définition, opérations) · ECUE : HP (arithmétique)
Formules : $a \equiv b\,[n] \iff n \mid a - b$ ; compatibilité avec $+$, $\times$, puissances ; $ab - cd = a(b - d) + d(a - c)$ ; réduire chaque nombre modulo $n$ ; reste dans $[\![0, n-1]\!]$

1. Soient $n \in \mathbb{N}^*$ et $a \in \mathbb{Z}$. Justifier qu'il existe un unique $r \in [\![0, n-1]\!]$ tel que $a \equiv r\,[n]$.
2. Soient $n \in \mathbb{N}^*$ et $(a, b, c, d) \in \mathbb{Z}^4$ tels que $a \equiv b\,[n]$ et $c \equiv d\,[n]$. Remplacer les pointillés par une réponse correcte (les réponses du type « $a \equiv a\,[n]$ » sont interdites) :
   (i) $a \equiv b\,[n] \iff$ … ; (ii) $a + c \equiv$ … $[n]$ ; (iii) $a \times c \equiv$ … $[n]$ ; (iv) $\forall k \in \mathbb{N}^*$, $a^k \equiv$ … $[n]$.
3. Application : on prend $n = 11$, $a = 224$ et $c = 85$. Vos réponses doivent être un entier entre 0 et 10.
   (a) À quoi sont congrus $a$ et $c$ modulo 11 ? Détaillez un peu vos calculs !
   (b) En déduire $a + c$, $2a - c$, $ac$ et $a^3$ modulo 11. Détaillez un peu vos calculs !

## Partie ASI, cours 1 : définitions (5 points)
Type : définitions sur les suites, exemples, limite de $q^n$ · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/3
Formules : croissante $\forall n, u_n \leqslant u_{n+1}$ ; bornée $\exists M, \forall n, |u_n| \leqslant M$ ; exemples $(-1)^n$, $1 - \frac1n$, $\cos n$ ; $(q^n)$ converge $\iff -1 < q \leqslant 1$ (limite 0 si $|q| < 1$, 1 si $q = 1$)

Soit $(u_n)$ une suite réelle définie sur $\mathbb{N}$.
1. (a) Donner la définition mathématique (avec des quantificateurs) de : « $(u_n)$ est bornée ».
   (b) Donner un exemple d'une suite non constante et bornée.
2. (a) Donner la définition mathématique (avec des quantificateurs) de : « $(u_n)$ est croissante ».
   (b) Que signifie que $(u_n)$ est monotone ?
   (c) Donner un exemple d'une suite ni croissante, ni décroissante.

## Partie ASI, cours 2 : convergence ou divergence (5 points)
Type : limites usuelles de suites · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/4
Formules : $\cos n$ diverge (suites extraites) ; $\ln(n^2 + n) \to +\infty$ ; $|q| < 1 \Rightarrow q^n \to 0$ ; $\frac1n \to 0$

Vos réponses doivent être justifiées.
1. La suite $(u_n)$ où, pour tout $n \in \mathbb{N}$, $u_n = \cos(n)$ est-elle convergente ? Si oui, donner sa limite.
2. La suite $(v_n)$ où, pour tout $n \in \mathbb{N}^*$, $v_n = \ln(n^2 + n)$ est-elle convergente ? Si oui, donner sa limite.
3. La suite $(w_n)$ où, pour tout $n \in \mathbb{N}$, $w_n = \left(-\dfrac23\right)^n$ est-elle convergente ? Si oui, donner sa limite.
4. La suite $(x_n)$ où, pour tout $n \in \mathbb{N}^*$, $x_n = 1 + \dfrac1n$ est-elle convergente ? Si oui, donner sa limite.
5. Donner un exemple d'une suite non constante convergente vers 2. Ne pas justifier.
