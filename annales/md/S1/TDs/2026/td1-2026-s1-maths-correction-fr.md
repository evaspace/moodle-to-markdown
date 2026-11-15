# Contrôle TD 1 de mathématiques S1 — 18 octobre 2021 (correction non officielle)

- Source : `raw/S1/TDs/2026/td1-2026-s1-maths-correction-fr.pdf` (scan d'une copie manuscrite, 2 pages, titrée « correction non officielle »)
- Date réelle : 18 octobre 2021 (dossier promo 2026). Sujet : `td1-2026-s1-maths-subject-fr.md`.

## Questions de cours (3 points)
Type : injectivité / surjectivité, restriction · ECUE : OBM · Niveau : maths-s1-obm/10
Formules : injective $\iff$ toute droite horizontale coupe le graphe au plus une fois ; surjective sur $F$ $\iff$ tout $y \in F$ est atteint ; $(x-2)^2 - 1 \geqslant -1$ ; restreindre le départ à $[2, +\infty[$ rend injective, l'arrivée à $[-1, +\infty[$ rend surjective

1. $f$ injective : $\forall (x_1, x_2) \in E^2$, $x_1 \neq x_2 \implies f(x_1) \neq f(x_2)$.
2. $f$ surjective : $\forall y \in F, \exists x \in E, y = f(x)$.
3. $f(-2) = (-2)^2 - 1 = 3$ et $f(2) = 3$ ; $-2 \neq 2$ et $f(-2) = f(2)$ : $f$ n'est pas injective. $f$ n'atteint pas la valeur $-3$ (car $x^2 - 1 \geqslant -1$), or $-3 \in \mathbb{R}$ : $f$ n'est pas surjective.

## Exercice 1 (3 points)
Type : vérité, négation et contraposée d'une implication quantifiée · ECUE : OBM · Niveau : maths-s1-obm/6
Formules : $x^2 - 3x + 2 = (x-1)(x-2) \leqslant 0 \iff x \in [1, 2]$ ; implication vraie $\iff$ inclusion des ensembles ; $\neg(\forall x, A \Rightarrow B) = \exists x, A \wedge \neg B$ ; contraposée $\neg B \Rightarrow \neg A$ ; $\neg(x \leqslant 1 \vee x \geqslant 2) = (x > 1 \wedge x < 2)$

1. $x^2 - 3x + 2$ : $\Delta = 9 - 8 = 1$, racines $x_1 = 1$ et $x_2 = 2$ ; $x^2 - 3x + 2 \leqslant 0 \iff x \in [1, 2]$. Or $(x \leqslant 1 \vee x \geqslant 2) \iff x \in ]-\infty, 1] \cup [2, +\infty[$ et $[1, 2] \not\subset ]-\infty, 1] \cup [2, +\infty[$ (par exemple $x = 1{,}5$) : l'assertion est fausse.
2. $\neg P$ : « $\exists x \in \mathbb{R}$, $(x^2 - 3x + 2 \leqslant 0) \wedge (x > 1 \wedge x < 2)$ ».
3. Contraposée : « $\forall x \in \mathbb{R}$, $(x > 1 \wedge x < 2) \implies x^2 - 3x + 2 > 0$ ».

## Exercice 2 (2,5 points)
Type : IPP : polynôme × sin/cos · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/7
Formules : IPP $\int_a^b uv' = [uv]_a^b - \int_a^b u'v$ ; $u = x$, $u' = 1$ ; $v' = \sin(kx)$, $v = -\frac{\cos(kx)}k$ ; $\int \cos(kx) = \frac{\sin(kx)}k$ ; $\cos\pi = -1$, $\cos\frac\pi2 = 0$, $\sin\frac\pi2 = 1$

$\int_a^b u(x)v'(x)\,dx = [u(x)v(x)]_a^b - \int_a^b u'(x)v(x)\,dx$. On pose $u(x) = x$, $u'(x) = 1$, $v'(x) = \sin(3x)$, $v(x) = -\frac13\cos(3x)$.
$I = \left[-\frac13x\cos(3x)\right]_0^{\pi/6} + \frac13\displaystyle\int_0^{\pi/6} \cos(3x)\,dx = -\frac{\pi}{18}\cos\frac\pi2 + \frac13\left[\frac13\sin(3x)\right]_0^{\pi/6} = 0 + \frac19 = \frac19$.

## Exercice 3 (1,5 points)
Type : p-listes, complémentaire · ECUE : DP · Niveau : maths-s1-dp/2
Formules : $p$-listes de $n$ éléments : $n^p$ ; « au moins un » = total $-$ « aucun » : $n^p - (n-1)^p$ ; premier chiffre fixé non réutilisé : $(n-1)^{p-1}$

1. Avec répétition : $\mathrm{Card}(E) = 5 \times 5 \times 5 = 5^3 = 125$.
2. Événement contraire « pas de chiffre 1 » : $5^3 - 4 \times 4 \times 4 = 5^3 - 4^3 = 61$.
3. $1 \times 4 \times 4 = 4^2 = 16$.
