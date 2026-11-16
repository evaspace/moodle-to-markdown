"""Level path: S2 computer architecture, sequential logic (flip-flops, asynchronous and synchronous counters, shift registers).

Calibrated on the Moodle course « Archi S2 2030 - Logique Séquentielle et systèmes à microprocesseur » (chapters 1 and 2,
`Fiche Méthode - Les compteurs`) and on the exam `b3_exam3_fr.pdf` (2025/2026, B3: timing diagrams, JK and D synthesis of the
sequence 7,4,5,6,3,1,0, counter identification). Synthesis answers are checked by `build.py` with `seqD` / `seqJK`
(the flip-flop inputs must drive the counter through the sequence; unused states are free). Clock convention stated in each
statement: JK/T flip-flops with J=K=1 toggle on the active clock edge.
"""

SUBJECT = {
    "id": "archi-s2-sequentielle",
    "ordre": 430,
    "matiere": "archi",
    "semestre": "S2",
    "ecue": "Logique séquentielle",
    "titre": "Logique séquentielle : bascules et compteurs",
    "chapitres_moodle": ["01_Logique Séquentielle (B3)", "02_Documents de cours", "03_Travaux Dirigés"],
    "td": "TD de logique séquentielle (Moodle Archi S2)",
    "examens": ["Examen B3 d'architecture des ordinateurs"],
}

NOTIONS = [
    {"id": "bascules", "titre": "Bascules D, T, JK, RS",
     "formule": r"D : $Q^+=D$ · T : $Q^+=T\oplus Q$ · JK : $Q^+=J\overline Q+\overline K\,Q$ · $J=K=0$ garde, $J=1,K=0$ met à $1$, $J=0,K=1$ met à $0$, $J=K=1$ bascule · RS : $R=S=1$ interdit",
     "exemple": r"JK avec $J=K=1$ : $Q^+=\overline Q$",
     "cours": r"Une bascule mémorise un bit et ne change qu'à un front d'horloge (montant ou descendant selon la bascule). $Q^+$ est la valeur de $Q$ après le front, calculée avec les entrées présentes juste avant."},
    {"id": "chrono", "titre": "Chronogrammes",
     "formule": r"on lit les entrées juste avant chaque front actif · sortie $Q$ constante entre deux fronts · bascule D sur front montant : $Q$ prend la valeur de $D$ avant le front",
     "exemple": r"$D=1,0,1$ avant trois fronts montants successifs : $Q=1,0,1$ après chacun",
     "cours": r"Repérer d'abord les fronts actifs sur l'horloge (traits verticaux pointillés). Pour chaque front, déterminer $Q^+$ avec la table de la bascule, puis tracer $Q$ jusqu'au front suivant. Une entrée qui change entre deux fronts n'a aucun effet."},
    {"id": "asynchrone", "titre": "Compteurs et décompteurs asynchrones",
     "formule": r"$n$ bascules JK avec $J=K=1$ en cascade : modulo $2^n$ · $f_{Q_{n-1}}=\dfrac f{2^n}$ · front descendant : $H_i=Q_{i-1}$ compte, $H_i=\overline{Q_{i-1}}$ décompte (front montant : inversé) · bascules nécessaires pour modulo $N$ : $\lceil\log_2N\rceil$",
     "exemple": r"$4$ bascules : modulo $16$, la sortie $Q_3$ est à $f/16$",
     "cours": r"Asynchrone : l'horloge d'une bascule est la sortie de la précédente, donc les changements se propagent en série (état intermédiaire transitoire). Chaque bascule divise la fréquence par $2$."},
    {"id": "modulo", "titre": "Modulo N par remise à zéro",
     "formule": r"modulo $N<2^n$ : détecter l'état $N$ (porte NON-ET sur les bits à $1$) et activer la remise à zéro asynchrone · modulo $10$ : état $10=1010$, entrées $Q_3$ et $Q_1$ · décompteur modulo $15$ : détecter $1111$ et remettre $Q_0$ à $0$ ($\to1110$)",
     "exemple": r"modulo $10$ : séquence $0,\dots,9,0$ (l'état $10$ ne dure qu'un instant)",
     "cours": r"On choisit le plus petit nombre de bascules, puis on détecte la première valeur interdite avec une porte dont la sortie commande la remise à zéro (active à l'état bas pour un NON-ET). Pour détecter $1010$ il suffit de $Q_3$ et $Q_1$ : c'est le premier état qui les met à $1$ ensemble."},
    {"id": "excitation", "titre": "Table d'excitation",
     "formule": r"D : $D=Q^+$ · JK : $0\to0$: $J=0,K=\Phi$ · $0\to1$: $J=1,K=\Phi$ · $1\to0$: $J=\Phi,K=1$ · $1\to1$: $J=\Phi,K=0$ · T : $T=Q\oplus Q^+$",
     "exemple": r"transition $1\to0$ avec une bascule JK : $K=1$, $J$ indifférent",
     "cours": r"Pour réaliser une séquence, on dresse le tableau « état présent, état suivant » puis on déduit les entrées de chaque bascule. Les états non utilisés de la séquence donnent des indifférents (Φ) dans les tableaux de Karnaugh."},
    {"id": "synchrone", "titre": "Compteur synchrone (synthèse)",
     "formule": r"1. séquence $\to$ tableau $Q^+$ · 2. entrées des bascules par table d'excitation · 3. un tableau de Karnaugh par entrée (états non utilisés $=\Phi$) · 4. expressions simplifiées · bascule D : $D_i=Q_i^+$",
     "exemple": r"séquence $0,1,3,2$ avec des bascules D : $D_1=Q_0$, $D_0=\overline{Q_1}$",
     "cours": r"Toutes les bascules reçoivent la même horloge : l'état change en même temps. Une solution « évidente » ne contient aucune opération logique (constante, variable ou complément). Mettre en place le tableau de Karnaugh avant d'écrire l'expression."},
    {"id": "registre", "titre": "Registres à décalage",
     "formule": r"bascules D en série : $Q_i^+=Q_{i-1}$ · décalage à gauche d'un rang (entrée $0$) : $\times2$ · décalage à droite : division entière par $2$ · registre de $n$ bits chargé en $n$ coups d'horloge en série",
     "exemple": r"$0110\to1100$ après un décalage à gauche ($6\to12$)",
     "cours": r"Chaque front d'horloge fait avancer d'un rang les bits mémorisés. L'entrée série fournit le nouveau bit. Un registre à décalage convertit un mot série en mot parallèle et inversement."},
]


def v(id, enonce, calc, ans, sol, src=None, duree=None):
    e = {"id": id, "kind": "value", "enonce": enonce, "calc": calc, "ans": ans, "sol": sol}
    if src:
        e["src"] = src
    if duree:
        e["duree"] = duree
    return e


def o(id, enonce, sol, src=None, duree=None):
    e = {"id": id, "kind": "open", "enonce": enonce, "sol": sol}
    if src:
        e["src"] = src
    if duree:
        e["duree"] = duree
    return e


B3 = "Examen B3 d'architecture 2025/2026"

LEVELS = [
    {"n": 1, "titre": "Bascules D, T, JK, RS", "notions": ["bascules"], "exos": [
        v("s11", r"Bascule D : $D=1$, $Q=0$ avant le front actif. Valeur de $Q$ après ?", "1", "1", r"$Q^+=D=1$.", duree=1),
        v("s12", r"Bascule T : $T=1$, $Q=1$ avant le front actif. Valeur de $Q$ après ?", "(1+1)%2", "0", r"$Q^+=T\oplus Q=0$ (la bascule change d'état).", duree=1),
        v("s13", r"Bascule JK : $J=1$, $K=0$, $Q=0$ avant le front. Valeur de $Q$ après ?", "1", "1", r"$J=1,K=0$ met la bascule à $1$.", duree=1),
        v("s14", r"Bascule JK : $J=1$, $K=1$, $Q=1$ avant le front. Valeur de $Q$ après ?", "0", "0", r"$J=K=1$ : $Q^+=\overline Q=0$.", duree=1),
        v("s15", r"Bascule JK : $J=0$, $K=0$, $Q=1$ avant le front. Valeur de $Q$ après ?", "1", "1", r"$J=K=0$ : l'état est conservé.", duree=1),
        v("s16", r"Bascule JK : $J=1$, $K=0$, $Q=1$ avant le front. Valeur de $Q$ après ?", "1", "1", r"$Q^+=J\overline Q+\overline K\,Q=0+1=1$.", duree=1),
        o("s17", r"Donner la table de transition d'une bascule JK ($J,K,Q\to Q^+$) et en déduire $Q^+=J\overline Q+\overline KQ$.",
          r"| $J$ | $K$ | $Q^+$ |" "\n|---|---|---|\n"
          r"| 0 | 0 | $Q$ |" "\n" r"| 0 | 1 | 0 |" "\n" r"| 1 | 0 | 1 |" "\n" r"| 1 | 1 | $\overline Q$ |" "\n\n"
          r"Pour $Q=0$ : $Q^+=J$. Pour $Q=1$ : $Q^+=\overline K$. Donc $Q^+=J\overline Q+\overline K\,Q$.", duree=5),
    ]},
    {"n": 2, "titre": "Chronogrammes", "notions": ["chrono", "bascules"], "exos": [
        v("s21", r"Bascule D sur front montant, $Q=0$ au départ, $D=1,0,1$ avant les trois fronts successifs. Valeur de $Q$ après le troisième front ?", "1", "1", r"Après chaque front $Q$ prend la valeur de $D$ : $1,0,1$.", src=B3 + ", ex. 1", duree=2),
        v("s22", r"Bascule T, $Q=0$ au départ, $T=1$ à chaque front. Valeur de $Q$ après $5$ fronts ?", "5%2", "1", r"$Q$ alterne $1,0,1,0,1$.", src=B3 + ", ex. 1", duree=2),
        v("s23", r"Bascule JK, $Q=0$ au départ, entrées $(J,K)=(1,0),(0,0),(1,1),(0,1)$ avant quatre fronts. Valeur de $Q$ à la fin ?", "0", "0",
          r"$(1,0)\to Q=1$ ; $(0,0)\to1$ ; $(1,1)\to0$ ; $(0,1)\to0$.", src=B3 + ", ex. 1", duree=3),
        v("s24", r"Une entrée $D$ passe de $0$ à $1$ juste après un front montant. Quand $Q$ change-t-il (numéro du front suivant à partir de ce front, $1$ = le front suivant) ?", "1", "1", r"Au front suivant : une bascule synchrone ignore les changements entre deux fronts.", duree=2),
        o("s25", r"Une bascule D reçoit $D=1,1,0,1$ avant quatre fronts montants. Dessiner ou décrire $Q$ (avec $Q=0$ au départ).",
          r"$Q$ passe à $1$ au premier front, reste à $1$ au deuxième, passe à $0$ au troisième, repasse à $1$ au quatrième : $1,1,0,1$. $Q$ est constante entre deux fronts.", src=B3 + ", ex. 1", duree=5),
        o("s26", r"Qu'est-ce qui différencie un verrou (latch, sensible au niveau) d'une bascule sur front ?",
          r"Le verrou est transparent tant que son entrée d'horloge/autorisation est active : la sortie suit l'entrée pendant tout ce niveau. La bascule sur front n'échantillonne l'entrée qu'à l'instant du front, puis mémorise : plus fiable dans un circuit synchrone.", duree=4),
    ]},
    {"n": 3, "titre": "Compteurs asynchrones", "notions": ["asynchrone", "bascules"], "exos": [
        v("s31", r"Compteur asynchrone à $4$ bascules JK ($J=K=1$). Modulo ?", "2**4", "16", r"$2^4=16$ états (de $0$ à $15$).", duree=1),
        v("s32", r"Horloge à $1{,}6$ kHz sur $4$ bascules en cascade : fréquence de $Q_3$ (en Hz) ?", "1600/2**4", "100", r"$f/2^4=100$ Hz.", duree=2),
        v("s33", r"Combien de bascules pour compter jusqu'à $100$ (modulo $100$) ?", "7", "7", r"$2^6=64<100\le128=2^7$ : $7$ bascules.", duree=2),
        v("s34", r"Compteur $3$ bits, front descendant, $H_i=Q_{i-1}$ : état après $5$ fronts depuis $000$ (décimal) ?", "5", "5", r"Compteur binaire : $5=101_2$.", duree=2),
        v("s35", r"Même compteur : état après $9$ fronts depuis $000$ (modulo $8$, décimal) ?", "9%8", "1", r"$9\bmod8=1$.", duree=2),
        o("s36", r"Compteur à bascules JK ($J=K=1$) actives sur front descendant : comment relier les horloges pour obtenir un compteur ? un décompteur ?",
          r"Compteur : $H_i=Q_{i-1}$ (la bascule suivante bascule quand $Q_{i-1}$ passe de $1$ à $0$, c'est-à-dire après le passage de $11\ldots$ à $00\ldots$ du bit précédent)." "\n\n"
          r"Décompteur : $H_i=\overline{Q_{i-1}}$ (pour un déclenchement sur front montant, c'est l'inverse).", src=B3 + ", ex. 4", duree=6),
    ]},
    {"n": 4, "titre": "Modulo N par remise à zéro", "notions": ["modulo", "asynchrone"], "exos": [
        v("s41", r"Compteur modulo $10$ à $4$ bascules : quel état (décimal) déclenche la remise à zéro ?", "10", "10", r"L'état $10=1010$ est détecté puis remis à $0$.", duree=2),
        v("s42", r"Pour le modulo $10$ : combien d'entrées faut-il à la porte NON-ET de détection ?", "2", "2", r"$1010$ : $Q_3$ et $Q_1$ suffisent car $1010$ est le premier état à les avoir à $1$ ensemble.", duree=2),
        v("s43", r"Modulo $12$ : état de détection (décimal) ?", "12", "12", r"$12=1100$ : $Q_3$ et $Q_2$ à $1$.", duree=2),
        v("s44", r"Combien de bascules pour un modulo $12$ ?", "4", "4", r"$2^3=8<12\le16=2^4$.", duree=2),
        v("s45", r"Décompteur asynchrone modulo $15$ à $4$ bascules : après $0000$ vient $1111$ ; on remet $Q_0$ à $0$. Quel état suit alors $0000$ (décimal) ?", "14", "14", r"$1111$ avec $Q_0=0$ donne $1110=14$ : séquence $14,13,\dots,0,14$.", src=B3 + ", ex. 4", duree=3),
        o("s46", r"Câbler un compteur asynchrone modulo $6$ avec des bascules JK à front descendant et une remise à zéro asynchrone.",
          r"$3$ bascules ($2^2=4<6\le8$). Compteur : $H_0$ horloge, $H_1=Q_0$, $H_2=Q_1$, $J=K=1$ partout." "\n\n"
          r"L'état $6=110$ est détecté par une NON-ET sur $Q_2$ et $Q_1$ ; sa sortie (active à l'état bas) est reliée aux entrées de remise à zéro de toutes les bascules. La séquence est $0,\dots,5$ (l'état $6$ est transitoire).", duree=8),
    ]},
    {"n": 5, "titre": "Table d'excitation", "notions": ["excitation", "bascules"], "exos": [
        v("s51", r"Bascule JK : transition $0\to1$. Valeur de $J$ ?", "1", "1", r"Pour mettre à $1$, $J=1$ ; $K$ est indifférent.", duree=1),
        v("s52", r"Bascule JK : transition $1\to0$. Valeur de $K$ ?", "1", "1", r"Pour mettre à $0$, $K=1$ ; $J$ est indifférent.", duree=1),
        v("s53", r"Bascule JK : transition $1\to1$. Valeur de $K$ ?", "0", "0", r"$K=0$ ($J$ indifférent) : l'état est conservé ou mis à $1$.", duree=1),
        v("s54", r"Bascule D : transition $1\to0$. Valeur de $D$ ?", "0", "0", r"$D=Q^+=0$.", duree=1),
        v("s55", r"Bascule T : transition $0\to1$. Valeur de $T$ ?", "(0+1)%2", "1", r"$T=Q\oplus Q^+=1$.", duree=1),
        o("s56", r"Donner la table d'excitation d'une bascule JK ($Q\to Q^+$, $J$, $K$).",
          r"| $Q$ | $Q^+$ | $J$ | $K$ |" "\n|---|---|---|---|\n"
          r"| 0 | 0 | 0 | Φ |" "\n" r"| 0 | 1 | 1 | Φ |" "\n" r"| 1 | 0 | Φ | 1 |" "\n" r"| 1 | 1 | Φ | 0 |", duree=4),
    ]},
    {"n": 6, "titre": "Compteurs synchrones à bascules D", "notions": ["synchrone", "excitation"], "exos": [
        v("s61", r"Séquence $0,1,3,2$ (2 bits $Q_1Q_0$) avec des bascules D. Solutions proposées : $D_1=Q_0$ et $D_0=\overline{Q_1}$. Contrôle ?", "seqD(2, [0,1,3,2], [Q0, ~Q1])", "1",
          r"$00\to01$ ($D_1=0,D_0=1$) ; $01\to11$ ($D_1=1,D_0=1$) ; $11\to10$ ($D_1=1,D_0=0$) ; $10\to00$ ($D_1=0,D_0=0$)." "\n\n" r"Code de Gray : $D_1=Q_0$, $D_0=\overline{Q_1}$.", duree=5),
        v("s62", r"Séquence $0,2,3,1$ (2 bits) avec des bascules D. Solutions proposées : $D_1=\overline{Q_0}$ et $D_0=Q_1$. Contrôle ?", "seqD(2, [0,2,3,1], [~Q0, Q1])", "1",
          r"$00\to10$, $10\to11$, $11\to01$, $01\to00$ : $D_1=\overline{Q_0}$ et $D_0=Q_1$.", duree=5),
        v("s63", r"Séquence $7,4,5,6,3,1,0$ (3 bits, état $2$ inutilisé) avec des bascules D. Solutions proposées : $D_2=Q_2Q_0+\overline{Q_1}\,\overline{Q_0}$, $D_1=Q_1\overline{Q_0}+\overline{Q_2}\,\overline{Q_0}+Q_2\overline{Q_1}Q_0$, $D_0=\overline{Q_0}+\overline{Q_2}Q_1$. Contrôle ?",
          "seqD(3, [7,4,5,6,3,1,0], [(Q2&Q0)|(~Q1&~Q0), (Q1&~Q0)|(~Q2&~Q0)|(Q2&~Q1&Q0), ~Q0|(~Q2&Q1)])", "1",
          r"Chaque $D_i$ est la colonne $Q_i^+$ du tableau, simplifiée par Karnaugh avec Φ pour l'état $010$.", src=B3 + ", ex. 3", duree=15),
        v("s64", r"Séquence $0,1,2,3,4,5,6$ (modulo $7$, état $7$ inutilisé) avec des bascules D. Solution proposée pour $D_0$ : $\overline{Q_0}\,\overline{Q_1}+\overline{Q_0}\,\overline{Q_2}$. Contrôle (avec $D_2=Q_0Q_1+Q_2\overline{Q_1}$ et $D_1=Q_0\overline{Q_1}+Q_1\overline{Q_0}\,\overline{Q_2}$) ?",
          "seqD(3, [0,1,2,3,4,5,6], [(Q0&Q1)|(Q2&~Q1), (Q0&~Q1)|(Q1&~Q0&~Q2), (~Q0&~Q1)|(~Q0&~Q2)])", "1",
          r"Comptage binaire jusqu'à $6$, puis retour à $0$.", duree=12),
        v("s65", r"Combien de bascules D pour un compteur modulo $7$ ?", "3", "3", r"$2^2=4<7\le8=2^3$.", duree=1),
        o("s66", r"Dresser le tableau d'états présent / suivant pour la séquence $7,4,5,6,3,1,0$ et en déduire $D_2$, $D_1$, $D_0$ (méthode complète).",
          r"| $Q_2Q_1Q_0$ | $Q_2^+Q_1^+Q_0^+$ |" "\n|---|---|\n"
          r"| 111 | 100 |" "\n" r"| 100 | 101 |" "\n" r"| 101 | 110 |" "\n" r"| 110 | 011 |" "\n" r"| 011 | 001 |" "\n" r"| 001 | 000 |" "\n" r"| 000 | 111 |" "\n" r"| 010 | ΦΦΦ |" "\n\n"
          r"$D_2=Q_2Q_0+\overline{Q_1}\,\overline{Q_0}$ ; $D_1=Q_1\overline{Q_0}+\overline{Q_2}\,\overline{Q_0}+Q_2\overline{Q_1}Q_0$ ; $D_0=\overline{Q_0}+\overline{Q_2}Q_1$.", src=B3 + ", ex. 3", duree=15),
    ]},
    {"n": 7, "titre": "Compteurs synchrones à bascules JK", "notions": ["synchrone", "excitation"], "exos": [
        v("s71", r"Séquence $0,1,3,2$ avec des bascules JK. Solutions proposées : $J_1=Q_0$, $K_1=\overline{Q_0}$, $J_0=\overline{Q_1}$, $K_0=Q_1$. Contrôle ?", "seqJK(2, [0,1,3,2], [Q0, ~Q0, ~Q1, Q1])", "1",
          r"$00\to01$ : $J_0=1$ ; $01\to11$ : $J_1=1$ ; $11\to10$ : $K_0=1$ ; $10\to00$ : $K_1=1$. Mise sous forme : $J_1=Q_0$, $K_1=\overline{Q_0}$, $J_0=\overline{Q_1}$, $K_0=Q_1$.", duree=6),
        v("s72", r"Séquence $7,4,5,6,3,1,0$ avec des bascules JK : $J_0=1$ et $K_0=Q_2+\overline{Q_1}$ sont proposés pour la bascule $0$ ; avec $J_1=Q_0Q_2+\overline{Q_0}\,\overline{Q_2}$, $K_1=Q_0$, $J_2=\overline{Q_0}$, $K_2=Q_1\overline{Q_0}$. Contrôle de l'ensemble ?",
          "seqJK(3, [7,4,5,6,3,1,0], [~Q0, Q1&~Q0, (Q0&Q2)|(~Q0&~Q2), Q0, 1, Q2|~Q1])", "1",
          r"$J_0=1$ est une solution évidente (constante) ; $K_0$, $J_1$ demandent un Karnaugh avec Φ pour l'état $010$ et les cases de la table d'excitation.", src=B3 + ", ex. 2", duree=18),
        v("s73", r"Dans le compteur de séquence $7,4,5,6,3,1,0$ (3 bits), combien d'états sur $8$ ne sont pas utilisés ?", "8-7", "1", r"Sept états dans la séquence : seul $010$ est inutilisé, d'où des Φ dans les tableaux de Karnaugh.", src=B3 + ", ex. 2", duree=2),
        v("s74", r"Séquence $0,1,2,3,4,5,6$ avec des bascules JK. Solutions proposées : $J_2=Q_0Q_1$, $K_2=Q_1$, $J_1=Q_0$, $K_1=Q_0+Q_2$, $J_0=\overline{Q_1}+\overline{Q_2}$, $K_0=1$. Contrôle ?",
          "seqJK(3, [0,1,2,3,4,5,6], [Q0&Q1, Q1, Q0, Q0|Q2, ~Q1|~Q2, 1])", "1", r"Chaque paire $(J,K)$ respecte la table d'excitation sur les 7 transitions de la séquence.", duree=18),
        o("s75", r"Pourquoi les indifférents (Φ) de la table d'excitation de la bascule JK simplifient-ils davantage les expressions que pour la bascule D ?",
          r"Une bascule D n'a qu'une entrée qui impose $Q^+$ : tous les cas sont déterminés (seuls les états inutilisés sont Φ). Une bascule JK a deux entrées et la table d'excitation laisse $K$ (pour $0\to0$ et $0\to1$) ou $J$ (pour $1\to0$ et $1\to1$) libre : beaucoup plus de Φ dans les tableaux de Karnaugh, donc des groupes plus grands et des expressions plus courtes (souvent des constantes).", duree=6),
        o("s76", r"Donner le tableau $Q_2Q_1Q_0\to(J_2,K_2),(J_1,K_1),(J_0,K_0)$ pour la séquence $7,4,5,6,3,1,0$.",
          r"| $Q_2Q_1Q_0$ | $J_2K_2$ | $J_1K_1$ | $J_0K_0$ |" "\n|---|---|---|---|\n"
          r"| 111 | Φ 0 | Φ 1 | Φ 1 |" "\n" r"| 100 | Φ 0 | 0 Φ | 1 Φ |" "\n" r"| 101 | Φ 0 | 1 Φ | Φ 1 |" "\n" r"| 110 | Φ 1 | Φ 0 | 1 Φ |" "\n"
          r"| 011 | 0 Φ | Φ 1 | Φ 0 |" "\n" r"| 001 | 0 Φ | 0 Φ | Φ 1 |" "\n" r"| 000 | 1 Φ | 1 Φ | 1 Φ |" "\n\n"
          r"Chaque couple se lit dans la table d'excitation : $0\to0$ : $(0,\Phi)$ ; $0\to1$ : $(1,\Phi)$ ; $1\to0$ : $(\Phi,1)$ ; $1\to1$ : $(\Phi,0)$.", src=B3 + ", ex. 2 q. 1", duree=12),
    ]},
    {"n": 8, "titre": "Registres à décalage", "notions": ["registre", "bascules"], "exos": [
        v("s81", r"Registre à décalage à gauche de $4$ bits contenant $0110$, entrée série $0$. Contenu (décimal) après un coup d'horloge ?", "bits('1100')", "12", r"$0110\to1100=12$ ($6\times2$).", duree=2),
        v("s82", r"Registre à décalage à droite de $4$ bits contenant $1100$, entrée série $0$. Contenu (décimal) après un coup d'horloge ?", "bits('0110')", "6", r"$1100\to0110=6$ ($12/2$).", duree=2),
        v("s83", r"Registre de $8$ bits : combien de coups d'horloge pour charger un mot en série ?", "8", "8", r"Un bit par coup d'horloge : $8$.", duree=1),
        v("s84", r"Registre à décalage à gauche de $4$ bits à $0001$ (entrée série $0$) : contenu (décimal) après $3$ coups d'horloge ?", "bits('1000')", "8", r"$0001\to0010\to0100\to1000=8=2^3$.", duree=2),
        o("s85", r"Dessiner un registre à décalage de $4$ bits avec des bascules D et expliquer le décalage d'un rang.",
          r"$Q_0$ est relié à $D_1$, $Q_1$ à $D_2$, $Q_2$ à $D_3$ ; $D_0$ reçoit l'entrée série ; horloge commune. À chaque front : $Q_0^+=D_0$, $Q_1^+=Q_0$, $Q_2^+=Q_1$, $Q_3^+=Q_2$ : le contenu avance d'un rang et $Q_3$ est la sortie série.", duree=6),
    ]},
    {"n": 9, "titre": "Niveau examen : sujet B3", "notions": ["chrono", "excitation", "synchrone", "asynchrone", "modulo"], "examen": True, "exos": [
        o("sx1", r"Compléter les chronogrammes de deux montages à bascules et la table de vérité d'un montage combinatoire à partir de bascules (méthode générale).",
          r"Pour chaque montage : nommer les bascules, écrire leurs équations ($Q^+=\ldots$), repérer les fronts actifs, évaluer les entrées juste avant chaque front, et tracer $Q$ constant jusqu'au front suivant. Pour la table de vérité, évaluer la sortie pour les 4 combinaisons de $A,B$.", src=B3 + ", ex. 1 (7 points)", duree=15),
        o("sx2", r"Réaliser avec des bascules JK la séquence $Q_2Q_1Q_0=111,100,101,110,011,001,000$ (puis retour à $111$) : tableau, $J_i$ et $K_i$ simplifiés avec tableaux de Karnaugh, sans OU exclusif.",
          r"$J_0=1$, $K_0=Q_2+\overline{Q_1}$, $J_1=Q_0Q_2+\overline{Q_0}\,\overline{Q_2}$, $K_1=Q_0$, $J_2=\overline{Q_0}$, $K_2=Q_1\overline{Q_0}$ (états inutilisé : $010$ en Φ).", src=B3 + ", ex. 2 (6 points)", duree=25),
        o("sx3", r"Réaliser la même séquence avec des bascules D.",
          r"$D_2=Q_2Q_0+\overline{Q_1}\,\overline{Q_0}$ ; $D_1=Q_1\overline{Q_0}+\overline{Q_2}\,\overline{Q_0}+Q_2\overline{Q_1}Q_0$ ; $D_0=\overline{Q_0}+\overline{Q_2}Q_1$.", src=B3 + ", ex. 3 (4 points)", duree=18),
        o("sx4", r"Que réalise un montage de $4$ bascules JK ($J=K=1$) où chaque horloge est la sortie $\overline Q$ de la précédente ? Câbler un décompteur asynchrone modulo $15$.",
          r"Avec l'horloge prise sur $\overline Q$ et un déclenchement sur front descendant, c'est un décompteur asynchrone modulo $16$. Pour le modulo $15$ : détecter l'état $1111$ (NON-ET sur $Q_3..Q_0$) et remettre $Q_0$ à $0$ pour revenir à $1110$.", src=B3 + ", ex. 4 (3 points)", duree=12),
    ]},
    {"n": 10, "titre": "Examen + 20 %", "notions": ["synchrone", "registre", "modulo"], "examen": True, "exos": [
        v("sy1", r"Séquence $0,1,\dots,7$ (compteur binaire 3 bits) avec des bascules T : $T_0=1$, $T_1=Q_0$, $T_2=Q_1Q_0$. Contrôle (avec $D_i=Q_i\oplus T_i$) ?", "seqD(3, [0,1,2,3,4,5,6,7], [Xor(Q2, Q1 & Q0), Xor(Q1, Q0), ~Q0])", "1",
          r"Une bascule T bascule quand $T=1$ : $Q_0$ toujours, $Q_1$ quand $Q_0=1$, $Q_2$ quand $Q_1Q_0=1$.", duree=12),
        v("sy2", r"Séquence $0,2,4,6$ (3 bits) avec des bascules D : $D_2=Q_2\oplus Q_1$, $D_1=\overline{Q_1}$, $D_0=0$. Contrôle ?", "seqD(3, [0,2,4,6], [Xor(Q2, Q1), ~Q1, 0])", "1",
          r"$000\to010$, $010\to100$, $100\to110$, $110\to000$ : $D_2=Q_2\oplus Q_1$, $D_1=\overline{Q_1}$, $D_0=0$ (solutions évidentes : $D_1$ et $D_0$).", duree=10),
        v("sy3", r"Compteur modulo $5$ ($0,\dots,4$) avec des bascules JK : $J_2=Q_1Q_0$, $K_2=1$, $J_1=Q_0$, $K_1=Q_0$, $J_0=\overline{Q_2}$, $K_0=1$ (états $5,6,7$ en Φ). Contrôle ?", "seqJK(3, [0,1,2,3,4], [Q1&Q0, 1, Q0, Q0, ~Q2, 1])", "1",
          r"Trois bascules ($2^2=4<5\le8$). Table d'excitation puis Karnaugh avec Φ pour $5,6,7$.", duree=20),
        o("sy4", r"Un compteur asynchrone modulo $10$ alimente un afficheur : expliquer pourquoi l'état $10$ peut produire un parasite d'affichage.",
          r"Dès que le compteur atteint $1010$, la remise à zéro est déclenchée avec un léger retard (délai de propagation de la porte NON-ET). Pendant ce court instant l'état $10$ existe et peut être décodé par un afficheur, provoquant un parasite. Un compteur synchrone n'a pas ce défaut (pas d'état transitoire interdit).", duree=6),
    ]},
]


def _v(enonce, calc, ans, sol):
    return {"enonce": enonce, "calc": calc, "ans": ans, "sol": sol}


VARIANTS = {
    "s11": [_v(r"Bascule D : $D=0$, $Q=1$ avant le front actif. Valeur de $Q$ après ?", "0", "0", r"$Q^+=D=0$.")],
    "s12": [_v(r"Bascule T : $T=0$, $Q=1$ avant le front actif. Valeur de $Q$ après ?", "(0+1)%2", "1", r"$Q^+=T\oplus Q=1$ : état conservé.")],
    "s13": [_v(r"Bascule JK : $J=0$, $K=1$, $Q=1$ avant le front. Valeur de $Q$ après ?", "0", "0", r"$J=0,K=1$ met la bascule à $0$.")],
    "s22": [_v(r"Bascule T, $Q=0$ au départ, $T=1$ à chaque front. Valeur de $Q$ après $8$ fronts ?", "8%2", "0", r"Nombre pair de basculements : $Q=0$.")],
    "s31": [_v(r"Compteur asynchrone à $5$ bascules JK ($J=K=1$). Modulo ?", "2**5", "32", r"$2^5=32$.")],
    "s32": [_v(r"Horloge à $3{,}2$ kHz sur $5$ bascules en cascade : fréquence de $Q_4$ (en Hz) ?", "3200/2**5", "100", r"$3200/32=100$ Hz.")],
    "s33": [_v(r"Combien de bascules pour un compteur modulo $50$ ?", "6", "6", r"$2^5=32<50\le64=2^6$.")],
    "s43": [_v(r"Modulo $6$ : état de détection (décimal) ?", "6", "6", r"$6=110$ : $Q_2$ et $Q_1$.")],
    "s81": [_v(r"Registre à décalage à gauche de $4$ bits à $0011$, entrée série $0$. Contenu (décimal) après un coup d'horloge ?", "bits('0110')", "6", r"$0011\to0110=6$ ($3\times2$).")],
    "s82": [_v(r"Registre à décalage à droite de $4$ bits à $1000$, entrée série $0$. Contenu (décimal) après un coup d'horloge ?", "bits('0100')", "4", r"$1000\to0100=4$ ($8/2$).")],
}
for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["id"] in VARIANTS:
            _e["variants"] = VARIANTS[_e["id"]]


EXTRA_PARTS = []

QUIZ = [
    {"notion": "bascules", "type": "qcm", "q": r"Bascule JK avec $J=K=1$ : l'état après le front actif est :", "choix": [r"$\overline Q$", r"$Q$", r"$0$", r"$1$"], "bonne": 0},
    {"notion": "bascules", "type": "vf", "q": r"Pour une bascule D, $Q^+=D$.", "bonne": True},
    {"notion": "chrono", "type": "qcm", "q": r"Une entrée $D$ qui change entre deux fronts actifs :", "choix": [r"n'a d'effet qu'au front suivant", r"change $Q$ immédiatement", r"est ignorée définitivement", r"bloque l'horloge"], "bonne": 0},
    {"notion": "chrono", "type": "vf", "q": r"Une bascule sur front échantillonne son entrée à l'instant du front.", "bonne": True},
    {"notion": "asynchrone", "type": "qcm", "q": r"Chaque bascule d'un compteur asynchrone divise la fréquence par :", "choix": [r"$2$", r"$4$", r"$10$", r"$1$"], "bonne": 0},
    {"notion": "asynchrone", "type": "vf", "q": r"Dans un compteur asynchrone, toutes les bascules reçoivent la même horloge.", "bonne": False},
    {"notion": "modulo", "type": "qcm", "q": r"Pour un modulo $10$ avec remise à zéro, on détecte l'état :", "choix": [r"$1010$", r"$1001$", r"$1111$", r"$0101$"], "bonne": 0},
    {"notion": "modulo", "type": "vf", "q": r"Dans un compteur modulo $10$ à remise à zéro, l'état $10$ existe un instant très bref.", "bonne": True},
    {"notion": "excitation", "type": "qcm", "q": r"Transition $1\to0$ d'une bascule JK :", "choix": [r"$K=1$, $J$ indifférent", r"$J=1$, $K$ indifférent", r"$J=K=0$", r"$J=K=1$ seulement"], "bonne": 0},
    {"notion": "excitation", "type": "vf", "q": r"Pour une bascule D, l'entrée vaut toujours l'état suivant souhaité.", "bonne": True},
    {"notion": "synchrone", "type": "qcm", "q": r"Dans la synthèse d'un compteur synchrone, un état non utilisé donne :", "choix": [r"des indifférents (Φ)", r"des zéros", r"des uns", r"une erreur"], "bonne": 0},
    {"notion": "synchrone", "type": "vf", "q": r"Dans un compteur synchrone toutes les bascules ont la même horloge.", "bonne": True},
    {"notion": "registre", "type": "qcm", "q": r"Un décalage à gauche d'un rang d'un mot non signé (entrée série $0$) :", "choix": [r"multiplie par $2$", r"divise par $2$", r"ajoute $1$", r"change le signe"], "bonne": 0},
    {"notion": "registre", "type": "vf", "q": r"Dans un registre à décalage à bascules D, $Q_i^+=Q_{i-1}$.", "bonne": True},
]

_B = r"D : $Q^+=D$ · T : $Q^+=T\oplus Q$ · JK : $Q^+=J\overline Q+\overline KQ$"
_AS = r"modulo $2^n$ · $f/2^n$ · $\lceil\log_2N\rceil$ bascules"
_EX = r"JK : $0\to1$: $J=1$ · $1\to0$: $K=1$ · $0\to0$: $K=\Phi$... · D : $D=Q^+$"
_SY = r"table présent/suivant · Karnaugh avec Φ pour les états inutilisés · " + _EX
_RG = r"$Q_i^+=Q_{i-1}$ · décalage à gauche $=\times2$"

FORMULES = {
    "s11": _B, "s12": _B, "s13": _B, "s14": _B, "s15": _B, "s16": _B, "s17": _B,
    "s21": _B, "s22": _B, "s23": _B, "s24": r"bascule sur front : l'entrée n'est lue qu'au front", "s25": _B, "s26": r"verrou : sensible au niveau · bascule : sensible au front",
    "s31": _AS, "s32": _AS, "s33": _AS, "s34": _AS, "s35": _AS, "s36": _AS + r" · $H_i=Q_{i-1}$ ou $\overline{Q_{i-1}}$",
    "s41": _AS + r" · détecter $N$", "s42": r"détecter le premier état avec ces bits à $1$", "s43": _AS, "s44": _AS, "s45": r"décompteur : $0000\to1111$ · remise à $0$ de $Q_0$ : $1111\to1110$", "s46": _AS + r" · NON-ET de détection",
    "s51": _EX, "s52": _EX, "s53": _EX, "s54": _EX, "s55": r"$T=Q\oplus Q^+$", "s56": _EX,
    "s61": _SY, "s62": _SY, "s63": _SY, "s64": _SY, "s65": _AS, "s66": _SY,
    "s71": _SY, "s72": _SY, "s73": _EX, "s74": _SY, "s75": _EX, "s76": _EX,
    "s81": _RG, "s82": _RG + r" · décalage à droite $=/2$", "s83": r"1 bit par coup d'horloge", "s84": _RG, "s85": _RG,
    "sx1": _B, "sx2": _SY, "sx3": _SY, "sx4": _AS + r" · décompteur : $H_i=\overline{Q_{i-1}}$",
    "sy1": r"T : $Q^+=T\oplus Q$ · " + _AS, "sy2": _SY, "sy3": _SY, "sy4": _AS + r" · temps de propagation",
}
