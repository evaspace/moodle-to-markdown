# Contrôle TD 1 de mathématiques S1 — lundi 18 octobre 2021 (sujet, FR)

- Source : `raw/S1/TDs/2026/td1-2026-s1-maths-subject-fr.pdf` (scan, 2 pages)
- Date réelle : 18 octobre 2021 (dossier promo 2026). Corrigé non officiel (étudiant) : `td1-2026-s1-maths-correction-fr.md`.
- Durée : 45 minutes. Barème sur 10, ramené sur 20.

## Questions de cours (3 points)
Type : injectivité / surjectivité, restriction · ECUE : OBM · Niveau : maths-s1-obm/10
Formules : injective $\iff$ toute droite horizontale coupe le graphe au plus une fois ; surjective sur $F$ $\iff$ tout $y \in F$ est atteint ; $(x-2)^2 - 1 \geqslant -1$ ; restreindre le départ à $[2, +\infty[$ rend injective, l'arrivée à $[-1, +\infty[$ rend surjective

Soient $E$ et $F$ deux ensembles et $f : E \to F$. Rappeler la définition mathématique (avec les quantificateurs) de :
1. $f$ est injective.
2. $f$ est surjective.
3. Application : la fonction $f : \mathbb{R} \to \mathbb{R},\ x \mapsto x^2 - 1$ est-elle injective ? surjective ? Justifiez vos réponses.

## Exercice 1 (3 points)
Type : vérité, négation et contraposée d'une implication quantifiée · ECUE : OBM · Niveau : maths-s1-obm/6
Formules : $x^2 - 3x + 2 = (x-1)(x-2) \leqslant 0 \iff x \in [1, 2]$ ; implication vraie $\iff$ inclusion des ensembles ; $\neg(\forall x, A \Rightarrow B) = \exists x, A \wedge \neg B$ ; contraposée $\neg B \Rightarrow \neg A$ ; $\neg(x \leqslant 1 \vee x \geqslant 2) = (x > 1 \wedge x < 2)$

On considère l'assertion $P$ : « $\forall x \in \mathbb{R}$, $(x^2 - 3x + 2 \leqslant 0 \implies (x \leqslant 1 \vee x \geqslant 2))$ ».
1. Cette assertion est-elle vraie ou fausse ? Justifiez votre réponse.
2. Donner la négation de $P$.
3. Donner la contraposée de $P$.

## Exercice 2 (2,5 points)
Type : IPP : polynôme × sin/cos · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/7
Formules : IPP $\int_a^b uv' = [uv]_a^b - \int_a^b u'v$ ; $u = x$, $u' = 1$ ; $v' = \sin(kx)$, $v = -\frac{\cos(kx)}k$ ; $\int \cos(kx) = \frac{\sin(kx)}k$ ; $\cos\pi = -1$, $\cos\frac\pi2 = 0$, $\sin\frac\pi2 = 1$

En intégrant par parties, calculer $I = \displaystyle\int_0^{\pi/6} x\sin(3x)\,dx$. Vous ferez clairement apparaître les fonctions mises en jeu ainsi que leurs dérivées et/ou primitives.

## Exercice 3 (1,5 points)
Type : p-listes, complémentaire · ECUE : DP · Niveau : maths-s1-dp/2
Formules : $p$-listes de $n$ éléments : $n^p$ ; « au moins un » = total $-$ « aucun » : $n^p - (n-1)^p$ ; premier chiffre fixé non réutilisé : $(n-1)^{p-1}$

On considère l'ensemble $E$ des nombres à trois chiffres choisis dans $\{1, 2, 3, 4, 5\}$, chaque chiffre pouvant être répété.
1. Quel est le cardinal de $E$ ?
2. Quel est le nombre d'éléments de $E$ dans lesquels le chiffre 1 apparaît au moins une fois ?
3. Quel est le nombre d'éléments de $E$ commençant par le chiffre 1, ce chiffre n'étant pas réutilisé par la suite ?
