# Contrôle 1 S1 — année 2018/2019 (sujet, FR)

- Source : `raw/S1/Midterms/Phys/2023/midterm-2023-s1-phys-subject-fr.pdf` (7 pages)
- Date réelle : année 2018/2019 (S1 2018, dossier promo 2023). Pas de corrigé.
- Calculatrices et documents non autorisés. Réponses sur le sujet. QCM sans points négatifs. Barème : 20 points. Rapport avec la mécanique : cinématique du point (vecteurs, polaires, cylindriques, Frenet). La numérotation du QCM saute de 4 à 6 dans le sujet.

## QCM (4 points)
Type : QCM de cinématique (vecteurs, polaires, Frenet, trajectoire) · ECUE : Mécanique · Niveau : physique-s1-meca/1
Formules : projection d'un vecteur de norme $F$ faisant l'angle $\alpha$ avec l'axe $x$ : $(F\cos\alpha, F\sin\alpha)$ ; $\vec V_1 \wedge \vec V_2 = (y_1z_2 - z_1y_2,\ z_1x_2 - x_1z_2,\ x_1y_2 - y_1x_2)$ ; $\vec V = \dot\rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta$ ; $\vec a = (\ddot\rho - \rho\dot\theta^2)\vec u_\rho + (2\dot\rho\dot\theta + \rho\ddot\theta)\vec u_\theta$ ; cercle : $\rho = R$ ; Frenet : $\vec V = R\dot\theta\,\vec u_T$, $a_T = dV/dt$, $a_N = V^2/R$

1. Les composantes de $\vec F_1$ (flèche dirigée vers le bas à droite, angle $\alpha$ sous l'axe $x$) sont : a) $(F_1\cos\alpha,\ -F_1\sin\alpha)$ ; b) $(-F_1\sin\alpha,\ F_1\cos\alpha)$ ; c) $(F_1\sin\alpha,\ -F_1\cos\alpha)$.
2. Les composantes de $\vec F_2$ (flèche horizontale dirigée vers la gauche) sont : a) $(-F_2, 0)$ ; b) $(F_2, 0)$ ; c) $(0, -F_2)$.
3. Le produit vectoriel de $\vec V_1 = (1, 3, 2)$ et $\vec V_2 = (-4, 1, 1)$ est : a) $\vec W = (1, 9, 13)$ ; b) $\vec W = (1, -9, 13)$ ; c) $\vec W = (1, -11, 12)$.
4. Le vecteur vitesse en coordonnées polaires s'écrit : a) $\vec V = \dot\rho\,\vec u_\rho + \dot\theta\,\vec u_\theta$ ; b) $\vec V = \dot\rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta$ ; c) $\vec V = \rho\,\vec u_\rho + \dot\theta\,\vec u_\theta$.
6. Le vecteur accélération en coordonnées polaires est $\vec a = (\ddot\rho - \rho\dot\theta^2)\vec u_\rho + (2\dot\rho\dot\theta + \rho\ddot\theta)\vec u_\theta$. Dans le cas d'un mouvement circulaire accéléré de rayon $R$, il s'écrit : a) $\vec a = (0,\ R\ddot\theta)$ ; b) $\vec a = (-R\dot\theta^2,\ R\ddot\theta)$ ; c) $\vec a = (-R\dot\theta^2,\ 0)$ ; d) $\vec a = (R\dot\theta^2,\ 0)$.
7. Dans la base de Frenet, le vecteur vitesse s'écrit : a) $\vec V = R(t)\dot\theta(t)\,\vec u_N$ ; b) $\vec V = R(t)\ddot\theta\,\vec u_T$ ; c) $\vec V = R(t)\dot\theta(t)\,\vec u_T$.
8. Le vecteur accélération en base de Frenet s'écrit : a) $a_T = \dfrac{dV}{dt}$, $a_N = \dfrac{V^2}{R^2}$ ; b) $a_T = \dfrac{dV}{dt}$, $a_N = \dfrac{V^2}{R}$ ; c) $a_T = \dfrac{d\rho}{dt}$, $a_N = \dfrac{V^2}{R}$.

## Exercice 1 (4 points)
Type : mouvement elliptique en cartésien (trajectoire, vitesse, accélération, $\vec a = -\omega^2\overrightarrow{OM}$) · ECUE : Mécanique · Niveau : physique-s1-meca/3
Formules : $\vec V = (\dot x, \dot y)$, $\vec a = (\ddot x, \ddot y)$ ; $\|\vec V\| = \sqrt{\dot x^2 + \dot y^2}$ ; $\cos^2 + \sin^2 = 1$ ; ellipse : $\dfrac{x^2}{A^2} + \dfrac{y^2}{B^2} = 1$ ; $\ddot x = -\omega^2 x$, $\ddot y = -\omega^2 y$

Les équations horaires dans le plan $(xOy)$ d'un point matériel sont $x(t) = 2a\cos(\omega t)$ et $y(t) = a\sin(\omega t)$ ($a$ et $\omega$ constantes positives).
1. Retrouver l'équation de la trajectoire de ce mouvement, préciser sa nature.
2. Exprimer le vecteur vitesse, en déduire sa norme.
3. a) Exprimer le vecteur accélération, en déduire sa norme. b) En déduire une relation entre les vecteurs $\vec a$ et $\overrightarrow{OM}$.

## Exercice 2 (8 points)
Type : spirale sur un cône en cylindriques (vitesse, accélération, passage en cartésien) · ECUE : Mécanique · Niveau : physique-s1-meca/8
Formules : $\overrightarrow{OM} = \rho\,\vec u_\rho + z\,\vec u_z$ ; $\vec V = \dot\rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta + \dot z\,\vec u_z$ ; $\vec a = (\ddot\rho - \rho\dot\theta^2)\vec u_\rho + (2\dot\rho\dot\theta + \rho\ddot\theta)\vec u_\theta + \ddot z\,\vec u_z$ ; $x = \rho\cos\theta$, $y = \rho\sin\theta$ ; $(e^{\omega t})' = \omega e^{\omega t}$ ; la norme est la même dans toute base orthonormée

On considère le mouvement d'un point matériel sur une spirale tracée sur un cône. Les équations horaires en coordonnées cylindriques sont $\rho(t) = \rho_0\,e^{\omega t}$ et $z(t) = a\rho_0\,e^{\omega t}$ ($\rho_0$, $a$ et $\omega$ constantes positives). On donne $\theta(t) = \omega t$.
1. a) Écrire le vecteur position $\overrightarrow{OM}$ en coordonnées cylindriques. En déduire le vecteur vitesse. b) Montrer que $V(t) = \rho_0\,\omega\,e^{\omega t}\sqrt{2 + a^2}$.
2. a) Exprimer le vecteur accélération. b) Montrer que $a(t) = \rho_0\,\omega^2\,e^{\omega t}\sqrt{4 + a^2}$.
3. Utiliser les équations de passage pour exprimer les équations horaires $x(t)$, $y(t)$ et $z(t)$ en coordonnées cartésiennes.
4. a) Exprimer le vecteur vitesse en coordonnées cartésiennes. b) Retrouver la norme du vecteur vitesse calculée à la question 1b.
5. a) Exprimer le vecteur accélération en coordonnées cartésiennes. b) Retrouver la norme du vecteur accélération calculée à la question 2b.

## Exercice 3 (4 points)
Type : mouvement circulaire (trajectoire, vitesse, accélération, composantes de Frenet, rayon de courbure) · ECUE : Mécanique · Niveau : physique-s1-meca/13
Formules : $x^2 + y^2 = R^2$ ; $\vec V = (\dot x, \dot y)$, $\vec a = (\ddot x, \ddot y)$ ; $a_T = \dfrac{dv}{dt}$, $a_N = \dfrac{v^2}{R_c}$, $a^2 = a_T^2 + a_N^2$ ; $R_c = \dfrac{v^2}{a_N}$ ; mouvement circulaire uniforme : $a_T = 0$, $R_c = R$

Les coordonnées cartésiennes d'un point M mobile dans le plan $(xOy)$ sont $x(t) = 2\cos(0{,}5\,t)$ et $y(t) = 2\sin(0{,}5\,t)$.
1. Déterminer l'équation et la nature de la trajectoire.
2. Déterminer les composantes des vecteurs vitesse et accélération ainsi que leurs normes.
3. Déterminer les composantes normale et tangentielle de l'accélération dans un repère de Frenet.
4. En déduire le rayon de courbure de la trajectoire.
