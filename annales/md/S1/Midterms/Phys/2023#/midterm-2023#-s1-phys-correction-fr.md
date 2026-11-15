# Contrôle S1 — mai 2018 (corrigé, FR)

- Source : `raw/S1/Midterms/Phys/2023#/midterm-2023#-s1-phys-correction-fr.pdf` (5 pages, corrigé manuscrit scanné)
- Date réelle : mai 2018 (S1#, dossier promo 2023#). Sujet : `midterm-2023#-s1-phys-subject-fr.md`.
- Calculatrices et documents non autorisés. QCM sans points négatifs. Barème : 20 points. Rapport avec la mécanique : cinématique du point (vecteurs, ellipse, hélice, cylindriques, Frenet). Les lignes `> ` sont les solutions manuscrites du corrigé.

## QCM (5 points)
Type : QCM de cinématique (vecteurs, polaires, Frenet, trajectoire) · ECUE : Mécanique · Niveau : physique-s1-meca/1
Formules : $\|\vec F_1 + \vec F_2\| = \sqrt{F_1^2 + F_2^2}$ si $\vec F_1 \perp \vec F_2$ ; projection d'un vecteur de norme $F$ : $(\pm F\cos\alpha, \pm F\sin\alpha)$ selon le quadrant ; $\vec V_1 \cdot \vec V_2 = V_1V_2\cos\alpha$ ; $\vec V_1 \wedge \vec V_2 = (y_1z_2 - z_1y_2,\ z_1x_2 - x_1z_2,\ x_1y_2 - y_1x_2)$ ; $\vec V = \dot\rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta$ ; $\vec a = (\ddot\rho - \rho\dot\theta^2)\vec u_\rho + (2\dot\rho\dot\theta + \rho\ddot\theta)\vec u_\theta$ ; Frenet : $\vec V = R\dot\theta\,\vec u_T$, $a_T = dV/dt$, $a_N = V^2/R$

1. La norme de la résultante $\vec R$ de deux forces $\vec F_1$ et $\vec F_2$ (non nulles) et orthogonales est : a) $R = 0$ ; b) $R = |F_1 - F_2|$ ; c) $R = F_1 + F_2$ ; d) $R = \sqrt{F_1^2 + F_2^2}$.
> Réponse d).
2. Les composantes de $\vec F_1$ (flèche dans le deuxième quadrant, angle $\alpha$ avec l'axe $y$) sont : a) $(F_1\sin\alpha,\ -F_1\cos\alpha)$ ; b) $(-F_1\sin\alpha,\ F_1\cos\alpha)$ ; c) $(-F_1\cos\alpha,\ F_1\sin\alpha)$.
> Réponse b).
3. Le produit scalaire de deux vecteurs colinéaires et de sens opposé est : a) strictement négatif ; b) nul ; c) strictement positif.
> Réponse a).
4. Le produit vectoriel de $\vec V_1 = (1, 3, 2)$ et $\vec V_2 = (-4, 1, 1)$ est : a) $\vec W = (1, 9, 13)$ ; b) $\vec W = (1, -9, 13)$ ; c) $\vec W = (1, -11, 12)$.
> Réponse b).
5. Le vecteur vitesse en coordonnées polaires s'écrit : a) $\vec V = \dot\rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta$ ; b) $\vec V = \dot\rho\,\vec u_\rho + \dot\theta\,\vec u_\theta$ ; c) $\vec V = \rho\,\vec u_\rho + \dot\theta\,\vec u_\theta$.
> Réponse a).
6. Le vecteur accélération en polaires est $\vec a = (\ddot\rho - \rho\dot\theta^2)\vec u_\rho + (2\dot\rho\dot\theta + \rho\ddot\theta)\vec u_\theta$. Pour un mouvement circulaire uniforme de rayon $R$, il s'écrit : a) $(0,\ R\ddot\theta)$ ; b) $(-R\dot\theta^2,\ R\ddot\theta)$ ; c) $(-R\dot\theta^2,\ 0)$ ; d) $(R\dot\theta^2,\ 0)$.
> Réponse c).
7. Dans la base de Frenet, le vecteur vitesse s'écrit : a) $\vec V = R(t)\dot\theta(t)\,\vec u_N$ ; b) $\vec V = R(t)\ddot\theta\,\vec u_T$ ; c) $\vec V = R(t)\dot\theta(t)\,\vec u_T$.
> Réponse c).
8. Le vecteur accélération en base de Frenet s'écrit : a) $a_T = \dfrac{dV}{dt}$, $a_N = \dfrac{V^2}{R^2}$ ; b) $a_T = \dfrac{d\rho}{dt}$, $a_N = \dfrac{V^2}{R}$ ; c) $a_T = \dfrac{dV}{dt}$, $a_N = \dfrac{V^2}{R}$.
> Réponse c).

## Exercice 1 (6 points)
Type : mouvement elliptique en cartésien (trajectoire, vitesse, accélération, $\vec a = -\omega^2\overrightarrow{OM}$) · ECUE : Mécanique · Niveau : physique-s1-meca/3
Formules : $\vec V = (\dot x, \dot y)$, $\vec a = (\ddot x, \ddot y)$ ; $\|\vec V\| = \sqrt{\dot x^2 + \dot y^2}$ ; $\cos^2 + \sin^2 = 1$ ; ellipse : $\dfrac{x^2}{A^2} + \dfrac{y^2}{B^2} = 1$ ; $\ddot x = -\omega^2 x$, $\ddot y = -\omega^2 y$

Les équations horaires dans le plan $(xOy)$ d'un point matériel sont $x(t) = 2a\cos(\omega t)$ et $y(t) = a\sin(\omega t)$ ($a$ et $\omega$ constantes positives).
1. a) Montrer que la trajectoire est elliptique. On rappelle l'équation d'une ellipse de centre $O$ et de demi-axes $A$ et $B$ : $\dfrac{x^2}{A^2} + \dfrac{y^2}{B^2} = 1$ ($A$ et $B$ constantes positives). b) Identifier $A$ et $B$ en fonction de $a$.
> a) $\dfrac{x}{2a} = \cos\omega t$ et $\dfrac ya = \sin\omega t$, donc $\dfrac{x^2}{4a^2} + \dfrac{y^2}{a^2} = \cos^2\omega t + \sin^2\omega t = 1$. b) Trajectoire elliptique pour tout $t$, avec $A = 2a$ (demi-grand axe) et $B = a$ (demi-petit axe).
2. Exprimer le vecteur vitesse, en déduire la norme de ce vecteur.
> $\dot x = -2a\omega\sin\omega t$, $\dot y = a\omega\cos\omega t$. $V = a\omega\sqrt{4\sin^2\omega t + \cos^2\omega t} = a\omega\sqrt{3\sin^2\omega t + 1}$.
3. Même question pour le vecteur accélération.
> $a_x = -2a\omega^2\cos\omega t$, $a_y = -a\omega^2\sin\omega t$. $a = a\omega^2\sqrt{4\cos^2\omega t + \sin^2\omega t} = a\omega^2\sqrt{3\cos^2\omega t + 1}$.

## Exercice 2 (9 points)
Type : hélice circulaire (cartésiennes puis cylindriques : vitesse, accélération, nature du mouvement) · ECUE : Mécanique · Niveau : physique-s1-meca/8
Formules : $\vec V = (\dot x, \dot y, \dot z)$, $\vec a = (\ddot x, \ddot y, \ddot z)$ ; $x^2 + y^2 = R^2$ : cercle de rayon $R$ ; $\dot z = \text{cste}$ : mouvement rectiligne uniforme selon $Oz$ ; $\rho = \sqrt{x^2 + y^2}$, $\theta = \arctan(y/x)$ ; $\overrightarrow{OM} = \rho\,\vec u_\rho + z\,\vec u_z$ ; $\vec V = \dot\rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta + \dot z\,\vec u_z$ ; $\vec a = (\ddot\rho - \rho\dot\theta^2)\vec u_\rho + (2\dot\rho\dot\theta + \rho\ddot\theta)\vec u_\theta + \ddot z\,\vec u_z$

Partie A : coordonnées cartésiennes. Un point M est repéré par $x(t) = R\cos(\omega t)$, $y(t) = R\sin(\omega t)$, $z(t) = H\omega t$ ($R$, $\omega$, $H$ constantes positives).
A1. Exprimer le vecteur vitesse de M dans la base cartésienne $(\vec u_x, \vec u_y, \vec u_z)$. Calculer sa norme.
> $\vec V = (-R\omega\sin\omega t,\ R\omega\cos\omega t,\ H\omega)$, $V = \omega\sqrt{R^2 + H^2}$.
A2. Exprimer le vecteur accélération de M dans la base cartésienne. Calculer sa norme.
> $\vec a = (-R\omega^2\cos\omega t,\ -R\omega^2\sin\omega t,\ 0)$ car $V_z$ est constante. $a = R\omega^2$.
A3. a) Quel est le mouvement de M dans le plan $(xOy)$ ? Justifier en donnant l'équation de la trajectoire. b) Quel est le mouvement de M selon l'axe $Oz$ ? Justifier.
> a) $x^2 + y^2 = R^2$ : mouvement circulaire de centre $O$ et de rayon $R$. b) $z = H\omega t$ et $V_z = \text{cste}$ : mouvement rectiligne uniforme selon $Oz$.

Partie B : coordonnées cylindriques (mêmes équations horaires).
B1. Exprimer le vecteur position dans la base cylindrique $(\vec u_\rho, \vec u_\theta, \vec u_z)$. Utiliser les équations de passage.
> $\overrightarrow{OM} = \rho\,\vec u_\rho + z\,\vec u_z$ avec $\rho = \sqrt{x^2 + y^2} = R$, $z_{cyl} = z_{cart}$, donc $\overrightarrow{OM} = R\,\vec u_\rho + H\omega t\,\vec u_z$.
B2. Exprimer le vecteur vitesse de M dans la base cylindrique.
> $\vec V = R\dot\theta\,\vec u_\theta + H\omega\,\vec u_z$ avec $\theta(t) = \omega t$, $\dot\theta = \omega$ : $\vec V = R\omega\,\vec u_\theta + H\omega\,\vec u_z$.
B3. Exprimer le vecteur accélération de M dans la base cylindrique.
> $\vec a = R\omega\,\dfrac{d\vec u_\theta}{dt} = -R\omega^2\,\vec u_\rho$ (avec $\dfrac{d\vec u_\theta}{dt} = -\dot\theta\,\vec u_\rho$). L'accélération est radiale, dirigée vers le centre.
