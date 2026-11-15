# Partiel n°1 S1 — janvier 2017 (sujet, FR)

- Source : `raw/S1/Finals/Phys/2021/final-2021-s1-phys-subject-fr.pdf` (6 pages)
- Date réelle : janvier 2017 (EPITA InfoSup S1, dossier promo 2021). Pas de corrigé.
- Calculatrices et documents non autorisés. Réponses sur le sujet. Barème : 20 points (7 + 6 + 7). Rapport avec la mécanique : cinématique (cycloïde, spirale, Frenet), statique (poutre et câble), énergie (piste avec frottement).

## Exercice 1. Mouvement en cycloïde (7 points)
Type : cycloïde puis spirale (vitesse, normes, tracé, polaires, rayon de courbure) · ECUE : Mécanique · Niveau : physique-s1-meca/3
Formules : $\vec V = (\dot x, \dot y)$, $\vec a = (\ddot x, \ddot y)$ ; $\|\vec V\| = \sqrt{\dot x^2 + \dot y^2}$ ; $1 - \cos\alpha = 2\sin^2(\alpha/2)$ ; $\omega = 2\pi/T$ ; tableau de valeurs de $(x(t), y(t))$ en $t = 0, T/4, T/2, 3T/4, T$ ; $\vec V = \dot\rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta$ ; $\vec V = V\,\vec u_T = R(t)\dot\theta\,\vec u_T$, donc $R = V/\dot\theta$ ; $a_T = \dfrac{dV}{dt}$, $a_N = \dfrac{V^2}{R}$

Partie A. On se place dans le repère cartésien $(Oxyz)$. Une roue de rayon $R$ et de centre C roule sans glisser dans le plan $(xOy)$ ; l'abscisse du centre de la roue est liée à l'angle $\theta$ dont a tourné la roue. Le vecteur position a pour coordonnées $x(t) = A(\omega t - \sin\omega t)$ et $y(t) = A(1 - \cos\omega t)$ ($\theta = \omega t$ ; $A$ et $\omega$ constantes positives).
1. Déterminer les composantes cartésiennes des vecteurs vitesse et accélération.
2. En déduire la norme de chacun de ces vecteurs. On donne $1 - \cos\alpha = 2\sin^2(\alpha/2)$.
3. Tracer la cycloïde ($y = f(x)$) sur un intervalle de temps de 2 périodes ($2T$), avec $\omega = 2\pi/T$ (valeurs : $t = 0$, $T/4$, $T/2$, $3T/4$, $T$).

Partie B. On considère le mouvement d'une spirale d'équations horaires $\rho(t) = \rho_0e^{\omega t}$ et $\theta(t) = \omega t$ ($\rho_0$ et $\omega$ constantes positives).
1. Exprimer le vecteur vitesse de ce mouvement en coordonnées polaires. On rappelle que $\vec V = \dot\rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta$.
2. Calculer la norme du vecteur vitesse.
3. a) Sachant qu'en base de Frenet $\vec V = V\,\vec u_T = R(t)\dot\theta\,\vec u_T$, exprimer le rayon $R(t)$ de cette trajectoire. b) En déduire les composantes du vecteur accélération $\vec a(a_T, a_N)$ dans la base de Frenet $(\vec u_T, \vec u_N)$.

## Exercice 2. Système en équilibre (6 points)
Type : équilibre d'une poutre articulée (câble, charge, réaction du mur) · ECUE : Mécanique · Niveau : physique-s1-meca/12
Formules : équilibre : $\sum\vec F_{ext} = \vec 0$ et $\sum\mathcal M_O(\vec F_{ext}) = 0$ ; $\mathcal M_O(\vec F) = \pm F\,d$ avec $d$ = bras de levier ; poids de la poutre en son milieu ; projection sur $Ox$ et $Oy$

Une poutre horizontale OA, homogène, de longueur $L$ et de masse $m = 40$ kg, est fixée à un mur par son extrémité O. Un câble AB, de masse négligeable et inextensible, relie le mur (point B) et l'extrémité A de la poutre. Une masse $M = 150$ kg est suspendue au point A. On donne $\widehat{BAO} = 30°$ et $g = 10$ m·s$^{-2}$.
1. Faire le bilan des forces extérieures appliquées sur la poutre. Représenter ces forces.
2. a) Écrire la condition d'équilibre de rotation par rapport au point O, en déduire la norme de la tension du câble. b) Utiliser la condition d'équilibre de translation pour calculer les composantes $(R_x, R_y)$ de $\vec R_{mur}$. c) Calculer la norme de la réaction $\vec R_{mur}$.

## Exercice 3 (7 points)
Type : piste circulaire puis horizontale avec frottement (théorème de l'énergie cinétique, force de frottement, vitesse, réaction) · ECUE : Mécanique · Niveau : physique-s1-meca/13
Formules : $\Delta E_c = \sum W(\vec F_{ext})$ ; $W_{AB}(\vec P) = mgR(1 - \cos\theta)$ ; $W_{AB}(\vec f) = -f\cdot R\theta$ (arc de rayon $R$ et d'angle $\theta$) ; réaction normale perpendiculaire au déplacement : $W = 0$ ; sur BC horizontal : $\tfrac12m(v_C^2 - v_B^2) = -f\cdot BC$ ; $R_N = mg$ (pas d'accélération verticale), $R = \sqrt{R_N^2 + f^2}$

Un solide ponctuel de masse $m$ se déplace sur une piste : la portion AB est un arc de cercle de rayon $R$, d'angle $\theta$ et de centre O ; la portion BC est un segment horizontal. On lance le solide du point A avec une vitesse $\vec v_A$ tangente au cercle.
1. a) Faire le bilan des forces extérieures exercées sur le solide entre A et B, sachant que les frottements sur la partie AB sont assimilables à une force constante $f$. Représenter ces forces. b) Utiliser le théorème de l'énergie cinétique entre A et B pour exprimer la force de frottement $f$ en fonction de $R$, $g$, $v_A$, $v_B$, $m$ et $\theta$. Faire le calcul avec : $m = 0{,}1$ kg, $g = 10$ m·s$^{-2}$, $R = 1{,}5$ m, $v_A = 2$ m·s$^{-1}$, $v_B = 3$ m·s$^{-1}$, $\theta = 60° \approx 1$ rad.
2. a) Les frottements sur le trajet BC sont assimilables à une force $f = 0{,}1$ N. Calculer la vitesse au point C, sachant que $BC = 2$ m. b) Calculer la norme de la réaction totale $\vec R$ qui s'exerce sur le solide pendant le trajet BC.
