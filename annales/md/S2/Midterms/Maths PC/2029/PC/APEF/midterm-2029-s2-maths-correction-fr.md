# Examen S2-B3 APEF — mars 2025 (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (pas de corrigé officiel). Sujet : `midterm-2029-s2-maths-subject-fr.md` (même dossier). Calculs vérifiés avec sympy. Pas de corrigé officiel dans les annales.

## Exercice 1 : polynômes (10 points)
Type : divisibilité de polynômes, multiplicité, factorisation dans $\mathbb{R}[X]$ et $\mathbb{C}[X]$ · ECUE : APEF (polynômes) · Niveau : maths-s2-apef-polynomes/9
Formules : $P(a) = 0 \iff X - a \mid P$ ; racine d'ordre $\geqslant 2$ $\iff P(a) = P'(a) = 0$ ; ordre exactement $m$ : $P^{(m)}(a) \neq 0$ ; $(X - a)^m \mid P$, $(X - a)^{m+1} \nmid P$ ; $X^2 + 1 = (X - i)(X + i)$ ; $\Delta < 0 \Rightarrow$ irréductible dans $\mathbb{R}[X]$

1. $P_1=X^2\,(3X^4+6X^2-X+2)$ et le facteur $3X^4+6X^2-X+2$ vaut $2\ne0$ en $0$ : $0$ est racine d'ordre exactement $2$ (le terme de plus bas degré est $2X^2$).
2. (a) $P_2(-1)=-1+2-2-8+19-10=0$. $P_2=(X+1)^2(X-2)(X^2+2X+5)$ : $-1$ est racine d'ordre exact $\alpha=2$ (le cofacteur $(X-2)(X^2+2X+5)$ vaut $-3\cdot4\ne0$ en $-1$).
   (b) $2$ est racine simple et $-1$ racine double, donc $(X-2)$ et $(X+1)^2$ divisent $P_2$ ; ils sont premiers entre eux, donc $(X-2)(X+1)^2$ divise $P_2$ : reste nul. La division donne $P_2=(X-2)(X+1)^2(X^2+2X+5)$.
   (c) $X^2+2X+5$ a pour discriminant $4-20=-16<0$ : irréductible dans $\mathbb R[X]$. Donc dans $\mathbb R[X]$ : $(X-2)(X+1)^2(X^2+2X+5)$ ; dans $\mathbb C[X]$ : $(X-2)(X+1)^2(X+1-2i)(X+1+2i)$.

## Exercice 2 : équations différentielles (10 points)
Type : EDO linéaires 1er ordre (variation de la constante) et 2nd ordre · ECUE : APIS (EDO) · Niveau : maths-s1-apis-edo/11
Formules : $y' + a(x)y = 0 \Rightarrow y = ke^{-A(x)}$, $A' = a$ ; solution générale = homogène + particulière ; variation de la constante $y_p = k(x)y_0(x)$ ; $ay'' + by' + cy = 0$ : $ar^2 + br + c = 0$, racine double $r$ : $y = (k_1x + k_2)e^{rx}$ ; second membre $P(x)e^{rx}$ : $y_p = Q(x)e^{rx}$

1. (a) $y=\dfrac13$ ($y'=y''=0$ et $9y=3$). (b) Équation caractéristique $r^2-6r+9=(r-3)^2$ : $y(x)=(\lambda x+\mu)e^{3x}+\dfrac13$, $(\lambda,\mu)\in\mathbb R^2$.
2. Sur $]0,\pi[$ : $y'-\dfrac{\cos x}{\sin x}y=x\sin x\,e^{-x}$. Solutions de l'équation homogène : $y=C\sin x$. Variation de la constante : $y=C(x)\sin x$ donne $C'(x)\sin^2x=x\sin^2x\,e^{-x}$, soit $C'(x)=xe^{-x}$ et $C(x)=-(x+1)e^{-x}+K$ (IPP). $y(x)=\big(K-(x+1)e^{-x}\big)\sin x$, $K\in\mathbb R$.

## Exercice 3 : étude locale de fonctions (10 points)
Type : petit o, équivalents et développements limités (manipulation) · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/10
Formules : $f = o(x^n) \iff f(x) = x^n\varepsilon(x)$, $\varepsilon \to 0$ ; $o(x^3) \Rightarrow o(x^2)$ (pas l'inverse) ; $o(x^p) + o(x^q) = o(x^{\min(p,q)})$ ; $f \sim$ premier terme non nul du DL ; $f \sim g \iff f - g = o(g)$ ; $\lim \frac{f}{x^n} = a \neq 0 \iff f \sim ax^n$

1. $f=o(g)\iff\dfrac fg\to0\iff\forall\varepsilon>0,\ |f|\le\varepsilon|g|$ au voisinage de $x_0$. $f\sim g\iff\dfrac fg\to1\iff f=g+o(g)$.
2. En $0$ : $P(x)\sim-3x$. En $+\infty$ : $P(x)\sim-x^4$.
3. (a) $\dfrac{f(x)}{2x}=1-\dfrac x2+o(x)\to1$ : $f\sim2x$. (b) $g\sim2$. (c) $h\sim2x\times2=4x$. (d) $xg(x)=2x-3x^3+o(x^4)$, donc $k(x)=2x-x^2-2x+o(x^2)=-x^2+o(x^2)$ : $k\sim-x^2$ (attention : on ne peut pas soustraire des équivalents).
4. (a) $f(x)=2x+o(x^2)$ ; $xf(x)=2x^2+o(x^3)$ ; $xf(x)=2x^2+6x^4+o(x^4)$. (b) $f(0)=0$, $f'(0)=2$, $f''(0)=0$, $f'''(0)=6\times3!=36$ (formule de Taylor-Young).

## Exercice 4 : développements limités (6 points)
Type : développements limités usuels et composés · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/8
Formules : $e^u = \sum \frac{u^k}{k!}$ ; $\cos u = 1 - \frac{u^2}2 + \frac{u^4}{24}$ ; $\sin u = u - \frac{u^3}6$ ; $\ln(1+u) = u - \frac{u^2}2 + \frac{u^3}3 - \frac{u^4}4$ ; $\sqrt{1+u} = 1 + \frac u2 - \frac{u^2}8 + \frac{u^3}{16} - \frac{5u^4}{128}$ ; $(1+u)^\alpha = 1 + \alpha u + \frac{\alpha(\alpha-1)}2u^2$ ; produit tronqué ; composition : poser $u$, calculer $u^2$ à l'ordre voulu ; $1 + \cos 2x = 2\cos^2 x$

1. (a) $f(x)=\dfrac1{1+x^2}=1-x^2+x^4+o(x^4)$. (b) $g(x)=\left(x-\dfrac{x^3}6+o(x^4)\right)(1-x^2+x^4+o(x^4))=x-\dfrac76x^3+o(x^4)$.
2. (a) Premier terme : $\ln(1+\cos0)=\ln2$. (b) $\cos x=1-\dfrac{x^2}2+\dfrac{x^4}{24}+o(x^4)$, $\ln(1+u)=u-\dfrac{u^2}2+o(u^2)$. $1+\cos x=2\left(1-\dfrac{x^2}4+\dfrac{x^4}{48}+o(x^4)\right)$ donc $h(x)=\ln2+u-\dfrac{u^2}2$ avec $u=-\dfrac{x^2}4+\dfrac{x^4}{48}$ : $h(x)=\ln2-\dfrac{x^2}4+\dfrac{x^4}{48}-\dfrac{x^4}{32}+o(x^4)=\ln2-\dfrac{x^2}4-\dfrac{x^4}{96}+o(x^4)$.

## Exercice 5 : calcul de limites (4 points)
Type : développements limités, limite par équivalents · ECUE : APEF (fonctions) · Niveau : maths-s2-apef-fonctions/9
Formules : en 0 : $e^x = 1 + x + \frac{x^2}2 + \frac{x^3}6 + o(x^3)$ ; $\ln(1+x) = x - \frac{x^2}2 + o(x^2)$ ; $\cos x = 1 - \frac{x^2}2 + o(x^3)$ ; $\sin x = x - \frac{x^3}6 + o(x^3)$ ; $\frac1{1-x} = 1 + x + x^2 + x^3 + o(x^3)$ ; produit de DL tronqué à l'ordre ; $a^b = e^{b\ln a}$ ; $f \sim g \Rightarrow$ même limite

1. Numérateur : $e^{2x}-2\sin x-1=(1+2x+2x^2)-2x-1+o(x^2)=2x^2+o(x^2)$. Dénominateur : $1-\sqrt{1-x}=\dfrac x2+o(x)$. Donc le quotient est équivalent à $\dfrac{2x^2}{x/2}=4x$ et la limite vaut $0$.
2. $\left(\cos\dfrac1x\right)^{x^2}=\exp\!\big(x^2\ln\cos\tfrac1x\big)$. Avec $t=\dfrac1x\to0$ : $\ln\cos t=-\dfrac{t^2}2+o(t^2)$, donc $x^2\ln\cos\tfrac1x\to-\dfrac12$ et la limite vaut $e^{-1/2}$.
