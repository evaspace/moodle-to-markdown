# Correction du contrôle S1 — novembre 2021

- Source : `raw/S1/Midterms/Maths PC/2026/midterm-2026-s1-maths-correction-fr.pdf` (5 pages)
- Date réelle : novembre 2021 (dossier promo 2026). Sujet : `midterm-2026-s1-maths-subject-fr.md` (énoncés repris en abrégé).
- Fractions perdues par la couche texte du PDF recalculées et vérifiées.

## Exercice 1
Type : relation d'ordre · ECUE : OBM · Niveau : maths-s1-obm/11
Formules : ordre = réflexive ($\forall x, x\mathcal Rx$), antisymétrique ($x\mathcal Ry$ et $y\mathcal Rx \Rightarrow x = y$), transitive ($x\mathcal Ry$ et $y\mathcal Rz \Rightarrow x\mathcal Rz$) ; contre-exemple pour réfuter ; $x^2 = y^2 \iff x = \pm y$

- Réflexive : $\forall x \in \mathbb{R}$, $x\,\mathcal{R}\,x$. Comme $x^2 \leqslant x^2$, $\mathcal{R}$ est réflexive.
- Antisymétrique : $\forall (x,y) \in \mathbb{R}^2$, $x\,\mathcal{R}\,y$ et $y\,\mathcal{R}\,x \implies x = y$. Avec $x = -1$, $y = 1$ : $x^2 = y^2 = 1$ donc $x\,\mathcal{R}\,y$ et $y\,\mathcal{R}\,x$, pourtant $x \neq y$. Pas antisymétrique.
- Transitive : $\forall (x,y,z) \in \mathbb{R}^3$, $x\,\mathcal{R}\,y$ et $y\,\mathcal{R}\,z \implies x\,\mathcal{R}\,z$. $x^2 \leqslant y^2 \leqslant z^2$ donne $x\,\mathcal{R}\,z$. Transitive.
$\mathcal{R}$ n'est pas une relation d'ordre.

## Exercice 2
Type : traduire avec quantificateurs · ECUE : OBM · Niveau : maths-s1-obm/4
Formules : « tout » $= \forall$, « il existe » $= \exists$, « aucun » $= \forall \dots \neg$ ; l'ordre $\forall\exists$ / $\exists\forall$ change le sens ; $f$ s'annule : $\exists x, f(x) = 0$ ; minimum en $a$ : $\exists a, \forall x, f(x) \geqslant f(a)$ ; pair : $\exists k, n = 2k$

1. $\forall x \in \mathbb{R}^+, \exists y \in \mathbb{R}, x = y^2$.
2. $\forall (x,y) \in \mathbb{R}^2, xy = 0 \implies (x = 0$ ou $y = 0)$.
3. $\forall n \in \mathbb{N}, \exists p \in \mathbb{N}, n = 2p$ ou $n = 2p + 1$.

## Exercice 3
Type : primitive directe $u'u^\alpha$, IPP, changement de variable affine vers arctan · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/13
Formules : $\int u'u^\alpha = \frac{u^{\alpha+1}}{\alpha+1}$ ($\alpha = \frac12$ : $\frac23u^{3/2}$) ; IPP $\int uv' = [uv] - \int u'v$ ; $\int e^{2x} = \frac{e^{2x}}2$ ; $x = 2t + 1$, $dx = 2\,dt$, bornes transformées ; $\int \frac{dt}{1 + t^2} = \arctan t$ ; $\arctan\sqrt3 = \frac\pi3$

1. $I = \dfrac13\displaystyle\int_0^1 (3x^2 + 3)\sqrt{x^3 + 3x + 1}\,dx$ : forme $u'u^\alpha$ avec $\alpha = \frac12$.
$I = \dfrac13\left[\dfrac{(x^3 + 3x + 1)^{3/2}}{3/2}\right]_0^1 = \dfrac29\left(5\sqrt5 - 1\right)$.
2. $u = 2x + 1$, $v' = e^{2x}$, $u' = 2$, $v = \frac{e^{2x}}2$ :
$J = \left[\dfrac{(2x+1)e^{2x}}2\right]_0^1 - \displaystyle\int_0^1 e^{2x}\,dx = \dfrac{3e^2}2 - \dfrac12 - \dfrac{e^2}2 + \dfrac12 = e^2$.
3. $x = 2t + 1 \iff t = \frac{x - 1}2$, $dx = 2\,dt$ ; $x = 1 \to t = 0$, $x = 2\sqrt3 + 1 \to t = \sqrt3$.
$K = \displaystyle\int_0^{\sqrt3} \frac{2\,dt}{4t^2 + 4} = \frac12\int_0^{\sqrt3} \frac{dt}{t^2 + 1} = \frac12[\arctan t]_0^{\sqrt3} = \frac12 \cdot \frac\pi3 = \frac\pi6$.

## Exercice 4
Type : injectivité, surjectivité, image directe et réciproque · ECUE : OBM · Niveau : maths-s1-obm/10
Formules : injective : $f(x) = f(y) \Rightarrow x = y$ (contre-exemple $f(1) = f(2)$) ; surjective : $\forall y, \exists x, f(x) = y$ ; $f(A) = \{f(x), x \in A\}$ ; $f^{-1}(B) = \{x, f(x) \in B\}$ (peut être vide)

1. $f(1) = 1 = f(2)$ et $1 \neq 2$ : $f$ n'est pas injective.
2. Pour $n \in \mathbb{N}$, $f(2n) = \frac{2n}2 = n$ : $\forall n, \exists m = 2n, n = f(m)$. $f$ est surjective.
3. Valeurs sur $E$ : $f(0) = 0$, $f(1) = 1$, $f(2) = 1$, $f(3) = 3$, $f(4) = 2$, $f(5) = 5$, $f(6) = 3$.
$f(\{0,1,2,3\}) = \{0, 1, 3\}$, $f^{-1}(\{1,3\}) = \{1, 2, 3, 6\}$ et $f^{-1}(\{4\}) = \emptyset$.

## Exercice 5
Type : combinaisons, formule de Pascal · ECUE : DP · Niveau : maths-s1-dp/6
Formules : tirage simultané : $\binom nk$ ; contenant un élément fixé : $\binom{n-1}{k-1}$ ; ne le contenant pas : $\binom{n-1}k$ ; Pascal : $\binom{n-1}{k-1} + \binom{n-1}{k} = \binom nk$ ; $\binom nk = \frac{n!}{k!(n-k)!}$ ; mettre au même dénominateur $k!(n-k)!$

1. Tirage simultané : $k$ éléments parmi $n$, $\mathrm{Card}(E) = \binom nk$.
2. Une seule façon de prendre la boule 1, puis $k - 1$ boules parmi $n - 1$ : $\mathrm{Card}(F) = \binom{n-1}{k-1}$.
3. $k$ boules parmi les $n - 1$ autres : $\mathrm{Card}(\bar F) = \binom{n-1}{k}$.
4. $E = F \cup \bar F$, union disjointe, donc $\binom nk = \binom{n-1}{k-1} + \binom{n-1}{k}$.
5. $\dbinom{n-1}{k} + \dbinom{n-1}{k-1} = \dfrac{(n-1)!}{k!(n-k-1)!} + \dfrac{(n-1)!}{(k-1)!(n-k)!} = \dfrac{(n-1)!(n-k) + (n-1)!\,k}{k!(n-k)!} = \dfrac{(n-1)!\,n}{k!(n-k)!} = \dbinom nk$.

## Exercice 6
Type : loi de Bernoulli, loi binomiale, espérance et variance · ECUE : DP · Niveau : maths-s1-dp/14
Formules : Bernoulli $\mathcal{B}(p)$ : $E = p$, $V = p(1-p)$ ; binomiale $\mathcal{B}(n,p)$ : $P(Y = k) = \binom nk p^k(1-p)^{n-k}$, $E = np$, $V = np(1-p)$ ; $E(G) = \sum x_iP(G = x_i)$ ; $V(G) = E(G^2) - E(G)^2$ (König-Huygens)

1. On lance une fois le dé ; $X = 1$ si le résultat est 1, $X = 0$ sinon. $P(X = 1) = \frac16$, $P(X = 0) = \frac56$ : $X \sim \mathcal{B}\left(\frac16\right)$, $E(X) = p = \frac16$, $V(X) = p(1-p) = \frac5{36}$.
2. On répète 10 fois l'expérience (lancers indépendants) ; $Y$ = nombre de 1 obtenus. $Y$ prend ses valeurs dans $[\![0,10]\!]$ et $P(Y = k) = \binom{10}k\left(\frac16\right)^k\left(\frac56\right)^{10-k}$. $E(Y) = np = \frac{10}6 = \frac53$, $V(Y) = np(1-p) = \frac{50}{36} = \frac{25}{18}$.
3. $G \in \{5, 3, 0\}$. $P(G = 5) = \frac26 = \frac13$ (3 et 6), $P(G = 3) = \frac16 + \frac16 = \frac13$, $P(G = 0) = \frac13$ (4 et 5).
$E(G) = 3 \times \frac13 + 5 \times \frac13 = \frac83$ ; $E(G^2) = 9 \times \frac13 + 25 \times \frac13 = \frac{34}3$ ; $V(G) = E(G^2) - E(G)^2 = \frac{34}3 - \frac{64}9 = \frac{38}9$.

## Exercice 7
Type : probabilités totales et Bayes · ECUE : DP · Niveau : maths-s1-dp/10
Formules : probabilités totales : $P(M) = P(M \mid V)P(V) + P(M \mid \bar V)P(\bar V)$ ; Bayes : $P(V \mid M) = \frac{P(M \mid V)P(V)}{P(M)}$ ; $P(\bar V) = 1 - P(V)$

1. $(M, \bar M)$ forment une partition de l'univers : $T = (T \cap M) \cup (T \cap \bar M)$, union disjointe.
$P(T) = P(T \mid M)P(M) + P(T \mid \bar M)P(\bar M) = 0{,}99 \times 0{,}25 + 0{,}2 \times 0{,}75 = 0{,}3975 \simeq 0{,}40$.
2. $P(M \mid T) = \dfrac{P(T \cap M)}{P(T)} = \dfrac{P(T \mid M)P(M)}{P(T)} = \dfrac{0{,}99 \times 0{,}25}{0{,}3975} \simeq 0{,}62$.

## Exercice 8
Type : récurrence (somme géométrique) · ECUE : OBM · Niveau : maths-s1-obm/7
Formules : récurrence ; $S_{n+1} = S_n + q^{n+1}$ ; $\sum_{k=0}^n q^k = \frac{1 - q^{n+1}}{1 - q}$ ($q \neq 1$), $= n + 1$ si $q = 1$

1. $S_n = 1 + 1 + \dots + 1$ avec $n + 1$ termes : $S_n = n + 1$.
2. $n = 0$ : $S_0 = q^0 = 1$ et $\frac{1 - q^1}{1 - q} = 1$. Hérédité : $S_{n+1} = S_n + q^{n+1} = \dfrac{1 - q^{n+1}}{1 - q} + q^{n+1} = \dfrac{1 - q^{n+1} + q^{n+1} - q^{n+2}}{1 - q} = \dfrac{1 - q^{n+2}}{1 - q}$. Conclusion : $\forall n$, $S_n = \frac{1 - q^{n+1}}{1 - q}$.
