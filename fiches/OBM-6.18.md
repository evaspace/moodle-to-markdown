---
id: OBM-6.18
syllabus: OBM
type: théorème
papier: maths-s1-obm/10
prereq: OBM-6.15, OBM-6.16
alias: composée d'injections, composée de surjections, g∘f injective, g∘f surjective, composée de bijections, (g∘f)^(-1)
---
# Composée d'injections, de surjections

> **À retenir.** $f:E\to F$, $g:F\to G$. Si $f$ et $g$ sont injectives, $g\circ f$ l'est ; si elles sont surjectives, $g\circ f$ l'est ; si elles sont bijectives, $g\circ f$ l'est et $(g\circ f)^{-1}=f^{-1}\circ g^{-1}$ (ordre inversé). Réciproquement : $g\circ f$ injective $\Rightarrow f$ injective ; $g\circ f$ surjective $\Rightarrow g$ surjective.

## Méthode en copie
- Composée injective : « Soient $x,x'\in E$ tels que $g(f(x))=g(f(x'))$. $g$ injective donne $f(x)=f(x')$, puis $f$ injective donne $x=x'$. »
- Composée surjective : « Soit $z\in G$. $g$ surjective : $\exists y\in F$, $g(y)=z$. $f$ surjective : $\exists x\in E$, $f(x)=y$. Alors $g(f(x))=z$. »

## Corrigé du cours
Montrer : $g\circ f$ injective $\Rightarrow f$ injective. Soient $x,x'\in E$ tels que $f(x)=f(x')$. Alors $g(f(x))=g(f(x'))$, et $g\circ f$ injective donne $x=x'$. Donc $f$ est injective.

## Pièges
- $(g\circ f)^{-1}=g^{-1}\circ f^{-1}$ : faux, l'ordre s'inverse.
- Croire que $g\circ f$ injective rend $g$ injective : faux en général.

## Teste-toi
1. Si $g\circ f$ est surjective, laquelle de $f$ ou $g$ est forcément surjective ?

## Réponses
1. $g$ : tout $z\in G$ s'écrit $g(f(x))$, donc a l'antécédent $f(x)$ par $g$.

Source : Cours 6 « Compléments séminaire » (fiches de synthèse, exercices types et corrigés), Moodle S1-MATHS-2031 ; types d'exercices des annales OBM.
