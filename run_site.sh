#!/usr/bin/env bash
# Lance le site en local (réseau privé) : gunicorn sur le port 5000. Base dans data/site.db, mot de passe admin dans ~/.cache/site_admin_password.
set -u
cd "$(dirname "$0")" || exit 1
ADMIN_PASSWORD="$(cat "$HOME/.cache/site_admin_password")"
export DB_PATH="$PWD/data/site.db" COOKIE_INSECURE=1 ADMIN_PASSWORD
exec .venv/bin/gunicorn -b 0.0.0.0:5000 -w 2 --access-logfile - app:app
