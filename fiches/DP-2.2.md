---
id: DP-2.2
syllabus: DP
type: définition
papier: maths-s1-dp/7
prereq: DP-2.1
alias: probabilité, espace probabilisé, P(Ω) = 1, P(∅) = 0, formules de base des probabilités, P(A ∪ B), contraire, complémentaire, P(A barre)
---
# Probabilité et espace probabilisé

Une probabilité sur $\Omega$ fini est une fonction $P : \mathcal{P}(\Omega) \to [0, 1]$ telle que $P(\Omega) = 1$ et $P(A \sqcup B) = P(A) + P(B)$ pour $A$, $B$ disjoints. $(\Omega, \mathcal{P}(\Omega), P)$ est un espace probabilisé.

Propriétés :

- $P(\emptyset) = 0$ et $P(\overline{A}) = 1 - P(A)$ ;
- $P(A) = P(A \setminus B) + P(A \cap B)$ ;
- $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ ;
- $P$ est déterminée par les $n$ valeurs $P(\{\omega_i\})$.

Source : Fiches de synthèse « Espace probabilisé », « Probabilités conditionnelles », « Variables aléatoires » (Moodle S1-MATHS-2031, Cours 2).
