# Partiel S2 d'architecture des ordinateurs — juin 2016 (corrigé rédigé, FR)

- Source : `raw/S2/Finals/Phys/2020/final-2020-s2-phys-subject-fr.pdf`, pages 45 à 50 (énoncé pages 45-46, document réponse pages 47-50 ; le PDF de 56 pages regroupe toute la session de juin 2016 ; la version anglaise est aux pages 51 à 56, non transcrite). Pas de corrigé officiel : corrigé rédigé pour cette application (IEEE 754 vérifié avec Python, chronogrammes simulés à la main sur la grille du document réponse).
- Date réelle : juin 2016 (EPITA S2 2015/2016, dossier promo 2020). Sujet : `final-2020-s2-archi-subject-fr.md`.
- Durée : 1 h 30. Réponses uniquement sur le document réponse ; ne pas détailler les calculs sauf demande explicite. Les lignes `> ` sont les solutions.

## Exercice 1 (2 points)
Type : flottants IEEE 754 simple et double précision (dénormalisé) · ECUE : Numération · Niveau : archi-s1-numeration/12
Formules : simple : 1 bit $S$, 8 bits $E$ (biais 127), 23 bits $M$ ; double : 1, 11 (biais 1023), 52 ; normalisé : $(-1)^S \times 1{,}M \times 2^{E - \text{biais}}$ ; $E = 0$ : dénormalisé $(-1)^S \times 0{,}M \times 2^{1 - \text{biais}}$ (double : $2^{-1022}$) ; $0{,}75 = 1{,}1_2 \times 2^{-1}$

1. Convertir le nombre $0{,}75$ dans le format flottant simple précision. Exprimer le résultat final sous forme binaire en précisant les trois champs ($S$, $E$, $M$).
> $0{,}75 = 0{,}11_2 = 1{,}1_2 \times 2^{-1}$ : $S = 0$, $E = 127 - 1 = 126 = 0111\,1110$, $M = 100\,0000\,0000\,0000\,0000\,0000$ (23 bits). Soit $3F40\,0000_{16}$.
2. Donner la représentation décimale associée au nombre codé en double précision $0004\ 4000\ 0000\ 0000_{16}$.
> $S = 0$, $E = 000\,0000\,0000 = 0$ : nombre dénormalisé. $M = 0100\,0100\,0000\ldots$, soit $0{,}M = 2^{-2} + 2^{-6}$.
> Valeur $= (2^{-2} + 2^{-6}) \times 2^{-1022} = 2^{-1024} + 2^{-1028} = 17 \times 2^{-1028} \approx 5{,}91 \cdot 10^{-309}$.

## Exercice 2 (5,5 points)
Type : décodage d'adresse par zone (bits de sélection, CS, adresses, redondance) · ECUE : Systèmes à microprocesseur · Niveau : archi-s2-microprocesseur/9
Formules : fils d'adresse $= \log_2(\text{capacité})$ ; linéaire possible si $P - C \geqslant n$ composants ; zone : $n$ bits de sélection de poids fort pour $2^n \geqslant$ composants ; $CS = AS \cdot$ (combinaison des bits de sélection) ; adresse basse : sélection, puis $0$ ; haute : bits du composant à $1$ ; images $= 2^{P - \text{sélection} - \text{fils}}$

Un système à microprocesseur comporte une mémoire morte (ROM), une mémoire vive (RAM) et deux périphériques (P1 et P2). Leurs capacités (en octets) sont respectivement 64 Kio, 8 Kio, 2 Kio et 512 octets. Le microprocesseur possède un bus d'adresse de 20 bits ($A_0$ à $A_{19}$, $A_0$ poids faible). Tous les composants ont un bus de donnée de 8 bits. La ROM sera située dans les adresses les plus faibles, viendront ensuite la RAM, P1 et P2.
1. Donner la taille du bus d'adresse de chaque mémoire et de chaque périphérique.
> ROM : $64\ \text{Ki} = 2^{16}$, 16 bits ($A_0$-$A_{15}$). RAM : $2^{13}$, 13 bits. P1 : $2^{11}$, 11 bits. P2 : $2^9$, 9 bits.
2. Est-il possible de réaliser un décodage de type linéaire ?
> Oui : il reste $20 - 16 = 4$ bits ($A_{16}$ à $A_{19}$) au-dessus du plus grand composant, un par composant.

Pour tout le reste de l'exercice, c'est le mode zone qui sera utilisé avec le moins de zones possible.

3. Donner les bits de sélection qui serviront au décodage.
> 4 composants, donc 4 zones : 2 bits de sélection, les poids forts $A_{19}$ et $A_{18}$ (zones de 256 Kio). ROM en zone $00$, RAM $01$, P1 $10$, P2 $11$.
4. Donner la fonction de décodage en tenant compte du signal $AS$ (Address Strobe).
> $CS_{ROM} = AS \cdot \overline{A_{19}} \cdot \overline{A_{18}}$ ; $CS_{RAM} = AS \cdot \overline{A_{19}} \cdot A_{18}$ ; $CS_{P1} = AS \cdot A_{19} \cdot \overline{A_{18}}$ ; $CS_{P2} = AS \cdot A_{19} \cdot A_{18}$.
5. Donner les adresses hautes et basses de chaque composant (représentation hexadécimale à 5 chiffres).
> ROM : $00000$ à $0FFFF$. RAM : $40000$ à $41FFF$. P1 : $80000$ à $807FF$. P2 : $C0000$ à $C01FF$ (bits inutilisés à 0).
6. Quelle est la redondance (le nombre d'images) des différents composants ?
> ROM : $20 - 2 - 16 = 2$ bits inutilisés, $2^2 = 4$ images. RAM : $5$ bits, $32$ images. P1 : $7$ bits, $128$ images. P2 : $9$ bits, $512$ images.

## Exercice 3 (6 points)
Type : compteur synchrone à bascules JK (table d'excitation, Karnaugh) · ECUE : Logique séquentielle · Niveau : archi-s2-sequentielle/7
Formules : excitation JK : $0 \to 0$ : $J = 0$, $K = \Phi$ ; $0 \to 1$ : $1, \Phi$ ; $1 \to 0$ : $\Phi, 1$ ; $1 \to 1$ : $\Phi, 0$ ; états inutilisés en $\Phi$ ; regrouper les $1$ et les $\Phi$ par puissances de 2

On souhaite réaliser à l'aide de bascules JK la séquence $Q_2Q_1Q_0$ : $111 \to 100 \to 101 \to 110 \to 010 \to 001 \to 000$ (puis retour à $111$).
1. Remplir le tableau des entrées $J_2$, $K_2$, $J_1$, $K_1$, $J_0$, $K_0$ pour chaque état de la séquence.
> $111 \to 100$ : $J_2K_2 = \Phi0$, $J_1K_1 = \Phi1$, $J_0K_0 = \Phi1$.
> $100 \to 101$ : $\Phi0$, $0\Phi$, $1\Phi$.
> $101 \to 110$ : $\Phi0$, $1\Phi$, $\Phi1$.
> $110 \to 010$ : $\Phi1$, $\Phi0$, $0\Phi$.
> $010 \to 001$ : $0\Phi$, $\Phi1$, $1\Phi$.
> $001 \to 000$ : $0\Phi$, $0\Phi$, $\Phi1$.
> $000 \to 111$ : $1\Phi$, $1\Phi$, $1\Phi$. L'état $011$ n'apparaît pas : $\Phi$ partout.
2. Donner les expressions les plus simplifiées des entrées $J$ et $K$ de chaque bascule, en justifiant par des tableaux de Karnaugh les solutions qui ne sont pas évidentes (solution évidente : aucune opération logique hormis la complémentation, par exemple $J_0 = 1$, $K_1 = \overline{Q_2}$).
> $K_0 = 1$ (évident : tous les $1 \to 0$ de $Q_0$).
> $J_0$ : vaut 0 seulement en $110$ (1 en $000$, $010$, $100$) : $J_0 = \overline{Q_2} + \overline{Q_1}$.
> $J_1$ : 1 en $000$ et $101$, 0 en $001$ et $100$ : $J_1 = \overline{Q_2}\,\overline{Q_0} + Q_2Q_0 = \overline{Q_2 \oplus Q_0}$.
> $K_1$ : 1 en $111$ et $010$, 0 en $110$, $\Phi$ en $011$ : $K_1 = \overline{Q_2} + Q_0$.
> $J_2$ : 1 en $000$, 0 en $001$ et $010$, $\Phi$ en $011$ : $J_2 = \overline{Q_1}\,\overline{Q_0}$.
> $K_2$ : 1 en $110$, 0 en $111$, $100$, $101$ : $K_2 = Q_1\overline{Q_0}$.

## Exercice 4 (6,5 points)
Type : décompteur asynchrone modulo N et chronogrammes (JK, D, RS) · ECUE : Logique séquentielle · Niveau : archi-s2-sequentielle/4
Formules : JK avec $J = K = 1$ : bascule $T$ ; front montant : décompteur si $H_i = Q_{i-1}$ (front descendant : $\overline{Q_{i-1}}$) ; modulo $N$ : détecter l'état transitoire $1111$ (NON-ET) et forcer $N - 1$ par $\overline{Pre}$ / $\overline{Clr}$ ; JK : $00$ mémoire, $10$ mise à 1, $01$ mise à 0, $11$ basculement ; D : $Q = D$ au front ; RS asynchrone : $S$ met à 1, $R$ met à 0

1. Câbler les 4 bascules JK du document réponse (horloge sur front montant, entrées asynchrones $\overline{Pre_i}$ et $\overline{Clr_i}$ actives à 0, horloge $C$ sur la bascule 0) afin de réaliser un décompteur asynchrone modulo 13.
> $J_i = K_i = 1$ pour les 4 bascules. Front montant et décompteur : $H_0 = C$, $H_1 = Q_0$, $H_2 = Q_1$, $H_3 = Q_2$.
> Séquence voulue $12, 11, \ldots, 0$ puis $12$. Après $0000$ le décompteur passe par l'état transitoire $1111$ : on le détecte avec un NON-ET de $Q_3, Q_2, Q_1, Q_0$ (ou de $Q_3, Q_2, Q_1$ : $14$ n'apparaît jamais) relié à $\overline{Pre_3}$, $\overline{Pre_2}$, $\overline{Clr_1}$, $\overline{Clr_0}$ : $1111 \to 1100 = 12$. Les autres entrées asynchrones restent à 1.
2. Compléter les chronogrammes de $Q_0$ à $Q_4$ pour le montage ci-dessous (jusqu'à la dernière ligne verticale pointillée). Montage : bascule JK 0 ($J = E_0$, $K = E_1$, horloge $C$ sur front montant, sorties $Q_0$ et $\overline{Q_0}$) ; bascule JK 1 ($J = Q_0$, $K = \overline{Q_0}$, horloge $C$ sur front descendant) ; bascule RS asynchrone ($R = E_2$, $S = E_3$, sortie $Q_2$) ; bascule D ($D = Q_2$, horloge $C$ sur front montant, sortie $Q_3$) ; $Q_4 = \text{NON-OU}(\overline{Q_1}, \overline{Q_3})$.
   Entrées, le temps étant compté en demi-périodes de $C$ (une ligne pointillée à chaque front, de $t = 1$ à $t = 14$) ; tous les $Q$ valent 0 au départ :
   - $C$ : 1 sur $[2k, 2k + 1]$, 0 sinon (fronts descendants en $t = 1, 3, \ldots, 13$, montants en $t = 2, 4, \ldots, 12$).
   - $E_0$ : 1 sur $[0 ; 1{,}4]$, $[1{,}9 ; 4{,}7]$, $[6{,}5 ; 8{,}3]$, $[11{,}5 ; 13{,}4]$.
   - $E_1$ : 1 sur $[0 ; 0{,}5]$, $[3{,}1 ; 5{,}6]$, $[8{,}6 ; 12{,}3]$.
   - $E_2$ : impulsions à 1 sur $[1 ; 1{,}5]$, $[5 ; 5{,}5]$, $[9{,}5 ; 11{,}6]$.
   - $E_3$ : impulsions à 1 sur $[2{,}5 ; 3{,}5]$, $[6{,}5 ; 7{,}5]$, $[8 ; 8{,}5]$.
> $Q_0$ (fronts montants, $J = E_0$, $K = E_1$) : $t = 2$ : $10$ mise à 1 ; $t = 4$ : $11$ bascule à 0 ; $t = 6$ : $00$ reste 0 ; $t = 8$ : $10$ mise à 1 ; $t = 10$ : $01$ mise à 0 ; $t = 12$ : $10$ mise à 1. $Q_0 = 1$ sur $[2, 4]$, $[8, 10]$, $[12, 14]$.
> $Q_1$ (fronts descendants, recopie $Q_0$) : $Q_1 = 1$ sur $[3, 5]$, $[9, 11]$, $[13, 14]$.
> $Q_2$ (RS asynchrone) : mis à 1 en $2{,}5$, à 0 en $5$, à 1 en $6{,}5$, à 0 en $9{,}5$. $Q_2 = 1$ sur $[2{,}5 ; 5]$ et $[6{,}5 ; 9{,}5]$.
> $Q_3$ (D, fronts montants, recopie $Q_2$) : $Q_3 = 1$ sur $[4, 6]$ et $[8, 10]$.
> $Q_4 = \overline{\overline{Q_1} + \overline{Q_3}} = Q_1 \cdot Q_3$ : $Q_4 = 1$ sur $[4, 5]$ et $[9, 10]$.
