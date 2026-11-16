# Contrôle 2 de physique S2 — février 2017 (corrigé, FR)

- Source : `raw/S2/Midterms/Phys/2021/midterm-2021-s2-phys-correction-fr.pdf` (7 pages, corrigé manuscrit scanné)
- Date réelle : février 2017 (EPITA S2, dossier promo 2021). Sujet : `midterm-2021-s2-phys-subject-fr.md`.
- Calculatrices et documents non autorisés, réponses sur le sujet. Noté sur 20. Mécanique : énergie, réaction en Frenet, oscillation amortie ; thermodynamique : calorimétrie. Les lignes `> ` sont les solutions, relues sur le corrigé manuscrit.

## Exercice 1. Solide dans une glissière (7 points)
Type : glissière inclinée puis circulaire (théorème de l'énergie cinétique, énergie mécanique, réaction en Frenet, énergie minimale) · ECUE : Mécanique · Niveau : physique-s2-energie/6
Formules : $\Delta E_c = \sum W$ ; $W(\vec P) = mgh$ en descente, $W(\vec R_N) = 0$ sans frottement ; $E_m = \tfrac12mv^2 + mgz$ conservée ; Frenet : $m\dfrac{v^2}{R} = \sum F_N$ ; $z = R\cos\alpha + R\cos\beta$ au-dessus du point bas de la pente

Un solide de masse $m$ se déplace dans une glissière constituée d'une partie rectiligne BC suivie d'une partie circulaire de centre O et de rayon $R$. Les frottements sont négligés. Le solide est lâché du point C sans vitesse initiale. E est le point le plus bas du cercle, D le point le plus haut ; B (bas de la pente) et A (sur l'arc, au-dessus de O) sont sur le cercle, avec $\alpha = (\widehat{BOE})$ et $\beta = (\widehat{AOD})$. La pente BC est inclinée d'un angle $\alpha$ sur l'horizontale.
1. a) Représenter les forces agissant sur le solide entre C et B. b) Utiliser le théorème de l'énergie cinétique pour exprimer la vitesse au point B. On prend l'origine des altitudes au point B. Faire le calcul pour $BC = 2$ m, $g = 10\ \text{m·s}^{-2}$, $\alpha = 30°$.
> a) Le poids $\vec P$ (vertical, vers le bas) et la réaction $\vec R_N$ (perpendiculaire à la pente).
> b) $\Delta E_{c,C\to B} = W(\vec R_N) + W(\vec P) = 0 + mgh$ avec $h = BC\sin\alpha$ (travail moteur). $\tfrac12mv_B^2 - 0 = mg\,BC\sin\alpha$, donc $v_B = \sqrt{2g\,BC\sin\alpha}$. A.N. : $v_B = \sqrt{2 \times 10 \times 2 \times \tfrac12} = 2\sqrt5\ \text{m·s}^{-1}$.
2. a) Utiliser le théorème de l'énergie mécanique pour exprimer la vitesse au point A en fonction de $BC$, $\alpha$, $\beta$, $R$ et $g$. Faire le calcul pour $R = 0{,}5$ m, $\beta = 60°$, $BC = 2$ m, $g = 10\ \text{m·s}^{-2}$, $\alpha = 30°$. b) Représenter les forces appliquées sur le solide au point A. c) Utiliser la deuxième loi de Newton dans la base de Frenet $(\vec u_T, \vec u_N)$ pour exprimer la norme de la réaction $R_N$ au point A, en fonction de $m$, $g$, $BC$, $R$, $\alpha$ et $\beta$.
> a) Frottements négligés : $E_{m,A} = E_{m,C}$, soit $\tfrac12mv_A^2 + mgz_A = 0 + mgz_C$ avec $z_C = BC\sin\alpha$ et $z_A = R\cos\alpha + R\cos\beta$. Donc $v_A = \sqrt{2g\left(BC\sin\alpha - R(\cos\alpha + \cos\beta)\right)}$. A.N. : $v_A = \sqrt{20\left(1 - \tfrac12\left(\tfrac{\sqrt3}2 + \tfrac12\right)\right)} = \sqrt{5(3 - \sqrt3)} \approx 2{,}5\ \text{m·s}^{-1}$.
> b) Le poids $\vec P$ (vertical, vers le bas) et la réaction $\vec R_N$ (dirigée vers O).
> c) $\vec P + \vec R_N = m\vec a$. Projection sur $\vec u_N$ (vers O) : $R_N + mg\cos\beta = m\dfrac{v_A^2}{R}$, donc $R_N = mg\left[\dfrac{2BC}{R}\sin\alpha - 2\cos\alpha - 3\cos\beta\right]$.
3. Calculer l'énergie mécanique minimale au point C pour atteindre le point D. On donne $m = 200$ g.
> $E_{m,C} = mg\,BC\sin\alpha$ ; en D : $E_{m,D} = \tfrac12mv_D^2 + mgR(1 + \cos\alpha)$. Conservation : $E_{m,C} = E_{m,D}$, minimale quand $v_D = 0$ (solide guidé par la glissière) : $E_{m,C,\min} = mgR(1 + \cos\alpha) = 0{,}2 \times 10 \times \tfrac12\left(1 + \tfrac{\sqrt3}2\right) \approx 1{,}87$ J (le corrigé donne $\approx 1{,}85$ J avec $\sqrt3 \approx 1{,}7$).

## Exercice 2. Étude d'une oscillation amortie (6 points)
Type : oscillation amortie sur un demi-cercle (Newton en Frenet, réaction, petites oscillations, régimes) · ECUE : Mécanique
Formules : $\sum\vec F_{ext} = m\vec a$ ; Frenet : $a_T = \dfrac{dv}{dt}$, $a_N = \dfrac{v^2}{R}$ ; $v = R\dot\theta$ ; $\sin\theta \approx \theta$ ; $r^2 + \dfrac\alpha m r + \dfrac gR = 0$, $\Delta = \left(\dfrac\alpha m\right)^2 - \dfrac{4g}R$ ; $\Delta > 0$ apériodique, $\Delta = 0$ critique, $\Delta < 0$ pseudopériodique

On s'intéresse au mouvement d'un objet M de masse $m$ le long d'un demi-cercle de rayon $R$ et de centre O (M sous O, $\theta$ = angle entre OM et la verticale). Les frottements sont modélisés par $\vec f = -\alpha\vec v$. La masse est lâchée à un angle $\theta_0$, sans vitesse initiale.
1. Citer les forces extérieures appliquées au point M et les représenter sur le schéma.
> $\vec f$ : force de frottement (opposée à la vitesse) ; $\vec P$ : poids ; $\vec R_N$ : réaction normale du support (vers O).
2. a) Écrire la deuxième loi de Newton. Projeter cette équation dans la base de Frenet $(\vec u_T, \vec u_N)$. b) En déduire l'expression de la réaction $R_N$, ainsi que l'équation différentielle vérifiée par $\theta(t)$ en fonction de $\dot\theta$ et $\ddot\theta$. c) On lâche la masse avec un angle $\theta_0$ assez petit pour que $\sin\theta \approx \theta$. Réécrire l'équation différentielle et préciser les différents régimes selon les valeurs du coefficient de frottement $\alpha$. d) Illustrer à l'aide des courbes $\theta(t)$ les régimes cités en c).
> a) $\vec P + \vec R_N + \vec f = m\vec a$. Sur $\vec u_T$ : $-f - mg\sin\theta = m\dfrac{dv}{dt}$ (1). Sur $\vec u_N$ : $R_N - mg\cos\theta = m\dfrac{v^2}{R}$ (2).
> b) Avec $v = R\dot\theta$, (1) donne $mR\ddot\theta + mg\sin\theta + \alpha R\dot\theta = 0$, soit $\ddot\theta + \dfrac\alpha m\dot\theta + \dfrac gR\sin\theta = 0$. (2) donne $R_N = mR\dot\theta^2 + mg\cos\theta$.
> c) $\ddot\theta + \dfrac\alpha m\dot\theta + \dfrac gR\theta = 0$. Équation caractéristique $r^2 + \dfrac\alpha mr + \dfrac gR = 0$, $\Delta = \left(\dfrac\alpha m\right)^2 - \dfrac{4g}R$. $\dfrac\alpha m > 2\sqrt{\dfrac gR}$ : apériodique ; $\dfrac\alpha m = 2\sqrt{\dfrac gR}$ : critique ; $\dfrac\alpha m < 2\sqrt{\dfrac gR}$ : pseudopériodique.
> d) Pseudopériodique : oscillations autour de 0 partant de $\theta_0$, d'amplitude décroissante. Critique : retour à 0 sans oscillation, le plus rapide. Apériodique : retour à 0 sans oscillation, plus lent.

## Exercice 3. Calorimétrie (7 points, questions indépendantes)
Type : calorimétrie (capacité du calorimètre, fusion d'un glaçon, mélange d'eau) · ECUE : Thermodynamique · Niveau : physique-s2-thermo/5
Formules : enceinte isolée : $\sum Q_i = 0$ ; $Q = mc(\theta_f - \theta_i)$ ; calorimètre : $Q = C_{cal}(\theta_f - \theta_i)$ ; fusion : $Q = mL_f$ ; chemin fictif glace $\theta_2 \to 0$ °C $\to$ fusion $\to$ eau $0 \to \theta_e$ ; $m = \rho V$

1. Un calorimètre contient une masse $m_1 = 200$ g d'eau ; la température initiale de l'ensemble est $\theta_1 = 20$ °C. On ajoute une masse $m_2 = 300$ g d'eau à $\theta_2 = 80$ °C. a) Quelle serait la température d'équilibre $\theta_e$ si la capacité thermique $C_{cal}$ du calorimètre était négligeable ? Capacité massique de l'eau : $c_e = 4 \cdot 10^3\ \text{J·K}^{-1}\text{·kg}^{-1}$. b) On mesure en fait $\theta_e = 50$ °C. Déterminer $C_{cal}$.
> a) $m_1c_e(\theta_e - \theta_1) + m_2c_e(\theta_e - \theta_2) = 0$, donc $\theta_e = \dfrac{m_1\theta_1 + m_2\theta_2}{m_1 + m_2} = \dfrac{200 \times 20 + 300 \times 80}{500} = 56$ °C.
> b) $m_1c_e(\theta_e - \theta_1) + m_2c_e(\theta_e - \theta_2) + C_{cal}(\theta_e - \theta_1) = 0$, donc $C_{cal} = -\dfrac{c_e\left[\theta_e(m_1 + m_2) - m_1\theta_1 - m_2\theta_2\right]}{\theta_e - \theta_1} = -\dfrac{4(25000 - 4000 - 24000)}{30} = 400\ \text{J·K}^{-1}$.
2. Un calorimètre de capacité négligeable contient $m_1 = 200$ g d'eau à $\theta_1 = 70$ °C. On y place un glaçon de masse $m_2 = 80$ g sortant du congélateur à $\theta_2 = -23$ °C. Déterminer la température d'équilibre $\theta_e$ sachant que le glaçon fond en totalité. Données : $L_f = 300 \cdot 10^3\ \text{J·kg}^{-1}$, $c_e = 4 \cdot 10^3\ \text{J·K}^{-1}\text{·kg}^{-1}$, $c_g = 2 \cdot 10^3\ \text{J·K}^{-1}\text{·kg}^{-1}$.
> Glace : $-23$ °C $\to 0$ °C ($c_g$), fusion ($L_f$), eau $0 \to \theta_e$ ($c_e$). $m_1c_e(\theta_e - \theta_1) + m_2c_g(0 - (-23)) + m_2L_f + m_2c_e(\theta_e - 0) = 0$, donc $\theta_e = \dfrac{m_1c_e\theta_1 - 23m_2c_g - m_2L_f}{(m_1 + m_2)c_e} = \dfrac{0{,}2 \times 4000 \times 70 - 0{,}08(46000 + 300000)}{0{,}28 \times 4000} \approx 25$ °C.
3. On veut un bain d'eau tiède à 37 °C, de volume total $V = 250$ L, en mélangeant un volume $V_1$ d'eau chaude à $\theta_1 = 70$ °C et un volume $V_2$ d'eau froide à $\theta_2 = 15$ °C. Déterminer $V_1$ et $V_2$ (fuites thermiques négligées). Données : $c_e = 4 \cdot 10^3\ \text{J·K}^{-1}\text{·kg}^{-1}$, $\rho_e = 1$ kg/L.
> $\rho V_1c_e(37 - 70) + \rho V_2c_e(37 - 15) = 0$, soit $-33V_1 + 22V_2 = 0$, donc $3V_1 = 2V_2$. Avec $V_1 + V_2 = 250$ : $V_1 = 100$ L, $V_2 = 150$ L.
