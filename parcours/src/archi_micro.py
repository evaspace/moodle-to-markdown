"""Level path: S2 computer architecture, microprocessor systems (memories, memory assembly, address decoding).

Calibrated on the Moodle course « Archi S2 2030 - ... » chapter 3 (`Chapitre_3.pdf`), TD3 (memory assembly), TD4 (address
decoding) and the exams `s2_exam4_fr` (2024/2025) and `b4_exam_fr` (2025/2026). Addresses are written in hexadecimal
(`hexa('...')` gives the value): the answer of an address exercise is the address itself, checked against an independent
computation (low address + size - 1). Overlines of the chip-select expressions are written `\\overline{A_i}`.
Conventions of the course: an unused microprocessor address bit is set to 0; `AS` (Address Strobe) must be 1 for any
component to be selected; the zone mode uses the high bits; the linear mode uses one selection bit per component.
TD5 (circuit drawing: RS latch, 74HCT193 counters, M2716 ROM, serial transmission) is not covered: schematics only.
"""

SUBJECT = {
    "id": "archi-s2-microprocesseur",
    "ordre": 440,
    "matiere": "archi",
    "semestre": "S2",
    "ecue": "Systèmes à microprocesseur",
    "titre": "Systèmes à microprocesseur : mémoires et décodage d'adresse",
    "chapitres_moodle": ["06_Les systèmes à microprocesseur (B4)", "07_Cours", "08_TD"],
    "td": "TD 3 (assemblage de mémoires) et TD 4 (décodage d'adresse)",
    "examens": ["Examen B4 d'architecture des ordinateurs"],
}

NOTIONS = [
    {"id": "memoire", "titre": "Mémoires : profondeur, largeur, capacité",
     "formule": r"capacité (bits) $=$ profondeur $\times$ largeur · capacité (octets) $=$ profondeur $\times$ largeur $/\,8$ · $1\text{ Ki}=2^{10}$, $1\text{ Mi}=2^{20}$ · RAM : volatile, lecture et écriture · ROM : non volatile, lecture seule",
     "exemple": r"$8$ mots de $16$ bits : $128$ bits, soit $16$ octets",
     "cours": r"Une mémoire est un ensemble de cases (mots binaires), chacune repérée par une adresse unique. La profondeur est le nombre de mots, la largeur le nombre de bits par mot. SRAM (bascules, rapide, chère, cache) et DRAM (condensateur, rafraîchissement, dense, mémoire principale) sont des RAM ; PROM, EPROM et EEPROM sont des ROM programmables."},
    {"id": "bus", "titre": "Bus d'adresse, de donnée et de contrôle",
     "formule": r"$a$ fils d'adresse : profondeur $=2^a$ · $d$ fils de donnée : largeur $=d$ · $CS=0$ : sorties en haute impédance · $WE$ seulement sur une RAM",
     "exemple": r"$10$ fils d'adresse et $4$ fils de donnée : $1024$ mots de $4$ bits",
     "cours": r"Le bus d'adresse est une entrée, le bus de donnée est une sortie pour une ROM et bidirectionnel pour une RAM. $CS$ (Chip Select) active la mémoire ; désactivée, elle est comme débranchée. $WE$ (Write Enable) choisit l'écriture ou la lecture d'une RAM."},
    {"id": "parallele", "titre": "Assemblage en parallèle",
     "formule": r"augmente la largeur · adresses reliées · contrôle (dont $CS$) relié · données juxtaposées · toutes les mémoires actives ensemble · nombre $=\dfrac{\text{largeur de }M}{\text{largeur de }m}$",
     "exemple": r"deux mémoires de $4$ bits forment une mémoire de $8$ bits",
     "cours": r"Le bus d'adresse de la mémoire obtenue a la même taille que celui des mémoires assemblées. Les deux mémoires reçoivent le même $CS$ : elles livrent ensemble le mot complet."},
    {"id": "serie", "titre": "Assemblage en série",
     "formule": r"augmente la profondeur · données reliées · $CS$ propre à chaque mémoire · jamais deux mémoires actives ensemble · nombre $=\dfrac{\text{profondeur de }M}{\text{profondeur de }m}$ · bits de sélection $=\log_2(\text{nombre})=a_M-a_m$",
     "exemple": r"deux mémoires de $128$ mots : $256$ mots, $A_7$ choisit la mémoire",
     "cours": r"Les bits d'adresse supplémentaires (poids fort) pilotent un démultiplexeur qui recopie le $CS$ de la grande mémoire sur une seule mémoire interne ; les autres reçoivent $0$. Si le $CS$ externe est à $0$, toutes sont désactivées. Éviter deux mémoires actives évite un conflit sur le bus de donnée."},
    {"id": "zone", "titre": "Décodage par zone",
     "formule": r"$n$ bits de sélection : $2^n$ zones · bits de sélection $=$ bits de poids fort · max (toutes zones) : $P-C$ bits · composants connectables : $2^{P-C}$ · $CS_{\text{comp}}=AS\cdot(\text{combinaison des bits de sélection})$",
     "exemple": r"$P=20$, $C=16$ : $4$ bits de sélection au plus, $16$ zones de $64$ Kio",
     "cours": r"Le bus d'adresse du microprocesseur ($P$ fils) est coupé en deux : les bits de poids faible vont aux bus d'adresse des composants, les bits de poids fort choisissent la zone. Une zone par composant, des zones vides restent possibles. Le $CS$ vaut $AS$ ET la combinaison de sélection (avec les compléments pour les bits à $0$). Un seul composant est actif à la fois : pas de conflit."},
    {"id": "espace", "titre": "Espace mémoire : adresses basse et haute",
     "formule": r"adresse basse : bits de sélection de la zone, bits inutilisés à $0$, bits du composant à $0$ · adresse haute : bits du composant à $1$ · haute $=$ basse $+\,2^{\text{fils}}-1$",
     "exemple": r"$P1$ ($10$ fils) en zone $010$ sur $20$ bits : $40000$ à $403FF$",
     "cours": r"Pour chaque composant, on écrit l'adresse sur $P$ bits : bits de sélection, bits inutilisés (mis à $0$), bits d'adresse du composant. L'adresse $403A6$ sélectionne $P1$ et son adresse interne $3A6$ (les bits de poids faible)."},
    {"id": "redondance", "titre": "Effet miroir et redondance",
     "formule": r"bits inutilisés $=P-(\text{bits de sélection})-(\text{fils du composant})$ · nombre d'images $=2^{\text{bits inutilisés}}$",
     "exemple": r"ROM ($16$ fils), $P=20$, $3$ bits de sélection : $1$ bit inutilisé, $2$ images",
     "cours": r"Un bit inutilisé peut valoir $0$ ou $1$ sans changer le composant sélectionné : le composant apparaît à plusieurs endroits de l'espace mémoire. Pour atteindre une même adresse interne il y a donc plusieurs adresses du microprocesseur."},
    {"id": "lineaire", "titre": "Décodage linéaire",
     "formule": r"un bit de sélection par composant : $n$ composants $\Rightarrow$ $n$ bits · possible si $P-C\ge n$ · $CS_i=AS\cdot A_{s_i}$ (jamais deux bits à $1$ ensemble) · bits inutilisés d'un composant $=P-n-\text{fils}$",
     "exemple": r"$4$ composants, plus grand à $19$ fils, $P=24$ : bits de sélection $A_{23}..A_{20}$, $CS_{ROM}=AS\cdot A_{20}$",
     "cours": r"Chaque composant est activé par son propre bit de poids fort : très simple (pas de décodeur) mais il consomme un bit par composant. Le programmeur ne doit jamais mettre deux bits de sélection à $1$ en même temps, sinon deux composants sont actifs et les bus entrent en conflit."},
    {"id": "compact", "titre": "Décodage sans espace vide",
     "formule": r"les composants se suivent : basse du suivant $=$ haute du précédent $+\,1$ · les bits significatifs distinguent le composant des suivants · on classe les composants du plus grand au plus petit",
     "exemple": r"ROM ($14$ fils) en $0000$ à $3FFF$, RAM ($11$ fils) en $4000$ à $47FF$",
     "cours": r"On place les composants les uns derrière les autres. Pour chaque composant on écrit son adresse en binaire avec des $\Phi$ pour ses bits d'adresse interne ; la fonction de décodage se réduit aux bits qui ne sont pas des $\Phi$ et qui séparent ce composant des autres, en complétant avec $AS$."},
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


E26 = "Examen B4 d'architecture 2025/2026"
E25 = "Examen d'architecture S2 (B4) 2024/2025"
T3 = "TD 3 (assemblage de mémoires)"
T4 = "TD 4 (décodage d'adresse)"
C3 = "Chapitre 3 du cours"

LEVELS = [
    {"n": 1, "titre": "Capacité, profondeur, largeur", "notions": ["memoire"], "exos": [
        v("u11", r"Une mémoire contient $8$ mots de $16$ bits. Capacité en bits ?", "8*16", "128", r"$8\times16=128$ bits.", src=C3, duree=1),
        v("u12", r"Même mémoire ($8$ mots de $16$ bits) : capacité en octets ?", "8*16/8", "16", r"$128/8=16$ octets.", src=C3, duree=1),
        v("u13", r"Une mémoire de $1\text{ Ki}$ mots de $8$ bits. Capacité en octets ?", "1024*8/8", "1024", r"Largeur d'un octet : capacité en octets $=$ profondeur $=1024$.", duree=1),
        v("u14", r"Une mémoire de $64\text{ Ki}$ mots de $16$ bits. Capacité en Kio ?", "64*16/8", "128", r"$64\times16/8=128$ Kio.", duree=2),
        v("u15", r"Une mémoire de $256\text{ Kib}$ a une largeur de $4$ bits. Profondeur en Ki mots ?", "256/4", "64", r"$256\text{ Ki}/4=64\text{ Ki}$ mots (TD 3).", src=T3 + ", ex. 1", duree=2),
        v("u16", r"Une mémoire de $512\text{ Kib}$ a une largeur de $8$ bits. Profondeur en Ki mots ?", "512/8", "64", r"$512\text{ Ki}/8=64\text{ Ki}$ mots, soit $64$ Kio (TD 3).", src=T3 + ", ex. 1", duree=2),
        o("u17", r"Comparer RAM et ROM, puis SRAM et DRAM.",
          r"RAM : volatile (données perdues hors tension), lecture et écriture. ROM : non volatile, lecture seule (BIOS)." "\n\n"
          r"SRAM : bascules, très rapide, peu consommatrice mais chère (cache). DRAM : condensateur, charge à rafraîchir régulièrement, forte densité, moins chère (mémoire principale).", src=C3, duree=5),
    ]},
    {"n": 2, "titre": "Bus d'adresse et de donnée", "notions": ["bus", "memoire"], "exos": [
        v("u21", r"Un bus d'adresse de $10$ fils. Profondeur de la mémoire (en mots) ?", "2**10", "1024", r"Profondeur $=2^a=2^{10}=1024$.", src=C3, duree=1),
        v("u22", r"Une mémoire de $128$ Kio a une largeur de $8$ bits. Nombre de fils d'adresse ?", "17", "17", r"Profondeur $=128\text{ Ki}=2^7\times2^{10}=2^{17}$ mots.", src=E25 + ", ex. 1", duree=2),
        v("u23", r"Une mémoire a une largeur de $16$ bits et une capacité de $128\text{ Kib}$. Nombre de fils d'adresse ?", "13", "13", r"Profondeur $=128\text{ Ki}/16=8\text{ Ki}=2^{13}$ : $13$ fils.", src=E26 + ", ex. 1", duree=2),
        v("u24", r"Une mémoire a $16$ fils d'adresse et $16$ fils de donnée. Exposant $e$ de sa capacité en bits ($2^e$) ?", "16+4", "20", r"$2^{16}\times16=2^{16}\times2^4=2^{20}$ bits.", src=E25 + ", ex. 1", duree=2),
        v("u25", r"Une mémoire a $32$ fils de donnée et $16$ fils d'adresse. Exposant $e$ de sa capacité en octets ($2^e$) ?", "16+5-3", "18", r"$2^{16}\times32/8=2^{16}\times2^2=2^{18}$ octets.", src=E26 + ", ex. 1", duree=2),
        v("u26", r"Une mémoire a $20$ fils d'adresse et $8$ fils de donnée. Capacité en Mio ?", "2**20*8/8/2**20", "1", r"$2^{20}$ octets $=1$ Mio.", duree=1),
        o("u27", r"Que signifie l'état de haute impédance et quand une mémoire s'y trouve-t-elle ?",
          r"Troisième état des sorties (ni $0$ ni $1$) : la mémoire n'impose aucune tension, comme si elle était débranchée. Elle y est quand $CS=0$ (mémoire désactivée) ; elle ignore alors aussi ses entrées. Cela permet de relier plusieurs mémoires au même bus de donnée sans conflit.", src=C3, duree=4),
    ]},
    {"n": 3, "titre": "Assemblage en parallèle", "notions": ["parallele", "bus"], "exos": [
        v("u31", r"On assemble deux mémoires de $8$ bits de donnée et $16$ fils d'adresse en parallèle. Fils d'adresse de la mémoire obtenue ?", "16", "16", r"Un assemblage en parallèle ne change pas le bus d'adresse.", src=E25 + ", ex. 1", duree=1),
        v("u32", r"Même assemblage : largeur de la mémoire obtenue (en bits) ?", "2*8", "16", r"Les largeurs s'ajoutent : $8+8=16$.", duree=1),
        v("u33", r"Combien de mémoires de $4$ bits faut-il en parallèle pour obtenir $16$ bits ?", "16/4", "4", r"$16/4=4$.", src=T3 + ", ex. 3", duree=1),
        v("u34", r"La ROM $M_1$ ($256\text{ Kib}$, $4$ bits) sert à former $M_2$ ($512\text{ Kib}$, $8$ bits). Combien de $M_1$ en parallèle ?", "8/4", "2", r"Les deux ont $64$ Ki mots ; il faut doubler la largeur : $8/4=2$.", src=T3 + ", ex. 1", duree=2),
        v("u35", r"On assemble $4$ mémoires de $8$ bits en parallèle. Nombre de mémoires actives simultanément quand la mémoire obtenue est active ?", "4", "4", r"Toutes : elles reçoivent le même $CS$ et livrent ensemble le mot complet.", duree=1),
        o("u36", r"Dire pour un assemblage en parallèle de deux mémoires lesquels des bus sont reliés et lesquels sont juxtaposés.",
          r"Bus d'adresse reliés (ils forment le bus d'adresse de la mémoire externe). Bus de contrôle reliés, $CS$ compris. Bus de donnée juxtaposés : $4+4$ fils donnent $8$ fils. Les deux mémoires sont toujours actives en même temps.", src=C3, duree=5),
    ]},
    {"n": 4, "titre": "Assemblage en série", "notions": ["serie", "bus"], "exos": [
        v("u41", r"On assemble deux mémoires ($8$ bits de donnée, $16$ fils d'adresse) en série. Fils d'adresse de la mémoire obtenue ?", "16+1", "17", r"La profondeur double : un fil de plus.", src=E26 + ", ex. 1", duree=1),
        v("u42", r"Quatre mémoires de $1\text{ Ki}$ mots en série : profondeur de la mémoire obtenue en Ki mots ?", "4*1", "4", r"$4\times1\text{ Ki}=4\text{ Ki}$ mots.", duree=1),
        v("u43", r"Combien de bits d'adresse supplémentaires pour sélectionner l'une de $8$ mémoires en série ?", "3", "3", r"$\log_2 8=3$.", src=E25 + ", ex. 2", duree=1),
        v("u44", r"Les $M_1$ (RAM $2\text{ Mib}$, $4$ bits) forment $M_2$ ($4\text{ Mib}$). Fils d'adresse de $M_2$ ?", "20", "20", r"$4\text{ Mib}/4=1\text{ Mi}$ mots $=2^{20}$ : $20$ fils ($M_1$ en a $19$ : $2\text{ Mib}/4=512$ Ki mots).", src=T3 + ", ex. 2", duree=2),
        v("u45", r"Même assemblage ($M_1$ en $19$ fils, $M_2$ en $20$ fils) : combien de $M_1$ en série ?", "2**(20-19)", "2", r"$2^{20-19}=2$.", src=T3 + ", ex. 2", duree=1),
        v("u46", r"Même assemblage : adresse $9A844_{16}$ sur $20$ bits. Numéro de la mémoire $M_1$ active ($1$ ou $2$) ?", "1+hexa('9A844')//2**19", "2", r"$9A844_{16}=1001\ 1010\ \ldots$ : $A_{19}=1$, donc la mémoire n° $2$.", src=T3 + ", ex. 2 q. 6", duree=2),
        o("u47", r"Pourquoi les mémoires en série ne doivent-elles jamais être actives en même temps ? Comment est généré leur $CS$ ?",
          r"Elles partagent le bus de donnée : deux mémoires actives imposeraient deux données différentes sur les mêmes fils (conflit d'accès). Les bits d'adresse en trop pilotent un démultiplexeur dont l'entrée est le $CS$ externe : une seule sortie recopie le $CS$, les autres valent $0$. Si le $CS$ externe est à $0$, toutes les mémoires internes sont désactivées.", src=C3, duree=6),
    ]},
    {"n": 5, "titre": "Assemblage mixte (série et parallèle)", "notions": ["parallele", "serie", "memoire"], "exos": [
        v("u51", r"On veut une ROM $M$ de $512\text{ Mib}$ sur $16$ bits avec des ROM $m$ de $4\text{ Mib}$ sur $8$ bits. Fils d'adresse de $m$ ?", "19", "19", r"$4\text{ Mib}/8=512\text{ Ki}=2^{19}$ mots : $19$ fils.", src=E26 + ", ex. 2", duree=2),
        v("u52", r"Même énoncé : fils d'adresse de $M$ ?", "25", "25", r"$512\text{ Mib}/16=32\text{ Mi}=2^{25}$ mots : $25$ fils.", src=E26 + ", ex. 2", duree=2),
        v("u53", r"Même énoncé : combien de $m$ en parallèle ?", "16/8", "2", r"Largeur $16/8=2$.", src=E26 + ", ex. 2", duree=1),
        v("u54", r"Même énoncé : combien de $m$ en série ?", "2**(25-19)", "64", r"Profondeur $2^{25}/2^{19}=2^6=64$.", src=E26 + ", ex. 2", duree=1),
        v("u55", r"Même énoncé : combien de bits d'adresse déterminent les $CS$ ?", "25-19", "6", r"$25-19=6$.", src=E26 + ", ex. 2", duree=1),
        v("u56", r"Même énoncé : nombre total de mémoires $m$ ?", "2*64", "128", r"$512\text{ Mib}/4\text{ Mib}=128=2\times64$.", src=E26 + ", ex. 2", duree=1),
        v("u57", r"On forme une RAM $M_2$ de $8\text{ Kio}$ sur $16$ bits avec des RAM $M_1$ de $512$ octets sur $4$ bits. Combien de $M_1$ au total ?", "8*1024*8/(512*8)", "16", r"$M_1$ : $512\times8/4=1\text{ Ki}$ mots ($10$ fils) ; $M_2$ : $8\text{ Ki}\times8/16=4\text{ Ki}$ mots ($12$ fils). Série : $4$, parallèle : $16/4=4$ ; total $4\times4=16$, avec $12-10=2$ bits pour les $CS$.", src=T3 + ", ex. 3", duree=5),
        o("u58", r"Tracer le schéma d'un assemblage de $4$ RAM ($15$ fils d'adresse, $8$ bits) formant une RAM de $64\text{ Ki}$ mots sur $16$ bits.",
          r"Deux rangées de deux : les mémoires 1 et 2 sont en parallèle (même $CS_0$), 3 et 4 en parallèle (même $CS_1$). Les rangées sont en série. $A_{14..0}$ vont à toutes les mémoires ; $A_{15}$ pilote un démultiplexeur : si $A_{15}=0$, $CS_0=CS$ et $CS_1=0$ ; si $A_{15}=1$, $CS_0=0$ et $CS_1=CS$. Les mémoires 1 et 3 donnent les 8 bits de poids fort (ou faible) ; 2 et 4 les 8 autres.", src=C3, duree=8),
    ]},
    {"n": 6, "titre": "Quelle mémoire est active", "notions": ["serie", "parallele"], "exos": [
        v("u61", r"Mémoire de $12$ bits d'adresse formée de $4$ RAM de $10$ bits (en série), numérotées $0$ à $3$ par $A_{11}A_{10}$. Adresse $95A_{16}$ : numéro de la RAM active ?", "hexa('95A')//2**10", "2", r"$95A_{16}=1001\ 0101\ 1010$ : $A_{11}A_{10}=10_2=2$.", src=T3 + ", ex. 3 q. 6", duree=2),
        v("u62", r"Même assemblage, adresse $E03_{16}$ : numéro de la RAM active ?", "hexa('E03')//2**10", "3", r"$E03_{16}=1110\ \ldots$ : $A_{11}A_{10}=11_2=3$.", src=T3 + ", ex. 3 q. 6", duree=2),
        v("u63", r"Même assemblage, adresse $1FF_{16}$ : numéro de la RAM active ?", "hexa('1FF')//2**10", "0", r"$1FF_{16}=0001\ 1111\ 1111$ : $A_{11}A_{10}=00_2=0$.", src=T3 + ", ex. 3 q. 6", duree=2),
        v("u64", r"Même assemblage, adresse $725_{16}$ : numéro de la RAM active ?", "hexa('725')//2**10", "1", r"$725_{16}=0111\ \ldots$ : $A_{11}A_{10}=01_2=1$.", src=T3 + ", ex. 3 q. 6", duree=2),
        v("u65", r"Deux mémoires de $15$ fils d'adresse en série (adresse sur $16$ bits). Adresse $8F3A_{16}$ : numéro de la mémoire active ($1$ ou $2$) ?", "1+hexa('8F3A')//2**15", "2", r"$8_{16}=1000_2$ : $A_{15}=1$, mémoire n° $2$.", duree=2),
        v("u66", r"Mémoire $16$ bits formée de $4$ mémoires de $4$ bits en parallèle. Combien de mémoires sont actives quand $CS=1$ ?", "4", "4", r"Les $4$ : elles ont le même $CS$.", duree=1),
        o("u67", r"Que se passe-t-il pour les mémoires internes d'un assemblage série quand le $CS$ de la mémoire externe vaut $0$ ?",
          r"Toutes les mémoires internes sont désactivées (le démultiplexeur met toutes ses sorties à $0$) : leurs sorties de donnée sont en haute impédance.", src=C3, duree=3),
    ]},
    {"n": 7, "titre": "Décodage par zone : bits de sélection", "notions": ["zone", "bus"], "exos": [
        v("u71", r"Microprocesseur à $20$ fils d'adresse, plus grand composant à $17$ fils : nombre maximal de composants en mode zone ?", "2**(20-17)", "8", r"$P-C=3$ bits de sélection : $2^3=8$ zones.", src=E26 + ", ex. 1", duree=1),
        v("u72", r"Microprocesseur à $20$ fils d'adresse dont $6$ servent à la sélection : nombre maximal de composants en mode zone ?", "2**6", "64", r"$2^6=64$ zones.", src=E25 + ", ex. 1", duree=1),
        v("u73", r"Cinq composants en mode zone avec le moins de zones possible : combien de bits de sélection ?", "3", "3", r"$2^2=4<5\le8=2^3$ : $3$ bits.", src=T4 + ", ex. 2", duree=1),
        v("u74", r"Microprocesseur à $22$ fils d'adresse, ROM de $20$ fils, RAM de $12$ fils, $2$ périphériques de $10$ fils. Nombre maximal de composants en zone ?", "2**(22-20)", "4", r"$P-C=2$ : $4$ zones, donc pas de cinquième composant.", src=E26 + ", ex. 1", duree=2),
        v("u75", r"Même système : fils d'adresse inutilisés pour la RAM (zones maximales) ?", "22-2-12", "8", r"$22-2-12=8$.", src=E26 + ", ex. 1", duree=2),
        v("u76", r"$P=20$, ROM de $16$ fils, $4$ bits de sélection : taille d'une zone en Kio ?", "2**(20-4)/1024", "64", r"$2^{16}$ octets $=64$ Kio.", src=C3, duree=2),
        o("u77", r"Un système a $20$ fils d'adresse, ROM $16$ fils, RAM $15$ fils, $P1$ $10$ fils, $P2$ $4$ fils, avec $8$ zones : donner les bits de sélection et les expressions des $CS$ (zones $0$ à $3$).",
          r"Bits de sélection $A_{19}A_{18}A_{17}$ : ROM $000$, RAM $001$, $P1$ $010$, $P2$ $011$." "\n\n"
          r"$CS_{ROM}=AS\cdot\overline{A_{19}}\cdot\overline{A_{18}}\cdot\overline{A_{17}}$" "\n"
          r"$CS_{RAM}=AS\cdot\overline{A_{19}}\cdot\overline{A_{18}}\cdot A_{17}$" "\n"
          r"$CS_{P1}=AS\cdot\overline{A_{19}}\cdot A_{18}\cdot\overline{A_{17}}$" "\n"
          r"$CS_{P2}=AS\cdot\overline{A_{19}}\cdot A_{18}\cdot A_{17}$", src=C3, duree=8),
    ]},
    {"n": 8, "titre": "Espace mémoire : adresses basse et haute", "notions": ["espace", "zone"], "exos": [
        v("u81", r"$P=20$, zone $001$ ($A_{19}A_{18}A_{17}$) : RAM de $15$ fils, basse $20000_{16}$. Adresse haute ?", "hexa('20000')+2**15-1", "hexa('27FFF')", r"Haute $=$ basse $+2^{15}-1$ : $20000+7FFF=27FFF_{16}$.", src=C3, duree=3),
        v("u82", r"Zone $010$ : $P1$ de $10$ fils, basse $40000_{16}$. Adresse haute ?", "hexa('40000')+2**10-1", "hexa('403FF')", r"$40000+3FF=403FF_{16}$.", src=C3, duree=3),
        v("u83", r"Zone $011$ : $P2$ de $4$ fils, basse $60000_{16}$. Adresse haute ?", "hexa('60000')+2**4-1", "hexa('6000F')", r"$60000+F=6000F_{16}$.", src=C3, duree=3),
        v("u84", r"Même système : adresse du microprocesseur pour atteindre l'adresse interne $3A6_{16}$ de $P1$ ?", "hexa('40000')+hexa('3A6')", "hexa('403A6')", r"Basse de $P1$ plus décalage : $40000+3A6=403A6_{16}$ (bits : $010\ 0000000\ 11\ 1010\ 0110$).", src=C3, duree=3),
        v("u85", r"ROM de $128$ Kio, $P=20$, zone $000$. Adresse haute ?", "hexa('00000')+2**17-1", "hexa('1FFFF')", r"$128\text{ Kio}=2^{17}$ : $0+1FFFF=1FFFF_{16}$.", src=E26 + ", ex. 3", duree=3),
        v("u86", r"$P1$ de $8$ Kio en zone $010$ ($P=20$), basse $40000_{16}$. Adresse haute ?", "hexa('40000')+2**13-1", "hexa('41FFF')", r"$8\text{ Kio}=2^{13}$ : $40000+1FFF=41FFF_{16}$.", src=E26 + ", ex. 3", duree=3),
        o("u87", r"Représenter l'espace mémoire du système de l'exercice précédent (ROM $128$ Kio, RAM $32$ Kio, $P1$ $8$ Kio, $P2$ $256$ octets, $20$ bits, $8$ zones) avec les adresses hautes et basses.",
          r"Taille de bus : ROM $17$, RAM $15$, $P1$ $13$, $P2$ $8$ ; sélection $A_{19}A_{18}A_{17}$." "\n\n"
          r"| Composant | basse | haute |" "\n|---|---|---|\n"
          r"| ROM | 00000 | 1FFFF |" "\n" r"| RAM | 20000 | 27FFF |" "\n" r"| P1 | 40000 | 41FFF |" "\n" r"| P2 | 60000 | 600FF |", src=E26 + ", ex. 3", duree=8),
    ]},
    {"n": 9, "titre": "Redondance (effet miroir)", "notions": ["redondance", "espace"], "exos": [
        v("u91", r"$P=20$, $3$ bits de sélection, ROM de $16$ fils. Nombre d'images de la ROM ?", "2**(20-3-16)", "2", r"$20-3-16=1$ bit inutilisé : $2^1=2$ images.", src=C3, duree=2),
        v("u92", r"Même système : nombre d'images de la RAM ($15$ fils) ?", "2**(20-3-15)", "4", r"$2$ bits inutilisés : $4$ images.", src=C3, duree=2),
        v("u93", r"Même système : nombre d'images de $P1$ ($10$ fils) ?", "2**(20-3-10)", "128", r"$7$ bits inutilisés : $2^7=128$.", src=C3, duree=2),
        v("u94", r"Même système : nombre d'images de $P2$ ($4$ fils) ?", "2**(20-3-4)", "8192", r"$13$ bits inutilisés : $2^{13}=8192$.", src=C3, duree=2),
        v("u95", r"$P=20$, $3$ bits de sélection, $P2$ de $256$ octets ($8$ fils). Nombre d'images de $P2$ ?", "2**(20-3-8)", "512", r"$20-3-8=9$ bits inutilisés : $2^9=512$.", src=E26 + ", ex. 3", duree=2),
        v("u96", r"$P=24$, $3$ bits de sélection, $P3$ de $2$ Kio ($11$ fils). Nombre d'images de $P3$ ?", "2**(24-3-11)", "1024", r"$10$ bits inutilisés : $2^{10}=1024$.", src=T4 + ", ex. 2", duree=2),
        o("u97", r"Donner deux adresses du microprocesseur ($P=20$, sélection $A_{19..17}=000$) qui désignent l'adresse $ABCD_{16}$ de la ROM ($16$ fils).",
          r"Le bit inutilisé $A_{16}$ peut valoir $0$ ou $1$ : $0ABCD_{16}$ et $1ABCD_{16}$. La ROM a deux images, de $00000$ à $0FFFF$ et de $10000$ à $1FFFF$.", src=C3, duree=4),
    ]},
    {"n": 10, "titre": "Décodage linéaire", "notions": ["lineaire", "zone"], "exos": [
        v("u101", r"Microprocesseur à $22$ fils d'adresse en mode linéaire avec ROM ($15$ fils), RAM ($12$ fils) et deux périphériques ($10$ fils). Bits de sélection (un par composant) ?", "4", "4", r"Un bit par composant : $4$.", src=E25 + ", ex. 1", duree=1),
        v("u102", r"Même système : fils d'adresse inutilisés pour la RAM ?", "22-4-12", "6", r"$22-4-12=6$.", src=E25 + ", ex. 1", duree=2),
        v("u103", r"Microprocesseur à $16$ bits, ROM $12$ fils, RAM $11$ fils, $P1$ $10$ fils, $P2$ $6$ fils : combien de bits restent pour la sélection ($P-C$) ? Le mode linéaire est-il possible ($4$ composants) ?", "16-12", "4", r"$16-12=4\ge4$ composants : oui.", src=E25 + ", ex. 4", duree=2),
        v("u104", r"$P=24$, ROM $19$ fils (sélection $A_{20}$, basse $100000_{16}$). Adresse haute de la ROM ?", "hexa('100000')+2**19-1", "hexa('17FFFF')", r"$100000+7FFFF=17FFFF_{16}$.", src=E25 + ", ex. 3", duree=3),
        v("u105", r"Même système : RAM $15$ fils, sélection $A_{21}$, basse $200000_{16}$. Adresse haute ?", "hexa('200000')+2**15-1", "hexa('207FFF')", r"$200000+7FFF=207FFF_{16}$.", src=E25 + ", ex. 3", duree=3),
        v("u106", r"Même système : $P2$ de $8$ fils, sélection $A_{23}$, basse $800000_{16}$. Adresse haute ?", "hexa('800000')+2**8-1", "hexa('8000FF')", r"$800000+FF=8000FF_{16}$.", src=E25 + ", ex. 3", duree=3),
        o("u107", r"Même système ($P=24$ ; ROM $19$ fils, RAM $15$, $P1$ $10$, $P2$ $8$ ; mode linéaire, $P2$ en $A_{23}$) : donner les bits de sélection et les $CS$.",
          r"Fils des composants : $19,15,10,8$ (capacités $4\text{ Mib}/8=512$ Ki octets, etc.). Bits de sélection $A_{23}A_{22}A_{21}A_{20}$ : ROM $A_{20}$, RAM $A_{21}$, $P1$ $A_{22}$, $P2$ $A_{23}$." "\n\n"
          r"$CS_{ROM}=AS\cdot A_{20}$, $CS_{RAM}=AS\cdot A_{21}$, $CS_{P1}=AS\cdot A_{22}$, $CS_{P2}=AS\cdot A_{23}$." "\n\n"
          r"Le programmeur ne doit jamais mettre deux de ces bits à $1$ simultanément.", src=E25 + ", ex. 3", duree=8),
    ]},
    {"n": 11, "titre": "Décodage sans espace vide", "notions": ["compact", "espace"], "exos": [
        v("u111", r"Microprocesseur à $16$ bits : ROM ($14$ fils) en $0000$, puis RAM ($11$ fils). Adresse basse de la RAM ?", "2**14", "hexa('4000')", r"La ROM occupe $2^{14}=4000_{16}$ adresses : la RAM commence en $4000_{16}$.", src=E26 + ", ex. 4", duree=2),
        v("u112", r"Même système : adresse haute de la RAM ($11$ fils) ?", "hexa('4000')+2**11-1", "hexa('47FF')", r"$4000+7FF=47FF_{16}$.", src=E26 + ", ex. 4", duree=2),
        v("u113", r"Même système : $P1$ ($9$ fils) suit la RAM. Adresse haute de $P1$ ?", "hexa('4800')+2**9-1", "hexa('49FF')", r"Basse $4800_{16}$ ; haute $4800+1FF=49FF_{16}$.", src=E26 + ", ex. 4", duree=2),
        v("u114", r"Même système : $P2$ ($5$ fils) suit $P1$. Adresse haute de $P2$ ?", "hexa('4A00')+2**5-1", "hexa('4A1F')", r"Basse $4A00_{16}$ ; haute $4A00+1F=4A1F_{16}$.", src=E26 + ", ex. 4", duree=2),
        v("u115", r"$P=24$ : ROM $23$ fils en $000000$, RAM $21$ fils. Adresse haute de la RAM ?", "hexa('800000')+2**21-1", "hexa('9FFFFF')", r"Basse $800000_{16}$ ($=2^{23}$) ; haute $800000+1FFFFF=9FFFFF_{16}$.", src=E25 + ", ex. 5", duree=3),
        v("u116", r"Même système : $P1$ ($15$ fils) suit la RAM. Adresse haute de $P1$ ?", "hexa('A00000')+2**15-1", "hexa('A07FFF')", r"Basse $A00000_{16}$ ; haute $A00000+7FFF=A07FFF_{16}$.", src=E25 + ", ex. 5", duree=3),
        o("u117", r"Même système que $u111$ à $u114$ : donner les expressions les plus simples des $CS$.",
          r"Adresses : ROM $0000$–$3FFF$, RAM $4000$–$47FF$, $P1$ $4800$–$49FF$, $P2$ $4A00$–$4A1F$." "\n\n"
          r"$CS_{ROM}=AS\cdot\overline{A_{14}}$ (tout le reste a $A_{14}=1$)" "\n"
          r"$CS_{RAM}=AS\cdot A_{14}\cdot\overline{A_{11}}$" "\n"
          r"$CS_{P1}=AS\cdot A_{14}\cdot A_{11}\cdot\overline{A_9}$" "\n"
          r"$CS_{P2}=AS\cdot A_{14}\cdot A_{11}\cdot A_9$", src=E26 + ", ex. 4", duree=10),
    ]},
    {"n": 12, "titre": "Niveau examen : sujet B4 2025/2026", "notions": ["memoire", "bus", "parallele", "serie", "zone", "espace", "redondance", "compact"], "examen": True, "exos": [
        o("ux1", r"Exercice 1 (méthode) : une mémoire de $16$ bits de largeur et de $128\text{ Kib}$, un assemblage en série de deux mémoires de $16$ fils d'adresse, un microprocesseur à $20$ fils avec un plus grand composant à $17$ fils : répondre aux sept questions de cours (fils d'adresse, capacité, nombre de composants en mode zone).",
          r"$128\text{ Kib}/16=8\text{ Ki}=2^{13}$ : $13$ fils. $32$ fils de donnée et $16$ fils d'adresse : $2^{16}\times32/8=2^{18}$ octets. Deux mémoires en série : $17$ fils. $P=20$, $C=17$ : $2^3=8$ composants. $P=22$, ROM $20$ fils : $2^2=4$ zones, donc pas de cinquième composant ; RAM de $12$ fils : $22-2-12=8$ fils inutilisés.", src=E26 + ", ex. 1 (7 points)", duree=15),
        o("ux2", r"Exercice 2 : réaliser une ROM de $512\text{ Mib}$ (largeur $16$) avec des ROM de $4\text{ Mib}$ (largeur $8$) : profondeurs, fils d'adresse, nombre en parallèle, en série, bits de $CS$, mémoires actives.",
          r"$m$ : $4\text{ Mib}/8=2^{19}$ mots, $19$ fils. $M$ : $512\text{ Mib}/16=2^{25}$ mots, $25$ fils. Parallèle : $16/8=2$. Série : $2^{25}/2^{19}=64$. Bits de $CS$ : $25-19=6$. Mémoires actives en même temps : $2$.", src=E26 + ", ex. 2 (5 points)", duree=12),
        o("ux3", r"Exercice 3 : ROM $128$ Kio, RAM $32$ Kio, $P1$ $8$ Kio, $P2$ $256$ o ; $20$ bits ; mode zone avec le plus de zones : fils d'adresse, bits de sélection, $CS$, adresses, redondance.",
          r"Fils : $17,15,13,8$. Sélection $A_{19}A_{18}A_{17}$." "\n\n"
          r"$CS_{ROM}=AS\cdot\overline{A_{19}}\,\overline{A_{18}}\,\overline{A_{17}}$, $CS_{RAM}=AS\cdot\overline{A_{19}}\,\overline{A_{18}}\,A_{17}$, $CS_{P1}=AS\cdot\overline{A_{19}}\,A_{18}\,\overline{A_{17}}$, $CS_{P2}=AS\cdot\overline{A_{19}}\,A_{18}\,A_{17}$." "\n\n"
          r"| Composant | basse | haute | images |" "\n|---|---|---|---|\n"
          r"| ROM | 00000 | 1FFFF | 1 |" "\n" r"| RAM | 20000 | 27FFF | 4 |" "\n" r"| P1 | 40000 | 41FFF | 16 |" "\n" r"| P2 | 60000 | 600FF | 512 |", src=E26 + ", ex. 3 (5 points)", duree=18),
        o("ux4", r"Exercice 4 : $16$ bits ; ROM $14$ fils, RAM $11$, $P1$ $9$, $P2$ $5$ ; sans espace vide : adresses et $CS$ les plus simples.",
          r"ROM $0000$–$3FFF$, RAM $4000$–$47FF$, $P1$ $4800$–$49FF$, $P2$ $4A00$–$4A1F$." "\n\n"
          r"$CS_{ROM}=AS\cdot\overline{A_{14}}$, $CS_{RAM}=AS\cdot A_{14}\overline{A_{11}}$, $CS_{P1}=AS\cdot A_{14}A_{11}\overline{A_9}$, $CS_{P2}=AS\cdot A_{14}A_{11}A_9$.", src=E26 + ", ex. 4 (3 points)", duree=12),
    ]},
    {"n": 13, "titre": "Niveau examen : sujet 2024/2025", "notions": ["memoire", "parallele", "serie", "zone", "lineaire", "redondance", "compact"], "examen": True, "exos": [
        o("uy1", r"Exercice 2 : ROM $M$ de $256\text{ Mib}$ (largeur $16$) avec des ROM $m$ de $8\text{ Mib}$ (largeur $4$).",
          r"$m$ : $8\text{ Mib}/4=2^{21}$ mots, $21$ fils. $M$ : $256\text{ Mib}/16=2^{24}$ mots, $24$ fils. Parallèle : $16/4=4$. Série : $2^{24}/2^{21}=8$. Bits de $CS$ : $3$. Mémoires actives : $4$.", src=E25 + ", ex. 2 (4 points)", duree=12),
        o("uy2", r"Exercice 3 : ROM $4$ Mib, RAM $256$ Kib, $P1$ $8$ Kib, $P2$ $2$ Kib (capacités en bits), $24$ bits, données sur $8$ bits, mode linéaire.",
          r"Fils : $19,15,10,8$. Sélection : $A_{23}A_{22}A_{21}A_{20}$. $CS_{ROM}=AS\cdot A_{20}$, $CS_{RAM}=AS\cdot A_{21}$, $CS_{P1}=AS\cdot A_{22}$, $CS_{P2}=AS\cdot A_{23}$." "\n\n"
          r"| Composant | basse | haute |" "\n|---|---|---|\n"
          r"| ROM | 100000 | 17FFFF |" "\n" r"| RAM | 200000 | 207FFF |" "\n" r"| P1 | 400000 | 4003FF |" "\n" r"| P2 | 800000 | 8000FF |", src=E25 + ", ex. 3 (4 points)", duree=18),
        o("uy3", r"Exercice 4 : $16$ bits ; ROM $4$ Kio, RAM $2$ Kio, $P1$ $1$ Kio, $P2$ $64$ o. Décodage linéaire possible ? Puis mode zone avec le moins de zones : sélection, $CS$, adresses, redondance.",
          r"Fils : $12,11,10,6$. Linéaire possible ($16-12=4\ge4$). Zone minimale : $2$ bits $A_{15}A_{14}$ : ROM $00$, RAM $01$, $P1$ $10$, $P2$ $11$." "\n\n"
          r"| Composant | basse | haute | images |" "\n|---|---|---|---|\n"
          r"| ROM | 0000 | 0FFF | 4 |" "\n" r"| RAM | 4000 | 47FF | 8 |" "\n" r"| P1 | 8000 | 83FF | 16 |" "\n" r"| P2 | C000 | C03F | 256 |", src=E25 + ", ex. 4 (5 points)", duree=22),
        o("uy4", r"Exercice 5 : $24$ bits ; ROM $23$ fils, RAM $21$, $P1$ $15$, $P2$ $10$ ; sans espace vide : adresses et $CS$ les plus simples.",
          r"ROM $000000$–$7FFFFF$, RAM $800000$–$9FFFFF$, $P1$ $A00000$–$A07FFF$, $P2$ $A08000$–$A083FF$." "\n\n"
          r"$CS_{ROM}=AS\cdot\overline{A_{23}}$, $CS_{RAM}=AS\cdot A_{23}\overline{A_{21}}$, $CS_{P1}=AS\cdot A_{23}A_{21}\overline{A_{15}}$, $CS_{P2}=AS\cdot A_{23}A_{21}A_{15}$.", src=E25 + ", ex. 5 (2 points)", duree=12),
    ]},
]


def _v(enonce, calc, ans, sol):
    return {"enonce": enonce, "calc": calc, "ans": ans, "sol": sol}


VARIANTS = {
    "u11": [_v(r"Une mémoire contient $16$ mots de $8$ bits. Capacité en bits ?", "16*8", "128", r"$16\times8=128$ bits.")],
    "u14": [_v(r"Une mémoire de $32\text{ Ki}$ mots de $16$ bits. Capacité en Kio ?", "32*16/8", "64", r"$32\times16/8=64$ Kio.")],
    "u21": [_v(r"Un bus d'adresse de $12$ fils. Profondeur de la mémoire (en mots) ?", "2**12", "4096", r"$2^{12}=4096$.")],
    "u22": [_v(r"Une mémoire de $64$ Kio a une largeur de $8$ bits. Nombre de fils d'adresse ?", "16", "16", r"$64\text{ Ki}=2^{16}$ mots.")],
    "u33": [_v(r"Combien de mémoires de $8$ bits faut-il en parallèle pour obtenir $32$ bits ?", "32/8", "4", r"$32/8=4$.")],
    "u41": [_v(r"On assemble deux mémoires ($8$ bits, $15$ fils d'adresse) en série. Fils d'adresse obtenus ?", "15+1", "16", r"Un fil de plus.")],
    "u43": [_v(r"Combien de bits d'adresse supplémentaires pour sélectionner l'une de $4$ mémoires en série ?", "2", "2", r"$\log_2 4=2$.")],
    "u54": [_v(r"ROM $M$ de $256\text{ Mib}$ sur $16$ bits avec des ROM $m$ de $8\text{ Mib}$ sur $4$ bits : combien de $m$ en série ?", "2**(24-21)", "8", r"$M$ : $2^{24}$ mots ; $m$ : $2^{21}$ mots ; $2^3=8$.")],
    "u71": [_v(r"Microprocesseur à $24$ fils d'adresse, plus grand composant à $20$ fils : nombre maximal de composants en mode zone ?", "2**(24-20)", "16", r"$2^4=16$.")],
    "u82": [_v(r"Zone $010$ : $P1$ de $8$ fils, basse $40000_{16}$. Adresse haute ?", "hexa('40000')+2**8-1", "hexa('400FF')", r"$40000+FF=400FF_{16}$.")],
    "u91": [_v(r"$P=20$, $3$ bits de sélection, ROM de $17$ fils. Nombre d'images ?", "2**(20-3-17)", "1", r"$0$ bit inutilisé : une seule image.")],
    "u102": [_v(r"$22$ fils d'adresse, mode linéaire, $4$ composants dont RAM de $11$ fils : fils inutilisés pour la RAM ?", "22-4-11", "7", r"$22-4-11=7$.")],
    "u112": [_v(r"$16$ bits : ROM ($13$ fils) en $0000$, RAM ($10$ fils) ensuite. Adresse haute de la RAM ?", "hexa('2000')+2**10-1", "hexa('23FF')", r"ROM : $0000$–$1FFF$ ; RAM : $2000$ + $3FF$ $=23FF_{16}$.")],
}
for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["id"] in VARIANTS:
            _e["variants"] = VARIANTS[_e["id"]]


EXTRA_PARTS = []

QUIZ = [
    {"notion": "memoire", "type": "qcm", "q": r"Une mémoire de $8$ mots de $16$ bits a une capacité de :", "choix": [r"$16$ octets", r"$8$ octets", r"$128$ octets", r"$32$ octets"], "bonne": 0},
    {"notion": "memoire", "type": "vf", "q": r"Une ROM est volatile.", "bonne": False},
    {"notion": "bus", "type": "qcm", "q": r"Avec $a$ fils d'adresse, la profondeur est :", "choix": [r"$2^a$", r"$a^2$", r"$2a$", r"$a$"], "bonne": 0},
    {"notion": "bus", "type": "vf", "q": r"Une mémoire désactivée ($CS=0$) a ses sorties en haute impédance.", "bonne": True},
    {"notion": "parallele", "type": "qcm", "q": r"L'assemblage en parallèle augmente :", "choix": [r"la largeur", r"la profondeur", r"le nombre de fils d'adresse", r"la fréquence"], "bonne": 0},
    {"notion": "parallele", "type": "vf", "q": r"Les mémoires assemblées en parallèle ont le même $CS$.", "bonne": True},
    {"notion": "serie", "type": "qcm", "q": r"L'assemblage en série augmente :", "choix": [r"la profondeur", r"la largeur", r"le nombre de fils de donnée", r"rien"], "bonne": 0},
    {"notion": "serie", "type": "vf", "q": r"Deux mémoires en série peuvent être actives en même temps.", "bonne": False},
    {"notion": "zone", "type": "qcm", "q": r"En mode zone, les bits de sélection sont :", "choix": [r"les bits de poids fort", r"les bits de poids faible", r"les bits inutilisés", r"les bits de donnée"], "bonne": 0},
    {"notion": "zone", "type": "vf", "q": r"Si $AS=0$, aucun composant ne doit être activé.", "bonne": True},
    {"notion": "espace", "type": "qcm", "q": r"Les bits inutilisés du microprocesseur sont, pour calculer les adresses :", "choix": [r"mis à $0$", r"mis à $1$", r"ignorés", r"aléatoires"], "bonne": 0},
    {"notion": "espace", "type": "vf", "q": r"L'adresse haute vaut l'adresse basse $+\,2^{\text{fils}}-1$.", "bonne": True},
    {"notion": "redondance", "type": "qcm", "q": r"Nombre d'images d'un composant :", "choix": [r"$2^{\text{bits inutilisés}}$", r"$\text{bits inutilisés}$", r"$2\times\text{fils}$", r"toujours $1$"], "bonne": 0},
    {"notion": "redondance", "type": "vf", "q": r"Un bit d'adresse inutilisé provoque l'apparition d'images du composant.", "bonne": True},
    {"notion": "lineaire", "type": "qcm", "q": r"Le décodage linéaire utilise :", "choix": [r"un bit de sélection par composant", r"un décodeur", r"deux bits par composant", r"aucun bit"], "bonne": 0},
    {"notion": "lineaire", "type": "vf", "q": r"En linéaire, deux bits de sélection à $1$ simultanément sont sans danger.", "bonne": False},
    {"notion": "compact", "type": "qcm", "q": r"Sans espace vide, l'adresse basse d'un composant est :", "choix": [r"la haute du précédent $+1$", r"la haute du précédent", r"toujours $0$", r"aléatoire"], "bonne": 0},
    {"notion": "compact", "type": "vf", "q": r"Le mode sans espace vide n'a pas de zones de taille égale.", "bonne": True},
]

_M = r"capacité (bits) $=$ profondeur $\times$ largeur · octets : $/\,8$ · $1\text{ Ki}=2^{10}$"
_B = r"profondeur $=2^a$ · largeur $=d$ · $CS=0$ : haute impédance"
_P = r"parallèle : $\dfrac{\text{largeur }M}{\text{largeur }m}$ mémoires · mêmes adresses, $CS$ commun"
_S = r"série : $\dfrac{\text{profondeur }M}{\text{profondeur }m}$ mémoires · bits de $CS$ $=a_M-a_m$ · jamais deux actives"
_Z = r"$P-C$ bits de sélection au plus · $2^n$ zones · $CS=AS\cdot(\text{combinaison})$"
_E = r"haute $=$ basse $+\,2^{\text{fils}}-1$ · bits inutilisés à $0$"
_R = r"images $=2^{P-\text{sélection}-\text{fils}}$"
_L = r"$n$ composants : $n$ bits de sélection · $CS_i=AS\cdot A_{s_i}$ · bits inutilisés $=P-n-\text{fils}$"
_C = r"basse $=$ haute du précédent $+\,1$ · bits significatifs $+\,AS$"

FORMULES = {
    "u11": _M, "u12": _M, "u13": _M, "u14": _M, "u15": _M, "u16": _M, "u17": r"RAM volatile, ROM non volatile · SRAM : bascules · DRAM : condensateur",
    "u21": _B, "u22": _B + " · " + _M, "u23": _B + " · " + _M, "u24": _B + " · " + _M, "u25": _B + " · " + _M, "u26": _B + " · " + _M, "u27": r"$CS=0$ : sorties en haute impédance",
    "u31": _P, "u32": _P, "u33": _P, "u34": _P + " · " + _M, "u35": _P, "u36": _P,
    "u41": _S, "u42": _S, "u43": _S, "u44": _S + " · " + _M, "u45": _S, "u46": _S + r" · $A_{19}$ choisit la mémoire", "u47": _S,
    "u51": _B + " · " + _M, "u52": _B + " · " + _M, "u53": _P, "u54": _S, "u55": _S, "u56": _P + " · " + _S, "u57": _P + " · " + _S + " · " + _M, "u58": _P + " · " + _S,
    "u61": _S, "u62": _S, "u63": _S, "u64": _S, "u65": _S, "u66": _P, "u67": _S,
    "u71": _Z, "u72": _Z, "u73": _Z, "u74": _Z, "u75": _Z + r" · bits inutilisés $=P-\text{sélection}-\text{fils}$", "u76": _Z, "u77": _Z,
    "u81": _E, "u82": _E, "u83": _E, "u84": _E + r" · adresse $=$ basse $+$ adresse interne", "u85": _E, "u86": _E, "u87": _E + " · " + _Z,
    "u91": _R, "u92": _R, "u93": _R, "u94": _R, "u95": _R, "u96": _R, "u97": _R,
    "u101": _L, "u102": _L, "u103": _L, "u104": _E, "u105": _E, "u106": _E, "u107": _L,
    "u111": _C + " · " + _E, "u112": _C + " · " + _E, "u113": _C + " · " + _E, "u114": _C + " · " + _E, "u115": _C + " · " + _E, "u116": _C + " · " + _E, "u117": _C,
    "ux1": _M + " · " + _B + " · " + _Z, "ux2": _P + " · " + _S, "ux3": _Z + " · " + _E + " · " + _R, "ux4": _C,
    "uy1": _P + " · " + _S, "uy2": _L + " · " + _E, "uy3": _L + " · " + _Z + " · " + _R, "uy4": _C,
}
