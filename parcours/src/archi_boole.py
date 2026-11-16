"""Level path: S1 computer architecture, Boolean algebra (laws, canonical forms, Karnaugh maps, combinational problems, NAND).

Calibrated on the Moodle course « Archi S1 - Promo 2030 » (Boolean algebra, TD4-TD7, QCM d'entraînement) and on the exams
`s1_exam2_fr.pdf` (2024/2025) and `b2_exam_fr.pdf` (2025/2026, B2). Notation: `+` OR, `.` AND, overline NOT.
`build.py` checks every stated expression: `eqv` (same truth table as the statement) or `cover` (true on the listed minterms,
false outside minterms and don't-cares; variables most significant first). Minimal forms were computed with sympy `SOPform`.
"""

SUBJECT = {
    "id": "archi-s1-boole",
    "ordre": 410,
    "matiere": "archi",
    "semestre": "S1",
    "ecue": "Algèbre de Boole",
    "titre": "Algèbre de Boole et logique combinatoire",
    "chapitres_moodle": ["06_Algèbre de Boole [2526_I_INF_FISE_S01_PR_BOOL]", "08_Travaux Dirigés", "09_Entraînement"],
    "td": "TD 4 à 7 d'architecture (Moodle Archi S1)",
    "examens": ["Examen B2 d'architecture des ordinateurs"],
}

NOTIONS = [
    {"id": "portes", "titre": "Portes logiques et tables de vérité",
     "formule": r"NON $\overline A$ · ET $A.B$ · OU $A+B$ · NON-ET $\overline{A.B}$ · NON-OU $\overline{A+B}$ · OU exclusif $A\oplus B=A\overline B+\overline AB$ · $n$ entrées : $2^n$ lignes",
     "exemple": r"$A\oplus B=1$ si et seulement si $A\neq B$ : $1\oplus1=0$",
     "cours": r"Une table de vérité donne la sortie pour chacune des $2^n$ combinaisons d'entrées. Énumérer les lignes dans l'ordre binaire (000, 001, 010, …) pour ne rien oublier."},
    {"id": "lois", "titre": "Lois de l'algèbre de Boole",
     "formule": r"$A+0=A$, $A.1=A$ · $A+1=1$, $A.0=0$ · $A+A=A$, $A.A=A$ · $A+\overline A=1$, $A.\overline A=0$ · absorption : $A+AB=A$, $A(A+B)=A$ · $A+\overline AB=A+B$ · $A.B+A.\overline B=A$",
     "exemple": r"$A+AB=A(1+B)=A$",
     "cours": r"Mettre en facteur (distributivité des deux lois : $A(B+C)=AB+AC$ et $A+BC=(A+B)(A+C)$) puis appliquer $A+\overline A=1$. L'absorption élimine tout terme contenant déjà un autre terme."},
    {"id": "morgan", "titre": "Théorèmes de De Morgan",
     "formule": r"$\overline{A.B}=\overline A+\overline B$ · $\overline{A+B}=\overline A.\overline B$ · $\overline{\overline A}=A$",
     "exemple": r"$\overline{A+B}.C=\overline A\,\overline B\,C$",
     "cours": r"Pour nier une expression : nier chaque variable et échanger ET et OU. Il faut ensuite que le résultat ne contienne plus de barre au-dessus de plusieurs variables (consigne habituelle : « pas de parenthèses »)."},
    {"id": "canonique", "titre": "Formes canoniques",
     "formule": r"1re forme : somme (OU) de produits (ET) contenant toutes les variables, un produit par ligne à $1$ · 2e forme : produit (ET) de sommes (OU) contenant toutes les variables, une somme par ligne à $0$ (variables complémentées quand elles valent $1$ sur la ligne)",
     "exemple": r"$A+B$ (2 variables) : $\overline AB+A\overline B+AB$ (lignes 01, 10, 11)",
     "cours": r"1re forme : pour chaque ligne à $1$, ET de toutes les variables (variable directe si elle vaut $1$, complémentée sinon). 2e forme : pour chaque ligne à $0$, OU de toutes les variables (directe si elle vaut $0$, complémentée sinon), puis ET de ces sommes."},
    {"id": "karnaugh3", "titre": "Tableau de Karnaugh à 3 variables",
     "formule": r"colonnes $BA$ en code de Gray : $00,01,11,10$ · lignes $C=0,1$ · regrouper des $1$ en rectangles de $1,2,4,8$ cases (bords opposés adjacents) · chaque groupe = produit des variables constantes",
     "exemple": r"$S=\overline A\,\overline B\,\overline C+BC\ldots$ : un groupe de $4$ cases ne garde qu'une variable",
     "cours": r"Les cases adjacentes ne diffèrent que d'un bit (y compris la première et la dernière colonne). Les groupes les plus grands donnent les termes les plus courts. Les indifférents (Φ) peuvent être inclus ou non dans un groupe, mais ne justifient jamais un groupe à eux seuls."},
    {"id": "karnaugh4", "titre": "Tableau de Karnaugh à 4 variables",
     "formule": r"lignes $DC$ et colonnes $BA$ en code de Gray ($00,01,11,10$) · 16 cases, adjacence circulaire (haut/bas et gauche/droite, 4 coins ensemble) · un groupe de $2^k$ cases supprime $k$ variables",
     "exemple": r"quatre coins du tableau : $\overline B\,\overline A$ ($DC$ varie, $BA=00$ et $10$ ...)",
     "cours": r"Toujours remplir le tableau avant de grouper : aucune note n'est donnée à une expression si le tableau est faux. Prendre les plus grands groupes possibles, couvrir tous les $1$, utiliser les Φ seulement s'ils agrandissent un groupe."},
    {"id": "xor", "titre": "Le OU exclusif",
     "formule": r"$A\oplus B=A\overline B+\overline AB=(A+B)\overline{AB}$ · $A\oplus0=A$ · $A\oplus1=\overline A$ · $A\oplus A=0$ · commutatif et associatif · motif en damier dans Karnaugh",
     "exemple": r"$\overline AB+A\overline B=A\oplus B$",
     "cours": r"Dans un tableau de Karnaugh, des $1$ disposés en damier se simplifient avec le OU exclusif. Pour 3 variables, $A\oplus B\oplus C=1$ si un nombre impair d'entrées valent $1$."},
    {"id": "probleme", "titre": "Du problème à la table de vérité",
     "formule": r"1. nommer entrées et sorties · 2. table de vérité ($2^n$ lignes), combinaisons impossibles : Φ · 3. une sortie = un tableau de Karnaugh · 4. expression simplifiée",
     "exemple": r"3 capteurs d'une cuve : seules $000,001,011,111$ sont possibles ; les autres combinaisons donnent le voyant de défaut",
     "cours": r"Lire l'énoncé ligne par ligne et traduire chaque condition en valeurs de capteurs. Une combinaison physiquement impossible vaut Φ (indifférent) si le cahier des charges ne dit rien, mais peut aussi déclencher une sortie « défaut » si l'énoncé le demande."},
    {"id": "nand", "titre": "Portes NON-ET universelles",
     "formule": r"$\overline A=\overline{A.A}$ · $A.B=\overline{\overline{A.B}.\overline{A.B}}$ (2 portes) · $A+B=\overline{\overline A.\overline B}$ (3 portes) · $A\oplus B$ avec 4 portes NON-ET",
     "exemple": r"NON : une porte dont les deux entrées sont reliées",
     "cours": r"Toute fonction booléenne se réalise avec seulement des portes NON-ET. Méthode : écrire l'expression, appliquer De Morgan pour faire apparaître des $\overline{X.Y}$, puis remplacer chaque NON par un NON-ET à entrées reliées."},
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


B2 = "Examen B2 d'architecture 2025/2026"
S12 = "Examen 2 d'architecture S1 2024/2025"

LEVELS = [
    {"n": 1, "titre": "Portes et tables de vérité", "notions": ["portes"], "exos": [
        v("b11", r"Sortie d'une porte NON-ET pour $A=1$, $B=1$ ?", "1-1*1", "0", r"$\overline{1.1}=\overline1=0$.", duree=1),
        v("b12", r"Sortie d'une porte NON-OU pour $A=0$, $B=0$ ?", "1-(0+0-0*0)", "1", r"$\overline{0+0}=\overline0=1$.", duree=1),
        v("b13", r"Sortie d'un OU exclusif pour $A=1$, $B=1$ ?", "1+1-2*1*1", "0", r"$A\oplus B=1$ seulement si $A\neq B$ : ici $0$.", duree=1),
        v("b14", r"Combien de lignes dans la table de vérité d'une fonction de $4$ variables ?", "2**4", "16", r"$2^4=16$.", duree=1),
        v("b15", r"Combien de fonctions booléennes différentes de $2$ variables existe-t-il ?", "2**(2**2)", "16", r"$4$ lignes, chacune à $0$ ou $1$ : $2^4=16$.", duree=2),
        o("b16", r"Donner la table de vérité du OU exclusif, du NON-ET et du NON-OU pour deux entrées $A$, $B$.",
          r"| $A$ | $B$ | $A\oplus B$ | NON-ET | NON-OU |" "\n|---|---|---|---|---|\n"
          r"| 0 | 0 | 0 | 1 | 1 |" "\n" r"| 0 | 1 | 1 | 1 | 0 |" "\n" r"| 1 | 0 | 1 | 1 | 0 |" "\n" r"| 1 | 1 | 0 | 0 | 0 |", duree=4),
    ]},
    {"n": 2, "titre": "Lois de base et absorption", "notions": ["lois"], "exos": [
        v("b21", r"Simplifier $A+A.B$. Contrôle : la forme simplifiée est $A$ ?", "eqv(A | (A & B), A)", "1", r"$A+AB=A(1+B)=A$ (absorption).", duree=2),
        v("b22", r"Simplifier $A.(A+B)$. Contrôle : la forme simplifiée est $A$ ?", "eqv(A & (A | B), A)", "1", r"$A(A+B)=A+AB=A$.", duree=2),
        v("b23", r"Simplifier $A+\overline A.B$. Contrôle : la forme simplifiée est $A+B$ ?", "eqv(A | (~A & B), A | B)", "1", r"$A+\overline AB=(A+\overline A)(A+B)=A+B$.", duree=2),
        v("b24", r"Simplifier $A.B+A.\overline B$. Contrôle : la forme simplifiée est $A$ ?", "eqv((A & B) | (A & ~B), A)", "1", r"$A(B+\overline B)=A$.", duree=2),
        v("b25", r"Simplifier $(A+B).(A+\overline B)$. Contrôle : la forme simplifiée est $A$ ?", "eqv((A | B) & (A | ~B), A)", "1", r"$(A+B)(A+\overline B)=A+B\overline B=A$.", duree=2),
        v("b26", r"Simplifier $\overline A.B+\overline A.\overline B+A.B$. Contrôle : la forme simplifiée est $\overline A+B$ ?", "eqv((~A & B) | (~A & ~B) | (A & B), ~A | B)", "1",
          r"$\overline A(B+\overline B)+AB=\overline A+AB=\overline A+B$.", duree=3),
    ]},
    {"n": 3, "titre": "De Morgan", "notions": ["morgan", "lois"], "exos": [
        v("b31", r"Développer $\overline{A+B}.C$ (sans barre sur plusieurs variables). Contrôle : $\overline A.\overline B.C$ ?", "eqv(~(A | B) & C, ~A & ~B & C)", "1", r"$\overline{A+B}=\overline A.\overline B$.", duree=2),
        v("b32", r"Développer $\overline{A.B}+C$. Contrôle : $\overline A+\overline B+C$ ?", "eqv(~(A & B) | C, ~A | ~B | C)", "1", r"$\overline{AB}=\overline A+\overline B$.", duree=2),
        v("b33", r"Simplifier $\overline{A.B}.(A+\overline B)$. Contrôle : $\overline B$ ?", "eqv(~(A & B) & (A | ~B), ~B)", "1",
          r"$(\overline A+\overline B)(A+\overline B)=\overline B+\overline A\,A=\overline B$.", src=S12 + ", ex. 1 (adapté)", duree=3),
        v("b34", r"Simplifier $\overline{\overline A+B}+A.B$. Contrôle : $A$ ?", "eqv(~(~A | B) | (A & B), A)", "1",
          r"$\overline{\overline A+B}=A\overline B$, donc $A\overline B+AB=A$.", duree=3),
        v("b35", r"Simplifier $\overline{ABC}+AB$. Contrôle : l'expression vaut toujours $1$ ?", "eqv(~(A & B & C) | (A & B), True)", "1",
          r"Si $AB=1$ le second terme vaut $1$ ; sinon $ABC=0$ et $\overline{ABC}=1$ : la somme vaut toujours $1$.", duree=3),
    ]},
    {"n": 4, "titre": "Simplifier des expressions", "notions": ["lois", "morgan"], "exos": [
        v("b41", r"Simplifier $A.B+\overline A.B+A.\overline B$. Contrôle : $A+B$ ?", "eqv((A & B) | (~A & B) | (A & ~B), A | B)", "1", r"$AB+\overline AB=B$, puis $B+A\overline B=A+B$.", duree=3),
        v("b42", r"Simplifier $(A+B).(A+C)+A.B.C$. Contrôle : $A+B.C$ ?", "eqv(((A | B) & (A | C)) | (A & B & C), A | (B & C))", "1",
          r"$(A+B)(A+C)=A+BC$ et $ABC$ est absorbé par $A$.", src=S12 + ", ex. 1", duree=3),
        v("b43", r"Simplifier $A+B.C+A.(B+C).(A.D+C)$. Contrôle : $A+B.C$ ?", "eqv(A | (B & C) | (A & (B | C) & ((A & D) | C)), A | (B & C))", "1",
          r"Le terme $A.(\ldots)$ est absorbé par $A$ : il reste $A+BC$.", src=B2 + ", ex. 1", duree=3),
        v("b44", r"Simplifier $A.B.C.D+A.B.C.\overline D+A.B.\overline C.D+A.B.\overline C.\overline D$. Contrôle : $A.B$ ?", "eqv((A&B&C&D) | (A&B&C&~D) | (A&B&~C&D) | (A&B&~C&~D), A & B)", "1",
          r"$AB\left(CD+C\overline D+\overline CD+\overline C\overline D\right)=AB$.", duree=3),
        v("b45", r"Simplifier $(A+B+C).(A+C).(A+B)$. Contrôle : $A+B.C$ ?", "eqv((A | B | C) & (A | C) & (A | B), A | (B & C))", "1",
          r"$(A+C)(A+B)=A+BC$ ; $(A+B+C)(A+BC)=A+BC$ (absorption).", src=S12 + ", ex. 1", duree=4),
        v("b46", r"Théorème du consensus : vérifier que $AB+\overline AC+BC=AB+\overline AC$. Contrôle ?", "eqv((A&B)|(~A&C)|(B&C), (A&B)|(~A&C))", "1",
          r"$BC=BC(A+\overline A)=ABC+\overline ABC$, terme absorbé par $AB$ et par $\overline AC$ : le terme $BC$ est redondant.", duree=4),
    ]},
    {"n": 5, "titre": "Formes canoniques", "notions": ["canonique", "portes"], "exos": [
        v("b51", r"1re forme canonique de $A+B$ (2 variables). Contrôle : $\overline AB+A\overline B+AB$ ?", "eqv(A | B, (~A & B) | (A & ~B) | (A & B))", "1",
          r"Lignes à $1$ : $01$, $10$, $11$.", duree=2),
        v("b52", r"1re forme canonique de $A.(B+C)$ (3 variables $A,B,C$). Contrôle : $ABC+AB\overline C+A\overline BC$ ?", "eqv(A & (B | C), (A&B&C) | (A&B&~C) | (A&~B&C))", "1",
          r"Lignes à $1$ : $111$, $110$, $101$.", src=S12 + ", ex. 2", duree=3),
        v("b53", r"2e forme canonique de $(A+B).(B+C)$ (3 variables). Contrôle : $(A+B+C)(A+B+\overline C)(\overline A+B+C)$ ?", "eqv((A | B) & (B | C), (A | B | C) & (A | B | ~C) & (~A | B | C))", "1",
          r"$(A+B)(B+C)=B+AC$ : à $0$ pour $ABC=000,001,100$ ; une somme par ligne à $0$.", src=B2 + ", ex. 2", duree=4),
        v("b54", r"2e forme canonique de $A+B.C$ (3 variables). Contrôle : $(A+B+C)(A+B+\overline C)(A+\overline B+C)$ ?", "eqv(A | (B & C), (A | B | C) & (A | B | ~C) & (A | ~B | C))", "1",
          r"À $0$ si $A=0$ et $BC\neq11$ : lignes $000,001,010$.", src=B2 + ", ex. 2", duree=4),
        v("b55", r"Combien de lignes à $1$ pour $A+B$ si l'on travaille avec $3$ variables $A,B,C$ ?", "6", "6", r"$A=1$ : $4$ lignes ; $B=1$ : $4$ lignes ; communes $A=B=1$ : $2$. Total $4+4-2=6$.", duree=3),
        o("b56", r"Donner la première forme canonique de $A+B.(C+D)$ (4 variables).",
          r"$A+BC+BD$ : $A=1$ (8 lignes) ou $B=1$ avec $C=1$ ou $D=1$." "\n\n"
          r"Lignes à $1$ ($ABCD$) : $1000$ à $1111$ ($A=1$), plus $0111,0110,0101$ (à $A=0$, $B=1$, $CD\neq00$). Soit $11$ produits de $4$ variables.", src=S12 + ", ex. 2", duree=6),
    ]},
    {"n": 6, "titre": "Karnaugh à 3 variables", "notions": ["karnaugh3", "lois"], "exos": [
        v("b61", r"$S_1=1$ pour $N=0,3,6,7$ ($N$ sur 3 bits $CBA$). Expression simplifiée proposée : $S_1=BC+AB+\overline A.\overline B.\overline C$. Contrôle ?", "cover((B&C)|(A&B)|(~A&~B&~C), 'CBA', [0,3,6,7])", "1",
          r"Groupes : $6,7$ ($BC$) ; $3,7$ ($AB$) ; $0$ seul.", src=S12 + ", ex. 3", duree=4),
        v("b62", r"$S_2=1$ pour $N=0,2,4,6$, indéfinie pour $N=1,5$ ($CBA$). Expression simplifiée proposée : $S_2=\overline A$. Contrôle ?", "cover(~A, 'CBA', [0,2,4,6], [1,5])", "1",
          r"Les quatre $1$ sont les cases où $A=0$ : un groupe de $4$ cases ($\overline A$) ; les Φ ne servent pas.", src=S12 + ", ex. 3", duree=3),
        v("b63", r"$f=1$ pour $N=1,3,5,7$ ($CBA$). Expression simplifiée : $A$. Contrôle ?", "cover(A, 'CBA', [1,3,5,7])", "1", r"Les cases à $A=1$ forment une colonne : $f=A$.", duree=2),
        v("b64", r"$f=1$ pour $N=0,1,2,3$ ($CBA$). Expression simplifiée : $\overline C$. Contrôle ?", "cover(~C, 'CBA', [0,1,2,3])", "1", r"La ligne $C=0$ entière : $f=\overline C$.", duree=2),
        v("b65", r"$f=1$ pour $N=0,2,4,6$ et $f$ indéfinie pour $N=3$ ($CBA$). Peut-on faire mieux que $\overline A$ ? Contrôle de $\overline A$ ?", "cover(~A, 'CBA', [0,2,4,6], [3])", "1",
          r"Non : $\overline A$ est déjà un groupe maximal de $4$ cases. Le Φ en $3$ ($A=1$) n'ajoute rien.", duree=3),
        o("b66", r"Remplir le tableau de Karnaugh de $S_1$ ($1$ pour $N=0,3,6,7$ ; lignes $C$, colonnes $BA$ dans l'ordre $00,01,11,10$) et justifier le choix des groupes.",
          r"| $C\backslash BA$ | 00 | 01 | 11 | 10 |" "\n|---|---|---|---|---|\n"
          r"| 0 | 1 | 0 | 1 | 0 |" "\n" r"| 1 | 0 | 0 | 1 | 1 |" "\n\n"
          r"Groupes : $\{N=6,7\}$ (colonnes $11,10$, ligne $1$) donne $BC$ ; $\{N=3,7\}$ (colonne $11$) donne $AB$ ; $N=0$ isolé donne $\overline A\,\overline B\,\overline C$. $S_1=BC+AB+\overline A\,\overline B\,\overline C$.", src=S12 + ", ex. 3", duree=6),
    ]},
    {"n": 7, "titre": "Karnaugh à 4 variables", "notions": ["karnaugh4", "karnaugh3"], "exos": [
        v("b71", r"$S_3=1$ pour $N=0,1,4,5,6,7,9,11$ ($DCBA$). Expression simplifiée proposée : $S_3=C\overline D+\overline B\overline D+A\overline C D$. Contrôle ?", "cover((C&~D)|(~B&~D)|(A&D&~C), 'DCBA', [0,1,4,5,6,7,9,11])", "1",
          r"Groupes : $\{4,5,6,7\}$ donne $C\overline D$ ; $\{0,1,4,5\}$ donne $\overline B\,\overline D$ ; $\{9,11\}$ donne $A\overline CD$.", src=S12 + ", ex. 3", duree=6),
        v("b72", r"$S_4=1$ pour $N=0,1,2,3,4,6,8,9,10,11$ ($DCBA$). Expression simplifiée proposée : $S_4=\overline C+\overline A\,\overline D$. Contrôle ?", "cover(~C | (~A & ~D), 'DCBA', [0,1,2,3,4,6,8,9,10,11])", "1",
          r"Groupe de $8$ cases ($C=0$) : $\overline C$ ; les cases $4,6$ complétées par $0,2$ ($\overline A\,\overline D$).", src=S12 + ", ex. 3", duree=6),
        v("b73", r"$S_5=1$ pour $N=0,2,4,5,6,8,12,13,14$, indéfinie pour $N=10,11,15$ ($DCBA$). Expression simplifiée proposée : $S_5=\overline A+C\overline B$. Contrôle ?", "cover(~A | (C&~B), 'DCBA', [0,2,4,5,6,8,12,13,14], [10,11,15])", "1",
          r"Groupe de $8$ cases ($A=0$, avec Φ en $10$) : $\overline A$ ; groupe $\{4,5,12,13\}$ : $C\overline B$.", src=S12 + ", ex. 3", duree=6),
        v("b74", r"$S_6=1$ pour $N=2,3,6,7,10,11,14,15$, indéfinie pour $N=1,4,5,9,12,13$ ($DCBA$). Expression simplifiée proposée : $S_6=B$. Contrôle ?", "cover(B, 'DCBA', [2,3,6,7,10,11,14,15], [1,4,5,9,12,13])", "1",
          r"Les huit $1$ sont les cases où $B=1$ : un groupe de $8$ cases, $S_6=B$.", src=S12 + ", ex. 3", duree=5),
        v("b75", r"Que vaut la fonction qui est à $1$ aux quatre coins du tableau ($N=0,2,8,10$, $DCBA$) ? Expression proposée : $\overline C.\overline A$. Contrôle ?", "cover(~C & ~A, 'DCBA', [0,2,8,10])", "1",
          r"Les quatre coins sont adjacents : $C=0$ et $A=0$, $D$ et $B$ varient.", duree=4),
        o("b76", r"Remplir le tableau de Karnaugh de $S_4$ et dessiner les groupes. Rappeler l'ordre des lignes et colonnes.",
          r"Lignes $DC$ : $00,01,11,10$ ; colonnes $BA$ : $00,01,11,10$. $S_4=1$ pour $N=0,1,2,3,4,6,8,9,10,11$." "\n\n"
          r"| $DC\backslash BA$ | 00 | 01 | 11 | 10 |" "\n|---|---|---|---|---|\n"
          r"| 00 | 1 | 1 | 1 | 1 |" "\n" r"| 01 | 1 | 0 | 0 | 1 |" "\n" r"| 11 | 0 | 0 | 0 | 0 |" "\n" r"| 10 | 1 | 1 | 1 | 1 |" "\n\n"
          r"Groupe de $8$ (lignes $00$ et $10$, bords opposés adjacents) : $\overline C$. Groupe de $4$ (colonnes $00$ et $10$, lignes $00$ et $01$) : $\overline A\,\overline D$.", src=S12 + ", ex. 3", duree=6),
    ]},
    {"n": 8, "titre": "Karnaugh avec indifférents et OU exclusif", "notions": ["karnaugh4", "xor"], "exos": [
        v("b81", r"$S_1=1$ ssi $N=2,3,6,7,10,11,12,13$ ($DCBA$). Expression simplifiée proposée : $S_1=B\overline C+B\overline D+\overline BCD$. Contrôle ?", "cover((B&~C)|(B&~D)|(C&D&~B), 'DCBA', [2,3,6,7,10,11,12,13])", "1",
          r"Groupes : $\{2,3,10,11\}$ donne $B\overline C$ ; $\{2,3,6,7\}$ donne $B\overline D$ ; $\{12,13\}$ donne $\overline BCD$.", src=B2 + ", ex. 3", duree=6),
        v("b82", r"$S_2=1$ ssi $N=0,4,6,8,12,14$, indéfinie pour $N=3,5,7,10,13,15$ ($DCBA$). Expression proposée : $S_2=C+\overline A\,\overline B$. Contrôle ?", "cover(C | (~A & ~B), 'DCBA', [0,4,6,8,12,14], [3,5,7,10,13,15])", "1",
          r"Groupe de $8$ cases ($C=1$, qui absorbe les Φ $5,7,13,15$) : $C$ ; groupe $\{0,4,8,12\}$ ($A=0$, $B=0$) : $\overline A\,\overline B$.", src=B2 + ", ex. 3", duree=6),
        v("b83", r"$S_3=1$ ssi $N=0,1,4,5,8,9,12,13$, indéfinie pour $N=3,7,11,15$ ($DCBA$). Expression proposée : $S_3=\overline B$. Contrôle ?", "cover(~B, 'DCBA', [0,1,4,5,8,9,12,13], [3,7,11,15])", "1",
          r"Groupe de $8$ cases où $B=0$ (les Φ $3,7,11,15$ ont $B=1$ et ne servent pas) : $S_3=\overline B$.", src=B2 + ", ex. 3", duree=5),
        v("b84", r"$S_4=1$ ssi $N=8,10,14,15$, indéfinie pour $N=0,\dots,7$ ($DCBA$). Expression simplifiée proposée : $S_4=BC+\overline A\,\overline C$. Contrôle ?", "cover((B&C)|(~A&~C), 'DCBA', [8,10,14,15], [0,1,2,3,4,5,6,7])", "1",
          r"$\{14,15\}$ élargi aux Φ $6,7$ ($B=1,C=1$) : $BC$ ; $\{8,10\}$ élargi aux Φ $0,2$ puis $\{0,2,8,10\}$ ($A=0$, $C=0$) : $\overline A\,\overline C$.", src=B2 + ", ex. 3", duree=6),
        v("b85", r"Écrire $\overline A.B+A.\overline B$ avec le OU exclusif. Contrôle : $A\oplus B$ ?", "eqv((~A & B) | (A & ~B), Xor(A, B))", "1", r"C'est la définition : $A\oplus B$.", duree=2),
        o("b86", r"Simplifier $S_1$ (niveau 8, $B\overline C+B\overline D+CD\overline B$) à l'aide du OU exclusif.",
          r"$S_1=B\overline C+B\overline D+\overline BCD$." "\n\n"
          r"On remarque $B(\overline C+\overline D)=B\,\overline{CD}$ et $\overline BCD$ : si $CD=1$, $S_1=\overline B$ ; si $CD=0$, $S_1=B$. Donc $S_1=B\oplus CD$ (vrai si $B$ et $CD$ diffèrent).", src=B2 + ", ex. 3 q. 2", duree=8),
    ]},
    {"n": 9, "titre": "Problèmes logiques", "notions": ["probleme", "karnaugh3"], "exos": [
        v("b91", r"Cuve à 3 capteurs $C_3C_2C_1$ (immergé $=1$). Seules $000,001,011,111$ sont cohérentes. Voyant $L_1$ (volume $<250$ L) : expression ? Contrôle : $\overline{C_3}\,\overline{C_2}\,\overline{C_1}$ ?", "cover(~C & ~B & ~A, 'CBA', [0])", "1",
          r"Avec $A=C_1$, $B=C_2$, $C=C_3$ : $L_1=1$ seulement pour $000$ (aucun capteur immergé).", src=B2 + ", ex. 4", duree=3),
        v("b92", r"Même cuve : $L_4$ (volume $\ge750$ L). Contrôle : $L_4=C_3.C_2.C_1$ ?", "cover(C & B & A, 'CBA', [7])", "1", r"Seul $111$ allume $L_4$.", src=B2 + ", ex. 4", duree=3),
        v("b93", r"Même cuve : le voyant de défaut $L_0$ s'allume pour $010,100,101,110$. Expression simplifiée proposée : $L_0=C_2.\overline{C_1}+C_3.\overline{C_2}$. Contrôle ?", "cover((B&~A)|(C&~B), 'CBA', [2,4,5,6])", "1",
          r"Karnaugh ($C_3$ en ligne, $C_2C_1$ en colonne) : groupe $\{010,110\}$ donne $C_2\overline{C_1}$ ; groupe $\{100,101\}$ donne $C_3\overline{C_2}$.", src=B2 + ", ex. 4", duree=5),
        v("b94", r"Deux réservoirs : détecteurs hauts $A$ ($R_1$), $B$ ($R_2$) et bas $C$ ($R_1$), $D$ ($R_2$). $V_1=1$ si les deux sont pleins. Les cas « haut à $1$ avec bas à $0$ » sont impossibles (Φ). Expression simplifiée proposée : $V_1=A.B$. Contrôle ?", "cover(A & B, 'ABCD', [15], [4,6,8,9,12,13,14])", "1",
          r"Φ en $A=1,C=0$ ($8,9,12,13$) et $B=1,D=0$ ($4,6,12,14$). Un seul $1$ réel ($1111$) : on le groupe avec les Φ voisins pour obtenir $AB$.", src=S12 + ", ex. 4", duree=6),
        v("b95", r"Mêmes réservoirs : $V_3=1$ dans tous les autres cas. Expression simplifiée proposée : $V_3=C.\overline B+D.\overline A$. Contrôle ?", "cover((C&~B)|(D&~A), 'ABCD', [1,2,3,5,7,10,11], [4,6,8,9,12,13,14])", "1",
          r"$V_3=1$ pour $0001,0010,0011,0101,0111,1010,1011$. Avec les Φ : $C\overline B$ et $D\overline A$.", src=S12 + ", ex. 4", duree=6),
        o("b96", r"Un ascenseur a deux capteurs d'étage $E_1$ et $E_2$ et un capteur de porte fermée $P$. Le moteur $M$ doit tourner si la porte est fermée et l'ascenseur n'est à aucun étage ($E_1=E_2=0$). $E_1$ et $E_2$ ne peuvent pas être à $1$ ensemble. Écrire la table de vérité et l'expression de $M$.",
          r"Entrées $E_1,E_2,P$ ; la combinaison $E_1E_2=11$ est impossible (Φ)." "\n\n"
          r"$M=1$ pour $E_1E_2P=001$ seulement. Les Φ ($110,111$) ne permettent aucun groupe plus grand : $M=\overline{E_1}\,\overline{E_2}\,P$." "\n\n"
          r"Contrôle : $M=P.\overline{E_1+E_2}$.", duree=8),
    ]},
    {"n": 10, "titre": "Tout avec des portes NON-ET", "notions": ["nand", "morgan"], "exos": [
        v("b101", r"Combien de portes NON-ET pour réaliser un ET ?", "2", "2", r"$A.B=\overline{\overline{A.B}}$ : une NON-ET puis une NON-ET à entrées reliées.", src=B2 + ", ex. 5", duree=2),
        v("b102", r"Combien de portes NON-ET pour réaliser un OU ?", "3", "3", r"$A+B=\overline{\overline A.\overline B}$ : deux inverseurs (NON-ET à entrées reliées) puis une NON-ET.", src=B2 + ", ex. 5", duree=3),
        v("b103", r"Combien de portes NON-ET pour réaliser un NON ?", "1", "1", r"$\overline A=\overline{A.A}$.", duree=1),
        v("b104", r"Combien de portes NON-ET pour réaliser un OU exclusif (version minimale) ?", "4", "4", r"Avec $P=\overline{AB}$, $N_1=\overline{AP}$, $N_2=\overline{BP}$ et $S=\overline{N_1N_2}$ : $4$ portes (le sujet en autorise $5$).", src=B2 + ", ex. 5", duree=4),
        v("b105", r"Vérifier $A\oplus B=\overline{\overline{A\,\overline{AB}}\ \overline{B\,\overline{AB}}}$. Contrôle ?", "eqv(Xor(A, B), ~(~(A & ~(A & B)) & ~(B & ~(A & B))))", "1",
          r"$A\overline{AB}=A\overline B$, $B\overline{AB}=\overline AB$, et $\overline{\overline X\,\overline Y}=X+Y$ : on retrouve $A\overline B+\overline AB$.", duree=4),
        o("b106", r"Dessiner le schéma (liste des portes) d'un ET, d'un OU et d'un OU exclusif avec uniquement des portes NON-ET.",
          r"ET : $N_1=\overline{AB}$, $S=\overline{N_1N_1}$ (2 portes)." "\n\n"
          r"OU : $N_1=\overline{AA}=\overline A$, $N_2=\overline{BB}=\overline B$, $S=\overline{N_1N_2}=A+B$ (3 portes)." "\n\n"
          r"OU exclusif : $P=\overline{AB}$, $N_1=\overline{AP}$, $N_2=\overline{BP}$, $S=\overline{N_1N_2}$ (4 portes).", src=B2 + ", ex. 5 (3 points)", duree=8),
    ]},
    {"n": 11, "titre": "Niveau examen : sujet B2", "notions": ["lois", "canonique", "karnaugh4", "xor", "probleme", "nand"], "examen": True, "exos": [
        o("bx1", r"Simplifier : $A+B.C+A.(B+C).(A.D+C)$ ; $A.B.C.D+A.B.C.\overline D+A.B.\overline C.D+A.B.\overline C.\overline D$ ; $(A+B.\overline C).A.B$ .",
          r"$A+BC$ ; $AB$ ; $(A+B\overline C)AB=AB+AB\overline C=AB$ (absorption).", src=B2 + ", ex. 1 (4 points)", duree=10),
        o("bx2", r"1. Première forme canonique de $A+B$ (2 variables) et de $(A+C).(A+C+D).B.C$ (variables $A,B,C,D$). 2. Seconde forme canonique de $(A+B).(B+C)$ et de $A+B.C$.",
          r"1. $A+B=\overline AB+A\overline B+AB$ ; pour le second, $(A+C)(A+C+D)BC=BC$ : lignes à $1$ ($ABCD$) $0110,0111,1110,1111$, soit $\overline ABC\overline D+\overline ABCD+ABC\overline D+ABCD$." "\n\n"
          r"2. $(A+B)(B+C)$ : $(A+B+C)(A+B+\overline C)(\overline A+B+C)$ ; $A+BC$ : $(A+B+C)(A+B+\overline C)(A+\overline B+C)$.", src=B2 + ", ex. 2 (4 points)", duree=12),
        o("bx3", r"Tableaux de Karnaugh ($DCBA$) : $S_1=1$ ssi $N=2,3,6,7,10,11,12,13$ ; $S_2=1$ ssi $N=0,4,6,8,12,14$ (Φ : $3,5,7,10,13,15$) ; $S_3=1$ ssi $N=0,1,4,5,8,9,12,13$ (Φ : $3,7,11,15$) ; $S_4=1$ ssi $N=8,10,14,15$ (Φ : $0$ à $7$). Donner les expressions les plus simplifiées.",
          r"$S_1=B\overline C+B\overline D+\overline BCD$." "\n\n"
          r"$S_2=C+\overline A\,\overline B$." "\n\n"
          r"$S_3=\overline B$." "\n\n"
          r"$S_4=BC+\overline A\,\overline C$ (groupes élargis aux Φ).", src=B2 + ", ex. 3 (5 points)", duree=15),
        o("bx4", r"Cuve de $1000$ L avec capteurs $C_1$ ($250$ L), $C_2$ ($500$ L), $C_3$ ($750$ L). Voyants $L_1$ ($V<250$), $L_2$ ($250\le V<500$), $L_3$ ($500\le V<750$), $L_4$ ($V\ge750$), $L_0$ défaut. Table de vérité, expressions de $L_1$ à $L_4$, tableau de Karnaugh de $L_0$.",
          r"Lignes $C_3C_2C_1$ : $000\to L_1$ ; $001\to L_2$ ; $011\to L_3$ ; $111\to L_4$ ; $010,100,101,110\to L_0$." "\n\n"
          r"$L_1=\overline{C_3}\,\overline{C_2}\,\overline{C_1}$, $L_2=\overline{C_3}\,\overline{C_2}\,C_1$, $L_3=\overline{C_3}C_2C_1$, $L_4=C_3C_2C_1$." "\n\n"
          r"$L_0=C_2\overline{C_1}+C_3\overline{C_2}$.", src=B2 + ", ex. 4 (4 points)", duree=15),
        o("bx5", r"Schémas d'un ET (2 portes), d'un OU (3 portes) et d'un OU exclusif (5 portes) avec uniquement des portes NON-ET.",
          r"ET : $\overline{\overline{AB}\ \overline{AB}}$. OU : $\overline{\overline{A}\ \overline{B}}$ avec $\overline A=\overline{AA}$. OU exclusif : $\overline{\overline{A\,\overline{AB}}\ \overline{B\,\overline{AB}}}$ (4 portes, donc dans la limite de 5).", src=B2 + ", ex. 5 (3 points)", duree=10),
    ]},
    {"n": 12, "titre": "Examen + 20 %", "notions": ["canonique", "karnaugh4", "probleme", "morgan"], "examen": True, "exos": [
        v("by1", r"$f=1$ pour $N=1,3,5,7,9,11,13,15$ ($DCBA$). Expression simplifiée : $A$. Contrôle ?", "cover(A, 'DCBA', [1,3,5,7,9,11,13,15])", "1", r"Toutes les cases à $A=1$ : un groupe de $8$.", duree=3),
        v("by2", r"$f=1$ pour $N=0,5,10,15$ ($DCBA$). Expression proposée avec le OU exclusif : $f=\overline{D\oplus B}\ .\ \overline{C\oplus A}$. Contrôle ?", "cover(~Xor(D, B) & ~Xor(C, A), 'DCBA', [0,5,10,15])", "1",
          r"$0000,0101,1010,1111$ : $D=B$ et $C=A$ dans chaque cas, et dans aucun autre.", duree=6),
        v("by3", r"$f=1$ si $N$ ($DCBA$) a un nombre impair de bits à $1$ : $N=1,2,4,7,8,11,13,14$. Expression proposée : $f=A\oplus B\oplus C\oplus D$. Contrôle ?", "cover(Xor(Xor(A, B), Xor(C, D)), 'DCBA', [1,2,4,7,8,11,13,14])", "1",
          r"Le OU exclusif de plusieurs bits vaut $1$ si le nombre de bits à $1$ est impair. Le tableau de Karnaugh est un damier : aucun groupe possible sans OU exclusif.", duree=6),
        o("by4", r"Détecteur de parité sur $3$ bits $A,B,C$ : $P=1$ si le nombre de bits à $1$ est impair. Table de vérité, tableau de Karnaugh et expression avec le OU exclusif.",
          r"$P=1$ pour $001,010,100,111$. Karnaugh en damier : aucun regroupement possible, $P=\overline A\,\overline BC+\overline AB\overline C+A\overline B\,\overline C+ABC$." "\n\n"
          r"Avec le OU exclusif : $P=A\oplus B\oplus C$.", duree=8),
        o("by5", r"Montrer que $A\oplus B$ peut s'écrire $(A+B).\overline{AB}$ et en déduire un montage à portes ET, OU et NON.",
          r"$(A+B)\overline{AB}=(A+B)(\overline A+\overline B)=A\overline B+\overline AB+A\overline A+B\overline B=A\overline B+\overline AB=A\oplus B$." "\n\n"
          r"Montage : une porte OU sur $(A,B)$, une porte ET sur $(A,B)$ suivie d'un NON, puis une porte ET combinant les deux sorties.", duree=6),
    ]},
]


def _v(enonce, calc, ans, sol):
    return {"enonce": enonce, "calc": calc, "ans": ans, "sol": sol}


VARIANTS = {
    "b21": [_v(r"Simplifier $B+B.C$. Contrôle : la forme simplifiée est $B$ ?", "eqv(B | (B & C), B)", "1", r"Absorption : $B(1+C)=B$.")],
    "b23": [_v(r"Simplifier $B+\overline B.C$. Contrôle : la forme simplifiée est $B+C$ ?", "eqv(B | (~B & C), B | C)", "1", r"$B+\overline BC=B+C$.")],
    "b24": [_v(r"Simplifier $B.C+B.\overline C$. Contrôle : $B$ ?", "eqv((B & C) | (B & ~C), B)", "1", r"$B(C+\overline C)=B$.")],
    "b31": [_v(r"Développer $\overline{B+C}.A$. Contrôle : $\overline B.\overline C.A$ ?", "eqv(~(B | C) & A, ~B & ~C & A)", "1", r"De Morgan.")],
    "b41": [_v(r"Simplifier $B.C+\overline B.C+B.\overline C$. Contrôle : $B+C$ ?", "eqv((B&C)|(~B&C)|(B&~C), B | C)", "1", r"$BC+\overline BC=C$ puis $C+B\overline C=B+C$.")],
    "b51": [_v(r"1re forme canonique de $A.B$ pour $3$ variables $A,B,C$ ? Contrôle : $ABC+AB\overline C$ ?", "eqv(A & B, (A&B&C) | (A&B&~C))", "1", r"Lignes à $1$ : $111$, $110$.")],
    "b62": [_v(r"$S=1$ pour $N=1,3,5,7$ et indéfinie pour $N=2$ ($CBA$). Expression proposée : $A$. Contrôle ?", "cover(A, 'CBA', [1,3,5,7], [2])", "1", r"Les quatre $1$ forment la colonne $A=1$.")],
    "b63": [_v(r"$f=1$ pour $N=2,3,6,7$ ($CBA$). Expression simplifiée : $B$. Contrôle ?", "cover(B, 'CBA', [2,3,6,7])", "1", r"Cases à $B=1$.")],
    "b75": [_v(r"Cases $N=0,1,8,9$ ($DCBA$) : expression proposée $\overline C.\overline B$. Contrôle ?", "cover(~C & ~B, 'DCBA', [0,1,8,9])", "1", r"$C=0$ et $B=0$.")],
    "b101": [_v(r"Combien de portes NON-ET pour réaliser un NON-OU ($\overline{A+B}$) ?", "4", "4", r"un OU ($3$ portes) suivi d'un inverseur ($1$ porte) : $4$ portes.")],
}
for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["id"] in VARIANTS:
            _e["variants"] = VARIANTS[_e["id"]]


EXTRA_PARTS = []

QUIZ = [
    {"notion": "portes", "type": "qcm", "q": r"La sortie d'un NON-ET vaut $0$ quand :", "choix": [r"les deux entrées valent $1$", r"une entrée vaut $1$", r"les deux entrées valent $0$", r"jamais"], "bonne": 0},
    {"notion": "portes", "type": "vf", "q": r"Une fonction de $n$ variables a une table de vérité de $2^n$ lignes.", "bonne": True},
    {"notion": "lois", "type": "qcm", "q": r"$A+\overline A.B$ vaut :", "choix": [r"$A+B$", r"$A$", r"$B$", r"$A.B$"], "bonne": 0},
    {"notion": "lois", "type": "vf", "q": r"$A+A.B=A$ (absorption).", "bonne": True},
    {"notion": "morgan", "type": "qcm", "q": r"$\overline{A+B}$ vaut :", "choix": [r"$\overline A.\overline B$", r"$\overline A+\overline B$", r"$A.B$", r"$\overline{A.B}$"], "bonne": 0},
    {"notion": "morgan", "type": "vf", "q": r"$\overline{A.B}=\overline A.\overline B$.", "bonne": False},
    {"notion": "canonique", "type": "qcm", "q": r"La première forme canonique est :", "choix": [r"une somme de produits contenant toutes les variables", r"un produit de sommes contenant toutes les variables", r"toujours la forme la plus courte", r"une expression sans complémentation"], "bonne": 0},
    {"notion": "canonique", "type": "vf", "q": r"La seconde forme canonique s'écrit à partir des lignes de la table de vérité où la fonction vaut $0$.", "bonne": True},
    {"notion": "karnaugh3", "type": "qcm", "q": r"L'ordre des colonnes $BA$ d'un tableau de Karnaugh est :", "choix": [r"$00,\ 01,\ 11,\ 10$", r"$00,\ 01,\ 10,\ 11$", r"$00,\ 10,\ 01,\ 11$", r"$11,\ 10,\ 01,\ 00$"], "bonne": 0},
    {"notion": "karnaugh3", "type": "vf", "q": r"La première et la dernière colonne d'un tableau de Karnaugh sont adjacentes.", "bonne": True},
    {"notion": "karnaugh4", "type": "qcm", "q": r"Un groupe de $8$ cases dans un tableau à $4$ variables correspond à un terme de :", "choix": [r"$1$ variable", r"$2$ variables", r"$3$ variables", r"$4$ variables"], "bonne": 0},
    {"notion": "karnaugh4", "type": "vf", "q": r"Les indifférents (Φ) doivent tous être inclus dans un groupe.", "bonne": False},
    {"notion": "xor", "type": "qcm", "q": r"$A\oplus A$ vaut :", "choix": [r"$0$", r"$1$", r"$A$", r"$\overline A$"], "bonne": 0},
    {"notion": "xor", "type": "vf", "q": r"$A\oplus1=\overline A$.", "bonne": True},
    {"notion": "probleme", "type": "qcm", "q": r"Une combinaison d'entrées physiquement impossible, sans consigne particulière, se note :", "choix": [r"Φ (indifférent)", r"$0$", r"$1$", r"une erreur"], "bonne": 0},
    {"notion": "probleme", "type": "vf", "q": r"On remplit le tableau de Karnaugh avant de choisir les groupes.", "bonne": True},
    {"notion": "nand", "type": "qcm", "q": r"Pour réaliser un OU avec des NON-ET, il faut au minimum :", "choix": [r"$3$ portes", r"$2$ portes", r"$1$ porte", r"$4$ portes"], "bonne": 0},
    {"notion": "nand", "type": "vf", "q": r"Toute fonction booléenne peut se réaliser avec uniquement des portes NON-ET.", "bonne": True},
]

_LOI = r"$A+AB=A$ · $A+\overline AB=A+B$ · $AB+A\overline B=A$ · $A+\overline A=1$"
_MOR = r"$\overline{AB}=\overline A+\overline B$ · $\overline{A+B}=\overline A\,\overline B$"
_CAN = r"1re forme : une ligne à $1$ $\to$ un produit · 2e forme : une ligne à $0$ $\to$ une somme"
_K3 = r"Gray $BA$ : $00,01,11,10$ · groupes de $2^k$ cases"
_K4 = r"Gray $DC$ et $BA$ · adjacence circulaire · groupe de $2^k$ cases supprime $k$ variables · Φ facultatifs"
_XOR = r"$A\oplus B=A\overline B+\overline AB$"
_PRO = r"table de vérité $\to$ Karnaugh (Φ pour les cas impossibles) $\to$ expression"
_NAND = r"$\overline A=\overline{AA}$ · $AB=\overline{\overline{AB}\,\overline{AB}}$ · $A+B=\overline{\overline A\,\overline B}$"

FORMULES = {
    "b11": r"NON-ET : $\overline{AB}$", "b12": r"NON-OU : $\overline{A+B}$", "b13": _XOR, "b14": r"$2^n$ lignes", "b15": r"$2^{2^n}$ fonctions de $n$ variables", "b16": _XOR + r" · NON-ET · NON-OU",
    "b21": _LOI, "b22": _LOI + r" · $A(A+B)=A+AB$", "b23": _LOI, "b24": _LOI, "b25": r"$A+B\overline B=A$ · distributivité $A+BC=(A+B)(A+C)$", "b26": _LOI,
    "b31": _MOR, "b32": _MOR, "b33": _MOR + r" · $A.\overline A=0$", "b34": _MOR + r" · $\overline{\overline A}=A$", "b35": _MOR + r" · $X+\overline X=1$",
    "b41": _LOI, "b42": r"$A+BC=(A+B)(A+C)$ · absorption", "b43": _LOI, "b44": r"mise en facteur · $X+\overline X=1$", "b45": r"$A+BC=(A+B)(A+C)$ · absorption", "b46": _LOI,
    "b51": _CAN, "b52": _CAN, "b53": _CAN + r" · $(A+B)(B+C)=B+AC$", "b54": _CAN, "b55": r"$|A+B|=4+4-2$", "b56": _CAN,
    "b61": _K3, "b62": _K3 + r" · Φ facultatifs", "b63": _K3, "b64": _K3, "b65": _K3, "b66": _K3,
    "b71": _K4, "b72": _K4, "b73": _K4, "b74": _K4, "b75": _K4 + r" · 4 coins adjacents", "b76": _K4,
    "b81": _K4, "b82": _K4, "b83": _K4, "b84": _K4, "b85": _XOR, "b86": _XOR + r" · $B\overline{CD}+\overline BCD=B\oplus CD$",
    "b91": _PRO, "b92": _PRO, "b93": _PRO + " · " + _K3, "b94": _PRO + " · " + _K4, "b95": _PRO + " · " + _K4, "b96": _PRO,
    "b101": _NAND, "b102": _NAND, "b103": _NAND, "b104": _NAND + r" · $A\oplus B=\overline{\overline{A\overline{AB}}\ \overline{B\overline{AB}}}$", "b105": _NAND + " · " + _XOR, "b106": _NAND,
    "bx1": _LOI + " · " + _MOR, "bx2": _CAN, "bx3": _K4 + " · " + _XOR, "bx4": _PRO + " · " + _K3, "bx5": _NAND,
    "by1": _K4, "by2": _K4 + " · " + _XOR, "by3": _XOR + r" · parité", "by4": _XOR + r" · Karnaugh en damier", "by5": _XOR + " · " + _MOR,
}
