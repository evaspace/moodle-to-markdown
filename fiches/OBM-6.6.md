---
id: OBM-6.6
syllabus: OBM
type: théorème
papier: maths-s1-obm/6
prereq: OBM-6.2, OBM-6.3
alias: contraposée, raisonnement par contraposition, non Q ⇒ non P, contraposée d'une implication quantifiée, n² pair implique n pair
---
# Contraposée

> **À retenir.** $P\Rightarrow Q\ \equiv\ \neg Q\Rightarrow\neg P$ (contraposée). Elle a **toujours** la même valeur de vérité que l'implication. La réciproque $Q\Rightarrow P$, elle, peut être fausse.

## Méthode en copie
1. Annoncer : « Raisonnons par contraposée : montrons $\neg Q\Rightarrow\neg P$. »
2. « Supposons $\neg Q$. » … « Donc $\neg P$. »
3. Conclure : « Par contraposée, $P\Rightarrow Q$. »
À utiliser quand $Q$ est une **non-égalité** ($x\neq y$) ou une phrase négative : sa négation est une égalité, plus facile à exploiter.

## Corrigé du TD
Soit $(x,y)\in(\mathbb R^{+*})^2$. Montrer que si $x\neq y$, alors $\ln x\neq\ln y$.
Raisonnons par contraposée. Supposons $\ln x=\ln y$. En appliquant $\exp$ : $e^{\ln x}=e^{\ln y}$, c'est-à-dire $x=y$.
Par contraposée, $x\neq y\Rightarrow\ln x\neq\ln y$.

## Pièges
- Écrire la réciproque ($\ln x\neq\ln y\Rightarrow x\neq y$) au lieu de la contraposée.
- Oublier d'annoncer la méthode : le correcteur ne sait pas ce que tu prouves.

## Teste-toi
1. Contraposée de « $n^2$ pair $\Rightarrow n$ pair ».
2. La prouver.

## Réponses
1. « $n$ impair $\Rightarrow n^2$ impair ». 2. $n=2k+1$, $n^2=4k^2+4k+1=2(2k^2+2k)+1$ est impair.

Source : Cours 6 « Compléments séminaire » (fiches de synthèse, exercices types et corrigés), Moodle S1-MATHS-2031 ; types d'exercices des annales OBM.
