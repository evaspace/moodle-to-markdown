---
id: OBM-6.16
syllabus: OBM
type: définition
papier: maths-s1-obm/10
prereq: OBM-6.12
alias: surjection, surjective, surjectivité, tout y a un antécédent, au moins un antécédent, f(E) = F, montrer qu'une fonction n'est pas surjective
---
# Surjection

> **À retenir.** $f:E\to F$ est **surjective** si $\forall y\in F,\ \exists x\in E,\ y=f(x)$ : tout élément de l'arrivée a **au moins un** antécédent ; autrement dit $f(E)=F$.

## Méthode en copie
- Prouver : « Soit $y\in F$. Posons $x=\dots$ ; alors $x\in E$ et $f(x)=y$. » Le $x$ se trouve en résolvant $f(x)=y$ au brouillon.
- Réfuter : donner un $y\in F$ et montrer que $f(x)=y$ n'a **aucune** solution dans $E$.

## Corrigé du TD
- $f(x)=|x|$, $\mathbb R\to\mathbb R$ : $-1$ n'a pas d'antécédent, $f$ n'est pas surjective.
- $f(x)=|x|$, $\mathbb R\to\mathbb R^+$ : tout $y\geqslant0$ vérifie $f(y)=y$, $f$ est surjective (mais pas injective).
- $f(n)=\frac n2$ ($n$ pair), $0$ ($n$ impair) sur $\mathbb N$ : $f(2n)=n$, donc surjective.
- $f(n)=2n$ sur $\mathbb N$ : $1$ n'a pas d'antécédent ($2n=1$ impossible dans $\mathbb N$), pas surjective.

## Pièges
- La surjectivité dépend de l'**arrivée** : même formule, conclusions opposées ci-dessus.
- Oublier de vérifier que l'antécédent proposé est bien dans $E$.

## Teste-toi
1. $f(x)=2x$, $\mathbb R\to\mathbb R$ surjective ?

## Réponses
1. Oui : pour $y\in\mathbb R$, $x=\frac y2\in\mathbb R$ et $f(x)=y$.

Source : Cours 6 « Compléments séminaire » (fiches de synthèse, exercices types et corrigés), Moodle S1-MATHS-2031 ; types d'exercices des annales OBM.
