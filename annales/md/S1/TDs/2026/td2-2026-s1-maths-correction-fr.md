# Contrôle TD 2 de mathématiques S1 — 29 novembre 2021 (corrigé)

- Source : `raw/S1/TDs/2026/td2-2026-s1-maths-correction-fr.pdf` (scan d'une copie manuscrite, 2 pages)
- Date réelle : 29 novembre 2021 (dossier promo 2026). Sujet : `td2-2026-s1-maths-subject-fr.md`.

## Questions de cours (3 points)
Type : division euclidienne dans $\mathbb{Z}$ · ECUE : HP (arithmétique)
Formules : $\exists!\,(q, r)$, $a = bq + r$, $0 \leqslant r < |b|$ ; ajuster : $a = bq + r = b(q+1) + (r - b)$ ; pour $-a$ : $-a = b(-q) - r = b(-q-1) + (b - r)$

1. $\exists!\,(q, r) \in \mathbb{Z}^2$ tel que $a = bq + r$ et $0 \leqslant r < |b|$.
2. (a) $1208 = 23 \times 51 + 35 = 23 \times 51 + 23 + 12 = 23 \times 52 + 12$. Comme $0 \leqslant 12 < 23$ : $q = 52$, $r = 12$.
(b) $-1208 = -23 \times 51 - 35 = 51 \times (-23) - 51 + 51 - 35 = 51 \times (-24) + 16$. Comme $0 \leqslant 16 < 51$ : $q = -24$, $r = 16$.

## Exercice 1 (2,5 points)
Type : petit théorème de Fermat, reste d'une puissance · ECUE : HP (arithmétique)
Formules : Fermat : $p$ premier, $p \nmid a \Rightarrow a^{p-1} \equiv 1\,[p]$ ; $a \equiv b\,[n] \Rightarrow a^k \equiv b^k\,[n]$ ; $a^{q(p-1)+r} \equiv a^r\,[p]$

Fermat : 1) $p$ premier, $n \in \mathbb{N}$ : $n^p \equiv n\,[p]$. 2) Si de plus $p \nmid n$ : $n^{p-1} \equiv 1\,[p]$.
$39 \equiv 4\,[7]$ d'où $39^{129} \equiv 4^{129}\,[7]$. 7 est premier et $7 \nmid 4$, d'où $4^6 \equiv 1\,[7]$.
$129 = 6 \times 21 + 3$, $4^{129} = (4^6)^{21} \times 4^3 \equiv 4^3\,[7]$. Or $4^2 = 16 \equiv 2\,[7]$ d'où $4^3 \equiv 4 \times 2 \equiv 1\,[7]$.
Ainsi $39^{129} \equiv 1\,[7]$ et, comme $0 \leqslant 1 < 7$, le reste est 1.

## Exercice 2 (3 points)
Type : décomposition en facteurs premiers, diviseurs communs · ECUE : HP (arithmétique)
Formules : $a \wedge b = \prod p^{\min(\alpha_p, \beta_p)}$ ; $d \mid a$ et $d \mid b \iff d \mid a \wedge b$ (Bézout) ; diviseurs de $\prod p_i^{\gamma_i}$ : $\prod p_i^{\delta_i}$, $0 \leqslant \delta_i \leqslant \gamma_i$ ; nombre : $\prod(\gamma_i + 1)$

1. $a = 2^2 \times 3^3 \times 5^1 \times 7^0$ et $b = 2^4 \times 3^3 \times 5^0 \times 7^1$, d'où $a \wedge b = 2^2 \times 3^3 = 108$.
2. Un diviseur commun s'écrit $d = 2^i \times 3^j$ avec $i \in [\![0, 2]\!]$ et $j \in [\![0, 3]\!]$ : $3 \times 4 = 12$ diviseurs communs.
3. $77 = 7 \times 11$ et $a = 2^2 \times 3^3 \times 5$, donc $77 \wedge a = 1$. Comme $77 \mid ac$, par Gauss $77 \mid c$.

## Exercice 3 (1,5 points)
Type : Bézout (énoncé et applications) · ECUE : HP (arithmétique)
Formules : Bézout : $\exists (u,v), au + bv = a \wedge b$ ; $a \wedge b = 1 \iff \exists (u,v), au + bv = 1$ ; élever au carré / multiplier une relation de Bézout ; $2 \times (2n+1) \cdot 1 - \dots$ : $1 \cdot (2n+1) - 2 \cdot n = 1$ ; fraction irréductible $\iff$ numérateur et dénominateur premiers entre eux

La fraction est irréductible $\iff (2n + 1) \wedge n = 1$. Or $(2n + 1) \times 1 + n \times (-2) = 1$ : par Bézout, $2n + 1$ et $n$ sont premiers entre eux.
