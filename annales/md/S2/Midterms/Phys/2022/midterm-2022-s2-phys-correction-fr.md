# Contrôle 2 de physique S2 — mars 2018 (corrigé, FR)

- Source : `raw/S2/Midterms/Phys/2022/midterm-2022-s2-phys-correction-fr.pdf` (5 pages, corrigé manuscrit scanné avec barème)
- Date réelle : mars 2018 (EPITA S2, dossier promo 2022). Sujet : `midterm-2022-s2-phys-subject-fr.md`.
- Calculatrices et documents non autorisés, réponses sur le sujet. Noté sur 20. Mécanique : pendule, oscillateur amorti ; thermodynamique : conduction, calorimétrie. Les lignes `> ` sont les solutions, relues sur le corrigé manuscrit.

## QCM (4 points, pas de points négatifs)
Type : QCM d'oscillateurs et de thermique (énergie du pendule, régime critique, système isolé, résistances thermiques, mélange) · ECUE : Mécanique
Formules : $E_m = \tfrac12mL^2\dot\theta^2 + mgL(1 - \cos\theta)$, $\dfrac{dE_m}{dt} = 0 \Rightarrow \ddot\theta + \dfrac gL\sin\theta = 0$ ; critique : $\alpha = 2m\omega_0$ ; isolé : ni matière ni énergie échangée ; $R_{th} = \dfrac{e}{\lambda_{th}S}$, en série $R = \sum R_i$ ; mélange d'eau : $\theta_e = \dfrac{V_1\theta_1 + V_2\theta_2}{V_1 + V_2}$ ; intensive : température, pression

Entourer la bonne réponse. $0{,}5$ point par question.
1. L'énergie mécanique de la masse $m$ d'un pendule simple est $E_m = \tfrac12mL^2\dot\theta^2 + mgL(1 - \cos\theta)$, où $m$, $L$ et $g$ sont des constantes. Sa dérivée par rapport au temps est : a) $\dfrac{dE_m}{dt} = mL^2\dot\theta\ddot\theta - mgL\sin\theta\,\dot\theta$ ; b) $\dfrac{dE_m}{dt} = mL^2\dot\theta\ddot\theta + mgL\sin\theta$ ; c) $\dfrac{dE_m}{dt} = mL^2\dot\theta\ddot\theta + mgL\sin\theta\,\dot\theta$.
> c).
2. L'équation différentielle du mouvement du pendule simple, obtenue en écrivant $\dfrac{dE_m}{dt} = 0$, est : a) $\ddot\theta + \dfrac gL\cos\theta = 0$ ; b) $\ddot\theta + \dfrac gL\sin\theta = 0$ ; c) $\ddot\theta - \dfrac gL\sin\theta = 0$.
> b).
3. La résolution de $\ddot x + \dfrac\alpha m\dot x + \omega_0^2x = 0$ nécessite de distinguer trois régimes. Le régime critique correspond à une valeur particulière de $\alpha$ (coefficient de frottement) : a) $\alpha_{crit} = 0$ ; b) $\alpha_{crit} > 2m\omega_0$ ; c) $\alpha_{crit} = 2m\omega_0$ ; d) $\alpha_{crit} < 2m\omega_0$.
> c).
4. Un système qui n'échange ni matière ni énergie avec le milieu extérieur est appelé : a) un système isolé ; b) un système exclusif ; c) un système fermé.
> a).
5. Quelle est l'expression de la résistance thermique ? a) $R_{th} = -\dfrac{\Phi}{\Delta\theta}$ ; b) $R_{th} = \dfrac{e}{\lambda_{th}S}$ ; c) $R_{th} = \dfrac{\lambda_{th}S}{e}$.
> b).
6. Un double vitrage est constitué de deux vitres en verre, chacune de résistance $R_{verre}$, séparées par un espace rempli d'air de résistance $R_{air}$. Que vaut la résistance totale du double vitrage ? a) $R_{verre} + R_{air}$ ; b) $\dfrac{2}{R_{verre}} + \dfrac{1}{R_{air}}$ ; c) $2R_{verre} + R_{air}$.
> c) : trois résistances en série.
7. La température d'équilibre atteinte lorsqu'on mélange dans un calorimètre (de capacité calorifique négligeable) un volume $V_1$ d'eau à $\theta_1$ et un volume $V_2$ d'eau à $\theta_2$ est : a) $\theta_e = \dfrac{V_1\theta_1 + V_2\theta_2}{V_1 + V_2}$ ; b) $\theta_e = \dfrac{\theta_1 + \theta_2}{2}$ ; c) $\theta_e = V_1\theta_1 + V_2\theta_2$.
> a).
8. Laquelle des grandeurs ci-dessous n'est pas extensive ? a) la température ; b) la masse ; d) le nombre de moles.
> a) : la température est intensive.

## Exercice 1. Oscillateur amorti (5 points)
Type : oscillateur ressort horizontal amorti (forces, équation différentielle, régimes, allure de x(t)) · ECUE : Mécanique
Formules : $\sum\vec F_{ext} = m\vec a$ ; rappel $-kx\,\vec u_x$, frottement $-\alpha\vec v$ ; $\ddot x + \dfrac\alpha m\dot x + \dfrac kmx = 0$ ; $\omega_0^2 = \dfrac km$ ; $r^2 + \dfrac\alpha mr + \omega_0^2 = 0$, $\Delta = \left(\dfrac\alpha m\right)^2 - 4\omega_0^2$ ; $\alpha < 2m\omega_0$ pseudopériodique, $\alpha = 2m\omega_0$ critique, $\alpha > 2m\omega_0$ apériodique

On considère un système (ressort horizontal de raideur $k$, masse $m$). On écarte la masse de sa position d'équilibre $x = 0$ d'une distance $x_0 > 0$ et on la lâche sans vitesse initiale. La masse est soumise à une force de frottement $\vec f = -\alpha\vec v$, $\alpha > 0$. On note $x(t)$ la position de la masse.
1. Représenter sur le schéma les forces appliquées sur la masse $m$, la masse se déplaçant de $x_0$ vers $x = 0$.
> Le poids $\vec P$ (vers le bas), la réaction $\vec R_N$ (vers le haut), la tension du ressort $\vec T$ (vers O, ici dans le sens du mouvement) et le frottement $\vec f$ (opposé à la vitesse).
2. a) Utiliser la deuxième loi de Newton pour retrouver l'équation différentielle du mouvement $\ddot x + \dfrac\alpha m\dot x + \dfrac kmx = 0$. b) Donner l'équation caractéristique, préciser les trois régimes d'oscillations selon les conditions sur $\alpha$. Donner l'allure de $x(t)$ pour chacun des régimes.
> a) $\vec P + \vec R_N + \vec T + \vec f = m\vec a$. Sur l'axe du mouvement Ox : $0 + 0 - kx - \alpha v = m\ddot x$ avec $v = \dot x$, d'où $\ddot x + \dfrac\alpha m\dot x + \dfrac kmx = 0$.
> b) $\omega_0^2 = \dfrac km$ (pulsation propre sans frottement). Équation caractéristique $r^2 + \dfrac\alpha mr + \omega_0^2 = 0$, $\Delta = \left(\dfrac\alpha m\right)^2 - 4\omega_0^2$. $\Delta < 0 \iff \alpha < 2m\omega_0$ : deux racines complexes conjuguées, régime pseudopériodique (oscillations de $x_0$ autour de 0, amplitude décroissante). $\Delta = 0 \iff \alpha = 2m\omega_0$ : régime critique (retour à 0 le plus rapide, sans oscillation). $\Delta > 0 \iff \alpha > 2m\omega_0$ : régime apériodique (retour lent à 0, sans oscillation).

## Exercice 2. Conduction thermique (5 points)
Type : conduction thermique (flux, unités, résistances thermiques en série) · ECUE : Thermodynamique
Formules : $\Phi = -\lambda_{th}S\dfrac{\Delta\theta}{e} = -\dfrac{\Delta\theta}{R_{th}}$ ; $R_{th} = \dfrac{e}{\lambda_{th}S}$ ; $[\Phi] = \text{J·s}^{-1} = \text{W}$, $[R_{th}] = \text{K·W}^{-1}$, $[\lambda_{th}] = \text{W·K}^{-1}\text{·m}^{-1}$ ; même flux dans chaque couche : $R_{th} = \sum R_{th,i}$

1. Rappeler l'expression du flux thermique $\Phi$ traversant un milieu, en fonction de l'écart de température $\Delta\theta$ et de la résistance thermique $R_{th}$ (propagation à une dimension, régime stationnaire). Retrouver les unités de $\Phi$, $R_{th}$ et de la conductivité thermique $\lambda_{th}$.
> $\Phi = -\lambda_{th}\dfrac{\Delta\theta}{e}S = -\dfrac{\Delta\theta}{R_{th}}$ avec $R_{th} = \dfrac{e}{\lambda_{th}S}$. $\Phi$ est une énergie thermique par unité de temps : $[\Phi] = \text{J·s}^{-1} = \text{W}$. $R_{th} = -\dfrac{\Delta\theta}{\Phi}$ : $[R_{th}] = \text{K·W}^{-1}$. $\lambda_{th} = \dfrac{e}{R_{th}S}$ : $[\lambda_{th}] = \text{W·K}^{-1}\text{·m}^{-1}$.
2. Montrer que la résistance thermique d'un système formé de trois milieux de conductivités $\lambda_1$, $\lambda_2$, $\lambda_3$, de même surface $S$ et d'épaisseurs $e_1$, $e_2$, $e_3$, s'écrit $R_{th} = R_{th1} + R_{th2} + R_{th3}$. Les trois milieux sont traversés par le même flux $\Phi$.
> Températures $\theta_1 = \theta_{int}$, $\theta_2$, $\theta_3$, $\theta_4 = \theta_{ext}$ aux interfaces. Milieu 1 : $\Phi = -\dfrac{\theta_2 - \theta_1}{e_1/(\lambda_1S)}$ ; milieu 2 : $\Phi = -\dfrac{\theta_3 - \theta_2}{e_2/(\lambda_2S)}$ ; milieu 3 : $\Phi = -\dfrac{\theta_4 - \theta_3}{e_3/(\lambda_3S)}$. En sommant : $\theta_1 - \theta_4 = \Phi\left(\dfrac{e_1}{\lambda_1S} + \dfrac{e_2}{\lambda_2S} + \dfrac{e_3}{\lambda_3S}\right)$. Or $\Delta\theta = -\Phi R_{th}$, d'où $R_{th} = R_{th1} + R_{th2} + R_{th3}$.

## Exercice 3. Calorimétrie (6 points, questions indépendantes)
Type : calorimétrie (capacité massique d'une huile, glace en vapeur, capacité du calorimètre) · ECUE : Thermodynamique · Niveau : physique-s2-thermo/5
Formules : enceinte adiabatique : $\sum Q_i = 0$ ; $Q = mc(\theta_f - \theta_i)$ ; calorimètre : $Q = C_{cal}(\theta_f - \theta_i)$ ; changement d'état : $Q = mL$ ; glace $-20$ °C $\to 0$ °C ($c_g$) $\to$ fusion ($L_f$) $\to 100$ °C ($c_e$) $\to$ vaporisation ($L_v$)

1. Dans un calorimètre de capacité thermique $100\ \text{J·K}^{-1}$, on introduit 100 g d'eau ; l'ensemble est à 20 °C. On y ajoute 100 g d'huile à 100 °C (température inférieure à sa température d'ébullition). La température finale est de 40 °C. Calculer la capacité massique de l'huile. Donnée : $c_{eau} = 4 \cdot 10^3\ \text{J·kg}^{-1}\text{·K}^{-1}$.
> $m_ec_e(\theta_e - \theta_1) + m_hc_h(\theta_e - \theta_2) + C_{cal}(\theta_e - \theta_1) = 0$, donc $c_h = -\dfrac{(\theta_e - \theta_1)(m_ec_e + C_{cal})}{m_h(\theta_e - \theta_2)} = -\dfrac{20 \times 500}{0{,}1 \times (-60)} \approx 1{,}67 \cdot 10^3\ \text{J·kg}^{-1}\text{·K}^{-1}$.
2. Quelle est la quantité de chaleur nécessaire pour convertir 10 g de glace à $-20$ °C en vapeur à 100 °C ? Données : $c_e = 4 \cdot 10^3\ \text{J·kg}^{-1}\text{·K}^{-1}$, $L_f = 335 \cdot 10^3\ \text{J·kg}^{-1}$, $c_g = 2 \cdot 10^3\ \text{J·kg}^{-1}\text{·K}^{-1}$, $L_v = 225 \cdot 10^4\ \text{J·kg}^{-1}$.
> $Q = m_g\left[c_g(0 - (-20)) + L_f + c_e(100 - 0) + L_v\right]$ (la masse est conservée) $= 10^{-2}\left[40 \cdot 10^3 + 335 \cdot 10^3 + 400 \cdot 10^3 + 2250 \cdot 10^3\right] = 30{,}25$ kJ.
3. Un calorimètre contient $m_1 = 150$ g d'eau ; l'ensemble est à $\theta_1 = 20$ °C. On ajoute $m_2 = 250$ g d'eau à $\theta_2 = 70$ °C. Calculer la capacité thermique $C_{cal}$ du calorimètre sachant que la température d'équilibre est $\theta_e = 50$ °C. Donnée : $c_e = 4 \cdot 10^3\ \text{J·kg}^{-1}\text{·K}^{-1}$.
> $C_{cal}(\theta_e - \theta_1) + m_1c_e(\theta_e - \theta_1) + m_2c_e(\theta_e - \theta_2) = 0$, donc $C_{cal} = -\dfrac{c_e\left(m_1(\theta_e - \theta_1) + m_2(\theta_e - \theta_2)\right)}{\theta_e - \theta_1} = -\dfrac{4(4500 - 5000)}{30} \approx 66{,}7\ \text{J·K}^{-1}$.
