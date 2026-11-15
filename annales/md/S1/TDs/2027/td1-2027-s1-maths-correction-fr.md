# Contrôle de cours 1, mathématiques S1 — lundi 3 octobre 2022 (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (pas de corrigé officiel). Sujet : `td1-2027-s1-maths-subject-fr.md` (même dossier). Calculs vérifiés avec sympy. 

## Exercice 1 (3,5 points)
Type : négations, implications et équivalences · ECUE : OBM · Niveau : maths-s1-obm/2
Formules : $\neg(P \wedge Q) = \neg P \vee \neg Q$ ; $\neg(P \vee (Q \wedge R)) = \neg P \wedge (\neg Q \vee \neg R)$ ; $\neg(P \Rightarrow Q) = P \wedge \neg Q$ ; $P \Rightarrow Q \equiv \neg P \vee Q$ ; $x^2 + x - 6 = (x+3)(x-2)$ ; multiple de 6 $\Rightarrow$ multiple de 3 ; $\sqrt{x^2} = |x|$

1. $\neg(P\wedge Q)=\neg P\vee\neg Q$ ; $\neg\big(P\vee(Q\wedge R)\big)=\neg P\wedge(\neg Q\vee\neg R)$ ; $\neg(P\Rightarrow Q)=P\wedge\neg Q$.
2. 1) $x<1\Rightarrow x\le1$. 2) $x^2+x-6=(x+3)(x-2)>0\iff x<-3$ ou $x>2$ : $x^2+x-6>0\Leftarrow x>2$. 3) $\ln x=3\iff x=e^3$. 4) $x$ multiple de 3 $\Leftarrow$ $x$ multiple de 6.

## Exercice 2 (6 points)
Type : injectivité, surjectivité, image directe et réciproque · ECUE : OBM · Niveau : maths-s1-obm/10
Formules : injective : $f(x) = f(y) \Rightarrow x = y$ (contre-exemple $f(1) = f(2)$) ; surjective : $\forall y, \exists x, f(x) = y$ ; $f(A) = \{f(x), x \in A\}$ ; $f^{-1}(B) = \{x, f(x) \in B\}$ (peut être vide)

1. $\forall(x,x')\in E^2,\ f(x)=f(x')\Rightarrow x=x'$. 2. $\forall y\in F,\ \exists x\in E,\ f(x)=y$.
3. (a) Par exemple $f(1)=1$, $f(2)=4$, $f(5)=1$, $f(3)=2$, $f(4)=5$. Trois éléments ($1,2,5$) ont deux images : $f$ n'est jamais injective ($f(1)=f(5)$ ici). L'image a au plus $2+2=4$ éléments, donc $f$ n'est jamais surjective (ici $3\notin f(E)$).
   (b) $f^{-1}(\{3,5\})=\{3,4\}$ force $f(3),f(4)\in\{3,5\}$ ; par exemple $f(3)=3$, $f(4)=5$, puis $f(1)=1$, $f(2)=2$, $f(5)=4$ (bijection de $[\![1,5]\!]$).

## Exercice 3 (4,5 points)
Type : primitive $u'\sqrt u$, théorème d'intégration par parties · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/6
Formules : $\int u'u^{1/2} = \frac23u^{3/2}$ ($x = \frac12(x^2+1)'$) ; IPP : $u$, $v$ de classe $C^1$ sur $[a,b]$, $\int_a^b uv' = [uv]_a^b - \int_a^b u'v$ ; preuve : $(uv)' = u'v + uv'$ intégré sur $[a,b]$

1. $\big(\tfrac13(x^2+1)^{3/2}\big)'=x\sqrt{x^2+1}$ : $I=\tfrac13\Big[(x^2+1)^{3/2}\Big]_0^1=\dfrac{2\sqrt2-1}3$.
2. Si $u$ et $v$ sont de classe $\mathcal C^1$ sur $[a,b]$ : $\displaystyle\int_a^bu(x)v'(x)\,dx=\big[uv\big]_a^b-\int_a^bu'(x)v(x)\,dx$.
3. $uv$ est $\mathcal C^1$ et $(uv)'=u'v+uv'$. On intègre sur $[a,b]$ : $[uv]_a^b=\int_a^bu'v+\int_a^buv'$, d'où la formule.

## Exercice 4 (2,5 points)
Type : dénombrement (p-listes, arrangements, anagrammes, parties) · ECUE : DP · Niveau : maths-s1-dp/4
Formules : $p$-listes (avec remise, ordre) : $n^p$ ; arrangements (sans remise, ordre) : $A_n^p = \frac{n!}{(n-p)!}$ ; permutations : $n!$ ; anagrammes avec lettres répétées : $\frac{n!}{k_1!k_2!\dots}$ ; nombre de parties d'un ensemble à $m$ éléments : $2^m$ ; principe multiplicatif

1. $5!=120$. 2. $5^3=125$. 3. $4\times3\times2=24$. 4. $2^5=32$. 5. $\dbinom53=10$.

## Exercice 5 (3,5 points)
Type : coefficients binomiaux (symétrie) · ECUE : DP · Niveau : maths-s1-dp/6
Formules : $\binom np = \frac{n!}{p!(n-p)!}$ ; $\binom np = \binom n{n-p}$ ; $\binom np$ = nombre de parties à $p$ éléments d'un ensemble à $n$ éléments ; bijection $A \mapsto \bar A$

1. $\dbinom nk=\dfrac{n!}{k!(n-k)!}$ : nombre de parties à $k$ éléments d'un ensemble à $n$ éléments.
2. L'application $A\mapsto E\setminus A$ est une bijection entre les parties à $k$ éléments et les parties à $n-k$ éléments, donc elles sont aussi nombreuses. Par le calcul : $\dbinom n{n-k}=\dfrac{n!}{(n-k)!\,(n-(n-k))!}=\dfrac{n!}{(n-k)!\,k!}=\dbinom nk$.
