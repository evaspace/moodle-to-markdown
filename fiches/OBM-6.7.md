---
id: OBM-6.7
syllabus: OBM
type: méthode
papier: maths-s1-obm/6
prereq: OBM-6.3
alias: raisonnement par l'absurde, absurde, contradiction, supposer le contraire, √2 irrationnel, contre-exemple, disjonction de cas, analyse-synthèse
---
# Absurde, contre-exemple, disjonction de cas, analyse-synthèse

> **À retenir.**
> - **Absurde** : supposer $\neg P$, aboutir à une contradiction, conclure $P$.
> - **Contre-exemple** : un seul $x$ avec $\neg P(x)$ suffit à prouver que « $\forall x,\ P(x)$ » est faux.
> - **Disjonction de cas** : les cas doivent couvrir **toutes** les possibilités ($n$ pair / impair, $x\geqslant0$ / $x < 0$).
> - **Analyse-synthèse** (existence et forme d'un objet) : analyse = on suppose qu'il existe et on trouve sa seule forme possible ; synthèse = on vérifie que cette forme convient.

## Méthode en copie
- Toujours annoncer le raisonnement en première ligne : « Par l'absurde, supposons… », « Distinguons deux cas », « Analyse : supposons qu'il existe… ».
- Contre-exemple : donner la valeur **et** le calcul qui montre que la propriété échoue.

## Corrigé du TD
Écrire $\exp$ comme somme d'une fonction paire $f$ et d'une fonction impaire $g$.
*Analyse.* Supposons $\forall x\in\mathbb R,\ e^x=f(x)+g(x)$. Alors $e^{-x}=f(-x)+g(-x)=f(x)-g(x)$. Par somme et différence : $f(x)=\frac{e^x+e^{-x}}2$ et $g(x)=\frac{e^x-e^{-x}}2$.
*Synthèse.* Ces $f$ et $g$ conviennent : $f(-x)=f(x)$, $g(-x)=-g(x)$ et $f(x)+g(x)=e^x$.
D'où l'existence (et l'unicité) de $f$ et $g$.

## Pièges
- Analyse sans synthèse : on a seulement prouvé « si ça existe, c'est ça ».
- Un exemple ne prouve pas un « pour tout ».
- Cas qui ne couvrent pas tout (oublier $x=0$).

## Teste-toi
1. Réfuter « $\forall n\in\mathbb N,\ n^2+n+41$ est premier ».
2. Quel raisonnement pour « $\sqrt2\notin\mathbb Q$ » ?

## Réponses
1. $n=40$ : $40^2+40+41=41^2$. 2. Par l'absurde : $\sqrt2=\frac pq$ irréductible donne $p$ et $q$ pairs.

Source : Cours 6 « Compléments séminaire » (fiches de synthèse, exercices types et corrigés), Moodle S1-MATHS-2031 ; types d'exercices des annales OBM.
