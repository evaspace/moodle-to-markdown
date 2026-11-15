"""Level path: S1 maths, ECUE OBM (logique, ensembles, fonctions, raisonnements, relations).

Calibrated on Examen B1-OBM oct. 2024 (promo 2029) and B1-LE nov. 2023 (promo 2028),
and the 2026 seminar TD. Mostly `open` exercises (proofs, negations): each has a model answer.
"""

SUBJECT = {
    "id": "maths-s1-obm",
    "ordre": 100,
    "matiere": "maths",
    "semestre": "S1",
    "ecue": "OBM",
    "titre": "Logique, ensembles, fonctions",
    "chapitres_moodle": [
        "24_Cours 6 - compléments Séminaire - ECUE OBM", "25_Logique", "26_Raisonnements", "27_Ensembles",
        "28_Ensembles finis", "29_Applications - image directe, image réciproque, antécédents",
        "30_Injections, surjections, bijections",
    ],
    "td": "TD_Séminaire2026",
    "examens": ["Examen B1-OBM (fin octobre)", "Rattrapage B1"],
}

NOTIONS = [
    {"id": "connecteurs", "titre": "Connecteurs logiques",
     "formule": r"$P\Rightarrow Q$ est faux seulement si $P$ vrai et $Q$ faux · $P\Rightarrow Q\equiv \lnot P\lor Q$ · $P\iff Q\equiv(P\Rightarrow Q)\land(Q\Rightarrow P)$",
     "exemple": r"« si $1=2$ alors $5$ est pair » est vraie",
     "cours": r"Tables de vérité : $\lnot P$ inverse ; $P\land Q$ vrai si les deux sont vrais ; $P\lor Q$ vrai si au moins un l'est ; $P\Leftrightarrow Q$ vrai si $P$ et $Q$ ont même valeur. Une implication dont l'hypothèse est fausse est vraie."},
    {"id": "cns", "titre": "Condition nécessaire, suffisante",
     "formule": r"$A\Rightarrow P$ : $A$ suffit pour $P$ · $P\Rightarrow B$ : $B$ est nécessaire à $P$",
     "exemple": r"$x<-10\Rightarrow x^2>4$ vrai ; $x^2>4\Rightarrow x>1{,}9$ faux ($x=-3$)",
     "cours": r"Pour une condition sur $x$, on réécrit chaque assertion comme un ensemble : $A\Rightarrow P$ vrai $\iff$ l'ensemble de $A$ est inclus dans celui de $P$. Pour prouver qu'une implication est fausse, un seul contre-exemple suffit."},
    {"id": "negation", "titre": "Négations",
     "formule": r"$\lnot(P\land Q)\equiv\lnot P\lor\lnot Q$ · $\lnot(P\lor Q)\equiv\lnot P\land\lnot Q$ · $\lnot(P\Rightarrow Q)\equiv P\land\lnot Q$",
     "exemple": r"$\lnot(x>2\Rightarrow x^2>4)$ : « $x>2$ et $x^2\le4$ »",
     "cours": r"Lois de De Morgan. La négation d'une implication n'est **pas** une implication : c'est « l'hypothèse est vraie et la conclusion fausse ». La négation de $<$ est $\ge$."},
    {"id": "quantificateurs", "titre": "Quantificateurs",
     "formule": r"$\lnot(\forall x,\,P(x))\equiv\exists x,\,\lnot P(x)$ · $\lnot(\exists x,\,P(x))\equiv\forall x,\,\lnot P(x)$",
     "exemple": r"$\forall x\,\exists y,\ y>x$ vrai ; $\exists y\,\forall x,\ y>x$ faux",
     "cours": r"L'ordre compte : dans $\forall x\,\exists y$, $y$ peut dépendre de $x$ ; dans $\exists y\,\forall x$, un même $y$ doit marcher pour tous les $x$. Pour nier, on échange $\forall$ et $\exists$ en gardant l'ordre, et on nie la propriété finale."},
    {"id": "raisonnements", "titre": "Contraposée, absurde, contre-exemple",
     "formule": r"contraposée : $(P\Rightarrow Q)\equiv(\lnot Q\Rightarrow\lnot P)$ · absurde : supposer $\lnot P$ et aboutir à une contradiction · contre-exemple : un seul $x$ tel que $\lnot P(x)$ réfute $\forall x,\,P(x)$",
     "exemple": r"$n^2$ pair $\Rightarrow n$ pair : on montre $n$ impair $\Rightarrow n^2$ impair",
     "cours": r"Contraposée : on suppose $\lnot Q$ et on montre $\lnot P$ ; à l'examen, écrire explicitement la contraposée. Absurde : on suppose $\lnot Q$ (avec $P$) et on aboutit à une contradiction. La réciproque de $P\Rightarrow Q$ est $Q\Rightarrow P$ : elle n'est pas équivalente."},
    {"id": "recurrence", "titre": "Récurrence",
     "formule": r"$P(n_0)$ vraie et $\forall n\ge n_0,\ P(n)\Rightarrow P(n+1)$ donnent $\forall n\ge n_0,\ P(n)$",
     "exemple": r"$\sum_{k=1}^nk=\frac{n(n+1)}2$",
     "cours": r"Rédaction : énoncer $P(n)$ ; initialisation ; hérédité (on fixe $n$, on suppose $P(n)$, on montre $P(n+1)$ en utilisant l'hypothèse) ; conclusion."},
    {"id": "ensembles", "titre": "Inclusion et égalité d'ensembles",
     "formule": r"$A\subset B\iff\forall x,\ (x\in A\Rightarrow x\in B)$ · $A=B\iff A\subset B$ et $B\subset A$",
     "exemple": r"$\{(x,x,x)\}\subset\{(x,y,z),\ 2x-y-z=0\}$",
     "cours": r"Pour montrer $A\subset B$ : « soit $x\in A$ », puis on vérifie la condition de $B$. Pour montrer $A\not\subset B$ : un élément de $A$ hors de $B$. $\overline{A\cup B}=\bar A\cap\bar B$, $\overline{A\cap B}=\bar A\cup\bar B$. $\mathcal P(E)$ : ensemble des parties, $|\mathcal P(E)|=2^{|E|}$."},
    {"id": "images", "titre": "Image directe, image réciproque",
     "formule": r"$f(I)=\{f(x),\ x\in I\}$ · $f^{-1}(J)=\{x\in A,\ f(x)\in J\}$",
     "exemple": r"$\exp^{-1}(\{0\})=\emptyset$ ; $\cos([0,\frac\pi2])=[0,1]$",
     "cours": r"$f(I)$ est une partie de l'ensemble d'arrivée, $f^{-1}(J)$ une partie de l'ensemble de départ. $f^{-1}(J)$ existe même si $f$ n'est pas bijective, et peut être vide. Faire un dessin du graphe au brouillon."},
    {"id": "injection", "titre": "Injection, surjection, bijection",
     "formule": r"Injective : $f(x)=f(x')\Rightarrow x=x'$ · Surjective : $\forall y\in B,\ \exists x\in A,\ f(x)=y$ · Bijective : injective et surjective, soit $\forall y\in B,\ \exists!\,x\in A,\ f(x)=y$",
     "exemple": r"$x\mapsto x^2$ de $\mathbb R$ dans $\mathbb R$ : ni injective ($f(-1)=f(1)$) ni surjective ($-1$ n'a pas d'antécédent)",
     "cours": r"Non injective : deux éléments distincts de même image. Non surjective : un élément de l'arrivée sans antécédent. Bijective = injective et surjective : tout $y$ a exactement un antécédent. Restreindre le départ ou l'arrivée change la réponse."},
    {"id": "relations", "titre": "Relations binaires",
     "formule": r"Réflexive : $xRx$ · Symétrique : $xRy\Rightarrow yRx$ · Antisymétrique : $xRy\land yRx\Rightarrow x=y$ · Transitive : $xRy\land yRz\Rightarrow xRz$",
     "exemple": r"$aRb\iff|a|\le|b|$ : réflexive, transitive, ni symétrique ni antisymétrique",
     "cours": r"Équivalence : réflexive, symétrique, transitive. Ordre : réflexive, antisymétrique, transitive. Pour montrer qu'une propriété est fausse, un contre-exemple chiffré suffit."},
]


def o(id, enonce, sol, src=None, duree=None):
    e = {"id": id, "kind": "open", "enonce": enonce, "sol": sol}
    if src:
        e["src"] = src
    if duree:
        e["duree"] = duree
    return e


def v(id, enonce, calc, ans, sol, src=None, duree=None):
    e = {"id": id, "kind": "value", "enonce": enonce, "calc": calc, "ans": ans, "sol": sol}
    if src:
        e["src"] = src
    if duree:
        e["duree"] = duree
    return e


O29 = "Examen B1-OBM oct. 2024"
L28 = "Examen B1-LE nov. 2023"

LEVELS = [
    {"n": 1, "titre": "Connecteurs et tables de vérité", "notions": ["connecteurs"], "exos": [
        o("lg1", r"$P$ est vraie et $Q$ est fausse. Donner la valeur de $P\land Q$, $P\lor Q$, $P\Rightarrow Q$, $Q\Rightarrow P$, $P\Leftrightarrow Q$.",
          r"Faux, vrai, faux, vrai, faux.", duree=2),
        o("lg2", r"La phrase « si $2+2=5$ alors la Lune est un fromage » est-elle vraie ?", r"Vraie : l'hypothèse est fausse, donc l'implication est vraie.", duree=2),
        o("lg3", r"Montrer avec une table de vérité que $P\Rightarrow Q$ a la même valeur que $\lnot P\lor Q$.",
          r"Les deux sont fausses uniquement pour $P$ vrai, $Q$ faux, et vraies dans les trois autres lignes.", duree=3),
        o("lg4", r"Donner une assertion équivalente à $\lnot(P\land\lnot Q)$ sans négation devant une parenthèse.",
          r"$\lnot P\lor Q$, c'est-à-dire $P\Rightarrow Q$.", duree=3),
    ]},
    {"n": 2, "titre": "Implications, condition nécessaire ou suffisante", "notions": ["cns"], "exos": [
        o("cn1", r"Soit $x\in\mathbb R$. $x>3\Rightarrow x^2>9$ ? $x^2>9\Rightarrow x>3$ ? Justifier.",
          r"Vrai : si $x>3>0$ alors $x^2>9$. Faux : $x=-4$ donne $x^2=16>9$ mais $x<3$.", duree=3),
        o("cn2", r"Soit $P$ : « $x^2>4$ » et les assertions (1) $x>-2$, (2) $x<-10$, (3) $x>1{,}9$, (4) $x<-3$ ou $x>3$, (5) $x<-2$ ou $x>2$. Lister les implications vraies « … $\Rightarrow P$ ».",
          r"$P\iff x\in\,]-\infty,-2[\cup]2,+\infty[$. Vraies : (2), (4), (5) (leurs ensembles sont inclus dans celui de $P$). (1) faux ($x=0$), (3) faux ($x=1{,}95$).", src=f"{O29}, ex. 1.1a"),
        o("cn3", r"Mêmes assertions : lister les implications vraies « $P\Rightarrow$ … ».",
          r"Seulement $P\Rightarrow(5)$, car (5) est équivalente à $P$. (1) : $x=-3$ ; (2) : $x=3$ ; (3) : $x=-3$ ; (4) : $x=2{,}5$ sont des contre-exemples.", src=f"{O29}, ex. 1.1b"),
        o("cn4", r"« Être divisible par 4 » est-il une condition nécessaire, suffisante, les deux ou aucune pour « être pair » ?",
          r"Suffisante (divisible par 4 $\Rightarrow$ pair) mais pas nécessaire ($2$ est pair, non divisible par 4).", duree=3),
    ]},
    {"n": 3, "titre": "Négations", "notions": ["negation"], "exos": [
        o("ng1", r"Nier « $x>0$ et $y\le1$ ».", r"« $x\le0$ ou $y>1$ ».", duree=2),
        o("ng2", r"Nier « $P\Rightarrow Q$ ».", r"« $P$ et non $Q$ ».", duree=2),
        o("ng3", r"Donner la négation de l'implication vraie « $x^2>4\Rightarrow(x<-2$ ou $x>2)$ ».",
          r"« $x^2>4$ et $-2\le x\le2$ ».", src=f"{O29}, ex. 1.1c", duree=3),
        o("ng4", r"Nier « s'il pleut, je prends mon parapluie ou je reste chez moi ».",
          r"« Il pleut, je ne prends pas mon parapluie et je ne reste pas chez moi ».", duree=3),
        o("ng5", r"Nier « $x\le0$ ou $y>1$ ».",
          r"$\lnot(P\lor Q)\equiv\lnot P\land\lnot Q$ : « $x>0$ et $y\le1$ ».", duree=2),
    ]},
    {"n": 4, "titre": "Quantificateurs", "notions": ["quantificateurs"], "exos": [
        o("qt1", r"$\forall x\in\mathbb R,\ \exists y\in\mathbb R,\ y>x$ est-elle vraie ? Et $\exists y\in\mathbb R,\ \forall x\in\mathbb R,\ y>x$ ?",
          r"Première vraie ($y=x+1$). Seconde fausse : pour tout $y$, $x=y$ donne $y>x$ faux."),
        o("qt2", r"$P$ : « $\forall x\in\mathbb R,\ \exists y\in\mathbb R,\ \cos(x)=y$ ». Vraie ? Justifier.",
          r"Vraie : pour $x$ donné, $y=\cos(x)$ convient.", src=f"{O29}, ex. 1.2a", duree=3),
        o("qt3", r"$Q$ : « $\exists y\in\mathbb R,\ \forall x\in\mathbb R,\ x=\cos(y)$ ». Vraie ? Justifier.",
          r"Fausse : $\cos(y)$ est un seul nombre, il ne peut pas être égal à tous les réels (par exemple $x=\cos(y)+1$).", src=f"{O29}, ex. 1.2a", duree=3),
        o("qt4", r"Écrire avec des quantificateurs : « la fonction $f:\mathbb R\to\mathbb R$ est majorée ».",
          r"$\exists M\in\mathbb R,\ \forall x\in\mathbb R,\ f(x)\le M$.", duree=3),
    ]},
    {"n": 5, "titre": "Nier une phrase quantifiée", "notions": ["quantificateurs", "negation"], "exos": [
        o("nq1", r"Nier $\forall x\in\mathbb R,\ \exists y\in\mathbb R,\ \cos(x)=y$.", r"$\exists x\in\mathbb R,\ \forall y\in\mathbb R,\ \cos(x)\neq y$.", src=f"{O29}, ex. 1.2b", duree=3),
        o("nq2", r"Nier $\exists y\in\mathbb R,\ \forall x\in\mathbb R,\ x=\cos(y)$.", r"$\forall y\in\mathbb R,\ \exists x\in\mathbb R,\ x\neq\cos(y)$.", src=f"{O29}, ex. 1.2b", duree=3),
        o("nq3", r"Nier « $f$ est majorée » et « $f$ est croissante sur $\mathbb R$ ».",
          r"$\forall M,\ \exists x,\ f(x)>M$. $\exists(x,y)\in\mathbb R^2,\ x\le y$ et $f(x)>f(y)$."),
        o("nq4", r"Nier $\forall\varepsilon>0,\ \exists N\in\mathbb N,\ \forall n\ge N,\ |u_n-\ell|\le\varepsilon$.",
          r"$\exists\varepsilon>0,\ \forall N\in\mathbb N,\ \exists n\ge N,\ |u_n-\ell|>\varepsilon$."),
    ]},
    {"n": 6, "titre": "Contraposée et absurde", "notions": ["raisonnements"], "exos": [
        o("rs1", r"Écrire la contraposée et la réciproque de « $A\Rightarrow B$ ». Laquelle est équivalente à $A\Rightarrow B$ ?",
          r"Contraposée : $\lnot B\Rightarrow\lnot A$, équivalente (même table de vérité : $B\lor\lnot A$). Réciproque : $B\Rightarrow A$, pas équivalente.", src=f"{O29}, ex. 1.3a-b", duree=3),
        o("rs2", r"Montrer par contraposée : si $n^2$ est pair alors $n$ est pair.",
          r"Contraposée : $n$ impair $\Rightarrow n^2$ impair. $n=2k+1$ donne $n^2=2(2k^2+2k)+1$, impair."),
        o("rs3", r"Soit $a\in\mathbb R$. Montrer par contraposée : $(\forall\varepsilon>0,\ |a|\le\varepsilon)\Rightarrow a=0$. La réciproque est-elle vraie ?",
          r"Contraposée : $a\neq0\Rightarrow\exists\varepsilon>0,\ |a|>\varepsilon$. Avec $\varepsilon=\frac{|a|}2>0$ on a $|a|>\varepsilon$. Réciproque vraie : si $a=0$, $|a|=0\le\varepsilon$ pour tout $\varepsilon>0$.", src=f"{O29}, ex. 1.3c-d"),
        o("rs4", r"Montrer par l'absurde que $\sqrt2$ est irrationnel.",
          r"Supposons $\sqrt2=\frac pq$ irréductible. $p^2=2q^2$ donc $p$ pair, $p=2r$, puis $q^2=2r^2$ donc $q$ pair : contradiction avec l'irréductibilité."),
    ]},
    {"n": 7, "titre": "Récurrence", "notions": ["recurrence"], "exos": [
        o("rc1", r"Montrer par récurrence : $\forall n\ge1,\ \sum_{k=1}^nk=\frac{n(n+1)}2$.",
          r"Init. $n=1$ : $1=1$. Hérédité : $\sum_{k=1}^{n+1}k=\frac{n(n+1)}2+n+1=\frac{(n+1)(n+2)}2$."),
        o("rc2", r"Montrer : $\forall n\in\mathbb N,\ 3$ divise $4^n-1$.",
          r"Init. $4^0-1=0$. Hérédité : $4^{n+1}-1=4(4^n-1)+3$, somme de multiples de 3."),
        o("rc3", r"Montrer : $\forall n\ge1,\ \sum_{k=1}^nk^2=\frac{n(n+1)(2n+1)}6$.",
          r"Init. $1=1$. Hérédité : $\frac{n(n+1)(2n+1)}6+(n+1)^2=\frac{(n+1)(2n^2+7n+6)}6=\frac{(n+1)(n+2)(2n+3)}6$."),
        o("rc4", r"Montrer : $\forall n\ge4,\ 2^n\ge n^2$.",
          r"Init. $16\ge16$. Hérédité : $2^{n+1}=2\cdot2^n\ge2n^2$ et $2n^2\ge(n+1)^2\iff n^2-2n-1\ge0$, vrai pour $n\ge3$."),
    ]},
    {"n": 8, "titre": "Ensembles : inclusion, égalité", "notions": ["ensembles"], "exos": [
        o("en1", r"$A=\{(x,y,z)\in\mathbb R^3,\ x=y=z\}$, $B=\{(x,y,z)\in\mathbb R^3,\ 2x-y-z=0\}$. De quel ensemble sont-ils des parties ? Montrer $A\subset B$.",
          r"Parties de $\mathbb R^3$. Soit $(x,y,z)\in A$ : $y=z=x$ donc $2x-y-z=0$, d'où $(x,y,z)\in B$.", src=f"{O29}, ex. 1.4a-b"),
        o("en2", r"Avec les mêmes $A$ et $B$, a-t-on $B\subset A$ ?", r"Non : $(1,2,0)\in B$ car $2-2-0=0$, mais $(1,2,0)\notin A$.", src=f"{O29}, ex. 1.4c", duree=3),
        o("en3", r"Montrer par double inclusion : $\overline{A\cup B}=\bar A\cap\bar B$.",
          r"$x\in\overline{A\cup B}\iff\lnot(x\in A\lor x\in B)\iff x\notin A\land x\notin B\iff x\in\bar A\cap\bar B$ (chaque équivalence donne les deux inclusions)."),
        v("en4", r"$E=\{1,2,3,4\}$. Combien d'éléments a $\mathcal P(E)$ ? Combien de parties à 2 éléments ?", "2**4+0", "16",
          r"$|\mathcal P(E)|=2^4=16$ ; parties à 2 éléments : $\binom42=6$.", duree=2),
    ]},
    {"n": 9, "titre": "Image directe, image réciproque", "notions": ["images"], "exos": [
        o("im1", r"Rappeler les définitions de $f(I)$ et $f^{-1}(J)$ pour $f:A\to B$, $I\subset A$, $J\subset B$.",
          r"$f(I)=\{f(x),\ x\in I\}=\{y\in B,\ \exists x\in I,\ y=f(x)\}$ ; $f^{-1}(J)=\{x\in A,\ f(x)\in J\}$.", src=f"{O29}, ex. 2.1", duree=2),
        o("im2", r"$E=\{2,3,4\}$, $F=\{1,2,3\}$, $f:E\times F\to\mathbb N$, $f(x,y)=x+y$. Déterminer $f(E\times F)$, $f(\{(2,2),(4,3)\})$, $f^{-1}(\{1\})$ et $f^{-1}(\{6\})$.",
          r"Valeurs : 3, 4, 5, 4, 5, 6, 5, 6, 7. $f(E\times F)=\{3,4,5,6,7\}$ ; $f(\{(2,2),(4,3)\})=\{4,7\}$ ; $f^{-1}(\{1\})=\emptyset$ ; $f^{-1}(\{6\})=\{(3,3),(4,2)\}$.", src=f"{O29}, ex. 2.2"),
        o("im3", r"Pour $\exp:\mathbb R\to\mathbb R$, donner $f(\{0\})$, $f([0,\frac\pi2])$, $f^{-1}(\{0\})$, $f^{-1}(\{-1\})$, $f^{-1}(]-\infty,0])$.",
          r"$\{1\}$ ; $[1,e^{\pi/2}]$ ; $\emptyset$ ; $\emptyset$ ; $\emptyset$ (exp est strictement positive et croissante).", src=f"{O29}, ex. 3"),
        o("im4", r"Pour $\cos:[0,\pi]\to\mathbb R$, donner $f(\{0\})$, $f([0,\frac\pi2])$, $f^{-1}(\{0\})$, $f^{-1}(\{-1\})$, $f^{-1}(]-\infty,0])$.",
          r"$\{1\}$ ; $[0,1]$ ; $\{\frac\pi2\}$ ; $\{\pi\}$ ; $[\frac\pi2,\pi]$ (cos décroît de 1 à $-1$ sur $[0,\pi]$).", src=f"{O29}, ex. 3"),
        o("im5", r"$f:\mathbb R\to\mathbb R$, $f(x)=x^2$. Donner $f([-1,2])$ et $f^{-1}([1,4])$.",
          r"$f([-1,2])=[0,4]$ ; $f^{-1}([1,4])=[-2,-1]\cup[1,2]$."),
    ]},
    {"n": 10, "titre": "Injection, surjection, bijection", "notions": ["injection"], "exos": [
        o("ij1", r"Écrire les définitions de « $f:A\to B$ injective » et « surjective ».",
          r"Injective : $\forall(x,x')\in A^2,\ f(x)=f(x')\Rightarrow x=x'$. Surjective : $\forall y\in B,\ \exists x\in A,\ f(x)=y$.", duree=2),
        o("ij2", r"$f:E\times F\to\mathbb N$, $f(x,y)=x+y$ avec $E=\{2,3,4\}$, $F=\{1,2,3\}$. Injective ? Surjective ?",
          r"Non injective : $f(2,2)=f(3,1)=4$. Non surjective : $0$ n'a pas d'antécédent.", src=f"{O29}, ex. 2.2c-d"),
        o("ij3", r"Même $f$ : trouver $I\subset E\times F$ et $J\subset\mathbb N$ (au moins deux éléments chacun) tels que $f:I\to J$ soit injective non surjective, puis $I',J'$ pour surjective non injective.",
          r"$I=\{(2,1),(2,2)\}$, $J=\{3,4,5\}$ : images 3 et 4 distinctes, 5 sans antécédent. $I'=\{(2,1),(2,2),(3,1)\}$, $J'=\{3,4\}$ : tout est atteint, $f(2,2)=f(3,1)$.", src=f"{O29}, ex. 2.2e-f"),
        o("ij4", r"$g:\mathbb R\to\mathbb R$, $g(x)=3x-2$. Montrer que $g$ est bijective et donner $g^{-1}$.",
          r"Pour $y\in\mathbb R$, $g(x)=y\iff x=\frac{y+2}3$ : un unique antécédent. $g^{-1}(y)=\frac{y+2}3$."),
        o("ij5", r"$h:\mathbb R_+\to\mathbb R$, $h(x)=x^2$ est-elle injective ? surjective ? Et $h:\mathbb R_+\to\mathbb R_+$ ?",
          r"Injective (sur $\mathbb R_+$, $x^2=x'^2\Rightarrow x=x'$), non surjective ($-1$ sans antécédent). Vers $\mathbb R_+$ : bijective, d'inverse $\sqrt{\cdot}$."),
    ]},
    {"n": 11, "titre": "Relations binaires", "notions": ["relations"], "exos": [
        o("rl1", r"Sur $\mathbb R$ : $aRb\iff|a|\le|b|$. Réflexive ? Symétrique ? Justifier.",
          r"Réflexive : $|a|\le|a|$. Non symétrique : $0R1$ mais pas $1R0$.", src=f"{O29}, ex. 4.1-2"),
        o("rl2", r"Même relation : antisymétrique ? transitive ?",
          r"Non antisymétrique : $1R(-1)$ et $(-1)R1$ avec $1\neq-1$. Transitive : $|a|\le|b|\le|c|$.", src=f"{O29}, ex. 4.3-4"),
        o("rl3", r"Sur $\mathbb Z$ : $aRb\iff a-b$ est pair. Montrer que c'est une relation d'équivalence.",
          r"$a-a=0$ pair ; $a-b$ pair $\Rightarrow b-a$ pair ; $a-c=(a-b)+(b-c)$ pair."),
        o("rl4", r"Sur $\mathbb N^*$ : $aRb\iff a$ divise $b$. Est-ce une relation d'ordre ? Totale ?",
          r"Réflexive, antisymétrique ($a\mid b$ et $b\mid a$ donnent $a=b$ dans $\mathbb N^*$), transitive : ordre. Non total : ni $2\mid3$ ni $3\mid2$."),
    ]},
    {"n": 12, "titre": "Niveau examen : annales complètes", "notions": ["cns", "quantificateurs", "images", "relations"], "examen": True, "exos": [
        {"id": "ox1", "kind": "multi", "src": f"{O29}, ex. 1 (10 points)",
         "enonce": r"1. $P$ : « $x^2>4$ » et (1) $x>-2$, (2) $x<-10$, (3) $x>1{,}9$, (4) $x<-3$ ou $x>3$, (5) $x<-2$ ou $x>2$. Implications vraies « … $\Rightarrow P$ », « $P\Rightarrow$ … », et négation de ces dernières." "\n"
                   r"2. $\forall x\,\exists y,\ \cos x=y$ et $\exists y\,\forall x,\ x=\cos y$ : vraies ? Négations." "\n"
                   r"3. Contraposée, équivalence, application : $(\forall\varepsilon>0,\ |a|\le\varepsilon)\Rightarrow a=0$ ; réciproque." "\n"
                   r"4. $A=\{x=y=z\}$, $B=\{2x-y-z=0\}$ : $A\subset B$ ? $B\subset A$ ?",
         "parts": ["cn2", "cn3", "ng3", "qt2", "qt3", "nq1", "nq2", "rs1", "rs3", "en1", "en2"]},
        {"id": "ox2", "kind": "multi", "src": f"{O29}, ex. 2 et 3 (10 points)",
         "enonce": r"$f:E\times F\to\mathbb N$, $(x,y)\mapsto x+y$, $E=\{2,3,4\}$, $F=\{1,2,3\}$ : définitions, images, antécédents, injectivité, surjectivité, restrictions." "\n"
                   r"Puis tableau des images directes et réciproques pour $\exp$ et $\cos:[0,\pi]\to\mathbb R$.",
         "parts": ["im1", "im2", "ij2", "ij3", "im3", "im4"]},
        {"id": "ox3", "kind": "multi", "src": f"{O29}, ex. 4 (4 points)",
         "enonce": r"Sur $\mathbb R$, $aRb\iff|a|\le|b|$. Après avoir rappelé chaque définition : réflexive ? symétrique ? antisymétrique ? transitive ?",
         "parts": ["rl1", "rl2"]},
        {"id": "ox4", "kind": "multi", "src": "Rattrapage type (raisonnements)",
         "enonce": r"1. Montrer par contraposée que si $n^2$ est pair, $n$ est pair." "\n" r"2. Montrer par récurrence que $3\mid4^n-1$." "\n"
                   r"3. Nier « $f$ est majorée » et « $f$ est croissante ».",
         "parts": ["rs2", "rc2", "nq3"]},
    ]},
    {"n": 13, "titre": "Examen + 20 %", "notions": ["injection", "images", "raisonnements"], "examen": True, "exos": [
        o("oh1", r"Soit $f:A\to B$ et $I_1,I_2\subset A$. Montrer $f(I_1\cap I_2)\subset f(I_1)\cap f(I_2)$ et donner un exemple où l'inclusion est stricte.",
          r"$y=f(x)$ avec $x\in I_1\cap I_2$ : $y\in f(I_1)$ et $y\in f(I_2)$. Exemple : $f(x)=x^2$, $I_1=\{-1\}$, $I_2=\{1\}$ : $f(\emptyset)=\emptyset$ mais $\{1\}\cap\{1\}=\{1\}$."),
        o("oh2", r"Soient $f:A\to B$ et $g:B\to C$. Montrer que si $g\circ f$ est injective alors $f$ est injective.",
          r"$f(x)=f(x')\Rightarrow g(f(x))=g(f(x'))\Rightarrow x=x'$ par injectivité de $g\circ f$."),
        o("oh3", r"$f:\mathbb R\setminus\{1\}\to\mathbb R\setminus\{2\}$, $f(x)=\frac{2x+1}{x-1}$. Montrer que $f$ est bijective et donner $f^{-1}$.",
          r"$y=\frac{2x+1}{x-1}\iff y(x-1)=2x+1\iff x(y-2)=y+1\iff x=\frac{y+1}{y-2}$, défini pour $y\neq2$, et toujours $x\neq1$ (sinon $y+1=y-2$, impossible). $f^{-1}(y)=\frac{y+1}{y-2}$."),
        o("oh4", r"Montrer que pour tout $n\in\mathbb N$, $n(n+1)(n+2)$ est divisible par 6.",
          r"Parmi trois entiers consécutifs, l'un est pair et l'un est multiple de 3 ; 2 et 3 premiers entre eux donc $6$ divise le produit (ou récurrence : $(n+1)(n+2)(n+3)-n(n+1)(n+2)=3(n+1)(n+2)$, multiple de 6)."),
        o("oh5", r"Nier puis démontrer la fausseté de : $\exists M>0,\ \forall x\in\mathbb R,\ |x^2-x|\le M$.",
          r"Négation : $\forall M>0,\ \exists x,\ |x^2-x|>M$. Vraie : $x=M+2$ donne $x^2-x=x(x-1)>x>M$. Donc l'assertion de départ est fausse."),
    ]},
]

EXTRA_PARTS = []

QUIZ = [
    {"notion": "connecteurs", "type": "vf", "q": r"$P\Rightarrow Q$ est vraie lorsque $P$ est fausse.", "bonne": True},
    {"notion": "connecteurs", "type": "qcm", "q": r"$P\Rightarrow Q$ équivaut à :", "choix": [r"$\lnot P\lor Q$", r"$P\lor\lnot Q$", r"$\lnot P\land Q$", r"$Q\Rightarrow P$"], "bonne": 0},
    {"notion": "negation", "type": "qcm", "q": r"Négation de $P\Rightarrow Q$ :", "choix": [r"$P\land\lnot Q$", r"$\lnot P\Rightarrow\lnot Q$", r"$Q\Rightarrow P$", r"$\lnot P\lor Q$"], "bonne": 0},
    {"notion": "negation", "type": "vf", "q": r"La négation de « $x>2$ ou $y<1$ » est « $x\le2$ et $y\ge1$ ».", "bonne": True},
    {"notion": "quantificateurs", "type": "qcm", "q": r"Négation de $\forall x\,\exists y,\ P(x,y)$ :",
     "choix": [r"$\exists x\,\forall y,\ \lnot P(x,y)$", r"$\forall x\,\exists y,\ \lnot P(x,y)$", r"$\exists y\,\forall x,\ \lnot P(x,y)$", r"$\forall y\,\exists x,\ P(x,y)$"], "bonne": 0},
    {"notion": "quantificateurs", "type": "vf", "q": r"$\forall x\,\exists y$ et $\exists y\,\forall x$ veulent dire la même chose.", "bonne": False},
    {"notion": "cns", "type": "vf", "q": r"$x<-10\Rightarrow x^2>4$", "bonne": True},
    {"notion": "cns", "type": "vf", "q": r"$x^2>4\Rightarrow x>2$", "bonne": False},
    {"notion": "raisonnements", "type": "qcm", "q": r"Contraposée de $A\Rightarrow B$ :", "choix": [r"$\lnot B\Rightarrow\lnot A$", r"$B\Rightarrow A$", r"$\lnot A\Rightarrow\lnot B$", r"$A\land\lnot B$"], "bonne": 0},
    {"notion": "raisonnements", "type": "vf", "q": r"La réciproque d'une implication vraie est toujours vraie.", "bonne": False},
    {"notion": "recurrence", "type": "vf", "q": r"Dans l'hérédité, on suppose $P(n)$ vraie pour un $n$ fixé et on montre $P(n+1)$.", "bonne": True},
    {"notion": "ensembles", "type": "qcm", "q": r"Pour montrer $A=B$ :", "choix": [r"$A\subset B$ et $B\subset A$", r"$A\cap B\neq\emptyset$", r"$|A|=|B|$", r"$A\subset B$"], "bonne": 0},
    {"notion": "ensembles", "type": "vf", "q": r"$\overline{A\cap B}=\bar A\cup\bar B$", "bonne": True},
    {"notion": "images", "type": "qcm", "q": r"$f^{-1}(J)=$ ?", "choix": [r"$\{x\in A,\ f(x)\in J\}$", r"$\{f(x),\ x\in J\}$", r"l'image de $J$ par la réciproque, si $f$ est bijective seulement", r"$\{y\in B,\ y\in J\}$"], "bonne": 0},
    {"notion": "images", "type": "vf", "q": r"$\exp^{-1}(\{-1\})=\emptyset$", "bonne": True},
    {"notion": "injection", "type": "qcm", "q": r"$f$ non injective signifie :", "choix": [r"$\exists x\neq x',\ f(x)=f(x')$", r"$\exists y,\ $ sans antécédent", r"$\forall x,\ f(x)=0$", r"$f$ non surjective"], "bonne": 0},
    {"notion": "injection", "type": "vf", "q": r"$x\mapsto x^2$ de $\mathbb R_+$ dans $\mathbb R_+$ est bijective.", "bonne": True},
    {"notion": "relations", "type": "qcm", "q": r"Une relation d'ordre est :", "choix": [r"réflexive, antisymétrique, transitive", r"réflexive, symétrique, transitive", r"symétrique et transitive", r"antisymétrique seulement"], "bonne": 0},
    {"notion": "relations", "type": "vf", "q": r"$aRb\iff|a|\le|b|$ est antisymétrique sur $\mathbb R$.", "bonne": False},
]

# Formulas used in each solution (help « Formules de la solution »); multi exercises get those of their parts.
_IMPL = r"$P\Rightarrow Q$ est fausse seulement si $P$ vraie et $Q$ fausse · $P\Rightarrow Q\equiv\lnot P\lor Q$"
_MORGAN = r"De Morgan : $\lnot(P\land Q)\equiv\lnot P\lor\lnot Q$ · $\lnot(P\lor Q)\equiv\lnot P\land\lnot Q$"
_NIMPL = r"$\lnot(P\Rightarrow Q)\equiv P\land\lnot Q$"
_NQ = r"$\lnot(\forall x,\ P(x))\equiv\exists x,\ \lnot P(x)$ · $\lnot(\exists x,\ P(x))\equiv\forall x,\ \lnot P(x)$"
_ORDREQ = r"$\forall x,\ \exists y$ : $y$ peut dépendre de $x$ · $\exists y,\ \forall x$ : le même $y$ pour tous les $x$"
_CE = r"un contre-exemple suffit pour montrer qu'un « pour tout » est faux"
_CONTRA = r"contraposée : $(A\Rightarrow B)\equiv(\lnot B\Rightarrow\lnot A)$"
_REC = r"récurrence : initialisation $P(n_0)$, hérédité $P(n)\Rightarrow P(n+1)$"
_INCL = r"$A\subset B\iff\forall x,\ x\in A\Rightarrow x\in B$"
_IMG = r"$f(I)=\{f(x),\ x\in I\}$ · $f^{-1}(J)=\{x\in A,\ f(x)\in J\}$"
_INJ = r"injective : $f(x)=f(x')\Rightarrow x=x'$"
_SURJ = r"surjective : $\forall y\in B,\ \exists x\in A,\ f(x)=y$"
_BIJ = r"bijective : tout $y\in B$ a un unique antécédent ; résoudre $f(x)=y$ donne $f^{-1}$"
_RST = r"réflexive : $aRa$ · symétrique : $aRb\Rightarrow bRa$ · antisymétrique : $aRb$ et $bRa\Rightarrow a=b$ · transitive : $aRb$ et $bRc\Rightarrow aRc$"
FORMULES = {
    "lg1": r"$P\land Q$ vraie si les deux le sont · $P\lor Q$ vraie si au moins une l'est · " + _IMPL
           + r" · $P\iff Q$ vraie si même valeur",
    "lg2": _IMPL, "lg3": _IMPL,
    "lg4": _MORGAN + r" · $\lnot\lnot Q\equiv Q$",
    "cn1": _CE + r" · sur $\mathbb R_+$, $x\mapsto x^2$ est croissante",
    "cn2": r"$(A\Rightarrow B)$ vraie $\iff$ l'ensemble des solutions de $A$ est inclus dans celui de $B$ · $x^2>a^2\iff x<-a$ ou $x>a$ ($a\ge0$)",
    "cn3": r"$(A\Rightarrow B)$ vraie $\iff$ l'ensemble des solutions de $A$ est inclus dans celui de $B$ · " + _CE,
    "cn4": r"$A\Rightarrow B$ : $A$ est suffisante pour $B$, $B$ est nécessaire pour $A$",
    "ng1": _MORGAN, "ng5": _MORGAN,
    "ng2": _NIMPL, "ng3": _NIMPL + " · " + _MORGAN, "ng4": _NIMPL + " · " + _MORGAN,
    "qt1": _ORDREQ, "qt2": _ORDREQ, "qt3": _ORDREQ,
    "qt4": r"majorée : $\exists M,\ \forall x,\ f(x)\le M$",
    "nq1": _NQ, "nq2": _NQ, "nq4": _NQ,
    "nq3": _NQ + " · " + _NIMPL + r" · croissante : $\forall x,y,\ x\le y\Rightarrow f(x)\le f(y)$",
    "rs1": _CONTRA + r" · réciproque : $B\Rightarrow A$",
    "rs2": _CONTRA + r" · impair : $n=2k+1$",
    "rs3": _CONTRA + " · " + _NQ,
    "rs4": r"absurde : supposer $\lnot P$ et aboutir à une contradiction · $p^2$ pair $\Rightarrow p$ pair",
    "rc1": _REC, "rc2": _REC, "rc3": _REC, "rc4": _REC,
    "en1": _INCL,
    "en2": r"$B\not\subset A\iff\exists x\in B,\ x\notin A$ (un contre-exemple)",
    "en3": r"$A=B\iff A\subset B$ et $B\subset A$ · " + _MORGAN,
    "en4": r"$|\mathcal P(E)|=2^{|E|}$ · parties à $p$ éléments : $\binom np$",
    "im1": _IMG, "im2": _IMG, "im3": _IMG, "im4": _IMG, "im5": _IMG,
    "ij1": _INJ + " · " + _SURJ, "ij2": _INJ + " · " + _SURJ, "ij3": _INJ + " · " + _SURJ,
    "ij4": _BIJ, "ij5": _INJ + " · " + _SURJ + " · " + _BIJ,
    "rl1": _RST, "rl2": _RST,
    "rl3": _RST + r" · équivalence : réflexive, symétrique, transitive",
    "rl4": _RST + r" · ordre : réflexive, antisymétrique, transitive · total : $\forall a,b,\ aRb$ ou $bRa$",
    "oh1": _IMG + " · " + _INCL,
    "oh2": _INJ,
    "oh3": _BIJ,
    "oh4": r"parmi $k$ entiers consécutifs, un est multiple de $k$ · " + _REC,
    "oh5": _NQ,
}
