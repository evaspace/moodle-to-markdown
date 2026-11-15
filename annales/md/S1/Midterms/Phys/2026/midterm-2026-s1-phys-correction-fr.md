# Contrôle S1 — novembre 2021 (corrigé, FR)

- Source : `raw/S1/Midterms/Phys/2026/midterm-2026-s1-phys-correction-fr.pdf` (6 pages, corrigé manuscrit scanné avec barème)
- Date réelle : novembre 2021 (EPITA InfoS1, dossier promo 2026). Sujet : `midterm-2026-s1-phys-subject-fr.md`.
- Calculatrices et documents non autorisés. Barème indicatif : 20 points. Rapport avec la mécanique : cinématique du point (base polaire, projectile, accélération polaire). Les lignes `> ` sont les solutions du corrigé.

## Exercice 1. Questions de cours (2,5 points, pas de points négatifs)
Type : QCM de cinématique (vecteurs, polaires, Frenet, trajectoire) · ECUE : Mécanique · Niveau : physique-s1-meca/2
Formules : mouvement uniforme : $\|\vec V\| = \text{cste}$ ; $\overrightarrow{OM} = \rho\,\vec u_\rho$ en polaires ; $\vec a = \dfrac{d^2\overrightarrow{OM}}{dt^2}$ ; $\vec u \perp \vec v \iff \vec u \cdot \vec v = 0$ ; $x(t) = 10 - 2t^2 \Rightarrow v = -4t$, $a = -4$

Choisissez la bonne réponse.
1. Un mouvement est dit uniforme si : a) sa trajectoire est une ligne droite ; b) son accélération est constante au cours du temps ; c) sa vitesse est constante au cours du temps ; d) sa vitesse et son accélération varient très peu avec le temps.
> Le corrigé entoure d). Attention : la définition du cours est c) (norme de la vitesse constante).
2. En coordonnées polaires $(\vec u_\rho, \vec u_\theta)$, le vecteur position est : a) $\rho\,\vec u_\rho + \theta\,\vec u_\theta$ ; b) $\rho\,\vec u_\rho$ ; c) $\theta\,\vec u_\rho + \rho\,\vec u_\theta$ ; d) $\rho\,\vec u_\theta$.
> Réponse b).
3. Un mobile décrit un trajet rectiligne le long de l'axe $(Ox)$, d'équation horaire $x(t) = 10 - 2t^2$ : a) le mouvement est uniforme ; b) le mouvement est uniformément circulaire ; c) le mouvement est décéléré ; d) la norme de l'accélération est de $2\ \text{m/s}^2$.
> Aucune réponse entourée dans le corrigé. Avec $x = 10 - 2t^2$ : $v = -4t$, $a = -4\ \text{m/s}^2$, donc $a = 4\ \text{m/s}^2$ en norme (d) est fausse) ; le mouvement est accéléré pour $t > 0$ et décéléré pour $t < 0$.
4. L'accélération d'un mobile de vecteur position $\vec r(t)$ est : a) $\dfrac{\partial\vec r}{\partial t^2}$ ; b) $\dfrac{\partial^2\vec r}{\partial t^2}$ ; c) $\left[\dfrac{\partial\vec r}{\partial t}\right]^2$ ; d) $\sqrt{r(t)}$.
> Réponse b) : la dérivée seconde de la position.
5. Deux vecteurs sont orthogonaux si leur produit scalaire est nul. a) VRAI ; b) FAUX.
> Réponse a).

## Exercice 2. Coordonnées cartésiennes et polaires (8 points)
Type : base polaire (vecteurs unitaires, dérivées, position, vitesse) · ECUE : Mécanique · Niveau : physique-s1-meca/6
Formules : $\vec u_\rho = \cos\theta\,\vec u_x + \sin\theta\,\vec u_y$ ; $\vec u_\theta = -\sin\theta\,\vec u_x + \cos\theta\,\vec u_y$ ; $\dfrac{d\vec u_\rho}{d\theta} = \vec u_\theta$, $\dfrac{d\vec u_\theta}{d\theta} = -\vec u_\rho$ ; $\dfrac{d\vec u}{dt} = \dot\theta\dfrac{d\vec u}{d\theta}$ ; $\overrightarrow{OM} = \rho\,\vec u_\rho$ ; $\vec V = \dfrac{d\overrightarrow{OM}}{dt} = \dot\rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta$

Un schéma représente, sur le même plan, les coordonnées polaires et cartésiennes.
1. Exprimer les vecteurs unitaires $\vec u_\rho$ et $\vec u_\theta$ de la base polaire en fonction de $\theta$ et de $\vec u_x$, $\vec u_y$.
> $\vec u_\rho = \cos\theta\,\vec u_x + \sin\theta\,\vec u_y$ et $\vec u_\theta = -\sin\theta\,\vec u_x + \cos\theta\,\vec u_y$.
2. a) Calculer $\dfrac{d\vec u_\rho}{d\theta}$. b) L'exprimer en fonction de $\vec u_\theta$.
> a) $\dfrac{d\vec u_\rho}{d\theta} = -\sin\theta\,\vec u_x + \cos\theta\,\vec u_y$. b) $= \vec u_\theta$.
3. a) Calculer $\dfrac{d\vec u_\theta}{d\theta}$. b) L'exprimer en fonction de $\vec u_\rho$.
> a) $\dfrac{d\vec u_\theta}{d\theta} = -\cos\theta\,\vec u_x - \sin\theta\,\vec u_y$. b) $= -\vec u_\rho$.
4. Le point M représente la position d'un mobile au cours du temps. Exprimer le vecteur position $\overrightarrow{OM}(t)$ dans la base cartésienne ainsi que dans la base polaire.
> $\overrightarrow{OM} = x\,\vec u_x + y\,\vec u_y$ avec $x = \rho\cos\theta$, $y = \rho\sin\theta$ ; $\overrightarrow{OM} = \rho\,\vec u_\rho$.
5. Écrire l'expression générale du vecteur vitesse instantanée et donner son expression dans la base polaire en expliquant chaque étape du calcul.
> $\vec V = \dfrac{d\overrightarrow{OM}}{dt} = \dfrac{d(\rho\,\vec u_\rho)}{dt} = \dot\rho\,\vec u_\rho + \rho\,\dfrac{d\vec u_\rho}{dt}$, et $\dfrac{d\vec u_\rho}{dt} = \dfrac{d\theta}{dt}\dfrac{d\vec u_\rho}{d\theta} = \dot\theta\,\vec u_\theta$, donc $\vec V = \dot\rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta$.

## Exercice 3. Mouvement d'un projectile (5,5 points)
Type : projectile (équations horaires, trajectoire, vitesse, flèche) · ECUE : Mécanique · Niveau : physique-s1-meca/5
Formules : $x = v_0\cos\alpha\,t$, $y = v_0\sin\alpha\,t - \tfrac12gt^2$ avec $g = 10\ \text{m/s}^2$ ; $y(x) = -\dfrac{g}{2v_0^2\cos^2\alpha}x^2 + \tan\alpha\,x$ ; $V = \sqrt{V_x^2 + V_y^2}$ ; sommet : $V_y = 0$, $y_{\max} = \dfrac{v_0^2\sin^2\alpha}{2g}$

Un projectile est lancé du point $(0;0)$ à $t = 0$ s en faisant un angle $\alpha$ avec l'horizontale ; il passe par le sommet S de la trajectoire. Le vecteur position vaut $\overrightarrow{OM} = (v_0\cos\alpha)\,t\,\vec u_x + \left[(v_0\sin\alpha)\,t - 5t^2\right]\vec u_y$.
1. a) Donner les équations horaires $x(t)$ et $y(t)$. b) Donner l'équation de la trajectoire de M $(x, y)$.
> a) $x(t) = v_0\cos\alpha\,t$ et $y(t) = v_0\sin\alpha\,t - 5t^2$. b) $t = \dfrac{x}{v_0\cos\alpha}$, d'où $y(x) = -\dfrac{5}{v_0^2\cos^2\alpha}x^2 + \tan\alpha\,x$.
2. Exprimer le vecteur vitesse instantanée $\vec v(t)$. Exprimer sa norme.
> $\vec v = v_0\cos\alpha\,\vec u_x + (v_0\sin\alpha - 10t)\,\vec u_y$ ; $v = \sqrt{v_0^2\cos^2\alpha + (v_0\sin\alpha - 10t)^2}$.
3. Au sommet de la trajectoire, $V_y$ est nulle. Calculer la hauteur maximale atteinte par le projectile en fonction de $V_0$ et de l'angle $\alpha$.
> $V_y = 0 \Rightarrow t = \dfrac{v_0\sin\alpha}{10}$ ; $y_{\max} = -5\dfrac{v_0^2\sin^2\alpha}{100} + \dfrac{v_0^2\sin^2\alpha}{10} = \dfrac{v_0^2\sin^2\alpha}{20}$.

## Exercice 4. Accélération en coordonnées polaires (4 points)
Type : accélération polaire (mouvement circulaire, circulaire uniforme) · ECUE : Mécanique · Niveau : physique-s1-meca/6
Formules : $\vec a = (\ddot\rho - \rho\dot\theta^2)\vec u_\rho + (\rho\ddot\theta + 2\dot\rho\dot\theta)\vec u_\theta$ ; cercle : $\rho = R$, $\dot\rho = \ddot\rho = 0$ ; uniforme : $\dot\theta = \omega = \text{cste}$, $\ddot\theta = 0$

Pour un mouvement quelconque, $\vec a(t) = (\ddot\rho - \rho\dot\theta^2)\vec u_\rho + (\rho\ddot\theta + 2\dot\rho\dot\theta)\vec u_\theta$.
1. Quelle est l'expression de l'accélération si le mouvement est circulaire ? Justifier.
> $\rho = R$ constant, donc $\dot\rho = \ddot\rho = 0$ : $\vec a = -R\dot\theta^2\,\vec u_\rho + R\ddot\theta\,\vec u_\theta$.
2. Quelle est l'expression de l'accélération si le mouvement est, en plus, uniforme ? Justifier.
> $\dot\theta = \omega$ constante, donc $\ddot\theta = 0$ : $\vec a = -R\omega^2\,\vec u_\rho$, accélération centripète.
