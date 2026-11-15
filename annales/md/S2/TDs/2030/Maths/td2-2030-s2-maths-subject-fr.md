# Feuille de TD — Équations différentielles linéaires (S2 2026) (sujet, FR)

- Source : `raw/S2/TDs/2030/Maths/td2-2030-s2-maths-subject-fr.pdf` (4 pages)
- Date réelle : S2 2026 (dossier promo 2030). Feuille de TD d'une semaine, ECUE APEF (bloc B3). Pas de corrigé dans les annales. Corrigé rédigé : `td2-2030-s2-maths-correction-fr.md` (même dossier).
- Prérequis : OBM du séminaire, équation du second degré, dérivées et primitives usuelles. Seuls les exercices sont transcrits.

Attendus : résoudre une équation linéaire homogène du premier ordre à coefficients quelconques (calcul de primitive) ; identifier les solutions évidentes ; trouver une solution particulière par variation de la constante ; résoudre une équation homogène du second ordre à coefficients constants ; trouver une solution particulière quand le second membre est un polynôme ou un polynôme multiplié par $e^{mt}$, $m \in \mathbb{R}$.

## Exercice 1.1
Type : EDO linéaires 1er ordre (homogène, solution évidente, variation de la constante, condition initiale) · ECUE : APIS (EDO) · Niveau : maths-s1-apis-edo/6
Formules : $a(x)y' + b(x)y = 0 \Rightarrow y_0 = ke^{-\int \frac ba}$ ; solution générale = $y_0 + y_p$ ; solution évidente (constante, ou de la forme du second membre) ; variation de la constante : $y_p = k(x)y_0(x)$, il reste $a\,k'\,y_0 = c$ ; condition initiale : remplacer pour trouver $k$ ; $\int \frac{dx}{x\ln x} = \ln|\ln x|$, $\int \frac{dx}{1+x^2} = \arctan x$, $\int \tan = -\ln|\cos|$

Résoudre les équations différentielles suivantes :
1. $xy' - 2y = 0$ sur $\mathbb{R}_+^*$.
2. $(x^2 + 1)y' - y = 1$ sur $\mathbb{R}$.
3. $x\ln(x)y' - y = 4$ sur $]1, +\infty[$.
4. $y' + y = e^x - 1$ sur $\mathbb{R}$.
5. (Travail personnel) $y' - 2xy = (1 - 2x)e^x$ sur $\mathbb{R}$.
6. $y' - \dfrac{2y}{x+1} = (x+1)^3$ sur $]-1, +\infty[$.
7. $(1 + x^2)y' + xy = 3x^3 + 3x$ sur $\mathbb{R}$ en cherchant une solution particulière polynomiale de degré 2.
8. $\cos(t)y' - \sin(t)y = 1$ sur $\big]-\frac\pi2, \frac\pi2\big[$ avec la condition initiale $y(0) = 2$.

## Exercice 1.2
Type : modélisation par une EDO du 1er ordre (crédit) · ECUE : APIS (EDO) · Niveau : maths-s1-apis-edo/6
Formules : $y' = ay + b$ ($a \neq 0$) : $y = ke^{at} - \frac ba$ ; condition initiale $y(0) = y_0 \Rightarrow k = y_0 + \frac ba$ ; $C(t) = \big(C_0 - \frac kr\big)e^{rt} + \frac kr$ ; $C(T) = 0 \iff T = \frac1r\ln\frac{k}{k - rC_0}$ ; $e^x = a \iff x = \ln a$

Léa contracte un crédit immobilier d'un montant initial $C_0$ (en euros) auprès d'une banque. Le capital restant dû, $C(t)$ (en euros), évolue dans le temps selon les deux règles suivantes : la banque applique un taux d'intérêt constant $r$ (par an) tout au long de la durée du crédit ; l'emprunteur rembourse le prêt en effectuant des versements constants $k$ (par an, en euros). L'évolution du capital restant dû est alors décrite par l'équation différentielle $\dfrac{dC}{dt} = rC - k$, avec $C(0) = C_0$.
1. Justifier l'équation différentielle décrivant l'évolution du capital restant dû.
2. Résoudre l'équation différentielle.
3. Justifier pourquoi on peut imposer que $k > rC_0$.
4. Déterminer le temps $T$ nécessaire pour rembourser le prêt immobilier.
5. Application numérique : Léa emprunte 200000 euros à un taux annuel de 3 % et rembourse 500 euros par mois. Combien de temps lui faudra-t-il pour rembourser son crédit ?

## Exercice 2.3
Type : EDO 2nd ordre à coefficients constants avec second membre · ECUE : APIS (EDO) · Niveau : maths-s1-apis-edo/9
Formules : $ar^2 + br + c = 0$ : deux racines réelles $k_1e^{r_1x} + k_2e^{r_2x}$ ; racine double $(k_1x + k_2)e^{rx}$ ; complexes $\alpha \pm i\beta$ : $e^{\alpha x}(k_1\cos\beta x + k_2\sin\beta x)$ ; second membre polynôme : $y_p$ polynôme de même degré ; second membre $P(x)e^{mx}$ : $y_p = Q(x)e^{mx}$ avec $\deg Q = \deg P$ (+1 si $m$ racine simple, +2 si racine double) ; solution générale = homogène + particulière

Résoudre sur $\mathbb{R}$ les équations différentielles suivantes :
1. $y'' - 2y' + 10y = -5$
2. $y'' - y' - 2y = -x^2 - 3x$
3. $y'' + 2y' + 5y = xe^x$
4. (Travail personnel) $y'' - 5y' + 6y = e^{2x}$
5. $y'' - 4y' + 4y = xe^{2x}$
6. (Travail personnel) $y'' + y = e^x$

## Exercice 2.4
Type : EDO 2nd ordre à coefficients constants avec second membre · ECUE : APIS (EDO) · Niveau : maths-s1-apis-edo/9
Formules : $ar^2 + br + c = 0$ : deux racines réelles $k_1e^{r_1x} + k_2e^{r_2x}$ ; racine double $(k_1x + k_2)e^{rx}$ ; complexes $\alpha \pm i\beta$ : $e^{\alpha x}(k_1\cos\beta x + k_2\sin\beta x)$ ; second membre polynôme : $y_p$ polynôme de même degré ; second membre $P(x)e^{mx}$ : $y_p = Q(x)e^{mx}$ avec $\deg Q = \deg P$ (+1 si $m$ racine simple, +2 si racine double) ; solution générale = homogène + particulière

Pour vous entraîner chez vous. Résoudre sur $\mathbb{R}$ :
1. $2y'' + 6y' + 5y = 10x^3 + 36x^2 + 29x + 1$
2. $y'' + 2y' - 3y = (12x^2 + 16x + 14)e^{3x}$
3. $4y'' + 16y' + 16y = 8e^{-2x}$
4. $y'' - y = 2e^x$
