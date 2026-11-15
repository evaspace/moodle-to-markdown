# Contrôle TD 1 (S1) — lundi 8 octobre 2018 (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (pas de corrigé officiel). Sujet : `td1-2023-s1-maths-subject-fr.md` (même dossier). Calculs vérifiés avec sympy. L'exercice 1 (complexes) est hors programme 2031.

## Question de cours
Type : image directe et réciproque, injectivité, surjectivité, composée · ECUE : OBM · Niveau : maths-s1-obm/10
Formules : $f(A) = \{y \in F, \exists x \in A, y = f(x)\}$ ; $f^{-1}(B) = \{x \in E, f(x) \in B\}$ ; injective : $f(x) = f(x') \Rightarrow x = x'$ ; surjective : $\forall y, \exists x, y = f(x)$ ; $g \circ f$ injective si $f$, $g$ injectives ; surjective si $f$, $g$ surjectives

1. $f(A)=\{f(x),\ x\in A\}=\{y\in F,\ \exists x\in A,\ y=f(x)\}$ et $f^{-1}(B)=\{x\in E,\ f(x)\in B\}$.
2. Surjective : $\forall y\in F,\ \exists x\in E,\ f(x)=y$.
3. Injective : $\forall(x,x')\in E^2,\ f(x)=f(x')\Rightarrow x=x'$.

## Exercice 1
Type : forme exponentielle, argument · ECUE : HP (nombres complexes, hors programme 2031)
Formules : $z = |z|e^{i\theta}$ ; $e^{i\theta}e^{i\varphi} = e^{i(\theta + \varphi)}$ ; $\frac{e^{i\theta}}{e^{i\varphi}} = e^{i(\theta - \varphi)}$ ; $(re^{i\theta})^n = r^ne^{in\theta}$ ; $-i = e^{-i\pi/2}$

$z_1=2\sqrt3+2i$ : $|z_1|=\sqrt{12+4}=4$, $\cos\theta=\dfrac{\sqrt3}2$, $\sin\theta=\dfrac12$ : $z_1=4e^{i\pi/6}$. $z_2=3\sqrt2(1-i)$ : $|z_2|=6$, $z_2=6e^{-i\pi/4}$. $z=\dfrac{z_1}{z_2}=\dfrac23e^{i(\pi/6+\pi/4)}=\dfrac23e^{5i\pi/12}$ : module $\dfrac23$, argument $\dfrac{5\pi}{12}$.

## Exercice 2
Type : coefficients binomiaux, récurrence (somme de $\binom kp$) · ECUE : DP · Niveau : maths-s1-dp/6
Formules : $C_n^p = \binom np = \frac{n!}{p!(n-p)!}$ ; Pascal $\binom n{p} + \binom n{p+1} = \binom{n+1}{p+1}$ ; même dénominateur $(p+1)!(n+1-p)!$ ; récurrence : $\sum_{k=p}^{n+1} \binom kp = \binom{n+1}{p+1} + \binom{n+1}p$

$\dfrac{(n+1)!}{(p+1)!(n-p)!}+\dfrac{(n+1)!}{p!(n+1-p)!}=\dfrac{(n+1)!}{(p+1)!(n+1-p)!}\big[(n+1-p)+(p+1)\big]=\dfrac{(n+1)!(n+2)}{(p+1)!(n+1-p)!}=\dfrac{(n+2)!}{(p+1)!(n+1-p)!}$. Cette égalité est la relation de Pascal $C_{n+1}^{p+1}+C_{n+1}^p=C_{n+2}^{p+1}$.
Récurrence sur $n\ge p$ : $n=p$ : $C_p^p=1=C_{p+1}^{p+1}$. Hérédité : $\sum_{k=p}^{n+1}C_k^p=C_{n+1}^{p+1}+C_{n+1}^p=C_{n+2}^{p+1}$.

## Exercice 3
Type : IPP : polynôme × sin/cos · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/7
Formules : IPP $\int_a^b uv' = [uv]_a^b - \int_a^b u'v$ ; $u = x$, $u' = 1$ ; $v' = \sin(kx)$, $v = -\frac{\cos(kx)}k$ ; $\int \cos(kx) = \frac{\sin(kx)}k$ ; $\cos\pi = -1$, $\cos\frac\pi2 = 0$, $\sin\frac\pi2 = 1$

$u=x$, $v'=\sin x$, $v=-\cos x$ : $I=\big[-x\cos x\big]_0^\pi+\int_0^\pi\cos x\,dx=\pi+\big[\sin x\big]_0^\pi=\pi$.
