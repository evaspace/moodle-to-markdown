---
title: Se faire expliquer une correction par une IA sans perdre les formules
date: 2026-11-16
description: Le bouton « Copier pour une IA » copie l'énoncé, la correction et les formules en LaTeX, avec une question prête à coller.
---

Quand une correction ne te parle pas, le plus rapide est de te la faire expliquer autrement. Le problème : copier un exercice de maths depuis une page web casse les formules, et l'IA reçoit du texte illisible.

## Ce que fait le bouton

Chaque correction d'exercice sur papier, et chaque carte du fil, a un bouton « Copier pour une IA ». Il place dans ton presse-papiers :

- l'énoncé et la correction ;
- les formules en LaTeX, telles qu'elles sont écrites dans le site, donc sans symbole cassé ;
- le lien vers l'exercice ;
- une question prête, que tu peux modifier.

Tu colles le tout dans ChatGPT, Claude ou Gemini.

## Bien l'utiliser

Pour apprendre plutôt que recopier : cherche d'abord sur papier, regarde la correction, et ne copie que si une étape te bloque. Demande alors d'expliquer cette étape, pas de refaire l'exercice. Puis refais l'exercice toi-même, avec la variante qui change les chiffres.

## Une bibliothèque libre

Le bouton est une petite bibliothèque JavaScript publique, `copy-for-llm`, que tu peux utiliser dans tes propres pages : <https://github.com/evaspace/copy-for-llm>.
