# S2 final exam — May 2022 (subject, EN)

- Source : `raw/S2/Finals/Maths PC/2026/final-2026-s2-maths-subject-en.pdf` (11 pages). Version anglaise de `final-2026-s2-maths-subject-fr.md` (mêmes exercices et données) ; énoncés repris en français ci-dessous.
- Date réelle : mai 2022 (dossier promo 2026). Corrigé : `final-2026-s2-maths-correction-fr.md`.
- Durée : 3 heures. Barème sur 40 points divisé par 2. 7 exercices. Rigueur prise en compte, malus d'un point pour manque de propreté. Documents et calculatrices interdits.

## Exercice 1 (6,5 points)
Type : développements limités usuels et composés · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/8
Formules : $e^u = \sum \frac{u^k}{k!}$ ; $\cos u = 1 - \frac{u^2}2 + \frac{u^4}{24}$ ; $\sin u = u - \frac{u^3}6$ ; $\ln(1+u) = u - \frac{u^2}2 + \frac{u^3}3 - \frac{u^4}4$ ; $\sqrt{1+u} = 1 + \frac u2 - \frac{u^2}8 + \frac{u^3}{16} - \frac{5u^4}{128}$ ; $(1+u)^\alpha = 1 + \alpha u + \frac{\alpha(\alpha-1)}2u^2$ ; produit tronqué ; composition : poser $u$, calculer $u^2$ à l'ordre voulu ; $1 + \cos 2x = 2\cos^2 x$

1. Rappeler les développements limités en 0 à l'ordre 4 de $e^u$, $\cos(u)$, $\sin(u)$, $\ln(1 + u)$ et $\sqrt{1 + u}$.
2. Donner le développement limité en 0 à l'ordre 4 de $f(x) = \ln(1 - 2x)\sin\left(\frac x2\right)$.
3. Donner le développement limité en 0 à l'ordre 4 de $g(x) = \sqrt{1 + \cos(2x)}$.

## Exercice 2 (4 points)
Type : développements limités, limite par équivalents · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/9
Formules : en 0 : $e^x = 1 + x + \frac{x^2}2 + \frac{x^3}6 + o(x^3)$ ; $\ln(1+x) = x - \frac{x^2}2 + o(x^2)$ ; $\cos x = 1 - \frac{x^2}2 + o(x^3)$ ; $\sin x = x - \frac{x^3}6 + o(x^3)$ ; $\frac1{1-x} = 1 + x + x^2 + x^3 + o(x^3)$ ; produit de DL tronqué à l'ordre ; $a^b = e^{b\ln a}$ ; $f \sim g \Rightarrow$ même limite

1. Calculer $\lim_{x \to 0} \dfrac{\cos(2x^2) - 1}{e^x - e^{-x} - 2x}$.
2. Calculer $\lim_{x \to +\infty} x^2\left(e^{\frac1{x^2}} - \cos\left(\frac1x\right)\right)$.

## Exercice 3 (5 points)
Type : inverse d'une matrice, application linéaire associée · ECUE : ALM · Niveau : maths-s2-alm/8
Formules : pivot de Gauss sur $AU = V$ ; $A$ inversible $\iff f$ bijective, $\mathrm{Mat}(f^{-1}) = A^{-1}$ ; colonnes de $A$ = images des vecteurs de la base de départ ; $g(aX^2 + bX + c) = ag(X^2) + bg(X) + cg(1)$

On considère l'endomorphisme $f$ de $\mathbb{R}^3$ dont la matrice dans la base canonique au départ et à l'arrivée est $A = \begin{pmatrix} 2 & 2 & 3 \\ 4 & 3 & 5 \\ -1 & -2 & -2 \end{pmatrix}$.
1. Inverser $A$.
2. L'endomorphisme $f$ est-il bijectif ? Justifier. Si oui, donner l'expression de $f^{-1}$.
3. Imaginons que $A$ corresponde aussi à la matrice de $g \in \mathcal{L}(\mathbb{R}_2[X], \mathbb{R}^3)$ dans les bases canoniques au départ et à l'arrivée. Quelle est l'expression de $g$ ? Justifier brièvement.

## Exercice 4 (5 points)
Type : familles libres, génératrices, bases ; coordonnées · ECUE : EV · Niveau : maths-s2-ev/7
Formules : libre : $\sum \lambda_ie_i = 0 \Rightarrow \lambda_i = 0$ ; en dimension $n$, une famille libre de $n$ vecteurs est une base ; plus de $n$ vecteurs $\Rightarrow$ liée ; coordonnées : résoudre $P = \alpha Q_1 + \beta Q_2 + \gamma Q_3$ en identifiant les coefficients

Dans cet exercice, les deux questions sont indépendantes.
1. On se place dans $E = \mathbb{R}_2[X]$ et on considère les familles $\mathcal{F}_1 = (P_1 = 1, P_2 = X^2 + X, P_3 = -X^2 - X - 2)$ et $\mathcal{F}_2 = (Q_1 = 1, Q_2 = X^2 + X + 1, Q_3 = X^2 - X)$. Ces familles sont-elles des bases de $E$ ? Justifiez rigoureusement votre réponse. Si oui, donner les coordonnées de $P = -X^2 + 7X + 5$ dans la (les) base(s) trouvée(s).
2. On se place dans $\mathbb{R}^3$. Soient les vecteurs $u = (2, 3, -1)$ et $v = (1, -1, -2)$.
   (a) La famille $(u, v)$ est-elle une base de $G = \mathrm{Vect}(u, v)$ ? Justifier.
   (b) Trouver $a \in \mathbb{R}$ tel que $w = (-15, 5, a) \in G$.

## Exercice 5 (8 points)
Type : noyau, image, rang ; matrice d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/5
Formules : $\mathrm{Ker} f$ : résoudre $f(P) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \dim\mathrm{Im} f$ ; injective $\iff \mathrm{Ker} = \{0\}$ ; $\dim\mathrm{Im} = \dim F \Rightarrow$ surjective ; colonne $j$ = coordonnées de $f(e_j)$ dans la base d'arrivée

On considère l'application linéaire $f : \mathbb{R}_2[X] \to \mathbb{R}^2,\ P \mapsto (P(0), P'(1))$.
1. Trouver une base du noyau de $f$. En déduire sa dimension.
2. Énoncer en toute généralité le théorème du rang. En déduire la dimension de l'image de $f$ dans notre cas.
3. $f$ est-elle injective ? $f$ est-elle surjective ? Justifier.
4. Donner la matrice de $f$ dans les bases canoniques au départ et à l'arrivée.
5. Donner la matrice de $f$ dans la base canonique au départ et la base $((2, 1), (-1, -1))$ à l'arrivée.

## Exercice 6 (8 points)
Type : projecteur, noyau et image · ECUE : ALM · Niveau : maths-s2-alm/10
Formules : projecteur $\iff f \circ f = f$ ; $E = \mathrm{Ker} f \oplus \mathrm{Im} f$ ; $f = id$ sur $\mathrm{Im} f$, $0$ sur $\mathrm{Ker} f$ ; matrice dans une base adaptée $\mathrm{diag}(0, \dots, 0, 1, \dots, 1)$

Soit $f \in \mathcal{L}(\mathbb{R}^3)$ dont la matrice dans la base canonique au départ et à l'arrivée est $A = \begin{pmatrix} 1 & 1 & 2 \\ 0 & 2 & 2 \\ 0 & -1 & -1 \end{pmatrix}$. On note $C_1$, $C_2$ et $C_3$ les trois vecteurs colonnes de $A$.
1. La famille $(C_1, C_2, C_3)$ est-elle libre ? Sinon, en extraire une famille libre maximale.
2. En déduire une base $\mathcal{B}_1$ de $\mathrm{Im}(f)$ et une base $\mathcal{B}_2$ de $\mathrm{Ker}(f)$. Donner leur dimension.
3. Montrer que $\mathrm{Im}(f) \oplus \mathrm{Ker}(f) = \mathbb{R}^3$. On crée alors la base $\mathcal{B}$ de $\mathbb{R}^3$ en réunissant les vecteurs de $\mathcal{B}_1$ et de $\mathcal{B}_2$.
4. Calculer $A^2$. Comment $f$ s'appelle-t-elle ?
5. Des questions 3. et 4., donner l'image par $f$ d'un vecteur quelconque de $\mathrm{Im}(f)$ puis d'un vecteur quelconque de $\mathbb{R}^3$.
6. En déduire, sans calcul, la matrice de $f$ dans la base $\mathcal{B}$ au départ et à l'arrivée.

## Exercice 7 (3,5 points)
Type : symétrie par rapport à un sous-espace · ECUE : ALM · Niveau : maths-s2-alm/10
Formules : $E = F \oplus G$ : $u = v + w$ unique ; projection sur $F$ : $u \mapsto v$ ; symétrie par rapport à $F$ parallèlement à $G$ : $u \mapsto v - w$, $s \circ s = id$

On considère $E = \mathbb{R}^2$, $F = \mathrm{Vect}((1, 1))$ et $G = \mathrm{Vect}((1, -1))$. On admet que $F \oplus G = E$. Ainsi, $\forall u \in E$, $\exists!\,(v, w) \in F \times G$ tel que $u = v + w$. On définit l'application linéaire $s : E \to E,\ u \mapsto v - w$.
1. Pour $u = (1, 3) \in \mathbb{R}^2$, trouver $v$ et $w$. En déduire $s(u)$.
2. Dessiner $F$ et $G$ dans $\mathbb{R}^2$. Placer le vecteur $u = (1, 3)$. Expliquer comment, graphiquement, on retrouve $v$, $w$ et $s(u)$ (les dessiner aussi). À votre avis, comment peut-on appeler l'endomorphisme $s$ ?
