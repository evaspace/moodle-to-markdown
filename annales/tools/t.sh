#!/bin/bash
# usage: t.sh N [N...] : print compact text layer of annale number N
S=$(cd "$(dirname "$0")" && pwd)
cd /opt/pierref/epitadoomscrolling/annales/raw || exit 1
for n in "$@"; do
  f=$(sed -n "${n}p" "$S/list.txt")
  echo "######## $n $f"
  python3 -I "$S/bx.py" "$f" | grep -v '^\s*$' | grep -v "^\.\.\.\.\.\.\.\." | grep -v "^Nom :\|^Prénom :\|^Classe :\|^[0-9]*$\|^---- page$"
done
