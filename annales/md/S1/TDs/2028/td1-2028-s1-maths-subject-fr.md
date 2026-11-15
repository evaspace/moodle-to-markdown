# Contrôle de cours 1, mathématiques S1 — lundi 16 octobre 2023 (sujet, FR)

- Source : `raw/S1/TDs/2028/td1-2028-s1-maths-subject-fr.pdf` (3 pages)
- Date réelle : 16 octobre 2023 (dossier promo 2028). Pas de corrigé.
- Durée : 1 heure. Deux parties (ECUE LE et DP), 30 minutes et 20 points chacune, deux notes distinctes.

## Partie LE, cours 1 : sur la logique (9 points)
Type : négations, implications et équivalences · ECUE : OBM · Niveau : maths-s1-obm/2
Formules : $\neg(P \wedge Q) = \neg P \vee \neg Q$ ; $\neg(P \vee (Q \wedge R)) = \neg P \wedge (\neg Q \vee \neg R)$ ; $\neg(P \Rightarrow Q) = P \wedge \neg Q$ ; $P \Rightarrow Q \equiv \neg P \vee Q$ ; $x^2 + x - 6 = (x+3)(x-2)$ ; multiple de 6 $\Rightarrow$ multiple de 3 ; $\sqrt{x^2} = |x|$

1. On considère les assertions $P$ : « Le chien aboie » et $Q$ : « Je pars en courant ». Traduire en langage propositionnel (en utilisant les symboles $\wedge$, $\vee$, $\Rightarrow$, etc.) les phrases suivantes :
   (a) « Si le chien aboie alors je pars en courant » ;
   (b) « Le chien n'aboie pas ou je pars en courant » ;
   (c) « Le chien aboie et je ne pars pas en courant » ;
   (d) « Le chien n'aboie pas si et seulement si je pars en courant ».
2. On considère deux assertions $A$ et $B$. La négation de $A \Rightarrow B$ est … et la contraposée de $A \Rightarrow B$ est …
   Application : soit $x \in \mathbb{R}$. On prend $A$ : « $0 \leqslant x < \pi$ » et $B$ : « $\sin(x) \geqslant 0$ ». Donner la négation puis la contraposée de $A \Rightarrow B$.
3. Soit $x \in \mathbb{R}$. Mettre le symbole $\Rightarrow$, $\Leftarrow$ ou $\iff$ à la place des pointillés :
   (a) $x^2 > 4 \ \dots\ x > 2$ ; (b) $x = \pi \ \dots\ \sin(x) = 0$ ; (c) $\sqrt{x^2} = 1 \ \dots\ x = 1$ ; (d) $\dfrac{x^2}3 = 0 \ \dots\ x = 0$.
4. Soit l'assertion $P$ : « $\exists x \in \mathbb{R}, \forall y \in \mathbb{R}, y^2 > x$ ».
   (a) $P$ est-elle vraie ou fausse ? Justifiez votre réponse.
   (b) Donner la négation de $P$.

## Partie LE, cours 2 : sur les ensembles (4 points)
Type : ensembles (appartenance, inclusion, union, intersection, produit, complémentaire) · ECUE : OBM · Niveau : maths-s1-obm/8
Formules : $x \in A$ ; $A \subset B$ ; $A \cup B$, $A \cap B$ ; $A \times B = \{(a, b), a \in A, b \in B\}$ ; complémentaire $\bar B = E \setminus B$ ; $B = [\![0, 7]\!]$

On considère les ensembles $A = \{x \in \mathbb{R}, -1 < x < 10\}$ et $B = \{n \in \mathbb{N}, n + 1 \leqslant 8\}$.
1. De quel ensemble commun $A$ et $B$ sont-ils deux sous-ensembles ?
2. Dans chacune des phrases suivantes, remplacer les pointillés afin de la rendre vraie (remplacer les pointillés par $\emptyset$ est interdit). Exemple : pour « … $\in B$ », on peut remplacer les pointillés par 0 car $0 \in B$.
   (a) … $\in A$ ; (b) … $\notin A \cup B$ ; (c) … $\subset A \cup B$ ; (d) … $\in A \cap B$ ; (e) … $\subset A \times B$.
3. Quel est le complémentaire de $B$ dans $\mathbb{Z}$ ?

## Partie LE, cours 3 : sur les fonctions (7 points)
Type : injectivité, surjectivité, image directe et réciproque · ECUE : OBM · Niveau : maths-s1-obm/10
Formules : injective : $f(x) = f(y) \Rightarrow x = y$ (contre-exemple $f(1) = f(2)$) ; surjective : $\forall y, \exists x, f(x) = y$ ; $f(A) = \{f(x), x \in A\}$ ; $f^{-1}(B) = \{x, f(x) \in B\}$ (peut être vide)

Soient $E$ et $F$ deux ensembles et $f : E \to F$.
1. Donner la définition mathématique de « $f$ surjective ».
2. Donner la définition mathématique de « $f$ injective ».
3. Dessiner (graphe, patate…) une fonction $f : [\![1, 4]\!] \to [\![1, 5]\!]$ qui n'est pas injective mais qui vérifie $f^{-1}(\{2, 3\}) = \{1\}$.

## Partie DP, cours 1 : dénombrement (6 points)
Type : interpréter une formule de dénombrement · ECUE : DP · Niveau : maths-s1-dp/4
Formules : $\frac{n!}{(n-p)!} = A_n^p$ : tirage successif sans remise (ordre) ; $\binom np$ : tirage simultané ; $\binom{8}{3}\binom{8}{2}$ : 3 cartes d'une couleur et 2 d'une autre ; $\binom{7}{1}\binom{24}{3}$ : exactement 1 parmi 7, le reste parmi 24 (catégories disjointes)

Dans une urne, il y a 10 boules numérotées de 1 à 10 indiscernables au toucher. On effectue des tirages de ces boules.
Réponses : 1 : $7 \times 8 \times 9 \times 10$ ; 2 : $10!$ ; 3 : $\binom{10}7$ ; 4 : $10^3$.
Modèles : A : tirage successif et sans remise de 10 boules ; B : tirage successif et avec remise de 3 boules ; C : tirage successif et sans remise de 4 boules ; D : tirage successif et avec remise de 4 boules ; E : tirage simultané de 7 boules ; F : tirage simultané de 3 boules.
1. Compléter : la réponse 1 (resp. 2, 3, 4) est le nombre de tirages possibles pour le(s) modèle(s) …
2. Donner le nombre de tirages possibles au(x) modèle(s) ci-dessus dont la réponse n'était ni 1, ni 2, ni 3, ni 4.

## Partie DP, cours 2 : sur les combinaisons (8 points)
Type : binôme de Newton et double comptage · ECUE : DP · Niveau : maths-s1-dp/6
Formules : $(a + b)^n = \sum_{k=0}^n \binom nk a^kb^{n-k}$ ; $a = 1$, $b = 3$ ; principe multiplicatif $4^n$ ; double comptage : compter le même ensemble de deux façons ; $\binom nk$ façons de choisir $k$ cases

Soient $n \in \mathbb{N}$ et $k \in [\![0, n]\!]$.
1. Que comptez-vous si vous calculez $\binom nk$ ? Donner son expression avec les factorielles.
2. Soit $E$ un ensemble ayant 7 éléments. Calculer le nombre $N$ de sous-ensembles de $E$ ayant 3 éléments. Vos calculs doivent être détaillés et simplifiés.
3. Soient $(a, b) \in \mathbb{R}^2$ et $n \in \mathbb{N}$. Donner la formule du binôme de Newton.
4. Soit $E$ un ensemble à $n$ éléments ($n \in \mathbb{N}^*$). Expliquer, via le dénombrement, pourquoi le cardinal de $\mathcal{P}(E)$ est $\sum_{k=0}^n \binom nk$.
5. En utilisant la formule du binôme de Newton, trouver la valeur de $\sum_{k=0}^n \binom nk$. Vous détaillerez votre calcul.

## Partie DP, cours 3 : probabilités (6 points)
Type : formules de base des probabilités · ECUE : DP · Niveau : maths-s1-dp/8
Formules : $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ ; $P(\Omega) = 1$ ; $P(\emptyset) = 0$ ; $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$ ; indépendants $\iff P(A \cap B) = P(A)P(B)$ ; partition : deux à deux disjoints, union $= \Omega$ (non vides)

Soient $A$, $B$ et $C$ trois événements d'un espace probabilisé $(\Omega, \mathcal{P}(\Omega), P)$ de probabilités non nulles.
1. Compléter les formules : (a) $P(A \cup B) = $ ; (b) $P(\Omega) = $ ; (c) $P(\emptyset) = $ ; (d) $P(A \mid B) = $.
2. Que signifie (mathématiquement) que « $A$ et $B$ sont indépendants » ?
3. Que signifie que « $A$, $B$ et $C$ forment une partition de $\Omega$ » ?
