"""Level path: S3 physics, introduction to quantum physics (Planck, photoelectric effect, Bohr, de Broglie, Heisenberg,
wave function, Schrödinger equation in an infinite well, superposition, qubits).

Moodle course « Introduction à la Physique Quantique » : `01_Cours et TD` (Cours_quantique_V6, TD1 « La quantification »,
TD2 « Principe d'indétermination et fonction d'onde », TD3 « Équation de Schrödinger »). The `04_QCM` pages only list the
topics of the tests (boundary conditions of the Schrödinger solution) and have no questions, so nothing is taken from them.
Calibrated on the only exam of the folder about quantum mechanics: « Examen Physique : Mécanique quantique » (décembre 2023,
`annales/raw/S3/Finals/Phys/2027`, scan, with a corrigé): ex. 1 questions de cours, ex. 2 Bohr model for hydrogenoids,
ex. 3 particle in a 1D then 2D box. The other S3 physics exams of `annales/raw/S3` are about electrostatics (Gauss, potential)
and are not used. Levels 1 and 2 are reminders of S1/S2 (energy, waves, units, Coulomb force and circular motion).
Numerical conventions follow the course: h = 6,6.10^-34 J.s, c = 3.10^8 m/s, 1 eV = 1,6.10^-19 J, m_e = 9.10^-31 kg
(9,1.10^-31 kg in TD2), hc = 1240 eV.nm (1200 eV.nm in the course example), E_1 = -13,6 eV.
`value` and `integral` exercises are checked by sympy; `open` ones have a model answer.
"""

SUBJECT = {
    "id": "physique-s3-quantique",
    "ordre": 340,
    "matiere": "physique",
    "semestre": "S3",
    "ecue": "QUANT",
    "titre": "Introduction à la physique quantique",
    "chapitres_moodle": ["01_Cours et TD", "04_QCM"],
    "td": "TD1, TD2, TD3 de mécanique quantique",
    "examens": ["Examen Physique : Mécanique quantique (décembre)"],
}

NOTIONS = [
    {"id": "rappels", "titre": "Rappels : énergie, ondes, unités",
     "formule": r"$E_c=\frac12mv^2$ · $p=mv$ · $c=\lambda f$ · 1 eV $=1{,}6\times10^{-19}$ J · 1 nm $=10^{-9}$ m",
     "exemple": r"un électron de $2\times10^6$ m/s : $E_c=\frac12\times9\times10^{-31}\times(2\times10^6)^2=1{,}8\times10^{-18}$ J $\approx11{,}25$ eV",
     "cours": r"Toujours convertir en unités SI (m, kg, s, J) avant de calculer, ou travailler en eV et en nm pour les photons. Une corde fixée aux deux extrémités ne vibre que sur des fréquences discrètes : c'est le premier exemple de quantification, repris par de Broglie."},
    {"id": "coulomb", "titre": "Rappels : force de Coulomb et mouvement circulaire",
     "formule": r"$F=\dfrac{kq_1q_2}{r^2}$ · $k=9\times10^9$ · $a=\dfrac{v^2}r$ (cercle, $v$ constant) · $\sum\vec F=m\vec a$ · on pose $e^2=kq^2$",
     "exemple": r"électron et proton à $r=5\times10^{-11}$ m : $F=\frac{9\times10^9\times(1{,}6\times10^{-19})^2}{r^2}\approx9{,}2\times10^{-8}$ N",
     "cours": r"Mouvement circulaire uniforme : l'accélération est centripète, de norme $\frac{v^2}r$. Pour l'électron de l'atome, la seule force est l'attraction de Coulomb : $\frac{ke^2}{r^2}\to\frac{mv^2}r=\frac{e^2}{r^2}$ avec $e^2=kq^2$. Énergie : $E_c=\frac{e^2}{2r}$, $E_p=-\frac{e^2}r$."},
    {"id": "photon", "titre": "Photon et corps noir",
     "formule": r"$E=h\nu=\dfrac{hc}\lambda$ · $h=6{,}6\times10^{-34}$ J·s · $hc\approx1240$ eV·nm · $\Delta E=|E_f-E_i|=\dfrac{hc}\lambda$",
     "exemple": r"$\lambda=620$ nm : $E=\frac{1240}{620}=2$ eV",
     "cours": r"Le rayonnement du corps noir ne dépend que de la température. Classiquement, l'énergie rayonnée diverge en $\frac1{\lambda^4}$ vers l'ultraviolet (catastrophe ultraviolette). Planck (1900) suppose que l'énergie est échangée par paquets $E=h\nu$ (quanta), ce qui reproduit la mesure. Le spectre est la densité d'énergie rayonnée en fonction de $\lambda$."},
    {"id": "photoelec", "titre": "Effet photoélectrique",
     "formule": r"$E_c=h\nu-W=\dfrac{hc}\lambda-W$ · seuil : $h\nu_s=W$, $\lambda_s=\dfrac{hc}W$ · aucun électron si $h\nu < W$ quelle que soit l'intensité",
     "exemple": r"$\lambda=300$ nm ($hc=1200$ eV·nm), $E_c=1$ eV : $W=\frac{1200}{300}-1=3$ eV",
     "cours": r"Einstein (1905) : la lumière est faite de photons d'énergie $h\nu$, absorbés un par un. Si l'énergie d'un photon dépasse le travail d'extraction $W$ du métal, l'électron sort avec l'énergie cinétique $E_c=h\nu-W$. L'intensité règle le nombre de photons, donc le nombre d'électrons, pas leur énergie. Dans l'exemple du cours, $E_c=\frac12m_ec^2\left(\frac vc\right)^2$ avec $m_ec^2\approx0{,}5$ MeV."},
    {"id": "bohr", "titre": "Modèle de Bohr : niveaux d'énergie",
     "formule": r"$m r v=n\hbar$ · $E_n=\dfrac{E_1}{n^2}$, $E_1=-13{,}6$ eV · $h\nu=E_i-E_f=E_1\left(\dfrac1{n_i^2}-\dfrac1{n_f^2}\right)$ · ionisation depuis $n=1$ : $13{,}6$ eV",
     "exemple": r"$3\to2$ : $\Delta E=13{,}6\left(\frac14-\frac19\right)=1{,}89$ eV, $\lambda=\frac{1240}{1{,}89}\approx656$ nm (rouge, série de Balmer)",
     "cours": r"Postulats : orbites circulaires stables sans rayonnement, moment cinétique quantifié $mrv=n\hbar$, saut entre couches par absorption ou émission d'un photon. Les énergies sont négatives, $0$ correspond à l'atome ionisé ($n\to\infty$). Émission : $n_i>n_f$ ; absorption : $n_i < n_f$. Balmer : $n_f=2$ (visible). Un photon d'énergie supérieure à $13{,}6$ eV ionise : l'excédent devient énergie cinétique."},
    {"id": "hydrogenoide", "titre": "Hydrogénoïdes : rayons et énergies",
     "formule": r"$r_n=\dfrac{n^2\hbar^2}{Zme^2}=\dfrac{n^2a_0}Z$ · $E_n=-\dfrac{Z^2me^4}{2\hbar^2n^2}=-13{,}6\dfrac{Z^2}{n^2}$ eV · $a_0=\dfrac{\hbar^2}{me^2}\approx5\times10^{-11}$ m",
     "exemple": r"$\mathrm{He}^+$ ($Z=2$) : $r_1=\frac{a_0}2=2{,}5\times10^{-11}$ m, $E_1=-4\times13{,}6=-54{,}4$ eV",
     "cours": r"Un hydrogénoïde est un ion à un seul électron et $Z$ protons. Coulomb : $\frac{Ze^2}{r^2}$. PFD avec $a=\frac{v^2}r$ : $mv^2=\frac{Ze^2}r$. Avec $mrv=n\hbar$ : $(mv)^2=\frac{n^2\hbar^2}{r^2}=\frac{Zme^2}r$, d'où $r_n$. Énergie : $E_n=E_c+E_p=-\frac{Ze^2}{2r_n}$. Plus $Z$ est grand, plus l'électron est proche et lié."},
    {"id": "debroglie", "titre": "Dualité onde-particule et longueur de de Broglie",
     "formule": r"$\lambda=\dfrac hp=\dfrac h{mv}$ · $h=6{,}62\times10^{-34}$ J·s · $\hbar=\dfrac h{2\pi}$",
     "exemple": r"balle de tennis, $0{,}05$ kg à $95$ m/s : $\lambda=\frac{6{,}62\times10^{-34}}{0{,}05\times95}\approx1{,}4\times10^{-34}$ m, inobservable",
     "cours": r"Toute particule a une longueur d'onde associée. Elle n'est observable que si elle est comparable aux distances en jeu : électrons (diffraction de Davisson et Germer, fentes d'Young avec électrons), pas objets macroscopiques. La lumière aussi est onde et particule (fentes d'Young avec photons un par un)."},
    {"id": "heisenberg", "titre": "Principe d'indétermination d'Heisenberg",
     "formule": r"$\Delta x\,\Delta p\geq\dfrac\hbar2$ · $p=mv$, $\Delta p=m\,\Delta v$ · $(\Delta A)^2=\langle A^2\rangle-\langle A\rangle^2$",
     "exemple": r"électron localisé à $\Delta x=10^{-10}$ m : $\Delta p\geq\frac\hbar{2\Delta x}\approx5\times10^{-25}$ kg·m·s$^{-1}$",
     "cours": r"Position et quantité de mouvement ne peuvent pas être connues simultanément avec précision : ce n'est pas un défaut de mesure mais une propriété de la matière. Plus on confine une particule, plus l'indétermination sur sa vitesse est grande. Pour un objet macroscopique les valeurs sont négligeables."},
    {"id": "psi", "titre": "Fonction d'onde et probabilité de présence",
     "formule": r"densité : $|\psi(x)|^2$ · $P(a:b)=\displaystyle\int_a^b|\psi|^2dx$ · normalisation : $\displaystyle\int_{-\infty}^{+\infty}|\psi|^2dx=1$",
     "exemple": r"$\psi=\Psi_0e^{-x/x_0}$ sur $[0;+\infty[$ : $\Psi_0^2\frac{x_0}2=1$ donc $\Psi_0=\sqrt{\frac2{x_0}}$",
     "cours": r"Born (1926) : $\psi$ est une onde de probabilité. $|\psi|^2$ est une densité de probabilité (par unité de longueur) : on l'intègre pour obtenir une probabilité. La particule étant quelque part, l'intégrale sur tout l'espace vaut $1$ : c'est ce qui fixe la constante de normalisation. Pour $P\geq95\%$ sur $[0;A]$, on résout $1-e^{-2A/x_0}\geq0{,}95$."},
    {"id": "moyennes", "titre": "Valeurs moyennes et incertitudes",
     "formule": r"$\langle x\rangle=\displaystyle\int x|\psi|^2dx$ · $\langle A\rangle=\displaystyle\int\psi^*\hat A\psi\,dx$ · $\hat p=-i\hbar\dfrac d{dx}$ · $\langle p^2\rangle=\hbar^2\displaystyle\int|\psi'|^2dx$ · $(\Delta A)^2=\langle A^2\rangle-\langle A\rangle^2$",
     "exemple": r"$\psi=Ne^{-\lambda x^2/2}$ : $N=\left(\frac\lambda\pi\right)^{1/4}$, $\langle x^2\rangle=\frac1{2\lambda}$, $\langle p^2\rangle=\frac{\hbar^2\lambda}2$, $\Delta x\,\Delta p=\frac\hbar2$",
     "cours": r"Intégrales utiles : $\int_{-\infty}^{+\infty}e^{-\lambda x^2}dx=\sqrt{\frac\pi\lambda}$ et $\int_{-\infty}^{+\infty}x^2e^{-\lambda x^2}dx=\frac1{2\lambda}\sqrt{\frac\pi\lambda}$. Une fonction d'onde paire donne $\langle x\rangle=0$ ($x|\psi|^2$ est impaire). Pour $\psi$ réelle, $\langle p\rangle=-i\hbar\int\psi\psi'dx=0$. La gaussienne atteint exactement la borne d'Heisenberg."},
    {"id": "schrodinger", "titre": "Équation de Schrödinger et puits infini 1D",
     "formule": r"$-\dfrac{\hbar^2}{2m}\psi''+V\psi=E\psi$ · puits : $\psi(0)=\psi(L)=0$ · $\psi_n=\sqrt{\dfrac2L}\sin\dfrac{n\pi x}L$ · $E_n=\dfrac{n^2\pi^2\hbar^2}{2mL^2}=n^2E_1$",
     "exemple": r"électron dans $L=1$ nm : $E_1=\frac{h^2}{8mL^2}\approx0{,}38$ eV",
     "cours": r"Dans $[0;L]$ ($V=0$) : $\psi''=-k^2\psi$ avec $k^2=\frac{2mE}{\hbar^2}$, soit $\psi=A\sin kx+B\cos kx$. $\psi(0)=0$ donne $B=0$ ; $\psi(L)=0$ donne $kL=n\pi$ avec $n\geq1$ ($n=0$ est la solution nulle) : l'énergie est quantifiée. La normalisation donne $A=\sqrt{\frac2L}$. $\psi_n$ a $n-1$ n{\oe}uds."},
    {"id": "superposition", "titre": "Superposition d'états et énergie moyenne",
     "formule": r"$\psi=\sum c_n\psi_n$ · $c_n=\displaystyle\int\psi_n^*\psi\,dx$ · $\displaystyle\int\psi_n^*\psi_m=\delta_{nm}$ · $\sum|c_n|^2=1$ · $\langle E\rangle=\sum|c_n|^2E_n$",
     "exemple": r"$\psi=N(3\psi_1-\psi_3)$ : $N^2=\frac1{10}$, $P_1=\frac9{10}$, $P_3=\frac1{10}$, $\langle E\rangle=\frac95E_1$",
     "cours": r"Les $\psi_n$ forment une base orthonormée : $\int\psi_n\psi_m=\delta_{nm}$ (relation $\sin a\sin b=\frac12[\cos(a-b)-\cos(a+b)]$). La normalisation de $\psi$ devient $\sum|c_n|^2=1$ ; $|c_n|^2$ est la probabilité de trouver l'énergie $E_n$. Pour $\sin^3u=\frac14(3\sin u-\sin3u)$, seuls $n=1$ et $n=3$ interviennent."},
    {"id": "boite2d", "titre": "Boîte 2D et dégénérescence",
     "formule": r"$E_{n_x,n_y}=\dfrac{\hbar^2\pi^2}{2m}\left(\dfrac{n_x^2}{a^2}+\dfrac{n_y^2}{b^2}\right)$ · $n_x,n_y\geq1$ · carré $a=b=1$ : $E_{min}=\dfrac{\hbar^2\pi^2}m$",
     "exemple": r"carré : $E_{4,1}=E_{1,4}=\frac{\hbar^2\pi^2}{2m}\times17=\frac{17}2E_{min}$ (sixième niveau)",
     "cours": r"Chaque direction est quantifiée. L'énergie minimale n'est pas nulle (énergie de point zéro) : contraire à la mécanique classique, c'est l'indétermination d'Heisenberg (particule confinée donc $\Delta p\neq0$). Deux états différents de même énergie, comme $(2,1)$ et $(1,2)$ dans un carré, sont dits dégénérés. Pour compter les niveaux, lister les sommes $n_x^2+n_y^2$ dans l'ordre : $2,5,8,10,13,17,18,\dots$"},
    {"id": "qubit", "titre": "Qubits et portes quantiques",
     "formule": r"$|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$, $|\alpha|^2+|\beta|^2=1$ · mesure : $|0\rangle$ avec $|\alpha|^2$, $|1\rangle$ avec $|\beta|^2$ · $X$ : $|0\rangle\leftrightarrow|1\rangle$ · $H|0\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2}$, $H|1\rangle=\frac{|0\rangle-|1\rangle}{\sqrt2}$ · CNOT · $n$ qubits : $2^n$ coefficients",
     "exemple": r"$|\psi\rangle=\frac35|0\rangle+\frac45|1\rangle$ : $P(0)=\frac9{25}$, $P(1)=\frac{16}{25}$",
     "cours": r"Avec $|0\rangle=\binom10$ et $|1\rangle=\binom01$ (base orthonormée), une porte est une matrice : $X=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, $H=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$. CNOT inverse le second qubit si le premier vaut $|1\rangle$ : sur $(\alpha,\beta,\gamma,\delta)$ dans l'ordre $|00\rangle,|01\rangle,|10\rangle,|11\rangle$, elle échange $\gamma$ et $\delta$. Une mesure donne un seul résultat, avec les probabilités $|\text{coefficient}|^2$."},
]


def v(id, enonce, calc, ans, sol, src=None, duree=None):
    e = {"id": id, "kind": "value", "enonce": enonce, "calc": calc, "ans": ans, "sol": sol}
    if src:
        e["src"] = src
    if duree:
        e["duree"] = duree
    return e


def itg(id, enonce, f, a, b, ans, sol, src=None, duree=None):
    e = {"id": id, "kind": "integral", "enonce": enonce, "f": f, "a": a, "b": b, "ans": ans, "sol": sol}
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


EX = "Examen Physique : Mécanique quantique (décembre 2023)"
TD1 = "TD1 de mécanique quantique"
TD2 = "TD2 de mécanique quantique"
TD3 = "TD3 de mécanique quantique"
COURS = "Cours de mécanique quantique"

LEVELS = [
    {"n": 1, "titre": "Rappels S1/S2 : énergie, ondes, unités", "notions": ["rappels"], "exos": [
        v("qa1", r"Une balle de $0{,}05$ kg lancée à $95$ m/s. Énergie cinétique (en J) ?", "Rational(1,2)*Rational(5,100)*95**2", "1805/8",
          r"$E_c=\frac12mv^2=\frac12\times0{,}05\times95^2=225{,}625$ J.", src=TD2 + ", ex. 1 (données)", duree=2),
        v("qa2", r"Convertir l'énergie d'ionisation de l'hydrogène, $13{,}6$ eV, en joules ($1$ eV $=1{,}6\times10^{-19}$ J).", "Rational(136,10)*Rational(16,10)*10**-19", "2176*10**-21",
          r"$13{,}6\times1{,}6\times10^{-19}=21{,}76\times10^{-19}=2{,}176\times10^{-18}$ J.", src=COURS + ", exemple 1 (unités)", duree=2),
        v("qa3", r"Une onde lumineuse de fréquence $f=5\times10^{14}$ Hz se propage à $c=3\times10^8$ m/s. Longueur d'onde (en nm) ?", "3*10**8/(5*10**14)*10**9", "600",
          r"$\lambda=\frac cf=\frac{3\times10^8}{5\times10^{14}}=6\times10^{-7}$ m $=600$ nm (orange).", duree=2),
        v("qa4", r"Un électron ($m=9\times10^{-31}$ kg) va à $2\times10^6$ m/s. Énergie cinétique (en eV) ?", "Rational(1,2)*9*10**-31*(2*10**6)**2/(Rational(16,10)*10**-19)", "45/4",
          r"$E_c=\frac12\times9\times10^{-31}\times4\times10^{12}=1{,}8\times10^{-18}$ J, soit $\frac{1{,}8\times10^{-18}}{1{,}6\times10^{-19}}=11{,}25$ eV.", duree=3),
        o("qa5", r"Une corde de longueur $L$, fixée à ses deux extrémités, vibre en onde stationnaire. Quelles longueurs d'onde sont possibles ? Pourquoi dit-on que la fréquence est « quantifiée » ?",
          r"Chaque extrémité est un n{\oe}ud, donc $L$ contient un nombre entier de demi-longueurs d'onde : $L=n\frac\lambda2$, soit $\lambda_n=\frac{2L}n$ ($n=1,2,3,\dots$). Avec $c=\lambda f$, $f_n=n\frac c{2L}$ : seules des fréquences discrètes sont permises (les notes d'une corde de guitare). C'est cette idée que de Broglie transpose à l'électron, et que l'on retrouve dans le puits de potentiel infini.", duree=3),
    ]},
    {"n": 2, "titre": "Rappels : force de Coulomb et mouvement circulaire", "notions": ["coulomb"], "exos": [
        v("qc1", r"Force de Coulomb (en N) entre un proton et un électron distants de $r=5\times10^{-11}$ m ($k=9\times10^9$, $q=1{,}6\times10^{-19}$ C) ?", "9*10**9*(Rational(16,10)*10**-19)**2/(5*10**-11)**2", "9216*10**-11",
          r"$F=\frac{kq^2}{r^2}=\frac{9\times10^9\times2{,}56\times10^{-38}}{25\times10^{-22}}=9{,}216\times10^{-8}$ N.", src=TD1 + ", ex. 1 q2", duree=3),
        v("qc2", r"Un électron décrit un cercle de rayon $r=5\times10^{-11}$ m à la vitesse constante $v=2{,}2\times10^6$ m/s. Norme de son accélération (en m·s$^{-2}$) ?", "(Rational(22,10)*10**6)**2/(5*10**-11)", "968*10**20",
          r"Mouvement circulaire uniforme : $a=\frac{v^2}r=\frac{4{,}84\times10^{12}}{5\times10^{-11}}=9{,}68\times10^{22}$ m·s$^{-2}$ (centripète).", src=EX + ", ex. 2", duree=3),
        v("qc3", r"Le PFD donne $mv^2=\frac{kq^2}r$. Calculer $mv^2$ (en J) pour $r=5\times10^{-11}$ m.", "9*10**9*(Rational(16,10)*10**-19)**2/(5*10**-11)", "4608*10**-21",
          r"$mv^2=\frac{kq^2}r=\frac{2{,}304\times10^{-28}}{5\times10^{-11}}=4{,}608\times10^{-18}$ J.", src=TD1 + ", ex. 1 q3", duree=3),
        v("qc4", r"Énergie cinétique de cet électron $E_c=\frac12mv^2=\frac{kq^2}{2r}$ (en eV), pour $r=5\times10^{-11}$ m ?", "9*10**9*(Rational(16,10)*10**-19)**2/(2*5*10**-11)/(Rational(16,10)*10**-19)", "72/5",
          r"$E_c=\frac{2{,}304\times10^{-28}}{10^{-10}}=2{,}304\times10^{-18}$ J, soit $\frac{2{,}304\times10^{-18}}{1{,}6\times10^{-19}}=14{,}4$ eV.", duree=4),
        o("qc5", r"Électron de l'atome d'hydrogène en orbite circulaire de rayon $r$. Avec $e^2=kq^2$, établir $E_c$, $E_p$ puis l'énergie totale $E$ en fonction de $e$ et $r$.",
          r"PFD : $\frac{e^2}{r^2}=\frac{mv^2}r$ donc $mv^2=\frac{e^2}r$ et $E_c=\frac12mv^2=\frac{e^2}{2r}$." "\n\n"
          r"Énergie potentielle de Coulomb (interaction proton-électron) : $E_p=-\frac{kq^2}r=-\frac{e^2}r$." "\n\n"
          r"Total : $E=E_c+E_p=\frac{e^2}{2r}-\frac{e^2}r=-\frac{e^2}{2r}$. Elle est négative : l'électron est lié, et on retrouve $E=-E_c$.", src=TD1 + ", ex. 1 q5", duree=5),
    ]},
    {"n": 3, "titre": "Photon et corps noir", "notions": ["photon"], "exos": [
        v("qp1", r"Énergie (en eV) d'un photon de longueur d'onde $620$ nm ($hc\approx1240$ eV·nm) ?", "1240/620", "2", r"$E=\frac{hc}\lambda=\frac{1240}{620}=2$ eV.", duree=2),
        v("qp2", r"Fréquence d'un photon d'énergie $3{,}3\times10^{-19}$ J ($h=6{,}6\times10^{-34}$ J·s) ?", "Rational(33,10)*10**-19/(Rational(66,10)*10**-34)", "5*10**14",
          r"$\nu=\frac Eh=\frac{3{,}3\times10^{-19}}{6{,}6\times10^{-34}}=5\times10^{14}$ Hz.", duree=2),
        v("qp3", r"Un laser de $1$ mW émet à $660$ nm. Nombre de photons émis par seconde ? ($h=6{,}6\times10^{-34}$, $c=3\times10^8$)", "Rational(1,1000)/(Rational(66,10)*10**-34*3*10**8/(Rational(66,10)*10**-7))", "10**16/3",
          r"Un photon : $E=\frac{hc}\lambda=\frac{6{,}6\times10^{-34}\times3\times10^8}{6{,}6\times10^{-7}}=3\times10^{-19}$ J. Nombre par seconde : $\frac{P}E=\frac{10^{-3}}{3\times10^{-19}}\approx3{,}3\times10^{15}$.", duree=4),
        o("qp4", r"La longueur d'onde du photon associé à une transition entre les niveaux $n=3$ et $n'=2$ vaut-elle $\lambda=hc\,|\Delta E_{3\to2}|$, $hc\,\Delta E_{3\to2}$, $\dfrac{hc}{|\Delta E_{3\to2}|}$ ou $\dfrac{hc}{\Delta E_{3\to2}}$ ? Justifier.",
          r"Réponse : $\lambda=\dfrac{hc}{|\Delta E_{3\to2}|}$. L'énergie du photon est $h\nu=\frac{hc}\lambda=|E_f-E_i|$. On prend la valeur absolue car $\Delta E$ est négatif pour une émission alors que $\lambda$ doit être positive. Les propositions avec $hc\times\Delta E$ ne sont pas homogènes à une longueur.", src=EX + ", ex. 1 q3", duree=3),
        o("qp5", r"Le spectre du rayonnement d'un corps noir est le graphe de : (a) la densité d'énergie rayonnée en fonction de la température $T$ ; (b) $T$ en fonction de la densité d'énergie ; (c) la densité d'énergie rayonnée en fonction de la longueur d'onde $\lambda$ ; (d) aucune. Que prédisait la physique classique aux petites longueurs d'onde, et comment Planck a-t-il résolu le problème ?",
          r"Réponse : (c). Un spectre représente l'énergie rayonnée en fonction de $\lambda$, à $T$ fixée ; sa forme ne dépend que de $T$, pas du matériau." "\n\n"
          r"La théorie classique prédit une densité d'énergie qui diverge en $\frac1{\lambda^4}$ quand $\lambda\to0$ (vers l'ultraviolet) : c'est la catastrophe ultraviolette, absurde puisqu'elle donnerait une énergie infinie." "\n\n"
          r"Planck (1900) suppose que l'énergie ne s'échange que par paquets $E=h\nu$ : la divergence disparaît et la courbe mesurée est reproduite.", src=EX + ", ex. 1 q5", duree=5),
    ]},
    {"n": 4, "titre": "Effet photoélectrique", "notions": ["photoelec", "photon"], "exos": [
        v("qe1", r"Un métal éclairé à $\lambda=300$ nm émet des électrons de vitesse $6\times10^5$ m/s. On prend $hc\approx1200$ eV·nm et $m_ec^2\approx0{,}5$ MeV. Travail d'extraction $W$ (en eV) ?", "Rational(1200,300)-Rational(1,2)*500000*(6*10**5/Rational(3*10**8))**2", "3",
          r"$h\nu=\frac{1200}{300}=4$ eV. $E_c=\frac12m_ec^2\left(\frac vc\right)^2=\frac12\times5\times10^5\times(2\times10^{-3})^2=1$ eV. $W=h\nu-E_c=3$ eV.", src=COURS + ", exemple 1", duree=5),
        v("qe2", r"Travail d'extraction du métal $W=2{,}5$ eV. Longueur d'onde seuil $\lambda_s$ (en nm), avec $hc=1240$ eV·nm ?", "1240/Rational(5,2)", "496",
          r"Seuil : $h\nu_s=\frac{hc}{\lambda_s}=W$, donc $\lambda_s=\frac{1240}{2{,}5}=496$ nm. Au-delà, aucun électron n'est émis, même très intense.", duree=3),
        v("qe3", r"Lumière à $200$ nm sur un métal de travail d'extraction $4{,}2$ eV ($hc=1240$ eV·nm). Énergie cinétique des électrons (en eV) ?", "1240/200-Rational(42,10)", "2",
          r"$E_c=\frac{hc}\lambda-W=\frac{1240}{200}-4{,}2=6{,}2-4{,}2=2$ eV.", duree=3),
        v("qe4", r"Un électron émis a l'énergie cinétique $1{,}8$ eV. Sa vitesse (en m/s), avec $m=9\times10^{-31}$ kg ?", "sqrt(2*Rational(18,10)*Rational(16,10)*10**-19/(9*10**-31))", "8*10**5",
          r"$E_c=1{,}8\times1{,}6\times10^{-19}=2{,}88\times10^{-19}$ J. $v=\sqrt{\frac{2E_c}m}=\sqrt{\frac{5{,}76\times10^{-19}}{9\times10^{-31}}}=\sqrt{6{,}4\times10^{11}}=8\times10^5$ m/s.", duree=4),
        o("qe5", r"On éclaire un métal avec une lumière de fréquence inférieure au seuil, mais très intense. Observe-t-on des électrons ? Pourquoi la théorie ondulatoire classique ne l'explique-t-elle pas ?",
          r"Non, aucun. Chaque électron absorbe un seul photon d'énergie $h\nu$ ; si $h\nu < W$, il ne sort pas, et augmenter l'intensité ajoute des photons sans augmenter l'énergie de chacun." "\n\n"
          r"Une onde classique continue donnerait de l'énergie aux électrons proportionnellement à l'intensité : une intensité assez forte les ferait sortir, et la fréquence ne ferait que changer le temps nécessaire. Cela contredit l'observation d'un seuil en fréquence. Einstein (1905) explique : $E_c=h\nu-W$.", src=COURS + ", II.2", duree=4),
    ]},
    {"n": 5, "titre": "Modèle de Bohr : niveaux d'énergie", "notions": ["bohr", "photon"], "exos": [
        v("qb1", r"Énergie du niveau $n=3$ de l'atome d'hydrogène (en eV), $E_1=-13{,}6$ eV ?", "-Rational(136,10)/9", "-68/45", r"$E_3=\frac{E_1}{9}=-\frac{13{,}6}9\approx-1{,}51$ eV.", src=EX + ", ex. 1 (document 1)", duree=1),
        v("qb2", r"Énergie à fournir pour passer de l'état fondamental à l'orbite $n=5$ (en eV) ?", "Rational(136,10)*(1-Rational(1,25))", "1632/125",
          r"$\Delta E=E_5-E_1=13{,}6\left(1-\frac1{25}\right)=13{,}6\times\frac{24}{25}=13{,}056\approx13{,}06$ eV (photon absorbé).", src=EX + ", ex. 1 q2", duree=3),
        v("qb3", r"Longueur d'onde (en nm) du photon émis par la désexcitation $3\to2$ ($hc=1240$ eV·nm) ? Est-elle visible ?", "1240/(Rational(136,10)*(Rational(1,4)-Rational(1,9)))", "11160/17",
          r"$\Delta E=13{,}6\left(\frac14-\frac19\right)=13{,}6\times\frac5{36}\approx1{,}89$ eV. $\lambda=\frac{1240}{1{,}89}\approx656$ nm : rouge, dans le visible. C'est la raie $H_\alpha$ de la série de Balmer ($n_f=2$).", src=TD1 + ", ex. 2 q2", duree=4),
        v("qb4", r"On fournit $14$ eV à l'électron de l'atome d'hydrogène dans son état fondamental. Énergie cinétique finale (en eV) ?", "14-Rational(136,10)", "2/5",
          r"$14$ eV $>13{,}6$ eV : l'atome est ionisé, l'électron s'échappe avec $E_c=14-13{,}6=0{,}4$ eV, donc avec une vitesse non nulle (réponses b et c du QCM).", src=EX + ", ex. 1 q4", duree=3),
        v("qb5", r"Longueur d'onde (en nm) de la transition $5\to2$ ($hc=1240$ eV·nm) ?", "1240/(Rational(136,10)*(Rational(1,4)-Rational(1,25)))", "155000/357",
          r"$\Delta E=13{,}6\left(\frac14-\frac1{25}\right)=13{,}6\times\frac{21}{100}=2{,}856$ eV. $\lambda=\frac{1240}{2{,}856}\approx434$ nm : violet-bleu (série de Balmer).", src=TD1 + ", ex. 2 q5", duree=4),
        o("qb6", r"Pour passer du niveau $4$ au niveau $3$ de l'hydrogène : l'électron a-t-il besoin de recevoir un photon, ou cède-t-il un photon ?",
          r"$E_4=-0{,}85$ eV est supérieur à $E_3=-1{,}51$ eV : l'électron descend et perd de l'énergie. Il cède donc de l'énergie sous forme d'un photon (émission), d'énergie $E_4-E_3=0{,}66$ eV.", src=EX + ", ex. 1 q1", duree=2),
        o("qb7", r"Sur le diagramme d'énergie de l'hydrogène : où est le niveau fondamental ? Que représente l'énergie nulle ? Comment ioniser l'atome depuis $n=1$ ? Comment interpréter les spectres d'émission et d'absorption ?",
          r"Fondamental : $n=1$, $E_1=-13{,}6$ eV (le plus bas, état normal de l'électron). L'énergie nulle correspond à l'atome ionisé ($n\to\infty$), électron libre au repos." "\n\n"
          r"Ionisation depuis $n=1$ : absorber un photon d'énergie au moins $-E_1=13{,}6$ eV ($\lambda\leq91$ nm, ultraviolet) ; l'excédent devient énergie cinétique." "\n\n"
          r"Émission : l'atome excité redescend en émettant des photons d'énergie $E_i-E_f$ : raies brillantes sur fond noir. Absorption : lumière continue, l'atome n'absorbe que les photons d'énergie $E_f-E_i$ : raies noires aux mêmes longueurs d'onde. Spectre discret : les énergies sont quantifiées.", src=TD1 + ", ex. 2 q1, q4, q5", duree=5),
    ]},
    {"n": 6, "titre": "Hydrogénoïdes : rayons et énergies", "notions": ["hydrogenoide", "bohr"], "exos": [
        v("qr1", r"Rayon de la couche $n=3$ de l'hydrogène (en m), avec $a_0=\frac{\hbar^2}{me^2}=5\times10^{-11}$ m ?", "9*5*10**-11", "45*10**-11", r"$r_3=n^2a_0=9\times5\times10^{-11}=4{,}5\times10^{-10}$ m.", src=TD1 + ", ex. 1 q4", duree=2),
        v("qr2", r"Plus petit rayon possible pour l'ion $\mathrm{He}^+$ ($Z=2$), avec $\frac{\hbar^2}{me^2}=5\times10^{-11}$ m (en m) ? Vraisemblable ?", "5*10**-11/2", "25*10**-12",
          r"$r_1=\frac{\hbar^2}{Zme^2}=\frac{5\times10^{-11}}2=2{,}5\times10^{-11}$ m. Deux fois plus petit que pour l'hydrogène : le noyau de charge $2e$ attire plus fortement l'électron. Vraisemblable (largement supérieur à la taille du noyau, $\sim10^{-15}$ m).", src=EX + ", ex. 2 q4", duree=3),
        v("qr3", r"Même question pour $\mathrm{Li}^{2+}$ ($Z=3$) : plus petit rayon (en m) ?", "5*10**-11/3", "Rational(5,3)*10**-11",
          r"$r_1=\frac{5\times10^{-11}}3\approx1{,}67\times10^{-11}$ m. Plus $Z$ est grand, plus le rayon est petit (en $\frac1Z$).", src=EX + ", ex. 2 q4", duree=3),
        v("qr4", r"Énergie fondamentale de $\mathrm{He}^+$ en valeur absolue (en eV), avec $E_n=-13{,}6\frac{Z^2}{n^2}$ ?", "Rational(136,10)*4", "272/5",
          r"$|E_1|=13{,}6\times4=54{,}4$ eV. Valeur expérimentale $54{,}42$ eV : accord très bon (le modèle de Bohr est exact pour un seul électron).", src=EX + ", ex. 2 q5", duree=2),
        v("qr5", r"Énergie fondamentale de $\mathrm{Li}^{2+}$ en valeur absolue (en eV) ?", "Rational(136,10)*9", "612/5",
          r"$|E_1|=13{,}6\times9=122{,}4$ eV, contre $122{,}45$ eV mesurés. L'énergie d'ionisation croît comme $Z^2$ : $13{,}6$ (H), $54{,}4$ ($\mathrm{He}^+$), $122{,}4$ ($\mathrm{Li}^{2+}$).", src=EX + ", ex. 2 q5", duree=2),
        v("qr6", r"Longueur d'onde (en nm) du photon émis par $\mathrm{He}^+$ lors de $n=2\to n=1$ ($hc=1240$ eV·nm) ?", "1240/(Rational(136,10)*4*(1-Rational(1,4)))", "1550/51",
          r"$\Delta E=13{,}6\times4\times\left(1-\frac14\right)=40{,}8$ eV. $\lambda=\frac{1240}{40{,}8}\approx30{,}4$ nm : ultraviolet.", duree=4),
        o("qr7", r"Hydrogénoïde (noyau de $Z$ protons de charge $+q$, un électron de masse $m$, $e^2=kq^2$). 1) Norme de la force de Coulomb. 2) PFD pour trouver $mv^2$ en fonction de $Z$, $e$, $m$, $r$ (accélération $a=\frac{v^2}r$).",
          r"1) $F=\frac{k\,(Zq)\,q}{r^2}=\dfrac{Ze^2}{r^2}$." "\n\n"
          r"2) Seule force : Coulomb, centripète. $\sum\vec F=m\vec a$ donne $\frac{Ze^2}{r^2}=m\frac{v^2}r$, soit $mv^2=\dfrac{Ze^2}r$.", src=EX + ", ex. 2 q1, q2", duree=5),
        o("qr8", r"Avec le 3e postulat $mrv=n\hbar$ et le résultat précédent, établir le système de deux équations puis le rayon $r_n$ des orbites en fonction de $n$, $m$, $e$, $Z$.",
          r"Postulat : $mv=\frac{n\hbar}r$, donc $(mv)^2=\frac{n^2\hbar^2}{r^2}$. PFD : $mv^2=\frac{Ze^2}r$, donc en multipliant par $m$, $(mv)^2=\frac{Zme^2}r$." "\n\n"
          r"Égalité : $\frac{n^2\hbar^2}{r^2}=\frac{Zme^2}r$, d'où $r_n=\dfrac{n^2\hbar^2}{Zme^2}=\dfrac{n^2}Za_0$ avec $a_0=\frac{\hbar^2}{me^2}$ (rayon de Bohr, $\approx5\times10^{-11}$ m). Rayons en $n^2$ : quantifiés.", src=EX + ", ex. 2 q3 ; " + TD1 + ", ex. 1 q4", duree=6),
        o("qr9", r"Retrouver l'énergie $E_n$ de l'électron d'un hydrogénoïde en fonction de $m$, $e$, $\hbar$, $n$, $Z$. Comment appelle-t-on $E_1$ pour l'hydrogène ?",
          r"$E=E_c+E_p=\frac12mv^2-\frac{Ze^2}r=\frac{Ze^2}{2r}-\frac{Ze^2}r=-\frac{Ze^2}{2r}$." "\n\n"
          r"Avec $r_n=\frac{n^2\hbar^2}{Zme^2}$ : $E_n=-\dfrac{Z^2me^4}{2\hbar^2n^2}=-13{,}6\,\dfrac{Z^2}{n^2}$ eV." "\n\n"
          r"Pour l'hydrogène ($Z=1$), $E_1=-13{,}6$ eV est l'énergie du niveau fondamental ; $-E_1$ est l'énergie d'ionisation (constante de Rydberg en énergie).", src=TD1 + ", ex. 1 q5, q6 ; " + EX + ", ex. 2 q5", duree=6),
    ]},
    {"n": 7, "titre": "De Broglie et indétermination d'Heisenberg", "notions": ["debroglie", "heisenberg"], "exos": [
        v("qd1", r"Longueur d'onde de de Broglie (en m) d'un électron ($9{,}1\times10^{-31}$ kg) à $95$ m/s ($h=6{,}62\times10^{-34}$) ?", "Rational(662,100)*10**-34/(Rational(91,10)*10**-31*95)", "Rational(662,8645)*10**-4",
          r"$\lambda=\frac h{mv}=\frac{6{,}62\times10^{-34}}{9{,}1\times10^{-31}\times95}\approx7{,}7\times10^{-6}$ m : observable (micromètres).", src=TD2 + ", ex. 1 q1", duree=3),
        v("qd2", r"Longueur d'onde de de Broglie (en m) d'une balle de tennis de $50$ g à $95$ m/s ?", "Rational(662,100)*10**-34/(Rational(5,100)*95)", "Rational(662,475)*10**-34",
          r"$\lambda=\frac{6{,}62\times10^{-34}}{0{,}05\times95}\approx1{,}4\times10^{-34}$ m : bien plus petite que n'importe quelle structure, aucun effet ondulatoire observable.", src=TD2 + ", ex. 1 q1", duree=3),
        v("qd3", r"Vitesse de $95$ m/s connue à $0{,}085\,\%$ près. Incertitude minimale sur la position de l'électron (en m), avec $\Delta x\,\Delta p=\frac\hbar2$ ?", "Rational(662,100)*10**-34/(4*pi*Rational(91,10)*10**-31*95*Rational(85,100000))", "Rational(6620000,29393)*10**-5/pi",
          r"$\Delta p=m\,\Delta v=9{,}1\times10^{-31}\times95\times8{,}5\times10^{-4}\approx7{,}35\times10^{-32}$. $\Delta x=\frac\hbar{2\Delta p}=\frac h{4\pi\Delta p}\approx7{,}2\times10^{-4}$ m, environ $0{,}7$ mm : énorme à l'échelle de l'électron.", src=TD2 + ", ex. 1 q2", duree=5),
        v("qd4", r"Même calcul pour la balle de tennis ($0{,}05$ kg) : $\Delta x$ minimale (en m) ?", "Rational(662,100)*10**-34/(4*pi*Rational(5,100)*95*Rational(85,100000))", "Rational(1324,323)*10**-32/pi",
          r"$\Delta p=0{,}05\times95\times8{,}5\times10^{-4}=4{,}04\times10^{-3}$. $\Delta x=\frac h{4\pi\Delta p}\approx1{,}3\times10^{-32}$ m : négligeable, la balle est localisée comme en mécanique classique.", src=TD2 + ", ex. 1 q2", duree=5),
        v("qd5", r"Un électron est localisé dans un atome, $\Delta x=10^{-10}$ m. Incertitude minimale sur sa quantité de mouvement (en kg·m·s$^{-1}$) ?", "Rational(662,100)*10**-34/(4*pi*10**-10)", "Rational(331,200)*10**-24/pi",
          r"$\Delta p\geq\frac\hbar{2\Delta x}=\frac h{4\pi\Delta x}=\frac{6{,}62\times10^{-34}}{4\pi\times10^{-10}}\approx5{,}3\times10^{-25}$. Soit $\Delta v\approx6\times10^5$ m/s : l'électron ne peut pas être « immobile ».", duree=4),
        o("qd6", r"Commenter les résultats pour l'électron et la balle de tennis (TD2, ex. 1) : pourquoi la nature ondulatoire ne se voit-elle que pour les petites particules ?",
          r"Électron : $\lambda\sim10^{-6}$ m et $\Delta x\sim10^{-4}$ m sont macroscopiques : sa position est très indéterminée, son comportement ondulatoire est mesurable (diffraction d'électrons)." "\n\n"
          r"Balle : $\lambda\sim10^{-34}$ m et $\Delta x\sim10^{-32}$ m : sans commune mesure avec sa taille. Le terme $h\approx6{,}6\times10^{-34}$ J·s est minuscule, donc $\lambda=\frac h{mv}$ et $\Delta x\propto\frac h{m\Delta v}$ ne sont notables que si $m$ est très petite. La mécanique classique est la limite quantique pour les grands objets.", src=TD2 + ", ex. 1 q3", duree=4),
    ]},
    {"n": 8, "titre": "Fonction d'onde et probabilité de présence", "notions": ["psi"], "exos": [
        v("qw1", r"$\Psi(x)=\Psi_0e^{-x/x_0}$ sur $[0;+\infty[$ avec $x_0=8$ (unité arbitraire). Normaliser : $\Psi_0$ ?", "sqrt(2/Rational(8))", "1/2",
          r"$\int_0^\infty\Psi_0^2e^{-2x/x_0}dx=\Psi_0^2\frac{x_0}2=1$, donc $\Psi_0=\sqrt{\frac2{x_0}}=\sqrt{\frac28}=\frac12$.", src=TD2 + ", ex. 2 q2", duree=3),
        itg("qw2", r"$\Psi(x)=e^{-x/2}$ sur $[0;+\infty[$ (normalisée, $x_0=2$, $\Psi_0=1$). Probabilité de trouver la particule dans $[0;2]$ ?", "exp(-x)", "0", "2", "1-exp(-2)",
            r"$P=\int_0^2|\Psi|^2dx=\int_0^2e^{-x}dx=1-e^{-2}\approx0{,}865$.", src=TD2 + ", ex. 2 q3", duree=3),
        v("qw3", r"Pour $x_0=2$, la probabilité sur $[0;A]$ vaut $1-e^{-A}$. Valeur de $A$ pour $P\geq95\,\%$, avec $\ln(0{,}05)\approx-3$ ?", "-Rational(2)/2*(-3)", "3",
          r"Densité $\frac2{x_0}e^{-2x/x_0}$ ; $P=1-e^{-2A/x_0}\geq0{,}95\iff e^{-2A/x_0}\leq0{,}05\iff A\geq-\frac{x_0}2\ln0{,}05\approx\frac{3x_0}2=3$.", src=TD2 + ", ex. 2 q4", duree=4),
        itg("qw4", r"Particule dans $[0;4]$ avec $\psi=N\sin\left(\frac{\pi x}4\right)$. Calculer $I=\int_0^4\sin^2\left(\frac{\pi x}4\right)dx$ (puis $N=\frac1{\sqrt I}$).", "sin(pi*x/4)**2", "0", "4", "2",
            r"$\sin^2u=\frac{1-\cos2u}2$ : $I=\frac L2=2$. Normalisation : $N^2I=1$ donc $N=\frac1{\sqrt2}=\sqrt{\frac2L}\times\ldots$ avec $L=4$ ($\sqrt{2/L}=\frac1{\sqrt2}$).", src=TD3 + ", ex. 1 q4", duree=4),
        itg("qw5", r"Particule dans un puits de largeur $1$ à l'état fondamental, $\psi=\sqrt2\sin(\pi x)$. Probabilité de la trouver dans le premier tiers $[0;\frac13]$ ?", "2*sin(pi*x)**2", "0", "Rational(1,3)", "Rational(1,3)-sqrt(3)/(4*pi)",
            r"$P=\int_0^{1/3}2\sin^2(\pi x)dx=\left[x-\frac{\sin2\pi x}{2\pi}\right]_0^{1/3}=\frac13-\frac{\sin(2\pi/3)}{2\pi}=\frac13-\frac{\sqrt3}{4\pi}\approx0{,}196$. Inférieure à $\frac13$ : la particule est plus souvent au centre.", duree=5),
        o("qw6", r"Que représente $|\psi(x)|^2$ ? Pourquoi $\int|\psi|^2dx=1$ ? Une densité de probabilité peut-elle dépasser $1$ ?",
          r"Interprétation de Born : $|\psi(x)|^2$ est la densité de probabilité de présence en $x$ (probabilité par unité de longueur). La probabilité de trouver la particule dans $[a;b]$ est $\int_a^b|\psi|^2dx$." "\n\n"
          r"La particule est certainement quelque part : la probabilité sur tout l'espace vaut $1$ (condition de normalisation, qui fixe la constante multiplicative de $\psi$)." "\n\n"
          r"Une densité peut dépasser $1$ (elle est en m$^{-1}$) : seule l'intégrale est une probabilité, donc $\leq1$. Exemple : $\psi=\sqrt2\sin\pi x$ sur $[0;1]$ donne $|\psi|^2=2$ au centre.", src=COURS + ", III.4", duree=4),
    ]},
    {"n": 9, "titre": "Valeurs moyennes et incertitudes", "notions": ["moyennes", "psi", "heisenberg"], "exos": [
        v("qm1", r"$\psi=Ne^{-\lambda x^2/2}$ avec $\lambda=2$. Normalisation avec $\int e^{-\lambda x^2}dx=\sqrt{\frac\pi\lambda}$ : valeur de $N$ ?", "(2/pi)**Rational(1,4)", "2**Rational(1,4)/pi**Rational(1,4)",
          r"$N^2\sqrt{\frac\pi\lambda}=1$ donc $N^2=\sqrt{\frac\lambda\pi}$ et $N=\left(\frac\lambda\pi\right)^{1/4}=\left(\frac2\pi\right)^{1/4}\approx0{,}893$.", src=TD2 + ", ex. 3 q1", duree=4),
        itg("qm2", r"Même fonction ($\lambda=2$, $N^2=\sqrt{\frac2\pi}$). Calculer $\langle x^2\rangle=\int_{-\infty}^{+\infty}x^2|\psi|^2dx$.", "x**2*sqrt(2/pi)*exp(-2*x**2)", "-oo", "oo", "Rational(1,4)",
            r"$\langle x^2\rangle=N^2\int x^2e^{-\lambda x^2}dx=N^2\frac1{2\lambda}\sqrt{\frac\pi\lambda}=\frac1{2\lambda}=\frac14$ (car $N^2\sqrt{\frac\pi\lambda}=1$).", src=TD2 + ", ex. 3 q3", duree=4),
        v("qm3", r"Avec $\langle x\rangle=0$, incertitude $\Delta x=\sqrt{\langle x^2\rangle-\langle x\rangle^2}$ pour $\lambda=8$ (donc $\langle x^2\rangle=\frac1{2\lambda}$) ?", "sqrt(1/(2*Rational(8)))", "1/4",
          r"$\Delta x=\sqrt{\frac1{2\lambda}}=\sqrt{\frac1{16}}=\frac14$.", src=TD2 + ", ex. 3 q3", duree=2),
        itg("qm4", r"$\psi=Ne^{-\lambda x^2/2}$, $\lambda=2$. Calculer $\frac{\langle p^2\rangle}{\hbar^2}=\int|\psi'|^2dx$ (avec $\psi'=-2x\psi$).", "4*x**2*sqrt(2/pi)*exp(-2*x**2)", "-oo", "oo", "1",
            r"$|\psi'|^2=\lambda^2x^2|\psi|^2$ : $\frac{\langle p^2\rangle}{\hbar^2}=\lambda^2\langle x^2\rangle=\frac{\lambda^2}{2\lambda}=\frac\lambda2=1$. Donc $\Delta p=\hbar\sqrt{\lambda/2}=\hbar$ (car $\langle p\rangle=0$).", src=TD2 + ", ex. 3 q6", duree=5),
        v("qm5", r"Pour $\lambda=2$ : $\Delta x=\frac12$ et $\Delta p=\hbar$. Rapport $\dfrac{\Delta x\,\Delta p}{\hbar/2}$ ? Que conclure sur Heisenberg ?", "Rational(1,2)*1/(Rational(1,2))", "1",
          r"$\Delta x\,\Delta p=\frac\hbar2$ : le rapport vaut $1$. L'inégalité $\Delta x\,\Delta p\geq\frac\hbar2$ est respectée, avec égalité (la gaussienne est l'état d'indétermination minimale). Pour tout $\lambda$ : $\frac1{\sqrt{2\lambda}}\times\hbar\sqrt{\frac\lambda2}=\frac\hbar2$.", src=TD2 + ", ex. 3 q7", duree=3),
        itg("qm6", r"$\Psi=\Psi_0e^{-x/x_0}$ sur $[0;+\infty[$ avec $x_0=4$ (donc $|\Psi|^2=\frac12e^{-x/2}$). Position moyenne $\langle x\rangle$ ?", "x*Rational(1,2)*exp(-x/2)", "0", "oo", "2",
            r"$\langle x\rangle=\int_0^\infty x\,\frac12e^{-x/2}dx$. Par parties : $=\left[-xe^{-x/2}\right]_0^\infty+\int_0^\infty e^{-x/2}dx=2$. En général $\langle x\rangle=\frac{x_0}2$.", duree=5),
        o("qm7", r"Pour une fonction d'onde réelle qui tend vers $0$ à l'infini, montrer que $\langle p\rangle=0$ et que $\langle p^2\rangle=\hbar^2\int|\psi'|^2dx$.",
          r"$\langle p\rangle=-i\hbar\int\psi\psi'dx=-i\hbar\int\left(\frac{\psi^2}2\right)'dx=-\frac{i\hbar}2\left[\psi^2\right]_{-\infty}^{+\infty}=0$." "\n\n"
          r"$\langle p^2\rangle=\int\psi^*\left(-\hbar^2\psi''\right)dx=-\hbar^2\left[\psi^*\psi'\right]_{-\infty}^{+\infty}+\hbar^2\int|\psi'|^2dx$ (intégration par parties). Le crochet est nul car $\psi\to0$ : $\langle p^2\rangle=\hbar^2\int|\psi'|^2dx$.", src=TD2 + ", ex. 3 q4, q5", duree=6),
        o("qm8", r"Expliquer à l'aide d'un dessin pourquoi $\langle x\rangle=0$ pour $\psi=Ne^{-\lambda x^2/2}$ sur $]-\infty;+\infty[$.",
          r"La gaussienne est une fonction paire, tracée en cloche centrée en $0$ : $|\psi|^2$ est aussi paire. Alors $x|\psi|^2$ est impaire et $\int_{-\infty}^{+\infty}x|\psi|^2dx=0$ : les contributions des deux côtés de l'origine, symétriques, se compensent. Particule aussi souvent à droite qu'à gauche : position moyenne nulle.", src=TD2 + ", ex. 3 q2", duree=3),
    ]},
    {"n": 10, "titre": "Équation de Schrödinger et puits infini 1D", "notions": ["schrodinger"], "exos": [
        v("qs1", r"Électron ($m=9\times10^{-31}$ kg) dans un puits infini de largeur $L=0{,}5$ nm. $E_1=\frac{h^2}{8mL^2}$ en eV ($h=6{,}6\times10^{-34}$, $1$ eV $=1{,}6\times10^{-19}$ J) ?", "(Rational(66,10)*10**-34)**2/(8*9*10**-31*(Rational(1,2)*10**-9)**2)/(Rational(16,10)*10**-19)", "121/80",
          r"$E_1=\frac{\pi^2\hbar^2}{2mL^2}=\frac{h^2}{8mL^2}=\frac{4{,}356\times10^{-67}}{8\times9\times10^{-31}\times2{,}5\times10^{-19}}\approx2{,}42\times10^{-19}$ J $\approx1{,}51$ eV.", duree=5),
        v("qs2", r"Dans un puits où $E_1=0{,}4$ eV, énergie du niveau $n=3$ (en eV) ?", "9*Rational(4,10)", "18/5", r"$E_n=n^2E_1$ donc $E_3=9\times0{,}4=3{,}6$ eV.", src=TD3 + ", ex. 1 q5", duree=2),
        v("qs3", r"Même puits ($E_1=0{,}4$ eV) : longueur d'onde du photon émis lors de $n=2\to n=1$ (en nm, $hc=1240$ eV·nm) ?", "1240/(3*Rational(4,10))", "3100/3",
          r"$\Delta E=E_2-E_1=4E_1-E_1=3E_1=1{,}2$ eV. $\lambda=\frac{1240}{1{,}2}\approx1033$ nm (infrarouge).", duree=3),
        v("qs4", r"Normalisation de $\psi=A\sin\frac{n\pi x}L$ sur $[0;L]$ : $A^2\frac L2=1$. Valeur de $A$ pour $L=\frac12$ ?", "sqrt(2/Rational(1,2))", "2",
          r"$A=\sqrt{\frac2L}=\sqrt4=2$ (car $\int_0^L\sin^2\frac{n\pi x}Ldx=\frac L2$).", src=TD3 + ", ex. 1 q4", duree=3),
        v("qs5", r"On double la largeur du puits. L'énergie $E_1=2$ eV devient (en eV) ?", "2/2**2", "1/2", r"$E_1\propto\frac1{L^2}$ : doubler $L$ divise par $4$ : $\frac24=0{,}5$ eV.", duree=2),
        o("qs6", r"Particule de masse $m$ dans le puits $V=0$ sur $[0;L]$, $V=+\infty$ ailleurs. 1) Équation de Schrödinger sur $[0;L]$ ; forme des solutions. 2) Conditions aux limites. 3) Que donne $\psi(0)$ ?",
          r"1) $V=0$ : $-\frac{\hbar^2}{2m}\psi''(x)=E\psi(x)$, soit $\psi''=-k^2\psi$ avec $k^2=\frac{2mE}{\hbar^2}$. Solutions générales : $\psi(x)=A\sin kx+B\cos kx$." "\n\n"
          r"2) $V=+\infty$ hors de $[0;L]$ : la particule ne peut s'y trouver, $\psi=0$ dehors, et $\psi$ est continue, donc $\psi(0)=0$ et $\psi(L)=0$." "\n\n"
          r"3) $\psi(0)=B=0$ : il reste $\psi(x)=A\sin kx$.", src=EX + ", ex. 3 I q1-3 ; " + TD3 + ", ex. 1 q1-3", duree=6),
        o("qs7", r"Condition $\psi(L)=0$ : montrer qu'il y a quantification, donner $k$ puis $E_n$, puis $A$ par normalisation. Quel est le nombre quantique ?",
          r"$\psi(L)=A\sin kL=0$ avec $A\neq0$ (sinon $\psi\equiv0$) : $kL=n\pi$, $n\in\mathbb N^*$ ($n=0$ donne $\psi=0$). Donc $k=\frac{n\pi}L$ : seules des valeurs discrètes." "\n\n"
          r"$k^2=\frac{2mE}{\hbar^2}$ : $E_n=\dfrac{n^2\pi^2\hbar^2}{2mL^2}=n^2E_1$ : l'énergie est quantifiée, $n$ est le nombre quantique." "\n\n"
          r"Normalisation : $\int_0^LA^2\sin^2\frac{n\pi x}Ldx=A^2\frac L2=1$, d'où $A=\sqrt{\frac2L}$ et $\psi_n(x)=\sqrt{\frac2L}\sin\frac{n\pi x}L$.", src=EX + ", ex. 3 I q4-5 ; " + TD3 + ", ex. 1 q4-5", duree=8),
        o("qs8", r"Schématiser le diagramme d'énergie du puits infini avec l'allure de $|\psi_n|^2$ pour $n=1,2,3$.",
          r"Niveaux $E_n=n^2E_1$ : $E_1$, $4E_1$, $9E_1$ (écart croissant avec $n$). Sur chaque niveau, tracer $|\psi_n|^2=\frac2L\sin^2\frac{n\pi x}L$ sur $[0;L]$ : $n=1$ une bosse centrée en $\frac L2$ ; $n=2$ deux bosses, un n{\oe}ud en $\frac L2$ ; $n=3$ trois bosses, deux n{\oe}uds en $\frac L3$ et $\frac{2L}3$. $|\psi_n|^2$ s'annule en $0$ et $L$ ; $\psi_n$ a $n-1$ n{\oe}uds. Classiquement, la densité serait uniforme et l'énergie minimale nulle.", src=TD3 + ", ex. 1 q6", duree=4),
    ]},
    {"n": 11, "titre": "Superposition d'états et énergie moyenne", "notions": ["superposition", "schrodinger"], "exos": [
        v("qv1", r"$\psi=N(3\psi_1-\psi_3)$ avec $\psi_n$ orthonormés. Probabilité de mesurer l'énergie $E_1$ ?", "9/Rational(9+1)", "9/10",
          r"Normalisation : $N^2(9+1)=1$, $N^2=\frac1{10}$. $P_1=|c_1|^2=\frac9{10}$ (et $P_3=\frac1{10}$).", src=TD3 + ", ex. 2 q4", duree=3),
        v("qv2", r"Même état : énergie moyenne $\langle E\rangle$ en unités de $E_1$ ($E_n=n^2E_1$) ?", "(9*1+1*9)/Rational(10)", "9/5",
          r"$\langle E\rangle=\sum|c_n|^2E_n=\frac9{10}E_1+\frac1{10}\times9E_1=\frac{18}{10}E_1=\frac95E_1$.", src=TD3 + ", ex. 2 q6", duree=3),
        itg("qv3", r"Dans un puits de largeur $1$ : $\psi_n=\sqrt2\sin(n\pi x)$. Calculer $\int_0^1\psi_1\psi_3\,dx$.", "2*sin(pi*x)*sin(3*pi*x)", "0", "1", "0",
            r"$\sin a\sin b=\frac12[\cos(a-b)-\cos(a+b)]$ : $\int_0^1[\cos2\pi x-\cos4\pi x]dx=\left[\frac{\sin2\pi x}{2\pi}-\frac{\sin4\pi x}{4\pi}\right]_0^1=0$. Orthogonalité : $\delta_{13}=0$.", src=TD3 + ", ex. 2 q2", duree=4),
        itg("qv4", r"Calculer $\int_0^1\sin^6(\pi x)\,dx$ (utile pour normaliser $\psi=N\sin^3(\pi x)$).", "sin(pi*x)**6", "0", "1", "Rational(5,16)",
            r"Formule de Wallis : $\int_0^\pi\sin^6u\,du=\frac{5\pi}{16}$, donc $\int_0^1\sin^6(\pi x)dx=\frac5{16}$ (aussi via $\sin^3=\frac14(3\sin u-\sin3u)$ : $\frac1{16}\cdot\frac12(9+1)=\frac5{16}$).", duree=5),
        v("qv5", r"Constante de normalisation de $\psi=N\sin^3(\pi x)$ sur $[0;1]$ : $N^2=\frac1{\int\sin^6}$. Calculer $N^2$.", "1/Rational(5,16)", "16/5",
          r"$N^2\times\frac5{16}=1$, $N^2=\frac{16}5$, $N=\frac4{\sqrt5}$. Pour une largeur $L$ : $N=\frac4{\sqrt{5L}}$.", src=TD3 + ", ex. 2 q3", duree=3),
        o("qv6", r"Montrer l'orthogonalité $\int_0^L\psi_n\psi_m\,dx=\delta_{nm}$ pour $\psi_n=\sqrt{\frac2L}\sin\frac{n\pi x}L$.",
          r"$\int_0^L\psi_n\psi_m=\frac2L\int_0^L\sin\frac{n\pi x}L\sin\frac{m\pi x}Ldx=\frac1L\int_0^L\left[\cos\frac{(n-m)\pi x}L-\cos\frac{(n+m)\pi x}L\right]dx$." "\n\n"
          r"Si $n\neq m$ : $n\pm m$ entiers non nuls, $\int_0^L\cos\frac{p\pi x}Ldx=\frac L{p\pi}\sin p\pi=0$ : résultat $0$." "\n\n"
          r"Si $n=m$ : $\frac1L\int_0^L[1-\cos\frac{2n\pi x}L]dx=\frac1L\times L=1$. Donc $\delta_{nm}$.", src=TD3 + ", ex. 2 q2", duree=6),
        o("qv7", r"Boîte $[0;L]$, $\psi(x)=N\sin^3\frac{\pi x}L$, avec $\sin^3u=\frac14(3\sin u-\sin3u)$. 1) Coefficients $c_n$. 2) Normalisation, $N$. 3) Niveaux possibles et probabilités. 4) $\langle E\rangle$ en fonction de $E_1$.",
          r"1) $\sin^3\frac{\pi x}L=\frac14\left(3\sin\frac{\pi x}L-\sin\frac{3\pi x}L\right)$ et $\sin\frac{n\pi x}L=\sqrt{\frac L2}\psi_n$ : $\psi=\frac N4\sqrt{\frac L2}\,(3\psi_1-\psi_3)$, soit $c_1=\frac{3N}4\sqrt{\frac L2}$, $c_3=-\frac N4\sqrt{\frac L2}$, les autres $c_n=0$." "\n\n"
          r"2) $\sum|c_n|^2=\frac{N^2}{16}\frac L2(9+1)=\frac{5N^2L}{16}=1$ : $N=\frac4{\sqrt{5L}}$." "\n\n"
          r"3) Niveaux $E_1$ et $E_3=9E_1$ seulement, avec $P_1=\frac9{10}$ et $P_3=\frac1{10}$." "\n\n"
          r"4) $\langle E\rangle=\sum|c_n|^2E_n=\frac9{10}E_1+\frac1{10}\cdot9E_1=\frac95E_1$.", src=TD3 + ", ex. 2", duree=10),
    ]},
    {"n": 12, "titre": "Boîte 2D et dégénérescence", "notions": ["boite2d", "schrodinger"], "exos": [
        v("q2a", r"Boîte carrée $a=b=1$. Énergie du niveau $(n_x,n_y)=(2,1)$ en unités de $\frac{\hbar^2\pi^2}{2m}$ ?", "2**2+1**2", "5", r"$E_{n_x,n_y}=\frac{\hbar^2\pi^2}{2m}(n_x^2+n_y^2)$, soit $4+1=5$. Même valeur pour $(1,2)$ : dégénérés.", src=EX + ", ex. 3 II q8", duree=2),
        v("q2b", r"Électron dans une boîte carrée de $1$ nm de côté. $E_{min}=2E_1^{1D}$ avec $E_1^{1D}=\frac{h^2}{8mL^2}$ ; en eV ($h=6{,}6\times10^{-34}$, $m=9\times10^{-31}$) ?", "2*(Rational(66,10)*10**-34)**2/(8*9*10**-31*(10**-9)**2)/(Rational(16,10)*10**-19)", "121/160",
          r"$E_{min}=\frac{\hbar^2\pi^2}{2m}(1+1)=\frac{\hbar^2\pi^2}m=2\times\frac{h^2}{8mL^2}=2\times0{,}378\approx0{,}76$ eV.", src=EX + ", ex. 3 II q6", duree=5),
        v("q2c", r"Boîte carrée : rang de $\frac{E}{E_{min}}$ pour le sixième niveau, atteint pour $(4,1)$ (les sommes $n_x^2+n_y^2$ ordonnées valent $2,5,8,10,13,17,\dots$). Calculer $\frac{E_{4,1}}{E_{min}}$.", "(4**2+1**2)/Rational(2)", "17/2",
          r"$E_{min}=\frac{\hbar^2\pi^2}{2m}\times2$ ; $E_{4,1}=\frac{\hbar^2\pi^2}{2m}\times17$ : $\frac{E_{4,1}}{E_{min}}=\frac{17}2=8{,}5$. Atteint pour $(4,1)$ ou $(1,4)$.", src=EX + ", ex. 3 II q9", duree=5),
        v("q2d", r"Boîte rectangulaire $a=1$, $b=2$ : $E\propto n_x^2+\frac{n_y^2}4$ (même unité). Énergie du premier niveau excité, atteint pour $(1,2)$ ?", "1**2+2**2/Rational(4)", "2",
          r"Niveaux : $(1,1):\frac54$ ; $(1,2):1+1=2$ ; $(1,3):\frac{13}4$ ; $(2,1):\frac{17}4$ ; le premier excité est $(1,2)$ de valeur $2$. Plus de dégénérescence systématique : $a\neq b$.", duree=4),
        v("q2e", r"Boîte carrée : combien de niveaux $(n_x,n_y)$ distincts ont l'énergie $n_x^2+n_y^2=25$ (en $\frac{\hbar^2\pi^2}{2m}$) ? ($n_x,n_y\geq1$)", "2", "2",
          r"$25=9+16$ : $(3,4)$ et $(4,3)$. Pas $(5,0)$ ni $(0,5)$ : $n_x,n_y\geq1$. Dégénérescence $2$.", duree=3),
        o("q2f", r"Boîte 2D carrée $a=b=1$ : donner $E_{min}$. En quoi est-ce surprenant par rapport à la mécanique classique ?",
          r"$E_{n_x,n_y}=\frac{\hbar^2\pi^2}{2m}(n_x^2+n_y^2)$ avec $n_x,n_y\geq1$ : $E_{min}=E_{1,1}=\dfrac{\hbar^2\pi^2}m$." "\n\n"
          r"Classiquement, une particule peut être au repos au fond de la boîte, d'énergie nulle. Ici l'énergie minimale n'est pas nulle : elle ne peut pas être immobile. C'est cohérent avec Heisenberg : confinée ($\Delta x\leq1$), elle a $\Delta p\geq\frac\hbar{2\Delta x}\neq0$.", src=EX + ", ex. 3 II q6-7", duree=4),
        o("q2g", r"Que peut-on dire des niveaux $(2,1)$ et $(1,2)$ de la boîte carrée ? Comment appelle-t-on cette situation ?",
          r"$E_{2,1}=\frac{\hbar^2\pi^2}{2m}(4+1)=E_{1,2}$ : même énergie pour deux fonctions d'onde différentes, $\psi_{2,1}\neq\psi_{1,2}$ (symétriques par échange de $x$ et $y$). On parle de dégénérescence (ici d'ordre $2$).", src=EX + ", ex. 3 II q8", duree=3),
    ]},
    {"n": 13, "titre": "Qubits et portes quantiques", "notions": ["qubit"], "exos": [
        v("qq1", r"Qubit $|\psi\rangle=\frac35|0\rangle+\frac45|1\rangle$. Probabilité de mesurer $|0\rangle$ ?", "(Rational(3,5))**2", "9/25",
          r"$P(0)=|\alpha|^2=\frac9{25}=0{,}36$ ; $P(1)=\frac{16}{25}$ ; $0{,}36+0{,}64=1$.", src=COURS + ", IV.2", duree=2),
        v("qq2", r"Un qubit a $\alpha=\frac12$ réel. Probabilité de mesurer $|1\rangle$ (normalisation $|\alpha|^2+|\beta|^2=1$) ?", "1-Rational(1,2)**2", "3/4",
          r"$|\beta|^2=1-|\alpha|^2=1-\frac14=\frac34$, soit $\beta=\frac{\sqrt3}2$.", duree=2),
        v("qq3", r"On applique $H$ à $|0\rangle$ : $\frac1{\sqrt2}(|0\rangle+|1\rangle)$. Probabilité de mesurer $|1\rangle$ ?", "(1/sqrt(2))**2", "1/2",
          r"$P(1)=\left|\frac1{\sqrt2}\right|^2=\frac12$ : superposition équiprobable ($P(0)=\frac12$ aussi).", src=COURS + ", IV.3", duree=2),
        v("qq4", r"Avec $H=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$, calculer $H^2|0\rangle$ (coordonnées).", "(Matrix([[1,1],[1,-1]])/sqrt(2))**2*Matrix([1,0])", "Matrix([1,0])",
          r"$H|0\rangle=\frac1{\sqrt2}\binom11$, puis $H\left(\frac1{\sqrt2}\binom11\right)=\frac12\binom{1+1}{1-1}=\binom10=|0\rangle$. $H$ est son propre inverse : $H^2=I$.", src=COURS + ", IV.3", duree=4),
        v("qq5", r"CNOT (premier qubit de contrôle) sur $(\alpha,\beta,\gamma,\delta)=(1,2,3,4)$ dans l'ordre $|00\rangle,|01\rangle,|10\rangle,|11\rangle$ : état de sortie ?", "Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])*Matrix([1,2,3,4])", "Matrix([1,2,4,3])",
          r"Si le premier qubit vaut $|1\rangle$, on inverse le second : $|10\rangle\leftrightarrow|11\rangle$, donc $\gamma$ et $\delta$ sont échangés : $(1,2,4,3)$.", src=COURS + ", IV.4", duree=4),
        v("qq6", r"Combien de coefficients complexes décrivent l'état de $10$ qubits ?", "2**10", "1024", r"$2^n$ coefficients pour $n$ qubits : $2^{10}=1024$.", src=COURS + ", IV.4", duree=1),
        o("qq7", r"Qu'est-ce que la superposition d'états ? Que donne la mesure d'un qubit $\alpha|0\rangle+\beta|1\rangle$ ? Que raconte le chat de Schrödinger ?",
          r"Un système quantique peut être dans une combinaison linéaire de plusieurs états de base à la fois. Pour un qubit $\alpha|0\rangle+\beta|1\rangle$ avec $|\alpha|^2+|\beta|^2=1$." "\n\n"
          r"La mesure ne donne qu'un seul résultat : $|0\rangle$ avec la probabilité $|\alpha|^2$, $|1\rangle$ avec $|\beta|^2$. Une seule mesure ne permet pas de connaître $\alpha$ et $\beta$. Après la mesure, l'état est celui obtenu." "\n\n"
          r"Chat de Schrödinger (1935) : expérience de pensée où un chat est lié à un processus quantique. Avant ouverture de la boîte, son état est une superposition « mort et vivant » ; à l'ouverture (mesure), un seul état est observé, avec les probabilités du processus.", src=COURS + ", IV.1-2", duree=4),
    ]},
    {"n": 14, "titre": "Niveau examen : final de mécanique quantique", "notions": ["bohr", "hydrogenoide", "schrodinger", "boite2d", "photon"], "examen": True, "exos": [
        {"id": "qx1", "kind": "multi", "src": EX + ", ex. 1 (5 points)",
         "enonce": r"Questions de cours (document : niveaux de l'hydrogène $-13{,}6$, $-3{,}4$, $-1{,}51$, $-0{,}850$, $-0{,}54$, $-0{,}37$, $0$ eV). 1. Passer du niveau $4$ au niveau $3$ : l'électron reçoit ou cède un photon ? 2. Énergie à fournir pour aller de $n=1$ à $n=5$. 3. Longueur d'onde de la transition $3\to2$. 4. On fournit $14$ eV à l'électron fondamental : que se passe-t-il ? 5. Que représente le spectre du rayonnement d'un corps noir ?",
         "parts": ["qb6", "qb2", "qp4", "qb4", "qp5"]},
        {"id": "qx2", "kind": "multi", "src": EX + ", ex. 2 (6 points)",
         "enonce": r"Modèle de Bohr pour un hydrogénoïde ($Z$ protons, un électron). 1. Norme de la force de Coulomb. 2. PFD : $mv^2$. 3. Rayons $r_n$ à l'aide de $mrv=n\hbar$. 4. Plus petit rayon de $\mathrm{He}^+$ et de $\mathrm{Li}^{2+}$ (avec $\frac{\hbar^2}{me^2}=5\times10^{-11}$ m). 5. Énergies fondamentales de $\mathrm{He}^+$ et $\mathrm{Li}^{2+}$ ; commenter avec $54{,}42$ eV et $122{,}45$ eV.",
         "parts": ["qr7", "qr8", "qr2", "qr3", "qr4", "qr5"]},
        {"id": "qx3", "kind": "multi", "src": EX + ", ex. 3 (9 points)",
         "enonce": r"Boîte quantique 1D puis 2D. I. Particule dans $[0;L]$ ($V=0$ dedans, $V=+\infty$ dehors) : 1. équation de Schrödinger ; 2. conditions aux limites ; 3. condition en $0$ ; 4. quantification ; 5. niveaux d'énergie. II. Boîte 2D, $a=b=1$ : 6. $E_{min}$ ; 7. en quoi est-ce surprenant ; 8. niveaux $(2,1)$ et $(1,2)$ ; 9. sixième niveau.",
         "parts": ["qs6", "qs7", "q2f", "q2g", "q2c"]},
    ]},
    {"n": 15, "titre": "Examen + 20 % : problèmes combinés", "notions": ["photoelec", "hydrogenoide", "heisenberg", "schrodinger", "moyennes", "superposition"], "examen": True, "exos": [
        v("qy1", r"Lumière à $200$ nm ($hc=1240$ eV·nm) sur un métal de travail d'extraction $4{,}4$ eV. Longueur d'onde de de Broglie des électrons émis (en m), $m=9\times10^{-31}$, $h=6{,}6\times10^{-34}$, $1$ eV $=1{,}6\times10^{-19}$ J ?", "Rational(66,10)*10**-34/(9*10**-31*sqrt(2*(Rational(1240,200)-Rational(44,10))*Rational(16,10)*10**-19/(9*10**-31)))", "Rational(11,12)*10**-9",
          r"$E_c=6{,}2-4{,}4=1{,}8$ eV. $v=\sqrt{\frac{2E_c}m}=8\times10^5$ m/s (voir niveau 4). $\lambda=\frac h{mv}=\frac{6{,}6\times10^{-34}}{9\times10^{-31}\times8\times10^5}=\frac{6{,}6\times10^{-34}}{7{,}2\times10^{-25}}\approx9{,}2\times10^{-10}$ m, de l'ordre de la distance interatomique : diffraction possible dans un cristal.", duree=8),
        v("qy2", r"Photon émis par $\mathrm{He}^+$ lors de $n=3\to n=2$ : longueur d'onde (en nm) avec $E_n=-13{,}6\frac{Z^2}{n^2}$ eV et $hc=1240$ eV·nm ?", "1240/(Rational(136,10)*4*(Rational(1,4)-Rational(1,9)))", "2790/17",
          r"$\Delta E=13{,}6\times4\times\left(\frac14-\frac19\right)=13{,}6\times4\times\frac5{36}\approx7{,}56$ eV. $\lambda=\frac{1240}{7{,}56}\approx164$ nm, ultraviolet : le visible de l'hydrogène (Balmer) est décalé vers l'UV pour $Z=2$.", duree=6),
        v("qy3", r"Puits infini 1D avec $E_1=0{,}4$ eV. Longueur d'onde (en nm) du photon absorbé pour passer de $n=1$ à $n=4$ ($hc=1240$ eV·nm) ?", "1240/(15*Rational(4,10))", "620/3",
          r"$E_4-E_1=16E_1-E_1=15E_1=6$ eV. $\lambda=\frac{1240}6\approx207$ nm (ultraviolet).", duree=5),
        v("qy4", r"Électron de l'hydrogène localisé à $\Delta x=a_0=5\times10^{-11}$ m. Incertitude minimale sur sa vitesse (en m/s), $h=6{,}62\times10^{-34}$, $m=9{,}1\times10^{-31}$ ? À comparer avec la vitesse de Bohr $2{,}2\times10^6$ m/s.", "Rational(662,100)*10**-34/(4*pi*5*10**-11)/(Rational(91,10)*10**-31)", "Rational(331,910)*10**7/pi",
          r"$\Delta p\geq\frac h{4\pi\Delta x}=\frac{6{,}62\times10^{-34}}{4\pi\times5\times10^{-11}}\approx1{,}05\times10^{-24}$. $\Delta v=\frac{\Delta p}m\approx1{,}2\times10^6$ m/s : même ordre de grandeur que la vitesse de Bohr, ce qui confirme que la trajectoire n'a pas de sens précis à cette échelle.", duree=6),
        {"id": "qy5", "kind": "multi", "src": TD2 + ", ex. 3",
         "enonce": r"Fonction d'onde $\psi(x)=Ne^{-\lambda x^2/2}$ (gaussienne). Calculer $N$, $\langle x^2\rangle$ et $\Delta x$, démontrer $\langle p^2\rangle=\hbar^2\int|\psi'|^2dx$ et $\langle p\rangle=0$, puis calculer $\Delta p$ et $\Delta x\,\Delta p$ (avec $\lambda=2$ pour les valeurs numériques).",
         "parts": ["qm1", "qm2", "qm3", "qm7", "qm4", "qm5"]},
        {"id": "qy6", "kind": "multi", "src": TD3 + ", ex. 2",
         "enonce": r"Particule dans une boîte $[0;L]$ avec $\psi(x)=N\sin^3\frac{\pi x}L$. Montrer l'orthogonalité des $\psi_n$, normaliser $\psi$, donner les niveaux et probabilités, et l'énergie moyenne en fonction de $E_1$.",
         "parts": ["qv6", "qv4", "qv5", "qv1", "qv2", "qv7"]},
    ]},
]


def _v(enonce, calc, ans, sol):
    return {"enonce": enonce, "calc": calc, "ans": ans, "sol": sol}


def _i(enonce, f, a, b, ans, sol):
    return {"enonce": enonce, "f": f, "a": a, "b": b, "ans": ans, "sol": sol}


# Numeric variants: a failed exercise comes back with other numbers; build.py checks them like the exercise itself.
VARIANTS = {
    "qa1": [_v(r"Un chariot de $2$ kg à $3$ m/s. Énergie cinétique (en J) ?", "Rational(1,2)*2*3**2", "9", r"$\frac12\times2\times9=9$ J.")],
    "qa2": [_v(r"Convertir $3$ eV en joules.", "3*Rational(16,10)*10**-19", "48*10**-20", r"$3\times1{,}6\times10^{-19}=4{,}8\times10^{-19}$ J.")],
    "qa3": [_v(r"Une lumière de fréquence $6\times10^{14}$ Hz : longueur d'onde (en nm) ?", "3*10**8/(6*10**14)*10**9", "500", r"$\lambda=\frac{3\times10^8}{6\times10^{14}}=5\times10^{-7}$ m $=500$ nm.")],
    "qa4": [_v(r"Un électron ($9\times10^{-31}$ kg) à $4\times10^6$ m/s. $E_c$ (en eV) ?", "Rational(1,2)*9*10**-31*(4*10**6)**2/(Rational(16,10)*10**-19)", "45",
               r"$E_c=\frac12\times9\times10^{-31}\times16\times10^{12}=7{,}2\times10^{-18}$ J $=45$ eV.")],
    "qc1": [_v(r"Même force pour $r=10^{-10}$ m (en N) ?", "9*10**9*(Rational(16,10)*10**-19)**2/(10**-10)**2", "2304*10**-11", r"$F=\frac{2{,}304\times10^{-28}}{10^{-20}}=2{,}304\times10^{-8}$ N : divisée par $4$ quand $r$ double.")],
    "qc2": [_v(r"$v=10^6$ m/s, $r=5\times10^{-11}$ m. $a$ (en m·s$^{-2}$) ?", "(10**6)**2/(5*10**-11)", "2*10**22", r"$a=\frac{10^{12}}{5\times10^{-11}}=2\times10^{22}$ m·s$^{-2}$.")],
    "qc3": [_v(r"$mv^2=\frac{kq^2}r$ pour $r=10^{-10}$ m (en J) ?", "9*10**9*(Rational(16,10)*10**-19)**2/10**-10", "2304*10**-21", r"$\frac{2{,}304\times10^{-28}}{10^{-10}}=2{,}304\times10^{-18}$ J.")],
    "qc4": [_v(r"$E_c=\frac{kq^2}{2r}$ pour $r=2\times10^{-10}$ m (en eV) ?", "9*10**9*(Rational(16,10)*10**-19)**2/(2*2*10**-10)/(Rational(16,10)*10**-19)", "18/5",
               r"$E_c=\frac{2{,}304\times10^{-28}}{4\times10^{-10}}=5{,}76\times10^{-19}$ J $=3{,}6$ eV.")],
    "qp1": [_v(r"Énergie (en eV) d'un photon de $400$ nm ?", "1240/400", "31/10", r"$\frac{1240}{400}=3{,}1$ eV.")],
    "qp2": [_v(r"Fréquence (en Hz) d'un photon de $1{,}98\times10^{-19}$ J ?", "Rational(198,100)*10**-19/(Rational(66,10)*10**-34)", "3*10**14", r"$\nu=\frac{1{,}98\times10^{-19}}{6{,}6\times10^{-34}}=3\times10^{14}$ Hz.")],
    "qp3": [_v(r"Laser de $2$ mW à $660$ nm : photons par seconde ?", "Rational(2,1000)/(3*10**-19)", "2*10**16/3", r"Un photon : $3\times10^{-19}$ J. $N=\frac{2\times10^{-3}}{3\times10^{-19}}\approx6{,}7\times10^{15}$ par seconde.")],
    "qe1": [_v(r"$\lambda=400$ nm, $v=3\times10^5$ m/s ($hc=1200$ eV·nm, $m_ec^2=0{,}5$ MeV). $W$ (en eV) ?", "Rational(1200,400)-Rational(1,2)*500000*(3*10**5/Rational(3*10**8))**2", "11/4",
               r"$h\nu=3$ eV, $E_c=\frac12\times5\times10^5\times(10^{-3})^2=0{,}25$ eV, $W=2{,}75$ eV.")],
    "qe2": [_v(r"$W=2$ eV : longueur d'onde seuil (en nm, $hc=1240$) ?", "1240/Rational(2)", "620", r"$\lambda_s=\frac{1240}2=620$ nm.")],
    "qe3": [_v(r"$\lambda=250$ nm, $W=3{,}4$ eV, $hc=1240$ eV·nm. $E_c$ (en eV) ?", "1240/250-Rational(34,10)", "39/25", r"$E_c=4{,}96-3{,}4=1{,}56$ eV.")],
    "qe4": [_v(r"Électron émis d'énergie cinétique $0{,}45$ eV : vitesse (en m/s) ?", "sqrt(2*Rational(45,100)*Rational(16,10)*10**-19/(9*10**-31))", "4*10**5", r"$v=\sqrt{\frac{2\times0{,}45\times1{,}6\times10^{-19}}{9\times10^{-31}}}=\sqrt{1{,}6\times10^{11}}=4\times10^5$ m/s.")],
    "qb1": [_v(r"Énergie du niveau $n=4$ de l'hydrogène (en eV) ?", "-Rational(136,10)/16", "-17/20", r"$E_4=-\frac{13{,}6}{16}=-0{,}85$ eV.")],
    "qb2": [_v(r"Énergie à fournir pour passer de $n=1$ à $n=4$ (en eV) ?", "Rational(136,10)*(1-Rational(1,16))", "51/4", r"$13{,}6\times\frac{15}{16}=12{,}75$ eV.")],
    "qb3": [_v(r"Longueur d'onde (en nm) de $4\to2$ ($hc=1240$ eV·nm) ?", "1240/(Rational(136,10)*(Rational(1,4)-Rational(1,16)))", "24800/51", r"$\Delta E=13{,}6\times\frac3{16}=2{,}55$ eV, $\lambda=\frac{1240}{2{,}55}\approx486$ nm (bleu-vert, $H_\beta$).")],
    "qb4": [_v(r"On fournit $15$ eV à l'électron fondamental de l'hydrogène. Énergie cinétique finale (en eV) ?", "15-Rational(136,10)", "7/5", r"$15-13{,}6=1{,}4$ eV.")],
    "qb5": [_v(r"Longueur d'onde (en nm) de $6\to2$ ($hc=1240$) ?", "1240/(Rational(136,10)*(Rational(1,4)-Rational(1,36)))", "1240/Rational(136,10)*9/2",
               r"$\Delta E=13{,}6\times\frac29=3{,}02$ eV ; $\lambda=\frac{1240}{3{,}02}\approx410$ nm (violet).")],
    "qr1": [_v(r"Rayon de la couche $n=2$ de l'hydrogène (en m), $a_0=5\times10^{-11}$ m ?", "4*5*10**-11", "20*10**-11", r"$r_2=4a_0=2\times10^{-10}$ m.")],
    "qr2": [_v(r"Plus petit rayon de $\mathrm{Be}^{3+}$ ($Z=4$), $\frac{\hbar^2}{me^2}=5\times10^{-11}$ m (en m) ?", "5*10**-11/4", "125*10**-13", r"$r_1=\frac{5\times10^{-11}}4=1{,}25\times10^{-11}$ m.")],
    "qr3": [_v(r"Rayon de la couche $n=2$ de $\mathrm{Li}^{2+}$ (en m), $\frac{\hbar^2}{me^2}=5\times10^{-11}$ ?", "4*5*10**-11/3", "Rational(20,3)*10**-11", r"$r_2=\frac{n^2a_0}Z=\frac{4\times5\times10^{-11}}3\approx6{,}7\times10^{-11}$ m.")],
    "qr4": [_v(r"Énergie d'ionisation de $\mathrm{Be}^{3+}$ ($Z=4$) depuis le fondamental (en eV) ?", "Rational(136,10)*16", "1088/5", r"$13{,}6\times16=217{,}6$ eV.")],
    "qr5": [_v(r"Énergie d'ionisation de $\mathrm{B}^{4+}$ ($Z=5$) (en eV) ?", "Rational(136,10)*25", "340", r"$13{,}6\times25=340$ eV.")],
    "qr6": [_v(r"Photon émis par $\mathrm{Li}^{2+}$ lors de $3\to2$ : longueur d'onde (en nm, $hc=1240$) ?", "1240/(Rational(136,10)*9*(Rational(1,4)-Rational(1,9)))", "1240/17", r"$\Delta E=13{,}6\times9\times\frac5{36}=17$ eV, $\lambda=\frac{1240}{17}\approx72{,}9$ nm.")],
    "qd1": [_v(r"Électron ($9{,}1\times10^{-31}$ kg) à $10^6$ m/s : $\lambda$ (en m, $h=6{,}62\times10^{-34}$) ?", "Rational(662,100)*10**-34/(Rational(91,10)*10**-31*10**6)", "Rational(662,91)*10**-10", r"$\lambda=\frac{6{,}62\times10^{-34}}{9{,}1\times10^{-25}}\approx7{,}3\times10^{-10}$ m : de l'ordre de la distance interatomique.")],
    "qd2": [_v(r"Balle de $0{,}1$ kg à $10$ m/s : $\lambda$ (en m) ?", "Rational(662,100)*10**-34/(Rational(1,10)*10)", "Rational(662,100)*10**-34", r"$\lambda=\frac h{mv}=\frac{6{,}62\times10^{-34}}1=6{,}62\times10^{-34}$ m.")],
    "qd3": [_v(r"Même électron, vitesse connue à $0{,}1\,\%$ près : $\Delta x$ minimale (en m) ?", "Rational(662,100)*10**-34/(4*pi*Rational(91,10)*10**-31*95*Rational(1,1000))", "Rational(6620,3458)*10**-3/pi",
               r"$\Delta p=9{,}1\times10^{-31}\times95\times10^{-3}=8{,}6\times10^{-32}$ ; $\Delta x=\frac h{4\pi\Delta p}\approx6{,}1\times10^{-4}$ m.")],
    "qd4": [_v(r"Balle de $0{,}1$ kg à $95$ m/s, vitesse à $0{,}085\,\%$ : $\Delta x$ minimale (en m) ?", "Rational(662,100)*10**-34/(4*pi*Rational(1,10)*95*Rational(85,100000))", "Rational(662,323)*10**-32/pi", r"$\Delta p=0{,}1\times95\times8{,}5\times10^{-4}=8{,}1\times10^{-3}$ ; $\Delta x\approx6{,}5\times10^{-33}$ m.")],
    "qd5": [_v(r"Électron localisé à $\Delta x=5\times10^{-11}$ m : $\Delta p$ minimale (en kg·m·s$^{-1}$) ?", "Rational(662,100)*10**-34/(4*pi*5*10**-11)", "Rational(331,100)*10**-24/pi", r"$\Delta p=\frac h{4\pi\Delta x}=\frac{6{,}62\times10^{-34}}{4\pi\times5\times10^{-11}}\approx1{,}05\times10^{-24}$.")],
    "qw1": [_v(r"Même normalisation avec $x_0=2$ : $\Psi_0$ ?", "sqrt(2/Rational(2))", "1", r"$\Psi_0=\sqrt{\frac2{x_0}}=1$.")],
    "qw2": [_i(r"Même fonction $e^{-x/2}$ : probabilité dans $[0;1]$ ?", "exp(-x)", "0", "1", "1-exp(-1)", r"$P=\int_0^1e^{-x}dx=1-e^{-1}\approx0{,}632$.")],
    "qw3": [_v(r"Pour $x_0=4$ : valeur de $A$ pour $P\geq95\,\%$ ($\ln0{,}05\approx-3$) ?", "-(Rational(4)/2)*(-3)", "6", r"$A\geq-\frac{x_0}2\ln0{,}05\approx\frac{3x_0}2=6$.")],
    "qw4": [_i(r"Puits de largeur $2$ : $I=\int_0^2\sin^2\left(\frac{\pi x}2\right)dx$ ?", "sin(pi*x/2)**2", "0", "2", "1", r"$I=\frac L2=1$, donc $N=1$.")],
    "qw5": [_i(r"Même état fondamental, probabilité dans la première moitié $[0;\frac12]$ ?", "2*sin(pi*x)**2", "0", "Rational(1,2)", "Rational(1,2)", r"$\left[x-\frac{\sin2\pi x}{2\pi}\right]_0^{1/2}=\frac12$ (symétrie de $|\psi|^2$ autour de $\frac12$).")],
    "qm1": [_v(r"$\psi=Ne^{-\lambda x^2/2}$ avec $\lambda=4\pi$ : $N$ ?", "(4*pi/pi)**Rational(1,4)", "sqrt(2)", r"$N=\left(\frac\lambda\pi\right)^{1/4}=4^{1/4}=\sqrt2$.")],
    "qm2": [_i(r"Même calcul avec $\lambda=8$ ($N^2=\sqrt{\frac8\pi}$) : $\langle x^2\rangle$ ?", "x**2*sqrt(8/pi)*exp(-8*x**2)", "-oo", "oo", "Rational(1,16)", r"$\langle x^2\rangle=\frac1{2\lambda}=\frac1{16}$.")],
    "qm3": [_v(r"$\lambda=2$ : $\Delta x=\sqrt{\frac1{2\lambda}}$ ?", "sqrt(1/(2*Rational(2)))", "1/2", r"$\sqrt{\frac14}=\frac12$.")],
    "qm4": [_i(r"$\lambda=8$ : $\frac{\langle p^2\rangle}{\hbar^2}=\int|\psi'|^2dx$ avec $\psi'=-8x\psi$ ?", "64*x**2*sqrt(8/pi)*exp(-8*x**2)", "-oo", "oo", "4", r"$\lambda^2\langle x^2\rangle=\frac{\lambda}2=4$.")],
    "qm5": [_v(r"Pour $\lambda=8$ : $\Delta x=\frac14$, $\Delta p=2\hbar$. Rapport $\frac{\Delta x\,\Delta p}{\hbar/2}$ ?", "Rational(1,4)*2/(Rational(1,2))", "1", r"$\Delta x\,\Delta p=\frac\hbar2$ : rapport $1$ (indépendant de $\lambda$).")],
    "qm6": [_i(r"$x_0=8$ (donc $|\Psi|^2=\frac14e^{-x/4}$) : $\langle x\rangle$ ?", "x*Rational(1,4)*exp(-x/4)", "0", "oo", "4", r"$\langle x\rangle=\frac{x_0}2=4$.")],
    "qs1": [_v(r"Même électron dans $L=1$ nm : $E_1$ (en eV) ?", "(Rational(66,10)*10**-34)**2/(8*9*10**-31*(10**-9)**2)/(Rational(16,10)*10**-19)", "121/320", r"$E_1\propto\frac1{L^2}$ : $\frac{1{,}51}4\approx0{,}38$ eV.")],
    "qs2": [_v(r"$E_1=0{,}25$ eV : énergie de $n=5$ (en eV) ?", "25*Rational(1,4)", "25/4", r"$25\times0{,}25=6{,}25$ eV.")],
    "qs3": [_v(r"$E_1=0{,}6$ eV : photon de $n=3\to1$ (en nm, $hc=1240$) ?", "1240/(8*Rational(6,10))", "775/3", r"$\Delta E=8E_1=4{,}8$ eV, $\lambda=\frac{1240}{4{,}8}\approx258$ nm.")],
    "qs4": [_v(r"Normalisation pour $L=2$ : $A$ ?", "sqrt(2/Rational(2))", "1", r"$A=\sqrt{\frac2L}=1$.")],
    "qs5": [_v(r"On triple la largeur ($E_1=1{,}8$ eV) : nouvelle énergie (en eV) ?", "Rational(18,10)/3**2", "1/5", r"$\frac{1{,}8}9=0{,}2$ eV.")],
    "qv1": [_v(r"$\psi=N(2\psi_1+\psi_2+2\psi_3)$ : probabilité de $E_2$ ?", "1/Rational(4+1+4)", "1/9", r"$N^2\times9=1$, $P_2=N^2=\frac19$.")],
    "qv2": [_v(r"$\psi=N(3\psi_1+4\psi_2)$ : $\frac{\langle E\rangle}{E_1}$ ?", "(9*1+16*4)/Rational(25)", "73/25", r"$N^2=\frac1{25}$ ; $\langle E\rangle=\frac9{25}E_1+\frac{16}{25}\times4E_1=\frac{73}{25}E_1$.")],
    "qv3": [_i(r"Largeur $1$ : $\int_0^1\psi_2^2\,dx$ pour $\psi_2=\sqrt2\sin2\pi x$ ?", "2*sin(2*pi*x)**2", "0", "1", "1", r"Normalisation : $\delta_{22}=1$.")],
    "qv4": [_i(r"Calculer $\int_0^1\sin^4(\pi x)\,dx$.", "sin(pi*x)**4", "0", "1", "Rational(3,8)", r"$\sin^4=\frac38-\frac12\cos2u+\frac18\cos4u$, donc $\frac38$.")],
    "qv5": [_v(r"$\psi=N\sin^2(\pi x)$ sur $[0;1]$ ($\int\sin^4=\frac38$) : $N^2$ ?", "1/Rational(3,8)", "8/3", r"$N^2=\frac83$.")],
    "q2a": [_v(r"Boîte carrée : niveau $(3,2)$ en unités de $\frac{\hbar^2\pi^2}{2m}$ ?", "3**2+2**2", "13", r"$9+4=13$.")],
    "q2b": [_v(r"Électron dans une boîte carrée de côté $0{,}5$ nm : $E_{min}$ (en eV) ?", "2*(Rational(66,10)*10**-34)**2/(8*9*10**-31*(Rational(1,2)*10**-9)**2)/(Rational(16,10)*10**-19)", "121/40", r"$E_{min}\propto\frac1{L^2}$ : $4\times0{,}756\approx3{,}0$ eV.")],
    "q2c": [_v(r"Septième niveau, atteint pour $(3,3)$ ($2,5,8,10,13,17,18$) : $\frac{E}{E_{min}}$ ?", "(3**2+3**2)/Rational(2)", "9", r"$\frac{18}2=9$. Niveau non dégénéré.")],
    "q2d": [_v(r"$a=1$, $b=3$ ($E\propto n_x^2+\frac{n_y^2}9$) : premier niveau excité, atteint pour $(1,2)$ ?", "1**2+2**2/Rational(9)", "13/9", r"$1+\frac49=\frac{13}9$ (le fondamental vaut $\frac{10}9$).")],
    "q2e": [_v(r"Combien de couples $(n_x,n_y)$, avec $n_x,n_y\geq1$, vérifient $n_x^2+n_y^2=50$ ? ($50=1+49=25+25$)", "3", "3", r"$(1,7)$, $(7,1)$ et $(5,5)$ : trois niveaux dégénérés.")],
    "qq1": [_v(r"$\alpha=\frac12$ : probabilité de mesurer $|0\rangle$ ?", "Rational(1,2)**2", "1/4", r"$|\alpha|^2=\frac14$.")],
    "qq2": [_v(r"$\alpha=\frac35$ : probabilité de mesurer $|1\rangle$ ?", "1-Rational(3,5)**2", "16/25", r"$1-\frac9{25}=\frac{16}{25}$.")],
    "qq3": [_v(r"$H|1\rangle=\frac1{\sqrt2}(|0\rangle-|1\rangle)$ : probabilité de mesurer $|1\rangle$ ?", "(-1/sqrt(2))**2", "1/2", r"$\left|-\frac1{\sqrt2}\right|^2=\frac12$ : le signe n'influence pas la probabilité.")],
    "qq4": [_v(r"Porte $X=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ appliquée à $|0\rangle=\binom10$ : résultat ?", "Matrix([[0,1],[1,0]])*Matrix([1,0])", "Matrix([0,1])", r"$X|0\rangle=\binom01=|1\rangle$ : NOT.")],
    "qq5": [_v(r"CNOT sur $(5,6,7,8)$ : état de sortie ?", "Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])*Matrix([5,6,7,8])", "Matrix([5,6,8,7])", r"On échange $\gamma=7$ et $\delta=8$ : $(5,6,8,7)$.")],
    "qq6": [_v(r"Nombre de coefficients pour $20$ qubits ?", "2**20", "1048576", r"$2^{20}=1\,048\,576$.")],
    "qy1": [_v(r"Même expérience avec $W=5{,}75$ eV ($200$ nm, $hc=1240$) : $\lambda_{dB}$ des électrons (en m) ?", "Rational(66,10)*10**-34/(9*10**-31*sqrt(2*(Rational(1240,200)-Rational(575,100))*Rational(16,10)*10**-19/(9*10**-31)))", "Rational(11,6)*10**-9",
               r"$E_c=0{,}45$ eV, $v=4\times10^5$ m/s, $\lambda=\frac{6{,}6\times10^{-34}}{3{,}6\times10^{-25}}\approx1{,}8\times10^{-9}$ m.")],
    "qy2": [_v(r"Photon émis par $\mathrm{Li}^{2+}$ lors de $4\to2$ (en nm, $hc=1240$) ?", "1240/(Rational(136,10)*9*(Rational(1,4)-Rational(1,16)))", "24800/459", r"$\Delta E=13{,}6\times9\times\frac3{16}\approx22{,}95$ eV, $\lambda\approx54$ nm.")],
    "qy3": [_v(r"Puits avec $E_1=0{,}3$ eV : photon pour $n=2\to4$ (en nm, $hc=1240$) ?", "1240/(12*Rational(3,10))", "3100/9", r"$E_4-E_2=12E_1=3{,}6$ eV, $\lambda=\frac{1240}{3{,}6}\approx344$ nm.")],
    "qy4": [_v(r"Électron localisé à $\Delta x=10^{-10}$ m : $\Delta v$ minimale (en m/s) ?", "Rational(662,100)*10**-34/(4*pi*10**-10)/(Rational(91,10)*10**-31)", "Rational(331,1820)*10**7/pi", r"$\Delta p\approx5{,}3\times10^{-25}$ ; $\Delta v=\frac{\Delta p}m\approx5{,}8\times10^5$ m/s.")],
}
for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["id"] in VARIANTS:
            _e["variants"] = VARIANTS[_e["id"]]


EXTRA_PARTS = []

QUIZ = [
    {"notion": "rappels", "type": "qcm", "q": r"Un électron a une énergie de $1$ eV. En joules, cela fait environ :", "choix": [r"$1{,}6\times10^{-19}$ J", r"$1{,}6\times10^{19}$ J", r"$9\times10^{-31}$ J", r"$6{,}6\times10^{-34}$ J"], "bonne": 0},
    {"notion": "rappels", "type": "vf", "q": r"Une onde stationnaire sur une corde fixée aux deux extrémités ne peut avoir que certaines longueurs d'onde.", "bonne": True},
    {"notion": "coulomb", "type": "qcm", "q": r"Pour un mouvement circulaire uniforme de rayon $r$ et de vitesse $v$, l'accélération vaut :", "choix": [r"$\dfrac{v^2}r$", r"$\dfrac vr$", r"$vr$", r"$0$"], "bonne": 0},
    {"notion": "coulomb", "type": "vf", "q": r"Si on double la distance entre deux charges, la force de Coulomb est divisée par $4$.", "bonne": True},
    {"notion": "photon", "type": "qcm", "q": r"L'énergie d'un photon de longueur d'onde $\lambda$ vaut :", "choix": [r"$\dfrac{hc}\lambda$", r"$hc\lambda$", r"$\dfrac{\lambda}{hc}$", r"$h\lambda$"], "bonne": 0},
    {"notion": "photon", "type": "vf", "q": r"La catastrophe ultraviolette désigne la divergence de l'énergie rayonnée par un corps noir prédite par la physique classique.", "bonne": True},
    {"notion": "photon", "type": "qcm", "q": r"Planck explique le rayonnement du corps noir en supposant que :", "choix": [r"l'énergie est échangée par paquets $h\nu$", r"la lumière est une onde continue", r"les électrons sont sur des orbites", r"la matière est continue"], "bonne": 0},
    {"notion": "photoelec", "type": "qcm", "q": r"Si la fréquence de la lumière est inférieure au seuil, augmenter son intensité :", "choix": [r"ne fait pas apparaître d'électrons", r"fait apparaître des électrons", r"augmente leur énergie cinétique", r"diminue le travail d'extraction"], "bonne": 0},
    {"notion": "photoelec", "type": "vf", "q": r"L'énergie cinétique des électrons émis vaut $h\nu-W$.", "bonne": True},
    {"notion": "bohr", "type": "qcm", "q": r"Pour passer de $n=4$ à $n=3$ dans l'hydrogène, l'électron :", "choix": [r"émet un photon", r"absorbe un photon", r"est ionisé", r"ne change pas d'énergie"], "bonne": 0},
    {"notion": "bohr", "type": "vf", "q": r"Dans le modèle de Bohr, l'énergie de l'électron est négative et vaut $\frac{E_1}{n^2}$.", "bonne": True},
    {"notion": "bohr", "type": "qcm", "q": r"Énergie minimale à fournir à un atome d'hydrogène fondamental pour l'ioniser :", "choix": [r"$13{,}6$ eV", r"$-13{,}6$ eV", r"$3{,}4$ eV", r"$0$ eV"], "bonne": 0},
    {"notion": "hydrogenoide", "type": "qcm", "q": r"Le rayon des orbites d'un hydrogénoïde varie comme :", "choix": [r"$\dfrac{n^2}Z$", r"$n^2Z$", r"$\dfrac Z{n^2}$", r"$\dfrac{n}{Z^2}$"], "bonne": 0},
    {"notion": "hydrogenoide", "type": "vf", "q": r"L'énergie d'ionisation de $\mathrm{He}^+$ est environ $4$ fois celle de l'hydrogène.", "bonne": True},
    {"notion": "debroglie", "type": "qcm", "q": r"La longueur d'onde de de Broglie d'une particule de quantité de mouvement $p$ est :", "choix": [r"$\dfrac hp$", r"$hp$", r"$\dfrac ph$", r"$\dfrac{h}{p^2}$"], "bonne": 0},
    {"notion": "debroglie", "type": "vf", "q": r"La nature ondulatoire d'une balle de tennis est facilement observable.", "bonne": False},
    {"notion": "heisenberg", "type": "qcm", "q": r"Le principe d'indétermination s'écrit :", "choix": [r"$\Delta x\,\Delta p\geq\dfrac\hbar2$", r"$\Delta x\,\Delta p=0$", r"$\Delta x+\Delta p\geq\hbar$", r"$\Delta x\,\Delta p\leq\dfrac\hbar2$"], "bonne": 0},
    {"notion": "heisenberg", "type": "vf", "q": r"L'indétermination d'Heisenberg vient d'un défaut des appareils de mesure.", "bonne": False},
    {"notion": "psi", "type": "qcm", "q": r"La condition de normalisation d'une fonction d'onde s'écrit :", "choix": [r"$\displaystyle\int|\psi|^2dx=1$", r"$\displaystyle\int\psi\,dx=1$", r"$|\psi|=1$", r"$\displaystyle\int|\psi|\,dx=0$"], "bonne": 0},
    {"notion": "psi", "type": "vf", "q": r"$|\psi(x)|^2$ est une densité de probabilité et peut dépasser $1$.", "bonne": True},
    {"notion": "moyennes", "type": "qcm", "q": r"L'incertitude sur $A$ se calcule par :", "choix": [r"$\sqrt{\langle A^2\rangle-\langle A\rangle^2}$", r"$\langle A\rangle^2-\langle A^2\rangle$", r"$\langle A\rangle$", r"$\sqrt{\langle A\rangle}$"], "bonne": 0},
    {"notion": "moyennes", "type": "vf", "q": r"Pour une fonction d'onde paire, la position moyenne $\langle x\rangle$ est nulle.", "bonne": True},
    {"notion": "schrodinger", "type": "qcm", "q": r"Dans un puits infini de largeur $L$, les énergies sont :", "choix": [r"$\dfrac{n^2\pi^2\hbar^2}{2mL^2}$", r"$\dfrac{n\pi\hbar}{2mL}$", r"$\dfrac{\hbar^2}{2mL^2}$", r"proportionnelles à $n$"], "bonne": 0},
    {"notion": "schrodinger", "type": "vf", "q": r"La condition $\psi(L)=0$ est ce qui impose la quantification de l'énergie.", "bonne": True},
    {"notion": "schrodinger", "type": "qcm", "q": r"La fonction $\psi_n$ du puits infini possède :", "choix": [r"$n-1$ n{\oe}uds", r"$n$ n{\oe}uds", r"$n+1$ n{\oe}uds", r"aucun n{\oe}ud"], "bonne": 0},
    {"notion": "superposition", "type": "vf", "q": r"Si $\psi=\sum c_n\psi_n$ est normalisée, alors $\sum|c_n|^2=1$.", "bonne": True},
    {"notion": "superposition", "type": "qcm", "q": r"L'énergie moyenne de $\psi=\sum c_n\psi_n$ est :", "choix": [r"$\sum|c_n|^2E_n$", r"$\sum c_nE_n$", r"$\sum E_n$", r"$\sum|c_n|E_n^2$"], "bonne": 0},
    {"notion": "boite2d", "type": "vf", "q": r"Dans une boîte 2D, l'énergie minimale est nulle.", "bonne": False},
    {"notion": "boite2d", "type": "qcm", "q": r"Deux états de même énergie sont dits :", "choix": [r"dégénérés", r"orthogonaux", r"normalisés", r"ionisés"], "bonne": 0},
    {"notion": "qubit", "type": "qcm", "q": r"Pour $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$, la mesure donne $|1\rangle$ avec la probabilité :", "choix": [r"$|\beta|^2$", r"$\beta$", r"$\dfrac12$", r"$|\alpha|^2$"], "bonne": 0},
    {"notion": "qubit", "type": "vf", "q": r"Un système de $n$ qubits est décrit par $2^n$ coefficients.", "bonne": True},
    {"notion": "qubit", "type": "qcm", "q": r"Que fait la porte CNOT ?", "choix": [r"inverse le second qubit si le premier vaut $|1\rangle$", r"inverse toujours le premier qubit", r"met les deux qubits en superposition", r"ne change rien"], "bonne": 0},
]

_E = r"$E=h\nu=\frac{hc}\lambda$ · $hc\approx1240$ eV·nm"
_EV = r"1 eV $=1{,}6\times10^{-19}$ J"
_BO = r"$E_n=\frac{E_1}{n^2}$, $E_1=-13{,}6$ eV · $h\nu=|E_i-E_f|$"
_HY = r"$r_n=\frac{n^2\hbar^2}{Zme^2}$ · $E_n=-13{,}6\frac{Z^2}{n^2}$ eV"
_COU = r"$F=\frac{ke^2}{r^2}$ · PFD : $\frac{Ze^2}{r^2}=\frac{mv^2}r$ · $a=\frac{v^2}r$"
_DB = r"$\lambda=\frac hp=\frac h{mv}$"
_HE = r"$\Delta x\Delta p\geq\frac\hbar2$ · $\Delta p=m\Delta v$"
_NORM = r"$\int|\psi|^2dx=1$ · $P(a:b)=\int_a^b|\psi|^2dx$"
_MOY = r"$\langle A\rangle=\int\psi^*\hat A\psi$ · $(\Delta A)^2=\langle A^2\rangle-\langle A\rangle^2$ · $\langle p^2\rangle=\hbar^2\int|\psi'|^2dx$"
_GAU = r"$\int e^{-\lambda x^2}=\sqrt{\frac\pi\lambda}$ · $\int x^2e^{-\lambda x^2}=\frac1{2\lambda}\sqrt{\frac\pi\lambda}$"
_PU = r"$-\frac{\hbar^2}{2m}\psi''=E\psi$ · $\psi(0)=\psi(L)=0$ · $E_n=\frac{n^2\pi^2\hbar^2}{2mL^2}$ · $\psi_n=\sqrt{\frac2L}\sin\frac{n\pi x}L$"
_SU = r"$\psi=\sum c_n\psi_n$ · $\sum|c_n|^2=1$ · $\langle E\rangle=\sum|c_n|^2E_n$"
_B2 = r"$E_{n_x,n_y}=\frac{\hbar^2\pi^2}{2m}\left(\frac{n_x^2}{a^2}+\frac{n_y^2}{b^2}\right)$"
_QB = r"$P(0)=|\alpha|^2$, $P(1)=|\beta|^2$ · $|\alpha|^2+|\beta|^2=1$"

FORMULES = {
    "qa1": r"$E_c=\frac12mv^2$", "qa2": _EV, "qa3": r"$c=\lambda f$", "qa4": r"$E_c=\frac12mv^2$ · " + _EV, "qa5": r"$L=n\frac\lambda2$ · $c=\lambda f$",
    "qc1": r"$F=\frac{kq^2}{r^2}$, $k=9\times10^9$", "qc2": r"$a=\frac{v^2}r$", "qc3": r"$mv^2=\frac{kq^2}r$", "qc4": r"$E_c=\frac{kq^2}{2r}$ · " + _EV,
    "qc5": r"$E_c=\frac{e^2}{2r}$ · $E_p=-\frac{e^2}r$ · $E=-\frac{e^2}{2r}$",
    "qp1": _E, "qp2": r"$\nu=\frac Eh$", "qp3": r"$E=\frac{hc}\lambda$ · $N=\frac PE$", "qp4": _E + r" · $\lambda=\frac{hc}{|\Delta E|}$", "qp5": r"catastrophe ultraviolette · quanta de Planck $E=h\nu$",
    "qe1": r"$E_c=h\nu-W$ · $E_c=\frac12m_ec^2\left(\frac vc\right)^2$ · $\frac{hc}\lambda$", "qe2": r"$\lambda_s=\frac{hc}W$", "qe3": r"$E_c=\frac{hc}\lambda-W$",
    "qe4": r"$v=\sqrt{\frac{2E_c}m}$ · " + _EV, "qe5": r"$E_c=h\nu-W$",
    "qb1": r"$E_n=\frac{E_1}{n^2}$", "qb2": _BO, "qb3": _BO + " · " + _E, "qb4": _BO + r" · $E_c=h\nu-|E_1|$", "qb5": _BO + " · " + _E,
    "qb6": _BO, "qb7": _BO + r" · $n\to\infty$ : $E=0$",
    "qr1": r"$r_n=n^2a_0$", "qr2": r"$r_n=\frac{n^2\hbar^2}{Zme^2}$", "qr3": r"$r_n=\frac{n^2\hbar^2}{Zme^2}$", "qr4": _HY, "qr5": _HY, "qr6": _HY + " · " + _E,
    "qr7": _COU, "qr8": _COU + r" · $mrv=n\hbar$", "qr9": r"$E=E_c+E_p=-\frac{Ze^2}{2r}$ · " + _HY,
    "qd1": _DB, "qd2": _DB, "qd3": _HE + r" · $\Delta x=\frac h{4\pi\Delta p}$", "qd4": _HE, "qd5": _HE, "qd6": _DB + " · " + _HE,
    "qw1": r"$\int_0^\infty\Psi_0^2e^{-2x/x_0}dx=\Psi_0^2\frac{x_0}2$", "qw2": _NORM, "qw3": _NORM + r" · $P=1-e^{-2A/x_0}$", "qw4": r"$\sin^2u=\frac{1-\cos2u}2$ · " + _NORM,
    "qw5": _NORM + r" · $\sin^2u=\frac{1-\cos2u}2$", "qw6": _NORM,
    "qm1": _GAU + r" · $N^2\sqrt{\frac\pi\lambda}=1$", "qm2": r"$\langle x^2\rangle=\int x^2|\psi|^2$ · " + _GAU, "qm3": _MOY, "qm4": _MOY + r" · $\psi'=-\lambda x\psi$",
    "qm5": _HE, "qm6": r"$\langle x\rangle=\int x|\psi|^2dx$ · intégration par parties", "qm7": _MOY + r" · $\hat p=-i\hbar\frac d{dx}$", "qm8": r"parité · $\langle x\rangle=\int x|\psi|^2dx$",
    "qs1": r"$E_1=\frac{h^2}{8mL^2}$ · " + _EV, "qs2": r"$E_n=n^2E_1$", "qs3": r"$E_n=n^2E_1$ · " + _E, "qs4": r"$A^2\frac L2=1$ · $\int_0^L\sin^2\frac{n\pi x}L=\frac L2$",
    "qs5": r"$E_1\propto\frac1{L^2}$", "qs6": _PU, "qs7": _PU, "qs8": _PU,
    "qv1": _SU, "qv2": _SU + r" · $E_n=n^2E_1$", "qv3": r"$\sin a\sin b=\frac12[\cos(a-b)-\cos(a+b)]$ · $\int\psi_n\psi_m=\delta_{nm}$", "qv4": r"$\sin^3u=\frac14(3\sin u-\sin3u)$ · $\int_0^\pi\sin^6=\frac{5\pi}{16}$",
    "qv5": _SU, "qv6": r"$\sin a\sin b=\frac12[\cos(a-b)-\cos(a+b)]$ · $\int\psi_n\psi_m=\delta_{nm}$",
    "qv7": r"$\sin^3u=\frac14(3\sin u-\sin3u)$ · " + _SU + r" · $E_n=n^2E_1$",
    "q2a": _B2, "q2b": _B2 + r" · $\frac{\hbar^2\pi^2}{m}=2\times\frac{h^2}{8mL^2}$", "q2c": _B2 + r" · carré : $E\propto n_x^2+n_y^2$", "q2d": _B2, "q2e": _B2,
    "q2f": _B2 + r" · $E_{min}=\frac{\hbar^2\pi^2}m$", "q2g": _B2 + " · dégénérescence",
    "qq1": _QB, "qq2": _QB, "qq3": r"$H|0\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2}$ · " + _QB, "qq4": r"$H=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ · $H^2=I$",
    "qq5": r"CNOT : $(\alpha,\beta,\gamma,\delta)\to(\alpha,\beta,\delta,\gamma)$", "qq6": r"$n$ qubits : $2^n$ coefficients", "qq7": _QB,
    "qy1": r"$E_c=\frac{hc}\lambda-W$ · $v=\sqrt{\frac{2E_c}m}$ · " + _DB, "qy2": _HY + " · " + _E, "qy3": r"$E_n=n^2E_1$ · " + _E, "qy4": _HE + " · " + _DB,
}
