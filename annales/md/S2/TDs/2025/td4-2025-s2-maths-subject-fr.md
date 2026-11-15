# Contrôle TD 2 (S2) — lundi 10 mai 2021 (sujet, FR)

- Source : `raw/S2/TDs/2025/td4-2025-s2-maths-subject-fr.pdf` (2 pages)
- Date réelle : 10 mai 2021 (dossier promo 2025 ; le fichier s'appelle td4 mais le document est le « Contrôle TD 2 » du S2). Pas de corrigé dans les annales.

## Question de cours
Type : noyau, image, injectivité, surjectivité (cours) · ECUE : ALM · Niveau : maths-s2-alm/2
Formules : sous-espace : contient 0 et stable par $\alpha u + v$ ; $f(\alpha u + v) = \alpha f(u) + f(v)$ ; injective $\iff \mathrm{Ker} f = \{0\}$ ; surjective $\iff \mathrm{Im} f = F$

Soient $E$ et $F$ deux $\mathbb{R}$-ev, et $\varphi \in \mathcal{L}(E,F)$ une application linéaire de $E$ dans $F$.
1. Donner la définition mathématique précise de $\mathrm{Ker}\,\varphi$ et $\mathrm{Im}\,\varphi$.
2. À quelles conditions sur $\mathrm{Ker}\,\varphi$ et $\mathrm{Im}\,\varphi$, $\varphi$ est-elle injective ? $\varphi$ est-elle surjective ?
3. Dans cette question $E$ et $F$ sont de dimensions finies : $\dim E = 5$ et $\dim F = 3$. Parmi les deux affirmations suivantes l'une est impossible. Déterminer laquelle et démontrer votre réponse à l'aide du théorème du rang dont vous rappellerez l'énoncé. (a) $\varphi$ est injective. (b) $\varphi$ est surjective.

## Exercice 1
Type : projecteur, noyau et image · ECUE : ALM · Niveau : maths-s2-alm/10
Formules : projecteur $\iff f \circ f = f$ ; $E = \mathrm{Ker} f \oplus \mathrm{Im} f$ ; $f = id$ sur $\mathrm{Im} f$, $0$ sur $\mathrm{Ker} f$ ; matrice dans une base adaptée $\mathrm{diag}(0, \dots, 0, 1, \dots, 1)$

Soit $g$ l'application linéaire définie par $g : \mathbb{R}^3 \to \mathbb{R}^3$, $(x,y,z) \mapsto (2x + y - z,\ z - 2x - y,\ z - 2x - y)$.
1. Déterminer le noyau de $g$ et sa dimension en justifiant soigneusement votre réponse.
2. $g$ est-elle une projection ?

## Exercice 2
Type : application linéaire (caractérisation) · ECUE : ALM · Niveau : maths-s2-alm/1
Formules : $f$ linéaire $\Rightarrow f(0) = 0$ et $f(2x) = 2f(x)$ (conditions nécessaires) ; réciproquement vérifier $f(\lambda x + y) = \lambda f(x) + f(y)$ ; les applications linéaires de $\mathbb{R}$ dans $\mathbb{R}$ sont $x \mapsto bx$

Soit $f : \mathbb{R}_2[X] \to \mathbb{R}_2[X]$, $P \mapsto 2X^2P'' - P$. Montrer que $f$ est un endomorphisme de $\mathbb{R}_2[X]$.
