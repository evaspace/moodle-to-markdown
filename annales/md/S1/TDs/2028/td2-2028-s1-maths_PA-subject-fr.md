# Contrôle de cours 1, mathématiques S1PA — lundi 9 octobre 2023 (sujet, FR)

- Source : `raw/S1/TDs/2028/td2-2028-s1-maths_PA-subject-fr.pdf` (scan d'une copie remplie et notée, 3 pages ; seuls les énoncés sont repris)
- Date réelle : 9 octobre 2023 (parcours PA, dossier promo 2028).
- Durée : 1 heure. Barème sur 20.

## Cours 1 : définitions et théorèmes à énoncer (5 points)
Type : énoncés de cours sur les suites (récurrence, gendarmes, majorée) · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/13
Formules : récurrence : $P(n_0)$ et $\forall n \geqslant n_0, P(n) \Rightarrow P(n+1)$ donnent $\forall n \geqslant n_0, P(n)$ ; gendarmes $v_n \leqslant u_n \leqslant w_n$, $v_n, w_n \to \ell \Rightarrow u_n \to \ell$ ; majorée : $\exists M, \forall n, u_n \leqslant M$

1. Soient $n \in \mathbb{N}$, $n_0 \in \mathbb{N}$ et $P(n)$ une propriété dépendant de $n$, définie pour $n \geqslant n_0$. Énoncer rigoureusement le théorème de récurrence dans ce cas-là.
2. Énoncer rigoureusement le théorème des gendarmes.
3. Soit $(u_n)$ une suite. Donner la définition mathématique de : « $(u_n)$ est majorée » (avec les quantificateurs).

## Cours 2 : exemple des suites géométriques (4 points)
Type : suites géométriques (terme général, somme, limite de $q^n$) · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/1
Formules : $u_n = u_0q^n$ ; $\sum_{k=p}^n q^k = q^p\frac{1 - q^{n-p+1}}{1 - q}$ ; $\sum_{k=2}^8 \frac1{2^k} = \frac14 \cdot \frac{1 - (1/2)^7}{1/2}$ ; $q^n \to +\infty$ ($q > 1$), $1$ ($q = 1$), $0$ ($|q| < 1$), pas de limite ($q \leqslant -1$)

Soient $q \in \mathbb{R}$ et la suite $(u_n)$ définie pour tout $n \in \mathbb{N}$ par $u_{n+1} = qu_n$ avec $u_0 \in \mathbb{R}$ non nul.
1. Donner l'expression de $u_n$ en fonction de $n$ et de $q$.
2. (a) Supposons dans cette question que $q \neq 1$. Soient $n$ et $p$ deux entiers naturels tels que $p \leqslant n$. Donner la formule permettant de calculer $\sum_{k=p}^n q^k$.
   (b) Application : calculer (en simplifiant le plus possible) $S = \displaystyle\sum_{k=2}^8 \frac1{2^k}$.
3. Donner $\lim_{n \to +\infty} q^n$ en fonction de $q$.

## Cours 3 : limites de suites (6 points)
Type : opérations sur les limites, formes indéterminées · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/5
Formules : $\frac{\ell}{\ell'}$ ; $\frac{\ell > 0}{0^+} = +\infty$ ; $\frac{\pm\infty}{\ell'}$ selon le signe ; $\frac\infty\infty$ indéterminée ; $\frac{+\infty}{0^+} = +\infty$ ; $\frac{0^-}{0^+}$ indéterminée ; factoriser par le terme dominant

1. On considère deux suites $(u_n)$ et $(v_n)$ ainsi que deux réels $\ell$ et $\ell'$. Remplir le tableau suivant (soyez le plus précis possible sur le signe des « 0 » ou le signe des « $\infty$ ») :

| $\lim u_n$ | $\ell$ | $\ell > 0$ | $-\infty$ | $+\infty$ | $+\infty$ | $\ell < 0$ | $0^-$ |
|---|---|---|---|---|---|---|---|
| $\lim v_n$ | $\ell' \neq 0$ | $0^+$ | $\ell' < 0$ | $-\infty$ | $0^+$ | $0^-$ | $0^+$ |
| $\lim \frac{u_n}{v_n}$ | | | | | | | |

2. Calculer la limite en $+\infty$ de $(u_n)$ dans les cas suivants. Rédiger proprement.
   (a) $\forall n \in \mathbb{N}^*$, $u_n = \dfrac{-2n^2 + \frac1{\sqrt n}}{e^{-n} - 3}$.
   (b) $\forall n \in \mathbb{N}$, $u_n = \dfrac{3 - 2n^2 + 6n^3}{n^2 + 1}$.

## Cours 4 : comparaisons (3 points)
Type : comparaison et limites · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/6
Formules : $u_n \leqslant v_n$ et $v_n \to -\infty \Rightarrow u_n \to -\infty$ ; $u_n \leqslant v_n$ et $u_n \to +\infty \Rightarrow v_n \to +\infty$ ; pour une limite finie, il faut deux gendarmes

1. Soit la suite $(u_n)$ telle que, pour tout $n \in \mathbb{N}$, $0 \leqslant u_n \leqslant \dfrac1{\sqrt{n + 1}}$. La suite $(u_n)$ est-elle convergente ? Justifiez rigoureusement votre réponse.
2. Trouver proprement $\lim_{n \to +\infty} e^n - 2n^2$.
3. Soit $(v_n)$ telle que $\forall n \in \mathbb{N}$, $e^n - 2n^2 \leqslant v_n$. En partant du résultat de la question précédente, peut-on déterminer le comportement de $(v_n)$ en $+\infty$ ? Si oui, lequel est-il ?

## Cours 5 : convergence ou divergence (2 points)
Type : théorème de la limite monotone · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/8
Formules : croissante majorée $\Rightarrow$ convergente ; décroissante minorée $\Rightarrow$ convergente ; croissante non majorée $\Rightarrow +\infty$

Les affirmations suivantes sont-elles vraies ou fausses ? Si elles sont vraies, citer le théorème mis en jeu en donnant son énoncé proprement, sinon donner un contre-exemple. Soit $(u_n)$ une suite.
1. Si $(u_n)$ est décroissante et bornée alors elle converge.
2. Si $(u_n)$ est bornée alors elle converge.
