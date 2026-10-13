# RAPPORT — Mission PORT (MathsDoomscroll) — tout ce qui a été dit/fait

_Dernière mise à jour : 2026-10-13. Fichier de synthèse non versionné._

---

## 1. Architecture découverte (audit)

- Application **Flask + SQLite** (`cards.db`), 3 types de cartes : `COURSE`, `QCM`, `TF`.
- **L'app NE LIT AUCUN JSON de cartes.** Format cible = texte à blocs interprété par
  `parse_blocks()` (`app.py:71`) :
  ```
  CAT: Matière / Sous-catégorie
  Q: [QCM] question        (ou Q: [TF] affirmation + A: Vrai|Faux ; ou Q: concept pour COURSE)
  C1: [x] bonne réponse
  C2: distracteur
  R: explication
  ---
  ```
  Règles : QCM = ≥ 2 choix et ≥ 1 `[x]` ; TF = ligne `A:` obligatoire ; sous-catégorie par
  défaut « Général » ; **dédup sur (type, front)**.
- Le LaTeX (`$…$`, `$$…$`) reste en texte brut (aucun échappement JSON).
- Pipeline existant : `main.py` (scrape Moodle) → `batch_convert.py` (MarkItDown) →
  `EPITA_Moodle_Notes_MD/` (**4 241 .md, 26 Mo — jamais envoyés au serveur**) →
  `generate_qcms.py` (Mistral) → `Generated_QCMs/*.txt` → `sync_to_server.sh` →
  `import_queue/` → `ingest_all.py` (`docker exec mathsdoomscroll_app`) → `cards.db`.
- Serveur : `ssh hetzner`, `/opt/pierref/mathsdoomscroll` (alias symlinks
  `mathsdoomscrolling`, `doomscrolling`), conteneur `mathsdoomscroll_app` (port 5080),
  **926 Mo libres (98 % plein)**.

## 2. Découverte critique sur les exports QCM Moodle

- Dans ces exports, `[x]` = réponse **SÉLECTIONNÉE par l'élève**, pas la correction.
- **Note pleine** (318/492 questions) : l'élève a tout bon → `[x]` = bonne réponse → **exploitable**.
- **Note partielle, nulle ou « Non noté »** (174 questions) : `[x]` = réponse (souvent fausse)
  de l'élève → **REJETÉE**, jamais publiée avec une fausse « bonne réponse ».
- Chaque option est exportée **3×** (label « a. » ×2 + sans label) → dédup sur le texte après
  retrait du label, `[x]` combiné (OU).
- Fichiers `qcms/*.md` : 162 contiennent de vraies questions à choix ; 2 024 sont des stubs
  de métadonnées (aucune tentative capturée).

## 3. État Git

- Branche **`feature/md-to-cards`** (créée depuis `origin/gemini/allow-bots` @ `ef6e61a`),
  **poussée sur GitHub** (`origin/feature/md-to-cards`) — sans force, `main` intacte.
- Commits : `b0f379c` (hygiène : `import_queue/` ignoré, `.done` désuivis mais conservés sur
  disque) + `cb15c79` (pipeline `md_to_cards.py` + tests + README).
- **Stash préservé** : `stash@{0}` = modif locale `templates/index.html` (gtag `G-K7M75BSXGY`,
  obsolète ; la branche utilise `G-ZK655F8T1W`). Récupérable via `git stash pop`.

## 4. Ce qui est implémenté (`md_to_cards.py`, tests 35/35 OK)

- **Passe A** (0 token) : `md_converter.normalize_mathjax_tags()` —
  `[mathjaxinline]X[/mathjaxinline]` → `$X$`, `[mathjax]X[/mathjax]` → `$$X$$`, contenu intact.
- **Passe B** (0 token) : extraction déterministe *score-aware*, dédup 3× export, retrait
  labels, suppression lignes admin, dédup `(type, front)` avec suffixe déterministe
  `[Q<n>·<hash6>]`, élimination des doublons exacts intra-lot, validation de chaque `.txt`
  par le vrai `parse_blocks()`.
- **Passe C** : `ensure_course_card()` — index **lecture seule** du serveur (ssh +
  `docker exec`, SQLite en mode `ro`), clé stable normalisée du chemin, front déterministe
  « Chapitre : <titre> », états `SKIPPED_EXISTS` / `NO_CONTENT` / `PENDING_LLM` /
  `GENERATED` / `FAILED`, backend LLM abstrait (Mistral modèle gratuit / Ollama) **derrière
  `--allow-llm`**.
- Tracker `md_to_cards_progress.json` (sauvegarde atomique, `--retry-failed`, `--force`).

## 5. Résultats chiffrés

- **Passe B (collection complète)** : 2 186 fichiers → 2 024 stubs SKIPPED, 139 REJECTED,
  **23 fichiers / 42 cartes QCM** écrites localement, 240 questions rejetées (réponses élève),
  209 doublons éliminés, 20 fronts reformulés, **0 échec de validation**.
- **Passe C (dry-run)** : 281 chapitres énumérés, 71 contiennent des QCM, 281 `PENDING_LLM`
  (0 `SKIPPED_EXISTS` : la taxonomie canonique est nouvelle et coexistera avec les 24 cartes
  historiques).
- Local : `Generated_QCMs/` = 25 `.txt` (2 anciens Mistral + 23 nouveaux).

## 6. Tiers gratuits (vérifiés, aucun appel payant effectué)

- **Mistral** : tier *Experiment* — **aucune carte bancaire** (vérification SMS + opt-in
  données), ~1 req/s, plafond TPM visible uniquement en console. ⚠️ `open-mistral-7b`
  (défaut de `generate_qcms.py`) est **payant → interdit** ; modèles gratuits :
  `mistral-small-latest`, `open-mistral-nemo`.
- **Gemini** : gratuit sans carte, mais les nouveaux comptes AI Studio peuvent être basculés
  en prépayé (depuis mars 2026).
- **Ollama** : coût zéro, **non installé** localement.
- **`MISTRAL_API_KEY`** : activée, lue depuis `.env` via `load_dotenv()`, **jamais affichée**.

## 7. Autorisations

- **Exécuté** : `git push -u origin feature/md-to-cards` (feu vert (a)).
- **Autorisé mais PAS encore exécuté** : lot de test de ~5 fichiers variés (feu vert (c)),
  dans l'ordre : `df -h /opt` → `rsync --dry-run` (vérifier aucun `.md`) → sauvegarde
  horodatée de `cards.db` → `./sync_to_server.sh` → vérification sur le site (carte visible,
  KaTeX, catégorie, aucun doublon, 24 cartes existantes intactes) → `rm import_queue/*.done`
  → `df -h /opt`. Restauration de la sauvegarde si quoi que ce soit casse.

## 8. Mission Passe C v2 (reçue, À IMPLÉMENTER)

- **Budget** : max 5 €, **plafond DUR 4 € dans le code** (arrêt automatique + checkpoint,
  même sans réponse de l'utilisateur). Clé lue depuis `MISTRAL_API_KEY`, jamais affichée/loggée.
- **Forme des cartes (mobile)** : cartes **ATOMIQUES** (une idée par carte).
  - COURSE : `Q:` = titre court du concept (≤ 80 caractères, unique dans la sous-catégorie,
    ex. « Théorème de Bézout : énoncé »), `R:` = 2 à 6 lignes max, formules en `$…$`.
    5 à 15 cartes COURSE par chapitre selon la densité (pas de quota fixe).
  - Mix par chapitre : COURSE + quelques **TF** (pièges classiques) + quelques **QCM**
    (4 choix, **1 seule bonne réponse**, distracteurs plausibles = erreurs réelles d'étudiant,
    `R:` courte). Le feed tire 4 COURSE + 3 QCM + 3 TF → répartition cohérente visée.
- **Exactitude (priorité n°1)** — pipeline en **2 appels** par chapitre (ou par section si
  trop long) :
  1. **GÉNÉRATION** : prompt système = grammaire exacte (`SYSTEM_PROMPT` de
     `generate_qcms.py`), texte brut exigé (ni JSON, ni ```), et règle : « n'utilise QUE le
     contenu du texte fourni, n'invente aucune formule, hypothèse ou valeur absente du texte ;
     si une notion est ambiguë ou incomplète, ne génère pas de carte dessus ».
  2. **VÉRIFICATION** : second appel qui relit chaque carte **contre le texte source** et
     renvoie par carte `OK` / `À_CORRIGER` / `REJETER` + justification d'une ligne.
     `REJETER` → supprimée ; `À_CORRIGER` → régénérée **UNE fois** puis re-vérifiée, sinon
     supprimée. Log : `cards_rejected.log`.
  - **Pas de troncature à 14 000 caractères** : découpage par sections cohérentes (titres),
    chaque section traitée séparément avec le titre du chapitre en contexte.
  - **Few-shot** : 2 à 3 vrais QCM validés de la passe B dans le prompt de génération (style
    et difficulté), sans copier leur contenu dans d'autres chapitres.
- **Contrôles automatiques (sans IA)** : chaque sortie dans `parse_blocks()` ; rejet si
  front vide/dupliqué, nombre de `$` impair, `back` vide (sauf TF/QCM), `back` > 600
  caractères, QCM sans exactement 1 `[x]`, TF sans `A:`. Doublons `(type, front)` détectés
  avant déploiement, front reformulé (suffixe déterministe).
- **§5 TEST COMPARATIF OBLIGATOIRE avant tout gros lot** :
  1. Prix officiels (entrée/sortie par million de tokens) lus sur la **page officielle**
     Mistral + estimation chiffrée pour 281 chapitres avec chaque modèle (2 passes incluses).
  2. Test sur **3 chapitres variés** (maths à formules, algo/code, chapitre court) avec
     **2 modèles de gammes différentes** : tableau côte à côte (cartes générées, cartes
     rejetées par la vérification + pourquoi, coût réel de chaque). Rien n'est déployé.
  3. **STOP → l'utilisateur choisit le modèle** (si écart de qualité faible : le moins cher).
- **§6 (après le choix du modèle)** : passe C complète par lots (`--limit`), checkpoint par
  chapitre, coût cumulé affiché à chaque lot ; régénération des **240 questions rejetées** en
  dérivant la bonne réponse du texte de la **CORRECTION/feedback** (source de vérité du prof,
  pas du `[x]`), rejet si la correction est ambiguë, passage en vérification, dry-run +
  échantillon de 10 à montrer avant le lot complet ; déploiement par lots avec feu vert par lot.
- **§7 ordre** : 1) push + lot de test A/B → 2) prix + estimations + comparatif §5 → STOP →
  3) lot de 10 chapitres → STOP → 4) rapport final (cartes par type, rejets + raisons, coût
  total, chapitres restants, stubs sans contenu non couverts).

## 9. Ce qu'il reste à faire (ordre)

1. **(c) Lot de test A/B** (~5 fichiers variés) : exécuter et montrer les résultats.
2. **Implémenter la passe C v2** (plafond 4 €, 2 appels génération+vérification, découpage
   par sections, cartes atomiques COURSE/QCM/TF, contrôles §4, few-shot, `cards_rejected.log`).
3. **Lire les prix officiels Mistral** + estimation chiffrée pour 281 chapitres.
4. **Comparatif §5** : 3 chapitres × 2 modèles → **STOP**, choix du modèle par l'utilisateur.
5. **Lot de 10 chapitres** (après choix) → montrer cartes + coût réel + taux de rejet → STOP.
6. **240 questions rejetées** : dry-run + échantillon de 10, puis lot complet (avec feu vert).
7. **Déploiement par lots** (df -h, sauvegarde, vérification site, nettoyage `.done`),
   feu vert pour chaque lot après le lot de test.
8. **Rapport final** chiffré.

**Ce que l'utilisateur doit décider :** choisir le modèle après le comparatif §5 ; donner le
feu vert pour le lot de 10 chapitres, puis chaque lot de déploiement ; valider la
régénération des 240 questions rejetées.
