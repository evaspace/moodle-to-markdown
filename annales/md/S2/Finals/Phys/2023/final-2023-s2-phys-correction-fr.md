# Partiel n° 2 S2 — mai 2019 (corrigé, FR)

- Source : `raw/S2/Finals/Phys/2023/final-2020-s2-phys-correction-fr.pdf` (8 pages, corrigé manuscrit scanné ; le fichier est mal nommé « 2020 » mais correspond au sujet de mai 2019)
- Date réelle : mai 2019 (EPITA S2, dossier promo 2023). Sujet : `final-2023-s2-phys-subject-fr.md`.
- Calculatrices et documents non autorisés. Réponses sur le sujet. Thermodynamique : premier principe, transformations du gaz parfait, cycle. Les lignes `> ` sont les solutions (QCM et exercice 1 relus sur le corrigé manuscrit, exercices 2 et 3 recalculés).

## QCM (4 points, sans points négatifs)
Type : QCM de thermodynamique (enthalpie, transformations du gaz parfait, Laplace) · ECUE : Thermodynamique · Niveau : physique-s2-thermo/7
Formules : $H = U + PV$ ; $dH = \delta Q + V\,dP$ (réversible) ; isotherme : $\Delta U = 0$, $Q = -W$ ; isobare : $W = -P(V_2 - V_1)$ ; isochore : $Q = nc_v\Delta T$, $\dfrac{P_1}{T_1} = \dfrac{P_2}{T_2}$ ; Laplace : $T^\gamma P^{1-\gamma} = \text{cste}$

1. La fonction d'état enthalpie est définie par : a) $H = U - PV$ ; b) $H = W + Q$ ; c) $H = U + TV$ ; d) $H = U + PV$.
> d).
2. La variation infinitésimale de l'enthalpie $dH$ lors d'une transformation réversible s'écrit : a) $dH = \delta Q + P\,dV$ ; b) $dH = \delta Q + V\,dP$ ; c) $dH = dU + V\,dP$.
> b).
3. Lorsqu'un système fermé (gaz parfait) subit une transformation isotherme, la quantité de chaleur échangée avec le milieu extérieur est : a) $Q = W$ ; b) $Q = \Delta U$ ; c) $Q = -W$ ; d) $Q = 0$.
> c) : $\Delta U = 0$ donc $Q = -W$.
4. Le travail des forces de pression de l'état (1) vers l'état (2) d'une transformation isobare s'écrit : a) $W = 0$ ; b) $W = -P(V_2 - V_1)$ ; c) $W = nRT_1\ln\left(\dfrac{V_2}{V_1}\right)$.
> b).
5. La quantité de chaleur échangée entre un gaz parfait et le milieu extérieur lors d'une transformation isochore réversible est : a) $Q = nc_p\Delta T$ ; b) $Q = nc_v\Delta T$ ; c) $Q = nR\Delta T$.
> b).
6. Laquelle parmi les grandeurs suivantes n'est pas une fonction d'état ? a) l'enthalpie $H$ ; b) l'énergie interne $U$ ; c) la quantité de chaleur $Q$.
> c).
7. Les grandeurs d'état température et pression d'un gaz parfait qui subit une transformation isochore de l'état (1) vers l'état (2) vérifient : a) $T_1P_2 = T_2P_1$ ; b) $T_1P_1 = T_2P_2$ ; c) $\dfrac{T_1}{P_2} = \dfrac{P_1}{T_2}$.
> a) : $\dfrac{P}{T} = \dfrac{nR}{V}$ est constant.
8. La loi de Laplace écrite en fonction de la température et de la pression donne ($C$ constante) : a) $TP^{\gamma-1} = C$ ; b) $T^\gamma P^{\gamma-1} = C$ ; c) $TP^{\gamma+1} = C$ ; d) $T^\gamma P^{1-\gamma} = C$.
> d).

## Exercice 1. Compression isotherme puis compression adiabatique (6 points)
Type : transformation isotherme et adiabatique du gaz parfait (Q, W, pression, volume, température) · ECUE : Thermodynamique · Niveau : physique-s2-thermo/7
Formules : isotherme : $\Delta U = 0$, $Q = -W$, $P_1V_1 = P_2V_2$, $W = -nRT\ln\dfrac{V_2}{V_1} = -P_1V_1\ln\dfrac{V_2}{V_1}$ ; $PV = nRT$ ; adiabatique : $Q = 0$, $W = \Delta U = nc_v\Delta T$, $c_v = \tfrac32R$ (monoatomique) ; Laplace : $P^{1-\gamma}T^\gamma = \text{cste}$

Les deux parties sont indépendantes.

**I. Compression isotherme.** Un gaz parfait, contenu dans un cylindre fermé par un piston et placé dans un four, subit une compression isotherme réversible d'un volume $V_1$ au volume $V_2 = \dfrac{V_1}{10}$. La pression initiale est $P_1 = 1$ bar. Le travail fourni au système gazeux est $W_{12} = 420$ J. $R = 8{,}3\ \text{J·mol}^{-1}\text{·K}^{-1}$.
1. Calculer la quantité de chaleur cédée au milieu extérieur $Q_{12}$.
> Isotherme : $\Delta T = 0$ donc $\Delta U = nc_v\Delta T = 0 = Q_{12} + W_{12}$, d'où $Q_{12} = -W_{12} = -420$ J.
2. Donner l'expression de la pression finale $P_2$ en fonction de $P_1$, puis sa valeur en bar.
> Isotherme et gaz parfait : $PV = \text{cste}$, donc $P_2 = P_1\dfrac{V_1}{V_2} = 10P_1 = 10$ bar.
3. Donner l'expression du volume $V_1$ en fonction de $W_{12}$ et $P_1$, puis l'application numérique en litres arrondie à un chiffre après la virgule. On donne $\ln(10) = 2{,}3$.
> $W_{12} = -nRT_1\ln\dfrac{V_2}{V_1} = -P_1V_1\ln\dfrac{1}{10} = P_1V_1\ln 10$, donc $V_1 = \dfrac{W_{12}}{P_1\ln 10} = \dfrac{420}{10^5 \times 2{,}3} \approx 1{,}8\cdot10^{-3}\ \text{m}^3 = 1{,}8$ L.
4. Déterminer l'expression de la température $T$, en fonction de $P_1$, $V_1$, $n$ et $R$, à laquelle s'effectuerait la compression s'il y avait $n = 0{,}02$ mol de gaz. Donner une estimation de la température en kelvin (un entier multiplié par une puissance de 10).
> $T = \dfrac{P_1V_1}{nR} = \dfrac{10^5 \times 1{,}8\cdot10^{-3}}{0{,}02 \times 8{,}3} \approx 1{,}1\cdot10^3$ K, soit environ $10^3$ K.

**II. Compression adiabatique.** La compression adiabatique et réversible de $n = 1$ mol de gaz parfait monoatomique élève la température de ce gaz de $\Delta T = 100$ °C. $R = 8{,}3\ \text{J·mol}^{-1}\text{·K}^{-1}$.
1. Donner la quantité de chaleur échangée avec l'extérieur $Q_{12}$ lors de la compression ; justifier.
> Adiabatique : pas d'échange de chaleur, $Q_{12} = 0$.
2. Déterminer l'expression du travail $W_{12}$ nécessaire pour réaliser cette compression en fonction de $n$, $R$ et $\Delta T$. Application numérique en joules arrondie à l'unité.
> $\Delta U = W_{12} + Q_{12} = W_{12}$ et $\Delta U = nc_v\Delta T$ avec $c_v = \tfrac32R$ : $W_{12} = \tfrac32nR\Delta T = 1{,}5 \times 8{,}3 \times 100 = 1245$ J.
3. Donner l'expression de la pression finale du gaz $P_2$ en fonction de la pression initiale $P_1$, de la température initiale $T_1$, de l'élévation de température $\Delta T$ et du coefficient de Laplace $\gamma$.
> Laplace : $P_1^{1-\gamma}T_1^\gamma = P_2^{1-\gamma}T_2^\gamma$ avec $T_2 = T_1 + \Delta T$, donc $P_2 = P_1\left(\dfrac{T_1 + \Delta T}{T_1}\right)^{\frac{\gamma}{\gamma-1}}$.

## Exercice 2. Trois chemins entre deux états (5 points)
Type : travail et chaleur selon le chemin (isochores, isobares, droite dans le diagramme de Clapeyron) · ECUE : Thermodynamique · Niveau : physique-s2-thermo/9
Formules : $PV = nRT$ ; isochore : $W = 0$, $Q = nc_v\Delta T$ ; isobare : $W = -P\Delta V$, $Q = nc_p\Delta T$ ; $W = -\displaystyle\int P\,dV$ (aire sous la courbe) ; $\Delta U = nc_v\Delta T = W + Q$

Une mole de gaz parfait, de capacité thermique molaire à volume constant $c_v = \tfrac52R$ et à pression constante $c_p = \tfrac72R$, est prise dans l'état $a$ $(V_1, P_1)$. On lui fait décrire le chemin de $a$ à $b$ $(V_2, P_2)$ de trois manières : le chemin $acb$, le chemin $adb$ et le chemin direct $ab$ (segment de droite dans le diagramme $(P, V)$). On pose $P_2 = 2P_1$ et $V_2 = 2V_1$. Les points $a$ et $b$ appartiennent respectivement aux isothermes $T_1$ et $T_2$. Toutes les transformations sont réversibles. $ac$ et $db$ sont isochores, $cb$ et $ad$ sont isobares (donc $c = (V_1, P_2)$ et $d = (V_2, P_1)$).
1. Montrer que $T_2 = 4T_1$ et $T_c = T_d = 2T_1$.
> $T = \dfrac{PV}{R}$ : $T_2 = \dfrac{2P_1 \cdot 2V_1}{R} = 4T_1$, $T_c = \dfrac{2P_1V_1}{R} = 2T_1$, $T_d = \dfrac{P_1 \cdot 2V_1}{R} = 2T_1$.
2. a) Exprimer les travaux $W_{ac}$, $W_{cb}$ et en déduire $W_{acb}$ en fonction de $T_1$ et $R$. b) Même chose pour $W_{ad}$, $W_{db}$, $W_{adb}$. c) Exprimer $W_{ab}$ sur le chemin direct (exprimer la pression en fonction du volume sur la droite $(ab)$). d) Comparer $W_{acb}$, $W_{adb}$ et $W_{ab}$. Conclure.
> a) $W_{ac} = 0$ (isochore), $W_{cb} = -P_2(V_2 - V_1) = -2P_1V_1 = -2RT_1$, donc $W_{acb} = -2RT_1$.
> b) $W_{ad} = -P_1(V_2 - V_1) = -RT_1$, $W_{db} = 0$, donc $W_{adb} = -RT_1$.
> c) Sur la droite, $P = \dfrac{P_1}{V_1}V$ ; $W_{ab} = -\displaystyle\int_{V_1}^{2V_1}\dfrac{P_1}{V_1}V\,dV = -\tfrac32P_1V_1 = -\tfrac32RT_1$.
> d) $W_{acb} \ne W_{ab} \ne W_{adb}$ : le travail dépend du chemin suivi, ce n'est pas une fonction d'état.
3. Reprendre les questions 2a à 2d pour la quantité de chaleur $Q$ échangée avec le milieu extérieur, en fonction de $T_1$ et $R$.
> $\Delta U_{ab} = c_v(T_2 - T_1) = \tfrac{15}{2}RT_1$ sur les trois chemins.
> a) $Q_{ac} = c_v(T_c - T_1) = \tfrac52RT_1$, $Q_{cb} = c_p(T_2 - T_c) = 7RT_1$, $Q_{acb} = \tfrac{19}{2}RT_1$.
> b) $Q_{ad} = c_p(T_d - T_1) = \tfrac72RT_1$, $Q_{db} = c_v(T_2 - T_d) = 5RT_1$, $Q_{adb} = \tfrac{17}{2}RT_1$.
> c) $Q_{ab} = \Delta U - W_{ab} = \tfrac{15}{2}RT_1 + \tfrac32RT_1 = 9RT_1$.
> d) $Q$ dépend aussi du chemin ; seule la somme $W + Q = \Delta U$ est la même : $U$ est une fonction d'état.

## Exercice 3. Cycle réversible (5 points)
Type : cycle adiabatique, isochore, isotherme (chaleur et travail reçus, Laplace) · ECUE : Thermodynamique · Niveau : physique-s2-thermo/8
Formules : Laplace : $PV^\gamma = \text{cste}$, $TV^{\gamma-1} = \text{cste}$ ; adiabatique : $Q = 0$, $W = \Delta U = \dfrac{P_BV_B - P_AV_A}{\gamma - 1}$ ; isochore : $W = 0$ ; isotherme : $Q = -W = nRT\ln\dfrac{V_f}{V_i}$

Une mole de gaz parfait de coefficient de Laplace $\gamma = C_p/C_v$ constant occupe à l'équilibre un volume $V_1$ à la température $T_1$ sous la pression $P_1$ (état A). On le comprime de façon réversible et adiabatique jusqu'au volume $V_2 = V_1/4$ (état B). On laisse le gaz revenir à la température $T_1$ à volume constant (état C). Le gaz est ensuite détendu de façon réversible et isotherme jusqu'au volume $V_1$ (état A).
1. Représenter le cycle ABCA dans un diagramme $(P, V)$.
> A $(V_1, P_1)$ ; B $(V_1/4, 4^\gamma P_1)$ sur une adiabatique ; C $(V_1/4, 4P_1)$ à la verticale de B, plus bas ; retour de C à A sur l'isotherme $T_1$ (hyperbole), au-dessous de l'adiabatique. Le cycle est parcouru dans le sens trigonométrique (récepteur).
2. Donner l'expression de la chaleur reçue en fonction de $P_1$, $V_1$. Préciser le chemin.
> Seul le chemin CA reçoit de la chaleur (AB : $Q = 0$ ; BC : refroidissement, $Q < 0$). $Q_{CA} = -W_{CA} = RT_1\ln\dfrac{V_1}{V_1/4} = P_1V_1\ln 4$.
3. Donner l'expression du travail reçu en fonction de $P_1$, $V_1$ et $\gamma$. Préciser le chemin.
> Le gaz reçoit du travail sur AB (compression ; BC : $W = 0$, CA : détente, $W < 0$). $W_{AB} = \Delta U_{AB} = \dfrac{P_BV_B - P_1V_1}{\gamma - 1} = \dfrac{P_1V_1(4^{\gamma-1} - 1)}{\gamma - 1}$.
4. Exprimer la pression $P_C$ au point C en fonction de $P_1$.
> C et A sont sur l'isotherme $T_1$ : $P_C\dfrac{V_1}{4} = P_1V_1$, donc $P_C = 4P_1$.
5. a) Utiliser la loi de Laplace pour exprimer la pression $P_B$ en fonction de $P_1$ et $\gamma$. b) En déduire la température $T_B$ en fonction de $T_1$ et $\gamma$.
> a) $P_BV_2^\gamma = P_1V_1^\gamma$ donc $P_B = 4^\gamma P_1$.
> b) $T_B = \dfrac{P_BV_2}{R} = \dfrac{4^\gamma P_1 V_1}{4R} = 4^{\gamma-1}T_1$.
