---
id: OBM-6.17
syllabus: OBM
type: définition
papier: maths-s1-obm/10
prereq: OBM-6.15, OBM-6.16
alias: bijection, bijective, application réciproque, f^(-1), un unique antécédent, injective et surjective, f∘f^(-1) = id
---
# Bijection et application réciproque

> **À retenir.** $f:E\to F$ est **bijective** si elle est injective et surjective : $\forall y\in F,\ \exists!\,x\in E,\ y=f(x)$. Sa **réciproque** $f^{-1}:F\to E$ envoie $y$ sur son unique antécédent ; $f^{-1}\circ f=\mathrm{id}_E$ et $f\circ f^{-1}=\mathrm{id}_F$.

## Méthode en copie
1. Vérifier que $f$ va bien de $E$ dans $F$.
2. Soit $y\in F$ : résoudre $f(x)=y$ par équivalences, obtenir **une seule** solution $x$.
3. Vérifier que cette solution est dans $E$.
4. Conclure : « $f$ est bijective et $f^{-1}(y)=\dots$ ».

## Corrigé du TD
$f(x)=\frac{x-1}{x+1}$, $E=\mathbb R\setminus\{-1\}$, $F=\mathbb R\setminus\{1\}$.
*$f$ va de $E$ dans $F$* : $x+1\neq0$ ; si $\frac{x-1}{x+1}=1$ alors $x-1=x+1$, soit $-1=1$, absurde.
*Soit $y\in F$* : $f(x)=y\iff x-1=y(x+1)\iff(1-y)x=y+1\iff x=\frac{y+1}{1-y}$ (car $y\neq1$).
*Dans $E$* : si $\frac{y+1}{1-y}=-1$ alors $y+1=y-1$, absurde.
Donc tout $y\in F$ a un unique antécédent : $f$ est bijective et $f^{-1}(y)=\frac{y+1}{1-y}$.

## Pièges
- Confondre $f^{-1}(y)$ (réciproque, $f$ bijective) et $f^{-1}(B)$ (image réciproque, toujours définie).
- Oublier l'étape « la solution est dans $E$ ».

## Teste-toi
1. $f(x)=2x$, $\mathbb R\to\mathbb R$ : bijective ? réciproque ?

## Réponses
1. Oui, $f^{-1}(x)=\frac x2$.

Source : Cours 6 « Compléments séminaire » (fiches de synthèse, exercices types et corrigés), Moodle S1-MATHS-2031 ; types d'exercices des annales OBM.
