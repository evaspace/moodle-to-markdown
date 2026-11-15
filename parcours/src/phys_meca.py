"""Level path: S1 physics, mechanics of a point (vectors, kinematics, dynamics, statics, Frenet).

Calibrated on the S1 physics midterms and finals 2022-2027 of `annales/raw/S1/*/Phys` (text-layer ones read
in full; scans only for the topics) and on the Moodle courses « Cours_cinématique_V4 » and the mechanics TDs.
g = 10 m/s² as in the exams. `value` exercises are checked by sympy; `open` ones have a model answer.
"""

SUBJECT = {
    "id": "physique-s1-meca",
    "ordre": 300,
    "matiere": "physique",
    "semestre": "S1",
    "ecue": "Mécanique",
    "titre": "Mécanique du point",
    "chapitres_moodle": ["02_Cours", "05_TD_Mécanique", "06_Corrigés_Mécanique"],
    "td": "TD mécanique (Moodle Physique)",
    "examens": ["Contrôle de physique (novembre)", "Partiel de physique (janvier)"],
}

NOTIONS = [
    {"id": "vecteurs", "titre": "Vecteurs, produit scalaire et vectoriel",
     "formule": r"$\vec u\cdot\vec v=\|\vec u\|\|\vec v\|\cos\alpha=x x'+y y'$ · $\vec u\cdot\vec v=0\iff$ orthogonaux · $\|\vec u\wedge\vec v\|=\|\vec u\|\|\vec v\||\sin\alpha|$ · composantes d'une force d'angle $\alpha$ avec $Ox$ : $(F\cos\alpha,\ F\sin\alpha)$",
     "exemple": r"$\vec F$ de norme $10$ N à $60^\circ$ de $Ox$ : $F_x=5$ N, $F_y=5\sqrt3$ N",
     "cours": r"Deux vecteurs colinéaires de sens opposés ont un produit scalaire strictement négatif ($\cos\pi=-1$). Le produit vectoriel est orthogonal aux deux vecteurs. Toujours dessiner l'angle avant de choisir sinus ou cosinus."},
    {"id": "derivation", "titre": "Dériver une fonction du temps",
     "formule": r"$\dfrac{d}{dt}f(\theta(t))=\dot\theta f'(\theta)$ · $\dfrac{d}{dt}\cos^2\theta=-2\dot\theta\cos\theta\sin\theta$ · $\dot x=\dfrac{dx}{dt}$, $\ddot x=\dfrac{d^2x}{dt^2}$",
     "exemple": r"$x(t)=10-2t^2$ : $\dot x=-4t$, $\ddot x=-4$",
     "cours": r"Une grandeur qui dépend de $t$ par l'intermédiaire de $\theta(t)$ se dérive comme une fonction composée : ne jamais oublier le facteur $\dot\theta$."},
    {"id": "cinematique", "titre": "Vitesse et accélération en cartésiennes",
     "formule": r"$\vec v=\dfrac{d\overrightarrow{OM}}{dt}=(\dot x,\dot y)$ · $\vec a=\dfrac{d\vec v}{dt}=(\ddot x,\ddot y)$ · $\|\vec v\|=\sqrt{\dot x^2+\dot y^2}$ · $\vec v\cdot\vec a>0$ accéléré, $<0$ décéléré, $=0$ trajectoire seule modifiée",
     "exemple": r"$x=3t^2-2t$ : $v=6t-2$, $a=6$",
     "cours": r"Uniforme : $\|\vec v\|$ constante (pas forcément rectiligne). Pour savoir si un mouvement accélère, regarder le signe de $\vec v\cdot\vec a$ et non celui de $a$."},
    {"id": "rectiligne", "titre": "Mouvement rectiligne uniformément varié",
     "formule": r"$a$ constante : $v=v_0+at$ · $x=x_0+v_0t+\frac12at^2$ · $v^2-v_0^2=2a(x-x_0)$ · $1\ \mathrm{km/h}=\frac1{3{,}6}\ \mathrm{m/s}$",
     "exemple": r"$v_0=20$ m/s, $a=-5$ m/s² : arrêt après $d=\dfrac{v_0^2}{2|a|}=40$ m",
     "cours": r"Convertir en unités SI avant tout calcul. Pour une distance sans le temps, utiliser $v^2-v_0^2=2a\Delta x$."},
    {"id": "projectile", "titre": "Chute libre et projectile",
     "formule": r"lancer de $v_0$, angle $\alpha$ : $x=v_0\cos\alpha\,t$, $y=v_0\sin\alpha\,t-\frac12gt^2$ · sommet : $v_y=0$, $t_S=\dfrac{v_0\sin\alpha}g$, $h=\dfrac{v_0^2\sin^2\alpha}{2g}$ · portée $\dfrac{v_0^2\sin2\alpha}g$ · trajectoire $y=x\tan\alpha-\dfrac{gx^2}{2v_0^2\cos^2\alpha}$",
     "exemple": r"chute de $5$ m sans vitesse initiale, $g=10$ : $t=\sqrt{2h/g}=1$ s, $v=10$ m/s",
     "cours": r"Le PFD donne $\vec a=\vec g$ : l'accélération ne dépend pas de la masse. Intégrer deux fois avec les conditions initiales. Pour la trajectoire, éliminer $t$ entre $x(t)$ et $y(t)$."},
    {"id": "polaires", "titre": "Coordonnées polaires",
     "formule": r"$\vec u_\rho=\cos\theta\,\vec u_x+\sin\theta\,\vec u_y$ · $\vec u_\theta=-\sin\theta\,\vec u_x+\cos\theta\,\vec u_y$ · $\dfrac{d\vec u_\rho}{dt}=\dot\theta\vec u_\theta$, $\dfrac{d\vec u_\theta}{dt}=-\dot\theta\vec u_\rho$ · $\overrightarrow{OM}=\rho\vec u_\rho$ · $x=\rho\cos\theta$, $y=\rho\sin\theta$",
     "exemple": r"$\rho=2$, $\theta=\frac\pi3$ : $x=1$, $y=\sqrt3$",
     "cours": r"La base polaire tourne avec le point : ses vecteurs ont une dérivée non nulle. $\vec v=\dot\rho\,\vec u_\rho+\rho\dot\theta\,\vec u_\theta$ et $\vec a=(\ddot\rho-\rho\dot\theta^2)\vec u_\rho+(2\dot\rho\dot\theta+\rho\ddot\theta)\vec u_\theta$."},
    {"id": "circulaire", "titre": "Mouvement circulaire",
     "formule": r"$\rho=R$ constant : $\vec v=R\dot\theta\,\vec u_\theta$ · $\vec a=-R\dot\theta^2\vec u_\rho+R\ddot\theta\,\vec u_\theta$ · uniforme ($\dot\theta=\omega$) : $\vec a=-R\omega^2\vec u_\rho$, $\|\vec a\|=\dfrac{v^2}R$ · $\omega=\dfrac{2\pi}T$",
     "exemple": r"$R=2$ m, $\omega=3$ rad/s : $v=6$ m/s, $a=18$ m/s²",
     "cours": r"Circulaire uniforme : l'accélération n'est pas nulle, elle est centripète (dirigée vers le centre). Circulaire décéléré : composante tangentielle $R\ddot\theta<0$."},
    {"id": "cylindrique", "titre": "Coordonnées cylindriques, hélice",
     "formule": r"$\vec v=\dot\rho\,\vec u_\rho+\rho\dot\theta\,\vec u_\theta+\dot z\,\vec u_z$ · hélice $x=R\cos\omega t$, $y=R\sin\omega t$, $z=H\omega t$ : $\|\vec v\|=\omega\sqrt{R^2+H^2}$, $\|\vec a\|=R\omega^2$",
     "exemple": r"$R=3$, $H=4$, $\omega=2$ : $\|\vec v\|=10$, $\|\vec a\|=12$",
     "cours": r"Les cylindriques sont les polaires plus la cote $z$ : la composante sur $\vec u_z$ s'ajoute simplement. Retrouver les normes cartésiennes sert de vérification."},
    {"id": "newton", "titre": "Lois de Newton et forces",
     "formule": r"1er : sans interaction (ou forces qui se compensent), $\vec v$ constant · 2e : $\sum\vec F=m\vec a=\dfrac{d\vec p}{dt}$, $\vec p=m\vec v$ · 3e : $\vec F_{1\to2}=-\vec F_{2\to1}$ · poids $\vec P=m\vec g$ · gravitation $F=G\dfrac{m_1m_2}{d^2}$ · frottement fluide $\vec f=-\alpha\vec v$",
     "exemple": r"$m=0{,}5$ kg, $F=3$ N : $a=6$ m/s²",
     "cours": r"Méthode : référentiel galiléen, système, bilan des forces (schéma), PFD, projection sur des axes, résolution. Le principe d'inertie ne dit rien d'un corps dont les forces ne se compensent pas."},
    {"id": "incline", "titre": "Plan incliné et poulies",
     "formule": r"sans frottement, angle $\alpha$ : $a=g\sin\alpha$ le long du plan · $R=mg\cos\alpha$ · fil inextensible : même accélération · poulie idéale : même tension",
     "exemple": r"$\alpha=30^\circ$ : $a=5$ m/s²",
     "cours": r"Choisir un axe le long du plan et un axe normal. Pour deux masses reliées, écrire le PFD sur chacune avec la même tension $T$, puis résoudre le système : additionner pour trouver $a$, remplacer pour trouver $T$."},
    {"id": "frottement", "titre": "Frottement fluide",
     "formule": r"$m\dot v=mg-\alpha v$ · $v(t)=v_\ell\left(1-e^{-t/\tau}\right)$ · $v_\ell=\dfrac{mg}\alpha$ · $\tau=\dfrac m\alpha$",
     "exemple": r"$m=2$ kg, $\alpha=4$ : $v_\ell=5$ m/s, $\tau=0{,}5$ s",
     "cours": r"Équation différentielle du premier ordre : solution homogène $Ke^{-t/\tau}$ plus solution particulière constante $v_\ell$. La vitesse limite est atteinte quand l'accélération s'annule."},
    {"id": "moment", "titre": "Moments et équilibre",
     "formule": r"$M_\Delta(\vec F)=\pm\,d\,F=\pm\,OA\,F\sin\varphi$ · équilibre : $\sum\vec F=\vec0$ et $\sum M_\Delta=0$ · $\vec M=\overrightarrow{OA}\wedge\vec F$ est orthogonal à $\vec F$",
     "exemple": r"$F=10$ N à $d=0{,}5$ m, perpendiculaire : $M=5$ N·m",
     "cours": r"Choisir l'axe de rotation sur le point où s'applique la force inconnue : son moment est nul. Le poids d'une poutre homogène s'applique en son milieu. Signe : sens trigonométrique positif."},
    {"id": "frenet", "titre": "Repère de Frenet et gouttière",
     "formule": r"$\vec a=\dfrac{dv}{dt}\vec u_T+\dfrac{v^2}{r}\vec u_N$ · gouttière sans frottement : $a_T=g\sin\theta$, $V^2=2gr(1-\cos\theta)$ · quitte le support quand $R=0$",
     "exemple": r"$\theta=60^\circ$, $r=1$ m, $g=10$ : $V^2=10$ m²/s²",
     "cours": r"Projeter le PFD sur la tangente puis sur la normale. La réaction se déduit de la composante normale. La relation $V^2$ vient de la conservation de l'énergie ou de l'intégration de $a_T$."},
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


M21 = "Contrôle de physique novembre (S1)"
F20 = "Partiel de physique janvier (S1)"

LEVELS = [
    {"n": 1, "titre": "Vecteurs et produits", "notions": ["vecteurs"], "exos": [
        v("pv1", r"$\vec u=(1,2)$ et $\vec v=(3,-1)$. Calculer $\vec u\cdot\vec v$.", "Matrix([1,2]).dot(Matrix([3,-1]))", "1", r"$1\times3+2\times(-1)=1$.", duree=2),
        v("pv2", r"$\vec u=(2,0,1)$ et $\vec v=(1,3,0)$. Calculer $\|\vec u\wedge\vec v\|$.", "Matrix([2,0,1]).cross(Matrix([1,3,0])).norm()", "sqrt(46)",
          r"$\vec u\wedge\vec v=(0\cdot0-1\cdot3,\ 1\cdot1-2\cdot0,\ 2\cdot3-0\cdot1)=(-3,1,6)$, norme $\sqrt{9+1+36}=\sqrt{46}$.", duree=3),
        v("pv3", r"Une force de norme $10$ N fait un angle de $60^\circ$ avec l'axe $Ox$. Quelle est sa composante $F_x$ (en N) ?", "10*cos(pi/3)", "5", r"$F_x=F\cos\alpha=10\times\frac12=5$ N.", duree=2),
        v("pv4", r"$\|\vec V_1\|=3$, $\|\vec V_2\|=4$ et l'angle entre eux vaut $30^\circ$. Calculer $\|\vec V_1\wedge\vec V_2\|$.", "3*4*sin(pi/6)", "6", r"$V_1V_2|\sin\alpha|=12\times\frac12=6$.", duree=2),
        o("pv5", r"Quel est le signe du produit scalaire de deux vecteurs non nuls colinéaires et de sens opposés ? Que vaut-il pour deux vecteurs orthogonaux ?",
          r"Strictement négatif : $\vec u\cdot\vec v=\|\vec u\|\|\vec v\|\cos\pi=-\|\vec u\|\|\vec v\|$. Nul pour deux vecteurs orthogonaux ($\cos\frac\pi2=0$).", duree=2),
    ]},
    {"n": 2, "titre": "Dériver en fonction du temps", "notions": ["derivation"], "exos": [
        v("pd1", r"$x(t)=10-2t^2$. Calculer l'accélération $\ddot x$.", "diff(10-2*t**2, t, 2)", "-4", r"$\dot x=-4t$, $\ddot x=-4$ m/s².", duree=2),
        v("pd2", r"$x(t)=e^{2t}$. Calculer la vitesse $\dot x$ à l'instant $t=0$.", "diff(exp(2*t), t).subs(t, 0)", "2", r"$\dot x=2e^{2t}$, soit $2$ en $t=0$.", duree=2),
        o("pd3", r"$f(t)=A\cos^2(\theta(t))$, $A$ constante. Calculer $\dfrac{df}{dt}$.", r"$f'=A\cdot2\cos\theta\cdot(-\sin\theta)\cdot\dot\theta=-2A\dot\theta\cos\theta\sin\theta$.", src="Contrôle 1 de physique, QCM 4", duree=3),
        v("pd4", r"$x(t)=A\left(\omega t-\sin\omega t\right)$ avec $A=2$, $\omega=3$. Calculer $\dot x$ en $t=\dfrac\pi3$.", "diff(2*(3*t-sin(3*t)), t).subs(t, pi/3)", "12",
          r"$\dot x=A\omega(1-\cos\omega t)=6(1-\cos\pi)=12$.", duree=3),
        o("pd5", r"Dériver par rapport à $\theta$ puis par rapport à $t$ les vecteurs $\vec u_\rho=\cos\theta\,\vec u_x+\sin\theta\,\vec u_y$ et $\vec u_\theta=-\sin\theta\,\vec u_x+\cos\theta\,\vec u_y$.",
          r"$\dfrac{d\vec u_\rho}{d\theta}=-\sin\theta\,\vec u_x+\cos\theta\,\vec u_y=\vec u_\theta$ et $\dfrac{d\vec u_\theta}{d\theta}=-\cos\theta\,\vec u_x-\sin\theta\,\vec u_y=-\vec u_\rho$. Avec la dérivée composée : $\dfrac{d\vec u_\rho}{dt}=\dot\theta\vec u_\theta$ et $\dfrac{d\vec u_\theta}{dt}=-\dot\theta\vec u_\rho$.", src=M21 + ", ex. 2", duree=5),
    ]},
    {"n": 3, "titre": "Vitesse et accélération cartésiennes", "notions": ["cinematique", "derivation"], "exos": [
        v("pc1", r"$x(t)=3t^2-2t$. Calculer la vitesse à $t=2$ s.", "diff(3*t**2-2*t, t).subs(t, 2)", "10", r"$v=6t-2=10$ m/s.", duree=2),
        v("pc2", r"$x(t)=t^3$ et $y(t)=2t$. Donner le vecteur accélération à $t=1$.", "Matrix([diff(t**3, t, 2), diff(2*t, t, 2)]).subs(t, 1)", "Matrix([6,0])", r"$\ddot x=6t=6$, $\ddot y=0$ : $\vec a=(6,0)$.", duree=2),
        v("pc3", r"Cycloïde $x=A(\omega t-\sin\omega t)$, $y=A(1-\cos\omega t)$, $A=2$, $\omega=3$. Calculer $\|\vec v\|$ à $t=\dfrac\pi3$.",
          "Matrix([diff(2*(3*t-sin(3*t)), t), diff(2*(1-cos(3*t)), t)]).subs(t, pi/3).norm()", "12",
          r"$\vec v=A\omega(1-\cos\omega t,\ \sin\omega t)$. En $\omega t=\pi$ : $\vec v=(12,0)$, norme $12$.", duree=4),
        o("pc4", r"Cycloïde $x=A(\omega t-\sin\omega t)$, $y=A(1-\cos\omega t)$. Calculer $\vec v$, $\vec a$ et leurs normes (on donne $1-\cos\alpha=2\sin^2\frac\alpha2$).",
          r"$\vec v=A\omega(1-\cos\omega t,\ \sin\omega t)$, $\vec a=A\omega^2(\sin\omega t,\ \cos\omega t)$." "\n\n"
          r"$\|\vec v\|^2=A^2\omega^2\left[(1-\cos\omega t)^2+\sin^2\omega t\right]=2A^2\omega^2(1-\cos\omega t)=4A^2\omega^2\sin^2\frac{\omega t}2$, donc $\|\vec v\|=2A\omega\left|\sin\frac{\omega t}2\right|$." "\n\n"
          r"$\|\vec a\|=A\omega^2$ (constante).", src="Contrôle 1 de physique, ex. 1 (6 points)", duree=10),
        o("pc5", r"Un mobile suit $x(t)=10-2t^2$ ($t>0$). Le mouvement est-il uniforme ? accéléré ou décéléré ? Quelle est la norme de l'accélération ?",
          r"$v=-4t$, $a=-4$ m/s². $v$ varie : pas uniforme. $v\,a=16t>0$ : $\vec v$ et $\vec a$ de même sens, le mouvement est accéléré. $\|\vec a\|=4$ m/s².", src=M21 + ", QCM 3", duree=4),
    ]},
    {"n": 4, "titre": "Mouvement rectiligne uniformément varié", "notions": ["rectiligne"], "exos": [
        v("pr1", r"Un mobile part de $x_0=0$ avec $v_0=5$ m/s et $a=2$ m/s². Quelle est sa position (en m) à $t=3$ s ?", "5*3+Rational(1,2)*2*3**2", "24", r"$x=v_0t+\frac12at^2=15+9=24$ m.", duree=2),
        v("pr2", r"Une voiture roule à $20$ m/s et freine avec $a=-5$ m/s². Quelle distance parcourt-elle avant de s'arrêter (en m) ?", "20**2/(2*5)", "40", r"$v^2-v_0^2=2a\Delta x$ avec $v=0$ : $\Delta x=\frac{400}{10}=40$ m.", duree=3),
        v("pr3", r"Une voiture passe de $72$ km/h à $108$ km/h avec $a=2$ m/s². Combien de secondes ?", "(108/Rational(36,10)-72/Rational(36,10))/2", "5", r"$72$ km/h $=20$ m/s, $108$ km/h $=30$ m/s. $t=\frac{30-20}2=5$ s.", duree=3),
        o("pr4", r"Pour $a$ constante, démontrer $v^2-v_0^2=2a(x-x_0)$.", r"$v=v_0+at$ et $x-x_0=v_0t+\frac12at^2$. Donc $t=\frac{v-v_0}a$ et $x-x_0=\frac{v_0(v-v_0)}a+\frac{(v-v_0)^2}{2a}=\frac{(v-v_0)(v+v_0)}{2a}=\frac{v^2-v_0^2}{2a}$.", duree=5),
    ]},
    {"n": 5, "titre": "Chute libre et projectile", "notions": ["projectile", "rectiligne"], "exos": [
        v("pj1", r"Chute libre sans vitesse initiale d'une hauteur de $5$ m, $g=10$ m/s². Durée de chute (en s) ?", "sqrt(2*5/10)", "1", r"$h=\frac12gt^2$ : $t=\sqrt{2h/g}=1$ s.", duree=2),
        v("pj2", r"Même chute : vitesse d'arrivée au sol (en m/s) ?", "sqrt(2*10*5)", "10", r"$v^2=2gh=100$ : $v=10$ m/s.", duree=2),
        v("pj3", r"Projectile lancé à $v_0=20$ m/s avec $\alpha=30^\circ$, $g=10$ m/s². Hauteur maximale (en m) ?", "(20*sin(pi/6))**2/(2*10)", "5", r"$h=\frac{(v_0\sin\alpha)^2}{2g}=\frac{100}{20}=5$ m.", duree=3),
        v("pj4", r"Même projectile : durée du vol jusqu'au retour à la hauteur de départ (en s) ?", "2*20*sin(pi/6)/10", "2", r"$t=\frac{2v_0\sin\alpha}g=\frac{2\times10}{10}=2$ s.", duree=3),
        v("pj5", r"Même projectile : portée (en m) ?", "20**2*sin(pi/3)/10", "20*sqrt(3)", r"$\frac{v_0^2\sin2\alpha}g=\frac{400\sin60^\circ}{10}=20\sqrt3$ m.", duree=3),
        o("pj6", r"$\overrightarrow{OM}=\big(v_0\cos\alpha\,t,\ v_0\sin\alpha\,t-5t^2\big)$. 1. Équations horaires. 2. Équation de la trajectoire. 3. Vecteur vitesse et sa norme. 4. Hauteur maximale.",
          r"1. $x=v_0\cos\alpha\,t$, $y=v_0\sin\alpha\,t-5t^2$." "\n\n"
          r"2. $t=\frac x{v_0\cos\alpha}$ donne $y=x\tan\alpha-\dfrac{5x^2}{v_0^2\cos^2\alpha}$ : une parabole." "\n\n"
          r"3. $\vec v=(v_0\cos\alpha,\ v_0\sin\alpha-10t)$, $\|\vec v\|=\sqrt{v_0^2-20v_0\sin\alpha\,t+100t^2}$." "\n\n"
          r"4. Au sommet $v_y=0$ : $t_S=\frac{v_0\sin\alpha}{10}$, $y_S=\dfrac{v_0^2\sin^2\alpha}{20}$.", src=M21 + ", ex. 3 (5,5 points)", duree=10),
    ]},
    {"n": 6, "titre": "Coordonnées polaires", "notions": ["polaires", "derivation"], "exos": [
        v("pp1", r"Un point a pour coordonnées polaires $\rho=2$, $\theta=\dfrac\pi3$. Quelle est son abscisse $x$ ?", "2*cos(pi/3)", "1", r"$x=\rho\cos\theta=1$.", duree=2),
        v("pp2", r"Un point a pour coordonnées cartésiennes $(1,1)$. Quel est son $\rho$ ?", "sqrt(1+1)", "sqrt(2)", r"$\rho=\sqrt{x^2+y^2}=\sqrt2$ et $\theta=\frac\pi4$.", duree=2),
        o("pp3", r"Exprimer $\vec u_\rho$ et $\vec u_\theta$ dans la base cartésienne. Exprimer $\overrightarrow{OM}$ dans les deux bases.",
          r"$\vec u_\rho=\cos\theta\,\vec u_x+\sin\theta\,\vec u_y$, $\vec u_\theta=-\sin\theta\,\vec u_x+\cos\theta\,\vec u_y$. $\overrightarrow{OM}=x\vec u_x+y\vec u_y=\rho\vec u_\rho$ avec $x=\rho\cos\theta$, $y=\rho\sin\theta$.", src=M21 + ", ex. 2", duree=4),
        o("pp4", r"Démontrer $\vec v=\dot\rho\,\vec u_\rho+\rho\dot\theta\,\vec u_\theta$ en partant de $\overrightarrow{OM}=\rho\,\vec u_\rho$.",
          r"$\vec v=\frac{d(\rho\vec u_\rho)}{dt}=\dot\rho\,\vec u_\rho+\rho\frac{d\vec u_\rho}{dt}=\dot\rho\,\vec u_\rho+\rho\dot\theta\,\vec u_\theta$, car $\frac{d\vec u_\rho}{dt}=\dot\theta\vec u_\theta$.", src=M21 + ", ex. 2 q. 5", duree=4),
        o("pp5", r"$\rho(t)=\rho_0e^{\omega t}$ et $\theta(t)=\omega t$. Donner $x(t)$ et $y(t)$.", r"$x=\rho\cos\theta=\rho_0e^{\omega t}\cos\omega t$ et $y=\rho\sin\theta=\rho_0e^{\omega t}\sin\omega t$.", src="Contrôle 1 de physique, QCM 8", duree=3),
        o("pp6", r"Établir $\vec a=(\ddot\rho-\rho\dot\theta^2)\vec u_\rho+(2\dot\rho\dot\theta+\rho\ddot\theta)\vec u_\theta$.",
          r"$\vec a=\frac{d}{dt}\big(\dot\rho\,\vec u_\rho+\rho\dot\theta\,\vec u_\theta\big)=\ddot\rho\,\vec u_\rho+\dot\rho\dot\theta\,\vec u_\theta+(\dot\rho\dot\theta+\rho\ddot\theta)\vec u_\theta-\rho\dot\theta^2\vec u_\rho$, soit le résultat.", duree=6),
    ]},
    {"n": 7, "titre": "Mouvement circulaire", "notions": ["circulaire", "polaires"], "exos": [
        v("pq1", r"Mouvement circulaire uniforme de rayon $R=2$ m et $\omega=3$ rad/s. Norme de l'accélération (en m/s²) ?", "2*3**2", "18", r"$a=R\omega^2=18$.", duree=2),
        v("pq2", r"Mouvement circulaire uniforme de rayon $2$ m et de période $4$ s. Vitesse (en m/s) ?", "2*pi/4*2", "pi", r"$\omega=\frac{2\pi}T=\frac\pi2$ et $v=R\omega=\pi$ m/s.", duree=2),
        v("pq3", r"Spirale $\rho=e^{2t}$, $\theta=2t$. Norme de la vitesse à $t=0$ ?", "sqrt(diff(exp(2*t), t).subs(t, 0)**2+(exp(2*t)*2).subs(t, 0)**2)", "2*sqrt(2)",
          r"$\dot\rho=2$ et $\rho\dot\theta=2$ en $t=0$ : $\|\vec v\|=\sqrt{4+4}=2\sqrt2$.", duree=3),
        o("pq4", r"Mouvement circulaire de rayon $R$ : écrire $\vec a$ d'après la formule générale. Que devient-elle si le mouvement est aussi uniforme ?",
          r"$\dot\rho=\ddot\rho=0$ : $\vec a=-R\dot\theta^2\vec u_\rho+R\ddot\theta\,\vec u_\theta$. Uniforme : $\dot\theta=\omega$ constante, $\ddot\theta=0$, donc $\vec a=-R\omega^2\vec u_\rho$, dirigée vers le centre (centripète) et non nulle.", src=M21 + ", ex. 4", duree=4),
        o("pq5", r"Mouvement circulaire décéléré de rayon $R$ : quelle est la composante de l'accélération sur $\vec u_\theta$ ? son signe ?",
          r"$a_\theta=R\ddot\theta$. Décéléré signifie $\dot\theta$ diminue, donc $\ddot\theta<0$ (pour $\dot\theta>0$) : $a_\theta<0$. La composante radiale reste $-R\dot\theta^2$.", src="Contrôle 1 de physique, QCM 6", duree=3),
    ]},
    {"n": 8, "titre": "Cylindriques et hélice", "notions": ["cylindrique", "circulaire"], "exos": [
        v("pe1", r"Hélice $x=R\cos\omega t$, $y=R\sin\omega t$, $z=H\omega t$ avec $R=3$, $H=4$, $\omega=2$. Norme de la vitesse ?", "2*sqrt(3**2+4**2)", "10", r"$\vec v=(-R\omega\sin,\ R\omega\cos,\ H\omega)$ : $\|\vec v\|=\omega\sqrt{R^2+H^2}=10$.", duree=3),
        v("pe2", r"Même hélice : norme de l'accélération ?", "3*2**2", "12", r"$\vec a=(-R\omega^2\cos,\ -R\omega^2\sin,\ 0)$ : $\|\vec a\|=R\omega^2=12$.", duree=3),
        o("pe3", r"Hélice $x=R\cos\omega t$, $y=R\sin\omega t$, $z=H\omega t$ : exprimer $\overrightarrow{OM}$, $\vec v$ et $\vec a$ en coordonnées cylindriques et retrouver les normes.",
          r"$\rho=R$, $\theta=\omega t$, $z=H\omega t$ : $\overrightarrow{OM}=R\vec u_\rho+H\omega t\,\vec u_z$." "\n\n"
          r"$\vec v=R\omega\,\vec u_\theta+H\omega\,\vec u_z$, $\|\vec v\|=\omega\sqrt{R^2+H^2}$." "\n\n"
          r"$\vec a=-R\omega^2\vec u_\rho$, $\|\vec a\|=R\omega^2$. On retrouve les normes cartésiennes.", src="Contrôle 1 de physique, ex. 2 (6 points)", duree=10),
    ]},
    {"n": 9, "titre": "Lois de Newton", "notions": ["newton"], "exos": [
        v("pn1", r"Quel est le poids (en N) d'un objet de masse $2$ kg, avec $g=10$ m/s² ?", "2*10", "20", r"$P=mg=20$ N.", duree=1),
        v("pn2", r"On double la distance entre deux masses. Par quel facteur la force de gravitation est-elle multipliée ?", "Rational(1,2)**2", "1/4", r"$F=G\frac{m_1m_2}{d^2}$ : $d\to2d$ donne $F\to F/4$.", duree=2),
        v("pn3", r"Un corps de masse $0{,}5$ kg subit une force résultante de $3$ N. Quelle accélération (en m/s²) ?", "3/Rational(1,2)", "6", r"$a=F/m=6$.", duree=1),
        v("pn4", r"Quantité de mouvement (en kg·m/s) d'un corps de $3$ kg à $4$ m/s ?", "3*4", "12", r"$p=mv=12$.", duree=1),
        o("pn5", r"Une balle lâchée tombe verticalement, mouvement non uniforme. Que dit le principe d'inertie ?",
          r"Rien sur ce cas : il décrit un corps soumis à des forces qui se compensent. Ici la vitesse varie, donc les forces (le poids) ne se compensent pas : c'est le PFD qui s'applique.", src=F20 + ", QCM 8", duree=3),
        o("pn6", r"Chute libre depuis $y_0=5$ m sans vitesse initiale. Établir $a$, $v(t)$ et $y(t)$ avec le PFD.",
          r"Poids seul, axe $y$ vers le haut : $-mg=ma$, donc $a=-g$ (indépendant de $m$). $v=-gt$ (car $v(0)=0$) et $y=y_0-\frac12gt^2$.", duree=5),
    ]},
    {"n": 10, "titre": "Plan incliné et poulies", "notions": ["incline", "newton"], "exos": [
        v("pi1", r"Bloc sur un plan incliné de $30^\circ$, sans frottement, $g=10$. Accélération le long du plan (en m/s²) ?", "10*sin(pi/6)", "5", r"$a=g\sin\alpha=5$.", duree=2),
        v("pi2", r"Bloc de $2$ kg sur un plan incliné de $60^\circ$ : norme de la réaction normale (en N) ?", "2*10*cos(pi/3)", "10", r"$R=mg\cos\alpha=20\times\frac12=10$ N.", duree=2),
        v("pi3", r"$m_1=0{,}8$ kg sur un plan incliné de $30^\circ$ (sans frottement), relié par un fil et une poulie idéale à $m=1$ kg qui pend. $g=10$. Accélération de $m$ (en m/s²) ?",
          "(1*10-Rational(4,5)*10*sin(pi/6))/(1+Rational(4,5))", "10/3",
          r"$m$ : $mg-T=ma$. $m_1$ : $T-m_1g\sin\alpha=m_1a$. Somme : $a=\dfrac{mg-m_1g\sin\alpha}{m+m_1}=\dfrac{10-4}{1{,}8}=\dfrac{10}3$ m/s².", src=F20 + ", ex. 1", duree=6),
        v("pi4", r"Même montage : tension du fil (en N) ?", "1*(10-Rational(10,3))", "20/3", r"$T=m(g-a)=10-\frac{10}3=\frac{20}3$ N.", src=F20 + ", ex. 1", duree=3),
        v("pi5", r"Même montage : norme de la réaction du plan sur $m_1$ (en N) ?", "Rational(4,5)*10*cos(pi/6)", "4*sqrt(3)", r"$R=m_1g\cos\alpha=8\times\frac{\sqrt3}2=4\sqrt3$ N.", src=F20 + ", ex. 1", duree=3),
        o("pi6", r"Machine d'Atwood : deux masses $m_1 < m_2$ reliées par un fil sur une poulie idéale. Établir l'accélération et la tension.",
          r"$m_2g-T=m_2a$ et $T-m_1g=m_1a$ (même $a$ et même $T$). Somme : $a=\dfrac{m_2-m_1}{m_1+m_2}g$. Puis $T=m_1(g+a)=\dfrac{2m_1m_2}{m_1+m_2}g$.", duree=6),
    ]},
    {"n": 11, "titre": "Frottement fluide", "notions": ["frottement", "newton"], "exos": [
        v("pf1", r"Chute avec frottement $-\alpha\vec v$, $m=2$ kg, $\alpha=4$ kg/s, $g=10$. Vitesse limite (en m/s) ?", "2*10/4", "5", r"$v_\ell=\frac{mg}\alpha=5$ m/s.", duree=2),
        v("pf2", r"Même chute : constante de temps $\tau$ (en s) ?", "Rational(2,4)", "1/2", r"$\tau=\frac m\alpha=\frac12$ s.", duree=2),
        v("pf3", r"Quelle fraction de $v_\ell$ la vitesse atteint-elle à $t=\tau$ ?", "1-exp(-1)", "1-exp(-1)", r"$v(\tau)=v_\ell(1-e^{-1})\approx0{,}63\,v_\ell$.", duree=2),
        o("pf4", r"Établir $v(t)$ pour une chute sans vitesse initiale avec frottement $-\alpha\vec v$ (axe vers le bas).",
          r"PFD : $m\dot v=mg-\alpha v$, soit $\dot v+\frac\alpha mv=g$. Homogène : $Ke^{-\alpha t/m}$. Particulière constante : $\frac{mg}\alpha$. Avec $v(0)=0$ : $K=-\frac{mg}\alpha$, donc $v(t)=\frac{mg}\alpha\left(1-e^{-\alpha t/m}\right)$.", duree=8),
    ]},
    {"n": 12, "titre": "Moments et équilibre", "notions": ["moment"], "exos": [
        v("pm1", r"Force de $10$ N appliquée à $0{,}5$ m de l'axe, perpendiculairement au bras de levier. Valeur du moment (en N·m) ?", "10*Rational(1,2)", "5", r"$M=Fd=5$ N·m.", duree=1),
        v("pm2", r"Même force à $0{,}5$ m, mais faisant $30^\circ$ avec le bras. Moment (en N·m) ?", "10*Rational(1,2)*sin(pi/6)", "5/2", r"$M=Fd\sin30^\circ=2{,}5$ N·m.", duree=2),
        v("pm3", r"Poutre horizontale homogène de longueur $L=1$ m, poids $100$ N, articulée au mur, portant une charge de $300$ N à son extrémité. Un câble vertical tient l'extrémité. Tension $T$ (en N) ?",
          "(100*Rational(1,2)+300)", "350", r"Moments par rapport à l'articulation : $TL=P\frac L2+P_1L$, donc $T=50+300=350$ N.", src=F20 + ", ex. 2 (adapté)", duree=5),
        v("pm4", r"Même poutre : composante verticale de la réaction du mur (en N) ?", "100+300-350", "50", r"Équilibre vertical : $R_y+T=P+P_1$, donc $R_y=400-350=50$ N.", src=F20 + ", ex. 2 (adapté)", duree=3),
        o("pm5", r"Échelle homogène, poids $P$, longueur $L$, faisant un angle $\beta$ avec le sol. Contact sans frottement en $A$ (mur), avec frottement en $B$ (sol), $\vec R_B$ faisant l'angle $\varphi$ avec la normale. Écrire les conditions d'équilibre et trouver la condition de non-glissement.",
          r"Translation : sur $x$, $R_A-R_B\sin\varphi=0$ ; sur $y$, $R_B\cos\varphi=P$." "\n\n"
          r"Rotation autour de $B$ : $P\frac L2\cos\beta=R_AL\sin\beta$, donc $R_A=\dfrac P{2\tan\beta}$." "\n\n"
          r"Alors $\tan\varphi=\dfrac{R_A}P=\dfrac1{2\tan\beta}$. Pas de glissement si $\tan\varphi\le\mu$, soit $\mu\ge\dfrac1{2\tan\beta}$.", src=F20 + ", QCM 2 et 3", duree=10),
    ]},
    {"n": 13, "titre": "Repère de Frenet et gouttière", "notions": ["frenet", "newton"], "exos": [
        v("pg1", r"Gouttière : $V^2=2gr(1-\cos\theta)$ avec $r=1$ m, $g=10$, $\theta=60^\circ$. Valeur de $V^2$ (en m²/s²) ?", "2*10*1*(1-cos(pi/3))", "10", r"$2\times10\times\frac12=10$.", duree=2),
        v("pg2", r"Composante tangentielle de l'accélération $a_T=g\sin\theta$ pour $\theta=30^\circ$, $g=10$ (en m/s²) ?", "10*sin(pi/6)", "5", r"$a_T=10\times\frac12=5$.", duree=1),
        o("pg3", r"Solide qui glisse sans frottement depuis le sommet $A$ d'une gouttière en quart de cercle de rayon $r$ (par l'extérieur), repéré par l'angle $\theta$ avec la verticale. Établir $a_T$ et la réaction $R$ en fonction de $g$, $\theta$ et $V$.",
          r"Forces : poids $m\vec g$ et réaction $\vec R$ (normale). PFD dans Frenet." "\n\n"
          r"Tangente : $m\dot V=mg\sin\theta$, donc $a_T=g\sin\theta$." "\n\n"
          r"Normale (vers le centre) : $mg\cos\theta-R=m\dfrac{V^2}r$, donc $R=m\left(g\cos\theta-\dfrac{V^2}r\right)$.", src=F20 + ", ex. 3 (6 points)", duree=10),
        o("pg4", r"Avec $V^2=2gr(1-\cos\theta)$, exprimer $R$ en fonction de $m$, $g$, $\theta$, puis trouver l'angle où le solide quitte la gouttière.",
          r"$R=m\left(g\cos\theta-2g(1-\cos\theta)\right)=mg(3\cos\theta-2)$. Le solide quitte la gouttière quand $R=0$ : $\cos\theta=\frac23$, soit $\theta\approx48^\circ$.", src=F20 + ", ex. 3", duree=6),
    ]},
    {"n": 14, "titre": "Niveau examen : sujets complets", "notions": ["cinematique", "polaires", "cylindrique", "incline", "frenet", "projectile"], "examen": True, "exos": [
        o("px1", r"Cycloïde $x=A(\omega t-\sin\omega t)$, $y=A(1-\cos\omega t)$. 1. Composantes de $\vec v$ et $\vec a$. 2. Leurs normes. 3. Tracer la cycloïde pour $t=0,\frac T4,\frac T2,\frac{3T}4,T$.",
          r"Voir la correction de « Cycloïde » au niveau 3. Points à tracer, avec $\omega t=0,\frac\pi2,\pi,\frac{3\pi}2,2\pi$ : $(0,0)$, $A(\frac\pi2-1,\ A)$, $A(\pi,\ 2A)$, $A(\frac{3\pi}2+1,\ A)$, $A(2\pi,\ 0)$. Le point revient à $y=0$ toutes les périodes avec une vitesse nulle (point de rebroussement).", src="Contrôle 1 de physique, ex. 1", duree=12),
        o("px2", r"Mouvement hélicoïdal $x=R\cos\omega t$, $y=R\sin\omega t$, $z=H\omega t$. 1. $\vec v$ et $\|\vec v\|$. 2. $\vec a$ et $\|\vec a\|$. 3. $\overrightarrow{OM}$, $\vec v$, $\vec a$ en cylindriques.",
          r"1. $\vec v=(-R\omega\sin\omega t,\ R\omega\cos\omega t,\ H\omega)$, $\|\vec v\|=\omega\sqrt{R^2+H^2}$." "\n\n"
          r"2. $\vec a=(-R\omega^2\cos\omega t,\ -R\omega^2\sin\omega t,\ 0)$, $\|\vec a\|=R\omega^2$." "\n\n"
          r"3. $\overrightarrow{OM}=R\vec u_\rho+H\omega t\,\vec u_z$, $\vec v=R\omega\vec u_\theta+H\omega\vec u_z$, $\vec a=-R\omega^2\vec u_\rho$ : mêmes normes.", src="Contrôle 1 de physique, ex. 2", duree=12),
        o("px3", r"Objet $m_1=0{,}8$ kg sur un plan incliné de $30^\circ$ sans frottement, relié par un fil et une poulie légère à $m=1$ kg qui pend. 1. Forces sur chaque système. 2. Accélération (expression puis valeur). 3. Tension. 4. Réaction du plan.",
          r"$a=\dfrac{mg-m_1g\sin\alpha}{m+m_1}=\dfrac{10}3$ m/s² ; $T=m(g-a)=\dfrac{20}3$ N ; $R=m_1g\cos\alpha=4\sqrt3\approx6{,}9$ N. (Détail au niveau 10.)", src=F20 + ", ex. 1", duree=12),
        o("px4", r"Solide sur gouttière en quart de cercle (voir niveau 13) : composante tangentielle, réaction, angle de décollage.",
          r"$a_T=g\sin\theta$ ; $R=mg(3\cos\theta-2)$ ; décollage pour $\cos\theta=\frac23$. (Détail au niveau 13.)", src=F20 + ", ex. 3", duree=12),
        o("px5", r"Questions de cours : (a) $\vec u_\rho$, $\vec u_\theta$ en cartésiennes ; (b) $\frac{d\vec u_\rho}{d\theta}$ et $\frac{d\vec u_\theta}{d\theta}$ ; (c) $\vec v$ en polaires ; (d) $\vec a$ pour un mouvement circulaire puis circulaire uniforme.",
          r"(a) $\vec u_\rho=(\cos\theta,\sin\theta)$, $\vec u_\theta=(-\sin\theta,\cos\theta)$. (b) $\vec u_\theta$ et $-\vec u_\rho$. (c) $\vec v=\dot\rho\vec u_\rho+\rho\dot\theta\vec u_\theta$. (d) $\vec a=-R\dot\theta^2\vec u_\rho+R\ddot\theta\vec u_\theta$, puis $-R\omega^2\vec u_\rho$.", src=M21 + ", ex. 2 et 4", duree=10),
    ]},
    {"n": 15, "titre": "Examen + 20 %", "notions": ["polaires", "projectile", "frottement"], "examen": True, "exos": [
        v("py1", r"Spirale $\rho=\rho_0e^{\omega t}$, $\theta=\omega t$ avec $\rho_0=1$, $\omega=1$. Norme de l'accélération à $t=0$ ?",
          "sqrt(((diff(exp(t), t, 2)-exp(t)*1**2)**2 + (2*diff(exp(t), t)*1)**2).subs(t, 0))", "2",
          r"$a_\rho=\ddot\rho-\rho\dot\theta^2=\omega^2\rho-\omega^2\rho=0$ et $a_\theta=2\dot\rho\dot\theta=2\rho_0\omega^2e^{\omega t}$ : $\|\vec a\|=2$ en $t=0$.", duree=6),
        o("py2", r"Démontrer que la portée d'un tir à $v_0$ fixé est maximale pour $\alpha=45^\circ$.",
          r"Portée $=\dfrac{v_0^2\sin2\alpha}g$, maximale quand $\sin2\alpha=1$, soit $\alpha=45^\circ$ (pour $\alpha\in[0,\frac\pi2]$).", duree=4),
        o("py3", r"Un projectile est lancé de l'origine avec $v_0=20$ m/s. Quel angle $\alpha$ permet d'atteindre le point $(20\sqrt3,\ 0)$ au sol ? Y a-t-il une autre solution ?",
          r"Portée $\frac{v_0^2\sin2\alpha}g=40\sin2\alpha=20\sqrt3$ donne $\sin2\alpha=\frac{\sqrt3}2$, soit $2\alpha=60^\circ$ ou $120^\circ$ : $\alpha=30^\circ$ ou $\alpha=60^\circ$ (tirs complémentaires).", duree=6),
        o("py4", r"Chute avec frottement fluide : montrer que l'accélération s'annule quand $v=v_\ell$ et que $v(t)$ ne dépasse jamais $v_\ell$.",
          r"$m\dot v=mg-\alpha v$, donc $\dot v=0\iff v=\frac{mg}\alpha=v_\ell$. Comme $v(t)=v_\ell(1-e^{-t/\tau})$ avec $e^{-t/\tau}>0$, on a $v < v_\ell$ pour tout $t$ fini, et $v\to v_\ell$.", duree=6),
    ]},
]


def _v(enonce, calc, ans, sol):
    return {"enonce": enonce, "calc": calc, "ans": ans, "sol": sol}


# Numeric variants: a failed exercise comes back with other numbers; build.py checks calc == ans.
VARIANTS = {
    "pv1": [_v(r"$\vec u=(2,-1)$ et $\vec v=(4,3)$. Calculer $\vec u\cdot\vec v$.", "Matrix([2,-1]).dot(Matrix([4,3]))", "5", r"$8-3=5$.")],
    "pv3": [_v(r"Une force de norme $20$ N fait un angle de $30^\circ$ avec $Ox$. Composante $F_y$ (en N) ?", "20*sin(pi/6)", "10", r"$F_y=20\sin30^\circ=10$ N.")],
    "pd1": [_v(r"$x(t)=5+3t^2$. Calculer $\ddot x$.", "diff(5+3*t**2, t, 2)", "6", r"$\dot x=6t$, $\ddot x=6$.")],
    "pc1": [_v(r"$x(t)=2t^2+t$. Calculer la vitesse à $t=3$ s.", "diff(2*t**2+t, t).subs(t, 3)", "13", r"$v=4t+1=13$ m/s.")],
    "pr1": [_v(r"$x_0=0$, $v_0=2$ m/s, $a=4$ m/s². Position à $t=3$ s (en m) ?", "2*3+Rational(1,2)*4*3**2", "24", r"$6+18=24$ m.")],
    "pr2": [_v(r"Une voiture roule à $30$ m/s et freine avec $a=-5$ m/s². Distance d'arrêt (en m) ?", "30**2/(2*5)", "90", r"$\frac{900}{10}=90$ m.")],
    "pj1": [_v(r"Chute libre sans vitesse initiale d'une hauteur de $20$ m, $g=10$. Durée (en s) ?", "sqrt(2*20/10)", "2", r"$t=\sqrt{2h/g}=2$ s.")],
    "pj3": [_v(r"Projectile lancé à $v_0=40$ m/s avec $\alpha=30^\circ$, $g=10$. Hauteur maximale (en m) ?", "(40*sin(pi/6))**2/(2*10)", "20", r"$\frac{(40\cdot\frac12)^2}{20}=20$ m.")],
    "pp1": [_v(r"Point de coordonnées polaires $\rho=4$, $\theta=\dfrac\pi6$. Ordonnée $y$ ?", "4*sin(pi/6)", "2", r"$y=\rho\sin\theta=2$.")],
    "pq1": [_v(r"Mouvement circulaire uniforme, $R=0{,}5$ m, $\omega=4$ rad/s. Norme de l'accélération (en m/s²) ?", "Rational(1,2)*4**2", "8", r"$R\omega^2=8$.")],
    "pe1": [_v(r"Hélice avec $R=6$, $H=8$, $\omega=1$. Norme de la vitesse ?", "1*sqrt(6**2+8**2)", "10", r"$\omega\sqrt{R^2+H^2}=10$.")],
    "pn3": [_v(r"Un corps de $2$ kg subit une force résultante de $9$ N. Accélération (en m/s²) ?", "9/Rational(2)", "9/2", r"$a=F/m=4{,}5$.")],
    "pi1": [_v(r"Plan incliné de $45^\circ$ sans frottement, $g=10$. Accélération (en m/s²) ?", "10*sin(pi/4)", "5*sqrt(2)", r"$g\sin45^\circ=5\sqrt2$.")],
    "pf1": [_v(r"$m=3$ kg, $\alpha=6$ kg/s, $g=10$. Vitesse limite (en m/s) ?", "3*10/6", "5", r"$mg/\alpha=5$.")],
    "pm1": [_v(r"Force de $20$ N à $0{,}25$ m de l'axe, perpendiculaire au bras. Moment (en N·m) ?", "20*Rational(1,4)", "5", r"$Fd=5$.")],
    "pg1": [_v(r"$V^2=2gr(1-\cos\theta)$ avec $r=2$ m, $g=10$, $\theta=60^\circ$. Valeur (en m²/s²) ?", "2*10*2*(1-cos(pi/3))", "20", r"$40\times\frac12=20$.")],
}
for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["id"] in VARIANTS:
            _e["variants"] = VARIANTS[_e["id"]]


EXTRA_PARTS = []

QUIZ = [
    {"notion": "vecteurs", "type": "vf", "q": r"Le produit scalaire de deux vecteurs non nuls colinéaires de sens opposés est strictement négatif.", "bonne": True},
    {"notion": "vecteurs", "type": "qcm", "q": r"La norme de $\vec V_1\wedge\vec V_2$ vaut :",
     "choix": [r"$V_1V_2|\sin\alpha|$", r"$V_1V_2|\cos\alpha|$", r"$\sqrt{V_1^2+V_2^2+2V_1V_2\cos\alpha}$", r"$V_1+V_2$"], "bonne": 0},
    {"notion": "derivation", "type": "qcm", "q": r"La dérivée de $A\cos^2(\theta(t))$ par rapport à $t$ est :",
     "choix": [r"$-2A\dot\theta\cos\theta\sin\theta$", r"$2A\dot\theta\cos\theta\sin\theta$", r"$-2A\cos\theta\sin\theta$", r"$-A\dot\theta\sin^2\theta$"], "bonne": 0},
    {"notion": "cinematique", "type": "vf", "q": r"Un mouvement uniforme est forcément rectiligne.", "bonne": False},
    {"notion": "cinematique", "type": "qcm", "q": r"$x(t)=10-2t^2$ avec $t>0$. Le mouvement est :",
     "choix": [r"accéléré", r"décéléré", r"uniforme", r"circulaire"], "bonne": 0},
    {"notion": "cinematique", "type": "qcm", "q": r"L'accélération est :",
     "choix": [r"$\dfrac{d^2\overrightarrow{OM}}{dt^2}$", r"$\dfrac{d\overrightarrow{OM}}{dt}$", r"$\left(\dfrac{d\overrightarrow{OM}}{dt}\right)^2$", r"$\overrightarrow{OM}$"], "bonne": 0},
    {"notion": "rectiligne", "type": "qcm", "q": r"$72$ km/h valent :", "choix": [r"20 m/s", r"72 m/s", r"7,2 m/s", r"259 m/s"], "bonne": 0},
    {"notion": "projectile", "type": "vf", "q": r"En chute libre, l'accélération dépend de la masse de l'objet.", "bonne": False},
    {"notion": "projectile", "type": "qcm", "q": r"Au sommet de la trajectoire d'un projectile :",
     "choix": [r"$v_y=0$", r"$v_x=0$", r"$\vec v=\vec0$", r"$\vec a=\vec0$"], "bonne": 0},
    {"notion": "polaires", "type": "qcm", "q": r"En polaires, $\vec v$ vaut :",
     "choix": [r"$\dot\rho\,\vec u_\rho+\rho\dot\theta\,\vec u_\theta$", r"$\rho\,\vec u_\rho+\theta\,\vec u_\theta$", r"$\dot\rho\,\vec u_\rho$", r"$\rho\dot\theta\,\vec u_\rho$"], "bonne": 0},
    {"notion": "polaires", "type": "qcm", "q": r"$\dfrac{d\vec u_\rho}{dt}$ vaut :", "choix": [r"$\dot\theta\,\vec u_\theta$", r"$-\dot\theta\,\vec u_\theta$", r"$\dot\theta\,\vec u_\rho$", r"$\vec0$"], "bonne": 0},
    {"notion": "circulaire", "type": "vf", "q": r"Dans un mouvement circulaire uniforme, l'accélération est nulle.", "bonne": False},
    {"notion": "circulaire", "type": "qcm", "q": r"Circulaire uniforme de rayon $R$ : l'accélération vaut :",
     "choix": [r"$-R\omega^2\vec u_\rho$", r"$R\omega^2\vec u_\theta$", r"$R\omega\,\vec u_\theta$", r"$\vec0$"], "bonne": 0},
    {"notion": "cylindrique", "type": "qcm", "q": r"Pour une hélice de rayon $R$, de pas lié à $H$, la norme de la vitesse est :",
     "choix": [r"$\omega\sqrt{R^2+H^2}$", r"$R\omega$", r"$H\omega$", r"$\omega(R+H)$"], "bonne": 0},
    {"notion": "newton", "type": "vf", "q": r"Le principe d'inertie s'applique à une balle qui tombe en accélérant.", "bonne": False},
    {"notion": "newton", "type": "qcm", "q": r"Deuxième loi de Newton à masse constante :", "choix": [r"$\sum\vec F=m\vec a$", r"$\sum\vec F=m\vec v$", r"$\sum\vec F=\dfrac{m}{\vec a}$", r"$\sum\vec F=\vec p\,t$"], "bonne": 0},
    {"notion": "incline", "type": "qcm", "q": r"Accélération sans frottement le long d'un plan incliné d'angle $\alpha$ :", "choix": [r"$g\sin\alpha$", r"$g\cos\alpha$", r"$g\tan\alpha$", r"$g$"], "bonne": 0},
    {"notion": "incline", "type": "vf", "q": r"Avec une poulie idéale et un fil inextensible, la tension est la même des deux côtés.", "bonne": True},
    {"notion": "frottement", "type": "qcm", "q": r"La vitesse limite avec un frottement $-\alpha\vec v$ vaut :", "choix": [r"$\dfrac{mg}\alpha$", r"$\dfrac{\alpha}{mg}$", r"$mg\alpha$", r"$\dfrac{g}\alpha$"], "bonne": 0},
    {"notion": "moment", "type": "qcm", "q": r"Le moment d'une force par rapport à un axe est nul quand :", "choix": [r"la droite d'action de la force coupe l'axe", r"la force est grande", r"la force est perpendiculaire à l'axe", r"le bras de levier est maximal"], "bonne": 0},
    {"notion": "moment", "type": "vf", "q": r"Le poids d'une poutre homogène s'applique en son milieu.", "bonne": True},
    {"notion": "frenet", "type": "qcm", "q": r"Dans le repère de Frenet, l'accélération vaut :", "choix": [r"$\dot v\,\vec u_T+\dfrac{v^2}r\vec u_N$", r"$\dot v\,\vec u_N+\dfrac{v^2}r\vec u_T$", r"$\dfrac{v^2}r\vec u_T$", r"$\dot v\,\vec u_T$"], "bonne": 0},
]

_PS = r"$\vec u\cdot\vec v=xx'+yy'=\|\vec u\|\|\vec v\|\cos\alpha$"
_PV = r"$\|\vec u\wedge\vec v\|=\|\vec u\|\|\vec v\||\sin\alpha|$"
_DER = r"dérivée composée : $\frac d{dt}f(\theta)=\dot\theta f'(\theta)$"
_VA = r"$\vec v=\frac{d\overrightarrow{OM}}{dt}$ · $\vec a=\frac{d\vec v}{dt}$ · $\|\vec v\|=\sqrt{\dot x^2+\dot y^2}$"
_MRUA = r"$v=v_0+at$ · $x=x_0+v_0t+\frac12at^2$ · $v^2-v_0^2=2a\Delta x$"
_PROJ = r"$x=v_0\cos\alpha\,t$ · $y=v_0\sin\alpha\,t-\frac12gt^2$ · sommet : $v_y=0$"
_POL = r"$\vec u_\rho=(\cos\theta,\sin\theta)$ · $\vec u_\theta=(-\sin\theta,\cos\theta)$ · $x=\rho\cos\theta$, $y=\rho\sin\theta$"
_VPOL = r"$\vec v=\dot\rho\,\vec u_\rho+\rho\dot\theta\,\vec u_\theta$"
_APOL = r"$\vec a=(\ddot\rho-\rho\dot\theta^2)\vec u_\rho+(2\dot\rho\dot\theta+\rho\ddot\theta)\vec u_\theta$"
_CIRC = r"$\rho=R$ : $\vec a=-R\dot\theta^2\vec u_\rho+R\ddot\theta\,\vec u_\theta$ · uniforme : $a=R\omega^2$"
_HEL = r"hélice : $\|\vec v\|=\omega\sqrt{R^2+H^2}$ · $\|\vec a\|=R\omega^2$"
_PFD = r"PFD : $\sum\vec F=m\vec a$ · poids $\vec P=m\vec g$"
_INC = r"plan incliné : $a=g\sin\alpha$ · $R=mg\cos\alpha$"
_FROT = r"$m\dot v=mg-\alpha v$ · $v_\ell=\frac{mg}\alpha$ · $\tau=\frac m\alpha$"
_MOM = r"$M=Fd\sin\varphi$ · équilibre : $\sum\vec F=\vec0$, $\sum M=0$"
_FREN = r"$\vec a=\dot v\,\vec u_T+\frac{v^2}r\vec u_N$ · quitte le support : $R=0$"

FORMULES = {
    "pv1": _PS, "pv2": _PV + r" · $\vec u\wedge\vec v$ par déterminant", "pv3": r"$F_x=F\cos\alpha$, $F_y=F\sin\alpha$", "pv4": _PV, "pv5": _PS + r" · $\cos\pi=-1$",
    "pd1": _DER + r" · $(t^n)'=nt^{n-1}$", "pd2": r"$(e^{at})'=ae^{at}$", "pd3": _DER, "pd4": _DER + r" · $(\sin\omega t)'=\omega\cos\omega t$",
    "pd5": r"$\frac d{d\theta}\cos\theta=-\sin\theta$ · $\frac d{d\theta}\sin\theta=\cos\theta$ · " + _DER,
    "pc1": _VA, "pc2": _VA, "pc3": _VA + r" · $\cos\pi=-1$", "pc4": _VA + r" · $1-\cos\alpha=2\sin^2\frac\alpha2$",
    "pc5": _VA + r" · $\vec v\cdot\vec a>0$ : accéléré",
    "pr1": _MRUA, "pr2": _MRUA, "pr3": r"$1\ \mathrm{km/h}=\frac1{3{,}6}\ \mathrm{m/s}$ · $v=v_0+at$", "pr4": _MRUA,
    "pj1": r"$h=\frac12gt^2$ · $t=\sqrt{2h/g}$", "pj2": r"$v^2=2gh$", "pj3": r"$h=\frac{v_0^2\sin^2\alpha}{2g}$ · " + _PROJ, "pj4": r"$t=\frac{2v_0\sin\alpha}g$ · " + _PROJ,
    "pj5": r"portée $\frac{v_0^2\sin2\alpha}g$", "pj6": _PROJ + r" · éliminer $t$ · $\|\vec v\|=\sqrt{v_x^2+v_y^2}$",
    "pp1": _POL, "pp2": r"$\rho=\sqrt{x^2+y^2}$ · $\tan\theta=\frac yx$", "pp3": _POL, "pp4": _VPOL + r" · $\frac{d\vec u_\rho}{dt}=\dot\theta\vec u_\theta$", "pp5": _POL,
    "pp6": _APOL + r" · $\frac{d\vec u_\theta}{dt}=-\dot\theta\vec u_\rho$",
    "pq1": _CIRC, "pq2": r"$\omega=\frac{2\pi}T$ · $v=R\omega$", "pq3": _VPOL, "pq4": _CIRC + " · " + _APOL, "pq5": _CIRC,
    "pe1": _HEL, "pe2": _HEL, "pe3": r"$\vec v=\dot\rho\vec u_\rho+\rho\dot\theta\vec u_\theta+\dot z\vec u_z$ · " + _HEL,
    "pn1": r"$\vec P=m\vec g$", "pn2": r"$F=G\frac{m_1m_2}{d^2}$", "pn3": _PFD, "pn4": r"$\vec p=m\vec v$",
    "pn5": r"1er principe : forces qui se compensent $\Rightarrow$ $\vec v$ constant · " + _PFD, "pn6": _PFD + r" · $v=\int a\,dt$",
    "pi1": _INC, "pi2": _INC, "pi3": _INC + r" · même $a$ et même $T$ · " + _PFD, "pi4": _PFD, "pi5": _INC, "pi6": _PFD + r" · même $a$ et même $T$",
    "pf1": _FROT, "pf2": _FROT, "pf3": r"$v(t)=v_\ell(1-e^{-t/\tau})$", "pf4": _FROT + r" · EDO du 1er ordre : homogène + particulière",
    "pm1": _MOM, "pm2": _MOM, "pm3": _MOM + r" · poids d'une poutre homogène au milieu", "pm4": _MOM, "pm5": _MOM + r" · axe en $B$ : $M(\vec R_B)=0$ · $\tan\varphi\le\mu$",
    "pg1": _FREN, "pg2": _FREN, "pg3": _FREN + " · " + _PFD, "pg4": _FREN + r" · $V^2=2gr(1-\cos\theta)$",
    "px1": _VA + r" · $1-\cos\alpha=2\sin^2\frac\alpha2$", "px2": _HEL + r" · " + _VPOL, "px3": _INC + r" · même $a$ et même $T$ · " + _PFD, "px4": _FREN + " · " + _PFD,
    "px5": _POL + " · " + _VPOL + " · " + _CIRC,
    "py1": _APOL + r" · $\rho=\rho_0e^{\omega t}$", "py2": r"portée $\frac{v_0^2\sin2\alpha}g$ · $\sin2\alpha\le1$", "py3": r"portée $\frac{v_0^2\sin2\alpha}g$ · $\sin x=\sin(\pi-x)$",
    "py4": _FROT,
}
