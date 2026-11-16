"""Level path: S1 computer architecture, number systems (bases, binary arithmetic, two's complement, IEEE 754).

Calibrated on the Moodle course « Archi S1 - Promo 2030 » (chapters 1 and 2, `Chapitre_1.pdf`, `Chapitre_2.pdf`)
and on the exams `b1_exam_fr.pdf` (2025/2026, B1) and `s1_exam2_fr.pdf`. Answers are checked by `build.py`
with the helpers `bits`, `hexa`, `octal`, `tc`, `f32`, `f32d`, `f64d` (`calc` = independent decimal computation,
`ans` = the result written in `sol`). `open` ones have a model answer.
"""

SUBJECT = {
    "id": "archi-s1-numeration",
    "ordre": 400,
    "matiere": "archi",
    "semestre": "S1",
    "ecue": "Numération",
    "titre": "Numération et arithmétique des ordinateurs",
    "chapitres_moodle": ["01_Numération [2526_I_INF_FISE_S01_PR_NUM]", "02_Documents de cours", "03_Travaux Dirigés"],
    "td": "TD d'architecture (Moodle Archi S1)",
    "examens": ["Examen B1 d'architecture des ordinateurs"],
}

NOTIONS = [
    {"id": "bases", "titre": "Bases 2, 8, 16 vers le décimal",
     "formule": r"$N=\sum_i a_i\,b^i$ · binaire : poids $1,2,4,8,16,32,64,128,256$ · hexadécimal : $A=10,\dots,F=15$, poids $1,16,256$ · octal : poids $1,8,64$",
     "exemple": r"$1101_2=8+4+1=13$ · $1A5_{16}=256+160+5=421$",
     "cours": r"Chaque chiffre est multiplié par la puissance de la base qui correspond à sa position (la plus à droite est $b^0$). Savoir par cœur les puissances de 2 jusqu'à $2^{10}=1024$."},
    {"id": "division", "titre": "Décimal vers une autre base",
     "formule": r"partie entière : divisions successives par $b$, restes lus de bas en haut · $528_{10}=210_{16}$ · hexa $\leftrightarrow$ décimal : $16^2=256$",
     "exemple": r"$213=128+64+16+4+1=1101\,0101_2$",
     "cours": r"On divise jusqu'à obtenir un quotient nul. Le premier reste est le chiffre de poids faible. Pour le binaire, on peut aussi soustraire les plus grandes puissances de 2."},
    {"id": "groupes", "titre": "Binaire, octal et hexadécimal",
     "formule": r"hexa = groupes de $4$ bits · octal = groupes de $3$ bits · groupes à partir de la virgule, vers la gauche pour la partie entière, vers la droite pour la fraction · $0\,0000\ldots F\,1111$",
     "exemple": r"$1011\,1011_2=BB_{16}$ · $3D7_{16}=001\,111\,010\,111_2=1727_8$",
     "cours": r"Pas de calcul : on remplace chaque chiffre hexa par 4 bits (ou chaque chiffre octal par 3). Compléter par des zéros les groupes incomplets : à gauche pour la partie entière, à droite pour la fraction."},
    {"id": "fractions", "titre": "Nombres à virgule",
     "formule": r"poids après la virgule : $2^{-1}=0{,}5$, $2^{-2}=0{,}25$, $2^{-3}=0{,}125$, $2^{-4}=0{,}0625$, $2^{-5}=0{,}03125$ · fraction décimale $\to$ base $b$ : multiplications successives par $b$, parties entières lues de haut en bas",
     "exemple": r"$0{,}35\to0{,}7;\ 1{,}4;\ 0{,}8;\ 1{,}6;\ 1{,}2$ donne $0{,}01011\ldots_2$",
     "cours": r"On convertit séparément la partie entière et la partie fractionnaire. La conversion peut ne jamais se terminer : on s'arrête à la précision demandée (nombre de chiffres)."},
    {"id": "addition", "titre": "Addition en base 2 et 16",
     "formule": r"binaire : $0+0=0$, $0+1=1$, $1+1=10$ (retenue $1$), $1+1+1=11$ · hexa : somme $\ge16\Rightarrow$ retrancher $16$ et retenue $1$",
     "exemple": r"$1011_2+0110_2=10001_2$ · $2F_{16}+1D_{16}=4C_{16}$",
     "cours": r"Même méthode qu'en décimal, colonne par colonne de la droite vers la gauche, avec la retenue. En hexadécimal, convertir chaque chiffre en décimal, additionner, puis réécrire."},
    {"id": "soustraction", "titre": "Soustraction en base 2 et 16",
     "formule": r"binaire : $0-1\to$ emprunt : $10-1=1$ · hexa : emprunt de $16$ · vérification : résultat $+$ soustrahende $=$ nombre de départ",
     "exemple": r"$1101001_2-110110_2=110011_2$ ($105-54=51$)",
     "cours": r"Quand le chiffre du haut est plus petit que celui du bas, on emprunte une unité à gauche, qui vaut 2 (ou 16) dans la colonne courante. Toujours vérifier avec l'addition."},
    {"id": "produit", "titre": "Multiplication et division en base 2",
     "formule": r"multiplication : somme des multiplicandes décalés pour chaque $1$ du multiplicateur · $\times2^k$ = décalage à gauche de $k$ rangs · division : poser comme en décimal, quotient $1$ si le diviseur « rentre »",
     "exemple": r"$10110_2\times101_2=1101110_2$ ($22\times5=110$)",
     "cours": r"Chaque chiffre du multiplicateur vaut 0 (ligne nulle) ou 1 (multiplicande décalé). Multiplier ou diviser par une puissance de 2 revient à décaler la virgule."},
    {"id": "capacite", "titre": "Capacité d'un mot de n bits",
     "formule": r"$2^n$ valeurs · non signé : $[0,\ 2^n-1]$ · signé (complément à deux) : $[-2^{n-1},\ 2^{n-1}-1]$ · $8$ bits : $256$ valeurs · $n$ bits : $\lceil\log_2 N\rceil$ pour coder $N$ valeurs",
     "exemple": r"$8$ bits : $[0,255]$ ou $[-128,127]$ · $16$ bits non signé : $65\,535$",
     "cours": r"Le même mot binaire peut représenter deux nombres selon qu'on l'interprète en non signé ou en signé. Le nombre de bits est fixé : une opération qui sort de la plage donne un dépassement."},
    {"id": "cplt2", "titre": "Complément à deux",
     "formule": r"$-x$ : inverser tous les bits de $x$ puis ajouter $1$ · bit de poids fort $=1\Rightarrow$ négatif · $N_{\text{signé}}=N_{\text{non signé}}-2^n$ si le bit de poids fort vaut $1$ · extension : recopier le bit de signe",
     "exemple": r"$-45$ sur 8 bits : $00101101\to11010010\to11010011$",
     "cours": r"Le complément à deux permet d'utiliser le même additionneur pour les nombres signés et non signés. $10000000$ est $-128$ sur 8 bits et n'a pas d'opposé représentable."},
    {"id": "depassement", "titre": "Dépassements non signé et signé",
     "formule": r"addition non signée : dépassement $\iff$ retenue sortante · soustraction non signée : dépassement $\iff$ emprunt ($A < B$) · signé : dépassement $\iff$ deux opérandes de même signe donnent un résultat de signe opposé",
     "exemple": r"$0111\,1111+1=1000\,0000$ : non signé $128$ correct, signé dépassement ($127+1$)",
     "cours": r"Le résultat binaire est le même dans les deux interprétations (on garde les 8 bits de poids faible), mais le dépassement se juge séparément selon l'interprétation. Écrire « ERREUR » si le résultat n'est pas représentable."},
    {"id": "ieee", "titre": "Flottants IEEE 754 simple précision",
     "formule": r"$32$ bits : $S$ ($1$) $|$ $E$ ($8$) $|$ $M$ ($23$) · $x=(-1)^S\times1{,}M\times2^{E-127}$ · biais $127$ · normaliser : $x=\pm1{,}f\times2^e$ puis $E=e+127$",
     "exemple": r"$320=1{,}01_2\times2^8$ : $S=0$, $E=135=1000\,0111$, $M=0100\ldots0$, soit $43A00000_{16}$",
     "cours": r"On écrit la valeur absolue en binaire, on décale la virgule pour avoir un seul $1$ devant, l'exposant est le nombre de rangs décalés. Le $1$ de tête n'est pas stocké (bit caché). Le signe est dans $S$, pas dans la mantisse."},
    {"id": "ieeedec", "titre": "Décodage et cas particuliers IEEE 754",
     "formule": r"double précision : $1|11|52$, biais $1023$ · $E=0,M=0$ : $\pm0$ · $E$ max, $M=0$ : $\pm\infty$ · $E$ max, $M\ne0$ : NaN · $E=0,M\ne0$ : dénormalisé $(-1)^S\times0{,}M\times2^{-126}$",
     "exemple": r"$41A00000_{16}$ : $S=0$, $E=131$, $M=0{,}25$ : $1{,}25\times2^4=20$",
     "cours": r"Pour décoder : séparer les trois champs en binaire, retrancher le biais à $E$, rajouter le $1$ caché à la mantisse. Vérifier d'abord les cas particuliers avant d'appliquer la formule."},
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


B1 = "Examen B1 d'architecture 2025/2026"
S12 = "Examen 2 d'architecture S1 2024/2025"

LEVELS = [
    {"n": 1, "titre": "Binaire, octal, hexa vers décimal", "notions": ["bases"], "exos": [
        v("n11", r"Convertir $1011\,0110_2$ en décimal.", "128+32+16+4+2", "bits('10110110')", r"$128+32+16+4+2=182$.", duree=2),
        v("n12", r"Convertir $1A5_{16}$ en décimal.", "256+10*16+5", "hexa('1A5')", r"$1\times256+10\times16+5=421$.", src=B1 + ", ex. 1", duree=2),
        v("n13", r"Convertir $725_8$ en décimal.", "7*64+2*8+5", "octal('725')", r"$7\times64+2\times8+5=469$.", duree=2),
        v("n14", r"Convertir $1\,0110\,1101_2$ en décimal.", "256+64+32+8+4+1", "bits('101101101')", r"$256+64+32+8+4+1=365$.", src=B1 + ", ex. 1", duree=2),
        v("n15", r"Quelle est la valeur décimale de $1111\,1111_2$ ?", "2**8-1", "bits('11111111')", r"$2^8-1=255$.", duree=1),
    ]},
    {"n": 2, "titre": "Décimal vers binaire et hexa", "notions": ["division", "bases"], "exos": [
        v("n21", r"Convertir $213$ en binaire (sur 8 bits).", "213", "bits('11010101')",
          r"$213=128+64+16+4+1=1101\,0101_2$.", duree=3),
        v("n22", r"Convertir $528$ en hexadécimal.", "528", "hexa('210')", r"$528=2\times256+1\times16+0$, soit $210_{16}$.", src=B1 + ", ex. 1", duree=3),
        v("n23", r"Convertir $1000$ en hexadécimal.", "1000", "hexa('3E8')", r"$1000=3\times256+14\times16+8$, soit $3E8_{16}$.", duree=3),
        v("n24", r"Convertir $255$ en binaire.", "255", "bits('11111111')", r"$255=2^8-1=1111\,1111_2$.", duree=1),
        o("n25", r"Convertir $715$ en binaire par divisions successives, puis en hexadécimal.",
          r"$715=2\times357+1$ ; $357=2\times178+1$ ; $178=2\times89+0$ ; $89=2\times44+1$ ; $44=2\times22+0$ ; $22=2\times11+0$ ; $11=2\times5+1$ ; $5=2\times2+1$ ; $2=2\times1+0$ ; $1=2\times0+1$." "\n\n"
          r"Restes lus de bas en haut : $715=10\,1100\,1011_2=2CB_{16}$.", src="Cours chapitre 1, § 2.3", duree=6),
    ]},
    {"n": 3, "titre": "Binaire, octal et hexadécimal", "notions": ["groupes"], "exos": [
        v("n31", r"Convertir $1011\,1011_2$ en hexadécimal.", "187", "hexa('BB')", r"$1011=B$, $1011=B$ : $BB_{16}=187$.", duree=2),
        v("n32", r"Convertir $3D7_{16}$ en binaire.", "983", "bits('1111010111')", r"$3=0011$, $D=1101$, $7=0111$ : $0011\,1101\,0111_2=11\,1101\,0111_2$ ($983$).", duree=2),
        v("n33", r"Convertir $1010011_2$ en octal.", "83", "octal('123')", r"Groupes de 3 : $001\ 010\ 011=123_8$ ($83$).", duree=2),
        v("n34", r"Convertir $235_8$ en binaire.", "157", "bits('10011101')", r"$2=010$, $3=011$, $5=101$ : $010\,011\,101=1001\,1101_2$ ($157$).", duree=2),
        v("n35", r"Convertir $3D7_{16}$ en octal (passer par le binaire).", "983", "octal('1727')", r"$0011\,1101\,0111=001\ 111\ 010\ 111$ : $1727_8$.", duree=3),
    ]},
    {"n": 4, "titre": "Nombres à virgule", "notions": ["fractions", "groupes"], "exos": [
        v("n41", r"Convertir $1101{,}1000\,1_2$ en décimal.", "13+Rational(17,32)", "bits('1101.10001')", r"$13+\frac12+\frac1{32}=13{,}53125$.", src=B1 + ", ex. 1", duree=3),
        v("n42", r"Convertir $28{,}28_{16}$ en décimal.", "40+Rational(5,32)", "hexa('28.28')", r"$2\times16+8=40$ et $\frac{2}{16}+\frac{8}{256}=0{,}15625$ : $40{,}15625$.", src=B1 + ", ex. 1", duree=3),
        v("n43", r"Convertir $40{,}35$ en binaire avec $5$ chiffres après la virgule (troncature). Valeur décimale exacte du résultat ?", "40+Rational(11,32)", "bits('101000.01011')",
          r"$40=101000_2$. $0{,}35\times2=0{,}7\ (0)$ ; $0{,}7\times2=1{,}4\ (1)$ ; $0{,}4\times2=0{,}8\ (0)$ ; $0{,}8\times2=1{,}6\ (1)$ ; $0{,}6\times2=1{,}2\ (1)$ : $101000{,}01011_2=40{,}34375$.", src=B1 + ", ex. 1", duree=4),
        v("n44", r"Convertir $22{,}84$ en hexadécimal avec $2$ chiffres après la virgule (troncature). Valeur décimale exacte ?", "22+Rational(13*16+7,256)", "hexa('16.D7')",
          r"$22=16_{16}$. $0{,}84\times16=13{,}44\ (D)$ ; $0{,}44\times16=7{,}04\ (7)$ : $16{,}D7_{16}$.", src=B1 + ", ex. 1", duree=4),
        v("n45", r"Convertir $1011\,1011{,}1011\,01_2$ en hexadécimal.", "187+Rational(45,64)", "hexa('BB.B4')", r"Partie entière : $BB$. Fraction : $1011\ 01\to1011\ 0100=B4$. Résultat $BB{,}B4_{16}$.", src=B1 + ", ex. 1", duree=3),
        o("n46", r"Pourquoi $0{,}1_{10}$ n'a-t-il pas d'écriture finie en binaire ?",
          r"$0{,}1\times2=0{,}2$, $0{,}2\times2=0{,}4$, $0{,}4\times2=0{,}8$, $0{,}8\times2=1{,}6$, $0{,}6\times2=1{,}2$, $0{,}2\ldots$ : on retrouve $0{,}2$, la suite des chiffres se répète indéfiniment ($0{,}0001\,1001\,1001\ldots_2$). Une fraction a une écriture finie en base 2 seulement si son dénominateur (irréductible) est une puissance de 2.", duree=5),
    ]},
    {"n": 5, "titre": "Addition en base 2 et 16", "notions": ["addition", "bases"], "exos": [
        v("n51", r"Calculer $1011_2+0110_2$.", "11+6", "bits('10001')", r"$11+6=17=1\,0001_2$.", duree=2),
        v("n52", r"Calculer $101101_2+110111_2$.", "45+55", "bits('1100100')", r"$45+55=100=110\,0100_2$.", duree=3),
        v("n53", r"Calculer $763_{16}+FAA_{16}$.", "1891+4010", "hexa('170D')", r"$3+A=D$ ; $6+A=16=10_{16}$ : écrire $0$, retenue $1$ ; $7+F+1=23=17_{16}$ : écrire $7$, retenue $1$ ; reste $1$. Résultat $170D_{16}$.", src=B1 + ", ex. 2", duree=4),
        v("n54", r"Calculer $2F_{16}+1D_{16}$.", "47+29", "hexa('4C')", r"$F+D=15+13=28=1C_{16}$ : $C$, retenue $1$ ; $2+1+1=4$ : $4C_{16}$.", duree=2),
        v("n55", r"Calculer $1111_2+1_2$.", "15+1", "bits('10000')", r"La retenue se propage jusqu'au bout : $1\,0000_2$.", duree=1),
    ]},
    {"n": 6, "titre": "Soustraction en base 2 et 16", "notions": ["soustraction", "addition"], "exos": [
        v("n61", r"Calculer $1101001_2-110110_2$.", "105-54", "bits('110011')", r"$105-54=51=110011_2$ (vérifier : $110011+110110=1101001$).", src="Cours chapitre 1, § 3.2", duree=4),
        v("n62", r"Calculer $1\,0111\,0110_2-1101\,1011_2$.", "374-219", "bits('10011011')", r"$374-219=155=1001\,1011_2$.", src=B1 + ", ex. 2", duree=4),
        v("n63", r"Calculer $A3_{16}-5F_{16}$.", "163-95", "hexa('44')", r"$3-F$ : emprunt, $19-15=4$ ; $A-1-5=4$ : $44_{16}$.", duree=3),
        v("n64", r"Calculer $1000_{16}-1_{16}$.", "4096-1", "hexa('FFF')", r"Les emprunts se propagent : $FFF_{16}$.", duree=2),
        v("n65", r"Calculer $1\,0000_2-1_2$.", "16-1", "bits('1111')", r"$16-1=15=1111_2$.", duree=1),
    ]},
    {"n": 7, "titre": "Multiplication et division", "notions": ["produit", "addition"], "exos": [
        v("n71", r"Calculer $10110_2\times101_2$.", "22*5", "bits('1101110')", r"$10110+1011000=1101110_2$ ($22\times5=110$).", src="Cours chapitre 1, § 3.3", duree=4),
        v("n72", r"Calculer $1011_2\times11_2$.", "11*3", "bits('100001')", r"$1011+10110=100001_2$ ($33$).", duree=3),
        v("n73", r"Calculer $1101_2\times1010_2$.", "13*10", "bits('10000010')", r"$1101\times1010$ : $0+11010+0+1101000=10000010_2$ ($130$).", duree=4),
        v("n74", r"Quotient de la division euclidienne de $1100100_2$ par $110_2$ (en décimal) ?", "100//6", "bits('10000')", r"$100=16\times6+4$ : quotient $10000_2$ ($16$), reste $100_2$ ($4$).", duree=4),
        v("n75", r"Calculer $1F_{16}\times3_{16}$.", "31*3", "hexa('5D')", r"$F\times3=45=2D_{16}$ : $D$, retenue $2$ ; $1\times3+2=5$ : $5D_{16}$.", duree=3),
    ]},
    {"n": 8, "titre": "Capacité d'un mot de n bits", "notions": ["capacite"], "exos": [
        v("n81", r"Combien de valeurs différentes sur $8$ bits ?", "2**8", "256", r"$2^8=256$.", duree=1),
        v("n82", r"Plus grand entier non signé sur $10$ bits ?", "2**10-1", "1023", r"$2^{10}-1=1023$.", duree=1),
        v("n83", r"Nombre minimal de bits pour coder $1000$ valeurs différentes ?", "10", "10", r"$2^9=512<1000\le2^{10}=1024$ : $10$ bits.", duree=2),
        v("n84", r"Combien de chiffres hexadécimaux pour $32$ bits ?", "32//4", "8", r"$4$ bits par chiffre : $8$ chiffres.", duree=1),
        v("n85", r"Plus grand entier non signé sur $16$ bits ?", "2**16-1", "65535", r"$2^{16}-1=65\,535$.", duree=1),
        v("n86", r"Plage signée sur $8$ bits : plus petite valeur ?", "-2**7", "-128", r"$-2^{n-1}=-128$.", duree=1),
    ]},
    {"n": 9, "titre": "Complément à deux", "notions": ["cplt2", "capacite"], "exos": [
        v("n91", r"Valeur signée (complément à deux) de $1001\,1100_2$ sur $8$ bits ?", "156-256", "tc('10011100')", r"Non signé $156$, bit de poids fort à $1$ : $156-256=-100$.", src=B1 + ", ex. 3", duree=2),
        v("n92", r"Représenter $-45$ en complément à deux sur $8$ bits. Valeur non signée du mot obtenu ?", "256-45", "bits('11010011')", r"$45=0010\,1101$, inversion $1101\,0010$, plus $1$ : $1101\,0011_2=211$.", duree=3),
        v("n93", r"Valeur signée de $1000\,0000_2$ sur $8$ bits ?", "-128", "tc('10000000')", r"$128-256=-128$ : plus petite valeur de la plage.", duree=1),
        v("n94", r"Valeur signée de $1111\,1111_2$ sur $8$ bits ?", "-1", "tc('11111111')", r"$255-256=-1$.", duree=1),
        v("n95", r"Étendre $1010_2$ (signé, $4$ bits) sur $8$ bits. Valeur signée ?", "-6", "tc('11111010')", r"On recopie le bit de signe : $1111\,1010_2=-6$.", duree=2),
        o("n96", r"Montrer que, pour $x$ sur $n$ bits, inverser tous les bits puis ajouter $1$ donne $-x$ modulo $2^n$.",
          r"Inverser tous les bits revient à calculer $(2^n-1)-x$, car $x+\bar x=11\ldots1=2^n-1$." "\n\n"
          r"Ajouter $1$ donne $2^n-x\equiv-x\pmod{2^n}$.", duree=5),
    ]},
    {"n": 10, "titre": "Dépassements sur 8 bits", "notions": ["depassement", "cplt2", "addition", "soustraction"], "exos": [
        v("n101", r"$0111\,0110+0001\,1001$ sur $8$ bits : résultat non signé (décimal) ?", "118+25", "143", r"$118+25=143\le255$, pas de retenue sortante : $1000\,1111_2=143$. (En signé : $118+25=143>127$, dépassement.)", src=B1 + ", ex. 3", duree=3),
        v("n102", r"$1101\,0011-0001\,0110$ sur $8$ bits : résultat signé (décimal) ?", "-45-22", "-67", r"$-45-22=-67\in[-128,127]$ : $1011\,1101_2$ ($189$ non signé).", src=B1 + ", ex. 3", duree=4),
        v("n103", r"$0011\,0010+0100\,0110$ sur $8$ bits : résultat signé (décimal) ?", "50+70", "tc('01111000')", r"$50+70=120\le127$ : $0111\,1000_2=120$, aucun dépassement.", duree=3),
        o("n104", r"$0101\,0100-1001\,1100$ sur $8$ bits : donner le résultat binaire, puis la valeur non signée et la valeur signée (« ERREUR » en cas de dépassement).",
          r"$84-156=-72$ : en binaire sur 8 bits, $0101\,0100-1001\,1100=1011\,1000_2$." "\n\n"
          r"Non signé : $84<156$, il y a un emprunt : ERREUR." "\n\n"
          r"Signé : $84-(-100)=184>127$ : ERREUR.", src=B1 + ", ex. 3", duree=6),
        o("n105", r"$0111\,1111+0000\,0001$ puis $1111\,1111+0000\,0001$ sur $8$ bits : résultat binaire, valeur non signée et valeur signée.",
          r"$0111\,1111+1=1000\,0000$ : non signé $128$ (correct) ; signé : deux positifs donnent un négatif, ERREUR ($127+1$)." "\n\n"
          r"$1111\,1111+1=1\,0000\,0000$, sur 8 bits $0000\,0000$ avec retenue sortante : non signé ERREUR ($255+1$) ; signé $0$ ($-1+1$), correct.", duree=6),
        o("n106", r"Donner le critère de dépassement d'une addition sur $n$ bits en non signé, puis en signé.",
          r"Non signé : dépassement si et seulement si il y a une retenue sortante du bit de poids fort ($A+B\ge2^n$)." "\n\n"
          r"Signé : dépassement si et seulement si $A$ et $B$ ont le même bit de signe et que le résultat a un bit de signe différent (deux positifs donnent un négatif, ou deux négatifs donnent un positif). Une addition de signes opposés ne peut pas déborder.", duree=5),
    ]},
    {"n": 11, "titre": "Flottants IEEE 754 simple précision", "notions": ["ieee", "fractions"], "exos": [
        v("n111", r"Écrire $320$ en IEEE 754 simple précision. Donner le mot en hexadécimal (valeur décimale pour contrôle).", "f32(320)", "hexa('43A00000')",
          r"$320=256+64=1{,}25\times2^8$ : $S=0$, $E=8+127=135=1000\,0111$, $M=01\,0000\ldots$ : $0\ 10000111\ 0100\ldots0=43A00000_{16}$.", src=B1 + ", ex. 4", duree=5),
        v("n112", r"Écrire $0{,}09375$ en IEEE 754 simple précision (hexadécimal).", "f32(0.09375)", "hexa('3DC00000')",
          r"$0{,}09375=\frac3{32}=1{,}1_2\times2^{-4}$ : $S=0$, $E=-4+127=123=0111\,1011$, $M=1000\ldots0$ : $3DC00000_{16}$.", src=B1 + ", ex. 4", duree=5),
        v("n113", r"Écrire $-6{,}5$ en IEEE 754 simple précision (hexadécimal).", "f32(-6.5)", "hexa('C0D00000')",
          r"$6{,}5=110{,}1_2=1{,}101_2\times2^2$ : $S=1$, $E=129=1000\,0001$, $M=101\,0\ldots0$ : $C0D00000_{16}$.", duree=5),
        v("n114", r"Écrire $12{,}375$ en IEEE 754 simple précision (hexadécimal).", "f32(12.375)", "hexa('41460000')",
          r"$12{,}375=1100{,}011_2=1{,}100011_2\times2^3$ : $E=130=1000\,0010$, $M=1000\,11\ldots$ : $41460000_{16}$.", duree=5),
        v("n115", r"Écrire $-0{,}15625$ en IEEE 754 simple précision (hexadécimal).", "f32(-0.15625)", "hexa('BE200000')",
          r"$0{,}15625=\frac5{32}=1{,}01_2\times2^{-3}$ : $S=1$, $E=124=0111\,1100$, $M=01\,0\ldots$ : $BE200000_{16}$.", duree=5),
        o("n116", r"Pourquoi $0{,}1$ n'est-il pas représenté exactement en simple précision ? Donner l'ordre de grandeur de l'erreur.",
          r"$0{,}1$ n'a pas d'écriture binaire finie (voir niveau 4) : la mantisse de $23$ bits est tronquée ou arrondie. On obtient $3DCCCCCD_{16}\approx0{,}100000001490116$. L'erreur relative est au plus $2^{-24}\approx6\times10^{-8}$.", duree=5),
    ]},
    {"n": 12, "titre": "Décodage et cas particuliers", "notions": ["ieeedec", "ieee"], "exos": [
        v("n121", r"Quelle valeur décimale représente le mot simple précision $41A00000_{16}$ ?", "20", "f32d('41A00000')",
          r"$0100\,0001\,1010\ldots$ : $S=0$, $E=1000\,0011=131$, $M=0100\ldots=0{,}25$ : $1{,}25\times2^{4}=20$.", duree=4),
        v("n122", r"Valeur de $C1200000_{16}$ (simple précision) ?", "-10", "f32d('C1200000')",
          r"$S=1$, $E=1000\,0010=130$, $M=0100\ldots$ : $-1{,}25\times2^3=-10$.", duree=4),
        v("n123", r"Valeur de $3F000000_{16}$ (simple précision) ?", "Rational(1,2)", "f32d('3F000000')",
          r"$S=0$, $E=0111\,1110=126$, $M=0$ : $1\times2^{-1}=0{,}5$.", duree=3),
        v("n124", r"Représentation associée au mot double précision $2844\,0000\,0000\,0000_{16}$, sous la forme $k\times2^n$ ?", "5*2**(-381)", "f64d('2844000000000000')",
          r"$S=0$, $E=284_{16}=644$, $644-1023=-379$, $M=0100\ldots=0{,}25$ : $1{,}25\times2^{-379}=5\times2^{-381}$.", src=B1 + ", ex. 4", duree=6),
        o("n125", r"Représentation associée au mot double précision $7FF0\,0001\,0000\,0000_{16}$ ?",
          r"$E=7FF_{16}=2047$ (tous les bits à $1$) et $M\ne0$ : ce n'est pas un nombre, c'est NaN (Not a Number).", src=B1 + ", ex. 4", duree=3),
        o("n126", r"Que représentent les mots simple précision $0000\,0000_{16}$, $8000\,0000_{16}$, $7F80\,0000_{16}$ et $FF80\,0000_{16}$ ?",
          r"$0000\,0000_{16}$ : $E=0,M=0$ : $+0$. $8000\,0000_{16}$ : $-0$. $7F80\,0000_{16}$ : $E=255,M=0$ : $+\infty$. $FF80\,0000_{16}$ : $-\infty$.", duree=4),
    ]},
    {"n": 13, "titre": "Niveau examen : sujet B1", "notions": ["bases", "fractions", "addition", "soustraction", "depassement", "ieee", "ieeedec"], "examen": True, "exos": [
        o("nx1", r"Convertir : $1\,0110\,1101_2$ en décimal ; $1A5_{16}$ en décimal ; $528$ en hexa ; $1101{,}1000\,1_2$ en décimal ; $28{,}28_{16}$ en décimal ; $40{,}35$ en binaire ($5$ chiffres après la virgule) ; $22{,}84$ en hexa ($2$ chiffres) ; $1011\,1011{,}1011\,01_2$ en hexa.",
          r"$365$ ; $421$ ; $210_{16}$ ; $13{,}53125$ ; $40{,}15625$ ; $101000{,}01011_2$ ; $16{,}D7_{16}$ ; $BB{,}B4_{16}$.", src=B1 + ", ex. 1 (4 points)", duree=12),
        o("nx2", r"Effectuer : $1\,0111\,0110_2-1101\,1011_2$ ; $763_{16}+FAA_{16}$ ; $1010\,1010\,100_2\times10\,1010_2$.",
          r"$1001\,1011_2$ ($374-219=155$) ; $170D_{16}$ ; $1364\times42=57\,288=1101\,1111\,1100\,1000_2$.", src=B1 + ", ex. 2 (adapté, 6 points)", duree=12),
        o("nx3", r"Sur $8$ bits, effectuer $0101\,0100-1001\,1100$, $0111\,0110+0001\,1001$, $1101\,0011-0001\,0110$ et donner le résultat binaire, la valeur non signée et la valeur signée (« ERREUR » si dépassement).",
          r"$1011\,1000$ : non signé ERREUR, signé ERREUR." "\n\n"
          r"$1000\,1111$ : non signé $143$, signé ERREUR." "\n\n"
          r"$1011\,1101$ : non signé $189$, signé $-67$.", src=B1 + ", ex. 3 (6 points)", duree=12),
        o("nx4", r"1. Convertir $320$ et $0{,}09375$ en IEEE 754 simple précision (champs $S$, $E$, $M$). 2. Interpréter en double précision $2844\,0000\,0000\,0000_{16}$ et $7FF0\,0001\,0000\,0000_{16}$ (forme $k\times2^n$ si nombre).",
          r"1. $320$ : $S=0$, $E=1000\,0111$, $M=010\ldots0$. $0{,}09375$ : $S=0$, $E=0111\,1011$, $M=10\ldots0$." "\n\n"
          r"2. $5\times2^{-381}$ et NaN.", src=B1 + ", ex. 4 (4 points)", duree=12),
    ]},
    {"n": 14, "titre": "Examen + 20 %", "notions": ["ieee", "depassement", "cplt2", "capacite"], "examen": True, "exos": [
        v("ny1", r"Écrire $18{,}25$ en IEEE 754 simple précision (hexadécimal).", "f32(18.25)", "hexa('41920000')",
          r"$18{,}25=10010{,}01_2=1{,}001001_2\times2^4$ : $E=131=1000\,0011$, $M=0010\,01\ldots$ : $41920000_{16}$.", duree=6),
        v("ny2", r"Écrire $-2$ en IEEE 754 simple précision (hexadécimal).", "f32(-2)", "hexa('C0000000')", r"$-2=-1{,}0\times2^1$ : $S=1$, $E=128=1000\,0000$, $M=0$ : $C0000000_{16}$.", duree=4),
        v("ny3", r"Plus petit entier positif non représentable exactement en simple précision (indice : $24$ bits significatifs) ?", "2**24+1", "16777217",
          r"Un entier $n\le2^{24}$ tient sur $24$ bits significatifs. $2^{24}+1=1\,0000\ldots01_2$ en demande $25$ : non représentable.", duree=5),
        o("ny4", r"Donner la représentation IEEE 754 double précision de $1{,}5$ (hexadécimal) et de $-0$.",
          r"$1{,}5=1{,}1_2\times2^0$ : $S=0$, $E=1023=011\,1111\,1111$, $M=1000\ldots$ : $3FF8\,0000\,0000\,0000_{16}$." "\n\n"
          r"$-0$ : $S=1$, $E=0$, $M=0$ : $8000\,0000\,0000\,0000_{16}$.", duree=6),
        o("ny5", r"Sur $8$ bits, calculer $1000\,0000-0000\,0001$ puis $0101\,1010+0110\,0110$. Donner le résultat binaire, la valeur non signée et signée (« ERREUR » en cas de dépassement).",
          r"$1000\,0000-0000\,0001=0111\,1111$ : non signé $127$ (pas d'emprunt) ; signé : $-128-1=-129$ ERREUR." "\n\n"
          r"$0101\,1010+0110\,0110=1100\,0000$ : non signé $192$ ; signé : $90+102=192>127$, ERREUR.", duree=8),
    ]},
]


def _v(enonce, calc, ans, sol):
    return {"enonce": enonce, "calc": calc, "ans": ans, "sol": sol}


VARIANTS = {
    "n11": [_v(r"Convertir $1100\,1010_2$ en décimal.", "128+64+8+2", "bits('11001010')", r"$128+64+8+2=202$.")],
    "n12": [_v(r"Convertir $2F3_{16}$ en décimal.", "2*256+15*16+3", "hexa('2F3')", r"$512+240+3=755$.")],
    "n13": [_v(r"Convertir $614_8$ en décimal.", "6*64+8+4", "octal('614')", r"$384+8+4=396$.")],
    "n31": [_v(r"Convertir $1100\,1010_2$ en hexadécimal.", "202", "hexa('CA')", r"$1100=C$, $1010=A$ : $CA_{16}$.")],
    "n34": [_v(r"Convertir $164_8$ en binaire.", "116", "bits('1110100')", r"$1=001$, $6=110$, $4=100$ : $001\,110\,100=111\,0100_2$ ($116$).")],
    "n41": [_v(r"Convertir $101{,}011_2$ en décimal.", "5+Rational(3,8)", "bits('101.011')", r"$4+1+\frac14+\frac18=5{,}375$.")],
    "n51": [_v(r"Calculer $1101_2+0111_2$.", "13+7", "bits('10100')", r"$13+7=20=1\,0100_2$.")],
    "n53": [_v(r"Calculer $3AF_{16}+1C5_{16}$.", "943+453", "hexa('574')", r"$F+5=20=14_{16}$ : $4$, retenue $1$ ; $A+C+1=23=17_{16}$ : $7$, retenue $1$ ; $3+1+1=5$ : $574_{16}$.")],
    "n61": [_v(r"Calculer $1010100_2-100111_2$.", "84-39", "bits('101101')", r"$84-39=45=101101_2$.")],
    "n63": [_v(r"Calculer $B2_{16}-6D_{16}$.", "178-109", "hexa('45')", r"$178-109=69=45_{16}$.")],
    "n71": [_v(r"Calculer $1001_2\times110_2$.", "9*6", "bits('110110')", r"$9\times6=54=11\,0110_2$.")],
    "n81": [_v(r"Combien de valeurs différentes sur $12$ bits ?", "2**12", "4096", r"$2^{12}=4096$.")],
    "n83": [_v(r"Nombre minimal de bits pour coder $300$ valeurs différentes ?", "9", "9", r"$2^8=256<300\le512=2^9$ : $9$ bits.")],
    "n91": [_v(r"Valeur signée de $1100\,0101_2$ sur $8$ bits ?", "197-256", "tc('11000101')", r"$197-256=-59$.")],
    "n92": [_v(r"Représenter $-20$ en complément à deux sur $8$ bits. Valeur non signée du mot ?", "256-20", "bits('11101100')", r"$20=0001\,0100$, inversion $1110\,1011$, plus $1$ : $1110\,1100_2=236$.")],
    "n101": [_v(r"$0110\,0100+0010\,1000$ sur $8$ bits : résultat non signé (décimal) ?", "100+40", "140", r"$100+40=140\le255$ : $1000\,1100_2$.")],
    "n102": [_v(r"$1100\,0000-0001\,0000$ sur $8$ bits : résultat signé (décimal) ?", "-64-16", "-80", r"$-64-16=-80$ : $1011\,0000_2$.")],
    "n111": [_v(r"Écrire $5$ en IEEE 754 simple précision (hexadécimal).", "f32(5)", "hexa('40A00000')", r"$5=1{,}01_2\times2^2$ : $E=129$, $M=01\,0\ldots$ : $40A00000_{16}$.")],
    "n121": [_v(r"Valeur du mot simple précision $40400000_{16}$ ?", "3", "f32d('40400000')", r"$E=128$, $M=1000\ldots$ : $1{,}5\times2=3$.")],
}
for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["id"] in VARIANTS:
            _e["variants"] = VARIANTS[_e["id"]]


EXTRA_PARTS = []

QUIZ = [
    {"notion": "bases", "type": "qcm", "q": r"$1101_2$ vaut en décimal :", "choix": [r"13", r"11", r"15", r"9"], "bonne": 0},
    {"notion": "bases", "type": "vf", "q": r"En hexadécimal, le chiffre $F$ vaut $15$.", "bonne": True},
    {"notion": "division", "type": "qcm", "q": r"Pour convertir un entier décimal en binaire par divisions successives, on lit les restes :",
     "choix": [r"de bas en haut (dernier reste en premier)", r"de haut en bas", r"dans un ordre quelconque", r"seulement les restes égaux à $1$"], "bonne": 0},
    {"notion": "groupes", "type": "qcm", "q": r"Un chiffre hexadécimal correspond à combien de bits ?", "choix": [r"4", r"3", r"8", r"2"], "bonne": 0},
    {"notion": "groupes", "type": "vf", "q": r"Pour passer de l'hexadécimal à l'octal, on peut passer par le binaire.", "bonne": True},
    {"notion": "fractions", "type": "qcm", "q": r"Dans $0{,}101_2$, le dernier chiffre pèse :", "choix": [r"$0{,}125$", r"$0{,}25$", r"$0{,}5$", r"$0{,}0625$"], "bonne": 0},
    {"notion": "fractions", "type": "vf", "q": r"Tout nombre décimal à virgule finie a une écriture binaire finie.", "bonne": False},
    {"notion": "addition", "type": "qcm", "q": r"$1_2+1_2$ vaut :", "choix": [r"$10_2$", r"$11_2$", r"$2_2$", r"$0_2$ sans retenue"], "bonne": 0},
    {"notion": "soustraction", "type": "qcm", "q": r"En binaire, lors d'un emprunt, l'unité empruntée vaut dans la colonne courante :", "choix": [r"$2$", r"$10$", r"$1$", r"$16$"], "bonne": 0},
    {"notion": "produit", "type": "vf", "q": r"Multiplier un entier binaire par $2^k$ revient à décaler ses bits de $k$ rangs vers la gauche.", "bonne": True},
    {"notion": "capacite", "type": "qcm", "q": r"Plage des entiers signés (complément à deux) sur $8$ bits :", "choix": [r"$[-128,\ 127]$", r"$[-127,\ 127]$", r"$[-128,\ 128]$", r"$[0,\ 255]$"], "bonne": 0},
    {"notion": "capacite", "type": "vf", "q": r"Le même mot binaire peut représenter deux entiers différents selon qu'on l'interprète en signé ou en non signé.", "bonne": True},
    {"notion": "cplt2", "type": "qcm", "q": r"Pour obtenir l'opposé d'un entier en complément à deux :", "choix": [r"inverser les bits puis ajouter $1$", r"inverser les bits seulement", r"ajouter $1$ puis inverser les bits", r"changer le bit de poids fort"], "bonne": 0},
    {"notion": "cplt2", "type": "vf", "q": r"$1000\,0000_2$ a un opposé représentable sur $8$ bits.", "bonne": False},
    {"notion": "depassement", "type": "qcm", "q": r"Une addition non signée déborde si et seulement si :", "choix": [r"il y a une retenue sortante", r"le résultat est négatif", r"les opérandes sont de signes opposés", r"le résultat est nul"], "bonne": 0},
    {"notion": "depassement", "type": "vf", "q": r"Additionner deux nombres signés de signes opposés peut déborder.", "bonne": False},
    {"notion": "ieee", "type": "qcm", "q": r"Le biais de l'exposant en simple précision vaut :", "choix": [r"$127$", r"$128$", r"$1023$", r"$255$"], "bonne": 0},
    {"notion": "ieee", "type": "vf", "q": r"Le $1$ de tête de la mantisse normalisée est stocké dans les $23$ bits de $M$.", "bonne": False},
    {"notion": "ieeedec", "type": "qcm", "q": r"$E$ avec tous les bits à $1$ et $M\ne0$ désigne :", "choix": [r"NaN", r"$+\infty$", r"$0$", r"un nombre dénormalisé"], "bonne": 0},
    {"notion": "ieeedec", "type": "qcm", "q": r"Le biais en double précision vaut :", "choix": [r"$1023$", r"$127$", r"$2047$", r"$1024$"], "bonne": 0},
]

_BASE = r"$N=\sum_ia_ib^i$"
_DIV = r"divisions successives par $b$, restes de bas en haut"
_GRP = r"hexa : 4 bits · octal : 3 bits"
_FRAC = r"$2^{-1}=0{,}5$, $2^{-2}=0{,}25$, $2^{-3}=0{,}125$, $2^{-4}=0{,}0625$, $2^{-5}=0{,}03125$"
_ADD = r"$1+1=10_2$ (retenue) · hexa : $\ge16\Rightarrow$ retenue"
_SUB = r"emprunt : $10_2-1=1$ · vérifier par l'addition"
_MUL = r"somme des multiplicandes décalés · $\times2^k$ = décalage de $k$ rangs"
_CAP = r"$2^n$ valeurs · non signé $[0,2^n-1]$ · signé $[-2^{n-1},2^{n-1}-1]$"
_C2 = r"$-x$ = inverser les bits puis $+1$ · $N_{signé}=N_{non\ signé}-2^n$ si bit de poids fort $=1$"
_DEP = r"non signé : retenue sortante (ou emprunt) · signé : même signe en entrée, signe opposé en sortie"
_IEEE = r"$x=(-1)^S\times1{,}M\times2^{E-127}$ · biais $127$ · $1|8|23$"
_IEEED = r"double : $1|11|52$, biais $1023$ · $E$ max et $M\ne0$ : NaN · $E=0,M=0$ : $\pm0$"

FORMULES = {
    "n11": _BASE + r" · puissances de 2", "n12": _BASE + r" · $A=10,\dots,F=15$", "n13": _BASE + r" · poids $64,8,1$", "n14": _BASE, "n15": r"$2^n-1=11\ldots1_2$",
    "n21": _DIV + r" · ou soustraire les puissances de 2", "n22": _DIV, "n23": _DIV, "n24": r"$2^8-1=1111\,1111_2$", "n25": _DIV + " · " + _GRP,
    "n31": _GRP, "n32": _GRP, "n33": r"octal : groupes de 3 bits", "n34": r"octal : groupes de 3 bits", "n35": _GRP,
    "n41": _FRAC, "n42": r"$16^{-1}=0{,}0625$, $16^{-2}=0{,}00390625$ · " + _BASE, "n43": r"fraction $\to$ binaire : $\times2$, partie entière", "n44": r"fraction $\to$ hexa : $\times16$, partie entière",
    "n45": _GRP + r" · compléter la fraction par des zéros à droite", "n46": r"fraction $\to$ binaire : $\times2$, partie entière",
    "n51": _ADD, "n52": _ADD, "n53": _ADD + r" · $A=10$, $F=15$", "n54": _ADD, "n55": _ADD,
    "n61": _SUB, "n62": _SUB, "n63": _SUB + r" · emprunt de $16$", "n64": _SUB, "n65": _SUB,
    "n71": _MUL, "n72": _MUL, "n73": _MUL, "n74": r"division euclidienne : dividende $=$ quotient $\times$ diviseur $+$ reste", "n75": _MUL + r" · hexa : $F\times3=45=2D_{16}$",
    "n81": _CAP, "n82": _CAP, "n83": r"$\lceil\log_2N\rceil$ bits", "n84": r"1 chiffre hexa = 4 bits", "n85": _CAP, "n86": _CAP,
    "n91": _C2, "n92": _C2, "n93": _C2, "n94": _C2, "n95": r"extension de signe : recopier le bit de poids fort", "n96": r"$x+\bar x=2^n-1$ · $-x\equiv2^n-x$",
    "n101": _DEP, "n102": _DEP + r" · " + _C2, "n103": _DEP, "n104": _DEP + r" · " + _SUB, "n105": _DEP, "n106": _DEP,
    "n111": _IEEE + r" · $E=e+127$", "n112": _IEEE, "n113": _IEEE + r" · $S=1$ si négatif", "n114": _IEEE + " · " + _FRAC, "n115": _IEEE + " · " + _FRAC, "n116": _FRAC + r" · fraction $\to$ binaire : $\times2$",
    "n121": _IEEE, "n122": _IEEE, "n123": _IEEE, "n124": _IEEED, "n125": _IEEED, "n126": _IEEED,
    "nx1": _BASE + r" · " + _DIV + r" · " + _GRP, "nx2": _SUB + r" · " + _ADD + r" · " + _MUL, "nx3": _DEP + r" · " + _C2, "nx4": _IEEE + r" · " + _IEEED,
    "ny1": _IEEE + r" · " + _FRAC, "ny2": _IEEE, "ny3": r"24 bits significatifs (1 caché + 23)", "ny4": _IEEED, "ny5": _DEP + r" · " + _C2,
}
