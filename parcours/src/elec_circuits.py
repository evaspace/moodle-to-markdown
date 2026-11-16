"""Level path: S1 electronics, circuit analysis tools (definitions, laws, theorems), promo 2031.

Calibrated on the Moodle course « S1 - Electronique - Promo 2030 » (`Concepts de base`, `Kit de survie régime sinusoïdal`),
TD1-4 and the B1 exams of October 2024 and October 2025 (`Examen1 Elec - InfoS1`). Exam circuits are redrawn as SVG
(`schema.py`, `FIGS`); every circuit is still described in words (series / parallel / node names) so that each
answer can be computed and the copy-for-AI text stays complete.
Units: V, A, Ω; k = 10^3 and m = 10^-3 are written inside the numbers (answers in the stated unit).
"""
from .schema import Fil, Inter, Point, R, SrcI, SrcU, ajoute, courant, fig, tension

SUBJECT = {
    "id": "elec-s1-circuits",
    "ordre": 500,
    "matiere": "electronique",
    "semestre": "S1",
    "ecue": "Outils d'analyse de circuits",
    "titre": "Outils d'analyse de circuits : lois et théorèmes",
    "chapitres_moodle": ["01_Outils d'analyse de circuits - Définitions, Lois et Théorèmes [2526_I_INF_FISE_S01_CN_OAC]", "02_Documents de cours", "05_Travaux Dirigés"],
    "td": "TD 1 à 4 d'électronique S1 (lois fondamentales, Thévenin/Norton, Millman, régime sinusoïdal)",
    "examens": ["Examen B1 d'électronique (octobre)", "Examen B2 d'électronique (janvier)"],
}

NOTIONS = [
    {"id": "grandeurs", "titre": "Courant, tension, puissance",
     "formule": r"$Q=I\,t$ · $U_{AB}=V_A-V_B$ · $P=U\,I$ · $W=P\,t$ · récepteur : $U$ et $I$ en sens opposés · générateur : $U$ et $I$ dans le même sens",
     "exemple": r"$I=2$ A pendant $5$ s : $Q=10$ C",
     "cours": r"Le courant est un déplacement ordonné de charges (en ampères) ; la tension est une différence de potentiel entre deux points (en volts). Le courant qui entre dans un dipôle ressort du même dipôle avec la même intensité. Un dipôle reçoit de la puissance si $P=UI>0$ en convention récepteur."},
    {"id": "dipoles", "titre": "Dipôles : résistance, condensateur, bobine",
     "formule": r"$U=R\,I$ · $P=R\,I^2=U^2/R$ · $i=C\dfrac{du}{dt}$ · $u=L\dfrac{di}{dt}$ · interrupteur fermé : $U=0$ · ouvert : $I=0$ · en continu : condensateur $=$ circuit ouvert, bobine $=$ fil",
     "exemple": r"$R=2$ kΩ et $I=3$ mA : $U=6$ V",
     "cours": r"La loi d'Ohm lie la tension et le courant d'une résistance (effet Joule : $P=RI^2$). Un condensateur stocke des charges, une bobine stocke de l'énergie magnétique ; en régime continu établi, $du/dt=0$ et $di/dt=0$."},
    {"id": "kirchhoff", "titre": "Lois de Kirchhoff",
     "formule": r"nœuds : $\sum I_{\text{entrants}}=\sum I_{\text{sortants}}$ · mailles : $\sum U=0$ le long d'une maille orientée · mailles indépendantes $=b-n+1$",
     "exemple": r"$I_3=I_2+I_4$ au nœud $B$ ; $U_4+U_3-E=0$ dans la maille",
     "cours": r"Un nœud relie au moins trois branches ; une branche est la portion de circuit entre deux nœuds consécutifs ; une maille est un chemin fermé. La loi des nœuds exprime la conservation de la charge, la loi des mailles l'unicité du potentiel."},
    {"id": "association", "titre": "Associations de résistances",
     "formule": r"série : $R_{eq}=R_1+R_2$ (même courant) · parallèle : $\dfrac1{R_{eq}}=\dfrac1{R_1}+\dfrac1{R_2}$, deux résistances : $\dfrac{R_1R_2}{R_1+R_2}$ (même tension)",
     "exemple": r"$2$ kΩ en parallèle avec $2$ kΩ : $1$ kΩ",
     "cours": r"Deux dipôles sont en série s'ils sont parcourus par le même courant (ils ne sont pas simplement dans la même maille) ; ils sont en parallèle s'ils ont la même tension (même paire de nœuds). On remplace les associations pas à pas, en refaisant le schéma."},
    {"id": "diviseurs", "titre": "Ponts diviseurs",
     "formule": r"tension : $U_2=\dfrac{R_2}{R_1+R_2}E$ (résistances en série) · courant : $I_1=\dfrac{R_2}{R_1+R_2}I$ (résistances en parallèle)",
     "exemple": r"$E=15$ V, $R_1=1$ kΩ, $R_2=2$ kΩ : $U_2=10$ V",
     "cours": r"Le diviseur de tension s'applique à des résistances en série traversées par le même courant (sans courant de sortie), le diviseur de courant à des résistances en parallèle. Dans le diviseur de courant, le courant le plus grand passe dans la plus petite résistance."},
    {"id": "equivalences", "titre": "Générateurs réels, Thévenin et Norton",
     "formule": r"Thévenin : $E_{th}$ en série avec $R_{th}$ · Norton : $I_N$ en parallèle avec $R_N$ · $R_N=R_{th}$ · $E_{th}=R_{th}I_N$ · réel : $U=E-R\,I$ · $E_{th}$ : tension à vide · $I_N$ : courant de court-circuit",
     "exemple": r"$E=12$ V, $R=4$ Ω : $I_N=3$ A en parallèle avec $4$ Ω",
     "cours": r"Un réseau linéaire vu de deux bornes équivaut à un générateur de Thévenin (tension à vide, résistance obtenue en éteignant les sources : source de tension $\to$ fil, source de courant $\to$ circuit ouvert) ou de Norton. On enchaîne les équivalences pour simplifier un montage."},
    {"id": "millman", "titre": "Théorème de Millman",
     "formule": r"$V_A=\dfrac{\sum E_i/R_i+\sum \eta_i}{\sum 1/R_i}$ · branches $(E_i,R_i)$ ou résistances seules entre le nœud $A$ et la masse · $\eta_i$ : sources de courant entrant en $A$",
     "exemple": r"$E_1=12$ V, $R_1=2$ kΩ, $E_2=6$ V, $R_2=3$ kΩ, $R_3=6$ kΩ : $V_A=8$ V",
     "cours": r"Pour des branches en parallèle entre un nœud $A$ et une référence, la loi des nœuds donne le potentiel de $A$. Une branche sans source contribue seulement au dénominateur."},
    {"id": "sinus", "titre": "Grandeurs sinusoïdales",
     "formule": r"$u(t)=U_m\cos(\omega t+\varphi)$ · $\omega=2\pi f=\dfrac{2\pi}T$ · $U_{eff}=\dfrac{U_m}{\sqrt2}$ · valeur moyenne $=0$ · déphasage $\varphi=360°\dfrac{\Delta t}T$",
     "exemple": r"$f=50$ Hz : $T=20$ ms, $\omega=100\pi$ rad/s",
     "cours": r"Une grandeur sinusoïdale est définie par son amplitude, sa pulsation et sa phase à l'origine. La valeur efficace est celle d'une tension continue qui dissiperait la même puissance dans une résistance."},
    {"id": "complexes", "titre": "Impédances complexes",
     "formule": r"$Z_R=R$ · $Z_L=jL\omega$ · $Z_C=\dfrac1{jC\omega}$ · $|Z|=\sqrt{\text{Re}^2+\text{Im}^2}$ · $\omega_0=\dfrac1{\sqrt{LC}}$ · RC série : $\left|\dfrac{U_C}{U}\right|=\dfrac1{\sqrt{1+(RC\omega)^2}}$",
     "exemple": r"$L=10$ mH, $\omega=1000$ rad/s : $|Z_L|=10$ Ω",
     "cours": r"En régime sinusoïdal forcé, on remplace les grandeurs par leurs amplitudes complexes : les lois (Ohm, Kirchhoff, diviseurs, Thévenin, Millman) s'appliquent avec des impédances. Le module donne le rapport des amplitudes, l'argument le déphasage."},
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


X25 = "Examen B1 d'électronique, octobre 2025"
X24 = "Examen B1 d'électronique, octobre 2024"
TD1 = "TD 1 d'électronique (lois fondamentales)"
TD2 = "TD 2 d'électronique (Thévenin / Norton)"
TD3 = "TD 3 d'électronique (théorème de Millman)"
TD4 = "TD 4 d'électronique (régime sinusoïdal)"


# ---------------------------------------------------------------- circuit figures (redrawn from the exam subjects)

def _x24e2(d):
    d += (s := SrcU().endpoints((0, 0), (0, 5)))
    tension(d, s, "$2E$")
    d += (w := Fil().endpoints((0, 5), (2, 5)))
    courant(d, w, "$I$", debut=False)
    d += (r1 := R().endpoints((2, 5), (6, 5)).label("$R_1$", loc="bottom"))
    courant(d, r1, "$I_1$")
    d += Point().at((6, 5)).label("$A$", loc="top")
    d += (w := Fil().endpoints((9, 5), (6, 5)))
    courant(d, w, "$I'$", debut=False)
    d += (s := SrcU().endpoints((9, 0), (9, 5)))
    tension(d, s, "$E$", cote=False)
    d += (r3 := R().endpoints((6, 5), (6, 2.5)).label("$R_3$", loc="bottom"))
    courant(d, r3, "$I_3$", loc="bottom")
    d += Point().at((6, 2.5)).label("$B$", loc="right")
    d += (r2 := R().endpoints((6, 2.5), (2, 2.5)).label("$R_2$"))
    courant(d, r2, "$I_2$", debut=False)
    d += Fil().endpoints((2, 2.5), (2, 5))
    d += (r4 := R().endpoints((6, 2.5), (6, 0)).label("$R_4$", loc="bottom"))
    courant(d, r4, "$I_4$", debut=False, loc="bottom")
    d += Fil().endpoints((0, 0), (9, 0))


def _x24e31(d):
    d += (s := SrcI().endpoints((0, 0), (0, 5)))
    courant(d, s, "$I$", debut=False)
    d += Fil().endpoints((0, 5), (10, 5))
    d += (s := SrcU().endpoints((2.5, 5), (2.5, 2.5)))
    tension(d, s, "$2E$", cote=False)
    d += R().endpoints((2.5, 2.5), (2.5, 0)).label("$4R$", loc="bottom")
    d += Point().at((10, 5)).label("$A$", loc="right")
    d += (r := R().endpoints((10, 5), (10, 0)).label("$2R$", loc="bottom"))
    tension(d, r, "$U$", sens=-1)
    d += Point().at((10, 0)).label("$B$", loc="right")
    d += Fil().endpoints((0, 0), (4.5, 0))
    d += (s := SrcI().endpoints((4.5, 0), (7.5, 0)).label("$2I$", loc="bottom"))
    courant(d, s, "", debut=False)
    d += Fil().endpoints((7.5, 0), (10, 0))
    d += Fil().endpoints((4.5, 0), (4.5, 1.5))
    d += R().endpoints((4.5, 1.5), (7.5, 1.5)).label("$R$")
    d += Fil().endpoints((7.5, 1.5), (7.5, 0))


def _x24e31_th(d):
    d += (s := SrcU().endpoints((13, 0.5), (13, 4.5)))
    tension(d, s, "$E_{th}$")
    d += R().endpoints((13, 4.5), (17, 4.5)).label("$R_{th}$")
    d += Point().at((17, 4.5)).label("$A$", loc="right")
    d += (r := R().endpoints((17, 4.5), (17, 0.5)).label("$2R$", loc="bottom"))
    tension(d, r, "$U$", sens=-1)
    d += Point().at((17, 0.5)).label("$B$", loc="right")
    d += Fil().endpoints((17, 0.5), (13, 0.5))


def _x24e32(d):
    d += (s := SrcU().endpoints((0, 0), (0, 4)))
    tension(d, s, "$E$")
    d += R().endpoints((0, 4), (3, 4)).label("$4R$", loc="bottom")
    d += R().endpoints((3, 4), (3, 0)).label("$4R$", loc="bottom")
    d += R().endpoints((3, 4), (6, 4)).label("$R$", loc="bottom")
    d += Point().at((6, 4)).label("$A$", loc="top")
    d += (r := R().endpoints((6, 4), (6, 0)).label("$2R$", loc="top"))
    tension(d, r, "$U$", sens=-1)
    d += Point().at((6, 0)).label("$B$", loc="bottom")
    d += Fil().endpoints((6, 4), (9, 4))
    d += (s := SrcI().endpoints((9, 4), (9, 0)))
    courant(d, s, "$I$", debut=False)
    d += Fil().endpoints((0, 0), (3, 0))
    d += R().endpoints((3, 0), (6, 0)).label("$R$", loc="bottom")
    d += Fil().endpoints((6, 0), (9, 0))


def _x25e2(d):
    d += (s := SrcU().endpoints((0, 0), (0, 2)))
    tension(d, s, "$E$")
    d += Fil().endpoints((0, 2), (0, 4))
    d += (r1 := R().endpoints((0, 4), (5, 4)).label("$R_1$"))
    tension(d, r1, "$U$", sens=-1, cote=False, ofst=0.35)
    d += R().endpoints((0, 2.5), (5, 2.5)).label("$R_2$", loc="bottom")
    d += Fil().endpoints((5, 2.5), (5, 4))
    d += (w := Fil().endpoints((5, 4), (8, 4)))
    courant(d, w, "$I_4$", debut=False)
    d += R().endpoints((5, 2.5), (5, 0)).label("$R_3$", loc="bottom")
    d += R().endpoints((8, 4), (8, 0)).label("$R_4$", loc="bottom")
    d += Fil().endpoints((0, 0), (8, 0))


def _x25e3(d):
    d += (s := SrcU().endpoints((0, 0), (0, 6)))
    tension(d, s, "$E$")
    d += Fil().endpoints((0, 6), (8, 6))
    d += (r := R().endpoints((4, 3), (4, 6)).label("$6R$", loc="bottom"))
    tension(d, r, "$U_1$")
    d += (r := R().endpoints((4, 0), (4, 3)).label("$2R$", loc="bottom"))
    tension(d, r, "$U_3$")
    d += (r := R().endpoints((8, 3), (8, 6)).label("$6R$", loc="bottom"))
    tension(d, r, "$U_2$")
    d += Inter().endpoints((4, 3), (8, 3)).label("$K_2$", loc="bottom")
    d += Fil().endpoints((0, 0), (4, 0))
    d += Inter().endpoints((4, 0), (8, 0)).label("$K_1$", loc="bottom")
    d += Fil().endpoints((8, 0), (8, 3))


FIG_X24E2 = fig(_x24e2, "Schéma : source 2E à gauche, R1 en haut vers le nœud A, R3 de A vers B, R2 de B vers la gauche, R4 de B vers le bas, source E à droite ; courants I, I1, I2, I3, I4, I'")
FIG_X24E31 = (fig(_x24e31, "Schéma : source de courant I, branche 2E en série avec 4R, R en parallèle avec la source de courant 2I sur le fil du bas, 2R entre A et B (tension U)")
              + "\n\n" + fig(_x24e31_th, "Schéma équivalent demandé : source Eth en série avec Rth, chargée par 2R entre A et B (tension U)"))
FIG_X24E32 = fig(_x24e32, "Schéma : source E en série avec 4R, 4R vers le bas, R vers A, R sur le fil du bas vers B, 2R entre A et B (tension U), source de courant I de A vers B")
FIG_X25E2 = fig(_x25e2, "Schéma : source E, R1 et R2 en parallèle (tension U), puis R3 et R4 en parallèle vers la masse ; courant I4 dans R4")
FIG_X25E3 = fig(_x25e3, "Schéma : source E ; colonne du milieu 6R (U1) puis 2R (U3) ; colonne de droite 6R (U2) ; interrupteur K2 entre les milieux des colonnes, K1 entre les bas des colonnes")

LEVELS = [
    {"n": 1, "titre": "Courant, tension, puissance", "notions": ["grandeurs"], "exos": [
        v("r11", r"Un courant de $2$ A traverse un fil pendant $5$ s. Charge transportée (en C) ?", "2*5", "10", r"$Q=It=10$ C.", duree=1),
        v("r12", r"Un courant de $3$ mA circule pendant $2$ s. Charge en mC ?", "3*2", "6", r"$Q=It=6$ mC.", duree=1),
        v("r13", r"Une tension de $12$ V et un courant de $0{,}5$ A. Puissance reçue (en W) ?", "12*Rational(1,2)", "6", r"$P=UI=6$ W.", duree=1),
        v("r14", r"Puissance de $6$ W pendant $10$ s. Énergie (en J) ?", "6*10", "60", r"$W=Pt=60$ J.", duree=1),
        v("r15", r"$V_A=5$ V et $V_B=2$ V. Tension $U_{AB}$ (en V) ?", "5-2", "3", r"$U_{AB}=V_A-V_B=3$ V.", duree=1),
        v("r16", r"$V_A=1$ V et $V_B=4$ V. Tension $U_{BA}$ (en V) ?", "4-1", "3", r"$U_{BA}=V_B-V_A=3$ V.", duree=1),
        o("r17", r"Rappeler les conventions récepteur et générateur : sens relatif de $U$ et de $I$, signe de la puissance $UI$.",
          r"Convention récepteur : $U$ et $I$ en sens opposés ; $P=UI>0$ signifie que le dipôle reçoit de la puissance. Convention générateur : $U$ et $I$ dans le même sens ; $P=UI>0$ signifie qu'il en fournit. Le courant qui entre dans un dipôle ressort avec la même intensité.", src=X25 + ", ex. 1", duree=4),
    ]},
    {"n": 2, "titre": "Loi d'Ohm et dipôles", "notions": ["dipoles", "grandeurs"], "exos": [
        v("r21", r"Une résistance de $2$ kΩ est traversée par $3$ mA. Tension (en V) ?", "2*3", "6", r"$U=RI=2\,\text{kΩ}\times3\,\text{mA}=6$ V.", duree=1),
        v("r22", r"Une résistance de $5$ kΩ sous $10$ V. Courant (en mA) ?", "10/5", "2", r"$I=U/R=2$ mA.", duree=1),
        v("r23", r"Une résistance de $100$ Ω parcourue par $0{,}1$ A. Puissance dissipée (en W) ?", "100*Rational(1,10)**2", "1", r"$P=RI^2=100\times0{,}01=1$ W.", duree=2),
        v("r24", r"Condensateur de $1\,\mu$F : $du/dt=1000$ V/s. Courant (en mA) ?", "1*1000/1000", "1", r"$i=C\,du/dt=10^{-6}\times10^3=10^{-3}$ A $=1$ mA.", duree=2),
        v("r25", r"Bobine de $10$ mH : $di/dt=200$ A/s. Tension (en V) ?", "10*200/1000", "2", r"$u=L\,di/dt=0{,}01\times200=2$ V.", duree=2),
        v("r26", r"Tension aux bornes d'un interrupteur fermé (en V) ?", "0", "0", r"Un interrupteur fermé est un fil : $U=0$.", duree=1),
        o("r27", r"En régime continu établi, par quoi peut-on remplacer un condensateur ? une bobine ? Pourquoi ?",
          r"Condensateur : circuit ouvert, car $i=C\,du/dt=0$ quand $u$ est constante. Bobine : fil (court-circuit), car $u=L\,di/dt=0$ quand $i$ est constant.", duree=4),
    ]},
    {"n": 3, "titre": "Lois de Kirchhoff", "notions": ["kirchhoff", "dipoles"], "exos": [
        v("r31", r"Au nœud $B$ : $I_3=I_2+I_4$ avec $I_3=2$ mA et $I_4=7$ mA. $I_2$ (en mA) ?", "2-7", "-5", r"$I_2=I_3-I_4=-5$ mA : le courant circule en sens contraire de la flèche.", src=X24 + ", ex. 2", duree=2),
        v("r32", r"Même circuit : $R_2=2$ kΩ traversée par $I_2=-5$ mA. $U_2$ (en V) ?", "2*(-5)", "-10", r"$U_2=R_2I_2=-10$ V.", src=X24 + ", ex. 2", duree=2),
        v("r33", r"Même circuit : $U_3=4$ V et $I_3=2$ mA. $R_3$ (en kΩ) ?", "4/2", "2", r"$R_3=U_3/I_3=2$ kΩ.", src=X24 + ", ex. 2", duree=2),
        v("r34", r"Même circuit : $E=6$ V et la maille $E\to R_3\to R_4$ donne $U_4+U_3-E=0$ ; $U_3=4$ V. $U_4$ (en V) ?", "6-4", "2", r"$U_4=E-U_3=2$ V.", src=X24 + ", ex. 2", duree=2),
        v("r35", r"Trois courants arrivent à un nœud : $5$ mA, $3$ mA et $I$ ; un seul sort : $12$ mA. $I$ (en mA) ?", "12-5-3", "4", r"$5+3+I=12$ donc $I=4$ mA.", duree=2),
        v("r36", r"Circuit à $4$ nœuds et $6$ branches. Nombre de mailles indépendantes ?", "6-4+1", "3", r"$b-n+1=6-4+1=3$.", src=X24 + ", ex. 2", duree=2),
        o("r37", r"Dans le montage $E$, $R_1$, $R_2$ en série, deux dipôles appartiennent à la même maille : sont-ils forcément en série ? Justifier.",
          r"Non. Deux dipôles sont en série s'ils sont traversés par le même courant, c'est-à-dire sans nœud entre eux. Appartenir à la même maille ne suffit pas : si un nœud sépare les deux, les courants peuvent différer.", src=X25 + ", ex. 1", duree=4),
    ]},
    {"n": 4, "titre": "Associations de résistances", "notions": ["association", "kirchhoff"], "exos": [
        v("r41", r"$R_1=2$ kΩ en série avec $R_2=3$ kΩ. $R_{eq}$ (en kΩ) ?", "2+3", "5", r"$R_{eq}=R_1+R_2=5$ kΩ.", duree=1),
        v("r42", r"$2$ kΩ en parallèle avec $2$ kΩ. $R_{eq}$ (en kΩ) ?", "2*2/(2+2)", "1", r"$\dfrac{R_1R_2}{R_1+R_2}=1$ kΩ.", duree=1),
        v("r43", r"$6$ kΩ en parallèle avec $3$ kΩ. $R_{eq}$ (en kΩ) ?", "6*3/(6+3)", "2", r"$\dfrac{18}{9}=2$ kΩ.", duree=1),
        v("r44", r"Trois résistances de $6$ Ω, $3$ Ω et $2$ Ω en parallèle. $R_{eq}$ (en Ω) ?", "1/(Rational(1,6)+Rational(1,3)+Rational(1,2))", "1", r"$1/R_{eq}=\tfrac16+\tfrac13+\tfrac12=1$ donc $R_{eq}=1$ Ω.", duree=2),
        v("r45", r"$R_1=R_2=2$ kΩ en parallèle, puis en série avec $R_3=R_4=1$ kΩ en parallèle. $R_{eq}$ (en kΩ) ?", "2*2/(2+2)+1*1/(1+1)", "Rational(3,2)", r"$R_{12}=1$ kΩ, $R_{34}=0{,}5$ kΩ, $R_{eq}=R_{12}+R_{34}=1{,}5$ kΩ.", src=X25 + ", ex. 2", duree=3),
        v("r46", r"Quatre résistances de $10$ Ω en série, l'ensemble en parallèle avec $40$ Ω. $R_{eq}$ (en Ω) ?", "40*40/(40+40)", "20", r"Série : $40$ Ω ; parallèle avec $40$ Ω : $20$ Ω.", duree=2),
        o("r47", r"Citer les deux critères pour reconnaître des résistances en série et en parallèle, puis en déduire la méthode de réduction d'un circuit.",
          r"Série : même courant (aucun nœud entre elles). Parallèle : même tension (mêmes deux nœuds). Méthode : repérer une association évidente, la remplacer par la résistance équivalente, refaire le schéma, recommencer jusqu'à une seule résistance $R_{eq}$.", src=X25 + ", ex. 2", duree=5),
    ]},
    {"n": 5, "titre": "Ponts diviseurs", "notions": ["diviseurs", "association"], "exos": [
        v("r51", r"$E=15$ V, $R_1=1$ kΩ en série avec $R_2=2$ kΩ. Tension aux bornes de $R_2$ (en V) ?", "15*2/(1+2)", "10", r"$U_2=\dfrac{R_2}{R_1+R_2}E=10$ V.", duree=2),
        v("r52", r"Un courant $I=9$ mA se partage entre $R_1=1$ kΩ et $R_2=2$ kΩ en parallèle. Courant dans $R_1$ (en mA) ?", "9*2/(1+2)", "6", r"$I_1=\dfrac{R_2}{R_1+R_2}I=6$ mA.", duree=2),
        v("r53", r"Même montage : courant dans $R_2$ (en mA) ?", "9*1/(1+2)", "3", r"$I_2=\dfrac{R_1}{R_1+R_2}I=3$ mA.", duree=2),
        v("r54", r"$E=15$ V ; $R_1=R_2=2$ kΩ en parallèle, en série avec $R_3=R_4=1$ kΩ en parallèle. Tension $U$ aux bornes de $R_1\parallel R_2$ (en V) ?", "15*1/(1+Rational(1,2))", "10", r"$U=\dfrac{R_{12}}{R_{12}+R_{34}}E=\dfrac{1}{1{,}5}\times15=10$ V.", src=X25 + ", ex. 2", duree=3),
        v("r55", r"Même montage : courant $I_4$ dans $R_4$ (en mA) ?", "(15-10)/1", "5", r"Tension aux bornes de $R_3\parallel R_4$ : $E-U=5$ V ; $I_4=5\text{ V}/1\text{ kΩ}=5$ mA.", src=X25 + ", ex. 2", duree=3),
        v("r56", r"Diviseur $E=12$ V, $R_1=R_2=1$ kΩ (sortie sur $R_2$, à vide : $6$ V). On branche une charge de $1$ kΩ en parallèle sur $R_2$. Nouvelle tension de sortie (en V) ?", "12*Rational(1,2)/(1+Rational(1,2))", "4", r"$R_2\parallel R_c=0{,}5$ kΩ : $U=\dfrac{0{,}5}{1+0{,}5}\times12=4$ V au lieu de $6$ V.", duree=3),
        o("r57", r"Établir la formule du diviseur de tension pour deux résistances en série sous $E$.",
          r"Même courant $I=\dfrac{E}{R_1+R_2}$ dans les deux résistances (association série). Loi d'Ohm : $U_2=R_2I=\dfrac{R_2}{R_1+R_2}E$.", duree=4),
    ]},
    {"n": 6, "titre": "Générateurs réels et équivalences", "notions": ["equivalences", "dipoles"], "exos": [
        v("r61", r"Générateur réel : $E=12$ V, $r=2$ Ω, courant débité $3$ A. Tension de sortie (en V) ?", "12-2*3", "6", r"$U=E-rI=6$ V.", duree=1),
        v("r62", r"Thévenin $E=12$ V, $R=4$ Ω. Courant de Norton $I_N$ (en A) ?", "12/4", "3", r"$I_N=E/R=3$ A (avec $R_N=4$ Ω en parallèle).", duree=1),
        v("r63", r"Norton $I_N=2$ A, $R=5$ Ω. Tension de Thévenin (en V) ?", "2*5", "10", r"$E_{th}=R\,I_N=10$ V.", duree=1),
        v("r64", r"Thévenin $E=10$ V, $R=5$ Ω, chargé par $R_c=5$ Ω. Tension aux bornes de la charge (en V) ?", "10*5/(5+5)", "5", r"Diviseur de tension : $U=\dfrac{R_c}{R+R_c}E=5$ V.", duree=2),
        v("r65", r"Générateur de tension $E=6$ V avec $R_1=3$ Ω en série ; $R_2=6$ Ω en parallèle sur la sortie. Tension de Thévenin vue de la sortie (en V) ?", "6*6/(3+6)", "4", r"Tension à vide : diviseur $\dfrac{R_2}{R_1+R_2}E=4$ V.", duree=2),
        v("r66", r"Même montage : résistance de Thévenin (source éteinte) (en Ω) ?", "3*6/(3+6)", "2", r"$R_{th}=R_1\parallel R_2=2$ Ω.", duree=2),
        o("r67", r"Indiquer comment « éteindre » une source de tension idéale et une source de courant idéale pour calculer $R_{th}$.",
          r"Source de tension idéale éteinte : remplacée par un fil (court-circuit, $E=0$). Source de courant idéale éteinte : remplacée par un circuit ouvert ($\eta=0$).", src=TD2, duree=3),
    ]},
    {"n": 7, "titre": "Thévenin et Norton : calculs", "notions": ["equivalences", "diviseurs"], "exos": [
        v("r71", r"Source $E=12$ V, $R_1=6$ Ω en série, $R_2=3$ Ω entre les bornes $A$ et $B$. Tension de Thévenin $E_{th}$ de $AB$ (en V) ?", "12*3/(6+3)", "4", r"$E_{th}=\dfrac{R_2}{R_1+R_2}E=4$ V.", src=TD2, duree=3),
        v("r72", r"Même montage : $R_{th}$ de $AB$ (en Ω) ?", "6*3/(6+3)", "2", r"$R_{th}=R_1\parallel R_2=2$ Ω.", src=TD2, duree=2),
        v("r73", r"Même montage : courant de Norton $I_N$ (en A) ?", "4/2", "2", r"$I_N=E_{th}/R_{th}=2$ A (on retrouve $E/R_1=2$ A).", src=TD2, duree=2),
        v("r74", r"Même montage chargé par $R_L=2$ Ω entre $A$ et $B$. Courant dans $R_L$ (en A) ?", "4/(2+2)", "1", r"$I=\dfrac{E_{th}}{R_{th}+R_L}=1$ A.", src=TD2, duree=2),
        v("r75", r"Source de courant $I=3$ A en parallèle avec $R_1=4$ Ω. Tension $E$ de son équivalent de Thévenin (en V) ?", "3*4", "12", r"$E=R_1I=12$ V en série avec $R_1=4$ Ω.", duree=2),
        v("r76", r"On place $R_2=4$ Ω en série avec cet équivalent de Thévenin. Résistance de Thévenin totale (en Ω) ?", "4+4", "8", r"$R_1+R_2=8$ Ω.", duree=1),
        o("r77", r"Expliquer la méthode générale d'enchaînement des équivalences Thévenin/Norton sur un circuit à plusieurs branches (exemple du sujet d'octobre 2024).",
          r"1. Transformer chaque générateur de Thévenin en Norton (ou l'inverse) pour obtenir des branches de même type. 2. Regrouper les résistances en parallèle et additionner les sources de courant en parallèle (en tenant compte du sens). 3. Revenir en Thévenin : $E_{th}=R_{eq}\,I_{eq}$. 4. Terminer avec un diviseur de tension. Dans le sujet : $E_{th}=2RI-2E$, $R_{th}=5R$, puis $U=\dfrac47(RI-E)$.", src=X24 + ", ex. 3", duree=12),
    ]},
    {"n": 8, "titre": "Théorème de Millman", "notions": ["millman", "equivalences"], "exos": [
        v("r81", r"Entre $A$ et la masse : $(E_1=12$ V, $R_1=2$ kΩ$)$, $(E_2=6$ V, $R_2=3$ kΩ$)$ et $R_3=6$ kΩ. $V_A$ (en V) ?", "(12/2+6/3)/(Rational(1,2)+Rational(1,3)+Rational(1,6))", "8", r"Numérateur : $6+2=8$ mA ; dénominateur : $\tfrac12+\tfrac13+\tfrac16=1$ mS ; $V_A=8$ V.", src=TD3, duree=4),
        v("r82", r"Entre $A$ et la masse : $(E=10$ V, $R=5$ kΩ$)$, $R_3=5$ kΩ et une source de courant de $2$ mA entrant en $A$. $V_A$ (en V) ?", "(10/5+2)/(Rational(1,5)+Rational(1,5))", "10", r"Numérateur : $2+2=4$ mA ; dénominateur : $0{,}4$ mS ; $V_A=10$ V.", src=TD3, duree=4),
        v("r83", r"Deux branches $(E,R)$ identiques entre $A$ et la masse. $V_A$ avec $E=9$ V (en V) ?", "(9/1+9/1)/(1+1)", "9", r"Deux sources identiques en parallèle : $V_A=E=9$ V.", duree=2),
        v("r84", r"Entre $A$ et la masse : $(E=10$ V, $R=1$ kΩ$)$ et $(E'=-10$ V, $R'=1$ kΩ$)$. $V_A$ (en V) ?", "(10-10)/(1+1)", "0", r"Les courants se compensent : $V_A=0$.", duree=2),
        v("r85", r"Entre $A$ et la masse : $(E=12$ V, $R=4$ kΩ$)$ seule. $V_A$ (en V) ?", "(12/4)/(Rational(1,4))", "12", r"Aucun courant ne circule (rien d'autre) : $V_A=E$.", duree=2),
        o("r86", r"Démontrer la formule de Millman pour deux branches $(E_1,R_1)$ et $(E_2,R_2)$ entre $A$ et la masse.",
          r"Loi des nœuds en $A$ : $\dfrac{E_1-V_A}{R_1}+\dfrac{E_2-V_A}{R_2}=0$. On regroupe : $V_A\left(\dfrac1{R_1}+\dfrac1{R_2}\right)=\dfrac{E_1}{R_1}+\dfrac{E_2}{R_2}$, d'où $V_A=\dfrac{E_1/R_1+E_2/R_2}{1/R_1+1/R_2}$.", src=TD3, duree=6),
    ]},
    {"n": 9, "titre": "Grandeurs sinusoïdales", "notions": ["sinus"], "exos": [
        v("r91", r"Fréquence $50$ Hz. Période (en ms) ?", "1000/50", "20", r"$T=1/f=20$ ms.", src=TD4, duree=1),
        v("r92", r"Période $2$ ms. Fréquence (en Hz) ?", "1000/2", "500", r"$f=1/T=500$ Hz.", src=TD4, duree=1),
        v("r93", r"Fréquence $50$ Hz. Pulsation en unités de $\pi$ rad/s ?", "2*50", "100", r"$\omega=2\pi f=100\pi$ rad/s.", src=TD4, duree=1),
        v("r94", r"Amplitude $U_m=10\sqrt2$ V. Valeur efficace (en V) ?", "10*sqrt(2)/sqrt(2)", "10", r"$U_{eff}=U_m/\sqrt2=10$ V.", src=TD4, duree=1),
        v("r95", r"Valeur efficace $230$ V. Amplitude $U_m$ (en V) ?", "230*sqrt(2)", "230*sqrt(2)", r"$U_m=U_{eff}\sqrt2=230\sqrt2\approx325$ V.", duree=2),
        v("r96", r"Période $20$ ms, retard $2$ ms entre $u$ et $i$. Déphasage (en degrés) ?", "360*2/20", "36", r"$\varphi=360°\times\Delta t/T=36°$.", src=TD4, duree=2),
        v("r97", r"Valeur moyenne d'une tension sinusoïdale de période $T$ sur une période (en V) ?", "0", "0", r"Les alternances positive et négative se compensent.", duree=1),
    ]},
    {"n": 10, "titre": "Impédances complexes", "notions": ["complexes", "sinus"], "exos": [
        v("ra1", r"Bobine $L=10$ mH, $\omega=1000$ rad/s. $|Z_L|$ (en Ω) ?", "Rational(10,1000)*1000", "10", r"$|Z_L|=L\omega=10$ Ω.", src=TD4, duree=2),
        v("ra2", r"Condensateur $C=100\,\mu$F, $\omega=1000$ rad/s. $|Z_C|$ (en Ω) ?", "1/(Rational(100,10**6)*1000)", "10", r"$|Z_C|=\dfrac1{C\omega}=10$ Ω.", src=TD4, duree=2),
        v("ra3", r"$R=10$ Ω en série avec la bobine ci-dessus ($Z_L=10j$). $|Z|$ (en Ω) ?", "sqrt(10**2+10**2)", "10*sqrt(2)", r"$|Z|=\sqrt{10^2+10^2}=10\sqrt2$ Ω.", src=TD4, duree=2),
        v("ra4", r"Même circuit RL : déphasage de la tension sur le courant (en degrés) ?", "45", "45", r"$\arg Z=\arctan(L\omega/R)=\arctan1=45°$.", src=TD4, duree=2),
        v("ra5", r"RLC série idéal : $L=10$ mH, $C=100\,\mu$F. Pulsation de résonance $\omega_0$ (en rad/s) ?", "1/sqrt(Rational(10,1000)*Rational(100,10**6))", "1000", r"$\omega_0=\dfrac1{\sqrt{LC}}=\dfrac1{\sqrt{10^{-6}}}=1000$ rad/s.", src=TD4, duree=3),
        v("ra6", r"Filtre RC (sortie sur $C$) avec $RC\omega=1$. Rapport $|U_C/U|$ au carré ?", "1/(1+1)", "Rational(1,2)", r"$|U_C/U|=\dfrac1{\sqrt{1+(RC\omega)^2}}=\dfrac1{\sqrt2}$, donc le carré vaut $\tfrac12$.", src=TD4, duree=3),
        o("ra7", r"Donner l'impédance complexe d'une résistance, d'une bobine et d'un condensateur, et le comportement limite à $\omega\to0$ et $\omega\to\infty$.",
          r"$Z_R=R$, $Z_L=jL\omega$, $Z_C=\dfrac1{jC\omega}$. À $\omega\to0$ (continu) : bobine $\to$ fil ($Z_L\to0$), condensateur $\to$ circuit ouvert ($Z_C\to\infty$). À $\omega\to\infty$ : bobine $\to$ circuit ouvert, condensateur $\to$ fil.", src=TD4, duree=5),
    ]},
    {"n": 11, "titre": "Niveau examen : sujet B1 octobre 2025", "notions": ["grandeurs", "association", "diviseurs", "kirchhoff"], "examen": True, "exos": [
        o("rx1", r"Exercice 1 : questions de cours (courant, tension, générateur, dipôles en série, mailles, associations dans un circuit à 6 résistances).",
          r"Courant : déplacement ordonné de charges. Tension : différence de potentiels. Le courant sortant d'un générateur est égal au courant entrant (vrai). Deux dipôles parcourus par le même courant sont en série. Appartenir à la même maille ne permet rien de conclure sur série ou parallèle.", src=X25 + ", ex. 1 (3 points)", duree=10),
        v("rx2", r"Exercice 2 : $R_1\parallel R_2$ en série avec $R_3\parallel R_4$ sous $E$. $R_1=R_2=2$ kΩ, $R_3=R_4=1$ kΩ, $E=15$ V. Tension aux bornes de $R_1\parallel R_2$ (en V) ?", "15*1/(1+Rational(1,2))", "10", r"$R_{12}=1$ kΩ, $R_{34}=0{,}5$ kΩ : $U=\dfrac{R_{12}}{R_{12}+R_{34}}E=10$ V.", src=X25 + ", ex. 2 (9 points)", duree=10),
        v("rx3", r"Même exercice : courant $I_4$ dans $R_4$ (en mA) ?", "(15-10)/1", "5", r"$U'=E-U=5$ V aux bornes de $R_3\parallel R_4$ ; $I_4=U'/R_4=5$ mA.", src=X25 + ", ex. 2", duree=5),
        o("rx4", r"Exercice 2 : nombre de nœuds, de branches et de mailles du circuit $E$, $R_1\parallel R_2$, $R_3\parallel R_4$ ; expression littérale de $U$ et $I_4$.",
          r"$3$ nœuds, $5$ branches, $6$ mailles (au total). $U=\dfrac{R_1R_2(R_3+R_4)}{R_1R_2(R_3+R_4)+R_3R_4(R_1+R_2)}E$ et $I_4=\dfrac{R_3(R_1+R_2)}{R_1R_2(R_3+R_4)+R_3R_4(R_1+R_2)}E$.", src=X25 + ", ex. 2", duree=15),
        o("rx5", r"Exercice 3 : circuit avec deux interrupteurs $K_1$ et $K_2$ ; trouver $U_1,U_2,U_3$ pour chaque position (ouvert/fermé) en fonction de $E$.",
          r"Méthode : redessiner le circuit pour chacune des quatre positions, identifier les résistances en série (même courant) et utiliser un diviseur de tension. Résultats : $K_1,K_2$ ouverts : $U_1=\tfrac34E$, $U_2=0$, $U_3=\tfrac14E$ ; $K_1$ ouvert, $K_2$ fermé : $\tfrac35E,\tfrac35E,\tfrac25E$ ; $K_1$ fermé, $K_2$ ouvert : $\tfrac34E,E,\tfrac14E$ ; tous fermés : $E,E,0$.", src=X25 + ", ex. 3 (9 points)", duree=20),
    ]},
    {"n": 12, "titre": "Niveau examen : sujet B1 octobre 2024", "notions": ["kirchhoff", "equivalences", "diviseurs"], "examen": True, "exos": [
        v("ry1", r"Exercice 2 : $I_3=2$ mA, $U_3=4$ V. $R_3$ (en kΩ) ?", "4/2", "2", r"$R_3=U_3/I_3=2$ kΩ.", src=X24 + ", ex. 2 (6,5 points)", duree=3),
        v("ry2", r"Même exercice : $I_2=I_3-I_4$ avec $I_4=7$ mA. $I_2$ (en mA) ?", "2-7", "-5", r"Loi des nœuds en $B$ : $I_2=-5$ mA.", src=X24 + ", ex. 2", duree=3),
        v("ry3", r"Même exercice : $U_2$ avec $R_2=2$ kΩ (en V) ?", "2*(-5)", "-10", r"$U_2=R_2I_2=-10$ V.", src=X24 + ", ex. 2", duree=3),
        v("ry4", r"Même exercice : $E=6$ V, $U_4=E-U_3$ (en V) ?", "6-4", "2", r"Loi des mailles : $U_4+U_3-E=0$ donc $U_4=2$ V.", src=X24 + ", ex. 2", duree=3),
        o("ry5", r"Exercice 3.1 (schéma du sujet : source $2E$ avec $4R$, $2R$ et $R$, source de courant $I$ ; $U$ aux bornes de $2R$) : donner l'équivalent de Thévenin $(E_{th},R_{th})$ puis $U$.",
          r"Norton/Thévenin enchaînés : $E_{th}=2RI-2E$ et $R_{th}=5R$. Diviseur de tension : $U=\dfrac{2R}{2R+5R}E_{th}=\dfrac27(2RI-2E)=\dfrac47(RI-E)$.", src=X24 + ", ex. 3 (11 points)", duree=15),
        o("ry6", r"Exercice 3.2 (schéma du sujet : $E$ avec $4R$, $2R$, $4R$, $R$ et source de courant $I$) : donner $U$ en fonction de $E$, $I$ et $R$.",
          r"On transforme $E,4R$ en source de courant $E/(4R)$ en parallèle avec $4R$, on associe les résistances en parallèle, on revient en Thévenin puis un diviseur donne $U=\dfrac{E-8RI}{6}$.", src=X24 + ", ex. 3", duree=15),
    ]},
]


# statements that refer to an exam figure show it first
FIGS = {**dict.fromkeys(["r31", "r32", "r33", "r34", "ry1", "ry2", "ry3", "ry4"], FIG_X24E2),
        "ry5": FIG_X24E31, "ry6": FIG_X24E32, "rx5": FIG_X25E3,
        **dict.fromkeys(["r45", "r54", "r55", "rx2", "rx3", "rx4"], FIG_X25E2)}

def _v(enonce, calc, ans, sol):
    return {"enonce": enonce, "calc": calc, "ans": ans, "sol": sol}


VARIANTS = {
    "r11": [_v(r"Un courant de $4$ A traverse un fil pendant $3$ s. Charge (en C) ?", "4*3", "12", r"$Q=It=12$ C.")],
    "r13": [_v(r"Une tension de $5$ V et un courant de $2$ A. Puissance reçue (en W) ?", "5*2", "10", r"$P=UI=10$ W.")],
    "r21": [_v(r"Une résistance de $3$ kΩ est traversée par $4$ mA. Tension (en V) ?", "3*4", "12", r"$U=RI=12$ V.")],
    "r22": [_v(r"Une résistance de $4$ kΩ sous $20$ V. Courant (en mA) ?", "20/4", "5", r"$I=U/R=5$ mA.")],
    "r23": [_v(r"Une résistance de $50$ Ω parcourue par $0{,}2$ A. Puissance (en W) ?", "50*Rational(1,5)**2", "2", r"$P=RI^2=2$ W.")],
    "r41": [_v(r"$R_1=4$ kΩ en série avec $R_2=6$ kΩ. $R_{eq}$ (en kΩ) ?", "4+6", "10", r"$10$ kΩ.")],
    "r42": [_v(r"$6$ kΩ en parallèle avec $6$ kΩ. $R_{eq}$ (en kΩ) ?", "6*6/(6+6)", "3", r"$3$ kΩ.")],
    "r43": [_v(r"$12$ kΩ en parallèle avec $4$ kΩ. $R_{eq}$ (en kΩ) ?", "12*4/(12+4)", "3", r"$48/16=3$ kΩ.")],
    "r51": [_v(r"$E=12$ V, $R_1=1$ kΩ en série avec $R_2=3$ kΩ. Tension aux bornes de $R_2$ (en V) ?", "12*3/(1+3)", "9", r"$U_2=\tfrac34\times12=9$ V.")],
    "r52": [_v(r"Un courant $I=12$ mA se partage entre $R_1=1$ kΩ et $R_2=3$ kΩ en parallèle. Courant dans $R_1$ (en mA) ?", "12*3/(1+3)", "9", r"$I_1=\tfrac{3}{4}\times12=9$ mA.")],
    "r61": [_v(r"Générateur réel : $E=10$ V, $r=1$ Ω, courant $4$ A. Tension de sortie (en V) ?", "10-1*4", "6", r"$U=E-rI=6$ V.")],
    "r62": [_v(r"Thévenin $E=20$ V, $R=5$ Ω. Courant de Norton (en A) ?", "20/5", "4", r"$I_N=4$ A.")],
    "r71": [_v(r"Source $E=18$ V, $R_1=3$ Ω en série, $R_2=6$ Ω entre $A$ et $B$. $E_{th}$ (en V) ?", "18*6/(3+6)", "12", r"$\tfrac{6}{9}\times18=12$ V.")],
    "r81": [_v(r"Entre $A$ et la masse : $(E_1=10$ V, $R_1=1$ kΩ$)$, $(E_2=5$ V, $R_2=1$ kΩ$)$, $R_3=\infty$ (absente). $V_A$ (en V) ?", "(10+5)/(1+1)", "Rational(15,2)", r"$V_A=\dfrac{10+5}{1+1}=7{,}5$ V.")],
    "r91": [_v(r"Fréquence $100$ Hz. Période (en ms) ?", "1000/100", "10", r"$T=10$ ms.")],
    "r96": [_v(r"Période $10$ ms, retard $1$ ms. Déphasage (en degrés) ?", "360*1/10", "36", r"$36°$.")],
}
for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["id"] in VARIANTS:
            _e["variants"] = VARIANTS[_e["id"]]


EXTRA_PARTS = []

QUIZ = [
    {"notion": "grandeurs", "type": "qcm", "q": r"Un déplacement ordonné de charges électriques est :", "choix": [r"un courant", r"une tension", r"une résistance", r"une puissance"], "bonne": 0},
    {"notion": "grandeurs", "type": "vf", "q": r"Le courant qui sort d'un générateur est égal à celui qui y entre.", "bonne": True},
    {"notion": "dipoles", "type": "qcm", "q": r"En régime continu établi, un condensateur se comporte comme :", "choix": [r"un circuit ouvert", r"un fil", r"une résistance nulle", r"une source"], "bonne": 0},
    {"notion": "dipoles", "type": "vf", "q": r"Un interrupteur fermé impose une tension nulle à ses bornes.", "bonne": True},
    {"notion": "kirchhoff", "type": "qcm", "q": r"Une branche est :", "choix": [r"une portion de circuit entre deux nœuds consécutifs", r"un fil reliant deux dipôles", r"un chemin fermé", r"une résistance"], "bonne": 0},
    {"notion": "kirchhoff", "type": "vf", "q": r"Deux dipôles de la même maille sont toujours en série.", "bonne": False},
    {"notion": "association", "type": "qcm", "q": r"Deux résistances de $2$ kΩ en parallèle valent :", "choix": [r"$1$ kΩ", r"$4$ kΩ", r"$2$ kΩ", r"$0{,}5$ kΩ"], "bonne": 0},
    {"notion": "association", "type": "vf", "q": r"Dipôles en série : même courant.", "bonne": True},
    {"notion": "diviseurs", "type": "qcm", "q": r"$U_2=\dfrac{R_2}{R_1+R_2}E$ est la formule :", "choix": [r"du diviseur de tension", r"du diviseur de courant", r"de Millman", r"de Norton"], "bonne": 0},
    {"notion": "diviseurs", "type": "vf", "q": r"Dans un diviseur de courant, la plus petite résistance reçoit le plus grand courant.", "bonne": True},
    {"notion": "equivalences", "type": "qcm", "q": r"Pour éteindre une source de courant idéale, on la remplace par :", "choix": [r"un circuit ouvert", r"un fil", r"une résistance de $1$ Ω", r"une source de tension"], "bonne": 0},
    {"notion": "equivalences", "type": "vf", "q": r"$R_N=R_{th}$ pour un même réseau.", "bonne": True},
    {"notion": "millman", "type": "qcm", "q": r"Le théorème de Millman donne :", "choix": [r"le potentiel d'un nœud commun à des branches en parallèle", r"la résistance équivalente", r"la fréquence de coupure", r"la puissance dissipée"], "bonne": 0},
    {"notion": "millman", "type": "vf", "q": r"Une branche sans source contribue seulement au dénominateur de Millman.", "bonne": True},
    {"notion": "sinus", "type": "qcm", "q": r"La valeur efficace d'une sinusoïde d'amplitude $U_m$ est :", "choix": [r"$U_m/\sqrt2$", r"$U_m\sqrt2$", r"$U_m/2$", r"$2U_m$"], "bonne": 0},
    {"notion": "sinus", "type": "vf", "q": r"La valeur moyenne d'une sinusoïde pure est nulle.", "bonne": True},
    {"notion": "complexes", "type": "qcm", "q": r"L'impédance d'une bobine est :", "choix": [r"$jL\omega$", r"$1/(jL\omega)$", r"$L/\omega$", r"$R$"], "bonne": 0},
    {"notion": "complexes", "type": "vf", "q": r"L'impédance d'un condensateur tend vers l'infini en continu.", "bonne": True},
]

_G = r"$Q=It$ · $P=UI$ · $W=Pt$ · $U_{AB}=V_A-V_B$"
_D = r"$U=RI$ · $P=RI^2$ · $i=C\,du/dt$ · $u=L\,di/dt$"
_K = r"nœuds : $\sum I_e=\sum I_s$ · mailles : $\sum U=0$ · indépendantes $=b-n+1$"
_A = r"série : $\sum R$ · parallèle : $\dfrac{R_1R_2}{R_1+R_2}$"
_V = r"$U_2=\dfrac{R_2}{R_1+R_2}E$ · $I_1=\dfrac{R_2}{R_1+R_2}I$"
_T = r"$E_{th}=R_{th}I_N$ · $R_N=R_{th}$ · éteindre : tension $\to$ fil, courant $\to$ ouvert"
_M = r"$V_A=\dfrac{\sum E_i/R_i+\sum\eta_i}{\sum1/R_i}$"
_S = r"$T=1/f$ · $\omega=2\pi f$ · $U_{eff}=U_m/\sqrt2$ · $\varphi=360°\,\Delta t/T$"
_Z = r"$Z_L=jL\omega$ · $Z_C=1/(jC\omega)$ · $\omega_0=1/\sqrt{LC}$ · $|Z|=\sqrt{\text{Re}^2+\text{Im}^2}$"

FORMULES = {
    "r11": _G, "r12": _G, "r13": _G, "r14": _G, "r15": _G, "r16": _G, "r17": _G,
    "r21": _D, "r22": _D, "r23": _D, "r24": _D, "r25": _D, "r26": _D, "r27": _D,
    "r31": _K, "r32": _K + " · " + _D, "r33": _D, "r34": _K, "r35": _K, "r36": _K, "r37": _K + " · série : même courant",
    "r41": _A, "r42": _A, "r43": _A, "r44": r"$\dfrac1{R_{eq}}=\sum\dfrac1{R_i}$", "r45": _A, "r46": _A, "r47": _A,
    "r51": _V, "r52": _V, "r53": _V, "r54": _V + " · " + _A, "r55": _V + " · " + _D, "r56": _V + " · " + _A, "r57": _V + " · " + _D,
    "r61": r"réel : $U=E-rI$", "r62": _T, "r63": _T, "r64": _T + " · " + _V, "r65": _T + " · " + _V, "r66": _T + " · " + _A, "r67": _T,
    "r71": _T + " · " + _V, "r72": _T + " · " + _A, "r73": _T, "r74": _T + " · " + _D, "r75": _T, "r76": _A, "r77": _T + " · " + _V,
    "r81": _M, "r82": _M, "r83": _M, "r84": _M, "r85": _M, "r86": _M + " · " + _K,
    "r91": _S, "r92": _S, "r93": _S, "r94": _S, "r95": _S, "r96": _S, "r97": r"valeur moyenne d'une sinusoïde $=0$",
    "ra1": _Z, "ra2": _Z, "ra3": _Z, "ra4": _Z + r" · $\arg Z=\arctan(\text{Im}/\text{Re})$", "ra5": _Z, "ra6": _Z, "ra7": _Z,
    "rx1": _G + " · " + _K, "rx2": _V + " · " + _A, "rx3": _V + " · " + _D, "rx4": _V + " · " + _A, "rx5": _V + " · " + _A,
    "ry1": _D, "ry2": _K, "ry3": _D, "ry4": _K, "ry5": _T + " · " + _V, "ry6": _T + " · " + _V,
}

ajoute(LEVELS, FIGS)
