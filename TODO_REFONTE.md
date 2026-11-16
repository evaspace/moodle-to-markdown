# TODO — Refonte EPITA Doomscrolling

Plan suivi en autonomie à partir du 2026-11-14. Objectifs : voir `README_OBJECTIFS.md`.
Cocher au fur et à mesure. Chaque étape notée « fait » a été vérifiée.

## Calendrier trouvé dans Moodle (S1-MATHS-2031)

Source : `EPITA_Moodle_Notes_MD/S1-MATHS-2031/04_*/fichiers/*.pdf`.

| Semaine | Dates | MiMos |
|---|---|---|
| S1-B1 | 21–25 sept. | Dénombrement |
| S2-B1 | 28 sept.–2 oct. | Espaces probabilisés |
| S3-B1 | 5–9 oct. | Probabilités conditionnelles |
| S4-B1 | 12–16 oct. | Variables aléatoires |
| S5-B1 | 19–23 oct. | Primitives et intégrales |
| S1-B2 | 9–13 nov. | IPP et changement de variable |
| S2-B2 | 16–20 nov. | Intro suites, limite, exemples remarquables |
| S3-B2 | 23–27 nov. | Théorèmes de convergence |
| S4-B2 | 30 nov.–4 déc. | Suites récurrentes, Landau |
| S5-B2 | 6–11 déc. | Équations différentielles 1er et 2nd ordre |

Tests à distance : 5 oct. (DP), 19 oct. (DP), **16 nov. (APIS : primitives, IPP, changement de variable)**, 7 déc. (APIS en entier).
Examen B2 (final S1) : date exacte non trouvée dans les exports Moodle (le planning hebdo n'a pas été téléchargé, `view.php`). Probablement mi-décembre ou janvier.

ECUE S1 promo 2031 : DP (dénombrement, probas), APIS (primitives, intégrales, suites, EDO), OBM (logique, ensembles, applications).

## Étapes

### Phase 0 — Sauvegarde
- [x] Copier `cards.db` et `Generated_QCMs/` dans `backups/pre-refonte-20261114/`

### Phase 1 — Annales (past-exams.epidocs.eu = repo GitHub Epidocs/Past-Exams)
- [x] Lister le dépôt (1611 fichiers) ; 147 fichiers de maths S1/S2
- [x] Télécharger les maths S1/S2 dans `annales/raw/` (46 Mo)
- [x] Détecter les PDF scannés : 41 sans couche texte, 105 avec texte
- [x] Extraction automatique brute (`pdftotext`) en `.md` pour tout ce qui a du texte → `annales/md/`
- [x] Transcription propre (LaTeX) des 146 fichiers (2026-11-15), 956 exercices, chacun avec type, ECUE, niveau et ligne « Formules : ». Ordre suivi :
  1. Finals S1 (= examen B2) et midterms S1 (= examen B1), sujets FR, 2024→2029
  2. Scans S1 restants
  3. S2
- [x] Corrigés : tous les sujets maths S1/S2 ont maintenant un corrigé (officiel ou rédigé, 2026-11-15) ; les corrigés rédigés disent « corrigé rédigé » dans leur en-tête, sont vérifiés avec sympy et signalent les lectures ambiguës (DP 2029 ex. 1.4, mid-term 2023 ex. 7, TD2 2030 ex. 1.2 q5)
- [x] Index `annales/INDEX.md` (examen → date réelle → exercices → type → ECUE → niveau), généré par `annales/tools/index.py`
- [x] Fiche synthèse `annales/FORMULES.md` + page `/formules` (2026-11-15)

### Phase 2 — Carte des compétences (maths S1)
- [x] Pour chaque exercice d'annale : type d'exercice + formules nécessaires (lignes « Type : » et « Formules : », 223 types)
- [x] Prérequis entre parcours (2026-11-15) : après un exercice raté, liens « Notions de base à revoir » vers les parcours dont dépend celui-ci (`levels.PREREQ`, ex. ALM → EV → polynômes → OBM). Reste ouvert : un graphe plus fin au niveau des notions.
- [x] Rattacher chaque exercice de TD (TD1–TD4 2026) à un niveau du graphe (les 956+ exercices d'annales, TD 2026 compris, portent un `Niveau :`, vérifié par `annales/tools/index.py`)
- [x] APIS intégrales : 14 niveaux, 77 exercices (TD3 + annales 2020-2024 + niveau +20 %), 11 notions, 23 QCM/VF.
  Source `parcours/src/apis_integrales.py`, vérifié par sympy (`parcours/build.py`), sortie `parcours/apis_integrales.json`.

### Phase 3 — Contenu
- [x] Cartes de cours 10 secondes par notion (APIS d'abord) (NOTIONS de chaque parcours : formule, exemple, cours long ; 9 parcours maths)
- [x] QCM / vrai-faux par notion (QUIZ de chaque parcours, 9 parcours maths)
- [x] Exercices types gradués par niveau + corrigés (582 exercices, corrigés inclus)

### Phase 4 — Application
- [x] Lien « Niveaux » sur l'accueil
- [x] Lire `app.py`, templates, schéma `cards.db`
- [x] Corriger le bouton retour (retour à la page précédente) (voir plus bas : fil à URL propre)
- [x] Hiérarchie matière → semestre → ECUE → chapitre dans l'ordre du syllabus (sélecteur sem/matière/chapitre de `/niveaux`, ordre du syllabus)
- [x] Comptes identifiant + mot de passe (`/compte`), e-mail facultatif stocké
- [x] Mail de réinitialisation (SMTP OVH depuis morgan@pierref.eu, lien 1 h, testé en réel le 2026-11-14)
- [x] Mode Niveaux (`/niveaux`, `levels.py`) : 3 réussites d'affilée, recul d'un niveau sur échec + formules, chat qui applaudit / explose, entraînement libre sur un autre niveau
- [x] Scroll adaptatif `/scroll/<parcours>` (`scroll.py`, 1 carte cours sur 4, QCM 1–2 cartes après, erreurs qui reviennent), tests `tests/test_scroll.py`
- [x] (2026-11-15, état par compte) Brancher aussi le fil d'accueil (cartes `cards.db`, état global non lié aux comptes) sur les parcours
- [x] Page « mes niveaux » avec % et liste cliquable des niveaux
- [x] Code couleur par matière : abandonné volontairement (règle de palette : un seul accent ; la matière est déjà écrite dans le titre de chaque parcours)
- [x] Tests `tests/test_levels.py` (8 OK), déployé le 2026-11-14, test de bout en bout en HTTPS OK
- [x] Bouton retour : le fil a sa propre URL (`/?cat=..`), retour navigateur = liste des modules (testé dans Chrome headless)
- [x] Les 4 tests de `tests/test_md_to_cards.py` en erreur réparés (signature de `FakeV2Backend.verify`) et le test de vérif mis à jour : la vérification LLM est désormais bloquante (2026-11-15)

## Journal
- 2026-11-16 (nuit, suite) : première matière Archi S1 : numération (14 niveaux, 75 exos) et algèbre de Boole (12 niveaux, 69 exos), réponses vérifiées par `build.py` (nouveaux helpers). 26 tests OK, 26 niveaux vus à 390 px (0 erreur KaTeX).
- 2026-11-16 (nuit) : parcours physique S2 « Travail et énergie » (11 niveaux, 64 exos), vérifié à 390 px (0 erreur KaTeX, pas de débordement), 26 tests OK.
- 2026-11-15 (suite 10) : niveaux d'examen S2 2028/2029 ajoutés (EV, APEF ×2, ALM). Premier parcours de physique : mécanique du point S1 (15 niveaux, 73 exos). Ordre des matières décidé : physique, archi, électronique, algo, prog, anglais, méthodo.
- 2026-11-15 (suite 5) : navbar commune `templates/nav.html` (Niveaux, Stats, Formules, Cours, Fil + niveaux sur papier validés / points / jours d'affilée via `/api/me`), pastille de l'accueil dynamique et cliquable vers `/stats`, footer PIERREFEU sur toutes les pages sauf le fil plein écran (`/scroll`, fil d'accueil). `/stats` : progression par parcours, réussite par semaine, niveaux à retravailler. `/admin/stats` (+ `?format=json`) : audience, activation, rétention, funnel par parcours, exercices les plus ratés (`admin_stats.py`). Branche `feat/navbar-stats-admin`.
- 2026-11-15 (suite 4) : parcours S2 en ligne. APEF polynômes (10 niveaux, 43 exos), APEF fonctions (11, 57), EV (11, 60), ALM (12, 64), calés sur les examens 2026 de la promo 2030, sans nombres complexes. `build.py` vérifie aussi les réponses polynomiales, les DL et les matrices. 394 exercices d'annales S2 rattachés à un niveau. 23 tests OK, 3725 formules rendues sans erreur KaTeX, 44 niveaux vus à 390 px sur le site.
- 2026-11-15 (suite 3) : « Formules de la solution » affiche maintenant les formules de l'exercice (dict `FORMULES` dans chaque `parcours/src/*.py`, 358 exercices, contrôlé par `build.py`), puis le rappel de cours du niveau. 23 tests OK, 0 erreur KaTeX sur les 358 listes.
- 2026-11-15 (suite 2) : confettis pixel art plein écran quand un niveau est validé (`confetti()` dans `static/niveaux.js`, sur le canvas du chat ; 7 gerbes, 14 au dernier niveau ; désactivé si `prefers-reduced-motion`).
- 2026-11-15 (suite) : aides sur les exercices sur papier. Boutons « Fiche du chapitre » (points ÷ 2, + 50 % de temps) et « Formules de la solution » (points ÷ 3, temps × 2), route `/api/niveaux/<parcours>/hint`, comptées côté serveur. 23 tests OK, vérifié dans Chromium à 390 et 1280 px. Reste : liste de formules par exercice (champ à ajouter dans `parcours/src/*.py`) au lieu des formules du niveau.
- 2026-11-15 : fin de la transcription des annales (103 à 146 : contrôles S2 2017-2026, contrôles de TD et feuilles de TD S2). Index, fiche synthèse des formules, page `/formules` en ligne. Coquilles relevées dans des corrigés officiels et signalées dans les fichiers : contrôle S2 février 2017 ex. 1 (`e cos 1`), contrôle S2 mars 2021 ex. 6 b (coordonnées `(2, 1, -1)`).
- 2026-11-14 nuit : chat partagé (`static/cat.js`) fixe en bas à droite, vit sa vie, explose en sang, renaît en 1,5 s. Points selon la vitesse (temps de référence = moyenne des utilisateurs par niveau), ÷3 si formules ouvertes avant de répondre. Mail de reset. `syllabus.json` + contrôles. Parcours suites. Scroll adaptatif. Mobile + bureau vérifiés dans Chromium.
- 2026-11-14 soir : chrono, parcours DP + OBM, `build.py` accepte `value` (calcul vérifié) et `open` (démonstration, corrigé obligatoire). Accord total de l'utilisateur ; pas de dates d'examen officielles (avant chaque vacances).
- 2026-11-14 : 146 annales maths S1/S2 en `annales/md/` (41 scans à transcrire). Constat : les exos d'intégrales d'annales suivent toujours le schéma primitive directe u'f(u) → IPP → changement de variable donné.
- 2026-11-14 : cadrage, `README_OBJECTIFS.md`, calendrier, téléchargement des annales.

## Suite (par priorité, mise à jour 2026-11-14 nuit)
- [x] Page 404 personnalisée (`templates/404.html`, JSON sur `/api/`)
- [x] Barre de progression totale sur la page d'exercice (% de toutes les formules du parcours en vert)
- [x] Validation par couverture : un carré par exercice (vert / rouge / vide), niveau validé quand tout est vert, les rouges reviennent
- [x] **Approfondir chaque niveau : un exercice par formule** (ex. primitives usuelles : une par ligne du tableau, sin et cos séparés ; dérivées usuelles idem). Commencer par APIS intégrales niveaux 1–5, puis DP, OBM, suites, EDO. (fait pour les 9 parcours)
  - [x] APIS intégrales niveaux 1–5 (2026-11-14) : +17 exos (cos u, 1/u, tan u ; cos, sin, eˣ, 1/x, 1/√x, arctan, 1/cos² seuls ; ln et √ de ax+b ; u'/u², u'/√u ; u'/(1+u²), u' cos u, u' sin u). 94 exos.
- [x] Sélection semestre → matière → chapitre (ou matière d'abord) + « Tout confondu » sur `/niveaux` (2026-11-14).
- [x] Approfondir DP, OBM, suites, EDO (2026-11-14) : formules sans exercice dédié ajoutées (E(X+Y), Bernoulli E=p, ¬(P∨Q), (ln n)^a/n^b, qⁿ/n!, EDO racine double).
- [x] Variantes chiffrées : un exercice raté revient avec d'autres chiffres (champ `variants`, vérifié par sympy, rotation à chaque nouvelle tentative). Écrites pour tous les exercices à réponse calculée : intégrales 88, DP 72, suites 23, EDO 45. Pas de variante pour les exercices de rédaction (OBM, démonstrations) ni les exercices à étapes.
- [x] Page « Mes stats » (`/stats`) : totaux, carrés de l'année rouge→vert, temps sur 30 jours, records, par matière.
- [x] Parcours APIS EDO (12 niveaux, 47 exos, type `ode` vérifié par sympy, calé sur APEF mars 2024 et mars 2025)
- [x] Chrono par exercice (2 min dérivée/primitive, 5 min intégrale, 5 min par question d'annale), temps écoulé = raté
1. [x] Registre `parcours/syllabus.json` + contrôles de liens dans `build.py` (chemins Moodle, annales ↔ niveaux, prérequis, TD) ; dates : avant chaque vacances (pas de dates officielles).
2. [x] Parcours **DP** (16 niveaux, 81 exos) et **OBM** (13 niveaux, 55 exos), calibrés sur B1-DP oct. 2024, B1 nov. 2023, B1-OBM oct. 2024, B1-LE nov. 2023, TD1/TD2/séminaire 2026. En ligne, ordre syllabus OBM → DP → APIS.
   - [x] Nombres complexes : hors programme 2031, non traités (décision utilisateur 2026-11-14)
   - [x] Rattacher chaque exercice de TD1/TD2/séminaire à un niveau (voir ci-dessus)
3. [x] Transcription propre de **toutes** les annales (146 fichiers, dont 41 scans) + `annales/INDEX.md` + `annales/FORMULES.md` (2026-11-15).
   - [x] Formules affichées dans les niveaux relues et complétées (2026-11-15) : 20 notions sur 57 (cas manquants : racine non/simple/double en EDO, primitives usuelles, formes $u'f(u)$, décroissante/minorée, partition, Bayes développé, bijection…). Aucune formule fausse trouvée. La fiche du chapitre de la page d'exercice affiche en plus toute la section de `annales/FORMULES.md`.
   - [x] Liste de formules par exercice (champ `formules` dans `parcours/src/*.py`) pour le bouton « Formules de la solution » ; aujourd'hui : formules du niveau. (dict `FORMULES`, 358 puis 582 exercices)
   - [x] Corrigés rédigés pour tous les sujets sans corrigé officiel (2026-11-15).
   - [x] Lectures incertaines vérifiées sur les PDF (2026-11-15) : td4-2030 ex. 1.1 = $-\frac12u$, td5-2030 = $\int_0^1$, td3-2028 cours 2 q5 c illisible mais sans effet (cubique toujours réductible).
4. [x] Parcours APIS suites (15 niveaux, 75 exos, calé sur SR janv. 2025 + ASI janv. 2024). [x] EDO. [x] S2 : APEF (polynômes, fonctions), EV, ALM (2026-11-15). [ ] Les autres matières : physique (S1 méca, S2 énergie, thermo, EM), archi (S1 ×3, S2 ×2), électronique S1 (B1 circuits, B2 régime sinusoïdal et filtres) faits ; restent électronique S2, algo, prog, anglais, méthodo.
5. [x] Scroll adaptatif. [x] Accueil maths dans l'ordre du syllabus (2031, S1, S2).
6. [x] Mail de réinitialisation depuis `morgan@pierref.eu` (via `/opt/pierref/mailer` ; accord donné le 2026-11-14).
