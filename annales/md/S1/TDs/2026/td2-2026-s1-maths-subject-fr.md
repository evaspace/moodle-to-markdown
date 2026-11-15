# Contrôle TD 2 de mathématiques S1 — lundi 29 novembre 2021 (sujet, FR)

- Source : `raw/S1/TDs/2026/td2-2026-s1-maths-subject-fr.pdf` (scan, 2 pages)
- Date réelle : 29 novembre 2021 (dossier promo 2026). Corrigé : `td2-2026-s1-maths-correction-fr.md`.
- Durée : 45 minutes. Barème sur 10, ramené sur 20.

## Questions de cours (3 points)
Type : division euclidienne dans $\mathbb{Z}$ · ECUE : HP (arithmétique)
Formules : $\exists!\,(q, r)$, $a = bq + r$, $0 \leqslant r < |b|$ ; ajuster : $a = bq + r = b(q+1) + (r - b)$ ; pour $-a$ : $-a = b(-q) - r = b(-q-1) + (b - r)$

Soit $(a, b) \in \mathbb{Z} \times \mathbb{Z}^*$.
1. Énoncer avec soin le théorème de la division euclidienne de $a$ par $b$.
2. On donne l'égalité : $1208 = 23 \times 51 + 35$.
   (a) Donner le quotient et le reste de la division euclidienne de 1208 par 23 en justifiant votre réponse.
   (b) Donner le quotient et le reste de la division euclidienne de $-1208$ par 51 en justifiant votre réponse.

## Exercice 1 (2,5 points)
Type : petit théorème de Fermat, reste d'une puissance · ECUE : HP (arithmétique)
Formules : Fermat : $p$ premier, $p \nmid a \Rightarrow a^{p-1} \equiv 1\,[p]$ ; $a \equiv b\,[n] \Rightarrow a^k \equiv b^k\,[n]$ ; $a^{q(p-1)+r} \equiv a^r\,[p]$

En utilisant obligatoirement le petit théorème de Fermat que vous énoncerez avec soin, trouver le reste de la division euclidienne de $n = 39^{129}$ par 7.

## Exercice 2 (3 points)
Type : décomposition en facteurs premiers, diviseurs communs · ECUE : HP (arithmétique)
Formules : $a \wedge b = \prod p^{\min(\alpha_p, \beta_p)}$ ; $d \mid a$ et $d \mid b \iff d \mid a \wedge b$ (Bézout) ; diviseurs de $\prod p_i^{\gamma_i}$ : $\prod p_i^{\delta_i}$, $0 \leqslant \delta_i \leqslant \gamma_i$ ; nombre : $\prod(\gamma_i + 1)$

On considère $a = 2 \times 3^2 \times 5 \times 6$ et $b = 2^4 \times 3^3 \times 7$.
1. Trouver $a \wedge b$ le pgcd de $a$ et de $b$.
2. Écrire sous forme de facteurs premiers la forme générale d'un diviseur commun (et positif) de $a$ et de $b$. En déduire le nombre de diviseurs communs (positifs) de $a$ et de $b$. Expliquer brièvement.
3. Soit $c \in \mathbb{N}^*$ tel que $77 \mid ac$. Montrer avec soin que $77 \mid c$.

## Exercice 3 (1,5 points)
Type : Bézout (énoncé et applications) · ECUE : HP (arithmétique)
Formules : Bézout : $\exists (u,v), au + bv = a \wedge b$ ; $a \wedge b = 1 \iff \exists (u,v), au + bv = 1$ ; élever au carré / multiplier une relation de Bézout ; $2 \times (2n+1) \cdot 1 - \dots$ : $1 \cdot (2n+1) - 2 \cdot n = 1$ ; fraction irréductible $\iff$ numérateur et dénominateur premiers entre eux

Soit $n \in \mathbb{N}^*$. Montrer que la fraction $\dfrac{n}{2n + 1}$ est irréductible.
