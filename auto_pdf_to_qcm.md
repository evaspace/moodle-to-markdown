Je te propose un pipeline en 3 étapes. Le point clé : l’API Claude lit directement les PDF, y compris les scans, car chaque page est donnée au modèle à la fois en texte et en image. Tu n’as donc besoin ni de pdftotext ni d’OCR (ce que je te disais avant ne vaut plus pour les PDF).
Architecture

annales/<matière>/*.pdf ──► [Étape 1] transcription ──► cache .md (relisible)
                                  │
                                  ▼
                            [Étape 2] analyse ──► profil_examen.json  (1 fois par matière)
                                                         │
cours/<matière>/*.pdf ──► [Étape 3] génération de cartes ◄┘
                                  │
                         validation (ingest.py actuel) ──► DB

Étape 1 : transcrire les annales (scans)

    Un appel par annale : le LLM transcrit chaque exercice en markdown avec le LaTeX en $...$, avec le barème s’il est visible.
    Le résultat est sauvegardé en .md à côté du PDF. Tu peux le corriger à la main si le scan est illisible, et tu ne repaies jamais cet appel.
    Tu peux ajouter [illisible] comme règle dans le prompt, pour qu’il n’invente pas.

Étape 2 : construire le « profil d’examen »

    Tu envoies toutes les annales transcrites d’une matière en un seul appel, et le LLM sort pour chaque notion : fréquence d’apparition (ex. 5/6 annales), type de question (démonstration, calcul, définition, piège classique), niveau de difficulté et chapitre.
    Pour cette étape, utilise le tool use / structured outputs de l’API : le JSON est garanti valide, et il n’y a pas le problème des backslashes LaTeX.
    Le résultat est un fichier profil_<matière>.json d’environ 30 à 60 lignes. Relis-le toi-même : c’est l’étape qui a le plus d’effet sur la qualité du reste, et ça prend 5 minutes.

Étape 3 : générer les cartes depuis le cours, pondérées par le profil

    Tu envoies le PDF du cours (découpé par plages de pages, ~10-15 pages avec 1 page de recouvrement) et le profil dans le prompt.
    Consignes à ajouter au prompt actuel :
        les notions fréquentes dans les annales reçoivent plus de cartes, avec des QCM/TF qui imitent le style d’examen ;
        les notions absentes des annales deviennent une seule carte COURSE courte, voire aucune ;
        il faut signaler en R: les pièges classiques relevés dans les annales.
    La sortie reste au format texte actuel, donc parse_blocks et les validations de ingest.py marchent sans changement.
    Mets le profil dans la partie system avec prompt caching : il est identique pour tous les morceaux de cours, donc très peu cher après le premier appel.

Ce que ça change dans le code

    chunk_text() est remplacé par un découpage de PDF avec pypdf en plages de pages.
    call_llm() envoie le PDF en base64 sous forme de bloc document (comme dans l’exemple de l’API), au lieu du texte.
    Il faut un analyze_exams.py (étapes 1-2) qui écrit profil_<matière>.json.
    Les limites de taille et de pages par requête existent. Vérifie-les dans la doc actuelle, et le découpage par plages de pages les respecte de toute façon.
    Un cache par hash de fichier évite de repayer quand tu relances.

Mes recommandations

    Ajoute une colonne priority à la table card (poids issu du profil) et fais-la peser dans fetch_batch. Sinon les cartes importantes et les accessoires sortent avec la même probabilité. C’est un petit changement de schéma que je peux te faire.
    Ajoute une 2ᵉ passe de vérification : un autre appel relit chaque QCM/TF contre le cours et rejette les douteux. Dans cette architecture, c’est plus important qu’avant, puisque le LLM choisit lui-même ce qui compte.
    Ne mélange pas les matières dans un même profil. Un profil par matière, sinon les fréquences n’ont aucun sens.

Ordre pour aller vite

    analyze_exams.py sur une matière avec 3-4 annales, pour juger la qualité du profil.
    Adaptation de ingest.py aux PDF, test en --dry sur un chapitre.
    Colonne priority, puis passe de vérification si les erreurs de contenu te gênent.

Je peux t’écrire analyze_exams.py et la version PDF de ingest.py d’un coup. Pour caler les prompts, combien d’annales as-tu par matière, et est-ce qu’elles sont plutôt en texte imprimé ou manuscrites ?

