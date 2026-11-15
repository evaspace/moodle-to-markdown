# Examen S1B2-SR (suites réelles) — janvier 2025 (sujet, FR)

- Source : `raw/S1/Finals/Maths PC/2029/PC/SR/final-2029-s1-maths-subject-fr.pdf` (8 pages)
- Date réelle : janvier 2025 (dossier promo 2029, ECUE SR = APIS suites 2031). Corrigé rédigé : `final-2029-s1-maths-correction-fr.md` (même dossier).
- Durée : 1 h 30. Barème sur 30 points ramené à 20. 6 exercices. Rigueur prise en compte, malus d'un point pour manque de propreté. Documents et calculatrices interdits.

## Exercice 1 : suites adjacentes (7 points)
Type : suites adjacentes via une suite géométrique · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/9
Formules : $w_{n+1} = qw_n \Rightarrow w_n = w_0q^n$ ; $|q| < 1 \Rightarrow q^n \to 0$ ; adjacentes : une croissante, l'autre décroissante, différence $\to 0$

Soient les suites $(u_n)$ et $(v_n)$ définies par : $u_0 = 2$, $v_0 = 3$ et $\forall n \in \mathbb{N}$, $u_{n+1} = \dfrac{3u_n + 2v_n}5$ et $v_{n+1} = \dfrac{2u_n + 3v_n}5$.
Soit $(w_n)$ définie pour tout entier $n \in \mathbb{N}$ par : $w_n = v_n - u_n$.
1. Étude de la suite $(w_n)$.
   (a) Montrer que la suite $(w_n)$ est géométrique. Préciser sa raison.
   (b) En déduire l'expression de $w_n$ en fonction de $n$.
   (c) De la question précédente, trouver le signe de la suite $(w_n)$.
2. En utilisant la question précédente, montrer que les suites $(u_n)$ et $(v_n)$ sont adjacentes.
3. Qu'en déduit-on sur les comportements des deux suites en $+\infty$ ?
4. Soit $(x_n) = (u_n + v_n)$.
   (a) Exprimer $x_{n+1}$ en fonction de $x_n$. En déduire l'expression de $x_n$ en fonction de $n$.
   (b) En déduire la limite de $(u_n)$ et la limite de $(v_n)$.

## Exercice 2 : étude d'une suite (5 points)
Type : monotonie et encadrement d'une somme · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/8
Formules : $u_{n+1} - u_n$ : écrire les deux sommes et simplifier les termes communs ($\frac1{2n} + \frac1{2n+1} - \frac1n$) ; $n \leqslant k \leqslant 2n-1 \Rightarrow \frac1{2n-1} \leqslant \frac1k \leqslant \frac1n$ ; somme de $n$ termes ; monotone bornée $\Rightarrow$ convergente ; passage à la limite dans les inégalités larges

Soit la suite $(u_n)$ définie, pour tout $n \in \mathbb{N}^*$, par $u_n = \displaystyle\sum_{k=n}^{2n-1} \frac1k$.
1. Étudier la monotonie (sens de variation) de la suite $(u_n)$.
2. En encadrant chaque terme de la somme, montrer que pour tout $n \in \mathbb{N}^*$, $\dfrac{n}{2n-1} \leqslant u_n \leqslant 1$.
3. En déduire que $(u_n)$ est bornée en précisant explicitement un majorant et un minorant.
4. Peut-on en déduire si $(u_n)$ converge ? Si oui, donner un encadrement de sa limite $\ell$ le plus précis possible que les données de l'exercice le permettent.

## Exercice 3 : comparaison de suites (7,5 points)
Type : comparaison de suites ($\sim$, $o$, $O$) · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/12
Formules : $u_n \sim v_n \iff \frac{u_n}{v_n} \to 1$ ; $u_n = o(v_n) \iff \frac{u_n}{v_n} \to 0$ ; $u_n = O(v_n) \iff \frac{u_n}{v_n}$ bornée ; convergente $\Rightarrow$ bornée, donc $\sim$ et $o$ impliquent $O$ ; croissances comparées : $\frac{\ln n}{n^a} \to 0$, $\frac{n^a}{e^n} \to 0$ ; $\frac{\sin n}{n} \to 0$ ; factoriser par le terme dominant

1. Soient $(u_n)$ et $(v_n)$ deux suites réelles ne s'annulant pas. Rappeler la définition de : $u_n = o(v_n)$, $u_n = O(v_n)$ et $u_n \sim v_n$ en $+\infty$.
2. Comparer en $+\infty$ les suites $(u_n)$ et $(v_n)$ suivantes à l'aide des comparateurs de Landau $\sim$, $= o(\cdot)$, $= O(\cdot)$ en citant toutes les comparaisons possibles et en justifiant vos réponses.
   (a) $u_n = -n^3 + n - 2$ et $v_n = -2n^2 + n$.
   (b) $u_n = e^n + \sqrt n$ et $v_n = e^n + e^{-n}$.
   (c) $u_n = 3^n + 6$ et $v_n = 5^n - 1$.

## Exercice 4 : cours (3 points)
Type : démonstration de cours (convergente implique bornée) · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/13
Formules : $u_n \to \ell$ : $\forall \varepsilon > 0, \exists N, \forall n \geqslant N, |u_n - \ell| < \varepsilon$ ; bornée : $\exists M, \forall n, |u_n| \leqslant M$ ; inégalité triangulaire $|u_n| \leqslant |u_n - \ell| + |\ell|$ ; $M = \max(|u_0|, \dots, |u_{N-1}|, 1 + |\ell|)$ ; contre-exemple $(-1)^n$

Soit $(u_n)$ une suite.
1. Rappeler la définition de : « $(u_n)$ est bornée ».
2. Montrer que : $(u_n)$ converge $\implies$ $(u_n)$ bornée.
3. La réciproque est-elle vraie ? Justifier.
4. Énoncer la contraposée de la proposition de la question 2.

## Exercice 5 : suite récurrente (4,5 points)
Type : suite récurrente $u_{n+1} = f(u_n)$ · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/10
Formules : constante $\iff u_0 = f(u_0)$ ; tableau de variations via $f'$ ; $f$ croissante sur $I$ et $u_n \in I \Rightarrow f(a) < f(u_n) < f(b)$ (récurrence) ; signe de $u_{n+1} - u_n$ ; monotone bornée $\Rightarrow$ convergente ; $\ell = f(\ell)$

Soit $(u_n)$ définie pour tout $n \in \mathbb{N}$ par $u_{n+1} = 1 + \dfrac14u_n^2$ avec $u_0 = \dfrac32$.
1. Étudier la monotonie de la suite $(u_n)$. (Vous chercherez à factoriser l'expression que vous calculez.)
2. Montrer par récurrence que : $\forall n \in \mathbb{N}$, $1 < u_n < 2$.
3. Peut-on en déduire le comportement de $(u_n)$ en $+\infty$ ? Si la suite converge, trouver sa limite. Justifier.

## Exercice 6 : suites extraites (3 points)
Type : suites extraites et divergence · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/11
Formules : $\sin(k\pi) = 0$ ; $\sin\left(2k\pi + \frac\pi3\right) = \frac{\sqrt3}2$ ; si $u_n \to \ell$, toute suite extraite tend vers $\ell$ ; deux suites extraites de limites différentes $\Rightarrow (u_n)$ diverge

Considérons la suite $(u_n) = \left(\sin\left(\dfrac{n\pi}3\right)\right)$.
1. Que vaut la suite $(u_{3n})$ ?
2. Vers quoi converge la suite $(u_{6n+1})$ ?
3. La suite $(u_n)$ est-elle convergente ? Justifier en citant proprement un résultat de votre cours.
