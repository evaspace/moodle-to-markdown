# Contrôle 1 S1 — octobre 2019 (sujet, FR)

- Source : `raw/S1/Midterms/Maths PC/2024/midterm-2024-s1-maths-subject-fr.pdf` (8 pages)
- Date réelle : octobre 2019 (S1 2019, dossier promo 2024). Corrigé : `midterm-2024-s1-maths-correction-fr.md`.
- Durée : trois heures. Documents et calculatrices non autorisés. Barème : 20 points.

## Exercice 1 (2 points)
Type : vérité d'une proposition quantifiée · ECUE : OBM · Niveau : maths-s1-obm/4
Formules : $\forall$ : une seule valeur contre-exemple suffit pour réfuter ; $\exists$ : un seul exemple suffit pour prouver ; $\forall x \exists y$ : $y$ peut dépendre de $x$ ; $y^2 \geqslant 0$

Pour tous réels $x$ et $y$, soit $P(x,y)$ la proposition $x + y^2 = 0$. Les assertions suivantes sont-elles vraies ? Justifier votre réponse.
1. $\forall x \in \mathbb{R}, \forall y \in \mathbb{R}, P(x,y)$
2. $\forall x \in \mathbb{R}, \exists y \in \mathbb{R}, P(x,y)$
3. $\forall y \in \mathbb{R}, \exists x \in \mathbb{R}, P(x,y)$
4. $\exists x \in \mathbb{R}, \exists y \in \mathbb{R}, P(x,y)$

## Exercice 2 (4 points)
Type : dérivée composée, double IPP, changement de variable · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/13
Formules : $(\arctan u)' = \frac{u'}{1+u^2}$ ; IPP : $\int_a^b uv' = [uv]_a^b - \int_a^b u'v$ (deux fois pour un polynôme de degré 2) ; $\int \cos\frac x2 = 2\sin\frac x2$, $\int \sin\frac x2 = -2\cos\frac x2$ ; $u = e^x \Rightarrow dx = \frac{du}u$ ; $\int \frac{du}{u+1} = \ln(u+1)$

1. Soit $f : x \mapsto \arctan\left(\arctan(x)\right)$. Déterminer $f'(x)$.
2. Via une double intégration par parties, déterminer $J = \displaystyle\int_0^\pi (x^2 + x)\cos\left(\frac x2\right)dx$.
3. Via le changement de variable $u = e^x$, déterminer $K = \displaystyle\int_0^1 \frac{dx}{1 + e^{-x}}$.

## Exercice 3 (2 points)
Type : injectivité / surjectivité, composées · ECUE : OBM · Niveau : maths-s1-obm/10
Formules : injective : $f(x) = f(y) \Rightarrow x = y$, contre-exemple $f(a) = f(b)$ avec $a \neq b$ ; surjective : $\forall y, \exists x, f(x) = y$ ; $(f \circ g)(x) = f(g(x))$

Soient $E = \mathbb{N}$ et $F = 2\mathbb{N}$ où $2\mathbb{N}$ désigne l'ensemble des entiers naturels pairs. Soient $f : E \to F,\ x \mapsto 2x + 4$ et $g : F \to E,\ x \mapsto \frac x2 + 2$ (expressions confirmées par le corrigé).
1. $f$ est-elle injective ? Surjective ? Justifiez votre réponse.
2. $g$ est-elle injective ? Surjective ? Justifiez votre réponse.

## Exercice 4 (1,5 points)
Type : relation d'équivalence · ECUE : OBM · Niveau : maths-s1-obm/11
Formules : équivalence = réflexive ($x\mathcal Rx$), symétrique ($x\mathcal Ry \Rightarrow y\mathcal Rx$), transitive ($x\mathcal Ry$ et $y\mathcal Rz \Rightarrow x\mathcal Rz$)

Sur $E = \mathbb{Z} \times \mathbb{Z}^*$ on définit la relation $\mathcal{R}$ par $(a,b)\,\mathcal{R}\,(a',b') \iff ab' = ba'$. Montrer que $\mathcal{R}$ est une relation d'équivalence.

## Exercice 5 (3 points)
Type : dénombrement (p-listes, arrangements, anagrammes, parties) · ECUE : DP · Niveau : maths-s1-dp/3
Formules : $p$-listes (avec remise, ordre) : $n^p$ ; arrangements (sans remise, ordre) : $A_n^p = \frac{n!}{(n-p)!}$ ; permutations : $n!$ ; anagrammes avec lettres répétées : $\frac{n!}{k_1!k_2!\dots}$ ; nombre de parties d'un ensemble à $m$ éléments : $2^m$ ; principe multiplicatif

1. Un sac contient $n$ balles de tennis de table numérotées de 1 à $n$. On tire successivement $p$ balles du sac en remettant chaque fois dans ce dernier la balle qu'on vient de sélectionner. Quel est le nombre de tirages possibles ?
2. Même question si à chaque tirage, on ne remet pas la balle sélectionnée dans le sac.
3. Déterminer le nombre d'anagrammes des mots « table » et « tableau ».
4. Imaginons une association de l'EPITA constituée de $n$ membres ($n \in \mathbb{N}^*$). Appelons bureau le choix d'un ensemble de conseillers dont le nombre peut aller de 1 à $n$ ainsi qu'un président faisant partie des conseillers. Déterminer le nombre de tels bureaux.

## Exercice 6 (3 points)
Type : tirages simultanés, combinaisons · ECUE : DP · Niveau : maths-s1-dp/7
Formules : tirage simultané de $k$ parmi $n$ : $\binom nk$ ; « A ou B » incompatibles : additionner ; « A et B » : multiplier les $\binom{}{}$ ; contraire : $P(\bar A) = 1 - P(A)$ ; équiprobabilité

Dans cet exercice, l'application numérique exacte n'est pas demandée : si les résultats s'expriment sous forme de fractions, on demande juste de déterminer explicitement les numérateurs et les dénominateurs.
Un sac contient 2 balles blanches, 3 vertes et 5 rouges. On pioche simultanément 3 balles. Déterminer la probabilité, lors du piochage de ces 3 balles, d'avoir
1. une seule couleur ?
2. les trois couleurs parmi ces 3 balles ?
3. au moins deux couleurs ?

## Exercice 7 (2 points)
Type : indépendance et incompatibilité · ECUE : DP · Niveau : maths-s1-dp/11
Formules : indépendants $\iff P(A \cap B) = P(A)P(B) \iff P_B(A) = P(A)$ ; $P_B(A) = \frac{P(A \cap B)}{P(B)}$ ; incompatibles $\iff A \cap B = \emptyset$

On jette un dé à 8 faces capricieux dont on appelle $X$ le résultat du jet. On obtient la situation suivante :

| $k$ (n° obtenu après le jet) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| $P(X = k)$ | 0,05 | 0,1 | 0,05 | 0,2 | 0,1 | 0,3 | 0,1 | 0,1 |

Les événements « $X$ pair » et « $X \leqslant 4$ » sont-ils indépendants ? Incompatibles ?

## Exercice 8 (3 points)
Type : probabilités totales et Bayes · ECUE : DP · Niveau : maths-s1-dp/10
Formules : probabilités totales : $P(M) = P(M \mid V)P(V) + P(M \mid \bar V)P(\bar V)$ ; Bayes : $P(V \mid M) = \frac{P(M \mid V)P(V)}{P(M)}$ ; $P(\bar V) = 1 - P(V)$

Dans une petite ville de province, 10000 personnes sont âgées de plus de 65 ans. 60 % d'entre elles ont pris la précaution de se faire vacciner contre la grippe. Au cours de l'hiver, les médecins observent que 10 % d'entre elles ont attrapé la grippe. Parmi celles-ci, 6 % étaient vaccinées.
1. Déterminer la probabilité d'attraper la grippe
   a. pour une personne vaccinée ;
   b. pour une personne non vaccinée.
   N.B. : on demande le résultat sous forme de fraction.
2. Notons $c$ le résultat de la question 1)b) précédente. Déterminer, en fonction de $c$, le taux de vaccination des personnes âgées pour qu'il y ait 500 personnes malades de la grippe.
