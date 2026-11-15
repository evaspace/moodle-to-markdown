# Correction examen S1B1-LE — octobre 2023

- Source : `raw/S1/Midterms/Maths PC/2028/PC/LE/midterm-2028-s1-maths-correction-fr.pdf` (2 pages)
- Date réelle : octobre 2023 (dossier promo 2028). Sujet : `midterm-2028-s1-maths-subject-fr.md`.

## Exercice 1 : équation du second degré
Type : équation du second degré dans $\mathbb{C}$ · ECUE : HP (nombres complexes, hors programme 2031)
Formules : $\Delta = b^2 - 4ac$ ; $\Delta < 0$ : $z = \frac{-b \pm i\sqrt{-\Delta}}{2a}$

1. $\Delta = 12 - 16 = -4$. $z_1 = \dfrac{-2\sqrt3 + 2i}4 = -\dfrac{\sqrt3}2 + \dfrac12 i$ et $z_2 = \overline{z_1} = -\dfrac{\sqrt3}2 - \dfrac12 i$.
2. $|z_1| = |z_2| = 1$ ; $z_1 = e^{i\frac{5\pi}6}$ et $z_2 = e^{i\frac{7\pi}6}$ (le corrigé écrit $z_1$ deux fois).

## Exercice 2 : logique
Type : quantificateurs, négations, implications · ECUE : OBM · Niveau : maths-s1-obm/5
Formules : s'annule : $\exists x, f(x) = 0$ ; constante : $\exists a, \forall x, f(x) = a$ ; majorée : $\exists M, \forall x, f(x) \leqslant M$ ; $\neg\forall = \exists\neg$ ; $\neg(A \vee B) = \neg A \wedge \neg B$ ; $\neg(f > 0) = (f \leqslant 0)$ ; $P \Rightarrow Q$ équivaut à sa contraposée $\neg Q \Rightarrow \neg P$

1. (a) $\exists x \in \mathbb{R}, f(x) = 0$. (b) $\exists a \in \mathbb{R}, \forall x \in \mathbb{R}, f(x) = a$. (c) $\exists M \in \mathbb{R}, \forall x \in \mathbb{R}, f(x) \leqslant M$.
2. (a) $\neg P$ : « $\exists x \in \mathbb{R}, f(x) \neq 0$ » ; $\neg Q$ : « $\forall x \in \mathbb{R}, f(x) \neq 0$ » ; $\neg R$ : « $(\exists x \in \mathbb{R}, f(x) \leqslant 0) \wedge (\exists x \in \mathbb{R}, f(x) \geqslant 0)$ ».
(b) Implications vraies : $P \Rightarrow Q$ et $\neg(Q) \Rightarrow \neg(P)$ (contraposée de la première).

## Exercice 3 : ensembles et fonctions
Type : image directe et réciproque, injectivité, surjectivité, composée · ECUE : OBM · Niveau : maths-s1-obm/9
Formules : $f(A) = \{y \in F, \exists x \in A, y = f(x)\}$ ; $f^{-1}(B) = \{x \in E, f(x) \in B\}$ ; injective : $f(x) = f(x') \Rightarrow x = x'$ ; surjective : $\forall y, \exists x, y = f(x)$ ; $g \circ f$ injective si $f$, $g$ injectives ; surjective si $f$, $g$ surjectives

1. $f(A) = \{f(x) ; x \in A\}$ et $f^{-1}(B) = \{x \in E ; f(x) \in B\}$.
2. Par exemple $f(a) = 1$, $f(b) = 2$, $f(c) = 2$ et $f(d) = 4$.
3. (a) Graphe en V de sommet $(1, 0)$.
(b) $g(\{-1, 2\}) = \{2, 1\}$, $g([-1, 3]) = [0, 2]$, $g^{-1}(\{1\}) = \{0, 2\}$ et $g^{-1}([0, 1]) = [0, 2]$.
(c) $g(0) = g(2) = 1$ et $0 \neq 2$ : $g$ n'est pas injective. Avec $I_1 = [1, +\infty[$ et $J_1 = \mathbb{R}$, $g$ est injective.
(d) $-2$ n'a pas d'antécédent : $g$ n'est pas surjective. Avec $I_2 = \mathbb{R}$ et $J_2 = \mathbb{R}^+$, $g$ est surjective.

## Exercice 4 : relations
Type : propriétés d'une relation, négation, contraposée · ECUE : OBM · Niveau : maths-s1-obm/11
Formules : réflexive $\forall x, x\mathcal Rx$ ; antisymétrique $x\mathcal Ry \wedge y\mathcal Rx \Rightarrow x = y$ ; transitive ; négation de $\forall(P \Rightarrow Q)$ : $\exists(P \wedge \neg Q)$ ; contraposée de $P \Rightarrow Q$ : $\neg Q \Rightarrow \neg P$ ; $\neg(A \wedge B) = \neg A \vee \neg B$ ; ordre = réflexive + antisymétrique + transitive

1. $a = a^1$ d'où $a\,\mathcal{R}\,a$ : réflexive.
2. $8 = 2^3$ d'où $2\,\mathcal{R}\,8$, mais 2 n'est pas une puissance de 8 : pas symétrique.
3. Si $b = a^n$ et $c = b^p$ alors $c = a^{np}$ : transitive.
4. (a) $b = a^n$ et $a = b^p$, donc $b = b^{np}$.
(b) $b = b^{np} \implies b = 1$ ou $np = 1$ ; $n$ et $p$ entiers naturels donc $n = p = 1$. Si $b = 1$ alors $a = 1$ ; sinon $b = a^1 = a$. Dans tous les cas $a = b$ : la relation est antisymétrique (donc $\mathcal{R}$ est une relation d'ordre).
