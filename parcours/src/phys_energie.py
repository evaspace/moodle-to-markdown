"""Level path: S2 physics, work and energy (work, power, kinetic energy theorem, mechanical energy, spring, pulleys).

Calibrated on the S2 physics finals and midterms of `annales/raw/S2/{Finals,Midterms}/Phys` (text-layer ones read:
final 2026 « partiel de mai », midterm 2024/2026) whose first exercises are QCM, Newton with a pulley and
mechanical energy on a bowl. g = 10 m/s² as in the exams. `value` exercises are checked by sympy; `open` ones have a model answer.
"""

SUBJECT = {
    "id": "physique-s2-energie",
    "ordre": 305,
    "matiere": "physique",
    "semestre": "S2",
    "ecue": "Travail et énergie",
    "titre": "Travail et énergie",
    "chapitres_moodle": ["02_Cours"],
    "td": "TD de physique (Moodle Physique)",
    "examens": ["Partiel de physique (S2)"],
}

NOTIONS = [
    {"id": "travail", "titre": "Travail d'une force constante",
     "formule": r"$W_{A\to B}(\vec F)=\vec F\cdot\overrightarrow{AB}=F\,AB\cos\alpha$ · $\alpha=0$ : $W=F\,AB$ · $\alpha=90^\circ$ : $W=0$ · $\alpha=180^\circ$ : $W=-F\,AB$ · en joules (J)",
     "exemple": r"$F=20$ N à $60^\circ$ du déplacement de $4$ m : $W=20\times4\times\frac12=40$ J",
     "cours": r"Le travail est un produit scalaire : seule la composante de la force le long du déplacement travaille. Il est positif si la force aide le mouvement (moteur), négatif si elle s'y oppose (résistant), nul si elle est perpendiculaire (réaction normale)."},
    {"id": "poids", "titre": "Travail du poids et du frottement",
     "formule": r"poids : $W_{A\to B}(\vec P)=mg\,(z_A-z_B)$ (descente $>0$, montée $<0$), indépendant du chemin · plan incliné de longueur $L$ : $mgL\sin\alpha$ · réaction normale : $0$ · frottement constant $f$ : $W=-f\,L$, $f=\mu mg\cos\alpha$ (plan incliné)",
     "exemple": r"$m=2$ kg descend de $5$ m : $W_P=2\times10\times5=100$ J",
     "cours": r"Le poids est une force conservative : son travail ne dépend que des altitudes de départ et d'arrivée. Le frottement s'oppose toujours au déplacement : son travail est négatif et dépend du chemin parcouru."},
    {"id": "puissance", "titre": "Puissance",
     "formule": r"$P=\dfrac{W}{\Delta t}$ · $P=\vec F\cdot\vec v=Fv\cos\alpha$ · watt (W) $=$ J/s · $1\ \mathrm{kWh}=3{,}6\times10^6$ J",
     "exemple": r"$F=50$ N, $v=4$ m/s : $P=200$ W",
     "cours": r"La puissance est le travail fourni par seconde. Pour une force constante et une vitesse constante, $P=Fv$. Soulever une charge à vitesse constante demande $P=mgv$."},
    {"id": "cinetique", "titre": "Énergie cinétique et théorème",
     "formule": r"$E_c=\frac12mv^2$ · théorème de l'énergie cinétique : $\Delta E_c=E_c(B)-E_c(A)=\sum W_{A\to B}(\vec F_{ext})$",
     "exemple": r"$m=1000$ kg freine de $20$ m/s à $0$ avec $4000$ N : $d=\dfrac{\frac12mv^2}{F}=50$ m",
     "cours": r"Le théorème donne la vitesse sans connaître le temps : on additionne les travaux de toutes les forces (poids, réaction, frottement, moteur) et on égale à la variation de $E_c$. Il faut un référentiel galiléen."},
    {"id": "potentielle", "titre": "Énergie potentielle et énergie mécanique",
     "formule": r"$E_p=mgz$ (axe $z$ vers le haut, origine au choix) · $E_m=E_c+E_p$ · $\Delta E_p=-W(\vec P)$ · au repos : $E_m=E_p$",
     "exemple": r"$m=2$ kg à $3$ m, $v=6$ m/s : $E_c=36$ J, $E_p=60$ J, $E_m=96$ J",
     "cours": r"L'énergie potentielle dépend du choix de l'origine des altitudes, mais ses variations n'en dépendent pas. Toujours préciser l'origine avant de calculer."},
    {"id": "conservation", "titre": "Conservation de l'énergie mécanique",
     "formule": r"seules forces conservatives (ou forces qui ne travaillent pas) : $E_m(A)=E_m(B)$ · $\frac12mv_B^2+mgz_B=\frac12mv_A^2+mgz_A$ · lâché sans vitesse : $v=\sqrt{2g\,\Delta h}$",
     "exemple": r"bille lâchée sans vitesse de $h=1{,}8$ m, vitesse à $d=0{,}8$ m : $v=\sqrt{2\times10\times1}=2\sqrt5$ m/s",
     "cours": r"La masse disparaît du résultat : tous les objets lâchés de la même hauteur arrivent à la même vitesse. L'énergie mécanique n'est pas toujours conservée : elle l'est seulement si les forces non conservatives (frottements, moteur) ne travaillent pas."},
    {"id": "nonconservatif", "titre": "Forces non conservatives",
     "formule": r"$\Delta E_m=E_m(B)-E_m(A)=\sum W(\vec F_{nc})$ · frottement : $\Delta E_m=-f\,L<0$ · l'énergie perdue passe en chaleur",
     "exemple": r"balle lâchée de $2$ m remontant à $1{,}5$ m, $m=0{,}5$ kg : perte $=mg\Delta h=2{,}5$ J",
     "cours": r"Si un frottement agit, l'énergie mécanique diminue exactement du travail (négatif) de la force de frottement. On peut aussi appliquer directement le théorème de l'énergie cinétique avec tous les travaux."},
    {"id": "ressort", "titre": "Ressort et énergie élastique",
     "formule": r"force de rappel $\vec F=-k\,x\,\vec u_x$ · $E_{p,el}=\frac12kx^2$ ($x$ : allongement) · conservation : $\frac12mv^2+\frac12kx^2=$ constante · équilibre vertical : $kx_{eq}=mg$",
     "exemple": r"$k=200$ N/m comprimé de $0{,}1$ m : $E_{p,el}=1$ J, il lance $m=0{,}5$ kg à $v=x\sqrt{k/m}=2$ m/s",
     "cours": r"L'énergie élastique est toujours positive (compression ou étirement). Un ressort lance une masse à la vitesse maximale quand il repasse par sa longueur à vide, car toute l'énergie élastique est devenue cinétique."},
    {"id": "newtonpoulie", "titre": "Lois de Newton et poulie",
     "formule": r"$\sum\vec F=m\vec a$ · fil inextensible : même $a$ en norme · poulie idéale et fil sans masse : même tension $T$ · $M$ et $M+m$ reliées : $a=\dfrac{mg}{2M+m}$",
     "exemple": r"$M=2$ kg, $m=0{,}5$ kg : $a=\dfrac{5}{4{,}5}=\dfrac{10}9$ m/s²",
     "cours": r"Écrire le PFD sur chaque masse (axe orienté dans le sens du mouvement), garder la même tension, puis additionner pour éliminer $T$. La durée de chute s'obtient avec $h=\frac12at^2$."},
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


P26 = "Partiel de physique S2 (mai)"

LEVELS = [
    {"n": 1, "titre": "Travail d'une force constante", "notions": ["travail"], "exos": [
        v("ew1", r"Une force de $10$ N, dans le sens du déplacement, déplace un objet de $5$ m. Travail (en J) ?", "10*5", "50", r"$W=F\,AB\cos0=50$ J.", duree=1),
        v("ew2", r"Une force de $20$ N fait un angle de $60^\circ$ avec le déplacement de $4$ m. Travail (en J) ?", "20*4*cos(pi/3)", "40", r"$W=20\times4\times\cos60^\circ=40$ J.", duree=2),
        v("ew3", r"Une force de $10$ N perpendiculaire à un déplacement de $3$ m. Travail (en J) ?", "10*3*cos(pi/2)", "0", r"$\cos90^\circ=0$ : la force ne travaille pas.", duree=1),
        v("ew4", r"$\vec F=(3,4)$ N et $\overrightarrow{AB}=(2,-1)$ m. Calculer $W_{A\to B}(\vec F)$ (en J).", "Matrix([3,4]).dot(Matrix([2,-1]))", "2", r"$W=\vec F\cdot\overrightarrow{AB}=3\times2+4\times(-1)=2$ J.", duree=2),
        v("ew5", r"Une force de $15$ N s'oppose à un déplacement de $2$ m. Travail (en J) ?", "15*2*cos(pi)", "-30", r"Angle de $180^\circ$ : $W=-F\,AB=-30$ J (travail résistant).", duree=1),
        o("ew6", r"Une caisse de masse $m$ est traînée à vitesse constante sur le sol par une force $\vec F$ faisant l'angle $\alpha$ avec l'horizontale, sur une distance $AB$. Donner $W(\vec F)$. Quel est le travail du poids ? de la réaction normale ? Que vaut le travail du frottement ?",
          r"$W(\vec F)=F\cdot AB\cdot\cos\alpha$ (réponse c du QCM : le produit scalaire, pas $F\cdot AB$ ni un sinus)." "\n\n"
          r"Poids et réaction normale sont perpendiculaires au déplacement : travail nul." "\n\n"
          r"Vitesse constante : $\Delta E_c=0$, donc la somme des travaux est nulle et $W(\vec f)=-F\cdot AB\cos\alpha$.", src=P26 + ", QCM 1", duree=6),
    ]},
    {"n": 2, "titre": "Travail du poids et du frottement", "notions": ["poids", "travail"], "exos": [
        v("ep1", r"Un objet de $2$ kg tombe de $5$ m, $g=10$ m/s². Travail du poids (en J) ?", "2*10*5", "100", r"$W_P=mg(z_A-z_B)=100$ J.", duree=1),
        v("ep2", r"Un objet de $3$ kg est monté de $4$ m. Travail du poids (en J) ?", "-3*10*4", "-120", r"Montée : $W_P=-mgh=-120$ J.", duree=1),
        v("ep3", r"Un solide de $2$ kg glisse sur $10$ m le long d'un plan incliné de $30^\circ$. Travail du poids (en J) ?", "2*10*10*sin(pi/6)", "100", r"$W_P=mgL\sin\alpha=2\times10\times10\times\frac12=100$ J.", duree=2),
        v("ep4", r"Même solide : travail de la réaction normale du plan (en J) ?", "2*10*cos(pi/6)*10*cos(pi/2)", "0", r"$\vec R\perp\overrightarrow{AB}$ : $W=0$.", duree=1),
        v("ep5", r"Un bloc de $5$ kg est traîné sur $6$ m sur un sol horizontal avec $\mu=0{,}2$. Travail du frottement (en J) ?", "-Rational(1,5)*5*10*6", "-60", r"$f=\mu mg=10$ N, $W_f=-fL=-60$ J.", duree=2),
        o("ep6", r"Montrer que le travail du poids entre $A$ et $B$ ne dépend que des altitudes $z_A$ et $z_B$.",
          r"Avec $z$ vers le haut, $\vec P=(0,0,-mg)$ et $\overrightarrow{AB}=(x_B-x_A,\ y_B-y_A,\ z_B-z_A)$ (pour un petit déplacement, puis en sommant)." "\n\n"
          r"$W=\vec P\cdot\overrightarrow{AB}=-mg\,(z_B-z_A)=mg\,(z_A-z_B)$ : aucune trace du chemin ni des coordonnées horizontales.", duree=5),
        o("ep7", r"Un solide de masse $m$ glisse sur une longueur $L$ le long d'un plan incliné d'angle $\alpha$, avec le coefficient de frottement $\mu$. Exprimer le travail du frottement.",
          r"Normale au plan : $R=mg\cos\alpha$, donc $f=\mu R=\mu mg\cos\alpha$." "\n\n"
          r"Le frottement s'oppose au mouvement : $W_f=-\mu mg\,L\cos\alpha$.", duree=5),
    ]},
    {"n": 3, "titre": "Puissance", "notions": ["puissance", "travail"], "exos": [
        v("eu1", r"Une force fournit $600$ J en $20$ s. Puissance (en W) ?", "600/20", "30", r"$P=W/\Delta t=30$ W.", duree=1),
        v("eu2", r"Une force de $50$ N sur un objet à $4$ m/s, dans le sens de la vitesse. Puissance (en W) ?", "50*4", "200", r"$P=Fv=200$ W.", duree=1),
        v("eu3", r"Un moteur soulève une charge de $100$ kg à vitesse constante de $0{,}5$ m/s, $g=10$. Puissance (en W) ?", "100*10*Rational(1,2)", "500", r"$P=mgv=500$ W.", duree=2),
        v("eu4", r"Une voiture de puissance $40$ kW roule à $20$ m/s. Force motrice (en N) ?", "40000/20", "2000", r"$F=P/v=2000$ N.", duree=2),
        v("eu5", r"Combien de joules dans $1$ kWh ?", "1000*3600", "3600000", r"$1\ \mathrm{kWh}=1000\ \mathrm{W}\times3600\ \mathrm{s}=3{,}6\times10^6$ J.", duree=1),
    ]},
    {"n": 4, "titre": "Énergie cinétique et théorème", "notions": ["cinetique", "travail"], "exos": [
        v("ec1", r"Énergie cinétique d'un objet de $2$ kg à $3$ m/s (en J) ?", "Rational(1,2)*2*3**2", "9", r"$\frac12mv^2=9$ J.", duree=1),
        v("ec2", r"Voiture de $1000$ kg à $72$ km/h. Énergie cinétique (en J) ?", "Rational(1,2)*1000*20**2", "200000", r"$72$ km/h $=20$ m/s : $\frac12\times1000\times400=2\times10^5$ J.", duree=2),
        v("ec3", r"Un corps de $4$ kg part du repos et reçoit un travail total de $50$ J. Vitesse finale (en m/s) ?", "sqrt(2*50/4)", "5", r"$\frac12mv^2=50$ : $v=\sqrt{25}=5$ m/s.", duree=2),
        v("ec4", r"Voiture de $1000$ kg à $20$ m/s, freinage constant de $4000$ N jusqu'à l'arrêt. Distance (en m) ?", "Rational(1,2)*1000*20**2/4000", "50", r"$0-\frac12mv^2=-Fd$ : $d=\frac{200000}{4000}=50$ m.", duree=3),
        v("ec5", r"Chute libre sans vitesse initiale de $20$ m. Vitesse à l'arrivée (en m/s) ?", "sqrt(2*10*20)", "20", r"$\frac12mv^2=mgh$ : $v=\sqrt{2gh}=20$ m/s.", duree=2),
        v("ec6", r"Un objet est lancé vers le haut à $20$ m/s. Hauteur maximale par le théorème de l'énergie cinétique (en m) ?", "20**2/(2*10)", "20", r"$0-\frac12mv_0^2=-mgh$ : $h=\frac{v_0^2}{2g}=20$ m.", duree=3),
        o("ec7", r"Démontrer le théorème de l'énergie cinétique pour un point matériel soumis à une force résultante $F$ constante, en mouvement rectiligne.",
          r"PFD : $F=ma$ avec $a$ constante. Alors $v_B^2-v_A^2=2a\,AB$ (mouvement rectiligne uniformément varié)." "\n\n"
          r"Multiplier par $\frac m2$ : $\frac12mv_B^2-\frac12mv_A^2=ma\,AB=F\,AB=W_{A\to B}(\vec F)$.", duree=5),
    ]},
    {"n": 5, "titre": "Énergie potentielle et énergie mécanique", "notions": ["potentielle", "cinetique"], "exos": [
        v("eq1", r"Énergie potentielle d'un objet de $2$ kg à $3$ m (origine au sol, $g=10$) en J ?", "2*10*3", "60", r"$E_p=mgz=60$ J.", duree=1),
        v("eq2", r"Un objet de $1$ kg lâché sans vitesse de $10$ m. Énergie mécanique (origine au sol) en J ?", "1*10*10", "100", r"Au repos $E_m=E_p=mgh=100$ J.", duree=1),
        v("eq3", r"Objet de $2$ kg à $4$ m avec $v=6$ m/s. Énergie mécanique (en J) ?", "Rational(1,2)*2*6**2+2*10*4", "116", r"$E_c=36$, $E_p=80$ : $E_m=116$ J.", duree=2),
        v("eq4", r"Un objet de $2$ kg monte de $5$ m. Variation d'énergie potentielle (en J) ?", "2*10*5", "100", r"$\Delta E_p=mg\Delta z=100$ J ($=-W_P$).", duree=1),
        o("eq5", r"Un objet de masse $m$ est lâché sans vitesse initiale en $A$ (hauteur $h$) d'une cuvette, glisse sans frottement jusqu'au point le plus bas $A'$ (au sol) puis remonte en $B$ à la hauteur $d < h$. Donner $E_c$, $E_p$ et $E_m$ en $A$, $A'$ et $B$ (origine au sol).",
          r"En $A$ : $E_c=0$, $E_p=mgh$, $E_m=mgh$." "\n\n"
          r"En $A'$ : $E_p=0$ ; l'énergie mécanique se conserve (réaction normale sans travail, pas de frottement), donc $E_m=mgh$ et $E_c=mgh$." "\n\n"
          r"En $B$ : $E_p=mgd$, $E_m=mgh$ et $E_c=mg(h-d)$.", src=P26 + ", ex. 3 q. 1", duree=8),
        o("eq6", r"Qu'est-ce qu'on ne peut pas dire de l'énergie mécanique d'un système : (a) c'est $E_c+E_p$ ; (b) elle est nulle pour un mouvement rectiligne ; (c) elle est toujours conservée ; (d) elle vaut $E_p$ au repos ?",
          r"(c) est faux : l'énergie mécanique n'est conservée que si les forces non conservatives (frottements, moteur) ne travaillent pas." "\n\n"
          r"(b) est faux aussi : un mouvement rectiligne a une énergie cinétique non nulle. Les deux réponses (b) et (c) sont donc des affirmations qu'on ne peut pas faire.", src=P26 + ", QCM 5", duree=4),
    ]},
    {"n": 6, "titre": "Conservation de l'énergie mécanique", "notions": ["conservation", "potentielle"], "exos": [
        v("ek1", r"Objet lâché sans vitesse de $5$ m. Vitesse au sol par conservation de l'énergie (en m/s) ?", "sqrt(2*10*5)", "10", r"$mgh=\frac12mv^2$ : $v=10$ m/s.", duree=2),
        v("ek2", r"Bille lâchée sans vitesse en $A$ à $h=1{,}8$ m. Vitesse en $B$ à $d=0{,}8$ m, sans frottement (en m/s) ?", "sqrt(2*10*(Rational(18,10)-Rational(8,10)))", "2*sqrt(5)", r"$v=\sqrt{2g(h-d)}=\sqrt{20}=2\sqrt5$ m/s.", src=P26 + ", ex. 3 q. 2 (adapté)", duree=3),
        v("ek3", r"Pendule de longueur $1$ m lâché sans vitesse de l'horizontale. Vitesse au point le plus bas (en m/s) ?", "sqrt(2*10*1)", "2*sqrt(5)", r"Descente de $l=1$ m : $v=\sqrt{2gl}=2\sqrt5$ m/s.", duree=3),
        v("ek4", r"Montagnes russes : $v=2$ m/s au sommet à $10$ m. Vitesse au point à $3$ m (en m/s) ?", "sqrt(2**2+2*10*(10-3))", "12", r"$v^2=v_0^2+2g\Delta h=4+140=144$ : $v=12$ m/s.", duree=3),
        v("ek5", r"Un objet lancé verticalement à $10$ m/s. Hauteur maximale par conservation de $E_m$ (en m) ?", "10**2/(2*10)", "5", r"$\frac12mv_0^2=mgh$ : $h=5$ m.", duree=2),
        v("ek6", r"Un solide glisse sans frottement sur une pente de $10$ m de long à $30^\circ$, sans vitesse initiale. Vitesse en bas (en m/s) ?", "sqrt(2*10*10*sin(pi/6))", "10", r"Dénivelé $h=L\sin\alpha=5$ m : $v=\sqrt{2gh}=10$ m/s.", duree=3),
        o("ek7", r"Montrer que la vitesse d'arrivée d'une bille qui glisse sans frottement dans une cuvette de profondeur $h$ ne dépend ni de sa masse, ni de la forme de la cuvette.",
          r"Réaction normale perpendiculaire au déplacement : pas de travail. Seul le poids travaille, donc $E_m$ se conserve : $mgh=\frac12mv^2$." "\n\n"
          r"$v=\sqrt{2gh}$ : $m$ se simplifie et seule la différence d'altitude intervient.", duree=5),
    ]},
    {"n": 7, "titre": "Forces non conservatives", "notions": ["nonconservatif", "poids", "cinetique"], "exos": [
        v("en1", r"Un solide de $2$ kg descend sur $10$ m d'un plan à $30^\circ$ depuis le repos, avec un frottement de $4$ N. Énergie cinétique en bas (en J) ?", "2*10*10*sin(pi/6)-4*10", "60", r"$E_c=W_P+W_f=100-40=60$ J.", duree=3),
        v("en2", r"Même solide : vitesse en bas (en m/s) ?", "sqrt(2*60/2)", "2*sqrt(15)", r"$\frac12\cdot2\cdot v^2=60$ : $v=\sqrt{60}=2\sqrt{15}$ m/s.", duree=2),
        v("en3", r"Une balle de $0{,}5$ kg lâchée de $2$ m rebondit à $1{,}5$ m. Énergie mécanique perdue (en J) ?", "Rational(1,2)*10*(2-Rational(3,2))", "5/2", r"$\Delta E_m=mg(h'-h)=-2{,}5$ J : perte de $2{,}5$ J.", duree=2),
        v("en4", r"Un objet de $1$ kg lancé à $10$ m/s vers le haut atteint seulement $4$ m à cause de l'air. Travail de l'air (en J) ?", "10*4-Rational(1,2)*10**2", "-10", r"$W_{air}=\Delta E_m=mgh-\frac12mv_0^2=40-50=-10$ J.", duree=3),
        v("en5", r"Un palet à $10$ m/s glisse sur du sol horizontal avec $\mu=0{,}5$. Distance d'arrêt (en m) ?", "10**2/(2*Rational(1,2)*10)", "10", r"$\frac12mv_0^2=\mu mg\,d$ : $d=\frac{v_0^2}{2\mu g}=10$ m.", duree=3),
        o("en6", r"Une bille lâchée sans vitesse en $A$ (hauteur $h$) d'une cuvette rugueuse s'arrête à la hauteur $d < h$ la première fois qu'elle remonte. Où est passée l'énergie ? Donner l'expression du travail du frottement.",
          r"L'énergie mécanique diminue : $E_m(B)-E_m(A)=mgd-mgh=W(\vec f)$." "\n\n"
          r"Donc $W(\vec f)=-mg(h-d)<0$. L'énergie perdue est devenue de la chaleur (échauffement de la bille et de la cuvette).", duree=5),
    ]},
    {"n": 8, "titre": "Ressort et énergie élastique", "notions": ["ressort", "conservation"], "exos": [
        v("er1", r"Ressort $k=200$ N/m comprimé de $0{,}1$ m. Énergie élastique (en J) ?", "Rational(1,2)*200*Rational(1,10)**2", "1", r"$\frac12kx^2=\frac12\times200\times0{,}01=1$ J.", duree=1),
        v("er2", r"Même ressort comprimé de $0{,}05$ m. Force de rappel (en N) ?", "200*Rational(1,20)", "10", r"$F=kx=10$ N.", duree=1),
        v("er3", r"Ce ressort ($k=200$, $x=0{,}1$ m) lance une masse de $0{,}5$ kg sans frottement. Vitesse de lancement (en m/s) ?", "sqrt(200/Rational(1,2))*Rational(1,10)", "2", r"$\frac12kx^2=\frac12mv^2$ : $v=x\sqrt{k/m}=0{,}1\times20=2$ m/s.", duree=3),
        v("er4", r"Une masse de $1$ kg à $2$ m/s heurte un ressort $k=100$ N/m (sans frottement). Compression maximale (en m) ?", "2*sqrt(Rational(1,100))", "1/5", r"$\frac12mv^2=\frac12kx^2$ : $x=v\sqrt{m/k}=2\times0{,}1=0{,}2$ m.", duree=3),
        v("er5", r"Une masse de $1$ kg est suspendue à un ressort $k=100$ N/m. Allongement à l'équilibre (en m) ?", "1*10/100", "1/10", r"$kx=mg$ : $x=0{,}1$ m.", duree=2),
        o("er6", r"Une masse $m$ liée à un ressort de raideur $k$, sur un plan horizontal sans frottement, est écartée de $x_0$ puis lâchée. Exprimer sa vitesse en fonction de $x$ et sa vitesse maximale.",
          r"Conservation de l'énergie mécanique : $\frac12mv^2+\frac12kx^2=\frac12kx_0^2$." "\n\n"
          r"$v=\sqrt{\dfrac k m\,(x_0^2-x^2)}$. Elle est maximale en $x=0$ : $v_{max}=x_0\sqrt{k/m}$.", duree=6),
    ]},
    {"n": 9, "titre": "Lois de Newton et poulie", "notions": ["newtonpoulie"], "exos": [
        v("eo1", r"Poulie bloquée libérée : deux masses $M=2$ kg et, du côté droit, $m=0{,}5$ kg de plus. Accélération (en m/s²) ?", "Rational(1,2)*10/(2*2+Rational(1,2))", "10/9", r"$a=\dfrac{mg}{2M+m}=\dfrac{5}{4{,}5}=\dfrac{10}9$ m/s².", src=P26 + ", ex. 2 q. 3", duree=3),
        v("eo2", r"Même système : tension du fil (en N) ?", "2*(10+Rational(10,9))", "200/9", r"Masse de gauche : $T-Mg=Ma$, donc $T=M(g+a)=2\times\frac{100}9=\frac{200}9$ N.", duree=3),
        v("eo3", r"Le côté droit est à $1{,}0$ m du sol. Durée de la chute (en s) ?", "sqrt(2*1/Rational(10,9))", "3*sqrt(5)/5", r"$h=\frac12at^2$ : $t=\sqrt{\frac{2h}a}=\sqrt{1{,}8}=\frac{3\sqrt5}5\approx1{,}34$ s.", duree=3),
        v("eo4", r"Même système : vitesse en arrivant au sol (en m/s) ?", "sqrt(2*Rational(10,9)*1)", "2*sqrt(5)/3", r"$v=\sqrt{2ah}=\sqrt{\frac{20}9}=\frac{2\sqrt5}3\approx1{,}49$ m/s.", duree=3),
        o("eo5", r"Deux masses égales $M$ sont attachées aux extrémités d'une corde passant sur une poulie bloquée ; une masse $m$ est posée sur celle de droite. Corde et poulie sans masse, sans frottement. Quelle relation entre les tensions ? Établir $a=\dfrac{mg}{2M+m}$.",
          r"Fil sans masse sur poulie sans frottement : la tension est la même des deux côtés, $T_1=T_2=T$. Fil inextensible : les accélérations ont la même norme $a$." "\n\n"
          r"Masse de gauche (monte) : $T-Mg=Ma$. Ensemble de droite (descend) : $(M+m)g-T=(M+m)a$." "\n\n"
          r"On additionne : $mg=(2M+m)a$, soit $a=\dfrac{mg}{2M+m}$.", src=P26 + ", ex. 2", duree=10),
    ]},
    {"n": 10, "titre": "Niveau examen : sujets complets", "notions": ["travail", "cinetique", "conservation", "nonconservatif", "newtonpoulie"], "examen": True, "exos": [
        o("ex1", r"QCM. (1) Travail d'une force $F$ d'angle $\alpha$ sur une boîte déplacée de $AB$ ? (2) Un bus démarre brusquement et les passagers sont repoussés en arrière : quelle loi ? (3) $\vec F=6\vec u_x-8\vec u_y+10\vec u_z$ donne une accélération de norme $1$ m/s² : masse ? (4) Le théorème de l'énergie cinétique ? (5) Que ne peut-on pas dire de l'énergie mécanique ?",
          r"(1) $W=\vec F\cdot\overrightarrow{AB}=F\,AB\cos\alpha$." "\n\n"
          r"(2) Première loi de Newton (inertie)." "\n\n"
          r"(3) $\|\vec F\|=\sqrt{36+64+100}=10\sqrt2$ N, $m=\|\vec F\|/a=10\sqrt2$ kg." "\n\n"
          r"(4) La somme des travaux des forces extérieures est égale à la variation de l'énergie cinétique." "\n\n"
          r"(5) Elle n'est pas toujours conservée.", src=P26 + ", QCM 1 à 5", duree=12),
        o("ex2", r"Deux masses $M=2{,}0$ kg sont attachées à une corde sur une poulie bloquée. La masse de gauche repose sur le sol, celle de droite est à $1{,}0$ m du sol et porte une masse $m=0{,}5$ kg. $g=10$ m/s². 1. Forces sur chaque masse. 2. Relation entre les tensions. 3. Accélération, application numérique. 4. Vitesse de l'ensemble de droite à l'arrivée au sol.",
          r"3. $a=\dfrac{mg}{2M+m}=\dfrac{10}9\approx1{,}1$ m/s²." "\n\n"
          r"4. $v=\sqrt{2ah}=\dfrac{2\sqrt5}3\approx1{,}5$ m/s (ou énergie : $(M+m)gh-Mgh=\frac12(2M+m)v^2$ donne $mgh=\frac12(2M+m)v^2$, même résultat)." "\n\n"
          r"Détail des forces et des tensions au niveau 9.", src=P26 + ", ex. 2 (8 points)", duree=15),
        o("ex3", r"Objet de masse $m$ lâché sans vitesse du haut d'une cuvette (point $A$, hauteur $h$) qui glisse et remonte à un deuxième sommet $B$ (hauteur $d$), sans frottement, $g=10$. 1. $E_c$, $E_p$, $E_m$ en $A$, $A'$ (bas) et $B$. 2. Vitesse en $B$. 3. Pour $h=1{,}8$ m et $d=0{,}8$ m, calculer la vitesse en $B$.",
          r"1. $A$ : $(0,\ mgh,\ mgh)$ ; $A'$ : $(mgh,\ 0,\ mgh)$ ; $B$ : $(mg(h-d),\ mgd,\ mgh)$." "\n\n"
          r"2. $\frac12mv_B^2=mg(h-d)$ donne $v_B=\sqrt{2g(h-d)}$." "\n\n"
          r"3. $v_B=\sqrt{20\times1}=2\sqrt5\approx4{,}5$ m/s.", src=P26 + ", ex. 3 (4,5 points)", duree=12),
        o("ex4", r"Un skieur de $80$ kg part du repos en haut d'une piste de $200$ m de long inclinée de $30^\circ$. Frottement constant de $100$ N. 1. Travail du poids. 2. Travail du frottement. 3. Vitesse en bas par le théorème de l'énergie cinétique. 4. Puissance moyenne du poids sur la descente si elle dure $20$ s.",
          r"1. $W_P=mgL\sin\alpha=80\times10\times200\times\frac12=80\,000$ J." "\n\n"
          r"2. $W_f=-fL=-20\,000$ J." "\n\n"
          r"3. $\frac12mv^2=60\,000$ donne $v^2=1500$, $v\approx38{,}7$ m/s (environ $139$ km/h)." "\n\n"
          r"4. $P=W_P/\Delta t=80\,000/20=4000$ W.", duree=12),
    ]},
    {"n": 11, "titre": "Examen + 20 %", "notions": ["ressort", "nonconservatif", "newtonpoulie", "puissance"], "examen": True, "exos": [
        v("ey1", r"Un bloc de $2$ kg à $4$ m/s glisse sur $0{,}6$ m de sol rugueux ($\mu=0{,}5$) puis percute un ressort $k=20$ N/m. Compression maximale (en m) ?",
          "sqrt((Rational(1,2)*2*4**2-Rational(1,2)*2*10*Rational(3,5))*2/20)", "1",
          r"Après le glissement : $\frac12mv^2-\mu mg\,d=16-6=10$ J. Ensuite $\frac12kx^2=10$ donne $x=\sqrt{2\times10/20}=1$ m.", duree=6),
        v("ey2", r"Sur un plan incliné de $30^\circ$, un solide de $1$ kg glisse sur $4$ m depuis le repos avec $\mu=0$. Puissance moyenne du poids si la descente dure $2$ s (en W) ?", "1*10*4*sin(pi/6)/2", "10", r"$W_P=mgL\sin\alpha=20$ J, $P=20/2=10$ W.", duree=4),
        v("ey3", r"Poulie : $M=3$ kg des deux côtés, $m=1$ kg en plus à droite. Accélération (en m/s²) ?", "1*10/(2*3+1)", "10/7", r"$a=\dfrac{mg}{2M+m}=\dfrac{10}7$ m/s².", duree=3),
        o("ey4", r"Un wagonnet de masse $m$ est lancé à la vitesse $v_0$ au bas d'une pente de hauteur $h$ avec frottement. Il s'arrête juste en haut. Exprimer le travail des frottements puis la vitesse minimale pour atteindre le haut sans frottement.",
          r"Théorème de l'énergie cinétique : $0-\frac12mv_0^2=-mgh+W_f$, donc $W_f=mgh-\frac12mv_0^2$ (négatif)." "\n\n"
          r"Sans frottement : $v_0=\sqrt{2gh}$ suffit juste. Avec frottement il faut plus : $\frac12mv_0^2=mgh+|W_f|$.", duree=8),
        o("ey5", r"Une masse $m$ est lâchée sans vitesse du haut d'une demi-sphère lisse de rayon $R$. Elle quitte la surface quand la réaction s'annule. Trouver l'angle $\theta$ (avec la verticale) du décollage.",
          r"Énergie : $v^2=2gR(1-\cos\theta)$. Normale : $mg\cos\theta-R_N=\dfrac{mv^2}R$, avec $R_N=0$ au décollage." "\n\n"
          r"$g\cos\theta=2g(1-\cos\theta)$ donne $\cos\theta=\frac23$, soit $\theta\approx48^\circ$.", duree=10),
    ]},
]


def _v(enonce, calc, ans, sol):
    return {"enonce": enonce, "calc": calc, "ans": ans, "sol": sol}


# Numeric variants: a failed exercise comes back with other numbers; build.py checks calc == ans.
VARIANTS = {
    "ew1": [_v(r"Une force de $8$ N, dans le sens du déplacement, déplace un objet de $6$ m. Travail (en J) ?", "8*6", "48", r"$W=48$ J.")],
    "ew2": [_v(r"Une force de $10$ N fait un angle de $60^\circ$ avec le déplacement de $8$ m. Travail (en J) ?", "10*8*cos(pi/3)", "40", r"$10\times8\times\frac12=40$ J.")],
    "ew4": [_v(r"$\vec F=(1,5)$ N et $\overrightarrow{AB}=(4,2)$ m. Travail (en J) ?", "Matrix([1,5]).dot(Matrix([4,2]))", "14", r"$4+10=14$ J.")],
    "ep1": [_v(r"Un objet de $4$ kg tombe de $3$ m. Travail du poids (en J) ?", "4*10*3", "120", r"$mgh=120$ J.")],
    "ep3": [_v(r"Un solide de $1$ kg glisse sur $8$ m le long d'un plan à $30^\circ$. Travail du poids (en J) ?", "1*10*8*sin(pi/6)", "40", r"$mgL\sin\alpha=40$ J.")],
    "ep5": [_v(r"Un bloc de $2$ kg est traîné sur $10$ m sur un sol horizontal avec $\mu=0{,}5$. Travail du frottement (en J) ?", "-Rational(1,2)*2*10*10", "-100", r"$f=10$ N, $W_f=-100$ J.")],
    "eu1": [_v(r"Une force fournit $900$ J en $30$ s. Puissance (en W) ?", "900/30", "30", r"$P=30$ W.")],
    "eu2": [_v(r"Une force de $30$ N sur un objet à $5$ m/s, dans le sens de la vitesse. Puissance (en W) ?", "30*5", "150", r"$P=Fv=150$ W.")],
    "eu3": [_v(r"Un moteur soulève $50$ kg à vitesse constante de $2$ m/s, $g=10$. Puissance (en W) ?", "50*10*2", "1000", r"$P=mgv=1000$ W.")],
    "ec1": [_v(r"Énergie cinétique d'un objet de $4$ kg à $5$ m/s (en J) ?", "Rational(1,2)*4*5**2", "50", r"$\frac12mv^2=50$ J.")],
    "ec3": [_v(r"Un corps de $2$ kg part du repos et reçoit un travail total de $100$ J. Vitesse finale (en m/s) ?", "sqrt(2*100/2)", "10", r"$v=\sqrt{100}=10$ m/s.")],
    "ec5": [_v(r"Chute libre sans vitesse initiale de $45$ m. Vitesse à l'arrivée (en m/s) ?", "sqrt(2*10*45)", "30", r"$\sqrt{2gh}=30$ m/s.")],
    "eq1": [_v(r"Énergie potentielle d'un objet de $5$ kg à $2$ m (origine au sol) en J ?", "5*10*2", "100", r"$mgz=100$ J.")],
    "eq3": [_v(r"Objet de $1$ kg à $5$ m avec $v=4$ m/s. Énergie mécanique (en J) ?", "Rational(1,2)*1*4**2+1*10*5", "58", r"$8+50=58$ J.")],
    "ek1": [_v(r"Objet lâché sans vitesse de $20$ m. Vitesse au sol par conservation de l'énergie (en m/s) ?", "sqrt(2*10*20)", "20", r"$\sqrt{2gh}=20$ m/s.")],
    "ek5": [_v(r"Objet lancé verticalement à $20$ m/s. Hauteur maximale (en m) ?", "20**2/(2*10)", "20", r"$\frac{v_0^2}{2g}=20$ m.")],
    "en3": [_v(r"Une balle de $1$ kg lâchée de $3$ m rebondit à $2$ m. Énergie perdue (en J) ?", "1*10*(3-2)", "10", r"$mg\Delta h=10$ J.")],
    "en5": [_v(r"Un palet à $6$ m/s glisse sur du sol horizontal avec $\mu=0{,}2$. Distance d'arrêt (en m) ?", "6**2/(2*Rational(1,5)*10)", "9", r"$\frac{v_0^2}{2\mu g}=9$ m.")],
    "er1": [_v(r"Ressort $k=100$ N/m comprimé de $0{,}2$ m. Énergie élastique (en J) ?", "Rational(1,2)*100*Rational(1,5)**2", "2", r"$\frac12kx^2=2$ J.")],
    "er2": [_v(r"Ressort $k=300$ N/m comprimé de $0{,}1$ m. Force de rappel (en N) ?", "300*Rational(1,10)", "30", r"$kx=30$ N.")],
    "er5": [_v(r"Une masse de $2$ kg est suspendue à un ressort $k=200$ N/m. Allongement à l'équilibre (en m) ?", "2*10/200", "1/10", r"$mg/k=0{,}1$ m.")],
    "eo1": [_v(r"Poulie bloquée : masses $M=4$ kg des deux côtés et $m=1$ kg en plus à droite. Accélération (en m/s²) ?", "1*10/(2*4+1)", "10/9", r"$\frac{mg}{2M+m}=\frac{10}9$ m/s².")],
    "eo3": [_v(r"Accélération $a=\dfrac{10}9$ m/s², hauteur de chute $0{,}5$ m. Durée (en s) ?", "sqrt(2*Rational(1,2)/Rational(10,9))", "3*sqrt(10)/10", r"$t=\sqrt{\frac{2h}a}=\sqrt{0{,}9}=\frac{3\sqrt{10}}{10}$ s.")],
}
for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["id"] in VARIANTS:
            _e["variants"] = VARIANTS[_e["id"]]


EXTRA_PARTS = []

QUIZ = [
    {"notion": "travail", "type": "qcm", "q": r"Le travail d'une force constante $\vec F$ entre $A$ et $B$ est :",
     "choix": [r"$\vec F\cdot\overrightarrow{AB}$", r"$F\cdot AB\cdot\sin\alpha$", r"$F\cdot AB$ toujours", r"$\vec F\wedge\overrightarrow{AB}$"], "bonne": 0},
    {"notion": "travail", "type": "vf", "q": r"Une force perpendiculaire au déplacement ne fournit aucun travail.", "bonne": True},
    {"notion": "poids", "type": "vf", "q": r"Le travail du poids dépend du chemin suivi entre $A$ et $B$.", "bonne": False},
    {"notion": "poids", "type": "qcm", "q": r"Un objet de masse $m$ monte d'une hauteur $h$. Le travail du poids vaut :",
     "choix": [r"$-mgh$", r"$mgh$", r"$0$", r"$mg/h$"], "bonne": 0},
    {"notion": "puissance", "type": "qcm", "q": r"L'unité de la puissance est :", "choix": [r"le watt", r"le joule", r"le newton", r"le pascal"], "bonne": 0},
    {"notion": "puissance", "type": "vf", "q": r"Pour une force constante et une vitesse constante dans le même sens, $P=Fv$.", "bonne": True},
    {"notion": "cinetique", "type": "qcm", "q": r"D'après le théorème de l'énergie cinétique, la somme des travaux des forces extérieures est égale à :",
     "choix": [r"la variation de l'énergie cinétique", r"l'énergie cinétique", r"la variation de l'énergie potentielle", r"l'énergie potentielle"], "bonne": 0},
    {"notion": "cinetique", "type": "qcm", "q": r"Si la vitesse double, l'énergie cinétique :", "choix": [r"est multipliée par $4$", r"est multipliée par $2$", r"reste constante", r"est divisée par $2$"], "bonne": 0},
    {"notion": "potentielle", "type": "vf", "q": r"La valeur de l'énergie potentielle de pesanteur dépend du choix de l'origine des altitudes.", "bonne": True},
    {"notion": "potentielle", "type": "qcm", "q": r"Un objet au repos a une énergie mécanique égale à :", "choix": [r"son énergie potentielle", r"son énergie cinétique", r"zéro", r"$mg$"], "bonne": 0},
    {"notion": "conservation", "type": "vf", "q": r"L'énergie mécanique d'un système est toujours conservée.", "bonne": False},
    {"notion": "conservation", "type": "qcm", "q": r"Une bille lâchée sans vitesse de la hauteur $h$ (sans frottement) arrive avec la vitesse :",
     "choix": [r"$\sqrt{2gh}$", r"$gh$", r"$\sqrt{gh}$", r"$2gh$"], "bonne": 0},
    {"notion": "nonconservatif", "type": "qcm", "q": r"Avec un frottement, la variation d'énergie mécanique est égale :",
     "choix": [r"au travail (négatif) du frottement", r"à zéro", r"à l'énergie cinétique", r"au poids"], "bonne": 0},
    {"notion": "nonconservatif", "type": "vf", "q": r"Le travail d'une force de frottement est toujours négatif.", "bonne": True},
    {"notion": "ressort", "type": "qcm", "q": r"L'énergie élastique d'un ressort allongé de $x$ est :", "choix": [r"$\frac12kx^2$", r"$kx$", r"$\frac12kx$", r"$kx^2$"], "bonne": 0},
    {"notion": "ressort", "type": "vf", "q": r"L'énergie élastique d'un ressort comprimé est négative.", "bonne": False},
    {"notion": "newtonpoulie", "type": "qcm", "q": r"Pour une poulie idéale et un fil sans masse, la tension du fil :",
     "choix": [r"est la même des deux côtés", r"est nulle", r"est plus grande côté charge", r"dépend de la masse du fil"], "bonne": 0},
    {"notion": "newtonpoulie", "type": "qcm", "q": r"Quand un bus démarre brusquement, les passagers sont repoussés en arrière : c'est :",
     "choix": [r"la première loi de Newton", r"la deuxième loi de Newton", r"la troisième loi de Newton", r"le théorème de l'énergie cinétique"], "bonne": 0},
]

_W = r"$W=\vec F\cdot\overrightarrow{AB}=F\,AB\cos\alpha$"
_WP = r"$W_P=mg(z_A-z_B)$"
_WF = r"$W_f=-fL$ · $f=\mu mg\cos\alpha$ sur un plan incliné"
_P = r"$P=\frac W{\Delta t}$ · $P=Fv$ · $1\ \mathrm{kWh}=3{,}6\times10^6$ J"
_EC = r"$E_c=\frac12mv^2$ · $\Delta E_c=\sum W$"
_EP = r"$E_p=mgz$ · $E_m=E_c+E_p$"
_CONS = r"$E_m(A)=E_m(B)$ · $v=\sqrt{2g\Delta h}$"
_NC = r"$\Delta E_m=\sum W(\vec F_{nc})$"
_RES = r"$F=kx$ · $E_{p,el}=\frac12kx^2$ · $\frac12mv^2+\frac12kx^2=$ cste"
_POU = r"$\sum\vec F=m\vec a$ · même $T$ · $a=\frac{mg}{2M+m}$ · $h=\frac12at^2$ · $v^2=2ah$"

FORMULES = {
    "ew1": _W, "ew2": _W, "ew3": _W + r" · $\cos90^\circ=0$", "ew4": r"$W=xx'+yy'$ (produit scalaire)", "ew5": _W + r" · $\cos180^\circ=-1$",
    "ew6": _W + r" · $\Delta E_c=0\Rightarrow\sum W=0$",
    "ep1": _WP, "ep2": _WP, "ep3": r"$W_P=mgL\sin\alpha$", "ep4": r"$\vec R\perp\overrightarrow{AB}\Rightarrow W=0$", "ep5": _WF + r" · $f=\mu mg$",
    "ep6": _WP + r" · $\vec P\cdot\overrightarrow{AB}$", "ep7": _WF,
    "eu1": _P, "eu2": _P, "eu3": _P + r" · $F=mg$ à vitesse constante", "eu4": _P, "eu5": _P,
    "ec1": _EC, "ec2": _EC + r" · $72\ \mathrm{km/h}=20\ \mathrm{m/s}$", "ec3": _EC, "ec4": _EC + r" · $W_f=-Fd$", "ec5": _EC + r" · $W_P=mgh$", "ec6": _EC + r" · $W_P=-mgh$",
    "ec7": r"$v_B^2-v_A^2=2a\,AB$ · $F=ma$ · " + _EC,
    "eq1": _EP, "eq2": _EP + r" · au repos $E_c=0$", "eq3": _EP + r" · " + _EC, "eq4": r"$\Delta E_p=mg\Delta z$", "eq5": _EP + r" · $E_m$ constante", "eq6": _EP + r" · " + _NC,
    "ek1": _CONS, "ek2": _CONS + r" · $\frac12mv^2=mg(h-d)$", "ek3": _CONS, "ek4": r"$v^2=v_0^2+2g\Delta h$", "ek5": _CONS + r" · $\frac12mv_0^2=mgh$", "ek6": _CONS + r" · $h=L\sin\alpha$",
    "ek7": _CONS + r" · $W(\vec R)=0$",
    "en1": _NC + r" · " + _EC + r" · " + _WP, "en2": _EC, "en3": r"$\Delta E_m=mg(h'-h)$", "en4": _NC + r" · $E_m=mgz+\frac12mv^2$", "en5": r"$\frac12mv_0^2=\mu mg\,d$", "en6": _NC,
    "er1": _RES, "er2": _RES, "er3": _RES, "er4": _RES, "er5": r"$kx=mg$", "er6": _RES,
    "eo1": _POU, "eo2": _POU, "eo3": _POU, "eo4": _POU + r" · $E_m$", "eo5": _POU,
    "ex1": _W + r" · " + _EC + r" · $\|\vec F\|=\sqrt{F_x^2+F_y^2+F_z^2}$ · $F=ma$ · " + _NC,
    "ex2": _POU, "ex3": _EP + r" · " + _CONS, "ex4": _WP + r" · $W_P=mgL\sin\alpha$ · " + _WF.split(" · ")[0] + r" · " + _EC + r" · $P=W/\Delta t$",
    "ey1": _NC + r" · " + _RES + r" · $f=\mu mg$", "ey2": r"$W_P=mgL\sin\alpha$ · " + _P, "ey3": _POU, "ey4": _EC + r" · " + _WP, "ey5": _CONS + r" · $mg\cos\theta-R=\frac{mv^2}r$ · $R=0$",
}
