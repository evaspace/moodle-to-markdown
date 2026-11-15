"""Level path: S2 maths, ECUE APEF, part 2: fonctions, étude locale (continuité, TVI, o, équivalents, DL, limites).

Moodle chapter "06_Cours 2 - Fonctions - étude locale" (S2-MATHS-2030). Calibrated on Examen S2-B3 APEF
mars 2026 (ex. 3, 4, 5), read on the official correction, and on `annales/FORMULES.md` (« APEF (fonctions) »).
`value` exercises: `calc` (sympy: limit, series(...).removeO()) must equal `ans`; expansions are compared at sample points.
"""

SUBJECT = {
    "id": "maths-s2-apef-fonctions",
    "ordre": 210,
    "matiere": "maths",
    "semestre": "S2",
    "ecue": "APEF",
    "titre": "Fonctions : étude locale, développements limités",
    "chapitres_moodle": ["06_Cours 2 - Fonctions - étude locale"],
    "td": "TD étude locale (S2 2030)",
    "examens": ["Examen S2-B3 APEF (avant les vacances de printemps)"],
}

NOTIONS = [
    {"id": "continuite", "titre": "Continuité en un point",
     "formule": r"$f$ continue en $a$ $\iff\lim_{x\to a}f(x)=f(a)$ $\iff\lim_{a^-}f=\lim_{a^+}f=f(a)$",
     "exemple": r"$f(x)=\frac{x^2-1}{x-1}$ se prolonge par continuité en $1$ avec $f(1)=2$",
     "cours": r"Les fonctions usuelles sont continues sur leur domaine. Pour une fonction définie par morceaux, calculer la limite à gauche et à droite au point de raccord et comparer à la valeur. Encadrement : $|f(x)|\le g(x)\to0$ donne $f\to0$."},
    {"id": "tvi", "titre": "Théorème des valeurs intermédiaires",
     "formule": r"$f$ continue sur $[a,b]$, $k$ entre $f(a)$ et $f(b)$ $\Rightarrow\exists c\in[a,b],\ f(c)=k$ · si $f(a)f(b)<0$ : $\exists c\in\,]a,b[,\ f(c)=0$",
     "exemple": r"$x^3+x-1$ s'annule sur $]0,1[$ : $f(0)=-1$, $f(1)=1$",
     "cours": r"Trois choses à écrire : $f$ est continue sur $[a,b]$, les valeurs $f(a)$ et $f(b)$, la conclusion. L'unicité demande en plus la stricte monotonie. Pour une équation $f(x)=g(x)$, appliquer le TVI à $f-g$."},
    {"id": "negligeable", "titre": "Négligeabilité : petit o",
     "formule": r"$f=o(g)\iff\frac fg\to0\iff f=g\,\varepsilon$ avec $\varepsilon\to0$ · en $0$ : $o(x^p)+o(x^q)=o(x^{\min(p,q)})$, $x^p\,o(x^q)=o(x^{p+q})$, $o(x^p)\,o(x^q)=o(x^{p+q})$",
     "exemple": r"en $0$ : $x^2=o(x)$ ; en $+\infty$ : $x=o(x^2)$",
     "cours": r"En $0$, les grandes puissances sont négligeables devant les petites ; en $+\infty$ c'est l'inverse. Croissances comparées en $+\infty$ : $\ln x\ll x^a\ll e^x$. Un $o(x^3)$ est aussi un $o(x^2)$ en $0$, pas l'inverse."},
    {"id": "equivalent", "titre": "Équivalents",
     "formule": r"$f\sim g\iff\frac fg\to1\iff f=g(1+\varepsilon)$, $\varepsilon\to0$ · en $0$ : $\sin x\sim x$, $e^x-1\sim x$, $\ln(1+x)\sim x$, $1-\cos x\sim\frac{x^2}2$ · polynôme : terme de plus bas degré en $0$, de plus haut degré en $\pm\infty$",
     "exemple": r"$\frac{\sin 3x}x\sim\frac{3x}x=3$ en $0$",
     "cours": r"Les équivalents se multiplient, se divisent, s'élèvent à une puissance fixe. **Jamais** de somme, d'exponentielle ni de logarithme d'équivalents : pour une somme, passer par les DL. $f\sim g$ donne la même limite. $f\sim$ le premier terme non nul de son DL."},
    {"id": "taylor-young", "titre": "Formule de Taylor-Young",
     "formule": r"$f(x)=\sum_{k=0}^n\frac{f^{(k)}(a)}{k!}(x-a)^k+o\big((x-a)^n\big)$",
     "exemple": r"$\ln x=(x-1)-\frac{(x-1)^2}2+o\big((x-1)^2\big)$ en $1$",
     "cours": r"Le DL à l'ordre $n$ est unique : on lit $f(a)$, $f'(a)$, $\frac{f''(a)}2$… sur ses coefficients. En $a\ne0$, poser $h=x-a$."},
    {"id": "dl-usuels", "titre": "DL usuels en 0",
     "formule": r"$e^x=1+x+\frac{x^2}2+\frac{x^3}6+o(x^3)$ · $\cos x=1-\frac{x^2}2+\frac{x^4}{24}+o(x^5)$ · $\sin x=x-\frac{x^3}6+\frac{x^5}{120}+o(x^6)$ · $\ln(1+x)=x-\frac{x^2}2+\frac{x^3}3+o(x^3)$ · $\frac1{1-x}=1+x+x^2+x^3+o(x^3)$ · $(1+x)^\alpha=1+\alpha x+\frac{\alpha(\alpha-1)}2x^2+o(x^2)$",
     "exemple": r"$\sqrt{1+x}=1+\frac x2-\frac{x^2}8+o(x^2)$ ($\alpha=\frac12$)",
     "cours": r"À connaître par cœur. $\cos$ est paire (puissances paires), $\sin$ impaire. Remplacer $x$ par $-x$, $2x$, $x^2$ donne $e^{-x}$, $\frac1{1+x}$, $\frac1{1+x^2}$… tant que la quantité substituée tend vers $0$."},
    {"id": "dl-operations", "titre": "Opérations sur les DL",
     "formule": r"somme : à l'ordre le plus petit des deux · produit : multiplier les parties régulières et tronquer à l'ordre $n$ · composition : poser $u\to0$, calculer $u$, $u^2$, $u^3$ tronqués à l'ordre $n$",
     "exemple": r"$e^x\sin x=(1+x+\frac{x^2}2)(x-\frac{x^3}6)+o(x^3)=x+x^2+\frac{x^3}3+o(x^3)$",
     "cours": r"Toujours rappeler les DL usuels utilisés. Dans un produit, ne garder que les termes de degré $\le n$. Pour $\ln(a+\dots)$, factoriser $a$ : $\ln a+\ln(1+u)$. Pour un quotient, écrire $\frac1{1+u}$."},
    {"id": "limite-dl", "titre": "Limites par DL et équivalents",
     "formule": r"forme $\frac00$ : DL du numérateur et du dénominateur jusqu'au premier terme non nul, puis quotient des équivalents · $a^b=e^{b\ln a}$ · en $+\infty$ : poser $X=\frac1x\to0$",
     "exemple": r"$\frac{e^x-1-x}{x^2}\sim\frac{x^2/2}{x^2}\to\frac12$",
     "cours": r"Pousser le DL assez loin pour que les termes ne se compensent pas tous. Pour $u^v$, toujours revenir à $e^{v\ln u}$ et chercher la limite de l'exposant."},
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


def dl(f, n, a=0):
    """sympy string: regular part of the expansion of f at a, order n."""
    return f"series({f}, x, {a}, {n + 1}).removeO()"


A30 = "Examen S2-B3 APEF mars 2026"

LEVELS = [
    {"n": 1, "titre": "Continuité en un point", "notions": ["continuite"], "exos": [
        v("fc1", r"$f(x)=\dfrac{x^2-1}{x-1}$ pour $x\ne1$. Quelle valeur donner à $f(1)$ pour que $f$ soit continue en $1$ ?",
          "limit((x**2-1)/(x-1), x, 1)", "2", r"$\frac{x^2-1}{x-1}=x+1\to2$. Il faut $f(1)=2$.", duree=2),
        v("fc2", r"$f(x)=\dfrac{\sin x}x$ pour $x\ne0$. Quelle valeur donner à $f(0)$ pour que $f$ soit continue en $0$ ?",
          "limit(sin(x)/x, x, 0)", "1", r"$\sin x\sim x$ en $0$, donc $\frac{\sin x}x\to1$. Il faut $f(0)=1$.", duree=2),
        v("fc3", r"$f(x)=x+a$ si $x<1$ et $f(x)=x^2+1$ si $x\ge1$. Pour quelle valeur de $a$ la fonction $f$ est-elle continue en $1$ ?",
          "limit(x**2+1, x, 1)-1", "1", r"$\lim_{1^-}f=1+a$ et $\lim_{1^+}f=f(1)=2$. Continue $\iff1+a=2\iff a=1$.", duree=3),
        o("fc4", r"$f(x)=x\sin\frac1x$ pour $x\ne0$ et $f(0)=0$. La fonction $f$ est-elle continue en $0$ ?",
          r"Oui. $|f(x)|\le|x|\to0$, donc $\lim_0f=0=f(0)$.", duree=3),
        o("fc5", r"La fonction partie entière $x\mapsto\lfloor x\rfloor$ est-elle continue en $1$ ?",
          r"Non. $\lim_{1^-}\lfloor x\rfloor=0$ et $\lim_{1^+}\lfloor x\rfloor=1$ : les limites à gauche et à droite diffèrent.", duree=2),
    ]},
    {"n": 2, "titre": "Théorème des valeurs intermédiaires", "notions": ["tvi"], "exos": [
        o("ft1", r"Montrer que l'équation $x^3+x-1=0$ a une unique solution dans $]0,1[$.",
          r"$f(x)=x^3+x-1$ est continue sur $[0,1]$, $f(0)=-1<0$, $f(1)=1>0$ : par le TVI, $f$ s'annule sur $]0,1[$. $f'(x)=3x^2+1>0$ : $f$ est strictement croissante, la solution est unique.", duree=4),
        o("ft2", r"Montrer que l'équation $\cos x=x$ a une solution dans $\left[0,\frac\pi2\right]$.",
          r"$g(x)=\cos x-x$ est continue sur $\left[0,\frac\pi2\right]$, $g(0)=1>0$, $g\left(\frac\pi2\right)=-\frac\pi2<0$. Par le TVI, $g$ s'annule.", duree=4),
        o("ft3", r"Soit $f:[0,1]\to[0,1]$ continue. Montrer que $f$ a un point fixe : $\exists c\in[0,1],\ f(c)=c$.",
          r"$g(x)=f(x)-x$ est continue sur $[0,1]$. $g(0)=f(0)\ge0$ et $g(1)=f(1)-1\le0$. Par le TVI, $\exists c$, $g(c)=0$, soit $f(c)=c$."),
        o("ft4", r"Montrer que tout polynôme réel de degré $3$ a au moins une racine réelle.",
          r"Quitte à diviser par le coefficient dominant, $P(x)\sim x^3$ : $\lim_{-\infty}P=-\infty$ et $\lim_{+\infty}P=+\infty$. Il existe donc $a < b$ avec $P(a)<0$ et $P(b)>0$ ; $P$ est continue sur $[a,b]$ : par le TVI, $P$ s'annule."),
        o("ft5", r"Vrai ou faux : si $f$ est continue sur $[a,b]$ et $f(a)f(b)>0$, alors $f$ ne s'annule pas sur $[a,b]$.",
          r"Faux. $f(x)=x^2-1$ sur $[-2,2]$ : $f(-2)f(2)=9>0$ mais $f(1)=0$. Le TVI donne une condition suffisante, pas nécessaire.", duree=3),
    ]},
    {"n": 3, "titre": "Petit o", "notions": ["negligeable"], "exos": [
        o("fo1", r"A-t-on $x^2=o(x)$ au voisinage de $0$ ? Au voisinage de $+\infty$ ?",
          r"$\frac{x^2}x=x$. En $0$ : $x\to0$, donc oui. En $+\infty$ : $x\to+\infty$, donc non (c'est $x=o(x^2)$).", duree=2),
        o("fo2", r"Simplifier au voisinage de $0$ : $o(x^2)+o(x^3)$ ; $x\cdot o(x^2)$ ; $o(x)\times o(x^2)$.",
          r"$o(x^2)+o(x^3)=o(x^2)$ ; $x\cdot o(x^2)=o(x^3)$ ; $o(x)\times o(x^2)=o(x^3)$.", duree=3),
        o("fo3", r"Classer avec le symbole $\ll$ au voisinage de $+\infty$ : $x^2$, $\ln x$, $e^x$, $\sqrt x$.",
          r"$\ln x\ll\sqrt x\ll x^2\ll e^x$ (croissances comparées).", duree=2),
        o("fo4", r"La notation $f=o(g)$ s'écrit aussi $f\ll g$. Compléter par $\ll$, $\gg$ ou $\sim$ : $2x^2\dots x$ ; $(x^3-3x^2+x)\dots x$ ; $(x^3-3x^2+x)\dots x^3$, au voisinage de $0$ puis de $+\infty$.",
          r"En $0$ : $2x^2\ll x$ ; $x^3-3x^2+x\sim x$ ; $x^3-3x^2+x\gg x^3$." "\n\n"
          r"En $+\infty$ : $2x^2\gg x$ ; $x^3-3x^2+x\gg x$ ; $x^3-3x^2+x\sim x^3$.", src=f"{A30}, ex. 3.2"),
        o("fo5", r"Au voisinage de $0$ : si $f=o(x^3)$, a-t-on $f=o(x^2)$ ? Et la réciproque ?",
          r"Oui : $\frac f{x^2}=x\cdot\frac f{x^3}\to0$. Réciproque fausse : $f(x)=x^3$ est un $o(x^2)$ mais pas un $o(x^3)$ ($\frac{x^3}{x^3}=1$).", duree=3),
    ]},
    {"n": 4, "titre": "Équivalents", "notions": ["equivalent"], "exos": [
        o("fe1", r"Donner un équivalent simple de $x^3-3x^2+x$ en $0$, puis en $+\infty$.",
          r"En $0$ : terme de plus bas degré, $x$. En $+\infty$ : terme de plus haut degré, $x^3$.", duree=2),
        v("fe2", r"Calculer $\displaystyle\lim_{x\to0}\frac{\sin 3x}x$.", "limit(sin(3*x)/x, x, 0)", "3", r"$\sin 3x\sim3x$, donc $\frac{\sin3x}x\sim3$.", duree=2),
        v("fe3", r"Calculer $\displaystyle\lim_{x\to0}\frac{e^{2x}-1}{\ln(1+x)}$.", "limit((exp(2*x)-1)/log(1+x), x, 0)", "2",
          r"$e^{2x}-1\sim2x$ et $\ln(1+x)\sim x$ : le quotient est équivalent à $2$.", duree=3),
        v("fe4", r"Calculer $\displaystyle\lim_{x\to+\infty}\frac{3x^2+x}{2x^2-1}$.", "limit((3*x**2+x)/(2*x**2-1), x, oo)", "Rational(3,2)",
          r"Quotient des termes de plus haut degré : $\frac{3x^2}{2x^2}=\frac32$.", duree=2),
        o("fe5", r"Peut-on additionner des équivalents ? Tester avec $f(x)=x+x^2$, $g(x)=-x$ en $0$.",
          r"Non. $f\sim x$ et $g\sim-x$, mais $f+g=x^2$ n'est pas équivalent à $x+(-x)=0$. Pour une somme, on passe par les DL.", duree=3),
        v("fe6", r"Calculer $\displaystyle\lim_{x\to0}\frac{1-\cos x}{x^2}$.", "limit((1-cos(x))/x**2, x, 0)", "Rational(1,2)",
          r"$\cos x=1-\frac{x^2}2+o(x^2)$, donc $1-\cos x\sim\frac{x^2}2$ : limite $\frac12$.", duree=3),
    ]},
    {"n": 5, "titre": "Formule de Taylor-Young", "notions": ["taylor-young"], "exos": [
        v("fy1", r"$f(0)=1$, $f'(0)=2$, $f''(0)=-4$. Donner la partie régulière du DL de $f$ en $0$ à l'ordre $2$.",
          "1+2*x-4*x**2/factorial(2)", "1+2*x-2*x**2", r"$f(x)=f(0)+f'(0)x+\frac{f''(0)}2x^2+o(x^2)=1+2x-2x^2+o(x^2)$.", duree=2),
        v("fy2", r"Avec la formule de Taylor-Young, donner le DL de $e^x$ en $0$ à l'ordre $3$.", dl("exp(x)", 3), "1+x+x**2/2+x**3/6",
          r"Toutes les dérivées valent $1$ en $0$ : $e^x=1+x+\frac{x^2}2+\frac{x^3}6+o(x^3)$.", duree=2),
        v("fy3", r"Donner le DL de $\ln x$ en $1$ à l'ordre $2$.", dl("log(x)", 2, 1), "(x-1)-(x-1)**2/2",
          r"$f(1)=0$, $f'(1)=1$, $f''(1)=-1$ : $\ln x=(x-1)-\frac{(x-1)^2}2+o\big((x-1)^2\big)$.", duree=3),
        v("fy4", r"Avec la formule de Taylor-Young, donner le DL de $\sqrt{1+x}$ en $0$ à l'ordre $2$.", dl("sqrt(1+x)", 2), "1+x/2-x**2/8",
          r"$f(0)=1$, $f'(0)=\frac12$, $f''(0)=-\frac14$ : $\sqrt{1+x}=1+\frac x2-\frac{x^2}8+o(x^2)$.", duree=3),
        v("fy5", r"On sait que $f(x)=2-x+3x^2+o(x^2)$ en $0$ et que $f$ est deux fois dérivable. Que vaut $f''(0)$ ?", "2*3", "6",
          r"Par unicité du DL, $\frac{f''(0)}2=3$, donc $f''(0)=6$ (et $f'(0)=-1$).", duree=2),
    ]},
    {"n": 6, "titre": "DL usuels", "notions": ["dl-usuels"], "exos": [
        v("fu1", r"DL de $\sin x$ en $0$ à l'ordre $5$.", dl("sin(x)", 5), "x-x**3/6+x**5/120", r"$\sin x=x-\frac{x^3}6+\frac{x^5}{120}+o(x^5)$.", duree=2),
        v("fu2", r"DL de $\cos x$ en $0$ à l'ordre $4$.", dl("cos(x)", 4), "1-x**2/2+x**4/24", r"$\cos x=1-\frac{x^2}2+\frac{x^4}{24}+o(x^4)$.", duree=2),
        v("fu3", r"DL de $\ln(1+x)$ en $0$ à l'ordre $4$.", dl("log(1+x)", 4), "x-x**2/2+x**3/3-x**4/4",
          r"$\ln(1+x)=x-\frac{x^2}2+\frac{x^3}3-\frac{x^4}4+o(x^4)$.", duree=2),
        v("fu4", r"DL de $\dfrac1{1-x}$ en $0$ à l'ordre $3$.", dl("1/(1-x)", 3), "1+x+x**2+x**3", r"$\frac1{1-x}=1+x+x^2+x^3+o(x^3)$.", duree=2),
        v("fu5", r"DL de $\dfrac1{\sqrt{1+x}}$ en $0$ à l'ordre $2$.", dl("1/sqrt(1+x)", 2), "1-x/2+3*x**2/8",
          r"$(1+x)^\alpha$ avec $\alpha=-\frac12$ : $1-\frac x2+\frac{(-\frac12)(-\frac32)}2x^2=1-\frac x2+\frac{3x^2}8+o(x^2)$.", duree=3),
        v("fu6", r"DL de $e^{-2x}$ en $0$ à l'ordre $3$.", dl("exp(-2*x)", 3), "1-2*x+2*x**2-4*x**3/3",
          r"$e^u$ avec $u=-2x$ : $1-2x+\frac{4x^2}2-\frac{8x^3}6=1-2x+2x^2-\frac43x^3+o(x^3)$.", duree=3),
        v("fu7", r"DL de $\dfrac1{1+x}$ en $0$ à l'ordre $3$.", dl("1/(1+x)", 3), "1-x+x**2-x**3", r"$\frac1{1-u}$ avec $u=-x$ : $1-x+x^2-x^3+o(x^3)$.", duree=2),
    ]},
    {"n": 7, "titre": "Somme et produit de DL", "notions": ["dl-operations", "dl-usuels"], "exos": [
        v("fp1", r"DL de $e^x+\cos x$ en $0$ à l'ordre $3$.", dl("exp(x)+cos(x)", 3), "2+x+x**3/6",
          r"$\left(1+x+\frac{x^2}2+\frac{x^3}6\right)+\left(1-\frac{x^2}2\right)+o(x^3)=2+x+\frac{x^3}6+o(x^3)$.", duree=3),
        v("fp2", r"Donner le développement limité en $0$ à l'ordre $3$ de $f(x)=\cos(x)e^{-2x}$.", dl("cos(x)*exp(-2*x)", 3), "1-2*x+3*x**2/2-x**3/3",
          r"$\left(1-\frac{x^2}2+o(x^3)\right)\left(1-2x+2x^2-\frac43x^3+o(x^3)\right)=1-2x+\frac{3x^2}2-\frac{x^3}3+o(x^3)$.", src=f"{A30}, ex. 4.1", duree=5),
        v("fp3", r"DL de $e^x\sin x$ en $0$ à l'ordre $3$.", dl("exp(x)*sin(x)", 3), "x+x**2+x**3/3",
          r"$\left(1+x+\frac{x^2}2\right)\left(x-\frac{x^3}6\right)+o(x^3)=x+x^2+\frac{x^3}2-\frac{x^3}6+o(x^3)=x+x^2+\frac{x^3}3+o(x^3)$.", duree=5),
        v("fp4", r"DL de $\dfrac{\ln(1+x)}{1-x}$ en $0$ à l'ordre $3$.", dl("log(1+x)/(1-x)", 3), "x+x**2/2+5*x**3/6",
          r"$\left(x-\frac{x^2}2+\frac{x^3}3\right)(1+x+x^2)+o(x^3)=x+\frac{x^2}2+\left(1-\frac12+\frac13\right)x^3+o(x^3)=x+\frac{x^2}2+\frac{5x^3}6+o(x^3)$.", duree=5),
        o("fp5", r"Au voisinage de $0$ : $f(x)=x-\frac{x^2}2+o(x^2)$ et $g(x)=-1+x+3x^2-x^3+o(x^3)$. A-t-on assez d'informations pour donner le DL de $f+g$ à l'ordre $1$ ? $2$ ? $3$ ? Le donner quand c'est possible.",
          r"Ordre 1 : $f+g=-1+2x+o(x)$. Ordre 2 : $f+g=-1+2x+\frac{5x^2}2+o(x^2)$. Ordre 3 : non, on ne connaît pas le DL de $f$ à l'ordre $3$.", src=f"{A30}, ex. 3.3 (c)"),
    ]},
    {"n": 8, "titre": "Composition de DL", "notions": ["dl-operations", "dl-usuels"], "exos": [
        v("fk1", r"DL de $e^{\sin x}$ en $0$ à l'ordre $3$.", dl("exp(sin(x))", 3), "1+x+x**2/2",
          r"$u=\sin x=x-\frac{x^3}6+o(x^3)$, $u^2=x^2+o(x^3)$, $u^3=x^3+o(x^3)$. $e^u=1+u+\frac{u^2}2+\frac{u^3}6=1+x+\frac{x^2}2+o(x^3)$ (les termes en $x^3$ se compensent).", duree=6),
        v("fk2", r"DL de $\ln(\cos x)$ en $0$ à l'ordre $4$.", dl("log(cos(x))", 4), "-x**2/2-x**4/12",
          r"$\cos x=1+u$ avec $u=-\frac{x^2}2+\frac{x^4}{24}$, $u^2=\frac{x^4}4+o(x^4)$. $\ln(1+u)=u-\frac{u^2}2=-\frac{x^2}2+\frac{x^4}{24}-\frac{x^4}8=-\frac{x^2}2-\frac{x^4}{12}+o(x^4)$.", duree=6),
        v("fk3", r"Donner le développement limité en $0$ à l'ordre $4$ de $g(x)=\dfrac1{\sqrt{1+x^2}}$.", dl("1/sqrt(1+x**2)", 4), "1-x**2/2+3*x**4/8",
          r"$(1+u)^{-1/2}$ avec $u=x^2$ : $1-\frac12x^2+\frac{(-\frac12)(-\frac32)}2x^4+o(x^4)=1-\frac{x^2}2+\frac{3x^4}8+o(x^4)$.", src=f"{A30}, ex. 4.2 (a)", duree=5),
        v("fk4", r"On donne $g(x)=\dfrac1{\sqrt{1+x^2}}=1-\dfrac{x^2}2+\dfrac{3x^4}8+o(x^4)$. Donner le développement limité en $0$ à l'ordre $4$ de $h(x)=\ln(1+g(x))$.",
          dl("log(1+1/sqrt(1+x**2))", 4), "log(2)-x**2/4+5*x**4/32",
          r"$h(x)=\ln\left(2-\frac{x^2}2+\frac{3x^4}8\right)=\ln2+\ln(1+u)$ avec $u=-\frac{x^2}4+\frac{3x^4}{16}\to0$ et $u^2=\frac{x^4}{16}+o(x^4)$. $h(x)=\ln2-\frac{x^2}4+\frac{3x^4}{16}-\frac{x^4}{32}+o(x^4)=\ln2-\frac{x^2}4+\frac{5x^4}{32}+o(x^4)$.",
          src=f"{A30}, ex. 4.2 (b)", duree=7),
        v("fk5", r"DL de $\sqrt{1+\sin x}$ en $0$ à l'ordre $2$.", dl("sqrt(1+sin(x))", 2), "1+x/2-x**2/8",
          r"$u=\sin x=x+o(x^2)$ : $\sqrt{1+u}=1+\frac u2-\frac{u^2}8=1+\frac x2-\frac{x^2}8+o(x^2)$.", duree=5),
        v("fk6", r"DL de $\tan x$ en $0$ à l'ordre $3$.", dl("tan(x)", 3), "x+x**3/3",
          r"$\tan x=\frac{\sin x}{\cos x}=\left(x-\frac{x^3}6\right)\left(1+\frac{x^2}2\right)+o(x^3)=x+\frac{x^3}3+o(x^3)$, car $\frac1{\cos x}=\frac1{1-\frac{x^2}2}=1+\frac{x^2}2+o(x^3)$.", duree=6),
    ]},
    {"n": 9, "titre": "Limites par DL", "notions": ["limite-dl", "equivalent"], "exos": [
        v("fl1", r"Calculer $\displaystyle\lim_{x\to0}\frac{e^x-1-x}{x^2}$.", "limit((exp(x)-1-x)/x**2, x, 0)", "Rational(1,2)",
          r"$e^x-1-x=\frac{x^2}2+o(x^2)\sim\frac{x^2}2$ : limite $\frac12$."),
        v("fl2", r"Calculer $\displaystyle\lim_{x\to0}\frac{\sin x-x}{x^3}$.", "limit((sin(x)-x)/x**3, x, 0)", "Rational(-1,6)",
          r"$\sin x-x=-\frac{x^3}6+o(x^3)$ : limite $-\frac16$."),
        v("fl3", r"Calculer $\displaystyle\lim_{x\to0}\frac{\ln(1+x)-x}{x^2}$.", "limit((log(1+x)-x)/x**2, x, 0)", "Rational(-1,2)",
          r"$\ln(1+x)-x=-\frac{x^2}2+o(x^2)$ : limite $-\frac12$."),
        v("fl4", r"Calculer $\displaystyle\lim_{x\to+\infty}\left(1+\frac1x\right)^x$.", "limit((1+1/x)**x, x, oo)", "E",
          r"$\left(1+\frac1x\right)^x=e^{x\ln(1+\frac1x)}$ et $x\ln\left(1+\frac1x\right)=x\left(\frac1x+o\left(\frac1x\right)\right)\to1$. Limite : $e$."),
        v("fl5", r"Calculer $\displaystyle\lim_{x\to0}\frac{\cos x-1}{x\sin x}$.", "limit((cos(x)-1)/(x*sin(x)), x, 0)", "Rational(-1,2)",
          r"$\cos x-1\sim-\frac{x^2}2$ et $x\sin x\sim x^2$ : limite $-\frac12$."),
        v("fl6", r"Calculer $\displaystyle\lim_{x\to0}\frac{e^x-\cos x-x}{x^2}$.", "limit((exp(x)-cos(x)-x)/x**2, x, 0)", "1",
          r"$e^x-\cos x-x=\left(1+x+\frac{x^2}2\right)-\left(1-\frac{x^2}2\right)-x+o(x^2)=x^2+o(x^2)$ : limite $1$."),
    ]},
    {"n": 10, "titre": "Niveau examen : annale complète", "notions": ["negligeable", "equivalent", "dl-operations", "limite-dl"], "examen": True, "exos": [
        {"id": "fx1", "kind": "multi", "src": f"{A30}, ex. 3 (étude locale)",
         "enonce": r"1. Soient $f$ et $g$ définies au voisinage de $x_0$ et ne s'y annulant pas. Donner deux définitions de chacune des notations $f=o(g)$ et $f\sim g$ au voisinage de $x_0$." "\n"
                   r"2. Compléter par $\ll$, $\gg$ ou $\sim$ : $2x^2\dots x$ ; $(x^3-3x^2+x)\dots x$ ; $(x^3-3x^2+x)\dots x^3$, en $0$ puis en $+\infty$." "\n"
                   r"3. En $0$ : $f(x)=x-\frac{x^2}2+o(x^2)$ et $g(x)=-1+x+3x^2-x^3+o(x^3)$. (a) Équivalent simple de $f$, en repartant de la définition. (b) Équivalent de $g(x)+1$ et de $h(x)=\sin(x)\,f(x)\,(g(x)+1)$. (c) DL de $f+g$ aux ordres $1$, $2$, $3$ quand c'est possible.",
         "parts": ["fd1", "fo4", "fq1", "fp5"]},
        {"id": "fx2", "kind": "multi", "src": f"{A30}, ex. 4 (développements limités)",
         "enonce": r"Rappeler les DL usuels utilisés." "\n"
                   r"1. DL en $0$ à l'ordre $3$ de $f(x)=\cos(x)e^{-2x}$." "\n"
                   r"2. (a) DL en $0$ à l'ordre $4$ de $g(x)=\frac1{\sqrt{1+x^2}}$. (b) DL en $0$ à l'ordre $4$ de $h(x)=\ln(1+g(x))$.",
         "parts": ["fp2", "fk3", "fk4"]},
        {"id": "fx3", "kind": "multi", "src": f"{A30}, ex. 5 (calcul de limites)",
         "enonce": r"1. Calculer $\displaystyle\lim_{x\to0}\frac{-1+x+\ln(1-x)+\cos x}{1-(1-x)^\pi}$." "\n"
                   r"2. Calculer $\displaystyle\lim_{x\to+\infty}\left(1+\sin\frac1x\right)^x$.",
         "parts": ["fa1", "fa2"]},
    ]},
    {"n": 11, "titre": "Examen + 20 %", "notions": ["limite-dl", "dl-operations"], "examen": True, "exos": [
        v("fz1", r"Calculer $\displaystyle\lim_{x\to0}\frac{e^x-\sqrt{1+2x}}{x^2}$.", "limit((exp(x)-sqrt(1+2*x))/x**2, x, 0)", "1",
          r"$\sqrt{1+2x}=1+x-\frac{x^2}2+o(x^2)$ et $e^x=1+x+\frac{x^2}2+o(x^2)$. Différence : $x^2+o(x^2)$. Limite $1$.", duree=7),
        v("fz2", r"DL de $\ln(1+x\sin x)$ en $0$ à l'ordre $4$.", dl("log(1+x*sin(x))", 4), "x**2-2*x**4/3",
          r"$u=x\sin x=x^2-\frac{x^4}6+o(x^4)$, $u^2=x^4+o(x^4)$. $\ln(1+u)=u-\frac{u^2}2=x^2-\frac{x^4}6-\frac{x^4}2=x^2-\frac{2x^4}3+o(x^4)$.", duree=7),
        v("fz3", r"Calculer $\displaystyle\lim_{x\to+\infty}\left(x^2\left(e^{1/x}-1\right)-x\right)$.", "limit(x**2*(exp(1/x)-1)-x, x, oo)", "Rational(1,2)",
          r"Avec $X=\frac1x\to0$ : $e^X-1=X+\frac{X^2}2+o(X^2)$, donc $x^2\left(e^{1/x}-1\right)=x+\frac12+o(1)$. Limite $\frac12$.", duree=7),
        v("fz4", r"Calculer $\displaystyle\lim_{x\to0}(\cos x)^{1/x^2}$.", "limit(cos(x)**(1/x**2), x, 0)", "exp(Rational(-1,2))",
          r"$(\cos x)^{1/x^2}=e^{\frac{\ln\cos x}{x^2}}$ et $\ln\cos x=\ln\left(1-\frac{x^2}2+o(x^2)\right)\sim-\frac{x^2}2$. L'exposant tend vers $-\frac12$ : limite $e^{-1/2}=\frac1{\sqrt e}$.", duree=7),
    ]},
    {"n": 12, "titre": "Examens 2028 et 2029", "notions": ["negligeable", "equivalent", "dl-usuels", "dl-operations", "limite-dl"], "examen": True, "exos": [
        o("fw1", r"1. Donner deux définitions de $f=o(g)$ et de $f\sim g$ en $x_0$. 2. Équivalent de $P(x)=2x^3-x^2+6x$ en $0$ et en $+\infty$. 3. Équivalents en $0$ de $f=\sin 2x$, $g=1-e^{-2x}$, $fg$ et $f-g$.",
          r"1. $f=o(g)\iff f=g\varepsilon$ avec $\varepsilon\to0\iff f/g\to0$. $f\sim g\iff f=g(1+\varepsilon)$ avec $\varepsilon\to0\iff f/g\to1$." "\n\n"
          r"2. En $+\infty$ : $P/2x^3=1-\frac1{2x}+\frac3{x^2}\to1$, $P\sim2x^3$. En $0$ : $P/6x=\frac{x^2}3-\frac x6+1\to1$, $P\sim6x$." "\n\n"
          r"3. $f=2x+o(x)\sim2x$ ; $g=1-(1-2x+o(x))\sim2x$ ; $fg\sim4x^2$. Pour $f-g$, il faut pousser les DL : $\sin2x=2x+o(x^2)$ et $g=2x-2x^2+o(x^2)$, donc $f-g=2x^2+o(x^2)\sim2x^2$ (on ne soustrait pas des équivalents).",
          src="Examen S2-B3 APEF mars 2024, ex. 4", duree=12),
        o("fw2", r"1. Condition nécessaire et suffisante sur $\alpha$ pour que $\dfrac{\ln x}{x^2}=o\!\left(\dfrac1{x^\alpha}\right)$ en $+\infty$. 2. DL d'ordre $3$ en $0$ d'une fonction avec $f(x)\sim-2x$ et $f(x)+2x=o(x^3)$.",
          r"1. Le quotient vaut $x^{\alpha-2}\ln x$. Si $\alpha\ge2$ il tend vers $+\infty$ ; si $\alpha<2$, croissances comparées : $0$. Condition : $\alpha<2$." "\n\n"
          r"2. $f(x)=-2x+o(x^3)$.",
          src="Examen S2-B3 APEF mars 2024, ex. 4", duree=8),
        v("fw3", r"Coefficient de $x^4$ dans le DL en $0$ de $\cos(x)\sqrt{1-x^2}$ ?", dl("cos(x)*sqrt(1-x**2)", 4) + ".coeff(x,4)", "Rational(1,6)",
          r"$\left(1-\frac{x^2}2+\frac{x^4}{24}\right)\left(1-\frac{x^2}2-\frac{x^4}8\right)=1-x^2+\frac{x^4}6+o(x^4)$.",
          src="Examen S2-B3 APEF mars 2024, ex. 5", duree=6),
        v("fw4", r"Coefficient de $x^3$ dans le DL en $0$ de $\ln(2-\sin x)$ ?", dl("log(2-sin(x))", 3) + ".coeff(x,3)", "Rational(1,24)",
          r"$\ln(2-\sin x)=\ln2+\ln\left(1-\frac x2+\frac{x^3}{12}\right)=\ln2-\frac x2-\frac{x^2}8+\frac{x^3}{24}+o(x^3)$.",
          src="Examen S2-B3 APEF mars 2024, ex. 5", duree=8),
        v("fw5", r"Calculer $\displaystyle\lim_{x\to+\infty}\left(1+\sin\frac1x\right)^x$.", "limit((1+sin(1/x))**x, x, oo)", "E",
          r"$\left(1+\sin\frac1x\right)^x=e^{x\ln(1+\frac1x+o(\frac1x))}=e^{1+o(1)}\to e$.",
          src="Examen S2-B3 APEF mars 2024, ex. 6", duree=6),
        v("fw6", r"Calculer $\displaystyle\lim_{x\to+\infty}\left(\cos\frac1x\right)^{x^2}$.", "limit(cos(1/x)**(x**2), x, oo)", "exp(-Rational(1,2))",
          r"$x^2\ln\cos\frac1x$ avec $t=\frac1x$ : $\ln\cos t=-\frac{t^2}2+o(t^2)$, donc l'exposant tend vers $-\frac12$ : limite $e^{-1/2}$.",
          src="Examen S2-B3 APEF mars 2025, ex. 5", duree=8),
        v("fw7", r"Coefficient de $x^4$ dans le DL en $0$ de $\ln(1+\cos x)$ ?", dl("log(1+cos(x))", 4) + ".coeff(x,4)", "-Rational(1,96)",
          r"$1+\cos x=2\left(1-\frac{x^2}4+\frac{x^4}{48}\right)$, puis $\ln(1+u)=u-\frac{u^2}2$ : $\ln2-\frac{x^2}4-\frac{x^4}{96}+o(x^4)$.",
          src="Examen S2-B3 APEF mars 2025, ex. 4", duree=8),
    ]},
]


# Variants (same method, other numbers): a failed exercise comes back with the next one; build.py checks calc == ans.
def _v(enonce, calc, ans, sol):
    return {"enonce": enonce, "calc": calc, "ans": ans, "sol": sol}


VARIANTS = {
    "fc1": [_v(r"$f(x)=\dfrac{x^2-4}{x-2}$ pour $x\ne2$. Quelle valeur donner à $f(2)$ pour que $f$ soit continue en $2$ ?", "limit((x**2-4)/(x-2), x, 2)", "4",
               r"$\frac{x^2-4}{x-2}=x+2\to4$.")],
    "fc2": [_v(r"$f(x)=\dfrac{\sin 2x}x$ pour $x\ne0$. Quelle valeur donner à $f(0)$ pour que $f$ soit continue en $0$ ?", "limit(sin(2*x)/x, x, 0)", "2",
               r"$\sin2x\sim2x$ : $f(0)=2$.")],
    "fc3": [_v(r"$f(x)=x+a$ si $x<2$ et $f(x)=x^2-1$ si $x\ge2$. Pour quelle valeur de $a$ la fonction $f$ est-elle continue en $2$ ?", "limit(x**2-1, x, 2)-2", "1",
               r"$2+a=3\iff a=1$.")],
    "fe2": [_v(r"Calculer $\displaystyle\lim_{x\to0}\frac{\sin 5x}{2x}$.", "limit(sin(5*x)/(2*x), x, 0)", "Rational(5,2)", r"$\sin5x\sim5x$ : limite $\frac52$.")],
    "fe3": [_v(r"Calculer $\displaystyle\lim_{x\to0}\frac{e^{3x}-1}{\sin x}$.", "limit((exp(3*x)-1)/sin(x), x, 0)", "3", r"$e^{3x}-1\sim3x$ et $\sin x\sim x$ : limite $3$.")],
    "fe4": [_v(r"Calculer $\displaystyle\lim_{x\to+\infty}\frac{x^3+2}{4x^3-x}$.", "limit((x**3+2)/(4*x**3-x), x, oo)", "Rational(1,4)", r"$\frac{x^3}{4x^3}=\frac14$.")],
    "fe6": [_v(r"Calculer $\displaystyle\lim_{x\to0}\frac{1-\cos 2x}{x^2}$.", "limit((1-cos(2*x))/x**2, x, 0)", "2", r"$1-\cos2x\sim\frac{(2x)^2}2=2x^2$ : limite $2$.")],
    "fy1": [_v(r"$f(0)=3$, $f'(0)=-1$, $f''(0)=2$. Donner la partie régulière du DL de $f$ en $0$ à l'ordre $2$.", "3-x+2*x**2/factorial(2)", "3-x+x**2",
               r"$3-x+\frac22x^2=3-x+x^2$.")],
    "fy2": [_v(r"Avec la formule de Taylor-Young, donner le DL de $e^{-x}$ en $0$ à l'ordre $3$.", dl("exp(-x)", 3), "1-x+x**2/2-x**3/6",
               r"$f^{(k)}(0)=(-1)^k$ : $e^{-x}=1-x+\frac{x^2}2-\frac{x^3}6+o(x^3)$.")],
    "fy3": [_v(r"Donner le DL de $\dfrac1x$ en $1$ à l'ordre $2$.", dl("1/x", 2, 1), "1-(x-1)+(x-1)**2",
               r"$f(1)=1$, $f'(1)=-1$, $f''(1)=2$ : $\frac1x=1-(x-1)+(x-1)^2+o\big((x-1)^2\big)$.")],
    "fy4": [_v(r"Avec la formule de Taylor-Young, donner le DL de $(1+x)^{1/3}$ en $0$ à l'ordre $2$.", dl("(1+x)**Rational(1,3)", 2), "1+x/3-x**2/9",
               r"$f'(0)=\frac13$, $f''(0)=-\frac29$ : $1+\frac x3-\frac{x^2}9+o(x^2)$.")],
    "fy5": [_v(r"On sait que $f(x)=1+4x-x^2+o(x^2)$ en $0$ et que $f$ est deux fois dérivable. Que vaut $f''(0)$ ?", "2*(-1)", "-2", r"$\frac{f''(0)}2=-1$, donc $f''(0)=-2$.")],
    "fu1": [_v(r"DL de $\sin 2x$ en $0$ à l'ordre $3$.", dl("sin(2*x)", 3), "2*x-4*x**3/3", r"$2x-\frac{(2x)^3}6=2x-\frac43x^3+o(x^3)$.")],
    "fu2": [_v(r"DL de $\cos 2x$ en $0$ à l'ordre $4$.", dl("cos(2*x)", 4), "1-2*x**2+2*x**4/3", r"$1-\frac{(2x)^2}2+\frac{(2x)^4}{24}=1-2x^2+\frac23x^4+o(x^4)$.")],
    "fu3": [_v(r"DL de $\ln(1-x)$ en $0$ à l'ordre $3$.", dl("log(1-x)", 3), "-x-x**2/2-x**3/3", r"$\ln(1+u)$ avec $u=-x$ : $-x-\frac{x^2}2-\frac{x^3}3+o(x^3)$.")],
    "fu4": [_v(r"DL de $\dfrac1{1-2x}$ en $0$ à l'ordre $3$.", dl("1/(1-2*x)", 3), "1+2*x+4*x**2+8*x**3", r"$1+2x+4x^2+8x^3+o(x^3)$.")],
    "fu5": [_v(r"DL de $\sqrt{1+x}$ en $0$ à l'ordre $3$.", dl("sqrt(1+x)", 3), "1+x/2-x**2/8+x**3/16", r"$1+\frac x2-\frac{x^2}8+\frac{x^3}{16}+o(x^3)$.")],
    "fu6": [_v(r"DL de $e^{3x}$ en $0$ à l'ordre $3$.", dl("exp(3*x)", 3), "1+3*x+9*x**2/2+9*x**3/2", r"$1+3x+\frac{9x^2}2+\frac{27x^3}6=1+3x+\frac92x^2+\frac92x^3+o(x^3)$.")],
    "fu7": [_v(r"DL de $\dfrac1{1+3x}$ en $0$ à l'ordre $2$.", dl("1/(1+3*x)", 2), "1-3*x+9*x**2", r"$1-3x+9x^2+o(x^2)$.")],
    "fp1": [_v(r"DL de $e^x-\cos x$ en $0$ à l'ordre $3$.", dl("exp(x)-cos(x)", 3), "x+x**2+x**3/6",
               r"$\left(1+x+\frac{x^2}2+\frac{x^3}6\right)-\left(1-\frac{x^2}2\right)=x+x^2+\frac{x^3}6+o(x^3)$.")],
    "fp3": [_v(r"DL de $e^x\cos x$ en $0$ à l'ordre $3$.", dl("exp(x)*cos(x)", 3), "1+x-x**3/3",
               r"$\left(1+x+\frac{x^2}2+\frac{x^3}6\right)\left(1-\frac{x^2}2\right)=1+x+\left(\frac16-\frac12\right)x^3+o(x^3)=1+x-\frac{x^3}3+o(x^3)$.")],
    "fp4": [_v(r"DL de $\dfrac{\sin x}{1-x}$ en $0$ à l'ordre $3$.", dl("sin(x)/(1-x)", 3), "x+x**2+5*x**3/6",
               r"$\left(x-\frac{x^3}6\right)(1+x+x^2)+o(x^3)=x+x^2+\frac{5x^3}6+o(x^3)$.")],
    "fk1": [_v(r"DL de $e^{x+x^2}$ en $0$ à l'ordre $2$.", dl("exp(x+x**2)", 2), "1+x+3*x**2/2",
               r"$u=x+x^2$, $u^2=x^2+o(x^2)$ : $1+u+\frac{u^2}2=1+x+\frac32x^2+o(x^2)$.")],
    "fk2": [_v(r"DL de $\ln(1+\sin x)$ en $0$ à l'ordre $3$.", dl("log(1+sin(x))", 3), "x-x**2/2+x**3/6",
               r"$u=x-\frac{x^3}6$, $u^2=x^2$, $u^3=x^3$ : $u-\frac{u^2}2+\frac{u^3}3=x-\frac{x^2}2+\frac{x^3}6+o(x^3)$.")],
    "fk5": [_v(r"DL de $\dfrac1{1+\sin x}$ en $0$ à l'ordre $2$.", dl("1/(1+sin(x))", 2), "1-x+x**2",
               r"$u=\sin x=x+o(x^2)$ : $\frac1{1+u}=1-u+u^2=1-x+x^2+o(x^2)$.")],
    "fl1": [_v(r"Calculer $\displaystyle\lim_{x\to0}\frac{e^{2x}-1-2x}{x^2}$.", "limit((exp(2*x)-1-2*x)/x**2, x, 0)", "2", r"$e^{2x}-1-2x=\frac{(2x)^2}2+o(x^2)=2x^2+o(x^2)$ : limite $2$.")],
    "fl2": [_v(r"Calculer $\displaystyle\lim_{x\to0}\frac{x-\sin x}{x^3}$.", "limit((x-sin(x))/x**3, x, 0)", "Rational(1,6)", r"$x-\sin x=\frac{x^3}6+o(x^3)$ : limite $\frac16$.")],
    "fl3": [_v(r"Calculer $\displaystyle\lim_{x\to0}\frac{\ln(1+x)-x+\frac{x^2}2}{x^3}$.", "limit((log(1+x)-x+x**2/2)/x**3, x, 0)", "Rational(1,3)",
               r"$\ln(1+x)=x-\frac{x^2}2+\frac{x^3}3+o(x^3)$ : limite $\frac13$.")],
    "fl4": [_v(r"Calculer $\displaystyle\lim_{x\to+\infty}\left(1+\frac2x\right)^x$.", "limit((1+2/x)**x, x, oo)", "E**2",
               r"$x\ln\left(1+\frac2x\right)=x\left(\frac2x+o\left(\frac1x\right)\right)\to2$. Limite : $e^2$.")],
    "fl5": [_v(r"Calculer $\displaystyle\lim_{x\to0}\frac{1-\cos x}{x\ln(1+x)}$.", "limit((1-cos(x))/(x*log(1+x)), x, 0)", "Rational(1,2)",
               r"$1-\cos x\sim\frac{x^2}2$ et $x\ln(1+x)\sim x^2$ : limite $\frac12$.")],
    "fl6": [_v(r"Calculer $\displaystyle\lim_{x\to0}\frac{e^x+e^{-x}-2}{x^2}$.", "limit((exp(x)+exp(-x)-2)/x**2, x, 0)", "1",
               r"$e^x+e^{-x}=2+x^2+o(x^2)$ : limite $1$.")],
}
for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["id"] in VARIANTS:
            _e["variants"] = VARIANTS[_e["id"]]


EXTRA_PARTS = [
    o("fd1", r"Donner deux définitions de chacune des notations $f=o(g)$ et $f\sim g$ au voisinage de $x_0$.",
      r"$f\sim g\iff\lim_{x\to x_0}\frac{f(x)}{g(x)}=1\iff f(x)=g(x)(1+\varepsilon(x))$ avec $\lim_{x_0}\varepsilon=0$." "\n\n"
      r"$f=o(g)\iff\lim_{x\to x_0}\frac{f(x)}{g(x)}=0\iff f(x)=g(x)\varepsilon(x)$ avec $\lim_{x_0}\varepsilon=0$."),
    o("fq1", r"Équivalent de $f(x)=x-\frac{x^2}2+o(x^2)$, de $g(x)+1$ et de $h(x)=\sin(x)f(x)(g(x)+1)$ en $0$.",
      r"(a) $f(x)=x-\frac{x^2}2+x^2\varepsilon(x)$, donc $\frac{f(x)}x=1-\frac x2+x\varepsilon(x)\to1$ : $f(x)\sim x$. (b) $g(x)+1\sim x$ ; $h(x)\sim x\times x\times x=x^3$."),
    v("fa1", r"Calculer $\displaystyle\lim_{x\to0}\frac{-1+x+\ln(1-x)+\cos x}{1-(1-x)^\pi}$.", "limit((-1+x+log(1-x)+cos(x))/(1-(1-x)**pi), x, 0)", "0",
      r"$N(x)=-1+x-x-\frac{x^2}2+1-\frac{x^2}2+o(x^2)=-x^2+o(x^2)\sim-x^2$. $D(x)=1-(1-\pi x+o(x))\sim\pi x$. $\frac ND\sim-\frac x\pi\to0$."),
    v("fa2", r"Calculer $\displaystyle\lim_{x\to+\infty}\left(1+\sin\frac1x\right)^x$.", "limit((1+sin(1/x))**x, x, oo)", "E",
      r"$\left(1+\sin\frac1x\right)^x=e^{x\ln(1+\sin\frac1x)}=e^{x\ln(1+\frac1x+o(\frac1x))}=e^{x(\frac1x+o(\frac1x))}=e^{1+o(1)}$. La limite vaut $e$."),
]

QUIZ = [
    {"notion": "continuite", "type": "qcm", "q": r"$f$ est continue en $a$ si et seulement si :",
     "choix": [r"$\lim_{x\to a}f(x)=f(a)$", r"$f$ est définie en $a$", r"$f$ est dérivable en $a$", r"$\lim_{a^-}f=\lim_{a^+}f$"], "bonne": 0},
    {"notion": "continuite", "type": "vf", "q": r"Toute fonction continue en $a$ est dérivable en $a$.", "bonne": False},
    {"notion": "tvi", "type": "vf", "q": r"Si $f$ est continue sur $[a,b]$ et $f(a)f(b)<0$, alors $f$ s'annule sur $]a,b[$.", "bonne": True},
    {"notion": "tvi", "type": "vf", "q": r"Le TVI donne l'unicité de la solution.", "bonne": False},
    {"notion": "negligeable", "type": "qcm", "q": r"Au voisinage de $0$, $o(x^2)+o(x^3)=$", "choix": [r"$o(x^2)$", r"$o(x^3)$", r"$o(x^5)$", r"$o(x)$ seulement"], "bonne": 0},
    {"notion": "negligeable", "type": "vf", "q": r"Au voisinage de $+\infty$, $x^2=o(x^3)$.", "bonne": True},
    {"notion": "equivalent", "type": "vf", "q": r"Si $f\sim g$ et $u\sim v$ alors $f+u\sim g+v$.", "bonne": False},
    {"notion": "equivalent", "type": "qcm", "q": r"En $0$, $e^x-1$ est équivalent à :", "choix": [r"$x$", r"$1$", r"$\frac{x^2}2$", r"$e^x$"], "bonne": 0},
    {"notion": "equivalent", "type": "vf", "q": r"Si $f\sim g$ alors $e^f\sim e^g$.", "bonne": False},
    {"notion": "taylor-young", "type": "qcm", "q": r"Dans le DL de $f$ en $0$, le coefficient de $x^2$ vaut :",
     "choix": [r"$\frac{f''(0)}2$", r"$f''(0)$", r"$2f''(0)$", r"$\frac{f'(0)}2$"], "bonne": 0},
    {"notion": "dl-usuels", "type": "qcm", "q": r"DL de $\ln(1+x)$ en $0$ à l'ordre $2$ :",
     "choix": [r"$x-\frac{x^2}2+o(x^2)$", r"$x+\frac{x^2}2+o(x^2)$", r"$1+x+\frac{x^2}2+o(x^2)$", r"$x-x^2+o(x^2)$"], "bonne": 0},
    {"notion": "dl-usuels", "type": "qcm", "q": r"DL de $\cos x$ en $0$ à l'ordre $2$ :",
     "choix": [r"$1-\frac{x^2}2+o(x^2)$", r"$1+\frac{x^2}2+o(x^2)$", r"$x-\frac{x^2}2+o(x^2)$", r"$1-x^2+o(x^2)$"], "bonne": 0},
    {"notion": "dl-operations", "type": "vf", "q": r"Pour un DL à l'ordre $3$ d'un produit, on peut jeter les termes de degré $>3$.", "bonne": True},
    {"notion": "limite-dl", "type": "qcm", "q": r"Pour étudier $u(x)^{v(x)}$ on écrit :", "choix": [r"$e^{v\ln u}$", r"$e^{u\ln v}$", r"$v\ln u$", r"$u^v\sim u$"], "bonne": 0},
]

_CONT = r"$f$ continue en $a$ $\iff\lim_{a^-}f=\lim_{a^+}f=f(a)$"
_TVI = r"TVI : $f$ continue sur $[a,b]$ et $f(a)f(b)<0$ $\Rightarrow\exists c\in\,]a,b[,\ f(c)=0$"
_O = r"$f=o(g)\iff\frac fg\to0$"
_EQ0 = r"en $0$ : $\sin x\sim x$, $e^x-1\sim x$, $\ln(1+x)\sim x$"
_EQQ = r"équivalent d'un quotient = quotient des équivalents"
_TY = r"$f(x)=\sum_{k=0}^n\frac{f^{(k)}(a)}{k!}(x-a)^k+o\big((x-a)^n\big)$"
_EXP = r"$e^u=1+u+\frac{u^2}2+\frac{u^3}6+o(u^3)$"
_COS = r"$\cos u=1-\frac{u^2}2+\frac{u^4}{24}+o(u^4)$"
_SIN = r"$\sin u=u-\frac{u^3}6+\frac{u^5}{120}+o(u^5)$"
_LN = r"$\ln(1+u)=u-\frac{u^2}2+\frac{u^3}3-\frac{u^4}4+o(u^4)$"
_GEO = r"$\frac1{1-u}=1+u+u^2+u^3+o(u^3)$"
_ALPHA = r"$(1+u)^\alpha=1+\alpha u+\frac{\alpha(\alpha-1)}2u^2+o(u^2)$"
_PROD = r"produit de DL : tronquer à l'ordre voulu"
_COMP = r"composition : poser $u\to0$, calculer $u^2$, $u^3$ à l'ordre voulu"
_POW = r"$a^b=e^{b\ln a}$"
FORMULES = {
    "fc1": r"$a^2-b^2=(a-b)(a+b)$ · prolongement par continuité : $f(a)=\lim_af$", "fc2": r"$\sin x\sim x$ en $0$ · prolongement par continuité : $f(a)=\lim_af$",
    "fc3": _CONT, "fc4": r"$|\sin|\le1$ · $|f|\le g$ et $g\to0\Rightarrow f\to0$ · $f$ continue en $a$ $\iff\lim_af=f(a)$", "fc5": _CONT,
    "ft1": _TVI + r" · strictement monotone $\Rightarrow$ au plus une solution", "ft2": _TVI + r" · $\cos0=1$, $\cos\frac\pi2=0$",
    "ft3": _TVI + r" (appliqué à $g(x)=f(x)-x$)", "ft4": _TVI + r" · polynôme $\sim$ terme de plus haut degré en $\pm\infty$", "ft5": _TVI + " · un contre-exemple suffit",
    "fo1": _O, "fo2": r"en $0$ : $o(x^p)+o(x^q)=o(x^{\min(p,q)})$ · $x^p\,o(x^q)=o(x^{p+q})$ · $o(x^p)\,o(x^q)=o(x^{p+q})$",
    "fo3": r"croissances comparées en $+\infty$ : $\ln x\ll x^a\ll e^x$ ($a>0$) · $x^a\ll x^b\iff a < b$",
    "fo4": _O + r" · $f\sim g\iff\frac fg\to1$ · polynôme : équivalent au terme de plus bas degré en $0$, de plus haut degré en $+\infty$",
    "fo5": _O + r" · $o(x^3)\Rightarrow o(x^2)$ en $0$ (pas l'inverse)",
    "fe1": r"polynôme : équivalent au terme de plus bas degré en $0$, de plus haut degré en $\pm\infty$",
    "fe2": _EQ0 + " · " + _EQQ, "fe3": _EQ0 + " · " + _EQQ, "fe4": r"fraction rationnelle en $\pm\infty$ : quotient des termes de plus haut degré",
    "fe5": r"$\sim$ compatible avec produit, quotient, puissance ; PAS avec la somme", "fe6": _COS + r" · $1-\cos x\sim\frac{x^2}2$",
    "fy1": _TY, "fy2": _TY + r" · $(e^x)'=e^x$", "fy3": _TY + r" · $(\ln x)'=\frac1x$", "fy4": _TY + r" · $(\sqrt u)'=\frac{u'}{2\sqrt u}$",
    "fy5": r"unicité du DL : coefficient de $x^k$ = $\frac{f^{(k)}(0)}{k!}$",
    "fu1": _SIN, "fu2": _COS, "fu3": _LN, "fu4": _GEO, "fu5": _ALPHA, "fu6": _EXP, "fu7": _GEO + r" avec $u=-x$",
    "fp1": _EXP + " · " + _COS, "fp2": _COS + " · " + _EXP + " · " + _PROD, "fp3": _EXP + " · " + _SIN + " · " + _PROD,
    "fp4": _LN + " · " + _GEO + " · " + _PROD, "fp5": r"$o(x^p)+o(x^q)=o(x^{\min(p,q)})$ : la somme n'est connue qu'à l'ordre le plus petit",
    "fk1": _SIN + " · " + _EXP + " · " + _COMP, "fk2": _COS + " · " + _LN + " · " + _COMP, "fk3": _ALPHA + r" avec $u=x^2$, $\alpha=-\frac12$",
    "fk4": r"$\ln(ab)=\ln a+\ln b$ · " + _LN + " · " + _COMP, "fk5": _SIN + r" · $\sqrt{1+u}=1+\frac u2-\frac{u^2}8+o(u^2)$",
    "fk6": r"$\tan=\frac{\sin}{\cos}$ · " + _SIN + " · " + _COS + " · " + _GEO,
    "fl1": _EXP + r" · $f\sim g\Rightarrow$ même limite", "fl2": _SIN, "fl3": _LN, "fl4": _POW + r" · $\ln(1+u)\sim u$ en $0$",
    "fl5": r"$1-\cos x\sim\frac{x^2}2$ · $\sin x\sim x$ · " + _EQQ, "fl6": _EXP + " · " + _COS,
    "fd1": _O + r" $\iff f=g\,\varepsilon$, $\varepsilon\to0$ · $f\sim g\iff\frac fg\to1\iff f=g(1+\varepsilon)$, $\varepsilon\to0$",
    "fw1": _O + r" · $f\sim g\iff\frac fg\to1$ · " + _EQ0 + r" · on ne soustrait pas des équivalents : pousser les DL", "fw2": _O + r" · croissances comparées : $x^a\ln x\to0$ pour $a<0$ en $+\infty$",
    "fw3": _COS + " · " + _ALPHA + " · " + _PROD, "fw4": _SIN + " · " + _LN + " · " + _COMP, "fw5": _POW + " · " + _LN + r" · $\sin t\sim t$",
    "fw6": _POW + " · " + _COS + " · " + _LN, "fw7": _COS + " · " + _LN + " · " + _COMP,
    "fq1": r"$f\sim$ premier terme non nul du DL · $o(x^2)=x^2\varepsilon(x)$ · $\sin x\sim x$ · équivalent d'un produit = produit des équivalents",
    "fa1": _LN + " · " + _COS + " · " + r"$(1+u)^\alpha=1+\alpha u+o(u)$ · " + _EQQ,
    "fa2": _POW + r" · $\sin u=u+o(u)$ · $\ln(1+u)=u+o(u)$",
    "fz1": r"$\sqrt{1+u}=1+\frac u2-\frac{u^2}8+o(u^2)$ · " + _EXP, "fz2": _SIN + " · " + _LN + " · " + _COMP,
    "fz3": r"poser $X=\frac1x\to0$ · " + _EXP, "fz4": _POW + " · " + _COS + r" · $\ln(1+u)\sim u$ en $0$",
}
