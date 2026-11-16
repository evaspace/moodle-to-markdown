"""Level path: S2 electronics, transient modes of RC and RL circuits, promo 2031.

Calibrated on the Moodle course « Electronique S2 - Études des régimes transitoires » (`Kit de Survie - Régimes
transitoires`), the TD « Les régimes transitoires » (4 exercises + optional spark exercise, with its correction) and the
February 2023 test (`Contrôle Elec - InfoS2 - Février 2023`, handwritten correction). No exam of promo 2030 is published.
Circuits are described in words and drawn as SVG
(`schema.py`, `FIGS` at the end). In `calc`, the source voltage is the symbol V
(E is Euler's number in build.NS) and t is time; s(t) = beta + (s0 - beta) exp(-t/tau) is the worked solution.
"""
from .schema import Fil, Gap, Point, R, SrcI, SrcU, ajoute, courant, fig, schema_echelle, tension


SUBJECT = {
    "id": "elec-s2-transitoires",
    "ordre": 530,
    "matiere": "electronique",
    "semestre": "S2",
    "ecue": "Études des régimes transitoires",
    "titre": "Régimes transitoires (circuits RC et RL)",
    "chapitres_moodle": ["Electronique S2 - Études des régimes transitoires [2526_I_INF_FISE_S02_CN_ERT]/01_Documents de cours",
                         "Electronique S2 - Études des régimes transitoires [2526_I_INF_FISE_S02_CN_ERT]/02_Travaux Dirigés"],
    "td": "TD « Les régimes transitoires » (4 exercices, étincelle de rupture)",
    "examens": ["Contrôle d'électronique S2 (février 2023)"],
}

NOTIONS = [
    {"id": "composants", "titre": "Condensateur et bobine : relations et continuité",
     "formule": r"$i=C\dfrac{du}{dt}$ · $u=L\dfrac{di}{dt}$ · continuité de la tension aux bornes d'un condensateur : $u_C(0^+)=u_C(0^-)$ · continuité du courant dans une bobine : $i_L(0^+)=i_L(0^-)$ · $C$ en farads (F), $L$ en henrys (H)",
     "exemple": r"condensateur initialement déchargé : $u_C(0^+)=0$ juste après la fermeture",
     "cours": r"La tension aux bornes d'un condensateur ne peut pas varier brutalement (le courant serait infini) ; de même le courant dans une bobine. Ces continuités donnent l'état du circuit juste après un changement ($t=0^+$, fermeture ou ouverture d'un interrupteur)."},
    {"id": "permanent", "titre": "Régime permanent continu",
     "formule": r"$t\to\infty$ : grandeurs constantes, $\dfrac{du}{dt}=0$, $\dfrac{di}{dt}=0$ · condensateur $=$ interrupteur ouvert ($i=0$) · bobine $=$ fil ($u=0$)",
     "exemple": r"$E$, $R$, $C$ en série : $u_C(\infty)=E$, $i(\infty)=0$",
     "cours": r"Une fois le régime permanent atteint, le circuit ne contient plus que des résistances et des sources : on calcule les valeurs finales avec les lois du continu (diviseurs, mailles). La tension aux bornes d'un interrupteur ouvert n'est en général pas nulle."},
    {"id": "initial", "titre": "Conditions initiales à $t=0^+$",
     "formule": r"à $t=0^+$ : condensateur déchargé $\to$ fil ($u_C=0$), chargé sous $U_0$ $\to$ source $U_0$ · bobine sans courant $\to$ interrupteur ouvert ($i_L=0$) · puis lois de Kirchhoff",
     "exemple": r"$E$, $R$, puis $R\parallel L$ : à $0^+$, $i_L=0$, $i=i_R=\dfrac E{2R}$, $u_L=\dfrac E2$",
     "cours": r"On commence par les grandeurs continues (tension du condensateur, courant de la bobine), puis on remplace le composant par son équivalent à cet instant seulement, et on calcule les autres grandeurs, qui elles peuvent sauter."},
    {"id": "equadiff", "titre": "Équation différentielle du premier ordre",
     "formule": r"$\dfrac{ds}{dt}+\dfrac1\tau s=A$ · RC : $\dfrac{du_C}{dt}+\dfrac{1}{RC}u_C=\dfrac{E}{RC}$ · RL : $\dfrac{di}{dt}+\dfrac RL i=\dfrac EL$ · $\tau$ : coefficient de $s$ quand celui de $\dfrac{ds}{dt}$ vaut $1$",
     "exemple": r"$\dfrac{di_2}{dt}+\dfrac{2}{3RC}i_2=0$ : $\tau=\dfrac{3RC}2$",
     "cours": r"La loi des mailles et la relation courant/tension du composant donnent une équation différentielle linéaire du premier ordre à coefficients constants. On la met sous forme normalisée (coefficient $1$ devant la dérivée) pour lire $\tau$."},
    {"id": "resolution", "titre": "Résolution : $s(t)=\\alpha e^{-t/\\tau}+\\beta$",
     "formule": r"$s(t)=\alpha\,e^{-t/\tau}+\beta$ · $\beta=s(\infty)$ : solution particulière (régime permanent) · $\alpha=s(0^+)-s(\infty)$ · donc $s(t)=s(\infty)+\big(s(0^+)-s(\infty)\big)e^{-t/\tau}$",
     "exemple": r"$u_C(0^+)=U_0$, $u_C(\infty)=E$ : $u_C(t)=E+(U_0-E)e^{-t/RC}$",
     "cours": r"Sans second membre, la solution est $\alpha e^{-t/\tau}$ (séparation des variables puis exponentielle). Avec un second membre constant, on ajoute une solution particulière constante, la valeur finale. La constante $\alpha$ vient de la condition initiale."},
    {"id": "tau", "titre": "Constante de temps",
     "formule": r"RC : $\tau=RC$ · RL : $\tau=\dfrac LR$ · tangente à l'origine : coupe l'asymptote en $t=\tau$ · $s(\tau)$ : $63\,\%$ du chemin · régime permanent atteint à $5\tau$ (écart $< 1\,\%$)",
     "exemple": r"$R=1$ kΩ, $C=1\,\mu$F : $\tau=1$ ms, permanent après $5$ ms",
     "cours": r"La constante de temps mesure la durée du régime transitoire. Après $\tau$, le signal a parcouru $1-e^{-1}\approx63\,\%$ de l'écart entre sa valeur initiale et sa valeur finale ; après $5\tau$, l'écart restant est inférieur à $1\,\%$."},
    {"id": "thevenin_t", "titre": "Se ramener à un circuit RC ou RL",
     "formule": r"Thévenin/Norton sur la partie résistive : $E_{th}$ (tension à vide), $R_{th}$ (sources éteintes) · puis $\tau=R_{th}C$ ou $\tau=\dfrac{L}{R_{th}}$ · $s(\infty)$ calculée avec $E_{th}$",
     "exemple": r"$E$, $R$, puis $R/2$ en parallèle avec $C$ : $E_{th}=\dfrac E3$, $R_{th}=\dfrac R3$, $\tau=\dfrac{RC}3$",
     "cours": r"Vu du condensateur ou de la bobine, le reste du circuit (sources et résistances) équivaut à un générateur de Thévenin. On retrouve le circuit RC ou RL série du cours, avec $R_{th}$ et $E_{th}$."},
    {"id": "millman_t", "titre": "Rappel : théorème de Millman",
     "formule": r"$V_A=\dfrac{\sum E_i/R_i+\sum\eta_i}{\sum1/R_i}$ (vient de la loi des nœuds)",
     "exemple": r"$(2E,R)$, $(-E,2R)$, $R$ et source $I$ entrant en $A$ : $U=\dfrac{3E+2RI}{5}$",
     "cours": r"Le théorème de Millman, vu en S1, revient au contrôle de S2 : il donne le potentiel d'un nœud relié à la masse par des branches en parallèle."},
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


X23 = "Contrôle d'électronique S2, février 2023"
TD = "TD d'électronique S2 « Les régimes transitoires »"
KIT = "Kit de survie « Les régimes transitoires »"

LEVELS = [
    {"n": 1, "titre": "Condensateur et bobine", "notions": ["composants"], "exos": [
        v("t11", r"Condensateur $C=2\,\mu$F, $\dfrac{du}{dt}=500$ V/s. Courant (en mA) ?", "2*500/1000", "1", r"$i=C\dfrac{du}{dt}=2\times10^{-6}\times500=10^{-3}$ A.", src=KIT, duree=2),
        v("t12", r"Bobine $L=50$ mH, $\dfrac{di}{dt}=100$ A/s. Tension (en V) ?", "Rational(50,1000)*100", "5", r"$u=L\dfrac{di}{dt}=5$ V.", src=KIT, duree=2),
        v("t13", r"Condensateur chargé sous $6$ V juste avant la fermeture d'un interrupteur. $u_C(0^+)$ (en V) ?", "6", "6", r"Continuité de la tension aux bornes d'un condensateur : $u_C(0^+)=u_C(0^-)=6$ V.", src=KIT, duree=1),
        v("t14", r"Bobine traversée par $2$ A juste avant l'ouverture d'un interrupteur. $i_L(0^+)$ (en A) ?", "2", "2", r"Continuité du courant dans une bobine : $2$ A.", src=KIT, duree=1),
        o("t15", r"Unités de la capacité $C$ et de l'inductance $L$ ?", r"$C$ en farads (F), $L$ en henrys (H).", src=X23 + ", Q2-Q3", duree=1),
        o("t16", r"Pourquoi la tension aux bornes d'un condensateur ne peut-elle pas varier brutalement ?",
          r"$i=C\dfrac{du}{dt}$ : un saut de tension demanderait une dérivée infinie, donc un courant infini, impossible dans un circuit réel. Même raisonnement pour le courant dans une bobine avec $u=L\dfrac{di}{dt}$.", src=KIT, duree=3),
        v("t17", r"Bobine sans courant avant la fermeture. $i_L(0^+)$ (en A) ?", "0", "0", r"Continuité : $i_L(0^+)=i_L(0^-)=0$ ; à cet instant la bobine se comporte comme un interrupteur ouvert.", src=TD + ", ex. 2", duree=1),
    ]},
    {"n": 2, "titre": "Régime permanent continu", "notions": ["permanent", "composants"], "exos": [
        o("t21", r"En régime permanent continu, par quoi remplace-t-on un condensateur ? une bobine ?",
          r"Condensateur : interrupteur ouvert ($i=C\,du/dt=0$). Bobine : fil ($u=L\,di/dt=0$).", src=X23 + ", Q4", duree=2),
        v("t22", r"$E=10$ V, $R$ et $C$ en série, interrupteur fermé depuis longtemps. $u_C(\infty)$ (en V) ?", "10", "10", r"$i=0$, pas de tension sur $R$ : $u_C=E=10$ V.", src=TD + ", ex. 1", duree=1),
        v("t23", r"$E=12$ V, $R=4$ Ω et $L$ en série, régime permanent. Courant (en A) ?", "12/4", "3", r"Bobine $=$ fil : $i=E/R=3$ A, $u_L=0$.", src=TD + ", ex. 2", duree=1),
        v("t24", r"$E$, $R$ en série, puis $R$ en parallèle avec ($R$ en série avec $C$). $E=12$ V. $u_C(\infty)$ (en V) ?", "12*1/(1+1)", "6", r"Aucun courant dans la branche de $C$ : diviseur $\dfrac{R}{R+R}E=6$ V, et $u_C=u$.", src=TD + ", ex. 3", duree=3),
        v("t25", r"$E=10$ V, $R$ en série, puis $R$ et $L$ en parallèle. $u_L(\infty)$ (en V) ?", "0", "0", r"Bobine $=$ fil : $u_L=0$ (et tout le courant $E/R$ passe dans $L$).", src=X23 + ", ex. 2", duree=2),
        v("t26", r"Même circuit, $R=5$ Ω : $i_L(\infty)$ (en A) ?", "10/5", "2", r"La bobine court-circuite la résistance de droite : $i=i_L=E/R=2$ A.", src=X23 + ", ex. 2", duree=2),
        v("t27", r"$E$, $R$, $C$ en série. Courant final (en A) ?", "0", "0", r"Condensateur $=$ interrupteur ouvert : $i(\infty)=0$.", src=TD + ", ex. 1", duree=1),
    ]},
    {"n": 3, "titre": "Conditions initiales", "notions": ["initial", "permanent"], "exos": [
        v("t31", r"Contrôle 2023, ex. 2 : $E$, $K$, $R$ en série, puis $R$ et $L$ en parallèle, courants nuls avant. $u_L(0^+)$ en fonction de $E$ ($E=10$ V) ?", "10*1/(1+1)", "5", r"$i_L(0^+)=0$ : la bobine est ouverte, diviseur $R$, $R$ : $u_L=\dfrac E2=5$ V.", src=X23 + ", ex. 2", duree=3),
        v("t32", r"Même circuit, $R=1$ kΩ : $i(0^+)$ (en mA) ?", "10/(2*1)", "5", r"$i=i_R=\dfrac E{2R}=5$ mA.", src=X23 + ", ex. 2", duree=2),
        v("t33", r"TD ex. 3 : $E$, $K$, $R$ en série, puis $(R$ en série avec $C)$ et $R$ en parallèle ; $C$ déchargé. $E=9$ V : $u(0^+)$ (en V) ?", "9*Rational(1,2)/(Rational(1,2)+1)", "3", r"$u_C(0^+)=0$ : $C$ est un fil, les deux $R$ sont en parallèle ($R/2$), diviseur : $u=\dfrac{R/2}{R/2+R}E=\dfrac E3=3$ V.", src=TD + ", ex. 3", duree=3),
        v("t34", r"Même circuit, $R=1$ kΩ : $i_1(0^+)$ (en mA) ?", "2*9/(3*1)", "6", r"$i_2=i_3=\dfrac{u}{R}=\dfrac E{3R}$, $i_1=\dfrac{2E}{3R}=6$ mA.", src=TD + ", ex. 3", duree=3),
        v("t35", r"$E=10$ V, $R$, $C$ en série, $C$ déchargé. $i(0^+)$ avec $R=2$ kΩ (en mA) ?", "10/2", "5", r"$u_C(0^+)=0$ : toute la tension est sur $R$, $i=\dfrac ER=5$ mA.", src=TD + ", ex. 1", duree=2),
        v("t36", r"$E=10$ V, $R=2$ kΩ, $C$ chargé sous $U_0=4$ V. $i(0^+)$ (en mA) ?", "(10-4)/2", "3", r"$i(0^+)=\dfrac{E-U_0}{R}=3$ mA.", src=TD + ", ex. 1.2", duree=2),
        o("t37", r"Contrôle 2023, ex. 2 : remplir le tableau $i$, $i_R$, $i_L$, $u_L$ à $t=0^+$ et $t\to\infty$.",
          r"$t=0^+$ : $i=\dfrac E{2R}$, $i_R=\dfrac E{2R}$, $i_L=0$, $u_L=\dfrac E2$. $t\to\infty$ : $i=\dfrac ER$, $i_R=0$, $i_L=\dfrac ER$, $u_L=0$.", src=X23 + ", ex. 2", duree=6),
    ]},
    {"n": 4, "titre": "Équation différentielle", "notions": ["equadiff", "composants"], "exos": [
        v("t41", r"$E$, $R$, $C$ en série : $\dfrac{du_C}{dt}+\dfrac1{RC}u_C=\dfrac E{RC}$. Constante de temps avec $R=10$ kΩ, $C=100$ nF (en ms) ?", "10*1000*Rational(100,10**9)*1000", "1", r"$\tau=RC=10^4\times10^{-7}=10^{-3}$ s.", src=TD + ", ex. 1", duree=2),
        v("t42", r"$E$, $R$, $L$ en série : $\dfrac{di}{dt}+\dfrac RLi=\dfrac EL$. $\tau$ avec $L=20$ mH, $R=10$ Ω (en ms) ?", "Rational(20,1000)/10*1000", "2", r"$\tau=\dfrac LR=2$ ms.", src=TD + ", ex. 2", duree=2),
        v("t43", r"$\dfrac{di_2}{dt}+\dfrac{2}{3RC}i_2=0$. $\tau$ avec $R=2$ kΩ, $C=1\,\mu$F (en ms) ?", "3*2000*Rational(1,10**6)/2*1000", "3", r"$\tau=\dfrac{3RC}2=3$ ms.", src=TD + ", ex. 3", duree=2),
        v("t44", r"$3\dfrac{ds}{dt}+6s=12$. Constante de temps (en s) ?", "Rational(3,6)", "Rational(1,2)", r"On divise par $3$ : $\dfrac{ds}{dt}+2s=4$, $\dfrac1\tau=2$, $\tau=0{,}5$ s.", duree=2),
        v("t45", r"Même équation : valeur finale $s(\infty)$ ?", "12/6", "2", r"En régime permanent $\dfrac{ds}{dt}=0$ : $6s=12$, $s=2$.", duree=2),
        o("t46", r"Établir l'équation différentielle de $u_C$ pour $E$, $R$, $C$ en série.",
          r"Mailles : $E=Ri+u_C$. Condensateur : $i=C\dfrac{du_C}{dt}$. D'où $RC\dfrac{du_C}{dt}+u_C=E$, soit $\dfrac{du_C}{dt}+\dfrac1{RC}u_C=\dfrac E{RC}$.", src=TD + ", ex. 1", duree=4),
        o("t47", r"Établir l'équation différentielle de $i$ pour $E$, $R$, $L$ en série.",
          r"Mailles : $E=Ri+u_L$ avec $u_L=L\dfrac{di}{dt}$. D'où $\dfrac{di}{dt}+\dfrac RLi=\dfrac EL$.", src=TD + ", ex. 2", duree=4),
    ]},
    {"n": 5, "titre": "Résolution", "notions": ["resolution", "equadiff"], "exos": [
        v("t51", r"$s(0^+)=0$, $s(\infty)=10$, $\tau=1$ ms. $s(t)$ avec $t$ en ms ?", "10+(0-10)*exp(-t/1)", "10*(1-exp(-t))", r"$s(t)=s(\infty)+(s(0^+)-s(\infty))e^{-t/\tau}=10(1-e^{-t})$.", duree=3),
        v("t52", r"$s(0^+)=5$, $s(\infty)=0$, $\tau=2$ ms. $s(t)$ avec $t$ en ms ?", "0+(5-0)*exp(-t/2)", "5*exp(-t/2)", r"Décroissance libre : $s(t)=5e^{-t/2}$.", duree=2),
        v("t53", r"$s(0^+)=2$, $s(\infty)=8$, $\tau=1$ s. $\alpha$ dans $s=\alpha e^{-t/\tau}+\beta$ ?", "2-8", "-6", r"$\beta=s(\infty)=8$, $\alpha=s(0^+)-\beta=-6$.", duree=2),
        v("t54", r"Vérifier : $u(t)=V(1-e^{-t/\tau})$ dans $\dfrac{du}{dt}+\dfrac u\tau$. Valeur (en fonction de $V$, $\tau$) ?", "diff(V*(1-exp(-t/tau)), t) + V*(1-exp(-t/tau))/tau", "V/tau", r"$\dfrac{V}{\tau}e^{-t/\tau}+\dfrac V\tau-\dfrac V\tau e^{-t/\tau}=\dfrac V\tau$ : c'est bien $\dfrac{E}{RC}$ avec $\tau=RC$, $V=E$.", duree=3),
        o("t55", r"Résoudre $\dfrac{du}{dt}+\dfrac1\tau u=0$ par séparation des variables.",
          r"$\dfrac{du}{u}=-\dfrac{dt}\tau$, on primitive : $\ln u=-\dfrac t\tau+c$, puis $u=e^{c}e^{-t/\tau}=\alpha e^{-t/\tau}$.", src=TD + ", ex. 1", duree=4),
        o("t56", r"Pourquoi la solution particulière est-elle une constante, et que représente-t-elle ?",
          r"Les coefficients et le second membre sont constants : une constante $\beta$ convient ($\dfrac{d\beta}{dt}=0$ donne $\beta=A\tau$). C'est la valeur du signal en régime permanent.", src=KIT, duree=3),
        v("t57", r"$E=10$ V, $U_0=4$ V, $RC=1$ ms. $u_C(t)$ avec $t$ en ms ?", "10+(4-10)*exp(-t)", "10-6*exp(-t)", r"$u_C(t)=E+(U_0-E)e^{-t/RC}=10-6e^{-t}$.", src=TD + ", ex. 1.2", duree=3),
    ]},
    {"n": 6, "titre": "Charge d'un condensateur", "notions": ["resolution", "tau"], "exos": [
        v("t61", r"Charge RC, $E=10$ V, $C$ déchargé. $u_C(\tau)$ (en V, exact) ?", "10*(1-exp(-1))", "10-10*exp(-1)", r"$u_C(\tau)=E(1-e^{-1})\approx6{,}3$ V.", src=TD + ", ex. 4", duree=2),
        v("t62", r"Même charge : courant $i(t)$ en mA, $R=1$ kΩ, $RC=1$ ms, $t$ en ms ?", "1*diff(10*(1-exp(-t)), t)", "10*exp(-t)", r"$i=C\dfrac{du_C}{dt}=\dfrac ER e^{-t/RC}=10e^{-t}$ mA.", src=TD + ", ex. 1", duree=3),
        v("t63", r"Charge RC : $u_C(5\tau)/E$ (exact) ?", "1-exp(-5)", "1-exp(-5)", r"$1-e^{-5}\approx0{,}993$ : écart inférieur à $1\,\%$.", src=TD + ", ex. 4", duree=2),
        v("t64", r"$E=10$ V, $R=2$ kΩ, $U_0=4$ V. Courant initial (en mA) ?", "(10-4)/2", "3", r"$i(t)=\dfrac{E-U_0}{R}e^{-t/RC}$ : $3$ mA à $t=0^+$.", src=TD + ", ex. 1.2", duree=2),
        o("t65", r"Allure de $u_C(t)$ et de $i(t)$ pour la charge d'un condensateur initialement déchargé.",
          r"$u_C$ part de $0$ (continuité), croît et tend vers $E$ ; la tangente à l'origine coupe $E$ en $t=\tau$. $i$ saute à $\dfrac ER$ à $0^+$ puis décroît exponentiellement vers $0$.", src=TD + ", ex. 1", duree=4),
        v("t66", r"Même charge, combien de temps (en ms) avant de considérer le régime permanent atteint si $RC=2$ ms ?", "5*2", "10", r"$5\tau=10$ ms.", src=KIT, duree=1),
        v("t67", r"Pente à l'origine de $u_C(t)=E(1-e^{-t/\tau})$ (en fonction de $V=E$ et $\tau$) ?", "diff(V*(1-exp(-t/tau)), t).subs(t, 0)", "V/tau", r"$\dfrac{du_C}{dt}(0)=\dfrac E\tau$ : la tangente atteint $E$ en $t=\tau$.", src=TD + ", ex. 1", duree=3),
    ]},
    {"n": 7, "titre": "Établissement du courant dans une bobine", "notions": ["resolution", "equadiff"], "exos": [
        v("t71", r"$E=12$ V, $R=6$ Ω, $L$ en série, fermeture à $t=0$. $i(\infty)$ (en A) ?", "12/6", "2", r"$i(\infty)=\dfrac ER=2$ A.", src=TD + ", ex. 2", duree=1),
        v("t72", r"Même circuit, $L=30$ mH. $\tau$ (en ms) ?", "Rational(30,1000)/6*1000", "5", r"$\tau=\dfrac LR=5$ ms.", src=TD + ", ex. 2", duree=2),
        v("t73", r"Même circuit : $i(t)$ en A, $t$ en ms ?", "2+(0-2)*exp(-t/5)", "2*(1-exp(-t/5))", r"$i(t)=\dfrac ER\left(1-e^{-Rt/L}\right)=2(1-e^{-t/5})$.", src=TD + ", ex. 2", duree=3),
        v("t74", r"Même circuit : $u_L(t)$ en V, $t$ en ms ?", "Rational(30,1000)*diff(2*(1-exp(-t/5)), t)*1000", "12*exp(-t/5)", r"$u_L=L\dfrac{di}{dt}=Ee^{-t/\tau}=12e^{-t/5}$ V.", src=TD + ", ex. 2", duree=3),
        v("t75", r"Même circuit : $u_L(0^+)$ (en V) ?", "12", "12", r"$i(0^+)=0$ : pas de tension sur $R$, toute la tension $E$ est sur la bobine.", src=TD + ", ex. 2", duree=1),
        o("t76", r"Allure de $i(t)$ et de $u_L(t)$ à la fermeture d'un circuit $E$, $R$, $L$.",
          r"$i$ part de $0$ (continuité) et tend vers $E/R$. $u_L$ saute à $E$ puis décroît vers $0$ ; leurs tangentes à l'origine coupent les asymptotes en $t=\tau=L/R$.", src=TD + ", ex. 2", duree=4),
        v("t77", r"Courant à $t=\tau$ en pourcentage de $E/R$ (exact) ?", "100*(1-exp(-1))", "100-100*exp(-1)", r"$1-e^{-1}\approx63\,\%$.", duree=2),
    ]},
    {"n": 8, "titre": "Constante de temps", "notions": ["tau", "resolution"], "exos": [
        v("t81", r"$R=4{,}7$ kΩ, $C=10\,\mu$F. $\tau$ (en ms) ?", "Rational(47,10)*10", "47", r"$\tau=RC=4{,}7\times10^3\times10^{-5}=47\times10^{-3}$ s.", duree=2),
        v("t82", r"$L=100$ mH, $R=50$ Ω. $\tau$ (en ms) ?", "Rational(100,50)", "2", r"$\tau=L/R=2$ ms.", duree=2),
        v("t83", r"Décharge : $s(t)=s_0e^{-t/\tau}$. Fraction restante à $t=3\tau$ (exact) ?", "exp(-3)", "exp(-3)", r"$e^{-3}\approx5\,\%$.", duree=2),
        v("t84", r"Instant (en multiples de $\tau$) où une décharge atteint la moitié de sa valeur initiale (exact) ?", "log(2)", "log(2)", r"$e^{-t/\tau}=\tfrac12$ donc $t=\tau\ln2\approx0{,}69\tau$.", duree=3),
        v("t85", r"Écart restant (en %) après $10\tau$ : arrondi du cours ?", "Rational(5,1000)", "Rational(1,200)", r"$e^{-10}\approx4{,}5\times10^{-5}$, soit moins de $0{,}005\,\%$.", src=TD + ", ex. 4", duree=2),
        o("t86", r"Deux façons de lire $\tau$ sur une courbe expérimentale.",
          r"1. La tangente à l'origine coupe l'asymptote finale en $t=\tau$. 2. À $t=\tau$, le signal a parcouru $63\,\%$ de l'écart initial–final (il reste $37\,\%$ pour une décharge).", src=TD + ", ex. 4", duree=3),
        o("t87", r"Comment identifier $\tau$ dans une équation différentielle ou dans une solution ?",
          r"Équation : coefficient de $s$ quand celui de $\dfrac{ds}{dt}$ vaut $1$ ($\dfrac1\tau$). Solution : dénominateur de $t$ dans l'exponentielle $e^{-t/\tau}$.", src=TD, duree=2),
    ]},
    {"n": 9, "titre": "Thévenin pour se ramener à RC ou RL", "notions": ["thevenin_t", "tau"], "exos": [
        v("t91", r"TD ex. 4 : $E$, $R$ en série, puis $R/2$ et $C$ en parallèle. $E_{th}$ vu par $C$ avec $E=9$ V (en V) ?", "9*Rational(1,2)/(1+Rational(1,2))", "3", r"Diviseur $R$, $R/2$ : $E_{th}=\dfrac E3=3$ V.", src=TD + ", ex. 4", duree=3),
        v("t92", r"Même circuit : $R_{th}$ avec $R=3$ kΩ (en kΩ) ?", "3*Rational(3,2)/(3+Rational(3,2))", "1", r"$R\parallel\dfrac R2=\dfrac R3=1$ kΩ.", src=TD + ", ex. 4", duree=2),
        v("t93", r"Même circuit, $R=3$ kΩ, $C=1\,\mu$F : $\tau'$ (en ms) ?", "1*1", "1", r"$\tau'=R_{th}C=\dfrac{RC}3=1$ ms.", src=TD + ", ex. 4", duree=2),
        v("t94", r"Même circuit, $C$ chargé sous $E=9$ V avant la fermeture de $K$. $u(t')$ en V, $t'$ en ms ($\tau'=1$ ms) ?", "3+(9-3)*exp(-t)", "3*(2*exp(-t)+1)", r"$u(t')=\dfrac E3+\dfrac{2E}3e^{-t'/\tau'}=3(2e^{-t'}+1)$ : décharge partielle de $9$ V vers $3$ V.", src=TD + ", ex. 4", duree=4),
        v("t95", r"Contrôle 2023 : $E$, $R$ en série, puis $R\parallel L$. $R_{th}$ vu par $L$ avec $R=2$ kΩ (en kΩ) ?", "2*2/(2+2)", "1", r"$E_{th}=\dfrac E2$, $R_{th}=R\parallel R=\dfrac R2=1$ kΩ.", src=X23 + ", ex. 2", duree=2),
        v("t96", r"Même circuit, $L=0{,}1$ H, $R=100$ Ω : $\tau$ (en ms) ?", "Rational(1,10)/50*1000", "2", r"$\tau=\dfrac{L}{R_{th}}=\dfrac{2L}R=2$ ms.", src=X23 + ", ex. 2", duree=2),
        o("t97", r"TD ex. 3 : montrer que $E$, $R$, puis $R$ en parallèle avec $(R+C)$ se ramène à un RC série ; donner $\tau$.",
          r"Norton : $\dfrac ER$ en parallèle avec $R$ et $R$, soit $\dfrac R2$ ; retour Thévenin : $\dfrac E2$ en série avec $\dfrac R2$, plus $R$ : $R_{th}=\dfrac{3R}2$. Mailles : $\dfrac E2=\dfrac{3R}2i_2+u_C$, d'où $\dfrac{di_2}{dt}+\dfrac{2}{3RC}i_2=0$ et $\tau=\dfrac{3RC}2$.", src=TD + ", ex. 3", duree=6),
    ]},
    {"n": 10, "titre": "Décharge et ouverture", "notions": ["resolution", "initial"], "exos": [
        v("t101", r"TD ex. 3.2 : on ouvre $K$, $C$ chargé sous $\dfrac E2$ se décharge dans $R$ et $R$ en série. $\tau$ avec $R=1$ kΩ, $C=1\,\mu$F (en ms) ?", "2*1*1", "2", r"$\tau=2RC=2$ ms.", src=TD + ", ex. 3.2", duree=2),
        v("t102", r"Même décharge, $E=8$ V, $R=1$ kΩ : $i_3(0^+)$ (en mA) ?", "(8/2)/(2*1)", "2", r"$i_3=\dfrac{u_C}{2R}=\dfrac{E}{4R}=2$ mA.", src=TD + ", ex. 3.2", duree=3),
        v("t103", r"Même décharge : $i_2(t')$ en mA, $t'$ en ms ?", "-2*exp(-t/2)", "-2*exp(-t/2)", r"$i_2=-i_3$ : $i_2(t')=-\dfrac E{4R}e^{-t'/2RC}=-2e^{-t'/2}$ mA.", src=TD + ", ex. 3.2", duree=3),
        v("t104", r"Même décharge : $u_C(\infty)$ (en V) ?", "0", "0", r"Aucun générateur : l'énergie du condensateur est dissipée par effet Joule, tout tend vers $0$.", src=TD + ", ex. 3.2", duree=1),
        v("t105", r"Étincelle de rupture : $E=40$ V, $R=40$ Ω, $L$ en série. Courant juste avant l'ouverture (en A) ?", "40/40", "1", r"Régime permanent : bobine $=$ fil, $i=E/R=1$ A.", src=TD + ", pour aller plus loin", duree=2),
        v("t106", r"Même circuit, coupure modélisée par $C=10$ pF, $L=4$ mH : $\omega_0=1/\sqrt{LC}$ (en rad/s) ?", "1/sqrt(Rational(4,1000)*Rational(10,10**12))", "5000000", r"$LC=4\times10^{-14}$, $\omega_0=5\times10^6$ rad/s.", src=TD + ", pour aller plus loin", duree=3),
        o("t107", r"Pourquoi l'ouverture d'un circuit inductif produit-elle une étincelle ?",
          r"Le courant dans la bobine ne peut pas s'annuler brutalement : il charge la petite capacité de la coupure. La tension monte à $u_{max}\approx E\left(1+\dfrac1{RC\omega_0}\right)\approx20\,000$ V en moins de $3\times10^{-7}$ s, au-delà du potentiel d'éclatement ($\approx1000$ V).", src=TD + ", pour aller plus loin", duree=5),
    ]},
    {"n": 11, "titre": "Rappel : théorème de Millman", "notions": ["millman_t"], "exos": [
        v("t111", r"Branches entre $A$ et la masse : $(2E,R)$, $(-E,2R)$, $R$ seule, et source $I$ entrant en $A$. $U$ en fonction de $E$, $R$, $I$ (symboles `V` pour $E$, `I0` pour $I$) ?", "(2*V/R - V/(2*R) + I0)/(1/R+1/(2*R)+1/R)", "(3*V+2*R*I0)/5", r"$U=\dfrac{\frac{2E}R-\frac E{2R}+I}{\frac1R+\frac1{2R}+\frac1R}=\dfrac{3E+2RI}{5}$.", src=X23 + ", ex. 3.1", duree=5),
        v("t112", r"Même montage, $E=5$ V, $R=1$ kΩ, $I=5$ mA : $U$ (en V) ?", "(3*5+2*1*5)/5", "5", r"$\dfrac{15+10}5=5$ V.", src=X23 + ", ex. 3.1", duree=2),
        v("t113", r"Contrôle 2023, ex. 3.2 : $U=\dfrac{-3E-6RI}{2}$ avec $E=2$ V, $R=1$ kΩ, $I=1$ mA. $U$ (en V) ?", "(-3*2-6*1*1)/2", "-6", r"$\dfrac{-6-6}2=-6$ V.", src=X23 + ", ex. 3.2", duree=2),
        o("t114", r"Contrôle 2023, ex. 3.2 : comment utiliser Millman quand une branche contient la source $2E$ entre $B$ et $C$ ?",
          r"Millman en $A$ : $U=\dfrac{\frac{V_C}{2R}-4I-\frac{2E}{4R}+I}{\frac1{2R}+\frac1{4R}+\frac1{4R}}=\dfrac{V_C-6RI-E}{2}$. La source de gauche impose $2E=V_B-V_C$, soit $V_C=-2E$, d'où $U=\dfrac{-3E-6RI}{2}$.", src=X23 + ", ex. 3.2", duree=8),
        o("t115", r"De quelle loi vient le théorème de Millman ?", r"De la loi des nœuds appliquée au nœud $A$.", src=X23 + ", Q1", duree=1),
        v("t116", r"Branches $(10$ V$, 1$ kΩ$)$ et $(0, 1$ kΩ$)$ entre $A$ et la masse. $V_A$ (en V) ?", "(10/1+0)/(1+1)", "5", r"$\dfrac{10}{2}=5$ V.", duree=2),
    ]},
    {"n": 12, "titre": "Niveau examen : contrôle février 2023", "notions": ["composants", "permanent", "initial", "thevenin_t", "millman_t"], "examen": True, "exos": [
        o("xd1", r"Exercice 1 (QCM) : origine de Millman ; unités de $C$ et $L$ ; bobine en régime permanent ; $E$, $K$, $R$, $C$ déchargé : $u_C$ juste après la fermeture et en régime permanent.",
          r"Loi des nœuds ; farad ; henry ; un fil ; $u_C(0^+)=0$ ; $u_C(\infty)=E$.", src=X23 + ", ex. 1 (4 points)", duree=5),
        o("xd2", r"Exercice 2.1 : tableau $i$, $i_R$, $i_L$, $u_L$ à $0^+$ et $t\to\infty$ ($E$, $K$, $R$, puis $R\parallel L$).",
          r"$0^+$ : $\dfrac E{2R}$, $\dfrac E{2R}$, $0$, $\dfrac E2$. $\infty$ : $\dfrac ER$, $0$, $\dfrac ER$, $0$.", src=X23 + ", ex. 2 (10 points)", duree=6),
        v("xd3", r"Exercice 2.2.a : $E_{th}$ vu par $L$, avec $E=12$ V (en V) ?", "12/2", "6", r"Norton $\dfrac ER$ avec $R\parallel R=\dfrac R2$ : $E_{th}=\dfrac E2=6$ V, $R_{th}=\dfrac R2$.", src=X23 + ", ex. 2", duree=4),
        v("xd4", r"Exercice 2.2.b : $u_L(t)$ en fonction de $E$, $R$, $L$, $t$ (symbole `V` pour $E$) ?", "V/2 * exp(-t*(R/2)/L)", "V/2*exp(-R*t/(2*L))", r"Mailles : $E_{th}=R_{th}i_L+u_L$, on dérive : $\dfrac{du_L}{dt}+\dfrac{R}{2L}u_L=0$. $u_L(0^+)=\dfrac E2$ : $u_L(t)=\dfrac E2e^{-\frac{R}{2L}t}$, $\tau=\dfrac{2L}R$.", src=X23 + ", ex. 2", duree=8),
        v("xd5", r"Exercice 2 : $\tau$ avec $L=50$ mH, $R=100$ Ω (en ms) ?", "2*Rational(50,1000)/100*1000", "1", r"$\tau=\dfrac{2L}R=1$ ms.", src=X23 + ", ex. 2", duree=2),
        v("xd6", r"Exercice 3.1 : $U$ en fonction de $E$, $R$, $I$ (symboles `V`, `I0`) ?", "(2*V/R - V/(2*R) + I0)/(1/R+1/(2*R)+1/R)", "(3*V+2*R*I0)/5", r"Millman en $A$ : $U=\dfrac{3E+2RI}{5}$.", src=X23 + ", ex. 3 (6 points)", duree=6),
        v("xd7", r"Exercice 3.2 : $U$ en fonction de $E$, $R$, $I$ (symboles `V`, `I0`), sachant $V_C=-2E$ ?", "(-2*V/(2*R) - 4*I0 - 2*V/(4*R) + I0)/(1/(2*R)+1/(4*R)+1/(4*R))", "(-3*V-6*R*I0)/2", r"$U=\dfrac{V_C-6RI-E}{2}$ avec $V_C=-2E$ : $U=\dfrac{-3E-6RI}{2}$.", src=X23 + ", ex. 3", duree=6),
    ]},
]


def _v(enonce, calc, ans, sol):
    return {"enonce": enonce, "calc": calc, "ans": ans, "sol": sol}


VARIANTS = {
    "t11": [_v(r"Condensateur $C=10\,\mu$F, $\dfrac{du}{dt}=200$ V/s. Courant (en mA) ?", "10*200/1000", "2", r"$i=10^{-5}\times200=2$ mA.")],
    "t12": [_v(r"Bobine $L=20$ mH, $\dfrac{di}{dt}=500$ A/s. Tension (en V) ?", "Rational(20,1000)*500", "10", r"$u=10$ V.")],
    "t23": [_v(r"$E=15$ V, $R=5$ Ω et $L$ en série, régime permanent. Courant (en A) ?", "15/5", "3", r"$i=3$ A.")],
    "t35": [_v(r"$E=12$ V, $R$, $C$ en série, $C$ déchargé. $i(0^+)$ avec $R=4$ kΩ (en mA) ?", "12/4", "3", r"$i=E/R=3$ mA.")],
    "t36": [_v(r"$E=12$ V, $R=3$ kΩ, $C$ chargé sous $U_0=3$ V. $i(0^+)$ (en mA) ?", "(12-3)/3", "3", r"$\dfrac{E-U_0}R=3$ mA.")],
    "t41": [_v(r"Constante de temps RC avec $R=2$ kΩ, $C=500$ nF (en ms) ?", "2*1000*Rational(500,10**9)*1000", "1", r"$\tau=10^{-3}$ s.")],
    "t42": [_v(r"$\tau=L/R$ avec $L=50$ mH, $R=25$ Ω (en ms) ?", "Rational(50,1000)/25*1000", "2", r"$2$ ms.")],
    "t53": [_v(r"$s(0^+)=10$, $s(\infty)=4$. $\alpha$ ?", "10-4", "6", r"$\alpha=10-4=6$.")],
    "t72": [_v(r"$L=60$ mH, $R=12$ Ω. $\tau$ (en ms) ?", "Rational(60,1000)/12*1000", "5", r"$5$ ms.")],
    "t81": [_v(r"$R=2{,}2$ kΩ, $C=100\,\mu$F. $\tau$ (en ms) ?", "Rational(22,10)*100", "220", r"$2{,}2\times10^3\times10^{-4}=0{,}22$ s.")],
    "t82": [_v(r"$L=200$ mH, $R=40$ Ω. $\tau$ (en ms) ?", "Rational(200,40)", "5", r"$5$ ms.")],
    "t92": [_v(r"Même circuit : $R_{th}$ avec $R=6$ kΩ (en kΩ) ?", "6*3/(6+3)", "2", r"$R/3=2$ kΩ.")],
    "t112": [_v(r"Même montage, $E=10$ V, $R=1$ kΩ, $I=10$ mA : $U$ (en V) ?", "(3*10+2*1*10)/5", "10", r"$\dfrac{30+20}5=10$ V.")],
    "xd5": [_v(r"Exercice 2 : $\tau$ avec $L=0{,}2$ H, $R=200$ Ω (en ms) ?", "2*Rational(2,10)/200*1000", "2", r"$\dfrac{2L}R=2$ ms.")],
}
for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["id"] in VARIANTS:
            _e["variants"] = VARIANTS[_e["id"]]


EXTRA_PARTS = []

QUIZ = [
    {"notion": "composants", "type": "qcm", "q": r"Il y a continuité :", "choix": [r"de la tension aux bornes d'un condensateur", r"du courant dans un condensateur", r"de la tension aux bornes d'une bobine", r"du courant dans une résistance"], "bonne": 0},
    {"notion": "composants", "type": "vf", "q": r"L'inductance d'une bobine s'exprime en henrys.", "bonne": True},
    {"notion": "permanent", "type": "qcm", "q": r"En régime permanent continu, un condensateur équivaut à :", "choix": [r"un interrupteur ouvert", r"un fil", r"une résistance", r"une source de tension"], "bonne": 0},
    {"notion": "permanent", "type": "vf", "q": r"En régime permanent continu, la tension aux bornes d'une bobine est nulle.", "bonne": True},
    {"notion": "initial", "type": "qcm", "q": r"$E$, $R$, $C$ déchargé : $u_C$ juste après la fermeture vaut :", "choix": [r"$0$", r"$E$", r"$E/R$", r"$RE$"], "bonne": 0},
    {"notion": "initial", "type": "vf", "q": r"À $t=0^+$, le courant dans une résistance est forcément continu.", "bonne": False},
    {"notion": "equadiff", "type": "qcm", "q": r"Dans $\dfrac{di}{dt}+\dfrac RLi=\dfrac EL$, la constante de temps est :", "choix": [r"$L/R$", r"$R/L$", r"$RL$", r"$E/L$"], "bonne": 0},
    {"notion": "equadiff", "type": "vf", "q": r"Un circuit RC série donne une équation différentielle du premier ordre.", "bonne": True},
    {"notion": "resolution", "type": "qcm", "q": r"Dans $s(t)=\alpha e^{-t/\tau}+\beta$, $\beta$ est :", "choix": [r"la valeur en régime permanent", r"la valeur initiale", r"la constante de temps", r"la pente à l'origine"], "bonne": 0},
    {"notion": "resolution", "type": "vf", "q": r"$\alpha$ se détermine avec la condition initiale.", "bonne": True},
    {"notion": "tau", "type": "qcm", "q": r"On considère le régime permanent atteint au bout de :", "choix": [r"$5\tau$", r"$\tau$", r"$\tau/2$", r"$2\tau$"], "bonne": 0},
    {"notion": "tau", "type": "vf", "q": r"La tangente à l'origine coupe l'asymptote finale en $t=\tau$.", "bonne": True},
    {"notion": "thevenin_t", "type": "qcm", "q": r"Vu du condensateur, $R_{th}$ s'obtient :", "choix": [r"sources éteintes", r"en court-circuitant le condensateur", r"en ajoutant toutes les résistances", r"avec Millman"], "bonne": 0},
    {"notion": "thevenin_t", "type": "vf", "q": r"Pour un circuit RL ramené à Thévenin, $\tau=L/R_{th}$.", "bonne": True},
    {"notion": "millman_t", "type": "qcm", "q": r"Le théorème de Millman vient de :", "choix": [r"la loi des nœuds", r"la loi des mailles", r"la loi d'Ohm seule", r"Thévenin"], "bonne": 0},
    {"notion": "millman_t", "type": "vf", "q": r"Une branche sans source contribue seulement au dénominateur de Millman.", "bonne": True},
]

_C = r"$i=C\dfrac{du}{dt}$ · $u=L\dfrac{di}{dt}$ · continuité : $u_C$ et $i_L$"
_P = r"$t\to\infty$ : $C\to$ ouvert, $L\to$ fil"
_I = r"$0^+$ : $u_C(0^+)=u_C(0^-)$, $i_L(0^+)=i_L(0^-)$ · puis Kirchhoff"
_Q = r"$\dfrac{ds}{dt}+\dfrac1\tau s=A$ · $\tau_{RC}=RC$ · $\tau_{RL}=L/R$"
_S = r"$s(t)=s(\infty)+\big(s(0^+)-s(\infty)\big)e^{-t/\tau}$"
_T = r"$\tau=RC$ ou $L/R$ · $63\,\%$ à $\tau$ · permanent à $5\tau$"
_H = r"$E_{th}$ à vide · $R_{th}$ sources éteintes · $\tau=R_{th}C$ ou $L/R_{th}$"
_M = r"$V_A=\dfrac{\sum E_i/R_i+\sum\eta_i}{\sum1/R_i}$"
_D = r"diviseur : $U_2=\dfrac{R_2}{R_1+R_2}E$"

FORMULES = {
    "t11": _C, "t12": _C, "t13": _C, "t14": _C, "t15": r"$C$ en F · $L$ en H", "t16": _C, "t17": _C,
    "t21": _P, "t22": _P, "t23": _P, "t24": _P + " · " + _D, "t25": _P, "t26": _P, "t27": _P,
    "t31": _I + " · " + _D, "t32": _I, "t33": _I + " · " + _D, "t34": _I, "t35": _I, "t36": _I, "t37": _I + " · " + _P,
    "t41": _Q, "t42": _Q, "t43": _Q, "t44": _Q, "t45": _Q, "t46": _Q + " · " + _C, "t47": _Q + " · " + _C,
    "t51": _S, "t52": _S, "t53": _S, "t54": _S + " · " + _Q, "t55": _S, "t56": _S, "t57": _S,
    "t61": _S + " · " + _T, "t62": _S + " · " + _C, "t63": _T, "t64": _I + " · " + _S, "t65": _S + " · " + _T, "t66": _T, "t67": _T,
    "t71": _P, "t72": _Q, "t73": _S, "t74": _C + " · " + _S, "t75": _I, "t76": _S + " · " + _T, "t77": _T,
    "t81": _T, "t82": _T, "t83": _S, "t84": _S, "t85": _T, "t86": _T, "t87": _Q,
    "t91": _H + " · " + _D, "t92": _H, "t93": _H, "t94": _H + " · " + _S, "t95": _H, "t96": _H, "t97": _H + " · " + _Q,
    "t101": _T, "t102": _I, "t103": _S, "t104": _P, "t105": _P, "t106": r"$\omega_0=\dfrac1{\sqrt{LC}}$", "t107": _C,
    "t111": _M, "t112": _M, "t113": _M, "t114": _M, "t115": _M, "t116": _M,
    "xd1": _C + " · " + _P, "xd2": _I + " · " + _P, "xd3": _H, "xd4": _S + " · " + _Q, "xd5": _H, "xd6": _M, "xd7": _M,
}


# ---------------------------------------------------------------- circuit figures (`schema.py`)

def _m31(d):
    """Contrôle 2023, ex. 3.1: branches (2E, R), (-E, 2R), R, and current source I behind 2R, between A and B."""
    d += (s := SrcU().endpoints((0, 0), (0, 3)))
    tension(d, s, "$2E$")
    d += R().endpoints((0, 3), (3, 3)).label("$R$")
    d += R().endpoints((3, 3), (3, 1.6)).label("$2R$", loc="bottom")
    d += (s := SrcU().endpoints((3, 1.6), (3, 0)))
    tension(d, s, "$E$", cote=False, ofst=0.5, length=1)
    d += Fil().endpoints((3, 3), (8, 3))
    d += Point().at((6, 3)).label("$A$", loc="top")
    d += (r := R().endpoints((6, 3), (6, 0)).label("$R$", loc="bottom"))
    tension(d, r, "$U$", sens=-1, cote=False, ofst=0.9)
    d += R().endpoints((6, 3), (9, 3)).label("$2R$")
    d += (s := SrcI().endpoints((9, 0), (9, 3)))
    courant(d, s, "$I$", debut=False)
    d += Point().at((6, 0)).label("$B$", loc="bottom")
    d += Fil().endpoints((0, 0), (9, 0))


def _m32(d):
    """Contrôle 2023, ex. 3.2: (R, E) and 2E between C and B, 2R from C to A; at A: (4I, 4R), 4R, (4R, 2E), I."""
    d += R().endpoints((0, 3), (0, 1.6)).label("$R$")
    d += (s := SrcU().endpoints((0, 0), (0, 1.6)))
    tension(d, s, "$E$", ofst=0.5, length=1)
    d += Fil().endpoints((0, 3), (2, 3))
    d += Point().at((2, 3)).label("$C$", loc="top")
    d += (s := SrcU().endpoints((2, 3), (2, 0)))
    tension(d, s, "$2E$")
    d += R().endpoints((2, 3), (5, 3)).label("$2R$")
    d += (s := SrcI().endpoints((5, 3), (5, 1.6)))
    courant(d, s, "$4I$", debut=False)
    d += R().endpoints((5, 1.6), (5, 0)).label("$4R$", loc="bottom")
    d += Fil().endpoints((5, 3), (11, 3))
    d += Point().at((7, 3)).label("$A$", loc="top")
    d += R().endpoints((7, 3), (7, 0)).label("$4R$", loc="bottom")
    d += R().endpoints((9, 3), (9, 1.6)).label("$4R$", loc="bottom")
    d += (s := SrcU().endpoints((9, 1.6), (9, 0)))
    tension(d, s, "$2E$", ofst=0.5, length=1)
    d += (s := SrcI().endpoints((11, 0), (11, 3)))
    courant(d, s, "$I$", debut=False)
    d += Point().at((7, 0)).label("$B$", loc="bottom")
    d += Fil().endpoints((0, 0), (11, 0))
    d += Fil().endpoints((11, 3), (12.2, 3))
    d += Fil().endpoints((11, 0), (12.2, 0))
    d += (g := Gap().endpoints((12.2, 3), (12.2, 0)))
    tension(d, g, "$U$", sens=-1, ofst=0.3)


S, P = "s", "p"
FIG_RC = schema_echelle("E", [(S, "R", "R"), (P, "C", "C")], "u_C")
FIG_RL = schema_echelle("E", [(S, "R", "R"), (P, "L", "L")], "u_L")
FIG_KRL = schema_echelle("E", [(S, "K", "K"), (S, "R", "R"), (P, "L", "L")], "u_L")
FIG_RRRC = schema_echelle("E", [(S, "R", "R"), (P, "R", "R"), (S, "R", "R"), (P, "C", "C")], "u_C")
FIG_EX2 = schema_echelle("E", [(S, "K", "K"), (S, "R", "R"), (P, "R", "R"), (P, "L", "L")], "u_L(t)")
FIG_EX2B = schema_echelle("E_{th}", [(S, "R", "R_{th}"), (P, "L", "L")], "u_L(t)")
FIG_TD4 = schema_echelle("E", [(S, "R", "R"), (P, "R", "R/2"), (P, "C", "C")], "u")
FIG_M31 = fig(_m31, "Schéma : entre A et B, les branches (2E, R), (-E, 2R), R seule (tension U) et une source de courant I en série avec 2R")
FIG_M32 = fig(_m32, "Schéma : branche (R, E) et source 2E entre C et B ; 2R de C vers A ; entre A et B : source de courant 4I en série avec 4R, 4R, (4R, 2E) et source de courant I ; U entre A et B")

FIGS = {**dict.fromkeys(["t22", "t27", "t35", "t36", "t41", "t46"], FIG_RC),
        **dict.fromkeys(["t23", "t42", "t47"], FIG_RL),
        **dict.fromkeys(["t71", "t72", "t73", "t74", "t75"], FIG_KRL),
        "t24": FIG_RRRC,
        **dict.fromkeys(["t25", "t26", "t31", "t32", "t37", "t95", "t96", "xd2"], FIG_EX2),
        **dict.fromkeys(["xd3", "xd4", "xd5"], FIG_EX2 + "\n\n" + FIG_EX2B),
        **dict.fromkeys(["t91", "t92", "t93", "t94"], FIG_TD4),
        **dict.fromkeys(["t111", "t112", "xd6"], FIG_M31),
        **dict.fromkeys(["t113", "t114", "xd7"], FIG_M32)}
ajoute(LEVELS, FIGS)
