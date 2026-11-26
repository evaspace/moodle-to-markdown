---
id: OBM-6.2
syllabus: OBM
type: définition
papier: maths-s1-obm/2
prereq: OBM-6.1
alias: implication, équivalence, condition nécessaire, condition suffisante, CNS, si et seulement si, ssi, réciproque, P ⇒ Q, non P ou Q
---
# Implication, équivalence, conditions nécessaire et suffisante

> **À retenir.** $P\Rightarrow Q$ est fausse **seulement** quand $P$ est vraie et $Q$ fausse : $P\Rightarrow Q\equiv\neg P\vee Q$. $P\iff Q$ signifie $(P\Rightarrow Q)\wedge(Q\Rightarrow P)$. Dans $P\Rightarrow Q$ : $P$ est une condition **suffisante** pour $Q$, $Q$ est une condition **nécessaire** pour $P$. La **réciproque** de $P\Rightarrow Q$ est $Q\Rightarrow P$ (elle peut être fausse).

## Méthode en copie
- Pour choisir entre $\Rightarrow$, $\Leftarrow$, $\iff$ : tester les deux sens séparément ; un contre-exemple suffit à tuer un sens.
- Pour prouver $P\iff Q$ : deux parties titrées « $\Rightarrow$ » puis « $\Leftarrow$ », ou une chaîne d'équivalences où **chaque** $\iff$ est justifiée.
- Pour prouver $P\Rightarrow Q$ : « Supposons $P$. » … « Donc $Q$. »

## Corrigé du TD
Soit $x\in\mathbb R$. Compléter par $\Rightarrow$, $\Leftarrow$ ou $\iff$.
1. $x^2=2\ \Leftarrow\ x=\sqrt2$ : si $x=\sqrt2$ alors $x^2=2$ ; mais $x=-\sqrt2$ vérifie $x^2=2$ sans être $\sqrt2$.
2. $x>1\ \Rightarrow\ x\geqslant1$ : $x=1$ vérifie $x\geqslant1$ mais pas $x>1$.
3. $e^x=1\ \iff\ x=0$ : $\exp$ est injective et $e^0=1$.

## Pièges
- Écrire $\iff$ dans une résolution alors qu'on a élevé au carré (on perd l'équivalence : $x=\sqrt{x+2}\Rightarrow x^2=x+2$ seulement).
- Confondre réciproque ($Q\Rightarrow P$) et contraposée ($\neg Q\Rightarrow\neg P$).
- « Nécessaire » et « suffisant » inversés : « il suffit d'être parisien pour être français » : parisien $\Rightarrow$ français.

## Teste-toi
1. Vrai ou faux : « $x^2 > 4\Rightarrow x > 2$ » pour $x\in\mathbb R$ ?
2. Pour qu'un entier soit divisible par 4, être pair est une condition nécessaire ou suffisante ?

## Réponses
1. Faux : $x=-3$. 2. Nécessaire (divisible par 4 $\Rightarrow$ pair), pas suffisante ($6$).

Source : Cours 6 « Compléments séminaire » (fiches de synthèse, exercices types et corrigés), Moodle S1-MATHS-2031 ; types d'exercices des annales OBM.
