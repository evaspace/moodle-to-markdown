# Partiel 1 S1 — janvier 2020 (corrigé, FR)

- Source : `raw/S1/Finals/Phys/2024/final-2024-s1-phys-correction-fr.pdf` (7 pages, corrigé manuscrit scanné avec barème ; les pages 5 et 6 ne contiennent pas de solution)
- Date réelle : janvier 2020 (S1, dossier promo 2024). Sujet : `final-2024-s1-phys-subject-fr.md`.
- Calculatrices et documents non autorisés. Réponses sur le sujet. QCM sans points négatifs (0,5 point par question). Barème : 20 points. Rapport avec la mécanique : statique (moments, échelle, poutre), dynamique (plan incliné et poulie, Newton en base de Frenet sur une gouttière). Les lignes `> ` sont les solutions du corrigé ; celles de l'exercice 2 et de l'exercice 3 questions 2 et 3a sont rédigées ici (absentes du scan).

## QCM (4 points)
Type : QCM de statique et d'énergie (moments, travail, théorèmes énergétiques) · ECUE : Mécanique · Niveau : physique-s1-meca/12
Formules : $\vec{\mathcal M}_{/\Delta}(\vec F_A) = \overrightarrow{OA}\wedge\vec F_A$ est orthogonal à $\overrightarrow{OA}$ et à $\vec F_A$ ; équilibre : $\sum\vec F_{ext} = \vec 0$ et $\sum\mathcal M = 0$ ; moment algébrique $= \pm F\,d$ (bras de levier) ; poids d'un corps homogène en son milieu ; $\sum\vec F_{ext} = \dfrac{d\vec p}{dt} = m\vec a$ ; principe d'inertie : vitesse non uniforme $\Rightarrow$ forces non compensées ; forces à distance : gravitation, électrostatique

1. Le vecteur moment d'une force $\vec{\mathcal M}_{/\Delta}(\vec F_A) = \overrightarrow{OA}\wedge\vec F_A$ est : a) colinéaire au vecteur force $\vec F_A$ ; b) colinéaire au vecteur $\overrightarrow{OA}$ ; c) orthogonal au vecteur $\vec F_A$.
> Réponse c).
2. Une échelle homogène de longueur $L$ s'appuie sur un mur au point A et sur le sol au point B (angle $\alpha$ en A avec le mur). Contact en A sans frottements, en B avec frottements. On note $\varphi$ l'angle entre la réaction $\vec R_B$ et la normale au sol. La condition d'équilibre de translation projetée sur $(Ox)$ donne : a) $R_A - R_B\sin\varphi = 0$ ; b) $R_A - R_B\cos\varphi = 0$ ; c) $R_A\sin\alpha - R_B\sin\varphi = 0$.
> Réponse a).
3. Le moment algébrique du poids de l'échelle par rapport à l'axe $(\Delta)$ passant par B et perpendiculaire au plan $(xOy)$ est : a) $P\dfrac L2$ ; b) $P\dfrac L2\cos\alpha$ ; c) $P\dfrac L2\sin\alpha$.
> Réponse c).
4. La deuxième loi de Newton s'écrit : a) $\sum\vec F_{ext} = m\dfrac{d\overrightarrow{OM}}{dt}$ ; b) $\sum\vec F_{ext} = m\dfrac{d^2\vec V}{dt^2}$ ; c) $\sum\vec F_{ext} = \dfrac{d\vec p}{dt}$.
> Réponse c).
5. Un exemple de force à distance : a) une force de frottement ; b) l'interaction électrostatique ; c) la force de rappel.
> Réponse b).
6. Trois forces agissent sur un levier de longueur $L$ pouvant tourner autour d'un axe $(\Delta)$ passant par P (perpendiculaire à la feuille). $d_1$ est la distance entre P et le point d'application de $\vec F_1$. Le moment de $\vec F_1$ par rapport à $(\Delta)$ est : a) $-d_1F_1\sin\theta$ ; b) $-d_1F_1$ ; c) nul ; d) $-d_1F_1\cos\theta$.
> Réponse d).
7. Le moment de la force $\vec F_3$ (appliquée à l'extrémité du levier) par rapport à $(\Delta)$ est : a) $-LF_3\cos\varphi$ ; b) $LF_3\cos\varphi$ ; c) $-LF_3\sin\varphi$.
> Réponse b).
8. Une balle lâchée près de la surface de la Terre chute verticalement. Dans un référentiel terrestre, son centre est animé d'un mouvement rectiligne vertical non uniforme. Que dit le principe d'inertie ? a) que les forces appliquées à la balle se compensent ; b) rien ; c) que les forces appliquées à la balle ne se compensent pas.
> Réponse c).

## Exercice 1 (5 points)
Type : plan incliné et poulie (Newton sur deux masses, accélération, tension, réaction) · ECUE : Mécanique · Niveau : physique-s1-meca/10
Formules : $\sum\vec F_{ext} = m\vec a$ pour chaque masse ; fil inextensible de masse négligeable : même accélération, même tension ; sur le plan incliné : $-m_1g\sin\alpha + T = m_1a$ ; masse suspendue : $mg - T = ma$ ; $a = g\dfrac{m - m_1\sin\alpha}{m_1 + m}$ ; réaction normale : $R = m_1g\cos\alpha$

Un objet de masse $m_1$ se déplace sans frottements sur un plan incliné d'un angle $\alpha$ par rapport à l'horizontale ; la poulie et les fils sont de masse négligeable, les fils inextensibles. Un objet de masse $m$ se déplace verticalement (figure 1). On donne $\alpha = 30°$, $m_1 = 0{,}8$ kg, $m = 1$ kg et $g = 10$ m·s$^{-2}$. L'angle $\alpha$ est aussi l'angle entre la verticale du poids et la normale au plan incliné.
1. Représenter les forces extérieures appliquées sur les systèmes $m_1$ et $m$.
> Sur $m_1$ : poids $\vec P_1$, réaction $\vec R$ du plan (normale au plan), tension $\vec T_1$ du fil (le long du plan). Sur $m$ : poids $\vec P$ et tension $\vec T$.
2. a) Appliquer la deuxième loi de Newton à $m_1$ et à $m$, pour en déduire l'accélération. Donner l'expression littérale en fonction de $m_1$, $m$, $\alpha$ et $g$. b) Faire l'application numérique.
> a) Sur $m_1$, projection selon l'axe du plan : $-m_1g\sin\alpha + T_1 = m_1a$, donc $T_1 = m_1a + m_1g\sin\alpha$. Sur $m$, projection verticale : $mg - T = ma$, donc $T = mg - ma$. Poulie et fil de masse négligeable, fil inextensible : $T_1 = T$ et les deux masses ont la même accélération $a$. D'où $mg - ma = m_1a + m_1g\sin\alpha$ et $a = g\dfrac{m - m_1\sin\alpha}{m_1 + m}$. b) $a = 10\times\dfrac{1 - 0{,}8/2}{1{,}8} = \dfrac{6}{1{,}8} \approx 3{,}3$ m·s$^{-2}$.
3. a) Calculer la tension du fil. b) Calculer la réaction du plan incliné exercée sur la masse $m_1$.
> a) $T = m(g - a) = 1\times(10 - 3{,}3) \approx 6{,}7$ N. b) Selon l'axe perpendiculaire au plan (pas de mouvement) : $R - P_1\cos\alpha = 0$, donc $R = m_1g\cos\alpha = 0{,}8\times10\times\dfrac{\sqrt3}2 = 4\sqrt3 \approx 6{,}9$ N.

## Exercice 2 (5 points)
Type : équilibre d'une poutre articulée (câble, charge, réaction du mur) · ECUE : Mécanique · Niveau : physique-s1-meca/12
Formules : équilibre : $\sum\vec F_{ext} = \vec 0$ et $\sum\mathcal M_O(\vec F_{ext}) = 0$ ; $\mathcal M_O(\vec F) = \pm F\,d$ avec $d$ = bras de levier ; poids de la poutre en son milieu ; projection sur $Ox$ et $Oy$

Une poutre de poids $P = 100$ N et de longueur $L = 1$ m, articulée en O au mur et inclinée de $30°$ sur l'horizontale, supporte une charge M de poids $P_1 = 300$ N à son extrémité droite. Un câble relié à un mur, fixé aux deux tiers de la poutre à partir de O et faisant $60°$ avec elle, assure l'équilibre (figure 2).
1. Faire le bilan des forces extérieures qui s'exercent sur la poutre. Préciser leurs points d'application.
> $\vec R$ : réaction du mur en O ; $\vec P$ : poids de la poutre en son milieu G ; $\vec T_M$ : tension du fil qui maintient la charge M, à l'extrémité ($T_M = P_1$) ; $\vec T$ : tension du câble à son point d'attache.
2. Utiliser la condition d'équilibre de rotation pour exprimer la tension du câble $T$. Faire l'application numérique.
> Moments par rapport à O : $-P\dfrac L2\sin 60° + T\dfrac{2L}3\sin 60° - T_ML\sin 60° = 0$, donc $T = \dfrac32\left(\dfrac P2 + T_M\right) = 525$ N.
3. Utiliser la condition d'équilibre de translation pour exprimer les composantes $R_x$ et $R_y$ de la réaction du mur. Faire l'application numérique.
> $R_x = T\cos 30° = 525\dfrac{\sqrt3}2 \approx 455$ N et $R_y = P + T_M - T\sin 30° = 137{,}5$ N.

## Exercice 3 (6 points)
Type : solide sur une gouttière en quart de cercle (Newton en base de Frenet, réaction, décollement) · ECUE : Mécanique · Niveau : physique-s1-meca/13
Formules : $\vec a = \dfrac{dv}{dt}\vec u_T + \dfrac{v^2}{r}\vec u_N$ ; $\vec P + \vec R = m\vec a$ ; $a_T = g\sin\theta$ ; $mg\cos\theta - R = m\dfrac{V^2}{r}$ ; $V^2 = 2gr(1 - \cos\theta)$ ; $R = mg(3\cos\theta - 2)$ ; décollement : $R = 0 \iff \cos\theta = \dfrac23$

Un solide (S) de masse $m$, assimilable à un point, glisse sans frottement sur une gouttière en quart de cercle de centre O et de rayon $r$ (dans un plan vertical). Il quitte le sommet A avec une vitesse quasi nulle. Sa position M est repérée par l'angle $\theta$ avec la verticale.
1. Représenter les forces extérieures exercées sur le solide (S) au point M.
> Le poids $\vec P$ (vertical vers le bas) et la réaction $\vec R$ de la gouttière (normale, dirigée vers l'extérieur du cercle).
2. Appliquer la deuxième loi de Newton à (S) dans le repère de Frenet pour en déduire : a) la composante tangentielle $a_T$ de l'accélération en fonction de $g$ et $\theta$ ; b) la norme de la réaction $\vec R$ en fonction de $g$, $\theta$ et de la vitesse $V$ en M.
> $\vec P + \vec R = m\vec a$. a) Sur $\vec u_T$ : $mg\sin\theta = ma_T$, donc $a_T = g\sin\theta$. b) Sur $\vec u_N$ (vers O) : $mg\cos\theta - R = m\dfrac{V^2}r$, donc $R = m\left(g\cos\theta - \dfrac{V^2}r\right)$.
3. a) On montre que $V^2 = 2gr(1 - \cos\theta)$. En déduire la norme de $\vec R$ en fonction de $g$, $\theta$ et $m$. b) Déterminer l'angle $\theta$ lorsque le système (S) quitte la gouttière.
> a) $R = m\left(g\cos\theta - 2g(1 - \cos\theta)\right) = mg(3\cos\theta - 2)$. b) Le solide quitte la gouttière quand $R = 0$ : $3\cos\theta - 2 = 0$, $\cos\theta = \dfrac23$, $\theta = \arccos\dfrac23$.
