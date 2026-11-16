# Partiel d'électronique S2 — juin 2016 (sujet, FR)

- Source : `raw/S2/Finals/Phys/2020/final-2020-s2-phys-subject-fr.pdf`, pages 31 à 37 (le PDF de 56 pages regroupe toute la session de juin 2016 ; la version anglaise du sujet est aux pages 38 à 44, non transcrite). Pas de corrigé officiel.
- Date réelle : juin 2016 (EPITA InfoS2, dossier promo 2020). Corrigé : `final-2020-s2-elec-correction-fr.md`.
- Calculatrices et documents non autorisés, barème indicatif, réponses sur le sujet.

## Exercice 1. QCM (4 points, pas de point négatif)
Type : QCM régime sinusoïdal et nature des filtres du 2nd ordre · ECUE : Études des filtres · Niveau : elec-s2-filtres/3
Formules : amplitude complexe (référence sinus) : $S\sin(\omega t + \theta) \to Se^{j\theta}$ ; $\cos x = \sin(x + \frac\pi2)$ ; $Z = \frac{U}{I}$ ; $u$, $i$ en phase : résistance ; $i$ en avance de $\frac\pi2$ : condensateur, $Z = \frac1{C\omega}$ ; $i$ en retard : bobine, $Z = L\omega$ ; $LC\omega^2$ sans unité ; $\underline T = A_0\frac{Num}{1 + 2jz\frac\omega{\omega_0} - (\frac\omega{\omega_0})^2}$ : $Num = 1$ passe-bas, $-(\frac\omega{\omega_0})^2$ passe-haut, $2jz\frac\omega{\omega_0}$ passe-bande

Pour chacune des questions ci-dessous, entourer la ou les bonnes réponses.
1. Soit les signaux sinusoïdaux $s(t) = S\sin(\omega t + \theta)$ et $s'(t) = S'\cos(\omega t + \theta')$. Les amplitudes complexes de ces signaux sont : a) $\underline S = Se^{j\theta}$ et $\underline{S'} = S'e^{j\theta'}$ ; b) $\underline S = Se^{j\theta}$ et $\underline{S'} = S'e^{j(\theta' + \frac\pi2)}$ ; c) $\underline S = Se^{j\theta}$ et $\underline{S'} = S'e^{j(\theta' + \pi)}$ ; d) $\underline S = Se^{j\theta}$ et $\underline{S'} = S'e^{j(\theta' - \frac\pi2)}$.

On cherche à identifier un dipôle. Pour cela, on mesure le courant $i(t)$ qui le traverse et la tension $u(t)$ à ses bornes, et on obtient : $u(t) = 10\sin(\omega t)$ et $i(t) = 5 \cdot 10^{-3}\cos(\omega t + \phi)$ avec $\omega = 1000\ \text{rad·s}^{-1}$.

2. Si $\phi = 0$, ce dipôle est : a) une résistance $R = 2\ \text{k}\Omega$ ; b) une bobine d'inductance $L = 2$ H ; c) une résistance $R = 0{,}5\ \Omega$ ; d) un condensateur de capacité $C = 0{,}5\ \mu\text{F}$.
3. Si $\phi = -\frac\pi2$, ce dipôle est : a) une résistance $R = 2\ \text{k}\Omega$ ; b) une bobine d'inductance $L = 2$ H ; c) une résistance $R = 0{,}5\ \Omega$ ; d) un condensateur de capacité $C = 0{,}5\ \mu\text{F}$.
4. Quelle est l'unité du produit $LC\omega^2$ ? a) des farads ; b) des siemens ; c) sans unité ; d) des ohms.

La forme normalisée d'une fonction de transfert d'un filtre du 2e ordre est de la forme : $\underline T = A_0\dfrac{\underline{Num}(\omega)}{1 + 2jz\frac{\omega}{\omega_0} - \left(\frac{\omega}{\omega_0}\right)^2}$.

5. Si $\underline{Num}(\omega) = 2jz\frac{\omega}{\omega_0}$, alors il s'agit d'un filtre : a) passe-bas ; b) passe-haut ; c) passe-bande ; d) coupe-bande.
6. Si $\underline{Num}(\omega) = -\left(\frac{\omega}{\omega_0}\right)^2$, alors il s'agit d'un filtre : a) passe-bas ; b) passe-haut ; c) passe-bande ; d) coupe-bande.
7. Pour un filtre passe-haut, $A_0$ est l'amplification maximale. a) VRAI ; b) FAUX.
8. Pour un filtre passe-bande, $A_0$ est l'amplification en très hautes fréquences. a) VRAI ; b) FAUX.

## Exercice 2. Filtres du premier ordre (8 points)
Type : filtre du 1er ordre (étude qualitative, transfert, Bode, régime sinusoïdal) · ECUE : Études des filtres · Niveau : elec-s2-filtres/6
Formules : TBF : bobine = fil, condensateur = interrupteur ouvert ; THF : l'inverse ; diviseur de tension $\underline{V_s} = \frac{Z_2}{Z_1 + Z_2}\underline{V_e}$ ; $Z_1 \parallel Z_2 = \frac{Z_1Z_2}{Z_1 + Z_2}$ ; passe-haut $\underline T = A_0\frac{j\frac\omega{\omega_c}}{1 + j\frac\omega{\omega_c}}$, passe-bas $\underline T = \frac{A_0}{1 + j\frac\omega{\omega_c}}$ ; $G_{dB} = 20\log|\underline T|$, pente $\pm 20$ dB/décade ; $v_s = V_E|\underline T|\sin(\omega t + \arg\underline T)$

Soit le filtre suivant (schéma) : $v_e(t)$ en entrée, une résistance $R$ en série, puis une bobine $L$ en parallèle (vers la masse), puis une seconde résistance $R$ en série, et enfin une résistance $R$ vers la masse aux bornes de laquelle on prend $v_s(t)$.
1. Étude qualitative : calculer les limites du gain quand $f \to 0$ et quand $f \to \infty$ et en déduire le type de filtre. Que vaut l'amplification maximale ?
2. Déterminer sa fonction de transfert. En déduire la pulsation de coupure.
3. Diagramme de Bode asymptotique. Tracer la courbe de gain. Préciser les limites du gain en très basses et très hautes fréquences, ainsi que l'équation de l'asymptote oblique.
4. Quel type de filtre obtient-on si on remplace la bobine par un condensateur ? Justifier (on ne demande pas de refaire une étude complète).
5. Si $v_e(t) = V_E\sin(\omega t)$, quelle est l'expression de $v_s(t)$ ?

## Exercice 3. Filtre du second ordre (8 points)
Type : filtre du 2nd ordre RLC (étude qualitative, forme normalisée, Bode) · ECUE : Études des filtres · Niveau : elec-s2-filtres/8
Formules : TBF / THF : bobine et condensateur en fil ou circuit ouvert ; $\underline T = \frac{A_0}{1 + 2jz\frac\omega{\omega_0} - (\frac\omega{\omega_0})^2}$ ; identifier $A_0$, $\omega_0^2$, $\frac{2z}{\omega_0}$ ; THF : $G_{dB} \approx 20\log A_0 - 40\log\frac\omega{\omega_0}$ ; phase $0 \to -\pi$ (passe-bas), $\pi \to 0$ (passe-haut)

Soit le circuit suivant (schéma) : la source $v_e(t)$ alimente une résistance $R$ et une bobine $L$ en série, puis un condensateur $C$ en parallèle avec une résistance $R$ ; $v_s(t)$ est la tension aux bornes de ce dernier groupe $C \parallel R$.
1. Étude qualitative : calculer les limites du gain quand $f \to 0$ et quand $f \to \infty$ et en déduire le type de filtre.
2. Déterminer sa fonction de transfert et la mettre sous la forme générale. Préciser les expressions de $A_0$, $\omega_0$ et $z$.
3. Diagrammes de Bode asymptotiques. Tracer les courbes de gain et de phase. Préciser les limites du gain et de la phase en très basses et très hautes fréquences, ainsi que l'équation de l'asymptote oblique pour la courbe de gain.
4. Quel type de filtre obtient-on si on inverse la bobine et le condensateur ? Justifier (on ne demande pas de refaire une étude complète).
