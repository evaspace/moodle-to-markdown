# Contrôle de cours EFDP (S2 PA) — lundi 19 février 2024 (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (pas de corrigé officiel). Sujet : `td3-2028-s2-maths-PA-subject-fr.md` (même dossier). Calculs vérifiés avec sympy. 

## Cours 1 : ensembles (4 points)
Type : ensembles (appartenance, inclusion, union, intersection, produit, complémentaire) · ECUE : OBM · Niveau : maths-s1-obm/8
Formules : $x \in A$ ; $A \subset B$ ; $A \cup B$, $A \cap B$ ; $A \times B = \{(a, b), a \in A, b \in B\}$ ; complémentaire $\bar B = E \setminus B$ ; $B = [\![0, 7]\!]$

1. $A$ et $B$ sont des sous-ensembles de $\mathbb R$.
2. a) $\{0,1\}\subset A$. b) $-5\notin A\cup B$. c) $\{1,2\}\subset A\cup B$. d) $1\in A\cap B$. e) $(1,1)\in A\times B$.
3. $A=]-2,5]$ est infini. $B=\{0,1,\dots,12\}$ est fini, de cardinal $13$.

## Cours 2 : ensembles et fonctions - partie 1 (5,5 points)
Type : injectivité, surjectivité, image directe et réciproque · ECUE : OBM · Niveau : maths-s1-obm/9
Formules : injective : $f(x) = f(y) \Rightarrow x = y$ (contre-exemple $f(1) = f(2)$) ; surjective : $\forall y, \exists x, f(x) = y$ ; $f(A) = \{f(x), x \in A\}$ ; $f^{-1}(B) = \{x, f(x) \in B\}$ (peut être vide)

1. $f(A)=\{f(x),\ x\in A\}=\{y\in F,\ \exists x\in A,\ y=f(x)\}$.
2. $f^{-1}(B)=\{x\in E,\ f(x)\in B\}$.
3. $f(a)=2$, $f(b)=2$, $f(c)=3$, $f(d)=1$ : $f(\{b,c\})=\{2,3\}$ et $f^{-1}(\{2\})=\{a,b\}$.
4. (a) $f(\{-4,2\})=\{16,4\}$ ; $f([-3,1])=[0,9]$. (b) $f^{-1}(\{4\})=\{-2,2\}$ ; $f^{-1}([0,2])=[-\sqrt2,\sqrt2]$.

## Cours 3 : ensembles et fonctions - partie 2 (5 points)
Type : injectivité, surjectivité, image directe et réciproque · ECUE : OBM · Niveau : maths-s1-obm/10
Formules : injective : $f(x) = f(y) \Rightarrow x = y$ (contre-exemple $f(1) = f(2)$) ; surjective : $\forall y, \exists x, f(x) = y$ ; $f(A) = \{f(x), x \in A\}$ ; $f^{-1}(B) = \{x, f(x) \in B\}$ (peut être vide)

1. $\forall(x,x')\in E^2,\ f(x)=f(x')\Rightarrow x=x'$. 2. $\forall y\in F,\ \exists x\in E,\ f(x)=y$.
3. Oui : $f(1)=1$, $f(2)=2$, $f(3)=3$, $f(4)=3$.
4. Non : $4$ éléments ne peuvent pas avoir $4$ images distinctes dans un ensemble de $3$ éléments (principe des tiroirs).

## Cours 4 : dénombrement 1 (6 points)
Type : dénombrement de mains de cartes · ECUE : DP · Niveau : maths-s1-dp/4
Formules : $|\Omega| = \binom{32}5$ ; « au moins un » : complémentaire $P(A) = 1 - P(\bar A)$ ; $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ ; principe multiplicatif (choisir chaque catégorie séparément) ; équiprobabilité $P = \frac{|A|}{|\Omega|}$

1. $\dfrac{32!}{27!}=32\times31\times30\times29\times28$. 2. $\dbinom{32}5=\dfrac{32!}{5!\,27!}$. 3. $32^5$. 4. Il reste $4$ cartes à choisir parmi $31$ : $\dbinom{31}4=\dfrac{31!}{4!\,27!}$.
5. Nombres à 5 chiffres avec $7,9,9,8,8$ : $\dfrac{5!}{2!\,2!}=30$ (permutations avec répétition).

## Cours 5 : dénombrement 2 (5,5 points)
Type : coefficients binomiaux (symétrie) · ECUE : DP · Niveau : maths-s1-dp/6
Formules : $\binom np = \frac{n!}{p!(n-p)!}$ ; $\binom np = \binom n{n-p}$ ; $\binom np$ = nombre de parties à $p$ éléments d'un ensemble à $n$ éléments ; bijection $A \mapsto \bar A$

1. $\dbinom nk=\dfrac{n!}{k!(n-k)!}$ : nombre de parties de $E$ à $k$ éléments.
2. $\dbinom n{n-k}=\dfrac{n!}{(n-k)!\,k!}=\dbinom nk$.
3. Choisir $k$ éléments à garder revient à choisir les $n-k$ éléments à écarter : $A\mapsto E\setminus A$ est une bijection entre parties à $k$ et à $n-k$ éléments.

## Cours 6 : variable aléatoire (4 points)
Type : loi d'une variable aléatoire finie, espérance, variance · ECUE : DP · Niveau : maths-s1-dp/12
Formules : $\sum_k P(X = k) = 1$ ; $E(X) = \sum_k kP(X = k)$ ; $V(X) = E\big((X - E(X))^2\big) = \sum_k (k - E(X))^2P(X = k)$ ; König-Huygens : $V(X) = E(X^2) - E(X)^2$, $E(X^2) = \sum_k k^2P(X = k)$

1. $P(X=2)=1-\dfrac12-\dfrac13=\dfrac16$.
2. $E(X)=\sum x_iP(X=x_i)=0\cdot\dfrac12+1\cdot\dfrac13+2\cdot\dfrac16=\dfrac23$.
3. $\mathrm{Var}(X)=E\big((X-E(X))^2\big)=E(X^2)-E(X)^2$. Ici $E(X^2)=\dfrac13+\dfrac46=1$ et $\mathrm{Var}(X)=1-\dfrac49=\dfrac59$.
