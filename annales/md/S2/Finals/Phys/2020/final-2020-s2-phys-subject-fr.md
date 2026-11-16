# Partiel 2 de physique S2 — juin 2016 (sujet, FR)

- Source : `raw/S2/Finals/Phys/2020/final-2020-s2-phys-subject-fr.pdf`, pages 1 à 7 (le PDF de 56 pages regroupe toute la session de juin 2016 : physique en français puis en anglais, mathématiques, électronique, architecture ; seule la physique en français est transcrite ici). Pas de corrigé officiel.
- Date réelle : juin 2016 (EPITA InfoSup S2, dossier promo 2020). Corrigé : `final-2020-s2-phys-correction-fr.md`.
- Calculatrices et documents non autorisés, réponses sur le sujet. Noté sur 20. Thermodynamique : calorimétrie, enthalpie, Meyer, transformations du gaz parfait, cycle de Joule, entropie. Formulaire fourni : $\Delta U = nc_v\Delta T$ ; $Q_P = nc_p\Delta T$ ($\delta Q_P = nc_pdT$).

## Exercice 1. Calorimétrie (5 points, questions indépendantes)
Type : calorimétrie (capacité du calorimètre, capacité massique du plomb, glace en eau liquide) · ECUE : Thermodynamique · Niveau : physique-s2-thermo/5
Formules : $\sum Q_i = 0$ ; $Q = mc(\theta_f - \theta_i)$ ; calorimètre : $Q = C_{cal}(\theta_f - \theta_i)$ ; fusion : $Q = mL_f$ ; glace $-20$ °C $\to 0$ °C ($c_g$) $\to$ fusion ($L_f$) $\to$ eau $0 \to 20$ °C ($c_e$)

1. On place 50 g d'eau dans un calorimètre. Au bout d'un certain temps, la température lue est de 20 °C. On ajoute 50 g d'eau à 30 °C. La température finale est de 23 °C. Calculer la capacité du calorimètre. Donnée : $c_e = 4 \cdot 10^3\ \text{J·kg}^{-1}\text{·K}^{-1}$.
2. Dans un calorimètre de capacité $200\ \text{J·K}^{-1}$ contenant 250 g d'eau à 20 °C, on introduit un bloc de plomb de masse $m_p = 300$ g à 113 °C. La température d'équilibre est de 23 °C. Calculer la capacité massique du plomb. Donnée : $c_e = 4 \cdot 10^3\ \text{J·kg}^{-1}\text{·K}^{-1}$.
3. Calculer la quantité de chaleur nécessaire pour convertir 10 g de glace à $-20$ °C en liquide à 20 °C. Données : $c_e = 4 \cdot 10^3\ \text{J·kg}^{-1}\text{·K}^{-1}$, $L_f = 335 \cdot 10^3\ \text{J·kg}^{-1}$, $c_g = 2 \cdot 10^3\ \text{J·kg}^{-1}\text{·K}^{-1}$.

## Exercice 2. Gaz parfait (7 points, questions indépendantes)
Type : gaz parfait (enthalpie, Meyer et capacités molaires, compression isotherme, Laplace en T, V et T, P) · ECUE : Thermodynamique · Niveau : physique-s2-thermo/7
Formules : $dU = \delta Q - P\,dV$ ; à $P$ constante $Q_P = \Delta(U + PV) = \Delta H$ ; $c_p - c_v = R$, $\gamma = \dfrac{c_p}{c_v}$ $\Rightarrow c_v = \dfrac{R}{\gamma - 1}$, $c_p = \dfrac{\gamma R}{\gamma - 1}$ ; isotherme : $W = -nRT\ln\dfrac{V_B}{V_A} = nRT\ln\dfrac{P_B}{P_A}$, $Q = -W$ ; Laplace : $PV^\gamma$, $TV^{\gamma-1}$, $T^\gamma P^{1-\gamma}$ constants

1. Utiliser le premier principe pour retrouver l'expression de la fonction d'état enthalpie $H$, sachant que $\Delta H$ représente la chaleur échangée à pression constante.
2. La relation de Meyer est $c_p - c_v = R$ et le coefficient de Laplace $\gamma = \dfrac{c_p}{c_v}$. Retrouver $c_v$ et $c_p$ en fonction de $R$ et $\gamma$.
3. Une mole de gaz parfait subit une compression isotherme de A vers B à la température $T_0$. a) Exprimer le travail $W_{AB}$ en fonction de $T_0$, $V_A$, $V_B$. b) Même travail en fonction de $T_0$, $P_A$, $P_B$. c) En déduire la chaleur cédée $Q_{AB}$ en fonction de $T_0$, $V_A$, $V_B$.
4. Une mole de gaz parfait subit une compression adiabatique de A vers B, avec $P_AV_A^\gamma = P_BV_B^\gamma$. a) Réécrire cette relation en fonction de $T$ et $V$. b) Même question en fonction de $T$ et $P$.

## Exercice 3. Cycle de Joule (8 points)
Type : cycle de Joule (deux adiabatiques, deux isobares, rendement, entropie) · ECUE : Thermodynamique · Niveau : physique-s2-thermo/12
Formules : Laplace $T^\gamma P^{1-\gamma} = \text{cte}$ ; adiabatique : $Q = 0$, $W = nc_v\Delta T$, $\Delta S = 0$ si réversible ; isobare : $Q = nc_p\Delta T$, $W = -nR\Delta T$, $\Delta S = nc_p\ln\dfrac{T_f}{T_i}$ ; $r = \dfrac{Q_{BC} + Q_{DA}}{Q_{BC}} = 1 - \dfrac{T_D - T_A}{T_C - T_B} = 1 - a^{\frac{1-\gamma}{\gamma}}$, $a = \dfrac{P_B}{P_A}$

Un moteur fonctionne selon le cycle de Joule : $n$ moles d'air (gaz parfait) parcourent le cycle idéal ABCDA. AB : compression adiabatique réversible de $P_A$ à $P_B$ ; BC : combustion isobare à $P_B$ ; CD : détente adiabatique réversible de $P_B$ à $P_A$ ; DA : refroidissement isobare à $P_A$.
1. Montrer à l'aide de la loi de Laplace que $\dfrac{T_D}{T_C} = \left(\dfrac{P_C}{P_D}\right)^{\frac{1-\gamma}\gamma}$ et $\dfrac{T_A}{T_B} = \left(\dfrac{P_B}{P_A}\right)^{\frac{1-\gamma}\gamma}$.
2. Exprimer le travail $W$ et la chaleur $Q$ pour chacune des transformations du cycle ABCDA.
3. a) En déduire le rendement $r = \dfrac{Q_{BC} + Q_{DA}}{Q_{BC}}$ en fonction de $T_A$, $T_B$, $T_C$, $T_D$. b) L'exprimer en fonction de $a = \dfrac{P_B}{P_A} = \dfrac{P_C}{P_D}$ et de $\gamma$. Indice : $\dfrac{T_D - T_A}{T_C - T_B} = \dfrac{T_D}{T_C}$.
4. Exprimer la variation d'entropie $\Delta S$ pour chacune des transformations du cycle.
