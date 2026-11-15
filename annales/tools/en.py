"""en.py N_EN N_FR 'Title' 'kind text': write out/N_EN.md as an English-version note of out/N_FR.md (same exercises, types kept)."""
import sys, re
S = __file__.rsplit("/", 1)[0]
ne, nf, title, kind = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4]
L = open(S + "/list.txt").read().split("\n")
fr = open(f"{S}/out/{nf:03d}.md", encoding="utf-8").read().split("\n")
date = next(l for l in fr if l.startswith("- Date réelle"))
date = date.split(". Corrigé")[0].split(". Sujet")[0].rstrip(".")
out = [f"# {title}", "", f"- Source : `raw/{L[ne-1][2:]}` ({kind})",
       f"{date}. Version anglaise de `{L[nf-1][2:].rsplit('/',1)[1][:-4]}.md` : mêmes exercices, mêmes données ; se reporter à la version française.", ""]
for i, l in enumerate(fr):
    if l.startswith("## "):
        out += [l.replace("Exercice", "Exercise"), fr[i + 1], ""]
open(f"{S}/out/{ne:03d}.md", "w", encoding="utf-8").write("\n".join(out))
