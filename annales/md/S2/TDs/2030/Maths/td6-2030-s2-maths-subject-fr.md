# Feuille de TD — Applications linéaires et matrices (S2 2026) (sujet, FR)

- Source : `raw/S2/TDs/2030/Maths/td6-2030-s2-maths-subject-fr.pdf` (9 pages)
- Date réelle : S2 2026 (dossier promo 2030). Feuille de TD, ECUE ALM. Pas de corrigé dans les annales.
- Seuls les exercices sont transcrits, avec la proposition à connaître par cœur. Les exercices marqués ⋆ sont plus difficiles.

Proposition à connaître par cœur : soient $E$ et $F$ deux $\mathbb{R}$-espaces vectoriels de dimension finie, $\mathcal{B}_1$ une base de $E$, $\mathcal{B}_2$ une base de $F$ et $f \in \mathcal{L}(E,F)$. Alors $\mathrm{Mat}_{\mathcal{B}_2}(f(u)) = \mathrm{Mat}_{\mathcal{B}_1,\mathcal{B}_2}(f) \times \mathrm{Mat}_{\mathcal{B}_1}(u)$, où $\mathrm{Mat}_{\mathcal{B}_2}(f(u))$ est la colonne des coordonnées de $f(u)$ dans $\mathcal{B}_2$, $\mathrm{Mat}_{\mathcal{B}_1,\mathcal{B}_2}(f)$ la matrice de $f$ dans la base $\mathcal{B}_1$ au départ et $\mathcal{B}_2$ à l'arrivée, et $\mathrm{Mat}_{\mathcal{B}_1}(u)$ la colonne des coordonnées de $u$ dans $\mathcal{B}_1$.

## Exercice 1.1
Type : application linéaire définie par l'image d'une base · ECUE : ALM · Niveau : maths-s2-alm/1
Formules : linéarité : $f(\alpha u + \beta v) = \alpha f(u) + \beta f(v)$ ; $u = \sum x_ie_i \Rightarrow f(u) = \sum x_if(e_i)$ ; une application linéaire est entièrement déterminée par l'image d'une base ; deux applications linéaires égales sur une base (ou une famille génératrice) sont égales ; si les vecteurs donnés sont liés, les images doivent vérifier la même relation ; s'ils n'engendrent pas l'espace, $f$ n'est pas déterminée

Soit $f : \mathbb{R}^3 \to \mathbb{R}^2$ une application linéaire telle que $f(e_1) = (2,1)$, $f(e_2) = (-1,1)$, $f(e_3) = (1,7)$.
1. Est-ce que $f$ peut prendre la valeur $(3,1)$ en $(1,-1,0)$ ?
2. Quelle est la valeur que prend $f$ en $(1,2,3)$ ?
3. Plus généralement, quelle valeur prend $f$ en un point $(x,y,z) \in \mathbb{R}^3$ en fonction des coordonnées $x$, $y$ et $z$ ?

## Exercice 1.2
Type : application linéaire définie par l'image d'une base · ECUE : ALM · Niveau : maths-s2-alm/1
Formules : linéarité : $f(\alpha u + \beta v) = \alpha f(u) + \beta f(v)$ ; $u = \sum x_ie_i \Rightarrow f(u) = \sum x_if(e_i)$ ; une application linéaire est entièrement déterminée par l'image d'une base ; deux applications linéaires égales sur une base (ou une famille génératrice) sont égales ; si les vecteurs donnés sont liés, les images doivent vérifier la même relation ; s'ils n'engendrent pas l'espace, $f$ n'est pas déterminée

Soit $f : \mathbb{R}^3 \to \mathbb{R}^2$ une application linéaire telle que $f(0,1,1) = (2,1)$, $f(0,1,0) = (-1,1)$, $f(0,-1,1) = (4,-1)$.
1. Quelle est la valeur que prend $f$ en $(0,1,2)$ ?
2. Quelle est la valeur que prend $f$ en $(1,0,2)$ ? Quel est le souci ?

## Exercice 1.3
Type : application linéaire définie par l'image d'une base · ECUE : ALM · Niveau : maths-s2-alm/1
Formules : linéarité : $f(\alpha u + \beta v) = \alpha f(u) + \beta f(v)$ ; $u = \sum x_ie_i \Rightarrow f(u) = \sum x_if(e_i)$ ; une application linéaire est entièrement déterminée par l'image d'une base ; deux applications linéaires égales sur une base (ou une famille génératrice) sont égales ; si les vecteurs donnés sont liés, les images doivent vérifier la même relation ; s'ils n'engendrent pas l'espace, $f$ n'est pas déterminée

Lors d'une de vos séances de TD, votre enseignant vous décrit une application linéaire $f : \mathbb{R}^3 \to \mathbb{R}^3$ donnée par $f(1,2,1) = (1,1,1)$, $f(-1,1,1) = (-1,1,1)$, $f(0,3,2) = (0,0,1)$. Pourquoi a-t-il fait une erreur de typo ?

## Exercice 1.4
Type : application linéaire définie par l'image d'une base · ECUE : ALM · Niveau : maths-s2-alm/1
Formules : linéarité : $f(\alpha u + \beta v) = \alpha f(u) + \beta f(v)$ ; $u = \sum x_ie_i \Rightarrow f(u) = \sum x_if(e_i)$ ; une application linéaire est entièrement déterminée par l'image d'une base ; deux applications linéaires égales sur une base (ou une famille génératrice) sont égales ; si les vecteurs donnés sont liés, les images doivent vérifier la même relation ; s'ils n'engendrent pas l'espace, $f$ n'est pas déterminée

1. Soient $E$ et $F$ deux $\mathbb{R}$-ev, $f$ et $g$ deux applications linéaires de $E$ dans $F$. On suppose de plus que $E$ est de dimension finie et on note $\mathcal{B}$ une base de $E$.
   - (a) Que signifie $f = g$ ?
   - (b) Montrer que $f = g$ si et seulement si $\forall u \in \mathcal{B}$, $f(u) = g(u)$.
2. Soient $F$ un $\mathbb{R}$-ev et $(f,g) \in \mathcal{L}(\mathbb{R}^2, F)^2$. Soit $A$ une partie de $\mathbb{R}^2$. On suppose que $\forall u \in A$, $f(u) = g(u)$. A-t-on $f = g$ (sur $\mathbb{R}^2$) dans les cas suivants ?
   - (a) $A = \mathbb{N}^2$
   - (b) $A$ est le disque de rayon 1, centré en l'origine
   - (c) $A$ est une droite vectorielle de $\mathbb{R}^2$
   - (d) $A$ est la droite affine $y = 2x + 1$

## Exercice 1.5
Type : matrice d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/5
Formules : colonne $j$ = coordonnées de $f(e_j)$ dans la base d'arrivée ; base canonique de $\mathbb{R}_2[X]$ : $(1, X, X^2)$ ; de $\mathcal{M}_2(\mathbb{R})$ : $E_{11}, E_{12}, E_{21}, E_{22}$ ; taille (dim arrivée) $\times$ (dim départ)

1. Soit $f \in \mathcal{L}(\mathbb{R}^2)$ tel que $f(e_1) = (2,3)$ et $f(e_2) = (-1,5)$ où $(e_1, e_2)$ est la base canonique de $\mathbb{R}^2$.
   - (a) Soit $(x,y) \in \mathbb{R}^2$. Que vaut $f((x,y))$ ?
   - (b) Soient $A = \begin{pmatrix} 2 & -1 \\ 3 & 5 \end{pmatrix}$ et $U = \begin{pmatrix} x \\ y \end{pmatrix}$. Calculer $AU$. Que remarquez-vous ?
2. Soient $u_1 = (1,-1)$ et $u_2 = (1,0)$ et $f \in \mathcal{L}(\mathbb{R}^2)$ tel que $f(u_1) = (2,3)$ et $f(u_2) = (-1,5)$.
   - (a) Soit $(x,y) \in \mathbb{R}^2$. Peut-on calculer $f((x,y))$ ? Si oui, le calculer.
   - (b) À quel produit matriciel cela correspond-il ?

## Exercice 2.6
Type : matrice d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/5
Formules : colonne $j$ = coordonnées de $f(e_j)$ dans la base d'arrivée ; base canonique de $\mathbb{R}_2[X]$ : $(1, X, X^2)$ ; de $\mathcal{M}_2(\mathbb{R})$ : $E_{11}, E_{12}, E_{21}, E_{22}$ ; taille (dim arrivée) $\times$ (dim départ)

Décrire les matrices des applications linéaires suivantes dans les bases indiquées :
1. $f : \mathbb{R}^2 \to \mathbb{R}^2$, $(x,y) \mapsto (2x + y,\ x - y)$
   - (a) dans la base canonique de $\mathbb{R}^2$ au départ et à l'arrivée ;
   - (b) dans la base canonique au départ et $((1,1), (1,-1))$ à l'arrivée ;
   - (c) dans la base $((1,1), (1,-1))$ au départ et la base canonique à l'arrivée ;
   - (d) dans la base $((1,-1), (1,1))$ au départ et la base canonique à l'arrivée ;
   - (e) dans la base $((1,1), (1,-1))$ au départ et $((0,1), (1,1))$ à l'arrivée.
2. $g : \mathbb{R}^3 \to \mathbb{R}^2$, $(x,y,z) \mapsto (3x - y + z,\ y - 2z)$
   - (a) dans les bases canoniques de $\mathbb{R}^3$ et $\mathbb{R}^2$ ;
   - (b) dans la base $((0,1,1), (1,0,1), (1,1,0))$ au départ et la base $((1,-1), (1,1))$ à l'arrivée.
3. (Travail personnel) $h : \mathbb{R}^4 \to \mathbb{R}$, $(x,y,z,t) \mapsto x - 2y + 3t$
   - (a) dans les bases canoniques au départ et à l'arrivée ;
   - (b) dans la base canonique au départ et la base $(2)$ à l'arrivée.
4. (⋆) $\ell : \mathbb{R}^p \to \mathbb{R}^n$, $\begin{pmatrix} x_1 \\ \vdots \\ x_p \end{pmatrix} \mapsto \begin{pmatrix} a_{11}x_1 + \dots + a_{1p}x_p \\ \vdots \\ a_{n1}x_1 + \dots + a_{np}x_p \end{pmatrix}$ où les $a_{ij}$ sont des réels, dans les bases canoniques de $\mathbb{R}^p$ et $\mathbb{R}^n$.
5. $\varphi : \mathbb{R}_3[X] \to \mathbb{R}_3[X]$, $P \mapsto P'$
   - (a) dans la base canonique $(1, X, X^2, X^3)$ au départ et à l'arrivée ;
   - (b) dans la base $(1,\ X + 1,\ X^2 - 1,\ X^3 + X)$ au départ et la base canonique à l'arrivée ;
   - (c) dans la base canonique au départ et la base $(1,\ X + 1,\ X^2 - 1,\ X^3 + X)$ à l'arrivée.

## Exercice 2.7
Type : changement de base, formule $Y = AX$ · ECUE : ALM · Niveau : maths-s2-alm/9
Formules : $X = PX'$, $P$ = matrice de passage (colonnes = nouveaux vecteurs dans l'ancienne base) ; $X' = P^{-1}X$ ; $f(e_j) = \sum_i a_{i,j}\varepsilon_i$ ; coordonnées de l'image $Y = AX$ ; inverse $2 \times 2$ : $\frac1{ad - bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$

Considérons la matrice $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{pmatrix}$.
1. À quelle application linéaire $f \in \mathcal{L}(\mathbb{R}^n, \mathbb{R}^p)$ (avec $n$ et $p$ à déterminer) la matrice $A$ est-elle associée dans les bases canoniques au départ et à l'arrivée ?
2. À quelle application linéaire $g \in \mathcal{L}(\mathbb{R}_n[X], \mathbb{R}_p[X])$ (avec $n$ et $p$ à déterminer) la matrice $A$ est-elle associée dans les bases canoniques au départ et à l'arrivée ?
3. Supposons que $A$ soit la matrice de l'application linéaire $h \in \mathcal{L}(\mathbb{R}^2, \mathbb{R}^3)$ dans la base $(u_1 = (1,1),\ u_2 = (1,-1))$ au départ et la base canonique à l'arrivée. Quelle est l'image de $u = (3,1)$ par $h$ ?
4. Supposons que $A$ soit la matrice de l'application linéaire $\varphi \in \mathcal{L}(\mathbb{R}^2, \mathbb{R}_2[X])$ dans la base $((1,2), (3,4))$ au départ et la base $(P_1 = 1,\ P_2 = X + 1,\ P_3 = (X-1)^2)$ à l'arrivée. Soit $u = (4,6)$. Trouver $a$, $b$ et $c$ réels tels que $\varphi(u) = aX^2 + bX + c$.

## Exercice 2.8
Type : opérations matricielles, produit, inverse · ECUE : ALM · Niveau : maths-s2-alm/6
Formules : $(\lambda A + \mu B)_{ij} = \lambda a_{ij} + \mu b_{ij}$ ; produit $AB$ défini si (colonnes de $A$) = (lignes de $B$), taille $n \times p$ par $p \times q$ donne $n \times q$ ; $(AB)_{ij} = \sum_k a_{ik}b_{kj}$ ; inverse par pivot de Gauss ; vérification $AA^{-1} = I$

On considère les applications linéaires $f : \mathbb{R}^2 \to \mathbb{R}^2$, $(x,y) \mapsto (-2x + 4y,\ x - y)$ et $g : \mathbb{R}^3 \to \mathbb{R}^2$, $(x,y,z) \mapsto (z + x,\ 2z + 3x - y)$. On note respectivement $M_f$ et $M_g$ les matrices de $f$ et $g$ dans les bases canoniques au départ et à l'arrivée.
1. Donner $M_f$ et $M_g$. Peut-on faire $M_f \times M_g$ et/ou $M_g \times M_f$ ? Si oui, effectuer le(s) produit(s) matriciel(s).
2. Peut-on faire $f \circ g$ et/ou $g \circ f$ ? Si oui, en trouver l'expression. En déduire la matrice $M$ associée dans les bases canoniques au départ et à l'arrivée.
3. Faire le lien matriciel entre $M$, $M_f$ et $M_g$.

## Exercice 2.9
Type : opérations matricielles, produit, inverse · ECUE : ALM · Niveau : maths-s2-alm/6
Formules : $(\lambda A + \mu B)_{ij} = \lambda a_{ij} + \mu b_{ij}$ ; produit $AB$ défini si (colonnes de $A$) = (lignes de $B$), taille $n \times p$ par $p \times q$ donne $n \times q$ ; $(AB)_{ij} = \sum_k a_{ik}b_{kj}$ ; inverse par pivot de Gauss ; vérification $AA^{-1} = I$

1. Soient $E$ un $\mathbb{R}$-espace vectoriel de dimension finie $n \in \mathbb{N}^*$ et $\mathrm{id}_E$ l'application identité de $E$. Soit $\mathcal{B} = (e_1, e_2, \dots, e_n)$ une base de $E$.
   - (a) Quelle est la matrice $I_n$ de $\mathrm{id}_E$ dans la base $\mathcal{B}$ au départ et à l'arrivée ?
   - (b) Soit $f$ un endomorphisme de $E$. On note $A$ sa matrice dans la base $\mathcal{B}$ au départ et à l'arrivée. Calculer, pour tout $u \in E$, $f \circ \mathrm{id}_E(u)$ et $\mathrm{id}_E \circ f(u)$. En déduire $f \circ \mathrm{id}_E$ et $\mathrm{id}_E \circ f$ et faire le lien matriciel entre $A$ et $I_n$.
2. (Travail personnel) Soient $f \in \mathcal{L}(\mathbb{R}^2, \mathbb{R}^2)$, $g \in \mathcal{L}(\mathbb{R}^3, \mathbb{R}^3)$ et $h \in \mathcal{L}(\mathbb{R}^3, \mathbb{R}^2)$ associées respectivement aux matrices $A$, $B$ et $C$ dans les bases canoniques : $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$, $B = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 3 & 1 \\ 1 & 3 & 2 \end{pmatrix}$ et $C = \begin{pmatrix} 0 & 2 & 4 \\ 1 & 3 & 5 \end{pmatrix}$.
   - (a) Identifier les compositions possibles entre $f$, $g$ et $h$ : $f \circ f$, $f \circ g$, $g \circ f$, $g \circ g$, $g \circ h$, $h \circ g$, $h \circ f$, $f \circ h$, $h \circ h$ ?
   - (b) Calculer les matrices correspondant à ces applications.

## Exercice 2.10
Type : noyau, image, rang ; matrice d'une application linéaire · ECUE : ALM · Niveau : maths-s2-alm/5
Formules : $\mathrm{Ker} f$ : résoudre $f(P) = 0$ ; théorème du rang $\dim E = \dim\mathrm{Ker} f + \dim\mathrm{Im} f$ ; injective $\iff \mathrm{Ker} = \{0\}$ ; $\dim\mathrm{Im} = \dim F \Rightarrow$ surjective ; colonne $j$ = coordonnées de $f(e_j)$ dans la base d'arrivée

Définitions. Soit $f$ une application linéaire d'un $\mathbb{R}$-espace vectoriel $E$ vers un $\mathbb{R}$-espace vectoriel $F$. On appelle rang de $f$, noté $\mathrm{Rg}(f)$, la dimension de l'image de $f$ : $\mathrm{Rg}(f) = \dim(\mathrm{Im}(f))$. Pour une matrice $A \in \mathcal{M}_{n,p}(\mathbb{R})$, on appelle rang de $A$, noté $\mathrm{Rg}(A)$, la dimension du sous-espace vectoriel engendré par ses colonnes. On note $0_{n,1}$ la colonne nulle de $\mathcal{M}_{n,1}(\mathbb{R})$.
1. Soient $E$ et $F$ deux espaces vectoriels de dimension finie, $\mathcal{B} = (e_1, \dots, e_p)$ une base de $E$, $\mathcal{B}'$ une base de $F$ et $f \in \mathcal{L}(E,F)$. On note $A \in \mathcal{M}_{n,p}(\mathbb{R})$ la matrice de $f$ dans la base $\mathcal{B}$ au départ et $\mathcal{B}'$ à l'arrivée, et $C_1, \dots, C_p$ ses colonnes.
   - (a) Montrer que $\mathrm{Im}(f) = \mathrm{Vect}(f(e_1), \dots, f(e_p))$.
   - (b) Soit $(\alpha_1, \dots, \alpha_p) \in \mathbb{R}^p$. Vérifier que $\alpha_1f(e_1) + \dots + \alpha_pf(e_p) = 0_F \iff \alpha_1\mathrm{Mat}_{\mathcal{B}'}(f(e_1)) + \dots + \alpha_p\mathrm{Mat}_{\mathcal{B}'}(f(e_p)) = 0_{n,1}$.
   - (c) En déduire que $\mathrm{Rg}(f) = \mathrm{Rg}(A)$.
   - (d) Supposons qu'il existe $(\alpha_1, \dots, \alpha_p) \in \mathbb{R}^p$ tel que $\alpha_1C_1 + \dots + \alpha_pC_p = 0_{n,1}$. Montrer que $\alpha_1e_1 + \dots + \alpha_pe_p \in \mathrm{Ker}(f)$.
2. Soit $f$ l'application linéaire associée à la matrice $A$ suivante dans la base canonique de $\mathbb{R}_2[X]$ au départ et à l'arrivée : $A = \begin{pmatrix} 1 & 2 & 0 \\ 1 & 0 & 2 \\ 1 & 1 & 1 \end{pmatrix}$. Trouver le rang, l'image et le noyau de $f$.
3. Reprendre la même démarche pour les applications linéaires $g \in \mathcal{L}(\mathbb{R}^2)$, $h \in \mathcal{L}(\mathbb{R}_2[X], \mathbb{R})$ et $i \in \mathcal{L}(\mathbb{R}^2, \mathbb{R}_2[X])$ associées aux matrices $B$, $C$ et $D$ dans les bases canoniques au départ et à l'arrivée : $B = \begin{pmatrix} 1 & 2 \\ -1 & 3 \end{pmatrix}$, $C = \begin{pmatrix} 1 & 2 & -1 \end{pmatrix}$, $D = \begin{pmatrix} 1 & 1 \\ 1 & 0 \\ 1 & 1 \end{pmatrix}$.
4. (⋆) Répondre aux mêmes questions pour l'application linéaire $\ell$ dont la matrice dans la base $((1,1), (1,-1))$ au départ et à l'arrivée est $\begin{pmatrix} 3 & 3 \\ -1 & -1 \end{pmatrix}$.

## Exercice 2.11 (⋆)
Type : changement de base, diagonalisation, puissance d'une matrice · ECUE : ALM · Niveau : maths-s2-alm/9
Formules : $\mathrm{Mat}_{\mathcal{B}'}(f) = P^{-1}AP$ avec $P = \mathrm{Mat}_{\mathcal{B}', \mathcal{B}}(id)$ (colonnes = vecteurs de $\mathcal{B}'$ dans $\mathcal{B}$) ; $f(u_i) = \lambda_iu_i \Rightarrow D = \mathrm{diag}(\lambda_i)$ ; $D^n = \mathrm{diag}(\lambda_i^n)$ ; $A = PDP^{-1} \Rightarrow A^n = PD^nP^{-1}$

On considère les applications linéaires $f$ et $g$ dont les matrices dans les bases canoniques sont respectivement $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ et $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$.
1. Quelle est la matrice de l'application linéaire $f \circ g$ dans les bases canoniques ? Celle de $g \circ f$ ?
2. Calculer la matrice de la composée de $g$ avec elle-même 10 fois, $g^{10}$, dans les bases canoniques.
3. Écrire les matrices de $f$ et $g$ respectivement dans la base $((1,1), (1,-1))$ au départ et à l'arrivée.
4. Exprimer $g^k$ et $f^k$ pour tout $k \in \mathbb{N}$.

## Exercice 3.12
Type : inverse d'une matrice, application linéaire associée · ECUE : ALM · Niveau : maths-s2-alm/8
Formules : pivot de Gauss sur $AU = V$ ; $A$ inversible $\iff f$ bijective, $\mathrm{Mat}(f^{-1}) = A^{-1}$ ; colonnes de $A$ = images des vecteurs de la base de départ ; $g(aX^2 + bX + c) = ag(X^2) + bg(X) + cg(1)$

1. Soit $f : \mathbb{R}^3 \to \mathbb{R}^3$ définie pour tout $(x,y,z) \in \mathbb{R}^3$ par $f((x,y,z)) = (x + y - 2z,\ x - y + z,\ -2x + y - z)$.
   - (a) Montrer que $f$ est bijective et déterminer $f^{-1}$.
   - (b) Soient $A$ la matrice de $f$ et $B$ la matrice de $f^{-1}$ dans la base canonique. Calculer $AB$ et $BA$. On note $A^{-1}$ la matrice $B$.
2. On admet que les matrices suivantes sont inversibles. Trouver leur matrice inverse : $C = \begin{pmatrix} 2 & 2 & 3 \\ 4 & 3 & 6 \\ -1 & -2 & -2 \end{pmatrix}$ et $D = \begin{pmatrix} 2 & 2 & 3 \\ -2 & 1 & 2 \\ -3 & 2 & 4 \end{pmatrix}$.

## Exercice 3.13
Type : changement de base, formule $Y = AX$ · ECUE : ALM · Niveau : maths-s2-alm/9
Formules : $X = PX'$, $P$ = matrice de passage (colonnes = nouveaux vecteurs dans l'ancienne base) ; $X' = P^{-1}X$ ; $f(e_j) = \sum_i a_{i,j}\varepsilon_i$ ; coordonnées de l'image $Y = AX$ ; inverse $2 \times 2$ : $\frac1{ad - bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$

Soient $E$ un $\mathbb{R}$-espace vectoriel de dimension finie $n$, $\mathcal{B}_1$ et $\mathcal{B}_2$ deux bases de $E$. On appelle matrice de passage de $\mathcal{B}_1$ vers $\mathcal{B}_2$ la matrice $n \times n$ dont les colonnes sont formées des coordonnées des vecteurs de $\mathcal{B}_2$ dans la base $\mathcal{B}_1$. On la note $P_{\mathcal{B}_1,\mathcal{B}_2}$.
1. Expliquer pourquoi toute matrice de passage $P_{\mathcal{B}_1,\mathcal{B}_2}$ est inversible. À quoi correspond $P_{\mathcal{B}_1,\mathcal{B}_2}^{-1}$ ?
2. Dans $\mathbb{R}^3$, on note $\mathcal{B}_1$ la base canonique et on considère une autre base $\mathcal{B}_2 = ((1,0,1), (0,1,0), (1,1,0))$.
   - (a) Donner la matrice de passage de $\mathcal{B}_1$ vers $\mathcal{B}_2$. On la notera $P$ pour simplifier.
   - (b) Soit $u = (x,y,z) \in \mathbb{R}^3$. On note $X = \begin{pmatrix} x \\ y \\ z \end{pmatrix}$ la colonne des coordonnées de $u$ dans $\mathcal{B}_1$ et $X' = \begin{pmatrix} x' \\ y' \\ z' \end{pmatrix}$ la colonne des coordonnées de $u$ dans $\mathcal{B}_2$. Exprimer $X$ en fonction de $P$ et de $X'$. En déduire aussi une expression de $X'$ en fonction de $X$.
   - (c) Soit $u = (1,2,3) \in \mathbb{R}^3$. Trouver $X$ et $X'$.
3. À votre avis, les formules de changement de bases vues dans la question précédente peuvent-elles se généraliser à n'importe quel espace vectoriel de dimension finie ?

## Exercice 3.14 (⋆)
Type : changement de base, formule $Y = AX$ · ECUE : ALM · Niveau : maths-s2-alm/9
Formules : $X = PX'$, $P$ = matrice de passage (colonnes = nouveaux vecteurs dans l'ancienne base) ; $X' = P^{-1}X$ ; $f(e_j) = \sum_i a_{i,j}\varepsilon_i$ ; coordonnées de l'image $Y = AX$ ; inverse $2 \times 2$ : $\frac1{ad - bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$

On reprend les notations de l'exercice 2.6 (1) : $f : \mathbb{R}^2 \to \mathbb{R}^2$, $(x,y) \mapsto (2x + y,\ x - y)$. On note $\mathcal{B} = (e_1, e_2)$ la base canonique de $\mathbb{R}^2$ et $\mathcal{B}' = ((1,1), (1,-1))$ une autre base de $\mathbb{R}^2$. On appelle $A$ la matrice de $f$ dans $\mathcal{B}$ (2.6 (1-a)), $B$ la matrice de $f$ dans la base $\mathcal{B}'$ au départ et la base $\mathcal{B}$ à l'arrivée (2.6 (1-c)) et $C$ la matrice de $f$ dans la base $\mathcal{B}$ au départ et la base $\mathcal{B}'$ à l'arrivée (2.6 (1-b)). L'objectif est de retrouver les matrices de f dans les bases décrites aux points 2.6 (1-b) et (1-c) à partir de la matrice $A$.
1. Quelle est la matrice de passage $P$ de la base $\mathcal{B}$ à la base $\mathcal{B}'$ ?
2. Pour $u \in \mathbb{R}^2$, on note $X$ (resp. $X'$) la colonne des coordonnées de $u$ dans $\mathcal{B}$ (resp. $\mathcal{B}'$) et $Y$ (resp. $Y'$) celle des coordonnées de $f(u)$ dans $\mathcal{B}$ (resp. $\mathcal{B}'$). Quel est le lien matriciel entre $X$ et $X'$ ? Entre $Y$ et $Y'$ ? Donner les relations matricielles qui relient $A$, $B$ et $C$ à $X$ et/ou $X'$, $Y$ et/ou $Y'$.
3. En déduire que $B = AP$ et $C = P^{-1}A$.
4. Notons $A'$ la matrice de $f$ dans la base $\mathcal{B}'$ au départ et à l'arrivée. En vous servant des questions précédentes, montrer que $A' = P^{-1}AP$.
