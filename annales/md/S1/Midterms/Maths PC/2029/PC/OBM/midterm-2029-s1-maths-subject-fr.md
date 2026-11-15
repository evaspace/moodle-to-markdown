# Examen S1B1-OBM — octobre 2024 (sujet, FR)

- Source : `raw/S1/Midterms/Maths PC/2029/PC/OBM/midterm-2029-s1-maths-subject-fr.pdf` (10 pages)
- Date réelle : octobre 2024 (dossier promo 2029, ECUE OBM). Pas de corrigé.
- Durée : 2 h 30. Barème sur 40 points divisé par 2. 6 exercices. Rigueur prise en compte, malus d'un point pour manque de propreté. Documents et calculatrices interdits.

## Exercice 1 : logique (10 points)
Type : conditions nécessaires et suffisantes, négations, contraposée, inclusion · ECUE : OBM · Niveau : maths-s1-obm/6
Formules : $x^2 > 4 \iff x < -2$ ou $x > 2$ ; $A \Rightarrow P$ vraie si l'ensemble de $A$ est inclus dans celui de $P$ ; $\neg(A \Rightarrow B) \iff A \wedge \neg B$ ; contraposée $\neg B \Rightarrow \neg A$ (même table de vérité) ; $\cos \in [-1, 1]$ ; $A \subset B \iff \forall x, x \in A \Rightarrow x \in B$ ; contre-exemple pour $B \not\subset A$

Les questions sont indépendantes.
1. Soit $x \in \mathbb{R}$. On s'intéresse à la condition $P$ : « $x^2 > 4$ ». On dresse une liste de 5 propositions : (1) « $x > -2$ », (2) « $x < -10$ », (3) « $x > 1{,}9$ », (4) « $x < -3$ ou $x > 3$ » et (5) « $x < -2$ ou $x > 2$ ».
   (a) Donner la liste des implications du type « … $\Rightarrow P$ » qui sont vraies.
   (b) Donner la liste des implications du type « $P \Rightarrow$ … » qui sont vraies.
   (c) Pour chacune des implications vraies du 1.(b), donner leur négation.
2. On considère les assertions : $P$ : « $\forall x \in \mathbb{R}, \exists y \in \mathbb{R}, \cos(x) = y$ », $Q$ : « $\exists y \in \mathbb{R}, \forall x \in \mathbb{R}, x = \cos(y)$ » et $R$ : « $\exists x \in \mathbb{R}, \exists y \in \mathbb{R}, \cos(x) < \cos(y)$ ».
   (a) $P$, $Q$ et $R$ sont-elles vraies ? Justifier dans tous les cas.
   (b) Donner la négation de $P$, de $Q$ et de $R$.
3. Raisonnement par contraposée : soient $A$ et $B$ deux assertions.
   (a) Écrire la contraposée de $A \Rightarrow B$.
   (b) Montrer que $A \Rightarrow B$ et sa contraposée sont équivalentes.
   (c) Application : soit $a \in \mathbb{R}$. Montrer par contraposée que : $(\forall \varepsilon > 0, |a| \leqslant \varepsilon) \Rightarrow a = 0$. Vous prendrez soin de votre rédaction et vous écrirez clairement la contraposée dans ce cas-là.
   (d) La réciproque est-elle vraie ? Justifier.
4. Soient $A = \{(x, y, z) \in \mathbb{R}^3, x = y = z\}$ et $B = \{(x, y, z) \in \mathbb{R}^3, 2x - y - z = 0\}$.
   (a) De quel ensemble $A$ et $B$ sont-ils des sous-ensembles ?
   (b) Montrer soigneusement que $A \subset B$.
   (c) A-t-on $B \subset A$ ? Justifier.

## Exercice 2 : ensembles et fonctions 1 (7 points)
Type : image directe et réciproque, injectivité, surjectivité, composée · ECUE : OBM · Niveau : maths-s1-obm/10
Formules : $f(A) = \{y \in F, \exists x \in A, y = f(x)\}$ ; $f^{-1}(B) = \{x \in E, f(x) \in B\}$ ; injective : $f(x) = f(x') \Rightarrow x = x'$ ; surjective : $\forall y, \exists x, y = f(x)$ ; $g \circ f$ injective si $f$, $g$ injectives ; surjective si $f$, $g$ surjectives

1. Soient $A$ et $B$ deux ensembles, $f : A \to B$, $I \subset A$ et $J \subset B$. Rappeler la définition mathématique de $f(I)$ et $f^{-1}(J)$.
2. Soient $E = \{2, 3, 4\}$ et $F = \{1, 2, 3\}$. On définit la fonction $f : E \times F \to \mathbb{N},\ (x, y) \mapsto x + y$.
   (a) Remplir le tableau de valeurs de la fonction $f$ (ligne $(x, y)$, ligne $f((x, y))$).
   (b) Déterminer $f(E \times F)$, $f(\{(2, 2), (4, 3)\})$, $f^{-1}(\{1\})$ et $f^{-1}(\{6\})$.
   (c) Écrire la définition mathématique de : « $f$ injective de $E \times F$ vers $\mathbb{N}$ ». $f$ est-elle injective ? Justifier.
   (d) Écrire la définition mathématique de : « $f$ surjective de $E \times F$ vers $\mathbb{N}$ ». $f$ est-elle surjective ? Justifier.
   (e) Déterminer $I \subset E \times F$ et $J \subset \mathbb{N}$ tels que $f : I \to J$ soit injective, non surjective. (Les ensembles $I$ et $J$ doivent contenir au moins deux éléments.)
   (f) Déterminer $I' \subset E \times F$ et $J' \subset \mathbb{N}$ tels que $f : I' \to J'$ soit surjective, non injective. (Les ensembles $I'$ et $J'$ doivent contenir au moins deux éléments.)

## Exercice 3 : ensembles et fonctions 2 (3 points)
Type : image directe, image réciproque (lecture graphique) · ECUE : OBM · Niveau : maths-s1-obm/9
Formules : $f(A) = \{f(x), x \in A\}$ ; $f^{-1}(B) = \{x, f(x) \in B\}$ ; lire les valeurs prises (bornes ouvertes / fermées) ; $f(\mathbb{R})$ = ensemble des valeurs prises

Compléter le tableau suivant. N.B. : nous vous conseillons de dessiner le graphe des fonctions concernées au brouillon ! La fonction $\exp$ est $x \mapsto e^x$ et la fonction $\cos$ est $x \mapsto \cos(x)$.

| $f$ | $\exp : \mathbb{R} \to \mathbb{R}$ | $\cos : [0, \pi] \to \mathbb{R}$ |
|---|---|---|
| $f(\{0\})$ | | |
| $f\left(\left[0, \frac\pi2\right]\right)$ | | |
| $f^{-1}(\{0\})$ | | |
| $f^{-1}(\{-1\})$ | | |
| $f^{-1}(]-\infty, 0])$ | | |

## Exercice 4 : relations (4 points)
Type : propriétés d'une relation, négation, contraposée · ECUE : OBM · Niveau : maths-s1-obm/11
Formules : réflexive $\forall x, x\mathcal Rx$ ; antisymétrique $x\mathcal Ry \wedge y\mathcal Rx \Rightarrow x = y$ ; transitive ; négation de $\forall(P \Rightarrow Q)$ : $\exists(P \wedge \neg Q)$ ; contraposée de $P \Rightarrow Q$ : $\neg Q \Rightarrow \neg P$ ; $\neg(A \wedge B) = \neg A \vee \neg B$ ; ordre = réflexive + antisymétrique + transitive

Dans $\mathbb{R}$, on définit la relation $\mathcal{R}$ par : $\forall (a, b) \in \mathbb{R}^2$, $a\,\mathcal{R}\,b \iff |a| \leqslant |b|$.
1. Après avoir rappelé la définition, dire si $\mathcal{R}$ est réflexive. Justifier.
2. Après avoir rappelé la définition, dire si $\mathcal{R}$ est symétrique. Justifier.
3. Après avoir rappelé la définition, dire si $\mathcal{R}$ est antisymétrique. Justifier.
4. Après avoir rappelé la définition, dire si $\mathcal{R}$ est transitive. Justifier.

## Exercice 5 : intégrales (6 points)
Type : primitive $u'/u$, IPP trigonométrique, changement de variable vers arctan · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/13
Formules : $\int \frac{u'}u = \ln|u|$ ($2x + 2 = \frac12(4x + 4)$) ; IPP $\int_a^b uv' = [uv]_a^b - \int_a^b u'v$, $\int \cos\frac x3 = 3\sin\frac x3$ ; $t = \frac x{\sqrt3}$, $dx = \sqrt3\,dt$, $3 + x^2 = 3(1 + t^2)$ ; $\int \frac{dt}{1+t^2} = \arctan t$

Les questions sont indépendantes.
1. Calculer directement avec une primitive : $I = \displaystyle\int_0^1 \frac{2x + 2}{2x^2 + 4x + 1}\,dx$.
2. Via une intégration par parties, calculer $J = \displaystyle\int_0^\pi (x + 1)\cos\left(\frac x3\right)dx$. Vous poserez clairement les fonctions $u$, $u'$, $v$ et $v'$ et vous mettrez en évidence la formule.
3. Calculer $K = \displaystyle\int_0^{\sqrt3} \frac{1}{3 + x^2}\,dx$ en posant $t = \dfrac{x}{\sqrt3}$.

## Exercice 6 : nombres complexes (10 points)
Type : nombres complexes (cours, forme algébrique, module, forme exponentielle, équation) · ECUE : HP (nombres complexes, hors programme 2031)
Formules : $i^2 = -1$ ; $z = a + ib$ (forme algébrique), $\bar z = a - ib$, $|z| = \sqrt{a^2 + b^2}$ ; $\cos\theta = \frac a{|z|}$, $\sin\theta = \frac b{|z|}$ ; $z = |z|(\cos\theta + i\sin\theta) = |z|e^{i\theta}$ ; $|zw| = |z||w|$ ; $\frac{e^{i\alpha}}{e^{i\beta}} = e^{i(\alpha - \beta)}$ ; $\Delta < 0 \Rightarrow z = \frac{-b \pm i\sqrt{-\Delta}}{2a}$

Partie 1 : questions de cours. Soient $(a, b) \in \mathbb{R}^2$ et $z = a + ib$. Compléter :
1. Le nombre imaginaire $i$ vérifie : …
2. L'écriture $z = a + ib$ est l'écriture … de $z$.
3. L'ensemble des nombres complexes se note : …
4. Le conjugué de $z$ est (en fonction de $a$ et $b$) : …
5. Le module de $z$ est égal à (en fonction de $a$ et $b$) : …
6. Soit $\theta \in \mathbb{R}$ un argument de $z$. On a (en fonction de $a$ et $b$) : $\cos(\theta) = $ … et $\sin(\theta) = $ …
7. L'écriture trigonométrique de $z$ est : …
8. Soit $\theta \in \mathbb{R}$. On a $e^{i\theta} = $ …
9. Sur le repère fourni, placer le point $M$ d'affixe $z = -4 + 3i$. Indiquer graphiquement son module et un argument.

Partie 2 : exercices types (indépendants).
1. Donner la forme algébrique de $z = (3 - i)(2 - 4i)$.
2. Soient $z_1 = 4 + 3i$ et $z_2 = \sqrt2 - i\sqrt2$. Donner $|z_1|$, $|z_2|$ et $|z_1 \times \overline{z_2}|$.
3. Donner la forme trigonométrique ou exponentielle de $z_1 = 1 - i$, $z_2 = -\sqrt3 - i$, $\dfrac{z_1}{z_2}$ et $z_2^3$.
4. Résoudre dans $\mathbb{C}$ l'équation $z^2 - 3z + 3 = 0$.
