# Examen S2PA-B3 EFDP — mars 2024 (corrigé, FR)

- Source : `raw/S2/Midterms/Maths PC/2028/PA/S2PA_2024_B3_COR_EFDP.pdf` (5 pages)
- Date réelle : mars 2024 (S2 PA, bloc 3, dossier promo 2028). Pas de sujet séparé.
- Corrigé officiel : énoncé rappelé, solution en citation.

## Exercice 1 : ensembles et fonctions 1
Type : injectivité, surjectivité, image directe et réciproque · ECUE : OBM · Niveau : maths-s1-obm/10
Formules : injective : $f(x) = f(y) \Rightarrow x = y$ (contre-exemple $f(1) = f(2)$) ; surjective : $\forall y, \exists x, f(x) = y$ ; $f(A) = \{f(x), x \in A\}$ ; $f^{-1}(B) = \{x, f(x) \in B\}$ (peut être vide)

Soient $E = \{1,2,3,4\}$ et $F = \{2,3,4\}$.

1. Quel est le cardinal de $E \times F$ ?
> $\mathrm{Card}(E \times F) = \mathrm{Card}(E) \times \mathrm{Card}(F) = 4 \times 3 = 12$.

2. A-t-on $E \times F = F \times E$ ? Pourquoi ?
> Non : $(1,2) \in E \times F$ et $(1,2) \notin F \times E$.

3. On définit la fonction $f : E \times F \to \mathbb{N}$, $(x,y) \mapsto x + y$.
   - (a) Remplir le tableau de valeurs de la fonction $f$.
   - (b) Déterminer $f(E \times F)$, $f(\{(2,2), (1,3), (4,3)\})$, $f^{-1}(\{1\})$ et $f^{-1}(\{6\})$.
   - (c) Écrire la définition de : « $f$ injective de $E \times F$ vers $\mathbb{N}$ ». $f$ est-elle injective ? Justifier.
   - (d) Écrire la définition de : « $f$ surjective de $E \times F$ vers $\mathbb{N}$ ». $f$ est-elle surjective ? Justifier.
   - (e) Déterminer $A \subset E \times F$ et $B \subset \mathbb{N}$ tels que $f : A \to B$ soit injective, non surjective ($A$ et $B$ doivent contenir au moins deux éléments).
   - (f) Déterminer $A' \subset E \times F$ et $B' \subset \mathbb{N}$ tels que $f : A' \to B'$ soit surjective, non injective ($A'$ et $B'$ doivent contenir au moins deux éléments).
> (a)
>
> | $(x,y)$ | (1,2) | (1,3) | (1,4) | (2,2) | (2,3) | (2,4) | (3,2) | (3,3) | (3,4) | (4,2) | (4,3) | (4,4) |
> |---|---|---|---|---|---|---|---|---|---|---|---|---|
> | $f((x,y))$ | 3 | 4 | 5 | 4 | 5 | 6 | 5 | 6 | 7 | 6 | 7 | 8 |
>
> (b) $f(E \times F) = \{3,4,5,6,7,8\}$ ; $f(\{(2,2),(1,3),(4,3)\}) = \{4,7\}$ ; $f^{-1}(\{1\}) = \emptyset$ ; $f^{-1}(\{6\}) = \{(2,4),(3,3),(4,2)\}$.
> (c) $\forall ((x,y),(x',y')) \in (E \times F)^2$, $f((x,y)) = f((x',y')) \Rightarrow (x,y) = (x',y')$. $f$ n'est pas injective : $f((1,3)) = f((2,2)) = 4$ et $(1,3) \neq (2,2)$.
> (d) $\forall n \in \mathbb{N}$, $\exists (x,y) \in E \times F$, $n = f((x,y))$. $f$ n'est pas surjective : 10 n'a pas d'antécédent.
> (e) Par exemple $A = \{(1,2),(1,3),(1,4)\}$ et $B = \mathbb{N}$.
> (f) Par exemple $A' = E \times F$ et $B' = \{3,4,5,6,7,8\}$.

## Exercice 2 : ensembles et fonctions 2
Type : image directe, image réciproque (lecture graphique) · ECUE : OBM · Niveau : maths-s1-obm/9
Formules : $f(A) = \{f(x), x \in A\}$ ; $f^{-1}(B) = \{x, f(x) \in B\}$ ; lire les valeurs prises (bornes ouvertes / fermées) ; $f(\mathbb{R})$ = ensemble des valeurs prises

Compléter le tableau suivant pour $f = \exp : \mathbb{R} \to \mathbb{R}$ et $f = \sin : [-\pi, \pi] \to \mathbb{R}$ : $f(\{0\})$, $f(]0, \pi])$, $f^{-1}(\{0\})$, $f^{-1}(\{1\})$, $f^{-1}(]-\infty, 0])$. (Conseil : dessiner le graphe des fonctions au brouillon.)
> | $f$ | $\exp : \mathbb{R} \to \mathbb{R}$ | $\sin : [-\pi,\pi] \to \mathbb{R}$ |
> |---|---|---|
> | $f(\{0\})$ | $\{1\}$ | $\{0\}$ |
> | $f(]0,\pi])$ | $]1, e^\pi]$ | $[0,1]$ |
> | $f^{-1}(\{0\})$ | $\emptyset$ | $\{-\pi, 0, \pi\}$ |
> | $f^{-1}(\{1\})$ | $\{0\}$ | $\{\frac\pi2\}$ |
> | $f^{-1}(]-\infty,0])$ | $\emptyset$ | $[-\pi,0] \cup \{\pi\}$ |

## Exercice 3 : fonction arctan
Type : fonction arctan (définition, dérivée, valeurs remarquables) · ECUE : APEF (fonctions)
Formules : $\arctan : \mathbb{R} \to \left]-\frac\pi2, \frac\pi2\right[$, réciproque de $\tan$ ; $\tan(\arctan x) = x$ ; $\arctan'(x) = \frac1{1+x^2}$ ; $\tan 0 = 0$, $\tan\frac\pi6 = \frac1{\sqrt3}$, $\tan\frac\pi4 = 1$, $\tan\frac\pi3 = \sqrt3$ ; $\tan$ impaire

On considère la fonction bijective $\tan : \big]-\frac\pi2, \frac\pi2\big[ \to \mathbb{R}$, $\alpha \mapsto \tan(\alpha)$. Soit $\arctan$ sa fonction réciproque.

1. Rappeler le domaine de définition $D$ de la fonction $\arctan$ ainsi que son domaine d'arrivée $\arctan(D)$.
> $D = \mathbb{R}$ et $\arctan(D) = \big]-\frac\pi2, \frac\pi2\big[$.

2. Rappeler l'expression de la dérivée de $\arctan$.
> Pour tout réel $x$, $\arctan'(x) = \dfrac1{1 + x^2}$.

3. Remplir le tableau des valeurs de $\tan(\alpha)$ pour $\alpha = 0, \frac\pi4, \frac\pi3, -\frac\pi3, \frac\pi6, -\frac\pi4, \arctan(x)$.
> | $\alpha$ | $0$ | $\frac\pi4$ | $\frac\pi3$ | $-\frac\pi3$ | $\frac\pi6$ | $-\frac\pi4$ | $\arctan(x)$ |
> |---|---|---|---|---|---|---|---|
> | $\tan(\alpha)$ | $0$ | $1$ | $\sqrt3$ | $-\sqrt3$ | $\frac1{\sqrt3}$ | $-1$ | $x$ |

## Exercice 4 : dénombrement 1
Type : binôme de Newton, cardinal de $\mathcal{P}(E)$ · ECUE : DP · Niveau : maths-s1-dp/6
Formules : $(a+b)^n = \sum_{k=0}^n \binom nk a^kb^{n-k}$ ; nombre de parties à $k$ éléments : $\binom nk$ ; union disjointe : les cardinaux s'ajoutent ; $\sum_{k=0}^n \binom nk = (1+1)^n = 2^n = \mathrm{Card}\,\mathcal{P}(E)$

1. Soient $(a,b) \in \mathbb{R}^2$ et $n \in \mathbb{N}^*$. Rappeler la formule du binôme de Newton donnant $(a+b)^n$.
> $(a+b)^n = \displaystyle\sum_{k=0}^n \binom nk a^kb^{n-k}$.

2. Soit $E$ un ensemble de cardinal $n \in \mathbb{N}^*$.
   - (a) Soit $k \in \mathbb{N}$ tel que $0 \leqslant k \leqslant n$. Combien y a-t-il de sous-ensembles de $E$ à $k$ éléments ?
   - (b) En utilisant les questions précédentes et en justifiant, calculer le cardinal de $\mathcal{P}(E)$.
> (a) $\binom nk$.
> (b) En notant $\mathcal{P}_k(E)$ l'ensemble des parties à $k$ éléments : $\mathcal{P}(E) = \mathcal{P}_0(E) \sqcup \mathcal{P}_1(E) \sqcup \dots \sqcup \mathcal{P}_n(E)$. Donc $\mathrm{Card}(\mathcal{P}(E)) = \displaystyle\sum_{k=0}^n \binom nk = \sum_{k=0}^n \binom nk 1^k1^{n-k} = (1+1)^n = 2^n$.

## Exercice 5 : dénombrement 2
Type : tirages simultanés, combinaisons · ECUE : DP · Niveau : maths-s1-dp/5
Formules : tirage simultané de $k$ parmi $n$ : $\binom nk$ ; « A ou B » incompatibles : additionner ; « A et B » : multiplier les $\binom{}{}$ ; contraire : $P(\bar A) = 1 - P(A)$ ; équiprobabilité

On considère les $N = 400$ étudiants de sup à Epita, répartis en 10 classes de 40 élèves. On désire réaliser un sondage de satisfaction auprès d'un échantillon de $n = 40$ étudiants sélectionnés aléatoirement. On ne demande pas d'effectuer les calculs.

1. Combien y a-t-il de façons de sélectionner l'échantillon ? Justifier.
> Tirage simultané de 40 élèves parmi 400, sans ordre et sans remise : $\binom{400}{40}$.

2. Combien y a-t-il de façons de sélectionner l'échantillon si on impose qu'il contienne autant d'étudiants de chaque classe ? Justifier.
> 4 élèves par classe, $\binom{40}4$ choix dans chacune des 10 classes : $\binom{40}4^{10}$.

3. Chaque classe possède deux délégués, qu'on impose dans l'échantillon. Combien y a-t-il de façons de sélectionner l'échantillon si les autres étudiants doivent être répartis équitablement dans chaque classe ? Justifier.
> 4 élèves par classe dont les 2 délégués (1 seule façon) et $\binom{38}2$ façons pour les deux autres : $\binom{38}2^{10}$.

4. Parmi les 400 élèves, 50 sont des filles. On veut un échantillon paritaire (autant de filles que de garçons). Combien y a-t-il de façons de le sélectionner ? Justifier.
> 20 filles et 20 garçons : $\binom{50}{20} \times \binom{350}{20}$.

## Exercice 6 : probabilités conditionnelles
Type : probabilités totales et Bayes · ECUE : DP · Niveau : maths-s1-dp/10
Formules : probabilités totales : $P(M) = P(M \mid V)P(V) + P(M \mid \bar V)P(\bar V)$ ; Bayes : $P(V \mid M) = \frac{P(M \mid V)P(V)}{P(M)}$ ; $P(\bar V) = 1 - P(V)$

Dans une promotion d'élèves en PA à Epita, on considère que seuls 40 % apprennent leur cours de maths. Pour ceux qui apprennent le cours, la probabilité de valider l'année est de 80 %. Pour les autres, celle-ci tombe à 20 %. On note $C$ l'événement « apprendre son cours » et $V$ l'événement « valider l'année ». Résultats sous forme de fraction simplifiée.

1. Traduire l'énoncé en termes de probabilités.
> $P(C) = 0{,}4$, $P(V \mid C) = 0{,}8$ et $P(V \mid \overline C) = 0{,}2$.

2. On choisit un élève de PA au hasard, quelle est sa probabilité de valider ?
> $\{C, \overline C\}$ est une partition de $\Omega$ : $P(V) = P(V \mid C)P(C) + P(V \mid \overline C)P(\overline C) = 0{,}8 \times 0{,}4 + 0{,}2 \times 0{,}6 = 0{,}44 = \dfrac{11}{25}$.

3. On choisit un élève qui valide l'année, au hasard. Quelle est la probabilité qu'il ait appris son cours ?
> $P(C \mid V) = \dfrac{P(V \mid C)P(C)}{P(V)} = \dfrac{0{,}8 \times 0{,}4}{0{,}44} = \dfrac8{11}$.

4. Quelle proportion minimale $p$ d'élèves qui apprennent leur cours faudrait-il pour que 60 % de la promotion valide ?
> $P(V) = 0{,}8p + 0{,}2(1-p) = 0{,}6p + 0{,}2 \geqslant 0{,}6 \iff p \geqslant \dfrac23$.

## Exercice 7 : variables aléatoires
Type : loi d'une variable, Bernoulli, binomiale (somme d'indépendantes) · ECUE : DP · Niveau : maths-s1-dp/14
Formules : $P(X = x) = \frac{\text{nb de boules } x}{\text{nb total}}$ ; $E(X) = \sum xP(X = x)$ ; $V = E(X^2) - E(X)^2$ ; Bernoulli $E = p$, $V = p(1-p)$ ; somme de $n$ Bernoulli indépendantes de paramètre $p$ : $\mathcal{B}(n, p)$, $E = np$, $V = np(1-p)$ ; binôme pour $\sum P = 1$

On dispose d'une urne contenant 3 boules rouges et 2 boules vertes. On effectue un tirage successif sans remise de 3 boules de l'urne. Résultats sous forme de fraction simplifiée.

1. Faire un schéma représentant toutes les issues possibles ainsi que leur probabilité (arbre pondéré).
> Arbre à trois étages R/V : 1er tirage $P(R) = \frac35$, $P(V) = \frac25$ ; les probabilités suivantes se lisent sur les boules restantes (sur 4, puis sur 3). $P(RRR) = \frac35 \cdot \frac24 \cdot \frac13 = \frac1{10}$ ; $P(RRV) = P(RVR) = P(VRR) = \frac15$ ; $P(RVV) = P(VRV) = P(VVR) = \frac1{10}$.

2. On note $X$ la variable aléatoire qui compte le nombre de boules vertes obtenues.
   - (a) Donner la loi de $X$.
   - (b) Calculer son espérance et sa variance.
> (a) $X(\Omega) = [\![0,2]\!]$. $P(X=0) = \frac1{10}$, $P(X=1) = \frac15 + \frac15 + \frac15 = \frac35$, $P(X=2) = \frac3{10}$.
> (b) $E(X) = 0 \times \frac1{10} + 1 \times \frac35 + 2 \times \frac3{10} = \frac65$. $E(X^2) = \frac35 + 4 \times \frac3{10} = \frac95$. $V(X) = E(X^2) - E(X)^2 = \frac95 - \frac{36}{25} = \frac9{25}$.

3. On note $Y$ la variable aléatoire qui vaut 1 si on obtient au moins une boule verte, 0 sinon.
   - (a) Exprimer l'événement « $Y = 1$ » à partir des valeurs prises par $X$.
   - (b) En déduire la loi de $Y$.
   - (c) Donner son espérance et sa variance.
> (a) $Y = 1 \iff X \geqslant 1$.
> (b) $P(Y=1) = P(X=1) + P(X=2) = \frac9{10}$, $P(Y=0) = \frac1{10}$ : $Y \sim \mathcal{B}\big(\frac9{10}\big)$ (Bernoulli).
> (c) $E(Y) = p = \frac9{10}$, $V(Y) = p(1-p) = \frac9{100}$.

4. On répète le tirage 10 fois de suite en remettant les boules entre chaque tirage. Les tirages sont indépendants. On note $Z$ la variable aléatoire qui compte le nombre de fois où on a obtenu au moins une boule verte.
   - (a) Quelles sont les valeurs prises par $Z$ ?
   - (b) Soit $k \in Z(\Omega)$. Que vaut $P(Z = k)$ ? Justifier.
   - (c) Donner l'espérance et la variance de $Z$.
> (a) $Z(\Omega) = [\![0,10]\!]$.
> (b) $Z$ est la somme de 10 variables de Bernoulli indépendantes de même paramètre $p = \frac9{10}$ : $Z \sim \mathcal{B}(10, \frac9{10})$, $P(Z = k) = \binom{10}k\big(\frac9{10}\big)^k\big(\frac1{10}\big)^{10-k}$.
> (c) $E(Z) = np = 9$, $V(Z) = np(1-p) = \frac9{10}$.
