# Contrôle de physique S2 — vers 2021 (sujet, FR)

- Source : `raw/S2/Midterms/Phys/2025/midterm-2025-s2-phys-correction-fr.pdf` (corrigé seul, 8 pages ; énoncés recopiés du corrigé, page 1 avec les QCM 1 à 5 absente)
- Date réelle : non indiquée sur les pages scannées (EPITA S2, dossier promo 2025, donc vraisemblablement printemps 2021). Corrigé : `midterm-2025-s2-phys-correction-fr.md`.
- Thermodynamique : calorimétrie, transferts thermiques à travers une paroi ; mécanique : pendule simple (énergie, petites oscillations, base polaire).

## QCM (questions 6 à 8 ; 1 à 5 absentes du scan)
Type : QCM de thermodynamique et de mécanique (force non conservative, grandeur intensive, premier principe élémentaire) · ECUE : Thermodynamique
Formules : force non conservative : frottement (travail dépendant du chemin) ; conservatives : poids, rappel du ressort, force électrique ; intensive : température, pression ; extensive : masse, volume ; $dU = \delta Q + \delta W = \delta Q - P\,dV$

6. Laquelle parmi les forces suivantes n'est pas conservative ? a) le poids $\vec P$ ; b) la tension du ressort $\vec T$ ; c) la force électrique $\vec F_e$ ; d) la force de frottement $\vec f$.
7. Laquelle parmi les grandeurs suivantes est intensive ? a) la masse ; b) le volume ; c) la température.
8. Le premier principe de la thermodynamique à l'échelle élémentaire est : a) $dQ - P\,dV$ ; b) $dQ + P\,dV$ ; c) $dQ - V\,dP$.

## Exercice 1. Calorimétrie (4 points)
Type : calorimétrie (capacité du calorimètre avec un bloc de plomb) · ECUE : Thermodynamique · Niveau : physique-s2-thermo/4
Formules : calorimètre isolé : $\sum Q_i = 0$ ; $Q = mc(\theta_e - \theta_i)$ ; calorimètre : $Q = C_{cal}(\theta_e - \theta_i)$, à la température initiale de l'eau qu'il contient

On sort un bloc de plomb de masse $m_1 = 300$ g d'une étuve à $\theta_1 = 98$ °C. On le plonge dans un calorimètre contenant $m_2 = 350$ g d'eau. L'ensemble (calorimètre + eau) est à $\theta_2 = 16$ °C. La température d'équilibre est $\theta_e = 18$ °C. Calculer la capacité thermique du calorimètre. Données : $c_{eau} = 4 \cdot 10^3\ \text{J·K}^{-1}\text{·kg}^{-1}$, $c_{plomb} = 150\ \text{J·K}^{-1}\text{·kg}^{-1}$.

## Exercice 2. Transferts thermiques à travers une paroi (6 points)
Type : résistances thermiques d'une paroi (double vitrage, mur isolé, série et parallèle, puissance de chauffage) · ECUE : Thermodynamique
Formules : $R_{th} = \dfrac{e}{\lambda S}$ ; couches traversées par le même flux (série) : $R = \sum R_i$ ; surfaces côte à côte (parallèle) : $\dfrac1R = \sum\dfrac1{R_i}$ ; $\Phi = \dfrac{\Delta T}{R_{th}}$ ; le flux va du chaud vers le froid

Un appartement n'a qu'une paroi en contact avec l'extérieur : un mur percé de deux fenêtres identiques. Les autres murs, le sol et le plafond touchent des appartements voisins, tous à 20 °C. La température extérieure est de 5 °C. On néglige la convection. Données : surface d'une fenêtre $S_1 = 1\ \text{m}^2$ ; surface totale du mur extérieur, fenêtres comprises, $S_2 = 10\ \text{m}^2$ ; $\lambda_{verre} = 0{,}7$, $\lambda_{air} = 0{,}024$, $\lambda_{béton} = 1{,}5$, $\lambda_{laine} = 0{,}030\ \text{W·m}^{-1}\text{·K}^{-1}$.
1. L'appartement est à 18 °C. Décrire qualitativement les transferts thermiques à travers les différentes parois et le sens du flux d'énergie thermique.
2. Les fenêtres sont en double vitrage : chaque fenêtre ($1\ \text{m}^2$) a deux épaisseurs de verre de 14 mm séparées par 2,4 cm d'air. Exprimer la résistance thermique totale d'une seule fenêtre. Application numérique.
3. La surface du mur sans les fenêtres est de $8\ \text{m}^2$. Il est composé de 24 cm de béton et de 7,2 cm de laine de verre. Exprimer la résistance thermique totale de cette surface de mur. Application numérique.
4. En déduire la résistance thermique totale de la paroi extérieure (mur et fenêtres). En arrondissant les résistances au dixième près, donner le résultat sous forme de fraction irréductible.
5. Si l'appartement est à 20 °C, quelle puissance de chauffage faut-il apporter pour le maintenir à cette température ?

## Exercice 3. Le pendule simple (6 points + 2 points bonus)
Type : pendule simple (énergie mécanique, petites oscillations, isochronisme, base polaire) · ECUE : Mécanique
Formules : $E_c = \tfrac12ml^2\dot\theta^2$ ($v = l\dot\theta$) ; $E_p = mgl(1 - \cos\theta)$ ; sans frottement $\dfrac{dE_m}{dt} = 0 \Rightarrow \ddot\theta + \dfrac gl\sin\theta = 0$ ; petites oscillations $\ddot\theta + \dfrac gl\theta = 0$, $\theta = \theta_0\cos(\omega t)$, $\omega = \sqrt{g/l}$ ; polaire : $\vec a = (\ddot r - r\dot\theta^2)\vec u_r + (2\dot r\dot\theta + r\ddot\theta)\vec u_\theta$

On écarte de sa position d'équilibre un pendule M de masse $m$ suspendu à un fil inextensible de longueur $l$ (point d'attache O, axe Ox vertical vers le bas). On repère M par l'angle $\theta$ entre la verticale et le fil. Tous les frottements sont négligés.
1. Faire le bilan des forces qui s'exercent sur M et les représenter.
2. On établit l'équation différentielle par le théorème de l'énergie mécanique. a) Établir l'expression de l'énergie cinétique et de l'énergie potentielle de M en fonction de $l$, $m$, $g$ et $\theta$, en précisant le niveau de référence de l'altitude. b) Pourquoi peut-on affirmer que $\dfrac{dE_m}{dt} = 0$ ? c) Utiliser $\dfrac{dE_m}{dt} = 0$ pour établir l'équation différentielle du mouvement.
3. Petites oscillations : $\ddot\theta + \dfrac gl\theta = 0$. Lâché sans vitesse initiale, $\theta(t) = A\cos(\omega t)$. a) En réinjectant la solution, écrire $\omega$ en fonction de $g$ et $l$. b) L'angle initial est $\theta_0$ : en déduire $A$ et tracer l'allure de $\theta(t)$. c) L'angle initial est $2\theta_0$ : en déduire $A$, tracer $\theta(t)$. Que peut-on en déduire ?
4. Bonus (2 points) : équation différentielle par le principe fondamental de la dynamique, dans le repère polaire $(\vec u_r, \vec u_\theta)$ ($\vec u_r$ de O vers M). a) Donner la projection des forces sur M dans ce repère. b) Appliquer le PFD, avec $\vec a = (\ddot r - r\dot\theta^2)\vec u_r + (2\dot r\dot\theta + r\ddot\theta)\vec u_\theta$. c) En projetant sur $\vec u_\theta$, retrouver l'équation différentielle de la question 2.
