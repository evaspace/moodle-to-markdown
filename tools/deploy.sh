#!/usr/bin/env bash
# Put a commit online. The site is served from the live copy (git worktree, branch `live`), never from the dev folder,
# so work in progress cannot break it. Steps: offline tests on the commit in a throwaway worktree, move `live` to it
# (keeping the exam dates the cron added online), restart, wait for /healthz, roll back if the site does not answer.
# Usage: tools/deploy.sh [commit]   (default HEAD; uncommitted changes are never deployed)
set -euo pipefail

DEV=/opt/pierref/epitadoomscrolling
LIVE=/opt/pierref/epitadoomscrolling-live
APP=epitadoomscrolling_app
HEALTH=http://127.0.0.1:5117/healthz
CAL=parcours/syllabus.json
TESTS=(tests.test_levels tests.test_scroll tests.test_blog tests.test_exam_dates tests.test_admin_stats tests.test_beta tests.test_fiches)

sha=$(git -C "$DEV" rev-parse --verify "${1:-HEAD}^{commit}")
prev=$(git -C "$LIVE" rev-parse HEAD)
if [ "$sha" = "$prev" ]; then echo "Already online: $sha"; exit 0; fi

tmp=$(mktemp -d -p "${TMPDIR:-$HOME/.cache/tmp}")
cleanup() { git -C "$DEV" worktree remove --force "$tmp/wt" 2>/dev/null || true; rm -rf "$tmp"; }
trap cleanup EXIT

echo "Testing $(git -C "$DEV" log -1 --format='%h %s' "$sha")"
git -C "$DEV" worktree add -q --detach "$tmp/wt" "$sha"
(cd "$tmp/wt" && DB_PATH="$tmp/test.db" "$DEV/.venv/bin/python" -m unittest -q "${TESTS[@]}")

healthy() {
  for _ in $(seq 30); do
    curl -fsS -o /dev/null "$HEALTH" 2>/dev/null && return 0
    sleep 1
  done
  return 1
}

# The cron adds exam dates to the live copy between deploys: keep them across the checkout.
cp "$LIVE/$CAL" "$tmp/calendar.json"
switch_to() {
  git -C "$LIVE" checkout -q -- "$CAL"
  git -C "$LIVE" checkout -q -B live "$1"
  python3 - "$tmp/calendar.json" "$LIVE/$CAL" <<'EOF'
import json, sys
old = json.load(open(sys.argv[1], encoding='utf-8'))['calendrier']
path = sys.argv[2]
data = json.load(open(path, encoding='utf-8'))
key = lambda e: (e.get('debut'), e.get('titre'))
known = {key(e) for e in data['calendrier']}
added = [e for e in old if key(e) not in known]  # the commit wins on entries both have
if added:
    data['calendrier'] = sorted(data['calendrier'] + added, key=lambda e: e.get('debut', ''))
    open(path, 'w', encoding='utf-8').write(json.dumps(data, ensure_ascii=False, indent=1) + '\n')
print(f'{len(added)} exam date(s) kept from the live copy')
EOF
  docker restart "$APP" >/dev/null
}

switch_to "$sha"
if healthy; then
  echo "Online: $(git -C "$LIVE" log -1 --format='%h %s')"
else
  echo "Site not answering on $HEALTH: rolling back to ${prev:0:7}" >&2
  switch_to "$prev"
  if healthy; then echo "Rolled back, site answers again" >&2; else echo "Still down after rollback: docker logs $APP" >&2; fi
  exit 1
fi
