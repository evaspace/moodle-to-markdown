---
id: OBM-6.15
syllabus: OBM
type: définition
papier: maths-s1-obm/10
prereq: OBM-6.12
alias: injection, injective, injectivité, f(x) = f(y) ⇒ x = y, au plus un antécédent, montrer qu'une fonction n'est pas injective, contre-exemple f(1) = f(2), x²
---
# Injection

> **À retenir.** $f:E\to F$ est **injective** si $\forall(x,x')\in E^2,\ f(x)=f(x')\Rightarrow x=x'$ : tout $y\in F$ a **au plus un** antécédent. Non injective : $\exists x\neq x'$, $f(x)=f(x')$.

## Méthode en copie
- Prouver : « Soient $x,x'\in E$ tels que $f(x)=f(x')$. » … « Donc $x=x'$. $f$ est injective. » (ou : $f$ strictement monotone sur un intervalle).
- Réfuter : donner deux valeurs **distinctes** et le calcul de leurs images égales.

## Corrigé du TD
- $f(x)=|x|$ sur $\mathbb R$ : $f(1)=f(-1)=1$ avec $1\neq-1$, donc $f$ n'est pas injective.
- $f(n)=2n$ sur $\mathbb N$ : si $2n=2m$ alors $n=m$, donc $f$ est injective.

## Pièges
- Écrire « $x=x'\Rightarrow f(x)=f(x')$ » : c'est vrai pour toute application, ça ne prouve rien.
- L'injectivité dépend du **départ** : $x\mapsto x^2$ est injective sur $\mathbb R^+$, pas sur $\mathbb R$.

## Teste-toi
1. $f(x)=x^3$ sur $\mathbb R$ est-elle injective ?

## Réponses
1. Oui : strictement croissante (ou $x^3=y^3\Rightarrow x=y$ par stricte croissance de la racine cubique).

Source : Cours 6 « Compléments séminaire » (fiches de synthèse, exercices types et corrigés), Moodle S1-MATHS-2031 ; types d'exercices des annales OBM.
