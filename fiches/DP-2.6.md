---
id: DP-2.6
syllabus: DP
type: théorème
papier: maths-s1-dp/9
prereq: DP-2.1, DP-2.5
alias: probabilités totales, formule des probabilités totales, système complet, partition, arbre pondéré, somme des branches
---
# Formule des probabilités totales

Soit $(B_1, \dots, B_n)$ une partition de $\Omega$ avec $P(B_i) \neq 0$. Pour tout évènement $A$ :
$$P(A) = \sum_{i=1}^{n} P(A \mid B_i)\,P(B_i)$$
Cas $n = 2$ : $P(A) = P(A \mid B)P(B) + P(A \mid \overline{B})P(\overline{B})$.

Méthode : nommer la partition, écrire $A = \bigsqcup (A \cap B_i)$, puis sommer les branches de l'arbre qui mènent à $A$.

Source : Fiches de synthèse « Espace probabilisé », « Probabilités conditionnelles », « Variables aléatoires » (Moodle S1-MATHS-2031, Cours 2).
