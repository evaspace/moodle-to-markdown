---
id: OBM-6.12
syllabus: OBM
type: définition
papier: maths-s1-obm/9
prereq: OBM-6.9
alias: application, fonction, ensemble de départ, ensemble d'arrivée, image, antécédent, composée, g∘f, restriction, identité, graphe
---
# Applications, image, antécédent, composée

> **À retenir.** Une application $f:E\to F$ associe à **chaque** $x\in E$ **un unique** $f(x)\in F$ (image de $x$). Si $f(x)=y$, $x$ est **un** antécédent de $y$. Composée : $g\circ f:E\to G$, $(g\circ f)(x)=g(f(x))$ (on applique $f$ d'abord). $\mathrm{id}_E(x)=x$.

## Méthode en copie
- Donner une application = donner départ, arrivée **et** formule.
- Calculer $g\circ f$ : « Pour $x\in E$, $(g\circ f)(x)=g(f(x))=\dots$ », puis conclure par une égalité de fonctions.
- Montrer que $f$ est bien une application $E\to F$ : vérifier que $f(x)$ est défini **et** dans $F$ pour tout $x\in E$.

## Corrigé du TD
$f(x)=|x|$, $g(x)=-x$ sur $\mathbb R$.
$f\circ f(x)=||x||=|x|$ donc $f\circ f=f$ ; $g\circ g(x)=-(-x)=x$ donc $g\circ g=\mathrm{id}_{\mathbb R}$ ; $f\circ g(x)=|-x|=|x|$ donc $f\circ g=f$ ; $g\circ f(x)=-|x|$.

## Pièges
- $g\circ f\neq f\circ g$ en général (ici $f\circ g=f$ mais $g\circ f=-f$).
- Lire $g\circ f$ de gauche à droite : on commence par $f$.

## Teste-toi
1. $f(x)=x+1$, $g(x)=x^2$ : $g\circ f$ et $f\circ g$ ?

## Réponses
1. $(g\circ f)(x)=(x+1)^2$ et $(f\circ g)(x)=x^2+1$.

Source : Cours 6 « Compléments séminaire » (fiches de synthèse, exercices types et corrigés), Moodle S1-MATHS-2031 ; types d'exercices des annales OBM.
