# Contrôle 2 de physique S2 — mars 2020 (sujet, FR)

- Source : `raw/S2/Midterms/Phys/2024/midterm-2024-s2-phys-subject-fr.pdf` (7 pages)
- Date réelle : mars 2020 (EPITA S2, dossier promo 2024). Corrigé : `midterm-2024-s2-phys-correction-fr.md`.
- Calculatrices et documents non autorisés. Sujet noté sur 21. Mécanique : énergie, oscillateurs (ressort, pendule, amortissement) ; une question de conduction thermique.

## QCM (4 points, sans points négatifs)
Type : QCM d'oscillateurs et de conduction (équation amortie, régimes, pendule, résistance thermique) · ECUE : Mécanique
Formules : $m\ddot x + \alpha\dot x + kx = 0$ ; pseudopériodique $\iff \alpha < 2m\omega_0$, $\omega_0 = \sqrt{k/m}$, $\omega < \omega_0$ ; $x(t) = x_0e^{-\frac{\alpha}{2m}t}\cos(\omega t)$ ; pendule : $\ddot\theta + \dfrac gL\theta = 0$, $T = 2\pi\sqrt{L/g}$ ; $R_{th} = \dfrac{e}{\lambda_{th}S}$, $\lambda_{th}$ en $\text{W·K}^{-1}\text{·m}^{-1}$

$0{,}5$ point par question.
1. Une masse $m$ accrochée à un ressort de raideur $k$ subit une force de frottement $\vec f = -\alpha\vec v$ ($\alpha > 0$). La position d'équilibre est en O. L'équation différentielle du mouvement s'écrit : a) $\ddot x + \alpha\dot x + \dfrac kmx = 0$ ; b) $\ddot x + \dfrac kmx = 0$ ; c) $\ddot x + \dfrac\alpha m\dot x + \dfrac kmx = 0$ ; d) $\ddot x + \dfrac km\dot x + \alpha x = 0$.
2. Le régime pseudopériodique correspond à la condition ($\omega_0$ pulsation propre sans frottement) : a) $\alpha < 2m\omega_0$ ; b) $\alpha = 0$ ; c) $\alpha > 2m\omega_0$.
3. Dans le régime pseudopériodique, la pulsation $\omega$ de l'oscillateur amorti vérifie : a) $\omega = \omega_0$ ; b) $\omega > \omega_0$ ; c) $\omega < \omega_0$.
4. L'équation horaire du régime pseudopériodique s'écrit : a) $x(t) = x_0\cos(\omega t)$ ; b) $x(t) = x_0e^{\frac{\alpha}{2m}t}\cos(\omega t)$ ; c) $x(t) = x_0e^{-\frac{\alpha}{2m}t}\cos(\omega t)$.
5. Pour les petites oscillations sans frottement, l'équation du pendule simple (longueur $L$, angle $\theta$) est : a) $\ddot\theta + \dfrac Lg\theta = 0$ ; b) $\ddot\theta + \dfrac gL\theta = 0$ ; c) $\ddot\theta + \dfrac mL\theta = 0$ ; d) $\ddot\theta + \dfrac{m}{gL}\theta = 0$.
6. Avec le même pendule mais un fil de longueur $2L$, la période $T'$ vaut : a) $2T$ ; b) $4T$ ; c) $T/2$ ; d) $\sqrt2\,T$.
7. En modèle purement conductif, la résistance thermique d'un conducteur de conductivité $\lambda_{th}$, de section $S$ et d'épaisseur $e$ s'écrit : a) $R_{th} = \dfrac{eS}{\lambda_{th}}$ ; b) $R_{th} = \dfrac{e}{\lambda_{th}S}$ ; c) $R_{th} = \dfrac{\lambda_{th}}{eS}$.
8. La conductivité thermique s'exprime en : a) $\text{K·W}^{-1}$ ; b) $\text{W·m}^{-2}$ ; c) $\text{K·W}^{-1}\text{·m}^{-2}$ ; d) $\text{W·K}^{-1}\text{·m}^{-1}$.

## Exercice 1. Palet sur une piste (6 points)
Type : énergie sur une piste avec propulsion (théorème de l'énergie cinétique, énergie mécanique, réaction en Frenet) · ECUE : Mécanique · Niveau : physique-s2-energie/6
Formules : $\Delta E_c = \sum W$ ; $W(\vec F) = Fl$ ; $E_m = \tfrac12mv^2 + mgz$ conservée sans frottement ; Frenet : $m\dfrac{v^2}{R} = \sum F_N$ ; $z_C = R(1 - \cos\theta)$

Un palet de masse $m$ est propulsé sur une piste dans un plan vertical : une partie horizontale (AB), raccordée tangentiellement à un arc de cercle (BC) de centre O et de rayon $R = OB = OC$, puis une partie rectiligne inclinée (CD). L'épreuve est réussie si le centre d'inertie G parvient en D, à une hauteur $h$ au-dessus de AB. Frottements négligés. Une force de propulsion $\vec F$ constante est exercée le long de AA' (longueur $l$) puis cesse en A'. Données : $l = 0{,}5$ m, $h = 1{,}5$ m, $m = 5$ kg, $g = 10\ \text{m·s}^{-2}$. En C, le rayon OC fait l'angle $\theta$ avec la verticale.
1. Représenter les forces extérieures appliquées sur le palet entre A et A'.
2. Utiliser le théorème de l'énergie cinétique entre A et A' pour en déduire la vitesse en A' (vitesse nulle en A), en fonction de $l$, $F$ et $m$.
3. Quelle est la relation entre la vitesse en B et celle en A' ? Justifier.
4. a) Déterminer, par le théorème de l'énergie mécanique, la vitesse en B (en fonction de $g$, $h$) pour que le palet atteigne D avec une vitesse nulle. b) En déduire la norme de $\vec F$. Application numérique.
5. a) Par le théorème de l'énergie mécanique entre B et C, exprimer la vitesse en C en fonction de $g$, $h$, $R$ et $\theta$. b) En déduire la norme de la réaction $\vec R_N$ en C en fonction de $m$, $g$, $h$, $R$ et $\theta$ (deuxième loi de Newton dans la base de Frenet en C).

## Exercice 2. Oscillateurs (11 points)
Type : oscillateur ressort amorti puis ressort sur plan incliné (équation différentielle, énergie, équilibre) · ECUE : Mécanique
Formules : $m\ddot x = -kx - \alpha\dot x$ ; pseudopériodique si $\alpha < 2m\omega_0$ ; $E_m = \tfrac12m\dot x^2 + \tfrac12kx^2$, $\dfrac{dE_m}{dt} = \dot x(m\ddot x + kx) = -\alpha\dot x^2 = \vec f \cdot \vec v$ ; plan incliné : $k(x_e - L_0) = mg\sin\alpha$ ; $X = x - x_e$, $\ddot X + \dfrac kmX = 0$

Les parties A et B sont indépendantes.

**Partie A (6 points).** Un oscillateur horizontal est formé d'un solide de masse $m$ fixé à un ressort de masse négligeable et de raideur $k$ ; la position d'équilibre est O. On écarte la masse de $x_0$ vers la droite et on la lâche à $t = 0$ sans vitesse initiale ; $x(t) = OG$. Les frottements valent $\vec f = -\alpha\vec v$ ($\alpha > 0$).
1. Représenter les forces extérieures exercées sur la masse pendant une phase où $\dot x < 0$.
2. Utiliser la deuxième loi de Newton pour écrire l'équation différentielle du mouvement.
3. On se place dans le cas $\alpha < 2m\omega_0$. a) Qualifier le mouvement ; justifier. b) Représenter schématiquement $x(t)$. c) Exprimer l'énergie mécanique à un instant quelconque et sa dérivée $\dfrac{dE_m}{dt}$ en fonction de $\dot x$ et $\ddot x$. d) Retrouver, avec l'équation différentielle, $\dfrac{dE_m}{dt} = \vec f \cdot \vec v$.

**Partie B (5 points).** Un point matériel M de masse $m$ est relié à un ressort de raideur $k$ et de longueur à vide $L_0$, attaché à un point fixe O. L'ensemble est sur un plan incliné d'un angle $\alpha$ par rapport à l'horizontale (l'angle $\alpha$ est aussi celui entre le poids et la normale au plan). Frottements négligés ; l'axe $x$ descend le long du plan.
1. Représenter les forces extérieures appliquées sur la masse.
2. Montrer que la longueur du ressort à l'équilibre est $x_e = \dfrac{mg\sin\alpha}{k} + L_0$.
3. On écarte la masse de $x_e$ vers $x > 0$ et on la lâche à $t = 0$ sans vitesse initiale. Avec $X(t) = x(t) - x_e$, montrer que $\ddot X + \dfrac kmX = 0$.
