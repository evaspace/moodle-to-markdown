# Examen S1B1-LE — octobre 2023 (sujet, FR)

- Source : `raw/S1/Midterms/Maths PC/2028/PC/LE/midterm-2028-s1-maths-subject-fr.pdf` (5 pages)
- Date réelle : octobre 2023 (dossier promo 2028, ECUE LE = logique et ensembles, équivalent OBM 2031). Corrigés : `midterm-2028-s1-maths-correction-fr.md` (FR), `midterm-2028-s1-maths-correction-en.md` (EN).
- Durée : 1 heure. Barème sur 20 points. Rigueur prise en compte, malus d'un point pour manque de propreté. Documents et calculatrices interdits.

## Exercice 1 : équation du second degré (2 points)
Type : équation du second degré dans $\mathbb{C}$ · ECUE : HP (nombres complexes, hors programme 2031)
Formules : $\Delta = b^2 - 4ac$ ; $\Delta < 0$ : $z = \frac{-b \pm i\sqrt{-\Delta}}{2a}$

1. Résoudre dans $\mathbb{C}$ l'équation $2z^2 + 2\sqrt3 z + 2 = 0$. On notera $z_1$ et $z_2$ les deux solutions trouvées.
2. Donner la forme exponentielle de $z_1$ et de $z_2$.

## Exercice 2 : logique (6 points)
Type : quantificateurs, négations, implications · ECUE : OBM · Niveau : maths-s1-obm/5
Formules : s'annule : $\exists x, f(x) = 0$ ; constante : $\exists a, \forall x, f(x) = a$ ; majorée : $\exists M, \forall x, f(x) \leqslant M$ ; $\neg\forall = \exists\neg$ ; $\neg(A \vee B) = \neg A \wedge \neg B$ ; $\neg(f > 0) = (f \leqslant 0)$ ; $P \Rightarrow Q$ équivaut à sa contraposée $\neg Q \Rightarrow \neg P$

Soit $f : \mathbb{R} \to \mathbb{R}$.
1. Traduire les phrases suivantes en syntaxe mathématique (avec les quantificateurs).
   (a) « La fonction $f$ s'annule au moins une fois »
   (b) « La fonction $f$ est constante »
   (c) « La fonction $f$ est majorée »
2. On considère les assertions : $P$ : « $\forall x \in \mathbb{R}, f(x) = 0$ », $Q$ : « $\exists x \in \mathbb{R}, f(x) = 0$ » et $R$ : « $(\forall x \in \mathbb{R}, f(x) > 0) \vee (\forall x \in \mathbb{R}, f(x) < 0)$ ».
   (a) Donner la négation de $P$, de $Q$ et de $R$.
   (b) Cocher dans le tableau suivant les implications vraies : $P \Rightarrow Q$ ; $Q \Rightarrow P$ ; $Q \Rightarrow R$ ; $\neg(Q) \Rightarrow \neg(P)$ ; $\neg(P) \Rightarrow \neg(R)$.

## Exercice 3 : ensembles et fonctions (8 points)
Type : image directe et réciproque, injectivité, surjectivité, composée · ECUE : OBM · Niveau : maths-s1-obm/9
Formules : $f(A) = \{y \in F, \exists x \in A, y = f(x)\}$ ; $f^{-1}(B) = \{x \in E, f(x) \in B\}$ ; injective : $f(x) = f(x') \Rightarrow x = x'$ ; surjective : $\forall y, \exists x, y = f(x)$ ; $g \circ f$ injective si $f$, $g$ injectives ; surjective si $f$, $g$ surjectives

1. Soient $E$ et $F$ deux ensembles, $f : E \to F$, $A \subset E$ et $B \subset F$. Rappeler la définition mathématique des ensembles $f(A)$ et $f^{-1}(B)$.
2. Dessiner (graphe, patate) une fonction $f : \{a, b, c, d\} \to [\![1, 5]\!]$ qui vérifie à la fois $f(\{a, b\}) = \{1, 2\}$, $f^{-1}(\{5\}) = \emptyset$ et $f^{-1}(\{2\}) = \{b, c\}$.
3. Soit $g : \mathbb{R} \to \mathbb{R},\ x \mapsto |x - 1|$.
   (a) Dessiner le graphe de $g$.
   (b) Donner $g(\{-1, 2\})$, $g([-1, 3])$, $g^{-1}(\{1\})$ et $g^{-1}([0, 1])$.
   (c) $g$ est-elle injective ? Justifier. Si non, proposer deux intervalles $I_1$ et $J_1$ pour lesquels $g : I_1 \to J_1$ soit injective.
   (d) $g$ est-elle surjective ? Justifier. Si non, proposer deux intervalles $I_2$ et $J_2$ pour lesquels $g : I_2 \to J_2$ soit surjective.

## Exercice 4 : relations (4 points)
Type : propriétés d'une relation, négation, contraposée · ECUE : OBM · Niveau : maths-s1-obm/11
Formules : réflexive $\forall x, x\mathcal Rx$ ; antisymétrique $x\mathcal Ry \wedge y\mathcal Rx \Rightarrow x = y$ ; transitive ; négation de $\forall(P \Rightarrow Q)$ : $\exists(P \wedge \neg Q)$ ; contraposée de $P \Rightarrow Q$ : $\neg Q \Rightarrow \neg P$ ; $\neg(A \wedge B) = \neg A \vee \neg B$ ; ordre = réflexive + antisymétrique + transitive

Dans $E = \mathbb{N}^*$, on définit la relation $\mathcal{R}$ par : $\forall (a, b) \in E^2$, $a\,\mathcal{R}\,b \iff \exists n \in \mathbb{N}$ tel que $b = a^n$.
1. Dire si $\mathcal{R}$ est réflexive. Justifier.
2. Dire si $\mathcal{R}$ est symétrique. Justifier.
3. Dire si $\mathcal{R}$ est transitive. Justifier.
4. Soit $(a, b) \in E^2$ tels que $a\,\mathcal{R}\,b$ et $b\,\mathcal{R}\,a$.
   (a) Montrer qu'il existe $(n, p) \in \mathbb{N}^2$ tel que $b = b^{np}$.
   (b) En déduire que $b = 1$ ou que $n = p = 1$. Qu'avez-vous finalement démontré ?
