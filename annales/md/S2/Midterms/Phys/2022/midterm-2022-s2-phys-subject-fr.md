# Contrôle 2 de physique S2 — mars 2018 (sujet, FR)

- Source : `raw/S2/Midterms/Phys/2022/midterm-2022-s2-phys-subject-fr.pdf` (5 pages)
- Date réelle : mars 2018 (EPITA S2, dossier promo 2022). Corrigé : `midterm-2022-s2-phys-correction-fr.md`.
- Calculatrices et documents non autorisés, réponses sur le sujet. Noté sur 20. Mécanique : pendule, oscillateur amorti ; thermodynamique : conduction, calorimétrie.

## QCM (4 points, pas de points négatifs)
Type : QCM d'oscillateurs et de thermique (énergie du pendule, régime critique, système isolé, résistances thermiques, mélange) · ECUE : Mécanique
Formules : $E_m = \tfrac12mL^2\dot\theta^2 + mgL(1 - \cos\theta)$, $\dfrac{dE_m}{dt} = 0 \Rightarrow \ddot\theta + \dfrac gL\sin\theta = 0$ ; critique : $\alpha = 2m\omega_0$ ; isolé : ni matière ni énergie échangée ; $R_{th} = \dfrac{e}{\lambda_{th}S}$, en série $R = \sum R_i$ ; mélange d'eau : $\theta_e = \dfrac{V_1\theta_1 + V_2\theta_2}{V_1 + V_2}$ ; intensive : température, pression

Entourer la bonne réponse. $0{,}5$ point par question.
1. L'énergie mécanique de la masse $m$ d'un pendule simple est $E_m = \tfrac12mL^2\dot\theta^2 + mgL(1 - \cos\theta)$, où $m$, $L$ et $g$ sont des constantes. Sa dérivée par rapport au temps est : a) $\dfrac{dE_m}{dt} = mL^2\dot\theta\ddot\theta - mgL\sin\theta\,\dot\theta$ ; b) $\dfrac{dE_m}{dt} = mL^2\dot\theta\ddot\theta + mgL\sin\theta$ ; c) $\dfrac{dE_m}{dt} = mL^2\dot\theta\ddot\theta + mgL\sin\theta\,\dot\theta$.
2. L'équation différentielle du mouvement du pendule simple, obtenue en écrivant $\dfrac{dE_m}{dt} = 0$, est : a) $\ddot\theta + \dfrac gL\cos\theta = 0$ ; b) $\ddot\theta + \dfrac gL\sin\theta = 0$ ; c) $\ddot\theta - \dfrac gL\sin\theta = 0$.
3. La résolution de $\ddot x + \dfrac\alpha m\dot x + \omega_0^2x = 0$ nécessite de distinguer trois régimes. Le régime critique correspond à une valeur particulière de $\alpha$ (coefficient de frottement) : a) $\alpha_{crit} = 0$ ; b) $\alpha_{crit} > 2m\omega_0$ ; c) $\alpha_{crit} = 2m\omega_0$ ; d) $\alpha_{crit} < 2m\omega_0$.
4. Un système qui n'échange ni matière ni énergie avec le milieu extérieur est appelé : a) un système isolé ; b) un système exclusif ; c) un système fermé.
5. Quelle est l'expression de la résistance thermique ? a) $R_{th} = -\dfrac{\Phi}{\Delta\theta}$ ; b) $R_{th} = \dfrac{e}{\lambda_{th}S}$ ; c) $R_{th} = \dfrac{\lambda_{th}S}{e}$.
6. Un double vitrage est constitué de deux vitres en verre, chacune de résistance $R_{verre}$, séparées par un espace rempli d'air de résistance $R_{air}$. Que vaut la résistance totale du double vitrage ? a) $R_{verre} + R_{air}$ ; b) $\dfrac{2}{R_{verre}} + \dfrac{1}{R_{air}}$ ; c) $2R_{verre} + R_{air}$.
7. La température d'équilibre atteinte lorsqu'on mélange dans un calorimètre (de capacité calorifique négligeable) un volume $V_1$ d'eau à $\theta_1$ et un volume $V_2$ d'eau à $\theta_2$ est : a) $\theta_e = \dfrac{V_1\theta_1 + V_2\theta_2}{V_1 + V_2}$ ; b) $\theta_e = \dfrac{\theta_1 + \theta_2}{2}$ ; c) $\theta_e = V_1\theta_1 + V_2\theta_2$.
8. Laquelle des grandeurs ci-dessous n'est pas extensive ? a) la température ; b) la masse ; d) le nombre de moles.

## Exercice 1. Oscillateur amorti (5 points)
Type : oscillateur ressort horizontal amorti (forces, équation différentielle, régimes, allure de x(t)) · ECUE : Mécanique
Formules : $\sum\vec F_{ext} = m\vec a$ ; rappel $-kx\,\vec u_x$, frottement $-\alpha\vec v$ ; $\ddot x + \dfrac\alpha m\dot x + \dfrac kmx = 0$ ; $\omega_0^2 = \dfrac km$ ; $r^2 + \dfrac\alpha mr + \omega_0^2 = 0$, $\Delta = \left(\dfrac\alpha m\right)^2 - 4\omega_0^2$ ; $\alpha < 2m\omega_0$ pseudopériodique, $\alpha = 2m\omega_0$ critique, $\alpha > 2m\omega_0$ apériodique

On considère un système (ressort horizontal de raideur $k$, masse $m$). On écarte la masse de sa position d'équilibre $x = 0$ d'une distance $x_0 > 0$ et on la lâche sans vitesse initiale. La masse est soumise à une force de frottement $\vec f = -\alpha\vec v$, $\alpha > 0$. On note $x(t)$ la position de la masse.
1. Représenter sur le schéma les forces appliquées sur la masse $m$, la masse se déplaçant de $x_0$ vers $x = 0$.
2. a) Utiliser la deuxième loi de Newton pour retrouver l'équation différentielle du mouvement $\ddot x + \dfrac\alpha m\dot x + \dfrac kmx = 0$. b) Donner l'équation caractéristique, préciser les trois régimes d'oscillations selon les conditions sur $\alpha$. Donner l'allure de $x(t)$ pour chacun des régimes.

## Exercice 2. Conduction thermique (5 points)
Type : conduction thermique (flux, unités, résistances thermiques en série) · ECUE : Thermodynamique
Formules : $\Phi = -\lambda_{th}S\dfrac{\Delta\theta}{e} = -\dfrac{\Delta\theta}{R_{th}}$ ; $R_{th} = \dfrac{e}{\lambda_{th}S}$ ; $[\Phi] = \text{J·s}^{-1} = \text{W}$, $[R_{th}] = \text{K·W}^{-1}$, $[\lambda_{th}] = \text{W·K}^{-1}\text{·m}^{-1}$ ; même flux dans chaque couche : $R_{th} = \sum R_{th,i}$

1. Rappeler l'expression du flux thermique $\Phi$ traversant un milieu, en fonction de l'écart de température $\Delta\theta$ et de la résistance thermique $R_{th}$ (propagation à une dimension, régime stationnaire). Retrouver les unités de $\Phi$, $R_{th}$ et de la conductivité thermique $\lambda_{th}$.
2. Montrer que la résistance thermique d'un système formé de trois milieux de conductivités $\lambda_1$, $\lambda_2$, $\lambda_3$, de même surface $S$ et d'épaisseurs $e_1$, $e_2$, $e_3$, s'écrit $R_{th} = R_{th1} + R_{th2} + R_{th3}$. Les trois milieux sont traversés par le même flux $\Phi$.

## Exercice 3. Calorimétrie (6 points, questions indépendantes)
Type : calorimétrie (capacité massique d'une huile, glace en vapeur, capacité du calorimètre) · ECUE : Thermodynamique · Niveau : physique-s2-thermo/5
Formules : enceinte adiabatique : $\sum Q_i = 0$ ; $Q = mc(\theta_f - \theta_i)$ ; calorimètre : $Q = C_{cal}(\theta_f - \theta_i)$ ; changement d'état : $Q = mL$ ; glace $-20$ °C $\to 0$ °C ($c_g$) $\to$ fusion ($L_f$) $\to 100$ °C ($c_e$) $\to$ vaporisation ($L_v$)

1. Dans un calorimètre de capacité thermique $100\ \text{J·K}^{-1}$, on introduit 100 g d'eau ; l'ensemble est à 20 °C. On y ajoute 100 g d'huile à 100 °C (température inférieure à sa température d'ébullition). La température finale est de 40 °C. Calculer la capacité massique de l'huile. Donnée : $c_{eau} = 4 \cdot 10^3\ \text{J·kg}^{-1}\text{·K}^{-1}$.
2. Quelle est la quantité de chaleur nécessaire pour convertir 10 g de glace à $-20$ °C en vapeur à 100 °C ? Données : $c_e = 4 \cdot 10^3\ \text{J·kg}^{-1}\text{·K}^{-1}$, $L_f = 335 \cdot 10^3\ \text{J·kg}^{-1}$, $c_g = 2 \cdot 10^3\ \text{J·kg}^{-1}\text{·K}^{-1}$, $L_v = 225 \cdot 10^4\ \text{J·kg}^{-1}$.
3. Un calorimètre contient $m_1 = 150$ g d'eau ; l'ensemble est à $\theta_1 = 20$ °C. On ajoute $m_2 = 250$ g d'eau à $\theta_2 = 70$ °C. Calculer la capacité thermique $C_{cal}$ du calorimètre sachant que la température d'équilibre est $\theta_e = 50$ °C. Donnée : $c_e = 4 \cdot 10^3\ \text{J·kg}^{-1}\text{·K}^{-1}$.
