# Feuille de TD — Équations différentielles linéaires (S2 2026) (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (pas de corrigé officiel). Sujet : `td2-2030-s2-maths-subject-fr.md` (même dossier). Calculs vérifiés avec sympy. 

## Exercice 1.1
Type : EDO linéaires 1er ordre (homogène, solution évidente, variation de la constante, condition initiale) · ECUE : APIS (EDO) · Niveau : maths-s1-apis-edo/6
Formules : $a(x)y' + b(x)y = 0 \Rightarrow y_0 = ke^{-\int \frac ba}$ ; solution générale = $y_0 + y_p$ ; solution évidente (constante, ou de la forme du second membre) ; variation de la constante : $y_p = k(x)y_0(x)$, il reste $a\,k'\,y_0 = c$ ; condition initiale : remplacer pour trouver $k$ ; $\int \frac{dx}{x\ln x} = \ln|\ln x|$, $\int \frac{dx}{1+x^2} = \arctan x$, $\int \tan = -\ln|\cos|$

1. $y'=\dfrac2xy$ : $y(x)=Cx^2$, $C\in\mathbb R$.
2. $y=-1$ est solution particulière ; homogène $y'=\dfrac y{x^2+1}$ : $Ce^{\arctan x}$. $y(x)=Ce^{\arctan x}-1$.
3. $y=-4$ solution particulière ; homogène $\dfrac{y'}y=\dfrac1{x\ln x}$ : $C\ln x$. $y(x)=C\ln x-4$.
4. Homogène $Ce^{-x}$ ; particulière $\dfrac12e^x-1$ ($y'+y=\frac12e^x+\frac12e^x-1$). $y(x)=Ce^{-x}+\dfrac12e^x-1$.
5. $y=e^x$ est solution évidente ($e^x-2xe^x=(1-2x)e^x$). Homogène : $Ce^{x^2}$. $y(x)=Ce^{x^2}+e^x$.
6. Homogène : $C(x+1)^2$. Variation de la constante : $C'(x)(x+1)^2=(x+1)^3$, $C'=x+1$, $C=\dfrac{(x+1)^2}2+K$. $y(x)=\dfrac{(x+1)^4}2+K(x+1)^2$.
7. Solution polynomiale $y=ax^2+bx+c$ : $3ax^3+2bx^2+(2a+c)x+b=3x^3+3x$, donc $a=1$, $b=0$, $c=1$ : $y=x^2+1$. Homogène : $\dfrac{y'}y=-\dfrac x{1+x^2}$, $\dfrac C{\sqrt{1+x^2}}$. $y(x)=x^2+1+\dfrac C{\sqrt{1+x^2}}$.
8. Homogène : $\dfrac C{\cos t}$. Variation : $y=\dfrac{C(t)}{\cos t}$ donne $C'(t)=1$, $C=t+K$. $y(t)=\dfrac{t+K}{\cos t}$ et $y(0)=K=2$ : $y(t)=\dfrac{t+2}{\cos t}$.

## Exercice 1.2
Type : modélisation par une EDO du 1er ordre (crédit) · ECUE : APIS (EDO) · Niveau : maths-s1-apis-edo/6
Formules : $y' = ay + b$ ($a \neq 0$) : $y = ke^{at} - \frac ba$ ; condition initiale $y(0) = y_0 \Rightarrow k = y_0 + \frac ba$ ; $C(t) = \big(C_0 - \frac kr\big)e^{rt} + \frac kr$ ; $C(T) = 0 \iff T = \frac1r\ln\frac{k}{k - rC_0}$ ; $e^x = a \iff x = \ln a$

1. Le capital $C$ augmente par les intérêts ($rC\,dt$ sur $dt$) et diminue des versements ($k\,dt$) : $\dfrac{dC}{dt}=rC-k$, $C(0)=C_0$.
2. Solution particulière constante $\dfrac kr$. $C(t)=\left(C_0-\dfrac kr\right)e^{rt}+\dfrac kr$.
3. Si $k\le rC_0$, les versements ne couvrent pas les intérêts : $C'(0)=rC_0-k\ge0$ et le capital ne diminue jamais, le prêt ne serait jamais remboursé. Il faut $k>rC_0$ pour que $C$ décroisse.
4. $C(T)=0\iff e^{rT}=\dfrac k{k-rC_0}$, soit $T=\dfrac1r\ln\dfrac k{k-rC_0}$.
5. $r=0{,}03$, $k=12\times500=6000$ €/an et $rC_0=0{,}03\times200000=6000$ : $k=rC_0$, cas limite exclu par la question 3 : $C(t)=C_0$ reste constant, le crédit n'est jamais remboursé (les versements ne paient que les intérêts). Lecture à confirmer : avec des versements $k>6000$ (par exemple $600$ €/mois soit $7200$ €/an) on trouve $T=\dfrac1{0{,}03}\ln\dfrac{7200}{1200}\approx59{,}7$ ans.

## Exercice 2.3
Type : EDO 2nd ordre à coefficients constants avec second membre · ECUE : APIS (EDO) · Niveau : maths-s1-apis-edo/9
Formules : $ar^2 + br + c = 0$ : deux racines réelles $k_1e^{r_1x} + k_2e^{r_2x}$ ; racine double $(k_1x + k_2)e^{rx}$ ; complexes $\alpha \pm i\beta$ : $e^{\alpha x}(k_1\cos\beta x + k_2\sin\beta x)$ ; second membre polynôme : $y_p$ polynôme de même degré ; second membre $P(x)e^{mx}$ : $y_p = Q(x)e^{mx}$ avec $\deg Q = \deg P$ (+1 si $m$ racine simple, +2 si racine double) ; solution générale = homogène + particulière

1. Équation caractéristique $r^2-2r+10=0$, $r=1\pm3i$. Particulière $-\dfrac12$. $y(x)=e^x(\lambda\cos3x+\mu\sin3x)-\dfrac12$.
2. $r^2-r-2=(r-2)(r+1)$ ; particulière $\dfrac{x^2}2+x$. $y(x)=\lambda e^{2x}+\mu e^{-x}+\dfrac{x^2}2+x$.
3. $r=-1\pm2i$ ; particulière $\dfrac{2x-1}{16}e^x$. $y(x)=e^{-x}(\lambda\cos2x+\mu\sin2x)+\dfrac{2x-1}{16}e^x$.
4. $r=2$ ou $3$ ; $2$ est racine du polynôme caractéristique : particulière $-xe^{2x}$. $y(x)=\lambda e^{2x}+\mu e^{3x}-xe^{2x}$.
5. $r=2$ double ; particulière $\dfrac{x^3}6e^{2x}$. $y(x)=\left(\lambda x+\mu+\dfrac{x^3}6\right)e^{2x}$.
6. $r=\pm i$ ; particulière $\dfrac12e^x$. $y(x)=\lambda\cos x+\mu\sin x+\dfrac12e^x$.

## Exercice 2.4
Type : EDO 2nd ordre à coefficients constants avec second membre · ECUE : APIS (EDO) · Niveau : maths-s1-apis-edo/9
Formules : $ar^2 + br + c = 0$ : deux racines réelles $k_1e^{r_1x} + k_2e^{r_2x}$ ; racine double $(k_1x + k_2)e^{rx}$ ; complexes $\alpha \pm i\beta$ : $e^{\alpha x}(k_1\cos\beta x + k_2\sin\beta x)$ ; second membre polynôme : $y_p$ polynôme de même degré ; second membre $P(x)e^{mx}$ : $y_p = Q(x)e^{mx}$ avec $\deg Q = \deg P$ (+1 si $m$ racine simple, +2 si racine double) ; solution générale = homogène + particulière

1. $r=\dfrac{-3\pm i}2$ ; particulière polynomiale $2x^3+x-1$. $y(x)=e^{-3x/2}\left(\lambda\cos\dfrac x2+\mu\sin\dfrac x2\right)+2x^3+x-1$.
2. $r=1$ ou $-3$ ; particulière $(x^2+1)e^{3x}$. $y(x)=\lambda e^x+\mu e^{-3x}+(x^2+1)e^{3x}$.
3. $4(r+2)^2=0$, $r=-2$ double ; particulière $x^2e^{-2x}$. $y(x)=(\lambda x+\mu+x^2)e^{-2x}$.
4. $r=\pm1$ ; $1$ est racine : particulière $xe^x$. $y(x)=\lambda e^x+\mu e^{-x}+xe^x$.
