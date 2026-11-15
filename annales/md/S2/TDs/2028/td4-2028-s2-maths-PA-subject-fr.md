# Contrôle de cours ARITH (S2 PA) — lundi 6 mai 2024 (sujet, FR)

- Source : `raw/S2/TDs/2028/td4-2028-s2-maths-PA-subject-fr.pdf` (scan d'une copie annotée, 4 pages)
- Date réelle : 6 mai 2024 (S2 PA, dossier promo 2028). Les réponses manuscrites de la copie ne sont pas reprises.
- Durée : 1 heure. Barème sur 30, ramené à 20.

## Cours 1 : divisibilité et division euclidienne (4 points)
Type : division euclidienne dans $\mathbb{Z}$ · ECUE : HP (arithmétique)
Formules : $\exists!\,(q, r)$, $a = bq + r$, $0 \leqslant r < |b|$ ; ajuster : $a = bq + r = b(q+1) + (r - b)$ ; pour $-a$ : $-a = b(-q) - r = b(-q-1) + (b - r)$

Soit $(a,b) \in \mathbb{Z}^2$.
1. Donner la définition mathématique de « $a$ divise $b$ ».
2. Exemple : donner tous les diviseurs positifs de 6 sous forme d'ensemble.
3. On suppose $b$ non nul. Énoncer le théorème de la division euclidienne de $a$ par $b$.

## Cours 2 : congruences (11,5 points)
Type : congruences, Fermat, reste d'une puissance · ECUE : HP (arithmétique)
Formules : reste de la division par 4 : $r \in \{0,1,2,3\}$ ; $a \equiv b\,[n] \Rightarrow a^k \equiv b^k\,[n]$ ; Fermat : $p$ premier, $p \nmid a \Rightarrow a^{p-1} \equiv 1\,[p]$ ; $a^{q(p-1)+r} \equiv a^r\,[p]$

1. Soit $(a,b,c) \in \mathbb{Z}^3$. Montrer que $a \mid b$ et $a \mid c \Rightarrow \forall (u,v) \in \mathbb{Z}^2$, $a \mid bu + cv$.
2. Soient $n \in \mathbb{N}^*$ et $(a,b,c,d) \in \mathbb{Z}^4$ tels que $a \equiv b\,[n]$ et $c \equiv d\,[n]$. En utilisant la propriété précédente, montrer que $a + c \equiv b + d\,[n]$ et $a \times c \equiv b \times d\,[n]$.
3. Exemples : on pose $n = 8$, $a = 18$ et $c = 31$. Trouver modulo 8 : $a$, $c$, $a - c$, $a \times c$ et $a^5$. Chacune de vos réponses doit être un entier entre 0 et 7.
4. - (a) Énoncer le petit théorème de Fermat.
   - (b) Application : trouver le reste de la division euclidienne de $15^{14}$ par 11. Vous mettrez en évidence les étapes des calculs.

## Cours 3 : nombres premiers et pgcd (2 points)
Type : décomposition en facteurs premiers, PGCD · ECUE : HP (arithmétique)
Formules : critères de divisibilité (2, 3 : somme des chiffres, 5, 11) ; $a \wedge b = \prod p^{\min(\alpha_p, \beta_p)}$

On considère les entiers $a = 700$ et $b = 2 \times 3 \times 5^3 \times 7^2 \times 11$.
1. Décomposer $a$ en produit de facteurs premiers.
2. Trouver $a \wedge b$.

## Cours 4 : polynômes 1 (2,5 points)
Type : degré, division euclidienne de polynômes, racine · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/2
Formules : $\deg(A+B) \leqslant \max(\deg A, \deg B)$ ; $\deg(AB) = \deg A + \deg B$ ; $\exists!\,(Q,R)$, $A = BQ + R$, $\deg R < \deg B$ ; $\alpha$ racine $\iff A(\alpha) = 0 \iff X - \alpha \mid A$

Effectuer la division euclidienne de $A = X^5 - X^3 + 2X^2 - 4$ par $X^3 + X + 1$. Écrire le résultat sous forme d'égalité.

## Cours 5 : polynômes 2 (10 points)
Type : divisibilité de polynômes, multiplicité, factorisation dans $\mathbb{R}[X]$ et $\mathbb{C}[X]$ · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/9
Formules : $P(a) = 0 \iff X - a \mid P$ ; racine d'ordre $\geqslant 2$ $\iff P(a) = P'(a) = 0$ ; ordre exactement $m$ : $P^{(m)}(a) \neq 0$ ; $(X - a)^m \mid P$, $(X - a)^{m+1} \nmid P$ ; $X^2 + 1 = (X - i)(X + i)$ ; $\Delta < 0 \Rightarrow$ irréductible dans $\mathbb{R}[X]$

Les questions sont indépendantes. Pour les questions 2, 3 et 4, ce n'est pas la peine de donner les polynômes sous une forme développée.
1. Soit $P \in \mathbb{R}[X]$ de degré strictement supérieur à 3. Mettre les symboles $\Rightarrow$, $\Leftarrow$ ou $\iff$ à la place des pointillés.
   a) $-2$ racine de $P$ $\dots$ $(X+2) \mid P$. b) $P(3) = 0$ $\dots$ $(X-3)^2 \mid P$. c) $\exists Q \in \mathbb{R}[X]$, $P(X) = (X-1)Q(X)$ $\dots$ $(X-1)$ divise $P$ et $(X-1)^2$ ne divise pas $P$. d) $(X-1)^3 \mid P$ $\dots$ $P(1) = P'(1) = 0$.
2. Soit $P(X) = X^5 - 3X^4 + X^2$. Sans utiliser la notion de dérivée, expliquer pourquoi 0 est une racine d'ordre de multiplicité exactement 2 de $P$.
3. Donner un exemple d'un polynôme $Q \in \mathbb{R}[X]$, de degré 5, ayant $-2$ comme racine d'ordre de multiplicité exactement égal à 3.
4. Donner un exemple d'un polynôme $A \in \mathbb{R}[X]$, de degré 4, vérifiant $A(1) = 0$ et $A(-3) = A'(-3) = 0$.
5. On se donne les polynômes suivants : a) $A = X^2 + X$ ; b) $B = X^2 + 1$ ; c) $C = X^3 + X + 1$ ; d) $D = X^2 - 3X + 2$ ; e) $E = X^2 + X + 1$. Dire pour chacun d'entre eux s'ils sont irréductibles dans $\mathbb{R}[X]$ (entourer « OUI » ou « NON ») en justifiant votre choix.
