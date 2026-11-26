---
id: OBM-6.5
syllabus: OBM
type: méthode
papier: maths-s1-obm/5
prereq: OBM-6.3, OBM-6.4
alias: nier une phrase quantifiée, négation d'une proposition quantifiée, non pour tout, non il existe, nier une phrase, négation de la convergence
---
# Nier une phrase quantifiée

> **À retenir.** $\neg(\forall x\in E,\ P(x))\equiv\exists x\in E,\ \neg P(x)$ et $\neg(\exists x\in E,\ P(x))\equiv\forall x\in E,\ \neg P(x)$. On échange chaque $\forall$ et $\exists$, **on garde l'ordre et les ensembles**, et on nie la propriété finale.

## Méthode en copie
1. Recopier les quantificateurs dans le même ordre en échangeant $\forall$ et $\exists$.
2. Garder les ensembles ($\forall\varepsilon > 0$ devient $\exists\varepsilon > 0$, jamais $\varepsilon\leqslant0$).
3. Nier la propriété finale avec De Morgan ([fiche OBM-6.3](/cours/fiches/OBM-6.3)).

## Corrigé du TD
$f:\mathbb R\to\mathbb R$.
- $\neg(\forall x\in\mathbb R,\ f(x)\neq0)$ : $\exists x\in\mathbb R,\ f(x)=0$.
- $\neg\big(\forall x\in\mathbb R,\ \forall y\in\mathbb R,\ (f(x)=f(y)\Rightarrow x=y)\big)$ : $\exists x\in\mathbb R,\ \exists y\in\mathbb R,\ f(x)=f(y)$ et $x\neq y$ ($f$ n'est pas injective).

## Pièges
- Nier l'ensemble : $\neg(\forall\varepsilon > 0\ldots)$ n'est pas « $\forall\varepsilon\leqslant0$ ».
- Garder l'implication dans la négation : $\neg(A\Rightarrow B)$ est « $A$ et $\neg B$ ».
- Changer l'ordre des quantificateurs.

## Teste-toi
1. Nier « $(u_n)$ est majorée » : $\exists M\in\mathbb R,\ \forall n\in\mathbb N,\ u_n\leqslant M$.
2. Nier « $u_n\to\ell$ » : $\forall\varepsilon > 0,\ \exists N\in\mathbb N,\ \forall n\geqslant N,\ |u_n-\ell|\leqslant\varepsilon$.

## Réponses
1. $\forall M\in\mathbb R,\ \exists n\in\mathbb N,\ u_n > M$.
2. $\exists\varepsilon > 0,\ \forall N\in\mathbb N,\ \exists n\geqslant N,\ |u_n-\ell| > \varepsilon$.

Source : Cours 6 « Compléments séminaire » (fiches de synthèse, exercices types et corrigés), Moodle S1-MATHS-2031 ; types d'exercices des annales OBM.
