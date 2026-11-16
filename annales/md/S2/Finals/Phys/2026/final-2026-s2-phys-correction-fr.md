# Partiel de physique S2 — mai 2022 (corrigé, FR)

- Source : `raw/S2/Finals/Phys/2026/final-2026-s2-phys-correction-fr.pdf` (6 pages, corrigé manuscrit photographié avec barème)
- Date réelle : mai 2022 (EPITA S2, dossier promo 2026). Sujet : `final-2026-s2-phys-subject-fr.md`.
- Documents et calculatrices interdits. Mécanique : lois de Newton (poulie), travail, énergies cinétique et mécanique. Les lignes `> ` sont les solutions (QCM, exercices 2 et 3 relus sur le corrigé ; exercice 4 rédigé).

## Exercice 1. QCM (3 points, pas de point négatif)
Type : QCM de mécanique (travail, lois de Newton, théorème de l'énergie cinétique, énergie mécanique) · ECUE : Mécanique · Niveau : physique-s2-energie/4
Formules : $W = \vec F \cdot \overrightarrow{AB} = F\,AB\cos\alpha$ ; première loi de Newton (inertie) ; $\|\vec F\| = ma$, $\|\vec F\| = \sqrt{F_x^2 + F_y^2 + F_z^2}$ ; $\Delta E_c = \sum W(\vec F_{ext})$ ; $E_m = E_c + E_p$, conservée seulement sans force non conservative

Encercler la bonne réponse. Une question peut avoir plusieurs bonnes réponses ($0{,}5$ point par bonne réponse).
1. Une force $\vec F$ s'exerce selon un angle $\alpha$ sur une boîte de masse $m$ traînée sur le sol à vitesse constante. Si la boîte parcourt une distance $AB$, le travail $W$ effectué par $\vec F$ est : a) $W = F \cdot AB$ ; b) $W = F \cdot AB \cdot \sin\alpha$ ; c) $W = \vec F \cdot \overrightarrow{AB}$ ; d) aucune bonne réponse.
> c) ($= F\,AB\cos\alpha$).
2. Lorsqu'un bus démarre brusquement, les passagers sont repoussés en arrière. C'est un exemple de : a) la première loi de Newton ; b) la deuxième loi de Newton ; c) la troisième loi de Newton ; d) la loi de l'énergie cinétique.
> a) : principe d'inertie.
3. La force appliquée à un corps est $\vec F = 6\vec u_x - 8\vec u_y + 10\vec u_z$. Le corps subit une accélération de norme $1\ \text{m/s}^2$. Sa masse est : a) $10\sqrt2$ kg ; b) $10$ kg ; c) $2\sqrt{10}$ kg ; d) $8$ kg.
> a) : $\|\vec F\| = \sqrt{36 + 64 + 100} = 10\sqrt2$ N et $m = \dfrac{\|\vec F\|}{a}$.
4. D'après le théorème de l'énergie cinétique, la somme des travaux des forces extérieures agissant sur un système est égale à : a) l'énergie cinétique du système ; b) l'énergie potentielle du système ; c) la variation de l'énergie cinétique du système ; d) la variation de l'énergie potentielle du système.
> c).
5. Que ne peut-on **pas** dire de l'énergie mécanique d'un système ? a) Elle est égale à la somme des énergies cinétique et potentielle du système. b) Elle est nulle pour une masse $m$ animée d'un mouvement rectiligne. c) Elle est toujours conservée. d) Elle est égale à l'énergie potentielle pour un système au repos.
> b) et c).

## Exercice 2. Lois de Newton (8 points)
Type : deuxième loi de Newton, masses reliées par une poulie (tensions, accélération) · ECUE : Mécanique · Niveau : physique-s2-energie/9
Formules : $\sum\vec F_{ext} = m\vec a$ pour chaque masse ; fil et poulie de masses négligeables : même tension de part et d'autre ; fil inextensible : même norme d'accélération ; $P = mg$

Deux masses égales $M = 2{,}0$ kg sont attachées à une corde enroulée sur une poulie bloquée. La masse de gauche repose sur le sol, celle de droite est suspendue à $1{,}0$ m au-dessus du sol. Une autre masse $m = 0{,}5$ kg est attachée au-dessus de la masse $M$ de droite. On néglige la masse de la corde, celle de la poulie et les frottements. La poulie est finalement libérée. $g = 10\ \text{m/s}^2$.
1. Représenter les forces extérieures qui agissent sur chacune des masses.
> $M$ de gauche : poids $\vec P_M$ vers le bas, tension $\vec T_1$ vers le haut. $m$ : poids $\vec P_m$, tension $\vec T_2$ du fil de la poulie vers le haut, tension $\vec T_3$ du fil qui la relie à $M$ vers le bas. $M$ de droite : poids $\vec P_M$, tension $\vec T_4$ vers le haut. Le côté gauche monte avec $\vec a$, le côté droit descend.
2. Quelles relations existent entre les différentes tensions des fils ? Justifier.
> $T_1 = T_2$ et $T_3 = T_4$ : la poulie et les fils ont une masse négligeable, la poulie transmet la tension sans la modifier.
3. Utiliser la deuxième loi de Newton pour chacune des trois masses et en déduire $a = \dfrac{mg}{2M + m}$. Application numérique.
> $M$ gauche : $T_1 - P_M = Ma$ (1). $m$ : $T_2 - T_3 - P_m = -ma$ (2). $M$ droite : $T_4 - P_M = -Ma$ (3). (1) + (2) + (3) avec $T_1 = T_2$, $T_3 = T_4$ : $2T_1 - 2P_M - P_m = -ma$ et $T_1 = Ma + P_M$, donc $(2M + m)a = P_m$ : $a = \dfrac{mg}{2M + m} = \dfrac{5}{4{,}5} \approx 1{,}1\ \text{m/s}^2$.

## Exercice 3. Énergie mécanique (4,5 points)
Type : conservation de l'énergie mécanique sur une piste (vitesse en un point, condition d'arrêt) · ECUE : Mécanique · Niveau : physique-s2-energie/6
Formules : $E_c = \tfrac12mv^2$ ; $E_p = mgz$ ; $E_m = E_c + E_p$ ; sans frottement : $\Delta E_m = 0$ ; $v_B = \sqrt{2g(h - d)}$

Un objet de masse $m$ assimilé à un point matériel est lâché sans vitesse initiale du haut d'une cuvette (point A) à une hauteur $h$ du sol. Il glisse jusqu'au fond de la cuvette (point A', au niveau du sol) puis remonte jusqu'à un deuxième sommet (point B) à une hauteur $d$. Frottements négligés, $g = 10\ \text{m·s}^{-2}$.
1. Donner les expressions des énergies cinétique, potentielle et mécanique aux points A, A' et B.
> A : $E_c = 0$, $E_p = mgh$, $E_m = mgh$. A' : $E_c = \tfrac12mv_{A'}^2$, $E_p = 0$, $E_m = \tfrac12mv_{A'}^2$. B : $E_c = \tfrac12mv_B^2$, $E_p = mgd$, $E_m = \tfrac12mv_B^2 + mgd$.
2. En utilisant le théorème de l'énergie mécanique, déterminer la vitesse $v_B$ au point B.
> $\Delta E_m = \sum W(\text{forces non conservatives}) = 0$ (pas de frottement). $\tfrac12mv_B^2 + mgd = mgh$, donc $v_B = \sqrt{2g(h - d)}$.
3. Quelle relation doit exister entre $d$ et $h$ pour que la bille s'arrête net au point B ?
> $v_B = 0 \iff d = h$.

## Exercice 4. Énergie cinétique et travail (4,5 points)
Type : théorème de l'énergie cinétique avec frottement (palet qui s'arrête) · ECUE : Mécanique · Niveau : physique-s2-energie/7
Formules : $W(\vec P) = 0$ et $W(\vec R_N) = 0$ sur un déplacement horizontal ; $W(\vec f) = -f\,x$ ; $\Delta E_c = \sum W$ ; $f = \dfrac{mv_A^2}{2x}$

Un palet de hockey de masse $m$ lancé à la vitesse $v_A$ parcourt une distance horizontale $x$ avant de s'immobiliser. On étudie son mouvement dans le référentiel terrestre.
1. Donner le bilan des forces extérieures qui s'exercent sur le palet.
> Le poids $\vec P$, la réaction normale de la glace $\vec R_N$ et la force de frottement $\vec f$ opposée au mouvement.
2. Quelle est la force responsable de son ralentissement ?
> La force de frottement $\vec f$.
3. Exprimer le travail de chacune de ces forces.
> $\vec P$ et $\vec R_N$ sont perpendiculaires au déplacement : $W = 0$. $W(\vec f) = -f\,x$.
4. Écrire le théorème de l'énergie cinétique et en déduire la norme de la force évoquée à la question 2.
> $0 - \tfrac12mv_A^2 = -f\,x$, donc $f = \dfrac{mv_A^2}{2x}$.
