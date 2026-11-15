# Contrôle 1 S1 — octobre 2018 (sujet, FR)

- Source : `raw/S1/Midterms/Maths PC/2023/midterm-2023-s1-maths-subject-fr.pdf` (scan, 6 pages)
- Date réelle : octobre 2018 (S1 18/19, dossier promo 2023). Pas de corrigé.
- Durée : trois heures. Documents et calculatrices non autorisés. Barème : 21 points.

## Exercice 1 (2,5 points)
Type : image directe, image réciproque (lecture graphique) · ECUE : OBM · Niveau : maths-s1-obm/9
Formules : $f(A) = \{f(x), x \in A\}$ ; $f^{-1}(B) = \{x, f(x) \in B\}$ ; lire les valeurs prises (bornes ouvertes / fermées) ; $f(\mathbb{R})$ = ensemble des valeurs prises

Soit $f : \mathbb{R} \to \mathbb{R}$ dont le graphe est donné (fonction en escalier, lue sur la figure) : $f = -3$ sur $[-6, -4[$, $f = -2$ sur $[-4, -2[$, $f = -1$ sur $[-2, 0[$, $f = 0$ sur $[0, 2[$, $f = 1$ sur $[2, 4[$, $f = 2$ sur $[4, 6[$ (soit $f(x) = \lfloor x/2 \rfloor$ sur la portion tracée).
Déterminer $f([0, 4])$, $f^{-1}([0, 1])$, $f^{-1}(\{0, 1\})$, $f(\mathbb{R})$ et $f^{-1}([-1, 1])$.

## Exercice 2 (1,5 points)
Type : image réciproque d'un singleton · ECUE : OBM · Niveau : maths-s1-obm/9
Formules : $f^{-1}(\{b\}) = \{x, f(x) = b\}$ ; séparer les cas $n$ pair ($n = 2k$) et impair

Soit $f : \mathbb{N} \to \mathbb{N}$ définie pour tout $n \in \mathbb{N}$ par $f(n) = \frac n2$ si $n$ pair et $f(n) = 0$ sinon.
Déterminer $f^{-1}(\{0\})$, $f^{-1}(\{1\})$ et $f^{-1}(\{2\})$.

## Exercice 3 (2 points)
Type : dériver une composée · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/1
Formules : $(g \circ u)' = u' \times g' \circ u$ ; $(e^u)' = u'e^u$ ; $(\sqrt u)' = \frac{u'}{2\sqrt u}$ ; $(u^n)' = nu'u^{n-1}$ ; $(\ln u)' = \frac{u'}u$

Soient $f$ et $g$ les fonctions définies par $f(x) = \sqrt{\arctan(\sqrt x)}$ et $g(x) = x^x$. Déterminer $f'(x)$ et $g'(x)$ (sans se préoccuper du domaine de définition).
N.B. : n'essayez pas de simplifier les résultats.

## Exercice 4 (4 points)
Type : intégrales (primitive directe, IPP, changement de variable) · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/13
Formules : $\int u'u = \frac{u^2}2$ ($u = \arctan$, $u' = \frac1{1+x^2}$) ; IPP : $\int uv' = [uv] - \int u'v$ avec $u = \ln x$, $v' = \frac1{x^2}$, $v = -\frac1x$ ; $u = \ln t \Rightarrow du = \frac{dt}t$ ; $u = \sqrt x \Rightarrow dx = 2u\,du$ ; $\int \frac{du}{1+u^2} = \arctan u$ ; $1 - u^2 = (1-u)(1+u)$

1. Déterminer, sans intégration par parties ni changement de variable, $I = \displaystyle\int_0^1 \frac{2x + 3}{(x^2 + 3x + 4)^2}\,dx$.
2. Via une intégration par parties, déterminer $J = \displaystyle\int_1^e \ln(x)\,dx$ puis via une nouvelle intégration par parties, déterminer $K = \displaystyle\int_1^e \ln^2(x)\,dx$.
3. Via le changement de variable $u = \sqrt x$, déterminer $L = \displaystyle\int_1^4 \frac{1 + e^{\sqrt x}}{\sqrt x}\,dx$.

## Exercice 5 (3 points)
Type : équation du second degré à coefficients complexes · ECUE : HP (nombres complexes, hors programme 2031)
Formules : $\Delta = b^2 - 4ac$ ; racine carrée $\delta = a + ib$ de $\Delta$ : $a^2 - b^2 = \mathrm{Re}\,\Delta$, $a^2 + b^2 = |\Delta|$, $2ab = \mathrm{Im}\,\Delta$ ; $z = \frac{-b \pm \delta}{2a}$

On rappelle dans cet exercice que $13^2 = 169$. Soit l'équation $(E)$ suivante : $z^2 - 5z + 5 - 3i = 0$.
1. Montrer que $\Delta = 5 + 12i$.
2. Déterminer une racine carrée de $\Delta$.
3. En déduire les solutions dans $\mathbb{C}$ de l'équation $(E)$.

## Exercice 6 (3 points)
Type : injectivité / surjectivité, composées · ECUE : OBM · Niveau : maths-s1-obm/10
Formules : injective : $f(x) = f(y) \Rightarrow x = y$, contre-exemple $f(a) = f(b)$ avec $a \neq b$ ; surjective : $\forall y, \exists x, f(x) = y$ ; $(f \circ g)(x) = f(g(x))$

Soient $f : \mathbb{R}^2 \to \mathbb{R},\ (x,y) \mapsto xy$ et $g : \mathbb{R} \to \mathbb{R}^2,\ x \mapsto (x, x^2)$.
1. $f$ est-elle injective ? Surjective ? Justifiez votre réponse.
2. $g$ est-elle injective ? Surjective ? Justifiez votre réponse.
3. Déterminer $f \circ g$ et $g \circ f$.

## Exercice 7 (2 points)
Type : dénombrement de mains de cartes · ECUE : DP · Niveau : maths-s1-dp/5
Formules : $|\Omega| = \binom{32}5$ ; « au moins un » : complémentaire $P(A) = 1 - P(\bar A)$ ; $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ ; principe multiplicatif (choisir chaque catégorie séparément) ; équiprobabilité $P = \frac{|A|}{|\Omega|}$

Dans un jeu de 32 cartes, on tire une main de 5 cartes. Déterminer la probabilité qu'une main contienne
- au moins un As ;
- le roi de carreau et 3 trèfles dont l'As.

## Exercice 8 (3 points)
Type : probabilités totales et Bayes · ECUE : DP · Niveau : maths-s1-dp/10
Formules : probabilités totales : $P(M) = P(M \mid V)P(V) + P(M \mid \bar V)P(\bar V)$ ; Bayes : $P(V \mid M) = \frac{P(M \mid V)P(V)}{P(M)}$ ; $P(\bar V) = 1 - P(V)$

En région parisienne, 60 % des personnes âgées de plus de 65 ans sont vaccinées contre la grippe. La proportion de malades est de 0,1 % parmi les vaccinés et de 10 % parmi les non vaccinés.
1. Déterminer le pourcentage de personnes âgées de plus de 65 ans atteintes par la grippe dans cette région.
2. On sélectionne une personne âgée de plus de 65 ans en région parisienne et on constate qu'elle a contracté la grippe. Quelle est la probabilité qu'elle ait été vaccinée ?
   N.B. : on demande juste ici la formule littérale permettant de déterminer cette probabilité mais pas l'application numérique.
