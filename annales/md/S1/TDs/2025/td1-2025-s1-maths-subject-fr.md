# Contrôle TD 1 (S1) — lundi 19 octobre 2020 (sujet, FR)

- Source : `raw/S1/TDs/2025/td1-2025-s1-maths-subject-fr.pdf` (2 pages)
- Date réelle : 19 octobre 2020 (dossier promo 2025). Corrigé rédigé : `td1-2025-s1-maths-correction-fr.md` (même dossier).

## Questions de cours
Type : image directe et réciproque, injectivité, surjectivité, composée · ECUE : OBM · Niveau : maths-s1-obm/10
Formules : $f(A) = \{y \in F, \exists x \in A, y = f(x)\}$ ; $f^{-1}(B) = \{x \in E, f(x) \in B\}$ ; injective : $f(x) = f(x') \Rightarrow x = x'$ ; surjective : $\forall y, \exists x, y = f(x)$ ; $g \circ f$ injective si $f$, $g$ injectives ; surjective si $f$, $g$ surjectives

Soient $E$, $F$ deux ensembles, $f : E \to F$, $A \subset E$ et $B \subset F$. Donner les définitions avec des quantificateurs de :
a. $f$ est injective. b. $f$ est surjective. c. $f(A)$. d. $f^{-1}(B)$.

## Exercice 1
Type : image directe, image réciproque (lecture graphique) · ECUE : OBM · Niveau : maths-s1-obm/9
Formules : $f(A) = \{f(x), x \in A\}$ ; $f^{-1}(B) = \{x, f(x) \in B\}$ ; lire les valeurs prises (bornes ouvertes / fermées) ; $f(\mathbb{R})$ = ensemble des valeurs prises

On considère la fonction $\cos : ]-\pi, \pi] \to \mathbb{R}$. Calculer $\cos\left(\left[0, \frac{3\pi}4\right[\right)$ et $\cos^{-1}\left(\left[-1, -\frac12\right]\right)$. Vous compléterez vos réponses par un dessin.

## Exercice 2
Type : primitive $u'/u^n$, IPP trigonométrique · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/7
Formules : $\int \frac{u'}{u^2} = -\frac1u$ ; IPP $\int uv' = [uv] - \int u'v$ avec $u = x$, $v' = \sin(3x)$, $v = -\frac{\cos(3x)}3$ ; $\int \cos(3x) = \frac{\sin(3x)}3$

1. À l'aide d'une primitive, calculer l'intégrale $I_1 = \displaystyle\int_1^2 \frac{3t^2 + 2}{(t^3 + 2t)^2}\,dt$.
2. À l'aide d'une intégration par parties, calculer l'intégrale $I_2 = \displaystyle\int_0^{\pi/6} x\sin(3x)\,dx$. Vous ferez apparaître clairement sur la copie les fonctions choisies pour l'intégration par parties.

## Exercice 3
Type : nier une phrase quantifiée · ECUE : OBM · Niveau : maths-s1-obm/5
Formules : $\neg(\forall x, P) = \exists x, \neg P$ ; $\neg(A \Rightarrow B) = A \wedge \neg B$ ; $\neg(f(x) \geqslant f(x')) = f(x) < f(x')$

Soit $f$ une fonction de $\mathbb{R}$ dans $\mathbb{R}$. Écrire la négation de : $\forall (x, x') \in \mathbb{R}^2$, $x \geqslant x' \implies f(x) \geqslant f(x')$.
