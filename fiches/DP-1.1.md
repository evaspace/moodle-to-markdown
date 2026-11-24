---
id: DP-1.1
syllabus: DP
type: définition
papier: maths-s1-dp/1
prereq: 
alias: cardinal, card, nombre d'éléments, union disjointe, réunion, formule du crible, card(A ∪ B), partition
---
# Cardinal d'un ensemble fini

Le cardinal $\mathrm{Card}(E)$ d'un ensemble fini $E$ est son nombre d'éléments.

Pour $A$, $B$ finis :

- si $A \cap B = \emptyset$ : $\mathrm{Card}(A \sqcup B) = \mathrm{Card}(A) + \mathrm{Card}(B)$ ;
- toujours : $\mathrm{Card}(A \cup B) = \mathrm{Card}(A) + \mathrm{Card}(B) - \mathrm{Card}(A \cap B)$ ;
- si $A_1, \dots, A_n$ sont deux à deux disjoints : $\mathrm{Card}(A_1 \sqcup \dots \sqcup A_n) = \sum_{k=1}^n \mathrm{Card}(A_k)$.

Complémentaire dans $E$ : $\mathrm{Card}(\overline{A}) = \mathrm{Card}(E) - \mathrm{Card}(A)$.

Source : Fiche de synthèse « Dénombrement » (Moodle S1-MATHS-2031, Cours 1).
