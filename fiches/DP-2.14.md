---
id: DP-2.14
syllabus: DP
type: théorème
papier: maths-s1-dp/14
prereq: DP-2.13, DP-1.5
alias: loi binomiale, B(n,p), nombre de succès, schéma de Bernoulli, répétitions indépendantes, espérance np, variance np(1-p), P(X = k), au moins un succès
---
# Loi binomiale

Somme $Y = X_1 + \dots + X_n$ de $n$ variables de Bernoulli **indépendantes** de paramètre $p$ (nombre de succès) : $Y \sim \mathcal{B}(n, p)$.
$$Y(\Omega) = [\![0, n]\!], \qquad P(Y = k) = \binom{n}{k} p^k (1-p)^{n-k}$$
$$E(Y) = np, \qquad V(Y) = np(1-p)$$
« Au moins un succès » : $P(Y \geqslant 1) = 1 - (1-p)^n$.

Source : Fiches de synthèse « Espace probabilisé », « Probabilités conditionnelles », « Variables aléatoires » (Moodle S1-MATHS-2031, Cours 2).
