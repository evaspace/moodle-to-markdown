# Partiel de physique S1 — décembre 2022 (sujet, FR)

- Source : `raw/S1/Finals/Phys/2027/final-2027-s1-phys-subject-fr.pdf` (8 pages)
- Date réelle : décembre 2022 (EPITA InfoS1, dossier promo 2027). Pas de corrigé : le PDF est la copie annotée d'un étudiant (réponses manuscrites en partie fausses, non reprises ici).
- Durée : 1 h. Calculatrices et documents non autorisés. Barème indicatif : 20 points (6 + 5,5 + 4,5 + 6 dont un bonus). Rapport avec la mécanique : statique (moments, équilibre de rotation et de translation), cinématique de l'ellipse, accélération en mouvement circulaire.

## Exercice 1. Questions de cours (6 points, pas de points négatifs pour le QCM)
Type : QCM de statique et d'énergie (moments, travail, théorèmes énergétiques) · ECUE : Mécanique · Niveau : physique-s1-meca/12
Formules : moment d'une force par rapport à un axe : $\mathcal M = \pm F\,d$ (bras de levier $d$), signe selon le sens de rotation ; moment nul si la droite d'action coupe l'axe ; $W_{AB}(\vec f) = \int_A^B \vec f\cdot d\vec l = \int_A^B f\,dl\cos\alpha$ ; $\Delta E_c = \sum W(\vec F_{ext})$ ; $\Delta E_m = W(\vec f_{frott})$ ; force perpendiculaire au déplacement : $W = 0$ ; $W_{A\to B}(\vec P) = mgR(1 - \cos\theta)$ pour une descente de hauteur $R(1 - \cos\theta)$

Choisissez la ou les bonnes réponses.
1. Lors d'un mouvement quelconque, la vitesse et l'accélération sont toujours colinéaires. a) Vrai ; b) Faux.
2. Pour un mouvement circulaire à vitesse quelconque : a) $\vec v = R\dot\theta\,\vec u_\theta$ ; b) $\vec v = R\,\vec u_\theta$ ; c) $\vec a = R\dot\theta^2\,\vec u_r$ ; d) $\vec a = -R\dot\theta^2\,\vec u_r + R\ddot\theta\,\vec u_\theta$.
3. Quelles affirmations sur le moment d'une force sont justes ? On note OP la distance entre le pivot et le point d'application de la force. a) Le moment d'une force dépend uniquement du bras de levier ; b) le moment d'une force est maximisé à angle nul entre la force et la direction OP ; c) le moment d'une force est maximisé à angle droit entre la force et la direction OP ; d) le moment d'une force dont la droite d'action passe par le pivot est nul.
4. On donne $\|\vec F\| = 10$ N ; $L = 1$ m ; $x = 60$ cm ; $\theta = 30°$ ($\theta$ = angle entre la force et la verticale). Le moment de la force $\vec F$ par rapport au point O (figure : $x$ et $L$ repèrent, à partir de O, la position du point d'application) vaut : a) $\dfrac{\sqrt3}2$ N·m ; b) $\dfrac12$ N·m ; c) 3 N·m ; d) $3\sqrt3$ N·m.
5. On donne $L = 1$ m ; $d = 40$ cm ; $\|\vec F_1\| = 15$ N ; $\|\vec F_2\| = 6$ N. La barre schématisée (pivot O à la distance $d$ de l'extrémité où s'applique $\vec F_1$, $\vec F_2$ à l'autre extrémité, toutes deux verticales vers le bas) est à l'équilibre de rotation. a) Vrai ; b) Faux.
6. On donne $L = 1$ m ; $\|\vec F_1\| = 6$ N ; $\|\vec F_2\| = 8$ N ; $\theta = 30°$ ($\vec F_1$ inclinée de $\theta$ par rapport à l'horizontale). Quelle doit être la distance $d$ pour que la barre soit à l'équilibre de rotation ? a) $\dfrac{8}{3\sqrt3}$ m ; b) $\dfrac{8}{11}$ m ; c) $\dfrac83$ m ; d) $\dfrac{8}{8 + 3\sqrt3}$ m.

## Exercice 2. Mouvement elliptique (5,5 points)
Type : mouvement elliptique en cartésien (trajectoire, vitesse, accélération, $\vec a = -\omega^2\overrightarrow{OM}$) · ECUE : Mécanique · Niveau : physique-s1-meca/3
Formules : $\vec V = (\dot x, \dot y)$, $\vec a = (\ddot x, \ddot y)$ ; $\|\vec V\| = \sqrt{\dot x^2 + \dot y^2}$ ; $\cos^2 + \sin^2 = 1$ ; ellipse : $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$ ; $\ddot x = -\omega^2 x$, $\ddot y = -\omega^2 y$

Un point matériel M se déplace sur une ellipse d'équation cartésienne $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$. La direction de $\overrightarrow{OM}$ par rapport à l'axe $Ox$ est repérée par l'angle $\varphi$. Les équations horaires peuvent se mettre sous la forme $x(t) = x_0\cos(\omega t + \varphi_0)$ et $y(t) = y_0\sin(\omega t + \varphi_0)$, où $\omega$ est une constante et $x_0$, $y_0$, $\varphi_0$ des constantes à déterminer. Conditions initiales : à $t = 0$, M se trouve en $M_0$ (sur l'axe $Ox$, à la distance $a$ de O).
1. Déterminer $x_0$ et $\varphi_0$ d'après les conditions initiales.
2. En utilisant l'équation de la trajectoire, en déduire que $y = b\sin(\omega t)$.
3. Déterminer les composantes du vecteur vitesse. Calculer sa norme.
4. Déterminer les composantes du vecteur accélération. Calculer sa norme.
5. Montrer que l'on peut écrire $\vec a = k\,\overrightarrow{OM}$ et déterminer la valeur de $k$.

## Exercice 3. Étude des forces et des moments sur un plongeoir (4,5 points)
Type : plongeoir sur deux appuis (forces, équilibre de translation et de rotation, réactions) · ECUE : Mécanique · Niveau : physique-s1-meca/12
Formules : équilibre : $\sum\vec F_{ext} = \vec 0$ et $\sum\mathcal M_{pivot}(\vec F_{ext}) = 0$ ; choisir le pivot au point d'application d'une force inconnue pour l'éliminer de l'équation des moments ; $\mathcal M = \pm F\,d$ (bras de levier) ; $T\,L = mg\,a$ (pivot en C), $R = T + mg$

On étudie un plongeoir de piscine immobile à l'horizontale. Le contact au niveau de l'appui simple au point B est considéré constamment maintenu (par un boulonnage adapté). Le plongeoir prend appui au point C. Un plongeur de masse $m$ est situé au point D. La masse de la planche est négligée. Le but est d'étudier les conditions d'équilibre. Distances : $BC = L$ et $CD = a$.
a. Nommer les forces en jeu sur le schéma et choisir un pivot adapté à cette étude.
b. Écrire la condition d'équilibre de translation, et la condition d'équilibre de rotation dans le cas présent.
c. Calculer la norme de la force s'exerçant au point B en fonction des grandeurs $a$, $L$, $m$ et $g$ (intensité du champ de pesanteur).
d. En déduire la valeur de la norme de la force s'exerçant au point C.

## Exercice 4. Condition d'équilibre d'une masse accrochée à deux fils (4 + 2 points)
Type : masse suspendue à deux fils (moments, équilibre de rotation, équation en $\cos\theta$) · ECUE : Mécanique · Niveau : physique-s1-meca/12
Formules : moment par rapport à A : $\vec{\mathcal M}_A(\vec F) = \overrightarrow{AM}\wedge\vec F$ ; $\mathcal M_A(\vec P_M) = -mga\cos\theta$ en valeur algébrique pour $AM = a$ à l'angle $\theta$ de l'horizontale ; fil tendu passant par une poulie parfaite : même tension, égale à $m'g$ à l'équilibre ; $\cos^2\theta = \dfrac{1 + \cos 2\theta}2$ ; équation du second degré en $X = \cos\theta$ avec $-1 \leqslant X \leqslant 1$ pour choisir la racine valide

On considère un fil inextensible de masse négligeable, fixé en A à un socle horizontal AB de longueur $a$, et passant en B par une poulie parfaite de dimension négligeable. En un point M, tel que $AM = a$, est fixée une masse ponctuelle de masse $m$ et, au bout du fil, est aussi accrochée une masse de masse $m'$ en N. La poulie transmet parfaitement en M le poids du point N de masse $m'$ (tension supplémentaire). Le point M est immobile. $\theta$ est l'angle en A du triangle ABM (figure).
1. Représenter toutes les forces qui s'exercent sur la masse $m$.
2. Exprimer les moments des forces par rapport au point A, en fonction de l'angle $\theta$, des masses $m$ et $m'$ et de $g$, intensité du champ de pesanteur.
3. Écrire la condition d'équilibre de rotation en fonction de ces mêmes grandeurs.
Bonus :
4. En utilisant le fait que $\cos^2\theta = \dfrac{1 + \cos(2\theta)}2$, écrire l'équation de la question 3 sous la forme $2mX^2 - m'X - m = 0$, en précisant $X$.
5. Résoudre le polynôme en tenant compte des valeurs possibles que peut prendre l'angle $\theta$ ; indiquer quelle racine est valide. Conclure en indiquant une condition reliant $m$ et $m'$.
