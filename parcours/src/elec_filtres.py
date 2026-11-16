"""Level path: S2 electronics, study of filters (B3, March), promo 2031.

Calibrated on the Moodle course « Electronique S2 - Études des filtres » (`Kit de Survie Filtres`, `Le filtrage -
Promo 2030`), the TD « Études des filtres » (8 circuits + 2 bonus, with its correction) and the B3 exam of March 2026
(`Examen Elec - InfoS2 - B3 - Mars 2026`, with its correction). S2 vocabulary: H(w) transfer function, G(w) = |H(w)|
gain, G_dB = 20 log G. Circuits are described in words and drawn as SVG
(`schema.py`, `FIGS` at the end).
Symbolic answers use the sympy symbols R, L, C, w (w = omega) and I (imaginary unit j); never E (Euler's number).
"""
from .schema import ajoute, schema_echelle


SUBJECT = {
    "id": "elec-s2-filtres",
    "ordre": 520,
    "matiere": "electronique",
    "semestre": "S2",
    "ecue": "Études des filtres",
    "titre": "Études des filtres",
    "chapitres_moodle": ["Electronique S2 - Études des filtres/01_Documents de cours", "Electronique S2 - Études des filtres/02_Travaux Dirigés"],
    "td": "TD « Études des filtres » (8 filtres, 2 exercices bonus)",
    "examens": ["Contrôle d'électronique B3 (mars 2026)"],
}

NOTIONS = [
    {"id": "ft", "titre": "Fonction de transfert et gain",
     "formule": r"$\underline H(\omega)=\dfrac{\underline V_S}{\underline V_E}$ · gain $G(\omega)=|\underline H(\omega)|=\dfrac{V_S}{V_E}$ · $G_{dB}=20\log G$ · $\arg\underline H=\arg\underline V_S-\arg\underline V_E$",
     "exemple": r"$G=\tfrac12$ : $G_{dB}=-20\log2\approx-6$ dB",
     "cours": r"Un filtre est un quadripôle dont le comportement dépend de la fréquence : il contient au moins un condensateur ou une bobine. On l'étudie par sa fonction de transfert, quotient des amplitudes complexes de sortie et d'entrée. Son module est le gain, son argument le déphasage de la sortie par rapport à l'entrée."},
    {"id": "limites", "titre": "Composants en TBF et en THF",
     "formule": r"$|\underline Z_C|=\dfrac1{C\omega}$ : TBF $\to\infty$ (interrupteur ouvert), THF $\to0$ (fil) · $|\underline Z_L|=L\omega$ : TBF $\to0$ (fil), THF $\to\infty$ (interrupteur ouvert)",
     "exemple": r"$3R$, $C$ en série, sortie sur $R$ : TBF $G\to0$, THF $G\to\tfrac14$",
     "cours": r"L'étude asymptotique remplace chaque condensateur et chaque bobine par un fil ou un interrupteur ouvert, puis calcule $v_s$ sur le schéma de résistances obtenu, le plus souvent avec un pont diviseur."},
    {"id": "nature", "titre": "Nature et ordre d'un filtre",
     "formule": r"passe-bas : $G$ décroissant · passe-haut : croissant · passe-bande : croissant puis décroissant · coupe-bande : décroissant puis croissant · ordre $=$ nombre de condensateurs et bobines $=$ degré en $\omega$",
     "exemple": r"$L$ en série, $C\parallel L$ … : $1$ condensateur et $2$ bobines, ordre $3$",
     "cours": r"La comparaison des gains en TBF et en THF donne la nature du filtre : gain nul aux deux bouts pour un passe-bande. L'ordre est le degré du polynôme en $\omega$ de la fonction de transfert ; pour un premier ordre, $G$ est forcément monotone."},
    {"id": "bode", "titre": "Gain en décibels et pentes",
     "formule": r"$G_{dB}=20\log G$ · $G=10^{G_{dB}/20}$ · $\times10\to+20$ dB · $\times2\to+6$ dB · pente des asymptotes : $\pm20n$ dB/décade (ordre $n$) · déphasage total $n\cdot\tfrac\pi2$",
     "exemple": r"passe-bas d'ordre $2$ : $-40$ dB par décade au-delà de la coupure",
     "cours": r"Le gain varie dans de grandes proportions : on le trace en décibels en fonction de $\log f$ (diagramme de Bode). Loin de la bande passante, la courbe est une droite (asymptote) dont la pente, en dB par décade, vaut $20$ fois l'ordre du filtre."},
    {"id": "coupure", "titre": "Fréquence de coupure et bande passante",
     "formule": r"$G(\omega_c)=\dfrac{G_{max}}{\sqrt2}$ · $G_{dB}(\omega_c)=G_{dB,max}-3$ dB · bande passante : $[f_{cb};f_{ch}]$, largeur $f_{ch}-f_{cb}$ · $f=\dfrac\omega{2\pi}$",
     "exemple": r"$G_{max}=\tfrac14$ : $G(\omega_c)=\dfrac1{4\sqrt2}$",
     "cours": r"À la fréquence de coupure, le gain est inférieur de $3$ dB au gain maximal. Au-delà, le signal n'est pas coupé mais atténué. Passe-bas et passe-haut ont une seule fréquence de coupure ; passe-bande et coupe-bande en ont deux."},
    {"id": "ordre1", "titre": "Filtres du premier ordre",
     "formule": r"passe-bas : $\underline H=G_{max}\dfrac1{1+j\frac\omega{\omega_c}}$, $G_{max}=G_{TBF}$ · passe-haut : $\underline H=G_{max}\dfrac{j\frac\omega{\omega_c}}{1+j\frac\omega{\omega_c}}$, $G_{max}=G_{THF}$",
     "exemple": r"$\dfrac{jRC\omega}{1+4jRC\omega}=\dfrac14\cdot\dfrac{4jRC\omega}{1+4jRC\omega}$ : $G_{max}=\tfrac14$, $\omega_c=\dfrac1{4RC}$",
     "cours": r"On met la fonction de transfert sous forme normalisée en rendant égal à $1$ le terme constant du dénominateur, puis on identifie $G_{max}$ et $\omega_c$. Le facteur mis en évidence est le gain en TBF (passe-bas) ou en THF (passe-haut)."},
    {"id": "ordre2", "titre": "Filtres du second ordre",
     "formule": r"dénominateur $1+2j\sigma\dfrac\omega{\omega_0}-\left(\dfrac\omega{\omega_0}\right)^2$ · passe-bas : $G_0$ · passe-haut : $-G_0\left(\frac\omega{\omega_0}\right)^2$ · passe-bande : $G_0\,2j\sigma\frac\omega{\omega_0}$ · $\omega_0$ : pulsation propre · $\sigma$ : amortissement",
     "exemple": r"$\dfrac1{1+jRC\omega-LC\omega^2}$ : $\omega_0=\dfrac1{\sqrt{LC}}$, $\sigma=\dfrac{RC}2\omega_0$",
     "cours": r"On identifie $(\omega/\omega_0)^2$ au terme en $\omega^2$ du dénominateur, puis $2\sigma\omega/\omega_0$ au terme en $j\omega$. La forme du numérateur donne la nature ; pour un passe-bande, le gain est maximal à $\omega_0$ et vaut $G_0$."},
    {"id": "methode", "titre": "Méthode complète d'étude d'un filtre",
     "formule": r"1. TBF et THF $\to$ nature · 2. représentation complexe · 3. réduction (associations, Thévenin/Norton) · 4. pont diviseur $\to\underline H$ · 5. forme normalisée $\to G_{max},\omega_c$ ou $G_0,\omega_0,\sigma$",
     "exemple": r"$R$, $C$ en parallèle, $L$, $R$ en sortie : $\underline E_{th}=\dfrac{\underline V_E}{1+jRC\omega}$, $\underline Z_{th}=\dfrac{R}{1+jRC\omega}+jL\omega$",
     "cours": r"L'étude qualitative sert aussi de vérification : les limites de la fonction de transfert trouvée doivent redonner les gains en TBF et en THF. Quand la sortie n'est pas sur un simple diviseur, on réduit la partie gauche du circuit en générateur de Thévenin."},
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


X26 = "Contrôle d'électronique B3, mars 2026"
TD = "TD d'électronique S2 « Études des filtres »"
KIT = "Kit de survie « Le filtrage »"
COURS = "Cours « Le filtrage »"

_ZC = "(1/(I*C*w))"

LEVELS = [
    {"n": 1, "titre": "Fonction de transfert et gain", "notions": ["ft"], "exos": [
        v("f11", r"$V_E=10$ V et $V_S=2$ V (valeurs efficaces). Gain $G$ ?", "Rational(2,10)", "Rational(1,5)", r"$G=V_S/V_E=0{,}2$.", src=KIT, duree=1),
        v("f12", r"$G=10$. $G_{dB}$ ?", "20*log(10,10)", "20", r"$20\log10=20$ dB.", src=KIT, duree=1),
        v("f13", r"$G=\tfrac12$. $G_{dB}$ exact ?", "20*log(Rational(1,2),10)", "-20*log(2)/log(10)", r"$-20\log2\approx-6$ dB.", duree=2),
        v("f14", r"$G_{dB}=-40$ dB. Gain $G$ ?", "10**(-2)", "Rational(1,100)", r"$G=10^{-40/20}=10^{-2}$.", duree=2),
        v("f15", r"$\underline H=\dfrac{1}{1+j}$. Gain $G$ ?", "abs(1/(1+I))", "1/sqrt(2)", r"$|1+j|=\sqrt2$, $G=\dfrac1{\sqrt2}$.", duree=2),
        v("f16", r"Même $\underline H$ : déphasage de $v_s$ par rapport à $v_e$ (en degrés) ?", "-45", "-45", r"$\arg\underline H=-\arg(1+j)=-45°$.", src=KIT, duree=2),
        o("f17", r"Qu'est-ce qu'un filtre électronique ? Que doit-il contenir ?",
          r"Un quadripôle qui amplifie ou atténue les composantes d'un signal selon leur fréquence. Il contient au moins un condensateur ou une bobine, dont l'impédance dépend de $\omega$.", src=X26 + ", Q5-Q6", duree=2),
    ]},
    {"n": 2, "titre": "Composants en TBF et en THF", "notions": ["limites", "ft"], "exos": [
        o("f21", r"À quoi équivalent une bobine et un condensateur en très basses fréquences ? En très hautes fréquences ?",
          r"TBF : bobine $=$ fil ($L\omega\to0$), condensateur $=$ interrupteur ouvert ($\frac1{C\omega}\to\infty$). THF : bobine $=$ interrupteur ouvert, condensateur $=$ fil (interrupteur fermé).", src=X26 + ", Q3-Q4", duree=2),
        v("f22", r"$v_e$, $3R$ et $C$ en série, sortie sur $R$. Gain en THF ?", "R/(3*R+R)", "Rational(1,4)", r"$C\to$ fil : diviseur $\dfrac{R}{3R+R}=\tfrac14$.", src=TD + ", filtre 1", duree=2),
        v("f23", r"Même filtre : gain en TBF ?", "0", "0", r"$C\to$ ouvert : aucun courant dans $R$, $v_s\to0$.", src=TD + ", filtre 1", duree=1),
        v("f24", r"$v_e$, $R$ et $L$ en série, sortie sur $5R$. Gain en TBF ?", "5*R/(R+5*R)", "Rational(5,6)", r"$L\to$ fil : $\dfrac{5R}{6R}=\tfrac56$.", src=TD + ", filtre 2", duree=2),
        v("f25", r"$v_e$, $R$ en série, puis $2R$ et $C$ en parallèle en sortie. Gain en TBF ?", "2*R/(2*R+R)", "Rational(2,3)", r"$C\to$ ouvert : $\dfrac{2R}{2R+R}=\tfrac23$ ; en THF $C\to$ fil, $G\to0$.", src=TD + ", filtre 3", duree=2),
        v("f26", r"$v_e$, $R_1$ en série, puis $R_2=R_1$ et $C$ en parallèle en sortie. Gain en TBF ?", "R/(R+R)", "Rational(1,2)", r"$C$ ouvert : diviseur $\dfrac{R}{2R}=\tfrac12$ ; en THF $G\to0$.", src=X26 + ", Q8-Q9", duree=2),
        v("f27", r"$v_e$, $L$ et $R$ en série, $C$ en sortie. Gain en TBF ?", "1", "1", r"$L$ fil, $C$ ouvert : aucun courant, pas de chute dans $R$, $v_s=v_e$.", src=TD + ", filtre 4", duree=2),
    ]},
    {"n": 3, "titre": "Nature et ordre d'un filtre", "notions": ["nature", "limites"], "exos": [
        o("f31", r"$v_e$, $3R$ et $C$ en série, sortie sur $R$ : nature du filtre ?",
          r"TBF : $G\to0$. THF : $G\to\tfrac14$. Le gain croît : passe-haut (ordre $1$).", src=TD + ", filtre 1", duree=3),
        o("f32", r"$v_e$, $C$ en série, puis $R$ et $L$ en parallèle en sortie : nature ?",
          r"TBF : $C$ ouvert, $G\to0$. THF : $C$ fil, $L$ ouvert, $v_s=v_e$, $G\to1$. Passe-haut d'ordre $2$.", src=TD + ", filtre 5", duree=3),
        o("f33", r"$v_e$, $R$ en série, puis $C$ et $L$ en parallèle en sortie : nature ?",
          r"TBF : $L$ fil, $v_s=0$. THF : $C$ fil, $v_s=0$. Gain nul aux deux bouts : passe-bande d'ordre $2$.", src=TD + ", filtre 6", duree=3),
        v("f34", r"Un filtre contient $1$ condensateur, $2$ bobines et $3$ résistances. Ordre ?", "1+2", "3", r"Ordre $=$ nombre de composants non résistifs $=3$.", src=KIT, duree=1),
        o("f35", r"Filtre $v_e$, $R_1$ en série, $R_2\parallel C$ en sortie. Quel filtre obtient-on si l'on remplace $R_2$ par une bobine ?",
          r"TBF : la bobine est un fil, $v_s=0$. THF : le condensateur est un fil, $v_s=0$. Passe-bande.", src=X26 + ", Q12", duree=3),
        o("f36", r"Filtre passe-bas : $v_e$, $R$ en série, $C$ en parallèle, $L$ en série, $R$ en sortie. Que devient-il si l'on inverse la bobine et le condensateur ?",
          r"Les comportements en TBF et en THF sont inversés : le passe-bas devient un passe-haut.", src=X26 + ", ex. 2", duree=3),
        o("f37", r"Pourquoi le gain d'un filtre du premier ordre est-il forcément monotone ?",
          r"Sa fonction de transfert normalisée ne contient qu'un terme $j\omega/\omega_c$ : son module varie dans un seul sens, de $G_{TBF}$ à $G_{THF}$. Un passe-bande demande au moins l'ordre $2$.", src=COURS, duree=3),
    ]},
    {"n": 4, "titre": "Décibels et pentes", "notions": ["bode", "ft"], "exos": [
        v("f41", r"Pente de l'asymptote d'un passe-bas d'ordre $1$ (en dB par décade) ?", "-20", "-20", r"$-20n$ avec $n=1$.", src=COURS, duree=1),
        v("f42", r"Pente de l'asymptote d'un passe-haut d'ordre $2$ (en dB par décade) ?", "40", "40", r"$+20n$ avec $n=2$.", src=COURS, duree=1),
        v("f43", r"Passe-bas d'ordre $3$ : de combien de dB le gain chute-t-il sur $2$ décades (asymptote) ?", "20*3*2", "120", r"$-60$ dB par décade, $2$ décades : $-120$ dB, soit une chute de $120$ dB.", duree=2),
        v("f44", r"Variation totale du déphasage d'un filtre d'ordre $2$ (en degrés) ?", "2*90", "180", r"$n\cdot\tfrac\pi2=\pi$, soit $180°$.", src=COURS, duree=2),
        v("f45", r"Bonus 1 du TD : $R_1=3$ kΩ, $G_{THF}=\dfrac{R_2}{R_1+R_2}$, $G_{min}=-12$ dB ($\log2\approx0{,}3$, donc $-12$ dB $=-40\log2$). $R_2$ (en Ω) ?", "3000*Rational(1,4)/(1-Rational(1,4))", "1000", r"$\dfrac{R_2}{R_1+R_2}=10^{-2\log2}=\tfrac14$, donc $R_1+R_2=4R_2$, $R_2=\tfrac{R_1}3=1$ kΩ.", src=TD + ", bonus 1", duree=4),
        v("f46", r"$G$ multiplié par $10$. Variation de $G_{dB}$ (en dB) ?", "20*log(10,10)", "20", r"$20\log10=+20$ dB.", duree=1),
        o("f47", r"Pourquoi trace-t-on le gain en dB en fonction de $\log f$ ?",
          r"Le gain varie sur plusieurs ordres de grandeur. En échelle log-log (dB et $\log f$), loin de la bande passante, la courbe devient une droite (asymptote) de pente $\pm20n$ dB/décade : c'est le diagramme de Bode.", src=COURS, duree=3),
    ]},
    {"n": 5, "titre": "Fréquence de coupure et bande passante", "notions": ["coupure", "bode"], "exos": [
        v("f51", r"$G_{max}=\tfrac14$. Gain à la pulsation de coupure ?", "Rational(1,4)/sqrt(2)", "sqrt(2)/8", r"$G(\omega_c)=\dfrac{G_{max}}{\sqrt2}=\dfrac{\sqrt2}8$.", src=COURS, duree=2),
        v("f52", r"$G_{dB,max}=0$ dB. $G_{dB}$ à la coupure, exact (en dB) ?", "20*log(1/sqrt(2),10)", "-10*log(2)/log(10)", r"$-10\log2\approx-3$ dB.", src=COURS, duree=2),
        v("f53", r"$\omega_c=1000$ rad/s. $f_c$ exacte (en Hz) ?", "1000/(2*pi)", "500/pi", r"$f_c=\dfrac{\omega_c}{2\pi}\approx159$ Hz.", duree=2),
        v("f54", r"Passe-bande : $f_{cb}=900$ Hz, $f_{ch}=1100$ Hz. Largeur de la bande passante (en Hz) ?", "1100-900", "200", r"$f_{ch}-f_{cb}=200$ Hz.", src=COURS, duree=1),
        v("f55", r"Même filtre, fréquence centrale $1000$ Hz. Rapport fréquence centrale / bande passante ?", "1000/200", "5", r"$1000/200=5$ : plus il est grand, plus le filtre est sélectif.", src=COURS, duree=2),
        v("f56", r"Bonus 2 du TD : $L=10$ mH, $C=1\,\mu$F. Fréquence du gain maximal (en Hz, exacte) ?", "1/(2*pi*sqrt(Rational(1,100)*Rational(1,10**6)))", "5000/pi", r"$f_0=\dfrac1{2\pi\sqrt{LC}}=\dfrac{10^4}{2\pi}\approx1592$ Hz.", src=TD + ", bonus 2", duree=3),
        o("f57", r"Le signal est-il supprimé au-delà de la fréquence de coupure ?",
          r"Non. Il est seulement atténué, d'autant plus que l'on s'éloigne de la coupure (pente de $20n$ dB/décade). À la coupure, le gain est $3$ dB sous le maximum.", src=COURS, duree=2),
    ]},
    {"n": 6, "titre": "Premier ordre : passe-haut", "notions": ["ordre1", "coupure"], "exos": [
        v("f61", r"$v_e$, $3R$ et $C$ en série, sortie sur $R$. $\underline H$ ?", f"R/(3*R+{_ZC}+R)", "I*R*C*w/(1+4*I*R*C*w)", r"Diviseur : $\dfrac{R}{4R+\frac1{jC\omega}}$, on multiplie par $jC\omega$ : $\dfrac{jRC\omega}{1+4jRC\omega}$.", src=TD + ", filtre 1", duree=4),
        v("f62", r"Même filtre : $G_{max}$ ?", "Rational(1,4)", "Rational(1,4)", r"$\underline H=\dfrac14\cdot\dfrac{4jRC\omega}{1+4jRC\omega}$ : $G_{max}=G_{THF}=\tfrac14$.", src=TD + ", filtre 1", duree=2),
        v("f63", r"Même filtre, $R=1$ kΩ, $C=1\,\mu$F. $\omega_c$ (en rad/s) ?", "1/(4*1000*Rational(1,10**6))", "250", r"$\omega_c=\dfrac1{4RC}=250$ rad/s.", src=TD + ", filtre 1", duree=2),
        v("f64", r"Passe-haut $\dfrac{j\omega/\omega_c}{1+j\omega/\omega_c}$ : déphasage à $\omega=\omega_c$ (en degrés) ?", "45", "45", r"$\arg\dfrac{j}{1+j}=90°-45°=45°$.", duree=2),
        v("f65", r"Même passe-haut : gain à $\omega=\omega_c/10$ (exact) ?", "abs((I/10)/(1+I/10))", "1/sqrt(101)", r"$\dfrac{0{,}1}{\sqrt{1+0{,}01}}=\dfrac1{\sqrt{101}}\approx0{,}1$ : $-20$ dB une décade sous la coupure.", duree=3),
        v("f66", r"$v_e$, $C$ en série, $R$ en sortie. $\omega_c$ avec $R=10$ kΩ, $C=100$ nF (en rad/s) ?", "1/(10000*Rational(100,10**9))", "1000", r"$\underline H=\dfrac{jRC\omega}{1+jRC\omega}$, $\omega_c=\dfrac1{RC}=1000$ rad/s.", duree=2),
        o("f67", r"Comment met-on $\dfrac{jRC\omega}{1+4jRC\omega}$ sous forme normalisée ?",
          r"On fait apparaître au numérateur le même terme qu'au dénominateur : $\dfrac14\cdot\dfrac{4jRC\omega}{1+4jRC\omega}$. Par identification, $G_{max}=\tfrac14$ et $\dfrac\omega{\omega_c}=4RC\omega$, soit $\omega_c=\dfrac1{4RC}$.", src=TD + ", filtre 1", duree=4),
    ]},
    {"n": 7, "titre": "Premier ordre : passe-bas", "notions": ["ordre1", "limites"], "exos": [
        v("f71", r"$v_e$, $R$ et $L$ en série, sortie sur $5R$. $\underline H$ ?", "5*R/(R+I*L*w+5*R)", "5*R/(6*R+I*L*w)", r"Diviseur : $\dfrac{5R}{6R+jL\omega}=\dfrac56\cdot\dfrac1{1+j\frac{L}{6R}\omega}$.", src=TD + ", filtre 2", duree=3),
        v("f72", r"Même filtre, $R=100$ Ω, $L=0{,}6$ H. $\omega_c$ (en rad/s) ?", "6*100/Rational(6,10)", "1000", r"$\omega_c=\dfrac{6R}L=1000$ rad/s, $G_{max}=\tfrac56$.", src=TD + ", filtre 2", duree=2),
        v("f73", r"$v_e$, $R$ en série, $2R\parallel C$ en sortie. $\underline H$ ?", f"(2*R/(1+2*I*R*C*w))/(R+2*R/(1+2*I*R*C*w))", "2/(3+2*I*R*C*w)", r"$2R\parallel C=\dfrac{2R}{1+2jRC\omega}$, diviseur : $\dfrac{2}{3+2jRC\omega}=\dfrac23\cdot\dfrac1{1+\frac23jRC\omega}$.", src=TD + ", filtre 3", duree=4),
        v("f74", r"Même filtre, $R=1{,}5$ kΩ, $C=1\,\mu$F. $\omega_c$ (en rad/s) ?", "3/(2*1500*Rational(1,10**6))", "1000", r"$\omega_c=\dfrac3{2RC}=1000$ rad/s.", src=TD + ", filtre 3", duree=2),
        v("f75", r"$v_e$, $R_1=R$ en série, $R_2=R$ et $C$ en parallèle en sortie. $\underline H$ ?", f"(R/(1+I*R*C*w))/(R+R/(1+I*R*C*w))", "1/(2+I*R*C*w)", r"$\dfrac{R/(1+jRC\omega)}{R+R/(1+jRC\omega)}=\dfrac1{2+jRC\omega}$.", src=X26 + ", Q10", duree=3),
        v("f76", r"Même filtre, $R=2$ kΩ, $C=1\,\mu$F. $\omega_c$ (en rad/s) ?", "2/(2000*Rational(1,10**6))", "1000", r"$\dfrac12\cdot\dfrac1{1+j\frac{RC}2\omega}$ : $\omega_c=\dfrac2{RC}=1000$ rad/s.", src=X26 + ", Q11", duree=2),
        o("f77", r"Comment vérifier une fonction de transfert de passe-bas avec l'étude qualitative ?",
          r"On fait tendre $\omega$ vers $0$ et vers l'infini dans $\underline H$ : on doit retrouver $G_{TBF}$ (ici $G_{max}$) et $G_{THF}=0$ trouvés sur les schémas équivalents. Exemple : $\dfrac{5R}{6R+jL\omega}\to\tfrac56$ et $\to0$.", src=TD, duree=3),
    ]},
    {"n": 8, "titre": "Second ordre : passe-bas", "notions": ["ordre2", "ordre1"], "exos": [
        v("f81", r"$v_e$, $L$ et $R$ en série, sortie sur $C$. $\underline H$ ?", f"{_ZC}/({_ZC}+R+I*L*w)", "1/(1+I*R*C*w-L*C*w**2)", r"Diviseur, on multiplie par $jC\omega$ : $\dfrac1{1+jRC\omega-LC\omega^2}$.", src=TD + ", filtre 4", duree=3),
        v("f82", r"Même filtre, $L=10$ mH, $C=1\,\mu$F. $\omega_0$ (en rad/s) ?", "1/sqrt(Rational(1,100)*Rational(1,10**6))", "10000", r"$\omega_0=\dfrac1{\sqrt{LC}}=10^4$ rad/s.", src=TD + ", filtre 4", duree=2),
        v("f83", r"Même filtre : $\sigma$ en fonction de $R$, $L$, $C$ ?", "R*C/2*(1/sqrt(L*C))", "R*C/(2*sqrt(L*C))", r"$2\sigma\dfrac\omega{\omega_0}=RC\omega$ donc $\sigma=\dfrac{RC}2\omega_0=\dfrac{RC}{2\sqrt{LC}}$.", src=TD + ", filtre 4", duree=3),
        v("f84", r"Même filtre, $R=100$ Ω, $L=10$ mH, $C=1\,\mu$F. $\sigma$ ?", "100*Rational(1,10**6)/(2*sqrt(Rational(1,100)*Rational(1,10**6)))", "Rational(1,2)", r"$RC=10^{-4}$, $\sqrt{LC}=10^{-4}$ : $\sigma=0{,}5$.", duree=3),
        v("f85", r"$v_e$, $L$, $R$ en série, puis $R$ et $C$ en parallèle en sortie. $\underline H$ ?", f"(R/(1+I*R*C*w))/(I*L*w+R+R/(1+I*R*C*w))", "R/(2*R+I*R**2*C*w+I*L*w-R*L*C*w**2)", r"$R\parallel C=\dfrac{R}{1+jRC\omega}$, diviseur : $\dfrac{R}{2R+jR^2C\omega+jL\omega-RLC\omega^2}$.", src=TD + ", filtre 7", duree=5),
        v("f86", r"Même filtre : $\omega_0$ en fonction de $L$, $C$ ?", "sqrt(2/(L*C))", "sqrt(2)/sqrt(L*C)", r"$\dfrac12\cdot\dfrac1{1+j\frac12(RC+\frac LR)\omega-\frac{LC}2\omega^2}$ : $\omega_0=\sqrt{\dfrac2{LC}}$, $G_0=\tfrac12$.", src=TD + ", filtre 7", duree=4),
        v("f87", r"Même filtre : $\sigma$ ?", "sqrt(2/(L*C))/4*(R*C+L/R)", "sqrt(2)*(R*C+L/R)/(4*sqrt(L*C))", r"$2\sigma\dfrac\omega{\omega_0}=\dfrac12\left(RC+\dfrac LR\right)\omega$ donc $\sigma=\dfrac{\omega_0}4\left(RC+\dfrac LR\right)$.", src=TD + ", filtre 7", duree=4),
    ]},
    {"n": 9, "titre": "Second ordre : passe-haut", "notions": ["ordre2", "methode"], "exos": [
        v("f91", r"$v_e$, $C$ en série, puis $R$ et $L$ en parallèle en sortie. $\underline H$ ?", f"(I*R*L*w/(R+I*L*w))/({_ZC}+I*R*L*w/(R+I*L*w))", "-R*L*C*w**2/(R+I*L*w-R*L*C*w**2)", r"$R\parallel L=\dfrac{jRL\omega}{R+jL\omega}$, diviseur : $\dfrac{-RLC\omega^2}{R+jL\omega-RLC\omega^2}$.", src=TD + ", filtre 5", duree=4),
        v("f92", r"Même filtre : $\sigma$ en fonction de $R$, $L$, $C$ ?", "L/(2*R)*(1/sqrt(L*C))", "L/(2*R*sqrt(L*C))", r"$\dfrac{-LC\omega^2}{1+j\frac LR\omega-LC\omega^2}$ : $G_0=1$, $\omega_0=\dfrac1{\sqrt{LC}}$, $\sigma=\dfrac{L}{2R\sqrt{LC}}$.", src=TD + ", filtre 5", duree=4),
        v("f93", r"Même filtre, $R=100$ Ω, $L=10$ mH, $C=1\,\mu$F. $\sigma$ ?", "Rational(1,100)/(2*100*sqrt(Rational(1,100)*Rational(1,10**6)))", "Rational(1,2)", r"$\dfrac{0{,}01}{200\times10^{-4}}=0{,}5$.", duree=3),
        v("f94", r"$v_e$, $C$ en série, $R$ en parallèle, puis $R$ en série et $L$ en sortie. Norton puis Thévenin : $\underline E_{th}/\underline V_E$ ?", f"R/(R+{_ZC})", "I*R*C*w/(1+I*R*C*w)", r"Source $jC\omega\underline V_E$ en parallèle avec $\dfrac{R}{1+jRC\omega}$ : $\underline E_{th}=\dfrac{jRC\omega}{1+jRC\omega}\underline V_E$.", src=TD + ", filtre 8", duree=4),
        v("f95", r"Même filtre : $\underline H$ ?", "(I*L*w/(R/(1+I*R*C*w)+R+I*L*w))*(I*R*C*w/(1+I*R*C*w))", "-R*L*C*w**2/(2*R+I*R**2*C*w+I*L*w-R*L*C*w**2)", r"Diviseur sur $jL\omega$ avec $\underline Z_{th}=\dfrac{R}{1+jRC\omega}+R$ : $\dfrac{-RLC\omega^2}{2R+jR^2C\omega+jL\omega-RLC\omega^2}$.", src=TD + ", filtre 8", duree=5),
        v("f96", r"Même filtre : $G_0=G_{THF}$ ?", "1", "1", r"$\dfrac{-\frac{LC}2\omega^2}{1+\dots-\frac{LC}2\omega^2}\to1$ : $G_0=1$, $\omega_0=\sqrt{\dfrac2{LC}}$.", src=TD + ", filtre 8", duree=3),
        o("f97", r"À quoi reconnaît-on un passe-haut du second ordre sur sa forme normalisée ?",
          r"Numérateur $-G_0\left(\dfrac\omega{\omega_0}\right)^2$ : le gain tend vers $0$ en TBF (en $\omega^2$, $+40$ dB/décade) et vers $G_0$ en THF.", src=COURS, duree=3),
    ]},
    {"n": 10, "titre": "Second ordre : passe-bande", "notions": ["ordre2", "coupure"], "exos": [
        v("fa1", r"$v_e$, $R$ en série, puis $C$ et $L$ en parallèle en sortie. $\underline H$ ?", "(I*L*w/(1-L*C*w**2))/(R+I*L*w/(1-L*C*w**2))", "I*L*w/(R+I*L*w-R*L*C*w**2)", r"$C\parallel L=\dfrac{jL\omega}{1-LC\omega^2}$, diviseur : $\dfrac{jL\omega}{R+jL\omega-RLC\omega^2}$.", src=TD + ", filtre 6", duree=4),
        v("fa2", r"Même filtre : gain à $\omega_0=1/\sqrt{LC}$ ?", "abs((I*L/sqrt(L*C))/(R+I*L/sqrt(L*C)-R))", "1", r"À $\omega_0$, $RLC\omega_0^2=R$ : $\underline H=\dfrac{jL\omega_0}{jL\omega_0}=1=G_0$.", src=TD + ", filtre 6", duree=3),
        v("fa3", r"Même filtre : $\sigma$ ?", "L/(2*R)*(1/sqrt(L*C))", "L/(2*R*sqrt(L*C))", r"$\dfrac{j\frac LR\omega}{1+j\frac LR\omega-LC\omega^2}$ : $2\sigma\dfrac\omega{\omega_0}=\dfrac LR\omega$, $\sigma=\dfrac{L}{2R\sqrt{LC}}$.", src=TD + ", filtre 6", duree=3),
        v("fa4", r"Bonus 2 : $R_2$, $L$, $C$ en parallèle. Admittance $\underline Y_{eq}$ ?", "1/R2+1/(I*L*w)+I*C*w", "1/R2+I*(C*w-1/(L*w))", r"$\underline Y_{eq}=\dfrac1{R_2}+\dfrac1{jL\omega}+jC\omega=\dfrac1{R_2}+j\left(C\omega-\dfrac1{L\omega}\right)$.", src=TD + ", bonus 2", duree=3),
        v("fa5", r"Bonus 2 : $v_e$, $R_1$ en série, $(R_2,L,C)$ en parallèle en sortie. Gain maximal en fonction de $R_1$, $R_2$ ?", "1/(1+R1/R2)", "R2/(R1+R2)", r"$\underline H=\dfrac1{1+R_1\underline Y_{eq}}$, maximal quand $C\omega=\dfrac1{L\omega}$ : $G_{max}=\dfrac{R_2}{R_1+R_2}$.", src=TD + ", bonus 2", duree=4),
        v("fa6", r"Bonus 2 : $R_1=1$ kΩ, $G_{max}=-9$ dB. $R_2$ (en Ω, valeur exacte) ?", "1000/(10**Rational(45,100)-1)", "1000/(10**Rational(9,20)-1)", r"$\dfrac{R_1+R_2}{R_2}=10^{0{,}45}\approx2{,}82$ donc $R_2=\dfrac{R_1}{10^{0{,}45}-1}\approx550$ Ω.", src=TD + ", bonus 2", duree=4),
        o("fa7", r"Pourquoi le gain du bonus 2 est-il maximal pour $\omega_0=1/\sqrt{LC}$ ?",
          r"$G=\dfrac1{\sqrt{\left(1+\frac{R_1}{R_2}\right)^2+R_1^2\left(C\omega-\frac1{L\omega}\right)^2}}$ : le premier terme est constant, le second est positif et s'annule pour $C\omega=\dfrac1{L\omega}$, soit $\omega_0=\dfrac1{\sqrt{LC}}$.", src=TD + ", bonus 2", duree=5),
    ]},
    {"n": 11, "titre": "Méthode complète : Thévenin et forme normalisée", "notions": ["methode", "ordre2"], "exos": [
        v("fb1", r"$v_e$, $R$ en série, $C$ en parallèle, puis $L$ en série et $R$ en sortie. $\underline E_{th}/\underline V_E$ vu par la résistance de sortie (avec $L$) ?", f"{_ZC}/(R+{_ZC})", "1/(1+I*R*C*w)", r"Norton $\dfrac{\underline V_E}R$, $R\parallel C=\dfrac{R}{1+jRC\omega}$, retour en Thévenin : $\underline E_{th}=\dfrac{\underline V_E}{1+jRC\omega}$.", src=X26 + ", ex. 2", duree=4),
        v("fb2", r"Même circuit : $\underline Z_{th}$ ?", "R/(1+I*R*C*w)+I*L*w", "R/(1+I*R*C*w)+I*L*w", r"$\underline Z_{th}=\dfrac{R}{1+jRC\omega}+jL\omega$.", src=X26 + ", ex. 2", duree=3),
        v("fb3", r"Même circuit : $\underline H=\underline V_S/\underline V_E$ ?", "(R/(R/(1+I*R*C*w)+I*L*w+R))*(1/(1+I*R*C*w))", "R/(2*R+I*(L+R**2*C)*w-R*L*C*w**2)", r"$\dfrac{R}{\underline Z_{th}+R}\cdot\dfrac1{1+jRC\omega}=\dfrac{R}{2R+j(L+R^2C)\omega-RLC\omega^2}$.", src=X26 + ", ex. 2", duree=5),
        v("fb4", r"Même circuit, $L=2$ mH, $C=1\,\mu$F. $\omega_0=\sqrt{2/(LC)}$ (en rad/s) ?", "sqrt(2/(Rational(2,1000)*Rational(1,10**6)))", "10**Rational(9,2)", r"$LC=2\times10^{-9}$, $\omega_0=\sqrt{10^9}\approx31\,623$ rad/s.", duree=3),
        v("fb5", r"$R=100$ Ω, $L=10$ mH, $C=1\,\mu$F, $\omega_0=\sqrt2\cdot10^4$ rad/s. $\sigma=\dfrac{\omega_0}4\left(RC+\dfrac LR\right)$ ?", "sqrt(2)*10**4/4*(100*Rational(1,10**6)+Rational(1,100)/100)", "sqrt(2)/2", r"$RC+\dfrac LR=2\times10^{-4}$ s ; $\sigma=\dfrac{\sqrt2\cdot10^4}4\times2\times10^{-4}=\dfrac{\sqrt2}2\approx0{,}71$.", duree=4),
        o("fb6", r"Décrire la méthode d'étude complète d'un filtre (étapes, vérifications).",
          r"1. Schémas TBF et THF : gains limites et nature. 2. Représentation complexe. 3. Réduction (associations, Thévenin/Norton). 4. Pont diviseur : $\underline H$. 5. Forme normalisée : $G_{max}$, $\omega_c$ (ordre 1) ou $G_0$, $\omega_0$, $\sigma$ (ordre 2). Vérifier que les limites de $\underline H$ redonnent les gains de l'étape 1.", src=COURS, duree=5),
        v("fb7", r"Filtre $\underline H=\dfrac{R}{2R+j(L+R^2C)\omega-RLC\omega^2}$ : $G_0$ ?", "limit(R/(2*R+I*(L+R**2*C)*w-R*L*C*w**2), w, 0)", "Rational(1,2)", r"En TBF : $\dfrac{R}{2R}=\tfrac12$ (on retrouve l'étude qualitative).", src=X26 + ", ex. 2", duree=2),
    ]},
    {"n": 12, "titre": "Niveau examen : contrôle B3 mars 2026", "notions": ["limites", "nature", "ordre1", "ordre2", "methode"], "examen": True, "exos": [
        o("xc1", r"Exercice 1, Q1-Q6 : $\underline Z_C$, $\underline Z_L$, bobine en TBF, condensateur en THF ; « un filtre amplifie ou atténue selon la fréquence » ; « un filtre contient au moins un condensateur ou une bobine ».",
          r"$\underline Z_C=\dfrac1{jC\omega}$, $\underline Z_L=jL\omega$ ; bobine en TBF : un fil ; condensateur en THF : un interrupteur fermé ; vrai ; vrai.", src=X26 + ", ex. 1 (7 points)", duree=5),
        o("xc2", r"Exercice 1, Q7-Q9 : $v_e$, $R_1$ en série, $R_2\parallel C$ en sortie, $R_1=R_2=R$. Nature, gain en THF, gain en TBF ?",
          r"Passe-bas. THF : $C$ fil, $G\to0$. TBF : $C$ ouvert, $G=\dfrac{R}{2R}=\tfrac12$.", src=X26 + ", ex. 1", duree=4),
        v("xc3", r"Exercice 1, Q10 : $\underline H$ ?", f"(R/(1+I*R*C*w))/(R+R/(1+I*R*C*w))", "1/(2+I*R*C*w)", r"$\underline H=\dfrac1{2+jRC\omega}$.", src=X26 + ", ex. 1", duree=3),
        v("xc4", r"Exercice 1, Q11 : $\omega_c$ avec $R=1$ kΩ, $C=2\,\mu$F (en rad/s) ?", "2/(1000*Rational(2,10**6))", "1000", r"$\omega_c=\dfrac2{RC}=1000$ rad/s ; Q12 : $R_2$ remplacée par une bobine donne un passe-bande.", src=X26 + ", ex. 1", duree=3),
        o("xc5", r"Exercice 2 (qualitatif) : $v_e$, $R$ en série, $C$ en parallèle, $L$ en série, $R$ en sortie. Gains limites, nature, filtre obtenu en inversant $L$ et $C$.",
          r"TBF : $C$ ouvert, $L$ fil, $G\to\tfrac12$. THF : $C$ fil, $G\to0$. Passe-bas (ordre $2$). En inversant $L$ et $C$, TBF et THF s'inversent : passe-haut.", src=X26 + ", ex. 2 (13 points)", duree=8),
        v("xc6", r"Exercice 2 (quantitatif) : $\underline H$ ?", "(R/(R/(1+I*R*C*w)+I*L*w+R))*(1/(1+I*R*C*w))", "R/(2*R+I*(L+R**2*C)*w-R*L*C*w**2)", r"$\underline E_{th}=\dfrac{\underline V_E}{1+jRC\omega}$, $\underline Z_{th}=\dfrac R{1+jRC\omega}+jL\omega$, diviseur : $\dfrac{R}{2R+j(L+R^2C)\omega-RLC\omega^2}$.", src=X26 + ", ex. 2", duree=10),
        v("xc7", r"Exercice 2 : $\sigma$ en fonction de $R$, $L$, $C$ ?", "sqrt(2/(L*C))/4*(L/R+R*C)", "sqrt(2)*(L/R+R*C)/(4*sqrt(L*C))", r"$\dfrac12\cdot\dfrac1{1+j\frac12\left(\frac LR+RC\right)\omega-\frac{LC}2\omega^2}$ : $G_0=\tfrac12$, $\omega_0=\sqrt{\dfrac2{LC}}$, $\sigma=\dfrac{\omega_0}4\left(\dfrac LR+RC\right)$.", src=X26 + ", ex. 2", duree=8),
    ]},
]


def _v(enonce, calc, ans, sol):
    return {"enonce": enonce, "calc": calc, "ans": ans, "sol": sol}


VARIANTS = {
    "f11": [_v(r"$V_E=12$ V et $V_S=3$ V. Gain $G$ ?", "Rational(3,12)", "Rational(1,4)", r"$G=0{,}25$.")],
    "f12": [_v(r"$G=1000$. $G_{dB}$ ?", "20*log(1000,10)", "60", r"$20\times3=60$ dB.")],
    "f14": [_v(r"$G_{dB}=-60$ dB. Gain $G$ ?", "10**(-3)", "Rational(1,1000)", r"$G=10^{-3}$.")],
    "f22": [_v(r"$v_e$, $2R$ et $C$ en série, sortie sur $R$. Gain en THF ?", "R/(2*R+R)", "Rational(1,3)", r"$\dfrac{R}{3R}=\tfrac13$.")],
    "f24": [_v(r"$v_e$, $R$ et $L$ en série, sortie sur $3R$. Gain en TBF ?", "3*R/(R+3*R)", "Rational(3,4)", r"$\tfrac34$.")],
    "f54": [_v(r"Passe-bande : $f_{cb}=450$ Hz, $f_{ch}=550$ Hz. Largeur de la bande passante (en Hz) ?", "550-450", "100", r"$100$ Hz.")],
    "f63": [_v(r"Même filtre, $R=500$ Ω, $C=1\,\mu$F. $\omega_c$ (en rad/s) ?", "1/(4*500*Rational(1,10**6))", "500", r"$\dfrac1{4RC}=500$ rad/s.")],
    "f66": [_v(r"$v_e$, $C$ en série, $R$ en sortie. $\omega_c$ avec $R=1$ kΩ, $C=10\,\mu$F (en rad/s) ?", "1/(1000*Rational(10,10**6))", "100", r"$\dfrac1{RC}=100$ rad/s.")],
    "f72": [_v(r"Même filtre, $R=50$ Ω, $L=0{,}3$ H. $\omega_c$ (en rad/s) ?", "6*50/Rational(3,10)", "1000", r"$\dfrac{6R}{L}=1000$ rad/s.")],
    "f76": [_v(r"Même filtre, $R=1$ kΩ, $C=1\,\mu$F. $\omega_c$ (en rad/s) ?", "2/(1000*Rational(1,10**6))", "2000", r"$\dfrac2{RC}=2000$ rad/s.")],
    "f82": [_v(r"Même filtre, $L=1$ mH, $C=100$ nF. $\omega_0$ (en rad/s) ?", "1/sqrt(Rational(1,1000)*Rational(1,10**7))", "100000", r"$LC=10^{-10}$, $\omega_0=10^5$ rad/s.")],
    "f84": [_v(r"Même filtre, $R=200$ Ω, $L=10$ mH, $C=1\,\mu$F. $\sigma$ ?", "200*Rational(1,10**6)/(2*sqrt(Rational(1,100)*Rational(1,10**6)))", "1", r"$RC=2\times10^{-4}$, $\sigma=1$.")],
    "f93": [_v(r"Même filtre, $R=50$ Ω, $L=10$ mH, $C=1\,\mu$F. $\sigma$ ?", "Rational(1,100)/(2*50*sqrt(Rational(1,100)*Rational(1,10**6)))", "1", r"$\dfrac{0{,}01}{100\times10^{-4}}=1$.")],
    "xc4": [_v(r"Exercice 1, Q11 : $\omega_c$ avec $R=4$ kΩ, $C=1\,\mu$F (en rad/s) ?", "2/(4000*Rational(1,10**6))", "500", r"$\dfrac2{RC}=500$ rad/s.")],
}
for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["id"] in VARIANTS:
            _e["variants"] = VARIANTS[_e["id"]]


EXTRA_PARTS = []

QUIZ = [
    {"notion": "ft", "type": "qcm", "q": r"Le gain $G(\omega)$ est :", "choix": [r"$|\underline H(\omega)|$", r"$\arg\underline H(\omega)$", r"$20\log\underline H$", r"$\underline V_E/\underline V_S$"], "bonne": 0},
    {"notion": "ft", "type": "vf", "q": r"Un filtre contient au moins un condensateur ou une bobine.", "bonne": True},
    {"notion": "limites", "type": "qcm", "q": r"En très hautes fréquences, un condensateur équivaut à :", "choix": [r"un interrupteur fermé", r"un interrupteur ouvert", r"une résistance", r"un générateur de tension"], "bonne": 0},
    {"notion": "limites", "type": "vf", "q": r"En très basses fréquences, une bobine équivaut à un interrupteur ouvert.", "bonne": False},
    {"notion": "nature", "type": "qcm", "q": r"Gain croissant puis décroissant :", "choix": [r"passe-bande", r"coupe-bande", r"passe-haut", r"passe-bas"], "bonne": 0},
    {"notion": "nature", "type": "vf", "q": r"Un filtre à $1$ condensateur et $2$ bobines est d'ordre $3$.", "bonne": True},
    {"notion": "bode", "type": "qcm", "q": r"Pente de l'asymptote d'un filtre d'ordre $2$ :", "choix": [r"$\pm40$ dB/décade", r"$\pm20$ dB/décade", r"$\pm6$ dB/décade", r"$\pm3$ dB/décade"], "bonne": 0},
    {"notion": "bode", "type": "vf", "q": r"Un gain de $-20$ dB correspond à $G=0{,}1$.", "bonne": True},
    {"notion": "coupure", "type": "qcm", "q": r"À la fréquence de coupure, le gain vaut :", "choix": [r"$G_{max}/\sqrt2$", r"$G_{max}/2$", r"$0$", r"$G_{max}-3$"], "bonne": 0},
    {"notion": "coupure", "type": "vf", "q": r"Au-delà de la fréquence de coupure, le signal ne passe plus du tout.", "bonne": False},
    {"notion": "ordre1", "type": "qcm", "q": r"Pour un passe-haut du premier ordre, $G_{max}$ vaut :", "choix": [r"$G_{THF}$", r"$G_{TBF}$", r"$G(\omega_c)$", r"$0$"], "bonne": 0},
    {"notion": "ordre1", "type": "vf", "q": r"$\dfrac1{2+jRC\omega}$ a pour pulsation de coupure $\omega_c=\dfrac2{RC}$.", "bonne": True},
    {"notion": "ordre2", "type": "qcm", "q": r"$\dfrac1{1+jRC\omega-LC\omega^2}$ a pour pulsation propre :", "choix": [r"$\dfrac1{\sqrt{LC}}$", r"$\dfrac1{RC}$", r"$\sqrt{LC}$", r"$\dfrac{R}{L}$"], "bonne": 0},
    {"notion": "ordre2", "type": "vf", "q": r"Pour un passe-bande, le gain est maximal à $\omega_0$ et vaut $G_0$.", "bonne": True},
    {"notion": "methode", "type": "qcm", "q": r"Première étape de l'étude d'un filtre :", "choix": [r"l'étude en TBF et en THF", r"la forme normalisée", r"le diagramme de Bode", r"le calcul de $\sigma$"], "bonne": 0},
    {"notion": "methode", "type": "vf", "q": r"Les limites de $\underline H$ en $0$ et en $+\infty$ doivent redonner les gains de l'étude qualitative.", "bonne": True},
]

_F = r"$\underline H=\underline V_S/\underline V_E$ · $G=|\underline H|$ · $G_{dB}=20\log G$ · $\arg\underline H$ : déphasage"
_L = r"TBF : $C\to$ ouvert, $L\to$ fil · THF : $C\to$ fil, $L\to$ ouvert"
_D = r"diviseur : $\underline V_S=\dfrac{\underline Z_S}{\underline Z_1+\underline Z_S}\underline V_E$"
_N = r"passe-bas : $G\searrow$ · passe-haut : $G\nearrow$ · passe-bande : $\nearrow\searrow$ · ordre $=$ nombre de $L$ et $C$"
_B = r"$G_{dB}=20\log G$ · pente $\pm20n$ dB/décade · déphasage total $n\pi/2$"
_C = r"$G(\omega_c)=G_{max}/\sqrt2$ · $-3$ dB · $f=\omega/(2\pi)$ · bande passante $f_{ch}-f_{cb}$"
_1 = r"$G_{max}\dfrac1{1+j\omega/\omega_c}$ · $G_{max}\dfrac{j\omega/\omega_c}{1+j\omega/\omega_c}$"
_2 = r"$1+2j\sigma\dfrac\omega{\omega_0}-\left(\dfrac\omega{\omega_0}\right)^2$ · $\left(\dfrac\omega{\omega_0}\right)^2=$ terme en $\omega^2$"
_P = r"$R\parallel C=\dfrac{R}{1+jRC\omega}$ · $R\parallel L=\dfrac{jRL\omega}{R+jL\omega}$ · $L\parallel C=\dfrac{jL\omega}{1-LC\omega^2}$"
_T = r"Norton $\underline V_E/\underline Z$ $\leftrightarrow$ Thévenin · $\underline E_{th}$ à vide · $\underline Z_{th}$ sources éteintes"

FORMULES = {
    "f11": _F, "f12": _F, "f13": _F, "f14": _F, "f15": _F, "f16": _F, "f17": _F,
    "f21": _L, "f22": _L + " · " + _D, "f23": _L, "f24": _L + " · " + _D, "f25": _L + " · " + _D, "f26": _L + " · " + _D, "f27": _L,
    "f31": _N + " · " + _L, "f32": _N + " · " + _L, "f33": _N + " · " + _L, "f34": _N, "f35": _N + " · " + _L, "f36": _N + " · " + _L, "f37": _N + " · " + _1,
    "f41": _B, "f42": _B, "f43": _B, "f44": _B, "f45": _B + " · " + _D, "f46": _B, "f47": _B,
    "f51": _C, "f52": _C + " · " + _B, "f53": _C, "f54": _C, "f55": _C, "f56": _C + r" · $\omega_0=1/\sqrt{LC}$", "f57": _C + " · " + _B,
    "f61": _D + " · " + _1, "f62": _1, "f63": _1, "f64": _1, "f65": _1 + " · " + _B, "f66": _1, "f67": _1,
    "f71": _D + " · " + _1, "f72": _1, "f73": _P + " · " + _D, "f74": _1, "f75": _P + " · " + _D, "f76": _1, "f77": _1 + " · " + _L,
    "f81": _D + " · " + _2, "f82": _2, "f83": _2, "f84": _2, "f85": _P + " · " + _D, "f86": _2, "f87": _2,
    "f91": _P + " · " + _D, "f92": _2, "f93": _2, "f94": _T + " · " + _P, "f95": _T + " · " + _D, "f96": _2, "f97": _2,
    "fa1": _P + " · " + _D, "fa2": _2, "fa3": _2, "fa4": r"$\underline Y=1/\underline Z$ · parallèle : $\underline Y=\sum\underline Y_i$", "fa5": _D, "fa6": _B, "fa7": _2,
    "fb1": _T + " · " + _P, "fb2": _T, "fb3": _D + " · " + _T, "fb4": _2, "fb5": _2, "fb6": _L + " · " + _D + " · " + _1 + " · " + _2, "fb7": _L,
    "xc1": _L, "xc2": _L + " · " + _N, "xc3": _P + " · " + _D, "xc4": _1, "xc5": _L + " · " + _N, "xc6": _T + " · " + _D, "xc7": _2,
}


# ---------------------------------------------------------------- circuit figures (`schema.py`)

def _s(*br):
    return schema_echelle("v_e(t)", list(br), "v_s(t)")


S, P = "s", "p"
FIG_3RC = _s((S, "R", "3R"), (S, "C", "C"), (P, "R", "R"))
FIG_RL5 = _s((S, "R", "R"), (S, "L", "L"), (P, "R", "5R"))
FIG_R2RC = _s((S, "R", "R"), (P, "R", "2R"), (P, "C", "C"))
FIG_R1R2C = _s((S, "R", "R_1"), (P, "R", "R_2"), (P, "C", "C"))
FIG_LRC = _s((S, "L", "L"), (S, "R", "R"), (P, "C", "C"))
FIG_CRL = _s((S, "C", "C"), (P, "R", "R"), (P, "L", "L"))
FIG_RCL = _s((S, "R", "R"), (P, "C", "C"), (P, "L", "L"))
FIG_EX2 = (_s((S, "R", "R"), (P, "C", "C"), (S, "L", "L"), (P, "R", "R")) + "\n\n"
           + schema_echelle("\\underline{E}_{th}", [(S, "Z", "\\underline{Z}_{th}"), (P, "R", "R")], "\\underline{V}_S"))
FIG_LRRC = _s((S, "L", "L"), (S, "R", "R"), (P, "R", "R"), (P, "C", "C"))
FIG_CRRL = _s((S, "C", "C"), (P, "R", "R"), (S, "R", "R"), (P, "L", "L"))
FIG_R1RLC = _s((S, "R", "R_1"), (P, "R", "R_2"), (P, "L", "L"), (P, "C", "C"))
FIG_CR = _s((S, "C", "C"), (P, "R", "R"))

FIGS = {**dict.fromkeys(["f22", "f23", "f31", "f61", "f62", "f63"], FIG_3RC),
        **dict.fromkeys(["f24", "f71", "f72"], FIG_RL5),
        **dict.fromkeys(["f25", "f73", "f74"], FIG_R2RC),
        **dict.fromkeys(["f26", "f35", "f75", "f76", "xc2", "xc3", "xc4"], FIG_R1R2C),
        **dict.fromkeys(["f27", "f81", "f82", "f83", "f84"], FIG_LRC),
        **dict.fromkeys(["f32", "f91", "f92", "f93"], FIG_CRL),
        **dict.fromkeys(["f33", "fa1", "fa2", "fa3"], FIG_RCL),
        **dict.fromkeys(["f36", "fb1", "fb2", "fb3", "fb4", "xc5", "xc6", "xc7"], FIG_EX2),
        **dict.fromkeys(["f85", "f86", "f87"], FIG_LRRC),
        **dict.fromkeys(["f94", "f95", "f96"], FIG_CRRL),
        "fa5": FIG_R1RLC, "f66": FIG_CR}
ajoute(LEVELS, FIGS)
