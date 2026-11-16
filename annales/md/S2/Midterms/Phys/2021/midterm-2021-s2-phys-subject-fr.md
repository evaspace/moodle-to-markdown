# Contrôle 2 de physique S2 — février 2017 (sujet, FR)

- Source : `raw/S2/Midterms/Phys/2021/midterm-2021-s2-phys-subject-fr.pdf` (7 pages)
- Date réelle : février 2017 (EPITA S2, dossier promo 2021). Corrigé : `midterm-2021-s2-phys-correction-fr.md`.
- Calculatrices et documents non autorisés, réponses sur le sujet. Noté sur 20. Mécanique : énergie, réaction en Frenet, oscillation amortie ; thermodynamique : calorimétrie.

## Exercice 1. Solide dans une glissière (7 points)
Type : glissière inclinée puis circulaire (théorème de l'énergie cinétique, énergie mécanique, réaction en Frenet, énergie minimale) · ECUE : Mécanique · Niveau : physique-s2-energie/6
Formules : $\Delta E_c = \sum W$ ; $W(\vec P) = mgh$ en descente, $W(\vec R_N) = 0$ sans frottement ; $E_m = \tfrac12mv^2 + mgz$ conservée ; Frenet : $m\dfrac{v^2}{R} = \sum F_N$ ; $z = R\cos\alpha + R\cos\beta$ au-dessus du point bas de la pente

Un solide de masse $m$ se déplace dans une glissière constituée d'une partie rectiligne BC suivie d'une partie circulaire de centre O et de rayon $R$. Les frottements sont négligés. Le solide est lâché du point C sans vitesse initiale. E est le point le plus bas du cercle, D le point le plus haut ; B (bas de la pente) et A (sur l'arc, au-dessus de O) sont sur le cercle, avec $\alpha = (\widehat{BOE})$ et $\beta = (\widehat{AOD})$. La pente BC est inclinée d'un angle $\alpha$ sur l'horizontale.
1. a) Représenter les forces agissant sur le solide entre C et B. b) Utiliser le théorème de l'énergie cinétique pour exprimer la vitesse au point B. On prend l'origine des altitudes au point B. Faire le calcul pour $BC = 2$ m, $g = 10\ \text{m·s}^{-2}$, $\alpha = 30°$.
2. a) Utiliser le théorème de l'énergie mécanique pour exprimer la vitesse au point A en fonction de $BC$, $\alpha$, $\beta$, $R$ et $g$. Faire le calcul pour $R = 0{,}5$ m, $\beta = 60°$, $BC = 2$ m, $g = 10\ \text{m·s}^{-2}$, $\alpha = 30°$. b) Représenter les forces appliquées sur le solide au point A. c) Utiliser la deuxième loi de Newton dans la base de Frenet $(\vec u_T, \vec u_N)$ pour exprimer la norme de la réaction $R_N$ au point A, en fonction de $m$, $g$, $BC$, $R$, $\alpha$ et $\beta$.
3. Calculer l'énergie mécanique minimale au point C pour atteindre le point D. On donne $m = 200$ g.

## Exercice 2. Étude d'une oscillation amortie (6 points)
Type : oscillation amortie sur un demi-cercle (Newton en Frenet, réaction, petites oscillations, régimes) · ECUE : Mécanique
Formules : $\sum\vec F_{ext} = m\vec a$ ; Frenet : $a_T = \dfrac{dv}{dt}$, $a_N = \dfrac{v^2}{R}$ ; $v = R\dot\theta$ ; $\sin\theta \approx \theta$ ; $r^2 + \dfrac\alpha m r + \dfrac gR = 0$, $\Delta = \left(\dfrac\alpha m\right)^2 - \dfrac{4g}R$ ; $\Delta > 0$ apériodique, $\Delta = 0$ critique, $\Delta < 0$ pseudopériodique

On s'intéresse au mouvement d'un objet M de masse $m$ le long d'un demi-cercle de rayon $R$ et de centre O (M sous O, $\theta$ = angle entre OM et la verticale). Les frottements sont modélisés par $\vec f = -\alpha\vec v$. La masse est lâchée à un angle $\theta_0$, sans vitesse initiale.
1. Citer les forces extérieures appliquées au point M et les représenter sur le schéma.
2. a) Écrire la deuxième loi de Newton. Projeter cette équation dans la base de Frenet $(\vec u_T, \vec u_N)$. b) En déduire l'expression de la réaction $R_N$, ainsi que l'équation différentielle vérifiée par $\theta(t)$ en fonction de $\dot\theta$ et $\ddot\theta$. c) On lâche la masse avec un angle $\theta_0$ assez petit pour que $\sin\theta \approx \theta$. Réécrire l'équation différentielle et préciser les différents régimes selon les valeurs du coefficient de frottement $\alpha$. d) Illustrer à l'aide des courbes $\theta(t)$ les régimes cités en c).

## Exercice 3. Calorimétrie (7 points, questions indépendantes)
Type : calorimétrie (capacité du calorimètre, fusion d'un glaçon, mélange d'eau) · ECUE : Thermodynamique · Niveau : physique-s2-thermo/5
Formules : enceinte isolée : $\sum Q_i = 0$ ; $Q = mc(\theta_f - \theta_i)$ ; calorimètre : $Q = C_{cal}(\theta_f - \theta_i)$ ; fusion : $Q = mL_f$ ; chemin fictif glace $\theta_2 \to 0$ °C $\to$ fusion $\to$ eau $0 \to \theta_e$ ; $m = \rho V$

1. Un calorimètre contient une masse $m_1 = 200$ g d'eau ; la température initiale de l'ensemble est $\theta_1 = 20$ °C. On ajoute une masse $m_2 = 300$ g d'eau à $\theta_2 = 80$ °C. a) Quelle serait la température d'équilibre $\theta_e$ si la capacité thermique $C_{cal}$ du calorimètre était négligeable ? Capacité massique de l'eau : $c_e = 4 \cdot 10^3\ \text{J·K}^{-1}\text{·kg}^{-1}$. b) On mesure en fait $\theta_e = 50$ °C. Déterminer $C_{cal}$.
2. Un calorimètre de capacité négligeable contient $m_1 = 200$ g d'eau à $\theta_1 = 70$ °C. On y place un glaçon de masse $m_2 = 80$ g sortant du congélateur à $\theta_2 = -23$ °C. Déterminer la température d'équilibre $\theta_e$ sachant que le glaçon fond en totalité. Données : $L_f = 300 \cdot 10^3\ \text{J·kg}^{-1}$, $c_e = 4 \cdot 10^3\ \text{J·K}^{-1}\text{·kg}^{-1}$, $c_g = 2 \cdot 10^3\ \text{J·K}^{-1}\text{·kg}^{-1}$.
3. On veut un bain d'eau tiède à 37 °C, de volume total $V = 250$ L, en mélangeant un volume $V_1$ d'eau chaude à $\theta_1 = 70$ °C et un volume $V_2$ d'eau froide à $\theta_2 = 15$ °C. Déterminer $V_1$ et $V_2$ (fuites thermiques négligées). Données : $c_e = 4 \cdot 10^3\ \text{J·K}^{-1}\text{·kg}^{-1}$, $\rho_e = 1$ kg/L.
