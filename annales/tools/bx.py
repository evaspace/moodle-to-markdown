"""Text layer with ^{..} / _{..} markers for small raised/lowered words.
Usage: python -I bx.py file.pdf  (reads pdftotext -bbox-layout output)."""
import html, re, subprocess, sys, statistics
xml = subprocess.run(["pdftotext", "-bbox-layout", sys.argv[1], "-"], capture_output=True, text=True).stdout
W = re.compile(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>')
SKIP = re.compile(r"^\.{8,}$|^[✬✫✤✣✩✪✜✢]$")
for page in xml.split("<page ")[1:]:
    for line in page.split("<line ")[1:]:
        ws = [(float(a), float(b), float(c), float(d), t) for a, b, c, d, t in W.findall(line)]
        ws = [w for w in ws if not SKIP.match(w[4])]
        if not ws:
            continue
        hs = [w[3] - w[1] for w in ws]
        H = statistics.median(hs)
        big = [w for w, h in zip(ws, hs) if h >= 0.85 * H] or ws
        base = statistics.median(w[3] for w in big)
        top = statistics.median(w[1] for w in big)
        out = []
        for w, h in zip(ws, hs):
            t = html.unescape(w[4])
            if h < 0.85 * H and w[3] < base - 0.2 * H:
                t = "^{" + t + "}"
            elif h < 0.85 * H and w[1] > top + 0.3 * H:
                t = "_{" + t + "}"
            out.append(t)
        s = " ".join(out)
        s = re.sub(r" (\^|_)\{", r"\1{", s)
        print(s)
    print("---- page")
