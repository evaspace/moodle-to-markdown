---
id: DP-2.12
syllabus: DP
type: théorème
papier: maths-s1-dp/13
prereq: DP-2.11
alias: linéarité de l'espérance, E(aX+b), V(aX+b), E(X+Y), variance d'une somme, variables indépendantes, démonstration de cours
---
# Espérance et variance de aX + b, linéarité

Pour $a, b \in \mathbb{R}$ :

- $E(aX + b) = a\,E(X) + b$ ;
- $E(X + Y) = E(X) + E(Y)$ ;
- $V(aX + b) = a^2\,V(X)$ ;
- si $X$ et $Y$ sont indépendantes, $V(X + Y) = V(X) + V(Y)$.

Démonstration à connaître : $E(aX+b) = \sum (a x_i + b) P(X = x_i) = a E(X) + b \sum P(X = x_i)$, puis $V(aX+b) = E\big((aX + b - aE(X) - b)^2\big) = a^2 V(X)$.

Source : Fiches de synthèse « Espace probabilisé », « Probabilités conditionnelles », « Variables aléatoires » (Moodle S1-MATHS-2031, Cours 2).
