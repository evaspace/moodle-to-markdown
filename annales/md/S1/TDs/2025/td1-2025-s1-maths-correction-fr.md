# Contrôle TD 1 (S1) — lundi 19 octobre 2020 (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (pas de corrigé officiel). Sujet : `td1-2025-s1-maths-subject-fr.md` (même dossier). Calculs vérifiés avec sympy. 

## Questions de cours
Type : image directe et réciproque, injectivité, surjectivité, composée · ECUE : OBM · Niveau : maths-s1-obm/10
Formules : $f(A) = \{y \in F, \exists x \in A, y = f(x)\}$ ; $f^{-1}(B) = \{x \in E, f(x) \in B\}$ ; injective : $f(x) = f(x') \Rightarrow x = x'$ ; surjective : $\forall y, \exists x, y = f(x)$ ; $g \circ f$ injective si $f$, $g$ injectives ; surjective si $f$, $g$ surjectives

a. $\forall(x,x')\in E^2,\ f(x)=f(x')\Rightarrow x=x'$. b. $\forall y\in F,\ \exists x\in E,\ f(x)=y$. c. $f(A)=\{f(x),\ x\in A\}$. d. $f^{-1}(B)=\{x\in E,\ f(x)\in B\}$.

## Exercice 1
Type : image directe, image réciproque (lecture graphique) · ECUE : OBM · Niveau : maths-s1-obm/9
Formules : $f(A) = \{f(x), x \in A\}$ ; $f^{-1}(B) = \{x, f(x) \in B\}$ ; lire les valeurs prises (bornes ouvertes / fermées) ; $f(\mathbb{R})$ = ensemble des valeurs prises

$\cos\left(\left[0,\frac{3\pi}4\right[\right)=\left]-\dfrac{\sqrt2}2,1\right]$ ($\cos$ est décroissante sur $[0,\pi]$ : $\cos0=1$ atteint, $\cos\frac{3\pi}4=-\frac{\sqrt2}2$ non atteint).
$\cos^{-1}\left(\left[-1,-\frac12\right]\right)=\left]-\pi,-\dfrac{2\pi}3\right]\cup\left[\dfrac{2\pi}3,\pi\right]$.

## Exercice 2
Type : primitive $u'/u^n$, IPP trigonométrique · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/7
Formules : $\int \frac{u'}{u^2} = -\frac1u$ ; IPP $\int uv' = [uv] - \int u'v$ avec $u = x$, $v' = \sin(3x)$, $v = -\frac{\cos(3x)}3$ ; $\int \cos(3x) = \frac{\sin(3x)}3$

1. $u=t^3+2t$, $u'=3t^2+2$ : $I_1=\Big[-\dfrac1{t^3+2t}\Big]_1^2=-\dfrac1{12}+\dfrac13=\dfrac14$.
2. $u=x$, $u'=1$, $v'=\sin3x$, $v=-\dfrac{\cos3x}3$ : $I_2=\Big[-\dfrac{x\cos3x}3\Big]_0^{\pi/6}+\dfrac13\int_0^{\pi/6}\cos3x\,dx=0+\dfrac19\Big[\sin3x\Big]_0^{\pi/6}=\dfrac19$ (car $\cos\frac\pi2=0$ et $\sin\frac\pi2=1$).

## Exercice 3
Type : nier une phrase quantifiée · ECUE : OBM · Niveau : maths-s1-obm/5
Formules : $\neg(\forall x, P) = \exists x, \neg P$ ; $\neg(A \Rightarrow B) = A \wedge \neg B$ ; $\neg(f(x) \geqslant f(x')) = f(x) < f(x')$

$\exists(x,x')\in\mathbb R^2,\ x\ge x'\ \text{et}\ f(x)<f(x')$.
