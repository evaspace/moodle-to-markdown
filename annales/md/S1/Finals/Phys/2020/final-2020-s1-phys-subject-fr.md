# Partiel n°1 S1 — janvier 2016 (sujet, FR)

- Source : `raw/S1/Finals/Phys/2020/final-2020-s1-phys-subject-fr.pdf` (6 pages)
- Date réelle : janvier 2016 (S1, dossier promo 2020). Pas de corrigé.
- Calculatrices et documents non autorisés. Réponses sur le sujet. Barème : 20 points (7 + 7 + 6). Rapport avec la mécanique : cinématique (Frenet, spirale, hélice) et statique (barre appuyée contre un mur, frottement).

## Exercice 1. Cinématique (7 points)
Type : Frenet (vitesse, accélération) et spirale logarithmique en polaires · ECUE : Mécanique · Niveau : physique-s1-meca/13
Formules : $dS = R\,d\theta$ ; $\vec V = \dfrac{dS}{dt}\vec u_T = R\dot\theta\,\vec u_T$ ; $\dfrac{d\vec u_T}{dt} = \dot\theta\,\vec u_N$ ; $a_T = \dfrac{dV}{dt}$, $a_N = \dfrac{V^2}{R}$ ; $\overrightarrow{OM} = \rho\,\vec u_\rho$ ; $\vec V = \dot\rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta$ ; $\vec a = (\ddot\rho - \rho\dot\theta^2)\vec u_\rho + (2\dot\rho\dot\theta + \rho\ddot\theta)\vec u_\theta$ ; $(e^{\omega t})' = \omega e^{\omega t}$

Partie A. On cherche à retrouver les expressions de la vitesse et de l'accélération dans la base de Frenet $(\vec u_T, \vec u_N)$. L'abscisse curviligne élémentaire est $dS = R\,d\theta$, où $R$ est le rayon de courbure en un point M quelconque de la trajectoire.
1. Exprimer le vecteur vitesse $\vec V$ dans la base de Frenet.
2. En déduire dans la base de Frenet les composantes $a_T$ et $a_N$ du vecteur accélération $\vec a$.

Partie B. Un objet supposé ponctuel décrit à vitesse angulaire constante $\omega$ la spirale d'équation, en coordonnées polaires, $\rho(t) = a\exp(\omega t)$, où $a$ et $\omega$ sont des constantes positives ; $\theta = \omega t$, avec $\dot\theta = \omega$.
1. Donner le vecteur position $\overrightarrow{OM}$ en coordonnées polaires.
2. Déterminer le vecteur vitesse de ce mouvement, sachant qu'en polaires $\vec V = \dot\rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta$.
3. En déduire le vecteur accélération $\vec a$, sachant qu'en polaires $\vec a = (\ddot\rho - \rho\dot\theta^2)\vec u_\rho + (2\dot\rho\dot\theta + \rho\ddot\theta)\vec u_\theta$.

## Exercice 2. Système en équilibre (7 points)
Type : barre contre un mur avec frottement au sol (bilan, moments, réaction, coefficient de frottement statique) · ECUE : Mécanique · Niveau : physique-s1-meca/12
Formules : équilibre : $\sum\vec F_{ext} = \vec 0$ et $\sum\mathcal M_B(\vec F_{ext}) = 0$ ; poids de la barre homogène en son milieu ; contact sans frottement : réaction normale à la paroi ; $R_{Bx} = f$ (frottement), $R_{By} = N$ ; $\|\vec R_B\| = \sqrt{R_{Bx}^2 + R_{By}^2}$ ; $\mu_s = \tan\varphi = \dfrac{R_{Bx}}{R_{By}}$ ; $\tan 30° = \dfrac1{\sqrt3}$

Une barre homogène AB de longueur $L$ est en équilibre : elle fait un angle $\alpha = 30°$ avec le mur vertical (A au mur, B au sol, O au pied du mur). Sa masse est $m = 10$ kg et $g = 10$ m·s$^{-2}$.
1. Faire le bilan des forces extérieures qui s'exercent sur la barre en équilibre. Représenter ces forces, sachant qu'il n'y a des frottements qu'au point de contact B. Commenter la direction de la réaction $\vec R_B$.
2. On suppose que la barre est susceptible de tourner autour d'un axe passant par B et perpendiculaire à la feuille. Utiliser la condition d'équilibre de rotation pour calculer la norme de la force exercée en A par le mur sur la barre. On donne $\tan 30° = \dfrac1{\sqrt3}$.
3. a) Utiliser la condition d'équilibre de translation pour exprimer les composantes $R_{Bx}$ et $R_{By}$ de la réaction $\vec R_B$. Faire le calcul numérique. b) Calculer la norme de la réaction $\vec R_B$. c) En déduire la valeur du coefficient de frottement statique $\mu_s$ au point B.

## Exercice 3. Cinématique (6 points)
Type : hélice circulaire (cartésiennes puis cylindriques : vitesse, accélération, nature du mouvement) · ECUE : Mécanique · Niveau : physique-s1-meca/8
Formules : $\vec V = (\dot x, \dot y, \dot z)$, $\vec a = (\ddot x, \ddot y, \ddot z)$ ; $\rho = \sqrt{x^2 + y^2}$, $\theta = \arctan(y/x)$ ; $\overrightarrow{OM} = \rho\,\vec u_\rho + z\,\vec u_z$ ; $\vec V = \dot\rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta + \dot z\,\vec u_z$ ; $\vec a = (\ddot\rho - \rho\dot\theta^2)\vec u_\rho + (2\dot\rho\dot\theta + \rho\ddot\theta)\vec u_\theta + \ddot z\,\vec u_z$ ; la norme ne dépend pas de la base orthonormée

Un point matériel M de masse $m$ est repéré dans un référentiel fixe $(Oxyz)$ par ses coordonnées cartésiennes $x(t) = R\cos(\omega t)$, $y(t) = R\sin(\omega t)$, $z(t) = H\omega t$, où $\omega$, $R$ et $H$ sont des constantes positives.
1. Donner l'équation et la nature de la trajectoire dans le plan $(xOy)$. Préciser la nature du mouvement sur l'axe $(Oz)$. En déduire la nature du mouvement total.
2. Exprimer le vecteur position $\overrightarrow{OM}$ en coordonnées cylindriques de base $(\vec u_\rho, \vec u_\theta, \vec u_z)$.
3. Exprimer le vecteur vitesse en coordonnées cylindriques, en déduire sa norme.
4. Exprimer le vecteur accélération en coordonnées cylindriques. En déduire sa norme.
