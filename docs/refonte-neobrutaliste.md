# Refonte néo-brutaliste de l'accueil : assets à générer

Demande de l'utilisateur (2026-11-26) : générer d'abord tous les visuels avec un générateur d'images gratuit, sans rien intégrer au site. L'intégration (section « Plus tard ») vient après. Le chat n'est pas à générer : on garde les fichiers existants (`static/*cat*`).

## Règles de génération

- Outil gratuit uniquement, jamais de crédits payants :
  - badges avec texte (2, 3, 9) : Ideogram (offre gratuite), c'est le meilleur pour écrire un texte lisible dans l'image ;
  - le reste : Microsoft Designer / Bing Image Creator (gratuit) ou Gemini (gratuit).
- `--ar 16:9` est une option Midjourney (payant) : ailleurs, demander 1920x1080 (fond) ou un carré 1024x1024 (stickers).
- Générer chaque sticker seul, sur fond blanc pur `#FFFFFF`.
- Détourage gratuit en local : `pipx install "rembg[cli]"` puis `rembg i entree.png sortie.png`. Sinon, garder le fond blanc et utiliser `mix-blend-mode: multiply` en CSS.
- Vérifier chaque image : texte exact (accents compris, « C'EST PARTI ! »), aucun filigrane, aucune lettre parasite.
- Déposer les fichiers finaux dans `static/neo/` avec les noms ci-dessous.

## Liste

- [ ] **Fond** — `static/neo/fond.svg` (1920x1080)
  ```
  Minimalist neo-brutalist web background on a pure solid white (#FFFFFF) canvas. Faint light gray (#E6E6E6) geometric accents placed sparsely near the edges: two small wireframe grids (top-right and bottom-left), two subtle pixel checkerboard clusters, a few tiny four-point stars on top-left, and a thin light-gray spiral on bottom-right. Vast empty pure white center, flat 2D vector, zero text, no letters, clean UI backdrop --ar 16:9
  ```
- [ ] **1. Badge « NON-STOP »** (haut-gauche du bouton noir) — `static/neo/badge-non-stop.svg`
  ```
  Neo-brutalist vector sticker of a slightly tilted blue pill badge with bold white uppercase text "NON-STOP" outlined in black. Thick 3px solid black border, hard offset black shadow, flat 2D retro web style, isolated on pure white #FFFFFF background.
  ```
- [ ] **2. Badge « NEW! »** (haut-droite du bouton noir) — `static/neo/badge-new.svg`
  ```
  Neo-brutalist vector sticker of a spiky red-orange comic starburst badge with bold yellow text "NEW!" outlined in black. Thick black outlines, hard offset black shadow, flat 2D retro UI style, isolated on pure white #FFFFFF background.
  ```
- [ ] **3. Bulle « C'EST PARTI ! »** (à droite du chat) — `static/neo/bulle-cest-parti.svg`
  ```
  Neo-brutalist comic speech bubble sticker, white rectangle with a bottom-left pointer tail and bold black uppercase text "C'EST PARTI !". Thick 3px black border, hard solid black offset shadow, flat 2D vector, isolated on pure white #FFFFFF background.
  ```
- [ ] **4. Étoiles et fleur** (autour du chat) — `static/neo/etoiles-fleur.svg`
  ```
  Small cluster of neo-brutalist comic doodle stickers: three yellow four-point sparkles and one small red pixel-art flower. Thick black outlines, flat 2D vector, isolated on pure white #FFFFFF background.
  ```
- [ ] **5. Curseur et explosion** (bas-gauche des boutons) — `static/neo/curseur-explosion.svg`
  ```
  Neo-brutalist vector sticker of a classic blue retro pixel mouse pointer clicking a jagged yellow and orange comic burst with a red four-point star. Thick black outlines, hard black shadow, isolated on pure white #FFFFFF background.
  ```
- [ ] **6. Feuilles d'examens** (sur le bouton rouge) — `static/neo/feuilles-examens.svg`
  ```
  Neo-brutalist vector sticker of three overlapping white exam paper sheets with red grade marks, checkmarks, and lines. Thick black outlines, crisp flat 2D comic illustration, isolated on pure white #FFFFFF background.
  ```
- [ ] **7. Livre ouvert et carnet** (sur le bouton bleu) — `static/neo/livre-carnet.svg`
  ```
  Neo-brutalist vector sticker of an open white textbook next to a small closed green notebook with tiny blue sparkles. Thick black outlines, flat 2D retro UI illustration, isolated on pure white #FFFFFF background.
  ```
- [ ] **8. Trophée** (sur le bouton jaune) — `static/neo/trophee.svg`
  ```
  Neo-brutalist vector sticker of a golden trophy cup with a small star embossed in the center. Thick black outlines, flat 2D retro game icon style, isolated on pure white #FFFFFF background.
  ```
- [ ] **9. Badge ovale « 100% C »** (droite des boutons) — `static/neo/badge-100-c.svg`
  ```
  Neo-brutalist vector sticker of a tilted orange-yellow gradient oval badge with bold white text "100% C" outlined in black. Thick 3px black border, hard offset black shadow, isolated on pure white #FFFFFF background.
  ```
- [ ] **10. Cocarde smiley** (bas-droite du bloc stats) — `static/neo/cocarde-smiley.svg`
  ```
  Neo-brutalist vector sticker of a blue scalloped seal rosette badge with a happy yellow smiley face in the center. Thick black outlines, hard offset black shadow, flat 2D retro aesthetic, isolated on pure white #FFFFFF background.
  ```

Pas à générer : le chat (déjà là) et les barres de stats (déjà codées, dynamiques).

## Plus tard : intégration (ne pas faire tant que les 11 assets ne sont pas validés)

À trancher avant : ce style (pastilles, majuscules, ombres portées, dégradé du badge 9, 5 couleurs vives) contredit les règles anti-slop globales. C'est un choix explicite de l'utilisateur pour cette page ; confirmer qu'il s'applique.

### Mise en page

1. Fond : garder le blanc pur (`background-color: #FFFFFF`), superposer `fond.png` (`background-size: cover; background-position: center; pointer-events: none;`). Pas de texte « PIERREFEU » en arrière-plan.
2. Mascotte : garder le chat actuel au-dessus du bouton principal.
3. Boutons et navigation : `border: 3px solid #000; box-shadow: 4px 4px 0px #000; border-radius: 6px; font-weight: 800; text-transform: uppercase;`.
   - Bouton 1, noir `#0D0D0D`, texte blanc : « SCROLLER LES COURS (EN DEV) ↓ »
   - Bouton 2, rouge `#F04438`, texte blanc : « NIVEAUX SUR PAPIER → »
   - Bouton 3, bleu `#155EEF`, texte blanc : « LIRE LE COURS COMPLET → »
   - Ligne 4, grille 2 colonnes : gauche jaune `#FACC15` « CLASSEMENT → » ; droite blanc `#FFFFFF` « MES STATS • 17/631 NIVEAUX → » avec les barres de progression existantes.
   - Footer : pastilles blanches (orange `#F97316` pour « CRÉDITS & REMERCIEMENTS »), `border: 2px solid #000; box-shadow: 3px 3px 0px #000;`.
4. Stickers : les 10 PNG/SVG en `position: absolute` par-dessus les bordures des boutons (`z-index` supérieur), masqués ou réduits sous `768px`.

### Animations

- Boutons principaux et pastilles du footer : `:hover` → `transform: translate(-2px, -2px)` et `box-shadow: 6px 6px 0 #000` ; `:active` → `transform: translate(4px, 4px)` et `box-shadow: 0 0 0 #000` (touche enfoncée).
- Chat + bulle + étoiles/fleur : au survol du chat ou du bouton noir, saut du chat (`translateY(-5px)`), apparition pop de la bulle (`scale(0.85 → 1.05 → 1)`), rotation `15deg` des étoiles/fleur.
- « NON-STOP » : oscillation lente en boucle (`rotate(-6deg)` à `rotate(-2deg)`, 3s infinite alternate) ; `:hover` → `scale(1.1) rotate(0deg)`.
- « NEW! » : pulsation continue (`scale(1)` à `1.06`, 1.8s) ; au survol du bouton noir, secousse rapide (`wiggle` ±8deg).
- Curseur et explosion : au survol des boutons rouge ou bleu, le curseur clique (`scale(0.85)`) et l'explosion grossit (`scale(1.15)`).
- Feuilles d'examens : au survol de « NIVEAUX SUR PAPIER », `translateY(-4px) rotate(6deg)`.
- Livre et carnet : au survol de « LIRE LE COURS COMPLET », `translateY(-5px) rotate(-4deg)`.
- Trophée : au survol de « CLASSEMENT », `scale(1.15) rotate(8deg)`.
- « 100% C » : `:hover` → `rotate(14deg) scale(1.1)`.
- Cocarde smiley : au survol de « MES STATS », balancier ±12deg ou rotation lente continue.
- Étoiles « Notez ce site » : jaune `#FACC15` progressif au survol, `scale(1.2)` sur l'étoile visée.
- Respecter `prefers-reduced-motion: reduce` (couper les boucles).
