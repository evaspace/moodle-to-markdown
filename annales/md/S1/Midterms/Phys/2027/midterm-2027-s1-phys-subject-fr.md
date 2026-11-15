# Contrôle de physique S1 — octobre 2022 (sujet, FR)

- Source : `raw/S1/Midterms/Phys/2027/midterm-2027-s1-phys-subject-fr.pdf` (6 pages)
- Date réelle : octobre 2022 (EPITA InfoS1, dossier promo 2027). Pas de corrigé : le PDF est la copie annotée d'un étudiant (réponses manuscrites, en partie fausses ou barrées), non reprises ici.
- Durée : 1 h. Calculatrices et documents non autorisés. Barème indicatif : 20 points (6 + 8 + 6). Rapport avec la mécanique : cinématique du point (unités, projectile lancé d'une hauteur, vilebrequin en polaires puis cartésiennes).

## Exercice 1. Questions de cours (6 points, pas de points négatifs pour le QCM)
Type : QCM de cinématique (vecteurs, polaires, Frenet, trajectoire) · ECUE : Mécanique · Niveau : physique-s1-meca/1
Formules : accélération : m·s$^{-2}$ ; mouvement uniforme : $\|\vec v\| = \text{cste}$ ; rectiligne uniforme : $\vec a = \vec 0$ ; circulaire uniforme : $\vec a = -R\dot\theta^2\vec u_\rho \neq \vec 0$ ; $\vec v = (\dot x, \dot y)$ ; parabole : $y$ polynôme de degré 2 en $x$ ; cylindriques : $\overrightarrow{OM} = \rho\,\vec u_\rho + z\,\vec u_z$ ; polaires : $\vec v = \dot\rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta$ ; circulaire uniforme : $\dot\rho = 0$, $\dot\theta = \text{cste}$, $\ddot\theta = 0$

Choisissez la ou les bonnes réponses.
1. L'unité d'une accélération peut être : a) m·s$^{-1}$ ; b) m·s$^{-2}$ ; c) kg·m·s$^{-1}$ ; d) kg·s$^{-2}$.
2. Choisir la ou les affirmations justes : a) un mouvement peut être uniforme sur une seule de ses composantes ; b) l'équation de la trajectoire permet de dire si le mouvement est uniforme ; c) lors d'un mouvement circulaire uniforme, l'accélération est nulle ; d) lors d'un mouvement rectiligne uniforme, l'accélération est nulle.
3. Un mouvement a pour équations horaires $x(t) = 4t$ et $y(t) = 3t^2 - 6t + 5$ : a) ce mouvement est décéléré ; b) ce mouvement est uniforme ; c) la vitesse s'annule en un point de la trajectoire ; d) ce mouvement est parabolique.
4. En coordonnées cylindriques, le vecteur position a pour expression : a) $\overrightarrow{OM} = \rho\,\vec u_\theta$ ; b) $\overrightarrow{OM} = \rho\,\vec u_\rho + 0\,\vec u_\theta$ ; c) $\overrightarrow{OM} = \rho\,\vec u_\rho + \theta\,\vec u_\theta + z\,\vec u_z$ ; d) $\overrightarrow{OM} = \rho\,\vec u_\rho + z\,\vec u_z$.
5. En coordonnées polaires, le vecteur vitesse a pour expression : a) $\vec v = \rho\dot\theta\,\vec u_\theta$ ; b) $\vec v = \dot\rho\,\vec u_\rho$ ; c) $\vec v = \rho\,\vec u_\rho$ ; d) $\vec v = \dot\rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta$.
6. Pour un mouvement circulaire uniforme : a) $\dot\theta = \text{constante}$ ; b) $\dot\theta = 0$ ; c) $\ddot\theta = 0$ ; d) $\dot\rho = 0$.

## Exercice 2. Cinématique en coordonnées cartésiennes (8 points)
Type : projectile lancé d'une hauteur $h$ (équations horaires, trajectoire, vitesse, accélération, sommet) · ECUE : Mécanique · Niveau : physique-s1-meca/5
Formules : $x = v_0\cos\alpha\,t$, $y = -\tfrac12gt^2 + v_0\sin\alpha\,t + h$ ; $y(x) = -\dfrac{g}{2v_0^2\cos^2\alpha}x^2 + \tan\alpha\,x + h$ ; $\vec v = (v_0\cos\alpha,\ -gt + v_0\sin\alpha)$, $\vec a = -g\,\vec u_y$ ; sommet S : $v_y = 0 \Rightarrow t_S = \dfrac{v_0\sin\alpha}{g}$, $x_S = v_0\cos\alpha\,t_S$ ; selon $Ox$ : mouvement rectiligne uniforme, selon $Oy$ : rectiligne uniformément varié

On étudie la trajectoire d'une balle dans le plan muni d'un repère cartésien. La balle est lancée avec une vitesse $\vec v_0$ faisant un angle $\alpha$ avec l'horizontale depuis le point de coordonnées $(0, h)$ (point A, sol en O). Le vecteur position est $\overrightarrow{OM}(t) = (v_0\cos\alpha)\,t\,\vec u_x + \left(-\dfrac12gt^2 + (v_0\sin\alpha)\,t + h\right)\vec u_y$, où $g$ est l'intensité du champ de pesanteur terrestre. Le schéma représente la trajectoire avec les points $M_1$, $S$ (sommet), $M_2$, $M_3$ et P (impact au sol).
1. Donner les équations horaires du mouvement.
2. Établir l'équation de la trajectoire.
3. Calculer le vecteur vitesse $\vec v(t)$ en fonction de $v_0$, $\alpha$, $t$ et $g$, et calculer sa norme.
4. Calculer le vecteur accélération $\vec a(t)$ et calculer sa norme.
5. Commenter les résultats des questions 3 et 4 en qualifiant le mouvement sur l'axe $Ox$ et sur l'axe $Oy$.
6. Sur le schéma, représenter les vecteurs vitesse et accélération aux points $M_1$, $M_2$, $M_3$ et S.
7. Calculer les coordonnées $(x_S, y_S)$ du sommet S de la trajectoire.
8. À quelle date $t'$ la balle atteint-elle le sommet ?

## Exercice 3. Cinématique en coordonnées polaires et cartésiennes (6 points)
Type : vilebrequin (polaires puis cartésiennes : position, vitesse, accélération du piston) · ECUE : Mécanique · Niveau : physique-s1-meca/6
Formules : $\theta(t) = \omega t \Rightarrow \dot\theta = \omega$ ; polaires : $\overrightarrow{OM} = R\,\vec u_\rho$, $\vec v = R\omega\,\vec u_\theta$, $\vec a = -R\omega^2\,\vec u_\rho$ ; cartésiennes : $\vec v = \dfrac{d\overrightarrow{OP}}{dt}$, $\vec a = \dfrac{d\vec v}{dt}$ ; $(\sin\omega t)' = \omega\cos\omega t$, $(\cos\omega t)' = -\omega\sin\omega t$

Un vilebrequin est une pièce mécanique d'un moteur thermique qui transforme un mouvement de translation sur l'axe $Oy$ (piston P) en un mouvement de rotation (point M). Le moteur tourne à vitesse angulaire $\omega$ constante : $\theta(t) = \omega t$. La longueur $L$ de la bielle PM est constante, $R$ est le rayon de la trajectoire de M. On étudie d'abord M en polaires, puis P en cartésiennes.
1. Sur le schéma, représenter la base polaire au point M.

Partie 1 : mouvement du point M en coordonnées polaires.
a. Donner l'expression de la dérivée de la position angulaire $\dot\theta(t)$.
b. Donner l'expression du vecteur position $\overrightarrow{OM}(t)$.
c. Calculer l'expression du vecteur vitesse $\vec v_M(t)$ en fonction du rayon $R$ et de la vitesse angulaire $\omega$.
d. Calculer l'expression du vecteur accélération $\vec a_M(t)$ en fonction de $R$ et $\omega$.

Partie 2 : mouvement du point P en coordonnées cartésiennes.
a. En utilisant les relations trigonométriques et le fait que le mouvement de P se fait sur l'axe $Oy$, montrer que le vecteur position de P est $\overrightarrow{OP} = (R\sin\theta + L\cos\theta)\,\vec u_y$ (expression telle qu'imprimée sur le sujet).
b. Établir l'expression du vecteur vitesse $\vec v_P(t)$ en fonction de $R$, $L$ et $\omega$.
c. Établir l'expression du vecteur accélération $\vec a_P(t)$ en fonction de $R$, $L$ et $\omega$.
