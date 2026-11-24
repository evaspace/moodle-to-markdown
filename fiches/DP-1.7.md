---
id: DP-1.7
syllabus: DP
type: théorème
papier: maths-s1-dp/6
prereq: DP-1.5
alias: triangle de Pascal, formule de Pascal, symétrie des coefficients binomiaux, binom(n,k) = binom(n,n-k), propriétés des coefficients binomiaux, k parmi n
---
# Propriétés des coefficients binomiaux, triangle de Pascal

Pour $n \in \mathbb{N}$ et $k \in [\![0, n]\!]$ :

- $\binom{n}{0} = \binom{n}{n} = 1$, et si $n \neq 0$, $\binom{n}{1} = \binom{n}{n-1} = n$ ;
- symétrie : $\binom{n}{k} = \binom{n}{n-k}$ ;
- formule de Pascal : $\binom{n+1}{k} = \binom{n}{k-1} + \binom{n}{k}$ ;
- $k\binom{n}{k} = n\binom{n-1}{k-1}$.

Triangle de Pascal ($n \leqslant 4$) : 1 ; 1 1 ; 1 2 1 ; 1 3 3 1 ; 1 4 6 4 1.

Source : Fiche de synthèse « Dénombrement » (Moodle S1-MATHS-2031, Cours 1).
