"""Level path: S2 physics, thermodynamics (state variables, 1st and 2nd principles, ideal gas, thermal machines).

Calibrated on the Moodle course « Cours_thermodynamique_V2 », the thermo TD1-3 (B3) and the text-layer S2 physics exams
(partiel May 2019, partiel 2020/2021, midterm 2030 correction); the other S2 physics exams are scans and not read yet.
R = 8,31 or 8,3 J/(mol·K) as in the exams, T(K) = θ(°C) + 273. `value` exercises are checked by sympy; `open` ones have a model answer.
"""

SUBJECT = {
    "id": "physique-s2-thermo",
    "ordre": 310,
    "matiere": "physique",
    "semestre": "S2",
    "ecue": "Thermodynamique",
    "titre": "Thermodynamique",
    "chapitres_moodle": ["02_Cours", "04_TD_Thermodynamique"],
    "td": "TD thermodynamique (Moodle Physique)",
    "examens": ["Partiel de physique (S2)"],
}

NOTIONS = [
    {"id": "etat", "titre": "Variables d'état et gaz parfait",
     "formule": r"$PV=nRT$ · $R=8{,}31$ J·mol$^{-1}$·K$^{-1}$ · $T(\mathrm K)=\theta(^\circ\mathrm C)+273$ · 1 bar $=10^5$ Pa · 1 L $=10^{-3}$ m³ · $n$ constant : $\dfrac{P_1V_1}{T_1}=\dfrac{P_2V_2}{T_2}$",
     "exemple": r"volume constant, $T$ de $250$ K à $300$ K : $P$ est multipliée par $\frac{300}{250}=\frac65$",
     "cours": r"Toujours convertir en kelvin, pascal et mètre cube avant de calculer. Intensives (indépendantes de la taille) : $T$, $P$. Extensives : $V$, $n$, $m$, $U$. Système ouvert : échange matière et énergie ; fermé : énergie seulement ; isolé : rien."},
    {"id": "energie_interne", "titre": "Énergie interne et capacité thermique",
     "formule": r"$dU=C_v\,dT$ · $\Delta U=C_v\Delta T=m\,c_v\Delta T$ · gaz parfait monoatomique : $C_v=\frac32nR$ · $\Delta U$ ne dépend que de l'état initial et final",
     "exemple": r"$150$ kg d'eau de $10$ à $60$ °C, $c_v=4{,}2$ kJ·kg$^{-1}$·K$^{-1}$ : $\Delta U=150\times4{,}2\times50=31\,500$ kJ",
     "cours": r"$U$ est une fonction d'état : sur un cycle, $\Delta U=0$. $C_v$ est supposée indépendante de $T$. Pour une phase condensée, $C_v=m\,c_v$ avec $c_v$ massique en J·kg$^{-1}$·K$^{-1}$."},
    {"id": "travail", "titre": "Travail des forces de pression",
     "formule": r"$W=-\displaystyle\int_{V_i}^{V_f}P_{ext}\,dV$ · isochore : $W=0$ · monobare : $W=-P_0(V_f-V_i)$ · isotherme réversible (gaz parfait) : $W=nRT\ln\dfrac{V_i}{V_f}=nRT\ln\dfrac{P_f}{P_i}$",
     "exemple": r"compression monobare à $10^5$ Pa de $3$ L à $1$ L : $W=-10^5\times(10^{-3}-3\times10^{-3})=+200$ J",
     "cours": r"Convention : $W>0$ si le système reçoit de l'énergie. Compression ($dV<0$) : $W>0$. Détente : $W<0$. Isobare avec variation de volume implique monobare. Pour une isotherme réversible, $P_{ext}=P=\frac{nRT}V$."},
    {"id": "chaleur", "titre": "Transfert thermique et calorimétrie",
     "formule": r"$Q=m\,c\,\Delta T$ · changement d'état à $T$ constante : $Q=m\,\Delta h_{fus}$ · calorimètre isolé : $\sum Q=0$ · adiabatique : $Q=0$",
     "exemple": r"$0{,}5$ kg d'eau de $20$ à $100$ °C, $c=4200$ J·kg$^{-1}$·K$^{-1}$ : $Q=0{,}5\times4200\times80=168\,000$ J",
     "cours": r"Trois modes : conduction (sans déplacement de matière), convection (avec un fluide en mouvement), rayonnement. Calorimétrie : tout ce qui est reçu par un corps est cédé par un autre. Vérifier d'abord si toute la glace peut fondre avant de supposer l'état final."},
    {"id": "premier", "titre": "Premier principe et enthalpie",
     "formule": r"$\Delta U=Q+W$ · $H=U+PV$ · $dH=C_p\,dT$ · isochore : $Q=\Delta U$ · monobare (état initial et final à $P_0$) : $Q=\Delta H$ · cycle : $\Delta U=0$, donc $Q=-W$",
     "exemple": r"$Q=-150$ J et $W=+400$ J : $\Delta U=250$ J",
     "cours": r"$\Delta U=Q+W$ traduit la conservation de l'énergie (on néglige les énergies cinétique et potentielle). $Q$ et $W$ dépendent du chemin suivi, pas $\Delta U$ ni $\Delta H$ : jamais de « $\Delta$ » devant $Q$ ou $W$."},
    {"id": "gp", "titre": "Gaz parfait : Mayer, Laplace, adiabatique",
     "formule": r"$C_p-C_v=nR$ · $\gamma=\dfrac{C_p}{C_v}$ · $C_v=\dfrac{nR}{\gamma-1}$ · adiabatique réversible : $PV^\gamma=$ cte, $TV^{\gamma-1}=$ cte, $T^\gamma P^{1-\gamma}=$ cte · $W=\Delta U=C_v\Delta T$",
     "exemple": r"monoatomique : $C_v=\frac32nR$, $\gamma=\frac53$ ; diatomique : $C_v=\frac52nR$, $\gamma=\frac75$",
     "cours": r"Quand $Q=0$, le premier principe donne $W=\Delta U$. Les lois de Laplace valent seulement pour une adiabatique réversible d'un gaz parfait. Elles se retrouvent à partir de $PV^\gamma=$ cte et $PV=nRT$."},
    {"id": "diagrammes", "titre": "Diagrammes de phase et de Clapeyron",
     "formule": r"point triple : trois phases en équilibre · point critique : au-delà, fluide supercritique · palier d'Andrews $(P,v)$ : liquide $+$ gaz à $T$ et $P$ constants · courbe d'ébullition (côté liquide), courbe de rosée (côté gaz)",
     "exemple": r"eau : la courbe de fusion $(P,T)$ a une pente négative",
     "cours": r"Sur la courbe de changement d'état de $(P,T)$, les deux phases coexistent mais le diagramme ne dit pas en quelle proportion : il faut $(P,v)$. Sur le palier, $P$ et $T$ sont liés, donc le volume massique $v$ fixe la proportion de chaque phase."},
    {"id": "entropie", "titre": "Entropie et deuxième principe",
     "formule": r"$\Delta S=S_{ech}+S_{cr}$ · $S_{ech}=\dfrac QT$ · $S_{cr}\geq0$, $=0$ si réversible · adiabatique réversible : $\Delta S=0$ (isentropique)",
     "exemple": r"$Q=600$ J reçus d'un thermostat à $300$ K, de façon réversible : $\Delta S=2$ J·K$^{-1}$",
     "cours": r"Le premier principe n'interdit pas une détente de Joule–Gay-Lussac à l'envers ; le deuxième impose $S_{cr}\geq0$ et donne le sens de l'évolution. $T$ est la température de la source avec laquelle l'échange a lieu, en kelvin."},
    {"id": "machines", "titre": "Machines thermiques dithermes",
     "formule": r"cycle : $Q_c+Q_f+W=0$ et $\dfrac{Q_c}{T_c}+\dfrac{Q_f}{T_f}+S_{cr}=0$ · moteur : $\rho=-\dfrac W{Q_c}=1+\dfrac{Q_f}{Q_c}\leq1-\dfrac{T_f}{T_c}$ · frigo : $e=\dfrac{Q_f}W\leq\dfrac{T_f}{T_c-T_f}$ · PAC : $\mathrm{COP}=-\dfrac{Q_c}W\leq\dfrac{T_c}{T_c-T_f}$",
     "exemple": r"frigo entre $T_f=278$ K et $T_c=298$ K : $e\leq\frac{278}{20}\approx14$",
     "cours": r"$Q>0$ si reçu par la machine. Moteur : $W<0$ et $Q_c>0$. Frigo : on prend $Q_f>0$ à la source froide avec $W>0$. PAC : on cède $Q_c<0$ à la source chaude. Efficacité d'un frigo ou d'une PAC supérieure à $1$ est possible ; le rendement d'un moteur est toujours inférieur à $1$."},
    {"id": "cycles", "titre": "Cycles : Carnot, Stirling, Lenoir, Brayton",
     "formule": r"Carnot (2 isothermes + 2 adiabatiques réversibles) : $\rho=1-\dfrac{T_f}{T_c}$ · Stirling : 2 isothermes + 2 isochores · Lenoir : isochore + isotherme + isobare · Brayton : 2 isobares + 2 adiabatiques, $\rho=1-\left(\dfrac{P_A}{P_B}\right)^{\frac{\gamma-1}\gamma}$",
     "exemple": r"Carnot entre $300$ K et $600$ K : $\rho=\frac12$",
     "cours": r"Sur un cycle $\Delta U=0$ donc $W=-\sum Q$. Un cycle parcouru dans le sens horaire du diagramme $(P,V)$ est moteur ($W<0$). Pour chaque étape : identifier la transformation, calculer $W$ et $Q$, puis vérifier le bilan du cycle."},
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


TD1 = "TD1 de thermodynamique"
TD2 = "TD2 de thermodynamique"
TD3 = "TD3 de thermodynamique"
P19 = "Partiel de physique n° 2 (mai 2019)"
P21 = "Partiel de physique 2020/2021"
M30 = "Midterm de physique 2030 (S2)"

LEVELS = [
    {"n": 1, "titre": "Variables d'état et gaz parfait", "notions": ["etat"], "exos": [
        v("he1", r"Convertir $27$ °C en kelvin (on prend $T=\theta+273$).", "27+273", "300", r"$T=27+273=300$ K.", duree=1),
        v("he2", r"Pneu à volume constant, gonflé à $3$ bar à $-23$ °C. Quelle pression (en bar) à $27$ °C ?", "3*300/250", "18/5",
          r"$T_1=250$ K, $T_2=300$ K. À $V$ et $n$ constants, $\frac{P_1}{T_1}=\frac{P_2}{T_2}$ donc $P_2=3\times\frac{300}{250}=3{,}6$ bar.", src=TD1 + ", ex. 1 (adapté)", duree=3),
        v("he3", r"Volume (en L) occupé par $1$ mol de gaz parfait à $300$ K sous $1$ bar ? ($R=8{,}31$)", "Rational(831,100)*300/10**5*1000", "2493/100",
          r"$V=\frac{nRT}P=\frac{8{,}31\times300}{10^5}=2{,}493\times10^{-2}$ m³ $\approx24{,}9$ L.", duree=3),
        v("he4", r"À température constante, on divise par $4$ le volume d'un gaz parfait. Par combien est multipliée la pression ?", "4", "4",
          r"$PV=nRT=$ cte : $P_2V_2=P_1V_1$ avec $V_2=\frac{V_1}4$, donc $P_2=4P_1$.", duree=1),
        o("he5", r"Parmi $T$, $V$, $P$, $n$, $U$, lesquelles sont intensives, lesquelles extensives ? Un café dans une bouteille thermos fermée est-il un système ouvert, fermé ou isolé ?",
          r"Intensives : $T$, $P$ (inchangées si on double le système). Extensives : $V$, $n$, $U$ (doublent). Un thermos fermé : isolé en première approximation (ni matière ni énergie échangées), fermé sinon.", duree=3),
    ]},
    {"n": 2, "titre": "Énergie interne et capacité thermique", "notions": ["energie_interne"], "exos": [
        v("hu1", r"$150$ kg d'eau passent de $10$ à $60$ °C, $c_v=4{,}2$ kJ·kg$^{-1}$·K$^{-1}$. Variation d'énergie interne (en kJ) ?", "150*Rational(42,10)*50", "31500",
          r"$\Delta U=mc_v\Delta T=150\times4{,}2\times50=31\,500$ kJ.", src="Cours, exemple 1", duree=2),
        v("hu2", r"Exprimer ces $31\,500$ kJ en kWh ($1$ kWh $=3600$ kJ).", "31500/3600", "35/4", r"$\frac{31\,500}{3600}=8{,}75$ kWh.", src="Cours, exemple 1", duree=2),
        v("hu3", r"$1$ mol de gaz parfait monoatomique voit sa température augmenter de $100$ K. Variation d'énergie interne (en J) ? ($R=8{,}3$)", "Rational(3,2)*Rational(83,10)*100", "1245",
          r"$\Delta U=C_v\Delta T=\frac32nR\Delta T=1{,}5\times8{,}3\times100=1245$ J.", duree=3),
        v("hu4", r"Bloc de cuivre de $2$ kg, $c=400$ J·kg$^{-1}$·K$^{-1}$, chauffé de $20$ à $70$ °C. $\Delta U$ (en J) ?", "2*400*50", "40000", r"$mc\Delta T=2\times400\times50=40\,000$ J.", duree=2),
        o("hu5", r"Pourquoi $\Delta U=0$ sur un cycle ? Et pourquoi dit-on que $U$ est une fonction d'état ?",
          r"$U$ ne dépend que de l'état du système ($P$, $T$, $V$, $n$) et non de la manière dont il y est arrivé. Un cycle ramène le système à son état initial, donc $\Delta U=U_f-U_i=0$.", duree=3),
    ]},
    {"n": 3, "titre": "Travail des forces de pression", "notions": ["travail"], "exos": [
        v("hw1", r"Un gaz est chauffé dans une enceinte rigide. Travail des forces de pression (en J) ?", "0", "0", r"Isochore : $dV=0$, donc $W=-\int P_{ext}dV=0$.", duree=1),
        v("hw2", r"Compression monobare à $P_0=1$ bar : le volume passe de $3$ L à $1$ L. Travail reçu (en J) ?", "-10**5*(Rational(1,1000)-Rational(3,1000))", "200",
          r"$W=-P_0(V_f-V_i)=-10^5\times(10^{-3}-3\times10^{-3})=+200$ J : positif, le gaz reçoit de l'énergie.", duree=3),
        v("hw3", r"Détente monobare à $2$ bar : le volume passe de $1$ L à $4$ L. Travail reçu (en J) ?", "-2*10**5*(Rational(4,1000)-Rational(1,1000))", "-600",
          r"$W=-2\times10^5\times3\times10^{-3}=-600$ J : négatif, le gaz fournit de l'énergie.", duree=3),
        v("hw4", r"Compression isotherme réversible d'un gaz parfait de $V_1=2$ L à $\frac{V_1}{10}$, avec $P_1=1$ bar. Donner $W$ en J avec $\ln10=2{,}3$.", "10**5*Rational(2,1000)*Rational(23,10)", "460",
          r"$W=nRT\ln\frac{V_1}{V_2}=P_1V_1\ln10=10^5\times2\times10^{-3}\times2{,}3=460$ J.", src=P19 + ", ex. 1 (adapté)", duree=4),
        o("hw5", r"Retrouver $W=nRT\ln\dfrac{V_i}{V_f}$ pour une isotherme réversible d'un gaz parfait.",
          r"Réversible : $P_{ext}=P=\dfrac{nRT}V$. Alors $W=-\displaystyle\int_{V_i}^{V_f}\frac{nRT}V\,dV=-nRT\ln\frac{V_f}{V_i}=nRT\ln\frac{V_i}{V_f}$. Comme $PV$ est constant, c'est aussi $nRT\ln\frac{P_f}{P_i}$.", duree=4),
    ]},
    {"n": 4, "titre": "Transfert thermique et calorimétrie", "notions": ["chaleur"], "exos": [
        v("hq1", r"Chaleur reçue (en J) par $0{,}5$ kg d'eau chauffée de $20$ à $100$ °C ($c=4200$ J·kg$^{-1}$·K$^{-1}$) ?", "Rational(1,2)*4200*80", "168000", r"$Q=mc\Delta T=0{,}5\times4200\times80=168\,000$ J.", duree=2),
        v("hq2", r"On mélange $2$ kg d'eau à $80$ °C et $3$ kg d'eau à $20$ °C dans un calorimètre isolé. Température finale (en °C) ?", "(2*80+3*20)/Rational(5)", "44",
          r"$\sum Q=0$ : $2c(T_F-80)+3c(T_F-20)=0$, donc $T_F=\frac{2\times80+3\times20}5=44$ °C.", duree=3),
        v("hq3", r"Énergie (en kJ) pour fondre $0{,}5$ kg de glace à $0$ °C ($\Delta h_{fus}=335$ kJ·kg$^{-1}$) ?", "Rational(1,2)*335", "335/2", r"$Q=m\Delta h_{fus}=0{,}5\times335=167{,}5$ kJ.", src=TD1 + ", ex. 3", duree=2),
        v("hq4", r"$1$ kg d'eau liquide passe de $20$ °C à $0$ °C ($c=4{,}2$ kJ·kg$^{-1}$·K$^{-1}$). Énergie cédée (en kJ) ?", "Rational(42,10)*20", "84", r"$mc|\Delta T|=1\times4{,}2\times20=84$ kJ.", src=TD1 + ", ex. 3", duree=2),
        v("hq5", r"On ajoute $0{,}5$ kg de glace à $0$ °C à $1$ kg d'eau à $20$ °C. Les $84$ kJ cédés ne suffisent pas à fondre toute la glace ($167{,}5$ kJ). Quelle masse de glace fond (en g) ? ($\Delta h_{fus}=335$ kJ·kg$^{-1}$)", "Rational(84)/335*1000", "84000/335",
          r"L'état final est à $0$ °C. $m_{fondue}=\frac{84}{335}\approx0{,}251$ kg, soit environ $251$ g ; il reste $\approx249$ g de glace, donc $x\approx0{,}50$.", src=TD1 + ", ex. 3", duree=4),
        o("hq6", r"Citer les trois modes de transfert thermique avec un exemple de chaque.",
          r"Conduction : transfert sans déplacement de matière (barre de métal chauffée à une extrémité). Convection : transfert porté par un fluide en mouvement (chauffage soufflant). Rayonnement : par onde électromagnétique (soleil, radiateur infrarouge).", duree=2),
    ]},
    {"n": 5, "titre": "Changement d'état et enthalpie", "notions": ["chaleur", "premier"], "exos": [
        v("hh1", r"$1{,}0$ g de glace passe de $250$ K à $273$ K ($c_g=2{,}1$ kJ·kg$^{-1}$·K$^{-1}$). $\Delta H_1$ (en J) ?", "Rational(1,1000)*2100*23", "483/10", r"$\Delta H_1=mc_g\Delta T=10^{-3}\times2100\times23=48{,}3$ J.", src="Cours, exemple 2", duree=2),
        v("hh2", r"Même échantillon : $1{,}0$ g de glace à $250$ K devient de l'eau à $300$ K. Variation totale d'enthalpie (en J), avec $\Delta h_{fus}=335$ kJ·kg$^{-1}$ et $c_e=4{,}2$ kJ·kg$^{-1}$·K$^{-1}$ ?", "Rational(1,1000)*(2100*23+335000+4200*27)", "4967/10",
          r"Trois étapes : réchauffer la glace ($48{,}3$ J), fondre ($335$ J), réchauffer l'eau de $273$ à $300$ K ($113{,}4$ J). Somme : $496{,}7$ J.", src="Cours, exemple 2", duree=5),
        v("hh3", r"$\Delta U=500$ J lors d'une transformation à $P=10^5$ Pa où le volume augmente de $2$ L. Calculer $\Delta H$ (en J).", "500+10**5*Rational(2,1000)", "700",
          r"$H=U+PV$ donc à $P$ constante $\Delta H=\Delta U+P\Delta V=500+10^5\times2\times10^{-3}=700$ J.", duree=3),
        v("hh4", r"Pour refroidir $200$ g de jus de $25$ °C à $5$ °C, on ajoute des glaçons à $-18$ °C. $m\,(\Delta h_{fus}+c_g\cdot18+c_e\cdot5)=200\,c_e\cdot20$ avec $\Delta h_{fus}=330$, $c_g=2{,}1$, $c_e=4{,}2$ (kJ·kg$^{-1}$, kJ·kg$^{-1}$·K$^{-1}$). Masse de glaçons (en g) ?",
          "200*Rational(42,10)*20/(330+Rational(21,10)*18+Rational(42,10)*5)", "3500/81",
          r"$m=\dfrac{200\times4{,}2\times20}{330+2{,}1\times18+4{,}2\times5}=\dfrac{16\,800}{388{,}8}\approx43{,}2$ g.", src=TD1 + ", ex. 4 (corrigé)", duree=6),
        o("hh5", r"Pourquoi la température reste-t-elle constante pendant la fusion de la glace alors qu'on lui fournit de l'énergie ?",
          r"L'énergie fournie sert à rompre les liaisons du solide (changement de phase), pas à augmenter l'agitation thermique. $Q=m\Delta h_{fus}$ à $T$ constante : $\Delta H\neq0$ avec $\Delta T=0$.", duree=3),
    ]},
    {"n": 6, "titre": "Premier principe", "notions": ["premier"], "exos": [
        v("hp1", r"Un système cède $150$ J de chaleur et reçoit $400$ J de travail. Variation d'énergie interne (en J) ?", "-150+400", "250", r"$\Delta U=Q+W=-150+400=250$ J.", duree=1),
        v("hp2", r"Un moteur reçoit $300$ J de chaleur sur un cycle. Travail reçu sur le cycle (en J) ?", "-300", "-300", r"$\Delta U=0$ donc $W=-Q=-300$ J : le moteur fournit $300$ J.", duree=2),
        v("hp3", r"Transformation isochore, $C_v=20$ J·K$^{-1}$, $\Delta T=15$ K. Chaleur reçue (en J) ?", "20*15", "300", r"$W=0$, donc $Q=\Delta U=C_v\Delta T=300$ J.", duree=2),
        v("hp4", r"Transformation isobare, $C_p=29$ J·K$^{-1}$, $\Delta T=10$ K. Chaleur reçue (en J) ?", "29*10", "290", r"À pression constante, $Q=\Delta H=C_p\Delta T=290$ J.", duree=2),
        o("hp5", r"Joule–Gay-Lussac : un gaz parfait se détend dans le vide entre deux récipients à parois adiabatiques. Calculer $W$, $Q$, $\Delta U$ et conclure sur $T$.",
          r"Détente dans le vide : $P_{ext}=0$ donc $W=0$. Parois adiabatiques : $Q=0$. Alors $\Delta U=0$ ; pour un gaz parfait $U$ ne dépend que de $T$, donc $T$ est inchangée. La transformation est irréversible : le premier principe ne l'interdit pas à l'envers, le deuxième si.", src="Cours, partie IV", duree=5),
    ]},
    {"n": 7, "titre": "Transformations du gaz parfait", "notions": ["gp", "travail", "premier"], "exos": [
        v("hg1", r"Gaz parfait avec $C_v=\frac52nR$. Que vaut $\gamma=\dfrac{C_p}{C_v}$ ?", "Rational(7,2)/Rational(5,2)", "7/5", r"Mayer : $C_p=C_v+nR=\frac72nR$, donc $\gamma=\frac75$.", duree=2),
        v("hg2", r"$1$ mol de gaz parfait ($C_v=\frac52R$, $R=8{,}3$) chauffée à volume constant de $300$ à $400$ K. $Q$ (en J) ?", "Rational(5,2)*Rational(83,10)*100", "2075", r"$Q=\Delta U=C_v\Delta T=2{,}5\times8{,}3\times100=2075$ J.", duree=3),
        v("hg3", r"Même gaz chauffé à pression constante de $300$ à $400$ K. $Q$ (en J) ?", "Rational(7,2)*Rational(83,10)*100", "2905", r"$Q=\Delta H=C_p\Delta T=3{,}5\times8{,}3\times100=2905$ J.", duree=3),
        v("hg4", r"Compression isotherme réversible d'un gaz parfait avec $W=+420$ J. Chaleur reçue (en J) ?", "-420", "-420", r"Isotherme d'un gaz parfait : $\Delta U=0$, donc $Q=-W=-420$ J : chaleur cédée.", src=P19 + ", ex. 1", duree=2),
        v("hg5", r"Un gaz passe de $(1\ \mathrm{bar},3\ \mathrm L)$ à $(3\ \mathrm{bar},1\ \mathrm L)$ par une isochore puis une isobare à $3$ bar. Chaleur reçue $Q$ (en J) ? ($P_1V_1=P_2V_2$ donc $\Delta U=0$)", "0-(-3*10**5*(Rational(1,1000)-Rational(3,1000)))", "-600",
          r"Isochore : $W=0$. Isobare à $3$ bar de $3$ L à $1$ L : $W=-3\times10^5\times(-2\times10^{-3})=+600$ J. $\Delta U=0$ donc $Q=-600$ J : chaleur évacuée.", src=TD2 + ", ex. 2", duree=5),
        v("hg6", r"Même passage de $(1\ \mathrm{bar},3\ \mathrm L)$ à $(3\ \mathrm{bar},1\ \mathrm L)$ par une isobare à $1$ bar puis une isochore. $Q$ (en J) ?", "0-(-10**5*(Rational(1,1000)-Rational(3,1000)))", "-200",
          r"Isobare à $1$ bar de $3$ L à $1$ L : $W=+200$ J. Isochore : $W=0$. $\Delta U=0$ donc $Q=-200$ J.", src=TD2 + ", ex. 2", duree=5),
        o("hg7", r"Même passage par l'isotherme réversible $PV=$ cte. Calculer $W$ et $Q$, puis comparer aux deux autres chemins. Conclusion ?",
          r"$W=P_1V_1\ln\frac{V_1}{V_2}=300\ln3\approx330$ J (avec $P_1V_1=10^5\times3\times10^{-3}=300$ J) et $Q=-W\approx-330$ J." "\n\n"
          r"Les trois chemins ont le même $\Delta U=0$ mais des $W$ différents ($600$, $200$, $330$ J) et des $Q$ différents : $W$ et $Q$ dépendent du chemin, pas $\Delta U$.", src=TD2 + ", ex. 2", duree=6),
    ]},
    {"n": 8, "titre": "Adiabatique et lois de Laplace", "notions": ["gp"], "exos": [
        v("ha1", r"Compression adiabatique réversible de $1$ mol de gaz parfait monoatomique qui échauffe le gaz de $60$ K. Travail reçu (en J) ? ($R=8{,}3$)", "Rational(3,2)*Rational(83,10)*60", "747",
          r"$Q=0$, donc $W=\Delta U=\frac32nR\Delta T=1{,}5\times8{,}3\times60=747$ J.", src=P19 + ", ex. 1 II", duree=3),
        v("ha2", r"Compression adiabatique réversible, $\gamma=\frac53$, volume divisé par $8$. Par combien est multipliée la pression ?", "8**Rational(5,3)", "32",
          r"$PV^\gamma=$ cte : $\frac{P_2}{P_1}=\left(\frac{V_1}{V_2}\right)^\gamma=8^{5/3}=2^5=32$.", duree=3),
        v("ha3", r"Même compression ($\gamma=\frac53$, volume divisé par $8$) à partir de $T_1=300$ K. Température finale (en K) ?", "300*8**Rational(2,3)", "1200",
          r"$TV^{\gamma-1}=$ cte : $T_2=T_1\times8^{2/3}=300\times4=1200$ K.", duree=3),
        v("ha4", r"Même compression avec $P_1V_1=100$ J et $P_2V_2=400$ J. Travail $W=\dfrac{P_2V_2-P_1V_1}{\gamma-1}$ (en J) ?", "(400-100)/(Rational(5,3)-1)", "450",
          r"$W=\dfrac{400-100}{\frac53-1}=\dfrac{300}{2/3}=450$ J.", duree=3),
        o("ha5", r"À partir de $PV^\gamma=$ cte et $PV=nRT$, établir $T^\gamma P^{1-\gamma}=$ cte.",
          r"$V=\dfrac{nRT}P$ donc $PV^\gamma=P\left(\dfrac{nRT}P\right)^\gamma=(nR)^\gamma\,T^\gamma P^{1-\gamma}$. Comme $PV^\gamma$ et $(nR)^\gamma$ sont constants, $T^\gamma P^{1-\gamma}=$ cte.", src=P19 + ", QCM 8", duree=4),
    ]},
    {"n": 9, "titre": "Diagrammes de phase et de Clapeyron", "notions": ["diagrammes"], "exos": [
        o("hd1", r"Définir : isobare, isotherme, isochore, monobare, monotherme, adiabatique, réversible.",
          r"Isobare : $P=$ cte. Isotherme : $T=$ cte. Isochore : $V=$ cte. Monobare : $P_{ext}=$ cte. Monotherme : $T_{ext}=$ cte. Adiabatique : $Q=0$. Réversible : suite d'états d'équilibre, on peut revenir en arrière en inversant les causes (lent, sans frottement).", src=TD2 + ", ex. 1", duree=4),
        o("hd2", r"Dans le diagramme $(P,v)$ avec isothermes d'Andrews, situer : liquide, gaz, liquide $+$ gaz, courbe de rosée, courbe d'ébullition.",
          r"La courbe de saturation (qui passe par le point critique $C$) délimite le domaine de coexistence. À gauche : liquide ; à droite : gaz ; sous la courbe : liquide $+$ gaz, avec un palier horizontal pour chaque isotherme. Branche gauche de la courbe : courbe d'ébullition ; branche droite : courbe de rosée.", src=TD2 + ", ex. 1", duree=5),
        o("hd3", r"Dans le diagramme $(P,T)$, décrire les domaines, le point triple et le point critique. Qu'a de particulier l'eau ?",
          r"Trois domaines : solide, liquide, gaz, séparés par les courbes de fusion, vaporisation et sublimation. Au point triple, les trois phases coexistent. Au point critique, liquide et gaz ne se distinguent plus : fluide supercritique. Pour l'eau la courbe de fusion a une pente négative (la glace fond sous pression, et elle flotte sur l'eau).", duree=5),
        o("hd4", r"Sur un palier de changement d'état, $P$ et $T$ ne suffisent pas à décrire l'état du système. Pourquoi, et que faut-il ajouter ?",
          r"Sur le palier, $P$ et $T$ sont liés ($P=P_{sat}(T)$) et restent constants quelle que soit la proportion de liquide et de gaz. Il faut une troisième variable, le volume massique $v$, pour fixer la proportion de chaque phase : c'est l'intérêt du diagramme de Clapeyron.", duree=4),
    ]},
    {"n": 10, "titre": "Entropie et deuxième principe", "notions": ["entropie"], "exos": [
        v("hs1", r"Un système reçoit $Q=600$ J d'un thermostat à $300$ K. Entropie échangée (en J·K$^{-1}$) ?", "600/300", "2", r"$S_{ech}=\frac QT=\frac{600}{300}=2$ J·K$^{-1}$.", duree=1),
        v("hs2", r"Fusion de $0{,}1$ kg de glace à $273$ K ($\Delta h_{fus}=335$ kJ·kg$^{-1}$), réversible. $\Delta S$ (en J·K$^{-1}$) ?", "Rational(1,10)*335000/273", "33500/273",
          r"$Q=m\Delta h_{fus}=33\,500$ J à $T=273$ K constante : $\Delta S=\frac QT\approx122{,}7$ J·K$^{-1}$.", duree=3),
        v("hs3", r"$1000$ J passent spontanément d'une source à $400$ K vers une source à $300$ K. Entropie créée (en J·K$^{-1}$) ?", "-Rational(1000,400)+Rational(1000,300)", "5/6",
          r"$\Delta S_{tot}=-\frac{1000}{400}+\frac{1000}{300}=\frac56\approx0{,}83$ J·K$^{-1}$. Positif : transformation irréversible, possible dans ce sens seulement.", duree=4),
        o("hs4", r"Pour la détente de Joule–Gay-Lussac, $Q=0$. Quel est le signe de $S_{cr}$ ? Que dit le deuxième principe de la transformation inverse ?",
          r"$\Delta S=S_{ech}+S_{cr}=0+S_{cr}$. La détente a lieu spontanément, donc $S_{cr}>0$ (irréversible). La transformation inverse aurait $S_{cr}<0$ : impossible. Le premier principe ne l'interdit pas (il donne $\Delta U=0$ dans les deux sens).", src="Cours, partie IV", duree=4),
        o("hs5", r"Que signifie « isentropique » ? À quelle condition une transformation l'est-elle ?",
          r"$\Delta S=0$. Comme $\Delta S=\frac QT+S_{cr}$, il faut $Q=0$ (adiabatique) et $S_{cr}=0$ (réversible) : une adiabatique réversible est isentropique.", duree=3),
    ]},
    {"n": 11, "titre": "Machines thermiques dithermes", "notions": ["machines", "entropie"], "exos": [
        v("hm1", r"Moteur : $Q_c=1000$ J, $Q_f=-600$ J. Rendement $\rho$ ?", "Rational(400,1000)", "2/5", r"$W=-(Q_c+Q_f)=-400$ J, $\rho=-\frac W{Q_c}=\frac{400}{1000}=0{,}4$.", duree=2),
        v("hm2", r"Rendement maximal d'un moteur entre $T_c=600$ K et $T_f=300$ K ?", "1-Rational(300,600)", "1/2", r"$\rho\leq1-\frac{T_f}{T_c}=\frac12$.", duree=2),
        v("hm3", r"Efficacité maximale d'un réfrigérateur entre $T_f=278$ K (intérieur) et $T_c=298$ K (cuisine) ?", "Rational(278,20)", "139/10", r"$e\leq\frac{T_f}{T_c-T_f}=\frac{278}{20}=13{,}9\approx14$.", src=M30 + ", ex. 2", duree=3),
        v("hm4", r"COP maximal d'une pompe à chaleur entre $T_f=273$ K (extérieur) et $T_c=293$ K (maison) ?", "Rational(293,20)", "293/20", r"$\mathrm{COP}\leq\frac{T_c}{T_c-T_f}=\frac{293}{20}=14{,}65$.", duree=3),
        v("hm5", r"Un frigo reçoit $W=100$ J d'électricité et prend $Q_f=400$ J à la source froide. Efficacité ?", "400/Rational(100)", "4", r"$e=\frac{Q_f}W=4$ : $1$ J d'électricité déplace $4$ J de chaleur.", duree=2),
        o("hm6", r"Montrer qu'un moteur avec une seule source de chaleur ne peut pas fournir de travail.",
          r"Cycle monotherme : $\Delta U=Q+W=0$ donc $W=-Q$. $\Delta S=\frac QT+S_{cr}=0$ donc $Q=-TS_{cr}\leq0$. Alors $W=-Q\geq0$ : le système reçoit du travail au lieu d'en fournir. Un moteur ($W<0$) exige deux sources.", src=TD3 + ", ex. 1", duree=5),
        o("hm7", r"Pompe à chaleur : schéma énergétique, COP en détaillant, puis cas réversible.",
          r"Schéma : flèche $Q_f>0$ de la source froide vers la machine, flèche $W>0$ vers la machine, flèche $Q_c<0$ de la machine vers la source chaude." "\n\n"
          r"1er principe : $W=-(Q_c+Q_f)$ donc $\mathrm{COP}=-\frac{Q_c}W=\frac{Q_c}{Q_c+Q_f}=\frac1{1+Q_f/Q_c}$." "\n\n"
          r"2e principe : $\frac{Q_f}{T_f}+\frac{Q_c}{T_c}+S_{cr}=0$ donc $\frac{Q_f}{Q_c}=-\frac{T_f}{T_c}-\frac{T_fS_{cr}}{Q_c}$. Réversible ($S_{cr}=0$) : $\mathrm{COP}=\dfrac1{1-T_f/T_c}=\dfrac{T_c}{T_c-T_f}$, et c'est un maximum.", src=TD3 + ", ex. 2", duree=8),
    ]},
    {"n": 12, "titre": "Cycles : Carnot, Stirling, Lenoir", "notions": ["cycles", "travail", "premier"], "exos": [
        v("hc1", r"Stirling : $n=40$ mmol, état 1 à $P_1=1$ bar et $T_1=300$ K. Volume $V_1$ (en L) ? ($R=8{,}31$)", "Rational(4,100)*Rational(831,100)*300/10**5*1000", "2493/2500",
          r"$V_1=\frac{nRT_1}{P_1}=\frac{0{,}04\times8{,}31\times300}{10^5}\approx9{,}97\times10^{-4}$ m³ $\approx1{,}0$ L.", src=TD3 + ", ex. 3", duree=3),
        v("hc2", r"Stirling, étape 1→2 : compression isotherme jusqu'à $V_2=\frac{V_1}{10}$ à $T_1$. Pression $P_2$ (en bar) ?", "10", "10", r"$P_2=P_1\frac{V_1}{V_2}=10$ bar.", src=TD3 + ", ex. 3", duree=1),
        v("hc3", r"Travail reçu en 1→2 (en J) avec $nRT_1=0{,}04\times8{,}31\times300$ et $\ln10=2{,}3$ ?", "Rational(4,100)*Rational(831,100)*300*Rational(23,10)", "57339/250",
          r"$W_{12}=nRT_1\ln\frac{V_1}{V_2}=99{,}72\times2{,}3\approx229$ J (positif : compression).", src=TD3 + ", ex. 3", duree=3),
        v("hc4", r"Étape 2→3 : isochore de $T_1=300$ K à $T_c=600$ K, $c_v=\dfrac{nR}{0{,}4}$. Chaleur $Q_{23}$ (en J) ?", "Rational(4,100)*Rational(831,100)/Rational(4,10)*300", "2493/10",
          r"$W_{23}=0$, $Q_{23}=\Delta U=c_v(T_c-T_1)=\frac{0{,}3324}{0{,}4}\times300=249{,}3$ J.", src=TD3 + ", ex. 3", duree=4),
        v("hc5", r"Rendement du Stirling sans régénérateur : $\rho=\dfrac{\ln10}{\frac1{0{,}4}+\frac{T_c}{T_c-T_f}\ln10}$ avec $T_c=600$, $T_f=300$, $\ln10=2{,}3$. Valeur ?", "Rational(23,10)/(Rational(5,2)+2*Rational(23,10))", "23/71",
          r"$\rho=\dfrac{2{,}3}{2{,}5+2\times2{,}3}=\dfrac{2{,}3}{7{,}1}\approx0{,}32$ (bien inférieur à Carnot, $0{,}5$).", src=TD3 + ", ex. 3", duree=4),
        v("hc6", r"Lenoir : état 1 à $T_1=373$ K, $V_1=10$ L, $P_1=2\times10^5$ Pa. Détente isotherme 2→3 jusqu'à $V_3=2V_1$, puis isobare 3→1. Température $T_2=T_3$ (en K) ?", "2*373", "746",
          r"Isobare 3→1 : $\frac{V_3}{T_3}=\frac{V_1}{T_1}$ donc $T_3=2T_1=746$ K, et $T_2=T_3$.", src=TD2 + ", ex. 3", duree=4),
        o("hc7", r"Stirling avec régénérateur : justifier l'idée de Stirling, donner le rendement et dire s'il peut être amélioré sans changer les sources.",
          r"Le régénérateur stocke la chaleur cédée par le gaz en 4→1 et la rend au gaz en 2→3 : ces deux échanges se compensent, donc les sources n'échangent de chaleur que pendant les deux isothermes. Rendement : $\rho=1-\frac{T_f}{T_c}=\frac12$, celui de Carnot. On ne peut pas faire mieux avec ces deux sources, c'est le maximum du deuxième principe.", src=TD3 + ", ex. 3", duree=6),
    ]},
    {"n": 13, "titre": "Niveau examen : sujets complets", "notions": ["premier", "gp", "chaleur", "machines", "cycles"], "examen": True, "exos": [
        o("hx1", r"QCM de partiel : (1) définition de $H$ ; (2) $dH$ pour une transformation réversible ; (3) $Q$ d'un gaz parfait en isotherme ; (4) $W$ en isobare ; (5) $Q$ en isochore réversible ; (6) fonction non d'état ; (7) $T$ et $P$ en isochore ; (8) loi de Laplace en $T$ et $P$.",
          r"(1) $H=U+PV$. (2) $dH=dU+VdP$. (3) $Q=-W$ (car $\Delta U=0$). (4) $W=-P(V_2-V_1)$. (5) $Q=nc_v\Delta T$. (6) $Q$, la chaleur. (7) $T_1P_2=T_2P_1$. (8) $T^\gamma P^{1-\gamma}=$ cte.", src=P19 + ", QCM", duree=8),
        o("hx2", r"$P_1=1$ bar. (I) Compression isotherme réversible de $V_1$ à $\frac{V_1}{10}$, $W_{12}=420$ J, $R=8{,}3$, $\ln10=2{,}3$ : 1) $Q_{12}$ ; 2) $P_2$ ; 3) $V_1$ ; 4) la température si $n=0{,}02$ mol. (II) Compression adiabatique réversible de $1$ mol de gaz monoatomique, $\Delta T=100$ °C : $Q_{12}$, $W_{12}$, $P_2$.",
          r"(I) 1) $\Delta U=0$ donc $Q_{12}=-W_{12}=-420$ J. 2) $P_2=10P_1=10$ bar. 3) $W_{12}=P_1V_1\ln10$ donc $V_1=\frac{420}{10^5\times2{,}3}\approx1{,}8\times10^{-3}$ m³ $=1{,}8$ L. 4) $T=\frac{P_1V_1}{nR}=\frac{182{,}6}{0{,}02\times8{,}3}\approx1{,}1\times10^3$ K." "\n\n"
          r"(II) $Q_{12}=0$ (adiabatique). $W_{12}=\Delta U=\frac32nR\Delta T=1{,}5\times8{,}3\times100=1245$ J. $T^\gamma P^{1-\gamma}=$ cte donne $P_2=P_1\left(\frac{T_1+\Delta T}{T_1}\right)^{\gamma/(\gamma-1)}$ avec $\gamma=\frac53$.", src=P19 + ", ex. 1", duree=12),
        o("hx3", r"$1$ mol de gaz parfait ($c_v=\frac52R$, $c_p=\frac72R$) passe de $a(P_1,V_1)$ à $b(2P_1,2V_1)$ par $acb$ (isochore puis isobare), $adb$ (isobare puis isochore) et la droite $ab$. 1) $T_b$, $T_c$, $T_d$. 2) $W$ pour chaque chemin. 3) $Q$ pour chaque chemin. Conclure.",
          r"1) $T_b=\frac{2P_1\cdot2V_1}{R}=4T_1$ ; $c=(2P_1,V_1)$ et $d=(P_1,2V_1)$ donnent $T_c=T_d=2T_1$." "\n\n"
          r"2) $W_{acb}=-2P_1(2V_1-V_1)=-2RT_1$ ; $W_{adb}=-P_1V_1=-RT_1$ ; droite : $P=\frac{P_1}{V_1}V$, $W_{ab}=-\frac{P_1}{2V_1}(4V_1^2-V_1^2)=-\frac32RT_1$." "\n\n"
          r"3) $\Delta U=c_v(T_b-T_a)=\frac{15}2RT_1$. $Q_{acb}=\Delta U-W=\frac{19}2RT_1$ ; $Q_{adb}=\frac{17}2RT_1$ ; $Q_{ab}=9RT_1$." "\n\n"
          r"$\Delta U$ ne dépend pas du chemin ; $W$ et $Q$ si.", src=P19 + ", ex. 2", duree=15),
        o("hx4", r"$1$ mol de gaz parfait : $A(P_1,V_1,T_1)$, compression adiabatique réversible jusqu'à $V_B=\frac{V_1}4$, puis isochore jusqu'à $T_1$ (état $C$), puis détente isotherme réversible jusqu'à $A$. 1) Tracer le cycle. 2) Chaleur reçue. 3) Travail reçu sur l'adiabatique. 4) $P_C$, $P_B$, $T_B$.",
          r"1) $A\to B$ adiabatique raide, $B\to C$ verticale vers le bas, $C\to A$ hyperbole $PV=$ cte." "\n\n"
          r"2) La chaleur reçue est celle de l'isotherme $C\to A$ : $Q_{CA}=-W_{CA}=P_1V_1\ln4$." "\n\n"
          r"3) $W_{AB}=\Delta U=\frac{nR}{\gamma-1}(T_B-T_1)=\dfrac{P_1V_1}{\gamma-1}\left(4^{\gamma-1}-1\right)$." "\n\n"
          r"4) $P_C=\frac{P_1V_1}{V_1/4}=4P_1$ (isotherme). Laplace : $P_B=P_1\cdot4^\gamma$ et $T_B=T_1\cdot4^{\gamma-1}$.", src=P19 + ", ex. 3", duree=15),
        v("hx5", r"Calorimètre : $0{,}02$ kg de glace à $-20$ °C ($c=2000$ J·kg$^{-1}$·K$^{-1}$) et $0{,}1$ kg d'eau à $30$ °C ($c=4000$). Température finale $10$ °C. $\Delta H_{tot}=0$ avec $\Delta H_1=400$ J, $\Delta H_3=800-8000$ J. Enthalpie de fusion (en kJ·kg$^{-1}$) ?", "(8000-800-400)/Rational(20,1000)/1000", "340",
          r"$m_{gl}\Delta h=-\Delta H_1-\Delta H_3=-400+7200=6800$ J, donc $\Delta h=\frac{6800}{0{,}02}=340\,000$ J·kg$^{-1}=340$ kJ·kg$^{-1}$.", src=M30 + ", ex. 1", duree=6),
        o("hx6", r"Réfrigérateur entre $T_f=5$ °C et $T_c=25$ °C : schéma, signes de $Q_c$, $Q_f$, $W$, efficacité réversible, valeur et interprétation.",
          r"Frigo : $Q_f>0$ (prise à l'intérieur), $W>0$ (électricité), $Q_c<0$ (cédée à la cuisine). $W=-(Q_c+Q_f)$ et $e=\frac{Q_f}W=\frac1{-1-Q_c/Q_f}$ ; avec $S_{cr}=0$ : $e=\frac{T_f}{T_c-T_f}=\frac{278}{20}\approx14$." "\n\n"
          r"Pour $1$ J d'énergie électrique fourni, le frigo extrait $14$ J de l'intérieur (valeur maximale, idéale).", src=M30 + ", ex. 2", duree=10),
    ]},
    {"n": 14, "titre": "Examen + 20 %", "notions": ["cycles", "gp", "machines"], "examen": True, "exos": [
        v("hy1", r"Brayton (hélium, $\gamma=\frac53$) : $\rho=1-\left(\dfrac{P_A}{P_B}\right)^{(\gamma-1)/\gamma}$ avec $\dfrac{P_B}{P_A}=32$. Valeur de $\rho$ ?", "1-Rational(1)/32**Rational(2,5)", "3/4",
          r"$\frac{\gamma-1}\gamma=\frac25$ et $32^{2/5}=2^2=4$, donc $\rho=1-\frac14=\frac34$.", src=P21 + ", ex. 1", duree=5),
        o("hy2", r"Cycle de Brayton $A\to B$ adiabatique réversible, $B\to C$ isobare, $C\to D$ adiabatique réversible, $D\to A$ isobare. Établir $\rho=1-\dfrac{T_A}{T_B}=1-\left(\dfrac{P_A}{P_B}\right)^{\frac{\gamma-1}\gamma}$.",
          r"Adiabatiques : $T_B=T_A\left(\frac{P_B}{P_A}\right)^{\frac{\gamma-1}\gamma}$ et $T_C=T_D\left(\frac{P_B}{P_A}\right)^{\frac{\gamma-1}\gamma}$, donc $\frac{T_C}{T_D}=\frac{T_B}{T_A}$." "\n\n"
          r"Isobares : $Q_{BC}=C_p(T_C-T_B)$ et $Q_{DA}=C_p(T_A-T_D)$. $\rho=1+\frac{Q_{DA}}{Q_{BC}}=1-\frac{T_D-T_A}{T_C-T_B}$." "\n\n"
          r"Or $T_D-T_A=\frac{T_A}{T_B}(T_C-T_B)$, d'où $\rho=1-\frac{T_A}{T_B}$.", src=P21 + ", ex. 1", duree=12),
        o("hy3", r"Cycle de Carnot $A\to B$ isotherme à $T_c$, $B\to C$ adiabatique, $C\to D$ isotherme à $T_f$, $D\to A$ adiabatique. Montrer $\dfrac{V_B}{V_A}=\dfrac{V_C}{V_D}$ avec Laplace, puis $\rho=1-\dfrac{T_f}{T_c}$.",
          r"Laplace $TV^{\gamma-1}=$ cte : $T_cV_B^{\gamma-1}=T_fV_C^{\gamma-1}$ et $T_cV_A^{\gamma-1}=T_fV_D^{\gamma-1}$. En divisant : $\frac{V_B}{V_A}=\frac{V_C}{V_D}$." "\n\n"
          r"$Q_{AB}=nRT_c\ln\frac{V_B}{V_A}$ et $Q_{CD}=nRT_f\ln\frac{V_D}{V_C}=-nRT_f\ln\frac{V_B}{V_A}$. $\rho=1+\frac{Q_{CD}}{Q_{AB}}=1-\frac{T_f}{T_c}$.", src=P21 + ", ex. 2", duree=12),
        v("hy4", r"Lenoir ($P_1=2\times10^5$ Pa, $V_1=10$ L, $T_2=2T_1$, $V_3=2V_1$) : $W_{12}=0$, $W_{31}=+2000$ J et $W_{23}=-4000\ln2$. Travail total (en J) avec $\ln2\approx0{,}7$ ?", "2000*(1-2*Rational(7,10))", "-800",
          r"$W_{tot}=2000-4000\times0{,}7=-800$ J : le moteur fournit environ $800$ J par cycle (sens horaire).", src=TD2 + ", ex. 3", duree=8),
        o("hy5", r"Pourquoi aucune transformation réelle n'est-elle parfaitement adiabatique ou réversible ? Quelle conséquence sur le rendement d'un moteur réel ?",
          r"L'équilibre thermique finit toujours par s'établir : même une transformation rapide échange un peu de chaleur. Frottements, gradients de température et de pression créent de l'entropie : $S_{cr}>0$. Le rendement réel $\rho=1-\frac{T_f}{T_c}-\frac{T_fS_{cr}}{Q_c}$ est donc inférieur à celui de Carnot.", duree=6),
    ]},
]


def _v(enonce, calc, ans, sol):
    return {"enonce": enonce, "calc": calc, "ans": ans, "sol": sol}


# Numeric variants: a failed exercise comes back with other numbers; build.py checks calc == ans.
VARIANTS = {
    "he1": [_v(r"Convertir $-13$ °C en kelvin ($T=\theta+273$).", "-13+273", "260", r"$-13+273=260$ K.")],
    "he2": [_v(r"Gaz à volume constant : $2$ bar à $300$ K. Pression (en bar) à $450$ K ?", "2*450/300", "3", r"$P_2=2\times\frac{450}{300}=3$ bar.")],
    "he4": [_v(r"À $T$ constante, on multiplie le volume par $3$. Par combien est multipliée la pression ?", "Rational(1,3)", "1/3", r"$P_2=\frac{P_1}3$.")],
    "hu1": [_v(r"$100$ kg d'eau passent de $20$ à $70$ °C, $c_v=4{,}2$ kJ·kg$^{-1}$·K$^{-1}$. $\Delta U$ (en kJ) ?", "100*Rational(42,10)*50", "21000", r"$100\times4{,}2\times50=21\,000$ kJ.")],
    "hu3": [_v(r"$2$ mol de gaz parfait monoatomique chauffées de $50$ K. $\Delta U$ (en J) ? ($R=8{,}3$)", "Rational(3,2)*2*Rational(83,10)*50", "1245", r"$\frac32\times2\times8{,}3\times50=1245$ J.")],
    "hw2": [_v(r"Compression monobare à $2$ bar de $4$ L à $2$ L. Travail reçu (en J) ?", "-2*10**5*(Rational(2,1000)-Rational(4,1000))", "400", r"$W=-2\times10^5\times(-2\times10^{-3})=400$ J.")],
    "hw4": [_v(r"Compression isotherme réversible de $V_1=3$ L à $\frac{V_1}{10}$ avec $P_1=1$ bar ($\ln10=2{,}3$). $W$ (en J) ?", "10**5*Rational(3,1000)*Rational(23,10)", "690", r"$P_1V_1\ln10=300\times2{,}3=690$ J.")],
    "hq1": [_v(r"$2$ kg d'eau chauffés de $10$ à $60$ °C ($c=4200$). $Q$ (en J) ?", "2*4200*50", "420000", r"$2\times4200\times50=420\,000$ J.")],
    "hq2": [_v(r"On mélange $1$ kg d'eau à $90$ °C et $4$ kg à $10$ °C. Température finale (en °C) ?", "(90+4*10)/Rational(5)", "26", r"$T_F=\frac{90+40}5=26$ °C.")],
    "hh1": [_v(r"$2{,}0$ g de glace passent de $263$ K à $273$ K ($c_g=2100$ J·kg$^{-1}$·K$^{-1}$). $\Delta H_1$ (en J) ?", "Rational(2,1000)*2100*10", "42", r"$2\times10^{-3}\times2100\times10=42$ J.")],
    "hh3": [_v(r"$\Delta U=300$ J à $P=10^5$ Pa avec $\Delta V=3$ L. $\Delta H$ (en J) ?", "300+10**5*Rational(3,1000)", "600", r"$\Delta H=\Delta U+P\Delta V=300+300=600$ J.")],
    "hp1": [_v(r"Un système cède $50$ J de chaleur et reçoit $120$ J de travail. $\Delta U$ (en J) ?", "-50+120", "70", r"$\Delta U=-50+120=70$ J.")],
    "hp3": [_v(r"Isochore, $C_v=25$ J·K$^{-1}$, $\Delta T=8$ K. $Q$ (en J) ?", "25*8", "200", r"$Q=C_v\Delta T=200$ J.")],
    "hg2": [_v(r"$2$ mol ($C_v=\frac52nR$, $R=8{,}3$) chauffées à volume constant de $50$ K. $Q$ (en J) ?", "Rational(5,2)*2*Rational(83,10)*50", "2075", r"$2{,}5\times2\times8{,}3\times50=2075$ J.")],
    "ha2": [_v(r"Compression adiabatique réversible, $\gamma=\frac53$, volume divisé par $27$. Facteur sur la pression ?", "27**Rational(5,3)", "243", r"$27^{5/3}=3^5=243$.")],
    "ha3": [_v(r"Même compression ($\gamma=\frac53$, volume divisé par $27$) à partir de $T_1=300$ K. $T_2$ (en K) ?", "300*27**Rational(2,3)", "2700", r"$27^{2/3}=9$, donc $T_2=2700$ K.")],
    "hs1": [_v(r"Un système reçoit $900$ J d'un thermostat à $300$ K. $S_{ech}$ (en J·K$^{-1}$) ?", "900/300", "3", r"$\frac{900}{300}=3$ J·K$^{-1}$.")],
    "hm1": [_v(r"Moteur : $Q_c=800$ J, $Q_f=-500$ J. Rendement ?", "Rational(300,800)", "3/8", r"$W=-300$ J, $\rho=\frac{300}{800}=\frac38$.")],
    "hm2": [_v(r"Rendement maximal entre $T_c=800$ K et $T_f=300$ K ?", "1-Rational(300,800)", "5/8", r"$1-\frac{300}{800}=\frac58$.")],
    "hm5": [_v(r"Un frigo reçoit $50$ J d'électricité et prend $200$ J au froid. Efficacité ?", "200/Rational(50)", "4", r"$e=\frac{200}{50}=4$.")],
}
for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["id"] in VARIANTS:
            _e["variants"] = VARIANTS[_e["id"]]


EXTRA_PARTS = []

QUIZ = [
    {"notion": "etat", "type": "qcm", "q": r"Parmi ces grandeurs, laquelle est extensive ?", "choix": [r"le volume", r"la pression", r"la température", r"la masse volumique"], "bonne": 0},
    {"notion": "etat", "type": "vf", "q": r"Dans $PV=nRT$, la température doit être exprimée en kelvin.", "bonne": True},
    {"notion": "energie_interne", "type": "vf", "q": r"Sur un cycle, la variation d'énergie interne est nulle.", "bonne": True},
    {"notion": "energie_interne", "type": "qcm", "q": r"Pour une phase condensée, $\Delta U$ vaut :", "choix": [r"$mc_v\Delta T$", r"$mc_v T$", r"$PV$", r"$Q+W$ seulement si adiabatique"], "bonne": 0},
    {"notion": "travail", "type": "qcm", "q": r"Le travail d'une transformation isochore vaut :", "choix": [r"$0$", r"$-P\Delta V$", r"$nRT\ln\frac{V_f}{V_i}$", r"$\Delta U$"], "bonne": 0},
    {"notion": "travail", "type": "vf", "q": r"Le travail reçu par un gaz que l'on comprime est positif.", "bonne": True},
    {"notion": "chaleur", "type": "qcm", "q": r"Pendant la fusion de la glace à $0$ °C sous pression constante :", "choix": [r"$T$ reste constante", r"$T$ augmente", r"$Q=0$", r"$\Delta H=0$"], "bonne": 0},
    {"notion": "chaleur", "type": "vf", "q": r"Dans un calorimètre isolé, la somme des chaleurs échangées est nulle.", "bonne": True},
    {"notion": "premier", "type": "qcm", "q": r"Pour un gaz parfait en transformation isotherme :", "choix": [r"$Q=-W$", r"$Q=W$", r"$Q=0$", r"$W=0$"], "bonne": 0},
    {"notion": "premier", "type": "qcm", "q": r"Laquelle de ces grandeurs n'est pas une fonction d'état ?", "choix": [r"la chaleur $Q$", r"l'enthalpie $H$", r"l'énergie interne $U$", r"la température $T$"], "bonne": 0},
    {"notion": "premier", "type": "qcm", "q": r"À pression constante, la chaleur reçue vaut :", "choix": [r"$\Delta H$", r"$\Delta U$", r"$-P\Delta V$", r"$0$"], "bonne": 0},
    {"notion": "gp", "type": "qcm", "q": r"La relation de Mayer pour un gaz parfait est :", "choix": [r"$C_p-C_v=nR$", r"$C_p+C_v=nR$", r"$C_pC_v=nR$", r"$C_p=C_v$"], "bonne": 0},
    {"notion": "gp", "type": "qcm", "q": r"Pour une adiabatique réversible d'un gaz parfait :", "choix": [r"$PV^\gamma=$ cte", r"$PV=$ cte", r"$P/V=$ cte", r"$P^\gamma V=$ cte"], "bonne": 0},
    {"notion": "gp", "type": "vf", "q": r"Pour une transformation adiabatique, le travail est égal à la variation d'énergie interne.", "bonne": True},
    {"notion": "diagrammes", "type": "qcm", "q": r"Au-delà du point critique, on a :", "choix": [r"un fluide supercritique", r"un solide", r"un mélange liquide-gaz", r"un gaz parfait"], "bonne": 0},
    {"notion": "diagrammes", "type": "vf", "q": r"Pour l'eau, la courbe de fusion du diagramme $(P,T)$ a une pente négative.", "bonne": True},
    {"notion": "entropie", "type": "qcm", "q": r"Pour une transformation réversible :", "choix": [r"$S_{cr}=0$", r"$S_{cr}>0$", r"$S_{cr}<0$", r"$S_{ech}=0$"], "bonne": 0},
    {"notion": "entropie", "type": "vf", "q": r"L'entropie créée peut être négative pour une transformation spontanée.", "bonne": False},
    {"notion": "machines", "type": "qcm", "q": r"Rendement maximal d'un moteur ditherme :", "choix": [r"$1-\dfrac{T_f}{T_c}$", r"$1-\dfrac{T_c}{T_f}$", r"$\dfrac{T_f}{T_c}$", r"$\dfrac{T_c}{T_c-T_f}$"], "bonne": 0},
    {"notion": "machines", "type": "vf", "q": r"L'efficacité d'une machine frigorifique peut dépasser $1$.", "bonne": True},
    {"notion": "machines", "type": "qcm", "q": r"Pour un moteur, les signes de $W$ et $Q_c$ sont :", "choix": [r"$W<0$ et $Q_c>0$", r"$W>0$ et $Q_c>0$", r"$W<0$ et $Q_c<0$", r"$W>0$ et $Q_c<0$"], "bonne": 0},
    {"notion": "cycles", "type": "qcm", "q": r"Le cycle de Carnot comprend :", "choix": [r"deux isothermes et deux adiabatiques", r"deux isobares et deux isochores", r"deux isothermes et deux isochores", r"deux isobares et deux adiabatiques"], "bonne": 0},
    {"notion": "cycles", "type": "vf", "q": r"Un cycle parcouru dans le sens horaire du diagramme $(P,V)$ est moteur.", "bonne": True},
]

_PV = r"$PV=nRT$ · $T(\mathrm K)=\theta+273$"
_ISO = r"$\frac{P_1}{T_1}=\frac{P_2}{T_2}$ (isochore)"
_U = r"$\Delta U=C_v\Delta T=mc_v\Delta T$"
_W = r"$W=-\int P_{ext}\,dV$ (reçu $>0$)"
_WM = r"monobare : $W=-P_0(V_f-V_i)$"
_WT = r"isotherme réversible : $W=nRT\ln\frac{V_i}{V_f}=P_1V_1\ln\frac{V_i}{V_f}$"
_Q = r"$Q=mc\Delta T$"
_QF = r"fusion : $Q=m\Delta h_{fus}$ à $T$ constante"
_CAL = r"calorimètre isolé : $\sum Q=0$"
_P1 = r"$\Delta U=Q+W$"
_H = r"$H=U+PV$ · $dH=C_pdT$ · $Q=\Delta H$ à $P$ constante"
_MAY = r"Mayer : $C_p-C_v=nR$ · $\gamma=\frac{C_p}{C_v}$ · $C_v=\frac32nR$ (monoatomique), $\frac52nR$ (diatomique)"
_LAP = r"Laplace : $PV^\gamma=$ cte · $TV^{\gamma-1}=$ cte · $T^\gamma P^{1-\gamma}=$ cte"
_ADI = r"adiabatique : $Q=0$, $W=\Delta U$"
_S = r"$\Delta S=\frac QT+S_{cr}$, $S_{cr}\geq0$"
_MOT = r"moteur : $\rho=-\frac W{Q_c}=1+\frac{Q_f}{Q_c}\leq1-\frac{T_f}{T_c}$"
_FRI = r"frigo : $e=\frac{Q_f}W\leq\frac{T_f}{T_c-T_f}$"
_PAC = r"PAC : $\mathrm{COP}=-\frac{Q_c}W\leq\frac{T_c}{T_c-T_f}$"
_CYC = r"cycle : $\Delta U=0$, $W=-\sum Q$ · $Q_c+Q_f+W=0$"
_CAR = r"Carnot : $\rho=1-\frac{T_f}{T_c}$"
_PH = r"isobare $P$, isotherme $T$, isochore $V$ constants · adiabatique $Q=0$"

FORMULES = {
    "he1": r"$T(\mathrm K)=\theta(^\circ\mathrm C)+273$", "he2": _PV + " · " + _ISO, "he3": _PV + r" · $V=\frac{nRT}P$", "he4": _PV + r" · $T$ constante : $P_1V_1=P_2V_2$",
    "he5": r"intensives : $T$, $P$ · extensives : $V$, $n$, $m$, $U$",
    "hu1": _U, "hu2": r"1 kWh $=3600$ kJ", "hu3": _U + r" · $C_v=\frac32nR$", "hu4": _U, "hu5": r"$U$ fonction d'état · cycle : $\Delta U=0$",
    "hw1": _W, "hw2": _W + " · " + _WM, "hw3": _W + " · " + _WM, "hw4": _WT, "hw5": _W + r" · $P=\frac{nRT}V$ · $\int\frac{dV}V=\ln V$",
    "hq1": _Q, "hq2": _Q + " · " + _CAL, "hq3": _QF, "hq4": _Q, "hq5": _Q + " · " + _QF + " · " + _CAL, "hq6": r"conduction · convection · rayonnement",
    "hh1": _Q + r" · $\Delta H=mc\Delta T$", "hh2": _Q + " · " + _QF + r" · $\Delta H=\Delta H_1+\Delta H_2+\Delta H_3$", "hh3": _H, "hh4": _Q + " · " + _QF + " · " + _CAL, "hh5": _QF,
    "hp1": _P1, "hp2": _CYC, "hp3": _P1 + r" · isochore : $Q=\Delta U=C_v\Delta T$", "hp4": _H + r" · $\Delta H=C_p\Delta T$", "hp5": _P1 + r" · $P_{ext}=0\Rightarrow W=0$",
    "hg1": _MAY, "hg2": _MAY + r" · isochore : $Q=\Delta U$", "hg3": _MAY + r" · isobare : $Q=\Delta H=C_p\Delta T$", "hg4": _P1 + r" · isotherme (gaz parfait) : $\Delta U=0$",
    "hg5": _W + " · " + _WM + " · " + _P1 + r" · $P_1V_1=P_2V_2\Rightarrow\Delta U=0$", "hg6": _W + " · " + _WM + " · " + _P1, "hg7": _WT + " · " + _P1,
    "ha1": _ADI + r" · $C_v=\frac32nR$", "ha2": _LAP, "ha3": _LAP, "ha4": r"$W=\frac{P_2V_2-P_1V_1}{\gamma-1}$ · " + _ADI, "ha5": _LAP + r" · $PV=nRT$",
    "hd1": _PH + r" · monobare : $P_{ext}$ constante · réversible : succession d'états d'équilibre", "hd2": r"courbe d'ébullition · courbe de rosée · palier d'Andrews · point critique",
    "hd3": r"point triple · point critique · eau : fusion de pente négative", "hd4": r"palier : $P=P_{sat}(T)$ · diagramme de Clapeyron $(P,v)$",
    "hs1": r"$S_{ech}=\frac QT$", "hs2": _QF + r" · $\Delta S=\frac QT$", "hs3": _S, "hs4": _S + r" · $Q=0$", "hs5": _S + r" · isentropique : $\Delta S=0$",
    "hm1": _CYC + " · " + _MOT, "hm2": _MOT, "hm3": _FRI, "hm4": _PAC, "hm5": _FRI.replace(r"\leq\frac{T_f}{T_c-T_f}", ""),
    "hm6": _P1 + " · " + _S + r" · cycle monotherme", "hm7": _CYC + " · " + _S + " · " + _PAC,
    "hc1": _PV, "hc2": _WT.split(" : ")[0] + r" : $P_1V_1=P_2V_2$ · " + _PV, "hc3": _WT, "hc4": _P1 + r" · isochore : $Q=\Delta U=C_v\Delta T$", "hc5": _CYC + r" · $\rho=-\frac W{Q_{reçu}}$",
    "hc6": r"isobare : $\frac VT=$ cte · " + _PV, "hc7": _CAR + " · " + _CYC,
    "hx1": _H + r" · $dH=dU+VdP$ · " + _LAP, "hx2": _WT + " · " + _ADI + " · " + _LAP, "hx3": _W + " · " + _U + " · " + _P1 + r" · $C_p-C_v=R$",
    "hx4": _LAP + " · " + _WT + " · " + _ADI, "hx5": _Q + " · " + _QF + " · " + _CAL, "hx6": _FRI + " · " + _S,
    "hy1": r"Brayton : $\rho=1-\left(\frac{P_A}{P_B}\right)^{\frac{\gamma-1}\gamma}$ · " + _LAP, "hy2": _LAP + r" · isobare : $Q=C_p\Delta T$ · " + _MOT, "hy3": _LAP + " · " + _WT + " · " + _CAR,
    "hy4": _W + " · " + _WM + " · " + _WT, "hy5": _S + " · " + _MOT,
}
