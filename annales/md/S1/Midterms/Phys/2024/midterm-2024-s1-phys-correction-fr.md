# Contrôle 1 S1 — année 2019/2020 (corrigé, FR)

- Source : `raw/S1/Midterms/Phys/2024/midterm-2024-s1-phys-correction-fr.pdf` (7 pages, corrigé manuscrit scanné avec barème)
- Date réelle : année 2019/2020 (S1 2019, dossier promo 2024). Sujet : `midterm-2024-s1-phys-subject-fr.md`.
- Calculatrices et documents non autorisés. QCM sans points négatifs. Barème : 20 points. Rapport avec la mécanique : cinématique du point (cycloïde, hélice, mouvement circulaire non uniforme, Frenet). Les lignes `> ` sont les solutions du corrigé.

## QCM (4 points)
Type : QCM de cinématique (vecteurs, polaires, Frenet, trajectoire) · ECUE : Mécanique · Niveau : physique-s1-meca/1
Formules : $\vec V_1 \cdot \vec V_2 = V_1V_2\cos\alpha$, négatif si les vecteurs sont de sens opposés ; $\|\vec V_1 \wedge \vec V_2\| = V_1V_2|\sin\alpha|$ ; $(\cos^2\theta)' = -2\dot\theta\cos\theta\sin\theta$ ; $\vec V = \dot\rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta + \dot z\,\vec u_z$ ; $\vec a = (\ddot\rho - \rho\dot\theta^2)\vec u_\rho + (2\dot\rho\dot\theta + \rho\ddot\theta)\vec u_\theta$ ; $\dfrac{d\vec u_\rho}{dt} = \dot\theta\,\vec u_\theta$ ; $x = \rho\cos\theta$, $y = \rho\sin\theta$

1. Le produit scalaire de deux vecteurs non nuls, colinéaires et de sens opposés est : a) strictement positif ; b) nul ; c) strictement négatif.
> Réponse c).
2. Les composantes de $\vec F_1$ (flèche vers le bas à gauche, angle $\alpha$ avec l'axe $y$) sont : a) $(-F_1\cos\alpha,\ F_1\sin\alpha)$ ; b) $(-F_1\sin\alpha,\ -F_1\cos\alpha)$ ; c) $(-F_1\sin\alpha,\ F_1\cos\alpha)$.
> Réponse b).
3. La norme de $\vec V_3 = \vec V_1 \wedge \vec V_2$, avec $(\vec V_1, \vec V_2) = \alpha$, est : a) $V_3 = V_1V_2|\sin\alpha|$ ; b) $V_3 = V_1V_2|\cos\alpha|$ ; c) $V_3 = \sqrt{V_1^2 + V_2^2 + 2V_1V_2\cos\alpha}$.
> Réponse a).
4. La dérivée par rapport à $t$ de $f(t) = A\cos^2(\theta(t))$, $A$ constante, est : a) $2A\dot\theta\cos\theta\sin\theta$ ; b) $-2A\dot\theta\cos\theta\sin\theta$ ; c) $2A\cos\theta\sin\theta$.
> Réponse b).
5. Le vecteur vitesse en coordonnées cylindriques s'écrit : a) $\vec V = \dot\rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta$ ; b) $\vec V = \rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta + \dot z\,\vec u_z$ ; c) $\vec V = \dot\rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta + \dot z\,\vec u_z$.
> Réponse c).
6. Le vecteur accélération en polaires est $\vec a = (\ddot\rho - \rho\dot\theta^2)\vec u_\rho + (2\dot\rho\dot\theta + \rho\ddot\theta)\vec u_\theta$. Pour un mouvement circulaire décéléré de rayon $R$, il s'écrit : a) $(0,\ R\ddot\theta)$ ; b) $(R\dot\theta^2,\ 0)$ ; c) $(-R\dot\theta^2,\ R\ddot\theta)$ ; d) $(-R\dot\theta^2,\ 0)$.
> Réponse c).
7. Le vecteur unitaire $\vec u_\rho$ des coordonnées polaires vérifie : a) $\dfrac{d\vec u_\rho}{dt} = -\dot\theta\,\vec u_\theta$ ; b) $\dfrac{d\vec u_\rho}{dt} = \vec 0$ ; c) $\dfrac{d\vec u_\rho}{dt} = \dot\theta\,\vec u_\rho$ ; d) $\dfrac{d\vec u_\rho}{dt} = \dot\theta\,\vec u_\theta$.
> Réponse d).
8. Les équations horaires polaires sont $\rho(t) = \rho_0e^{\omega t}$, $\theta(t) = \omega t$ ($\rho_0$, $\omega$ constantes positives). En cartésiennes : a) $x = \rho_0\sin\omega t$, $y = \rho_0\cos\omega t$ ; b) $x = \rho_0e^{\omega t}\cos\omega t$, $y = \rho_0e^{\omega t}\sin\omega t$ ; c) $x = \rho_0e^{\omega t}\sin\omega t$, $y = \rho_0e^{\omega t}\cos\omega t$.
> Réponse b).

## Exercice 1 (6 points)
Type : cycloïde (vitesse, accélération, normes, tracé) · ECUE : Mécanique · Niveau : physique-s1-meca/3
Formules : $\vec V = (\dot x, \dot y)$, $\vec a = (\ddot x, \ddot y)$ ; $\|\vec V\| = \sqrt{\dot x^2 + \dot y^2}$ ; $1 - \cos\alpha = 2\sin^2(\alpha/2)$ ; $\omega = 2\pi/T$ ; tracé : tableau de valeurs de $(x(t), y(t))$ en $t = 0, T/4, T/2, 3T/4, T$

La cycloïde est la trajectoire d'un point d'un cercle de rayon $R$ roulant sans glisser sur une droite $(D)$. On peut aussi la définir comme la trajectoire d'un mouvement composé d'un mouvement rectiligne uniforme et d'un mouvement circulaire uniforme de même vitesse. Ses équations horaires sont $x(t) = A(\omega t - \sin\omega t)$ et $y(t) = A(1 - \cos\omega t)$ ($A$ et $\omega$ constantes positives).
1. Déterminer les composantes cartésiennes des vecteurs vitesse et accélération.
> $\vec V = (A\omega(1 - \cos\omega t),\ A\omega\sin\omega t)$ et $\vec a = (A\omega^2\sin\omega t,\ A\omega^2\cos\omega t)$.
2. En déduire la norme de chacun de ces vecteurs. On donne $1 - \cos\alpha = 2\sin^2(\alpha/2)$.
> $V = A\omega\sqrt{(1 - \cos\omega t)^2 + \sin^2\omega t} = A\omega\sqrt{2(1 - \cos\omega t)} = 2A\omega\left|\sin\dfrac{\omega t}2\right|$ et $a = A\omega^2\sqrt{\sin^2\omega t + \cos^2\omega t} = A\omega^2$.
3. Tracer la cycloïde ($y = f(x)$) sur un intervalle de deux périodes ($2T$), avec $\omega = 2\pi/T$ (valeurs : $t = 0$, $T/4$, $T/2$, $3T/4$, $T$).
> $t = 0$ : $(0, 0)$ ; $t = T/4$ : $\left(A\left(\dfrac\pi2 - 1\right), A\right)$ ; $t = T/2$ : $(\pi A, 2A)$ ; $t = 3T/4$ : $\left(A\left(\dfrac{3\pi}2 + 1\right), A\right)$ ; $t = T$ : $(2\pi A, 0)$. Arches identiques, translatées de $2\pi A$ à chaque période, avec un point de rebroussement sur l'axe $x$ ($V = 0$ en $t = kT$).

## Exercice 2 (6 points)
Type : hélice circulaire (cartésiennes puis cylindriques : vitesse, accélération, nature du mouvement) · ECUE : Mécanique · Niveau : physique-s1-meca/8
Formules : $\vec V = (\dot x, \dot y, \dot z)$, $\vec a = (\ddot x, \ddot y, \ddot z)$ ; $\rho = \sqrt{x^2 + y^2}$, $\theta = \arctan(y/x)$ ; $\overrightarrow{OM} = \rho\,\vec u_\rho + z\,\vec u_z$ ; $\vec V = \dot\rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta + \dot z\,\vec u_z$ ; $\vec a = (\ddot\rho - \rho\dot\theta^2)\vec u_\rho + (2\dot\rho\dot\theta + \rho\ddot\theta)\vec u_\theta + \ddot z\,\vec u_z$ ; la norme ne dépend pas de la base orthonormée

Mouvement hélicoïdal : $x(t) = R\cos\omega t$, $y(t) = R\sin\omega t$, $z(t) = H\omega t$ ($R$, $\omega$, $H$ constantes positives).
1. Exprimer le vecteur vitesse en coordonnées cartésiennes, en déduire sa norme.
> $\vec V = (-R\omega\sin\omega t,\ R\omega\cos\omega t,\ H\omega)$, $V = \omega\sqrt{R^2 + H^2}$.
2. Exprimer le vecteur accélération en coordonnées cartésiennes, en déduire sa norme.
> $\vec a = (-R\omega^2\cos\omega t,\ -R\omega^2\sin\omega t,\ 0)$, $a = R\omega^2$.
3. a) Utiliser les équations horaires et les équations de passage pour exprimer $\overrightarrow{OM}(t)$ en coordonnées cylindriques. b) Exprimer les vecteurs vitesse et accélération en coordonnées cylindriques, retrouver les normes des questions 1 et 2.
> a) $\rho = \sqrt{x^2 + y^2} = R$, $\theta = \omega t$, donc $\overrightarrow{OM} = R\,\vec u_\rho + H\omega t\,\vec u_z$. b) $\vec V = R\omega\,\vec u_\theta + H\omega\,\vec u_z$, $V = \omega\sqrt{R^2 + H^2}$ ; $\vec a = -R\omega^2\,\vec u_\rho$, $a = R\omega^2$.

## Exercice 3 (4 points)
Type : mouvement circulaire à vitesse variable (abscisse curviligne, tour complet, composantes de Frenet) · ECUE : Mécanique · Niveau : physique-s1-meca/13
Formules : $s(t) = \int_0^t v\,dt$ ; $\int \dfrac{dt}{1 + \alpha t} = \dfrac1\alpha\ln(1 + \alpha t)$ ; un tour : $s = 2\pi R$ ; $a_T = \dfrac{dv}{dt}$, $a_N = \dfrac{v^2}{R}$, $a = \sqrt{a_T^2 + a_N^2}$

Un point matériel décrit un cercle de centre $O$ et de rayon $R$ avec une vitesse de norme $v(t) = \dfrac{v_0}{1 + \alpha t}$ ($v_0$ et $\alpha$ constantes positives).
1. a) Exprimer l'abscisse curviligne $s(t)$, sachant que $s(t_0 = 0) = 0$. b) En déduire le temps au bout duquel le mobile fait un tour, en fonction de $\alpha$, $v_0$ et $R$.
> a) $s(t) = \dfrac{v_0}\alpha\ln(1 + \alpha t)$. b) $s = 2\pi R \Rightarrow 1 + \alpha t = e^{2\pi R\alpha/v_0}$, donc $t = \dfrac1\alpha\left(e^{2\pi R\alpha/v_0} - 1\right)$.
2. Exprimer les composantes $a_T$ et $a_N$ du vecteur accélération en base de Frenet. En déduire la norme du vecteur accélération dans cette base.
> $a_T = \dfrac{dv}{dt} = -\dfrac{\alpha v_0}{(1 + \alpha t)^2}$, $a_N = \dfrac{v^2}{R} = \dfrac{v_0^2}{R(1 + \alpha t)^2}$, $a = \sqrt{a_T^2 + a_N^2} = \dfrac{v_0}{(1 + \alpha t)^2}\sqrt{\alpha^2 + \dfrac{v_0^2}{R^2}}$.
