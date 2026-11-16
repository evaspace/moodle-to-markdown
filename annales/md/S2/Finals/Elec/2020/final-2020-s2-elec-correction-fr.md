# Partiel d'électronique S2 — juin 2016 (corrigé rédigé, FR)

- Source : `raw/S2/Finals/Phys/2020/final-2020-s2-phys-subject-fr.pdf`, pages 31 à 37 (le PDF de 56 pages regroupe toute la session de juin 2016 ; la version anglaise du sujet est aux pages 38 à 44, non transcrite). Pas de corrigé officiel : corrigé rédigé pour cette application, fonctions de transfert vérifiées avec sympy.
- Date réelle : juin 2016 (EPITA InfoS2, dossier promo 2020). Sujet : `final-2020-s2-elec-subject-fr.md`.
- Calculatrices et documents non autorisés, barème indicatif, réponses sur le sujet. Les lignes `> ` sont les solutions.

## Exercice 1. QCM (4 points, pas de point négatif)
Type : QCM régime sinusoïdal et nature des filtres du 2nd ordre · ECUE : Études des filtres · Niveau : elec-s2-filtres/3
Formules : amplitude complexe (référence sinus) : $S\sin(\omega t + \theta) \to Se^{j\theta}$ ; $\cos x = \sin(x + \frac\pi2)$ ; $Z = \frac{U}{I}$ ; $u$, $i$ en phase : résistance ; $i$ en avance de $\frac\pi2$ : condensateur, $Z = \frac1{C\omega}$ ; $i$ en retard : bobine, $Z = L\omega$ ; $LC\omega^2$ sans unité ; $\underline T = A_0\frac{Num}{1 + 2jz\frac\omega{\omega_0} - (\frac\omega{\omega_0})^2}$ : $Num = 1$ passe-bas, $-(\frac\omega{\omega_0})^2$ passe-haut, $2jz\frac\omega{\omega_0}$ passe-bande

Pour chacune des questions ci-dessous, entourer la ou les bonnes réponses.
1. Soit les signaux sinusoïdaux $s(t) = S\sin(\omega t + \theta)$ et $s'(t) = S'\cos(\omega t + \theta')$. Les amplitudes complexes de ces signaux sont : a) $\underline S = Se^{j\theta}$ et $\underline{S'} = S'e^{j\theta'}$ ; b) $\underline S = Se^{j\theta}$ et $\underline{S'} = S'e^{j(\theta' + \frac\pi2)}$ ; c) $\underline S = Se^{j\theta}$ et $\underline{S'} = S'e^{j(\theta' + \pi)}$ ; d) $\underline S = Se^{j\theta}$ et $\underline{S'} = S'e^{j(\theta' - \frac\pi2)}$.
> b) : la référence est le sinus et $S'\cos(\omega t + \theta') = S'\sin(\omega t + \theta' + \frac\pi2)$.

On cherche à identifier un dipôle. Pour cela, on mesure le courant $i(t)$ qui le traverse et la tension $u(t)$ à ses bornes, et on obtient : $u(t) = 10\sin(\omega t)$ et $i(t) = 5 \cdot 10^{-3}\cos(\omega t + \phi)$ avec $\omega = 1000\ \text{rad·s}^{-1}$.

2. Si $\phi = 0$, ce dipôle est : a) une résistance $R = 2\ \text{k}\Omega$ ; b) une bobine d'inductance $L = 2$ H ; c) une résistance $R = 0{,}5\ \Omega$ ; d) un condensateur de capacité $C = 0{,}5\ \mu\text{F}$.
> d) : $i = 5 \cdot 10^{-3}\sin(\omega t + \frac\pi2)$ est en avance de $\frac\pi2$ sur $u$ : condensateur. $\frac{1}{C\omega} = \frac{10}{5 \cdot 10^{-3}} = 2000\ \Omega$, donc $C = \frac{1}{2000 \times 1000} = 0{,}5\ \mu\text{F}$.
3. Si $\phi = -\frac\pi2$, ce dipôle est : a) une résistance $R = 2\ \text{k}\Omega$ ; b) une bobine d'inductance $L = 2$ H ; c) une résistance $R = 0{,}5\ \Omega$ ; d) un condensateur de capacité $C = 0{,}5\ \mu\text{F}$.
> a) : $i = 5 \cdot 10^{-3}\sin(\omega t)$ est en phase avec $u$ : résistance $R = \frac{10}{5 \cdot 10^{-3}} = 2\ \text{k}\Omega$.
4. Quelle est l'unité du produit $LC\omega^2$ ? a) des farads ; b) des siemens ; c) sans unité ; d) des ohms.
> c) : $L\omega$ et $\frac1{C\omega}$ sont des ohms, leur quotient $LC\omega^2$ est sans unité.

La forme normalisée d'une fonction de transfert d'un filtre du 2e ordre est de la forme : $\underline T = A_0\dfrac{\underline{Num}(\omega)}{1 + 2jz\frac{\omega}{\omega_0} - \left(\frac{\omega}{\omega_0}\right)^2}$.

5. Si $\underline{Num}(\omega) = 2jz\frac{\omega}{\omega_0}$, alors il s'agit d'un filtre : a) passe-bas ; b) passe-haut ; c) passe-bande ; d) coupe-bande.
> c) : $\underline T \to 0$ en TBF et en THF, $\underline T(\omega_0) = A_0$.
6. Si $\underline{Num}(\omega) = -\left(\frac{\omega}{\omega_0}\right)^2$, alors il s'agit d'un filtre : a) passe-bas ; b) passe-haut ; c) passe-bande ; d) coupe-bande.
> b) : $\underline T \to 0$ en TBF et $\underline T \to A_0$ en THF.
7. Pour un filtre passe-haut, $A_0$ est l'amplification maximale. a) VRAI ; b) FAUX.
> b) FAUX : $A_0$ est l'amplification en très hautes fréquences ; si $z < \frac{1}{\sqrt2}$, il y a résonance et le gain dépasse $A_0$.
8. Pour un filtre passe-bande, $A_0$ est l'amplification en très hautes fréquences. a) VRAI ; b) FAUX.
> b) FAUX : en THF le gain tend vers 0 ; $A_0$ est l'amplification à $\omega_0$ (maximale).

## Exercice 2. Filtres du premier ordre (8 points)
Type : filtre du 1er ordre (étude qualitative, transfert, Bode, régime sinusoïdal) · ECUE : Études des filtres · Niveau : elec-s2-filtres/6
Formules : TBF : bobine = fil, condensateur = interrupteur ouvert ; THF : l'inverse ; diviseur de tension $\underline{V_s} = \frac{Z_2}{Z_1 + Z_2}\underline{V_e}$ ; $Z_1 \parallel Z_2 = \frac{Z_1Z_2}{Z_1 + Z_2}$ ; passe-haut $\underline T = A_0\frac{j\frac\omega{\omega_c}}{1 + j\frac\omega{\omega_c}}$, passe-bas $\underline T = \frac{A_0}{1 + j\frac\omega{\omega_c}}$ ; $G_{dB} = 20\log|\underline T|$, pente $\pm 20$ dB/décade ; $v_s = V_E|\underline T|\sin(\omega t + \arg\underline T)$

Soit le filtre suivant (schéma) : $v_e(t)$ en entrée, une résistance $R$ en série, puis une bobine $L$ en parallèle (vers la masse), puis une seconde résistance $R$ en série, et enfin une résistance $R$ vers la masse aux bornes de laquelle on prend $v_s(t)$.
1. Étude qualitative : calculer les limites du gain quand $f \to 0$ et quand $f \to \infty$ et en déduire le type de filtre. Que vaut l'amplification maximale ?
> $f \to 0$ : la bobine est un fil, elle court-circuite la suite : $v_s \to 0$. $f \to \infty$ : la bobine est un circuit ouvert, il reste le diviseur $R$, $R$, $R$ : $v_s = \frac{R}{3R}v_e$, gain $\frac13$.
> Filtre passe-haut, amplification maximale $\frac13$ (soit $-9{,}5$ dB).
2. Déterminer sa fonction de transfert. En déduire la pulsation de coupure.
> Au nœud de la bobine, $\underline{Z_A} = jL\omega \parallel 2R = \frac{2jRL\omega}{2R + jL\omega}$, puis $\underline{V_A} = \frac{\underline{Z_A}}{R + \underline{Z_A}}\underline{V_e}$ et $\underline{V_s} = \frac12\underline{V_A}$.
> $\underline T = \dfrac{jL\omega}{2R + 3jL\omega} = \dfrac13 \cdot \dfrac{j\frac{\omega}{\omega_c}}{1 + j\frac{\omega}{\omega_c}}$ avec $\omega_c = \dfrac{2R}{3L}$.
3. Diagramme de Bode asymptotique. Tracer la courbe de gain. Préciser les limites du gain en très basses et très hautes fréquences, ainsi que l'équation de l'asymptote oblique.
> $G_{dB} = 20\log\frac13 + 20\log\frac{\omega/\omega_c}{\sqrt{1 + (\omega/\omega_c)^2}}$.
> THF : asymptote horizontale $G_{dB} = -20\log3 \approx -9{,}5$ dB. TBF : $G_{dB} \to -\infty$, asymptote oblique $G_{dB} = -9{,}5 + 20\log\frac{\omega}{\omega_c}$ (pente $+20$ dB/décade). Les deux se coupent en $\omega_c$ ; la courbe réelle y passe 3 dB en dessous ($-12{,}5$ dB).
4. Quel type de filtre obtient-on si on remplace la bobine par un condensateur ? Justifier (on ne demande pas de refaire une étude complète).
> Passe-bas : en TBF le condensateur est ouvert, gain $\frac13$ ; en THF il court-circuite la sortie, gain 0. (Calcul : $\underline T = \dfrac{1/3}{1 + j\frac{2RC\omega}{3}}$.)
5. Si $v_e(t) = V_E\sin(\omega t)$, quelle est l'expression de $v_s(t)$ ?
> Avec $x = \frac{\omega}{\omega_c}$ : $|\underline T| = \dfrac{x}{3\sqrt{1 + x^2}}$ et $\arg\underline T = \dfrac\pi2 - \arctan x$.
> $v_s(t) = \dfrac{V_E}{3}\dfrac{\omega/\omega_c}{\sqrt{1 + (\omega/\omega_c)^2}}\sin\left(\omega t + \dfrac\pi2 - \arctan\dfrac{\omega}{\omega_c}\right)$, $\omega_c = \dfrac{2R}{3L}$.

## Exercice 3. Filtre du second ordre (8 points)
Type : filtre du 2nd ordre RLC (étude qualitative, forme normalisée, Bode) · ECUE : Études des filtres · Niveau : elec-s2-filtres/8
Formules : TBF / THF : bobine et condensateur en fil ou circuit ouvert ; $\underline T = \frac{A_0}{1 + 2jz\frac\omega{\omega_0} - (\frac\omega{\omega_0})^2}$ ; identifier $A_0$, $\omega_0^2$, $\frac{2z}{\omega_0}$ ; THF : $G_{dB} \approx 20\log A_0 - 40\log\frac\omega{\omega_0}$ ; phase $0 \to -\pi$ (passe-bas), $\pi \to 0$ (passe-haut)

Soit le circuit suivant (schéma) : la source $v_e(t)$ alimente une résistance $R$ et une bobine $L$ en série, puis un condensateur $C$ en parallèle avec une résistance $R$ ; $v_s(t)$ est la tension aux bornes de ce dernier groupe $C \parallel R$.
1. Étude qualitative : calculer les limites du gain quand $f \to 0$ et quand $f \to \infty$ et en déduire le type de filtre.
> $f \to 0$ : bobine = fil, condensateur ouvert : diviseur $R$, $R$, gain $\frac12$. $f \to \infty$ : bobine ouverte (et condensateur en court-circuit) : gain 0. Filtre passe-bas.
2. Déterminer sa fonction de transfert et la mettre sous la forme générale. Préciser les expressions de $A_0$, $\omega_0$ et $z$.
> $\underline{Z} = R \parallel \frac{1}{jC\omega} = \frac{R}{1 + jRC\omega}$, $\underline T = \dfrac{\underline Z}{R + jL\omega + \underline Z} = \dfrac{1}{2 + j\left(RC + \frac LR\right)\omega - LC\omega^2}$.
> $\underline T = \dfrac{1/2}{1 + j\frac{RC + L/R}{2}\omega - \frac{LC}{2}\omega^2}$ : $A_0 = \dfrac12$, $\omega_0 = \sqrt{\dfrac{2}{LC}}$, $\dfrac{2z}{\omega_0} = \dfrac{RC + L/R}{2}$, soit $z = \dfrac{R^2C + L}{2R\sqrt{2LC}}$.
3. Diagrammes de Bode asymptotiques. Tracer les courbes de gain et de phase. Préciser les limites du gain et de la phase en très basses et très hautes fréquences, ainsi que l'équation de l'asymptote oblique pour la courbe de gain.
> TBF : $G_{dB} \to 20\log\frac12 \approx -6$ dB (asymptote horizontale), $\varphi \to 0$.
> THF : $\underline T \approx -A_0\left(\frac{\omega_0}{\omega}\right)^2$, asymptote oblique $G_{dB} = -6 - 40\log\dfrac{\omega}{\omega_0}$ (pente $-40$ dB/décade), $\varphi \to -\pi$. Les asymptotes se coupent en $\omega_0$, où $\varphi = -\frac\pi2$.
4. Quel type de filtre obtient-on si on inverse la bobine et le condensateur ? Justifier (on ne demande pas de refaire une étude complète).
> Passe-haut : en TBF le condensateur série est ouvert, gain 0 ; en THF il devient un fil et la bobine en parallèle est ouverte : diviseur $R$, $R$, gain $\frac12$.
