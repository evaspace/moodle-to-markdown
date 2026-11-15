"""Level path: S2 maths, ECUE ALM (applications linéaires, matrices, systèmes linéaires).

Moodle chapters 09, 10 and 11 (S2-MATHS-2030). Calibrated on Examen S2-B4 ALM 2026 (promo 2030), read on the
subject and the official correction, and on `annales/FORMULES.md` (« ALM »).
`value` exercises use sympy matrices (product, inverse, rank); `open` exercises have a model answer.
"""

SUBJECT = {
    "id": "maths-s2-alm",
    "ordre": 230,
    "matiere": "maths",
    "semestre": "S2",
    "ecue": "ALM",
    "titre": "Applications linéaires et matrices",
    "chapitres_moodle": ["09_Cours 5 - Applications linéaires", "10_Cours 6 - Matrices", "11_7 - Résolution de systèmes linéaires"],
    "td": "TD applications linéaires et matrices (S2 2030)",
    "examens": ["Examen S2-B4 ALM (avant l'été)"],
}

NOTIONS = [
    {"id": "lineaire", "titre": "Application linéaire",
     "formule": r"$f$ linéaire $\iff\forall(u,v),\ \forall\lambda,\ f(\lambda u+v)=\lambda f(u)+f(v)$ · alors $f(0)=0$ · $u=\sum x_ie_i\Rightarrow f(u)=\sum x_if(e_i)$",
     "exemple": r"$f(x,y)=(x+1,y)$ n'est pas linéaire : $f(0,0)=(1,0)\ne0$",
     "cours": r"Pour dire non : $f(0)\ne0$ ou $f(2u)\ne2f(u)$ sur un exemple. Pour dire oui : vérifier $f(\lambda u+v)=\lambda f(u)+f(v)$. Une application linéaire est entièrement déterminée par l'image d'une base."},
    {"id": "noyau", "titre": "Noyau, injectivité",
     "formule": r"$\mathrm{Ker}f=\{u\in E,\ f(u)=0_F\}$, sev de $E$ · $f$ injective $\iff\mathrm{Ker}f=\{0_E\}$",
     "exemple": r"$f(x,y)=(x-y,2x-2y)$ : $\mathrm{Ker}f=\mathrm{Vect}((1,1))$",
     "cours": r"Résoudre le système $f(u)=0$, puis écrire l'ensemble des solutions sous forme de Vect. Le nombre de paramètres libres est la dimension du noyau."},
    {"id": "image", "titre": "Image, surjectivité",
     "formule": r"$\mathrm{Im}f=\{f(u),\ u\in E\}=\mathrm{Vect}(f(e_1),\dots,f(e_n))$, sev de $F$ · $\mathrm{rg}f=\dim\mathrm{Im}f$ · $f$ surjective $\iff\mathrm{Im}f=F\iff\mathrm{rg}f=\dim F$",
     "exemple": r"$f(x,y)=(x-y,2x-2y)$ : $\mathrm{Im}f=\mathrm{Vect}((1,2))$, rang $1$",
     "cours": r"Les images des vecteurs d'une base engendrent l'image : on en extrait une base en retirant ceux qui sont combinaisons des autres. Sur une matrice : l'image est engendrée par les colonnes, le rang est le nombre de colonnes indépendantes."},
    {"id": "rang", "titre": "Théorème du rang",
     "formule": r"$E$ de dimension finie, $f\in\mathcal L(E,F)$ : $\dim E=\dim\mathrm{Ker}f+\mathrm{rg}f$ · si $\dim E=\dim F$ : injective $\iff$ surjective $\iff$ bijective",
     "exemple": r"$f:\mathbb R^3\to\mathbb R^2$ : $\mathrm{rg}f\le2$, donc $\dim\mathrm{Ker}f\ge1$ : jamais injective",
     "cours": r"$\dim E>\dim F$ : pas injective. $\dim E<\dim F$ : pas surjective. On calcule le plus facile des deux (noyau ou image) et on déduit la dimension de l'autre."},
    {"id": "matrice", "titre": "Matrice d'une application linéaire",
     "formule": r"colonne $j$ = coordonnées de $f(e_j)$ dans la base d'arrivée · taille $(\dim F)\times(\dim E)$ · coordonnées de l'image : $Y=AX$",
     "exemple": r"$f(x,y)=(2x-3y,-2x+y)$ : $\begin{pmatrix}2&-3\\-2&1\end{pmatrix}$",
     "cours": r"Calculer l'image de chaque vecteur de la base de départ, l'exprimer dans la base d'arrivée, ranger en colonnes. Base canonique de $\mathbb R_2[X]$ : $(1,X,X^2)$."},
    {"id": "produit", "titre": "Produit matriciel, transposée",
     "formule": r"$AB$ défini si (colonnes de $A$) = (lignes de $B$) : $n\times p$ par $p\times q$ donne $n\times q$ · $(AB)_{ij}=\sum_ka_{ik}b_{kj}$ · $AB\ne BA$ en général · ${}^t(AB)={}^tB\,{}^tA$",
     "exemple": r"$\begin{pmatrix}1&2\\3&4\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix}=\begin{pmatrix}2&1\\4&3\end{pmatrix}$",
     "cours": r"Coefficient $(i,j)$ : ligne $i$ de $A$ contre colonne $j$ de $B$. Le produit correspond à la composition des applications linéaires. Si $AB=BA$ : binôme $(A+B)^n=\sum\binom nkA^kB^{n-k}$."},
    {"id": "systeme", "titre": "Systèmes linéaires, pivot de Gauss",
     "formule": r"opérations $L_i\leftarrow L_i+\lambda L_j$, $L_i\leftrightarrow L_j$, $L_i\leftarrow\lambda L_i$ ($\lambda\ne0$) · système échelonné puis remontée · $0=c\ne0$ : pas de solution · inconnues libres : infinité de solutions",
     "exemple": r"$x+y=3$, $x-y=1$ : $L_2\leftarrow L_2-L_1$ donne $-2y=-2$, $y=1$, $x=2$",
     "cours": r"Éliminer la première inconnue dans toutes les lignes sauf la première, puis recommencer sur le sous-système. Écrire chaque opération. Vérifier la solution dans le système de départ."},
    {"id": "inverse", "titre": "Inverse d'une matrice",
     "formule": r"$A$ inversible $\iff\exists B,\ AB=BA=I_n$ (matrice carrée) · $2\times2$ : $\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1}=\frac1{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$ si $ad-bc\ne0$ · résoudre $AU=V$ par pivot : $U=A^{-1}V$",
     "exemple": r"$\begin{pmatrix}2&1\\5&3\end{pmatrix}^{-1}=\begin{pmatrix}3&-1\\-5&2\end{pmatrix}$",
     "cours": r"Méthode du système : résoudre $AU=V$ avec $V=(X,Y,Z)$ quelconque, lire $A^{-1}$ dans $U=A^{-1}V$. Toujours vérifier $AA^{-1}=I_n$. Une matrice non carrée n'est jamais inversible."},
    {"id": "changement", "titre": "Changement de base",
     "formule": r"$P$ = matrice de passage : colonnes = vecteurs de la nouvelle base dans l'ancienne · $X=PX'$, $X'=P^{-1}X$ · $\mathrm{Mat}_{\mathcal B'}(f)=P^{-1}AP$ · $A=PDP^{-1}\Rightarrow A^n=PD^nP^{-1}$",
     "exemple": r"$A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$, $P=\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ : $P^{-1}AP=\mathrm{diag}(3,1)$",
     "cours": r"Si $f(u_i)=\lambda_iu_i$ pour une base $(u_i)$, la matrice de $f$ dans cette base est diagonale. Bases différentes au départ et à l'arrivée : exprimer chaque $f(e_j)$ dans la base d'arrivée."},
    {"id": "projecteur", "titre": "Projecteurs et symétries",
     "formule": r"$p$ projecteur $\iff p\circ p=p$ · alors $E=\mathrm{Ker}p\oplus\mathrm{Im}p$, $p=id$ sur $\mathrm{Im}p$ · $E=F\oplus G$, $u=v+w$ : projection sur $F$ parallèlement à $G$ : $u\mapsto v$ ; symétrie : $u\mapsto v-w$, $s\circ s=id$, $s=2p-id$",
     "exemple": r"$p(x,y)=(x,0)$ : projection sur l'axe des abscisses parallèlement à l'axe des ordonnées",
     "cours": r"Dans une base adaptée à $E=F\oplus G$, la matrice de la projection sur $F$ est $\mathrm{diag}(1,\dots,1,0,\dots,0)$."},
]


def v(id, enonce, calc, ans, sol, src=None, duree=None):
    e = {"id": id, "kind": "value", "enonce": enonce, "calc": calc, "ans": ans, "sol": sol}
    if src:
        e["src"] = src
    if duree:
        e["duree"] = duree
    return e


def o(id, enonce, sol, src=None, duree=None):
    e = {"id": id, "kind": "open", "enonce": enonce, "sol": sol}
    if src:
        e["src"] = src
    if duree:
        e["duree"] = duree
    return e


def pm(rows):
    """LaTeX pmatrix from a list of rows."""
    return r"\begin{pmatrix}" + r"\\".join("&".join(str(c) for c in r) for r in rows) + r"\end{pmatrix}"


F30 = "Examen S2-B4 ALM 2026"
_A3 = [[1, 2, 3], [1, 3, 7], [-3, -7, -14]]
_A3I = [[-7, -7, -5], [7, 5, 4], [-2, -1, -1]]

LEVELS = [
    {"n": 1, "titre": "Reconnaître une application linéaire", "notions": ["lineaire"], "exos": [
        o("al1", r"$f:\mathbb R^2\to\mathbb R^2$, $f(x,y)=(x+y,2x)$ est-elle linéaire ?",
          r"Oui. Pour $u=(x,y)$, $v=(x',y')$ : $f(\lambda u+v)=(\lambda x+x'+\lambda y+y',\ 2\lambda x+2x')=\lambda(x+y,2x)+(x'+y',2x')=\lambda f(u)+f(v)$.", duree=3),
        o("al2", r"$f:\mathbb R^2\to\mathbb R^2$, $f(x,y)=(x+1,y)$ est-elle linéaire ?", r"Non : $f(0,0)=(1,0)\ne(0,0)$.", duree=2),
        o("al3", r"$f:\mathbb R\to\mathbb R$, $f(x)=x^2$ est-elle linéaire ?", r"Non : $f(2\times1)=4\ne2=2f(1)$.", duree=2),
        o("al4", r"Montrer que la dérivation $D:\mathbb R[X]\to\mathbb R[X]$, $P\mapsto P'$ est linéaire.",
          r"$(\lambda P+Q)'=\lambda P'+Q'$, donc $D(\lambda P+Q)=\lambda D(P)+D(Q)$.", duree=2),
        v("al5", r"$f:\mathbb R^2\to\mathbb R^2$ est linéaire, $f(e_1)=(1,2)$ et $f(e_2)=(0,-1)$. Calculer $f(3,4)$.", "3*Matrix([1,2])+4*Matrix([0,-1])", "Matrix([3,2])",
          r"$f(3,4)=3f(e_1)+4f(e_2)=(3,6)+(0,-4)=(3,2)$.", duree=2),
        o("al6", r"Existe-t-il une application linéaire $f:\mathbb R^2\to\mathbb R^2$ telle que $f(1,0)=(1,1)$, $f(0,1)=(2,0)$ et $f(1,1)=(0,0)$ ?",
          r"Non. $(1,1)=(1,0)+(0,1)$, donc par linéarité $f(1,1)=(1,1)+(2,0)=(3,1)\ne(0,0)$. Les vecteurs donnés sont liés : les images doivent vérifier la même relation.", duree=3),
    ]},
    {"n": 2, "titre": "Noyau", "notions": ["noyau"], "exos": [
        o("an1", r"$f(x,y)=(x-y,\ 2x-2y)$. Déterminer $\mathrm{Ker}f$.",
          r"$f(x,y)=0\iff x=y$ : $\mathrm{Ker}f=\{(x,x)\}=\mathrm{Vect}((1,1))$.", duree=3),
        o("an2", r"$f:\mathbb R^3\to\mathbb R_2[X]$, $(a,b,c)\mapsto(a-b)X^2+(a+b-c)X-2a+2b$. Trouver la dimension du noyau de $f$, en précisant une base.",
          r"$\mathrm{Ker}f=\{(a,b,c),\ a-b=0,\ a+b-c=0,\ -2a+2b=0\}=\{(a,a,2a)\}=\mathrm{Vect}(u=(1,1,2))$. $u\ne0$ : $(u)$ est une base, $\dim\mathrm{Ker}f=1$.", src=f"{F30}, ex. 2.1"),
        o("an3", r"$f(x,y)=(x+y,\ x-y)$ est-elle injective ?",
          r"$f(x,y)=0\iff x+y=0$ et $x-y=0\iff x=y=0$. $\mathrm{Ker}f=\{0\}$ : $f$ est injective.", duree=3),
        v("an4", r"$f:\mathbb R^3\to\mathbb R^2$ a pour matrice $" + pm([[1, 2, 3], [2, 4, 6]]) + r"$. Quelle est la dimension de $\mathrm{Ker}f$ ?",
          "3-Matrix([[1,2,3],[2,4,6]]).rank()", "2", r"$L_2=2L_1$ : une seule équation $x+2y+3z=0$, deux paramètres libres. $\dim\mathrm{Ker}f=2$.", duree=3),
        o("an5", r"Déterminer le noyau de la dérivation $D:\mathbb R_2[X]\to\mathbb R_2[X]$, $P\mapsto P'$. $D$ est-elle injective ?",
          r"$P'=0\iff P$ constant : $\mathrm{Ker}D=\mathrm{Vect}(1)$. $\mathrm{Ker}D\ne\{0\}$ : $D$ n'est pas injective.", duree=3),
        o("an6", r"Soit $f\in\mathcal L(E,F)$. Montrer que $f$ est injective si et seulement si $\mathrm{Ker}f=\{0_E\}$.",
          r"Si $f$ est injective et $f(x)=0=f(0)$, alors $x=0$. Réciproquement, si $\mathrm{Ker}f=\{0\}$ et $f(x)=f(y)$ : $f(x-y)=f(x)-f(y)=0$, donc $x-y\in\mathrm{Ker}f$, $x=y$."),
    ]},
    {"n": 3, "titre": "Image et rang", "notions": ["image"], "exos": [
        o("ai1", r"$f(x,y)=(x-y,\ 2x-2y)$. Déterminer $\mathrm{Im}f$ et le rang de $f$.",
          r"$\mathrm{Im}f=\mathrm{Vect}(f(e_1),f(e_2))=\mathrm{Vect}((1,2),(-1,-2))=\mathrm{Vect}((1,2))$. Rang $1$.", duree=3),
        v("ai2", r"Quel est le rang de $" + pm([[1, 2], [3, 6]]) + r"$ ?", "Matrix([[1,2],[3,6]]).rank()", "1", r"$C_2=2C_1$ : une seule colonne indépendante. Rang $1$.", duree=2),
        v("ai3", r"Quel est le rang de $" + pm([[1, 0, 1], [0, 1, 1], [1, 1, 2]]) + r"$ ?", "Matrix([[1,0,1],[0,1,1],[1,1,2]]).rank()", "2",
          r"$C_3=C_1+C_2$, et $C_1$, $C_2$ ne sont pas colinéaires. Rang $2$.", duree=3),
        o("ai4", r"$f:\mathbb R^3\to\mathbb R_2[X]$, $(a,b,c)\mapsto(a-b)X^2+(a+b-c)X-2a+2b$, de rang $2$. Trouver une base de $\mathrm{Im}f$.",
          r"$\mathrm{Im}f=\{a(X^2+X-2)+b(-X^2+X+2)+c(-X)\}=\mathrm{Vect}(P_1,P_2,P_3)$ avec $P_1+P_2=2X=-2P_3$, donc $\mathrm{Im}f=\mathrm{Vect}(P_1,P_2)$. Famille génératrice de cardinal $2=\dim\mathrm{Im}f$ : $(P_1=X^2+X-2,\ P_2=-X^2+X+2)$ est une base.", src=f"{F30}, ex. 2.3"),
        o("ai5", r"$f:\mathbb R^3\to\mathbb R^2$, $f(x,y,z)=(x+y,\ y+z)$ est-elle surjective ?",
          r"$f(e_1)=(1,0)$ et $f(e_2)=(1,1)$ ne sont pas colinéaires : $\mathrm{rg}f=2=\dim\mathbb R^2$. $f$ est surjective.", duree=3),
        o("ai6", r"$f\in\mathcal L(\mathbb R^3,\mathbb R_2[X])$ a pour matrice dans les bases canoniques $A=" + pm([[1, 2, -1], [-2, 1, 2], [1, 0, -1]]) + r"$. En raisonnant sur les colonnes, trouver le rang de $A$, une base de l'image et une base du noyau de $f$.",
          r"$C_3=-C_1$, donc $\mathrm{Im}f=\mathrm{Vect}(C_1,C_2)$, soit $\mathrm{Vect}(1-2X+X^2,\ 2+X)$. Ces deux polynômes ne sont pas colinéaires : base de $\mathrm{Im}f$, rang $2$. Théorème du rang : $\dim\mathrm{Ker}f=3-2=1$. $C_1+C_3=0$ donne $f(1,0,1)=0$ : $u=(1,0,1)$, non nul, est une base de $\mathrm{Ker}f$.", src=f"{F30}, ex. 5 (5 points)", duree=7),
    ]},
    {"n": 4, "titre": "Théorème du rang", "notions": ["rang"], "exos": [
        o("at0", r"Énoncer rigoureusement le théorème du rang.",
          r"Soient $E$ un espace vectoriel de dimension finie et $f\in\mathcal L(E,F)$. Alors $\dim E=\dim\mathrm{Ker}f+\dim\mathrm{Im}f$.", src=f"{F30}, ex. 2.2", duree=2),
        v("at1", r"$f:\mathbb R^5\to\mathbb R^3$ est linéaire et surjective. Quelle est la dimension de $\mathrm{Ker}f$ ?", "5-3", "2",
          r"$\mathrm{rg}f=3$, donc $\dim\mathrm{Ker}f=5-3=2$.", duree=2),
        v("at2", r"$f$ est un endomorphisme de $\mathbb R^4$ et $\dim\mathrm{Ker}f=1$. Quel est le rang de $f$ ?", "4-1", "3", r"$\mathrm{rg}f=4-1=3$.", duree=2),
        o("at3", r"Une application linéaire $f:\mathbb R^3\to\mathbb R^2$ peut-elle être injective ?",
          r"Non. $\mathrm{rg}f\le2$, donc $\dim\mathrm{Ker}f=3-\mathrm{rg}f\ge1$ : $\mathrm{Ker}f\ne\{0\}$.", duree=3),
        o("at4", r"Une application linéaire $f:\mathbb R^2\to\mathbb R^3$ peut-elle être surjective ?",
          r"Non. $\mathrm{rg}f=2-\dim\mathrm{Ker}f\le2<3$ : $\mathrm{Im}f\ne\mathbb R^3$.", duree=3),
        o("at5", r"Soit $f$ un endomorphisme de $E$ de dimension finie $n$. Montrer que $f$ injective $\iff f$ surjective.",
          r"Injective $\iff\dim\mathrm{Ker}f=0\iff\mathrm{rg}f=n$ (théorème du rang) $\iff\mathrm{Im}f=E$ (sev de même dimension que $E$) $\iff$ surjective.", duree=4),
    ]},
    {"n": 5, "titre": "Matrice d'une application linéaire", "notions": ["matrice"], "exos": [
        o("am1", r"$f:\mathbb R^2\to\mathbb R^2$, $(x,y)\mapsto(2x-3y,\ -2x+y)$. Écrire la matrice de $f$ dans la base canonique.",
          r"$f(e_1)=(2,-2)$, $f(e_2)=(-3,1)$, rangés en colonnes : $" + pm([[2, -3], [-2, 1]]) + r"$.", src=f"{F30}, ex. 3.1 (a)", duree=2),
        o("am2", r"Écrire la matrice de la dérivation $D:\mathbb R_2[X]\to\mathbb R_2[X]$ dans la base canonique $(1,X,X^2)$.",
          r"$D(1)=0$, $D(X)=1$, $D(X^2)=2X$ : $" + pm([[0, 1, 0], [0, 0, 2], [0, 0, 0]]) + r"$.", duree=3),
        v("am3", r"$f$ a pour matrice $A=" + pm([[1, 2], [0, -1]]) + r"$ dans la base canonique. Calculer $f(3,1)$.", "Matrix([[1,2],[0,-1]])*Matrix([3,1])", "Matrix([5,-1])",
          r"$Y=AX$ : $(3+2,\ -1)=(5,-1)$.", duree=2),
        o("am4", r"Quelle est la taille de la matrice d'une application linéaire de $\mathbb R^3$ dans $\mathbb R^2$ ?",
          r"$2$ lignes ($\dim$ arrivée) et $3$ colonnes ($\dim$ départ) : $2\times3$.", duree=2),
        o("am5", r"$f:\mathbb R^3\to\mathbb R^2$, $f(x,y,z)=(x+y,\ y-z)$. Écrire sa matrice dans les bases canoniques.",
          r"$f(e_1)=(1,0)$, $f(e_2)=(1,1)$, $f(e_3)=(0,-1)$ : $" + pm([[1, 1, 0], [0, 1, -1]]) + r"$.", duree=3),
    ]},
    {"n": 6, "titre": "Produit matriciel", "notions": ["produit"], "exos": [
        v("ap1", r"Calculer $" + pm([[1, 2], [3, 4]]) + pm([[0, 1], [1, 0]]) + r"$.", "Matrix([[1,2],[3,4]])*Matrix([[0,1],[1,0]])", "Matrix([[2,1],[4,3]])",
          r"$" + pm([[2, 1], [4, 3]]) + r"$ : multiplier à droite par cette matrice échange les colonnes.", duree=3),
        v("ap2", r"$A=" + pm([[-2, 1, 2], [-1, 3, -1]]) + r"$ et $B=" + pm([[2, 1], [1, -2]]) + r"$. Les produits $AB$ et $BA$ sont-ils définis ? Effectuer celui qui l'est.",
          "Matrix([[2,1],[1,-2]])*Matrix([[-2,1,2],[-1,3,-1]])", "Matrix([[-5,5,3],[0,-5,4]])",
          r"$A$ a $3$ colonnes et $B$ a $2$ lignes : $AB$ n'est pas défini. $B$ a $2$ colonnes et $A$ a $2$ lignes : $BA$ est défini ($2\times3$), $BA=" + pm([[-5, 5, 3], [0, -5, 4]]) + r"$.", src=f"{F30}, ex. 1.1"),
        v("ap3", r"$A=" + pm([[1, 1], [0, 1]]) + r"$. Calculer $A^3$.", "Matrix([[1,1],[0,1]])**3", "Matrix([[1,3],[0,1]])",
          r"$A^2=" + pm([[1, 2], [0, 1]]) + r"$, $A^3=" + pm([[1, 3], [0, 1]]) + r"$.", duree=3),
        v("ap4", r"$A=" + pm([[1, 2], [0, 1]]) + r"$ et $B=" + pm([[1, 0], [1, 1]]) + r"$. Calculer $AB-BA$. Les matrices commutent-elles ?",
          "Matrix([[1,2],[0,1]])*Matrix([[1,0],[1,1]])-Matrix([[1,0],[1,1]])*Matrix([[1,2],[0,1]])", "Matrix([[2,0],[0,-2]])",
          r"$AB=" + pm([[3, 2], [1, 1]]) + r"$, $BA=" + pm([[1, 2], [1, 3]]) + r"$, $AB-BA=" + pm([[2, 0], [0, -2]]) + r"\ne0$ : elles ne commutent pas."),
        v("ap5", r"$A=" + pm([[1, 2], [3, 4]]) + r"$. Calculer ${}^tA\,A$.", "Matrix([[1,2],[3,4]]).T*Matrix([[1,2],[3,4]])", "Matrix([[10,14],[14,20]])",
          r"${}^tA=" + pm([[1, 3], [2, 4]]) + r"$, ${}^tA\,A=" + pm([[10, 14], [14, 20]]) + r"$ (symétrique).", duree=3),
        v("ap6", r"$U=" + pm([[1], [2], [3]]) + r"$. Calculer ${}^tU\,U$.", "(Matrix([1,2,3]).T*Matrix([1,2,3]))[0]", "14",
          r"${}^tU\,U=1^2+2^2+3^2=14$ (un scalaire ; $U\,{}^tU$ serait une matrice $3\times3$).", duree=2),
        v("ap7", r"$A=" + pm([[-3, 7, -1], [-1, 2, 0]]) + r"$ et $B=" + pm([[-2, 5], [-1, 3], [-2, 6]]) + r"$. Calculer $AB$. La matrice $A$ est-elle inversible ?",
          "Matrix([[-3,7,-1],[-1,2,0]])*Matrix([[-2,5],[-1,3],[-2,6]])", "Matrix([[1,0],[0,1]])",
          r"$AB=I_2$. Mais $A$ n'est pas carrée : elle n'est pas inversible.", src=f"{F30}, ex. 1.2"),
    ]},
    {"n": 7, "titre": "Systèmes linéaires", "notions": ["systeme"], "exos": [
        v("as1", r"Résoudre $\begin{cases}x+y=3\\x-y=1\end{cases}$", "Matrix([[1,1],[1,-1]]).inv()*Matrix([3,1])", "Matrix([2,1])",
          r"$L_2\leftarrow L_2-L_1$ : $-2y=-2$, $y=1$, puis $x=2$.", duree=2),
        v("as2", r"Résoudre $\begin{cases}x+y+z=6\\x-y+z=2\\x+y-z=0\end{cases}$", "Matrix([[1,1,1],[1,-1,1],[1,1,-1]]).inv()*Matrix([6,2,0])", "Matrix([1,2,3])",
          r"$L_2\leftarrow L_2-L_1$ : $-2y=-4$, $y=2$. $L_3\leftarrow L_3-L_1$ : $-2z=-6$, $z=3$. Puis $x=6-2-3=1$."),
        o("as3", r"Résoudre $\begin{cases}x+y=1\\2x+2y=3\end{cases}$", r"$L_2\leftarrow L_2-2L_1$ : $0=1$. Le système n'a pas de solution.", duree=2),
        o("as4", r"Résoudre $\begin{cases}x+y+z=1\\x-y=0\end{cases}$",
          r"$y=x$ puis $z=1-2x$ : une infinité de solutions, $\{(t,\ t,\ 1-2t),\ t\in\mathbb R\}$.", duree=3),
    ]},
    {"n": 8, "titre": "Inverse d'une matrice", "notions": ["inverse", "systeme"], "exos": [
        v("av1", r"Calculer l'inverse de $" + pm([[2, 1], [5, 3]]) + r"$.", "Matrix([[2,1],[5,3]]).inv()", "Matrix([[3,-1],[-5,2]])",
          r"$ad-bc=6-5=1$ : $A^{-1}=" + pm([[3, -1], [-5, 2]]) + r"$.", duree=2),
        v("av2", r"Calculer l'inverse de $" + pm([[1, 2], [3, 4]]) + r"$.", "Matrix([[1,2],[3,4]]).inv()", "Matrix([[-2,1],[Rational(3,2),Rational(-1,2)]])",
          r"$ad-bc=4-6=-2$ : $A^{-1}=-\frac12" + pm([[4, -2], [-3, 1]]) + r"=\begin{pmatrix}-2&1\\\frac32&-\frac12\end{pmatrix}$.", duree=3),
        o("av3", r"La matrice $" + pm([[1, 2], [2, 4]]) + r"$ est-elle inversible ?",
          r"Non : $ad-bc=4-4=0$ (les colonnes sont colinéaires, le rang vaut $1$).", duree=2),
        v("av4", r"Soit $A=" + pm(_A3) + r"$. On admet que $A$ est inversible. Trouver $A^{-1}$ en détaillant les calculs, et expliquer comment vérifier le résultat.",
          f"Matrix({_A3}).inv()", f"Matrix({_A3I})",
          r"$AU=V$ avec $U=(x,y,z)$, $V=(X,Y,Z)$. $L_2\leftarrow L_2-L_1$, $L_3\leftarrow L_3+3L_1$ : $y+4z=Y-X$, $-y-5z=Z+3X$. $L_3\leftarrow L_3+L_2$ : $-z=2X+Y+Z$. En remontant : $z=-2X-Y-Z$, $y=7X+5Y+4Z$, $x=-7X-7Y-5Z$. $A^{-1}=" + pm(_A3I) + r"$. Vérification : calculer $AA^{-1}$ et trouver $I_3$.",
          src=f"{F30}, ex. 1.3", duree=10),
        v("av5", r"Calculer l'inverse de $" + pm([[1, 1, 0], [0, 1, 1], [0, 0, 1]]) + r"$.", "Matrix([[1,1,0],[0,1,1],[0,0,1]]).inv()", "Matrix([[1,-1,1],[0,1,-1],[0,0,1]])",
          r"$x+y=X$, $y+z=Y$, $z=Z$ : $z=Z$, $y=Y-Z$, $x=X-Y+Z$. $A^{-1}=" + pm([[1, -1, 1], [0, 1, -1], [0, 0, 1]]) + r"$."),
    ]},
    {"n": 9, "titre": "Changement de base", "notions": ["changement", "matrice"], "exos": [
        v("ab1", r"Dans $\mathbb R^2$, nouvelle base $\mathcal B'=((1,1),(1,-1))$. Donner les coordonnées $X'$ dans $\mathcal B'$ du vecteur de coordonnées $X=(3,1)$ dans la base canonique.",
          "Matrix([[1,1],[1,-1]]).inv()*Matrix([3,1])", "Matrix([2,1])", r"$P=" + pm([[1, 1], [1, -1]]) + r"$, $X=PX'$ : $a+b=3$, $a-b=1$, donc $X'=(2,1)$.", duree=3),
        v("ab2", r"$A=" + pm([[2, 1], [1, 2]]) + r"$ est la matrice de $f$ dans la base canonique. Donner la matrice de $f$ dans la base $\mathcal B'=((1,1),(1,-1))$.",
          "Matrix([[1,1],[1,-1]]).inv()*Matrix([[2,1],[1,2]])*Matrix([[1,1],[1,-1]])", "Matrix([[3,0],[0,1]])",
          r"$f(1,1)=(3,3)=3(1,1)$ et $f(1,-1)=(1,-1)$ : $P^{-1}AP=" + pm([[3, 0], [0, 1]]) + r"$."),
        v("ab3", r"$f(x,y)=(2x-3y,\ -2x+y)$, $\mathcal B$ base canonique, $\mathcal B'=(\varepsilon_1=(2,1),\ \varepsilon_2=(1,1))$. Écrire la matrice de $f$ avec $\mathcal B'$ au départ et $\mathcal B$ à l'arrivée.",
          "Matrix([[2,-3],[-2,1]])*Matrix([[2,1],[1,1]])", "Matrix([[1,-1],[-3,-1]])",
          r"$f(\varepsilon_1)=(1,-3)$, $f(\varepsilon_2)=(-1,-1)$, en colonnes : $" + pm([[1, -1], [-3, -1]]) + r"$.", src=f"{F30}, ex. 3.1 (b)"),
        v("ab4", r"$f(x,y)=(2x-3y,\ -2x+y)$, $\mathcal B$ base canonique, $\mathcal B'=(\varepsilon_1=(2,1),\ \varepsilon_2=(1,1))$. Écrire la matrice de $f$ avec $\mathcal B$ au départ et $\mathcal B'$ à l'arrivée.",
          "Matrix([[2,1],[1,1]]).inv()*Matrix([[2,-3],[-2,1]])", "Matrix([[4,-4],[-6,5]])",
          r"$f(e_1)=(2,-2)=4\varepsilon_1-6\varepsilon_2$ et $f(e_2)=(-3,1)=-4\varepsilon_1+5\varepsilon_2$ : $" + pm([[4, -4], [-6, 5]]) + r"$.", src=f"{F30}, ex. 3.1 (c)", duree=6),
        o("ab5", r"$\mathcal B=(u_1=(1,2),\ u_2=(-1,-1))$ base de $\mathbb R^2$, $\mathcal B'=(P_1=2,\ P_2=X-1,\ P_3=(X+1)^2)$ base de $\mathbb R_2[X]$. $f$ a pour matrice $A=" + pm([[1, 2], [-1, -4], [0, -2]]) + r"$ ($\mathcal B$ au départ, $\mathcal B'$ à l'arrivée). Pour $u=(0,1)$, trouver $(a,b,c)$ tel que $f(u)=aX^2+bX+c$.",
          r"$u=(0,1)=u_1+u_2$ : $U=" + pm([[1], [1]]) + r"$, $AU=" + pm([[3], [-5], [-2]]) + r"$. $f(u)=3P_1-5P_2-2P_3=6-5(X-1)-2(X+1)^2=-2X^2-9X+9$. $a=-2$, $b=-9$, $c=9$.", src=f"{F30}, ex. 3.2", duree=7),
        v("ab6", r"$A=" + pm([[2, 1], [1, 2]]) + r"=PDP^{-1}$ avec $P=" + pm([[1, 1], [1, -1]]) + r"$ et $D=\mathrm{diag}(3,1)$. Calculer $A^3$.",
          "Matrix([[2,1],[1,2]])**3", "Matrix([[14,13],[13,14]])",
          r"$A^3=PD^3P^{-1}$ avec $D^3=\mathrm{diag}(27,1)$ et $P^{-1}=\frac12" + pm([[1, 1], [1, -1]]) + r"$ : $A^3=\frac12" + pm([[28, 26], [26, 28]]) + "=" + pm([[14, 13], [13, 14]]) + r"$.", duree=6),
    ]},
    {"n": 10, "titre": "Projecteurs et symétries", "notions": ["projecteur"], "exos": [
        o("aj1", r"$p(x,y)=(x,0)$. Montrer que $p$ est un projecteur et donner $\mathrm{Ker}p$ et $\mathrm{Im}p$.",
          r"$p(p(x,y))=p(x,0)=(x,0)$ : $p\circ p=p$. $\mathrm{Ker}p=\{(0,y)\}=\mathrm{Vect}(e_2)$, $\mathrm{Im}p=\mathrm{Vect}(e_1)$.", duree=3),
        v("aj2", r"$p(x,y)=\left(\dfrac{4x+2y}5,\ \dfrac{2x+y}5\right)$ a pour matrice $M=\frac15" + pm([[4, 2], [2, 1]]) + r"$. Calculer $M^2$. Qu'en déduit-on ?",
          "(Matrix([[4,2],[2,1]])/5)**2", "Matrix([[4,2],[2,1]])/5",
          r"$M^2=\frac1{25}" + pm([[20, 10], [10, 5]]) + r"=M$ : $p\circ p=p$, $p$ est un projecteur.", duree=4),
        o("aj3", r"Dans $\mathbb R^2$, $F=\mathrm{Vect}(\varepsilon_1)$, $G=\mathrm{Vect}(\varepsilon_2)$ avec $\varepsilon_1=(2,1)$, $\varepsilon_2=(-1,2)$. 1. Montrer que $F\cap G=\{0\}$. 2. Pour $u=(x,y)$, montrer que $v=\left(\frac{2y+4x}5,\frac{y+2x}5\right)\in F$ et $w=\left(\frac{-2y+x}5,\frac{4y-2x}5\right)\in G$. 3. En déduire $E=F\oplus G$.",
          r"1. $u\in F\cap G$ : $u=(2\alpha,\alpha)=(-\beta,2\beta)$, d'où $\alpha=2\beta$ et $2\alpha=-\beta$, soit $\alpha=\beta=0$. 2. $v=\frac{y+2x}5(2,1)\in F$ et $w=\frac{2y-x}5(-1,2)\in G$. 3. $v+w=(x,y)=u$ donc $E=F+G$, et $F\cap G=\{0\}$ : $E=F\oplus G$.", src=f"{F30}, ex. 4.1 à 4.3", duree=7),
        o("aj4", r"Avec $\varepsilon_1=(2,1)$, $\varepsilon_2=(-1,2)$, $\mathcal B=(\varepsilon_1,\varepsilon_2)$ et $p$ la projection sur $F=\mathrm{Vect}(\varepsilon_1)$ parallèlement à $G=\mathrm{Vect}(\varepsilon_2)$ : 1. donner $p(u)$ pour $u=(3,4)$ dans la base canonique et dans $\mathcal B$ ; 2. $p(\varepsilon_1)$ et $p(\varepsilon_2)$ ; 3. la matrice de $p$ dans $\mathcal B$ ; 4. l'expression de $p(x,y)$.",
          r"1. $u=2\varepsilon_1+\varepsilon_2$, donc $p(u)=2\varepsilon_1=(4,2)$ : coordonnées $(2,0)$ dans $\mathcal B$. 2. $p(\varepsilon_1)=\varepsilon_1$, $p(\varepsilon_2)=0$. 3. $" + pm([[1, 0], [0, 0]]) + r"$. 4. $p(x,y)=v=\left(\frac{2y+4x}5,\frac{y+2x}5\right)$.", src=f"{F30}, ex. 4.4", duree=7),
        o("aj5", r"Soit $p$ un projecteur de $E$ et $s=2p-id$. Montrer que $s\circ s=id$.",
          r"$s\circ s=(2p-id)\circ(2p-id)=4p\circ p-4p+id=4p-4p+id=id$.", duree=3),
        o("aj6", r"Soit $p$ un projecteur de $E$. Montrer que $E=\mathrm{Ker}p\oplus\mathrm{Im}p$.",
          r"Si $x\in\mathrm{Ker}p\cap\mathrm{Im}p$ : $x=p(y)$ et $0=p(x)=p(p(y))=p(y)=x$. Tout $x$ s'écrit $x=(x-p(x))+p(x)$ avec $p(x-p(x))=p(x)-p(x)=0$, donc $x-p(x)\in\mathrm{Ker}p$, et $p(x)\in\mathrm{Im}p$.", duree=6),
    ]},
    {"n": 11, "titre": "Niveau examen : annale complète", "notions": ["produit", "inverse", "rang", "changement", "projecteur"], "examen": True, "exos": [
        {"id": "ax1", "kind": "multi", "src": f"{F30}, ex. 1 (8 points)",
         "enonce": r"1. $A=" + pm([[-2, 1, 2], [-1, 3, -1]]) + r"$, $B=" + pm([[2, 1], [1, -2]]) + r"$ : $AB$ et $BA$ sont-ils définis ? Effectuer le produit défini." "\n"
                   r"2. $A=" + pm([[-3, 7, -1], [-1, 2, 0]]) + r"$, $B=" + pm([[-2, 5], [-1, 3], [-2, 6]]) + r"$ : calculer $AB$. $A$ est-elle inversible ?" "\n"
                   r"3. $A=" + pm(_A3) + r"$ : trouver $A^{-1}$ en détaillant, et expliquer comment vérifier.",
         "parts": ["ap2", "ap7", "av4"]},
        {"id": "ax2", "kind": "multi", "src": f"{F30}, ex. 2 (10 points)",
         "enonce": r"$f:\mathbb R^3\to\mathbb R_2[X]$, $(a,b,c)\mapsto(a-b)X^2+(a+b-c)X-2a+2b$." "\n"
                   r"1. Dimension du noyau de $f$, avec une base." "\n"
                   r"2. Énoncer le théorème du rang. En déduire la dimension de l'image." "\n"
                   r"3. Trouver une base de $\mathrm{Im}f$.",
         "parts": ["an2", "at0", "ai4"]},
        {"id": "ax3", "kind": "multi", "src": f"{F30}, ex. 3 (7 points)",
         "enonce": r"1. $f(x,y)=(2x-3y,-2x+y)$, $\mathcal B$ canonique, $\mathcal B'=(\varepsilon_1=(2,1),\varepsilon_2=(1,1))$. Matrice de $f$ : (a) dans $\mathcal B$ ; (b) $\mathcal B'$ au départ, $\mathcal B$ à l'arrivée ; (c) $\mathcal B$ au départ, $\mathcal B'$ à l'arrivée." "\n"
                   r"2. $\mathcal B=((1,2),(-1,-1))$, $\mathcal B'=(2,\ X-1,\ (X+1)^2)$, $A=" + pm([[1, 2], [-1, -4], [0, -2]]) + r"$, $u=(0,1)$ : trouver $f(u)=aX^2+bX+c$.",
         "parts": ["am1", "ab3", "ab4", "ab5"]},
        {"id": "ax4", "kind": "multi", "src": f"{F30}, ex. 4 et 5 (15 points)",
         "enonce": r"1. $F=\mathrm{Vect}(\varepsilon_1=(2,1))$, $G=\mathrm{Vect}(\varepsilon_2=(-1,2))$ : $F\cap G=\{0\}$ ; $v=\left(\frac{2y+4x}5,\frac{y+2x}5\right)\in F$, $w=\left(\frac{-2y+x}5,\frac{4y-2x}5\right)\in G$ ; $E=F\oplus G$." "\n"
                   r"2. $p$ projection sur $F$ parallèlement à $G$ : $p(3,4)$ dans la base canonique et dans $\mathcal B=(\varepsilon_1,\varepsilon_2)$ ; $p(\varepsilon_1)$, $p(\varepsilon_2)$ ; matrice de $p$ dans $\mathcal B$ ; expression de $p(x,y)$." "\n"
                   r"3. $A=" + pm([[1, 2, -1], [-2, 1, 2], [1, 0, -1]]) + r"$ (bases canoniques de $\mathbb R^3$ et $\mathbb R_2[X]$) : rang, base de l'image, base du noyau, en raisonnant sur les colonnes.",
         "parts": ["aj3", "aj4", "ai6"]},
    ]},
    {"n": 12, "titre": "Examen + 20 %", "notions": ["noyau", "image", "produit"], "examen": True, "exos": [
        o("ay1", r"Soit $f$ un endomorphisme de $E$ de dimension finie $n$. Montrer que $f\circ f=0\iff\mathrm{Im}f\subset\mathrm{Ker}f$, et qu'alors $\mathrm{rg}f\le\frac n2$.",
          r"Si $f\circ f=0$ et $y=f(x)\in\mathrm{Im}f$ : $f(y)=f(f(x))=0$, donc $y\in\mathrm{Ker}f$. Réciproquement, si $\mathrm{Im}f\subset\mathrm{Ker}f$ : $f(x)\in\mathrm{Ker}f$, donc $f(f(x))=0$ pour tout $x$. Alors $\mathrm{rg}f\le\dim\mathrm{Ker}f=n-\mathrm{rg}f$, d'où $\mathrm{rg}f\le\frac n2$.", duree=10),
        v("ay2", r"$A=" + pm([[1, 1, 0], [0, 1, 1], [0, 0, 1]]) + r"=I+N$. Calculer $N^2$, $N^3$, puis $A^5$ avec la formule du binôme.",
          "Matrix([[1,1,0],[0,1,1],[0,0,1]])**5", "Matrix([[1,5,10],[0,1,5],[0,0,1]])",
          r"$N=" + pm([[0, 1, 0], [0, 0, 1], [0, 0, 0]]) + r"$, $N^2=" + pm([[0, 0, 1], [0, 0, 0], [0, 0, 0]]) + r"$, $N^3=0$. $I$ et $N$ commutent : $A^5=I+5N+\binom52N^2=" + pm([[1, 5, 10], [0, 1, 5], [0, 0, 1]]) + r"$.", duree=10),
        o("ay3", r"Soit $f$ un endomorphisme de $E$. Montrer que $\mathrm{Ker}f\subset\mathrm{Ker}f^2$ et $\mathrm{Im}f^2\subset\mathrm{Im}f$.",
          r"Si $x\in\mathrm{Ker}f$ : $f^2(x)=f(f(x))=f(0)=0$, donc $x\in\mathrm{Ker}f^2$. Si $y\in\mathrm{Im}f^2$ : $y=f^2(x)=f(f(x))\in\mathrm{Im}f$.", duree=6),
    ]},
    {"n": 13, "titre": "Examens 2028 et 2029", "notions": ["inverse", "noyau", "rang", "matrice", "changement", "projecteur"], "examen": True, "exos": [
        v("aw1", r"Inverse de $A=" + pm([[2, 1, 1], [2, -1, 2], [-1, 1, -1]]) + r"$ : donner le coefficient en ligne 3, colonne 3 de $A^{-1}$.", "Matrix([[2,1,1],[2,-1,2],[-1,1,-1]]).inv()[2,2]", "4",
          r"Pivot de Gauss : $A^{-1}=" + pm([[1, -2, -3], [0, 1, 2], [-1, 3, 4]]) + r"$.", src="Examen S2-B4 ALM juin 2024, ex. 1", duree=8),
        v("aw2", r"$f:\mathbb R_2[X]\to\mathbb R^2$, $P\mapsto(P(0),P'(-1))$. Quelle est la dimension de $\mathrm{Ker}f$ ?", "3-Matrix([[1,0,0],[0,1,-2]]).rank()", "1",
          r"Matrice $" + pm([[1, 0, 0], [0, 1, -2]]) + r"$. $\mathrm{Ker}f=\mathrm{Vect}(2X+X^2)$, dimension $1$ (rang $2$, théorème du rang).", src="Examen S2-B4 ALM juin 2024, ex. 2", duree=6),
        o("aw3", r"$f:\mathbb R_2[X]\to\mathbb R^2$ vérifie $\mathrm{Ker}f=\mathrm{Vect}(X+1)$. 1. $\dim\mathrm{Im}f$ ? 2. $f$ injective ? surjective ? Énoncer le théorème du rang.",
          r"Théorème du rang : $f\in\mathcal L(E,F)$, $E$ de dimension finie : $\dim E=\dim\mathrm{Ker}f+\dim\mathrm{Im}f$. 1. $3-1=2$. 2. Non injective ($\mathrm{Ker}f\ne\{0\}$). Surjective : $\mathrm{Im}f\subset\mathbb R^2$ et $\dim\mathrm{Im}f=2$, donc $\mathrm{Im}f=\mathbb R^2$.",
          src="Examen S2-B4 ALM mai 2025, ex. 2", duree=8),
        o("aw4", r"$f:\mathbb R^2\to\mathbb R_1[X]$, $(a,b)\mapsto(-3a+5b)X-4a+6b$. 1. Matrice dans les bases canoniques. 2. Matrice dans $\mathcal B_1=((1,1),(2,1))$ et $\mathcal B_2=(X+1,X+2)$.",
          r"1. $f(1,0)=-3X-4$, $f(0,1)=5X+6$ : $A=" + pm([[-4, 6], [-3, 5]]) + r"$." "\n\n"
          r"2. $f(1,1)=2X+2=2(X+1)$ et $f(2,1)=-X-2=-(X+2)$ : matrice $" + pm([[2, 0], [0, -1]]) + r"$.",
          src="Examen S2-B4 ALM juin 2024, ex. 3", duree=10),
        o("aw5", r"$p:\mathbb R^2\to\mathbb R^2$, $(x,y)\mapsto(0,x+y)$. 1. Vérifier $p\circ p=p$. 2. $\mathrm{Ker}p=\mathrm{Vect}(1,-1)$ et $\mathrm{Im}p=\mathrm{Vect}(0,1)$ : montrer que $\mathbb R^2=\mathrm{Ker}p\oplus\mathrm{Im}p$. 3. $p(-1,-2)$ ? 4. Matrice de $p$ dans $((1,-1),(0,1))$.",
          r"1. $p(p(x,y))=p(0,x+y)=(0,x+y)=p(x,y)$." "\n\n"
          r"2. $\mathrm{Ker}p\cap\mathrm{Im}p=\{0\}$ (droites distinctes) et $\dim=1+1-0=2$." "\n\n"
          r"3. $(-1,-2)=(-1,1)+(0,-3)$ avec $(-1,1)\in\mathrm{Ker}p$ : $p(-1,-2)=(0,-3)$." "\n\n"
          r"4. $p(1,-1)=0$, $p(0,1)=(0,1)$ : $" + pm([[0, 0], [0, 1]]) + r"$.",
          src="Examen S2-B4 ALM juin 2024, ex. 4", duree=12),
        v("aw6", r"$\mathcal B'=((2,0,0),(-3,1,0),(16,8,1))$, $u=2u_1+3u_2-4u_3$. Quelles sont les coordonnées de $u$ dans la base canonique ?", "Matrix([[2,-3,16],[0,1,8],[0,0,1]])*Matrix([2,3,-4])", "Matrix([-69,-29,-4])",
          r"$X=PX'$ avec $P=" + pm([[2, -3, 16], [0, 1, 8], [0, 0, 1]]) + r"$ et $X'=(2,3,-4)^T$ : $X=(-69,-29,-4)^T$.", src="Examen S2-B4 ALM juin 2024, ex. 5", duree=6),
        v("aw7", r"$p$ projection de $\mathbb R^2$ sur $F=\mathrm{Vect}(2,1)$ parallèlement à $G=\mathrm{Vect}(-2,4)$. Calculer $p(3,4)$.", "2*Matrix([2,1])", "Matrix([4,2])",
          r"$(3,4)=2(2,1)+\frac12(-2,4)$ : $p(3,4)=2(2,1)$, soit $(4,2)$.", src="Examen S2-B4 ALM mai 2025, ex. 4", duree=6),
    ]},
]


# Variants (same method, other numbers): a failed exercise comes back with the next one; build.py checks calc == ans.
def _v(enonce, calc, ans, sol):
    return {"enonce": enonce, "calc": calc, "ans": ans, "sol": sol}


VARIANTS = {
    "al5": [_v(r"$f:\mathbb R^2\to\mathbb R^2$ est linéaire, $f(e_1)=(2,1)$ et $f(e_2)=(1,-1)$. Calculer $f(2,3)$.", "2*Matrix([2,1])+3*Matrix([1,-1])", "Matrix([7,-1])",
               r"$2f(e_1)+3f(e_2)=(4,2)+(3,-3)=(7,-1)$.")],
    "an4": [_v(r"$f:\mathbb R^3\to\mathbb R^2$ a pour matrice $" + pm([[1, 0, 1], [0, 1, 1]]) + r"$. Quelle est la dimension de $\mathrm{Ker}f$ ?", "3-Matrix([[1,0,1],[0,1,1]]).rank()", "1",
               r"$x=-z$, $y=-z$ : $\mathrm{Vect}((-1,-1,1))$, dimension $1$.")],
    "ai2": [_v(r"Quel est le rang de $" + pm([[1, 2], [3, 4]]) + r"$ ?", "Matrix([[1,2],[3,4]]).rank()", "2", r"Les colonnes ne sont pas colinéaires : rang $2$.")],
    "ai3": [_v(r"Quel est le rang de $" + pm([[1, 2, 3], [2, 4, 6], [1, 1, 1]]) + r"$ ?", "Matrix([[1,2,3],[2,4,6],[1,1,1]]).rank()", "2",
               r"$L_2=2L_1$, et $L_1$, $L_3$ ne sont pas colinéaires : rang $2$.")],
    "at1": [_v(r"$f:\mathbb R^4\to\mathbb R^2$ est linéaire et surjective. Quelle est la dimension de $\mathrm{Ker}f$ ?", "4-2", "2", r"$4-2=2$.")],
    "at2": [_v(r"$f$ est un endomorphisme de $\mathbb R^5$ et $\dim\mathrm{Ker}f=2$. Quel est le rang de $f$ ?", "5-2", "3", r"$5-2=3$.")],
    "am3": [_v(r"$f$ a pour matrice $A=" + pm([[2, -1], [1, 3]]) + r"$ dans la base canonique. Calculer $f(1,2)$.", "Matrix([[2,-1],[1,3]])*Matrix([1,2])", "Matrix([0,7])",
               r"$(2-2,\ 1+6)=(0,7)$.")],
    "ap1": [_v(r"Calculer $" + pm([[1, 2], [3, 4]]) + pm([[1, 1], [0, 1]]) + r"$.", "Matrix([[1,2],[3,4]])*Matrix([[1,1],[0,1]])", "Matrix([[1,3],[3,7]])",
               r"$" + pm([[1, 3], [3, 7]]) + r"$.")],
    "ap3": [_v(r"$A=" + pm([[2, 0], [1, 1]]) + r"$. Calculer $A^2$.", "Matrix([[2,0],[1,1]])**2", "Matrix([[4,0],[3,1]])", r"$A^2=" + pm([[4, 0], [3, 1]]) + r"$.")],
    "ap5": [_v(r"$A=" + pm([[1, 0], [2, 1]]) + r"$. Calculer ${}^tA\,A$.", "Matrix([[1,0],[2,1]]).T*Matrix([[1,0],[2,1]])", "Matrix([[5,2],[2,1]])",
               r"${}^tA=" + pm([[1, 2], [0, 1]]) + r"$, ${}^tA\,A=" + pm([[5, 2], [2, 1]]) + r"$.")],
    "ap6": [_v(r"$U=" + pm([[2], [-1], [2]]) + r"$. Calculer ${}^tU\,U$.", "(Matrix([2,-1,2]).T*Matrix([2,-1,2]))[0]", "9", r"$4+1+4=9$.")],
    "as1": [_v(r"Résoudre $\begin{cases}2x+y=4\\x-y=5\end{cases}$", "Matrix([[2,1],[1,-1]]).inv()*Matrix([4,5])", "Matrix([3,-2])",
               r"$L_1+L_2$ : $3x=9$, $x=3$, puis $y=x-5=-2$.")],
    "as2": [_v(r"Résoudre $\begin{cases}x+y+z=3\\x-y+z=1\\x+y-z=1\end{cases}$", "Matrix([[1,1,1],[1,-1,1],[1,1,-1]]).inv()*Matrix([3,1,1])", "Matrix([1,1,1])",
               r"$L_2\leftarrow L_2-L_1$ : $-2y=-2$, $y=1$. $L_3\leftarrow L_3-L_1$ : $-2z=-2$, $z=1$. Puis $x=1$.")],
    "av1": [_v(r"Calculer l'inverse de $" + pm([[3, 2], [1, 1]]) + r"$.", "Matrix([[3,2],[1,1]]).inv()", "Matrix([[1,-2],[-1,3]])",
               r"$ad-bc=1$ : $" + pm([[1, -2], [-1, 3]]) + r"$.")],
    "av2": [_v(r"Calculer l'inverse de $" + pm([[1, 1], [1, 3]]) + r"$.", "Matrix([[1,1],[1,3]]).inv()", "Matrix([[3,-1],[-1,1]])/2",
               r"$ad-bc=2$ : $\frac12" + pm([[3, -1], [-1, 1]]) + r"$.")],
    "av5": [_v(r"Calculer l'inverse de $" + pm([[1, 2, 0], [0, 1, 0], [0, 0, 2]]) + r"$.", "Matrix([[1,2,0],[0,1,0],[0,0,2]]).inv()", "Matrix([[1,-2,0],[0,1,0],[0,0,Rational(1,2)]])",
               r"$x+2y=X$, $y=Y$, $2z=Z$ : $x=X-2Y$, $y=Y$, $z=\frac Z2$. $A^{-1}=\begin{pmatrix}1&-2&0\\0&1&0\\0&0&\frac12\end{pmatrix}$.")],
    "ab1": [_v(r"Dans $\mathbb R^2$, nouvelle base $\mathcal B'=((1,1),(1,-1))$. Donner les coordonnées dans $\mathcal B'$ du vecteur de coordonnées $(4,-2)$ dans la base canonique.",
               "Matrix([[1,1],[1,-1]]).inv()*Matrix([4,-2])", "Matrix([1,3])", r"$a+b=4$, $a-b=-2$ : $X'=(1,3)$.")],
    "ab2": [_v(r"$A=" + pm([[1, 2], [2, 1]]) + r"$ est la matrice de $f$ dans la base canonique. Donner la matrice de $f$ dans la base $\mathcal B'=((1,1),(1,-1))$.",
               "Matrix([[1,1],[1,-1]]).inv()*Matrix([[1,2],[2,1]])*Matrix([[1,1],[1,-1]])", "Matrix([[3,0],[0,-1]])",
               r"$f(1,1)=(3,3)$ et $f(1,-1)=(-1,1)=-(1,-1)$ : $" + pm([[3, 0], [0, -1]]) + r"$.")],
    "ab6": [_v(r"$A=" + pm([[1, 2], [2, 1]]) + r"=PDP^{-1}$ avec $P=" + pm([[1, 1], [1, -1]]) + r"$ et $D=\mathrm{diag}(3,-1)$. Calculer $A^3$.",
               "Matrix([[1,2],[2,1]])**3", "Matrix([[13,14],[14,13]])",
               r"$D^3=\mathrm{diag}(27,-1)$ : $A^3=\frac12" + pm([[26, 28], [28, 26]]) + "=" + pm([[13, 14], [14, 13]]) + r"$.")],
}
for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["id"] in VARIANTS:
            _e["variants"] = VARIANTS[_e["id"]]


EXTRA_PARTS = []

QUIZ = [
    {"notion": "lineaire", "type": "vf", "q": r"Si $f$ est linéaire alors $f(0)=0$.", "bonne": True},
    {"notion": "lineaire", "type": "vf", "q": r"Si $f(0)=0$ alors $f$ est linéaire.", "bonne": False},
    {"notion": "noyau", "type": "qcm", "q": r"$f$ linéaire est injective si et seulement si :",
     "choix": [r"$\mathrm{Ker}f=\{0_E\}$", r"$\mathrm{Im}f=F$", r"$\mathrm{Ker}f=E$", r"$f(0)=0$"], "bonne": 0},
    {"notion": "image", "type": "qcm", "q": r"$\mathrm{Im}f$ est engendrée par :",
     "choix": [r"les images des vecteurs d'une base de $E$", r"les vecteurs d'une base de $E$", r"les vecteurs du noyau", r"les lignes de la matrice"], "bonne": 0},
    {"notion": "rang", "type": "qcm", "q": r"Théorème du rang pour $f\in\mathcal L(E,F)$ :",
     "choix": [r"$\dim E=\dim\mathrm{Ker}f+\mathrm{rg}f$", r"$\dim F=\dim\mathrm{Ker}f+\mathrm{rg}f$", r"$\dim E=\dim F+\mathrm{rg}f$", r"$\mathrm{rg}f=\dim E+\dim\mathrm{Ker}f$"], "bonne": 0},
    {"notion": "rang", "type": "vf", "q": r"Une application linéaire de $\mathbb R^3$ dans $\mathbb R^2$ n'est jamais injective.", "bonne": True},
    {"notion": "matrice", "type": "qcm", "q": r"La colonne $j$ de la matrice de $f$ contient :",
     "choix": [r"les coordonnées de $f(e_j)$ dans la base d'arrivée", r"les coordonnées de $e_j$", r"les antécédents de $e_j$", r"la ligne $j$ du système"], "bonne": 0},
    {"notion": "produit", "type": "vf", "q": r"Pour toutes matrices carrées $A$, $B$ de même taille, $AB=BA$.", "bonne": False},
    {"notion": "produit", "type": "qcm", "q": r"$A$ est de taille $2\times3$ et $B$ de taille $3\times4$. $AB$ est de taille :",
     "choix": [r"$2\times4$", r"$3\times3$", r"$4\times2$", r"non défini"], "bonne": 0},
    {"notion": "systeme", "type": "vf", "q": r"Si le pivot de Gauss donne une ligne $0=1$, le système n'a pas de solution.", "bonne": True},
    {"notion": "inverse", "type": "qcm", "q": r"$\begin{pmatrix}a&b\\c&d\end{pmatrix}$ est inversible si et seulement si :",
     "choix": [r"$ad-bc\ne0$", r"$ad+bc\ne0$", r"$a\ne0$ et $d\ne0$", r"$ab-cd\ne0$"], "bonne": 0},
    {"notion": "inverse", "type": "vf", "q": r"Une matrice non carrée peut être inversible.", "bonne": False},
    {"notion": "changement", "type": "qcm", "q": r"Si $P$ est la matrice de passage de $\mathcal B$ à $\mathcal B'$ et $A=\mathrm{Mat}_{\mathcal B}(f)$, alors $\mathrm{Mat}_{\mathcal B'}(f)=$",
     "choix": [r"$P^{-1}AP$", r"$PAP^{-1}$", r"$AP$", r"$P^{-1}A$"], "bonne": 0},
    {"notion": "projecteur", "type": "qcm", "q": r"$p$ est un projecteur si et seulement si :", "choix": [r"$p\circ p=p$", r"$p\circ p=id$", r"$p\circ p=0$", r"$p$ est bijective"], "bonne": 0},
]

_LIN = r"$f$ linéaire $\iff f(\lambda u+v)=\lambda f(u)+f(v)$"
_NL = r"$f$ linéaire $\Rightarrow f(0)=0$ et $f(2u)=2f(u)$ (conditions nécessaires)"
_BASEIM = r"$u=\sum x_ie_i\Rightarrow f(u)=\sum x_if(e_i)$"
_KER = r"$\mathrm{Ker}f$ : résoudre $f(u)=0$"
_INJ = r"injective $\iff\mathrm{Ker}f=\{0\}$"
_IM = r"$\mathrm{Im}f=\mathrm{Vect}(f(e_1),\dots,f(e_n))$"
_RG = r"théorème du rang : $\dim E=\dim\mathrm{Ker}f+\mathrm{rg}f$"
_COL = r"colonne $j$ = coordonnées de $f(e_j)$ dans la base d'arrivée"
_PROD = r"$(AB)_{ij}=\sum_ka_{ik}b_{kj}$"
_DEF = r"$AB$ défini si (colonnes de $A$) = (lignes de $B$)"
_GAUSS = r"pivot de Gauss : $L_i\leftarrow L_i+\lambda L_j$, puis remontée"
_INV2 = r"$\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1}=\frac1{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$"
_PASS = r"$X=PX'$, $P$ = matrice de passage (colonnes = nouveaux vecteurs dans l'ancienne base)"
_PROJ = r"projecteur $\iff p\circ p=p$"
_SD = r"$E=F\oplus G\iff F\cap G=\{0\}$ et $E=F+G$"
FORMULES = {
    "al1": _LIN, "al2": _NL, "al3": _NL, "al4": _LIN + r" · $(\lambda P+Q)'=\lambda P'+Q'$", "al5": _BASEIM,
    "al6": _BASEIM + r" · si les vecteurs donnés sont liés, les images doivent vérifier la même relation",
    "an1": _KER, "an2": _KER + r" · un polynôme est nul $\iff$ tous ses coefficients sont nuls · un vecteur non nul forme une base de la droite qu'il engendre",
    "an3": _KER + " · " + _INJ, "an4": _RG + r" · rang = nombre de lignes indépendantes", "an5": _KER + " · " + _INJ + r" · $P'=0\iff P$ constant",
    "an6": _INJ + r" · $f(x)-f(y)=f(x-y)$ · $f(0)=0$",
    "ai1": _IM, "ai2": r"rang = nombre de colonnes indépendantes", "ai3": r"rang = nombre de colonnes indépendantes",
    "ai4": _IM + r" · famille génératrice de cardinal $\dim$ = base", "ai5": _IM + r" · surjective $\iff\mathrm{rg}f=\dim F$",
    "ai6": r"$\mathrm{Im}f$ = Vect des colonnes · " + _RG + r" · une relation entre colonnes donne un vecteur du noyau",
    "at0": _RG, "at1": _RG + r" · surjective $\iff\mathrm{rg}f=\dim F$", "at2": _RG, "at3": _RG + r" · $\mathrm{rg}f\le\dim F$ · " + _INJ,
    "at4": _RG + r" · surjective $\iff\mathrm{rg}f=\dim F$", "at5": _RG + " · " + _INJ + r" · $F\subset E$ et $\dim F=\dim E\Rightarrow F=E$",
    "am1": _COL, "am2": _COL + r" · base canonique de $\mathbb R_2[X]$ : $(1,X,X^2)$", "am3": r"coordonnées de l'image : $Y=AX$",
    "am4": r"taille $(\dim$ arrivée$)\times(\dim$ départ$)$", "am5": _COL,
    "ap1": _PROD, "ap2": _DEF + r" : $n\times p$ par $p\times q$ donne $n\times q$ · " + _PROD, "ap3": _PROD, "ap4": _PROD + r" · $AB\ne BA$ en général",
    "ap5": r"$({}^tA)_{ij}=a_{ji}$ · " + _PROD, "ap6": r"${}^tUU=\sum x_i^2$ (scalaire)", "ap7": _PROD + r" · seule une matrice carrée peut être inversible",
    "as1": _GAUSS, "as2": _GAUSS, "as3": _GAUSS + r" · $0=c\ne0$ : pas de solution", "as4": _GAUSS + r" · inconnue libre : infinité de solutions",
    "av1": _INV2, "av2": _INV2, "av3": r"$2\times2$ inversible $\iff ad-bc\ne0$", "av4": r"résoudre $AU=V$ par pivot de Gauss : $U=A^{-1}V$ · vérifier $AA^{-1}=I_n$",
    "av5": r"résoudre $AU=V$ par remontée : $U=A^{-1}V$",
    "ab1": _PASS + r" · $X'=P^{-1}X$", "ab2": r"$\mathrm{Mat}_{\mathcal B'}(f)=P^{-1}AP$ · $f(u_i)=\lambda_iu_i\Rightarrow D=\mathrm{diag}(\lambda_i)$", "ab3": _COL,
    "ab4": _COL + r" · exprimer $f(e_j)$ dans $\mathcal B'$ : résoudre $f(e_j)=a\varepsilon_1+b\varepsilon_2$", "ab5": r"coordonnées de $u$ dans $\mathcal B$ · $Y=AX$ · $f(u)=\sum y_iP_i$",
    "ab6": r"$A=PDP^{-1}\Rightarrow A^n=PD^nP^{-1}$ · $D^n=\mathrm{diag}(\lambda_i^n)$ · " + _INV2,
    "aj1": _PROJ + " · " + _KER, "aj2": _PROJ + " · " + _PROD, "aj3": _SD + r" · $u\in\mathrm{Vect}(\varepsilon)\iff u=\lambda\varepsilon$",
    "aj4": r"projection sur $F$ parallèlement à $G$ : $u=v+w\mapsto v$ · " + _COL + r" · matrice dans une base adaptée : $\mathrm{diag}(1,0)$",
    "aj5": _PROJ + r" · $s=2p-id$ · $s\circ s=id$", "aj6": _PROJ + " · " + _SD + r" · $x=(x-p(x))+p(x)$",
    "aw1": _GAUSS + r" · $AA^{-1}=I$", "aw2": _KER + " · " + _RG + " · " + _COL, "aw3": _RG + " · " + _INJ + r" · $\dim\mathrm{Im}f=\dim F\Rightarrow$ surjective",
    "aw4": _COL + r" · coordonnées dans la base d'arrivée", "aw5": _PROJ + " · " + _SD + " · " + _COL,
    "aw6": _PASS, "aw7": r"projection sur $F$ parallèlement à $G$ : $u=v+w\mapsto v$ · " + _PROJ,
    "ay1": r"$\mathrm{Im}f=\{f(x)\}$ · $\mathrm{Ker}f=\{x,\ f(x)=0\}$ · " + _RG + r" · $F\subset G\Rightarrow\dim F\le\dim G$",
    "ay2": r"$N$ nilpotente : $N^3=0$ · si $AB=BA$ : $(A+B)^n=\sum_k\binom nkA^kB^{n-k}$ · $(I+N)^n=I+nN+\binom n2N^2$",
    "ay3": r"$\mathrm{Ker}f=\{x,\ f(x)=0\}$ · $\mathrm{Im}f=\{f(x)\}$ · $f(0)=0$ · $f^2(x)=f(f(x))$",
}
