# Contrôle de cours ECUE FCT, mathématiques S1PA — lundi 20 novembre 2023 (corrigé rédigé, FR)

- Source : corrigé rédigé pour cette application (pas de corrigé officiel). Sujet : `td1-2028-s1-maths_PA-subject-fr.md` (même dossier). Calculs vérifiés avec sympy. 

## Cours 1 : fonctions trigonométriques (8 points)
Type : cercle trigonométrique, valeurs remarquables, fonction tangente · ECUE : APEF (fonctions)
Formules : $\cos(\pi - x) = -\cos x$ ; $\cos(\frac\pi2 + x) = -\sin x$ ; $\sin(\frac\pi2 - x) = \cos x$ ; table $0, \frac\pi6, \frac\pi4, \frac\pi3, \frac\pi2$ : $\cos = 1, \frac{\sqrt3}2, \frac{\sqrt2}2, \frac12, 0$ ; réduire modulo $2\pi$ ; $\tan = \frac{\sin}{\cos}$ sur $\mathbb{R} \setminus \{\frac\pi2 + k\pi\}$ ; $\tan' = \frac1{\cos^2} = 1 + \tan^2$ ; $(\frac uv)' = \frac{u'v - uv'}{v^2}$

1. (a) Sur le cercle trigonométrique, le point $M$ d'angle $x$ a pour abscisse $\cos x$ (projection sur l'axe horizontal) et pour ordonnée $\sin x$ (projection sur l'axe vertical).
   (b) $\cos(\pi-x)=-\cos x$, $\cos\left(\frac\pi2+x\right)=-\sin x$, $\sin\left(\frac\pi2-x\right)=\cos x$.
   (c) | $x$ | $0$ | $\frac\pi6$ | $\frac\pi4$ | $\frac\pi3$ | $\frac\pi2$ |
       |---|---|---|---|---|---|
       | $\cos x$ | $1$ | $\frac{\sqrt3}2$ | $\frac{\sqrt2}2$ | $\frac12$ | $0$ |
       | $\sin x$ | $0$ | $\frac12$ | $\frac{\sqrt2}2$ | $\frac{\sqrt3}2$ | $1$ |
   (d) $\cos\frac{7\pi}6=-\frac{\sqrt3}2$ ; $\sin\frac{5\pi}4=-\frac{\sqrt2}2$ ; $\sin7\pi=0$ ; $\cos\frac{17\pi}3=\cos\left(\frac{17\pi}3-6\pi\right)=\cos\left(-\frac\pi3\right)=\frac12$.
2. (a) $I=\mathbb R\setminus\left\{\frac\pi2+k\pi,\ k\in\mathbb Z\right\}$ et $\tan x=\dfrac{\sin x}{\cos x}$.
   (b) Quotient avec $u=\sin$, $u'=\cos$, $v=\cos$, $v'=-\sin$ : $f'=\dfrac{\cos^2x+\sin^2x}{\cos^2x}=\dfrac1{\cos^2x}=1+\tan^2x$.

## Cours 2 : dérivées de fonctions composées (2 points)
Type : dériver une composée · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/1
Formules : $(g \circ u)' = u' \times g' \circ u$ ; $(e^u)' = u'e^u$ ; $(\sqrt u)' = \frac{u'}{2\sqrt u}$ ; $(u^n)' = nu'u^{n-1}$ ; $(\ln u)' = \frac{u'}u$

1. $f'(x)=\dfrac x{\sqrt{x^2+1}}\,e^{\sqrt{x^2+1}}$ (avec $(\sqrt u)'=\frac{u'}{2\sqrt u}$, $u=x^2+1$).
2. $g'(x)=2x\big(1+\tan^2(x^2)\big)=\dfrac{2x}{\cos^2(x^2)}$.

## Cours 3 : la fonction $x \mapsto \ln(x)$ (10 points)
Type : fonction logarithme (propriétés, équations, limites, composées) · ECUE : APEF (fonctions)
Formules : $e^{\ln x} = x$ ($x > 0$), $\ln(e^x) = x$ ; $\ln 1 = 0$, $\ln e = 1$ ; $\ln(ab) = \ln a + \ln b$, $\ln\frac1a = -\ln a$, $\ln\frac ab = \ln a - \ln b$, $n\ln a = \ln(a^n)$ ; $\ln$ croissante : $\ln X < 1 \iff 0 < X < e$ ; $\frac{\ln x}x \to 0$, $x\ln x \to 0$ en $0^+$ ; $(\ln u)' = \frac{u'}u$, $(\sqrt u)' = \frac{u'}{2\sqrt u}$

1. La courbe de $\ln$ est définie sur $]0,+\infty[$, croissante, passe par $(1,0)$ et $(e,1)$, avec l'axe des ordonnées comme asymptote verticale ($\ln x\to-\infty$ en $0^+$).
2. a) $\forall x>0,\ e^{\ln x}=x$. b) $\forall x\in\mathbb R,\ \ln(e^x)=x$. c) $\ln e=1$. d) $\ln1=0$. e) $\ln0$ n'existe pas. f) Pas de formule en général ($\ln(a+b)\ne\ln a+\ln b$). g) $\ln(ab)=\ln a+\ln b$. i) $\ln\frac1a=-\ln a$. j) $\ln\frac ab=\ln a-\ln b$. k) $n\ln a=\ln(a^n)$.
3. (a) $e^{-2\ln2}=\dfrac14$, $\ln(9e^2)=2\ln3+2$, $4\ln27=12\ln3$ : $A=\dfrac14+2\ln3+2-12\ln3=\dfrac94-10\ln3$.
   (b) $\ln(1-x)<1\iff0<1-x<e\iff1-e<x<1$ : $S=]1-e,1[$.
4. a) $0$. b) $+\infty$. c) $-\infty$. d) $0$.
5. (a) $f\circ g(x)=\ln\sqrt x=\dfrac12\ln x$, $D_1=]0,+\infty[$, dérivée $\dfrac1{2x}$.
   (b) $g\circ f(x)=\sqrt{\ln x}$, $D_2=[1,+\infty[$, dérivée sur $]1,+\infty[$ : $\dfrac1{2x\sqrt{\ln x}}$.
