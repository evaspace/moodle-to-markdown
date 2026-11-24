---
id: APIS-4.12
syllabus: APIS
type: théorème
papier: maths-s1-apis-suites/9
prereq: APIS-4.11
alias: suites adjacentes, u croissante v décroissante, v_n - u_n tend vers 0, même limite, encadrement de la limite, somme 1/k!, e
---
# Suites adjacentes

$(u_n)$ et $(v_n)$ sont adjacentes si $(u_n)$ est croissante, $(v_n)$ décroissante et $v_n - u_n \to 0$.

Théorème : elles convergent vers une même limite $\ell$ et $\forall n, u_n \leqslant u_{n+1} \leqslant \ell \leqslant v_{n+1} \leqslant v_n$.

Exemple classique : $u_n = \sum_{k=0}^{n} \frac{1}{k!}$ et $v_n = u_n + \frac{1}{n \cdot n!}$ (limite $e$). Les suites $(u_{2n})$ et $(u_{2n+1})$ d'une somme alternée sont souvent adjacentes.

Source : Fiches « Théorèmes de convergence », « Comparaisons asymptotiques » et TD4 (Moodle S1-MATHS-2031, Cours 4).
