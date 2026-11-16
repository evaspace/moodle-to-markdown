"""Replay every Caml phrase of parcours/src/algo_caml.py in a real OCaml toplevel and compare the answers.

build.py cannot run OCaml (not installed on the server, not in the app image): run this after any change to
algo_caml.py. It starts one throwaway Alpine container (`apk add ocaml`, OCaml 4.14), runs each check in its own
toplevel with warnings off, and compares the answers with whitespace collapsed (long values wrap in the toplevel).

    python3 parcours/check_caml.py
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from src.algo_caml import CHECKS  # noqa: E402

NOISE = re.compile(r"^(OCaml version|Enter #help|The OCaml toplevel|Line \d+|Characters \d+|\s*\d+ \||\s*\^+\s*$)")


def norm(text):
    lines = [x for x in text.splitlines() if x.strip() and not NOISE.match(x)]
    return " ".join(" ".join(lines).split())


def main():
    with tempfile.TemporaryDirectory() as tmp:
        for i, (code, _) in enumerate(CHECKS):
            Path(tmp, f"{i:03}.ml").write_text(code + "\n")
        script = ("apk add -q ocaml >/dev/null 2>&1 && for f in /w/*.ml; do "
                  "ocaml -w -a -color=never -noprompt -nopromptcont < $f > ${f%.ml}.out 2>&1; done")
        subprocess.run(["docker", "run", "--rm", "-v", f"{tmp}:/w", "alpine:3.20", "sh", "-c", script], check=True)
        bad = 0
        for i, (code, ans) in enumerate(CHECKS):
            got = Path(tmp, f"{i:03}.out").read_text()
            if norm(got) != norm(ans):
                bad += 1
                print(f"--- check {i}\n{code}\n--- expected\n{ans}\n--- OCaml\n{got.strip()}\n")
    print(f"{len(CHECKS) - bad}/{len(CHECKS)} Caml checks OK")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
