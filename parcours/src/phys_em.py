"""Level path: S2 physics, electromagnetism (Coulomb, field, superposition, potential, energy, continuous charges, Lorentz).

Calibrated on the Moodle course « Cours_Electromagnétisme_V1 » and the TD1-5 (B4, read as images). No S2 electromagnetism exam
is transcribed yet. k = 9×10^9 N·m²·C⁻² as in the course approximations; `value` exercises are checked by sympy.
"""

SUBJECT = {
    "id": "physique-s2-em",
    "ordre": 320,
    "matiere": "physique",
    "semestre": "S2",
    "ecue": "Électromagnétisme",
    "titre": "Électromagnétisme",
    "chapitres_moodle": ["02_Cours", "03_TD_Electromagnétisme"],
    "td": "TD électromagnétisme (Moodle Physique)",
    "examens": ["Partiel de physique (S2)"],
}

NOTIONS = [
    {"id": "coulomb", "titre": "Loi de Coulomb",
     "formule": r"$\vec F_{1\to2}=k\dfrac{q_1q_2}{r^2}\vec u_{12}$ · $k=\dfrac1{4\pi\varepsilon_0}\approx9\times10^9$ N·m²·C$^{-2}$ · même signe : répulsion, signes opposés : attraction",
     "exemple": r"$q_1=q_2=1\ \mu$C à $3$ cm : $F=\dfrac{9\times10^9\times10^{-12}}{9\times10^{-4}}=10$ N",
     "cours": r"Comme la gravitation, la force varie en $\frac1{r^2}$. Différence : les charges peuvent être négatives, la force électrique est attractive ou répulsive. Convertir en coulombs et en mètres avant de calculer ($1\ \mu\mathrm C=10^{-6}$ C, $1$ nC $=10^{-9}$ C)."},
    {"id": "champ", "titre": "Champ électrique d'une charge",
     "formule": r"$\vec F=q\vec E$ · $\vec E=k\dfrac{q_1}{r^2}\vec u_r$ · en N·C$^{-1}$ ou V·m$^{-1}$ · charge positive : champ sortant ; négative : champ rentrant",
     "exemple": r"$q=2$ nC à $0{,}3$ m : $E=\dfrac{9\times10^9\times2\times10^{-9}}{0{,}09}=200$ V·m$^{-1}$",
     "cours": r"Le champ d'une charge n'agit pas sur elle-même. Une ligne de champ est tangente au champ : $d\vec l\wedge\vec E=\vec0$. Entre deux charges opposées, les lignes vont de la positive vers la négative."},
    {"id": "superposition", "titre": "Principe de superposition",
     "formule": r"$\vec E_{tot}(M)=\sum_i\vec E_i(M)$ (somme vectorielle) · $\vec u_x$, $\vec u_y$ : projeter chaque champ sur les axes · triangle équilatéral : $\cos60^\circ=\frac12$, $\sin60^\circ=\frac{\sqrt3}2$",
     "exemple": r"deux charges $Q$ à la base d'un triangle équilatéral de côté $r$ : en $M$ au sommet, $E=\dfrac{2kQ\sin60^\circ}{r^2}=\dfrac{\sqrt3\,kQ}{r^2}$ sur l'axe de symétrie",
     "cours": r"Calculer le champ de chaque charge comme si elle était seule, dessiner les vecteurs, projeter, additionner. Le champ d'une charge positive s'éloigne d'elle, celui d'une charge négative pointe vers elle."},
    {"id": "symetrie", "titre": "Symétries et antisymétries",
     "formule": r"plan de symétrie $\Pi$ : $\vec E(M)$ est dans $\Pi$ pour $M\in\Pi$ · plan d'antisymétrie $\Pi^*$ : $\vec E(M)$ est orthogonal à $\Pi^*$ pour $M\in\Pi^*$",
     "exemple": r"quatre charges identiques aux sommets d'un carré : $\vec E(O)=\vec0$",
     "cours": r"Chercher les symétries avant tout calcul : elles disent quelles composantes du champ sont nulles. Une distribution peut avoir plusieurs plans."},
    {"id": "energie", "titre": "Énergie électrostatique",
     "formule": r"$E_{pe}=k\dfrac{qq'}r$ (en $\frac1r$, pas $\frac1{r^2}$) · plusieurs charges : somme sur toutes les paires · $>0$ si même signe (il faut fournir de l'énergie)",
     "exemple": r"$q=2$ nC et $q'=3$ nC à $6$ cm : $E_{pe}=\dfrac{9\times10^9\times6\times10^{-18}}{0{,}06}=9\times10^{-7}$ J",
     "cours": r"L'énergie à fournir pour assembler une distribution est la somme des $k\frac{q_iq_j}{r_{ij}}$ sur chaque paire, comptée une fois. L'ordre d'assemblage ne change pas le total."},
    {"id": "potentiel", "titre": "Potentiel électrostatique",
     "formule": r"$V(M)=k\dfrac qr$ (volt) · plusieurs charges : $V=\sum k\dfrac{q_i}{r_i}$ · $V=\dfrac{E_{pe}}{q'}$ · $\vec E=-\overrightarrow{\mathrm{grad}}\,V$ · $\overrightarrow{\mathrm{grad}}f=\dfrac{\partial f}{\partial x}\vec u_x+\dfrac{\partial f}{\partial y}\vec u_y+\dfrac{\partial f}{\partial z}\vec u_z$",
     "exemple": r"$q=2$ nC à $0{,}3$ m : $V=60$ V, et $E=\dfrac Vr=200$ V·m$^{-1}$",
     "cours": r"Le potentiel est un scalaire : on additionne simplement les valeurs (avec leur signe), sans projeter. Les équipotentielles sont les courbes de niveau de $V$. Le champ pointe vers les potentiels décroissants."},
    {"id": "continu", "titre": "Distributions continues de charge",
     "formule": r"$Q=\int\lambda\,dl$ · $Q=\iint\sigma\,dS$ · $Q=\iiint\rho\,dV$ · $dl=dx$ (segment), $dl=R\,d\theta$ (arc) · $d^2S=dx\,dy$ (rectangle), $d^2S=r\,dr\,d\theta$ (disque)",
     "exemple": r"fil de longueur $L$, $\lambda=3$ C·m$^{-1}$ : $Q=3L$ ; si $\lambda=x$ : $Q=\int_0^Lx\,dx=\frac{L^2}2$",
     "cours": r"Choisir l'élément d'intégration adapté à la géométrie, écrire $dQ=\lambda\,dl$ (ou $\sigma\,dS$), puis intégrer sur toute la distribution. Si la densité dépend d'une variable, elle reste dans l'intégrale."},
    {"id": "lorentz", "titre": "Force de Lorentz et particule dans $\\vec B$",
     "formule": r"$\vec F=q\vec E+q\vec v\wedge\vec B$ · $\vec F_{mag}\perp\vec v$ : elle ne travaille pas · $\vec E$ seul accélère : $\frac12mv^2=q\,U$ · $\vec B$ seul : mouvement circulaire uniforme de rayon $R=\dfrac{mv}{|q|B}$",
     "exemple": r"$m=1{,}6\times10^{-27}$ kg, $v=10^5$ m·s$^{-1}$, $q=1{,}6\times10^{-19}$ C, $B=0{,}5$ T : $R=2$ mm",
     "cours": r"La force magnétique incurve la trajectoire sans changer la norme de la vitesse. Sens de $\vec v\wedge\vec B$ : règle de la main droite ou déterminant. Le spectromètre de masse sépare les isotopes : à $U$ et $B$ fixés, $R\propto\sqrt m$."},
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


T1 = "TD1 d'électromagnétisme"
T2 = "TD2 d'électromagnétisme"
T3 = "TD3 d'électromagnétisme"
T4 = "TD4 d'électromagnétisme"
T5 = "TD5 d'électromagnétisme"

LEVELS = [
    {"n": 1, "titre": "Loi de Coulomb", "notions": ["coulomb"], "exos": [
        v("ec1", r"Deux charges de $1\ \mu$C sont à $3$ cm l'une de l'autre. Norme de la force (en N) avec $k=9\times10^9$ ?", "9*10**9*10**-12/(Rational(3,100))**2", "10",
          r"$F=k\frac{q^2}{r^2}=\frac{9\times10^9\times10^{-12}}{9\times10^{-4}}=10$ N.", duree=2),
        v("ec2", r"On double la distance entre deux charges. Par combien est multipliée la force ?", "Rational(1,4)", "1/4", r"$F\propto\frac1{r^2}$ : $\frac1{2^2}=\frac14$.", duree=1),
        v("ec3", r"Charges $+2\ \mu$C et $-3\ \mu$C à $0{,}1$ m. Norme de la force (en N) ?", "9*10**9*6*10**-12/Rational(1,100)", "27/5",
          r"$F=\frac{9\times10^9\times6\times10^{-12}}{10^{-2}}=5{,}4$ N ; signes opposés : attractive.", duree=3),
        v("ec4", r"Rapport entre la force de Coulomb et la force gravitationnelle entre deux protons ($e=1{,}6\times10^{-19}$ C, $m=1{,}67\times10^{-27}$ kg, $G=6{,}67\times10^{-11}$), indépendant de la distance. Ordre de grandeur ?",
          "9*10**9*(Rational(16,10)*10**-19)**2/(Rational(667,100)*10**-11*(Rational(167,100)*10**-27)**2)", "9*10**9*(Rational(16,10)*10**-19)**2/(Rational(667,100)*10**-11*(Rational(167,100)*10**-27)**2)",
          r"$\dfrac{ke^2}{Gm^2}=\dfrac{9\times10^9\times2{,}56\times10^{-38}}{6{,}67\times10^{-11}\times2{,}79\times10^{-54}}\approx1{,}2\times10^{36}$ : la gravitation est négligeable.", src="Cours, partie I.2", duree=4),
        o("ec5", r"Donner deux ressemblances et une différence entre la force de Coulomb et la force de gravitation.",
          r"Ressemblances : toutes deux en $\frac1{r^2}$ et dirigées selon la droite qui joint les corps. Différence : les masses sont positives donc la gravitation est toujours attractive ; les charges ont un signe, la force électrique est attractive ou répulsive.", duree=3),
    ]},
    {"n": 2, "titre": "Champ électrique d'une charge", "notions": ["champ"], "exos": [
        v("ee1", r"Champ (en V·m$^{-1}$) créé par $q=2$ nC à $0{,}3$ m ?", "9*10**9*2*10**-9/Rational(9,100)", "200", r"$E=\frac{kq}{r^2}=\frac{18}{0{,}09}=200$ V·m$^{-1}$.", duree=2),
        v("ee2", r"Force (en N) sur une charge $Q=5\ \mu$C placée dans un champ de $200$ V·m$^{-1}$ ?", "5*10**-6*200", "1/1000", r"$F=QE=5\times10^{-6}\times200=10^{-3}$ N.", duree=2),
        v("ee3", r"À quelle distance (en m) d'une charge $q=2$ nC le champ vaut-il $50$ V·m$^{-1}$ ?", "sqrt(9*10**9*2*10**-9/50)", "3/5", r"$r=\sqrt{\frac{kq}E}=\sqrt{\frac{18}{50}}=0{,}6$ m.", duree=3),
        o("ee4", r"Une charge $q<0$ est seule dans l'espace. Quel est le sens du champ et l'allure des lignes de champ ? Même question pour deux charges $+q$ et $-q$.",
          r"Charge seule négative : champ radial rentrant, lignes qui convergent vers la charge. Deux charges $+q$, $-q$ : les lignes partent de $+q$ et arrivent sur $-q$, sans se refermer.", duree=3),
    ]},
    {"n": 3, "titre": "Superposition de charges", "notions": ["superposition", "champ"], "exos": [
        v("es1", r"Charges $+1$ nC en $x=0$ et $-1$ nC en $x=0{,}3$ m. Champ (en V·m$^{-1}$) au milieu du segment ?", "2*9*10**9*10**-9/Rational(225,10000)", "800",
          r"Au milieu ($r=0{,}15$ m), la charge positive repousse vers $+x$ et la négative attire vers $+x$ : $E=2\frac{kq}{r^2}=\frac{18}{0{,}0225}=800$ V·m$^{-1}$.", duree=4),
        v("es2", r"Quatre charges sur un cercle de rayon $R=0{,}3$ m : $A(-q)$ en haut, $B(-q)$ à droite, $C(+q)$ en bas, $D(+q)$ à gauche, $q=1$ nC. Norme du champ en $O$ (en V·m$^{-1}$) ?", "2*sqrt(2)*9*10**9*10**-9/Rational(9,100)", "200*sqrt(2)",
          r"Chaque charge crée $\frac{kq}{R^2}=100$ V·m$^{-1}$. $A$ et $C$ donnent chacune $+\vec u_y$ ; $B$ et $D$ chacune $+\vec u_x$. $\vec E=200(\vec u_x+\vec u_y)$, norme $200\sqrt2$.", src=T1 + ", ex. 1", duree=6),
        v("es3", r"Force (en N) sur $Q=2\ \mu$C placée en $O$ dans la situation précédente ?", "2*10**-6*200*sqrt(2)", "sqrt(2)/2500", r"$F=QE=2\times10^{-6}\times200\sqrt2=4\sqrt2\times10^{-4}$ N.", src=T1 + ", ex. 1", duree=2),
        v("es4", r"Deux charges $Q=1$ nC sur la base d'un triangle équilatéral de côté $r=0{,}3$ m. Champ (en V·m$^{-1}$) au troisième sommet ?", "sqrt(3)*9*10**9*10**-9/Rational(9,100)", "100*sqrt(3)",
          r"Les composantes selon l'axe de la base s'annulent, celles selon l'axe de symétrie s'ajoutent : $E=\frac{2kQ\sin60^\circ}{r^2}=\sqrt3\times100$.", src="Cours, exemple 1", duree=5),
        o("es5", r"Énoncer le principe de superposition et la méthode pour l'appliquer.",
          r"Le champ créé par plusieurs charges est la somme vectorielle des champs que chacune créerait seule. Méthode : un schéma, le vecteur de chaque charge (sortant si $q>0$, rentrant si $q<0$), projection sur les axes, somme des composantes.", duree=3),
    ]},
    {"n": 4, "titre": "Symétries et antisymétries", "notions": ["symetrie", "superposition"], "exos": [
        o("esy1", r"Que peut-on dire de la direction du champ en un point d'un plan de symétrie ? d'un plan d'antisymétrie ?",
          r"En un point d'un plan de symétrie $\Pi$, le champ appartient au plan. En un point d'un plan d'antisymétrie $\Pi^*$, le champ est perpendiculaire au plan.", duree=2),
        o("esy2", r"Deux charges $+q$ en $A(-a,0)$ et $-q$ en $B(a,0)$. Donner un plan de symétrie, un plan d'antisymétrie, et la direction de $\vec E$ en $O$.",
          r"Le plan $z=0$ (contenant les charges) est plan de symétrie ; le plan $x=0$ est plan d'antisymétrie (la distribution devient opposée). En $O$, point de $x=0$ : $\vec E\perp$ ce plan, donc $\vec E=E\,\vec u_x$.", duree=4),
        o("esy3", r"Quatre charges identiques $q$ aux sommets d'un carré. Montrer sans calcul que $\vec E(O)=\vec0$ au centre.",
          r"$O$ est sur les deux diagonales, plans de symétrie, donc $\vec E$ est dans les deux plans : il est colinéaire à leur intersection (l'axe perpendiculaire au carré) et, dans le plan du carré, la symétrie le force à être nul. Autre argument : les charges opposées par rapport à $O$ créent des champs opposés qui s'annulent deux à deux.", src=T3 + ", ex. 1", duree=4),
    ]},
    {"n": 5, "titre": "Champ sur un axe", "notions": ["superposition", "champ"], "exos": [
        v("ex1", r"$q$ en $A(0)$ et $q'$ en $B(d)$, $q=q'=1$ nC, $d=0{,}4$ m. Champ (en V·m$^{-1}$) en $x=0{,}1$ m, entre les deux ?", "9*10**9*10**-9*(1/Rational(1,100)-1/Rational(9,100))", "800",
          r"$A$ repousse vers $+x$ : $\frac{9}{0{,}01}=900$. $B$ repousse vers $-x$ : $\frac{9}{0{,}09}=100$. Total $800$ V·m$^{-1}$ selon $+x$.", src=T1 + ", ex. 2", duree=5),
        v("ex2", r"Mêmes charges, point $M$ en $x=0{,}8$ m ($x>d$). Champ (en V·m$^{-1}$) ?", "9*(1/Rational(64,100)+1/Rational(16,100))", "1125/16",
          r"Les deux champs pointent vers $+x$ : $\frac9{0{,}64}+\frac9{0{,}16}=14{,}06+56{,}25\approx70{,}3$ V·m$^{-1}$.", src=T1 + ", ex. 2", duree=5),
        v("ex3", r"$q=4$ nC en $0$, $q'=1$ nC en $d=0{,}3$ m. En quel point entre eux le champ s'annule-t-il (distance à $A$, en m) ?", "2*Rational(3,10)/3", "1/5",
          r"$\frac{kq}{x^2}=\frac{kq'}{(d-x)^2}$ donne $\frac x{d-x}=\sqrt{\frac q{q'}}=2$, donc $x=\frac{2d}3=0{,}2$ m.", src=T1 + ", ex. 2", duree=5),
        o("ex4", r"Le champ créé par deux charges sur l'axe $AB$ peut-il s'annuler ? Selon les signes, où ?",
          r"Même signe : le champ peut s'annuler seulement entre les charges (les deux champs s'opposent), plus près de la charge la plus petite en valeur absolue. Signes opposés : entre les charges les champs s'ajoutent, donc il ne s'annule qu'à l'extérieur du segment, du côté de la charge de plus petite valeur absolue.", src=T1 + ", ex. 2", duree=5),
    ]},
    {"n": 6, "titre": "Énergie électrostatique", "notions": ["energie", "coulomb"], "exos": [
        v("en1", r"$q=2$ nC et $q'=3$ nC à $6$ cm. Énergie électrostatique (en J) ?", "9*10**9*6*10**-18/Rational(6,100)", "9/10**7", r"$E_{pe}=\frac{kqq'}r=\frac{9\times10^9\times6\times10^{-18}}{0{,}06}=9\times10^{-7}$ J.", duree=3),
        v("en2", r"Mêmes valeurs mais $q'=-3$ nC. Énergie (en J) ?", "-9*10**9*6*10**-18/Rational(6,100)", "-9/10**7", r"Signes opposés : $E_{pe}=-9\times10^{-7}$ J, la configuration est liée.", duree=2),
        v("en3", r"On double la distance entre deux charges. Par combien est multipliée l'énergie électrostatique ?", "Rational(1,2)", "1/2", r"$E_{pe}\propto\frac1r$ : elle est divisée par $2$ (et non par $4$ comme la force).", duree=1),
        o("en4", r"Pourquoi faut-il fournir de l'énergie pour rapprocher deux charges de même signe, et pas deux charges de signes opposés ?",
          r"Charges de même signe : la force est répulsive, l'opérateur doit travailler contre elle, $E_{pe}=k\frac{qq'}r>0$ augmente quand $r$ diminue. Charges de signes opposés : la force est attractive, le rapprochement libère de l'énergie ($E_{pe}<0$).", duree=3),
    ]},
    {"n": 7, "titre": "Potentiel électrostatique", "notions": ["potentiel", "champ"], "exos": [
        v("ep1", r"Potentiel (en V) à $0{,}3$ m d'une charge $q=2$ nC ?", "9*10**9*2*10**-9/Rational(3,10)", "60", r"$V=\frac{kq}r=\frac{18}{0{,}3}=60$ V.", duree=2),
        v("ep2", r"En ce point, $V=60$ V à $r=0{,}3$ m de la charge. En déduire $E$ (en V·m$^{-1}$) avec $E=\frac Vr$.", "60/Rational(3,10)", "200", r"$E=-\frac{dV}{dr}=\frac{kq}{r^2}=\frac Vr=200$ V·m$^{-1}$.", duree=2),
        v("ep3", r"Quatre charges $-q,-q,+q,+q$ à égale distance $R$ de $O$. Potentiel en $O$ ?", "0", "0", r"$V(O)=\frac{k}R(-q-q+q+q)=0$ : le potentiel est un scalaire, on additionne.", src=T2 + ", ex. 1", duree=2),
        v("ep4", r"Charges $1$ nC à $0{,}3$ m et $3$ nC à $0{,}6$ m d'un point $M$. Potentiel (en V) en $M$ ?", "9*10**9*(10**-9/Rational(3,10)+3*10**-9/Rational(6,10))", "75", r"$V=9\times10^9\left(\frac{10^{-9}}{0{,}3}+\frac{3\times10^{-9}}{0{,}6}\right)=30+45=75$ V.", duree=4),
        o("ep5", r"Pour $V=\dfrac{kq}{\sqrt{x^2+y^2+z^2}}$, calculer $-\overrightarrow{\mathrm{grad}}\,V$ et retrouver $\vec E=k\dfrac q{r^2}\vec u_r$.",
          r"$\frac{\partial V}{\partial x}=-\frac{kqx}{r^3}$, de même pour $y$ et $z$. Donc $-\overrightarrow{\mathrm{grad}}V=\frac{kq}{r^3}(x,y,z)=\frac{kq}{r^2}\frac{\overrightarrow{OM}}r=\frac{kq}{r^2}\vec u_r$.", duree=6),
    ]},
    {"n": 8, "titre": "Énergie d'une distribution et potentiel nul", "notions": ["energie", "potentiel"], "exos": [
        v("ew1", r"Une charge $q=1$ nC est en $(0,0)$. On amène $2q$ depuis l'infini en $(0,-a)$ avec $a=0{,}1$ m. Énergie à fournir (en J) ?", "2*9*10**9*10**-18/Rational(1,10)", "18/10**8",
          r"$E=\frac{k\,q\cdot2q}a=\frac{2\times9\times10^9\times10^{-18}}{0{,}1}=1{,}8\times10^{-7}$ J.", src=T2 + ", ex. 3", duree=4),
        v("ew2", r"On ajoute $-2q$ en $(b,0)$ et $3q$ en $(b,-a)$ avec $a=b=0{,}1$ m, $q=1$ nC. Énergie totale d'assemblage des quatre charges (en J), sachant que le total vaut $kq^2\left(-\frac4a+\frac4b-\frac1{\sqrt{a^2+b^2}}\right)$ ?", "-9*10**9*10**-18*5*sqrt(2)", "-45*sqrt(2)/10**9",
          r"Paires : $q,2q$ ($a$) ; $q,-2q$ ($b$) ; $q,3q$ (diagonale $d$) ; $2q,-2q$ ($d$) ; $2q,3q$ ($b$) ; $-2q,3q$ ($a$). Somme : $kq^2\left(\frac2a-\frac2b+\frac3d-\frac4d+\frac6b-\frac6a\right)=kq^2\left(-\frac4a+\frac4b-\frac1d\right)$. Avec $a=b$ : $-\frac{kq^2}d=-5\sqrt2\,kq^2\approx-6{,}4\times10^{-8}$ J.", src=T2 + ", ex. 3", duree=8),
        o("ew3", r"Le potentiel peut-il être nul sur l'axe de deux charges $q$ en $0$ et $q'$ en $d$ ? Examiner $0 < x < d$ et $x>d$.",
          r"$V=k\left(\frac q{|x|}+\frac{q'}{|x-d|}\right)$. Il s'annule seulement si $q$ et $q'$ sont de signes opposés. Entre les charges : $\frac{|q|}x=\frac{|q'|}{d-x}$ donne $x=\frac{|q|d}{|q|+|q'|}$, toujours possible. Pour $x>d$ : $x=\frac{|q|d}{|q|-|q'|}$, possible seulement si $|q|>|q'|$.", src=T2 + ", ex. 2", duree=6),
        o("ew4", r"On ajoute une charge $Q$ au centre $O$ de la distribution du cercle ($V(O)=0$). Quelle est son énergie ? Interpréter si $qQ>0$ puis $qQ<0$.",
          r"$E=QV(O)=0$ : amener $Q$ en $O$ ne coûte et ne rapporte rien. Les répulsions et attractions des quatre charges se compensent pour le travail à fournir, mais la force sur $Q$ n'est pas nulle (le champ vaut $2\sqrt2\,kq/R^2$) : elle tend à écarter $Q$ de $O$ dans un sens ou dans l'autre selon son signe.", src=T2 + ", ex. 1", duree=6),
    ]},
    {"n": 9, "titre": "Charge totale d'une distribution", "notions": ["continu"], "exos": [
        v("ed1", r"Fil de longueur $L=2$ m, $\lambda=3$ C·m$^{-1}$. Charge totale (en C) ?", "3*2", "6", r"$Q=\lambda L=6$ C.", src=T4 + ", ex. 2", duree=1),
        v("ed2", r"Fil de longueur $L=2$ m sur l'axe $x$, $\lambda(x)=x$ C·m$^{-1}$. Charge totale (en C) ?", "Rational(1,2)*2**2", "2", r"$Q=\int_0^2x\,dx=\frac{2^2}2=2$ C.", src=T4 + ", ex. 2", duree=3),
        v("ed3", r"Anneau de rayon $R=0{,}5$ m, $\lambda=5\alpha$ C·m$^{-1}$ ($\alpha$ angle). Charge totale (en C) ?", "5*Rational(1,2)*2*pi**2", "5*pi**2",
          r"$dl=R\,d\alpha$ : $Q=\int_0^{2\pi}5\alpha R\,d\alpha=5R\frac{(2\pi)^2}2=5R\cdot2\pi^2=5\pi^2$ C.", src=T4 + ", ex. 2", duree=5),
        v("ed4", r"Carré de côté $L=3$ m, $\sigma=5$ C·m$^{-2}$. Charge totale (en C) ?", "5*3**2", "45", r"$Q=\sigma L^2=45$ C.", src=T4 + ", ex. 2", duree=2),
        v("ed5", r"Disque de rayon $R=2$ m, $\sigma=5\alpha$ C·m$^{-2}$. Charge totale (en C) ?", "Rational(1,2)*2**2*5*2*pi**2", "20*pi**2",
          r"$d^2S=r\,dr\,d\alpha$ : $Q=\int_0^R r\,dr\int_0^{2\pi}5\alpha\,d\alpha=\frac{R^2}2\times5\times2\pi^2=20\pi^2$ C.", src=T4 + ", ex. 2", duree=6),
        o("ed6", r"Donner l'élément $dl$ d'un segment et d'un anneau, puis $d^2S$ d'un carré et d'un disque, avec un schéma mental.",
          r"Segment : $dl=dx$. Anneau de rayon $R$ : $dl=R\,d\theta$ (arc d'angle $d\theta$). Carré : $d^2S=dx\,dy$. Disque : $d^2S=r\,dr\,d\theta$ (couronne d'épaisseur $dr$, longueur $r\,d\theta$).", src=T4 + ", ex. 1", duree=4),
    ]},
    {"n": 10, "titre": "Champ de quatre charges sur un axe", "notions": ["superposition", "symetrie"], "exos": [
        v("ea1", r"Quatre charges $q$ aux sommets d'un carré de côté $L$ ; sur l'axe, $E=\dfrac{4kqx}{(x^2+L^2/2)^{3/2}}$. Valeur en $x=0$ ?", "0", "0", r"Le numérateur contient $x$ : $E(0)=0$, ce qui rejoint l'argument de symétrie.", src=T3 + ", ex. 1", duree=1),
        v("ea2", r"Pour $x\gg L$ : $E\approx\dfrac{4kq}{x^2}$. Valeur (en V·m$^{-1}$) pour $q=1$ nC et $x=3$ m ?", "4*9*10**9*10**-9/9", "4", r"$E\approx\frac{4\times9}{9}=4$ V·m$^{-1}$ : de loin, les quatre charges se voient comme une charge $4q$.", src=T3 + ", ex. 1", duree=2),
        v("ea3", r"Le champ est maximal en $x=\frac L2$. Valeur (en V·m$^{-1}$) pour $q=1$ nC et $L=0{,}3$ m ?", "16*9*10**9*10**-9/(3*sqrt(3)*Rational(9,100))", "1600*sqrt(3)/9",
          r"$E_{max}=\frac{4kq\frac L2}{\left(\frac{L^2}4+\frac{L^2}2\right)^{3/2}}=\frac{16kq}{3\sqrt3L^2}=\frac{144}{0{,}27\sqrt3}\approx308$ V·m$^{-1}$.", src=T3 + ", ex. 1", duree=6),
        o("ea4", r"Établir $\vec E_{tot}(M)=\dfrac{4kqx}{(x^2+L^2/2)^{3/2}}\vec u_x$.",
          r"Chaque sommet est à la distance $AM=\sqrt{x^2+\frac{L^2}2}$ de $M$ (la demi-diagonale vaut $\frac L{\sqrt2}$). Par symétrie, les composantes perpendiculaires à l'axe s'annulent deux à deux ; chaque charge apporte $\frac{kq}{AM^2}\cos\alpha$ avec $\cos\alpha=\frac x{AM}$." "\n\n"
          r"Total : $E=4\frac{kq}{AM^2}\frac x{AM}=\dfrac{4kqx}{(x^2+L^2/2)^{3/2}}$.", src=T3 + ", ex. 1", duree=8),
        o("ea5", r"Décrire l'allure de $\|\vec E_{tot}\|$ en fonction de $x\geq0$.",
          r"Nulle en $x=0$, croissante jusqu'au maximum en $x=\frac L2$, puis décroissante en $\frac1{x^2}$ vers $0$ quand $x\to\infty$.", src=T3 + ", ex. 1", duree=3),
    ]},
    {"n": 11, "titre": "Force de Lorentz", "notions": ["lorentz"], "exos": [
        v("el1", r"$q=3{,}2\times10^{-19}$ C, $\vec v=(2,3,-1)$ m·s$^{-1}$, $\vec E=(4,-1,-2)$ V·m$^{-1}$, $\vec B=(2,2,1)$ T. Composante $F_x$ de la force de Lorentz (en $10^{-19}$ N) ?", "Rational(32,10)*9", "144/5",
          r"$\vec v\wedge\vec B=(3\cdot1-(-1)\cdot2,\ (-1)\cdot2-2\cdot1,\ 2\cdot2-3\cdot2)=(5,-4,-2)$. $\vec E+\vec v\wedge\vec B=(9,-5,-4)$, donc $F_x=3{,}2\times9=28{,}8$ ($\times10^{-19}$ N).", src=T5 + ", ex. 2 (valeurs lues sur scan)", duree=6),
        v("el2", r"$q=2\ \mu$C, $v=500$ m·s$^{-1}$ perpendiculaire à $B=0{,}2$ T. Norme de la force magnétique (en N) ?", "2*10**-6*500*Rational(2,10)", "1/5000", r"$F=|q|vB\sin90^\circ=2\times10^{-6}\times500\times0{,}2=2\times10^{-4}$ N.", duree=2),
        v("el3", r"Proton ($m=1{,}6\times10^{-27}$ kg, $q=1{,}6\times10^{-19}$ C) à $v=10^5$ m·s$^{-1}$ dans $B=0{,}5$ T perpendiculaire. Rayon de la trajectoire (en m) ?", "Rational(16,10)*10**-27*10**5/(Rational(16,10)*10**-19*Rational(1,2))", "1/500",
          r"$R=\frac{mv}{qB}=\frac{1{,}6\times10^{-22}}{8\times10^{-20}}=2\times10^{-3}$ m.", duree=3),
        o("el4", r"Pourquoi la force magnétique ne change-t-elle pas l'énergie cinétique d'une particule ?",
          r"$\vec F_{mag}=q\vec v\wedge\vec B$ est toujours perpendiculaire à $\vec v$, donc sa puissance $\vec F\cdot\vec v=0$ : elle ne travaille pas. Elle courbe la trajectoire mais $\|\vec v\|$ reste constante.", src="Cours, partie III.2", duree=3),
        o("el5", r"Particule de charge $q$, masse $m$, vitesse $\vec v\perp\vec B$ uniforme. Montrer que le mouvement est circulaire uniforme et que $R=\dfrac{mv}{|q|B}$.",
          r"PFD : $m\vec a=q\vec v\wedge\vec B$ donc $\vec a\perp\vec v$ : $a_T=\dot v=0$, $v$ constante, et $a=a_N=\frac{v^2}R$ avec $\|\vec a\|=\frac{|q|vB}m$ constante. La courbure est constante : cercle de rayon $R=\frac{mv^2}{|q|vB}=\frac{mv}{|q|B}$.", src=T5 + ", ex. 3", duree=7),
    ]},
    {"n": 12, "titre": "Spectromètre de masse", "notions": ["lorentz", "potentiel"], "exos": [
        v("sp1", r"Les ions ²³⁵U⁺ et ²³⁸U⁺ ont la même énergie cinétique à la sortie de l'accélération. Rapport $\dfrac{R_{238}}{R_{235}}$ des rayons dans $B$ (avec $R=\dfrac{\sqrt{2mqU}}{qB}$) ?", "sqrt(Rational(238,235))", "sqrt(Rational(238,235))",
          r"$R\propto\sqrt m$ à $U$, $q$, $B$ fixés : $\frac{R_{238}}{R_{235}}=\sqrt{\frac{238}{235}}\approx1{,}0064$.", src=T5 + ", ex. 3", duree=4),
        v("sp2", r"Le collecteur est à $D=940$ mm de $O_2$ : les ions ²³⁵U⁺ décrivent un demi-cercle. Rayon $R_{235}$ (en m) ?", "Rational(940,1000)/2", "47/100", r"$D=2R_{235}$ donc $R_{235}=0{,}47$ m.", src=T5 + ", ex. 3 q. 8", duree=2),
        v("sp3", r"Écart (en mm) entre les points d'impact des deux isotopes : $2(R_{238}-R_{235})$ avec $R_{235}=0{,}47$ m ?", "2*Rational(47,100)*(sqrt(Rational(238,235))-1)*1000", "940*(sqrt(Rational(238,235))-1)",
          r"$2\times0{,}47\times(1{,}0064-1)\approx5{,}97\times10^{-3}$ m, soit $\approx6{,}0$ mm. Supérieur à $L_0=4{,}0$ mm : la fente du collecteur peut isoler le ²³⁵U, la séparation isotopique est possible.", src=T5 + ", ex. 3 q. 9", duree=5),
        o("sp4", r"Sens de $\vec E_1$ dans la chambre d'accélération, puis expression de la vitesse $v$ en $G_2$.",
          r"Les ions positifs partent de $G_1$ (vitesse quasi nulle) vers $G_2$ : $\vec E_1$ est dirigé de $G_1$ vers $G_2$ (la force $q\vec E_1$ a le sens du champ pour $q>0$). Énergie : $\frac12mv^2=qU$ avec $U=V_{G_1}-V_{G_2}>0$, donc $v=\sqrt{\frac{2eU}m}$.", src=T5 + ", ex. 3 q. 1-3", duree=6),
        o("sp5", r"Ec $=15{,}0$ keV à la sortie. Déduire $U$ puis $v_{235}$ et $v_{238}$.",
          r"$E_c=eU$ avec $E_c=15{,}0$ keV donne $U=15{,}0$ kV. $v=\sqrt{\frac{2E_c}m}$ avec $E_c=15\times10^3\times1{,}60\times10^{-19}=2{,}40\times10^{-15}$ J : $m_{235}=235\times1{,}66\times10^{-27}$ kg donne $v_{235}\approx1{,}11\times10^5$ m·s$^{-1}$, et $v_{238}\approx1{,}10\times10^5$ m·s$^{-1}$.", src=T5 + ", ex. 3 q. 4", duree=7),
        o("sp6", r"Montrer que le mouvement dans la chambre de déviation est circulaire uniforme, exprimer $R_{235}$ puis la valeur de $B$ pour $D=940$ mm.",
          r"Voir niveau 11 : $R=\frac{mv}{eB}$ avec $v=\sqrt{\frac{2eU}m}$, soit $R_{235}=\frac1B\sqrt{\frac{2m_{235}U}e}$." "\n\n"
          r"$B=\frac1{R_{235}}\sqrt{\frac{2m_{235}U}e}$ avec $R_{235}=0{,}47$ m, $m_{235}=3{,}90\times10^{-25}$ kg, $U=15{,}0$ kV : $B\approx\frac{0{,}27}{0{,}47}\approx0{,}58$ T. Le sens de $\vec B$ est celui qui courbe $q\vec v\wedge\vec B$ vers le collecteur.", src=T5 + ", ex. 3 q. 5-8", duree=9),
    ]},
    {"n": 13, "titre": "Niveau examen : sujets complets", "notions": ["superposition", "potentiel", "energie", "continu", "lorentz"], "examen": True, "exos": [
        o("exa1", r"Quatre charges sur un cercle de rayon $R$ centré en $O$ : $A(-q)$ en haut, $B(-q)$ à droite, $C(+q)$ en bas, $D(+q)$ à gauche. 1. Tracer les champs en $O$. 2. Expressions et normes. 3. Champ résultant. 4. Force sur $Q$ en $O$. Puis $V(O)$ et l'énergie de $Q$.",
          r"Champs en $O$, tous de norme $\frac{kq}{R^2}$ : $\vec E_A=\frac{kq}{R^2}\vec u_y$ (charge négative : vers $A$), $\vec E_B=\frac{kq}{R^2}\vec u_x$, $\vec E_C=\frac{kq}{R^2}\vec u_y$ (charge positive : loin de $C$), $\vec E_D=\frac{kq}{R^2}\vec u_x$." "\n\n"
          r"Résultante : $\vec E=\frac{2kq}{R^2}(\vec u_x+\vec u_y)$, norme $\frac{2\sqrt2\,kq}{R^2}$. Force sur $Q$ : $\vec F=Q\vec E$, norme $\frac{2\sqrt2\,k|qQ|}{R^2}$." "\n\n"
          r"Potentiel : $V(O)=\frac kR(-q-q+q+q)=0$, donc $E_{pe}(Q)=QV(O)=0$.", src=T1 + ", ex. 1 et " + T2 + ", ex. 1", duree=12),
        o("exa2", r"$A(q)$ en $0$ et $B(q')$ en $d$ sur $Ox$, $M$ en $x>0$. 1. Schéma pour $q,q'>0$. 2. Champ de $q$. 3. Champ de $q'$ pour $x < d$ et $x>d$. 4. Le champ peut-il être nul ? Où ?",
          r"2. $\vec E_q=\frac{kq}{x^2}\vec u_x$." "\n\n"
          r"3. $x < d$ : $\vec E_{q'}=-\frac{kq'}{(d-x)^2}\vec u_x$ ; $x>d$ : $\vec E_{q'}=\frac{kq'}{(x-d)^2}\vec u_x$ (écrire $\frac{kq'}{(x-d)^2}\mathrm{sgn}(x-d)$ en général)." "\n\n"
          r"4. Même signe : seulement entre les charges, en $x$ tel que $\frac x{d-x}=\sqrt{\frac q{q'}}$, soit $x=\frac{d\sqrt q}{\sqrt q+\sqrt{q'}}$. Signes opposés : à l'extérieur du segment, près de la charge de plus petite valeur absolue.", src=T1 + ", ex. 2", duree=12),
        o("exa3", r"Quatre charges $q$ aux sommets d'un carré de côté $L$. 1. $\vec E(O)$. 2. Champ en $M(x)$ sur l'axe. 3. Maximum. 4. Cas $x\gg L$.",
          r"1. $\vec E(O)=\vec0$ (symétrie). 2. $\vec E=\frac{4kqx}{(x^2+L^2/2)^{3/2}}\vec u_x$ (niveau 10). 3. $\frac{dE}{dx}=0$ donne $x^2+\frac{L^2}2=3x^2$, soit $x=\frac L2$, et $E_{max}=\frac{16kq}{3\sqrt3L^2}$. 4. $E\approx\frac{4kq}{x^2}$ : champ d'une charge $4q$.", src=T3 + ", ex. 1", duree=12),
        o("exa4", r"Calculer la charge totale de : un fil de longueur $L$ avec $\lambda=x$ ; un anneau de rayon $R$ avec $\lambda=5\alpha$ ; un rectangle $l\times L$ avec $\sigma=5$ ; un disque de rayon $R$ avec $\sigma=5\alpha$.",
          r"Fil : $\int_0^Lx\,dx=\frac{L^2}2$. Anneau : $\int_0^{2\pi}5\alpha R\,d\alpha=10\pi^2R$. Rectangle : $5lL$. Disque : $\int_0^Rr\,dr\int_0^{2\pi}5\alpha\,d\alpha=5\pi^2R^2$.", src=T4 + ", ex. 2", duree=10),
        o("exa5", r"Spectromètre de masse : accélération sous $U$, déviation dans $B$ uniforme. Établir $v$, $R$ en fonction de $m$, $e$, $U$, $B$, puis dire si l'on sépare ²³⁵U⁺ de ²³⁸U⁺ avec une fente de $4{,}0$ mm quand $D=940$ mm.",
          r"$v=\sqrt{\frac{2eU}m}$ ; $R=\frac{mv}{eB}=\frac1B\sqrt{\frac{2mU}e}$ ; $D=2R$. $R_{235}=0{,}47$ m et $R_{238}=R_{235}\sqrt{\frac{238}{235}}$, écart des points d'impact $\approx6{,}0$ mm $>4{,}0$ mm : la séparation est possible.", src=T5 + ", ex. 3", duree=12),
    ]},
    {"n": 14, "titre": "Examen + 20 %", "notions": ["energie", "potentiel", "lorentz"], "examen": True, "exos": [
        v("exb1", r"Trois charges $q$, $q$, $q$ aux sommets d'un triangle équilatéral de côté $a$, $q=1$ nC, $a=0{,}1$ m. Énergie d'assemblage (en J) ?", "3*9*10**9*10**-18/Rational(1,10)", "27/10**8",
          r"Trois paires, chacune $\frac{kq^2}a$ : $3\times\frac{9\times10^9\times10^{-18}}{0{,}1}=2{,}7\times10^{-7}$ J.", duree=5),
        v("exb2", r"Un électron ($q=-1{,}6\times10^{-19}$ C) est accéléré depuis le repos sous $U=1000$ V. Énergie cinétique (en eV) ?", "1000", "1000", r"$E_c=|q|U=1000$ eV.", duree=2),
        o("exb3", r"Deux charges $+q$ et $-q$ en $(-a,0)$ et $(a,0)$. Calculer $V$ sur la médiatrice, puis $\vec E$ en $O$ à partir du gradient.",
          r"Sur la médiatrice $x=0$ : $V=k\left(\frac q{\sqrt{a^2+y^2}}-\frac q{\sqrt{a^2+y^2}}\right)=0$ : c'est une équipotentielle (plan d'antisymétrie), le champ lui est perpendiculaire donc selon $\vec u_x$. En $O$, chaque charge crée $\frac{kq}{a^2}\vec u_x$ (répulsion de $+q$, attraction par $-q$) : $\vec E(O)=\frac{2kq}{a^2}\vec u_x$.", duree=8),
        o("exb4", r"Une particule de charge $q$ et masse $m$ entre dans une zone de champ $\vec B$ uniforme avec une vitesse $\vec v_0$ qui fait un angle $\alpha$ avec $\vec B$. Décrire la trajectoire.",
          r"On décompose $\vec v_0=\vec v_\parallel+\vec v_\perp$. Selon $\vec B$, la force est nulle : mouvement uniforme à $v_\parallel=v_0\cos\alpha$. Perpendiculairement, mouvement circulaire uniforme de rayon $R=\frac{mv_0\sin\alpha}{|q|B}$. Composition : une hélice d'axe parallèle à $\vec B$.", duree=8),
    ]},
]


def _v(enonce, calc, ans, sol):
    return {"enonce": enonce, "calc": calc, "ans": ans, "sol": sol}


VARIANTS = {
    "ec1": [_v(r"Deux charges de $2\ \mu$C à $6$ cm. Force (en N) ?", "9*10**9*4*10**-12/(Rational(6,100))**2", "10", r"$\frac{9\times10^9\times4\times10^{-12}}{3{,}6\times10^{-3}}=10$ N.")],
    "ee1": [_v(r"Champ (en V·m$^{-1}$) créé par $q=4$ nC à $0{,}6$ m ?", "9*10**9*4*10**-9/Rational(36,100)", "100", r"$\frac{36}{0{,}36}=100$.")],
    "ee2": [_v(r"Force (en N) sur $Q=2\ \mu$C dans un champ de $500$ V·m$^{-1}$ ?", "2*10**-6*500", "1/1000", r"$QE=10^{-3}$ N.")],
    "es1": [_v(r"Charges $+1$ nC et $-1$ nC distantes de $0{,}6$ m. Champ (en V·m$^{-1}$) au milieu ?", "2*9*10**9*10**-9/Rational(9,100)", "200", r"$2\frac{kq}{r^2}$ avec $r=0{,}3$ : $\frac{18}{0{,}09}=200$.")],
    "ex1": [_v(r"Mêmes charges ($1$ nC), $d=0{,}6$ m, point en $x=0{,}2$ m. Champ (en V·m$^{-1}$) ?", "9*(1/Rational(4,100)-1/Rational(16,100))", "675/4", r"$\frac9{0{,}04}-\frac9{0{,}16}=225-56{,}25=168{,}75$ V·m$^{-1}$.")],
    "en1": [_v(r"$q=1$ nC et $q'=4$ nC à $4$ cm. Énergie (en J) ?", "9*10**9*4*10**-18/Rational(4,100)", "9/10**7", r"$\frac{9\times10^9\times4\times10^{-18}}{0{,}04}=9\times10^{-7}$ J.")],
    "ep1": [_v(r"Potentiel (en V) à $0{,}6$ m d'une charge $q=4$ nC ?", "9*10**9*4*10**-9/Rational(6,10)", "60", r"$\frac{36}{0{,}6}=60$ V.")],
    "ed1": [_v(r"Fil de longueur $4$ m, $\lambda=2{,}5$ C·m$^{-1}$. Charge totale (en C) ?", "Rational(5,2)*4", "10", r"$\lambda L=10$ C.")],
    "ed4": [_v(r"Rectangle $2\times5$ m, $\sigma=3$ C·m$^{-2}$. Charge totale (en C) ?", "3*2*5", "30", r"$\sigma lL=30$ C.")],
    "el2": [_v(r"$q=1\ \mu$C, $v=200$ m·s$^{-1}$ perpendiculaire à $B=0{,}5$ T. Force (en N) ?", "10**-6*200*Rational(1,2)", "1/10000", r"$qvB=10^{-4}$ N.")],
}
for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["id"] in VARIANTS:
            _e["variants"] = VARIANTS[_e["id"]]


EXTRA_PARTS = []

QUIZ = [
    {"notion": "coulomb", "type": "qcm", "q": r"Quand on double la distance entre deux charges, la force est :", "choix": [r"divisée par $4$", r"divisée par $2$", r"multipliée par $2$", r"inchangée"], "bonne": 0},
    {"notion": "coulomb", "type": "vf", "q": r"Deux charges de signes opposés se repoussent.", "bonne": False},
    {"notion": "champ", "type": "qcm", "q": r"Le champ créé par une charge négative est :", "choix": [r"radial rentrant", r"radial sortant", r"nul", r"orthoradial"], "bonne": 0},
    {"notion": "champ", "type": "vf", "q": r"Une charge est soumise au champ qu'elle crée elle-même.", "bonne": False},
    {"notion": "superposition", "type": "qcm", "q": r"Le champ de plusieurs charges est :", "choix": [r"la somme vectorielle des champs de chacune", r"la somme des normes", r"le champ de la plus grande charge", r"le produit des champs"], "bonne": 0},
    {"notion": "symetrie", "type": "qcm", "q": r"En un point d'un plan d'antisymétrie, le champ est :", "choix": [r"perpendiculaire au plan", r"contenu dans le plan", r"nul", r"indéterminé"], "bonne": 0},
    {"notion": "symetrie", "type": "vf", "q": r"Quatre charges identiques aux sommets d'un carré créent un champ nul au centre.", "bonne": True},
    {"notion": "energie", "type": "qcm", "q": r"L'énergie électrostatique de deux charges varie comme :", "choix": [r"$\frac1r$", r"$\frac1{r^2}$", r"$r$", r"$r^2$"], "bonne": 0},
    {"notion": "energie", "type": "vf", "q": r"Deux charges de même signe ont une énergie électrostatique positive.", "bonne": True},
    {"notion": "potentiel", "type": "qcm", "q": r"Le potentiel créé par plusieurs charges ponctuelles est :", "choix": [r"la somme algébrique des $k\frac{q_i}{r_i}$", r"une somme vectorielle", r"le produit des $k\frac{q_i}{r_i}$", r"toujours positif"], "bonne": 0},
    {"notion": "potentiel", "type": "qcm", "q": r"Le champ se déduit du potentiel par :", "choix": [r"$\vec E=-\overrightarrow{\mathrm{grad}}\,V$", r"$\vec E=\overrightarrow{\mathrm{grad}}\,V$", r"$\vec E=V\vec u_r$", r"$\vec E=\frac Vr$ en toutes circonstances"], "bonne": 0},
    {"notion": "continu", "type": "qcm", "q": r"Pour un anneau de rayon $R$, l'élément de longueur est :", "choix": [r"$R\,d\theta$", r"$d\theta$", r"$R^2d\theta$", r"$dr$"], "bonne": 0},
    {"notion": "continu", "type": "qcm", "q": r"Pour un disque, l'élément de surface est :", "choix": [r"$r\,dr\,d\theta$", r"$dr\,d\theta$", r"$dx\,dy\,dz$", r"$R\,d\theta$"], "bonne": 0},
    {"notion": "lorentz", "type": "qcm", "q": r"La force de Lorentz s'écrit :", "choix": [r"$q\vec E+q\vec v\wedge\vec B$", r"$q\vec E+q\vec v\cdot\vec B$", r"$q\vec v\wedge\vec E$", r"$q\vec B$"], "bonne": 0},
    {"notion": "lorentz", "type": "vf", "q": r"La force magnétique modifie l'énergie cinétique de la particule.", "bonne": False},
    {"notion": "lorentz", "type": "qcm", "q": r"Dans un champ $\vec B$ uniforme perpendiculaire à $\vec v$, la trajectoire est :", "choix": [r"un cercle parcouru à vitesse constante", r"une droite", r"une parabole", r"une spirale qui s'élargit"], "bonne": 0},
]

_COU = r"$F=k\frac{q_1q_2}{r^2}$, $k=9\times10^9$"
_E = r"$E=k\frac{q}{r^2}$ · $\vec F=q\vec E$"
_SUP = r"$\vec E_{tot}=\sum\vec E_i$ (somme vectorielle)"
_SYM = r"plan de symétrie : $\vec E\in\Pi$ · antisymétrie : $\vec E\perp\Pi^*$"
_EN = r"$E_{pe}=k\frac{qq'}r$ (somme sur les paires)"
_V = r"$V=k\frac qr$ (scalaire, somme algébrique)"
_GR = r"$\vec E=-\overrightarrow{\mathrm{grad}}V$"
_CON = r"$Q=\int\lambda\,dl$ · $Q=\iint\sigma\,dS$ · $dl=R\,d\theta$ · $d^2S=r\,dr\,d\theta$"
_LOR = r"$\vec F=q\vec E+q\vec v\wedge\vec B$ · $\vec F_{mag}\perp\vec v$"
_RAY = r"$R=\frac{mv}{|q|B}$ · $\frac12mv^2=qU$"

FORMULES = {
    "ec1": _COU, "ec2": _COU, "ec3": _COU, "ec4": _COU + r" · $F=G\frac{m_1m_2}{r^2}$", "ec5": _COU + r" · $F=G\frac{m_1m_2}{r^2}$",
    "ee1": _E, "ee2": _E, "ee3": _E, "ee4": _E + r" · $d\vec l\wedge\vec E=\vec0$",
    "es1": _E + " · " + _SUP, "es2": _E + " · " + _SUP, "es3": _E, "es4": _SUP + r" · $\sin60^\circ=\frac{\sqrt3}2$", "es5": _SUP,
    "esy1": _SYM, "esy2": _SYM, "esy3": _SYM + " · " + _SUP,
    "ex1": _E + " · " + _SUP, "ex2": _E + " · " + _SUP, "ex3": _E + r" · $\frac x{d-x}=\sqrt{\frac q{q'}}$", "ex4": _E + " · " + _SUP,
    "en1": _EN, "en2": _EN, "en3": _EN, "en4": _EN,
    "ep1": _V, "ep2": _GR + r" · $E=\frac Vr$", "ep3": _V, "ep4": _V, "ep5": _GR + r" · $\overrightarrow{\mathrm{grad}}f=\sum\frac{\partial f}{\partial x_i}\vec u_i$",
    "ew1": _EN, "ew2": _EN + r" · distance diagonale $\sqrt{a^2+b^2}$", "ew3": _V, "ew4": r"$E=QV$ · " + _V,
    "ed1": _CON, "ed2": _CON + r" · $\int x\,dx=\frac{x^2}2$", "ed3": _CON, "ed4": _CON, "ed5": _CON, "ed6": _CON,
    "ea1": _SYM, "ea2": r"$E\approx\frac{4kq}{x^2}$ pour $x\gg L$", "ea3": r"$E=\frac{4kqx}{(x^2+L^2/2)^{3/2}}$ · $E'=0\Rightarrow x=\frac L2$", "ea4": _SUP + r" · $\cos\alpha=\frac xr$", "ea5": r"$E=\frac{4kqx}{(x^2+L^2/2)^{3/2}}$",
    "el1": _LOR + r" · produit vectoriel par déterminant", "el2": _LOR + r" · $F=|q|vB\sin\theta$", "el3": _RAY, "el4": _LOR + r" · $P=\vec F\cdot\vec v=0$", "el5": _LOR + " · " + _RAY + r" · $a_N=\frac{v^2}R$",
    "sp1": _RAY + r" · $R\propto\sqrt m$", "sp2": r"demi-cercle : $D=2R$", "sp3": _RAY, "sp4": r"$\frac12mv^2=qU$", "sp5": r"$E_c=eU$ · $v=\sqrt{\frac{2E_c}m}$", "sp6": _RAY + r" · $B=\frac1R\sqrt{\frac{2mU}e}$",
    "exa1": _E + " · " + _SUP + " · " + _V + r" · $E=QV$", "exa2": _E + " · " + _SUP, "exa3": r"$E=\frac{4kqx}{(x^2+L^2/2)^{3/2}}$ · " + _SYM,
    "exa4": _CON, "exa5": _RAY + r" · $\frac12mv^2=qU$",
    "exb1": _EN, "exb2": r"$E_c=|q|U$ (eV)", "exb3": _V + " · " + _SYM + " · " + _SUP, "exb4": _LOR + " · " + _RAY,
}
