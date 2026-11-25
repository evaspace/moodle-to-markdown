# Plan beta : réviser sans effort

Objectif (README_OBJECTIFS, « zéro effort ») : l'élève ne règle rien et ne saisit rien. Il lit un conseil placé au bon moment, fait les exercices qu'on lui présente et lit la copie 20/20 de chaque exercice. Tout le reste s'adapte seul.

## Déjà en place (`beta.py`, `/admin/beta`)

- Planning Auriga (cron 30 min), dates d'évaluation, retard par ECUE contre la classe, prérequis en chaîne.
- Créneaux libres, révision « à chaud » de 20 min, au plus 2 séances par ECUE et par jour.
- Rythme horaire mesuré (`rhythm`, dès 40 réponses) et longueur de séance mesurée (`block_length`).
- Règles d'humanité : repas, rien après 22 h, samedi soir, plafond 3 h / 5 h.

## État réel vérifié (2026-11-23, 21 h 40, sur mes vraies données)

Planificateur lancé sur le compte propriétaire : 43 créneaux Auriga, 286 réponses.

- Les règles s'appliquent bien dans le calcul. Rythme mesuré actif (286 ≥ 40), séance de 45 + 10 déduite de mes réponses, plan de demain cohérent (« à chaud » après chaque cours, puis C, algo, analyse triés par retard et date d'évaluation).
- Mais personne n'est prévenu. Le plan n'existe que si j'ouvre `/admin/beta`. Il n'y a ni rappel, ni lien depuis l'accueil ou un exercice, ni Google Calendar.
- Personne ne vérifie si le plan est suivi. Rien ne compare blocs proposés et exercices faits.
- La version en ligne a un commit de retard : le live est sur 649958b, la dernière version (couleurs, bloc compte à rebours) est 2ebed4c.
- Le rythme est bruité : 8 à 55 réponses par heure, sans correction de difficulté. Mes meilleures heures mesurées (19 h : 73 %, 23 h : 75 %) tombent sur le repas et après 22 h, donc le planificateur les écarte sans le dire.

## Ce qui manque

1. Un bloc du planning renvoie vers un parcours entier, pas vers les exercices précis à faire.
2. Pas de mémoire par exercice : un exercice réussi n'est jamais reproposé au bon moment, un raté non plus.
3. Les paramètres fixes (plafond journalier, seuils) ne s'ajustent pas à ce que l'élève fait vraiment.
4. Les conseils sont une liste en bas de page, pas au moment où ils servent.
5. La copie 20/20 existe par matière (listes), pas par exercice. Les 3267 exercices ont `enonce`, `sol`, `ans` mais aucun champ `copie`.
6. Il faut ouvrir le site pour savoir quoi faire.

## Principe d'adaptation

Une seule boucle, sans saisie : plan proposé, puis réponses observées, puis paramètres mis à jour, puis nouveau plan. Chaque paramètre a une valeur par défaut tant qu'il n'y a pas assez de données, puis passe à la valeur mesurée.

| Paramètre | Mesure (déjà en base) | Défaut |
|---|---|---|
| Meilleures heures | réussite par heure, corrigée de la difficulté (comparée au temps moyen des autres sur le même exo) | matin |
| Longueur de séance | baisse de réussite après 25 min (`block_length`) | 45 + 10 |
| Charge par jour | part des blocs proposés réellement faits sur 7 jours : moins de 60 % alors plafond −20 %, plus de 90 % alors +10 % (bornes 1 h à 5 h) | 3 h / 5 h |
| Fatigue | réussite et vitesse qui chutent dans la séance en cours | rien |
| Mémoire par exercice | succès ou échec de chaque `exo_id` | voir étape 1 |

Bloc « fait » = au moins 5 réponses de l'ECUE dans la fenêtre du bloc (±30 min). Rien à cocher.

## Étapes (une branche chacune, chacune utile seule)

### 0. Signaler activement (`feat/beta-signal`), avant tout le reste

Fait le 2026-11-24 (branche `feat/beta-signal`) : bandeau, flux `.ics` (adresse sur `/admin/beta`, à ajouter dans Google Agenda par URL), fait/manqué, phrase de conflit. Le plan du jour est figé au premier calcul (`beta_plans.json`), sinon on ne pourrait pas dire si un bloc passé a été fait. Pas encore branché dans auriga2google : abonnement direct à l'URL.

- Bandeau « Maintenant » en haut de l'accueil et de chaque page d'exercice (compte admin d'abord) : le bloc en cours ou le prochain, avec son lien et sa raison en une ligne.
- Flux `.ics` des blocs (étape 5 avancée ici) : le téléphone notifie à l'heure du bloc.
- Suivi : bloc fait ou manqué, calculé depuis `exo_log`, affiché sur la grille (plein = fait, barré = manqué).
- Conflit visible : quand mes meilleures heures mesurées tombent dans une plage protégée (repas, après 22 h), une phrase le dit au lieu de l'ignorer.

### 1. Séance concrète (`feat/beta-seance`)

Fait le 2026-11-24 : `/beta/seance/<ecue>` et `beta.seance_next`. Écart au plan : la révision espacée existante (`levels.due_reviews`, J+1/J+3/J+7 après un raté) est réutilisée au lieu d'un Leitner ×2,5 sur tous les exercices, et la séance redirige vers la page d'exercice existante au lieu d'un nouveau gabarit.

- `beta.queue(account, ecue, n)` : liste ordonnée d'`exo_id`.
  1. Exercices à revoir (dus) de l'ECUE.
  2. Exercices ratés dans les 3 derniers jours.
  3. Exercices suivants du niveau en cours.
- Révision espacée simple (boîtes de Leitner) : réussi alors intervalle ×2,5 (1, 3, 7, 18 j…), raté alors retour à 1 j. Calculé depuis `exo_log`, sans nouvelle table.
- Route `/beta/seance/<ecue>` : enchaîne les exercices de la file, avec les mêmes cartes qu'un niveau. Chaque bloc de la grille pointe dessus au lieu de `/niveaux/<parcours>`.
- Tests : `tests/test_beta.py` (intervalles, ordre de la file, bloc fait ou pas).

### 2. Adaptation automatique (`feat/beta-adapt`)

Fait le 2026-11-24 : plafond mesuré (`beta.load`, `beta.caps`) et rythme corrigé de la difficulté (`score`). La difficulté = réussite lissée des autres élèves sur le même exercice, pas leur temps. La fatigue en direct passe à l'étape 3, avec son bandeau.

- `beta.load(logs, plans)` remplace `CAP_COURSE_DAY` / `CAP_FREE_DAY` par le plafond mesuré.
- `rhythm` corrigé de la difficulté : une réussite sur un exo dur compte plus qu'une réussite sur un exo facile.
- Fatigue en direct : trois échecs de suite, ou un temps de réponse au-delà de 1,5 fois la moyenne de l'élève, alors pause proposée maintenant (étape 3).
- Tout reste dans des fonctions pures de `beta.py`, testées.

### 3. Conseils au bon endroit (`feat/beta-conseils`)

Fait le 2026-11-24, avec la fatigue en direct de l'étape 2. Limite : le piège 20/20 vient de la liste par matière (en algo, une règle OCaml peut tomber sur un exercice Python) tant que l'étape 4 n'a pas les barèmes par type d'exercice. La liste « Copie 20/20 » reste sur `/admin/beta` comme référence avant examen.

Un conseil = une phrase, affichée là où l'action se passe. On retire la liste fixe.

| Moment | Où | Exemple |
|---|---|---|
| Avant la séance | en tête de `/beta/seance` | « Mécanique : 2 exos ratés hier d'abord, puis le niveau 4. » |
| Après un échec | sous la correction | le piège 20/20 du type d'exercice (unités, hypothèses du théorème…) |
| Fin de bloc | écran de pause | « 10 min loin de l'écran, de l'eau. Reprise à 16 h 05 avec Algo. » |
| Fatigue détectée | bandeau dans la séance | « Ta réussite baisse : pause maintenant, la suite est gardée. » |
| Soir | haut de `/admin/beta` | le plan de demain en 3 lignes |

### 4. Copie 20/20 par exercice (`feat/copie-2020`)

Les critères viennent de faits vérifiables, pas d'opinions.

Sources, dans cet ordre de preuve :
1. Barèmes officiels des annales : 168 fichiers de `annales/md` portent des points par question (807 marques « (n pts) »), et 129 PDF de correction officielle sont dans `annales/raw`. Ce qui rapporte des points est écrit noir sur blanc.
2. Corrections officielles des TD de l'année (Moodle S1-MATHS-2031) : la forme de rédaction que les profs attendent.
3. Recherche publiée, seulement pour la méthode d'apprentissage : effet de test (Roediger et Karpicke 2006), exemples rédigés puis estompés (« worked examples », Sweller ; Renkl), auto-explication (Chi 1989). Chaque règle de méthode cite sa source dans le code.

Interdit : une règle de copie sans source. Si un barème ne dit rien, la règle n'existe pas.

Méthode qui s'apprend : un seul squelette par type d'exercice, toujours le même ordre, déduit des barèmes. Exemple pour les maths : hypothèses citées, théorème nommé, calcul, résultat encadré avec unité, vérification. Ordre d'apprentissage :
1. Copie 20/20 complète montrée (exemple rédigé).
2. Squelette à trous sur l'exercice suivant du même type.
3. Squelette seul.
4. Rien : l'élève rédige, la liste de contrôle vérifie.

Mise en œuvre :
- `annales/tools/baremes.py` extrait, par type d'exercice (`Type :` déjà présent dans chaque exo des annales), les étapes qui portent des points. Résultat : `parcours/baremes.json`, relu à la main.
- Champ `copie` par exo, construit sur ce squelette. Onglet « Copie 20/20 » à côté de la correction.
- Ordre de rédaction : évaluation la plus proche d'abord. Le build avertit si un parcours évalué dans les 14 jours a des exos sans `copie`.

Fait le 2026-11-24 (partie 1, exemple rédigé). Constat : les annales donnent les points par exercice (857 marques « (n points) »), presque jamais par étape ; les barèmes détaillés sont manuscrits dans quelques scans de physique. Décision de l'utilisateur : la copie modèle vient des corrections officielles. `annales/tools/baremes.py` prend chaque exercice des corrigés officiels (pas les « corrigés rédigés » du site) qui porte un `Niveau`, avec ses points et le total quand le fichier les donne, et écrit `parcours/baremes.json` (256 exercices, 81 niveaux). Sous la correction, la page d'exercice montre le corrigé officiel le plus récent du niveau (« Copie 20/20 », bloc repliable, propriétaire seulement comme le reste de la beta). `parcours/build.py` et `baremes.py` listent les parcours évalués dans les 14 jours qui ont des niveaux sans copie officielle.
Reste : squelettes à trous (étapes 2 et 3 de l'ordre d'apprentissage), à écrire à la main depuis ces corrigés, évaluation la plus proche d'abord ; points par étape lus sur les scans de physique avec barème.

Fait le 2026-11-24 (partie 2, branche `feat/copie-squelettes`) : `squelettes.py` contient 19 squelettes écrits à la main, un par type d'exercice, pour les trois parcours APIS (test du 7 décembre, examen du 14 décembre) : suites (niveaux 1 à 12), primitives et intégrales (1 à 12), équations différentielles (1 à 10). Chaque squelette cite le corrigé officiel d'où vient son ordre (`source`, clé de `baremes.json`, vérifiée par `tests/test_squelettes.py`). Les niveaux examen (annales complètes, examen + 20 %) mélangent les types : pas de squelette. Le palier dépend du nombre d'exercices déjà faits sur le type, tous ses niveaux confondus : 0 → corrigé officiel déplié sous la correction ; 1 à 2 → squelette à trous au-dessus de « J'ai ma réponse » ; 3 à 5 → étapes seules ; 6 et plus → liste « vérifie ta copie » sous la correction. Sans corrigé officiel sur le niveau, on commence aux trous. Propriétaire seulement.
Suite le 2026-11-24 : 15 squelettes de plus pour DP (dénombrement, cardinaux, double comptage, équiprobabilité, probabilités totales et Bayes, indépendance, loi et variance, binomiale) et OBM (négation, quantificateurs, contraposée, récurrence, image, injection et surjection, relations). Total : 34 squelettes sur 54 niveaux. Pas de squelette quand aucun corrigé officiel ne couvre le type : OBM 1, 2 et 8, DP 4 et 8.
Reste : squelettes des autres matières (archi 68000 n'a aucun corrigé officiel : rien à écrire tant qu'il n'y en a pas) ; points par étape lus sur les scans de physique avec barème.

### 5. Le plan vient à l'élève (`feat/beta-ics`)

- Route `/beta/plan.ics?t=<jeton>` : blocs de révision des 7 prochains jours, chacun avec le lien vers sa séance.
- auriga2google l'ajoute au flux Google Calendar, comme `calendrier.json` pour les examens. Le téléphone notifie, plus besoin d'ouvrir le site.

### 6. Plus tard

Ouvrir la beta aux autres élèves : chacun son planning auriga2google, ses propres paramètres. Le code est par compte dès l'étape 1.

## Ce qui ne sera pas fait

- Aucune saisie manuelle (énergie, sommeil, repas) : contraire au zéro effort. Les règles d'humanité restent fixes.
- Pas de FSRS ni de ML : Leitner et des moyennes suffisent tant qu'il n'y a qu'un utilisateur.
- Pas de test A/B.

## Vérification

- `.venv/bin/python -m unittest tests.test_levels tests.test_scroll tests.test_beta` à chaque étape.
- Mise en ligne une seule fois en fin d'étape, par l'utilisateur (`tools/deploy.sh`).

Fait le 2026-11-25 (partie 3) : copie 20/20 rédigée par exercice, parcours suites S1 complet (`COPIES` dans le fichier du parcours, branché par `parcours/build.py`, champ `copie` ; les exercices multi joignent les copies de leurs parties ; formules vérifiées avec KaTeX 0.16.9, 0 erreur). Reste : intégrales, EDO, DP, OBM, S2, puis les autres matières.
