"""Regenerate the last cat explosion frame (static/seconde-explosing-cat-removebg-preview.png).

The old frame was a blood splatter along the four edges: at 84 px it looked like a red square box.
This one is a radial pixel-art blood burst that continues the previous frame (orange core, rings gone)
and fades out before the edges, so nothing draws a frame.

Run: python tools/gen_explosion.py   (needs Pillow). Deterministic (fixed seed).
"""
import math
import random
from pathlib import Path

from PIL import Image, ImageDraw

GRID, SCALE = 100, 5          # drawn on a 100x100 pixel grid, upscaled x5 (nearest) = 500x500 like the other frames
DARK, BLOOD, RED, ORANGE, SPARK = (100, 0, 24), (150, 4, 30), (205, 18, 32), (255, 97, 13), (255, 190, 90)
OUT = Path(__file__).resolve().parent.parent / 'static' / 'seconde-explosing-cat-removebg-preview.png'


def burst(seed=7):
    rnd = random.Random(seed)
    im = Image.new('RGBA', (GRID, GRID), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    c = GRID / 2
    max_r = GRID / 2 - 3  # keep a transparent margin: no edge, no box
    # rays of blood, each ending in a droplet
    for k in range(26):
        a = 2 * math.pi * k / 26 + rnd.uniform(-0.12, 0.12)
        r0, r1 = rnd.uniform(6, 12), rnd.uniform(22, max_r - 4)
        w = rnd.choice((1, 1, 2, 2, 3))
        steps = int(r1 - r0)
        for i in range(steps):
            r = r0 + i
            x, y = round(c + r * math.cos(a)), round(c + r * math.sin(a))
            col = DARK if i % 7 == 0 else BLOOD if r > r1 * 0.7 else RED
            d.rectangle([x, y, x + w - 1, y + w - 1], fill=col)
            if rnd.random() < 0.12:  # side spatter
                sx, sy = x + rnd.randint(-2, 2), y + rnd.randint(-2, 2)
                d.point((sx, sy), fill=DARK)
        ex, ey = round(c + r1 * math.cos(a)), round(c + r1 * math.sin(a))
        s = rnd.choice((1, 2, 2, 3))
        d.rectangle([ex - s, ey - s, ex + s, ey + s], fill=DARK)
        d.rectangle([ex - s + 1, ey - s + 1, ex + s - 1, ey + s - 1], fill=BLOOD)
    # loose droplets, sparser towards the outside
    for _ in range(140):
        r = max_r * math.sqrt(rnd.random())
        a = rnd.uniform(0, 2 * math.pi)
        x, y = round(c + r * math.cos(a)), round(c + r * math.sin(a))
        if rnd.random() < 1 - r / max_r * 0.8:
            s = rnd.choice((0, 0, 1))
            d.rectangle([x, y, x + s, y + s], fill=rnd.choice((DARK, BLOOD, RED)))
    # central splat with the last orange sparks of the previous frame
    for _ in range(60):
        r, a = rnd.uniform(0, 9), rnd.uniform(0, 2 * math.pi)
        x, y = round(c + r * math.cos(a)), round(c + r * math.sin(a))
        d.rectangle([x - 1, y - 1, x + 1, y + 1], fill=rnd.choice((RED, BLOOD, DARK)))
    for _ in range(14):
        r, a = rnd.uniform(3, 16), rnd.uniform(0, 2 * math.pi)
        d.point((c + r * math.cos(a), c + r * math.sin(a)), fill=rnd.choice((ORANGE, SPARK)))
    return im.resize((GRID * SCALE, GRID * SCALE), Image.NEAREST)


if __name__ == '__main__':
    img = burst()
    a = img.getchannel('A')
    w, h = img.size
    edge = [a.getpixel((x, y)) for x in range(w) for y in (0, h - 1)] + [a.getpixel((x, y)) for y in range(h) for x in (0, w - 1)]
    assert not any(edge), 'the burst must not touch the edges (that is what looked like a box)'
    img.save(OUT, optimize=True)
    print('wrote', OUT)
