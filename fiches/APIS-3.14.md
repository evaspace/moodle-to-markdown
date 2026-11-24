---
id: APIS-3.14
syllabus: APIS
type: théorème
papier: maths-s1-apis-integrales/10
prereq: APIS-3.8, APIS-3.5
alias: changement de variable, substitution, poser t =, du = u'(x) dx, changer les bornes, changement de variable affine, changement de variable racine, changement de variable ln, tan
---
# Changement de variable

Si $\varphi$ est $C^1$ sur $[\alpha, \beta]$ et $f$ continue sur $\varphi([\alpha, \beta])$ :
$$\int_{\alpha}^{\beta} f(\varphi(t))\,\varphi'(t)\,dt = \int_{\varphi(\alpha)}^{\varphi(\beta)} f(x)\,dx$$
Méthode : poser $x = \varphi(t)$ (ou $t = \dots$), remplacer $dx = \varphi'(t)\,dt$, **changer les bornes**, puis calculer. Exemples : $t = \sqrt{x}$, $t = e^x$, $t = \ln x$, $t = ax + b$.

Source : Poly « S1 Cours Primitives Intégrales » et TD3 (Moodle S1-MATHS-2031, Cours 3).
