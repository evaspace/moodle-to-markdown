# Partiel 2 de physique S2 — mai 2017 (sujet, FR)

- Source : `raw/S2/Finals/Phys/2021/final-2021-s2-phys-subject-fr.pdf` (6 pages, sujet scanné sans corrigé)
- Date réelle : mai 2017 (EPITA S2, dossier promo 2021). Corrigé : `final-2021-s2-phys-correction-fr.md`.
- Calculatrices et documents non autorisés, réponses sur le sujet. Noté sur 20. Thermodynamique : calorimétrie, premier principe et gaz parfait, cycle de Beau de Rochas.

## Exercice 1. Calorimétrie (5 points, parties indépendantes)
Type : calorimétrie (capacité du calorimètre, fusion d'un glaçon, mélange d'eau) · ECUE : Thermodynamique · Niveau : physique-s2-thermo/5
Formules : enceinte isolée : $\sum Q_i = 0$ ; $Q = mc(\theta_f - \theta_i)$ ; calorimètre : $Q = C_{cal}(\theta_f - \theta_i)$ ; fusion : $Q = mL_f$ ; chemin fictif glace $\theta_2 \to 0$ °C $\to$ fusion $\to$ eau $0 \to \theta_e$ ; $m = \rho V$

1. Un calorimètre de capacité négligeable contient $m_1 = 200$ g d'eau à $\theta_1 = 70$ °C. On y place un glaçon de masse $m_2 = 80$ g sortant du congélateur à $\theta_2 = -20$ °C. Exprimer les quantités de chaleur $Q$ échangées par l'eau et le glaçon, en déduire la température d'équilibre $\theta_e$, sachant que le glaçon fond en totalité. Données : $L_f = 300 \cdot 10^3\ \text{J·kg}^{-1}$, $c_e = 4 \cdot 10^3\ \text{J·K}^{-1}\text{·kg}^{-1}$, $c_g = 2 \cdot 10^3\ \text{J·K}^{-1}\text{·kg}^{-1}$.
2. Un calorimètre contient $m_1 = 150$ g d'eau ; l'ensemble est à $\theta_1 = 20$ °C. On ajoute $m_2 = 250$ g d'eau à $\theta_2 = 70$ °C. Calculer la capacité thermique $C_{cal}$ du calorimètre sachant que la température d'équilibre est $\theta_e = 50$ °C. Donnée : $c_e = 4 \cdot 10^3\ \text{J·K}^{-1}\text{·kg}^{-1}$.

## Exercice 2. Gaz parfait et premier principe (7 points, questions indépendantes)
Type : gaz parfait (dU, dH, relation de Mayer, chaleur isobare, travail isobare et adiabatique) · ECUE : Thermodynamique · Niveau : physique-s2-thermo/7
Formules : $dU = nc_vdT$, $dH = nc_pdT$ ; $H = U + PV$, $PV = nRT$ ; Mayer : $C_p - C_v = nR$ ; $dU = \delta Q + \delta W$, $\delta W = -P\,dV$ ; isobare : $W = -P(V_B - V_A)$, $\delta Q_P = nc_pdT$ ; adiabatique : $Q = 0$, $W = \Delta U = nc_v(T_B - T_A)$

1. a) Exprimer l'énergie interne élémentaire $dU$ et l'enthalpie élémentaire $dH$ d'un gaz parfait. b) En déduire la relation de Meyer $C_p - C_v = nR$, valable pour un gaz parfait.
2. a) Énoncer le premier principe donnant $dU$ en fonction de $\delta Q$ et $\delta W$. b) Utiliser ce principe et la loi de Mayer pour montrer que la chaleur échangée par $n$ moles de gaz parfait à pression constante s'écrit $\delta Q_P = nc_pdT$. (On donne $\dfrac{dV}V = \dfrac{dT}T$ lorsque la pression est constante.)
3. Exprimer le travail des forces de pression $W$ dans les cas suivants : a) détente isobare à la pression $P_A$, du volume $V_A$ au volume $V_B$ ; b) compression adiabatique de $V_A$ à $V_B$, en fonction des températures $T_A$, $T_B$ et de la capacité molaire à volume constant $c_v$.

## Exercice 3. Cycle de Beau de Rochas (8 points)
Type : cycle de Beau de Rochas (deux adiabatiques, deux isochores, rendement) · ECUE : Thermodynamique · Niveau : physique-s2-thermo/12
Formules : Laplace : $TV^{\gamma-1} = \text{cte}$ ; isochore : $W = 0$, $Q = \Delta U = nc_v\Delta T$ ; adiabatique : $Q = 0$, $W = \Delta U = nc_v\Delta T$ ; $r = \dfrac{Q_{AB} + Q_{CD}}{Q_{AB}} = 1 - \dfrac{T_C - T_D}{T_B - T_A}$ ; $a = \dfrac{V_2}{V_1}$, $r = 1 - a^{1-\gamma}$

Un moteur thermique fonctionne selon le cycle de Beau de Rochas : $n$ moles de gaz parfait décrivent le cycle ABCDA. AB : isochore à $V_1$ (la pression monte de A à B) ; BC : adiabatique de $V_1$ à $V_2$ ; CD : isochore à $V_2$ ; DA : adiabatique de $V_2$ à $V_1$. On note $a = V_2/V_1$ le taux de compression.
1. Utiliser la loi de Laplace pour montrer que $T_BV_1^{\gamma-1} = T_CV_2^{\gamma-1}$ et $T_AV_1^{\gamma-1} = T_DV_2^{\gamma-1}$.
2. Exprimer $Q$, $W$ et $\Delta U$ pour chacune des transformations du cycle, en fonction des températures.
3. a) Exprimer le rendement $r = \dfrac{Q_{AB} + Q_{CD}}{Q_{AB}}$ en fonction des températures. b) Retrouver une expression de ce rendement en fonction de $a$ et de $\gamma$. Indice : $\dfrac{T_C - T_D}{T_B - T_A} = \dfrac{T_D}{T_A} = \dfrac{T_C}{T_B}$. c) Calcul numérique pour $a = 9$, $\gamma = 1{,}4$. On donne $9^{-0{,}4} \approx 0{,}4$.
