"""Draw the neo-brutalist home background and its 10 stickers as SVG into static/neo/ (docs/refonte-neobrutaliste.md).

Run: python3 tools/gen_neo_stickers.py
"""
import math
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / 'static' / 'neo'
FONT = "font-family=\"'Arial Black', Impact, 'Helvetica Neue', Arial, sans-serif\" font-weight=\"900\""
INK = '#0D0D0D'
SH = 8  # hard offset shadow


def svg(w, h, body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">{body}</svg>\n'


def shadowed(shape, fill, sw=4):
    """shape = an SVG element string without fill/stroke; drawn once in black offset, once in colour."""
    return (f'<g transform="translate({SH} {SH})" fill="{INK}" stroke="{INK}" stroke-width="{sw}" stroke-linejoin="round">{shape}</g>'
            f'<g fill="{fill}" stroke="{INK}" stroke-width="{sw}" stroke-linejoin="round">{shape}</g>')


def label(x, y, txt, size, fill, outline=True):
    stroke = f' stroke="{INK}" stroke-width="{size / 7:.1f}" paint-order="stroke" stroke-linejoin="round"' if outline else ''
    return f'<text x="{x}" y="{y}" text-anchor="middle" dominant-baseline="central" font-size="{size}" {FONT} fill="{fill}"{stroke}>{txt}</text>'


def pts(points):
    return ' '.join(f'{x:.1f},{y:.1f}' for x, y in points)


def burst(cx, cy, r_out, r_in, n, phase=0.0):
    return [(cx + (r_out if i % 2 == 0 else r_in) * math.cos(phase + i * math.pi / n),
             cy + (r_out if i % 2 == 0 else r_in) * math.sin(phase + i * math.pi / n)) for i in range(2 * n)]


def star4(cx, cy, r):
    return (f'<path d="M{cx} {cy - r} Q{cx} {cy} {cx + r} {cy} Q{cx} {cy} {cx} {cy + r} '
            f'Q{cx} {cy} {cx - r} {cy} Q{cx} {cy} {cx} {cy - r} Z"/>')


def background():
    g = '#E6E6E6'
    parts = [f'<rect width="1920" height="1080" fill="#FFFFFF"/>', f'<g stroke="{g}" stroke-width="2" fill="none">']
    for x0, y0 in ((1600, 70), (70, 820)):  # wireframe grids
        for i in range(7):
            parts.append(f'<line x1="{x0 + i * 32}" y1="{y0}" x2="{x0 + i * 32}" y2="{y0 + 192}"/>')
            parts.append(f'<line x1="{x0}" y1="{y0 + i * 32}" x2="{x0 + 192}" y2="{y0 + i * 32}"/>')
    spiral = [(1760 + 4 * t * math.cos(t), 900 + 4 * t * math.sin(t)) for t in (k * 0.12 for k in range(260))]
    parts.append(f'<polyline points="{pts(spiral)}"/></g><g fill="{g}">')
    for x0, y0 in ((1500, 330), (330, 640)):  # pixel checkerboards
        for i in range(4):
            for j in range(4):
                if (i + j) % 2 == 0:
                    parts.append(f'<rect x="{x0 + i * 16}" y="{y0 + j * 16}" width="16" height="16"/>')
    for cx, cy, r in ((120, 110, 22), (210, 70, 12), (260, 160, 16), (90, 230, 10)):
        parts.append(star4(cx, cy, r))
    parts.append('</g>')
    return svg(1920, 1080, ''.join(parts))


def non_stop():
    body = shadowed('<rect x="6" y="6" width="232" height="76" rx="38"/>', '#155EEF')
    return svg(254, 98, body + label(122, 44, 'NON-STOP', 30, '#FFFFFF'))


def new():
    shape = f'<polygon points="{pts(burst(96, 96, 88, 62, 14))}"/>'
    return svg(200, 200, shadowed(shape, '#FF5A1F') + label(96, 98, 'NEW!', 36, '#FACC15'))


def bulle():
    shape = '<path d="M6 6 H254 V96 H76 L34 138 L48 96 H6 Z"/>'
    return svg(270, 152, shadowed(shape, '#FFFFFF') + label(130, 51, "C'EST PARTI !", 25, INK, outline=False))


def etoiles_fleur():
    out = ['<g fill="#FACC15" stroke="#0D0D0D" stroke-width="4" stroke-linejoin="round">',
           star4(40, 44, 34), star4(150, 30, 22), star4(128, 150, 26), '</g>']
    flower = ['....RR....', '...RRRR...', '.RR.RR.RR.', 'RRRRYYRRRR', 'RRRRYYRRRR',
              '.RR.RR.RR.', '...RRRR...', '....GG....', '..GGGG....', '....GG....']
    colours = {'R': '#F04438', 'Y': '#FACC15', 'G': '#12B76A'}
    for j, row in enumerate(flower):
        for i, c in enumerate(row):
            if c in colours:
                out.append(f'<rect x="{30 + i * 10}" y="{90 + j * 10}" width="10" height="10" fill="{colours[c]}" stroke="#0D0D0D" stroke-width="2"/>')
    return svg(190, 200, ''.join(out))


def curseur_explosion():
    outer = f'<polygon points="{pts(burst(110, 100, 86, 50, 11, 0.2))}"/>'
    inner = f'<polygon points="{pts(burst(110, 100, 52, 30, 9))}" fill="#F97316" stroke="#0D0D0D" stroke-width="3"/>'
    star = f'<g fill="#F04438" stroke="#0D0D0D" stroke-width="3">{star4(110, 100, 24)}</g>'
    arrow = [(0, 0), (0, 34), (8, 26), (14, 40), (20, 37), (14, 24), (25, 24)]
    arrow = [(120 + 2.6 * x, 108 + 2.6 * y) for x, y in arrow]
    cursor = shadowed(f'<polygon points="{pts(arrow)}"/>', '#155EEF')
    return svg(220, 222, shadowed(outer, '#FACC15') + inner + star + cursor)


def feuilles():
    out = []
    for i, (rot, dx) in enumerate(((-12, 20), (6, 46), (-2, 34))):
        sheet = ['<rect width="110" height="140" fill="#FFFFFF" stroke="#0D0D0D" stroke-width="4"/>']
        sheet += [f'<line x1="14" y1="{40 + k * 16}" x2="96" y2="{40 + k * 16}" stroke="#9A9A9A" stroke-width="3"/>' for k in range(5)]
        if i == 2:
            sheet.append('<path d="M14 18 l8 9 l16 -18" fill="none" stroke="#F04438" stroke-width="5" stroke-linecap="round"/>')
            sheet.append('<ellipse cx="80" cy="20" rx="24" ry="14" fill="none" stroke="#F04438" stroke-width="4"/>')
            sheet.append(label(80, 21, '20', 18, '#F04438', outline=False))
            sheet.append('<path d="M70 110 l6 7 l12 -14" fill="none" stroke="#F04438" stroke-width="4" stroke-linecap="round"/>')
        out.append(f'<g transform="translate({dx} {30 + i * 4}) rotate({rot} 55 70)">{"".join(sheet)}</g>')
    return svg(200, 210, ''.join(out))


def livre_carnet():
    book = ('<path d="M10 40 Q60 22 110 44 V160 Q60 138 10 156 Z"/><path d="M110 44 Q160 22 210 40 V156 Q160 138 110 160 Z"/>')
    lines = ''.join(f'<path d="M{a} {y} Q{a + 22} {y - 7} {a + 44} {y + 2}" fill="none" stroke="#9A9A9A" stroke-width="3"/>'
                    for a in (28, 128) for y in (64, 84, 104, 124))
    nb = shadowed('<rect x="196" y="78" width="70" height="96" rx="4"/>', '#12B76A')
    band = '<rect x="208" y="78" width="12" height="96" fill="#0D0D0D"/><rect x="226" y="100" width="30" height="16" fill="#FFFFFF" stroke="#0D0D0D" stroke-width="3"/>'
    sparks = f'<g fill="#155EEF" stroke="#0D0D0D" stroke-width="3">{star4(250, 40, 16)}{star4(22, 186, 12)}{star4(274, 196, 10)}</g>'
    return svg(290, 214, shadowed(book, '#FFFFFF') + lines + nb + band + sparks)


def trophee():
    cup = ('<path d="M44 16 H156 V60 Q156 118 100 126 Q44 118 44 60 Z"/>'
           '<path d="M92 124 H108 V156 H92 Z"/><path d="M56 156 H144 V184 H56 Z"/>')
    handles = ('<path d="M44 34 H18 Q14 82 52 92" fill="none" stroke="#0D0D0D" stroke-width="10" stroke-linecap="round"/>'
               '<path d="M156 34 H182 Q186 82 148 92" fill="none" stroke="#0D0D0D" stroke-width="10" stroke-linecap="round"/>'
               '<path d="M44 34 H18 Q14 82 52 92" fill="none" stroke="#F5B700" stroke-width="4" stroke-linecap="round"/>'
               '<path d="M156 34 H182 Q186 82 148 92" fill="none" stroke="#F5B700" stroke-width="4" stroke-linecap="round"/>')
    star = f'<polygon points="{pts(burst(100, 62, 24, 10, 5, -math.pi / 2))}" fill="#FFF3B0" stroke="#0D0D0D" stroke-width="3"/>'
    return svg(208, 200, handles + shadowed(cup, '#FACC15') + star)


def badge_100c():
    grad = ('<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">'
            '<stop offset="0" stop-color="#F97316"/><stop offset="1" stop-color="#FACC15"/></linearGradient></defs>')
    shape = '<ellipse cx="112" cy="62" rx="104" ry="54"/>'
    return svg(232, 132, grad + shadowed(shape, 'url(#g)') + label(112, 62, '100% C', 34, '#FFFFFF'))


def cocarde():
    seal = [(100 + (80 + 8 * math.cos(16 * t)) * math.cos(t), 100 + (80 + 8 * math.cos(16 * t)) * math.sin(t))
            for t in (k * math.pi / 160 for k in range(320))]
    face = ('<circle cx="100" cy="100" r="52" fill="#FACC15" stroke="#0D0D0D" stroke-width="4"/>'
            '<circle cx="82" cy="88" r="7" fill="#0D0D0D"/><circle cx="118" cy="88" r="7" fill="#0D0D0D"/>'
            '<path d="M74 110 Q100 140 126 110" fill="none" stroke="#0D0D0D" stroke-width="6" stroke-linecap="round"/>')
    return svg(204, 204, shadowed(f'<polygon points="{pts(seal)}"/>', '#155EEF') + face)


FILES = {
    'fond.svg': background, 'badge-non-stop.svg': non_stop, 'badge-new.svg': new, 'bulle-cest-parti.svg': bulle,
    'etoiles-fleur.svg': etoiles_fleur, 'curseur-explosion.svg': curseur_explosion, 'feuilles-examens.svg': feuilles,
    'livre-carnet.svg': livre_carnet, 'trophee.svg': trophee, 'badge-100-c.svg': badge_100c, 'cocarde-smiley.svg': cocarde,
}

if __name__ == '__main__':
    import xml.dom.minidom
    OUT.mkdir(parents=True, exist_ok=True)
    for name, draw in FILES.items():
        data = draw()
        xml.dom.minidom.parseString(data)  # self-check: every file is well-formed XML
        (OUT / name).write_text(data)
        print(name)
