"""Level path: S1 electronics B2 (January), linear networks in sinusoidal steady state and filters, promo 2031.

Calibrated on the Moodle course « S1 - Electronique - Promo 2030 » (`Kit de Survie Régime Sinusoïdal`), TD 4 (réseaux
linéaires en régime sinusoïdal forcé, with its correction) and the B2 exams of January 2025 (`Examen B2 Elec`, filters)
and January 2026 (`Examen 2 Elec`). Circuits are described in words and drawn as SVG (`schema.py`, `FIGS` at the end).
Symbolic answers use the sympy symbols R, L, C, w (w = omega) and I (imaginary unit j); they are compared at sample points.
"""
from .schema import Fil, Point, R, SrcI, SrcU, ajoute, courant, fig, schema_echelle, tension


SUBJECT = {
    "id": "elec-s1-sinus",
    "ordre": 510,
    "matiere": "electronique",
    "semestre": "S1",
    "ecue": "Outils d'analyse de circuits",
    "titre": "Régime sinusoïdal forcé et filtres",
    "chapitres_moodle": ["01_Outils d'analyse de circuits - Définitions, Lois et Théorèmes [2526_I_INF_FISE_S01_CN_OAC]", "02_Documents de cours", "05_Travaux Dirigés"],
    "td": "TD 4 d'électronique S1 (réseaux linéaires en régime sinusoïdal forcé)",
    "examens": ["Examen B2 d'électronique (janvier 2025)", "Examen 2 d'électronique (janvier 2026)"],
}

NOTIONS = [
    {"id": "amplitude", "titre": "Signal sinusoïdal et amplitude complexe",
     "formule": r"$s(t)=S\sqrt2\sin(\omega t+\varphi)$ · $S$ : valeur efficace · $\omega=2\pi f=\dfrac{2\pi}T$ · $\underline S=S\,e^{j\varphi}$ : $|\underline S|=S$, $\arg\underline S=\varphi$ · $e^{j\theta}=\cos\theta+j\sin\theta$ · $\cos(\omega t)=\sin(\omega t+\tfrac\pi2)$",
     "exemple": r"$i(t)=I\sqrt2\cos(\omega t)=I\sqrt2\sin(\omega t+\tfrac\pi2)$ : $\underline I=I\,e^{j\pi/2}=jI$",
     "cours": r"Une grandeur sinusoïdale de pulsation connue est entièrement décrite par sa valeur efficace et sa phase à l'origine : on la représente par un nombre complexe, son amplitude complexe. Tous les signaux d'un circuit doivent être écrits avec la même fonction (tout en sinus ou tout en cosinus) avant de passer en complexe."},
    {"id": "impedances", "titre": "Impédances complexes",
     "formule": r"$\underline Z=\dfrac{\underline U}{\underline I}$ (convention récepteur) · $\underline Z_R=R$ · $\underline Z_L=jL\omega$ · $\underline Z_C=\dfrac1{jC\omega}=-\dfrac{j}{C\omega}$ · $|\underline Z|=\dfrac UI$ · $\arg\underline Z$ : déphasage de $u$ par rapport à $i$ · $L\omega$ en ohms, $C\omega$ en siemens",
     "exemple": r"$L=20$ mH, $\omega=500$ rad/s : $\underline Z_L=10j$ Ω, $\arg=+90°$",
     "cours": r"L'impédance d'un dipôle passif linéaire est le quotient des amplitudes complexes de sa tension et de son courant. Son module est le quotient des valeurs efficaces, son argument le déphasage de la tension sur le courant : $0$ pour une résistance, $+\tfrac\pi2$ pour une bobine, $-\tfrac\pi2$ pour un condensateur."},
    {"id": "associations", "titre": "Associations d'impédances",
     "formule": r"série : $\underline Z=\underline Z_1+\underline Z_2$ · parallèle : $\underline Z=\dfrac{\underline Z_1\underline Z_2}{\underline Z_1+\underline Z_2}$ · $R\parallel C$ : $\dfrac{R}{1+jRC\omega}$ · $L\parallel C$ : $\dfrac{jL\omega}{1-LC\omega^2}$ · $R\parallel L$ : $\dfrac{jRL\omega}{R+jL\omega}$",
     "exemple": r"$R=3$ Ω, $L\omega=8$ Ω, $\tfrac1{C\omega}=4$ Ω en série : $\underline Z=3+4j$, $|\underline Z|=5$ Ω",
     "cours": r"Les règles d'association des résistances restent valables avec des impédances complexes. On simplifie en multipliant numérateur et dénominateur pour faire disparaître les fractions emboîtées ($j^2=-1$)."},
    {"id": "ohm_c", "titre": "Loi d'Ohm généralisée",
     "formule": r"$\underline U=\underline Z\,\underline I$ · $U=|\underline Z|\,I$ (valeurs efficaces) · $\arg\underline I=\arg\underline U-\arg\underline Z$ · $i(t)=|\underline I|\sqrt2\sin(\omega t+\arg\underline I)$ · les valeurs efficaces ne s'additionnent pas",
     "exemple": r"$E=20$ V, $R=L\omega=10$ Ω en série : $|\underline I|=\dfrac{20}{10\sqrt2}=\sqrt2$ A, en retard de $45°$",
     "cours": r"En représentation complexe, toutes les lois du continu (Ohm, nœuds, mailles) s'écrivent avec les amplitudes complexes et les impédances. On revient au signal réel en prenant le module (valeur efficace) et l'argument (phase à l'origine). Les lois des mailles s'appliquent aux complexes, pas aux valeurs efficaces : $3$ V sur $R$ et $4$ V sur $L$ donnent $5$ V au total."},
    {"id": "diviseur_c", "titre": "Diviseur de tension en complexe",
     "formule": r"$\underline U_2=\dfrac{\underline Z_2}{\underline Z_1+\underline Z_2}\underline E$ (même courant, pas de courant de sortie) · RC, sortie sur $C$ : $\dfrac{1}{1+jRC\omega}$ · RL, sortie sur $L$ : $\dfrac{jL\omega}{R+jL\omega}$",
     "exemple": r"RC avec $RC\omega=1$ : $\left|\dfrac{\underline U}{\underline E}\right|=\dfrac1{\sqrt2}$, déphasage $-45°$",
     "cours": r"Le pont diviseur de tension s'applique tel quel à des impédances en série. C'est l'outil principal pour calculer une tension de sortie, souvent après avoir réduit le reste du circuit par associations ou par Thévenin/Norton."},
    {"id": "thevenin_c", "titre": "Thévenin et Norton en complexe",
     "formule": r"$\underline E_{th}$ : tension à vide · $\underline Z_{th}$ : impédance vue des bornes, sources éteintes · $\underline I_N=\dfrac{\underline E_{th}}{\underline Z_{th}}$ · $(\underline E,\underline Z)$ série $\leftrightarrow$ $(\underline E/\underline Z,\underline Z)$ parallèle",
     "exemple": r"$v_e$, $2R$ en série, $C$ en parallèle : $\underline E_{th}=\dfrac{\underline V_E}{1+2jRC\omega}$, $\underline Z_{th}=\dfrac{2R}{1+2jRC\omega}$",
     "cours": r"Les équivalences de Thévenin et de Norton s'enchaînent comme en continu, avec des impédances. On transforme une source de tension avec son impédance série en source de courant avec la même impédance en parallèle, on associe les impédances en parallèle, puis on revient en Thévenin."},
    {"id": "limites", "titre": "Très basses et très hautes fréquences",
     "formule": r"TBF ($\omega\to0$) : condensateur $\to$ circuit ouvert, bobine $\to$ fil · THF ($\omega\to\infty$) : condensateur $\to$ fil, bobine $\to$ circuit ouvert · $A$ décroissante : passe-bas · croissante : passe-haut · nulle aux deux bouts : passe-bande",
     "exemple": r"$C$ en série, $4R\parallel L$ en sortie : TBF $A\to0$, THF $A\to1$, passe-haut",
     "cours": r"L'étude qualitative d'un filtre remplace chaque condensateur et chaque bobine par son comportement limite, puis calcule l'amplification sur le schéma simplifié (souvent un diviseur de résistances). Comparer les deux limites donne la nature du filtre."},
    {"id": "transfert", "titre": "Fonction de transfert, amplification, gain",
     "formule": r"$\underline T(\omega)=\dfrac{\underline V_S}{\underline V_E}$ · amplification $A(\omega)=|\underline T(\omega)|=\dfrac{V_S}{V_E}$ (valeurs efficaces) · gain $G=20\log_{10}A$ en dB · $\arg\underline T$ : déphasage de $v_s$ par rapport à $v_e$",
     "exemple": r"$A=\dfrac1{\sqrt2}$ : $G=-10\log_{10}2\approx-3$ dB",
     "cours": r"La fonction de transfert est le quotient des amplitudes complexes de sortie et d'entrée. Son module est l'amplification (quotient des valeurs efficaces), son argument le déphasage de la sortie sur l'entrée. Le gain est l'amplification en décibels."},
    {"id": "ordre1", "titre": "Filtres du premier ordre",
     "formule": r"passe-bas : $\underline T=A_{max}\dfrac1{1+j\frac\omega{\omega_c}}$, $A_{max}=A_{TBF}$ · passe-haut : $\underline T=A_{max}\dfrac{j\frac\omega{\omega_c}}{1+j\frac\omega{\omega_c}}$, $A_{max}=A_{THF}$ · $A(\omega_c)=\dfrac{A_{max}}{\sqrt2}$ · $f_c=\dfrac{\omega_c}{2\pi}$",
     "exemple": r"$\underline T=\dfrac{R}{5R+jL\omega}=\dfrac15\cdot\dfrac1{1+j\frac{L}{5R}\omega}$ : $A_{max}=\tfrac15$, $\omega_c=\dfrac{5R}L$",
     "cours": r"On met la fonction de transfert sous forme normalisée en factorisant le terme réel du dénominateur, puis on identifie avec la forme du cours. À la pulsation de coupure, l'amplification vaut $A_{max}/\sqrt2$, soit un gain de $3$ dB sous le maximum."},
    {"id": "ordre2", "titre": "Filtres du second ordre",
     "formule": r"dénominateur $1+2j\sigma\dfrac\omega{\omega_0}-\left(\dfrac\omega{\omega_0}\right)^2$ · passe-bas : numérateur $A_0$ · passe-haut : $-A_0\left(\frac\omega{\omega_0}\right)^2$ · passe-bande : $A_0\,2j\sigma\frac\omega{\omega_0}$ · $\omega_0$ : pulsation propre · $\sigma$ : coefficient d'amortissement",
     "exemple": r"$\underline T=\dfrac{-LC\omega^2}{1+j\frac{L}{4R}\omega-LC\omega^2}$ : $\omega_0=\dfrac1{\sqrt{LC}}$, $\sigma=\dfrac{L}{8R}\omega_0$",
     "cours": r"On identifie le terme en $\omega^2$ du dénominateur pour obtenir $\omega_0$ ($LC\omega^2=(\omega/\omega_0)^2$), puis le terme en $j\omega$ pour obtenir $\sigma$. La forme du numérateur donne la nature du filtre."},
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


X25 = "Examen B2 d'électronique, janvier 2025"
X26 = "Examen 2 d'électronique, janvier 2026"
TD4 = "TD 4 d'électronique (régime sinusoïdal forcé)"
KIT = "Kit de survie régime sinusoïdal"

# shared circuit expressions (sympy strings): R // L, the TD4 ex. 3 output voltage over E
_RL = "(I*R*L*w/(R+I*L*w))"
_ZC = "(1/(I*C*w))"

LEVELS = [
    {"n": 1, "titre": "Amplitude complexe", "notions": ["amplitude"], "exos": [
        v("s11", r"$u(t)=5\sqrt2\sin(\omega t+\tfrac\pi3)$ (en V). Module de $\underline U$ (en V) ?", "5", "5", r"$|\underline U|$ est la valeur efficace : $5$ V.", src=KIT, duree=1),
        v("s12", r"Même tension. Argument de $\underline U$ (en rad) ?", "pi/3", "pi/3", r"$\arg\underline U$ est la phase à l'origine : $\tfrac\pi3$.", src=KIT, duree=1),
        v("s13", r"$i_1(t)=I\sqrt2\cos(\omega t)$, les autres signaux du circuit sont en sinus. Argument de $\underline I_1$ (en rad) ?", "pi/2", "pi/2", r"$\cos(\omega t)=\sin(\omega t+\tfrac\pi2)$, donc $\underline I_1=I\,e^{j\pi/2}=jI$.", src=TD4 + ", ex. 5", duree=2),
        v("s14", r"$\underline U=3+4j$ V. Valeur efficace de $u(t)$ (en V) ?", "abs(3+4*I)", "5", r"$|\underline U|=\sqrt{3^2+4^2}=5$ V.", duree=2),
        v("s15", r"Même tension. Amplitude maximale de $u(t)$ (en V) ?", "abs(3+4*I)*sqrt(2)", "5*sqrt(2)", r"$U_m=U\sqrt2=5\sqrt2\approx7{,}07$ V.", duree=2),
        v("s16", r"$\underline I=2\,e^{-j\pi/4}$ A. Partie réelle de $\underline I$ (en A) ?", "re(2*exp(-I*pi/4))", "sqrt(2)", r"$2\cos(-\tfrac\pi4)=\sqrt2$ A (et partie imaginaire $-\sqrt2$).", src=TD4 + ", ex. 5", duree=2),
        o("s17", r"Pourquoi faut-il écrire $i_1(t)=I\sqrt2\cos(\omega t)$, $i_2(t)=I\sqrt2\sin(\omega t)$ et $e(t)=E\sqrt2\sin(\omega t)$ avec la même fonction avant de passer en complexe ? Donner $\underline I_1$, $\underline I_2$, $\underline E$.",
          r"L'amplitude complexe repose sur la phase à l'origine, définie par rapport à une seule fonction de référence. On réécrit $i_1(t)=I\sqrt2\sin(\omega t+\tfrac\pi2)$, d'où $\underline I_1=jI$, $\underline I_2=I$, $\underline E=E$.", src=TD4 + ", ex. 5", duree=4),
    ]},
    {"n": 2, "titre": "Impédances complexes", "notions": ["impedances", "amplitude"], "exos": [
        v("s21", r"Bobine $L=20$ mH, $\omega=500$ rad/s. Partie imaginaire de $\underline Z_L$ (en Ω) ?", "Rational(20,1000)*500", "10", r"$\underline Z_L=jL\omega=10j$ Ω.", duree=1),
        v("s22", r"Condensateur $C=10\,\mu$F, $\omega=1000$ rad/s. Partie imaginaire de $\underline Z_C$ (en Ω) ?", "im(1/(I*Rational(10,10**6)*1000))", "-100", r"$\underline Z_C=\dfrac1{jC\omega}=-\dfrac{j}{C\omega}=-100j$ Ω.", duree=2),
        v("s23", r"Argument de l'impédance d'une bobine idéale (en degrés) ?", "90", "90", r"$jL\omega$ est imaginaire pur positif : $+90°$, la tension est en avance sur le courant.", duree=1),
        v("s24", r"Argument de l'impédance d'un condensateur idéal (en degrés) ?", "-90", "-90", r"$-\dfrac{j}{C\omega}$ : $-90°$, la tension est en retard sur le courant.", duree=1),
        v("s25", r"Bobine $L=0{,}1$ H à $f=50$ Hz. $|\underline Z_L|$ en unités de $\pi$ Ω ?", "Rational(1,10)*2*50", "10", r"$L\omega=0{,}1\times100\pi=10\pi\approx31{,}4$ Ω.", duree=2),
        v("s26", r"Un dipôle sous $12$ V efficaces est traversé par $3$ A efficaces. $|\underline Z|$ (en Ω) ?", "12/3", "4", r"$|\underline Z|=U/I=4$ Ω.", duree=1),
        o("s27", r"Que représente l'argument de l'impédance complexe $\underline Z$ d'un dipôle (convention récepteur) ? Quelle est l'unité de $L\omega$, de $C\omega$ ?",
          r"$\arg\underline Z=\arg\underline U-\arg\underline I$ : le déphasage de la tension à ses bornes par rapport au courant qui le traverse. $L\omega$ est en ohms (c'est $|\underline Z_L|$), $C\omega$ en siemens (c'est $1/|\underline Z_C|$).", src=X26 + ", Q3-Q4", duree=3),
    ]},
    {"n": 3, "titre": "Associations d'impédances", "notions": ["associations", "impedances"], "exos": [
        v("s31", r"$R=3$ Ω, $L\omega=8$ Ω et $\tfrac1{C\omega}=4$ Ω en série. $|\underline Z|$ (en Ω) ?", "abs(3+8*I-4*I)", "5", r"$\underline Z=3+8j-4j=3+4j$, $|\underline Z|=5$ Ω.", duree=2),
        v("s32", r"$R=10$ Ω en parallèle avec $L\omega=10$ Ω. $|\underline Z|$ (en Ω) ?", "abs(10*10*I/(10+10*I))", "5*sqrt(2)", r"$\underline Z=\dfrac{100j}{10+10j}=5+5j$, $|\underline Z|=5\sqrt2$ Ω.", duree=3),
        v("s33", r"$R$ en parallèle avec $C$. $\underline Z$ en fonction de $R$, $C$, $\omega$ (écrire $j$ = `I`, $\omega$ = `w`) ?", f"R*{_ZC}/(R+{_ZC})", "R/(1+I*R*C*w)", r"$\underline Z=\dfrac{R\cdot\frac1{jC\omega}}{R+\frac1{jC\omega}}=\dfrac{R}{1+jRC\omega}$ (on multiplie par $jC\omega$).", src=X26 + ", Q5", duree=3),
        v("s34", r"$L$ en parallèle avec $C$. $\underline Z''$ en fonction de $L$, $C$, $\omega$ ?", f"(I*L*w)*{_ZC}/(I*L*w+{_ZC})", "I*L*w/(1-L*C*w**2)", r"$\underline Z''=\dfrac{jL\omega\cdot\frac1{jC\omega}}{jL\omega+\frac1{jC\omega}}=\dfrac{jL\omega}{1-LC\omega^2}$.", src=X26 + ", Q6", duree=3),
        v("s35", r"$L=10$ mH en parallèle avec $C=100\,\mu$F. Pulsation (en rad/s) pour laquelle $|\underline Z''|\to\infty$ ?", "1/sqrt(Rational(1,100)*Rational(1,10**4))", "1000", r"Le dénominateur $1-LC\omega^2$ s'annule pour $\omega=\dfrac1{\sqrt{LC}}=1000$ rad/s : l'ensemble se comporte comme un circuit ouvert.", duree=3),
        v("s36", r"$R$ en parallèle avec $L$ (TD 4, ex. 3). $\underline Z$ en fonction de $R$, $L$, $\omega$ ?", f"1/(1/R+1/(I*L*w))", "I*R*L*w/(R+I*L*w)", r"$\underline Z=\dfrac{R\cdot jL\omega}{R+jL\omega}$.", src=TD4 + ", ex. 3", duree=2),
        o("s37", r"Quel est le déphasage de la tension aux bornes de $\underline Z''=\dfrac{jL\omega}{1-LC\omega^2}$ par rapport au courant qui le traverse ? Justifier.",
          r"$\underline Z''$ est imaginaire pur, le signe de sa partie imaginaire est celui de $1-LC\omega^2$. Déphasage $+\tfrac\pi2$ si $1-LC\omega^2 > 0$ et $-\tfrac\pi2$ si $1-LC\omega^2 < 0$.", src=X26 + ", question bonus", duree=4),
    ]},
    {"n": 4, "titre": "Loi d'Ohm généralisée", "notions": ["ohm_c", "associations"], "exos": [
        v("s41", r"$E=20$ V efficaces aux bornes de $R=10$ Ω en série avec $L\omega=10$ Ω. Courant efficace (en A) ?", "20/abs(10+10*I)", "sqrt(2)", r"$|\underline Z|=10\sqrt2$ Ω, $I=\dfrac{20}{10\sqrt2}=\sqrt2$ A.", src=TD4 + ", ex. 1", duree=2),
        v("s42", r"Même circuit : phase de $\underline I$ par rapport à $\underline E$ (en degrés) ?", "-45", "-45", r"$\arg\underline I=\arg\underline E-\arg\underline Z=0-45°=-45°$ : le courant est en retard.", src=TD4 + ", ex. 1", duree=2),
        v("s43", r"Même circuit : tension efficace aux bornes de la bobine (en V) ?", "10*sqrt(2)", "10*sqrt(2)", r"$U_L=L\omega\,I=10\sqrt2\approx14{,}1$ V.", duree=2),
        v("s44", r"$230$ V efficaces aux bornes de $\underline Z=30+40j$ Ω. Courant efficace (en A) ?", "230/abs(30+40*I)", "Rational(23,5)", r"$|\underline Z|=50$ Ω, $I=230/50=4{,}6$ A.", duree=2),
        v("s45", r"$R$ et $L$ en série : $3$ V efficaces sur $R$, $4$ V efficaces sur $L$. Tension efficace totale (en V) ?", "abs(3+4*I)", "5", r"Les tensions sont déphasées de $90°$ : $\underline U=3+4j$, $U=5$ V (et non $7$ V).", duree=3),
        v("s46", r"TD 4, ex. 1 : $R$ et $L$ en série sous $e(t)=E\sqrt2\sin(\omega t)$. $\underline I/\underline E$ en fonction de $R$, $L$, $\omega$ ?", "1/(R+I*L*w)", "(R-I*L*w)/(R**2+L**2*w**2)", r"$\underline I=\dfrac{\underline E}{R+jL\omega}$ ; on peut aussi écrire $\dfrac{R-jL\omega}{R^2+L^2\omega^2}\underline E$.", src=TD4 + ", ex. 1", duree=3),
        o("s47", r"Une fois $\underline I$ calculé, comment écrire le courant réel $i(t)$ ?",
          r"$i(t)=I\sqrt2\sin(\omega t+\varphi)$ avec $I=|\underline I|$ (valeur efficace) et $\varphi=\arg\underline I$ (phase à l'origine), en gardant la fonction de référence choisie (ici le sinus).", src=TD4 + ", ex. 1", duree=3),
    ]},
    {"n": 5, "titre": "Diviseur de tension en complexe", "notions": ["diviseur_c", "associations"], "exos": [
        v("s51", r"TD 4, ex. 2 : $R$ en série avec $C$ sous $\underline E$, sortie $\underline U$ sur $C$. $\underline U/\underline E$ ?", f"{_ZC}/(R+{_ZC})", "1/(1+I*R*C*w)", r"Diviseur de tension : $\underline U=\dfrac{\frac1{jC\omega}}{R+\frac1{jC\omega}}\underline E=\dfrac{1}{1+jRC\omega}\underline E$.", src=TD4 + ", ex. 2", duree=3),
        v("s52", r"Même montage avec $RC\omega=1$ et $E=10$ V. Tension efficace $U$ (en V) ?", "10/abs(1+I)", "5*sqrt(2)", r"$U=\dfrac{10}{|1+j|}=\dfrac{10}{\sqrt2}=5\sqrt2$ V.", duree=2),
        v("s53", r"Même montage avec $RC\omega=1$. Déphasage de $u$ par rapport à $e$ (en degrés) ?", "-45", "-45", r"$\arg\dfrac1{1+j}=-45°$.", duree=2),
        v("s54", r"$R$ en série avec $L$, sortie sur $L$, $L\omega=R$. Déphasage de la sortie par rapport à l'entrée (en degrés) ?", "45", "45", r"$\dfrac{jL\omega}{R+jL\omega}=\dfrac{j}{1+j}$ : $90°-45°=45°$.", duree=2),
        v("s55", r"TD 4, ex. 3 : $C$ en série avec $R\parallel L$ sous $\underline E$ ; $\underline U$ aux bornes de $R\parallel L$. $\underline U/\underline E$ ?", f"{_RL}/({_RL}+{_ZC})", "-R*L*C*w**2/(R-R*L*C*w**2+I*L*w)", r"$\underline U=\dfrac{\frac{jRL\omega}{R+jL\omega}}{\frac{jRL\omega}{R+jL\omega}+\frac1{jC\omega}}\underline E=\dfrac{-RLC\omega^2}{R-RLC\omega^2+jL\omega}\underline E$.", src=TD4 + ", ex. 3", duree=5),
        v("s56", r"Même circuit : courant $\underline I_L$ dans la bobine, $\underline I_L/\underline E$ ?", "(-R*L*C*w**2/(R-R*L*C*w**2+I*L*w))/(I*L*w)", "I*R*C*w/(R-R*L*C*w**2+I*L*w)", r"$\underline I_L=\dfrac{\underline U}{jL\omega}=\dfrac{jRC\omega}{R-RLC\omega^2+jL\omega}\underline E$ ; puis $\underline I_R=\underline U/R$ et $\underline I=\underline I_L+\underline I_R$.", src=TD4 + ", ex. 3", duree=4),
        o("s57", r"À quelle condition peut-on appliquer le pont diviseur de tension à deux impédances ?",
          r"Les deux impédances doivent être parcourues par le même courant : en série, sans courant prélevé entre elles (sortie à vide). Sinon on réduit d'abord le circuit (associations, Thévenin).", duree=3),
    ]},
    {"n": 6, "titre": "Thévenin et Norton en complexe", "notions": ["thevenin_c", "diviseur_c"], "exos": [
        v("s61", r"$v_e$ en série avec $2R$, puis $C$ et $R$ en parallèle en sortie. Thévenin vu par $R$ : $\underline E_{th}/\underline V_E$ ?", f"{_ZC}/(2*R+{_ZC})", "1/(1+2*I*R*C*w)", r"On retire $R$ : diviseur $2R$, $C$ : $\underline E_{th}=\dfrac{1}{1+2jRC\omega}\underline V_E$.", src=X25 + ", Q7", duree=3),
        v("s62", r"Même montage : $\underline Z_{th}$ ?", f"2*R*{_ZC}/(2*R+{_ZC})", "2*R/(1+2*I*R*C*w)", r"Source éteinte (fil) : $2R\parallel C=\dfrac{2R}{1+2jRC\omega}$.", src=X25 + ", Q8", duree=3),
        v("s63", r"Source $\underline E=10$ V en série avec $\underline Z=5j$ Ω. Courant de Norton efficace (en A) ?", "abs(10/(5*I))", "2", r"$\underline I_N=\underline E/\underline Z=-2j$ A, $|\underline I_N|=2$ A.", duree=2),
        v("s64", r"$v_e$, $6R$ en série, $6R$ en parallèle, puis $L$ et $2R$ en série en sortie. Thévenin vu par $2R$ : $\underline Z_{th}$ ?", "6*R*6*R/(12*R)+I*L*w", "3*R+I*L*w", r"$6R\parallel6R=3R$ en série avec $L$ : $\underline Z_{th}=3R+jL\omega$ (et $\underline E_{th}=\tfrac12\underline V_E$).", src=X25 + ", ex. 2", duree=3),
        v("s65", r"$v_e$, $2R$ en série, $4R$ en parallèle, puis $C$ en série et $L$ en sortie. $\underline E_{th}/\underline V_E$ vu par $L$ ?", "4*R/(2*R+4*R)", "Rational(2,3)", r"Norton : $\dfrac{\underline V_E}{2R}$ avec $2R\parallel4R=\tfrac{4R}3$, d'où $\underline E_{th}=\tfrac{4R}{3}\cdot\dfrac{\underline V_E}{2R}=\tfrac23\underline V_E$.", src=X26 + ", ex. 3", duree=3),
        v("s66", r"Même montage : $\underline Z_{th}$ vu par $L$ ?", f"2*R*4*R/(6*R)+{_ZC}", "4*R/3+1/(I*C*w)", r"$\underline Z_{th}=\dfrac{4R}3+\dfrac1{jC\omega}$.", src=X26 + ", ex. 3", duree=3),
        o("s67", r"Comment obtient-on $\underline E_{th}$ et $\underline Z_{th}$ d'un réseau linéaire en régime sinusoïdal ?",
          r"$\underline E_{th}$ : tension à vide entre les deux bornes (charge retirée). $\underline Z_{th}$ : impédance vue des bornes, sources éteintes (source de tension $\to$ fil, source de courant $\to$ circuit ouvert). On peut aussi enchaîner les transformations Thévenin $\leftrightarrow$ Norton.", duree=3),
    ]},
    {"n": 7, "titre": "Très basses et très hautes fréquences", "notions": ["limites", "diviseur_c"], "exos": [
        v("s71", r"$v_e$, $6R$ en série, $6R$ en parallèle, puis $L$ en série et $2R$ en sortie. Limite de $A(\omega)$ en TBF ?", "(6*R*2*R/(8*R))/(6*R+6*R*2*R/(8*R))", "Rational(1,5)", r"$L\to$ fil : $6R\parallel2R=1{,}5R$, $A=\dfrac{1{,}5R}{6R+1{,}5R}=\tfrac15$.", src=X25 + ", ex. 2", duree=3),
        v("s72", r"Même filtre : limite de $A(\omega)$ en THF ?", "0", "0", r"$L\to$ circuit ouvert : aucun courant dans $2R$, $v_s\to0$.", src=X25 + ", ex. 2", duree=2),
        o("s73", r"Même filtre : nature ? Et si l'on remplace la bobine par un condensateur ?",
          r"$A$ décroît de $\tfrac15$ à $0$ : passe-bas. Avec un condensateur, les comportements TBF et THF sont inversés : passe-haut.", src=X25 + ", ex. 2", duree=3),
        v("s74", r"$v_e$, $C$ en série, puis $4R$ et $L$ en parallèle en sortie. Limite de $A(\omega)$ en THF ?", "1", "1", r"$C\to$ fil, $L\to$ circuit ouvert : $v_s=v_e$, $A\to1$ (en TBF $C$ ouvert : $A\to0$). Passe-haut.", src=X25 + ", ex. 3", duree=2),
        o("s75", r"Même filtre : nature si l'on remplace le condensateur par une bobine ? Justifier.",
          r"TBF : la bobine de sortie est un fil, $v_s=0$. THF : la bobine série est ouverte, aucun courant dans $4R$, $v_s=0$. Amplification nulle aux deux bouts : passe-bande.", src=X25 + ", ex. 3", duree=4),
        v("s76", r"$v_e$, $2R$ en série, $4R$ en parallèle, puis $C$ en série et $L$ en sortie. Limite de $A(\omega)$ en THF ?", "4*R/(6*R)", "Rational(2,3)", r"$C\to$ fil, $L\to$ ouvert : $v_s$ est la tension sur $4R$, $A=\dfrac{4R}{2R+4R}=\tfrac23$ ; en TBF $C$ ouvert donne $A\to0$.", src=X26 + ", ex. 3", duree=3),
        v("s77", r"Filtre RC, sortie sur $C$. Limite de $A(\omega)$ en TBF ?", "1", "1", r"$C\to$ circuit ouvert, pas de courant dans $R$ : $v_s=v_e$. Passe-bas.", duree=1),
    ]},
    {"n": 8, "titre": "Fonction de transfert et gain", "notions": ["transfert", "limites"], "exos": [
        v("s81", r"Amplification $A=10$. Gain (en dB) ?", "20*log(10,10)", "20", r"$G=20\log_{10}10=20$ dB.", duree=1),
        v("s82", r"Gain $-20$ dB. Amplification ?", "10**(-20/20)", "Rational(1,10)", r"$A=10^{G/20}=0{,}1$.", duree=2),
        v("s83", r"Amplification $\tfrac1{\sqrt2}$. Gain exact (en dB) ?", "20*log(1/sqrt(2),10)", "-10*log(2)/log(10)", r"$G=20\log_{10}2^{-1/2}=-10\log_{10}2\approx-3$ dB.", duree=2),
        v("s84", r"$V_E=10$ V efficaces, $A=0{,}2$. $V_S$ efficace (en V) ?", "10*Rational(1,5)", "2", r"$V_S=A\,V_E=2$ V.", src=X25 + ", Q5", duree=1),
        v("s85", r"$\underline T=\dfrac1{1+j\omega/\omega_c}$ à $\omega=\omega_c$. Déphasage de $v_s$ par rapport à $v_e$ (en degrés) ?", "-45", "-45", r"$\arg\dfrac1{1+j}=-45°$.", duree=2),
        v("s86", r"$\underline T=\dfrac{R}{5R+jL\omega}$ à $\omega=5R/L$. Amplification ?", "abs(1/(5+5*I))", "sqrt(2)/10", r"$\underline T=\dfrac{1}{5+5j}$, $A=\dfrac1{5\sqrt2}=\dfrac{\sqrt2}{10}$.", src=X25 + ", ex. 2", duree=3),
        o("s87", r"Vrai ou faux : $\arg\underline T(\omega)$ est le déphasage de la tension de sortie par rapport à la tension d'entrée. Que représente $V_S/V_E$ ?",
          r"Vrai : $\arg\underline T=\arg\underline V_S-\arg\underline V_E$. Le quotient des valeurs efficaces $V_S/V_E=|\underline T|$ est l'amplification $A(\omega)$ (le gain est $20\log_{10}A$).", src=X25 + ", Q5-Q6", duree=3),
    ]},
    {"n": 9, "titre": "Filtres du premier ordre", "notions": ["ordre1", "transfert"], "exos": [
        v("s91", r"Filtre RC passe-bas $\dfrac1{1+jRC\omega}$, $R=1$ kΩ, $C=1\,\mu$F. $\omega_c$ (en rad/s) ?", "1/(1000*Rational(1,10**6))", "1000", r"$\omega_c=\dfrac1{RC}=\dfrac1{10^{-3}}=1000$ rad/s.", duree=2),
        v("s92", r"$\omega_c=1000$ rad/s. Fréquence de coupure en Hz (valeur exacte) ?", "1000/(2*pi)", "500/pi", r"$f_c=\dfrac{\omega_c}{2\pi}=\dfrac{500}\pi\approx159$ Hz.", duree=2),
        v("s93", r"Examen 2025, ex. 2 : diviseur de $\underline E_{th}=\tfrac12\underline V_E$, $\underline Z_{th}=3R+jL\omega$ et $2R$. $\underline T=\underline V_S/\underline V_E$ ?", "2*R/(3*R+I*L*w+2*R)/2", "R/(5*R+I*L*w)", r"$\underline V_S=\dfrac{2R}{3R+jL\omega+2R}\cdot\dfrac{\underline V_E}2$, donc $\underline T=\dfrac{R}{5R+jL\omega}$.", src=X25 + ", ex. 2", duree=4),
        v("s94", r"Même filtre : $A_{max}$ ?", "Rational(1,5)", "Rational(1,5)", r"$\underline T=\dfrac15\cdot\dfrac{1}{1+j\frac{L}{5R}\omega}$ : $A_{max}=A_{TBF}=\tfrac15$.", src=X25 + ", ex. 2", duree=2),
        v("s95", r"Même filtre, $R=100$ Ω, $L=0{,}5$ H. $\omega_c$ (en rad/s) ?", "5*100/Rational(1,2)", "1000", r"$\omega_c=\dfrac{5R}{L}=1000$ rad/s.", src=X25 + ", ex. 2", duree=2),
        v("s96", r"Passe-haut du premier ordre, $A_{max}=1$. Amplification à $\omega=\omega_c$ ?", "abs(I/(1+I))", "1/sqrt(2)", r"$\left|\dfrac{j}{1+j}\right|=\dfrac1{\sqrt2}$.", duree=2),
        o("s97", r"Comment met-on une fonction de transfert du premier ordre sous forme normalisée ? Que vaut le gain à $\omega_c$ ?",
          r"On factorise le terme réel du dénominateur pour obtenir $1+j\frac\omega{\omega_c}$, puis on identifie $A_{max}$ et $\omega_c$. À $\omega_c$ : $A=A_{max}/\sqrt2$, soit $G=G_{max}-3$ dB.", src=X25 + ", ex. 2", duree=4),
    ]},
    {"n": 10, "titre": "Filtres du second ordre", "notions": ["ordre2", "ordre1"], "exos": [
        v("sa1", r"Examen 2025, ex. 3 : $C$ en série, $4R\parallel L$ en sortie. $\underline T$ ?", f"(4*I*R*L*w/(4*R+I*L*w))/((4*I*R*L*w/(4*R+I*L*w))+{_ZC})", "-4*R*L*C*w**2/(4*R+I*L*w-4*R*L*C*w**2)", r"$4R\parallel L=\dfrac{j4RL\omega}{4R+jL\omega}$, diviseur : $\underline T=\dfrac{-4RLC\omega^2}{4R+jL\omega-4RLC\omega^2}$.", src=X25 + ", ex. 3", duree=5),
        v("sa2", r"$L=10$ mH, $C=1\,\mu$F. Pulsation propre $\omega_0=1/\sqrt{LC}$ (en rad/s) ?", "1/sqrt(Rational(1,100)*Rational(1,10**6))", "10000", r"$LC=10^{-8}$, $\omega_0=10^4$ rad/s.", duree=2),
        v("sa3", r"Même filtre que sa1 : $\sigma$ en fonction de $R$, $L$, $C$ ?", "(L/(4*R))*(1/sqrt(L*C))/2", "L/(8*R*sqrt(L*C))", r"Forme normalisée : $\dfrac{-LC\omega^2}{1+j\frac{L}{4R}\omega-LC\omega^2}$ ; $2\sigma\dfrac{\omega}{\omega_0}=\dfrac{L}{4R}\omega$ donc $\sigma=\dfrac{L}{8R}\omega_0=\dfrac{L}{8R\sqrt{LC}}$.", src=X25 + ", ex. 3", duree=4),
        v("sa4", r"$L=10$ mH, $C=1\,\mu$F, $R=25$ Ω dans ce filtre. $\sigma$ ?", "Rational(1,100)/(8*25*sqrt(Rational(1,100)*Rational(1,10**6)))", "Rational(1,2)", r"$\sigma=\dfrac{L\omega_0}{8R}=\dfrac{0{,}01\times10^4}{200}=0{,}5$.", duree=3),
        v("sa5", r"Passe-bande du second ordre, $A_0=1$. Amplification à $\omega=\omega_0$ ?", "abs(2*I*Rational(1,2)/(1+2*I*Rational(1,2)-1))", "1", r"À $\omega_0$ : $\underline T=A_0\dfrac{2j\sigma}{2j\sigma}=A_0=1$, quel que soit $\sigma$.", duree=2),
        v("sa6", r"Examen 2026, ex. 3 : $\underline E_{th}=\tfrac23\underline V_E$, $\underline Z_{th}=\tfrac{4R}3+\tfrac1{jC\omega}$, sortie sur $L$. $\underline V_S/\underline V_E$ ?", f"(I*L*w/(4*R/3+{_ZC}+I*L*w))*Rational(2,3)", "-2*L*C*w**2/(4*I*R*C*w+3-3*L*C*w**2)", r"Diviseur : $\dfrac{jL\omega}{\frac{4R}3+\frac1{jC\omega}+jL\omega}\cdot\dfrac23$ ; on multiplie par $3jC\omega$ : $\dfrac{-2LC\omega^2}{4jRC\omega+3-3LC\omega^2}$.", src=X26 + ", ex. 3", duree=5),
        o("sa7", r"Nature du filtre de l'examen 2026 (ex. 3) à partir de $\dfrac{-2LC\omega^2}{3+4jRC\omega-3LC\omega^2}$ ?",
          r"Divisé par $3$ : $\dfrac23\cdot\dfrac{-LC\omega^2}{1+j\frac{4RC}{3}\omega-LC\omega^2}$, numérateur en $-(\omega/\omega_0)^2$ : passe-haut du second ordre, $A_0=A_{THF}=\tfrac23$, $\omega_0=\dfrac1{\sqrt{LC}}$.", src=X26 + ", ex. 3", duree=5),
    ]},
    {"n": 11, "titre": "Niveau examen : sujet B2 janvier 2025", "notions": ["impedances", "thevenin_c", "limites", "ordre1", "ordre2"], "examen": True, "exos": [
        o("xa1", r"Exercice 1 (QCM) : unité de $U$ dans $u(t)=U\sqrt2\sin(\omega t+\varphi)$ ; argument de $\underline U$ ; argument de $\underline Z$ ; unité de $C\omega$ ; nom de $V_S/V_E$ ; $\arg\underline T$ = déphasage de la sortie sur l'entrée ?",
          r"$U$ en volts ; $\arg\underline U=\varphi$ ; $\arg\underline Z$ : déphasage de $u$ par rapport à $i$ ; $C\omega$ en siemens ; $V_S/V_E$ : l'amplification $A(\omega)$ ; vrai.", src=X25 + ", ex. 1 (4 points)", duree=6),
        v("xa2", r"Exercice 1, Q7-Q8 : $v_e$, $2R$ en série, $C\parallel R$ en sortie. $\underline Z_{th}$ vu par $R$ ?", f"2*R*{_ZC}/(2*R+{_ZC})", "2*R/(1+2*I*R*C*w)", r"$\underline E_{th}=\dfrac{\underline V_E}{1+2jRC\omega}$, $\underline Z_{th}=\dfrac{2R}{1+2jRC\omega}$.", src=X25 + ", ex. 1", duree=4),
        o("xa3", r"Exercice 2 (qualitatif) : $v_e$, $6R$ en série, $6R$ en parallèle, $L$ en série, $2R$ en sortie. Limites TBF et THF de $A$, nature, et nature avec un condensateur à la place de $L$.",
          r"TBF : $L$ fil, $A\to\tfrac15$. THF : $L$ ouvert, $A\to0$. Passe-bas. Avec un condensateur : TBF et THF inversés, passe-haut.", src=X25 + ", ex. 2 (9 points)", duree=8),
        v("xa4", r"Exercice 2 (quantitatif) : $\underline T(\omega)$ ?", "(2*R/(3*R+I*L*w+2*R))*Rational(1,2)", "R/(5*R+I*L*w)", r"$\underline E_{th}=\tfrac12\underline V_E$, $\underline Z_{th}=3R+jL\omega$, diviseur sur $2R$ : $\underline T=\dfrac{R}{5R+jL\omega}=\dfrac15\cdot\dfrac{1}{1+j\frac{L}{5R}\omega}$.", src=X25 + ", ex. 2", duree=8),
        v("xa5", r"Exercice 2 : $R=200$ Ω, $L=1$ H. $\omega_c$ (en rad/s) ?", "5*200/1", "1000", r"$\omega_c=\dfrac{5R}{L}=1000$ rad/s.", src=X25 + ", ex. 2", duree=3),
        o("xa6", r"Exercice 3 (qualitatif) : $v_e$, $C$ en série, $4R\parallel L$ en sortie. Limites, nature, et nature avec une bobine à la place de $C$.",
          r"TBF : $C$ ouvert, $A\to0$. THF : $C$ fil et $L$ ouvert, $A\to1$. Passe-haut. Avec une bobine à la place de $C$ : $A\to0$ aux deux bouts, passe-bande.", src=X25 + ", ex. 3 (7 points)", duree=8),
        v("xa7", r"Exercice 3 (quantitatif) : $\underline T(\omega)$ ?", f"(4*I*R*L*w/(4*R+I*L*w))/((4*I*R*L*w/(4*R+I*L*w))+{_ZC})", "-4*R*L*C*w**2/(4*R+I*L*w-4*R*L*C*w**2)", r"$\underline T=\dfrac{-4RLC\omega^2}{4R+jL\omega-4RLC\omega^2}$.", src=X25 + ", ex. 3", duree=8),
        v("xa8", r"Exercice 3 : $\omega_0$ en fonction de $L$, $C$ ?", "1/sqrt(L*C)", "(L*C)**Rational(-1,2)", r"$\left(\dfrac\omega{\omega_0}\right)^2=LC\omega^2$ donc $\omega_0=\dfrac1{\sqrt{LC}}$, puis $\sigma=\dfrac{L}{8R\sqrt{LC}}$.", src=X25 + ", ex. 3", duree=5),
    ]},
    {"n": 12, "titre": "Niveau examen : sujet janvier 2026", "notions": ["associations", "thevenin_c", "amplitude", "ordre2"], "examen": True, "exos": [
        o("xb1", r"Exercice 1 : vrai ou faux, « le courant qui entre dans une résistance est plus intense que celui qui en sort » ; que représente $\arg\underline Z$ ; unité de $L\omega$ ; $\underline Z$ de $R\parallel C$ ; $\underline Z''$ de $L\parallel C$.",
          r"Faux (même courant). $\arg\underline Z$ : déphasage de la tension sur le courant. $L\omega$ en ohms. $\underline Z=\dfrac{R}{1+jRC\omega}$. $\underline Z''=\dfrac{jL\omega}{1-LC\omega^2}$, déphasage $\pm\tfrac\pi2$ selon le signe de $1-LC\omega^2$.", src=X26 + ", ex. 1 (4,5 points)", duree=6),
        v("xb2", r"Exercice 1, Q2 : $E$, $R$, $R$ en série, puis $R$ entre $A$ et $B$. $E=9$ V : $E_{th}$ (en V) ?", "9*1/3", "3", r"Diviseur : $E_{th}=\dfrac{R}{3R}E=\dfrac E3=3$ V et $R_{th}=2R\parallel R=\dfrac{2R}3$.", src=X26 + ", ex. 1", duree=3),
        o("xb3", r"Exercice 2 (régime continu, figure 1 du sujet) : nombre de nœuds, de branches, de mailles ; méthode pour exprimer $U$ aux bornes de $4R$.",
          r"$3$ nœuds, $6$ branches, $10$ mailles. On transforme $I_0$ et $R$ en source $RI_0$ en série avec $R$, on associe avec $E$ et $R$ ($RI_0-E$, $2R$), on repasse en Norton $\dfrac{RI_0-E}{2R}$, on associe les sources de courant et $2R\parallel6R\parallel4R=\dfrac{12R}{11}$, d'où $U=-\dfrac{6}{11}(RI_0+E)$.", src=X26 + ", ex. 2 (7,5 points)", duree=15),
        v("xb4", r"Exercice 2 : $U=-\tfrac{6}{11}(RI_0+E)$ avec $R=1$ kΩ, $I_0=2$ mA, $E=9$ V. $U$ (en V) ?", "-Rational(6,11)*(1*2+9)", "-6", r"$RI_0=2$ V, $U=-\tfrac6{11}\times11=-6$ V.", src=X26 + ", ex. 2", duree=3),
        o("xb5", r"Exercice 3, Q1-Q4 : $V_E$ est-il une grandeur sans unité ? Que représente $\omega$ ? Module et argument de $\underline V_E$ pour $v_e(t)=V_E\sqrt2\sin(\omega t)$ ?",
          r"Faux : $V_E$ est une valeur efficace en volts. $\omega$ est la pulsation. $|\underline V_E|=V_E$ et $\arg\underline V_E=0$.", src=X26 + ", ex. 3 (8 points)", duree=4),
        v("xb6", r"Exercice 3, Q5 : $\underline Z_{th}$ vu par $L$ ($v_e$, $2R$ en série, $4R$ en parallèle, $C$ en série) ?", f"2*R*4*R/(6*R)+{_ZC}", "4*R/3+1/(I*C*w)", r"$\underline E_{th}=\tfrac23\underline V_E$, $\underline Z_{th}=\dfrac{4R}3+\dfrac1{jC\omega}$.", src=X26 + ", ex. 3", duree=6),
        v("xb7", r"Exercice 3, Q5 : $\underline V_S/\underline V_E$ ?", f"(I*L*w/(4*R/3+{_ZC}+I*L*w))*Rational(2,3)", "-2*L*C*w**2/(4*I*R*C*w+3-3*L*C*w**2)", r"$\underline V_S=\dfrac{jL\omega}{\underline Z_{th}+jL\omega}\underline E_{th}=\dfrac{-2LC\omega^2}{4jRC\omega+3-3LC\omega^2}\underline V_E$.", src=X26 + ", ex. 3", duree=8),
    ]},
]


def _v(enonce, calc, ans, sol):
    return {"enonce": enonce, "calc": calc, "ans": ans, "sol": sol}


VARIANTS = {
    "s11": [_v(r"$u(t)=12\sqrt2\sin(\omega t-\tfrac\pi6)$ (en V). Module de $\underline U$ (en V) ?", "12", "12", r"Valeur efficace : $12$ V.")],
    "s14": [_v(r"$\underline U=6-8j$ V. Valeur efficace de $u(t)$ (en V) ?", "abs(6-8*I)", "10", r"$\sqrt{36+64}=10$ V.")],
    "s21": [_v(r"Bobine $L=50$ mH, $\omega=200$ rad/s. Partie imaginaire de $\underline Z_L$ (en Ω) ?", "Rational(50,1000)*200", "10", r"$L\omega=10$ Ω.")],
    "s22": [_v(r"Condensateur $C=20\,\mu$F, $\omega=500$ rad/s. Partie imaginaire de $\underline Z_C$ (en Ω) ?", "im(1/(I*Rational(20,10**6)*500))", "-100", r"$-\dfrac1{C\omega}=-100$ Ω.")],
    "s26": [_v(r"Un dipôle sous $10$ V efficaces est traversé par $0{,}5$ A efficaces. $|\underline Z|$ (en Ω) ?", "10/Rational(1,2)", "20", r"$U/I=20$ Ω.")],
    "s31": [_v(r"$R=6$ Ω, $L\omega=12$ Ω et $\tfrac1{C\omega}=4$ Ω en série. $|\underline Z|$ (en Ω) ?", "abs(6+12*I-4*I)", "10", r"$6+8j$, module $10$ Ω.")],
    "s41": [_v(r"$E=30$ V efficaces aux bornes de $R=30$ Ω en série avec $L\omega=40$ Ω. Courant efficace (en A) ?", "30/abs(30+40*I)", "Rational(3,5)", r"$|\underline Z|=50$ Ω, $I=0{,}6$ A.")],
    "s44": [_v(r"$100$ V efficaces aux bornes de $\underline Z=60-80j$ Ω. Courant efficace (en A) ?", "100/abs(60-80*I)", "1", r"$|\underline Z|=100$ Ω, $I=1$ A.")],
    "s45": [_v(r"$R$ et $C$ en série : $6$ V efficaces sur $R$, $8$ V efficaces sur $C$. Tension efficace totale (en V) ?", "abs(6-8*I)", "10", r"$|6-8j|=10$ V.")],
    "s63": [_v(r"Source $\underline E=12$ V en série avec $\underline Z=-4j$ Ω. Courant de Norton efficace (en A) ?", "abs(12/(-4*I))", "3", r"$|\underline I_N|=12/4=3$ A.")],
    "s81": [_v(r"Amplification $100$. Gain (en dB) ?", "20*log(100,10)", "40", r"$20\log_{10}100=40$ dB.")],
    "s84": [_v(r"$V_E=5$ V efficaces, $A=3$. $V_S$ efficace (en V) ?", "5*3", "15", r"$V_S=15$ V.")],
    "s91": [_v(r"Filtre RC passe-bas, $R=10$ kΩ, $C=10$ nF. $\omega_c$ (en rad/s) ?", "1/(10000*Rational(10,10**9))", "10000", r"$RC=10^{-4}$ s, $\omega_c=10^4$ rad/s.")],
    "s95": [_v(r"Même filtre, $R=20$ Ω, $L=0{,}1$ H. $\omega_c$ (en rad/s) ?", "5*20/Rational(1,10)", "1000", r"$5R/L=1000$ rad/s.")],
    "sa2": [_v(r"$L=1$ mH, $C=10\,\mu$F. $\omega_0$ (en rad/s) ?", "1/sqrt(Rational(1,1000)*Rational(10,10**6))", "10000", r"$LC=10^{-8}$, $\omega_0=10^4$ rad/s.")],
    "xb4": [_v(r"Exercice 2 : $U=-\tfrac{6}{11}(RI_0+E)$ avec $R=2$ kΩ, $I_0=1$ mA, $E=20$ V. $U$ (en V) ?", "-Rational(6,11)*(2*1+20)", "-12", r"$RI_0+E=22$ V, $U=-12$ V.")],
}
for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["id"] in VARIANTS:
            _e["variants"] = VARIANTS[_e["id"]]


EXTRA_PARTS = []

QUIZ = [
    {"notion": "amplitude", "type": "qcm", "q": r"Le module de l'amplitude complexe $\underline U$ de $u(t)=U\sqrt2\sin(\omega t+\varphi)$ est :", "choix": [r"$U$, la valeur efficace", r"$U\sqrt2$", r"$\omega$", r"$\varphi$"], "bonne": 0},
    {"notion": "amplitude", "type": "vf", "q": r"$\cos(\omega t)=\sin(\omega t+\tfrac\pi2)$.", "bonne": True},
    {"notion": "impedances", "type": "qcm", "q": r"L'unité du produit $C\omega$ est :", "choix": [r"le siemens", r"l'ohm", r"le hertz", r"l'ampère"], "bonne": 0},
    {"notion": "impedances", "type": "vf", "q": r"L'argument de $\underline Z$ est le déphasage du courant par rapport à la tension.", "bonne": False},
    {"notion": "associations", "type": "qcm", "q": r"$R$ en parallèle avec $C$ :", "choix": [r"$\dfrac{R}{1+jRC\omega}$", r"$\dfrac1R+jC\omega$", r"$R+\dfrac1{jC\omega}$", r"$\dfrac{jRC\omega}{R+jC\omega}$"], "bonne": 0},
    {"notion": "associations", "type": "vf", "q": r"$L$ et $C$ en parallèle se comportent comme un circuit ouvert à $\omega=1/\sqrt{LC}$.", "bonne": True},
    {"notion": "ohm_c", "type": "qcm", "q": r"$3$ V efficaces sur $R$ et $4$ V efficaces sur $L$ en série donnent au total :", "choix": [r"$5$ V", r"$7$ V", r"$1$ V", r"$12$ V"], "bonne": 0},
    {"notion": "ohm_c", "type": "vf", "q": r"$|\underline I|$ est la valeur efficace du courant $i(t)$.", "bonne": True},
    {"notion": "diviseur_c", "type": "qcm", "q": r"RC série sous $\underline E$, sortie sur $C$ :", "choix": [r"$\dfrac{\underline E}{1+jRC\omega}$", r"$\dfrac{jRC\omega\,\underline E}{1+jRC\omega}$", r"$jRC\omega\,\underline E$", r"$\underline E$"], "bonne": 0},
    {"notion": "diviseur_c", "type": "vf", "q": r"Le pont diviseur s'applique si un courant est prélevé entre les deux impédances.", "bonne": False},
    {"notion": "thevenin_c", "type": "qcm", "q": r"$\underline Z_{th}$ s'obtient :", "choix": [r"sources éteintes, vu des bornes", r"en court-circuitant les bornes", r"en divisant $\underline E_{th}$ par $\underline V_E$", r"en ajoutant toutes les impédances"], "bonne": 0},
    {"notion": "thevenin_c", "type": "vf", "q": r"Une source $\underline E$ en série avec $\underline Z$ équivaut à $\underline E/\underline Z$ en parallèle avec $\underline Z$.", "bonne": True},
    {"notion": "limites", "type": "qcm", "q": r"En très haute fréquence, une bobine se comporte comme :", "choix": [r"un circuit ouvert", r"un fil", r"une résistance", r"une source"], "bonne": 0},
    {"notion": "limites", "type": "vf", "q": r"Une amplification nulle en TBF et en THF indique un passe-bande.", "bonne": True},
    {"notion": "transfert", "type": "qcm", "q": r"Le quotient $V_S/V_E$ des valeurs efficaces est :", "choix": [r"l'amplification $A(\omega)$", r"le gain $G(\omega)$", r"la fonction de transfert $\underline T(\omega)$", r"le déphasage"], "bonne": 0},
    {"notion": "transfert", "type": "vf", "q": r"$A=1/\sqrt2$ correspond à un gain d'environ $-3$ dB.", "bonne": True},
    {"notion": "ordre1", "type": "qcm", "q": r"Pour un passe-bas du premier ordre, $A_{max}$ vaut :", "choix": [r"$A_{TBF}$", r"$A_{THF}$", r"$A(\omega_c)$", r"$1$ toujours"], "bonne": 0},
    {"notion": "ordre1", "type": "vf", "q": r"À la pulsation de coupure, $A=A_{max}/2$.", "bonne": False},
    {"notion": "ordre2", "type": "qcm", "q": r"Si $LC\omega^2=(\omega/\omega_0)^2$, alors :", "choix": [r"$\omega_0=1/\sqrt{LC}$", r"$\omega_0=LC$", r"$\omega_0=\sqrt{LC}$", r"$\omega_0=1/(LC)$"], "bonne": 0},
    {"notion": "ordre2", "type": "vf", "q": r"Un numérateur en $-(\omega/\omega_0)^2$ indique un passe-haut du second ordre.", "bonne": True},
]

_A = r"$\underline S=S\,e^{j\varphi}$ · $|\underline S|=S$ (efficace) · $\arg\underline S=\varphi$ · $\cos(\omega t)=\sin(\omega t+\tfrac\pi2)$ · $U_m=U\sqrt2$"
_Z = r"$\underline Z_R=R$ · $\underline Z_L=jL\omega$ · $\underline Z_C=\dfrac1{jC\omega}$ · $|\underline Z|=U/I$ · $\arg\underline Z=\arg\underline U-\arg\underline I$"
_S = r"série : $\underline Z_1+\underline Z_2$ · parallèle : $\dfrac{\underline Z_1\underline Z_2}{\underline Z_1+\underline Z_2}$"
_O = r"$\underline U=\underline Z\,\underline I$ · $U=|\underline Z|I$ · $\arg\underline I=\arg\underline U-\arg\underline Z$"
_D = r"$\underline U_2=\dfrac{\underline Z_2}{\underline Z_1+\underline Z_2}\underline E$"
_T = r"$\underline E_{th}$ : tension à vide · $\underline Z_{th}$ : sources éteintes · $\underline I_N=\underline E_{th}/\underline Z_{th}$"
_L = r"TBF : $C\to$ ouvert, $L\to$ fil · THF : $C\to$ fil, $L\to$ ouvert"
_F = r"$\underline T=\underline V_S/\underline V_E$ · $A=|\underline T|$ · $G=20\log_{10}A$ · $\arg\underline T$ : déphasage sortie/entrée"
_1 = r"$\underline T=A_{max}\dfrac1{1+j\omega/\omega_c}$ · $A(\omega_c)=A_{max}/\sqrt2$ · $f_c=\omega_c/(2\pi)$"
_2 = r"$1+2j\sigma\dfrac\omega{\omega_0}-\left(\dfrac\omega{\omega_0}\right)^2$ · $\omega_0=\dfrac1{\sqrt{LC}}$"

FORMULES = {
    "s11": _A, "s12": _A, "s13": _A, "s14": _A + r" · $|a+jb|=\sqrt{a^2+b^2}$", "s15": _A, "s16": r"$e^{j\theta}=\cos\theta+j\sin\theta$", "s17": _A,
    "s21": _Z, "s22": _Z, "s23": _Z, "s24": _Z, "s25": _Z + r" · $\omega=2\pi f$", "s26": _Z, "s27": _Z,
    "s31": _S + " · " + _Z, "s32": _S, "s33": _S + " · " + _Z, "s34": _S + " · " + _Z, "s35": _S + r" · $\omega_0=1/\sqrt{LC}$", "s36": _S, "s37": _Z + " · " + _S,
    "s41": _O + " · " + _S, "s42": _O, "s43": _O, "s44": _O, "s45": _O + r" · $|a+jb|=\sqrt{a^2+b^2}$", "s46": _O + " · " + _S, "s47": _O + " · " + _A,
    "s51": _D + " · " + _Z, "s52": _D, "s53": _D, "s54": _D, "s55": _D + " · " + _S, "s56": _D + " · " + _O, "s57": _D,
    "s61": _T + " · " + _D, "s62": _T + " · " + _S, "s63": _T, "s64": _T + " · " + _S, "s65": _T + " · " + _D, "s66": _T + " · " + _S, "s67": _T,
    "s71": _L + " · " + _D, "s72": _L, "s73": _L, "s74": _L, "s75": _L, "s76": _L + " · " + _D, "s77": _L,
    "s81": _F, "s82": _F, "s83": _F, "s84": _F, "s85": _F, "s86": _F, "s87": _F,
    "s91": _1, "s92": _1, "s93": _1 + " · " + _D, "s94": _1, "s95": _1, "s96": r"passe-haut : $A_{max}\dfrac{j\omega/\omega_c}{1+j\omega/\omega_c}$", "s97": _1,
    "sa1": _2 + " · " + _D + " · " + _S, "sa2": _2, "sa3": _2, "sa4": _2, "sa5": r"passe-bande : $A_0\dfrac{2j\sigma\omega/\omega_0}{1+2j\sigma\omega/\omega_0-(\omega/\omega_0)^2}$", "sa6": _D + " · " + _T, "sa7": _2,
    "xa1": _Z + " · " + _F, "xa2": _T + " · " + _S, "xa3": _L + " · " + _D, "xa4": _T + " · " + _D + " · " + _1, "xa5": _1, "xa6": _L, "xa7": _D + " · " + _S, "xa8": _2,
    "xb1": _Z + " · " + _S, "xb2": _T + " · " + _D, "xb3": _T, "xb4": _T, "xb5": _A, "xb6": _T + " · " + _S, "xb7": _D + " · " + _T,
}


# ---------------------------------------------------------------- circuit figures (`schema.py`)

def _fig26_1(d):
    """Exam January 2026, ex. 2, figure 1 (U = -6/11 (R I0 + E), checked with sympy)."""
    d += R().endpoints((0, 3), (0, 0)).label("$R$")
    d += (s := SrcI().endpoints((2, 0), (2, 3)))
    courant(d, s, "$I_0$", debut=False)
    d += Fil().endpoints((0, 3), (2, 3))
    d += R().endpoints((2, 3), (5, 3)).label("$R$")
    d += (s := SrcU().endpoints((8, 3), (5, 3)))
    tension(d, s, "$E$")
    d += R().endpoints((8, 3), (8, 0)).label("$6R$", loc="bottom")
    d += Fil().endpoints((8, 3), (13, 3))
    d += (s := SrcI().endpoints((10.5, 3), (10.5, 0)))
    courant(d, s, "$I_0$")
    d += Point().at((13, 3)).label("$A$", loc="right")
    d += (r := R().endpoints((13, 3), (13, 0)).label("$4R$", loc="top"))
    tension(d, r, "$U$", sens=-1)
    d += Point().at((13, 0)).label("$B$", loc="right")
    d += Fil().endpoints((0, 0), (13, 0))


FIG_RL = schema_echelle("e(t)", [("s", "R", "R"), ("s", "L", "L")])
FIG_RC = schema_echelle("e(t)", [("s", "R", "R"), ("p", "C", "C")], "u(t)")
FIG_RLs = schema_echelle("e(t)", [("s", "R", "R"), ("p", "L", "L")], "u(t)")
FIG_C_RL = schema_echelle("e(t)", [("s", "C", "C"), ("p", "R", "R"), ("p", "L", "L")], "u(t)")
FIG_Q78 = (schema_echelle("v_e(t)", [("s", "R", "2R"), ("p", "C", "C"), ("p", "R", "R")], "u(t)") + "\n\n"
           + schema_echelle("\\underline{E}_{th}", [("s", "Z", "\\underline{Z}_{th}"), ("p", "R", "R")], "\\underline{U}"))
FIG_EX2 = schema_echelle("v_e(t)", [("s", "R", "6R"), ("p", "R", "6R"), ("s", "L", "L"), ("p", "R", "2R")], "v_s(t)")
FIG_EX3 = schema_echelle("v_e(t)", [("s", "C", "C"), ("p", "R", "4R"), ("p", "L", "L")], "v_s(t)")
FIG_F3 = schema_echelle("v_e(t)", [("s", "R", "2R"), ("p", "R", "4R"), ("s", "C", "C"), ("p", "L", "L")], "v_s(t)")
FIG_Q2 = (schema_echelle("E", [("s", "R", "R"), ("s", "R", "R"), ("p", "R", "R"), ("p", "R", "R_4")], "U") + "\n\n"
          + schema_echelle("E_{th}", [("s", "R", "R_{th}"), ("p", "R", "R_4")], "U"))
FIG_F1 = fig(_fig26_1, "Schéma : R et source de courant I0 à gauche, R puis source E sur le fil du haut, 6R, source de courant I0 vers le bas et 4R (tension U) entre A et B")

FIGS = {**dict.fromkeys(["s41", "s42", "s43", "s45", "s46"], FIG_RL),
        **dict.fromkeys(["s51", "s52", "s53"], FIG_RC), "s54": FIG_RLs,
        **dict.fromkeys(["s55", "s56"], FIG_C_RL),
        **dict.fromkeys(["s61", "s62", "xa2"], FIG_Q78),
        **dict.fromkeys(["s64", "s71", "s72", "s73", "s86", "s93", "s94", "s95", "xa3", "xa4", "xa5"], FIG_EX2),
        **dict.fromkeys(["s74", "s75", "sa1", "sa3", "sa4", "xa6", "xa7", "xa8"], FIG_EX3),
        **dict.fromkeys(["s65", "s66", "s76", "sa6", "xb6", "xb7"], FIG_F3),
        "xb2": FIG_Q2, "xb3": FIG_F1, "xb4": FIG_F1}
ajoute(LEVELS, FIGS)
