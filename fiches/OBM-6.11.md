---
id: OBM-6.11
syllabus: OBM
type: théorème
papier: maths-s1-dp/1
prereq: OBM-6.10, DP-1.1
alias: ensembles finis, cardinal d'un produit cartésien, card(A × B), cardinal de P(E), 2^n, cardinal du complémentaire
---
# Ensembles finis : cardinaux usuels

> **À retenir.** $\mathrm{Card}(A\cup B)=\mathrm{Card}A+\mathrm{Card}B-\mathrm{Card}(A\cap B)$ ; $\mathrm{Card}(A\times B)=\mathrm{Card}A\times\mathrm{Card}B$ ; $\mathrm{Card}\,\overline A=\mathrm{Card}E-\mathrm{Card}A$ ; $\mathrm{Card}\,\mathcal P(E)=2^n$ ; nombre d'applications de $E$ ($n$ éléments) dans $F$ ($p$ éléments) : $p^n$ ; $\binom nk=\frac{n!}{k!(n-k)!}$ parties à $k$ éléments.

## Méthode en copie
- Dire **ce qu'on choisit** et dans quel ordre : « choisir une application, c'est choisir $f(a)$, $f(b)$, $f(c)$ dans $F$ : $2^3$ choix ».
- Pour « au moins » / « non surjectif » : compter le complémentaire.

## Corrigé du TD
$\mathrm{Card}A=\mathrm{Card}B=10$. $0\leqslant\mathrm{Card}(A\cap B)\leqslant10$ (vide si disjoints, 10 si $A=B$). Par la formule de l'union, $10\leqslant\mathrm{Card}(A\cup B)\leqslant20$. $\mathrm{Card}(A\times B)=10\times10=100$.
Surjections d'un ensemble à $n$ éléments sur $F=\{a,b,c\}$ : $3^n$ applications ; non surjectives : 3 constantes, et pour chaque paire, $2^n-2$ surjections sur cette paire, soit $3+3(2^n-2)$. Donc $3^n-3\cdot2^n+3$ surjections.

## Pièges
- Oublier de retirer l'intersection dans le cardinal d'une union.
- Compter $2^n$ applications de $E$ dans $F$ au lieu de $p^n$ : la base est le cardinal de l'**arrivée**.

## Teste-toi
1. Nombre d'applications de $\{a,b,c\}$ dans $\{u,v\}$ ?
2. Développer $(a+b)^4$.

## Réponses
1. $2^3=8$. 2. $a^4+4a^3b+6a^2b^2+4ab^3+b^4$.

Source : Cours 6 « Compléments séminaire » (fiches de synthèse, exercices types et corrigés), Moodle S1-MATHS-2031 ; types d'exercices des annales OBM.
