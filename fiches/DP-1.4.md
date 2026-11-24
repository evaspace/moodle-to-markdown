---
id: DP-1.4
syllabus: DP
type: théorème
papier: maths-s1-dp/3
prereq: DP-1.2, DP-1.3
alias: arrangement, A(n,p), Anp, permutation, n!, tirage sans remise ordonné, p-uplet sans répétition, injections, anagramme, podium, classement, dénombrement, dénombrements de référence
---
# Arrangements et permutations

Si $p \leqslant n$, nombre de $p$-uplets **sans répétition** d'éléments d'un ensemble à $n$ éléments (tirage ordonné sans remise) :
$$A_n^p = n(n-1)\cdots(n-p+1) = \frac{n!}{(n-p)!}$$
C'est aussi le nombre d'injections d'un ensemble à $p$ éléments dans un ensemble à $n$ éléments.

Permutations de $F$ ($p = n$) : $n!$.

Anagrammes d'un mot de $n$ lettres où les lettres se répètent $k_1, k_2, \dots$ fois : $\dfrac{n!}{k_1!\,k_2!\cdots}$.

Source : Fiche de synthèse « Dénombrement » (Moodle S1-MATHS-2031, Cours 1).
