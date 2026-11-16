# Examen de physique S2 : thermodynamique — mai 2024 (corrigé, FR)

- Source : `raw/S2/Finals/Phys/2028/final-2028-s2-phys-correction-fr.pdf` (5 pages, corrigé tapé, surtout les calculs)
- Date réelle : mai 2024 (EPITA S2, dossier promo 2028), durée 1 h 30. Sujet : `final-2028-s2-phys-subject-fr.md`.
- Calculatrices et documents non autorisés. Thermodynamique : calorimétrie, cycle de Lenoir dans le diagramme de Watt, machine ditherme. Les lignes `> ` sont les solutions (reprises du corrigé, rédigées quand il ne donne que le calcul).

## Exercice 1. Questions de cours (5 points, pas de points négatifs)
Type : QCM de thermodynamique (intensif, isobare, travail, force de pression, unités) · ECUE : Thermodynamique · Niveau : physique-s2-thermo/3
Formules : intensive : $P$, $T$ ; extensive : $V$, $m$ ; isobare : $P = \text{cste}$, $W = -P_0(V_f - V_i)$ ; $d\vec F = P\,d\vec S$ ; énergie en joules (J)

Pour certaines questions il faut cocher plusieurs bonnes réponses.
1. Entourer les variables d'état intensives : a) pression ; b) température ; c) volume ; d) masse.
> a) et b).
2. Une transformation isobare est une transformation où : a) la température est constante ; b) la pression du gaz est constante ; c) le volume est constant ; d) la force est constante.
> b).
3. Pour une transformation isobare et réversible d'un gaz parfait, le travail vaut : a) $W = 0$ ; b) $W = nRT\ln\left(\dfrac{V_{initial}}{V_{final}}\right)$ ; c) $W = -P_0(V_{initial} - V_{final})$ ; d) $W = -P_0(V_{final} - V_{initial})$.
> d).
4. La relation traduisant la force élémentaire de pression est : a) $dF = P\,ds$ ; b) $d\vec F = P\,d\vec s$ ; c) $d\vec F = mg\,d\vec s$ ; d) $d\vec P = F\,d\vec s$.
> b).
5. L'énergie s'exprime : a) en kg ; b) en J ; c) en m ; d) en N.
> b).

## Exercice 2. Capacité thermique du cuivre (6 points)
Type : calorimétrie (bilan d'enthalpie dans une enceinte isolée, capacité thermique massique) · ECUE : Thermodynamique · Niveau : physique-s2-thermo/4
Formules : $\Delta H = mc(T_f - T_i)$ ; enceinte isolée, isobare : $\sum\Delta H = 0$ ; $c_{cuivre} = -\dfrac{m_{eau}c_{eau}(T_f - T_{eau})}{m_{cuivre}(T_f - T_{cuivre})}$

On veut mesurer la capacité thermique massique du cuivre. Dans un récipient parfaitement isolé on met $m_{eau} = 100$ g d'eau à $T_{eau} = 25$ °C, puis on plonge une barre de cuivre de $m_{cuivre} = 200$ g à $T_{cuivre} = 60$ °C. À l'équilibre, la température est $T_f = 30$ °C. On prend $c_{eau} = 4\ \text{kJ·kg}^{-1}\text{·K}^{-1}$.
1. Expliquer le sens du transfert thermique.
> Du corps chaud vers le corps froid : le cuivre (60 °C) cède de la chaleur à l'eau (25 °C).
2. Donner l'expression de $\Delta H_{eau}$.
> $\Delta H_{eau} = m_{eau}c_{eau}(T_f - T_{eau})$.
3. Donner l'expression de $\Delta H_{cuivre}$.
> $\Delta H_{cuivre} = m_{cuivre}c_{cuivre}(T_f - T_{cuivre})$.
4. Quel lien existe-t-il entre $\Delta H_{eau}$ et $\Delta H_{cuivre}$ ? Justifier à l'aide de l'énoncé.
> Le récipient est isolé et la transformation se fait à pression constante : $\Delta H_{eau} + \Delta H_{cuivre} = 0$.
5. En déduire l'expression littérale de la capacité thermique du cuivre.
> $c_{cuivre} = -\dfrac{m_{eau}c_{eau}(T_f - T_{eau})}{m_{cuivre}(T_f - T_{cuivre})}$.
6. Application numérique : ordre de grandeur, comparaison avec l'eau.
> $c_{cuivre} = -\dfrac{0{,}1 \times 4 \times 5}{0{,}2 \times (-30)} = \dfrac13\ \text{kJ·kg}^{-1}\text{·K}^{-1} \approx 0{,}33\ \text{kJ·kg}^{-1}\text{·K}^{-1}$, environ 12 fois moins que l'eau.

## Exercice 3. Machine thermique et cycle de Lenoir (5 points)
Type : cycle de Lenoir dans le diagramme de Watt (isochore, isotherme, isobare, travaux) · ECUE : Thermodynamique · Niveau : physique-s2-thermo/12
Formules : isotherme : $P = \dfrac{nRT}{V}$ (hyperbole) ; isochore : $W = 0$ ; isotherme : $W = -nRT\ln\dfrac{V_f}{V_i}$ ; isobare : $W = -P(V_f - V_i)$ ; $PV = nRT$

Le cycle de Lenoir est un modèle idéalisé de cycle moteur à deux temps. L'air de la chambre de combustion, modélisé par un gaz parfait, est dans l'état 1 : $T_1 = 100$ °C, $V_1 = 10$ L, $P_1 = 2\cdot10^5$ Pa ; il forme un système fermé de $n_0$ moles. Le cycle comporte :
- 1 → 2 : explosion isochore jusqu'à la pression $P_2$ ;
- 2 → 3 : détente isotherme jusqu'à $V_3 = 2V_1$ ;
- 3 → 1 : compression isobare jusqu'au volume initial.

On représente le cycle dans le diagramme de Watt $(P, V)$ ; les transformations sont quasi statiques.
1. Déterminer l'équation d'une isotherme quasi statique d'un gaz parfait dans le diagramme de Watt.
> $PV = nRT$ donc $P = \dfrac{nRT}{V}$ : une branche d'hyperbole.
2. En déduire la représentation du cycle (faire apparaître $V_1$, $V_3$, $P_1$, $P_2$).
> 3 → 1 est à la pression $P_1$, donc $P_3 = P_1$ ; sur l'isotherme 2 → 3, $P_2V_1 = P_1 \cdot 2V_1$, donc $P_2 = 2P_1$. Segment vertical de $(V_1, P_1)$ à $(V_1, 2P_1)$, hyperbole jusqu'à $(2V_1, P_1)$, segment horizontal de retour.
3. Donner le travail pour chacune des étapes.
> $W_{12} = 0$ (isochore).
> $W_{23} = -\displaystyle\int_{V_1}^{2V_1}\dfrac{nRT_2}{V}dV = -nRT_2\ln 2 = -P_2V_1\ln2 = -2P_1V_1\ln 2 \approx -2{,}8$ kJ.
> $W_{31} = -P_1(V_1 - V_3) = P_1V_1 = 2$ kJ. Travail total $\approx -0{,}8$ kJ $< 0$ : le cycle est moteur.

## Exercice 4. Rendement d'un moteur (4 points)
Type : machine ditherme réversible (premier et deuxième principes, rendement de Carnot) · ECUE : Thermodynamique · Niveau : physique-s2-thermo/11
Formules : sur un cycle : $\Delta U = Q_c + Q_f + W = 0$ ; $\Delta S = \dfrac{Q_c}{T_c} + \dfrac{Q_f}{T_f} + S_{créée} = 0$, $S_{créée} = 0$ (réversible) ; $\rho = \left|\dfrac{\text{énergie utile}}{\text{énergie coûteuse}}\right| = -\dfrac{W}{Q_c} = 1 + \dfrac{Q_f}{Q_c} = 1 - \dfrac{T_f}{T_c}$

Une machine échange de la chaleur $Q_f$ avec une source froide $T_f$, de la chaleur $Q_c$ avec une source chaude $T_c$, et du travail $W$ avec le milieu extérieur. Toutes les transformations sont réversibles.
1. Énoncer le premier principe avec ces notations. Que peut-on dire de la variation d'énergie interne ? Justifier.
> $\Delta U = Q_c + Q_f + W$. Sur un cycle, $U$ est une fonction d'état : $\Delta U = 0$.
2. Citer le deuxième principe avec ces notations ($S_{créée}$ est nulle ici).
> $\Delta S = S_{échangée} + S_{créée} = \dfrac{Q_c}{T_c} + \dfrac{Q_f}{T_f} = 0$ sur un cycle.
3. Le rendement est le rapport de l'énergie utile sur l'énergie coûteuse. L'exprimer en fonction de $Q_c$ et $Q_f$, puis de $T_c$ et $T_f$.
> $\rho = -\dfrac{W}{Q_c} = \dfrac{Q_c + Q_f}{Q_c} = 1 + \dfrac{Q_f}{Q_c}$ ; avec $\dfrac{Q_f}{Q_c} = -\dfrac{T_f}{T_c}$ : $\rho = 1 - \dfrac{T_f}{T_c}$.
