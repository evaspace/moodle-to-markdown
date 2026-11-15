# Partiel 1 S1 — janvier 2018 (sujet, FR)

- Source : `raw/S1/Finals/Phys/2022/final-2022-s1-phys-subject-fr.pdf` (6 pages)
- Date réelle : janvier 2018 (S1, dossier promo 2022). Corrigé : `final-2022-s1-phys-correction-fr.md`.
- Calculatrices et documents non autorisés. Réponses sur le sujet. Barème : 20 points. Rapport avec la mécanique : statique (moments, équilibre d'une poutre), dynamique (Newton en base de Frenet), énergie (travail, théorèmes de l'énergie cinétique et mécanique).

## QCM (4 points)
Type : QCM de statique et d'énergie (moments, travail, théorèmes énergétiques) · ECUE : Mécanique · Niveau : physique-s1-meca/12
Formules : moment d'une force par rapport à un axe : $\mathcal M = \pm F\,d$ (bras de levier $d$), signe selon le sens de rotation ; moment nul si la droite d'action coupe l'axe ; $W_{AB}(\vec f) = \int_A^B \vec f\cdot d\vec l = \int_A^B f\,dl\cos\alpha$ ; $\Delta E_c = \sum W(\vec F_{ext})$ ; $\Delta E_m = W(\vec f_{frott})$ ; force perpendiculaire au déplacement : $W = 0$ ; $W_{A\to B}(\vec P) = mgR(1 - \cos\theta)$ pour une descente de hauteur $R(1 - \cos\theta)$

1. Le moment du poids $\vec P$ de la poutre par rapport au point d'appui du triangle (poutre posée sur un appui, centre de gravité à $L/4$ de l'appui, force $\vec T$ vers le haut à l'autre bout) est : a) $-P\,L/2$ ; b) $P\,L/4$ ; c) nul ; d) $-P\,L/4$.
2. Le moment de la force $\vec F_2$ (verticale, appliquée en B) par rapport à l'axe $(\Delta)$ passant par O (milieu de la tige AB de longueur $L$, inclinée de $\alpha$) et perpendiculaire à la feuille est : a) $-F_2L/2$ ; b) $-F_2\dfrac L2\cos\alpha$ ; c) $-F_2\dfrac L2\sin\alpha$ ; d) nul.
3. Le moment du poids par rapport à l'axe $(\Delta)$ (schéma de la question 2, poids appliqué en O) est : a) $-P\,L/2$ ; b) $P\,L/2$ ; c) nul.
4. Le travail d'une force variable $\vec f$ qui fait un angle $\alpha$ avec le déplacement $d\vec l$ sur le trajet AB est : a) $\int_A^B f\,dl\sin\alpha$ ; b) $f\cdot AB\cos\alpha$ ; c) $\int_A^B f\,dl\cos\alpha$.
5. Le théorème de l'énergie cinétique est : a) $\Delta E_c = W(\vec P)$ où $\vec P$ est le poids ; b) $\Delta E_c = W(\vec f)$ où $\vec f$ est la force de frottement ; c) $\Delta E_c = \sum W(\vec F_{ext})$.
6. En présence de frottements (seule force non conservative), le théorème de l'énergie mécanique s'écrit : a) $\Delta E_m = 0$ ; b) $\Delta E_m = W(\vec f_{frott})$ ; c) $\Delta E_m = \Delta E_c$.
7. Le travail d'une force $\vec F$ perpendiculaire au déplacement est : a) strictement positif ; b) nul ; c) strictement négatif ; d) dépendant de la vitesse.
8. Une masse $m$ glisse sur la piste AB (arc de cercle de centre O, $OA = OB = R$, A repéré par l'angle $\theta$ avec la verticale OB). Le travail du poids sur le trajet AB est : a) $-mgR(1 - \cos\theta)$ ; b) $mgR\cos\theta$ ; c) $mgR(1 - \cos\theta)$.

## Exercice 1 (6 points)
Type : équilibre d'une poutre articulée (câble, charge, réaction du mur) · ECUE : Mécanique · Niveau : physique-s1-meca/12
Formules : équilibre : $\sum\vec F_{ext} = \vec 0$ et $\sum\mathcal M_O(\vec F_{ext}) = 0$ ; $\mathcal M_O(\vec F) = \pm F\,d$ avec $d$ = bras de levier ; poids de la poutre en son milieu ; projection sur $Ox$ et $Oy$

Une poutre de poids $P = 100$ N et de longueur $L = 1$ m, articulée en O au mur et inclinée de $30°$ sur l'horizontale, supporte à son extrémité droite une charge de poids $P_M = 300$ N. Un câble, fixé au mur et à la poutre aux deux tiers de sa longueur à partir de O, fait un angle de $60°$ avec la poutre et la maintient en équilibre (figure 2).
1. Représenter les forces extérieures qui s'exercent sur la poutre.
2. Calculer la tension du câble pour assurer l'équilibre de la poutre.
3. Calculer les composantes (horizontale $R_x$ et verticale $R_y$) de la réaction exercée par le mur sur la poutre.

## Exercice 2 (5 points)
Type : bille sur une sphère (Newton en base de Frenet, équation du mouvement, réaction) · ECUE : Mécanique · Niveau : physique-s1-meca/13
Formules : $\vec a = \dfrac{dv}{dt}\vec u_T + \dfrac{v^2}{r}\vec u_N$ avec $v = r\dot\theta$ : $a_T = r\ddot\theta$, $a_N = r\dot\theta^2$ ; $\vec P + \vec R = m\vec a$ ; poids : $P\sin\theta$ selon $\vec u_T$, $P\cos\theta$ selon $-\vec u_N$ ; $\ddot\theta = \dfrac gr\sin\theta$ ; $\dot\theta^2 = \dfrac{2g}r(1 - \cos\theta)$ ; $R = mg(3\cos\theta - 2)$

Une bille de masse $m$ est lâchée sans vitesse initiale du point A d'une sphère de rayon $OM = r$ et de centre O. Les frottements sont négligés. On étudie le mouvement tant que la bille est en contact avec la sphère ($\theta$ = angle entre la verticale ascendante et OM).
1. Donner les composantes du vecteur accélération de la bille dans la base de Frenet $(\vec\tau, \vec n)$, en fonction de $(\ddot\theta, \dot\theta, r)$.
2. a) Écrire la deuxième loi de Newton dans la base de Frenet. b) En déduire l'équation différentielle du mouvement ainsi que la norme de la réaction $R$.

## Exercice 3 (5 points)
Type : glissement avec frottement sur un guide hémicylindrique (énergie cinétique, énergie potentielle, énergie mécanique, travail de frottement) · ECUE : Mécanique · Niveau : physique-s1-meca/13
Formules : $\Delta E_c = \tfrac12m(v_B^2 - v_A^2)$ ; $\Delta E_p = mg(z_B - z_A)$ ; $\Delta E_m = \Delta E_c + \Delta E_p = W(\vec f)$ ; $W_{AB}(\vec f) = -f\cdot\widehat{AB}$ (force de norme constante opposée au déplacement) ; $\widehat{AB} = R\dfrac\pi2$ (quart de cercle)

Un objet ponctuel de masse $m = 10$ g est lâché du point A sans vitesse initiale. Le guide hémicylindrique de rayon $R$ est immobile dans le référentiel terrestre. Lorsque l'objet passe pour la première fois par le point B le plus bas du guide ($z = 0$), sa vitesse est $v_B = 4$ m/s. On note $\vec f$ la force de frottement, de norme constante. On donne $R = 1$ m et $g = 10$ m/s².
1. Représenter les forces extérieures exercées sur la masse en un point M quelconque entre A et B.
2. Calculer la variation d'énergie cinétique $\Delta E_c$ et la variation d'énergie potentielle de pesanteur $\Delta E_p$ entre A et B. En déduire la variation d'énergie mécanique $\Delta E_m$.
3. Déterminer le travail de la force de frottement entre A et B en utilisant le théorème de l'énergie mécanique. En déduire la norme de cette force supposée constante.
