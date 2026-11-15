# Correction examen S1B2-ARITH — janvier 2024

- Source : `raw/S1/Finals/Maths PC/2028/PC/ARITH/final-2028-s1-maths-correction-fr.pdf` (2 pages)
- Date réelle : janvier 2024 (dossier promo 2028). Sujet : `final-2028-s1-maths-subject-fr.md`.

## Exercice 1 : nombres premiers et pgcd
Type : décomposition en facteurs premiers, nombre de diviseurs, PGCD · ECUE : HP (arithmétique)
Formules : diviseur de $\prod p_i^{\alpha_i}$ : $\prod p_i^{\beta_i}$, $0 \leqslant \beta_i \leqslant \alpha_i$ ; nombre de diviseurs $\prod(\alpha_i + 1)$ ; $a \wedge b = \prod p^{\min}$

1. $a = 2^2 \times 3 \times 5^2$.
2. Tout diviseur de $b$ est de la forme $d = 2^i \times 3^j \times 5^k \times 11^r$ avec $i \in \{0,1,2\}$, $j \in \{0,1,2,3\}$, $k \in \{0,1\}$, $r \in \{0,1\}$. Ainsi $b$ a $3 \times 4 \times 2 \times 2 = 48$ diviseurs positifs distincts.
3. $c = 2 \times 3^2 \times 5^2 \times 11$. En prenant les plus petites puissances communes : $b \wedge c = 2 \times 3^2 \times 5 \times 11 = 990$.

## Exercice 2 : congruence
Type : congruences, Fermat, reste d'une puissance · ECUE : HP (arithmétique)
Formules : reste de la division par 4 : $r \in \{0,1,2,3\}$ ; $a \equiv b\,[n] \Rightarrow a^k \equiv b^k\,[n]$ ; Fermat : $p$ premier, $p \nmid a \Rightarrow a^{p-1} \equiv 1\,[p]$ ; $a^{q(p-1)+r} \equiv a^r\,[p]$

1. (a) Le reste $r$ vaut 0, 1, 2 ou 3. Si $r = 0$, $4 \mid n$ : contradiction avec $n \wedge 4 = 1$. Si $r = 2$, $n = 4q + 2 = 2(2q + 1)$ et 2 est un diviseur commun de $n$ et 4 : contradiction. Donc $r = 1$ ou $3$.
(b) Si $r = 1$, $n^2 - 1 \equiv 1 - 1 \equiv 0\,[4]$. Si $r = 3$, $n^2 \equiv 9 \equiv 1\,[4]$, donc $n^2 - 1 \equiv 0\,[4]$.
2. $8 \equiv 1\,[7]$ donc $8^{2023} \equiv 1\,[7]$. $17 \equiv 3\,[7]$, $17^9 \equiv 3^9\,[7]$ ; 7 premier et $3 \wedge 7 = 1$ : par Fermat $3^6 \equiv 1\,[7]$, d'où $3^9 = 3^6 \times 3^3 \equiv 27 \equiv 6\,[7]$.
$N \equiv 6 - 1 \equiv 5\,[7]$ et $0 \leqslant 5 < 7$ : le reste est 5.

## Exercice 3 : autour de Bézout et Gauss
Type : Bézout, Euclide, lemme de Gauss (démonstrations) · ECUE : HP (arithmétique)
Formules : Bézout : $\exists (u,v), au + bv = a \wedge b$ ; $a \wedge b = 1 \iff \exists (u,v), au + bv = 1$ ; Euclide : $a = bq + r$, remonter les divisions ; Gauss : $a \mid bc$, $a \wedge b = 1 \Rightarrow a \mid c$ ; $a \mid c$, $b \mid c$, $a \wedge b = 1 \Rightarrow ab \mid c$

1. (a) Version 1 : $\exists (u,v) \in \mathbb{Z}^2$, $au + bv = a \wedge b$. Version 2 : $a \wedge b = 1 \iff \exists (u,v) \in \mathbb{Z}^2$, $au + bv = 1$.
(b) Vraie : si $au_0 + bv_0 = 1$, alors $a(2u_0) + b(2v_0) = 2$.
(c) $47 = 39 \times 1 + 8$, $39 = 8 \times 4 + 7$, $8 = 7 \times 1 + 1$, $7 = 1 \times 7 + 0$ : $47 \wedge 39 = 1$.
$1 = 8 - 7 = 8 - (39 - 8 \times 4) = 8 \times 5 - 39 = (47 - 39) \times 5 - 39 = 39 \times (-6) + 47 \times 5$ : $(u,v) = (-6, 5)$.
2. (a) Démonstration de cours (renvoi au document « Démonstrations à connaître »).
(b) $5(x - 1) = 7y$ donc $5 \mid 7y$ ; $5 \wedge 7 = 1$ donc par Gauss $5 \mid y$ : $y = 5k$. En reportant, $5(x - 1) = 35k$, soit $x = 1 + 7k$.
3. $c = ak_1 = bk_2$ et, par Bézout, $au + bv = 1$. Alors $c = cau + cbv = bk_2au + ak_1bv = ab(uk_2 + k_1v)$, donc $ab \mid c$.
Variante par Gauss : $c = ak$ et $b \mid ak$ avec $a \wedge b = 1$, donc $b \mid k$, $k = bk'$ et $c = abk'$.
