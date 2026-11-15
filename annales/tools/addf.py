"""Install out/NNN.md into annales/md, inserting 'Formules : ...' after each 'Type : X · ...' line of scratchpad/out/*.md.
Usage: python addf.py SCRATCH  -> lists types missing from formules.F (exit 1 if any)."""
import sys, glob, re, importlib.util
S = sys.argv[1]
spec = importlib.util.spec_from_file_location("formules", S + "/formules.py")
mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
missing = set()
for p in sorted(glob.glob(S + "/out/*.md")):
    lines = open(p, encoding="utf-8").read().split("\n")
    out = []
    for i, l in enumerate(lines):
        out.append(l)
        m = re.match(r"Type : (.*?) · ECUE", l)
        if not m:
            continue
        if i + 1 < len(lines) and lines[i + 1].startswith("Formules :"):
            continue
        t = m.group(1)
        if t in mod.F:
            out.append("Formules : " + mod.F[t])
        else:
            missing.add(t)
    n = int(p.rsplit("/", 1)[1][:3])
    src = open(S + "/list.txt").read().split("\n")[n - 1][2:]
    dst = "/opt/pierref/epitadoomscrolling/annales/md/" + src[:-4] + ".md"
    open(dst, "w", encoding="utf-8").write("\n".join(out).rstrip("\n") + "\n")
for t in sorted(missing):
    print("MISSING:", t)
sys.exit(1 if missing else 0)
