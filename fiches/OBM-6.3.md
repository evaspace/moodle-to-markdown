---
id: OBM-6.3
syllabus: OBM
type: théorème
papier: maths-s1-obm/3
prereq: OBM-6.1
alias: négation, nier, De Morgan, lois de De Morgan, non (P et Q), non (P ou Q), négation d'une implication, P et non Q
---
# Négations, lois de De Morgan

> **À retenir.** $\neg(\neg P)\equiv P$ ; $\neg(P\wedge Q)\equiv\neg P\vee\neg Q$ ; $\neg(P\vee Q)\equiv\neg P\wedge\neg Q$ ; $\neg(P\Rightarrow Q)\equiv P\wedge\neg Q$ (la négation d'une implication n'est **pas** une implication).

## Méthode en copie
1. Repérer le connecteur principal.
2. Appliquer la règle : « et » devient « ou », « ou » devient « et », l'implication devient « $P$ et non $Q$ ».
3. Nier les inégalités : $\neg(x\leqslant2)$ est $x > 2$ (pas $x\geqslant2$).

## Corrigé du TD
- $\neg(x\leqslant2)$ : $x > 2$.
- $\neg(0 < x\leqslant1)$ : $0 < x\leqslant1$ est « $0 < x$ et $x\leqslant1$ », donc sa négation est « $x\leqslant0$ ou $x > 1$ ».

## Pièges
- $\neg(x < 2)$ est $x\geqslant2$ : l'égalité change de camp.
- $\neg(P\Rightarrow Q)$ écrit $\neg P\Rightarrow\neg Q$ : faux.
- Nier un encadrement en un seul encadrement : on obtient un « ou ».

## Teste-toi
1. Nier « $n$ est pair et $n > 10$ ».
2. Nier « s'il pleut, je prends un parapluie ».

## Réponses
1. « $n$ est impair ou $n\leqslant10$ ». 2. « Il pleut et je ne prends pas de parapluie ».

Source : Cours 6 « Compléments séminaire » (fiches de synthèse, exercices types et corrigés), Moodle S1-MATHS-2031 ; types d'exercices des annales OBM.
