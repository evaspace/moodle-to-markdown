---
id: APIS-3.7
syllabus: APIS
type: méthode
papier: 
prereq: APIS-3.6
alias: méthode des rectangles, somme de Riemann, encadrer une intégrale, approximation, subdivision
---
# Méthode des rectangles

On découpe $[a, b]$ en $n$ intervalles de longueur $\frac{b-a}{n}$ et on approche l'aire par des rectangles :
$$\frac{b-a}{n}\sum_{k=0}^{n-1} f\!\left(a + k\tfrac{b-a}{n}\right) \xrightarrow[n \to +\infty]{} \int_a^b f(x)\,dx$$
Si $f$ est croissante, les rectangles « à gauche » minorent l'intégrale et ceux « à droite » la majorent (exemple : encadrer $\int_0^1 x^2\,dx$).

Source : Poly « S1 Cours Primitives Intégrales » et TD3 (Moodle S1-MATHS-2031, Cours 3).
