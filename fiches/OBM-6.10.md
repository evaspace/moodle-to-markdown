---
id: OBM-6.10
syllabus: OBM
type: définition
papier: maths-s1-obm/8
prereq: OBM-6.9
alias: union, réunion, intersection, complémentaire, différence, produit cartésien, ensemble des parties, P(E), A \ B, opérations sur les ensembles, De Morgan ensembles
---
# Opérations sur les ensembles

> **À retenir.** $A\cup B=\{x,\ x\in A\text{ ou }x\in B\}$ ; $A\cap B=\{x,\ x\in A\text{ et }x\in B\}$ ; $A\setminus B=\{x\in A,\ x\notin B\}$ ; complémentaire $\overline A=E\setminus A$ ; $A\times B=\{(a,b),\ a\in A,\ b\in B\}$ (couples **ordonnés**) ; $\mathcal P(E)$ = ensemble des parties de $E$. De Morgan : $\overline{A\cup B}=\overline A\cap\overline B$, $\overline{A\cap B}=\overline A\cup\overline B$.

## Méthode en copie
- Calcul sur des ensembles donnés en liste : écrire la liste complète, accolades comprises.
- Égalité générale : traduire en logique (« $x\in A\cup B\iff x\in A$ ou $x\in B$ ») puis appliquer les règles de [OBM-6.3](/cours/fiches/OBM-6.3).

## Corrigé du TD
$A=\{1,\dots,10\}$, $B=\{x\in A,\ x < 5\}=\{1,2,3,4\}$, $C=\{x\in A,\ x > 3\}=\{4,\dots,10\}$, $D$ = pairs $=\{2,4,6,8,10\}$, $E$ = multiples de 3 $=\{3,6,9\}$.
$F=B\cup D=\{1,2,3,4,6,8,10\}$ ; $G=F\cap E=\{3,6\}$ ; $H=A\setminus C=\{1,2,3\}$ ; $H\cap E=\{3\}$ ; $\{3\}\cap D=\emptyset$.
$\{1,2,3\}\times\{3,4\}=\{(1,3),(1,4),(2,3),(2,4),(3,3),(3,4)\}$ et $\{3,4\}\times\{1,2,3\}$ est différent : seul $(3,3)$ est commun.

## Pièges
- $A\times B\neq B\times A$ en général.
- $\mathcal P(\{1,2\})=\{\emptyset,\{1\},\{2\},\{1,2\}\}$ : ne pas oublier $\emptyset$ et l'ensemble lui-même.

## Teste-toi
1. $\{1,2,3\}\setminus\{2,5\}$ ?
2. Combien d'éléments dans $\mathcal P(\{a,b,c\})$ ?

## Réponses
1. $\{1,3\}$. 2. $2^3=8$.

Source : Cours 6 « Compléments séminaire » (fiches de synthèse, exercices types et corrigés), Moodle S1-MATHS-2031 ; types d'exercices des annales OBM.
