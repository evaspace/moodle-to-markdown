---
id: APIS-4.14
syllabus: APIS
type: méthode
papier: maths-s1-apis-suites/10
prereq: APIS-4.11, OBM-6.8
alias: suite récurrente, u_(n+1) = f(u_n), intervalle stable, point fixe, f(l) = l, suite définie par récurrence, étude d'une suite récurrente, f croissante, toile d'araignée
---
# Suites récurrentes u(n+1) = f(u(n))

Plan d'étude :

1. Intervalle stable $I$ ($f(I) \subset I$) et $u_0 \in I$ : par récurrence, $u_n \in I$ pour tout $n$ (la suite est bien définie et bornée).
2. Monotonie : si $f$ est croissante sur $I$, $(u_n)$ est monotone (sens donné par $u_1 - u_0$) ; sinon signe de $f(x) - x$.
3. Convergence par la limite monotone.
4. Si $f$ est continue et $u_n \to \ell \in I$, alors $f(\ell) = \ell$ : la limite est un point fixe.

Exemple : $u_0 = 0$, $u_{n+1} = \sqrt{1 + u_n}$, $I = [0, 2]$.

Source : Fiches « Théorèmes de convergence », « Comparaisons asymptotiques » et TD4 (Moodle S1-MATHS-2031, Cours 4).
