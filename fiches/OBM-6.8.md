---
id: OBM-6.8
syllabus: OBM
type: méthode
papier: maths-s1-obm/7
prereq: OBM-6.4
alias: récurrence, raisonnement par récurrence, initialisation, hérédité, récurrence forte, récurrence double, inégalité de Bernoulli, n! > 2^n, somme géométrique par récurrence, dérivée n-ième
---
# Raisonnement par récurrence

Pour montrer $\forall n \geqslant n_0, P(n)$ :

1. **Initialisation** : $P(n_0)$ est vraie.
2. **Hérédité** : pour un $n \geqslant n_0$ fixé, $P(n) \Rightarrow P(n+1)$.

Récurrence double : initialiser $P(n_0)$ et $P(n_0 + 1)$, puis $P(n) \wedge P(n+1) \Rightarrow P(n+2)$. Récurrence forte : supposer $P(n_0), \dots, P(n)$.

Classiques des annales : inégalité de Bernoulli $(1+x)^n \geqslant 1 + nx$ ($x > -1$), $n! > 2^n$ pour $n \geqslant 4$, dérivée $n$-ième.

Source : Cours 6 « Compléments séminaire » et TD séminaire (Moodle S1-MATHS-2031) ; types d'exercices des annales OBM.
