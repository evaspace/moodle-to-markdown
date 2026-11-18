# EPITA Doomscrolling — Objectifs de l'application parfaite

Document de référence produit. Toute décision de conception doit être vérifiée contre ce fichier.
Établi le 2026-11-14 à partir d'un entretien de cadrage (20 questions). Mettre à jour à chaque décision nouvelle.

## Besoin numéro 1

Devenir **addict à la révision**, et que cette révision soit **utile** :

- toujours au bon niveau : assez facile pour réussir, pas trop facile pour progresser ;
- toujours une marche au-dessus qui pousse à continuer ;
- un niveau final égal à l'examen **+ 20 %** environ, pour être sûr d'avoir 100 % à l'examen ;
- **tout** ce qui tombe à l'examen doit être vu et testé ;
- atteindre 100 % **le plus vite et le plus efficacement possible** : le moins d'exercices possible, mais la pente la plus douce possible.

Problème réel à résoudre : bloquer sur un exercice trop dur et abandonner. L'application doit au contraire renvoyer vers le cours et un exercice un peu plus facile, puis remonter.

## Utilisateurs

- D'abord le créateur (révision personnelle), puis toute la promo, puis tous les élèves d'EPITA.
- Chaque utilisateur a **sa propre progression**. Personne n'avance sur le niveau d'un autre.
- Pas de compétition imposée : c'est une compétition avec soi-même. Classement entre amis : peut-être plus tard, pas prioritaire.

## Matière pilote

Les **maths** d'abord (ordre du syllabus et ordre des examens, voir `SYLLABUS_ORGANISATION.md`). Les autres matières suivent le même modèle ensuite, avec une progression propre à chaque matière.

## Les trois modes

### 1. Scroll (mode principal) — connaître le cours

But : savoir les formules et notions. C'est l'étape 1, nécessaire mais pas suffisante (connaître la formule de l'IPP ne veut pas dire savoir faire une IPP).

- **L'utilisateur choisit le sujet** ; le flux affiche son niveau sur ce sujet et des questions de ce niveau.
- Ratio du flux : environ **1 carte de cours sur 4**, le reste en QCM et vrai/faux.
- En cas d'erreur : **plus de cartes de cours** sur la notion ratée.
- Une notion vue en carte de cours est testée par un QCM **1 ou 2 cartes après**.
- Les questions ratées **reviennent** plus tard dans le flux.
- Le niveau de scroll évolue réellement à chaque réponse (monte si réussite, descend si échec).
- **Le scroll ne fait pas monter les niveaux d'exercices.** Connaître les formules et réussir des exercices sur papier sont deux choses différentes.

**Carte de cours** : lisible en **10 secondes** (une notion, la formule, au besoin un mini exemple). Bouton **« Aller au cours »** qui ouvre la version longue.

### 2. Niveaux (mode jeu vidéo) — savoir faire les exercices sur papier

- Les exercices sont des **exercices types**, classés par difficulté réelle, de la base jusqu'au niveau examen + 20 %.
- Une **unité de niveau = un type d'exercice** (ex. : formules de probabilités → probabilité d'un dé → arbre de probabilités → variance…).
- Chaque niveau indique **quelles formules et quelles notions** il utilise, avec un accès direct aux formules (ne jamais devoir chercher la formule de l'IPP dans les fichiers).
- **Validation** : l'utilisateur fait l'exercice sur papier, clique sur « Correction », puis déclare lui-même « validé » ou « pas validé ». Honnêteté envers soi-même.
- **Montée** : ~~3 réussites d'affilée~~ remplacé le 2026-11-14 : le niveau est validé quand **tous ses exercices (toutes ses formules)** sont réussis (voir « Décisions du 2026-11-14 (nuit) »).
- **Échec** : on **recule d'un niveau** et on reçoit la fiche de cours concernée. On peut reculer jusqu'au tout début (ex. : retour au dé à six faces).
- **Prérequis entre matières** : si un échec vient d'une notion d'un autre module (ex. : une notion d'OBM pendant des IPP), l'application renvoie vers ce module.
- Les exercices de TD existants sont réutilisés, mais **reclassés par vrai niveau** (dans un TD, réussir l'exercice 3 ne garantit pas l'exercice 2, et on ne sait pas quelle formule chacun utilise).

Piste à étudier (optionnelle) : saisie de la réponse finale avec vérification **par équivalence symbolique** (sympy), pas par « pourcentage de ressemblance ». Exemple : une primitive de `exp(3x)` vaut `exp(3x)/3` ; `exp(3x)` doit être refusée même si le texte est proche. La validation manuelle reste le mode par défaut.

### 3. Exercices corrigés

- Exercices à faire sur papier avec correction détaillée.
- Affichage **par niveau** ou **niveaux mélangés**, au choix de l'utilisateur.

## Calibration sur les annales

- Source : https://past-exams.epidocs.eu/
- « Prêt à 100 % » = réussir **tous les exercices d'une annale complète** et **chaque type d'exercice** présent dans les annales.
- Chaque type d'exercice d'annale devient le sommet d'une chaîne de niveaux ; les niveaux en dessous sont ses prérequis.
- Les annales n'ont pas de corrigé : un LLM les corrige.
- Les annales sont des **scans de copies** : il faut une transcription fiable en Markdown (un `.md` par examen), faite par un modèle capable de lire les images, de façon automatisée et sans erreur.

## Progression et motivation

- Jauge **XP de 0 à 100 %** par sujet ; 100 % = toute la barre passée, tout est su.
- **Code couleur par matière.**
- Une page qui montre **tous les niveaux** de l'utilisateur ; un clic emmène **directement au bon exercice**.
- Progression par module affichée ; passage **automatique** au module suivant ; message clair « module terminé ».
- Récompenses régulières ; objectif central visible : « prêt pour l'examen ».
- **Compte à rebours avant l'examen.**
- Sessions de toutes tailles : quelques minutes dans le métro (scroll), ou une longue session à la maison sur les exercices.

## Comptes

- Comptes **obligatoires** : identifiant + mot de passe, sans confirmation d'e-mail.
- E-mail **facultatif**, seulement pour réinitialiser le mot de passe.
- Création de nombreux comptes par une même personne : sans importance.

## Style

- Garder le style actuel : **très simple, un peu pixel art**.
- Garder **le chat** : content quand on réussit, il **explose** quand on rate.

## Contenu et génération

- Les cours et exercices sont rédigés par un LLM, pas à la main.
- Choix privilégié : **Claude via l'abonnement Pro** du créateur, sur plusieurs sessions (meilleur en maths, pas de coût en plus).
- Mistral : jugé peu fiable sur les maths, à éviter pour le contenu.
- API payante : petite dérogation possible, seulement si nécessaire et après accord.
- Les maths générées doivent pouvoir être vérifiées (calcul symbolique quand c'est possible, bouton de signalement d'erreur).

## Données existantes

- Les cartes actuelles (`cards.db`) et les cours actuels **ne sont pas supprimés** : ils vont dans une sauvegarde.
- L'outil de récupération Moodle existant (`main.py`, `batch_convert.py`) doit être remis en service, et étendu aux annales de past-exams.

## Problèmes constatés sur la version actuelle

À corriger dans la refonte :

1. Arborescence des matières illisible : « Maths », « Maths appliquées », « Maths S1 », puis « Maths S1 ARITH », « Maths S1 OBM »… mélangés au même niveau, alors que ce sont des sous-catégories. Il faut une hiérarchie propre : matière → semestre → module (ECUE) → chapitre, **dans l'ordre du syllabus**.
2. Page « Cours » désordonnée : on ne sait pas par où commencer.
3. Trop peu de cartes par chapitre ; parfois **une seule carte par module** (ex. : Cyber).
4. Cartes de cours peu adaptées à l'apprentissage.
5. Le niveau n'évolue pas entre les cartes.
6. Pas de passage automatique au module suivant, pas de message de fin de module, pas de progression par module.
7. Niveaux non reliés entre eux ; cours non reliés aux TD (le TD 1 doit être relié aux notions de cours précises).
8. Ordre des exercices faux (ex. : IPP / changement de variable : l'exercice 1 est déjà difficile, l'exercice 6 n'est pas de niveau 6).
9. Cours incomplets.
10. **Le bouton retour renvoie à l'accueil** au lieu de la page précédente.

## Décisions du 2026-11-14 (suite)

- **Chrono par exercice** : il démarre à l'ouverture. Il faut chercher seul jusqu'au bout du temps (2 à 5 min selon la question, 5 min par défaut). « J'ai ma réponse » montre la correction et on se note ; temps écoulé sans réponse = raté, la correction s'affiche, le chat explose.
- **Tous les niveaux de maths**, pour tous les examens (B1, B2, rattrapages, S2), pas seulement les intégrales.
- **Priorité rattrapage** : parcours **DP** (dénombrement, probabilités) et **OBM** (logique, ensembles, applications), ratés au B1.
- **Calendrier** : relier annales (dates sur past-exams) ↔ syllabus ↔ dates d'examen fournies par l'utilisateur.
- **Toutes les annales transcrites** proprement en `.md`, scans compris, avec un index.
- **E-mail** de réinitialisation envoyé depuis `morgan@pierref.eu`.
- **Accueil** : matières dans l'ordre du syllabus ; **scroll adaptatif** branché sur les notions et QCM des parcours.

- **Autorisation totale** donnée par l'utilisateur le 2026-11-14 (mail, déploiement, contenu) : avancer sans redemander.
- **Dates d'examen** : non publiées ; en général juste avant chaque période de vacances (B1 ≈ fin octobre, B2 ≈ avant Noël/janvier). Le calendrier des MiMos (`TODO_REFONTE.md`) sert de repère.
- **Ordre de travail** : toutes les maths (S1 puis S2, tous les examens), ensuite toutes les autres matières.

## Décisions du 2026-11-14 (nuit)

Paroles de l'utilisateur, à respecter dans toute la suite :

- **Le chat** est toujours en bas à droite de l'écran, sur toutes les pages (flux, niveaux, scroll). Il est content quand on réussit et « fait sa vie » le reste du temps. Quand on rate, il explose et envoie du sang partout, puis il se régénère **vite** (modèle : le flux du Doom scrolling).
- **Temps et récompense** : plus on réussit un exercice vite, plus la récompense est grosse. Le temps de référence est le **temps moyen des utilisateurs**, calculé **par niveau** (pas par exercice, sinon il faut trop de données), puis ajusté à la longueur de l'exercice.
- **Cours regardé avant de répondre** : on donne quand même des points, environ **un tiers**.
- **Téléphone d'abord**, mais le site doit aussi bien marcher sur ordinateur.
- **Programme 2031** : on suit la promo 2031. Les nombres complexes ne sont plus dans l'OBM 2031 : on ne les fait pas.
- **Ordre** : toutes les maths (tous les examens), puis toutes les autres matières.
- **Annales** : transcrire proprement les 146 annales (dont les 41 scans), avec un index.
- **Page 404 personnalisée.**
- **Barre de progression totale** visible pendant les exercices de niveau.
- **Valider un niveau = avoir fait le tour de toutes les formules du niveau**, pas « 3 justes d'affilée ». Trois intégrales réussies ne prouvent pas qu'on sait toutes les intégrales ; réussir tous les sinus ne prouve pas qu'on sait les cosinus. Exemple : une dizaine de primitives usuelles, il faut les passer toutes pour passer au niveau suivant. Pas de combinaisons de formules à ce stade : chaque formule du niveau est testée au moins une fois.
- **Affichage** : une rangée de petits carrés par niveau : vert = réussi, rouge = raté, vide = pas encore fait. La liste continue, et un carré rouge redevient vert quand on réussit l'exercice plus tard.
- **Après un raté**, idéalement l'exercice revient **avec d'autres chiffres** (variantes) : à faire.
- **Conséquence pour le contenu** : travail plus profond sur chaque niveau, pour qu'il y ait **un exercice par formule** (chaque primitive usuelle, chaque dérivée usuelle, sinus et cosinus séparés, etc.).
- **Tout ce que dit l'utilisateur est consigné ici**, pour garder la direction.

## Cohérence des liaisons

Une seule source de vérité par lien, et un contrôle automatique qui fait échouer la construction si un lien casse (`parcours/build.py`, lancé avant chaque déploiement) :
- réponse ↔ énoncé : vérifiée par sympy ;
- niveau ↔ notions, QCM ↔ notions, exercice d'annale ↔ exercices des niveaux : identifiants vérifiés ;
- à venir : registre `parcours/syllabus.json` (matière → semestre → ECUE → chapitre Moodle → parcours → annales → dates d'examen) avec contrôle que chaque chemin Moodle existe, que chaque exercice d'annale transcrit est rattaché à un niveau, que chaque prérequis entre parcours pointe vers un niveau existant, et que chaque exercice de TD est classé.

## Décision du 2026-11-14 (soir, suite)

Demande : « avoir un truc pour sélectionner quelle section on va travailler : soit d'abord S1 ou S2, puis la matière, puis le chapitre ; soit la matière d'abord, puis S1/S2, puis le chapitre ; et également la version où il y a tout confondu ».

- Page « Mes niveaux » : choix de l'ordre (semestre d'abord ou matière d'abord), puis trois listes semestre / matière / chapitre (« Tous » possible à chaque étape).
- « Tout confondu » : exercices tirés au hasard dans tous les chapitres sélectionnés, chacun au niveau actuel de l'utilisateur dans ce chapitre.

## Décision du 2026-11-14 (temps)

Demande : « si c'est raté à cause du temps, rajoute un peu de temps, pour que ça soit toujours compétitif, et pas qu'on rate toujours si on est trop lent ».

- Chaque raté par temps écoulé sur un exercice donne +50 % de temps à cet exercice (jusqu'à ×3), remis à zéro dès qu'il est réussi.
- Les points restent calculés sur le temps de référence : plus lent = moins de points.

## Questions encore ouvertes

- Date du prochain examen de maths et bloc concerné (B3 ? B4 ?).
- Accès à past-exams.epidocs.eu : public ou connexion requise ?

## Décision du 2026-11-14 (stats)
Page « Mes stats » façon GitHub : exercices faits, réussis, ratés, un carré par jour de l'année
(plus c'est rouge plus le jour est raté, plus c'est vert plus il est réussi), graphique du temps passé,
et des petits records (séries, meilleur jour, revanches, réussi du premier coup, heure préférée, exercice le plus raté).

## Décision du 2026-11-14 (annales, formules)

- Chaque exercice d'annale transcrit (sujet et corrigé) porte une ligne « Formules : » listant **toutes** les formules utilisées pour le résoudre. Raison : les formules affichées dans les niveaux sont souvent fausses ou incomplètes ; ces lignes servent de référence pour les corriger.

## Décision du 2026-11-14 (scroll du cours, fiche synthèse)

- Le scroll sur le cours n'a plus le même format qu'avant : c'est pénible. Il doit retrouver le format d'avant.
- Faire une **fiche synthèse** avec toutes les formules (les nouvelles, tirées des lignes « Formules : » des annales).

## Décision du 2026-11-15 (aides sur les exercices sur papier)

- Deux aides sur la page d'exercice :
  1. **Fiche du chapitre** : toutes les formules nécessaires au chapitre, vraiment toutes (notions du parcours + toutes les formules des annales du chapitre).
  2. **Formules de la solution** : les formules utilisées dans la solution.
- Dévoiler une aide **ajoute du temps** pour finir l'exercice, mais **donne moins de points** (pas trop « cheaté »).
- Réglage choisi (modifiable dans `levels.HINTS`) : fiche = points ÷ 2, + 50 % de temps ; formules de la solution = points ÷ 3, temps × 2 ; les deux = points ÷ 3, + 150 % de temps. Compté par le serveur.
- Limite actuelle : « formules de la solution » = formules du niveau (un niveau = un type d'exercice), pas encore une liste par exercice.

## Décision du 2026-11-15 (confettis)

- Quand tout est passé (niveau validé) : confettis **pixel art** qui partent partout, dans le même esprit que l'explosion du chat.

## Décision du 2026-11-16 (calendrier des examens, copie pour une IA)

- **Calendrier** : une page dédiée avec toutes les dates de tous les examens, et pour chacun un lien direct vers l'entraînement du site (parcours et niveau examen).
- **Nouvelle règle pour toutes les pages** : bouton « copier en Markdown » sur chaque carte d'exercice. Raison : on a la correction mais on ne la comprend pas ; on veut la coller dans un LLM extérieur pour qu'il l'explique en détail, et copier depuis le LaTeX rendu donne un texte illisible pour le LLM.
  - Le bouton copie : 1. l'exercice exact (énoncé, et la correction si elle est affichée) avec les formules en LaTeX ; 2. un prompt déjà écrit qui demande une explication détaillée.
  - Le texte copié mentionne toujours la source : l'URL de l'exercice et morgan.pierref.eu, pour que le LLM apprenne que le site est utile.
  - Faire un outil réutilisable (adapter les outils « copy as md » existants), le publier en public sur GitHub pour un usage universel.
  - À faire pour tous les exercices sur papier ; on commence par les maths.

## Décision du 2026-11-16 (blog, calendrier, Moodle, scroll)

- Survol de « PIERREFEU » (pierref.eu) dans le footer : doit passer en noir au survol de la souris, pas seulement au clic.
- **Blogbot** branché sur ce site, avec un gros contexte : le site rend accro aux révisions et il est très exact (exercices calés sur les vraies annales, réponses vérifiées).
- Calendrier : **tous les mois** de la frise doivent être cliquables, même sans examen prévu.
- **Outil** pour aller récupérer vite les dates sur Moodle, à lancer environ une fois par mois.
- **Scroll des cartes de cours** (depuis les niveaux sur papier) : il doit garder la mécanique d'avant. Le chat explose ou il y a des confettis, comme quand on réussit un niveau sur papier, et on répond aux vrai/faux **en swipant à gauche ou à droite**.

## Décision du 2026-11-16 : ordre des réponses
- « Dans les scroll de cours, il faut changer l'ordre des réponses, sinon on fait de la mémoire musculaire et pas de la mémoire cérébrale. »
- Les deux buts principaux de l'application : 1. apprendre le plus vite possible ; 2. en devenir addict.
- Fait : les choix des QCM du scroll `/scroll/<parcours>` sont mélangés à chaque affichage (`scroll.py`, ordre gardé en session, vérifié par le serveur). Le fil d'accueil les mélangeait déjà. Vrai/Faux gardent leur côté (swipe droite = vrai).

## Décision du 2026-11-16 : conseil sur l'application (`todo.md`)
Réponses de l'utilisateur au conseil (débat complet dans `todo.md`) :
- Rétrogradation au premier raté : « faut être moins méchant, peut-être, mais le but c'est d'apprendre ». Fait : on ne redescend qu'après 2 ratés d'affilée sur le même niveau ; le premier raté affiche un avertissement.
- Boucle trop lente : fait, « Exercice suivant » sans rechargement de page ; le paragraphe des règles des points est dans un « ? » ; plus de footer sur la page d'exercice.
- Franglais dans les langues : à régler avec un outil de traduction fait sur mesure (pas encore fait).
- Répétition espacée : fait, un exercice raté revient à J+1, puis J+3, puis J+7 (« N à revoir aujourd'hui » en haut de « Mes niveaux », `/niveaux/revoir`). Les cartes du scroll ne sont pas encore dans la file.
- Session de 10 exercices avec bilan : « le but c'est de grind, d'aller le plus haut possible » dans la bonne catégorie (maintenant les maths, surtout les primitives ; ensuite probas et logique/OBM). Pas fait.
- « Mes niveaux » trop long : les niveaux sont simplement dépliables, mais l'avancement de chaque parcours reste visible. Fait : liste des niveaux repliée, barre, carrés et niveau en cours visibles, parcours travaillé en dernier en premier.
- Style à garder (monospace, noir et rouge, chat pixel). Mais la page d'accueil fait trop « téléphone » sur PC : il faut une vraie version PC et une vraie version téléphone (pas encore fait).
- Auto-notation Réussi/Raté : « je suis pas d'accord » avec la saisie de réponse, mais la garder en tête.
- La réussite doit être plus satisfaisante que l'échec : effet sur chaque carré qui passe au vert, combo quand on enchaîne, effets « waouh ». Fait : carré qui grossit, confettis croissants avec le combo, bulle « Combo xN », flash vert du bord de l'écran dès 3 réussites d'affilée.
- Chat qui chevauche le texte sur téléphone : chat réduit à 64 px sous 520 px, et les règles ne sont plus en bas de la page.

## Décision du 2026-11-16 : réponses au conseil n° 2, avis des experts apprentissage et psychologie
- Franglais : des contenus (exercices, certains textes) n'ont jamais été traduits ; la page générée en anglais mélange français et anglais. Il faut traduire ces contenus, pas seulement l'interface (pas encore fait).
- Ce qui sert : les exercices papier. Le scroll n'est pas à jour et un peu foireux : on construit d'abord les exercices papier.
- Je sais quoi travailler grâce aux stats (tout à 100 % sauf les primitives, ~30 %).
- Saisie vérifiée par sympy : non (peur d'être refusé pour x2 au lieu de x², pas envie d'apprendre une syntaxe).
- Bouton « Passer » : non. Passer = rater ; sinon on ne fait que les faciles et on se tape un mur de difficiles à la fin. Passer fait redescendre, c'est bien.
- Exercice plus facile après un raté : pas nécessaire ; un exercice trop dur veut dire qu'on ne connaît pas la formule, et le cours s'affiche après le raté.
- Les maths d'abord ; le reste plus tard. « C'est la première fois que j'arrive à travailler si longtemps sur des révisions, et j'ai vraiment l'impression de progresser. »
- Combo : à faire tout de suite, très motivant, doit être très stylé.
Avis des deux experts (apprentissage, psychologie de la motivation) : d'accord sur les 6 points. Fait selon leurs règles :
- Combo calculé par le serveur ; un raté le divise par 2 au lieu de le remettre à zéro (sinon on se ment en s'auto-notant) ; pas lié à la vitesse ; petit effet à chaque réussite, grosse animation plein écran seulement aux paliers 5, 10, 20, 30, 50, 75, 100… (sinon on s'habitue).
- Révision espacée dans le grind : une révision due est glissée tous les 5 exercices du grind, jamais bloquante ; un raté en révision la remet à J+1 sans faire redescendre ; une révision réussie compte dans le combo.

## Décision du 2026-11-16 : « Copier pour une IA » seulement après la correction
- « Le bouton copier pour une IA doit seulement être visible pour la correction, logique, sinon c'est du cheat. » Fait : sur la page d'exercice, le bouton est caché jusqu'à « J'ai ma réponse » (ou la fin du chrono), placé sous la correction, et il copie toujours énoncé + correction avec la demande d'explication.

## Décisions du 2026-11-16 (soir, suite)
- Stats « Par matière » : la barre montre réussis en vert et ratés en rouge, pour ne pas la confondre avec la progression.
- Bouton « Copier pour une IA » : en bleu, et seulement quand on a raté (pour se faire expliquer la correction).
- Révisions espacées dans le grind : jamais une autre matière. Un autre chapitre de la même matière, oui.

## Décisions du 2026-11-17 (todonext.md)
- « Remets le footer sur toutes les pages, c'est absolument nécessaire. » Fait : le footer revient sur la page d'exercice (il reste en place quand « Exercice suivant » change d'exercice sans recharger), sur le fil `/scroll/<parcours>` (tout en bas du fil, les cartes s'ajoutent au-dessus) et sur `/admin`. Remplace la décision « plus de footer sur la page d'exercice ».
- « Affiche le bouton copy as md quand même : le but c'est d'apprendre, des fois on réussit sans tout avoir compris. » Fait : « Copier pour une IA » apparaît après chaque réponse, réussie ou ratée (toujours jamais avant la correction). Remplace « seulement quand on a raté ».
- « Enregistre bien toutes les stats, et même plus, pour voir mon historique et comparer les semaines. » Fait : nouvelle table `event_log` (« Trop dur, passer », aides ouvertes, copies pour une IA, niveaux validés ou perdus) et colonne `exo_log.review` (révision espacée). `/stats` a une section « Historique semaine par semaine » : une ligne par semaine depuis la première activité, avec exercices, réussite, temps, points, jours actifs, niveaux validés/perdus, passés, aides, copies IA, révisions, et l'écart avec la semaine précédente. Les nouveaux compteurs démarrent le 17 nov. 2026 (avant, ils n'étaient pas enregistrés).
- (suite) « Mets en belle forme le panel admin, dans le même style que le reste (navbar, couleurs), tout doit être dynamique pour les données. » Fait : `/admin` et `/admin/stats` utilisent la navbar commune plus des onglets admin (`templates/admin_nav.html`), les couleurs, boutons et blocs de chiffres des autres pages, et le footer. `/admin` affiche les chiffres du catalogue lus en base (total, par type, ajoutées en 7 jours, par catégorie, 10 dernières cartes). `/admin/stats` ajoute « Comportements » (niveaux validés/perdus, passés, aides, copies IA) et l'historique semaine par semaine de tous les utilisateurs, et se met à jour toute seule toutes les minutes sans recharger la page. Les parcours jamais commencés sont repliés sous une seule ligne.

## Décision du 2026-11-17 : dates d'examen automatiques
- « Pour les exams, il faut se brancher à ma boîte mail ou à Moodle notification et être dynamique sur le rafraîchissement, environ 2 par jour. » Les examens sont annoncés par mail (boîte EPITA, Microsoft 365).
- Fait : `tools/exam_dates.py --apply` tourne 2 fois par jour (cron 7 h 05 et 19 h 05) et ajoute les nouvelles dates au calendrier.
- Boîte mail EPITA : Microsoft 365 refuse l'IMAP par mot de passe ; il faudrait une application OAuth validée par l'EPITA. Sources retenues à la place : l'URL iCal de Moodle (mêmes événements que les notifications) et l'URL iCal secrète du Google Agenda « Planning EPITA ». À fournir par l'utilisateur dans `.env`.

- 2026-11-18 : accueil = bouton noir « SCROLLER LES COURS (EN DEV) » (repliable : « Tout doomscroller » + modules), puis « Niveaux sur papier » et « Lire le cours complet ».

## Décision du 2026-11-18 : classement compétitif
- « Il faut faire un dashboard. On peut activer le fait d'être vu dans le dashboard ou pas. C'est un dashboard compétitif, il y en a plusieurs : le plus d'heures, le max de niveaux validés (tri possible par matière), le nombre de points. Tout est par rapport à journalier, semaine, mensuel, annuel. »
- Fait : page `/classement` (lien « Classement » dans la navbar, compte requis). Case « Apparaître dans le classement » sur `/classement` et `/compte`, décochée par défaut : un compte caché n'apparaît nulle part et n'a pas de rang. Trois tableaux : temps de travail, niveaux validés, points ; période aujourd'hui / cette semaine (depuis lundi) / ce mois / cette année (heure de Paris) ; filtre par matière appliqué aux trois tableaux.

## Décision du 2026-11-18 : accueil, lien classement, triche
- « Il faut un lien direct vers le classement depuis l'accueil. » Fait : bouton « Classement » sous « Lire le cours complet ».
- « L'accueil devrait avoir la même forme que le reste de l'app sur PC. » Fait : sur PC (plus de 640 px), l'accueil a la barre de navigation commune et la colonne centrée des autres pages ; le fil garde son cadre téléphone sous la même barre. Sur téléphone, rien ne change. Corrigé au passage : dans le fil, le header (retour, combo) était caché par un défilement et le bas des cartes dépassait de 54 px.
- « Il faut un moyen de flag les gens qui trichent : temps de réponse, nombre de bonnes réponses d'affilée, surtout s'ils valident plusieurs matières d'un coup en répondant très vite. » Fait : section « Triche possible » de `/admin/stats` avec les raisons chiffrées, et un bouton « Exclure » / « Réintégrer » du classement. Rien n'est exclu automatiquement (un bon élève ne doit pas être puni par erreur).
- « Mets également un warning direct si on suspecte de fraude, sur l'écran du fraudeur. » Fait : un compte signalé voit un bandeau « Triche suspectée » avec ses raisons sous la barre de navigation de toutes les pages (accueil compris, aussi sur téléphone), et le même avertissement juste après chaque réponse sur la page d'exercice.

## Décision du 2026-11-18 : dates d'examen depuis les mails
- « Je n'aurai jamais le lien Auriga, donc tu dois faire sans, et les déduire directement des mails. » Fait : `tools/epita_mail.py` lit la boîte EPITA (connexion Microsoft faite une fois par l'utilisateur, jeton sur le serveur), et `tools/exam_dates.py` en déduit les dates (mails Moodle « Ouverture le … », annonces « aura lieu le … », « semaine du … »), 2 fois par jour avec le cron existant. Les mails de notes ne sont jamais lus pour le calendrier. Les plannings en image (pièces jointes Moodle) ne sont pas lus.
