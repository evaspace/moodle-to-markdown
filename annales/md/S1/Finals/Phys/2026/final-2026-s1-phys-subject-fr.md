# Partiel S1 — janvier 2022 (sujet, FR)

- Source : `raw/S1/Finals/Phys/2026/final-2026-s1-phys-subject-fr.pdf` (6 pages)
- Date réelle : janvier 2022 (EPITA InfoS1, dossier promo 2026). Pas de corrigé.
- Documents et calculatrices interdits. QCM sans points négatifs. Barème : 21 points (4 + 11 + 6). Rapport avec la mécanique : cinématique du point (repère orthonormé, polaires, Frenet, mouvement hélicoïdal, cercle à vitesse variable).

## Exercice 1. QCM (4 points)
Type : QCM de cinématique (vecteurs, polaires, Frenet, trajectoire) · ECUE : Mécanique · Niveau : physique-s1-meca/1
Formules : repère orthonormé : vecteurs de norme 1, deux à deux perpendiculaires ; $\overrightarrow{OM} = \rho\,\vec u_\rho$, $\vec v = \dot\rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta$, $\dot{\vec u}_\rho = \dot\theta\,\vec u_\theta$, $\dot{\vec u}_\theta = -\dot\theta\,\vec u_\rho$ ; Frenet : $\vec u_T \perp \vec u_N$, $\vec u_N$ vers l'intérieur de la concavité, $v = \dfrac{ds}{dt}$, $\vec a = \dot v\,\vec u_T + \dfrac{v^2}{R}\vec u_N$ ; mouvement hélicoïdal : coordonnées cylindriques

Q1. Trois vecteurs $\vec u_1$, $\vec u_2$, $\vec u_3$ forment un repère orthonormé si et seulement si : a) ils sont tous de norme égale à 1 et deux à deux perpendiculaires ; b) ils sont de norme égale à 1 et deux à deux parallèles ; c) ils appartiennent tous au même plan ; d) leur somme est un vecteur nul.
Q2. Mouvement en polaires $(\vec u_\rho, \vec u_\theta)$. Une seule assertion est fausse, laquelle ? a) $\overrightarrow{OM}(t) = \rho\,\vec u_\rho$ ; b) $\vec v(t) = \dot\rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta$ ; c) $\dot{\vec u}_\rho = \dot\theta\,\vec u_\theta$ ; d) $\dot{\vec u}_\theta = \dot\theta\,\vec u_\rho$.
Q3. Base de Frenet $(\vec u_T, \vec u_N)$ en un point M d'une trajectoire curviligne. Une seule affirmation est vraie, laquelle ? a) $\vec u_T$ est un vecteur normal à la trajectoire ; b) $\vec u_N$ est toujours dirigé vers l'intérieur de la concavité de la trajectoire ; c) $\vec u_T$ et $\vec u_N$ sont colinéaires ; d) le produit scalaire de $\vec u_T$ et $\vec u_N$ est égal au rayon de courbure.
Q4. Dans la base de Frenet, la norme du vecteur vitesse $v(t)$ est une primitive de l'abscisse curviligne $s(t)$. a) VRAI ; b) FAUX.
Q5. Dans la base de Frenet, l'abscisse curviligne $s(t)$ est une dérivée, par rapport au temps, du module de la vitesse $v(t)$. a) VRAI ; b) FAUX.
Q6. Dans la base de Frenet, un mobile d'abscisse curviligne $s(t)$ et de vitesse $v(t)$ a une accélération : a) $\vec a = \ddot s\,\vec u_T + \dfrac{v^2}{R}\vec u_N$ ; b) $\vec a = \ddot s\,\vec u_T + \dfrac{2v}{R^2}\vec u_N$ ; c) $\vec a = \dot v\,\vec u_T + \dfrac{R^2}{v}\vec u_N$.
Q7. Le mouvement d'une particule dans le plan $(xOy)$ a pour équations horaires $x(t) = V_0t\cos t$ et $y(t) = V_0t\sin t$ ($V_0$ constante). Au temps $t = \pi$ secondes, la particule se trouve : a) sur l'axe des Y ; b) sur l'axe des X ; c) à l'origine des axes ; d) nulle part.
Q8. Le système idéal pour étudier un mouvement hélicoïdal est le système des coordonnées : a) polaires ; b) cartésiennes ; c) sphériques ; d) cylindriques.

## Exercice 2. Coordonnées cartésiennes et base de Frenet (11 points)
Type : mouvement circulaire accéléré en cartésien (norme, Frenet, abscisse curviligne, tour complet) · ECUE : Mécanique · Niveau : physique-s1-meca/13
Formules : $x^2 + y^2 = R^2$ : cercle de centre $O$ et de rayon $R$ ; $\vec v = (\dot x, \dot y)$, $v = \sqrt{\dot x^2 + \dot y^2}$ ; $\vec v = v\,\vec u_T$ ; $s(t) = \int_0^t v\,dt$ ; un tour : $s = 2\pi R$ ; $a_T = \dfrac{dv}{dt}$, $a_N = \dfrac{v^2}{R}$, $a = \sqrt{a_T^2 + a_N^2}$ ; analyse dimensionnelle : $[\alpha t^2] = 1$ (un angle est sans dimension)

Un point matériel M a pour équations horaires $x(t) = R\cos(\alpha t^2)$ et $y(t) = R\sin(\alpha t^2)$, où $R$ et $\alpha$ sont des constantes strictement positives.
1. Montrer que M possède une trajectoire circulaire de centre O et de rayon R.
2. En coordonnées cartésiennes, écrire le vecteur position puis déterminer le vecteur vitesse en fonction de $\alpha$, $R$ et $t$.
3. En déduire que la norme du vecteur vitesse est $v(t) = 2\alpha Rt$. Le mouvement est-il uniforme ?
4. À l'aide d'une analyse dimensionnelle, donner l'unité de $\alpha$.
5. Le point M est initialement au point A (à $t = 0$). Représenter la base de Frenet au point A. Indiquer le sens du mouvement sur le cercle.
6. Déduire des questions précédentes le vecteur vitesse en base de Frenet.
7. Déterminer l'abscisse curviligne $s(t)$ en fonction de $\alpha$, $R$ et $t$.
8. Déterminer le temps $t_1$ nécessaire à M pour effectuer un tour complet, en fonction de $\alpha$.
9. a) Exprimer les composantes normale et tangentielle du vecteur accélération $\vec a(t)$ en base de Frenet. b) En déduire la norme de l'accélération de M en fonction de $\alpha$, $R$ et $t$.

## Exercice 3. Coordonnées polaires (6 points)
Type : cercle décrit en polaires (ρ, θ, position, vitesse) · ECUE : Mécanique · Niveau : physique-s1-meca/6
Formules : $\rho = \sqrt{x^2 + y^2}$ ; $\tan\theta = \dfrac yx$ ; $1 - \cos\varphi = 2\sin^2\dfrac\varphi2$ ; $\sin\varphi = 2\sin\dfrac\varphi2\cos\dfrac\varphi2$ ; $\dfrac{1 - \cos\varphi}{\sin\varphi} = \tan\dfrac\varphi2$ ; $\overrightarrow{OM} = \rho\,\vec u_\rho$ ; $\vec v = \dot\rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta$

Un point matériel M décrit, par rapport à un repère cartésien $(\vec u_x, \vec u_y)$, la trajectoire d'équations horaires $x(t) = b\sin(\omega t)$ et $y(t) = b\left[1 - \cos(\omega t)\right]$, avec $b$ constante strictement positive.
1. a) Donner l'expression de la coordonnée polaire radiale $\rho(t)$. b) Sachant que $1 - \cos(\omega t) = 2\sin^2\left(\dfrac{\omega t}2\right)$, trouver l'expression simplifiée de $\rho(t)$.
2. a) Donner l'expression de la coordonnée polaire angulaire $\theta(t)$. b) Sachant que $\dfrac{1 - \cos\omega t}{\sin\omega t} = \tan\left(\dfrac{\omega t}2\right)$, trouver l'expression simplifiée de $\theta(t)$.
3. a) Donner l'expression du vecteur position $\overrightarrow{OM}(t)$ en coordonnées polaires. b) En déduire l'expression en coordonnées polaires du vecteur vitesse $\vec v(t)$ de M.
