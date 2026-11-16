"""Circuit figures for the electronics paths, drawn with schemdraw in the French (exam) conventions.

`fig(draw, alt)` runs `draw(d)` on a fresh schemdraw Drawing, saves the SVG in `static/schemas/` (name = hash of the
drawing, like `algo_abg.fig` does for trees) and returns the Markdown image. Build-time only: needs `schemdraw` and
`ziamath` (labels written `$...$` are turned into paths, so no font is needed on the phone). The app serves the SVG
as a static file and never imports this module.

Conventions of the EPITA subjects: voltage source = circle crossed by the wire (`SrcU`), current source = circle
crossed perpendicularly (`SrcI`), resistor = IEC box, voltage = arrow beside the dipole (`tension`), current = arrow
head on the wire (`courant`).
"""
import hashlib
from pathlib import Path

import schemdraw
import schemdraw.elements as elm
from schemdraw.segments import Segment, SegmentCircle

schemdraw.use("svg")
schemdraw.svgconfig.text = "path"  # math labels as outlines: same look on every device
schemdraw.svgconfig.svg2 = False

FIG_DIR = Path(__file__).resolve().parents[2] / "static" / "schemas"
FIG_URL = "/static/schemas/"

R = elm.ResistorIEC
C = elm.Capacitor
L = elm.Inductor2
D = elm.Diode
Fil = elm.Line
Point = elm.Dot
Masse = elm.Ground
Inter = elm.Switch
Gap = elm.Gap


class SrcU(elm.Element2Term):
    """Ideal voltage source, French symbol: circle crossed by the wire."""
    def __init__(self, **kw):
        super().__init__(**kw)
        self.segments.append(Segment([(0, 0), (0, 0), elm.elements.gap, (1, 0), (1, 0)]))  # leads
        self.segments.append(SegmentCircle((0.5, 0), 0.5))
        self.segments.append(Segment([(0, 0), (1, 0)]))  # the wire crossing the circle


class SrcI(elm.Element2Term):
    """Ideal current source, French symbol: circle crossed perpendicularly to the wire."""
    def __init__(self, **kw):
        super().__init__(**kw)
        self.segments.append(Segment([(0, 0), (0, 0), elm.elements.gap, (1, 0), (1, 0)]))
        self.segments.append(SegmentCircle((0.5, 0), 0.5))
        self.segments.append(Segment([(0.5, -0.5), (0.5, 0.5)]))


def tension(d, e, label, sens=1, cote=True, ofst=0.6, length=1.6):
    """Voltage arrow beside element `e`; sens=1 points the arrow along the element's drawing direction."""
    d += elm.CurrentLabel(top=cote, ofst=ofst, length=length, reverse=sens < 0).at(e).label(label)


def courant(d, e, label, sens=1, debut=True, loc=None):
    """Current arrow head on the wire of element `e`; sens=1 = along the drawing direction; loc moves the label."""
    along = "in" if debut else "out"  # schemdraw: "in" points into the element
    d += elm.CurrentLabelInline(direction=along if sens > 0 else {"in": "out", "out": "in"}[along],
                                start=debut).at(e).label(label, loc=loc)


def fig(draw, alt):
    """Markdown image of the circuit drawn by `draw(d)`; `alt` describes it in words (screen readers, copy-for-AI)."""
    with schemdraw.Drawing(show=False, unit=2.5, fontsize=19, lw=1.6) as d:
        draw(d)
    svg = d.get_imagedata("svg").decode()
    name = "elec-" + hashlib.sha1(svg.encode()).hexdigest()[:12] + ".svg"
    path = FIG_DIR / name
    if not path.exists() or path.read_text() != svg:
        FIG_DIR.mkdir(parents=True, exist_ok=True)
        path.write_text(svg)
    return f"![{alt.replace('[', '(').replace(']', ')')}]({FIG_URL}{name})"


_DIP = {"R": R, "C": C, "L": L, "D": D, "DZ": elm.Zener, "K": Inter, "I": SrcI, "U": SrcU, "Z": R}


def _dip(code, a, b):
    """Element `code` from a to b: 'R', 'C', 'L', 'D', 'DZ' (Zener), 'K' (switch), 'I'/'U' (sources), 'Z' (impedance
    box). A diode drawn from a to b has its anode at a; a trailing '<' draws it from b to a (cathode at a)."""
    if code.endswith("<"):  # schemdraw's reverse() is ignored once endpoints() places the element
        a, b = b, a
    return _DIP[code.rstrip("<")]().endpoints(a, b)


def echelle(d, source, branches, sortie=None, sortie_sur=None):
    """Ladder circuit: voltage source `source` on the left, then `branches` from left to right, each
    ('s', code, label) on the top rail or ('p', code, label) from the top rail to the bottom one.
    `sortie` labels the output voltage, across the last shunt or across open terminals after a series element;
    `sortie_sur` = index of the branch carrying the output when it is not the last one. Without `sortie`, a
    circuit ending with a series element is closed by a wire.
    Labels are math without the dollars ('2R', 'v_e(t)')."""
    H, x, prev, last = 3, 0, "src", None
    d += (s := SrcU().endpoints((0, 0), (0, H)))
    tension(d, s, f"${source}$")
    for i, (kind, code, lab) in enumerate(branches):
        if kind == "s":
            d += _dip(code, (x, H), (x + 3, H)).label(f"${lab}$" if lab else "")
            d += Fil().endpoints((x, 0), (x + 3, 0))
            x += 3
        else:
            if prev != "s":  # two shunts side by side need a wire between them
                d += Fil().endpoints((x, H), (x + 2, H))
                d += Fil().endpoints((x, 0), (x + 2, 0))
                x += 2
            d += (e := _dip(code, (x, H), (x, 0)).label(f"${lab}$" if lab else "", loc="bottom"))
            if i == (len(branches) - 1 if sortie_sur is None else sortie_sur):
                last, up = e, code.endswith("<")  # `up`: drawn bottom to top
        prev = kind
    if not sortie and prev == "s":  # nothing at the output: close the loop
        d += Fil().endpoints((x, H), (x, 0))
    if sortie and last is not None:
        tension(d, last, f"${sortie}$", sens=1 if up else -1, cote=not up, ofst=0.9)
    elif sortie:  # open output terminals after a series element
        d += Fil().endpoints((x, H), (x + 1.5, H))
        d += Fil().endpoints((x, 0), (x + 1.5, 0))
        d += Point(open=True).at((x + 1.5, H))
        d += Point(open=True).at((x + 1.5, 0))
        d += (g := elm.Gap().endpoints((x + 1.5, H), (x + 1.5, 0)))
        tension(d, g, f"${sortie}$", sens=-1, ofst=0.4)


def ajoute(levels, figs):
    """Put each figure of `figs` ({exercise id: Markdown image}) at the top of the statement and of its variants."""
    for lvl in levels:
        for e in lvl["exos"]:
            if e["id"] in figs:
                for x in [e] + e.get("variants", []):
                    x["enonce"] = figs[e["id"]] + "\n\n" + x["enonce"]


def schema_echelle(source, branches, sortie=None):
    """Markdown image of a ladder circuit (see `echelle`), with a description in words as alt text."""
    words = [f"source {source}"] + [f"{lab or code} {'en série' if k == 's' else 'en parallèle'}"
                                    for k, code, lab in branches]
    alt = ", ".join(words) + (f", sortie {sortie}" if sortie else "")
    for ch in "\\{}":
        alt = alt.replace(ch, "")
    return fig(lambda d: echelle(d, source, branches, sortie), "Schéma : " + alt.replace("underline", ""))
