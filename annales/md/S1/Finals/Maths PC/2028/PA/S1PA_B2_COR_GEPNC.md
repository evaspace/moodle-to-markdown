# Correction examen B2-GEPNC (S1 PA) — janvier 2024

- Source : `raw/S1/Finals/Maths PC/2028/PA/S1PA_B2_COR_GEPNC.pdf` (3 pages, corrigé avec énoncés)
- Date réelle : janvier 2024 (parcours PA, dossier promo 2028). Pas de sujet séparé.
- Les exercices 1 et 2 s'appuient sur un plan quadrillé et des droites tracées dans le sujet (figures non reproduites).

## Exercice 1 : géométrie du plan
Type : vecteurs du plan, repère, combinaison linéaire · ECUE : HP (géométrie, parcours PA)
Formules : $(O\,;\,\vec u, \vec v)$ repère $\iff \vec u, \vec v$ non colinéaires $\iff \det(\vec u, \vec v) = xy' - x'y \neq 0$ ; $a\vec u + b\vec v = (ax + bx', ay + by')$

Soient $\vec u_1$, $\vec u_2$, $\vec u_3$ et $\vec v$ quatre vecteurs du plan dont les coordonnées dans le repère $(O ; \vec\imath, \vec\jmath)$ sont : $\vec u_1 = (1, -2)$, $\vec u_2 = (-2, 1)$, $\vec u_3 = (-3, 6)$ et $\vec v = (3, -3)$.
1. Dessiner les vecteurs $\vec u_1$, $\vec u_2$, $\vec u_3$ et $\vec v$ sur le plan quadrillé.
2. (a) $(O ; \vec u_1, \vec u_2)$ est-il un repère du plan ? Justifier.
   Oui car les deux vecteurs $\vec u_1$ et $\vec u_2$ ne sont pas colinéaires.
   (b) Si oui, déterminer graphiquement deux réels $a$ et $b$ tels que $\vec v = a\vec u_1 + b\vec u_2$. (Les marques de construction doivent apparaître clairement sur le plan.)
   On trouve 1 et $-1$ : $\vec v = \vec u_1 - \vec u_2$.
   (c) Mêmes questions avec $\vec u_1$ et $\vec u_3$.
   $\vec u_3 = -3\vec u_1$. Ces deux vecteurs sont colinéaires : ils ne peuvent pas former un repère du plan.
3. Construire le vecteur $\vec w = -\vec u_1 + 2\vec u_2$. Quelles sont ses coordonnées dans le repère $(O ; \vec\imath, \vec\jmath)$ ?
   Graphiquement, on trouve $\vec w = (-5, 4)$.

## Exercice 2 : droites dans le plan
Type : droites du plan (point, vecteur directeur, équation, parallélisme) · ECUE : HP (géométrie, parcours PA)
Formules : $D = \{M, \exists \alpha, \overrightarrow{AM} = \alpha\vec u\}$ ; $ax + by + c = 0$ a pour vecteur directeur $(-b, a)$ ; droite par l'origine : $y = mx$ ; droites parallèles $\iff$ vecteurs directeurs colinéaires

Trois droites $D_1$, $D_2$, $D_3$ sont tracées sur la figure du sujet.
1. Déterminer un point et un vecteur directeur de la droite $D_1$ et compléter sa définition en utilisant ces éléments.
   $A_1(0, 1)$, $\vec u_1 = (2, -1)$ et $D_1 = \{M \in \mathbb{R}^2, \exists \alpha \in \mathbb{R}, \overrightarrow{A_1M} = \alpha\vec u_1\}$.
2. Déterminer deux points de la droite $D_2$ et compléter sa définition en utilisant ces points.
   $A_2(2, 0)$, $B_2(2, 2)$, $D_2 = \{M \in \mathbb{R}^2, \exists \alpha \in \mathbb{R}, \overrightarrow{A_2M} = \alpha\overrightarrow{A_2B_2}\}$.
3. Déterminer une équation de la droite $D_3$ ainsi qu'un vecteur directeur.
   La droite passe par l'origine : $y = ax$. Elle passe par $A(1, 3)$, d'où $a = 3$ : $y = 3x$, vecteur directeur $\vec u = (1, 3)$.
4. Dessiner la droite $D_4$ d'équation $x + 2y + 2 = 0$.
5. Déterminer un vecteur directeur de $D_4$. De laquelle des autres droites $D_4$ est-elle parallèle ? Justifier par une propriété du cours.
   $\vec u = (-2, 1)$ dirige $D_4$ ; il est colinéaire à $\vec u_1 = (2, -1)$, donc $D_1$ et $D_4$ sont parallèles.

## Exercice 3 : nombres complexes 1
Type : forme algébrique, conjugué, module · ECUE : HP (nombres complexes, hors programme 2031)
Formules : $i^2 = -1$ ; $\overline{a + ib} = a - ib$ ; $\frac{z}{w} = \frac{z\bar w}{|w|^2}$ ; $|a + ib| = \sqrt{a^2 + b^2}$ ; $\left|\frac zw\right| = \frac{|z|}{|w|}$ ; $|\bar z| = |z|$

Soient $z_1 = 5 - 3i$, $z_2 = 2i + 3$, $z_3 = 1 + i$, $z_4 = 10 - 5i$ et $z_5 = 3 - 4i$.
1. Écrire les deux nombres complexes $Z_1 = iz_1 + \overline{z_2}\,z_3$ et $Z_2 = \dfrac{\overline{z_4}}{z_5}$ sous forme algébrique.
   $Z_1 = i(5 - 3i) + (3 - 2i)(1 + i) = 5i + 3 + 3 + 3i - 2i + 2 = 8 + 6i$.
   $Z_2 = \dfrac{10 + 5i}{3 - 4i} = \dfrac{(10 + 5i)(3 + 4i)}{3^2 + 4^2} = \dfrac{30 + 40i + 15i - 20}{25} = \dfrac{10 + 55i}{25} = \dfrac25 + \dfrac{11}5 i$.
2. Déterminer le module de $z_4$ et $z_5$. En déduire celui de $Z_2$.
   $|z_4| = \sqrt{10^2 + 5^2} = \sqrt{125} = 5\sqrt5$, $|z_5| = 5$, donc $|Z_2| = \dfrac{|\overline{z_4}|}{|z_5|} = \sqrt5$.

## Exercice 4 : nombres complexes 2
Type : forme exponentielle, argument · ECUE : HP (nombres complexes, hors programme 2031)
Formules : $z = |z|e^{i\theta}$ ; $e^{i\theta}e^{i\varphi} = e^{i(\theta + \varphi)}$ ; $\frac{e^{i\theta}}{e^{i\varphi}} = e^{i(\theta - \varphi)}$ ; $(re^{i\theta})^n = r^ne^{in\theta}$ ; $-i = e^{-i\pi/2}$

1. Écrire sous forme exponentielle : $z_1 = \sqrt3 - i$, $z_2 = 2 + 2i$, $z_3 = \dfrac{\sqrt3 - i}{2 + 2i}$ et $z_4 = (\sqrt3 - i)^5$.
   $|z_1| = 2$, $z_1 = 2\left(\frac{\sqrt3}2 - \frac12 i\right) = 2e^{-i\frac\pi6}$. $|z_2| = 2\sqrt2$, $z_2 = 2\sqrt2 e^{i\frac\pi4}$.
   $z_3 = \dfrac{2e^{-i\pi/6}}{2\sqrt2 e^{i\pi/4}} = \dfrac1{\sqrt2}e^{-i\frac{5\pi}{12}}$. $z_4 = z_1^5 = 32e^{-i\frac{5\pi}6}$.
2. Déterminer un argument de $z = \dfrac{-3i}{e^{i\pi/4}}$.
   $z = \dfrac{3e^{-i\pi/2}}{e^{i\pi/4}} = 3e^{-i\frac{3\pi}4}$. Un argument de $z$ est $-\frac{3\pi}4$ (le corrigé écrit $\frac{3\pi}4$, erreur de signe).

## Exercice 5 : résolution d'équation du second degré
Type : équation du second degré dans $\mathbb{C}$ · ECUE : HP (nombres complexes, hors programme 2031)
Formules : $\Delta = b^2 - 4ac$ ; $\Delta < 0$ : $z = \frac{-b \pm i\sqrt{-\Delta}}{2a}$

Résoudre dans $\mathbb{C}$ l'équation $z^2 - 3z + 3 = 0$.
$\Delta = 9 - 12 = -3$, donc $S = \left\{\dfrac{3 + i\sqrt3}2 ; \dfrac{3 - i\sqrt3}2\right\}$.
