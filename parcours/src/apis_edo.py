"""Level path: S1 maths, ECUE APIS, part 3: équations différentielles linéaires (1er et 2nd ordre).

Taught S5-B2 (6-11 déc.), chapter "23_Cours 5 - Equations différentielles (S2)". Calibrated on
Examen S2-B3-APEF mars 2025 (ex. 2) and mars 2024 (ex. 3), read on the PDF.
`ode` exercises: the general solution `f` (constants C1, C2) is plugged into `lhs`
(Y0 = y, Y1 = y', Y2 = y'') by build.py and must give 0; the number of constants must equal the order.
"""

SUBJECT = {
    "id": "maths-s1-apis-edo",
    "ordre": 150,
    "matiere": "maths",
    "semestre": "S1",
    "ecue": "APIS",
    "titre": "Équations différentielles (vues en déc., évaluées au S2)",
    "chapitres_moodle": ["23_Cours 5 - Equations différentielles (S2)"],
    "td": "TD EDO (S2 2030)",
    "examens": ["Examen B2 S1 (APIS)", "Examen S2-B3 APEF"],
}

NOTIONS = [
    {"id": "ordre1-homogene", "titre": "1er ordre homogène à coefficient constant",
     "formule": r"$y'=ay\iff y=Ce^{ax}$, $C\in\mathbb R$",
     "exemple": r"$2y'-y=0$ : $y'=\frac12y$, $y=Ce^{x/2}$",
     "cours": r"Mettre l'équation sous la forme $y'=ay$ (diviser par le coefficient de $y'$). Les solutions forment une droite : $Ce^{ax}$. Ne jamais oublier la constante $C$."},
    {"id": "solution-generale", "titre": "Solution générale = homogène + particulière",
     "formule": r"$y=y_h+y_p$ : toutes les solutions de l'équation homogène, plus une solution particulière de l'équation complète · $y'=ay+b$ ($a\ne0$) : $y=Ce^{ax}-\frac ba$",
     "exemple": r"$y'+2y=6$ : $y_p=3$, $y=Ce^{-2x}+3$",
     "cours": r"Pour une équation linéaire avec second membre : résoudre l'équation homogène, trouver **une** solution particulière, additionner. Second membre constant : chercher $y_p$ constante. Polynôme : $y_p$ polynôme de même degré. $e^{mx}$ : $y_p=\lambda e^{mx}$, ou $\lambda xe^{mx}$ si $m$ est solution de l'homogène (résonance)."},
    {"id": "ordre1-variable", "titre": "$y'+a(x)y=0$",
     "formule": r"$y=Ce^{-A(x)}$ où $A$ est une primitive de $a$",
     "exemple": r"$y'+2xy=0$ : $y=Ce^{-x^2}$",
     "cours": r"Sur un intervalle où le coefficient de $y'$ ne s'annule pas, diviser pour obtenir $y'+a(x)y=0$. Une primitive de $\tan$ est $-\ln\cos$, de $\frac{2x}{1+x^2}$ est $\ln(1+x^2)$, de $-\frac1x$ est $-\ln x$ sur $]0,+\infty[$."},
    {"id": "variation-constante", "titre": "Variation de la constante",
     "formule": r"$y_p=C(x)y_h(x)$ dans $y'+a(x)y=b(x)$ donne $C'(x)y_h(x)=b(x)$, donc $C(x)=\int\frac{b(x)}{y_h(x)}\,dx$",
     "exemple": r"$y'+y=e^{-x}$ : $C'e^{-x}=e^{-x}$, $C=x+K$, $y=(x+K)e^{-x}$",
     "cours": r"On remplace la constante par une fonction : les termes en $C$ se simplifient, il reste $C'y_h=b$ (si l'équation est normalisée). On intègre $C'$, sans oublier la nouvelle constante $K$. Astuce : $(x^2+1)y'+2xy$ ou $(e^x+1)y'+e^xy$ est la dérivée d'un produit."},
    {"id": "cauchy", "titre": "Condition initiale",
     "formule": r"$y(x_0)=y_0$ (et $y'(x_0)=y_1$ à l'ordre 2) fixe les constantes",
     "exemple": r"$y'+2y=6$, $y(0)=1$ : $C+3=1$, $C=-2$",
     "cours": r"Écrire d'abord la solution générale, **puis** utiliser les conditions. À l'ordre 2, deux conditions donnent un système de deux équations en $C_1$, $C_2$. Le problème de Cauchy a une unique solution."},
    {"id": "ordre2-homogene", "titre": "2nd ordre homogène : équation caractéristique",
     "formule": r"$y''+ay'+by=0$, $r^2+ar+b=0$ : $\Delta>0$ : $C_1e^{r_1x}+C_2e^{r_2x}$ · $\Delta=0$ : $(C_1+C_2x)e^{rx}$ · $\Delta<0$, $r=\alpha\pm i\beta$ : $e^{\alpha x}(C_1\cos\beta x+C_2\sin\beta x)$",
     "exemple": r"$y''+y'+y=0$ : $r=-\frac12\pm i\frac{\sqrt3}2$",
     "cours": r"Toujours deux constantes. Si $\Delta<0$, les solutions réelles utilisent la partie réelle $\alpha$ dans l'exponentielle et la partie imaginaire $\beta$ dans $\cos$, $\sin$. $y''+\omega^2y=0$ : $C_1\cos\omega x+C_2\sin\omega x$."},
    {"id": "ordre2-particuliere", "titre": "2nd ordre : solution particulière",
     "formule": r"constante $c$ : $y_p=\frac cb$ si $b\ne0$ · polynôme : $y_p$ polynôme · $e^{mx}$ : $\lambda e^{mx}$ si $m$ n'est pas racine de l'équation caractéristique, $\lambda xe^{mx}$ si $m$ est racine simple, $\lambda x^2e^{mx}$ si $m$ est racine double",
     "exemple": r"$y''+y'+y=x+1$ : $y_p=x$",
     "cours": r"Second membre polynôme de degré $d$ (avec $b\ne0$) : $y_p$ polynôme de degré $d$, on identifie les coefficients. $e^{mx}$ : si $m$ n'est pas racine, $y_p=\lambda e^{mx}$ ; racine simple : $\lambda xe^{mx}$ ; racine double : $\lambda x^2e^{mx}$. $\cos\omega x$ quand $\pm i\omega$ sont racines : $y_p=x(a\cos\omega x+b\sin\omega x)$."},
]


def ode(id, enonce, lhs, f, sol, src=None, duree=None):
    e = {"id": id, "kind": "ode", "enonce": enonce, "lhs": lhs, "f": f, "sol": sol}
    if src:
        e["src"] = src
    if duree:
        e["duree"] = duree
    return e


def v(id, enonce, calc, ans, sol, src=None, duree=None):
    e = {"id": id, "kind": "value", "enonce": enonce, "calc": calc, "ans": ans, "sol": sol}
    if src:
        e["src"] = src
    if duree:
        e["duree"] = duree
    return e


A25 = "Examen S2-B3-APEF mars 2025"
A24 = "Examen S2-B3-APEF mars 2024"

LEVELS = [
    {"n": 1, "titre": "y' = ay", "notions": ["ordre1-homogene"], "exos": [
        ode("e1", r"Résoudre $y'=3y$ sur $\mathbb R$.", "Y1-3*Y0", "C1*exp(3*x)", r"$y=Ce^{3x}$, $C\in\mathbb R$.", duree=2),
        ode("e2", r"Résoudre $y'+2y=0$ sur $\mathbb R$.", "Y1+2*Y0", "C1*exp(-2*x)", r"$y'=-2y$ : $y=Ce^{-2x}$.", duree=2),
        ode("e3", r"Résoudre $2y'-y=0$ sur $\mathbb R$.", "2*Y1-Y0", "C1*exp(x/2)", r"$y'=\frac12y$ : $y=Ce^{x/2}$.", duree=2),
        ode("e4", r"Résoudre $4y'+y=0$ sur $\mathbb R$.", "4*Y1+Y0", "C1*exp(-x/4)", r"$y'=-\frac14y$ : $y=Ce^{-x/4}$.", duree=2),
    ]},
    {"n": 2, "titre": "Second membre constant", "notions": ["solution-generale", "ordre1-homogene"], "exos": [
        ode("c1", r"Résoudre $y'+2y=6$.", "Y1+2*Y0-6", "C1*exp(-2*x)+3", r"$y_p=3$ (constante : $2y_p=6$). $y=Ce^{-2x}+3$.", duree=3),
        ode("c2", r"Trouver une solution particulière de $2y'+6y=-3$ puis résoudre sur $\mathbb R$.", "2*Y1+6*Y0+3",
            "C1*exp(-3*x)-Rational(1,2)", r"Constante : $6y_p=-3$, $y_p=-\frac12$. Homogène $y'=-3y$. $y=Ce^{-3x}-\frac12$.",
            src=f"{A24}, ex. 3.1a", duree=3),
        ode("c3", r"Résoudre $y'-y=5$.", "Y1-Y0-5", "C1*exp(x)-5", r"$y_p=-5$, $y=Ce^x-5$.", duree=3),
    ]},
    {"n": 3, "titre": "Second membre polynôme ou exponentielle", "notions": ["solution-generale"], "exos": [
        ode("s1", r"Résoudre $y'+y=x$.", "Y1+Y0-x", "C1*exp(-x)+x-1",
            r"$y_p=ax+b$ : $a+ax+b=x$, $a=1$, $b=-1$. $y=Ce^{-x}+x-1$."),
        ode("s2", r"Trouver une solution particulière de $y'+y=e^x$ puis résoudre.", "Y1+Y0-exp(x)", "C1*exp(-x)+exp(x)/2",
            r"$y_p=\lambda e^x$ : $2\lambda=1$, $y_p=\frac{e^x}2$. $y=Ce^{-x}+\frac{e^x}2$.", src=f"{A24}, ex. 3.1b"),
        ode("s3", r"Résoudre $y'-2y=e^{2x}$.", "Y1-2*Y0-exp(2*x)", "C1*exp(2*x)+x*exp(2*x)",
            r"$2$ est la solution de l'homogène (résonance) : $y_p=\lambda xe^{2x}$, $y_p'-2y_p=\lambda e^{2x}$, $\lambda=1$. $y=(C+x)e^{2x}$."),
        ode("s4", r"Résoudre $y'+y=2x^2$.", "Y1+Y0-2*x**2", "C1*exp(-x)+2*x**2-4*x+4",
            r"$y_p=ax^2+bx+c$ : $ax^2+(2a+b)x+(b+c)=2x^2$ donne $a=2$, $b=-4$, $c=4$. $y=Ce^{-x}+2x^2-4x+4$."),
    ]},
    {"n": 4, "titre": "y' + a(x) y = 0", "notions": ["ordre1-variable"], "exos": [
        ode("a1", r"Résoudre $y'+2xy=0$ sur $\mathbb R$.", "Y1+2*x*Y0", "C1*exp(-x**2)", r"$A(x)=x^2$ : $y=Ce^{-x^2}$.", duree=3),
        ode("a2", r"Résoudre $y'-\frac yx=0$ sur $]0,+\infty[$.", "Y1-Y0/x", "C1*x", r"$A(x)=-\ln x$ : $y=Ce^{\ln x}=Cx$.", duree=3),
        ode("a3", r"Résoudre $(1+x^2)y'+2xy=0$ sur $\mathbb R$.", "(1+x**2)*Y1+2*x*Y0", "C1/(1+x**2)",
            r"$y'+\frac{2x}{1+x^2}y=0$, $A=\ln(1+x^2)$ : $y=\frac C{1+x^2}$.", duree=3),
        ode("a4", r"Résoudre $y'+\tan(x)\,y=0$ sur $\left]-\frac\pi2,\frac\pi2\right[$.", "Y1+tan(x)*Y0", "C1*cos(x)",
            r"Primitive de $\tan$ : $-\ln\cos x$ ($\cos>0$ ici). $y=Ce^{\ln\cos x}=C\cos x$.", duree=3),
    ]},
    {"n": 5, "titre": "Variation de la constante", "notions": ["variation-constante", "ordre1-variable"], "exos": [
        ode("v1", r"Résoudre $y'+y=e^{-x}$.", "Y1+Y0-exp(-x)", "(x+C1)*exp(-x)",
            r"$y_h=Ce^{-x}$ ; $y=C(x)e^{-x}$ donne $C'e^{-x}=e^{-x}$, $C=x+K$. $y=(x+K)e^{-x}$."),
        ode("v2", r"Résoudre $xy'-y=x^2$ sur $]0,+\infty[$.", "x*Y1-Y0-x**2", "x**2+C1*x",
            r"Homogène : $y=Cx$. $y=C(x)x$ : $x\cdot C'x=x^2$, $C'=1$, $C=x+K$. $y=x^2+Kx$."),
        ode("v3", r"Résoudre $(1+x^2)y'+2xy=1$ sur $\mathbb R$.", "(1+x**2)*Y1+2*x*Y0-1", "(x+C1)/(1+x**2)",
            r"Le membre de gauche est $\left((1+x^2)y\right)'$, donc $(1+x^2)y=x+C$, $y=\frac{x+C}{1+x^2}$."),
        ode("v4", r"Résoudre dans $]0,\pi[$ : $\sin(x)y'-\cos(x)y=x\sin^2(x)e^{-x}$.", "sin(x)*Y1-cos(x)*Y0-x*sin(x)**2*exp(-x)",
            "(C1-(x+1)*exp(-x))*sin(x)",
            r"Homogène : $y'=\frac{\cos x}{\sin x}y$, $y=C\sin x$. Variation : $C'\sin^2x=x\sin^2x\,e^{-x}$, $C'=xe^{-x}$. IPP : $C=-(x+1)e^{-x}+K$. $y=\left(K-(x+1)e^{-x}\right)\sin x$.",
            src=f"{A25}, ex. 2.2", duree=8),
        ode("v5", r"Résoudre dans $\mathbb R$ : $(e^x+1)y'+e^xy=\cos(3x)$.", "(exp(x)+1)*Y1+exp(x)*Y0-cos(3*x)",
            "(sin(3*x)/3+C1)/(exp(x)+1)",
            r"$\left((e^x+1)y\right)'=\cos3x$, donc $(e^x+1)y=\frac{\sin3x}3+C$, $y=\frac{\sin(3x)/3+C}{e^x+1}$ (même résultat par variation de la constante, $y_h=\frac C{e^x+1}$).",
            src=f"{A24}, ex. 3.3", duree=7),
    ]},
    {"n": 6, "titre": "Condition initiale (1er ordre)", "notions": ["cauchy", "solution-generale"], "exos": [
        v("k1", r"$y'+2y=6$, $y(0)=1$. Calculer $y(\ln2)$.", "-2*exp(-2*log(2))+3", "Rational(5,2)",
          r"$y=Ce^{-2x}+3$, $C+3=1$, $C=-2$. $y(\ln2)=-2\cdot\frac14+3=\frac52$.", duree=3),
        v("k2", r"$y'+y=x$, $y(0)=0$. Calculer $y(1)$.", "exp(-1)+1-1", "exp(-1)",
          r"$y=Ce^{-x}+x-1$, $C-1=0$, $C=1$. $y(1)=e^{-1}$.", duree=3),
        v("k3", r"$y'+2xy=0$, $y(0)=5$. Calculer $y(1)$.", "5*exp(-1)", "5/E", r"$y=5e^{-x^2}$, $y(1)=\frac5e$.", duree=2),
        v("k4", r"$y'=3y$, $y(1)=2$. Calculer $y(0)$.", "2*exp(-3)", "2/E**3", r"$Ce^3=2$, $C=2e^{-3}=y(0)$.", duree=2),
    ]},
    {"n": 7, "titre": "2nd ordre homogène, deux racines réelles", "notions": ["ordre2-homogene"], "exos": [
        ode("h1", r"Résoudre $y''-3y'+2y=0$.", "Y2-3*Y1+2*Y0", "C1*exp(x)+C2*exp(2*x)", r"$r^2-3r+2=(r-1)(r-2)$ : $y=C_1e^x+C_2e^{2x}$.", duree=3),
        ode("h2", r"Résoudre $y''-y=0$.", "Y2-Y0", "C1*exp(x)+C2*exp(-x)", r"$r=\pm1$ : $y=C_1e^x+C_2e^{-x}$.", duree=2),
        ode("h3", r"Résoudre $y''+y'-6y=0$.", "Y2+Y1-6*Y0", "C1*exp(2*x)+C2*exp(-3*x)", r"$r^2+r-6=(r-2)(r+3)$ : $y=C_1e^{2x}+C_2e^{-3x}$.", duree=3),
        ode("h4", r"Résoudre $y''-4y'=0$.", "Y2-4*Y1", "C1+C2*exp(4*x)", r"$r(r-4)=0$ : $y=C_1+C_2e^{4x}$.", duree=3),
    ]},
    {"n": 8, "titre": "2nd ordre homogène, racine double ou complexes", "notions": ["ordre2-homogene"], "exos": [
        ode("d1", r"Résoudre $y''-4y'+4y=0$.", "Y2-4*Y1+4*Y0", "(C1+C2*x)*exp(2*x)", r"$(r-2)^2=0$ : $y=(C_1+C_2x)e^{2x}$.", duree=3),
        ode("d2", r"Résoudre $y''+4y=0$.", "Y2+4*Y0", "C1*cos(2*x)+C2*sin(2*x)", r"$r=\pm2i$ : $y=C_1\cos2x+C_2\sin2x$.", duree=3),
        ode("d3", r"Résoudre $y''+2y'+5y=0$.", "Y2+2*Y1+5*Y0", "exp(-x)*(C1*cos(2*x)+C2*sin(2*x))",
            r"$\Delta=-16$, $r=-1\pm2i$ : $y=e^{-x}(C_1\cos2x+C_2\sin2x)$."),
        ode("d4", r"Résoudre $y''+y'+y=0$.", "Y2+Y1+Y0", "exp(-x/2)*(C1*cos(sqrt(3)*x/2)+C2*sin(sqrt(3)*x/2))",
            r"$\Delta=-3$, $r=-\frac12\pm i\frac{\sqrt3}2$ : $y=e^{-x/2}\left(C_1\cos\frac{\sqrt3x}2+C_2\sin\frac{\sqrt3x}2\right)$."),
    ]},
    {"n": 9, "titre": "2nd ordre avec second membre", "notions": ["ordre2-particuliere", "ordre2-homogene"], "exos": [
        ode("p1", r"$(E)$ : $y''-6y'+9y=3$. Trouver une solution particulière évidente, puis résoudre $(E)$ dans $\mathbb R$.",
            "Y2-6*Y1+9*Y0-3", "(C1+C2*x)*exp(3*x)+Rational(1,3)",
            r"$y_p=\frac13$ (constante : $9y_p=3$). $r^2-6r+9=(r-3)^2$ : $y=(C_1+C_2x)e^{3x}+\frac13$.", src=f"{A25}, ex. 2.1"),
        ode("p2", r"Trouver une solution particulière de $y''+y'+y=x+1$, puis résoudre dans $\mathbb R$.", "Y2+Y1+Y0-x-1",
            "exp(-x/2)*(C1*cos(sqrt(3)*x/2)+C2*sin(sqrt(3)*x/2))+x",
            r"$y_p=x$ : $0+1+x=x+1$. $y=e^{-x/2}\left(C_1\cos\frac{\sqrt3x}2+C_2\sin\frac{\sqrt3x}2\right)+x$.", src=f"{A24}, ex. 3.1c-3.2"),
        ode("p3", r"Résoudre $y''-3y'+2y=e^{3x}$.", "Y2-3*Y1+2*Y0-exp(3*x)", "C1*exp(x)+C2*exp(2*x)+exp(3*x)/2",
            r"$3$ n'est pas racine : $y_p=\lambda e^{3x}$, $(9-9+2)\lambda=1$, $\lambda=\frac12$."),
        ode("p4", r"Résoudre $y''+y=x^2$.", "Y2+Y0-x**2", "C1*cos(x)+C2*sin(x)+x**2-2",
            r"$y_p=ax^2+bx+c$ : $2a+ax^2+bx+c=x^2$, $a=1$, $b=0$, $c=-2$. $y=C_1\cos x+C_2\sin x+x^2-2$."),
        ode("p5", r"Résoudre $y''-y=e^x$.", "Y2-Y0-exp(x)", "C1*exp(x)+C2*exp(-x)+x*exp(x)/2",
            r"$1$ est racine simple : $y_p=\lambda xe^x$, $y_p''-y_p=2\lambda e^x$, $\lambda=\frac12$."),
        ode("p6", r"Résoudre $y''+4y'+4y=e^{-2x}$.", "Y2+4*Y1+4*Y0-exp(-2*x)", "(C1+C2*x+x**2/2)*exp(-2*x)",
            r"$r^2+4r+4=(r+2)^2$ : $-2$ est racine double, donc $y_p=\lambda x^2e^{-2x}$ et on trouve $2\lambda=1$. $y=\left(C_1+C_2x+\frac{x^2}2\right)e^{-2x}$."),
    ]},
    {"n": 10, "titre": "Conditions initiales (2nd ordre)", "notions": ["cauchy", "ordre2-homogene"], "exos": [
        v("q1", r"$y''-y=0$, $y(0)=1$, $y'(0)=0$. Calculer $y(\ln2)$.", "(exp(log(2))+exp(-log(2)))/2", "Rational(5,4)",
          r"$C_1+C_2=1$, $C_1-C_2=0$ : $y=\frac{e^x+e^{-x}}2$, $y(\ln2)=\frac{2+1/2}2=\frac54$."),
        v("q2", r"$y''+4y=0$, $y(0)=0$, $y'(0)=2$. Calculer $y\left(\frac\pi4\right)$.", "sin(2*pi/4)", "1",
          r"$C_1=0$, $2C_2=2$ : $y=\sin2x$, $y\left(\frac\pi4\right)=1$.", duree=3),
        v("q3", r"$y''-3y'+2y=0$, $y(0)=0$, $y'(0)=1$. Calculer $y(\ln3)$.", "exp(2*log(3))-exp(log(3))", "6",
          r"$C_1+C_2=0$, $C_1+2C_2=1$ : $C_2=1$, $C_1=-1$, $y=e^{2x}-e^x$, $y(\ln3)=9-3=6$."),
    ]},
    {"n": 11, "titre": "Niveau examen : annales complètes", "notions": ["variation-constante", "ordre2-particuliere"], "examen": True, "exos": [
        {"id": "ex25", "kind": "multi", "src": f"{A25}, ex. 2 (10 points)",
         "enonce": r"1. $(E)$ : $y''-6y'+9y=3$. (a) Solution particulière évidente. (b) Résoudre dans $\mathbb R$." "\n"
                   r"2. Résoudre dans $]0,\pi[$ : $\sin(x)y'-\cos(x)y=x\sin^2(x)e^{-x}$.",
         "parts": ["p1", "v4"]},
        {"id": "ex24", "kind": "multi", "src": f"{A24}, ex. 3 (9 points)",
         "enonce": r"1. Solution particulière de : (a) $2y'+6y=-3$ ; (b) $y'+y=e^x$ ; (c) $y''+y'+y=x+1$." "\n"
                   r"2. Résoudre $y''+y'+y=x+1$ dans $\mathbb R$." "\n" r"3. Résoudre $(e^x+1)y'+e^xy=\cos(3x)$ dans $\mathbb R$.",
         "parts": ["c2", "s2", "p2", "v5"]},
        {"id": "exmix", "kind": "multi", "src": "Type annale",
         "enonce": r"1. Résoudre $y'-2y=e^{2x}$. 2. Résoudre $y''-y=e^x$. 3. $y''-3y'+2y=0$, $y(0)=0$, $y'(0)=1$ : $y(\ln3)$ ?",
         "parts": ["s3", "p5", "q3"]},
    ]},
    {"n": 12, "titre": "Examen + 20 %", "notions": ["ordre2-particuliere", "variation-constante"], "examen": True, "exos": [
        ode("x1", r"Résoudre $y''-2y'+y=e^x$.", "Y2-2*Y1+Y0-exp(x)", "(C1+C2*x+x**2/2)*exp(x)",
            r"$1$ est racine double : $y_p=\lambda x^2e^x$, on trouve $2\lambda=1$. $y=\left(C_1+C_2x+\frac{x^2}2\right)e^x$."),
        ode("x2", r"Résoudre $y''+y=\cos x$.", "Y2+Y0-cos(x)", "C1*cos(x)+C2*sin(x)+x*sin(x)/2",
            r"$\pm i$ sont racines : $y_p=x(a\cos x+b\sin x)$ ; on trouve $a=0$, $b=\frac12$. $y=C_1\cos x+C_2\sin x+\frac{x\sin x}2$."),
        ode("x3", r"Résoudre $x^2y'+y=1$ sur $]0,+\infty[$.", "x**2*Y1+Y0-1", "1+C1*exp(1/x)",
            r"$y'+\frac1{x^2}y=0$ : $A=-\frac1x$, $y_h=Ce^{1/x}$ ; $y_p=1$. $y=1+Ce^{1/x}$."),
        ode("x4", r"Résoudre $y'-y=\sin x$.", "Y1-Y0-sin(x)", "C1*exp(x)-(cos(x)+sin(x))/2",
            r"$y_p=a\cos x+b\sin x$ : $(-a-b)\sin x+(b-a)\cos x=\sin x$, $a=b=-\frac12$. $y=Ce^x-\frac{\cos x+\sin x}2$."),
    ]},
]


# Variants (same method, other numbers): a failed exercise comes back with the next one; build.py checks each with sympy.
def _o(enonce, lhs, f, sol):
    return {"enonce": enonce, "lhs": lhs, "f": f, "sol": sol}


def _v(enonce, calc, ans, sol):
    return {"enonce": enonce, "calc": calc, "ans": ans, "sol": sol}


VARIANTS = {
    "e1": [_o(r"Résoudre $y'=-5y$ sur $\mathbb R$.", "Y1+5*Y0", "C1*exp(-5*x)", r"$y=Ce^{-5x}$, $C\in\mathbb R$.")],
    "e2": [_o(r"Résoudre $y'-4y=0$ sur $\mathbb R$.", "Y1-4*Y0", "C1*exp(4*x)", r"$y'=4y$ : $y=Ce^{4x}$.")],
    "e3": [_o(r"Résoudre $3y'+y=0$ sur $\mathbb R$.", "3*Y1+Y0", "C1*exp(-x/3)", r"$y'=-\frac13y$ : $y=Ce^{-x/3}$.")],
    "e4": [_o(r"Résoudre $5y'-2y=0$ sur $\mathbb R$.", "5*Y1-2*Y0", "C1*exp(2*x/5)", r"$y'=\frac25y$ : $y=Ce^{2x/5}$.")],
    "c1": [_o(r"Résoudre $y'+3y=12$.", "Y1+3*Y0-12", "C1*exp(-3*x)+4", r"$y_p=4$ ($3y_p=12$). $y=Ce^{-3x}+4$.")],
    "c2": [_o(r"Trouver une solution particulière de $3y'-6y=4$ puis résoudre sur $\mathbb R$.", "3*Y1-6*Y0-4", "C1*exp(2*x)-Rational(2,3)",
              r"$y_p$ constante : $-6y_p=4$, $y_p=-\frac23$. $y=Ce^{2x}-\frac23$.")],
    "c3": [_o(r"Résoudre $y'-2y=8$.", "Y1-2*Y0-8", "C1*exp(2*x)-4", r"$y_p=-4$, $y=Ce^{2x}-4$.")],
    "s1": [_o(r"Résoudre $y'+2y=4x$.", "Y1+2*Y0-4*x", "C1*exp(-2*x)+2*x-1",
              r"$y_p=ax+b$ : $a+2ax+2b=4x$, donc $a=2$, $b=-1$. $y=Ce^{-2x}+2x-1$.")],
    "s2": [_o(r"Trouver une solution particulière de $y'+2y=e^x$ puis résoudre.", "Y1+2*Y0-exp(x)", "C1*exp(-2*x)+exp(x)/3",
              r"$y_p=ae^x$ : $3a=1$. $y=Ce^{-2x}+\frac{e^x}3$.")],
    "s3": [_o(r"Résoudre $y'+3y=e^{-3x}$.", "Y1+3*Y0-exp(-3*x)", "C1*exp(-3*x)+x*exp(-3*x)",
              r"Second membre solution de l'homogène : $y_p=xe^{-3x}$. $y=(x+C)e^{-3x}$.")],
    "s4": [_o(r"Résoudre $y'-y=x^2$.", "Y1-Y0-x**2", "C1*exp(x)-x**2-2*x-2",
              r"$y_p=ax^2+bx+c$ : $-a=1$, $2a-b=0$, $b-c=0$, donc $y_p=-x^2-2x-2$. $y=Ce^x-x^2-2x-2$.")],
    "a1": [_o(r"Résoudre $y'-3x^2y=0$ sur $\mathbb R$.", "Y1-3*x**2*Y0", "C1*exp(x**3)", r"$A(x)=-x^3$ : $y=Ce^{x^3}$.")],
    "a2": [_o(r"Résoudre $y'+\frac yx=0$ sur $]0,+\infty[$.", "Y1+Y0/x", "C1/x", r"$A(x)=\ln x$ : $y=Ce^{-\ln x}=\frac Cx$.")],
    "a3": [_o(r"Résoudre $(1+x^2)y'-2xy=0$ sur $\mathbb R$.", "(1+x**2)*Y1-2*x*Y0", "C1*(1+x**2)",
              r"$y'=\frac{2x}{1+x^2}y$, $A(x)=-\ln(1+x^2)$ : $y=C(1+x^2)$.")],
    "a4": [_o(r"Résoudre $y'-\tan(x)\,y=0$ sur $\left]-\frac\pi2,\frac\pi2\right[$.", "Y1-tan(x)*Y0", "C1/cos(x)",
              r"$A(x)=\ln\cos x$ : $y=Ce^{-\ln\cos x}=\frac C{\cos x}$.")],
    "v1": [_o(r"Résoudre $y'-2y=e^{2x}$.", "Y1-2*Y0-exp(2*x)", "(x+C1)*exp(2*x)", r"$y=C(x)e^{2x}$ : $C'(x)=1$, $y=(x+C)e^{2x}$.")],
    "v2": [_o(r"Résoudre $xy'+y=x^2$ sur $]0,+\infty[$.", "x*Y1+Y0-x**2", "x**2/3+C1/x",
              r"$(xy)'=x^2$ donc $xy=\frac{x^3}3+C$ et $y=\frac{x^2}3+\frac Cx$.")],
    "v3": [_o(r"Résoudre $(1+x^2)y'+2xy=2x$ sur $\mathbb R$.", "(1+x**2)*Y1+2*x*Y0-2*x", "(x**2+C1)/(1+x**2)",
              r"$\big((1+x^2)y\big)'=2x$ : $y=\frac{x^2+C}{1+x^2}$.")],
    "v4": [_o(r"Résoudre dans $\left]-\frac\pi2,\frac\pi2\right[$ : $\cos(x)y'+\sin(x)y=\cos^2(x)$.", "cos(x)*Y1+sin(x)*Y0-cos(x)**2", "(x+C1)*cos(x)",
              r"Homogène : $y=C\cos x$. Variation : $C'(x)\cos^2x=\cos^2x$, $C(x)=x+C$ : $y=(x+C)\cos x$.")],
    "v5": [_o(r"Résoudre dans $\mathbb R$ : $(e^x+1)y'+e^xy=\sin(2x)$.", "(exp(x)+1)*Y1+exp(x)*Y0-sin(2*x)", "(C1-cos(2*x)/2)/(exp(x)+1)",
              r"$\big((e^x+1)y\big)'=\sin2x$ : $(e^x+1)y=-\frac{\cos2x}2+C$.")],
    "k1": [_v(r"$y'+3y=6$, $y(0)=0$. Calculer $y(\ln2)$.", "2-2*exp(-3*log(2))", "Rational(7,4)",
              r"$y=2-2e^{-3x}$, $y(\ln2)=2-\frac28=\frac74$.")],
    "k2": [_v(r"$y'+y=2x$, $y(0)=0$. Calculer $y(1)$.", "2*1-2+2*exp(-1)", "2*exp(-1)", r"$y=2x-2+2e^{-x}$, $y(1)=\frac2e$.")],
    "k3": [_v(r"$y'+2xy=0$, $y(0)=3$. Calculer $y(2)$.", "3*exp(-4)", "3/E**4", r"$y=3e^{-x^2}$, $y(2)=3e^{-4}$.")],
    "k4": [_v(r"$y'=2y$, $y(1)=5$. Calculer $y(0)$.", "5*exp(-2)", "5/E**2", r"$Ce^2=5$, $y(0)=C=5e^{-2}$.")],
    "h1": [_o(r"Résoudre $y''-5y'+6y=0$.", "Y2-5*Y1+6*Y0", "C1*exp(2*x)+C2*exp(3*x)", r"$(r-2)(r-3)$ : $y=C_1e^{2x}+C_2e^{3x}$.")],
    "h2": [_o(r"Résoudre $y''-9y=0$.", "Y2-9*Y0", "C1*exp(3*x)+C2*exp(-3*x)", r"$r=\pm3$ : $y=C_1e^{3x}+C_2e^{-3x}$.")],
    "h3": [_o(r"Résoudre $y''-y'-2y=0$.", "Y2-Y1-2*Y0", "C1*exp(2*x)+C2*exp(-x)", r"$(r-2)(r+1)$ : $y=C_1e^{2x}+C_2e^{-x}$.")],
    "h4": [_o(r"Résoudre $y''+3y'=0$.", "Y2+3*Y1", "C1+C2*exp(-3*x)", r"$r(r+3)=0$ : $y=C_1+C_2e^{-3x}$.")],
    "d1": [_o(r"Résoudre $y''+6y'+9y=0$.", "Y2+6*Y1+9*Y0", "(C1+C2*x)*exp(-3*x)", r"$(r+3)^2=0$ : $y=(C_1+C_2x)e^{-3x}$.")],
    "d2": [_o(r"Résoudre $y''+9y=0$.", "Y2+9*Y0", "C1*cos(3*x)+C2*sin(3*x)", r"$r=\pm3i$ : $y=C_1\cos3x+C_2\sin3x$.")],
    "d3": [_o(r"Résoudre $y''-2y'+5y=0$.", "Y2-2*Y1+5*Y0", "exp(x)*(C1*cos(2*x)+C2*sin(2*x))",
              r"$r=1\pm2i$ : $y=e^x(C_1\cos2x+C_2\sin2x)$.")],
    "d4": [_o(r"Résoudre $y''-y'+y=0$.", "Y2-Y1+Y0", "exp(x/2)*(C1*cos(sqrt(3)*x/2)+C2*sin(sqrt(3)*x/2))",
              r"$r=\frac12\pm i\frac{\sqrt3}2$ : $y=e^{x/2}\left(C_1\cos\frac{\sqrt3x}2+C_2\sin\frac{\sqrt3x}2\right)$.")],
    "p1": [_o(r"$(E)$ : $y''-4y'+4y=8$. Trouver une solution particulière évidente, puis résoudre $(E)$ dans $\mathbb R$.", "Y2-4*Y1+4*Y0-8",
              "(C1+C2*x)*exp(2*x)+2", r"$y_p=2$ ; $(r-2)^2$ : $y=(C_1+C_2x)e^{2x}+2$.")],
    "p2": [_o(r"Trouver une solution particulière de $y''+2y'+y=x$, puis résoudre dans $\mathbb R$.", "Y2+2*Y1+Y0-x", "(C1+C2*x)*exp(-x)+x-2",
              r"$y_p=ax+b$ : $2a+ax+b=x$, $a=1$, $b=-2$. $y=(C_1+C_2x)e^{-x}+x-2$.")],
    "p3": [_o(r"Résoudre $y''-3y'+2y=e^{-x}$.", "Y2-3*Y1+2*Y0-exp(-x)", "C1*exp(x)+C2*exp(2*x)+exp(-x)/6",
              r"$y_p=ae^{-x}$ : $a(1+3+2)=1$, $a=\frac16$.")],
    "p4": [_o(r"Résoudre $y''+4y=x$.", "Y2+4*Y0-x", "C1*cos(2*x)+C2*sin(2*x)+x/4", r"$y_p=\frac x4$ : $y=C_1\cos2x+C_2\sin2x+\frac x4$.")],
    "p5": [_o(r"Résoudre $y''-4y=e^{2x}$.", "Y2-4*Y0-exp(2*x)", "C1*exp(2*x)+C2*exp(-2*x)+x*exp(2*x)/4",
              r"$2$ racine simple : $y_p=axe^{2x}$, $4a=1$. $y=C_1e^{2x}+C_2e^{-2x}+\frac x4e^{2x}$.")],
    "p6": [_o(r"Résoudre $y''-6y'+9y=e^{3x}$.", "Y2-6*Y1+9*Y0-exp(3*x)", "(C1+C2*x+x**2/2)*exp(3*x)",
              r"$3$ racine double : $y_p=ax^2e^{3x}$, $2a=1$. $y=\left(C_1+C_2x+\frac{x^2}2\right)e^{3x}$.")],
    "q1": [_v(r"$y''-4y=0$, $y(0)=1$, $y'(0)=0$. Calculer $y(\ln2)$.", "(exp(2*log(2))+exp(-2*log(2)))/2", "Rational(17,8)",
              r"$y=\frac{e^{2x}+e^{-2x}}2$, $y(\ln2)=\frac{4+1/4}2=\frac{17}8$.")],
    "q2": [_v(r"$y''+9y=0$, $y(0)=0$, $y'(0)=3$. Calculer $y\left(\frac\pi{18}\right)$.", "sin(3*pi/18)", "Rational(1,2)",
              r"$y=\sin3x$, $y\left(\frac\pi{18}\right)=\sin\frac\pi6=\frac12$.")],
    "q3": [_v(r"$y''-5y'+6y=0$, $y(0)=0$, $y'(0)=1$. Calculer $y(\ln2)$.", "exp(3*log(2))-exp(2*log(2))", "4",
              r"$y=e^{3x}-e^{2x}$, $y(\ln2)=8-4=4$.")],
    "x1": [_o(r"Résoudre $y''-4y'+4y=e^{2x}$.", "Y2-4*Y1+4*Y0-exp(2*x)", "(C1+C2*x+x**2/2)*exp(2*x)",
              r"Racine double $2$ : $y_p=\frac{x^2}2e^{2x}$.")],
    "x2": [_o(r"Résoudre $y''+4y=\cos(2x)$.", "Y2+4*Y0-cos(2*x)", "C1*cos(2*x)+C2*sin(2*x)+x*sin(2*x)/4",
              r"Résonance : $y_p=\frac x4\sin2x$.")],
    "x3": [_o(r"Résoudre $x^2y'-y=-1$ sur $]0,+\infty[$.", "x**2*Y1-Y0+1", "1+C1*exp(-1/x)",
              r"$y_p=1$ ; homogène $y'=\frac y{x^2}$, $y=Ce^{-1/x}$.")],
    "x4": [_o(r"Résoudre $y'+y=\sin x$.", "Y1+Y0-sin(x)", "C1*exp(-x)+(sin(x)-cos(x))/2",
              r"$y_p=a\cos x+b\sin x$ : $a=-\frac12$, $b=\frac12$. $y=Ce^{-x}+\frac{\sin x-\cos x}2$.")],
}
for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["id"] in VARIANTS:
            _e["variants"] = VARIANTS[_e["id"]]


EXTRA_PARTS = []

QUIZ = [
    {"notion": "ordre1-homogene", "type": "qcm", "q": r"Solutions de $y'=-2y$ ?",
     "choix": [r"$Ce^{-2x}$", r"$Ce^{2x}$", r"$e^{-2x}+C$", r"$-2Ce^x$"], "bonne": 0},
    {"notion": "ordre1-homogene", "type": "vf", "q": r"$y=e^{3x}$ est la seule solution de $y'=3y$.", "bonne": False},
    {"notion": "solution-generale", "type": "qcm", "q": r"Solution particulière de $y'+2y=6$ ?",
     "choix": [r"$3$", r"$6$", r"$e^{-2x}$", r"$6x$"], "bonne": 0},
    {"notion": "solution-generale", "type": "vf", "q": r"La solution générale est la somme des solutions homogènes et d'une solution particulière.", "bonne": True},
    {"notion": "solution-generale", "type": "qcm", "q": r"Forme de $y_p$ pour $y'-2y=e^{2x}$ ?",
     "choix": [r"$\lambda xe^{2x}$", r"$\lambda e^{2x}$", r"$\lambda$", r"$\lambda x$"], "bonne": 0},
    {"notion": "ordre1-variable", "type": "qcm", "q": r"Solutions de $y'+2xy=0$ ?",
     "choix": [r"$Ce^{-x^2}$", r"$Ce^{-2x}$", r"$Ce^{x^2}$", r"$Cx^2$"], "bonne": 0},
    {"notion": "ordre1-variable", "type": "vf", "q": r"Sur $]-\frac\pi2,\frac\pi2[$, une primitive de $\tan$ est $-\ln(\cos x)$.", "bonne": True},
    {"notion": "variation-constante", "type": "qcm", "q": r"$y'+y=e^{-x}$, $y=C(x)e^{-x}$ : $C'(x)=$ ?",
     "choix": [r"$1$", r"$e^{-x}$", r"$e^{-2x}$", r"$x$"], "bonne": 0},
    {"notion": "variation-constante", "type": "vf", "q": r"$(1+x^2)y'+2xy$ est la dérivée de $(1+x^2)y$.", "bonne": True},
    {"notion": "cauchy", "type": "qcm", "q": r"$y=Ce^{-2x}+3$, $y(0)=1$ : $C=$ ?",
     "choix": [r"$-2$", r"$1$", r"$4$", r"$-3$"], "bonne": 0},
    {"notion": "ordre2-homogene", "type": "qcm", "q": r"Solutions de $y''+4y=0$ ?",
     "choix": [r"$C_1\cos2x+C_2\sin2x$", r"$C_1e^{2x}+C_2e^{-2x}$", r"$(C_1+C_2x)e^{2x}$", r"$C\cos2x$"], "bonne": 0},
    {"notion": "ordre2-homogene", "type": "qcm", "q": r"$r^2-4r+4=0$ : solutions de l'équation ?",
     "choix": [r"$(C_1+C_2x)e^{2x}$", r"$C_1e^{2x}+C_2e^{-2x}$", r"$Ce^{2x}$", r"$C_1\cos2x+C_2\sin2x$"], "bonne": 0},
    {"notion": "ordre2-homogene", "type": "vf", "q": r"$r=-1\pm2i$ : $y=e^{-x}(C_1\cos2x+C_2\sin2x)$.", "bonne": True},
    {"notion": "ordre2-particuliere", "type": "qcm", "q": r"Solution particulière de $y''+y'+y=x+1$ ?",
     "choix": [r"$x$", r"$x+1$", r"$1$", r"$\frac{x}{2}$"], "bonne": 0},
    {"notion": "ordre2-particuliere", "type": "vf", "q": r"Pour $y''-y=e^x$, on cherche $y_p=\lambda e^x$.", "bonne": False},
]

# Formulas used in each solution (help « Formules de la solution »); multi exercises get those of their parts.
_H1 = r"$y'=ay\iff y=Ce^{ax}$, $C\in\mathbb R$"
_GEN = r"solution générale = solution de l'homogène + une solution particulière : $y=y_h+y_p$"
_VAR = r"$y'+a(x)y=0\iff y=Ce^{-A(x)}$, $A$ primitive de $a$"
_VC = r"variation de la constante : $y=C(x)\,y_h(x)$, on trouve $C'(x)\,y_h(x)=$ second membre (équation mise sous la forme $y'+a(x)y=b(x)$)"
_PROD = r"reconnaître $(uy)'=u'y+uy'$ à gauche, puis intégrer"
_CAR = r"équation caractéristique $ar^2+br+c=0$"
_R2 = _CAR + r" · $\Delta>0$ : $y=C_1e^{r_1x}+C_2e^{r_2x}$"
_R0 = _CAR + r" · $\Delta=0$ : $y=(C_1+C_2x)e^{rx}$"
_RC = _CAR + r" · $\Delta<0$, $r=\alpha\pm i\beta$ : $y=e^{\alpha x}(C_1\cos\beta x+C_2\sin\beta x)$"
_PCST = r"second membre constant : chercher $y_p$ constante"
_PPOL = r"second membre polynôme : chercher $y_p$ polynôme de même degré"
_PEXP = r"second membre $e^{mx}$ : $y_p=\lambda e^{mx}$ si $m$ n'est pas racine, $\lambda xe^{mx}$ si racine simple, $\lambda x^2e^{mx}$ si racine double"
_CI = r"les conditions initiales fixent les constantes"
FORMULES = {
    "e1": _H1, "e2": _H1, "e3": _H1, "e4": _H1,
    "c1": _GEN + " · " + _PCST + " · " + _H1,
    "c2": _GEN + " · " + _PCST + " · " + _H1,
    "c3": _GEN + " · " + _PCST + " · " + _H1,
    "s1": _GEN + " · " + _PPOL + " · " + _H1,
    "s2": _GEN + " · " + _PEXP + " · " + _H1,
    "s3": _GEN + " · " + _PEXP + " · " + _H1,
    "s4": _GEN + " · " + _PPOL + " · " + _H1,
    "a1": _VAR,
    "a2": _VAR + r" · $\int\frac{dx}x=\ln x$ ($x>0$)",
    "a3": _VAR + r" · $\int\frac{u'}u=\ln|u|$",
    "a4": _VAR + r" · $\int\tan x\,dx=-\ln|\cos x|$",
    "v1": _H1 + " · " + _VC,
    "v2": _VAR + " · " + _VC,
    "v3": _PROD,
    "v4": _VAR + " · " + _VC + r" · IPP : $\int u'v=uv-\int uv'$",
    "v5": _PROD + r" · $\int\cos(ax)\,dx=\frac{\sin(ax)}a$",
    "k1": _GEN + " · " + _PCST + " · " + _CI + r" : $y(x_0)=y_0$",
    "k2": _GEN + " · " + _PPOL + " · " + _CI + r" : $y(x_0)=y_0$",
    "k3": _VAR + " · " + _CI + r" : $y(x_0)=y_0$",
    "k4": _H1 + " · " + _CI + r" : $y(x_0)=y_0$",
    "h1": _R2, "h2": _R2, "h3": _R2, "h4": _R2,
    "d1": _R0, "d2": _RC, "d3": _RC, "d4": _RC,
    "p1": _GEN + " · " + _PCST + " · " + _R0,
    "p2": _GEN + " · " + _PPOL + " · " + _RC,
    "p3": _GEN + " · " + _PEXP + " · " + _R2,
    "p4": _GEN + " · " + _PPOL + " · " + _RC,
    "p5": _GEN + " · " + _PEXP + " · " + _R2,
    "p6": _GEN + " · " + _PEXP + " · " + _R0,
    "q1": _R2 + " · " + _CI + r" : $y(0)$ et $y'(0)$ donnent un système en $C_1$, $C_2$",
    "q2": _RC + " · " + _CI + r" : $y(0)$ et $y'(0)$ donnent un système en $C_1$, $C_2$",
    "q3": _R2 + " · " + _CI + r" : $y(0)$ et $y'(0)$ donnent un système en $C_1$, $C_2$",
    "x1": _GEN + " · " + _PEXP + " · " + _R0,
    "x2": _GEN + " · " + _RC + r" · second membre $\cos\beta x$ avec $\pm i\beta$ racines : $y_p=x(a\cos\beta x+b\sin\beta x)$",
    "x3": _VAR + " · " + _GEN + " · " + _PCST,
    "x4": _GEN + " · " + _H1 + r" · second membre $\sin x$ : $y_p=a\cos x+b\sin x$",
}
