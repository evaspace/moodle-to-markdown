# Contrôle de cours ECUE ARITH, mathématiques S1 — lundi 25 novembre 2024 (sujet, FR)

- Source : `raw/S1/TDs/2029/td2-2029-s1-maths-subject-fr.pdf` (3 pages)
- Date réelle : 25 novembre 2024 (dossier promo 2029). Pas de corrigé.
- Durée : 1 heure. Barème sur 20.

## Cours 1 : divisibilité et division euclidienne (5 points)
Type : divisibilité et division euclidienne (vrai/faux) · ECUE : HP (arithmétique)
Formules : $a \mid b \iff \exists k \in \mathbb{Z}, b = ka$ ; $a \mid b$ et $b \mid a \Rightarrow a = \pm b$ ; $a \mid b$, $a \mid c \Rightarrow a \mid bu + cv$ ; contre-exemple $2 \mid 4$, $4 \mid 4$, $8 \nmid 4$ ; $a \mid bc \not\Rightarrow a \mid b$ ou $a \mid c$ ($6 \mid 2 \times 3$) ; division euclidienne $0 \leqslant r < |b|$

Soit $(a, b, c) \in \mathbb{Z}^3$.
1. Donner la définition mathématique de « $a$ est un multiple de $b$ ».
2. Donner tous les entiers relatifs $a$ tels que $a \mid 6$.
3. Énoncer le théorème de la division euclidienne de $a \in \mathbb{Z}$ par $-18$.
4. Les affirmations suivantes sont-elles vraies ou fausses ? Si oui, justifier par une preuve, si non, donner un contre-exemple.
   (a) « $a \mid b$ et $b \mid c \implies a \mid c$ »
   (b) « $a \mid bc \implies a \mid b$ ou $a \mid c$ »
   (c) « $\exists!\,n \in [\![0, 6]\!]$ tel que $7 \mid a - n$ »
   (d) « $a \mid b$ et $b \mid a \implies a = b$ »

## Cours 2 : congruence (6,5 points)
Type : congruences (définition, opérations) · ECUE : HP (arithmétique)
Formules : $a \equiv b\,[n] \iff n \mid a - b$ ; compatibilité avec $+$, $\times$, puissances ; $ab - cd = a(b - d) + d(a - c)$ ; réduire chaque nombre modulo $n$ ; reste dans $[\![0, n-1]\!]$

1. Soient $n \in \mathbb{N}^*$ et $(a, b) \in \mathbb{Z}^2$. Donner la définition mathématique de $a \equiv b\,[n]$.
2. Compléter les pointillés par un entier $r \in [\![0, n-1]\!]$ : a) $87 \equiv \dots\,[5]$ ; b) $24 \equiv \dots\,[7]$ ; c) $-15 \equiv \dots\,[6]$ ; d) $-13 \equiv \dots\,[11]$.
3. Soient $n \in \mathbb{N}^*$ et $(a, b, c, d) \in \mathbb{Z}^4$ tels que $a \equiv b\,[n]$ et $c \equiv d\,[n]$. Compléter par une expression avec $b$ et/ou $d$ : a) $-2a + 3c \equiv \dots\,[n]$ ; b) $a \times c \equiv \dots\,[n]$ ; c) $a^{13} \equiv \dots\,[n]$.
   Application : prenons $n = 6$. Compléter le tableau par un entier $r \in [\![0, 5]\!]$ :

| $a$ | $-2$ | 1 | 28 |
|---|---|---|---|
| $b$ | 3 | 4 | 14 |
| $a\,[6]$ | | | |
| $b\,[6]$ | | | |
| $a^3 - 2b\,[6]$ | | | |

4. Petit théorème de Fermat.
   (a) Énoncer proprement le théorème ainsi que son corollaire.
   (b) Application : i. En termes de congruence, que signifie $11 \mid 4^{13}$ ? ii. A-t-on $11 \mid 4^{13}$ ? Justifiez votre réponse en utilisant le petit théorème de Fermat.

## Cours 3 : autour de Bézout (6,5 points)
Type : Bézout, Euclide, lemme de Gauss (démonstrations) · ECUE : HP (arithmétique)
Formules : Bézout : $\exists (u,v), au + bv = a \wedge b$ ; $a \wedge b = 1 \iff \exists (u,v), au + bv = 1$ ; Euclide : $a = bq + r$, remonter les divisions ; Gauss : $a \mid bc$, $a \wedge b = 1 \Rightarrow a \mid c$ ; $a \mid c$, $b \mid c$, $a \wedge b = 1 \Rightarrow ab \mid c$

1. Énoncer rigoureusement le théorème de Bézout d'une part pour deux entiers ayant un pgcd quelconque et d'autre part pour des entiers premiers entre eux.
2. Soit $(a, b, c, d, \alpha) \in (\mathbb{Z}^*)^5$ tel que $ac + bd = \alpha$. Dire si les affirmations suivantes sont vraies (V) ou fausses (F) :
   a) « Si $\alpha = 1$ alors $a$ et $b$ sont premiers entre eux » ; b) « Si $\alpha = 1$ alors $a$ et $d$ sont premiers entre eux » ; c) « Si $\alpha = 2$ alors $c \wedge d = 2$ ».
3. Énoncer ET démontrer le lemme de Gauss.

## Cours 4 : nombres premiers et pgcd (2 points)
Type : PGCD par facteurs premiers, Fermat · ECUE : HP (arithmétique)
Formules : décomposition en facteurs premiers ; $a \wedge b = \prod p^{\min}$ ; Fermat : $p$ premier, $p \nmid a \Rightarrow a^{p-1} \equiv 1\,[p]$ ; premier : exactement deux diviseurs positifs

1. Soit $p \in \mathbb{N}^*$. Rappeler ce que signifie que « $p$ est un nombre premier ».
2. Décomposer $a = 300$ en produit de facteurs premiers.
3. Soit $b = 2^3 \times 3^2 \times 5 \times 7$. Donner $a \wedge b$.
