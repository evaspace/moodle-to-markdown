"""Subject « Bases maths »: calculation basics (lycée prerequisites used by every S1 subject).

Fractions, powers, roots, expanding/factoring, quadratics, divisions, equations, absolute value,
sums, exp, ln, trigonometry, usual derivatives and limits. One chapter = one level path (bases_<key>.py stubs call chapter()).
Not tied to an exam: these are the
prerequisite paths linked from « Notions de base à revoir » (levels.PREREQ).
Every `value`/`derivative` answer is checked by build.py with sympy, variants included.
"""

NOTIONS = [
    {"id": "fractions", "titre": "Fractions",
     "formule": r"$\frac ab+\frac cd=\frac{ad+bc}{bd}$ · $\frac ab\times\frac cd=\frac{ac}{bd}$ · $\frac{a/b}{c/d}=\frac ab\times\frac dc$",
     "exemple": r"$\frac23+\frac14=\frac{8+3}{12}=\frac{11}{12}$",
     "cours": r"Pour additionner, mettre au même dénominateur (le plus petit multiple commun suffit). Pour multiplier, numérateurs entre eux et dénominateurs entre eux. Diviser par une fraction, c'est multiplier par son inverse. Simplifier en divisant haut et bas par le même facteur, jamais en barrant des termes d'une somme."},
    {"id": "puissances", "titre": "Puissances",
     "formule": r"$a^na^m=a^{n+m}$ · $\frac{a^n}{a^m}=a^{n-m}$ · $(a^n)^m=a^{nm}$ · $(ab)^n=a^nb^n$ · $a^{-n}=\frac1{a^n}$ · $a^0=1$",
     "exemple": r"$\frac{2^5\times2^{-2}}{2^4}=2^{5-2-4}=\frac12$",
     "cours": r"Les règles ne valent que pour une même base (produit) ou un même exposant ($(ab)^n$). Il n'y a pas de règle pour $a^n+a^m$ : on factorise, $2^5+2^3=2^3(2^2+1)$. $a^{1/2}=\sqrt a$ et $a^{p/q}=\sqrt[q]{a^p}$ pour $a>0$."},
    {"id": "racines", "titre": "Racines carrées",
     "formule": r"$\sqrt{ab}=\sqrt a\sqrt b$ · $\sqrt{\frac ab}=\frac{\sqrt a}{\sqrt b}$ · $\sqrt{a^2}=|a|$ · $\frac1{\sqrt a-\sqrt b}=\frac{\sqrt a+\sqrt b}{a-b}$",
     "exemple": r"$\sqrt{50}=\sqrt{25\times2}=5\sqrt2$",
     "cours": r"Pour simplifier $\sqrt n$, sortir le plus grand carré qui divise $n$. $\sqrt{a+b}\neq\sqrt a+\sqrt b$. Pour enlever une racine d'un dénominateur, multiplier haut et bas par la quantité conjuguée : $(\sqrt a-\sqrt b)(\sqrt a+\sqrt b)=a-b$."},
    {"id": "developper", "titre": "Développer",
     "formule": r"$(a+b)^2=a^2+2ab+b^2$ · $(a-b)^2=a^2-2ab+b^2$ · $(a+b)(a-b)=a^2-b^2$ · $(a+b)^3=a^3+3a^2b+3ab^2+b^3$",
     "exemple": r"$(2x-3)^2=4x^2-12x+9$",
     "cours": r"Double distributivité : $(a+b)(c+d)=ac+ad+bc+bd$. Le signe moins devant une parenthèse change tous les signes à l'intérieur. Les identités remarquables évitent de tout distribuer."},
    {"id": "factoriser", "titre": "Factoriser",
     "formule": r"$ka+kb=k(a+b)$ · $a^2-b^2=(a-b)(a+b)$ · $a^2\pm2ab+b^2=(a\pm b)^2$ · $a^3-b^3=(a-b)(a^2+ab+b^2)$",
     "exemple": r"$x^2-9=(x-3)(x+3)$ ; $(x+1)^2-4=(x-1)(x+3)$",
     "cours": r"Ordre des réflexes : facteur commun, puis identité remarquable, puis racine évidente d'un polynôme (si $P(a)=0$, $P(x)=(x-a)Q(x)$). Une expression factorisée sert à trouver le signe et les zéros."},
    {"id": "trinome", "titre": "Trinôme du second degré",
     "formule": r"$\Delta=b^2-4ac$ · $\Delta>0$ : $x_{1,2}=\frac{-b\pm\sqrt\Delta}{2a}$ et $ax^2+bx+c=a(x-x_1)(x-x_2)$ · $\Delta=0$ : $a\left(x+\frac b{2a}\right)^2$ · $x_1+x_2=-\frac ba$, $x_1x_2=\frac ca$",
     "exemple": r"$x^2-5x+6$ : $\Delta=1$, racines 2 et 3, $=(x-2)(x-3)$",
     "cours": r"Le trinôme a le signe de $a$ à l'extérieur des racines et le signe opposé entre elles. Si $\Delta < 0$, pas de racine réelle et signe de $a$ partout. Racine évidente : essayer $1,-1,2$ puis utiliser le produit $\frac ca$ pour l'autre."},
    {"id": "fractions_alg", "titre": "Fractions rationnelles",
     "formule": r"$\frac{A}{B}+\frac{C}{D}=\frac{AD+BC}{BD}$ · $\frac{AC}{BC}=\frac AB$ si $C\neq0$",
     "exemple": r"$\frac1x-\frac1{x+1}=\frac{1}{x(x+1)}$",
     "cours": r"Même méthode que les fractions numériques, en gardant les dénominateurs factorisés. On ne simplifie que des facteurs communs. Préciser les valeurs interdites (dénominateur nul)."},
    {"id": "divisions", "titre": "Divisions euclidiennes",
     "formule": r"Entiers : $a=bq+r$, $0\le r < b$ · Polynômes : $A=BQ+R$, $\deg R < \deg B$",
     "exemple": r"$47=6\times7+5$ ; $x^2+3x+5=(x+1)(x+2)+3$",
     "cours": r"Pour les entiers : $q$ est la partie entière de $\frac ab$, puis $r=a-bq$. Pour les polynômes : diviser les termes de plus haut degré, multiplier, soustraire, recommencer tant que le degré du reste est au moins celui de $B$. Le reste de la division de $P$ par $x-a$ vaut $P(a)$."},
    {"id": "equations", "titre": "Équations et inéquations",
     "formule": r"$AB=0\iff A=0$ ou $B=0$ · $\frac AB=0\iff A=0$ et $B\neq0$ · multiplier une inégalité par un négatif la renverse",
     "exemple": r"$(x-1)(x+2)\le0\iff x\in[-2,1]$",
     "cours": r"Ne jamais diviser par une expression qui peut être nulle : factoriser à la place. Pour une inéquation, tout passer d'un côté, factoriser, puis tableau de signes (un facteur par ligne, valeurs interdites en double barre)."},
    {"id": "valeur_absolue", "titre": "Valeur absolue",
     "formule": r"$|a|=a$ si $a\ge0$, $-a$ sinon · $|x-a|\le r\iff a-r\le x\le a+r$ · $|ab|=|a||b|$ · $|a+b|\le|a|+|b|$",
     "exemple": r"$|x-3|\le2\iff1\le x\le5$",
     "cours": r"$|x-a|$ est la distance de $x$ à $a$. Pour une expression avec plusieurs valeurs absolues, découper selon le signe de chaque intérieur. $|x|=a$ ($a\ge0$) $\iff x=a$ ou $x=-a$."},
    {"id": "sommes", "titre": "Sommes",
     "formule": r"$\sum_{k=1}^nk=\frac{n(n+1)}2$ · $\sum_{k=1}^nk^2=\frac{n(n+1)(2n+1)}6$ · $\sum_{k=0}^nq^k=\frac{1-q^{n+1}}{1-q}$ ($q\neq1$) · $\sum_{k=1}^n(a_{k+1}-a_k)=a_{n+1}-a_1$",
     "exemple": r"$\sum_{k=0}^{9}2^k=2^{10}-1=1023$",
     "cours": r"Linéarité : $\sum(\lambda a_k+b_k)=\lambda\sum a_k+\sum b_k$. Une constante sommée de $k=p$ à $n$ donne $(n-p+1)\times$ la constante. Somme arithmétique : nombre de termes $\times\frac{\text{premier}+\text{dernier}}2$. Somme géométrique : premier terme $\times\frac{1-q^{\text{nb termes}}}{1-q}$. Télescopage : les termes intermédiaires s'annulent."},
    {"id": "exp", "titre": "Exponentielle",
     "formule": r"$e^{a+b}=e^ae^b$ · $e^{-a}=\frac1{e^a}$ · $(e^a)^n=e^{na}$ · $e^x>0$ · $e^a=e^b\iff a=b$",
     "exemple": r"$\frac{e^{2x}e^{3}}{e^{x}}=e^{x+3}$",
     "cours": r"Mêmes règles que les puissances. $e^x$ est strictement positive et croissante : $e^a\le e^b\iff a\le b$. Pour $e^{2x}-3e^x+2=0$, poser $X=e^x$ ($X>0$) et résoudre le trinôme."},
    {"id": "ln", "titre": "Logarithme népérien",
     "formule": r"$\ln(ab)=\ln a+\ln b$ · $\ln\frac ab=\ln a-\ln b$ · $\ln(a^n)=n\ln a$ · $\ln1=0$, $\ln e=1$ · $e^{\ln a}=a$ ($a>0$), $\ln(e^x)=x$",
     "exemple": r"$\ln8-\ln2=\ln4=2\ln2$",
     "cours": r"$\ln$ n'est défini que sur $]0,+\infty[$ : vérifier le domaine avant de résoudre. $\ln$ est croissante : $\ln a\le\ln b\iff a\le b$. $\ln(a+b)\neq\ln a+\ln b$. $a^b=e^{b\ln a}$ pour $a>0$."},
    {"id": "trigo", "titre": "Trigonométrie",
     "formule": r"$\cos^2x+\sin^2x=1$ · $\cos(a+b)=\cos a\cos b-\sin a\sin b$ · $\sin(a+b)=\sin a\cos b+\cos a\sin b$ · $\cos2a=2\cos^2a-1$ · $\sin2a=2\sin a\cos a$",
     "exemple": r"$\cos\frac\pi3=\frac12$, $\sin\frac\pi3=\frac{\sqrt3}2$, $\cos\frac\pi4=\frac{\sqrt2}2$",
     "cours": r"Valeurs à connaître en $0,\frac\pi6,\frac\pi4,\frac\pi3,\frac\pi2$ : $\sin$ vaut $\frac{\sqrt0}2,\frac{\sqrt1}2,\frac{\sqrt2}2,\frac{\sqrt3}2,\frac{\sqrt4}2$, $\cos$ dans l'autre sens. $\cos(-x)=\cos x$, $\sin(-x)=-\sin x$, $\cos(\pi-x)=-\cos x$, $\sin(\pi-x)=\sin x$. $\tan x=\frac{\sin x}{\cos x}$."},
    {"id": "derivees", "titre": "Dérivées usuelles",
     "formule": r"$(x^n)'=nx^{n-1}$ · $(e^u)'=u'e^u$ · $(\ln u)'=\frac{u'}u$ · $(uv)'=u'v+uv'$ · $\left(\frac uv\right)'=\frac{u'v-uv'}{v^2}$ · $(\sqrt u)'=\frac{u'}{2\sqrt u}$",
     "exemple": r"$(x^2e^x)'=(2x+x^2)e^x$",
     "cours": r"$(\cos u)'=-u'\sin u$, $(\sin u)'=u'\cos u$, $(u^n)'=nu'u^{n-1}$, $\left(\frac1u\right)'=-\frac{u'}{u^2}$. Toujours repérer la forme (produit, quotient, composée) avant de dériver."},
    {"id": "limites", "titre": "Limites usuelles",
     "formule": r"En $+\infty$ : $\frac{e^x}{x^n}\to+\infty$ · $\frac{\ln x}{x^n}\to0$ · $x^ne^{-x}\to0$ · en $0^+$ : $x\ln x\to0$ · $\frac{e^x-1}x\to1$, $\frac{\ln(1+x)}x\to1$, $\frac{\sin x}x\to1$ en 0",
     "exemple": r"$\lim_{x\to+\infty}\frac{3x^2+1}{x^2-5}=3$",
     "cours": r"Polynôme ou fraction rationnelle en $\pm\infty$ : factoriser par le terme de plus haut degré. Croissances comparées : l'exponentielle l'emporte sur les puissances, qui l'emportent sur le logarithme. Formes indéterminées : $\infty-\infty$, $0\times\infty$, $\frac\infty\infty$, $\frac00$."},
]

_FO = {n["id"]: n["formule"] for n in NOTIONS}


def v(id, enonce, calc, ans, sol, fo, var=(), duree=2):
    """Computed answer: build.py checks calc == ans (at sample points if x/n appear). var: (enonce, calc, ans, sol)."""
    e = {"id": id, "kind": "value", "enonce": enonce, "calc": calc, "ans": ans, "sol": sol, "_f": fo, "duree": duree}
    if var:
        e["variants"] = [{"enonce": a, "calc": b, "ans": c, "sol": d} for a, b, c, d in var]
    return e


def d(id, f, ans, enonce, sol, var=(), duree=2):
    """Derivative of f(x), checked with sympy. var: (f, ans, enonce, sol)."""
    e = {"id": id, "kind": "derivative", "f": f, "ans": ans, "enonce": enonce, "sol": sol, "_f": _FO["derivees"], "duree": duree}
    if var:
        e["variants"] = [{"f": a, "ans": b, "enonce": c, "sol": s} for a, b, c, s in var]
    return e


def o(id, enonce, sol, fo, duree=3):
    return {"id": id, "kind": "open", "enonce": enonce, "sol": sol, "_f": fo, "duree": duree}


F = _FO
# Exercise pool: grouped below into chapters (one level path each) by CHAPTERS.
_POOL = [
    {"n": 1, "titre": "Fractions", "notions": ["fractions"], "exos": [
        v("fr1", r"Calculer $\frac23+\frac34$.", "Rational(2,3)+Rational(3,4)", "Rational(17,12)",
          r"Dénominateur commun 12 : $\frac8{12}+\frac9{12}=\frac{17}{12}$.", F["fractions"],
          [(r"Calculer $\frac35+\frac16$.", "Rational(3,5)+Rational(1,6)", "Rational(23,30)", r"$\frac{18}{30}+\frac5{30}=\frac{23}{30}$.")]),
        v("fr2", r"Calculer $\frac56-\frac7{10}$.", "Rational(5,6)-Rational(7,10)", "Rational(2,15)",
          r"Dénominateur commun 30 : $\frac{25}{30}-\frac{21}{30}=\frac4{30}=\frac2{15}$.", F["fractions"],
          [(r"Calculer $\frac34-\frac56$.", "Rational(3,4)-Rational(5,6)", "Rational(-1,12)", r"$\frac9{12}-\frac{10}{12}=-\frac1{12}$.")]),
        v("fr3", r"Calculer $\frac{14}{15}\times\frac{25}{21}$ sous forme irréductible.", "Rational(14,15)*Rational(25,21)", "Rational(10,9)",
          r"Simplifier avant de multiplier : $\frac{2\times7}{3\times5}\times\frac{5\times5}{3\times7}=\frac{2\times5}{3\times3}=\frac{10}9$.", F["fractions"],
          [(r"Calculer $\frac{6}{35}\times\frac{14}{9}$.", "Rational(6,35)*Rational(14,9)", "Rational(4,15)", r"$\frac{2\cdot3}{5\cdot7}\times\frac{2\cdot7}{3\cdot3}=\frac4{15}$.")]),
        v("fr4", r"Calculer $\dfrac{\frac34}{\frac9{8}}$.", "Rational(3,4)/Rational(9,8)", "Rational(2,3)",
          r"Diviser, c'est multiplier par l'inverse : $\frac34\times\frac89=\frac{24}{36}=\frac23$.", F["fractions"],
          [(r"Calculer $\dfrac{\frac5{6}}{\frac{10}{9}}$.", "Rational(5,6)/Rational(10,9)", "Rational(3,4)", r"$\frac56\times\frac9{10}=\frac{45}{60}=\frac34$.")]),
        v("fr5", r"Calculer $\dfrac{1+\frac12}{1-\frac13}$.", "(1+Rational(1,2))/(1-Rational(1,3))", "Rational(9,4)",
          r"$\frac{3/2}{2/3}=\frac32\times\frac32=\frac94$.", F["fractions"],
          [(r"Calculer $\dfrac{2-\frac14}{\frac12+\frac13}$.", "(2-Rational(1,4))/(Rational(1,2)+Rational(1,3))", "Rational(21,10)",
            r"$\frac{7/4}{5/6}=\frac74\times\frac65=\frac{42}{20}=\frac{21}{10}$.")]),
    ]},
    {"n": 2, "titre": "Puissances", "notions": ["puissances"], "exos": [
        v("pu1", r"Écrire $\frac{2^5\times2^{-3}}{2^{4}}$ sous la forme $2^p$ et donner sa valeur.", "2**5*2**(-3)/2**4", "Rational(1,4)",
          r"$2^{5-3-4}=2^{-2}=\frac14$.", F["puissances"],
          [(r"Écrire $\frac{3^{-2}\times3^{7}}{3^{3}}$ sous la forme $3^p$ et donner sa valeur.", "3**(-2)*3**7/3**3", "9", r"$3^{-2+7-3}=3^2=9$.")]),
        v("pu2", r"Simplifier $\frac{(x^3)^2\,x^{-1}}{x^4}$ pour $x\neq0$.", "(x**3)**2*x**(-1)/x**4", "x",
          r"$x^{6-1-4}=x^1=x$.", F["puissances"],
          [(r"Simplifier $\frac{x^5(x^{-2})^3}{x^{-4}}$ pour $x\neq0$.", "x**5*(x**(-2))**3/x**(-4)", "x**3", r"$x^{5-6+4}=x^3$.")]),
        v("pu3", r"Calculer $\frac{6^3}{2^3\times3^2}$.", "6**3/(2**3*3**2)", "3",
          r"$6^3=2^3\cdot3^3$ donc $\frac{2^33^3}{2^33^2}=3$.", F["puissances"],
          [(r"Calculer $\frac{10^4}{2^3\times5^4}$.", "10**4/(2**3*5**4)", "2", r"$10^4=2^45^4$ donc $\frac{2^45^4}{2^35^4}=2$.")]),
        v("pu4", r"Factoriser puis calculer $2^{10}+2^{8}$.", "2**10+2**8", "2**8*5",
          r"$2^8(2^2+1)=5\times2^8=1280$. Aucune règle ne donne $2^{18}$.", F["puissances"],
          [(r"Factoriser puis calculer $3^{6}-3^{4}$.", "3**6-3**4", "3**4*8", r"$3^4(3^2-1)=8\times3^4=648$.")]),
        v("pu5", r"Calculer $8^{2/3}$ et $27^{-1/3}$.", "8**Rational(2,3)+27**Rational(-1,3)", "4+Rational(1,3)",
          r"$8^{2/3}=(\sqrt[3]8)^2=4$ et $27^{-1/3}=\frac1{\sqrt[3]{27}}=\frac13$ (le calcul vérifié est leur somme).", F["puissances"],
          [(r"Calculer $16^{3/4}$ et $32^{-1/5}$.", "16**Rational(3,4)+32**Rational(-1,5)", "8+Rational(1,2)", r"$(\sqrt[4]{16})^3=8$ et $\frac1{\sqrt[5]{32}}=\frac12$.")]),
    ]},
    {"n": 3, "titre": "Racines carrées", "notions": ["racines"], "exos": [
        v("ra1", r"Simplifier $\sqrt{72}$.", "sqrt(72)", "6*sqrt(2)", r"$72=36\times2$ : $\sqrt{72}=6\sqrt2$.", F["racines"],
          [(r"Simplifier $\sqrt{48}$.", "sqrt(48)", "4*sqrt(3)", r"$48=16\times3$ : $4\sqrt3$.")]),
        v("ra2", r"Simplifier $\sqrt{50}-2\sqrt{18}+\sqrt8$.", "sqrt(50)-2*sqrt(18)+sqrt(8)", "sqrt(2)",
          r"$5\sqrt2-2\cdot3\sqrt2+2\sqrt2=\sqrt2$.", F["racines"],
          [(r"Simplifier $\sqrt{12}+\sqrt{27}-\sqrt{75}$.", "sqrt(12)+sqrt(27)-sqrt(75)", "0", r"$2\sqrt3+3\sqrt3-5\sqrt3=0$.")]),
        v("ra3", r"Écrire $\frac{1}{\sqrt3-1}$ sans racine au dénominateur.", "1/(sqrt(3)-1)", "(sqrt(3)+1)/2",
          r"Conjugué : $\frac{\sqrt3+1}{(\sqrt3-1)(\sqrt3+1)}=\frac{\sqrt3+1}{3-1}=\frac{\sqrt3+1}2$.", F["racines"],
          [(r"Écrire $\frac{2}{\sqrt5+\sqrt3}$ sans racine au dénominateur.", "2/(sqrt(5)+sqrt(3))", "sqrt(5)-sqrt(3)",
            r"$\frac{2(\sqrt5-\sqrt3)}{5-3}=\sqrt5-\sqrt3$.")]),
        v("ra4", r"Développer $(2+\sqrt3)^2$.", "(2+sqrt(3))**2", "7+4*sqrt(3)", r"$4+4\sqrt3+3=7+4\sqrt3$.", F["racines"] + " · " + F["developper"],
          [(r"Développer $(\sqrt5-1)^2$.", "(sqrt(5)-1)**2", "6-2*sqrt(5)", r"$5-2\sqrt5+1=6-2\sqrt5$.")]),
        v("ra5", r"Calculer $\sqrt{(1-\sqrt2)^2}$.", "sqrt((1-sqrt(2))**2)", "sqrt(2)-1",
          r"$\sqrt{a^2}=|a|$ et $1-\sqrt2 < 0$ : $|1-\sqrt2|=\sqrt2-1$.", F["racines"],
          [(r"Calculer $\sqrt{(2-\sqrt5)^2}$.", "sqrt((2-sqrt(5))**2)", "sqrt(5)-2", r"$2 < \sqrt5$ donc $|2-\sqrt5|=\sqrt5-2$.")]),
    ]},
    {"n": 4, "titre": "Développer", "notions": ["developper"], "exos": [
        v("dv1", r"Développer $(3x-2)^2$.", "(3*x-2)**2", "9*x**2-12*x+4", r"$(a-b)^2$ : $9x^2-12x+4$.", F["developper"],
          [(r"Développer $(2x+5)^2$.", "(2*x+5)**2", "4*x**2+20*x+25", r"$4x^2+20x+25$.")]),
        v("dv2", r"Développer $(x-4)(x+4)$.", "(x-4)*(x+4)", "x**2-16", r"$(a-b)(a+b)=a^2-b^2$ : $x^2-16$.", F["developper"],
          [(r"Développer $(5-2x)(5+2x)$.", "(5-2*x)*(5+2*x)", "25-4*x**2", r"$25-4x^2$.")]),
        v("dv3", r"Développer $(2x+1)(x-3)$.", "(2*x+1)*(x-3)", "2*x**2-5*x-3", r"$2x^2-6x+x-3=2x^2-5x-3$.", F["developper"],
          [(r"Développer $(3x-1)(2x+4)$.", "(3*x-1)*(2*x+4)", "6*x**2+10*x-4", r"$6x^2+12x-2x-4=6x^2+10x-4$.")]),
        v("dv4", r"Développer $(x+2)^2-(x-1)(x+3)$.", "(x+2)**2-(x-1)*(x+3)", "2*x+7",
          r"$x^2+4x+4-(x^2+2x-3)=2x+7$ (le moins change tous les signes).", F["developper"],
          [(r"Développer $(2x-1)^2-(2x+1)(2x-3)$.", "(2*x-1)**2-(2*x+1)*(2*x-3)", "4", r"$4x^2-4x+1-(4x^2-4x-3)=4$.")]),
        v("dv5", r"Développer $(x+1)^3$.", "(x+1)**3", "x**3+3*x**2+3*x+1", r"$(a+b)^3$ : $x^3+3x^2+3x+1$.", F["developper"],
          [(r"Développer $(x-2)^3$.", "(x-2)**3", "x**3-6*x**2+12*x-8", r"$x^3-3\cdot2x^2+3\cdot4x-8$.")]),
    ]},
    {"n": 5, "titre": "Factoriser", "notions": ["factoriser"], "exos": [
        v("fa1", r"Factoriser $6x^2-9x$.", "6*x**2-9*x", "3*x*(2*x-3)", r"Facteur commun $3x$ : $3x(2x-3)$.", F["factoriser"],
          [(r"Factoriser $4x^3+10x^2$.", "4*x**3+10*x**2", "2*x**2*(2*x+5)", r"Facteur commun $2x^2$ : $2x^2(2x+5)$.")]),
        v("fa2", r"Factoriser $25x^2-4$.", "25*x**2-4", "(5*x-2)*(5*x+2)", r"$a^2-b^2$ avec $a=5x$, $b=2$ : $(5x-2)(5x+2)$.", F["factoriser"],
          [(r"Factoriser $9-16x^2$.", "9-16*x**2", "(3-4*x)*(3+4*x)", r"$(3-4x)(3+4x)$.")]),
        v("fa3", r"Factoriser $x^2-10x+25$.", "x**2-10*x+25", "(x-5)**2", r"$a^2-2ab+b^2$ : $(x-5)^2$.", F["factoriser"],
          [(r"Factoriser $4x^2+12x+9$.", "4*x**2+12*x+9", "(2*x+3)**2", r"$(2x)^2+2\cdot2x\cdot3+3^2=(2x+3)^2$.")]),
        v("fa4", r"Factoriser $(x+1)^2-9$.", "(x+1)**2-9", "(x-2)*(x+4)", r"$a^2-b^2$ avec $a=x+1$, $b=3$ : $(x+1-3)(x+1+3)=(x-2)(x+4)$.", F["factoriser"],
          [(r"Factoriser $(2x-1)^2-(x+2)^2$.", "(2*x-1)**2-(x+2)**2", "(x-3)*(3*x+1)", r"$(2x-1-x-2)(2x-1+x+2)=(x-3)(3x+1)$.")]),
        v("fa5", r"Factoriser $(x-2)(3x+1)+(x-2)(x+4)$.", "(x-2)*(3*x+1)+(x-2)*(x+4)", "(x-2)*(4*x+5)",
          r"Facteur commun $(x-2)$ : $(x-2)(3x+1+x+4)=(x-2)(4x+5)$.", F["factoriser"],
          [(r"Factoriser $(2x+1)^2-(2x+1)(x-3)$.", "(2*x+1)**2-(2*x+1)*(x-3)", "(2*x+1)*(x+4)", r"$(2x+1)(2x+1-x+3)=(2x+1)(x+4)$.")]),
        v("fa6", r"$P(x)=x^3-2x^2-x+2$. Vérifier que $1$ est racine puis factoriser $P$ complètement.", "x**3-2*x**2-x+2", "(x-1)*(x+1)*(x-2)",
          r"$P(1)=0$ donc $P=(x-1)(x^2-x-2)$, et $x^2-x-2=(x+1)(x-2)$ : $P=(x-1)(x+1)(x-2)$.", F["factoriser"] + " · " + F["trinome"],
          [(r"$P(x)=x^3+x^2-4x-4$. Trouver une racine évidente puis factoriser $P$.", "x**3+x**2-4*x-4", "(x+1)*(x-2)*(x+2)",
            r"$P(-1)=0$ : $P=(x+1)(x^2-4)=(x+1)(x-2)(x+2)$ (ou facteur commun par groupes : $x^2(x+1)-4(x+1)$).")], duree=3),
    ]},
    {"n": 6, "titre": "Trinôme du second degré", "notions": ["trinome"], "exos": [
        v("tr1", r"Calculer le discriminant de $2x^2-3x-5$ puis ses racines (donner leur produit).", "Rational(-1)*Rational(5,2)", "Rational(-5,2)",
          r"$\Delta=9+40=49$, racines $\frac{3\pm7}4$ : $-1$ et $\frac52$. Produit $-\frac52=\frac ca$.", F["trinome"],
          [(r"Racines de $3x^2+x-2$ (donner leur produit).", "Rational(-1)*Rational(2,3)", "Rational(-2,3)", r"$\Delta=1+24=25$, racines $\frac{-1\pm5}6$ : $-1$ et $\frac23$.")], duree=3),
        v("tr2", r"Factoriser $x^2+x-12$.", "x**2+x-12", "(x-3)*(x+4)", r"Racines de somme $-1$ et produit $-12$ : $3$ et $-4$. $(x-3)(x+4)$.", F["trinome"],
          [(r"Factoriser $x^2-7x+10$.", "x**2-7*x+10", "(x-2)*(x-5)", r"Somme 7, produit 10 : $2$ et $5$.")]),
        v("tr3", r"Factoriser $2x^2-x-1$.", "2*x**2-x-1", "(x-1)*(2*x+1)", r"$1$ racine évidente, l'autre $\frac ca=-\frac12$ : $2(x-1)(x+\frac12)=(x-1)(2x+1)$.", F["trinome"],
          [(r"Factoriser $3x^2+5x+2$.", "3*x**2+5*x+2", "(x+1)*(3*x+2)", r"$-1$ racine, l'autre $\frac ca\cdot\frac1{-1}=-\frac23$ : $(x+1)(3x+2)$.")]),
        v("tr4", r"Combien de racines réelles a $x^2-4x+7$ ? (donner $\Delta$)", "(-4)**2-4*1*7", "-12",
          r"$\Delta=16-28=-12 < 0$ : aucune racine réelle, et $x^2-4x+7>0$ pour tout $x$ (signe de $a$).", F["trinome"],
          [(r"Combien de racines réelles a $4x^2-4x+1$ ? (donner $\Delta$)", "(-4)**2-4*4*1", "0", r"$\Delta=0$ : racine double $\frac12$, $4x^2-4x+1=(2x-1)^2$.")]),
        o("tr5", r"Donner le signe de $-x^2+x+6$ selon $x$.",
          r"Racines $-2$ et $3$ ($\Delta=25$). $a=-1 < 0$ : négatif à l'extérieur des racines, positif entre. $-x^2+x+6>0\iff x\in\,]-2,3[$.", F["trinome"]),
    ]},
    {"n": 7, "titre": "Fractions rationnelles", "notions": ["fractions_alg"], "exos": [
        v("fa_1", r"Réduire au même dénominateur $\frac1x+\frac2{x+1}$.", "1/x+2/(x+1)", "(3*x+1)/(x*(x+1))",
          r"$\frac{(x+1)+2x}{x(x+1)}=\frac{3x+1}{x(x+1)}$, pour $x\notin\{0,-1\}$.", F["fractions_alg"],
          [(r"Réduire $\frac3{x-1}-\frac1{x}$.", "3/(x-1)-1/x", "(2*x+1)/(x*(x-1))", r"$\frac{3x-(x-1)}{x(x-1)}=\frac{2x+1}{x(x-1)}$.")]),
        v("fa_2", r"Simplifier $\frac{x^2-4}{x^2+2x}$.", "(x**2-4)/(x**2+2*x)", "(x-2)/x",
          r"$\frac{(x-2)(x+2)}{x(x+2)}=\frac{x-2}x$ pour $x\notin\{0,-2\}$.", F["fractions_alg"] + " · " + F["factoriser"],
          [(r"Simplifier $\frac{x^2-6x+9}{x^2-9}$.", "(x**2-6*x+9)/(x**2-9)", "(x-3)/(x+3)", r"$\frac{(x-3)^2}{(x-3)(x+3)}=\frac{x-3}{x+3}$.")]),
        v("fa_3", r"Écrire $\frac{1}{x}-\frac1{x+1}$ en une seule fraction.", "1/x-1/(x+1)", "1/(x*(x+1))",
          r"$\frac{x+1-x}{x(x+1)}=\frac1{x(x+1)}$ (identité utile pour les sommes télescopiques).", F["fractions_alg"],
          [(r"Écrire $\frac{1}{x-1}-\frac1{x+1}$ en une seule fraction.", "1/(x-1)-1/(x+1)", "2/(x**2-1)", r"$\frac{x+1-(x-1)}{(x-1)(x+1)}=\frac2{x^2-1}$.")]),
        v("fa_4", r"Trouver $a$ et $b$ tels que $\frac{x+3}{x+1}=a+\frac{b}{x+1}$ (donner $a+\frac b{x+1}$).", "(x+3)/(x+1)", "1+2/(x+1)",
          r"$x+3=(x+1)+2$ : $a=1$, $b=2$.", F["fractions_alg"] + " · " + F["divisions"],
          [(r"Écrire $\frac{2x-1}{x-2}$ sous la forme $a+\frac b{x-2}$.", "(2*x-1)/(x-2)", "2+3/(x-2)", r"$2x-1=2(x-2)+3$ : $a=2$, $b=3$.")]),
    ]},
    {"n": 8, "titre": "Divisions euclidiennes", "notions": ["divisions"], "exos": [
        v("di1", r"Division euclidienne de $157$ par $12$ : donner le reste.", "157-12*13", "1",
          r"$12\times13=156\le157 < 168$ : $q=13$, $r=1$.", F["divisions"],
          [(r"Division euclidienne de $250$ par $17$ : donner le reste.", "250-17*14", "12", r"$17\times14=238$ : $q=14$, $r=12$.")]),
        v("di2", r"Division euclidienne de $-23$ par $5$ : donner le quotient.", "floor(Rational(-23,5))", "-5",
          r"Le reste doit vérifier $0\le r < 5$ : $-23=5\times(-5)+2$, donc $q=-5$, $r=2$ (pas $q=-4$, $r=-3$).", F["divisions"],
          [(r"Division euclidienne de $-40$ par $7$ : donner le quotient.", "floor(Rational(-40,7))", "-6", r"$-40=7\times(-6)+2$.")]),
        v("di6", r"Reste de la division euclidienne de $2^{10}$ par $7$.", "Mod(2**10,7)", "2",
          r"$2^{10}=1024=7\times146+2$. Plus rapide : $2^3=8=7+1$, donc $2^9=(2^3)^3$ a pour reste 1 et $2^{10}$ a pour reste 2.", F["divisions"],
          [(r"Reste de la division euclidienne de $3^{5}$ par $4$.", "Mod(3**5,4)", "3", r"$243=4\times60+3$.")]),
    ]},
    {"n": 0, "titre": "Division des polynômes", "notions": ["divisions"], "exos": [
        v("di3", r"Diviser $x^3-3x^2+5x-2$ par $x-1$ : écrire $A=BQ+R$.", "x**3-3*x**2+5*x-2", "(x-1)*(x**2-2*x+3)+1",
          r"$x^3\div x=x^2$ ; reste $-2x^2+5x-2$ ; $-2x$ ; reste $3x-2$ ; $+3$ ; reste $1$. $Q=x^2-2x+3$, $R=1=A(1)$.", F["divisions"],
          [(r"Diviser $2x^3+x^2-4$ par $x+2$.", "2*x**3+x**2-4", "(x+2)*(2*x**2-3*x+6)-16", r"$Q=2x^2-3x+6$, $R=A(-2)=-16+4-4=-16$.")], duree=4),
        v("di4", r"Diviser $x^4+1$ par $x^2+1$.", "x**4+1", "(x**2+1)*(x**2-1)+2",
          r"$x^4+1=(x^2+1)(x^2-1)+2$ : $Q=x^2-1$, $R=2$ ($\deg R < 2$).", F["divisions"],
          [(r"Diviser $x^3+2x+1$ par $x^2+1$.", "x**3+2*x+1", "(x**2+1)*x+x+1", r"$Q=x$, $R=x+1$.")], duree=3),
        v("di5", r"Reste de la division de $P(x)=x^{5}-3x+4$ par $x-2$ (sans poser la division).", "2**5-3*2+4", "30",
          r"Le reste de la division par $x-a$ vaut $P(a)$ : $P(2)=32-6+4=30$.", F["divisions"],
          [(r"Reste de la division de $P(x)=x^{4}+2x^2-1$ par $x+1$.", "(-1)**4+2*(-1)**2-1", "2", r"$P(-1)=1+2-1=2$.")]),
    ]},
    {"n": 9, "titre": "Équations et inéquations", "notions": ["equations"], "exos": [
        v("eq1", r"Résoudre $\frac{3x-1}{2}=\frac{x+4}{3}$.", "Rational(11,7)", "Rational(11,7)",
          r"$3(3x-1)=2(x+4)$, $9x-3=2x+8$, $x=\frac{11}7$.", F["equations"],
          [(r"Résoudre $\frac{x+2}{4}=\frac{2x-1}{3}$.", "Rational(2,1)", "2", r"$3x+6=8x-4$, $x=2$.")]),
        o("eq2", r"Résoudre $x^2=3x$. Pourquoi ne pas diviser par $x$ ?",
          r"$x^2-3x=0\iff x(x-3)=0\iff x=0$ ou $x=3$. Diviser par $x$ perd la solution $0$.", F["equations"]),
        o("eq3", r"Résoudre $(2x-1)(x+3)\le0$.",
          r"Zéros $\frac12$ et $-3$. Tableau de signes : produit négatif entre les zéros. $S=\left[-3,\frac12\right]$.", F["equations"]),
        o("eq4", r"Résoudre $\frac{x-2}{x+1}\ge0$.",
          r"Zéro $2$, valeur interdite $-1$. Positif à l'extérieur : $S=\,]-\infty,-1[\,\cup[2,+\infty[$ ($-1$ exclu).", F["equations"]),
        o("eq5", r"Résoudre $\frac1x\le2$.",
          r"$\frac1x-2\le0\iff\frac{1-2x}{x}\le0$. Zéro $\frac12$, valeur interdite $0$ : $S=\,]-\infty,0[\,\cup\left[\frac12,+\infty\right[$. Erreur classique : multiplier par $x$ sans connaître son signe.", F["equations"]),
    ]},
    {"n": 10, "titre": "Valeur absolue", "notions": ["valeur_absolue"], "exos": [
        o("va1", r"Résoudre $|x-3|=5$.", r"$x-3=5$ ou $x-3=-5$ : $x=8$ ou $x=-2$.", F["valeur_absolue"], duree=2),
        o("va2", r"Résoudre $|2x+1|\le3$.", r"$-3\le2x+1\le3\iff-2\le x\le1$ : $S=[-2,1]$.", F["valeur_absolue"], duree=2),
        o("va3", r"Résoudre $|x+1|>2$.", r"$x+1>2$ ou $x+1 < -2$ : $S=\,]-\infty,-3[\,\cup\,]1,+\infty[$.", F["valeur_absolue"], duree=2),
        o("va4", r"Écrire $f(x)=|x-1|+|x+2|$ sans valeur absolue.",
          r"$x < -2$ : $-2x-1$. $-2\le x\le1$ : $3$. $x>1$ : $2x+1$.", F["valeur_absolue"]),
        v("va5", r"Calculer $|3-\pi|+|\pi-4|$.", "Abs(3-pi)+Abs(pi-4)", "1",
          r"$3 < \pi < 4$ : $(\pi-3)+(4-\pi)=1$.", F["valeur_absolue"],
          [(r"Calculer $|\sqrt2-2|+|1-\sqrt2|$.", "Abs(sqrt(2)-2)+Abs(1-sqrt(2))", "1", r"$(2-\sqrt2)+(\sqrt2-1)=1$.")]),
    ]},
    {"n": 11, "titre": "Sommes", "notions": ["sommes"], "exos": [
        v("so1", r"Calculer $\sum_{k=1}^{100}k$.", "summation(k,(k,1,100))", "5050", r"$\frac{100\times101}2=5050$.", F["sommes"],
          [(r"Calculer $\sum_{k=1}^{50}k$.", "summation(k,(k,1,50))", "1275", r"$\frac{50\times51}2=1275$.")]),
        v("so2", r"Calculer $\sum_{k=1}^{n}(2k+3)$ en fonction de $n$.", "summation(2*k+3,(k,1,n))", "n**2+4*n",
          r"Linéarité : $2\cdot\frac{n(n+1)}2+3n=n^2+4n$.", F["sommes"],
          [(r"Calculer $\sum_{k=1}^{n}(4k-1)$.", "summation(4*k-1,(k,1,n))", "2*n**2+n", r"$4\cdot\frac{n(n+1)}2-n=2n^2+n$.")]),
    ]},
    {"n": 0, "titre": "Sommes géométriques et télescopiques", "notions": ["sommes"], "exos": [
        v("so3", r"Calculer $\sum_{k=0}^{n}3^k$.", "summation(3**k,(k,0,n))", "(3**(n+1)-1)/2",
          r"Géométrique de raison 3, $n+1$ termes : $\frac{3^{n+1}-1}{3-1}$.", F["sommes"],
          [(r"Calculer $\sum_{k=0}^{n}\left(\frac12\right)^k$.", "summation((Rational(1,2))**k,(k,0,n))", "2-(Rational(1,2))**n",
            r"$\frac{1-(1/2)^{n+1}}{1/2}=2-\frac1{2^n}$.")]),
        v("so7", r"Calculer $\sum_{k=1}^{10}2^k$.", "summation(2**k,(k,1,10))", "2046",
          r"Premier terme $2$, raison 2, 10 termes : $2\cdot\frac{2^{10}-1}{2-1}=2046$.", F["sommes"],
          [(r"Calculer $\sum_{k=2}^{6}3^k$.", "summation(3**k,(k,2,6))", "1089", r"$9\cdot\frac{3^5-1}{3-1}=9\cdot121=1089$.")]),
    ]},
    {"n": 0, "titre": "Sommes usuelles et linéarité", "notions": ["sommes"], "exos": [
        v("so4", r"Calculer $\sum_{k=2}^{10}5$.", "summation(5,(k,2,10))", "45", r"$10-2+1=9$ termes : $9\times5=45$.", F["sommes"],
          [(r"Calculer $\sum_{k=0}^{n}7$.", "summation(7,(k,0,n))", "7*(n+1)", r"$n+1$ termes : $7(n+1)$.")]),
        v("so5", r"Calculer $\sum_{k=1}^{n}\frac1{k(k+1)}$ (écrire $\frac1{k(k+1)}=\frac1k-\frac1{k+1}$).", "summation(1/(k*(k+1)),(k,1,n))", "1-1/(n+1)",
          r"Télescopage : $\left(1-\frac12\right)+\left(\frac12-\frac13\right)+\dots=1-\frac1{n+1}$.", F["sommes"] + " · " + F["fractions_alg"],
          [(r"Calculer $\sum_{k=1}^{n}\left(\sqrt{k+1}-\sqrt k\right)$.", "summation(sqrt(k+1)-sqrt(k),(k,1,n))", "sqrt(n+1)-1",
            r"Télescopage : $\sqrt{n+1}-\sqrt1$.")], duree=3),
        v("so6", r"Calculer $\sum_{k=1}^{n}k^2$ pour $n=10$.", "summation(k**2,(k,1,10))", "385", r"$\frac{10\cdot11\cdot21}6=385$.", F["sommes"],
          [(r"Calculer $\sum_{k=1}^{20}k^2$.", "summation(k**2,(k,1,20))", "2870", r"$\frac{20\cdot21\cdot41}6=2870$.")]),
    ]},
    {"n": 12, "titre": "Exponentielle", "notions": ["exp"], "exos": [
        v("ex1", r"Simplifier $\frac{e^{3x}\,e^{-x}}{e^{x+1}}$.", "exp(3*x)*exp(-x)/exp(x+1)", "exp(x-1)", r"$e^{3x-x-x-1}=e^{x-1}$.", F["exp"],
          [(r"Simplifier $\frac{(e^{x})^3}{e^{2x-1}}$.", "exp(x)**3/exp(2*x-1)", "exp(x+1)", r"$e^{3x-2x+1}=e^{x+1}$.")]),
        v("ex2", r"Résoudre $e^{2x-1}=e^{x+3}$.", "4", "4", r"$\exp$ injective : $2x-1=x+3$, $x=4$.", F["exp"],
          [(r"Résoudre $e^{3x}=e^{1-x}$.", "Rational(1,4)", "Rational(1,4)", r"$3x=1-x$, $x=\frac14$.")]),
        v("ex3", r"Résoudre $e^{x}=5$.", "log(5)", "log(5)", r"$x=\ln5$.", F["exp"] + " · " + F["ln"],
          [(r"Résoudre $e^{2x}=3$.", "log(3)/2", "log(3)/2", r"$2x=\ln3$, $x=\frac{\ln3}2$.")]),
        o("ex4", r"Résoudre $e^{2x}-3e^x+2=0$.",
          r"$X=e^x>0$ : $X^2-3X+2=0$, $X=1$ ou $X=2$. Donc $x=0$ ou $x=\ln2$.", F["exp"] + " · " + F["trinome"]),
        o("ex5", r"Résoudre $e^{x^2}\le e^{4}$.", r"$\exp$ croissante : $x^2\le4\iff x\in[-2,2]$.", F["exp"], duree=2),
    ]},
    {"n": 13, "titre": "Logarithme", "notions": ["ln"], "exos": [
        v("ln1", r"Écrire $\ln 12-\ln3+\ln 2$ sous la forme $a\ln2$.", "log(12)-log(3)+log(2)", "3*log(2)", r"$\ln\frac{12\times2}3=\ln8=3\ln2$.", F["ln"],
          [(r"Écrire $\ln 50-2\ln5+\ln4$ sous la forme $a\ln2$.", "log(50)-2*log(5)+log(4)", "3*log(2)", r"$\ln\frac{50\cdot4}{25}=\ln8=3\ln2$.")]),
        v("ln2", r"Simplifier $\ln(e^3)+e^{\ln 2}-\ln\sqrt e$.", "log(exp(3))+exp(log(2))-log(sqrt(E))", "Rational(9,2)",
          r"$3+2-\frac12=\frac92$.", F["ln"],
          [(r"Simplifier $\ln\frac1{e^2}+e^{2\ln3}$.", "log(1/E**2)+exp(2*log(3))", "7", r"$-2+e^{\ln9}=-2+9=7$.")]),
        v("ln3", r"Résoudre $\ln(2x-1)=\ln(x+2)$.", "3", "3", r"Domaine $x>\frac12$. $2x-1=x+2$, $x=3$ (dans le domaine).", F["ln"],
          [(r"Résoudre $\ln(3x+1)=\ln(x+5)$.", "2", "2", r"Domaine $x>-\frac13$ ; $3x+1=x+5$, $x=2$.")]),
        o("ln4", r"Résoudre $\ln x+\ln(x-1)=\ln 2$.",
          r"Domaine $x>1$. $\ln(x(x-1))=\ln2\iff x^2-x-2=0$, $x=2$ ou $x=-1$. Seul $x=2$ est dans le domaine.", F["ln"] + " · " + F["trinome"]),
        o("ln5", r"Résoudre $\ln(x-2)\le0$.", r"Domaine $x>2$. $\ln(x-2)\le\ln1\iff x-2\le1$ : $S=\,]2,3]$.", F["ln"], duree=2),
        v("ln6", r"Écrire $2^{x}$ avec l'exponentielle puis calculer $\ln(2^{10})/\ln 2$.", "log(2**10)/log(2)", "10",
          r"$2^x=e^{x\ln2}$ ; $\ln(2^{10})=10\ln2$.", F["ln"] + " · " + F["exp"],
          [(r"Calculer $\frac{\ln 81}{\ln 3}$.", "log(81)/log(3)", "4", r"$\ln81=\ln3^4=4\ln3$.")]),
    ]},
    {"n": 14, "titre": "Trigonométrie", "notions": ["trigo"], "exos": [
        v("tg1", r"Calculer $\cos\frac\pi6+\sin\frac\pi6$.", "cos(pi/6)+sin(pi/6)", "(sqrt(3)+1)/2", r"$\frac{\sqrt3}2+\frac12$.", F["trigo"],
          [(r"Calculer $\cos\frac\pi4\,\sin\frac\pi4$.", "cos(pi/4)*sin(pi/4)", "Rational(1,2)", r"$\frac{\sqrt2}2\cdot\frac{\sqrt2}2=\frac12$.")]),
        v("tg2", r"Calculer $\cos\frac{2\pi}3$ et $\sin\frac{5\pi}6$ (donner leur somme).", "cos(2*pi/3)+sin(5*pi/6)", "0",
          r"$\cos(\pi-\frac\pi3)=-\frac12$, $\sin(\pi-\frac\pi6)=\frac12$ : somme $0$.", F["trigo"],
          [(r"Calculer $\cos\frac{3\pi}4+\sin\frac{3\pi}4$.", "cos(3*pi/4)+sin(3*pi/4)", "0", r"$-\frac{\sqrt2}2+\frac{\sqrt2}2=0$.")]),
        v("tg3", r"Sachant $\cos x=\frac35$ et $x\in\left]-\frac\pi2,0\right[$, calculer $\sin x$.", "-sqrt(1-Rational(9,25))", "Rational(-4,5)",
          r"$\sin^2x=1-\frac9{25}=\frac{16}{25}$, et $\sin x < 0$ sur cet intervalle : $-\frac45$.", F["trigo"],
          [(r"Sachant $\sin x=\frac5{13}$ et $x\in\left]\frac\pi2,\pi\right[$, calculer $\cos x$.", "-sqrt(1-Rational(25,169))", "Rational(-12,13)", r"$\cos x < 0$ : $-\frac{12}{13}$.")]),
    ]},
    {"n": 0, "titre": "Formules d'addition, équations", "notions": ["trigo"], "exos": [
        v("tg4", r"Calculer $\cos\frac\pi{12}$ avec $\frac\pi{12}=\frac\pi3-\frac\pi4$.", "cos(pi/3)*cos(pi/4)+sin(pi/3)*sin(pi/4)", "(sqrt(6)+sqrt(2))/4",
          r"$\cos(a-b)=\cos a\cos b+\sin a\sin b=\frac12\cdot\frac{\sqrt2}2+\frac{\sqrt3}2\cdot\frac{\sqrt2}2=\frac{\sqrt6+\sqrt2}4$.", F["trigo"],
          [(r"Calculer $\sin\frac\pi{12}$.", "sin(pi/3)*cos(pi/4)-cos(pi/3)*sin(pi/4)", "(sqrt(6)-sqrt(2))/4", r"$\sin(a-b)=\sin a\cos b-\cos a\sin b$.")], duree=3),
        v("tg5", r"Simplifier $\cos^2x-\sin^2x-2\cos^2x$.", "cos(x)**2-sin(x)**2-2*cos(x)**2", "-1", r"$-(\cos^2x+\sin^2x)=-1$.", F["trigo"],
          [(r"Simplifier $(\cos x+\sin x)^2-\sin(2x)$.", "(cos(x)+sin(x))**2-sin(2*x)", "1", r"$1+2\sin x\cos x-2\sin x\cos x=1$.")]),
        o("tg6", r"Résoudre $\cos x=\frac12$ sur $\mathbb R$.", r"$x=\frac\pi3+2k\pi$ ou $x=-\frac\pi3+2k\pi$, $k\in\mathbb Z$.", F["trigo"], duree=2),
    ]},
    {"n": 15, "titre": "Dérivées usuelles", "notions": ["derivees"], "exos": [
        d("de1", "3*x**4-2*x**2+5*x-1", "12*x**3-4*x+5", r"Dériver $f(x)=3x^4-2x^2+5x-1$.", r"$f'(x)=12x^3-4x+5$.",
          [("x**5-3*x+2", "5*x**4-3", r"Dériver $f(x)=x^5-3x+2$.", r"$f'(x)=5x^4-3$.")]),
        d("de2", "x**2*exp(x)", "(x**2+2*x)*exp(x)", r"Dériver $f(x)=x^2e^x$.", r"$(uv)'$ : $2xe^x+x^2e^x=(x^2+2x)e^x$.",
          [("x*log(x)", "log(x)+1", r"Dériver $f(x)=x\ln x$.", r"$\ln x+x\cdot\frac1x=\ln x+1$.")]),
        d("de3", "(2*x+1)/(x+3)", "5/(x+3)**2", r"Dériver $f(x)=\frac{2x+1}{x+3}$.", r"$\frac{2(x+3)-(2x+1)}{(x+3)^2}=\frac5{(x+3)^2}$.",
          [("(x-1)/(x+1)", "2/(x+1)**2", r"Dériver $f(x)=\frac{x-1}{x+1}$.", r"$\frac{(x+1)-(x-1)}{(x+1)^2}=\frac2{(x+1)^2}$.")]),
    ]},
    {"n": 0, "titre": "Composées", "notions": ["derivees"], "exos": [
        d("de4", "exp(-x**2)", "-2*x*exp(-x**2)", r"Dériver $f(x)=e^{-x^2}$.", r"$u'e^u$ avec $u'=-2x$.",
          [("exp(3*x+1)", "3*exp(3*x+1)", r"Dériver $f(x)=e^{3x+1}$.", r"$3e^{3x+1}$.")]),
        d("de5", "log(x**2+1)", "2*x/(x**2+1)", r"Dériver $f(x)=\ln(x^2+1)$.", r"$\frac{u'}u=\frac{2x}{x^2+1}$.",
          [("log(3*x-1)", "3/(3*x-1)", r"Dériver $f(x)=\ln(3x-1)$ sur $\left]\frac13,+\infty\right[$.", r"$\frac3{3x-1}$.")]),
        d("de6", "sqrt(x**2+1)", "x/sqrt(x**2+1)", r"Dériver $f(x)=\sqrt{x^2+1}$.", r"$\frac{u'}{2\sqrt u}=\frac{2x}{2\sqrt{x^2+1}}=\frac{x}{\sqrt{x^2+1}}$.",
          [("1/(x**2+1)", "-2*x/(x**2+1)**2", r"Dériver $f(x)=\frac1{x^2+1}$.", r"$-\frac{u'}{u^2}$.")]),
        d("de7", "sin(2*x)*cos(x)", "2*cos(2*x)*cos(x)-sin(2*x)*sin(x)", r"Dériver $f(x)=\sin(2x)\cos x$.",
          r"$(uv)'$ : $2\cos(2x)\cos x-\sin(2x)\sin x$.",
          [("cos(x)**3", "-3*sin(x)*cos(x)**2", r"Dériver $f(x)=\cos^3x$.", r"$3u'u^2$ avec $u'=-\sin x$.")]),
    ]},
    {"n": 16, "titre": "Limites usuelles", "notions": ["limites"], "exos": [
        v("li1", r"Calculer $\lim_{x\to+\infty}\frac{3x^2-x+1}{2x^2+5}$.", "limit((3*x**2-x+1)/(2*x**2+5),x,oo)", "Rational(3,2)",
          r"Factoriser par $x^2$ : $\frac{3-\frac1x+\frac1{x^2}}{2+\frac5{x^2}}\to\frac32$.", F["limites"],
          [(r"Calculer $\lim_{x\to+\infty}\frac{x^3+1}{4x^3-x}$.", "limit((x**3+1)/(4*x**3-x),x,oo)", "Rational(1,4)", r"Termes dominants : $\frac{x^3}{4x^3}=\frac14$.")]),
        v("li2", r"Calculer $\lim_{x\to+\infty}\left(x^2-3x\right)$.", "limit(x**2-3*x,x,oo)", "oo",
          r"Forme $\infty-\infty$ : $x^2\left(1-\frac3x\right)\to+\infty$.", F["limites"],
          [(r"Calculer $\lim_{x\to-\infty}\left(x^3+x^2\right)$.", "limit(x**3+x**2,x,-oo)", "-oo", r"$x^3\left(1+\frac1x\right)\to-\infty$.")]),
    ]},
    {"n": 0, "titre": "Croissances comparées, limites en 0", "notions": ["limites"], "exos": [
        v("li3", r"Calculer $\lim_{x\to+\infty}x^3e^{-x}$.", "limit(x**3*exp(-x),x,oo)", "0", r"Croissances comparées : $\frac{x^3}{e^x}\to0$.", F["limites"],
          [(r"Calculer $\lim_{x\to+\infty}\frac{\ln x}{\sqrt x}$.", "limit(log(x)/sqrt(x),x,oo)", "0", r"Croissances comparées : $\ln$ est dominé par toute puissance.")]),
        v("li4", r"Calculer $\lim_{x\to0}\frac{e^{2x}-1}{x}$.", "limit((exp(2*x)-1)/x,x,0)", "2",
          r"$\frac{e^{2x}-1}{2x}\cdot2\to1\cdot2=2$.", F["limites"],
          [(r"Calculer $\lim_{x\to0}\frac{\ln(1+3x)}{x}$.", "limit(log(1+3*x)/x,x,0)", "3", r"$\frac{\ln(1+3x)}{3x}\cdot3\to3$.")]),
        v("li5", r"Calculer $\lim_{x\to0}\frac{\sin(5x)}{x}$.", "limit(sin(5*x)/x,x,0)", "5", r"$\frac{\sin(5x)}{5x}\cdot5\to5$.", F["limites"],
          [(r"Calculer $\lim_{x\to0}\frac{\sin x}{3x}$.", "limit(sin(x)/(3*x),x,0)", "Rational(1,3)", r"$\frac13\cdot\frac{\sin x}x\to\frac13$.")]),
        v("li6", r"Calculer $\lim_{x\to+\infty}\left(\sqrt{x+1}-\sqrt x\right)$.", "limit(sqrt(x+1)-sqrt(x),x,oo)", "0",
          r"Conjugué : $\frac{1}{\sqrt{x+1}+\sqrt x}\to0$.", F["limites"] + " · " + F["racines"],
          [(r"Calculer $\lim_{x\to+\infty}\left(\sqrt{x^2+x}-x\right)$.", "limit(sqrt(x**2+x)-x,x,oo)", "Rational(1,2)",
            r"$\frac{x}{\sqrt{x^2+x}+x}=\frac1{\sqrt{1+1/x}+1}\to\frac12$.")], duree=3),
    ]},
]

FORMULES = {e["id"]: e.pop("_f") for lvl in _POOL for e in lvl["exos"]}
_EXOS = {e["id"]: e for lvl in _POOL for e in lvl["exos"]}

# Chapter = one level path of the subject « Bases maths ». Levels: (title, notions, exercise ids).
CHAPTERS = {
    "fractions": ("Fractions", 10, [
        ("Fractions numériques", ["fractions"], ["fr1", "fr2", "fr3", "fr4", "fr5"]),
        ("Fractions rationnelles", ["fractions_alg"], ["fa_1", "fa_2", "fa_3", "fa_4"])]),
    "puissances": ("Puissances et racines", 11, [
        ("Puissances", ["puissances"], ["pu1", "pu2", "pu3", "pu4", "pu5"]),
        ("Racines carrées", ["racines"], ["ra1", "ra2", "ra3", "ra4", "ra5"])]),
    "algebre": ("Développer et factoriser", 12, [
        ("Développer", ["developper"], ["dv1", "dv2", "dv3", "dv4", "dv5"]),
        ("Factoriser", ["factoriser"], ["fa1", "fa2", "fa3", "fa4", "fa5", "fa6"]),
        ("Trinôme du second degré", ["trinome"], ["tr1", "tr2", "tr3", "tr4", "tr5"])]),
    "divisions": ("Divisions", 13, [
        ("Division euclidienne des entiers", ["divisions"], ["di1", "di2", "di6"]),
        ("Division des polynômes", ["divisions"], ["di3", "di4", "di5"])]),
    "equations": ("Équations, inéquations, valeur absolue", 14, [
        ("Équations et inéquations", ["equations"], ["eq1", "eq2", "eq3", "eq4", "eq5"]),
        ("Valeur absolue", ["valeur_absolue"], ["va1", "va2", "va3", "va4", "va5"])]),
    "sommes": ("Sommes", 15, [
        ("Sommes usuelles et linéarité", ["sommes"], ["so1", "so2", "so4", "so6"]),
        ("Sommes géométriques et télescopiques", ["sommes"], ["so3", "so7", "so5"])]),
    "exp_ln": ("Exponentielle et logarithme", 16, [
        ("Exponentielle", ["exp"], ["ex1", "ex2", "ex3", "ex4", "ex5"]),
        ("Logarithme", ["ln"], ["ln1", "ln2", "ln3", "ln4", "ln5", "ln6"])]),
    "trigo": ("Trigonométrie", 17, [
        ("Valeurs remarquables et relations", ["trigo"], ["tg1", "tg2", "tg3"]),
        ("Formules d'addition, équations", ["trigo"], ["tg4", "tg5", "tg6"])]),
    "derivees": ("Dérivées", 18, [
        ("Opérations : somme, produit, quotient", ["derivees"], ["de1", "de2", "de3"]),
        ("Composées", ["derivees"], ["de4", "de5", "de6", "de7"])]),
    "limites": ("Limites", 19, [
        ("Polynômes, fractions, conjugué", ["limites"], ["li1", "li2", "li6"]),
        ("Croissances comparées, limites en 0", ["limites"], ["li3", "li4", "li5"])]),
}
_used = [i for _, _, lv in CHAPTERS.values() for _, _, ids in lv for i in ids]
assert sorted(_used) == sorted(_EXOS), "every pool exercise in exactly one chapter"


def chapter(key):
    """Module globals of the level path for one chapter (parcours/src/bases_<key>.py)."""
    titre, ordre, levels = CHAPTERS[key]
    notions = {n for _, ns, _ in levels for n in ns}
    ids = {i for _, _, lv in levels for i in lv}
    return {
        "SUBJECT": {"id": f"bases-{key.replace('_', '-')}", "ordre": ordre, "matiere": "bases", "semestre": "S0",
                    "ecue": "Calcul", "titre": titre, "chapitres_moodle": [], "td": "", "examens": []},
        "NOTIONS": [n for n in NOTIONS if n["id"] in notions],
        "LEVELS": [{"n": j, "titre": t, "notions": ns, "exos": [_EXOS[i] for i in lv]} for j, (t, ns, lv) in enumerate(levels, 1)],
        "FORMULES": {i: FORMULES[i] for i in ids},
        "QUIZ": [q for q in QUIZ if q["notion"] in notions],
        "EXTRA_PARTS": [],
    }

QUIZ = [
    {"notion": "fractions", "type": "vf", "q": r"$\frac{a+b}{a+c}=\frac{b}{c}$", "bonne": False},
    {"notion": "fractions", "type": "qcm", "q": r"$\frac{2/3}{4/5}=$", "choix": [r"$\frac56$", r"$\frac8{15}$", r"$\frac{6}{5}$", r"$\frac{10}{12}$ non simplifiable"], "bonne": 0},
    {"notion": "puissances", "type": "vf", "q": r"$2^3+2^3=2^4$", "bonne": True},
    {"notion": "puissances", "type": "qcm", "q": r"$(x^2)^3=$", "choix": [r"$x^6$", r"$x^5$", r"$x^8$", r"$x^9$"], "bonne": 0},
    {"notion": "racines", "type": "vf", "q": r"$\sqrt{9+16}=3+4$", "bonne": False},
    {"notion": "racines", "type": "vf", "q": r"$\sqrt{x^2}=|x|$ pour tout réel $x$.", "bonne": True},
    {"notion": "developper", "type": "qcm", "q": r"$(a-b)^2=$", "choix": [r"$a^2-2ab+b^2$", r"$a^2-b^2$", r"$a^2+b^2$", r"$a^2-ab+b^2$"], "bonne": 0},
    {"notion": "factoriser", "type": "qcm", "q": r"$x^2-25=$", "choix": [r"$(x-5)(x+5)$", r"$(x-5)^2$", r"$(x-25)(x+1)$", r"pas factorisable"], "bonne": 0},
    {"notion": "trinome", "type": "vf", "q": r"Si $\Delta < 0$, $ax^2+bx+c$ a le signe de $a$ pour tout $x$.", "bonne": True},
    {"notion": "trinome", "type": "qcm", "q": r"Produit des racines de $2x^2-6x+4$ :", "choix": [r"$2$", r"$3$", r"$4$", r"$-3$"], "bonne": 0},
    {"notion": "fractions_alg", "type": "vf", "q": r"$\frac{x+2}{x+5}=\frac25$", "bonne": False},
    {"notion": "divisions", "type": "vf", "q": r"Le reste de la division de $P$ par $x-a$ est $P(a)$.", "bonne": True},
    {"notion": "divisions", "type": "qcm", "q": r"Reste de la division euclidienne de $-7$ par $3$ :", "choix": [r"$2$", r"$-1$", r"$1$", r"$-2$"], "bonne": 0},
    {"notion": "equations", "type": "vf", "q": r"Si $-2x\le6$ alors $x\le-3$.", "bonne": False},
    {"notion": "valeur_absolue", "type": "qcm", "q": r"$|x-2| < 1\iff$", "choix": [r"$1 < x < 3$", r"$x < 3$", r"$-1 < x < 1$", r"$x>1$"], "bonne": 0},
    {"notion": "sommes", "type": "qcm", "q": r"Nombre de termes de $\sum_{k=3}^{10}$ :", "choix": [r"$8$", r"$7$", r"$10$", r"$13$"], "bonne": 0},
    {"notion": "sommes", "type": "vf", "q": r"$\sum_{k=0}^{n}2^k=2^{n+1}-1$", "bonne": True},
    {"notion": "exp", "type": "vf", "q": r"$e^{a}+e^{b}=e^{a+b}$", "bonne": False},
    {"notion": "exp", "type": "vf", "q": r"$e^x>0$ pour tout réel $x$.", "bonne": True},
    {"notion": "ln", "type": "qcm", "q": r"$\ln(8)=$", "choix": [r"$3\ln2$", r"$\ln6+\ln2$", r"$8\ln1$", r"$\ln2^3=(\ln2)^3$"], "bonne": 0},
    {"notion": "ln", "type": "vf", "q": r"$\ln(a+b)=\ln a\,\ln b$", "bonne": False},
    {"notion": "trigo", "type": "qcm", "q": r"$\sin\frac\pi3=$", "choix": [r"$\frac{\sqrt3}2$", r"$\frac12$", r"$\frac{\sqrt2}2$", r"$1$"], "bonne": 0},
    {"notion": "trigo", "type": "vf", "q": r"$\cos(\pi-x)=\cos x$", "bonne": False},
    {"notion": "derivees", "type": "qcm", "q": r"$(\ln u)'=$", "choix": [r"$\frac{u'}u$", r"$\frac1u$", r"$u'\ln u$", r"$\frac{u}{u'}$"], "bonne": 0},
    {"notion": "limites", "type": "vf", "q": r"$\lim_{x\to+\infty}\frac{e^x}{x^{10}}=+\infty$", "bonne": True},
    {"notion": "limites", "type": "qcm", "q": r"$\lim_{x\to0^+}x\ln x=$", "choix": [r"$0$", r"$-\infty$", r"$1$", r"$+\infty$"], "bonne": 0},
]
