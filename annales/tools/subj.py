"""subj.py N_COR N_SUBJ 'Title' 'header line 2' 'header line 3': derive the subject file from a correction file
whose solutions are blockquote lines ('> ...')."""
import sys
S = __file__.rsplit("/", 1)[0]
nc, ns, title, h2, h3 = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4], sys.argv[5]
L = open(S + "/list.txt").read().split("\n")
src = open(f"{S}/out/{nc:03d}.md", encoding="utf-8").read().split("\n")
i = next(k for k, l in enumerate(src) if l.startswith("## "))
body = [l for l in src[i:] if not l.startswith(">")]
out, prev = [], None
for l in body:  # collapse blank runs left by removed solutions
    if l == "" and prev == "":
        continue
    out.append(l); prev = l
if len(sys.argv) > 6:  # points per exercise, ';'-separated
    pts = sys.argv[6].split(";"); k = 0
    for j, l in enumerate(out):
        if l.startswith("## "):
            out[j] = f"{l} ({pts[k]} points)"; k += 1
    assert k == len(pts), (k, len(pts))
head = [f"# {title}", "", f"- Source : `raw/{L[ns-1][2:]}` {h2}", f"- {h3}", ""]
open(f"{S}/out/{ns:03d}.md", "w", encoding="utf-8").write("\n".join(head + out).rstrip("\n") + "\n")
