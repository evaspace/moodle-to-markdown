---
id: OBM-6.8
syllabus: OBM
type: méthode
papier: maths-s1-obm/7
prereq: OBM-6.4
alias: récurrence, raisonnement par récurrence, initialisation, hérédité, récurrence forte, récurrence double, inégalité de Bernoulli, n! > 2^n, somme géométrique par récurrence, dérivée n-ième
---
# Raisonnement par récurrence

> **À retenir.** Pour prouver $\forall n\geqslant n_0,\ P(n)$ : **initialisation** $P(n_0)$ vraie ; **hérédité** : pour un $n\geqslant n_0$ **fixé**, $P(n)\Rightarrow P(n+1)$. Alors $P(n)$ est vraie pour tout $n\geqslant n_0$.

## Méthode en copie
1. « Pour $n\in\mathbb N^*$, notons $P(n)$ : » puis la propriété **en entier**.
2. *Initialisation* : calculer les deux membres pour $n=n_0$.
3. *Hérédité* : « Soit $n\in\mathbb N^*$ tel que $P(n)$ est vraie. Montrons $P(n+1)$. » Utiliser l'hypothèse en le disant (« par hypothèse de récurrence »).
4. *Conclusion* : « Par récurrence, $P(n)$ est vraie pour tout $n\in\mathbb N^*$. »

## Corrigé du TD
Montrer $\forall n\in\mathbb N^*,\ 1^3+2^3+\dots+n^3=\left(\frac{n(n+1)}2\right)^2$.
$P(n)$ : $1^3+\dots+n^3=\left(\frac{n(n+1)}2\right)^2$.
*Initialisation* : $1^3=1=\left(\frac{1\times2}2\right)^2$, donc $P(1)$ est vraie.
*Hérédité* : soit $n\in\mathbb N^*$ tel que $P(n)$. Par hypothèse de récurrence,
$1^3+\dots+n^3+(n+1)^3=\left(\frac{n(n+1)}2\right)^2+(n+1)^3=(n+1)^2\left(\frac{n^2}4+n+1\right)=(n+1)^2\frac{(n+2)^2}4=\left(\frac{(n+1)(n+2)}2\right)^2$, donc $P(n+1)$.
*Conclusion* : par récurrence, $P(n)$ est vraie pour tout $n\in\mathbb N^*$.

## Pièges
- « Supposons $P(n)$ vraie **pour tout** $n$ » : c'est supposer ce qu'on veut prouver.
- Initialisation oubliée ou faite au mauvais rang.
- Hypothèse de récurrence jamais utilisée : alors la récurrence était inutile ou fausse.

## Teste-toi
1. Montrer $\forall n\in\mathbb N,\ 2^n\geqslant n+1$ : écrire l'hérédité.

## Réponses
1. Soit $n\in\mathbb N$ tel que $2^n\geqslant n+1$. Alors $2^{n+1}=2\cdot2^n\geqslant2(n+1)=2n+2\geqslant n+2$, donc $P(n+1)$.

Source : Cours 6 « Compléments séminaire » (fiches de synthèse, exercices types et corrigés), Moodle S1-MATHS-2031 ; types d'exercices des annales OBM.
