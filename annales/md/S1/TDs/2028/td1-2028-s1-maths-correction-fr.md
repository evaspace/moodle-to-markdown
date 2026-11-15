# Contrôle de cours 1, mathématiques S1 — lundi 16 octobre 2023 (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (pas de corrigé officiel). Sujet : `td1-2028-s1-maths-subject-fr.md` (même dossier). Calculs vérifiés avec sympy. 

## Partie LE, cours 1 : sur la logique (9 points)
Type : négations, implications et équivalences · ECUE : OBM · Niveau : maths-s1-obm/2
Formules : $\neg(P \wedge Q) = \neg P \vee \neg Q$ ; $\neg(P \vee (Q \wedge R)) = \neg P \wedge (\neg Q \vee \neg R)$ ; $\neg(P \Rightarrow Q) = P \wedge \neg Q$ ; $P \Rightarrow Q \equiv \neg P \vee Q$ ; $x^2 + x - 6 = (x+3)(x-2)$ ; multiple de 6 $\Rightarrow$ multiple de 3 ; $\sqrt{x^2} = |x|$

1. (a) $P\Rightarrow Q$. (b) $\neg P\vee Q$. (c) $P\wedge\neg Q$. (d) $\neg P\iff Q$.
2. $\neg(A\Rightarrow B)=A\wedge\neg B$ et contraposée : $\neg B\Rightarrow\neg A$. Application : négation « $0\le x<\pi$ et $\sin x<0$ ». Contraposée : « $\sin x<0\Rightarrow(x<0$ ou $x\ge\pi)$ ».
3. (a) $x^2>4\Leftarrow x>2$. (b) $x=\pi\Rightarrow\sin x=0$. (c) $\sqrt{x^2}=|x|=1\Leftarrow x=1$. (d) $\dfrac{x^2}3=0\iff x=0$.
4. (a) $P$ est vraie : $x=-1$ convient car $y^2\ge0>-1$ pour tout $y$. (b) $\neg P:\ \forall x\in\mathbb R,\ \exists y\in\mathbb R,\ y^2\le x$.

## Partie LE, cours 2 : sur les ensembles (4 points)
Type : ensembles (appartenance, inclusion, union, intersection, produit, complémentaire) · ECUE : OBM · Niveau : maths-s1-obm/8
Formules : $x \in A$ ; $A \subset B$ ; $A \cup B$, $A \cap B$ ; $A \times B = \{(a, b), a \in A, b \in B\}$ ; complémentaire $\bar B = E \setminus B$ ; $B = [\![0, 7]\!]$

1. $A$ et $B$ sont des sous-ensembles de $\mathbb R$.
2. (a) $1\in A$. (b) $-5\notin A\cup B$. (c) $\{0,1\}\subset A\cup B$. (d) $0\in A\cap B$. (e) $\{(0,0)\}\subset A\times B$.
3. $B=\{0,1,\dots,7\}$ : le complémentaire dans $\mathbb Z$ est $\{n\in\mathbb Z,\ n<0\}\cup\{n\in\mathbb N,\ n\ge8\}$.

## Partie LE, cours 3 : sur les fonctions (7 points)
Type : injectivité, surjectivité, image directe et réciproque · ECUE : OBM · Niveau : maths-s1-obm/10
Formules : injective : $f(x) = f(y) \Rightarrow x = y$ (contre-exemple $f(1) = f(2)$) ; surjective : $\forall y, \exists x, f(x) = y$ ; $f(A) = \{f(x), x \in A\}$ ; $f^{-1}(B) = \{x, f(x) \in B\}$ (peut être vide)

1. Surjective : $\forall y\in F,\ \exists x\in E,\ f(x)=y$. 2. Injective : $\forall(x,x')\in E^2,\ f(x)=f(x')\Rightarrow x=x'$.
3. $f(1)=2$, $f(2)=1$, $f(3)=1$, $f(4)=4$ : $f(2)=f(3)$ donc non injective, et $f^{-1}(\{2,3\})=\{1\}$.

## Partie DP, cours 1 : dénombrement (6 points)
Type : interpréter une formule de dénombrement · ECUE : DP · Niveau : maths-s1-dp/4
Formules : $\frac{n!}{(n-p)!} = A_n^p$ : tirage successif sans remise (ordre) ; $\binom np$ : tirage simultané ; $\binom{8}{3}\binom{8}{2}$ : 3 cartes d'une couleur et 2 d'une autre ; $\binom{7}{1}\binom{24}{3}$ : exactement 1 parmi 7, le reste parmi 24 (catégories disjointes)

1. Réponse 1 : $7\times8\times9\times10$ = tirages successifs sans remise de 4 boules : **C**. Réponse 2 : $10!$ : **A**. Réponse 3 : $\binom{10}7=120=\binom{10}3$ : **E** et **F**. Réponse 4 : $10^3$ : **B**.
2. Le modèle restant est **D** (successif avec remise, 4 boules) : $10^4=10000$ tirages.

## Partie DP, cours 2 : sur les combinaisons (8 points)
Type : binôme de Newton et double comptage · ECUE : DP · Niveau : maths-s1-dp/6
Formules : $(a + b)^n = \sum_{k=0}^n \binom nk a^kb^{n-k}$ ; $a = 1$, $b = 3$ ; principe multiplicatif $4^n$ ; double comptage : compter le même ensemble de deux façons ; $\binom nk$ façons de choisir $k$ cases

1. $\dbinom nk$ est le nombre de parties à $k$ éléments d'un ensemble à $n$ éléments, $\dbinom nk=\dfrac{n!}{k!(n-k)!}$.
2. $N=\dbinom73=\dfrac{7\times6\times5}{3\times2\times1}=35$.
3. $(a+b)^n=\displaystyle\sum_{k=0}^n\binom nka^kb^{n-k}$.
4. On classe les parties de $E$ selon leur nombre d'éléments $k\in[\![0,n]\!]$ : il y en a $\dbinom nk$ de taille $k$. Donc $|\mathcal P(E)|=\sum_{k=0}^n\dbinom nk$.
5. $a=b=1$ : $\displaystyle\sum_{k=0}^n\binom nk=(1+1)^n=2^n$.

## Partie DP, cours 3 : probabilités (6 points)
Type : formules de base des probabilités · ECUE : DP · Niveau : maths-s1-dp/8
Formules : $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ ; $P(\Omega) = 1$ ; $P(\emptyset) = 0$ ; $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$ ; indépendants $\iff P(A \cap B) = P(A)P(B)$ ; partition : deux à deux disjoints, union $= \Omega$ (non vides)

1. (a) $P(A\cup B)=P(A)+P(B)-P(A\cap B)$. (b) $P(\Omega)=1$. (c) $P(\emptyset)=0$. (d) $P(A\mid B)=\dfrac{P(A\cap B)}{P(B)}$.
2. $A$ et $B$ indépendants : $P(A\cap B)=P(A)P(B)$.
3. Partition : $A,B,C$ deux à deux disjoints et $A\cup B\cup C=\Omega$.
