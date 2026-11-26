---
id: OBM-6.14
syllabus: OBM
type: définition
papier: maths-s1-obm/9
prereq: OBM-6.12
alias: image réciproque, f^(-1)(B), antécédents, image réciproque d'un singleton, préimage, ensemble des antécédents, peut être vide
---
# Image réciproque

> **À retenir.** Pour $B\subset F$ : $f^{-1}(B)=\{x\in E,\ f(x)\in B\}$, l'ensemble des antécédents des éléments de $B$. $x\in f^{-1}(B)\iff f(x)\in B$. Elle existe **toujours**, même si $f$ n'est pas bijective, et peut être vide. $f^{-1}(X\cup Y)=f^{-1}(X)\cup f^{-1}(Y)$ et $f^{-1}(X\cap Y)=f^{-1}(X)\cap f^{-1}(Y)$.

## Méthode en copie
- Résoudre $f(x)\in B$ en $x$ : « $x\in f^{-1}(B)\iff f(x)\in B\iff\dots$ », chaque $\iff$ justifié.
- Pour un ensemble fini $B$ : chercher les antécédents de chaque élément, puis réunir.

## Corrigé du TD
$f(x)=|x|$ : les $y < 0$ n'ont pas d'antécédent, $y > 0$ en a deux ($y$ et $-y$). Donc $f^{-1}([-2,3])=[-3,3]$, $f^{-1}(\{-2,3\})=\{-3,3\}$, $f^{-1}(\mathbb R)=\mathbb R$.
$f(n)=\frac n2$ ($n$ pair), $0$ ($n$ impair), $X=\{0,1,2,3\}$ : $1$ a pour antécédent $2$, $2$ a $4$, $3$ a $6$, et $0$ a $0$ et tous les impairs. $f^{-1}(X)=\{0,2,4,6\}\cup\{n\in\mathbb N,\ n\text{ impair}\}$.

## Pièges
- Croire que $f^{-1}(B)$ demande $f$ bijective : non, c'est une notation d'ensemble.
- Oublier les éléments de $B$ sans antécédent (ils ne contribuent rien) ou les antécédents multiples.

## Teste-toi
1. $f(x)=x^2$ : $f^{-1}(\{4\})$, $f^{-1}([-1,0[)$ ?

## Réponses
1. $\{-2,2\}$ et $\emptyset$.

Source : Cours 6 « Compléments séminaire » (fiches de synthèse, exercices types et corrigés), Moodle S1-MATHS-2031 ; types d'exercices des annales OBM.
