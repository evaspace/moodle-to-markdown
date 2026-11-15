# Partiel S1 — juin 2018 (corrigé, FR)

- Source : `raw/S1/Finals/Phys/2023#/final-2023#-s1-phys-correction-fr.pdf` (4 pages, corrigé manuscrit scanné ; l'exercice 3 n'y figure pas)
- Date réelle : juin 2018 (S1#, dossier promo 2023#). Sujet : `final-2023#-s1-phys-subject-fr.md`.
- Calculatrices et documents non autorisés. Réponses sur le sujet. QCM sans points négatifs. Barème : 20 points. Rapport avec la mécanique : cinématique en base de Frenet, statique (moments, équilibre d'une barre), énergie (boucle). Les lignes `> ` sont les solutions du corrigé ; celles de l'exercice 3 sont rédigées ici (absentes du corrigé scanné).

## QCM (4 points)
Type : QCM de statique et d'énergie (moments, travail, théorèmes énergétiques) · ECUE : Mécanique · Niveau : physique-s1-meca/12
Formules : $R_c = \dfrac{v^2}{a_N}$ ; circulaire décéléré : $a_T < 0$, $a_N = v^2/R > 0$ ; $\vec v = R\dot\theta\,\vec u_T$ ; équilibre de rotation : $\sum\mathcal M_{/\Delta}(\vec F_{ext}) = 0$ ; moment = $\pm F\,d$ (bras de levier) ; force conservative : travail indépendant du chemin ; $\Delta E_m = W(\vec f_{frott})$ ; $W_{AB}(\vec f) = -f\cdot\widehat{AB} = -fR\theta$ sur un arc de rayon $R$ et d'angle $\theta$

1. Le vecteur vitesse est de norme $v = \dfrac{2}{\sqrt{1 - t^2}}$ et l'accélération normale $a_N = \dfrac{2}{1 - t^2}$. Le rayon de courbure vaut : a) $R = 2$ ; b) $R = \sqrt{1 - t^2}$ ; c) $R = \dfrac{1}{\sqrt{1 - t^2}}$.
> Réponse a) : $R = \dfrac{v^2}{a_N} = \dfrac{4/(1 - t^2)}{2/(1 - t^2)} = 2$.
2. Le vecteur accélération d'un mouvement circulaire décéléré en base de Frenet s'écrit : a) $a_T < 0$, $a_N < 0$ ; b) $a_T < 0$, $a_N > 0$ ; c) $a_T < 0$, $a_N = 0$ ; d) $a_T = 0$, $a_N > 0$.
> Réponse b).
3. Dans la base de Frenet, le vecteur vitesse s'écrit : a) $\vec v = R\dot\theta\,\vec u_T$ ; b) $\vec v = R\ddot\theta\,\vec u_T$ ; c) $\vec v = R\dot\theta\,\vec u_N$.
> Réponse a).
4. La condition d'équilibre de rotation est : a) $\sum\vec F_{ext} = \vec 0$ ; b) $\sum\vec{\mathcal M}_{/\Delta}(\vec F_{ext}) = \dfrac{d\vec L}{dt}$ ; c) $\sum\vec F_{ext} = m\vec a$ ; d) $\sum\vec{\mathcal M}_{/\Delta}(\vec F_{ext}) = \vec 0$.
> Réponse d).
5. Le moment de la tension $\vec T$ par rapport au point d'appui du triangle (poutre de longueur $L$ posée sur un appui situé à $L/4$ d'une extrémité, $\vec T$ vers le haut à l'autre extrémité, poids $M\vec g$ à l'extrémité de l'appui) est : a) nul ; b) $-TL/2$ ; c) $3TL/4$ ; d) $TL/4$.
> Réponse c) : bras de levier $3L/4$.
6. Une force conservative est une force dont le travail est : a) nul quel que soit le trajet ; b) strictement positif ; c) indépendant du chemin suivi.
> Réponse c).
7. Le théorème de l'énergie mécanique pour un mouvement quelconque est : a) $\Delta E_m = W(\vec P)$ où $\vec P$ est le poids ; b) $\Delta E_m = W(\vec f)$ où $\vec f$ est la force de frottement ; c) $\Delta E_m = \Delta E_c + \Delta E_p$.
> Réponse b).
8. Une masse $m$ glisse sur la piste AB (arc de cercle de centre O, $OA = OB = R$, angle $\theta$ en O). Le travail de la force de frottement sur AB est : a) $-f\,R\cos\theta$ ; b) $f(1 - \cos\theta)$ ; c) $-f\,R\,\theta$.
> Réponse c) : $W = -f\cdot R\theta$ (longueur de l'arc).

## Exercice 1 (4 points)
Type : mouvement circulaire à vitesse variable (abscisse curviligne, tour complet, composantes de Frenet) · ECUE : Mécanique · Niveau : physique-s1-meca/13
Formules : $s(t) = \int_0^t v\,dt$ ; $\int \dfrac{dt}{1 + \alpha t} = \dfrac1\alpha\ln(1 + \alpha t)$ ; $a_T = \dfrac{dv}{dt}$, $a_N = \dfrac{v^2}{R}$, $a = \sqrt{a_T^2 + a_N^2}$

Un point matériel décrit un cercle de centre $O$ et de rayon $R$ avec une vitesse de norme $V(t) = \dfrac{V_0}{1 + \alpha t}$ ($V_0$ et $\alpha$ constantes positives).
1. Exprimer l'abscisse curviligne $s(t)$, sachant que $s(t = 0) = 0$.
> Avec $u = 1 + \alpha t$, $dt = du/\alpha$ : $s(t) = V_0\int_1^{1 + \alpha t}\dfrac{du}{\alpha u} = \dfrac{V_0}\alpha\ln(1 + \alpha t)$.
2. Exprimer les composantes du vecteur accélération en base de Frenet.
> $a_T = \dfrac{dV}{dt} = -\dfrac{\alpha V_0}{(1 + \alpha t)^2}$ et $a_N = \dfrac{V^2}{R} = \dfrac{V_0^2}{R(1 + \alpha t)^2}$.

## Exercice 2 (6 points)
Type : équilibre d'une poutre articulée (câble, charge, réaction du mur) · ECUE : Mécanique · Niveau : physique-s1-meca/12
Formules : équilibre : $\sum\vec F_{ext} = \vec 0$ et $\sum\mathcal M_O(\vec F_{ext}) = 0$ ; $\mathcal M_O(\vec F) = \pm F\,d$ avec $d$ = bras de levier ; poids de la barre en son milieu ; projection sur $Ox$ et $Oy$

Une enseigne de magasin est composée d'une barre OA de masse $m$ et de longueur $L$ mobile autour d'un point O. À l'extrémité A est suspendu un objet décoratif de masse $M$. En un point B tel que $OB = \dfrac14L$ est fixée une tige BC perpendiculaire à la barre. Quand l'enseigne est sur son support, la barre OA fait un angle $\alpha = 30°$ avec la verticale.
1. Faire le bilan des forces extérieures exercées sur la barre OA, en précisant leurs points d'application. Représenter ces forces.
> $\vec R$ : réaction du mur en O ; $\vec T_A$ : tension du fil en A ($T_A = P_M$) ; $\vec P$ : poids de la barre en son milieu G ; $\vec F$ : force exercée par la tige BC en B.
2. a) Écrire la condition d'équilibre de rotation, en déduire l'expression littérale de la force $\vec F$ exercée par la tige BC sur la barre OA, sachant qu'elle est dirigée le long de la tige BC. b) Faire l'application numérique pour $m = 2$ kg, $M = 3$ kg, $g = 10$ m·s$^{-2}$.
> a) Moments par rapport à O : $F\cdot OB - P\cdot OG\sin\alpha - T_A\cdot OA\sin\alpha = 0$, soit $F\dfrac L4 = P\dfrac L2\sin\alpha + T_AL\sin\alpha$, donc $F = 4\left(\dfrac P2 + T_A\right)\sin\alpha$. b) $F = 4\left(\dfrac{mg}2 + Mg\right)\sin 30° = 4(10 + 30)\times\dfrac12 = 80$ N.
3. Utiliser la condition d'équilibre de translation pour exprimer les composantes $R_x$ et $R_y$ de la réaction en O. Faire l'application numérique.
> $\vec R + \vec F + \vec P + \vec T_A = \vec 0$. Sur $Ox$ : $R_x - F\cos 30° = 0$, donc $R_x = 80\dfrac{\sqrt3}2 = 40\sqrt3 \approx 69$ N. Sur $Oy$ : $R_y + F\sin 30° - P - T_A = 0$, donc $R_y = 20 + 30 - 40 = 10$ N.

## Exercice 3 (6 points)
Type : boucle (looping) : énergie mécanique, vitesse, réaction normale · ECUE : Mécanique · Niveau : physique-s1-meca/13
Formules : sans frottement : $E_m = \text{cste}$, $\tfrac12mv_A^2 + mgz_A = \tfrac12mv^2 + mgz$ ; hauteur de M sur la boucle : $z_M = R + R\sin\theta$ ; Newton en Frenet : $\vec P + \vec R_N = m\vec a$, $a_N = \dfrac{v^2}{R}$ vers le centre ; $R_N = \dfrac{mv_M^2}{R} - mg\sin\theta$

Une masse $m$ est lâchée sans vitesse initiale du point A ($V_A = 0$). En B, elle suit le profil circulaire de la boucle BCB, de centre O et de rayon R, en tournant dans le sens trigonométrique à l'intérieur de la boucle. Les frottements sont négligeables. A est à la hauteur $h$ au-dessus de B ; M est repéré par l'angle $\theta$ entre OM et l'horizontale ($OO_1$).
1. Utiliser le théorème de l'énergie mécanique entre A et B pour calculer la vitesse $V_B$. On donne $g = 10$ m·s$^{-2}$ et $h = 1$ m.
> $\Delta E_m = 0$ : $mgh = \tfrac12mV_B^2$, donc $V_B = \sqrt{2gh} = \sqrt{20} \approx 4{,}5$ m/s.
2. Utiliser le théorème de l'énergie mécanique entre A et M pour exprimer la vitesse $V_M$ en fonction de $g$, $R$, $h$ et $\theta$.
> $mgh = \tfrac12mV_M^2 + mg(R + R\sin\theta)$, donc $V_M = \sqrt{2g\left(h - R - R\sin\theta\right)}$.
3. Représenter la réaction $\vec R_N$ exercée par le support sur la masse en M (à l'intérieur de la boucle), l'exprimer en fonction de $g$, $h$, $m$, $R$ et $\theta$ avec la deuxième loi de Newton en base de Frenet $(\vec u_T, \vec u_N)$.
> $\vec R_N$ est dirigée vers O. Sur $\vec u_N$ (vers O) : $R_N + mg\sin\theta = m\dfrac{V_M^2}{R}$, donc $R_N = \dfrac{2mg(h - R - R\sin\theta)}R - mg\sin\theta = mg\left(\dfrac{2h}R - 2 - 3\sin\theta\right)$.
