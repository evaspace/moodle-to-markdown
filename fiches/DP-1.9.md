---
id: DP-1.9
syllabus: DP
type: méthode
papier: maths-s1-dp/6
prereq: DP-1.5
alias: double comptage, Vandermonde, compter de deux façons, interpréter une formule de dénombrement, preuve combinatoire
---
# Double comptage

Compter le même ensemble de deux façons donne une égalité.

- Vandermonde : $\sum_{k=0}^{p} \binom{a}{k}\binom{b}{p-k} = \binom{a+b}{p}$ (choisir $p$ personnes parmi $a$ filles et $b$ garçons, selon le nombre $k$ de filles).
- $\binom{n}{p}\binom{p}{k} = \binom{n}{k}\binom{n-k}{p-k}$ (un comité de $p$ personnes et son bureau de $k$ personnes).

Interpréter une formule : dire quel ensemble chaque membre compte.

Source : Fiche de synthèse « Dénombrement » (Moodle S1-MATHS-2031, Cours 1).
