# Contrôle de cours ECUE FCT, mathématiques S1PA — lundi 20 novembre 2023 (sujet, FR)

- Source : `raw/S1/TDs/2028/td1-2028-s1-maths_PA-subject-fr.pdf` (scan d'une copie remplie et notée, 3 pages ; seuls les énoncés sont repris)
- Date réelle : 20 novembre 2023 (parcours PA, dossier promo 2028). Corrigé rédigé : `td1-2028-s1-maths_PA-correction-fr.md` (même dossier).
- Durée : 1 heure. Barème sur 20.

## Cours 1 : fonctions trigonométriques (8 points)
Type : cercle trigonométrique, valeurs remarquables, fonction tangente · ECUE : APEF (fonctions)
Formules : $\cos(\pi - x) = -\cos x$ ; $\cos(\frac\pi2 + x) = -\sin x$ ; $\sin(\frac\pi2 - x) = \cos x$ ; table $0, \frac\pi6, \frac\pi4, \frac\pi3, \frac\pi2$ : $\cos = 1, \frac{\sqrt3}2, \frac{\sqrt2}2, \frac12, 0$ ; réduire modulo $2\pi$ ; $\tan = \frac{\sin}{\cos}$ sur $\mathbb{R} \setminus \{\frac\pi2 + k\pi\}$ ; $\tan' = \frac1{\cos^2} = 1 + \tan^2$ ; $(\frac uv)' = \frac{u'v - uv'}{v^2}$

1. Manipulation du cercle trigonométrique (deux cercles fournis, point $M$ d'angle $x$).
   (a) Sur le dessin de gauche, indiquer graphiquement le cosinus et le sinus de $x$ (faire apparaître les traits de construction).
   (b) Placer les angles $\pi - x$, $\frac\pi2 + x$ et $\frac\pi2 - x$ sur le dessin de droite. Donner $\cos(\pi - x)$, $\cos\left(\frac\pi2 + x\right)$ et $\sin\left(\frac\pi2 - x\right)$ en fonction de $\cos(x)$ et $\sin(x)$.
   (c) Remplir le tableau de valeurs de $\cos(x)$ et $\sin(x)$ pour $x \in \left\{0, \frac\pi6, \frac\pi4, \frac\pi3, \frac\pi2\right\}$.
   (d) Calculer $\cos\left(\frac{7\pi}6\right)$, $\sin\left(\frac{5\pi}4\right)$, $\sin(7\pi)$ et $\cos\left(\frac{17\pi}3\right)$.
2. La fonction tangente.
   (a) Rappeler le domaine de définition $I$ de $f : x \mapsto \tan(x)$ ainsi que son expression en fonction de $\cos(x)$ et $\sin(x)$.
   (b) Calculer la dérivée de $f$ sur $I$. En trouver deux écritures distinctes. Vous détaillerez vos calculs en mettant en évidence les dérivées des fonctions mises en jeu.

## Cours 2 : dérivées de fonctions composées (2 points)
Type : dériver une composée · ECUE : APIS (intégrales) · Niveau : maths-s1-apis-integrales/1
Formules : $(g \circ u)' = u' \times g' \circ u$ ; $(e^u)' = u'e^u$ ; $(\sqrt u)' = \frac{u'}{2\sqrt u}$ ; $(u^n)' = nu'u^{n-1}$ ; $(\ln u)' = \frac{u'}u$

Sans se soucier du domaine de définition, trouver la dérivée de :
1. $f(x) = e^{\sqrt{x^2 + 1}}$ ;
2. $g(x) = \tan(x^2) + 1$.

## Cours 3 : la fonction $x \mapsto \ln(x)$ (10 points)
Type : fonction logarithme (propriétés, équations, limites, composées) · ECUE : APEF (fonctions)
Formules : $e^{\ln x} = x$ ($x > 0$), $\ln(e^x) = x$ ; $\ln 1 = 0$, $\ln e = 1$ ; $\ln(ab) = \ln a + \ln b$, $\ln\frac1a = -\ln a$, $\ln\frac ab = \ln a - \ln b$, $n\ln a = \ln(a^n)$ ; $\ln$ croissante : $\ln X < 1 \iff 0 < X < e$ ; $\frac{\ln x}x \to 0$, $x\ln x \to 0$ en $0^+$ ; $(\ln u)' = \frac{u'}u$, $(\sqrt u)' = \frac{u'}{2\sqrt u}$

1. Donner l'allure de sa courbe représentative.
2. Soient $a$ et $b$ deux réels strictement positifs et $n \in \mathbb{N}$. Remplacer les pointillés par une formule correcte quand cela est possible (une réponse du type « $y = y$ » est interdite) :
   a) $\forall x \in \dots$, $e^{\ln(x)} = \dots$ ; b) $\forall x \in \dots$, $\ln(e^x) = \dots$ ; c) $\ln(e) = \dots$ ; d) $\ln(1) = \dots$ ; e) $\ln(0) = \dots$ ; f) $\ln(a + b) = \dots$ ; g) $\ln(a \times b) = \dots$ ; i) $\ln\left(\frac1a\right) = \dots$ ; j) $\ln\left(\frac ab\right) = \dots$ ; k) $n\ln(a) = \dots$
3. (a) Exprimer en fonction de $\ln(3)$ : $A = e^{-2\ln(2)} + \ln(9e^2) - 4\ln(27)$.
   (b) Résoudre l'inéquation $\ln(1 - x) < 1$.
4. Donner la réponse aux limites suivantes : a) $\lim_{x \to +\infty} \frac{\ln(x)}x$ ; b) $\lim_{x \to +\infty} \ln(x)$ ; c) $\lim_{x \to 0^+} \ln(x)$ ; d) $\lim_{x \to 0^+} x\ln(x)$.
5. Soient $f : x \mapsto \ln(x)$ et $g : x \mapsto \sqrt x$.
   (a) Trouver l'expression de $f \circ g$ ainsi que son domaine de définition $D_1$ et sa dérivée.
   (b) Trouver l'expression de $g \circ f$ ainsi que son domaine de définition $D_2$ et sa dérivée.
