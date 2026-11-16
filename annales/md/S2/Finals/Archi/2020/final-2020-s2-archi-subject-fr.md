# Partiel S2 d'architecture des ordinateurs — juin 2016 (sujet, FR)

- Source : `raw/S2/Finals/Phys/2020/final-2020-s2-phys-subject-fr.pdf`, pages 45 à 50 (énoncé pages 45-46, document réponse pages 47-50 ; le PDF de 56 pages regroupe toute la session de juin 2016 ; la version anglaise est aux pages 51 à 56, non transcrite). Pas de corrigé officiel.
- Date réelle : juin 2016 (EPITA S2 2015/2016, dossier promo 2020). Corrigé : `final-2020-s2-archi-correction-fr.md`.
- Durée : 1 h 30. Réponses uniquement sur le document réponse ; ne pas détailler les calculs sauf demande explicite.

## Exercice 1 (2 points)
Type : flottants IEEE 754 simple et double précision (dénormalisé) · ECUE : Numération · Niveau : archi-s1-numeration/12
Formules : simple : 1 bit $S$, 8 bits $E$ (biais 127), 23 bits $M$ ; double : 1, 11 (biais 1023), 52 ; normalisé : $(-1)^S \times 1{,}M \times 2^{E - \text{biais}}$ ; $E = 0$ : dénormalisé $(-1)^S \times 0{,}M \times 2^{1 - \text{biais}}$ (double : $2^{-1022}$) ; $0{,}75 = 1{,}1_2 \times 2^{-1}$

1. Convertir le nombre $0{,}75$ dans le format flottant simple précision. Exprimer le résultat final sous forme binaire en précisant les trois champs ($S$, $E$, $M$).
2. Donner la représentation décimale associée au nombre codé en double précision $0004\ 4000\ 0000\ 0000_{16}$.

## Exercice 2 (5,5 points)
Type : décodage d'adresse par zone (bits de sélection, CS, adresses, redondance) · ECUE : Systèmes à microprocesseur · Niveau : archi-s2-microprocesseur/9
Formules : fils d'adresse $= \log_2(\text{capacité})$ ; linéaire possible si $P - C \geqslant n$ composants ; zone : $n$ bits de sélection de poids fort pour $2^n \geqslant$ composants ; $CS = AS \cdot$ (combinaison des bits de sélection) ; adresse basse : sélection, puis $0$ ; haute : bits du composant à $1$ ; images $= 2^{P - \text{sélection} - \text{fils}}$

Un système à microprocesseur comporte une mémoire morte (ROM), une mémoire vive (RAM) et deux périphériques (P1 et P2). Leurs capacités (en octets) sont respectivement 64 Kio, 8 Kio, 2 Kio et 512 octets. Le microprocesseur possède un bus d'adresse de 20 bits ($A_0$ à $A_{19}$, $A_0$ poids faible). Tous les composants ont un bus de donnée de 8 bits. La ROM sera située dans les adresses les plus faibles, viendront ensuite la RAM, P1 et P2.
1. Donner la taille du bus d'adresse de chaque mémoire et de chaque périphérique.
2. Est-il possible de réaliser un décodage de type linéaire ?

Pour tout le reste de l'exercice, c'est le mode zone qui sera utilisé avec le moins de zones possible.

3. Donner les bits de sélection qui serviront au décodage.
4. Donner la fonction de décodage en tenant compte du signal $AS$ (Address Strobe).
5. Donner les adresses hautes et basses de chaque composant (représentation hexadécimale à 5 chiffres).
6. Quelle est la redondance (le nombre d'images) des différents composants ?

## Exercice 3 (6 points)
Type : compteur synchrone à bascules JK (table d'excitation, Karnaugh) · ECUE : Logique séquentielle · Niveau : archi-s2-sequentielle/7
Formules : excitation JK : $0 \to 0$ : $J = 0$, $K = \Phi$ ; $0 \to 1$ : $1, \Phi$ ; $1 \to 0$ : $\Phi, 1$ ; $1 \to 1$ : $\Phi, 0$ ; états inutilisés en $\Phi$ ; regrouper les $1$ et les $\Phi$ par puissances de 2

On souhaite réaliser à l'aide de bascules JK la séquence $Q_2Q_1Q_0$ : $111 \to 100 \to 101 \to 110 \to 010 \to 001 \to 000$ (puis retour à $111$).
1. Remplir le tableau des entrées $J_2$, $K_2$, $J_1$, $K_1$, $J_0$, $K_0$ pour chaque état de la séquence.
2. Donner les expressions les plus simplifiées des entrées $J$ et $K$ de chaque bascule, en justifiant par des tableaux de Karnaugh les solutions qui ne sont pas évidentes (solution évidente : aucune opération logique hormis la complémentation, par exemple $J_0 = 1$, $K_1 = \overline{Q_2}$).

## Exercice 4 (6,5 points)
Type : décompteur asynchrone modulo N et chronogrammes (JK, D, RS) · ECUE : Logique séquentielle · Niveau : archi-s2-sequentielle/4
Formules : JK avec $J = K = 1$ : bascule $T$ ; front montant : décompteur si $H_i = Q_{i-1}$ (front descendant : $\overline{Q_{i-1}}$) ; modulo $N$ : détecter l'état transitoire $1111$ (NON-ET) et forcer $N - 1$ par $\overline{Pre}$ / $\overline{Clr}$ ; JK : $00$ mémoire, $10$ mise à 1, $01$ mise à 0, $11$ basculement ; D : $Q = D$ au front ; RS asynchrone : $S$ met à 1, $R$ met à 0

1. Câbler les 4 bascules JK du document réponse (horloge sur front montant, entrées asynchrones $\overline{Pre_i}$ et $\overline{Clr_i}$ actives à 0, horloge $C$ sur la bascule 0) afin de réaliser un décompteur asynchrone modulo 13.
2. Compléter les chronogrammes de $Q_0$ à $Q_4$ pour le montage ci-dessous (jusqu'à la dernière ligne verticale pointillée). Montage : bascule JK 0 ($J = E_0$, $K = E_1$, horloge $C$ sur front montant, sorties $Q_0$ et $\overline{Q_0}$) ; bascule JK 1 ($J = Q_0$, $K = \overline{Q_0}$, horloge $C$ sur front descendant) ; bascule RS asynchrone ($R = E_2$, $S = E_3$, sortie $Q_2$) ; bascule D ($D = Q_2$, horloge $C$ sur front montant, sortie $Q_3$) ; $Q_4 = \text{NON-OU}(\overline{Q_1}, \overline{Q_3})$.
   Entrées, le temps étant compté en demi-périodes de $C$ (une ligne pointillée à chaque front, de $t = 1$ à $t = 14$) ; tous les $Q$ valent 0 au départ :
   - $C$ : 1 sur $[2k, 2k + 1]$, 0 sinon (fronts descendants en $t = 1, 3, \ldots, 13$, montants en $t = 2, 4, \ldots, 12$).
   - $E_0$ : 1 sur $[0 ; 1{,}4]$, $[1{,}9 ; 4{,}7]$, $[6{,}5 ; 8{,}3]$, $[11{,}5 ; 13{,}4]$.
   - $E_1$ : 1 sur $[0 ; 0{,}5]$, $[3{,}1 ; 5{,}6]$, $[8{,}6 ; 12{,}3]$.
   - $E_2$ : impulsions à 1 sur $[1 ; 1{,}5]$, $[5 ; 5{,}5]$, $[9{,}5 ; 11{,}6]$.
   - $E_3$ : impulsions à 1 sur $[2{,}5 ; 3{,}5]$, $[6{,}5 ; 7{,}5]$, $[8 ; 8{,}5]$.
