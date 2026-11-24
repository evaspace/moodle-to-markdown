---
id: DP-1.8
syllabus: DP
type: théorème
papier: maths-s1-dp/6
prereq: DP-1.7
alias: binôme de Newton, (x+y)^n, (a+b)^n, développer une puissance, somme des coefficients binomiaux, 2^n, cardinal de P(E), nombre de parties
---
# Formule du binôme de Newton

Pour $x, y \in \mathbb{C}$ et $n \in \mathbb{N}$ :
$$(x+y)^n = \sum_{k=0}^{n} \binom{n}{k} x^{n-k} y^k$$

Conséquences : $\sum_{k=0}^n \binom{n}{k} = 2^n$ (donc $\mathrm{Card}(\mathcal{P}(E)) = 2^n$) et $\sum_{k=0}^n (-1)^k \binom{n}{k} = 0$ pour $n \geqslant 1$.

Source : Fiche de synthèse « Dénombrement » (Moodle S1-MATHS-2031, Cours 1).
