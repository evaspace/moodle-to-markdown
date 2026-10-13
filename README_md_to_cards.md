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

## Commandes exactes

```bash
# Tests (35 tests, unittest — aucune dépendance ajoutée)
.venv/bin/python -m unittest tests.test_md_to_cards -v

# Analyse complète sans rien écrire (recommandé en premier)
.venv/bin/python md_to_cards.py --dry-run --only-pass b
.venv/bin/python md_to_cards.py --dry-run --only-pass c

# Lot limité réel (écrit Generated_QCMs/*.txt localement)
.venv/bin/python md_to_cards.py --only "10_Cours 3 - Arithmétique" --only-pass b
.venv/bin/python md_to_cards.py --limit 20 --only-pass b

# Reprise après interruption / échecs
.venv/bin/python md_to_cards.py --retry-failed --only-pass b
.venv/bin/python md_to_cards.py --force --only "S2-MATHS-2030" --only-pass b

# Passe C avec LLM — UNIQUEMENT après validation du tier gratuit (§ Coût)
.venv/bin/python md_to_cards.py --only-pass c --allow-llm
```

Options : `--limit N`, `--only SUBSTR`, `--retry-failed`, `--force`,
`--dry-run`, `--only-pass ab`, `--allow-llm`, `--offline` (index local),
`--refresh-index`, `--tracker PATH`.

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
- Le modèle par défaut de `generate_qcms.py` (`open-mistral-7b`) est **payant** :
  ne pas l'utiliser. Le tier gratuit *Experiment* de Mistral (aucune carte
  bancaire, vérification SMS requise) couvre `mistral-small-latest` /
  `open-mistral-nemo` — **vérifier le quota dans console.mistral.ai avant tout
  appel** (limites exactes non publiées : ~1 req/s, plafond TPM visible en
  console). Alternative zéro coût : `LLM_PROVIDER=ollama` (local, mais nécessite
  Ollama + un modèle téléchargé — aucune installation automatique).
- Gemini API : tier gratuit sans carte bancaire pour certains modèles, mais les
  nouveaux comptes AI Studio peuvent être basculés sur un plan prépayé
  (mars 2026) — à vérifier avant usage.

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
