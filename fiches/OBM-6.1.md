---
id: OBM-6.1
syllabus: OBM
type: définition
papier: maths-s1-obm/1
prereq: 
alias: proposition, assertion, connecteurs logiques, et, ou, non, table de vérité, valeur de vérité, ou inclusif
---
# Propositions, connecteurs, tables de vérité

> **À retenir.** Une proposition est vraie (V) ou fausse (F), jamais les deux. $\neg P$ (non), $P\wedge Q$ (et : vraie seulement si les deux le sont), $P\vee Q$ (ou **inclusif** : fausse seulement si les deux sont fausses). Deux propositions sont **équivalentes** ($\equiv$) si elles ont la même table de vérité.

| $P$ | $Q$ | $\neg P$ | $P \wedge Q$ | $P \vee Q$ | $P \Rightarrow Q$ |
|---|---|---|---|---|---|
| V | V | F | V | V | V |
| V | F | F | F | V | F |
| F | V | V | F | V | V |
| F | F | V | F | F | V |

## Méthode en copie
1. Une colonne par proposition de base, $2^n$ lignes pour $n$ propositions (4 lignes pour $P,Q$ ; 8 pour $P,Q,R$).
2. Une colonne par sous-expression, de l'intérieur vers l'extérieur.
3. Comparer les deux colonnes finales ligne par ligne, puis conclure par une phrase.

## Corrigé du TD
Vérifier $\neg(P\Rightarrow Q)\equiv P\wedge\neg Q$.

| $P$ | $Q$ | $\neg Q$ | $P\Rightarrow Q$ | $\neg(P\Rightarrow Q)$ | $P\wedge\neg Q$ |
|---|---|---|---|---|---|
| V | V | F | V | F | F |
| V | F | V | F | V | V |
| F | V | F | V | F | F |
| F | F | V | V | F | F |

Les deux dernières colonnes sont identiques, donc $\neg(P\Rightarrow Q)\equiv P\wedge\neg Q$.

## Pièges
- « ou » est inclusif : $P\vee Q$ est vraie quand $P$ et $Q$ sont toutes deux vraies.
- $P\Rightarrow Q$ est **vraie** quand $P$ est fausse (lignes 3 et 4).
- Oublier une ligne : avec 3 propositions il faut 8 lignes.

## Teste-toi
1. Combien de lignes pour la table de $(P\wedge Q)\vee R$ ?
2. $P$ fausse, $Q$ vraie : que vaut $P\vee\neg Q$ ?

## Réponses
1. $2^3=8$ lignes. 2. $\neg Q$ est fausse et $P$ est fausse, donc $P\vee\neg Q$ est fausse.

Source : Cours 6 « Compléments séminaire » (fiches de synthèse, exercices types et corrigés), Moodle S1-MATHS-2031 ; types d'exercices des annales OBM.
