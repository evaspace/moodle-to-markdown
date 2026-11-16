# Contrôle de physique S2 : lois de Newton — février 2023 (corrigé rédigé, FR)

- Source : `raw/S2/Midterms/Phys/2027/midterm-2027-s2-phys-subject-fr.pdf` (6 pages : copie d'étudiant scannée et notée, 12/20 ; pas de corrigé officiel dans le dépôt)
- Date réelle : février 2023 (EPITA InfoS2, dossier promo 2027), durée 1 h. Sujet : `midterm-2027-s2-phys-subject-fr.md`.
- Calculatrices et documents non autorisés. Mécanique : lois de Newton (fils, poulies, plan incliné), base polaire. Les lignes `> ` sont un corrigé rédigé (pas officiel) ; les réponses de la copie notée ont servi de contrôle.

## Exercice 1. Questions de cours (6 points, pas de points négatifs)
Type : QCM de dynamique (unité du newton, tension, poulie, machine d'Atwood) · ECUE : Mécanique · Niveau : physique-s2-energie/9
Formules : $1\ \text{N} = 1\ \text{kg·m·s}^{-2}$ ; équilibre : $T = mg$ ; $T - mg = ma$ (montée) ; fil et poulie idéaux : même tension aux deux bouts ; Atwood : $a = g\dfrac{m_2 - m_1}{m_1 + m_2}$

Choisissez la ou les bonnes réponses.
1. L'unité newton est équivalente à : a) $\text{kg·m·s}^{-2}$ ; b) $\text{kg·m·s}^{-1}$ ; c) $\text{kg·m}^2\text{·s}^{-1}$ ; d) $\text{kg·s}^{-1}$.
> a).

Q2 et Q3 : une corde inextensible de masse négligeable tient une masse $m = 50$ kg ; $g = 10\ \text{m·s}^{-2}$. Une machine exerce une tension pour faire monter la masse sans frottements.

2. Quelle valeur doit avoir la tension pour que la masse reste à l'équilibre ? a) 500 N ; b) 50 N ; c) 60 N ; d) aucune des valeurs précédentes.
> a) : $T = mg = 500$ N.
3. Si la norme de la tension vaut 900 N, quelle est celle de l'accélération ? a) $940\ \text{m·s}^{-2}$ ; b) $950\ \text{m·s}^{-2}$ ; c) $400\ \text{m·s}^{-2}$ ; d) aucune des valeurs précédentes.
> d) : $T - mg = ma$ donne $a = \dfrac{900 - 500}{50} = 8\ \text{m·s}^{-2}$.

Q4 et Q5 : une corde inextensible de masse négligeable relie deux masses $m_1$ (suspendue) et $m_2$ (sur une pente d'angle $\alpha$) en passant par une poulie de masse négligeable. Mouvement sans frottements : $m_1$ descend, $m_2$ monte la pente. Les tensions sur $m_1$ et $m_2$ sont $\vec T$ et $\vec T'$.

4. Les relations correctes entre les tensions sont : a) $\|\vec T\| = \|\vec P_1\|$ et $\|\vec T'\| = \|\vec P_2\|$ ; b) $\|\vec T\| = \|\vec P_1\|$ et $\|\vec T'\| = \|\vec P_2\|\,|\sin\alpha|$ ; c) $\|\vec T\| = \|\vec P_2\|\,|\sin\alpha|$ et $\|\vec T'\| = \|\vec P_1\|$ ; d) $\|\vec T\| = \|\vec T'\|$.
> d) : fil et poulie idéaux. Les autres égalités ne valent qu'à l'équilibre.
5. La deuxième loi de Newton appliquée à $m_1$ donne : a) $\|\vec T\| = m_1(g + a)$ ; b) $\|\vec T\| = m_1(g - a)$ ; c) $\|\vec T\| = m_1(a - g)$ ; d) $\|\vec T\| = m_1a$.
> b) : $m_1$ descend, $m_1g - T = m_1a$.
6. Deux masses $m_1$ et $m_2$ sont suspendues de part et d'autre d'une poulie (fil et poulie idéaux) ; $m_2$ descend. La norme de l'accélération vaut : a) $g\dfrac{m_1}{m_2}$ ; b) $g\dfrac{m_2 - m_1}{m_2 + m_1}$ ; c) $g\dfrac{m_1 - m_2}{m_2 + m_1}$ ; d) $g\dfrac{m_1 + m_2}{m_2 - m_1}$.
> b) : $m_2g - T = m_2a$ et $T - m_1g = m_1a$.

## Exercice 2. Lois de Newton : trois masses (8 points)
Type : trois masses reliées par des fils (suspendue, table, plan incliné) : accélération et équilibre · ECUE : Mécanique · Niveau : physique-s2-energie/9
Formules : $\sum\vec F_{ext} = m\vec a$ pour chaque masse ; $T_1 = T_2$, $T_2' = T_3$ (fils et poulies idéaux) ; $a = g\dfrac{m_1 - m_3\sin\alpha}{m_1 + m_2 + m_3}$ ; équilibre : $m_1 = m_3\sin\alpha$

Trois masses sont reliées par des fils inextensibles de masses négligeables passant sur des poulies de masses négligeables : $m_1$ est suspendue à gauche, $m_2$ glisse sur une table horizontale, $m_3$ est sur un plan incliné d'angle $\alpha$ à droite. Pas de frottements. Sens du mouvement : $m_1$ descend, $m_2$ va vers la gauche, $m_3$ monte la pente. $m_1 = 5$ kg, $m_2 = 10$ kg, $m_3 = 5$ kg, $g = 10\ \text{m·s}^{-2}$, $\alpha = 30°$.
1. Schématiser les forces sur les trois masses (notation indicée par le numéro de la masse).
> $m_1$ : $\vec P_1$, $\vec T_1$. $m_2$ : $\vec P_2$, $\vec R_2$, $\vec T_2$ (vers $m_1$), $\vec T_2'$ (vers $m_3$). $m_3$ : $\vec P_3$, $\vec R_3$, $\vec T_3$ (vers le haut de la pente).
2. Identifier les tensions de même norme. Justifier.
> $\|\vec T_1\| = \|\vec T_2\|$ et $\|\vec T_2'\| = \|\vec T_3\|$ : fils et poulies de masses négligeables.
3. Appliquer la deuxième loi de Newton à chaque masse (forme vectorielle).
> $\vec T_1 + \vec P_1 = m_1\vec a_1$ ; $\vec T_2 + \vec T_2' + \vec R_2 + \vec P_2 = m_2\vec a_2$ ; $\vec P_3 + \vec T_3 + \vec R_3 = m_3\vec a_3$.
4. Projeter sur les axes du mouvement : trois égalités entre tensions, masses, $\alpha$, $g$ et $a$, et deux égalités donnant les réactions du support.
> $m_1g - T_1 = m_1a$ ; $T_2 - T_2' = m_2a$ ; $T_3 - m_3g\sin\alpha = m_3a$. Réactions : $R_2 = m_2g$, $R_3 = m_3g\cos\alpha$.
5. Exprimer l'accélération en fonction des masses, de $g$ et de $\alpha$. Application numérique.
> En sommant : $m_1g - m_3g\sin\alpha = (m_1 + m_2 + m_3)a$, donc $a = g\dfrac{m_1 - m_3\sin\alpha}{m_1 + m_2 + m_3} = \dfrac{50 - 25}{20} = 1{,}25\ \text{m·s}^{-2}$.
6. Quelle devrait être la valeur de $m_3$ pour que le système soit à l'équilibre statique ?
> $a = 0 \iff m_3\sin\alpha = m_1$, soit $m_3 = \dfrac{m_1}{\sin\alpha} = 10$ kg.

## Exercice 3. Lois de Newton : franchir une bosse (6 points)
Type : véhicule sur une bosse circulaire (base polaire, réaction normale, condition de contact) · ECUE : Mécanique · Niveau : physique-s1-meca/6
Formules : base polaire $(\vec u_r, \vec u_\theta)$ centrée en O ; $\vec a = \begin{pmatrix} -v^2/R \\ R\ddot\theta \end{pmatrix}$ ; $\vec P = \begin{pmatrix} -mg\cos\theta \\ mg\sin\theta \end{pmatrix}$, $\vec R_N = \begin{pmatrix} R_N \\ 0 \end{pmatrix}$ ; contact $\iff R_N > 0 \iff v^2 < gR\cos\theta$

Une voiture de masse $m$ franchit une bosse en arc de cercle de centre O et de rayon $R$ ; au temps $t$, elle est en M, repéré par l'angle $\theta$ entre la verticale et OM. On cherche les conditions pour qu'elle reste toujours en contact avec le sol.
1. Schématiser la base du système de coordonnées polaires.
> Origine O ; $\vec u_r$ le long de OM, vers l'extérieur ; $\vec u_\theta$ perpendiculaire, dans le sens du mouvement (θ croissant).
2. Schématiser les forces sur la voiture en M.
> Le poids $\vec P$ (vertical, vers le bas) et la réaction normale $\vec R_N$ du sol (selon $\vec u_r$, vers l'extérieur).
3. Appliquer la deuxième loi de Newton (forme vectorielle) et la projeter dans la base polaire, sachant que $\vec a = \begin{pmatrix} -v^2/R \\ R\ddot\theta \end{pmatrix}$.
> $\vec P + \vec R_N = m\vec a$. Sur $\vec u_r$ : $R_N - mg\cos\theta = -m\dfrac{v^2}{R}$ ; sur $\vec u_\theta$ : $mg\sin\theta = mR\ddot\theta$.
4. À quelle condition la voiture franchit-elle la bosse sans décoller ? Écrire une inégalité sur la norme d'une force, puis une condition sur l'angle $\theta$ en fonction de $v$, $R$ et $g$.
> Il faut $R_N > 0$. Or $R_N = mg\cos\theta - m\dfrac{v^2}{R}$, donc $\cos\theta > \dfrac{v^2}{gR}$.
