# Contrôle TD 1 (S1) — lundi 8 octobre 2018 (sujet, FR)

- Source : `raw/S1/TDs/2023/td1-2023-s1-maths-subject-fr.pdf` (scan, 2 pages)
- Date réelle : 8 octobre 2018 (dossier promo 2023). Corrigé rédigé : `td1-2023-s1-maths-correction-fr.md` (même dossier).
- Durée : 45 minutes.

## Question de cours
Type : image directe et réciproque, injectivité, surjectivité, composée · ECUE : OBM · Niveau : maths-s1-obm/10
Formules : $f(A) = \{y \in F, \exists x \in A, y = f(x)\}$ ; $f^{-1}(B) = \{x \in E, f(x) \in B\}$ ; injective : $f(x) = f(x') \Rightarrow x = x'$ ; surjective : $\forall y, \exists x, y = f(x)$ ; $g \circ f$ injective si $f$, $g$ injectives ; surjective si $f$, $g$ surjectives

Soient $E$ et $F$ deux ensembles et $f : E \to F$.
1. Soient $A \subset E$ et $B \subset F$. Donner la définition rigoureuse des ensembles $f(A)$ et $f^{-1}(B)$.
2. Donner la définition rigoureuse (avec les quantificateurs) de : $f$ est surjective de $E$ vers $F$.
3. Donner la définition rigoureuse (avec les quantificateurs) de : $f$ est injective de $E$ vers $F$.

## Exercice 1
Type : forme exponentielle, argument · ECUE : HP (nombres complexes, hors programme 2031)
Formules : $z = |z|e^{i\theta}$ ; $e^{i\theta}e^{i\varphi} = e^{i(\theta + \varphi)}$ ; $\frac{e^{i\theta}}{e^{i\varphi}} = e^{i(\theta - \varphi)}$ ; $(re^{i\theta})^n = r^ne^{in\theta}$ ; $-i = e^{-i\pi/2}$

Soient les nombres complexes $z_1 = 2\sqrt3 + 2i$ et $z_2 = 3\sqrt2 - 3\sqrt2 i$. Donner la forme exponentielle de $z_1$ et de $z_2$. En déduire le module et un argument de $z = \dfrac{z_1}{z_2}$.

## Exercice 2
Type : coefficients binomiaux, récurrence (somme de $\binom kp$) · ECUE : DP · Niveau : maths-s1-dp/6
Formules : $C_n^p = \binom np = \frac{n!}{p!(n-p)!}$ ; Pascal $\binom n{p} + \binom n{p+1} = \binom{n+1}{p+1}$ ; même dénominateur $(p+1)!(n+1-p)!$ ; récurrence : $\sum_{k=p}^{n+1} \binom kp = \binom{n+1}{p+1} + \binom{n+1}p$

Soient $p \in \mathbb{N}$ et $n \in \mathbb{N}$ tel que $n \geqslant p$. Montrer que $\dfrac{(n+1)!}{(p+1)!(n-p)!} + \dfrac{(n+1)!}{p!(n+1-p)!} = \dfrac{(n+2)!}{(p+1)!(n+1-p)!}$.
Soit $p \in \mathbb{N}^*$. Via la question précédente, montrer par récurrence sur $n$ que, pour tout entier $n \geqslant p$, $\displaystyle\sum_{k=p}^n C_k^p = C_{n+1}^{p+1}$.

## Exercice 3
Type : IPP : polynôme × sin/cos · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/7
Formules : IPP $\int_a^b uv' = [uv]_a^b - \int_a^b u'v$ ; $u = x$, $u' = 1$ ; $v' = \sin(kx)$, $v = -\frac{\cos(kx)}k$ ; $\int \cos(kx) = \frac{\sin(kx)}k$ ; $\cos\pi = -1$, $\cos\frac\pi2 = 0$, $\sin\frac\pi2 = 1$

Via une intégration par parties, déterminer $I = \displaystyle\int_0^\pi x\sin(x)\,dx$.
