---
id: DP-2.5
syllabus: DP
type: théorème
papier: maths-s1-dp/8
prereq: DP-2.4
alias: probabilités composées, intersection de n évènements, formule des probabilités composées, arbre, tirages successifs sans remise, urne
---
# Formule des probabilités composées

Si $P(A_1 \cap \dots \cap A_{n-1}) \neq 0$ :
$$P(A_1 \cap \dots \cap A_n) = P(A_1)\,P(A_2 \mid A_1)\,P(A_3 \mid A_1 \cap A_2) \cdots P(A_n \mid A_1 \cap \dots \cap A_{n-1})$$
C'est le produit des probabilités le long d'une branche d'arbre (tirages successifs).

Source : Fiches de synthèse « Espace probabilisé », « Probabilités conditionnelles », « Variables aléatoires » (Moodle S1-MATHS-2031, Cours 2).
