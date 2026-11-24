---
id: DP-2.7
syllabus: DP
type: théorème
papier: maths-s1-dp/10
prereq: DP-2.6
alias: Bayes, formule de Bayes, inverser le conditionnement, P(B|A) à partir de P(A|B), test de dépistage, probabilité des causes
---
# Formule de Bayes

$$P(B \mid A) = \frac{P(A \mid B)\,P(B)}{P(A)}$$
Avec une partition $(B_1, \dots, B_n)$, en calculant $P(A)$ par les probabilités totales :
$$P(B_k \mid A) = \frac{P(A \mid B_k)\,P(B_k)}{\sum_{i=1}^n P(A \mid B_i)\,P(B_i)}$$
Exemple type : test de dépistage, probabilité d'être malade sachant le test positif.

Source : Fiches de synthèse « Espace probabilisé », « Probabilités conditionnelles », « Variables aléatoires » (Moodle S1-MATHS-2031, Cours 2).
