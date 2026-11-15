# Contrôle de cours APEF (S2 B3) — lundi 10 février 2025 (sujet, FR)

- Source : `raw/S2/TDs/2029/td3-2029-s2-maths-subject-fr.pdf` (3 pages)
- Date réelle : 10 février 2025 (dossier promo 2029). Pas de corrigé dans les annales. Corrigé rédigé : `td3-2029-s2-maths-correction-fr.md` (même dossier).
- Durée : 1 heure. Barème sur 20 points.

## 1. Polynômes (7 points)
Type : divisibilité de polynômes, multiplicité, factorisation dans $\mathbb{R}[X]$ et $\mathbb{C}[X]$ · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/9
Formules : $P(a) = 0 \iff X - a \mid P$ ; racine d'ordre $\geqslant 2$ $\iff P(a) = P'(a) = 0$ ; ordre exactement $m$ : $P^{(m)}(a) \neq 0$ ; $(X - a)^m \mid P$, $(X - a)^{m+1} \nmid P$ ; $X^2 + 1 = (X - i)(X + i)$ ; $\Delta < 0 \Rightarrow$ irréductible dans $\mathbb{R}[X]$

Les questions sont indépendantes.
1. Soit $(A,B) \in (\mathbb{R}[X])^2$ avec $B \neq 0$. Énoncer le théorème de la division euclidienne de $A$ par $B$.
2. Soient $P \in \mathbb{R}[X]$ et $a \in \mathbb{R}$. On suppose que $a$ est une racine d'ordre de multiplicité exactement 3 de $P$.
   - (a) En termes de divisibilité, que cela signifie-t-il ?
   - (b) Donner une condition nécessaire et suffisante sur $P$ et ses dérivées pour être dans ce cas-là.
3. Soit $P \in \mathbb{R}[X]$ de degré strictement supérieur à 3. Mettre les symboles $\Rightarrow$, $\Leftarrow$ ou $\iff$ à la place des pointillés. Si aucun symbole n'est possible, mettre une croix.
   a) $X + 3 \mid P$ $\dots$ $-3$ racine de $P$. b) $(X-1)^3 \mid P$ $\dots$ $P(1) = 0$ et $P'(1) = 0$. c) $X \mid P$ $\dots$ $P(X) = X^4 - X$. d) $P(0) = P(2) = 0$ $\dots$ $X^2 - 2X \mid P$. e) $P'(1) = 0$ $\dots$ $(X-1) \mid P$.
4. Donner l'ordre de multiplicité exact de la racine 1 de $P(X) = (X-1)^4(X^2 - X)$. Justifier.
5. Donner un exemple d'un polynôme $P \in \mathbb{R}[X]$, de degré 6, qui admet $-1$ comme racine d'ordre de multiplicité exactement 3 et tel que $P(-3) = P'(-3) = 0$.
6. Soit $P(X) = X^5(2X + 4)^2(X^2 - 5X + 6)(X^2 + X + 3)$. Écrire $P$ comme produit de polynômes irréductibles dans $\mathbb{R}[X]$ (justifier brièvement).

## 2. Équations différentielles linéaires du premier ordre (5,5 points)
Type : démonstration de cours (solutions de $a(t)y' + b(t)y = 0$) · ECUE : APIS (EDO) · Niveau : maths-s1-apis-edo/4
Formules : $S_0 = \{t \mapsto ke^{-F(t)}, k \in \mathbb{R}\}$ avec $F$ primitive de $\frac ba$, $F' = \frac ba$ ; $z = y_0e^F \Rightarrow z' = (y_0' + \frac bay_0)e^F = 0 \Rightarrow z$ constante (inclusion $\subset$) ; réciproque : dériver $ke^{-F}$ et reporter (inclusion $\supset$) ; $\int \frac{u'}u = \ln|u|$, $e^{-\alpha\ln u} = u^{-\alpha}$

Soient $a$, $b$ et $c$ trois fonctions continues sur $\mathbb{R}$ telles que $\forall t \in \mathbb{R}$, $a(t) \neq 0$. On considère les équations différentielles $(E)$ : $a(t)y'(t) + b(t)y(t) = c(t)$ et $(E_0)$ : $a(t)y'(t) + b(t)y(t) = 0$. On note $S$ l'ensemble des solutions de $(E)$ et $S_0$ l'ensemble des solutions de $(E_0)$. Un professeur demande à un élève d'expliciter précisément l'ensemble $S_0$ au tableau. L'élève note alors : $S_0 = \{ t \mapsto ke^{-F(t)},\ k \in \mathbb{R} \}$.
1. Le professeur demande à l'élève d'être plus précis et d'écrire $F$ en fonction de $a$ et de $b$. Qu'écrit l'élève ? Vous donnerez aussi $F'$ en fonction de $a$ et de $b$.
2. Montrer l'inclusion $S_0 \subset \{ t \mapsto ke^{-F(t)},\ k \in \mathbb{R} \}$. On admet l'inclusion réciproque.
3. Soit $y_p$ une solution particulière de $(E)$. Donner $S$ en fonction de $S_0$ et $y_p$.
4. Continuer les 2 phrases suivantes.
   - (a) Une solution particulière évidente de $(E_1)$ : $2y' - 3y = 6$ est $\dots$
   - (b) Une solution particulière évidente de $(E_2)$ : $2y' - xy = x$ est $\dots$

## 3. Équations différentielles linéaires du second ordre (2 points)
Type : EDO 2nd ordre homogène (équation caractéristique, cours) · ECUE : APIS (EDO) · Niveau : maths-s1-apis-edo/8
Formules : $ay'' + by' + cy = 0$ : équation caractéristique $ar^2 + br + c = 0$ ; deux racines réelles $r_1 \neq r_2$ : $y = k_1e^{r_1x} + k_2e^{r_2x}$ ; racine double $r$ : $y = (k_1x + k_2)e^{rx}$ ; racines complexes $\alpha \pm i\beta$ : $y = e^{\alpha x}(k_1\cos(\beta x) + k_2\sin(\beta x))$

On considère l'équation différentielle $(E)$ : $ay'' + by' + cy = 0$ où $(a,b,c) \in \mathbb{R}^3$ avec $a \neq 0$. On note $(C)$ l'équation caractéristique associée à $(E)$. Continuer les phrases ci-dessous :
1. $(C)$ est l'équation mathématique : $\dots$
2. Si 3 et $-4$ sont les deux racines réelles de $(C)$ alors l'ensemble des solutions de $(E)$ est formé des fonctions de la forme : $\dots$
3. Si $-2 + 3i$ est une des deux racines complexes de $(C)$ alors l'ensemble des solutions de $(E)$ est formé des fonctions de la forme : $\dots$
4. Si $(C)$ admet $-7$ comme racine double réelle alors l'ensemble des solutions de $(E)$ est formé des fonctions de la forme : $\dots$

## 4. Étude locale de fonctions (5,5 points)
Type : petit o, équivalents et développements limités (manipulation) · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/10
Formules : $f = o(x^n) \iff f(x) = x^n\varepsilon(x)$, $\varepsilon \to 0$ ; $o(x^3) \Rightarrow o(x^2)$ (pas l'inverse) ; $o(x^p) + o(x^q) = o(x^{\min(p,q)})$ ; $f \sim$ premier terme non nul du DL ; $f \sim g \iff f - g = o(g)$ ; $\lim \frac{f}{x^n} = a \neq 0 \iff f \sim ax^n$

Les questions sont indépendantes.
1. Donner le développement limité au voisinage de 0 à l'ordre 4 de : (a) $\ln(1+x)$ ; (b) $\sin(x)$.
2. Soient $f$ et $g$ deux fonctions telles qu'au voisinage de 0, $f(x) = x - 2x^2 + x^3 + o(x^3)$ et $g(x) = 1 + 3x - x^2 + o(x^2)$.
   - (a) Donner (sans justifier) un équivalent simple en 0 de $f(x)$ et de $g(x) - 1$.
   - (b) Donner une autre façon d'écrire $o(x^3)$.
   - (c) À quel ordre maximal peut-on avoir le DL de $f(x) + g(x)$ ? Trouver ce DL dans ce cas-là.
   - (d) Donner le DL à l'ordre 2 de $f(x) \times g(x)$.
