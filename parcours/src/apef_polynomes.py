"""Level path: S2 maths, ECUE APEF, part 1: polynômes (division, racines, multiplicité, factorisation dans R[X]).

Calibrated on Examen S2-B3 APEF mars 2026 (ex. 1), read on the official correction, and on the
exercise types of `annales/FORMULES.md` (section « APEF (polynômes) »). No Moodle chapter in S2-MATHS-2030.
Promo 2031 has no complex numbers: factorisation in R[X] only.
`value` exercises: `calc` (sympy, variable x for X) must equal `ans`; polynomial answers are compared at sample points.
"""

SUBJECT = {
    "id": "maths-s2-apef-polynomes",
    "ordre": 200,
    "matiere": "maths",
    "semestre": "S2",
    "ecue": "APEF",
    "titre": "Polynômes",
    "chapitres_moodle": [],
    "td": "TD polynômes (S2)",
    "examens": ["Examen S2-B3 APEF (avant les vacances de printemps)"],
}

NOTIONS = [
    {"id": "degre", "titre": "Degré d'un polynôme",
     "formule": r"$\deg(AB)=\deg A+\deg B$ · $\deg(A+B)\le\max(\deg A,\deg B)$ · coefficient dominant de $AB$ = produit des coefficients dominants",
     "exemple": r"$(X^3+2X-1)(X^2-3)$ est de degré $5$",
     "cours": r"Le degré d'une somme peut baisser si les termes dominants se compensent. Par convention $\deg 0=-\infty$."},
    {"id": "division", "titre": "Division euclidienne",
     "formule": r"$\exists!\,(Q,R)$, $A=BQ+R$ et $\deg R<\deg B$",
     "exemple": r"$X^4+1=(X^2+1)(X^2-1)+2$",
     "cours": r"On pose la division comme pour les entiers : on élimine à chaque étape le terme de plus haut degré. On s'arrête dès que le degré du reste est strictement inférieur à celui de $B$. Toujours vérifier $A=BQ+R$."},
    {"id": "racine", "titre": "Racine et divisibilité",
     "formule": r"$P(a)=0\iff X-a\mid P$ · le reste de $P$ par $X-a$ est $P(a)$ · $(X-a)(X-b)\mid P\iff P(a)=P(b)=0$ ($a\ne b$)",
     "exemple": r"$X-2$ divise $X^3-3X^2+4$ car $8-12+4=0$",
     "cours": r"Pour factoriser : trouver une racine évidente $a$ parmi $0,\pm1,\pm2$, diviser par $X-a$, recommencer sur le quotient."},
    {"id": "multiplicite", "titre": "Multiplicité d'une racine",
     "formule": r"$a$ racine d'ordre $m$ $\iff P(a)=P'(a)=\dots=P^{(m-1)}(a)=0$ et $P^{(m)}(a)\ne0$ $\iff (X-a)^m\mid P$ et $(X-a)^{m+1}\nmid P$",
     "exemple": r"$X^3-3X+2$ : $P(1)=P'(1)=0$, $P''(1)=6$, donc $1$ est racine double",
     "cours": r"On dérive tant que la valeur en $a$ est nulle. Racine au moins double : $P(a)=P'(a)=0$. Si $a$ est racine d'ordre $m$ de $P$, elle est racine d'ordre $m-1$ de $P'$."},
    {"id": "reste", "titre": "Reste sans poser la division",
     "formule": r"par $(X-a)(X-b)$ : $R=\alpha X+\beta$ avec $R(a)=P(a)$, $R(b)=P(b)$ · par $(X-a)^2$ : $R=P'(a)(X-a)+P(a)$",
     "exemple": r"reste de $X^5$ par $(X-1)^2$ : $5(X-1)+1=5X-4$",
     "cours": r"Écrire $P=BQ+R$ avec $\deg R<\deg B$, puis évaluer aux racines de $B$ : le terme $BQ$ disparaît. Pour une racine double, dériver l'égalité puis évaluer."},
    {"id": "factorisation", "titre": "Factorisation dans $\\mathbb R[X]$",
     "formule": r"irréductibles de $\mathbb R[X]$ : les polynômes de degré 1 et ceux de degré 2 avec $\Delta<0$ · $X^2-a^2=(X-a)(X+a)$ · $X^3-a^3=(X-a)(X^2+aX+a^2)$",
     "exemple": r"$X^4-1=(X-1)(X+1)(X^2+1)$",
     "cours": r"Chercher les racines réelles, diviser, puis vérifier que chaque facteur de degré 2 restant a un discriminant strictement négatif. Polynôme bicarré : poser $Y=X^2$."},
    {"id": "taylor", "titre": "Formule de Taylor pour les polynômes",
     "formule": r"$P(X)=\sum_{k=0}^{\deg P}\frac{P^{(k)}(a)}{k!}(X-a)^k$ · en $0$ : le coefficient de $X^k$ vaut $\frac{P^{(k)}(0)}{k!}$",
     "exemple": r"$X^3-2X+1=(X-1)+3(X-1)^2+(X-1)^3$",
     "cours": r"La formule est exacte pour un polynôme (pas de reste). Elle donne directement la multiplicité : $a$ est d'ordre $m$ si les $m$ premiers coefficients sont nuls."},
    {"id": "des", "titre": "Décomposition en éléments simples",
     "formule": r"si $\deg N\ge\deg D$ : division euclidienne d'abord · pôle simple $a$ : $\frac{c}{X-a}$ avec $c=[(X-a)F](a)$ · pôle double : $\frac{c_1}{X-a}+\frac{c_2}{(X-a)^2}$ · facteur $X^2+1$ : $\frac{bX+c}{X^2+1}$",
     "exemple": r"$\frac1{(X-1)(X+1)}=\frac{1/2}{X-1}-\frac{1/2}{X+1}$",
     "cours": r"Coefficient d'un pôle simple : multiplier par $X-a$ puis remplacer $X$ par $a$. Les autres coefficients s'obtiennent en évaluant en un point ou par la limite de $xF(x)$ en $+\infty$. Sert à calculer des primitives : $\int\frac{dx}{x-a}=\ln|x-a|$."},
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


A30 = "Examen S2-B3 APEF mars 2026"

LEVELS = [
    {"n": 1, "titre": "Degré et opérations", "notions": ["degre"], "exos": [
        v("pd1", r"$A=X^3+2X-1$ et $B=X^2-3$. Quel est le degré de $AB$ ?", "degree((x**3+2*x-1)*(x**2-3), x)", "5",
          r"$\deg(AB)=\deg A+\deg B=3+2=5$.", duree=2),
        v("pd2", r"$A=2X^3+X$ et $B=-2X^3+X^2+1$. Quel est le degré de $A+B$ ?", "degree(2*x**3+x-2*x**3+x**2+1, x)", "2",
          r"Les termes en $X^3$ se compensent : $A+B=X^2+X+1$, de degré $2$.", duree=2),
        v("pd3", r"Développer $(X^2+1)(X-2)$.", "expand((x**2+1)*(x-2))", "x**3-2*x**2+x-2",
          r"$X^3-2X^2+X-2$.", duree=2),
        v("pd4", r"Quel est le coefficient dominant de $(2X-1)^3$ ?", "LC((2*x-1)**3, x)", "8",
          r"Le terme dominant est $(2X)^3=8X^3$ : coefficient $8$.", duree=2),
    ]},
    {"n": 2, "titre": "Division euclidienne", "notions": ["division"], "exos": [
        v("pe1", r"Donner le quotient de la division euclidienne de $X^3+2X^2-X+3$ par $X-1$ (et le reste).",
          "quo(x**3+2*x**2-x+3, x-1)", "x**2+3*x+2",
          r"$X^3+2X^2-X+3=(X-1)(X^2+3X+2)+5$ : $Q=X^2+3X+2$, $R=5$."),
        v("pe2", r"Donner le reste de la division euclidienne de $X^4+1$ par $X^2+1$.", "rem(x**4+1, x**2+1)", "2",
          r"$X^4+1=(X^2+1)(X^2-1)+2$ : $R=2$."),
        v("pe3", r"Donner le quotient de la division euclidienne de $2X^3-3X^2+4$ par $X^2-X+1$ (et le reste).",
          "quo(2*x**3-3*x**2+4, x**2-x+1)", "2*x-1",
          r"$2X^3-3X^2+4=(X^2-X+1)(2X-1)+(-3X+5)$ : $Q=2X-1$, $R=-3X+5$."),
        v("pe4", r"Donner le reste de la division euclidienne de $X^4-3X^2+2X+1$ par $X^2+X$.", "rem(x**4-3*x**2+2*x+1, x**2+x)", "4*x+1",
          r"$X^4-3X^2+2X+1=(X^2+X)(X^2-X-2)+4X+1$ : $R=4X+1$."),
    ]},
    {"n": 3, "titre": "Racines et divisibilité", "notions": ["racine"], "exos": [
        v("pr1", r"Sans poser la division, donner le reste de $X^5-3X+1$ par $X-2$.", "rem(x**5-3*x+1, x-2)", "27",
          r"Le reste par $X-a$ est $P(a)$ : $P(2)=32-6+1=27$.", duree=2),
        v("pr2", r"Pour quelle valeur de $m$ le polynôme $X-1$ divise-t-il $X^3+mX^2-2$ ?", "-(x**3-2).subs(x,1)", "1",
          r"$X-1\mid P\iff P(1)=0\iff1+m-2=0\iff m=1$.", duree=2),
        v("pr3", r"Vérifier que $2$ est racine de $P=X^3-3X^2+4$, puis factoriser $P$.", "x**3-3*x**2+4", "(x-2)**2*(x+1)",
          r"$P(2)=8-12+4=0$. Division par $X-2$ : $P=(X-2)(X^2-X-2)$, et $X^2-X-2=(X-2)(X+1)$. Donc $P=(X-2)^2(X+1)$."),
        o("pr4", r"Montrer, sans poser la division, que $X^2-3X+2$ divise $X^4-5X^2+4$.",
          r"$X^2-3X+2=(X-1)(X-2)$. $P(1)=1-5+4=0$ et $P(2)=16-20+4=0$. Les racines $1$ et $2$ sont distinctes, donc $(X-1)(X-2)\mid P$.", duree=3),
        v("pr5", r"Trouver $a$ et $b$ pour que $X^2-1$ divise $P=X^4+aX^3+bX^2+X-2$.", "rem(x**4-x**3+x**2+x-2, x**2-1)", "0",
          r"$P(1)=a+b=0$ et $P(-1)=-a+b-2=0$. D'où $b=1$, $a=-1$."),
    ]},
    {"n": 4, "titre": "Multiplicité d'une racine", "notions": ["multiplicite"], "exos": [
        v("pm1", r"Soit $A=X^4+2X^2+8X+5$. Montrer que $-1$ est racine de $A$ et trouver $\alpha\in\mathbb N$ tel que $(X+1)^\alpha$ divise $A$ et $(X+1)^{\alpha+1}$ ne divise pas $A$.",
          "roots(x**4+2*x**2+8*x+5)[-1]", "2",
          r"$A(-1)=1+2-8+5=0$. $A'=4X^3+4X+8$, $A'(-1)=0$. $A''=12X^2+4$, $A''(-1)=16\ne0$. Racine d'ordre exactement $2$ : $\alpha=2$.", src=f"{A30}, ex. 1.1 (a)"),
        v("pm2", r"Quel est l'ordre de multiplicité de la racine $1$ de $P=X^3-3X+2$ ?", "roots(x**3-3*x+2)[1]", "2",
          r"$P(1)=0$. $P'=3X^2-3$, $P'(1)=0$. $P''=6X$, $P''(1)=6\ne0$. Ordre $2$ : $P=(X-1)^2(X+2)$."),
        v("pm3", r"Quel est l'ordre de multiplicité de la racine $1$ de $P=X^4-2X^3+2X-1$ ?", "roots(x**4-2*x**3+2*x-1)[1]", "3",
          r"$P(1)=0$. $P'=4X^3-6X^2+2$, $P'(1)=0$. $P''=12X^2-12X$, $P''(1)=0$. $P'''=24X-12$, $P'''(1)=12\ne0$. Ordre $3$ : $P=(X-1)^3(X+1)$."),
        v("pm4", r"Trouver $a$ et $b$ pour que $2$ soit racine double de $P=X^3+aX+b$.", "rem(x**3-12*x+16, (x-2)**2)", "0",
          r"$P'(2)=12+a=0$ donne $a=-12$. $P(2)=8-24+b=0$ donne $b=16$. $P=X^3-12X+16=(X-2)^2(X+4)$."),
        o("pm5", r"Soit $a$ une racine d'ordre $m\ge1$ de $P$. Montrer que $a$ est racine d'ordre $m-1$ de $P'$.",
          r"$P=(X-a)^mQ$ avec $Q(a)\ne0$. $P'=(X-a)^{m-1}\big(mQ+(X-a)Q'\big)$ et le second facteur vaut $mQ(a)\ne0$ en $a$. Donc $a$ est d'ordre exactement $m-1$ dans $P'$."),
    ]},
    {"n": 5, "titre": "Reste sans poser la division", "notions": ["reste", "racine"], "exos": [
        v("ps1", r"Donner le reste de la division euclidienne de $X^{10}$ par $X^2-1$.", "rem(x**10, x**2-1)", "1",
          r"$R=\alpha X+\beta$. $R(1)=1$ et $R(-1)=1$ : $\alpha=0$, $\beta=1$. $R=1$."),
        v("ps2", r"Donner le reste de la division euclidienne de $X^7$ par $X^2-3X+2$.", "rem(x**7, x**2-3*x+2)", "127*x-126",
          r"$X^2-3X+2=(X-1)(X-2)$, $R=\alpha X+\beta$. $\alpha+\beta=1$ et $2\alpha+\beta=128$ : $\alpha=127$, $\beta=-126$."),
        v("ps3", r"Donner le reste de la division euclidienne de $X^5$ par $(X-1)^2$.", "rem(x**5, (x-1)**2)", "5*x-4",
          r"$R=P'(1)(X-1)+P(1)=5(X-1)+1=5X-4$."),
        v("ps4", r"Donner le reste de la division euclidienne de $X^6+X$ par $(X+1)^2$.", "rem(x**6+x, (x+1)**2)", "-5*x-5",
          r"$P(-1)=1-1=0$, $P'(-1)=-6+1=-5$. $R=-5(X+1)=-5X-5$."),
    ]},
    {"n": 6, "titre": "Factorisation dans R[X]", "notions": ["factorisation", "racine"], "exos": [
        v("pf1", r"Factoriser $X^3-X^2-4X+4$ dans $\mathbb R[X]$.", "x**3-x**2-4*x+4", "(x-1)*(x-2)*(x+2)",
          r"$1$ est racine. $P=(X-1)(X^2-4)=(X-1)(X-2)(X+2)$."),
        v("pf2", r"Factoriser $X^4-1$ en produit d'irréductibles de $\mathbb R[X]$.", "x**4-1", "(x-1)*(x+1)*(x**2+1)",
          r"$X^4-1=(X^2-1)(X^2+1)=(X-1)(X+1)(X^2+1)$. $X^2+1$ est irréductible ($\Delta=-4<0$)."),
        v("pf3", r"Factoriser $X^3+1$ en produit d'irréductibles de $\mathbb R[X]$.", "x**3+1", "(x+1)*(x**2-x+1)",
          r"$-1$ est racine : $X^3+1=(X+1)(X^2-X+1)$. $\Delta=1-4=-3<0$ : irréductible."),
        v("pf4", r"Soit $A=X^4+2X^2+8X+5$, dont $-1$ est racine double. Effectuer la division euclidienne de $A$ par $(X+1)^2$ et écrire $A$ comme produit d'irréductibles de $\mathbb R[X]$.",
          "x**4+2*x**2+8*x+5", "(x+1)**2*(x**2-2*x+5)",
          r"$A=(X+1)^2(X^2-2X+5)$. Le discriminant de $X^2-2X+5$ vaut $4-20=-16<0$ : irréductible dans $\mathbb R[X]$.", src=f"{A30}, ex. 1.1 (b)"),
        v("pf5", r"Factoriser $X^4+X^2-2$ en produit d'irréductibles de $\mathbb R[X]$.", "x**4+x**2-2", "(x-1)*(x+1)*(x**2+2)",
          r"Avec $Y=X^2$ : $Y^2+Y-2=(Y-1)(Y+2)$. Donc $(X^2-1)(X^2+2)=(X-1)(X+1)(X^2+2)$."),
    ]},
    {"n": 7, "titre": "Formule de Taylor", "notions": ["taylor"], "exos": [
        v("pt1", r"Écrire $P=X^3-2X+1$ en puissances de $X-1$.", "x**3-2*x+1", "(x-1)+3*(x-1)**2+(x-1)**3",
          r"$P(1)=0$, $P'(1)=1$, $\frac{P''(1)}2=3$, $\frac{P'''(1)}6=1$. $P=(X-1)+3(X-1)^2+(X-1)^3$."),
        v("pt2", r"$P$ est de degré $2$, $P(0)=1$, $P'(0)=-2$, $P''(0)=6$. Donner $P$.", "1-2*x+6*x**2/factorial(2)", "1-2*x+3*x**2",
          r"$P=P(0)+P'(0)X+\frac{P''(0)}2X^2=1-2X+3X^2$.", duree=2),
        v("pt3", r"On sait que $P'''(0)=12$. Quel est le coefficient de $X^3$ dans $P$ ?", "12/factorial(3)", "2",
          r"$a_3=\frac{P'''(0)}{3!}=\frac{12}6=2$.", duree=2),
        v("pt4", r"Écrire $X^4$ en puissances de $X+1$.", "x**4", "1-4*(x+1)+6*(x+1)**2-4*(x+1)**3+(x+1)**4",
          r"$P(-1)=1$, $P'(-1)=-4$, $\frac{P''(-1)}2=6$, $\frac{P'''(-1)}6=-4$, $\frac{P^{(4)}}{24}=1$. $X^4=1-4(X+1)+6(X+1)^2-4(X+1)^3+(X+1)^4$."),
    ]},
    {"n": 8, "titre": "Décomposition en éléments simples", "notions": ["des", "division"], "exos": [
        v("pz1", r"Décomposer en éléments simples $\dfrac1{(X-1)(X+1)}$.", "1/((x-1)*(x+1))", "1/(2*(x-1))-1/(2*(x+1))",
          r"Pôle $1$ : $c=\frac1{1+1}=\frac12$. Pôle $-1$ : $c=\frac1{-1-1}=-\frac12$. $F=\frac{1/2}{X-1}-\frac{1/2}{X+1}$."),
        v("pz2", r"Décomposer en éléments simples $\dfrac{X+3}{(X-1)(X+2)}$.", "(x+3)/((x-1)*(x+2))", "4/(3*(x-1))-1/(3*(x+2))",
          r"Pôle $1$ : $\frac{1+3}{1+2}=\frac43$. Pôle $-2$ : $\frac{-2+3}{-2-1}=-\frac13$. $F=\frac{4/3}{X-1}-\frac{1/3}{X+2}$."),
        v("pz3", r"Décomposer en éléments simples $\dfrac{X^2}{X-1}$.", "x**2/(x-1)", "x+1+1/(x-1)",
          r"$\deg N\ge\deg D$ : division. $X^2=(X-1)(X+1)+1$, donc $F=X+1+\frac1{X-1}$."),
        v("pz4", r"Calculer $\displaystyle\int_2^3\frac{dx}{x^2-1}$.", "integrate(1/(x**2-1), (x,2,3))", "log(Rational(3,2))/2",
          r"$\frac1{x^2-1}=\frac12\left(\frac1{x-1}-\frac1{x+1}\right)$. $\frac12\left[\ln\frac{x-1}{x+1}\right]_2^3=\frac12\left(\ln\frac12-\ln\frac13\right)=\frac12\ln\frac32$.", duree=5),
        v("pz5", r"Décomposer en éléments simples $\dfrac1{X(X^2+1)}$.", "1/(x*(x**2+1))", "1/x-x/(x**2+1)",
          r"$F=\frac aX+\frac{bX+c}{X^2+1}$. $a=\frac1{0+1}=1$. $1=(X^2+1)+(bX+c)X$ donne $b=-1$, $c=0$. $F=\frac1X-\frac X{X^2+1}$."),
        v("pz6", r"Décomposer en éléments simples $\dfrac1{X^2(X+1)}$.", "1/(x**2*(x+1))", "-1/x+1/x**2+1/(x+1)",
          r"$F=\frac aX+\frac b{X^2}+\frac c{X+1}$. $b=\frac1{0+1}=1$, $c=\frac1{(-1)^2}=1$. Limite de $xF(x)$ en $+\infty$ : $0=a+c$, $a=-1$."),
    ]},
    {"n": 9, "titre": "Niveau examen : annale complète", "notions": ["multiplicite", "factorisation", "reste"], "examen": True, "exos": [
        {"id": "px1", "kind": "multi", "src": f"{A30}, ex. 1.1",
         "enonce": r"Soit $A(X)=X^4+2X^2+8X+5$." "\n"
                   r"(a) Montrer que $-1$ est une racine de $A$. Trouver $\alpha\in\mathbb N$ tel que $(X+1)^\alpha$ divise $A$ et $(X+1)^{\alpha+1}$ ne divise pas $A$." "\n"
                   r"(b) Après avoir effectué la division euclidienne de $A$ par $(X+1)^\alpha$, écrire $A$ comme produit de polynômes irréductibles dans $\mathbb R[X]$.",
         "parts": ["pm1", "pf4"]},
        o("px2", r"Soit $P\in\mathbb R[X]$ de degré $3$ vérifiant $(X-1)^2\mid(P+1)$ et $X^2\mid(P-1)$." "\n"
                 r"(a) Que signifient ces deux affirmations ? En déduire $P(1)=-1$ et $P(0)=1$." "\n"
                 r"(b) Expliquer pourquoi $X\mid P'$ et $(X-1)\mid P'$. En déduire que $X(X-1)\mid P'$." "\n"
                 r"(c) En déduire que $P'=aX^2-aX$ avec $a\in\mathbb R$." "\n"
                 r"(d) En déduire qu'il existe $b$ tel que $P=a\frac{X^3}3-a\frac{X^2}2+b$, puis trouver $a$ et $b$.",
          r"**(a)** Il existe $Q_1,Q_2$ tels que $P+1=(X-1)^2Q_1$ et $P-1=X^2Q_2$. En $X=1$ : $P(1)=-1$. En $X=0$ : $P(0)=1$." "\n\n"
          r"**(b)** $1$ est racine d'ordre au moins $2$ de $P+1$, donc racine de $(P+1)'=P'$. De même $0$ est racine de $(P-1)'=P'$. Racines distinctes : $X(X-1)\mid P'$." "\n\n"
          r"**(c)** $P'=X(X-1)Q_3$ et $\deg P'=2$, donc $Q_3$ est une constante $a$ : $P'=aX^2-aX$." "\n\n"
          r"**(d)** En primitivant : $P=a\frac{X^3}3-a\frac{X^2}2+b$. $P(0)=1$ donne $b=1$. $P(1)=-1$ donne $\frac a3-\frac a2+1=-1$, soit $a=12$. $P=4X^3-6X^2+1$.",
          src=f"{A30}, ex. 1.2", duree=12),
        o("px3", r"Soit $n\ge2$ et $P=(X-3)^{2n}+(X-2)^n-2$. Donner le reste de la division euclidienne de $P$ par $(X-2)(X-3)$.",
          r"$R=\alpha X+\beta$ avec $R(2)=P(2)=1+0-2=-1$ et $R(3)=P(3)=0+1-2=-1$. Donc $\alpha=0$, $\beta=-1$ : $R=-1$.", duree=6),
    ]},
    {"n": 10, "titre": "Examen + 20 %", "notions": ["multiplicite", "reste", "racine"], "examen": True, "exos": [
        o("py1", r"Trouver le polynôme $P$ de degré $3$ tel que $(X-1)^2\mid(P-1)$ et $(X+1)^2\mid(P+1)$.",
          r"$1$ et $-1$ sont racines de $P'$, de degré $2$ : $P'=a(X^2-1)$, donc $P=a\left(\frac{X^3}3-X\right)+b$. $P(1)=1$ : $-\frac{2a}3+b=1$. $P(-1)=-1$ : $\frac{2a}3+b=-1$. D'où $b=0$, $a=-\frac32$ : $P=-\frac12X^3+\frac32X$.", duree=10),
        o("py2", r"Soit $n\ge2$. Donner le reste de la division euclidienne de $X^n$ par $(X-1)^2$, puis par $(X-1)(X-2)$.",
          r"Par $(X-1)^2$ : $R=P'(1)(X-1)+P(1)=n(X-1)+1=nX-n+1$." "\n\n"
          r"Par $(X-1)(X-2)$ : $R=\alpha X+\beta$, $\alpha+\beta=1$, $2\alpha+\beta=2^n$. $\alpha=2^n-1$, $\beta=2-2^n$.", duree=8),
        o("py3", r"Trouver $a\in\mathbb R$ pour que $Q=(X+1)^7-X^7-a$ ait une racine réelle au moins double.",
          r"$\alpha$ racine au moins double $\iff Q(\alpha)=Q'(\alpha)=0$. $Q'=7(X+1)^6-7X^6=0\iff X+1=\pm X\iff X=-\frac12$. $Q\left(-\frac12\right)=\frac1{128}+\frac1{128}-a=0$ donne $a=\frac1{64}$.", duree=8),
    ]},
]


# Variants (same method, other numbers): a failed exercise comes back with the next one; build.py checks calc == ans.
def _v(enonce, calc, ans, sol):
    return {"enonce": enonce, "calc": calc, "ans": ans, "sol": sol}


VARIANTS = {
    "pd1": [_v(r"$A=X^4-X$ et $B=X^3+2$. Quel est le degré de $AB$ ?", "degree((x**4-x)*(x**3+2), x)", "7", r"$4+3=7$.")],
    "pd2": [_v(r"$A=X^4+X^2$ et $B=-X^4+3X$. Quel est le degré de $A+B$ ?", "degree(x**4+x**2-x**4+3*x, x)", "2", r"$A+B=X^2+3X$, de degré $2$.")],
    "pd3": [_v(r"Développer $(X^2-1)(X+3)$.", "expand((x**2-1)*(x+3))", "x**3+3*x**2-x-3", r"$X^3+3X^2-X-3$.")],
    "pd4": [_v(r"Quel est le coefficient dominant de $(3X+1)^2$ ?", "LC((3*x+1)**2, x)", "9", r"$(3X)^2=9X^2$ : coefficient $9$.")],
    "pe1": [_v(r"Donner le quotient de la division euclidienne de $X^3-2X^2+3X-1$ par $X-2$ (et le reste).", "quo(x**3-2*x**2+3*x-1, x-2)", "x**2+3",
               r"$X^3-2X^2+3X-1=(X-2)(X^2+3)+5$ : $Q=X^2+3$, $R=5$.")],
    "pe2": [_v(r"Donner le reste de la division euclidienne de $X^4+X^2+1$ par $X^2-1$.", "rem(x**4+x**2+1, x**2-1)", "3",
               r"$X^4+X^2+1=(X^2-1)(X^2+2)+3$ : $R=3$.")],
    "pe3": [_v(r"Donner le quotient de la division euclidienne de $X^3+X+1$ par $X^2+1$ (et le reste).", "quo(x**3+x+1, x**2+1)", "x",
               r"$X^3+X+1=(X^2+1)X+1$ : $Q=X$, $R=1$.")],
    "pe4": [_v(r"Donner le reste de la division euclidienne de $X^4$ par $X^2+X+1$.", "rem(x**4, x**2+x+1)", "x",
               r"$X^4=(X^2+X+1)(X^2-X)+X$ : $R=X$.")],
    "pr1": [_v(r"Sans poser la division, donner le reste de $X^4-2X+3$ par $X+1$.", "rem(x**4-2*x+3, x+1)", "6", r"$P(-1)=1+2+3=6$.")],
    "pr2": [_v(r"Pour quelle valeur de $m$ le polynôme $X-2$ divise-t-il $X^3+mX-2$ ?", "-(x**3-2).subs(x,2)/2", "-3", r"$P(2)=8+2m-2=0\iff m=-3$.")],
    "pr3": [_v(r"Vérifier que $1$ est racine de $P=X^3-7X+6$, puis factoriser $P$.", "x**3-7*x+6", "(x-1)*(x-2)*(x+3)",
               r"$P(1)=1-7+6=0$. $P=(X-1)(X^2+X-6)=(X-1)(X-2)(X+3)$.")],
    "pm2": [_v(r"Quel est l'ordre de multiplicité de la racine $-1$ de $P=X^3+3X^2+3X+1$ ?", "roots(x**3+3*x**2+3*x+1)[-1]", "3",
               r"$P(-1)=0$, $P'(-1)=3-6+3=0$, $P''(-1)=-6+6=0$, $P'''=6\ne0$. Ordre $3$ : $P=(X+1)^3$.")],
    "pm3": [_v(r"Quel est l'ordre de multiplicité de la racine $2$ de $P=X^4-8X^3+24X^2-32X+16$ ?", "roots(x**4-8*x**3+24*x**2-32*x+16)[2]", "4",
               r"$P(2)=P'(2)=P''(2)=P'''(2)=0$ et $P^{(4)}=24\ne0$. Ordre $4$ : $P=(X-2)^4$.")],
    "pm4": [_v(r"Trouver $a$ et $b$ pour que $1$ soit racine double de $P=X^3+aX+b$.", "rem(x**3-3*x+2, (x-1)**2)", "0",
               r"$P'(1)=3+a=0$ donne $a=-3$. $P(1)=1-3+b=0$ donne $b=2$.")],
    "ps1": [_v(r"Donner le reste de la division euclidienne de $X^9$ par $X^2-1$.", "rem(x**9, x**2-1)", "x",
               r"$R(1)=1$ et $R(-1)=-1$ : $\alpha=1$, $\beta=0$. $R=X$.")],
    "ps2": [_v(r"Donner le reste de la division euclidienne de $X^5$ par $(X-1)(X-2)$.", "rem(x**5, (x-1)*(x-2))", "31*x-30",
               r"$\alpha+\beta=1$ et $2\alpha+\beta=32$ : $\alpha=31$, $\beta=-30$.")],
    "ps3": [_v(r"Donner le reste de la division euclidienne de $X^4$ par $(X-2)^2$.", "rem(x**4, (x-2)**2)", "32*x-48",
               r"$R=P'(2)(X-2)+P(2)=32(X-2)+16=32X-48$.")],
    "ps4": [_v(r"Donner le reste de la division euclidienne de $X^4-X$ par $(X-1)^2$.", "rem(x**4-x, (x-1)**2)", "3*x-3",
               r"$P(1)=0$, $P'(1)=4-1=3$. $R=3(X-1)=3X-3$.")],
    "pf1": [_v(r"Factoriser $X^3-2X^2-X+2$ dans $\mathbb R[X]$.", "x**3-2*x**2-x+2", "(x-2)*(x-1)*(x+1)",
               r"$2$ est racine. $P=(X-2)(X^2-1)=(X-2)(X-1)(X+1)$.")],
    "pf2": [_v(r"Factoriser $X^4-16$ en produit d'irréductibles de $\mathbb R[X]$.", "x**4-16", "(x-2)*(x+2)*(x**2+4)",
               r"$(X^2-4)(X^2+4)=(X-2)(X+2)(X^2+4)$, et $X^2+4$ est irréductible ($\Delta<0$).")],
    "pf3": [_v(r"Factoriser $X^3-8$ en produit d'irréductibles de $\mathbb R[X]$.", "x**3-8", "(x-2)*(x**2+2*x+4)",
               r"$2$ est racine : $(X-2)(X^2+2X+4)$. $\Delta=4-16=-12<0$ : irréductible.")],
    "pf5": [_v(r"Factoriser $X^4-3X^2-4$ en produit d'irréductibles de $\mathbb R[X]$.", "x**4-3*x**2-4", "(x-2)*(x+2)*(x**2+1)",
               r"Avec $Y=X^2$ : $(Y-4)(Y+1)$. Donc $(X-2)(X+2)(X^2+1)$.")],
    "pt1": [_v(r"Écrire $P=X^2+X+1$ en puissances de $X-2$.", "x**2+x+1", "7+5*(x-2)+(x-2)**2",
               r"$P(2)=7$, $P'(2)=5$, $\frac{P''(2)}2=1$. $P=7+5(X-2)+(X-2)^2$.")],
    "pt2": [_v(r"$P$ est de degré $2$, $P(0)=2$, $P'(0)=1$, $P''(0)=-4$. Donner $P$.", "2+x-4*x**2/factorial(2)", "2+x-2*x**2", r"$P=2+X-2X^2$.")],
    "pt3": [_v(r"On sait que $P^{(4)}(0)=48$. Quel est le coefficient de $X^4$ dans $P$ ?", "48/factorial(4)", "2", r"$a_4=\frac{48}{4!}=2$.")],
    "pt4": [_v(r"Écrire $X^3$ en puissances de $X-1$.", "x**3", "1+3*(x-1)+3*(x-1)**2+(x-1)**3",
               r"$P(1)=1$, $P'(1)=3$, $\frac{P''(1)}2=3$, $\frac{P'''}6=1$. $X^3=1+3(X-1)+3(X-1)^2+(X-1)^3$.")],
    "pz1": [_v(r"Décomposer en éléments simples $\dfrac1{(X-2)(X+2)}$.", "1/((x-2)*(x+2))", "1/(4*(x-2))-1/(4*(x+2))",
               r"Pôle $2$ : $\frac14$. Pôle $-2$ : $-\frac14$. $F=\frac{1/4}{X-2}-\frac{1/4}{X+2}$.")],
    "pz2": [_v(r"Décomposer en éléments simples $\dfrac{2X+1}{(X-1)(X-2)}$.", "(2*x+1)/((x-1)*(x-2))", "-3/(x-1)+5/(x-2)",
               r"Pôle $1$ : $\frac3{-1}=-3$. Pôle $2$ : $\frac51=5$. $F=-\frac3{X-1}+\frac5{X-2}$.")],
    "pz3": [_v(r"Décomposer en éléments simples $\dfrac{X^2}{X+2}$.", "x**2/(x+2)", "x-2+4/(x+2)",
               r"$X^2=(X+2)(X-2)+4$, donc $F=X-2+\frac4{X+2}$.")],
    "pz4": [_v(r"Calculer $\displaystyle\int_3^4\frac{dx}{x^2-4}$.", "integrate(1/(x**2-4), (x,3,4))", "log(Rational(5,3))/4",
               r"$\frac1{x^2-4}=\frac14\left(\frac1{x-2}-\frac1{x+2}\right)$. $\frac14\left[\ln\frac{x-2}{x+2}\right]_3^4=\frac14\left(\ln\frac13-\ln\frac15\right)=\frac14\ln\frac53$.")],
}
for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["id"] in VARIANTS:
            _e["variants"] = VARIANTS[_e["id"]]


EXTRA_PARTS = []

QUIZ = [
    {"notion": "degre", "type": "vf", "q": r"$\deg(A+B)=\max(\deg A,\deg B)$ pour tous polynômes $A$, $B$.", "bonne": False},
    {"notion": "degre", "type": "qcm", "q": r"$\deg A=3$, $\deg B=4$. Degré de $AB$ ?", "choix": [r"$7$", r"$12$", r"$4$", r"$3$"], "bonne": 0},
    {"notion": "division", "type": "qcm", "q": r"Dans $A=BQ+R$, la condition sur le reste est :",
     "choix": [r"$\deg R<\deg B$", r"$\deg R<\deg Q$", r"$\deg R\le\deg B$", r"$R=0$"], "bonne": 0},
    {"notion": "racine", "type": "qcm", "q": r"Le reste de la division de $P$ par $X-a$ est :", "choix": [r"$P(a)$", r"$P'(a)$", r"$0$", r"$P(-a)$"], "bonne": 0},
    {"notion": "racine", "type": "vf", "q": r"Si $P(1)=P(2)=0$ alors $(X-1)(X-2)$ divise $P$.", "bonne": True},
    {"notion": "multiplicite", "type": "qcm", "q": r"$a$ est racine au moins double de $P$ si et seulement si :",
     "choix": [r"$P(a)=P'(a)=0$", r"$P(a)=0$ et $P'(a)\ne0$", r"$P'(a)=P''(a)=0$", r"$P(a)^2=0$"], "bonne": 0},
    {"notion": "multiplicite", "type": "vf", "q": r"Si $P(a)=P'(a)=0$ et $P''(a)\ne0$, alors $a$ est racine d'ordre exactement $2$.", "bonne": True},
    {"notion": "reste", "type": "qcm", "q": r"Le reste de $P$ par $(X-a)^2$ est :",
     "choix": [r"$P'(a)(X-a)+P(a)$", r"$P(a)X+P'(a)$", r"$P(a)$", r"$P'(a)$"], "bonne": 0},
    {"notion": "factorisation", "type": "vf", "q": r"$X^2+X+1$ est irréductible dans $\mathbb R[X]$.", "bonne": True},
    {"notion": "factorisation", "type": "vf", "q": r"$X^4+1$ est irréductible dans $\mathbb R[X]$.", "bonne": False},
    {"notion": "taylor", "type": "qcm", "q": r"Le coefficient de $X^k$ dans $P$ vaut :",
     "choix": [r"$\frac{P^{(k)}(0)}{k!}$", r"$P^{(k)}(0)$", r"$k!\,P^{(k)}(0)$", r"$\frac{P(0)}{k!}$"], "bonne": 0},
    {"notion": "des", "type": "qcm", "q": r"Dans $\frac1{(X-1)(X+2)}$, le coefficient de $\frac1{X-1}$ vaut :",
     "choix": [r"$\frac13$", r"$-\frac13$", r"$1$", r"$\frac12$"], "bonne": 0},
]

_RAC = r"$P(a)=0\iff X-a\mid P$"
_MULT = r"$a$ racine d'ordre $m$ $\iff P(a)=\dots=P^{(m-1)}(a)=0$ et $P^{(m)}(a)\ne0$"
_DIV = r"$A=BQ+R$, $\deg R<\deg B$"
_R2 = r"reste par $(X-a)(X-b)$ : $R=\alpha X+\beta$, $R(a)=P(a)$, $R(b)=P(b)$"
_RD = r"reste par $(X-a)^2$ : $R=P'(a)(X-a)+P(a)$"
_IRR = r"$aX^2+bX+c$ irréductible dans $\mathbb R[X]$ $\iff\Delta=b^2-4ac<0$"
_TAY = r"$P(X)=\sum_k\frac{P^{(k)}(a)}{k!}(X-a)^k$"
_PS = r"pôle simple $a$ : coefficient $\left[(X-a)F\right](a)$"
FORMULES = {
    "pd1": r"$\deg(AB)=\deg A+\deg B$", "pd2": r"$\deg(A+B)\le\max(\deg A,\deg B)$, avec égalité si les degrés sont différents",
    "pd3": r"distributivité · $X^aX^b=X^{a+b}$", "pd4": r"coefficient dominant d'un produit = produit des coefficients dominants",
    "pe1": _DIV, "pe2": _DIV, "pe3": _DIV, "pe4": _DIV,
    "pr1": r"le reste de $P$ par $X-a$ est $P(a)$", "pr2": _RAC, "pr3": _RAC + " · " + _DIV,
    "pr4": r"$(X-a)(X-b)\mid P\iff P(a)=P(b)=0$ ($a\ne b$)", "pr5": r"$(X-a)(X-b)\mid P\iff P(a)=P(b)=0$ ($a\ne b$)",
    "pm1": _MULT + r" · $(X^n)'=nX^{n-1}$", "pm2": _MULT, "pm3": _MULT,
    "pm4": r"$a$ racine au moins double $\iff P(a)=P'(a)=0$",
    "pm5": r"$P=(X-a)^mQ$ avec $Q(a)\ne0$ · $(uv)'=u'v+uv'$",
    "ps1": _R2, "ps2": _R2, "ps3": _RD, "ps4": _RD,
    "pf1": _RAC + r" · $X^2-a^2=(X-a)(X+a)$", "pf2": r"$X^2-a^2=(X-a)(X+a)$ · " + _IRR,
    "pf3": _RAC + " · " + _DIV + " · " + _IRR, "pf4": _DIV + " · " + _IRR, "pf5": r"poser $Y=X^2$ · " + _IRR,
    "pt1": _TAY, "pt2": _TAY, "pt3": r"$a_k=\frac{P^{(k)}(0)}{k!}$", "pt4": _TAY + r" · $(X^n)^{(k)}=\frac{n!}{(n-k)!}X^{n-k}$",
    "pz1": _PS, "pz2": _PS, "pz3": r"si $\deg N\ge\deg D$ : " + _DIV + r", $\frac AB=Q+\frac RB$",
    "pz4": _PS + r" · $\int\frac{dx}{x-a}=\ln|x-a|$ · $\ln a-\ln b=\ln\frac ab$",
    "pz5": _PS + r" · facteur $X^2+1$ : $\frac{bX+c}{X^2+1}$",
    "pz6": r"pôle double : $\frac{c_1}{X-a}+\frac{c_2}{(X-a)^2}$, $c_2=\left[(X-a)^2F\right](a)$ · " + _PS + r" · limite de $xF(x)$ en $+\infty$",
    "px2": r"$B\mid A\iff\exists Q,\ A=BQ$ · racine d'ordre $\ge2$ de $P$ $\Rightarrow$ racine de $P'$ · $(X-a)(X-b)\mid P\iff P(a)=P(b)=0$ · $\deg(AB)=\deg A+\deg B$ · $\int X^n=\frac{X^{n+1}}{n+1}$",
    "px3": _R2,
    "py1": r"racine d'ordre $\ge2$ de $P$ $\Rightarrow$ racine de $P'$ · $\int X^n=\frac{X^{n+1}}{n+1}$",
    "py2": _RD + " · " + _R2 + r" · $(X^n)'=nX^{n-1}$",
    "py3": r"$\alpha$ racine au moins double $\iff Q(\alpha)=Q'(\alpha)=0$ · $((X+1)^7)'=7(X+1)^6$ · $u^6=v^6\iff u=\pm v$ (réels)",
}
