"""Level path: S3 electronics, bipolar transistors, then MOS transistors and CMOS logic gates, promo 2030.

Moodle course « [Elec] Transistors » (id 6330, ECUE code `TB`): chapters 01 (Révisions S1), 02-03 (bipolar course and
« Kit de survie »), 04 (TD « Les transistors bipolaires », 5 exercises, extracts of the typed correction), 05 (« Pour
s'entraîner » : exam of March 2026 with official correction), 06-07 (MOS course), 08 (TD « Fonctions logiques en
technologie CMOS », no correction), 09-10 (Moodle test 1, bipolar transistors). Announcements: the mid-semester exam
covers the whole bipolar course and the biasing TD; small signals: method only.
Calibrated on the March 2026 exam (official correction) and on the S3 Elec finals found in `annales/raw/S3/Finals/Elec`
(2018, 2020, 2021, 2022, 2024, 2025 files: biasing, saturation, collector feedback, Darlington, amplifier). The scanned
corrections of 2020, 2021, 2022, 2024 and 2025 were read as images; the 2018 amplifier question has no correction, so its
answers are ours (checked here). Circuits are described in words and drawn as SVG (`schema.py`, `FIGS` at the end).
Levels 1 and 2 are S1/S2 reminders (Kirchhoff and divider, diode/PN junction): `elec-s1-circuits`, `elec-s2-diodes`.
In `calc`: voltages in V, currents in mA, resistances in kΩ (V/kΩ = mA), or SI units when the statement says so.
The course never gives MOS drain currents: the MOS levels only use the switch model (blocked / conducting).
"""
from schemdraw import elements as elm

from .schema import C, Fil, Masse, Point, R, SrcU, ajoute, courant, fig, schema_echelle, tension

SUBJECT = {
    "id": "electronique-s3-transistors",
    "ordre": 550,
    "matiere": "electronique",
    "semestre": "S3",
    "ecue": "TB",
    "titre": "Transistors bipolaires, MOS et portes logiques",
    "chapitres_moodle": ["[Elec] Transistors/01_Révisions", "[Elec] Transistors/02_Transistors Bipolaires",
                         "[Elec] Transistors/03_Cours", "[Elec] Transistors/04_TD",
                         "[Elec] Transistors/05_Pour s'entraîner",
                         "[Elec] Transistors/06_Transistors MOS et portes logiques", "[Elec] Transistors/07_Cours",
                         "[Elec] Transistors/08_TD", "[Elec] Transistors/09_Tests Moodle",
                         "[Elec] Transistors/10_Test 1"],
    "td": "TD « Les transistors bipolaires » (5 exercices), TD « Fonctions logiques en technologie CMOS » (4 exercices)",
    "examens": ["Examen d'électronique B7 « Transistors bipolaires » (mars 2026, corrigé officiel)",
                "Examens finaux S3 d'électronique (2018, 2020, 2021, 2022, 2024, 2025)"],
}

# ---------------------------------------------------------------- circuit figures (`schema.py`)

DX, STEP = 1.3667, 2.7      # gate-to-drain distance of a reversed MOS symbol, spacing of parallel MOS columns


def _npn(d, bx, by):
    d += (q := elm.BjtNpn().theta(0).at((bx, by)))
    return q


def _bjt(d, rc="R_C", re=None, rb=None, pont=False, fb=False, entrees=None, sortie=None, base=None):
    """NPN stage: collector load `rc` to the V_CC rail (None = wire), emitter resistor `re` (None = wire) to ground.
    Base: `rb` to V_CC, `pont` (R_1 to V_CC, R_2 to ground), `fb` (R_B from the collector), `entrees` (inputs through
    R_B), or `base` = 'gnd' / 'vcc' (wire). `sortie` labels an output terminal at the collector."""
    Y, bx, by = 4.6, 2.4, 1.2
    q = _npn(d, bx, by)
    cx, cy = q.collector
    ex, ey = q.emitter
    x0 = 0.6 if (rb or pont or fb or base == "vcc") else cx - 1.2
    d += Fil().endpoints((x0, Y), (cx, Y))
    d += elm.Vdd().at(((x0 + cx) / 2, Y)).label("$V_{CC}$")
    if rc is None:
        d += Fil().endpoints((cx, Y), (cx, cy))
    elif fb:
        d += R().endpoints((cx, Y), (cx, 3.4)).label(f"${rc}$", loc="top")
        d += Fil().endpoints((cx, 3.4), (cx, cy))
    else:
        d += R().endpoints((cx, Y), (cx, cy)).label(f"${rc}$", loc="top")
    yg = ey - 1.9 if re else ey - 0.6
    if re:
        d += R().endpoints((ex, ey), (ex, yg)).label(f"${re}$", loc="top")
    else:
        d += Fil().endpoints((ex, ey), (ex, yg))
    if pont or base == "gnd":
        d += Fil().endpoints((x0, yg), (ex, yg))
        d += Masse().at(((x0 + ex) / 2, yg))
    else:
        d += Masse().at((ex, yg))
    if rb:
        d += R().endpoints((x0, Y), (x0, by)).label(f"${rb}$", loc="bottom")
    elif pont:
        d += R().endpoints((x0, Y), (x0, by)).label("$R_1$", loc="bottom")
        d += R().endpoints((x0, by), (x0, yg)).label("$R_2$", loc="bottom")
        d += Point().at((x0, by))
    elif fb:
        d += Point().at((cx, 2.6))
        d += R().endpoints((cx, 2.6), (x0, 2.6)).label("$R_B$", loc="top")
        d += Fil().endpoints((x0, 2.6), (x0, by))
    elif base == "vcc":
        d += Fil().endpoints((x0, Y), (x0, by))
    elif base == "gnd":
        d += Fil().endpoints((x0, by), (x0, yg))
    if entrees:
        ys = [by] if len(entrees) == 1 else [by + 1.0, by - 1.0]
        for e, y in zip(entrees, ys):
            d += Point(open=True).at((-1.8, y)).label(f"${e}$", loc="left")
            d += R().endpoints((-1.8, y), (x0, y)).label("$R_B$", loc="top")
        if len(ys) == 2:
            d += Fil().endpoints((x0, ys[0]), (x0, ys[1]))
            d += Point().at((x0, by))
    d += Fil().endpoints((x0, by), (bx, by))
    if sortie:
        d += Point().at((cx, cy))
        d += Fil().endpoints((cx, cy), (cx + 1.6, cy))
        d += Point(open=True).at((cx + 1.6, cy)).label(f"${sortie}$", loc="right")


def _ampli(d, pont=False, cb=False, re=True):
    """Common-emitter amplifier: source e_G with R_G, C_1, base bias (R_B or R_1/R_2), R_C, C_2, load R_u."""
    Y, bx, by = 5.0, 4.6, 1.5
    q = _npn(d, bx, by)
    cx, cy = q.collector
    ex, ey = q.emitter
    yg = -1.4
    d += (s := SrcU().endpoints((0, yg), (0, by)))
    tension(d, s, "$v_g$", cote=False)
    d += R().endpoints((0, by), (1.8, by)).label("$R_g$", loc="top")
    d += C().endpoints((1.8, by), (3.4, by)).label("$C_1$", loc="top")
    d += Fil().endpoints((3.4, by), (bx, by))
    d += Point().at((3.4, by))
    d += Fil().endpoints((3.4, Y), (cx, Y))
    d += elm.Vdd().at((3.9, Y)).label("$V_{CC}$")
    d += R().endpoints((3.4, Y), (3.4, by)).label("$R_1$" if pont else "$R_B$", loc="top")
    if pont:
        d += R().endpoints((3.4, by), (3.4, yg)).label("$R_2$", loc="bottom")
    d += R().endpoints((cx, Y), (cx, 3.2)).label("$R_C$", loc="right")
    d += Fil().endpoints((cx, 3.2), (cx, cy))
    d += Point().at((cx, 2.7))
    d += C().endpoints((cx, 2.7), (7.0, 2.7)).label("$C_2$", loc="top")
    d += Fil().endpoints((7.0, 2.7), (8.4, 2.7))
    d += (u := R().endpoints((8.4, 2.7), (8.4, yg)).label("$R_u$", loc="bottom"))
    tension(d, u, "$u$", sens=-1, ofst=0.9)
    if re:
        d += R().endpoints((ex, ey), (ex, yg)).label("$R_E$", loc="bottom")
        if cb:
            d += Fil().endpoints((ex, ey - 0.5), (ex + 1.6, ey - 0.5))
            d += C().endpoints((ex + 1.6, ey - 0.5), (ex + 1.6, yg + 0.5)).label("$C_E$", loc="bottom")
            d += Fil().endpoints((ex + 1.6, yg + 0.5), (ex + 1.6, yg))
            d += Fil().endpoints((ex, yg), (ex + 1.6, yg))
    else:
        d += Fil().endpoints((ex, ey), (ex, yg))
    d += Fil().endpoints((0, yg), (8.4, yg))
    d += Masse().at((2.0, yg))


def _ps(d, re=False):
    """Small-signal equivalent of the common-emitter stage: R_B parallel to r (+ R_E in series), source beta*i_b."""
    d += (s := SrcU().endpoints((0, 0), (0, 3)))
    tension(d, s, "$e_G$", cote=False)
    d += R().endpoints((0, 3), (1.8, 3)).label("$R_G$", loc="top")
    d += Fil().endpoints((1.8, 3), (11.4, 3))
    d += (b := R().endpoints((3.6, 3), (3.6, 0)).label("$R_B$", loc="top"))
    tension(d, b, "$v$", sens=-1, ofst=0.9)
    d += Point().at((3.6, 3))
    ym = 1.2 if re else 0
    d += R().endpoints((6.4, 3), (6.4, ym)).label("$r$", loc="top")
    d += Point().at((6.4, 3))
    if re:
        d += R().endpoints((6.4, 1.2), (6.4, 0)).label("$R_E$", loc="top")
        d += Point().at((6.4, 1.2))
        d += Fil().endpoints((6.4, 1.2), (8.0, 1.2))
    d += elm.SourceI().endpoints((8.0, 3), (8.0, ym)).label(r"$\beta i_b$", loc="top")
    d += Point().at((8.0, 3))
    d += R().endpoints((9.6, 3), (9.6, 0)).label("$R_C$", loc="top")
    d += Point().at((9.6, 3))
    d += (u := R().endpoints((11.4, 3), (11.4, 0)).label("$R_u$", loc="bottom"))
    tension(d, u, "$u$", sens=-1, ofst=0.9)
    d += Fil().endpoints((0, 0), (11.4, 0))


def _darl(d):
    """Darlington pair: collectors joined, emitter of the left transistor on the base of the right one."""
    q1 = _npn(d, 1.2, 2.4)
    c1, e1 = q1.collector, q1.emitter
    q2 = _npn(d, 3.2, 0.6)
    c2, e2 = q2.collector, q2.emitter
    d += Fil().endpoints(e1, (e1[0], 0.6))
    d += Fil().endpoints((e1[0], 0.6), (3.2, 0.6))
    d += Fil().endpoints(c1, (c1[0], 4.4))
    d += Fil().endpoints((c1[0], 4.4), (c2[0], 4.4))
    d += Fil().endpoints((c2[0], 4.4), c2)
    d += Point().at((c2[0], 4.4))
    d += Fil().endpoints((c2[0], 4.4), (c2[0] + 1.0, 4.4))
    d += Point(open=True).at((c2[0] + 1.0, 4.4)).label("$C$", loc="right")
    d += Fil().endpoints((0, 2.4), (1.2, 2.4))
    d += Point(open=True).at((0, 2.4)).label("$B$", loc="left")
    d += Fil().endpoints(e2, (e2[0], -0.8))
    d += Fil().endpoints((e2[0], -0.8), (e2[0] + 1.0, -0.8))
    d += Point(open=True).at((e2[0] + 1.0, -0.8)).label("$E$", loc="right")


def _symbole(d):
    """NPN symbol with the sign conventions: I_B, I_C in, I_E out, V_BE, V_CE."""
    q = _npn(d, 0, 0)
    cx, cy = q.collector
    ex, ey = q.emitter
    d += (wb := Fil().endpoints((-3.2, 0), (0, 0)))
    courant(d, wb, "")
    d += elm.Label().at((-1.9, 0.45)).label("$I_B$")
    d += Point(open=True).at((-3.2, 0)).label("$B$", loc="left")
    d += (wc := Fil().endpoints((cx, cy + 2.0), (cx, cy)))
    courant(d, wc, "")
    d += elm.Label().at((cx - 0.6, cy + 1.1)).label("$I_C$")
    d += Point(open=True).at((cx, cy + 2.0)).label("$C$", loc="top")
    d += (we := Fil().endpoints((ex, ey), (ex, ey - 2.0)))
    courant(d, we, "")
    d += Point(open=True).at((ex, ey - 2.0)).label("$E$", loc="bottom")
    d += elm.Label().at((ex - 0.6, ey - 1.1)).label("$I_E$")
    d += elm.Line(arrow="->").endpoints((cx + 1.6, ey), (cx + 1.6, cy))
    d += elm.Label().at((cx + 2.4, 0)).label("$V_{CE}$")
    d += elm.Line(arrow="->").endpoints((-1.6, ey), (-1.6, 0))
    d += elm.Label().at((-0.85, ey / 2)).label("$V_{BE}$")


def _mos(d, kind, cx, ytop, lab):
    """One MOS ('N' or 'P') whose drain/source column is x = cx, top terminal at ytop; returns the bottom y."""
    ym = ytop - 0.75
    d += (elm.NFet() if kind == "N" else elm.PFet()).theta(0).reverse().at((cx - DX, ym)).anchor("gate")
    d += Point(open=True).at((cx - DX, ym)).label(f"${lab}$", loc="left")
    return ytop - 1.5


def _largeur(net):
    if isinstance(net, str):
        return 1
    op, items = net
    return max(map(_largeur, items)) if op == "S" else sum(map(_largeur, items))


def _reseau(d, net, kind, cx, y):
    """Series ('S', [...]) / parallel ('P', [...]) network of MOS from y downwards; leaves are gate labels."""
    if isinstance(net, str):
        return _mos(d, kind, cx, y, net)
    op, items = net
    if op == "S":
        for it in items:
            y = _reseau(d, it, kind, cx, y)
        return y
    xs, x, ends = [], cx, []
    for it in items:
        xs.append(x)
        ends.append(_reseau(d, it, kind, x, y))
        x += _largeur(it) * STEP
    yb = min(ends)
    d += Fil().endpoints((cx, y), (xs[-1], y))
    for xi, ye in zip(xs, ends):
        if ye > yb:
            d += Fil().endpoints((xi, ye), (xi, yb))
    d += Fil().endpoints((cx, yb), (xs[-1], yb))
    return yb


def _porte(d, pnet, nnet, sortie="V_{OUT}", etage=None):
    """CMOS gate: MOSP network from V_CC down to the output, MOSN network from the output to ground. `etage` = 'N' or
    'P' replaces that stage by a box to be completed."""
    cx, y0 = 3.0, 6.0
    wmax = max(_largeur(pnet) if pnet else 1, _largeur(nnet) if nnet else 1)
    d += elm.Vdd().at((cx, y0 + 0.7)).label("$V_{CC}$")
    d += Fil().endpoints((cx, y0 + 0.7), (cx, y0))
    if etage == "P":
        yp = _boite(d, cx, y0, "étage MOSP (à déterminer)")
    else:
        yp = _reseau(d, pnet, "P", cx, y0)
    yn = yp - 0.8
    d += Fil().endpoints((cx, yp), (cx, yn))
    d += Point().at((cx, (yp + yn) / 2))
    xr = cx + (wmax - 1) * STEP + 1.2
    d += Fil().endpoints((cx, (yp + yn) / 2), (xr, (yp + yn) / 2))
    d += Point(open=True).at((xr, (yp + yn) / 2)).label(f"${sortie}$", loc="right")
    if etage == "N":
        ye = _boite(d, cx, yn, "étage MOSN (à déterminer)")
    else:
        ye = _reseau(d, nnet, "N", cx, yn)
    d += Fil().endpoints((cx, ye), (cx, ye - 0.5))
    d += Masse().at((cx, ye - 0.5))


def _boite(d, cx, y, texte):
    """Box of height 1.6 hanging from (cx, y); returns its bottom y."""
    d += elm.Line().endpoints((cx, y), (cx, y - 0.2))
    x0, x1, y1, y2 = cx - 2.7, cx + 2.7, y - 0.2, y - 1.8
    for a, b in [((x0, y1), (x1, y1)), ((x1, y1), (x1, y2)), ((x1, y2), (x0, y2)), ((x0, y2), (x0, y1))]:
        d += elm.Line().endpoints(a, b)
    d += elm.Label().at((cx, (y1 + y2) / 2)).label(texte, fontsize=15)
    d += elm.Line().endpoints((cx, y2), (cx, y2 - 0.2))
    return y2 - 0.2


S, P = "s", "p"
FIG_DIV = schema_echelle("E", [(S, "R", "R_1"), (P, "R", "R_2")], "U")
FIG_MAILLE = schema_echelle("E", [(S, "R", "R"), (S, "Z", "D")])
FIG_DIODE = schema_echelle("E", [(S, "R", "R"), (S, "D", "D")])
FIG_DIODE_INV = schema_echelle("E", [(S, "R", "R"), (S, "D<", "D")])
FIG_JBE = schema_echelle("E", [(S, "R", "R_B"), (S, "D", "D_{BE}")])
FIG_SYMB = fig(_symbole, "Schéma : transistor NPN avec I_B et I_C entrants, I_E sortant, V_BE et V_CE")
FIG_RB = fig(lambda d: _bjt(d, rb="R_B"),
             "Schéma : NPN, R_B entre V_CC et la base, R_C entre V_CC et le collecteur, émetteur à la masse")
FIG_GND = fig(lambda d: _bjt(d, base="gnd"), "Schéma : NPN avec R_C au collecteur, base reliée à l'émetteur et à la masse")
FIG_BVCC = fig(lambda d: _bjt(d, base="vcc"), "Schéma : NPN avec R_C au collecteur, base reliée directement à V_CC")
FIG_RE = fig(lambda d: _bjt(d, rb="R_B", re="R_E"),
             "Schéma : NPN, R_B entre V_CC et la base, R_C au collecteur, R_E entre émetteur et masse")
FIG_FB = fig(lambda d: _bjt(d, fb=True),
             "Schéma : NPN, R_C entre V_CC et collecteur, R_B entre le collecteur et la base (réaction de collecteur)")
FIG_PONT_E = fig(lambda d: _bjt(d, rc=None, re="R_E", pont=True),
                 "Schéma : NPN, collecteur à V_CC, pont R_1 (vers V_CC) et R_2 (vers la masse) sur la base, R_E à l'émetteur")
FIG_PONT_C = fig(lambda d: _bjt(d, re="R_E", pont=True),
                 "Schéma : NPN, R_C au collecteur, pont R_1 (vers V_CC) et R_2 (vers la masse) sur la base, R_E à l'émetteur")
FIG_INV = fig(lambda d: _bjt(d, entrees=["V_1"], sortie="V_S"),
              "Schéma : NPN, entrée V_1 par R_B sur la base, R_C entre V_CC et collecteur, sortie V_S au collecteur")
FIG_NOR = fig(lambda d: _bjt(d, entrees=["V_1", "V_2"], sortie="V_S"),
              "Schéma : NPN, entrées V_1 et V_2 chacune par une résistance R_B vers la base, R_C au collecteur, sortie V_S")
FIG_AMP0 = fig(lambda d: _ampli(d, re=False), "Schéma : amplificateur à émetteur commun sans R_E, R_B, R_C, condensateurs C_1 et C_2, source v_g avec R_g, charge R_u")
FIG_AMP = fig(lambda d: _ampli(d), "Schéma : amplificateur à émetteur commun, R_B, R_C, R_E, condensateurs C_1 et C_2, source v_g avec R_g, charge R_u")
FIG_AMP_PONT = fig(lambda d: _ampli(d, pont=True, cb=True),
                   "Schéma : amplificateur à émetteur commun avec pont R_1 R_2, R_C, R_E découplée par C_E, C_1, C_2, charge R_u")
FIG_PS = fig(_ps, "Schéma : petits signaux, R_B en parallèle avec r, source de courant beta i_b en parallèle avec R_C et R_u")
FIG_PS_RE = fig(lambda d: _ps(d, re=True),
                "Schéma : petits signaux, r en série avec R_E, source de courant beta i_b, R_C en parallèle avec R_u")
FIG_DARL = fig(_darl, "Schéma : montage Darlington, collecteurs reliés, émetteur de T_1 sur la base de T_2")
FIG_CINV = fig(lambda d: _porte(d, "V_{IN}", "V_{IN}"), "Schéma : inverseur CMOS, un MOSP et un MOSN, grilles à V_IN")
FIG_NAND = fig(lambda d: _porte(d, ("P", ["a", "b"]), ("S", ["a", "b"])),
               "Schéma : porte CMOS, deux MOSP en parallèle, deux MOSN en série")
FIG_CNOR = fig(lambda d: _porte(d, ("S", ["a", "b"]), ("P", ["a", "b"])),
               "Schéma : porte CMOS, deux MOSP en série, deux MOSN en parallèle")
FIG_TD1 = fig(lambda d: _porte(d, ("P", [("S", ["x", "z"]), "y"]), ("S", [("P", ["x", "z"]), "y"])),
              "Schéma : porte CMOS, MOSP : x en série avec z, le tout en parallèle avec y ; MOSN : x en parallèle avec z, le tout en série avec y")
FIG_ETAGEN = fig(lambda d: _porte(d, ("P", [("S", ["a", "b"]), "c"]), None, etage="N"),
                 "Schéma : étage MOSP (a en série avec b, en parallèle avec c) ; l'étage MOSN est une boîte à déterminer")
FIG_ETAGEN_SOL = fig(lambda d: _porte(d, ("P", [("S", ["a", "b"]), "c"]), ("S", [("P", ["a", "b"]), "c"])),
                     "Schéma : porte complète, MOSN : a en parallèle avec b, le tout en série avec c")
FIG_AOI = fig(lambda d: _porte(d, ("S", [("P", ["a", "b"]), ("P", ["c", "d"])]), ("P", [("S", ["a", "b"]), ("S", ["c", "d"])])),
              "Schéma : porte CMOS à quatre entrées, MOSP : (a // b) en série avec (c // d) ; MOSN : (a série b) en parallèle avec (c série d)")
FIG_XOR = fig(lambda d: _porte(d, ("S", [("P", ["a", "b"]), ("P", [r"\bar a", r"\bar b"])]),
                               ("P", [("S", ["a", "b"]), ("S", [r"\bar a", r"\bar b"])])),
              "Schéma : OU exclusif CMOS, MOSP : (a // b) en série avec (a barre // b barre) ; MOSN : (a série b) // (a barre série b barre)")

# ---------------------------------------------------------------- notions

NOTIONS = [
    {"id": "lois", "titre": "Lois de Kirchhoff, loi d'Ohm, diviseur de tension (rappel S1)",
     "formule": r"mailles : $\sum U=0$ · nœuds : $\sum I_{entrants}=\sum I_{sortants}$ · Ohm : $U=RI$ · diviseur : $U_{R_2}=\dfrac{R_2}{R_1+R_2}E$ (même courant dans $R_1$ et $R_2$)",
     "exemple": r"$E=12$ V, $R_1=2$ kΩ, $R_2=4$ kΩ : $I=2$ mA et $U_{R_2}=8$ V",
     "cours": r"Toute l'étude d'un transistor se ramène à des lois des mailles et des nœuds : le transistor est remplacé par quelques relations (tension $V_{BE}$, courant $I_C=\beta I_B$). Rappel S1 : parcours « Outils d'analyse de circuits » (`elec-s1-circuits`). Dans les unités kΩ et mA, les volts s'obtiennent sans puissance de 10 : $1$ kΩ $\times1$ mA $=1$ V."},
    {"id": "jonction", "titre": "Jonction PN : passante ou bloquée (rappel S2)",
     "formule": r"passante : $V_{AK}=V_0\approx0{,}6$ à $0{,}7$ V · bloquée : $I=0$ · le courant va de l'anode vers la cathode · jonction base-émetteur passante : $V_{BE}=0{,}6$ ou $0{,}7$ V",
     "exemple": r"$E=5$ V, $R=430$ Ω, diode à seuil $0{,}7$ V : $I=\dfrac{5-0{,}7}{430}=10$ mA",
     "cours": r"Un transistor bipolaire contient deux jonctions PN (base-émetteur et base-collecteur), chacune passante ou bloquée comme une diode. Pour le silicium, la tension d'une jonction passante vaut $0{,}6$ ou $0{,}7$ V (donnée de l'énoncé). Rappel S2 : parcours « Diodes » (`elec-s2-diodes`)."},
    {"id": "bjt", "titre": "Le transistor bipolaire : bornes, courants, gain $\\beta$",
     "formule": r"bornes : base $B$, émetteur $E$, collecteur $C$ · NPN : $I_B$ et $I_C$ entrent, $I_E$ sort · $I_E=I_C+I_B$ · $V_{BC}=V_{BE}-V_{CE}$ · linéaire : $I_C=\beta I_B$, $I_E=(\beta+1)I_B\approx I_C$ · $\beta=\dfrac{\alpha}{1-\alpha}$",
     "exemple": r"$\beta=200$, $I_C=100$ mA : $I_B=0{,}5$ mA et $I_E=100{,}5$ mA",
     "cours": r"Deux jonctions PN, trois segments dopés : l'émetteur (fortement dopé) injecte des électrons, la base (mince, peu dopée) les transmet presque tous au collecteur. La flèche de l'émetteur donne le sens passant de la jonction base-émetteur (NPN : vers l'extérieur). Un petit courant de base commande un grand courant de collecteur : $\beta\in[15\,;500]$. On n'étudie que le NPN."},
    {"id": "modes", "titre": "Les trois modes de fonctionnement",
     "formule": r"bloqué : $I_B=I_C=0$, interrupteur ouvert $C$-$E$ · linéaire : $V_{BE}=0{,}7$ V, $I_C=\beta I_B$, $V_{CE} > 0$ (amplificateurs) · saturé : $V_{CE}=0$, interrupteur fermé, $I_B > I_{C,sat}/\beta$ · bloqué et saturé : portes logiques",
     "exemple": r"$I_B=0$ : bloqué. $I_B$ grand : saturé, $V_{CE}=0$.",
     "cours": r"Chaque jonction est passante ou bloquée, ce qui donne quatre régimes. Bloqué : les deux jonctions bloquées. Linéaire : base-émetteur passante, base-collecteur bloquée ($V_{BC} < 0{,}7$ V, ce qui revient à $V_{CE} > 0$). Saturé : les deux passantes. Le mode inverse n'est pas utilisé et n'est pas au programme. Le linéaire sert aux amplificateurs, bloqué et saturé aux portes logiques."},
    {"id": "mode_test", "titre": "Trouver le mode de fonctionnement et le courant de saturation",
     "formule": r"$I_B=0$ : bloqué · sinon on suppose le linéaire, on calcule $I_B,I_C,V_{CE}$, puis on vérifie $V_{CE} > 0$ (ou $I_C \leq I_{C,sat}$, ou $I_B \leq I_{C,sat}/\beta$) · sinon saturé · $I_{C,sat}$ : $V_{CE}=0$",
     "exemple": r"$V_{CC}=10$ V, $R_C=200$ Ω : $I_{C,sat}=\dfrac{10}{0{,}2}=50$ mA",
     "cours": r"Méthode du « Kit de survie » : si $I_B=0$, le transistor est bloqué. Sinon on suppose le linéaire, on calcule le point de polarisation, et on vérifie. Si la vérification échoue (par exemple $V_{CE} < 0$), le transistor est saturé et il faut reprendre les calculs avec $V_{CE}=0$. Pour montrer qu'un transistor n'est pas linéaire, on raisonne par l'absurde : on le suppose linéaire et on trouve $V_{CE} < 0$. Le courant de saturation $I_{C,sat}$ est le courant $I_C$ quand $V_{CE}=0$ : il ne dépend que du circuit extérieur."},
    {"id": "pol_rb", "titre": "Polarisation par résistance de base et droite de charge",
     "formule": r"$I_B=\dfrac{V_{CC}-V_{BE}}{R_B}$ · $I_C=\beta I_B$ · $V_{CE}=V_{CC}-R_CI_C$ · droite de charge : $V_{CE}=V_{CC}-R_CI_C$ (points $(V_{CC},0)$ et $(0,\frac{V_{CC}}{R_C})$) · $R_B=\beta\dfrac{V_{CC}-V_{BE}}{I_C}$",
     "exemple": r"$V_{CC}=15$ V, $\beta=200$, $I_C=100$ mA : $R_B=200\times\dfrac{14{,}3}{100}=28{,}6$ kΩ",
     "cours": r"Pour un amplificateur, le point de polarisation doit être dans la zone linéaire avant d'appliquer le signal. Montage à résistance de base : maille d'entrée $V_{CC}=R_BI_B+V_{BE}$, maille de sortie $V_{CC}=R_CI_C+V_{CE}$. Le point de repos est l'intersection de la droite de charge ($V_{CE}=V_{CC}-R_CI_C$) et de la caractéristique $I_C=\beta I_B$. On trouve $5$ inconnues ($I_B,I_C,I_E,V_{BE},V_{CE}$) : $V_{BE}$ est donné, les autres se calculent dans l'ordre $I_B$, $I_C$, $V_{CE}$. Dans les problèmes de dimensionnement, le cahier des charges ($I_C$, $V_{CE}$) fixe les résistances."},
    {"id": "pol_re", "titre": "Résistance d'émetteur et réaction de collecteur",
     "formule": r"avec $R_E$ : $V_{CC}=R_BI_B+V_{BE}+R_EI_E$, $I_B=\dfrac{V_{CC}-V_{BE}}{R_B+(\beta+1)R_E}$ · $V_{CE}=V_{CC}-R_CI_C-R_EI_E$ · $I_{C,sat}=\dfrac{V_{CC}}{R_C+R_E}$ · réaction de collecteur : $I_B=\dfrac{V_{CC}-V_{BE}}{R_B+(\beta+1)R_C}$",
     "exemple": r"$R_B=150$ kΩ, $R_E=1$ kΩ, $\beta=150$, $V_{CC}=10$ V : $I_B=\dfrac{9{,}3}{150+150}=31$ \mu A, $I_C=4{,}65$ mA",
     "cours": r"Avec une résistance d'émetteur, le courant qui la traverse est $I_E=(\beta+1)I_B\approx I_C$ : elle apparaît multipliée par $\beta+1$ dans la maille d'entrée. Avec la réaction de collecteur ($R_B$ entre collecteur et base), le courant dans $R_C$ est $I_C+I_B=(\beta+1)I_B$ : c'est $R_C$ qui est multipliée par $\beta+1$. Le transistor est linéaire tant que $V_{CE} > 0$, c'est-à-dire tant que $I_C < I_{C,sat}$. Annales : on prend souvent $\beta+1\approx\beta$ (c'est précisé)."},
    {"id": "pol_pont", "titre": "Polarisation par pont de résistances, Thévenin",
     "formule": r"$E_{th}=\dfrac{R_2}{R_1+R_2}V_{CC}$ · $R_{th}=R_1\parallel R_2$ · $I_B=\dfrac{E_{th}-V_{BE}}{R_{th}+(\beta+1)R_E}$ · $I_B$ négligeable : $V_B=E_{th}$, $I_E=\dfrac{E_{th}-V_{BE}}{R_E}$ · $V_E=V_B-V_{BE}$",
     "exemple": r"$R_1=10$ k, $R_2=5$ k, $V_{CC}=15$ V, $R_E=1$ k : $E_{th}=5$ V, $I_E=\dfrac{5-0{,}6}{1}=4{,}4$ mA",
     "cours": r"$R_1$ est reliée à $V_{CC}$, $R_2$ à la masse. Si $I_B$ est négligeable devant le courant dans $R_1$ et $R_2$, ces deux résistances sont en série et forment un pont diviseur. Sinon, le générateur de Thévenin vu par la base est $E_{th}$ en série avec $R_{th}$. Ce montage stabilise le point de repos (moins sensible à $\beta$). Si le collecteur est relié directement à $V_{CC}$, $I_{C,sat}=V_{CC}/R_E$."},
    {"id": "commut", "titre": "Transistor en commutation : inverseur et porte NOR",
     "formule": r"$V_1=0$ : $I_B=0$, bloqué, $V_S=V_{CC}$ · $V_1=V_{CC}$ : $I_B=\dfrac{V_1-V_{BE}}{R_B}$, saturé si $\beta I_B > I_{C,sat}=\dfrac{V_{CC}}{R_C}$, alors $V_S=0$ · NON · deux entrées par $R_B$ : NOR, $V_S=\overline{V_1+V_2}$",
     "exemple": r"$V_{CC}=5$ V, $R_B=10$ k, $R_C=1$ k, $\beta=100$, $V_1=5$ V : $I_B=0{,}43$ mA, $\beta I_B=43$ mA $> 5$ mA : saturé, $V_S=0$",
     "cours": r"En commutation, on n'utilise que bloqué et saturé. Entrée basse : $I_B=0$, aucun courant dans $R_C$, $V_S=V_{CC}$. Entrée haute : si $\beta I_B$ dépasse le courant maximal $V_{CC}/R_C$, le transistor est saturé et $V_S\approx0$ : c'est un inverseur. Avec deux entrées reliées à la base par deux résistances, il conduit dès qu'une entrée est haute : $V_S$ est haute seulement si les deux sont basses, c'est une porte NOR. Un transistor permet à un circuit logique de commander un courant important qu'il ne pourrait pas fournir."},
    {"id": "petits", "titre": "Petits signaux : schéma équivalent du transistor",
     "formule": r"méthode : annuler les sources continues · condensateurs $\to$ fils · transistor $\to$ $r$ entre $B$ et $E$, source $\beta i_b$ entre $C$ et $E$ (et $\rho$ en parallèle) · $r=\dfrac{mV_T}{I_{B0}}$ ($m=2$, $V_T=26$ mV) · $\rho=\dfrac{|V_{EA}|+V_{CE0}}{I_{C0}}$",
     "exemple": r"$I_{B0}=26$ \mu A : $r=\dfrac{2\times26}{0{,}026}=2$ kΩ",
     "cours": r"Autour du point de polarisation, le transistor est un quadripôle linéaire (paramètres hybrides). On retient $h_{11}=r$, $h_{21}=\beta$, $h_{22}=1/\rho$ (effet Early), $h_{12}\approx0$. La résistance de sortie $\rho$ est très grande et on la néglige souvent. Seule la méthode est à connaître pour l'examen. Étapes : (1) repérer la masse, (2) mettre les sources continues à zéro (une source de tension devient un fil), (3) remplacer les condensateurs de liaison et de découplage par des fils, (4) remplacer le transistor, (5) replacer les éléments restants entre les bonnes bornes. $r$ est inversement proportionnelle à $I_{B0}$."},
    {"id": "ampli", "titre": "Amplificateur à émetteur commun : $R_i$, $R_o$, $A_v$",
     "formule": r"$R_i=\dfrac{v}{i_1}$ · $A_v=\dfrac uv$ · $R_o$ : $R_u\to\infty$, $e_G=0$ · EC : $R_i=R_B\parallel r$, $R_o=R_C$, $A_v=-\beta\dfrac{R_C\parallel R_u}{r}$ · avec $R_E$ non découplée : $A_v=-\beta\dfrac{R_C\parallel R_u}{r+(\beta+1)R_E}$",
     "exemple": r"$\beta=100$, $R_C=R_u=5$ k, $r=2$ k : $A_v=-100\times\dfrac{2{,}5}{2}=-125$",
     "cours": r"On exprime les signaux d'entrée et de sortie en fonction du courant de commande $i_b$ : $v=r\,i_b$ (plus $(\beta+1)R_Ei_b$ s'il reste $R_E$) et $u=-(R_C\parallel R_u)\beta i_b$. L'amplification est négative : l'amplificateur inverse. Condensateurs : les condensateurs de liaison $C_1,C_2$ isolent la polarisation du générateur et de la charge (interrupteurs ouverts en continu, fils en variable) ; un condensateur de découplage $C_E$ en parallèle sur $R_E$ le court-circuite en variable. Une source de tension $V_{CC}$ ne sert qu'à polariser le transistor dans sa zone linéaire."},
    {"id": "darlington", "titre": "Montage Darlington et mise en cascade",
     "formule": r"$I_C=I_{C1}+I_{C2}$ · $I_{B2}=I_{E1}=(\beta_1+1)I_B$ · $\beta=\beta_1+\beta_2+\beta_1\beta_2\approx\beta_1\beta_2$ · cascade : $A_v=A_{v1}\cdot A_{v2}\cdots$, $R_o$ de l'étage $n$ = $R_g$ de l'étage $n+1$, $R_i$ de l'étage $n+1$ = $R_u$ de l'étage $n$",
     "exemple": r"$\beta_1=100$, $\beta_2=50$ : $\beta\approx5000$ (exact : $5150$)",
     "cours": r"Deux transistors dont l'émetteur du premier attaque la base du second se comportent comme un transistor unique de gain $\beta\approx\beta_1\beta_2$. Démonstration : $I_{C1}=\beta_1I_B$, $I_{B2}=I_B+I_{C1}=(\beta_1+1)I_B$, $I_{C2}=\beta_2(\beta_1+1)I_B$, donc $I_C=(\beta_1+\beta_2+\beta_1\beta_2)I_B$. En cascade d'amplificateurs, l'amplification totale est le produit des amplifications, chaque étage étant calculé chargé par l'étage suivant."},
    {"id": "mos", "titre": "Transistors MOS en commutation",
     "formule": r"MOSN : $V_{GS}=0$ bloqué, $V_{GS}=5$ V conducteur · MOSP : $V_{GS}=0$ bloqué, $V_{GS}=-5$ V conducteur · $V_{GS}=V_G-V_S$ · bloqué = interrupteur ouvert $D$-$S$, conducteur = interrupteur fermé · $I_G=0$",
     "exemple": r"Inverseur, $V_{IN}=0$ : $V_{GS_P}=0-5=-5$ V, MOSP conducteur ; $V_{GS_N}=0$, MOSN bloqué",
     "cours": r"Transistor à effet de champ : trois broches grille $G$, drain $D$, source $S$, commandé par la tension $V_{GS}$ (la grille est isolée, $I_G=0$ : impédance d'entrée infinie). Deux types : MOS canal N (MOSN) et canal P (MOSP). Le cours n'étudie que la commutation. Les portes TTL (bipolaires) sont rapides mais gourmandes ; les portes CMOS (MOSFET complémentaires) consomment très peu et sont commandées en tension."},
    {"id": "cmos", "titre": "Portes logiques CMOS : inverseur, NAND, NOR et fonctions composées",
     "formule": r"inverseur : $S=\overline e$ · NAND : MOSP en parallèle, MOSN en série, $S=\overline{ab}$ · NOR : MOSP en série, MOSN en parallèle, $S=\overline{a+b}$ · l'étage MOSP est le dual de l'étage MOSN (série $\leftrightarrow$ parallèle) · $S=V_{CC}$ si l'étage MOSP conduit, $S=0$ si le MOSN conduit",
     "exemple": r"MOSN : ($x$ // $z$) en série avec $y$ : $S=\overline{(x+z)\,y}$",
     "cours": r"Un montage CMOS est complémentaire : étage MOSP entre $V_{CC}$ et la sortie, étage MOSN entre la sortie et la masse, jamais conducteurs en même temps. Il suffit d'étudier un seul étage. Un MOSP conduit si sa grille est à $0$ : une branche MOSP conduit si toutes les entrées de la branche série sont à $0$. Un MOSN conduit si sa grille est à $1$. Pour compléter un montage : MOSN en série $\leftrightarrow$ MOSP en parallèle, et inversement. Équation : $S=1$ quand l'étage MOSP conduit (grille à $0$ pour chaque MOSP : une série devient un ET des complémentés, un parallèle un OU)."},
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


def _v(enonce, calc, ans, sol):
    return {"enonce": enonce, "calc": calc, "ans": ans, "sol": sol}


X26 = "Examen Elec B7 « Transistors bipolaires », mars 2026 (corrigé officiel)"
TDB = "TD « Les transistors bipolaires »"
TDC = "TD « Fonctions logiques en technologie CMOS » (sans corrigé : corrigé rédigé)"
T1 = "Test Moodle 1 « Transistors bipolaires »"
KIT = "Kit de survie « Transistors bipolaires »"
COURS = "Cours « Les transistors bipolaires »"
COURS_MOS = "Cours « Les transistors à effet de champ »"
F20 = "Examen final S3 Elec, dossier 2020 (sujet de décembre 2016, corrigé officiel)"
F21 = "Examen final S3 Elec, dossier 2021 (sujet de décembre 2017, corrigé officiel)"
F22 = "Examen final S3 Elec, dossier 2022 (sujet de décembre 2018, corrigé officiel)"
F24 = "Examen final S3 Elec, dossier 2024 (sujet de janvier 2021, corrigé officiel)"
F25 = "Examen final S3 Elec, dossier 2025 (sujet de décembre 2021, corrigé officiel)"
F18 = "Examen final S3 Elec, dossier 2018 (sujet en anglais de décembre 2014, sans corrigé : corrigé rédigé)"


LEVELS = [
    {"n": 1, "titre": "Rappel S1 : mailles, nœuds, diviseur de tension", "notions": ["lois"], "exos": [
        v("k11", r"$E=12$ V alimente $R_1=2$ kΩ en série avec $R_2=4$ kΩ. Courant $I$ (en mA) ?", "12/(2+4)", "2",
          r"Les deux résistances sont en série : $I=\dfrac{E}{R_1+R_2}=\dfrac{12}{6}=2$ mA.", src="Rappel S1 : TD0 « Révisions »", duree=1),
        v("k12", r"$E=12$ V alimente $R_1=2$ kΩ en série avec $R_2=4$ kΩ : tension $U$ aux bornes de $R_2$ (en V) ?", "12*4/(2+4)", "8",
          r"Pont diviseur de tension : $U=\dfrac{R_2}{R_1+R_2}E=\dfrac46\times12=8$ V.", src="Rappel S1 : TD0 « Révisions »", duree=1),
        v("k13", r"$E=10$ V alimente $R=2$ kΩ en série avec un dipôle $D$ dont la tension vaut $4$ V. Courant $I$ (en mA) ?", "(10-4)/2", "3",
          r"Loi des mailles : $E=RI+U_D$, donc $I=\dfrac{E-U_D}{R}=\dfrac{6}{2}=3$ mA.", src="Rappel S1 : lois de Kirchhoff", duree=2),
        v("k14", r"Dans un nœud, $5$ mA entrent par une branche, $2$ mA sortent par une deuxième. Quel courant $i$ (en mA) sort par la troisième ?", "5-2", "3",
          r"Loi des nœuds : $\sum I_{entrants}=\sum I_{sortants}$, donc $5=2+i$ et $i=3$ mA.", src="Rappel S1 : lois de Kirchhoff", duree=1),
        o("k15", r"Énoncer la loi des mailles, la loi des nœuds et la formule du diviseur de tension. À quelle condition le diviseur est-il valable ?",
          r"Mailles : la somme algébrique des tensions le long d'une maille fermée est nulle. Nœuds : la somme des courants entrants est égale à la somme des courants sortants. Diviseur : $U_{R_2}=\dfrac{R_2}{R_1+R_2}E$ ; il suppose que $R_1$ et $R_2$ sont traversées par le même courant (en série, rien d'autre branché au point milieu).", src="Rappel S1 : TD0 « Révisions »", duree=3),
    ]},
    {"n": 2, "titre": "Rappel S2 : jonction PN passante ou bloquée", "notions": ["jonction", "lois"], "exos": [
        v("j21", r"$E=5$ V alimente $R=430$ Ω en série avec une diode à seuil ($V_0=0{,}7$ V) dans le sens passant. $I$ (en mA) ?", "(5-0.7)/0.43", "10",
          r"Diode passante : maille $E=RI+V_0$, donc $I=\dfrac{5-0{,}7}{0{,}43}=10$ mA.", src="Rappel S2 : parcours Diodes", duree=2),
        v("j22", r"$E=5$ V alimente $R=430$ Ω en série avec une diode à seuil ($V_0=0{,}7$ V) montée en sens inverse. $I$ (en mA) ?", "0", "0",
          r"Diode en polarisation inverse : bloquée, interrupteur ouvert, $I=0$.", src="Rappel S2 : parcours Diodes", duree=1),
        v("j23", r"La jonction base-émetteur d'un transistor se comporte comme une diode. $E=5$ V, $R_B=10$ kΩ, jonction passante ($V_{BE}=0{,}7$ V). $I_B$ (en µA) ?", "(5-0.7)/10*1000", "430",
          r"Maille : $E=R_BI_B+V_{BE}$, donc $I_B=\dfrac{4{,}3}{10}=0{,}43$ mA $=430$ µA.", src=COURS, duree=2),
        v("j24", r"La jonction base-émetteur d'un transistor se comporte comme une diode ($V_{BE}=0{,}7$ V passante). $E=0{,}4$ V (inférieure au seuil), $R_B=10$ kΩ. $I_B$ (en µA) ?", "0", "0",
          r"$E < 0{,}7$ V : la jonction ne peut pas être passante (sinon $I_B < 0$, absurde). Elle est bloquée, $I_B=0$.", src=COURS, duree=2),
        o("j25", r"Dans quel sens circule le courant dans une jonction PN, et quelle tension a-t-elle quand elle est passante (silicium) ?",
          r"De l'anode (P) vers la cathode (N). Passante : $V_{AK}\approx0{,}6$ à $0{,}7$ V (valeur donnée par l'énoncé). Bloquée : courant nul. Un transistor NPN possède deux jonctions : base-émetteur (flèche de l'émetteur dans le sens passant) et base-collecteur.", src=COURS, duree=2),
    ]},
    {"n": 3, "titre": "Le transistor bipolaire : bornes, courants et gain", "notions": ["bjt", "modes"], "exos": [
        v("m31", r"Transistor NPN en mode linéaire, $\beta=200$, $I_C=100$ mA. Courant de base $I_B$ (en µA) ?", "100/200*1000", "500",
          r"$I_C=\beta I_B$ donc $I_B=\dfrac{100}{200}=0{,}5$ mA $=500$ µA.", src=X26 + ", ex. 3 Q7 (et " + T1 + ", Q4)", duree=1),
        v("m32", r"Transistor NPN en mode linéaire, $\beta=200$, $I_C=100$ mA. Courant d'émetteur $I_E$ (en mA) ?", "100+100/200", "100.5",
          r"$I_E=I_C+I_B=100+0{,}5=100{,}5$ mA.", src=X26 + ", ex. 3 Q8", duree=1),
        v("m33", r"Le coefficient de transfert du courant d'émetteur vaut $\alpha=0{,}99$. Gain $\beta$ en courant de base ?", "Rational(99,100)/(1-Rational(99,100))", "99",
          r"$I_C=\alpha I_E$ et $I_E=I_C+I_B$ donnent $I_C(1-\alpha)=\alpha I_B$, soit $\beta=\dfrac{\alpha}{1-\alpha}=\dfrac{0{,}99}{0{,}01}=99$.", src=COURS, duree=2),
        v("m34", r"$\beta=150$, courant de base $I_B=20$ \mu A, transistor linéaire. $I_C$ (en mA) ?", "150*20/1000", "3",
          r"$I_C=\beta I_B=150\times0{,}02=3$ mA.", src=COURS, duree=1),
        o("m35", r"Comment s'appellent les bornes d'un transistor bipolaire ? Dessiner un NPN et placer sur le schéma les courants et les tensions (sens conventionnels).",
          r"Base, émetteur, collecteur. NPN : $I_B$ et $I_C$ entrent, $I_E=I_C+I_B$ sort, $V_{BE}$ de la base vers l'émetteur, $V_{CE}$ du collecteur vers l'émetteur, et $V_{BC}=V_{BE}-V_{CE}$." "" "" "\n\n" + FIG_SYMB, src=T1 + ", Q1 et Q5", duree=3),
        o("m36", r"Quand le transistor est bloqué, saturé, ou linéaire, que valent les deux jonctions (base-émetteur, base-collecteur) et que vaut l'équivalent entre collecteur et émetteur ?",
          r"Bloqué : les deux jonctions bloquées, $I_B=I_C=0$, interrupteur ouvert entre $C$ et $E$. Saturé : les deux passantes, $V_{CE}=0$, interrupteur fermé. Linéaire : base-émetteur passante, base-collecteur bloquée, $V_{BE}=0{,}6$ ou $0{,}7$ V, $I_C=\beta I_B$, $V_{CE} > 0$.", src=T1 + ", Q2, Q3 et " + X26 + ", ex. 3 Q1 à Q6", duree=3),
    ]},
    {"n": 4, "titre": "Mode de fonctionnement et courant de saturation", "notions": ["modes", "mode_test"], "exos": [
        v("s41", r"La base est reliée à la masse (donc à l'émetteur : $V_{BE}=0$). Courant de collecteur $I_C$ (en mA) ?", "0", "0",
          r"$V_{BE}=0 < 0{,}7$ V : la jonction base-émetteur ne peut pas être passante, $I_B=0$ : le transistor est bloqué et $I_C=0$.", src=TDB + ", ex. 1 a", duree=2),
        v("s42", r"$V_{CC}=10$ V, $R_C=200$ Ω, $R_B=1500$ Ω, $\beta=50$, $V_{BE}=0{,}7$ V. Courant de saturation $I_{C,sat}$ (en mA) ?", "10/0.2", "50",
          r"Saturé : $V_{CE}=0$, donc $V_{CC}=R_CI_{C,sat}$ et $I_{C,sat}=\dfrac{10}{0{,}2}=50$ mA.", src=TDB + ", ex. 1 c", duree=2),
        v("s43", r"$V_{CC}=10$ V, $R_C=200$ Ω, $R_B=1500$ Ω, $\beta=50$, $V_{BE}=0{,}7$ V. On suppose le transistor linéaire : que vaut $V_{CE}$ (en V) ? Conclusion ?", "10-0.2*50*(10-0.7)/1.5", "-52",
          r"$I_B=\dfrac{10-0{,}7}{1{,}5}=6{,}2$ mA, $I_C=\beta I_B=310$ mA, $V_{CE}=10-0{,}2\times310=-52$ V $< 0$ : impossible, l'hypothèse est absurde. Le transistor est saturé.", src=TDB + ", ex. 1 c", duree=4),
        v("s44", r"$V_{CC}=10$ V, $R_C=200$ Ω, $R_B=1500$ Ω, $\beta=50$, $V_{BE}=0{,}7$ V. Valeur minimale du courant de base pour saturer le transistor (en µA) ?", "10/0.2/50*1000", "1000",
          r"Il sature quand $I_C=\beta I_B\geq I_{C,sat}$ : $I_B\geq\dfrac{50}{50}=1$ mA $=1000$ \mu A. Ici $I_B=6{,}2$ mA $\gg 1$ mA : saturé.", src=KIT, duree=3),
        o("s45", r"La base est reliée directement à $V_{CC}=10$ V (figure). Pourquoi le transistor n'est-il pas polarisé correctement ? Que se passe-t-il ? Même question quand la base est reliée à la masse (donc à l'émetteur, $V_{BE}=0$).",
          r"Base à $V_{CC}$ : $V_{BE}=10$ V, bien trop pour une jonction PN passante ($0{,}7$ V). Aucune résistance ne limite le courant de base : la jonction est détruite. Base à la masse : $V_{BE}=0 < 0{,}7$ V, la jonction base-émetteur est bloquée, $I_B=0$ : le transistor est bloqué.", src=TDB + ", ex. 1 a et b", duree=3),
        o("s46", r"Décrire la méthode pour trouver le mode de fonctionnement d'un transistor NPN à partir d'un circuit.",
          r"1. Si $I_B=0$, le transistor est bloqué. 2. Sinon, supposer le mode linéaire : $V_{BE}=0{,}7$ V, $I_C=\beta I_B$, $I_E=(\beta+1)I_B$, et calculer $I_B,I_C,V_{CE}$ par les lois des mailles et des nœuds. 3. Vérifier $V_{CE} > 0$ (ou $I_C\leq I_{C,sat}$, ou $I_B\leq I_{C,sat}/\beta$). 4. Si la condition n'est pas vérifiée, le transistor est saturé : reprendre avec $V_{CE}=0$. Pour prouver qu'il n'est pas linéaire, on raisonne par l'absurde.", src=KIT, duree=3),
    ]},
    {"n": 5, "titre": "Polarisation par résistance de base et droite de charge", "notions": ["pol_rb"], "exos": [
        v("p51", r"$V_{CC}=10$ V, $R_B=10$ kΩ, $R_C=50$ Ω, $\beta=100$, $V_{BE}=0{,}7$ V, transistor linéaire. Courant de base $I_B$ (en mA) ?", "(10-0.7)/10", "0.93",
          r"Maille d'entrée : $V_{CC}=R_BI_B+V_{BE}$, donc $I_B=\dfrac{9{,}3}{10}=0{,}93$ mA.", src=TDB + ", ex. 2 A (RC corrigé en 50 Ω)", duree=2),
        v("p52", r"$V_{CC}=10$ V, $R_B=10$ kΩ, $R_C=50$ Ω, $\beta=100$, $V_{BE}=0{,}7$ V, transistor linéaire. Courant de collecteur $I_C$ (en mA) ?", "100*(10-0.7)/10", "93",
          r"$I_C=\beta I_B=100\times0{,}93=93$ mA.", src=TDB + ", ex. 2 A", duree=1),
        v("p53", r"$V_{CC}=10$ V, $R_B=10$ kΩ, $R_C=50$ Ω, $\beta=100$, $V_{BE}=0{,}7$ V, transistor linéaire. Tension $V_{CE}$ (en V) ?", "10-0.05*100*(10-0.7)/10", "5.35",
          r"Maille de sortie : $V_{CE}=V_{CC}-R_CI_C=10-0{,}05\times93=5{,}35$ V $> 0$ : l'hypothèse linéaire est vérifiée.", src=TDB + ", ex. 2 A", duree=2),
        v("p54", r"$V_{CC}=15$ V, $R_C=50$ Ω, $\beta=200$, $V_{BE}=0{,}7$ V. On veut $I_C=100$ mA. Valeur de $R_B$ (en kΩ) ?", "200*(15-0.7)/100", "28.6",
          r"$V_{CE}=15-0{,}05\times100=10$ V $> 0$ : linéaire. $I_B=\dfrac{I_C}{\beta}=0{,}5$ mA et $R_B=\dfrac{V_{CC}-V_{BE}}{I_B}=\dfrac{14{,}3}{0{,}5}=28{,}6$ kΩ.", src=F24 + ", ex. 3 q.1", duree=5),
        v("p55", r"$V_{CC}=15$ V, $R_C=50$ Ω, $\beta=200$, $V_{BE}=0{,}7$ V. Courant de collecteur maximal possible $I_{C,sat}$ quand $R_B$ varie (en mA) ?", "15/0.05", "300",
          r"Maximal quand $V_{CE}=0$ : $I_{C,sat}=\dfrac{V_{CC}}{R_C}=\dfrac{15}{0{,}05}=300$ mA.", src=F24 + ", ex. 3 q.2", duree=3),
        v("p56", r"$V_{CC}=15$ V, $R_C=50$ Ω, $\beta=200$, $V_{BE}=0{,}7$ V. Valeur minimale de $R_B$ pour que le transistor ne soit pas saturé (en kΩ, valeur exacte) ?", "200*(15-0.7)/300", "28.6/3",
          r"Linéaire tant que $I_C < I_{C,sat}$ : $R_B=\beta\dfrac{V_{CC}-V_{BE}}{I_C} > \beta\dfrac{V_{CC}-V_{BE}}{I_{C,sat}}=200\times\dfrac{14{,}3}{300}=\dfrac{28{,}6}{3}\approx9{,}53$ kΩ. (Le corrigé officiel écrit $\frac{28{,}8}{3}$ kΩ, coquille : $15-0{,}7=14{,}3$.)", src=F24 + ", ex. 3 q.3", duree=5),
        v("p58", r"$V_{CC}=12$ V, $R_C=100$ Ω. On veut placer le point de repos au milieu de la droite de charge ($V_{CE}=V_{CC}/2$). $I_C$ (en mA) ?", "(12-6)/0.1", "60",
          r"$V_{CE}=V_{CC}-R_CI_C$ donne $I_C=\dfrac{12-6}{0{,}1}=60$ mA.", src=COURS, duree=2),
        o("p57", r"Qu'est-ce que la droite de charge ? Donner ses deux points d'intersection avec les axes et expliquer comment elle donne le point de repos.",
          r"C'est la droite $V_{CE}=V_{CC}-R_CI_C$ (maille de sortie) tracée dans le plan des caractéristiques de sortie $I_C=f(V_{CE})$. Elle coupe l'axe $V_{CE}$ en $(V_{CC},0)$ (transistor bloqué) et l'axe $I_C$ en $(0,\frac{V_{CC}}{R_C})$ (saturé, $I_{C,sat}$). Le point de repos est son intersection avec la courbe $I_B=I_{B0}$ imposée par la maille d'entrée. Pour un amplificateur, on le place dans la zone linéaire, par exemple au milieu.", src=COURS, duree=3),
        o("p59", r"Montage de polarisation par résistance de base, transistor linéaire. Donner $V_{BE}$, $I_B$ et $V_{CE}$ en fonction de $V_{CC}$, $R_B$, $R_C$, $\beta$.",
          r"$V_{BE}=0{,}7$ V (ou $0{,}6$ V selon l'énoncé). $I_B=\dfrac{V_{CC}-V_{BE}}{R_B}$. $V_{CE}=V_{CC}-R_CI_C=V_{CC}-\beta R_CI_B$.", src=T1 + ", Q6 à Q8", duree=3),
    ]},
    {"n": 6, "titre": "Résistance d'émetteur et réaction de collecteur", "notions": ["pol_re"], "exos": [
        v("e61", r"$V_{CC}=10$ V, $R_B=150$ kΩ, $R_C=1$ kΩ, $R_E=1$ kΩ, $\beta=150$, $V_{BE}=0{,}7$ V. Transistor linéaire, $\beta+1\approx\beta$. Courant de base $I_B$ (en µA) ?", "(10-0.7)/(150+150*1)*1000", "31",
          r"Maille d'entrée : $V_{CC}=R_BI_B+V_{BE}+R_EI_E$ avec $I_E=(\beta+1)I_B\approx\beta I_B$. Donc $I_B=\dfrac{V_{CC}-V_{BE}}{R_B+\beta R_E}=\dfrac{9{,}3}{150+150}=0{,}031$ mA $=31$ µA.", src=X26 + ", ex. 1 A.2", duree=4),
        v("e62", r"$V_{CC}=10$ V, $R_B=150$ kΩ, $R_C=1$ kΩ, $R_E=1$ kΩ, $\beta=150$, $V_{BE}=0{,}7$ V, transistor linéaire, $\beta+1\approx\beta$. Courant de collecteur $I_C$ (en mA) ?", "150*(10-0.7)/(150+150*1)", "4.65",
          r"$I_C=\beta I_B=150\times0{,}031=4{,}65$ mA.", src=X26 + ", ex. 1 A.2", duree=2),
        v("e63", r"$V_{CC}=10$ V, $R_B=150$ kΩ, $R_C=1$ kΩ, $R_E=1$ kΩ, $\beta=150$, $V_{BE}=0{,}7$ V, transistor linéaire, $\beta+1\approx\beta$. Tension $V_{CE}$ (en V) ?", "10-(1+1)*150*(10-0.7)/(150+150*1)", "0.7",
          r"Maille de sortie : $V_{CE}=V_{CC}-R_CI_C-R_EI_E=V_{CC}-(R_C+R_E)I_C=10-2\times4{,}65=0{,}7$ V.", src=X26 + ", ex. 1 A.2 (corrigé : 0,7 V)", duree=2),
        v("e64", r"$V_{CC}=10$ V, $R_C=1$ kΩ, $R_E=1$ kΩ, $\beta=150$, $V_{BE}=0{,}7$ V, transistor linéaire. On veut $I_C=4{,}65$ mA. Quelle valeur de $R_B$ (en kΩ) ? ($\beta+1\approx\beta$)", "(10-0.7-1*4.65)/(4.65/150)", "150",
          r"$I_B=\dfrac{I_C}{\beta}=0{,}031$ mA. $V_{CC}=R_BI_B+V_{BE}+R_EI_E$ avec $I_E\approx I_C$ : $R_B=\dfrac{V_{CC}-V_{BE}-R_EI_C}{I_B}=\dfrac{10-0{,}7-4{,}65}{0{,}031}=150$ kΩ.", src=F25 + ", ex. 2 q.1b", duree=5),
        v("e65", r"$V_{CC}=10$ V, $R_C=1$ kΩ, $R_E=1$ kΩ, $\beta=150$, $V_{BE}=0{,}7$ V, transistor linéaire. Valeur minimale de $R_B$ (en kΩ) qui assure un fonctionnement linéaire ? ($\beta+1\approx\beta$)", "150*(10-0.7)/(10/(1+1))-150*1", "129",
          r"Linéaire tant que $V_{CE} > 0$, soit $I_C < I_{C,sat}=\dfrac{V_{CC}}{R_C+R_E}=5$ mA. Comme $I_C=\beta\dfrac{V_{CC}-V_{BE}}{R_B+\beta R_E}$, la condition donne $R_B > \beta\left(\dfrac{V_{CC}-V_{BE}}{I_{C,sat}}-R_E\right)=150\times(1{,}86-1)=129$ kΩ.", src=F25 + ", ex. 2 q.2", duree=6),
        v("e66", r"$V_{CC}=10$ V, $R_C=1$ kΩ, $R_B=99$ kΩ entre collecteur et base, $\beta=100$, $V_{BE}=0{,}7$ V, transistor linéaire. Courant de base $I_B$ (en µA) ?", "(10-0.7)/(99+(100+1)*1)*1000", "46.5",
          r"Le courant dans $R_C$ est $I_C+I_B=(\beta+1)I_B$. Maille : $V_{CC}=R_C(\beta+1)I_B+R_BI_B+V_{BE}$, donc $I_B=\dfrac{V_{CC}-V_{BE}}{R_B+(\beta+1)R_C}=\dfrac{9{,}3}{99+101}=46{,}5$ µA.", src=F21 + ", ex. 4 et " + X26 + ", ex. 3 Q9", duree=4),
        v("e67", r"$V_{CC}=10$ V, $R_C=1$ kΩ, $R_B=99$ kΩ entre collecteur et base, $\beta=100$, $V_{BE}=0{,}7$ V, transistor linéaire. Tension $V_{CE}$ (en V) ?", "10-1*(100+1)*(10-0.7)/(99+(100+1)*1)", "5.3035",
          r"$V_{CE}=V_{CC}-R_C(\beta+1)I_B=10-101\times0{,}0465=10-4{,}6965=5{,}3035$ V $> 0$ : linéaire.", src=F21 + ", ex. 4", duree=3),
        o("e68", r"Montage à réaction de collecteur (QCM mars 2026, Q9). Quelle est la bonne loi des mailles, parmi $V_{CC}=(\beta+1)R_CI_B+R_BI_B+V_{BE}$ ou $V_{CC}=R_CI_C+R_BI_B+V_{BE}$ ? Le transistor peut-il saturer ?",
          r"La première : le courant dans $R_C$ est $I_C+I_B=(\beta+1)I_B$, pas $I_C$. Le transistor ne peut pas saturer : $V_{CE}=V_{BE}+R_BI_B > V_{BE}=0{,}7$ V $> V_{CE,sat}$, donc $V_{CE}$ reste strictement positive tant que $I_B > 0$ (annale 2021, question bonus).", src=X26 + ", ex. 3 Q9 et " + F21 + ", ex. 4 bonus", duree=5),
    ]},
    {"n": 7, "titre": "Pont de résistances et dimensionnement", "notions": ["pol_pont"], "exos": [
        v("q71", r"$V_{CC}=15$ V, $R_1=10$ kΩ (vers $V_{CC}$), $R_2=5$ kΩ (vers la masse), $R_E=1000$ Ω, $\beta=200$, $V_{BE}=0{,}6$ V. Le collecteur est relié à $V_{CC}$. Courant de saturation $I_{C,sat}$ (en mA) ?", "15/1", "15",
          r"Saturé : $V_{CE}=0$, donc $V_{CC}=R_EI_E$ et $I_{C,sat}=I_{E,sat}=\dfrac{15}{1}=15$ mA.", src=X26 + ", ex. 2 q.1", duree=2),
        v("q72", r"$V_{CC}=15$ V, $R_1=10$ kΩ (vers $V_{CC}$), $R_2=5$ kΩ (vers la masse), $R_E=1000$ Ω, $\beta=200$, $V_{BE}=0{,}6$ V, collecteur relié à $V_{CC}$. $I_B$ est négligeable devant les courants de $R_1$ et $R_2$ et $\beta+1\approx\beta$. Courant d'émetteur $I_E$ (en mA) ?", "(5/(10+5)*15-0.6)/1", "4.4",
          r"$R_1$ et $R_2$ sont en série : $U_{R_2}=\dfrac{R_2}{R_1+R_2}V_{CC}=5$ V. Maille : $U_{R_2}=V_{BE}+R_EI_E$, donc $I_E=\dfrac{5-0{,}6}{1}=4{,}4$ mA.", src=X26 + ", ex. 2 q.2", duree=4),
        v("q73", r"$V_{CC}=15$ V, $R_1=10$ kΩ (vers $V_{CC}$), $R_2=5$ kΩ (vers la masse), $R_E=1000$ Ω, $\beta=200$, $V_{BE}=0{,}6$ V, collecteur relié à $V_{CC}$. On suppose $I_B$ négligeable devant les courants de $R_1$ et $R_2$ et $\beta+1\approx\beta$. Courant de base $I_B$ (en µA) ?", "4.4/200*1000", "22",
          r"$I_B=\dfrac{I_C}{\beta}\approx\dfrac{I_E}{\beta}=\dfrac{4{,}4}{200}=0{,}022$ mA $=22$ µA.", src=X26 + ", ex. 2 q.3", duree=2),
        v("q74", r"$V_{CC}=15$ V, $R_1=10$ kΩ (vers $V_{CC}$), $R_2=5$ kΩ (vers la masse), $R_E=1000$ Ω, $\beta=200$, $V_{BE}=0{,}6$ V, collecteur relié à $V_{CC}$. On suppose $I_B$ négligeable devant les courants de $R_1$ et $R_2$ et $\beta+1\approx\beta$. Tension $V_{CE}$ (en V) ?", "15-1*4.4", "10.6",
          r"$V_{CC}=V_{CE}+R_EI_E$ donc $V_{CE}=15-1\times4{,}4=10{,}6$ V.", src=X26 + ", ex. 2 q.3", duree=2),
        v("q76", r"$V_{CC}=15$ V, $R_1=10$ kΩ (vers $V_{CC}$), $R_2=5$ kΩ (vers la masse), $R_E=1000$ Ω, $\beta=200$, $V_{BE}=0{,}6$ V, collecteur relié à $V_{CC}$. Sans négliger $I_B$ : on utilise le générateur de Thévenin vu par la base et $\beta=200$ (avec $\beta+1$). $I_B$ (en µA, valeur exacte) ?", "(5-0.6)/(Rational(10,3)+(200+1)*1)*1000", "13200/613",
          r"$E_{th}=\dfrac{R_2}{R_1+R_2}V_{CC}=5$ V, $R_{th}=R_1\parallel R_2=\dfrac{10}{3}$ kΩ. $I_B=\dfrac{E_{th}-V_{BE}}{R_{th}+(\beta+1)R_E}=\dfrac{4{,}4}{\frac{10}3+201}\approx21{,}5$ \mu A : très proche de $22$ \mu A, l'approximation $I_B$ négligeable est bonne.", src="Méthode de " + F22 + ", ex. 4 (Thévenin)", duree=6),
        v("q77", r"$V_{CC}=10$ V, $\beta=100$, $V_{BE}=0{,}7$ V. Point de repos voulu : $V_C=6$ V, $I_B=100$ \mu A. Valeur de $R_C$ (en Ω) ?", "(10-6)/(100*0.1)*1000", "400",
          r"$I_C=\beta I_B=10$ mA. $V_{CC}-V_C=R_CI_C$ donne $R_C=\dfrac{4}{10}=0{,}4$ kΩ $=400$ Ω (corrigé du TD). Et $V_{CE}=V_C-V_E > 0$ si $V_E < 6$ V.", src=TDB + ", ex. 3 A.2", duree=4),
        v("q78", r"Dans le montage de la figure, avec $V_E=2$ V et $I_E\approx I_C=10$ mA. Valeur de $R_E$ (en Ω) ?", "2/10*1000", "200",
          r"$R_E=\dfrac{V_E}{I_E}=\dfrac{2}{10}=0{,}2$ kΩ $=200$ Ω.", src=TDB + ", ex. 3 A.2", duree=2),
        v("q79", r"Dans le montage de la figure ($V_{CC}=10$ V, $V_E=2$ V, $V_{BE}=0{,}7$ V, $I_B=0{,}1$ mA). On impose $0{,}9$ mA dans $R_2$ (vers la masse). Valeur de $R_1$ (en kΩ) ?", "(10-2.7)/(0.9+0.1)", "7.3",
          r"$V_B=V_E+V_{BE}=2{,}7$ V, donc $R_2=\dfrac{2{,}7}{0{,}9}=3$ kΩ. Loi des nœuds : le courant dans $R_1$ vaut $0{,}9+0{,}1=1$ mA, donc $R_1=\dfrac{V_{CC}-V_B}{1}=7{,}3$ kΩ.", src=TDB + ", ex. 3 A.2", duree=5),
        o("q75", r"Dans le montage de l'examen (collecteur à $V_{CC}$, $R_E=1$ kΩ, $V_{CC}=15$ V), pourquoi peut-on affirmer que le transistor fonctionne en mode linéaire ?",
          r"$I_B$ négligeable donne $I_E=4{,}4$ mA et $I_C=I_E\approx\beta I_B < I_{C,sat}=15$ mA. Tant que $I_C < I_{C,sat}$, $V_{CE}=V_{CC}-R_EI_E > 0$ : le transistor n'est pas saturé, il est linéaire ($V_{CE}=10{,}6$ V).", src=X26 + ", ex. 2 bonus", duree=3),
        o("q80", r"Pourquoi dit-on que $R_1$ et $R_2$ sont « en série » quand $I_B$ est négligeable, et comment choisit-on les courants dans le pont ?",
          r"Le courant de base est le seul courant qui quitte le point milieu du pont. S'il est négligeable devant les courants de $R_1$ et $R_2$, ces deux courants sont égaux : les résistances sont en série et le pont diviseur donne $V_B=\dfrac{R_2}{R_1+R_2}V_{CC}$. Dans un dimensionnement, on impose un courant de pont plusieurs fois plus grand que $I_B$ (ici $0{,}9$ mA contre $0{,}1$ mA) et on applique la loi des nœuds pour $R_1$.", src=X26 + ", ex. 2 q.2 (remarque)", duree=3),
    ]},
    {"n": 8, "titre": "Transistor en commutation : inverseur et porte NOR", "notions": ["commut", "mode_test"], "exos": [
        v("c81", r"$V_{CC}=5$ V, $R_B=10$ kΩ, $R_C=1$ kΩ, $\beta=100$, $V_{BE}=0{,}7$ V. Entrée $V_1=0$ V : le transistor est bloqué. Tension de sortie $V_S$ (en V) ?", "5-1*0", "5",
          r"$V_{BE}=0$ : jonction bloquée, $I_B=0$, donc $I_C=0$. Aucune chute dans $R_C$ : $V_S=V_{CC}=5$ V.", src=TDB + ", ex. 4 q.1", duree=2),
        v("c82", r"$V_{CC}=5$ V, $R_B=10$ kΩ, $R_C=1$ kΩ, $\beta=100$, $V_{BE}=0{,}7$ V. Entrée $V_1=5$ V. Courant de base $I_B$ (en mA) ?", "(5-0.7)/10", "0.43",
          r"$V_1=R_BI_B+V_{BE}$ donc $I_B=\dfrac{5-0{,}7}{10}=0{,}43$ mA.", src=TDB + ", ex. 4 q.2", duree=2),
        v("c83", r"$V_{CC}=5$ V, $R_B=10$ kΩ, $R_C=1$ kΩ, $\beta=100$, $V_{BE}=0{,}7$ V. Entrée $V_1=5$ V. Courant de collecteur théorique $\beta I_B$ (en mA) ?", "100*(5-0.7)/10", "43",
          r"$\beta I_B=100\times0{,}43=43$ mA (valeur théorique si le transistor était linéaire).", src=TDB + ", ex. 4 q.2", duree=2),
        v("c84", r"$V_{CC}=5$ V, $R_B=10$ kΩ, $R_C=1$ kΩ, $\beta=100$, $V_{BE}=0{,}7$ V. Courant de saturation $I_{C,sat}$ (en mA) ?", "5/1", "5",
          r"$V_{CE}=0$ : $I_{C,sat}=\dfrac{V_{CC}}{R_C}=5$ mA. Comme $43 > 5$ mA, le transistor est saturé.", src=TDB + ", ex. 4 q.2", duree=2),
        v("c85", r"$V_{CC}=5$ V, $R_B=10$ kΩ, $R_C=1$ kΩ, $\beta=100$, $V_{BE}=0{,}7$ V. Le transistor est saturé : $I_C=I_{C,sat}$. Tension de sortie $V_S$ (en V) ?", "5-1*(5/1)", "0",
          r"$V_S=V_{CE}=V_{CC}-R_CI_{C,sat}=5-1\times5=0$ V : le montage inverse (fonction NON).", src=TDB + ", ex. 4 q.2 et q.3", duree=2),
        v("c86", r"$V_{CC}=5$ V, $R_B=10$ kΩ, $R_C=1$ kΩ, $\beta=100$, $V_{BE}=0{,}7$ V. Valeur maximale de $R_B$ (en kΩ) qui sature encore le transistor quand $V_1=5$ V ?", "100*(5-0.7)/5", "86",
          r"Saturé si $\beta I_B\geq I_{C,sat}$ : $I_B\geq0{,}05$ mA, soit $R_B\leq\dfrac{V_1-V_{BE}}{0{,}05}=\dfrac{4{,}3}{0{,}05}=86$ kΩ.", src=KIT, duree=4),
        v("c88", r"Montage à deux entrées $V_1$ et $V_2$, chacune reliée à la base par $R_B=10$ kΩ ; $V_1=V_2=5$ V. Courant de base total (en mA, $V_{BE}=0{,}7$ V) ?", "2*(5-0.7)/10", "0.86",
          r"Chaque résistance apporte $\dfrac{5-0{,}7}{10}=0{,}43$ mA : $I_B=0{,}86$ mA, $\beta I_B=86$ mA $\gg 5$ mA : saturé, $V_S=0$.", src=TDB + ", ex. 5", duree=3),
        o("c87", r"Montage à deux entrées $V_1$, $V_2$ (figure, $\beta=100$, $V_{CC}=5$ V, $R_C=1$ kΩ). Compléter la table de vérité de $V_S$ et identifier la fonction. Pourquoi le transistor conduit-il dès qu'une entrée est haute ?",
          r"$V_1=V_2=0$ : $I_B=0$, bloqué, $V_S=5$ V. Une seule entrée à $5$ V : $I_B=0{,}43$ mA, $\beta I_B=43 > 5$ mA, saturé, $V_S=0$. Deux entrées à $5$ V : $I_B=0{,}86$ mA, saturé, $V_S=0$. Table : $(0,0)\to5$ ; $(0,5)\to0$ ; $(5,0)\to0$ ; $(5,5)\to0$ : c'est un NOR, $V_S=\overline{V_1+V_2}$. Il suffit d'une entrée haute pour que $I_B$ dépasse $I_{C,sat}/\beta=0{,}05$ mA : les courants des deux entrées s'additionnent. Le ventilateur est activé quand $V_S$ est à l'état bas, c'est-à-dire dès qu'une alerte est active.", src=TDB + ", ex. 5", duree=6),
        o("c89", r"Quelle fonction logique réalise le montage à une entrée $V_1$ (figure de l'inverseur) ? Pourquoi utiliser un transistor plutôt qu'une liaison directe entre deux circuits numériques ?",
          r"Un inverseur (NON) : $V_1=0\Rightarrow V_S=5$ V, $V_1=5$ V $\Rightarrow V_S=0$. Une sortie logique ne peut fournir qu'un courant faible. Le transistor est commandé par un faible courant de base ($0{,}43$ mA) et permet de contrôler un courant bien plus grand dans $R_C$ ou une charge : il adapte les niveaux et isole la commande de la puissance.", src=TDB + ", ex. 4 q.3 et q.4", duree=4),
    ]},
    {"n": 9, "titre": "Petits signaux : schéma équivalent et paramètres", "notions": ["petits"], "exos": [
        o("g91", r"Donner la méthode pour obtenir le schéma équivalent petits signaux d'un amplificateur à transistor bipolaire.",
          r"1. Repérer la masse. 2. Annuler les sources continues (une source de tension continue devient un fil, $V_{CC}$ est reliée à la masse). 3. Remplacer les condensateurs (liaison, découplage) par des fils. 4. Remplacer le transistor par son schéma équivalent : $r$ entre base et émetteur, source de courant $\beta i_b$ entre collecteur et émetteur (en parallèle avec $\rho$, souvent négligée). 5. Replacer les éléments restants du circuit initial entre les bornes correspondantes.", src=KIT, duree=4),
        v("g92", r"Le point de polarisation donne $I_{B0}=26$ \mu A. Avec $m=2$ et $V_T=26$ mV, résistance d'entrée $r=\dfrac{mV_T}{I_{B0}}$ (en Ω) ?", "2*26/Rational(26,1000)", "2000",
          r"$r=\dfrac{2\times26\text{ mV}}{26\text{}\mu\text{A}}=2000$ Ω.", src=COURS + ", IV.2", duree=2),
        v("g93", r"Résistance d'entrée $r=\dfrac{mV_T}{I_{B0}}$ avec $m=2$, $V_T=26$ mV et $I_{B0}=25$ \mu A. $r$ (en Ω) ?", "2*26/Rational(25,1000)", "2080",
          r"$r=\dfrac{52\text{ mV}}{25\text{}\mu\text{A}}=2080$ Ω.", src=COURS + ", IV.2", duree=2),
        v("g94", r"Tension d'Early $|V_{EA}|=100$ V, point de polarisation $V_{CE0}=5$ V et $I_{C0}=1$ mA. Résistance de sortie $\rho=\dfrac{|V_{EA}|+V_{CE0}}{I_{C0}}$ (en kΩ) ?", "(100+5)/1", "105",
          r"$\rho=\dfrac{100+5}{1\text{ mA}}=105$ kΩ : très grande, on la néglige souvent.", src=COURS + ", IV.4", duree=2),
        v("g98", r"Le courant de base de polarisation double et passe à $52$ \mu A ($m=2$, $V_T=26$ mV). Nouvelle valeur de $r$ (en Ω) ?", "2*26/Rational(52,1000)", "1000",
          r"$r=\dfrac{52}{0{,}052}=1000$ Ω : $r$ est inversement proportionnelle à $I_{B0}$ (elle a été divisée par $2$ par rapport aux $2000$ Ω).", src=COURS + ", IV.2", duree=2),
        o("g95", r"Dessiner le schéma équivalent petits signaux de l'amplificateur à émetteur commun de la figure (polarisation par résistance de base, sans $R_E$) en négligeant la résistance de sortie du transistor.",
          r"On met $V_{CC}$ et la masse au même potentiel, $C_1$ et $C_2$ deviennent des fils : $R_B$ se retrouve entre la base et la masse, $R_C$ entre le collecteur et la masse (via l'alimentation annulée). Le transistor est remplacé par $r$ (base-émetteur) et la source $\beta i_b$ (collecteur-émetteur). Résultat : $R_B$ en parallèle avec $r$ à l'entrée, $\beta i_b$ en parallèle avec $R_C$ et $R_u$ à la sortie." "" "\n\n" + FIG_PS, src=TDB + ", ex. 2 B.1", duree=6),
        o("g97", r"Dans l'amplificateur de la figure, à quoi servent la source continue $V_{CC}$ et les deux condensateurs $C_1$ et $C_2$ ?",
          r"$V_{CC}$ polarise le transistor : elle place le point de fonctionnement dans la zone linéaire. Les condensateurs de liaison coupent les composantes continues (interrupteurs ouverts en continu) : les potentiels continus de la base et du collecteur n'influencent ni le générateur ni la charge. Ils laissent passer le signal variable (fils en régime variable).", src=T1 + ", Q9 et Q10", duree=3),
    ]},
    {"n": 10, "titre": "Amplificateur à émetteur commun : $R_i$, $R_o$, $A_v$", "notions": ["ampli", "petits"], "exos": [
        v("a101", r"Amplificateur à émetteur commun sans $R_E$, résistance de sortie du transistor négligée. $R_B=18$ kΩ et $r=2$ kΩ. Résistance d'entrée $R_i$ (en kΩ) ?", "18*2/(18+2)", "1.8",
          r"À l'entrée, $R_B$ et $r$ sont en parallèle : $R_i=\dfrac{rR_B}{r+R_B}=\dfrac{36}{20}=1{,}8$ kΩ.", src=TDB + ", ex. 2 B.2", duree=2),
        v("a102", r"Amplificateur à émetteur commun sans $R_E$ (figure), résistance de sortie du transistor négligée, $\beta=100$, $R_C=5$ kΩ, $r=2$ kΩ, à vide ($R_u\to\infty$). Amplification en tension $A_v$ ?", "-100*5/2", "-250",
          r"$v=r\,i_b$ et $u=-R_C\beta i_b$ : $A_v=-\beta\dfrac{R_C}{r}=-100\times\dfrac{5}{2}=-250$.", src=TDB + ", ex. 2 B.2", duree=3),
        v("a103", r"Amplificateur à émetteur commun sans $R_E$ (figure), résistance de sortie du transistor négligée, $\beta=100$, $R_C=5$ kΩ, $r=2$ kΩ, chargé par $R_u=5$ kΩ. $A_v$ ?", "-100*(5*5/(5+5))/2", "-125",
          r"$u=-(R_C\parallel R_u)\beta i_b$ avec $R_C\parallel R_u=2{,}5$ kΩ : $A_v=-\beta\dfrac{R_C\parallel R_u}{r}=-100\times\dfrac{2{,}5}{2}=-125$.", src=TDB + ", ex. 2 B.2", duree=3),
        v("a104", r"Amplificateur de la figure avec $R_E=0{,}1$ kΩ non découplée, $\beta=100$ ($\beta+1\approx\beta$), $R_C=R_u=6$ kΩ, $r=2$ kΩ. $A_v$ ?", "-100*(6*6/(6+6))/(2+100*0.1)", "-25",
          r"$v=r\,i_b+(\beta+1)R_Ei_b\approx(r+\beta R_E)i_b=12\,i_b$ (en kΩ). $u=-(R_C\parallel R_u)\beta i_b=-3\times100\,i_b$. $A_v=-\dfrac{300}{12}=-25$ : $R_E$ divise le gain.", src=X26 + ", ex. 1 B.2", duree=5),
        v("a105", r"Le générateur a une amplitude $e_G=50$ mV et une résistance interne $R_g=0{,}6$ kΩ ; l'amplificateur a $R_i=1{,}8$ kΩ. Amplitude de la tension d'entrée $v$ (en mV) ?", "50*1.8/(1.8+0.6)", "37.5",
          r"$R_g$ et $R_i$ forment un diviseur : $v=\dfrac{R_i}{R_i+R_g}e_G=\dfrac{1{,}8}{2{,}4}\times50=37{,}5$ mV.", src=F18 + ", ex. 4", duree=3),
        o("a106", r"Amplificateur de la figure (mars 2026). Donner le schéma équivalent petits signaux, puis l'expression littérale de $A_v=\dfrac uv$ ($\beta+1\approx\beta$, résistance de sortie du transistor négligée ; exprimer $v$ et $u$ en fonction de $i_b$).",
          r"Schéma : $r$ en série avec $R_E$ (le courant $(\beta+1)i_b$ traverse $R_E$), le tout en parallèle avec $R_B$ ; source $\beta i_b$ en parallèle avec $R_C$ et $R_u$." "" "\n\n" + FIG_PS_RE + "\n\n" r"$v=r\,i_b+(\beta+1)R_Ei_b=(r+\beta R_E)i_b$ ; $u=-\dfrac{R_CR_u}{R_C+R_u}\beta i_b$. Donc $A_v=\dfrac uv=-\dfrac{\beta R_CR_u}{(r+\beta R_E)(R_C+R_u)}$.", src=X26 + ", ex. 1 B (corrigé officiel)", duree=8),
    ]},
    {"n": 11, "titre": "Montage Darlington et étages en cascade", "notions": ["darlington", "ampli"], "exos": [
        v("d111", r"Deux transistors forment un Darlington (figure), $\beta_1=100$, $\beta_2=50$, grands devant $1$. Gain du transistor équivalent $\beta\approx\beta_1\beta_2$ ?", "100*50", "5000",
          r"$I_{C1}=\beta_1I_B$, $I_{B2}=I_B+I_{C1}=(\beta_1+1)I_B$, $I_{C2}=\beta_2I_{B2}$. Alors $I_C=\beta_1I_B+\beta_2(\beta_1+1)I_B\approx\beta_1\beta_2I_B$ : $\beta\approx5000$.", src=F25 + ", ex. 3", duree=4),
        v("d112", r"Darlington (figure), $\beta_1=100$, $\beta_2=50$, sans approximation : $\beta=\beta_1+\beta_2+\beta_1\beta_2$ ?", "100+50+100*50", "5150",
          r"$I_C=[\beta_1+\beta_2(\beta_1+1)]I_B=(\beta_1+\beta_2+\beta_1\beta_2)I_B$ : $\beta=100+50+5000=5150$ (le corrigé 2020 donne $\beta=\beta_1\beta_2+\beta_1+\beta_2$).", src=F20 + ", ex. 4", duree=3),
        v("d113", r"Darlington de gain $\beta\approx5000$, courant de base $I_B=2$ \mu A. Courant de collecteur $I_C$ (en mA) ?", "5000*2/1000", "10",
          r"$I_C=\beta I_B=5000\times2\text{}\mu\text{A}=10$ mA : un courant de base minuscule commande un courant important.", src=F25 + ", ex. 3", duree=2),
        v("d114", r"Deux étages amplificateurs en cascade, chacun mesuré chargé par le suivant : $A_{v1}=-20$ et $A_{v2}=-10$. Amplification totale $A_v$ ?", "(-20)*(-10)", "200",
          r"$A_v=A_{v1}A_{v2}=(-20)(-10)=200$ : deux inversions, un signal en phase.", src=COURS + ", V.2", duree=2),
        v("d116", r"Étage $1$ : $A_{v1}$ à vide $=-50$, $R_o=1$ kΩ. L'étage $2$ a pour résistance d'entrée $R_{i2}=1$ kΩ. Amplification de l'étage $1$ chargé par l'étage $2$ ?", "-50*1/(1+1)", "-25",
          r"$R_{i2}$ joue le rôle de $R_u$ pour l'étage $1$ et $R_o$ celui de $R_g$ pour l'étage $2$ : diviseur $\dfrac{R_{i2}}{R_{i2}+R_{o1}}=\dfrac12$, donc $A_{v1,charge}=-50\times\dfrac12=-25$.", src=COURS + ", V.2 (remarque)", duree=3),
        o("d115", r"Montage Darlington (figure) : démontrer que le gain en courant du transistor équivalent vaut $\beta\approx\beta_1\beta_2$.",
          r"$I_C=I_{C1}+I_{C2}$ (les collecteurs sont reliés). $I_{C1}=\beta_1I_B$ et $I_{B2}=I_{E1}=I_B+I_{C1}=(\beta_1+1)I_B$. $I_{C2}=\beta_2I_{B2}=\beta_2(\beta_1+1)I_B$. Donc $I_C=\beta_1I_B+\beta_2(\beta_1+1)I_B\approx\beta_1\beta_2I_B$ car $\beta_1\beta_2$ est très grand devant $\beta_1$ et $\beta_2$. Gain exact : $\beta_1+\beta_2+\beta_1\beta_2$.", src=F25 + ", ex. 3", duree=5),
    ]},
    {"n": 12, "titre": "Transistors MOS : blocage et conduction", "notions": ["mos"], "exos": [
        v("o121", r"Inverseur CMOS (figure), $V_{CC}=5$ V, entrée $V_{IN}=0$ V. Tension $V_{GS}$ du MOSP (en V) ?", "0-5", "-5",
          r"$V_{GS_P}=V_G-V_S=V_{IN}-V_{CC}=0-5=-5$ V : le MOSP est conducteur.", src=COURS_MOS + ", II.3.a", duree=2),
        v("o122", r"Inverseur CMOS (figure), $V_{CC}=5$ V, entrée $V_{IN}=5$ V. Tension $V_{GS}$ du MOSN (en V) ?", "5-0", "5",
          r"La source du MOSN est à la masse : $V_{GS_N}=5-0=5$ V : le MOSN est conducteur (et le MOSP, $V_{GS_P}=0$, est bloqué).", src=COURS_MOS + ", II.3.a", duree=2),
        v("o123", r"Inverseur CMOS (figure), $V_{CC}=5$ V, $V_{IN}=5$ V. Tension de sortie $V_{OUT}$ (en V) ?", "5*(1-5/5)", "0",
          r"MOSN conducteur et MOSP bloqué : la sortie est reliée à la masse, $V_{OUT}=0$ V.", src=COURS_MOS + ", II.3.a", duree=2),
        v("o124", r"Combien de transistors conduisent dans l'inverseur CMOS, quelle que soit l'entrée ?", "1", "1",
          r"Les deux étages sont complémentaires : l'un conduit, l'autre est bloqué. Un seul transistor conduit (d'où une consommation statique quasi nulle).", src=COURS_MOS + ", II.3", duree=2),
        o("o125", r"Rappeler, pour un MOSN et pour un MOSP, la condition de blocage et la condition de conduction (tensions $V_{GS}$ du cours, alimentation $5$ V). Quel est l'équivalent drain-source dans chaque cas ?",
          r"MOSN : bloqué si $V_{GS}=0$ V, conducteur si $V_{GS}=5$ V. MOSP : bloqué si $V_{GS}=0$ V, conducteur si $V_{GS}=-5$ V. Un transistor bloqué est un interrupteur ouvert entre drain et source, un transistor conducteur un interrupteur fermé. Le courant de grille est nul (grille isolée par l'oxyde).", src=COURS_MOS + ", II.1", duree=3),
        o("o126", r"Comparer les technologies TTL et CMOS (transistors, commande, consommation, rapidité).",
          r"TTL : transistors bipolaires, commandés en courant (faible impédance d'entrée), gourmandes en énergie, rapides. CMOS : MOSFET complémentaires, commandés en tension (impédance d'entrée infinie), très faible consommation, un peu plus lentes (mais suffisantes dans la plupart des cas). Les temps de commutation non nuls sont à l'origine des temps de propagation.", src=COURS_MOS + ", II.2", duree=3),
    ]},
    {"n": 13, "titre": "Portes CMOS : inverseur, NAND, NOR", "notions": ["cmos", "mos"], "exos": [
        v("n131", r"Porte NAND CMOS (figure), $V_{CC}=5$ V. Entrées $a=5$ V, $b=5$ V. $V_{OUT}$ (en V) ?", "5*(1-1*1)", "0",
          r"Les deux MOSN en série conduisent ($V_{GS}=5$ V), les deux MOSP en parallèle sont bloqués : la sortie est à la masse, $V_{OUT}=0$. C'est $\overline{a\cdot b}=\overline1=0$.", src=COURS_MOS + ", II.3.b", duree=2),
        v("n132", r"Porte NAND CMOS (figure), $V_{CC}=5$ V, $a=0$ V, $b=5$ V. $V_{OUT}$ (en V) ?", "5*(1-0*1)", "5",
          r"Le MOSP de grille $a=0$ conduit : la sortie est reliée à $V_{CC}$ (le MOSN en série avec $a$ est bloqué). $V_{OUT}=5$ V.", src=COURS_MOS + ", II.3.b", duree=2),
        v("n133", r"Porte NOR CMOS (figure : MOSP en série, MOSN en parallèle). $a=0$ V, $b=0$ V. $V_{OUT}$ (en V) ?", "5*(1-(0+0-0*0))", "5",
          r"Les deux MOSP en série conduisent (grilles à $0$), les MOSN sont bloqués : $V_{OUT}=V_{CC}=5$ V. C'est $\overline{a+b}=\overline0=1$.", src=COURS_MOS + ", II.3.c", duree=2),
        v("n134", r"Porte NOR CMOS (figure : MOSP en série, MOSN en parallèle), $V_{CC}=5$ V, $a=5$ V, $b=0$ V. $V_{OUT}$ (en V) ?", "5*(1-(1+0-1*0))", "0",
          r"Le MOSN de grille $a=5$ V conduit : la sortie est à la masse. La branche MOSP en série est coupée par le MOSP de grille $a$ bloqué. $V_{OUT}=0$.", src=COURS_MOS + ", II.3.c", duree=2),
        v("n135", r"Combien de transistors comporte une porte NAND CMOS à $3$ entrées ?", "2*3", "6",
          r"Chaque entrée commande un MOSP et un MOSN : $2\times3=6$ transistors (3 MOSP en parallèle, 3 MOSN en série).", src=COURS_MOS + ", II.3.b", duree=2),
        o("n136", r"Montrer que le montage de la figure est une NAND : déterminer la tension de sortie pour chaque combinaison des entrées, puis l'équation logique.",
          r"Les étages sont complémentaires (MOSP en parallèle, MOSN en série) : il suffit d'étudier l'étage MOSP. La sortie est reliée à $V_{CC}$ si $P_A$ ou $P_B$ conduit, c'est-à-dire si $V_{GS}=V_a-5=-5$ V (soit $a=0$) ou $V_b=0$. Donc $S=\overline a+\overline b=\overline{a\cdot b}$ (de Morgan) : c'est une NAND. Table : $S=0$ seulement pour $a=b=1$.", src=COURS_MOS + ", II.3.b", duree=5),
        o("n137", r"Montrer que le montage de la figure (MOSP en série, MOSN en parallèle) est une NOR : déterminer la tension de sortie pour chaque combinaison des entrées, puis l'équation logique.",
          r"Les MOSP en série conduisent si les deux grilles sont à $0$ : $S=\overline a\cdot\overline b=\overline{a+b}$ (de Morgan). Si $a=1$ ou $b=1$, un MOSN conduit et un MOSP est bloqué : $S=0$. C'est une NOR.", src=COURS_MOS + ", II.3.c", duree=5),
    ]},
    {"n": 14, "titre": "Fonctions CMOS composées et étage complémentaire", "notions": ["cmos"], "exos": [
        v("n141", r"Porte CMOS de la figure (TD, exercice 1). $V_{CC}=5$ V. Entrées $x=5$ V, $y=5$ V, $z=0$ V. $V_{OUT}$ (en V) ?", "5*(1-(1+0-1*0)*1)", "0",
          r"Étage MOSN : ($x$ // $z$) en série avec $y$. $x=1$ : la branche parallèle conduit ; $y=1$ conduit : le MOSN est passant, la sortie est à la masse. $V_{OUT}=0$ ($S=\overline{(x+z)y}=\overline1=0$).", src=TDC + ", ex. 1", duree=3),
        v("n142", r"Porte CMOS de la figure, $V_{CC}=5$ V, $x=0$, $y=5$ V, $z=0$. $V_{OUT}$ (en V) ?", "5*(1-(0+0-0*0)*1)", "5",
          r"$x=z=0$ : la branche parallèle des MOSN est bloquée, le MOSN n'est pas passant. Côté MOSP, $x$ et $z$ à $0$ sont conducteurs en série : la sortie est à $V_{CC}$. $V_{OUT}=5$ V.", src=TDC + ", ex. 1", duree=3),
        v("n143", r"Équation de cette porte : contrôler que $S=\overline x\,\overline z+\overline y$ est égale à $\overline{(x+z)\,y}$ (on note $A=x$, $B=y$, $C=z$). Contrôle (1 = égales) ?", "eqv(Not((A|C)&B), (~A&~C)|~B)", "1",
          r"Côté MOSP : la branche ($x$ en série avec $z$) conduit si $x=0$ et $z=0$, la branche $y$ si $y=0$. $S=\overline x\,\overline z+\overline y$. Par De Morgan, $\overline{(x+z)\,y}=\overline{x+z}+\overline y=\overline x\,\overline z+\overline y$ : les deux expressions sont égales.", src=TDC + ", ex. 1", duree=4),
        v("n144", r"Pour la porte CMOS de la figure ($V_{CC}=5$ V), pour combien de combinaisons des trois entrées la sortie est-elle à $5$ V ?", "4+1", "5",
          r"$S=\overline x\,\overline z+\overline y$ vaut $1$ si $y=0$ (4 combinaisons de $x,z$) ou si $y=1$ et $x=z=0$ (1 combinaison) : $4+1=5$ combinaisons sur $8$.", src=TDC + ", ex. 1", duree=3),
        o("n145", r"Le montage de la figure est une fonction CMOS dont l'étage MOSN est à déterminer. Donner l'équation logique, puis redessiner le schéma complet.",
          r"Étage MOSP : branche ($a$ en série avec $b$) en parallèle avec $c$. Il conduit si ($a=0$ et $b=0$) ou $c=0$ : $S=\overline a\,\overline b+\overline c=\overline{(a+b)\,c}$. L'étage MOSN est le dual (série $\leftrightarrow$ parallèle) : $a$ en parallèle avec $b$, le tout en série avec $c$." "" "\n\n" + FIG_ETAGEN_SOL, src=TDC + ", ex. 2", duree=8),
        o("n146", r"Bonus du TD : donner le schéma d'un OU exclusif en technologie CMOS.",
          r"$a\oplus b=\overline{ab+\overline a\,\overline b}$. On génère $\overline a$ et $\overline b$ avec deux inverseurs CMOS, puis on réalise la fonction $S=\overline{ab+\overline a\,\overline b}$. MOSN : ($a$ série $b$) en parallèle avec ($\overline a$ série $\overline b$). MOSP, dual : ($a$ // $b$) en série avec ($\overline a$ // $\overline b$)." "" "\n\n" + FIG_XOR, src=TDC + ", ex. 4", duree=8),
        v("n147", r"Contrôler que $S=\overline{ab+\overline a\,\overline b}$ est le OU exclusif $a\oplus b$ (contrôle, 1 = égal) ?", "eqv(Xor(A,B), ~((A&B)|(~A&~B)))", "1",
          r"$ab+\overline a\,\overline b$ est l'égalité (XNOR) ; son complément est le OU exclusif : $S=a\oplus b$ (vaut $1$ quand $a\neq b$).", src=TDC + ", ex. 4", duree=3),
    ]},
    {"n": 15, "titre": "Niveau examen : transistors bipolaires, mars 2026", "notions": ["pol_re", "pol_pont", "ampli", "modes"], "examen": True, "exos": [
        {"id": "mx1", "kind": "multi", "src": f"{X26}, ex. 1 (10 points)",
         "enonce": r"Amplificateur de la figure ($C_1$, $C_2$ : condensateurs de liaison) : $R_B=150$ kΩ, $R_C=1$ kΩ, $R_E=1$ kΩ, $V_{CC}=10$ V, $V_{BE}=0{,}7$ V, $\beta=150$." "\n"
                   r"A. Polarisation. 1. Dessiner le schéma de polarisation. 2. Déterminer $I_B$ (en \mu A), $I_C$ (en mA) et $V_{CE}$ (en V), transistor linéaire, $1+\beta\approx\beta$." "\n"
                   r"B. Petits signaux. 3. Schéma équivalent petits signaux, puis expression littérale de $A_v$ ($\beta+1\approx\beta$, résistance de sortie du transistor négligée).",
         "parts": ["x11", "e61", "e62", "e63", "a106"]},
        {"id": "mx2", "kind": "multi", "src": f"{X26}, ex. 2 (4 points + 1 bonus)",
         "enonce": r"Montage de la figure (collecteur à $V_{CC}=15$ V) : $R_1=10$ kΩ, $R_2=5$ kΩ, $R_E=1000$ Ω, $\beta=200$, $V_{BE}=0{,}6$ V." "\n"
                   r"1. Courant de saturation $I_{C,sat}$ (en mA). 2. On suppose $\beta+1\approx\beta$ et $I_B$ négligeable devant les courants de $R_1$ et $R_2$ : courant $I_E$ (en mA). Bonus : pourquoi le transistor est-il linéaire ? 3. $I_B$ (en \mu A) puis $V_{CE}$ (en V).",
         "parts": ["q71", "q72", "q75", "q73", "q74"]},
        {"id": "mx3", "kind": "multi", "src": f"{X26}, ex. 3 (6 points)",
         "enonce": r"QCM. Q1 : en mode linéaire, la jonction base-émetteur est (bloquée / passante) ? Q2 : bloqué et saturé servent à concevoir (portes logiques / filtres / amplificateurs / ponts diviseurs) ? Q3 : saturé, équivalent $C$-$E$ (diode / résistance / interrupteur ouvert / fil) ? Q4 : saturé, les deux jonctions sont bloquées (vrai / faux) ? Q5 : bloqué, équivalent $C$-$E$ ? Q6 : le mode linéaire sert surtout aux portes logiques (vrai / faux) ? Q7 et Q8 : $\beta=200$, $I_C=100$ mA, linéaire : $I_B$ et $I_E$ ? Q9 : montage à réaction de collecteur, quelle loi des mailles ?",
         "parts": ["x31", "m31", "m32", "e68"]},
    ]},
    {"n": 16, "titre": "Plus dur que l'examen (+20 %) : bipolaire", "notions": ["pol_pont", "pol_re", "ampli", "commut"], "examen": True, "exos": [
        {"id": "hx1", "kind": "multi", "src": "Exercice d'entraînement, difficulté examen + 20 % (non tiré d'une annale)",
         "enonce": r"Étage à pont de résistances (figure) : $V_{CC}=12$ V, $R_1=9$ kΩ (vers $V_{CC}$), $R_2=4{,}5$ kΩ (vers la masse), $R_C=0{,}5$ kΩ, $R_E=0{,}3$ kΩ découplée par $C_E$, charge $R_u=0{,}5$ kΩ, $\beta=100$ ($\beta+1\approx\beta$), $V_{BE}=0{,}7$ V, $m=2$, $V_T=26$ mV." "\n"
                   r"1. $I_B$ (en \mu A) avec le générateur de Thévenin vu par la base. 2. $V_{CE}$ (en V). 3. $I_{C,sat}$ (en mA) : le transistor est-il linéaire ? 4. $r$ (en Ω). 5. $A_v$ (condensateur $C_E$ en place). 6. Résistance d'entrée $R_i=R_{th}\parallel r$ (en kΩ). 7. $A_v$ si l'on retire $C_E$.",
         "parts": ["h11", "h12", "h13", "h14", "h15", "h16", "h17"]},
        {"id": "hx2", "kind": "multi", "src": "Exercice d'entraînement, difficulté examen + 20 % (non tiré d'une annale)",
         "enonce": r"Montage à réaction de collecteur (figure) : $V_{CC}=10{,}7$ V, $R_C=2$ kΩ, $R_B=198$ kΩ, $\beta=100$, $V_{BE}=0{,}7$ V." "\n"
                   r"1. $I_B$ (en \mu A). 2. $V_{CE}$ (en V). 3. Quelle valeur de $R_B$ (en kΩ) donne $V_{CE}=5{,}7$ V ? 4. Ce montage peut-il saturer ? 5. Le transistor est remplacé par un autre de gain $\beta=200$ : nouveau $I_C$ (en mA).",
         "parts": ["r1", "r2", "r3", "r4", "r5"]},
        {"id": "hx3", "kind": "multi", "src": "Exercice d'entraînement, difficulté examen + 20 % (non tiré d'une annale)",
         "enonce": r"Un transistor commande une charge $R_C=240$ Ω sous $V_{CC}=12$ V (figure). L'entrée $V_1$ vaut $0$ ou $5$ V ; $\beta=100$, $V_{BE}=0{,}7$ V." "\n"
                   r"1. $I_{C,sat}$ (en mA). 2. Courant de base minimal pour saturer (en \mu A). 3. $R_B$ maximale (en kΩ). 4. On choisit $R_B=4{,}3$ kΩ : courant de base (en mA). 5. Quelle est la fonction réalisée et que vaut $V_S$ pour $V_1=0$ ?",
         "parts": ["t1", "t2", "t3", "t4", "t5"]},
    ]},
    {"n": 17, "titre": "Plus dur que l'examen (+20 %) : portes CMOS", "notions": ["cmos", "mos"], "examen": True, "exos": [
        {"id": "ix1", "kind": "multi", "src": "Exercice d'entraînement, difficulté examen + 20 % (style TD CMOS, non tiré d'une annale)",
         "enonce": r"Porte CMOS à quatre entrées (figure) : MOSP : ($a$ // $b$) en série avec ($c$ // $d$) ; MOSN : ($a$ série $b$) // ($c$ série $d$) ; $V_{CC}=5$ V." "\n"
                   r"1. $V_{OUT}$ pour $a=b=5$ V, $c=0$, $d=5$ V. 2. Pour combien de combinaisons des entrées la sortie est-elle à $5$ V ? 3. Contrôler que $S=\overline{ab+cd}=(\overline a+\overline b)(\overline c+\overline d)$. 4. Nombre de transistors. 5. Pourquoi les deux étages ne conduisent-ils jamais ensemble ?",
         "parts": ["i11", "i12", "i13", "i14", "i15"]},
        {"id": "ix2", "kind": "multi", "src": "Exercice d'entraînement, difficulté examen + 20 % (style TD CMOS, non tiré d'une annale)",
         "enonce": r"OU exclusif en CMOS : $V_{CC}=5$ V. 1. Donner le schéma complet. 2. Nombre total de transistors avec les deux inverseurs. 3. $V_{OUT}$ (en V) pour $a=5$ V, $b=0$. 4. Contrôler que $S=\overline{ab+\overline a\,\overline b}=a\oplus b$.",
         "parts": ["n146", "i22", "i23", "n147"]},
        {"id": "ix3", "kind": "multi", "src": "Exercice d'entraînement, difficulté examen + 20 % (style TD CMOS, non tiré d'une annale)",
         "enonce": r"L'étage MOSP de la figure ($a$ série $b$, en parallèle avec $c$) est donné, l'étage MOSN est à déterminer." "\n"
                   r"1. Équation de la fonction et schéma complet. 2. Pour combien de combinaisons $(a,b,c)$ la sortie est-elle à $5$ V ? 3. $V_{OUT}$ (en V) pour $a=5$ V, $b=0$, $c=5$ V.",
         "parts": ["n145", "i31", "i32"]},
    ]},
    {"n": 18, "titre": "Annales S3 d'électronique : polarisation, saturation, amplificateur", "notions": ["pol_rb", "pol_re", "pol_pont", "mode_test", "darlington", "ampli"], "examen": True, "exos": [
        {"id": "fx1", "kind": "multi", "src": f"{F20}, ex. 3 (6 points) et ex. 4 (2 points)",
         "enonce": r"Exercice 3. $R_B=200$ kΩ, $R_C=500$ Ω, $R_E=1$ kΩ, $V_{CC}=10$ V, $\beta=100$, $V_{BE}=0{,}7$ V, $\beta+1\approx\beta$ pour les applications numériques. Transistor linéaire : $I_B$ (\mu A), $I_C$ (mA), $V_{CE}$ (V) ; hypothèse vérifiée ? Puis $I_{C,sat}$ (mA)." "\n"
                   r"Exercice 4 (Darlington, figure ci-dessous) : gain en courant du transistor équivalent en fonction de $\beta_1$ et $\beta_2$ ?" "" "\n\n" + FIG_DARL,
         "parts": ["f201", "f202", "f203", "f204", "d112"]},
        {"id": "fx2", "kind": "multi", "src": f"{F21}, ex. 3 (4 points) et ex. 4 (5 points + 1)",
         "enonce": r"Exercice 3. $R_C=4$ kΩ, $R_E=1$ kΩ, $V_{CC}=10$ V, $\beta=100$, $V_{BE}=0{,}6$ V. 1. $I_{C,sat}$ (mA). 2. Valeur minimale de $R_B$ (kΩ) pour un fonctionnement linéaire ($\beta+1\approx\beta$ ; le corrigé garde $\beta+1=101$)." "\n"
                   r"Exercice 4 (réaction de collecteur, figure ci-dessous). Point de polarisation en expressions littérales ($I_B$, $I_C$, $I_E$, $V_{BE}$, $V_{BC}$, $V_{CE}$), puis : le transistor peut-il saturer ?" "" "\n\n" + FIG_FB,
         "parts": ["f211", "f212", "f213", "e68"]},
        {"id": "fx3", "kind": "multi", "src": f"{F22}, ex. 3 (3 points) et ex. 4 (4,5 points)",
         "enonce": r"Exercice 3. $R_C=60$ Ω, $V_{CC}=12$ V, $\beta=100$, $V_{BE}=0{,}7$ V. 1. $R_B$ (kΩ) pour $I_C=100$ mA. 2. $I_{C,sat}$ (mA). 3. $R_B$ minimale (kΩ) pour saturer." "\n"
                   r"Exercice 4 (pont de résistances, figure ci-dessous) : $R_1=20$ kΩ, $R_2=4$ kΩ, $R_C=1{,}2$ kΩ, $R_E=80$ Ω, $V_{CC}=12$ V, $\beta=100$, $V_{BE}=0{,}7$ V. Point de polarisation en expressions littérales (Thévenin), puis $V_{CE}$ numérique (en V) et conclusion." "" "\n\n" + FIG_PONT_C,
         "parts": ["f221", "f222", "f223", "f224", "f225"]},
        {"id": "fx4", "kind": "multi", "src": f"{F25}, ex. 2 (6 points), ex. 3 (3 points) et ex. 4 Q9-Q10",
         "enonce": r"Exercice 2. $R_C=1$ kΩ, $R_E=1$ kΩ, $V_{CC}=10$ V, $\beta=150$, $V_{BE}=0{,}7$ V, on veut $I_C=4{,}65$ mA. 1a. $V_{CE}$ (V) (transistor linéaire, $\beta\gg1$) ; hypothèse bien vérifiée ? 1b. $R_B$ (kΩ) ($\beta+1\approx\beta$). 2. $R_B$ minimale (kΩ) pour rester linéaire." "\n"
                   r"Exercice 3 (Darlington, figure ci-dessous) : gain du transistor équivalent ?" "\n\n" + FIG_DARL + "\n\n"
                   r"Exercice 4, QCM Q9-Q10 (polarisation par résistance de base, figure ci-dessous, $I_C=20$ mA, $V_{CE}=5$ V, $\beta=100$, $V_{BE}=0{,}7$ V, $E=10$ V) : $V_{BC}$ (V) puis $R_C$ (Ω) ?" "\n\n" + FIG_RB,
         "parts": ["f251", "e64", "e65", "d115", "f254", "f255"]},
        {"id": "fx5", "kind": "multi", "src": f"{F24}, ex. 3 (4,5 points) et ex. 4 Q5-Q6",
         "enonce": r"Exercice 3. $R_C=50$ Ω, $V_{CC}=15$ V, $\beta=200$, $V_{BE}=0{,}7$ V. 1. $R_B$ (kΩ) pour $I_C=100$ mA. 2. $I_{C,sat}$ (mA). 3. $R_B$ minimale (kΩ) pour ne pas saturer." "\n"
                   r"Exercice 4, QCM Q5-Q6 (montage $R_B$, $R_C$, $R_E$ ci-dessous, $V_{CC}=15$ V, $\beta=200$) : le point de polarisation est caractérisé par $V_E=2$ V, $V_C=5$ V, $I_B=100$ \mu A. Q5 : $V_{CE}$ (V) et mode ? Q6 : $R_C$ (en Ω) ?" "" "\n\n" + FIG_RE,
         "parts": ["p54", "p55", "p56", "f241", "f242"]},
        {"id": "fx6", "kind": "multi", "src": f"{F18}, ex. 3 (3 points) et ex. 4 (7 points)",
         "enonce": r"Exercice 3. $R_C=4$ kΩ, $V_{CC}=10$ V, $\beta=100$, $V_{BE}=0{,}6$ V. 1. $I_{C,sat}$ (mA). 2. $R_B$ minimale (kΩ) pour rester linéaire." "\n"
                   r"Exercice 4 (amplificateur, figure ci-dessous) : $R_B=200$ kΩ, $R_C=1$ kΩ, $R_E=1$ kΩ, $R_u=10$ kΩ, $V_{CC}=10$ V, $\beta=100$, $V_{BE}=0{,}7$ V, $\beta+1\approx\beta$. Point de polarisation : $I_B$ (\mu A), $I_C$ (mA), $V_{CE}$ (V). Petits signaux : expression de $A_v$." "\n\n" + FIG_AMP,
         "parts": ["f261", "f262", "f263", "f264", "f265", "a106"]},
    ]},
]

EXTRA_PARTS = [
    o("x11", r"Dessiner le schéma de polarisation de l'amplificateur.",
      r"En continu, les condensateurs de liaison $C_1$ et $C_2$ sont des interrupteurs ouverts : le générateur $v_g$ avec $R_g$ et la charge $R_u$ disparaissent. Il reste $R_B$ entre $V_{CC}$ et la base, $R_C$ entre $V_{CC}$ et le collecteur, $R_E$ entre l'émetteur et la masse, avec $I_B$, $I_C$, $I_E$, $V_{BE}$, $V_{CE}$." "\n\n" + FIG_RE, src=X26 + ", ex. 1 A.1", duree=4),
    o("x31", r"QCM (Q1 à Q6).",
      r"Q1 : passante. Q2 : des portes logiques (bloqué et saturé). Q3 : un fil ($V_{CE}=0$). Q4 : faux (saturé : les deux jonctions sont passantes). Q5 : un interrupteur ouvert. Q6 : faux (le linéaire sert aux amplificateurs). Q7 : $0{,}5$ mA. Q8 : $100{,}5$ mA. Q9 : $V_{CC}=(\beta+1)R_CI_B+R_BI_B+V_{BE}$.", src=X26 + ", ex. 3 Q1 à Q6", duree=5),
    v("h11", r"Étage à pont ($V_{CC}=12$ V, $R_1=9$ kΩ, $R_2=4{,}5$ kΩ, $R_E=0{,}3$ kΩ, $\beta=100$, $\beta+1\approx\beta$, $V_{BE}=0{,}7$ V). $I_B$ (en µA) ?", "(4-0.7)/(3+100*0.3)*1000", "100",
      r"$E_{th}=\dfrac{4{,}5}{13{,}5}\times12=4$ V, $R_{th}=\dfrac{9\times4{,}5}{13{,}5}=3$ kΩ. $I_B=\dfrac{E_{th}-V_{BE}}{R_{th}+\beta R_E}=\dfrac{3{,}3}{3+30}=0{,}1$ mA $=100$ µA.", src="Exercice d'entraînement", duree=6),
    v("h12", r"Mêmes données, $R_C=0{,}5$ kΩ. $V_{CE}$ (en V) ?", "12-(0.5+0.3)*100*(4-0.7)/(3+100*0.3)", "4",
      r"$I_C=\beta I_B=10$ mA, $I_E\approx I_C$ : $V_{CE}=V_{CC}-(R_C+R_E)I_C=12-0{,}8\times10=4$ V.", src="Exercice d'entraînement", duree=3),
    v("h13", r"Mêmes données. $I_{C,sat}$ (en mA) ? Le transistor est-il linéaire ?", "12/(0.5+0.3)", "15",
      r"$I_{C,sat}=\dfrac{V_{CC}}{R_C+R_E}=\dfrac{12}{0{,}8}=15$ mA. $I_C=10 < 15$ mA : linéaire (cohérent avec $V_{CE}=4$ V $> 0$).", src="Exercice d'entraînement", duree=3),
    v("h14", r"$I_{B0}=100$ \mu A, $m=2$, $V_T=26$ mV. Résistance $r$ (en Ω) ?", "2*26/Rational(100,1000)", "520",
      r"$r=\dfrac{mV_T}{I_{B0}}=\dfrac{52\text{ mV}}{0{,}1\text{ mA}}=520$ Ω.", src="Exercice d'entraînement", duree=2),
    v("h15", r"$C_E$ en place ($R_E$ court-circuitée en variable), $\beta=100$, $R_C=R_u=0{,}5$ kΩ, $r=0{,}52$ kΩ. $A_v$ ?", "-100*(0.5*0.5/(0.5+0.5))/0.52", "-625/13",
      r"$A_v=-\beta\dfrac{R_C\parallel R_u}{r}=-100\times\dfrac{0{,}25}{0{,}52}=-\dfrac{625}{13}\approx-48{,}1$.", src="Exercice d'entraînement", duree=4),
    v("h16", r"Résistance d'entrée $R_i=R_{th}\parallel r$ avec $R_{th}=3$ kΩ et $r=0{,}52$ kΩ (en kΩ, valeur exacte) ?", "3*0.52/(3+0.52)", "39/88",
      r"$R_i=\dfrac{3\times0{,}52}{3{,}52}=\dfrac{39}{88}\approx0{,}44$ kΩ (le pont $R_1\parallel R_2$ est en parallèle avec $r$ après annulation de $V_{CC}$).", src="Exercice d'entraînement", duree=4),
    v("h17", r"On retire $C_E$ : $R_E=0{,}3$ kΩ reste en variable. $\beta=100$ ($\beta+1\approx\beta$), $R_C\parallel R_u=0{,}25$ kΩ, $r=0{,}52$ kΩ. $A_v$ ?", "-100*0.25/(0.52+100*0.3)", "-625/763",
      r"$A_v=-\beta\dfrac{R_C\parallel R_u}{r+\beta R_E}=-\dfrac{25}{0{,}52+30}=-\dfrac{625}{763}\approx-0{,}82$ : le gain est presque détruit sans le découplage.", src="Exercice d'entraînement", duree=4),
    v("r1", r"Réaction de collecteur : $V_{CC}=10{,}7$ V, $R_C=2$ kΩ, $R_B=198$ kΩ, $\beta=100$, $V_{BE}=0{,}7$ V. $I_B$ (en µA) ?", "(10.7-0.7)/(198+(100+1)*2)*1000", "25",
      r"$V_{CC}=R_C(\beta+1)I_B+R_BI_B+V_{BE}$ donc $I_B=\dfrac{10}{198+202}=25$ µA.", src="Exercice d'entraînement", duree=3),
    v("r2", r"Mêmes données. $V_{CE}$ (en V) ?", "10.7-2*(100+1)*(10.7-0.7)/(198+(100+1)*2)", "5.65",
      r"$V_{CE}=V_{CC}-R_C(\beta+1)I_B=10{,}7-2\times101\times0{,}025=5{,}65$ V.", src="Exercice d'entraînement", duree=3),
    v("r3", r"On veut $V_{CE}=5{,}7$ V. Valeur de $R_B$ (en kΩ) ?", "(5.7-0.7)/((10.7-5.7)/(2*(100+1)))", "202",
      r"$V_{CC}-V_{CE}=R_C(\beta+1)I_B$ donne $I_B=\dfrac{5}{202}$ mA. $V_{CE}=V_{BE}+R_BI_B$ donne $R_B=\dfrac{5}{5/202}=202$ kΩ.", src="Exercice d'entraînement", duree=5),
    o("r4", r"Ce montage peut-il saturer ?",
      r"$V_{CE}=V_{BE}+R_BI_B > V_{BE}=0{,}7$ V pour $I_B > 0$ : $V_{CE}$ ne peut pas atteindre $0$. Le transistor reste linéaire (ou bloqué si $I_B=0$) : la jonction base-collecteur reste bloquée.", src="Exercice d'entraînement", duree=3),
    v("r5", r"Avec un transistor de gain $\beta=200$ (autres données identiques), $I_C$ (en mA, valeur exacte) ?", "200*(10.7-0.7)/(198+(200+1)*2)", "10/3",
      r"$I_B=\dfrac{10}{198+402}=\dfrac{1}{60}$ mA, $I_C=200\times\dfrac1{60}=\dfrac{10}{3}\approx3{,}33$ mA contre $2{,}5$ mA : un gain doublé n'augmente $I_C$ que de $33$ % (stabilisation par la réaction).", src="Exercice d'entraînement", duree=4),
    v("t1", r"Charge $R_C=240$ Ω sous $V_{CC}=12$ V. $I_{C,sat}$ (en mA) ?", "12/0.24", "50",
      r"$V_{CE}=0$ : $I_{C,sat}=\dfrac{12}{0{,}24}=50$ mA.", src="Exercice d'entraînement", duree=2),
    v("t2", r"$\beta=100$. Courant de base minimal pour saturer (en µA) ?", "12/0.24/100*1000", "500",
      r"$I_B\geq\dfrac{I_{C,sat}}{\beta}=0{,}5$ mA $=500$ µA.", src="Exercice d'entraînement", duree=2),
    v("t3", r"$V_1=5$ V, $V_{BE}=0{,}7$ V. $R_B$ maximale (en kΩ) pour saturer ?", "(5-0.7)/0.5", "8.6",
      r"$R_B\leq\dfrac{V_1-V_{BE}}{I_{B,min}}=\dfrac{4{,}3}{0{,}5}=8{,}6$ kΩ.", src="Exercice d'entraînement", duree=3),
    v("t4", r"On choisit $R_B=4{,}3$ kΩ. Courant de base $I_B$ (en mA) ?", "(5-0.7)/4.3", "1",
      r"$I_B=\dfrac{4{,}3}{4{,}3}=1$ mA, soit deux fois le minimum : la saturation est assurée avec marge.", src="Exercice d'entraînement", duree=2),
    o("t5", r"Quelle fonction réalise le montage et que vaut $V_S$ pour $V_1=0$ ?",
      r"Un inverseur (NON). $V_1=0$ : $I_B=0$, bloqué, $V_S=V_{CC}=12$ V. $V_1=5$ V : saturé, $V_S=0$.", src="Exercice d'entraînement", duree=2),
    v("i11", r"Porte à quatre entrées de la figure ($V_{CC}=5$ V). $a=b=5$ V, $c=0$ V, $d=5$ V. $V_{OUT}$ (en V) ?", "5*(1-(1*1+0*1-1*1*0*1))", "0",
      r"Branche MOSN ($a$ série $b$) : $a=b=1$ conduit : la sortie est à la masse. $S=\overline{ab+cd}=\overline{1}=0$.", src="Exercice d'entraînement", duree=3),
    v("i12", r"Même porte. Pour combien de combinaisons des quatre entrées la sortie est-elle à $5$ V ?", "3*3", "9",
      r"$S=1$ si $ab=0$ et $cd=0$ : $3$ combinaisons de $(a,b)$ ne donnent pas $ab=1$, et $3$ de $(c,d)$ : $3\times3=9$ sur $16$.", src="Exercice d'entraînement", duree=3),
    v("i13", r"Contrôler que $S=\overline{ab+cd}=(\overline a+\overline b)(\overline c+\overline d)$ (contrôle, 1 = égal, $A=a$, $B=b$, $C=c$, $D=d$) ?", "eqv(Not((A&B)|(C&D)), (~A|~B)&(~C|~D))", "1",
      r"De Morgan : $\overline{ab+cd}=\overline{ab}\cdot\overline{cd}=(\overline a+\overline b)(\overline c+\overline d)$. C'est aussi l'équation de l'étage MOSP ($a$ // $b$) série ($c$ // $d$).", src="Exercice d'entraînement", duree=4),
    v("i14", r"Nombre de transistors de la porte ?", "2*4", "8",
      r"$4$ MOSP et $4$ MOSN : $8$ transistors.", src="Exercice d'entraînement", duree=1),
    o("i15", r"Pourquoi les étages MOSP et MOSN ne conduisent-ils jamais ensemble ?",
      r"Les étages sont duaux : MOSN ($a$ série $b$) // ($c$ série $d$) conduit si $ab+cd=1$, MOSP ($a$ // $b$) série ($c$ // $d$) conduit si $(\overline a+\overline b)(\overline c+\overline d)=\overline{ab+cd}=1$. Les deux conditions sont complémentaires : exactement un étage conduit, la sortie est toujours définie (pas de court-circuit $V_{CC}$-masse).", src="Exercice d'entraînement", duree=4),
    v("i22", r"Nombre total de transistors du OU exclusif (étage de $8$ transistors plus deux inverseurs) ?", "8+2*2", "12",
      r"Étage principal : $8$ ; chaque inverseur : $2$ transistors ; total $8+2\times2=12$.", src="Exercice d'entraînement", duree=2),
    v("i23", r"$a=5$ V, $b=0$ : $V_{OUT}$ du OU exclusif (en V) ?", "5*(1-(1*0+(1-1)*(1-0)))", "5",
      r"$a\neq b$ : $ab=0$ et $\overline a\,\overline b=0$, donc $S=\overline0=1$ : $V_{OUT}=5$ V.", src="Exercice d'entraînement", duree=2),
    v("i31", r"Étage MOSP : ($a$ série $b$) // $c$. Pour combien de combinaisons $(a,b,c)$ la sortie est-elle à $5$ V ?", "4+1", "5",
      r"$S=\overline a\,\overline b+\overline c$ : $c=0$ donne $4$ combinaisons ; $c=1$ exige $a=b=0$ : $1$. Total $5$ sur $8$.", src="Exercice d'entraînement", duree=3),
    v("i32", r"Même porte, $a=5$ V, $b=0$ V, $c=5$ V. $V_{OUT}$ (en V) ?", "5*(1-(1+0-0)*1)", "0",
      r"MOSN : ($a$ // $b$) série $c$ : $a=1$ conduit, $c=1$ conduit : sortie à la masse, $V_{OUT}=0$.", src="Exercice d'entraînement", duree=2),
    v("f201", r"Exercice 3 (déc. 2016) : $I_B$ (en µA) ?", "(10-0.7)/(200+100*1)*1000", "31",
      r"$I_B=\dfrac{V_{CC}-V_{BE}}{R_B+(\beta+1)R_E}\approx\dfrac{9{,}3}{200+100}=31$ µA.", src=F20 + ", ex. 3 q.1", duree=4),
    v("f202", r"Même exercice : $I_C$ (en mA) ?", "100*(10-0.7)/(200+100*1)", "3.1",
      r"$I_C=\beta I_B=3{,}1$ mA ($\approx I_E$).", src=F20 + ", ex. 3 q.1", duree=2),
    v("f203", r"Même exercice : $V_{CE}$ (en V) ? Hypothèse vérifiée ?", "10-(0.5+1)*100*(10-0.7)/(200+100*1)", "5.35",
      r"$V_{CE}=V_{CC}-R_CI_C-R_EI_E=10-1{,}5\times3{,}1=5{,}35$ V $> 0$ ; $V_{BC}=V_{BE}-V_{CE}=-4{,}65$ V : le transistor est bien linéaire.", src=F20 + ", ex. 3 q.1", duree=3),
    v("f204", r"Même exercice : $I_{C,sat}$ (en mA, valeur exacte) ?", "10/(0.5+1)", "20/3",
      r"$V_{CE}=0$ et $I_E\approx I_C$ : $I_{C,sat}=\dfrac{V_{CC}}{R_C+R_E}=\dfrac{10}{1{,}5}=\dfrac{20}{3}\approx6{,}67$ mA.", src=F20 + ", ex. 3 q.2", duree=3),
    v("f211", r"Exercice 3 (déc. 2017) : $R_C=4$ kΩ, $R_E=1$ kΩ, $V_{CC}=10$ V. $I_{C,sat}$ (en mA) ?", "10/(4+1)", "2",
      r"Saturé : $V_{CE}=0$, $V_{CC}=(R_C+R_E)I_{C,sat}$, donc $I_{C,sat}=2$ mA.", src=F21 + ", ex. 3 q.1", duree=3),
    v("f212", r"Même exercice ($\beta=100$, $V_{BE}=0{,}6$ V) : $R_B$ minimale (en kΩ, avec $\beta+1=101$) ?", "100*(10-0.6)/2-(100+1)*1", "369",
      r"Linéaire si $I_B=\dfrac{V_{CC}-V_{BE}}{R_B+(\beta+1)R_E} < \dfrac{I_{C,sat}}{\beta}$, soit $R_B > \beta\dfrac{V_{CC}-V_{BE}}{I_{C,sat}}-(\beta+1)R_E=470-101=369$ kΩ (le corrigé donne $369$ kΩ).", src=F21 + ", ex. 3 q.2", duree=5),
    o("f213", r"Réaction de collecteur : donner $I_B$, $I_C$, $I_E$, $V_{BE}$, $V_{CE}$ et $V_{BC}$ en expressions littérales.",
      r"$I_E=I_B+I_C=(\beta+1)I_B$ et $V_{CC}=R_CI_E+R_BI_B+V_{BE}$ donnent $I_B=\dfrac{V_{CC}-V_{BE}}{R_B+(\beta+1)R_C}$, $I_C=\beta I_B$. $V_{CE}=V_{CC}-(\beta+1)R_CI_B$, $V_{BC}=V_{BE}-V_{CE}=-R_BI_B$.", src=F21 + ", ex. 4", duree=6),
    v("f221", r"Exercice 3 (déc. 2018) : $R_C=60$ Ω, $V_{CC}=12$ V, $\beta=100$, $V_{BE}=0{,}7$ V, $I_C=100$ mA. $R_B$ (en kΩ) ?", "100*(12-0.7)/100", "11.3",
      r"$V_{CE}=12-0{,}06\times100=6$ V $> 0$ : linéaire. $I_B=1$ mA, $R_B=\dfrac{12-0{,}7}{1}=11{,}3$ kΩ.", src=F22 + ", ex. 3 q.1", duree=4),
    v("f222", r"Même exercice : $I_{C,sat}$ (en mA) ?", "12/0.06", "200",
      r"$I_{C,sat}=\dfrac{V_{CC}}{R_C}=\dfrac{12}{0{,}06}=200$ mA (corrigé : $0{,}2$ A).", src=F22 + ", ex. 3 q.2", duree=2),
    v("f223", r"Même exercice : $R_B$ minimale pour saturer le transistor (en kΩ) ?", "100*(12-0.7)/200", "5.65",
      r"Saturation : $I_B=\dfrac{I_{C,sat}}{\beta}=2$ mA, $R_B=\dfrac{V_{CC}-V_{BE}}{2}=5{,}65$ kΩ.", src=F22 + ", ex. 3 q.3", duree=3),
    o("f224", r"Pont de résistances : simplifier le circuit par le générateur de Thévenin vu par la base et donner $I_B$, $I_C$, $I_E$, $V_{BE}$, $V_{CE}$, $V_{BC}$ en expressions littérales.",
      r"$E_{th}=\dfrac{R_2}{R_1+R_2}V_{CC}$, $R_{th}=\dfrac{R_1R_2}{R_1+R_2}$. Maille : $E_{th}=R_{th}I_B+V_{BE}+R_EI_E$ avec $I_E=(\beta+1)I_B$, donc $I_B=\dfrac{E_{th}-V_{BE}}{R_{th}+(\beta+1)R_E}$, $I_C=\beta I_B$, $I_E=(\beta+1)I_B$. $V_{CC}=R_CI_C+V_{CE}+R_EI_E$ donne $V_{CE}=V_{CC}-(\beta R_C+(\beta+1)R_E)I_B$ et $V_{BC}=V_{BE}-V_{CE}$.", src=F22 + ", ex. 4", duree=8),
    v("f225", r"Application numérique ajoutée à l'exercice 4 : $V_{CE}$ calculé sous l'hypothèse linéaire (en V, valeur exacte) ?", "12-(100*1.2+(100+1)*0.08)*(2-0.7)/(Rational(10,3)+(100+1)*0.08)", "-11079/4280",
      r"$E_{th}=\dfrac{4}{24}\times12=2$ V, $R_{th}=\dfrac{20\times4}{24}=\dfrac{10}{3}$ kΩ. $I_B=\dfrac{1{,}3}{\frac{10}3+8{,}08}\approx0{,}114$ mA, $V_{CE}=12-(120+8{,}08)\times0{,}114\approx-2{,}59$ V $< 0$ : l'hypothèse est absurde, le transistor est saturé (le sujet précisait qu'aucune application numérique n'était demandée ; ce calcul est un complément).", src=F22 + ", ex. 4 (application numérique ajoutée)", duree=8),
    v("f241", r"QCM Q5 : $V_C=5$ V et $V_E=2$ V. $V_{CE}$ (en V) ? Le transistor est linéaire si $V_{CE} > 0$.", "5-2", "3",
      r"$V_{CE}=V_C-V_E=3$ V $> 0$ : mode normal (linéaire).", src=F24 + ", ex. 4 Q5", duree=2),
    v("f242", r"QCM Q6 : $V_{CC}=15$ V, $V_C=5$ V, $I_B=100$ \mu A, $\beta=200$. $R_C$ (en Ω) ?", "(15-5)/(200*0.1)*1000", "500",
      r"$I_C=\beta I_B=20$ mA, $R_C=\dfrac{V_{CC}-V_C}{I_C}=\dfrac{10}{20}=0{,}5$ kΩ $=500$ Ω.", src=F24 + ", ex. 4 Q6", duree=3),
    v("f251", r"Exercice 2 (déc. 2021) : $I_C=4{,}65$ mA, $\beta\gg1$ ($I_E\approx I_C$). $V_{CE}$ (en V) ?", "10-(1+1)*4.65", "0.7",
      r"$V_{CE}=V_{CC}-(R_C+R_E)I_C=10-2\times4{,}65=0{,}7$ V $> 0$ : l'hypothèse linéaire est bien vérifiée.", src=F25 + ", ex. 2 q.1a", duree=3),
    v("f254", r"Q9 : $V_{BC}$ (en V) ?", "0.7-5", "-4.3",
      r"$V_{BC}=V_{BE}-V_{CE}=0{,}7-5=-4{,}3$ V (corrigé : réponse d).", src=F25 + ", ex. 4 Q9", duree=2),
    v("f255", r"Q10 : $R_C$ (en Ω) ?", "(10-5)/20*1000", "250",
      r"$V_{CC}=R_CI_C+V_{CE}$ donne $R_C=\dfrac{10-5}{20}=0{,}25$ kΩ $=250$ Ω (corrigé : réponse b).", src=F25 + ", ex. 4 Q10", duree=2),
    v("f261", r"Exercice 3 (déc. 2014, anglais) : $R_C=4$ kΩ, $V_{CC}=10$ V. $I_{C,sat}$ (en mA) ?", "10/4", "2.5",
      r"$V_{CE}=0$ : $I_{C,sat}=\dfrac{10}{4}=2{,}5$ mA.", src=F18 + ", ex. 3 q.1", duree=2),
    v("f262", r"Même exercice ($\beta=100$, $V_{BE}=0{,}6$ V) : $R_B$ minimale pour rester linéaire (en kΩ) ?", "100*(10-0.6)/(10/4)", "376",
      r"$R_B > \beta\dfrac{V_{CC}-V_{BE}}{I_{C,sat}}=100\times\dfrac{9{,}4}{2{,}5}=376$ kΩ.", src=F18 + ", ex. 3 q.2", duree=3),
    v("f263", r"Exercice 4 : $R_B=200$ kΩ, $R_C=R_E=1$ kΩ, $V_{CC}=10$ V, $\beta=100$, $V_{BE}=0{,}7$ V, $\beta+1\approx\beta$. $I_B$ (en µA) ?", "(10-0.7)/(200+100*1)*1000", "31",
      r"$I_B=\dfrac{V_{CC}-V_{BE}}{R_B+\beta R_E}=\dfrac{9{,}3}{300}=31$ µA.", src=F18 + ", ex. 4 Q1c", duree=4),
    v("f264", r"Même exercice : $I_C$ (en mA) ?", "100*(10-0.7)/(200+100*1)", "3.1",
      r"$I_C=\beta I_B=3{,}1$ mA.", src=F18 + ", ex. 4 Q1c", duree=2),
    v("f265", r"Même exercice : $V_{CE}$ (en V) ?", "10-(1+1)*3.1", "3.8",
      r"$V_{CE}=V_{CC}-(R_C+R_E)I_C=10-2\times3{,}1=3{,}8$ V $> V_{CE,sat}$ : linéaire.", src=F18 + ", ex. 4 Q1c", duree=3),
]


VARIANTS = {
    "k11": [_v(r"$E=15$ V alimente $R_1=1$ kΩ en série avec $R_2=4$ kΩ. $I$ (en mA) ?", "15/(1+4)", "3", r"$I=\dfrac{15}{5}=3$ mA.")],
    "k12": [_v(r"$E=9$ V, $R_1=1$ kΩ, $R_2=2$ kΩ. $U$ aux bornes de $R_2$ (en V) ?", "9*2/(1+2)", "6", r"$U=\dfrac23\times9=6$ V.")],
    "k13": [_v(r"$E=12$ V, $R=3$ kΩ, tension du dipôle $D$ : $3$ V. $I$ (en mA) ?", "(12-3)/3", "3", r"$I=\dfrac{12-3}{3}=3$ mA.")],
    "k14": [_v(r"$7$ mA entrent dans un nœud, $3$ mA sortent par une branche. Courant de la troisième branche (en mA) ?", "7-3", "4", r"$7=3+i$, $i=4$ mA.")],
    "j21": [_v(r"$E=10$ V, $R=1$ kΩ, diode à seuil $0{,}7$ V passante. $I$ (en mA) ?", "(10-0.7)/1", "9.3", r"$I=\dfrac{9{,}3}{1}=9{,}3$ mA.")],
    "j22": [_v(r"$E=12$ V, $R=1$ kΩ, diode en sens inverse. $I$ (en mA) ?", "0", "0", r"Diode bloquée : $I=0$.")],
    "j23": [_v(r"$E=3{,}3$ V, $R_B=10$ kΩ, $V_{BE}=0{,}7$ V. $I_B$ (en \mu A) ?", "(3.3-0.7)/10*1000", "260", r"$I_B=\dfrac{2{,}6}{10}=0{,}26$ mA $=260$ µA.")],
    "j24": [_v(r"$E=0{,}5$ V, $R_B=10$ kΩ, $V_{BE}=0{,}7$ V. $I_B$ (en \mu A) ?", "0", "0", r"$0{,}5 < 0{,}7$ V : la jonction est bloquée, $I_B=0$.")],
    "m31": [_v(r"$\beta=50$, $I_C=20$ mA, linéaire. $I_B$ (en \mu A) ?", "20/50*1000", "400", r"$I_B=\dfrac{20}{50}=0{,}4$ mA $=400$ µA.")],
    "m32": [_v(r"$\beta=100$, $I_C=50$ mA. $I_E$ (en mA) ?", "50+50/100", "50.5", r"$I_B=0{,}5$ mA, $I_E=50{,}5$ mA.")],
    "m33": [_v(r"$\alpha=0{,}98$. $\beta$ ?", "Rational(49,50)/(1-Rational(49,50))", "49", r"$\beta=\dfrac{0{,}98}{0{,}02}=49$.")],
    "m34": [_v(r"$\beta=100$, $I_B=30$ \mu A. $I_C$ (en mA) ?", "100*30/1000", "3", r"$I_C=100\times0{,}03=3$ mA.")],
    "s41": [_v(r"La base est reliée à la masse (donc à l'émetteur), $V_{CC}=12$ V. Courant $I_C$ (en mA) avec $V_{BE}=0$ ?", "0", "0", r"$V_{BE}=0$ : bloqué, $I_C=0$.")],
    "s42": [_v(r"$V_{CC}=12$ V, $R_C=60$ Ω. $I_{C,sat}$ (en mA) ?", "12/0.06", "200", r"$I_{C,sat}=\dfrac{12}{0{,}06}=200$ mA.")],
    "s43": [_v(r"$V_{CC}=12$ V, $R_B=1$ kΩ, $R_C=200$ Ω, $\beta=50$, $V_{BE}=0{,}7$ V. $V_{CE}$ sous l'hypothèse linéaire (en V) ?", "12-0.2*50*(12-0.7)/1", "-101", r"$I_B=11{,}3$ mA, $I_C=565$ mA, $V_{CE}=12-0{,}2\times565=-101$ V : saturé.")],
    "s44": [_v(r"$V_{CC}=12$ V, $R_C=60$ Ω, $\beta=100$. $I_B$ minimal pour saturer (en \mu A) ?", "12/0.06/100*1000", "2000", r"$I_{C,sat}=200$ mA, $I_B\geq\dfrac{200}{100}=2$ mA $=2000$ µA.")],
    "p51": [_v(r"$V_{CC}=12$ V, $R_B=20$ kΩ, $V_{BE}=0{,}7$ V. $I_B$ (en mA) ?", "(12-0.7)/20", "0.565", r"$I_B=\dfrac{11{,}3}{20}=0{,}565$ mA.")],
    "p52": [_v(r"$V_{CC}=12$ V, $R_B=10$ kΩ, $\beta=50$, $V_{BE}=0{,}7$ V. $I_C$ (en mA) ?", "50*(12-0.7)/10", "56.5", r"$I_B=1{,}13$ mA, $I_C=50\times1{,}13=56{,}5$ mA.")],
    "p53": [_v(r"$V_{CC}=12$ V, $R_B=20$ kΩ, $R_C=100$ Ω, $\beta=100$, $V_{BE}=0{,}7$ V. $V_{CE}$ (en V) ?", "12-0.1*100*(12-0.7)/20", "6.35", r"$I_C=56{,}5$ mA, $V_{CE}=12-0{,}1\times56{,}5=6{,}35$ V.")],
    "p54": [_v(r"$V_{CC}=12$ V, $\beta=100$, $V_{BE}=0{,}7$ V, $I_C=20$ mA. $R_B$ (en kΩ) ?", "100*(12-0.7)/20", "56.5", r"$I_B=0{,}2$ mA, $R_B=\dfrac{11{,}3}{0{,}2}=56{,}5$ kΩ.")],
    "p55": [_v(r"$V_{CC}=12$ V, $R_C=60$ Ω. $I_{C,sat}$ (en mA) ?", "12/0.06", "200", r"$\dfrac{12}{0{,}06}=200$ mA.")],
    "p56": [_v(r"$V_{CC}=12$ V, $R_C=60$ Ω, $\beta=100$, $V_{BE}=0{,}7$ V. $R_B$ minimale pour rester linéaire (en kΩ) ?", "100*(12-0.7)/200", "5.65", r"$R_B > \beta\dfrac{11{,}3}{200}=5{,}65$ kΩ.")],
    "p58": [_v(r"$V_{CC}=10$ V, $R_C=50$ Ω, point au milieu de la droite de charge. $I_C$ (en mA) ?", "(10-5)/0.05", "100", r"$I_C=\dfrac{10-5}{0{,}05}=100$ mA.")],
    "e61": [_v(r"$V_{CC}=12$ V, $R_B=100$ kΩ, $R_E=1$ kΩ, $\beta=100$, $\beta+1\approx\beta$. $I_B$ (en \mu A) ?", "(12-0.7)/(100+100*1)*1000", "56.5", r"$I_B=\dfrac{11{,}3}{100+100}=56{,}5$ µA.")],
    "e62": [_v(r"$V_{CC}=12$ V, $R_B=100$ kΩ, $R_E=1$ kΩ, $\beta=100$, $V_{BE}=0{,}7$ V, $\beta+1\approx\beta$. $I_C$ (en mA) ?", "100*(12-0.7)/(100+100*1)", "5.65", r"$I_C=100\times0{,}0565=5{,}65$ mA.")],
    "e63": [_v(r"$V_{CC}=12$ V, $R_B=100$ kΩ, $R_C=0{,}5$ kΩ, $R_E=1$ kΩ, $\beta=100$, $V_{BE}=0{,}7$ V, $\beta+1\approx\beta$. $V_{CE}$ (en V) ?", "12-(0.5+1)*100*(12-0.7)/(100+100*1)", "3.525", r"$V_{CE}=12-1{,}5\times5{,}65=3{,}525$ V.")],
    "e64": [_v(r"$V_{CC}=12$ V, $R_E=1$ kΩ, $\beta=100$, $I_C=5$ mA. $R_B$ (en kΩ, $\beta+1\approx\beta$) ?", "(12-0.7-1*5)/(5/100)", "126", r"$I_B=0{,}05$ mA, $R_B=\dfrac{12-0{,}7-5}{0{,}05}=126$ kΩ.")],
    "e65": [_v(r"$V_{CC}=12$ V, $R_C=R_E=1$ kΩ, $\beta=100$, $V_{BE}=0{,}7$ V. $R_B$ minimale (en kΩ, valeur exacte) ?", "100*(12-0.7)/(12/(1+1))-100*1", "265/3", r"$I_{C,sat}=6$ mA, $R_B > 100\times\dfrac{11{,}3}{6}-100=\dfrac{265}{3}\approx88{,}3$ kΩ.")],
    "e66": [_v(r"$V_{CC}=10{,}7$ V, $R_C=1$ kΩ, $R_B=100$ kΩ, $\beta=99$, $V_{BE}=0{,}7$ V. $I_B$ (en \mu A) ?", "(10.7-0.7)/(100+(99+1)*1)*1000", "50", r"$I_B=\dfrac{10}{100+100}=50$ µA.")],
    "e67": [_v(r"$V_{CC}=10{,}7$ V, $R_C=1$ kΩ, $R_B=100$ kΩ entre collecteur et base, $\beta=99$, $V_{BE}=0{,}7$ V, transistor linéaire. $V_{CE}$ (en V) ?", "10.7-1*(99+1)*(10.7-0.7)/(100+(99+1)*1)", "5.7", r"$V_{CE}=10{,}7-1\times100\times0{,}05=5{,}7$ V.")],
    "q71": [_v(r"$V_{CC}=12$ V, $R_E=2$ kΩ, collecteur à $V_{CC}$. $I_{C,sat}$ (en mA) ?", "12/2", "6", r"$\dfrac{12}{2}=6$ mA.")],
    "q72": [_v(r"$V_{CC}=12$ V, $R_1=20$ kΩ, $R_2=10$ kΩ, $R_E=1$ kΩ, $V_{BE}=0{,}6$ V, $I_B$ négligeable. $I_E$ (en mA) ?", "(10/(20+10)*12-0.6)/1", "3.4", r"$U_{R_2}=4$ V, $I_E=\dfrac{4-0{,}6}{1}=3{,}4$ mA.")],
    "q73": [_v(r"$V_{CC}=12$ V, $R_1=20$ kΩ, $R_2=10$ kΩ, $R_E=1$ kΩ, $V_{BE}=0{,}6$ V, $\beta=100$, $I_B$ négligeable pour $I_E$ et $\beta+1\approx\beta$, collecteur à $V_{CC}$. $I_B$ (en \mu A) ?", "3.4/100*1000", "34", r"$I_B=\dfrac{3{,}4}{100}=34$ µA.")],
    "q74": [_v(r"$V_{CC}=12$ V, $R_1=20$ kΩ, $R_2=10$ kΩ, $R_E=1$ kΩ, $V_{BE}=0{,}6$ V, $\beta=100$, $I_B$ négligeable pour $I_E$ et $\beta+1\approx\beta$, collecteur à $V_{CC}$. $V_{CE}$ (en V) ?", "12-1*3.4", "8.6", r"$V_{CE}=12-3{,}4=8{,}6$ V.")],
    "q76": [_v(r"$V_{CC}=12$ V, $R_1=20$ kΩ, $R_2=10$ kΩ, $R_E=1$ kΩ, $\beta=100$, $V_{BE}=0{,}6$ V, Thévenin avec $\beta+1$. $I_B$ (en \mu A, valeur exacte) ?", "(4-0.6)/(Rational(20,3)+(100+1)*1)*1000", "10200/323", r"$E_{th}=4$ V, $R_{th}=\frac{20}3$ kΩ : $I_B=\dfrac{3{,}4}{\frac{20}3+101}\approx31{,}6$ µA.")],
    "q77": [_v(r"$V_{CC}=12$ V, $\beta=100$, $V_C=8$ V, $I_B=50$ \mu A. $R_C$ (en Ω) ?", "(12-8)/(100*0.05)*1000", "800", r"$I_C=5$ mA, $R_C=\dfrac{4}{5}=0{,}8$ kΩ.")],
    "q78": [_v(r"$V_E=1{,}5$ V, $I_E\approx I_C=5$ mA. $R_E$ (en Ω) ?", "1.5/5*1000", "300", r"$R_E=\dfrac{1{,}5}{5}=0{,}3$ kΩ.")],
    "q79": [_v(r"$V_{CC}=12$ V, $V_E=2{,}5$ V, $V_{BE}=0{,}7$ V, $I_B=0{,}2$ mA, $0{,}8$ mA dans $R_2$. $R_1$ (en kΩ) ?", "(12-3.2)/(0.8+0.2)", "8.8", r"$V_B=3{,}2$ V, courant dans $R_1$ : $1$ mA, $R_1=8{,}8$ kΩ.")],
    "c81": [_v(r"$V_{CC}=12$ V, $R_C=2$ kΩ, entrée basse. $V_S$ (en V) ?", "12-2*0", "12", r"Bloqué : $V_S=V_{CC}=12$ V.")],
    "c82": [_v(r"$V_1=3{,}3$ V, $R_B=10$ kΩ, $V_{BE}=0{,}7$ V. $I_B$ (en mA) ?", "(3.3-0.7)/10", "0.26", r"$I_B=\dfrac{2{,}6}{10}=0{,}26$ mA.")],
    "c83": [_v(r"$\beta=50$, $V_1=5$ V, $R_B=10$ kΩ. $\beta I_B$ (en mA) ?", "50*(5-0.7)/10", "21.5", r"$I_B=0{,}43$ mA, $\beta I_B=21{,}5$ mA.")],
    "c84": [_v(r"$V_{CC}=12$ V, $R_C=2$ kΩ. $I_{C,sat}$ (en mA) ?", "12/2", "6", r"$\dfrac{12}{2}=6$ mA.")],
    "c85": [_v(r"$V_{CC}=12$ V, $R_C=2$ kΩ, saturé. $V_S$ (en V) ?", "12-2*(12/2)", "0", r"$V_S=12-2\times6=0$ V.")],
    "c86": [_v(r"$\beta=50$, $V_1=5$ V, $I_{C,sat}=5$ mA. $R_B$ maximale (en kΩ) ?", "50*(5-0.7)/5", "43", r"$R_B\leq\beta\dfrac{V_1-V_{BE}}{I_{C,sat}}=50\times\dfrac{4{,}3}{5}=43$ kΩ.")],
    "c88": [_v(r"Deux entrées à $5$ V, $R_B=5$ kΩ chacune. Courant de base total (en mA) ?", "2*(5-0.7)/5", "1.72", r"$2\times\dfrac{4{,}3}{5}=1{,}72$ mA.")],
    "g92": [_v(r"$I_{B0}=13$ \mu A. $r$ (en Ω) ?", "2*26/Rational(13,1000)", "4000", r"$r=\dfrac{52}{0{,}013}=4000$ Ω.")],
    "g93": [_v(r"$I_{B0}=20$ \mu A. $r$ (en Ω) ?", "2*26/Rational(20,1000)", "2600", r"$r=\dfrac{52}{0{,}02}=2600$ Ω.")],
    "g94": [_v(r"$|V_{EA}|=75$ V, $V_{CE0}=5$ V, $I_{C0}=2$ mA. $\rho$ (en kΩ) ?", "(75+5)/2", "40", r"$\rho=\dfrac{80}{2}=40$ kΩ.")],
    "g98": [_v(r"$I_{B0}=104$ \mu A. $r$ (en Ω) ?", "2*26/Rational(104,1000)", "500", r"$r=\dfrac{52}{0{,}104}=500$ Ω.")],
    "a101": [_v(r"$R_B=38$ kΩ, $r=2$ kΩ. $R_i$ (en kΩ) ?", "38*2/(38+2)", "1.9", r"$R_i=\dfrac{76}{40}=1{,}9$ kΩ.")],
    "a102": [_v(r"$\beta=200$, $R_C=3$ kΩ, $r=3$ kΩ, à vide. $A_v$ ?", "-200*3/3", "-200", r"$A_v=-\beta\dfrac{R_C}{r}=-200$.")],
    "a103": [_v(r"$\beta=100$, $R_C=R_u=4$ kΩ, $r=1$ kΩ. $A_v$ ?", "-100*(4*4/(4+4))/1", "-200", r"$R_C\parallel R_u=2$ kΩ, $A_v=-100\times2=-200$.")],
    "a104": [_v(r"$\beta=100$, $R_C=R_u=4{,}4$ kΩ, $r=1$ kΩ, $R_E=0{,}1$ kΩ non découplée ($\beta+1\approx\beta$). $A_v$ ?", "-100*(4.4*4.4/(4.4+4.4))/(1+100*0.1)", "-20", r"$A_v=-\dfrac{100\times2{,}2}{1+10}=-20$.")],
    "a105": [_v(r"$e_G=50$ mV, $R_g=1$ kΩ, $R_i=1{,}5$ kΩ. $v$ (en mV) ?", "50*1.5/(1.5+1)", "30", r"$v=\dfrac{1{,}5}{2{,}5}\times50=30$ mV.")],
    "d111": [_v(r"$\beta_1=80$, $\beta_2=25$. $\beta\approx\beta_1\beta_2$ ?", "80*25", "2000", r"$\beta\approx2000$.")],
    "d112": [_v(r"$\beta_1=80$, $\beta_2=25$. $\beta=\beta_1+\beta_2+\beta_1\beta_2$ ?", "80+25+80*25", "2105", r"$80+25+2000=2105$.")],
    "d113": [_v(r"Darlington de gain $2000$, $I_B=5$ \mu A. $I_C$ (en mA) ?", "2000*5/1000", "10", r"$I_C=2000\times0{,}005=10$ mA.")],
    "d114": [_v(r"$A_{v1}=-5$ et $A_{v2}=-8$ en cascade. $A_v$ ?", "(-5)*(-8)", "40", r"$A_v=(-5)(-8)=40$.")],
    "d116": [_v(r"$A_{v1}$ à vide $=-50$, $R_{o1}=2$ kΩ, $R_{i2}=6$ kΩ. $A_{v1}$ chargé ?", "-50*6/(6+2)", "-37.5", r"$-50\times\dfrac{6}{8}=-37{,}5$.")],
    "o121": [_v(r"Inverseur CMOS (figure), $V_{CC}=3{,}3$ V, $V_{IN}=0$. $V_{GS}$ du MOSP (en V) ?", "0-3.3", "-3.3", r"$V_{GS_P}=0-3{,}3=-3{,}3$ V.")],
    "o122": [_v(r"Inverseur CMOS (figure), $V_{CC}=3{,}3$ V, $V_{IN}=3{,}3$ V. $V_{GS}$ du MOSN (en V) ?", "3.3-0", "3.3", r"$V_{GS_N}=3{,}3$ V.")],
    "o123": [_v(r"Inverseur CMOS (figure), $V_{CC}=5$ V, $V_{IN}=0$. $V_{OUT}$ (en V) ?", "5*(1-0/5)", "5", r"MOSP conducteur : $V_{OUT}=V_{CC}=5$ V.")],
    "o124": [_v(r"Inverseur CMOS (figure), $V_{CC}=5$ V, $V_{IN}=5$ V : combien de transistors conduisent ?", "1", "1", r"Un seul (le MOSN).")],
    "n131": [_v(r"Porte NAND CMOS (figure), $V_{CC}=5$ V, $a=5$ V, $b=0$ V. $V_{OUT}$ (en V) ?", "5*(1-1*0)", "5", r"Le MOSP de grille $b=0$ conduit : $V_{OUT}=5$ V.")],
    "n132": [_v(r"Porte NAND CMOS (figure), $V_{CC}=5$ V, $a=5$ V, $b=5$ V. $V_{OUT}$ (en V) ?", "5*(1-1*1)", "0", r"Les deux MOSN conduisent : $V_{OUT}=0$.")],
    "n133": [_v(r"Porte NOR CMOS (figure : MOSP en série, MOSN en parallèle), $V_{CC}=5$ V, $a=5$ V, $b=5$ V. $V_{OUT}$ (en V) ?", "5*(1-(1+1-1*1))", "0", r"Les deux MOSN en parallèle conduisent : $V_{OUT}=0$.")],
    "n134": [_v(r"Porte NOR CMOS (figure : MOSP en série, MOSN en parallèle), $V_{CC}=5$ V, $a=0$ V, $b=5$ V. $V_{OUT}$ (en V) ?", "5*(1-(0+1-0*1))", "0", r"Le MOSN de grille $b=5$ V conduit : $V_{OUT}=0$.")],
    "n135": [_v(r"Combien de transistors dans une NOR CMOS à $4$ entrées ?", "2*4", "8", r"$4$ MOSP et $4$ MOSN : $8$.")],
    "n141": [_v(r"Porte CMOS de la figure, $V_{CC}=5$ V, $x=0$, $y=0$, $z=5$ V. $V_{OUT}$ (en V) ?", "5*(1-(0+1-0*1)*0)", "5", r"$y=0$ : le MOSN de grille $y$ est bloqué, le MOSP $y$ conduit : $V_{OUT}=5$ V.")],
    "n142": [_v(r"Porte CMOS de la figure, $V_{CC}=5$ V, $x=5$ V, $y=5$ V, $z=5$ V. $V_{OUT}$ (en V) ?", "5*(1-(1+1-1*1)*1)", "0", r"MOSN passant : $V_{OUT}=0$.")],
    "n143": [_v(r"Contrôler que $\overline{ab+cd}=(\overline a+\overline b)(\overline c+\overline d)$ (1 = égal) ?", "eqv(Not((A&B)|(C&D)), (~A|~B)&(~C|~D))", "1", r"De Morgan sur la somme puis sur chaque produit.")],
    "n144": [_v(r"Combien de combinaisons des trois entrées donnent $5$ V pour une NAND à $3$ entrées ?", "2**3-1", "7", r"Seule $a=b=c=1$ donne $0$ : $8-1=7$.")],
    "n147": [_v(r"Contrôler que $\overline{a\oplus b}=ab+\overline a\,\overline b$ (1 = égal) ?", "eqv(~Xor(A,B), (A&B)|(~A&~B))", "1", r"Le XNOR est vrai quand $a=b$ : $ab+\overline a\,\overline b$.")],
    "h11": [_v(r"Même étage avec $R_1=18$ kΩ, $R_2=9$ kΩ, $R_E=0{,}6$ kΩ, $V_{CC}=12$ V. $I_B$ (en \mu A) ?", "(4-0.7)/(6+100*0.6)*1000", "50", r"$E_{th}=4$ V, $R_{th}=6$ kΩ : $I_B=\dfrac{3{,}3}{66}=50$ µA.")],
    "h12": [_v(r"Même variante avec $R_C=1$ kΩ. $V_{CE}$ (en V) ?", "12-(1+0.6)*100*(4-0.7)/(6+100*0.6)", "4", r"$I_C=5$ mA, $V_{CE}=12-1{,}6\times5=4$ V.")],
    "h13": [_v(r"Même variante. $I_{C,sat}$ (en mA) ?", "12/(1+0.6)", "7.5", r"$\dfrac{12}{1{,}6}=7{,}5$ mA : $I_C=5 < 7{,}5$, linéaire.")],
    "h14": [_v(r"$I_{B0}=50$ \mu A. $r$ (en Ω) ?", "2*26/Rational(50,1000)", "1040", r"$r=\dfrac{52}{0{,}05}=1040$ Ω.")],
    "h15": [_v(r"$\beta=100$, $R_C=1$ kΩ, $R_u=3$ kΩ, $r=1{,}04$ kΩ, $C_E$ en place. $A_v$ ?", "-100*(1*3/(1+3))/1.04", "-1875/26", r"$A_v=-\dfrac{100\times0{,}75}{1{,}04}=-\dfrac{1875}{26}\approx-72{,}1$.")],
    "h16": [_v(r"$R_{th}=6$ kΩ, $r=1{,}04$ kΩ. $R_i$ (en kΩ, valeur exacte) ?", "6*1.04/(6+1.04)", "39/44", r"$R_i=\dfrac{6{,}24}{7{,}04}=\dfrac{39}{44}\approx0{,}89$ kΩ.")],
    "h17": [_v(r"$\beta=100$, $R_C\parallel R_u=0{,}75$ kΩ, $r=1{,}04$ kΩ, $R_E=0{,}6$ kΩ sans découplage. $A_v$ ?", "-100*0.75/(1.04+100*0.6)", "-1875/1526", r"$A_v=-\dfrac{75}{61{,}04}=-\dfrac{1875}{1526}\approx-1{,}23$.")],
    "r1": [_v(r"$V_{CC}=12{,}7$ V, $R_C=1$ kΩ, $R_B=199$ kΩ, $\beta=100$. $I_B$ (en \mu A) ?", "(12.7-0.7)/(199+(100+1)*1)*1000", "40", r"$I_B=\dfrac{12}{199+101}=40$ µA.")],
    "r2": [_v(r"Même variante. $V_{CE}$ (en V) ?", "12.7-1*(100+1)*(12.7-0.7)/(199+(100+1)*1)", "8.66", r"$V_{CE}=12{,}7-101\times0{,}04=8{,}66$ V.")],
    "r3": [_v(r"$V_{CC}=10{,}7$ V, $R_C=2$ kΩ, $\beta=100$ : $R_B$ pour $V_{CE}=7{,}7$ V (en kΩ) ?", "(7.7-0.7)/((10.7-7.7)/(2*(100+1)))", "1414/3", r"$I_B=\dfrac{3}{202}$ mA, $R_B=\dfrac{7}{3/202}=\dfrac{1414}{3}\approx471{,}3$ kΩ.")],
    "r5": [_v(r"Même montage de base ($V_{CC}=10{,}7$ V, $R_C=2$ kΩ, $R_B=198$ kΩ), $\beta=50$. $I_C$ (en mA, valeur exacte) ?", "50*(10.7-0.7)/(198+(50+1)*2)", "5/3", r"$I_B=\dfrac{10}{300}=\dfrac1{30}$ mA, $I_C=\dfrac{50}{30}=\dfrac53\approx1{,}67$ mA.")],
    "t1": [_v(r"$R_C=120$ Ω, $V_{CC}=12$ V. $I_{C,sat}$ (en mA) ?", "12/0.12", "100", r"$\dfrac{12}{0{,}12}=100$ mA.")],
    "t2": [_v(r"$R_C=120$ Ω, $V_{CC}=12$ V, $\beta=50$. $I_B$ minimal (en \mu A) ?", "12/0.12/50*1000", "2000", r"$\dfrac{100}{50}=2$ mA $=2000$ µA.")],
    "t3": [_v(r"$V_1=5$ V, $I_{B,min}=1$ mA. $R_B$ maximale (en kΩ) ?", "(5-0.7)/1", "4.3", r"$R_B\leq\dfrac{4{,}3}{1}=4{,}3$ kΩ.")],
    "t4": [_v(r"$R_B=2{,}15$ kΩ, $V_1=5$ V. $I_B$ (en mA) ?", "(5-0.7)/2.15", "2", r"$I_B=\dfrac{4{,}3}{2{,}15}=2$ mA.")],
    "i11": [_v(r"Même porte, $a=0$, $b=5$ V, $c=0$, $d=5$ V. $V_{OUT}$ (en V) ?", "5*(1-(0*1+0*1-0*1*0*1))", "5", r"$ab=0$ et $cd=0$ : aucun MOSN conducteur, les MOSP conduisent : $V_{OUT}=5$ V.")],
    "i12": [_v(r"Porte à six entrées, MOSN ($a$ série $b$) // ($c$ série $d$) // ($e$ série $f$). Combinaisons donnant $5$ V (sur $64$) ?", "3*3*3", "27", r"$S=1$ si les trois produits sont nuls : $3\times3\times3=27$.")],
    "i13": [_v(r"Contrôler que $\overline{ab+c}=(\overline a+\overline b)\overline c$ (1 = égal) ?", "eqv(Not((A&B)|C), (~A|~B)&~C)", "1", r"De Morgan : $\overline{ab}\cdot\overline c$.")],
    "i14": [_v(r"Nombre de transistors de la porte à six entrées de la question 2 ?", "2*6", "12", r"$6$ MOSP et $6$ MOSN : $12$.")],
    "i22": [_v(r"Un XNOR obtenu en ajoutant un inverseur supplémentaire (3 inverseurs) : total ?", "8+3*2", "14", r"$8+3\times2=14$.")],
    "i23": [_v(r"$a=5$ V, $b=5$ V : $V_{OUT}$ du OU exclusif (en V) ?", "5*(1-(1*1+(1-1)*(1-1)))", "0", r"$ab=1$ : MOSN conducteur, $S=0$.")],
    "i31": [_v(r"Étage MOSP : ($a$ série $b$ série $c$) // $d$. Combinaisons de $(a,b,c,d)$ donnant $5$ V (sur $16$) ?", "8+1", "9", r"$S=\overline a\,\overline b\,\overline c+\overline d$ : $d=0$ donne $8$ ; $d=1$ exige $a=b=c=0$ : $1$. Total $9$.")],
    "i32": [_v(r"Même porte que n145, $a=0$, $b=0$, $c=5$ V. $V_{OUT}$ (en V) ?", "5*(1-(0+0-0)*1)", "5", r"Branche MOSP ($a$ série $b$) conduit ($a=b=0$) : $V_{OUT}=5$ V.")],
    "f201": [_v(r"$R_B=100$ kΩ, $R_C=500$ Ω, $R_E=1$ kΩ, $V_{CC}=10$ V, $\beta=100$. $I_B$ (en \mu A, $\beta+1\approx\beta$) ?", "(10-0.7)/(100+100*1)*1000", "46.5", r"$I_B=\dfrac{9{,}3}{200}=46{,}5$ µA.")],
    "f202": [_v(r"Même variante. $I_C$ (en mA) ?", "100*(10-0.7)/(100+100*1)", "4.65", r"$100\times0{,}0465=4{,}65$ mA.")],
    "f203": [_v(r"Même variante. $V_{CE}$ (en V) ?", "10-(0.5+1)*100*(10-0.7)/(100+100*1)", "3.025", r"$V_{CE}=10-1{,}5\times4{,}65=3{,}025$ V.")],
    "f204": [_v(r"$V_{CC}=12$ V, $R_C=1$ kΩ, $R_E=1$ kΩ. $I_{C,sat}$ (en mA) ?", "12/2", "6", r"$\dfrac{12}{2}=6$ mA.")],
    "f211": [_v(r"$R_C=2$ kΩ, $R_E=1$ kΩ, $V_{CC}=12$ V. $I_{C,sat}$ (en mA) ?", "12/(2+1)", "4", r"$\dfrac{12}{3}=4$ mA.")],
    "f212": [_v(r"$R_C=2$ kΩ, $R_E=1$ kΩ, $V_{CC}=12$ V, $\beta=100$, $V_{BE}=0{,}6$ V. $R_B$ minimale (en kΩ, avec $\beta+1=101$) ?", "100*(12-0.6)/4-(100+1)*1", "184", r"$R_B > 100\times\dfrac{11{,}4}{4}-101=285-101=184$ kΩ.")],
    "f221": [_v(r"$R_C=60$ Ω, $V_{CC}=12$ V, $\beta=100$, $I_C=50$ mA. $R_B$ (en kΩ) ?", "100*(12-0.7)/50", "22.6", r"$I_B=0{,}5$ mA, $R_B=\dfrac{11{,}3}{0{,}5}=22{,}6$ kΩ.")],
    "f222": [_v(r"$R_C=100$ Ω, $V_{CC}=12$ V. $I_{C,sat}$ (en mA) ?", "12/0.1", "120", r"$\dfrac{12}{0{,}1}=120$ mA.")],
    "f223": [_v(r"$R_C=100$ Ω, $V_{CC}=12$ V, $\beta=100$, $V_{BE}=0{,}7$ V. $R_B$ minimale pour saturer (en kΩ) ?", "100*(12-0.7)/120", "113/12", r"$R_B=100\times\dfrac{11{,}3}{120}=\dfrac{113}{12}\approx9{,}42$ kΩ.")],
    "f225": [_v(r"Même circuit avec $R_E=40$ Ω : $V_{CE}$ calculé sous l'hypothèse linéaire (en V, valeur exacte) ?", "12-(100*1.2+(100+1)*0.04)*(2-0.7)/(Rational(10,3)+(100+1)*0.04)", "-7797/790", r"$I_B=\dfrac{1{,}3}{\frac{10}3+4{,}04}\approx0{,}176$ mA, $V_{CE}=12-124{,}04\times0{,}176\approx-9{,}87$ V $< 0$ : saturé.")],
    "f241": [_v(r"$V_C=8$ V et $V_E=2$ V. $V_{CE}$ (en V) ?", "8-2", "6", r"$V_{CE}=6$ V $> 0$ : linéaire.")],
    "f242": [_v(r"$V_{CC}=15$ V, $V_C=5$ V, $I_B=50$ \mu A, $\beta=200$. $R_C$ (en Ω) ?", "(15-5)/(200*0.05)*1000", "1000", r"$I_C=10$ mA, $R_C=1$ kΩ.")],
    "f251": [_v(r"$R_C=2$ kΩ, $R_E=1$ kΩ, $V_{CC}=12$ V, $I_C=3$ mA. $V_{CE}$ (en V) ?", "12-(2+1)*3", "3", r"$V_{CE}=12-9=3$ V.")],
    "f254": [_v(r"$V_{BE}=0{,}7$ V, $V_{CE}=4$ V. $V_{BC}$ (en V) ?", "0.7-4", "-3.3", r"$V_{BC}=0{,}7-4=-3{,}3$ V.")],
    "f255": [_v(r"$E=10$ V, $V_{CE}=4$ V, $I_C=10$ mA. $R_C$ (en Ω) ?", "(10-4)/10*1000", "600", r"$R_C=\dfrac{6}{10}=0{,}6$ kΩ.")],
    "f261": [_v(r"$R_C=2$ kΩ, $V_{CC}=10$ V. $I_{C,sat}$ (en mA) ?", "10/2", "5", r"$\dfrac{10}{2}=5$ mA.")],
    "f262": [_v(r"$R_C=2$ kΩ, $V_{CC}=10$ V, $\beta=100$, $V_{BE}=0{,}6$ V. $R_B$ minimale (en kΩ) ?", "100*(10-0.6)/5", "188", r"$R_B > 100\times\dfrac{9{,}4}{5}=188$ kΩ.")],
    "f263": [_v(r"$R_B=100$ kΩ, $R_C=R_E=1$ kΩ, $V_{CC}=10$ V, $\beta=100$. $I_B$ (en \mu A) ?", "(10-0.7)/(100+100*1)*1000", "46.5", r"$I_B=\dfrac{9{,}3}{200}=46{,}5$ µA.")],
    "f264": [_v(r"Même variante. $I_C$ (en mA) ?", "100*(10-0.7)/(100+100*1)", "4.65", r"$I_C=4{,}65$ mA.")],
    "f265": [_v(r"Même variante. $V_{CE}$ (en V) ?", "10-(1+1)*4.65", "0.7", r"$V_{CE}=10-9{,}3=0{,}7$ V.")],
}
for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["id"] in VARIANTS:
            _e["variants"] = VARIANTS[_e["id"]]
for _e in EXTRA_PARTS:
    if _e["id"] in VARIANTS:
        _e["variants"] = VARIANTS[_e["id"]]


def _q(notion, q, choix, bonne):
    return {"notion": notion, "type": "qcm", "q": q, "choix": choix, "bonne": bonne}


def _f(notion, q, bonne):
    return {"notion": notion, "type": "vf", "q": q, "bonne": bonne}


QUIZ = [
    _f("lois", r"Dans un pont diviseur, les deux résistances sont traversées par le même courant.", True),
    _q("lois", r"$E=10$ V, $R_1=1$ kΩ, $R_2=4$ kΩ en série : la tension aux bornes de $R_2$ vaut", [r"$8$ V", r"$2$ V", r"$10$ V", r"$4$ V"], 0),
    _f("jonction", r"Une jonction PN en polarisation inverse laisse passer un courant important.", False),
    _q("jonction", r"La tension d'une jonction base-émetteur passante (silicium) vaut environ", [r"$0{,}7$ V", r"$5$ V", r"$0$ V", r"$7$ V"], 0),
    _q("bjt", r"Comment s'appellent les bornes d'un transistor bipolaire ?", [r"Grille, drain, source", r"Base, émetteur, collecteur", r"Anode, cathode", r"Base, convecteur, éditeur"], 1),
    _q("bjt", r"En mode linéaire, $\beta=200$ et $I_C=100$ mA : $I_B$ vaut", [r"$500$ \mu A", r"$20$ A", r"$0{,}2$ mA", r"$2$ A"], 0),
    _f("bjt", r"Dans un NPN, $I_E=I_C+I_B$.", True),
    _f("modes", r"Quand le transistor est saturé, ses deux jonctions sont passantes.", True),
    _q("modes", r"Un transistor saturé est équivalent, entre collecteur et émetteur, à", [r"un interrupteur ouvert", r"une diode", r"un fil", r"une résistance"], 2),
    _f("modes", r"Le mode linéaire du transistor bipolaire sert principalement à concevoir des portes logiques.", False),
    _q("mode_test", r"Si $I_B=0$, le transistor est", [r"saturé", r"linéaire", r"bloqué", r"détruit"], 2),
    _f("mode_test", r"Le courant de saturation $I_{C,sat}$ est le courant $I_C$ quand $V_{CE}=0$.", True),
    _q("mode_test", r"Pour montrer qu'un transistor n'est pas linéaire, on le suppose linéaire puis on trouve", [r"$V_{CE} < 0$", r"$I_B=0$", r"$V_{BE}=5$ V", r"$\beta=0$"], 0),
    _q("pol_rb", r"Montage à résistance de base : $I_B=$", [r"$\dfrac{V_{CC}-V_{BE}}{R_B}$", r"$\dfrac{V_{CC}}{R_B}$", r"$\dfrac{V_{CC}+V_{BE}}{R_B}$", r"$\dfrac{V_{BE}}{R_B}$"], 0),
    _f("pol_rb", r"La droite de charge a pour équation $V_{CE}=V_{CC}-R_CI_C$.", True),
    _q("pol_rb", r"$V_{CC}=12$ V, $R_C=60$ Ω : le courant de saturation vaut", [r"$200$ mA", r"$720$ mA", r"$5$ mA", r"$12$ A"], 0),
    _q("pol_re", r"Avec une résistance d'émetteur, le courant qui la traverse vaut", [r"$I_C$", r"$(\beta+1)I_B$", r"$I_B$", r"$\beta I_C$"], 1),
    _f("pol_re", r"Avec la réaction de collecteur, le courant dans $R_C$ est $I_C$ uniquement.", False),
    _q("pol_re", r"Avec $R_E$ et $R_C$ en série, $I_{C,sat}=$", [r"$\dfrac{V_{CC}}{R_C+R_E}$", r"$\dfrac{V_{CC}}{R_C}$", r"$\dfrac{V_{CC}}{R_E}$", r"$\dfrac{V_{CC}}{\beta}$"], 0),
    _q("pol_pont", r"Le générateur de Thévenin vu par la base d'un pont $R_1$ (vers $V_{CC}$), $R_2$ (vers la masse) a pour tension", [r"$\dfrac{R_2}{R_1+R_2}V_{CC}$", r"$\dfrac{R_1}{R_1+R_2}V_{CC}$", r"$V_{CC}$", r"$R_1\parallel R_2$"], 0),
    _f("pol_pont", r"Si $I_B$ est négligeable devant les courants du pont, $R_1$ et $R_2$ sont traversées par le même courant.", True),
    _q("commut", r"Inverseur à transistor : entrée à $5$ V, transistor saturé, la sortie vaut", [r"$5$ V", r"$0$ V", r"$2{,}5$ V", r"$0{,}7$ V"], 1),
    _f("commut", r"Un transistor commandé par un petit courant de base peut contrôler un courant de collecteur beaucoup plus grand.", True),
    _f("commut", r"Deux entrées reliées à la base par deux résistances réalisent une NOR.", True),
    _q("petits", r"Pour le schéma petits signaux, les condensateurs de liaison sont remplacés par", [r"des interrupteurs ouverts", r"des fils", r"des résistances", r"des sources"], 1),
    _f("petits", r"Pour le schéma petits signaux, on annule les sources continues.", True),
    _q("petits", r"La résistance $r=\dfrac{mV_T}{I_{B0}}$ : si $I_{B0}$ double, $r$", [r"double", r"est divisée par $2$", r"ne change pas", r"est multipliée par $4$"], 1),
    _q("ampli", r"Amplificateur émetteur commun sans $R_E$ : $A_v=$", [r"$-\beta\dfrac{R_C\parallel R_u}{r}$", r"$+\beta R_C$", r"$\dfrac{r}{R_C}$", r"$-\dfrac{R_B}{r}$"], 0),
    _f("ampli", r"Une résistance d'émetteur non découplée diminue le gain en tension.", True),
    _q("ampli", r"Le rôle de $V_{CC}$ dans un amplificateur est", [r"de polariser le transistor dans sa zone linéaire", r"de bloquer le transistor", r"de saturer le transistor", r"aucun"], 0),
    _q("darlington", r"Deux transistors en Darlington ($\beta_1$, $\beta_2$ grands) ont un gain équivalent d'environ", [r"$\beta_1\beta_2$", r"$\beta_1+\beta_2$", r"$\beta_1/\beta_2$", r"$\beta_1-\beta_2$"], 0),
    _f("darlington", r"Pour deux étages en cascade, l'amplification totale est le produit des amplifications.", True),
    _q("mos", r"Un MOSN est conducteur quand", [r"$V_{GS}=0$", r"$V_{GS}=5$ V", r"$V_{GS}=-5$ V", r"$I_G\neq0$"], 1),
    _f("mos", r"Un MOSP est conducteur quand $V_{GS}=-5$ V.", True),
    _f("mos", r"Le courant de grille d'un MOSFET est nul.", True),
    _q("cmos", r"Une NAND CMOS à deux entrées a ses MOSP", [r"en parallèle", r"en série", r"seulement un", r"absents"], 0),
    _q("cmos", r"MOSN : $x$ en parallèle avec $z$, le tout en série avec $y$. La fonction est", [r"$\overline{(x+z)\,y}$", r"$(x+z)\,y$", r"$\overline{xz+y}$", r"$xz\,y$"], 0),
    _f("cmos", r"Dans une porte CMOS, les étages MOSP et MOSN ne conduisent jamais ensemble.", True),
]

# ---------------------------------------------------------------- formulas by level

_F = {n["id"]: n["formule"] for n in NOTIONS}
FORMULES = {e["id"]: " · ".join(_F[n] for n in lvl["notions"]) for lvl in LEVELS for e in lvl["exos"] if e["kind"] != "multi"}
_EX = {"x11": ["pol_re"], "x31": ["modes"], "h11": ["pol_pont"], "h12": ["pol_re"], "h13": ["mode_test"], "h14": ["petits"],
       "h15": ["ampli"], "h16": ["ampli"], "h17": ["ampli"], "r1": ["pol_re"], "r2": ["pol_re"], "r3": ["pol_re"], "r4": ["pol_re"],
       "r5": ["pol_re"], "t1": ["mode_test"], "t2": ["commut"], "t3": ["commut"], "t4": ["commut"], "t5": ["commut"],
       "i11": ["cmos"], "i12": ["cmos"], "i13": ["cmos"], "i14": ["cmos"], "i15": ["cmos"], "i22": ["cmos"], "i23": ["cmos"],
       "i31": ["cmos"], "i32": ["cmos"], "f201": ["pol_re"], "f202": ["pol_re"], "f203": ["pol_re"], "f204": ["pol_re", "mode_test"],
       "f211": ["pol_re", "mode_test"], "f212": ["pol_re", "mode_test"], "f213": ["pol_re"], "f221": ["pol_rb"], "f222": ["mode_test"],
       "f223": ["pol_rb", "mode_test"], "f224": ["pol_pont"], "f225": ["pol_pont", "mode_test"], "f241": ["mode_test"],
       "f242": ["pol_re"], "f251": ["pol_re"], "f254": ["bjt"], "f255": ["pol_rb"], "f261": ["mode_test"], "f262": ["pol_rb", "mode_test"],
       "f263": ["pol_re"], "f264": ["pol_re"], "f265": ["pol_re"]}
FORMULES.update({i: " · ".join(_F[n] for n in ns) for i, ns in _EX.items()})

# ---------------------------------------------------------------- figures per exercise

FIGS = {**dict.fromkeys(["k11", "k12"], FIG_DIV), "k13": FIG_MAILLE, "j21": FIG_DIODE, "j22": FIG_DIODE_INV,
        **dict.fromkeys(["j23", "j24"], FIG_JBE),
        "s41": FIG_GND, **dict.fromkeys(["s42", "s43", "s44"], FIG_RB), "s45": FIG_BVCC,
        **dict.fromkeys(["p51", "p52", "p53", "p54", "p55", "p56", "p57", "p58", "p59", "fx3", "fx5", "fx6", "f221", "f222", "f223"], FIG_RB),
        **dict.fromkeys(["e61", "e62", "e63", "e64", "e65", "fx1", "fx2", "fx4"], FIG_RE),
        **dict.fromkeys(["e66", "e67", "e68", "hx2"], FIG_FB),
        **dict.fromkeys(["q71", "q72", "q73", "q74", "q75", "q76", "q80", "mx2"], FIG_PONT_E),
        **dict.fromkeys(["q77", "q78", "q79"], FIG_PONT_C),
        **dict.fromkeys(["c81", "c82", "c83", "c84", "c85", "c86", "c89", "hx3"], FIG_INV),
        **dict.fromkeys(["c87", "c88"], FIG_NOR),
        **dict.fromkeys(["g95", "g97", "a101", "a102", "a103", "a105"], FIG_AMP0),
        **dict.fromkeys(["a104", "a106", "mx1"], FIG_AMP), "hx1": FIG_AMP_PONT,
        **dict.fromkeys(["d111", "d112", "d113", "d115"], FIG_DARL),
        **dict.fromkeys(["o121", "o122", "o123", "o124"], FIG_CINV),
        **dict.fromkeys(["n131", "n132", "n136"], FIG_NAND), **dict.fromkeys(["n133", "n134", "n137"], FIG_CNOR),
        **dict.fromkeys(["n141", "n142", "n143", "n144"], FIG_TD1), "n145": FIG_ETAGEN, "ix3": FIG_ETAGEN, "ix1": FIG_AOI}
ajoute(LEVELS, FIGS)
