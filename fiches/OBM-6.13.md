---
id: OBM-6.13
syllabus: OBM
type: définition
papier: maths-s1-obm/9
prereq: OBM-6.12
alias: image directe, f(A), ensemble image, lecture graphique, f(R), valeurs prises, image d'un intervalle
---
# Image directe

> **À retenir.** Pour $A\subset E$ : $f(A)=\{f(x),\ x\in A\}\subset F$, l'ensemble des images des éléments de $A$. $y\in f(A)\iff\exists x\in A,\ y=f(x)$. Toujours : $f(A\cup B)=f(A)\cup f(B)$ et $f(A\cap B)\subset f(A)\cap f(B)$ (inclusion seulement).

## Méthode en copie
- Ensemble fini : calculer chaque image et lister **sans doublon**.
- Intervalle : étudier les variations de $f$ sur l'intervalle (tableau), lire l'ensemble des valeurs prises.

## Corrigé du TD
$f(x)=|x|$ : $f([-2,3])=[0,3]$ ; $f(\{-2,3\})=\{2,3\}$ ; $f(\mathbb R)=\mathbb R^+$.
$f(n)=\frac n2$ si $n$ pair, $0$ si $n$ impair : $f(0)=0$, $f(1)=0$, $f(2)=1$, $f(3)=0$, donc $f(\{0,1,2,3\})=\{0,1\}$.
Contre-exemple pour l'intersection : $f=0$, $A=[1,2]$, $B=[3,4]$ : $f(A)\cap f(B)=\{0\}$ mais $f(A\cap B)=f(\emptyset)=\emptyset$.

## Pièges
- $f([a,b])=[f(a),f(b)]$ seulement si $f$ est continue et croissante : $f([-2,3])$ n'est pas $[2,3]$.
- Écrire $f(\{-2,3\})=\{2,3\}$ avec des crochets : c'est un ensemble fini, pas un intervalle.

## Teste-toi
1. $f(x)=x^2$ : $f([-1,2])$ ?

## Réponses
1. $[0,4]$ (minimum $0$ en $x=0$, maximum $4$ en $x=2$).

Source : Cours 6 « Compléments séminaire » (fiches de synthèse, exercices types et corrigés), Moodle S1-MATHS-2031 ; types d'exercices des annales OBM.
