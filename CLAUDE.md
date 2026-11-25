# EPITA Doomscrolling

Revision app for EPITA prépa (Flask + SQLite). S1/S2 content is done; S3/S4 (spé) is being added by a second contributor.

- Adding S3/S4 content: follow [CONTRIBUER_S3_S4.md](CONTRIBUER_S3_S4.md) step by step. It is the spec.
- Product rules and the owner's decisions: [README_OBJECTIFS.md](README_OBJECTIFS.md). Technical reference: [README.md](README.md), section « Levels mode ».
- Course files (`EPITA_Moodle_Notes_MD/`) and exam PDFs (`annales/raw/`) are git-ignored: never commit them, the repo is public.
- Never commit on `main` or `dev`: one branch per ECUE from `dev`, pull request to `dev`. No AI/assistant mention in commits, branches or PRs.
- Before saying a path is done: `parcours/build.py` (needs sympy), `annales/tools/index.py` and the offline tests listed in the guide must pass. Never run `unittest discover` (it calls a paid API).
- Deploy (owner's rule, 2026-11-22): the site runs from the live copy `/opt/pierref/epitadoomscrolling-live` (branch `live`), not from this folder, so edits here never reach users by themselves. Deploy only once, at the end of a task, with `tools/deploy.sh [commit]` (tests, restart, health check, automatic rollback); a very quick fix (a line or two) may be deployed right away, still with the script. Never `docker restart` the app or edit the live copy by hand.
- Public changelog (owner's rule, 2026-11-25): every change a user can see (content, page, fix) gets one line in French in [NOUVEAUTES.md](NOUVEAUTES.md), under the date of the deploy, newest first, written for students (no commit jargon). Do it in the same commit, without being asked. Served at `/nouveautes`, linked from the footer.
