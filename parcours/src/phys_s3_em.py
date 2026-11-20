"""Level path: S3 physics, ECUE EM2 (Électromagnétisme II : symétries, théorème de Gauss, ondes électromagnétiques).

Moodle course « Électrostatique et Magnétostatique, ondes électromagnétiques » : chapitres 01_Cours et TD (Cours_EM2 du 15/09/2026,
TD1 à TD5, fiche de coordonnées), 02_TD Corrigé (corrigés des TD1 à TD5), 05_QCM (QCM 1 et 2). Le cours actuel traite : symétries
et invariances, flux, théorème de Gauss (fil, plan, sphère), puis le modèle de l'onde plane progressive monochromatique. La
magnétostatique (Biot-Savart, Ampère, induction) n'est pas dans le cours Moodle actuel : elle n'est pas dans ce parcours.
Calibrated on the transcribed EPITA S3 physics exams (annales/raw/S3/Midterms/Phys and Finals/Phys) :
Examen Physique Électromagnétisme octobre 2024 (dossier promo 2028, sujet seul), partiel de physique décembre 2021 et contrôle
de novembre 2021 (dossiers 2025, sujets seuls), partiel 1 de décembre 2017 (dossier 2021, corrigé manuscrit), partiel (dossier 2024,
copie corrigée à la main), contrôle d'octobre 2016 (dossier 2020).
Levels 1 to 5 are reminders of S1 (vecteurs, intégrales) and S2 (parcours `physique-s2-em` : Coulomb, champ, potentiel, énergie,
force de Lorentz). `value` exercises are checked by build.py (sympy) ; k = 9×10^9 SI, donc ε0 = 1/(4πk) ; `open` exercises carry a
full model answer. No official correction exists for the exam subjects : solutions are « corrigé rédigé », checked with sympy.
"""

SUBJECT = {
    "id": "physique-s3-em",
    "ordre": 345,
    "matiere": "physique",
    "semestre": "S3",
    "ecue": "EM2",
    "titre": "Électromagnétisme II : théorème de Gauss et ondes",
    "chapitres_moodle": ["01_Cours et TD", "02_TD Corrigé", "05_QCM"],
    "td": "TD1 à TD5 EM2 (S3 2026)",
    "examens": ["Examen B5 Électromagnétisme (octobre)", "Partiel de physique S3 (décembre)"],
}

NOTIONS = [
    {"id": "vect", "titre": "Vecteurs, produit scalaire et vectoriel (rappel S1)",
     "formule": r"$\|\vec u\|=\sqrt{u_x^2+u_y^2+u_z^2}$ · $\vec u\cdot\vec v=u_xv_x+u_yv_y+u_zv_z=\|\vec u\|\|\vec v\|\cos\theta$ · $\vec u\wedge\vec v=(u_yv_z-u_zv_y,\ u_zv_x-u_xv_z,\ u_xv_y-u_yv_x)$",
     "exemple": r"$\vec E$ de norme $10$ incliné de $60^\circ$ sur $\vec u_x$ : $E_x=\vec E\cdot\vec u_x=10\cos60^\circ=5$",
     "cours": r"Le produit scalaire sert à projeter un vecteur sur un axe (composante) et à calculer un flux ; le produit vectoriel donne la direction de la force de Lorentz $q\vec v\wedge\vec B$ (perpendiculaire aux deux vecteurs, sens de la règle de la main droite). Rappel S1 : parcours de mécanique (`physique-s1-meca`)."},
    {"id": "integ", "titre": "Intégrales et éléments d'intégration (rappel S1/S2)",
     "formule": r"$dl=dx$ · $dl=R\,d\theta$ (anneau) · $d^2S=dx\,dy$ · $d^2S=r\,dr\,d\theta$ (disque) · $d\tau=r\,dr\,d\theta\,dz$ (cylindre) · $d\tau=r^2\sin\theta\,dr\,d\theta\,d\varphi$ (sphère) · $Q=\int\lambda\,dl=\iint\sigma\,dS=\iiint\rho\,d\tau$",
     "exemple": r"volume de la sphère : $\int_0^R r^2dr\int_0^\pi\sin\theta\,d\theta\int_0^{2\pi}d\varphi=\frac{R^3}3\times2\times2\pi=\frac43\pi R^3$",
     "cours": r"Choisir les coordonnées adaptées à la géométrie (voir la fiche de coordonnées du cours), écrire la charge élémentaire $dQ=\rho\,d\tau$ puis intégrer sur le domaine. Si la densité dépend de $r$, elle reste sous l'intégrale. Rappel : parcours d'intégrales de S1 (`maths-s1-apis-integrales`) et TD1 ex. 2-3, TD5 ex. 1."},
    {"id": "coulomb", "titre": "Coulomb, champ et superposition (rappel S2)",
     "formule": r"$F=k\frac{|q_1q_2|}{r^2}$ · $\vec E=k\frac q{r^2}\vec u_r$ · $\vec F=q\vec E$ · $\vec E_{tot}=\sum\vec E_i$ · $k=\frac1{4\pi\varepsilon_0}\approx9\times10^9$",
     "exemple": r"$q=1$ nC à $0{,}3$ m : $E=\frac{9\times10^9\times10^{-9}}{0{,}09}=100$ V·m$^{-1}$",
     "cours": r"Le champ d'une charge ponctuelle est radial, sortant si $q>0$, rentrant si $q<0$. Pour plusieurs charges : un champ par charge, projection sur les axes, somme des composantes (jamais la somme des normes). Rappel S2 : parcours `physique-s2-em`."},
    {"id": "potentiel", "titre": "Potentiel et énergie (rappel S2)",
     "formule": r"$V=k\frac qr$ (scalaire : somme algébrique) · $E_p=qV$ · $E_{pe}=\sum_{paires}k\frac{q_iq_j}{r_{ij}}$ · $\vec E=-\overrightarrow{\mathrm{grad}}\,V$ · $V_B-V_A=-\int_A^B\vec E\cdot d\vec l$",
     "exemple": r"$V=ar\,e^{-b/r}$ : $E_r=-\frac{dV}{dr}=-ae^{-b/r}\left(1+\frac br\right)$",
     "cours": r"Le potentiel s'additionne sans projection. En un seul paramètre $r$, $E_r=-\frac{dV}{dr}$ ; inversement $V(r)=-\int E\,dr+\text{cste}$ : la constante se fixe par une référence (par exemple $V(\infty)=0$) ou par la continuité de $V$. Gradient en cylindriques : $\left(\frac\partial{\partial r},\frac1r\frac\partial{\partial\theta},\frac\partial{\partial z}\right)$ ; en sphériques : $\left(\frac\partial{\partial r},\frac1r\frac\partial{\partial\theta},\frac1{r\sin\theta}\frac\partial{\partial\varphi}\right)$."},
    {"id": "lorentz", "titre": "Force de Lorentz et spectromètre de masse (rappel S2)",
     "formule": r"$\vec F=q\vec E+q\vec v\wedge\vec B$ · $\frac12mv^2=qU$ · $R=\frac{mv}{|q|B}$ (cercle) · $\vec F_{mag}\perp\vec v$ : elle ne travaille pas",
     "exemple": r"proton ($m=1{,}6\times10^{-27}$ kg), $v=10^5$ m·s$^{-1}$, $B=0{,}5$ T : $R=2$ mm",
     "cours": r"Dans une cavité d'accélération, seul $\vec E$ agit : $E_c=qU$. Dans la zone de séparation, $\vec B$ perpendiculaire à $\vec v$ donne un mouvement circulaire uniforme d'accélération $-\frac{v^2}R\vec e_r$, d'où $R=\frac{mv}{|q|B}$ : à $v$ et $B$ fixés, $R\propto m$, ce qui sépare les isotopes (Examen octobre 2024)."},
    {"id": "oem", "titre": "Onde plane progressive monochromatique",
     "formule": r"$\vec E=\vec E_0\cos(\omega t-kx)$ · $c=\lambda f=\frac\omega k$ · $k=\frac{2\pi}\lambda$ · $\omega=2\pi f$ · $T=\frac1f$ · $B_0=\frac{E_0}c$ · $\frac{\partial^2E}{\partial x^2}=\frac1{c^2}\frac{\partial^2E}{\partial t^2}$",
     "exemple": r"$f=100$ MHz : $\lambda=\frac{3\times10^8}{10^8}=3$ m",
     "cours": r"Une onde polarisée rectilignement qui se propage selon $x$ avec $\vec E$ selon $y$ et $\vec B$ selon $z$ obéit à $\frac{\partial E}{\partial x}=-\frac{\partial B}{\partial t}$ et $\frac{\partial B}{\partial x}=-\frac1{c^2}\frac{\partial E}{\partial t}$ ; on en déduit l'équation d'onde. $\vec E\perp\vec B$, $(\vec E,\vec B,\vec u_x)$ direct. Dans le vide, la célérité est celle de la lumière, $c=3\times10^8$ m·s$^{-1}$ ; $\lambda$ en m, $f$ en Hz, $\omega$ en rad·s$^{-1}$."},
    {"id": "symetrie", "titre": "Principe de Curie, symétries et invariances",
     "formule": r"plan de symétrie $\Pi$ : $\vec E(M)\in\Pi$ · plan d'antisymétrie $\Pi^*$ : $\vec E(M)\perp\Pi^*$ · invariance par translation selon $z$ : $\vec E$ ne dépend pas de $z$ · invariance par rotation d'angle $\theta$ : pas de dépendance en $\theta$",
     "exemple": r"fil infini : deux plans de symétrie $(M,\vec u_r,\vec u_z)$ et $(M,\vec u_r,\vec u_\theta)$ donnent $E_\theta=E_z=0$ ; les invariances donnent $\vec E=E_r(r)\vec u_r$",
     "cours": r"Les éléments de symétrie des causes (la distribution de charges) se retrouvent dans les effets (le champ). Méthode : lister les plans de symétrie qui passent par $M$ (le champ est dans leur intersection), puis les invariances (le champ ne dépend pas de ces coordonnées). On passe de trois composantes dépendant de trois variables à une seule composante dépendant d'une seule variable."},
    {"id": "flux", "titre": "Flux d'un champ à travers une surface",
     "formule": r"$\Phi=\iint_S\vec F\cdot d\vec S$ · champ uniforme, surface plane : $\Phi=FS\cos\alpha$ · sphère de rayon $r$, champ radial : $\Phi=E(r)\,4\pi r^2$ · cylindre latéral : $\Phi=E(r)\,2\pi rh$",
     "exemple": r"$E=200$ V·m$^{-1}$ à $60^\circ$ de la normale d'un disque de rayon $0{,}1$ m : $\Phi=200\times\pi\times0{,}01\times\frac12=\pi$ V·m",
     "cours": r"Le flux est un scalaire proportionnel à la densité du champ, à l'aire et à l'orientation de la surface. $d\vec S$ est orienté vers l'extérieur d'une surface fermée. Sur les faces où $\vec E\perp d\vec S$ le flux est nul ; sur celles où $\vec E\parallel d\vec S$ avec $E$ constant, $\Phi=\pm E\,S$."},
    {"id": "gauss", "titre": "Théorème de Gauss",
     "formule": r"$\oiint_{S_G}\vec E\cdot d\vec S=\frac{Q_{int}}{\varepsilon_0}$ · $\varepsilon_0=\frac1{4\pi k}\approx8{,}85\times10^{-12}$ F·m$^{-1}$",
     "exemple": r"charge ponctuelle : sphère de rayon $r$, $E\,4\pi r^2=\frac q{\varepsilon_0}$, donc $E=\frac q{4\pi\varepsilon_0r^2}=k\frac q{r^2}$ (on retrouve Coulomb)",
     "cours": r"Méthode en sept étapes : (1) système de coordonnées, (2) symétries, (3) invariances, (4) surface de Gauss fermée passant par $M$, (5) flux, (6) charge intérieure $Q_{int}$ (intégrale de la densité), (7) conclusion. Toutes les charges créent le champ, mais seules celles à l'intérieur de la surface de Gauss comptent dans $Q_{int}$ : le flux ne voit que l'intérieur."},
    {"id": "gauss-cyl", "titre": "Gauss : fil et cylindre infinis",
     "formule": r"fil : $\vec E=\frac\lambda{2\pi\varepsilon_0r}\vec u_r$ · cylindre plein ($\rho$) : $E=\frac{\rho r}{2\varepsilon_0}$ ($r < R$), $E=\frac{\rho R^2}{2\varepsilon_0r}$ ($r > R$) · cylindre creux ($\sigma$) : $E=0$ ($r < a$), $E=\frac{\sigma a}{\varepsilon_0r}$ ($r > a$)",
     "exemple": r"fil de $\lambda=1$ nC·m$^{-1}$ à $0{,}2$ m : $E=\frac{2k\lambda}r=\frac{18}{0{,}2}=90$ V·m$^{-1}$",
     "cours": r"Coordonnées cylindriques, $\vec E=E_r(r)\vec u_r$. Surface de Gauss : cylindre fermé de rayon $r$ et de hauteur $h$ ; le flux traverse la surface latérale seule : $\Phi=E_r\,2\pi rh$. Charge intérieure : $\lambda h$ pour un fil, $\iiint\rho\,r\,dr\,d\theta\,dz$ pour une densité volumique (limite à $R$ si $r > R$). Le champ est discontinu de $\frac\sigma{\varepsilon_0}$ à la traversée d'une nappe chargée en surface."},
    {"id": "gauss-plan", "titre": "Gauss : plan infini et condensateur plan",
     "formule": r"plan : $\vec E=\pm\frac\sigma{2\varepsilon_0}\vec u_z$ · deux plans $\pm\sigma$ : $E=\frac\sigma{\varepsilon_0}$ entre eux, $0$ dehors · $U=Ee=\frac{\sigma e}{\varepsilon_0}$ · $C=\frac QU=\frac{\varepsilon_0S}e$",
     "exemple": r"$S=1$ m$^2$, $e=1$ mm : $C=\frac{\varepsilon_0S}e\approx8{,}85$ nF",
     "cours": r"Coordonnées cartésiennes, $\vec E=E_z(z)\vec u_z$, impair en $z$. Surface de Gauss : cylindre fermé de section $S$ traversant le plan : deux bases de flux $E_zS$ chacune, d'où $2E_zS=\frac{\sigma S}{\varepsilon_0}$. Deux plans $\pm\sigma$ : superposition. $E=-\frac{dV}{dz}$ donne $U=Ee$. Pour augmenter $C$ à encombrement donné : réduire $e$ (limité par la tension de claquage, environ $32$ kV·cm$^{-1}$ dans l'air)."},
    {"id": "gauss-sph", "titre": "Gauss : sphère chargée",
     "formule": r"sphère pleine ($\rho_0$) : $E=\frac{\rho_0r}{3\varepsilon_0}$ ($r < R$), $E=\frac{\rho_0R^3}{3\varepsilon_0r^2}$ ($r > R$) · sphère creuse ($\sigma$) : $E=0$ puis $\frac{\sigma R^2}{\varepsilon_0r^2}$ · flux : $E\,4\pi r^2$",
     "exemple": r"$\rho(r)=\rho_0\frac{r^2}{R^2}$ : $Q_{int}=\frac{4\pi\rho_0r^5}{5R^2}$, d'où $E=\frac{\rho_0r^3}{5\varepsilon_0R^2}$ ($r < R$)",
     "cours": r"Coordonnées sphériques : tout plan contenant $OM$ est plan de symétrie, donc $\vec E=E_r(r)\vec u_r$. Surface de Gauss : sphère de rayon $r$ passant par $M$ ; $Q_{int}=\int_0^r\rho(s)\,4\pi s^2\,ds$. À l'extérieur, la sphère se comporte comme une charge ponctuelle $Q_{tot}$ placée en $O$. Si $\rho$ varie, vérifier la continuité de $E$ en $r=R$ (il n'y a de saut que s'il existe une charge surfacique)."},
    {"id": "anneau", "titre": "Distribution continue sans Gauss : l'anneau",
     "formule": r"$E_z=\frac{2\pi k\lambda Rz}{(R^2+z^2)^{3/2}}$ · $V=\frac{2\pi k\lambda R}{\sqrt{R^2+z^2}}$ · $E_z=-\frac{dV}{dz}$ · loin : $E\approx\frac{kQ}{z^2}$ avec $Q=2\pi R\lambda$",
     "exemple": r"carré de côté $L$, charge $q$ à chaque sommet, sur l'axe : $E=\frac{4kqx}{(x^2+L^2/2)^{3/2}}$, maximal en $x=\frac L2$",
     "cours": r"Quand il n'y a pas assez de symétries pour Gauss (anneau, disque), on revient à Coulomb : par symétrie le champ est sur l'axe, on projette $dE_z=dE\cos\alpha$ avec $\cos\alpha=\frac z{\sqrt{R^2+z^2}}$, puis on intègre sur $\theta$ de $0$ à $2\pi$ avec $dQ=\lambda R\,d\theta$ (TD2). Contrôles de cohérence : analyse dimensionnelle, comportement quand $z$ varie, et $E\to\frac{kQ}{z^2}$ quand $z\gg R$."},
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


OCT24 = "Examen Physique Électromagnétisme octobre 2024 (dossier promo 2028)"
DEC21 = "Partiel de physique décembre 2021 (dossier 2025)"
NOV21 = "Contrôle de physique novembre 2021 (dossier 2025)"
DEC17 = "Partiel 1 de physique décembre 2017 (dossier 2021)"
P24 = "Partiel de physique (dossier 2024)"
OCT16 = "Contrôle 1 de physique octobre 2016 (dossier 2020)"
T1 = "TD1 EM2"
T2 = "TD2 EM2"
T3 = "TD3 EM2"
T4 = "TD4 EM2"
T5 = "TD5 EM2"

LEVELS = [
    {"n": 1, "titre": "Rappel S1 : vecteurs et projections", "notions": ["vect"], "exos": [
        v("vc1", r"Norme du vecteur $\vec u=(3,4,0)$ ?", "sqrt(3**2+4**2)", "5", r"$\|\vec u\|=\sqrt{3^2+4^2+0^2}=5$.", duree=1),
        v("vc2", r"Produit scalaire de $\vec u=(1,2,3)$ et $\vec v=(4,-1,2)$ ?", "1*4+2*(-1)+3*2", "8", r"$\vec u\cdot\vec v=1\times4+2\times(-1)+3\times2=4-2+6=8$.", duree=1),
        v("vc3", r"Composante selon $\vec u_z$ du produit vectoriel $\vec u\wedge\vec v$ avec $\vec u=(2,1,0)$ et $\vec v=(1,3,0)$ ?", "Matrix([2,1,0]).cross(Matrix([1,3,0]))[2]", "5",
          r"$(\vec u\wedge\vec v)_z=u_xv_y-u_yv_x=2\times3-1\times1=5$.", duree=2),
        v("vc4", r"Un champ de norme $10$ V·m$^{-1}$ fait un angle de $60^\circ$ avec l'axe $Ox$. Sa composante selon $Ox$ ?", "10*cos(pi/3)", "5", r"$E_x=\vec E\cdot\vec u_x=E\cos60^\circ=10\times\frac12=5$ V·m$^{-1}$.", duree=1),
        v("vc5", r"Deux champs de norme $E=10$ V·m$^{-1}$ font chacun un angle de $60^\circ$ avec l'axe $Ox$, l'un au-dessus et l'autre au-dessous. Norme de leur somme (en V·m$^{-1}$) ?", "2*10*cos(pi/3)", "10",
          r"Les composantes sur $Oy$ s'annulent, celles sur $Ox$ s'ajoutent : $2E\cos60^\circ=2\times10\times\frac12=10$.", src="Cours, partie I.2 (projection) ; TD1 ex. 1", duree=2),
    ]},
    {"n": 2, "titre": "Rappel S1/S2 : intégrales et éléments d'intégration", "notions": ["integ"], "exos": [
        v("in1", r"Fil de longueur $L=3$ m sur l'axe $Ox$, de densité linéique $\lambda=x$ (C·m$^{-1}$). Charge totale ?", "integrate(x,(x,0,3))", "9/2", r"$Q=\int_0^3x\,dx=\frac{3^2}2=\frac92$ C.", src=T1 + ", ex. 3", duree=2),
        v("in2", r"Anneau de rayon $R=2$ m, de densité linéique $\lambda=5\alpha$ (avec $\alpha\in[0,2\pi]$ l'angle). Charge totale ?", "integrate(5*x*2,(x,0,2*pi))", "20*pi**2",
          r"$dl=R\,d\alpha$ : $Q=\int_0^{2\pi}5\alpha\,R\,d\alpha=5R\frac{(2\pi)^2}2=10\pi^2R=20\pi^2$ C.", src=T1 + ", ex. 3", duree=3),
        v("in3", r"Disque de rayon $R=2$ m, $\sigma=5$ C·m$^{-2}$ uniforme. Charge totale ?", "integrate(integrate(5*x,(x,0,2)),(t,0,2*pi))", "20*pi",
          r"$d^2S=r\,dr\,d\theta$ : $Q=5\int_0^2r\,dr\int_0^{2\pi}d\theta=5\times2\times2\pi=20\pi$ C ($=\sigma\pi R^2$).", src=T1 + ", ex. 3", duree=3),
        v("in4", r"Volume d'une sphère de rayon $R=3$ m par l'intégrale en coordonnées sphériques ?", "integrate(integrate(integrate(s**2*sin(t),(s,0,3)),(t,0,pi)),(ph,0,2*pi))", "36*pi",
          r"$V=\int_0^3r^2dr\int_0^\pi\sin\theta\,d\theta\int_0^{2\pi}d\varphi=9\times2\times2\pi=36\pi$ m$^3$ ($=\frac43\pi R^3$).", src=T5 + ", ex. 1", duree=3),
        v("in5", r"Cylindre de rayon $R=1$ m et de hauteur $h=2$ m, $\rho=4$ C·m$^{-3}$. Charge totale ?", "integrate(integrate(integrate(4*s,(s,0,1)),(t,0,2*pi)),(ph,0,2))", "8*pi",
          r"$d\tau=r\,dr\,d\theta\,dz$ : $Q=4\int_0^1r\,dr\int_0^{2\pi}d\theta\int_0^2dz=4\times\frac12\times2\pi\times2=8\pi$ C ($=\rho\pi R^2h$).", src=T4 + ", ex. 1", duree=3),
    ]},
    {"n": 3, "titre": "Rappel S2 : champ de charges ponctuelles et superposition", "notions": ["coulomb", "vect"], "exos": [
        v("ch1", r"Force (en N) entre deux charges de $2$ nC et $3$ nC distantes de $3$ cm ($k=9\times10^9$) ?", "9*10**9*2*10**-9*3*10**-9/Rational(3,100)**2", "6/10**5",
          r"$F=k\frac{q_1q_2}{r^2}=\frac{9\times10^9\times6\times10^{-18}}{9\times10^{-4}}=6\times10^{-5}$ N.", duree=2),
        v("ch2", r"Champ (en V·m$^{-1}$) créé par $q=5$ nC à $0{,}5$ m ?", "9*10**9*5*10**-9/Rational(1,2)**2", "180", r"$E=k\frac q{r^2}=\frac{45}{0{,}25}=180$ V·m$^{-1}$.", duree=2),
        v("ch3", r"Deux charges identiques $q=1$ nC en $A$ et $B$ distants de $2a$ ; $C$ est sur la médiatrice, $CA=CB=0{,}5$ m et $OC=d=0{,}3$ m ($O$ milieu de $AB$). Champ total en $C$ (en V·m$^{-1}$) ?",
          "2*9*10**9*10**-9*Rational(3,10)/Rational(1,2)**3", "216/5",
          r"Chaque charge crée $\frac{kq}{a^2}$ avec $a=0{,}5$ ; les composantes parallèles à $AB$ s'annulent, celles selon $OC$ s'ajoutent : $E=2\frac{kq}{a^2}\cos\alpha$ avec $\cos\alpha=\frac da$, soit $E=\frac{2kqd}{a^3}=\frac{2\times9\times0{,}3}{0{,}125}=43{,}2$ V·m$^{-1}$.", src=OCT16 + ", ex. 1", duree=5),
        v("ch4", r"Trois charges $+q,-q,-q$ ($q=1$ nC) aux sommets $A,B,C$ d'un triangle équilatéral de côté $a=0{,}3$ m. Norme du champ au centre $O$ (en V·m$^{-1}$) ?",
          "6*9*10**9*10**-9/Rational(3,10)**2", "600",
          r"$OA=OB=OC=\frac a{\sqrt3}$ : chaque charge crée $E_1=\frac{3kq}{a^2}=300$. Avec $\vec u_A+\vec u_B+\vec u_C=\vec0$ ($\vec u$ unitaires de $O$ vers les sommets) : $\vec E=E_1(-\vec u_A+\vec u_B+\vec u_C)=-2E_1\vec u_A$, de norme $2E_1=\frac{6kq}{a^2}=600$ V·m$^{-1}$.", src=NOV21 + ", ex. 1", duree=6),
        v("ch5", r"Carré $ABCD$ de côté $a=0{,}3$ m : $A$ (en haut à gauche) porte $-q$, $B$ (en haut à droite) $+q$, $D$ (en bas à gauche) $+q$, avec $q=1$ nC ; $C$ (en bas à droite) est vide. Norme du champ en $C$ (en V·m$^{-1}$) ?",
          "sqrt((100-50*cos(pi/4))**2+(-100+50*sin(pi/4))**2)", "100*sqrt(2)-50",
          r"$\frac{kq}{a^2}=100$. $\vec E_D(C)=100\vec u_x$ ; $\vec E_B(C)=-100\vec u_y$ ; $A$ est à $a\sqrt2$ et attire : $E_A=\frac{kq}{2a^2}=50$, dirigé vers $A$, soit $50\left(-\cos45^\circ,\sin45^\circ\right)$. Somme : $\vec E=(100-25\sqrt2,\ -100+25\sqrt2)$, de norme $\sqrt2(100-25\sqrt2)=100\sqrt2-50\approx91{,}4$ V·m$^{-1}$.", src=OCT24 + ", ex. 2", duree=8),
    ]},
    {"n": 4, "titre": "Rappel S2 : potentiel et énergie", "notions": ["potentiel"], "exos": [
        v("pe1", r"Potentiel (en V) en un point à $0{,}3$ m d'une charge de $3$ nC et à $0{,}6$ m d'une charge de $-1$ nC ?", "9*10**9*(3*10**-9/Rational(3,10)-10**-9/Rational(6,10))", "75",
          r"$V=\sum k\frac{q_i}{r_i}=9\times10^9\left(\frac{3\times10^{-9}}{0{,}3}-\frac{10^{-9}}{0{,}6}\right)=90-15=75$ V : le potentiel est un scalaire, on additionne sans projeter.", duree=3),
        v("pe2", r"Trois charges $+q,-q,-q$ ($q=4$ nC) aux sommets d'un triangle équilatéral de côté $a=2$ cm. Potentiel en son centre $O$ (en V) ?", "-sqrt(3)*9*10**9*4*10**-9/Rational(2,100)", "-1800*sqrt(3)",
          r"$OA=OB=OC=\frac a{\sqrt3}$ : $V(O)=\frac{k}{a/\sqrt3}(q-q-q)=-\frac{\sqrt3\,kq}a=-\frac{\sqrt3\times36}{0{,}02}=-1800\sqrt3\approx-3118$ V.", src=NOV21 + ", ex. 1", duree=4),
        v("pe3", r"Mêmes charges : énergie potentielle électrique (en J) de la charge $+q$ placée en $A$ dans le champ des deux autres ?", "4*10**-9*(-2*9*10**9*4*10**-9/Rational(2,100))", "-144/10**7",
          r"$V(A)=k\frac{-q}a+k\frac{-q}a=-\frac{2kq}a=-3600$ V, puis $E_p(A)=qV(A)=4\times10^{-9}\times(-3600)=-1{,}44\times10^{-5}$ J.", src=NOV21 + ", ex. 1", duree=4),
        v("pe4", r"On donne $V(r)=a\,r\,e^{-b/r}$ ($a$, $b$ constantes). Calculer $E_r=-\frac{dV}{dr}$.", "-diff(a*x*exp(-b/x),x)", "-a*exp(-b/x)*(1+b/x)",
          r"$\frac{dV}{dr}=ae^{-b/r}+ar\cdot\frac b{r^2}e^{-b/r}=ae^{-b/r}\left(1+\frac br\right)$, donc $E_r=-ae^{-b/r}\left(1+\frac br\right)$.", src=NOV21 + ", QCM 1", duree=3),
        v("pe5", r"Trois charges de $1$ nC aux sommets d'un triangle équilatéral de côté $0{,}3$ m. Énergie électrostatique du système (en J) ?", "3*9*10**9*10**-18/Rational(3,10)", "9/10**8",
          r"Trois paires, chacune à $0{,}3$ m : $E_{pe}=3\times k\frac{q^2}a=3\times\frac{9\times10^9\times10^{-18}}{0{,}3}=9\times10^{-8}$ J.", duree=4),
    ]},
    {"n": 5, "titre": "Rappel S2 : force de Lorentz et spectromètre de masse", "notions": ["lorentz", "vect"], "exos": [
        v("lo1", r"Force (en N) sur $q=2e$ ($e=1{,}6\times10^{-19}$ C) de vitesse $10^5$ m·s$^{-1}$ perpendiculaire à $B=0{,}2$ T ?", "2*Rational(16,10)*10**-19*10**5*Rational(2,10)", "64/10**16",
          r"$F=|q|vB=3{,}2\times10^{-19}\times10^5\times0{,}2=6{,}4\times10^{-15}$ N.", duree=2),
        v("lo2", r"$\vec v=(2,0,0)$ et $\vec B=(0,0,-3)$ en unités SI. Calculer $\vec v\wedge\vec B$.", "Matrix([2,0,0]).cross(Matrix([0,0,-3]))", "Matrix([0,6,0])",
          r"$(\vec v\wedge\vec B)=(v_yB_z-v_zB_y,\ v_zB_x-v_xB_z,\ v_xB_y-v_yB_x)=(0,\ -2\times(-3),\ 0)=(0,6,0)$ : pour $q>0$ la particule est déviée vers $+\vec u_y$.", src=OCT24 + ", ex. 3 (q. 4)", duree=3),
        v("lo3", r"Ion $^{200}$Hg$^{2+}$ ($m=200\,u$ avec $u=1{,}66\times10^{-27}$ kg, $q=2e$) à $v_0=10^4$ m·s$^{-1}$ dans $B=0{,}2$ T perpendiculaire. Rayon de la trajectoire (en m) ?",
          "200*Rational(166,100)*10**-27*10**4/(2*Rational(16,10)*10**-19*Rational(2,10))", "83/1600",
          r"$R=\frac{mv_0}{qB}=\frac{3{,}32\times10^{-25}\times10^4}{3{,}2\times10^{-19}\times0{,}2}=\frac{3{,}32\times10^{-21}}{6{,}4\times10^{-20}}\approx0{,}052$ m.", src=OCT24 + ", ex. 3 (q. 5, données numériques choisies)", duree=4),
        v("lo4", r"Mêmes données avec l'isotope $^{202}$Hg$^{2+}$ : écart $\Delta y$ (en m) entre les points d'impact des deux isotopes (demi-tour, $y=2R$) ?", "2*(202-200)*Rational(166,100)*10**-27*10**4/(2*Rational(16,10)*10**-19*Rational(2,10))", "83/80000",
          r"À $v_0$ et $B$ fixés, $R\propto m$ : $\Delta y=2(R_{202}-R_{200})=\frac{2\times2u\times v_0}{qB}=\frac{4\times1{,}66\times10^{-27}\times10^4}{6{,}4\times10^{-20}}\approx1{,}04\times10^{-3}$ m.", src=OCT24 + ", ex. 3", duree=5),
        v("lo5", r"Un proton ($m=1{,}6\times10^{-27}$ kg, $q=1{,}6\times10^{-19}$ C), initialement au repos, est accéléré par $U=50$ V. Vitesse (en m·s$^{-1}$) ?", "sqrt(2*Rational(16,10)*10**-19*50/(Rational(16,10)*10**-27))", "100000",
          r"$\frac12mv^2=qU$ donne $v=\sqrt{\frac{2qU}m}=\sqrt{\frac{2\times1{,}6\times10^{-19}\times50}{1{,}6\times10^{-27}}}=\sqrt{10^{10}}=10^5$ m·s$^{-1}$.", src=OCT24 + ", ex. 3 (q. 3)", duree=3),
        o("lo6", r"Pourquoi la force magnétique ne change-t-elle pas la norme de la vitesse, alors que la force électrique le fait ?",
          r"La puissance de la force magnétique est $\vec F_{mag}\cdot\vec v=(q\vec v\wedge\vec B)\cdot\vec v=0$ car un produit vectoriel est orthogonal à chacun de ses facteurs : elle ne travaille pas, l'énergie cinétique est constante. La force électrique $q\vec E$ n'est pas orthogonale à $\vec v$ en général : sa puissance $q\vec E\cdot\vec v$ est non nulle, elle accélère la particule (cavité d'accélération : $E_c=qU$).", duree=3),
    ]},
    {"n": 6, "titre": "Onde plane progressive monochromatique", "notions": ["oem"], "exos": [
        v("wa1", r"Longueur d'onde (en m) d'une onde de fréquence $f=100$ MHz dans le vide ($c=3\times10^8$ m·s$^{-1}$) ?", "3*10**8/(100*10**6)", "3", r"$\lambda=\frac cf=\frac{3\times10^8}{10^8}=3$ m.", duree=1),
        v("wa2", r"Nombre d'onde $k$ (en rad·m$^{-1}$) d'une onde de longueur d'onde $\lambda=0{,}5$ m ?", "2*pi/Rational(1,2)", "4*pi", r"$k=\frac{2\pi}\lambda=4\pi$ rad·m$^{-1}$.", duree=1),
        v("wa3", r"Amplitude du champ magnétique (en T) d'une OPPM dont l'amplitude électrique est $E_0=300$ V·m$^{-1}$ ?", "300/(3*10**8)", "1/10**6", r"$B_0=\frac{E_0}c=\frac{300}{3\times10^8}=10^{-6}$ T.", duree=1),
        v("wa4", r"Fréquence (en THz) de la lumière de longueur d'onde $600$ nm ?", "3*10**8/(600*10**-9)/10**12", "500", r"$f=\frac c\lambda=\frac{3\times10^8}{6\times10^{-7}}=5\times10^{14}$ Hz $=500$ THz.", duree=2),
        v("wa5", r"L'onde $E=E_0\cos(\omega t-kx)$ vérifie $\frac{\partial^2E}{\partial x^2}=\frac1{c^2}\frac{\partial^2E}{\partial t^2}$. Exprimer $c$ en fonction de $\omega$ et $k$ (noté kk).",
          "sqrt(diff(cos(w*t-kk*x),t,2)/diff(cos(w*t-kk*x),x,2))", "w/kk",
          r"$\frac{\partial^2E}{\partial x^2}=-k^2E$ et $\frac{\partial^2E}{\partial t^2}=-\omega^2E$ : l'équation d'onde donne $k^2=\frac{\omega^2}{c^2}$, soit $c=\frac\omega k$ (relation de dispersion).", src="Cours, partie III.3", duree=4),
        v("wa6", r"Avec $E=E_0\cos(\omega t-kx)$ (noté kk pour $k$) et $\frac{\partial E}{\partial x}=-\frac{\partial B}{\partial t}$, trouver $B(x,t)$ (sans constante).",
          "-integrate(diff(E0*cos(w*t-kk*x),x),t)", "kk*E0*cos(w*t-kk*x)/w",
          r"$\frac{\partial E}{\partial x}=kE_0\sin(\omega t-kx)=-\frac{\partial B}{\partial t}$, donc $B=\frac{kE_0}\omega\cos(\omega t-kx)=\frac{E_0}c\cos(\omega t-kx)$ : $B_0=\frac{E_0}c$ et $\vec B$ en phase avec $\vec E$.", src="Cours, partie III.3", duree=5),
    ]},
    {"n": 7, "titre": "Symétries et invariances", "notions": ["symetrie"], "exos": [
        o("sy1", r"Énoncer le principe de Curie. Que peut-on dire de $\vec E(M)$ si $M$ appartient à un plan de symétrie de la distribution ? à un plan d'antisymétrie ?",
          r"Principe de Curie : les éléments de symétrie des causes (la distribution de charges) se retrouvent dans les effets (le champ). Si $M\in\Pi$ plan de symétrie, $\vec E(M)$ est contenu dans $\Pi$ (parallèle à ce plan). Si $M\in\Pi^*$ plan d'antisymétrie (la distribution devient opposée), $\vec E(M)$ est perpendiculaire à $\Pi^*$. Plusieurs plans : le champ est dans leur intersection.", src="Cours, partie I", duree=3),
        v("sy2", r"Fil infini (axe $Oz$) chargé uniformément, base $(\vec u_r,\vec u_\theta,\vec u_z)$. Combien de composantes de $\vec E(M)$ sont non nulles ?", "3-2", "1",
          r"Les plans $(M,\vec u_r,\vec u_z)$ et $(M,\vec u_r,\vec u_\theta)$ sont plans de symétrie : $\vec E$ est dans leur intersection, la droite portée par $\vec u_r$. Deux composantes ($E_\theta,E_z$) sont nulles, il en reste une : $E_r$.", src="QCM 2 ; TD4 ex. 1", duree=2),
        v("sy3", r"Fil infini chargé uniformément : de combien de coordonnées parmi $(r,\theta,z)$ dépend $E_r$ ?", "3-2", "1",
          r"Invariance par rotation autour de $Oz$ : pas de dépendance en $\theta$ ; invariance par translation le long de $Oz$ : pas de dépendance en $z$. Il reste $E_r(r)$ : une seule variable.", src="Cours, partie II.4", duree=2),
        v("sy4", r"Quatre charges identiques $q=1$ nC aux sommets d'un carré de côté $a=0{,}3$ m. Norme du champ au centre $O$ (en V·m$^{-1}$) ?", "(200*(Matrix([-1,1])+Matrix([1,1])+Matrix([1,-1])+Matrix([-1,-1]))/sqrt(2)).norm()", "0",
          r"Chaque charge est à $\frac a{\sqrt2}$ de $O$ et crée $\frac{2kq}{a^2}=200$ V·m$^{-1}$ ; les champs de deux sommets opposés sont opposés et s'annulent deux à deux : $\vec E(O)=\vec0$. Les diagonales sont des plans de symétrie.", src=T1 + ", ex. 1 (q. 1)", duree=3),
        o("sy5", r"Anneau de rayon $R$, d'axe $Oz$, chargé uniformément. Quelle est la direction de $\vec E(M)$ pour $M$ sur l'axe ?",
          r"Tout plan contenant l'axe $Oz$ est plan de symétrie de l'anneau et contient $M$ : $\vec E(M)$ appartient à tous ces plans, donc à leur intersection, l'axe $Oz$. Ainsi $\vec E(M)=E_z\vec u_z$. (Autre argument : pour tout point $P$ de l'anneau, le point diamétralement opposé crée un champ dont la composante perpendiculaire à l'axe est opposée.)", src=DEC17 + ", ex. 1", duree=3),
    ]},
    {"n": 8, "titre": "Flux d'un champ", "notions": ["flux"], "exos": [
        v("fl1", r"Champ uniforme de norme $200$ V·m$^{-1}$ faisant $60^\circ$ avec la normale d'un disque de rayon $0{,}1$ m. Flux (en V·m) ?", "200*pi*Rational(1,100)*cos(pi/3)", "pi", r"$\Phi=ES\cos\alpha=200\times\pi\times10^{-2}\times\frac12=\pi$ V·m.", src=P24 + ", QCM", duree=2),
        v("fl2", r"Champ radial $E(r)=100$ V·m$^{-1}$ à $r=0{,}5$ m. Flux (en V·m) à travers la sphère de rayon $0{,}5$ m centrée à l'origine ?", "100*4*pi*Rational(1,2)**2", "100*pi", r"$\Phi=E(r)\times4\pi r^2=100\times4\pi\times0{,}25=100\pi$ V·m.", src=DEC21 + ", QCM 5", duree=2),
        v("fl3", r"Champ radial $E_r=50$ V·m$^{-1}$ à $r=0{,}2$ m. Flux (en V·m) à travers la surface latérale du cylindre de rayon $0{,}2$ m et de hauteur $h=1$ m ?", "50*2*pi*Rational(1,5)*1", "20*pi",
          r"$\Phi=E_r\times2\pi rh=50\times2\pi\times0{,}2\times1=20\pi$ V·m (les bases n'ont pas de flux : $\vec E\perp d\vec S$).", src="Cours, partie II.4", duree=3),
        v("fl4", r"Champ uniforme $E_0\vec u_z$ à travers un cube de côté $a$ aux faces perpendiculaires aux axes : flux total sortant ?", "E0*a**2-E0*a**2", "0",
          r"Face du haut : $+E_0a^2$ ; face du bas : $-E_0a^2$ (normale sortante $-\vec u_z$) ; les quatre faces latérales : $0$. Total $0$ : un champ uniforme n'a pas de flux sortant net, il ne contient pas de charge.", duree=3),
        o("fl5", r"Donner l'expression de $d\vec S$ (orienté vers l'extérieur) pour une sphère de rayon $r$, pour la surface latérale d'un cylindre et pour ses deux bases.",
          r"Sphère : $d\vec S=r^2\sin\theta\,d\theta\,d\varphi\,\vec u_r$. Surface latérale du cylindre de rayon $r$ : $d\vec S=r\,d\theta\,dz\,\vec u_r$. Base du haut : $d\vec S=r\,dr\,d\theta\,\vec u_z$ ; base du bas : $d\vec S=-r\,dr\,d\theta\,\vec u_z$.", src="TD4 EM2 ; TD5 EM2", duree=4),
    ]},
    {"n": 9, "titre": "Théorème de Gauss : de la charge au flux", "notions": ["gauss"], "exos": [
        v("ga1", r"Flux (en V·m) du champ électrique à travers une surface fermée contenant $Q=2$ nC ($\varepsilon_0=\frac1{4\pi k}$) ?", "4*pi*9*10**9*2*10**-9", "72*pi", r"$\Phi=\frac Q{\varepsilon_0}=4\pi kQ=4\pi\times9\times10^9\times2\times10^{-9}=72\pi$ V·m.", src="QCM 2, question 1", duree=2),
        v("ga2", r"Par Gauss, champ (en V·m$^{-1}$) d'une charge ponctuelle $q=2$ nC à $r=0{,}3$ m : $E\times4\pi r^2=\frac q{\varepsilon_0}$ avec $\varepsilon_0=\frac1{4\pi k}$.", "(4*pi*9*10**9*2*10**-9)/(4*pi*Rational(9,100))", "200",
          r"$E=\frac q{4\pi\varepsilon_0r^2}=\frac{72\pi}{4\pi\times0{,}09}=200$ V·m$^{-1}$ : on retrouve $\frac{kq}{r^2}$.", duree=3),
        v("ga3", r"Une surface de Gauss contient $2$ nC et $-3$ nC ; une charge de $5$ nC est à l'extérieur. Flux (en V·m) ?", "4*pi*9*10**9*(2-3)*10**-9", "-36*pi",
          r"Seules les charges intérieures comptent : $\Phi=\frac{Q_{int}}{\varepsilon_0}=4\pi k(2-3)\times10^{-9}=-36\pi$ V·m. La charge extérieure crée du champ, mais son flux entrant et sortant se compensent.", src="Cours, partie II.3", duree=3),
        o("ga4", r"Citer les étapes de la méthode pour calculer un champ avec le théorème de Gauss.",
          r"1. Choisir les coordonnées adaptées (cylindriques pour un fil, sphériques pour une sphère, cartésiennes pour un plan). 2. Étudier les symétries : directions du champ. 3. Étudier les invariances : variables dont dépend le champ. 4. Schéma et surface de Gauss fermée passant par $M$, sur laquelle $E$ est constant ou $\vec E\perp d\vec S$. 5. Calculer le flux $\oiint\vec E\cdot d\vec S$. 6. Calculer $Q_{int}$ (intégrale de $\lambda$, $\sigma$ ou $\rho$ sur la partie intérieure). 7. Égaler flux $=\frac{Q_{int}}{\varepsilon_0}$ et conclure, en séparant les régions (intérieur/extérieur).", src="Cours, partie II ; TD3-TD5", duree=4),
    ]},
    {"n": 10, "titre": "Gauss : fil infini et cylindre creux", "notions": ["gauss-cyl", "gauss"], "exos": [
        v("fi1", r"Champ (en V·m$^{-1}$) d'un fil infini de densité $\lambda=1$ nC·m$^{-1}$ à $r=0{,}2$ m ($\frac1{2\pi\varepsilon_0}=2k$) ?", "2*9*10**9*10**-9/Rational(1,5)", "90",
          r"$E=\frac\lambda{2\pi\varepsilon_0r}=\frac{2k\lambda}r=\frac{2\times9\times10^9\times10^{-9}}{0{,}2}=90$ V·m$^{-1}$.", src="Cours, partie II.4", duree=2),
        v("fi2", r"Fil infini de densité $\lambda$. Surface de Gauss : cylindre de rayon $r$ et de hauteur $h$. Exprimer $E_r$ en fonction de lam ($\lambda$), h, r, e0 ($\varepsilon_0$).", "lam*h/(e0*2*pi*r*h)", "lam/(2*pi*e0*r)",
          r"Flux : $E_r\,2\pi rh$ (latéral seul) ; $Q_{int}=\int_0^h\lambda\,dz=\lambda h$. Donc $E_r=\frac{\lambda h}{2\pi\varepsilon_0rh}=\frac\lambda{2\pi\varepsilon_0r}$ : la hauteur arbitraire $h$ disparaît.", src="Cours, partie II.4", duree=3),
        v("fi3", r"À quelle distance (en m) d'un fil de $\lambda=1$ nC·m$^{-1}$ le champ vaut-il $45$ V·m$^{-1}$ ?", "2*9*10**9*10**-9/45", "2/5", r"$r=\frac{2k\lambda}E=\frac{18}{45}=0{,}4$ m.", duree=2),
        v("fi4", r"Cylindre creux infini de rayon $a=0{,}1$ m, chargé en surface ($\sigma=2$ nC·m$^{-2}$). Champ (en V·m$^{-1}$) à $r=0{,}4$ m de l'axe ($\varepsilon_0=\frac1{4\pi k}$) ?", "2*10**-9*Rational(1,10)*4*pi*9*10**9/Rational(4,10)", "18*pi",
          r"Gauss : $Q_{int}=\sigma\,2\pi ah$ et flux $E\,2\pi rh$ : $E=\frac{\sigma a}{\varepsilon_0r}=\frac{2\times10^{-9}\times0{,}1\times4\pi\times9\times10^9}{0{,}4}=18\pi\approx56{,}5$ V·m$^{-1}$.", src=DEC21 + ", QCM 8 (partie extérieure)", duree=4),
        o("fi5", r"Montrer que le champ est nul à l'intérieur d'un cylindre creux infini chargé uniformément en surface.",
          r"Symétries et invariances : $\vec E=E_r(r)\vec u_r$. Surface de Gauss : cylindre de rayon $r < a$ et de hauteur $h$, de flux $E_r\,2\pi rh$. Charge intérieure : $Q_{int}=0$ car toute la charge est sur la surface $r=a$. Donc $E_r\,2\pi rh=0$ : $\vec E=\vec0$ pour $r < a$.", src=DEC21 + ", QCM 8", duree=4),
    ]},
    {"n": 11, "titre": "Gauss : cylindre chargé en volume", "notions": ["gauss-cyl", "integ"], "exos": [
        v("cv1", r"Cylindre infini plein de rayon $R=0{,}2$ m, $\rho=2$ nC·m$^{-3}$. Champ (en V·m$^{-1}$) à $r=0{,}1$ m de l'axe ($\frac1{2\varepsilon_0}=2\pi k$) ?", "2*10**-9*Rational(1,10)*2*pi*9*10**9", "18*pi/5",
          r"Pour $r < R$ : $Q_{int}=\rho\pi r^2h$ et flux $E\,2\pi rh$, donc $E=\frac{\rho r}{2\varepsilon_0}=2\times10^{-9}\times0{,}1\times2\pi\times9\times10^9=3{,}6\pi\approx11{,}3$ V·m$^{-1}$.", src=T4 + ", ex. 1", duree=4),
        v("cv2", r"Même cylindre, mais à $r=0{,}4$ m ($r > R$) ?", "2*10**-9*Rational(1,5)**2*2*pi*9*10**9/Rational(4,10)", "18*pi/5",
          r"Pour $r > R$ : $Q_{int}=\rho\pi R^2h$, donc $E=\frac{\rho R^2}{2\varepsilon_0r}=\frac{2\times10^{-9}\times0{,}04\times2\pi\times9\times10^9}{0{,}4}=3{,}6\pi\approx11{,}3$ V·m$^{-1}$.", src=T4 + ", ex. 1", duree=4),
        v("cv3", r"Vérifier la continuité en $r=R$ : calculer le rapport $\frac{E(R^+)}{E(R^-)}$ avec $E(r < R)=\frac{\rho r}{2\varepsilon_0}$ et $E(r > R)=\frac{\rho R^2}{2\varepsilon_0r}$ (r, R, rho, e0).", "(rho*R**2/(2*e0*R))/(rho*R/(2*e0))", "1",
          r"$E(R^+)=\frac{\rho R}{2\varepsilon_0}=E(R^-)$ : le rapport vaut $1$, le champ est continu (pas de charge surfacique).", src=T4 + ", ex. 1", duree=2),
        v("cv4", r"Fil de rayon $R=2$ m, $\rho(r)=\frac\lambda r e^{-r/a}$ avec $\lambda=1$ et $a=2$. Charge (en C) contenue dans le cylindre de rayon $r=2$ m et de hauteur $h=1$ m ?", "integrate(integrate(integrate(exp(-s/2)/s*s,(s,0,2)),(t,0,2*pi)),(ph,0,1))", "4*pi*(1-exp(-1))",
          r"$Q_{int}=\int_0^h\!\!\int_0^{2\pi}\!\!\int_0^r\frac\lambda re^{-s/a}\,s\,ds\,d\theta\,dz=2\pi h\lambda a\left(1-e^{-r/a}\right)=2\pi\times1\times1\times2\left(1-e^{-1}\right)=4\pi(1-e^{-1})$ (le facteur $r$ du jacobien simplifie le $\frac1r$).", src=T4 + ", ex. 2", duree=6),
        v("cv5", r"Fil de rayon $R_1$, $\rho_0$ uniforme, entouré d'un cylindre creux de rayon $R_2$ chargé en surface avec $+Q$ (qq), même hauteur $h$. Champ pour $r > R_2$ en fonction de rho0, R1, h, qq, e0, r.",
          "(integrate(integrate(integrate(rho0*s,(s,0,R1)),(t,0,2*pi)),(z,0,h))+qq)/(e0*2*pi*r*h)", "(rho0*pi*R1**2*h+qq)/(2*pi*e0*r*h)",
          r"$Q_{int}=\rho_0\pi R_1^2h+Q$ (toute la charge est à l'intérieur de la surface de Gauss de rayon $r > R_2$), flux $E\,2\pi rh$ : $E=\frac{\rho_0\pi R_1^2h+Q}{2\pi\varepsilon_0rh}$.", src=DEC21 + ", ex. 3", duree=6),
    ]},
    {"n": 12, "titre": "Gauss : plan infini et condensateur plan", "notions": ["gauss-plan", "gauss"], "exos": [
        v("pl1", r"Plan infini de densité $\sigma=2$ nC·m$^{-2}$. Champ (en V·m$^{-1}$) de part et d'autre ($\frac1{2\varepsilon_0}=2\pi k$) ?", "2*10**-9*2*pi*9*10**9", "36*pi",
          r"Cylindre de Gauss de section $S$ : $2ES=\frac{\sigma S}{\varepsilon_0}$, donc $E=\frac\sigma{2\varepsilon_0}=2\times10^{-9}\times2\pi\times9\times10^9=36\pi\approx113$ V·m$^{-1}$, sortant ($z > 0$) ou rentrant ($z < 0$).", src=T3 + ", ex. 1", duree=3),
        v("pl2", r"Deux plans infinis chargés $+\sigma$ et $-\sigma$ ($\sigma=2$ nC·m$^{-2}$). Champ (en V·m$^{-1}$) entre eux ?", "2*(2*10**-9*2*pi*9*10**9)", "72*pi",
          r"Par superposition, entre les plans les champs des deux nappes ont même sens : $E=\frac\sigma{2\varepsilon_0}+\frac\sigma{2\varepsilon_0}=\frac\sigma{\varepsilon_0}=72\pi$ V·m$^{-1}$ ; à l'extérieur ils se compensent : $\vec E=\vec0$.", src=T3 + ", ex. 2", duree=3),
        v("pl3", r"Les plans sont distants de $e=1$ mm. Tension $U$ (en V) entre eux ?", "(2*10**-9*4*pi*9*10**9)*Rational(1,1000)", "9*pi/125",
          r"$E=-\frac{dV}{dz}$ donne $U=Ee=\frac{\sigma e}{\varepsilon_0}=72\pi\times10^{-3}=\frac{9\pi}{125}\approx0{,}226$ V.", src=T3 + ", ex. 2", duree=3),
        v("pl4", r"Surface $S=1$ m$^2$ et $e=1$ mm. Capacité $C=\frac{\varepsilon_0S}e$ (en F) avec $\varepsilon_0=\frac1{4\pi k}$ ?", "1*1000/(4*pi*9*10**9)", "1/(36*10**6*pi)",
          r"$C=\frac QU=\frac{\sigma S}{\sigma e/\varepsilon_0}=\frac{\varepsilon_0S}e=\frac{1000}{4\pi\times9\times10^9}=\frac1{36\times10^6\pi}\approx8{,}8\times10^{-9}$ F.", src=T3 + ", ex. 2", duree=3),
        o("pl5", r"Comment fabriquer un condensateur de grande capacité tout en réduisant la place occupée ? Quelle est la limite ?",
          r"$C=\frac{\varepsilon_0S}e$ : il faut augmenter $S$ et diminuer $e$. Augmenter $S$ augmente l'encombrement (on enroule ou on empile les armatures) ; diminuer $e$ réduit l'encombrement. Limite : la tension de claquage (environ $32$ kV·cm$^{-1}$ dans l'air), au-delà de laquelle une étincelle décharge le condensateur.", src=T3 + ", ex. 2", duree=4),
    ]},
    {"n": 13, "titre": "Gauss : sphère chargée", "notions": ["gauss-sph", "gauss", "integ"], "exos": [
        v("sp1", r"Boule uniformément chargée, $\rho_0=3$ nC·m$^{-3}$, rayon $R=0{,}2$ m. Champ (en V·m$^{-1}$) à $r=0{,}1$ m ($\varepsilon_0=\frac1{4\pi k}$) ?", "3*10**-9*Rational(1,10)*4*pi*9*10**9/3", "18*pi/5",
          r"$r < R$ : $Q_{int}=\frac43\pi r^3\rho_0$, flux $E\,4\pi r^2$ : $E=\frac{\rho_0r}{3\varepsilon_0}=\frac{3\times10^{-9}\times0{,}1\times4\pi\times9\times10^9}3=3{,}6\pi$ V·m$^{-1}$.", src=T5 + ", ex. 2", duree=4),
        v("sp2", r"Même boule, mais à $r=0{,}4$ m ?", "3*10**-9*Rational(1,5)**3*4*pi*9*10**9/(3*Rational(4,10)**2)", "9*pi/5",
          r"$r > R$ : $Q_{int}=\frac43\pi R^3\rho_0$, donc $E=\frac{\rho_0R^3}{3\varepsilon_0r^2}=\frac{3\times10^{-9}\times0{,}008\times4\pi\times9\times10^9}{3\times0{,}16}=1{,}8\pi$ V·m$^{-1}$ : champ d'une charge ponctuelle placée en $O$.", src=T5 + ", ex. 2", duree=4),
        v("sp3", r"Boule de rayon $R$ avec $\rho(r)=\rho_0\frac{r^2}{R^2}$. Champ pour $r < R$ en fonction de rho0, r, R, e0.", "integrate(rho0*s**2/R**2*4*pi*s**2,(s,0,r))/(4*pi*r**2*e0)", "rho0*r**3/(5*e0*R**2)",
          r"$Q_{int}=\int_0^r\rho_0\frac{s^2}{R^2}4\pi s^2ds=\frac{4\pi\rho_0r^5}{5R^2}$ ; flux $E\,4\pi r^2$ : $E=\frac{\rho_0r^3}{5\varepsilon_0R^2}$.", src=DEC21 + ", ex. 2", duree=6),
        v("sp4", r"Noyau de rayon $a$ avec $\rho(r)=\rho_0\left(1-\frac{r^2}{a^2}\right)$ et de charge totale $Ze$ (Z, qe, a). Exprimer $\rho_0$.", "Z*qe/integrate(integrate(integrate((1-s**2/a**2)*s**2*sin(t),(s,0,a)),(t,0,pi)),(ph,0,2*pi))", "15*Z*qe/(8*pi*a**3)",
          r"$Ze=\rho_0\int_0^a\left(1-\frac{r^2}{a^2}\right)r^2dr\times4\pi=4\pi\rho_0\left(\frac{a^3}3-\frac{a^3}5\right)=\frac{8\pi\rho_0a^3}{15}$, donc $\rho_0=\frac{15Ze}{8\pi a^3}$.", src=T5 + ", ex. 3", duree=6),
        v("sp5", r"Sphère creuse de rayon $R=0{,}1$ m chargée en surface ($\sigma=1$ nC·m$^{-2}$). Champ (en V·m$^{-1}$) à $r=0{,}3$ m ($\varepsilon_0=\frac1{4\pi k}$) ?", "10**-9*Rational(1,10)**2*4*pi*9*10**9/Rational(3,10)**2", "4*pi",
          r"$Q_{int}=\sigma4\pi R^2$ et flux $E\,4\pi r^2$ : $E=\frac{\sigma R^2}{\varepsilon_0r^2}=\frac{10^{-9}\times0{,}01\times4\pi\times9\times10^9}{0{,}09}=4\pi\approx12{,}6$ V·m$^{-1}$ ; à l'intérieur $Q_{int}=0$ donc $\vec E=\vec0$.", src=DEC17 + ", ex. 2", duree=4),
    ]},
    {"n": 14, "titre": "Du champ au potentiel : intégration et gradient", "notions": ["potentiel", "gauss-sph", "gauss-cyl"], "exos": [
        v("pg1", r"Sphère creuse : $E(r)=\frac{\sigma R^2}{\varepsilon_0r^2}$ pour $r > R$. Potentiel $V(r)$ en prenant $V(\infty)=0$ (sig, R, e0, r).", "-integrate(sig*R**2/(e0*s**2),s).subs(s,r)", "sig*R**2/(e0*r)",
          r"$V(r)=-\int E\,dr=\frac{\sigma R^2}{\varepsilon_0r}+C$ et $V(\infty)=0$ donne $C=0$. On retrouve $\frac{kQ}r$ avec $Q=4\pi R^2\sigma$.", src=DEC17 + ", ex. 2 (q. 3)", duree=4),
        v("pg2", r"Fil infini $\lambda=1$ nC·m$^{-1}$, $E(r)=\frac{2k\lambda}r$. Différence de potentiel $V(0{,}1)-V(0{,}2)$ (en V) ?", "integrate(2*9*10**9*10**-9/s,(s,Rational(1,10),Rational(2,10)))", "18*log(2)",
          r"$V(r_1)-V(r_2)=\int_{r_1}^{r_2}E\,dr=2k\lambda\ln\frac{r_2}{r_1}=18\ln2\approx12{,}5$ V.", src=P24 + ", ex. 3 (q. 4)", duree=4),
        v("pg3", r"Boule uniformément chargée : $E=\frac{\rho_0r}{3\varepsilon_0}$ pour $r < R$. $V(r)$ à une constante près (rho0, e0, r).", "-integrate(rho0*s/(3*e0),s).subs(s,r)", "-rho0*r**2/(6*e0)",
          r"$V(r)=-\int\frac{\rho_0r}{3\varepsilon_0}dr=-\frac{\rho_0r^2}{6\varepsilon_0}+C$ : le potentiel est maximal au centre.", src=DEC21 + ", ex. 2 (q. 3)", duree=4),
        v("pg4", r"Potentiel $V(r)=\frac{kq}r$. Calculer $E_r=-\frac{dV}{dr}$ (k, q, x).", "-diff(k*q/x,x)", "k*q/x**2", r"$E_r=-\frac{d}{dr}\left(\frac{kq}r\right)=\frac{kq}{r^2}$.", duree=2),
        o("pg5", r"Pourquoi ne peut-on pas imposer $V(\infty)=0$ pour un fil infini ? Comment fixer la constante ?",
          r"$V(r)=-\int\frac\lambda{2\pi\varepsilon_0r}dr=-\frac\lambda{2\pi\varepsilon_0}\ln r+C$ : $V$ diverge quand $r\to\infty$ (la charge est elle-même à l'infini). On choisit une référence $V(r_0)=0$ en un rayon $r_0$ fini : $V(r)=-\frac\lambda{2\pi\varepsilon_0}\ln\frac r{r_0}$. Seules les différences de potentiel ont un sens physique.", src=P24 + ", ex. 3 (q. 4)", duree=4),
    ]},
    {"n": 15, "titre": "Distributions continues sans Gauss : anneau et axe", "notions": ["anneau", "potentiel"], "exos": [
        v("an1", r"Anneau de rayon $R=0{,}6$ m, $\lambda=1$ nC·m$^{-1}$. Champ (en V·m$^{-1}$) au point de l'axe à $z=0{,}8$ m ?", "9*10**9*10**-9*2*pi*Rational(6,10)*Rational(8,10)/(Rational(6,10)**2+Rational(8,10)**2)**Rational(3,2)", "216*pi/25",
          r"$E_z=\frac{k\,2\pi R\lambda\,z}{(R^2+z^2)^{3/2}}$ avec $R^2+z^2=1$ : $E=9\times2\pi\times0{,}6\times0{,}8=8{,}64\pi\approx27{,}1$ V·m$^{-1}$ ($=\frac{216\pi}{25}$).", src=T2 + ", ex. 1", duree=5),
        v("an2", r"Un élément de l'anneau, de charge $dQ=\lambda R\,d\theta$, crée sur l'axe $dE_z=\frac{k\lambda Rz\,d\theta}{(R^2+z^2)^{3/2}}$. Intégrer sur l'anneau (lam, R, z, k).", "integrate(k*lam*R*z/(R**2+z**2)**Rational(3,2),(t,0,2*pi))", "2*pi*k*lam*R*z/(R**2+z**2)**Rational(3,2)",
          r"Seul $\theta$ varie : $E_z=\frac{k\lambda Rz}{(R^2+z^2)^{3/2}}\int_0^{2\pi}d\theta=\frac{2\pi k\lambda Rz}{(R^2+z^2)^{3/2}}$ (les composantes perpendiculaires à l'axe s'annulent par symétrie).", src=NOV21 + ", ex. 3 (q. 2)", duree=5),
        v("an3", r"Potentiel de l'anneau en $M$ de l'axe : $dV=\frac{k\lambda R\,d\theta}{\sqrt{R^2+z^2}}$. Intégrer (lam, R, z, k).", "integrate(k*lam*R/sqrt(R**2+z**2),(t,0,2*pi))", "2*pi*k*lam*R/sqrt(R**2+z**2)",
          r"$V(M)=\frac{k\lambda R}{\sqrt{R^2+z^2}}\int_0^{2\pi}d\theta=\frac{2\pi k\lambda R}{\sqrt{R^2+z^2}}=\frac{kQ}{\sqrt{R^2+z^2}}$ : scalaire, aucune projection.", src=NOV21 + ", ex. 3 (q. 3)", duree=4),
        v("an4", r"Retrouver le champ à partir de $V(z)=\frac{2\pi k\lambda R}{\sqrt{R^2+z^2}}$ avec $E_z=-\frac{\partial V}{\partial z}$ (lam, R, z, k).", "-diff(2*pi*k*lam*R/sqrt(R**2+z**2),z)", "2*pi*k*lam*R*z/(R**2+z**2)**Rational(3,2)",
          r"$\frac d{dz}(R^2+z^2)^{-1/2}=-z(R^2+z^2)^{-3/2}$, donc $E_z=\frac{2\pi k\lambda R\,z}{(R^2+z^2)^{3/2}}$ : même résultat que par intégration.", src=NOV21 + ", ex. 3 (q. 4)", duree=4),
        v("an5", r"Comportement loin de l'anneau : calculer $\lim_{z\to+\infty}z^2E_z$ avec $E_z=\frac{2\pi k\lambda Rz}{(R^2+z^2)^{3/2}}$ (lam, R, k).", "limit(2*pi*k*lam*R*z**3/(R**2+z**2)**Rational(3,2),z,oo)", "2*pi*k*lam*R",
          r"$\frac{z^3}{(R^2+z^2)^{3/2}}\to1$, donc $E_z\sim\frac{2\pi k\lambda R}{z^2}=\frac{kQ}{z^2}$ avec $Q=2\pi R\lambda$ : de loin, l'anneau se comporte comme une charge ponctuelle (vérification de vraisemblance).", src=T2 + ", ex. 1 (q. 5)", duree=4),
        v("an6", r"Quatre charges $q$ aux sommets d'un carré de côté $L$ créent sur l'axe $E=\frac{4kqx}{(x^2+L^2/2)^{3/2}}$, maximal en $x=\frac L2$. Valeur maximale (k, q, L).", "4*k*q*(L/2)/((L/2)**2+L**2/2)**Rational(3,2)", "16*sqrt(3)*k*q/(9*L**2)",
          r"En $x=\frac L2$ : $x^2+\frac{L^2}2=\frac{3L^2}4$, donc $E_{max}=\frac{4kq\frac L2}{\left(\frac{3L^2}4\right)^{3/2}}=\frac{2kqL}{\frac{3\sqrt3L^3}8}=\frac{16kq}{3\sqrt3L^2}=\frac{16\sqrt3\,kq}{9L^2}$.", src=T1 + ", ex. 1 (q. 5)", duree=5),
    ]},
    {"n": 16, "titre": "Niveau examen : charges discrètes et spectromètre", "notions": ["coulomb", "potentiel", "lorentz", "vect"], "examen": True, "exos": [
        {"id": "mx1", "kind": "multi", "src": f"{OCT24}, ex. 2 (7 points)",
         "enonce": r"Trois charges : $A$ porte $-q$, $B$ et $D$ portent $+q$, $ABCD$ est un carré de côté $a$ ($A$ en haut à gauche, $B$ en haut à droite, $C$ en bas à droite, $D$ en bas à gauche ; $\vec u_x$ vers la droite, $\vec u_y$ vers le haut ; $C$ est vide)." "\n"
                   r"1. Champs de chaque charge en $C$ (schéma). 2. Norme de $\vec E_A(C)$. 3. Composante $E_x$ du champ total en $C$. 4. Norme du champ total en $C$ (en fonction de $k$, $q$, $a$).",
         "parts": ["x1a", "x1b", "x1c"]},
        {"id": "mx2", "kind": "multi", "src": f"{OCT24}, ex. 3 (8 points)",
         "enonce": r"Spectromètre de masse : une source émet des ions $^{200}$Hg$^{2+}$ et $^{202}$Hg$^{2+}$ ($q=2e$) qui traversent une cavité d'accélération (plaques $P_1$ et $P_2$, tension $U$, $\vec v_i\approx\vec0$), une cavité de filtrage en vitesse, puis entrent par la fente $F_3$ avec la vitesse $\vec v_0=v_0\vec e_x$ dans une zone où règne $\vec B_3=-B_3\vec e_z$ ($B_3=200$ mT). Ils décrivent un demi-cercle et frappent un détecteur à l'abscisse $y$." "\n"
                   r"1. Sens du champ $\vec E_1$ d'accélération ? 2. Force de Lorentz en $F_3$ (sens de déviation). 3. Rayon $R$ avec $\vec a=-\frac{v^2}R\vec e_r$. 4. Application : $v_0=10^4$ m·s$^{-1}$, rayon de l'isotope 200. 5. Écart des points d'impact des deux isotopes.",
         "parts": ["x2o", "x2b", "x2a", "lo3", "lo4"]},
        {"id": "mx3", "kind": "multi", "src": f"{DEC21}, ex. 1 (5 points)",
         "enonce": r"Quatre charges $+q$, $-2q$, $+2q$, $-q$ sont placées en $A$, $B$, $C$, $D$, sommets consécutifs d'un carré de côté $a$ (sens de rotation $A\to B\to C\to D$), de centre $O$." "\n"
                   r"1. Norme du champ résultant en $O$ (en fonction de $k$, $q$, $a$). 2. Potentiel en $A$. 3. Énergie électrique de la charge placée en $A$.",
         "parts": ["x3a", "x3b", "x3c"]},
    ]},
    {"n": 17, "titre": "Niveau examen : théorème de Gauss et anneau", "notions": ["gauss", "gauss-sph", "gauss-cyl", "anneau", "potentiel"], "examen": True, "exos": [
        {"id": "mx4", "kind": "multi", "src": f"{DEC21}, ex. 2 (6 points)",
         "enonce": r"Une sphère de centre $O$ et de rayon $R$ est chargée en volume avec la densité $\rho(r)=\rho_0\frac{r^2}{R^2}$ ($\rho_0$, $R$ positifs)." "\n"
                   r"1. Direction de $\vec E$ et variables dont il dépend. 2. Champ pour $r < R$ et pour $r > R$ (Gauss). 3. Continuité en $r=R$. 4. Potentiel pour $r > R$ ($V(\infty)=0$).",
         "parts": ["sy6", "sp3", "x4b", "x4c", "x4d"]},
        {"id": "mx5", "kind": "multi", "src": f"{DEC21}, ex. 3 (7 points)",
         "enonce": r"Deux cylindres de même axe $Oz$ et de même hauteur $h$ (grande devant les rayons, effets de bords négligés) : le cylindre plein de rayon $R_1$ porte la densité volumique constante $\rho_0 > 0$ ; le cylindre creux de rayon $R_2 > R_1$ porte la charge $+Q$ uniformément répartie sur sa surface latérale." "\n"
                   r"Champ $E(r)$ pour $r < R_1$, $R_1 < r < R_2$ et $r > R_2$.",
         "parts": ["x5c", "x5b", "cv5"]},
        {"id": "mx6", "kind": "multi", "src": f"{NOV21}, ex. 3 (6 points)",
         "enonce": r"Un anneau de rayon $R$, d'axe $Oz$, est chargé avec la densité linéique constante $\lambda > 0$. Pour un point $M$ de l'axe, d'altitude $z$ :" "\n"
                   r"1. Champ $E_z$ créé par l'anneau (intégration). 2. Potentiel $V(M)$. 3. Retrouver le champ avec $\vec E=-\overrightarrow{\mathrm{grad}}\,V$ (gradient en cylindriques).",
         "parts": ["an2", "an3", "an4"]},
    ]},
    {"n": 18, "titre": "Plus dur que l'examen (+20 %)", "notions": ["gauss", "gauss-cyl", "gauss-sph", "anneau", "potentiel"], "examen": True, "exos": [
        {"id": "mh1", "kind": "multi", "src": f"{P24}, ex. 3 (style : fil et cylindre creux, potentiel)",
         "enonce": r"Un fil infini de densité linéique $\lambda > 0$ est placé sur l'axe $Oz$ d'un cylindre creux de rayon $R$, de longueur $h$ (grande), portant la charge $+Q$ uniformément répartie sur sa surface latérale (effets de bords négligés)." "\n"
                   r"1. $E(r)$ pour $r < R$. 2. $E(r)$ pour $r > R$. 3. Saut de $E$ en $r=R$ et lien avec la densité surfacique $\sigma=\frac{Q}{2\pi Rh}$. 4. Potentiel $V(r)$ pour $r > R$ (à une constante près).",
         "parts": ["x8a", "x8b", "x8c", "x8d"]},
        {"id": "mh2", "kind": "multi", "src": f"{DEC17}, ex. 1 (style : deux anneaux coaxiaux)",
         "enonce": r"Deux anneaux de même axe $Oz$, de même centre $O$ et de rayons $R_1 < R_2$ portent respectivement les densités linéiques constantes $+\lambda$ et $-\lambda$. Pour $M$ sur l'axe, à la cote $z > 0$ :" "\n"
                   r"1. Champ créé par chaque anneau (direction et expression). 2. Champ total. 3. Potentiel total. 4. Que vaut le champ total quand $R_1\to R_2$ ?",
         "parts": ["an2", "x6b", "x6c", "x6d"]},
        {"id": "mh3", "kind": "multi", "src": f"{T5}, ex. 3 (noyau atomique)",
         "enonce": r"Un noyau de numéro atomique $Z$ est modélisé par $\rho(r)=\rho_0\left(1-\frac{r^2}{a^2}\right)$ pour $r < a$ et $0$ sinon." "\n"
                   r"1. Exprimer $\rho_0$ en fonction de $Z$ et de la charge élémentaire $e$. 2. Champ pour $r < a$. 3. Champ pour $r > a$. 4. Valeur du champ à la surface.",
         "parts": ["sp4", "x7b", "x7c", "x7d"]},
    ]},
]


EXTRA_PARTS = [
    v("x1a", r"Norme de $\vec E_A(C)$ en fonction de $k$, $q$, $a$ ($AC=a\sqrt2$).", "k*q/(sqrt(2)*a)**2", "k*q/(2*a**2)",
      r"$AC=a\sqrt2$ (diagonale) donc $E_A(C)=\frac{kq}{(a\sqrt2)^2}=\frac{kq}{2a^2}$, dirigé vers $A$ (charge négative) : $\vec E_A(C)=\frac{kq}{2a^2}\left(-\cos45^\circ\vec u_x+\sin45^\circ\vec u_y\right)$. Les autres : $\vec E_B(C)=-\frac{kq}{a^2}\vec u_y$ (répulsion par $B$ situé au-dessus de $C$) et $\vec E_D(C)=\frac{kq}{a^2}\vec u_x$ (répulsion par $D$ situé à gauche).", src=f"{OCT24}, ex. 2.2"),
    v("x1b", r"Composante $E_x$ du champ total en $C$ (en fonction de $k$, $q$, $a$).", "k*q/a**2-k*q/(2*a**2)*cos(pi/4)", "k*q/a**2*(1-sqrt(2)/4)",
      r"Seuls $\vec E_D$ et $\vec E_A$ ont une composante en $x$ : $E_x=\frac{kq}{a^2}-\frac{kq}{2a^2}\cos45^\circ=\frac{kq}{a^2}\left(1-\frac{\sqrt2}4\right)$. Par symétrie du carré par rapport à la diagonale $AC$, $E_y=-E_x$.", src=f"{OCT24}, ex. 2.3"),
    v("x1c", r"Norme du champ total en $C$ (en fonction de $k$, $q$, $a$).", "sqrt(2)*(k*q/a**2-k*q/(2*a**2)*cos(pi/4))", "k*q/a**2*(sqrt(2)-1/2)",
      r"$E_y=-E_x$, donc $E=\sqrt{E_x^2+E_y^2}=\sqrt2\,E_x=\frac{kq}{a^2}\sqrt2\left(1-\frac{\sqrt2}4\right)=\frac{kq}{a^2}\left(\sqrt2-\frac12\right)$ (corrigé rédigé, vérifié par un calcul symbolique).", src=f"{OCT24}, ex. 2.4"),
    o("x2o", r"Sens du champ $\vec E_1$ dans la cavité d'accélération (ion positif émis depuis la source en $P_1$ vers $P_2$).",
      r"La force électrique $q\vec E_1$ doit accélérer l'ion de $P_1$ vers $P_2$ ; comme $q=2e > 0$, $\vec E_1$ a le même sens que la force : il est dirigé de $P_1$ vers $P_2$ (potentiel plus élevé en $P_1$ qu'en $P_2$, $U=V_1-V_2 > 0$). Dans cette cavité il n'y a pas de champ magnétique : $\vec F=q\vec E_1$.", src=f"{OCT24}, ex. 3.1"),
    v("x2b", r"Force de Lorentz en $F_3$ pour $\vec v_0=v_0\vec e_x$ et $\vec B_3=-B_3\vec e_z$ (v0, B3, q) : composantes $(F_x,F_y,F_z)$.", "q*Matrix([v0,0,0]).cross(Matrix([0,0,-B3]))", "Matrix([0,q*v0*B3,0])",
      r"$\vec F=q\vec v_0\wedge\vec B_3=q\,v_0\vec e_x\wedge(-B_3\vec e_z)=-qv_0B_3(\vec e_x\wedge\vec e_z)=+qv_0B_3\vec e_y$ car $\vec e_x\wedge\vec e_z=-\vec e_y$ : la force est selon $+\vec e_y$ (perpendiculaire à $\vec v_0$ et à $\vec B_3$), l'ion est dévié vers $+y$ et décrit un demi-cercle.", src=f"{OCT24}, ex. 3.4"),
    v("x2a", r"Rayon $R$ : on écrit $\vec a=-\frac{v_0^2}R\vec e_r$ et $m\vec a=\vec F_{Lorentz}$, soit $m\frac{v_0^2}R=qv_0B_3$ (m, v0, q, B3).", "solve(Eq(m*v0**2/R,q*v0*B3),R)[0]", "m*v0/(q*B3)",
      r"Mouvement circulaire uniforme : $m\frac{v_0^2}R=|q|v_0B_3$, d'où $R=\frac{mv_0}{qB_3}$ ; à $v_0$ et $B_3$ fixés, $R\propto m$, ce qui sépare les isotopes : $y=2R$ au détecteur.", src=f"{OCT24}, ex. 3.5"),
    v("x3a", r"Norme du champ en $O$ pour $+q,-2q,+2q,-q$ en $A,B,C,D$ (sommets consécutifs, $q=1$ nC, $a=0{,}3$ m).", "(2*100*(-(Matrix([-1,1])-2*Matrix([1,1])+2*Matrix([1,-1])-Matrix([-1,-1]))/sqrt(2))).norm()", "200*sqrt(2)",
      r"Chaque charge $q_i$ est à $\frac a{\sqrt2}$ de $O$ : $E_i=\frac{2k|q_i|}{a^2}$ ; avec les vecteurs unitaires $\vec u_i$ de $O$ vers les sommets, $\vec E_i=-\frac{2kq_i}{a^2}\vec u_i$. Somme : $-\frac{2kq}{a^2}(\vec u_A-2\vec u_B+2\vec u_C-\vec u_D)=-\frac{2kq}{a^2}\left(0,-\sqrt2\right)$ dans la base du carré, de norme $\frac{2\sqrt2\,kq}{a^2}$ ; numériquement $\frac{kq}{a^2}=100$ : $E=200\sqrt2\approx283$ V·m$^{-1}$ (corrigé rédigé : sujet sans corrigé, vérifié par somme vectorielle).", src=f"{DEC21}, ex. 1.2"),
    v("x3b", r"Potentiel en $A$ créé par les trois autres charges, en unités de $\frac{kq}a$ (coefficient numérique).", "(-2+2/sqrt(2)-1)", "-3+sqrt(2)",
      r"$V(A)=k\left(\frac{-2q}a+\frac{2q}{a\sqrt2}+\frac{-q}a\right)=\frac{kq}a\left(\sqrt2-3\right)$ ($B$ et $D$ sont adjacents à $A$, $C$ est à $a\sqrt2$).", src=f"{DEC21}, ex. 1.3a"),
    v("x3c", r"Énergie électrique de la charge $+q$ placée en $A$, en unités de $\frac{kq^2}a$.", "1*(-3+sqrt(2))", "-3+sqrt(2)",
      r"$E_p(A)=q\,V(A)=\frac{kq^2}a\left(\sqrt2-3\right)\approx-1{,}59\frac{kq^2}a<0$ : la charge en $A$ est globalement attirée par le reste de la distribution.", src=f"{DEC21}, ex. 1.3b"),
    o("sy6", r"Pour la boule de densité $\rho(r)$, quelle est la direction de $\vec E$ et de quelles variables dépend-il ?",
      r"Tout plan contenant $OM$ est plan de symétrie de la distribution : $\vec E(M)$ est dans tous ces plans, donc selon leur intersection, la droite $OM$ : $\vec E=E_r\vec u_r$. La distribution est invariante par toute rotation autour de $O$ : $E_r$ ne dépend ni de $\theta$ ni de $\varphi$. Ainsi $\vec E=E_r(r)\vec u_r$.", src=f"{DEC21}, ex. 2.1"),
    v("x4b", r"Champ pour $r > R$ de la boule de densité $\rho_0\frac{r^2}{R^2}$ (rho0, R, r, e0).", "integrate(rho0*s**2/R**2*4*pi*s**2,(s,0,R))/(4*pi*r**2*e0)", "rho0*R**3/(5*e0*r**2)",
      r"$Q_{int}=\frac{4\pi\rho_0R^3}5$ (toute la boule), flux $E\,4\pi r^2$ : $E=\frac{\rho_0R^3}{5\varepsilon_0r^2}$.", src=f"{DEC21}, ex. 2.2a"),
    v("x4c", r"Continuité en $r=R$ : calculer $E(R^+)-E(R^-)$ avec les deux expressions (rho0, R, e0).", "rho0*R**3/(5*e0*R**2)-rho0*R**3/(5*e0*R**2)", "0",
      r"$E(R^-)=\frac{\rho_0R^3}{5\varepsilon_0R^2}=\frac{\rho_0R}{5\varepsilon_0}$ et $E(R^+)=\frac{\rho_0R^3}{5\varepsilon_0R^2}=\frac{\rho_0R}{5\varepsilon_0}$ : égaux, le champ est continu (il n'y a pas de charge surfacique).", src=f"{DEC21}, ex. 2.2b"),
    v("x4d", r"Potentiel pour $r > R$, à une constante près (rho0, R, e0, r).", "-integrate(rho0*R**3/(5*e0*s**2),s).subs(s,r)", "rho0*R**3/(5*e0*r)",
      r"$E_r=-\frac{dV}{dr}$ ($\vec E$ radial, ne dépend que de $r$) : $V(r)=-\int\frac{\rho_0R^3}{5\varepsilon_0r^2}dr=\frac{\rho_0R^3}{5\varepsilon_0r}+C_2$. Pour $r < R$ : $V=-\frac{\rho_0r^4}{20\varepsilon_0R^2}+C_1$.", src=f"{DEC21}, ex. 2.3"),
    v("x5b", r"Champ pour $R_1 < r < R_2$ (rho0, R1, r, e0).", "integrate(integrate(integrate(rho0*s,(s,0,R1)),(t,0,2*pi)),(z,0,h))/(e0*2*pi*r*h)", "rho0*R1**2/(2*e0*r)",
      r"Surface de Gauss de rayon $r$ entre les deux cylindres : seule la charge du cylindre plein est à l'intérieur, $Q_{int}=\rho_0\pi R_1^2h$ ; flux $E\,2\pi rh$ : $E=\frac{\rho_0R_1^2}{2\varepsilon_0r}$.", src=f"{DEC21}, ex. 3.2"),
    v("x5c", r"Champ pour $r < R_1$ (rho0, r, e0).", "integrate(integrate(integrate(rho0*s,(s,0,r)),(t,0,2*pi)),(z,0,h))/(e0*2*pi*r*h)", "rho0*r/(2*e0)",
      r"$Q_{int}=\rho_0\pi r^2h$ (cylindre de Gauss de rayon $r < R_1$), flux $E\,2\pi rh$ : $E=\frac{\rho_0r}{2\varepsilon_0}$.", src=f"{DEC21}, ex. 3.2"),
    v("x6b", r"Champ de l'anneau de rayon $R_i$ à la cote $z$ (densité $\lambda_i$) : $E_i=\frac{2\pi k\lambda_iR_iz}{(R_i^2+z^2)^{3/2}}$. Champ total des deux anneaux ($+\lambda$ sur $R_1$, $-\lambda$ sur $R_2$) en fonction de k, lam, R1, R2, z.",
      "2*pi*k*lam*R1*z/(R1**2+z**2)**Rational(3,2)-2*pi*k*lam*R2*z/(R2**2+z**2)**Rational(3,2)", "2*pi*k*lam*z*(R1/(R1**2+z**2)**Rational(3,2)-R2/(R2**2+z**2)**Rational(3,2))",
      r"Chaque anneau crée un champ selon $\vec u_z$ ; celui de l'anneau $+\lambda$ s'éloigne de $M$ vers le haut, celui de l'anneau $-\lambda$ revient vers $O$. Par superposition : $E_z=2\pi k\lambda z\left[\frac{R_1}{(R_1^2+z^2)^{3/2}}-\frac{R_2}{(R_2^2+z^2)^{3/2}}\right]$ (les normes se soustraient car les champs sont opposés).", src=f"{DEC17}, ex. 1.4"),
    v("x6c", r"Potentiel total des deux anneaux (lam, k, R1, R2, z).", "2*pi*k*lam*R1/sqrt(R1**2+z**2)-2*pi*k*lam*R2/sqrt(R2**2+z**2)", "2*pi*k*lam*(R1/sqrt(R1**2+z**2)-R2/sqrt(R2**2+z**2))",
      r"Le potentiel est un scalaire : $V=\frac{2\pi k\lambda R_1}{\sqrt{R_1^2+z^2}}-\frac{2\pi k\lambda R_2}{\sqrt{R_2^2+z^2}}$.", src="Corrigé rédigé (extension de l'exercice)"),
    v("x6d", r"Limite du champ total quand $R_1\to R_2$ (les deux anneaux se confondent) à $z$ fixé : calculer $\lim_{R_1\to R_2}E_z$ avec les deux expressions précédentes (k, lam, R2, z).", "limit(2*pi*k*lam*z*(x/(x**2+z**2)**Rational(3,2)-R2/(R2**2+z**2)**Rational(3,2)),x,R2)", "0",
      r"Quand $R_1\to R_2$ les deux anneaux ont des charges opposées au même endroit : le champ total tend vers $0$ (distribution globalement neutre, le crochet s'annule).", src="Corrigé rédigé (extension de l'exercice)"),
    v("x7b", r"Noyau de densité $\rho_0\left(1-\frac{r^2}{a^2}\right)$ : champ pour $r < a$ (rho0, a, r, e0).", "integrate(rho0*(1-s**2/a**2)*4*pi*s**2,(s,0,r))/(4*pi*r**2*e0)", "rho0/(e0*r**2)*(r**3/3-r**5/(5*a**2))",
      r"$Q_{int}=4\pi\rho_0\left(\frac{r^3}3-\frac{r^5}{5a^2}\right)$ et flux $E\,4\pi r^2$ : $E=\frac{\rho_0}{\varepsilon_0r^2}\left(\frac{r^3}3-\frac{r^5}{5a^2}\right)$.", src=f"{T5}, ex. 3.2"),
    v("x7c", r"Champ pour $r > a$ (rho0, a, r, e0).", "integrate(rho0*(1-s**2/a**2)*4*pi*s**2,(s,0,a))/(4*pi*r**2*e0)", "2*rho0*a**3/(15*e0*r**2)",
      r"$Q_{int}=\frac{8\pi\rho_0a^3}{15}=Ze$ : $E=\frac{2\rho_0a^3}{15\varepsilon_0r^2}=\frac{Ze}{4\pi\varepsilon_0r^2}$ (champ d'une charge ponctuelle $Ze$).", src=f"{T5}, ex. 3.2"),
    v("x7d", r"Le champ est-il continu en $r=a$ ? Calculer $E(a^+)-E(a^-)$ (rho0, a, e0).", "2*rho0*a**3/(15*e0*a**2)-rho0/(e0*a**2)*(a**3/3-a**5/(5*a**2))", "0",
      r"$E(a^-)=\frac{\rho_0}{\varepsilon_0a^2}\left(\frac{a^3}3-\frac{a^3}5\right)=\frac{2\rho_0a}{15\varepsilon_0}$ et $E(a^+)=\frac{2\rho_0a^3}{15\varepsilon_0a^2}=\frac{2\rho_0a}{15\varepsilon_0}$ : continu ; la norme croît de $0$ en $r=0$, atteint un maximum puis décroît en $\frac1{r^2}$. (Représentation graphique : TD5 ex. 3.3.)", src=f"{T5}, ex. 3.3"),
    v("x8a", r"Champ pour $r < R$ du fil de densité $\lambda$ à l'intérieur du cylindre creux (lam, r, e0).", "lam*h/(e0*2*pi*r*h)", "lam/(2*pi*e0*r)",
      r"$Q_{int}=\lambda h$ (la charge $Q$ est sur le cylindre, à l'extérieur de la surface de Gauss), flux $E\,2\pi rh$ : $E=\frac\lambda{2\pi\varepsilon_0r}$.", src=f"{P24}, ex. 3.2"),
    v("x8b", r"Champ pour $r > R$ (lam, h, qq, r, e0).", "(lam*h+qq)/(e0*2*pi*r*h)", "(lam*h+qq)/(2*pi*e0*r*h)",
      r"$Q_{int}=\lambda h+Q$ : $E=\frac{\lambda h+Q}{2\pi\varepsilon_0rh}=\frac\lambda{2\pi\varepsilon_0r}+\frac Q{2\pi\varepsilon_0rh}$.", src=f"{P24}, ex. 3.2"),
    v("x8c", r"Saut $E(R^+)-E(R^-)$ en $r=R$ (qq, h, R, e0) et comparaison avec $\frac\sigma{\varepsilon_0}$, $\sigma=\frac Q{2\pi Rh}$.", "(lam*h+qq)/(2*pi*e0*R*h)-lam/(2*pi*e0*R)", "qq/(2*pi*e0*R*h)",
      r"$E(R^+)-E(R^-)=\frac{Q}{2\pi\varepsilon_0Rh}=\frac\sigma{\varepsilon_0}$ : le champ n'est pas continu en $r=R$, il saute de $\frac\sigma{\varepsilon_0}$ à la traversée de la nappe chargée.", src=f"{P24}, ex. 3.3"),
    v("x8d", r"Potentiel pour $r > R$, à une constante près (lam, h, qq, r, e0).", "-integrate((lam*h+qq)/(2*pi*e0*h*s),s).subs(s,r)", "-(lam*h+qq)/(2*pi*e0*h)*log(r)",
      r"$E_r=-\frac{dV}{dr}$ : $V(r)=-\frac{\lambda h+Q}{2\pi\varepsilon_0h}\ln r+C_2$ ; pour $r < R$ : $V=-\frac\lambda{2\pi\varepsilon_0}\ln r+C_1$ ; $C_1$ et $C_2$ se relient par la continuité de $V$ en $R$.", src=f"{P24}, ex. 3.4"),
]


def _v(enonce, calc, ans, sol):
    return {"enonce": enonce, "calc": calc, "ans": ans, "sol": sol}


VARIANTS = {
    "vc1": [_v(r"Norme du vecteur $\vec u=(2,3,6)$ ?", "sqrt(2**2+3**2+6**2)", "7", r"$\sqrt{4+9+36}=7$.")],
    "vc2": [_v(r"Produit scalaire de $\vec u=(2,-1,0)$ et $\vec v=(3,4,5)$ ?", "2*3-1*4+0*5", "2", r"$6-4+0=2$.")],
    "vc3": [_v(r"Composante selon $\vec u_z$ de $\vec u\wedge\vec v$ avec $\vec u=(1,4,0)$ et $\vec v=(2,3,0)$ ?", "Matrix([1,4,0]).cross(Matrix([2,3,0]))[2]", "-5", r"$u_xv_y-u_yv_x=3-8=-5$.")],
    "vc4": [_v(r"Un champ de norme $8$ V·m$^{-1}$ fait $30^\circ$ avec $Oy$. Sa composante selon $Oy$ ?", "8*cos(pi/6)", "4*sqrt(3)", r"$8\cos30^\circ=4\sqrt3$.")],
    "vc5": [_v(r"Deux champs de norme $E=8$ V·m$^{-1}$ font $\pm30^\circ$ avec $Ox$. Norme de leur somme ?", "2*8*cos(pi/6)", "8*sqrt(3)", r"$2E\cos30^\circ=8\sqrt3$.")],
    "in1": [_v(r"Fil de longueur $L=4$ m, $\lambda=x$. Charge totale ?", "integrate(x,(x,0,4))", "8", r"$\frac{L^2}2=8$ C.")],
    "in2": [_v(r"Anneau de rayon $R=1$ m, $\lambda=3\alpha$. Charge totale ?", "integrate(3*x*1,(x,0,2*pi))", "6*pi**2", r"$3R\frac{(2\pi)^2}2=6\pi^2$ C.")],
    "in3": [_v(r"Disque de rayon $R=3$ m, $\sigma=2$ C·m$^{-2}$ uniforme. Charge totale ?", "integrate(integrate(2*x,(x,0,3)),(t,0,2*pi))", "18*pi", r"$\sigma\pi R^2=18\pi$ C.")],
    "in4": [_v(r"Volume d'une sphère de rayon $R=2$ m par l'intégrale en sphériques ?", "integrate(integrate(integrate(s**2*sin(t),(s,0,2)),(t,0,pi)),(ph,0,2*pi))", "32*pi/3", r"$\frac43\pi\times8=\frac{32\pi}3$ m$^3$.")],
    "in5": [_v(r"Cylindre de rayon $R=2$ m, hauteur $h=1$ m, $\rho=3$ C·m$^{-3}$. Charge totale ?", "integrate(integrate(integrate(3*s,(s,0,2)),(t,0,2*pi)),(ph,0,1))", "12*pi", r"$\rho\pi R^2h=12\pi$ C.")],
    "ch1": [_v(r"Charges de $4$ nC et $1$ nC à $2$ cm. Force (en N) ?", "9*10**9*4*10**-9*10**-9/Rational(2,100)**2", "9/10**5", r"$\frac{9\times10^9\times4\times10^{-18}}{4\times10^{-4}}=9\times10^{-5}$ N.")],
    "ch2": [_v(r"Champ (en V·m$^{-1}$) créé par $q=2$ nC à $0{,}6$ m ?", "9*10**9*2*10**-9/Rational(6,10)**2", "50", r"$\frac{18}{0{,}36}=50$.")],
    "ch3": [_v(r"Mêmes charges, $CA=CB=0{,}5$ m et $OC=0{,}4$ m. Champ en $C$ (en V·m$^{-1}$) ?", "2*9*10**9*10**-9*Rational(4,10)/Rational(1,2)**3", "288/5", r"$\frac{2kqd}{a^3}=\frac{2\times9\times0{,}4}{0{,}125}=57{,}6$ V·m$^{-1}$.")],
    "ch4": [_v(r"Même triangle avec $q=2$ nC et $a=0{,}6$ m. Norme du champ en $O$ ?", "6*9*10**9*2*10**-9/Rational(6,10)**2", "300", r"$\frac{6kq}{a^2}=\frac{108}{0{,}36}=300$ V·m$^{-1}$.")],
    "ch5": [_v(r"Même carré avec $q=2$ nC et $a=0{,}6$ m. Norme du champ en $C$ ?", "sqrt((50-25*cos(pi/4))**2+(-50+25*sin(pi/4))**2)", "50*sqrt(2)-25", r"$\frac{kq}{a^2}=50$ : $E=50\sqrt2-25$ V·m$^{-1}$.")],
    "pe1": [_v(r"$2$ nC à $0{,}3$ m et $-1$ nC à $0{,}9$ m. Potentiel (en V) ?", "9*10**9*(2*10**-9/Rational(3,10)-10**-9/Rational(9,10))", "50", r"$60-10=50$ V.")],
    "pe2": [_v(r"Même triangle, $q=2$ nC et $a=3$ cm. $V(O)$ (en V) ?", "-sqrt(3)*9*10**9*2*10**-9/Rational(3,100)", "-600*sqrt(3)", r"$-\frac{\sqrt3kq}a=-\frac{18\sqrt3}{0{,}03}=-600\sqrt3$ V.")],
    "pe3": [_v(r"Même triangle, $q=2$ nC et $a=3$ cm. Énergie de $+q$ en $A$ (en J) ?", "2*10**-9*(-2*9*10**9*2*10**-9/Rational(3,100))", "-24/10**7", r"$V(A)=-\frac{2kq}a=-1200$ V, $E_p=2\times10^{-9}\times(-1200)=-2{,}4\times10^{-6}$ J.")],
    "pe4": [_v(r"$V(r)=a\,r\,e^{-r/b}$. Calculer $E_r=-\frac{dV}{dr}$.", "-diff(a*x*exp(-x/b),x)", "-a*exp(-x/b)*(1-x/b)", r"$\frac{dV}{dr}=ae^{-r/b}\left(1-\frac rb\right)$.")],
    "pe5": [_v(r"Trois charges de $2$ nC, triangle de côté $0{,}6$ m. Énergie (en J) ?", "3*9*10**9*4*10**-18/Rational(6,10)", "18/10**8", r"$3\frac{kq^2}a=\frac{1{,}08\times10^{-7}}{0{,}6}=1{,}8\times10^{-7}$ J.")],
    "lo1": [_v(r"$q=e$, $v=2\times10^5$ m·s$^{-1}$, $B=0{,}5$ T perpendiculaire. Force (en N) ?", "Rational(16,10)*10**-19*2*10**5*Rational(1,2)", "16/10**15", r"$evB=1{,}6\times10^{-14}$ N.")],
    "lo2": [_v(r"$\vec v=(1,0,0)$ et $\vec B=(0,0,-5)$. Calculer $\vec v\wedge\vec B$.", "Matrix([1,0,0]).cross(Matrix([0,0,-5]))", "Matrix([0,5,0])", r"$(0,\ -1\times(-5),\ 0)=(0,5,0)$.")],
    "lo3": [_v(r"Ion $^{202}$Hg$^{2+}$, mêmes $v_0$ et $B$. Rayon (en m) ?", "202*Rational(166,100)*10**-27*10**4/(2*Rational(16,10)*10**-19*Rational(2,10))", "8383/160000", r"$R=\frac{mv_0}{qB}=\frac{3{,}3532\times10^{-21}}{6{,}4\times10^{-20}}\approx0{,}0524$ m.")],
    "lo4": [_v(r"Mêmes ions avec $B=0{,}4$ T : écart $\Delta y$ (en m) ?", "2*(202-200)*Rational(166,100)*10**-27*10**4/(2*Rational(16,10)*10**-19*Rational(4,10))", "83/160000", r"$B$ double : $\Delta y$ est divisé par $2$ : $\approx5{,}2\times10^{-4}$ m.")],
    "lo5": [_v(r"Proton accéléré par $U=200$ V. Vitesse (en m·s$^{-1}$) ?", "sqrt(2*Rational(16,10)*10**-19*200/(Rational(16,10)*10**-27))", "200000", r"$v=\sqrt{\frac{2qU}m}=\sqrt{4\times10^{10}}=2\times10^5$ m·s$^{-1}$.")],
    "wa1": [_v(r"Longueur d'onde (en m) pour $f=1{,}5$ GHz ?", "3*10**8/(15*10**8)", "1/5", r"$\lambda=\frac{3\times10^8}{1{,}5\times10^9}=0{,}2$ m.")],
    "wa2": [_v(r"Nombre d'onde (en rad·m$^{-1}$) pour $\lambda=2$ m ?", "2*pi/2", "pi", r"$k=\frac{2\pi}2=\pi$.")],
    "wa3": [_v(r"$E_0=150$ V·m$^{-1}$. Amplitude $B_0$ (en T) ?", "150/(3*10**8)", "5/10**7", r"$B_0=\frac{150}{3\times10^8}=5\times10^{-7}$ T.")],
    "wa4": [_v(r"Fréquence (en THz) pour $\lambda=500$ nm ?", "3*10**8/(500*10**-9)/10**12", "600", r"$f=\frac{3\times10^8}{5\times10^{-7}}=6\times10^{14}$ Hz $=600$ THz.")],
    "wa5": [_v(r"Même question avec $E=E_0\sin(\omega t-kx)$ : exprimer $c$ (w, kk).", "sqrt(diff(sin(w*t-kk*x),t,2)/diff(sin(w*t-kk*x),x,2))", "w/kk", r"Les deux dérivées secondes valent $-\omega^2E$ et $-k^2E$ : $c^2=\frac{\omega^2}{k^2}$.")],
    "wa6": [_v(r"Avec $E=E_0\sin(\omega t-kx)$ (kk pour $k$) et $\frac{\partial E}{\partial x}=-\frac{\partial B}{\partial t}$, trouver $B(x,t)$ (sans constante).", "-integrate(diff(E0*sin(w*t-kk*x),x),t)", "kk*E0*sin(w*t-kk*x)/w", r"$\frac{\partial E}{\partial x}=-kE_0\cos(\omega t-kx)$, donc $\frac{\partial B}{\partial t}=kE_0\cos(\omega t-kx)$ et $B=\frac{kE_0}\omega\sin(\omega t-kx)$.")],
    "sy2": [_v(r"Sphère chargée en volume, base sphérique $(\vec u_r,\vec u_\theta,\vec u_\varphi)$. Nombre de composantes de $\vec E$ non nulles ?", "3-2", "1", r"Tout plan contenant $OM$ est de symétrie : $\vec E=E_r\vec u_r$.")],
    "sy3": [_v(r"Plan infini chargé uniformément ($Oxy$), base cartésienne : de combien de coordonnées dépend $E_z$ ?", "3-2", "1", r"Invariance par translation selon $x$ et $y$ : $E_z$ ne dépend que de $z$.")],
    "sy4": [_v(r"Carré $ABCD$ de côté $0{,}3$ m (sommets consécutifs) avec $+q,+q,-q,-q$ en $A,B,C,D$ ($q=1$ nC). Norme du champ en $O$ ?", "(200*(Matrix([-1,1])+Matrix([1,1])-Matrix([1,-1])-Matrix([-1,-1]))/sqrt(2)).norm()", "400*sqrt(2)", r"Les quatre champs ont même composante selon $-\vec u_y$ : $\vec E=-200\times\frac{4}{\sqrt2}\vec u_y\cdot\frac{1}{\ }$, soit une norme $400\sqrt2\approx566$ V·m$^{-1}$ (somme vectorielle des quatre termes $200$).")],
    "fl1": [_v(r"$E=100$ V·m$^{-1}$ à $60^\circ$ de la normale d'un disque de rayon $0{,}2$ m. Flux ?", "100*pi*Rational(1,25)*cos(pi/3)", "2*pi", r"$100\times\pi\times0{,}04\times\frac12=2\pi$ V·m.")],
    "fl2": [_v(r"$E(r)=50$ V·m$^{-1}$ à $r=1$ m. Flux à travers la sphère de rayon $1$ m ?", "50*4*pi*1**2", "200*pi", r"$E\times4\pi r^2=200\pi$ V·m.")],
    "fl3": [_v(r"$E_r=100$ V·m$^{-1}$ à $r=0{,}1$ m, hauteur $h=2$ m. Flux latéral ?", "100*2*pi*Rational(1,10)*2", "40*pi", r"$E\,2\pi rh=40\pi$ V·m.")],
    "fl4": [_v(r"Champ uniforme $E_0\vec u_x$ à travers un cylindre fermé d'axe $Ox$, de rayon $R$. Flux total sortant ?", "E0*pi*R**2-E0*pi*R**2", "0", r"Base de droite : $+E_0\pi R^2$ ; base de gauche : $-E_0\pi R^2$ ; surface latérale : $0$. Total nul.")],
    "ga1": [_v(r"Flux pour une surface fermée contenant $Q=-3$ nC ?", "4*pi*9*10**9*(-3)*10**-9", "-108*pi", r"$4\pi kQ=-108\pi$ V·m.")],
    "ga2": [_v(r"Par Gauss, champ de $q=5$ nC à $r=0{,}5$ m (V·m$^{-1}$) ?", "(4*pi*9*10**9*5*10**-9)/(4*pi*Rational(1,2)**2)", "180", r"$E=\frac{180\pi}{4\pi\times0{,}25}=180$.")],
    "ga3": [_v(r"Surface contenant $4$ nC et $-1$ nC ; $-7$ nC à l'extérieur. Flux ?", "4*pi*9*10**9*(4-1)*10**-9", "108*pi", r"$\Phi=\frac{Q_{int}}{\varepsilon_0}=4\pi k\times3\times10^{-9}=108\pi$ V·m.")],
    "fi1": [_v(r"Fil $\lambda=2$ nC·m$^{-1}$, $r=0{,}6$ m. Champ (V·m$^{-1}$) ?", "2*9*10**9*2*10**-9/Rational(6,10)", "60", r"$\frac{2k\lambda}r=\frac{36}{0{,}6}=60$.")],
    "fi2": [_v(r"Fil de charge totale $Q_0$ (qq) sur la longueur $h$ ($\lambda=\frac{Q_0}h$). Champ à $r$ (qq, h, r, e0) ?", "(qq/h)*h/(e0*2*pi*r*h)", "qq/(2*pi*e0*r*h)", r"$E=\frac{\lambda}{2\pi\varepsilon_0r}=\frac{Q_0}{2\pi\varepsilon_0rh}$.")],
    "fi3": [_v(r"$\lambda=2$ nC·m$^{-1}$, champ $60$ V·m$^{-1}$. Distance (m) ?", "2*9*10**9*2*10**-9/60", "3/5", r"$r=\frac{36}{60}=0{,}6$ m.")],
    "fi4": [_v(r"Cylindre creux $a=0{,}2$ m, $\sigma=1$ nC·m$^{-2}$, $r=0{,}5$ m. Champ (V·m$^{-1}$) ?", "10**-9*Rational(1,5)*4*pi*9*10**9/Rational(1,2)", "72*pi/5", r"$\frac{\sigma a}{\varepsilon_0r}=\frac{10^{-9}\times0{,}2\times4\pi\times9\times10^9}{0{,}5}=14{,}4\pi$.")],
    "cv1": [_v(r"$\rho=4$ nC·m$^{-3}$, $R=0{,}2$ m, $r=0{,}1$ m. Champ (V·m$^{-1}$) ?", "4*10**-9*Rational(1,10)*2*pi*9*10**9", "36*pi/5", r"$\frac{\rho r}{2\varepsilon_0}=4\times10^{-9}\times0{,}1\times2\pi\times9\times10^9=7{,}2\pi$.")],
    "cv2": [_v(r"$\rho=4$ nC·m$^{-3}$, $R=0{,}2$ m, $r=0{,}8$ m. Champ (V·m$^{-1}$) ?", "4*10**-9*Rational(1,5)**2*2*pi*9*10**9/Rational(8,10)", "18*pi/5", r"$\frac{\rho R^2}{2\varepsilon_0r}=\frac{4\times10^{-9}\times0{,}04\times2\pi\times9\times10^9}{0{,}8}=3{,}6\pi$.")],
    "cv3": [_v(r"Même question pour un cylindre creux : $E(r > a)=\frac{\sigma a}{\varepsilon_0r}$ et $E(a^-)=0$. Calculer $E(a^+)-E(a^-)$ (sig, a, e0).", "sig*a/(e0*a)-0", "sig/e0", r"$E(a^+)=\frac\sigma{\varepsilon_0}$ : saut égal à $\frac\sigma{\varepsilon_0}$ (charge surfacique).")],
    "cv4": [_v(r"Même densité avec $a=1$, $\lambda=3$, $r=1$, $h=1$. Charge intérieure ?", "integrate(integrate(integrate(3*exp(-s)/s*s,(s,0,1)),(t,0,2*pi)),(ph,0,1))", "6*pi*(1-exp(-1))", r"$2\pi h\lambda a(1-e^{-r/a})=6\pi(1-e^{-1})$.")],
    "cv5": [_v(r"Mêmes cylindres avec $\rho_0=2$, $R_1=1$, $h=1$, $Q=2\pi$, $r=2$, $\varepsilon_0=1$ (unités arbitraires). Champ ?", "(integrate(integrate(integrate(2*s,(s,0,1)),(t,0,2*pi)),(z,0,1))+2*pi)/(1*2*pi*2*1)", "1", r"$Q_{int}=2\pi+2\pi=4\pi$ et flux $E\times2\pi\times2\times1=4\pi E$ : $E=1$.")],
    "pl1": [_v(r"$\sigma=1$ nC·m$^{-2}$. Champ du plan (V·m$^{-1}$) ?", "10**-9*2*pi*9*10**9", "18*pi", r"$\frac\sigma{2\varepsilon_0}=2\pi k\sigma=18\pi$.")],
    "pl2": [_v(r"Deux plans $\pm\sigma$, $\sigma=1$ nC·m$^{-2}$. Champ entre eux (V·m$^{-1}$) ?", "2*(10**-9*2*pi*9*10**9)", "36*pi", r"$\frac\sigma{\varepsilon_0}=36\pi$.")],
    "pl3": [_v(r"$\sigma=1$ nC·m$^{-2}$, $e=5$ mm. Tension (V) ?", "(10**-9*4*pi*9*10**9)*Rational(5,1000)", "9*pi/50", r"$U=\frac{\sigma e}{\varepsilon_0}=36\pi\times5\times10^{-3}=\frac{9\pi}{50}$ V.")],
    "pl4": [_v(r"$S=2$ m$^2$, $e=1$ mm. Capacité (F) ?", "2*1000/(4*pi*9*10**9)", "1/(18*10**6*pi)", r"$C=\frac{\varepsilon_0S}e=\frac{2000}{4\pi\times9\times10^9}\approx1{,}8\times10^{-8}$ F.")],
    "sp1": [_v(r"$\rho_0=6$ nC·m$^{-3}$, $R=0{,}2$ m, $r=0{,}1$ m. Champ (V·m$^{-1}$) ?", "6*10**-9*Rational(1,10)*4*pi*9*10**9/3", "36*pi/5", r"$\frac{\rho_0r}{3\varepsilon_0}=7{,}2\pi$.")],
    "sp2": [_v(r"$\rho_0=3$ nC·m$^{-3}$, $R=0{,}2$ m, $r=0{,}4$ m. Champ (V·m$^{-1}$) ?", "3*10**-9*Rational(1,5)**3*4*pi*9*10**9/(3*Rational(4,10)**2)", "9*pi/5", r"$\frac{\rho_0R^3}{3\varepsilon_0r^2}=1{,}8\pi$.")],
    "sp3": [_v(r"$\rho(r)=\rho_0\frac rR$. Champ pour $r < R$ (rho0, r, R, e0) ?", "integrate(rho0*s/R*4*pi*s**2,(s,0,r))/(4*pi*r**2*e0)", "rho0*r**2/(4*e0*R)", r"$Q_{int}=\frac{\pi\rho_0r^4}R$ ; $E=\frac{\rho_0r^2}{4\varepsilon_0R}$.")],
    "sp4": [_v(r"$\rho(r)=\rho_0\left(1-\frac ra\right)$, charge totale $Ze$. Exprimer $\rho_0$ (Z, qe, a).", "Z*qe/integrate(integrate(integrate((1-s/a)*s**2*sin(t),(s,0,a)),(t,0,pi)),(ph,0,2*pi))", "3*Z*qe/(pi*a**3)", r"$Ze=4\pi\rho_0\left(\frac{a^3}3-\frac{a^3}4\right)=\frac{\pi\rho_0a^3}3$.")],
    "sp5": [_v(r"$R=0{,}2$ m, $\sigma=2$ nC·m$^{-2}$, $r=0{,}4$ m. Champ (V·m$^{-1}$) ?", "2*10**-9*Rational(1,5)**2*4*pi*9*10**9/Rational(4,10)**2", "18*pi", r"$\frac{\sigma R^2}{\varepsilon_0r^2}=18\pi$.")],
    "pg1": [_v(r"Boule pleine : $E=\frac{\rho_0R^3}{3\varepsilon_0r^2}$ pour $r > R$. $V(r)$ avec $V(\infty)=0$ (rho0, R, e0, r).", "-integrate(rho0*R**3/(3*e0*s**2),s).subs(s,r)", "rho0*R**3/(3*e0*r)", r"$V=\frac{\rho_0R^3}{3\varepsilon_0r}$ : potentiel d'une charge ponctuelle $Q=\frac43\pi R^3\rho_0$.")],
    "pg2": [_v(r"Même fil avec $\lambda=2$ nC·m$^{-1}$ : $V(0{,}1)-V(0{,}4)$ (V) ?", "integrate(2*9*10**9*2*10**-9/s,(s,Rational(1,10),Rational(4,10)))", "36*log(4)", r"$2k\lambda\ln\frac{0{,}4}{0{,}1}=36\ln4$ V.")],
    "pg3": [_v(r"Cylindre plein : $E=\frac{\rho r}{2\varepsilon_0}$ pour $r < R$. $V(r)$ à une constante près (rho0, e0, r).", "-integrate(rho0*s/(2*e0),s).subs(s,r)", "-rho0*r**2/(4*e0)", r"$V=-\frac{\rho r^2}{4\varepsilon_0}+C$.")],
    "pg4": [_v(r"$V(r)=-\frac\lambda{2\pi\varepsilon_0}\ln r$. Calculer $E_r$ (lam, e0, x).", "-diff(-lam*log(x)/(2*pi*e0),x)", "lam/(2*pi*e0*x)", r"$E_r=\frac\lambda{2\pi\varepsilon_0r}$ : on retrouve le champ du fil.")],
    "an1": [_v(r"Anneau $R=0{,}3$ m, $\lambda=2$ nC·m$^{-1}$, $z=0{,}4$ m. Champ (V·m$^{-1}$) ?", "9*10**9*2*10**-9*2*pi*Rational(3,10)*Rational(4,10)/(Rational(3,10)**2+Rational(4,10)**2)**Rational(3,2)", "864*pi/25", r"$R^2+z^2=0{,}25$ ; $E=\frac{18\times2\pi\times0{,}12}{0{,}125}=34{,}56\pi$.")],
    "an2": [_v(r"Mêmes données avec valeurs : $R=0{,}3$, $z=0{,}4$, $k\lambda=18$. Intégrer $dE_z=\frac{k\lambda Rz\,d\theta}{(R^2+z^2)^{3/2}}$ sur $[0,2\pi]$.", "integrate(18*Rational(3,10)*Rational(4,10)/(Rational(1,4))**Rational(3,2),(t,0,2*pi))", "864*pi/25", r"$\frac{18\times0{,}12}{0{,}125}=17{,}28$, puis $\times2\pi=34{,}56\pi$.")],
    "an3": [_v(r"$R=0{,}3$, $z=0{,}4$, $k\lambda=9$. Intégrer $dV=\frac{k\lambda R\,d\theta}{\sqrt{R^2+z^2}}$ sur $[0,2\pi]$.", "integrate(9*Rational(3,10)/sqrt(Rational(1,4)),(t,0,2*pi))", "54*pi/5", r"$\frac{9\times0{,}3}{0{,}5}=5{,}4$ puis $\times2\pi=10{,}8\pi$.")],
    "an4": [_v(r"Disque : $V(z)=\frac\sigma{2\varepsilon_0}\left(\sqrt{R^2+z^2}-z\right)$. $E_z=-\frac{dV}{dz}$ (sig, e0, R, z).", "-diff(sig*(sqrt(R**2+z**2)-z)/(2*e0),z)", "sig/(2*e0)*(1-z/sqrt(R**2+z**2))", r"$\frac d{dz}\sqrt{R^2+z^2}=\frac z{\sqrt{R^2+z^2}}$, donc $E_z=\frac\sigma{2\varepsilon_0}\left(1-\frac z{\sqrt{R^2+z^2}}\right)$.")],
    "an5": [_v(r"$\lim_{z\to\infty}zV(z)$ avec $V=\frac{2\pi k\lambda R}{\sqrt{R^2+z^2}}$ (lam, R, k).", "limit(z*2*pi*k*lam*R/sqrt(R**2+z**2),z,oo)", "2*pi*k*lam*R", r"$V\sim\frac{kQ}z$ avec $Q=2\pi R\lambda$.")],
    "an6": [_v(r"$q=1$ nC, $L=0{,}6$ m, $x=\frac L2$. Champ (V·m$^{-1}$) ?", "4*9*(Rational(6,10)/2)/((Rational(6,10)/2)**2+Rational(6,10)**2/2)**Rational(3,2)", "400*sqrt(3)/9", r"$E=\frac{16kq}{3\sqrt3L^2}=\frac{16\times9}{3\sqrt3\times0{,}36}=\frac{400\sqrt3}9\approx77$.")],
}
for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["id"] in VARIANTS:
            _e["variants"] = VARIANTS[_e["id"]]


def _q(notion, q, choix, bonne):
    return {"notion": notion, "type": "qcm", "q": q, "choix": choix, "bonne": bonne}


def _vf(notion, q, bonne):
    return {"notion": notion, "type": "vf", "q": q, "bonne": bonne}


QUIZ = [
    _vf("vect", r"Le produit scalaire de deux vecteurs orthogonaux est nul.", True),
    _q("vect", r"Le produit vectoriel $\vec u\wedge\vec v$ est :", [r"orthogonal à $\vec u$ et à $\vec v$", r"colinéaire à $\vec u$", r"un scalaire", r"toujours positif"], 0),
    _q("integ", r"L'élément de longueur d'un anneau de rayon $R$ est :", [r"$R\,d\theta$", r"$d\theta$", r"$R^2d\theta$", r"$dR$"], 0),
    _q("integ", r"L'élément de volume en coordonnées sphériques est :", [r"$r^2\sin\theta\,dr\,d\theta\,d\varphi$", r"$r\,dr\,d\theta\,d\varphi$", r"$dr\,d\theta\,d\varphi$", r"$r\sin\theta\,dr\,d\theta\,d\varphi$"], 0),
    _vf("integ", r"La densité surfacique de charge s'exprime en C·m$^{-2}$.", True),
    _q("coulomb", r"La force de Coulomb entre deux charges est multipliée par quoi si la distance est doublée ?", [r"$\frac14$", r"$\frac12$", r"$2$", r"$4$"], 0),
    _vf("coulomb", r"La force de Coulomb peut être attractive ou répulsive, contrairement à la force gravitationnelle.", True),
    _q("potentiel", r"Le potentiel d'une charge ponctuelle $q$ à la distance $r$ est :", [r"$\frac{kq}r$", r"$\frac{kq}{r^2}$", r"$\frac{kq^2}r$", r"$kqr$"], 0),
    _q("potentiel", r"La différence de potentiel entre $A$ et $B$ s'écrit :", [r"$V_B-V_A=-\int_A^B\vec E\cdot d\vec l$", r"$V_B-V_A=\int_A^B\vec E\cdot d\vec l$", r"$V_B-V_A=\vec E\,AB$", r"aucune des propositions précédentes"], 0),
    _vf("potentiel", r"La force électrostatique est conservative.", True),
    _q("lorentz", r"La force de Lorentz s'écrit :", [r"$q\vec E+q\vec v\wedge\vec B$", r"$q\vec E+q\vec v\cdot\vec B$", r"$q\vec v\wedge\vec E$", r"$q\vec B$"], 0),
    _vf("lorentz", r"La force magnétique modifie l'énergie cinétique de la particule.", False),
    _q("lorentz", r"Dans un champ $\vec B$ uniforme perpendiculaire à $\vec v$, la trajectoire est :", [r"un cercle parcouru à vitesse constante", r"une droite", r"une parabole", r"une spirale qui s'élargit"], 0),
    _q("oem", r"La célérité d'une onde se calcule par :", [r"$c=\lambda\times f$", r"$c=\lambda-f$", r"$c=\frac\lambda f$", r"$c=\frac f\lambda$"], 0),
    _q("oem", r"L'unité de la célérité est :", [r"le mètre par seconde", r"le mètre", r"la seconde", r"le hertz"], 0),
    _vf("oem", r"Pour une OPPM dans le vide, $B_0=\frac{E_0}c$ et $\vec E\perp\vec B$.", True),
    _q("symetrie", r"En un point d'un plan de symétrie de la distribution, le champ électrique est :", [r"contenu dans ce plan", r"perpendiculaire à ce plan", r"nul", r"quelconque"], 0),
    _vf("symetrie", r"Si la distribution est invariante par translation selon $Oz$, $\vec E$ ne dépend pas de $z$.", True),
    _q("symetrie", r"Un fil infini chargé uniformément est invariant par :", [r"rotation autour de l'axe et translation le long de l'axe", r"translation perpendiculaire à l'axe", r"aucune transformation", r"rotation autour d'un axe perpendiculaire"], 0),
    _q("flux", r"Le flux d'un champ radial $E(r)$ à travers une sphère de rayon $r$ est :", [r"$E(r)\,4\pi r^2$", r"$E(r)\,\pi r^2$", r"$E(r)\frac43\pi r^3$", r"$E(r)\,2\pi r$"], 0),
    _q("flux", r"Le flux d'un champ uniforme de norme $E$ qui forme un angle $\alpha$ avec la normale à un disque de rayon $R$ est :", [r"$\pi R^2E\cos\alpha$", r"$4\pi R^2E\cos\alpha$", r"$2\pi RE\cos\alpha$", r"$\pi R^2E$ quel que soit $\alpha$"], 0),
    _vf("flux", r"Le flux d'un champ uniforme à travers une surface fermée est nul.", True),
    _q("gauss", r"Le théorème de Gauss relie le flux de $\vec E$ à travers une surface fermée à :", [r"la charge intérieure divisée par $\varepsilon_0$", r"la charge surfacique de la surface", r"le nombre d'électrons qui la traversent", r"le flux à travers le volume"], 0),
    _vf("gauss", r"Les charges situées à l'extérieur de la surface de Gauss ne créent aucun champ.", False),
    _vf("gauss", r"La surface de Gauss doit passer par le point $M$ où l'on cherche le champ.", True),
    _q("gauss-cyl", r"Le champ d'un fil infini chargé avec $\lambda$ vaut :", [r"$\frac\lambda{2\pi\varepsilon_0r}$", r"$\frac\lambda{4\pi\varepsilon_0r^2}$", r"$\frac\lambda{2\varepsilon_0}$", r"$\frac{\lambda r}{2\varepsilon_0}$"], 0),
    _q("gauss-cyl", r"Le champ à l'intérieur d'un cylindre creux infini chargé en surface est :", [r"nul", r"non nul mais constant", r"proportionnel à $r$", r"inversement proportionnel à $r$"], 0),
    _vf("gauss-cyl", r"Le système de coordonnées adapté à un fil infini est cylindrique.", True),
    _q("gauss-plan", r"Le champ d'un plan infini de densité $\sigma$ est :", [r"$\frac\sigma{2\varepsilon_0}$", r"$\frac\sigma{\varepsilon_0}$", r"$\frac\sigma{4\pi\varepsilon_0}$", r"$\frac{\sigma}{2\pi\varepsilon_0z}$"], 0),
    _q("gauss-plan", r"La capacité d'un condensateur plan de surface $S$ et d'épaisseur $e$ est :", [r"$\frac{\varepsilon_0S}e$", r"$\frac{\varepsilon_0e}S$", r"$\varepsilon_0Se$", r"$\frac{eS}{\varepsilon_0}$"], 0),
    _vf("gauss-plan", r"Entre deux plans infinis chargés $+\sigma$ et $-\sigma$, le champ vaut $\frac\sigma{\varepsilon_0}$.", True),
    _q("gauss-sph", r"Pour une sphère uniformément chargée, on utilise de préférence les coordonnées :", [r"sphériques", r"cylindriques", r"polaires", r"cartésiennes"], 0),
    _q("gauss-sph", r"À l'extérieur d'une boule chargée, le champ est celui d'une charge ponctuelle :", [r"égale à la charge totale, placée au centre", r"nulle", r"égale à $\rho$, placée au centre", r"située sur la surface"], 0),
    _vf("gauss-sph", r"À l'intérieur d'une sphère creuse chargée en surface, le champ est nul.", True),
    _q("anneau", r"Par symétrie, le champ d'un anneau en un point de son axe est :", [r"porté par l'axe", r"perpendiculaire à l'axe", r"nul", r"orthoradial"], 0),
    _vf("anneau", r"Loin d'un anneau chargé, son champ se comporte comme celui d'une charge ponctuelle $Q=2\pi R\lambda$.", True),
]

_LEVEL_FORMULES = {
    1: r"$\|\vec u\|=\sqrt{u_x^2+u_y^2+u_z^2}$ · $\vec u\cdot\vec v=\sum u_iv_i$ · $\vec u\wedge\vec v$ · $E_x=E\cos\alpha$",
    2: r"$Q=\int\lambda\,dl=\iint\sigma\,dS=\iiint\rho\,d\tau$ · $dl=R\,d\theta$ · $dS=r\,dr\,d\theta$ · $d\tau=r^2\sin\theta\,dr\,d\theta\,d\varphi$",
    3: r"$F=k\frac{q_1q_2}{r^2}$ · $E=k\frac q{r^2}$ · $\vec E_{tot}=\sum\vec E_i$ · projection $\cos\alpha$",
    4: r"$V=\sum k\frac{q_i}{r_i}$ · $E_p=qV$ · $E_{pe}=\sum k\frac{q_iq_j}{r_{ij}}$ · $E_r=-\frac{dV}{dr}$",
    5: r"$\vec F=q\vec E+q\vec v\wedge\vec B$ · $R=\frac{mv}{|q|B}$ · $\frac12mv^2=qU$ · $R\propto m$",
    6: r"$c=\lambda f=\frac\omega k$ · $k=\frac{2\pi}\lambda$ · $B_0=\frac{E_0}c$ · $\frac{\partial E}{\partial x}=-\frac{\partial B}{\partial t}$",
    7: r"plan de symétrie : $\vec E\in\Pi$ · antisymétrie : $\vec E\perp\Pi^*$ · invariance : pas de dépendance",
    8: r"$\Phi=\iint\vec E\cdot d\vec S$ · $\Phi=ES\cos\alpha$ · $4\pi r^2$ · $2\pi rh$",
    9: r"$\oiint\vec E\cdot d\vec S=\frac{Q_{int}}{\varepsilon_0}$ · $\varepsilon_0=\frac1{4\pi k}$",
    10: r"$\oiint\vec E\cdot d\vec S=\frac{Q_{int}}{\varepsilon_0}$ · $E\,2\pi rh=\frac{Q_{int}}{\varepsilon_0}$ · $E=\frac\lambda{2\pi\varepsilon_0r}$",
    11: r"$E\,2\pi rh=\frac{Q_{int}}{\varepsilon_0}$ · $d\tau=r\,dr\,d\theta\,dz$ · continuité de $E$",
    12: r"$2ES=\frac{\sigma S}{\varepsilon_0}$ · $E=\frac\sigma{2\varepsilon_0}$ · $U=Ee$ · $C=\frac{\varepsilon_0S}e$",
    13: r"$E\,4\pi r^2=\frac{Q_{int}}{\varepsilon_0}$ · $Q_{int}=\int\rho\,4\pi s^2ds$ · $\frac43\pi R^3$",
    14: r"$E_r=-\frac{dV}{dr}$ · $V=-\int E\,dr+C$ · $V(r_1)-V(r_2)=\int_{r_1}^{r_2}E\,dr$",
    15: r"$dE_z=dE\cos\alpha$ · $E_z=\frac{2\pi k\lambda Rz}{(R^2+z^2)^{3/2}}$ · $V=\frac{2\pi k\lambda R}{\sqrt{R^2+z^2}}$ · $E_z=-\frac{dV}{dz}$",
    16: r"$E=\frac{kq}{r^2}$ · $V=\sum\frac{kq_i}{r_i}$ · $\vec F=q\vec v\wedge\vec B$ · $R=\frac{mv}{qB}$",
    17: r"$\oiint\vec E\cdot d\vec S=\frac{Q_{int}}{\varepsilon_0}$ · $E_z=-\frac{dV}{dz}$ · continuité de $E$",
    18: r"$\oiint\vec E\cdot d\vec S=\frac{Q_{int}}{\varepsilon_0}$ · saut de $E$ : $\frac\sigma{\varepsilon_0}$ · $V=-\int E\,dr$ · superposition",
}
FORMULES = {e["id"]: _LEVEL_FORMULES[lvl["n"]] for lvl in LEVELS for e in lvl["exos"] if e["kind"] != "multi"}
FORMULES.update({
    "lo6": r"$\vec F_{mag}\cdot\vec v=0$ · $E_c=qU$",
    "cv5": r"$Q_{int}=\rho_0\pi R_1^2h+Q$ · $E\,2\pi rh=\frac{Q_{int}}{\varepsilon_0}$",
    "x1a": r"$E=\frac{kq}{d^2}$ avec $d=a\sqrt2$", "x1b": r"$E_x=\sum E_i\cos\alpha_i$ · $\cos45^\circ=\frac{\sqrt2}2$", "x1c": r"$E=\sqrt{E_x^2+E_y^2}$ · symétrie par rapport à $AC$",
    "x2o": r"$\vec F=q\vec E$ · $q > 0$", "x2b": r"$\vec F=q\vec v\wedge\vec B$ · $\vec e_x\wedge\vec e_z=-\vec e_y$", "x2a": r"$m\frac{v^2}R=|q|vB$ · $R=\frac{mv}{|q|B}$",
    "x3a": r"$E_i=\frac{kq_i}{(a/\sqrt2)^2}$ · superposition vectorielle", "x3b": r"$V=\sum\frac{kq_i}{r_i}$", "x3c": r"$E_p=qV$",
    "sy6": r"plans de symétrie · invariance par rotation",
    "x4b": r"$E\,4\pi r^2=\frac{Q_{int}}{\varepsilon_0}$ · $Q_{int}=\int\rho\,4\pi s^2ds$", "x4c": r"continuité de $E$ en $R$", "x4d": r"$E_r=-\frac{dV}{dr}$",
    "x5b": r"$E\,2\pi rh=\frac{Q_{int}}{\varepsilon_0}$ · $Q_{int}=\rho_0\pi R_1^2h$", "x5c": r"$E\,2\pi rh=\frac{Q_{int}}{\varepsilon_0}$ · $Q_{int}=\rho_0\pi r^2h$",
    "x6b": r"$E_i=\frac{2\pi k\lambda_iR_iz}{(R_i^2+z^2)^{3/2}}$ · superposition", "x6c": r"$V=\sum\frac{2\pi k\lambda_iR_i}{\sqrt{R_i^2+z^2}}$", "x6d": r"limite · neutralité",
    "x7b": r"$E\,4\pi r^2=\frac{Q_{int}}{\varepsilon_0}$ · $Q_{int}=4\pi\rho_0\left(\frac{r^3}3-\frac{r^5}{5a^2}\right)$", "x7c": r"$Q_{int}=Ze$ · $E=\frac{Ze}{4\pi\varepsilon_0r^2}$", "x7d": r"continuité de $E$ en $a$",
    "x8a": r"$E\,2\pi rh=\frac{\lambda h}{\varepsilon_0}$", "x8b": r"$E\,2\pi rh=\frac{\lambda h+Q}{\varepsilon_0}$", "x8c": r"saut de $E$ : $\frac\sigma{\varepsilon_0}$", "x8d": r"$V=-\int E\,dr$",
})
