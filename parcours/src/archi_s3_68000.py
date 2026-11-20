"""Level path: S3 computer architecture, the basics of 68000 assembly (« Les bases de l'assembleur 68000 »).

ECUE ASM68K (code chosen by the path: the Moodle course is called « Les bases de l'assembleur 68000 », the exams are the
« Contrôle S3 » (mid-semester) and the « Partiel S3 » (final) of « Architecture des ordinateurs »).
Moodle chapters used: `01_Ressource` (Chapitre 1, TP 1 to TP 8 with their corrections, mid-semester and final exams 2025/2026,
EASy68K quick reference) and `02_Tests en ligne` (Test 1 and Test 2). Annales: S3 Archi contrôles 2016/2017 to 2024/2025,
partiels 2016/2017 to 2023/2024 and the retake 2016/2017.
Calibrated on the Contrôle S3 2025/2026 and Partiel S3 2025/2026 (tables of instructions on memory and registers, flags N Z V C
of additions, programs with loops, rotations, subroutines on strings).
Every register value, address, flag and memory image is computed in `calc` with Python integers (masks, `//`, `%`, `lambda x:`)
from the course rules, independently from the stated answer; hexadecimal answers are written `hexa('...')`. The programs and
the subroutines of the `open` exercises were run on a minimal 68000 emulator (not in the repository) and checked against the
official corrections of the exams. In texts every hexadecimal number is inside backticks (a `$` outside code would be read as LaTeX).
"""

SUBJECT = {
    "id": "archi-s3-assembleur-68000",
    "ordre": 450,
    "matiere": "archi",
    "semestre": "S3",
    "ecue": "ASM68K",
    "titre": "Les bases de l'assembleur 68000",
    "chapitres_moodle": ["01_Ressource", "02_Tests en ligne"],
    "td": "TP 1 à TP 8 (premiers pas, modes d'adressage, branchements et boucles, pile et sous-programmes, calculatrice)",
    "examens": ["Contrôle S3 (mi-semestre)", "Partiel S3 (fin de semestre)"],
}

NOTIONS = [
    {
     "id": "nombres",
     "titre": "Hexadécimal, binaire et complément à deux (rappel S1)",
     "formule": "un chiffre hexa $=4$ bits · dollar : hexa, pourcent : binaire, rien : décimal · valeur signée sur $n$ bits : $v-2^n$ si le bit de poids fort vaut $1$ · extension de signe : on recopie le bit de poids fort",
     "exemple": "```" "\n"
        "$B4 sur 8 bits = 180 - 256 = -76" "\n"
        "$B4 étendu sur 16 bits : $FFB4" "\n"
        "```",
     "cours": r"Rappel S1 : $N=\sum a_i\,b^i$. En assembleur 68000 les nombres s'écrivent avec le préfixe dollar (hexadécimal), pourcent (binaire) ou sans préfixe (décimal). Un octet vaut deux chiffres hexa, un mot (16 bits) quatre, un mot long (32 bits) huit. En complément à deux sur $n$ bits, un nombre dont le bit de poids fort est $1$ est négatif : valeur $=v-2^n$. Pour passer à une taille supérieure en conservant la valeur, on recopie le bit de poids fort (extension de signe) : l'octet F0 devient le mot FFF0, puis le mot long FFFFFFF0 (valeur moins seize).",
    },
    {
     "id": "memoire",
     "titre": "Mémoire du 68000 : octets, big-endian, alignement (rappel S2)",
     "formule": "adresses sur $24$ fils : $2^{24}$ octets $=16$ Mio · big-endian : l'octet de poids fort est à l'adresse la plus basse · mot et mot long : adresse paire obligatoire · octet : toute adresse",
     "exemple": "```" "\n"
        "$1000 : 21 45 87 AF" "\n"
        "mot à $1002 = $87AF ; mot long à $1000 = $214587AF" "\n"
        "```",
     "cours": "Rappel S2 (microprocesseur) : le bus d'adresse sélectionne un octet. Le 68000 a un bus de donnée de $16$ fils et $23$ fils d'adresse de mots ; avec les signaux UDS et LDS il se comporte comme s'il avait $24$ fils d'adresse d'octets : $16$ Mio. Les données multi-octets sont rangées en big-endian. Un mot ou un mot long ne peut être lu ou écrit qu'à une adresse paire, sinon le processeur lève une erreur d'adresse ; un octet est accessible à toute adresse. Une instruction est toujours à une adresse paire.",
    },
    {
     "id": "directives",
     "titre": "Structure d'un source et directives ORG, EQU, DC, DS",
     "formule": r"ligne : étiquette · mnémonique · opérandes · commentaire (`;`) · `ORG` : adresse d'assemblage · `EQU` : constante · `DC` : place des données · `DS` : réserve de la place (adresse suivante $=$ adresse $+$ nombre $\times$ taille)",
     "exemple": "`TAB2 DS.W 3` réserve $6$ octets",
     "cours": "Un source contient une instruction par ligne, en quatre champs. L'étiquette (facultative, en première colonne) prend la valeur de l'adresse de l'instruction qui suit. Une directive n'est pas une instruction : elle ne produit pas de code machine. `ORG` fixe l'adresse d'assemblage, `EQU` nomme une constante, `DC.B/W/L` place des valeurs ou des chaînes ASCII en mémoire, `DS.B/W/L` réserve de l'espace non initialisé. Une instruction fait de 2 à 10 octets.",
    },
    {
     "id": "registres",
     "titre": "Registres et architecture du 68000",
     "formule": "$8$ registres de donnée D0-D7 (32 bits, accès .B .W .L) · $8$ registres d'adresse A0-A7 (32 bits, accès .W .L, $24$ bits utiles) · A7 $=$ pointeur de pile (SSP ou USP) · PC · SR $=16$ bits, CCR $=8$ bits de poids faible · $2$ modes : superviseur et utilisateur",
     "exemple": "```" "\n"
        "A0 = $F59809AC  →  adresse accédée $9809AC" "\n"
        "```",
     "cours": "Les registres de donnée contiennent n'importe quelle donnée. Les registres d'adresse contiennent des adresses ; seuls leurs $24$ bits de poids faible sortent sur le bus. A7 est le pointeur de pile : SSP en mode superviseur, USP en mode utilisateur. Le compteur programme PC contient l'adresse de la prochaine instruction. Le registre d'état SR ($16$ bits) n'est accessible en entier qu'en mode superviseur ; son octet de poids faible, le CCR, contient les drapeaux X N Z V C. Le mode utilisateur interdit les instructions privilégiées.",
    },
    {
     "id": "tailles",
     "titre": "Tailles .B .W .L et écriture partielle des registres",
     "formule": "`.B` $=8$ bits, `.W` $=16$, `.L` $=32$ · une opération `.B` ou `.W` ne modifie que les bits de poids faible du registre · `MOVEQ` : $-128$ à $127$ étendu sur $32$ bits · `EXT.W` / `EXT.L` : extension de signe · `MOVEA` pour écrire dans An",
     "exemple": "```" "\n"
        "D0 = $11223344   D1 = $AABBCCDD" "\n"
        "MOVE.B D0,D1  →  D1 = $AABBCC44" "\n"
        "```",
     "cours": "Une instruction travaille sur la taille donnée par son extension. Sur un registre de donnée, les bits au-dessus de la taille sont conservés. `MOVEQ #n,Dn` charge un entier signé de $8$ bits étendu sur tout le registre. `EXT.W Dn` étend le signe de D.B vers D.W, `EXT.L Dn` de D.W vers D.L. `CLR.s` met à zéro la partie concernée. MOVE n'écrit pas dans un registre d'adresse : on utilise MOVEA ou LEA.",
    },
    {
     "id": "drapeaux",
     "titre": "Drapeaux N, Z, V, C",
     "formule": r"N : bit de poids fort du résultat · Z : résultat nul · C : retenue (dépassement non signé) · V : dépassement signé : $+,+\to-$ ou $-,-\to+$ · `CMP S,D` calcule $D-S$ sans stocker",
     "exemple": "```" "\n"
        "$7F + $80 = $FF (8 bits) : N=1  Z=0  V=0  C=0" "\n"
        "```",
     "cours": "Après une addition, on calcule la somme sur la taille de l'opération. N copie le bit de poids fort du résultat. Z vaut $1$ si le résultat tronqué est nul. C vaut $1$ si la somme dépasse la taille (retenue). V se détermine en supposant les nombres signés : $1$ si l'on additionne deux positifs et que le résultat est négatif, ou deux négatifs et que le résultat est positif. Pour une soustraction ou une comparaison, C vaut $1$ en cas d'emprunt (destination plus petite que la source en non signé).",
    },
    {
     "id": "adressage",
     "titre": "Modes d'adressage : Dn, An, #, (An), (An)+, -(An)",
     "formule": "Dn, An et `#data` ne spécifient pas d'emplacement mémoire · `(An)` : adresse $=$ An · `(An)+` : lire puis An $+=$ taille · `-(An)` : An $-=$ taille puis lire · taille $=1,2,4$ pour .B .W .L",
     "exemple": "`MOVE.W -(A0),D0` : A0 diminue de $2$ avant la lecture",
     "cours": "L'adresse effective « ea » est l'emplacement de l'opérande. Les modes directs (Dn, An) et immédiat (`#`) n'ont pas d'adresse mémoire. Les modes indirects et absolus en ont une. La postincrémentation `(An)+` utilise An puis l'augmente de la taille de l'instruction ; la prédécrémentation `-(An)` diminue An puis l'utilise. Avec `(An)+`, l'adresse effective est l'ancienne valeur ; avec `-(An)` c'est la nouvelle.",
    },
    {
     "id": "ea",
     "titre": "Adresse effective : d16(An), d8(An,Xn), absolu, relatif au PC",
     "formule": r"`d16(An)` : $\text{An}+d_{16}$ ($-32768$ à $32767$) · `d8(An,Xn)` : $\text{An}+d_8+X_n$ ($-128$ à $127$) · index `.W` : étendu en signe · absolu : l'adresse écrite · `étiquette(PC)` : adresse relative au PC · adresse impaire + `.W`/`.L` : erreur",
     "exemple": "```" "\n"
        "A2 = $500A   D1 = $FFFFFFE0" "\n"
        "34(A2,D1.L) = $500A + 34 - 32 = $500C" "\n"
        "```",
     "cours": "On calcule l'adresse effective en additionnant le registre, le déplacement et l'index. L'index `.W` est un mot signé : un index `.W` dont les $16$ bits de poids faible valent FFFF vaut moins un. Un déplacement négatif s'écrit en décimal ou en hexadécimal signé. L'opération `.W` ou `.L` à une adresse impaire provoque une erreur à l'exécution (pas à l'assemblage).",
    },
    {
     "id": "memmove",
     "titre": "MOVE et mémoire : lire ce qui change",
     "formule": "source d'abord (avec ses effets sur An), puis destination · big-endian · `MOVE` copie $1,2$ ou $4$ octets · MOVE modifie N et Z, met V et C à $0$ · `LEA` charge l'adresse effective, pas son contenu",
     "exemple": "```" "\n"
        "A0 = $1000" "\n"
        "MOVE.W #36,(A0)  →  $1000 : 00 24 ..." "\n"
        "```",
     "cours": "Pour trouver l'effet d'un MOVE : (1) calculer l'adresse effective source et lire la valeur ; (2) calculer l'adresse effective destination ; (3) écrire en big-endian sur la taille de l'instruction ; (4) noter les registres d'adresse modifiés par `(An)+` et `-(An)`. Les octets voisins ne changent pas. Dans le contrôle, la mémoire et les registres sont réinitialisés avant chaque instruction.",
    },
    {
     "id": "arith",
     "titre": "Arithmétique et logique",
     "formule": r"`ADD`/`SUB` : dest $\pm$ source · `ADDQ`/`SUBQ` : constante $1$ à $8$ · `NEG` : $0-$dest · `NOT` : complément à $1$ · `AND`/`OR`/`EOR` bit à bit · `MULU.W` : D $\leftarrow$ D.W $\times$ source.W · `DIVU.W` : quotient en D.W, reste en D(31:16) · `ADDX` ajoute X",
     "exemple": "```" "\n"
        "D0 = $12340005 ; NEG.B D0  →  D0 = $123400FB" "\n"
        "```",
     "cours": "Toutes les opérations travaillent sur la taille indiquée et ne modifient que cette partie du registre de donnée (sauf MULU, MULS, DIVU, DIVS dont le résultat est sur 32 bits). `ADDX.L` additionne aussi le drapeau X : on additionne des entiers de plus de $32$ bits en chaînant `ADD` puis `ADDX`. `DIVU.W S,Dn` divise Dn (32 bits) par S (16 bits) : quotient dans les $16$ bits de poids faible, reste dans les $16$ bits de poids fort.",
    },
    {
     "id": "rotation",
     "titre": "Décalages, rotations et SWAP",
     "formule": "`ROR.s #k` / `ROL.s #k` : rotation sur la taille $s$ seulement · `SWAP` : échange les deux mots · `LSL`/`LSR` : décalage logique (entre des $0$) · `ASR` : conserve le signe · `ROL.s #k` $=$ `ROR.s #(taille-k)`",
     "exemple": "```" "\n"
        "à partir de $12345678 :" "\n"
        "ROR.W #4 → $12348567   ROL.B #4 → $12345687   SWAP → $56781234" "\n"
        "```",
     "cours": "Une rotation sur `.B`, `.W` ou `.L` ne touche que les $8$, $16$ ou $32$ bits de poids faible. `ROR.B #4` échange les deux chiffres hexa du dernier octet. `ROR.W #4` fait tourner les quatre chiffres hexa de poids faible. `ROR.L #8` déplace l'octet de poids faible en tête. `SWAP Dn` échange les mots haut et bas. En écrivant le registre chiffre par chiffre, on suit chaque rotation à la main.",
    },
    {
     "id": "branch",
     "titre": "TST, CMP et branchements conditionnels",
     "formule": r"`BEQ` $Z=1$ · `BNE` $Z=0$ · `BMI` $N=1$ · `BPL` $N=0$ · `CMP S,D` puis `Bcc` : branche si D $\text{cc}$ S · signé : `BGT BGE BLT BLE` · non signé : `BHI BHS BLO BLS` · `BRA`/`JMP` : toujours",
     "exemple": "```" "\n"
        "D7.B = $89 : TST.B D7 / BMI → saut (N = 1)" "\n"
        "CMP.B #$70,D7 / BLT → saut (signé : -119 < 112)" "\n"
        "```",
     "cours": "`TST` met à jour N et Z d'après l'opérande. `CMP S,D` fait $D-S$ et met à jour N, Z, V, C sans écrire le résultat. Le branchement qui suit se lit « D (condition) S ». Après une comparaison, le choix entre les branchements signés (BGT, BGE, BLT, BLE) et non signés (BHI, BHS, BLO, BLS) dépend de l'interprétation des nombres : l'octet FF vaut $255$ en non signé et $-1$ en signé. La taille de la comparaison compte : `CMP.B` ne regarde que l'octet de poids faible.",
    },
    {
     "id": "boucle",
     "titre": "Boucles : SUBQ/BNE et DBRA",
     "formule": r"`SUBQ.s #k,Dn` puis `BNE` : s'arrête quand la partie `.s` de Dn vaut $0$ · valeur initiale $v$ (taille $s$), pas $1$ : $v$ tours ($2^{\text{taille}}$ si $v=0$) · `DBRA Dn,étiquette` : $D_n.W-1$, saut si $\ne-1$ : $D_n.W+1$ tours",
     "exemple": "```" "\n"
        "D0 = $00000104 : SUBQ.B #1,D0 / BNE → 4 tours" "\n"
        "DBRA avec D0.W = $9999 → $999A tours" "\n"
        "```",
     "cours": "Avec `SUBQ.B #1,D0` suivi de `BNE`, seul l'octet de poids faible compte : les bits de poids fort de D0 ne sont jamais testés. Si D0.B vaut $0$ au départ, la boucle fait $256$ tours. Avec un pas $k$, on compte le nombre de soustractions nécessaires pour atteindre $0$ modulo $2^8$ (ou $2^{16}$). `DBRA Dn,étiquette` décrémente les $16$ bits de poids faible puis boucle tant que le résultat n'est pas FFFF en hexadécimal : un compteur $n$ donne $n+1$ tours.",
    },
    {
     "id": "pile",
     "titre": "Pile, A7 et MOVEM",
     "formule": r"empiler : `MOVE.s src,-(A7)` (A7 diminue de $2$ ou $4$) · dépiler : `MOVE.s (A7)+,dst` · `MOVEM.L liste,-(A7)` : A7 diminue de $4\times$ nombre de registres · LIFO : le dernier empilé sort le premier",
     "exemple": "```" "\n"
        "A7 = $F00006" "\n"
        "MOVE.W #$42,-(A7)  →  A7 = $F00004" "\n"
        "MOVE.L #$53,-(A7)  →  A7 = $F00000" "\n"
        "```",
     "cours": "A7 pointe sur le sommet de la pile. Empiler : A7 est décrémenté puis la donnée est écrite ; dépiler : la donnée est lue puis A7 est incrémenté. Seuls des mots ou mots longs sont empilés. `MOVEM` empile ou dépile plusieurs registres : avec `-(A7)` l'ordre est inversé (A7 d'abord, D0 en dernier), donc D0 se retrouve au sommet de la pile ; avec `(A7)+` l'ordre est D0 d'abord, A7 ensuite. Seule la variation de A7 compte, pas sa valeur.",
    },
    {
     "id": "sousprog",
     "titre": "Sous-programmes : JSR, BSR, RTS",
     "formule": "`JSR`/`BSR` : empile l'adresse de retour ($32$ bits, A7 $-4$), puis saute · `RTS` : dépile l'adresse dans PC (A7 $+4$) · sauvegarder les registres modifiés avec `MOVEM` · entrées et sorties documentées",
     "exemple": "```" "\n"
        "A7 = $5004 avant RTS  →  A7 = $5008 après" "\n"
        "```",
     "cours": "Un sous-programme est l'équivalent d'une fonction. `JSR` ou `BSR` empile l'adresse de l'instruction suivante puis branche ; `RTS` la dépile dans PC. Les paramètres sont passés dans des registres. Les consignes d'examen imposent souvent de ne modifier aucun registre en dehors des registres de sortie : on commence par `MOVEM.L liste,-(A7)` et on termine par `MOVEM.L (A7)+,liste` juste avant `RTS`. Des étiquettes locales commencent par un antislash.",
    },
    {
     "id": "chaines",
     "titre": "Chaînes de caractères et ASCII",
     "formule": r"chaîne : octets ASCII terminés par $0$ · `'A'` $=65$, `'a'` $=97$, `'0'` $=48$, espace $=32$, tabulation $=9$ · chiffre $\to$ valeur : `SUB.B #'0'` · `MOVE.B (A0)+,D1` puis `BEQ` : test de fin de chaîne",
     "exemple": "```" "\n"
        '"704" → 37 30 34 00 ; somme des chiffres = 11' "\n"
        "```",
     "cours": r"Une chaîne se termine par un octet nul. On la parcourt avec `MOVE.B (A0)+,D1` : l'instruction MOVE met Z à jour comme TST, donc `BEQ` détecte la fin. On teste une classe de caractères par deux comparaisons non signées (`CMP.B #'a',D1 / BLO`, `CMP.B #'z',D1 / BHI`). Pour convertir un chiffre ASCII en valeur on soustrait `'0'` ; pour lire un nombre : $r\leftarrow 10r+\text{chiffre}$ (`MULU.W #10,D0`).",
    },
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


def m(id, enonce, parts, src):
    return {"id": id, "kind": "multi", "src": src, "enonce": enonce, "parts": parts}


LEVELS = [
    {"n": 1, "titre": "Rappel S1 : hexadécimal et complément à deux", "notions": ["nombres"], "exos": [
        v("n11", "Convertir `$7A8` en décimal.", "7*256+10*16+8", "hexa('7A8')", r"$7\times256+10\times16+8=1960$.", src="Chapitre 1 du cours (D. Bouchet), I-3.3 ; IV-2.3"),
        v("n12", "Convertir le nombre décimal $2000$ en hexadécimal (donner la valeur).", "2000", "hexa('7D0')", r"$2000=7\times256+13\times16+0$, soit" "\n"
        "`$7D0`."),
        v("n13", "Quelle est la valeur signée de l'octet `$B4` (complément à deux sur" "\n"
        "$8$ bits) ?", "180-256", "tc('10110100')", "`$B4` s'écrit `1011 0100` : le bit de poids fort vaut" "\n"
        "$1$. Non signé $180$, donc $180-256=-76$."),
        v("n14", "Quelle est la valeur signée du mot long `$FFFFFFFB` ?", "hexa('FFFFFFFB')-2**32", "-5", "Le bit de poids fort vaut $1$ : $4294967291-2^{32}=-5$.", src="Contrôle S3 2025/2026, ex. 1 (valeur initiale de D0)"),
        v("n15", "Étendre en signe l'octet `$F0` sur" "\n"
        "$16$ bits. Donner le mot obtenu.", "hexa('F0')+(2**16-2**8)", "hexa('FFF0')", "Le bit de poids fort de `$F0` vaut" "\n"
        "$1$ : on remplit les $8$ bits de poids fort avec des $1$. On obtient" "\n"
        "`$FFF0`" "\n"
        "($-16$ sur $8$ comme sur $16$ bits)."),
        v("n16", "Écrire $-5$ sur $8$ bits en hexadécimal (complément à deux).", "2**8-5", "hexa('FB')", "$256-5=251$, soit" "\n"
        "`$FB`. Par la méthode des bits :" "\n"
        r"$5=0000\,0101$, complément $1111\,1010$, plus $1$ : $1111\,1011$."),
        v("n17", "Additionner `$4AC9` et" "\n"
        "`$D841` en hexadécimal (résultat complet, sans le tronquer à" "\n"
        "$16$ bits).", "19145+55361", "hexa('1230A')", "Colonne par colonne : $9+1=A$ ; $C+4=16=10_{16}$ (retenue) ; $A+8+1=19=13_{16}$ (retenue) ; $4+D+1=18=12_{16}$. Résultat" "\n"
        "`$1230A`. Sur" "\n"
        "$16$ bits, on garderait" "\n"
        "`$230A` avec une retenue.", src="TP 1, étape 1"),
        o("n18", "Convertir `%10001001` en hexadécimal et en décimal. Quelle est sa valeur signée sur $8$ bits ?", "Groupes de $4$ bits : $1000=8$ et $1001=9$, donc" "\n"
        "`$89`." "\n"
        r"Décimal : $8\times16+9=137$." "\n"
        "Le bit de poids fort vaut $1$ : valeur signée $137-256=-119$.", src="Chapitre 1 du cours (D. Bouchet), I-3.3"),
    ]},
    {"n": 2, "titre": "Rappel S2 : mémoire, big-endian, directives", "notions": ["memoire", "directives"], "exos": [
        v("m21", "Le 68000 a $23$ fils d'adresse de mots de $16$ bits, mais, grâce aux signaux UDS et LDS, il se comporte comme s'il avait $24$ fils d'adresse d'octets. Combien de Mio d'octets adresse-t-il ?", "2**24/2**20", "16", "$2^{24}$ octets $=2^{24}/2^{20}$ Mio $=16$ Mio.", src="Chapitre 1 du cours (D. Bouchet), II-1"),
        v("m27", r"Un microprocesseur a $23$ fils d'adresse de mots et un bus de donnée de $16$ fils. Quelle est sa capacité d'adressage en Mio (profondeur $\times$ largeur $/\,8$) ?", "2**23*16/8/2**20", "16", r"Profondeur $2^{23}$ mots, largeur $16$ bits : $2^{23}\times16/8=2^{24}$ octets $=16$ Mio. On retrouve les $24$ fils d'adresse d'octets.", src="Chapitre 1 du cours (D. Bouchet), II-1"),
        v("m22", "Mémoire à partir de `$1000` :" "\n"
        "" "\n"
        "```" "\n"
        "$1000 : 21 45 87 AF B5 F3 3C 32" "\n"
        "```" "\n"
        "" "\n"
        "Quelle est la valeur du mot de $16$ bits situé à l'adresse" "\n"
        "`$1002` (big-endian) ?", "135*256+175", "hexa('87AF')", "Les octets à `$1002` et" "\n"
        "`$1003` sont `87` et `AF`. L'octet de poids fort est à l'adresse la plus basse : le mot vaut" "\n"
        "`$87AF`.", src="Chapitre 1 du cours (D. Bouchet), IV-3.1"),
        v("m23", "Même mémoire :" "\n"
        "" "\n"
        "```" "\n"
        "$1000 : 21 45 87 AF B5 F3 3C 32" "\n"
        "```" "\n"
        "" "\n"
        "Quelle est la valeur du mot long (32 bits) situé à l'adresse `$1004` ?", "181*2**24+243*2**16+60*256+50", "hexa('B5F33C32')", "Les quatre octets à partir de `$1004` sont `B5 F3 3C 32` ; le mot long vaut" "\n"
        "`$B5F33C32`.", src="Chapitre 1 du cours (D. Bouchet), IV-3.1"),
        v("m24", "```asm" "\n"
        "        ORG   $1000" "\n"
        "        DC.B  10,5,7,$7A,255,%11111001" "\n"
        '        DC.B  "Hello World",13,10,0' "\n"
        "        DC.W  5,6" "\n"
        "L       DC.L  5,6" "\n"
        "```" "\n"
        "" "\n"
        "Quelle est la valeur de l'étiquette `L` ?", "hexa('1000')+6+14+4", "hexa('1018')", "Le premier `DC.B` place $6$ octets (de" "\n"
        "`$1000` à" "\n"
        "`$1005`). Le second place" "\n"
        "$11$ caractères plus `13`, `10`, `0` : $14$ octets (jusqu'à" "\n"
        "`$1013`). `DC.W 5,6` place" "\n"
        r"$2\times2=4$ octets (de" "\n"
        "`$1014` à" "\n"
        "`$1017`). `L` vaut donc" "\n"
        "`$1018`.", src="Chapitre 1 du cours (D. Bouchet), III-3"),
        v("m25", "```asm" "\n"
        "        ORG   $5000" "\n"
        "TAB1    DS.B  4" "\n"
        "TAB2    DS.W  3" "\n"
        "TAB3    DS.L  1" "\n"
        "NEXT" "\n"
        "```" "\n"
        "" "\n"
        "Quelle est la valeur de l'étiquette `NEXT` ?", "hexa('5000')+4+3*2+4", "hexa('500E')", "`TAB1` vaut `$5000`" "\n"
        "($4$ octets), `TAB2` vaut" "\n"
        "`$5004`" "\n"
        "($6$ octets), `TAB3` vaut" "\n"
        "`$500A`" "\n"
        "($4$ octets) et `NEXT` vaut" "\n"
        "`$500E`.", src="Chapitre 1 du cours (D. Bouchet), III-4"),
        o("m26", "Pourquoi l'instruction `MOVE.W D0,$5001` provoque-t-elle une erreur à l'exécution alors que" "\n"
        "`MOVE.B D0,$5001` est correcte ? L'assembleur peut-il toujours le détecter ?", "Le 68000 est organisé en mots de $16$ bits : un mot ou un mot long ne peut être lu ou écrit qu'à une **adresse paire**." "\n"
        "`$5001` est impaire : écrire un mot à cette adresse provoque une erreur d'adresse. Un octet peut au contraire être lu ou écrit à toute adresse, paire ou impaire. Une instruction est elle aussi toujours à une adresse paire." "\n"
        "" "\n"
        "L'erreur est **dynamique** : quand l'adresse vient d'un registre (par exemple `MOVE.W D0,(A0)`), l'assembleur ne peut pas la prévoir ; elle n'apparaît qu'à l'exécution.", src="Chapitre 1 du cours (D. Bouchet), II-1 ; TP 2"),
    ]},
    {"n": 3, "titre": "Architecture et registres du 68000", "notions": ["registres"], "exos": [
        v("r31", "Combien de bits contiennent au total les huit registres de donnée D0 à D7 ?", "8*32", "256", r"Chaque registre de donnée a $32$ bits : $8\times32=256$.", src="Chapitre 1 du cours (D. Bouchet), II-3.1"),
        v("r32", "Le registre A0 contient `$F59809AC`. Le 68000 n'envoie que" "\n"
        "$24$ bits sur le bus d'adresse. À quelle adresse accède-t-il ?", "hexa('F59809AC')%2**24", "hexa('9809AC')", "On ignore les $8$ bits de poids fort" "\n"
        "(`$F5`) : l'adresse accédée est" "\n"
        "`$9809AC`.", src="Chapitre 1 du cours (D. Bouchet), II-3.2"),
        v("r33", "Quelle est la taille maximale (en octets) d'une instruction du 68000, sachant qu'elle contient au plus cinq mots de $16$ bits ?", "5*2", "10", r"$5\times2=10$ octets. La taille minimale est un mot : $2$ octets.", src="Chapitre 1 du cours (D. Bouchet), I-3"),
        v("r34", "Le registre d'état SR fait $16$ bits et le registre CCR en est l'octet de poids faible. Combien de bits de SR sont accessibles uniquement en mode superviseur ?", "16-8", "8", "$16-8=8$ : l'octet de poids fort de SR (T, S et le masque d'interruption I2 I1 I0) n'est accessible qu'en mode superviseur ; le CCR (X N Z V C) est accessible en mode utilisateur.", src="Chapitre 1 du cours (D. Bouchet), II-3.4"),
        v("r35", "Dans le CCR (bits $4$ à $0$ : X N Z V C), on a X$=0$, N$=1$, Z$=0$, V$=1$, C$=0$. Quelle est la valeur du CCR (nombre) ?", "8+2", "bits('1010')", "Poids : X$=16$, N$=8$, Z$=4$, V$=2$, C$=1$. Ici N et V valent $1$ : $8+2=10$, soit `%01010`."),
        o("r36", "Combien de registres de donnée, de registres d'adresse, de compteurs programme, de pointeurs de pile, de registres d'état et de modes de fonctionnement le 68000 possède-t-il ? Quels sont les noms des pointeurs de pile ?", "$8$ registres de donnée (D0 à D7), $8$ registres d'adresse (A0 à A7), $1$ compteur programme (PC), $2$ pointeurs de pile (SSP en mode superviseur, USP en mode utilisateur, tous deux accessibles par A7), $1$ registre d'état (SR, dont le CCR est l'octet de poids faible), $2$ modes (superviseur et utilisateur).", src="Contrôle S3 2020/2021, ex. 4", duree=3),
        o("r37", "Quelle différence y a-t-il entre le mode superviseur et le mode utilisateur ? Que se passe-t-il pour A7 quand on passe de l'un à l'autre ?", "En mode superviseur le processeur peut exécuter toutes les instructions ; en mode utilisateur il ne peut pas exécuter les instructions **privilégiées**, ce qui protège le système des applications défaillantes." "\n"
        "" "\n"
        "A7 est SSP en mode superviseur et USP en mode utilisateur : il y a deux piles distinctes. Si l'on écrit A7 en mode superviseur puis qu'on passe en mode utilisateur, on lit USP et non la valeur qu'on vient d'écrire.", src="Chapitre 1 du cours (D. Bouchet), II-2 et II-3.2", duree=4),
    ]},
    {"n": 4, "titre": "Tailles .B .W .L et instructions MOVE, MOVEQ, EXT, CLR", "notions": ["tailles"], "exos": [
        v("s41", "D0 contient `$11223344` et D1 contient" "\n"
        "`$AABBCCDD`. Que contient D1 après `MOVE.B D0,D1` ?", "(hexa('AABBCCDD')-hexa('AABBCCDD')%2**8)+hexa('11223344')%2**8", "hexa('AABBCC44')", "`MOVE.B` copie les 8 bits de poids faible de D0 (`$44`) dans D1 et laisse les autres bits de D1. D1 vaut" "\n"
        "`$AABBCC44`.", src="Chapitre 1 du cours (D. Bouchet), IV-2.1"),
        v("s42", "D0 contient `$11223344` et D1 contient" "\n"
        "`$AABBCCDD`. Que contient D1 après `MOVE.W D0,D1` ?", "(hexa('AABBCCDD')-hexa('AABBCCDD')%2**16)+hexa('11223344')%2**16", "hexa('AABB3344')", "`MOVE.W` copie les 16 bits de poids faible de D0 (`$3344`) dans D1 et laisse les autres bits de D1. D1 vaut" "\n"
        "`$AABB3344`.", src="Chapitre 1 du cours (D. Bouchet), IV-2.1"),
        v("s43", "D0 contient `$11223344`. Que contient D0 après" "\n"
        "`MOVE.W #$7A8,D0` ?", "(hexa('11223344')-hexa('11223344')%2**16)+hexa('7A8')", "hexa('112207A8')", "Le mot immédiat `$07A8` remplace les" "\n"
        "$16$ bits de poids faible : D0 vaut" "\n"
        "`$112207A8`.", src="Chapitre 1 du cours (D. Bouchet), IV-2.3"),
        v("s44", "D0 contient `$11223344`. Que contient D0 après" "\n"
        "`MOVE.L #$7A8,D0` ?", "hexa('7A8')", "hexa('000007A8')", "Avec `.L` les $32$ bits sont remplacés : D0 vaut" "\n"
        "`$000007A8`.", src="Chapitre 1 du cours (D. Bouchet), IV-2.3"),
        v("s45", "Que contient D0 après `MOVEQ.L #-5,D0` ?", "2**32-5", "hexa('FFFFFFFB')", "`MOVEQ` étend le signe de l'entier $-5$" "\n"
        "(`$FB`) sur" "\n"
        "$32$ bits : D0 vaut" "\n"
        "`$FFFFFFFB`.", src="Chapitre 1 du cours (D. Bouchet), VIII-1"),
        v("s46", "D0 contient `$11223380`. Que contient D0 après `EXT.W D0` ?", "(hexa('11223380')-hexa('11223380')%2**16)+(hexa('80')+2**16-2**8)", "hexa('1122FF80')", "`EXT.W` étend le signe de D0.B (`$80`, négatif) sur D0.W :" "\n"
        "`$FF80`. Les" "\n"
        "$16$ bits de poids fort ne changent pas :" "\n"
        "`$1122FF80`.", src="Chapitre 1 du cours (D. Bouchet), VIII-2.5"),
        v("s47", "A0 contient `$005030B0` et D0 contient" "\n"
        "`$11223344`. Que contient D0 après `MOVE.W A0,D0` ?", "(hexa('11223344')-hexa('11223344')%2**16)+hexa('005030B0')%2**16", "hexa('112230B0')", "`MOVE.W A0,D0` copie le mot de poids faible de A0 (`$30B0`) : D0 vaut" "\n"
        "`$112230B0`.", src="Chapitre 1 du cours (D. Bouchet), IV-2.2"),
        v("s48", "D0 contient `$FFFFFFFF`. Que contient D0 après `CLR.W D0` ?", "hexa('FFFFFFFF')-hexa('FFFFFFFF')%2**16", "hexa('FFFF0000')", "`CLR.W` met à $0$ les $16$ bits de poids faible :" "\n"
        "`$FFFF0000`."),
        o("s49", "Pourquoi `MOVE.L D0,A0` est-il refusé ou remplacé par `MOVEA.L D0,A0` ? Quelle est la plage de valeurs de `MOVEQ` ? Que fait `EXT.W D0` quand D0.B vaut `$7F` ?", "`MOVE` n'accepte pas de registre d'adresse en destination : il faut `MOVEA` ou `LEA`. (`MOVEA` ne modifie d'ailleurs pas les drapeaux.)" "\n"
        "" "\n"
        "`MOVEQ #n,Dn` charge un entier signé de $8$ bits, soit de $-128$ à $127$ ; il est étendu en signe sur $32$ bits." "\n"
        "" "\n"
        "`EXT.W D0` avec D0.B $=$" "\n"
        "`$7F` (positif) donne D0.W" "\n"
        "$=$" "\n"
        "`$007F`.", src="Chapitre 1 du cours (D. Bouchet), IV-2.2 ; VIII", duree=4),
    ]},
    {"n": 5, "titre": "Drapeaux N Z V C après une addition ou une comparaison", "notions": ["drapeaux"], "exos": [
        v("f51", "On additionne sur 8 bits : `$7F + $7F` (par exemple avec `ADD.B`). Donner le résultat (en hexadécimal, sur 8 bits).", "(hexa('7F')+hexa('7F'))%2**8", "hexa('FE')", "`$7F + $7F = $FE` ; sur 8 bits on garde" "\n"
        "`$FE`.", src="Contrôle S3 2025/2026, ex. 2"),
        v("f52", "On additionne sur 8 bits : `$7F + $80` (par exemple avec `ADD.B`). Donner le drapeau N.", "((hexa('7F')+hexa('80'))%2**8)//2**7", "1", "`$7F + $80 = $FF` ; sur 8 bits on garde" "\n"
        "`$FF`. N est le bit de poids fort du résultat :" "\n"
        "N$=1$.", src="Contrôle S3 2025/2026, ex. 2"),
        v("f53", "On additionne sur 8 bits : `$7A + $86` (par exemple avec `ADD.B`). Donner le drapeau Z.", "1-Min(1,(hexa('7A')+hexa('86'))%2**8)", "1", "`$7A + $86 = $100` ; sur 8 bits on garde" "\n"
        "`$00`. Le résultat tronqué est nul :" "\n"
        "Z$=1$.", src="Chapitre 1 du cours (D. Bouchet), II-3.4"),
        v("f54", "On additionne sur 8 bits : `$7F + $7F` (par exemple avec `ADD.B`). Donner le drapeau V.", "abs(((hexa('7F')-2**8*(hexa('7F')//2**7))+(hexa('7F')-2**8*(hexa('7F')//2**7))+2**7)//2**8)", "1", "`$7F + $7F = $FE` ; sur 8 bits on garde" "\n"
        "`$FE`. Signes : opérandes positif et positif, résultat négatif :" "\n"
        "V$=1$.", src="Contrôle S3 2025/2026, ex. 2"),
        v("f55", "On additionne sur 8 bits : `$F0 + $11` (par exemple avec `ADD.B`). Donner le drapeau C.", "(hexa('F0')+hexa('11'))//2**8", "1", "`$F0 + $11 = $101` ; sur 8 bits on garde" "\n"
        "`$01`. La somme dépasse 8 bits (retenue) :" "\n"
        "C$=1$.", src="Contrôle S3 2016/2017, ex. 2"),
        v("f56", "On additionne sur 32 bits : `$40000000 + $80000000` (par exemple avec `ADD.L`). Donner les drapeaux N, Z, V, C (écrire NZVC en binaire, par exemple `%1010`).", "8*(((hexa('40000000')+hexa('80000000'))%2**32)//2**31)+4*(1-Min(1,(hexa('40000000')+hexa('80000000'))%2**32))+2*(abs(((hexa('40000000')-2**32*(hexa('40000000')//2**31))+(hexa('80000000')-2**32*(hexa('80000000')//2**31))+2**31)//2**32))+(hexa('40000000')+hexa('80000000'))//2**32", "bits('1000')", "`$40000000 + $80000000 = $C0000000` ; sur 32 bits on garde" "\n"
        "`$C0000000`." "\n"
        "N$=1$, Z$=0$, V$=0$ (pas de dépassement signé), C$=0$. On lit NZVC `1000`.", src="Contrôle S3 2016/2017, ex. 2"),
        v("f57", "On additionne sur 32 bits : `$A0101010 + $A0909090` (par exemple avec `ADD.L`). Donner les drapeaux N, Z, V, C (écrire NZVC en binaire, par exemple `%1010`).", "8*(((hexa('A0101010')+hexa('A0909090'))%2**32)//2**31)+4*(1-Min(1,(hexa('A0101010')+hexa('A0909090'))%2**32))+2*(abs(((hexa('A0101010')-2**32*(hexa('A0101010')//2**31))+(hexa('A0909090')-2**32*(hexa('A0909090')//2**31))+2**31)//2**32))+(hexa('A0101010')+hexa('A0909090'))//2**32", "bits('0011')", "`$A0101010 + $A0909090 = $140A0A0A0` ; sur 32 bits on garde" "\n"
        "`$40A0A0A0`." "\n"
        "N$=0$, Z$=0$, V$=1$ (dépassement signé), C$=1$. On lit NZVC `0011`.", src="Contrôle S3 2025/2026, ex. 2"),
        v("f58", "D0 contient `$25` (taille 8 bits : on ne regarde que D0.B). On exécute" "\n"
        "`CMP.B #$30,D0`. Donner le drapeau C.", "Max(0,Min(1,hexa('30')-hexa('25')))", "1", "`CMP`/`SUB` calculent destination $-$ source :" "\n"
        "`$25 - $30` donne" "\n"
        "`$F5` sur 8 bits." "\n"
        "C$=1$ : emprunt, la destination est plus petite que la source en non signé.", src="Chapitre 1 du cours (D. Bouchet), VIII-6"),
        v("f59", "D0 contient `$7F` (taille 8 bits : on ne regarde que D0.B). On exécute" "\n"
        "`CMP.B #$80,D0`. Donner le drapeau V.", "abs(((hexa('7F')-2**8*(hexa('7F')//2**7))-(hexa('80')-2**8*(hexa('80')//2**7))+2**7)//2**8)", "1", "`CMP`/`SUB` calculent destination $-$ source :" "\n"
        "`$7F - $80` donne" "\n"
        "`$FF` sur 8 bits." "\n"
        "V$=1$ : dépassement signé (127 - -128 = 255 sort de la plage signée sur 8 bits).", src="Chapitre 1 du cours (D. Bouchet), VIII-6"),
        v("f510", "D0 contient `$11` (taille 8 bits : on ne regarde que D0.B). On exécute" "\n"
        "`CMP.B #$11,D0`. Donner le drapeau Z.", "1-Min(1,(hexa('11')-hexa('11'))%2**8)", "1", "`CMP`/`SUB` calculent destination $-$ source :" "\n"
        "`$11 - $11` donne" "\n"
        "`$00` sur 8 bits." "\n"
        "Z$=1$ (résultat nul).", src="Chapitre 1 du cours (D. Bouchet), V-2"),
        o("f511", "Dans l'addition sur $8$ bits" "\n"
        "`$F0 + $11`, on obtient" "\n"
        "`$01` avec" "\n"
        "C$=1$ et V$=0$. Expliquer pourquoi, en interprétant les nombres en non signé puis en signé.", "Non signé : $240+17=257>255$, la somme dépasse $8$ bits : **retenue**, C$=1$ (le résultat tronqué est $257-256=1$)." "\n"
        "" "\n"
        "Signé : `$F0` vaut" "\n"
        "$-16$ et" "\n"
        "`$11` vaut" "\n"
        "$17$ ; la somme $-16+17=1$ est dans la plage $[-128,127]$ : **pas de dépassement signé**, V$=0$. Le résultat" "\n"
        "`$01` est donc correct en signé, alors qu'il est faux en non signé." "\n"
        "" "\n"
        "Le drapeau C détecte un dépassement non signé, le drapeau V un dépassement signé : ils sont indépendants.", src="Contrôle S3 2016/2017, ex. 2", duree=5),
        v("f512", "On additionne sur 8 bits : `$1A + X`. Quel est le **plus petit** nombre X (en hexadécimal, sur 2 chiffres) pour lequel on obtient" "\n"
        "N$=0$, Z$=0$, V$=0$, C$=1$ ?", "2**8-hexa('1A')+1", "hexa('E7')", r"Il faut une retenue (C$=1$) : $26+X\ge256$, soit $X\ge230$. Pour $X=230$" "\n"
        "(`$E6`), le résultat vaut" "\n"
        "$0$ (Z$=1$) : on prend donc $X=231$. Résultat $1$ : N$=0$, Z$=0$, V$=0$ (un nombre positif et un nombre négatif ne débordent pas). Le plus petit X est" "\n"
        "`$E7`.", src="Partiel S3 2019/2020, ex. 2"),
        v("f513", "On additionne sur 16 bits : `$98BD + X`. Quel est le **plus petit** nombre X (en hexadécimal, sur 4 chiffres) pour lequel on obtient" "\n"
        "N$=0$, Z$=1$, V$=0$, C$=1$ ?", "2**16-hexa('98BD')", "hexa('6743')", "On veut un résultat nul avec retenue (Z$=1$, C$=1$) : $A+X=2^{16}$, soit $X=2^{16}-A=65536-39101=26435$. Le plus petit X est" "\n"
        "`$6743`." "\n"
        "V$=0$ car un nombre négatif et un nombre positif ne débordent pas.", src="Partiel S3 2018/2019, ex. 2"),
        v("f514", "On additionne sur 32 bits : `$7FFFFFFF + X`. Quel est le **plus petit** nombre X (en hexadécimal, sur 8 chiffres) pour lequel on obtient" "\n"
        "N$=1$, Z$=0$, V$=0$, C$=0$ ?", "2**31", "hexa('80000000')", r"N$=1$ avec V$=0$ : le premier opérande est positif, le résultat est négatif sans dépassement signé, donc X est négatif ($X\ge2^{31}$ en non signé). Avec X positif, $7FFFFFFF+X$ donnerait V$=1$. Le plus petit X est" "\n"
        "`$80000000`" "\n"
        "($-2^{31}$).", src="Partiel S3 2019/2020, ex. 2"),
        v("f515", "On additionne sur 8 bits : `$7F + X`. Quel est le **plus petit** nombre X (en hexadécimal, sur 2 chiffres) pour lequel on obtient" "\n"
        "N$=1$, Z$=0$, V$=1$, C$=0$ ?", "2**7-hexa('7F')", "hexa('01')", r"N$=1$ et V$=1$ : deux nombres positifs donnent un résultat négatif. $127+X\ge128$ donne $X\ge1$, le plus petit X est" "\n"
        "`$01` :" "\n"
        "$127+1=128$" "\n"
        "(`$80`)," "\n"
        "N$=1$, V$=1$, Z$=0$, C$=0$.", src="Partiel S3 2018/2019, ex. 2"),
    ]},
    {"n": 6, "titre": "Modes d'adressage : registre, immédiat, (An), (An)+, -(An)", "notions": ["adressage"], "exos": [
        v("a61", "On part de l'état suivant (la mémoire et les registres sont ceux du cours) :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $11223344   A0 = $00001000" "\n"
        "D1 = $AABBCCDD   A1 = $00001008" "\n"
        "D2 = $0000FFFF   A2 = $00001010" "\n"
        "D3 = $00000003   A3 = $00000006" "\n"
        "$001000  21 45 87 AF B5 F3 3C 32" "\n"
        "$001008  AD 45 39 98 9A 9B 9C 9D" "\n"
        "$001010  03 69 01 00 12 0A 0D C9" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVE.W (A0)+,D0` puis `MOVE.L (A0)+,D0`. Quelle est la valeur finale de D0 ?", "135*2**24+175*2**16+181*256+243", "hexa('87AFB5F3')", "`MOVE.W (A0)+,D0` lit le mot à `$1000`" "\n"
        "(`$2145`) puis A0 passe à" "\n"
        "`$1002`. `MOVE.L (A0)+,D0` lit le mot long à" "\n"
        "`$1002` : `87 AF B5 F3`. D0 vaut" "\n"
        "`$87AFB5F3` (le second MOVE remplit les" "\n"
        "$32$ bits) et A0 vaut" "\n"
        "`$1006`.", src="Chapitre 1 du cours (D. Bouchet), IV-3.2"),
        v("a62", "Même état :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $11223344   A0 = $00001000" "\n"
        "D1 = $AABBCCDD   A1 = $00001008" "\n"
        "D2 = $0000FFFF   A2 = $00001010" "\n"
        "D3 = $00000003   A3 = $00000006" "\n"
        "$001000  21 45 87 AF B5 F3 3C 32" "\n"
        "$001008  AD 45 39 98 9A 9B 9C 9D" "\n"
        "$001010  03 69 01 00 12 0A 0D C9" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVE.W (A0)+,D0`, `MOVE.L (A0)+,D0` puis `MOVE.B (A0)+,D0`. Quelle est la valeur finale de A0 ?", "hexa('1000')+2+4+1", "hexa('1007')", "Chaque postincrémentation ajoute la taille de l'instruction : $2+4+1=7$. A0 vaut" "\n"
        "`$1007`.", src="Chapitre 1 du cours (D. Bouchet), IV-3.2"),
        v("a63", "Même état :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $11223344   A0 = $00001000" "\n"
        "D1 = $AABBCCDD   A1 = $00001008" "\n"
        "D2 = $0000FFFF   A2 = $00001010" "\n"
        "D3 = $00000003   A3 = $00000006" "\n"
        "$001000  21 45 87 AF B5 F3 3C 32" "\n"
        "$001008  AD 45 39 98 9A 9B 9C 9D" "\n"
        "$001010  03 69 01 00 12 0A 0D C9" "\n"
        "```" "\n"
        "" "\n"
        "On exécute deux fois `MOVE.B -(A1),D0`. Quelle est la valeur finale de D0 ?", "hexa('11223344')-hexa('11223344')%256+60", "hexa('1122333C')", "Premier `MOVE.B -(A1),D0` : A1 passe à `$1007` puis on lit" "\n"
        "`$32`. Second : A1 passe à" "\n"
        "`$1006` et on lit" "\n"
        "`$3C`. Seul D0.B change : D0 vaut" "\n"
        "`$1122333C`.", src="Chapitre 1 du cours (D. Bouchet), IV-3.3"),
        v("a64", "Même état. On exécute `MOVE.W -(A1),D0` puis `MOVE.L -(A1),D0`. Quelle est la valeur finale de A1 ?", "hexa('1008')-2-4", "hexa('1002')", "A1 diminue de $2$ puis de $4$ :" "\n"
        "`$1002`.", src="Chapitre 1 du cours (D. Bouchet), IV-3.3"),
        v("a65", "Même état. On exécute `MOVE.L -(A2),-(A2)` (A2 vaut `$1010`). Quelle est la valeur du mot long situé à" "\n"
        "`$1008` après l'instruction ?", "154*2**24+155*2**16+156*256+157", "hexa('9A9B9C9D')", "La source est évaluée d'abord : A2 passe à `$100C` et on lit le mot long" "\n"
        "`$9A9B9C9D` à cette adresse. Puis la destination : A2 passe à" "\n"
        "`$1008` et on y écrit" "\n"
        "`$9A9B9C9D`. A2 vaut" "\n"
        "`$1008` à la fin.", src="Chapitre 1 du cours (D. Bouchet), IV-4.8"),
        o("a66", "Pour chacune des instructions suivantes, dire si l'opérande source se trouve dans un registre, dans l'instruction ou en mémoire (spécifie-t-il un emplacement mémoire ?) et donner l'adresse effective quand elle existe, A0 valant `$1000` :" "\n"
        "" "\n"
        "```asm" "\n"
        "MOVE.B D1,D0" "\n"
        "MOVE.W A0,D0" "\n"
        "MOVE.L #$1000,D0" "\n"
        "MOVE.L (A0),D0" "\n"
        "MOVE.W (A0)+,D0" "\n"
        "MOVE.W -(A0),D0" "\n"
        "MOVE.W $1000,D0" "\n"
        "```", "```" "\n"
        "Instruction          Source                  Mémoire ?  Adresse effective" "\n"
        "MOVE.B D1,D0         registre de donnée      non        aucune (registre D1)" "\n"
        "MOVE.W A0,D0         registre d'adresse      non        aucune (registre A0)" "\n"
        "MOVE.L #$1000,D0     immédiat                non        n'existe pas" "\n"
        "MOVE.L (A0),D0       indirect par registre   oui        $1000" "\n"
        "MOVE.W (A0)+,D0      postincrémentation      oui        $1000 (A0 devient $1002)" "\n"
        "MOVE.W -(A0),D0      prédécrémentation       oui        $0FFE (A0 décrémenté de 2)" "\n"
        "MOVE.W $1000,D0      absolu long             oui        $1000" "\n"
        "```" "\n"
        "" "\n"
        "Un mode **direct** ou **immédiat** ne spécifie pas d'emplacement mémoire ; les modes **indirects** et **absolus** en spécifient un (test de cours : « le mode d'adressage direct ne spécifie pas d'emplacement mémoire », « la valeur de `MOVE.W $5000,D0` est une adresse sur 32 bits »).", src="Chapitre 1 du cours (D. Bouchet), IV-1 ; Test 1, questions 6 à 10", duree=6),
    ]},
    {"n": 7, "titre": "Adresse effective : d16(An), d8(An,Xn), absolu, PC", "notions": ["ea"], "exos": [
        v("e71", "Dans `MOVE.W 4(A1),D0` :" "\n"
        "" "\n"
        "```" "\n"
        "A1 = $00001008" "\n"
        "```" "\n"
        "" "\n"
        "Quelle est l'adresse effective de l'opérande `4(A1)` ?", "hexa('1008')+4", "hexa('100C')", "A1 vaut `$1008` : A1 plus" "\n"
        "$4$ donne" "\n"
        "`$100C`.", src="Chapitre 1 du cours (D. Bouchet), IV-3.4"),
        v("e72", "Dans `MOVE.W 1(A1,D3.L),D0` :" "\n"
        "" "\n"
        "```" "\n"
        "D3 = $00000003   A1 = $00001008" "\n"
        "```" "\n"
        "" "\n"
        "Quelle est l'adresse effective de l'opérande `1(A1,D3.L)` ?", "hexa('1008')+1+3", "hexa('100C')", "A1 vaut `$1008`, d8 vaut" "\n"
        "$1$, D3.L vaut $3$ :" "\n"
        "`$100C`.", src="Chapitre 1 du cours (D. Bouchet), IV-3.5"),
        v("e73", "Dans `MOVE.B $5006,34(A2,D1.L)` on s'intéresse à l'opérande destination :" "\n"
        "" "\n"
        "```" "\n"
        "D1 = $FFFFFFE0   A2 = $0000500A" "\n"
        "```" "\n"
        "" "\n"
        "Quelle est l'adresse effective de l'opérande `34(A2,D1.L)` ?", "hexa('500A')+34+(hexa('FFFFFFE0')-2**32)", "hexa('500C')", "D1.L vaut `$FFFFFFE0`, soit" "\n"
        "$-32$ en complément à deux. Adresse :" "\n"
        "`$500A` plus" "\n"
        "$34$ moins $32$ donne" "\n"
        "`$500C`.", src="TP 2, étape 4"),
        v("e74", "Dans `MOVE.L $11(A1,D0.W),-$1A(A0,D2.L)` on s'intéresse à la source :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $FFFF0005   A1 = $00005008" "\n"
        "```" "\n"
        "" "\n"
        "Quelle est l'adresse effective de l'opérande `$11(A1,D0.W)` ?", "hexa('5008')+hexa('11')+5", "hexa('501E')", "L'index est D0.W (mot signé) : D0.W vaut `$0005`, donc" "\n"
        "$5$. Adresse :" "\n"
        "`$5008` plus" "\n"
        "`$11` plus" "\n"
        "$5$ donne" "\n"
        "`$501E`.", src="TP 2, étape 4"),
        v("e75", "Dans la destination `-$1A(A0,D2.L)` :" "\n"
        "" "\n"
        "```" "\n"
        "D2 = $00000025   A0 = $00005000" "\n"
        "```" "\n"
        "" "\n"
        "Quelle est l'adresse effective de l'opérande `-$1A(A0,D2.L)` ?", "hexa('5000')-hexa('1A')+hexa('25')", "hexa('500B')", "A0 vaut `$5000`, D2.L vaut" "\n"
        "`$25` :" "\n"
        "`$5000` moins" "\n"
        "`$1A` plus" "\n"
        "`$25` donne" "\n"
        "`$500B`. Cette adresse est **impaire** : avec `MOVE.L` l'exécution provoque une erreur d'adresse (voir l'exercice suivant).", src="TP 2, étape 4"),
        v("e76", "Même mémoire que le cours :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $11223344   A0 = $00001000" "\n"
        "D1 = $AABBCCDD   A1 = $00001008" "\n"
        "D2 = $0000FFFF   A2 = $00001010" "\n"
        "D3 = $00000003   A3 = $00000006" "\n"
        "$001000  21 45 87 AF B5 F3 3C 32" "\n"
        "$001008  AD 45 39 98 9A 9B 9C 9D" "\n"
        "$001010  03 69 01 00 12 0A 0D C9" "\n"
        "```" "\n"
        "" "\n"
        "Quelle est la valeur de D0.W après `MOVE.W $100C,D0` ?" "\n"
        "(`$100C` est une adresse absolue.)", "154*256+155", "hexa('9A9B')", "Le mode absolu lit directement à `$100C` : octets `9A 9B`, donc D0.W vaut" "\n"
        "`$9A9B`.", src="Chapitre 1 du cours (D. Bouchet), IV-3.8"),
        v("e77", "Même mémoire :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $11223344   A0 = $00001000" "\n"
        "D1 = $AABBCCDD   A1 = $00001008" "\n"
        "D2 = $0000FFFF   A2 = $00001010" "\n"
        "D3 = $00000003   A3 = $00000006" "\n"
        "$001000  21 45 87 AF B5 F3 3C 32" "\n"
        "$001008  AD 45 39 98 9A 9B 9C 9D" "\n"
        "$001010  03 69 01 00 12 0A 0D C9" "\n"
        "```" "\n"
        "" "\n"
        "Quelle est la valeur de D0 après `MOVE.B $1010(PC),D0` ? (Dans le source, on écrit l'adresse effective ; l'assembleur calcule le déplacement par rapport au PC.)", "hexa('11223344')-hexa('11223344')%256+3", "hexa('11223303')", "L'adresse effective est `$1010` : l'octet vaut" "\n"
        "`$03`. Seul D0.B change : D0 vaut" "\n"
        "`$11223303`.", src="Chapitre 1 du cours (D. Bouchet), IV-3.6"),
        v("e78", "Quel est le plus grand déplacement positif d'un mode `d16(An)` (déplacement signé sur $16$ bits) ?", "2**15-1", "32767", r"$d_{16}\in[-32768,32767]$ : le plus grand est $2^{15}-1=32767$.", src="Chapitre 1 du cours (D. Bouchet), IV-3.4"),
        o("e79", "Dans le TP 2, l'instruction `MOVE.L $11(A1,D0.W),-$1A(A0,D2.L)` est acceptée par l'assembleur, mais elle provoque une erreur à l'exécution. Pourquoi ? Avec A0" "\n"
        "`$5000`, A1" "\n"
        "`$5008`, D0" "\n"
        "`$FFFF0005`, D2" "\n"
        "`$25`, quelles sont les adresses effectives ?", "Source : D0.W vaut `$0005` (l'index `.W` est le mot de poids faible, étendu en signe), donc A1 plus" "\n"
        "`$11` plus" "\n"
        "$5$ donne" "\n"
        "`$501E` (adresse paire, accès valide)." "\n"
        "" "\n"
        "Destination : A0 vaut `$5000` et D2.L vaut" "\n"
        "`$25` :" "\n"
        "`$5000` moins" "\n"
        "`$1A` plus" "\n"
        "`$25` donne" "\n"
        "`$500B`." "\n"
        "" "\n"
        "L'adresse `$500B` est **impaire** et l'opération est sur" "\n"
        "$32$ bits (`.L`) : le 68000 ne peut accéder à un mot ou à un mot long qu'à une adresse paire, il y a une erreur d'adresse. Cette erreur est **dynamique** : elle dépend du contenu des registres au moment de l'exécution, l'assembleur ne peut pas la détecter.", src="TP 2, étape 4 (corrigé)", duree=5),
    ]},
    {"n": 8, "titre": "MOVE : ce qui change en mémoire et dans les registres", "notions": ["memmove"], "exos": [
        v("g81", "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $0000FFFF   A0 = $00001000" "\n"
        "D1 = $00000004   A1 = $00001008" "\n"
        "D2 = $FFFFF000   A2 = $00001010" "\n"
        "$001000  21 45 87 AF B5 F3 3C 32" "\n"
        "$001008  AD 45 39 98 9A 9B 9C 9D" "\n"
        "$001010  03 69 01 00 12 0A 0D C9" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVE.W #36,(A0)`. Donner les $8$ octets de la mémoire à partir de" "\n"
        "`$1000` après l'instruction, écrits comme un seul nombre hexadécimal de" "\n"
        "$16$ chiffres.", "hexa(''+'0024'+'87AFB5F33C32')", "hexa('002487AFB5F33C32')", "Avant : `214587AFB5F33C32`. L'instruction écrit `0024` à partir de l'octet n° 0 de la fenêtre (adresse `$1000`) ; les autres octets ne changent pas. Après : `002487AFB5F33C32`.", src="Chapitre 1 du cours (D. Bouchet), IV-4.5"),
        v("g82", "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $0000FFFF   A0 = $00001000" "\n"
        "D1 = $00000004   A1 = $00001008" "\n"
        "D2 = $FFFFF000   A2 = $00001010" "\n"
        "$001000  21 45 87 AF B5 F3 3C 32" "\n"
        "$001008  AD 45 39 98 9A 9B 9C 9D" "\n"
        "$001010  03 69 01 00 12 0A 0D C9" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVE.B D1,(A1)+`. Donner les $8$ octets de la mémoire à partir de" "\n"
        "`$1008` après l'instruction, écrits comme un seul nombre hexadécimal de" "\n"
        "$16$ chiffres.", "hexa(''+'04'+'4539989A9B9C9D')", "hexa('044539989A9B9C9D')", "Avant : `AD4539989A9B9C9D`. L'instruction écrit `04` à partir de l'octet n° 0 de la fenêtre (adresse `$1008`) ; les autres octets ne changent pas. Après : `044539989A9B9C9D`.", src="Chapitre 1 du cours (D. Bouchet), IV-4.6"),
        v("g83", "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $0000FFFF   A0 = $00001000" "\n"
        "D1 = $00000004   A1 = $00001008" "\n"
        "D2 = $FFFFF000   A2 = $00001010" "\n"
        "$001000  21 45 87 AF B5 F3 3C 32" "\n"
        "$001008  AD 45 39 98 9A 9B 9C 9D" "\n"
        "$001010  03 69 01 00 12 0A 0D C9" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVE.L $1004,-(A2)`. Donner les" "\n"
        "$8$ octets de la mémoire à partir de" "\n"
        "`$1008` après l'instruction, écrits comme un seul nombre hexadécimal de" "\n"
        "$16$ chiffres.", "hexa('AD453998'+'B5F33C32'+'')", "hexa('AD453998B5F33C32')", "Avant : `AD4539989A9B9C9D`. L'instruction écrit `B5F33C32` à partir de l'octet n° 4 de la fenêtre (adresse `$100C`) ; les autres octets ne changent pas. Après : `AD453998B5F33C32`.", src="Chapitre 1 du cours (D. Bouchet), IV-4.7"),
        v("g84", "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $0000FFFF   A0 = $00001000" "\n"
        "D1 = $00000004   A1 = $00001008" "\n"
        "D2 = $FFFFF000   A2 = $00001010" "\n"
        "$001000  21 45 87 AF B5 F3 3C 32" "\n"
        "$001008  AD 45 39 98 9A 9B 9C 9D" "\n"
        "$001010  03 69 01 00 12 0A 0D C9" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVE.B 5(A1),-1(A1,D0.W)`. Donner les $8$ octets de la mémoire à partir de" "\n"
        "`$1000` après l'instruction, écrits comme un seul nombre hexadécimal de" "\n"
        "$16$ chiffres.", "hexa('214587AFB5F3'+'9B'+'32')", "hexa('214587AFB5F39B32')", "Avant : `214587AFB5F33C32`. L'instruction écrit `9B` à partir de l'octet n° 6 de la fenêtre (adresse `$1006`) ; les autres octets ne changent pas. Après : `214587AFB5F39B32`.", src="Chapitre 1 du cours (D. Bouchet), IV-4.9"),
        v("g85", "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $0000FFFF   A0 = $00001000" "\n"
        "D1 = $00000004   A1 = $00001008" "\n"
        "D2 = $FFFFF000   A2 = $00001010" "\n"
        "$001000  21 45 87 AF B5 F3 3C 32" "\n"
        "$001008  AD 45 39 98 9A 9B 9C 9D" "\n"
        "$001010  03 69 01 00 12 0A 0D C9" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVE.W 2(A1,D1.L),-6(A2)`. Donner les $8$ octets de la mémoire à partir de" "\n"
        "`$1008` après l'instruction, écrits comme un seul nombre hexadécimal de" "\n"
        "$16$ chiffres.", "hexa('AD45'+'9C9D'+'9A9B9C9D')", "hexa('AD459C9D9A9B9C9D')", "Avant : `AD4539989A9B9C9D`. L'instruction écrit `9C9D` à partir de l'octet n° 2 de la fenêtre (adresse `$100A`) ; les autres octets ne changent pas. Après : `AD459C9D9A9B9C9D`.", src="Chapitre 1 du cours (D. Bouchet), IV-4.10"),
        v("g86", "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $0000FFFF   A0 = $00001000" "\n"
        "D1 = $00000004   A1 = $00001008" "\n"
        "D2 = $FFFFF000   A2 = $00001010" "\n"
        "$001000  21 45 87 AF B5 F3 3C 32" "\n"
        "$001008  AD 45 39 98 9A 9B 9C 9D" "\n"
        "$001010  03 69 01 00 12 0A 0D C9" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVE.W $1000(PC),$100A`. Donner les" "\n"
        "$8$ octets de la mémoire à partir de" "\n"
        "`$1008` après l'instruction, écrits comme un seul nombre hexadécimal de" "\n"
        "$16$ chiffres.", "hexa('AD45'+'2145'+'9A9B9C9D')", "hexa('AD4521459A9B9C9D')", "Avant : `AD4539989A9B9C9D`. L'instruction écrit `2145` à partir de l'octet n° 2 de la fenêtre (adresse `$100A`) ; les autres octets ne changent pas. Après : `AD4521459A9B9C9D`.", src="Chapitre 1 du cours (D. Bouchet), IV-4.11"),
        v("g87", "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $FFFFFFFB   A0 = $00005000" "\n"
        "D1 = $00000008   A1 = $00005008" "\n"
        "D2 = $4444FFFE   A2 = $00005010" "\n"
        "$005000  54 AF 18 B9 E7 21 48 C0" "\n"
        "$005008  C9 10 11 C8 D4 36 1F 88" "\n"
        "$005010  13 79 01 80 42 1A 2D 49" "\n"
        "```" "\n"
        "" "\n"
        "Quelle est la valeur de A1 après `MOVE.L #$5006,-(A1)` ?", "hexa('5008')-4", "hexa('5004')", "La prédécrémentation retire la taille de l'instruction ($4$ pour `.L`) avant l'écriture : A1 vaut" "\n"
        "`$5004`.", src="Contrôle S3 2025/2026, ex. 1"),
        o("g88", "Réécrire chacune de ces instructions avec des instructions sans postincrémentation, sans prédécrémentation et sans index, de façon que les registres et la mémoire finals soient identiques :" "\n"
        "" "\n"
        "```asm" "\n"
        "MOVE.B #$51,(A0)+" "\n"
        "MOVE.W #$4A6B,-(A2)" "\n"
        "MOVE.W #$2233,-1(A4,D1.L)" "\n"
        "```", "On remplace chaque mode d'adressage par un `MOVE` en `(An)` et des `ADDA`/`SUBA` sur le registre d'adresse :" "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVE.B  #$51,(A0)        ; (A0)+ : écrire puis avancer" "\n"
        "        ADDA.L  #1,A0" "\n"
        "" "\n"
        "        SUBA.L  #2,A2            ; -(A2) : reculer puis écrire" "\n"
        "        MOVE.W  #$4A6B,(A2)" "\n"
        "" "\n"
        "        ADDA.L  D1,A4            ; -1(A4,D1.L) : A4 + D1 - 1" "\n"
        "        SUBA.L  #1,A4" "\n"
        "        MOVE.W  #$2233,(A4)" "\n"
        "        SUBA.L  D1,A4            ; on restaure A4" "\n"
        "        ADDA.L  #1,A4" "\n"
        "```" "\n"
        "" "\n"
        "Pour l'adresse effective, il faut que A4 redevienne ce qu'il était à la fin. Corrigé rédigé : j'ai exécuté les deux versions sur un émulateur 68000 avec les mêmes registres initiaux (A0 `$550`, A2" "\n"
        "`$558`, A4" "\n"
        "`$560`, D1" "\n"
        "$=5$) : mémoire et registres finals sont identiques.", src="TP 2, étape 6", duree=8),
    ]},
    {"n": 9, "titre": "Arithmétique et logique : ADDQ, NEG, NOT, AND, MULU, DIVU, ADDX, décalages", "notions": ["arith"], "exos": [
        v("ar91", "Registres initiaux :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $1234FFFE" "\n"
        "```" "\n"
        "" "\n"
        "Que contient D0 après `ADDQ.W #3,D0` ?", "(hexa('1234FFFE')-hexa('1234FFFE')%2**16)+(hexa('1234FFFE')%2**16+3)%2**16", "hexa('12340001')", "Sur $16$ bits :" "\n"
        "`$FFFE` plus" "\n"
        "$3$ donne" "\n"
        "`$10001`, on garde" "\n"
        "`$0001` ; les" "\n"
        "$16$ bits de poids fort ne changent pas. D0 vaut" "\n"
        "`$12340001`.", src="Chapitre 1 du cours (D. Bouchet), VIII-2"),
        v("ar92", "Registres initiaux :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $00000005" "\n"
        "```" "\n"
        "" "\n"
        "Que contient D0 après `NEG.B D0` ?", "(hexa('00000005')-hexa('00000005')%2**8)+(-hexa('00000005')%2**8)%2**8", "hexa('000000FB')", "`NEG` calcule $0-D0.B=-5$, c'est-à-dire" "\n"
        "`$FB` sur" "\n"
        "$8$ bits ; D0 vaut" "\n"
        "`$000000FB`.", src="Chapitre 1 du cours (D. Bouchet), VIII-2.5"),
        v("ar93", "Registres initiaux :" "\n"
        "" "\n"
        "```" "\n"
        "D1 = $12345678" "\n"
        "```" "\n"
        "" "\n"
        "Que contient D1 après `NOT.W D1` ?", "(hexa('12345678')-hexa('12345678')%2**16)+(2**16-1-hexa('12345678')%2**16)%2**16", "hexa('1234A987')", "`NOT.W` inverse les $16$ bits de poids faible :" "\n"
        "`$5678` devient" "\n"
        "`$A987`. D1 vaut" "\n"
        "`$1234A987`.", src="Chapitre 1 du cours (D. Bouchet), VIII-3"),
        v("ar94", "Registres initiaux :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $ABCDEF12" "\n"
        "```" "\n"
        "" "\n"
        "Que contient D0 après `AND.L #$0000FFFF,D0` ?", "hexa('ABCDEF12')&hexa('0000FFFF')", "hexa('0000EF12')", "Le ET bit à bit avec `$0000FFFF` annule les" "\n"
        "$16$ bits de poids fort et conserve les autres : D0 vaut" "\n"
        "`$0000EF12`.", src="Chapitre 1 du cours (D. Bouchet), VIII-3"),
        v("ar95", "Registres initiaux :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $0000012C" "\n"
        "D1 = $FFFF0064" "\n"
        "```" "\n"
        "" "\n"
        "Que contient D0 après `MULU.W D1,D0` ?", "(hexa('0000012C')%2**16)*(hexa('FFFF0064')%2**16)", "hexa('00007530')", "`MULU.W` multiplie les mots de poids faible : D0.W $=300$ et D1.W $=100$" "\n"
        "(`$0064`)." "\n"
        r"$300\times100=30000$, soit" "\n"
        "`$7530` ; le résultat occupe tout D0 :" "\n"
        "`$00007530`.", src="Chapitre 1 du cours (D. Bouchet), VIII-2.3 ; TP 4, Atoui"),
        v("ar96", "Registres initiaux :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $000004D2" "\n"
        "```" "\n"
        "" "\n"
        "Que contient D0 après `DIVU.W #10,D0` ? (`$4D2` vaut" "\n"
        "$1234$.)", "(hexa('4D2')%10)*2**16+hexa('4D2')//10", "hexa('0004007B')", r"$1234=10\times123+4$ : le quotient $123$" "\n"
        "(`$007B`) va dans D0.W et le reste" "\n"
        "$4$ dans les $16$ bits de poids fort. D0 vaut" "\n"
        "`$0004007B`.", src="Chapitre 1 du cours (D. Bouchet), VIII-2.4"),
        v("ar97", "Registres initiaux :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $FFFFFFFF" "\n"
        "D1 = $00000005" "\n"
        "D2 = $00000001" "\n"
        "D3 = $00000002" "\n"
        "```" "\n"
        "" "\n"
        "On additionne les entiers de $64$ bits D1:D0 et D3:D2 avec `ADD.L D2,D0` puis `ADDX.L D3,D1`. Que contient D1 à la fin ?", "(5+2+(hexa('FFFFFFFF')+1)//2**32)%2**32", "hexa('00000008')", "`ADD.L D2,D0` : `$FFFFFFFF` plus" "\n"
        "$1$ déborde de $32$ bits : D0 vaut" "\n"
        "`$00000000` et" "\n"
        "X$=1$ (retenue). `ADDX.L D3,D1` additionne D1, D3 et X : $5+2+1=8$. D1 vaut" "\n"
        "`$00000008`.", src="TP 1, étape 6 (addition sur 128 bits)"),
        v("ar98", "Registres initiaux :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $00000F0F" "\n"
        "```" "\n"
        "" "\n"
        "Que contient D0 après `LSL.W #2,D0` ?", "(hexa('00000F0F')-hexa('00000F0F')%2**16)+(hexa('0F0F')%2**16*4)%2**16", "hexa('00003C3C')", "Décalage logique de $2$ bits vers la gauche :" "\n"
        "`$0F0F` devient" "\n"
        "`$3C3C`. D0 vaut" "\n"
        "`$00003C3C`.", src="Chapitre 1 du cours (D. Bouchet), VIII-4"),
        o("ar99", "Écrire un programme qui additionne deux entiers de $128$ bits : `D3:D2:D1:D0` (D0 : $32$ bits de poids faible) et `D7:D6:D5:D4` (D4 : $32$ bits de poids faible). Le résultat est placé dans `D3:D2:D1:D0`.", "On additionne mot long par mot long, en propageant la retenue grâce au drapeau X :" "\n"
        "" "\n"
        "```asm" "\n"
        "        ADD.L   D4,D0      ; D0 + D4 -> D0, retenue -> X" "\n"
        "        ADDX.L  D5,D1      ; D1 + D5 + X -> D1, retenue -> X" "\n"
        "        ADDX.L  D6,D2      ; D2 + D6 + X -> D2, retenue -> X" "\n"
        "        ADDX.L  D7,D3      ; D3 + D7 + X -> D3" "\n"
        "```" "\n"
        "" "\n"
        "`ADD` ne tient pas compte de X, `ADDX` l'ajoute. Corrigé vérifié sur un émulateur 68000 avec $20$ couples d'entiers de $128$ bits tirés au hasard (résultat égal à la somme modulo $2^{128}$).", src="TP 1, étape 6", duree=6),
    ]},
    {"n": 10, "titre": "Rotations ROR, ROL et SWAP", "notions": ["rotation"], "exos": [
        v("ro101", "D4 vaut `$12345678`. On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "ROR.W #4,D4" "\n"
        "```" "\n"
        "" "\n"
        "Quelle est la valeur finale de D4 ?", "(lambda x: (x-x%65536)+((((x%65536)>>4)|((x%65536)<<12))%65536))(hexa('12345678'))", "hexa('12348567')", "On suit les $8$ chiffres hexadécimaux à chaque instruction :" "\n"
        "" "\n"
        "```asm" "\n"
        "; D4 = $12345678" "\n"
        "ROR.W #4,D4    ; D4 = $12348567" "\n"
        "```" "\n"
        "" "\n"
        "On obtient `$12348567`.", src="Chapitre 1 du cours (D. Bouchet), VIII-4"),
        v("ro102", "D1 vaut `$12345678`. On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "ROL.B #4,D1" "\n"
        "```" "\n"
        "" "\n"
        "Quelle est la valeur finale de D1 ?", "(lambda x: (x-x%256)+((((x%256)>>4)|((x%256)<<4))%256))(hexa('12345678'))", "hexa('12345687')", "On suit les $8$ chiffres hexadécimaux à chaque instruction :" "\n"
        "" "\n"
        "```asm" "\n"
        "; D1 = $12345678" "\n"
        "ROL.B #4,D1    ; D1 = $12345687" "\n"
        "```" "\n"
        "" "\n"
        "On obtient `$12345687`.", src="Chapitre 1 du cours (D. Bouchet), VIII-4"),
        v("ro103", "D0 vaut `$12345678`. On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "ROR.L #8,D0" "\n"
        "```" "\n"
        "" "\n"
        "Quelle est la valeur finale de D0 ?", "(lambda x: (x-x%4294967296)+((((x%4294967296)>>8)|((x%4294967296)<<24))%4294967296))(hexa('12345678'))", "hexa('78123456')", "On suit les $8$ chiffres hexadécimaux à chaque instruction :" "\n"
        "" "\n"
        "```asm" "\n"
        "; D0 = $12345678" "\n"
        "ROR.L #8,D0    ; D0 = $78123456" "\n"
        "```" "\n"
        "" "\n"
        "On obtient `$78123456`.", src="Chapitre 1 du cours (D. Bouchet), VIII-4"),
        v("ro104", "D3 vaut `$12345678`. On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "SWAP D3" "\n"
        "```" "\n"
        "" "\n"
        "Quelle est la valeur finale de D3 ?", "(lambda x: (x%65536)*65536+x//65536)(hexa('12345678'))", "hexa('56781234')", "On suit les $8$ chiffres hexadécimaux à chaque instruction :" "\n"
        "" "\n"
        "```asm" "\n"
        "; D3 = $12345678" "\n"
        "SWAP D3        ; D3 = $56781234" "\n"
        "```" "\n"
        "" "\n"
        "On obtient `$56781234`.", src="Chapitre 1 du cours (D. Bouchet), VIII-4"),
        v("ro105", "D4 vaut `$12345678`. On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "ROR.W #4,D4" "\n"
        "ROR.L #8,D4" "\n"
        "SWAP D4" "\n"
        "ROL.B #4,D4" "\n"
        "ROR.L #8,D4" "\n"
        "```" "\n"
        "" "\n"
        "Quelle est la valeur finale de D4 ?", "(lambda x: (x-x%4294967296)+((((x%4294967296)>>8)|((x%4294967296)<<24))%4294967296))((lambda x: (x-x%256)+((((x%256)>>4)|((x%256)<<4))%256))((lambda x: (x%65536)*65536+x//65536)((lambda x: (x-x%4294967296)+((((x%4294967296)>>8)|((x%4294967296)<<24))%4294967296))((lambda x: (x-x%65536)+((((x%65536)>>4)|((x%65536)<<12))%65536))(hexa('12345678'))))))", "hexa('21348567')", "On suit les $8$ chiffres hexadécimaux à chaque instruction :" "\n"
        "" "\n"
        "```asm" "\n"
        "; D4 = $12345678" "\n"
        "ROR.W #4,D4    ; D4 = $12348567" "\n"
        "ROR.L #8,D4    ; D4 = $67123485" "\n"
        "SWAP D4        ; D4 = $34856712" "\n"
        "ROL.B #4,D4    ; D4 = $34856721" "\n"
        "ROR.L #8,D4    ; D4 = $21348567" "\n"
        "```" "\n"
        "" "\n"
        "On obtient `$21348567`.", src="Contrôle S3 2025/2026, ex. 4"),
        v("ro106", "D1 vaut `$76543210`. On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "ROR.B #4,D1" "\n"
        "ROL.L #8,D1" "\n"
        "ROR.W #4,D1" "\n"
        "SWAP D1" "\n"
        "ROL.W #4,D1" "\n"
        "```" "\n"
        "" "\n"
        "Quelle est la valeur finale de D1 ?", "(lambda x: (x-x%65536)+((((x%65536)>>12)|((x%65536)<<4))%65536))((lambda x: (x%65536)*65536+x//65536)((lambda x: (x-x%65536)+((((x%65536)>>4)|((x%65536)<<12))%65536))((lambda x: (x-x%4294967296)+((((x%4294967296)>>24)|((x%4294967296)<<8))%4294967296))((lambda x: (x-x%256)+((((x%256)>>4)|((x%256)<<4))%256))(hexa('76543210'))))))", "hexa('60174325')", "On suit les $8$ chiffres hexadécimaux à chaque instruction :" "\n"
        "" "\n"
        "```asm" "\n"
        "; D1 = $76543210" "\n"
        "ROR.B #4,D1    ; D1 = $76543201" "\n"
        "ROL.L #8,D1    ; D1 = $54320176" "\n"
        "ROR.W #4,D1    ; D1 = $54326017" "\n"
        "SWAP D1        ; D1 = $60175432" "\n"
        "ROL.W #4,D1    ; D1 = $60174325" "\n"
        "```" "\n"
        "" "\n"
        "On obtient `$60174325`.", src="Contrôle S3 2020/2021, ex. 3"),
        o("ro107", "La valeur initiale de D1 est `$12345678`. En utilisant uniquement les instructions `SWAP`, `ROR` et `ROL`, donner au plus 3 lignes d'instructions qui transforment D1 en" "\n"
        "`$67581234`.", "```asm" "\n"
        "        ROL.W #4,D1 ; D1 = $12346785" "\n"
        "        ROL.B #4,D1 ; D1 = $12346758" "\n"
        "        SWAP D1     ; D1 = $67581234" "\n"
        "```" "\n"
        "" "\n"
        "Méthode : on repère où va chaque chiffre. Le résultat `67 58 12 34` est un `SWAP` de `12 34 67 58` ; le mot de poids faible `5678` doit devenir `6758`, ce qui est une rotation de $4$ bits vers la gauche du mot (`6785`) suivie d'un échange des deux derniers chiffres (`6758`)." "\n"
        "" "\n"
        "Il existe plusieurs solutions ; celle-ci a été exécutée sur un émulateur 68000 (corrigé rédigé, conforme au corrigé officiel).", src="Partiel S3 2025/2026, ex. 4", duree=8),
        o("ro108", "La valeur initiale de D1 est `$87654321`. En utilisant uniquement les instructions `SWAP`, `ROR` et `ROL`, donner au plus 3 lignes d'instructions qui transforment D1 en" "\n"
        "`$43215687`.", "```asm" "\n"
        "        SWAP D1     ; D1 = $43218765" "\n"
        "        ROL.B #4,D1 ; D1 = $43218756" "\n"
        "        ROL.W #8,D1 ; D1 = $43215687" "\n"
        "```" "\n"
        "" "\n"
        "Méthode : `SWAP` met `4321` en tête (`43218765`). Il faut ensuite `5687` à la place de `8765` : on échange les deux derniers chiffres (`ROL.B #4` donne `8756`) puis les deux octets du mot (`ROL.W #8` donne `5687`)." "\n"
        "" "\n"
        "Il existe plusieurs solutions ; celle-ci a été exécutée sur un émulateur 68000 (corrigé rédigé, conforme au corrigé officiel).", src="Partiel S3 2023/2024, ex. 4", duree=8),
        o("ro109", "La valeur initiale de D1 est `$76543210`. En utilisant uniquement les instructions `SWAP`, `ROR` et `ROL`, donner au plus 4 lignes d'instructions qui transforment D1 en" "\n"
        "`$54231067`.", "```asm" "\n"
        "        ROR.L #8,D1 ; D1 = $10765432" "\n"
        "        ROR.B #4,D1 ; D1 = $10765423" "\n"
        "        SWAP D1     ; D1 = $54231076" "\n"
        "        ROR.B #4,D1 ; D1 = $54231067" "\n"
        "```" "\n"
        "" "\n"
        "Méthode : `ROR.L #8` ramène l'octet `10` en tête (`10765432`). `ROR.B #4` échange `32` en `23`. `SWAP` donne `54231076`, puis `ROR.B #4` échange `76` en `67`." "\n"
        "" "\n"
        "Il existe plusieurs solutions ; celle-ci a été exécutée sur un émulateur 68000 (corrigé rédigé, conforme au corrigé officiel).", src="Contrôle S3 2016/2017, ex. 3", duree=8),
    ]},
    {"n": 11, "titre": "TST, CMP et branchements conditionnels (signé et non signé)", "notions": ["branch"], "exos": [
        v("b111", "Valeur initiale :" "\n"
        "" "\n"
        "```" "\n"
        "D7 = $23456789" "\n"
        "```" "\n"
        "" "\n"
        "On exécute le programme :" "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVEQ.L #1,D1" "\n"
        "        TST.B   D7" "\n"
        "        BMI     NEXT" "\n"
        "        MOVEQ.L #2,D1" "\n"
        "NEXT" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D1 à la fin ?", "1 if (lambda x: x-2**8*(x//2**7))((hexa('89'))%2**8)<0 else 2", "hexa('00000001')", "`TST.B D7` ne regarde que D7.B (`$89`). Son bit de poids fort est à" "\n"
        "$1$ : N$=1$, `BMI` saute à `NEXT`, `MOVEQ.L #2,D1` n'est pas exécuté : D1 vaut" "\n"
        "`$00000001`.", src="Contrôle S3 2016/2017, ex. 5"),
        v("b112", "Valeur initiale :" "\n"
        "" "\n"
        "```" "\n"
        "D7 = $52A59382" "\n"
        "```" "\n"
        "" "\n"
        "On exécute le programme :" "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVEQ.L #1,D1" "\n"
        "        CMP.W   #$7000,D7" "\n"
        "        BGT     PART2" "\n"
        "        MOVEQ.L #2,D1" "\n"
        "PART2" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D1 à la fin ?", "1 if (lambda x: x-2**16*(x//2**15))((hexa('9382'))%2**16)>28672 else 2", "hexa('00000002')", "`CMP.W #$7000,D7` compare D7.W" "\n"
        "(`$9382`, soit" "\n"
        "$-27774$ en signé) à" "\n"
        "`$7000`" "\n"
        "($28672$). `BGT` est une comparaison **signée** : il n'y a pas de saut (D7.W ≤ $28672$), `MOVEQ.L #2,D1` est exécuté : D1 vaut" "\n"
        "`$00000002`.", src="Contrôle S3 2025/2026, ex. 4"),
        v("b113", "Valeur initiale :" "\n"
        "" "\n"
        "```" "\n"
        "D7 = $23456789" "\n"
        "```" "\n"
        "" "\n"
        "On exécute le programme :" "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVEQ.L #1,D6" "\n"
        "        CMP.B   #$70,D7" "\n"
        "        BLT     QUIT" "\n"
        "        MOVEQ.L #2,D6" "\n"
        "QUIT" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D6 à la fin ?", "1 if (lambda x: x-2**8*(x//2**7))((hexa('89'))%2**8)<112 else 2", "hexa('00000001')", "`CMP.B #$70,D7` compare D7.B" "\n"
        "(`$89`, soit" "\n"
        "$-119$ en signé) à" "\n"
        "`$70`" "\n"
        "($112$). `BLT` est signé : le saut est pris, `MOVEQ.L #2,D6` est sauté : D6 vaut" "\n"
        "`$00000001`.", src="Contrôle S3 2016/2017, ex. 5"),
        v("b114", "Même programme avec une comparaison **non signée** (`BLO` au lieu de `BLT`). Valeur initiale :" "\n"
        "" "\n"
        "```" "\n"
        "D7 = $23456789" "\n"
        "```" "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVEQ.L #1,D6" "\n"
        "        CMP.B   #$70,D7" "\n"
        "        BLO     QUIT" "\n"
        "        MOVEQ.L #2,D6" "\n"
        "QUIT" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D6 à la fin ?", "1 if hexa('89')<112 else 2", "hexa('00000002')", "`BLO` est non signé : `$89` vaut" "\n"
        "$137$ et" "\n"
        "`$70` vaut" "\n"
        "$112$. Le saut est non pris, D6 vaut" "\n"
        "`$00000002`. Avec D7.B" "\n"
        "`$89`, `BLT` (signé :" "\n"
        "$-119<112$) saute alors que `BLO` (non signé : $137<112$ est faux) ne saute pas."),
        v("b115", "Valeur initiale :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $FFFFFFFF" "\n"
        "```" "\n"
        "" "\n"
        "On exécute le programme :" "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVEQ.L #1,D5" "\n"
        "        CMP.L   #1,D0" "\n"
        "        BHI     NEXT" "\n"
        "        MOVEQ.L #2,D5" "\n"
        "NEXT" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D5 à la fin ?", "1 if hexa('FFFFFFFF')>1 else 2", "hexa('00000001')", "`CMP.L #1,D0` compare D0 (`$FFFFFFFF`) à" "\n"
        "$1$. `BHI` est non signé : $4294967295>1$, le saut est pris et `MOVEQ.L #2,D5` est sauté : D5 vaut" "\n"
        "`$00000001`. Avec `BGT` (signé :" "\n"
        "$-1>1$ est faux), D5 vaudrait" "\n"
        "`$00000002`.", src="Chapitre 1 du cours (D. Bouchet), V-2.2"),
        v("b116", "On exécute le programme suivant :" "\n"
        "" "\n"
        "```asm" "\n"
        "VALUE   EQU     96" "\n"
        "        MOVE.B  #VALUE,D1" "\n"
        "        TST.B   D1" "\n"
        "        BNE     NEXT1" "\n"
        "        MOVE.L  #200,D0" "\n"
        "        BRA     QUIT" "\n"
        "NEXT1   BMI     NEXT3" "\n"
        "        CMP.B   #$61,D1" "\n"
        "        BLT     NEXT2" "\n"
        "        MOVE.L  #400,D0" "\n"
        "        BRA     QUIT" "\n"
        "NEXT2   MOVE.L  #600,D0" "\n"
        "        BRA     QUIT" "\n"
        "NEXT3   MOVE.L  #800,D0" "\n"
        "QUIT" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D0 à la fin ?", "200 if 96==0 else (800 if 96<0 else (400 if 96>=97 else 600))", "600", "`TST.B D1` met à jour N et Z. D1.B vaut 96, positif et inférieur à $97$" "\n"
        "(`$61`) : `BLT NEXT2` saute : D0 vaut" "\n"
        "$600$.", src="TP 3, étape 2"),
        v("b117", "On exécute le programme suivant :" "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVE.L  #-1,D0" "\n"
        "        TST.L   D0" "\n"
        "        BPL     QUIT" "\n"
        "        NEG.L   D0" "\n"
        "QUIT" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D0 à la fin (en décimal, valeur signée) ?", "abs(-1)", "1", "D0 vaut $-1$, négatif : N$=1$, `BPL` ne saute pas et `NEG.L D0` calcule $0-D0$. D0 vaut $1$.", src="TP 3, étape 3"),
        o("b118", "Le code ci-dessous comporte deux erreurs. Le sous-programme `Eleven` doit renvoyer $1$ dans D0 si D1.L est strictement inférieur à $11$, sinon $2$. Le programme principal doit appeler `Eleven` avec une valeur dans D1.L. Indiquer les deux numéros de ligne fautifs et les deux instructions correctes." "\n"
        "" "\n"
        "```asm" "\n"
        " 1                   org       $4" "\n"
        " 2                   dc.l      Main" "\n"
        " 3" "\n"
        " 4                   org       $500" "\n"
        " 5 Main              moveq.l   #50,d1" "\n"
        " 6                   jmp       Eleven" "\n"
        " 7                   illegal" "\n"
        " 8" "\n"
        " 9 Eleven            cmp.l     11,d1" "\n"
        r"10                   blo       \lower" "\n"
        "11                   moveq.l   #2,d0" "\n"
        "12                   rts" "\n"
        r"13 \lower            moveq.l   #1,d0" "\n"
        "14                   rts" "\n"
        "```", "**Ligne 6** : `jmp Eleven` saute au sous-programme sans empiler d'adresse de retour. Le `rts` de la ligne 12 ou 14 dépilerait donc une valeur quelconque. Il faut appeler le sous-programme : `jsr Eleven` (ou `bsr Eleven`)." "\n"
        "" "\n"
        "**Ligne 9** : `cmp.l 11,d1` compare D1 à la valeur contenue **à l'adresse** $11$ (mode absolu, et adresse impaire). Pour comparer à la constante $11$, il faut le mode immédiat : `cmp.l #11,d1`." "\n"
        "" "\n"
        "Le reste est correct : `blo` compare en non signé D1 à $11$ (`CMP S,D` puis `Bcc` se lit « D condition S »). Corrigé rédigé : version corrigée exécutée sur un émulateur 68000, D0 vaut $2$ pour D1 $=50$ et $1$ pour D1 $=5$.", src="Contrôle S3 2024/2025, ex. 4", duree=6),
        o("b119", r"Après `CMP.L D0,D1`, quel branchement faut-il utiliser pour sauter si D1 $\ge$ D0 en comparaison signée ? Et en comparaison non signée ? Donner les alias de `BHS` et `BLO`. Pourquoi `CMP` et pas `SUB` pour une comparaison ?", "`CMP S,D` calcule $D-S$ : le branchement se lit « D condition S ». Ici D est D1 et S est D0." "\n"
        "" "\n"
        "- signé : `BGE` (Greater or Equal), $N=V$ ;" "\n"
        "- non signé : `BHS` (Higher or Same), $C=0$." "\n"
        "" "\n"
        "`BHS` est un alias de `BCC` (Carry Clear) et `BLO` est un alias de `BCS` (Carry Set). Pour tester l'égalité on utilise `BEQ` / `BNE` ($Z$)." "\n"
        "" "\n"
        "`CMP` ne stocke pas le résultat de la soustraction : D1 reste inchangé, seuls N, Z, V, C sont mis à jour. Avec `SUB` on perdrait la valeur de D1.", src="Chapitre 1 du cours (D. Bouchet), V-2.2", duree=5),
    ]},
    {"n": 12, "titre": "Boucles : SUBQ/BNE, DBRA, CMPI", "notions": ["boucle"], "exos": [
        v("l121", "On exécute le programme :" "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVE.L  #260,D0" "\n"
        "        CLR.L   D2" "\n"
        "LOOP    ADDQ.L  #1,D2" "\n"
        "        SUBQ.B  #1,D0" "\n"
        "        BNE     LOOP" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D2 à la fin (en hexadécimal) ?", "(260%256 or 256)//1", "hexa('00000004')", "Seul l'octet de poids faible de D0 est décrémenté et testé. D0.B vaut $4$ (260 modulo $256$) et le pas est $1$ : la boucle fait $4$ tours. D2 vaut" "\n"
        "`$00000004`.", src="Contrôle S3 2025/2026, ex. 4"),
        v("l122", "On exécute le programme :" "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVE.L  #$88664422,D0" "\n"
        "        CLR.L   D2" "\n"
        "LOOP    ADDQ.L  #1,D2" "\n"
        "        SUBQ.W  #2,D0" "\n"
        "        BNE     LOOP" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D2 à la fin ? (donner la valeur de D2)", "(hexa('88664422')%65536)//2", "hexa('00002211')", "`SUBQ.W #2,D0` agit sur D0.W et le pas vaut $2$ : D0.W atteint $0$ après $8721$ tours. D2 vaut" "\n"
        "`$00002211`.", src="Contrôle S3 2024/2025, ex. 5"),
        v("l123", "On exécute le programme :" "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVE.L  #$99999999,D0" "\n"
        "        CLR.L   D3" "\n"
        "LOOP    ADDQ.L  #1,D3" "\n"
        "        DBRA    D0,LOOP" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D3 à la fin ?", "hexa('99999999')%65536+1", "hexa('0000999A')", "`DBRA D0,LOOP` ne regarde que D0.W. Il décrémente D0.W et reboucle tant que le résultat n'est pas `$FFFF` : la boucle fait D0.W" "\n"
        "$+1$ tours. Ici D0.W vaut" "\n"
        "`$9999`, donc" "\n"
        "$39322$ tours : D3 vaut" "\n"
        "`$0000999A`.", src="Contrôle S3 2025/2026, ex. 4"),
        v("l124", "On exécute le programme :" "\n"
        "" "\n"
        "```asm" "\n"
        "        CLR.L   D4" "\n"
        "        MOVEQ.L #10,D0" "\n"
        "LOOP    ADDQ.L  #1,D4" "\n"
        "        ADDQ.L  #1,D0" "\n"
        "        CMPI.L  #30,D0" "\n"
        "        BNE     LOOP" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D4 à la fin ?", "30-10", "hexa('00000014')", "D0 part de $10$ et augmente de $1$ à chaque tour jusqu'à valoir $30$ : $20$ tours. D4 vaut" "\n"
        "`$00000014`.", src="TP 3, étape 1"),
        v("l125", "On exécute le programme :" "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVE.L  #$1200,D0" "\n"
        "        CLR.L   D2" "\n"
        "LOOP    ADDQ.L  #1,D2" "\n"
        "        SUBQ.B  #1,D0" "\n"
        "        BNE     LOOP" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D2 à la fin ?", "(hexa('1200')%256 or 256)", "hexa('00000100')", "D0.B vaut $0$. Le premier `SUBQ.B #1,D0` le fait passer à" "\n"
        "`$FF`, qui n'est pas nul : la boucle continue jusqu'à ce que D0.B retombe à" "\n"
        "$0$, soit $256$ tours. D2 vaut" "\n"
        "`$00000100`."),
        v("l126", "On exécute le programme :" "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVE.W  #$255,D0" "\n"
        "        CLR.L   D3" "\n"
        "LOOP    ADDQ.L  #1,D3" "\n"
        "        SUBQ.B  #1,D0" "\n"
        "        BNE     LOOP" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D3 à la fin ?", "(hexa('255')%256 or 256)", "hexa('00000055')", "`SUBQ.B` ne touche que D0.B : `$255` a pour octet de poids faible" "\n"
        "`$55`. La boucle fait autant de tours que cet octet" "\n"
        "($85$) : D3 vaut" "\n"
        "`$00000055`.", src="Partiel S3 2020/2021, ex. 3"),
        v("l127", "On exécute le programme :" "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVE.W  #$100,D0" "\n"
        "        CLR.L   D4" "\n"
        "LOOP    ADDQ.L  #1,D4" "\n"
        "        DBRA    D0,LOOP" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D4 à la fin ?", "hexa('100')+1", "hexa('00000101')", "D0.W vaut `$100` : `DBRA` fait D0.W" "\n"
        "$+1$ tours, soit $257$ tours. D4 vaut" "\n"
        "`$00000101`.", src="Contrôle S3 2020/2021, ex. 5"),
        o("l128", "Traduire en assembleur 68000 la boucle C ci-dessous (`MAX` vaut $17$). Le corps de la boucle ajoute `i` à une somme conservée dans D1." "\n"
        "" "\n"
        "```c" "\n"
        "#define MAX 17" "\n"
        "int i, somme = 0;" "\n"
        "for (i = 0; i < MAX; i++)" "\n"
        "{" "\n"
        "    somme += i;" "\n"
        "}" "\n"
        "```", "```asm" "\n"
        "MAX     EQU     17" "\n"
        "        CLR.L   D1              ; somme = 0" "\n"
        "        CLR.L   D0              ; i = 0" "\n"
        "        MOVE.L  #MAX,D7" "\n"
        "LOOP    CMP.L   D7,D0           ; compare i et MAX (D0 - D7)" "\n"
        "        BGE     DONE            ; sortie si i >= MAX (comparaison signée)" "\n"
        "        ADD.L   D0,D1           ; corps : somme += i" "\n"
        "        ADDQ.L  #1,D0           ; i++" "\n"
        "        BRA     LOOP" "\n"
        "DONE" "\n"
        "```" "\n"
        "" "\n"
        r"`CMP.L D7,D0` calcule D0 $-$ D7 : `BGE` saute si D0 $\ge$ D7, c'est-à-dire quand `i < MAX` devient faux. Corrigé rédigé : exécuté sur un émulateur 68000, D1 vaut $0+1+\dots+16=136$ à la sortie.", src="Chapitre 1 du cours (D. Bouchet), V-3", duree=7),
    ]},
    {"n": 13, "titre": "Pile, A7 et MOVEM", "notions": ["pile"], "exos": [
        v("p131", "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $11112222   A7 = $00F00006" "\n"
        "D1 = $AAAABBBB" "\n"
        "```" "\n"
        "" "\n"
        "On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVE.W  #$42,-(A7)" "\n"
        "        MOVE.L  #$53,-(A7)" "\n"
        "        MOVE.W  D0,-(A7)" "\n"
        "        MOVE.L  D1,-(A7)" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut A7 à la fin ?", "hexa('F00006')-2-4-2-4", "hexa('EFFFFA')", "Quatre empilements : $2+4+2+4=12$ octets. A7 vaut" "\n"
        "`$F00006` moins" "\n"
        "$12$, soit" "\n"
        "`$EFFFFA`.", src="Chapitre 1 du cours (D. Bouchet), VI-1"),
        v("p132", "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $11112222   A7 = $00F00006" "\n"
        "D1 = $AAAABBBB" "\n"
        "D2 = $00000000" "\n"
        "D3 = $00000000" "\n"
        "```" "\n"
        "" "\n"
        "On exécute le programme suivant (D2 vaut $0$ au départ) :" "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVE.W  #$42,-(A7)" "\n"
        "        MOVE.L  #$53,-(A7)" "\n"
        "        MOVE.W  D0,-(A7)" "\n"
        "        MOVE.L  D1,-(A7)" "\n"
        "        CLR.W   D0" "\n"
        "        CLR.L   D1" "\n"
        "        MOVE.L  (A7)+,D1" "\n"
        "        MOVE.W  (A7)+,D0" "\n"
        "        MOVE.L  (A7)+,D2" "\n"
        "        MOVE.W  (A7)+,D3" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D2 à la fin ?", "hexa('53')", "hexa('00000053')", "La pile est LIFO. Les quatre derniers `MOVE` dépilent dans l'ordre inverse : D1 reçoit `$AAAABBBB`, D0.W reçoit" "\n"
        "`$2222`, D2 reçoit le mot long" "\n"
        "`$00000053`, D3.W reçoit" "\n"
        "`$0042`. D2 vaut" "\n"
        "`$00000053`. A7 est revenu à sa valeur initiale.", src="Chapitre 1 du cours (D. Bouchet), VI-1"),
        v("p133", "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D1 = $11111111   A4 = $44444444" "\n"
        "D2 = $22222222   A5 = $55555555" "\n"
        "D3 = $33333333   A7 = $00F00000" "\n"
        "```" "\n"
        "" "\n"
        "On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVEM.L D1-D3/A4/A5,-(A7)" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut A7 après l'instruction ?", "hexa('F00000')-5*4", "hexa('EFFFEC')", "`MOVEM.L` empile $5$ registres de $4$ octets, soit $20$ octets : A7 vaut" "\n"
        "`$EFFFEC`.", src="Chapitre 1 du cours (D. Bouchet), VI-2"),
        v("p134", "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D1 = $11111111   A4 = $44444444" "\n"
        "D2 = $22222222   A5 = $55555555" "\n"
        "D3 = $33333333   A7 = $00F00000" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVEM.L D1-D3/A4/A5,-(A7)` puis `MOVE.L (A7),D0`. Que vaut D0 ?", "hexa('11111111')", "hexa('11111111')", "Avec `-(A7)`, `MOVEM` utilise l'ordre inversé : A5, puis A4, D3, D2, et D1 en dernier. D1 est donc au sommet de la pile (`(A7)`) : D0 vaut `$11111111`.", src="Chapitre 1 du cours (D. Bouchet), VI-2"),
        v("p135", "A7 vaut `$F00000`. Que vaut A7 après `MOVEM.L (A7)+,A1-A4` ?", "hexa('F00000')+4*4", "hexa('00F00010')", "`MOVEM.L (A7)+,A1-A4` dépile $4$ registres de $4$ octets (A1, A2, A3, A4 dans cet ordre) : A7 augmente de $16$ et vaut" "\n"
        "`$F00010`.", src="Contrôle S3 2025/2026, ex. 3"),
        v("p136", "A7 vaut `$F00000` au début de `Main`. On exécute le programme suivant, qui s'arrête sur l'instruction `ILLEGAL` à la fin de `Sub2` :" "\n"
        "" "\n"
        "```asm" "\n"
        "Main    JSR     Sub1" "\n"
        "        ILLEGAL" "\n"
        "Sub1    JSR     Sub2" "\n"
        "        RTS" "\n"
        "Sub2    MOVEM.L D0-D2,-(A7)" "\n"
        "        ILLEGAL" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut A7 quand le processeur atteint cet `ILLEGAL` ?", "hexa('F00000')-4-4-3*4", "hexa('EFFFEC')", "`JSR Sub1` empile l'adresse de retour ($4$ octets), `JSR Sub2` de même ($4$ octets), puis `MOVEM.L D0-D2,-(A7)` empile $3$ registres ($12$ octets) : $4+4+12=20$ octets de plus. A7 vaut" "\n"
        "`$EFFFEC`.", src="Chapitre 1 du cours (D. Bouchet), VII"),
        v("p137", "A7 vaut `$5004` juste avant l'exécution d'un `RTS`. Que vaut A7 juste après ?", "hexa('5004')+4", "hexa('5008')", "`RTS` dépile l'adresse de retour ($32$ bits) dans le PC : A7 augmente de $4$ et vaut" "\n"
        "`$5008`.", src="Contrôle S3 2023/2024, ex. 4"),
        v("p138", "A7 vaut `$F00000`. On exécute le programme suivant :" "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVEQ.L #5,D0" "\n"
        "        MOVE.L  D0,-(A7)" "\n"
        "        MOVEQ.L #7,D0" "\n"
        "        ADD.L   D0,(A7)" "\n"
        "        MOVEQ.L #3,D0" "\n"
        "        ADD.L   (A7)+,D0" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D0 à la fin (en décimal) ?", "5+7+3", "15", "`MOVE.L D0,-(A7)` empile $5$. `ADD.L D0,(A7)` ajoute D0 ($7$) directement à la valeur au sommet de la pile : la pile contient $12$. `ADD.L (A7)+,D0` ajoute le sommet de pile à D0 ($3$) puis dépile : D0 $=12+3=15$. A7 revient à" "\n"
        "`$F00000` (technique du TP 4, AlphaCount).", src="TP 4, étape 4 (AlphaCount)"),
        o("p139", "À partir de A7 `$F00006`, on exécute" "\n"
        "`MOVE.W #$42,-(A7)`," "\n"
        "`MOVE.L #$53,-(A7)`, `MOVE.W D0,-(A7)` (D0.W vaut" "\n"
        "`$2222`) puis `MOVE.L D1,-(A7)` (D1 vaut" "\n"
        "`$AAAABBBB`). Dessiner la pile (mots de" "\n"
        "$16$ bits) après chaque instruction et donner A7. Que se passe-t-il ensuite avec `MOVE.L (A7)+,D1` ?", "```" "\n"
        "Adresse  apres 1   apres 2   apres 3   apres 4" "\n"
        "F00006   (hors pile)" "\n"
        "F00004   0042      0042      0042      0042" "\n"
        "F00002             0053      0053      0053" "\n"
        "F00000             0000      0000      0000" "\n"
        "EFFFFE                       2222      2222" "\n"
        "EFFFFC                                 BBBB" "\n"
        "EFFFFA                                 AAAA" "\n"
        "A7       F00004    F00000    EFFFFE    EFFFFA" "\n"
        "```" "\n"
        "" "\n"
        "Chaque `MOVE` décrémente A7 de la taille puis écrit. Le mot long `$AAAABBBB` est écrit en big-endian : `AAAA` à l'adresse la plus basse (sommet de pile, `EFFFFA`), `BBBB` ensuite. Le dernier empilé est le premier dépilé (LIFO) : `MOVE.L (A7)+,D1` lit" "\n"
        "`$AAAABBBB` à `EFFFFA` puis A7 augmente de" "\n"
        "$4$ et vaut" "\n"
        "`$EFFFFE`." "\n"
        "" "\n"
        "Vérifié sur un émulateur 68000 (pile, A7 et contenu).", src="Chapitre 1 du cours (D. Bouchet), VI-1", duree=8),
        o("p1310", "Quelle est la différence d'ordre entre `MOVEM.L D1-D3/A4/A5,-(A7)` et `MOVEM.L (A7)+,D1-D3/A4/A5` ? Écrire les instructions `MOVE.L` équivalentes. Pourquoi cet ordre permet-il de restaurer les registres ?", "Avec la prédécrémentation, `MOVEM` traite les registres dans l'ordre **inversé** : A7, A6, ..., A0, D7, ..., D0. Avec tous les autres modes (dont `(A7)+`), c'est l'ordre normal D0, ..., D7, A0, ..., A7." "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVEM.L D1-D3/A4/A5,-(A7)  ; équivaut à :" "\n"
        "        MOVE.L  A5,-(A7)" "\n"
        "        MOVE.L  A4,-(A7)" "\n"
        "        MOVE.L  D3,-(A7)" "\n"
        "        MOVE.L  D2,-(A7)" "\n"
        "        MOVE.L  D1,-(A7)" "\n"
        "" "\n"
        "        MOVEM.L (A7)+,D1-D3/A4/A5  ; équivaut à :" "\n"
        "        MOVE.L  (A7)+,D1" "\n"
        "        MOVE.L  (A7)+,D2" "\n"
        "        MOVE.L  (A7)+,D3" "\n"
        "        MOVE.L  (A7)+,A4" "\n"
        "        MOVE.L  (A7)+,A5" "\n"
        "```" "\n"
        "" "\n"
        "Empilement (ordre inversé) et dépilement (ordre normal) sont symétriques : le dernier empilé (D1) est le premier dépilé (D1). On restaure donc chaque registre avec sa propre valeur, avec la même liste des deux côtés. Équivalence vérifiée sur un émulateur 68000 (même mémoire, mêmes registres).", src="Chapitre 1 du cours (D. Bouchet), VI-2", duree=6),
    ]},
    {"n": 14, "titre": "Sous-programmes : JSR, BSR, RTS et sauvegarde des registres", "notions": ["sousprog"], "exos": [
        v("sp141", "Le sous-programme `GetMin` renvoie dans D0 la plus petite valeur **signée** de D1 et D2 :" "\n"
        "" "\n"
        "```asm" "\n"
        "GetMin  CMP.L   D1,D2" "\n"
        "        BLE     D2MIN" "\n"
        "D1MIN   MOVE.L  D1,D0" "\n"
        "        RTS" "\n"
        "D2MIN   MOVE.L  D2,D0" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "Main    MOVE.L  #15,D1" "\n"
        "        MOVE.L  #25,D2" "\n"
        "        JSR     GetMin" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D0 après l'appel (en hexadécimal sur $32$ bits) ?", "min(15,25)%2**32", "hexa('0000000F')", r"`CMP.L D1,D2` calcule D2 $-$ D1 ; `BLE` (signé) saute si D2 $\le$ D1. Avec D1 $=15$ et D2 $=25$ : D2 est supérieur à D1, on copie D1. Après `RTS`, le programme continue après le `JSR`. D0 vaut" "\n"
        "`$0000000F`.", src="Chapitre 1 du cours (D. Bouchet), VII"),
        v("sp142", "Le sous-programme `Double` double D1 :" "\n"
        "" "\n"
        "```asm" "\n"
        "Double  ADD.L   D1,D1" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "Main    MOVE.L  #3,D1" "\n"
        "        BSR     Double" "\n"
        "        BSR     Double" "\n"
        "        BSR     Double" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D1 à la fin (en décimal) ?", "3*2**3", "24", r"Chaque `BSR Double` double D1 puis `RTS` revient à l'instruction suivante : $3\times2^3=24$.", src="Chapitre 1 du cours (D. Bouchet), VII"),
        v("sp143", "Le sous-programme `Calc` utilise D1 :" "\n"
        "" "\n"
        "```asm" "\n"
        "Calc    MOVEM.L D1,-(A7)" "\n"
        "        MOVE.L  #99,D1" "\n"
        "        MOVEM.L (A7)+,D1" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "Main    MOVE.L  #10,D1" "\n"
        "        BSR     Calc" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D1 après le retour (en décimal) ?", "10", "10", "`Calc` sauvegarde D1 dans la pile avant de le modifier et le restaure juste avant `RTS` : l'appelant retrouve $10$. C'est la consigne des examens : à l'exception des registres de sortie, aucun registre ne doit être modifié."),
        o("sp144", "Écrire le sous-programme `Max` qui renvoie dans D0.L le plus grand des deux entiers **signés** D1.L et D2.L. Aucun registre autre que D0 ne doit être modifié.", "```asm" "\n"
        "Max     CMP.L   D1,D2          ; D2 - D1" "\n"
        r"        BGE     \d2            ; si D2 >= D1 (signé), D2 est le plus grand" "\n"
        "        MOVE.L  D1,D0          ; sinon D1 est le plus grand" "\n"
        "        RTS" "\n"
        r"\d2     MOVE.L  D2,D0" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "On utilise un branchement **signé** (`BGE`) car les entiers sont signés ; seul D0 est écrit, D1 et D2 ne sont pas modifiés, donc rien à sauvegarder. Le même schéma que `GetMin` du cours. Corrigé vérifié sur un émulateur 68000 avec $30$ couples d'entiers signés tirés au hasard (D0 égal au maximum, D5 inchangé).", src="Chapitre 1 du cours (D. Bouchet), VII (GetMin)", duree=7),
        o("sp145", r"Écrire le sous-programme `SumArr` qui additionne les mots de $16$ bits d'un tableau (on suppose que la somme tient sur $16$ bits). Entrées : A0.L pointe sur le tableau, D1.W contient le nombre de mots ($\ge1$). Sortie : D0.L contient la somme. Aucun autre registre ne doit être modifié.", "```asm" "\n"
        "SumArr  MOVEM.L D1/A0,-(A7)    ; sauvegarde des registres modifiés" "\n"
        "        CLR.L   D0             ; somme = 0" "\n"
        "        SUBQ.W  #1,D1          ; DBRA fait n+1 tours : on part de n-1" "\n"
        r"\loop   ADD.W   (A0)+,D0       ; somme += mot, A0 avance de 2" "\n"
        r"        DBRA    D1,\loop" "\n"
        "        MOVEM.L (A7)+,D1/A0    ; restauration" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "D0 est mis à zéro avec `CLR.L` pour que sa partie haute soit nulle. `DBRA` fait D1.W $+1$ tours, d'où le `SUBQ.W #1,D1` initial. D1 et A0 sont modifiés, donc sauvegardés dans la pile. Corrigé vérifié sur un émulateur 68000 avec $30$ tableaux tirés au hasard (somme exacte, D1, A0 et D7 inchangés).", src="TP 4, étapes 4 à 6 (même schéma)", duree=8),
        o("sp146", "Quelle est la différence entre `JSR` et `BSR` ? Que fait `RTS` ? Pourquoi un sous-programme qui modifie D1 sans le sauvegarder est-il dangereux pour l'appelant ? Que se passe-t-il si l'on appelle un sous-programme avec `JMP` au lieu de `JSR` ?", "`JSR` et `BSR` ont le même effet dans le cadre du cours (opérande étiquette) : ils empilent l'adresse de l'instruction qui suit l'appel (sur $32$ bits, A7 $-4$) puis branchent au sous-programme. Elles diffèrent par les modes d'adressage et le codage machine (comme `JMP` et `BRA`)." "\n"
        "" "\n"
        "`RTS` dépile cette adresse dans le PC (A7 $+4$) : c'est un simple saut dont l'adresse est au sommet de la pile. L'exécution reprend juste après l'appel." "\n"
        "" "\n"
        "Si le sous-programme modifie D1 et que l'appelant s'en sert, la valeur de l'appelant est perdue. Convention des examens : sauvegarder avec `MOVEM.L liste,-(A7)` en entrée, restaurer avec `MOVEM.L (A7)+,liste` avant `RTS`, sauf pour les registres de sortie." "\n"
        "" "\n"
        "Avec `JMP`, aucune adresse de retour n'est empilée : le `RTS` dépilerait une valeur quelconque et sauterait n'importe où (erreur du contrôle 2024/2025, ex. 4).", src="Chapitre 1 du cours (D. Bouchet), VII ; Contrôle S3 2024/2025, ex. 4", duree=6),
    ]},
    {"n": 15, "titre": "Chaînes de caractères : parcours, comptage, conversion", "notions": ["chaines"], "exos": [
        v("ch151", "Le sous-programme `StrLen` renvoie dans D0 la longueur d'une chaîne (A0 pointe sur son premier caractère) :" "\n"
        "" "\n"
        "```asm" "\n"
        "StrLen  CLR.L   D0" "\n"
        r"\loop   TST.B   (A0)+" "\n"
        r"        BEQ     \quit" "\n"
        "        ADDQ.L  #1,D0" "\n"
        r"        BRA     \loop" "\n"
        r"\quit   RTS" "\n"
        "```" "\n"
        "" "\n"
        "On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "        ORG     $2000" "\n"
        'TEXT    DC.B    "Cette chaine comporte 36 caracteres.",0' "\n"
        "" "\n"
        "Main    LEA     TEXT,A0" "\n"
        "        JSR     StrLen" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D0 à la fin (en décimal) ?", "len('Cette chaine comporte 36 caracteres.')", "36", "`TST.B (A0)+` teste l'octet pointé et fait avancer A0 ; `BEQ` sort sur l'octet nul sans compter. Chaque autre caractère incrémente D0. La chaîne contient $36$ caractères (sans l'octet nul) : D0 vaut $36$.", src="TP 3, étape 4"),
        v("ch152", "Le sous-programme `SpaceCount` compte les espaces d'une chaîne :" "\n"
        "" "\n"
        "```asm" "\n"
        "SpaceCount" "\n"
        "        CLR.L   D0" "\n"
        r"\loop   MOVE.B  (A0)+,D1" "\n"
        r"        BEQ     \quit" "\n"
        "        CMP.B   #' ',D1" "\n"
        r"        BNE     \loop" "\n"
        "        ADDQ.L  #1,D0" "\n"
        r"        BRA     \loop" "\n"
        r"\quit   RTS" "\n"
        "```" "\n"
        "" "\n"
        "On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "        ORG     $2000" "\n"
        'TEXT    DC.B    "Cette chaine comporte 4 espaces.",0' "\n"
        "" "\n"
        "Main    LEA     TEXT,A0" "\n"
        "        JSR     SpaceCount" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D0 à la fin (en décimal) ?", "'Cette chaine comporte 4 espaces.'.count(' ')", "4", "`MOVE.B (A0)+,D1` met Z à $1$ sur l'octet nul (fin). Chaque caractère égal à `' '` ($32$) incrémente D0. Il y a $4$ espaces.", src="TP 3, étape 5"),
        v("ch153", "Le sous-programme `LowerCount` compte les minuscules (`'a'` à `'z'`) :" "\n"
        "" "\n"
        "```asm" "\n"
        "LowerCount" "\n"
        "        MOVEM.L D1/A0,-(A7)" "\n"
        "        CLR.L   D0" "\n"
        r"\loop   MOVE.B  (A0)+,D1" "\n"
        r"        BEQ     \quit" "\n"
        "        CMP.B   #'a',D1" "\n"
        r"        BLO     \loop" "\n"
        "        CMP.B   #'z',D1" "\n"
        r"        BHI     \loop" "\n"
        "        ADDQ.L  #1,D0" "\n"
        r"        BRA     \loop" "\n"
        r"\quit   MOVEM.L (A7)+,D1/A0" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "        ORG     $2000" "\n"
        'TEXT    DC.B    "Cette chaine comporte 28 minuscules.",0' "\n"
        "" "\n"
        "Main    LEA     TEXT,A0" "\n"
        "        JSR     LowerCount" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D0 à la fin (en décimal) ?", "len([i for i in 'Cette chaine comporte 28 minuscules.' if 'a'<=i<='z'])", "28", "Un caractère est une minuscule si son code ASCII est entre `'a'` ($97$) et `'z'` ($122$) : `BLO` élimine les codes trop petits, `BHI` les trop grands (comparaisons non signées). Il y a $28$ minuscules. Le sous-programme sauvegarde D1 et A0.", src="TP 4, étape 4"),
        v("ch154", "Le sous-programme `GetSum` additionne les chiffres d'une chaîne qui ne contient que des chiffres :" "\n"
        "" "\n"
        "```asm" "\n"
        "GetSum  MOVEM.L A0/D1,-(A7)" "\n"
        "        CLR.L   D0" "\n"
        "        CLR.L   D1" "\n"
        r"\loop   MOVE.B  (A0)+,D1" "\n"
        r"        BEQ     \quit" "\n"
        "        SUB.B   #'0',D1" "\n"
        "        ADD.L   D1,D0" "\n"
        r"        BRA     \loop" "\n"
        r"\quit   MOVEM.L (A7)+,A0/D1" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "        ORG     $2000" "\n"
        'TEXT    DC.B    "704894203",0' "\n"
        "" "\n"
        "Main    LEA     TEXT,A0" "\n"
        "        JSR     GetSum" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D0 à la fin (en décimal) ?", "sum(ord(i)-48 for i in '704894203')", "37", "Pour chaque caractère on soustrait `'0'` ($48$) pour obtenir sa valeur, puis on l'ajoute à D0. Ici $7+0+4+8+9+4+2+0+3=37$.", src="Partiel S3 2020/2021, ex. 4"),
        v("ch155", r"Le sous-programme `Atoui` convertit une chaîne de chiffres en entier : $r\leftarrow10r+\text{chiffre}$." "\n"
        "" "\n"
        "```asm" "\n"
        "Atoui   MOVEM.L D1/A0,-(A7)" "\n"
        "        CLR.L   D0" "\n"
        "        CLR.L   D1" "\n"
        r"\loop   MOVE.B  (A0)+,D1" "\n"
        r"        BEQ     \quit" "\n"
        "        SUBI.B  #'0',D1" "\n"
        "        MULU.W  #10,D0" "\n"
        "        ADD.L   D1,D0" "\n"
        r"        BRA     \loop" "\n"
        r"\quit   MOVEM.L (A7)+,D1/A0" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "        ORG     $2000" "\n"
        'TEXT    DC.B    "12345",0' "\n"
        "" "\n"
        "Main    LEA     TEXT,A0" "\n"
        "        JSR     Atoui" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D0 à la fin (en décimal) ?", "Integer('12345')", "12345", r"On part de D0 $=0$ ; pour chaque chiffre : D0 $\leftarrow D0\times10+\text{chiffre}$. Pour `12345` : $12345$.", src="TP 4, étape 6"),
        v("ch156", "Les sous-programmes `IsBlank` (D0 vaut $0$ si le caractère D1.B est blanc : espace ou tabulation) et `BlankCount` (nombre de caractères blancs d'une chaîne) :" "\n"
        "" "\n"
        "```asm" "\n"
        "IsBlank CMPI.B  #' ',D1" "\n"
        r"        BEQ     \blank" "\n"
        "        CMPI.B  #9,D1" "\n"
        r"        BEQ     \blank" "\n"
        "        MOVEQ.L #1,D0" "\n"
        "        RTS" "\n"
        r"\blank  MOVEQ.L #0,D0" "\n"
        "        RTS" "\n"
        "BlankCount" "\n"
        "        MOVEM.L D1/D2/A0,-(A7)" "\n"
        "        CLR.L   D2" "\n"
        r"\loop   MOVE.B  (A0)+,D1" "\n"
        r"        BEQ     \quit" "\n"
        "        JSR     IsBlank" "\n"
        "        TST.L   D0" "\n"
        r"        BNE     \loop" "\n"
        "        ADDQ.L  #1,D2" "\n"
        r"        BRA     \loop" "\n"
        r"\quit   MOVE.L  D2,D0" "\n"
        "        MOVEM.L (A7)+,D1/D2/A0" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "        ORG     $2000" "\n"
        'TEXT    DC.B    "a b",9,"c  d",0' "\n"
        "" "\n"
        "Main    LEA     TEXT,A0" "\n"
        "        JSR     BlankCount" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D0 à la fin (en décimal) ?", "'a b	c  d'.count(' ')+'a b	c  d'.count(chr(9))", "4", "`IsBlank` renvoie $0$ pour l'espace ($32$) et la tabulation ($9$), $1$ sinon. `BlankCount` compte les caractères pour lesquels `IsBlank` renvoie $0$. La chaîne contient $4$ caractères blancs (la tabulation et les espaces comptent).", src="Partiel S3 2016/2017, ex. 1 ; Partiel S3 2022/2023, ex. 4"),
        v("ch157", "Quel est le code ASCII (en hexadécimal) du caractère `'A'` ?", "ord('A')", "hexa('41')", "`'A'` a pour code $65$, soit" "\n"
        "`$41`.", src="Chapitre 1 du cours (D. Bouchet), III-3"),
        v("ch158", "D1.B contient le code ASCII du caractère `'7'`. Que contient D1.B après `SUB.B #'0',D1` (valeur décimale) ?", "ord('7')-ord('0')", "7", "`'7'` a pour code $55$ et `'0'` pour code $48$ : $55-48=7$. Les chiffres `'0'` à `'9'` ont des codes consécutifs de $48$ à $57$.", src="Partiel S3 2020/2021, ex. 4"),
        o("ch159", "Écrire les sous-programmes suivants (aucun registre de donnée ou d'adresse, hors registres de sortie, ne doit être modifié ; les chaînes ne sont jamais vides) :" "\n"
        "" "\n"
        "1. `IsNumber` : A0 pointe sur une chaîne ; D0.L vaut $0$ si elle ne contient que des chiffres, $1$ sinon." "\n"
        "2. `GetSum` : A0 pointe sur une chaîne de chiffres ; D0.L renvoie la somme de ses chiffres." "\n"
        "3. `CheckSum` : avec `IsNumber` et `GetSum`, renvoie D0 $=0$ et D1 $=$ somme si la chaîne ne contient que des chiffres, sinon D0 $=1$ et D1 $=0$.", "```asm" "\n"
        "IsNumber MOVE.L  A0,-(A7)" "\n"
        r"\loop    MOVE.B  (A0)+,D0       ; caractère courant" "\n"
        r"         BEQ     \number        ; octet nul : que des chiffres" "\n"
        "         CMPI.B  #'0',D0" "\n"
        r"         BLO     \notnum        ; code < '0' (non signé)" "\n"
        "         CMPI.B  #'9',D0" "\n"
        r"         BLS     \loop          ; code <= '9' : c'est un chiffre" "\n"
        r"\notnum  MOVEQ.L #1,D0" "\n"
        r"         BRA     \quit" "\n"
        r"\number  CLR.L   D0" "\n"
        r"\quit    MOVEA.L (A7)+,A0" "\n"
        "         RTS" "\n"
        "" "\n"
        "GetSum   MOVEM.L A0/D1,-(A7)" "\n"
        "         CLR.L   D0" "\n"
        "         CLR.L   D1" "\n"
        r"\loop    MOVE.B  (A0)+,D1" "\n"
        r"         BEQ     \quit" "\n"
        "         SUB.B   #'0',D1" "\n"
        "         ADD.L   D1,D0" "\n"
        r"         BRA     \loop" "\n"
        r"\quit    MOVEM.L (A7)+,A0/D1" "\n"
        "         RTS" "\n"
        "" "\n"
        "CheckSum JSR     IsNumber" "\n"
        "         TST.L   D0" "\n"
        r"         BNE     \notnum" "\n"
        "         JSR     GetSum" "\n"
        "         MOVE.L  D0,D1" "\n"
        "         CLR.L   D0" "\n"
        "         RTS" "\n"
        r"\notnum  CLR.L   D1" "\n"
        "         RTS" "\n"
        "```" "\n"
        "" "\n"
        "`MOVE.B (A0)+,D0` met Z à $1$ sur l'octet nul. Un chiffre est un code entre `'0'` et `'9'` (comparaisons non signées). `CheckSum` n'a pas besoin de sauvegarder D0 et D1 (registres de sortie) ; A0 est restauré par `IsNumber` et `GetSum`. Corrigé officiel du partiel 2020/2021, exécuté sur un émulateur 68000 (chaînes `704894203`, `12a4`, `9`, `0x`).", src="Partiel S3 2020/2021, ex. 4", duree=12),
        o("ch1510", "Écrire le sous-programme `StrCpy` qui copie la chaîne pointée par A0.L (octet nul compris) à l'adresse pointée par A1.L. Aucun registre ne doit être modifié.", "```asm" "\n"
        "StrCpy  MOVEM.L A0/A1/D0,-(A7)" "\n"
        r"\loop   MOVE.B  (A0)+,D0       ; lit un caractère, A0 avance" "\n"
        "        MOVE.B  D0,(A1)+       ; l'écrit, A1 avance ; Z reflète D0" "\n"
        r"        BNE     \loop          ; recommence tant que le caractère copié n'est pas nul" "\n"
        "        MOVEM.L (A7)+,A0/A1/D0" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "L'instruction `MOVE` met à jour N et Z comme `TST` : après `MOVE.B D0,(A1)+`, Z vaut $1$ si le caractère copié est l'octet nul, ce qui permet de ne pas répéter de `TST`. On copie l'octet nul avant de sortir. Même technique que `RemoveSpace` du TP 5. Corrigé rédigé, vérifié sur un émulateur 68000 (chaînes de $1$, $5$ et $7$ caractères ; D0, A0, A1 inchangés).", src="TP 5, étape 1 (RemoveSpace)", duree=8),
    ]},
    {"n": 16, "titre": "Niveau examen : Contrôle S3 2025/2026", "notions": ["memmove", "drapeaux", "registres", "boucle", "rotation", "branch", "pile"], "examen": True, "exos": [
        m("cx1", "Exercice 1. Remplir le tableau : donner le nouveau contenu des registres (sauf le PC) et/ou de la mémoire modifiés par chaque instruction. Valeurs initiales :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $FFFFFFFB   A0 = $00005000" "\n"
        "D1 = $00000008   A1 = $00005008" "\n"
        "D2 = $4444FFFE   A2 = $00005010" "\n"
        "$005000  54 AF 18 B9 E7 21 48 C0" "\n"
        "$005008  C9 10 11 C8 D4 36 1F 88" "\n"
        "$005010  13 79 01 80 42 1A 2D 49" "\n"
        "```" "\n"
        "" "\n"
        "La mémoire et les registres sont réinitialisés avant chaque instruction. Instructions :" "\n"
        "" "\n"
        "```asm" "\n"
        "MOVE.L #$5006,-(A1)" "\n"
        "MOVE.L $5006,2(A0)" "\n"
        "MOVE.W #52,(A0)+" "\n"
        "MOVE.B -7(A1),2(A1,D0.L)" "\n"
        "```", ["x1a", "x1b", "x1c", "x1d", "x1e", "x1f"], "Contrôle S3 2025/2026, ex. 1 (6 points)"),
        m("cx2", "Exercice 2. Donner le résultat (hexadécimal) de chaque addition et le contenu des bits N, Z, V, C du registre d'état (écrire NZVC en binaire) :" "\n"
        "" "\n"
        "```" "\n"
        "$7F + $7F                 8 bits" "\n"
        "$7F + $80                 8 bits" "\n"
        "$007F + $0080            16 bits" "\n"
        "$A0101010 + $A0909090    32 bits" "\n"
        "```", ["x2a", "x2b", "x2c", "x2d", "x2e", "x2f", "x2g"], "Contrôle S3 2025/2026, ex. 2 (4 points)"),
        o("x3", "Exercice 3. Répondre aux questions :" "\n"
        "" "\n"
        "1. Quelle instruction permet d'empiler le registre D0 sur $32$ bits ?" "\n"
        "2. Quelle instruction permet de dépiler les registres A1, A2, A3 et A4 sur $32$ bits ?" "\n"
        "3. Quelle instruction permet d'appeler un sous-programme ?" "\n"
        "4. Quel registre contient l'adresse de la prochaine instruction à exécuter ?", "1. `MOVE.L D0,-(A7)`." "\n"
        "2. `MOVEM.L (A7)+,A1-A4` (liste équivalente : `A1/A2/A3/A4`)." "\n"
        "3. `BSR` (ou `JSR`)." "\n"
        "4. Le compteur programme **PC**." "\n"
        "" "\n"
        "Vérification : `MOVEM.L (A7)+,A1-A4` dépile dans l'ordre normal A1 d'abord, et `BSR`/`JSR` empilent l'adresse de retour avant de brancher (voir le niveau « Pile, A7 et MOVEM »).", src="Contrôle S3 2025/2026, ex. 3 (4 points)", duree=4),
        m("cx4", "Exercice 4. Soit le programme ci-dessous. Donner les valeurs finales de D1, D2, D3 et D4 (hexadécimal sur $32$ bits)." "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVE.L  #$52A59382,D7" "\n"
        "        MOVEQ.L #1,D1" "\n"
        "        CMP.W   #$7000,D7" "\n"
        "        BGT     PART2" "\n"
        "        MOVEQ.L #2,D1" "\n"
        "PART2   CLR.L   D2" "\n"
        "        MOVE.L  #260,D0" "\n"
        "LOOP2   ADDQ.L  #1,D2" "\n"
        "        SUBQ.B  #1,D0" "\n"
        "        BNE     LOOP2" "\n"
        "PART3   CLR.L   D3" "\n"
        "        MOVE.L  #$99999999,D0" "\n"
        "LOOP3   ADDQ.L  #1,D3" "\n"
        "        DBRA    D0,LOOP3" "\n"
        "PART4   MOVE.L  #$12345678,D4" "\n"
        "        ROR.W   #4,D4" "\n"
        "        ROR.L   #8,D4" "\n"
        "        SWAP    D4" "\n"
        "        ROL.B   #4,D4" "\n"
        "        ROR.L   #8,D4" "\n"
        "```", ["x4a", "x4b", "x4c", "x4d"], "Contrôle S3 2025/2026, ex. 4 (6 points)"),
    ]},
    {"n": 17, "titre": "Niveau examen : Partiel S3 2025/2026", "notions": ["memmove", "drapeaux", "boucle", "rotation", "sousprog", "pile", "chaines"], "examen": True, "exos": [
        m("px1", "Exercice 1. Remplir le tableau : nouveau contenu des registres (sauf le PC) et/ou de la mémoire modifiés par chaque instruction. Valeurs initiales :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $FFFFFFFF   A0 = $00005000" "\n"
        "D1 = $0000FFF0   A1 = $00005008" "\n"
        "D2 = $0000000A   A2 = $00005010" "\n"
        "$005000  54 AF 18 B9 E7 21 48 C0" "\n"
        "$005008  C9 10 11 C8 D4 36 1F 88" "\n"
        "$005010  13 79 01 80 42 1A 2D 49" "\n"
        "```" "\n"
        "" "\n"
        "La mémoire et les registres sont réinitialisés avant chaque instruction. Instructions :" "\n"
        "" "\n"
        "```asm" "\n"
        "MOVE.L $5006,-(A2)" "\n"
        "MOVE.W #5001,3(A1,D0.L)" "\n"
        "MOVE.B -8(A2),9(A2,D1.W)" "\n"
        "```", ["y1a", "y1b", "y1c", "y1d"], "Partiel S3 2025/2026, ex. 1 (3 points)"),
        m("px2", "Exercice 2. Donner le résultat (hexadécimal) de chaque addition et le contenu des bits N, Z, V, C (écrire NZVC en binaire) :" "\n"
        "" "\n"
        "```" "\n"
        "$7A + $49                  8 bits" "\n"
        "$7AAA + $9444             16 bits" "\n"
        "$A0A0A0A0 + $A0A0A0A0    32 bits" "\n"
        "```", ["y2a", "y2b", "y2c", "y2d", "y2e", "y2f"], "Partiel S3 2025/2026, ex. 2 (3 points)"),
        m("px3", "Exercice 3. Soit le programme ci-dessous. Donner les valeurs finales de D1, D2 et D3 (hexadécimal sur $32$ bits)." "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVE.L  #127,D7" "\n"
        "        MOVEQ.L #1,D1" "\n"
        "        CMPI.L  #128,D7" "\n"
        "        BLT     NEXT2" "\n"
        "        MOVEQ.L #2,D1" "\n"
        "NEXT2   CLR.L   D2" "\n"
        "        MOVE.B  #20,D0" "\n"
        "LOOP2   ADDQ.L  #1,D2" "\n"
        "        SUBI.B  #1,D0" "\n"
        "        BNE     LOOP2" "\n"
        "NEXT3   ADDI.W  #$10,D7" "\n"
        "        CLR.L   D3" "\n"
        "LOOP3   ADDQ.L  #1,D3" "\n"
        "        DBRA    D7,LOOP3" "\n"
        "```", ["y3a", "y3b", "y3c"], "Partiel S3 2025/2026, ex. 3 (3 points)"),
        o("px4", "Exercice 4. En utilisant uniquement les instructions `SWAP`, `ROR` et `ROL`, donner les instructions qui transforment la valeur initiale de D1 (`$12345678`) en sa valeur finale" "\n"
        "(`$67581234`). Utiliser au maximum trois lignes d'instructions.", "```asm" "\n"
        "        ROL.W #4,D1 ; D1 = $12346785" "\n"
        "        ROL.B #4,D1 ; D1 = $12346758" "\n"
        "        SWAP D1     ; D1 = $67581234" "\n"
        "```" "\n"
        "" "\n"
        "Méthode : on repère où va chaque chiffre. Le résultat `67 58 12 34` est un `SWAP` de `12 34 67 58` ; le mot de poids faible `5678` doit devenir `6758` : rotation de $4$ bits à gauche du mot (`6785`) puis échange des deux derniers chiffres (`6758`). La seconde instruction peut aussi s'écrire `ROR.B #4,D1`." "\n"
        "" "\n"
        "Il existe plusieurs solutions ; celle-ci a été exécutée sur un émulateur 68000 (corrigé rédigé, conforme au corrigé officiel).", src="Partiel S3 2025/2026, ex. 4 (2 points)", duree=8),
        m("px5", "Exercice 5. Toutes les questions sont indépendantes. Réaliser trois sous-programmes qui copient des octets d'un emplacement mémoire vers un autre. **Aucun registre de donnée ou d'adresse ne doit être modifié en sortie.** Entrées de chacun : A1.L pointe sur la source, A2.L sur la destination, D0.L contient le nombre d'octets à copier (entier non signé)." "\n"
        "" "\n"
        "1. `CopyInc` copie en commençant par le premier octet et en incrémentant les adresses. D0 n'est jamais nul, A1 et A2 ne sont jamais égaux. Limité à $9$ lignes d'instructions (RTS compris)." "\n"
        "2. `CopyDec` copie en commençant par le dernier octet et en décrémentant les adresses. Mêmes hypothèses. Limité à $11$ lignes." "\n"
        "3. `Copy` appelle `CopyInc` si la destination est strictement inférieure à la source, `CopyDec` si elle est strictement supérieure. D0 peut être nul et A1 et A2 peuvent être égaux : dans ces deux cas aucun octet n'est copié. Limité à $11$ lignes." "\n"
        "" "\n"
        "Exemple avec A1 `$1000`, A2" "\n"
        "`$2000`, D0" "\n"
        "$=3$ : `CopyInc` copie" "\n"
        "`($1000)` vers" "\n"
        "`($2000)`, puis" "\n"
        "`($1001)`, puis" "\n"
        "`($1002)` ; `CopyDec` copie" "\n"
        "`($1002)` vers" "\n"
        "`($2002)`, puis" "\n"
        "`($1001)`, puis" "\n"
        "`($1000)`.", ["py5a", "py5b", "py5c"], "Partiel S3 2025/2026, ex. 5 (9 points)"),
    ]},
    {"n": 18, "titre": "Niveau examen : anciens sujets (partiels, contrôles, rattrapage)", "notions": ["chaines", "sousprog", "branch", "boucle", "pile"], "examen": True, "exos": [
        m("qq1", "Partiel 2022/2023, exercice 4. Les chaînes se terminent par un octet nul et ne sont jamais vides. À l'exception des registres de sortie, aucun registre ne doit être modifié en sortie des sous-programmes. Réaliser `GetStart`, `GetEnd` et `SuccessiveCount` (voir les trois questions).", ["q1a", "q1b", "q1c"], "Partiel S3 2022/2023, ex. 4 (11 points)"),
        m("qq2", "Partiel 2023/2024, exercice 5. Un tableau de chaînes est constitué de plusieurs chaînes les unes derrière les autres ; il se termine par deux zéros (le zéro de la dernière chaîne suivi d'un zéro supplémentaire). Aucun registre ne doit être modifié en sortie. Réaliser `next_str`, `two_by_two_swap` et `swap_all`.", ["q2a", "q2b", "q2c"], "Partiel S3 2023/2024, ex. 5 (10 points)"),
        m("qq3", "Partiel 2016/2017, exercice 1. Une chaîne se termine par un caractère nul. Un caractère est blanc s'il s'agit d'un espace ou d'une tabulation (code $9$). À l'exception des registres de sortie, aucun registre ne doit être modifié. Réaliser `IsBlank`, `BlankCount` et `BlankToUnderscore`.", ["q3a", "q3b", "q3c"], "Partiel S3 2016/2017, ex. 1 (9 points)"),
        m("qq4", "Contrôle 2020/2021, exercice 5. Soit le programme ci-dessous. Donner les valeurs finales de D1 à D6 (hexadécimal sur $32$ bits)." "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVE.L  #$FF11FF,D7" "\n"
        "        MOVEQ.L #1,D1" "\n"
        "        TST.L   D7" "\n"
        "        BPL     NEXT2" "\n"
        "        MOVEQ.L #2,D1" "\n"
        "NEXT2   MOVEQ.L #1,D2" "\n"
        "        TST.B   D7" "\n"
        "        BMI     NEXT3" "\n"
        "        MOVEQ.L #2,D2" "\n"
        "NEXT3   CLR.L   D3" "\n"
        "        MOVE.L  #$FFFFFFFF,D0" "\n"
        "LOOP3   ADDQ.L  #1,D3" "\n"
        "        SUBQ.W  #1,D0" "\n"
        "        BNE     LOOP3" "\n"
        "NEXT4   CLR.L   D4" "\n"
        "        MOVE.W  #$100,D0" "\n"
        "LOOP4   ADDQ.L  #1,D4" "\n"
        "        DBRA    D0,LOOP4" "\n"
        "NEXT5   MOVEQ.L #1,D5" "\n"
        "        CMP.B   #$42,D7" "\n"
        "        BGT     NEXT6" "\n"
        "        MOVEQ.L #2,D5" "\n"
        "NEXT6   MOVEQ.L #1,D6" "\n"
        "        CMP.B   #$42,D7" "\n"
        "        BLS     QUIT" "\n"
        "        MOVEQ.L #2,D6" "\n"
        "QUIT" "\n"
        "```", ["qd1", "qd2", "qd3", "qd4", "qd5", "qd6"], "Contrôle S3 2020/2021, ex. 5 (6 points)"),
        m("rz1", "Exercice 1. Donner le nouveau contenu des registres (sauf le PC) et/ou de la mémoire modifiés par chaque instruction. Valeurs initiales :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $0001FFFF   A0 = $00005000" "\n"
        "D1 = $10000002   A1 = $00005008" "\n"
        "D2 = $FFFFFFFE   A2 = $00005010" "\n"
        "$005000  54 AF 18 B9 E7 21 48 C0" "\n"
        "$005008  C9 10 11 C8 D4 36 1F 88" "\n"
        "$005010  13 79 01 80 42 1A 2D 49" "\n"
        "```" "\n"
        "" "\n"
        "La mémoire et les registres sont réinitialisés avant chaque instruction." "\n"
        "" "\n"
        "```asm" "\n"
        "MOVE.W #$5000,-(A1)" "\n"
        "MOVE.W $5000,-1(A1,D0.W)" "\n"
        "MOVE.W $5000(PC),-2(A1)" "\n"
        "```", ["z1a", "z1b", "z1c", "z1d"], "Rattrapage S3 2016/2017, ex. 1 (3 points)"),
        m("rz2", "Exercice 2. Donner le résultat (hexadécimal) de chaque addition et les bits N, Z, V, C (écrire NZVC en binaire) :" "\n"
        "" "\n"
        "```" "\n"
        "$E2 + $A8          8 bits" "\n"
        "$8000 + $8000     16 bits" "\n"
        "```", ["z2a", "z2b", "z2c", "z2d"], "Rattrapage S3 2016/2017, ex. 2 (2 points)"),
        m("rz3", "Exercice 3. Soit le programme ci-dessous. Donner les valeurs finales de D1, D2 et D3 (hexadécimal sur $32$ bits)." "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVE.L  #$00BB00BB,D7" "\n"
        "        MOVEQ.L #1,D1" "\n"
        "        TST.B   D7" "\n"
        "        BMI     NEXT2" "\n"
        "        MOVEQ.L #2,D1" "\n"
        "NEXT2   CLR.L   D2" "\n"
        "        MOVE.L  #$FFFFFFFF,D0" "\n"
        "LOOP2   ADDQ.L  #1,D2" "\n"
        "        SUBQ.B  #1,D0" "\n"
        "        BNE     LOOP2" "\n"
        "NEXT3   CLR.L   D3" "\n"
        "        MOVE.W  #$9999,D0" "\n"
        "LOOP3   ADDQ.L  #1,D3" "\n"
        "        DBRA    D0,LOOP3" "\n"
        "```", ["z3a", "z3b", "z3c"], "Rattrapage S3 2016/2017, ex. 3 (3 points)"),
        o("z4", "`IsCharError` : A0.L pointe sur une chaîne non vide. Renvoyer dans D0.L $1$ (vrai) si la chaîne contient au moins un caractère qui n'est pas un chiffre, $0$ (faux) si elle ne contient que des chiffres. Indications : un caractère inférieur à `'0'` ou supérieur à `'9'` n'est pas un chiffre. Aucun registre, hors D0, ne doit être modifié.", "```asm" "\n"
        "IsCharError" "\n"
        "        MOVE.L  A0,-(A7)       ; A0 sera modifié" "\n"
        r"\loop   MOVE.B  (A0)+,D0       ; caractère courant" "\n"
        r"        BEQ     \false         ; octet nul : aucun caractère invalide" "\n"
        "        CMPI.B  #'0',D0" "\n"
        r"        BLO     \true          ; code < '0' : pas un chiffre" "\n"
        "        CMPI.B  #'9',D0" "\n"
        r"        BLS     \loop          ; code <= '9' : c'est un chiffre" "\n"
        r"\true   MOVEQ.L #1,D0          ; erreur" "\n"
        r"        BRA     \quit" "\n"
        r"\false  MOVEQ.L #0,D0          ; que des chiffres" "\n"
        r"\quit   MOVE.L  (A7)+,A0" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "Les comparaisons sont **non signées** (`BLO`, `BLS`) : les codes ASCII sont des octets positifs. Corrigé officiel, vérifié sur un émulateur 68000 (`12345`, `12a45`, `/9`, `0`, `:`).", src="Rattrapage S3 2016/2017, ex. 4 (2 points)", duree=8),
    ]},
    {"n": 19, "titre": "Plus dur que l'examen (+20 %)", "notions": ["boucle", "pile", "sousprog", "chaines", "tailles"], "examen": True, "exos": [
        v("h191", "On exécute le programme suivant :" "\n"
        "" "\n"
        "```asm" "\n"
        "        CLR.L   D1" "\n"
        "        MOVE.W  #2,D2" "\n"
        "OUTER   MOVE.B  #48,D0" "\n"
        "INNER   ADDQ.L  #1,D1" "\n"
        "        SUBQ.B  #3,D0" "\n"
        "        BNE     INNER" "\n"
        "        DBRA    D2,OUTER" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D1 à la fin (en décimal) ?", "(2+1)*(48//3)", "48", r"La boucle interne fait $48/3=16$ tours à chaque passage (D0.B vaut $48$ au départ et `SUBQ.B` a un pas de $3$). La boucle externe est un `DBRA` avec D2.W $=2$ : $2+1=3$ passages. D1 $=(2+1)\times16=48$."),
        v("h192", r"Le sous-programme récursif `Fact` calcule $n!$ pour $n$ dans D0 (avec $n\le8$) :" "\n"
        "" "\n"
        "```asm" "\n"
        "Fact    CMP.L   #1,D0" "\n"
        r"        BLS     \one" "\n"
        "        MOVE.L  D0,-(A7)" "\n"
        "        SUBQ.L  #1,D0" "\n"
        "        JSR     Fact" "\n"
        "        MOVE.L  (A7)+,D1" "\n"
        "        MULU.W  D1,D0" "\n"
        "        RTS" "\n"
        r"\one    MOVEQ.L #1,D0" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "Main    MOVEQ.L #5,D0" "\n"
        "        JSR     Fact" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D0 à la fin (en décimal) ?", "factorial(5)", "120", r"Pour $n>1$, `Fact` empile $n$, calcule $(n-1)!$ par un appel récursif, dépile $n$ dans D1 et multiplie (`MULU.W D1,D0`). Pour $n\le1$ elle renvoie $1$. Résultat : $5!=120$."),
        v("h193", r"A7 vaut `$F00000` au début de `Main`. On modifie `Fact` : le cas de base (`\one`) contient maintenant `ILLEGAL`, qui arrête le programme :" "\n"
        "" "\n"
        "```asm" "\n"
        "Fact    CMP.L   #1,D0" "\n"
        r"        BLS     \one" "\n"
        "        MOVE.L  D0,-(A7)" "\n"
        "        SUBQ.L  #1,D0" "\n"
        "        JSR     Fact" "\n"
        "        MOVE.L  (A7)+,D1" "\n"
        "        MULU.W  D1,D0" "\n"
        "        RTS" "\n"
        r"\one    ILLEGAL" "\n"
        "```" "\n"
        "" "\n"
        "On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "Main    MOVEQ.L #5,D0" "\n"
        "        JSR     Fact" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut A7 quand le processeur atteint `ILLEGAL` ?", "hexa('F00000')-(8*5-4)", "hexa('EFFFDC')", r"Pour $n=5$ le programme fait $5$ appels `JSR Fact` (le premier depuis `Main`, $4$ récursifs) : $5\times4$ octets d'adresses de retour. Chaque appel non terminal empile aussi D0 ($4$ octets) : $4\times4$ octets. Profondeur : $4n+4(n-1)=8n-4=36$ octets. A7 vaut" "\n"
        "`$F00000` moins" "\n"
        "$36$."),
        o("h194", "Écrire le sous-programme `Reverse` qui inverse **en place** la chaîne pointée par A0.L (`Hello` devient `olleH`). La chaîne peut être vide. Aucun registre ne doit être modifié.", "On utilise deux pointeurs : A0 au début, A1 sur le dernier caractère. On échange les octets tant que A0 est avant A1." "\n"
        "" "\n"
        "```asm" "\n"
        "Reverse MOVEM.L D0/D1/A0/A1,-(A7)" "\n"
        "        MOVEA.L A0,A1" "\n"
        r"\find   TST.B   (A1)+          ; avance jusqu'après l'octet nul" "\n"
        r"        BNE     \find" "\n"
        "        SUBQ.L  #2,A1          ; A1 pointe sur le dernier caractère" "\n"
        r"\loop   CMPA.L  A1,A0          ; A0 - A1" "\n"
        r"        BHS     \quit          ; A0 >= A1 : fini (non signé)" "\n"
        "        MOVE.B  (A0),D0        ; échange (A0) et (A1)" "\n"
        "        MOVE.B  (A1),D1" "\n"
        "        MOVE.B  D1,(A0)+" "\n"
        "        MOVE.B  D0,(A1)" "\n"
        "        SUBQ.L  #1,A1" "\n"
        r"        BRA     \loop" "\n"
        r"\quit   MOVEM.L (A7)+,D0/D1/A0/A1" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        r"Pour la chaîne vide, après `\find` A1 vaut A0 $+1$, puis `SUBQ.L #2,A1` donne A0 $-1$ : A0 $\ge$ A1, on sort tout de suite. Corrigé rédigé, vérifié sur un émulateur 68000 (chaînes de $0$, $1$, $2$, $5$, $6$ et $8$ caractères ; D0, D1, A0, A1 inchangés).", duree=14),
        o("h195", "Écrire le sous-programme `Utoa` qui convertit l'entier non signé de $16$ bits contenu dans D0.W (de $0$ à $65535$) en une chaîne de chiffres décimaux terminée par un zéro, écrite à l'adresse A0.L. Aucun registre ne doit être modifié. Indication : on obtient les chiffres du moins significatif au plus significatif avec `DIVU.W #10`.", "Les divisions successives par $10$ donnent les chiffres dans l'ordre inverse de l'écriture : on les **empile**, puis on les dépile pour les écrire dans le bon ordre." "\n"
        "" "\n"
        "```asm" "\n"
        "Utoa    MOVEM.L D0/D1/D2/A0,-(A7)" "\n"
        "        CLR.L   D2             ; nombre de chiffres empilés" "\n"
        r"\div    AND.L   #$FFFF,D0      ; ne garde que le quotient (D0.W)" "\n"
        "        DIVU.W  #10,D0         ; D0.W = quotient, D0(31:16) = reste" "\n"
        "        MOVE.L  D0,D1" "\n"
        "        SWAP    D1             ; D1.W = reste" "\n"
        "        ADD.W   #'0',D1        ; code ASCII du chiffre" "\n"
        "        MOVE.W  D1,-(A7)       ; on l'empile" "\n"
        "        ADDQ.L  #1,D2" "\n"
        "        AND.L   #$FFFF,D0      ; quotient seul, met Z à jour" "\n"
        r"        BNE     \div           ; encore des chiffres ?" "\n"
        r"\pop    MOVE.W  (A7)+,D1       ; dernier chiffre empilé = chiffre de poids fort" "\n"
        "        MOVE.B  D1,(A0)+" "\n"
        "        SUBQ.L  #1,D2" "\n"
        r"        BNE     \pop" "\n"
        "        CLR.B   (A0)           ; zéro de fin de chaîne" "\n"
        "        MOVEM.L (A7)+,D0/D1/D2/A0" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "Le `AND.L #$FFFF,D0` avant `DIVU` est indispensable : sinon le reste du tour précédent (poids fort de D0) ferait partie du dividende. Pour D0" "\n"
        "$=0$, la boucle s'exécute une fois et écrit `0`. Corrigé rédigé, vérifié sur un émulateur 68000 pour $0$, $7$, $10$, $100$, $12345$, $40000$ et $65535$ (registres et pile inchangés).", duree=18),
        v("h196", "Que vaut A0 après `MOVEA.W #$8000,A0` (hexadécimal sur" "\n"
        "$32$ bits) ?", "hexa('8000')+2**32-2**16", "hexa('FFFF8000')", "Une écriture `.W` dans un registre d'adresse est **étendue en signe** sur $32$ bits :" "\n"
        "`$8000` est négatif sur" "\n"
        "$16$ bits ($-32768$), donc A0 vaut" "\n"
        "`$FFFF8000`. Sur le bus, seuls les" "\n"
        "$24$ bits de poids faible sortent : l'adresse accédée est" "\n"
        "`$FF8000`."),
        o("h197", "Dans `Fact`, pourquoi ne peut-on pas remplacer `MOVE.L (A7)+,D1` puis `MULU.W D1,D0` par la seule instruction `MULU.W (A7)+,D0` ? Que se passe-t-il ?", "On a empilé un **mot long** (`MOVE.L D0,-(A7)`, $4$ octets, big-endian : mot de poids fort à l'adresse la plus basse). `MULU.W (A7)+,D0` lit un **mot** (`.W`) : celui qui est au sommet de la pile, c'est-à-dire le mot de **poids fort** de $n$, nul tant que $n<65536$. Deux erreurs se cumulent :" "\n"
        "" "\n"
        "1. la multiplication se fait par $0$ au lieu de $n$ : le résultat est faux ;" "\n"
        "2. `(A7)+` n'incrémente A7 que de $2$ (taille `.W`) : la pile n'est pas rééquilibrée de $4$ octets et le `RTS` suivant dépile une adresse de retour décalée (erreur d'adresse ou saut dans un mauvais endroit)." "\n"
        "" "\n"
        "Il faut dépiler avec la même taille que l'empilement : `MOVE.L (A7)+,D1`, puis multiplier D0.W par D1.W. Le comportement fautif a été constaté sur l'émulateur 68000 : le `RTS` dépile une mauvaise adresse de retour et l'exécution part dans un endroit invalide (plantage constaté sur l'émulateur).", duree=7),
    ]},
]

EXTRA_PARTS = [
    o("q2a", "`next_str` : A0.L pointe sur une chaîne d'un tableau de chaînes (chaînes les unes derrière les autres, le tableau se termine par deux zéros consécutifs). Renvoyer dans A0.L l'adresse de la chaîne suivante, ou celle du dernier zéro s'il n'y en a plus (limité à $3$ lignes).", "```asm" "\n"
        "next_str" "\n"
        "        TST.B   (A0)+         ; teste l'octet, A0 avance" "\n"
        "        BNE     next_str      ; tant que ce n'est pas le zéro de fin de chaîne" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "Le zéro de la chaîne courante est consommé ; A0 pointe sur le premier caractère de la chaîne suivante, ou sur le zéro supplémentaire qui termine le tableau. Corrigé officiel (la correction écrit `test.b` par erreur : l'instruction est `tst.b`).", src="Partiel S3 2023/2024, ex. 5.1", duree=4),
    o("q2b", "`two_by_two_swap` : A0.L pointe sur une chaîne ; inverser les caractères deux par deux, en place (si la longueur est impaire, le dernier caractère ne change pas). `ABCDEF` devient `BADCFE`, `ABCDEFG` devient `BADCFEG` (limité à $13$ lignes).", "```asm" "\n"
        "two_by_two_swap" "\n"
        "        MOVEM.L D0/D1/A0,-(A7)" "\n"
        r"\loop   MOVE.B  (A0),D0        ; premier caractère de la paire" "\n"
        r"        BEQ     \quit          ; fin de chaîne" "\n"
        "        MOVE.B  1(A0),D1       ; second caractère" "\n"
        r"        BEQ     \quit          ; longueur impaire : le dernier ne bouge pas" "\n"
        "        MOVE.B  D1,(A0)+       ; écrit le second à la place du premier" "\n"
        "        MOVE.B  D0,(A0)+       ; écrit le premier à la place du second" "\n"
        r"        BRA     \loop" "\n"
        r"\quit   MOVEM.L (A7)+,D0/D1/A0" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "`MOVE.B (A0),D0` met Z à jour : zéro signifie fin de chaîne. On lit la paire avant de l'écrire. Corrigé officiel, vérifié sur un émulateur 68000.", src="Partiel S3 2023/2024, ex. 5.2", duree=8),
    o("q2c", "`swap_all` : A0.L pointe sur la première chaîne d'un tableau de chaînes ; appliquer `two_by_two_swap` à chacune, avec `next_str` et `two_by_two_swap` (limité à $10$ lignes).", "```asm" "\n"
        "swap_all" "\n"
        "        MOVE.L  A0,-(A7)       ; A0 sera modifié par next_str" "\n"
        r"\loop   JSR     two_by_two_swap" "\n"
        "        JSR     next_str       ; A0 -> chaîne suivante" "\n"
        "        TST.B   (A0)          ; le tableau se termine par un zéro supplémentaire" "\n"
        r"        BNE     \loop" "\n"
        "        MOVE.L  (A7)+,A0" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "Un octet nul à l'adresse pointée signifie qu'il n'y a plus de chaîne. Corrigé officiel, vérifié sur un émulateur 68000 pour deux tableaux de chaînes (D5 et A0 inchangés).", src="Partiel S3 2023/2024, ex. 5.3", duree=7),
    v("x4a", "Dans le programme de l'exercice 4, que vaut D1 à la fin ?", "1 if (lambda x: x-2**16*(x//2**15))((hexa('9382'))%2**16)>28672 else 2", "hexa('00000002')", "`CMP.W #$7000,D7` compare D7.W" "\n"
        "(`$9382`, négatif en signé) à" "\n"
        "`$7000`. `BGT` est signé :" "\n"
        "$-27774>28672$ est faux, pas de saut, `MOVEQ.L #2,D1` est exécuté : D1 vaut" "\n"
        "`$00000002`.", src="Contrôle S3 2025/2026, ex. 4"),
    v("x4b", "Dans le programme de l'exercice 4, que vaut D2 à la fin ?", "(260%256 or 256)", "hexa('00000004')", "Seul l'octet de poids faible de D0 est décrémenté : `260` $=$" "\n"
        "`$104`, donc D0.B vaut" "\n"
        "$4$ au départ : la boucle fait $4$ tours. D2 vaut" "\n"
        "`$00000004`.", src="Contrôle S3 2025/2026, ex. 4"),
    v("x4c", "Dans le programme de l'exercice 4, que vaut D3 à la fin ?", "hexa('99999999')%65536+1", "hexa('0000999A')", "`DBRA D0,LOOP3` ne regarde que D0.W (`$9999`) : il fait D0.W" "\n"
        "$+1$ tours, soit" "\n"
        "`$999A`. D3 vaut" "\n"
        "`$0000999A`.", src="Contrôle S3 2025/2026, ex. 4"),
    v("x4d", "Dans le programme de l'exercice 4, que vaut D4 à la fin ?", "(lambda x: (x-x%4294967296)+((((x%4294967296)>>8)|((x%4294967296)<<24))%4294967296))((lambda x: (x-x%256)+((((x%256)>>4)|((x%256)<<4))%256))((lambda x: (x%65536)*65536+x//65536)((lambda x: (x-x%4294967296)+((((x%4294967296)>>8)|((x%4294967296)<<24))%4294967296))((lambda x: (x-x%65536)+((((x%65536)>>4)|((x%65536)<<12))%65536))(hexa('12345678'))))))", "hexa('21348567')", "On suit les chiffres hexadécimaux : `12345678` ; `ROR.W #4` : `12348567` ; `ROR.L #8` : `67123485` ; `SWAP` : `34856712` ; `ROL.B #4` : `34856721` ; `ROR.L #8` : `21348567`. D4 vaut `$21348567`.", src="Contrôle S3 2025/2026, ex. 4"),
    o("py5a", r"`CopyInc` : copie de A1 vers A2 en incrémentant (D0 $\ne0$, A1 $\ne$ A2, $9$ lignes maximum).", "```asm" "\n"
        "CopyInc MOVEM.L D0/A1/A2,-(A7)   ; sauvegarde des registres modifiés" "\n"
        r"\loop   MOVE.B  (A1)+,(A2)+      ; copie un octet, les deux pointeurs avancent" "\n"
        "        SUBQ.L  #1,D0            ; un octet de moins" "\n"
        r"        BNE     \loop            ; recommence tant que D0 n'est pas nul" "\n"
        "        MOVEM.L (A7)+,D0/A1/A2   ; restauration" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "Total : $6$ lignes d'instructions (limite : $9$). D0, A1 et A2 sont modifiés par la boucle : ils sont sauvegardés. Corrigé officiel, vérifié sur un émulateur 68000 sur des copies aléatoires (D0, A1, A2 et un registre témoin inchangés).", src="Partiel S3 2025/2026, ex. 5.1", duree=8),
    o("py5b", r"`CopyDec` : copie de A1 vers A2 en commençant par le dernier octet, en décrémentant (D0 $\ne0$, A1 $\ne$ A2, $11$ lignes maximum).", "```asm" "\n"
        "CopyDec MOVE.L  D0,-(A7)         ; seul D0 est modifié (A1, A2 sont rétablis par le calcul inverse)" "\n"
        "        ADDA.L  D0,A1            ; A1 pointe après le dernier octet source" "\n"
        "        ADDA.L  D0,A2            ; A2 pointe après le dernier octet destination" "\n"
        r"\loop   MOVE.B  -(A1),-(A2)      ; prédécrémente puis copie" "\n"
        "        SUBQ.L  #1,D0" "\n"
        r"        BNE     \loop" "\n"
        "        MOVE.L  (A7)+,D0" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "Total : $8$ lignes (limite : $11$). Après la boucle, A1 et A2 sont revenus à leur valeur initiale : on a ajouté D0 puis retiré D0 fois $1$ ($D_0$ prédécrémentations). Corrigé officiel, vérifié sur un émulateur 68000.", src="Partiel S3 2025/2026, ex. 5.2", duree=10),
    o("py5c", "`Copy` : appelle `CopyInc` si A2 est strictement inférieur à A1, `CopyDec` si A2 est strictement supérieur à A1 ; ne copie rien si D0 est nul ou si A1 $=$ A2 ($11$ lignes maximum).", "```asm" "\n"
        "Copy    TST.L   D0               ; rien à copier ?" "\n"
        r"        BEQ     \quit" "\n"
        "        CMPA.L  A1,A2            ; A2 - A1" "\n"
        r"        BEQ     \quit            ; mêmes adresses : rien à copier" "\n"
        r"        BLO     \inc             ; A2 < A1 (non signé) : copie en incrémentant" "\n"
        r"\dec    JSR     CopyDec          ; A2 > A1 : copie en décrémentant" "\n"
        "        RTS" "\n"
        r"\inc    JSR     CopyInc" "\n"
        r"\quit   RTS" "\n"
        "```" "\n"
        "" "\n"
        "Pourquoi deux sens ? Si les zones se chevauchent, copier dans le mauvais sens écraserait des octets source avant de les lire : quand la destination est avant la source on copie du début à la fin, quand elle est après on copie de la fin au début. Total : $9$ lignes (limite : $11$). Les adresses se comparent en **non signé** (`BLO`). Corrigé officiel, vérifié sur un émulateur 68000 avec des zones qui se chevauchent.", src="Partiel S3 2025/2026, ex. 5.3", duree=10),
    v("z1a", "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $0001FFFF   A0 = $00005000" "\n"
        "D1 = $10000002   A1 = $00005008" "\n"
        "D2 = $FFFFFFFE   A2 = $00005010" "\n"
        "$005000  54 AF 18 B9 E7 21 48 C0" "\n"
        "$005008  C9 10 11 C8 D4 36 1F 88" "\n"
        "$005010  13 79 01 80 42 1A 2D 49" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVE.W #$5000,-(A1)`. Donner les" "\n"
        "$8$ octets de la mémoire à partir de" "\n"
        "`$5000` après l'instruction, écrits comme un seul nombre hexadécimal de" "\n"
        "$16$ chiffres.", "hexa('54AF18B9E721'+'5000'+'')", "hexa('54AF18B9E7215000')", "Avant : `54AF18B9E72148C0`. L'instruction écrit `5000` à partir de l'octet n° 6 de la fenêtre (adresse `$5006`) ; les autres octets ne changent pas. Après : `54AF18B9E7215000`.", src="Rattrapage S3 2016/2017, ex. 1"),
    v("z1b", "Mêmes valeurs initiales (A1 `$5008`). Quelle est la valeur de A1 après" "\n"
        "`MOVE.W #$5000,-(A1)` ?", "hexa('5008')-2", "hexa('5006')", "`-(A1)` retire $2$ (taille `.W`) : A1 vaut" "\n"
        "`$5006`.", src="Rattrapage S3 2016/2017, ex. 1"),
    v("z1c", "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $0001FFFF   A0 = $00005000" "\n"
        "D1 = $10000002   A1 = $00005008" "\n"
        "D2 = $FFFFFFFE   A2 = $00005010" "\n"
        "$005000  54 AF 18 B9 E7 21 48 C0" "\n"
        "$005008  C9 10 11 C8 D4 36 1F 88" "\n"
        "$005010  13 79 01 80 42 1A 2D 49" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVE.W $5000,-1(A1,D0.W)`. Donner les" "\n"
        "$8$ octets de la mémoire à partir de" "\n"
        "`$5000` après l'instruction, écrits comme un seul nombre hexadécimal de" "\n"
        "$16$ chiffres.", "hexa('54AF18B9E721'+'54AF'+'')", "hexa('54AF18B9E72154AF')", "Avant : `54AF18B9E72148C0`. L'instruction écrit `54AF` à partir de l'octet n° 6 de la fenêtre (adresse `$5006`) ; les autres octets ne changent pas. Après : `54AF18B9E72154AF`.", src="Rattrapage S3 2016/2017, ex. 1"),
    v("z1d", "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $0001FFFF   A0 = $00005000" "\n"
        "D1 = $10000002   A1 = $00005008" "\n"
        "D2 = $FFFFFFFE   A2 = $00005010" "\n"
        "$005000  54 AF 18 B9 E7 21 48 C0" "\n"
        "$005008  C9 10 11 C8 D4 36 1F 88" "\n"
        "$005010  13 79 01 80 42 1A 2D 49" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVE.W $5000(PC),-2(A1)`. Donner les" "\n"
        "$8$ octets de la mémoire à partir de" "\n"
        "`$5000` après l'instruction, écrits comme un seul nombre hexadécimal de" "\n"
        "$16$ chiffres.", "hexa('54AF18B9E721'+'54AF'+'')", "hexa('54AF18B9E72154AF')", "Avant : `54AF18B9E72148C0`. L'instruction écrit `54AF` à partir de l'octet n° 6 de la fenêtre (adresse `$5006`) ; les autres octets ne changent pas. Après : `54AF18B9E72154AF`.", src="Rattrapage S3 2016/2017, ex. 1"),
    v("y2a", "On additionne sur 8 bits : `$7A + $49` (par exemple avec `ADD.B`). Donner le résultat (en hexadécimal, sur 8 bits).", "(hexa('7A')+hexa('49'))%2**8", "hexa('C3')", "`$7A + $49 = $C3` ; sur 8 bits on garde" "\n"
        "`$C3`.", src="Partiel S3 2025/2026, ex. 2"),
    v("y2b", "On additionne sur 8 bits : `$7A + $49` (par exemple avec `ADD.B`). Donner les drapeaux N, Z, V, C (écrire NZVC en binaire, par exemple `%1010`).", "8*(((hexa('7A')+hexa('49'))%2**8)//2**7)+4*(1-Min(1,(hexa('7A')+hexa('49'))%2**8))+2*(abs(((hexa('7A')-2**8*(hexa('7A')//2**7))+(hexa('49')-2**8*(hexa('49')//2**7))+2**7)//2**8))+(hexa('7A')+hexa('49'))//2**8", "bits('1010')", "`$7A + $49 = $C3` ; sur 8 bits on garde" "\n"
        "`$C3`." "\n"
        "N$=1$, Z$=0$, V$=1$ (dépassement signé), C$=0$. On lit NZVC `1010`.", src="Partiel S3 2025/2026, ex. 2"),
    v("y2c", "On additionne sur 16 bits : `$7AAA + $9444` (par exemple avec `ADD.W`). Donner le résultat (en hexadécimal, sur 16 bits).", "(hexa('7AAA')+hexa('9444'))%2**16", "hexa('0EEE')", "`$7AAA + $9444 = $10EEE` ; sur 16 bits on garde" "\n"
        "`$0EEE`.", src="Partiel S3 2025/2026, ex. 2"),
    v("y2d", "On additionne sur 16 bits : `$7AAA + $9444` (par exemple avec `ADD.W`). Donner les drapeaux N, Z, V, C (écrire NZVC en binaire, par exemple `%1010`).", "8*(((hexa('7AAA')+hexa('9444'))%2**16)//2**15)+4*(1-Min(1,(hexa('7AAA')+hexa('9444'))%2**16))+2*(abs(((hexa('7AAA')-2**16*(hexa('7AAA')//2**15))+(hexa('9444')-2**16*(hexa('9444')//2**15))+2**15)//2**16))+(hexa('7AAA')+hexa('9444'))//2**16", "bits('0001')", "`$7AAA + $9444 = $10EEE` ; sur 16 bits on garde" "\n"
        "`$0EEE`." "\n"
        "N$=0$, Z$=0$, V$=0$ (pas de dépassement signé), C$=1$. On lit NZVC `0001`.", src="Partiel S3 2025/2026, ex. 2"),
    v("y2e", "On additionne sur 32 bits : `$A0A0A0A0 + $A0A0A0A0` (par exemple avec `ADD.L`). Donner le résultat (en hexadécimal, sur 32 bits).", "(hexa('A0A0A0A0')+hexa('A0A0A0A0'))%2**32", "hexa('41414140')", "`$A0A0A0A0 + $A0A0A0A0 = $141414140` ; sur 32 bits on garde" "\n"
        "`$41414140`.", src="Partiel S3 2025/2026, ex. 2"),
    v("y2f", "On additionne sur 32 bits : `$A0A0A0A0 + $A0A0A0A0` (par exemple avec `ADD.L`). Donner les drapeaux N, Z, V, C (écrire NZVC en binaire, par exemple `%1010`).", "8*(((hexa('A0A0A0A0')+hexa('A0A0A0A0'))%2**32)//2**31)+4*(1-Min(1,(hexa('A0A0A0A0')+hexa('A0A0A0A0'))%2**32))+2*(abs(((hexa('A0A0A0A0')-2**32*(hexa('A0A0A0A0')//2**31))+(hexa('A0A0A0A0')-2**32*(hexa('A0A0A0A0')//2**31))+2**31)//2**32))+(hexa('A0A0A0A0')+hexa('A0A0A0A0'))//2**32", "bits('0011')", "`$A0A0A0A0 + $A0A0A0A0 = $141414140` ; sur 32 bits on garde" "\n"
        "`$41414140`." "\n"
        "N$=0$, Z$=0$, V$=1$ (dépassement signé), C$=1$. On lit NZVC `0011`.", src="Partiel S3 2025/2026, ex. 2"),
    v("z3a", "Dans le programme de l'exercice 3, que vaut D1 à la fin ?", "1 if (lambda x: x-2**8*(x//2**7))((hexa('BB'))%2**8)<0 else 2", "hexa('00000001')", "`TST.B D7` : D7.B vaut `$BB`, négatif en signé," "\n"
        "N$=1$ : `BMI` saute à `NEXT2`, D1 reste à $1$.", src="Rattrapage S3 2016/2017, ex. 3"),
    v("z3b", "Dans le programme de l'exercice 3, que vaut D2 à la fin ?", "hexa('FFFFFFFF')%256 or 256", "hexa('000000FF')", "`SUBQ.B #1,D0` ne touche que D0.B (`$FF`" "\n"
        "$=255$) : $255$ tours, D2 vaut" "\n"
        "`$000000FF`.", src="Rattrapage S3 2016/2017, ex. 3"),
    v("z3c", "Dans le programme de l'exercice 3, que vaut D3 à la fin ?", "hexa('9999')+1", "hexa('0000999A')", "`DBRA D0,LOOP3` avec D0.W `$9999` : D0.W" "\n"
        "$+1$ tours, soit" "\n"
        "`$999A`. D3 vaut" "\n"
        "`$0000999A`.", src="Rattrapage S3 2016/2017, ex. 3"),
    v("y3a", "Dans le programme de l'exercice 3, que vaut D1 à la fin ?", "1 if 127<128 else 2", "hexa('00000001')", "`CMPI.L #128,D7` compare D7 ($127$) à $128$ sur $32$ bits : $127<128$, `BLT` saute à `NEXT2` et `MOVEQ.L #2,D1` n'est pas exécuté. D1 vaut" "\n"
        "`$00000001`.", src="Partiel S3 2025/2026, ex. 3"),
    v("y3b", "Dans le programme de l'exercice 3, que vaut D2 à la fin ?", "20", "hexa('00000014')", "`MOVE.B #20,D0` puis `SUBI.B #1,D0` / `BNE` : $20$ tours. D2 vaut" "\n"
        "`$00000014`.", src="Partiel S3 2025/2026, ex. 3"),
    v("y3c", "Dans le programme de l'exercice 3, que vaut D3 à la fin ?", "(127+16)%65536+1", "hexa('00000090')", "`ADDI.W #$10,D7` : D7 vaut" "\n"
        "$127+16=143$" "\n"
        "(`$8F`). `DBRA D7,LOOP3` ne regarde que D7.W : il fait D7.W" "\n"
        "$+1=144$ tours, soit" "\n"
        "`$90`. D3 vaut" "\n"
        "`$00000090`.", src="Partiel S3 2025/2026, ex. 3"),
    v("x2a", "On additionne sur 8 bits : `$7F + $7F` (par exemple avec `ADD.B`). Donner le résultat (en hexadécimal, sur 8 bits).", "(hexa('7F')+hexa('7F'))%2**8", "hexa('FE')", "`$7F + $7F = $FE` ; sur 8 bits on garde" "\n"
        "`$FE`.", src="Contrôle S3 2025/2026, ex. 2"),
    v("x2b", "On additionne sur 8 bits : `$7F + $7F` (par exemple avec `ADD.B`). Donner les drapeaux N, Z, V, C (écrire NZVC en binaire, par exemple `%1010`).", "8*(((hexa('7F')+hexa('7F'))%2**8)//2**7)+4*(1-Min(1,(hexa('7F')+hexa('7F'))%2**8))+2*(abs(((hexa('7F')-2**8*(hexa('7F')//2**7))+(hexa('7F')-2**8*(hexa('7F')//2**7))+2**7)//2**8))+(hexa('7F')+hexa('7F'))//2**8", "bits('1010')", "`$7F + $7F = $FE` ; sur 8 bits on garde" "\n"
        "`$FE`." "\n"
        "N$=1$, Z$=0$, V$=1$ (dépassement signé), C$=0$. On lit NZVC `1010`.", src="Contrôle S3 2025/2026, ex. 2"),
    v("x2c", "On additionne sur 8 bits : `$7F + $80` (par exemple avec `ADD.B`). Donner le résultat (en hexadécimal, sur 8 bits).", "(hexa('7F')+hexa('80'))%2**8", "hexa('FF')", "`$7F + $80 = $FF` ; sur 8 bits on garde" "\n"
        "`$FF`.", src="Contrôle S3 2025/2026, ex. 2"),
    v("x2d", "On additionne sur 8 bits : `$7F + $80` (par exemple avec `ADD.B`). Donner les drapeaux N, Z, V, C (écrire NZVC en binaire, par exemple `%1010`).", "8*(((hexa('7F')+hexa('80'))%2**8)//2**7)+4*(1-Min(1,(hexa('7F')+hexa('80'))%2**8))+2*(abs(((hexa('7F')-2**8*(hexa('7F')//2**7))+(hexa('80')-2**8*(hexa('80')//2**7))+2**7)//2**8))+(hexa('7F')+hexa('80'))//2**8", "bits('1000')", "`$7F + $80 = $FF` ; sur 8 bits on garde" "\n"
        "`$FF`." "\n"
        "N$=1$, Z$=0$, V$=0$ (pas de dépassement signé), C$=0$. On lit NZVC `1000`.", src="Contrôle S3 2025/2026, ex. 2"),
    v("x2e", "On additionne sur 16 bits : `$007F + $0080` (par exemple avec `ADD.W`). Donner les drapeaux N, Z, V, C (écrire NZVC en binaire, par exemple `%1010`).", "8*(((hexa('007F')+hexa('0080'))%2**16)//2**15)+4*(1-Min(1,(hexa('007F')+hexa('0080'))%2**16))+2*(abs(((hexa('007F')-2**16*(hexa('007F')//2**15))+(hexa('0080')-2**16*(hexa('0080')//2**15))+2**15)//2**16))+(hexa('007F')+hexa('0080'))//2**16", "bits('0000')", "`$007F + $0080 = $FF` ; sur 16 bits on garde" "\n"
        "`$00FF`." "\n"
        "N$=0$, Z$=0$, V$=0$ (pas de dépassement signé), C$=0$. On lit NZVC `0000`.", src="Contrôle S3 2025/2026, ex. 2"),
    v("x2f", "On additionne sur 32 bits : `$A0101010 + $A0909090` (par exemple avec `ADD.L`). Donner le résultat (en hexadécimal, sur 32 bits).", "(hexa('A0101010')+hexa('A0909090'))%2**32", "hexa('40A0A0A0')", "`$A0101010 + $A0909090 = $140A0A0A0` ; sur 32 bits on garde" "\n"
        "`$40A0A0A0`.", src="Contrôle S3 2025/2026, ex. 2"),
    v("x2g", "On additionne sur 32 bits : `$A0101010 + $A0909090` (par exemple avec `ADD.L`). Donner les drapeaux N, Z, V, C (écrire NZVC en binaire, par exemple `%1010`).", "8*(((hexa('A0101010')+hexa('A0909090'))%2**32)//2**31)+4*(1-Min(1,(hexa('A0101010')+hexa('A0909090'))%2**32))+2*(abs(((hexa('A0101010')-2**32*(hexa('A0101010')//2**31))+(hexa('A0909090')-2**32*(hexa('A0909090')//2**31))+2**31)//2**32))+(hexa('A0101010')+hexa('A0909090'))//2**32", "bits('0011')", "`$A0101010 + $A0909090 = $140A0A0A0` ; sur 32 bits on garde" "\n"
        "`$40A0A0A0`." "\n"
        "N$=0$, Z$=0$, V$=1$ (dépassement signé), C$=1$. On lit NZVC `0011`.", src="Contrôle S3 2025/2026, ex. 2"),
    v("x1a", "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $FFFFFFFB   A0 = $00005000" "\n"
        "D1 = $00000008   A1 = $00005008" "\n"
        "D2 = $4444FFFE   A2 = $00005010" "\n"
        "$005000  54 AF 18 B9 E7 21 48 C0" "\n"
        "$005008  C9 10 11 C8 D4 36 1F 88" "\n"
        "$005010  13 79 01 80 42 1A 2D 49" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVE.L #$5006,-(A1)`. Donner les" "\n"
        "$8$ octets de la mémoire à partir de" "\n"
        "`$5000` après l'instruction, écrits comme un seul nombre hexadécimal de" "\n"
        "$16$ chiffres.", "hexa('54AF18B9'+'00005006'+'')", "hexa('54AF18B900005006')", "Avant : `54AF18B9E72148C0`. L'instruction écrit `00005006` à partir de l'octet n° 4 de la fenêtre (adresse `$5004`) ; les autres octets ne changent pas. Après : `54AF18B900005006`.", src="Contrôle S3 2025/2026, ex. 1"),
    v("x1b", "Mêmes valeurs initiales (A1 `$5008`). Quelle est la valeur de A1 après" "\n"
        "`MOVE.L #$5006,-(A1)` ?", "hexa('5008')-4", "hexa('5004')", "`-(A1)` retire $4$ (taille `.L`) à A1 :" "\n"
        "`$5004`. La donnée immédiate est écrite à cette adresse.", src="Contrôle S3 2025/2026, ex. 1"),
    v("x1c", "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $FFFFFFFB   A0 = $00005000" "\n"
        "D1 = $00000008   A1 = $00005008" "\n"
        "D2 = $4444FFFE   A2 = $00005010" "\n"
        "$005000  54 AF 18 B9 E7 21 48 C0" "\n"
        "$005008  C9 10 11 C8 D4 36 1F 88" "\n"
        "$005010  13 79 01 80 42 1A 2D 49" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVE.L $5006,2(A0)`. Donner les" "\n"
        "$8$ octets de la mémoire à partir de" "\n"
        "`$5000` après l'instruction, écrits comme un seul nombre hexadécimal de" "\n"
        "$16$ chiffres.", "hexa('54AF'+'48C0C910'+'48C0')", "hexa('54AF48C0C91048C0')", "Avant : `54AF18B9E72148C0`. L'instruction écrit `48C0C910` à partir de l'octet n° 2 de la fenêtre (adresse `$5002`) ; les autres octets ne changent pas. Après : `54AF48C0C91048C0`.", src="Contrôle S3 2025/2026, ex. 1"),
    v("x1d", "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $FFFFFFFB   A0 = $00005000" "\n"
        "D1 = $00000008   A1 = $00005008" "\n"
        "D2 = $4444FFFE   A2 = $00005010" "\n"
        "$005000  54 AF 18 B9 E7 21 48 C0" "\n"
        "$005008  C9 10 11 C8 D4 36 1F 88" "\n"
        "$005010  13 79 01 80 42 1A 2D 49" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVE.W #52,(A0)+`. Donner les $8$ octets de la mémoire à partir de" "\n"
        "`$5000` après l'instruction, écrits comme un seul nombre hexadécimal de" "\n"
        "$16$ chiffres.", "hexa(''+'0034'+'18B9E72148C0')", "hexa('003418B9E72148C0')", "Avant : `54AF18B9E72148C0`. L'instruction écrit `0034` à partir de l'octet n° 0 de la fenêtre (adresse `$5000`) ; les autres octets ne changent pas. Après : `003418B9E72148C0`.", src="Contrôle S3 2025/2026, ex. 1"),
    v("x1e", "Mêmes valeurs initiales (A0 `$5000`). Quelle est la valeur de A0 après `MOVE.W #52,(A0)+` ?", "hexa('5000')+2", "hexa('5002')", "`(A0)+` ajoute la taille de l'instruction (`.W` : $2$) à A0 :" "\n"
        "`$5002`.", src="Contrôle S3 2025/2026, ex. 1"),
    v("x1f", "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $FFFFFFFB   A0 = $00005000" "\n"
        "D1 = $00000008   A1 = $00005008" "\n"
        "D2 = $4444FFFE   A2 = $00005010" "\n"
        "$005000  54 AF 18 B9 E7 21 48 C0" "\n"
        "$005008  C9 10 11 C8 D4 36 1F 88" "\n"
        "$005010  13 79 01 80 42 1A 2D 49" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVE.B -7(A1),2(A1,D0.L)`. Donner les $8$ octets de la mémoire à partir de" "\n"
        "`$5000` après l'instruction, écrits comme un seul nombre hexadécimal de" "\n"
        "$16$ chiffres.", "hexa('54AF18B9E7'+'AF'+'48C0')", "hexa('54AF18B9E7AF48C0')", "Avant : `54AF18B9E72148C0`. L'instruction écrit `AF` à partir de l'octet n° 5 de la fenêtre (adresse `$5005`) ; les autres octets ne changent pas. Après : `54AF18B9E7AF48C0`.", src="Contrôle S3 2025/2026, ex. 1"),
    v("qd1", "Dans le programme de l'exercice, que vaut D1 à la fin ?", "1 if (lambda x: x-2**32*(x//2**31))((hexa('00FF11FF'))%2**32)>=0 else 2", "hexa('00000001')", "`TST.L D7` : D7 `$00FF11FF` est positif," "\n"
        "N$=0$, `BPL` saute à `NEXT2` : D1 reste à $1$.", src="Contrôle S3 2020/2021, ex. 5"),
    v("qd2", "Dans le programme de l'exercice, que vaut D2 à la fin ?", "1 if (lambda x: x-2**8*(x//2**7))((hexa('FF'))%2**8)<0 else 2", "hexa('00000001')", "`TST.B D7` ne regarde que D7.B (`$FF`, négatif) :" "\n"
        "N$=1$, `BMI` saute à `NEXT3` : D2 vaut $1$.", src="Contrôle S3 2020/2021, ex. 5"),
    v("qd3", "Dans le programme de l'exercice, que vaut D3 à la fin ?", "hexa('FFFFFFFF')%65536", "hexa('0000FFFF')", "`SUBQ.W #1,D0` agit sur D0.W (`$FFFF`) : la boucle s'arrête quand D0.W vaut" "\n"
        "$0$, soit après" "\n"
        "`$FFFF`" "\n"
        "($65535$) tours. D3 vaut" "\n"
        "`$0000FFFF`.", src="Contrôle S3 2020/2021, ex. 5"),
    v("qd4", "Dans le programme de l'exercice, que vaut D4 à la fin ?", "hexa('100')+1", "hexa('00000101')", "`DBRA D0,LOOP4` avec D0.W `$100` : D0.W" "\n"
        "$+1$ tours, soit" "\n"
        "`$101`. D4 vaut" "\n"
        "`$00000101`.", src="Contrôle S3 2020/2021, ex. 5"),
    v("qd5", "Dans le programme de l'exercice, que vaut D5 à la fin ?", "1 if (lambda x: x-2**8*(x//2**7))((hexa('FF'))%2**8)>66 else 2", "hexa('00000002')", "`CMP.B #$42,D7` compare D7.B" "\n"
        "(`$FF`, soit" "\n"
        "$-1$ en signé) à" "\n"
        "`$42`" "\n"
        "($66$). `BGT` est signé : $-1>66$ est faux, pas de saut, D5 vaut $2$.", src="Contrôle S3 2020/2021, ex. 5"),
    v("qd6", "Dans le programme de l'exercice, que vaut D6 à la fin ?", "1 if hexa('FF')<=66 else 2", "hexa('00000002')", "`BLS` est non signé : D7.B `$FF` vaut" "\n"
        r"$255$, et $255\le66$ est faux : pas de saut, `MOVEQ.L #2,D6` est exécuté. D6 vaut $2$. (Avec `BLE`, signé, on aurait $-1\le66$ et un saut.)", src="Contrôle S3 2020/2021, ex. 5"),
    v("z2a", "On additionne sur 8 bits : `$E2 + $A8` (par exemple avec `ADD.B`). Donner le résultat (en hexadécimal, sur 8 bits).", "(hexa('E2')+hexa('A8'))%2**8", "hexa('8A')", "`$E2 + $A8 = $18A` ; sur 8 bits on garde" "\n"
        "`$8A`.", src="Rattrapage S3 2016/2017, ex. 2"),
    v("z2b", "On additionne sur 8 bits : `$E2 + $A8` (par exemple avec `ADD.B`). Donner les drapeaux N, Z, V, C (écrire NZVC en binaire, par exemple `%1010`).", "8*(((hexa('E2')+hexa('A8'))%2**8)//2**7)+4*(1-Min(1,(hexa('E2')+hexa('A8'))%2**8))+2*(abs(((hexa('E2')-2**8*(hexa('E2')//2**7))+(hexa('A8')-2**8*(hexa('A8')//2**7))+2**7)//2**8))+(hexa('E2')+hexa('A8'))//2**8", "bits('1001')", "`$E2 + $A8 = $18A` ; sur 8 bits on garde" "\n"
        "`$8A`." "\n"
        "N$=1$, Z$=0$, V$=0$ (pas de dépassement signé), C$=1$. On lit NZVC `1001`.", src="Rattrapage S3 2016/2017, ex. 2"),
    v("z2c", "On additionne sur 16 bits : `$8000 + $8000` (par exemple avec `ADD.W`). Donner le résultat (en hexadécimal, sur 16 bits).", "(hexa('8000')+hexa('8000'))%2**16", "hexa('0000')", "`$8000 + $8000 = $10000` ; sur 16 bits on garde" "\n"
        "`$0000`.", src="Rattrapage S3 2016/2017, ex. 2"),
    v("z2d", "On additionne sur 16 bits : `$8000 + $8000` (par exemple avec `ADD.W`). Donner les drapeaux N, Z, V, C (écrire NZVC en binaire, par exemple `%1010`).", "8*(((hexa('8000')+hexa('8000'))%2**16)//2**15)+4*(1-Min(1,(hexa('8000')+hexa('8000'))%2**16))+2*(abs(((hexa('8000')-2**16*(hexa('8000')//2**15))+(hexa('8000')-2**16*(hexa('8000')//2**15))+2**15)//2**16))+(hexa('8000')+hexa('8000'))//2**16", "bits('0111')", "`$8000 + $8000 = $10000` ; sur 16 bits on garde" "\n"
        "`$0000`." "\n"
        "N$=0$, Z$=1$, V$=1$ (dépassement signé), C$=1$. On lit NZVC `0111`.", src="Rattrapage S3 2016/2017, ex. 2"),
    o("q1a", "`GetStart` : A0.L pointe sur une chaîne, D0.B contient un caractère C présent dans la chaîne. Renvoyer dans A0.L l'adresse de la première occurrence de C (limité à $4$ lignes).", "```asm" "\n"
        "GetStart" "\n"
        "        CMP.B   (A0)+,D0       ; compare C à l'octet pointé, A0 avance" "\n"
        "        BNE     GetStart       ; pas encore C : on continue" "\n"
        "        SUBQ.L  #1,A0          ; A0 a dépassé C : on recule d'un octet" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "`CMP.B (A0)+,D0` calcule D0 $-$ (A0). Dès que les deux octets sont égaux, Z vaut $1$, mais A0 a déjà avancé : `SUBQ.L #1,A0` le replace sur le caractère. Corrigé officiel, vérifié sur un émulateur 68000.", src="Partiel S3 2022/2023, ex. 4.1", duree=6),
    o("q1b", "`GetEnd` : A0.L pointe sur un caractère non nul C d'une chaîne. Renvoyer dans A0.L l'adresse qui suit le dernier caractère d'une suite de C identiques. Exemple avec `Heeeellooooo Wooorld` : depuis le premier `e`, on renvoie l'adresse du premier `l` (limité à $12$ lignes).", "```asm" "\n"
        "GetEnd  MOVE.L  D0,-(A7)       ; D0 est utilisé : sauvegarde" "\n"
        "        MOVE.B  (A0)+,D0       ; C -> D0.B, A0 pointe sur le caractère suivant" "\n"
        r"\loop   CMP.B   (A0)+,D0       ; même caractère que C ?" "\n"
        r"        BEQ     \loop          ; oui : on continue" "\n"
        "        SUBQ.L  #1,A0          ; A0 a dépassé le premier caractère différent" "\n"
        "        MOVE.L  (A7)+,D0" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "Si le caractère suivant est différent, la première comparaison échoue et `SUBQ.L #1,A0` replace A0 sur lui. Sur le caractère nul final, la comparaison échoue (C n'est pas nul), donc A0 pointe sur le nul. Corrigé officiel, vérifié depuis $6$ positions de `Heeeellooooo Wooorld`.", src="Partiel S3 2022/2023, ex. 4.2", duree=8),
    o("q1c", "`SuccessiveCount` : avec `GetStart` et `GetEnd`, renvoyer dans D0.L le nombre de caractères identiques consécutifs à partir de la première occurrence du caractère D0.B dans la chaîne pointée par A0. Pour `Heeeellooooo Wooorld` : `H` donne $1$, `e` donne $4$, `l` donne $2$, `o` donne $5$ (limité à $12$ lignes).", "```asm" "\n"
        "SuccessiveCount" "\n"
        "        MOVE.L  A0,-(A7)       ; A0 doit être conservé" "\n"
        "        JSR     GetStart       ; A0 -> première occurrence de C" "\n"
        "        MOVE.L  A0,D0          ; début de la suite" "\n"
        "        JSR     GetEnd         ; A0 -> après la suite" "\n"
        "        SUBA.L  D0,A0          ; longueur = fin - début" "\n"
        "        MOVE.L  A0,D0" "\n"
        "        MOVE.L  (A7)+,A0" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "`GetEnd` sauvegarde D0 lui-même : on peut donc y ranger l'adresse de début avant de l'appeler. Corrigé officiel, vérifié sur un émulateur 68000 pour $H, e, l, o, W, d$ (D6 et A0 inchangés).", src="Partiel S3 2022/2023, ex. 4.3", duree=8),
    v("y1a", "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $FFFFFFFF   A0 = $00005000" "\n"
        "D1 = $0000FFF0   A1 = $00005008" "\n"
        "D2 = $0000000A   A2 = $00005010" "\n"
        "$005000  54 AF 18 B9 E7 21 48 C0" "\n"
        "$005008  C9 10 11 C8 D4 36 1F 88" "\n"
        "$005010  13 79 01 80 42 1A 2D 49" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVE.L $5006,-(A2)`. Donner les" "\n"
        "$8$ octets de la mémoire à partir de" "\n"
        "`$5008` après l'instruction, écrits comme un seul nombre hexadécimal de" "\n"
        "$16$ chiffres.", "hexa('C91011C8'+'48C0C910'+'')", "hexa('C91011C848C0C910')", "Avant : `C91011C8D4361F88`. L'instruction écrit `48C0C910` à partir de l'octet n° 4 de la fenêtre (adresse `$500C`) ; les autres octets ne changent pas. Après : `C91011C848C0C910`.", src="Partiel S3 2025/2026, ex. 1"),
    v("y1b", "Valeurs initiales : A2 `$5010`. Quelle est la valeur de A2 après" "\n"
        "`MOVE.L $5006,-(A2)` ?", "hexa('5010')-4", "hexa('500C')", "La destination `-(A2)` retire $4$ à A2 :" "\n"
        "`$500C` (l'adresse où l'on écrit).", src="Partiel S3 2025/2026, ex. 1"),
    v("y1c", "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $FFFFFFFF   A0 = $00005000" "\n"
        "D1 = $0000FFF0   A1 = $00005008" "\n"
        "D2 = $0000000A   A2 = $00005010" "\n"
        "$005000  54 AF 18 B9 E7 21 48 C0" "\n"
        "$005008  C9 10 11 C8 D4 36 1F 88" "\n"
        "$005010  13 79 01 80 42 1A 2D 49" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVE.W #5001,3(A1,D0.L)`. Donner les $8$ octets de la mémoire à partir de" "\n"
        "`$5008` après l'instruction, écrits comme un seul nombre hexadécimal de" "\n"
        "$16$ chiffres.", "hexa('C910'+'1389'+'D4361F88')", "hexa('C9101389D4361F88')", "Avant : `C91011C8D4361F88`. L'instruction écrit `1389` à partir de l'octet n° 2 de la fenêtre (adresse `$500A`) ; les autres octets ne changent pas. Après : `C9101389D4361F88`.", src="Partiel S3 2025/2026, ex. 1"),
    v("y1d", "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $FFFFFFFF   A0 = $00005000" "\n"
        "D1 = $0000FFF0   A1 = $00005008" "\n"
        "D2 = $0000000A   A2 = $00005010" "\n"
        "$005000  54 AF 18 B9 E7 21 48 C0" "\n"
        "$005008  C9 10 11 C8 D4 36 1F 88" "\n"
        "$005010  13 79 01 80 42 1A 2D 49" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVE.B -8(A2),9(A2,D1.W)`. Donner les $8$ octets de la mémoire à partir de" "\n"
        "`$5008` après l'instruction, écrits comme un seul nombre hexadécimal de" "\n"
        "$16$ chiffres.", "hexa('C9'+'C9'+'11C8D4361F88')", "hexa('C9C911C8D4361F88')", "Avant : `C91011C8D4361F88`. L'instruction écrit `C9` à partir de l'octet n° 1 de la fenêtre (adresse `$5009`) ; les autres octets ne changent pas. Après : `C9C911C8D4361F88`.", src="Partiel S3 2025/2026, ex. 1"),
    o("q3a", "`IsBlank` : D1.B contient le code ASCII d'un caractère. Renvoyer dans D0.L $0$ si le caractère est blanc (espace ou tabulation, de code $9$), $1$ sinon.", "```asm" "\n"
        "IsBlank CMPI.B  #' ',D1          ; espace ?" "\n"
        r"        BEQ     \blank" "\n"
        "        CMPI.B  #9,D1           ; tabulation ?" "\n"
        r"        BEQ     \blank" "\n"
        "        MOVEQ.L #1,D0           ; ni l'un ni l'autre : D0 = 1" "\n"
        "        RTS" "\n"
        r"\blank  MOVEQ.L #0,D0           ; blanc : D0 = 0" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "D0 est un registre de sortie ; aucun autre registre n'est modifié. Corrigé officiel, vérifié sur un émulateur 68000.", src="Partiel S3 2016/2017, ex. 1.1", duree=5),
    o("q3b", "`BlankCount` : A0.L pointe sur une chaîne ; renvoyer dans D0.L le nombre de caractères blancs, en utilisant `IsBlank`. Indication : utiliser D2 comme compteur (D0 est utilisé par `IsBlank`), puis le copier dans D0.", "```asm" "\n"
        "BlankCount" "\n"
        "        MOVEM.L D1/D2/A0,-(A7)" "\n"
        "        CLR.L   D2              ; compteur de blancs" "\n"
        r"\loop   MOVE.B  (A0)+,D1        ; caractère courant dans D1.B" "\n"
        r"        BEQ     \quit           ; octet nul : fin" "\n"
        "        JSR     IsBlank" "\n"
        "        TST.L   D0" "\n"
        r"        BNE     \loop           ; non blanc : suivant" "\n"
        "        ADDQ.L  #1,D2           ; blanc : on compte" "\n"
        r"        BRA     \loop" "\n"
        r"\quit   MOVE.L  D2,D0           ; résultat dans D0" "\n"
        "        MOVEM.L (A7)+,D1/D2/A0" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "D0 est le registre de sortie, il n'est donc pas sauvegardé. Corrigé officiel, vérifié sur un émulateur 68000 (`a b<tab>c  d` contient $4$ blancs).", src="Partiel S3 2016/2017, ex. 1.2", duree=8),
    o("q3c", "`BlankToUnderscore` : A0.L pointe sur une chaîne ; remplacer chaque caractère blanc par un caractère `'_'`, en utilisant `IsBlank`. Aucun registre ne doit être modifié.", "```asm" "\n"
        "BlankToUnderscore" "\n"
        "        MOVEM.L D0/D1/A0,-(A7)" "\n"
        r"\loop   MOVE.B  (A0)+,D1        ; caractère courant, A0 avance" "\n"
        r"        BEQ     \quit" "\n"
        "        JSR     IsBlank" "\n"
        "        TST.L   D0" "\n"
        r"        BNE     \loop           ; pas blanc : suivant" "\n"
        "        MOVE.B  #'_',-1(A0)     ; blanc : on remplace le caractère déjà lu" "\n"
        r"        BRA     \loop" "\n"
        r"\quit   MOVEM.L (A7)+,D0/D1/A0" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "Après `(A0)+`, le caractère lu est à `-1(A0)`. Ici D0 n'est pas un registre de sortie : il est sauvegardé. Corrigé officiel, vérifié sur un émulateur 68000.", src="Partiel S3 2016/2017, ex. 1.3", duree=8),
]

VARIANTS = {
    "n11": [
        {"enonce": "Convertir `$2EF8` en décimal.", "calc": "2*4096+14*256+15*16+8", "ans": "hexa('2EF8')", "sol": r"$2\times4096+14\times256+15\times16+8=12024$."},
    ],
    "n12": [
        {"enonce": "Convertir le nombre décimal $255$ en hexadécimal.", "calc": "255", "ans": "hexa('FF')", "sol": r"$255=15\times16+15$, soit" "\n"
        "`$FF`."},
    ],
    "n13": [
        {"enonce": "Quelle est la valeur signée de l'octet `$9C` ?", "calc": "156-256", "ans": "tc('10011100')", "sol": "`$9C` vaut" "\n"
        "$156$ non signé, bit de poids fort $1$ : $156-256=-100$."},
    ],
    "n14": [
        {"enonce": "Quelle est la valeur signée du mot long `$FFFFFFF0` ?", "calc": "hexa('FFFFFFF0')-2**32", "ans": "-16", "sol": "$2^{32}-16$ en non signé : la valeur signée est $-16$."},
    ],
    "n15": [
        {"enonce": "Étendre en signe l'octet `$7A` sur" "\n"
        "$16$ bits. Donner le mot obtenu.", "calc": "hexa('7A')", "ans": "hexa('007A')", "sol": "Le bit de poids fort vaut $0$ : on remplit avec des $0$, d'où" "\n"
        "`$007A`."},
    ],
    "n16": [
        {"enonce": "Écrire $-100$ sur $8$ bits en hexadécimal.", "calc": "2**8-100", "ans": "hexa('9C')", "sol": "$256-100=156$, soit" "\n"
        "`$9C`."},
    ],
    "n17": [
        {"enonce": "Additionner `$B4` et" "\n"
        "`$4C` en hexadécimal (résultat complet).", "calc": "180+76", "ans": "hexa('100')", "sol": "$180+76=256$, soit" "\n"
        "`$100`."},
    ],
    "m21": [
        {"enonce": "Une mémoire d'octets a $20$ fils d'adresse. Combien de Mio contient-elle ?", "calc": "2**20/2**20", "ans": "1", "sol": "$2^{20}$ octets $=1$ Mio."},
    ],
    "m22": [
        {"enonce": "Mémoire à partir de `$2000` :" "\n"
        "" "\n"
        "```" "\n"
        "$2000 : 10 20 30 40 50 60" "\n"
        "```" "\n"
        "" "\n"
        "Quelle est la valeur du mot de $16$ bits situé à l'adresse" "\n"
        "`$2004` ?", "calc": "80*256+96", "ans": "hexa('5060')", "sol": "Les octets à `$2004` et" "\n"
        "`$2005` sont `50` et `60` : le mot vaut" "\n"
        "`$5060`."},
    ],
    "m23": [
        {"enonce": "Mémoire à partir de `$3000` :" "\n"
        "" "\n"
        "```" "\n"
        "$3000 : 00 00 12 34 AB CD EF 01" "\n"
        "```" "\n"
        "" "\n"
        "Quelle est la valeur du mot long à l'adresse `$3004` ?", "calc": "171*2**24+205*2**16+239*256+1", "ans": "hexa('ABCDEF01')", "sol": "Les quatre octets à partir de `$3004` sont `AB CD EF 01` :" "\n"
        "`$ABCDEF01`."},
    ],
    "m24": [
        {"enonce": "```asm" "\n"
        "        ORG   $2000" "\n"
        "        DC.B  1,2,3,4" "\n"
        "        DC.W  7,8,9" "\n"
        "L       DC.L  1" "\n"
        "```" "\n"
        "" "\n"
        "Quelle est la valeur de l'étiquette `L` ?", "calc": "hexa('2000')+4+3*2", "ans": "hexa('200A')", "sol": r"$4$ octets puis $3\times2=6$ octets : $10$ octets de données, donc `L` vaut" "\n"
        "`$200A`."},
    ],
    "m25": [
        {"enonce": "```asm" "\n"
        "        ORG   $6000" "\n"
        "A       DS.B  2" "\n"
        "B       DS.W  5" "\n"
        "C       DS.L  2" "\n"
        "END" "\n"
        "```" "\n"
        "" "\n"
        "Quelle est la valeur de l'étiquette `END` ?", "calc": "hexa('6000')+2+5*2+2*4", "ans": "hexa('6014')", "sol": "$2+10+8=20$ octets réservés ($20=14_{16}$) : `END` vaut" "\n"
        "`$6014`."},
    ],
    "m27": [
        {"enonce": "Une mémoire a $16$ fils d'adresse et $16$ fils de donnée. Quelle est sa capacité en Kio ?", "calc": "2**16*16/8/2**10", "ans": "128", "sol": r"$2^{16}\times16/8=2^{17}$ octets $=128$ Kio."},
    ],
    "r31": [
        {"enonce": "Combien de bits contiennent au total les registres d'adresse A0 à A7 et les registres de donnée D0 à D7 ensemble ?", "calc": "16*32", "ans": "512", "sol": "$16$ registres de $32$ bits : $512$ bits."},
    ],
    "r32": [
        {"enonce": "Le registre A1 contient `$A1B2C3D4`. À quelle adresse accède-t-on ?", "calc": "hexa('A1B2C3D4')%2**24", "ans": "hexa('B2C3D4')", "sol": "On retire l'octet de poids fort `$A1` :" "\n"
        "`$B2C3D4`."},
    ],
    "r33": [
        {"enonce": "Quelle est la taille minimale, en bits, d'une instruction du 68000 ?", "calc": "16", "ans": "16", "sol": "Un mot de $16$ bits (soit $2$ octets)."},
    ],
    "r34": [
        {"enonce": "Le CCR contient $5$ drapeaux utiles (X, N, Z, V, C). Combien de bits du CCR sont inutilisés ?", "calc": "8-5", "ans": "3", "sol": "$8-5=3$ bits inutilisés."},
    ],
    "r35": [
        {"enonce": "Même question avec X$=1$, N$=0$, Z$=1$, V$=0$, C$=1$.", "calc": "16+4+1", "ans": "bits('10101')", "sol": "$16+4+1=21$, soit `%10101`."},
    ],
    "s41": [
        {"enonce": "D0 contient `$11223344` et D1 contient" "\n"
        "`$AABBCCDD`. Que contient D1 après `MOVE.W D0,D1` ?", "calc": "(hexa('AABBCCDD')-hexa('AABBCCDD')%2**16)+hexa('11223344')%2**16", "ans": "hexa('AABB3344')", "sol": "`MOVE.W` copie les 16 bits de poids faible de D0 (`$3344`) dans D1. D1 vaut" "\n"
        "`$AABB3344`."},
        {"enonce": "D0 contient `$000000FE` et D1 contient" "\n"
        "`$12345678`. Que contient D1 après `MOVE.B D0,D1` ?", "calc": "(hexa('12345678')-hexa('12345678')%2**8)+hexa('000000FE')%2**8", "ans": "hexa('123456FE')", "sol": "`MOVE.B` copie les 8 bits de poids faible de D0 (`$FE`) dans D1. D1 vaut" "\n"
        "`$123456FE`."},
    ],
    "s42": [
        {"enonce": "D0 contient `$11223344` et D1 contient" "\n"
        "`$AABBCCDD`. Que contient D1 après `MOVE.L D0,D1` ?", "calc": "(hexa('AABBCCDD')-hexa('AABBCCDD')%2**32)+hexa('11223344')%2**32", "ans": "hexa('11223344')", "sol": "`MOVE.L` copie les 32 bits de poids faible de D0 (`$11223344`) dans D1. D1 vaut" "\n"
        "`$11223344`."},
        {"enonce": "D0 contient `$0000FFFF` et D1 contient" "\n"
        "`$00000001`. Que contient D1 après `MOVE.W D0,D1` ?", "calc": "(hexa('00000001')-hexa('00000001')%2**16)+hexa('0000FFFF')%2**16", "ans": "hexa('0000FFFF')", "sol": "`MOVE.W` copie les 16 bits de poids faible de D0 (`$FFFF`) dans D1. D1 vaut" "\n"
        "`$0000FFFF`."},
    ],
    "s43": [
        {"enonce": "D0 contient `$11223344`. Que contient D0 après `MOVE.B #255,D0` ?", "calc": "(hexa('11223344')-hexa('11223344')%2**8)+255", "ans": "hexa('112233FF')", "sol": "$255$ s'écrit" "\n"
        "`$FF` : il remplace l'octet de poids faible, D0 vaut" "\n"
        "`$112233FF`."},
    ],
    "s44": [
        {"enonce": "D3 contient `$FFFFFFFF`. Que contient D3 après `MOVE.L #1960,D3` ?", "calc": "1960", "ans": "hexa('7A8')", "sol": "$1960$ s'écrit" "\n"
        "`$7A8` : D3 vaut" "\n"
        "`$000007A8`."},
    ],
    "s45": [
        {"enonce": "D1 contient `$12345678`. Que contient D1 après `MOVEQ.L #100,D1` ?", "calc": "100", "ans": "hexa('64')", "sol": "$100$ s'écrit" "\n"
        "`$64` ; l'entier est positif : D1 vaut" "\n"
        "`$00000064` (tous les bits de poids fort sont remplacés)."},
    ],
    "s46": [
        {"enonce": "D0 contient `$1122FF80`. Que contient D0 après `EXT.L D0` ?", "calc": "hexa('FF80')+(2**32-2**16)", "ans": "hexa('FFFFFF80')", "sol": "`EXT.L` étend le signe de D0.W (`$FF80`, négatif) sur" "\n"
        "$32$ bits :" "\n"
        "`$FFFFFF80`."},
    ],
    "s47": [
        {"enonce": "A1 contient `$00AB1234` et D2 contient" "\n"
        "`$FFFFFFFF`. Que contient D2 après `MOVE.W A1,D2` ?", "calc": "(hexa('FFFFFFFF')-hexa('FFFFFFFF')%2**16)+hexa('00AB1234')%2**16", "ans": "hexa('FFFF1234')", "sol": "Mot de poids faible de A1 : `$1234`. D2 vaut" "\n"
        "`$FFFF1234`."},
    ],
    "s48": [
        {"enonce": "D1 contient `$12345678`. Que contient D1 après `CLR.B D1` ?", "calc": "hexa('12345678')-hexa('12345678')%2**8", "ans": "hexa('12345600')", "sol": "`CLR.B` met l'octet de poids faible à $0$ :" "\n"
        "`$12345600`."},
    ],
    "f51": [
        {"enonce": "On additionne sur 8 bits : `$5D + $6F` (par exemple avec `ADD.B`). Donner le résultat (en hexadécimal, sur 8 bits).", "calc": "(hexa('5D')+hexa('6F'))%2**8", "ans": "hexa('CC')", "sol": "`$5D + $6F = $CC` ; sur 8 bits on garde" "\n"
        "`$CC`."},
        {"enonce": "On additionne sur 16 bits : `$7AAA + $9444` (par exemple avec `ADD.W`). Donner le résultat (en hexadécimal, sur 16 bits).", "calc": "(hexa('7AAA')+hexa('9444'))%2**16", "ans": "hexa('0EEE')", "sol": "`$7AAA + $9444 = $10EEE` ; sur 16 bits on garde" "\n"
        "`$0EEE`."},
    ],
    "f52": [
        {"enonce": "On additionne sur 8 bits : `$7F + $7F` (par exemple avec `ADD.B`). Donner le drapeau N.", "calc": "((hexa('7F')+hexa('7F'))%2**8)//2**7", "ans": "1", "sol": "`$7F + $7F = $FE` ; sur 8 bits on garde" "\n"
        "`$FE`. N est le bit de poids fort du résultat :" "\n"
        "N$=1$."},
        {"enonce": "On additionne sur 16 bits : `$4AC9 + $D841` (par exemple avec `ADD.W`). Donner le drapeau N.", "calc": "((hexa('4AC9')+hexa('D841'))%2**16)//2**15", "ans": "0", "sol": "`$4AC9 + $D841 = $1230A` ; sur 16 bits on garde" "\n"
        "`$230A`. N est le bit de poids fort du résultat :" "\n"
        "N$=0$."},
    ],
    "f53": [
        {"enonce": "On additionne sur 8 bits : `$B4 + $4C` (par exemple avec `ADD.B`). Donner le drapeau Z.", "calc": "1-Min(1,(hexa('B4')+hexa('4C'))%2**8)", "ans": "1", "sol": "`$B4 + $4C = $100` ; sur 8 bits on garde" "\n"
        "`$00`. Le résultat tronqué est nul :" "\n"
        "Z$=1$."},
        {"enonce": "On additionne sur 32 bits : `$FFFFFFFF + $00000015` (par exemple avec `ADD.L`). Donner le drapeau Z.", "calc": "1-Min(1,(hexa('FFFFFFFF')+hexa('00000015'))%2**32)", "ans": "0", "sol": "`$FFFFFFFF + $00000015 = $100000014` ; sur 32 bits on garde" "\n"
        "`$00000014`. Le résultat tronqué est non nul :" "\n"
        "Z$=0$."},
    ],
    "f54": [
        {"enonce": "On additionne sur 32 bits : `$70000000 + $10000000` (par exemple avec `ADD.L`). Donner le drapeau V.", "calc": "abs(((hexa('70000000')-2**32*(hexa('70000000')//2**31))+(hexa('10000000')-2**32*(hexa('10000000')//2**31))+2**31)//2**32)", "ans": "1", "sol": "`$70000000 + $10000000 = $80000000` ; sur 32 bits on garde" "\n"
        "`$80000000`. Signes : opérandes positif et positif, résultat négatif :" "\n"
        "V$=1$."},
        {"enonce": "On additionne sur 8 bits : `$5A + $A5` (par exemple avec `ADD.B`). Donner le drapeau V.", "calc": "abs(((hexa('5A')-2**8*(hexa('5A')//2**7))+(hexa('A5')-2**8*(hexa('A5')//2**7))+2**7)//2**8)", "ans": "0", "sol": "`$5A + $A5 = $FF` ; sur 8 bits on garde" "\n"
        "`$FF`. Signes : opérandes positif et négatif, résultat négatif :" "\n"
        "V$=0$."},
    ],
    "f55": [
        {"enonce": "On additionne sur 16 bits : `$9F00 + $8E00` (par exemple avec `ADD.W`). Donner le drapeau C.", "calc": "(hexa('9F00')+hexa('8E00'))//2**16", "ans": "1", "sol": "`$9F00 + $8E00 = $12D00` ; sur 16 bits on garde" "\n"
        "`$2D00`. La somme dépasse 16 bits (retenue) :" "\n"
        "C$=1$."},
        {"enonce": "On additionne sur 16 bits : `$8000 + $8000` (par exemple avec `ADD.W`). Donner le drapeau C.", "calc": "(hexa('8000')+hexa('8000'))//2**16", "ans": "1", "sol": "`$8000 + $8000 = $10000` ; sur 16 bits on garde" "\n"
        "`$0000`. La somme dépasse 16 bits (retenue) :" "\n"
        "C$=1$."},
    ],
    "f56": [
        {"enonce": "On additionne sur 16 bits : `$7005 + $7005` (par exemple avec `ADD.W`). Donner les drapeaux N, Z, V, C (écrire NZVC en binaire, par exemple `%1010`).", "calc": "8*(((hexa('7005')+hexa('7005'))%2**16)//2**15)+4*(1-Min(1,(hexa('7005')+hexa('7005'))%2**16))+2*(abs(((hexa('7005')-2**16*(hexa('7005')//2**15))+(hexa('7005')-2**16*(hexa('7005')//2**15))+2**15)//2**16))+(hexa('7005')+hexa('7005'))//2**16", "ans": "bits('1010')", "sol": "`$7005 + $7005 = $E00A` ; sur 16 bits on garde" "\n"
        "`$E00A`." "\n"
        "N$=1$, Z$=0$, V$=1$ (dépassement signé), C$=0$. On lit NZVC `1010`."},
        {"enonce": "On additionne sur 16 bits : `$8000 + $8000` (par exemple avec `ADD.W`). Donner les drapeaux N, Z, V, C (écrire NZVC en binaire, par exemple `%1010`).", "calc": "8*(((hexa('8000')+hexa('8000'))%2**16)//2**15)+4*(1-Min(1,(hexa('8000')+hexa('8000'))%2**16))+2*(abs(((hexa('8000')-2**16*(hexa('8000')//2**15))+(hexa('8000')-2**16*(hexa('8000')//2**15))+2**15)//2**16))+(hexa('8000')+hexa('8000'))//2**16", "ans": "bits('0111')", "sol": "`$8000 + $8000 = $10000` ; sur 16 bits on garde" "\n"
        "`$0000`." "\n"
        "N$=0$, Z$=1$, V$=1$ (dépassement signé), C$=1$. On lit NZVC `0111`."},
    ],
    "f57": [
        {"enonce": "On additionne sur 32 bits : `$A0A0A0A0 + $A0A0A0A0` (par exemple avec `ADD.L`). Donner les drapeaux N, Z, V, C (écrire NZVC en binaire, par exemple `%1010`).", "calc": "8*(((hexa('A0A0A0A0')+hexa('A0A0A0A0'))%2**32)//2**31)+4*(1-Min(1,(hexa('A0A0A0A0')+hexa('A0A0A0A0'))%2**32))+2*(abs(((hexa('A0A0A0A0')-2**32*(hexa('A0A0A0A0')//2**31))+(hexa('A0A0A0A0')-2**32*(hexa('A0A0A0A0')//2**31))+2**31)//2**32))+(hexa('A0A0A0A0')+hexa('A0A0A0A0'))//2**32", "ans": "bits('0011')", "sol": "`$A0A0A0A0 + $A0A0A0A0 = $141414140` ; sur 32 bits on garde" "\n"
        "`$41414140`." "\n"
        "N$=0$, Z$=0$, V$=1$ (dépassement signé), C$=1$. On lit NZVC `0011`."},
        {"enonce": "On additionne sur 8 bits : `$5D + $6F` (par exemple avec `ADD.B`). Donner les drapeaux N, Z, V, C (écrire NZVC en binaire, par exemple `%1010`).", "calc": "8*(((hexa('5D')+hexa('6F'))%2**8)//2**7)+4*(1-Min(1,(hexa('5D')+hexa('6F'))%2**8))+2*(abs(((hexa('5D')-2**8*(hexa('5D')//2**7))+(hexa('6F')-2**8*(hexa('6F')//2**7))+2**7)//2**8))+(hexa('5D')+hexa('6F'))//2**8", "ans": "bits('1010')", "sol": "`$5D + $6F = $CC` ; sur 8 bits on garde" "\n"
        "`$CC`." "\n"
        "N$=1$, Z$=0$, V$=1$ (dépassement signé), C$=0$. On lit NZVC `1010`."},
    ],
    "f58": [
        {"enonce": "D0 contient `$30` (taille 8 bits : on ne regarde que D0.B). On exécute" "\n"
        "`CMP.B #$25,D0`. Donner le drapeau C.", "calc": "Max(0,Min(1,hexa('25')-hexa('30')))", "ans": "0", "sol": "`CMP`/`SUB` calculent destination $-$ source :" "\n"
        "`$30 - $25` donne" "\n"
        "`$0B` sur 8 bits." "\n"
        "C$=0$ : pas d'emprunt, la destination est supérieure ou égale à la source en non signé."},
    ],
    "f59": [
        {"enonce": "D0 contient `$80` (taille 8 bits : on ne regarde que D0.B). On exécute" "\n"
        "`CMP.B #$01,D0`. Donner le drapeau V.", "calc": "abs(((hexa('80')-2**8*(hexa('80')//2**7))-(hexa('01')-2**8*(hexa('01')//2**7))+2**7)//2**8)", "ans": "1", "sol": "`CMP`/`SUB` calculent destination $-$ source :" "\n"
        "`$80 - $01` donne" "\n"
        "`$7F` sur 8 bits." "\n"
        "V$=1$ : dépassement signé (-128 - 1 = -129 sort de la plage signée sur 8 bits)."},
    ],
    "f510": [
        {"enonce": "D0 contient `$11` (taille 8 bits : on ne regarde que D0.B). On exécute" "\n"
        "`CMP.B #$12,D0`. Donner le drapeau Z.", "calc": "1-Min(1,(hexa('11')-hexa('12'))%2**8)", "ans": "0", "sol": "`CMP`/`SUB` calculent destination $-$ source :" "\n"
        "`$11 - $12` donne" "\n"
        "`$FF` sur 8 bits." "\n"
        "Z$=0$ (résultat non nul)."},
    ],
    "a61": [
        {"enonce": "Même état. On exécute deux fois `MOVE.W (A1)+,D0` (A1 vaut `$1008`). Quelle est la valeur finale de D0 ?", "calc": "(hexa('11223344')-hexa('11223344')%2**16)+57*256+152", "ans": "hexa('11223998')", "sol": "Premier mot lu à `$1008` :" "\n"
        "`$AD45` ; second mot lu à" "\n"
        "`$100A` :" "\n"
        "`$3998`. D0.W vaut" "\n"
        "`$3998`, les" "\n"
        "$16$ bits de poids fort de D0 ne changent pas :" "\n"
        "`$11223998`."},
    ],
    "a62": [
        {"enonce": "Même état. On exécute `MOVE.L D1,(A1)+` puis `MOVE.W D1,(A1)+` puis `MOVE.B D1,(A1)+` (A1 vaut `$1008`). Valeur finale de A1 ?", "calc": "hexa('1008')+4+2+1", "ans": "hexa('100F')", "sol": "$4+2+1=7$ : A1 vaut" "\n"
        "`$100F`."},
    ],
    "a63": [
        {"enonce": "Même état. On exécute `MOVE.W -(A1),D0` puis `MOVE.W -(A1),D0`. Valeur finale de D0 ?", "calc": "(hexa('11223344')-hexa('11223344')%2**16)+181*256+243", "ans": "hexa('1122B5F3')", "sol": "Premier `MOVE.W -(A1),D0` : A1 passe à `$1006`, on lit le mot" "\n"
        "`$3C32`. Second : A1 passe à" "\n"
        "`$1004`, on lit" "\n"
        "`$B5F3`. D0 vaut" "\n"
        "`$1122B5F3`."},
    ],
    "a64": [
        {"enonce": "Même état. On exécute `MOVE.B -(A2),D0` puis `MOVE.L -(A2),D0` (A2 vaut `$1010`). Valeur finale de A2 ?", "calc": "hexa('1010')-1-4", "ans": "hexa('100B')", "sol": "A2 diminue de $1$ puis de $4$ :" "\n"
        "`$100B`."},
    ],
    "a65": [
        {"enonce": "Même état. On exécute `MOVE.W -(A2),-(A1)` (A1 vaut `$1008`, A2 vaut" "\n"
        "`$1010`). Valeur du mot situé à" "\n"
        "`$1006` après l'instruction ?", "calc": "156*256+157", "ans": "hexa('9C9D')", "sol": "Source : A2 passe à `$100E`, on lit le mot" "\n"
        "`$9C9D`. Destination : A1 passe à" "\n"
        "`$1006` et on y écrit" "\n"
        "`$9C9D`."},
    ],
    "e71": [
        {"enonce": "Dans `MOVE.B -5(A1),D0` :" "\n"
        "" "\n"
        "```" "\n"
        "A1 = $00001008" "\n"
        "```" "\n"
        "" "\n"
        "Quelle est l'adresse effective de l'opérande `-5(A1)` ?", "calc": "hexa('1008')-5", "ans": "hexa('1003')", "sol": "A1 vaut `$1008` : A1 moins" "\n"
        "$5$ donne" "\n"
        "`$1003`."},
    ],
    "e72": [
        {"enonce": "Dans `MOVE.B 2(A1,A3.W),D0` :" "\n"
        "" "\n"
        "```" "\n"
        "A1 = $00001008" "\n"
        "A3 = $00000006" "\n"
        "```" "\n"
        "" "\n"
        "Quelle est l'adresse effective de l'opérande `2(A1,A3.W)` ?", "calc": "hexa('1008')+2+6", "ans": "hexa('1010')", "sol": "A1 vaut `$1008`, d8 vaut" "\n"
        "$2$, A3.W vaut $6$ :" "\n"
        "`$1010`."},
    ],
    "e73": [
        {"enonce": "Même instruction avec un autre index :" "\n"
        "" "\n"
        "```" "\n"
        "D1 = $FFFFFFF0   A2 = $0000500A" "\n"
        "```" "\n"
        "" "\n"
        "Quelle est l'adresse effective de l'opérande `34(A2,D1.L)` ?", "calc": "hexa('500A')+34-16", "ans": "hexa('501C')", "sol": "D1.L vaut $-16$ :" "\n"
        "`$500A` plus" "\n"
        "$34$ moins $16$ donne" "\n"
        "`$501C`."},
    ],
    "e74": [
        {"enonce": "Autre cas : l'index `.W` est négatif." "\n"
        "" "\n"
        "```" "\n"
        "D0 = $0001FFFE   A1 = $00005008" "\n"
        "```" "\n"
        "" "\n"
        "Quelle est l'adresse effective de l'opérande `$10(A1,D0.W)` ?", "calc": "hexa('5008')+hexa('10')-2", "ans": "hexa('5016')", "sol": "D0.W vaut `$FFFE`, soit" "\n"
        "$-2$ :" "\n"
        "`$5008` plus" "\n"
        "`$10` moins" "\n"
        "$2$ donne" "\n"
        "`$5016`."},
    ],
    "e75": [
        {"enonce": "Avec l'état du cours (D0 vaut `$0000FFFF`) :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $0000FFFF   A1 = $00001008" "\n"
        "```" "\n"
        "" "\n"
        "Quelle est l'adresse effective de l'opérande `-1(A1,D0.W)` ?", "calc": "hexa('1008')-1-1", "ans": "hexa('1006')", "sol": "D0.W vaut `$FFFF`, soit" "\n"
        "$-1$ :" "\n"
        "`$1008` moins" "\n"
        "$1$ moins $1$ donne" "\n"
        "`$1006`."},
    ],
    "e76": [
        {"enonce": "Même mémoire. Quelle est la valeur de D2 après `MOVE.L $100A,D2` ?", "calc": "57*2**24+152*2**16+154*256+155", "ans": "hexa('39989A9B')", "sol": "Mot long lu à `$100A` : `39 98 9A 9B`, donc" "\n"
        "`$39989A9B`."},
    ],
    "e77": [
        {"enonce": "Même mémoire. Quelle est la valeur de D0 après `MOVE.W $100C(PC),D0` ?", "calc": "(hexa('11223344')-hexa('11223344')%2**16)+154*256+155", "ans": "hexa('11229A9B')", "sol": "Mot lu à `$100C` :" "\n"
        "`$9A9B`. D0 vaut" "\n"
        "`$11229A9B`."},
    ],
    "e78": [
        {"enonce": "Quel est le plus petit déplacement d'un mode `d8(An,Xn)` (déplacement signé sur $8$ bits) ?", "calc": "-2**7", "ans": "-128", "sol": r"$d_8\in[-128,127]$ : le plus petit est $-2^7=-128$."},
    ],
    "g81": [
        {"enonce": "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $FFFFFFFB   A0 = $00005000" "\n"
        "D1 = $00000008   A1 = $00005008" "\n"
        "D2 = $4444FFFE   A2 = $00005010" "\n"
        "$005000  54 AF 18 B9 E7 21 48 C0" "\n"
        "$005008  C9 10 11 C8 D4 36 1F 88" "\n"
        "$005010  13 79 01 80 42 1A 2D 49" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVE.W #52,(A0)+`. Donner les $8$ octets de la mémoire à partir de" "\n"
        "`$5000` après l'instruction, écrits comme un seul nombre hexadécimal de" "\n"
        "$16$ chiffres.", "calc": "hexa(''+'0034'+'18B9E72148C0')", "ans": "hexa('003418B9E72148C0')", "sol": "Avant : `54AF18B9E72148C0`. L'instruction écrit `0034` à partir de l'octet n° 0 de la fenêtre (adresse `$5000`) ; les autres octets ne changent pas. Après : `003418B9E72148C0`."},
    ],
    "g82": [
        {"enonce": "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $0004FFFF   A0 = $00005000" "\n"
        "D1 = $FFFF0005   A1 = $00005008" "\n"
        "D2 = $FFFFFFFE   A2 = $00005010" "\n"
        "$005000  54 AF 18 B9 E7 21 48 C0" "\n"
        "$005008  C9 10 11 C8 D4 36 1F 88" "\n"
        "$005010  13 79 01 80 42 1A 2D 49" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVE.L (A2)+,(A0)+`. Donner les $8$ octets de la mémoire à partir de" "\n"
        "`$5000` après l'instruction, écrits comme un seul nombre hexadécimal de" "\n"
        "$16$ chiffres.", "calc": "hexa(''+'13790180'+'E72148C0')", "ans": "hexa('13790180E72148C0')", "sol": "Avant : `54AF18B9E72148C0`. L'instruction écrit `13790180` à partir de l'octet n° 0 de la fenêtre (adresse `$5000`) ; les autres octets ne changent pas. Après : `13790180E72148C0`."},
    ],
    "g83": [
        {"enonce": "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $FFFFFFFF   A0 = $00005000" "\n"
        "D1 = $0000FFF0   A1 = $00005008" "\n"
        "D2 = $0000000A   A2 = $00005010" "\n"
        "$005000  54 AF 18 B9 E7 21 48 C0" "\n"
        "$005008  C9 10 11 C8 D4 36 1F 88" "\n"
        "$005010  13 79 01 80 42 1A 2D 49" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVE.L $5006,-(A2)`. Donner les" "\n"
        "$8$ octets de la mémoire à partir de" "\n"
        "`$5008` après l'instruction, écrits comme un seul nombre hexadécimal de" "\n"
        "$16$ chiffres.", "calc": "hexa('C91011C8'+'48C0C910'+'')", "ans": "hexa('C91011C848C0C910')", "sol": "Avant : `C91011C8D4361F88`. L'instruction écrit `48C0C910` à partir de l'octet n° 4 de la fenêtre (adresse `$500C`) ; les autres octets ne changent pas. Après : `C91011C848C0C910`."},
    ],
    "g84": [
        {"enonce": "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $0004FFFF   A0 = $00005000" "\n"
        "D1 = $FFFF0005   A1 = $00005008" "\n"
        "D2 = $FFFFFFFE   A2 = $00005010" "\n"
        "$005000  54 AF 18 B9 E7 21 48 C0" "\n"
        "$005008  C9 10 11 C8 D4 36 1F 88" "\n"
        "$005010  13 79 01 80 42 1A 2D 49" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVE.B $500A,-1(A1,D0.W)`. Donner les" "\n"
        "$8$ octets de la mémoire à partir de" "\n"
        "`$5000` après l'instruction, écrits comme un seul nombre hexadécimal de" "\n"
        "$16$ chiffres.", "calc": "hexa('54AF18B9E721'+'11'+'C0')", "ans": "hexa('54AF18B9E72111C0')", "sol": "Avant : `54AF18B9E72148C0`. L'instruction écrit `11` à partir de l'octet n° 6 de la fenêtre (adresse `$5006`) ; les autres octets ne changent pas. Après : `54AF18B9E72111C0`."},
    ],
    "g85": [
        {"enonce": "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $0004FFFF   A0 = $00005000" "\n"
        "D1 = $FFFF0005   A1 = $00005008" "\n"
        "D2 = $FFFFFFFE   A2 = $00005010" "\n"
        "$005000  54 AF 18 B9 E7 21 48 C0" "\n"
        "$005008  C9 10 11 C8 D4 36 1F 88" "\n"
        "$005010  13 79 01 80 42 1A 2D 49" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVE.L #$500A,-5(A1,D1.W)`. Donner les" "\n"
        "$8$ octets de la mémoire à partir de" "\n"
        "`$5008` après l'instruction, écrits comme un seul nombre hexadécimal de" "\n"
        "$16$ chiffres.", "calc": "hexa(''+'0000500A'+'D4361F88')", "ans": "hexa('0000500AD4361F88')", "sol": "Avant : `C91011C8D4361F88`. L'instruction écrit `0000500A` à partir de l'octet n° 0 de la fenêtre (adresse `$5008`) ; les autres octets ne changent pas. Après : `0000500AD4361F88`."},
    ],
    "g86": [
        {"enonce": "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $0004FFFF   A0 = $00005000" "\n"
        "D1 = $FFFF0005   A1 = $00005008" "\n"
        "D2 = $FFFFFFFE   A2 = $00005010" "\n"
        "$005000  54 AF 18 B9 E7 21 48 C0" "\n"
        "$005008  C9 10 11 C8 D4 36 1F 88" "\n"
        "$005010  13 79 01 80 42 1A 2D 49" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVE.W $500A(PC),-(A1)`. Donner les" "\n"
        "$8$ octets de la mémoire à partir de" "\n"
        "`$5000` après l'instruction, écrits comme un seul nombre hexadécimal de" "\n"
        "$16$ chiffres.", "calc": "hexa('54AF18B9E721'+'11C8'+'')", "ans": "hexa('54AF18B9E72111C8')", "sol": "Avant : `54AF18B9E72148C0`. L'instruction écrit `11C8` à partir de l'octet n° 6 de la fenêtre (adresse `$5006`) ; les autres octets ne changent pas. Après : `54AF18B9E72111C8`."},
    ],
    "g87": [
        {"enonce": "Même état. Quelle est la valeur de A0 après `MOVE.W #52,(A0)+` ?", "calc": "hexa('5000')+2", "ans": "hexa('5002')", "sol": "La postincrémentation ajoute $2$ pour `.W` : A0 vaut" "\n"
        "`$5002`."},
    ],
    "ar91": [
        {"enonce": "Registres initiaux :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $12345600" "\n"
        "```" "\n"
        "" "\n"
        "Que contient D0 après `SUBQ.B #1,D0` ?", "calc": "(hexa('12345600')-hexa('12345600')%2**8)+(hexa('12345600')%2**8-1)%2**8", "ans": "hexa('123456FF')", "sol": "D0.B vaut $0$ : $0-1$ revient à" "\n"
        "`$FF` (emprunt, seul l'octet de poids faible change). D0 vaut" "\n"
        "`$123456FF`."},
    ],
    "ar92": [
        {"enonce": "Registres initiaux :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $12340001" "\n"
        "```" "\n"
        "" "\n"
        "Que contient D0 après `NEG.W D0` ?", "calc": "(hexa('12340001')-hexa('12340001')%2**16)+(-hexa('12340001')%2**16)%2**16", "ans": "hexa('1234FFFF')", "sol": "`NEG.W` : $0-1=-1$, soit" "\n"
        "`$FFFF` sur" "\n"
        "$16$ bits. D0 vaut" "\n"
        "`$1234FFFF`."},
    ],
    "ar93": [
        {"enonce": "Registres initiaux :" "\n"
        "" "\n"
        "```" "\n"
        "D1 = $000000F0" "\n"
        "```" "\n"
        "" "\n"
        "Que contient D1 après `NOT.B D1` ?", "calc": "(hexa('000000F0')-hexa('000000F0')%2**8)+(2**8-1-hexa('000000F0')%2**8)%2**8", "ans": "hexa('0000000F')", "sol": "`NOT.B` inverse l'octet de poids faible : `$F0` devient" "\n"
        "`$0F`. D1 vaut" "\n"
        "`$0000000F`."},
    ],
    "ar94": [
        {"enonce": "Registres initiaux :" "\n"
        "" "\n"
        "```" "\n"
        "D1 = $12345678" "\n"
        "```" "\n"
        "" "\n"
        "Que contient D1 après `ORI.B #$80,D1` ?", "calc": "hexa('12345678')|hexa('80')", "ans": "hexa('123456F8')", "sol": "Le OU avec `$80` met à" "\n"
        "$1$ le bit $7$ de l'octet de poids faible :" "\n"
        "`$78` devient" "\n"
        "`$F8`. D1 vaut" "\n"
        "`$123456F8`."},
        {"enonce": "Registres initiaux :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $0F0F1234" "\n"
        "```" "\n"
        "" "\n"
        "Que contient D0 après `EORI.L #$FFFFFFFF,D0` ?", "calc": "(hexa('0F0F1234')|hexa('FFFFFFFF'))-(hexa('0F0F1234')&hexa('FFFFFFFF'))", "ans": "hexa('F0F0EDCB')", "sol": "Le OU exclusif avec `$FFFFFFFF` inverse tous les bits : D0 vaut" "\n"
        "`$F0F0EDCB`."},
    ],
    "ar95": [
        {"enonce": "Registres initiaux :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $AAAA0007" "\n"
        "```" "\n"
        "" "\n"
        "Que contient D0 après `MULU.W #10,D0` ?", "calc": "(hexa('AAAA0007')%2**16)*10", "ans": "hexa('00000046')", "sol": r"Le mot de poids faible vaut $7$ ; $7\times10=70$, soit" "\n"
        "`$46`. Le résultat est sur" "\n"
        "$32$ bits : D0 vaut" "\n"
        "`$00000046`."},
    ],
    "ar96": [
        {"enonce": "Registres initiaux :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $00000064" "\n"
        "```" "\n"
        "" "\n"
        "Que contient D0 après `DIVU.W #7,D0` ? (`$64` vaut" "\n"
        "$100$.)", "calc": "(hexa('64')%7)*2**16+hexa('64')//7", "ans": "hexa('0002000E')", "sol": r"$100=7\times14+2$ : quotient $14$" "\n"
        "(`$000E`), reste" "\n"
        "$2$ (poids fort). D0 vaut" "\n"
        "`$0002000E`."},
    ],
    "ar97": [
        {"enonce": "Registres initiaux :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $00000010" "\n"
        "D1 = $00000005" "\n"
        "D2 = $00000001" "\n"
        "D3 = $00000002" "\n"
        "```" "\n"
        "" "\n"
        "Même programme avec D0 `$10`, D1" "\n"
        "$5$, D2 $1$, D3 $2$. Que contient D1 à la fin ?", "calc": "(5+2+(hexa('10')+1)//2**32)%2**32", "ans": "hexa('00000007')", "sol": "L'addition des mots bas ne déborde pas : X$=0$. `ADDX.L D3,D1` : $5+2+0=7$. D1 vaut" "\n"
        "`$00000007`."},
    ],
    "ar98": [
        {"enonce": "Registres initiaux :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $123456F0" "\n"
        "```" "\n"
        "" "\n"
        "Que contient D0 après `ASR.B #1,D0` ?", "calc": "(hexa('123456F0')-hexa('123456F0')%2**8)+((hexa('123456F0')%2**8>>1)|(hexa('123456F0')%2**8&128))%2**8", "ans": "hexa('123456F8')", "sol": "Décalage arithmétique vers la droite : le bit de signe est recopié. `$F0`" "\n"
        "($-16$) devient" "\n"
        "`$F8`" "\n"
        "($-8$). D0 vaut" "\n"
        "`$123456F8`."},
    ],
    "ro101": [
        {"enonce": "D1 vaut `$76543210`. On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "ROL.W #8,D1" "\n"
        "```" "\n"
        "" "\n"
        "Quelle est la valeur finale de D1 ?", "calc": "(lambda x: (x-x%65536)+((((x%65536)>>8)|((x%65536)<<8))%65536))(hexa('76543210'))", "ans": "hexa('76541032')", "sol": "On suit les $8$ chiffres hexadécimaux à chaque instruction :" "\n"
        "" "\n"
        "```asm" "\n"
        "; D1 = $76543210" "\n"
        "ROL.W #8,D1    ; D1 = $76541032" "\n"
        "```" "\n"
        "" "\n"
        "On obtient `$76541032`."},
    ],
    "ro102": [
        {"enonce": "D2 vaut `$76543210`. On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "ROR.B #4,D2" "\n"
        "```" "\n"
        "" "\n"
        "Quelle est la valeur finale de D2 ?", "calc": "(lambda x: (x-x%256)+((((x%256)>>4)|((x%256)<<4))%256))(hexa('76543210'))", "ans": "hexa('76543201')", "sol": "On suit les $8$ chiffres hexadécimaux à chaque instruction :" "\n"
        "" "\n"
        "```asm" "\n"
        "; D2 = $76543210" "\n"
        "ROR.B #4,D2    ; D2 = $76543201" "\n"
        "```" "\n"
        "" "\n"
        "On obtient `$76543201`."},
    ],
    "ro103": [
        {"enonce": "D0 vaut `$12345678`. On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "ROL.L #4,D0" "\n"
        "```" "\n"
        "" "\n"
        "Quelle est la valeur finale de D0 ?", "calc": "(lambda x: (x-x%4294967296)+((((x%4294967296)>>28)|((x%4294967296)<<4))%4294967296))(hexa('12345678'))", "ans": "hexa('23456781')", "sol": "On suit les $8$ chiffres hexadécimaux à chaque instruction :" "\n"
        "" "\n"
        "```asm" "\n"
        "; D0 = $12345678" "\n"
        "ROL.L #4,D0    ; D0 = $23456781" "\n"
        "```" "\n"
        "" "\n"
        "On obtient `$23456781`."},
    ],
    "ro104": [
        {"enonce": "D5 vaut `$87654321`. On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "SWAP D5" "\n"
        "```" "\n"
        "" "\n"
        "Quelle est la valeur finale de D5 ?", "calc": "(lambda x: (x%65536)*65536+x//65536)(hexa('87654321'))", "ans": "hexa('43218765')", "sol": "On suit les $8$ chiffres hexadécimaux à chaque instruction :" "\n"
        "" "\n"
        "```asm" "\n"
        "; D5 = $87654321" "\n"
        "SWAP D5        ; D5 = $43218765" "\n"
        "```" "\n"
        "" "\n"
        "On obtient `$43218765`."},
    ],
    "ro105": [
        {"enonce": "D4 vaut `$87654321`. On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "ROR.W #4,D4" "\n"
        "ROR.L #8,D4" "\n"
        "SWAP D4" "\n"
        "ROL.B #4,D4" "\n"
        "ROR.L #8,D4" "\n"
        "```" "\n"
        "" "\n"
        "Quelle est la valeur finale de D4 ?", "calc": "(lambda x: (x-x%4294967296)+((((x%4294967296)>>8)|((x%4294967296)<<24))%4294967296))((lambda x: (x-x%256)+((((x%256)>>4)|((x%256)<<4))%256))((lambda x: (x%65536)*65536+x//65536)((lambda x: (x-x%4294967296)+((((x%4294967296)>>8)|((x%4294967296)<<24))%4294967296))((lambda x: (x-x%65536)+((((x%65536)>>4)|((x%65536)<<12))%65536))(hexa('87654321'))))))", "ans": "hexa('78651432')", "sol": "On suit les $8$ chiffres hexadécimaux à chaque instruction :" "\n"
        "" "\n"
        "```asm" "\n"
        "; D4 = $87654321" "\n"
        "ROR.W #4,D4    ; D4 = $87651432" "\n"
        "ROR.L #8,D4    ; D4 = $32876514" "\n"
        "SWAP D4        ; D4 = $65143287" "\n"
        "ROL.B #4,D4    ; D4 = $65143278" "\n"
        "ROR.L #8,D4    ; D4 = $78651432" "\n"
        "```" "\n"
        "" "\n"
        "On obtient `$78651432`."},
    ],
    "ro106": [
        {"enonce": "D2 vaut `$76543210`. On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "SWAP D2" "\n"
        "ROR.L #4,D2" "\n"
        "SWAP D2" "\n"
        "ROR.L #8,D2" "\n"
        "ROR.W #4,D2" "\n"
        "ROL.L #8,D2" "\n"
        "```" "\n"
        "" "\n"
        "Quelle est la valeur finale de D2 ?", "calc": "(lambda x: (x-x%4294967296)+((((x%4294967296)>>24)|((x%4294967296)<<8))%4294967296))((lambda x: (x-x%65536)+((((x%65536)>>4)|((x%65536)<<12))%65536))((lambda x: (x-x%4294967296)+((((x%4294967296)>>8)|((x%4294967296)<<24))%4294967296))((lambda x: (x%65536)*65536+x//65536)((lambda x: (x-x%4294967296)+((((x%4294967296)>>4)|((x%4294967296)<<28))%4294967296))((lambda x: (x%65536)*65536+x//65536)(hexa('76543210')))))))", "ans": "hexa('07365421')", "sol": "On suit les $8$ chiffres hexadécimaux à chaque instruction :" "\n"
        "" "\n"
        "```asm" "\n"
        "; D2 = $76543210" "\n"
        "SWAP D2        ; D2 = $32107654" "\n"
        "ROR.L #4,D2    ; D2 = $43210765" "\n"
        "SWAP D2        ; D2 = $07654321" "\n"
        "ROR.L #8,D2    ; D2 = $21076543" "\n"
        "ROR.W #4,D2    ; D2 = $21073654" "\n"
        "ROL.L #8,D2    ; D2 = $07365421" "\n"
        "```" "\n"
        "" "\n"
        "On obtient `$07365421`."},
    ],
    "b111": [
        {"enonce": "Valeur initiale :" "\n"
        "" "\n"
        "```" "\n"
        "D7 = $44AA77FF" "\n"
        "```" "\n"
        "" "\n"
        "On exécute le programme :" "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVEQ.L #1,D1" "\n"
        "        TST.W   D7" "\n"
        "        BMI     NEXT" "\n"
        "        MOVEQ.L #2,D1" "\n"
        "NEXT" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D1 à la fin ?", "calc": "1 if (lambda x: x-2**16*(x//2**15))((hexa('77FF'))%2**16)<0 else 2", "ans": "hexa('00000002')", "sol": "`TST.B D7` ne regarde que D7.B (`$FF`). Son bit de poids fort est à" "\n"
        "$1$ : N$=1$, `BMI` saute à `NEXT`, `MOVEQ.L #2,D1` n'est pas exécuté : D1 vaut" "\n"
        "`$00000002`."},
    ],
    "b112": [
        {"enonce": "Valeur initiale :" "\n"
        "" "\n"
        "```" "\n"
        "D7 = $12347000" "\n"
        "```" "\n"
        "" "\n"
        "On exécute le programme :" "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVEQ.L #1,D1" "\n"
        "        CMP.W   #$7000,D7" "\n"
        "        BGT     PART2" "\n"
        "        MOVEQ.L #2,D1" "\n"
        "PART2" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D1 à la fin ?", "calc": "1 if (lambda x: x-2**16*(x//2**15))((hexa('7000'))%2**16)>28672 else 2", "ans": "hexa('00000002')", "sol": "`CMP.W #$7000,D7` compare D7.W" "\n"
        "(`$7000`, soit" "\n"
        "$28672$ en signé) à" "\n"
        "`$7000`" "\n"
        "($28672$). `BGT` est une comparaison **signée** : il n'y a pas de saut (D7.W ≤ $28672$), `MOVEQ.L #2,D1` est exécuté : D1 vaut" "\n"
        "`$00000002`."},
    ],
    "b113": [
        {"enonce": "Valeur initiale :" "\n"
        "" "\n"
        "```" "\n"
        "D7 = $23456711" "\n"
        "```" "\n"
        "" "\n"
        "On exécute le programme :" "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVEQ.L #1,D6" "\n"
        "        CMP.B   #$70,D7" "\n"
        "        BLT     QUIT" "\n"
        "        MOVEQ.L #2,D6" "\n"
        "QUIT" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D6 à la fin ?", "calc": "1 if (lambda x: x-2**8*(x//2**7))((hexa('11'))%2**8)<112 else 2", "ans": "hexa('00000001')", "sol": "`CMP.B #$70,D7` compare D7.B" "\n"
        "(`$11`, soit" "\n"
        "$17$ en signé) à" "\n"
        "`$70`" "\n"
        "($112$). `BLT` est signé : le saut est pris, `MOVEQ.L #2,D6` est sauté : D6 vaut" "\n"
        "`$00000001`."},
    ],
    "b114": [
        {"enonce": "Même programme avec une comparaison **non signée** (`BLO` au lieu de `BLT`). Valeur initiale :" "\n"
        "" "\n"
        "```" "\n"
        "D7 = $23456711" "\n"
        "```" "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVEQ.L #1,D6" "\n"
        "        CMP.B   #$70,D7" "\n"
        "        BLO     QUIT" "\n"
        "        MOVEQ.L #2,D6" "\n"
        "QUIT" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D6 à la fin ?", "calc": "1 if hexa('11')<112 else 2", "ans": "hexa('00000001')", "sol": "`BLO` est non signé : `$11` vaut" "\n"
        "$17$ et" "\n"
        "`$70` vaut" "\n"
        "$112$. Le saut est pris, D6 vaut" "\n"
        "`$00000001`. Avec D7.B" "\n"
        "`$89`, `BLT` (signé :" "\n"
        "$-119<112$) saute alors que `BLO` (non signé : $137<112$ est faux) ne saute pas."},
    ],
    "b115": [
        {"enonce": "Valeur initiale :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $FFFFFFFF" "\n"
        "```" "\n"
        "" "\n"
        "On exécute le programme :" "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVEQ.L #1,D5" "\n"
        "        CMP.L   #1,D0" "\n"
        "        BGT     NEXT" "\n"
        "        MOVEQ.L #2,D5" "\n"
        "NEXT" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D5 à la fin ?", "calc": "1 if (lambda x: x-2**32*(x//2**31))((hexa('FFFFFFFF'))%2**32)>1 else 2", "ans": "hexa('00000002')", "sol": "`BGT` est signé : D0 vaut $-1$ et $-1>1$ est faux, pas de saut. `MOVEQ.L #2,D5` est exécuté : D5 vaut" "\n"
        "`$00000002`."},
    ],
    "b116": [
        {"enonce": "On exécute le programme suivant :" "\n"
        "" "\n"
        "```asm" "\n"
        "VALUE   EQU     -5" "\n"
        "        MOVE.B  #VALUE,D1" "\n"
        "        TST.B   D1" "\n"
        "        BNE     NEXT1" "\n"
        "        MOVE.L  #200,D0" "\n"
        "        BRA     QUIT" "\n"
        "NEXT1   BMI     NEXT3" "\n"
        "        CMP.B   #$61,D1" "\n"
        "        BLT     NEXT2" "\n"
        "        MOVE.L  #400,D0" "\n"
        "        BRA     QUIT" "\n"
        "NEXT2   MOVE.L  #600,D0" "\n"
        "        BRA     QUIT" "\n"
        "NEXT3   MOVE.L  #800,D0" "\n"
        "QUIT" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D0 à la fin ?", "calc": "200 if -5==0 else (800 if -5<0 else (400 if -5>=97 else 600))", "ans": "800", "sol": "`TST.B D1` met à jour N et Z. D1.B vaut -5, négatif : `BMI NEXT3` saute : D0 vaut $800$."},
    ],
    "b117": [
        {"enonce": "On exécute le programme suivant :" "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVE.L  #7,D0" "\n"
        "        TST.L   D0" "\n"
        "        BPL     QUIT" "\n"
        "        NEG.L   D0" "\n"
        "QUIT" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D0 à la fin (en décimal, valeur signée) ?", "calc": "abs(7)", "ans": "7", "sol": "D0 vaut $7$, positif : N$=0$, `BPL` saute à `QUIT`. D0 vaut $7$."},
        {"enonce": "On exécute le programme suivant :" "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVE.L  #-250,D0" "\n"
        "        TST.L   D0" "\n"
        "        BPL     QUIT" "\n"
        "        NEG.L   D0" "\n"
        "QUIT" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D0 à la fin (en décimal, valeur signée) ?", "calc": "abs(-250)", "ans": "250", "sol": "D0 vaut $-250$, négatif : N$=1$, `BPL` ne saute pas et `NEG.L D0` calcule $0-D0$. D0 vaut $250$."},
    ],
    "l121": [
        {"enonce": "On exécute le programme :" "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVE.L  #518,D0" "\n"
        "        CLR.L   D2" "\n"
        "LOOP    ADDQ.L  #1,D2" "\n"
        "        SUBQ.B  #2,D0" "\n"
        "        BNE     LOOP" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D2 à la fin (en hexadécimal) ?", "calc": "(518%256 or 256)//2", "ans": "hexa('00000003')", "sol": "Seul l'octet de poids faible de D0 est décrémenté et testé. D0.B vaut $6$ (518 modulo $256$) et le pas est $2$ : la boucle fait $3$ tours. D2 vaut" "\n"
        "`$00000003`."},
        {"enonce": "On exécute le programme :" "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVE.L  #200,D0" "\n"
        "        CLR.L   D2" "\n"
        "LOOP    ADDQ.L  #1,D2" "\n"
        "        SUBQ.B  #4,D0" "\n"
        "        BNE     LOOP" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D2 à la fin (en hexadécimal) ?", "calc": "(200%256 or 256)//4", "ans": "hexa('00000032')", "sol": "Seul l'octet de poids faible de D0 est décrémenté et testé. D0.B vaut $200$ (200 modulo $256$) et le pas est $4$ : la boucle fait $50$ tours. D2 vaut" "\n"
        "`$00000032`."},
    ],
    "l122": [
        {"enonce": "On exécute le programme :" "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVE.L  #$11112222,D0" "\n"
        "        CLR.L   D2" "\n"
        "LOOP    ADDQ.L  #1,D2" "\n"
        "        SUBQ.W  #2,D0" "\n"
        "        BNE     LOOP" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D2 à la fin ? (donner la valeur de D2)", "calc": "(hexa('11112222')%65536)//2", "ans": "hexa('00001111')", "sol": "`SUBQ.W #2,D0` agit sur D0.W et le pas vaut $2$ : D0.W atteint $0$ après $4369$ tours. D2 vaut" "\n"
        "`$00001111`."},
    ],
    "l123": [
        {"enonce": "On exécute le programme :" "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVE.L  #$77777777,D0" "\n"
        "        CLR.L   D3" "\n"
        "LOOP    ADDQ.L  #1,D3" "\n"
        "        DBRA    D0,LOOP" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D3 à la fin ?", "calc": "hexa('77777777')%65536+1", "ans": "hexa('00007778')", "sol": "`DBRA D0,LOOP` ne regarde que D0.W. Il décrémente D0.W et reboucle tant que le résultat n'est pas `$FFFF` : la boucle fait D0.W" "\n"
        "$+1$ tours. Ici D0.W vaut" "\n"
        "`$7777`, donc" "\n"
        "$30584$ tours : D3 vaut" "\n"
        "`$00007778`."},
        {"enonce": "On exécute le programme :" "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVE.L  #$12345678,D0" "\n"
        "        CLR.L   D3" "\n"
        "LOOP    ADDQ.L  #1,D3" "\n"
        "        DBRA    D0,LOOP" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D3 à la fin ?", "calc": "hexa('12345678')%65536+1", "ans": "hexa('00005679')", "sol": "`DBRA D0,LOOP` ne regarde que D0.W. Il décrémente D0.W et reboucle tant que le résultat n'est pas `$FFFF` : la boucle fait D0.W" "\n"
        "$+1$ tours. Ici D0.W vaut" "\n"
        "`$5678`, donc" "\n"
        "$22137$ tours : D3 vaut" "\n"
        "`$00005679`."},
    ],
    "l124": [
        {"enonce": "On exécute le programme :" "\n"
        "" "\n"
        "```asm" "\n"
        "        CLR.L   D4" "\n"
        "        MOVEQ.L #5,D0" "\n"
        "LOOP    ADDQ.L  #1,D4" "\n"
        "        ADDQ.L  #1,D0" "\n"
        "        CMPI.L  #47,D0" "\n"
        "        BNE     LOOP" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D4 à la fin ?", "calc": "47-5", "ans": "hexa('0000002A')", "sol": "D0 part de $5$ et augmente de $1$ à chaque tour jusqu'à valoir $47$ : $42$ tours. D4 vaut" "\n"
        "`$0000002A`."},
    ],
    "l125": [
        {"enonce": "On exécute le programme :" "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVE.L  #$FF00,D0" "\n"
        "        CLR.L   D2" "\n"
        "LOOP    ADDQ.L  #1,D2" "\n"
        "        SUBQ.B  #1,D0" "\n"
        "        BNE     LOOP" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D2 à la fin ?", "calc": "(hexa('FF00')%256 or 256)", "ans": "hexa('00000100')", "sol": "D0.B vaut $0$. Le premier `SUBQ.B #1,D0` le fait passer à" "\n"
        "`$FF`, qui n'est pas nul : la boucle continue jusqu'à ce que D0.B retombe à" "\n"
        "$0$, soit $256$ tours. D2 vaut" "\n"
        "`$00000100`."},
    ],
    "l126": [
        {"enonce": "On exécute le programme :" "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVE.W  #$4321,D0" "\n"
        "        CLR.L   D3" "\n"
        "LOOP    ADDQ.L  #1,D3" "\n"
        "        SUBQ.B  #1,D0" "\n"
        "        BNE     LOOP" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D3 à la fin ?", "calc": "(hexa('4321')%256 or 256)", "ans": "hexa('00000021')", "sol": "`SUBQ.B` ne touche que D0.B : `$255` a pour octet de poids faible" "\n"
        "`$21`. La boucle fait autant de tours que cet octet" "\n"
        "($33$) : D3 vaut" "\n"
        "`$00000021`."},
    ],
    "l127": [
        {"enonce": "On exécute le programme :" "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVE.W  #0,D0" "\n"
        "        CLR.L   D4" "\n"
        "LOOP    ADDQ.L  #1,D4" "\n"
        "        DBRA    D0,LOOP" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D4 à la fin ?", "calc": "0+1", "ans": "hexa('00000001')", "sol": "D0.W vaut `$100` : `DBRA` fait D0.W" "\n"
        "$+1$ tours, soit $1$ tours. D4 vaut" "\n"
        "`$00000001`."},
    ],
    "p131": [
        {"enonce": "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $00000005   A7 = $00F00000" "\n"
        "D1 = $00000006" "\n"
        "```" "\n"
        "" "\n"
        "On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVE.L  #1,-(A7)" "\n"
        "        MOVE.L  D0,-(A7)" "\n"
        "        MOVE.W  D1,-(A7)" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut A7 à la fin ?", "calc": "hexa('F00000')-4-4-2", "ans": "hexa('EFFFF6')", "sol": "$4+4+2=10$ octets : A7 vaut" "\n"
        "`$EFFFF6`."},
    ],
    "p132": [
        {"enonce": "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $11112222   A7 = $00F00006" "\n"
        "D1 = $AAAABBBB" "\n"
        "D2 = $00000000" "\n"
        "D3 = $00000000" "\n"
        "```" "\n"
        "" "\n"
        "Même programme. Que vaut D3 à la fin ?", "calc": "hexa('42')", "ans": "hexa('00000042')", "sol": "D3 reçoit en dernier le mot `$0042`, empilé en premier : D3 vaut" "\n"
        "`$00000042`."},
    ],
    "p133": [
        {"enonce": "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "A7 = $00F00000" "\n"
        "```" "\n"
        "" "\n"
        "On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "        MOVEM.L D0-D7,-(A7)" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut A7 après l'instruction ?", "calc": "hexa('F00000')-8*4", "ans": "hexa('EFFFE0')", "sol": "$8$ registres de $4$ octets : $32$ octets, A7 vaut" "\n"
        "`$EFFFE0`."},
    ],
    "p134": [
        {"enonce": "État initial identique. On exécute `MOVEM.L D1-D3/A4/A5,-(A7)` puis `MOVE.L 16(A7),D0`. Que vaut D0 ?", "calc": "hexa('55555555')", "ans": "hexa('55555555')", "sol": r"A5 a été empilé en premier : il est le plus profond, à `16(A7)` (A5 est à $4\times4=16$ octets au-dessus du sommet). D0 vaut" "\n"
        "`$55555555`."},
    ],
    "p135": [
        {"enonce": "A7 vaut `$F00000`. Que vaut A7 après `MOVEM.L (A7)+,D0-D2/A0` ?", "calc": "hexa('F00000')+4*4", "ans": "hexa('00F00010')", "sol": "$4$ registres : $16$ octets," "\n"
        "`$F00010`."},
    ],
    "p136": [
        {"enonce": "A7 vaut `$F00000` au début de `Main`. Même programme, mais `Sub2` commence par `MOVEM.L D0-D7/A0-A6,-(A7)`" "\n"
        "($15$ registres). Que vaut A7 quand le processeur atteint `ILLEGAL` ?", "calc": "hexa('F00000')-4-4-15*4", "ans": "hexa('EFFFBC')", "sol": r"$4+4+15\times4=68$ octets : A7 vaut" "\n"
        "`$EFFFBC`."},
    ],
    "p137": [
        {"enonce": "A7 vaut `$F0FFFC` juste avant un `JSR Sub`. Que vaut A7 juste après le `JSR` ?", "calc": "hexa('F0FFFC')-4", "ans": "hexa('F0FFF8')", "sol": "`JSR` empile l'adresse de retour : A7 diminue de $4$ et vaut" "\n"
        "`$F0FFF8`."},
    ],
    "p138": [
        {"enonce": "A7 vaut `$F00000`. Même programme avec `MOVEQ.L #10,D0`, `MOVEQ.L #20,D0` et `MOVEQ.L #30,D0` à la place de" "\n"
        "$5$, $7$ et $3$. Que vaut D0 à la fin ?", "calc": "10+20+30", "ans": "60", "sol": "$10$ est empilé, $20$ y est ajouté ($30$), puis $30+30=60$."},
    ],
    "sp141": [
        {"enonce": "Le sous-programme `GetMin` renvoie dans D0 la plus petite valeur **signée** de D1 et D2 :" "\n"
        "" "\n"
        "```asm" "\n"
        "GetMin  CMP.L   D1,D2" "\n"
        "        BLE     D2MIN" "\n"
        "D1MIN   MOVE.L  D1,D0" "\n"
        "        RTS" "\n"
        "D2MIN   MOVE.L  D2,D0" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "Main    MOVE.L  #30,D1" "\n"
        "        MOVE.L  #16,D2" "\n"
        "        JSR     GetMin" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D0 après l'appel (en hexadécimal sur $32$ bits) ?", "calc": "min(30,16)%2**32", "ans": "hexa('00000010')", "sol": r"`CMP.L D1,D2` calcule D2 $-$ D1 ; `BLE` (signé) saute si D2 $\le$ D1. Avec D1 $=30$ et D2 $=16$ : D2 est inférieur ou égal à D1, on copie D2. Après `RTS`, le programme continue après le `JSR`. D0 vaut" "\n"
        "`$00000010`."},
        {"enonce": "Le sous-programme `GetMin` renvoie dans D0 la plus petite valeur **signée** de D1 et D2 :" "\n"
        "" "\n"
        "```asm" "\n"
        "GetMin  CMP.L   D1,D2" "\n"
        "        BLE     D2MIN" "\n"
        "D1MIN   MOVE.L  D1,D0" "\n"
        "        RTS" "\n"
        "D2MIN   MOVE.L  D2,D0" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "Main    MOVE.L  #-3,D1" "\n"
        "        MOVE.L  #5,D2" "\n"
        "        JSR     GetMin" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D0 après l'appel (en hexadécimal sur $32$ bits) ?", "calc": "min(-3,5)%2**32", "ans": "hexa('FFFFFFFD')", "sol": r"`CMP.L D1,D2` calcule D2 $-$ D1 ; `BLE` (signé) saute si D2 $\le$ D1. Avec D1 $=-3$ et D2 $=5$ : D2 est supérieur à D1, on copie D1. Après `RTS`, le programme continue après le `JSR`. D0 vaut" "\n"
        "`$FFFFFFFD`."},
    ],
    "sp142": [
        {"enonce": "Le sous-programme `Double` double D1 :" "\n"
        "" "\n"
        "```asm" "\n"
        "Double  ADD.L   D1,D1" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "Main    MOVE.L  #5,D1" "\n"
        "        BSR     Double" "\n"
        "        BSR     Double" "\n"
        "        BSR     Double" "\n"
        "        BSR     Double" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D1 à la fin (en décimal) ?", "calc": "5*2**4", "ans": "80", "sol": r"Chaque `BSR Double` double D1 puis `RTS` revient à l'instruction suivante : $5\times2^4=80$."},
    ],
    "sp143": [
        {"enonce": "Même appel, mais le sous-programme est :" "\n"
        "" "\n"
        "```asm" "\n"
        "Calc    MOVE.L  #99,D1" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVE.L #10,D1` puis `BSR Calc`. Que vaut D1 après le retour ?", "calc": "99", "ans": "99", "sol": "Sans sauvegarde, `MOVE.L #99,D1` écrase la valeur de l'appelant : D1 vaut $99$."},
    ],
    "ch151": [
        {"enonce": "Le sous-programme `StrLen` renvoie dans D0 la longueur d'une chaîne (A0 pointe sur son premier caractère) :" "\n"
        "" "\n"
        "```asm" "\n"
        "StrLen  CLR.L   D0" "\n"
        r"\loop   TST.B   (A0)+" "\n"
        r"        BEQ     \quit" "\n"
        "        ADDQ.L  #1,D0" "\n"
        r"        BRA     \loop" "\n"
        r"\quit   RTS" "\n"
        "```" "\n"
        "" "\n"
        "On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "        ORG     $2000" "\n"
        'TEXT    DC.B    "Hello World",0' "\n"
        "" "\n"
        "Main    LEA     TEXT,A0" "\n"
        "        JSR     StrLen" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D0 à la fin (en décimal) ?", "calc": "len('Hello World')", "ans": "11", "sol": "`TST.B (A0)+` teste l'octet pointé et fait avancer A0 ; `BEQ` sort sur l'octet nul sans compter. Chaque autre caractère incrémente D0. La chaîne contient $11$ caractères (sans l'octet nul) : D0 vaut $11$."},
        {"enonce": "Le sous-programme `StrLen` renvoie dans D0 la longueur d'une chaîne (A0 pointe sur son premier caractère) :" "\n"
        "" "\n"
        "```asm" "\n"
        "StrLen  CLR.L   D0" "\n"
        r"\loop   TST.B   (A0)+" "\n"
        r"        BEQ     \quit" "\n"
        "        ADDQ.L  #1,D0" "\n"
        r"        BRA     \loop" "\n"
        r"\quit   RTS" "\n"
        "```" "\n"
        "" "\n"
        "On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "        ORG     $2000" "\n"
        'TEXT    DC.B    "a",0' "\n"
        "" "\n"
        "Main    LEA     TEXT,A0" "\n"
        "        JSR     StrLen" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D0 à la fin (en décimal) ?", "calc": "len('a')", "ans": "1", "sol": "`TST.B (A0)+` teste l'octet pointé et fait avancer A0 ; `BEQ` sort sur l'octet nul sans compter. Chaque autre caractère incrémente D0. La chaîne contient $1$ caractères (sans l'octet nul) : D0 vaut $1$."},
    ],
    "ch152": [
        {"enonce": "Le sous-programme `SpaceCount` compte les espaces d'une chaîne :" "\n"
        "" "\n"
        "```asm" "\n"
        "SpaceCount" "\n"
        "        CLR.L   D0" "\n"
        r"\loop   MOVE.B  (A0)+,D1" "\n"
        r"        BEQ     \quit" "\n"
        "        CMP.B   #' ',D1" "\n"
        r"        BNE     \loop" "\n"
        "        ADDQ.L  #1,D0" "\n"
        r"        BRA     \loop" "\n"
        r"\quit   RTS" "\n"
        "```" "\n"
        "" "\n"
        "On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "        ORG     $2000" "\n"
        'TEXT    DC.B    "Un deux trois quatre",0' "\n"
        "" "\n"
        "Main    LEA     TEXT,A0" "\n"
        "        JSR     SpaceCount" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D0 à la fin (en décimal) ?", "calc": "'Un deux trois quatre'.count(' ')", "ans": "3", "sol": "`MOVE.B (A0)+,D1` met Z à $1$ sur l'octet nul (fin). Chaque caractère égal à `' '` ($32$) incrémente D0. Il y a $3$ espaces."},
        {"enonce": "Le sous-programme `SpaceCount` compte les espaces d'une chaîne :" "\n"
        "" "\n"
        "```asm" "\n"
        "SpaceCount" "\n"
        "        CLR.L   D0" "\n"
        r"\loop   MOVE.B  (A0)+,D1" "\n"
        r"        BEQ     \quit" "\n"
        "        CMP.B   #' ',D1" "\n"
        r"        BNE     \loop" "\n"
        "        ADDQ.L  #1,D0" "\n"
        r"        BRA     \loop" "\n"
        r"\quit   RTS" "\n"
        "```" "\n"
        "" "\n"
        "On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "        ORG     $2000" "\n"
        'TEXT    DC.B    "AAA",0' "\n"
        "" "\n"
        "Main    LEA     TEXT,A0" "\n"
        "        JSR     SpaceCount" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D0 à la fin (en décimal) ?", "calc": "'AAA'.count(' ')", "ans": "0", "sol": "`MOVE.B (A0)+,D1` met Z à $1$ sur l'octet nul (fin). Chaque caractère égal à `' '` ($32$) incrémente D0. Il y a $0$ espaces."},
    ],
    "ch153": [
        {"enonce": "Le sous-programme `LowerCount` compte les minuscules (`'a'` à `'z'`) :" "\n"
        "" "\n"
        "```asm" "\n"
        "LowerCount" "\n"
        "        MOVEM.L D1/A0,-(A7)" "\n"
        "        CLR.L   D0" "\n"
        r"\loop   MOVE.B  (A0)+,D1" "\n"
        r"        BEQ     \quit" "\n"
        "        CMP.B   #'a',D1" "\n"
        r"        BLO     \loop" "\n"
        "        CMP.B   #'z',D1" "\n"
        r"        BHI     \loop" "\n"
        "        ADDQ.L  #1,D0" "\n"
        r"        BRA     \loop" "\n"
        r"\quit   MOVEM.L (A7)+,D1/A0" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "        ORG     $2000" "\n"
        'TEXT    DC.B    "Bonjour Le Monde 2026",0' "\n"
        "" "\n"
        "Main    LEA     TEXT,A0" "\n"
        "        JSR     LowerCount" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D0 à la fin (en décimal) ?", "calc": "len([i for i in 'Bonjour Le Monde 2026' if 'a'<=i<='z'])", "ans": "11", "sol": "Un caractère est une minuscule si son code ASCII est entre `'a'` ($97$) et `'z'` ($122$) : `BLO` élimine les codes trop petits, `BHI` les trop grands (comparaisons non signées). Il y a $11$ minuscules. Le sous-programme sauvegarde D1 et A0."},
        {"enonce": "Le sous-programme `LowerCount` compte les minuscules (`'a'` à `'z'`) :" "\n"
        "" "\n"
        "```asm" "\n"
        "LowerCount" "\n"
        "        MOVEM.L D1/A0,-(A7)" "\n"
        "        CLR.L   D0" "\n"
        r"\loop   MOVE.B  (A0)+,D1" "\n"
        r"        BEQ     \quit" "\n"
        "        CMP.B   #'a',D1" "\n"
        r"        BLO     \loop" "\n"
        "        CMP.B   #'z',D1" "\n"
        r"        BHI     \loop" "\n"
        "        ADDQ.L  #1,D0" "\n"
        r"        BRA     \loop" "\n"
        r"\quit   MOVEM.L (A7)+,D1/A0" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "        ORG     $2000" "\n"
        'TEXT    DC.B    "ABC 123",0' "\n"
        "" "\n"
        "Main    LEA     TEXT,A0" "\n"
        "        JSR     LowerCount" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D0 à la fin (en décimal) ?", "calc": "len([i for i in 'ABC 123' if 'a'<=i<='z'])", "ans": "0", "sol": "Un caractère est une minuscule si son code ASCII est entre `'a'` ($97$) et `'z'` ($122$) : `BLO` élimine les codes trop petits, `BHI` les trop grands (comparaisons non signées). Il y a $0$ minuscules. Le sous-programme sauvegarde D1 et A0."},
    ],
    "ch154": [
        {"enonce": "Le sous-programme `GetSum` additionne les chiffres d'une chaîne qui ne contient que des chiffres :" "\n"
        "" "\n"
        "```asm" "\n"
        "GetSum  MOVEM.L A0/D1,-(A7)" "\n"
        "        CLR.L   D0" "\n"
        "        CLR.L   D1" "\n"
        r"\loop   MOVE.B  (A0)+,D1" "\n"
        r"        BEQ     \quit" "\n"
        "        SUB.B   #'0',D1" "\n"
        "        ADD.L   D1,D0" "\n"
        r"        BRA     \loop" "\n"
        r"\quit   MOVEM.L (A7)+,A0/D1" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "        ORG     $2000" "\n"
        'TEXT    DC.B    "9876",0' "\n"
        "" "\n"
        "Main    LEA     TEXT,A0" "\n"
        "        JSR     GetSum" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D0 à la fin (en décimal) ?", "calc": "sum(ord(i)-48 for i in '9876')", "ans": "30", "sol": "Pour chaque caractère on soustrait `'0'` ($48$) pour obtenir sa valeur, puis on l'ajoute à D0. Ici $9+8+7+6=30$."},
        {"enonce": "Le sous-programme `GetSum` additionne les chiffres d'une chaîne qui ne contient que des chiffres :" "\n"
        "" "\n"
        "```asm" "\n"
        "GetSum  MOVEM.L A0/D1,-(A7)" "\n"
        "        CLR.L   D0" "\n"
        "        CLR.L   D1" "\n"
        r"\loop   MOVE.B  (A0)+,D1" "\n"
        r"        BEQ     \quit" "\n"
        "        SUB.B   #'0',D1" "\n"
        "        ADD.L   D1,D0" "\n"
        r"        BRA     \loop" "\n"
        r"\quit   MOVEM.L (A7)+,A0/D1" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "        ORG     $2000" "\n"
        'TEXT    DC.B    "1000001",0' "\n"
        "" "\n"
        "Main    LEA     TEXT,A0" "\n"
        "        JSR     GetSum" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D0 à la fin (en décimal) ?", "calc": "sum(ord(i)-48 for i in '1000001')", "ans": "2", "sol": "Pour chaque caractère on soustrait `'0'` ($48$) pour obtenir sa valeur, puis on l'ajoute à D0. Ici $1+0+0+0+0+0+1=2$."},
    ],
    "ch155": [
        {"enonce": r"Le sous-programme `Atoui` convertit une chaîne de chiffres en entier : $r\leftarrow10r+\text{chiffre}$." "\n"
        "" "\n"
        "```asm" "\n"
        "Atoui   MOVEM.L D1/A0,-(A7)" "\n"
        "        CLR.L   D0" "\n"
        "        CLR.L   D1" "\n"
        r"\loop   MOVE.B  (A0)+,D1" "\n"
        r"        BEQ     \quit" "\n"
        "        SUBI.B  #'0',D1" "\n"
        "        MULU.W  #10,D0" "\n"
        "        ADD.L   D1,D0" "\n"
        r"        BRA     \loop" "\n"
        r"\quit   MOVEM.L (A7)+,D1/A0" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "        ORG     $2000" "\n"
        'TEXT    DC.B    "407",0' "\n"
        "" "\n"
        "Main    LEA     TEXT,A0" "\n"
        "        JSR     Atoui" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D0 à la fin (en décimal) ?", "calc": "Integer('407')", "ans": "407", "sol": r"On part de D0 $=0$ ; pour chaque chiffre : D0 $\leftarrow D0\times10+\text{chiffre}$. Pour `407` : $407$."},
        {"enonce": r"Le sous-programme `Atoui` convertit une chaîne de chiffres en entier : $r\leftarrow10r+\text{chiffre}$." "\n"
        "" "\n"
        "```asm" "\n"
        "Atoui   MOVEM.L D1/A0,-(A7)" "\n"
        "        CLR.L   D0" "\n"
        "        CLR.L   D1" "\n"
        r"\loop   MOVE.B  (A0)+,D1" "\n"
        r"        BEQ     \quit" "\n"
        "        SUBI.B  #'0',D1" "\n"
        "        MULU.W  #10,D0" "\n"
        "        ADD.L   D1,D0" "\n"
        r"        BRA     \loop" "\n"
        r"\quit   MOVEM.L (A7)+,D1/A0" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "        ORG     $2000" "\n"
        'TEXT    DC.B    "30000",0' "\n"
        "" "\n"
        "Main    LEA     TEXT,A0" "\n"
        "        JSR     Atoui" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D0 à la fin (en décimal) ?", "calc": "Integer('30000')", "ans": "30000", "sol": r"On part de D0 $=0$ ; pour chaque chiffre : D0 $\leftarrow D0\times10+\text{chiffre}$. Pour `30000` : $30000$."},
    ],
    "ch156": [
        {"enonce": "Les sous-programmes `IsBlank` (D0 vaut $0$ si le caractère D1.B est blanc : espace ou tabulation) et `BlankCount` (nombre de caractères blancs d'une chaîne) :" "\n"
        "" "\n"
        "```asm" "\n"
        "IsBlank CMPI.B  #' ',D1" "\n"
        r"        BEQ     \blank" "\n"
        "        CMPI.B  #9,D1" "\n"
        r"        BEQ     \blank" "\n"
        "        MOVEQ.L #1,D0" "\n"
        "        RTS" "\n"
        r"\blank  MOVEQ.L #0,D0" "\n"
        "        RTS" "\n"
        "BlankCount" "\n"
        "        MOVEM.L D1/D2/A0,-(A7)" "\n"
        "        CLR.L   D2" "\n"
        r"\loop   MOVE.B  (A0)+,D1" "\n"
        r"        BEQ     \quit" "\n"
        "        JSR     IsBlank" "\n"
        "        TST.L   D0" "\n"
        r"        BNE     \loop" "\n"
        "        ADDQ.L  #1,D2" "\n"
        r"        BRA     \loop" "\n"
        r"\quit   MOVE.L  D2,D0" "\n"
        "        MOVEM.L (A7)+,D1/D2/A0" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "        ORG     $2000" "\n"
        'TEXT    DC.B    "Hello World",0' "\n"
        "" "\n"
        "Main    LEA     TEXT,A0" "\n"
        "        JSR     BlankCount" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D0 à la fin (en décimal) ?", "calc": "'Hello World'.count(' ')+'Hello World'.count(chr(9))", "ans": "1", "sol": "`IsBlank` renvoie $0$ pour l'espace ($32$) et la tabulation ($9$), $1$ sinon. `BlankCount` compte les caractères pour lesquels `IsBlank` renvoie $0$. La chaîne contient $1$ caractères blancs (la tabulation et les espaces comptent)."},
        {"enonce": "Les sous-programmes `IsBlank` (D0 vaut $0$ si le caractère D1.B est blanc : espace ou tabulation) et `BlankCount` (nombre de caractères blancs d'une chaîne) :" "\n"
        "" "\n"
        "```asm" "\n"
        "IsBlank CMPI.B  #' ',D1" "\n"
        r"        BEQ     \blank" "\n"
        "        CMPI.B  #9,D1" "\n"
        r"        BEQ     \blank" "\n"
        "        MOVEQ.L #1,D0" "\n"
        "        RTS" "\n"
        r"\blank  MOVEQ.L #0,D0" "\n"
        "        RTS" "\n"
        "BlankCount" "\n"
        "        MOVEM.L D1/D2/A0,-(A7)" "\n"
        "        CLR.L   D2" "\n"
        r"\loop   MOVE.B  (A0)+,D1" "\n"
        r"        BEQ     \quit" "\n"
        "        JSR     IsBlank" "\n"
        "        TST.L   D0" "\n"
        r"        BNE     \loop" "\n"
        "        ADDQ.L  #1,D2" "\n"
        r"        BRA     \loop" "\n"
        r"\quit   MOVE.L  D2,D0" "\n"
        "        MOVEM.L (A7)+,D1/D2/A0" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "        ORG     $2000" "\n"
        'TEXT    DC.B    9,9," x",0' "\n"
        "" "\n"
        "Main    LEA     TEXT,A0" "\n"
        "        JSR     BlankCount" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D0 à la fin (en décimal) ?", "calc": "'		 x'.count(' ')+'		 x'.count(chr(9))", "ans": "3", "sol": "`IsBlank` renvoie $0$ pour l'espace ($32$) et la tabulation ($9$), $1$ sinon. `BlankCount` compte les caractères pour lesquels `IsBlank` renvoie $0$. La chaîne contient $3$ caractères blancs (la tabulation et les espaces comptent)."},
    ],
    "ch157": [
        {"enonce": "Quel est le code ASCII (en hexadécimal) du caractère `'z'` ?", "calc": "ord('z')", "ans": "hexa('7A')", "sol": "`'z'` a pour code $122$, soit" "\n"
        "`$7A`."},
    ],
    "ch158": [
        {"enonce": "D1.B contient le code ASCII du caractère `'3'`. Que contient D1.B après `SUB.B #'0',D1` (décimal) ?", "calc": "ord('3')-ord('0')", "ans": "3", "sol": "$51-48=3$."},
    ],
    "x1a": [
        {"enonce": "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $FFFFFFFB   A0 = $00005000" "\n"
        "D1 = $00000008   A1 = $00005008" "\n"
        "D2 = $4444FFFE   A2 = $00005010" "\n"
        "$005000  54 AF 18 B9 E7 21 48 C0" "\n"
        "$005008  C9 10 11 C8 D4 36 1F 88" "\n"
        "$005010  13 79 01 80 42 1A 2D 49" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVE.L #$5006,-(A2)`. Donner les" "\n"
        "$8$ octets de la mémoire à partir de" "\n"
        "`$5008` après l'instruction, écrits comme un seul nombre hexadécimal de" "\n"
        "$16$ chiffres.", "calc": "hexa('C91011C8'+'00005006'+'')", "ans": "hexa('C91011C800005006')", "sol": "Avant : `C91011C8D4361F88`. L'instruction écrit `00005006` à partir de l'octet n° 4 de la fenêtre (adresse `$500C`) ; les autres octets ne changent pas. Après : `C91011C800005006`."},
    ],
    "x1b": [
        {"enonce": "Mêmes valeurs initiales (A2 `$5010`). Quelle est la valeur de A2 après `MOVE.W #5,-(A2)` ?", "calc": "hexa('5010')-2", "ans": "hexa('500E')", "sol": "`.W` : A2 diminue de $2$ :" "\n"
        "`$500E`."},
    ],
    "x1c": [
        {"enonce": "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $FFFFFFFB   A0 = $00005000" "\n"
        "D1 = $00000008   A1 = $00005008" "\n"
        "D2 = $4444FFFE   A2 = $00005010" "\n"
        "$005000  54 AF 18 B9 E7 21 48 C0" "\n"
        "$005008  C9 10 11 C8 D4 36 1F 88" "\n"
        "$005010  13 79 01 80 42 1A 2D 49" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVE.W $500A,4(A1)`. Donner les" "\n"
        "$8$ octets de la mémoire à partir de" "\n"
        "`$5008` après l'instruction, écrits comme un seul nombre hexadécimal de" "\n"
        "$16$ chiffres.", "calc": "hexa('C91011C8'+'11C8'+'1F88')", "ans": "hexa('C91011C811C81F88')", "sol": "Avant : `C91011C8D4361F88`. L'instruction écrit `11C8` à partir de l'octet n° 4 de la fenêtre (adresse `$500C`) ; les autres octets ne changent pas. Après : `C91011C811C81F88`."},
    ],
    "x1d": [
        {"enonce": "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $FFFFFFFB   A0 = $00005000" "\n"
        "D1 = $00000008   A1 = $00005008" "\n"
        "D2 = $4444FFFE   A2 = $00005010" "\n"
        "$005000  54 AF 18 B9 E7 21 48 C0" "\n"
        "$005008  C9 10 11 C8 D4 36 1F 88" "\n"
        "$005010  13 79 01 80 42 1A 2D 49" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVE.B #7,(A0)+`. Donner les $8$ octets de la mémoire à partir de" "\n"
        "`$5000` après l'instruction, écrits comme un seul nombre hexadécimal de" "\n"
        "$16$ chiffres.", "calc": "hexa(''+'07'+'AF18B9E72148C0')", "ans": "hexa('07AF18B9E72148C0')", "sol": "Avant : `54AF18B9E72148C0`. L'instruction écrit `07` à partir de l'octet n° 0 de la fenêtre (adresse `$5000`) ; les autres octets ne changent pas. Après : `07AF18B9E72148C0`."},
    ],
    "x1e": [
        {"enonce": "Mêmes valeurs initiales (A0 `$5000`). Quelle est la valeur de A0 après `MOVE.L D1,(A0)+` ?", "calc": "hexa('5000')+4", "ans": "hexa('5004')", "sol": "`.L` : A0 augmente de $4$ :" "\n"
        "`$5004`."},
    ],
    "x1f": [
        {"enonce": "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $FFFFFFFB   A0 = $00005000" "\n"
        "D1 = $00000008   A1 = $00005008" "\n"
        "D2 = $4444FFFE   A2 = $00005010" "\n"
        "$005000  54 AF 18 B9 E7 21 48 C0" "\n"
        "$005008  C9 10 11 C8 D4 36 1F 88" "\n"
        "$005010  13 79 01 80 42 1A 2D 49" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVE.B 3(A1),-2(A1,D1.W)`. Donner les $8$ octets de la mémoire à partir de" "\n"
        "`$5008` après l'instruction, écrits comme un seul nombre hexadécimal de" "\n"
        "$16$ chiffres.", "calc": "hexa('C91011C8D436'+'C8'+'88')", "ans": "hexa('C91011C8D436C888')", "sol": "Avant : `C91011C8D4361F88`. L'instruction écrit `C8` à partir de l'octet n° 6 de la fenêtre (adresse `$500E`) ; les autres octets ne changent pas. Après : `C91011C8D436C888`."},
    ],
    "x2a": [
        {"enonce": "On additionne sur 8 bits : `$7F + $7E` (par exemple avec `ADD.B`). Donner le résultat (en hexadécimal, sur 8 bits).", "calc": "(hexa('7F')+hexa('7E'))%2**8", "ans": "hexa('FD')", "sol": "`$7F + $7E = $FD` ; sur 8 bits on garde" "\n"
        "`$FD`."},
    ],
    "x2b": [
        {"enonce": "On additionne sur 8 bits : `$7F + $7E` (par exemple avec `ADD.B`). Donner les drapeaux N, Z, V, C (écrire NZVC en binaire, par exemple `%1010`).", "calc": "8*(((hexa('7F')+hexa('7E'))%2**8)//2**7)+4*(1-Min(1,(hexa('7F')+hexa('7E'))%2**8))+2*(abs(((hexa('7F')-2**8*(hexa('7F')//2**7))+(hexa('7E')-2**8*(hexa('7E')//2**7))+2**7)//2**8))+(hexa('7F')+hexa('7E'))//2**8", "ans": "bits('1010')", "sol": "`$7F + $7E = $FD` ; sur 8 bits on garde" "\n"
        "`$FD`." "\n"
        "N$=1$, Z$=0$, V$=1$ (dépassement signé), C$=0$. On lit NZVC `1010`."},
    ],
    "x2c": [
        {"enonce": "On additionne sur 8 bits : `$7E + $80` (par exemple avec `ADD.B`). Donner le résultat (en hexadécimal, sur 8 bits).", "calc": "(hexa('7E')+hexa('80'))%2**8", "ans": "hexa('FE')", "sol": "`$7E + $80 = $FE` ; sur 8 bits on garde" "\n"
        "`$FE`."},
    ],
    "x2d": [
        {"enonce": "On additionne sur 8 bits : `$7E + $80` (par exemple avec `ADD.B`). Donner les drapeaux N, Z, V, C (écrire NZVC en binaire, par exemple `%1010`).", "calc": "8*(((hexa('7E')+hexa('80'))%2**8)//2**7)+4*(1-Min(1,(hexa('7E')+hexa('80'))%2**8))+2*(abs(((hexa('7E')-2**8*(hexa('7E')//2**7))+(hexa('80')-2**8*(hexa('80')//2**7))+2**7)//2**8))+(hexa('7E')+hexa('80'))//2**8", "ans": "bits('1000')", "sol": "`$7E + $80 = $FE` ; sur 8 bits on garde" "\n"
        "`$FE`." "\n"
        "N$=1$, Z$=0$, V$=0$ (pas de dépassement signé), C$=0$. On lit NZVC `1000`."},
    ],
    "x2e": [
        {"enonce": "On additionne sur 16 bits : `$00FF + $0001` (par exemple avec `ADD.W`). Donner les drapeaux N, Z, V, C (écrire NZVC en binaire, par exemple `%1010`).", "calc": "8*(((hexa('00FF')+hexa('0001'))%2**16)//2**15)+4*(1-Min(1,(hexa('00FF')+hexa('0001'))%2**16))+2*(abs(((hexa('00FF')-2**16*(hexa('00FF')//2**15))+(hexa('0001')-2**16*(hexa('0001')//2**15))+2**15)//2**16))+(hexa('00FF')+hexa('0001'))//2**16", "ans": "bits('0000')", "sol": "`$00FF + $0001 = $100` ; sur 16 bits on garde" "\n"
        "`$0100`." "\n"
        "N$=0$, Z$=0$, V$=0$ (pas de dépassement signé), C$=0$. On lit NZVC `0000`."},
    ],
    "x2f": [
        {"enonce": "On additionne sur 32 bits : `$A0101010 + $20909090` (par exemple avec `ADD.L`). Donner le résultat (en hexadécimal, sur 32 bits).", "calc": "(hexa('A0101010')+hexa('20909090'))%2**32", "ans": "hexa('C0A0A0A0')", "sol": "`$A0101010 + $20909090 = $C0A0A0A0` ; sur 32 bits on garde" "\n"
        "`$C0A0A0A0`."},
    ],
    "x2g": [
        {"enonce": "On additionne sur 32 bits : `$A0101010 + $20909090` (par exemple avec `ADD.L`). Donner les drapeaux N, Z, V, C (écrire NZVC en binaire, par exemple `%1010`).", "calc": "8*(((hexa('A0101010')+hexa('20909090'))%2**32)//2**31)+4*(1-Min(1,(hexa('A0101010')+hexa('20909090'))%2**32))+2*(abs(((hexa('A0101010')-2**32*(hexa('A0101010')//2**31))+(hexa('20909090')-2**32*(hexa('20909090')//2**31))+2**31)//2**32))+(hexa('A0101010')+hexa('20909090'))//2**32", "ans": "bits('1000')", "sol": "`$A0101010 + $20909090 = $C0A0A0A0` ; sur 32 bits on garde" "\n"
        "`$C0A0A0A0`." "\n"
        "N$=1$, Z$=0$, V$=0$ (pas de dépassement signé), C$=0$. On lit NZVC `1000`."},
    ],
    "x4a": [
        {"enonce": "Même programme avec `MOVE.L #$12347000,D7` au début. Que vaut D1 à la fin ?", "calc": "1 if (lambda x: x-2**16*(x//2**15))((hexa('7000'))%2**16)>28672 else 2", "ans": "hexa('00000002')", "sol": "D7.W vaut `$7000` :" "\n"
        "$28672>28672$ est faux (égalité), pas de saut : D1 vaut" "\n"
        "`$00000002`."},
    ],
    "x4b": [
        {"enonce": "Même programme avec `MOVE.L #515,D0` (au lieu de $260$). Que vaut D2 à la fin ?", "calc": "(515%256 or 256)", "ans": "hexa('00000003')", "sol": r"$515=2\times256+3$ : D0.B vaut $3$, trois tours. D2 vaut" "\n"
        "`$00000003`."},
    ],
    "x4c": [
        {"enonce": "Même programme avec `MOVE.L #$00123400,D0` avant `LOOP3`. Que vaut D3 à la fin ?", "calc": "hexa('00123400')%65536+1", "ans": "hexa('00003401')", "sol": "D0.W vaut `$3400` :" "\n"
        "`$3401` tours."},
    ],
    "x4d": [
        {"enonce": "Même programme avec `MOVE.L #$87654321,D4` au début de `PART4`. Que vaut D4 à la fin ?", "calc": "(lambda x: (x-x%4294967296)+((((x%4294967296)>>8)|((x%4294967296)<<24))%4294967296))((lambda x: (x-x%256)+((((x%256)>>4)|((x%256)<<4))%256))((lambda x: (x%65536)*65536+x//65536)((lambda x: (x-x%4294967296)+((((x%4294967296)>>8)|((x%4294967296)<<24))%4294967296))((lambda x: (x-x%65536)+((((x%65536)>>4)|((x%65536)<<12))%65536))(hexa('87654321'))))))", "ans": "hexa('78651432')", "sol": "Même méthode, chiffre par chiffre."},
    ],
    "y1a": [
        {"enonce": "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $FFFFFFFF   A0 = $00005000" "\n"
        "D1 = $0000FFF0   A1 = $00005008" "\n"
        "D2 = $0000000A   A2 = $00005010" "\n"
        "$005000  54 AF 18 B9 E7 21 48 C0" "\n"
        "$005008  C9 10 11 C8 D4 36 1F 88" "\n"
        "$005010  13 79 01 80 42 1A 2D 49" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVE.L $5000,-(A1)`. Donner les" "\n"
        "$8$ octets de la mémoire à partir de" "\n"
        "`$5000` après l'instruction, écrits comme un seul nombre hexadécimal de" "\n"
        "$16$ chiffres.", "calc": "hexa('54AF18B9'+'54AF18B9'+'')", "ans": "hexa('54AF18B954AF18B9')", "sol": "Avant : `54AF18B9E72148C0`. L'instruction écrit `54AF18B9` à partir de l'octet n° 4 de la fenêtre (adresse `$5004`) ; les autres octets ne changent pas. Après : `54AF18B954AF18B9`."},
    ],
    "y1b": [
        {"enonce": "A1 vaut `$5008`. Quelle est la valeur de A1 après `MOVE.B D0,-(A1)` ?", "calc": "hexa('5008')-1", "ans": "hexa('5007')", "sol": "`.B` : A1 diminue de $1$" "\n"
        "(`$5007`)."},
    ],
    "y1c": [
        {"enonce": "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $FFFFFFFF   A0 = $00005000" "\n"
        "D1 = $0000FFF0   A1 = $00005008" "\n"
        "D2 = $0000000A   A2 = $00005010" "\n"
        "$005000  54 AF 18 B9 E7 21 48 C0" "\n"
        "$005008  C9 10 11 C8 D4 36 1F 88" "\n"
        "$005010  13 79 01 80 42 1A 2D 49" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVE.W #5001,2(A0,D2.L)`. Donner les $8$ octets de la mémoire à partir de" "\n"
        "`$5008` après l'instruction, écrits comme un seul nombre hexadécimal de" "\n"
        "$16$ chiffres.", "calc": "hexa('C91011C8'+'1389'+'1F88')", "ans": "hexa('C91011C813891F88')", "sol": "Avant : `C91011C8D4361F88`. L'instruction écrit `1389` à partir de l'octet n° 4 de la fenêtre (adresse `$500C`) ; les autres octets ne changent pas. Après : `C91011C813891F88`."},
    ],
    "y1d": [
        {"enonce": "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $FFFFFFFF   A0 = $00005000" "\n"
        "D1 = $0000FFF0   A1 = $00005008" "\n"
        "D2 = $0000000A   A2 = $00005010" "\n"
        "$005000  54 AF 18 B9 E7 21 48 C0" "\n"
        "$005008  C9 10 11 C8 D4 36 1F 88" "\n"
        "$005010  13 79 01 80 42 1A 2D 49" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVE.B -8(A2),$11(A0)`. Donner les" "\n"
        "$8$ octets de la mémoire à partir de" "\n"
        "`$5010` après l'instruction, écrits comme un seul nombre hexadécimal de" "\n"
        "$16$ chiffres.", "calc": "hexa('13'+'C9'+'0180421A2D49')", "ans": "hexa('13C90180421A2D49')", "sol": "Avant : `13790180421A2D49`. L'instruction écrit `C9` à partir de l'octet n° 1 de la fenêtre (adresse `$5011`) ; les autres octets ne changent pas. Après : `13C90180421A2D49`."},
    ],
    "y2a": [
        {"enonce": "On additionne sur 8 bits : `$7A + $4A` (par exemple avec `ADD.B`). Donner le résultat (en hexadécimal, sur 8 bits).", "calc": "(hexa('7A')+hexa('4A'))%2**8", "ans": "hexa('C4')", "sol": "`$7A + $4A = $C4` ; sur 8 bits on garde" "\n"
        "`$C4`."},
    ],
    "y2b": [
        {"enonce": "On additionne sur 8 bits : `$7A + $4A` (par exemple avec `ADD.B`). Donner les drapeaux N, Z, V, C (écrire NZVC en binaire, par exemple `%1010`).", "calc": "8*(((hexa('7A')+hexa('4A'))%2**8)//2**7)+4*(1-Min(1,(hexa('7A')+hexa('4A'))%2**8))+2*(abs(((hexa('7A')-2**8*(hexa('7A')//2**7))+(hexa('4A')-2**8*(hexa('4A')//2**7))+2**7)//2**8))+(hexa('7A')+hexa('4A'))//2**8", "ans": "bits('1010')", "sol": "`$7A + $4A = $C4` ; sur 8 bits on garde" "\n"
        "`$C4`." "\n"
        "N$=1$, Z$=0$, V$=1$ (dépassement signé), C$=0$. On lit NZVC `1010`."},
    ],
    "y2c": [
        {"enonce": "On additionne sur 16 bits : `$7AAA + $9446` (par exemple avec `ADD.W`). Donner le résultat (en hexadécimal, sur 16 bits).", "calc": "(hexa('7AAA')+hexa('9446'))%2**16", "ans": "hexa('0EF0')", "sol": "`$7AAA + $9446 = $10EF0` ; sur 16 bits on garde" "\n"
        "`$0EF0`."},
    ],
    "y2d": [
        {"enonce": "On additionne sur 16 bits : `$7AAA + $9446` (par exemple avec `ADD.W`). Donner les drapeaux N, Z, V, C (écrire NZVC en binaire, par exemple `%1010`).", "calc": "8*(((hexa('7AAA')+hexa('9446'))%2**16)//2**15)+4*(1-Min(1,(hexa('7AAA')+hexa('9446'))%2**16))+2*(abs(((hexa('7AAA')-2**16*(hexa('7AAA')//2**15))+(hexa('9446')-2**16*(hexa('9446')//2**15))+2**15)//2**16))+(hexa('7AAA')+hexa('9446'))//2**16", "ans": "bits('0001')", "sol": "`$7AAA + $9446 = $10EF0` ; sur 16 bits on garde" "\n"
        "`$0EF0`." "\n"
        "N$=0$, Z$=0$, V$=0$ (pas de dépassement signé), C$=1$. On lit NZVC `0001`."},
    ],
    "y2e": [
        {"enonce": "On additionne sur 32 bits : `$50505050 + $50505050` (par exemple avec `ADD.L`). Donner le résultat (en hexadécimal, sur 32 bits).", "calc": "(hexa('50505050')+hexa('50505050'))%2**32", "ans": "hexa('A0A0A0A0')", "sol": "`$50505050 + $50505050 = $A0A0A0A0` ; sur 32 bits on garde" "\n"
        "`$A0A0A0A0`."},
    ],
    "y2f": [
        {"enonce": "On additionne sur 32 bits : `$50505050 + $50505050` (par exemple avec `ADD.L`). Donner les drapeaux N, Z, V, C (écrire NZVC en binaire, par exemple `%1010`).", "calc": "8*(((hexa('50505050')+hexa('50505050'))%2**32)//2**31)+4*(1-Min(1,(hexa('50505050')+hexa('50505050'))%2**32))+2*(abs(((hexa('50505050')-2**32*(hexa('50505050')//2**31))+(hexa('50505050')-2**32*(hexa('50505050')//2**31))+2**31)//2**32))+(hexa('50505050')+hexa('50505050'))//2**32", "ans": "bits('1010')", "sol": "`$50505050 + $50505050 = $A0A0A0A0` ; sur 32 bits on garde" "\n"
        "`$A0A0A0A0`." "\n"
        "N$=1$, Z$=0$, V$=1$ (dépassement signé), C$=0$. On lit NZVC `1010`."},
    ],
    "y3a": [
        {"enonce": "Même programme avec `MOVE.L #200,D7` au début. Que vaut D1 à la fin ?", "calc": "1 if 200<128 else 2", "ans": "hexa('00000002')", "sol": "$200<128$ est faux : pas de saut, `MOVEQ.L #2,D1` est exécuté :" "\n"
        "`$00000002`."},
    ],
    "y3b": [
        {"enonce": "Même programme avec `MOVE.B #35,D0`. Que vaut D2 à la fin ?", "calc": "35", "ans": "hexa('00000023')", "sol": "$35$ tours : D2 vaut" "\n"
        "`$00000023`."},
    ],
    "y3c": [
        {"enonce": "Même programme avec `MOVE.L #15,D7` au début. Que vaut D3 à la fin ?", "calc": "(15+16)%65536+1", "ans": "hexa('00000020')", "sol": "D7 vaut $15+16=31$ : $32$ tours, D3 vaut" "\n"
        "`$00000020`."},
    ],
    "qd1": [
        {"enonce": "Même programme avec `MOVE.L #$80FF11FF,D7`. Que vaut D1 à la fin ?", "calc": "1 if (lambda x: x-2**32*(x//2**31))((hexa('80FF11FF'))%2**32)>=0 else 2", "ans": "hexa('00000002')", "sol": "D7 est négatif : `BPL` ne saute pas, `MOVEQ.L #2,D1` est exécuté : D1 vaut $2$."},
    ],
    "qd2": [
        {"enonce": "Même programme avec `MOVE.L #$00FF1100,D7`. Que vaut D2 à la fin ?", "calc": "1 if (lambda x: x-2**8*(x//2**7))((hexa('00'))%2**8)<0 else 2", "ans": "hexa('00000002')", "sol": "D7.B vaut $0$ : N$=0$, pas de saut, D2 vaut $2$."},
    ],
    "qd3": [
        {"enonce": "Même programme avec `MOVE.L #$10003,D0`. Que vaut D3 à la fin ?", "calc": "hexa('10003')%65536", "ans": "hexa('00000003')", "sol": "D0.W vaut `$0003` :" "\n"
        "$3$ tours. D3 vaut" "\n"
        "`$00000003`."},
    ],
    "qd4": [
        {"enonce": "Même programme avec `MOVE.W #$7F,D0` avant `LOOP4`. Que vaut D4 à la fin ?", "calc": "hexa('7F')+1", "ans": "hexa('00000080')", "sol": "D0.W vaut `$7F` :" "\n"
        "$128$ tours," "\n"
        "`$80`."},
    ],
    "qd5": [
        {"enonce": "Même programme avec `MOVE.L #$00FF1142,D7`... et" "\n"
        "`CMP.B #$42,D7` (égalité). Que vaut D5 à la fin ?", "calc": "1 if (lambda x: x-2**8*(x//2**7))((hexa('42'))%2**8)>66 else 2", "ans": "hexa('00000002')", "sol": "D7.B vaut `$42` :" "\n"
        "$66>66$ est faux, pas de saut, D5 vaut $2$."},
    ],
    "qd6": [
        {"enonce": "Même programme avec `MOVE.L #$00FF1140,D7`. Que vaut D6 à la fin ?", "calc": "1 if hexa('40')<=66 else 2", "ans": "hexa('00000001')", "sol": "D7.B vaut `$40`" "\n"
        r"($64$) : $64\le66$ est vrai, `BLS` saute : D6 reste à $1$."},
    ],
    "h191": [
        {"enonce": "On exécute le programme suivant :" "\n"
        "" "\n"
        "```asm" "\n"
        "        CLR.L   D1" "\n"
        "        MOVE.W  #4,D2" "\n"
        "OUTER   MOVE.B  #64,D0" "\n"
        "INNER   ADDQ.L  #1,D1" "\n"
        "        SUBQ.B  #4,D0" "\n"
        "        BNE     INNER" "\n"
        "        DBRA    D2,OUTER" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D1 à la fin (en décimal) ?", "calc": "(4+1)*(64//4)", "ans": "80", "sol": r"La boucle interne fait $64/4=16$ tours à chaque passage (D0.B vaut $64$ au départ et `SUBQ.B` a un pas de $4$). La boucle externe est un `DBRA` avec D2.W $=4$ : $4+1=5$ passages. D1 $=(4+1)\times16=80$."},
    ],
    "h192": [
        {"enonce": r"Le sous-programme récursif `Fact` calcule $n!$ pour $n$ dans D0 (avec $n\le8$) :" "\n"
        "" "\n"
        "```asm" "\n"
        "Fact    CMP.L   #1,D0" "\n"
        r"        BLS     \one" "\n"
        "        MOVE.L  D0,-(A7)" "\n"
        "        SUBQ.L  #1,D0" "\n"
        "        JSR     Fact" "\n"
        "        MOVE.L  (A7)+,D1" "\n"
        "        MULU.W  D1,D0" "\n"
        "        RTS" "\n"
        r"\one    MOVEQ.L #1,D0" "\n"
        "        RTS" "\n"
        "```" "\n"
        "" "\n"
        "On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "Main    MOVEQ.L #7,D0" "\n"
        "        JSR     Fact" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut D0 à la fin (en décimal) ?", "calc": "factorial(7)", "ans": "5040", "sol": r"Pour $n>1$, `Fact` empile $n$, calcule $(n-1)!$ par un appel récursif, dépile $n$ dans D1 et multiplie (`MULU.W D1,D0`). Pour $n\le1$ elle renvoie $1$. Résultat : $7!=5040$."},
    ],
    "h193": [
        {"enonce": r"A7 vaut `$F00000` au début de `Main`. On modifie `Fact` : le cas de base (`\one`) contient maintenant `ILLEGAL`, qui arrête le programme :" "\n"
        "" "\n"
        "```asm" "\n"
        "Fact    CMP.L   #1,D0" "\n"
        r"        BLS     \one" "\n"
        "        MOVE.L  D0,-(A7)" "\n"
        "        SUBQ.L  #1,D0" "\n"
        "        JSR     Fact" "\n"
        "        MOVE.L  (A7)+,D1" "\n"
        "        MULU.W  D1,D0" "\n"
        "        RTS" "\n"
        r"\one    ILLEGAL" "\n"
        "```" "\n"
        "" "\n"
        "On exécute :" "\n"
        "" "\n"
        "```asm" "\n"
        "Main    MOVEQ.L #3,D0" "\n"
        "        JSR     Fact" "\n"
        "```" "\n"
        "" "\n"
        "Que vaut A7 quand le processeur atteint `ILLEGAL` ?", "calc": "hexa('F00000')-(8*3-4)", "ans": "hexa('EFFFEC')", "sol": r"Pour $n=3$ le programme fait $3$ appels `JSR Fact` (le premier depuis `Main`, $2$ récursifs) : $3\times4$ octets d'adresses de retour. Chaque appel non terminal empile aussi D0 ($4$ octets) : $2\times4$ octets. Profondeur : $4n+4(n-1)=8n-4=20$ octets. A7 vaut" "\n"
        "`$F00000` moins" "\n"
        "$20$."},
    ],
    "h196": [
        {"enonce": "Que vaut A1 après `MOVEA.W #$1234,A1` (hexadécimal sur" "\n"
        "$32$ bits) ?", "calc": "hexa('1234')", "ans": "hexa('00001234')", "sol": "`$1234` est positif : A1 vaut" "\n"
        "`$00001234`."},
    ],
    "z1a": [
        {"enonce": "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $0001FFFF   A0 = $00005000" "\n"
        "D1 = $10000002   A1 = $00005008" "\n"
        "D2 = $FFFFFFFE   A2 = $00005010" "\n"
        "$005000  54 AF 18 B9 E7 21 48 C0" "\n"
        "$005008  C9 10 11 C8 D4 36 1F 88" "\n"
        "$005010  13 79 01 80 42 1A 2D 49" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVE.W #$5000,-(A2)`. Donner les" "\n"
        "$8$ octets de la mémoire à partir de" "\n"
        "`$5008` après l'instruction, écrits comme un seul nombre hexadécimal de" "\n"
        "$16$ chiffres.", "calc": "hexa('C91011C8D436'+'5000'+'')", "ans": "hexa('C91011C8D4365000')", "sol": "Avant : `C91011C8D4361F88`. L'instruction écrit `5000` à partir de l'octet n° 6 de la fenêtre (adresse `$500E`) ; les autres octets ne changent pas. Après : `C91011C8D4365000`."},
    ],
    "z1b": [
        {"enonce": "Mêmes valeurs initiales (A2 `$5010`). Quelle est la valeur de A2 après `MOVE.L D0,-(A2)` ?", "calc": "hexa('5010')-4", "ans": "hexa('500C')", "sol": "`.L` : A2 diminue de $4$ :" "\n"
        "`$500C`."},
    ],
    "z1c": [
        {"enonce": "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $0001FFFF   A0 = $00005000" "\n"
        "D1 = $10000002   A1 = $00005008" "\n"
        "D2 = $FFFFFFFE   A2 = $00005010" "\n"
        "$005000  54 AF 18 B9 E7 21 48 C0" "\n"
        "$005008  C9 10 11 C8 D4 36 1F 88" "\n"
        "$005010  13 79 01 80 42 1A 2D 49" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVE.W $5000,3(A1,D0.W)`. Donner les" "\n"
        "$8$ octets de la mémoire à partir de" "\n"
        "`$5008` après l'instruction, écrits comme un seul nombre hexadécimal de" "\n"
        "$16$ chiffres.", "calc": "hexa('C910'+'54AF'+'D4361F88')", "ans": "hexa('C91054AFD4361F88')", "sol": "Avant : `C91011C8D4361F88`. L'instruction écrit `54AF` à partir de l'octet n° 2 de la fenêtre (adresse `$500A`) ; les autres octets ne changent pas. Après : `C91054AFD4361F88`."},
    ],
    "z1d": [
        {"enonce": "État initial :" "\n"
        "" "\n"
        "```" "\n"
        "D0 = $0001FFFF   A0 = $00005000" "\n"
        "D1 = $10000002   A1 = $00005008" "\n"
        "D2 = $FFFFFFFE   A2 = $00005010" "\n"
        "$005000  54 AF 18 B9 E7 21 48 C0" "\n"
        "$005008  C9 10 11 C8 D4 36 1F 88" "\n"
        "$005010  13 79 01 80 42 1A 2D 49" "\n"
        "```" "\n"
        "" "\n"
        "On exécute `MOVE.W $5002(PC),-2(A1)`. Donner les" "\n"
        "$8$ octets de la mémoire à partir de" "\n"
        "`$5000` après l'instruction, écrits comme un seul nombre hexadécimal de" "\n"
        "$16$ chiffres.", "calc": "hexa('54AF18B9E721'+'18B9'+'')", "ans": "hexa('54AF18B9E72118B9')", "sol": "Avant : `54AF18B9E72148C0`. L'instruction écrit `18B9` à partir de l'octet n° 6 de la fenêtre (adresse `$5006`) ; les autres octets ne changent pas. Après : `54AF18B9E72118B9`."},
    ],
    "z2a": [
        {"enonce": "On additionne sur 8 bits : `$E2 + $A9` (par exemple avec `ADD.B`). Donner le résultat (en hexadécimal, sur 8 bits).", "calc": "(hexa('E2')+hexa('A9'))%2**8", "ans": "hexa('8B')", "sol": "`$E2 + $A9 = $18B` ; sur 8 bits on garde" "\n"
        "`$8B`."},
    ],
    "z2b": [
        {"enonce": "On additionne sur 8 bits : `$E2 + $A9` (par exemple avec `ADD.B`). Donner les drapeaux N, Z, V, C (écrire NZVC en binaire, par exemple `%1010`).", "calc": "8*(((hexa('E2')+hexa('A9'))%2**8)//2**7)+4*(1-Min(1,(hexa('E2')+hexa('A9'))%2**8))+2*(abs(((hexa('E2')-2**8*(hexa('E2')//2**7))+(hexa('A9')-2**8*(hexa('A9')//2**7))+2**7)//2**8))+(hexa('E2')+hexa('A9'))//2**8", "ans": "bits('1001')", "sol": "`$E2 + $A9 = $18B` ; sur 8 bits on garde" "\n"
        "`$8B`." "\n"
        "N$=1$, Z$=0$, V$=0$ (pas de dépassement signé), C$=1$. On lit NZVC `1001`."},
    ],
    "z2c": [
        {"enonce": "On additionne sur 16 bits : `$4000 + $4000` (par exemple avec `ADD.W`). Donner le résultat (en hexadécimal, sur 16 bits).", "calc": "(hexa('4000')+hexa('4000'))%2**16", "ans": "hexa('8000')", "sol": "`$4000 + $4000 = $8000` ; sur 16 bits on garde" "\n"
        "`$8000`."},
    ],
    "z2d": [
        {"enonce": "On additionne sur 16 bits : `$4000 + $4000` (par exemple avec `ADD.W`). Donner les drapeaux N, Z, V, C (écrire NZVC en binaire, par exemple `%1010`).", "calc": "8*(((hexa('4000')+hexa('4000'))%2**16)//2**15)+4*(1-Min(1,(hexa('4000')+hexa('4000'))%2**16))+2*(abs(((hexa('4000')-2**16*(hexa('4000')//2**15))+(hexa('4000')-2**16*(hexa('4000')//2**15))+2**15)//2**16))+(hexa('4000')+hexa('4000'))//2**16", "ans": "bits('1010')", "sol": "`$4000 + $4000 = $8000` ; sur 16 bits on garde" "\n"
        "`$8000`." "\n"
        "N$=1$, Z$=0$, V$=1$ (dépassement signé), C$=0$. On lit NZVC `1010`."},
    ],
    "z3a": [
        {"enonce": "Même programme avec `MOVE.L #$00BB0033,D7`. Que vaut D1 à la fin ?", "calc": "1 if (lambda x: x-2**8*(x//2**7))((hexa('33'))%2**8)<0 else 2", "ans": "hexa('00000002')", "sol": "D7.B vaut `$33`, positif : pas de saut, D1 vaut" "\n"
        "$2$."},
    ],
    "z3b": [
        {"enonce": "Même programme avec `MOVE.L #$FFFFFF10,D0`. Que vaut D2 à la fin ?", "calc": "hexa('FFFFFF10')%256 or 256", "ans": "hexa('00000010')", "sol": "D0.B vaut `$10` :" "\n"
        "$16$ tours, D2 vaut" "\n"
        "`$00000010`."},
    ],
    "z3c": [
        {"enonce": "Même programme avec `MOVE.W #$0200,D0` avant `LOOP3`. Que vaut D3 à la fin ?", "calc": "hexa('0200')+1", "ans": "hexa('00000201')", "sol": "D0.W vaut `$200` :" "\n"
        "`$201` tours."},
    ],
    "f512": [
        {"enonce": "On additionne sur 8 bits : `$2B + X`. Quel est le **plus petit** nombre X (en hexadécimal, sur 2 chiffres) pour lequel on obtient" "\n"
        "N$=0$, Z$=0$, V$=0$, C$=1$ ?", "calc": "2**8-hexa('2B')+1", "ans": "hexa('D6')", "sol": r"Retenue : $43+X\ge256$. Pour $X=213$ le résultat est nul (Z$=1$) : on prend $X=214$. Le plus petit X est" "\n"
        "`$D6`."},
    ],
    "f513": [
        {"enonce": "On additionne sur 16 bits : `$1234 + X`. Quel est le **plus petit** nombre X (en hexadécimal, sur 4 chiffres) pour lequel on obtient" "\n"
        "N$=0$, Z$=1$, V$=0$, C$=1$ ?", "calc": "2**16-hexa('1234')", "ans": "hexa('EDCC')", "sol": "Z$=1$ et C$=1$ : $A+X=2^{16}$, d'où $X=2^{16}-4660=60876$. Le plus petit X est" "\n"
        "`$EDCC`."},
    ],
    "f514": [
        {"enonce": "On additionne sur 32 bits : `$7FFFFFF0 + X`. Quel est le **plus petit** nombre X (en hexadécimal, sur 8 chiffres) pour lequel on obtient" "\n"
        "N$=1$, Z$=0$, V$=1$, C$=0$ ?", "calc": "2**31-hexa('7FFFFFF0')", "ans": "hexa('00000010')", "sol": r"N$=1$ et V$=1$ : deux positifs donnent un résultat négatif. $7FFFFFF0+X\ge2^{31}$ donne $X\ge16$ : le plus petit X est" "\n"
        "`$00000010`."},
    ],
    "f515": [
        {"enonce": "On additionne sur 8 bits : `$6F + X`. Quel est le **plus petit** nombre X (en hexadécimal, sur 2 chiffres) pour lequel on obtient" "\n"
        "N$=1$, Z$=0$, V$=1$, C$=0$ ?", "calc": "2**7-hexa('6F')", "ans": "hexa('11')", "sol": r"Deux positifs donnent un résultat négatif : $111+X\ge128$, donc $X\ge17$. Le plus petit X est" "\n"
        "`$11`."},
    ],
}
for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["id"] in VARIANTS:
            _e["variants"] = VARIANTS[_e["id"]]
for _e in EXTRA_PARTS:
    if _e["id"] in VARIANTS:
        _e["variants"] = VARIANTS[_e["id"]]

QUIZ = [
    {"notion": "nombres", "type": "qcm", "q": "L'octet `$F0`, en complément à deux sur" "\n"
        "$8$ bits, vaut :", "choix": ["$-16$", "$240$", "$-240$", "$-112$"], "bonne": 0},
    {"notion": "nombres", "type": "vf", "q": "Étendre en signe l'octet `$80` sur" "\n"
        "$16$ bits donne" "\n"
        "`$0080`.", "bonne": False},
    {"notion": "nombres", "type": "qcm", "q": "En assembleur 68000, un nombre précédé de `%` est écrit en :", "choix": ["hexadécimal", "binaire", "octal", "décimal"], "bonne": 1},
    {"notion": "memoire", "type": "vf", "q": "Un mot de $16$ bits peut être lu à n'importe quelle adresse, paire ou impaire.", "bonne": False},
    {"notion": "memoire", "type": "qcm", "q": "Le mot long `$12345678` est rangé à partir de l'adresse" "\n"
        "`$1000` en big-endian. Quel octet est à" "\n"
        "`$1000` ?", "choix": ["`$34`", "`$12`", "`$56`", "`$78`"], "bonne": 1},
    {"notion": "memoire", "type": "qcm", "q": "Combien d'octets le 68000 peut-il adresser ?", "choix": ["$4$ Gio", "$64$ Kio", "$16$ Mio", "$1$ Mio"], "bonne": 2},
    {"notion": "directives", "type": "vf", "q": "`ORG` est une instruction du 68000 : elle est traduite en code machine.", "bonne": False},
    {"notion": "directives", "type": "qcm", "q": "`DS.W 5` réserve :", "choix": ["$6$ octets", "$5$ octets", "$10$ octets", "$20$ octets"], "bonne": 2},
    {"notion": "directives", "type": "qcm", "q": "Quelle directive donne une valeur à une étiquette ?", "choix": ["`ORG`", "`EQU`", "`DC`", "`DS`"], "bonne": 1},
    {"notion": "registres", "type": "qcm", "q": "Le 68000 possède :", "choix": ["un seul registre d'adresse", "$16$ registres d'adresse", "$8$ registres d'adresse", "$32$ registres d'adresse"], "bonne": 2},
    {"notion": "registres", "type": "vf", "q": "Le 68000 possède deux pointeurs de pile, USP et SSP, tous deux accessibles par A7.", "bonne": True},
    {"notion": "registres", "type": "vf", "q": "Les registres d'adresse sont accessibles sur $8$ bits.", "bonne": False},
    {"notion": "tailles", "type": "qcm", "q": "D0 contient `$11223344`. Après" "\n"
        "`MOVE.B #$FF,D0`, D0 contient :", "choix": ["`$FFFFFFFF`", "`$000000FF`", "`$1122FFFF`", "`$112233FF`"], "bonne": 3},
    {"notion": "tailles", "type": "vf", "q": "`MOVEQ.L #-1,D0` met `$FFFFFFFF` dans D0.", "bonne": True},
    {"notion": "tailles", "type": "vf", "q": "L'instruction `MOVE` accepte un registre d'adresse comme destination : il n'y a pas besoin de `MOVEA`.", "bonne": False},
    {"notion": "drapeaux", "type": "qcm", "q": "Le drapeau V est à $0$ quand :", "choix": ["aucun dépassement signé n'apparaît", "le résultat est négatif", "un dépassement non signé apparaît", "la retenue vaut $1$"], "bonne": 0},
    {"notion": "drapeaux", "type": "vf", "q": "Sur $8$ bits," "\n"
        "`$7F + $80` donne" "\n"
        "C$=0$ et V$=0$.", "bonne": True},
    {"notion": "drapeaux", "type": "qcm", "q": "Sur $8$ bits," "\n"
        "`$F0 + $11` donne :", "choix": ["C$=1$ et V$=0$", "C$=0$ et V$=1$", "C$=1$ et V$=1$", "C$=0$ et V$=0$"], "bonne": 0},
    {"notion": "adressage", "type": "qcm", "q": "Avec `MOVE.W -(A0),D0`, le registre A0 est :", "choix": ["décrémenté de $1$", "inchangé", "décrémenté de $2$", "décrémenté de $4$"], "bonne": 2},
    {"notion": "adressage", "type": "qcm", "q": "Avec `MOVE.L -1(A0),D0`, le registre A0 est :", "choix": ["incrémenté de $4$", "décrémenté de $1$", "inchangé", "décrémenté de $4$"], "bonne": 2},
    {"notion": "adressage", "type": "vf", "q": "Le mode d'adressage direct spécifie un emplacement mémoire.", "bonne": False},
    {"notion": "ea", "type": "qcm", "q": "Dans `MOVE.W $5000,D0`, la valeur" "\n"
        "`$5000` est :", "choix": ["une adresse sur $16$ bits", "une donnée immédiate", "une adresse sur $32$ bits", "un numéro de registre"], "bonne": 2},
    {"notion": "ea", "type": "vf", "q": "`MOVE.L $5003,D0` est refusée par l'assembleur.", "bonne": False},
    {"notion": "ea", "type": "qcm", "q": "A1 vaut `$1008` et D3 vaut" "\n"
        "$3$. Quelle est l'adresse effective de `1(A1,D3.L)` ?", "choix": ["`$100D`", "`$1009`", "`$100C`", "`$100B`"], "bonne": 2},
    {"notion": "memmove", "type": "qcm", "q": "A0 vaut `$1000`. `MOVE.W #36,(A0)` écrit à partir de" "\n"
        "`$1000` les octets :", "choix": ["`00 24`", "`24`", "`24 00`", "`00 00 00 24`"], "bonne": 0},
    {"notion": "memmove", "type": "vf", "q": "Dans `MOVE.L -(A2),-(A2)`, la source est évaluée avant la destination.", "bonne": True},
    {"notion": "arith", "type": "qcm", "q": "D0.B vaut $5$. Après `NEG.B D0`, D0.B vaut :", "choix": ["`$FB`", "`$FA`", "`$05`", "`$00`"], "bonne": 0},
    {"notion": "arith", "type": "vf", "q": "`MULU.W D1,D0` ne laisse que $16$ bits de résultat dans D0.", "bonne": False},
    {"notion": "arith", "type": "qcm", "q": "Après `DIVU.W #10,D0`, où se trouve le reste ?", "choix": ["dans A0", "dans les bits $15$ à $0$ de D0", "dans les bits $31$ à $16$ de D0", "dans D1"], "bonne": 2},
    {"notion": "rotation", "type": "qcm", "q": "D1 vaut `$12345678`. Après `SWAP D1`, D1 vaut :", "choix": ["`$34127856`", "`$78563412`", "`$87654321`", "`$56781234`"], "bonne": 3},
    {"notion": "rotation", "type": "vf", "q": "`ROR.B #4,D1` échange les deux chiffres hexadécimaux de l'octet de poids faible de D1.", "bonne": True},
    {"notion": "rotation", "type": "qcm", "q": "D4 vaut `$12345678`. Après `ROR.W #4,D4`, D4 vaut :", "choix": ["`$81234567`", "`$12345867`", "`$67812345`", "`$12348567`"], "bonne": 3},
    {"notion": "branch", "type": "qcm", "q": "Après `CMP.B #$70,D7`, quel branchement saute si D7.B est inférieur à" "\n"
        "`$70` en comparaison non signée ?", "choix": ["`BMI`", "`BLT`", "`BPL`", "`BLO`"], "bonne": 3},
    {"notion": "branch", "type": "vf", "q": "`BHS` est un alias de `BCC`.", "bonne": True},
    {"notion": "branch", "type": "vf", "q": "`BGT` est un branchement à comparaison non signée.", "bonne": False},
    {"notion": "branch", "type": "qcm", "q": "Après `TST.B D1`, `BMI` saute si :", "choix": ["D1.B est négatif", "D1.B est nul", "D1.B vaut $1$", "D1.B est positif"], "bonne": 0},
    {"notion": "boucle", "type": "qcm", "q": "`DBRA D0,LOOP` avec D0.W $=9$ fait :", "choix": ["$9$ tours", "$11$ tours", "$10$ tours", "$8$ tours"], "bonne": 2},
    {"notion": "boucle", "type": "vf", "q": "Avec `SUBQ.B #1,D0` puis `BNE`, si D0.B vaut $0$ au départ, la boucle s'exécute $256$ fois.", "bonne": True},
    {"notion": "boucle", "type": "vf", "q": "`SUBQ.B #1,D0` modifie les $32$ bits de D0.", "bonne": False},
    {"notion": "pile", "type": "qcm", "q": "`MOVEM.L D1-D3/A4/A5,-(A7)` fait diminuer A7 de :", "choix": ["$10$ octets", "$12$ octets", "$5$ octets", "$20$ octets"], "bonne": 3},
    {"notion": "pile", "type": "vf", "q": "Avec `MOVEM.L liste,-(A7)`, D0 (s'il est dans la liste) est empilé en dernier : il se retrouve au sommet de la pile.", "bonne": True},
    {"notion": "pile", "type": "vf", "q": "On peut empiler un octet seul avec `MOVE.B D0,-(A7)` ; c'est la règle du cours.", "bonne": False},
    {"notion": "sousprog", "type": "qcm", "q": "L'instruction `RTS` :", "choix": ["branche à l'étiquette suivante", "vide la pile", "empile l'adresse de retour", "dépile l'adresse de retour dans PC"], "bonne": 3},
    {"notion": "sousprog", "type": "vf", "q": "`JSR` empile l'adresse de l'instruction qui suit le `JSR`.", "bonne": True},
    {"notion": "sousprog", "type": "vf", "q": "Si l'on appelle un sous-programme avec `JMP`, le `RTS` revient correctement à l'appelant.", "bonne": False},
    {"notion": "chaines", "type": "qcm", "q": "Quel est le code ASCII (en décimal) du caractère `'0'` ?", "choix": ["$57$", "$48$", "$30$", "$0$"], "bonne": 1},
    {"notion": "chaines", "type": "vf", "q": "Après `MOVE.B (A0)+,D1`, on peut tester l'octet nul avec `BEQ`, car `MOVE` met Z à jour.", "bonne": True},
    {"notion": "chaines", "type": "qcm", "q": "Pour obtenir la valeur $7$ à partir du caractère `'7'` dans D1.B :", "choix": ["`MULU.W #10,D1`", "`ADD.B #'0',D1`", "`SWAP D1`", "`SUB.B #'0',D1`"], "bonne": 3},
]

FORMULES = {
    "n11": r"valeur signée sur $n$ bits $=v-2^n$ si le bit de poids fort vaut $1$ · extension de signe : recopier le bit de poids fort · $N=\sum a_i\,16^i$",
    "n12": r"valeur signée sur $n$ bits $=v-2^n$ si le bit de poids fort vaut $1$ · extension de signe : recopier le bit de poids fort · $N=\sum a_i\,16^i$",
    "n13": r"valeur signée sur $n$ bits $=v-2^n$ si le bit de poids fort vaut $1$ · extension de signe : recopier le bit de poids fort · $N=\sum a_i\,16^i$",
    "n14": r"valeur signée sur $n$ bits $=v-2^n$ si le bit de poids fort vaut $1$ · extension de signe : recopier le bit de poids fort · $N=\sum a_i\,16^i$",
    "n15": r"valeur signée sur $n$ bits $=v-2^n$ si le bit de poids fort vaut $1$ · extension de signe : recopier le bit de poids fort · $N=\sum a_i\,16^i$",
    "n16": r"valeur signée sur $n$ bits $=v-2^n$ si le bit de poids fort vaut $1$ · extension de signe : recopier le bit de poids fort · $N=\sum a_i\,16^i$",
    "n17": r"valeur signée sur $n$ bits $=v-2^n$ si le bit de poids fort vaut $1$ · extension de signe : recopier le bit de poids fort · $N=\sum a_i\,16^i$",
    "n18": r"valeur signée sur $n$ bits $=v-2^n$ si le bit de poids fort vaut $1$ · extension de signe : recopier le bit de poids fort · $N=\sum a_i\,16^i$",
    "m21": r"$24$ fils d'adresse : $2^{24}$ octets · big-endian : octet de poids fort à l'adresse la plus basse · mot et mot long : adresse paire · `DS` : adresse suivante $=$ adresse $+$ nombre $\times$ taille",
    "m22": r"$24$ fils d'adresse : $2^{24}$ octets · big-endian : octet de poids fort à l'adresse la plus basse · mot et mot long : adresse paire · `DS` : adresse suivante $=$ adresse $+$ nombre $\times$ taille",
    "m23": r"$24$ fils d'adresse : $2^{24}$ octets · big-endian : octet de poids fort à l'adresse la plus basse · mot et mot long : adresse paire · `DS` : adresse suivante $=$ adresse $+$ nombre $\times$ taille",
    "m24": r"$24$ fils d'adresse : $2^{24}$ octets · big-endian : octet de poids fort à l'adresse la plus basse · mot et mot long : adresse paire · `DS` : adresse suivante $=$ adresse $+$ nombre $\times$ taille",
    "m25": r"$24$ fils d'adresse : $2^{24}$ octets · big-endian : octet de poids fort à l'adresse la plus basse · mot et mot long : adresse paire · `DS` : adresse suivante $=$ adresse $+$ nombre $\times$ taille",
    "m27": r"$24$ fils d'adresse : $2^{24}$ octets · big-endian : octet de poids fort à l'adresse la plus basse · mot et mot long : adresse paire · `DS` : adresse suivante $=$ adresse $+$ nombre $\times$ taille",
    "m26": r"$24$ fils d'adresse : $2^{24}$ octets · big-endian : octet de poids fort à l'adresse la plus basse · mot et mot long : adresse paire · `DS` : adresse suivante $=$ adresse $+$ nombre $\times$ taille",
    "r31": "$8$ registres D (32 bits) · $8$ registres A (32 bits, $24$ bits utiles) · A7 $=$ SSP ou USP · SR $=16$ bits, CCR $=$ octet de poids faible · instruction : $2$ à $10$ octets",
    "r32": "$8$ registres D (32 bits) · $8$ registres A (32 bits, $24$ bits utiles) · A7 $=$ SSP ou USP · SR $=16$ bits, CCR $=$ octet de poids faible · instruction : $2$ à $10$ octets",
    "r33": "$8$ registres D (32 bits) · $8$ registres A (32 bits, $24$ bits utiles) · A7 $=$ SSP ou USP · SR $=16$ bits, CCR $=$ octet de poids faible · instruction : $2$ à $10$ octets",
    "r34": "$8$ registres D (32 bits) · $8$ registres A (32 bits, $24$ bits utiles) · A7 $=$ SSP ou USP · SR $=16$ bits, CCR $=$ octet de poids faible · instruction : $2$ à $10$ octets",
    "r35": "$8$ registres D (32 bits) · $8$ registres A (32 bits, $24$ bits utiles) · A7 $=$ SSP ou USP · SR $=16$ bits, CCR $=$ octet de poids faible · instruction : $2$ à $10$ octets",
    "r36": "$8$ registres D (32 bits) · $8$ registres A (32 bits, $24$ bits utiles) · A7 $=$ SSP ou USP · SR $=16$ bits, CCR $=$ octet de poids faible · instruction : $2$ à $10$ octets",
    "r37": "$8$ registres D (32 bits) · $8$ registres A (32 bits, $24$ bits utiles) · A7 $=$ SSP ou USP · SR $=16$ bits, CCR $=$ octet de poids faible · instruction : $2$ à $10$ octets",
    "s41": "`.B` $=8$ bits, `.W` $=16$, `.L` $=32$ · seuls les bits de la taille changent · `MOVEQ` : entier signé de $8$ bits étendu à $32$ · `EXT.W` : octet vers mot, `EXT.L` : mot vers mot long",
    "s42": "`.B` $=8$ bits, `.W` $=16$, `.L` $=32$ · seuls les bits de la taille changent · `MOVEQ` : entier signé de $8$ bits étendu à $32$ · `EXT.W` : octet vers mot, `EXT.L` : mot vers mot long",
    "s43": "`.B` $=8$ bits, `.W` $=16$, `.L` $=32$ · seuls les bits de la taille changent · `MOVEQ` : entier signé de $8$ bits étendu à $32$ · `EXT.W` : octet vers mot, `EXT.L` : mot vers mot long",
    "s44": "`.B` $=8$ bits, `.W` $=16$, `.L` $=32$ · seuls les bits de la taille changent · `MOVEQ` : entier signé de $8$ bits étendu à $32$ · `EXT.W` : octet vers mot, `EXT.L` : mot vers mot long",
    "s45": "`.B` $=8$ bits, `.W` $=16$, `.L` $=32$ · seuls les bits de la taille changent · `MOVEQ` : entier signé de $8$ bits étendu à $32$ · `EXT.W` : octet vers mot, `EXT.L` : mot vers mot long",
    "s46": "`.B` $=8$ bits, `.W` $=16$, `.L` $=32$ · seuls les bits de la taille changent · `MOVEQ` : entier signé de $8$ bits étendu à $32$ · `EXT.W` : octet vers mot, `EXT.L` : mot vers mot long",
    "s47": "`.B` $=8$ bits, `.W` $=16$, `.L` $=32$ · seuls les bits de la taille changent · `MOVEQ` : entier signé de $8$ bits étendu à $32$ · `EXT.W` : octet vers mot, `EXT.L` : mot vers mot long",
    "s48": "`.B` $=8$ bits, `.W` $=16$, `.L` $=32$ · seuls les bits de la taille changent · `MOVEQ` : entier signé de $8$ bits étendu à $32$ · `EXT.W` : octet vers mot, `EXT.L` : mot vers mot long",
    "s49": "`.B` $=8$ bits, `.W` $=16$, `.L` $=32$ · seuls les bits de la taille changent · `MOVEQ` : entier signé de $8$ bits étendu à $32$ · `EXT.W` : octet vers mot, `EXT.L` : mot vers mot long",
    "f51": r"résultat $=(a\pm b)\bmod 2^n$ · N : bit $n-1$ du résultat · Z : résultat $=0$ · C : retenue (ou emprunt) · V : $+,+\to-$ ou $-,-\to+$",
    "f52": r"résultat $=(a\pm b)\bmod 2^n$ · N : bit $n-1$ du résultat · Z : résultat $=0$ · C : retenue (ou emprunt) · V : $+,+\to-$ ou $-,-\to+$",
    "f53": r"résultat $=(a\pm b)\bmod 2^n$ · N : bit $n-1$ du résultat · Z : résultat $=0$ · C : retenue (ou emprunt) · V : $+,+\to-$ ou $-,-\to+$",
    "f54": r"résultat $=(a\pm b)\bmod 2^n$ · N : bit $n-1$ du résultat · Z : résultat $=0$ · C : retenue (ou emprunt) · V : $+,+\to-$ ou $-,-\to+$",
    "f55": r"résultat $=(a\pm b)\bmod 2^n$ · N : bit $n-1$ du résultat · Z : résultat $=0$ · C : retenue (ou emprunt) · V : $+,+\to-$ ou $-,-\to+$",
    "f56": r"résultat $=(a\pm b)\bmod 2^n$ · N : bit $n-1$ du résultat · Z : résultat $=0$ · C : retenue (ou emprunt) · V : $+,+\to-$ ou $-,-\to+$",
    "f57": r"résultat $=(a\pm b)\bmod 2^n$ · N : bit $n-1$ du résultat · Z : résultat $=0$ · C : retenue (ou emprunt) · V : $+,+\to-$ ou $-,-\to+$",
    "f58": r"résultat $=(a\pm b)\bmod 2^n$ · N : bit $n-1$ du résultat · Z : résultat $=0$ · C : retenue (ou emprunt) · V : $+,+\to-$ ou $-,-\to+$",
    "f59": r"résultat $=(a\pm b)\bmod 2^n$ · N : bit $n-1$ du résultat · Z : résultat $=0$ · C : retenue (ou emprunt) · V : $+,+\to-$ ou $-,-\to+$",
    "f510": r"résultat $=(a\pm b)\bmod 2^n$ · N : bit $n-1$ du résultat · Z : résultat $=0$ · C : retenue (ou emprunt) · V : $+,+\to-$ ou $-,-\to+$",
    "f511": r"résultat $=(a\pm b)\bmod 2^n$ · N : bit $n-1$ du résultat · Z : résultat $=0$ · C : retenue (ou emprunt) · V : $+,+\to-$ ou $-,-\to+$",
    "a61": "`(An)+` : adresse $=$ An puis An $+=$ taille · `-(An)` : An $-=$ taille puis adresse $=$ An · taille $1,2,4$ pour `.B .W .L` · Dn, An et `#` : pas d'adresse mémoire",
    "a62": "`(An)+` : adresse $=$ An puis An $+=$ taille · `-(An)` : An $-=$ taille puis adresse $=$ An · taille $1,2,4$ pour `.B .W .L` · Dn, An et `#` : pas d'adresse mémoire",
    "a63": "`(An)+` : adresse $=$ An puis An $+=$ taille · `-(An)` : An $-=$ taille puis adresse $=$ An · taille $1,2,4$ pour `.B .W .L` · Dn, An et `#` : pas d'adresse mémoire",
    "a64": "`(An)+` : adresse $=$ An puis An $+=$ taille · `-(An)` : An $-=$ taille puis adresse $=$ An · taille $1,2,4$ pour `.B .W .L` · Dn, An et `#` : pas d'adresse mémoire",
    "a65": "`(An)+` : adresse $=$ An puis An $+=$ taille · `-(An)` : An $-=$ taille puis adresse $=$ An · taille $1,2,4$ pour `.B .W .L` · Dn, An et `#` : pas d'adresse mémoire · la source est évaluée avant la destination",
    "a66": "`(An)+` : adresse $=$ An puis An $+=$ taille · `-(An)` : An $-=$ taille puis adresse $=$ An · taille $1,2,4$ pour `.B .W .L` · Dn, An et `#` : pas d'adresse mémoire",
    "e71": r"`d16(An)` : $\text{An}+d_{16}$ · `d8(An,Xn)` : $\text{An}+d_8+X_n$ · index `.W` : mot étendu en signe · `.L` : $32$ bits · adresse impaire avec `.W` ou `.L` : erreur",
    "e72": r"`d16(An)` : $\text{An}+d_{16}$ · `d8(An,Xn)` : $\text{An}+d_8+X_n$ · index `.W` : mot étendu en signe · `.L` : $32$ bits · adresse impaire avec `.W` ou `.L` : erreur",
    "e73": r"`d16(An)` : $\text{An}+d_{16}$ · `d8(An,Xn)` : $\text{An}+d_8+X_n$ · index `.W` : mot étendu en signe · `.L` : $32$ bits · adresse impaire avec `.W` ou `.L` : erreur",
    "e74": r"`d16(An)` : $\text{An}+d_{16}$ · `d8(An,Xn)` : $\text{An}+d_8+X_n$ · index `.W` : mot étendu en signe · `.L` : $32$ bits · adresse impaire avec `.W` ou `.L` : erreur",
    "e75": r"`d16(An)` : $\text{An}+d_{16}$ · `d8(An,Xn)` : $\text{An}+d_8+X_n$ · index `.W` : mot étendu en signe · `.L` : $32$ bits · adresse impaire avec `.W` ou `.L` : erreur",
    "e76": r"`d16(An)` : $\text{An}+d_{16}$ · `d8(An,Xn)` : $\text{An}+d_8+X_n$ · index `.W` : mot étendu en signe · `.L` : $32$ bits · adresse impaire avec `.W` ou `.L` : erreur",
    "e77": r"`d16(An)` : $\text{An}+d_{16}$ · `d8(An,Xn)` : $\text{An}+d_8+X_n$ · index `.W` : mot étendu en signe · `.L` : $32$ bits · adresse impaire avec `.W` ou `.L` : erreur",
    "e78": r"`d16(An)` : $\text{An}+d_{16}$ · `d8(An,Xn)` : $\text{An}+d_8+X_n$ · index `.W` : mot étendu en signe · `.L` : $32$ bits · adresse impaire avec `.W` ou `.L` : erreur",
    "e79": r"`d16(An)` : $\text{An}+d_{16}$ · `d8(An,Xn)` : $\text{An}+d_8+X_n$ · index `.W` : mot étendu en signe · `.L` : $32$ bits · adresse impaire avec `.W` ou `.L` : erreur",
    "g81": "source évaluée d'abord, puis destination · big-endian · taille $1,2,4$ · `(An)+`, `-(An)` modifient An · les octets voisins ne changent pas",
    "g82": "source évaluée d'abord, puis destination · big-endian · taille $1,2,4$ · `(An)+`, `-(An)` modifient An · les octets voisins ne changent pas",
    "g83": "source évaluée d'abord, puis destination · big-endian · taille $1,2,4$ · `(An)+`, `-(An)` modifient An · les octets voisins ne changent pas",
    "g84": "source évaluée d'abord, puis destination · big-endian · taille $1,2,4$ · `(An)+`, `-(An)` modifient An · les octets voisins ne changent pas",
    "g85": "source évaluée d'abord, puis destination · big-endian · taille $1,2,4$ · `(An)+`, `-(An)` modifient An · les octets voisins ne changent pas",
    "g86": "source évaluée d'abord, puis destination · big-endian · taille $1,2,4$ · `(An)+`, `-(An)` modifient An · les octets voisins ne changent pas",
    "g87": "source évaluée d'abord, puis destination · big-endian · taille $1,2,4$ · `(An)+`, `-(An)` modifient An · les octets voisins ne changent pas",
    "g88": "source évaluée d'abord, puis destination · big-endian · taille $1,2,4$ · `(An)+`, `-(An)` modifient An · les octets voisins ne changent pas",
    "ar91": r"seule la partie `.s` du registre change · `ADDQ`/`SUBQ` : constante de $1$ à $8$ · `NEG` : $0-$dest · `NOT` : tous les bits inversés · `MULU.W` : D.W $\times$ source.W sur $32$ bits · `DIVU.W` : quotient (bits $15$ à $0$), reste (bits $31$ à $16$) · `ADDX` ajoute X",
    "ar92": r"seule la partie `.s` du registre change · `ADDQ`/`SUBQ` : constante de $1$ à $8$ · `NEG` : $0-$dest · `NOT` : tous les bits inversés · `MULU.W` : D.W $\times$ source.W sur $32$ bits · `DIVU.W` : quotient (bits $15$ à $0$), reste (bits $31$ à $16$) · `ADDX` ajoute X",
    "ar93": r"seule la partie `.s` du registre change · `ADDQ`/`SUBQ` : constante de $1$ à $8$ · `NEG` : $0-$dest · `NOT` : tous les bits inversés · `MULU.W` : D.W $\times$ source.W sur $32$ bits · `DIVU.W` : quotient (bits $15$ à $0$), reste (bits $31$ à $16$) · `ADDX` ajoute X",
    "ar94": r"seule la partie `.s` du registre change · `ADDQ`/`SUBQ` : constante de $1$ à $8$ · `NEG` : $0-$dest · `NOT` : tous les bits inversés · `MULU.W` : D.W $\times$ source.W sur $32$ bits · `DIVU.W` : quotient (bits $15$ à $0$), reste (bits $31$ à $16$) · `ADDX` ajoute X",
    "ar95": r"seule la partie `.s` du registre change · `ADDQ`/`SUBQ` : constante de $1$ à $8$ · `NEG` : $0-$dest · `NOT` : tous les bits inversés · `MULU.W` : D.W $\times$ source.W sur $32$ bits · `DIVU.W` : quotient (bits $15$ à $0$), reste (bits $31$ à $16$) · `ADDX` ajoute X",
    "ar96": r"seule la partie `.s` du registre change · `ADDQ`/`SUBQ` : constante de $1$ à $8$ · `NEG` : $0-$dest · `NOT` : tous les bits inversés · `MULU.W` : D.W $\times$ source.W sur $32$ bits · `DIVU.W` : quotient (bits $15$ à $0$), reste (bits $31$ à $16$) · `ADDX` ajoute X",
    "ar97": r"seule la partie `.s` du registre change · `ADDQ`/`SUBQ` : constante de $1$ à $8$ · `NEG` : $0-$dest · `NOT` : tous les bits inversés · `MULU.W` : D.W $\times$ source.W sur $32$ bits · `DIVU.W` : quotient (bits $15$ à $0$), reste (bits $31$ à $16$) · `ADDX` ajoute X",
    "ar98": r"seule la partie `.s` du registre change · `ADDQ`/`SUBQ` : constante de $1$ à $8$ · `NEG` : $0-$dest · `NOT` : tous les bits inversés · `MULU.W` : D.W $\times$ source.W sur $32$ bits · `DIVU.W` : quotient (bits $15$ à $0$), reste (bits $31$ à $16$) · `ADDX` ajoute X",
    "ar99": r"seule la partie `.s` du registre change · `ADDQ`/`SUBQ` : constante de $1$ à $8$ · `NEG` : $0-$dest · `NOT` : tous les bits inversés · `MULU.W` : D.W $\times$ source.W sur $32$ bits · `DIVU.W` : quotient (bits $15$ à $0$), reste (bits $31$ à $16$) · `ADDX` ajoute X",
    "ro101": "`ROR.s #k` fait tourner les $8$, $16$ ou $32$ bits de poids faible vers la droite · `ROL.s #k` vers la gauche · `SWAP` échange les deux mots · $4$ bits $=$ un chiffre hexa",
    "ro102": "`ROR.s #k` fait tourner les $8$, $16$ ou $32$ bits de poids faible vers la droite · `ROL.s #k` vers la gauche · `SWAP` échange les deux mots · $4$ bits $=$ un chiffre hexa",
    "ro103": "`ROR.s #k` fait tourner les $8$, $16$ ou $32$ bits de poids faible vers la droite · `ROL.s #k` vers la gauche · `SWAP` échange les deux mots · $4$ bits $=$ un chiffre hexa",
    "ro104": "`ROR.s #k` fait tourner les $8$, $16$ ou $32$ bits de poids faible vers la droite · `ROL.s #k` vers la gauche · `SWAP` échange les deux mots · $4$ bits $=$ un chiffre hexa",
    "ro105": "`ROR.s #k` fait tourner les $8$, $16$ ou $32$ bits de poids faible vers la droite · `ROL.s #k` vers la gauche · `SWAP` échange les deux mots · $4$ bits $=$ un chiffre hexa",
    "ro106": "`ROR.s #k` fait tourner les $8$, $16$ ou $32$ bits de poids faible vers la droite · `ROL.s #k` vers la gauche · `SWAP` échange les deux mots · $4$ bits $=$ un chiffre hexa",
    "ro107": "`ROR.s #k` fait tourner les $8$, $16$ ou $32$ bits de poids faible vers la droite · `ROL.s #k` vers la gauche · `SWAP` échange les deux mots · $4$ bits $=$ un chiffre hexa",
    "ro108": "`ROR.s #k` fait tourner les $8$, $16$ ou $32$ bits de poids faible vers la droite · `ROL.s #k` vers la gauche · `SWAP` échange les deux mots · $4$ bits $=$ un chiffre hexa",
    "ro109": "`ROR.s #k` fait tourner les $8$, $16$ ou $32$ bits de poids faible vers la droite · `ROL.s #k` vers la gauche · `SWAP` échange les deux mots · $4$ bits $=$ un chiffre hexa",
    "b111": "`TST.s` : N, Z d'après l'opérande · `CMP.s S,D` : $D-S$ · `BEQ` $Z=1$, `BNE` $Z=0$, `BMI` $N=1$, `BPL` $N=0$ · signé : `BGT BGE BLT BLE` · non signé : `BHI BHS BLO BLS` · la taille `.s` limite la comparaison aux bits de poids faible",
    "b112": "`TST.s` : N, Z d'après l'opérande · `CMP.s S,D` : $D-S$ · `BEQ` $Z=1$, `BNE` $Z=0$, `BMI` $N=1$, `BPL` $N=0$ · signé : `BGT BGE BLT BLE` · non signé : `BHI BHS BLO BLS` · la taille `.s` limite la comparaison aux bits de poids faible",
    "b113": "`TST.s` : N, Z d'après l'opérande · `CMP.s S,D` : $D-S$ · `BEQ` $Z=1$, `BNE` $Z=0$, `BMI` $N=1$, `BPL` $N=0$ · signé : `BGT BGE BLT BLE` · non signé : `BHI BHS BLO BLS` · la taille `.s` limite la comparaison aux bits de poids faible",
    "b114": "`TST.s` : N, Z d'après l'opérande · `CMP.s S,D` : $D-S$ · `BEQ` $Z=1$, `BNE` $Z=0$, `BMI` $N=1$, `BPL` $N=0$ · signé : `BGT BGE BLT BLE` · non signé : `BHI BHS BLO BLS` · la taille `.s` limite la comparaison aux bits de poids faible",
    "b115": "`TST.s` : N, Z d'après l'opérande · `CMP.s S,D` : $D-S$ · `BEQ` $Z=1$, `BNE` $Z=0$, `BMI` $N=1$, `BPL` $N=0$ · signé : `BGT BGE BLT BLE` · non signé : `BHI BHS BLO BLS` · la taille `.s` limite la comparaison aux bits de poids faible",
    "b116": "`TST.s` : N, Z d'après l'opérande · `CMP.s S,D` : $D-S$ · `BEQ` $Z=1$, `BNE` $Z=0$, `BMI` $N=1$, `BPL` $N=0$ · signé : `BGT BGE BLT BLE` · non signé : `BHI BHS BLO BLS` · la taille `.s` limite la comparaison aux bits de poids faible",
    "b117": "`TST.s` : N, Z d'après l'opérande · `CMP.s S,D` : $D-S$ · `BEQ` $Z=1$, `BNE` $Z=0$, `BMI` $N=1$, `BPL` $N=0$ · signé : `BGT BGE BLT BLE` · non signé : `BHI BHS BLO BLS` · la taille `.s` limite la comparaison aux bits de poids faible",
    "b118": "`TST.s` : N, Z d'après l'opérande · `CMP.s S,D` : $D-S$ · `BEQ` $Z=1$, `BNE` $Z=0$, `BMI` $N=1$, `BPL` $N=0$ · signé : `BGT BGE BLT BLE` · non signé : `BHI BHS BLO BLS` · la taille `.s` limite la comparaison aux bits de poids faible",
    "b119": "`TST.s` : N, Z d'après l'opérande · `CMP.s S,D` : $D-S$ · `BEQ` $Z=1$, `BNE` $Z=0$, `BMI` $N=1$, `BPL` $N=0$ · signé : `BGT BGE BLT BLE` · non signé : `BHI BHS BLO BLS` · la taille `.s` limite la comparaison aux bits de poids faible",
    "l121": r"`SUBQ.s #k` + `BNE` : seule la partie `.s` compte, tours $=\dfrac{D_n.s}{k}$ ($2^{\text{taille}}/k$ si elle vaut $0$) · `DBRA` : $D_n.W+1$ tours · `CMPI` + `BNE` : tours $=$ valeur d'arrivée $-$ valeur de départ",
    "l122": r"`SUBQ.s #k` + `BNE` : seule la partie `.s` compte, tours $=\dfrac{D_n.s}{k}$ ($2^{\text{taille}}/k$ si elle vaut $0$) · `DBRA` : $D_n.W+1$ tours · `CMPI` + `BNE` : tours $=$ valeur d'arrivée $-$ valeur de départ",
    "l123": r"`SUBQ.s #k` + `BNE` : seule la partie `.s` compte, tours $=\dfrac{D_n.s}{k}$ ($2^{\text{taille}}/k$ si elle vaut $0$) · `DBRA` : $D_n.W+1$ tours · `CMPI` + `BNE` : tours $=$ valeur d'arrivée $-$ valeur de départ",
    "l124": r"`SUBQ.s #k` + `BNE` : seule la partie `.s` compte, tours $=\dfrac{D_n.s}{k}$ ($2^{\text{taille}}/k$ si elle vaut $0$) · `DBRA` : $D_n.W+1$ tours · `CMPI` + `BNE` : tours $=$ valeur d'arrivée $-$ valeur de départ",
    "l125": r"`SUBQ.s #k` + `BNE` : seule la partie `.s` compte, tours $=\dfrac{D_n.s}{k}$ ($2^{\text{taille}}/k$ si elle vaut $0$) · `DBRA` : $D_n.W+1$ tours · `CMPI` + `BNE` : tours $=$ valeur d'arrivée $-$ valeur de départ",
    "l126": r"`SUBQ.s #k` + `BNE` : seule la partie `.s` compte, tours $=\dfrac{D_n.s}{k}$ ($2^{\text{taille}}/k$ si elle vaut $0$) · `DBRA` : $D_n.W+1$ tours · `CMPI` + `BNE` : tours $=$ valeur d'arrivée $-$ valeur de départ",
    "l127": r"`SUBQ.s #k` + `BNE` : seule la partie `.s` compte, tours $=\dfrac{D_n.s}{k}$ ($2^{\text{taille}}/k$ si elle vaut $0$) · `DBRA` : $D_n.W+1$ tours · `CMPI` + `BNE` : tours $=$ valeur d'arrivée $-$ valeur de départ",
    "l128": r"`SUBQ.s #k` + `BNE` : seule la partie `.s` compte, tours $=\dfrac{D_n.s}{k}$ ($2^{\text{taille}}/k$ si elle vaut $0$) · `DBRA` : $D_n.W+1$ tours · `CMPI` + `BNE` : tours $=$ valeur d'arrivée $-$ valeur de départ",
    "p131": r"empiler : A7 diminue (`.W` : $2$, `.L` : $4$) puis écriture · dépiler : lecture puis A7 augmente · `MOVEM.L liste,-(A7)` : $4\times$ nombre de registres, D0 au sommet · `JSR`/`BSR` : A7 $-4$ · `RTS` : A7 $+4$",
    "p132": r"empiler : A7 diminue (`.W` : $2$, `.L` : $4$) puis écriture · dépiler : lecture puis A7 augmente · `MOVEM.L liste,-(A7)` : $4\times$ nombre de registres, D0 au sommet · `JSR`/`BSR` : A7 $-4$ · `RTS` : A7 $+4$",
    "p133": r"empiler : A7 diminue (`.W` : $2$, `.L` : $4$) puis écriture · dépiler : lecture puis A7 augmente · `MOVEM.L liste,-(A7)` : $4\times$ nombre de registres, D0 au sommet · `JSR`/`BSR` : A7 $-4$ · `RTS` : A7 $+4$",
    "p134": r"empiler : A7 diminue (`.W` : $2$, `.L` : $4$) puis écriture · dépiler : lecture puis A7 augmente · `MOVEM.L liste,-(A7)` : $4\times$ nombre de registres, D0 au sommet · `JSR`/`BSR` : A7 $-4$ · `RTS` : A7 $+4$",
    "p135": r"empiler : A7 diminue (`.W` : $2$, `.L` : $4$) puis écriture · dépiler : lecture puis A7 augmente · `MOVEM.L liste,-(A7)` : $4\times$ nombre de registres, D0 au sommet · `JSR`/`BSR` : A7 $-4$ · `RTS` : A7 $+4$",
    "p136": r"empiler : A7 diminue (`.W` : $2$, `.L` : $4$) puis écriture · dépiler : lecture puis A7 augmente · `MOVEM.L liste,-(A7)` : $4\times$ nombre de registres, D0 au sommet · `JSR`/`BSR` : A7 $-4$ · `RTS` : A7 $+4$",
    "p137": r"empiler : A7 diminue (`.W` : $2$, `.L` : $4$) puis écriture · dépiler : lecture puis A7 augmente · `MOVEM.L liste,-(A7)` : $4\times$ nombre de registres, D0 au sommet · `JSR`/`BSR` : A7 $-4$ · `RTS` : A7 $+4$",
    "p138": r"empiler : A7 diminue (`.W` : $2$, `.L` : $4$) puis écriture · dépiler : lecture puis A7 augmente · `MOVEM.L liste,-(A7)` : $4\times$ nombre de registres, D0 au sommet · `JSR`/`BSR` : A7 $-4$ · `RTS` : A7 $+4$",
    "p139": r"empiler : A7 diminue (`.W` : $2$, `.L` : $4$) puis écriture · dépiler : lecture puis A7 augmente · `MOVEM.L liste,-(A7)` : $4\times$ nombre de registres, D0 au sommet · `JSR`/`BSR` : A7 $-4$ · `RTS` : A7 $+4$",
    "p1310": r"empiler : A7 diminue (`.W` : $2$, `.L` : $4$) puis écriture · dépiler : lecture puis A7 augmente · `MOVEM.L liste,-(A7)` : $4\times$ nombre de registres, D0 au sommet · `JSR`/`BSR` : A7 $-4$ · `RTS` : A7 $+4$",
    "sp141": "`JSR`/`BSR` : empile l'adresse de retour puis saute · `RTS` : dépile dans PC · paramètres et résultats dans des registres · sauvegarder avec `MOVEM.L liste,-(A7)` et restaurer avec `MOVEM.L (A7)+,liste` · `CMP S,D` + `Bcc` : D condition S",
    "sp142": "`JSR`/`BSR` : empile l'adresse de retour puis saute · `RTS` : dépile dans PC · paramètres et résultats dans des registres · sauvegarder avec `MOVEM.L liste,-(A7)` et restaurer avec `MOVEM.L (A7)+,liste` · `CMP S,D` + `Bcc` : D condition S",
    "sp143": "`JSR`/`BSR` : empile l'adresse de retour puis saute · `RTS` : dépile dans PC · paramètres et résultats dans des registres · sauvegarder avec `MOVEM.L liste,-(A7)` et restaurer avec `MOVEM.L (A7)+,liste` · `CMP S,D` + `Bcc` : D condition S",
    "sp144": "`JSR`/`BSR` : empile l'adresse de retour puis saute · `RTS` : dépile dans PC · paramètres et résultats dans des registres · sauvegarder avec `MOVEM.L liste,-(A7)` et restaurer avec `MOVEM.L (A7)+,liste` · `CMP S,D` + `Bcc` : D condition S",
    "sp145": "`JSR`/`BSR` : empile l'adresse de retour puis saute · `RTS` : dépile dans PC · paramètres et résultats dans des registres · sauvegarder avec `MOVEM.L liste,-(A7)` et restaurer avec `MOVEM.L (A7)+,liste` · `CMP S,D` + `Bcc` : D condition S",
    "sp146": "`JSR`/`BSR` : empile l'adresse de retour puis saute · `RTS` : dépile dans PC · paramètres et résultats dans des registres · sauvegarder avec `MOVEM.L liste,-(A7)` et restaurer avec `MOVEM.L (A7)+,liste` · `CMP S,D` + `Bcc` : D condition S",
    "ch151": "chaîne $=$ octets ASCII + octet nul · `'0'`$=48$, `'A'`$=65$, `'a'`$=97$, espace $=32$, tabulation $=9$ · `MOVE.B (A0)+,D1` puis `BEQ` : fin de chaîne · valeur d'un chiffre : `SUB.B #'0',D1`",
    "ch152": "chaîne $=$ octets ASCII + octet nul · `'0'`$=48$, `'A'`$=65$, `'a'`$=97$, espace $=32$, tabulation $=9$ · `MOVE.B (A0)+,D1` puis `BEQ` : fin de chaîne · valeur d'un chiffre : `SUB.B #'0',D1`",
    "ch153": "chaîne $=$ octets ASCII + octet nul · `'0'`$=48$, `'A'`$=65$, `'a'`$=97$, espace $=32$, tabulation $=9$ · `MOVE.B (A0)+,D1` puis `BEQ` : fin de chaîne · valeur d'un chiffre : `SUB.B #'0',D1`",
    "ch154": "chaîne $=$ octets ASCII + octet nul · `'0'`$=48$, `'A'`$=65$, `'a'`$=97$, espace $=32$, tabulation $=9$ · `MOVE.B (A0)+,D1` puis `BEQ` : fin de chaîne · valeur d'un chiffre : `SUB.B #'0',D1`",
    "ch155": "chaîne $=$ octets ASCII + octet nul · `'0'`$=48$, `'A'`$=65$, `'a'`$=97$, espace $=32$, tabulation $=9$ · `MOVE.B (A0)+,D1` puis `BEQ` : fin de chaîne · valeur d'un chiffre : `SUB.B #'0',D1`",
    "ch156": "chaîne $=$ octets ASCII + octet nul · `'0'`$=48$, `'A'`$=65$, `'a'`$=97$, espace $=32$, tabulation $=9$ · `MOVE.B (A0)+,D1` puis `BEQ` : fin de chaîne · valeur d'un chiffre : `SUB.B #'0',D1`",
    "ch157": "chaîne $=$ octets ASCII + octet nul · `'0'`$=48$, `'A'`$=65$, `'a'`$=97$, espace $=32$, tabulation $=9$ · `MOVE.B (A0)+,D1` puis `BEQ` : fin de chaîne · valeur d'un chiffre : `SUB.B #'0',D1`",
    "ch158": "chaîne $=$ octets ASCII + octet nul · `'0'`$=48$, `'A'`$=65$, `'a'`$=97$, espace $=32$, tabulation $=9$ · `MOVE.B (A0)+,D1` puis `BEQ` : fin de chaîne · valeur d'un chiffre : `SUB.B #'0',D1`",
    "ch159": "chaîne $=$ octets ASCII + octet nul · `'0'`$=48$, `'A'`$=65$, `'a'`$=97$, espace $=32$, tabulation $=9$ · `MOVE.B (A0)+,D1` puis `BEQ` : fin de chaîne · valeur d'un chiffre : `SUB.B #'0',D1`",
    "ch1510": "chaîne $=$ octets ASCII + octet nul · `'0'`$=48$, `'A'`$=65$, `'a'`$=97$, espace $=32$, tabulation $=9$ · `MOVE.B (A0)+,D1` puis `BEQ` : fin de chaîne · valeur d'un chiffre : `SUB.B #'0',D1`",
    "x1a": "source évaluée d'abord, puis destination · big-endian · taille $1,2,4$ · `(An)+`, `-(An)` modifient An · les octets voisins ne changent pas",
    "x1b": "`-(An)` : An diminue de la taille avant l'accès",
    "x1c": "source évaluée d'abord, puis destination · big-endian · taille $1,2,4$ · `(An)+`, `-(An)` modifient An · les octets voisins ne changent pas",
    "x1d": "source évaluée d'abord, puis destination · big-endian · taille $1,2,4$ · `(An)+`, `-(An)` modifient An · les octets voisins ne changent pas",
    "x1e": "`(An)+` : An augmente de la taille après l'accès",
    "x1f": "source évaluée d'abord, puis destination · big-endian · taille $1,2,4$ · `(An)+`, `-(An)` modifient An · les octets voisins ne changent pas",
    "x2a": r"résultat $=(a\pm b)\bmod 2^n$ · N : bit $n-1$ du résultat · Z : résultat $=0$ · C : retenue (ou emprunt) · V : $+,+\to-$ ou $-,-\to+$",
    "x2b": r"résultat $=(a\pm b)\bmod 2^n$ · N : bit $n-1$ du résultat · Z : résultat $=0$ · C : retenue (ou emprunt) · V : $+,+\to-$ ou $-,-\to+$",
    "x2c": r"résultat $=(a\pm b)\bmod 2^n$ · N : bit $n-1$ du résultat · Z : résultat $=0$ · C : retenue (ou emprunt) · V : $+,+\to-$ ou $-,-\to+$",
    "x2d": r"résultat $=(a\pm b)\bmod 2^n$ · N : bit $n-1$ du résultat · Z : résultat $=0$ · C : retenue (ou emprunt) · V : $+,+\to-$ ou $-,-\to+$",
    "x2e": r"résultat $=(a\pm b)\bmod 2^n$ · N : bit $n-1$ du résultat · Z : résultat $=0$ · C : retenue (ou emprunt) · V : $+,+\to-$ ou $-,-\to+$",
    "x2f": r"résultat $=(a\pm b)\bmod 2^n$ · N : bit $n-1$ du résultat · Z : résultat $=0$ · C : retenue (ou emprunt) · V : $+,+\to-$ ou $-,-\to+$",
    "x2g": r"résultat $=(a\pm b)\bmod 2^n$ · N : bit $n-1$ du résultat · Z : résultat $=0$ · C : retenue (ou emprunt) · V : $+,+\to-$ ou $-,-\to+$",
    "x3": "`MOVE.L D0,-(A7)` · `MOVEM.L (A7)+,liste` · `JSR`/`BSR` · PC",
    "x4a": "`CMP.W` ne compare que le mot de poids faible · `BGT` : comparaison signée",
    "x4b": "`SUBQ.B #1` + `BNE` : tours $=$ D0.B",
    "x4c": "`DBRA` : D0.W $+1$ tours",
    "x4d": "`ROR.s #k` : rotation sur la taille $s$ · `SWAP` : échange les mots · `ROL.B #4` : échange les deux chiffres de l'octet",
    "y1a": "source évaluée d'abord, puis destination · big-endian · taille $1,2,4$ · `(An)+`, `-(An)` modifient An · les octets voisins ne changent pas",
    "y1b": "`-(An)` : An diminue de la taille avant l'accès",
    "y1c": "source évaluée d'abord, puis destination · big-endian · taille $1,2,4$ · `(An)+`, `-(An)` modifient An · les octets voisins ne changent pas",
    "y1d": "source évaluée d'abord, puis destination · big-endian · taille $1,2,4$ · `(An)+`, `-(An)` modifient An · les octets voisins ne changent pas",
    "y2a": r"résultat $=(a\pm b)\bmod 2^n$ · N : bit $n-1$ du résultat · Z : résultat $=0$ · C : retenue (ou emprunt) · V : $+,+\to-$ ou $-,-\to+$",
    "y2b": r"résultat $=(a\pm b)\bmod 2^n$ · N : bit $n-1$ du résultat · Z : résultat $=0$ · C : retenue (ou emprunt) · V : $+,+\to-$ ou $-,-\to+$",
    "y2c": r"résultat $=(a\pm b)\bmod 2^n$ · N : bit $n-1$ du résultat · Z : résultat $=0$ · C : retenue (ou emprunt) · V : $+,+\to-$ ou $-,-\to+$",
    "y2d": r"résultat $=(a\pm b)\bmod 2^n$ · N : bit $n-1$ du résultat · Z : résultat $=0$ · C : retenue (ou emprunt) · V : $+,+\to-$ ou $-,-\to+$",
    "y2e": r"résultat $=(a\pm b)\bmod 2^n$ · N : bit $n-1$ du résultat · Z : résultat $=0$ · C : retenue (ou emprunt) · V : $+,+\to-$ ou $-,-\to+$",
    "y2f": r"résultat $=(a\pm b)\bmod 2^n$ · N : bit $n-1$ du résultat · Z : résultat $=0$ · C : retenue (ou emprunt) · V : $+,+\to-$ ou $-,-\to+$",
    "y3a": "`CMPI.L` : $D-S$ sur $32$ bits · `BLT` : signé",
    "y3b": "`SUBI.B #1` + `BNE` : tours $=$ D0.B",
    "y3c": "`ADDI.W` · `DBRA` : D7.W $+1$ tours",
    "px4": "`ROR.s #k` fait tourner les $8$, $16$ ou $32$ bits de poids faible vers la droite · `ROL.s #k` vers la gauche · `SWAP` échange les deux mots · $4$ bits $=$ un chiffre hexa",
    "py5a": "`MOVE.B (A1)+,(A2)+` · `SUBQ.L #1,D0` + `BNE` · `MOVEM` pour sauvegarder",
    "py5b": "`-(A1)` et `-(A2)` : prédécrémentation · `ADDA.L D0,A1`",
    "py5c": "`CMPA.L A1,A2` puis `BLO` (non signé) · `JSR` / `RTS`",
    "q1a": "`CMP.B (A0)+,D0` · `BNE` · `SUBQ.L #1,A0`",
    "q1b": "`CMP.B (A0)+,D0` · `BEQ` · `SUBQ.L #1,A0`",
    "q1c": "`SUBA.L D0,A0` : différence d'adresses · appels `JSR`",
    "q2a": "`TST.B (A0)+` puis `BNE`",
    "q2b": "`MOVE.B (A0),D0` + `BEQ` · `1(A0)` · `(A0)+`",
    "q2c": "appels `JSR` · `TST.B (A0)` + `BNE`",
    "q3a": "`CMPI.B #' ',D1` · `BEQ` · `MOVEQ.L`",
    "q3b": "`JSR IsBlank` · `TST.L D0` · compteur dans D2",
    "q3c": "`MOVE.B #'_',-1(A0)` · `JSR IsBlank` · `MOVEM`",
    "qd1": "`TST.L` · `BPL`",
    "qd2": "`TST.B` · `BMI`",
    "qd3": "`SUBQ.W #1` + `BNE` : tours $=$ D0.W",
    "qd4": "`DBRA` : D0.W $+1$ tours",
    "qd5": "`CMP.B` · `BGT` : signé",
    "qd6": "`BLS` : non signé",
    "h191": r"boucles imbriquées : tours $=$ tours externes $\times$ tours internes · récursivité : la pile garde l'adresse de retour et la donnée empilée · `MOVEA.W` étend le signe sur $32$ bits · `DIVU.W` : quotient (poids faible), reste (poids fort)",
    "h192": r"boucles imbriquées : tours $=$ tours externes $\times$ tours internes · récursivité : la pile garde l'adresse de retour et la donnée empilée · `MOVEA.W` étend le signe sur $32$ bits · `DIVU.W` : quotient (poids faible), reste (poids fort)",
    "h193": r"boucles imbriquées : tours $=$ tours externes $\times$ tours internes · récursivité : la pile garde l'adresse de retour et la donnée empilée · `MOVEA.W` étend le signe sur $32$ bits · `DIVU.W` : quotient (poids faible), reste (poids fort)",
    "h194": "`TST.B (A1)+` pour trouver la fin · `CMPA.L A1,A0` + `BHS` · échange par deux registres",
    "h195": "`DIVU.W #10,D0` · `SWAP` pour lire le reste · pile LIFO pour inverser · `MOVEM`",
    "h196": r"boucles imbriquées : tours $=$ tours externes $\times$ tours internes · récursivité : la pile garde l'adresse de retour et la donnée empilée · `MOVEA.W` étend le signe sur $32$ bits · `DIVU.W` : quotient (poids faible), reste (poids fort)",
    "h197": "empiler et dépiler avec la même taille · `(A7)+` augmente de la taille de l'instruction · `MULU.W` lit un mot",
    "z1a": "source évaluée d'abord, puis destination · big-endian · taille $1,2,4$ · `(An)+`, `-(An)` modifient An · les octets voisins ne changent pas",
    "z1b": "`-(An)` : An diminue de la taille avant l'accès",
    "z1c": "source évaluée d'abord, puis destination · big-endian · taille $1,2,4$ · `(An)+`, `-(An)` modifient An · les octets voisins ne changent pas",
    "z1d": "source évaluée d'abord, puis destination · big-endian · taille $1,2,4$ · `(An)+`, `-(An)` modifient An · les octets voisins ne changent pas",
    "z2a": r"résultat $=(a\pm b)\bmod 2^n$ · N : bit $n-1$ du résultat · Z : résultat $=0$ · C : retenue (ou emprunt) · V : $+,+\to-$ ou $-,-\to+$",
    "z2b": r"résultat $=(a\pm b)\bmod 2^n$ · N : bit $n-1$ du résultat · Z : résultat $=0$ · C : retenue (ou emprunt) · V : $+,+\to-$ ou $-,-\to+$",
    "z2c": r"résultat $=(a\pm b)\bmod 2^n$ · N : bit $n-1$ du résultat · Z : résultat $=0$ · C : retenue (ou emprunt) · V : $+,+\to-$ ou $-,-\to+$",
    "z2d": r"résultat $=(a\pm b)\bmod 2^n$ · N : bit $n-1$ du résultat · Z : résultat $=0$ · C : retenue (ou emprunt) · V : $+,+\to-$ ou $-,-\to+$",
    "z3a": "`TST.B` · `BMI`",
    "z3b": "`SUBQ.B #1` + `BNE` : tours $=$ D0.B",
    "z3c": "`DBRA` : D0.W $+1$ tours",
    "z4": "`CMPI.B #'0'` + `BLO` · `CMPI.B #'9'` + `BLS` · `MOVE.B (A0)+,D0` + `BEQ`",
    "f512": r"résultat $=(a\pm b)\bmod 2^n$ · N : bit $n-1$ du résultat · Z : résultat $=0$ · C : retenue (ou emprunt) · V : $+,+\to-$ ou $-,-\to+$ · plus petit $X$ : on cherche le premier résultat qui vérifie les quatre drapeaux",
    "f513": r"résultat $=(a\pm b)\bmod 2^n$ · N : bit $n-1$ du résultat · Z : résultat $=0$ · C : retenue (ou emprunt) · V : $+,+\to-$ ou $-,-\to+$ · plus petit $X$ : on cherche le premier résultat qui vérifie les quatre drapeaux",
    "f514": r"résultat $=(a\pm b)\bmod 2^n$ · N : bit $n-1$ du résultat · Z : résultat $=0$ · C : retenue (ou emprunt) · V : $+,+\to-$ ou $-,-\to+$ · plus petit $X$ : on cherche le premier résultat qui vérifie les quatre drapeaux",
    "f515": r"résultat $=(a\pm b)\bmod 2^n$ · N : bit $n-1$ du résultat · Z : résultat $=0$ · C : retenue (ou emprunt) · V : $+,+\to-$ ou $-,-\to+$ · plus petit $X$ : on cherche le premier résultat qui vérifie les quatre drapeaux",
}
