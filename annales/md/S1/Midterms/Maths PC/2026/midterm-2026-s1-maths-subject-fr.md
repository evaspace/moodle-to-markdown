# Contrôle S1 — novembre 2021 (sujet, FR)

- Source : `raw/S1/Midterms/Maths PC/2026/midterm-2026-s1-maths-subject-fr.pdf` (9 pages)
- Date réelle : novembre 2021 (dossier promo 2026). Corrigé : `midterm-2026-s1-maths-correction-fr.md`.
- Durée : 3 heures. Barème sur 30 points ramené à 20. 8 exercices. Documents et calculatrices interdits.

## Exercice 1 (3 points)
Type : relation d'ordre · ECUE : OBM · Niveau : maths-s1-obm/11
Formules : ordre = réflexive ($\forall x, x\mathcal Rx$), antisymétrique ($x\mathcal Ry$ et $y\mathcal Rx \Rightarrow x = y$), transitive ($x\mathcal Ry$ et $y\mathcal Rz \Rightarrow x\mathcal Rz$) ; contre-exemple pour réfuter ; $x^2 = y^2 \iff x = \pm y$

Dans $\mathbb{R}$, on définit la relation suivante : $\forall (x,y) \in \mathbb{R}^2$, $x\,\mathcal{R}\,y \iff x^2 \leqslant y^2$.
Citer les différentes propriétés (avec les quantificateurs) qui définissent une relation d'ordre. Pour chacune d'entre elles, dire si la relation $\mathcal{R}$ ci-dessus la vérifie en justifiant votre réponse.

## Exercice 2 (3 points)
Type : traduire avec quantificateurs · ECUE : OBM · Niveau : maths-s1-obm/4
Formules : « tout » $= \forall$, « il existe » $= \exists$, « aucun » $= \forall \dots \neg$ ; l'ordre $\forall\exists$ / $\exists\forall$ change le sens ; $f$ s'annule : $\exists x, f(x) = 0$ ; minimum en $a$ : $\exists a, \forall x, f(x) \geqslant f(a)$ ; pair : $\exists k, n = 2k$

Traduire les propriétés suivantes en syntaxe mathématique (avec les quantificateurs).
1. Tout réel positif est le carré d'un réel.
2. Si le produit de deux réels est nul alors l'un au moins de ces réels est nul.
3. Tout entier naturel est pair ou impair. (Il est interdit dans cette question d'utiliser la notion de congruence.)

## Exercice 3 (4,5 points)
Type : primitive directe $u'u^\alpha$, IPP, changement de variable affine vers arctan · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/13
Formules : $\int u'u^\alpha = \frac{u^{\alpha+1}}{\alpha+1}$ ($\alpha = \frac12$ : $\frac23u^{3/2}$) ; IPP $\int uv' = [uv] - \int u'v$ ; $\int e^{2x} = \frac{e^{2x}}2$ ; $x = 2t + 1$, $dx = 2\,dt$, bornes transformées ; $\int \frac{dt}{1 + t^2} = \arctan t$ ; $\arctan\sqrt3 = \frac\pi3$

1. Calculer directement $I = \displaystyle\int_0^1 (x^2 + 1)\sqrt{x^3 + 3x + 1}\,dx$.
2. Calculer, en intégrant par parties, $J = \displaystyle\int_0^1 (2x + 1)e^{2x}\,dx$.
3. À l'aide du changement de variable $x = 2t + 1$, calculer $K = \displaystyle\int_1^{2\sqrt3 + 1} \frac{dx}{(x - 1)^2 + 4}$.

## Exercice 4 (3,5 points)
Type : injectivité, surjectivité, image directe et réciproque · ECUE : OBM · Niveau : maths-s1-obm/10
Formules : injective : $f(x) = f(y) \Rightarrow x = y$ (contre-exemple $f(1) = f(2)$) ; surjective : $\forall y, \exists x, f(x) = y$ ; $f(A) = \{f(x), x \in A\}$ ; $f^{-1}(B) = \{x, f(x) \in B\}$ (peut être vide)

On considère la fonction $f : \mathbb{N} \to \mathbb{N}$ définie par $f(n) = \frac n2$ si $n$ est pair et $f(n) = n$ sinon.
1. $f$ est-elle injective ? Justifiez votre réponse.
2. $f$ est-elle surjective ? Justifiez votre réponse.
3. On suppose, dans cette question, que l'on restreint le domaine de départ de $f$ à $E = \{0, 1, 2, 3, 4, 5, 6\}$. Donner $f(\{0, 1, 2, 3\})$, $f^{-1}(\{1, 3\})$ et $f^{-1}(\{4\})$.

## Exercice 5 (5 points)
Type : combinaisons, formule de Pascal · ECUE : DP · Niveau : maths-s1-dp/6
Formules : tirage simultané : $\binom nk$ ; contenant un élément fixé : $\binom{n-1}{k-1}$ ; ne le contenant pas : $\binom{n-1}k$ ; Pascal : $\binom{n-1}{k-1} + \binom{n-1}{k} = \binom nk$ ; $\binom nk = \frac{n!}{k!(n-k)!}$ ; mettre au même dénominateur $k!(n-k)!$

Dans une urne, il y a $n$ boules indiscernables au toucher et numérotées de 1 à $n$. Pour un entier naturel $k \leqslant n$, on tire simultanément $k$ boules de l'urne.
1. Quel est le nombre de tirages possibles ? Justifiez brièvement.
2. Quel est le nombre de tirages ayant la boule numérotée 1 ? Justifiez brièvement.
3. Quel est le nombre de tirages n'ayant pas la boule numérotée 1 ? Justifiez brièvement.
4. Expliquez en quoi les résultats précédents permettent de montrer la formule $(P)$ suivante : $\dbinom{n-1}{k-1} + \dbinom{n-1}{k} = \dbinom nk$.
5. Redémontrer la formule $(P)$ en utilisant l'expression des coefficients binomiaux avec les factorielles.

## Exercice 6 (5 points)
Type : loi de Bernoulli, loi binomiale, espérance et variance · ECUE : DP · Niveau : maths-s1-dp/14
Formules : Bernoulli $\mathcal{B}(p)$ : $E = p$, $V = p(1-p)$ ; binomiale $\mathcal{B}(n,p)$ : $P(Y = k) = \binom nk p^k(1-p)^{n-k}$, $E = np$, $V = np(1-p)$ ; $E(G) = \sum x_iP(G = x_i)$ ; $V(G) = E(G^2) - E(G)^2$ (König-Huygens)

On dispose d'un dé équilibré à 6 faces numérotées de 1 à 6.
1. Proposer une expérience simple qui amène à la création d'une variable aléatoire $X$ suivant une loi de Bernoulli de paramètre $p = \frac16$. Rappeler l'espérance et la variance de $X$ en fonction de $p$.
2. Proposer une expérience simple qui amène à la création d'une variable aléatoire $Y$ suivant une loi binomiale de paramètres $n = 10$ et $p = \frac16$. Rappeler l'espérance et la variance de $Y$ en fonction de $n$ et de $p$.
3. On lance le dé une seule fois. On gagne 5 points si le dé amène un multiple de 3, 3 points si le dé amène 1 ou 2 et zéro point dans les autres cas. Soit $G$ la variable égale au nombre de points marqués. Donner la loi de $G$ et calculer son espérance et sa variance.

## Exercice 7 (4 points)
Type : probabilités totales et Bayes · ECUE : DP · Niveau : maths-s1-dp/10
Formules : probabilités totales : $P(M) = P(M \mid V)P(V) + P(M \mid \bar V)P(\bar V)$ ; Bayes : $P(V \mid M) = \frac{P(M \mid V)P(V)}{P(M)}$ ; $P(\bar V) = 1 - P(V)$

Imaginons qu'un virus touche les habitants du monde entier. Des tests de dépistage du virus sont alors mis en vente. Le mode d'emploi précise que :
- si un individu n'est pas malade, le test est fiable dans 80 % des cas ;
- si un individu est malade, le test est fiable dans 99 % des cas.
On suppose que le virus touche 25 % de la population française. On tire un habitant au hasard et on lui fait passer le test. On note $M$ : « L'habitant est malade » et $T$ : « Le test est positif ».
1. Donner une partition de l'événement $T$ en fonction de $M$. Donner alors la formule littérale qui permet de calculer $P(T)$. Préciser les valeurs numériques de chacune des probabilités y apparaissant (sans finaliser les calculs).
2. Expliquer comment calculer la probabilité qu'un habitant soit malade sachant que le test est positif (la valeur finale n'est pas demandée).

## Exercice 8 (2 points)
Type : récurrence (somme géométrique) · ECUE : OBM · Niveau : maths-s1-obm/7
Formules : récurrence ; $S_{n+1} = S_n + q^{n+1}$ ; $\sum_{k=0}^n q^k = \frac{1 - q^{n+1}}{1 - q}$ ($q \neq 1$), $= n + 1$ si $q = 1$

Soit $q \in \mathbb{R}$. Pour tout $n \in \mathbb{N}$, on considère la somme $S_n = \displaystyle\sum_{k=0}^n q^k = q^0 + q^1 + q^2 + \dots + q^n$.
1. Que vaut $S_n$ dans le cas où $q = 1$ ?
2. On suppose que $q \neq 1$. Montrer par récurrence que, pour tout $n \in \mathbb{N}$, $S_n = \dfrac{1 - q^{n+1}}{1 - q}$.
