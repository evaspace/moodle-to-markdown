# Contrôle de cours 2, mathématiques S1 — lundi 5 décembre 2022 (sujet, FR)

- Source : `raw/S1/TDs/2027/td2-2027-s1-maths-subject-fr.pdf` (3 pages)
- Date réelle : 5 décembre 2022 (dossier promo 2027). Pas de corrigé.
- Durée : 1 heure. Barème sur 20.

## Exercice 1 : divisibilité et division euclidienne (3,5 points)
Type : division euclidienne dans $\mathbb{Z}$ · ECUE : HP (arithmétique)
Formules : $\exists!\,(q, r)$, $a = bq + r$, $0 \leqslant r < |b|$ ; ajuster : $a = bq + r = b(q+1) + (r - b)$ ; pour $-a$ : $-a = b(-q) - r = b(-q-1) + (b - r)$

1. (a) Soit $(n, m) \in \mathbb{Z}^2$. Donner la définition mathématique de $n \mid m$.
   (b) Application : donner tous les diviseurs de 4 dans $\mathbb{Z}$.
2. (a) Soit $(n, m) \in \mathbb{Z} \times \mathbb{Z}^*$. Énoncer avec soin le théorème de la division euclidienne de $n$ par $m$.
   (b) On donne l'égalité : $-358 = 21 \times (-18) + 20$.
      (i) Donner le quotient $q_1$ et le reste $r_1$ de la division euclidienne de $-358$ par 21. Justifier.
      (ii) Donner le quotient $q_2$ et le reste $r_2$ de la division euclidienne de $-358$ par $-18$. Justifier.

## Exercice 2 : congruence (5 points)
Type : congruences (définition, opérations) · ECUE : HP (arithmétique)
Formules : $a \equiv b\,[n] \iff n \mid a - b$ ; compatibilité avec $+$, $\times$, puissances ; $ab - cd = a(b - d) + d(a - c)$ ; réduire chaque nombre modulo $n$ ; reste dans $[\![0, n-1]\!]$

Soient $n \in \mathbb{N}^*$ et $(a, b, c, d) \in \mathbb{Z}^4$.
1. Donner la définition mathématique de $a \equiv b\,[n]$.
2. Montrer que si $a \equiv c\,[n]$ et $b \equiv d\,[n]$ alors $ab \equiv cd\,[n]$.
3. Dans le même esprit que la question précédente, que dire de $a + b$ et $a^8$ modulo $n$ dans le cas où $a \equiv c\,[n]$ et $b \equiv d\,[n]$ ? Ne pas justifier.
4. $24^3 + 78$ est-il divisible par 7 ? Justifier.

## Exercice 3 : lemme de Gauss (3 points)
Type : Bézout, Euclide, lemme de Gauss (démonstrations) · ECUE : HP (arithmétique)
Formules : Bézout : $\exists (u,v), au + bv = a \wedge b$ ; $a \wedge b = 1 \iff \exists (u,v), au + bv = 1$ ; Euclide : $a = bq + r$, remonter les divisions ; Gauss : $a \mid bc$, $a \wedge b = 1 \Rightarrow a \mid c$ ; $a \mid c$, $b \mid c$, $a \wedge b = 1 \Rightarrow ab \mid c$

Énoncer et démontrer le lemme de Gauss.

## Exercice 4 : pgcd (2,5 points)
Type : PGCD par facteurs premiers, Fermat · ECUE : HP (arithmétique)
Formules : décomposition en facteurs premiers ; $a \wedge b = \prod p^{\min}$ ; Fermat : $p$ premier, $p \nmid a \Rightarrow a^{p-1} \equiv 1\,[p]$ ; premier : exactement deux diviseurs positifs

On se donne les deux entiers $a = 2^3 \times 3 \times 21$ et $b = 90$. Les deux questions sont indépendantes.
1. Trouver $a \wedge b$. Donnez quelques explications sur votre calcul.
2. Trouver le reste de la division euclidienne de $a^{22}$ par 23. Justifiez rigoureusement votre réponse.

## Exercice 5 (6 points)
Type : définitions sur les suites, exemples, limite de $q^n$ · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/4
Formules : croissante $\forall n, u_n \leqslant u_{n+1}$ ; bornée $\exists M, \forall n, |u_n| \leqslant M$ ; exemples $(-1)^n$, $1 - \frac1n$, $\cos n$ ; $(q^n)$ converge $\iff -1 < q \leqslant 1$ (limite 0 si $|q| < 1$, 1 si $q = 1$)

Soit $(u_n)$ une suite.
1. Rappeler les définitions mathématiques (avec les quantificateurs) de :
   (a) $(u_n)$ est croissante ;
   (b) $(u_n)$ est bornée.
2. Donner un exemple d'une suite (non constante) :
   (a) divergente (justifier brièvement) ;
   (b) majorée par 3 (justifier brièvement) ;
   (c) strictement croissante et convergente (justifier proprement).
3. Soit $q \in \mathbb{R}$. Prenons $(u_n) = (q^n)$. Donner une condition nécessaire et suffisante sur $q$ pour que la suite $(u_n)$ converge. Donner la limite dans ce cas-là.
