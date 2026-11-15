"""Level path: S2 maths, ECUE EV (espaces vectoriels, sous-espaces, familles, bases, dimension, somme directe).

Moodle chapters 07 and 08 (S2-MATHS-2030). Calibrated on Examen S2-B3 EV mars 2026 and Examen S2-B4 EV 2026
(promo 2030), read on the official corrections, and on `annales/FORMULES.md` (« EV »).
Mostly `open` exercises (proofs); `value` exercises use sympy matrices (coordinates, rank).
"""

SUBJECT = {
    "id": "maths-s2-ev",
    "ordre": 220,
    "matiere": "maths",
    "semestre": "S2",
    "ecue": "EV",
    "titre": "Espaces vectoriels",
    "chapitres_moodle": ["07_Cours 3 - Espaces vectoriels", "08_Cours 4 - Base et dimension d'un espace vectoriel"],
    "td": "TD espaces vectoriels (S2 2030)",
    "examens": ["Examen S2-B3 EV (avant les vacances de printemps)", "Examen S2-B4 EV (avant l'été)"],
}

NOTIONS = [
    {"id": "vect", "titre": "Combinaisons linéaires et Vect",
     "formule": r"$\mathrm{Vect}(u_1,\dots,u_n)=\{\alpha_1u_1+\dots+\alpha_nu_n,\ (\alpha_1,\dots,\alpha_n)\in\mathbb R^n\}$ · $\mathrm{Vect}(\dots)$ est toujours un sev · $F\subset G$ si les générateurs de $F$ sont dans $G$",
     "exemple": r"$\{(x,y,z),\ x+y-z=0\}=\{(x,y,x+y)\}=\mathrm{Vect}((1,0,1),(0,1,1))$",
     "cours": r"Pour savoir si $u\in\mathrm{Vect}(u_1,\dots)$ : résoudre $u=\sum\alpha_iu_i$. Pour écrire un sev défini par des équations sous forme de Vect : exprimer les inconnues principales en fonction des inconnues libres, puis factoriser chaque paramètre."},
    {"id": "axiomes", "titre": "Axiomes d'un espace vectoriel",
     "formule": r"$(E,+)$ groupe commutatif · $1.u=u$ · $\alpha.(\beta.u)=(\alpha\beta).u$ · $(\alpha+\beta).u=\alpha.u+\beta.u$ · $\alpha.(u+v)=\alpha.u+\alpha.v$",
     "exemple": r"avec $\alpha*(x,y)=(\alpha x,\alpha^{-1}y)$ : $2*u+3*u\ne5*u$, ce n'est pas un ev",
     "cours": r"Pour montrer qu'une structure **n'est pas** un ev, un seul axiome en défaut suffit, avec un contre-exemple chiffré. Pour montrer qu'un ensemble **est** un ev, on montre presque toujours que c'est un sev d'un ev connu."},
    {"id": "sev", "titre": "Sous-espace vectoriel",
     "formule": r"$F$ sev de $E$ $\iff F\subset E$, $0_E\in F$ et $\forall(u,v)\in F^2,\ \forall\alpha\in\mathbb R,\ \alpha u+v\in F$",
     "exemple": r"$\{(x,y),\ x+y=1\}$ n'est pas un sev : il ne contient pas $(0,0)$",
     "cours": r"Trois points à écrire, dans l'ordre. Pour dire non : $0\notin F$, ou un contre-exemple à la stabilité. Une équation non linéaire ($z^2$, $xy$) ou une inégalité donne en général un ensemble qui n'est pas un sev."},
    {"id": "libre", "titre": "Familles libres et liées",
     "formule": r"libre : $\forall(\alpha_i),\ \sum\alpha_iu_i=0_E\Rightarrow\alpha_1=\dots=\alpha_n=0$ · liée : $\exists(\alpha_i)$ non tous nuls, $\sum\alpha_iu_i=0_E$",
     "exemple": r"$((1,2),(2,4))$ est liée : $2u_1-u_2=0$",
     "cours": r"Méthode : poser $\sum\alpha_iu_i=0$, écrire le système, le résoudre. Raccourcis : une famille contenant $0_E$ est liée ; deux vecteurs sont liés si et seulement s'ils sont colinéaires ; plus de $n$ vecteurs en dimension $n$ : liée ; polynômes de degrés échelonnés : libre."},
    {"id": "base", "titre": "Familles génératrices et bases",
     "formule": r"génératrice : $\forall u\in E,\ \exists(\alpha_i),\ u=\sum\alpha_iu_i$ · base = libre et génératrice · en dimension $n$ : $n$ vecteurs libres forment une base",
     "exemple": r"$((1,1),(1,-1))$ : deux vecteurs non colinéaires de $\mathbb R^2$, donc une base",
     "cours": r"En dimension $n$ : moins de $n$ vecteurs ne peuvent pas engendrer, plus de $n$ sont liés. Avec exactement $n$ vecteurs, il suffit de montrer libre **ou** génératrice."},
    {"id": "dimension", "titre": "Dimension",
     "formule": r"$\dim E$ = cardinal d'une base · $\dim\mathbb R^n=n$ · $\dim\mathbb R_n[X]=n+1$ · $F\subset E\Rightarrow\dim F\le\dim E$, avec égalité $\iff F=E$ · dimension d'un sev défini par des équations = nombre de paramètres libres",
     "exemple": r"le plan $x+y+z=0$ de $\mathbb R^3$ est de dimension $3-1=2$",
     "cours": r"Pour trouver la dimension : exhiber une base (famille génératrice, dont on retire les vecteurs combinaisons des autres jusqu'à ce qu'elle soit libre)."},
    {"id": "coordonnees", "titre": "Coordonnées dans une base",
     "formule": r"$u=\sum x_ie_i$ de manière unique : $(x_1,\dots,x_n)$ sont les coordonnées de $u$ dans la base $(e_i)$",
     "exemple": r"dans la base $(u_1=(3,2),u_2=(-1,2))$ : $(-5,2)=-u_1+2u_2$, coordonnées $(-1,2)$",
     "cours": r"Des coordonnées vers le vecteur : calculer la combinaison. Du vecteur vers les coordonnées : résoudre le système $u=\sum x_ie_i$ (pour des polynômes, identifier les coefficients). Base canonique de $\mathbb R_2[X]$ : $(1,X,X^2)$."},
    {"id": "somme", "titre": "Intersection et somme de sous-espaces",
     "formule": r"$F+G=\{v+w,\ v\in F,\ w\in G\}$ · $F\cap G$ et $F+G$ sont des sev, $F\cup G$ en général non · Grassmann : $\dim(F+G)=\dim F+\dim G-\dim(F\cap G)$",
     "exemple": r"deux plans distincts de $\mathbb R^3$ : $\dim(F\cap G)=2+2-3=1$, une droite",
     "cours": r"Pour $F\cap G$ : paramétrer les vecteurs de $F$, puis injecter dans les équations de $G$."},
    {"id": "supplementaire", "titre": "Somme directe, supplémentaires",
     "formule": r"$E=F\oplus G\iff F\cap G=\{0_E\}$ et $E=F+G$ $\iff F\cap G=\{0_E\}$ et $\dim F+\dim G=\dim E$ $\iff$ tout $u\in E$ s'écrit de manière unique $u=v+w$, $v\in F$, $w\in G$",
     "exemple": r"$\mathbb R^2=\mathrm{Vect}((1,1))\oplus\mathrm{Vect}((1,-2))$",
     "cours": r"En dimension finie : montrer $F\cap G=\{0\}$ puis compter les dimensions. Sans dimension (espaces de fonctions) : exhiber la décomposition, par exemple $f=\frac{f(x)+f(-x)}2+\frac{f(x)-f(-x)}2$."},
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


M30 = "Examen S2-B3 EV mars 2026"
F30 = "Examen S2-B4 EV 2026"

LEVELS = [
    {"n": 1, "titre": "Combinaisons linéaires", "notions": ["vect"], "exos": [
        v("ec1", r"$u=(1,2)$ et $v=(3,-1)$. Calculer $2u-3v$.", "2*Matrix([1,2])-3*Matrix([3,-1])", "Matrix([-7,7])",
          r"$2u-3v=(2-9,\ 4+3)=(-7,7)$.", duree=2),
        v("ec2", r"Trouver $(a,b)$ tel que $(5,1)=a(1,1)+b(1,-1)$.", "Matrix([[1,1],[1,-1]]).inv()*Matrix([5,1])", "Matrix([3,2])",
          r"$a+b=5$ et $a-b=1$ : $a=3$, $b=2$.", duree=3),
        o("ec3", r"Le vecteur $(1,2,3)$ appartient-il à $\mathrm{Vect}((1,0,1),(0,1,1))$ ?",
          r"On cherche $a(1,0,1)+b(0,1,1)=(1,2,3)$ : $a=1$, $b=2$, et $a+b=3$ est vérifié. Oui.", duree=3),
        o("ec4", r"Le polynôme $X^2+1$ appartient-il à $\mathrm{Vect}(X^2,\ X+1)$ ?",
          r"$aX^2+b(X+1)=X^2+1$ : le coefficient de $X$ donne $b=0$, le terme constant donne $b=1$. Impossible : non.", duree=3),
    ]},
    {"n": 2, "titre": "Axiomes d'un espace vectoriel", "notions": ["axiomes"], "exos": [
        o("ea1", r"Sur $\mathbb R^2$ : $u+v=(x+x',y+y')$, $\alpha*u=(\alpha x,\alpha^{-1}y)$ si $\alpha\ne0$ et $0*u=(0,0)$. Pour $u=(-1,30)$ et $v=(2,-7)$, calculer $u+v$, $1*u$, $2*u$, $3*u$, $5*u$.",
          r"$u+v=(1,23)$ ; $1*u=(-1,30)$ ; $2*u=(-2,15)$ ; $3*u=(-3,10)$ ; $5*u=(-5,6)$.", src=f"{M30}, ex. 1.2", duree=3),
        o("ea2", r"Avec les mêmes opérations ($\alpha*(x,y)=(\alpha x,\alpha^{-1}y)$), $\mathbb R^2$ est-il un $\mathbb R$-espace vectoriel ?",
          r"Non. Pour $u=(-1,30)$ : $2*u+3*u=(-5,25)\ne(-5,6)=5*u=(2+3)*u$. La distributivité $(\alpha+\beta).u=\alpha.u+\beta.u$ n'est pas vérifiée.", src=f"{M30}, ex. 1.3", duree=4),
        o("ea3", r"Sur $\mathbb R^2$ avec l'addition usuelle et $\lambda.(x,y)=(\lambda x,0)$. Est-ce un $\mathbb R$-espace vectoriel ?",
          r"Non : $1.(0,1)=(0,0)\ne(0,1)$. L'axiome $1.u=u$ est en défaut.", duree=3),
        o("ea4", r"Citer les quatre axiomes que doit vérifier la loi externe d'un $\mathbb R$-espace vectoriel.",
          r"$1.u=u$ ; $\alpha.(\beta.u)=(\alpha\beta).u$ ; $(\alpha+\beta).u=\alpha.u+\beta.u$ ; $\alpha.(u+v)=\alpha.u+\alpha.v$.", duree=3),
        o("ea5", r"Avec $\alpha*(x,y)=(\alpha x,\alpha^{-1}y)$ et $\alpha\ne0$, montrer que $\alpha*u=0_{\mathbb R^2}\iff u=0_{\mathbb R^2}$.",
          r"Si $\alpha*u=0$ : $\alpha x=0$ et $\alpha^{-1}y=0$ avec $\alpha\ne0$ et $\alpha^{-1}\ne0$, donc $x=y=0$. Réciproquement, $\alpha*(0,0)=(\alpha\times0,\alpha^{-1}\times0)=(0,0)$.", src=f"{M30}, ex. 1.1", duree=3),
    ]},
    {"n": 3, "titre": "Reconnaître un sous-espace vectoriel", "notions": ["sev"], "exos": [
        o("es0", r"Soient $E$ un $\mathbb R$-espace vectoriel et $F$ un ensemble. Donner TOUTES les conditions pour que $F$ soit un sous-espace vectoriel de $E$.",
          r"$F\subset E$ ; $0_E\in F$ ; $\forall(u,v)\in F^2$, $\forall\alpha\in\mathbb R$, $\alpha u+v\in F$.", src=f"{M30}, ex. 2.1", duree=2),
        o("es1", r"Montrer que $F=\{(x,y,z)\in\mathbb R^3,\ x+y-2z=0\}$ est un sous-espace vectoriel de $\mathbb R^3$.",
          r"$F\subset\mathbb R^3$. $0+0-0=0$ : $0\in F$. Si $u=(x,y,z)$, $v=(x',y',z')$ sont dans $F$ et $\alpha\in\mathbb R$ : $(\alpha x+x')+(\alpha y+y')-2(\alpha z+z')=\alpha(x+y-2z)+(x'+y'-2z')=0$, donc $\alpha u+v\in F$.", duree=4),
        o("es2", r"$\{(x,y)\in\mathbb R^2,\ x+y=1\}$ est-il un sous-espace vectoriel de $\mathbb R^2$ ?",
          r"Non : $(0,0)$ n'en fait pas partie ($0+0\ne1$).", duree=2),
        o("es3", r"$F=\{(x,y,z)\in\mathbb R^3,\ x-y=0\text{ et }x-z^2=0\}$ est-il un $\mathbb R$-espace vectoriel ? Justifier rigoureusement.",
          r"Non. $u=(4,4,2)\in F$ et $v=(4,4,-2)\in F$, mais $u+v=(8,8,0)\notin F$ car $8\ne0^2$.", src=f"{M30}, ex. 2.2 (a)", duree=4),
        o("es4", r"$G=\{P\in\mathbb R[X],\ P(1)+P'(1)=0\}$ est-il un $\mathbb R$-espace vectoriel ? Justifier rigoureusement.",
          r"$G\subset\mathbb R[X]$ et le polynôme nul est dans $G$. Si $(P,Q)\in G^2$ et $\alpha\in\mathbb R$ : $(\alpha P+Q)(1)+(\alpha P+Q)'(1)=\alpha(P(1)+P'(1))+(Q(1)+Q'(1))=0$. Donc $\alpha P+Q\in G$ : $G$ est un sev de $\mathbb R[X]$, donc un $\mathbb R$-ev.", src=f"{M30}, ex. 2.2 (b)", duree=4),
        o("es5", r"$\{(x,y)\in\mathbb R^2,\ xy=0\}$ est-il un sous-espace vectoriel de $\mathbb R^2$ ?",
          r"Non : $(1,0)$ et $(0,1)$ en font partie, mais leur somme $(1,1)$ non ($1\times1\ne0$).", duree=3),
        o("es6", r"$\{(x,y)\in\mathbb R^2,\ x\ge0\}$ est-il un sous-espace vectoriel de $\mathbb R^2$ ?",
          r"Non : $(1,0)$ en fait partie mais $-1.(1,0)=(-1,0)$ non. Pas stable par multiplication par un scalaire.", duree=2),
        o("es7", r"$E=\{(x,y,z)\in\mathbb R^3,\ x-y=0\text{ et }y-z^2=0\}$ est-il un $\mathbb R$-espace vectoriel ?",
          r"Non. $u=(1,1,1)\in E$ mais $2u=(2,2,2)\notin E$ car $2-2^2=-2\ne0$ : pas stable par multiplication externe.", src=f"{F30}, ex. 1.1", duree=3),
        o("es8", r"$F=\{(u_n)\in\mathbb R^{\mathbb N},\ \exists(\alpha,\beta)\in\mathbb R^2,\ \forall n,\ u_n=\alpha\times2^n+\beta\times3^n\}$ est-il un $\mathbb R$-espace vectoriel ?",
          r"Oui : $F=\mathrm{Vect}\big((2^n),(3^n)\big)$ est un sous-espace vectoriel de $\mathbb R^{\mathbb N}$, donc un $\mathbb R$-ev.", src=f"{F30}, ex. 1.2", duree=3),
    ]},
    {"n": 4, "titre": "Écrire un sous-espace sous forme de Vect", "notions": ["vect", "sev"], "exos": [
        o("eg1", r"Écrire $F=\{(x,y,z)\in\mathbb R^3,\ x+y-z=0\}$ sous la forme d'un Vect.",
          r"$z=x+y$ : $F=\{(x,y,x+y)\}=\{x(1,0,1)+y(0,1,1)\}=\mathrm{Vect}((1,0,1),(0,1,1))$.", duree=3),
        o("eg2", r"Écrire $\{(x,y,z)\in\mathbb R^3,\ x=2y\text{ et }z=-y\}$ sous la forme d'un Vect.",
          r"$\{(2y,y,-y)\}=\mathrm{Vect}((2,1,-1))$ : une droite.", duree=3),
        o("eg3", r"Trouver une base de $G=\{(x,y,z)\in\mathbb R^3,\ 2x+y=0\}$ et en déduire sa dimension.",
          r"$y=-2x$ : $G=\{(x,-2x,z)\}=\mathrm{Vect}(v_1=(1,-2,0),\ v_2=(0,0,1))$. $v_1$, $v_2$ ne sont pas colinéaires : famille libre et génératrice, base de $G$. $\dim G=2$.", src=f"{F30}, ex. 5.2", duree=4),
        o("eg4", r"Écrire $\{(x,y,z)\in\mathbb R^3,\ x+y+z=0\text{ et }x-y=0\}$ sous la forme d'un Vect.",
          r"$y=x$ et $z=-2x$ : $\{(x,x,-2x)\}=\mathrm{Vect}((1,1,-2))$.", duree=3),
        o("eg5", r"$F=\mathrm{Vect}(u_1=(1,2,-1),\ u_2=(-2,-4,2))$. Trouver une base de $F$ et sa dimension.",
          r"$u_2=-2u_1$, donc $F=\mathrm{Vect}(u_1)$. $u_1\ne0$ : $(u_1)$ est libre et génératrice, base de $F$. $\dim F=1$.", src=f"{F30}, ex. 5.1", duree=3),
        o("en1", r"Dans $\mathbb R_2[X]$, $F=\mathrm{Vect}(X^2+X)$ et $G=\mathrm{Vect}(X^2,X)$. 1. Donner un vecteur de $F$ et un vecteur hors de $F$. 2. Idem pour $G$. 3. A-t-on $F\subset G$ ? $G\subset F$ ? 4. Dimensions de $F$ et $G$.",
          r"1. $2(X^2+X)\in F$ ; $2X^2+3X\notin F$. 2. $2X^2+3X\in G$ ; $2X^2+3X+2\notin G$. 3. $2X^2+3X$ est dans $G$ mais pas dans $F$ : $G\not\subset F$. Si $P\in F$, $P=\alpha X^2+\alpha X\in G$ : $F\subset G$. 4. $(X^2+X)$ non nul : base de $F$, $\dim F=1$. $(X^2,X)$ non colinéaires : base de $G$, $\dim G=2$.",
          src=f"{F30}, ex. 4", duree=6),
    ]},
    {"n": 5, "titre": "Familles libres et liées", "notions": ["libre"], "exos": [
        o("el0", r"Soit $\mathcal F=(u_1,\dots,u_n)$ une famille de $E$. Donner, avec les quantificateurs, la définition de « $\mathcal F$ est libre », « $\mathcal F$ est liée », « $\mathcal F$ est génératrice de $E$ », et écrire $\mathrm{Vect}(\mathcal F)$ sous la forme d'un ensemble.",
          r"Libre : $\forall(\alpha_1,\dots,\alpha_n)\in\mathbb R^n$, $(\alpha_1u_1+\dots+\alpha_nu_n=0_E\Rightarrow\alpha_1=\dots=\alpha_n=0)$." "\n\n"
          r"Liée : $\exists(\alpha_1,\dots,\alpha_n)\in\mathbb R^n$ non tous nuls, $\alpha_1u_1+\dots+\alpha_nu_n=0_E$." "\n\n"
          r"Génératrice : $\forall u\in E$, $\exists(\alpha_1,\dots,\alpha_n)\in\mathbb R^n$, $u=\alpha_1u_1+\dots+\alpha_nu_n$." "\n\n"
          r"$\mathrm{Vect}(\mathcal F)=\{\alpha_1u_1+\dots+\alpha_nu_n,\ (\alpha_1,\dots,\alpha_n)\in\mathbb R^n\}$.", src=f"{M30}, ex. 5.1"),
        o("el1", r"La famille $((1,2),(2,4))$ est-elle libre ?", r"Non : $(2,4)=2(1,2)$, les deux vecteurs sont colinéaires. Liée.", duree=2),
        o("el2", r"La famille $((1,0,1),(0,1,1),(1,1,0))$ de $\mathbb R^3$ est-elle libre ?",
          r"$a(1,0,1)+b(0,1,1)+c(1,1,0)=0$ : $a+c=0$, $b+c=0$, $a+b=0$. Donc $a=b=-c$ et $a+b=-2c=0$ : $a=b=c=0$. Libre.", duree=4),
        o("el3", r"Dans $\mathbb R[X]$, la famille $(0_{\mathbb R[X]},\ X-1,\ X^2+3)$ est-elle libre ou liée ? Justifier.",
          r"$46\cdot0_{\mathbb R[X]}+0\cdot(X-1)+0\cdot(X^2+3)=0$ avec $(46,0,0)$ non tous nuls : liée. Toute famille contenant le vecteur nul est liée.", src=f"{M30}, ex. 5.2", duree=3),
        o("el4", r"Dans $\mathbb R[X]$ : la famille $(1,\ X,\ X^2)$ est-elle libre ? Et $(1+X,\ 1-X,\ X)$ ?",
          r"$(1,X,X^2)$ : degrés échelonnés, libre. $(1+X,1-X,X)$ : $X=\frac12(1+X)-\frac12(1-X)$, liée.", duree=3),
        o("el5", r"Dans $\mathbb R^3$, $\mathcal F_1=(u_1=(1,-1,2),\ u_2=(1,-2,1),\ u_3=(-1,3,0))$ est-elle une base ?",
          r"$u_1-2u_2=(1-2,\ -1+4,\ 2-2)=(-1,3,0)=u_3$ : la famille est liée, ce n'est pas une base.", src=f"{F30}, ex. 2", duree=4),
        o("el6", r"Une famille de $4$ vecteurs de $\mathbb R^3$ peut-elle être libre ?",
          r"Non : en dimension $3$, toute famille de plus de $3$ vecteurs est liée.", duree=2),
    ]},
    {"n": 6, "titre": "Bases et dimension", "notions": ["base", "dimension"], "exos": [
        o("eb1", r"Montrer que $((1,1),(1,-1))$ est une base de $\mathbb R^2$.",
          r"Les deux vecteurs ne sont pas colinéaires : famille libre. Elle a $2=\dim\mathbb R^2$ vecteurs : c'est une base.", duree=3),
        o("eb2", r"Dans $\mathbb R^3$, $\mathcal F_2=(v_1=(1,1,1),\ v_2=(2,2,1),\ v_3=(2,3,2))$ est-elle une base ?",
          r"$\alpha v_1+\beta v_2+\gamma v_3=0\iff\alpha+2\beta+2\gamma=0\ (L_1)$, $\alpha+2\beta+3\gamma=0\ (L_2)$, $\alpha+\beta+2\gamma=0\ (L_3)$. $L_2-L_1$ : $\gamma=0$. $L_3-L_1$ : $\beta=0$. D'où $\alpha=0$. Libre, et $3=\dim\mathbb R^3$ vecteurs : base.", src=f"{F30}, ex. 2"),
        v("eb3", r"Quelle est la dimension de $\mathbb R_3[X]$ ?", "3+1", "4", r"Base $(1,X,X^2,X^3)$ : dimension $4$.", duree=2),
        v("eb4", r"Quelle est la dimension de $\{(x,y,z)\in\mathbb R^3,\ x+y+z=0\}$ ?", "3-Matrix([[1,1,1]]).rank()", "2",
          r"$z=-x-y$ : deux paramètres libres, $\mathrm{Vect}((1,0,-1),(0,1,-1))$. Dimension $2$.", duree=3),
        o("eb5", r"La famille $((1,2,3),(4,5,6))$ est-elle génératrice de $\mathbb R^3$ ?",
          r"Non : $2$ vecteurs engendrent un espace de dimension au plus $2<3$.", duree=2),
        v("eb6", r"Quelle est la dimension de $\mathrm{Vect}((1,2,1),(2,4,2),(0,1,1))$ ?", "Matrix([[1,2,1],[2,4,2],[0,1,1]]).rank()", "2",
          r"$(2,4,2)=2(1,2,1)$ : on le retire. $(1,2,1)$ et $(0,1,1)$ ne sont pas colinéaires : base, dimension $2$.", duree=3),
    ]},
    {"n": 7, "titre": "Coordonnées dans une base", "notions": ["coordonnees", "base"], "exos": [
        v("eo1", r"Dans $\mathbb R^2$, base $\mathcal B=(u_1=(3,2),\ u_2=(-1,2))$. Trouver les coordonnées de $u=(-5,2)$ dans $\mathcal B$.",
          "Matrix([[3,-1],[2,2]]).inv()*Matrix([-5,2])", "Matrix([-1,2])",
          r"$au_1+bu_2=(3a-b,\ 2a+2b)=(-5,2)$ : $a=-1$, $b=2$. Vérification : $-(3,2)+2(-1,2)=(-5,2)$. Coordonnées $(-1,2)$.", src=f"{F30}, ex. 3.2"),
        v("eo2", r"Trouver les coordonnées de $(1,5)$ dans la base $((1,2),(1,-1))$ de $\mathbb R^2$.",
          "Matrix([[1,1],[2,-1]]).inv()*Matrix([1,5])", "Matrix([2,-1])", r"$a+b=1$ et $2a-b=5$ : $a=2$, $b=-1$."),
        v("eo3", r"Dans $\mathbb R_2[X]$, base $\mathcal B=(P_1=1-X,\ P_2=1+X,\ P_3=(1+X)^2)$. $P$ a pour coordonnées $(1,2,-1)$ dans $\mathcal B$. Donner $P$ et ses coordonnées dans la base canonique.",
          "(1-x)+2*(1+x)-(1+x)**2", "2-x-x**2",
          r"$P=P_1+2P_2-P_3=1-X+2(1+X)-(1+X)^2=2-X-X^2$ : coordonnées $(2,-1,-1)$ dans $(1,X,X^2)$.", src=f"{F30}, ex. 3.1 (a)"),
        v("eo4", r"Dans la base $\mathcal B=(P_1=1-X,\ P_2=1+X,\ P_3=(1+X)^2)$ de $\mathbb R_2[X]$, donner les coordonnées $(\alpha,\beta,\gamma)$ de $Q=2X^2+1$.",
          "Rational(3,2)*(1-x)-Rational(5,2)*(1+x)+2*(1+x)**2", "2*x**2+1",
          r"$\alpha P_1+\beta P_2+\gamma P_3=Q\iff\alpha+\beta+\gamma=1$, $-\alpha+\beta+2\gamma=0$, $\gamma=2$. D'où $\alpha=\frac32$, $\beta=-\frac52$, $\gamma=2$.", src=f"{F30}, ex. 3.1 (b)", duree=6),
    ]},
    {"n": 8, "titre": "Intersection et somme", "notions": ["somme"], "exos": [
        o("ei1", r"Dans $\mathbb R^3$, $F=\mathrm{Vect}((1,2,-1))$ et $G=\{(x,y,z),\ 2x+y=0\}$. Montrer que $F\cap G=\{0\}$.",
          r"$u\in F\cap G$ : $u=(\alpha,2\alpha,-\alpha)$ et $2\alpha+2\alpha=0$, donc $\alpha=0$ et $u=0$.", src=f"{F30}, ex. 5.3", duree=3),
        o("ei2", r"Dans $\mathbb R^3$, $F=\{x+y-z=0\}$ et $G=\{x+z=0\}$. Déterminer $F\cap G$.",
          r"$z=-x$ puis $y=z-x=-2x$ : $F\cap G=\{(x,-2x,-x)\}=\mathrm{Vect}((1,-2,-1))$, une droite.", duree=4),
        v("ei3", r"Dans $\mathbb R^3$, $F$ et $G$ sont deux plans et $F\cap G$ est une droite. Quelle est la dimension de $F+G$ ?", "2+2-1", "3",
          r"Grassmann : $\dim(F+G)=2+2-1=3$, donc $F+G=\mathbb R^3$.", duree=2),
        o("ei4", r"$F$ et $G$ sont deux sev de $E$. $F\cup G$ est-il toujours un sev ? Preuve ou contre-exemple.",
          r"Non. Dans $\mathbb R^2$, $F=\mathrm{Vect}((1,0))$ et $G=\mathrm{Vect}((0,1))$ : $(1,0)+(0,1)=(1,1)\notin F\cup G$.", duree=3),
        o("ei5", r"$F$ et $G$ sont deux sev de $E$. Vrai ou faux : $F+G$, $F\cup G$, $F\cap G$ sont des sev de $E$. Justifier la réponse pour $F\cap G$.",
          r"$F+G$ : vrai. $F\cup G$ : faux. $F\cap G$ : vrai. Preuve : $F\cap G\subset E$ ; $0_E\in F$ et $0_E\in G$ donc $0_E\in F\cap G$ ; si $(u,v)\in(F\cap G)^2$ et $\alpha\in\mathbb R$, $\alpha u+v\in F$ ($F$ sev) et $\alpha u+v\in G$ ($G$ sev), donc $\alpha u+v\in F\cap G$.", src=f"{M30}, ex. 3.1 et 3.2"),
        o("ei6", r"Donner la définition mathématique de $F+G$.",
          r"$F+G=\{u\in E,\ \exists(v,w)\in F\times G,\ u=v+w\}$.", src=f"{M30}, ex. 3.3", duree=2),
    ]},
    {"n": 9, "titre": "Somme directe, supplémentaires", "notions": ["supplementaire", "somme"], "exos": [
        o("ed1", r"Donner la définition mathématique de $E=F\oplus G$.",
          r"$E=F\oplus G\iff F\cap G=\{0_E\}$ et $E=F+G$.", src=f"{M30}, ex. 4.3", duree=2),
        o("ed2", r"Dans $\mathbb R^2$, $F=\mathrm{Vect}((1,1))$ et $G=\mathrm{Vect}((1,-2))$. Décomposer $u=(3,-3)$ dans $F+G$.",
          r"$a(1,1)+b(1,-2)=(3,-3)$ : $a+b=3$, $a-2b=-3$, d'où $b=2$, $a=1$. $u=v+w$ avec $v=(1,1)\in F$ et $w=(2,-4)\in G$. (Sur le dessin : parallèles à $F$ et à $G$ passant par l'extrémité de $u$.)", src=f"{M30}, ex. 3.3", duree=4),
        o("ed3", r"Dans $\mathbb R^3$, $F=\mathrm{Vect}((1,2,-1))$ (dimension $1$), $G=\{2x+y=0\}$ (dimension $2$) et $F\cap G=\{0\}$. A-t-on $F\oplus G=\mathbb R^3$ ?",
          r"$\dim(F+G)=1+2-0=3$ et $F+G\subset\mathbb R^3$, donc $F+G=\mathbb R^3$. Avec $F\cap G=\{0\}$ : $F\oplus G=\mathbb R^3$.", src=f"{F30}, ex. 5.4", duree=3),
        o("ed4", r"Dans $E=\mathbb R^3$ : $F=\{x+y-z=0\}$, $G=\{x+z=0\}$. Pour $u=(x,y,z)$, on pose $v=(0,x+z,x+z)$ et $w=(x,-x+y-z,-x)$. 1. Montrer que $v\in F$ et $w\in G$. 2. A-t-on $E=F+G$ ? 3. A-t-on $E=F\oplus G$ ?",
          r"1. $0+(x+z)-(x+z)=0$ : $v\in F$. $x+(-x)=0$ : $w\in G$. 2. $v+w=(x,y,z)=u$ : tout $u$ est dans $F+G$, donc $E=F+G$. 3. $(-1,2,1)$ est dans $F$ ($-1+2-1=0$) et dans $G$ ($-1+1=0$) : $F\cap G\ne\{0_E\}$, la somme n'est pas directe.", src=f"{M30}, ex. 4", duree=6),
        o("ed5", r"Dans l'espace des fonctions de $\mathbb R$ dans $\mathbb R$, montrer que les fonctions paires $\mathcal P$ et impaires $\mathcal I$ sont supplémentaires.",
          r"Si $f$ est paire et impaire : $f(x)=f(-x)=-f(x)$, donc $f=0$ : $\mathcal P\cap\mathcal I=\{0\}$. Toute $f$ s'écrit $f(x)=\frac{f(x)+f(-x)}2+\frac{f(x)-f(-x)}2$, somme d'une fonction paire et d'une impaire. Donc $E=\mathcal P\oplus\mathcal I$.", duree=6),
        v("ed6", r"Dans $\mathbb R^3$, quelle est la dimension d'un supplémentaire d'une droite vectorielle ?", "3-1", "2",
          r"$\dim F+\dim G=\dim E$ : $3-1=2$, un plan.", duree=2),
    ]},
    {"n": 10, "titre": "Niveau examen : annales complètes", "notions": ["sev", "libre", "coordonnees", "supplementaire"], "examen": True, "exos": [
        {"id": "ex1", "kind": "multi", "src": f"{M30}, ex. 1 et 2",
         "enonce": r"Sur $\mathbb R^2$ : $u+v=(x+x',y+y')$, $\alpha*u=(\alpha x,\alpha^{-1}y)$ si $\alpha\ne0$, $0*u=(0,0)$." "\n"
                   r"1. Pour $\alpha\ne0$, montrer que $\alpha*u=0\iff u=0$." "\n"
                   r"2. Pour $u=(-1,30)$, $v=(2,-7)$, calculer $u+v$, $1*u$, $2*u$, $3*u$, $5*u$." "\n"
                   r"3. Est-ce un $\mathbb R$-espace vectoriel ?" "\n"
                   r"4. Donner toutes les conditions pour que $F$ soit un sev de $E$." "\n"
                   r"5. $F=\{(x,y,z),\ x-y=0\text{ et }x-z^2=0\}$ et $G=\{P\in\mathbb R[X],\ P(1)+P'(1)=0\}$ sont-ils des $\mathbb R$-ev ?",
         "parts": ["ea5", "ea1", "ea2", "es0", "es3", "es4"]},
        {"id": "ex2", "kind": "multi", "src": f"{M30}, ex. 3, 4 et 5",
         "enonce": r"1. $F$, $G$ sev de $E$. Vrai ou faux : $F+G$, $F\cup G$, $F\cap G$ sont des sev. Justifier pour $F\cap G$." "\n"
                   r"2. Dans $\mathbb R^2$, $F=\mathrm{Vect}((1,1))$, $G=\mathrm{Vect}((1,-2))$ : décomposer $u=(3,-3)$ dans $F+G$." "\n"
                   r"3. Dans $\mathbb R^3$, $F=\{x+y-z=0\}$, $G=\{x+z=0\}$, $v=(0,x+z,x+z)$, $w=(x,-x+y-z,-x)$ : $v\in F$, $w\in G$ ? $E=F+G$ ? $E=F\oplus G$ ?" "\n"
                   r"4. Définitions de famille libre, liée, génératrice, et de $\mathrm{Vect}(\mathcal F)$." "\n"
                   r"5. $(0,\ X-1,\ X^2+3)$ est-elle libre ou liée ?",
         "parts": ["ei5", "ed2", "ed4", "el0", "el3"]},
        {"id": "ex3", "kind": "multi", "src": f"{F30}, ex. 1 à 4",
         "enonce": r"1. $E=\{(x,y,z),\ x-y=0\text{ et }y-z^2=0\}$ et $F=\{(u_n),\ u_n=\alpha2^n+\beta3^n\}$ sont-ils des $\mathbb R$-ev ?" "\n"
                   r"2. $\mathcal F_1=((1,-1,2),(1,-2,1),(-1,3,0))$ et $\mathcal F_2=((1,1,1),(2,2,1),(2,3,2))$ sont-elles des bases de $\mathbb R^3$ ?" "\n"
                   r"3. Base $\mathcal B=(1-X,\ 1+X,\ (1+X)^2)$ de $\mathbb R_2[X]$ : $P$ de coordonnées $(1,2,-1)$ dans $\mathcal B$ ; coordonnées de $Q=2X^2+1$ dans $\mathcal B$." "\n"
                   r"4. Coordonnées de $u=(-5,2)$ dans la base $((3,2),(-1,2))$ de $\mathbb R^2$." "\n"
                   r"5. $F=\mathrm{Vect}(X^2+X)$, $G=\mathrm{Vect}(X^2,X)$ : un vecteur dedans, un dehors, inclusions, dimensions.",
         "parts": ["es7", "es8", "el5", "eb2", "eo3", "eo4", "eo1", "en1"]},
        o("ex4", r"Dans $E=\mathbb R^3$ : $F=\mathrm{Vect}(u_1=(1,2,-1),\ u_2=(-2,-4,2))$ et $G=\{(x,y,z),\ 2x+y=0\}$." "\n"
                 r"1. Base et dimension de $F$. 2. Base et dimension de $G$. 3. Montrer que $F\cap G=\{0_E\}$. 4. Rappeler la définition de $F\oplus G=E$. Est-ce le cas ?" "\n"
                 r"5. Proposer un sev $F'$ tel que $F'\cap G\ne\{0_E\}$ mais $F'+G=E$. 6. Proposer un sev $H$ tel que $H\cap F=\{0_E\}$ mais $H+F\ne E$.",
          r"**1.** $u_2=-2u_1$ donc $F=\mathrm{Vect}(u_1)$ ; $u_1\ne0$ : base $(u_1)$, $\dim F=1$." "\n\n"
          r"**2.** $G=\{(x,-2x,z)\}=\mathrm{Vect}((1,-2,0),(0,0,1))$ ; non colinéaires : base, $\dim G=2$." "\n\n"
          r"**3.** $u\in F\cap G$ : $u=(\alpha,2\alpha,-\alpha)$ et $2\alpha+2\alpha=0$, donc $\alpha=0$." "\n\n"
          r"**4.** $F\oplus G=E\iff E=F+G$ et $F\cap G=\{0_E\}$. $\dim(F+G)=1+2-0=3$ et $F+G\subset E$ : oui." "\n\n"
          r"**5.** $F'$ doit être un plan vectoriel différent de $G$, par exemple $F'=\{(x,y,z),\ y=0\}$." "\n\n"
          r"**6.** $H$ doit être une droite vectorielle différente de $F$, par exemple $H=\{(x,y,z),\ x=y=0\}$.",
          src=f"{F30}, ex. 5 (10 points)", duree=15),
    ]},
    {"n": 11, "titre": "Examen + 20 %", "notions": ["supplementaire", "libre", "dimension"], "examen": True, "exos": [
        o("ey1", r"Soit $F=\{P\in\mathbb R_2[X],\ P(1)=0\}$. Montrer que $F$ est un sev, en donner une base et la dimension, puis un supplémentaire dans $\mathbb R_2[X]$.",
          r"$0\in F$ ; si $P,Q\in F$ : $(\alpha P+Q)(1)=0$. $P(1)=0\iff P=(X-1)(aX+b)$ : $F=\mathrm{Vect}(X-1,\ X(X-1))$, degrés échelonnés donc libre : base, $\dim F=2$. $G=\mathrm{Vect}(1)$ : un polynôme constant nul en $1$ est nul, donc $F\cap G=\{0\}$, et $2+1=3=\dim\mathbb R_2[X]$ : $F\oplus G=\mathbb R_2[X]$.", duree=10),
        o("ey2", r"Soient $F$ et $G$ deux sev de $E$. Montrer que $F\cup G$ est un sev de $E$ si et seulement si $F\subset G$ ou $G\subset F$.",
          r"Si $F\subset G$, $F\cup G=G$ est un sev (idem si $G\subset F$). Réciproquement, supposons $F\cup G$ sev, $F\not\subset G$ et $G\not\subset F$ : il existe $u\in F\setminus G$ et $v\in G\setminus F$. $u+v\in F\cup G$. Si $u+v\in F$, alors $v=(u+v)-u\in F$ : absurde. Si $u+v\in G$, alors $u=(u+v)-v\in G$ : absurde.", duree=10),
        o("ey3", r"Soit $(u,v,w)$ une famille libre de $E$. Montrer que $(u+v,\ v+w,\ w+u)$ est libre.",
          r"$a(u+v)+b(v+w)+c(w+u)=0\iff(a+c)u+(a+b)v+(b+c)w=0$. Comme $(u,v,w)$ est libre : $a+c=0$, $a+b=0$, $b+c=0$. Donc $b=c=-a$ et $b+c=-2a=0$ : $a=b=c=0$.", duree=8),
    ]},
    {"n": 12, "titre": "Examens 2028 et 2029", "notions": ["sev", "libre", "coordonnees", "supplementaire"], "examen": True, "exos": [
        o("ez1", r"Les ensembles suivants sont-ils des $\mathbb R$-ev ? Justifier." "\n"
                 r"(a) $F=\{P\in\mathbb R[X],\ P'(1)=1\}$. (b) $G=\{(x,y,z)\in\mathbb R^3,\ 2x=z\}$. (c) $H=\{f\in\mathbb R^{\mathbb R},\ \exists(a,b),\ \forall x,\ f(x)=ax+b\}$ (fonctions affines)." "\n"
                 r"(d) $G'=\{f\in\mathbb R^{\mathbb R},\ f(0)f(1)=0\}$.",
          r"(a) Non : le polynôme nul a $P'(1)=0\ne1$, donc $0\notin F$." "\n\n"
          r"(b) Oui : $0\in G$, et si $u,v\in G$, $\alpha\in\mathbb R$ : $2(\alpha x+x')=\alpha z+z'$, donc $\alpha u+v\in G$." "\n\n"
          r"(c) Oui : la fonction nulle est affine, et $\alpha(ax+b)+(a'x+b')=(\alpha a+a')x+(\alpha b+b')$." "\n\n"
          r"(d) Non : $f(x)=x$ et $g(x)=1-x$ sont dans $G'$ mais $(f+g)(0)(f+g)(1)=1\ne0$ : non stable par addition.",
          src="Examen S2-B3 EV mars 2024 et mars 2025, ex. 1", duree=10),
        o("ez2", r"Dans $\mathbb R^3$, $F=\{x=0\}$ et $G=\{z=0\}$. 1. A-t-on $E=F+G$ ? 2. A-t-on $E=F\oplus G$ ? Rappeler la caractérisation avec quantificateurs. 3. $F\cup G$ est-il un sev ?",
          r"1. $u=(x,y,z)=(0,y,z)+(x,0,0)$ avec $(0,y,z)\in F$, $(x,0,0)\in G$ : $E=F+G$." "\n\n"
          r"2. $E=F\oplus G\iff\forall u\in E,\ \exists!(u_1,u_2)\in F\times G,\ u=u_1+u_2$. Ici $u=(0,0,z)+(x,y,0)$ est une autre décomposition : pas unique, donc non." "\n\n"
          r"3. Non : $(0,1,1)\in F$, $(1,1,0)\in G$, leur somme $(1,2,1)$ n'est ni dans $F$ ni dans $G$.",
          src="Examen S2-B3 EV mars 2024, ex. 2", duree=10),
        o("ez3", r"Dans $\mathbb R^3$, $F=\{2x+y=0\}$ et $G=\{x+y+z=0\}$ sont deux plans, $H$ est la droite engendrée par $(-1,2,3)$ et $K$ celle engendrée par $(1,1,0)$. 1. $H\subset F$ ? 2. $F\cap K=\{0_E\}$ ? 3. $F\oplus K=E$ ? 4. Donner un plan $F'$ avec $F'\cap H=\{0_E\}$.",
          r"1. $(-\alpha,2\alpha,3\alpha)$ : $2(-\alpha)+2\alpha=0$, donc $H\subset F$." "\n\n"
          r"2. $(\alpha,\alpha,0)$ : $2\alpha+\alpha=0$ donne $\alpha=0$ : oui." "\n\n"
          r"3. $F\cap K=\{0\}$ et $\dim F+\dim K=2+1=3=\dim E$ : oui." "\n\n"
          r"4. $F'=\{x+y+z=0\}$ : $(-\alpha,2\alpha,3\alpha)$ donne $4\alpha=0$, donc $F'\cap H=\{0\}$.",
          src="Examen S2-B4 EV juin 2024, ex. 2", duree=12),
        o("ez4", r"Dans $\mathbb R^3$, $u_1=(1,1,1)$, $u_2=(2,1,1)$, $u_3=(1,-1,1)$. 1. $(u_1,u_2,u_3)$ est-elle une base ? 2. Coordonnées de $v=(3,2,0)$. 3. Dans $\mathbb R_2[X]$, $(1,X,X^2+X,X^2)$ est-elle génératrice ? libre ?",
          r"1. $\alpha+2\beta+\gamma=0$, $\alpha+\beta-\gamma=0$, $\alpha+\beta+\gamma=0$. $L_3-L_2$ : $2\gamma=0$ ; puis $L_1-L_3$ : $\beta=0$ ; puis $\alpha=0$. Libre, 3 vecteurs en dimension 3 : base." "\n\n"
          r"2. $\alpha+2\beta+\gamma=3$, $\alpha+\beta-\gamma=2$, $\alpha+\beta+\gamma=0$ : $\gamma=-1$, $\beta=3$, $\alpha=-2$. Coordonnées $(-2,3,-1)$." "\n\n"
          r"3. Génératrice : $a+bX+cX^2=a\cdot1+bX+0\,(X^2+X)+cX^2$. Pas libre : $(X^2+X)-X-X^2=0$ (4 vecteurs en dimension 3).",
          src="Examen S2-B4 EV juin 2024, ex. 1", duree=12),
        o("ez5", r"Dans $\mathbb R_2[X]$, $P_1=1$, $P_2=X^2+X+1$, $P_3=X^2-X+1$. 1. Montrer que $(P_1,P_2,P_3)$ est une base. 2. Coordonnées de $Q=3X^2+X+4$ dans cette base." "\n"
                 r"3. $\mathcal F=(\varepsilon_1,\varepsilon_2,\varepsilon_3)$ libre et $F=\mathrm{Vect}(\mathcal F)$ : montrer que $(\varepsilon_1,2\varepsilon_2,\varepsilon_3)$ est une base de $F$.",
          r"1. $\alpha+\beta P_2+\gamma P_3=0$ : $X^2$ : $\beta+\gamma=0$ ; $X$ : $\beta-\gamma=0$ ; donc $\beta=\gamma=0$ puis $\alpha=0$ : libre, 3 vecteurs, $\dim\mathbb R_2[X]=3$ : base." "\n\n"
          r"2. $Q=\alpha+\beta P_2+\gamma P_3$ : $\beta+\gamma=3$, $\beta-\gamma=1$, $\alpha+\beta+\gamma=4$ : $\beta=2$, $\gamma=1$, $\alpha=1$. Coordonnées $(1,2,1)$." "\n\n"
          r"3. Si $a\varepsilon_1+b(2\varepsilon_2)+c\varepsilon_3=0$, $\mathcal F$ libre donne $a=2b=c=0$ : libre. Elle engendre $F$ car $\varepsilon_2=\frac12(2\varepsilon_2)$. Libre et génératrice : base.",
          src="Examen S2-B4 EV mai 2025, ex. 1", duree=12),
    ]},
]


# Variants (same method, other numbers): a failed exercise comes back with the next one; build.py checks calc == ans.
def _v(enonce, calc, ans, sol):
    return {"enonce": enonce, "calc": calc, "ans": ans, "sol": sol}


VARIANTS = {
    "ec1": [_v(r"$u=(2,-1)$ et $v=(1,3)$. Calculer $3u+2v$.", "3*Matrix([2,-1])+2*Matrix([1,3])", "Matrix([8,3])", r"$(6+2,\ -3+6)=(8,3)$.")],
    "ec2": [_v(r"Trouver $(a,b)$ tel que $(4,2)=a(1,1)+b(1,-1)$.", "Matrix([[1,1],[1,-1]]).inv()*Matrix([4,2])", "Matrix([3,1])", r"$a+b=4$ et $a-b=2$ : $a=3$, $b=1$.")],
    "eb3": [_v(r"Quelle est la dimension de $\mathbb R_5[X]$ ?", "5+1", "6", r"Base $(1,X,\dots,X^5)$ : dimension $6$.")],
    "eb4": [_v(r"Quelle est la dimension de $\{(x,y,z)\in\mathbb R^3,\ x-y=0\text{ et }y-z=0\}$ ?", "3-Matrix([[1,-1,0],[0,1,-1]]).rank()", "1",
               r"$x=y=z$ : $\mathrm{Vect}((1,1,1))$, dimension $1$.")],
    "eb6": [_v(r"Quelle est la dimension de $\mathrm{Vect}((1,0,1),(0,1,1),(1,1,2))$ ?", "Matrix([[1,0,1],[0,1,1],[1,1,2]]).rank()", "2",
               r"$(1,1,2)=(1,0,1)+(0,1,1)$ : on le retire. Les deux autres ne sont pas colinéaires : dimension $2$.")],
    "eo1": [_v(r"Dans $\mathbb R^2$, base $\mathcal B=(u_1=(3,2),\ u_2=(-1,2))$. Trouver les coordonnées de $u=(5,6)$ dans $\mathcal B$.",
               "Matrix([[3,-1],[2,2]]).inv()*Matrix([5,6])", "Matrix([2,1])", r"$3a-b=5$ et $2a+2b=6$ : $a=2$, $b=1$.")],
    "eo2": [_v(r"Trouver les coordonnées de $(4,-1)$ dans la base $((1,2),(1,-1))$ de $\mathbb R^2$.", "Matrix([[1,1],[2,-1]]).inv()*Matrix([4,-1])", "Matrix([1,3])",
               r"$a+b=4$ et $2a-b=-1$ : $a=1$, $b=3$.")],
    "eo3": [_v(r"Dans $\mathbb R_2[X]$, base $\mathcal B=(1-X,\ 1+X,\ (1+X)^2)$. $P$ a pour coordonnées $(2,-1,1)$ dans $\mathcal B$. Donner $P$.",
               "2*(1-x)-(1+x)+(1+x)**2", "2-x+x**2", r"$2(1-X)-(1+X)+(1+X)^2=2-X+X^2$.")],
    "eo4": [_v(r"Dans la base $\mathcal B=(1-X,\ 1+X,\ (1+X)^2)$ de $\mathbb R_2[X]$, donner les coordonnées de $Q=X^2$.",
               "Rational(1,2)*(1-x)-Rational(3,2)*(1+x)+(1+x)**2", "x**2",
               r"$\alpha+\beta+\gamma=0$, $-\alpha+\beta+2\gamma=0$, $\gamma=1$ : $\alpha=\frac12$, $\beta=-\frac32$, $\gamma=1$.")],
    "ei3": [_v(r"Dans $\mathbb R^4$, $\dim F=3$, $\dim G=2$ et $\dim(F\cap G)=1$. Quelle est la dimension de $F+G$ ?", "3+2-1", "4", r"Grassmann : $3+2-1=4$.")],
    "ed6": [_v(r"Dans $\mathbb R^4$, quelle est la dimension d'un supplémentaire d'un plan vectoriel ?", "4-2", "2", r"$4-2=2$.")],
}
for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["id"] in VARIANTS:
            _e["variants"] = VARIANTS[_e["id"]]


EXTRA_PARTS = []

QUIZ = [
    {"notion": "sev", "type": "vf", "q": r"Un sous-espace vectoriel contient toujours le vecteur nul.", "bonne": True},
    {"notion": "sev", "type": "qcm", "q": r"Lequel est un sev de $\mathbb R^2$ ?",
     "choix": [r"$\{(x,y),\ x=2y\}$", r"$\{(x,y),\ x+y=1\}$", r"$\{(x,y),\ xy=0\}$", r"$\{(x,y),\ x\ge0\}$"], "bonne": 0},
    {"notion": "axiomes", "type": "vf", "q": r"Pour montrer qu'une structure n'est pas un ev, un seul axiome en défaut suffit.", "bonne": True},
    {"notion": "vect", "type": "vf", "q": r"$\mathrm{Vect}(u_1,\dots,u_n)$ est toujours un sous-espace vectoriel.", "bonne": True},
    {"notion": "libre", "type": "vf", "q": r"Toute famille contenant le vecteur nul est liée.", "bonne": True},
    {"notion": "libre", "type": "qcm", "q": r"Dans $\mathbb R^3$, une famille de $4$ vecteurs est :", "choix": [r"toujours liée", r"toujours libre", r"toujours génératrice", r"toujours une base"], "bonne": 0},
    {"notion": "base", "type": "vf", "q": r"En dimension $n$, une famille libre de $n$ vecteurs est une base.", "bonne": True},
    {"notion": "dimension", "type": "qcm", "q": r"$\dim\mathbb R_n[X]=$", "choix": [r"$n+1$", r"$n$", r"$n-1$", r"$2n$"], "bonne": 0},
    {"notion": "coordonnees", "type": "qcm", "q": r"Coordonnées de $3-X^2$ dans la base $(1,X,X^2)$ :", "choix": [r"$(3,0,-1)$", r"$(-1,0,3)$", r"$(3,-1)$", r"$(3,-1,0)$"], "bonne": 0},
    {"notion": "somme", "type": "vf", "q": r"L'union de deux sous-espaces vectoriels est toujours un sous-espace vectoriel.", "bonne": False},
    {"notion": "somme", "type": "qcm", "q": r"$\dim(F+G)=$",
     "choix": [r"$\dim F+\dim G-\dim(F\cap G)$", r"$\dim F+\dim G$", r"$\dim F\times\dim G$", r"$\max(\dim F,\dim G)$"], "bonne": 0},
    {"notion": "supplementaire", "type": "qcm", "q": r"$E=F\oplus G$ signifie :",
     "choix": [r"$F\cap G=\{0_E\}$ et $E=F+G$", r"$F\cap G=\varnothing$ et $E=F\cup G$", r"$E=F+G$", r"$F\cap G=\{0_E\}$"], "bonne": 0},
]

_SEV = r"$F$ sev de $E$ $\iff F\subset E$, $0_E\in F$, $\forall(u,v)\in F^2,\ \forall\alpha,\ \alpha u+v\in F$"
_CE = r"un contre-exemple chiffré suffit pour dire non"
_CL = r"$u\in\mathrm{Vect}(u_1,\dots,u_n)\iff\exists(\alpha_i),\ u=\sum\alpha_iu_i$"
_VECT = r"exprimer les inconnues principales en fonction des inconnues libres, factoriser chaque paramètre · nombre de paramètres libres = dimension"
_LIB = r"libre : $\sum\alpha_iu_i=0_E\Rightarrow\forall i,\ \alpha_i=0$"
_LIE = r"liée : $\exists(\alpha_i)$ non tous nuls, $\sum\alpha_iu_i=0_E$"
_BASE = r"en dimension $n$, une famille libre de $n$ vecteurs est une base"
_COORD = r"coordonnées de $u$ dans $(e_i)$ : l'unique $(x_i)$ tel que $u=\sum x_ie_i$"
_GR = r"Grassmann : $\dim(F+G)=\dim F+\dim G-\dim(F\cap G)$"
_SD = r"$E=F\oplus G\iff F\cap G=\{0_E\}$ et $E=F+G$"
_DIST = r"axiome : $(\alpha+\beta).u=\alpha.u+\beta.u$"
FORMULES = {
    "ec1": r"$(x,y)+(x',y')=(x+x',y+y')$ · $\alpha(x,y)=(\alpha x,\alpha y)$", "ec2": _CL + " · système $2\times2$", "ec3": _CL, "ec4": _CL + " · identifier les coefficients",
    "ea1": r"appliquer la définition des lois données", "ea2": _DIST + " · " + _CE, "ea3": r"axiome : $1.u=u$ · " + _CE,
    "ea4": r"$1.u=u$ · $\alpha.(\beta.u)=(\alpha\beta).u$ · $(\alpha+\beta).u=\alpha.u+\beta.u$ · $\alpha.(u+v)=\alpha.u+\alpha.v$",
    "ea5": r"$ab=0$ et $a\ne0\Rightarrow b=0$ · double implication",
    "es0": _SEV, "es1": _SEV, "es2": r"un sev contient $0_E$", "es3": _SEV + " · " + _CE, "es4": _SEV + r" · $(\alpha P+Q)'=\alpha P'+Q'$",
    "es5": _SEV + " · " + _CE, "es6": _SEV + " · " + _CE, "es7": _SEV + " · " + _CE, "es8": r"$\mathrm{Vect}(\dots)$ est toujours un sev",
    "eg1": _VECT, "eg2": _VECT, "eg3": _VECT + r" · deux vecteurs non colinéaires forment une famille libre", "eg4": _VECT,
    "eg5": r"retirer un vecteur combinaison des autres ne change pas le Vect · un vecteur non nul forme une famille libre",
    "en1": _CL + r" · $F\subset G$ si les générateurs de $F$ sont dans $G$ · famille génératrice libre = base, $\dim$ = cardinal",
    "el0": _LIB + " · " + _LIE + r" · génératrice : $\forall u\in E,\ \exists(\alpha_i),\ u=\sum\alpha_iu_i$",
    "el1": r"deux vecteurs sont liés $\iff$ ils sont colinéaires", "el2": _LIB, "el3": _LIE + r" · toute famille contenant $0_E$ est liée",
    "el4": r"degrés échelonnés $\Rightarrow$ libre · " + _LIE, "el5": _LIE + r" · une base est libre", "el6": r"en dimension $n$, plus de $n$ vecteurs $\Rightarrow$ liée",
    "eb1": r"deux vecteurs non colinéaires $\Rightarrow$ libre · " + _BASE, "eb2": _LIB + " · " + _BASE, "eb3": r"$\dim\mathbb R_n[X]=n+1$",
    "eb4": r"nombre de paramètres libres = dimension", "eb5": r"en dimension $n$, moins de $n$ vecteurs $\Rightarrow$ non génératrice",
    "eb6": r"retirer les vecteurs combinaisons des autres · famille génératrice libre = base",
    "eo1": _COORD, "eo2": _COORD, "eo3": _COORD + r" · base canonique de $\mathbb R_2[X]$ : $(1,X,X^2)$", "eo4": _COORD + r" · identifier les coefficients",
    "ei1": r"$u\in F\cap G$ : paramétrer par $F$, injecter l'équation de $G$", "ei2": r"$u\in F\cap G$ : résoudre les deux équations ensemble", "ei3": _GR,
    "ei4": _CE + r" · $F\cup G$ n'est pas stable par addition en général", "ei5": _SEV, "ei6": r"$F+G=\{v+w,\ v\in F,\ w\in G\}$",
    "ed1": _SD, "ed2": r"$u=v+w$, $v\in F$, $w\in G$ : résoudre $u=a\,f+b\,g$", "ed3": _GR + " · " + _SD + r" · $F\subset E$ et $\dim F=\dim E\Rightarrow F=E$",
    "ed4": r"$F+G=\{v+w,\ v\in F,\ w\in G\}$ · " + _SD, "ed5": _SD + r" · $f(x)=\frac{f(x)+f(-x)}2+\frac{f(x)-f(-x)}2$ · paire : $f(-x)=f(x)$, impaire : $f(-x)=-f(x)$",
    "ed6": r"$E=F\oplus G\Rightarrow\dim F+\dim G=\dim E$",
    "ex4": r"retirer un vecteur colinéaire · " + _VECT + r" · $u\in F\cap G$ : paramétrer par $F$, injecter l'équation de $G$ · " + _GR + " · " + _SD,
    "ey1": _SEV + r" · $P(a)=0\iff X-a\mid P$ · degrés échelonnés $\Rightarrow$ libre · $E=F\oplus G\iff F\cap G=\{0\}$ et $\dim F+\dim G=\dim E$",
    "ey2": _SEV + r" · raisonnement par l'absurde · $v=(u+v)-u$",
    "ey3": _LIB + r" · regrouper selon $u$, $v$, $w$",
    "ez1": _SEV + " · " + _CE, "ez2": _SD + r" · décomposition unique : $\forall u,\ \exists!(v,w),\ u=v+w$ · " + _CE,
    "ez3": r"$u\in F\cap G$ : paramétrer par $F$, injecter l'équation de $G$ · " + _SD,
    "ez4": _LIB + r" · " + _BASE + r" · " + _COORD, "ez5": _LIB + r" · " + _BASE + r" · " + _COORD,
}
