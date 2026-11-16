# Examen de physique S2 : mécanique — mars 2024 (sujet, FR)

- Source : `raw/S2/Midterms/Phys/2028/midterm-2028-s2-phys-subject-fr.pdf` (6 pages)
- Date réelle : mars 2024 (EPITA S2, dossier promo 2028), durée 1 h 30. Corrigé : `midterm-2028-s2-phys-correction-fr.md`.
- Calculatrices et documents non autorisés. Mécanique : cinématique, tir horizontal, pendule en coordonnées polaires.

## Exercice 1. Questions de cours (5 points, pas de points négatifs)
Type : QCM de cinématique (unité de force, position, vitesse, norme, intégration) · ECUE : Mécanique · Niveau : physique-s1-meca/2
Formules : $1\ \text{N} = 1\ \text{kg·m·s}^{-2}$ ; $\overrightarrow{OM} = x\,\vec u_x + y\,\vec u_y$ ; $\vec v = \dfrac{d\overrightarrow{OM}}{dt}$ ; $\|\vec v\| = \sqrt{v_x^2 + v_y^2}$ ; $\overrightarrow{OM}(t) = \overrightarrow{OM}(0) + \displaystyle\int_0^t\vec v\,dt$ ; $\vec a = \dfrac{d\vec v}{dt}$

Pour certaines questions il faut cocher plusieurs bonnes réponses.
1. L'unité d'une force est : a) le newton N ; b) le $\text{m·s}^{-2}$ ; c) le kg·m·s ; d) le $\text{kg·s}^{-2}$.

Pour les questions 2 à 4 : $x(t) = v_0\cos(\alpha)\,t$ et $y(t) = v_0\sin(\alpha)\,t - 5t^2$.

2. Le vecteur position peut s'écrire : a) $\overrightarrow{OM}(t) = v_0\cos(\alpha)\,t + v_0\sin(\alpha)\,t - 5t^2$ ; b) $\overrightarrow{OM}(t) = x(t) + y(t)$ ; c) $\overrightarrow{OM}(t) = x(t)\,\vec u_x + y(t)\,\vec u_y$ ; d) $\overrightarrow{OM}(t) = \begin{pmatrix} v_0\cos(\alpha)\,t \\ v_0\sin(\alpha)\,t - 5t^2 \end{pmatrix}$.
3. Le vecteur vitesse peut s'écrire : a) $\vec v(t) = v(t)\,\vec u_x + v(t)\,\vec u_y$ ; b) $\vec v(t) = v_0\cos(\alpha)\,\vec u_x + (v_0\sin(\alpha) - 10t)\,\vec u_y$ ; c) $\vec v(t) = v_0\sin(\alpha)\,\vec u_x + (v_0\cos(\alpha) - 10t)\,\vec u_y$ ; d) $\vec v(t) = v_0\sin(\alpha)\,\vec u_x - (v_0\cos(\alpha) - 10t)\,\vec u_y$.
4. La norme du vecteur vitesse vaut : a) $\sqrt{(v_0\cos\alpha)^2 + (v_0\sin\alpha - 10t)^2}$ ; b) $\sqrt{v_0\cos\alpha + (v_0\cos\alpha - 10t)}$ ; c) $\sqrt{v_0^2\cos^2\alpha + (v_0^2\cos^2\alpha - 100t^2)}$ ; d) $\sqrt{(v_0\cos\alpha)^2 + (v_0\cos\alpha + 10t)^2}$.
5. Un point M a pour vecteur vitesse $\vec v(t) = \begin{pmatrix} 5t \\ 4 \end{pmatrix}$, avec $\overrightarrow{OM}(0) = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$. Les expressions correctes sont : a) $\overrightarrow{OM}(t) = \begin{pmatrix} 5t^2/2 \\ 4t + 1 \end{pmatrix}$ ; b) $\overrightarrow{OM}(t) = \begin{pmatrix} 5 \\ 0 \end{pmatrix}$ ; c) $\vec a(t) = \begin{pmatrix} 5(t^2 + 1) \\ 4t \end{pmatrix}$ ; d) $\vec a(t) = \begin{pmatrix} 5 \\ 0 \end{pmatrix}$.

## Exercice 2. Tir au tennis (9 points)
Type : tir horizontal (PFD, équations horaires, trajectoire parabolique, passage d'un obstacle, portée) · ECUE : Mécanique · Niveau : physique-s1-meca/5
Formules : $m\vec a = \vec P \Rightarrow a_x = 0$, $a_y = -g$ ; $\vec v = (v_0,\ -gt)$ ; $x = v_0t$, $y = -\tfrac12gt^2 + H$ ; $y(x) = -\dfrac{gx^2}{2v_0^2} + H$ ; portée : $y = 0 \Rightarrow x = \sqrt{\dfrac{2v_0^2H}{g}}$

Un terrain de tennis est un rectangle de longueur $23{,}8$ m et de largeur $8{,}23$ m, séparé en deux par un filet de hauteur $0{,}920$ m. Au service, la balle doit tomber entre le filet et une ligne située à $6{,}40$ m du filet. Le joueur, placé en O, veut que la balle touche le sol en B tel que $OB = L = 18{,}7$ m. Il frappe la balle en un point D à la verticale de O, à la hauteur $H = 2{,}20$ m ; la balle part de D avec une vitesse horizontale $v_0 = 35{,}35\ \text{m·s}^{-1}$. La balle ($m = 58{,}0$ g) est ponctuelle ; après le service, seul le poids agit. $g = 10$ N/kg.
1. Donner le cadre d'étude (référentiel, système, système de coordonnées).
2. En appliquant le PFD, donner le vecteur accélération.
3. Donner le vecteur vitesse, en déterminant les constantes par les conditions initiales.
4. Donner le vecteur position, en déterminant les constantes par les conditions initiales.
5. Établir l'équation de la trajectoire $y(x)$. Comment se nomme ce type de trajectoire ?
6. Sachant que la distance au filet est $OF = 10$ m, la balle passe-t-elle au-dessus du filet ? On donne $35{,}35^2 \approx 1250$.
7. Montrer que le service sera mauvais, c'est-à-dire que la balle frappera le sol en un point B' tel que $OB' > OB$. On donne $23{,}4^2 \approx 550$.
8. En réalité, la balle tombe en B. Quel paramètre, non pris en compte ici, peut expliquer cette différence ?

## Exercice 3. Pendule en coordonnées polaires (7 points)
Type : pendule simple en coordonnées polaires (vitesse, accélération, PFD, petites oscillations, période) · ECUE : Mécanique · Niveau : physique-s1-meca/6
Formules : $\overrightarrow{OM} = r\,\vec u_r$ ; $\vec v = \dot r\,\vec u_r + r\dot\theta\,\vec u_\theta$ ; $\vec a = (\ddot r - r\dot\theta^2)\vec u_r + (2\dot r\dot\theta + r\ddot\theta)\vec u_\theta$ ; $r = l$ : $\vec a = -l\dot\theta^2\vec u_r + l\ddot\theta\vec u_\theta$ ; $\sin\theta \approx \theta$ : $\ddot\theta + \dfrac gl\theta = 0$ ; $T_p = 2\pi\sqrt{l/g}$

Une boule M de masse $m$, assimilable à un point, est accrochée par un fil de longueur $l$ en un point O d'une tige métallique. $\theta$ est l'angle entre la verticale et le fil ; on travaille dans la base polaire $(\vec u_r, \vec u_\theta)$, $\vec u_r$ dirigé de O vers M. La boule passe devant la tige sans la toucher.
1. Schématiser les forces qui s'exercent sur M.
2. Rappeler le vecteur position dans le cas général en coordonnées polaires.
3. En déduire l'expression générale du vecteur vitesse.
4. Vérifier que $\vec a(t) = (\ddot r - r\dot\theta^2)\vec u_r + (2\dot r\dot\theta + r\ddot\theta)\vec u_\theta$.
5. Le fil étant inextensible, réécrire le vecteur accélération du pendule.
6. Par le PFD, exprimer l'accélération en fonction de $m$, $g$, $l$, $T$ et $\theta$ ; projeter sur $\vec u_r$ et $\vec u_\theta$.
7. Avec l'approximation des petits angles ($\sin\theta \approx \theta$) et une des équations de la question 6, montrer que $\ddot\theta + \omega^2\theta = 0$. Préciser $\omega$.
8. (Bonus) La solution est $\theta(t) = \theta_{max}\cos(\omega t + \phi)$ avec $\omega = \dfrac{2\pi}{T_p}$. Donner $T_p$ en fonction de $g$ et $l$. Quelle longueur de fil choisir pour un pendule qui bat la seconde ($T_p = 2$ s) ? $g = 10\ \text{m·s}^{-2}$, $\pi^2 \approx 10$.
