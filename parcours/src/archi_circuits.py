"""Level path: S1 computer architecture, combinational circuits (adders, adder-subtractor, comparators, multiplexers, decoders, TD6 problem).

Calibrated on the Moodle TDs « TD 6 - Problèmes de logique combinatoire » and « TD 7 - Quelques circuits combinatoires »
(Archi S1 - Promo 2030) and on the B2 exam. Expressions are checked by `build.py` (`eqv`, `cover`); numeric examples
use `bits`. Minimal forms of the vending machine come from sympy `SOPform`.
"""

SUBJECT = {
    "id": "archi-s1-circuits",
    "ordre": 420,
    "matiere": "archi",
    "semestre": "S1",
    "ecue": "Circuits combinatoires",
    "titre": "Circuits combinatoires : additionneurs, comparateurs, décodeurs",
    "chapitres_moodle": ["06_Algèbre de Boole [2526_I_INF_FISE_S01_PR_BOOL]", "08_Travaux Dirigés", "09_Entraînement"],
    "td": "TD 6 et 7 d'architecture (Moodle Archi S1)",
    "examens": ["Examen B2 d'architecture des ordinateurs"],
}

NOTIONS = [
    {"id": "additionneur", "titre": "Demi-additionneur et additionneur complet",
     "formule": r"demi-additionneur : $S=A\oplus B$, $C=AB$ · additionneur complet : $S_i=A_i\oplus B_i\oplus C_{i-1}$, $C_i=A_iB_i+C_{i-1}(A_i\oplus B_i)=A_iB_i+A_iC_{i-1}+B_iC_{i-1}$",
     "exemple": r"$1+1+1=11_2$ : $S=1$, $C=1$",
     "cours": r"L'additionneur complet additionne deux bits et la retenue entrante. La somme vaut $1$ si le nombre d'entrées à $1$ est impair. La retenue sortante vaut $1$ si au moins deux entrées valent $1$ (majorité)."},
    {"id": "cascade", "titre": "Additionneur n bits en cascade",
     "formule": r"additionneur 4 bits = 4 additionneurs complets, $C_i$ de l'étage $i$ vers l'étage $i+1$ · $S=(A+B+C_{-1})\bmod2^4$ · $C_3=1\iff A+B+C_{-1}\ge16$",
     "exemple": r"$1011+0110$ : $S=0001$, $C_3=1$ ($11+6=17$)",
     "cours": r"La retenue se propage d'un étage au suivant (retenue en série), ce qui rend le circuit lent pour beaucoup de bits. $C_3$ est la retenue sortante : dépassement en non signé."},
    {"id": "addsub", "titre": "Additionneur-soustracteur",
     "formule": r"$X-Y=X+\overline Y+1$ · $Q=X+(Y\oplus\text{Sub}\ldots)$ : chaque bit de $Y$ passe par un OU exclusif avec $\text{Add/Sub}$ · retenue d'entrée $=\text{Add/Sub}$ · $A\oplus0=A$, $A\oplus1=\overline A$",
     "exemple": r"$5-3$ sur 4 bits : $Y=0011\to\overline Y=1100$, $+1$ : $0101+1100+1=1\,0010$, $Q=0010$",
     "cours": r"Le OU exclusif joue le rôle d'un inverseur commandé : transparent si $\text{Sub}=0$, inverseur si $\text{Sub}=1$. Ajouter $1$ (retenue d'entrée) complète le complément à deux."},
    {"id": "comparateur", "titre": "Comparateurs",
     "formule": r"1 bit avec validation $G$ : $H=G\,A\,\overline B$ · $L=G\,\overline A\,B$ · $E=G\,\overline{A\oplus B}$ · 4 bits : $H=H_3+E_3H_2+E_3E_2H_1+E_3E_2E_1H_0$, $E=E_3E_2E_1E_0$",
     "exemple": r"$A=1,B=0,G=1$ : $H=1,E=0,L=0$",
     "cours": r"On compare d'abord les bits de poids fort ; les étages suivants ne comptent que si les bits de poids fort sont égaux. Les trois sorties $H,E,L$ ne valent jamais $1$ ensemble."},
    {"id": "mux", "titre": "Multiplexeurs et démultiplexeurs",
     "formule": r"mux 2 vers 1 : $S=\overline{\text{Sel}}\,I_0+\text{Sel}\,I_1$ · mux 4 vers 1 : $S=\overline{S_1}\,\overline{S_0}I_0+\overline{S_1}S_0I_1+S_1\overline{S_0}I_2+S_1S_0I_3$ · $2^n$ entrées de données, $n$ entrées de sélection",
     "exemple": r"$\text{Sel}=1$ : $S=I_1$",
     "cours": r"Un multiplexeur choisit une entrée parmi $2^n$ grâce à $n$ bits de sélection. Il permet de réaliser n'importe quelle fonction de $n+1$ variables en câblant les entrées de données à $0$, $1$ ou la dernière variable."},
    {"id": "decodeur", "titre": "Décodeurs",
     "formule": r"décodeur $n\to2^n$ : la sortie $i$ vaut $1$ si l'entrée vaut $i$ en binaire (une seule sortie active) · 2 entrées $A_1A_0$ : $Y_0=\overline{A_1}\,\overline{A_0}$, $Y_1=\overline{A_1}A_0$, $Y_2=A_1\overline{A_0}$, $Y_3=A_1A_0$",
     "exemple": r"entrée $10_2$ : seule la sortie $Y_2$ vaut $1$",
     "cours": r"Chaque sortie est un minterm de l'entrée. Avec une entrée de validation (enable), toutes les sorties valent $0$ quand elle est inactive. On peut réaliser une fonction en faisant le OU des sorties qui correspondent à ses lignes à $1$."},
    {"id": "distributeur", "titre": "Problème du distributeur",
     "formule": r"entrées $A$ (café), $B$ (thé), $C$ (lait), $D$ (jeton) · sorties $W$ (café), $X$ (thé), $Y$ (lait), $Z$ (jeton rendu) · sans jeton ($D=0$) : $W=X=Y=0$, $Z=\Phi$",
     "exemple": r"café seul avec jeton : $A\overline B\overline CD$ donne $W=1$, $Z=0$",
     "cours": r"Une fausse manœuvre (deux boissons demandées, ou aucun bouton) rend le jeton. Le lait seul est gratuit : lait servi et jeton rendu. Remplir une table de vérité de 16 lignes puis un tableau de Karnaugh par sortie."},
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


TD7 = "TD 7 d'architecture (circuits combinatoires)"
TD6 = "TD 6 d'architecture (problèmes de logique combinatoire)"

LEVELS = [
    {"n": 1, "titre": "Demi-additionneur et additionneur complet", "notions": ["additionneur"], "exos": [
        v("c11", r"Demi-additionneur : $A=1$, $B=1$. Valeur de la somme $S$ ?", "(1+1)%2", "0", r"$S=A\oplus B=0$ et $C=AB=1$ ($1+1=10_2$).", duree=1),
        v("c12", r"Additionneur complet : $A_i=1$, $B_i=1$, $C_{i-1}=1$. Valeur de $S_i$ ?", "(1+1+1)%2", "1", r"$1+1+1=11_2$ : $S_i=1$ et $C_i=1$.", src=TD7 + ", ex. 1", duree=1),
        v("c13", r"Additionneur complet : $A_i=1$, $B_i=0$, $C_{i-1}=1$. Valeur de $C_i$ ?", "(1+0+1)//2", "1", r"$1+0+1=10_2$ : $S_i=0$ et $C_i=1$.", src=TD7 + ", ex. 1", duree=1),
        v("c14", r"Vérifier que $S_i=A_i\oplus B_i\oplus C_{i-1}$ est à $1$ pour un nombre impair d'entrées à $1$ (contrôle : l'expression est vraie pour $100$) ?", "eqv(Xor(Xor(A, B), C), (A&~B&~C)|(~A&B&~C)|(~A&~B&C)|(A&B&C))", "1",
          r"Lignes à $1$ de $S_i$ : $001,010,100,111$ (nombre impair de $1$).", src=TD7 + ", ex. 1 q. 2", duree=3),
        v("c15", r"Retenue sortante : montrer que $C_i=A_iB_i+C_{i-1}(A_i\oplus B_i)$ est égale à $A_iB_i+A_iC_{i-1}+B_iC_{i-1}$. Contrôle ?", "eqv((A&B)|(C&Xor(A,B)), (A&B)|(A&C)|(B&C))", "1",
          r"$C(A\overline B+\overline AB)=AC\overline B+\overline ABC$ ; avec $AB$ on retrouve $AB+AC+BC$ (terme consensus compris).", src=TD7 + ", ex. 1 q. 3", duree=4),
        o("c16", r"Donner la table de vérité de l'additionneur complet ($A_i,B_i,C_{i-1}\to S_i,C_i$) puis le schéma en portes.",
          r"| $A_i$ | $B_i$ | $C_{i-1}$ | $S_i$ | $C_i$ |" "\n|---|---|---|---|---|\n"
          r"| 0 | 0 | 0 | 0 | 0 |" "\n" r"| 0 | 0 | 1 | 1 | 0 |" "\n" r"| 0 | 1 | 0 | 1 | 0 |" "\n" r"| 0 | 1 | 1 | 0 | 1 |" "\n"
          r"| 1 | 0 | 0 | 1 | 0 |" "\n" r"| 1 | 0 | 1 | 0 | 1 |" "\n" r"| 1 | 1 | 0 | 0 | 1 |" "\n" r"| 1 | 1 | 1 | 1 | 1 |" "\n\n"
          r"Schéma : deux portes OU exclusif en série pour $S_i$ ($P=A_i\oplus B_i$, $S_i=P\oplus C_{i-1}$), deux portes ET ($A_iB_i$ et $PC_{i-1}$) et une porte OU pour $C_i$.", src=TD7 + ", ex. 1 q. 1 et 4", duree=8),
    ]},
    {"n": 2, "titre": "Additionneur 4 bits en cascade", "notions": ["cascade", "additionneur"], "exos": [
        v("c21", r"Additionneur 4 bits : $A=1011$, $B=0110$, $C_{-1}=0$. Valeur de $S$ (décimal) ?", "(11+6)%16", "bits('0001')", r"$11+6=17=1\,0001_2$ : $S=0001$ et $C_3=1$.", src=TD7 + ", ex. 1 q. 5", duree=3),
        v("c22", r"Mêmes opérandes : valeur de la retenue sortante $C_3$ ?", "(11+6)//16", "1", r"$17\ge16$ : $C_3=1$.", duree=2),
        v("c23", r"$A=0101$, $B=0011$, $C_{-1}=1$. Valeur de $S$ (décimal) ?", "(5+3+1)%16", "bits('1001')", r"$5+3+1=9=1001_2$, pas de retenue sortante.", duree=3),
        v("c24", r"Combien d'additionneurs complets pour un additionneur $32$ bits ?", "32", "32", r"Un par bit : $32$.", duree=1),
        v("c25", r"Combien d'additionneurs complets pour additionner deux mots de $8$ bits et une retenue d'entrée ?", "8", "8", r"Un par bit, la retenue d'entrée va dans l'étage $0$ : $8$.", duree=1),
        o("c26", r"Pourquoi une cascade d'additionneurs complets est-elle lente pour beaucoup de bits ?",
          r"Chaque étage doit attendre la retenue de l'étage précédent. Le temps de calcul croît linéairement avec le nombre de bits (propagation de la retenue en série). Les additionneurs rapides calculent les retenues en parallèle (anticipation de retenue).", duree=4),
    ]},
    {"n": 3, "titre": "Additionneur-soustracteur", "notions": ["addsub", "cascade"], "exos": [
        v("c31", r"Sur $4$ bits, calculer $5-3$ avec $X+\overline Y+1$. Valeur de $Q$ (décimal) ?", "(5+(15-3)+1)%16", "2", r"$\overline{0011}=1100$ ; $0101+1100+1=1\,0010$ : $Q=0010=2$ (retenue ignorée).", src=TD7 + ", ex. 1 q. 8", duree=3),
        v("c32", r"Sur $4$ bits, $X=0011$, $Y=0101$ avec $\text{Add/Sub}=1$. Valeur de $Q$ (décimal, signé) ?", "(3+(15-5)+1)%16-16", "-2", r"$0011+1010+1=1110$ soit $-2$ en complément à deux.", src=TD7 + ", ex. 1 q. 8", duree=3),
        v("c33", r"Circuit à deux entrées $N$ et $D$ : $G=D$ si $N=0$ et $G=\overline D$ si $N=1$. Contrôle : $G=N\oplus D$ ?", "eqv(Xor(A, B), (~A&B)|(A&~B))", "1", r"C'est la table du OU exclusif : transparent quand $N=0$, inverseur quand $N=1$.", src=TD7 + ", ex. 1 q. 6", duree=2),
        v("c34", r"Combien de portes OU exclusif pour inverser conditionnellement un mot de $4$ bits (circuit de la q. 7) ?", "4", "4", r"Une porte par bit, la commande d'inversion $I$ est reliée aux quatre portes.", src=TD7 + ", ex. 1 q. 7", duree=2),
        v("c35", r"Quelle valeur faut-il appliquer à la retenue d'entrée de l'additionneur 4 bits pour une soustraction ?", "1", "1", r"$X-Y=X+\overline Y+1$ : la retenue d'entrée vaut $\text{Add/Sub}=1$.", src=TD7 + ", ex. 1 q. 8", duree=2),
        o("c36", r"Dessiner l'additionneur-soustracteur 4 bits avec un additionneur 4 bits et des portes OU exclusif.",
          r"Entrées $X_3..X_0$ directement sur l'entrée $A$ de l'additionneur. Chaque $Y_i$ passe dans une porte OU exclusif dont l'autre entrée est $\text{Add/Sub}$ ; sorties vers l'entrée $B$. $\text{Add/Sub}$ est aussi reliée à la retenue d'entrée $C_{-1}$." "\n\n"
          r"$\text{Add/Sub}=0$ : $Q=X+Y$. $\text{Add/Sub}=1$ : $Q=X+\overline Y+1=X-Y$.", src=TD7 + ", ex. 1 q. 8", duree=6),
    ]},
    {"n": 4, "titre": "Comparateurs", "notions": ["comparateur", "additionneur"], "exos": [
        v("c41", r"Comparateur 1 bit, $G=1$, $A=1$, $B=0$. Valeur de $H$ ($A>B$) ?", "1*1*(1-0)", "1", r"$H=G\,A\,\overline B=1$.", src=TD7 + ", ex. 2", duree=1),
        v("c42", r"Comparateur 1 bit, $G=1$, $A=0$, $B=0$. Valeur de $E$ ?", "1*(1-(0+0)%2)", "1", r"$E=G\,\overline{A\oplus B}=1$ car $A=B$.", src=TD7 + ", ex. 2", duree=1),
        v("c43", r"Comparateur 1 bit : montrer que $E=G.\overline{A\oplus B}$ vaut $G(AB+\overline A\,\overline B)$. Contrôle ?", "eqv(C & ~Xor(A, B), C & ((A&B)|(~A&~B)))", "1", r"Le complément du OU exclusif est l'égalité : $AB+\overline A\,\overline B$.", src=TD7 + ", ex. 2 q. 2", duree=3),
        v("c44", r"Comparateur 4 bits : $A=0110$, $B=0101$. Quel étage décide (indice du bit de poids le plus fort où $A\neq B$) ?", "1", "1", r"Bits $3$ et $2$ égaux ($0$ et $1$) ; bit $1$ : $A_1=1>B_1=0$ : $H=1$ décidé à l'étage $1$.", src=TD7 + ", ex. 2 q. 4", duree=3),
        v("c45", r"Comparateur 4 bits : $H=H_3+E_3H_2+E_3E_2H_1+E_3E_2E_1H_0$. Combien de termes contient cette somme ?", "4", "4", r"$H_3$, $E_3H_2$, $E_3E_2H_1$, $E_3E_2E_1H_0$ : $4$ termes.", src=TD7 + ", ex. 2 q. 4", duree=2),
        o("c46", r"Donner la table de vérité du comparateur 1 bit (entrées $G,A,B$, sorties $H,E,L$) et les expressions de $H,E,L$.",
          r"| $G$ | $A$ | $B$ | $H$ | $E$ | $L$ |" "\n|---|---|---|---|---|---|\n"
          r"| 0 | x | x | 0 | 0 | 0 |" "\n" r"| 1 | 0 | 0 | 0 | 1 | 0 |" "\n" r"| 1 | 0 | 1 | 0 | 0 | 1 |" "\n" r"| 1 | 1 | 0 | 1 | 0 | 0 |" "\n" r"| 1 | 1 | 1 | 0 | 1 | 0 |" "\n\n"
          r"$H=G\,A\,\overline B$, $L=G\,\overline A\,B$, $E=G\,\overline{A\oplus B}$.", src=TD7 + ", ex. 2 q. 1-2", duree=6),
    ]},
    {"n": 5, "titre": "Multiplexeurs et décodeurs", "notions": ["mux", "decodeur"], "exos": [
        v("c51", r"Multiplexeur 2 vers 1 avec $\text{Sel}=1$, $I_0=0$, $I_1=1$. Valeur de $S$ ?", "1", "1", r"$\text{Sel}=1$ choisit $I_1=1$.", duree=1),
        v("c52", r"Combien d'entrées de sélection pour un multiplexeur $8$ vers $1$ ?", "3", "3", r"$2^3=8$ : $3$ bits de sélection.", duree=1),
        v("c53", r"Décodeur $3\to8$ : entrée $101_2$. Numéro de la sortie active ?", "bits('101')", "5", r"La sortie $Y_5$ est active.", duree=1),
        v("c54", r"Combien de sorties pour un décodeur à $4$ entrées ?", "2**4", "16", r"$2^4=16$ sorties.", duree=1),
        v("c55", r"Multiplexeur 4 vers 1 : $S_1S_0=10$, $I_2=1$. Valeur de $S$ ?", "1", "1", r"$S_1S_0=10$ sélectionne $I_2$.", duree=2),
        v("c56", r"Expression du multiplexeur 2 vers 1 : contrôle que $S=\overline{\text{Sel}}\,I_0+\text{Sel}\,I_1$ est égale à $(\text{Sel}+I_0)(\overline{\text{Sel}}+I_1)$ ?", "eqv((~C&A)|(C&B), (C|A)&(~C|B))", "1",
          r"Avec $C$=Sel, $A=I_0$, $B=I_1$ : les deux formes valent $I_1$ si $\text{Sel}=1$ et $I_0$ sinon (le terme $I_0I_1$ est consensus).", duree=4),
        o("c57", r"Réaliser $f(A,B,C)=AB+\overline AC$ avec un multiplexeur $4$ vers $1$ (sélection $A,B$).",
          r"Pour chaque valeur de $AB$ exprimer $f$ en fonction de $C$ : $AB=00\to C$ ; $01\to C$ ; $10\to0$ ; $11\to1$." "\n\n"
          r"Entrées de données : $I_0=C$, $I_1=C$, $I_2=0$, $I_3=1$ ; entrées de sélection $S_1=A$, $S_0=B$.", duree=6),
    ]},
    {"n": 6, "titre": "Problème du distributeur", "notions": ["distributeur", "mux"], "exos": [
        v("c61", r"Distributeur : café seul avec jeton ($A=1$, $B=0$, $C=0$, $D=1$). Expression simplifiée proposée de $W$ : $W=A\,\overline B\,D$. Contrôle ($ABCD$, $A$ poids fort) ?", "cover(A & ~B & D, 'ABCD', [9, 11])", "1",
          r"Café servi pour $A\overline BD$ avec ou sans lait : $1001$ et $1011$ ; le bouton lait ne change pas $W$.", src=TD6 + ", ex. 1", duree=4),
        v("c62", r"Même distributeur : thé servi $X=B\,\overline A\,D$. Contrôle ?", "cover(B & ~A & D, 'ABCD', [5, 7])", "1", r"Symétrique du café : $0101$ et $0111$.", src=TD6 + ", ex. 1", duree=4),
        v("c63", r"Lait servi : $Y=C\,D\,\overline{A\,B}$. Contrôle ($1$ pour $0011,0111,1011$) ?", "cover(C & D & ~(A & B), 'ABCD', [3, 7, 11])", "1",
          r"Lait servi dès qu'un jeton est présent et que $C=1$, sauf fausse manœuvre café + thé ($AB=1$). Cela couvre lait seul, café-lait et thé-lait.", src=TD6 + ", ex. 1", duree=5),
        v("c64", r"Jeton rendu : $Z=\overline{A\oplus B}$ (indifférent si $D=0$). Contrôle avec $Z=1$ pour $0001,0011,1101,1111$ ?", "cover(~Xor(A, B), 'ABCD', [1,3,13,15], [0,2,4,6,8,10,12,14])", "1",
          r"Jeton rendu si ni café ni thé (lait seul ou rien) ou si café et thé ensemble : $A=B$. D'où $Z=\overline{A\oplus B}=AB+\overline A\,\overline B$.", src=TD6 + ", ex. 1", duree=6),
        v("c65", r"Combien de lignes dans la table de vérité du distributeur ?", "2**4", "16", r"$4$ entrées : $2^4=16$ lignes.", src=TD6 + ", ex. 1 q. 1", duree=1),
        o("c66", r"Donner la table de vérité complète du distributeur ($A$ café, $B$ thé, $C$ lait, $D$ jeton ; $W,X,Y,Z$).",
          r"Pour $D=0$ : $W=X=Y=0$, $Z=\Phi$ (8 lignes)." "\n\n"
          r"Pour $D=1$ ($ABC$) : $000\to Z=1$ ; $001\to Y=1,Z=1$ ; $010\to X=1$ ; $011\to X=1,Y=1$ ; $100\to W=1$ ; $101\to W=1,Y=1$ ; $110\to Z=1$ ; $111\to Z=1$ (les sorties non citées valent $0$).", src=TD6 + ", ex. 1 q. 1", duree=8),
    ]},
    {"n": 7, "titre": "Niveau examen : circuits et logique", "notions": ["additionneur", "addsub", "comparateur", "distributeur"], "examen": True, "exos": [
        o("cx1", r"Additionneur complet : table de vérité, $S_i$ simplifiée par la méthode algébrique, $C_i$ par un tableau de Karnaugh, schéma de câblage.",
          r"$S_i=A_i\oplus B_i\oplus C_{i-1}$ (à $1$ pour un nombre impair d'entrées à $1$)." "\n\n"
          r"Karnaugh de $C_i$ (lignes $C_{i-1}$, colonnes $A_iB_i$) : trois groupes de $2$ cases : $C_i=A_iB_i+A_iC_{i-1}+B_iC_{i-1}$." "\n\n"
          r"Schéma : voir le niveau 1.", src=TD7 + ", ex. 1 q. 1-4", duree=14),
        o("cx2", r"Additionneur-soustracteur 4 bits : schéma à partir d'un additionneur 4 bits, 4 portes OU exclusif et le signal $\text{Add/Sub}$. Calculer $0111-0100$.",
          r"Schéma au niveau 3. $0111-0100$ : $Y=0100\to\overline Y=1011$ ; $0111+1011+1=1\,0011$, $Q=0011=3$ (retenue ignorée).", src=TD7 + ", ex. 1 q. 8", duree=12),
        o("cx3", r"Comparateur 4 bits à partir de comparateurs 1 bit et de quelques portes : donner les expressions de $H$, $E$, $L$.",
          r"$H=H_3+E_3H_2+E_3E_2H_1+E_3E_2E_1H_0$ ; $E=E_3E_2E_1E_0$ ; $L=L_3+E_3L_2+E_3E_2L_1+E_3E_2E_1L_0$. La validation $G$ est reliée à tous les étages." "\n\n"
          r"Contrôle : si $A=B$ alors $E=1$ et $H=L=0$ (aucun étage ne détecte $A>B$ ni $A < B$).", src=TD7 + ", ex. 2 q. 4", duree=12),
        o("cx4", r"Distributeur de boissons chaudes : donner les expressions simplifiées de $W,X,Y,Z$ par Karnaugh.",
          r"$W=A\,\overline B\,D$, $X=\overline A\,B\,D$, $Y=C\,D\,\overline{AB}=CD\overline A+CD\overline B$, $Z=\overline{A\oplus B}=AB+\overline A\,\overline B$ (avec les Φ de $D=0$).", src=TD6 + ", ex. 1 q. 2", duree=14),
    ]},
    {"n": 8, "titre": "Examen + 20 %", "notions": ["cascade", "mux", "decodeur", "comparateur"], "examen": True, "exos": [
        v("cy1", r"Additionneur 8 bits : $A=1111\,0000$, $B=0001\,0000$, $C_{-1}=0$. Valeur de $S$ (décimal non signé) ?", "(240+16)%256", "0", r"$240+16=256$ : $S=0000\,0000$ et $C_7=1$.", duree=4),
        v("cy2", r"Même addition : valeur de la retenue sortante $C_7$ ?", "(240+16)//256", "1", r"$256\ge256$ : $C_7=1$ (dépassement en non signé).", duree=2),
        v("cy3", r"Additionneur-soustracteur 4 bits : $X=0010$, $Y=0101$, $\text{Add/Sub}=1$. Valeur signée de $Q$ ?", "(2+(15-5)+1)%16-16", "-3", r"$0010+1010+1=1101=-3$.", duree=4),
        o("cy4", r"Réaliser $f(A,B,C)=A\oplus B\oplus C$ avec un multiplexeur $4$ vers $1$ (sélection $A,B$) puis avec un décodeur $3\to8$ et une porte OU.",
          r"Multiplexeur : $AB=00\to C$ ; $01\to\overline C$ ; $10\to\overline C$ ; $11\to C$ (entrées $I_0=C$, $I_1=\overline C$, $I_2=\overline C$, $I_3=C$)." "\n\n"
          r"Décodeur : $f=1$ pour $001,010,100,111$ : OU des sorties $Y_1,Y_2,Y_4,Y_7$.", duree=10),
        o("cy5", r"Concevoir un détecteur de majorité sur $3$ bits ($M=1$ si au moins deux entrées valent $1$). Comparer avec la retenue de l'additionneur complet.",
          r"$M=AB+AC+BC$ (tableau de Karnaugh : trois groupes de deux cases)." "\n\n"
          r"C'est exactement la retenue sortante de l'additionneur complet $C_i=A_iB_i+A_iC_{i-1}+B_iC_{i-1}$.", duree=8),
    ]},
]


def _v(enonce, calc, ans, sol):
    return {"enonce": enonce, "calc": calc, "ans": ans, "sol": sol}


VARIANTS = {
    "c21": [_v(r"Additionneur 4 bits : $A=0111$, $B=0101$, $C_{-1}=0$. Valeur de $S$ (décimal) ?", "(7+5)%16", "bits('1100')", r"$7+5=12=1100_2$.")],
    "c22": [_v(r"Mêmes opérandes que $1110+0110$ : valeur de $C_3$ ?", "(14+6)//16", "1", r"$14+6=20\ge16$ : $C_3=1$.")],
    "c23": [_v(r"$A=0110$, $B=0001$, $C_{-1}=1$. Valeur de $S$ ?", "(6+1+1)%16", "bits('1000')", r"$6+1+1=8$.")],
    "c31": [_v(r"Sur $4$ bits, calculer $7-2$ avec $X+\overline Y+1$ (décimal) ?", "(7+(15-2)+1)%16", "5", r"$0111+1101+1=1\,0101$ : $Q=0101=5$.")],
    "c41": [_v(r"Comparateur 1 bit, $G=1$, $A=0$, $B=1$. Valeur de $L$ ?", "1*(1-0)*1", "1", r"$L=G\,\overline AB=1$.")],
    "c53": [_v(r"Décodeur $3\to8$ : entrée $110_2$. Numéro de la sortie active ?", "bits('110')", "6", r"$Y_6$.")],
}
for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["id"] in VARIANTS:
            _e["variants"] = VARIANTS[_e["id"]]


EXTRA_PARTS = []

QUIZ = [
    {"notion": "additionneur", "type": "qcm", "q": r"La somme $S_i$ d'un additionneur complet vaut $1$ quand :", "choix": [r"un nombre impair d'entrées vaut $1$", r"au moins deux entrées valent $1$", r"toutes les entrées valent $1$", r"une seule entrée vaut $1$"], "bonne": 0},
    {"notion": "additionneur", "type": "vf", "q": r"La retenue sortante d'un additionneur complet est la fonction majorité de ses trois entrées.", "bonne": True},
    {"notion": "cascade", "type": "qcm", "q": r"Un additionneur $4$ bits se construit avec :", "choix": [r"$4$ additionneurs complets", r"$2$ additionneurs complets", r"$8$ demi-additionneurs seuls", r"$1$ seul additionneur complet"], "bonne": 0},
    {"notion": "cascade", "type": "vf", "q": r"La retenue sortante $C_3$ d'un additionneur $4$ bits indique un dépassement en non signé.", "bonne": True},
    {"notion": "addsub", "type": "qcm", "q": r"$X-Y$ se calcule comme :", "choix": [r"$X+\overline Y+1$", r"$X+\overline Y$", r"$\overline X+Y+1$", r"$X-\overline Y$"], "bonne": 0},
    {"notion": "addsub", "type": "vf", "q": r"Un OU exclusif avec une commande à $0$ laisse passer le bit inchangé.", "bonne": True},
    {"notion": "comparateur", "type": "qcm", "q": r"Dans un comparateur $4$ bits, on regarde d'abord :", "choix": [r"les bits de poids fort", r"les bits de poids faible", r"tous les bits en même temps sans priorité", r"la retenue"], "bonne": 0},
    {"notion": "comparateur", "type": "vf", "q": r"Les sorties $H$, $E$, $L$ d'un comparateur peuvent valoir $1$ en même temps.", "bonne": False},
    {"notion": "mux", "type": "qcm", "q": r"Un multiplexeur $16$ vers $1$ a combien d'entrées de sélection ?", "choix": [r"$4$", r"$16$", r"$8$", r"$2$"], "bonne": 0},
    {"notion": "mux", "type": "vf", "q": r"Un multiplexeur $4$ vers $1$ peut réaliser n'importe quelle fonction de $3$ variables.", "bonne": True},
    {"notion": "decodeur", "type": "qcm", "q": r"Dans un décodeur $n\to2^n$, combien de sorties sont actives à la fois ?", "choix": [r"une seule", r"toutes", r"$n$", r"aucune"], "bonne": 0},
    {"notion": "decodeur", "type": "vf", "q": r"Chaque sortie d'un décodeur est un minterm de ses entrées.", "bonne": True},
    {"notion": "distributeur", "type": "qcm", "q": r"Dans le distributeur, une fausse manœuvre (café et thé ensemble) provoque :", "choix": [r"la restitution du jeton et aucune boisson", r"du café seulement", r"du thé seulement", r"du café et du thé"], "bonne": 0},
    {"notion": "distributeur", "type": "vf", "q": r"Quand aucun jeton n'est introduit, la sortie $Z$ (jeton rendu) est un indifférent.", "bonne": True},
]

_FA = r"$S_i=A_i\oplus B_i\oplus C_{i-1}$ · $C_i=A_iB_i+A_iC_{i-1}+B_iC_{i-1}$"
_AS = r"$X-Y=X+\overline Y+1$ · $A\oplus1=\overline A$"
_CMP = r"$H=G\,A\overline B$, $L=G\,\overline AB$, $E=G\,\overline{A\oplus B}$ · $H=H_3+E_3H_2+E_3E_2H_1+E_3E_2E_1H_0$"
_MUX = r"mux 2 vers 1 : $S=\overline{\text{Sel}}I_0+\text{Sel}\,I_1$ · décodeur : une sortie par minterm"
_DIS = r"$W=A\overline BD$ · $X=\overline ABD$ · $Y=CD\overline{AB}$ · $Z=\overline{A\oplus B}$"

FORMULES = {
    "c11": r"$S=A\oplus B$ · $C=AB$", "c12": _FA, "c13": _FA, "c14": _FA + r" · $\oplus$ : nombre impair de $1$", "c15": _FA, "c16": _FA,
    "c21": _FA + r" · $S=(A+B+C_{-1})\bmod16$", "c22": r"$C_3=1\iff A+B+C_{-1}\ge16$", "c23": r"$S=(A+B+C_{-1})\bmod16$", "c24": r"1 additionneur complet par bit", "c25": r"1 additionneur complet par bit", "c26": r"propagation de la retenue en série",
    "c31": _AS, "c32": _AS + r" · complément à deux", "c33": r"$A\oplus B=A\overline B+\overline AB$", "c34": r"1 porte $\oplus$ par bit", "c35": _AS, "c36": _AS,
    "c41": _CMP, "c42": _CMP, "c43": _CMP, "c44": _CMP, "c45": _CMP, "c46": _CMP,
    "c51": _MUX, "c52": r"$2^n$ entrées de données, $n$ sélections", "c53": _MUX, "c54": r"$2^n$ sorties", "c55": _MUX, "c56": _MUX + r" · consensus", "c57": _MUX + r" · $f=AB+\overline AC$ par valeur de $AB$",
    "c61": _DIS, "c62": _DIS, "c63": _DIS, "c64": _DIS + r" · Φ si $D=0$", "c65": r"$2^4$ lignes", "c66": _DIS,
    "cx1": _FA, "cx2": _AS, "cx3": _CMP, "cx4": _DIS,
    "cy1": _FA + r" · $S=(A+B+C_{-1})\bmod2^8$", "cy2": r"$C_7=1\iff A+B+C_{-1}\ge256$", "cy3": _AS, "cy4": _MUX + r" · $A\oplus B\oplus C$ impair", "cy5": r"majorité $=AB+AC+BC$ · " + _FA,
}
