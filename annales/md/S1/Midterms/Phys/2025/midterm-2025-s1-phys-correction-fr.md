# Contrôle 1 S1 — année 2020/2021 (corrigé, FR)

- Source : `raw/S1/Midterms/Phys/2025/midterm-2025-s1-phys-correction-fr.pdf` (6 pages, corrigé manuscrit scanné avec barème)
- Date réelle : année 2020/2021 (S1 2020, dossier promo 2025). Sujet : `midterm-2025-s1-phys-subject-fr.md`.
- Calculatrices et documents non autorisés. QCM sans points négatifs (0,5 point par question). Barème : 20 points. Rapport avec la mécanique : cinématique du point (ellipse, droite, hélice en cylindriques, base de Frenet). Les lignes `> ` sont les solutions du corrigé.

## QCM (4 points)
Type : QCM de cinématique (vecteurs, polaires, Frenet, trajectoire) · ECUE : Mécanique · Niveau : physique-s1-meca/1
Formules : $\vec V = \dot\rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta$ ; $\dfrac{d\vec u_\rho}{dt} = \dot\theta\,\vec u_\theta$ ; $\vec a = (\ddot\rho - \rho\dot\theta^2)\vec u_\rho + (2\dot\rho\dot\theta + \rho\ddot\theta)\vec u_\theta$, circulaire uniforme : $\vec a = -R\dot\theta^2\,\vec u_\rho$ ; $\vec V = (\dot x, \dot y)$ ; $\vec v = \dfrac{ds}{dt}\vec u_T$ ; $s(t) = \int_0^t v\,dt + s(0)$ ; éliminer $t$ avec $\cos^2 + \sin^2 = 1$

1. Le vecteur vitesse en coordonnées polaires s'écrit : a) $\vec V = \rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta$ ; b) $\vec V = \dot\rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta$ ; c) $\vec V = \dot\rho\,\vec u_\rho + \rho\ddot\theta\,\vec u_\theta$.
> Réponse b).
2. Le vecteur unitaire $\vec u_\rho$ des coordonnées polaires vérifie : a) $\dfrac{d\vec u_\rho}{dt} = -\dot\theta\,\vec u_\theta$ ; b) $\dfrac{d\vec u_\rho}{dt} = \vec 0$ ; c) $\dfrac{d\vec u_\rho}{dt} = \dot\theta\,\vec u_\rho$ ; d) $\dfrac{d\vec u_\rho}{dt} = \dot\theta\,\vec u_\theta$.
> Réponse d).
3. Le vecteur accélération en polaires est $\vec a = (\ddot\rho - \rho\dot\theta^2)\vec u_\rho + (2\dot\rho\dot\theta + \rho\ddot\theta)\vec u_\theta$. Pour un mouvement circulaire uniforme de rayon $R$, il s'écrit : a) $(0,\ R\ddot\theta)$ ; b) $(R\dot\theta^2,\ 0)$ ; c) $(-R\dot\theta^2,\ R\ddot\theta)$ ; d) $(-R\dot\theta^2,\ 0)$.
> Réponse d).
4. Un point se déplace dans le plan $(x, y)$ à partir de $t = 1$ s avec $x(t) = \ln t$ et $y(t) = t + \dfrac1t$. Son vecteur vitesse en cartésiennes est : a) $\left(\dfrac1t,\ 1 + \dfrac1{t^2}\right)$ ; b) $\left(\dfrac1t,\ 1 - \dfrac1{t^2}\right)$ ; c) $\left(1,\ 1 - \dfrac1{t^2}\right)$.
> Réponse b).
5. Dans la base de Frenet, le vecteur vitesse s'exprime par : a) $\vec v = \dfrac{ds}{dt}\vec u_T$ ; b) $\vec v = R\,\dot\theta\,\vec u_T$ ; c) $\vec v = R\dot\theta\,\vec u_N$.
> Réponse a).
6. Dans la base de Frenet, l'abscisse curviligne est : a) $s(t) = \int_0^t a_T\,dt + s(0)$ ; b) $s(t) = \int_0^t v\,dt + s(0)$ ; c) $s(t) = \int_0^t a_N\,dt + s(0)$.
> Réponse b).
7. Le vecteur vitesse d'un mouvement d'équations horaires $x(t) = -2t^3 - t$ et $y(t) = 4t^2$ est : a) $(-6t - 1,\ 8t)$ ; b) $(-6t^2 - 1,\ 8t)$ ; c) $(-2t^2 - 1,\ 8t)$.
> Réponse b).
8. Un mouvement plan $(X, Y)$ a pour équations horaires $x = R\cos\omega t$ et $y = R\sin\omega t$ ($R$ et $\omega$ constantes positives). L'équation de la trajectoire est : a) $x^2 + y^2 = R$ ; b) $x^2 + y^2 = (R\omega)^2$ ; c) $\dfrac{x^2}{R^2} + \dfrac{y^2}{R^2} = 1$ ; d) $x^2 - y^2 = R^2$.
> Réponse c).

## Exercice 1 (5 points)
Type : mouvement elliptique en cartésien (trajectoire, vitesse, accélération, $\vec a = -\omega^2\overrightarrow{OM}$) · ECUE : Mécanique · Niveau : physique-s1-meca/3
Formules : $\vec V = (\dot x, \dot y)$, $\vec a = (\ddot x, \ddot y)$ ; $\|\vec V\| = \sqrt{\dot x^2 + \dot y^2}$ ; $\cos^2 + \sin^2 = 1$ ; ellipse : $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$ ; $\ddot x = -\omega^2 x$, $\ddot y = -\omega^2 y$

Une particule se déplace dans le plan $(X, Y)$ avec $x(t) = \sqrt2\cos(\omega t)$ et $y(t) = 2\sqrt2\sin(\omega t)$ ($\omega$ constante positive en rad·s$^{-1}$).
1. a) Montrer que l'équation de la trajectoire est de la forme $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$ (ellipse, $a$ et $b$ constantes positives). b) Préciser les valeurs de $a$ et $b$.
> a) $\dfrac{x}{\sqrt2} = \cos\omega t$ et $\dfrac{y}{2\sqrt2} = \sin\omega t$, donc $\dfrac{x^2}2 + \dfrac{y^2}8 = \cos^2\omega t + \sin^2\omega t = 1$. b) $a = \sqrt2$ et $b = 2\sqrt2$ ($b > a$ : le grand axe est vertical).
2. Exprimer les composantes du vecteur vitesse $\vec V(t)$. Donner sa norme.
> $\vec V = (-\sqrt2\omega\sin\omega t,\ 2\sqrt2\omega\cos\omega t)$ ; $V = \sqrt{2\omega^2\sin^2\omega t + 8\omega^2\cos^2\omega t} = \sqrt2\,\omega\sqrt{1 + 3\cos^2\omega t}$.
3. a) Exprimer les composantes du vecteur accélération $\vec a(t)$. Donner sa norme. b) Exprimer $\vec a(t)$ en fonction du vecteur position $\overrightarrow{OM}(t)$.
> a) $\vec a = (-\sqrt2\omega^2\cos\omega t,\ -2\sqrt2\omega^2\sin\omega t)$ ; $a = \sqrt2\,\omega^2\sqrt{1 + 3\sin^2\omega t}$. b) $\vec a = -\omega^2(x\,\vec u_x + y\,\vec u_y) = -\omega^2\,\overrightarrow{OM}(t)$.

## Exercice 2 (5 points)
Type : mouvement rectiligne oscillant en cartésien (trajectoire, tracé, vitesse) · ECUE : Mécanique · Niveau : physique-s1-meca/3
Formules : $\cos 2\varphi = 1 - 2\sin^2\varphi$ ; $0 \leqslant \sin^2 \leqslant 1$ borne le segment parcouru ; $\dot x = 2\omega\sin\omega t\cos\omega t = \omega\sin 2\omega t$ ; $\dot y = -2\omega\sin 2\omega t$ ; $V = \sqrt{\dot x^2 + \dot y^2}$

Mouvement plan d'équations horaires $x(t) = \sin^2(\omega t)$ et $y(t) = 1 + \cos(2\omega t)$ ($\omega$ constante positive).
1. a) Retrouver l'équation de la trajectoire. Préciser sa nature. On donne $\cos(2\omega t) = 1 - 2\sin^2(\omega t)$. b) Tracer cette trajectoire, sachant que $0 \leqslant \sin^2(\omega t) \leqslant 1$.
> a) $y = 1 + 1 - 2\sin^2\omega t = 2 - 2x$ : la trajectoire est une droite. b) Segment de droite d'extrémités $(x, y) = (0, 2)$ et $(1, 0)$ ; le point oscille sur ce segment.
2. Exprimer les composantes du vecteur vitesse en coordonnées cartésiennes. Donner sa norme.
> $\dot x = \omega\sin 2\omega t$ et $\dot y = -2\omega\sin 2\omega t$ (cohérent avec $y = 2 - 2x$), donc $V = \sqrt5\,\omega|\sin 2\omega t|$. Le corrigé manuscrit écrit $\dot y = -2\omega\sin\omega t\cos\omega t$ (un facteur 2 manque) et trouve $\sqrt2\,\omega|\sin 2\omega t|$ : la valeur correcte est $\sqrt5\,\omega|\sin 2\omega t|$.

## Exercice 3. Base cylindrique, base de Frenet (6 points)
Type : hélice en cylindriques et Frenet (vitesse, abscisse curviligne, accélération, rayon de courbure) · ECUE : Mécanique · Niveau : physique-s1-meca/8
Formules : $\overrightarrow{OM} = R\,\vec u_\rho + Kt\,\vec u_z$, $\theta = \omega t$ ; $\vec V = R\dot\theta\,\vec u_\theta + K\vec u_z$, $\dfrac{d\vec u_\rho}{dt} = \dot\theta\,\vec u_\theta$, $\dfrac{d\vec u_\theta}{dt} = -\dot\theta\,\vec u_\rho$ ; $V = \sqrt{R^2\omega^2 + K^2}$ constante ; $s(t) = \int_0^t V\,dt$ ; $a_T = \dfrac{dV}{dt} = 0$, $a_N = \dfrac{V^2}{R_c}$ ; la norme de $\vec a$ ne dépend pas de la base ; $R_c = \dfrac{V^2}{a}$

Mouvement hélicoïdal : combinaison d'un mouvement circulaire de rayon $R$ dans le plan $(X, Y)$ et d'une translation sur l'axe $(OZ)$. En cylindriques : $\overrightarrow{OM}(t) = R\,\vec u_\rho + Kt\,\vec u_z$, avec $R$ et $K$ constantes positives et $\theta(t) = \omega t$ ($\omega$ constante positive).
1. a) Exprimer le vecteur vitesse $\vec V$ en cylindriques. Exprimer sa norme. b) En déduire l'abscisse curviligne $s(t)$, sachant que $V = \dfrac{ds}{dt}$ et $s(t_0 = 0) = 0$.
> a) $\vec V = R\dfrac{d\vec u_\rho}{dt} + K\vec u_z = R\omega\,\vec u_\theta + K\,\vec u_z$ ; $V = \sqrt{R^2\omega^2 + K^2}$ (constante). b) $s(t) = \sqrt{R^2\omega^2 + K^2}\;t$.
2. a) Exprimer le vecteur accélération $\vec a$ en cylindriques. Exprimer sa norme. b) Exprimer les composantes tangentielle $a_T$ et normale $a_N$ dans la base de Frenet ($a_N$ en fonction du rayon de courbure $R_c$). c) En déduire le rayon de courbure $R_c$ en fonction de $R$, $K$ et $\omega$, en utilisant l'égalité des normes de $\vec a$ dans les deux bases.
> a) $\vec a = R\omega\dfrac{d\vec u_\theta}{dt} = -R\omega^2\,\vec u_\rho$ ; $a = R\omega^2$. b) $V$ constante, donc $a_T = \dfrac{dV}{dt} = 0$ et $a_N = \dfrac{V^2}{R_c} = \dfrac{R^2\omega^2 + K^2}{R_c}$. c) $a = a_N$ (car $a_T = 0$) : $R\omega^2 = \dfrac{R^2\omega^2 + K^2}{R_c}$, donc $R_c = \dfrac{R^2\omega^2 + K^2}{R\omega^2}$. Pour $K = 0$ (rotation dans le plan seul) on retrouve $R_c = R$.
