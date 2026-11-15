# Contrôle 1 S1 — novembre 2017 (sujet, FR)

- Source : `raw/S1/Midterms/Phys/2022/midterm-2022-s1-phys-subject-fr.pdf` (6 pages)
- Date réelle : novembre 2017 (S1 2017, dossier promo 2022). Pas de corrigé.
- Calculatrices et documents non autorisés. Réponses sur le sujet. Barème : 20 points. Rapport avec la mécanique : cinématique du point (vecteurs, polaires, Frenet), tout le chapitre « mécanique du point » de S1.

## QCM (4 points)
Type : QCM de cinématique (vecteurs, polaires, Frenet, trajectoire) · ECUE : Mécanique · Niveau : physique-s1-meca/1
Formules : $\vec R = \vec F_1 + \vec F_2$ ; $\vec V_1 \cdot \vec V_2 = V_1V_2\cos\alpha$ ; $\|\vec V_1 + \vec V_2\|^2 = V_1^2 + V_2^2 + 2V_1V_2\cos\alpha$ ; $\vec V = \dot\rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta$ ; $ds = R\,d\theta$, $s(t) = \int_0^t v\,dt$ ; trajectoire : éliminer $t$ avec $\cos^2 + \sin^2 = 1$

Entourer la bonne réponse.
1. La norme de la résultante $\vec R$ de deux forces $\vec F_1$ et $\vec F_2$ (non nulles), colinéaires et de sens opposé est : a) $R = 0$ ; b) $R = \sqrt{F_1^2 + F_2^2}$ ; c) $R = F_1 + F_2$ ; d) $R = |F_1 - F_2|$.
2. Les composantes de $\vec F_1$ (angle $\alpha$ avec l'axe $x$, dans le premier quadrant) sont : a) $(F_1, 0)$ ; b) $(F_1\sin\alpha,\ F_1\cos\alpha)$ ; c) $(F_1\cos\alpha,\ F_1\sin\alpha)$.
3. Le produit scalaire de deux vecteurs colinéaires et de sens opposé est : a) strictement positif ; b) nul ; c) strictement négatif.
4. La norme de $\vec V_3 = \vec V_1 \wedge \vec V_2$, avec $(\vec V_1, \vec V_2) = \alpha$, est : a) $V_3 = V_1V_2|\sin\alpha|$ ; b) $V_3 = V_1V_2\cos\alpha$ ; c) $V_3 = \sqrt{V_1^2 + V_2^2 + 2V_1V_2\cos\alpha}$.
5. Le vecteur vitesse en coordonnées polaires s'écrit : a) $\vec V = \dot\rho\,\vec u_\rho + \dot\theta\,\vec u_\theta$ ; b) $\vec V = \dot\rho\,\vec u_\rho + \rho\,\vec u_\theta$ ; c) $\vec V = \dot\rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta$.
6. Dans la base de Frenet, l'abscisse curviligne élémentaire $ds$ s'écrit : a) $ds = R\dot\theta$ ; b) $ds = dV\,dt$ ; c) $ds = R\,d\theta$.
7. L'expression de l'abscisse curviligne $s(t)$ est : a) $\int_0^t a_T\,dt$ ; b) $\int_0^t v\,dt$ ; c) $\int_0^t a_N\,dt$.
8. L'équation de la trajectoire d'équations horaires $x(t) = A\sin(\omega t)$, $y(t) = B\cos(\omega t)$ ($A, B, \omega$ constantes positives, $A \neq B$) est : a) $x^2 + y^2 = 1$ ; b) $x^2 + y^2 = A^2 + B^2$ ; c) $\dfrac{x^2}{A^2} + \dfrac{y^2}{B^2} = 1$.

## Exercice 1 (4 points)
Type : mouvement circulaire en cartésien (vitesse, accélération, trajectoire) · ECUE : Mécanique · Niveau : physique-s1-meca/7
Formules : $\vec V = (\dot x, \dot y)$, $\vec a = (\ddot x, \ddot y)$ ; $\|\vec V\| = \sqrt{\dot x^2 + \dot y^2}$ ; $\sin^2 + \cos^2 = 1$ ; cercle de centre $(x_0, y_0)$ et de rayon $R$ : $(x - x_0)^2 + (y - y_0)^2 = R^2$

Les équations horaires d'un mouvement en coordonnées cartésiennes sont $x(t) = 1 + R\sin(\omega t)$ et $y(t) = 2 + R\cos(\omega t)$, où $\omega$ et $R$ sont des constantes.
1. Exprimer les composantes du vecteur vitesse $\vec V$ en fonction du temps. Calculer sa norme.
2. Exprimer les composantes du vecteur accélération $\vec a$ en fonction du temps. Calculer sa norme.
3. Retrouver l'équation de la trajectoire $y = f(x)$. Préciser sa nature et ses caractéristiques.

## Exercice 2 (6 points)
Type : spirale logarithmique en polaires (vitesse, accélération, Frenet) · ECUE : Mécanique · Niveau : physique-s1-meca/6
Formules : $\rho = \sqrt{x^2 + y^2}$, $\tan\theta = y/x$ ; $\vec V = \dot\rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta$ ; $\vec a = (\ddot\rho - \rho\dot\theta^2)\vec u_\rho + (2\dot\rho\dot\theta + \rho\ddot\theta)\vec u_\theta$ ; $a_T = \dfrac{dv}{dt}$, $a_N = \dfrac{v^2}{R_c}$, $a^2 = a_T^2 + a_N^2$ ; $R_c = \dfrac{v^2}{a_N}$

Les composantes du vecteur position $\overrightarrow{OM}$ en coordonnées cartésiennes sont $x(t) = a\,e^{\omega t}\cos(\omega t)$ et $y(t) = a\,e^{\omega t}\sin(\omega t)$, où $a$ et $\omega$ sont des constantes positives.
1. Écrire le vecteur position $\overrightarrow{OM}$ en coordonnées polaires de base $(\vec u_\rho, \vec u_\theta)$.
2. Exprimer en coordonnées polaires le vecteur vitesse $\vec V$. Calculer la norme de $\vec V$. On donne $\dot\theta = \omega$.
3. Exprimer en coordonnées polaires le vecteur accélération $\vec a$. Calculer la norme de $\vec a$.
4. Exprimer les composantes $a_T$ et $a_N$ du vecteur accélération dans la base de Frenet. En déduire le rayon de courbure $R_c$.

## Exercice 3 (6 points)
Type : base de Frenet (démonstration, abscisse curviligne, rayon de courbure) · ECUE : Mécanique · Niveau : physique-s1-meca/13
Formules : $\vec V = v\,\vec u_T = R\dot\theta\,\vec u_T$ ; $\vec a = \dfrac{dv}{dt}\vec u_T + \dfrac{v^2}{R_c}\vec u_N$ ; $\dfrac{d\vec u_T}{dt} = \dot\theta\,\vec u_N$ ; $s(t) = \int_0^t v\,dt$, $v(t) = v(t_0) + \int a_T\,dt$ ; $R_c = \dfrac{v^2}{a_N}$ ; unité de $\alpha$ = (m·s$^{-2}$)/(unité du facteur de $\vec u_T$)

Les parties I et II sont indépendantes.

I-1) Montrer que la vitesse en base de Frenet s'écrit $\vec V = R(t)\,\dot\theta\,\vec u_T$.

I-2) En déduire l'écriture du vecteur accélération $\vec a$ dans la base de Frenet.

II- Un point matériel M se déplace dans un plan avec l'accélération, donnée en fonction du temps dans la base de Frenet, $\vec a = \alpha\,\vec u_T + \beta t^2\,\vec u_N$ ($\alpha$ et $\beta$ constantes positives).
1) Déterminer les unités des constantes $\alpha$ et $\beta$. Justifier votre réponse.
2) Calculer l'abscisse curviligne $s(t)$ entre les instants $t_0 = 0$ et $t$. On donne $v(t_0) = 0$ et $s(t_0) = 0$.
3) Montrer que le rayon de courbure de la trajectoire est donné par $R_c = \dfrac{\alpha^2}{\beta}$.
