# Examen S1B1-DP — octobre 2024 (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (le sujet n'avait pas de corrigé officiel). Sujet : `midterm-2029-s1-maths-subject-fr.md` (même dossier). Tous les calculs ont été revérifiés avec sympy.

## Exercice 1 : autour du cours et du TD (4 points)
Type : interpréter une formule de dénombrement · ECUE : DP · Niveau : maths-s1-dp/5
Formules : $\frac{n!}{(n-p)!} = A_n^p$ : tirage successif sans remise (ordre) ; $\binom np$ : tirage simultané ; $\binom{8}{3}\binom{8}{2}$ : 3 cartes d'une couleur et 2 d'une autre ; $\binom{7}{1}\binom{24}{3}$ : exactement 1 parmi 7, le reste parmi 24 (catégories disjointes)

1. Tirage successif sans remise de 5 cartes parmi 32, en tenant compte de l'ordre : $32\times31\times30\times29\times28=\dfrac{32!}{27!}$.
2. Tirage simultané de 5 cartes parmi 32 : $\dbinom{32}{5}$.
3. Dans un jeu où il y a 4 couleurs de 8 cartes : 3 cartes d'une couleur donnée et 2 cartes d'une autre couleur donnée, tirage simultané : $\dbinom83\dbinom82$.
4. Coquille probable de l'énoncé : $1+3=4$ cartes, pas 5, et $7+24=31\ne32$. Situation cohérente : on met de côté une carte précise, puis on tire simultanément 4 des 31 cartes restantes dont 7 sont des cœurs : « exactement un cœur » donne $\dbinom71\dbinom{24}3$.

## Exercice 2 : dénombrement 1 (6 points)
Type : p-listes, arrangements, complémentaire (digicode) · ECUE : DP · Niveau : maths-s1-dp/5
Formules : principe multiplicatif ; chiffres distincts : $10 \times 9 \times 8$ ; avec répétition : $10^3$ ; permutations de 3 chiffres connus : $3!$ ; « au moins un 4 » = total $-$ « aucun 4 » : $10^3 - 9^3$

1. Lettre : 3 choix. Chiffres distincts : $10\times9\times8=720$. Total $3\times720=\mathbf{2160}$.
2. Chiffres quelconques : $10^3$. Total $3\times10^3=\mathbf{3000}$.
3. Lettre connue. Chiffres impairs ($1,3,5,7,9$) distincts : $5\times4\times3=\mathbf{60}$.
4. Lettre : 3 choix. Les chiffres $6,2,9$ dans un ordre quelconque : $3!=6$. Total $3\times6=\mathbf{18}$.
5. Complémentaire : au moins un 4 $=$ tous les codes $-$ aucun 4. Par lettre : $10^3-9^3=1000-729=271$. Total $3\times271=\mathbf{813}$.

## Exercice 3 : dénombrement 2 (8,5 points)
Type : double comptage, $\binom np\binom pk = \binom nk\binom{n-k}{p-k}$ · ECUE : DP · Niveau : maths-s1-dp/6
Formules : choisir $p$ puis $k$ parmi eux = choisir les $k$ puis $p - k$ parmi les $n - k$ restants ; $\binom nk = \frac{n!}{k!(n-k)!}$ ; $\sum_{k=0}^p \binom pk = 2^p$, donc $S_p = \binom np 2^p$

1. (a) 2 jetons parmi 9 pour le triangle, puis 3 parmi les 7 restants : $N_1=\dbinom92\times\dbinom73=36\times35=1260$.
   (b) 5 jetons parmi 9 pour l'hexagone, puis 2 parmi ces 5 pour le triangle : $N_2=\dbinom95\times\dbinom52=126\times10=1260$.
   (c) $N_1=N_2$ : les deux choix comptent les mêmes répartitions.
2. Les deux membres comptent les façons de choisir $p$ éléments parmi $n$, dont $k$ marqués. Gauche : on choisit les $p$ éléments, puis les $k$ marqués parmi eux. Droite : on choisit d'abord les $k$ marqués parmi $n$, puis les $p-k$ autres parmi les $n-k$ restants. C'est le même ensemble de configurations, donc le même nombre.
3. $\dbinom np\dbinom pk=\dfrac{n!}{p!(n-p)!}\cdot\dfrac{p!}{k!(p-k)!}=\dfrac{n!}{(n-p)!\,k!\,(p-k)!}$ et $\dbinom nk\dbinom{n-k}{p-k}=\dfrac{n!}{k!(n-k)!}\cdot\dfrac{(n-k)!}{(p-k)!(n-p)!}=\dfrac{n!}{k!\,(p-k)!\,(n-p)!}$ : égaux.
4. D'après la formule : $S_p=\sum_{k=0}^p\dbinom np\dbinom pk=\dbinom np\sum_{k=0}^p\dbinom pk=\dbinom np\,2^p$ (binôme de Newton avec $(1+1)^p$).

## Exercice 4 : probabilités conditionnelles (6,5 points)
Type : probabilités totales et Bayes · ECUE : DP · Niveau : maths-s1-dp/10
Formules : probabilités totales : $P(M) = P(M \mid V)P(V) + P(M \mid \bar V)P(\bar V)$ ; Bayes : $P(V \mid M) = \frac{P(M \mid V)P(V)}{P(M)}$ ; $P(\bar V) = 1 - P(V)$

1. $P(C)=\dfrac25$, $P(V\mid C)=\dfrac45$, $P(V\mid\bar C)=\dfrac15$.
2. Probabilités totales : $P(V)=P(V\mid C)P(C)+P(V\mid\bar C)P(\bar C)=\dfrac45\cdot\dfrac25+\dfrac15\cdot\dfrac35=\dfrac{8+3}{25}=\dfrac{11}{25}$.
3. Bayes : $P(C\mid V)=\dfrac{P(V\mid C)P(C)}{P(V)}=\dfrac{8/25}{11/25}=\dfrac8{11}$.
4. Soit $p$ la proportion d'élèves qui apprennent : $\dfrac45p+\dfrac15(1-p)=\dfrac35$, soit $\dfrac15+\dfrac35p=\dfrac35$ et $p=\dfrac23$. Il faut donc que au moins $\dfrac23$ des élèves apprennent leur cours.

## Exercice 5 : cours (6 points)
Type : démonstration de cours ($E(aX+b)$, $V(aX+b)$) · ECUE : DP · Niveau : maths-s1-dp/13
Formules : $E(X) = \sum x_iP(X = x_i)$ ; $V(X) = \sum (x_i - E(X))^2P(X = x_i)$ ; $E(aX + b) = aE(X) + b$ ; $V(aX + b) = a^2V(X)$ ; $\sum P(X = x_i) = 1$

1. $E(X)=\sum_{i=1}^nx_iP(X=x_i)$ et $\mathrm{Var}(X)=\sum_{i=1}^n(x_i-E(X))^2P(X=x_i)$.
2. $E(aX+b)=aE(X)+b$. Preuve : $E(aX+b)=\sum(ax_i+b)P(X=x_i)=a\sum x_iP(X=x_i)+b\sum P(X=x_i)=aE(X)+b$ car $\sum P(X=x_i)=1$.
3. $\mathrm{Var}(aX+b)=a^2\mathrm{Var}(X)$. Preuve : $E(aX+b)=aE(X)+b$ donc $(ax_i+b)-E(aX+b)=a(x_i-E(X))$ et $\mathrm{Var}(aX+b)=\sum a^2(x_i-E(X))^2P(X=x_i)=a^2\mathrm{Var}(X)$.

## Exercice 6 : variables aléatoires (9 points)
Type : loi d'une variable, Bernoulli, binomiale (somme d'indépendantes) · ECUE : DP · Niveau : maths-s1-dp/14
Formules : $P(X = x) = \frac{\text{nb de boules } x}{\text{nb total}}$ ; $E(X) = \sum xP(X = x)$ ; $V = E(X^2) - E(X)^2$ ; Bernoulli $E = p$, $V = p(1-p)$ ; somme de $n$ Bernoulli indépendantes de paramètre $p$ : $\mathcal{B}(n, p)$, $E = np$, $V = np(1-p)$ ; binôme pour $\sum P = 1$

1. (a) $P(X_k=0)=\dfrac14$, $P(X_k=1)=\dfrac12$, $P(X_k=2)=\dfrac14$.
   (b) $E(X_k)=0\cdot\dfrac14+1\cdot\dfrac12+2\cdot\dfrac14=1$.
   (c) $E(X_k^2)=0+1\cdot\dfrac12+4\cdot\dfrac14=\dfrac32$ donc $\mathrm{Var}(X_k)=\dfrac32-1^2=\dfrac12$.
2. (a) $Y_k\in\{0,1\}$ et $P(Y_k=1)=P(X_k\in\{0,1\})=\dfrac34$ : $Y_k$ suit une loi de Bernoulli de paramètre $\dfrac34$.
   (b) $E(Y_k)=\dfrac34$ et $\mathrm{Var}(Y_k)=\dfrac34\cdot\dfrac14=\dfrac3{16}$.
3. (a) $Z=\sum_{k=1}^{20}Y_k$ : le gain total est la somme des gains de chaque tirage.
   (b) Les $Y_k$ sont indépendantes de même loi $\mathcal B\!\left(\frac34\right)$, donc $Z\sim\mathcal B\!\left(20,\frac34\right)$ et $P(Z=i)=\dbinom{20}i\left(\dfrac34\right)^i\left(\dfrac14\right)^{20-i}$ pour $i\in[\![0,20]\!]$.
   (c) $\sum_{i=0}^{20}\dbinom{20}i\left(\frac34\right)^i\left(\frac14\right)^{20-i}=\left(\frac34+\frac14\right)^{20}=1$ (binôme de Newton).
   (d) $E(Z)=20\cdot\dfrac34=15$ et $\mathrm{Var}(Z)=20\cdot\dfrac34\cdot\dfrac14=\dfrac{15}4$ (loi binomiale ; ou somme d'espérances, et de variances car indépendance).
