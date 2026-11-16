# Partiel 2 de physique S2 — juin 2018 (sujet, FR)

- Source : `raw/S2/Finals/Phys/2022/final-2022-s2-phys-subject-fr.pdf` (6 pages)
- Date réelle : juin 2018 (EPITA S2, dossier promo 2022). Corrigé : `final-2022-s2-phys-correction-fr.md`.
- Calculatrices et documents non autorisés, réponses sur le sujet. Noté sur 20. Thermodynamique : premier principe, calorimétrie, loi de Laplace, cycle Diesel.

## QCM (4 points, pas de points négatifs)
Type : QCM de thermodynamique (premier principe, adiabatique, isotherme, isobare, fonction d'état, Laplace) · ECUE : Thermodynamique · Niveau : physique-s2-thermo/7
Formules : $dU = \delta W + \delta Q = -P\,dV + \delta Q$ ; adiabatique : $PV^\gamma = \text{cte}$, $W = nc_v(T_2 - T_1)$ ; isotherme : $\Delta U = 0$, $Q = -W$, $W = -nRT\ln\dfrac{V_2}{V_1}$ ; isobare : $\dfrac VT = \text{cte}$ ; $W$ et $Q$ ne sont pas des fonctions d'état ; Laplace en $(T, P)$ : $T^\gamma P^{1-\gamma} = \text{cte}$

1. La différentielle de l'énergie interne $dU$ d'un gaz, donnée par le premier principe, s'écrit : a) $dU = -P\,dV + Q$ ; b) $dU = -P\,dV + \delta Q$ ; c) $\delta U = -P\,dV + \delta Q$.
2. Un gaz parfait subit une transformation adiabatique de l'état (1) vers l'état (2) ($\gamma$ coefficient de Laplace). Le volume $V_2$ vérifie : a) $V_2 = V_1\left(\dfrac{P_2}{P_1}\right)^{1/\gamma}$ ; b) $V_2 = V_1\left(\dfrac{P_1}{P_2}\right)^{1/\gamma}$ ; c) $V_2 = V_1\left(\dfrac{P_2}{P_1}\right)^{-\gamma}$ ; d) $V_2 = \gamma V_1$.
3. Lorsqu'un système fermé (gaz parfait) subit une transformation isotherme, la chaleur échangée avec l'extérieur est : a) $Q = W$ ; b) $Q = \Delta U$ ; c) $Q = -W$ ; d) $Q = 0$.
4. Le travail des forces de pression de l'état (1) vers l'état (2) d'une transformation isotherme de température $T$ est : a) $W = -nRT\ln\dfrac{V_2}{V_1}$ ; b) $W = -nRT(V_2 - V_1)$ ; c) $W = nRT\ln\dfrac{V_2}{V_1}$ ; d) nul.
5. Le travail des forces de pression de (1) vers (2) d'une transformation adiabatique de $n$ moles de gaz parfait, de capacité molaire $c_v$, s'écrit : a) $W = -nRT\ln\dfrac{V_2}{V_1}$ ; b) $W = P_2V_2^\gamma - P_1V_1^\gamma$ ; c) $W = nc_v(T_2 - T_1)$.
6. Laquelle des grandeurs suivantes n'est pas une fonction d'état ? a) l'enthalpie $H$ ; b) l'énergie interne $U$ ; c) le travail des forces de pression $W$.
7. Les températures et volumes d'un gaz parfait qui subit une transformation isobare de (1) vers (2) vérifient : a) $T_1V_2 = T_2V_1$ ; b) $T_1V_1 = T_2V_2$ ; c) $\dfrac{V_1}{T_2} = \dfrac{T_1}{V_2}$.
8. La loi de Laplace écrite en fonction de la température et de la pression donne ($C$ constante) : a) $TP^{\gamma-1} = C$ ; b) $T^\gamma P^{\gamma-1} = C$ ; c) $TP^{\gamma+1} = C$ ; d) $T^\gamma P^{1-\gamma} = C$.

## Exercice 1. Calorimétrie (4 points, questions indépendantes)
Type : calorimétrie (vapeur sur glace avec condensation et fusion, capacité du calorimètre) · ECUE : Thermodynamique · Niveau : physique-s2-thermo/5
Formules : $\sum Q_i = 0$ ; $Q = mc(\theta_f - \theta_i)$ ; fusion : $Q = mL_f$ ; condensation : $Q = mL_c = -mL_v$ ; calorimètre : $Q = C_{cal}(\theta_f - \theta_i)$

1. Dans un calorimètre, 10 g de vapeur d'eau à 100 °C sont injectés sur 50 g de glace à 0 °C. Calculer la température à l'équilibre. Données : $c_e = 4 \cdot 10^3\ \text{J·kg}^{-1}\text{·K}^{-1}$, $L_f = 3 \cdot 10^5\ \text{J·kg}^{-1}$, $L_v = 2 \cdot 10^6\ \text{J·kg}^{-1}$ ($L_{condensation} = -L_{vaporisation}$).
2. On sort un bloc de plomb de masse $m_1 = 300$ g d'une étuve à $\theta_1 = 98$ °C. On le plonge dans un calorimètre contenant $m_2 = 350$ g d'eau ; l'ensemble est à $\theta_2 = 16$ °C. La température d'équilibre est $\theta_e = 18$ °C. Calculer la capacité thermique du calorimètre. Données : $c_e = 4 \cdot 10^3$, $c_p = 150\ \text{J·kg}^{-1}\text{·K}^{-1}$.

## Exercice 2. Partie cours : loi de Laplace (4 points)
Type : démonstration de la loi de Laplace (dH = V dP, dU, dH, intégration) · ECUE : Thermodynamique · Niveau : physique-s2-thermo/8
Formules : $H = U + PV$ ; $dU = \delta Q - P\,dV$ ; adiabatique : $\delta Q = 0$, $dH = V\,dP$ ; $dU = nc_vdT$, $dH = nc_pdT$ ; $\gamma = \dfrac{c_p}{c_v}$ ; $\gamma\dfrac{dV}V = -\dfrac{dP}P \Rightarrow PV^\gamma = \text{cte}$

1. Pour une transformation adiabatique, montrer que $dH = V\,dP$.
2. a) Rappeler $dU$ et $dH$ de $n$ moles de gaz parfait en fonction de $c_v$ et $c_p$. b) Donner $dU$ et $dH$ en fonction de la pression et du volume pour une transformation adiabatique. c) En déduire la loi de Laplace.

## Exercice 3. Cycle de Diesel idéal (8 points)
Type : cycle Diesel (deux adiabatiques, une isobare, une isochore, rendement) · ECUE : Thermodynamique · Niveau : physique-s2-thermo/12
Formules : Laplace $TV^{\gamma-1} = \text{cte}$ ; isobare : $\dfrac TV = \text{cte}$, $W = -P\Delta V$, $Q = nc_p\Delta T$ ; isochore : $W = 0$, $Q = nc_v\Delta T$ ; adiabatique : $Q = 0$, $W = nc_v\Delta T$ ; $\alpha = \dfrac{V_A}{V_B}$, $\beta = \dfrac{V_C}{V_B}$ ; $r = 1 + \dfrac{Q_{DA}}{Q_{BC}} = 1 + \dfrac{\alpha^{1-\gamma}(1 - \beta^\gamma)}{\gamma(\beta - 1)}$

Le moteur Diesel est un moteur à combustion interne sans éclateurs : l'air est fortement comprimé, le carburant est injecté seul et progressivement dans la chambre de combustion. Le cycle : admission de l'air dans le volume $V_A$ (IA) ; compression adiabatique AB ; injection et combustion à pression constante BC ; détente adiabatique CD jusqu'au volume initial ; ouverture de la soupape d'échappement, la pression chute brutalement (isochore DA). Taux de compression $\alpha = \dfrac{V_A}{V_B}$, rapport de détente $\beta = \dfrac{V_C}{V_B}$. Le mélange est un gaz parfait.
1. a) Utiliser la loi de Laplace pour retrouver $T_AV_A^{\gamma-1} = T_BV_B^{\gamma-1}$ et $T_CV_C^{\gamma-1} = T_DV_D^{\gamma-1}$. b) Utiliser la propriété de l'isobare BC pour montrer que $\dfrac{T_C}{V_C} = \dfrac{T_B}{V_B}$. c) En déduire $T_C = \beta T_B$, $T_A = \alpha^{1-\gamma}T_B$, $T_D = \beta^\gamma\alpha^{1-\gamma}T_B$.
2. Exprimer $Q$, $W$ et $\Delta U$ des quatre transformations du cycle, pour $n$ moles de gaz parfait, en fonction des températures.
3. a) En déduire le rendement $r = \dfrac{Q_{BC} + Q_{DA}}{Q_{BC}}$ en fonction de $\alpha$, $\beta$ et $\gamma$ (utiliser 1c). b) Calcul pour $\alpha = 14$, $\beta = 1{,}6$, $\gamma = 1{,}4$. On donne $14^{0{,}4} \approx 3$ et $1{,}6^{1{,}4} \approx 2$.
