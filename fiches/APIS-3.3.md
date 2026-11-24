---
id: APIS-3.3
syllabus: APIS
type: théorème
papier: maths-s1-apis-integrales/4
prereq: APIS-3.2, APIS-3.5
alias: primitive de fonction composée, u'u^n, u' u puissance alpha, u'/u, ln|u|, u'e^u, u'/√u, 2√u, u'/u², u' cos u, u'/(1+u²), arctan u, reconnaître une dérivée
---
# Primitives de fonctions composées

$u$ dérivable sur $I$ (et $u > 0$ ou $u \neq 0$ quand il le faut) :

| $f$ | primitive |
|---|---|
| $u' u^\alpha$, $\alpha \neq -1$ | $\frac{u^{\alpha+1}}{\alpha+1}$ |
| $\frac{u'}{u}$ | $\ln\lvert u\rvert$ |
| $\frac{u'}{u^n}$, $n \geqslant 2$ | $-\frac{1}{(n-1)u^{n-1}}$ |
| $\frac{u'}{\sqrt{u}}$ | $2\sqrt{u}$ |
| $u' e^u$ | $e^u$ |
| $u' \cos u$ | $\sin u$ |
| $u' \sin u$ | $-\cos u$ |
| $\frac{u'}{1+u^2}$ | $\arctan u$ |

Méthode : repérer $u$, vérifier que $u'$ est là (à une constante multiplicative près), ajuster le coefficient.

Source : Poly « S1 Cours Primitives Intégrales » et TD3 (Moodle S1-MATHS-2031, Cours 3).
