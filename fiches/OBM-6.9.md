---
id: OBM-6.9
syllabus: OBM
type: définition
papier: maths-s1-obm/8
prereq: OBM-6.4
alias: ensemble, appartenance, inclusion, sous-ensemble, partie, égalité d'ensembles, double inclusion, ensemble vide, ⊂, ∈
---
# Ensembles : appartenance, inclusion, égalité

> **À retenir.** $x\in A$ : $x$ est un élément de $A$. $A\subset B$ : $\forall x,\ (x\in A\Rightarrow x\in B)$. $A=B\iff A\subset B$ et $B\subset A$ (**double inclusion**). $\emptyset$ est inclus dans tout ensemble. $\{x\in A,\ P(x)\}$ : les éléments de $A$ qui vérifient $P$.

## Méthode en copie
- Prouver $A\subset B$ : « Soit $x\in A$. » … « Donc $x\in B$. Ainsi $A\subset B$. »
- Prouver $A=B$ : deux paragraphes, $A\subset B$ puis $B\subset A$.
- Ne pas confondre $\in$ (élément) et $\subset$ (partie) : $1\in\{1,2\}$ mais $\{1\}\subset\{1,2\}$.

## Corrigé du TD
Montrer que $A\cap B=A\cup B\iff A=B$.
*$\Leftarrow$* : si $A=B$, $A\cap B=A=A\cup B$.
*$\Rightarrow$* : supposons $A\cap B=A\cup B$. Soit $x\in A$. Alors $x\in A\cup B=A\cap B$, donc $x\in B$ : $A\subset B$. De même, si $x\in B$, $x\in A\cup B=A\cap B$, donc $x\in A$ : $B\subset A$. Donc $A=B$.

## Pièges
- $\{1\}\in\{1,2\}$ est faux ; $\emptyset\in A$ est en général faux, $\emptyset\subset A$ est vrai.
- Prouver une seule inclusion et conclure à l'égalité.

## Teste-toi
1. $A=\{1,2,\dots,10\}$. Lister $\{x\in A,\ x\text{ multiple de }3\}$.
2. Vrai ou faux : $\{2\}\subset\{\{2\},3\}$ ?

## Réponses
1. $\{3,6,9\}$. 2. Faux : $2$ n'est pas un élément de $\{\{2\},3\}$ (c'est $\{2\}$ qui en est un).

Source : Cours 6 « Compléments séminaire » (fiches de synthèse, exercices types et corrigés), Moodle S1-MATHS-2031 ; types d'exercices des annales OBM.
