---
title: Pourquoi les corrigés du site sont vérifiés par ordinateur
date: 2026-11-16
description: Calcul formel pour les maths, vrai toplevel pour le Caml, compilation pour le C : comment une réponse fausse est empêchée d'arriver jusqu'à toi.
---

Un corrigé faux est pire que pas de corrigé : tu apprends une erreur et tu la refais à l'examen. Les réponses du site sont donc vérifiées par des programmes, avant d'être publiées.

## En maths : le calcul formel

Les réponses calculées sont contrôlées avec la bibliothèque `sympy`. Prends une primitive : le site stocke l'énoncé $f(x) = x e^x$ et la réponse $F(x) = (x-1)e^x$. À la construction, il dérive la réponse et compare :

$$F'(x) = e^x + (x-1)e^x = x e^x = f(x)$$

Si l'égalité est fausse, le site refuse de se construire. Il en va de même pour les intégrales (comparées numériquement avec 30 chiffres), les dérivées, les équations différentielles ou les valeurs de probabilités.

## En Caml : un vrai toplevel

Pour les exercices du type « que répond Caml ? », une phrase mal recopiée est vite arrivée. Chaque phrase Caml du parcours est rejouée dans un vrai OCaml, et la réponse affichée doit être exactement celle du toplevel.

## En C : on compile et on exécute

Pour le début du C, chaque programme est compilé avec `gcc` puis exécuté. La sortie annoncée dans l'énoncé doit être celle que le programme affiche vraiment.

## Ce que ça ne garantit pas

Ces vérifications portent sur le résultat, pas sur la pédagogie. Un énoncé peut être mal posé, ou une transcription d'annale contenir une faute de lecture. Les corrigés rédigés par l'auteur, quand la correction officielle n'existe pas, sont signalés comme tels.
