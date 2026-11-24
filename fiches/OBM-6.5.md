---
id: OBM-6.5
syllabus: OBM
type: méthode
papier: maths-s1-obm/5
prereq: OBM-6.3, OBM-6.4
alias: nier une phrase quantifiée, négation d'une proposition quantifiée, non pour tout, non il existe, nier une phrase, négation de la convergence
---
# Nier une phrase quantifiée

$$\neg(\forall x, P(x)) \iff \exists x, \neg P(x), \qquad \neg(\exists x, P(x)) \iff \forall x, \neg P(x)$$
Méthode : échanger chaque $\forall$ et $\exists$ en gardant l'ordre et les ensembles, puis nier la proposition finale ($\leqslant$ devient $>$, $\Rightarrow$ devient « et non »).

Exemple : $\neg(\forall \varepsilon > 0, \exists N, \forall n \geqslant N, \lvert u_n - \ell\rvert \leqslant \varepsilon) \iff \exists \varepsilon > 0, \forall N, \exists n \geqslant N, \lvert u_n - \ell\rvert > \varepsilon$.

Source : Cours 6 « Compléments séminaire » et TD séminaire (Moodle S1-MATHS-2031) ; types d'exercices des annales OBM.
