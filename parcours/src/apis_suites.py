"""Level path: S1 maths, ECUE APIS, part 2: suites numériques.

Calibrated on Examen S1B2-SR janv. 2025 (promo 2029) and Examen B2-ASI janv. 2024 (promo 2028),
read on the PDF pages (pdftotext loses exponents: 3^n + 6, not 3n + 6).
`value` exercises carry `calc` (sympy, limits included) checked against `ans` by build.py;
`open` exercises (proofs, studies) carry a model answer.
"""

SUBJECT = {
    "id": "maths-s1-apis-suites",
    "ordre": 140,  # after APIS intégrales: suites are taught from S2-B2 (16 nov.)
    "matiere": "maths",
    "semestre": "S1",
    "ecue": "APIS",
    "titre": "Suites numériques",
    "chapitres_moodle": [
        "15_Cours 4 - Suites numériques - ECUE APIS", "16_Introduction aux suites numériques",
        "17_Limite d'une suite numérique", "18_Exemples remarquables", "19_Théorèmes de convergence",
        "20_Suites récurrentes", "21_Comparaisons de suites", "22_Démonstrations à connaître",
    ],
    "td": "TD4 suites (2026)",
    "examens": ["Test à distance 7 déc. 2026", "Examen B2 S1 (APIS)"],
}

NOTIONS = [
    {"id": "arith-geo", "titre": "Suites arithmétiques et géométriques",
     "formule": r"$u_n=u_0+nr$ · $v_n=v_0q^n$ · $\sum_{k=0}^{n}q^k=\frac{1-q^{n+1}}{1-q}$ ($q\ne1$) · $\sum_{k=1}^{n}k=\frac{n(n+1)}2$",
     "exemple": r"$1+3+\dots+3^9=\frac{3^{10}-1}{2}$",
     "cours": r"Arithmétique : $u_{n+1}-u_n=r$ constant. Géométrique : $\frac{v_{n+1}}{v_n}=q$ constant. Pour montrer qu'une suite est géométrique, on calcule $v_{n+1}$ et on l'écrit $q\,v_n$. Somme de termes consécutifs d'une suite géométrique : premier terme $\times\frac{1-q^{\text{nombre de termes}}}{1-q}$. Si $|q|<1$, $q^n\to0$ ; si $q>1$, $q^n\to+\infty$."},
    {"id": "variation", "titre": "Sens de variation",
     "formule": r"$u_{n+1}-u_n\ge0$ : croissante, $\le0$ : décroissante · si $u_n>0$ : $\frac{u_{n+1}}{u_n}\ge1$ : croissante, $\le1$ : décroissante · $u_n=f(n)$ : même sens de variation que $f$",
     "exemple": r"$u_n=\frac{n}{n+1}$ : $u_{n+1}-u_n=\frac1{(n+1)(n+2)}>0$",
     "cours": r"Méthode 1 : signe de $u_{n+1}-u_n$ (factoriser, réduire au même dénominateur). Méthode 2, pour une suite à termes strictement positifs : comparer $\frac{u_{n+1}}{u_n}$ à $1$ (pratique avec des puissances et des factorielles). Méthode 3 : si $u_n=f(n)$, étudier $f$ sur $[0,+\infty[$. Pour une somme $\sum_{k=n}^{2n-1}$, écrire les deux sommes et regarder quels termes restent."},
    {"id": "bornee", "titre": "Suite majorée, minorée, bornée",
     "formule": r"majorée : $\exists M,\ \forall n,\ u_n\le M$ · minorée : $\exists m,\ \forall n,\ u_n\ge m$ · bornée $\iff\exists M\ge0,\ \forall n,\ |u_n|\le M$",
     "exemple": r"$u_n=(-1)^n+\frac1{n+1}$ : $-1<u_n\le2$",
     "cours": r"Majorée : $\exists M,\ \forall n,\ u_n\le M$ ; minorée : $\exists m,\ \forall n,\ u_n\ge m$ ; bornée = les deux, ou de façon équivalente $|u_n|\le M$. Pour encadrer une somme de $p$ termes, on encadre chaque terme par le plus petit et le plus grand : $p\times\min\le\sum\le p\times\max$."},
    {"id": "limites", "titre": "Limites usuelles et croissances comparées",
     "formule": r"$\frac{P(n)}{Q(n)}$ : quotient des termes de plus haut degré · $q^n\to0$ si $|q|<1$, $\to+\infty$ si $q>1$, pas de limite si $q\le-1$ · $\frac{(\ln n)^a}{n^b}\to0$ ($b>0$) · $\frac{n^a}{q^n}\to0$ ($q>1$) · $\frac{q^n}{n!}\to0$",
     "exemple": r"$\frac{3n^2+1}{n^2+5}\to3$ ; $n^2e^{-n}\to0$",
     "cours": r"Factoriser par le terme dominant au numérateur et au dénominateur. Hiérarchie en $+\infty$ : $\ln n\ll n^a\ll q^n\ll n!$ ($a>0$, $q>1$). Somme de deux puissances : factoriser par la plus grande, $\frac{3^n+2^n}{3^n}=1+\left(\frac23\right)^n\to1$."},
    {"id": "fi", "titre": "Formes indéterminées",
     "formule": r"$\sqrt a-\sqrt b=\frac{a-b}{\sqrt a+\sqrt b}$ · $\frac{\sin x}{x}\xrightarrow[x\to0]{}1$ · $\left(1+\frac1n\right)^n\to e$",
     "exemple": r"$\sqrt{n^2+n}-n=\frac{n}{\sqrt{n^2+n}+n}\to\frac12$",
     "cours": r"$\infty-\infty$ avec racines : quantité conjuguée. $0\times\infty$ : se ramener à une limite connue ($n\sin\frac1n=\frac{\sin(1/n)}{1/n}$ avec $x=\frac1n\to0$). Puissance $1^\infty$ : écrire $\left(1+\frac1n\right)^n=e^{n\ln(1+1/n)}$ et utiliser $\frac{\ln(1+x)}{x}\to1$."},
    {"id": "gendarmes", "titre": "Gendarmes et comparaison",
     "formule": r"$v_n\le u_n\le w_n$, $v_n\to\ell$, $w_n\to\ell$ $\Rightarrow u_n\to\ell$ · $u_n\ge v_n\to+\infty\Rightarrow u_n\to+\infty$",
     "exemple": r"$\left|\frac{\sin n}n\right|\le\frac1n$ donc $\frac{\sin n}n\to0$",
     "cours": r"Encadrer à partir d'un certain rang, avec deux suites de **même** limite. Bornes utiles : $-1\le\sin,\cos,(-1)^n\le1$ ; pour une somme de $n$ termes, minorer et majorer chaque terme. Une seule minoration par une suite qui tend vers $+\infty$ suffit pour $+\infty$."},
    {"id": "arith-geo-rec", "titre": "Suites arithmético-géométriques",
     "formule": r"$u_{n+1}=au_n+b$, $a\ne1$ : $\ell=\frac{b}{1-a}$, $v_n=u_n-\ell$ géométrique de raison $a$",
     "exemple": r"$u_{n+1}=2u_n-3$, $u_0=5$ : $\ell=3$, $u_n=3+2^{n+1}$",
     "cours": r"On cherche le point fixe $\ell=a\ell+b$. Alors $u_{n+1}-\ell=a(u_n-\ell)$ : $v_n=u_n-\ell$ est géométrique, $v_n=a^nv_0$, donc $u_n=\ell+a^n(u_0-\ell)$. Si $|a|<1$, $u_n\to\ell$. Un énoncé peut aussi donner directement la suite auxiliaire $v_n$ (parfois avec $\frac1{u_n}$) : il suffit de calculer $v_{n+1}$."},
    {"id": "monotone", "titre": "Théorème de la limite monotone",
     "formule": r"croissante et majorée $\Rightarrow$ converge · croissante non majorée $\Rightarrow+\infty$ · décroissante et minorée $\Rightarrow$ converge · décroissante non minorée $\Rightarrow-\infty$",
     "exemple": r"$u_n=\sum_{k=1}^n\frac1{k^2}$ croissante, majorée par $2$ : converge",
     "cours": r"Énoncé symétrique : décroissante et minorée $\Rightarrow$ converge. Le théorème donne l'existence de la limite, pas sa valeur : on l'encadre avec les bornes ($m\le\ell\le M$, et $\ell\le u_n$ pour tout $n$ si la suite décroît). Majorations classiques : $\frac1{k^2}\le\frac1{k-1}-\frac1k$, $\frac1{k!}\le\frac1{2^{k-1}}$."},
    {"id": "adjacentes", "titre": "Suites adjacentes",
     "formule": r"$(u_n)\nearrow$, $(v_n)\searrow$, $v_n-u_n\to0$ $\Rightarrow$ même limite $\ell$, et $u_n\le\ell\le v_n$",
     "exemple": r"$u_n=\sum_{k=0}^n\frac1{k!}$, $v_n=u_n+\frac1{n!}$",
     "cours": r"Rédaction attendue : rappeler la définition, puis trois points : monotonie de $(u_n)$ (signe de $u_{n+1}-u_n$), monotonie de $(v_n)$, limite de $v_n-u_n$. Souvent on étudie d'abord $w_n=v_n-u_n$ (géométrique, de signe connu). Conclusion : convergence vers une limite commune, encadrée par $u_n$ et $v_n$."},
    {"id": "recurrentes", "titre": r"Suites récurrentes $u_{n+1}=f(u_n)$",
     "formule": r"si $u_n\to\ell$ et $f$ continue en $\ell$ : $\ell=f(\ell)$",
     "exemple": r"$u_{n+1}=1+\frac{u_n^2}4$ : $u_{n+1}-u_n=\frac{(u_n-2)^2}4\ge0$",
     "cours": r"Plan type : 1) encadrement $a<u_n<b$ par récurrence ; 2) monotonie (signe de $u_{n+1}-u_n=f(u_n)-u_n$, à factoriser) ; 3) limite monotone : la suite converge ; 4) la limite vérifie $\ell=f(\ell)$, on garde la solution compatible avec l'encadrement. Les limites **possibles** se cherchent avant de savoir si la suite converge."},
    {"id": "extraites", "titre": "Suites extraites",
     "formule": r"$u_n\to\ell\Rightarrow u_{\varphi(n)}\to\ell$ · $u_{2n}\to\ell$ et $u_{2n+1}\to\ell\Rightarrow u_n\to\ell$",
     "exemple": r"$\sin\frac{n\pi}3$ : $u_{3n}=0$, $u_{6n+1}=\frac{\sqrt3}2$ : diverge",
     "cours": r"Pour montrer qu'une suite **diverge** : deux suites extraites de limites différentes (contraposée du premier résultat). Pour montrer qu'elle **converge** : les termes pairs et impairs tendent vers la même limite. Calculer $u_{2n}$, $u_{2n+1}$ en remplaçant $n$."},
    {"id": "landau", "titre": r"Comparaison : $o$, $O$, $\sim$",
     "formule": r"$u_n=o(v_n)$ : $\frac{u_n}{v_n}\to0$ · $u_n=O(v_n)$ : $\frac{u_n}{v_n}$ bornée · $u_n\sim v_n$ : $\frac{u_n}{v_n}\to1$",
     "exemple": r"$1-2n^2\sim-2n^2+n-3$ ; $4^n+1=o(5^n)$",
     "cours": r"(Suites ne s'annulant pas à partir d'un certain rang.) Méthode : calculer la limite de $\frac{u_n}{v_n}$. Limite $1$ : $u\sim v$, $u=O(v)$ et $v=O(u)$. Limite $c\ne0,1$ : $O$ dans les deux sens, pas $\sim$. Limite $0$ : $u=o(v)$ donc $u=O(v)$ ; $v$ n'est pas $O(u)$. Limite infinie : inverser les rôles. Citer **toutes** les relations vraies."},
    {"id": "demos", "titre": "Démonstrations à connaître",
     "formule": r"$u_n\to\ell\iff\forall\varepsilon>0,\ \exists N,\ \forall n\ge N,\ |u_n-\ell|\le\varepsilon$",
     "exemple": r"convergente $\Rightarrow$ bornée ; réciproque fausse : $(-1)^n$",
     "cours": r"À savoir rédiger : unicité de la limite ($\varepsilon=\frac{|\ell-\ell'|}3$) ; convergente $\Rightarrow$ bornée ($\varepsilon=1$, puis $M=\max(|u_0|,\dots,|u_{N-1}|,|\ell|+1)$) ; théorème des gendarmes (à partir d'un rang, $\ell-\varepsilon\le v_n\le u_n\le w_n\le\ell+\varepsilon$)."},
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


SR = "Examen S1B2-SR janv. 2025"
ASI = "Examen B2-ASI janv. 2024"

LEVELS = [
    {"n": 1, "titre": "Suites arithmétiques et géométriques", "notions": ["arith-geo"], "exos": [
        v("ag1", r"$(u_n)$ est arithmétique, $u_0=3$, raison $4$. Calculer $u_{20}$.", "3+20*4", "83",
          r"$u_{20}=u_0+20r=3+80=83$.", duree=2),
        v("ag2", r"$(v_n)$ est géométrique, $v_0=5$, raison $2$. Calculer $v_6$.", "5*2**6", "320",
          r"$v_6=v_0q^6=5\times64=320$.", duree=2),
        v("ag3", r"Calculer $1+2+\dots+100$.", "summation(k,(k,1,100))", "5050",
          r"$\frac{100\times101}2=5050$.", duree=2),
        v("ag4", r"Calculer $\sum_{k=0}^{9}3^k$.", "summation(3**k,(k,0,9))", "(3**10-1)/2",
          r"Géométrique de raison $3$, 10 termes : $\frac{3^{10}-1}{3-1}=29524$.", duree=3),
        v("ag5", r"$(u_n)$ est arithmétique avec $u_3=10$ et $u_7=22$. Calculer $u_{50}$.", "10+(50-3)*3", "151",
          r"$u_7-u_3=4r=12$ donc $r=3$ ; $u_{50}=u_3+47r=10+141=151$.", duree=3),
    ]},
    {"n": 2, "titre": "Sens de variation", "notions": ["variation"], "exos": [
        o("va1", r"Étudier le sens de variation de $u_n=\frac{n}{n+1}$, $n\in\mathbb N$.",
          r"$u_{n+1}-u_n=\frac{n+1}{n+2}-\frac n{n+1}=\frac{(n+1)^2-n(n+2)}{(n+1)(n+2)}=\frac1{(n+1)(n+2)}>0$ : $(u_n)$ est strictement croissante.", duree=3),
        o("va2", r"Étudier le sens de variation de $u_n=\frac{2^n}{n!}$, $n\ge1$.",
          r"$u_n>0$ et $\frac{u_{n+1}}{u_n}=\frac{2^{n+1}}{(n+1)!}\cdot\frac{n!}{2^n}=\frac2{n+1}\le1$ pour $n\ge1$ : $(u_n)$ est décroissante (strictement à partir de $n=2$ ; $u_1=u_2=2$).", duree=3),
        o("va3", r"Étudier le sens de variation de $u_n=\sum_{k=1}^{n}\frac1{k^2}$, $n\ge1$.",
          r"$u_{n+1}-u_n=\frac1{(n+1)^2}>0$ : $(u_n)$ est strictement croissante.", duree=2),
        o("va4", r"Étudier le sens de variation de $u_n=n^2-4n$.",
          r"$u_{n+1}-u_n=(n+1)^2-4(n+1)-n^2+4n=2n-3$. Négatif pour $n\le1$, positif pour $n\ge2$ : $u_0=0>u_1=-3>u_2=-4$, puis $(u_n)$ est croissante à partir du rang $2$.", duree=3),
        o("va5", r"Soit $u_n=\sum_{k=n}^{2n-1}\frac1k$ pour $n\ge1$. Étudier la monotonie de $(u_n)$.",
          r"$u_{n+1}=\sum_{k=n+1}^{2n+1}\frac1k$. Les termes $k=n+1,\dots,2n-1$ sont communs, donc $u_{n+1}-u_n=\frac1{2n}+\frac1{2n+1}-\frac1n=\frac1{2n+1}-\frac1{2n}=\frac{-1}{2n(2n+1)}<0$ : $(u_n)$ est strictement décroissante.",
          src=f"{SR}, ex. 2.1"),
    ]},
    {"n": 3, "titre": "Suites bornées, encadrements", "notions": ["bornee"], "exos": [
        o("bo1", r"Montrer que $u_n=(-1)^n+\frac1{n+1}$ est bornée.",
          r"$-1\le(-1)^n\le1$ et $0<\frac1{n+1}\le1$, donc $-1<u_n\le2$ et $|u_n|\le2$ : $(u_n)$ est bornée.", duree=2),
        o("bo2", r"Montrer que $u_n=\frac{2n+1}{n+3}$ est bornée en donnant un minorant et un majorant.",
          r"$u_n=\frac{2(n+3)-5}{n+3}=2-\frac5{n+3}$. Comme $0<\frac5{n+3}\le\frac53$ : $\frac13\le u_n<2$.", duree=3),
        o("bo3", r"Rappeler la définition de « $(u_n)$ est bornée » et montrer qu'elle équivaut à $\exists M\ge0,\ \forall n,\ |u_n|\le M$.",
          r"Bornée : $\exists m,M',\ \forall n,\ m\le u_n\le M'$. Si c'est le cas, $M=\max(|m|,|M'|)$ convient : $-M\le m\le u_n\le M'\le M$. Réciproquement $|u_n|\le M$ donne $-M\le u_n\le M$.",
          src=f"{SR}, ex. 4.1"),
        o("bo4", r"Soit $u_n=\sum_{k=n}^{2n-1}\frac1k$ ($n\ge1$). En encadrant chaque terme, montrer $\frac{n}{2n-1}\le u_n\le1$, puis donner un minorant et un majorant explicites.",
          r"La somme a $n$ termes et pour $n\le k\le2n-1$ : $\frac1{2n-1}\le\frac1k\le\frac1n$. Donc $\frac n{2n-1}\le u_n\le n\cdot\frac1n=1$. Comme $\frac n{2n-1}\ge\frac12$ ($2n\ge2n-1$), on a $\frac12\le u_n\le1$ : $(u_n)$ est bornée.",
          src=f"{SR}, ex. 2.2-2.3"),
        o("bo5", r"Montrer que $u_n=\frac{\cos n+2\sin(3n)}{n+1}$ est bornée.",
          r"$|\cos n+2\sin 3n|\le1+2=3$ et $n+1\ge1$, donc $|u_n|\le3$.", duree=2),
    ]},
    {"n": 4, "titre": "Limites usuelles", "notions": ["limites"], "exos": [
        v("li1", r"Limite de $\frac{3n^2+1}{n^2+5}$ ?", "limit((3*n**2+1)/(n**2+5), n, oo)", "3",
          r"$\frac{n^2(3+1/n^2)}{n^2(1+5/n^2)}\to3$.", duree=2),
        v("li2", r"Limite de $\frac{2n+1}{n^2+1}$ ?", "limit((2*n+1)/(n**2+1), n, oo)", "0",
          r"$\frac{n(2+1/n)}{n^2(1+1/n^2)}=\frac1n\cdot\frac{2+1/n}{1+1/n^2}\to0$.", duree=2),
        v("li3", r"Limite de $\frac{n^3-2n}{5n^2+1}$ ?", "limit((n**3-2*n)/(5*n**2+1), n, oo)", "oo",
          r"$\frac{n^3(1-2/n^2)}{n^2(5+1/n^2)}=n\cdot\frac{1-2/n^2}{5+1/n^2}\to+\infty$.", duree=2),
        v("li4", r"Limite de $n^2e^{-n}$ ?", "limit(n**2*exp(-n), n, oo)", "0",
          r"Croissances comparées : $\frac{n^2}{e^n}\to0$.", duree=2),
        v("li5", r"Limite de $\frac{3^n+2^n}{3^n}$ ?", "limit((3**n+2**n)/3**n, n, oo)", "1",
          r"$1+\left(\frac23\right)^n\to1$ car $\left|\frac23\right|<1$.", duree=2),
        v("li6", r"Limite de $n^5\left(\frac23\right)^n$ ?", "limit(n**5*Rational(2,3)**n, n, oo)", "0",
          r"$n^5\left(\frac23\right)^n=\frac{n^5}{(3/2)^n}$ et $\frac{n^a}{q^n}\to0$ pour $q=\frac32>1$.", duree=2),
        v("li7", r"Limite de $\frac{(\ln n)^3}{\sqrt n}$ ?", "limit(log(n)**3/sqrt(n), n, oo)", "0",
          r"$\frac{(\ln n)^a}{n^b}\to0$ avec $a=3$, $b=\frac12$ : le logarithme perd contre toute puissance.", duree=2),
        v("li8", r"Limite de $\frac{5^n}{n!}$ ?", "limit(5**n/factorial(n), n, oo)", "0",
          r"$\frac{q^n}{n!}\to0$ pour tout $q$ : la factorielle gagne contre l'exponentielle.", duree=2),
    ]},
    {"n": 5, "titre": "Formes indéterminées", "notions": ["fi", "limites"], "exos": [
        v("fi1", r"Limite de $\sqrt{n+1}-\sqrt n$ ?", "limit(sqrt(n+1)-sqrt(n), n, oo)", "0",
          r"Quantité conjuguée : $\frac{1}{\sqrt{n+1}+\sqrt n}\to0$.", duree=3),
        v("fi2", r"Limite de $\sqrt{n^2+n}-n$ ?", "limit(sqrt(n**2+n)-n, n, oo)", "Rational(1,2)",
          r"$\frac{n}{\sqrt{n^2+n}+n}=\frac{1}{\sqrt{1+1/n}+1}\to\frac12$.", duree=3),
        v("fi3", r"Limite de $\left(1+\frac1n\right)^n$ ?", "limit((1+1/n)**n, n, oo)", "E",
          r"$e^{n\ln(1+1/n)}$ et $n\ln\left(1+\frac1n\right)=\frac{\ln(1+x)}x$ avec $x=\frac1n\to0$, donc $\to1$ : la limite est $e$."),
        v("fi4", r"Limite de $n\sin\frac1n$ ?", "limit(n*sin(1/n), n, oo)", "1",
          r"$\frac{\sin x}{x}$ avec $x=\frac1n\to0$ : limite $1$.", duree=3),
        v("fi5", r"Limite de $\frac{2^n-3^n}{2^n+3^n}$ ?", "limit((2**n-3**n)/(2**n+3**n), n, oo)", "-1",
          r"Diviser par $3^n$ : $\frac{(2/3)^n-1}{(2/3)^n+1}\to\frac{-1}{1}=-1$.", duree=3),
    ]},
    {"n": 6, "titre": "Gendarmes et comparaison", "notions": ["gendarmes"], "exos": [
        o("ge1", r"Montrer que $\frac{\sin n}{n}\to0$.",
          r"$-\frac1n\le\frac{\sin n}n\le\frac1n$ et $\pm\frac1n\to0$ : par le théorème des gendarmes, la limite est $0$.", duree=2),
        v("ge2", r"Limite de $\frac{n+\cos n}{n}$ ? (justifier par encadrement)", "limit((n+cos(n))/n, n, oo)", "1",
          r"$1-\frac1n\le\frac{n+\cos n}n\le1+\frac1n$, les deux bornes tendent vers $1$ : limite $1$.", duree=3),
        o("ge3", r"Soit $u_n=\sum_{k=1}^{n}\frac{n}{n^2+k}$. Encadrer $u_n$ et en déduire sa limite.",
          r"Pour $1\le k\le n$ : $\frac n{n^2+n}\le\frac n{n^2+k}\le\frac n{n^2+1}$. Avec $n$ termes : $\frac{n^2}{n^2+n}\le u_n\le\frac{n^2}{n^2+1}$. Les deux bornes tendent vers $1$ : $u_n\to1$."),
        o("ge4", r"Montrer que $u_n=n+(-1)^n\sqrt n$ tend vers $+\infty$.",
          r"$u_n\ge n-\sqrt n=\sqrt n(\sqrt n-1)$ et $\sqrt n(\sqrt n-1)\to+\infty$ : par comparaison, $u_n\to+\infty$.", duree=3),
        o("ge5", r"Soit $u_n=\frac{\lfloor n\sqrt2\rfloor}{n}$. Montrer que $u_n\to\sqrt2$.",
          r"$n\sqrt2-1<\lfloor n\sqrt2\rfloor\le n\sqrt2$, donc $\sqrt2-\frac1n<u_n\le\sqrt2$. Gendarmes : $u_n\to\sqrt2$.", duree=3),
    ]},
    {"n": 7, "titre": "Suites arithmético-géométriques", "notions": ["arith-geo-rec", "arith-geo"], "exos": [
        v("rg1", r"$u_0=5$, $u_{n+1}=2u_n-3$. Trouver $u_n$ en fonction de $n$ puis calculer $u_5$.", "3+2*2**5", "67",
          r"Point fixe $\ell=2\ell-3$, $\ell=3$. $v_n=u_n-3$ vérifie $v_{n+1}=2v_n$, $v_0=2$, donc $u_n=3+2^{n+1}$ et $u_5=67$."),
        v("rg2", r"$u_0=0$, $u_{n+1}=\frac{u_n}2+1$. Limite de $(u_n)$ ?", "limit(2-2*Rational(1,2)**n, n, oo)", "2",
          r"$\ell=\frac\ell2+1$ donne $\ell=2$ ; $u_n-2=\left(\frac12\right)^n(u_0-2)=-2\left(\frac12\right)^n\to0$, donc $u_n\to2$."),
        v("rg3", r"$u_0=0$, $u_{n+1}=3u_n+2$. Exprimer $u_n$ puis calculer $u_4$.", "3**4-1", "80",
          r"$\ell=3\ell+2$, $\ell=-1$ ; $u_n+1=3^n(u_0+1)$, donc $u_n=3^n-1$ et $u_4=80$."),
        o("rg4", r"$u_0=1$, $u_{n+1}=\frac{u_n}{u_n+8}$ (on admet $u_n>0$). Soit $v_n=1+\frac7{u_n}$. Montrer que $(v_n)$ est géométrique de raison $8$, puis exprimer $v_n$ et $u_n$ en fonction de $n$.",
          r"$\frac1{u_{n+1}}=\frac{u_n+8}{u_n}=1+\frac8{u_n}$, donc $v_{n+1}=1+7+\frac{56}{u_n}=8\left(1+\frac7{u_n}\right)=8v_n$. $v_0=8$, donc $v_n=8^{n+1}$ et $u_n=\frac{7}{v_n-1}=\frac{7}{8^{n+1}-1}$ (on vérifie $u_0=1$, $u_1=\frac19$). Donc $u_n\to0$.",
          src=f"{ASI}, ex. 5.2"),
        o("rg5", r"$u_0=2$, $v_0=3$, $u_{n+1}=\frac{3u_n+2v_n}5$, $v_{n+1}=\frac{2u_n+3v_n}5$. Soit $x_n=u_n+v_n$. Exprimer $x_{n+1}$ en fonction de $x_n$, puis $x_n$ en fonction de $n$.",
          r"$x_{n+1}=\frac{5u_n+5v_n}5=x_n$ : $(x_n)$ est constante, $x_n=x_0=5$.",
          src=f"{SR}, ex. 1.4a", duree=3),
    ]},
    {"n": 8, "titre": "Théorème de la limite monotone", "notions": ["monotone", "variation", "bornee"], "exos": [
        o("lm1", r"Soit $u_n=\sum_{k=1}^{n}\frac1{k^2}$. En utilisant $\frac1{k^2}\le\frac1{k-1}-\frac1k$ pour $k\ge2$, montrer que $(u_n)$ converge.",
          r"$(u_n)$ est croissante ($u_{n+1}-u_n=\frac1{(n+1)^2}>0$). Pour $n\ge2$, par télescopage $u_n\le1+\sum_{k=2}^n\left(\frac1{k-1}-\frac1k\right)=2-\frac1n<2$. Croissante et majorée : $(u_n)$ converge (vers une limite $\le2$)."),
        o("lm2", r"Soit $u_n=\sum_{k=0}^{n}\frac1{k!}$. Montrer que $(u_n)$ converge (utiliser $k!\ge2^{k-1}$ pour $k\ge1$).",
          r"Croissante : $u_{n+1}-u_n=\frac1{(n+1)!}>0$. Majorée : $u_n\le1+\sum_{k=1}^n\frac1{2^{k-1}}=1+\frac{1-(1/2)^n}{1/2}<3$. Croissante et majorée : converge."),
        o("lm3", r"Soit $u_n=\sum_{k=n}^{2n-1}\frac1k$. On sait que $(u_n)$ est décroissante et que $\frac12\le u_n\le1$. Converge-t-elle ? Encadrer sa limite $\ell$.",
          r"Décroissante et minorée par $\frac12$ : $(u_n)$ converge. En passant à la limite dans $\frac n{2n-1}\le u_n\le1$ : $\frac12\le\ell\le1$. Plus précis : la suite décroît, donc $\ell\le u_n$ pour tout $n$, par exemple $\ell\le u_2=\frac12+\frac13=\frac56$.",
          src=f"{SR}, ex. 2.4", duree=3),
        o("lm4", r"Énoncer le théorème de la limite monotone pour une suite croissante (les deux cas).",
          r"Une suite croissante et majorée converge (vers la borne supérieure de ses termes). Une suite croissante non majorée tend vers $+\infty$.", duree=2),
    ]},
    {"n": 9, "titre": "Suites adjacentes", "notions": ["adjacentes", "arith-geo"], "exos": [
        o("ad1", r"Rappeler la définition de deux suites adjacentes et montrer que $u_n=1-\frac1n$ et $v_n=1+\frac1{n^2}$ ($n\ge1$) sont adjacentes.",
          r"$(u_n)$ croissante, $(v_n)$ décroissante, $v_n-u_n\to0$. Ici $u_{n+1}-u_n=\frac1n-\frac1{n+1}>0$, $v_{n+1}-v_n=\frac1{(n+1)^2}-\frac1{n^2}<0$ et $v_n-u_n=\frac1n+\frac1{n^2}\to0$.", duree=3),
        o("ad2", r"Soit $u_n=\sum_{k=0}^{n}\frac1{k!}$ et $v_n=u_n+\frac1{n!}$ pour $n\ge2$. Après avoir rappelé la définition, montrer que $(u_n)$ et $(v_n)$ sont adjacentes. $(u_n)$ converge-t-elle ? Est-elle majorée ?",
          r"$u_{n+1}-u_n=\frac1{(n+1)!}>0$. $v_{n+1}-v_n=\frac2{(n+1)!}-\frac1{n!}=\frac{2-(n+1)}{(n+1)!}=\frac{1-n}{(n+1)!}<0$ pour $n\ge2$. $v_n-u_n=\frac1{n!}\to0$. Adjacentes, donc elles convergent vers la même limite $\ell$. $(u_n)$ est majorée par $v_2=\frac52+\frac12=3$ (car $u_n\le\ell\le v_n\le v_2$).",
          src=f"{ASI}, ex. 2"),
        o("ad3", r"$u_0=2$, $v_0=3$, $u_{n+1}=\frac{3u_n+2v_n}5$, $v_{n+1}=\frac{2u_n+3v_n}5$, $w_n=v_n-u_n$. Montrer que $(w_n)$ est géométrique, exprimer $w_n$ et donner son signe.",
          r"$w_{n+1}=\frac{2u_n+3v_n-3u_n-2v_n}5=\frac{v_n-u_n}5=\frac15w_n$ : géométrique de raison $\frac15$, $w_0=1$, $w_n=\left(\frac15\right)^n>0$.",
          src=f"{SR}, ex. 1.1"),
        o("ad4", r"Mêmes suites. Montrer que $(u_n)$ et $(v_n)$ sont adjacentes et donner leur limite (on sait $u_n+v_n=5$).",
          r"$u_{n+1}-u_n=\frac{2(v_n-u_n)}5=\frac25w_n>0$ : croissante. $v_{n+1}-v_n=-\frac25w_n<0$ : décroissante. $v_n-u_n=\left(\frac15\right)^n\to0$. Adjacentes : même limite $\ell$, et $2\ell=\lim(u_n+v_n)=5$, donc $\ell=\frac52$.",
          src=f"{SR}, ex. 1.2-1.4"),
        o("ad5", r"Montrer que $u_n=\sum_{k=1}^{n}\frac1{k^2}$ et $v_n=u_n+\frac1n$ sont adjacentes.",
          r"$u$ croissante. $v_{n+1}-v_n=\frac1{(n+1)^2}+\frac1{n+1}-\frac1n=\frac1{(n+1)^2}-\frac1{n(n+1)}=\frac{-1}{n(n+1)^2}<0$. $v_n-u_n=\frac1n\to0$."),
    ]},
    {"n": 10, "titre": "Suites récurrentes", "notions": ["recurrentes", "monotone"], "exos": [
        o("re1", r"$u_0=0$, $u_{n+1}=\sqrt{2+u_n}$. Montrer que $0\le u_n\le2$, que $(u_n)$ est croissante, puis trouver sa limite.",
          r"Récurrence : $u_0=0\in[0,2]$ ; si $0\le u_n\le2$ alors $\sqrt2\le u_{n+1}\le2$. Monotonie : $u_{n+1}^2-u_n^2=2+u_n-u_n^2=(2-u_n)(1+u_n)\ge0$ et les termes sont positifs, donc $u_{n+1}\ge u_n$. Croissante majorée : converge vers $\ell\in[0,2]$ avec $\ell=\sqrt{2+\ell}$, soit $\ell^2-\ell-2=0$, $\ell=2$ ($\ell=-1$ exclu)."),
        o("re2", r"$u_0=1$, $u_{n+1}=\frac{u_n}{u_n+8}$. (a) Montrer par récurrence que $u_n>0$. (b) Si $(u_n)$ converge vers $\ell$, quelles valeurs possibles ? (c) Monotonie. (d) Convergence et limite.",
          r"(a) $u_0=1>0$ ; si $u_n>0$, numérateur et dénominateur sont $>0$. (b) $\ell=\frac\ell{\ell+8}$ donne $\ell^2+7\ell=0$ : $\ell\in\{0,-7\}$ ; comme $u_n>0$, $\ell\ge0$ donc $\ell=0$. (c) $\frac{u_{n+1}}{u_n}=\frac1{u_n+8}<1$ : strictement décroissante. (d) Décroissante, minorée par $0$ : converge, et la seule limite possible est $0$.",
          src=f"{ASI}, ex. 5.1"),
        o("re3", r"$u_0=\frac32$, $u_{n+1}=1+\frac{u_n^2}4$. (1) Monotonie (factoriser). (2) Montrer par récurrence $1<u_n<2$. (3) Comportement en $+\infty$.",
          r"(1) $u_{n+1}-u_n=\frac{u_n^2}4-u_n+1=\left(\frac{u_n}2-1\right)^2=\frac{(u_n-2)^2}4\ge0$ : croissante. (2) $1<\frac32<2$ ; si $1<u_n<2$ alors $\frac14<\frac{u_n^2}4<1$, donc $\frac54<u_{n+1}<2$. (3) Croissante, majorée par $2$ : converge vers $\ell\in[1,2]$ et $\ell=1+\frac{\ell^2}4$, $(\ell-2)^2=0$, $\ell=2$.",
          src=f"{SR}, ex. 5"),
        o("re4", r"$u_0=\frac12$, $u_{n+1}=u_n-u_n^2$. Montrer que $0<u_n\le\frac12$, que $(u_n)$ décroît et trouver sa limite.",
          r"Si $0<u_n\le\frac12$ : $u_{n+1}=u_n(1-u_n)$ avec $1-u_n\in[\frac12,1[$, donc $0<u_{n+1}<u_n\le\frac12$. Cela donne aussi la décroissance ($u_{n+1}-u_n=-u_n^2<0$). Minorée par $0$ : converge, $\ell=\ell-\ell^2$, $\ell=0$."),
        o("re5", r"$u_{n+1}=\frac{u_n^2+6}5$. Quelles sont les limites possibles de $(u_n)$ ?",
          r"$\ell=\frac{\ell^2+6}5\iff\ell^2-5\ell+6=0\iff\ell\in\{2,3\}$. Ce sont les seules limites finies possibles ; la suite peut aussi diverger selon $u_0$.", duree=3),
    ]},
    {"n": 11, "titre": "Suites extraites", "notions": ["extraites"], "exos": [
        o("ex1", r"$u_n=\sin\frac{n\pi}3$. Que vaut $(u_{3n})$ ? Vers quoi converge $(u_{6n+1})$ ? $(u_n)$ converge-t-elle ?",
          r"$u_{3n}=\sin(n\pi)=0$. $u_{6n+1}=\sin\left(2n\pi+\frac\pi3\right)=\frac{\sqrt3}2$. Deux suites extraites ont des limites différentes ($0\ne\frac{\sqrt3}2$) ; or si $(u_n)$ convergeait vers $\ell$, toute suite extraite tendrait vers $\ell$. Donc $(u_n)$ diverge.",
          src=f"{SR}, ex. 6"),
        o("ex2", r"$u_n=\frac1n\sum_{k=0}^{n-1}(-1)^k$ ($n\ge1$). Exprimer $u_{2n}$ et $u_{2n+1}$ ; $(u_n)$ converge-t-elle ?",
          r"Les termes s'annulent deux par deux : $\sum_{k=0}^{2n-1}(-1)^k=0$ et $\sum_{k=0}^{2n}(-1)^k=1$. Donc $u_{2n}=0$ et $u_{2n+1}=\frac1{2n+1}$. Les deux tendent vers $0$ : $(u_n)$ converge vers $0$.",
          src=f"{ASI}, ex. 6"),
        o("ex3", r"$u_n=(-1)^n\frac{n}{n+1}$ converge-t-elle ?",
          r"$u_{2n}=\frac{2n}{2n+1}\to1$ et $u_{2n+1}=-\frac{2n+1}{2n+2}\to-1$ : deux limites différentes, $(u_n)$ diverge.", duree=3),
        o("ex4", r"$u_n=\cos\frac{n\pi}2$ converge-t-elle ?",
          r"$u_{4n}=\cos(2n\pi)=1$ et $u_{4n+2}=\cos(2n\pi+\pi)=-1$ : $(u_n)$ diverge.", duree=2),
    ]},
    {"n": 12, "titre": "Comparaison : o, O, équivalents", "notions": ["landau", "limites"], "exos": [
        o("la1", r"Soient $(u_n)$, $(v_n)$ ne s'annulant pas. Rappeler les définitions de $u_n=o(v_n)$, $u_n=O(v_n)$ et $u_n\sim v_n$.",
          r"$u_n=o(v_n)$ : $\frac{u_n}{v_n}\to0$. $u_n=O(v_n)$ : $\left(\frac{u_n}{v_n}\right)$ est bornée. $u_n\sim v_n$ : $\frac{u_n}{v_n}\to1$.",
          src=f"{SR}, ex. 3.1", duree=2),
        o("la2", r"Comparer $u_n=-n^3+n-2$ et $v_n=-2n^2+n$ (toutes les relations).",
          r"$\frac{v_n}{u_n}=\frac{-2n^2+n}{-n^3+n-2}\sim\frac{-2n^2}{-n^3}=\frac2n\to0$. Donc $v_n=o(u_n)$, d'où $v_n=O(u_n)$. $\frac{u_n}{v_n}\to+\infty$ : ni $u=O(v)$, ni $u\sim v$.",
          src=f"{SR}, ex. 3.2a"),
        o("la3", r"Comparer $u_n=e^n+\sqrt n$ et $v_n=e^n+e^{-n}$.",
          r"$\frac{u_n}{v_n}=\frac{1+\sqrt ne^{-n}}{1+e^{-2n}}\to1$ (croissances comparées). Donc $u_n\sim v_n$, $u_n=O(v_n)$ et $v_n=O(u_n)$ ; pas de $o$.",
          src=f"{SR}, ex. 3.2b"),
        o("la4", r"Comparer $u_n=3^n+6$ et $v_n=5^n-1$.",
          r"$\frac{u_n}{v_n}=\frac{(3/5)^n+6/5^n}{1-1/5^n}\to0$. Donc $u_n=o(v_n)$ et $u_n=O(v_n)$ ; $v_n$ n'est pas $O(u_n)$, pas d'équivalence.",
          src=f"{SR}, ex. 3.2c"),
        o("la5", r"Comparer $u_n=1-2n^2$ et $v_n=-2n^2+n-3$.",
          r"$\frac{u_n}{v_n}=\frac{-2+1/n^2}{-2+1/n-3/n^2}\to1$ : $u_n\sim v_n$, $u=O(v)$ et $v=O(u)$.",
          src=f"{ASI}, ex. 3.1", duree=3),
        o("la6", r"Comparer $u_n=e^{2n}-\sqrt n$ et $v_n=n+1$, puis $u_n=4^n+1$ et $v_n=5^n$.",
          r"$\frac{v_n}{u_n}=\frac{n+1}{e^{2n}-\sqrt n}\to0$ : $v_n=o(u_n)$, $v_n=O(u_n)$. Puis $\frac{4^n+1}{5^n}=\left(\frac45\right)^n+\frac1{5^n}\to0$ : $u_n=o(v_n)$, $u_n=O(v_n)$.",
          src=f"{ASI}, ex. 3.2-3.3"),
    ]},
    {"n": 13, "titre": "Démonstrations du cours", "notions": ["demos", "gendarmes", "bornee"], "exos": [
        o("de1", r"Montrer : $(u_n)$ converge $\Rightarrow(u_n)$ bornée. La réciproque est-elle vraie ? Énoncer la contraposée.",
          r"Soit $\ell$ la limite. Avec $\varepsilon=1$ : $\exists N,\ \forall n\ge N,\ |u_n-\ell|\le1$, donc $|u_n|\le|\ell|+1$. Alors $M=\max(|u_0|,\dots,|u_{N-1}|,|\ell|+1)$ majore tous les $|u_n|$. Réciproque fausse : $(-1)^n$ est bornée et diverge. Contraposée : si $(u_n)$ n'est pas bornée, alors elle diverge.",
          src=f"{SR}, ex. 4"),
        o("de2", r"Énoncer rigoureusement puis démontrer le théorème des gendarmes.",
          r"Si $v_n\le u_n\le w_n$ à partir d'un rang $n_0$ et $v_n\to\ell$, $w_n\to\ell$, alors $u_n\to\ell$. Preuve : soit $\varepsilon>0$. $\exists N_1,\ n\ge N_1\Rightarrow v_n\ge\ell-\varepsilon$ ; $\exists N_2,\ n\ge N_2\Rightarrow w_n\le\ell+\varepsilon$. Pour $n\ge\max(n_0,N_1,N_2)$ : $\ell-\varepsilon\le v_n\le u_n\le w_n\le\ell+\varepsilon$, donc $|u_n-\ell|\le\varepsilon$.",
          src=f"{ASI}, ex. 4"),
        o("de3", r"Montrer l'unicité de la limite d'une suite convergente.",
          r"Supposons $u_n\to\ell$ et $u_n\to\ell'$ avec $\ell\ne\ell'$. Prenons $\varepsilon=\frac{|\ell-\ell'|}3>0$. Pour $n$ assez grand, $|u_n-\ell|\le\varepsilon$ et $|u_n-\ell'|\le\varepsilon$, donc $|\ell-\ell'|\le|\ell-u_n|+|u_n-\ell'|\le\frac23|\ell-\ell'|$ : contradiction."),
        o("de4", r"Écrire la définition de $u_n\to\ell$ et l'utiliser pour montrer que $\frac1n\to0$.",
          r"$\forall\varepsilon>0,\ \exists N\in\mathbb N,\ \forall n\ge N,\ |u_n-\ell|\le\varepsilon$. Soit $\varepsilon>0$ ; prenons $N=\lfloor1/\varepsilon\rfloor+1>\frac1\varepsilon$. Pour $n\ge N$ : $\left|\frac1n-0\right|=\frac1n\le\frac1N<\varepsilon$.", duree=3),
    ]},
    {"n": 14, "titre": "Niveau examen : annales complètes", "notions": ["adjacentes", "recurrentes", "landau", "extraites"], "examen": True, "exos": [
        {"id": "sx1", "kind": "multi", "src": f"{SR}, ex. 1 (7 points)",
         "enonce": r"$u_0=2$, $v_0=3$, $u_{n+1}=\frac{3u_n+2v_n}5$, $v_{n+1}=\frac{2u_n+3v_n}5$, $w_n=v_n-u_n$." "\n"
                   r"1. Montrer que $(w_n)$ est géométrique ; exprimer $w_n$ ; son signe." "\n"
                   r"2. Montrer que $(u_n)$ et $(v_n)$ sont adjacentes ; conséquence en $+\infty$." "\n"
                   r"3. $x_n=u_n+v_n$ : exprimer $x_{n+1}$ en fonction de $x_n$, puis $x_n$ ; en déduire les limites.",
         "parts": ["ad3", "ad4", "rg5"]},
        {"id": "sx2", "kind": "multi", "src": f"{SR}, ex. 2 (5 points)",
         "enonce": r"$u_n=\sum_{k=n}^{2n-1}\frac1k$, $n\ge1$." "\n"
                   r"1. Monotonie. 2. Montrer $\frac n{2n-1}\le u_n\le1$ ; minorant et majorant." "\n"
                   r"3. $(u_n)$ converge-t-elle ? Encadrer sa limite.",
         "parts": ["va5", "bo4", "lm3"]},
        {"id": "sx3", "kind": "multi", "src": f"{SR}, ex. 3 (7,5 points)",
         "enonce": r"1. Définitions de $o$, $O$, $\sim$." "\n"
                   r"2. Comparer : (a) $-n^3+n-2$ et $-2n^2+n$ ; (b) $e^n+\sqrt n$ et $e^n+e^{-n}$ ; (c) $3^n+6$ et $5^n-1$.",
         "parts": ["la1", "la2", "la3", "la4"]},
        {"id": "sx4", "kind": "multi", "src": f"{ASI}, ex. 5 (10 points)",
         "enonce": r"$u_0=1$, $u_{n+1}=\frac{u_n}{u_n+8}$." "\n"
                   r"1. (a) $u_n>0$ par récurrence. (b) Limites possibles. (c) Monotonie. (d) Convergence, limite." "\n"
                   r"2. $v_n=1+\frac7{u_n}$ : géométrique de raison $8$ ; $v_n$ puis $u_n$ en fonction de $n$ ; retrouver la limite.",
         "parts": ["re2", "rg4"]},
        {"id": "sx5", "kind": "multi", "src": f"{SR}, ex. 4-6 (10,5 points)",
         "enonce": r"1. (cours) Convergente $\Rightarrow$ bornée ; réciproque ; contraposée." "\n"
                   r"2. $u_0=\frac32$, $u_{n+1}=1+\frac{u_n^2}4$ : monotonie, $1<u_n<2$, limite." "\n"
                   r"3. $u_n=\sin\frac{n\pi}3$ : $u_{3n}$, $u_{6n+1}$, convergence.",
         "parts": ["de1", "re3", "ex1"]},
        {"id": "sx6", "kind": "multi", "src": f"{ASI}, ex. 2-4 et 6 (14 points)",
         "enonce": r"1. $u_n=\sum_{k=0}^n\frac1{k!}$, $v_n=u_n+\frac1{n!}$ : adjacentes, convergence, majorant." "\n"
                   r"2. Comparer $1-2n^2$ et $-2n^2+n-3$ ; $e^{2n}-\sqrt n$ et $n+1$ ; $4^n+1$ et $5^n$." "\n"
                   r"3. Énoncer et démontrer le théorème des gendarmes." "\n"
                   r"4. $u_n=\frac1n\sum_{k=0}^{n-1}(-1)^k$ : $u_{2n}$, $u_{2n+1}$, convergence.",
         "parts": ["ad2", "la5", "la6", "de2", "ex2"]},
    ]},
    {"n": 15, "titre": "Examen + 20 %", "notions": ["recurrentes", "adjacentes", "landau", "fi"], "examen": True, "exos": [
        o("sh1", r"$u_n=\sum_{k=1}^{n}\frac1{n+k}$. Étudier la monotonie, montrer $\frac12\le u_n<1$ et conclure sur la convergence.",
          r"$u_{n+1}-u_n=\frac1{2n+1}+\frac1{2n+2}-\frac1{n+1}=\frac1{2n+1}-\frac1{2n+2}>0$ : croissante. $n$ termes compris entre $\frac1{2n}$ et $\frac1{n+1}$ : $\frac12\le u_n\le\frac n{n+1}<1$. Croissante et majorée : converge, vers $\ell\in[\frac12,1]$ (en fait $\ln2$)."),
        o("sh2", r"$u_0=\frac32$, $u_{n+1}=\frac{u_n^2+2}3$. Montrer que $1<u_n<2$, étudier la monotonie et trouver la limite.",
          r"Points fixes : $\ell^2-3\ell+2=0$, $\ell\in\{1,2\}$. Si $1<u_n<2$ : $1<u_n^2<4$, $1<u_{n+1}<2$. $u_{n+1}-u_n=\frac{u_n^2-3u_n+2}3=\frac{(u_n-1)(u_n-2)}3<0$ : décroissante. Minorée par $1$ : converge vers $\ell\in[1,\frac32]$, donc $\ell=1$."),
        o("sh3", r"Comparer $u_n=\ln(n^2+1)$ et $v_n=\ln n$ ($n\ge2$).",
          r"$\ln(n^2+1)=2\ln n+\ln\left(1+\frac1{n^2}\right)$, donc $\frac{u_n}{v_n}=2+\frac{\ln(1+1/n^2)}{\ln n}\to2$. $u=O(v)$ et $v=O(u)$ ; $u\sim2v$ mais pas $u\sim v$ ; pas de $o$."),
        o("sh4", r"$u_n=\sum_{k=1}^{n}\frac{(-1)^{k+1}}k$. Montrer que $(u_{2n})$ et $(u_{2n+1})$ sont adjacentes et en déduire que $(u_n)$ converge.",
          r"$u_{2n+2}-u_{2n}=\frac1{2n+1}-\frac1{2n+2}>0$ ; $u_{2n+3}-u_{2n+1}=-\frac1{2n+2}+\frac1{2n+3}<0$ ; $u_{2n+1}-u_{2n}=\frac1{2n+1}\to0$. Adjacentes : même limite $\ell$. Les termes pairs et impairs tendent vers $\ell$, donc $u_n\to\ell$."),
        v("sh5", r"Limite de $\sqrt{n^2+3n}-\sqrt{n^2+n}$ ?", "limit(sqrt(n**2+3*n)-sqrt(n**2+n), n, oo)", "1",
          r"$\frac{2n}{\sqrt{n^2+3n}+\sqrt{n^2+n}}=\frac{2}{\sqrt{1+3/n}+\sqrt{1+1/n}}\to1$."),
    ]},
]


# Variants (same method, other numbers): a failed exercise comes back with the next one; build.py checks calc == ans.
def _v(enonce, calc, ans, sol):
    return {"enonce": enonce, "calc": calc, "ans": ans, "sol": sol}


VARIANTS = {
    "ag1": [_v(r"$(u_n)$ est arithmétique, $u_0=7$, raison $-2$. Calculer $u_{15}$.", "7+15*(-2)", "-23", r"$u_{15}=7-30=-23$.")],
    "ag2": [_v(r"$(v_n)$ est géométrique, $v_0=3$, raison $3$. Calculer $v_5$.", "3*3**5", "729", r"$v_5=3\times3^5=729$.")],
    "ag3": [_v(r"Calculer $1+2+\dots+50$.", "summation(k,(k,1,50))", "1275", r"$\frac{50\times51}2=1275$.")],
    "ag4": [_v(r"Calculer $\sum_{k=0}^{7}2^k$.", "summation(2**k,(k,0,7))", "255", r"8 termes de raison $2$ : $\frac{2^8-1}{2-1}=255$.")],
    "ag5": [_v(r"$(u_n)$ est arithmétique avec $u_2=5$ et $u_6=17$. Calculer $u_{40}$.", "5+(40-2)*3", "119",
               r"$4r=12$ donc $r=3$ ; $u_{40}=u_2+38r=5+114=119$.")],
    "li1": [_v(r"Limite de $\frac{2n^2-1}{4n^2+n}$ ?", "limit((2*n**2-1)/(4*n**2+n), n, oo)", "Rational(1,2)",
               r"$\frac{n^2(2-1/n^2)}{n^2(4+1/n)}\to\frac24=\frac12$.")],
    "li2": [_v(r"Limite de $\frac{3n+2}{n^3+1}$ ?", "limit((3*n+2)/(n**3+1), n, oo)", "0", r"$\frac1{n^2}\cdot\frac{3+2/n}{1+1/n^3}\to0$.")],
    "li3": [_v(r"Limite de $\frac{n^4+1}{2n^2+3}$ ?", "limit((n**4+1)/(2*n**2+3), n, oo)", "oo", r"$n^2\cdot\frac{1+1/n^4}{2+3/n^2}\to+\infty$.")],
    "li4": [_v(r"Limite de $n^3e^{-n}$ ?", "limit(n**3*exp(-n), n, oo)", "0", r"Croissances comparées : $\frac{n^3}{e^n}\to0$.")],
    "li5": [_v(r"Limite de $\frac{5^n-4^n}{5^n}$ ?", "limit((5**n-4**n)/5**n, n, oo)", "1", r"$1-\left(\frac45\right)^n\to1$.")],
    "li6": [_v(r"Limite de $n^3\left(\frac12\right)^n$ ?", "limit(n**3*Rational(1,2)**n, n, oo)", "0", r"$\frac{n^3}{2^n}\to0$ : l'exponentielle gagne.")],
    "li7": [_v(r"Limite de $\frac{(\ln n)^2}{n}$ ?", "limit(log(n)**2/n, n, oo)", "0", r"$\frac{(\ln n)^a}{n^b}\to0$ avec $a=2$, $b=1$.")],
    "li8": [_v(r"Limite de $\frac{10^n}{n!}$ ?", "limit(10**n/factorial(n), n, oo)", "0", r"$\frac{q^n}{n!}\to0$ pour tout $q$.")],
    "fi1": [_v(r"Limite de $\sqrt{n+3}-\sqrt n$ ?", "limit(sqrt(n+3)-sqrt(n), n, oo)", "0",
               r"Quantité conjuguée : $\frac3{\sqrt{n+3}+\sqrt n}\to0$.")],
    "fi2": [_v(r"Limite de $\sqrt{n^2+4n}-n$ ?", "limit(sqrt(n**2+4*n)-n, n, oo)", "2",
               r"$\frac{4n}{\sqrt{n^2+4n}+n}=\frac4{\sqrt{1+4/n}+1}\to2$.")],
    "fi3": [_v(r"Limite de $\left(1+\frac2n\right)^n$ ?", "limit((1+2/n)**n, n, oo)", "exp(2)",
               r"$e^{n\ln(1+2/n)}$ et $n\ln\left(1+\frac2n\right)=2\cdot\frac{\ln(1+x)}x$ avec $x=\frac2n\to0$ : limite $e^2$.")],
    "fi4": [_v(r"Limite de $n\sin\frac3n$ ?", "limit(n*sin(3/n), n, oo)", "3", r"$3\cdot\frac{\sin x}x$ avec $x=\frac3n\to0$ : limite $3$.")],
    "fi5": [_v(r"Limite de $\frac{2\cdot3^n+2^n}{3^n+1}$ ?", "limit((2*3**n+2**n)/(3**n+1), n, oo)", "2",
               r"Diviser par $3^n$ : $\frac{2+(2/3)^n}{1+3^{-n}}\to2$.")],
    "ge2": [_v(r"Limite de $\frac{2n+\sin n}{n}$ ? (justifier par encadrement)", "limit((2*n+sin(n))/n, n, oo)", "2",
               r"$2-\frac1n\le\frac{2n+\sin n}n\le2+\frac1n$ : limite $2$.")],
    "rg1": [_v(r"$u_0=4$, $u_{n+1}=3u_n-4$. Trouver $u_n$ en fonction de $n$ puis calculer $u_4$.", "2+2*3**4", "164",
               r"Point fixe $\ell=2$ ; $v_n=u_n-2$ est géométrique de raison $3$, $v_0=2$ : $u_n=2+2\cdot3^n$, $u_4=164$.")],
    "rg2": [_v(r"$u_0=1$, $u_{n+1}=\frac{u_n}3+2$. Limite de $(u_n)$ ?", "limit(3-2*Rational(1,3)**n, n, oo)", "3",
               r"$\ell=\frac\ell3+2$ donne $\ell=3$ ; $u_n-3=-2\left(\frac13\right)^n\to0$, donc $u_n\to3$.")],
    "rg3": [_v(r"$u_0=1$, $u_{n+1}=2u_n+1$. Exprimer $u_n$ puis calculer $u_5$.", "2**6-1", "63",
               r"$\ell=-1$ ; $u_n+1=2^n(u_0+1)=2^{n+1}$, donc $u_n=2^{n+1}-1$ et $u_5=63$.")],
    "sh5": [_v(r"Limite de $\sqrt{n^2+5n}-\sqrt{n^2+n}$ ?", "limit(sqrt(n**2+5*n)-sqrt(n**2+n), n, oo)", "2",
               r"$\frac{4n}{\sqrt{n^2+5n}+\sqrt{n^2+n}}=\frac4{\sqrt{1+5/n}+\sqrt{1+1/n}}\to2$.")],
}
for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["id"] in VARIANTS:
            _e["variants"] = VARIANTS[_e["id"]]


EXTRA_PARTS = []

QUIZ = [
    {"notion": "arith-geo", "type": "qcm", "q": r"$\sum_{k=0}^{n}q^k$ ($q\ne1$) $=$ ?",
     "choix": [r"$\frac{1-q^{n+1}}{1-q}$", r"$\frac{1-q^{n}}{1-q}$", r"$nq$", r"$\frac{q^n}{1-q}$"], "bonne": 0},
    {"notion": "arith-geo", "type": "vf", "q": r"Si $|q|<1$, $q^n\to0$.", "bonne": True},
    {"notion": "variation", "type": "qcm", "q": r"$u_n>0$ et $\frac{u_{n+1}}{u_n}\le1$ pour tout $n$ : $(u_n)$ est",
     "choix": [r"décroissante", r"croissante", r"constante", r"on ne peut rien dire"], "bonne": 0},
    {"notion": "variation", "type": "vf", "q": r"$u_n=\frac n{n+1}$ est décroissante.", "bonne": False},
    {"notion": "bornee", "type": "vf", "q": r"Une suite bornée est convergente.", "bonne": False},
    {"notion": "bornee", "type": "qcm", "q": r"Somme de $n$ termes, chacun entre $a$ et $b$ :",
     "choix": [r"$na\le S\le nb$", r"$a\le S\le b$", r"$a^n\le S\le b^n$", r"$S\le n$"], "bonne": 0},
    {"notion": "limites", "type": "qcm", "q": r"$\lim\frac{3n^2+1}{n^2+5}=$ ?",
     "choix": [r"$3$", r"$\frac15$", r"$+\infty$", r"$0$"], "bonne": 0},
    {"notion": "limites", "type": "vf", "q": r"$\frac{n^{10}}{2^n}\to0$", "bonne": True},
    {"notion": "fi", "type": "qcm", "q": r"$\lim\left(\sqrt{n^2+n}-n\right)=$ ?",
     "choix": [r"$\frac12$", r"$0$", r"$1$", r"$+\infty$"], "bonne": 0},
    {"notion": "fi", "type": "qcm", "q": r"$\lim\left(1+\frac1n\right)^n=$ ?",
     "choix": [r"$e$", r"$1$", r"$+\infty$", r"$0$"], "bonne": 0},
    {"notion": "gendarmes", "type": "vf", "q": r"$v_n\le u_n\le w_n$, $v_n\to0$, $w_n\to1$ : $(u_n)$ converge.", "bonne": False},
    {"notion": "gendarmes", "type": "qcm", "q": r"$\lim\frac{\sin n}n=$ ?",
     "choix": [r"$0$", r"$1$", r"n'existe pas", r"$+\infty$"], "bonne": 0},
    {"notion": "arith-geo-rec", "type": "qcm", "q": r"$u_{n+1}=2u_n-3$ : point fixe ?",
     "choix": [r"$3$", r"$-3$", r"$\frac32$", r"$1$"], "bonne": 0},
    {"notion": "arith-geo-rec", "type": "vf", "q": r"Si $u_{n+1}=au_n+b$ et $\ell=a\ell+b$, alors $u_n-\ell$ est géométrique de raison $a$.", "bonne": True},
    {"notion": "monotone", "type": "vf", "q": r"Une suite croissante et majorée converge.", "bonne": True},
    {"notion": "monotone", "type": "vf", "q": r"Une suite croissante tend vers $+\infty$.", "bonne": False},
    {"notion": "adjacentes", "type": "qcm", "q": r"Adjacentes : $(u_n)\nearrow$, $(v_n)\searrow$ et",
     "choix": [r"$v_n-u_n\to0$", r"$u_n\le v_n$", r"$u_0=v_0$", r"$v_n-u_n$ constante"], "bonne": 0},
    {"notion": "adjacentes", "type": "vf", "q": r"Deux suites adjacentes convergent vers la même limite.", "bonne": True},
    {"notion": "recurrentes", "type": "qcm", "q": r"$u_{n+1}=\frac{u_n}{u_n+8}$, $u_n>0$ : limites possibles ?",
     "choix": [r"$0$ seulement", r"$0$ et $-7$", r"$-7$", r"$\frac18$"], "bonne": 0},
    {"notion": "recurrentes", "type": "vf", "q": r"Si $u_{n+1}=f(u_n)$, toute solution de $\ell=f(\ell)$ est la limite de $(u_n)$.", "bonne": False},
    {"notion": "extraites", "type": "vf", "q": r"$u_{2n}\to1$ et $u_{2n+1}\to-1$ : $(u_n)$ diverge.", "bonne": True},
    {"notion": "extraites", "type": "qcm", "q": r"$u_n=\sin\frac{n\pi}3$ : $u_{6n+1}=$ ?",
     "choix": [r"$\frac{\sqrt3}2$", r"$0$", r"$\frac12$", r"$1$"], "bonne": 0},
    {"notion": "landau", "type": "qcm", "q": r"$\frac{u_n}{v_n}\to0$ :",
     "choix": [r"$u_n=o(v_n)$", r"$u_n\sim v_n$", r"$v_n=o(u_n)$", r"$v_n=O(u_n)$"], "bonne": 0},
    {"notion": "landau", "type": "vf", "q": r"$3n+6\sim5n-1$", "bonne": False},
    {"notion": "landau", "type": "vf", "q": r"$4^n+1=o(5^n)$", "bonne": True},
    {"notion": "demos", "type": "vf", "q": r"La réciproque de « convergente $\Rightarrow$ bornée » est vraie.", "bonne": False},
]

# Formulas used in each solution (help « Formules de la solution »); multi exercises get those of their parts.
_GEO = r"$\sum_{k=0}^{n}q^k=\frac{1-q^{n+1}}{1-q}$ ($q\ne1$)"
_DIFF = r"signe de $u_{n+1}-u_n$ : $\ge0$ croissante, $\le0$ décroissante"
_DOM = r"factoriser par le terme dominant : $\frac{P(n)}{Q(n)}$ se comporte comme le quotient des termes de plus haut degré"
_QN = r"$q^n\to0$ si $|q|<1$"
_CONJ = r"quantité conjuguée : $\sqrt a-\sqrt b=\frac{a-b}{\sqrt a+\sqrt b}$"
_GEND = r"gendarmes : $v_n\le u_n\le w_n$, $v_n\to\ell$ et $w_n\to\ell$ $\Rightarrow u_n\to\ell$"
_FIXE = r"$u_{n+1}=au_n+b$ : point fixe $\ell=a\ell+b$, puis $u_n-\ell=a^n(u_0-\ell)$"
_MONO = r"limite monotone : croissante et majorée $\Rightarrow$ converge · décroissante et minorée $\Rightarrow$ converge"
_ADJ = r"adjacentes : $(u_n)$ croissante, $(v_n)$ décroissante, $v_n-u_n\to0$ $\Rightarrow$ même limite $\ell$, et $u_n\le\ell\le v_n$"
_PF = r"si $u_n\to\ell$ et $f$ continue en $\ell$ : $\ell=f(\ell)$"
_REC = r"récurrence : initialisation, puis hérédité ($P(n)\Rightarrow P(n+1)$)"
_EXTD = r"deux suites extraites de limites différentes $\Rightarrow$ $(u_n)$ diverge"
_LANDAU = r"$u_n=o(v_n)$ : $\frac{u_n}{v_n}\to0$ · $u_n=O(v_n)$ : $\frac{u_n}{v_n}$ bornée · $u_n\sim v_n$ : $\frac{u_n}{v_n}\to1$"
_CC = r"croissances comparées : $\ln n\ll n^a\ll q^n\ll n!$ ($a>0$, $q>1$)"
_DEF = r"$u_n\to\ell\iff\forall\varepsilon>0,\ \exists N,\ \forall n\ge N,\ |u_n-\ell|\le\varepsilon$"
_ENC = r"somme de $p$ termes : $p\times\min\le\sum\le p\times\max$"
FORMULES = {
    "ag1": r"$u_n=u_0+nr$",
    "ag2": r"$v_n=v_0q^n$",
    "ag3": r"$\sum_{k=1}^{n}k=\frac{n(n+1)}2$",
    "ag4": _GEO,
    "ag5": r"$u_n=u_p+(n-p)r$",
    "va1": _DIFF, "va3": _DIFF, "va4": _DIFF, "va5": _DIFF,
    "va2": r"si $u_n>0$ : $\frac{u_{n+1}}{u_n}\le1$ $\Rightarrow$ décroissante · $(n+1)!=(n+1)\,n!$",
    "bo1": r"bornée $\iff\exists M\ge0,\ \forall n,\ |u_n|\le M$ · $-1\le(-1)^n\le1$",
    "bo2": r"bornée : $\exists m,M,\ \forall n,\ m\le u_n\le M$ · écrire $\frac{2n+1}{n+3}=2-\frac5{n+3}$",
    "bo3": r"bornée : $\exists m,M',\ \forall n,\ m\le u_n\le M'$ · $|x|\le M\iff-M\le x\le M$",
    "bo4": _ENC,
    "bo5": r"$|a+b|\le|a|+|b|$ · $|\cos|\le1$, $|\sin|\le1$",
    "li1": _DOM, "li2": _DOM, "li3": _DOM,
    "li4": r"$\frac{n^a}{q^n}\to0$ ($q>1$), avec $q=e$",
    "li5": _QN,
    "li6": r"$\frac{n^a}{q^n}\to0$ ($q>1$)",
    "li7": r"$\frac{(\ln n)^a}{n^b}\to0$ ($b>0$)",
    "li8": r"$\frac{q^n}{n!}\to0$",
    "fi1": _CONJ, "fi2": _CONJ, "sh5": _CONJ,
    "fi3": r"$a^b=e^{b\ln a}$ · $\frac{\ln(1+x)}{x}\xrightarrow[x\to0]{}1$",
    "fi4": r"$\frac{\sin x}{x}\xrightarrow[x\to0]{}1$",
    "fi5": r"factoriser par la plus grande puissance · " + _QN,
    "ge1": _GEND + r" · $-1\le\sin n\le1$",
    "ge2": _GEND + r" · $-1\le\cos n\le1$",
    "ge3": _ENC + " · " + _GEND,
    "ge4": r"comparaison : $u_n\ge v_n$ et $v_n\to+\infty$ $\Rightarrow u_n\to+\infty$ · $(-1)^n\ge-1$",
    "ge5": r"$x-1<\lfloor x\rfloor\le x$ · " + _GEND,
    "rg1": _FIXE, "rg2": _FIXE + " · " + _QN, "rg3": _FIXE,
    "rg4": r"géométrique : $v_{n+1}=q\,v_n$, alors $v_n=v_0q^n$",
    "rg5": r"calculer $x_{n+1}$ en fonction de $x_n$ · suite constante : $x_n=x_0$",
    "lm1": _MONO + r" · télescopage : $\sum_{k=2}^{n}\left(\frac1{k-1}-\frac1k\right)=1-\frac1n$",
    "lm2": _MONO + " · " + _GEO,
    "lm3": _MONO + r" · passage à la limite dans une inégalité large : $a\le u_n\le b\Rightarrow a\le\ell\le b$",
    "lm4": r"croissante et majorée $\Rightarrow$ converge · croissante non majorée $\Rightarrow+\infty$",
    "ad1": _ADJ, "ad2": _ADJ, "ad4": _ADJ, "ad5": _ADJ,
    "ad3": r"géométrique : $w_{n+1}=q\,w_n$, alors $w_n=w_0q^n$",
    "re1": _REC + " · " + _MONO + " · " + _PF,
    "re2": _REC + " · " + _PF + r" · si $u_n>0$ : $\frac{u_{n+1}}{u_n}<1$ $\Rightarrow$ décroissante · " + _MONO,
    "re3": _DIFF + " · " + _REC + " · " + _MONO + " · " + _PF,
    "re4": _REC + " · " + _MONO + " · " + _PF,
    "re5": _PF,
    "ex1": _EXTD + r" · $\sin(x+2n\pi)=\sin x$, $\sin(n\pi)=0$",
    "ex2": r"$u_{2n}\to\ell$ et $u_{2n+1}\to\ell\Rightarrow u_n\to\ell$",
    "ex3": _EXTD, "ex4": _EXTD + r" · $\cos(x+2n\pi)=\cos x$",
    "la1": _LANDAU,
    "la2": _LANDAU + " · " + _DOM,
    "la3": _LANDAU + " · " + _CC,
    "la4": _LANDAU + " · " + _QN,
    "la5": _LANDAU + " · " + _DOM,
    "la6": _LANDAU + " · " + _CC + " · " + _QN,
    "de1": _DEF + r" avec $\varepsilon=1$ · $|u_n|\le|u_n-\ell|+|\ell|$",
    "de2": _DEF + r" · $N=\max(n_0,N_1,N_2)$",
    "de3": _DEF + r" · inégalité triangulaire : $|\ell-\ell'|\le|\ell-u_n|+|u_n-\ell'|$",
    "de4": _DEF,
    "sh1": _DIFF + " · " + _ENC + " · " + _MONO,
    "sh2": _REC + " · " + _DIFF + " · " + _MONO + " · " + _PF,
    "sh3": _LANDAU + r" · $\ln(ab)=\ln a+\ln b$",
    "sh4": _ADJ + r" · $u_{2n}\to\ell$ et $u_{2n+1}\to\ell\Rightarrow u_n\to\ell$",
}
