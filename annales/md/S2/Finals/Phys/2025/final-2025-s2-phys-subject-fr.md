# Partiel de physique S2 — 2020-2021 (sujet, FR)

- Source : `raw/S2/Finals/Phys/2025/final-2025-s2-phys-subject-fr.pdf` (6 pages)
- Date réelle : année 2020-2021 (EPITA S2, dossier promo 2025). Corrigé : `final-2025-s2-phys-correction-fr.md`.
- Calculatrices et documents non autorisés. Réponses sur le sujet. Thermodynamique : cycles de Brayton et de Carnot.

## QCM (4 points, sans points négatifs)
Type : QCM de thermodynamique (unités, Mayer, cycle, premier principe, grandeurs intensives) · ECUE : Thermodynamique · Niveau : physique-s2-thermo/6
Formules : résistance thermique en $\text{K·W}^{-1}$ ; Mayer : $c_p - c_v = R$, $\gamma = \dfrac{c_p}{c_v}$ $\Rightarrow c_p = \dfrac{\gamma R}{\gamma - 1}$ ; sur un cycle : $\Delta U = \Delta H = 0$, $W + Q = 0$ ; $dU = \delta Q - P\,dV$ ; isobare : $Q = \Delta H = nc_p\Delta T$ ; équilibre thermique : $T_1 = T_2$

Entourer la bonne réponse ($0{,}5$ point par question).
1. La résistance thermique s'exprime en : a) $\text{K·W}^{-1}$ ; b) $\text{W·K}^{-1}$ ; c) $\text{W·m}^{-1}\text{·K}^{-1}$ ; d) $\text{m·K·W}^{-1}$.
2. Si l'on connaît la relation de Mayer ($c_p - c_v = R$) et que l'on sait que $\gamma = \dfrac{c_p}{c_v}$, on peut en déduire que : a) $c_p = \dfrac{\gamma R}{\gamma - 1}$ ; b) $c_p = \dfrac{R}{\gamma - 1}$ ; c) $c_p = \dfrac{\gamma^2 R}{\gamma - 1}$.
3. Lors d'un cycle thermodynamique, il n'est **pas** possible d'écrire à propos du système étudié : a) $W_{cycle} + Q_{cycle} = 0$ ; b) $\Delta H_{cycle} = 0$ ; c) $Q_{cycle} = 0$.
4. Laquelle parmi les grandeurs suivantes n'est pas une fonction d'état ? a) l'enthalpie $H$ ; b) l'énergie interne $U$ ; c) la quantité de chaleur $Q$.
5. Le premier principe de la thermodynamique à l'échelle infinitésimale est : a) $dU = \delta Q - V\,dP$ ; b) $dU = \delta Q + V\,dP$ ; c) $dU = \delta Q + P\,dV$ ; d) $dU = \delta Q - P\,dV$.
6. Laquelle de ces grandeurs est intensive ? a) la masse ; b) le volume ; c) la température.
7. Un équilibre thermique entre un système de température $T_1$ et un système de température $T_2$ est atteint lorsque : a) $T_1 = T_2$ ; b) $T_1$ et $T_2$ tendent vers l'infini ; c) $T_1 < T_2$.
8. Dans le cas isobare, la chaleur $Q$ est égale à la variation de l'enthalpie $H$. Si le gaz est parfait, la variation d'enthalpie est égale à : a) $\Delta H = nc_v\Delta T$ ; b) $\Delta H = nc_T\Delta T$ ; c) $\Delta H = nc_p\Delta T$.

## Exercice 1. Le cycle de Brayton (9 points)
Type : cycle de Brayton (deux adiabatiques, deux isobares, rendement) · ECUE : Thermodynamique · Niveau : physique-s2-thermo/12
Formules : Laplace : $PV^\gamma = \text{cste}$ $\Rightarrow \dfrac{T}{P^\beta} = \text{cste}$ avec $\beta = \dfrac{\gamma - 1}{\gamma}$ ; adiabatique : $Q = 0$, $W = \Delta U = C_v\Delta T$ ; isobare : $Q = C_p\Delta T$, $W = \Delta U - Q = (C_v - C_p)\Delta T$ ; $W_{cycle} = -Q_{cycle}$ ; $\eta = -\dfrac{W_{cycle}}{Q_{BC}} = 1 - \dfrac{1}{r_p^\beta}$, $r_p = \dfrac{P_B}{P_A}$

Rappels : $c_p - c_v = R$ (ou $C_p - C_v = nR$) et $\gamma = \dfrac{c_p}{c_v}$.

Un gaz parfait (hélium) circule dans une installation (compresseur et turbine sur le même axe, deux échangeurs). Le travail fourni par la turbine fait fonctionner le compresseur et produit de l'électricité. Le gaz décrit le cycle de Brayton, formé de deux isobares et de deux adiabatiques, toutes réversibles :
- compression adiabatique du point A ($T_A = 300$ K, $P_A = 20\cdot10^5$ Pa) vers le point B à la pression $P_B = 80\cdot10^5$ Pa ;
- transformation isobare de B vers C (échauffement) jusqu'à $T_C = 1300$ K ;
- détente adiabatique de C vers D ;
- transformation isobare de D vers A (refroidissement).

On donne pour 1 mol d'hélium $C_v = \tfrac32R$, $C_p = \tfrac52R$, $R = 8{,}314\ \text{J·K}^{-1}\text{·mol}^{-1}$.
1. Représenter le cycle ABCDA dans un diagramme de Clapeyron.
2. Pour une transformation adiabatique réversible, montrer que $\dfrac{T}{P^\beta} = \text{cste}$ avec $\beta$ fonction de $\gamma$.
3. En déduire $T_B$ et $T_D$. Application numérique, avec $4^{0{,}4} \approx 1{,}75$ et $\dfrac{52}{7} \approx 7{,}42$.
4. Pour chaque transformation, donner $\Delta U$, $Q$ et $W$.
5. En déduire $Q_{cycle}$ et $W_{cycle}$ (seulement en fonction de $C_p$ et des températures $T_A$ et $T_C$).
6. Le rendement du cycle s'écrit $\eta = -\dfrac{W_{cycle}}{Q_{BC}}$. Montrer qu'il peut se mettre sous la forme $\eta = 1 - \dfrac{1}{r_p^\beta}$ avec $r_p = \dfrac{P_B}{P_A}$. Application numérique.

## Exercice 2. Le cycle de Carnot (8 points)
Type : cycle de Carnot (deux isothermes, deux adiabatiques, rendement) · ECUE : Thermodynamique · Niveau : physique-s2-thermo/12
Formules : Laplace : $TV^{\gamma-1} = \text{cste}$ ; isotherme : $\Delta U = 0$, $Q = -W = nRT\ln\dfrac{V_f}{V_i}$ ; adiabatique : $Q = 0$, $W = \Delta U = \dfrac{nR}{\gamma - 1}\Delta T$ ; $\dfrac{V_A}{V_B} = \dfrac{V_D}{V_C}$ ; $r = \dfrac{|W_{cycle}|}{Q_{absorbée}} = 1 - \dfrac{T_f}{T_c}$

Une mole de gaz parfait ($n = 1$), initialement dans l'état $(P_A, V_A, T_A = T_f)$, subit les transformations réversibles suivantes :
- isotherme jusqu'à l'état $(P_B, V_B < V_A, T_B = T_f)$ ;
- adiabatique jusqu'à l'état $(P_C, V_C, T_C = T_c > T_f)$ ;
- isotherme jusqu'à l'état $(P_D, V_D > V_C, T_D = T_c)$ ;
- adiabatique ramenant le gaz dans l'état initial.
1. Représenter l'allure du cycle dans le diagramme de Clapeyron $(P, V)$.
2. Utiliser la loi de Laplace pour montrer : $T_fV_B^{\gamma-1} = T_cV_C^{\gamma-1}$ (adiabatique de B à C) et $T_fV_A^{\gamma-1} = T_cV_D^{\gamma-1}$ (adiabatique de D à A).
3. En déduire que $\dfrac{V_A}{V_B} = \dfrac{V_D}{V_C}$.
4. Exprimer la quantité de chaleur et le travail pour chaque transformation en fonction de $R$, $T_f$, $T_c$, $V_A$, $V_B$, $V_C$ et $V_D$.
5. En déduire le rendement $r = \dfrac{|W_{cycle}|}{Q_{absorbée}}$ en fonction de $T_c$ et $T_f$.
