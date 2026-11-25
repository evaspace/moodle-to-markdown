"""Verify every answer of a level path with sympy, then write the JSON the app reads.

Usage: python parcours/build.py   (needs sympy; the web app itself does not)
Exit code 1 if any answer is wrong.
"""
import importlib
import json
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).parent
PATHS = ["bases_fractions", "bases_puissances", "bases_algebre", "bases_divisions", "bases_equations", "bases_sommes", "bases_exp_ln", "bases_trigo", "bases_derivees", "bases_limites",
         "obm", "dp", "apis_integrales", "apis_suites", "apis_edo",
         "apef_polynomes", "apef_fonctions", "ev", "alm", "phys_meca", "phys_thermo", "phys_em", "phys_energie", "archi_numeration", "archi_boole", "archi_circuits", "archi_sequentielle", "archi_micro", "elec_circuits", "elec_sinus", "elec_filtres", "elec_transitoires", "elec_diodes", "algo_taa", "algo_caml", "algo_python", "algo_matrices", "algo_abg", "algo_recherche", "prog_c_debut", "prog_minimake", "maths_s3_asn", "maths_s3_pse", "maths_s3_al", "phys_s3_quantique", "phys_s3_em", "elec_s3_transistors", "algo_s3_hachage", "algo_s3_arbres", "algo_s3_graphes", "algo_s3_thlr", "archi_s3_68000"]
x, t = sp.symbols("x t", real=True)
i, k = sp.symbols("i k", integer=True)
n = sp.symbols("n", integer=True, positive=True)


def _sym(s, base):
    """Value of a number written in `base` with an optional fractional part ('1011.01')."""
    whole, _, frac = s.replace(" ", "").partition(".")
    v = sp.Integer(int(whole or "0", base))
    return v + sum((sp.Rational(int(c, base), base ** (j + 1)) for j, c in enumerate(frac)), sp.Integer(0))


def _tc(s, n=None):
    """Two's complement value of a bit string."""
    s = s.replace(" ", "")
    return sp.Integer(int(s, 2) - (1 << len(s) if s[0] == "1" else 0))


def _f32(v):
    import struct
    return sp.Integer(struct.unpack(">I", struct.pack(">f", float(v)))[0])


def _f64(v):
    import struct
    return sp.Integer(struct.unpack(">Q", struct.pack(">d", float(v)))[0])


def _fdec(hexstr, fmt):
    import struct
    return sp.Rational(struct.unpack(fmt, bytes.fromhex(hexstr.replace(" ", "")))[0])


def _seq(kind, n, seq, exprs):
    """1 if the flip-flop inputs `exprs` drive the counter through `seq` (cyclic, unused states ignored).
    kind 'D': exprs = [D_{n-1}, ..., D_0]; kind 'JK': exprs = [J_{n-1}, K_{n-1}, ..., J_0, K_0]."""
    q = [sp.Symbol(f"Q{b}") for b in range(n)]
    exprs = [sp.sympify(e) for e in exprs]
    for i, m in enumerate(seq):
        nxt = seq[(i + 1) % len(seq)]
        env = {q[b]: bool((m >> b) & 1) for b in range(n)}
        for b in range(n - 1, -1, -1):
            j = n - 1 - b
            if kind == "D":
                got = bool(exprs[j].subs(env))
            else:
                jj, kk = bool(exprs[2 * j].subs(env)), bool(exprs[2 * j + 1].subs(env))
                got = (jj and not env[q[b]]) or (not kk and env[q[b]])
            if got != bool((nxt >> b) & 1):
                return sp.Integer(0)
    return sp.Integer(1)


def _eqv(a, b):
    from sympy.logic.boolalg import Xor, simplify_logic
    return sp.Integer(0 if sp.satisfiable(Xor(a, b)) else 1)


def _cover(expr, names, ones, dcs=()):
    """1 if expr is true on every minterm of `ones`, false outside ones+dcs (names: most significant first)."""
    syms = [sp.Symbol(c) for c in names]
    for m in range(1 << len(syms)):
        val = {s: bool((m >> (len(syms) - 1 - j)) & 1) for j, s in enumerate(syms)}
        got = bool(expr.subs(val))
        if m in ones and not got or m not in ones and m not in dcs and got:
            return sp.Integer(0)
    return sp.Integer(1)


def _parc(mode, adj, s=0, base=0):
    """Graph search for `calc`: adj[v - base] = successors of v (read in this order). Full search, first launch on s then
    on the unvisited vertices in increasing order. Row matrix of: bfs / dfs (prefix) / suf (suffix) order, dist (from s, -1 if
    unreachable), cc (component number of each vertex, 1-based)."""
    adj, s = [[int(y) - base for y in a] for a in adj], int(s) - base
    nv, seen, pre, suf, dist, cc = len(adj), set(), [], [], [-1] * len(adj), [0] * len(adj)

    def dfs(v, c):
        seen.add(v)
        pre.append(v)
        cc[v] = c
        for y in adj[v]:
            if y not in seen:
                dfs(y, c)
        suf.append(v)

    def bfs(v, c):
        seen.add(v)
        q, j = [v], 0
        dist[v], cc[v] = 0, c
        while j < len(q):
            for y in adj[q[j]]:
                if y not in seen:
                    seen.add(y)
                    dist[y], cc[y] = dist[q[j]] + 1, c
                    q.append(y)
            j += 1
        return q

    order, c = [], 0
    for v in [s] + ([] if mode == "dist" else list(range(nv))):
        if v not in seen:
            c += 1
            if mode in ("bfs", "dist"):
                order += bfs(v, c)
            else:
                dfs(v, c)
    res = {"bfs": order, "dfs": pre, "suf": suf, "dist": dist, "cc": cc}[mode]
    return sp.Matrix([[(y + base if mode in ("bfs", "dfs", "suf") else y) for y in res]])


def _hach(kind, m, hs, what, d=1, ds=None):
    """Hash table after inserting elements 1..n (hash values hs, in order). kind: lin (step d), dbl (steps ds), coal (no reserve), sep (tail insertion).
    what: tab/lien/len (Matrix row), pos (cell of the last element), probes (cells examined), coll, prim, sec, succ (comparisons to find every element), maxlen."""
    n, T, L, probes, prim, sec, coll = len(hs), [0] * m, [-1] * m, 0, 0, 0, 0
    lists = [[] for _ in range(m)]
    pos = None
    for e, h in enumerate(hs, 1):
        if kind == "sep":
            coll += bool(lists[h])
            lists[h].append(e)
        elif kind == "coal":
            if not T[h]:
                T[h], pos, probes = e, h, probes + 1
                continue
            coll += 1
            if hs[T[h] - 1] == h:
                prim += 1
            else:
                sec += 1
            c, probes = h, probes + 1
            while L[c] != -1:
                c, probes = L[c], probes + 1
            r = m - 1
            while T[r]:
                r -= 1
            T[r], L[c], pos = e, r, r
        else:
            step = d if kind == "lin" else ds[e - 1]
            for j in range(m):
                c = (h + step * j) % m
                probes += 1
                if not T[c]:
                    T[c], pos = e, c
                    break
                coll += j == 0
    if kind == "coal":  # position of each element in its collision list
        succ = 0
        for h in set(hs):
            c, k = h, 1
            while c != -1 and T[c]:
                succ += k * (hs[T[c] - 1] == h)
                c, k = L[c], k + 1
        probes = succ
    if kind == "sep":
        succ = sum(len(q) * (len(q) + 1) // 2 for q in lists)
    else:
        succ = probes
    res = {"tab": T, "lien": L, "len": [len(q) for q in lists]}
    if what in res:
        return sp.Matrix([res[what]])
    return sp.Integer({"pos": pos, "probes": probes, "coll": coll, "prim": prim, "sec": sec, "succ": succ,
                       "maxlen": max(len(q) for q in lists)}[what])


NS = {"hach": _hach, "parc": _parc, "x": x, "t": t, "E": sp.E, "pi": sp.pi, "log": sp.log, "sqrt": sp.sqrt,
      "exp": sp.exp, "sin": sp.sin, "cos": sp.cos, "tan": sp.tan, "atan": sp.atan,
      "Rational": sp.Rational, "i": i, "k": k, "binomial": sp.binomial,
      "factorial": sp.factorial, "summation": sp.summation,
      "n": n, "oo": sp.oo, "limit": sp.limit,
      "coef": lambda f, k: sp.series(f, x, 0, k + 1).removeO().coeff(x, k),  # coefficient of x^k of the DL of f at 0
      "bits": lambda s: _sym(s, 2), "hexa": lambda s: _sym(s, 16), "octal": lambda s: _sym(s, 8), "tc": _tc,
      "f32": _f32, "f32d": lambda h: _fdec(h, ">f"), "f64d": lambda h: _fdec(h, ">d"), "f64": _f64, "eqv": _eqv, "seqD": lambda n, sq, ex: _seq("D", n, list(sq), list(ex)), "seqJK": lambda n, sq, ex: _seq("JK", n, list(sq), list(ex)),
      "Q0": sp.Symbol("Q0"), "Q1": sp.Symbol("Q1"), "Q2": sp.Symbol("Q2"), "Q3": sp.Symbol("Q3"), "cover": _cover, "A": sp.Symbol("A"), "B": sp.Symbol("B"),
      "C": sp.Symbol("C"), "D": sp.Symbol("D"), "Xor": sp.Xor, "Not": sp.Not,
      "C1": sp.Symbol("C1"), "C2": sp.Symbol("C2"), "Y0": sp.Symbol("Y0"), "Y1": sp.Symbol("Y1"), "Y2": sp.Symbol("Y2")}
DUREE = {"derivative": 2, "primitive": 2, "integral": 5, "value": 4, "open": 5, "ode": 6}
SAMPLES = [sp.Rational(3, 10), sp.Rational(7, 10), sp.Rational(6, 5)]  # inside every domain used


def parse(s):
    return sp.sympify(sp.sympify(s, locals=NS))  # twice: a dict lookup such as roots(...)[a] gives a plain int


def close(a, b):
    if a.is_infinite or b.is_infinite:  # limits equal to +oo / -oo
        return a == b
    return abs(complex(sp.N(a - b, 30))) < 1e-12


def check(e):
    """Return None if the answer is right, else an error message."""
    if e["kind"] == "open":  # proof / course question: no automatic check, a model answer is required
        return None if e.get("sol") else "open exercise without sol"
    if e["kind"] == "value":  # counting / probability: the worked computation must equal the stated answer
        calc, ans = parse(e["calc"]), parse(e["ans"])
        if isinstance(calc, sp.MatrixBase):  # matrix answers (product, inverse, coordinates): exact equality
            return None if calc == ans else f"calc={calc.tolist()} expected {e['ans']}"
        syms = (calc - ans).free_symbols  # polynomial / expansion answers: compare at sample points
        if syms:
            bad = [p for p in SAMPLES if not close(calc.subs({s: p for s in syms}), ans.subs({s: p for s in syms}))]
            return None if not bad else f"mismatch at {bad}"
        return None if close(calc, ans) else f"calc={sp.N(calc)} expected {sp.N(ans)}"
    if e["kind"] == "ode":  # general solution f (constants C1, C2) plugged into lhs(Y0=y, Y1=y', Y2=y'') must give 0
        lhs, f = parse(e["lhs"]), parse(e["f"])
        order = max(int(str(s)[1]) for s in lhs.free_symbols if str(s) in ("Y0", "Y1", "Y2"))
        consts = {s for s in f.free_symbols if str(s) in ("C1", "C2")}
        if len(consts) != order:
            return f"{len(consts)} constants for an order {order} equation"
        res = lhs.subs({NS["Y0"]: f, NS["Y1"]: sp.diff(f, x), NS["Y2"]: sp.diff(f, x, 2)})
        res = res.subs({NS["C1"]: sp.Rational(7, 10), NS["C2"]: sp.Rational(-13, 10)})
        bad = [p for p in SAMPLES if not close(res.subs(x, p), sp.Integer(0))]
        return None if not bad else f"not a solution at {bad}"
    v = t if e.get("var") == "t" else x
    f, ans = parse(e["f"]), parse(e["ans"])
    if e["kind"] == "derivative":
        got = sp.diff(f, v)
    elif e["kind"] == "primitive":
        got, f, ans = sp.diff(ans, v), None, f  # F' must equal f
    elif e["kind"] == "integral":
        a, b = parse(e["a"]), parse(e["b"])
        val = sp.Integral(f, (v, a, b)).evalf(30)
        return None if close(val, ans) else f"integral={val} expected {sp.N(ans)}"
    else:
        return f"unknown kind {e['kind']}"
    bad = [p for p in SAMPLES if not close(got.subs(v, p), ans.subs(v, p))]
    return None if not bad else f"mismatch at {bad}"


PRIVATE = ("f", "a", "b", "var", "kind", "parts", "calc", "lhs")


def public(e):
    """Exercise as the web app sees it: no checking fields; variants keep only what is shown."""
    out = {k: v for k, v in e.items() if k not in PRIVATE}
    if "variants" in e:
        out["variants"] = [{k: v for k, v in x.items() if k not in PRIVATE} for x in e["variants"]]
    return out


def build(name):
    mod = importlib.import_module(f"src.{name}")
    by_id = {e["id"]: e for lvl in mod.LEVELS for e in lvl["exos"] if e["kind"] != "multi"}
    by_id.update({e["id"]: e for e in mod.EXTRA_PARTS})
    errors = []
    all_ids = [e["id"] for lvl in mod.LEVELS for e in lvl["exos"]] + [e["id"] for e in mod.EXTRA_PARTS]
    errors += [f"duplicate exercise id: {i}" for i in dict.fromkeys(all_ids) if all_ids.count(i) > 1]
    formules = getattr(mod, "FORMULES", {})  # per exercise: the formulas its solution uses
    errors += [f"FORMULES: unknown exercise {i}" for i in formules if i not in by_id]
    copies = getattr(mod, "COPIES", {})  # per exercise: the 20/20 student copy (optional, path by path)
    errors += [f"COPIES: unknown exercise {i}" for i in copies if i not in by_id]
    for e in by_id.values():
        if e["id"] not in formules:
            errors.append(f"{e['id']}: no entry in FORMULES")
        e["formules"] = formules.get(e["id"], "")
        if e["id"] in copies:
            e["copie"] = copies[e["id"]]
        # variants: same formula, other numbers; each one is checked like the exercise itself
        for i, x in enumerate([e] + [e | v for v in e.get("variants", [])]):
            err = check(x)
            if err:
                errors.append(f"{e['id']}{f' variant {i}' if i else ''}: {err}")
    for lvl in mod.LEVELS:
        assert len(lvl["exos"]) >= 3, f"level {lvl['n']} needs >= 3 exercises (3 in a row to pass)"
        for e in lvl["exos"]:
            if e["kind"] == "multi":
                missing = [p for p in e["parts"] if p not in by_id]
                if missing:
                    errors.append(f"{e['id']}: missing parts {missing}")
                    continue
                e["sol"] = "\n\n".join(f"**{i}.** {by_id[p]['sol']}" for i, p in enumerate(e["parts"], 1))
                parts = [f.strip() for p in e["parts"] for f in by_id[p]["formules"].split(" · ")]
                e["formules"] = " · ".join(dict.fromkeys(parts))  # union of the parts, first occurrence order
                if all("copie" in by_id[p] for p in e["parts"]):
                    e["copie"] = "\n".join(f"**{i}.** {by_id[p]['copie']}" for i, p in enumerate(e["parts"], 1))
    notion_ids = {n["id"] for n in mod.NOTIONS}
    for lvl in mod.LEVELS:
        errors += [f"level {lvl['n']}: unknown notion {n}" for n in lvl["notions"] if n not in notion_ids]
    errors += [f"quiz: unknown notion {q['notion']}" for q in mod.QUIZ if q["notion"] not in notion_ids]
    if errors:
        print("\n".join(errors))
        return False
    for lvl in mod.LEVELS:
        for e in lvl["exos"]:
            # minutes of forced solo thinking before the correction (README_OBJECTIFS: chrono)
            e.setdefault("duree", 5 * len(e["parts"]) if e["kind"] == "multi" else DUREE[e["kind"]])
    out = {"subject": mod.SUBJECT, "notions": mod.NOTIONS, "quiz": mod.QUIZ,
           "levels": [{**lvl, "exos": [public(e) | {"type": e["kind"]} for e in lvl["exos"]]} for lvl in mod.LEVELS]}
    (HERE / f"{name}.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
    n = sum(len(lvl["exos"]) for lvl in mod.LEVELS)
    print(f"{name}: OK, {len(mod.LEVELS)} levels, {n} exercises, {len(mod.NOTIONS)} notions, {len(mod.QUIZ)} quiz")
    return True


def check_syllabus():
    """Every link of parcours/syllabus.json must resolve: Moodle chapters, past exams, level paths."""
    syl = json.loads((HERE / "syllabus.json").read_text(encoding="utf-8"))
    root = HERE.parent
    errors, listed, skipped = [], {}, set()
    for mat in syl["matieres"]:
        for sem in mat["semestres"]:
            moodle = root / syl["moodle_root"] / sem["moodle"]
            # Course and exam folders are git-ignored: a contributor only has the semesters they work on.
            # A missing folder is skipped with a notice; a missing file inside a present folder is an error.
            if not moodle.is_dir():
                skipped.add(f"{syl['moodle_root']}/{sem['moodle']}")
            for ecue in sem["ecues"]:
                where = f"{sem['id']} {ecue['id']}"
                if moodle.is_dir():
                    errors += [f"{where}: Moodle chapter not found: {c}" for c in ecue["chapitres"] if not (moodle / c).is_dir()]
                for a in ecue["annales"]:
                    if (root / syl["annales_root"] / a.split("/")[0]).is_dir():
                        if not (root / syl["annales_root"] / a).is_file():
                            errors.append(f"{where}: past exam not found: {a}")
                    else:
                        skipped.add(f"{syl['annales_root']}/{a.split('/')[0]}")
                for pid in ecue["parcours"]:
                    listed[pid] = (ecue, sem["id"])
    built = {}
    for name in PATHS:
        mod = importlib.import_module(f"src.{name}")
        built[mod.SUBJECT["id"]] = mod.SUBJECT
    for pid, (ecue, sem) in listed.items():
        subj = built.get(pid)
        if not subj:
            errors.append(f"syllabus lists level path {pid}, not built (add it to PATHS)")
            continue
        if (subj["ecue"], subj["semestre"]) != (ecue["id"], sem):
            errors.append(f"{pid}: ECUE/semester differs from syllabus")
        errors += [f"{pid}: Moodle chapter not in syllabus ECUE: {c}" for c in subj["chapitres_moodle"]
                   if not any(x == c or x.endswith("/" + c) for x in ecue["chapitres"])]
    errors += [f"level path {pid} missing from syllabus.json" for pid in built if pid not in listed]
    for s in sorted(skipped):
        print(f"syllabus: not checked, folder absent locally: {s}")
    if errors:
        print("\n".join(errors))
        return False
    print(f"syllabus: OK, {len(listed)} level paths linked")
    return True


if __name__ == "__main__":
    sys.path.insert(0, str(HERE))
    ok = all([build(p) for p in PATHS])  # build every path even if one fails
    sys.path.insert(0, str(HERE.parent / "annales" / "tools"))
    for line in __import__("baremes").warn_missing():  # PLAN_BETA étape 4: nearest exam first
        print("Avertissement copie 20/20 :", line)
    sys.exit(0 if ok and check_syllabus() else 1)
