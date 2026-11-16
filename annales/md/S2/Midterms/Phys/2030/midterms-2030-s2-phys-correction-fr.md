# Contrôle de physique S2 : thermodynamique — promo 2030 (corrigé, FR)

- Source : `raw/S2/Midterms/Phys/2030/midterms-2030-s2-phys-correction-fr.pdf` (3 pages, corrigé tapé ; le sujet n'est pas dans le dépôt)
- Date réelle : S2 2025-2026 (EPITA, dossier promo 2030). Pas de sujet : les énoncés ci-dessous sont reconstitués à partir du corrigé (données déduites des applications numériques).
- Thermodynamique : calorimétrie avec changement d'état, machine frigorifique. Les lignes `> ` sont les solutions du corrigé.

## Exercice 1. Chaleur latente de fusion de la glace (10 points)
Type : calorimétrie avec changement d'état (chemin fictif, chaleur latente de fusion) · ECUE : Thermodynamique · Niveau : physique-s2-thermo/5
Formules : $\Delta H = mc\Delta T$ sans changement d'état ; fusion à 0 °C : $\Delta H = m\,\Delta h_F$ ; enceinte isolée, isobare : $\sum\Delta H = 0$ ; chemin fictif : échauffement de la glace, fusion, puis échauffement ou refroidissement de l'eau liquide

Énoncé reconstitué. Dans un calorimètre parfaitement isolé, on verse $m_{liq} = 100$ g d'eau liquide à $T_{liq} = 30$ °C et on ajoute $m_{gl} = 20$ g de glace à $T_{gl} = -20$ °C. À l'équilibre, toute la glace a fondu et la température finale est $T_F = 10$ °C. On donne $c_{glace} = 2000\ \text{J·kg}^{-1}\text{·K}^{-1}$ et $c_{eau} = 4000\ \text{J·kg}^{-1}\text{·K}^{-1}$. On cherche la chaleur latente massique de fusion $\Delta h_F$ de la glace.
1. Compléter le schéma du chemin fictif entre l'état initial (liquide $m_{liq}$, $T_{liq}$ ; solide $m_{gl}$, $T_{gl}$) et l'état final (liquide $m_{liq} + m_{gl}$, $T_F$).
> $\Delta H_1$ : la glace se réchauffe de $T_{gl}$ à 0 °C ; $\Delta H_2$ : la glace fond en totalité à 0 °C ; $\Delta H_3$ : les deux masses d'eau liquide atteignent $T_F$.
2. Calculer la variation d'enthalpie de l'eau solide (glace qui se réchauffe).
> $\Delta H_1 = m_{gl}c_{glace}(0 - T_{gl}) = 0{,}02 \times 2000 \times 20 = 400$ J.
3. Exprimer la variation d'enthalpie lors de la fusion.
> $\Delta H_2 = m_{gl}\,\Delta h_F$.
4. Calculer la variation d'enthalpie de l'eau liquide.
> $\Delta H_3 = m_{gl}c_{eau}(T_F - 0) + m_{liq}c_{eau}(T_F - T_{liq}) = 0{,}02 \times 4000 \times 10 + 0{,}1 \times 4000 \times (-20) = 800 - 8000 = -7200$ J.
5. En déduire $\Delta h_F$.
> $\Delta H = \Delta H_1 + \Delta H_2 + \Delta H_3 = 0$, donc $m_{gl}\Delta h_F = 7200 - 400 = 6800$ J et $\Delta h_F = \dfrac{6800}{0{,}02} = 340\,000\ \text{J/kg}$.

## Exercice 2. Efficacité d'une machine frigorifique (10 points)
Type : machine frigorifique ditherme (signes des échanges, premier et deuxième principes, efficacité de Carnot) · ECUE : Thermodynamique · Niveau : physique-s2-thermo/11
Formules : sur un cycle : $\Delta U = Q_c + Q_f + W = 0$ ; $\Delta S = \dfrac{Q_c}{T_c} + \dfrac{Q_f}{T_f} + S_{créée} = 0$ ; réfrigérateur : $Q_f > 0$, $Q_c < 0$, $W > 0$ ; $e = \dfrac{Q_f}{W} = -\dfrac{1}{1 + Q_c/Q_f}$ ; réversible : $e = \dfrac{T_f}{T_c - T_f}$ ; $T(\text{K}) = T(°\text{C}) + 273$

Énoncé reconstitué. Un réfrigérateur fonctionne entre l'air extérieur (source chaude, $T_c = 25$ °C) et l'air intérieur (source froide, $T_f = 5$ °C). Le fluide reçoit le travail $W$ (électrique) et échange $Q_c$ et $Q_f$ avec les sources.
1. Représenter les échanges d'énergie et donner leurs signes.
> Le fluide prend de la chaleur à l'intérieur ($Q_f > 0$), en rend à l'extérieur ($Q_c < 0$) et reçoit du travail ($W > 0$).
2. Écrire le premier principe sur un cycle ; préciser chaque terme.
> $\Delta U = W + Q_c + Q_f = 0$ : $\Delta U$ variation d'énergie interne (J), $Q$ échanges thermiques (J), $W$ travail échangé (J).
3. Exprimer l'efficacité $e$ en fonction de $Q_c$ et $Q_f$.
> $W = -(Q_c + Q_f)$ donc $e = \dfrac{Q_f}{W} = -\dfrac{Q_f}{Q_c + Q_f} = -\dfrac{1}{1 + Q_c/Q_f}$.
4. Écrire le deuxième principe sur un cycle (variation d'entropie, entropie échangée, entropie créée, en J/K).
> $\Delta S = S_{éch} + S_{créée} = \dfrac{Q_c}{T_c} + \dfrac{Q_f}{T_f} + S_{créée} = 0$.
5. Si $S_{créée} = 0$, exprimer $e$ en fonction des températures.
> $\dfrac{Q_c}{Q_f} = -\dfrac{T_c}{T_f}$, d'où $e = \dfrac{T_f}{T_c - T_f}$.
6. Application numérique ; interpréter.
> $e = \dfrac{278}{298 - 278} = \dfrac{278}{20} \approx 14$ : pour 1 J d'énergie électrique fournie, la machine retire 14 J à l'intérieur du réfrigérateur.
