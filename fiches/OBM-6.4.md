---
id: OBM-6.4
syllabus: OBM
type: définition
papier: maths-s1-obm/4
prereq: OBM-6.1
alias: quantificateurs, pour tout, il existe, ∀, ∃, ∃!, traduire avec quantificateurs, ordre des quantificateurs, vérité d'une proposition quantifiée, aucun
---
# Quantificateurs

> **À retenir.** $\forall x\in E,\ P(x)$ : tout élément de $E$ vérifie $P$. $\exists x\in E,\ P(x)$ : au moins un. $\exists!\,x\in E,\ P(x)$ : exactement un. Deux quantificateurs **différents** ne commutent pas : $\forall x\ \exists y$ ($y$ peut dépendre de $x$) n'est pas $\exists y\ \forall x$ ($y$ unique pour tous).

## Méthode en copie
1. Chaque variable reçoit son quantificateur **et** son ensemble ($\forall n\in\mathbb N$).
2. Les quantificateurs s'écrivent **avant** la propriété, dans l'ordre où les objets sont choisis.
3. « Aucun $x$ ne vérifie $P$ » s'écrit $\forall x,\ \neg P(x)$.

## Corrigé du TD
- « Tout entier naturel est pair ou impair » : $\forall n\in\mathbb N,\ \exists p\in\mathbb N,\ n=2p$ ou $n=2p+1$.
- « Pour tout réel $x$, il existe un entier naturel supérieur à $x$ » : $\forall x\in\mathbb R,\ \exists n\in\mathbb N,\ n\geqslant x$.
- « Il existe au moins un réel qui n'est pas rationnel » : $\exists x\in\mathbb R,\ x\notin\mathbb Q$.
- « Un produit de deux réels est nul si et seulement si l'un des deux est nul » : $\forall(a,b)\in\mathbb R^2,\ (ab=0\iff a=0$ ou $b=0)$.
- « Tout réel est le cube d'un réel » : $\forall x\in\mathbb R,\ \exists y\in\mathbb R,\ x=y^3$.
- « Le carré de tout réel est positif » : $\forall x\in\mathbb R,\ x^2\geqslant0$.

## Pièges
- $\exists y\in\mathbb R,\ \forall x\in\mathbb R,\ x=y^3$ dit qu'un seul $y$ sert pour tous les $x$ : faux.
- Variable sans ensemble ($\exists N$) : point perdu.
- Mettre le quantificateur à la fin (« $x^2\geqslant0,\ \forall x$ ») : à éviter en copie.

## Teste-toi
1. Écrire « $f$ s'annule au moins une fois sur $\mathbb R$ ».
2. Vrai ou faux : $\exists x\in\mathbb R,\ \forall y\in\mathbb R,\ y\leqslant x$ ?

## Réponses
1. $\exists x\in\mathbb R,\ f(x)=0$. 2. Faux : $\mathbb R$ n'a pas de plus grand élément ($y=x+1$).

Source : Cours 6 « Compléments séminaire » (fiches de synthèse, exercices types et corrigés), Moodle S1-MATHS-2031 ; types d'exercices des annales OBM.
