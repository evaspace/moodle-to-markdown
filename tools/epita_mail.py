#!/usr/bin/env python3
"""Read the EPITA mailbox (Microsoft 365) over IMAP with OAuth2, to find exam dates in the mails.

Microsoft 365 refuses IMAP with a password; it accepts OAuth2. We use Thunderbird's public client id
(the same login screen as adding the account in Thunderbird), so no app has to be registered at EPITA.

One-time login, from any terminal on the server (the browser can be on another machine):
    .venv/bin/python tools/epita_mail.py login
    -> open the printed link, sign in with the EPITA account, accept;
    -> the browser ends on a page that does not load (https://localhost/?code=...): copy that whole
       address from the address bar and paste it in the terminal.
The refresh token is saved in ~/.config/epita-mail/token.json (mode 600) and renewed on each use;
it stays valid as long as it is used at least every 90 days (the cron uses it twice a day).

Check:  .venv/bin/python tools/epita_mail.py check   # number of mails in INBOX
"""
import base64
import hashlib
import imaplib
import json
import os
import secrets
import sys
import urllib.parse
import urllib.request
from pathlib import Path

CLIENT_ID = '9e5f94bc-e8a4-4e73-b8be-63364c29d753'  # Thunderbird (Mozilla), public client
REDIRECT = 'https://localhost'
SCOPE = 'https://outlook.office.com/IMAP.AccessAsUser.All offline_access'
AUTH = 'https://login.microsoftonline.com/organizations/oauth2/v2.0/'
HOST = 'outlook.office365.com'
TOKEN = Path.home() / '.config' / 'epita-mail' / 'token.json'


def _post(data):
    req = urllib.request.Request(AUTH + 'token', urllib.parse.urlencode(data).encode())
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        err = json.load(e)
        sys.exit(f"Microsoft refuse : {err.get('error')} : {err.get('error_description', '').splitlines()[0]}")


def _save(tok, user=None):
    old = json.loads(TOKEN.read_text()) if TOKEN.exists() else {}
    TOKEN.parent.mkdir(parents=True, exist_ok=True)
    TOKEN.touch(mode=0o600)
    TOKEN.write_text(json.dumps({'refresh_token': tok['refresh_token'], 'user': user or old.get('user')}))


def login():
    user = input('Adresse EPITA (ex. prenom.nom@epita.fr) : ').strip()
    verifier = secrets.token_urlsafe(64)
    challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).rstrip(b'=').decode()
    state = secrets.token_urlsafe(16)
    url = AUTH + 'authorize?' + urllib.parse.urlencode({
        'client_id': CLIENT_ID, 'response_type': 'code', 'redirect_uri': REDIRECT, 'scope': SCOPE,
        'login_hint': user, 'state': state, 'code_challenge': challenge, 'code_challenge_method': 'S256'})
    print('\n1. Ouvre ce lien dans ton navigateur et connecte-toi :\n\n' + url +
          '\n\n2. La page finale ne charge pas (https://localhost/?code=...) : copie son adresse complète.\n')
    back = urllib.parse.parse_qs(urllib.parse.urlparse(input('Adresse de la page finale : ').strip()).query)
    if 'error' in back:
        sys.exit(f"Refusé : {back['error'][0]} : {back.get('error_description', [''])[0]}")
    if back.get('state', [''])[0] != state or 'code' not in back:
        sys.exit("Adresse invalide : copie toute l'adresse de la page finale (elle contient code= et state=).")
    tok = _post({'client_id': CLIENT_ID, 'grant_type': 'authorization_code', 'code': back['code'][0],
                 'redirect_uri': REDIRECT, 'code_verifier': verifier, 'scope': SCOPE})
    _save(tok, user)
    print(f'Connecté. Jeton enregistré dans {TOKEN} (lisible par toi seul).')


def imap():
    """Logged-in IMAP connection; renews and saves the refresh token."""
    if not TOKEN.exists():
        sys.exit('Pas de jeton : lance d\'abord  .venv/bin/python tools/epita_mail.py login')
    saved = json.loads(TOKEN.read_text())
    tok = _post({'client_id': CLIENT_ID, 'grant_type': 'refresh_token', 'refresh_token': saved['refresh_token'],
                 'scope': SCOPE})
    _save(tok)
    conn = imaplib.IMAP4_SSL(HOST)
    auth = f"user={saved['user']}\x01auth=Bearer {tok['access_token']}\x01\x01"
    conn.authenticate('XOAUTH2', lambda _: auth.encode())
    return conn


def check():
    conn = imap()
    typ, data = conn.select('INBOX', readonly=True)
    print(f'OK : {int(data[0])} mails dans INBOX.')
    conn.logout()


if __name__ == '__main__':
    os.umask(0o077)
    {'login': login, 'check': check}.get(sys.argv[1] if len(sys.argv) > 1 else '', lambda: sys.exit(__doc__))()
