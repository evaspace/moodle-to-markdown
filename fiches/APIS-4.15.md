---
id: APIS-4.15
syllabus: APIS
type: définition
papier: maths-s1-apis-suites/12
prereq: APIS-4.6
alias: négligeable, petit o, o(v_n), dominée, grand O, O(v_n), comparaison de Landau, comparaison asymptotique, u_n/v_n tend vers 0, comparaisons de suites, comparaison asymptotique de suites
---
# Négligeabilité et domination : o et O

- $u_n = o(v_n)$ ($u$ négligeable devant $v$) : $u_n = \varepsilon_n v_n$ avec $\varepsilon_n \to 0$ ; si $v_n \neq 0$ : $\dfrac{u_n}{v_n} \to 0$.
- $u_n = O(v_n)$ ($u$ dominée par $v$) : $u_n = b_n v_n$ avec $(b_n)$ bornée ; si $v_n \neq 0$ : $\dfrac{u_n}{v_n}$ bornée.
- $u_n = o(v_n) \Rightarrow u_n = O(v_n)$ ; $u_n = o(1) \iff u_n \to 0$.

Croissances comparées en notation $o$ : $\ln n = o(n)$, $n^b = o(q^n)$ pour $q > 1$.

Source : Fiches « Théorèmes de convergence », « Comparaisons asymptotiques » et TD4 (Moodle S1-MATHS-2031, Cours 4).
