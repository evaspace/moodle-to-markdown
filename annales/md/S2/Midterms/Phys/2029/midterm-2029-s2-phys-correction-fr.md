# Examen de physique S2 : mécanique — mars 2025 (corrigé rédigé, FR)

- Source : `raw/S2/Midterms/Phys/2029/midterm-2029-s2-phys-subject-fr.pdf` (6 pages, sujet scanné ; pas de corrigé officiel dans le dépôt)
- Date réelle : mars 2025 (EPITA InfoS2, dossier promo 2029), durée 1 h 30. Sujet : `midterm-2029-s2-phys-subject-fr.md`.
- Calculatrices et documents non autorisés. Mécanique : travail, tir oblique, théorèmes de l'énergie. Les lignes `> ` sont un corrigé rédigé (pas officiel), applications numériques vérifiées par calcul.

## Exercice 1. Questions de cours (5 points, pas de points négatifs)
Type : QCM de mécanique (unité et signe du travail, cinématique, position en polaires) · ECUE : Mécanique · Niveau : physique-s2-energie/1
Formules : $W$ en joules, comme l'énergie ; $W > 0$ : travail moteur, $W < 0$ : résistant ; $\vec F \perp \overrightarrow{AB} \Rightarrow W = 0$ ; cinématique : description du mouvement sans ses causes ; polaires : $\overrightarrow{OM} = r\,\vec u_r = \begin{pmatrix} r \\ 0 \end{pmatrix}$ dans $(\vec u_r, \vec u_\theta)$

Pour certaines questions il faut cocher plusieurs bonnes réponses.
1. L'unité du travail $W$ est : a) le newton ; b) le joule ; c) la même que celle de la force ; d) la même que celle de l'énergie.
> b) et d).
2. Un travail $W > 0$ est dit : a) résistif ; b) récursif ; c) moteur ; d) accélérateur.
> c).
3. Si une force est perpendiculaire au déplacement, le travail est : a) nul ; b) maximum ; c) négatif ; d) dépend de la norme de la force.
> a) : $W = F\,AB\cos 90° = 0$.
4. La cinématique est la branche de la physique qui s'intéresse : a) au mouvement indépendamment des causes le produisant ; b) à la cause des mouvements ; c) au cinéma ; d) aucune des réponses.
> a).
5. En coordonnées polaires, le vecteur position s'écrit : a) $\overrightarrow{OM} = r\,\vec u_r$ ; b) $\overrightarrow{OM} = \begin{pmatrix} r \\ 0 \end{pmatrix}$ ; c) $\overrightarrow{OM} = \begin{pmatrix} 0 \\ r \end{pmatrix}$ ; d) $\overrightarrow{OM} = \begin{pmatrix} r \\ \theta \end{pmatrix}$.
> a) et b).

## Exercice 2. Lancer de javelot (8 points)
Type : tir oblique depuis une hauteur (PFD, équations horaires, trajectoire, durée de vol, portée) · ECUE : Mécanique · Niveau : physique-s1-meca/5
Formules : $\vec a = \begin{pmatrix} 0 \\ -g \end{pmatrix}$ ; $\vec v = \begin{pmatrix} v_0\cos\alpha \\ v_0\sin\alpha - gt \end{pmatrix}$ ; $\overrightarrow{OM} = \begin{pmatrix} v_0\cos\alpha\,t \\ -\tfrac12gt^2 + v_0\sin\alpha\,t + h \end{pmatrix}$ ; $y(x) = -\dfrac{gx^2}{2v_0^2\cos^2\alpha} + x\tan\alpha + h$ ; impact : $y = 0$, $t = \dfrac{v_0\sin\alpha + \sqrt{v_0^2\sin^2\alpha + 2gh}}{g}$

On lance un javelot de masse $m = 0{,}8$ kg depuis un point A à la hauteur $h = 1{,}95$ m au-dessus du sol. Sa vitesse initiale a pour norme $v_0 = 10$ m/s et fait un angle $\alpha = 30°$ avec l'horizontale. $g = 10\ \text{m·s}^{-2}$ ; frottements de l'air négligés. L'origine O est au sol, à la verticale de A.
1. Donner le cadre d'étude (référentiel, système, système de coordonnées).
> Référentiel terrestre, système : le javelot (assimilé à un point), coordonnées cartésiennes $(O, \vec u_x, \vec u_y)$.
2. Par le PFD, donner le vecteur accélération.
> $m\vec a = m\vec g$ donc $\vec a = -g\,\vec u_y$.
3. Donner le vecteur vitesse (constante d'intégration par les conditions initiales).
> $\vec v(0) = \vec v_0$ : $\vec v = v_0\cos\alpha\,\vec u_x + (v_0\sin\alpha - gt)\,\vec u_y$.
4. Donner le vecteur position (constante d'intégration par les conditions initiales).
> $\overrightarrow{OM}(0) = h\,\vec u_y$ : $x = v_0\cos\alpha\,t$, $y = -\tfrac12gt^2 + v_0\sin\alpha\,t + h$.
5. Établir l'équation de la trajectoire $y(x)$. Quel est le type de trajectoire ?
> $t = \dfrac{x}{v_0\cos\alpha}$ : $y = -\dfrac{g}{2v_0^2\cos^2\alpha}x^2 + x\tan\alpha + h$, une parabole.
6. Quelle est la durée écoulée avant que le javelot touche le sol ? Application numérique.
> $y = 0$ : $-5t^2 + 5t + 1{,}95 = 0$, soit $t^2 - t - 0{,}39 = 0$, $\Delta = 1 + 1{,}56 = 2{,}56 = 1{,}6^2$ ; la racine positive est $t = \dfrac{1 + 1{,}6}{2} = 1{,}3$ s.
7. À quelle distance de l'origine se situe le point d'impact ? Application numérique.
> $x = v_0\cos\alpha\,t = 10 \times \dfrac{\sqrt3}{2} \times 1{,}3 \approx 11{,}3$ m.

## Exercice 3. Étude énergétique (7 points)
Type : plan incliné sans frottement puis piste horizontale avec frottement (travail, énergie mécanique, théorème de l'énergie cinétique) · ECUE : Mécanique · Niveau : physique-s2-energie/7
Formules : $W(\vec P) = mg\,AB\sin\alpha$ en descente ; $W(\vec R_N) = 0$ ; sans frottement $E_m$ conservée : $v_B = \sqrt{2g\,AB\sin\alpha}$ ; $W(\vec f) = -f\,BC$ ; $\Delta E_c = \sum W$ : $BC = \dfrac{mv_B^2}{2f}$

Une boîte de masse $m = 0{,}1$ kg est lâchée sans vitesse initiale du point A d'un plan incliné d'angle $\alpha$ avec l'horizontale. Les frottements sont négligeables sur AB ; sur la partie horizontale BC, elle subit une force de frottement $\vec f$. Données : $\alpha = 30°$, $g = 10\ \text{m·s}^{-2}$, $AB = 10$ m, $\sin 30° = \tfrac12$, $\cos 30° = \tfrac{\sqrt3}{2}$.
1. Représenter les forces extérieures sur la boîte au cours du trajet AB.
> Le poids $\vec P$ (vertical) et la réaction normale $\vec R_N$ (perpendiculaire au plan).
2. Donner le travail des forces sur AB en fonction de $m$, $AB$, $\alpha$ et $g$.
> $W_{AB}(\vec P) = mg\,AB\sin\alpha$ (la boîte descend de $AB\sin\alpha$) ; $W_{AB}(\vec R_N) = 0$.
3. Sur quelle partie du trajet peut-on utiliser le théorème de l'énergie mécanique ? Justifier.
> Sur AB, où seules agissent des forces conservatives ou qui ne travaillent pas : $E_m$ y est conservée. Sur BC, le frottement fait varier $E_m$.
4. Par le théorème de l'énergie mécanique entre A et B, déduire la vitesse en B. Application numérique.
> $mg\,AB\sin\alpha = \tfrac12mv_B^2$, donc $v_B = \sqrt{2g\,AB\sin\alpha} = \sqrt{2 \times 10 \times 10 \times 0{,}5} = 10$ m/s.
5. Représenter les forces sur la boîte sur le trajet BC.
> Le poids $\vec P$, la réaction normale $\vec R_N$ et le frottement $\vec f$ opposé au mouvement.
6. Donner le travail des forces sur BC en fonction de $f$ et de $BC$.
> $W(\vec P) = W(\vec R_N) = 0$ (perpendiculaires au déplacement), $W(\vec f) = -f\,BC$.
7. Par le théorème de l'énergie cinétique entre B et C, calculer $BC$ sachant que la boîte s'arrête en C. Le frottement est constant, $f = 0{,}20$ N.
> $0 - \tfrac12mv_B^2 = -f\,BC$, donc $BC = \dfrac{mv_B^2}{2f} = \dfrac{0{,}1 \times 100}{0{,}4} = 25$ m.
