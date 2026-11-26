---
id: OBM-6.19
syllabus: OBM
type: définition
papier: maths-s1-obm/11
prereq: OBM-6.10
alias: relation binaire, relation d'ordre, relation d'équivalence, réflexive, symétrique, antisymétrique, transitive, classe d'équivalence, ordre total
---
# Relations binaires : ordre et équivalence

> **À retenir.** Une relation $\mathcal R$ sur $E$ est **réflexive** ($\forall x,\ x\mathcal Rx$), **symétrique** ($x\mathcal Ry\Rightarrow y\mathcal Rx$), **antisymétrique** ($x\mathcal Ry$ et $y\mathcal Rx\Rightarrow x=y$), **transitive** ($x\mathcal Ry$ et $y\mathcal Rz\Rightarrow x\mathcal Rz$). **Équivalence** = réflexive, symétrique, transitive. **Ordre** = réflexive, antisymétrique, transitive ; ordre **total** si deux éléments sont toujours comparables.

## Méthode en copie
- Une propriété par paragraphe, titrée, chacune prouvée pour des éléments **quelconques** (« Soient $x,y\in E$ tels que… »).
- Pour une équivalence, décrire les classes : $\bar x=\{y\in E,\ y\mathcal Rx\}$.

## Corrigé du cours
Sur $\mathbb Z$, $x\mathcal Ry\iff x-y$ pair.
*Réflexive* : $x-x=0$ est pair. *Symétrique* : si $x-y=2k$, $y-x=2(-k)$. *Transitive* : si $x-y=2k$ et $y-z=2l$, $x-z=2(k+l)$.
C'est une relation d'équivalence, de classes : les pairs et les impairs.

## Pièges
- Antisymétrique n'est pas « non symétrique ».
- Prouver sur un exemple au lieu d'éléments quelconques.

## Teste-toi
1. $\leqslant$ sur $\mathbb R$ : ordre ? total ?
2. « divise » sur $\mathbb N^*$ : ordre total ?

## Réponses
1. Ordre total. 2. Ordre, non total ($2$ et $3$ ne sont pas comparables).

Source : Cours 6 « Compléments séminaire » (fiches de synthèse, exercices types et corrigés), Moodle S1-MATHS-2031 ; types d'exercices des annales OBM.
