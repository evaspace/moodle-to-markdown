# Contrôle S1 — novembre 2022 (sujet, FR)

- Source : `raw/S1/Midterms/Maths PC/2027/midterm-2027-s1-maths-subject.pdf` (10 pages)
- Date réelle : novembre 2022 (dossier promo 2027). Corrigé : `midterm-2027-s1-maths-correction-fr.md`.
- Durée : 3 heures. Barème sur 40 points divisé par 2. 8 exercices. Rigueur prise en compte, malus d'un point pour manque de propreté. Documents et calculatrices interdits.

## Exercice 1 : intégrales (5 points)
Type : primitive $u'/u^n$, IPP trigonométrique, changement de variable racine vers arctan · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/13
Formules : $\int \frac{u'}{u^n} = \frac{u^{1-n}}{1-n}$ ($n \neq 1$) ; IPP avec $v' = \sin(2x)$, $v = -\frac{\cos(2x)}2$ ; $\int \cos(2x) = \frac{\sin(2x)}2$ ; $t = \sqrt{x+2} \Rightarrow x = t^2 - 2$, $dx = 2t\,dt$ ; $\int \frac{dt}{1+t^2} = \arctan t$ ; $\arctan\sqrt3 = \frac\pi3$, $\arctan 1 = \frac\pi4$

1. Sans intégration par parties ni changement de variable, calculer $I = \displaystyle\int_0^1 \frac{2x^3 + 1}{(x^4 + 2x + 1)^3}\,dx$.
2. En intégrant par parties, calculer $J = \displaystyle\int_0^{\pi/4} (2x + 1)\sin(2x)\,dx$.
3. Calculer $K = \displaystyle\int_{-1}^1 \frac{dx}{(x + 3)\sqrt{x + 2}}$ en posant $t = \sqrt{x + 2}$.

## Exercice 2 : ensembles et fonctions (8,5 points)
Type : image directe et réciproque, injectivité, surjectivité, composée · ECUE : OBM · Niveau : maths-s1-obm/10
Formules : $f(A) = \{y \in F, \exists x \in A, y = f(x)\}$ ; $f^{-1}(B) = \{x \in E, f(x) \in B\}$ ; injective : $f(x) = f(x') \Rightarrow x = x'$ ; surjective : $\forall y, \exists x, y = f(x)$ ; $g \circ f$ injective si $f$, $g$ injectives ; surjective si $f$, $g$ surjectives

Dans cet exercice, les questions sont indépendantes.
1. Soient $E$ et $F$ deux ensembles, $f : E \to F$, $A \subset E$ et $B \subset F$. Rappeler la définition mathématique des ensembles $f(A)$ et $f^{-1}(B)$.
2. Soit $f : [\![1, 4]\!] \to [\![10, 14]\!]$ telle que $f(1) = 10$, $f(2) = 11$, $f(3) = 11$ et $f(4) = 13$. Donner $f([\![1, 4]\!])$, $f(\{3\})$, $f^{-1}(\{10, 11\})$ et $f^{-1}(\{12\})$.
3. Soit $g : \mathbb{R} \to \mathbb{R},\ x \mapsto |x| + 1$.
   (a) Dessiner le graphe de $g$.
   (b) $g$ est-elle injective ? Justifier. Si non, proposer deux intervalles $I_1$ et $J_1$ pour lesquels $g : I_1 \to J_1$ soit injective.
   (c) $g$ est-elle surjective ? Justifier. Si non, proposer deux intervalles $I_2$ et $J_2$ pour lesquels $g : I_2 \to J_2$ soit surjective.
4. Soient $E$, $F$ et $G$ trois ensembles, $f : E \to F$ et $g : F \to G$.
   (a) À partir de $f$ et $g$, quelle fonction composée $h$ peut-on faire ? Donner les domaines de départ et d'arrivée de cette fonction $h$.
   (b) On suppose $f$ et $g$ injectives. Montrer que $h$ est aussi injective.
   (c) (question bonus) On suppose $f$ et $g$ surjectives. Montrer que $h$ est aussi surjective.

## Exercice 3 : logique et relations (4 points)
Type : propriétés d'une relation, négation, contraposée · ECUE : OBM · Niveau : maths-s1-obm/11
Formules : réflexive $\forall x, x\mathcal Rx$ ; antisymétrique $x\mathcal Ry \wedge y\mathcal Rx \Rightarrow x = y$ ; transitive ; négation de $\forall(P \Rightarrow Q)$ : $\exists(P \wedge \neg Q)$ ; contraposée de $P \Rightarrow Q$ : $\neg Q \Rightarrow \neg P$ ; $\neg(A \wedge B) = \neg A \vee \neg B$ ; ordre = réflexive + antisymétrique + transitive

Soient $E$ un ensemble et $\mathcal{R}$ une relation sur $E$. Pour deux éléments $x$ et $y$ de $E$, on notera $x\,\mathcal{R}\,y$ si $x$ et $y$ sont en relation, sinon on notera $x\,\cancel{\mathcal{R}}\,y$.
1. Rappeler la définition mathématique de « $\mathcal{R}$ est réflexive ». Donner aussi sa négation.
2. Rappeler la définition mathématique de « $\mathcal{R}$ est antisymétrique ». Donner aussi sa négation.
3. Rappeler la définition mathématique de « $\mathcal{R}$ est transitive ». Donner aussi sa contraposée.
4. Proposer un exemple d'une relation $\mathcal{R}$ réflexive, antisymétrique et transitive. Comment appelle-t-on une telle relation ?

## Exercice 4 : dénombrement (6,5 points)
Type : combinaisons et arrangements avec contraintes · ECUE : DP · Niveau : maths-s1-dp/5
Formules : groupe sans ordre : $\binom nk$ ; postes distincts : principe multiplicatif $n(n-1)\dots$ ; « exactement $a$ de type 1 et $b$ de type 2 » : $\binom{n_1}a\binom{n_2}b$ ; « au moins » : somme des cas disjoints ; élément imposé : choisir parmi les restants ; disjonction de cas

Pierre et Marie sont dans une classe de 20 élèves. Dans cette classe, il y a 12 garçons et 8 filles.
1. On décide d'élire un comité de 3 élèves qui représentera la classe au niveau de l'école.
   (a) Combien y a-t-il de comités possibles ? Justifier brièvement.
   (b) Combien y a-t-il de comités contenant exactement 2 garçons et 1 fille ? Justifier brièvement.
   (c) Combien y a-t-il de comités contenant au moins 2 filles ? Justifier brièvement.
   (d) On veut que Pierre et Marie soient dans le comité. Combien y a-t-il de comités dans ce cas-là ? Justifier brièvement.
2. Les élèves de la classe doivent partir en week-end d'intégration. Pour cela, ils doivent créer un groupe de quatre responsables : un chef, un sous-chef et deux assistants (ces deux-là peuvent assister aussi bien le chef que le sous-chef). Personne ne peut occuper simultanément deux postes dans ce groupe.
   (a) Combien y a-t-il de groupes de responsables possibles ? Justifier brièvement.
   (b) On veut que le chef soit une fille, le sous-chef un garçon et parmi les deux assistants, on veut une fille et un garçon. Combien y a-t-il de groupes de responsables possibles dans ce cas-là ? Justifier brièvement.
   (c) C'est décidé : Marie sera la chef du groupe. Combien y a-t-il de groupes de responsables possibles dans ce cas-là ? Justifier brièvement.
   (d) « Si Marie est la chef alors je veux aussi faire partie du groupe des responsables ! » dit Pierre. Combien y a-t-il de groupes de responsables possibles dans ce cas-là ? Justifier brièvement.

## Exercice 5 : variables aléatoires (6,5 points)
Type : Bernoulli, binomiale, loi d'un rang d'apparition · ECUE : DP · Niveau : maths-s1-dp/14
Formules : Bernoulli $E = p$, $V = p(1-p)$ ; binomiale (tirages avec remise) $P(Y = k) = \binom nk p^k(1-p)^{n-k}$, $E = np$, $V = np(1-p)$ ; tirages sans remise : produit de probabilités conditionnelles ; $E(Z) = \sum kP(Z = k)$ ; $V = E(Z^2) - E(Z)^2$

Dans une urne, on a 3 boules blanches et 2 boules vertes indiscernables au toucher.
1. Proposer une expérience simple avec cette urne qui amène à la création d'une variable $X$ de Bernoulli. Donner $E(X)$ et $V(X)$.
2. Proposer une expérience simple avec cette urne qui amène à la création d'une variable $Y$ binomiale de paramètres $n = 5$ et $p = \frac25$. Donner $E(Y)$ et $V(Y)$.
3. On extrait une à une les boules de l'urne (c'est-à-dire qu'on effectue un tirage successif et sans remise !). Soit $Z$ la variable aléatoire égale au rang d'apparition de la première boule blanche tirée.
   (a) Quelles sont les valeurs prises par $Z$ ? Justifier brièvement.
   (b) Donner la loi de $Z$.
   (c) Calculer l'espérance de $Z$.
   (d) Calculer la variance de $Z$.

## Exercice 6 : probabilités conditionnelles (2,5 points)
Type : probabilités totales et Bayes · ECUE : DP · Niveau : maths-s1-dp/10
Formules : probabilités totales : $P(M) = P(M \mid V)P(V) + P(M \mid \bar V)P(\bar V)$ ; Bayes : $P(V \mid M) = \frac{P(M \mid V)P(V)}{P(M)}$ ; $P(\bar V) = 1 - P(V)$

On dispose de deux boîtes de bonbons A et B indiscernables. Dans A, il y a 10 sucettes au citron et 30 sucettes au coca. Dans B, il y a 25 sucettes au citron et 15 sucettes au coca. On choisit au hasard une boîte puis une sucette dans cette boîte.
1. Quelle est la probabilité pour que la sucette extraite soit au citron ? Vous détaillerez avec soin vos étapes avant de passer à l'application numérique.
2. Sachant que l'on a extrait une sucette au citron, quelle est la probabilité qu'elle provienne de la boîte A ?

## Exercice 7 : une démonstration (3 points)
Type : démonstration de cours ($E(aX+b)$) · ECUE : DP · Niveau : maths-s1-dp/13
Formules : $E(Y) = \sum_i y_iP(Y = y_i)$ ; $P(aX + b = ax_i + b) = P(X = x_i)$ ; $\sum_i P(X = x_i) = 1$ ; linéarité de $\sum$

Soient $(a,b) \in \mathbb{R}^2$ et $X$ une variable aléatoire finie. On note $X(\Omega) = \{x_1, x_2, \dots, x_n\}$ et $Y = aX + b$. Montrer que $E(Y) = aE(X) + b$.

## Exercice 8 : exercice original (4 points)
Type : binôme de Newton et double comptage · ECUE : DP · Niveau : maths-s1-dp/6
Formules : $(a + b)^n = \sum_{k=0}^n \binom nk a^kb^{n-k}$ ; $a = 1$, $b = 3$ ; principe multiplicatif $4^n$ ; double comptage : compter le même ensemble de deux façons ; $\binom nk$ façons de choisir $k$ cases

1. Rappeler la formule du binôme de Newton.
2. Grâce à cette formule, expliquer pourquoi $\displaystyle\sum_{k=0}^n \binom nk 3^{n-k} = 4^n$.
3. Le but est de redémontrer la formule ci-dessus par le dénombrement. Considérons $n$ cases. On veut colorier chaque case. Pour cela, on ne dispose que de 4 feutres de couleurs : un feutre bleu, un feutre vert, un feutre rouge et un feutre jaune.
   (a) Proposer une façon de colorier ces $n$ cases qui amène à : « il y a $4^n$ façons de colorier les cases ». Vous prendrez soin d'expliquer votre raisonnement proprement.
   (b) Proposer une autre façon de colorier ces $n$ cases qui amène à : « il y a $\displaystyle\sum_{k=0}^n \binom nk 3^{n-k}$ façons de colorier les cases ». Vous prendrez soin d'expliquer votre raisonnement proprement.
   (c) En déduire la formule voulue.
