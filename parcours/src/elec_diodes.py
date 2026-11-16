"""Level path: S2 electronics, PN junction, diodes and Zener diodes, promo 2031.

Calibrated on the Moodle course « Electronique S2 - Diodes » (`Jonction PN et Diodes`, `Précisions et méthodes -
Diode`), the TD « Les diodes » (6 exercises, typed correction), the TD « La diode Zéner » (4 exercises, handwritten
correction) and the exam « Electronics Exam - Diodes » of March 2025 (English, no official correction: the answers of
level 12 are our own, worked out and checked here). Circuits are described in words and drawn as SVG
(`schema.py`, `FIGS` at the end).
In `calc`, V0 is the threshold voltage, Vz the Zener voltage (absolute value), V the input voltage.
"""
from .schema import D, Fil, Point, R, SrcU, ajoute, fig, schema_echelle, tension


SUBJECT = {
    "id": "elec-s2-diodes",
    "ordre": 540,
    "matiere": "electronique",
    "semestre": "S2",
    "ecue": "Diodes",
    "titre": "Jonction PN, diodes et diode Zéner",
    "chapitres_moodle": ["Electronique S2 - Diodes [2526_I_INF_FISE_S02_CN_DIO]/01_Documents de cours",
                         "Electronique S2 - Diodes [2526_I_INF_FISE_S02_CN_DIO]/02_Travaux Dirigés"],
    "td": "TD « Les diodes » (6 exercices) et TD « La diode Zéner » (4 exercices)",
    "examens": ["Examen d'électronique « Diodes » (mars 2025, en anglais)"],
}

NOTIONS = [
    {"id": "polarisation", "titre": "Diode à jonction PN : polarisation",
     "formule": r"anode $A$, cathode $K$ · directe : $V_{AK} > 0$, la diode conduit · inverse : $V_{AK} < 0$, bloquée (courant inverse négligeable) · le courant circule de l'anode vers la cathode · le courant descend les potentiels",
     "exemple": r"$E$, diode dans le sens de $E$, $R$ : la diode est passante, $U_R=E$ (modèle idéal)",
     "cours": r"Une diode est une jonction PN : elle laisse passer le courant dans un seul sens, de l'anode vers la cathode. Sa caractéristique est exponentielle en direct et presque horizontale (courant quasi nul) en inverse."},
    {"id": "modeles", "titre": "Modèles statiques de la diode",
     "formule": r"idéal (interrupteur) : passante $=$ fil, bloquée $=$ interrupteur ouvert · à seuil : passante $=$ source $V_0$ ($0{,}6$ à $0{,}7$ V pour le silicium) · réel : source $V_0$ en série avec $r_D$ · bloquée ($V_{AK} < V_0$) : $I=0$",
     "exemple": r"$E=5$ V, $R=10$ Ω, $V_0=0{,}7$ V : $I=\dfrac{E-V_0}{R}=0{,}43$ A",
     "cours": r"On remplace la diode par un modèle linéaire. Le modèle réel est le plus précis, le modèle idéal le plus simple. Si la résistance du circuit est grande devant $r_D$, les modèles à seuil et réel donnent le même résultat."},
    {"id": "absurde", "titre": "Raisonnement par l'absurde",
     "formule": r"montrer « passante » : on la suppose bloquée (interrupteur ouvert), on calcule $V_{AK}$ et on trouve $V_{AK} > V_0$ (absurde) · montrer « bloquée » : on la suppose passante (fil ou $V_0$), on calcule $I_{AK}$ et on trouve $I_{AK} < 0$ (absurde)",
     "exemple": r"$E=10$ V, $R_1=50$ Ω, $R_2=100$ Ω, diode sur $R_2$ : bloquée donnerait $V_{AK}=\tfrac{20}3$ V $> 0{,}7$ V, donc elle est passante",
     "cours": r"On ne sait pas à l'avance l'état d'une diode : on fait une hypothèse, on calcule, et on vérifie la cohérence. Une hypothèse qui mène à une contradiction est fausse, l'autre état est le bon."},
    {"id": "transfert_d", "titre": "Caractéristique de transfert",
     "formule": r"lister les états possibles des diodes · exprimer $U$ dans chaque cas · trouver les valeurs de $V$ (ou de $e(t)$) correspondant à chaque état · raccorder les morceaux (la courbe est continue)",
     "exemple": r"$R$ et $R_L$, deux diodes tête-bêche en parallèle sur $R_L$ (modèle à seuil, $R=R_L$) : $U=\tfrac V2$ pour $|V| < 2V_0$, $U=\pm V_0$ sinon",
     "cours": r"La caractéristique de transfert est la courbe $U=f(V)$. Pour une courbe en fonction du temps, il est plus simple de tracer d'abord la tension d'entrée, puis de reporter les cas."},
    {"id": "portes", "titre": "Portes logiques à diodes",
     "formule": r"anodes sur les entrées, cathodes communes, $R$ vers la masse : porte OU · cathodes sur les entrées, anodes communes, $R$ vers $+E$ : porte ET · diode idéale passante : $V_A=V_K$",
     "exemple": r"OU, $E=5$ V, $R=5$ kΩ : une entrée à $5$ V suffit, $V_S=5$ V et $I_R=1$ mA",
     "cours": r"Les diodes choisissent automatiquement l'entrée la plus haute (porte OU) ou la plus basse (porte ET). C'est la base historique de la logique électronique."},
    {"id": "redressement", "titre": "Redressement",
     "formule": r"simple alternance (diode et $R$ en série) : idéal $u=e$ si $e > 0$, sinon $0$ · à seuil : $u=e-V_0$ si $e > V_0$ · double alternance (pont de Graetz) : idéal $u=|e|$ · à seuil : $u=|e|-2V_0$ si $|e| > 2V_0$, sinon $0$",
     "exemple": r"pont, $V\sqrt2=10$ V, $V_0=0{,}7$ V : $U_{max}=10-1{,}4=8{,}6$ V",
     "cours": r"Un redresseur transforme une tension alternative en tension de signe constant. Dans le pont de Graetz, deux diodes conduisent à chaque alternance ; avec le modèle à seuil, il faut $|e| > 2V_0$ pour que le courant passe."},
    {"id": "zener", "titre": "Diode Zéner",
     "formule": r"en direct : diode normale ($V_0$, $r_D$) · en inverse : bloquée tant que $|V_{AK}| < |V_Z|$, puis passante (claquage) : source $-|V_Z|$ en série avec $r_Z$ · bloquée si $-|V_Z| < V_{AK} < V_0$",
     "exemple": r"$R$ puis Zéner en sortie, modèles à seuil : $U=V$ pour $-V_0 < V < |V_Z|$, $U=|V_Z|$ au-dessus, $U=-V_0$ en dessous",
     "cours": r"Une diode Zéner est conçue pour conduire en inverse au-delà de la tension Zéner (effet tunnel) sans être détruite. En inverse passante, la tension à ses bornes reste presque égale à $|V_Z|$ : elle sert à écrêter ou à stabiliser une tension."},
    {"id": "stabilisateur", "titre": "Stabilisateur de tension à Zéner",
     "formule": r"$E$, $R$ série, Zéner et charge $R_c$ en parallèle · Thévenin : $E_{th}=\dfrac{R_c}{R+R_c}E$ · Zéner passante si $E_{th}\geq|V_Z|$ : $U=|V_Z|$ · sinon $U=E_{th}$ · $R_{c,min}=\dfrac{|V_Z|}{E-|V_Z|}R$",
     "exemple": r"$E=12$ V, $R=1$ kΩ, $R_c=2{,}2$ kΩ, $|V_Z|=6{,}2$ V : $E_{th}=8{,}25$ V, donc $U=6{,}2$ V",
     "cours": r"Tant que la Zéner conduit en inverse, la tension de sortie reste égale à $|V_Z|$ quelle que soit la charge : la tension est stabilisée. Si la charge devient trop faible ($R_c < R_{c,min}$), $E_{th}$ passe sous $|V_Z|$ et la régulation est perdue."},
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


X25 = "Examen d'électronique « Diodes », mars 2025 (corrigé rédigé, non officiel)"
TD = "TD d'électronique S2 « Les diodes »"
TZ = "TD d'électronique S2 « La diode Zéner »"
PM = "Précisions et méthodes - Diode"
COURS = "Cours « Jonction PN et diodes »"

LEVELS = [
    {"n": 1, "titre": "Polarisation d'une diode", "notions": ["polarisation"], "exos": [
        o("d11", r"Dans quel sens circule le courant dans une diode ? Que signifient polarisation directe et inverse ?",
          r"De l'anode vers la cathode. Directe : $V_{AK} > 0$, la diode peut conduire. Inverse : $V_{AK} < 0$, elle est bloquée (seul un courant inverse négligeable circule).", src=COURS, duree=2),
        o("d12", r"Comment se comporte une diode en polarisation inverse (hors effet Zéner) ?", r"Comme un interrupteur ouvert : courant nul.", src=X25 + ", Q2", duree=1),
        v("d13", r"$E=10$ V, diode idéale dans le sens de $E$, en série avec $R=100$ Ω. Tension $U_R$ (en V) ?", "10", "10", r"Diode passante (fil) : $U_R=E=10$ V.", src=X25 + ", Q3", duree=1),
        v("d14", r"Même circuit, $R=1$ kΩ. $V_{AK}$ (en V) ?", "0", "0", r"Diode idéale passante : $V_{AK}=0$.", src=X25 + ", Q4", duree=1),
        v("d15", r"$E=10$ V, diode à seuil ($V_0=0{,}7$ V) montée en sens inverse, en série avec $R=100$ Ω. $U_R$ (en V) ?", "0", "0", r"Diode bloquée : aucun courant, $U_R=0$.", src=X25 + ", Q5", duree=2),
        v("d16", r"Même circuit, $R=1$ kΩ. $V_{AK}$ (en V) ?", "-10", "-10", r"Pas de courant, $U_R=0$ : toute la tension est sur la diode, en inverse : $V_{AK}=-E=-10$ V.", src=X25 + ", Q6", duree=2),
        o("d17", r"Deux propriétés à citer pour justifier quelles diodes conduisent dans un redresseur.",
          r"Dans une diode, le courant circule toujours de l'anode vers la cathode. Une diode est un dipôle récepteur : le courant descend les potentiels.", src=PM, duree=2),
    ]},
    {"n": 2, "titre": "Modèles de la diode", "notions": ["modeles", "polarisation"], "exos": [
        o("d21", r"Citer les trois modèles statiques d'une diode passante, du moins précis au plus précis.",
          r"Idéal : fil. À seuil : source de tension idéale $V_0$. Réel : source $V_0$ en série avec la résistance dynamique $r_D$. Bloquée : interrupteur ouvert dans les trois cas. Le plus précis est le modèle réel.", src=X25 + ", Q1", duree=3),
        v("d22", r"$E=5$ V, $R=10$ Ω, diode passante, modèle à seuil $V_0=0{,}7$ V. $I$ (en A) ?", "(5-Rational(7,10))/10", "Rational(43,100)", r"Mailles : $E-RI-V_0=0$, $I=\dfrac{E-V_0}R=0{,}43$ A.", src=TD + ", ex. 2", duree=2),
        v("d23", r"Même circuit, modèle réel avec $r_D=1$ Ω. $I$ (en A, exact) ?", "(5-Rational(7,10))/(10+1)", "Rational(43,110)", r"$I=\dfrac{E-V_0}{R+r_D}=\dfrac{4{,}3}{11}\approx0{,}39$ A.", src=TD + ", ex. 2", duree=2),
        v("d24", r"Même circuit avec $R=1$ kΩ, modèle à seuil. $I$ (en mA) ?", "(5-Rational(7,10))/1", "Rational(43,10)", r"$\dfrac{4{,}3}{1000}$ A $=4{,}3$ mA.", src=TD + ", ex. 2", duree=2),
        v("d25", r"$R=1$ kΩ, modèle réel ($r_D=1$ Ω). $I$ (en mA, exact) ?", "(5-Rational(7,10))*1000/1001", "4300/1001", r"$\dfrac{4{,}3}{1001}$ A $\approx4{,}296$ mA : identique au modèle à seuil car $R\gg r_D$.", src=TD + ", ex. 2", duree=2),
        v("d26", r"Tension de seuil typique d'une diode au silicium : borne haute (en V) ?", "Rational(7,10)", "Rational(7,10)", r"$V_0$ entre $0{,}5$ et $0{,}7$ V pour le silicium.", src=COURS, duree=1),
        o("d27", r"Quand les modèles à seuil et réel donnent-ils le même résultat ?", r"Quand la résistance du circuit est grande devant $r_D$ : la chute $r_DI$ est négligeable devant $RI$.", src=TD + ", ex. 2", duree=2),
    ]},
    {"n": 3, "titre": "Raisonnement par l'absurde", "notions": ["absurde", "modeles"], "exos": [
        v("d31", r"$E=10$ V, $R_1=50$ Ω en série, puis $R_2=100$ Ω en parallèle avec la diode ($A$ côté $R_1$). Diode supposée bloquée : $V_{AK}$ (en V) ?", "100/150*10", "Rational(20,3)", r"$R_1$, $R_2$ en série : $V_{AK}=\dfrac{R_2}{R_1+R_2}E=\dfrac{20}3\approx6{,}7$ V $> V_0$ : absurde, la diode est passante.", src=TD + ", ex. 1", duree=3),
        v("d32", r"Même circuit, diode passante ($V_0=0{,}7$ V). $I_{AK}$ (en mA) ?", "((10-Rational(7,10))/50 - Rational(7,10)/100)*1000", "179", r"$I_1=\dfrac{E-V_0}{R_1}=186$ mA, $I_2=\dfrac{V_0}{R_2}=7$ mA, $I_{AK}=I_1-I_2=179$ mA.", src=TD + ", ex. 1", duree=4),
        v("d33", r"$R_1=10$ kΩ, $R_2=10$ Ω. Diode supposée passante : $I_{AK}$ (en mA) ?", "((10-Rational(7,10))/10000 - Rational(7,10)/10)*1000", "-Rational(6907,100)", r"$I_{AK}=\dfrac{9{,}3}{10^4}-\dfrac{0{,}7}{10}\approx-69$ mA $< 0$ : absurde, la diode est bloquée.", src=TD + ", ex. 1", duree=4),
        v("d34", r"Même circuit, diode bloquée. Courant dans $R_2$ (en mA, exact) ?", "10/10010*1000", "Rational(1000,1001)", r"$R_1$, $R_2$ en série : $I_2=\dfrac{E}{R_1+R_2}\approx1$ mA.", src=TD + ", ex. 1", duree=2),
        o("d35", r"Méthode pour montrer qu'une diode est passante.",
          r"On la suppose bloquée et on la remplace par un interrupteur ouvert. On calcule $V_{AK}$ et on montre que $V_{AK} > 0$ (idéal) ou $V_{AK} > V_0$ (seuil, réel) : contradiction, donc elle est passante.", src=PM, duree=3),
        o("d36", r"Méthode pour montrer qu'une diode est bloquée.",
          r"On la suppose passante (fil, source $V_0$ ou $V_0+r_D$). On calcule $I_{AK}$ et on montre qu'il est négatif : impossible, le courant ne va que de l'anode vers la cathode. Donc elle est bloquée.", src=PM, duree=3),
        v("d37", r"Diode bloquée : courant (en A) ?", "0", "0", r"Interrupteur ouvert : $I=0$.", duree=1),
    ]},
    {"n": 4, "titre": "Circuits à diode : calculs", "notions": ["absurde", "modeles"], "exos": [
        v("d41", r"Examen 2025, ex. 2 : $E_2=20$ V alimente $R_2=1$ kΩ en série avec $R_3=1$ kΩ (nœud $N$ entre les deux). Diode supposée bloquée : $V_N$ (en V) ?", "20*1/(1+1)", "10", r"Diviseur : $V_N=\dfrac{R_3}{R_2+R_3}E_2=10$ V.", src=X25 + ", ex. 2", duree=3),
        v("d42", r"Même circuit : la cathode de la diode est reliée au $+$ de $E_1=5$ V, dont le $-$ rejoint la masse par $R_1=2$ kΩ. Diode bloquée : $V_{AK}$ (en V) ?", "10-5", "5", r"Pas de courant dans $R_1$ : $V_K=E_1=5$ V, $V_{AK}=10-5=5$ V $> 0$ : absurde, la diode conduit.", src=X25 + ", ex. 2", duree=3),
        v("d43", r"Même circuit, diode idéale passante. Courant $I$ dans la diode (en mA) ?", "solve([(20-x)/1 - y - x/1, x - 5 - 2*y], [x, y])[y]", "2", r"$V_N=E_1+R_1I$ et nœud $N$ : $\dfrac{E_2-V_N}{R_2}=I+\dfrac{V_N}{R_3}$. Avec les kΩ et mA : $20-V_N=I+V_N$, $V_N=5+2I$, d'où $10=5I$, $I=2$ mA ($V_N=9$ V).", src=X25 + ", ex. 2", duree=6),
        v("d44", r"Même circuit : $V_N$ (en V) ?", "5+2*2", "9", r"$V_N=E_1+R_1I=9$ V, et le courant dans $R_2$ vaut $11$ mA.", src=X25 + ", ex. 2", duree=2),
        v("d45", r"$E=12$ V, $R=1$ kΩ, deux diodes à seuil ($V_0=0{,}7$ V) en série dans le sens passant. $I$ (en mA) ?", "(12-2*Rational(7,10))/1", "Rational(53,5)", r"$I=\dfrac{E-2V_0}{R}=10{,}6$ mA.", duree=2),
        v("d46", r"$E=3$ V, $R=100$ Ω, diode réelle ($V_0=0{,}7$ V, $r_D=15$ Ω). $I$ (en mA) ?", "(3-Rational(7,10))/115*1000", "20", r"$I=\dfrac{2{,}3}{115}=20$ mA.", duree=2),
        o("d47", r"Examen 2025, ex. 2 : rédiger le raisonnement par l'absurde complet.",
          r"Supposons la diode bloquée : $R_2$, $R_3$ en série, $V_N=10$ V ; aucun courant dans $R_1$, $V_K=E_1=5$ V ; $V_{AK}=5$ V $> 0$ : absurde. La diode est passante (fil) : $V_N=E_1+R_1I$, nœud $N$ : $\dfrac{E_2-V_N}{R_2}=I+\dfrac{V_N}{R_3}$, d'où $I=2$ mA $> 0$ (cohérent).", src=X25 + ", ex. 2", duree=8),
    ]},
    {"n": 5, "titre": "Caractéristique de transfert", "notions": ["transfert_d", "absurde"], "exos": [
        v("d51", r"Écrêteur : $V$, $R$ série, puis $R_L$ en parallèle avec deux diodes tête-bêche. Les deux bloquées : $U$ en fonction de $V$ ($R=R_L$) ?", "R*V/(R+R)", "V/2", r"Diviseur : $U=\dfrac{R_L}{R+R_L}V=\dfrac V2$.", src=TD + ", ex. 3", duree=2),
        v("d52", r"Même écrêteur, modèle à seuil $V_0=0{,}7$ V, $R=R_L$ : valeur maximale de $V$ (en V) pour laquelle les deux diodes restent bloquées ?", "(1+1)*Rational(7,10)", "Rational(7,5)", r"Bloquées si $-V_0 < U < V_0$, soit $|V| < \dfrac{R+R_L}{R_L}V_0=1{,}4$ V.", src=TD + ", ex. 3", duree=3),
        v("d53", r"Même écrêteur, modèle réel : $D_1$ passante. $U$ par Millman (symboles `V`, `V0`, `rD`, `R`, `RL`) ?", "(V/R + V0/rD)/(1/R+1/rD+1/RL)", "RL*rD*V/(rD*RL+rD*R+R*RL) + RL*R*V0/(rD*RL+rD*R+R*RL)", r"$U=\dfrac{\frac VR+\frac{V_0}{r_D}}{\frac1R+\frac1{r_D}+\frac1{R_L}}=\dfrac{R_Lr_D}{r_DR_L+r_DR+RR_L}V+\dfrac{R_LR}{r_DR_L+r_DR+RR_L}V_0$.", src=TD + ", ex. 3", duree=5),
        o("d54", r"Pourquoi les deux diodes tête-bêche de l'écrêteur ne peuvent-elles pas être passantes en même temps ?",
          r"$D_1$ passante impose $V_{AK_1}\geq V_0$. Les diodes sont tête-bêche : $V_{AK_2}=-V_{AK_1}\leq-V_0$, donc $D_2$ est bloquée. Il reste trois cas : les deux bloquées, $D_1$ seule, $D_2$ seule.", src=TD + ", ex. 3", duree=4),
        v("d55", r"Examen 2025, ex. 3 : $V$, puis ($R$ en parallèle avec une diode, anode côté sortie), puis $R$ en sortie. Diode bloquée : $U$ ?", "R*V/(R+R)", "V/2", r"Pas de courant dans la diode : diviseur, $U=\dfrac V2$.", src=X25 + ", ex. 3", duree=3),
        v("d56", r"Même circuit, diode passante (modèle à seuil) : $U$ en fonction de $V$, $V_0$ ?", "V + V0", "V+V0", r"La diode impose $V_{AK}=U-V=V_0$, donc $U=V+V_0$.", src=X25 + ", ex. 3", duree=3),
        v("d57", r"Même circuit : la diode est bloquée pour $V >$ ? (en fonction de $V_0$)", "solve(V/2 - V - V0, V)[0]", "-2*V0", r"Bloquée si $V_{AK}=U-V=-\dfrac V2 < V_0$, soit $V > -2V_0$. Pour $V\leq-2V_0$ : $U=V+V_0$. La courbe est continue en $V=-2V_0$ ($U=-V_0$).", src=X25 + ", ex. 3", duree=4),
    ]},
    {"n": 6, "titre": "Portes logiques à diodes", "notions": ["portes", "polarisation"], "exos": [
        v("d61", r"Porte OU (diodes idéales, anodes sur $A$ et $B$, cathodes sur $R=5$ kΩ vers la masse). $V_A=5$ V, $V_B=0$ : $V_S$ (en V) ?", "5", "5", r"$D_A$ passante : $V_S=V_A=5$ V ; $D_B$ bloquée ($V_{AK}=-5$ V).", src=TD + ", ex. 4", duree=2),
        v("d62", r"Même porte : $I_R$ (en mA) ?", "5/5", "1", r"$I_R=\dfrac{V_S}R=1$ mA.", src=TD + ", ex. 4", duree=1),
        v("d63", r"Même porte, $V_A=V_B=5$ V : courant dans chaque diode (en mA) ?", "Rational(1,2)", "Rational(1,2)", r"Les deux conduisent et se partagent $I_R=1$ mA : $0{,}5$ mA chacune.", src=TD + ", ex. 4", duree=2),
        v("d64", r"Porte ET ($R=5$ kΩ vers $E=5$ V, anodes communes, cathodes sur $A$ et $B$). $V_A=0$, $V_B=5$ V : $V_S$ (en V) ?", "0", "0", r"$D_A$ conduit et impose $V_S=V_A=0$ ; $D_B$ est bloquée.", src=TD + ", ex. 4", duree=2),
        v("d65", r"Même porte ET, $V_A=V_B=0$ : courant $I_R$ (en mA) ?", "5/5", "1", r"$I_R=\dfrac{E-V_S}{R}=1$ mA, partagé : $0{,}5$ mA par diode.", src=TD + ", ex. 4", duree=2),
        v("d66", r"Même porte ET, $V_A=V_B=5$ V : $I_R$ (en mA) ?", "0", "0", r"Les deux diodes sont bloquées ($V_{AK}\leq0$), $V_S=E=5$ V et $I_R=0$.", src=TD + ", ex. 4", duree=2),
        o("d67", r"Pourquoi le premier montage réalise-t-il un OU et le second un ET ?",
          r"OU : une seule entrée haute suffit à rendre sa diode passante et à porter la sortie à $5$ V. ET : une seule entrée basse suffit à tirer la sortie à $0$ ; la sortie n'est haute que si toutes les entrées le sont.", src=TD + ", ex. 4", duree=3),
    ]},
    {"n": 7, "titre": "Redressement simple alternance", "notions": ["redressement", "modeles"], "exos": [
        v("d71", r"$e(t)=E\sqrt2\sin(\omega t)$, diode idéale et $R$ en série. $u$ quand $e < 0$ (en V) ?", "0", "0", r"La diode est bloquée ($V_{AK}=e < 0$), aucun courant : $u=0$.", src=TD + ", ex. 5", duree=2),
        v("d72", r"Même montage, $e > 0$ : $u$ en fonction de $e$ (symbole `e`) ?", "e", "e", r"Diode passante (fil) : $u=e$.", src=TD + ", ex. 5", duree=1),
        v("d73", r"Modèle à seuil : $u$ quand la diode conduit (symboles `e`, `V0`) ?", "e - V0", "e-V0", r"$u=e-V_0$, pour $e > V_0$.", src=TD + ", ex. 5", duree=2),
        v("d74", r"$E\sqrt2=10$ V, $V_0=0{,}7$ V. Valeur maximale de $u$ (en V) ?", "10-Rational(7,10)", "Rational(93,10)", r"$U_{max}=E\sqrt2-V_0=9{,}3$ V.", src=TD + ", ex. 5", duree=2),
        v("d75", r"Même montage, $E\sqrt2=10$ V, modèle idéal. Tension inverse maximale aux bornes de la diode (en V) ?", "-10", "-10", r"Quand $e=-E\sqrt2$, $u=0$ et $V_{AK}=e=-10$ V.", duree=2),
        o("d76", r"Allure de $u(t)$ pour le redresseur simple alternance (modèles idéal puis à seuil).",
          r"Idéal : $u$ reproduit les alternances positives de $e$ et vaut $0$ pendant les négatives. À seuil : même allure, arches abaissées de $V_0$ et plus courtes ($u=0$ tant que $e < V_0$).", src=TD + ", ex. 5", duree=4),
        v("d77", r"Valeur maximale de $u$ (en V) si $E\sqrt2=0{,}5$ V et $V_0=0{,}7$ V ?", "0", "0", r"$e$ ne dépasse jamais $V_0$ : la diode reste bloquée, $u=0$.", duree=2),
    ]},
    {"n": 8, "titre": "Pont de Graetz (double alternance)", "notions": ["redressement", "polarisation"], "exos": [
        o("d81", r"Pont de Graetz : combien de diodes conduisent à chaque alternance, et lesquelles ?",
          r"Deux, en diagonale : celles qui permettent au courant d'aller de la borne haute du générateur vers $R$ puis de revenir à la borne basse. À l'alternance suivante, ce sont les deux autres. Le courant traverse $R$ toujours dans le même sens.", src=TD + ", ex. 6", duree=3),
        v("d82", r"Pont, diodes idéales : $u$ en fonction de $v$ (symbole `v`) quand $v > 0$ ?", "v", "v", r"Mailles : $u=v-V_1-V_3$ avec $V_1=V_3=0$.", src=TD + ", ex. 6", duree=2),
        v("d83", r"Même pont, $v < 0$ : $u$ ?", "-v", "-v", r"$u=-v-V_2-V_4=-v$ : au total $u=|v|$.", src=TD + ", ex. 6", duree=2),
        v("d84", r"Pont, modèle à seuil, $V\sqrt2=10$ V, $V_0=0{,}7$ V. $U_{max}$ (en V) ?", "10-2*Rational(7,10)", "Rational(43,5)", r"$U_{max}=V\sqrt2-2V_0=8{,}6$ V.", src=TD + ", ex. 6", duree=2),
        v("d85", r"Même pont : $u$ est nulle tant que $|v|$ est inférieure à (en V) ?", "2*Rational(7,10)", "Rational(7,5)", r"Il faut $|v| > 2V_0=1{,}4$ V pour que deux diodes conduisent ; sinon au moins trois sont bloquées et $u=0$.", src=TD + ", ex. 6", duree=2),
        v("d86", r"$e(t)$ de fréquence $50$ Hz redressée double alternance. Fréquence de $u(t)$ (en Hz) ?", "2*50", "100", r"$|e|$ a pour période $T/2$ : $100$ Hz.", duree=2),
        o("d87", r"Examen 2025, ex. 4 (bonus) : $e(t)$ triangulaire d'amplitude $E_M > 2V_0$, pont à seuil. Allure de $u(t)$ ?",
          r"$u=|e|-2V_0$ quand $|e| > 2V_0$, sinon $u=0$ : des triangles positifs de hauteur $E_M-2V_0$, à chaque alternance, séparés par des paliers nuls autour des passages de $e$ par $0$.", src=X25 + ", ex. 4 bonus", duree=5),
    ]},
    {"n": 9, "titre": "Diode Zéner", "notions": ["zener", "modeles"], "exos": [
        o("d91", r"Qu'est-ce qu'une diode Zéner ? Comment se comporte-t-elle en direct et en inverse ?",
          r"Une diode conçue pour conduire en inverse au-delà de la tension Zéner (effet tunnel). En direct : diode normale ($V_0$). En inverse : bloquée tant que $|V_{AK}| < |V_Z|$, puis passante avec $V_{AK}\approx-|V_Z|$.", src=COURS, duree=3),
        v("d92", r"$V$, $R$ série, Zéner en sortie (cathode en haut), modèles à seuil, $V_0=0{,}7$ V, $|V_Z|=4{,}3$ V. $V=3$ V : $U$ (en V) ?", "3", "3", r"$-V_0 < V < |V_Z|$ : Zéner bloquée, pas de courant, $U=V=3$ V.", src=TZ + ", ex. 1", duree=2),
        v("d93", r"Même circuit, $V=10$ V : $U$ (en V) ?", "Rational(43,10)", "Rational(43,10)", r"$V > |V_Z|$ : Zéner passante en inverse, $U=|V_Z|=4{,}3$ V.", src=TZ + ", ex. 1", duree=2),
        v("d94", r"Même circuit, $V=-5$ V : $U$ (en V) ?", "-Rational(7,10)", "-Rational(7,10)", r"$V < -V_0$ : passante en direct, $U=-V_0=-0{,}7$ V.", src=TZ + ", ex. 1", duree=2),
        v("d95", r"Même circuit, modèle réel en inverse ($r_Z$) : $U$ par Millman (symboles `V`, `Vz`, `rz`, `R`) ?", "(V/R + Vz/rz)/(1/R + 1/rz)", "rz*V/(R+rz) + R*Vz/(R+rz)", r"$U=\dfrac{\frac VR+\frac{|V_Z|}{r_Z}}{\frac1R+\frac1{r_Z}}=\dfrac{r_Z}{R+r_Z}V+\dfrac{R}{R+r_Z}|V_Z|$.", src=TZ + ", ex. 1", duree=4),
        v("d96", r"Condition de blocage d'une Zéner : $V_{AK}$ doit être inférieure à (borne haute, symbole `V0`) ?", "V0", "V0", r"Bloquée si $-|V_Z| < V_{AK} < V_0$.", src=TZ, duree=1),
        o("d97", r"Pourquoi faut-il $V_0\ll|V_Z|$ et $r_D$, $r_Z$ faibles pour que le tracé de la caractéristique soit réaliste ?",
          r"Pour que les morceaux où la diode conduit soient presque horizontaux (tension quasi constante, $U\approx|V_Z|$ ou $U\approx-V_0$) et que le palier de blocage soit nettement plus large que la zone directe.", src=TZ + ", ex. 1", duree=3),
    ]},
    {"n": 10, "titre": "Zéner : écrêtage", "notions": ["zener", "transfert_d"], "exos": [
        v("d101", r"$v$, $R$ série, puis diode normale et Zéner en série tête-bêche en sortie ($V_0=0{,}7$ V, $|V_Z|=4{,}3$ V). Tension de sortie maximale (en V) ?", "Rational(7,10)+Rational(43,10)", "5", r"$D$ passante en direct et $D_Z$ en inverse : $v_{out}=V_0+|V_Z|=5$ V.", src=TZ + ", ex. 2", duree=3),
        v("d102", r"Même montage, $v_{in}=3$ V : $v_{out}$ (en V) ?", "3", "3", r"$v_{in} < V_0+|V_Z|$ : au moins une diode bloquée, pas de courant, $v_{out}=v_{in}$.", src=TZ + ", ex. 2", duree=2),
        v("d103", r"Même montage, $v_{in}=-8$ V : $v_{out}$ (en V) ?", "-8", "-8", r"La diode normale est bloquée en inverse (pas de borne inférieure) : $v_{out}=v_{in}$.", src=TZ + ", ex. 2", duree=2),
        o("d104", r"Pourquoi la diode normale et la Zéner de l'exercice 2 ne peuvent-elles pas conduire « en direct » toutes les deux ?",
          r"Elles sont tête-bêche : pour que le courant traverse les deux, il faut la diode normale en direct et la Zéner en inverse (claquage). Une diode classique ne conduit jamais de la cathode vers l'anode.", src=TZ + ", ex. 2", duree=3),
        v("d105", r"Ex. 3 : $V$, $R$, puis $R_L$ en parallèle avec deux Zéner tête-bêche. Les deux bloquées pour $|V| < V_T$ : $V_T$ (symboles `R`, `RL`, `V0`, `Vz`) ?", "(1+R/RL)*(V0+Vz)", "(R+RL)*(V0+Vz)/RL", r"Bloquées si $|U| < V_0+|V_Z|$ avec $U=\dfrac{R_L}{R+R_L}V$, donc $V_T=\left(1+\dfrac R{R_L}\right)(V_0+|V_Z|)$.", src=TZ + ", ex. 3", duree=4),
        v("d106", r"Même montage, $R=R_L$, $V_0=0{,}7$ V, $|V_Z|=4{,}3$ V : $V_T$ (en V) ?", "2*(Rational(7,10)+Rational(43,10))", "10", r"$V_T=2\times5=10$ V.", src=TZ + ", ex. 3", duree=2),
        v("d107", r"Même montage, modèle à seuil, $V=20$ V : $U$ (en V) ?", "Rational(7,10)+Rational(43,10)", "5", r"$V > V_T$ : $U$ écrêtée à $V_0+|V_Z|=5$ V.", src=TZ + ", ex. 3", duree=2),
    ]},
    {"n": 11, "titre": "Stabilisateur de tension", "notions": ["stabilisateur", "zener"], "exos": [
        v("d111", r"$E=12$ V, $R=1$ kΩ, Zéner et $R_c=2{,}2$ kΩ en parallèle. $E_{th}$ (en V) ?", "12*Rational(22,10)/(1+Rational(22,10))", "Rational(33,4)", r"$E_{th}=\dfrac{R_c}{R+R_c}E=\dfrac{2{,}2}{3{,}2}\times12=8{,}25$ V.", src=TZ + ", ex. 4", duree=2),
        v("d112", r"Même montage, $|V_Z|=6{,}2$ V : $U$ (en V) ?", "Rational(62,10)", "Rational(31,5)", r"$E_{th}=8{,}25$ V $\geq|V_Z|$ : Zéner passante en inverse, $U=|V_Z|=6{,}2$ V.", src=TZ + ", ex. 4", duree=2),
        v("d113", r"Même montage avec $E=8$ V : $U$ (en V) ?", "8*Rational(22,10)/(1+Rational(22,10))", "Rational(11,2)", r"$E_{th}=5{,}5$ V $< 6{,}2$ V : Zéner bloquée, $U=E_{th}=5{,}5$ V.", src=TZ + ", ex. 4", duree=2),
        v("d114", r"Même montage, $E=12$ V : $R_{th}$ (en kΩ) ?", "1*Rational(22,10)/(1+Rational(22,10))", "Rational(11,16)", r"$R_{th}=R\parallel R_c=\dfrac{2{,}2}{3{,}2}\approx0{,}69$ kΩ.", src=TZ + ", ex. 4", duree=2),
        v("d115", r"$E=12$ V, $R=1$ kΩ, $|V_Z|=6{,}2$ V : $R_{c,min}$ (en kΩ, exact) ?", "Rational(62,10)/(12-Rational(62,10))*1", "Rational(31,29)", r"$E_{th}=|V_Z|$ donne $R_{c,min}=\dfrac{|V_Z|}{E-|V_Z|}R=\dfrac{6{,}2}{5{,}8}\approx1{,}07$ kΩ $\approx1$ kΩ.", src=TZ + ", ex. 4", duree=3),
        o("d116", r"Démontrer $R_{c,min}=\dfrac{|V_Z|}{E-|V_Z|}R$.",
          r"La tension est stabilisée tant que la Zéner conduit en inverse, soit $E_{th}=\dfrac{R_c}{R+R_c}E\geq|V_Z|$. À la limite : $R_{c,min}E=(R+R_{c,min})|V_Z|$, donc $R_{c,min}(E-|V_Z|)=R|V_Z|$.", src=TZ + ", ex. 4", duree=4),
        o("d117", r"Pourquoi la Zéner du stabilisateur ne peut-elle pas être passante en direct ?",
          r"$E > 0$ impose $U > 0$ côté cathode, donc $V_{AK}=-U < 0$ : la diode ne peut être que bloquée ou passante en inverse.", src=TZ + ", ex. 4", duree=2),
    ]},
    {"n": 12, "titre": "Niveau examen : diodes, mars 2025", "notions": ["modeles", "absurde", "transfert_d", "redressement"], "examen": True, "exos": [
        o("xe1", r"Exercice 1 (QCM) : modèle le plus précis ; diode en inverse ; $E=10$ V, diode idéale directe, $R$ : $U_R$ et $V_{AK}$ ; diode à seuil inverse : $U_R$ et $V_{AK}$.",
          r"Modèle réel ; interrupteur ouvert ; $U_R=10$ V, $V_{AK}=0$ ; $U_R=0$, $V_{AK}=-10$ V.", src=X25 + ", ex. 1 (3 points)", duree=5),
        v("xe2", r"Exercice 2 : $R_1=2$ kΩ, $R_2=R_3=1$ kΩ, $E_1=5$ V, $E_2=20$ V, diode idéale. Courant dans la diode (en mA) ?", "solve([(20-x)/1 - y - x/1, x - 5 - 2*y], [x, y])[y]", "2", r"Bloquée : $V_{AK}=10-5=5$ V $> 0$, absurde. Passante : $V_N=E_1+R_1I$ et $\dfrac{E_2-V_N}{R_2}=I+\dfrac{V_N}{R_3}$, donc $I=2$ mA.", src=X25 + ", ex. 2 (5 points)", duree=10),
        v("xe3", r"Exercice 3.1 : $U$ quand la diode conduit (modèle à seuil) ?", "V + V0", "V+V0", r"$U-V=V_0$.", src=X25 + ", ex. 3 (6 points)", duree=4),
        v("xe4", r"Exercice 3.2 : $U$ quand la diode est bloquée ?", "R*V/(2*R)", "V/2", r"Diviseur $R$, $R$ : $U=\dfrac V2$.", src=X25 + ", ex. 3", duree=3),
        v("xe5", r"Exercice 3.3 : avec $V_0=0{,}7$ V, la diode est bloquée pour $V >$ (en V) ?", "-2*Rational(7,10)", "-Rational(7,5)", r"$V_{AK}=-\dfrac V2 < V_0$ donne $V > -2V_0=-1{,}4$ V.", src=X25 + ", ex. 3", duree=4),
        o("xe6", r"Exercice 4 : pont (diodes $D_1$ à $D_4$ toutes orientées vers $C$, $e(t)$ entre $A$ et $D$, $+$ en $A$, $R$ entre $C$ et $B$), modèle idéal. Diodes passantes et expression de $u$ pour $e > 0$ puis $e < 0$.",
          r"$e > 0$ : $A$ est la borne haute, le courant va $A\to D_4\to C\to R\to B\to D_1\to D$ : $D_4$ et $D_1$ passantes, $u=e$. $e < 0$ : $D_2$ et $D_3$ passantes, $u=-e$. Donc $u=|e|$ (redressement double alternance).", src=X25 + ", ex. 4 (6 points)", duree=10),
        v("xe7", r"Exercice 4 bonus : modèle à seuil, $E_M=5$ V, $V_0=0{,}7$ V. Valeur maximale de $u$ (en V) ?", "5-2*Rational(7,10)", "Rational(18,5)", r"$u=|e|-2V_0$ quand $|e| > 2V_0$ : $U_{max}=3{,}6$ V.", src=X25 + ", ex. 4 bonus", duree=4),
    ]},
]


def _v(enonce, calc, ans, sol):
    return {"enonce": enonce, "calc": calc, "ans": ans, "sol": sol}


VARIANTS = {
    "d22": [_v(r"$E=10$ V, $R=100$ Ω, modèle à seuil $V_0=0{,}7$ V. $I$ (en mA) ?", "(10-Rational(7,10))/100*1000", "93", r"$\dfrac{9{,}3}{100}$ A $=93$ mA.")],
    "d24": [_v(r"$E=12$ V, $R=2$ kΩ, modèle à seuil. $I$ (en mA) ?", "(12-Rational(7,10))/2", "Rational(113,20)", r"$\dfrac{11{,}3}{2}=5{,}65$ mA.")],
    "d45": [_v(r"$E=5$ V, $R=1$ kΩ, deux diodes à seuil en série. $I$ (en mA) ?", "(5-2*Rational(7,10))/1", "Rational(18,5)", r"$3{,}6$ mA.")],
    "d62": [_v(r"Porte OU, $R=10$ kΩ, une entrée à $5$ V : $I_R$ (en mA) ?", "5/10", "Rational(1,2)", r"$0{,}5$ mA.")],
    "d74": [_v(r"$E\sqrt2=15$ V, $V_0=0{,}7$ V. $U_{max}$ (en V) ?", "15-Rational(7,10)", "Rational(143,10)", r"$14{,}3$ V.")],
    "d84": [_v(r"Pont à seuil, $V\sqrt2=12$ V. $U_{max}$ (en V) ?", "12-2*Rational(7,10)", "Rational(53,5)", r"$12-1{,}4=10{,}6$ V.")],
    "d93": [_v(r"Même circuit avec $|V_Z|=5{,}1$ V, $V=12$ V : $U$ (en V) ?", "Rational(51,10)", "Rational(51,10)", r"$U=|V_Z|=5{,}1$ V.")],
    "d106": [_v(r"Même montage, $R_L=2R$, $V_0=0{,}7$ V, $|V_Z|=4{,}3$ V : $V_T$ (en V) ?", "Rational(3,2)*5", "Rational(15,2)", r"$\left(1+\tfrac12\right)\times5=7{,}5$ V.")],
    "d111": [_v(r"$E=16$ V, $R=1$ kΩ, $R_c=3$ kΩ. $E_{th}$ (en V) ?", "16*3/(1+3)", "12", r"$\tfrac34\times16=12$ V.")],
    "d115": [_v(r"$E=15$ V, $R=1$ kΩ, $|V_Z|=5$ V : $R_{c,min}$ (en kΩ) ?", "5/(15-5)", "Rational(1,2)", r"$\dfrac{5}{10}=0{,}5$ kΩ.")],
    "xe7": [_v(r"Exercice 4 bonus : $E_M=10$ V, $V_0=0{,}7$ V. $U_{max}$ (en V) ?", "10-2*Rational(7,10)", "Rational(43,5)", r"$8{,}6$ V.")],
}
for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["id"] in VARIANTS:
            _e["variants"] = VARIANTS[_e["id"]]


EXTRA_PARTS = []

QUIZ = [
    {"notion": "polarisation", "type": "qcm", "q": r"Dans une diode, le courant circule :", "choix": [r"de l'anode vers la cathode", r"de la cathode vers l'anode", r"dans les deux sens", r"seulement en inverse"], "bonne": 0},
    {"notion": "polarisation", "type": "vf", "q": r"En inverse, une diode classique se comporte comme un interrupteur ouvert.", "bonne": True},
    {"notion": "modeles", "type": "qcm", "q": r"Le modèle le plus précis d'une diode est :", "choix": [r"le modèle réel ($V_0$ et $r_D$)", r"le modèle idéal", r"le modèle à seuil", r"ils se valent"], "bonne": 0},
    {"notion": "modeles", "type": "vf", "q": r"Dans le modèle à seuil, une diode passante est une source de tension $V_0$.", "bonne": True},
    {"notion": "absurde", "type": "qcm", "q": r"Pour montrer qu'une diode est bloquée, on la suppose passante et on trouve :", "choix": [r"$I_{AK} < 0$", r"$V_{AK} > V_0$", r"$I_{AK} > 0$", r"$V_{AK}=0$"], "bonne": 0},
    {"notion": "absurde", "type": "vf", "q": r"Supposée bloquée, une diode avec $V_{AK} > V_0$ est en réalité passante.", "bonne": True},
    {"notion": "transfert_d", "type": "qcm", "q": r"La caractéristique de transfert d'un montage est :", "choix": [r"$U=f(V)$", r"$U=f(t)$", r"$I=f(V_{AK})$", r"$G=f(\omega)$"], "bonne": 0},
    {"notion": "transfert_d", "type": "vf", "q": r"Deux diodes tête-bêche peuvent être passantes en même temps.", "bonne": False},
    {"notion": "portes", "type": "qcm", "q": r"Diodes avec anodes sur les entrées et cathodes communes reliées à la masse par $R$ :", "choix": [r"porte OU", r"porte ET", r"porte NON", r"porte OU exclusif"], "bonne": 0},
    {"notion": "portes", "type": "vf", "q": r"Dans une porte ET à diodes, une seule entrée à $0$ suffit à mettre la sortie à $0$.", "bonne": True},
    {"notion": "redressement", "type": "qcm", "q": r"Pont de Graetz, modèle à seuil : $U_{max}=$", "choix": [r"$V\sqrt2-2V_0$", r"$V\sqrt2-V_0$", r"$V\sqrt2$", r"$2V\sqrt2$"], "bonne": 0},
    {"notion": "redressement", "type": "vf", "q": r"Dans un pont de Graetz, deux diodes conduisent à chaque alternance.", "bonne": True},
    {"notion": "zener", "type": "qcm", "q": r"En inverse, au-delà de $|V_Z|$, une diode Zéner :", "choix": [r"conduit avec $V_{AK}\approx-|V_Z|$", r"est détruite", r"reste bloquée", r"conduit avec $V_{AK}=V_0$"], "bonne": 0},
    {"notion": "zener", "type": "vf", "q": r"En direct, une Zéner se comporte comme une diode normale.", "bonne": True},
    {"notion": "stabilisateur", "type": "qcm", "q": r"Le stabilisateur à Zéner fournit $U=|V_Z|$ tant que :", "choix": [r"$E_{th}\geq|V_Z|$", r"$E_{th} < |V_Z|$", r"$R_c=0$", r"$E < |V_Z|$"], "bonne": 0},
    {"notion": "stabilisateur", "type": "vf", "q": r"Une charge trop faible ($R_c < R_{c,min}$) fait perdre la régulation.", "bonne": True},
]

_P = r"courant de $A$ vers $K$ · directe $V_{AK} > 0$ · inverse : interrupteur ouvert"
_M = r"idéal : fil · seuil : $V_0$ · réel : $V_0+r_DI$ · bloquée : $I=0$"
_A = r"supposée bloquée $\to V_{AK} > V_0$ absurde · supposée passante $\to I_{AK} < 0$ absurde"
_K = r"mailles : $\sum U=0$ · nœuds : $\sum I_e=\sum I_s$ · diviseur : $\dfrac{R_2}{R_1+R_2}E$"
_T = r"états possibles $\to$ $U$ dans chaque cas $\to$ domaines de $V$ · courbe continue"
_G = r"OU : $V_S=\max(V_A,V_B)$ · ET : $V_S=\min(V_A,V_B)$ (diodes idéales)"
_R = r"simple : $u=e-V_0$ si $e > V_0$ · pont : $u=|e|-2V_0$ si $|e| > 2V_0$"
_Z = r"bloquée si $-|V_Z| < V_{AK} < V_0$ · inverse passante : $V_{AK}=-|V_Z|$ (plus $r_ZI$)"
_S = r"$E_{th}=\dfrac{R_c}{R+R_c}E$ · $U=|V_Z|$ si $E_{th}\geq|V_Z|$ · $R_{c,min}=\dfrac{|V_Z|}{E-|V_Z|}R$"
_MI = r"Millman : $V_A=\dfrac{\sum E_i/R_i}{\sum1/R_i}$"

FORMULES = {
    "d11": _P, "d12": _P, "d13": _P + " · " + _M, "d14": _M, "d15": _P + " · " + _M, "d16": _P + " · " + _K, "d17": _P,
    "d21": _M, "d22": _M + " · " + _K, "d23": _M + " · " + _K, "d24": _M, "d25": _M, "d26": r"$V_0\approx0{,}5$ à $0{,}7$ V (silicium)", "d27": _M,
    "d31": _A + " · " + _K, "d32": _A + " · " + _K, "d33": _A + " · " + _K, "d34": _K, "d35": _A, "d36": _A, "d37": _M,
    "d41": _A + " · " + _K, "d42": _A, "d43": _K + " · " + _M, "d44": _K, "d45": _M + " · " + _K, "d46": _M + " · " + _K, "d47": _A + " · " + _K,
    "d51": _T + " · " + _K, "d52": _T, "d53": _T + " · " + _MI, "d54": _T + " · " + _P, "d55": _T + " · " + _K, "d56": _T + " · " + _M, "d57": _T + " · " + _A,
    "d61": _G, "d62": _G + r" · $I=U/R$", "d63": _G, "d64": _G, "d65": _G, "d66": _G, "d67": _G,
    "d71": _R, "d72": _R, "d73": _R, "d74": _R, "d75": _R + " · " + _K, "d76": _R, "d77": _R,
    "d81": _R + " · " + _P, "d82": _R, "d83": _R, "d84": _R, "d85": _R, "d86": r"$|e|$ : période $T/2$", "d87": _R,
    "d91": _Z, "d92": _Z, "d93": _Z, "d94": _Z, "d95": _Z + " · " + _MI, "d96": _Z, "d97": _Z,
    "d101": _Z, "d102": _Z, "d103": _Z + " · " + _P, "d104": _Z + " · " + _P, "d105": _Z + " · " + _K, "d106": _Z, "d107": _Z,
    "d111": _S, "d112": _S, "d113": _S, "d114": _S + r" · $R_{th}=R\parallel R_c$", "d115": _S, "d116": _S, "d117": _S + " · " + _P,
    "xe1": _P + " · " + _M, "xe2": _A + " · " + _K, "xe3": _T + " · " + _M, "xe4": _T + " · " + _K, "xe5": _T + " · " + _A, "xe6": _R + " · " + _P, "xe7": _R,
}


# ---------------------------------------------------------------- circuit figures (`schema.py`)

def _ex2(d):
    """Exam March 2025, ex. 2: N between R2 (to E2+) and R3; diode from N (anode) to E1+ (cathode)."""
    d += (s := SrcU().endpoints((0, 0), (0, 2.5)))
    tension(d, s, "$E_1$")
    d += Fil().endpoints((0, 2.5), (0, 3))
    d += D().endpoints((4, 3), (0, 3)).label("$D$")
    d += Point().at((4, 3)).label("$N$", loc="left")
    d += R().endpoints((4, 6), (4, 3)).label("$R_2$")
    d += R().endpoints((4, 3), (4, 0)).label("$R_3$")
    d += R().endpoints((0, 0), (4, 0)).label("$R_1$", loc="bottom")
    d += Fil().endpoints((4, 6), (7, 6))
    d += (s := SrcU().endpoints((7, 0), (7, 6)))
    tension(d, s, "$E_2$", cote=False)
    d += Fil().endpoints((4, 0), (7, 0))


def _ex3(d):
    """Exam March 2025, ex. 3: R in parallel with a diode (anode on the output side), then R at the output."""
    d += (s := SrcU().endpoints((0, 0), (0, 3)))
    tension(d, s, "$V$")
    d += R().endpoints((0, 3), (4, 3)).label("$R$", loc="bottom")
    d += Fil().endpoints((0, 3), (0, 4.5))
    d += D().endpoints((4, 4.5), (0, 4.5)).label("$D$")
    d += Fil().endpoints((4, 4.5), (4, 3))
    d += (r := R().endpoints((4, 3), (4, 0)).label("$R$", loc="top"))
    tension(d, r, "$U$", sens=-1)
    d += Fil().endpoints((0, 0), (4, 0))


S, P = "s", "p"
FIG_DIRECT = schema_echelle("E", [(S, "D", "D"), (P, "R", "R")], "U_R")
FIG_INVERSE = schema_echelle("E", [(S, "D<", "D"), (P, "R", "R")], "U_R")
FIG_SERIE = schema_echelle("E", [(S, "R", "R"), (S, "D", "D")])
FIG_SHUNT = schema_echelle("E", [(S, "R", "R_1"), (P, "R", "R_2"), (P, "D", "D")])
FIG_DEUX = schema_echelle("E", [(S, "R", "R"), (S, "D", "D_1"), (S, "D", "D_2")])
FIG_ECRETEUR = schema_echelle("V", [(S, "R", "R"), (P, "R", "R_L"), (P, "D", "D_1"), (P, "D<", "D_2")], "U")
FIG_REDRESSEUR = schema_echelle("e(t)", [(S, "D", "D"), (P, "R", "R")], "u")
FIG_ZENER = schema_echelle("V", [(S, "R", "R"), (P, "DZ<", "D_Z")], "U")
FIG_REGUL = schema_echelle("E", [(S, "R", "R"), (P, "DZ<", "D_Z"), (P, "R", "R_c")], "U")
FIG_EX2 = fig(_ex2, "Schéma : E2 alimente R2 puis R3 (nœud N entre les deux) ; diode de N (anode) vers le + de E1 (cathode) ; le - de E1 rejoint la masse par R1")
FIG_EX3 = fig(_ex3, "Schéma : source V, puis R en parallèle avec une diode (anode côté sortie), puis R en sortie (tension U)")

FIGS = {**dict.fromkeys(["d13", "d14"], FIG_DIRECT), **dict.fromkeys(["d15", "d16"], FIG_INVERSE),
        **dict.fromkeys(["d22", "d23", "d24"], FIG_SERIE),
        **dict.fromkeys(["d31", "d32", "d33", "d34"], FIG_SHUNT), "d45": FIG_DEUX,
        **dict.fromkeys(["d51", "d52", "d53", "d54"], FIG_ECRETEUR),
        **dict.fromkeys(["d71", "d72", "d73", "d74", "d75"], FIG_REDRESSEUR),
        **dict.fromkeys(["d92", "d93", "d94", "d95"], FIG_ZENER),
        **dict.fromkeys(["d111", "d112", "d113", "d114"], FIG_REGUL),
        **dict.fromkeys(["d41", "d42", "d43", "d44", "d47", "xe2"], FIG_EX2),
        **dict.fromkeys(["d55", "d56", "d57", "xe3", "xe4", "xe5"], FIG_EX3)}
ajoute(LEVELS, FIGS)
