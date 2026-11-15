# Contrôle TD 4 (S2) — lundi 9 avril 2018 (sujet, FR)

- Source : `raw/S2/TDs/2022/td4-2022-s2-maths-subject-fr.pdf` (scan, 2 pages)
- Date réelle : 9 avril 2018 (dossier promo 2022). Pas de corrigé dans les annales. Corrigé rédigé : `td4-2022-s2-maths-correction-fr.md` (même dossier).

## Question de cours
Type : noyau, image, injectivité, surjectivité (cours) · ECUE : ALM · Niveau : maths-s2-alm/2
Formules : sous-espace : contient 0 et stable par $\alpha u + v$ ; $f(\alpha u + v) = \alpha f(u) + f(v)$ ; injective $\iff \mathrm{Ker} f = \{0\}$ ; surjective $\iff \mathrm{Im} f = F$

Soient $E$ et $F$ deux $\mathbb{R}$-ev, et $\varphi \in \mathscr{L}(E,F)$ une application linéaire de $E$ dans $F$.
- a. Donner la définition mathématique précise de $\mathrm{Ker}(\varphi)$ et $\mathrm{Im}(\varphi)$.
- b. À quelle condition $\varphi$ est-elle injective ? À quelle condition $\varphi$ est-elle surjective ? Répondez à ces deux questions en vous servant obligatoirement des notions de la question précédente.

## Exercice 1
Type : application linéaire (caractérisation) · ECUE : ALM · Niveau : maths-s2-alm/1
Formules : $f$ linéaire $\Rightarrow f(0) = 0$ et $f(2x) = 2f(x)$ (conditions nécessaires) ; réciproquement vérifier $f(\lambda x + y) = \lambda f(x) + f(y)$ ; les applications linéaires de $\mathbb{R}$ dans $\mathbb{R}$ sont $x \mapsto bx$

Soit $\Delta : \mathbb{R}[X] \to \mathbb{R}[X]$, $P \mapsto XP' - 2P$. Montrer que $\Delta$ est linéaire.

## Exercice 2
Type : sous-espaces, intersection, somme directe · ECUE : EV · Niveau : maths-s2-ev/9
Formules : $\mathrm{Vect}(u)$ : droite si $u \neq 0$ ; plan $ax + by + cz = 0$ : exprimer $z$, $G = \mathrm{Vect}(u, v)$ ; $u \in F \cap G$ : paramétrer par $F$ puis injecter l'équation de $G$ ; Grassmann $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$ ; $F \oplus G = E \iff F \cap G = \{0\}$ et $\dim F + \dim G = \dim E$

Soient $E = \{(u_n) \in \mathbb{R}^{\mathbb{N}},\ u_0 = u_1 = 0\}$ et $F = \{(v_n) \in \mathbb{R}^{\mathbb{N}},\ \exists (a,b) \in \mathbb{R}^2,\ \forall n \in \mathbb{N},\ v_n = an + b\}$ deux sev de $\mathbb{R}^{\mathbb{N}}$. Montrer que $E$ et $F$ sont supplémentaires.

## Exercice 3
Type : écrire un sous-espace sous forme de Vect (système linéaire) · ECUE : EV · Niveau : maths-s2-ev/4
Formules : résoudre le système par pivot de Gauss ; exprimer les inconnues principales en fonction des inconnues libres ; factoriser chaque paramètre : $\{(x,y,z)\} = \{t\,u,\ t \in \mathbb{R}\} = \mathrm{Vect}(u)$ ; nombre de paramètres libres = dimension

Soit $E = \left\{ \begin{pmatrix} x \\ y \\ z \end{pmatrix} \in \mathbb{R}^3 \text{ tel que } \begin{cases} -x - 3y + 2z = 0 \\ -x + y - 2z = 0 \\ -x + 3y - 4z = 0 \end{cases} \right\}$. Écrire $E$ sous forme de sev engendré en utilisant la notation Vect.
