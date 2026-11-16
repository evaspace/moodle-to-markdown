# Examen de physique S2 : thermodynamique — mai 2025 (corrigé rédigé, FR)

- Source : `raw/S2/Finals/Phys/2029/midterm-2029-s2-phys-subject-fr.pdf` (6 pages, sujet scanné, fichier mal nommé « midterm » ; pas de corrigé officiel dans le dépôt)
- Date réelle : mai 2025 (EPITA InfoS2, dossier promo 2029), durée 1 h 30. Sujet : `final-2029-s2-phys-subject-fr.md`.
- Calculatrices et documents non autorisés. Thermodynamique : premier principe, changement d'état, cycle du gaz parfait. Les lignes `> ` sont un corrigé rédigé (pas officiel), applications numériques vérifiées par calcul.

## Exercice 1. Questions de cours (5 points, pas de points négatifs)
Type : QCM de thermodynamique (gaz qui refroidit, cycle, isochore, pompe à chaleur, conduction) · ECUE : Thermodynamique · Niveau : physique-s2-thermo/6
Formules : $PV = nRT$ ; sur un cycle : état initial = état final, $\Delta U = 0$ ; isochore : $W = 0$, $Q = \Delta U$ ; pompe à chaleur : énergie utile = chaleur cédée à la source chaude ; conduction : transfert sans déplacement de matière

Pour certaines questions plusieurs réponses sont à cocher.
1. Un ballon de baudruche rempli d'air à 20 °C est plongé dans l'eau à 5 °C. On peut dire que : a) le volume du ballon va augmenter ; b) le volume du ballon va diminuer ; c) la température de l'air augmente ; d) la température de l'air diminue.
> b) et d) : l'air se refroidit et, à pression à peu près constante, $V = \dfrac{nRT}{P}$ diminue.
2. Lors d'un cycle thermodynamique, $\Delta U = 0$ car : a) c'est une hypothèse de la thermodynamique ; b) l'état initial et l'état final sont identiques ; c) c'est une approximation pratique pour la modélisation ; d) aucune des réponses précédentes.
> b) : $U$ est une fonction d'état.
3. Lors d'une transformation isochore, le transfert thermique $Q$ est égal à : a) $W$ ; b) $-W$ ; c) $\Delta U$ ; d) $-\Delta U$.
> c).
4. Dans le cas d'une pompe à chaleur, l'énergie utile est : a) le travail ; b) le transfert thermique vers la source chaude ; c) le transfert thermique vers la source froide ; d) cela dépend de la pompe à chaleur.
> b).
5. Le transfert thermique sans déplacement de matière, dû à une différence de température entre deux endroits d'un même objet, est : a) la conduction ; b) la convection ; c) le rayonnement ; d) la subduction.
> a).

## Exercice 2. Vaporisation de l'eau (6,5 points)
Type : calorimétrie avec vaporisation partielle (bilan d'enthalpie, masse vaporisée) · ECUE : Thermodynamique · Niveau : physique-s2-thermo/5
Formules : $\Delta H = mc_p\Delta T$ sans changement d'état ; $\Delta H = m\,\Delta h_{vap}$ pour la vaporisation ; enceinte calorifugée, isobare : $\sum\Delta H = 0$ ; $m_{vap} = \dfrac{-m_{fer}c_{fer}(T_f - T_{fer}) - m_{eau}c_{eau}(T_f - T_{eau})}{\Delta h_{vap}}$

On plonge un bloc de fer de masse $m_{fer} = 1$ kg à la température initiale $T_{fer} = 1100$ °C dans une masse $m_{eau} = 1$ kg d'eau liquide à $T_{eau} = 0$ °C. Le tout est enfermé dans une enceinte parfaitement calorifugée. La pression extérieure reste constante, $P_{ext} = 1$ bar. On suppose que la température finale est $T_f = 100$ °C et qu'une partie de l'eau, $m_{vap}$, est vaporisée.

Données (certaines sont inutiles) :

| | $T_{fus}$ (°C) | $T_{vap}$ (°C) | $\Delta h_{fus}$ (kJ/kg) | $\Delta h_{vap}$ (kJ/kg) | $c_p$ (kJ·kg⁻¹·K⁻¹) |
|---|---|---|---|---|---|
| Eau | 0 | 100 | 300 | 2000 | 4 |
| Fer | 1535 | 2750 | 200 | 5000 | 0,5 |

1. Donner $\Delta H_1$, variation d'enthalpie de l'eau due à sa variation de température. Application numérique.
> $\Delta H_1 = m_{eau}c_{eau}(T_f - T_{eau}) = 1 \times 4 \times 100 = 400$ kJ.
2. Donner $\Delta H_2$, variation d'enthalpie de l'eau due à son changement d'état.
> $\Delta H_2 = m_{vap}\,\Delta h_{vap}$.
3. Sous quel état est le fer au début de l'expérience ? Donner $\Delta H_3$, variation d'enthalpie du fer. Application numérique.
> Solide ($1100\ °\text{C} < T_{fus} = 1535$ °C) ; il reste solide. $\Delta H_3 = m_{fer}c_{fer}(T_f - T_{fer}) = 1 \times 0{,}5 \times (-1000) = -500$ kJ.
4. Quel lien existe-t-il entre ces variations d'enthalpie ? Justifier à l'aide de l'énoncé.
> Enceinte calorifugée et pression constante : $Q = \Delta H = 0$, donc $\Delta H_1 + \Delta H_2 + \Delta H_3 = 0$.
5. Donner l'expression de la masse d'eau vaporisée puis l'application numérique.
> $m_{vap} = -\dfrac{\Delta H_1 + \Delta H_3}{\Delta h_{vap}} = \dfrac{500 - 400}{2000} = 0{,}05$ kg $= 50$ g.

## Exercice 3. Cycle thermodynamique (8,5 points)
Type : cycle isotherme, isobare, isochore du gaz parfait (volumes, travaux, bilan) · ECUE : Thermodynamique · Niveau : physique-s2-thermo/7
Formules : $PV = nRT$ ; isotherme : $P_AV_A = P_BV_B$, $W = -nRT\ln\dfrac{V_f}{V_i}$ ; isobare : $W = -P(V_f - V_i)$ ; isochore : $W = 0$ ; sur un cycle : $\sum W + \sum Q = \Delta U = 0$

Une mole de gaz parfait dans un cylindre décrit de manière quasi statique et mécaniquement réversible le cycle ABCA : AB à la température constante $T_A = 300$ K, avec $P_A = 1{,}0$ bar ; BC à la pression $P_B = 5{,}0$ bar ; dans le diagramme $(P, V)$, C est à la verticale de A. Données : $R \approx 8{,}314\ \text{J·K}^{-1}\text{·mol}^{-1}$, $1\ \text{m}^3 = 1000$ L, $1\ \text{bar} = 10^5$ Pa, $\ln 5 \approx 1{,}5$, $\ln(1/5) \approx -1{,}5$, $8{,}314 \times 3 \approx 25$.
1. Rappeler l'équation des gaz parfaits.
> $PV = nRT$.
2. Donner la nature des transformations AB, BC et CA.
> AB : isotherme (compression) ; BC : isobare (détente) ; CA : isochore (refroidissement).
3. Donner les volumes $V_A$, $V_B$ et $V_C$ en litres, en justifiant.
> $V_A = \dfrac{RT_A}{P_A} = \dfrac{8{,}314 \times 300}{10^5} \approx 25$ L. Isotherme : $V_B = V_A\dfrac{P_A}{P_B} = 5$ L. CA isochore : $V_C = V_A = 25$ L.
4. Donner les expressions des travaux $W_{AB}$, $W_{BC}$ et $W_{CA}$ puis les applications numériques.
> $W_{AB} = -RT_A\ln\dfrac{V_B}{V_A} = -2500 \times (-1{,}5) = 3{,}75$ kJ.
> $W_{BC} = -P_B(V_C - V_B) = -5\cdot10^5 \times 20\cdot10^{-3} = -10$ kJ.
> $W_{CA} = 0$.

On donne les transferts thermiques : $Q_{AB} = -3{,}75$ kJ, $Q_{BC} = 25$ kJ, $Q_{CA} = -15$ kJ.

5. Sommer les travaux et les transferts thermiques échangés pendant un cycle et commenter.
> $\sum W = -6{,}25$ kJ et $\sum Q = 6{,}25$ kJ : $\sum W + \sum Q = 0 = \Delta U_{cycle}$, conforme au premier principe. $\sum W < 0$ : le cycle fournit du travail (moteur).
