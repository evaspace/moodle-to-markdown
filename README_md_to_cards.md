# md_to_cards.py — Convertisseur Markdown EPITA → cartes MathsDoomscroll

Convertit les Markdown locaux (`EPITA_Moodle_Notes_MD/`, **jamais envoyés
au serveur**) en blocs de cartes au format texte interprété par
`parse_blocks()` (`app.py:71`). L'application ne lit **aucun JSON** de
cartes ; le LaTeX reste en texte brut (`$…$`, `$$…$$`).

## Pipeline en 3 passes

| Passe | Rôle | Tokens |
|---|---|---|
| **A** | Normalisation `[mathjaxinline]X[/mathjaxinline]` → `$X$`, `[mathjax]X[/mathjax]` → `$$X$$` (`md_converter.normalize_mathjax_tags`) | 0 |
| **B** | Extraction QCM réels depuis `qcms/*.md` — **questions à note PLEINE uniquement** (à note partielle/nulle, `[x]` = réponse de l'élève, pas la correction → rejet) | 0 |
| **C** | Cartes COURSE par chapitre : existence via index **lecture seule** du serveur, front déterministe `Chapitre : <titre>`, résumé (R:) sémantique → LLM | LLM |
| **D** | **QCM/TF d'entraînement** : génère des questions **conceptuelles** (raisonner, appliquer, analyser) pour les chapitres avec COURSE mais sans QCM | LLM |

## Commandes exactes

```bash
# Tests (62 tests, unittest — aucune dépendance ajoutée)
.venv/bin/python -m unittest tests.test_md_to_cards -v

# Analyse complète sans rien écrire (recommandé en premier)
.venv/bin/python md_to_cards.py --dry-run --only-pass b
.venv/bin/python md_to_cards.py --dry-run --only-pass c
.venv/bin/python md_to_cards.py --dry-run --only-pass d

# Lot limité réel (écrit Generated_QCMs/*.txt localement)
.venv/bin/python md_to_cards.py --only "10_Cours 3 - Arithmétique" --only-pass b
.venv/bin/python md_to_cards.py --limit 20 --only-pass b

# Reprise après interruption / échecs
.venv/bin/python md_to_cards.py --retry-failed --only-pass b
.venv/bin/python md_to_cards.py --force --only "S2-MATHS-2030" --only-pass b

# Passe C avec LLM — UNIQUEMENT après validation du tier gratuit (§ Coût)
.venv/bin/python md_to_cards.py --only-pass c --allow-llm

# Passe D — QCM d'entraînement conceptuels (chaps sans QCM)
.venv/bin/python md_to_cards.py --only-pass d --allow-llm --pass-d-limit 5
```

Options : `--limit N`, `--only SUBSTR`, `--retry-failed`, `--force`,
`--dry-run`, `--only-pass abcd`, `--allow-llm`, `--offline` (index local),
`--refresh-index`, `--tracker PATH`, `--pass-c-limit N`, `--pass-d-limit N`.

## Règles métier déterministes (Passe B)

- Un fichier `qcms/*.md` est un vrai QCM ssi `### Question N (Note …)` **et**
  lignes `- [x]/- [ ]` sont présents ; sinon **SKIPPED** (stub de métadonnées
  ou questions ouvertes).
- **Note pleine** (`Note de X,X0 sur X,X0`) : les options cochées `[x]` sont
  la bonne réponse. **Note partielle, nulle ou « Non noté »** : `[x]` est la
  réponse *sélectionnée* par l'élève — la question est **REJETÉE** (jamais
  publiée avec une fausse « bonne réponse »), et devient candidate LLM.
- Chaque option est exportée 3× (label « a. » ×2 + sans label) : déduplication
  sur le texte après retrait du label, `[x]` combiné (OU).
- ≥ 2 choix distincts non vides et ≥ 1 `[x]` requis, sinon rejet.
- Corrections : lignes administratives retirées (`Correct`, `Note pour cet
  envoi : …`, `Votre réponse est correcte.`, …).
- **Dédup (type, front)** avant déploiement : doublon exact (même énoncé,
  correction, choix, chapitre) → rejeté ; deux questions *distinctes* partageant
  un front → suffixe déterministe `[Q<n>·<hash6>]` (aucune n'est perdue).
- Chaque `.txt` généré est validé avec le vrai `parse_blocks()` : tout bloc en
  erreur est rejeté, jamais déployé.

## Catégories canoniques

`selected_courses.json` mappe `source_folder → category_name`, mais plusieurs
ECUE partagent un dossier (ex. `S1-MATHS-2030` = OBM+DP+ARITH+SR). Pour ceux-
ci, `SYLLABUS_ORGANISATION.md` fournit la table chapitre → ECUE :

```
S1-MATHS-2030/10_Cours 3 - Arithmétique  →  CAT: Maths S1 - ARITH / Cours 3 - Arithmétique
S2-MATHS-2030/07_Cours 3 - Espaces vectoriels  →  CAT: Maths S2 - EV / Cours 3 - Espaces vectoriels
```

## Suivi / reprise

`md_to_cards_progress.json` (gitignore) : `DONE` / `SKIPPED` / `REJECTED` /
`FAILED` par fichier et `SKIPPED_EXISTS` / `NO_CONTENT` / `PENDING_LLM` /
`GENERATED` / `FAILED` par chapitre (clé stable du chemin, normalisée).
Sauvegarde atomique après chaque fichier — une interruption ne retraite rien.

## Coût zéro (contrainte absolue)

- **Aucun appel LLM sans `--allow-llm`**, et toujours un `--dry-run` d'abord.
- **Aucun modèle Mistral n'est gratuit** : la documentation officielle
  (docs.mistral.ai/inference/pricing, 2026-10-13) liste tous les modèles
  comme payants au volume. Le "tier gratuit Experiment" auquel le projet
  faisait référence n'est plus mentionné dans les prix publiques. Ne pas
  utiliser `open-mistral-7b` (modèle payant, ~0.15/0.60 $).
- Modèles validés sur la clé API Experiment (testé 2026-10-13) — par coût croissant :
  - `open-mistral-nemo-2407` : $0.15 / $0.15  (32K ctx, 7B, open-weight, **fonctionne**)
  - `mistral-small-latest` : $0.15 / $0.60  (32K ctx, 24B, mais 429 fréquent)
  - `mistral-medium-latest` : $1.50 / $7.50 (32K ctx, mais 429 fréquent)
  - Les modèles récents (ministral-3-*, codestral-25-08, mistral-large-3)
    retournent HTTP 400 "Invalid model" — **non disponibles** pour cette clé.
- Coût estimé pour 281 chapitres : ~€0.16 (nemo 2407 seulement).
- Alternative zéro coût : `LLM_PROVIDER=ollama` (local, mais nécessite Ollama +
  un modèle téléchargé — aucune installation automatique).
- Gemini API : tier gratuit possible pour certains modèles, mais vérifier
  le quota avant usage.

## Passe C v2 — rotation de modèles + vérification + checkpoint

Pass C génère des cartes COURSE par chapitre avec :

1. **Rotation stricte 1 modèle/chapitre** (`ModelRotator`) : le même modèle
   est utilisé pour toutes les cartes d'un chapitre, le suivant au chapitre
   suivant. Triée par coût croissant :
   `ministral-3-3b → ministral-3-14b → codestral → mistral-large-3`.
2. **Modèle de vérification distinct** (`DEFAULT_VERIFY_MODEL`) : toujours
   différent du modèle de génération courant. Vérifie le lot entier du
   chapitre en **un seul appel** (batch). Si la vérif échoue → FAILED.
   Si la vérif a 429 → on garde la carte (parse_blocks a déjà validé).
3. **429 fallback** : sur un rate-limit, passe au modèle suivant dans la
   rotation (max 2 fallbacks). Si tous les modèles sont en 429 →
   `RateLimitError` → **checkpoint FAILED** (reprise avec `--retry-failed`).
   **Aucun retry-loop** : 429 = changement de modèle OU checkpoint.
4. **Rate limiting** : délai safe de 0.5s entre appels (60 % des limites
   publiques). Configurable via `MISTRAL_DELAY` / `MISTRAL_VERIFY_DELAY`.
5. **Clé API multiples** : `MISTRAL_API_KEY_2` (clé dédiée, priorité haute)
   + `MISTRAL_API_KEY` (existante). Rotation automatique en cas de
   rate-limit global.
6. **Reprise** : `md_to_cards_progress.json` checkpointe chaque chapitre.
   `--retry-failed` relance uniquement les FAILED (rate-limit). `--force`
   regénère tout.

### Alias de modèles

Les noms proposés par l'utilisateur sont résolus vers les IDs API valides
via `MISTRAL_MODEL_ALIASES` :

| Alias utilisateur       | ID API valide          |
|---|---|
| `mistral-large-2512`    | `mistral-large-2411`    |
| `codestral-2508`        | `codestral-2405`          |
| `ministral-14b-2512`    | `open-mistral-nemo-2407` (résolu — modèle récent non dispo)    |
| `ministral-8b-2512`     | `open-mistral-nemo-2407` (résolu — modèle récent non dispo)     |
| `mistral-medium-latest` | `mistral-medium-latest`      |

```bash
# Pass C avec rotation + vérification (dry-run d'abord, toujours)
.env/bin/python md_to_cards.py --dry-run --only-pass c
.env/bin/python md_to_cards.py --only-pass c --allow-llm
.env/bin/python md_to_cards.py --only-pass c --allow-llm --pass-c-limit 5
.env/bin/python md_to_cards.py --only-pass c --allow-llm --retry-failed

# Pass D — QCM d'entraînement conceptuels (chaps sans QCM existant)
.env/bin/python md_to_cards.py --only-pass d --allow-llm --pass-d-limit 5
```

### Pass D — QCM d'entraînement

La Pass D génère des **questions de compréhension concrète** (raisonner, appliquer,
analyser) pour les chapitres qui ont des cartes COURSE mais **aucun QCM**.

Le `SYSTEM_PROMPT_QCM` exige :
- Au moins 2 QCM par bloc (4 choix, 1 juste)
- 1-2 Vrai/Faux par bloc
- Pas de questions factuelles simples (pas de "calculer le PGCD de 12342")
- Questions de niveau difficile : application, analyse, synthèse

Même infrastructure de rotation/429/fallback/verification que la Pass C.

## Déploiement (après feu vert)

```bash
df -h /opt                                                    # espace serveur
rsync --dry-run -av --delete Generated_QCMs/ hetzner:/opt/pierref/mathsdoomscroll/import_queue/
ssh hetzner "cp /opt/pierref/mathsdoomscroll/cards.db /opt/pierref/mathsdoomscroll/backups/cards_\$(date +%Y%m%d_%H%M%S).db"
./sync_to_server.sh                                           # rsync + docker exec ingest_all.py
ssh hetzner "rm /opt/pierref/mathsdoomscroll/import_queue/*.done && df -h /opt"
```

Jamais de `make sync-md` (les Markdown ne doivent PAS monter sur le serveur).
Serveur ~926 Mo libres : ingestion par petits lots, nettoyage des `.done`
après chaque lot.
