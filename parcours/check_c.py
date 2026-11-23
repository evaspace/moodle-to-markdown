"""Compile and run every C program of the C level paths (prog_c_debut, prog_minimake) and compare the output.

build.py cannot run C: run this after any change to those files. One throwaway Alpine container
(`apk add gcc musl-dev`), each program compiled with `gcc -std=c99 -w` and run with a 5 s timeout; whitespace collapsed.

    python3 parcours/check_c.py
"""
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from src import prog_c_debut, prog_minimake  # noqa: E402

CHECKS = prog_c_debut.CHECKS + prog_minimake.CHECKS


def norm(text):
    return " ".join(text.split())


def main():
    with tempfile.TemporaryDirectory() as tmp:
        for i, (code, _) in enumerate(CHECKS):
            Path(tmp, f"{i:03}.c").write_text(code)
        script = ("apk add -q gcc musl-dev >/dev/null 2>&1 && cd /w && for f in *.c; do b=${f%.c}; "
                  "gcc -std=c99 -w -o $b.bin $f > $b.out 2>&1 && timeout 5 ./$b.bin >> $b.out 2>&1; done")
        subprocess.run(["docker", "run", "--rm", "-v", f"{tmp}:/w", "alpine:3.20", "sh", "-c", script], check=True)
        bad = 0
        for i, (code, ans) in enumerate(CHECKS):
            got = Path(tmp, f"{i:03}.out").read_text()
            if norm(got) != norm(ans):
                bad += 1
                print(f"--- check {i}\n{code}\n--- expected\n{ans}\n--- got\n{got.strip()}\n")
    print(f"{len(CHECKS) - bad}/{len(CHECKS)} C checks OK")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
