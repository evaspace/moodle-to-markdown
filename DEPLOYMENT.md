# Déploiement Maths Doomscrolling

## Ce qui alimente le site

L'application web lit les cartes depuis `cards.db` et propose aussi un lecteur des
fichiers Markdown de `EPITA_Moodle_Notes_MD/` à l'adresse `/cours/`. Les contenus
Moodle et la base SQLite sont exclus de Git. Un `git push` seul publie donc le code,
pas les cartes ni les cours complets.

La base locale vérifiée dans ce dépôt contient 3 486 cartes actives. Les 294 fichiers
de `Generated_QCMs/` représentent déjà ces cartes ; l'importeur ignore les doublons.
Les QCM Moodle avec plusieurs bonnes réponses sont maintenant jouables en sélection
multiple. Les cartes générées par l'IA restent limitées à quatre choix et une réponse
juste.

## Préparer un nouveau serveur

1. Installer Docker avec Docker Compose, créer le dossier d'application et configurer
   l'alias SSH utilisé comme `REMOTE_HOST`.
2. Dans le dossier distant, créer un `.env` contenant au minimum :

   ```dotenv
   ADMIN_PASSWORD=un-mot-de-passe-long-et-aleatoire
   APP_BIND_IP=127.0.0.1
   ```

   `APP_BIND_IP` doit être l'adresse que le reverse proxy du serveur peut joindre.
   L'application écoute sur le port hôte `5080` et expose `/healthz` pour le contrôle
   de santé. Aucune clé Mistral n'est nécessaire pour faire tourner le site.

3. Depuis ce dépôt, envoyer le code et construire l'application :

   ```bash
   make sync-app REMOTE_HOST=nouveau-serveur REMOTE_APP_DIR=/opt/mathsdoomscrolling
   ```

4. Envoyer `cards.db` avec sauvegarde SQLite cohérente et vérification de santé :

   ```bash
   make deploy-db REMOTE_HOST=nouveau-serveur REMOTE_APP_DIR=/opt/mathsdoomscrolling
   ```

   La commande demande confirmation avant de remplacer la base distante. Elle conserve
   une sauvegarde distante et restaure celle-ci si le health check échoue.

5. Pointer le reverse proxy du domaine vers `127.0.0.1:5080` (ou vers `APP_BIND_IP`)
   et vérifier `/healthz`, puis la page d'accueil et le chargement de quelques cartes.

## Commandes de contenu

- `make sync-server` envoie et ingère les fichiers texte de QCM. Les doublons sont
  ignorés ; pour un nouveau serveur, le transfert de `cards.db` ci-dessus fournit déjà
  la base complète et évite une ingestion redondante.
- `make sync-md` copie les fichiers Markdown Moodle, consultables sur le site depuis
  le lien « Lire les cours complets ». Le lecteur rend le Markdown et les formules,
  et limite les chemins aux fichiers `.md` du dossier exporté.
- `make sync-all` déploie le code, les cours Markdown et la base complète (cartes QCM
  comprises). Il ne retransfère pas les `.txt` déjà présents dans la base.
