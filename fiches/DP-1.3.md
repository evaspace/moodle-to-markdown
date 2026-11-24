---
id: DP-1.3
syllabus: DP
type: théorème
papier: maths-s1-dp/2
prereq: DP-1.1
alias: p-liste, p-uplet, n puissance p, n^p, tirage avec remise, principe multiplicatif, nombre d'applications, digicode, code, mot de passe, dénombrement, dénombrements de référence
---
# p-listes et principe multiplicatif

Principe multiplicatif : un choix en $k$ étapes indépendantes, avec $n_1, \dots, n_k$ possibilités, donne $n_1 \times \dots \times n_k$ résultats.

Avec $\mathrm{Card}(E) = p$ et $\mathrm{Card}(F) = n$ :

- nombre de $p$-listes (p-uplets) d'éléments de $F$ : $n^p$ ;
- nombre d'applications de $E$ dans $F$ : $\mathrm{Card}(F^E) = n^p$.

Modèle : tirage **ordonné avec remise** de $p$ éléments parmi $n$ (digicode, mot de passe).

Source : Fiche de synthèse « Dénombrement » (Moodle S1-MATHS-2031, Cours 1).
