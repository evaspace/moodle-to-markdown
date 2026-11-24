---
id: DP-1.5
syllabus: DP
type: théorème
papier: maths-s1-dp/4
prereq: DP-1.4
alias: combinaison, coefficient binomial, k parmi n, n choose k, binom, parties à p éléments, sous-ensembles, tirage simultané, main de cartes, comité, dénombrement, dénombrements de référence
---
# Combinaisons

Nombre de parties à $k$ éléments d'un ensemble à $n$ éléments (tirage **simultané**, sans ordre ni remise) :
$$\binom{n}{k} = \frac{n!}{k!\,(n-k)!} = \frac{A_n^k}{k!}, \qquad k \in [\![0, n]\!]$$

Mains de cartes : choisir chaque « couleur » ou « hauteur » séparément puis multiplier, par exemple une main de 5 cartes avec exactement 2 as dans un jeu de 32 : $\binom{4}{2}\binom{28}{3}$.

Source : Fiche de synthèse « Dénombrement » (Moodle S1-MATHS-2031, Cours 1).
