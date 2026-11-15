# Feuille de TD — Applications linéaires (S2 2026) (sujet, FR)

- Source : `raw/S2/TDs/2030/Maths/td5-2030-s2-maths-subject-fr.pdf` (8 pages)
- Date réelle : S2 2026 (dossier promo 2030). Feuille de TD, ECUE ALM. Pas de corrigé dans les annales. Corrigé rédigé : `td5-2030-s2-maths-correction-fr.md` (même dossier).
- Seuls les exercices sont transcrits. Les exercices marqués ⋆ sont plus difficiles. Le théorème du rang n'a pas de MiMo : à apprendre par cœur.

## Exercice 1.1
Type : application linéaire (caractérisation) · ECUE : ALM · Niveau : maths-s2-alm/1
Formules : $f$ linéaire $\Rightarrow f(0) = 0$ et $f(2x) = 2f(x)$ (conditions nécessaires) ; réciproquement vérifier $f(\lambda x + y) = \lambda f(x) + f(y)$ ; les applications linéaires de $\mathbb{R}$ dans $\mathbb{R}$ sont $x \mapsto bx$

On se place dans le cas d'une fonction numérique d'une variable réelle.
1. Soit $f$ une fonction de $\mathbb{R}$ dans $\mathbb{R}$, que signifie « $f$ est linéaire » ? Quelle est sa représentation graphique dans le plan ?
2. On suppose $f$ linéaire. Soient $u$ et $v$ deux réels, quelle est l'image de $u + v$ par $f$ ? Soit $\alpha$ un réel, que dire de l'image de $\alpha u$ ? Que vaut $f(0)$ ?
3. Soit $g$ une fonction affine de $\mathbb{R}$ dans $\mathbb{R}$. Répondez à nouveau aux questions précédentes.
4. Soit $h$ la fonction carré de $\mathbb{R}$ dans $\mathbb{R}$. Répondez à nouveau aux mêmes questions.

## Exercice 1.2
Type : application linéaire (caractérisation) · ECUE : ALM · Niveau : maths-s2-alm/1
Formules : $f$ linéaire $\Rightarrow f(0) = 0$ et $f(2x) = 2f(x)$ (conditions nécessaires) ; réciproquement vérifier $f(\lambda x + y) = \lambda f(x) + f(y)$ ; les applications linéaires de $\mathbb{R}$ dans $\mathbb{R}$ sont $x \mapsto bx$

Les applications suivantes sont-elles linéaires ?
- $f_1 : \mathbb{R}^3 \to \mathbb{R}^2$, $(x,y,z) \mapsto (2x - z,\ 3x + y + z)$
- $f_2 : \mathbb{R}^3 \to \mathbb{R}^2$, $(x,y,z) \mapsto (2x - z,\ 3x + 2 + z)$
- $f_3 : \mathbb{R}^2 \to \mathbb{R}^3$, $(x,y) \mapsto (x + y,\ -y,\ 2x - y)$
- $f_4 : \mathbb{R}^2 \to \mathbb{R}^3$, $(x,y) \mapsto (x - y,\ xy,\ 2x)$
- (⋆) $f_5 : \mathbb{R}^p \to \mathbb{R}^n$, $\begin{pmatrix} x_1 \\ \vdots \\ x_p \end{pmatrix} \mapsto \begin{pmatrix} a_{11}x_1 + \dots + a_{1p}x_p \\ \vdots \\ a_{n1}x_1 + \dots + a_{np}x_p \end{pmatrix}$ où les $a_{ij}$ sont des réels.
- (Travail personnel) $f_6 : E \to E$, $\begin{pmatrix} a & b \\ c & d \end{pmatrix} \mapsto \begin{pmatrix} a - b & b - c \\ d & d \end{pmatrix}$ où $E = \left\{ \begin{pmatrix} a & b \\ c & d \end{pmatrix},\ (a,b,c,d) \in \mathbb{R}^4 \right\}$ est le $\mathbb{R}$-ev étudié au cours du TD précédent.
- $f_7 : \mathbb{R}^{\mathbb{N}} \to \mathbb{R}^2$, $(u_n) \mapsto (u_0, u_1)$
- $f_8 : \mathbb{R}^{\mathbb{N}} \to \mathbb{R}^2$, $(u_n) \mapsto (u_0, |u_1|)$
- $f_9 : \mathbb{R}[X] \to \mathbb{R}[X]$, $P \mapsto 2(X+1)P - X^2$
- $f_{10} : \mathbb{R}[X] \to \mathbb{R}[X]$, $P \mapsto 2(X+1)P - (X^2 - 2X + 1)P'$
- $\varphi : C^0(\mathbb{R}) \to \mathbb{R}$, $f \mapsto \displaystyle\int_0^1 f(t)\,dt$ où $C^0(\mathbb{R})$ est l'ensemble des fonctions continues de $\mathbb{R}$ dans $\mathbb{R}$ (bornes de l'intégrale lues 0 et 1 ; la borne basse est perdue dans la couche texte).

## Exercice 2.3
Type : noyau, image, rang d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/3
Formules : linéaire : $f(\lambda u + v) = \lambda f(u) + f(v)$ ; $\mathrm{Ker} f$ : résoudre $f(x) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \mathrm{rg} f$ ; $\mathrm{rg} f = \dim F \Rightarrow \mathrm{Im} f = F$ (surjective) ; $\mathrm{Im} f = \mathrm{Vect}(f(e_1), \dots, f(e_n))$

1. Soient $E$ et $F$ deux $\mathbb{R}$-espaces vectoriels et $f \in \mathcal{L}(E,F)$. Rappeler la définition du noyau de $f$ et la définition de l'image de $f$. Montrer que le noyau de $f$ est un sev de $E$ et que l'image de $f$ est un sev de $F$.
2. Soit $f : \mathbb{R}^2 \to \mathbb{R}^2$, $(x,y) \mapsto (x + y, 0)$.
   - (a) Montrer que $f$ est linéaire.
   - (b) Déterminer le noyau de $f$ et le représenter dans le plan.
   - (c) Déterminer l'image de $f$ et la représenter dans le plan.
   - (d) De quel type de sous-ensembles de $\mathbb{R}^2$ s'agit-il ?

## Exercice 2.4
Type : noyau, image, rang d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/3
Formules : linéaire : $f(\lambda u + v) = \lambda f(u) + f(v)$ ; $\mathrm{Ker} f$ : résoudre $f(x) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \mathrm{rg} f$ ; $\mathrm{rg} f = \dim F \Rightarrow \mathrm{Im} f = F$ (surjective) ; $\mathrm{Im} f = \mathrm{Vect}(f(e_1), \dots, f(e_n))$

Déterminer le noyau et l'image des applications linéaires suivantes. Les exprimer sous forme d'espaces vectoriels engendrés lorsque c'est possible.
- $f_1 : \mathbb{R}^3 \to \mathbb{R}^2$, $(x,y,z) \mapsto (x - y,\ 2x - y + z)$
- $f_2 : \mathbb{R}^3 \to \mathbb{R}^3$, $(x,y,z) \mapsto (x,\ x + z,\ z)$
- $f_3 : \mathbb{R}^2 \to \mathbb{R}^3$, $(x,y) \mapsto (x,\ 2x + y,\ 3y)$
- $f_4 : \mathbb{R}_2[X] \to \mathbb{R}_2[X]$, $P \mapsto P'$. Même question si $f_4 : \mathbb{R}[X] \to \mathbb{R}[X]$.
- $f_5 : \mathbb{R}[X] \to \mathbb{R}^2$, $P \mapsto (P(0), P(1))$

## Exercice 2.5
Type : injectivité et noyau · ECUE : ALM · Niveau : maths-s2-alm/2
Formules : $f$ linéaire : $f(0) = 0$, $f(x) - f(y) = f(x - y)$ ; $f$ injective $\iff \mathrm{Ker} f = \{0\}$

Soient $E$, $F$ deux $\mathbb{R}$-ev et $f \in \mathcal{L}(E,F)$.
1. - (a) Montrer que si $f$ est injective alors : $\forall u \in E$, $f(u) = 0_F \Rightarrow u = 0_E$.
   - (b) Montrer que si $\mathrm{Ker}(f) = \{0_E\}$ alors : $\forall (u,v) \in E^2$, $f(u) = f(v) \Rightarrow u = v$.
   - (c) Montrer que $f$ est injective si et seulement si $\mathrm{Ker}(f) = \{0_E\}$.
2. Montrer que $f$ est surjective si et seulement si $\mathrm{Im}(f) = F$.

## Exercice 2.6
Type : injectivité et noyau · ECUE : ALM · Niveau : maths-s2-alm/2
Formules : $f$ linéaire : $f(0) = 0$, $f(x) - f(y) = f(x - y)$ ; $f$ injective $\iff \mathrm{Ker} f = \{0\}$

Indiquer pour chacune des applications de l'exercice 2.4 si elle est injective et/ou surjective.

## Exercice 3.7
Type : noyau, image, rang d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/3
Formules : linéaire : $f(\lambda u + v) = \lambda f(u) + f(v)$ ; $\mathrm{Ker} f$ : résoudre $f(x) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \mathrm{rg} f$ ; $\mathrm{rg} f = \dim F \Rightarrow \mathrm{Im} f = F$ (surjective) ; $\mathrm{Im} f = \mathrm{Vect}(f(e_1), \dots, f(e_n))$

Reprendre les applications linéaires de l'exercice 2.4, identifier les dimensions des noyaux et des images de chaque application et vérifier le théorème du rang sur ces exemples.

## Exercice 3.8
Type : noyau, image, rang d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/3
Formules : linéaire : $f(\lambda u + v) = \lambda f(u) + f(v)$ ; $\mathrm{Ker} f$ : résoudre $f(x) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \mathrm{rg} f$ ; $\mathrm{rg} f = \dim F \Rightarrow \mathrm{Im} f = F$ (surjective) ; $\mathrm{Im} f = \mathrm{Vect}(f(e_1), \dots, f(e_n))$

On considère l'application linéaire $f : \mathbb{R}_2[X] \to \mathbb{R}^2$, $P = aX^2 + bX + c \mapsto (a + c,\ a + 2b + 3c)$.
1. Trouver la dimension de $\mathrm{Ker}(f)$ en justifiant proprement votre raisonnement.
2. Quelle est la dimension de $\mathrm{Im}(f)$ ?
3. Trouver $\mathrm{Im}(f)$.
4. $f$ est-elle injective ? surjective ? bijective ?

## Exercice 3.9
Type : noyau, image, rang d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/3
Formules : linéaire : $f(\lambda u + v) = \lambda f(u) + f(v)$ ; $\mathrm{Ker} f$ : résoudre $f(x) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \mathrm{rg} f$ ; $\mathrm{rg} f = \dim F \Rightarrow \mathrm{Im} f = F$ (surjective) ; $\mathrm{Im} f = \mathrm{Vect}(f(e_1), \dots, f(e_n))$

(Travail personnel) Soient $\mathcal{B} = (e_1, e_2, e_3)$ la base canonique de $\mathbb{R}^3$ et l'application linéaire $f : \mathbb{R}^3 \to \mathbb{R}^3$, $(x,y,z) \mapsto (6x - 4y - 4z,\ 5x - 3y - 4z,\ x - y)$.
1. Déterminer $\mathrm{Ker}(f)$ et donner sa dimension en exhibant une de ses bases.
2. En déduire la dimension de $\mathrm{Im}(f)$.
3. Soient $u = e_1 + e_2$ et $v = e_2 - e_3$. Calculer $f(u)$ et $f(v)$.
4. En déduire que $(u,v)$ est une base de $\mathrm{Im}(f)$.

## Exercice 3.10
Type : théorème du rang (conséquences : injectif, surjectif, bijectif) · ECUE : ALM · Niveau : maths-s2-alm/4
Formules : théorème du rang : $\dim E = \dim \mathrm{Ker}(f) + \dim \mathrm{Im}(f)$ ; injective $\iff \mathrm{Ker}(f) = \{0_E\}$ ; surjective $\iff \mathrm{Im}(f) = F$ ; si $\dim E = \dim F$ : injective $\iff$ surjective $\iff$ bijective ; $\dim E > \dim F \Rightarrow$ pas injective ; $\dim E < \dim F \Rightarrow$ pas surjective ; un polynôme de degré $\leqslant n$ ayant $n + 1$ racines est nul

1. Soient $E$ un $\mathbb{R}$-ev de dimension finie et $f \in \mathcal{L}(E)$ un endomorphisme de $E$. À l'aide du théorème du rang, montrer que :
   - (a) si $f$ est injective alors $f$ est surjective ;
   - (b) si $f$ est surjective alors $f$ est injective ;
   - (c) $f$ bijective $\iff \mathrm{Ker}(f) = \{0_E\} \iff \mathrm{Im}(f) = E$.
2. On se donne désormais un deuxième $\mathbb{R}$-ev $F$ de dimension finie. Que dire d'une application linéaire $f \in \mathcal{L}(E,F)$ suivant les dimensions de $E$ et de $F$ ?

## Exercice 3.11 (⋆)
Type : théorème du rang (conséquences : injectif, surjectif, bijectif) · ECUE : ALM · Niveau : maths-s2-alm/4
Formules : théorème du rang : $\dim E = \dim \mathrm{Ker}(f) + \dim \mathrm{Im}(f)$ ; injective $\iff \mathrm{Ker}(f) = \{0_E\}$ ; surjective $\iff \mathrm{Im}(f) = F$ ; si $\dim E = \dim F$ : injective $\iff$ surjective $\iff$ bijective ; $\dim E > \dim F \Rightarrow$ pas injective ; $\dim E < \dim F \Rightarrow$ pas surjective ; un polynôme de degré $\leqslant n$ ayant $n + 1$ racines est nul

Soient $(x_0, x_1, \dots, x_n)$ $n + 1$ réels distincts et $f$ l'application linéaire définie par $f : \mathbb{R}_n[X] \to \mathbb{R}^{n+1}$, $P \mapsto (P(x_0), P(x_1), \dots, P(x_n))$.
1. Montrer que $f$ est injective puis qu'elle est bijective.
2. En déduire que par $n + 1$ points du plan d'abscisses distinctes passe un et un seul polynôme de degré au plus $n$.

## Exercice 3.12
Type : noyau, image, rang d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/3
Formules : linéaire : $f(\lambda u + v) = \lambda f(u) + f(v)$ ; $\mathrm{Ker} f$ : résoudre $f(x) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \mathrm{rg} f$ ; $\mathrm{rg} f = \dim F \Rightarrow \mathrm{Im} f = F$ (surjective) ; $\mathrm{Im} f = \mathrm{Vect}(f(e_1), \dots, f(e_n))$

(Travail personnel) Soient $E = \mathbb{R}[X]$ et $f : \mathbb{R}[X] \to \mathbb{R}[X]$, $P \mapsto P'$.
1. Montrer que $f$ est un endomorphisme de $E$.
2. Déterminer le noyau et l'image de $f$.
3. $f$ est-elle injective ? surjective ?
4. Qu'en pensez-vous ?

## Exercice 4.13
Type : projecteur, noyau et image · ECUE : ALM · Niveau : maths-s2-alm/10
Formules : projecteur $\iff f \circ f = f$ ; $E = \mathrm{Ker} f \oplus \mathrm{Im} f$ ; $f = id$ sur $\mathrm{Im} f$, $0$ sur $\mathrm{Ker} f$ ; matrice dans une base adaptée $\mathrm{diag}(0, \dots, 0, 1, \dots, 1)$

Dans le plan $\mathbb{R}^2$, on a représenté la droite $D_1$ d'équation $y = x$, la droite $D_2$ d'équation $y = -2x$ ainsi que le vecteur $v = (1,4)$.
1. En reliant à la théorie des espaces vectoriels, que peut-on dire des deux droites $D_1$ et $D_2$ ?
2. Construire le projeté $v_1$ de $v$ sur $D_1$ parallèlement à $D_2$ ainsi que le projeté $v_2$ de $v$ sur $D_2$ parallèlement à $D_1$. Quel est le lien entre $v$, $v_1$ et $v_2$ ?
3. Graphiquement quelles sont les coordonnées respectives de $v_1$ et $v_2$ ? Que remarquez-vous à nouveau ?
4. Quel serait le projeté de $v_1$ sur $D_1$ parallèlement à $D_2$ ? Quel serait le projeté de $v_2$ sur $D_1$ parallèlement à $D_2$ ?
5. Construire le symétrique de $v$ par rapport à $D_1$ parallèlement à $D_2$.

## Exercice 4.14
Type : projecteur, noyau et image · ECUE : ALM · Niveau : maths-s2-alm/10
Formules : projecteur $\iff f \circ f = f$ ; $E = \mathrm{Ker} f \oplus \mathrm{Im} f$ ; $f = id$ sur $\mathrm{Im} f$, $0$ sur $\mathrm{Ker} f$ ; matrice dans une base adaptée $\mathrm{diag}(0, \dots, 0, 1, \dots, 1)$

Soient $p_1$, $p_2$ deux endomorphismes de $\mathbb{R}^2$ définis par $p_1 : (x,y) \mapsto (x, 0)$ et $p_2 : (x,y) \mapsto (x - y, 0)$. Pour chacune de ces applications linéaires :
1. Déterminer $\mathrm{Ker}(p)$ et $\mathrm{Im}(p)$. Les dessiner sur le plan.
2. Justifier graphiquement que $\mathrm{Ker}(p) \oplus \mathrm{Im}(p) = \mathbb{R}^2$.
3. Soient $u \in E$, $v \in \mathrm{Im}(p)$ et $w \in \mathrm{Ker}(p)$ tels que $u = v + w$. Que peut-on dire de $p(v)$ ? En déduire l'expression de $p(u)$ en fonction de $v$ et $w$. En déduire la construction graphique de $p(u)$.
4. Expliquer pourquoi ce type d'application linéaire s'appelle un projecteur.
5. Vérifier que $p \circ p = p$.
6. On note $f = 2p - \mathrm{id}$. Étudier l'image d'un vecteur du plan par $f$. Comment appelleriez-vous cette application ?

## Exercice 4.15
Type : projecteur, noyau et image · ECUE : ALM · Niveau : maths-s2-alm/10
Formules : projecteur $\iff f \circ f = f$ ; $E = \mathrm{Ker} f \oplus \mathrm{Im} f$ ; $f = id$ sur $\mathrm{Im} f$, $0$ sur $\mathrm{Ker} f$ ; matrice dans une base adaptée $\mathrm{diag}(0, \dots, 0, 1, \dots, 1)$

Soit $f \in \mathcal{L}(\mathbb{R}^2)$ définie par $f : (x,y) \mapsto (4x - 6y,\ 2x - 3y)$.
1. Montrer que $f$ est un projecteur, c'est-à-dire que $f \circ f = f$.
2. Déterminer $\mathrm{Ker}(f)$ et $\mathrm{Im}(f)$ sous forme de Vect, les dessiner sur le plan.
3. Justifier que $\mathrm{Ker}(f) \oplus \mathrm{Im}(f) = \mathbb{R}^2$.
4. Montrer que $\forall v \in \mathrm{Im}(f)$, $f(v) = v$.
5. Soient $u \in \mathbb{R}^2$ et $(v,w) \in \mathrm{Im}(f) \times \mathrm{Ker}(f)$ tels que $u = v + w$. Que vaut $f(u)$ ?

## Exercice 4.16
Type : projecteur, noyau et image · ECUE : ALM · Niveau : maths-s2-alm/10
Formules : projecteur $\iff f \circ f = f$ ; $E = \mathrm{Ker} f \oplus \mathrm{Im} f$ ; $f = id$ sur $\mathrm{Im} f$, $0$ sur $\mathrm{Ker} f$ ; matrice dans une base adaptée $\mathrm{diag}(0, \dots, 0, 1, \dots, 1)$

(Travail personnel) Décrire les projections suivantes :
- $p_1 : \mathbb{R}^3 \to \mathbb{R}^3$, $(x,y,z) \mapsto \frac13(x + y + z,\ x + y + z,\ x + y + z)$
- $p_2 : \mathbb{R}^3 \to \mathbb{R}^3$, $(x,y,z) \mapsto \big(\frac12(x - y),\ \frac12(y - x),\ z\big)$
