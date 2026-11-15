# Contrôle S2 — mars 2022 (corrigé, FR)

- Source : `raw/S2/Midterms/Maths PC/2026/midterm-2026-s2-maths-correction-fr.pdf` (4 pages)
- Date réelle : mars 2022 (dossier promo 2026). Sujet : `midterm-2026-s2-maths-subject-fr.md`.
- Corrigé officiel.

## Exercice 1 (5,5 points)
Type : EDO linéaires 1er ordre (variation de la constante) et 2nd ordre · ECUE : APIS (EDO) · Niveau : maths-s1-apis-edo/11
Formules : $y' + a(x)y = 0 \Rightarrow y = ke^{-A(x)}$, $A' = a$ ; solution générale = homogène + particulière ; variation de la constante $y_p = k(x)y_0(x)$ ; $ay'' + by' + cy = 0$ : $ar^2 + br + c = 0$, racine double $r$ : $y = (k_1x + k_2)e^{rx}$ ; second membre $P(x)e^{rx}$ : $y_p = Q(x)e^{rx}$

1. $(E)$ : $xy' + \frac12y = -2$ sur $]0, +\infty[$.
   - $(E_0)$ : $xy' + \frac12y = 0$ : $y_0(x) = ke^{-\int \frac1{2x}dx} = ke^{-\frac12\ln x} = \dfrac k{\sqrt x}$, $k \in \mathbb{R}$.
   - Solution particulière évidente : $y_p : x \mapsto -4$.
   - $S = \Big\{ x \mapsto \dfrac k{\sqrt x} - 4,\ k \in \mathbb{R} \Big\}$.
2. $(E)$ : $2y'' + 8y' + 8y = 3e^{-2x}$ sur $\mathbb{R}$.
   - $(E_0)$ : équation caractéristique $2r^2 + 8r + 8 = 2(r+2)^2 = 0$, racine double $-2$ : $y_0(x) = (k_1x + k_2)e^{-2x}$.
   - On cherche $y_p(x) = Q(x)e^{-2x}$ : $y_p' = (Q' - 2Q)e^{-2x}$, $y_p'' = (Q'' - 4Q' + 4Q)e^{-2x}$. En réinjectant : $2Q''(x) = 3$. On choisit $Q'(x) = \frac32x$, $Q(x) = \frac{3x^2}4$ : $y_p(x) = \dfrac{3x^2}4e^{-2x}$.
   - $S = \Big\{ x \mapsto (k_1x + k_2)e^{-2x} + \dfrac{3x^2}4e^{-2x},\ (k_1,k_2) \in \mathbb{R}^2 \Big\}$.

## Exercice 2 (5 points)
Type : petit o, équivalents et développements limités (manipulation) · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/10
Formules : $f = o(x^n) \iff f(x) = x^n\varepsilon(x)$, $\varepsilon \to 0$ ; $o(x^3) \Rightarrow o(x^2)$ (pas l'inverse) ; $o(x^p) + o(x^q) = o(x^{\min(p,q)})$ ; $f \sim$ premier terme non nul du DL ; $f \sim g \iff f - g = o(g)$ ; $\lim \frac{f}{x^n} = a \neq 0 \iff f \sim ax^n$

1. (a) $f(x) = x^3\phi(x)$ avec $\phi(x) \to 0$, donc $f(x) = x^2(x\phi(x))$ avec $x\phi(x) \to 0$ : $f(x) = o(x^2)$. En revanche on ne peut pas dire que $f(x) = o(x^4)$.
   (b) $f(x) - 2g(x) = x^2\big(x\phi(x) - 2\varepsilon(x)\big)$ avec $x\phi(x) - 2\varepsilon(x) \to 0$. Donc $f(x) - 2g(x) = o(x^2)$ (pas mieux) : $n = 2$.
2. $f(x) \sim 1$ et $g(x) \sim 2x$. $2xf(x) - g(x) = 2x + 2x^2 + o(x^2) - 2x - x^2 + o(x^2) = x^2 + o(x^2)$, donc $2xf(x) - g(x) \sim x^2$.
3. Par exemple $h(x) = -3x + 5x^2 + \pi x^3 + o(x^3)$ (le coefficient de $x^3$ est libre).
4. Une seule réponse : $i(x) = 2x^4 + o(x^4)$.

## Exercice 3 (5 points)
Type : développements limités usuels et composés · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/8
Formules : $e^u = \sum \frac{u^k}{k!}$ ; $\cos u = 1 - \frac{u^2}2 + \frac{u^4}{24}$ ; $\sin u = u - \frac{u^3}6$ ; $\ln(1+u) = u - \frac{u^2}2 + \frac{u^3}3 - \frac{u^4}4$ ; $\sqrt{1+u} = 1 + \frac u2 - \frac{u^2}8 + \frac{u^3}{16} - \frac{5u^4}{128}$ ; $(1+u)^\alpha = 1 + \alpha u + \frac{\alpha(\alpha-1)}2u^2$ ; produit tronqué ; composition : poser $u$, calculer $u^2$ à l'ordre voulu ; $1 + \cos 2x = 2\cos^2 x$

1. $f(x) = \Big(2x - \frac{(2x)^3}6 + o(x^3)\Big)\Big(1 - x + \frac{x^2}2 - \frac{x^3}6 + o(x^3)\Big) = 2x - 2x^2 + x^3 - \frac{4x^3}3 + o(x^3) = 2x - 2x^2 - \dfrac{x^3}3 + o(x^3)$.
2. $g(x) = \ln\Big(2 + x - \frac{x^2}2 + o(x^3)\Big) = \ln 2 + \ln\Big(1 + \frac x2 - \frac{x^2}4 + o(x^3)\Big)$. Posons $u = \frac x2 - \frac{x^2}4 + o(x^3) \to 0$ : $u^2 = \frac{x^2}4 - \frac{x^3}4 + o(x^3)$, $u^3 = \frac{x^3}8 + o(x^3)$. Avec $\ln(1+u) = u - \frac{u^2}2 + \frac{u^3}3 + o(u^3)$ :
   $g(x) = \ln 2 + \dfrac x2 - \dfrac{3x^2}8 + \dfrac{x^3}6 + o(x^3)$.

## Exercice 4 (5 points)
Type : développements limités, limite par équivalents · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/9
Formules : en 0 : $e^x = 1 + x + \frac{x^2}2 + \frac{x^3}6 + o(x^3)$ ; $\ln(1+x) = x - \frac{x^2}2 + o(x^2)$ ; $\cos x = 1 - \frac{x^2}2 + o(x^3)$ ; $\sin x = x - \frac{x^3}6 + o(x^3)$ ; $\frac1{1-x} = 1 + x + x^2 + x^3 + o(x^3)$ ; produit de DL tronqué à l'ordre ; $a^b = e^{b\ln a}$ ; $f \sim g \Rightarrow$ même limite

1. $N(x) = \sqrt{1 + 2x^2} - \cos(2x^2) - x^2 = 1 + x^2 - \frac18(4x^4) - \Big(1 - \frac{4x^4}2\Big) - x^2 + o(x^4) = \frac{3x^4}2 + o(x^4)$, donc $N(x) \sim \frac{3x^4}2$.
   $D(x) = e^{-x} + \sin x - 1 = 1 - x + \frac{x^2}2 + x - 1 + o(x^2) = \frac{x^2}2 + o(x^2)$, donc $D(x) \sim \frac{x^2}2$.
   $\dfrac{N(x)}{D(x)} \sim 3x^2 \to 0$ : la limite vaut 0.
2. $\Big(x\sin\frac1x\Big)^{x^2} = e^{x^2\ln(x\sin\frac1x)}$ et $x\sin\frac1x = x\Big(\frac1x - \frac1{6x^3} + o\big(\frac1{x^3}\big)\Big) = 1 - \frac1{6x^2} + o\big(\frac1{x^2}\big)$. Donc $x^2\ln\big(x\sin\frac1x\big) = x^2\Big(-\frac1{6x^2} + o\big(\frac1{x^2}\big)\Big) = -\frac16 + o(1)$. La limite vaut $e^{-1/6}$.

## Exercice 5 (6 points)
Type : reconnaître un sous-espace vectoriel · ECUE : EV · Niveau : maths-s2-ev/3
Formules : sev : contient 0, stable par addition et multiplication par un scalaire ; contre-exemple $\lambda u \notin E$ ; équation non linéaire ($z^2$) $\Rightarrow$ en général pas un sev ; $\mathrm{Vect}(\dots)$ est toujours un sev

1. $(u_n) = (2) \in E$ mais $-(u_n) = (-2) \notin E$ ($-2 < -1$). $E$ n'est pas un $\mathbb{R}$-ev.
2. $F \subset \mathbb{R}^3$ ; $0_{\mathbb{R}^3} = 0e_1 + 0e_2 \in F$ ; si $u = ae_1 + be_2$, $v = a'e_1 + b'e_2$ et $\alpha \in \mathbb{R}$, $\alpha u + v = (\alpha a + a')e_1 + (\alpha b + b')e_2 \in F$. $F$ est un sev de $\mathbb{R}^3$, donc un $\mathbb{R}$-ev.
3. $G \subset \mathbb{R}^{\mathbb{R}}$ ; la fonction nulle est dans $G$ ; si $f(x) = x\varepsilon(x)$, $g(x) = x\phi(x)$ avec $\varepsilon, \phi \to 0$ et $\alpha \in \mathbb{R}$, $\alpha f + g = x(\alpha\varepsilon(x) + \phi(x))$ avec $\alpha\varepsilon + \phi \to 0$, donc $\alpha f + g \in G$. $G$ est un sev de $\mathbb{R}^{\mathbb{R}}$, donc un $\mathbb{R}$-ev.

## Exercice 6 (4,5 points)
Type : divisibilité de polynômes, multiplicité, factorisation dans $\mathbb{R}[X]$ et $\mathbb{C}[X]$ · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/9
Formules : $P(a) = 0 \iff X - a \mid P$ ; racine d'ordre $\geqslant 2$ $\iff P(a) = P'(a) = 0$ ; ordre exactement $m$ : $P^{(m)}(a) \neq 0$ ; $(X - a)^m \mid P$, $(X - a)^{m+1} \nmid P$ ; $X^2 + 1 = (X - i)(X + i)$ ; $\Delta < 0 \Rightarrow$ irréductible dans $\mathbb{R}[X]$

1. $P_n(X) = X^{n-3}(X^4 - 2X^3 + 2X^2 - 2X + 1) = X^{n-3}Q(X)$ avec $Q(0) = 1 \neq 0$ : $X^{n-3} \mid P_n$ et $X^{n-2} \nmid P_n$. 0 est racine d'ordre exactement $n - 3$.
2. Il suffit d'étudier $Q$. $Q(1) = 1 - 2 + 2 - 2 + 1 = 0$. $Q'(X) = 4X^3 - 6X^2 + 4X - 2$, $Q'(1) = 0$. $Q''(X) = 12X^2 - 12X + 4$, $Q''(1) = 4 \neq 0$. 1 est racine de $Q$ (donc de $P_n$) d'ordre exactement 2.
3. $P_{11}(X) = X^8Q(X)$ et $(X-1)^2 \mid Q$. Division euclidienne de $Q$ par $(X-1)^2 = X^2 - 2X + 1$ : $Q(X) = (X^2 - 2X + 1)(X^2 + 1)$. $X^2 + 1$ a un discriminant strictement négatif : irréductible dans $\mathbb{R}[X]$.
   $P_{11}(X) = X^8(X-1)^2(X^2+1)$.

## Exercice 7 (4 points)
Type : divisibilité de polynômes, multiplicité d'une racine · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/4
Formules : $(X-a)(X-b) \mid P \iff P(a) = P(b) = 0$ ($a \neq b$) ; $\alpha$ racine d'ordre $m$ $\iff P(\alpha) = \dots = P^{(m-1)}(\alpha) = 0$, $P^{(m)}(\alpha) \neq 0$ ; $(X^n)' = nX^{n-1}$

1. $(X-1)^2 \mid A$ donc $A(1) = A'(1) = 0$. $(X+1)^2 \mid B$ donc $B(-1) = B'(-1) = 0$.
2. $A' = B' = P'$. Donc $P(1) = 1$, $P(-1) = -1$, $P'(1) = 0$ et $P'(-1) = 0$.
3. $P'(1) = 0$ : $3a + 2b + c = 0$ ; $P'(-1) = 0$ : $3a - 2b + c = 0$ ; $P(1) = 1$ : $a + b + c + d = 1$ ; $P(-1) = -1$ : $-a + b - c + d = -1$. $L_1 - L_2$ : $b = 0$ ; $L_1 + L_2$ : $c = -3a$ ; $L_3 + L_4$ : $2b + 2d = 0$, $d = 0$ ; $L_3 - L_4$ : $2a + 2c = 2$, donc $a = -\frac12$, $c = \frac32$.
   Un seul polynôme vérifie $(H)$ : $P(X) = -\dfrac{X^3}2 + \dfrac{3X}2$.
