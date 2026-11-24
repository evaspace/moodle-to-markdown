---
id: DP-1.6
syllabus: DP
type: méthode
papier: maths-s1-dp/5
prereq: DP-1.1, DP-1.5
alias: au moins un, au plus, complémentaire, passer au contraire, mais pas, contraintes, compter le contraire
---
# Dénombrer avec contraintes : passer au complémentaire

« Au moins un » : compter le contraire « aucun » puis soustraire.
$$\mathrm{Card}(\text{au moins un}) = \mathrm{Card}(\text{tout}) - \mathrm{Card}(\text{aucun})$$

« A mais pas B » : $\mathrm{Card}(A \setminus B) = \mathrm{Card}(A) - \mathrm{Card}(A \cap B)$.

Exemple : codes de 4 chiffres avec au moins un 0 : $10^4 - 9^4$.

Source : Fiche de synthèse « Dénombrement » (Moodle S1-MATHS-2031, Cours 1).
