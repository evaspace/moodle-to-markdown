"""Build annales/INDEX.md and annales/FORMULES.md from annales/md/**/*.md and tools/formules.py.
Usage: python3 tools/index.py   (run from anywhere; fails if a Type has no formulas or a level id is unknown)."""
import glob, importlib.util, json, os, re, sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("formules", ROOT + "/tools/formules.py")
mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)

# level ids -> number of levels, from the built paths
levels = {}
for p in glob.glob(ROOT + "/../parcours/*.json"):
    d = json.load(open(p, encoding="utf-8"))
    if isinstance(d, dict) and "levels" in d:
        levels[d["subject"]["id"]] = len(d["levels"])

TYPE = re.compile(r"Type : (.*?) · ECUE : (.*?)(?: · Niveau : (\S+))?$")
KIND = {"Finals": "Partiels (finals)", "Midterms": "Contrôles (midterms)", "TDs": "Contrôles de TD et feuilles de TD", "MCQs": "QCM"}
files = sorted(glob.glob(ROOT + "/md/**/*.md", recursive=True))
errors, by_ecue, n_ex = [], defaultdict(lambda: defaultdict(int)), 0
out = ["# Index des annales (maths et physique)", "",
       f"{len(files)} fichiers transcrits depuis `annales/raw/` (dépôt Epidocs/Past-Exams). Généré par `tools/index.py` : ne pas modifier à la main.",
       "Le dossier « promo » est l'année de diplôme ; la date réelle de l'épreuve est indiquée pour chaque fichier.",
       "Niveau = identifiant du parcours et numéro du niveau dans l'application (— : type sans niveau dédié, par exemple les révisions de lycée ou le hors programme).", ""]
cur = None
for f in files:
    rel = os.path.relpath(f, ROOT + "/md")
    parts = rel.split(os.sep)
    head = (parts[0], parts[1])
    if head != cur:
        cur = head
        out += [f"## {parts[0]} — {KIND.get(parts[1], parts[1])}", ""]
    lines = open(f, encoding="utf-8").read().split("\n")
    title = lines[0].lstrip("# ").strip()
    date = next((l.split("Date réelle :", 1)[1].strip() for l in lines if "Date réelle :" in l), "")
    date = re.split(r" \(|\. ", date)[0].rstrip(".")
    out += [f"### {title}", "", f"`md/{rel}` — date réelle : {date or 'non indiquée'}", "",
            "| Exercice | Type | ECUE | Niveau |", "|---|---|---|---|"]
    for i, l in enumerate(lines):
        if not l.startswith("## "):
            continue
        m = TYPE.match(lines[i + 1]) if i + 1 < len(lines) else None
        if not m:
            errors.append(f"{rel}: no Type line after '{l}'"); continue
        t, ecue, niv = m.groups()
        if t not in mod.F:
            errors.append(f"{rel}: type without formulas: {t}")
        if not (i + 2 < len(lines) and lines[i + 2].startswith("Formules :")):
            errors.append(f"{rel}: no Formules line after '{l}'")
        if niv:
            slug, _, k = niv.partition("/")
            if slug not in levels or not k.isdigit() or not 1 <= int(k) <= levels[slug]:
                errors.append(f"{rel}: unknown level {niv}")
        n_ex += 1
        by_ecue[ecue][t] += 1
        out.append(f"| {l[3:]} | {t.replace('|', chr(92) + '|')} | {ecue} | {niv or '—'} |")
    out.append("")
if errors:
    print("\n".join(errors)); sys.exit(1)
out[2] += f" {n_ex} exercices."
open(ROOT + "/INDEX.md", "w", encoding="utf-8").write("\n".join(out))

ORDER = ["Mécanique", "Thermodynamique", "Électromagnétisme", "OBM", "DP", "APIS (intégrales)", "APIS (suites)", "APIS (EDO)", "APEF (fonctions)", "APEF (polynômes)", "EV", "ALM"]
fo = ["# Fiche synthèse des formules (maths et physique)", "",
      "Toutes les formules utilisées pour résoudre les exercices des annales, par ECUE puis par type d'exercice.",
      "Entre parenthèses : nombre d'exercices d'annales de ce type. Généré par `tools/index.py` depuis `tools/formules.py` : ne pas modifier à la main.", ""]
for ecue in ORDER + sorted(e for e in by_ecue if e not in ORDER):
    if ecue not in by_ecue:
        continue
    fo += [f"## {ecue}", ""]
    for t, n in sorted(by_ecue[ecue].items(), key=lambda kv: -kv[1]):
        fo.append(f"**{t}** ({n})")
        fo.append("")
        fo += [f"- {x.strip()}" for x in mod.F[t].split(" ; ")]
        fo.append("")
open(ROOT + "/FORMULES.md", "w", encoding="utf-8").write("\n".join(fo))
print(f"{len(files)} files, {n_ex} exercises, {sum(len(v) for v in by_ecue.values())} (ECUE, type) pairs")
