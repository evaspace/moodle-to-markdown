"""Level path: S3 maths, ECUE ASN (analyse et séries numériques).

Moodle course « Analyse, séries numériques » (chapters 05 to 15 : comparaisons de fonctions, développements limités,
séries à termes positifs, séries à termes quelconques). Calibrated on Examen B5/ASN octobre 2024 (dossier promo 2028,
corrigé officiel, ex. 1 : nature de trois séries ; ex. 2 : ln(n)/n^alpha selon alpha), `annales/raw/S3/Midterms/Maths PC/2028`.
Levels 1 and 2 are reminders of S1 (limites, croissances comparées) and S2 (DL usuels), because every later level uses them.
`value` exercises are checked by build.py (sympy, `coef(f, k)` = coefficient of x^k of the DL of f at 0);
`open` exercises (nature of a series) carry a full model answer.
"""

SUBJECT = {
    "id": "maths-s3-asn",
    "ordre": 240,
    "matiere": "maths",
    "semestre": "S3",
    "ecue": "ASN",
    "titre": "Analyse et séries numériques",
    "chapitres_moodle": ["Analyse, séries numériques"],
    "td": "TD et MiMos ASN (S3 2026)",
    "examens": ["Examen B5/ASN (octobre)"],
}

NOTIONS = [
    {"id": "croiss", "titre": "Limites usuelles et croissances comparées (rappel S1)",
     "formule": r"$\frac{(\ln n)^a}{n^b}\to0$ · $\frac{n^b}{q^n}\to0$ $(q>1)$ · $\frac{q^n}{n!}\to0$ · $\left(1+\frac an\right)^n\to e^a$",
     "exemple": r"$\frac{n^3}{2^n}\to0$ : l'exponentielle gagne sur la puissance",
     "cours": r"Ordre de domination en $+\infty$ : $\ln n\ll n^b\ll q^n\ll n!\ll n^n$. Une forme indéterminée se lève en factorisant le terme dominant. Rappel S1 : parcours « Suites numériques » (`maths-s1-apis-suites`)."},
    {"id": "dl-usuels", "titre": "DL usuels en 0 (rappel S2)",
     "formule": r"$e^x=\sum\frac{x^k}{k!}$ · $\sin x=x-\frac{x^3}6+\frac{x^5}{120}$ · $\cos x=1-\frac{x^2}2+\frac{x^4}{24}$ · $\ln(1+x)=x-\frac{x^2}2+\frac{x^3}3$ · $\frac1{1-x}=\sum x^k$ · $(1+x)^\alpha=1+\alpha x+\frac{\alpha(\alpha-1)}2x^2$",
     "exemple": r"$\sqrt{1+x}=1+\frac x2-\frac{x^2}8+\frac{x^3}{16}+o(x^3)$",
     "cours": r"Le coefficient de $x^k$ dans le DL de $f$ en 0 vaut $\frac{f^{(k)}(0)}{k!}$ (Taylor-Young). Ces sept DL sont à connaître par cœur. Rappel S2 : parcours « Fonctions » (`maths-s2-apef-fonctions`)."},
    {"id": "equiv", "titre": "Équivalents usuels",
     "formule": r"$\sin x\sim x$ · $e^x-1\sim x$ · $\ln(1+x)\sim x$ · $1-\cos x\sim\frac{x^2}2$ · $(1+x)^\alpha-1\sim\alpha x$ (en 0)",
     "exemple": r"$\frac{\sin 3x}{5x}\to\frac35$",
     "cours": r"$u\sim v\iff\frac uv\to1$. On peut multiplier, diviser, élever à une puissance des équivalents, **pas** les additionner ni les composer par une fonction quelconque. Pour une suite : $\ln(1+\frac1n)\sim\frac1n$, $\sin\frac1n\sim\frac1n$, $e^{1/n}-1\sim\frac1n$."},
    {"id": "dl-calc", "titre": "Calcul d'un DL : produit et composée",
     "formule": r"produit : on multiplie les polynômes et on tronque à l'ordre demandé · composée $f(u(x))$ : $u(x)\to0$, on injecte le DL de $u$ dans celui de $f$",
     "exemple": r"$e^x\cos x$ : coefficient de $x^3=\frac16-\frac12=-\frac13$",
     "cours": r"Pour le coefficient de $x^k$ d'un produit $f\times g$ : $\sum_{i+j=k}a_ib_j$. Pour $\frac1{1+x+x^2}$ : écrire $\frac{1-x}{1-x^3}$. On ne garde que les termes de degré $\le k$."},
    {"id": "dl-lim", "titre": "Limites par développements limités",
     "formule": r"$\lim\frac{f(x)-P(x)}{x^k}$ = coefficient de $x^k$ de $f$ quand $P$ est son DL à l'ordre $k-1$",
     "exemple": r"$\frac{x-\sin x}{x^3}\to\frac16$",
     "cours": r"On développe numérateur et dénominateur à l'ordre qui fait apparaître le premier terme non nul, puis on simplifie par la puissance de $x$ dominante. Penser à développer assez loin : un terme qui s'annule oblige à monter d'un ordre."},
    {"id": "geom-tele", "titre": "Séries géométriques et télescopiques",
     "formule": r"$\sum_{k\ge0}q^k=\frac1{1-q}$ $(|q|<1)$ · $\sum_{k\ge1}\frac1{k(k+1)}=\sum\left(\frac1k-\frac1{k+1}\right)=1$",
     "exemple": r"$\sum_{k\ge0}\left(-\frac13\right)^k=\frac1{1+1/3}=\frac34$",
     "cours": r"Série géométrique : première terme divisé par $1-q$. Série télescopique : décomposer en éléments simples, écrire la somme partielle $S_N$, passer à la limite. Rappel S1 : sommes de suites géométriques."},
    {"id": "div", "titre": "Condition nécessaire de convergence",
     "formule": r"$\sum u_n$ converge $\Rightarrow u_n\to0$ · $u_n\not\to0\Rightarrow\sum u_n$ diverge grossièrement",
     "exemple": r"$\sum\frac n{n+1}$ : $u_n\to1\ne0$, divergence grossière",
     "cours": r"La réciproque est **fausse** : $\sum\frac1n$ diverge bien que $\frac1n\to0$. Si $u_n\to0$ on ne peut rien conclure et il faut un autre critère."},
    {"id": "riemann", "titre": "Séries de Riemann",
     "formule": r"$\sum\frac1{n^\alpha}$ converge $\iff\alpha>1$",
     "exemple": r"$\sum\frac1{n^2}$ converge ; $\sum\frac1{\sqrt n}$ et $\sum\frac1n$ divergent",
     "cours": r"C'est la série de référence pour comparer. Pour un terme général $u_n\sim\frac c{n^p}$ : converge $\iff p>1$. L'exposant se lit sur $-\frac{\ln u_n}{\ln n}\to p$."},
    {"id": "comp", "titre": "Séries à termes positifs : comparaison",
     "formule": r"$0\le u_n\le v_n$ : $\sum v_n$ converge $\Rightarrow\sum u_n$ converge · $u_n\sim v_n$ (positifs) : même nature · $u_n=o(v_n)$ : $\sum v_n$ converge $\Rightarrow\sum u_n$ converge",
     "exemple": r"$\frac{\ln n}{n^2}=o\left(\frac1{n^{3/2}}\right)$ donc converge",
     "cours": r"Toujours vérifier le signe avant d'utiliser un équivalent. Choisir la référence $\frac1{n^\beta}$ avec $\beta$ entre 1 et l'exposant pour les puissances de $\ln n$ (croissances comparées)."},
    {"id": "dalembert", "titre": "Règle de d'Alembert",
     "formule": r"$u_n>0$ et $\frac{u_{n+1}}{u_n}\to\ell$ : $\ell<1$ converge · $\ell>1$ diverge · $\ell=1$ on ne conclut pas",
     "exemple": r"$u_n=\frac n{2^n}$ : $\frac{u_{n+1}}{u_n}=\frac{n+1}{2n}\to\frac12<1$",
     "cours": r"Adaptée aux factorielles et aux produits $a^n$. Elle ne dit rien pour $\ell=1$ (séries de Riemann). Pour un terme de signe quelconque, l'appliquer à $|u_n|$."},
    {"id": "cauchy", "titre": "Règle de Cauchy",
     "formule": r"$\sqrt[n]{u_n}\to\ell$ : $\ell<1$ converge · $\ell>1$ diverge · $\ell=1$ on ne conclut pas",
     "exemple": r"$u_n=\frac{n^3}{3^n}$ : $\sqrt[n]{u_n}=\frac{e^{3\ln n/n}}3\to\frac13<1$",
     "cours": r"Adaptée aux puissances $n$-ièmes : $\left(\frac n{2n+1}\right)^n$. On écrit $\sqrt[n]{u_n}=e^{\frac1n\ln u_n}$. Même cas d'indécision que d'Alembert."},
    {"id": "abs", "titre": "Convergence absolue et séries alternées",
     "formule": r"$\sum|u_n|$ converge $\Rightarrow\sum u_n$ converge · séries alternées : $|u_n|\searrow0\Rightarrow\sum(-1)^n|u_n|$ converge",
     "exemple": r"$\sum\frac{\sin n}{n^2}$ : $\left|\frac{\sin n}{n^2}\right|\le\frac1{n^2}$, convergence absolue",
     "cours": r"Pour un signe quelconque, étudier d'abord $\sum|u_n|$. Une série alternée dont $|u_n|\not\searrow0$ peut diverger : développer $u_n$ (DL) pour isoler un terme positif de série divergente."},
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


ASN = "Examen B5/ASN octobre 2024"

LEVELS = [
    {"n": 1, "titre": "Rappel S1 : limites et croissances comparées", "notions": ["croiss"], "exos": [
        v("c1", r"Limite de $\frac{n^2}{2^n}$ ?", "limit(n**2/2**n, n, oo)", "0", r"Croissances comparées : $2^n\gg n^2$, donc $\frac{n^2}{2^n}\to0$."),
        v("c2", r"Limite de $\frac{\ln n}{\sqrt n}$ ?", "limit(log(n)/sqrt(n), n, oo)", "0", r"$\frac{(\ln n)^a}{n^b}\to0$ avec $a=1$, $b=\frac12$."),
        v("c3", r"Limite de $\frac{3^n}{n!}$ ?", "limit(3**n/factorial(n), n, oo)", "0", r"$\frac{q^n}{n!}\to0$ pour tout $q$."),
        v("c4", r"Limite de $\frac{e^n}{n^5}$ ?", "limit(exp(n)/n**5, n, oo)", "oo", r"L'exponentielle domine : $\frac{e^n}{n^5}\to+\infty$."),
        v("c5", r"Limite de $\left(1+\frac1n\right)^n$ ?", "limit((1+1/n)**n, n, oo)", "E", r"$\left(1+\frac an\right)^n\to e^a$ avec $a=1$ : la limite est $e$."),
        v("c6", r"Limite de $n\sin\frac1n$ ?", "limit(n*sin(1/n), n, oo)", "1", r"$\sin\frac1n\sim\frac1n$, donc $n\sin\frac1n\to1$."),
    ]},
    {"n": 2, "titre": "Rappel S2 : DL usuels en 0", "notions": ["dl-usuels"], "exos": [
        v("d1", r"Coefficient de $x^4$ dans le DL de $e^x$ en 0 ?", "coef(exp(x), 4)", "Rational(1,24)", r"$\frac1{4!}=\frac1{24}$."),
        v("d2", r"Coefficient de $x^5$ dans le DL de $\sin x$ en 0 ?", "coef(sin(x), 5)", "Rational(1,120)", r"$\sin x=x-\frac{x^3}6+\frac{x^5}{120}$ : le coefficient est $\frac1{5!}=\frac1{120}$."),
        v("d3", r"Coefficient de $x^2$ dans le DL de $\cos x$ en 0 ?", "coef(cos(x), 2)", "Rational(-1,2)", r"$\cos x=1-\frac{x^2}2+\dots$ : $-\frac12$."),
        v("d4", r"Coefficient de $x^4$ dans le DL de $\ln(1+x)$ en 0 ?", "coef(log(1+x), 4)", "Rational(-1,4)", r"$\ln(1+x)=\sum(-1)^{k+1}\frac{x^k}k$ : pour $k=4$, $-\frac14$."),
        v("d5", r"Coefficient de $x^2$ dans le DL de $\sqrt{1+x}$ en 0 ?", "coef(sqrt(1+x), 2)", "Rational(-1,8)", r"$\frac{\alpha(\alpha-1)}2$ avec $\alpha=\frac12$ : $\frac{\frac12\times(-\frac12)}2=-\frac18$."),
        v("d6", r"Coefficient de $x^7$ dans le DL de $\frac1{1-x}$ en 0 ?", "coef(1/(1-x), 7)", "1", r"$\frac1{1-x}=\sum x^k$ : tous les coefficients valent 1."),
    ]},
    {"n": 3, "titre": "Équivalents usuels", "notions": ["equiv"], "exos": [
        v("e1", r"Limite en $0$ de $\frac{\sin 3x}{5x}$ ?", "limit(sin(3*x)/(5*x), x, 0)", "Rational(3,5)", r"$\sin3x\sim3x$, donc $\frac{3x}{5x}=\frac35$."),
        v("e2", r"Limite en $0$ de $\frac{e^{2x}-1}x$ ?", "limit((exp(2*x)-1)/x, x, 0)", "2", r"$e^{2x}-1\sim2x$."),
        v("e3", r"Limite en $0$ de $\frac{\ln(1+x^2)}{x^2}$ ?", "limit(log(1+x**2)/x**2, x, 0)", "1", r"$\ln(1+u)\sim u$ avec $u=x^2\to0$."),
        v("e4", r"Limite en $0$ de $\frac{1-\cos x}{x^2}$ ?", "limit((1-cos(x))/x**2, x, 0)", "Rational(1,2)", r"$1-\cos x\sim\frac{x^2}2$."),
        v("e5", r"Limite en $+\infty$ de $\frac{\sqrt{n^2+n}}n$ ?", "limit(sqrt(n**2+n)/n, n, oo)", "1", r"$\sqrt{n^2+n}=n\sqrt{1+\frac1n}\sim n$."),
        v("e6", r"Limite en $+\infty$ de $\frac{\ln(n+1)}{\ln n}$ ?", "limit(log(n+1)/log(n), n, oo)", "1", r"$\ln(n+1)=\ln n+\ln\left(1+\frac1n\right)\sim\ln n$."),
    ]},
    {"n": 4, "titre": "Calcul d'un DL : produit et composée", "notions": ["dl-calc"], "exos": [
        v("p1", r"Coefficient de $x^3$ dans le DL de $e^x\cos x$ en 0 ?", "coef(exp(x)*cos(x), 3)", "Rational(-1,3)", r"$e^x=1+x+\frac{x^2}2+\frac{x^3}6$, $\cos x=1-\frac{x^2}2$ : $x^3$ : $\frac16+1\times\left(-\frac12\right)=-\frac13$."),
        v("p2", r"Coefficient de $x^3$ dans le DL de $e^x\sin x$ en 0 ?", "coef(exp(x)*sin(x), 3)", "Rational(1,3)", r"$\sin x=x-\frac{x^3}6$ : $x^3$ : $\frac12\times1+1\times\left(-\frac16\right)=\frac13$."),
        v("p3", r"Coefficient de $x^2$ dans le DL de $\ln(1+\sin x)$ en 0 ?", "coef(log(1+sin(x)), 2)", "Rational(-1,2)", r"$u=\sin x=x+o(x^2)$ ; $\ln(1+u)=u-\frac{u^2}2$ : $x^2$ : $-\frac12$."),
        v("p4", r"Coefficient de $x^3$ dans le DL de $\frac1{1+x+x^2}$ en 0 ?", "coef(1/(1+x+x**2), 3)", "1", r"$\frac1{1+x+x^2}=\frac{1-x}{1-x^3}=(1-x)(1+x^3+\dots)=1-x+x^3-\dots$ : le coefficient de $x^3$ est $1$."),
        v("p5", r"Coefficient de $x^3$ dans le DL de $\frac{e^x}{1-x}$ en 0 ?", "coef(exp(x)/(1-x), 3)", "Rational(8,3)", r"Coefficient de $\frac1{1-x}\times e^x$ : somme des $\frac1{k!}$ pour $k\le3$ : $1+1+\frac12+\frac16=\frac83$."),
        v("p6", r"Coefficient de $x^2$ dans le DL de $\cos^2x$ en 0 ?", "coef(cos(x)**2, 2)", "-1", r"$\cos^2x=\left(1-\frac{x^2}2\right)^2=1-x^2+\dots$ : $-1$."),
    ]},
    {"n": 5, "titre": "Limites par développements limités", "notions": ["dl-lim", "dl-usuels"], "exos": [
        v("l1", r"Limite en $0$ de $\frac{e^x-1-x}{x^2}$ ?", "limit((exp(x)-1-x)/x**2, x, 0)", "Rational(1,2)", r"$e^x-1-x=\frac{x^2}2+o(x^2)$."),
        v("l2", r"Limite en $0$ de $\frac{x-\sin x}{x^3}$ ?", "limit((x-sin(x))/x**3, x, 0)", "Rational(1,6)", r"$x-\sin x=\frac{x^3}6+o(x^3)$."),
        v("l3", r"Limite en $0$ de $\frac{\cos x-1+\frac{x^2}2}{x^4}$ ?", "limit((cos(x)-1+x**2/2)/x**4, x, 0)", "Rational(1,24)", r"$\cos x=1-\frac{x^2}2+\frac{x^4}{24}+o(x^4)$."),
        v("l4", r"Limite en $0$ de $\frac{e^x-\cos x-x}{x^2}$ ?", "limit((exp(x)-cos(x)-x)/x**2, x, 0)", "1", r"$e^x-\cos x-x=\left(\frac{x^2}2\right)-\left(-\frac{x^2}2\right)+o(x^2)=x^2+o(x^2)$."),
        v("l5", r"Limite en $0$ de $\frac1{x^2}-\frac1{\sin^2x}$ ?", "limit(1/x**2-1/sin(x)**2, x, 0)", "Rational(-1,3)", r"$\sin^2x=x^2-\frac{x^4}3+o(x^4)$, donc $\frac1{\sin^2x}=\frac1{x^2}\left(1+\frac{x^2}3+o(x^2)\right)=\frac1{x^2}+\frac13+o(1)$ : la limite vaut $-\frac13$."),
        v("l6", r"Limite en $0$ de $\frac{\ln(1+x)-x}{x^2}$ ?", "limit((log(1+x)-x)/x**2, x, 0)", "Rational(-1,2)", r"$\ln(1+x)-x=-\frac{x^2}2+o(x^2)$."),
    ]},
    {"n": 6, "titre": "Séries géométriques et télescopiques", "notions": ["geom-tele"], "exos": [
        v("s1", r"Calculer $\sum_{k=0}^{+\infty}\left(\frac12\right)^k$.", "summation(Rational(1,2)**k, (k, 0, oo))", "2", r"$\frac1{1-\frac12}=2$."),
        v("s2", r"Calculer $\sum_{k=1}^{+\infty}\frac1{k(k+1)}$.", "summation(1/(k*(k+1)), (k, 1, oo))", "1", r"$\frac1{k(k+1)}=\frac1k-\frac1{k+1}$ : $S_N=1-\frac1{N+1}\to1$."),
        v("s3", r"Calculer $\sum_{k=1}^{+\infty}\left(\frac23\right)^k$.", "summation(Rational(2,3)**k, (k, 1, oo))", "2", r"$\frac{q}{1-q}=\frac{2/3}{1/3}=2$ (la somme commence à $k=1$)."),
        v("s4", r"Calculer $\sum_{k=1}^{+\infty}\frac1{k(k+2)}$.", "summation(1/(k*(k+2)), (k, 1, oo))", "Rational(3,4)", r"$\frac1{k(k+2)}=\frac12\left(\frac1k-\frac1{k+2}\right)$ : $S_N=\frac12\left(1+\frac12-\frac1{N+1}-\frac1{N+2}\right)\to\frac34$."),
        v("s5", r"Calculer $\sum_{k=0}^{+\infty}\left(-\frac13\right)^k$.", "summation((-Rational(1,3))**k, (k, 0, oo))", "Rational(3,4)", r"$\frac1{1-q}$ avec $q=-\frac13$ : $\frac1{4/3}=\frac34$."),
        v("s6", r"Calculer $\sum_{k=2}^{+\infty}\frac1{k^2-1}$.", "summation(1/(k**2-1), (k, 2, oo))", "Rational(3,4)", r"$\frac1{k^2-1}=\frac12\left(\frac1{k-1}-\frac1{k+1}\right)$ : $S_N=\frac12\left(1+\frac12-\frac1N-\frac1{N+1}\right)\to\frac34$."),
    ]},
    {"n": 7, "titre": "Condition nécessaire de convergence", "notions": ["div"], "exos": [
        o("g1", r"Étudier la nature de $\sum\frac n{n+1}$.", r"$u_n=\frac n{n+1}\to1\ne0$ : la série diverge grossièrement.", duree=2),
        o("g2", r"Étudier la nature de $\sum\left(1+\frac1n\right)^n$.", r"$u_n\to e\ne0$ : divergence grossière.", duree=2),
        o("g3", r"Étudier la nature de $\sum\cos\frac1n$.", r"$\cos\frac1n\to1\ne0$ : divergence grossière.", duree=2),
        o("g4", r"Étudier la nature de $\sum(-1)^n$.", r"$(-1)^n$ n'a pas de limite, donc ne tend pas vers $0$ : divergence grossière.", duree=2),
        o("g5", r"$\frac1n\to0$ : peut-on en déduire que $\sum\frac1n$ converge ? Montrer que $\sum\frac1n$ diverge.",
          r"Non, la réciproque de la condition nécessaire est fausse. Comme $\ln\left(1+\frac1k\right)\le\frac1k$, $\sum_{k=1}^n\frac1k\ge\sum_{k=1}^n\ln\frac{k+1}k=\ln(n+1)\to+\infty$ : la série harmonique diverge.", duree=4),
        o("g6", r"Si $u_n\to0$, que peut-on dire de la nature de $\sum u_n$ ?", r"Rien : $\sum\frac1n$ diverge et $\sum\frac1{n^2}$ converge, toutes deux avec $u_n\to0$. Il faut un autre critère (comparaison, d'Alembert...).", duree=2),
    ]},
    {"n": 8, "titre": "Séries de Riemann", "notions": ["riemann"], "exos": [
        o("r1", r"Nature de $\sum\frac1{n^2}$ ?", r"Série de Riemann avec $\alpha=2>1$ : elle converge.", duree=1),
        o("r2", r"Nature de $\sum\frac1{\sqrt n}$ ?", r"Riemann avec $\alpha=\frac12\le1$ : elle diverge.", duree=1),
        o("r3", r"Nature de $\sum\frac1{n^{3/2}}$ ?", r"Riemann avec $\alpha=\frac32>1$ : elle converge.", duree=1),
        o("r4", r"Pour quelles valeurs du réel $\alpha$ la série $\sum\frac1{n^\alpha}$ converge-t-elle ?", r"Exactement pour $\alpha>1$.", duree=1),
        v("r5", r"$u_n=\frac{\sqrt n}{n^2+1}\sim\frac1{n^p}$. Quelle est la valeur de $p$ ? (la série converge-t-elle ?)", "limit(-log(sqrt(n)/(n**2+1))/log(n), n, oo)", "Rational(3,2)",
          r"$u_n\sim\frac{n^{1/2}}{n^2}=\frac1{n^{3/2}}$ : $p=\frac32>1$, la série converge."),
        v("r6", r"$u_n=\frac{n+1}{n^3+n}\sim\frac1{n^p}$. Quelle est la valeur de $p$ ? (la série converge-t-elle ?)", "limit(-log((n+1)/(n**3+n))/log(n), n, oo)", "2",
          r"$u_n\sim\frac n{n^3}=\frac1{n^2}$ : $p=2>1$, la série converge."),
    ]},
    {"n": 9, "titre": "Séries à termes positifs : comparaison", "notions": ["comp", "riemann", "equiv"], "exos": [
        o("k1", r"Nature de $\sum\frac1{n^2+n}$ ?", r"$0\le\frac1{n^2+n}\le\frac1{n^2}$ et $\sum\frac1{n^2}$ converge : la série converge.", duree=2),
        o("k2", r"Nature de $\sum\frac1{\sqrt n+1}$ ?", r"$\frac1{\sqrt n+1}\sim\frac1{\sqrt n}$ (termes positifs), et $\sum\frac1{\sqrt n}$ diverge ($\alpha=\frac12$) : la série diverge.", duree=2),
        o("k3", r"Nature de $\sum\sin\frac1{n^2}$ ?", r"Pour $n\ge1$, $\sin\frac1{n^2}>0$ et $\sin\frac1{n^2}\sim\frac1{n^2}$ : même nature que $\sum\frac1{n^2}$, convergente.", duree=2),
        o("k4", r"Nature de $\sum\ln\left(1+\frac1n\right)$ ?", r"$\ln\left(1+\frac1n\right)\sim\frac1n>0$ : même nature que la série harmonique, elle diverge.", duree=2),
        o("k5", r"Nature de $\sum\left(e^{1/n}-1\right)$ ?", r"$e^{1/n}-1\sim\frac1n>0$ : elle diverge.", duree=2),
        o("k6", r"Nature de $\sum\frac{\ln n}{n^2}$ ?", r"Par croissances comparées, $\frac{\ln n}{n^2}=\frac{\ln n}{\sqrt n}\times\frac1{n^{3/2}}=o\left(\frac1{n^{3/2}}\right)$ et $\sum\frac1{n^{3/2}}$ converge : la série converge.", duree=3),
    ]},
    {"n": 10, "titre": "Règle de d'Alembert", "notions": ["dalembert"], "exos": [
        v("a1", r"$u_n=\frac n{2^n}$. Calculer $\lim\frac{u_{n+1}}{u_n}$ puis conclure.", "limit(((n+1)/2**(n+1))/(n/2**n), n, oo)", "Rational(1,2)",
          r"$\frac{u_{n+1}}{u_n}=\frac{n+1}{2n}\to\frac12<1$ : la série converge."),
        v("a2", r"$u_n=\frac{3^n}{n!}$. Calculer $\lim\frac{u_{n+1}}{u_n}$ puis conclure.", "limit((3**(n+1)/factorial(n+1))/(3**n/factorial(n)), n, oo)", "0",
          r"$\frac{u_{n+1}}{u_n}=\frac3{n+1}\to0<1$ : la série converge."),
        v("a3", r"$u_n=\frac{n^2}{e^n}$. Calculer $\lim\frac{u_{n+1}}{u_n}$ puis conclure.", "limit(((n+1)**2/exp(n+1))/(n**2/exp(n)), n, oo)", "exp(-1)",
          r"$\frac{u_{n+1}}{u_n}=\left(\frac{n+1}n\right)^2e^{-1}\to\frac1e<1$ : la série converge."),
        v("a4", r"$u_n=\frac{n!}{n^n}$. Calculer $\lim\frac{u_{n+1}}{u_n}$ puis conclure.", "limit(factorial(n+1)/(n+1)**(n+1)*n**n/factorial(n), n, oo)", "exp(-1)",
          r"$\frac{u_{n+1}}{u_n}=\frac{(n+1)!\,n^n}{(n+1)^{n+1}n!}=\left(\frac n{n+1}\right)^n=\left(1+\frac1n\right)^{-n}\to\frac1e<1$ : la série converge."),
        v("a5", r"$u_n=\frac{2^n}{n^2}$. Calculer $\lim\frac{u_{n+1}}{u_n}$ puis conclure.", "limit((2**(n+1)/(n+1)**2)/(2**n/n**2), n, oo)", "2",
          r"$\frac{u_{n+1}}{u_n}=2\left(\frac n{n+1}\right)^2\to2>1$ : la série diverge."),
        o("a6", r"Que dit la règle de d'Alembert pour $\sum\frac1n$ et $\sum\frac1{n^2}$ ? Que conclure ?", r"Dans les deux cas $\frac{u_{n+1}}{u_n}\to1$ : la règle ne permet pas de conclure, alors que la première diverge et la seconde converge. Il faut comparer avec Riemann.", duree=3),
    ]},
    {"n": 11, "titre": "Règle de Cauchy", "notions": ["cauchy"], "exos": [
        v("h1", r"$u_n=\frac{n^3}{3^n}$. Calculer $\lim\sqrt[n]{u_n}$ puis conclure.", "limit(exp(log(n**3/3**n)/n), n, oo)", "Rational(1,3)",
          r"$\sqrt[n]{u_n}=\frac{n^{3/n}}3=\frac{e^{3\ln n/n}}3\to\frac13<1$ : la série converge."),
        v("h2", r"$u_n=\left(\frac n{2n+1}\right)^n$. Calculer $\lim\sqrt[n]{u_n}$ puis conclure.", "limit(n/(2*n+1), n, oo)", "Rational(1,2)",
          r"$\sqrt[n]{u_n}=\frac n{2n+1}\to\frac12<1$ : la série converge."),
        v("h3", r"$u_n=\left(1+\frac1n\right)^{-n^2}$. Calculer $\lim\sqrt[n]{u_n}$ puis conclure.", "limit((1+1/n)**(-n), n, oo)", "exp(-1)",
          r"$\sqrt[n]{u_n}=\left(1+\frac1n\right)^{-n}\to\frac1e<1$ : la série converge."),
        v("h4", r"$u_n=\left(\frac{2n+1}{n+3}\right)^n$. Calculer $\lim\sqrt[n]{u_n}$ puis conclure.", "limit((2*n+1)/(n+3), n, oo)", "2",
          r"$\sqrt[n]{u_n}=\frac{2n+1}{n+3}\to2>1$ : la série diverge."),
        v("h5", r"$u_n=\left(\frac{\ln n}n\right)^n$. Calculer $\lim\sqrt[n]{u_n}$ puis conclure.", "limit(log(n)/n, n, oo)", "0",
          r"$\sqrt[n]{u_n}=\frac{\ln n}n\to0<1$ : la série converge."),
        v("h6", r"$u_n=\frac{n^2}{2^n}$. Calculer $\lim\sqrt[n]{u_n}$ puis conclure.", "limit(exp(log(n**2/2**n)/n), n, oo)", "Rational(1,2)",
          r"$\sqrt[n]{u_n}=\frac{n^{2/n}}2\to\frac12<1$ : la série converge."),
    ]},
    {"n": 12, "titre": "Convergence absolue et séries alternées", "notions": ["abs"], "exos": [
        o("b1", r"Nature de $\sum\frac{\sin n}{n^2}$ ?", r"$\left|\frac{\sin n}{n^2}\right|\le\frac1{n^2}$ et $\sum\frac1{n^2}$ converge : la série converge absolument, donc converge.", duree=3),
        o("b2", r"Nature de $\sum\frac{(-1)^n}{\sqrt n}$ ?", r"Série alternée, $\frac1{\sqrt n}$ décroît vers $0$ : elle converge (critère des séries alternées). Elle ne converge pas absolument car $\sum\frac1{\sqrt n}$ diverge.", duree=3),
        o("b3", r"Nature de $\sum\frac{(-1)^nn}{n+1}$ ?", r"$|u_n|=\frac n{n+1}\to1$ : $u_n\not\to0$, divergence grossière (le critère des séries alternées ne s'applique pas).", duree=3),
        o("b4", r"Nature de $\sum\frac{(-1)^n}{\ln n}$ ($n\ge2$) ?", r"$\frac1{\ln n}$ décroît vers $0$ : série alternée convergente. Pas absolument convergente : $\frac1{\ln n}\ge\frac1n$ et $\sum\frac1n$ diverge.", duree=3),
        o("b5", r"Nature de $\sum\frac{\cos n}{n^2+1}$ ?", r"$\left|\frac{\cos n}{n^2+1}\right|\le\frac1{n^2}$ : convergence absolue, donc convergence.", duree=3),
        o("b6", r"$\sum|u_n|$ diverge. Peut-on dire que $\sum u_n$ diverge ?", r"Non : $u_n=\frac{(-1)^n}n$ converge (alternée) alors que $\sum|u_n|=\sum\frac1n$ diverge.", duree=3),
    ]},
    {"n": 13, "titre": "Niveau examen : B5/ASN octobre 2024", "notions": ["abs", "dalembert", "cauchy", "comp", "riemann"], "examen": True, "exos": [
        {"id": "mx1", "kind": "multi", "src": f"{ASN}, ex. 1 (9 points)",
         "enonce": r"Déterminer la nature des séries de terme général (justifier proprement) :" "\n"
                   r"1. $u_n=\frac{\sin n}{n^2}$. 2. $u_n=\frac{n^3}{3^n}$. 3. $u_n=\frac{(-1)^nn}{e^n}$.",
         "parts": ["x1a", "x1b", "x1c"]},
        {"id": "mx2", "kind": "multi", "src": f"{ASN}, ex. 2 (6 points)",
         "enonce": r"Soit $\alpha\in\mathbb R$. On étudie la nature de $\sum\frac{\ln n}{n^\alpha}$." "\n"
                   r"1. Montrer que pour tout $\beta<\alpha$, $\frac{\ln n}{n^\alpha}=o\left(\frac1{n^\beta}\right)$." "\n"
                   r"2. En déduire que la série converge si $\alpha>1$. 3. Montrer qu'elle diverge si $\alpha\le1$.",
         "parts": ["x2a", "x2b", "x2c"]},
        o("x3", r"Nature de $\sum\frac{n!}{n^n}\times\frac{(-1)^n}{2}$, puis de $\sum\left(\frac{\ln n}{n}\right)^n\sin n$ ?",
          r"1. $\left|\frac{(-1)^nn!}{2n^n}\right|=\frac{n!}{2n^n}$ ; d'Alembert : $\frac{u_{n+1}}{u_n}=\left(1+\frac1n\right)^{-n}\to\frac1e<1$ : convergence absolue, donc convergence. 2. $\left|\left(\frac{\ln n}n\right)^n\sin n\right|\le\left(\frac{\ln n}n\right)^n$ et Cauchy : $\frac{\ln n}n\to0<1$ : convergence absolue, donc convergence.",
          src=f"{ASN}, style ex. 1", duree=10),
    ]},
    {"n": 14, "titre": "Plus dur que l'examen (+20 %)", "notions": ["comp", "abs", "dl-lim", "equiv"], "examen": True, "exos": [
        o("z1", r"Montrer que $\sum\left(\frac1n-\ln\left(1+\frac1n\right)\right)$ converge.",
          r"$\ln(1+u)=u-\frac{u^2}2+o(u^2)$ avec $u=\frac1n$ : $\frac1n-\ln\left(1+\frac1n\right)=\frac1{2n^2}+o\left(\frac1{n^2}\right)\sim\frac1{2n^2}>0$. Même nature que $\sum\frac1{n^2}$ : elle converge.", duree=8),
        o("z2", r"Étudier la nature de $\sum\frac{(-1)^n}{\sqrt n+(-1)^n}$ ($n\ge2$).",
          r"$u_n=\frac{(-1)^n}{\sqrt n}\cdot\frac1{1+\frac{(-1)^n}{\sqrt n}}=\frac{(-1)^n}{\sqrt n}\left(1-\frac{(-1)^n}{\sqrt n}+O\left(\frac1n\right)\right)=\frac{(-1)^n}{\sqrt n}-\frac1n+O\left(\frac1{n^{3/2}}\right)$. $\sum\frac{(-1)^n}{\sqrt n}$ converge, $\sum O\left(\frac1{n^{3/2}}\right)$ converge, mais $\sum\frac1n$ diverge : la série **diverge**, bien que $|u_n|$ n'ait pas de signe constant. (Le critère des séries alternées ne s'applique pas : $|u_n|$ n'est pas décroissante.)", duree=12),
        o("z3", r"Étudier la nature de $\sum\frac{(\ln n)^2}{n^{3/2}}$.",
          r"Croissances comparées : $(\ln n)^2=o(n^{1/4})$, donc $\frac{(\ln n)^2}{n^{3/2}}=o\left(\frac1{n^{5/4}}\right)$ et $\sum\frac1{n^{5/4}}$ converge ($\frac54>1)$ : la série converge.", duree=8),
        o("z4", r"Étudier la nature de $\sum\left(\sqrt{n+1}-\sqrt n\right)$ et de $\sum\left(\sqrt{n+1}-\sqrt n\right)^2$.",
          r"$\sqrt{n+1}-\sqrt n=\frac1{\sqrt{n+1}+\sqrt n}\sim\frac1{2\sqrt n}>0$ : $\sum\frac1{2\sqrt n}$ diverge, donc la première série diverge (télescopique : $S_N=\sqrt{N+1}-1\to+\infty$). La seconde : terme $\sim\frac1{4n}>0$ : elle diverge aussi.", duree=8),
    ]},
]

EXTRA_PARTS = [
    o("x1a", r"Nature de $\sum\frac{\sin n}{n^2}$.", r"Pour $n\ge1$, $\left|\frac{\sin n}{n^2}\right|\le\frac1{n^2}$ et $\sum\frac1{n^2}$ converge (Riemann, $\alpha=2$) : $\sum u_n$ converge absolument, donc converge.", src=f"{ASN}, ex. 1.1"),
    o("x1b", r"Nature de $\sum\frac{n^3}{3^n}$.", r"Règle de Cauchy : $\sqrt[n]{u_n}=\frac{n^{3/n}}3$ et $n^{3/n}=\exp\left(\frac{3\ln n}n\right)\to e^0=1$ car $\frac{\ln n}n\to0$. Donc $\sqrt[n]{u_n}\to\frac13<1$ : la série converge.", src=f"{ASN}, ex. 1.2"),
    o("x1c", r"Nature de $\sum\frac{(-1)^nn}{e^n}$.", r"On applique d'Alembert à $|u_n|=\frac n{e^n}>0$ : $\frac{|u_{n+1}|}{|u_n|}=\frac{n+1}n\times\frac1e\to\frac1e<1$. Donc $\sum|u_n|$ converge : $\sum u_n$ converge absolument, donc converge.", src=f"{ASN}, ex. 1.3"),
    o("x2a", r"Montrer que pour tout $\beta<\alpha$, $\frac{\ln n}{n^\alpha}=o\left(\frac1{n^\beta}\right)$.", r"$\frac{\ln n}{n^\alpha}\Big/\frac1{n^\beta}=\frac{\ln n}{n^{\alpha-\beta}}\to0$ par croissances comparées, car $\alpha-\beta>0$.", src=f"{ASN}, ex. 2.1"),
    o("x2b", r"En déduire que $\sum\frac{\ln n}{n^\alpha}$ converge si $\alpha>1$.", r"Si $\alpha>1$, on prend $\beta=\frac{1+\alpha}2\in]1,\alpha[$. Alors $\frac{\ln n}{n^\alpha}=o\left(\frac1{n^\beta}\right)$ et $\sum\frac1{n^\beta}$ converge ($\beta>1$) : la série converge.", src=f"{ASN}, ex. 2.2"),
    o("x2c", r"Montrer que $\sum\frac{\ln n}{n^\alpha}$ diverge si $\alpha\le1$.", r"Pour $n\ge3$, $\ln n\ge1$, donc $\frac{\ln n}{n^\alpha}\ge\frac1{n^\alpha}\ge\frac1n$ (car $n^\alpha\le n$ pour $\alpha\le1$). Or $\sum\frac1n$ diverge : par comparaison de séries positives, $\sum\frac{\ln n}{n^\alpha}$ diverge. (Corrigé rédigé.)", src=f"{ASN}, ex. 2.3"),
]


def _v(enonce, calc, ans, sol):
    return {"enonce": enonce, "calc": calc, "ans": ans, "sol": sol}


VARIANTS = {
    "c1": [_v(r"Limite de $\frac{n^3}{3^n}$ ?", "limit(n**3/3**n, n, oo)", "0", r"$3^n\gg n^3$ : $\frac{n^3}{3^n}\to0$.")],
    "c2": [_v(r"Limite de $\frac{(\ln n)^2}n$ ?", "limit(log(n)**2/n, n, oo)", "0", r"$\frac{(\ln n)^2}{n}\to0$ (croissances comparées).")],
    "c3": [_v(r"Limite de $\frac{5^n}{n!}$ ?", "limit(5**n/factorial(n), n, oo)", "0", r"$\frac{q^n}{n!}\to0$.")],
    "c4": [_v(r"Limite de $\frac{e^n}{n^3}$ ?", "limit(exp(n)/n**3, n, oo)", "oo", r"$\frac{e^n}{n^3}\to+\infty$.")],
    "c5": [_v(r"Limite de $\left(1+\frac2n\right)^n$ ?", "limit((1+2/n)**n, n, oo)", "exp(2)", r"$\left(1+\frac an\right)^n\to e^a$ avec $a=2$.")],
    "c6": [_v(r"Limite de $n\left(e^{1/n}-1\right)$ ?", "limit(n*(exp(1/n)-1), n, oo)", "1", r"$e^{1/n}-1\sim\frac1n$.")],
    "d1": [_v(r"Coefficient de $x^5$ dans le DL de $e^x$ en 0 ?", "coef(exp(x), 5)", "Rational(1,120)", r"$\frac1{5!}=\frac1{120}$.")],
    "d2": [_v(r"Coefficient de $x^3$ dans le DL de $\sin x$ en 0 ?", "coef(sin(x), 3)", "Rational(-1,6)", r"$-\frac1{3!}=-\frac16$.")],
    "d3": [_v(r"Coefficient de $x^4$ dans le DL de $\cos x$ en 0 ?", "coef(cos(x), 4)", "Rational(1,24)", r"$\frac1{4!}=\frac1{24}$.")],
    "d4": [_v(r"Coefficient de $x^3$ dans le DL de $\ln(1+x)$ en 0 ?", "coef(log(1+x), 3)", "Rational(1,3)", r"$\frac{(-1)^{3+1}}3=\frac13$.")],
    "d5": [_v(r"Coefficient de $x^3$ dans le DL de $\sqrt{1+x}$ en 0 ?", "coef(sqrt(1+x), 3)", "Rational(1,16)", r"$\frac{\alpha(\alpha-1)(\alpha-2)}6$ avec $\alpha=\frac12$ : $\frac{\frac12\cdot(-\frac12)\cdot(-\frac32)}6=\frac1{16}$.")],
    "d6": [_v(r"Coefficient de $x^5$ dans le DL de $\frac1{1+x}$ en 0 ?", "coef(1/(1+x), 5)", "-1", r"$\frac1{1+x}=\sum(-1)^kx^k$ : $(-1)^5=-1$.")],
    "e1": [_v(r"Limite en $0$ de $\frac{\sin4x}{2x}$ ?", "limit(sin(4*x)/(2*x), x, 0)", "2", r"$\sin4x\sim4x$ : $\frac{4x}{2x}=2$.")],
    "e2": [_v(r"Limite en $0$ de $\frac{e^{3x}-1}x$ ?", "limit((exp(3*x)-1)/x, x, 0)", "3", r"$e^{3x}-1\sim3x$.")],
    "e3": [_v(r"Limite en $0$ de $\frac{\ln(1+x^3)}{x^3}$ ?", "limit(log(1+x**3)/x**3, x, 0)", "1", r"$\ln(1+u)\sim u$ avec $u=x^3$.")],
    "e4": [_v(r"Limite en $0$ de $\frac{1-\cos2x}{x^2}$ ?", "limit((1-cos(2*x))/x**2, x, 0)", "2", r"$1-\cos2x\sim\frac{(2x)^2}2=2x^2$.")],
    "e5": [_v(r"Limite en $+\infty$ de $\frac{\sqrt{n^2+3n}}n$ ?", "limit(sqrt(n**2+3*n)/n, n, oo)", "1", r"$\sqrt{n^2+3n}\sim n$.")],
    "e6": [_v(r"Limite en $+\infty$ de $\frac{\ln(2n)}{\ln n}$ ?", "limit(log(2*n)/log(n), n, oo)", "1", r"$\ln(2n)=\ln2+\ln n\sim\ln n$.")],
    "p1": [_v(r"Coefficient de $x^3$ dans le DL de $\sin x\cos x$ en 0 ?", "coef(sin(x)*cos(x), 3)", "Rational(-2,3)", r"$\sin x\cos x=\frac{\sin2x}2=x-\frac{(2x)^3}{12}=x-\frac23x^3$.")],
    "p2": [_v(r"Coefficient de $x^2$ dans le DL de $e^x\sin x$ en 0 ?", "coef(exp(x)*sin(x), 2)", "1", r"$x\times x=x^2$ : coefficient $1$.")],
    "p3": [_v(r"Coefficient de $x^2$ dans le DL de $\ln(1+\tan x)$ en 0 ?", "coef(log(1+tan(x)), 2)", "Rational(-1,2)", r"$\tan x=x+o(x^2)$ : $\ln(1+u)=u-\frac{u^2}2$ donne $-\frac12$.")],
    "p4": [_v(r"Coefficient de $x^3$ dans le DL de $\frac1{1-x+x^2}$ en 0 ?", "coef(1/(1-x+x**2), 3)", "-1", r"$\frac1{1-x+x^2}=\frac{1+x}{1+x^3}=(1+x)(1-x^3+\dots)$ : $x^3$ : $-1$.")],
    "p5": [_v(r"Coefficient de $x^2$ dans le DL de $\frac{e^x}{1-x}$ en 0 ?", "coef(exp(x)/(1-x), 2)", "Rational(5,2)", r"$1+1+\frac12=\frac52$.")],
    "p6": [_v(r"Coefficient de $x^2$ dans le DL de $\sin^2x$ en 0 ?", "coef(sin(x)**2, 2)", "1", r"$\sin^2x=x^2+o(x^2)$.")],
    "l1": [_v(r"Limite en $0$ de $\frac{e^x-1-x-\frac{x^2}2}{x^3}$ ?", "limit((exp(x)-1-x-x**2/2)/x**3, x, 0)", "Rational(1,6)", r"Le terme suivant du DL est $\frac{x^3}6$.")],
    "l2": [_v(r"Limite en $0$ de $\frac{\sin x-x+\frac{x^3}6}{x^5}$ ?", "limit((sin(x)-x+x**3/6)/x**5, x, 0)", "Rational(1,120)", r"Le terme suivant est $\frac{x^5}{120}$.")],
    "l3": [_v(r"Limite en $0$ de $\frac{e^{2x}-1-2x}{x^2}$ ?", "limit((exp(2*x)-1-2*x)/x**2, x, 0)", "2", r"$e^{2x}=1+2x+\frac{4x^2}2+\dots$ : $2x^2$.")],
    "l4": [_v(r"Limite en $0$ de $\frac{x\cos x-\sin x}{x^3}$ ?", "limit((x*cos(x)-sin(x))/x**3, x, 0)", "Rational(-1,3)", r"$x\cos x-\sin x=\left(x-\frac{x^3}2\right)-\left(x-\frac{x^3}6\right)=-\frac{x^3}3$.")],
    "l5": [_v(r"Limite en $0$ de $\frac1x-\frac1{\ln(1+x)}$ ?", "limit(1/x-1/log(1+x), x, 0)", "Rational(-1,2)", r"$\frac1{\ln(1+x)}=\frac1x\left(1+\frac x2-\dots\right)=\frac1x+\frac12+o(1)$ : limite $-\frac12$.")],
    "l6": [_v(r"Limite en $0$ de $\frac{\ln(1+x)-x+\frac{x^2}2}{x^3}$ ?", "limit((log(1+x)-x+x**2/2)/x**3, x, 0)", "Rational(1,3)", r"Le terme suivant du DL est $\frac{x^3}3$.")],
    "s1": [_v(r"Calculer $\sum_{k=0}^{+\infty}\left(\frac13\right)^k$.", "summation(Rational(1,3)**k, (k, 0, oo))", "Rational(3,2)", r"$\frac1{1-\frac13}=\frac32$.")],
    "s2": [_v(r"Calculer $\sum_{k=2}^{+\infty}\frac1{k(k+1)}$.", "summation(1/(k*(k+1)), (k, 2, oo))", "Rational(1,2)", r"$S_N=\frac12-\frac1{N+1}\to\frac12$.")],
    "s3": [_v(r"Calculer $\sum_{k=1}^{+\infty}\left(\frac34\right)^k$.", "summation(Rational(3,4)**k, (k, 1, oo))", "3", r"$\frac{3/4}{1/4}=3$.")],
    "s4": [_v(r"Calculer $\sum_{k=1}^{+\infty}\frac1{k(k+3)}$.", "summation(1/(k*(k+3)), (k, 1, oo))", "Rational(11,18)", r"$\frac13\left(1+\frac12+\frac13\right)=\frac13\times\frac{11}6=\frac{11}{18}$.")],
    "s5": [_v(r"Calculer $\sum_{k=0}^{+\infty}\left(-\frac12\right)^k$.", "summation((-Rational(1,2))**k, (k, 0, oo))", "Rational(2,3)", r"$\frac1{1+\frac12}=\frac23$.")],
    "s6": [_v(r"Calculer $\sum_{k=1}^{+\infty}\frac1{4k^2-1}$.", "summation(1/(4*k**2-1), (k, 1, oo))", "Rational(1,2)", r"$\frac1{4k^2-1}=\frac12\left(\frac1{2k-1}-\frac1{2k+1}\right)$ : somme $\frac12$.")],
    "r5": [_v(r"$u_n=\frac{n^2+1}{n^4+n}\sim\frac1{n^p}$. Quelle est la valeur de $p$ ?", "limit(-log((n**2+1)/(n**4+n))/log(n), n, oo)", "2", r"$u_n\sim\frac{n^2}{n^4}=\frac1{n^2}$ : $p=2$.")],
    "r6": [_v(r"$u_n=\frac{\sqrt n}{n+1}\sim\frac1{n^p}$. Quelle est la valeur de $p$ ?", "limit(-log(sqrt(n)/(n+1))/log(n), n, oo)", "Rational(1,2)", r"$u_n\sim\frac{n^{1/2}}n=\frac1{n^{1/2}}$ : $p=\frac12\le1$, la série diverge.")],
    "a1": [_v(r"$u_n=\frac n{3^n}$. Calculer $\lim\frac{u_{n+1}}{u_n}$.", "limit(((n+1)/3**(n+1))/(n/3**n), n, oo)", "Rational(1,3)", r"$\frac{n+1}{3n}\to\frac13<1$ : converge.")],
    "a2": [_v(r"$u_n=\frac{5^n}{n!}$. Calculer $\lim\frac{u_{n+1}}{u_n}$.", "limit((5**(n+1)/factorial(n+1))/(5**n/factorial(n)), n, oo)", "0", r"$\frac5{n+1}\to0$ : converge.")],
    "a3": [_v(r"$u_n=\frac{n^3}{e^n}$. Calculer $\lim\frac{u_{n+1}}{u_n}$.", "limit(((n+1)**3/exp(n+1))/(n**3/exp(n)), n, oo)", "exp(-1)", r"$\left(\frac{n+1}n\right)^3e^{-1}\to\frac1e$ : converge.")],
    "a4": [_v(r"$u_n=\frac{(2n)!}{(n!)^2\,5^n}$. Calculer $\lim\frac{u_{n+1}}{u_n}$.", "limit(factorial(2*n+2)/(factorial(n+1)**2*5**(n+1))/(factorial(2*n)/(factorial(n)**2*5**n)), n, oo)", "Rational(4,5)", r"$\frac{(2n+1)(2n+2)}{(n+1)^2\times5}\to\frac45<1$ : converge.")],
    "a5": [_v(r"$u_n=\frac{3^n}{n^3}$. Calculer $\lim\frac{u_{n+1}}{u_n}$.", "limit((3**(n+1)/(n+1)**3)/(3**n/n**3), n, oo)", "3", r"$3\left(\frac n{n+1}\right)^3\to3>1$ : diverge.")],
    "h1": [_v(r"$u_n=\frac{n^2}{5^n}$. Calculer $\lim\sqrt[n]{u_n}$.", "limit(exp(log(n**2/5**n)/n), n, oo)", "Rational(1,5)", r"$\frac{n^{2/n}}5\to\frac15<1$ : converge.")],
    "h2": [_v(r"$u_n=\left(\frac{n}{3n+1}\right)^n$. Calculer $\lim\sqrt[n]{u_n}$.", "limit(n/(3*n+1), n, oo)", "Rational(1,3)", r"$\frac n{3n+1}\to\frac13<1$ : converge.")],
    "h3": [_v(r"$u_n=\left(1-\frac1n\right)^{n^2}$. Calculer $\lim\sqrt[n]{u_n}$.", "limit((1-1/n)**n, n, oo)", "exp(-1)", r"$\left(1-\frac1n\right)^n\to e^{-1}<1$ : converge.")],
    "h4": [_v(r"$u_n=\left(\frac{3n+2}{n+5}\right)^n$. Calculer $\lim\sqrt[n]{u_n}$.", "limit((3*n+2)/(n+5), n, oo)", "3", r"$\to3>1$ : diverge.")],
    "h5": [_v(r"$u_n=\left(\frac{\ln n}{\sqrt n}\right)^n$. Calculer $\lim\sqrt[n]{u_n}$.", "limit(log(n)/sqrt(n), n, oo)", "0", r"$\frac{\ln n}{\sqrt n}\to0<1$ : converge.")],
    "h6": [_v(r"$u_n=\frac{n^5}{4^n}$. Calculer $\lim\sqrt[n]{u_n}$.", "limit(exp(log(n**5/4**n)/n), n, oo)", "Rational(1,4)", r"$\frac{n^{5/n}}4\to\frac14<1$ : converge.")],
}

for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["id"] in VARIANTS:
            _e["variants"] = VARIANTS[_e["id"]]

QUIZ = [
    {"notion": "croiss", "type": "vf", "q": r"$\frac{n^{10}}{2^n}\to0$.", "bonne": True},
    {"notion": "croiss", "type": "qcm", "q": r"$\lim\left(1+\frac3n\right)^n=$ ?", "choix": [r"$e^3$", r"$3e$", r"$e$", r"$+\infty$"], "bonne": 0},
    {"notion": "dl-usuels", "type": "qcm", "q": r"Le coefficient de $x^3$ dans le DL de $\sin x$ en 0 est", "choix": [r"$-\frac16$", r"$\frac16$", r"$-\frac12$", r"$0$"], "bonne": 0},
    {"notion": "dl-usuels", "type": "vf", "q": r"$\cos x=1-\frac{x^2}2+\frac{x^4}{24}+o(x^4)$.", "bonne": True},
    {"notion": "equiv", "type": "vf", "q": r"$1-\cos x\sim x$ en 0.", "bonne": False},
    {"notion": "equiv", "type": "qcm", "q": r"En 0, $\ln(1+x)\sim$", "choix": [r"$x$", r"$1$", r"$x^2$", r"$\frac1x$"], "bonne": 0},
    {"notion": "dl-calc", "type": "vf", "q": r"Pour le DL d'un produit, on multiplie les DL et on tronque à l'ordre demandé.", "bonne": True},
    {"notion": "dl-calc", "type": "qcm", "q": r"Le DL de $e^x\cos x$ à l'ordre 2 est", "choix": [r"$1+x$", r"$1+x+x^2$", r"$1+x-\frac{x^2}2$", r"$1+\frac{x^2}2$"], "bonne": 0},
    {"notion": "dl-lim", "type": "qcm", "q": r"$\lim_{x\to0}\frac{x-\sin x}{x^3}=$", "choix": [r"$\frac16$", r"$0$", r"$\frac12$", r"$1$"], "bonne": 0},
    {"notion": "dl-lim", "type": "vf", "q": r"Si le terme de degré 2 s'annule dans un quotient par $x^2$, on peut conclure sans aller plus loin.", "bonne": False},
    {"notion": "geom-tele", "type": "qcm", "q": r"$\sum_{k=0}^{+\infty}\left(\frac13\right)^k=$", "choix": [r"$\frac32$", r"$3$", r"$\frac13$", r"$\frac23$"], "bonne": 0},
    {"notion": "geom-tele", "type": "vf", "q": r"$\sum_{k\ge1}\frac1{k(k+1)}=1$.", "bonne": True},
    {"notion": "div", "type": "vf", "q": r"Si $u_n\to0$ alors $\sum u_n$ converge.", "bonne": False},
    {"notion": "div", "type": "qcm", "q": r"$\sum\frac n{n+1}$ est", "choix": [r"grossièrement divergente", r"convergente", r"absolument convergente", r"de somme $1$"], "bonne": 0},
    {"notion": "riemann", "type": "vf", "q": r"$\sum\frac1{n^{3/2}}$ converge.", "bonne": True},
    {"notion": "riemann", "type": "qcm", "q": r"$\sum\frac1{n^\alpha}$ converge si et seulement si", "choix": [r"$\alpha>1$", r"$\alpha\ge1$", r"$\alpha<1$", r"$\alpha>0$"], "bonne": 0},
    {"notion": "comp", "type": "vf", "q": r"On peut utiliser un équivalent pour conclure sur la nature d'une série à termes de signe quelconque.", "bonne": False},
    {"notion": "comp", "type": "qcm", "q": r"$\frac{\ln n}{n^2}=o\left(\frac1{n^{3/2}}\right)$ donc la série $\sum\frac{\ln n}{n^2}$", "choix": [r"converge", r"diverge", r"est indéterminée", r"vaut $0$"], "bonne": 0},
    {"notion": "dalembert", "type": "vf", "q": r"Si $\frac{u_{n+1}}{u_n}\to1$, d'Alembert prouve la divergence.", "bonne": False},
    {"notion": "dalembert", "type": "qcm", "q": r"$u_n=\frac{3^n}{n!}$ : $\frac{u_{n+1}}{u_n}\to$", "choix": [r"$0$", r"$3$", r"$1$", r"$+\infty$"], "bonne": 0},
    {"notion": "cauchy", "type": "vf", "q": r"$\sqrt[n]{u_n}\to\frac13$ implique que $\sum u_n$ converge.", "bonne": True},
    {"notion": "cauchy", "type": "qcm", "q": r"$u_n=\left(\frac n{2n+1}\right)^n$ : $\sqrt[n]{u_n}\to$", "choix": [r"$\frac12$", r"$0$", r"$1$", r"$2$"], "bonne": 0},
    {"notion": "abs", "type": "vf", "q": r"Une série absolument convergente converge.", "bonne": True},
    {"notion": "abs", "type": "vf", "q": r"$\sum\frac{(-1)^n}{\sqrt n}$ converge absolument.", "bonne": False},
]

_LEVEL_FORMULES = {
    1: r"$\frac{(\ln n)^a}{n^b}\to0$ · $\frac{n^b}{q^n}\to0$ · $\frac{q^n}{n!}\to0$ · $\left(1+\frac an\right)^n\to e^a$",
    2: r"$e^x=\sum\frac{x^k}{k!}$ · $\sin x$ · $\cos x$ · $\ln(1+x)$ · $\frac1{1-x}=\sum x^k$ · $(1+x)^\alpha$",
    3: r"$\sin x\sim x$ · $e^x-1\sim x$ · $\ln(1+x)\sim x$ · $1-\cos x\sim\frac{x^2}2$",
    4: r"coefficient d'un produit $\sum_{i+j=k}a_ib_j$ · DL usuels · composée $f(u(x))$",
    5: r"DL usuels · Taylor-Young : coefficient de $x^k$ $=\frac{f^{(k)}(0)}{k!}$",
    6: r"$\sum_{k\ge0}q^k=\frac1{1-q}$ · décomposition en éléments simples · somme partielle $S_N$",
    7: r"$\sum u_n$ converge $\Rightarrow u_n\to0$ · $\ln\left(1+\frac1k\right)\le\frac1k$",
    8: r"$\sum\frac1{n^\alpha}$ converge $\iff\alpha>1$ · $u_n\sim\frac c{n^p}$",
    9: r"$0\le u_n\le v_n$ · $u_n\sim v_n$ · $u_n=o(v_n)$ · Riemann · équivalents usuels",
    10: r"d'Alembert : $\frac{u_{n+1}}{u_n}\to\ell$ · $\left(1+\frac1n\right)^n\to e$",
    11: r"Cauchy : $\sqrt[n]{u_n}\to\ell$ · $\sqrt[n]{u_n}=e^{\frac1n\ln u_n}$",
    12: r"$\sum|u_n|$ converge $\Rightarrow\sum u_n$ converge · critère des séries alternées",
    13: r"Riemann · Cauchy · d'Alembert · convergence absolue · croissances comparées",
    14: r"$\ln(1+u)=u-\frac{u^2}2+o(u^2)$ · comparaison · séries alternées · croissances comparées",
}
FORMULES = {e["id"]: _LEVEL_FORMULES[lvl["n"]] for lvl in LEVELS for e in lvl["exos"] if e["kind"] != "multi"}
FORMULES.update({
    "x1a": r"$\left|\frac{\sin n}{n^2}\right|\le\frac1{n^2}$ · Riemann $\alpha=2$ · convergence absolue",
    "x1b": r"Cauchy : $\sqrt[n]{u_n}\to\ell<1$ · $n^{3/n}=e^{3\ln n/n}\to1$",
    "x1c": r"d'Alembert sur $|u_n|$ · convergence absolue",
    "x2a": r"$\frac{\ln n}{n^{\alpha-\beta}}\to0$ (croissances comparées) · $u_n=o(v_n)$",
    "x2b": r"$u_n=o(v_n)$ et $\sum v_n$ converge · Riemann $\beta>1$",
    "x2c": r"$0\le v_n\le u_n$ et $\sum v_n$ diverge · Riemann $\alpha\le1$",
})
