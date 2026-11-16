ù le conseil est d'accord (5/5)

- La rétrogradation au premier raté est le défaut n°1. J'ai vérifié dans levels.py:156 (apply_result) : un seul raté sur ton niveau actuel te fait descendre d'un niveau, sur-le-champ. Un soir de fatigue peut te faire dégringoler en cascade, et tu n'ouvres plus l'appli le lendemain., javoue faut etre moins mechant , peutetre, mais le but cest dapprendre,
- La boucle est trop lente. Captures sur téléphone : 
  - la page se recharge à chaque « Exercice suivant » ;
  - le paragraphe de ~90 mots sur les règles de points revient à chaque exercice ;
  - gros probleme sur les langues, il y a beaucoup de franglais, a regler avec un outil de traduction fait sur messure.
- Il n'y a pas de répétition espacée. Un niveau validé est ensuite oublié, alors que le B2 est dans environ 6 semaines. Il faut qu'un rouge revienne à J+1, puis J+3, puis J+7. « 12 à revoir aujourd'hui » devient alors la raison d'ouvrir l'appli, et ta série de jours repose enfin sur quelque chose.
- Il n'y a pas de session avec un début et une fin. Rien comme « 10 exos, 3/10 » suivi d'un écran de bilan. Sans fin, pas de « j'ai fini », donc pas d'habitude. il a pas tord mais le but cest de graind,daller le plus haut possible, actullement je suis en retard mais je travail donc cest deja ca, je trouve, mais il faut pas que je me mettent a plus travailler, oopsie 
- « Mes niveaux » est trop long. La page fait 37 000 px sur téléphone. Il faut montrer en premier ton niveau actuel et le prochain exercice, et replier le reste. qui sont juste simplement depliable mais il faut laisser la visiblité sur lavancement du niveau sur le niveau, cest surtout a quil faut montrer 
- Le style est à garder. Le monospace, le noir et rouge et le chat pixel sont cohérents. Ne le « polis » pas , le seul truc dommage cest ladaptation telephone est trop forcé sur la page dacceuil quand on est sur pc, il faut une vrai version pc et une vrai version telephone,.

Où le conseil se dispute

- Auto-notation Réussi/Raté. Le Contrarian et l'Executor disent « tu vas te tricher à 23 h » et veulent saisir la réponse puis la vérifier par sympy. Tu as choisi l'honnêteté envers toi-même (README_OBJECTIFS.md). Mon avis : garde l'auto-notation par défaut, et ajoute la saisie seulement pour les réponses courtes (Q d'une bascule, une valeur numérique). C'est plus rapide que de lire une correction. je suis pas daccord mais garde le en tete, 
- Indices payants (÷2, ÷3). Le Contrarian dit que ça te pousse à ne pas apprendre quand tu bloques, et veut un premier indice gratuit qui fasse seulement revenir l'exercice plus tôt. C'est ta décision du 15/11, elle est défendable. À revoir seulement si tu te vois rester bloqué plutôt qu'ouvrir la fiche.
- Valider à 100 % de carrés verts ou à 80 %. Le Contrarian veut 80 %. Tu as décidé « toutes les formules », et c'est juste pour l'examen. Le blocage vient de la rétrogradation, pas de ce seuil : corrige la rétrogradation et garde le 100 %.
- Promo, classements et prédiction de note (Expansionist) contre « pas maintenant » (Executor). L'Executor a raison avant le B2.

Angles morts (revue croisée)

J'ai fait la revue croisée et la synthèse moi-même, sans 6 agents de plus, pour économiser ton quota. Ce que les 5 conseillers ont tous raté :
- Rater est le meilleur moment du jeu. Raté = explosion, sang, vibration. Réussi = une petite bulle « Bien joué ». La récompense la plus spectaculaire tombe sur l'échec. Il faut rendre la réussite plus satisfaisante :effet court sur chaque carré qui passe au vert, et un combo quand tu en enchaînes plusieurs vite, et dautres effet whaou spectaculaire. 
- Le papier tue la haute fréquence dans le métro. Beaucoup d'exercices se font de tête (bascule D, dérivée usuelle). Marque-les « sans papier » et fais-en le contenu des sessions courtes. Garde les longs pour la maison. 
- Le scroll et les niveaux ne se parlent pas. La file « à revoir aujourd'hui » devrait mélanger les cartes de cours ratées et les exercices papier ratés.
- Le chat chevauche le texte sur téléphone : sur la capture, il recouvre le paragraphe des règles.

Recommandation

Ne touche pas au style. Refais la boucle, dans cet ordre :
1. Rétrograder seulement après 2 ratés d'affilée sur le même niveau.
2. Passer au suivant sans rechargement de page
3. Sortir le footer et le paragraphe des règles de la page d'exercice (mettre les règles dans un « ? »).
4. Créer la file « à revoir » à J+1/J+3/J+7.
5. Ajouter une session de 10 exercices avec un écran de bilan, ca ca risque detre compliquer puisque le but cest de grind dans la bonne categorie, actuellement cest les maths et surtout les primitive, et quand jaurai finit tout les niveau je re attaquerai les probas et la logiques /obm, 

Les points 1 à 3 tiennent en une soirée. Les points 4 et 5 sont le vrai levier d'apprentissage avant le B2.

À faire en premier

Modifier apply_result (levels.py:156) : un raté ne fait descendre que s'il suit un autre raté sur le même niveau. C'est environ 20 lignes, plus un test dans tests/test_levels.py. C'est ce qui pèse le plus sur ton envie de rouvrir l'appli.

---
Je n'ai pas testé le mode Scroll : aucun lien /scroll n'apparaissait sur la page testée. Les captures viennent d'une copie locale de la base, avec un compte jetable zz_council. La production n'a pas été touchée.



---
# Conseil n° 2 (2026-11-16), avec le vrai but : grind addictif + apprendre le plus vite

Accord des 5 : pas de session de 10 (le grind est la boucle) ; pas de classement ni de prédiction de note ; « sans papier » à la main = trop cher ; traducteur franglais = pas de première étape tant que le besoin n'est pas défini ; flashcards ratées du scroll dans la file à revoir = petit et utile ; vraie version PC = utile mais après.
Priorité commune : l'anti-blocage (bouton « Trop dur, passer » sans pénalité, qui sert un exercice plus facile de la même notion) et une jauge honnête « % de l'examen couvert » par bloc, qui dit ce qui manque (anglais, méthodo, prog).
Désaccord : sympy. Contrarian et Expansionist : l'auto-notation rend la difficulté adaptative fictive, vérifier au moins les primitives. Outsider, First Principles, Executor : pas avant l'examen.
Déjà dans l'appli (les conseillers ne l'ont pas vu) : niveaux adaptatifs par parcours, chrono rallongé de 50 % après un temps écoulé, formules et liens vers les prérequis affichés après un raté, % par parcours.
