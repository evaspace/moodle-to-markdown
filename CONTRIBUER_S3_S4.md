# Ajouter la spé (S3 et S4) à EPITA Doomscrolling

Guide pour le contributeur de spé et pour son assistant de code. Il décrit exactement comment S1 et S2 ont été construits, pour refaire la même chose sur S3 et S4, avec le même niveau d'exigence.

Lire aussi, dans cet ordre, avant de toucher au code :

1. [README_OBJECTIFS.md](README_OBJECTIFS.md) : ce que veut l'application, décisions du propriétaire (Morgan). Elles s'appliquent aussi à la spé.
2. [README.md](README.md), section « Levels mode » : fonctionnement technique des niveaux.
3. Ce fichier.

## Ce qu'il faut produire

Pour chaque ECUE de S3 et de S4, la même chose que pour chaque ECUE de S1/S2 :

1. **Les annales transcrites** dans `annales/md/S3/...` et `annales/md/S4/...` : chaque examen en Markdown + LaTeX, chaque exercice étiqueté (type, ECUE, niveau, formules), avec son corrigé.
2. **Un ou plusieurs parcours de niveaux** dans `parcours/src/<parcours>.py` : des exercices sur papier classés du plus simple au niveau examen + 20 %, chaque réponse vérifiée par machine.
3. **Les fiches de cours** de ce parcours (`NOTIONS`) et ses **questions de scroll** (`QUIZ`).
4. **L'inscription au registre** `parcours/syllabus.json` (matière, semestre, ECUE, chapitres Moodle, parcours, annales, période d'examen).

Ordre des matières (décision de Morgan, ne pas redemander) : maths d'abord, puis physique, archi, électronique, algo, prog, anglais, méthodo, puis le reste. Dans une matière, suivre l'ordre des examens du semestre.

## Règles de fond (non négociables)

- **Un exercice par formule.** Un niveau = un type d'exercice. Le niveau est validé quand *tous* ses exercices sont verts. Si un niveau mélange deux formules, le couper en deux niveaux.
- **Du plus simple au niveau examen + 20 %.** Niveau 1 : appliquer une formule une fois, avec des nombres simples. Derniers niveaux : de vrais exercices d'annales (champ `src`), puis un niveau légèrement plus dur que l'examen.
- **Calibrer sur les TD et sur toutes les annales.** Les annales donnent le format et le niveau attendu, mais ne couvrent pas tout le programme : chaque chapitre du cours Moodle doit avoir ses niveaux, même s'il n'est jamais tombé.
- **Le programme est celui de la promo qui passe l'examen.** Les spé actuels sont la promo 2030 : se baser sur le cours Moodle 2030 de S3/S4. Ce qui est dans de vieilles annales mais plus au programme va dans `hors_programme_<promo>` de `syllabus.json`, sans niveau.
- **Aucune réponse non vérifiée.** Tout ce qui se calcule passe par `parcours/build.py` (sympy). Le code C, OCaml et Python est exécuté (voir « Vérifier »). Seules les démonstrations (`open`) sont relues à la main, et elles ont toujours une solution modèle complète.
- **Ne rien inventer sur les sources.** Si un examen n'a pas de corrigé officiel, le corrigé écrit pour l'application le dit dans son en-tête : « corrigé rédigé ». Une lecture douteuse d'un scan est signalée dans le texte, pas devinée.
- **Jamais de nom d'étudiant.** Certains PDF d'annales sont des copies d'étudiants annotées : ne transcrire que l'énoncé et les réponses, jamais le nom, le prénom ou la classe.
- **Schémas obligatoires en électronique** dès qu'un énoncé décrit un circuit (`parcours/src/schema.py`). Arbres dessinés en algo (`algo_abg.fig`).
- **Le texte d'un exercice est du HTML brut.** Ne jamais écrire `<` collé à une lettre dans une formule : `$a<b$` ouvre une balise `<b>`. Écrire `$a < b$`.
- **Exercices en français.** Les annales anglaises ne sont pas transcrites quand la version française existe.

## Installation

Le dépôt est public : les cours et les PDF d'annales n'y sont **pas** (droits d'auteur, `.gitignore`). Chacun garde les siens en local.

```sh
git clone git@github.com:evaspace/moodle-to-markdown.git epitadoomscrolling
cd epitadoomscrolling
git switch dev                      # base de travail, contient tout S1/S2

python3 -m venv .venv               # l'application web
.venv/bin/pip install -r requirements.txt

python3 -m venv .venv-build         # la vérification du contenu (pas besoin dans l'appli)
.venv-build/bin/pip install sympy schemdraw ziamath
```

Docker est nécessaire seulement pour `parcours/check_c.py` et `parcours/check_caml.py` (ils lancent un conteneur Alpine jetable, sans réseau).

### Où mettre les fichiers locaux

| Quoi | Où | Versionné |
|---|---|---|
| Cours Moodle convertis en Markdown (sortie de l'outil de scraping) | `EPITA_Moodle_Notes_MD/<nom du cours Moodle>/<chapitre>/` | non |
| PDF d'annales S3 | `annales/raw/S3/{Finals,Midterms,MCQs,TDs}/<Matière>/<dossier promo>/...` | non |
| PDF d'annales S4 | `annales/raw/S4/...` (même arborescence) | non |
| Transcriptions d'annales | `annales/md/S3/...`, `annales/md/S4/...` (même chemin que le PDF, `.md`) | oui |
| Parcours de niveaux | `parcours/src/*.py` (source) et `parcours/*.json` (généré) | oui |

Les annales viennent du dépôt GitHub Epidocs/Past-Exams (site past-exams.epidocs.eu). Garder exactement son arborescence et ses noms de fichiers : `syllabus.json` et les en-têtes des transcriptions y font référence.

Sans les dossiers S1/S2 en local, `parcours/build.py` affiche « not checked, folder absent locally » pour eux et continue : c'est normal. Pour S3/S4, les dossiers sont présents chez toi, donc tout chemin faux reste une erreur.

Pour que Morgan puisse déployer, il lui faut tes dossiers S3/S4 de `EPITA_Moodle_Notes_MD/` et `annales/raw/S3`, `annales/raw/S4` : les lui envoyer par un canal privé (archive), jamais dans le dépôt.

## Méthode, ECUE par ECUE

Faire les étapes dans cet ordre pour une ECUE, puis passer à la suivante. Une ECUE terminée = une branche poussée.

### Étape 1 : inventaire

1. Lister les cours Moodle S3/S4 présents dans `EPITA_Moodle_Notes_MD/` et leurs chapitres.
2. Retrouver la maquette (UE, ECUE, codes, blocs d'examen, coefficients) et l'ajouter à [SYLLABUS_ORGANISATION.md](SYLLABUS_ORGANISATION.md), sections « Semestre 3 » et « Semestre 4 », au même format que S1/S2.
3. Lister les annales S3/S4 de chaque ECUE dans `annales/raw/`, avec leur vraie date (le dossier porte la promo, pas l'année de l'examen : un dossier `2027` de S3 = examen passé à l'automne 2025 environ ; vérifier sur la première page).
4. Ajouter le semestre à `parcours/syllabus.json`, dans la matière concernée (ne pas créer de nouvelle structure) :

```json
{"id": "S3", "moodle": "<nom exact du dossier du cours dans EPITA_Moodle_Notes_MD>",
 "ecues": [
  {"id": "<code ECUE>", "titre": "<intitulé officiel>", "bloc": "<B5…>",
   "periode_examen": "<ex. : mi-novembre, avant les vacances>",
   "chapitres": ["<nom exact de chaque dossier de chapitre>"],
   "parcours": [], "a_faire": ["<chapitres sans parcours pour l'instant>"],
   "hors_programme_2030": [],
   "annales": ["S3/Finals/<Matière>/<promo>/<fichier>.pdf"]}
 ]}
```

`moodle` vaut `"."` quand les chapitres sont des dossiers de cours entiers (cas de l'algo). `parcours` reste vide tant que le parcours n'est pas construit : `build.py` refuse un parcours listé mais absent.

### Étape 2 : transcrire les annales

Une transcription par PDF, au chemin du PDF avec `.md`. Exemple réel : [annales/md/S2/Finals/Elec/2020/final-2020-s2-elec-correction-fr.md](annales/md/S2/Finals/Elec/2020/final-2020-s2-elec-correction-fr.md).

Format exact :

```markdown
# Partiel de <matière> S3 — <mois année> (<corrigé officiel | corrigé rédigé>, FR)

- Source : `raw/S3/Finals/<...>.pdf`, pages a à b. <Corrigé officiel ou « Pas de corrigé officiel : corrigé rédigé pour cette application, vérifié avec sympy ».>
- Date réelle : <mois année> (dossier promo <promo>). Sujet : `<fichier-subject>.md`.
- <Conditions : calculatrice, documents, barème.>

## Exercice 1. <titre> (<points>)
Type : <type d'exercice> · ECUE : <titre de l'ECUE> · Niveau : <id du parcours>/<numéro du niveau>
Formules : <toutes les formules nécessaires pour le résoudre>

<énoncé, formules en LaTeX entre $…$>
> <solution, uniquement dans les fichiers de corrigé>
```

- Chaque exercice est un titre `## ` suivi **immédiatement** des lignes `Type :` et `Formules :`. `Niveau :` est ajouté quand le parcours existe (étape 4). Un type sans niveau dédié s'écrit sans `· Niveau`.
- Dans un corrigé, les lignes de solution commencent par `> `. Le fichier sujet se dérive du corrigé en retirant ces lignes (`annales/tools/subj.py`).
- Chaque nouveau type va dans le dictionnaire `F` de `annales/tools/formules.py` (type → formules, une seule source). Réutiliser un type existant quand c'est le même exercice.
- PDF avec couche texte : `pdftotext` perd les exposants (`3^n` devient `3n`) ; utiliser `python3 annales/tools/bx.py fichier.pdf` (marque `^{}`/`_{}`), et comparer visuellement avec l'image de la page (`pdftoppm -r 70 -png`).
- Scans sans couche texte : lire les pages en image, une par une. Ne jamais compléter un passage illisible : le signaler.
- Pas de corrigé officiel : en rédiger un, vérifier chaque calcul avec sympy (ou en exécutant le code), et écrire « corrigé rédigé » dans l'en-tête.

Après chaque fichier : `python3 annales/tools/index.py`. Il reconstruit `annales/INDEX.md` et `annales/FORMULES.md` et échoue si un exercice n'a pas de ligne Type/Formules, si un type n'a pas de formules ou si un niveau n'existe pas. Ne jamais modifier ces deux fichiers à la main.

Outils de série (facultatifs) : `annales/tools/list.txt` (ligne N = PDF N), `t.sh N` (texte compact du PDF N), `addf.py DOSSIER` (installe `DOSSIER/out/NNN.md` et insère les lignes Formules). Pour S3/S4, regénérer `list.txt` avec `cd annales/raw && find ./S3 ./S4 -name '*.pdf' | sort`.

### Étape 3 : construire le parcours de niveaux

Partir d'un parcours existant de la même nature et le copier : [parcours/src/ev.py](parcours/src/ev.py) (maths, démonstrations et matrices), `apis_integrales.py` (calcul), `phys_thermo.py` (physique), `elec_filtres.py` (circuits avec schémas), `archi_sequentielle.py` (logique), `algo_recherche.py` (algo avec figures), `prog_c_debut.py` (code exécuté).

Structure d'un fichier `parcours/src/<nom>.py` :

1. **Docstring** : ECUE, chapitres Moodle utilisés, examens sur lesquels le parcours est calibré.
2. **`SUBJECT`** :

```python
SUBJECT = {
    "id": "maths-s3-<ecue>",          # <matière>-<semestre>-<sujet>, en minuscules
    "ordre": 240,                      # tri de l'accueil, voir ci-dessous
    "matiere": "maths",                # id de la matière dans syllabus.json
    "semestre": "S3",
    "ecue": "<code ECUE>",             # identique à syllabus.json
    "titre": "<titre court>",
    "chapitres_moodle": ["<dossiers de chapitre>"],   # sous-ensemble de ceux de l'ECUE
    "td": "<TD utilisés>",
    "examens": ["<examen (période)>"],
}
```

   `ordre` : chaque matière a sa centaine (maths 100-299, physique 300-399, archi 400-499, électronique 500-599, algo 600-699, prog 700-799). S1 et S2 occupent le début de chaque centaine ; prendre la suite pour S3 puis S4 (maths : S3 à partir de 240, S4 à partir de 270 ; physique : S3 340, S4 370 ; etc.), dans l'ordre des examens.

3. **`NOTIONS`** : une fiche par notion, `{"id", "titre", "formule", "exemple", "cours"}`. `formule` = l'essentiel lisible en 10 secondes (formules séparées par ` · `), `exemple` = un cas chiffré, `cours` = l'explication et la méthode. Ce sont les cartes du scroll et la « Fiche du chapitre ».
4. **`LEVELS`** : liste de `{"n": 1, "titre", "notions": [ids], "exos": [...]}`, `n` de 1 à N sans trou. Chaque exercice a un `id` unique dans le fichier (2-3 lettres), un `enonce`, une `sol` complète et un `kind` :

   | `kind` | Vérification par `build.py` |
   |---|---|
   | `value` | `calc` (expression sympy du calcul) doit valoir `ans`. Nombres, limites (`limit(...)`, `oo`), polynômes (comparés en plusieurs points), matrices (égalité exacte). Aides disponibles : `bits`, `hexa`, `tc`, `f32`, `eqv`, `cover`, `seqD`, `seqJK`… (voir `NS` dans `build.py`) |
   | `derivative`, `primitive`, `integral` | `f`, `ans` (et `a`, `b` pour une intégrale) |
   | `ode` | solution générale `f` (constantes `C1`, `C2`) injectée dans `lhs` (`Y0`=y, `Y1`=y', `Y2`=y'') |
   | `open` | démonstration ou question de cours : pas de calcul, `sol` obligatoire |
   | `multi` | exercice d'examen en plusieurs questions : `parts` = ids d'autres exercices du fichier, déjà vérifiés ; solution et formules = celles des parties |

   Si un type de calcul n'est pas vérifiable avec ces outils, ajouter une aide dans `NS` de `build.py` (comme `seqJK` pour l'archi) plutôt que de passer l'exercice en `open`.

   Champs optionnels : `src` (« Examen S3-B5 <ECUE> 2026, ex. 2 » : obligatoire pour un exercice repris d'une annale), `duree` (minutes de réflexion avant la correction). Écrire de petites fonctions `v(...)` et `o(...)` comme dans `ev.py`.

   Construction des niveaux : lister tous les types d'exercices des annales de l'ECUE (lignes `Type :` de l'étape 2) et toutes les formules du cours ; chaque type d'annale devient le sommet d'une chaîne de niveaux, les niveaux en dessous sont ses prérequis. Les deux ou trois derniers niveaux sont de vrais exercices d'examen, le tout dernier un peu plus dur.

5. **`VARIANTS`** : pour chaque exercice calculé, au moins une variante avec d'autres nombres (`{"enonce", "calc", "ans", "sol"}`), vérifiée comme l'exercice. Une variante ne montre jamais le `src`.
6. **`EXTRA_PARTS`** (souvent `[]`) et **`QUIZ`** : questions du scroll, `{"notion", "type": "vf", "q", "bonne": True}` ou `{"notion", "type": "qcm", "q", "choix": [4 réponses], "bonne": index}`. Au moins deux questions par notion.
7. **`FORMULES`** : id d'exercice → formules de la solution, séparées par ` · `. `build.py` échoue si un exercice n'en a pas.
8. Électronique : dessiner chaque circuit avec `schema.py` (`schema_echelle(...)` ou `fig(draw, alt)`), dictionnaire `FIGS` et `ajoute(LEVELS, FIGS)` en fin de fichier, comme `elec_filtres.py`.

### Étape 4 : brancher le parcours

Un nouveau parcours doit apparaître à quatre endroits, sinon le build ou les tests échouent :

1. `PATHS` dans [parcours/build.py](parcours/build.py) (nom du fichier sans `.py`).
2. `parcours` de son ECUE dans `parcours/syllabus.json` (retirer les chapitres couverts de `a_faire`).
3. `FICHE_SECTION` dans [levels.py](levels.py) : id du parcours → titre de la section de `annales/FORMULES.md` (= titre de l'ECUE dans les lignes `ECUE :`).
4. `PREREQ` dans `levels.py` : parcours dont il dépend. En spé, pointer vers les parcours S1/S2 utiles (ex. réduction des endomorphismes → `maths-s2-alm`, `maths-s2-ev`).

Puis ajouter `· Niveau : <id>/<n>` à chaque exercice d'annale de l'ECUE dans `annales/md/` et relancer `annales/tools/index.py`.

### Étape 5 : vérifier

```sh
.venv-build/bin/python parcours/build.py          # toutes les réponses + le registre, doit finir par « syllabus: OK »
python3 annales/tools/index.py                     # annales cohérentes
python3 parcours/check_c.py                        # si le parcours contient du C (Docker)
python3 parcours/check_caml.py                     # si OCaml (Docker)
.venv/bin/python -m unittest tests.test_levels tests.test_scroll tests.test_blog tests.test_exam_dates tests.test_admin_stats
```

Ne pas lancer `unittest discover` : il inclut `test_md_to_cards`, qui appelle une API payante. Tout test qui importe `app` doit définir `DB_PATH` avant (voir `tests/test_blog.py`), sinon il écrit dans la vraie base.

Puis lancer l'application en local (`DB_PATH=/tmp/dev.db .venv/bin/python app.py`, page `http://localhost:5000/niveaux`), créer un compte de test, et parcourir le nouveau parcours **sur un écran de téléphone (390 px de large)** : chaque niveau s'affiche, aucune erreur KaTeX (formule en rouge), pas de défilement horizontal, les schémas s'affichent.

### Étape 6 : documenter

- Une ligne dans [README.md](README.md), section « Levels mode », au format des lignes S1/S2 : fichier, id, nombre de niveaux et d'exercices, sources, ce qui n'est pas fait.
- Cocher l'avancement dans [TODO_REFONTE.md](TODO_REFONTE.md).
- Une décision de Morgan reçue en cours de route va dans [README_OBJECTIFS.md](README_OBJECTIFS.md), datée.

### Étape 7 : git

- Ne jamais committer sur `main`, ni sur `dev`. Une branche par ECUE, créée depuis `dev` :
  `git switch dev && git pull && git switch -c feat/s3-<matiere>-<ecue>` (annales seules : `feat/annales-s3-<matiere>`).
- Commits en anglais, au format `feat(<parcours>): ...`, `docs(annales): ...`. Aucune mention d'IA ni d'assistant dans les commits, branches, PR ou fichiers (pas de `Co-Authored-By`).
- Vérifier avant chaque commit qu'aucun fichier ignoré n'est forcé (`git status` ne doit montrer ni PDF, ni `EPITA_Moodle_Notes_MD/`, ni `.env`, ni `*.db`).
- Pousser la branche et ouvrir une pull request vers `dev`. Morgan relit, fusionne et déploie (le serveur et le domaine sont à lui).

## Organisation des branches

- `main` : ancienne version publique, ne pas toucher.
- `dev` : base de travail, contient tout le travail S1/S2 et ce guide. Partir de là.
- `feat/...`, `fix/...`, `docs/...` : une branche par sujet. Les branches S1/S2 existantes sont empilées les unes sur les autres (chacune contient les précédentes) et toutes incluses dans `dev` ; elles servent d'historique, ne pas travailler dessus.

## Liste de contrôle d'une ECUE

- [ ] ECUE, chapitres, annales et période d'examen dans `syllabus.json` et `SYLLABUS_ORGANISATION.md`
- [ ] Toutes les annales de l'ECUE transcrites, chacune avec son corrigé (officiel ou « corrigé rédigé »)
- [ ] Chaque exercice d'annale : `Type`, `ECUE`, `Niveau`, `Formules` ; `index.py` passe
- [ ] Chaque chapitre du cours couvert par au moins un niveau, même s'il n'est jamais tombé
- [ ] Un exercice par formule, du niveau 1 trivial au niveau examen + 20 %
- [ ] Derniers niveaux = vrais exercices d'examen avec `src`
- [ ] `VARIANTS` pour chaque exercice calculé, `FORMULES` pour chaque exercice, `QUIZ` sur chaque notion
- [ ] Parcours dans `PATHS`, `syllabus.json`, `FICHE_SECTION`, `PREREQ`
- [ ] `build.py`, `index.py`, tests : tout passe
- [ ] Vérifié à l'écran à 390 px
- [ ] README et TODO à jour, branche poussée, pull request vers `dev`
