# Contrôle 2 — février 2017 (sujet, FR)

- Source : `raw/S2/Midterms/Maths PC/2021/midterm-2021-s2-maths-subject-fr.pdf` (scan, 6 pages)
- Date réelle : février 2017 (Info-Sup 16/17, dossier promo 2021). Corrigé (EN) : `midterm-2021-s2-maths-correction-en.md`.
- Durée : trois heures. Documents et calculatrices non autorisés. Barème : 21 points.

## Exercice 1 (4,5 points)
Type : IPP et changement de variable · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/13
Formules : IPP : $\int_a^b uv' = [uv]_a^b - \int_a^b u'v$ ($u = \ln$, $v' = 1$) ; changement de variable : $x = \varphi(t)$, $dx = \varphi'(t)\,dt$, bornes transformées ; $t = \sqrt{1-x} \Rightarrow x = 1 - t^2$, $dx = -2t\,dt$ ; $t = e^{-x} \Rightarrow dx = -\frac{dt}t$ ; $\int \frac{dt}{1+t} = \ln(1+t)$ ; $\int t^n = \frac{t^{n+1}}{n+1}$

1. Via une double intégration par parties, calculer $I = \displaystyle\int_1^e \sin(\ln(x))\,dx$.
2. Via une intégration par parties, calculer $J = \displaystyle\int_0^1 \arctan(x)\,dx$.
3. Via le changement de variable $u = \sqrt x$ puis une intégration par parties, calculer $K = \displaystyle\int_0^{\pi^2} \cos(\sqrt x)\,dx$.

## Exercice 2 (3 points)
Type : comparaison et limites · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/6
Formules : $u_n \leqslant v_n$ et $v_n \to -\infty \Rightarrow u_n \to -\infty$ ; $u_n \leqslant v_n$ et $u_n \to +\infty \Rightarrow v_n \to +\infty$ ; pour une limite finie, il faut deux gendarmes

Soient $(u_n)$ et $(v_n)$ deux suites réelles strictement positives telles que pour tout $n \in \mathbb{N}$, $\dfrac{u_{n+1}}{u_n} \leqslant \dfrac{v_{n+1}}{v_n}$.
1. Montrer que si $v_n \to 0$ alors $u_n \to 0$.
2. Montrer que si $u_n \to +\infty$ alors $v_n \to +\infty$.

## Exercice 3 (3 points)
Type : propriétés de suites et suites extraites (vrac) · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/11
Formules : $q^n$ ($q > 1$) croissante non bornée ; $(-1)^n$ bornée divergente ; suite extraite d'une convergente converge vers la même limite ; $(u_{2n})$ et $(u_{2n+1})$ même limite $\Rightarrow (u_n)$ converge ; $(u_{3n})$, $(u_{3n+1})$ ne couvrent pas $(u_{3n+2})$

Encadrer le numéro des questions contenant les énoncés vrais (les réponses erronées ne retirent pas de point).
1. Soient $(u_n)$ une suite réelle et $\ell \in \mathbb{R}$. L'assertion « si $(u_n)$ converge vers $\ell$ alors, pour tout $n$, $u_n \leqslant \ell$ » est équivalente à « s'il existe $n$ tel que $u_n > \ell$, alors $(u_n)$ ne converge pas vers $\ell$ ».
2. Si $(u_n)$ est géométrique non nulle de raison $q \in \mathbb{R}^*$, alors $\left(\frac1{u_n}\right)$ est géométrique de raison $\frac1q$.
3. Si $(u_n)$ est bornée, il existe une suite extraite de $(u_n)$ convergente.
4. $(u_{6n})$ est extraite de $(u_{2n})$.
5. $(u_{3 \cdot 2^{n+1}})$ est extraite de $(u_{6n})$.
6. Rien de ce qui précède.

## Exercice 4 (3 points)
Type : suites adjacentes · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/9
Formules : adjacentes : $(u_n)$ croissante, $(v_n)$ décroissante, $v_n - u_n \to 0$ ; alors elles convergent vers la même limite ; $\frac1{(n+1)!} = \frac1{n!} \cdot \frac1{n+1}$

Soient $(u_n)$ et $(v_n)$ définies pour tout $n \in \mathbb{N}$ par $u_n = \displaystyle\sum_{k=0}^{2n+1} \frac{(-1)^k}{(2k)!}$ et $v_n = u_n + \dfrac1{(4n+4)!}$. Montrer que $(u_n)$ et $(v_n)$ sont adjacentes.

## Exercice 5 (2 points)
Type : comparaison et limites · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/6
Formules : $u_n \leqslant v_n$ et $v_n \to -\infty \Rightarrow u_n \to -\infty$ ; $u_n \leqslant v_n$ et $u_n \to +\infty \Rightarrow v_n \to +\infty$ ; pour une limite finie, il faut deux gendarmes

Soit $(u_n)_{n \in \mathbb{N}^*}$ définie par $u_n = \dfrac{\ln(n!)}{n^2}$.
1. Soit $n \in \mathbb{N}^*$. Montrer (sans récurrence) que $\ln(n!) \leqslant n\ln(n)$.
2. En déduire la limite de la suite $(u_n)$.

## Exercice 6 (5,5 points)
Type : suites adjacentes ($\sum 1/k!$) · ECUE : APIS (suites) · Niveau : maths-s1-apis-suites/8
Formules : adjacentes : $(u_n)$ croissante, $(v_n)$ décroissante, $v_n - u_n \to 0$ ; $u_{n+1} - u_n = \frac1{(n+1)!}$ ; $\frac1{n!} = \frac{n+1}{(n+1)!}$ ; adjacentes $\Rightarrow$ convergentes ; convergente $\Rightarrow$ bornée

Soit $(u_n)$ définie pour tout $n \in \mathbb{N}$ par $u_n = \displaystyle\sum_{k=0}^n \frac1{k!}$.
1. Soient $n \in \mathbb{N}^*$ et $q \in \mathbb{R} \setminus \{1\}$. Que vaut $\sum_{k=1}^n q^{k-1}$ ?
2. Via la question précédente, montrer (sans récurrence) que $\sum_{k=1}^n \frac1{2^{k-1}} = 2 - \frac1{2^{n-1}}$.
3. Soit $k \geqslant 2$. Montrer (sans récurrence) que $\frac1{k!} = \frac1{2 \times 3 \times \dots \times k} \leqslant \frac1{2^{k-1}}$. Vérifier que l'inégalité est encore vraie pour $k = 1$.
4. Montrer que $(u_n)$ est croissante.
5. Montrer (sans récurrence), via les questions 2 et 3, que pour tout $n$, $u_n \leqslant 3$.
6. $(u_n)$ est-elle convergente ? Justifier votre réponse.
