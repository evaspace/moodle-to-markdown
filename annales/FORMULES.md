# Fiche synthèse des formules (maths et physique)

Toutes les formules utilisées pour résoudre les exercices des annales, par ECUE puis par type d'exercice.
Entre parenthèses : nombre d'exercices d'annales de ce type. Généré par `tools/index.py` depuis `tools/formules.py` : ne pas modifier à la main.

## Mécanique

**QCM de cinématique (vecteurs, polaires, Frenet, trajectoire)** (12)

- $\vec V_1 \cdot \vec V_2 = V_1V_2\cos\alpha$, négatif si les vecteurs sont de sens opposés
- $\|\vec V_1 \wedge \vec V_2\| = V_1V_2|\sin\alpha|$
- $(\cos^2\theta)' = -2\dot\theta\cos\theta\sin\theta$
- $\vec V = \dot\rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta + \dot z\,\vec u_z$
- $\vec a = (\ddot\rho - \rho\dot\theta^2)\vec u_\rho + (2\dot\rho\dot\theta + \rho\ddot\theta)\vec u_\theta$
- $\dfrac{d\vec u_\rho}{dt} = \dot\theta\,\vec u_\theta$
- $x = \rho\cos\theta$, $y = \rho\sin\theta$

**équilibre d'une poutre articulée (câble, charge, réaction du mur)** (7)

- équilibre : $\sum\vec F_{ext} = \vec 0$ et $\sum\mathcal M_O(\vec F_{ext}) = 0$
- $\mathcal M_O(\vec F) = \pm F\,d$ avec $d$ = bras de levier
- poids de la poutre en son milieu
- projection sur $Ox$ et $Oy$

**QCM de statique et d'énergie (moments, travail, théorèmes énergétiques)** (7)

- moment d'une force par rapport à un axe : $\mathcal M = \pm F\,d$ (bras de levier $d$), signe selon le sens de rotation
- moment nul si la droite d'action coupe l'axe
- $W_{AB}(\vec f) = \int_A^B \vec f\cdot d\vec l = \int_A^B f\,dl\cos\alpha$
- $\Delta E_c = \sum W(\vec F_{ext})$
- $\Delta E_m = W(\vec f_{frott})$
- force perpendiculaire au déplacement : $W = 0$
- $W_{A\to B}(\vec P) = mgR(1 - \cos\theta)$ pour une descente de hauteur $R(1 - \cos\theta)$

**mouvement elliptique en cartésien (trajectoire, vitesse, accélération, $\vec a = -\omega^2\overrightarrow{OM}$)** (6)

- $\vec V = (\dot x, \dot y)$, $\vec a = (\ddot x, \ddot y)$
- $\|\vec V\| = \sqrt{\dot x^2 + \dot y^2}$
- $\cos^2 + \sin^2 = 1$
- ellipse : $\dfrac{x^2}{A^2} + \dfrac{y^2}{B^2} = 1$
- $\ddot x = -\omega^2 x$, $\ddot y = -\omega^2 y$

**hélice circulaire (cartésiennes puis cylindriques : vitesse, accélération, nature du mouvement)** (5)

- $\vec V = (\dot x, \dot y, \dot z)$, $\vec a = (\ddot x, \ddot y, \ddot z)$
- $\rho = \sqrt{x^2 + y^2}$, $\theta = \arctan(y/x)$
- $\overrightarrow{OM} = \rho\,\vec u_\rho + z\,\vec u_z$
- $\vec V = \dot\rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta + \dot z\,\vec u_z$
- $\vec a = (\ddot\rho - \rho\dot\theta^2)\vec u_\rho + (2\dot\rho\dot\theta + \rho\ddot\theta)\vec u_\theta + \ddot z\,\vec u_z$
- la norme ne dépend pas de la base orthonormée

**mouvement circulaire à vitesse variable (abscisse curviligne, tour complet, composantes de Frenet)** (4)

- $s(t) = \int_0^t v\,dt$
- $\int \dfrac{dt}{1 + \alpha t} = \dfrac1\alpha\ln(1 + \alpha t)$
- $a_T = \dfrac{dv}{dt}$, $a_N = \dfrac{v^2}{R}$, $a = \sqrt{a_T^2 + a_N^2}$

**bille sur une sphère (Newton en base de Frenet, équation du mouvement, réaction)** (2)

- $\vec a = \dfrac{dv}{dt}\vec u_T + \dfrac{v^2}{r}\vec u_N$ avec $v = r\dot\theta$ : $a_T = r\ddot\theta$, $a_N = r\dot\theta^2$
- $\vec P + \vec R = m\vec a$
- poids : $P\sin\theta$ selon $\vec u_T$, $P\cos\theta$ selon $-\vec u_N$
- $\ddot\theta = \dfrac gr\sin\theta$
- $\dot\theta^2 = \dfrac{2g}r(1 - \cos\theta)$
- $R = mg(3\cos\theta - 2)$

**glissement avec frottement sur un guide hémicylindrique (énergie cinétique, énergie potentielle, énergie mécanique, travail de frottement)** (2)

- $\Delta E_c = \tfrac12m(v_B^2 - v_A^2)$
- $\Delta E_p = mg(z_B - z_A)$
- $\Delta E_m = \Delta E_c + \Delta E_p = W(\vec f)$
- $W_{AB}(\vec f) = -f\cdot\widehat{AB}$ (force de norme constante opposée au déplacement)
- $\widehat{AB} = R\dfrac\pi2$ (quart de cercle)

**boucle (looping) : énergie mécanique, vitesse, réaction normale** (2)

- sans frottement : $E_m = \text{cste}$, $\tfrac12mv_A^2 + mgz_A = \tfrac12mv^2 + mgz$
- hauteur de M sur la boucle : $z_M = R + R\sin\theta$
- Newton en Frenet : $\vec P + \vec R_N = m\vec a$, $a_N = \dfrac{v^2}{R}$ vers le centre
- $R_N = \dfrac{mv_M^2}{R} - mg\sin\theta$

**plan incliné et poulie (Newton sur deux masses, accélération, tension, réaction)** (2)

- $\sum\vec F_{ext} = m\vec a$ pour chaque masse
- fil inextensible de masse négligeable : même accélération, même tension
- sur le plan incliné : $-m_1g\sin\alpha + T = m_1a$
- masse suspendue : $mg - T = ma$
- $a = g\dfrac{m - m_1\sin\alpha}{m_1 + m}$
- réaction normale : $R = m_1g\cos\alpha$

**solide sur une gouttière en quart de cercle (Newton en base de Frenet, réaction, décollement)** (2)

- $\vec a = \dfrac{dv}{dt}\vec u_T + \dfrac{v^2}{r}\vec u_N$
- $\vec P + \vec R = m\vec a$
- $a_T = g\sin\theta$
- $mg\cos\theta - R = m\dfrac{V^2}{r}$
- $V^2 = 2gr(1 - \cos\theta)$
- $R = mg(3\cos\theta - 2)$
- décollement : $R = 0 \iff \cos\theta = \dfrac23$

**cycloïde (vitesse, accélération, normes, tracé)** (2)

- $\vec V = (\dot x, \dot y)$, $\vec a = (\ddot x, \ddot y)$
- $\|\vec V\| = \sqrt{\dot x^2 + \dot y^2}$
- $1 - \cos\alpha = 2\sin^2(\alpha/2)$
- $\omega = 2\pi/T$
- tracé : tableau de valeurs de $(x(t), y(t))$ en $t = 0, T/4, T/2, 3T/4, T$

**mouvement rectiligne oscillant en cartésien (trajectoire, tracé, vitesse)** (2)

- $\cos 2\varphi = 1 - 2\sin^2\varphi$
- $0 \leqslant \sin^2 \leqslant 1$ borne le segment parcouru
- $\dot x = 2\omega\sin\omega t\cos\omega t = \omega\sin 2\omega t$
- $\dot y = -2\omega\sin 2\omega t$
- $V = \sqrt{\dot x^2 + \dot y^2}$

**hélice en cylindriques et Frenet (vitesse, abscisse curviligne, accélération, rayon de courbure)** (2)

- $\overrightarrow{OM} = R\,\vec u_\rho + Kt\,\vec u_z$, $\theta = \omega t$
- $\vec V = R\dot\theta\,\vec u_\theta + K\vec u_z$, $\dfrac{d\vec u_\rho}{dt} = \dot\theta\,\vec u_\theta$, $\dfrac{d\vec u_\theta}{dt} = -\dot\theta\,\vec u_\rho$
- $V = \sqrt{R^2\omega^2 + K^2}$ constante
- $s(t) = \int_0^t V\,dt$
- $a_T = \dfrac{dV}{dt} = 0$, $a_N = \dfrac{V^2}{R_c}$
- la norme de $\vec a$ ne dépend pas de la base
- $R_c = \dfrac{V^2}{a}$

**base polaire (vecteurs unitaires, dérivées, position, vitesse)** (2)

- $\vec u_\rho = \cos\theta\,\vec u_x + \sin\theta\,\vec u_y$
- $\vec u_\theta = -\sin\theta\,\vec u_x + \cos\theta\,\vec u_y$
- $\dfrac{d\vec u_\rho}{d\theta} = \vec u_\theta$, $\dfrac{d\vec u_\theta}{d\theta} = -\vec u_\rho$
- $\dfrac{d\vec u}{dt} = \dot\theta\dfrac{d\vec u}{d\theta}$
- $\overrightarrow{OM} = \rho\,\vec u_\rho$
- $\vec V = \dfrac{d\overrightarrow{OM}}{dt} = \dot\rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta$

**projectile (équations horaires, trajectoire, vitesse, flèche)** (2)

- $x = v_0\cos\alpha\,t$, $y = v_0\sin\alpha\,t - \tfrac12gt^2$ avec $g = 10\ \text{m/s}^2$
- $y(x) = -\dfrac{g}{2v_0^2\cos^2\alpha}x^2 + \tan\alpha\,x$
- $V = \sqrt{V_x^2 + V_y^2}$
- sommet : $V_y = 0$, $y_{\max} = \dfrac{v_0^2\sin^2\alpha}{2g}$

**accélération polaire (mouvement circulaire, circulaire uniforme)** (2)

- $\vec a = (\ddot\rho - \rho\dot\theta^2)\vec u_\rho + (\rho\ddot\theta + 2\dot\rho\dot\theta)\vec u_\theta$
- cercle : $\rho = R$, $\dot\rho = \ddot\rho = 0$
- uniforme : $\dot\theta = \omega = \text{cste}$, $\ddot\theta = 0$

**QCM de mécanique (travail, lois de Newton, théorème de l'énergie cinétique, énergie mécanique)** (2)

- $W = \vec F \cdot \overrightarrow{AB} = F\,AB\cos\alpha$
- première loi de Newton (inertie)
- $\|\vec F\| = ma$, $\|\vec F\| = \sqrt{F_x^2 + F_y^2 + F_z^2}$
- $\Delta E_c = \sum W(\vec F_{ext})$
- $E_m = E_c + E_p$, conservée seulement sans force non conservative

**deuxième loi de Newton, masses reliées par une poulie (tensions, accélération)** (2)

- $\sum\vec F_{ext} = m\vec a$ pour chaque masse
- fil et poulie de masses négligeables : même tension de part et d'autre
- fil inextensible : même norme d'accélération
- $P = mg$

**conservation de l'énergie mécanique sur une piste (vitesse en un point, condition d'arrêt)** (2)

- $E_c = \tfrac12mv^2$
- $E_p = mgz$
- $E_m = E_c + E_p$
- sans frottement : $\Delta E_m = 0$
- $v_B = \sqrt{2g(h - d)}$

**théorème de l'énergie cinétique avec frottement (palet qui s'arrête)** (2)

- $W(\vec P) = 0$ et $W(\vec R_N) = 0$ sur un déplacement horizontal
- $W(\vec f) = -f\,x$
- $\Delta E_c = \sum W$
- $f = \dfrac{mv_A^2}{2x}$

**glissière inclinée puis circulaire (théorème de l'énergie cinétique, énergie mécanique, réaction en Frenet, énergie minimale)** (2)

- $\Delta E_c = \sum W$
- $W(\vec P) = mgh$ en descente, $W(\vec R_N) = 0$ sans frottement
- $E_m = \tfrac12mv^2 + mgz$ conservée
- Frenet : $m\dfrac{v^2}{R} = \sum F_N$
- $z = R\cos\alpha + R\cos\beta$ au-dessus du point bas de la pente

**oscillation amortie sur un demi-cercle (Newton en Frenet, réaction, petites oscillations, régimes)** (2)

- $\sum\vec F_{ext} = m\vec a$
- Frenet : $a_T = \dfrac{dv}{dt}$, $a_N = \dfrac{v^2}{R}$
- $v = R\dot\theta$
- $\sin\theta \approx \theta$
- $r^2 + \dfrac\alpha m r + \dfrac gR = 0$, $\Delta = \left(\dfrac\alpha m\right)^2 - \dfrac{4g}R$
- $\Delta > 0$ apériodique, $\Delta = 0$ critique, $\Delta < 0$ pseudopériodique

**QCM d'oscillateurs et de thermique (énergie du pendule, régime critique, système isolé, résistances thermiques, mélange)** (2)

- $E_m = \tfrac12mL^2\dot\theta^2 + mgL(1 - \cos\theta)$, $\dfrac{dE_m}{dt} = 0 \Rightarrow \ddot\theta + \dfrac gL\sin\theta = 0$
- critique : $\alpha = 2m\omega_0$
- isolé : ni matière ni énergie échangée
- $R_{th} = \dfrac{e}{\lambda_{th}S}$, en série $R = \sum R_i$
- mélange d'eau : $\theta_e = \dfrac{V_1\theta_1 + V_2\theta_2}{V_1 + V_2}$
- intensive : température, pression

**oscillateur ressort horizontal amorti (forces, équation différentielle, régimes, allure de x(t))** (2)

- $\sum\vec F_{ext} = m\vec a$
- rappel $-kx\,\vec u_x$, frottement $-\alpha\vec v$
- $\ddot x + \dfrac\alpha m\dot x + \dfrac kmx = 0$
- $\omega_0^2 = \dfrac km$
- $r^2 + \dfrac\alpha mr + \omega_0^2 = 0$, $\Delta = \left(\dfrac\alpha m\right)^2 - 4\omega_0^2$
- $\alpha < 2m\omega_0$ pseudopériodique, $\alpha = 2m\omega_0$ critique, $\alpha > 2m\omega_0$ apériodique

**QCM d'oscillateurs et de conduction (équation amortie, régimes, pendule, résistance thermique)** (2)

- $m\ddot x + \alpha\dot x + kx = 0$
- pseudopériodique $\iff \alpha < 2m\omega_0$, $\omega_0 = \sqrt{k/m}$, $\omega < \omega_0$
- $x(t) = x_0e^{-\frac{\alpha}{2m}t}\cos(\omega t)$
- pendule : $\ddot\theta + \dfrac gL\theta = 0$, $T = 2\pi\sqrt{L/g}$
- $R_{th} = \dfrac{e}{\lambda_{th}S}$, $\lambda_{th}$ en $\text{W·K}^{-1}\text{·m}^{-1}$

**énergie sur une piste avec propulsion (théorème de l'énergie cinétique, énergie mécanique, réaction en Frenet)** (2)

- $\Delta E_c = \sum W$
- $W(\vec F) = Fl$
- $E_m = \tfrac12mv^2 + mgz$ conservée sans frottement
- Frenet : $m\dfrac{v^2}{R} = \sum F_N$
- $z_C = R(1 - \cos\theta)$

**oscillateur ressort amorti puis ressort sur plan incliné (équation différentielle, énergie, équilibre)** (2)

- $m\ddot x = -kx - \alpha\dot x$
- pseudopériodique si $\alpha < 2m\omega_0$
- $E_m = \tfrac12m\dot x^2 + \tfrac12kx^2$, $\dfrac{dE_m}{dt} = \dot x(m\ddot x + kx) = -\alpha\dot x^2 = \vec f \cdot \vec v$
- plan incliné : $k(x_e - L_0) = mg\sin\alpha$
- $X = x - x_e$, $\ddot X + \dfrac kmX = 0$

**pendule simple (énergie mécanique, petites oscillations, isochronisme, base polaire)** (2)

- $E_c = \tfrac12ml^2\dot\theta^2$ ($v = l\dot\theta$)
- $E_p = mgl(1 - \cos\theta)$
- sans frottement $\dfrac{dE_m}{dt} = 0 \Rightarrow \ddot\theta + \dfrac gl\sin\theta = 0$
- petites oscillations $\ddot\theta + \dfrac gl\theta = 0$, $\theta = \theta_0\cos(\omega t)$, $\omega = \sqrt{g/l}$
- polaire : $\vec a = (\ddot r - r\dot\theta^2)\vec u_r + (2\dot r\dot\theta + r\ddot\theta)\vec u_\theta$

**QCM de dynamique (unité du newton, tension, poulie, machine d'Atwood)** (2)

- $1\ \text{N} = 1\ \text{kg·m·s}^{-2}$
- équilibre : $T = mg$
- $T - mg = ma$ (montée)
- fil et poulie idéaux : même tension aux deux bouts
- Atwood : $a = g\dfrac{m_2 - m_1}{m_1 + m_2}$

**trois masses reliées par des fils (suspendue, table, plan incliné) : accélération et équilibre** (2)

- $\sum\vec F_{ext} = m\vec a$ pour chaque masse
- $T_1 = T_2$, $T_2' = T_3$ (fils et poulies idéaux)
- $a = g\dfrac{m_1 - m_3\sin\alpha}{m_1 + m_2 + m_3}$
- équilibre : $m_1 = m_3\sin\alpha$

**véhicule sur une bosse circulaire (base polaire, réaction normale, condition de contact)** (2)

- base polaire $(\vec u_r, \vec u_\theta)$ centrée en O
- $\vec a = \begin{pmatrix} -v^2/R \\ R\ddot\theta \end{pmatrix}$
- $\vec P = \begin{pmatrix} -mg\cos\theta \\ mg\sin\theta \end{pmatrix}$, $\vec R_N = \begin{pmatrix} R_N \\ 0 \end{pmatrix}$
- contact $\iff R_N > 0 \iff v^2 < gR\cos\theta$

**QCM de cinématique (unité de force, position, vitesse, norme, intégration)** (2)

- $1\ \text{N} = 1\ \text{kg·m·s}^{-2}$
- $\overrightarrow{OM} = x\,\vec u_x + y\,\vec u_y$
- $\vec v = \dfrac{d\overrightarrow{OM}}{dt}$
- $\|\vec v\| = \sqrt{v_x^2 + v_y^2}$
- $\overrightarrow{OM}(t) = \overrightarrow{OM}(0) + \displaystyle\int_0^t\vec v\,dt$
- $\vec a = \dfrac{d\vec v}{dt}$

**tir horizontal (PFD, équations horaires, trajectoire parabolique, passage d'un obstacle, portée)** (2)

- $m\vec a = \vec P \Rightarrow a_x = 0$, $a_y = -g$
- $\vec v = (v_0,\ -gt)$
- $x = v_0t$, $y = -\tfrac12gt^2 + H$
- $y(x) = -\dfrac{gx^2}{2v_0^2} + H$
- portée : $y = 0 \Rightarrow x = \sqrt{\dfrac{2v_0^2H}{g}}$

**pendule simple en coordonnées polaires (vitesse, accélération, PFD, petites oscillations, période)** (2)

- $\overrightarrow{OM} = r\,\vec u_r$
- $\vec v = \dot r\,\vec u_r + r\dot\theta\,\vec u_\theta$
- $\vec a = (\ddot r - r\dot\theta^2)\vec u_r + (2\dot r\dot\theta + r\ddot\theta)\vec u_\theta$
- $r = l$ : $\vec a = -l\dot\theta^2\vec u_r + l\ddot\theta\vec u_\theta$
- $\sin\theta \approx \theta$ : $\ddot\theta + \dfrac gl\theta = 0$
- $T_p = 2\pi\sqrt{l/g}$

**QCM de mécanique (unité et signe du travail, cinématique, position en polaires)** (2)

- $W$ en joules, comme l'énergie
- $W > 0$ : travail moteur, $W < 0$ : résistant
- $\vec F \perp \overrightarrow{AB} \Rightarrow W = 0$
- cinématique : description du mouvement sans ses causes
- polaires : $\overrightarrow{OM} = r\,\vec u_r = \begin{pmatrix} r \\ 0 \end{pmatrix}$ dans $(\vec u_r, \vec u_\theta)$

**tir oblique depuis une hauteur (PFD, équations horaires, trajectoire, durée de vol, portée)** (2)

- $\vec a = \begin{pmatrix} 0 \\ -g \end{pmatrix}$
- $\vec v = \begin{pmatrix} v_0\cos\alpha \\ v_0\sin\alpha - gt \end{pmatrix}$
- $\overrightarrow{OM} = \begin{pmatrix} v_0\cos\alpha\,t \\ -\tfrac12gt^2 + v_0\sin\alpha\,t + h \end{pmatrix}$
- $y(x) = -\dfrac{gx^2}{2v_0^2\cos^2\alpha} + x\tan\alpha + h$
- impact : $y = 0$, $t = \dfrac{v_0\sin\alpha + \sqrt{v_0^2\sin^2\alpha + 2gh}}{g}$

**plan incliné sans frottement puis piste horizontale avec frottement (travail, énergie mécanique, théorème de l'énergie cinétique)** (2)

- $W(\vec P) = mg\,AB\sin\alpha$ en descente
- $W(\vec R_N) = 0$
- sans frottement $E_m$ conservée : $v_B = \sqrt{2g\,AB\sin\alpha}$
- $W(\vec f) = -f\,BC$
- $\Delta E_c = \sum W$ : $BC = \dfrac{mv_B^2}{2f}$

**Frenet (vitesse, accélération) et spirale logarithmique en polaires** (1)

- $dS = R\,d\theta$
- $\vec V = \dfrac{dS}{dt}\vec u_T = R\dot\theta\,\vec u_T$
- $\dfrac{d\vec u_T}{dt} = \dot\theta\,\vec u_N$
- $a_T = \dfrac{dV}{dt}$, $a_N = \dfrac{V^2}{R}$
- $\overrightarrow{OM} = \rho\,\vec u_\rho$
- $\vec V = \dot\rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta$
- $\vec a = (\ddot\rho - \rho\dot\theta^2)\vec u_\rho + (2\dot\rho\dot\theta + \rho\ddot\theta)\vec u_\theta$
- $(e^{\omega t})' = \omega e^{\omega t}$

**barre contre un mur avec frottement au sol (bilan, moments, réaction, coefficient de frottement statique)** (1)

- équilibre : $\sum\vec F_{ext} = \vec 0$ et $\sum\mathcal M_B(\vec F_{ext}) = 0$
- poids de la barre homogène en son milieu
- contact sans frottement : réaction normale à la paroi
- $R_{Bx} = f$ (frottement), $R_{By} = N$
- $\|\vec R_B\| = \sqrt{R_{Bx}^2 + R_{By}^2}$
- $\mu_s = \tan\varphi = \dfrac{R_{Bx}}{R_{By}}$
- $\tan 30° = \dfrac1{\sqrt3}$

**cycloïde puis spirale (vitesse, normes, tracé, polaires, rayon de courbure)** (1)

- $\vec V = (\dot x, \dot y)$, $\vec a = (\ddot x, \ddot y)$
- $\|\vec V\| = \sqrt{\dot x^2 + \dot y^2}$
- $1 - \cos\alpha = 2\sin^2(\alpha/2)$
- $\omega = 2\pi/T$
- tableau de valeurs de $(x(t), y(t))$ en $t = 0, T/4, T/2, 3T/4, T$
- $\vec V = \dot\rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta$
- $\vec V = V\,\vec u_T = R(t)\dot\theta\,\vec u_T$, donc $R = V/\dot\theta$
- $a_T = \dfrac{dV}{dt}$, $a_N = \dfrac{V^2}{R}$

**piste circulaire puis horizontale avec frottement (théorème de l'énergie cinétique, force de frottement, vitesse, réaction)** (1)

- $\Delta E_c = \sum W(\vec F_{ext})$
- $W_{AB}(\vec P) = mgR(1 - \cos\theta)$
- $W_{AB}(\vec f) = -f\cdot R\theta$ (arc de rayon $R$ et d'angle $\theta$)
- réaction normale perpendiculaire au déplacement : $W = 0$
- sur BC horizontal : $\tfrac12m(v_C^2 - v_B^2) = -f\cdot BC$
- $R_N = mg$ (pas d'accélération verticale), $R = \sqrt{R_N^2 + f^2}$

**mouvement circulaire accéléré en cartésien (norme, Frenet, abscisse curviligne, tour complet)** (1)

- $x^2 + y^2 = R^2$ : cercle de centre $O$ et de rayon $R$
- $\vec v = (\dot x, \dot y)$, $v = \sqrt{\dot x^2 + \dot y^2}$
- $\vec v = v\,\vec u_T$
- $s(t) = \int_0^t v\,dt$
- un tour : $s = 2\pi R$
- $a_T = \dfrac{dv}{dt}$, $a_N = \dfrac{v^2}{R}$, $a = \sqrt{a_T^2 + a_N^2}$
- analyse dimensionnelle : $[\alpha t^2] = 1$ (un angle est sans dimension)

**cercle décrit en polaires (ρ, θ, position, vitesse)** (1)

- $\rho = \sqrt{x^2 + y^2}$
- $\tan\theta = \dfrac yx$
- $1 - \cos\varphi = 2\sin^2\dfrac\varphi2$
- $\sin\varphi = 2\sin\dfrac\varphi2\cos\dfrac\varphi2$
- $\dfrac{1 - \cos\varphi}{\sin\varphi} = \tan\dfrac\varphi2$
- $\overrightarrow{OM} = \rho\,\vec u_\rho$
- $\vec v = \dot\rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta$

**plongeoir sur deux appuis (forces, équilibre de translation et de rotation, réactions)** (1)

- équilibre : $\sum\vec F_{ext} = \vec 0$ et $\sum\mathcal M_{pivot}(\vec F_{ext}) = 0$
- choisir le pivot au point d'application d'une force inconnue pour l'éliminer de l'équation des moments
- $\mathcal M = \pm F\,d$ (bras de levier)
- $T\,L = mg\,a$ (pivot en C), $R = T + mg$

**masse suspendue à deux fils (moments, équilibre de rotation, équation en $\cos\theta$)** (1)

- moment par rapport à A : $\vec{\mathcal M}_A(\vec F) = \overrightarrow{AM}\wedge\vec F$
- $\mathcal M_A(\vec P_M) = -mga\cos\theta$ en valeur algébrique pour $AM = a$ à l'angle $\theta$ de l'horizontale
- fil tendu passant par une poulie parfaite : même tension, égale à $m'g$ à l'équilibre
- $\cos^2\theta = \dfrac{1 + \cos 2\theta}2$
- équation du second degré en $X = \cos\theta$ avec $-1 \leqslant X \leqslant 1$ pour choisir la racine valide

**mouvement circulaire en cartésien (vitesse, accélération, trajectoire)** (1)

- $\vec V = (\dot x, \dot y)$, $\vec a = (\ddot x, \ddot y)$
- $\|\vec V\| = \sqrt{\dot x^2 + \dot y^2}$
- $\sin^2 + \cos^2 = 1$
- cercle de centre $(x_0, y_0)$ et de rayon $R$ : $(x - x_0)^2 + (y - y_0)^2 = R^2$

**spirale logarithmique en polaires (vitesse, accélération, Frenet)** (1)

- $\rho = \sqrt{x^2 + y^2}$, $\tan\theta = y/x$
- $\vec V = \dot\rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta$
- $\vec a = (\ddot\rho - \rho\dot\theta^2)\vec u_\rho + (2\dot\rho\dot\theta + \rho\ddot\theta)\vec u_\theta$
- $a_T = \dfrac{dv}{dt}$, $a_N = \dfrac{v^2}{R_c}$, $a^2 = a_T^2 + a_N^2$
- $R_c = \dfrac{v^2}{a_N}$

**base de Frenet (démonstration, abscisse curviligne, rayon de courbure)** (1)

- $\vec V = v\,\vec u_T = R\dot\theta\,\vec u_T$
- $\vec a = \dfrac{dv}{dt}\vec u_T + \dfrac{v^2}{R_c}\vec u_N$
- $\dfrac{d\vec u_T}{dt} = \dot\theta\,\vec u_N$
- $s(t) = \int_0^t v\,dt$, $v(t) = v(t_0) + \int a_T\,dt$
- $R_c = \dfrac{v^2}{a_N}$
- unité de $\alpha$ = (m·s$^{-2}$)/(unité du facteur de $\vec u_T$)

**spirale sur un cône en cylindriques (vitesse, accélération, passage en cartésien)** (1)

- $\overrightarrow{OM} = \rho\,\vec u_\rho + z\,\vec u_z$
- $\vec V = \dot\rho\,\vec u_\rho + \rho\dot\theta\,\vec u_\theta + \dot z\,\vec u_z$
- $\vec a = (\ddot\rho - \rho\dot\theta^2)\vec u_\rho + (2\dot\rho\dot\theta + \rho\ddot\theta)\vec u_\theta + \ddot z\,\vec u_z$
- $x = \rho\cos\theta$, $y = \rho\sin\theta$
- $(e^{\omega t})' = \omega e^{\omega t}$
- la norme est la même dans toute base orthonormée

**mouvement circulaire (trajectoire, vitesse, accélération, composantes de Frenet, rayon de courbure)** (1)

- $x^2 + y^2 = R^2$
- $\vec V = (\dot x, \dot y)$, $\vec a = (\ddot x, \ddot y)$
- $a_T = \dfrac{dv}{dt}$, $a_N = \dfrac{v^2}{R_c}$, $a^2 = a_T^2 + a_N^2$
- $R_c = \dfrac{v^2}{a_N}$
- mouvement circulaire uniforme : $a_T = 0$, $R_c = R$

**projectile lancé d'une hauteur $h$ (équations horaires, trajectoire, vitesse, accélération, sommet)** (1)

- $x = v_0\cos\alpha\,t$, $y = -\tfrac12gt^2 + v_0\sin\alpha\,t + h$
- $y(x) = -\dfrac{g}{2v_0^2\cos^2\alpha}x^2 + \tan\alpha\,x + h$
- $\vec v = (v_0\cos\alpha,\ -gt + v_0\sin\alpha)$, $\vec a = -g\,\vec u_y$
- sommet S : $v_y = 0 \Rightarrow t_S = \dfrac{v_0\sin\alpha}{g}$, $x_S = v_0\cos\alpha\,t_S$
- selon $Ox$ : mouvement rectiligne uniforme, selon $Oy$ : rectiligne uniformément varié

**vilebrequin (polaires puis cartésiennes : position, vitesse, accélération du piston)** (1)

- $\theta(t) = \omega t \Rightarrow \dot\theta = \omega$
- polaires : $\overrightarrow{OM} = R\,\vec u_\rho$, $\vec v = R\omega\,\vec u_\theta$, $\vec a = -R\omega^2\,\vec u_\rho$
- cartésiennes : $\vec v = \dfrac{d\overrightarrow{OP}}{dt}$, $\vec a = \dfrac{d\vec v}{dt}$
- $(\sin\omega t)' = \omega\cos\omega t$, $(\cos\omega t)' = -\omega\sin\omega t$

## Thermodynamique

**calorimétrie (capacité du calorimètre, fusion d'un glaçon, mélange d'eau)** (4)

- enceinte isolée : $\sum Q_i = 0$
- $Q = mc(\theta_f - \theta_i)$
- calorimètre : $Q = C_{cal}(\theta_f - \theta_i)$
- fusion : $Q = mL_f$
- chemin fictif glace $\theta_2 \to 0$ °C $\to$ fusion $\to$ eau $0 \to \theta_e$
- $m = \rho V$

**calorimétrie (capacité du calorimètre, capacité massique du plomb, glace en eau liquide)** (2)

- $\sum Q_i = 0$
- $Q = mc(\theta_f - \theta_i)$
- calorimètre : $Q = C_{cal}(\theta_f - \theta_i)$
- fusion : $Q = mL_f$
- glace $-20$ °C $\to 0$ °C ($c_g$) $\to$ fusion ($L_f$) $\to$ eau $0 \to 20$ °C ($c_e$)

**gaz parfait (enthalpie, Meyer et capacités molaires, compression isotherme, Laplace en T, V et T, P)** (2)

- $dU = \delta Q - P\,dV$
- à $P$ constante $Q_P = \Delta(U + PV) = \Delta H$
- $c_p - c_v = R$, $\gamma = \dfrac{c_p}{c_v}$ $\Rightarrow c_v = \dfrac{R}{\gamma - 1}$, $c_p = \dfrac{\gamma R}{\gamma - 1}$
- isotherme : $W = -nRT\ln\dfrac{V_B}{V_A} = nRT\ln\dfrac{P_B}{P_A}$, $Q = -W$
- Laplace : $PV^\gamma$, $TV^{\gamma-1}$, $T^\gamma P^{1-\gamma}$ constants

**cycle de Joule (deux adiabatiques, deux isobares, rendement, entropie)** (2)

- Laplace $T^\gamma P^{1-\gamma} = \text{cte}$
- adiabatique : $Q = 0$, $W = nc_v\Delta T$, $\Delta S = 0$ si réversible
- isobare : $Q = nc_p\Delta T$, $W = -nR\Delta T$, $\Delta S = nc_p\ln\dfrac{T_f}{T_i}$
- $r = \dfrac{Q_{BC} + Q_{DA}}{Q_{BC}} = 1 - \dfrac{T_D - T_A}{T_C - T_B} = 1 - a^{\frac{1-\gamma}{\gamma}}$, $a = \dfrac{P_B}{P_A}$

**gaz parfait (dU, dH, relation de Mayer, chaleur isobare, travail isobare et adiabatique)** (2)

- $dU = nc_vdT$, $dH = nc_pdT$
- $H = U + PV$, $PV = nRT$
- Mayer : $C_p - C_v = nR$
- $dU = \delta Q + \delta W$, $\delta W = -P\,dV$
- isobare : $W = -P(V_B - V_A)$, $\delta Q_P = nc_pdT$
- adiabatique : $Q = 0$, $W = \Delta U = nc_v(T_B - T_A)$

**cycle de Beau de Rochas (deux adiabatiques, deux isochores, rendement)** (2)

- Laplace : $TV^{\gamma-1} = \text{cte}$
- isochore : $W = 0$, $Q = \Delta U = nc_v\Delta T$
- adiabatique : $Q = 0$, $W = \Delta U = nc_v\Delta T$
- $r = \dfrac{Q_{AB} + Q_{CD}}{Q_{AB}} = 1 - \dfrac{T_C - T_D}{T_B - T_A}$
- $a = \dfrac{V_2}{V_1}$, $r = 1 - a^{1-\gamma}$

**QCM de thermodynamique (premier principe, adiabatique, isotherme, isobare, fonction d'état, Laplace)** (2)

- $dU = \delta W + \delta Q = -P\,dV + \delta Q$
- adiabatique : $PV^\gamma = \text{cte}$, $W = nc_v(T_2 - T_1)$
- isotherme : $\Delta U = 0$, $Q = -W$, $W = -nRT\ln\dfrac{V_2}{V_1}$
- isobare : $\dfrac VT = \text{cte}$
- $W$ et $Q$ ne sont pas des fonctions d'état
- Laplace en $(T, P)$ : $T^\gamma P^{1-\gamma} = \text{cte}$

**calorimétrie (vapeur sur glace avec condensation et fusion, capacité du calorimètre)** (2)

- $\sum Q_i = 0$
- $Q = mc(\theta_f - \theta_i)$
- fusion : $Q = mL_f$
- condensation : $Q = mL_c = -mL_v$
- calorimètre : $Q = C_{cal}(\theta_f - \theta_i)$

**démonstration de la loi de Laplace (dH = V dP, dU, dH, intégration)** (2)

- $H = U + PV$
- $dU = \delta Q - P\,dV$
- adiabatique : $\delta Q = 0$, $dH = V\,dP$
- $dU = nc_vdT$, $dH = nc_pdT$
- $\gamma = \dfrac{c_p}{c_v}$
- $\gamma\dfrac{dV}V = -\dfrac{dP}P \Rightarrow PV^\gamma = \text{cte}$

**cycle Diesel (deux adiabatiques, une isobare, une isochore, rendement)** (2)

- Laplace $TV^{\gamma-1} = \text{cte}$
- isobare : $\dfrac TV = \text{cte}$, $W = -P\Delta V$, $Q = nc_p\Delta T$
- isochore : $W = 0$, $Q = nc_v\Delta T$
- adiabatique : $Q = 0$, $W = nc_v\Delta T$
- $\alpha = \dfrac{V_A}{V_B}$, $\beta = \dfrac{V_C}{V_B}$
- $r = 1 + \dfrac{Q_{DA}}{Q_{BC}} = 1 + \dfrac{\alpha^{1-\gamma}(1 - \beta^\gamma)}{\gamma(\beta - 1)}$

**QCM de thermodynamique (enthalpie, transformations du gaz parfait, Laplace)** (2)

- $H = U + PV$
- $dH = \delta Q + V\,dP$ (réversible)
- isotherme : $\Delta U = 0$, $Q = -W$
- isobare : $W = -P(V_2 - V_1)$
- isochore : $Q = nc_v\Delta T$, $\dfrac{P_1}{T_1} = \dfrac{P_2}{T_2}$
- Laplace : $T^\gamma P^{1-\gamma} = \text{cste}$

**transformation isotherme et adiabatique du gaz parfait (Q, W, pression, volume, température)** (2)

- isotherme : $\Delta U = 0$, $Q = -W$, $P_1V_1 = P_2V_2$, $W = -nRT\ln\dfrac{V_2}{V_1} = -P_1V_1\ln\dfrac{V_2}{V_1}$
- $PV = nRT$
- adiabatique : $Q = 0$, $W = \Delta U = nc_v\Delta T$, $c_v = \tfrac32R$ (monoatomique)
- Laplace : $P^{1-\gamma}T^\gamma = \text{cste}$

**travail et chaleur selon le chemin (isochores, isobares, droite dans le diagramme de Clapeyron)** (2)

- $PV = nRT$
- isochore : $W = 0$, $Q = nc_v\Delta T$
- isobare : $W = -P\Delta V$, $Q = nc_p\Delta T$
- $W = -\displaystyle\int P\,dV$ (aire sous la courbe)
- $\Delta U = nc_v\Delta T = W + Q$

**cycle adiabatique, isochore, isotherme (chaleur et travail reçus, Laplace)** (2)

- Laplace : $PV^\gamma = \text{cste}$, $TV^{\gamma-1} = \text{cste}$
- adiabatique : $Q = 0$, $W = \Delta U = \dfrac{P_BV_B - P_AV_A}{\gamma - 1}$
- isochore : $W = 0$
- isotherme : $Q = -W = nRT\ln\dfrac{V_f}{V_i}$

**QCM de thermodynamique (unités, Mayer, cycle, premier principe, grandeurs intensives)** (2)

- résistance thermique en $\text{K·W}^{-1}$
- Mayer : $c_p - c_v = R$, $\gamma = \dfrac{c_p}{c_v}$ $\Rightarrow c_p = \dfrac{\gamma R}{\gamma - 1}$
- sur un cycle : $\Delta U = \Delta H = 0$, $W + Q = 0$
- $dU = \delta Q - P\,dV$
- isobare : $Q = \Delta H = nc_p\Delta T$
- équilibre thermique : $T_1 = T_2$

**cycle de Brayton (deux adiabatiques, deux isobares, rendement)** (2)

- Laplace : $PV^\gamma = \text{cste}$ $\Rightarrow \dfrac{T}{P^\beta} = \text{cste}$ avec $\beta = \dfrac{\gamma - 1}{\gamma}$
- adiabatique : $Q = 0$, $W = \Delta U = C_v\Delta T$
- isobare : $Q = C_p\Delta T$, $W = \Delta U - Q = (C_v - C_p)\Delta T$
- $W_{cycle} = -Q_{cycle}$
- $\eta = -\dfrac{W_{cycle}}{Q_{BC}} = 1 - \dfrac{1}{r_p^\beta}$, $r_p = \dfrac{P_B}{P_A}$

**cycle de Carnot (deux isothermes, deux adiabatiques, rendement)** (2)

- Laplace : $TV^{\gamma-1} = \text{cste}$
- isotherme : $\Delta U = 0$, $Q = -W = nRT\ln\dfrac{V_f}{V_i}$
- adiabatique : $Q = 0$, $W = \Delta U = \dfrac{nR}{\gamma - 1}\Delta T$
- $\dfrac{V_A}{V_B} = \dfrac{V_D}{V_C}$
- $r = \dfrac{|W_{cycle}|}{Q_{absorbée}} = 1 - \dfrac{T_f}{T_c}$

**QCM de thermodynamique (intensif, isobare, travail, force de pression, unités)** (2)

- intensive : $P$, $T$
- extensive : $V$, $m$
- isobare : $P = \text{cste}$, $W = -P_0(V_f - V_i)$
- $d\vec F = P\,d\vec S$
- énergie en joules (J)

**calorimétrie (bilan d'enthalpie dans une enceinte isolée, capacité thermique massique)** (2)

- $\Delta H = mc(T_f - T_i)$
- enceinte isolée, isobare : $\sum\Delta H = 0$
- $c_{cuivre} = -\dfrac{m_{eau}c_{eau}(T_f - T_{eau})}{m_{cuivre}(T_f - T_{cuivre})}$

**cycle de Lenoir dans le diagramme de Watt (isochore, isotherme, isobare, travaux)** (2)

- isotherme : $P = \dfrac{nRT}{V}$ (hyperbole)
- isochore : $W = 0$
- isotherme : $W = -nRT\ln\dfrac{V_f}{V_i}$
- isobare : $W = -P(V_f - V_i)$
- $PV = nRT$

**machine ditherme réversible (premier et deuxième principes, rendement de Carnot)** (2)

- sur un cycle : $\Delta U = Q_c + Q_f + W = 0$
- $\Delta S = \dfrac{Q_c}{T_c} + \dfrac{Q_f}{T_f} + S_{créée} = 0$, $S_{créée} = 0$ (réversible)
- $\rho = \left|\dfrac{\text{énergie utile}}{\text{énergie coûteuse}}\right| = -\dfrac{W}{Q_c} = 1 + \dfrac{Q_f}{Q_c} = 1 - \dfrac{T_f}{T_c}$

**QCM de thermodynamique (gaz qui refroidit, cycle, isochore, pompe à chaleur, conduction)** (2)

- $PV = nRT$
- sur un cycle : état initial = état final, $\Delta U = 0$
- isochore : $W = 0$, $Q = \Delta U$
- pompe à chaleur : énergie utile = chaleur cédée à la source chaude
- conduction : transfert sans déplacement de matière

**calorimétrie avec vaporisation partielle (bilan d'enthalpie, masse vaporisée)** (2)

- $\Delta H = mc_p\Delta T$ sans changement d'état
- $\Delta H = m\,\Delta h_{vap}$ pour la vaporisation
- enceinte calorifugée, isobare : $\sum\Delta H = 0$
- $m_{vap} = \dfrac{-m_{fer}c_{fer}(T_f - T_{fer}) - m_{eau}c_{eau}(T_f - T_{eau})}{\Delta h_{vap}}$

**cycle isotherme, isobare, isochore du gaz parfait (volumes, travaux, bilan)** (2)

- $PV = nRT$
- isotherme : $P_AV_A = P_BV_B$, $W = -nRT\ln\dfrac{V_f}{V_i}$
- isobare : $W = -P(V_f - V_i)$
- isochore : $W = 0$
- sur un cycle : $\sum W + \sum Q = \Delta U = 0$

**conduction thermique (flux, unités, résistances thermiques en série)** (2)

- $\Phi = -\lambda_{th}S\dfrac{\Delta\theta}{e} = -\dfrac{\Delta\theta}{R_{th}}$
- $R_{th} = \dfrac{e}{\lambda_{th}S}$
- $[\Phi] = \text{J·s}^{-1} = \text{W}$, $[R_{th}] = \text{K·W}^{-1}$, $[\lambda_{th}] = \text{W·K}^{-1}\text{·m}^{-1}$
- même flux dans chaque couche : $R_{th} = \sum R_{th,i}$

**calorimétrie (capacité massique d'une huile, glace en vapeur, capacité du calorimètre)** (2)

- enceinte adiabatique : $\sum Q_i = 0$
- $Q = mc(\theta_f - \theta_i)$
- calorimètre : $Q = C_{cal}(\theta_f - \theta_i)$
- changement d'état : $Q = mL$
- glace $-20$ °C $\to 0$ °C ($c_g$) $\to$ fusion ($L_f$) $\to 100$ °C ($c_e$) $\to$ vaporisation ($L_v$)

**QCM de thermodynamique et de mécanique (force non conservative, grandeur intensive, premier principe élémentaire)** (2)

- force non conservative : frottement (travail dépendant du chemin)
- conservatives : poids, rappel du ressort, force électrique
- intensive : température, pression
- extensive : masse, volume
- $dU = \delta Q + \delta W = \delta Q - P\,dV$

**calorimétrie (capacité du calorimètre avec un bloc de plomb)** (2)

- calorimètre isolé : $\sum Q_i = 0$
- $Q = mc(\theta_e - \theta_i)$
- calorimètre : $Q = C_{cal}(\theta_e - \theta_i)$, à la température initiale de l'eau qu'il contient

**résistances thermiques d'une paroi (double vitrage, mur isolé, série et parallèle, puissance de chauffage)** (2)

- $R_{th} = \dfrac{e}{\lambda S}$
- couches traversées par le même flux (série) : $R = \sum R_i$
- surfaces côte à côte (parallèle) : $\dfrac1R = \sum\dfrac1{R_i}$
- $\Phi = \dfrac{\Delta T}{R_{th}}$
- le flux va du chaud vers le froid

**calorimétrie avec changement d'état (chemin fictif, chaleur latente de fusion)** (1)

- $\Delta H = mc\Delta T$ sans changement d'état
- fusion à 0 °C : $\Delta H = m\,\Delta h_F$
- enceinte isolée, isobare : $\sum\Delta H = 0$
- chemin fictif : échauffement de la glace, fusion, puis échauffement ou refroidissement de l'eau liquide

**machine frigorifique ditherme (signes des échanges, premier et deuxième principes, efficacité de Carnot)** (1)

- sur un cycle : $\Delta U = Q_c + Q_f + W = 0$
- $\Delta S = \dfrac{Q_c}{T_c} + \dfrac{Q_f}{T_f} + S_{créée} = 0$
- réfrigérateur : $Q_f > 0$, $Q_c < 0$, $W > 0$
- $e = \dfrac{Q_f}{W} = -\dfrac{1}{1 + Q_c/Q_f}$
- réversible : $e = \dfrac{T_f}{T_c - T_f}$
- $T(\text{K}) = T(°\text{C}) + 273$

## OBM

**traduire avec quantificateurs** (13)

- « tout » $= \forall$, « il existe » $= \exists$, « aucun » $= \forall \dots \neg$
- l'ordre $\forall\exists$ / $\exists\forall$ change le sens
- $f$ s'annule : $\exists x, f(x) = 0$
- minimum en $a$ : $\exists a, \forall x, f(x) \geqslant f(a)$
- pair : $\exists k, n = 2k$

**injectivité, surjectivité, image directe et réciproque** (12)

- injective : $f(x) = f(y) \Rightarrow x = y$ (contre-exemple $f(1) = f(2)$)
- surjective : $\forall y, \exists x, f(x) = y$
- $f(A) = \{f(x), x \in A\}$
- $f^{-1}(B) = \{x, f(x) \in B\}$ (peut être vide)

**image directe et réciproque, injectivité, surjectivité, composée** (11)

- $f(A) = \{y \in F, \exists x \in A, y = f(x)\}$
- $f^{-1}(B) = \{x \in E, f(x) \in B\}$
- injective : $f(x) = f(x') \Rightarrow x = x'$
- surjective : $\forall y, \exists x, y = f(x)$
- $g \circ f$ injective si $f$, $g$ injectives
- surjective si $f$, $g$ surjectives

**image directe, image réciproque (lecture graphique)** (9)

- $f(A) = \{f(x), x \in A\}$
- $f^{-1}(B) = \{x, f(x) \in B\}$
- lire les valeurs prises (bornes ouvertes / fermées)
- $f(\mathbb{R})$ = ensemble des valeurs prises

**nier une phrase** (8)

- $\neg(\forall x, P(x)) \iff \exists x, \neg P(x)$
- $\neg(\exists x, P(x)) \iff \forall x, \neg P(x)$
- $\neg(P \Rightarrow Q) \iff P \wedge \neg Q$
- $\neg(P \wedge Q) \iff \neg P \vee \neg Q$
- $\neg(P \vee Q) \iff \neg P \wedge \neg Q$
- « aucun » = $\forall, \neg$

**ensembles (appartenance, inclusion, union, intersection, produit, complémentaire)** (8)

- $x \in A$
- $A \subset B$
- $A \cup B$, $A \cap B$
- $A \times B = \{(a, b), a \in A, b \in B\}$
- complémentaire $\bar B = E \setminus B$
- $B = [\![0, 7]\!]$

**propriétés d'une relation, négation, contraposée** (7)

- réflexive $\forall x, x\mathcal Rx$
- antisymétrique $x\mathcal Ry \wedge y\mathcal Rx \Rightarrow x = y$
- transitive
- négation de $\forall(P \Rightarrow Q)$ : $\exists(P \wedge \neg Q)$
- contraposée de $P \Rightarrow Q$ : $\neg Q \Rightarrow \neg P$
- $\neg(A \wedge B) = \neg A \vee \neg B$
- ordre = réflexive + antisymétrique + transitive

**injectivité / surjectivité, restriction** (6)

- injective $\iff$ toute droite horizontale coupe le graphe au plus une fois
- surjective sur $F$ $\iff$ tout $y \in F$ est atteint
- $(x-2)^2 - 1 \geqslant -1$
- restreindre le départ à $[2, +\infty[$ rend injective, l'arrivée à $[-1, +\infty[$ rend surjective

**injectivité / surjectivité, composées** (5)

- injective : $f(x) = f(y) \Rightarrow x = y$, contre-exemple $f(a) = f(b)$ avec $a \neq b$
- surjective : $\forall y, \exists x, f(x) = y$
- $(f \circ g)(x) = f(g(x))$

**relation d'ordre** (5)

- ordre = réflexive ($\forall x, x\mathcal Rx$), antisymétrique ($x\mathcal Ry$ et $y\mathcal Rx \Rightarrow x = y$), transitive ($x\mathcal Ry$ et $y\mathcal Rz \Rightarrow x\mathcal Rz$)
- contre-exemple pour réfuter
- $x^2 = y^2 \iff x = \pm y$

**négations, implications et équivalences** (4)

- $\neg(P \wedge Q) = \neg P \vee \neg Q$
- $\neg(P \vee (Q \wedge R)) = \neg P \wedge (\neg Q \vee \neg R)$
- $\neg(P \Rightarrow Q) = P \wedge \neg Q$
- $P \Rightarrow Q \equiv \neg P \vee Q$
- $x^2 + x - 6 = (x+3)(x-2)$
- multiple de 6 $\Rightarrow$ multiple de 3
- $\sqrt{x^2} = |x|$

**récurrence (inégalité de Bernoulli)** (3)

- récurrence : $P(n_0)$ et $P(n) \Rightarrow P(n+1)$
- $(1+x)^{n+1} = (1+x)^n(1+x)$
- $(1+nx)(1+x) = 1 + (n+1)x + nx^2 \geqslant 1 + (n+1)x$

**injectivité / surjectivité de $x \mapsto x^2$** (3)

- injective : $f(x) = f(y) \Rightarrow x = y$
- surjective : $\forall y \in F, \exists x \in E, y = f(x)$
- $x^2 = y^2 \iff x = \pm y$
- $x^2 \geqslant 0$

**récurrence ($n! > 2^n$)** (3)

- récurrence : $P(n_0)$ et $P(n) \Rightarrow P(n+1)$
- $(n+1)! = (n+1)\,n!$
- $2^{n+1} = 2 \cdot 2^n$
- $n + 1 > 2$

**composée d'injections / surjections** (3)

- $(f \circ g)(x) = f(g(x))$
- injective : $f(x) = f(y) \Rightarrow x = y$
- surjective : $\forall y, \exists x, y = f(x)$
- $g \circ f$ injective $\Rightarrow f$ injective
- $g \circ f$ surjective $\Rightarrow g$ surjective

**récurrence (somme géométrique)** (3)

- récurrence
- $S_{n+1} = S_n + q^{n+1}$
- $\sum_{k=0}^n q^k = \frac{1 - q^{n+1}}{1 - q}$ ($q \neq 1$), $= n + 1$ si $q = 1$

**quantificateurs, négations, implications** (3)

- s'annule : $\exists x, f(x) = 0$
- constante : $\exists a, \forall x, f(x) = a$
- majorée : $\exists M, \forall x, f(x) \leqslant M$
- $\neg\forall = \exists\neg$
- $\neg(A \vee B) = \neg A \wedge \neg B$
- $\neg(f > 0) = (f \leqslant 0)$
- $P \Rightarrow Q$ équivaut à sa contraposée $\neg Q \Rightarrow \neg P$

**récurrence (dérivée $n$-ième)** (2)

- récurrence
- $(\ln(1+x))' = \frac1{1+x}$
- $((1+x)^{-n})' = -n(1+x)^{-n-1}$
- $(n-1)! \cdot n = n!$

**injectivité / surjectivité, composées sur $\mathbb{N}$** (2)

- injective : $f(x) = f(y) \Rightarrow x = y$ (contre-exemple : $f(a) = f(b)$, $a \neq b$)
- surjective : $\forall y, \exists x, y = f(x)$ (contre-exemple : un $y$ sans antécédent)
- $(g \circ f)(n) = g(f(n))$

**image réciproque d'un singleton** (2)

- $f^{-1}(\{b\}) = \{x, f(x) = b\}$
- séparer les cas $n$ pair ($n = 2k$) et impair

**vérité d'une proposition quantifiée** (2)

- $\forall$ : une seule valeur contre-exemple suffit pour réfuter
- $\exists$ : un seul exemple suffit pour prouver
- $\forall x \exists y$ : $y$ peut dépendre de $x$
- $y^2 \geqslant 0$

**relation d'équivalence** (2)

- équivalence = réflexive ($x\mathcal Rx$), symétrique ($x\mathcal Ry \Rightarrow y\mathcal Rx$), transitive ($x\mathcal Ry$ et $y\mathcal Rz \Rightarrow x\mathcal Rz$)

**récurrence (inégalité avec factorielle)** (2)

- récurrence
- $\frac{2^{n+1}}{(n+1)!} = \frac{2^n}{n!} \cdot \frac2{n+1}$
- $n \geqslant 2 \Rightarrow \frac2{n+1} \leqslant \frac23$
- initialisation $n = 2$ : $\frac{4}{2} = 2 = \frac92 \cdot \frac49$

**conditions nécessaires et suffisantes, négations, contraposée, inclusion** (2)

- $x^2 > 4 \iff x < -2$ ou $x > 2$
- $A \Rightarrow P$ vraie si l'ensemble de $A$ est inclus dans celui de $P$
- $\neg(A \Rightarrow B) \iff A \wedge \neg B$
- contraposée $\neg B \Rightarrow \neg A$ (même table de vérité)
- $\cos \in [-1, 1]$
- $A \subset B \iff \forall x, x \in A \Rightarrow x \in B$
- contre-exemple pour $B \not\subset A$

**nier une phrase quantifiée** (2)

- $\neg(\forall x, P) = \exists x, \neg P$
- $\neg(A \Rightarrow B) = A \wedge \neg B$
- $\neg(f(x) \geqslant f(x')) = f(x) < f(x')$

**vérité, négation et contraposée d'une implication quantifiée** (2)

- $x^2 - 3x + 2 = (x-1)(x-2) \leqslant 0 \iff x \in [1, 2]$
- implication vraie $\iff$ inclusion des ensembles
- $\neg(\forall x, A \Rightarrow B) = \exists x, A \wedge \neg B$
- contraposée $\neg B \Rightarrow \neg A$
- $\neg(x \leqslant 1 \vee x \geqslant 2) = (x > 1 \wedge x < 2)$

## DP

**probabilités totales et Bayes** (17)

- probabilités totales : $P(M) = P(M \mid V)P(V) + P(M \mid \bar V)P(\bar V)$
- Bayes : $P(V \mid M) = \frac{P(M \mid V)P(V)}{P(M)}$
- $P(\bar V) = 1 - P(V)$

**dénombrement (p-listes, arrangements, anagrammes, parties)** (10)

- $p$-listes (avec remise, ordre) : $n^p$
- arrangements (sans remise, ordre) : $A_n^p = \frac{n!}{(n-p)!}$
- permutations : $n!$
- anagrammes avec lettres répétées : $\frac{n!}{k_1!k_2!\dots}$
- nombre de parties d'un ensemble à $m$ éléments : $2^m$
- principe multiplicatif

**formules de base des probabilités** (9)

- $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
- $P(\Omega) = 1$
- $P(\emptyset) = 0$
- $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$
- indépendants $\iff P(A \cap B) = P(A)P(B)$
- partition : deux à deux disjoints, union $= \Omega$ (non vides)

**coefficients binomiaux (symétrie)** (8)

- $\binom np = \frac{n!}{p!(n-p)!}$
- $\binom np = \binom n{n-p}$
- $\binom np$ = nombre de parties à $p$ éléments d'un ensemble à $n$ éléments
- bijection $A \mapsto \bar A$

**loi de Bernoulli, loi binomiale, espérance et variance** (6)

- Bernoulli $\mathcal{B}(p)$ : $E = p$, $V = p(1-p)$
- binomiale $\mathcal{B}(n,p)$ : $P(Y = k) = \binom nk p^k(1-p)^{n-k}$, $E = np$, $V = np(1-p)$
- $E(G) = \sum x_iP(G = x_i)$
- $V(G) = E(G^2) - E(G)^2$ (König-Huygens)

**binôme de Newton et double comptage** (6)

- $(a + b)^n = \sum_{k=0}^n \binom nk a^kb^{n-k}$
- $a = 1$, $b = 3$
- principe multiplicatif $4^n$
- double comptage : compter le même ensemble de deux façons
- $\binom nk$ façons de choisir $k$ cases

**interpréter une formule de dénombrement** (6)

- $\frac{n!}{(n-p)!} = A_n^p$ : tirage successif sans remise (ordre)
- $\binom np$ : tirage simultané
- $\binom{8}{3}\binom{8}{2}$ : 3 cartes d'une couleur et 2 d'une autre
- $\binom{7}{1}\binom{24}{3}$ : exactement 1 parmi 7, le reste parmi 24 (catégories disjointes)

**dénombrement de mains de cartes** (4)

- $|\Omega| = \binom{32}5$
- « au moins un » : complémentaire $P(A) = 1 - P(\bar A)$
- $\binom{n}{k} = \frac{n!}{k!(n-k)!}$
- principe multiplicatif (choisir chaque catégorie séparément)
- équiprobabilité $P = \frac{|A|}{|\Omega|}$

**cardinal d'une union, partition** (4)

- $F \cap G = \emptyset \Rightarrow \mathrm{Card}(F \cup G) = \mathrm{Card}F + \mathrm{Card}G$
- $A = (A \setminus B) \sqcup (A \cap B)$
- $\mathrm{Card}(A \cup B) = \mathrm{Card}A + \mathrm{Card}B - \mathrm{Card}(A \cap B)$

**tirages simultanés, combinaisons** (3)

- tirage simultané de $k$ parmi $n$ : $\binom nk$
- « A ou B » incompatibles : additionner
- « A et B » : multiplier les $\binom{}{}$
- contraire : $P(\bar A) = 1 - P(A)$
- équiprobabilité

**indépendance et incompatibilité** (3)

- indépendants $\iff P(A \cap B) = P(A)P(B) \iff P_B(A) = P(A)$
- $P_B(A) = \frac{P(A \cap B)}{P(B)}$
- incompatibles $\iff A \cap B = \emptyset$

**combinaisons, formule de Pascal** (3)

- tirage simultané : $\binom nk$
- contenant un élément fixé : $\binom{n-1}{k-1}$
- ne le contenant pas : $\binom{n-1}k$
- Pascal : $\binom{n-1}{k-1} + \binom{n-1}{k} = \binom nk$
- $\binom nk = \frac{n!}{k!(n-k)!}$
- mettre au même dénominateur $k!(n-k)!$

**arrangements, combinaisons, complémentaire** (3)

- classement de $p$ parmi $n$ (ordre) : $n(n-1)\dots(n-p+1)$
- sans ordre : $\binom np$
- « au moins A ou B » = total $-$ « ni A ni B »
- place imposée : multiplier par le nombre de places possibles

**formule de Vandermonde par double comptage** (3)

- $\binom pi$ façons de choisir $i$ vertes, $\binom n{k-i}$ rouges
- somme sur les cas disjoints $i = 0..k$
- Vandermonde $\sum_{i=0}^k \binom pi\binom n{k-i} = \binom{n+p}k$
- $\binom{11}4 = 330$

**linéarité de l'espérance, formule de König-Huygens** (3)

- $E(X + Y) = E(X) + E(Y)$
- $E(aX + b) = aE(X) + b$
- $V(X) = E((X - E(X))^2) = E(X^2) - E(X)^2$
- $(a - b)^2 = a^2 - 2ab + b^2$

**loi d'une variable, Bernoulli, binomiale (somme d'indépendantes)** (3)

- $P(X = x) = \frac{\text{nb de boules } x}{\text{nb total}}$
- $E(X) = \sum xP(X = x)$
- $V = E(X^2) - E(X)^2$
- Bernoulli $E = p$, $V = p(1-p)$
- somme de $n$ Bernoulli indépendantes de paramètre $p$ : $\mathcal{B}(n, p)$, $E = np$, $V = np(1-p)$
- binôme pour $\sum P = 1$

**dénombrement de mains, probabilités totales et Bayes** (2)

- équiprobabilité : $P(A) = \frac{|A|}{|\Omega|}$
- $|\Omega| = \binom{32}{5}$
- $\binom nk = \frac{n!}{k!(n-k)!}$
- partition : $A_i$ deux à deux disjoints et $\bigsqcup A_i = \Omega$
- probabilités totales : $P(B) = \sum P(B \mid A_i)P(A_i)$
- Bayes : $P(A \mid B) = \frac{P(B \mid A)P(A)}{P(B)}$

**loi binomiale et loi uniforme (espérance, variance)** (2)

- $X \sim \mathcal{B}(n,p)$ : $P(X = k) = \binom nk p^k(1-p)^{n-k}$, $E(X) = np$, $V(X) = np(1-p)$
- uniforme sur $[\![1,n]\!]$ : $P(Y = k) = \frac1n$, $E(Y) = \frac{n+1}2$
- $\sum_{k=1}^n k = \frac{n(n+1)}2$

**combinaisons et arrangements avec contraintes** (2)

- groupe sans ordre : $\binom nk$
- postes distincts : principe multiplicatif $n(n-1)\dots$
- « exactement $a$ de type 1 et $b$ de type 2 » : $\binom{n_1}a\binom{n_2}b$
- « au moins » : somme des cas disjoints
- élément imposé : choisir parmi les restants
- disjonction de cas

**Bernoulli, binomiale, loi d'un rang d'apparition** (2)

- Bernoulli $E = p$, $V = p(1-p)$
- binomiale (tirages avec remise) $P(Y = k) = \binom nk p^k(1-p)^{n-k}$, $E = np$, $V = np(1-p)$
- tirages sans remise : produit de probabilités conditionnelles
- $E(Z) = \sum kP(Z = k)$
- $V = E(Z^2) - E(Z)^2$

**démonstration de cours ($E(aX+b)$)** (2)

- $E(Y) = \sum_i y_iP(Y = y_i)$
- $P(aX + b = ax_i + b) = P(X = x_i)$
- $\sum_i P(X = x_i) = 1$
- linéarité de $\sum$

**p-listes, arrangements, complémentaire (digicode)** (2)

- principe multiplicatif
- chiffres distincts : $10 \times 9 \times 8$
- avec répétition : $10^3$
- permutations de 3 chiffres connus : $3!$
- « au moins un 4 » = total $-$ « aucun 4 » : $10^3 - 9^3$

**double comptage, $\binom np\binom pk = \binom nk\binom{n-k}{p-k}$** (2)

- choisir $p$ puis $k$ parmi eux = choisir les $k$ puis $p - k$ parmi les $n - k$ restants
- $\binom nk = \frac{n!}{k!(n-k)!}$
- $\sum_{k=0}^p \binom pk = 2^p$, donc $S_p = \binom np 2^p$

**démonstration de cours ($E(aX+b)$, $V(aX+b)$)** (2)

- $E(X) = \sum x_iP(X = x_i)$
- $V(X) = \sum (x_i - E(X))^2P(X = x_i)$
- $E(aX + b) = aE(X) + b$
- $V(aX + b) = a^2V(X)$
- $\sum P(X = x_i) = 1$

**coefficients binomiaux, récurrence (somme de $\binom kp$)** (2)

- $C_n^p = \binom np = \frac{n!}{p!(n-p)!}$
- Pascal $\binom n{p} + \binom n{p+1} = \binom{n+1}{p+1}$
- même dénominateur $(p+1)!(n+1-p)!$
- récurrence : $\sum_{k=p}^{n+1} \binom kp = \binom{n+1}{p+1} + \binom{n+1}p$

**loi binomiale (QCM)** (2)

- $\mathcal{B}(n, p)$ : $P(Y = k) = \binom nk p^k(1-p)^{n-k}$, $E = np$, $V = np(1-p)$
- $P(Y > 1) = 1 - P(Y = 0) - P(Y = 1)$

**p-listes, complémentaire** (2)

- $p$-listes de $n$ éléments : $n^p$
- « au moins un » = total $-$ « aucun » : $n^p - (n-1)^p$
- premier chiffre fixé non réutilisé : $(n-1)^{p-1}$

**équiprobabilité (deux dés)** (2)

- $|\Omega| = 36$
- « exactement un 6 » : $2 \times \frac16 \times \frac56 = \frac{10}{36}$
- « au moins un 6 » $= 1 - P(\text{aucun}) = 1 - \left(\frac56\right)^2$

**loi d'une variable aléatoire finie, espérance, variance** (2)

- $\sum_k P(X = k) = 1$
- $E(X) = \sum_k kP(X = k)$
- $V(X) = E\big((X - E(X))^2\big) = \sum_k (k - E(X))^2P(X = k)$
- König-Huygens : $V(X) = E(X^2) - E(X)^2$, $E(X^2) = \sum_k k^2P(X = k)$

**binôme de Newton, cardinal de $\mathcal{P}(E)$** (1)

- $(a+b)^n = \sum_{k=0}^n \binom nk a^kb^{n-k}$
- nombre de parties à $k$ éléments : $\binom nk$
- union disjointe : les cardinaux s'ajoutent
- $\sum_{k=0}^n \binom nk = (1+1)^n = 2^n = \mathrm{Card}\,\mathcal{P}(E)$

## APIS (intégrales)

**primitives usuelles et intégrales par primitive directe** (13)

- $\int x^n = \frac{x^{n+1}}{n+1}$
- $\int \frac1{x^2} = -\frac1x$
- $\int \frac1x = \ln|x|$
- $\int \sqrt x = \frac23x^{3/2}$
- $\int \frac1{\sqrt x} = 2\sqrt x$
- $\int e^x = e^x$
- $\int \sin = -\cos$
- $\int (1 + \tan^2) = \tan$
- $\int u'u^n = \frac{u^{n+1}}{n+1}$
- $\int \frac{u'}{u^2} = -\frac1u$
- $\int u'e^u = e^u$
- $\int \frac{u'}u = \ln|u|$
- $\int u'\cos u = \sin u$
- $\int f(ax+b) = \frac1aF(ax+b)$

**dériver une composée** (10)

- $(g \circ u)' = u' \times g' \circ u$
- $(e^u)' = u'e^u$
- $(\sqrt u)' = \frac{u'}{2\sqrt u}$
- $(u^n)' = nu'u^{n-1}$
- $(\ln u)' = \frac{u'}u$

**propriétés des primitives** (6)

- $F$ primitive de $f$ $\iff F' = f$
- primitives de $f$ : $F + c$, $c \in \mathbb{R}$
- linéarité : $aF + bG$ primitive de $af + bg$
- pas de règle pour le produit ni l'inverse
- toute fonction continue sur un intervalle admet une primitive

**IPP et changement de variable** (6)

- IPP : $\int_a^b uv' = [uv]_a^b - \int_a^b u'v$ ($u = \ln$, $v' = 1$)
- changement de variable : $x = \varphi(t)$, $dx = \varphi'(t)\,dt$, bornes transformées
- $t = \sqrt{1-x} \Rightarrow x = 1 - t^2$, $dx = -2t\,dt$
- $t = e^{-x} \Rightarrow dx = -\frac{dt}t$
- $\int \frac{dt}{1+t} = \ln(1+t)$
- $\int t^n = \frac{t^{n+1}}{n+1}$

**intégrales (primitive directe, IPP, changement de variable)** (6)

- $\int u'u = \frac{u^2}2$ ($u = \arctan$, $u' = \frac1{1+x^2}$)
- IPP : $\int uv' = [uv] - \int u'v$ avec $u = \ln x$, $v' = \frac1{x^2}$, $v = -\frac1x$
- $u = \ln t \Rightarrow du = \frac{dt}t$
- $u = \sqrt x \Rightarrow dx = 2u\,du$
- $\int \frac{du}{1+u^2} = \arctan u$
- $1 - u^2 = (1-u)(1+u)$

**IPP : polynôme × sin/cos** (5)

- IPP $\int_a^b uv' = [uv]_a^b - \int_a^b u'v$
- $u = x$, $u' = 1$
- $v' = \sin(kx)$, $v = -\frac{\cos(kx)}k$
- $\int \cos(kx) = \frac{\sin(kx)}k$
- $\cos\pi = -1$, $\cos\frac\pi2 = 0$, $\sin\frac\pi2 = 1$

**primitive directe $u'u^\alpha$, IPP, changement de variable affine vers arctan** (3)

- $\int u'u^\alpha = \frac{u^{\alpha+1}}{\alpha+1}$ ($\alpha = \frac12$ : $\frac23u^{3/2}$)
- IPP $\int uv' = [uv] - \int u'v$
- $\int e^{2x} = \frac{e^{2x}}2$
- $x = 2t + 1$, $dx = 2\,dt$, bornes transformées
- $\int \frac{dt}{1 + t^2} = \arctan t$
- $\arctan\sqrt3 = \frac\pi3$

**intégrale par primitive directe ($u'u^\alpha$, $u'/u$)** (2)

- $\int u'u^\alpha = \frac{u^{\alpha+1}}{\alpha+1}$ ($\alpha \neq -1$)
- $\int \frac{u'}u = \ln|u|$
- $\sqrt x = x^{1/2}$
- $x\sqrt x = x^{3/2}$
- $\ln 8 = 3\ln 2$

**primitives usuelles, IPP, changement de variable vers arctan** (2)

- primitives usuelles ($\int \frac{u'}{\sqrt u}$-type : $\int \frac{e^{\sqrt x}}{\sqrt x} = 2e^{\sqrt x}$, $\int \frac{u'}u = \ln|u|$)
- IPP : $\int_a^b uv' = [uv]_a^b - \int_a^b u'v$
- changement de variable $x = \varphi(t)$, $dt = \frac{dx}{x}$ pour $x = e^t$, bornes transformées
- $\int \frac{dx}{1+x^2} = \arctan x$
- $\arctan\sqrt3 = \frac\pi3$, $\arctan 1 = \frac\pi4$

**dérivée composée, double IPP, changement de variable** (2)

- $(\arctan u)' = \frac{u'}{1+u^2}$
- IPP : $\int_a^b uv' = [uv]_a^b - \int_a^b u'v$ (deux fois pour un polynôme de degré 2)
- $\int \cos\frac x2 = 2\sin\frac x2$, $\int \sin\frac x2 = -2\cos\frac x2$
- $u = e^x \Rightarrow dx = \frac{du}u$
- $\int \frac{du}{u+1} = \ln(u+1)$

**dérivée composée, changement de variable, IPP** (2)

- $(\sin u)' = u'\cos u$
- $(e^{3x})' = 3e^{3x}$
- changement de variable $t = \sqrt{x^2+3}$ : $t\,dt = x\,dx$
- IPP $u = \ln x$, $v' = \frac1{\sqrt x}$, $v = 2\sqrt x$
- $\int \frac{1}{\sqrt x} = 2\sqrt x$

**primitive $u'/u^n$, IPP trigonométrique, changement de variable racine vers arctan** (2)

- $\int \frac{u'}{u^n} = \frac{u^{1-n}}{1-n}$ ($n \neq 1$)
- IPP avec $v' = \sin(2x)$, $v = -\frac{\cos(2x)}2$
- $\int \cos(2x) = \frac{\sin(2x)}2$
- $t = \sqrt{x+2} \Rightarrow x = t^2 - 2$, $dx = 2t\,dt$
- $\int \frac{dt}{1+t^2} = \arctan t$
- $\arctan\sqrt3 = \frac\pi3$, $\arctan 1 = \frac\pi4$

**primitive $u'/u$, IPP trigonométrique, changement de variable vers arctan** (2)

- $\int \frac{u'}u = \ln|u|$ ($2x + 2 = \frac12(4x + 4)$)
- IPP $\int_a^b uv' = [uv]_a^b - \int_a^b u'v$, $\int \cos\frac x3 = 3\sin\frac x3$
- $t = \frac x{\sqrt3}$, $dx = \sqrt3\,dt$, $3 + x^2 = 3(1 + t^2)$
- $\int \frac{dt}{1+t^2} = \arctan t$

**primitive $u'/u^n$, IPP trigonométrique** (2)

- $\int \frac{u'}{u^2} = -\frac1u$
- IPP $\int uv' = [uv] - \int u'v$ avec $u = x$, $v' = \sin(3x)$, $v = -\frac{\cos(3x)}3$
- $\int \cos(3x) = \frac{\sin(3x)}3$

**primitive $u'\sqrt u$, théorème d'intégration par parties** (2)

- $\int u'u^{1/2} = \frac23u^{3/2}$ ($x = \frac12(x^2+1)'$)
- IPP : $u$, $v$ de classe $C^1$ sur $[a,b]$, $\int_a^b uv' = [uv]_a^b - \int_a^b u'v$
- preuve : $(uv)' = u'v + uv'$ intégré sur $[a,b]$

**intégrale comme aire, relation de Chasles** (1)

- $f \geqslant 0$ : $\int_a^b f$ = aire sous la courbe
- rectangle $L \times l$, triangle $\frac{b \times h}2$
- Chasles : $\int_a^c = \int_a^b + \int_b^c$
- continue sur $I$ $\Rightarrow$ admet une primitive

**Chasles, positivité, valeur moyenne** (1)

- $\int_b^a = -\int_a^b$
- Chasles
- $f \leqslant g$ sur $[a,b]$ $\Rightarrow \int_a^b f \leqslant \int_a^b g$
- valeur moyenne $\mu = \frac1{b-a}\int_a^b f$
- $\ln(2e^3) = \ln 2 + 3$, $\ln\sqrt2 = \frac12\ln2$

**dérivées usuelles** (1)

- $\cos' = -\sin$
- $\sin' = \cos$
- $\tan' = 1 + \tan^2 = \frac1{\cos^2}$
- $(x^n)' = nx^{n-1}$
- $(e^x)' = e^x$
- $(\ln x)' = \frac1x$

**IPP avec ln** (1)

- IPP : $\int_a^b uv' = [uv]_a^b - \int_a^b u'v$ avec $u = \ln x$, $u' = \frac1x$
- $\int \frac{dx}{x^2} = -\frac1x$
- $\ln e = 1$, $\ln 1 = 0$

## APIS (suites)

**comparaison et limites** (11)

- $u_n \leqslant v_n$ et $v_n \to -\infty \Rightarrow u_n \to -\infty$
- $u_n \leqslant v_n$ et $u_n \to +\infty \Rightarrow v_n \to +\infty$
- pour une limite finie, il faut deux gendarmes

**comparaison de suites ($\sim$, $o$, $O$)** (9)

- $u_n \sim v_n \iff \frac{u_n}{v_n} \to 1$
- $u_n = o(v_n) \iff \frac{u_n}{v_n} \to 0$
- $u_n = O(v_n) \iff \frac{u_n}{v_n}$ bornée
- convergente $\Rightarrow$ bornée, donc $\sim$ et $o$ impliquent $O$
- croissances comparées : $\frac{\ln n}{n^a} \to 0$, $\frac{n^a}{e^n} \to 0$
- $\frac{\sin n}{n} \to 0$
- factoriser par le terme dominant

**suites adjacentes** (8)

- adjacentes : $(u_n)$ croissante, $(v_n)$ décroissante, $v_n - u_n \to 0$
- alors elles convergent vers la même limite
- $\frac1{(n+1)!} = \frac1{n!} \cdot \frac1{n+1}$

**suite récurrente $u_{n+1} = f(u_n)$** (8)

- constante $\iff u_0 = f(u_0)$
- tableau de variations via $f'$
- $f$ croissante sur $I$ et $u_n \in I \Rightarrow f(a) < f(u_n) < f(b)$ (récurrence)
- signe de $u_{n+1} - u_n$
- monotone bornée $\Rightarrow$ convergente
- $\ell = f(\ell)$

**suites extraites** (6)

- toute suite extraite d'une suite convergente converge vers la même limite
- $(u_{6n})$ extraite de $(u_{2n})$ et de $(u_{3n})$
- $(u_{2n})$ et $(u_{2n+1})$ convergent vers $\ell$ $\Rightarrow (u_n) \to \ell$

**propriétés de suites avec quantificateurs** (5)

- bornée : $\exists m, M, \forall n, m \leqslant u_n \leqslant M$
- non bornée : $\forall m, M, \exists n, u_n < m$ ou $u_n > M$
- croissante : $\forall n, u_{n+1} \geqslant u_n$
- monotone : croissante ou décroissante

**suite récurrente $u_{n+1} = f(u_n)$, intervalles stables** (5)

- constante $\iff u_0 = f(u_0)$
- $I$ stable : $f(I) \subset I$, alors $u_n \in I$ par récurrence
- signe de $u_{n+1} - u_n = f(u_n) - u_n$
- monotone bornée $\Rightarrow$ convergente
- $f$ continue : $\ell = f(\ell)$

**suites adjacentes via une suite géométrique** (5)

- $w_{n+1} = qw_n \Rightarrow w_n = w_0q^n$
- $|q| < 1 \Rightarrow q^n \to 0$
- adjacentes : une croissante, l'autre décroissante, différence $\to 0$

**suites adjacentes ($\sum 1/k!$)** (5)

- adjacentes : $(u_n)$ croissante, $(v_n)$ décroissante, $v_n - u_n \to 0$
- $u_{n+1} - u_n = \frac1{(n+1)!}$
- $\frac1{n!} = \frac{n+1}{(n+1)!}$
- adjacentes $\Rightarrow$ convergentes
- convergente $\Rightarrow$ bornée

**limites usuelles de suites** (5)

- $\cos n$ diverge (suites extraites)
- $\ln(n^2 + n) \to +\infty$
- $|q| < 1 \Rightarrow q^n \to 0$
- $\frac1n \to 0$

**suites adjacentes, suites extraites $(u_{2n})$, $(u_{2n+1})$** (4)

- adjacentes : une croissante, l'autre décroissante, différence $\to 0$
- $u_{2n+2} - u_{2n}$ = deux termes de la somme
- $\frac1{a^2} - \frac1{b^2} = \frac{(b-a)(b+a)}{a^2b^2}$
- $(u_{2n})$ et $(u_{2n+1})$ même limite $\Rightarrow (u_n)$ converge

**démonstration de cours (convergente implique bornée)** (4)

- $u_n \to \ell$ : $\forall \varepsilon > 0, \exists N, \forall n \geqslant N, |u_n - \ell| < \varepsilon$
- bornée : $\exists M, \forall n, |u_n| \leqslant M$
- inégalité triangulaire $|u_n| \leqslant |u_n - \ell| + |\ell|$
- $M = \max(|u_0|, \dots, |u_{N-1}|, 1 + |\ell|)$
- contre-exemple $(-1)^n$

**suites extraites et divergence** (4)

- $\sin(k\pi) = 0$
- $\sin\left(2k\pi + \frac\pi3\right) = \frac{\sqrt3}2$
- si $u_n \to \ell$, toute suite extraite tend vers $\ell$
- deux suites extraites de limites différentes $\Rightarrow (u_n)$ diverge

**limite de $q^n$** (4)

- $q > 1$ : $q^n \to +\infty$
- $|q| < 1$ : $q^n \to 0$
- $q = 1$ : 1
- $q \leqslant -1$ : pas de limite

**théorème de la limite monotone** (4)

- croissante majorée $\Rightarrow$ convergente
- décroissante minorée $\Rightarrow$ convergente
- croissante non majorée $\Rightarrow +\infty$

**définitions sur les suites, exemples, limite de $q^n$** (4)

- croissante $\forall n, u_n \leqslant u_{n+1}$
- bornée $\exists M, \forall n, |u_n| \leqslant M$
- exemples $(-1)^n$, $1 - \frac1n$, $\cos n$
- $(q^n)$ converge $\iff -1 < q \leqslant 1$ (limite 0 si $|q| < 1$, 1 si $q = 1$)

**propriétés de suites et suites extraites (vrac)** (4)

- $q^n$ ($q > 1$) croissante non bornée
- $(-1)^n$ bornée divergente
- suite extraite d'une convergente converge vers la même limite
- $(u_{2n})$ et $(u_{2n+1})$ même limite $\Rightarrow (u_n)$ converge
- $(u_{3n})$, $(u_{3n+1})$ ne couvrent pas $(u_{3n+2})$

**monotonie et encadrement d'une somme** (3)

- $u_{n+1} - u_n$ : écrire les deux sommes et simplifier les termes communs ($\frac1{2n} + \frac1{2n+1} - \frac1n$)
- $n \leqslant k \leqslant 2n-1 \Rightarrow \frac1{2n-1} \leqslant \frac1k \leqslant \frac1n$
- somme de $n$ termes
- monotone bornée $\Rightarrow$ convergente
- passage à la limite dans les inégalités larges

**monotonie d'une suite, somme géométrique** (3)

- croissante : $\forall n, u_n \leqslant u_{n+1}$
- signe de $u_{n+1} - u_n$ (même dénominateur)
- $\sum_{k=p}^{n} q^k = q^p\frac{1 - q^{n-p+1}}{1 - q}$

**suite arithmético-géométrique** (2)

- $u_{n+1} = au_n + b$
- point fixe $\ell = a\ell + b$, $\ell = \frac{b}{1-a}$
- $v_n = u_n - \ell$ géométrique de raison $a$
- $v_n = v_0a^n$
- $u_n = (u_0 - \ell)a^n + \ell$

**comparaison de suites ($\sim$, $o$, $O$), développements** (2)

- $u_n \sim v_n \iff \frac{u_n}{v_n} \to 1$
- $o$ : quotient $\to 0$
- $O$ : quotient borné
- $o(\frac1{n^2}) = \frac{\varepsilon_n}{n^2}$, $\varepsilon_n \to 0$
- $u_n \sim$ premier terme non nul du développement
- croissances comparées $\frac{\ln n}n \to 0$

**suites extraites et gendarmes** (2)

- gendarmes : $a_n \leqslant u_n \leqslant b_n$, $a_n, b_n \to \ell \Rightarrow u_n \to \ell$
- $(u_{2n})$ et $(u_{2n+1})$ même limite $\Rightarrow (u_n)$ converge vers cette limite

**démonstration de cours (théorème des gendarmes)** (2)

- gendarmes : $\forall n \geqslant N_0$, $a_n \leqslant u_n \leqslant b_n$, $a_n \to \ell$, $b_n \to \ell \Rightarrow u_n \to \ell$
- définition $\forall \varepsilon, \exists N, n \geqslant N \Rightarrow |u_n - \ell| < \varepsilon$
- prendre $N = \max(N_0, N_1, N_2)$ : $\ell - \varepsilon < a_n \leqslant u_n \leqslant b_n < \ell + \varepsilon$

**suite homographique, suite auxiliaire géométrique** (2)

- récurrence pour le signe
- $\ell = f(\ell)$ si $f$ continue
- signe de $u_{n+1} - u_n$
- décroissante minorée $\Rightarrow$ convergente
- $v_{n+1} = qv_n \Rightarrow v_n = v_0q^n$
- $q > 1 \Rightarrow q^n \to +\infty$

**suites extraites $(u_{2n})$, $(u_{2n+1})$** (2)

- $\sum_{k=0}^{n-1} q^k = \frac{1 - q^n}{1 - q}$ ($q \neq 1$)
- $(-1)^{2n} = 1$, $(-1)^{2n+1} = -1$
- $(u_{2n})$ et $(u_{2n+1})$ même limite $\Rightarrow (u_n)$ converge

**somme des termes d'une suite géométrique** (2)

- $\sum_{k=0}^{n} q^k = \frac{1 - q^{n+1}}{1 - q}$ ($q \neq 1$)
- nombre de termes = $n + 1$

**énoncés de cours sur les suites (récurrence, gendarmes, majorée)** (2)

- récurrence : $P(n_0)$ et $\forall n \geqslant n_0, P(n) \Rightarrow P(n+1)$ donnent $\forall n \geqslant n_0, P(n)$
- gendarmes $v_n \leqslant u_n \leqslant w_n$, $v_n, w_n \to \ell \Rightarrow u_n \to \ell$
- majorée : $\exists M, \forall n, u_n \leqslant M$

**suites géométriques (terme général, somme, limite de $q^n$)** (2)

- $u_n = u_0q^n$
- $\sum_{k=p}^n q^k = q^p\frac{1 - q^{n-p+1}}{1 - q}$
- $\sum_{k=2}^8 \frac1{2^k} = \frac14 \cdot \frac{1 - (1/2)^7}{1/2}$
- $q^n \to +\infty$ ($q > 1$), $1$ ($q = 1$), $0$ ($|q| < 1$), pas de limite ($q \leqslant -1$)

**opérations sur les limites, formes indéterminées** (2)

- $\frac{\ell}{\ell'}$
- $\frac{\ell > 0}{0^+} = +\infty$
- $\frac{\pm\infty}{\ell'}$ selon le signe
- $\frac\infty\infty$ indéterminée
- $\frac{+\infty}{0^+} = +\infty$
- $\frac{0^-}{0^+}$ indéterminée
- factoriser par le terme dominant

**somme de suites convergentes ou divergentes** (2)

- somme de deux suites convergentes : convergente, $\lim(u_n + v_n) = \lim u_n + \lim v_n$
- convergente + divergente = divergente (par l'absurde, $v_n = w_n - u_n$)
- divergente + divergente : on ne peut rien dire (contre-exemples $n$ et $1 - n$)

**monotonie par quotient, majoration d'un produit, gendarmes** (2)

- $u_n > 0$ : $\frac{u_{n+1}}{u_n} \leqslant 1 \Rightarrow (u_n)$ décroissante
- $(n+1)! = (n+1)\,n!$
- décroissante minorée $\Rightarrow$ convergente
- $\frac{n!}{n^n} = \prod_{k=1}^n \frac kn$, facteurs $\leqslant 1$
- gendarmes

**encadrement d'une somme, gendarmes** (2)

- somme de $n$ termes : $n \times (\text{plus petit}) \leqslant \sum \leqslant n \times (\text{plus grand})$
- gendarmes : $a_n \leqslant u_n \leqslant b_n$, $a_n, b_n \to \ell \Rightarrow u_n \to \ell$
- $\frac{n^2}{n^2 + n} \to 1$

**sommes de termes consécutifs (suites arithmétiques et géométriques)** (2)

- arithmétique : $\sum_{k=p}^n u_k = (n - p + 1)\frac{u_p + u_n}2$ (nombre de termes × moyenne des extrêmes)
- géométrique, $q \neq 1$ : $\sum_{k=p}^n u_k = u_p\frac{1 - q^{n-p+1}}{1 - q}$ (premier terme × $\frac{1 - q^{\text{nb de termes}}}{1 - q}$)

**suite récurrente, calcul de termes** (1)

- $u_{n+1} = f(u_n, n)$ : calculer $u_1$ puis $u_2$
- géométrique $\iff u_{n+1} = qu_n$

**suite arithmétique** (1)

- $u_{n+1} = u_n + r$
- $u_n = u_p + (n - p)r$

**formes indéterminées** (1)

- formes indéterminées : $\infty - \infty$, $0 \times \infty$, $\frac\infty\infty$, $\frac00$
- $\frac{+\infty}{0^+} = +\infty$ et $\frac{0^+}{+\infty} = 0$ ne sont pas indéterminées

**limites usuelles (polynôme)** (1)

- limite d'un polynôme en $\pm\infty$ = limite du terme de plus haut degré

**limites usuelles (produit)** (1)

- $\frac1{\sqrt n} \to 0$, $\frac1{n^2} \to 0$
- produit : $(+\infty) \times \ell = -\infty$ si $\ell < 0$

**suites croissantes, contre-exemple** (1)

- croissante majorée converge (contre-exemple $-\frac1n$)
- croissante non majorée tend vers $+\infty$

**formes indéterminées, croissances comparées** (1)

- factoriser par le terme dominant
- $\frac{e^n}{n} \to +\infty$, $\frac{n}{e^n} \to 0$
- $q^n \to +\infty$ si $q > 1$, $\to 0$ si $|q| < 1$
- $\sqrt{n+1} = \sqrt n\sqrt{1 + \frac1n}$

**monotonie par quotient, récurrence, gendarmes** (1)

- $u_n > 0$ et $\frac{u_{n+1}}{u_n} \leqslant 1 \Rightarrow$ décroissante
- $\frac{(n+1)!}{n!} = n + 1$
- décroissante minorée $\Rightarrow$ convergente
- gendarmes $0 \leqslant u_n \leqslant v_n \to 0$
- $|q| < 1 \Rightarrow q^n \to 0$

**limite d'une fraction rationnelle** (1)

- en $\pm\infty$ : quotient des termes de plus haut degré, $\frac{x - 1}{x + 1} \sim \frac xx = 1$

## APIS (EDO)

**EDO linéaires 1er ordre (variation de la constante) et 2nd ordre** (13)

- $y' + a(x)y = 0 \Rightarrow y = ke^{-A(x)}$, $A' = a$
- solution générale = homogène + particulière
- variation de la constante $y_p = k(x)y_0(x)$
- $ay'' + by' + cy = 0$ : $ar^2 + br + c = 0$, racine double $r$ : $y = (k_1x + k_2)e^{rx}$
- second membre $P(x)e^{rx}$ : $y_p = Q(x)e^{rx}$

**démonstration de cours (solutions de $a(t)y' + b(t)y = 0$)** (4)

- $S_0 = \{t \mapsto ke^{-F(t)}, k \in \mathbb{R}\}$ avec $F$ primitive de $\frac ba$, $F' = \frac ba$
- $z = y_0e^F \Rightarrow z' = (y_0' + \frac bay_0)e^F = 0 \Rightarrow z$ constante (inclusion $\subset$)
- réciproque : dériver $ke^{-F}$ et reporter (inclusion $\supset$)
- $\int \frac{u'}u = \ln|u|$, $e^{-\alpha\ln u} = u^{-\alpha}$

**EDO 2nd ordre à coefficients constants avec second membre** (4)

- $ar^2 + br + c = 0$ : deux racines réelles $k_1e^{r_1x} + k_2e^{r_2x}$
- racine double $(k_1x + k_2)e^{rx}$
- complexes $\alpha \pm i\beta$ : $e^{\alpha x}(k_1\cos\beta x + k_2\sin\beta x)$
- second membre polynôme : $y_p$ polynôme de même degré
- second membre $P(x)e^{mx}$ : $y_p = Q(x)e^{mx}$ avec $\deg Q = \deg P$ (+1 si $m$ racine simple, +2 si racine double)
- solution générale = homogène + particulière

**EDO linéaire 1er ordre à coefficient variable, solution particulière constante** (3)

- $a(t)y' + b(t)y = c$ : homogène $y_0 = ke^{-\int \frac ba}$
- $e^{-\alpha\ln u} = u^{-\alpha}$
- solution particulière constante $y_p = \frac cb$ si $b$ constant ($y_p' = 0$)
- solution générale $y = y_p + y_0$

**EDO linéaires 1er ordre (variation de la constante, solution particulière trigonométrique)** (2)

- $a(t)y' + b(t)y = 0 \Rightarrow y_0 = ke^{-\int \frac ba}$
- solution générale = homogène + particulière
- variation de la constante : $y_p = k(t)y_0(t)$, les termes en $k$ s'annulent, reste $k'$
- $\int \frac1{2\sqrt t} = \sqrt t$
- second membre $\cos + \sin$ : $y_p = a\cos t + b\sin t$, identifier les coefficients de $\cos$ et $\sin$

**démonstration de cours (structure des solutions de $a(t)y' + b(t)y = c(t)$)** (2)

- $S_0 = \{t \mapsto ke^{-F(t)}\}$, $F' = \frac ba$
- $S = \{y_p + y_0,\ y_0 \in S_0\}$
- linéarité : $a(y_p + y_0)' + b(y_p + y_0) = c + 0$ (inclusion $\supset$)
- si $y \in S$ alors $y - y_p \in S_0$ (inclusion $\subset$)
- retrouver l'équation : $y_0 = ke^{-F}$ donne $\frac ba = F'$, puis $c = ay_p' + by_p$

**EDO 2nd ordre homogène (équation caractéristique, cours)** (2)

- $ay'' + by' + cy = 0$ : équation caractéristique $ar^2 + br + c = 0$
- deux racines réelles $r_1 \neq r_2$ : $y = k_1e^{r_1x} + k_2e^{r_2x}$
- racine double $r$ : $y = (k_1x + k_2)e^{rx}$
- racines complexes $\alpha \pm i\beta$ : $y = e^{\alpha x}(k_1\cos(\beta x) + k_2\sin(\beta x))$

**EDO linéaires 1er ordre (homogène, solution évidente, variation de la constante, condition initiale)** (2)

- $a(x)y' + b(x)y = 0 \Rightarrow y_0 = ke^{-\int \frac ba}$
- solution générale = $y_0 + y_p$
- solution évidente (constante, ou de la forme du second membre)
- variation de la constante : $y_p = k(x)y_0(x)$, il reste $a\,k'\,y_0 = c$
- condition initiale : remplacer pour trouver $k$
- $\int \frac{dx}{x\ln x} = \ln|\ln x|$, $\int \frac{dx}{1+x^2} = \arctan x$, $\int \tan = -\ln|\cos|$

**modélisation par une EDO du 1er ordre (crédit)** (2)

- $y' = ay + b$ ($a \neq 0$) : $y = ke^{at} - \frac ba$
- condition initiale $y(0) = y_0 \Rightarrow k = y_0 + \frac ba$
- $C(t) = \big(C_0 - \frac kr\big)e^{rt} + \frac kr$
- $C(T) = 0 \iff T = \frac1r\ln\frac{k}{k - rC_0}$
- $e^x = a \iff x = \ln a$

## APEF (fonctions)

**développements limités usuels et composés** (30)

- $e^u = \sum \frac{u^k}{k!}$
- $\cos u = 1 - \frac{u^2}2 + \frac{u^4}{24}$
- $\sin u = u - \frac{u^3}6$
- $\ln(1+u) = u - \frac{u^2}2 + \frac{u^3}3 - \frac{u^4}4$
- $\sqrt{1+u} = 1 + \frac u2 - \frac{u^2}8 + \frac{u^3}{16} - \frac{5u^4}{128}$
- $(1+u)^\alpha = 1 + \alpha u + \frac{\alpha(\alpha-1)}2u^2$
- produit tronqué
- composition : poser $u$, calculer $u^2$ à l'ordre voulu
- $1 + \cos 2x = 2\cos^2 x$

**développements limités, limite par équivalents** (23)

- en 0 : $e^x = 1 + x + \frac{x^2}2 + \frac{x^3}6 + o(x^3)$
- $\ln(1+x) = x - \frac{x^2}2 + o(x^2)$
- $\cos x = 1 - \frac{x^2}2 + o(x^3)$
- $\sin x = x - \frac{x^3}6 + o(x^3)$
- $\frac1{1-x} = 1 + x + x^2 + x^3 + o(x^3)$
- produit de DL tronqué à l'ordre
- $a^b = e^{b\ln a}$
- $f \sim g \Rightarrow$ même limite

**petit o, équivalents et développements limités (manipulation)** (16)

- $f = o(x^n) \iff f(x) = x^n\varepsilon(x)$, $\varepsilon \to 0$
- $o(x^3) \Rightarrow o(x^2)$ (pas l'inverse)
- $o(x^p) + o(x^q) = o(x^{\min(p,q)})$
- $f \sim$ premier terme non nul du DL
- $f \sim g \iff f - g = o(g)$
- $\lim \frac{f}{x^n} = a \neq 0 \iff f \sim ax^n$

**théorème des valeurs intermédiaires** (10)

- TVI : $f$ continue sur $[a,b]$, $k$ entre $f(a)$ et $f(b)$ $\Rightarrow \exists c \in [a,b]$, $f(c) = k$
- si $f(a)f(b) < 0$, $\exists c \in ]a,b[$, $f(c) = 0$

**petit o, grand O, équivalents (définitions et opérations)** (10)

- $f = o(g) \iff \frac fg \to 0$
- $f = O(g) \iff \frac fg$ bornée
- $f \sim g \iff \frac fg \to 1$
- $f \sim \ell \neq 0 \iff f \to \ell$ (faux pour $\ell = 0$)
- $\sim$ compatible avec produit, quotient, puissance fixe, valeur absolue
- PAS avec somme, exponentielle, logarithme
- $o(x^p) + o(x^q) = o(x^{\min(p,q)})$ en 0
- $o(x^p) \times o(x^q) = o(x^{p+q})$
- croissances comparées : $\ln x = o(x)$ et $x = o(e^x)$ en $+\infty$

**équivalents simples (polynômes, fonctions usuelles, produits)** (6)

- polynôme : équivalent au terme de plus bas degré en 0, de plus haut degré en $\pm\infty$
- $x^\alpha = o(x^\beta)$ en $+\infty$ $\iff \alpha < \beta$, en 0 $\iff \alpha > \beta$
- en 0 : $\sin x \sim x$, $e^x - 1 \sim x$, $\ln(1+x) \sim x$, $e^x \sim 1$
- équivalent d'un produit ou d'un quotient = produit ou quotient des équivalents
- pour une somme, revenir au terme dominant

**continuité et dérivabilité** (3)

- dérivable $\Rightarrow$ continue (réciproque fausse : $|x|$ en 0)
- continue en $a$ $\iff \lim_a f = f(a)$
- tangente verticale : $\frac{f(x) - f(a)}{x - a} \to \pm\infty$, non dérivable

**limites usuelles de fonctions** (2)

- $\lim_{-\infty} e^x = 0$, $\lim_{+\infty} e^x = +\infty$
- $\lim_{0^+} \ln x = -\infty$, $\lim_{+\infty} \ln x = +\infty$

**limite d'une fraction rationnelle** (2)

- en $\pm\infty$ : quotient des termes de plus haut degré, $\frac{x - 1}{x + 1} \sim \frac xx = 1$

**cercle trigonométrique, valeurs remarquables, fonction tangente** (2)

- $\cos(\pi - x) = -\cos x$
- $\cos(\frac\pi2 + x) = -\sin x$
- $\sin(\frac\pi2 - x) = \cos x$
- table $0, \frac\pi6, \frac\pi4, \frac\pi3, \frac\pi2$ : $\cos = 1, \frac{\sqrt3}2, \frac{\sqrt2}2, \frac12, 0$
- réduire modulo $2\pi$
- $\tan = \frac{\sin}{\cos}$ sur $\mathbb{R} \setminus \{\frac\pi2 + k\pi\}$
- $\tan' = \frac1{\cos^2} = 1 + \tan^2$
- $(\frac uv)' = \frac{u'v - uv'}{v^2}$

**fonction logarithme (propriétés, équations, limites, composées)** (2)

- $e^{\ln x} = x$ ($x > 0$), $\ln(e^x) = x$
- $\ln 1 = 0$, $\ln e = 1$
- $\ln(ab) = \ln a + \ln b$, $\ln\frac1a = -\ln a$, $\ln\frac ab = \ln a - \ln b$, $n\ln a = \ln(a^n)$
- $\ln$ croissante : $\ln X < 1 \iff 0 < X < e$
- $\frac{\ln x}x \to 0$, $x\ln x \to 0$ en $0^+$
- $(\ln u)' = \frac{u'}u$, $(\sqrt u)' = \frac{u'}{2\sqrt u}$

**asymptotes** (1)

- $\lim_{x \to a} f = \pm\infty$ : asymptote verticale $x = a$
- $\lim_{\pm\infty} f = \ell$ : asymptote horizontale $y = \ell$
- $\frac{4}{\sqrt x} \to +\infty$ en $0^+$, $\to 0$ en $+\infty$

**formes indéterminées** (1)

- formes indéterminées : $\infty - \infty$, $0 \times \infty$, $\frac\infty\infty$, $\frac00$
- $\frac{+\infty}{0^+} = +\infty$ et $\frac{0^+}{+\infty} = 0$ ne sont pas indéterminées

**croissances comparées** (1)

- $\lim_{-\infty} xe^x = 0$
- $\lim_{+\infty} \frac{e^x}{x^n} = +\infty$
- $\lim_{0^+} x\ln x = 0$
- $\lim_{+\infty} \frac{\ln x}{x} = 0$

**limites par comparaison** (1)

- $f \leqslant g$ et $g \to -\infty \Rightarrow f \to -\infty$
- majorer par une fonction qui tend vers $+\infty$ ne donne rien

**continuité en un point** (1)

- $f$ continue en $a$ $\iff \lim_{x \to a} f(x) = f(a)$
- fonctions usuelles continues sur leur domaine
- $\ln$ non définie en 0

**trigonométrie (parité, signe de sin)** (1)

- $\sin(-x) = -\sin x$ (impaire), $\cos(-x) = \cos x$ (paire)
- $\sin \geqslant 0$ sur $[0, \pi]$, $\leqslant 0$ sur $[\pi, 2\pi]$

**valeurs remarquables de cos et sin** (1)

- $\cos\frac\pi6 = \frac{\sqrt3}2$, $\cos\frac\pi4 = \frac{\sqrt2}2$, $\cos\frac\pi3 = \frac12$, $\cos\frac\pi2 = 0$
- $\sin\frac\pi6 = \frac12$, $\sin\frac\pi3 = \frac{\sqrt3}2$, $\sin\frac\pi2 = 1$
- $\cos(\pi - x) = -\cos x$

**formules trigonométriques** (1)

- $\cos(\pi - x) = -\cos x$
- $\cos(\pi + x) = -\cos x$
- $\sin\left(\frac\pi2 - x\right) = \cos x$
- $\cos^2 x + \sin^2 x = 1$

**fonction tangente** (1)

- $\tan = \frac{\sin}{\cos}$, définie sur $\mathbb{R} \setminus \{\frac\pi2 + k\pi\}$
- $\tan' = 1 + \tan^2 = \frac1{\cos^2}$

**coefficient directeur d'une droite** (1)

- $m = \frac{f(b) - f(a)}{b - a} = \frac{y_B - y_A}{x_B - x_A}$

**limites de fonctions (croissances comparées, comparaison, asymptotes)** (1)

- $\lim_{+\infty} xe^{-x} = 0$
- $-1 \leqslant \cos \leqslant 1$
- $f \geqslant g$ et $g \to +\infty \Rightarrow f \to +\infty$
- fraction rationnelle : factoriser par le terme dominant
- $\frac{a}{0^\pm} = \pm\infty$ selon les signes
- $\lim_a f = \pm\infty$ : asymptote $x = a$
- $\lim_{\pm\infty} f = \ell$ : asymptote $y = \ell$

**continuité d'une fonction définie par morceaux** (1)

- continue en $a$ $\iff \lim_{a^-} f = \lim_{a^+} f = f(a)$
- continue à gauche : $\lim_{a^-} f = f(a)$
- fonctions usuelles continues sur leur domaine

**étude de fonction (parité, variations, asymptote, tangente)** (1)

- paire : $f(-x) = f(x)$
- $(e^u)' = u'e^u$
- signe de $f'$ donne les variations
- tangente en $a$ : $y = f'(a)(x - a) + f(a)$
- $\lim_{+\infty} e^{-x^2/2} = 0$ : asymptote $y = 0$
- paire : symétrie par rapport à l'axe des ordonnées

**parité, périodicité, TVI pour une fonction trigonométrique** (1)

- $\sin(-x) = -\sin x$, $\cos(-x) = \cos x$
- $\sin$, $\cos$ $2\pi$-périodiques
- $\cos\frac{2\pi}3 = -\frac12$, $\sin\frac{2\pi}3 = \frac{\sqrt3}2$
- TVI : $f$ continue et $f(a)f(b) < 0 \Rightarrow \exists \alpha \in ]a,b[$, $f(\alpha) = 0$

**fonction arctan (définition, dérivée, valeurs remarquables)** (1)

- $\arctan : \mathbb{R} \to \left]-\frac\pi2, \frac\pi2\right[$, réciproque de $\tan$
- $\tan(\arctan x) = x$
- $\arctan'(x) = \frac1{1+x^2}$
- $\tan 0 = 0$, $\tan\frac\pi6 = \frac1{\sqrt3}$, $\tan\frac\pi4 = 1$, $\tan\frac\pi3 = \sqrt3$
- $\tan$ impaire

## APEF (polynômes)

**divisibilité de polynômes, multiplicité, factorisation dans $\mathbb{R}[X]$ et $\mathbb{C}[X]$** (25)

- $P(a) = 0 \iff X - a \mid P$
- racine d'ordre $\geqslant 2$ $\iff P(a) = P'(a) = 0$
- ordre exactement $m$ : $P^{(m)}(a) \neq 0$
- $(X - a)^m \mid P$, $(X - a)^{m+1} \nmid P$
- $X^2 + 1 = (X - i)(X + i)$
- $\Delta < 0 \Rightarrow$ irréductible dans $\mathbb{R}[X]$

**degré, division euclidienne de polynômes, racine** (16)

- $\deg(A+B) \leqslant \max(\deg A, \deg B)$
- $\deg(AB) = \deg A + \deg B$
- $\exists!\,(Q,R)$, $A = BQ + R$, $\deg R < \deg B$
- $\alpha$ racine $\iff A(\alpha) = 0 \iff X - \alpha \mid A$

**multiplicité d'une racine d'un polynôme** (9)

- $\alpha$ racine d'ordre $m$ $\iff P(\alpha) = P'(\alpha) = \dots = P^{(m-1)}(\alpha) = 0$ et $P^{(m)}(\alpha) \neq 0$
- $(X^n)' = nX^{n-1}$

**divisibilité de polynômes, multiplicité d'une racine** (8)

- $(X-a)(X-b) \mid P \iff P(a) = P(b) = 0$ ($a \neq b$)
- $\alpha$ racine d'ordre $m$ $\iff P(\alpha) = \dots = P^{(m-1)}(\alpha) = 0$, $P^{(m)}(\alpha) \neq 0$
- $(X^n)' = nX^{n-1}$

**décomposition en éléments simples** (8)

- si $\deg N \geqslant \deg D$ : division euclidienne, partie entière
- pôle simple $a$ : $\frac{c}{X - a}$ avec $c = \left[(X - a)F\right](a)$
- pôle double : $\frac{c_1}{X-a} + \frac{c_2}{(X-a)^2}$
- facteur irréductible $X^2 + 1$ : $\frac{bX + c}{X^2 + 1}$
- identifier en évaluant (ex. $X = 0$) ou par limite de $xF(x)$ en $+\infty$

**divisibilité et reste de division euclidienne de polynômes** (7)

- $A = BQ + R$, $\deg R < \deg B$
- $(X-a)(X-b) \mid P \iff P(a) = P(b) = 0$ ($a \neq b$)
- reste par $(X-a)(X-b)$ : $R = \alpha X + \beta$ avec $R(a) = P(a)$, $R(b) = P(b)$
- reste par $(X-a)^2$ : $R(a) = P(a)$, $R'(a) = P'(a)$

**divisibilité de polynômes par les racines** (5)

- $X - a \mid P \iff P(a) = 0$
- $(X-a)(X-b) \mid P \iff P(a) = P(b) = 0$ ($a \neq b$)
- $(X-a)^2 \mid P \iff P(a) = P'(a) = 0$

**racine multiple d'un polynôme à paramètre** (3)

- $\alpha$ racine au moins double $\iff Q(\alpha) = Q'(\alpha) = 0$
- $((X+1)^7)' = 7(X+1)^6$
- $(X+1)^6 = X^6 \iff X + 1 = \pm X$

**factorisation d'un polynôme dans $\mathbb{R}[X]$** (2)

- $P(a) = 0 \iff X - a \mid P$
- division euclidienne $A = BQ + R$
- $\Delta = b^2 - 4ac < 0 \Rightarrow aX^2 + bX + c$ irréductible dans $\mathbb{R}[X]$

**formule de Taylor pour les polynômes** (2)

- $P = \sum a_kX^k \Rightarrow a_k = \frac{P^{(k)}(0)}{k!}$
- $P(X) = \sum_{k=0}^{\deg P} \frac{P^{(k)}(0)}{k!}X^k$
- en $a$ : $P(X) = \sum_{k=0}^{\deg P} \frac{P^{(k)}(a)}{k!}(X - a)^k$
- $(X^n)^{(k)} = \frac{n!}{(n-k)!}X^{n-k}$

**division euclidienne et primitive d'une fraction rationnelle** (2)

- $A = BQ + R$, $\deg R < \deg B$ $\Rightarrow \frac AB = Q + \frac RB$
- $\int x^n = \frac{x^{n+1}}{n+1}$
- $\int \frac{u'}u = \ln|u|$
- $\int \frac{dx}{1+x^2} = \arctan x$

## EV

**sous-espaces, intersection, somme directe** (35)

- $\mathrm{Vect}(u)$ : droite si $u \neq 0$
- plan $ax + by + cz = 0$ : exprimer $z$, $G = \mathrm{Vect}(u, v)$
- $u \in F \cap G$ : paramétrer par $F$ puis injecter l'équation de $G$
- Grassmann $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$
- $F \oplus G = E \iff F \cap G = \{0\}$ et $\dim F + \dim G = \dim E$

**familles libres, génératrices, bases** (27)

- libre : $\sum \lambda_ie_i = 0 \Rightarrow \forall i, \lambda_i = 0$
- génératrice : tout vecteur est combinaison linéaire
- base = libre + génératrice
- $\dim \mathbb{R}_n[X] = n + 1$
- en dimension $n$ : plus de $n$ vecteurs $\Rightarrow$ liée, moins de $n$ $\Rightarrow$ non génératrice, $n$ vecteurs libres $\Rightarrow$ base
- degrés échelonnés $\Rightarrow$ libre

**familles libres, génératrices, bases ; coordonnées** (24)

- libre : $\sum \lambda_ie_i = 0 \Rightarrow \lambda_i = 0$
- en dimension $n$, une famille libre de $n$ vecteurs est une base
- plus de $n$ vecteurs $\Rightarrow$ liée
- coordonnées : résoudre $P = \alpha Q_1 + \beta Q_2 + \gamma Q_3$ en identifiant les coefficients

**reconnaître un sous-espace vectoriel** (24)

- sev : contient 0, stable par addition et multiplication par un scalaire
- contre-exemple $\lambda u \notin E$
- équation non linéaire ($z^2$) $\Rightarrow$ en général pas un sev
- $\mathrm{Vect}(\dots)$ est toujours un sev

**sous-espaces engendrés, inclusion, dimension** (10)

- $P \in \mathrm{Vect}(u_1, \dots) \iff P$ combinaison linéaire des $u_i$
- $F \subset G$ si les générateurs de $F$ sont dans $G$
- famille génératrice libre = base, $\dim$ = cardinal

**axiomes d'un espace vectoriel (loi externe non standard)** (9)

- $\mathbb{R}$-ev : $(E,+)$ groupe commutatif
- $1.u = u$
- $\alpha.(\beta.u) = (\alpha\beta).u$
- $(\alpha + \beta).u = \alpha.u + \beta.u$
- $\alpha.(u + v) = \alpha.u + \alpha.v$
- un seul axiome en défaut (contre-exemple chiffré) suffit pour conclure que ce n'est pas un ev

**sous-espaces supplémentaires (fonctions paires et impaires)** (5)

- sev : non vide, stable par $\lambda f + g$
- $F \oplus G = E \iff F \cap G = \{0\}$ et $F + G = E$
- $f = \frac{f(x) + f(-x)}2 + \frac{f(x) - f(-x)}2$
- paire et impaire $\Rightarrow f = 0$

**écrire un sous-espace sous forme de Vect (système linéaire)** (4)

- résoudre le système par pivot de Gauss
- exprimer les inconnues principales en fonction des inconnues libres
- factoriser chaque paramètre : $\{(x,y,z)\} = \{t\,u,\ t \in \mathbb{R}\} = \mathrm{Vect}(u)$
- nombre de paramètres libres = dimension

**vecteurs du plan, combinaisons linéaires (dessin)** (2)

- $(x,y) + (x',y') = (x + x', y + y')$
- $\alpha(x,y) = (\alpha x, \alpha y)$
- $\{\alpha u\}$ : droite vectorielle dirigée par $u \neq 0$
- $\{\alpha u + \beta v\}$ avec $u$, $v$ non colinéaires : le plan $\mathbb{R}^2$ (un plan vectoriel dans $\mathbb{R}^3$)
- relation de Chasles pour construire $u + v$

## ALM

**noyau, image, rang d'une application linéaire** (45)

- linéaire : $f(\lambda u + v) = \lambda f(u) + f(v)$
- $\mathrm{Ker} f$ : résoudre $f(x) = 0$
- théorème du rang $\dim E = \dim\mathrm{Ker} f + \mathrm{rg} f$
- $\mathrm{rg} f = \dim F \Rightarrow \mathrm{Im} f = F$ (surjective)
- $\mathrm{Im} f = \mathrm{Vect}(f(e_1), \dots, f(e_n))$

**projecteur, noyau et image** (21)

- projecteur $\iff f \circ f = f$
- $E = \mathrm{Ker} f \oplus \mathrm{Im} f$
- $f = id$ sur $\mathrm{Im} f$, $0$ sur $\mathrm{Ker} f$
- matrice dans une base adaptée $\mathrm{diag}(0, \dots, 0, 1, \dots, 1)$

**matrice d'une application linéaire** (19)

- colonne $j$ = coordonnées de $f(e_j)$ dans la base d'arrivée
- base canonique de $\mathbb{R}_2[X]$ : $(1, X, X^2)$
- de $\mathcal{M}_2(\mathbb{R})$ : $E_{11}, E_{12}, E_{21}, E_{22}$
- taille (dim arrivée) $\times$ (dim départ)

**inverse d'une matrice** (15)

- $A$ inversible $\iff \det A \neq 0$
- pivot de Gauss sur $(A \mid I_n) \to (I_n \mid A^{-1})$
- ou $A^{-1} = \frac1{\det A}{}^t\mathrm{Com}(A)$
- vérifier $AA^{-1} = I_n$
- $2 \times 2$ : $\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1} = \frac1{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$

**changement de base, formule $Y = AX$** (14)

- $X = PX'$, $P$ = matrice de passage (colonnes = nouveaux vecteurs dans l'ancienne base)
- $X' = P^{-1}X$
- $f(e_j) = \sum_i a_{i,j}\varepsilon_i$
- coordonnées de l'image $Y = AX$
- inverse $2 \times 2$ : $\frac1{ad - bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$

**application linéaire (caractérisation)** (12)

- $f$ linéaire $\Rightarrow f(0) = 0$ et $f(2x) = 2f(x)$ (conditions nécessaires)
- réciproquement vérifier $f(\lambda x + y) = \lambda f(x) + f(y)$
- les applications linéaires de $\mathbb{R}$ dans $\mathbb{R}$ sont $x \mapsto bx$

**noyau, image, injectivité, surjectivité (cours)** (9)

- sous-espace : contient 0 et stable par $\alpha u + v$
- $f(\alpha u + v) = \alpha f(u) + f(v)$
- injective $\iff \mathrm{Ker} f = \{0\}$
- surjective $\iff \mathrm{Im} f = F$

**noyau, image, rang ; matrice d'une application linéaire** (9)

- $\mathrm{Ker} f$ : résoudre $f(P) = 0$
- théorème du rang $\dim E = \dim\mathrm{Ker} f + \dim\mathrm{Im} f$
- injective $\iff \mathrm{Ker} = \{0\}$
- $\dim\mathrm{Im} = \dim F \Rightarrow$ surjective
- colonne $j$ = coordonnées de $f(e_j)$ dans la base d'arrivée

**opérations matricielles, produit, inverse** (8)

- $(\lambda A + \mu B)_{ij} = \lambda a_{ij} + \mu b_{ij}$
- produit $AB$ défini si (colonnes de $A$) = (lignes de $B$), taille $n \times p$ par $p \times q$ donne $n \times q$
- $(AB)_{ij} = \sum_k a_{ik}b_{kj}$
- inverse par pivot de Gauss
- vérification $AA^{-1} = I$

**application linéaire définie par l'image d'une base** (8)

- linéarité : $f(\alpha u + \beta v) = \alpha f(u) + \beta f(v)$
- $u = \sum x_ie_i \Rightarrow f(u) = \sum x_if(e_i)$
- une application linéaire est entièrement déterminée par l'image d'une base
- deux applications linéaires égales sur une base (ou une famille génératrice) sont égales
- si les vecteurs donnés sont liés, les images doivent vérifier la même relation
- s'ils n'engendrent pas l'espace, $f$ n'est pas déterminée

**injectivité et noyau** (7)

- $f$ linéaire : $f(0) = 0$, $f(x) - f(y) = f(x - y)$
- $f$ injective $\iff \mathrm{Ker} f = \{0\}$

**changement de base, diagonalisation, puissance d'une matrice** (7)

- $\mathrm{Mat}_{\mathcal{B}'}(f) = P^{-1}AP$ avec $P = \mathrm{Mat}_{\mathcal{B}', \mathcal{B}}(id)$ (colonnes = vecteurs de $\mathcal{B}'$ dans $\mathcal{B}$)
- $f(u_i) = \lambda_iu_i \Rightarrow D = \mathrm{diag}(\lambda_i)$
- $D^n = \mathrm{diag}(\lambda_i^n)$
- $A = PDP^{-1} \Rightarrow A^n = PD^nP^{-1}$

**inverse d'une matrice, application linéaire associée** (7)

- pivot de Gauss sur $AU = V$
- $A$ inversible $\iff f$ bijective, $\mathrm{Mat}(f^{-1}) = A^{-1}$
- colonnes de $A$ = images des vecteurs de la base de départ
- $g(aX^2 + bX + c) = ag(X^2) + bg(X) + cg(1)$

**noyau et image d'un endomorphisme (inclusions)** (6)

- $\mathrm{Ker} f = \{x, f(x) = 0\}$
- $\mathrm{Im} f = \{f(x)\}$
- $f(0) = 0$
- $x \in \mathrm{Ker} f \Rightarrow f^2(x) = f(0) = 0$
- $f^2(x) = f(f(x)) \in \mathrm{Im} f$
- double implication par éléments

**théorème du rang (conséquences : injectif, surjectif, bijectif)** (4)

- théorème du rang : $\dim E = \dim \mathrm{Ker}(f) + \dim \mathrm{Im}(f)$
- injective $\iff \mathrm{Ker}(f) = \{0_E\}$
- surjective $\iff \mathrm{Im}(f) = F$
- si $\dim E = \dim F$ : injective $\iff$ surjective $\iff$ bijective
- $\dim E > \dim F \Rightarrow$ pas injective
- $\dim E < \dim F \Rightarrow$ pas surjective
- un polynôme de degré $\leqslant n$ ayant $n + 1$ racines est nul

**puissance d'une matrice (binôme, nilpotente)** (3)

- $J$ nilpotente : $J^3 = 0$
- si $AB = BA$ : $(A + B)^n = \sum_k \binom nk A^kB^{n-k}$
- $I$ commute avec tout
- $(I + N)^n = I + nN + \binom n2 N^2$ si $N^3 = 0$

**symétrie par rapport à un sous-espace** (3)

- $E = F \oplus G$ : $u = v + w$ unique
- projection sur $F$ : $u \mapsto v$
- symétrie par rapport à $F$ parallèlement à $G$ : $u \mapsto v - w$, $s \circ s = id$

**puissance d'une matrice par polynôme annulateur** (2)

- $J^2 - J - 2I = 0 \Rightarrow J(J - I) = 2I$, donc $J^{-1} = \frac12(J - I)$
- $JK = I \Rightarrow J^{-1} = K$
- division euclidienne $X^n = (X^2 - X - 2)Q + aX + b$
- évaluer en $2$ et $-1$ (racines) : $2^n = 2a + b$, $(-1)^n = -a + b$
- substituer $J$ : $J^n = aJ + bI$

**endomorphisme de dérivation : base, matrice, puissance** (2)

- famille libre : $\sum \lambda_if_i = 0 \Rightarrow \lambda_i = 0$ (diviser par $e^{2x}$, polynôme nul)
- $d$ linéaire et $d(F) \subset F$
- colonne $j$ = coordonnées de $d(f_j)$
- $(e^{2x})^{(n)} = 2^ne^{2x}$
- Leibniz $(uv)^{(n)} = \sum_k C_n^ku^{(k)}v^{(n-k)}$
- $\mathrm{Mat}(d^n) = A^n$

**calcul matriciel, transposée** (2)

- $({}^tA)_{i,j} = a_{j,i}$
- ${}^t(AB) = {}^tB\,{}^tA$
- ${}^tUU = \sum x_i^2$ (scalaire)
- $U\,{}^tU$ matrice $n \times n$
- associativité $(AB)C = A(BC)$
- produit $(AB)_{ij} = \sum_k a_{ik}b_{kj}$

**application linéaire dans une base adaptée (lecture graphique)** (2)

- $u = \alpha v + \beta w$ (coordonnées dans $\mathcal{B}$)
- $f(u) = \alpha f(v) + \beta f(w)$
- colonnes de $A$ : $f(v) = -v$, $f(w) = 2w$
- décomposer $u$ graphiquement par parallèles à $F$ et $G$

## HP (arithmétique)

**équation diophantienne $ax+by=c$ (Euclide, Gauss)** (16)

- Euclide : $a = bq + r$, $a \wedge b = b \wedge r$
- solutions $\iff (a \wedge b) \mid c$
- diviser par $d = a \wedge b$
- remonter Euclide : $au_0 + bv_0 = d$ puis multiplier par $c/d$
- Gauss : $a \mid bc$ et $a \wedge b = 1 \Rightarrow a \mid c$
- $a(x - x_0) = -b(y - y_0)$ donne $x = x_0 + \frac{b}{d}k$, $y = y_0 - \frac{a}{d}k$, $k \in \mathbb{Z}$
- vérifier la réciproque

**congruences (définition, opérations)** (9)

- $a \equiv b\,[n] \iff n \mid a - b$
- compatibilité avec $+$, $\times$, puissances
- $ab - cd = a(b - d) + d(a - c)$
- réduire chaque nombre modulo $n$
- reste dans $[\![0, n-1]\!]$

**division euclidienne dans $\mathbb{Z}$** (8)

- $\exists!\,(q, r)$, $a = bq + r$, $0 \leqslant r < |b|$
- ajuster : $a = bq + r = b(q+1) + (r - b)$
- pour $-a$ : $-a = b(-q) - r = b(-q-1) + (b - r)$

**divisibilité et division euclidienne (vrai/faux)** (8)

- $a \mid b \iff \exists k \in \mathbb{Z}, b = ka$
- $a \mid b$ et $b \mid a \Rightarrow a = \pm b$
- $a \mid b$, $a \mid c \Rightarrow a \mid bu + cv$
- contre-exemple $2 \mid 4$, $4 \mid 4$, $8 \nmid 4$
- $a \mid bc \not\Rightarrow a \mid b$ ou $a \mid c$ ($6 \mid 2 \times 3$)
- division euclidienne $0 \leqslant r < |b|$

**Bézout, Euclide, lemme de Gauss (démonstrations)** (7)

- Bézout : $\exists (u,v), au + bv = a \wedge b$
- $a \wedge b = 1 \iff \exists (u,v), au + bv = 1$
- Euclide : $a = bq + r$, remonter les divisions
- Gauss : $a \mid bc$, $a \wedge b = 1 \Rightarrow a \mid c$
- $a \mid c$, $b \mid c$, $a \wedge b = 1 \Rightarrow ab \mid c$

**petit théorème de Fermat, reste d'une puissance** (6)

- Fermat : $p$ premier, $p \nmid a \Rightarrow a^{p-1} \equiv 1\,[p]$
- $a \equiv b\,[n] \Rightarrow a^k \equiv b^k\,[n]$
- $a^{q(p-1)+r} \equiv a^r\,[p]$

**Bézout (énoncé et applications)** (6)

- Bézout : $\exists (u,v), au + bv = a \wedge b$
- $a \wedge b = 1 \iff \exists (u,v), au + bv = 1$
- élever au carré / multiplier une relation de Bézout
- $2 \times (2n+1) \cdot 1 - \dots$ : $1 \cdot (2n+1) - 2 \cdot n = 1$
- fraction irréductible $\iff$ numérateur et dénominateur premiers entre eux

**PGCD par facteurs premiers, Fermat** (6)

- décomposition en facteurs premiers
- $a \wedge b = \prod p^{\min}$
- Fermat : $p$ premier, $p \nmid a \Rightarrow a^{p-1} \equiv 1\,[p]$
- premier : exactement deux diviseurs positifs

**congruences, reste d'une puissance** (5)

- $a \equiv b\,[n] \Rightarrow a^k \equiv b^k\,[n]$
- chercher la période : $a^p \equiv 1\,[n]$
- division euclidienne de l'exposant $N = pq + r$ : $a^N = (a^p)^q a^r$
- le reste est dans $[\![0, n-1]\!]$

**Bézout (énoncé), diviseurs communs et PGCD** (5)

- Bézout : $a \wedge b = 1 \iff \exists (u,v), au + bv = 1$
- corollaire : $\exists (u,v), au + bv = a \wedge b$
- $d \mid a$ et $d \mid b \Rightarrow d \mid au + bv$
- transitivité de $\mid$

**congruences, Fermat, reste d'une puissance** (5)

- reste de la division par 4 : $r \in \{0,1,2,3\}$
- $a \equiv b\,[n] \Rightarrow a^k \equiv b^k\,[n]$
- Fermat : $p$ premier, $p \nmid a \Rightarrow a^{p-1} \equiv 1\,[p]$
- $a^{q(p-1)+r} \equiv a^r\,[p]$

**décomposition en facteurs premiers, diviseurs communs** (5)

- $a \wedge b = \prod p^{\min(\alpha_p, \beta_p)}$
- $d \mid a$ et $d \mid b \iff d \mid a \wedge b$ (Bézout)
- diviseurs de $\prod p_i^{\gamma_i}$ : $\prod p_i^{\delta_i}$, $0 \leqslant \delta_i \leqslant \gamma_i$
- nombre : $\prod(\gamma_i + 1)$

**décomposition en facteurs premiers, PGCD** (4)

- critères de divisibilité (2, 3 : somme des chiffres, 5, 11)
- $a \wedge b = \prod p^{\min(\alpha_p, \beta_p)}$

**congruences et Fermat, divisibilité** (4)

- $a \equiv b\,[n] \Rightarrow a^k \equiv b^k\,[n]$
- Fermat : $p$ premier $\Rightarrow a^p \equiv a\,[p]$
- $a^{mn+r} = (a^m)^n a^r$
- $n \mid A \iff A \equiv 0\,[n]$

**PGCD et Bézout (démonstration)** (3)

- $d \mid a$ et $d \mid b$ : $a = da'$, $b = db'$
- $a' \wedge b' = 1$
- Bézout : $a' \wedge b' = 1 \iff \exists (u,v), a'u + b'v = 1$
- multiplier par $d$

**Bézout ($a+b$ et $ab$ premiers entre eux)** (3)

- Bézout : $a \wedge b = 1 \iff \exists (u,v) \in \mathbb{Z}^2, au + bv = 1$
- $(au + bv)^2 = 1$
- $a^2u^2 + b^2v^2 = (a+b)(au^2 + bv^2) - ab(u^2 + v^2)$

**décomposition en facteurs premiers, nombre de diviseurs, PGCD** (3)

- diviseur de $\prod p_i^{\alpha_i}$ : $\prod p_i^{\beta_i}$, $0 \leqslant \beta_i \leqslant \alpha_i$
- nombre de diviseurs $\prod(\alpha_i + 1)$
- $a \wedge b = \prod p^{\min}$

**petit théorème de Fermat (énoncé, démonstration, application)** (3)

- Fermat : $p$ premier $\Rightarrow \forall n, n^p \equiv n\,[p]$
- si $p \nmid n$, $n^{p-1} \equiv 1\,[p]$
- binôme $(n+1)^p = \sum_k \binom pk n^k$ et $p \mid \binom pk$ pour $1 \leqslant k \leqslant p-1$ (récurrence)
- Gauss pour simplifier par $n$
- $a^{6q+r} \equiv a^r\,[7]$

**division euclidienne (énigme)** (2)

- $n = bq + r$, $0 \leqslant r < b$
- égaliser les deux écritures

**lemme de Gauss et Bézout (démonstration)** (2)

- Bézout : $a \wedge b = 1 \iff \exists (u,v), au + bv = 1$
- multiplier par $c$ : $acu + bcv = c$
- $a \mid bc \Rightarrow bc = ak$
- produit de deux relations de Bézout

**divisibilité, $24 \mid p^2 - 1$ pour $p$ premier $\geqslant 5$** (2)

- Bézout
- $a \wedge b = 1$, $a \mid c$, $b \mid c \Rightarrow ab \mid c$
- division euclidienne par 3 : $d = 3q + r$, $r \in \{0,1,2\}$
- $p^2 - 1 = (p-1)(p+1)$
- $k(k+1)$ est pair
- $24 = 8 \times 3$, $8 \wedge 3 = 1$

**inverse modulo un premier, Bézout, Gauss, Fermat** (2)

- $p$ premier : $p \wedge a \in \{1, p\}$
- Bézout : $a \wedge p = 1 \iff \exists (b,v), ab + pv = 1$
- Gauss
- $ab \equiv 0\,[p] \Rightarrow a \equiv 0$ ou $b \equiv 0\,[p]$
- $a^2 - 1 = (a-1)(a+1)$
- Fermat : $p \nmid a \Rightarrow a^{p-1} \equiv 1\,[p]$

**congruences modulo $n$, équation sans solution** (2)

- $a \equiv b\,[n] \Rightarrow a^2 \equiv b^2\,[n]$
- $11 \equiv 1$, $7 \equiv 2\,[5]$
- table des carrés modulo 5 : $0, 1, 4, 4, 1$
- $x = 5k \Rightarrow x^2 = 25k^2$
- $25 \mid$ membre de gauche mais $25 \nmid 5$

**divisibilité, PGCD, Bézout, Gauss, Fermat (QCM)** (2)

- $a \mid b$ et $a \mid c \Rightarrow a \mid b - c$
- $au + cv = d \Rightarrow (a \wedge c) \mid d$
- Fermat $p \nmid a \Rightarrow a^{p-1} \equiv 1\,[p]$
- $\mathrm{pgcd}$ = produit des facteurs communs à la plus petite puissance
- Gauss exige $a \wedge b = 1$

## HP (consigne)

**question bonus (consigne)** (2)

- lire la consigne
- $96 \div 2 \div 4 \div 3 = 4$

## HP (géométrie, parcours PA)

**vecteurs du plan, repère, combinaison linéaire** (6)

- $(O\,;\,\vec u, \vec v)$ repère $\iff \vec u, \vec v$ non colinéaires $\iff \det(\vec u, \vec v) = xy' - x'y \neq 0$
- $a\vec u + b\vec v = (ax + bx', ay + by')$

**droites du plan (point, vecteur directeur, équation, parallélisme)** (6)

- $D = \{M, \exists \alpha, \overrightarrow{AM} = \alpha\vec u\}$
- $ax + by + c = 0$ a pour vecteur directeur $(-b, a)$
- droite par l'origine : $y = mx$
- droites parallèles $\iff$ vecteurs directeurs colinéaires

**géométrie de l'espace (plans, droites, vecteurs)** (4)

- $ax + by + cz + d = 0$ : plan de $\mathbb{R}^3$
- $\{M, \overrightarrow{OM} = \alpha\vec u\}$ : droite vectorielle
- combinaison linéaire coordonnée par coordonnée
- $\vec u, \vec v$ colinéaires $\iff \exists k, \vec v = k\vec u$ (ou l'un nul)

## HP (nombres complexes, hors programme 2031)

**forme exponentielle, argument** (10)

- $z = |z|e^{i\theta}$
- $e^{i\theta}e^{i\varphi} = e^{i(\theta + \varphi)}$
- $\frac{e^{i\theta}}{e^{i\varphi}} = e^{i(\theta - \varphi)}$
- $(re^{i\theta})^n = r^ne^{in\theta}$
- $-i = e^{-i\pi/2}$

**équation du second degré à coefficients complexes** (6)

- $\Delta = b^2 - 4ac$
- racine carrée $\delta = a + ib$ de $\Delta$ : $a^2 - b^2 = \mathrm{Re}\,\Delta$, $a^2 + b^2 = |\Delta|$, $2ab = \mathrm{Im}\,\Delta$
- $z = \frac{-b \pm \delta}{2a}$

**forme algébrique, conjugué, module** (4)

- $i^2 = -1$
- $\overline{a + ib} = a - ib$
- $\frac{z}{w} = \frac{z\bar w}{|w|^2}$
- $|a + ib| = \sqrt{a^2 + b^2}$
- $\left|\frac zw\right| = \frac{|z|}{|w|}$
- $|\bar z| = |z|$

**équation du second degré dans $\mathbb{C}$** (4)

- $\Delta = b^2 - 4ac$
- $\Delta < 0$ : $z = \frac{-b \pm i\sqrt{-\Delta}}{2a}$

**équation dans $\mathbb{C}$, forme exponentielle** (2)

- $AB = 0 \iff A = 0$ ou $B = 0$
- $\Delta < 0$ : $z = \frac{-b \pm i\sqrt{-\Delta}}{2a}$
- $z = |z|e^{i\theta}$, $|a + ib| = \sqrt{a^2 + b^2}$, $\cos\theta = \frac{a}{|z|}$, $\sin\theta = \frac{b}{|z|}$

**nombres complexes (cours, forme algébrique, module, forme exponentielle, équation)** (2)

- $i^2 = -1$
- $z = a + ib$ (forme algébrique), $\bar z = a - ib$, $|z| = \sqrt{a^2 + b^2}$
- $\cos\theta = \frac a{|z|}$, $\sin\theta = \frac b{|z|}$
- $z = |z|(\cos\theta + i\sin\theta) = |z|e^{i\theta}$
- $|zw| = |z||w|$
- $\frac{e^{i\alpha}}{e^{i\beta}} = e^{i(\alpha - \beta)}$
- $\Delta < 0 \Rightarrow z = \frac{-b \pm i\sqrt{-\Delta}}{2a}$

## Études des filtres

**QCM régime sinusoïdal et nature des filtres du 2nd ordre** (2)

- amplitude complexe (référence sinus) : $S\sin(\omega t + \theta) \to Se^{j\theta}$
- $\cos x = \sin(x + \frac\pi2)$
- $Z = \frac{U}{I}$
- $u$, $i$ en phase : résistance
- $i$ en avance de $\frac\pi2$ : condensateur, $Z = \frac1{C\omega}$
- $i$ en retard : bobine, $Z = L\omega$
- $LC\omega^2$ sans unité
- $\underline T = A_0\frac{Num}{1 + 2jz\frac\omega{\omega_0} - (\frac\omega{\omega_0})^2}$ : $Num = 1$ passe-bas, $-(\frac\omega{\omega_0})^2$ passe-haut, $2jz\frac\omega{\omega_0}$ passe-bande

**filtre du 1er ordre (étude qualitative, transfert, Bode, régime sinusoïdal)** (2)

- TBF : bobine = fil, condensateur = interrupteur ouvert
- THF : l'inverse
- diviseur de tension $\underline{V_s} = \frac{Z_2}{Z_1 + Z_2}\underline{V_e}$
- $Z_1 \parallel Z_2 = \frac{Z_1Z_2}{Z_1 + Z_2}$
- passe-haut $\underline T = A_0\frac{j\frac\omega{\omega_c}}{1 + j\frac\omega{\omega_c}}$, passe-bas $\underline T = \frac{A_0}{1 + j\frac\omega{\omega_c}}$
- $G_{dB} = 20\log|\underline T|$, pente $\pm 20$ dB/décade
- $v_s = V_E|\underline T|\sin(\omega t + \arg\underline T)$

**filtre du 2nd ordre RLC (étude qualitative, forme normalisée, Bode)** (2)

- TBF / THF : bobine et condensateur en fil ou circuit ouvert
- $\underline T = \frac{A_0}{1 + 2jz\frac\omega{\omega_0} - (\frac\omega{\omega_0})^2}$
- identifier $A_0$, $\omega_0^2$, $\frac{2z}{\omega_0}$
- THF : $G_{dB} \approx 20\log A_0 - 40\log\frac\omega{\omega_0}$
- phase $0 \to -\pi$ (passe-bas), $\pi \to 0$ (passe-haut)
