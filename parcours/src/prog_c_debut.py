"""Level path: S1 programming, start of C (compilation, printf, types, operators, conditions, loops, functions,
arrays, pointers, strings, malloc).

NOT CALIBRATED on the official course: the course lives on prepa.pages.epita.fr (GitLab login) and no PDF, TD or
past exam of the programming ECUE is on the server. The content follows the standard first weeks of a C course.
When the real material is available, recalibrate (order, vocabulary, tools such as `-Wall -Wextra`).

Every program of this file is compiled and run by `parcours/check_c.py` (gcc in a throwaway Alpine container):
`CHECKS` holds (full source, expected stdout) pairs. build.py itself cannot run C: run the checker after any change.
Output is compared with whitespace collapsed.
"""

SUBJECT = {
    "id": "prog-s1-c-debut",
    "ordre": 700,
    "matiere": "prog",
    "semestre": "S1",
    "ecue": "Programmation C (début)",
    "titre": "Début du C : printf, types, conditions, boucles, fonctions, tableaux, pointeurs",
    "chapitres_moodle": ["2030-S1 Programmation/00_Section 0"],
    "td": "Non calibré : cours officiel inaccessible (GitLab EPITA), programme standard d'un début de C",
    "examens": [],
}

CHECKS = []  # (full C source, expected stdout), replayed by parcours/check_c.py
INC = "#include <stdio.h>\n"
S = "Programme standard de début de C (non calibré sur le cours EPITA)"


def _full(code):
    return code if code.lstrip().startswith("#include") else INC + code


def _blk(s):
    return f"```c\n{s}\n```"


def _out(s):
    return f"```\n{s}\n```"


def _pr(code, out, sol, enonce):
    code = _full(code).strip()
    CHECKS.append((code + "\n", out))
    return {"enonce": f"{enonce}\n\n{_blk(code)}", "sol": f"**Affichage :**\n\n{_out(out)}\n\n{sol}"}


PR = "Qu'affiche ce programme ? (donner exactement la sortie)"


def pr(id, code, out, sol, enonce=PR, duree=2):
    """« What does it print? » exercise; the output is checked by check_c.py."""
    return {"id": id, "kind": "open", **_pr(code, out, sol, enonce), "src": S, "duree": duree}


def prv(code, out, sol, enonce=PR):
    """Variant of a pr() exercise, checked too."""
    return _pr(code, out, sol, enonce)


def w(id, enonce, fn, main, out, sol="", duree=6):
    """« Write the function » exercise: `fn` is the model code, `main` the test program shown to the student."""
    src = _full(fn).strip() + "\n\n" + main.strip() + "\n"
    CHECKS.append((src, out))
    return {"id": id, "kind": "open", "src": S, "duree": duree,
            "enonce": f"{enonce}\n\nCe `main` doit afficher :\n\n{_out(out)}\n\n{_blk(main.strip())}",
            "sol": f"{_blk(fn.strip())}\n\n{sol}"}


def v(id, enonce, calc, ans, sol, duree=2):
    return {"id": id, "kind": "value", "enonce": enonce, "calc": calc, "ans": ans, "sol": sol, "src": S, "duree": duree}


def o(id, enonce, sol, duree=4):
    return {"id": id, "kind": "open", "enonce": enonce, "sol": sol, "src": S, "duree": duree}


# ---------------------------------------------------------------- course

NOTIONS = [
    {"id": "compil", "titre": "Programme minimal, compilation, printf",
     "formule": r"`#include <stdio.h>` · `int main(void) { … return 0; }` · `gcc -Wall -Wextra -std=c99 -pedantic -o prog prog.c` · `printf(\"%d\", n)` · `%d` int · `%f` double · `%c` char · `%s` chaîne · `%zu` taille · `%%` · `\\n` retour à la ligne · `%5d`, `%-5d`, `%05d`, `%.2f`",
     "exemple": r"`printf(\"%d + %d = %d\\n\", 2, 3, 2 + 3);` affiche `2 + 3 = 5`",
     "cours": r"Un programme C est un ensemble de fonctions dont `main` est le point d'entrée : sa valeur de retour est le code de sortie (`0` = succès). `gcc` compile le fichier source en exécutable ; les options `-Wall -Wextra` demandent les avertissements, qu'il faut lire et corriger. `printf` affiche selon un format : chaque `%` consomme un argument du type indiqué. Un format qui ne correspond pas au type de l'argument est un bug (comportement indéfini)."},
    {"id": "types", "titre": "Types, variables, conversions",
     "formule": r"`char` (1 octet) · `int` (4) · `long` · `float` · `double` (8) · `unsigned` · déclaration `int x = 3;` · `sizeof(type)` en octets · cast `(double) a` · `int` $\to$ `double` automatique · `double` $\to$ `int` tronque",
     "exemple": r"`char c = 'a'; c = c + 2;` donne `'c'` (code $99$)",
     "cours": r"Une variable a un type, fixé à sa déclaration, qui détermine sa taille et ses opérations. Un `char` est un petit entier (code ASCII) : `'a' + 1` vaut `98`. Un entier non signé qui dépasse sa capacité revient à $0$ (modulo $2^{8k}$). Dans une expression mixte, l'entier est converti en flottant ; la conversion inverse tronque vers $0$. Une variable locale non initialisée contient n'importe quoi."},
    {"id": "operateurs", "titre": "Opérateurs et priorités",
     "formule": r"`/` entier : quotient tronqué vers $0$ · `%` reste (signe de l'opérande de gauche) · `+= -= *= /= %=` · `i++` (valeur puis +1) · `++i` (+1 puis valeur) · priorité : `* / %` avant `+ -` · cast avant `/` : `(double) a / b`",
     "exemple": r"`7 / 2` $=3$ ; `-7 / 2` $=-3$ ; `7 % 2` $=1$ ; `7 / 2.0` $=3{,}5$",
     "cours": r"La division de deux entiers est entière : `5 / 2` vaut `2`, même si le résultat est rangé dans un `double`. Pour une division réelle, un des deux opérandes doit être flottant, avant la division. `i++` rend l'ancienne valeur, `++i` la nouvelle. Ne jamais modifier deux fois la même variable dans une expression : le résultat n'est pas défini."},
    {"id": "conditions", "titre": "Conditions : if, switch, booléens",
     "formule": r"`if (c) … else …` · `==` comparaison, `=` affectation · vrai $\ne 0$, faux $=0$ · `!` `&&` `||` (paresseux) · `c ? a : b` · `switch (n) { case 1: … break; default: … }` · sans `break`, on continue dans le `case` suivant · `else` se rattache au `if` le plus proche",
     "exemple": r"`if (n = 0)` affecte $0$ à `n` puis est faux : bug classique, à la place de `if (n == 0)`",
     "cours": r"Il n'y a pas de type booléen en C classique : une comparaison vaut `1` (vrai) ou `0` (faux) et toute valeur non nulle est vraie. `&&` et `||` s'arrêtent dès que le résultat est connu : la suite n'est pas évaluée. Dans un `switch`, chaque `case` doit finir par `break`, sinon l'exécution « tombe » dans le suivant (parfois voulu, souvent un bug)."},
    {"id": "boucles", "titre": "Boucles : while, for, do-while",
     "formule": r"`while (c) { … }` · `for (init; cond; pas) { … }` $\equiv$ `init; while (cond) { …; pas; }` · `do { … } while (c);` (au moins un tour) · `break` sort de la boucle · `continue` passe au tour suivant · `for (int i = 0; i < n; i++)` : $n$ tours",
     "exemple": r"`for (int i = 1; i < 100; i *= 2)` fait $7$ tours ($i=1,2,4,\dots,64$)",
     "cours": r"`while` teste avant chaque tour, `do … while` après (donc un tour au moins). Le `for` regroupe initialisation, condition et pas. `break` quitte la boucle la plus interne, `continue` saute à l'itération suivante (en passant par le pas du `for`). Pour une boucle de $n$ tours, le motif `i` de $0$ à $n-1$ avec `i < n` évite les décalages de un."},
    {"id": "fonctions", "titre": "Fonctions : paramètres, retour, portée",
     "formule": r"`type nom(type p1, type p2) { … return v; }` · `void` : pas de valeur · prototype `int f(int);` avant l'appel · paramètres passés par valeur (copie) · variable locale : bloc `{ }` · `static` : garde sa valeur entre les appels · récursivité : cas d'arrêt",
     "exemple": r"`int f(int x) { x = x * 2; return x; }` ne modifie pas la variable de l'appelant",
     "cours": r"Une fonction reçoit une copie de ses arguments : modifier un paramètre ne change pas la variable de l'appelant. Une fonction doit être déclarée (définie ou prototypée) avant son premier appel. Une variable locale n'existe que dans son bloc et masque une variable de même nom d'un bloc extérieur. Une variable `static` locale est initialisée une seule fois et garde sa valeur d'un appel à l'autre."},
    {"id": "tableaux", "titre": "Tableaux et chaînes de caractères",
     "formule": r"`int t[5];` · indices de $0$ à $4$ · `int t[5] = {1, 2};` : le reste vaut $0$ · taille : `sizeof t / sizeof t[0]` · un tableau passé en paramètre n'est pas copié (adresse) : `void f(int t[], int n)` · chaîne = `char s[]` finissant par `'\\0'` · `strlen` (sans le `\\0`) · `sizeof` (avec)",
     "exemple": r"`char s[] = \"abc\";` : `sizeof s` $=4$, `strlen(s)` $=3$",
     "cours": r"Un tableau a une taille fixe et ses éléments sont contigus. C ne vérifie jamais les indices : `t[5]` sur un tableau de $5$ éléments est une erreur silencieuse (comportement indéfini). Un tableau passé à une fonction n'est pas copié et la fonction ne connaît pas sa taille : on la passe à part. Une chaîne est un tableau de `char` terminé par `'\\0'` ; `strlen`, `strcpy`, `strcat`, `strcmp` sont dans `<string.h>`."},
    {"id": "pointeurs", "titre": "Pointeurs",
     "formule": r"`int *p = &a;` · `&a` adresse de `a` · `*p` valeur pointée · `*p = 9;` modifie `a` · `p + 1` : élément suivant · `t[i]` $\equiv$ `*(t + i)` · tableau $\approx$ adresse de son premier élément · passage par adresse : `void f(int *n) { (*n)++; }` · appel `f(&x)`",
     "exemple": r"`void echange(int *a, int *b) { int t = *a; *a = *b; *b = t; }`",
     "cours": r"Un pointeur est une variable qui contient une adresse. `&` donne l'adresse d'une variable, `*` accède à ce qui est à une adresse. Passer l'adresse d'une variable à une fonction permet à celle-ci de la modifier (sinon elle ne reçoit qu'une copie). L'arithmétique de pointeurs avance d'un élément entier, pas d'un octet : `p + 1` pointe sur l'`int` suivant."},
    {"id": "memoire", "titre": "Mémoire dynamique, chaînes en détail",
     "formule": r"`#include <stdlib.h>` · `int *t = malloc(n * sizeof(int));` · tester `t != NULL` · `free(t);` · toujours un `free` par `malloc` · ne pas utiliser après `free` · `<string.h>` : `strlen`, `strcpy`, `strcat`, `strcmp` (`0` si égales) · le tampon doit contenir le `\\0`",
     "exemple": r"`malloc(10 * sizeof(double))` réserve $80$ octets",
     "cours": r"`malloc` réserve un bloc dont la taille est donnée en octets ; on écrit `n * sizeof(type)` pour ne pas dépendre de la machine. Le bloc reste réservé jusqu'à `free` : oublier le `free` est une fuite mémoire, l'appeler deux fois ou utiliser le bloc après est une erreur grave. `strcpy` et `strcat` ne vérifient pas la taille de destination : un tampon trop petit déborde sur la mémoire voisine."},
]

# ---------------------------------------------------------------- levels

LEVELS = [
    {"n": 1, "titre": "Premier programme et printf", "notions": ["compil"], "exos": [
        pr("c11", r'''int main(void)
{
    printf("Salut\n");
    printf("EPITA");
    return 0;
}''', "Salut\nEPITA", r"`\n` termine la première ligne ; le second `printf` n'ajoute pas de retour à la ligne.", duree=1),
        pr("c12", r'''int main(void)
{
    printf("%d + %d = %d\n", 2, 3, 2 + 3);
    return 0;
}''', "2 + 3 = 5", r"Chaque `%d` prend l'argument suivant : `2`, `3`, puis la valeur de `2 + 3`.", duree=1),
        pr("c13", r'''int main(void)
{
    printf("%c%c%c\n", 'E', 'P', 'A');
    printf("%s\n", "ok");
    return 0;
}''', "EPA\nok", r"`%c` affiche un caractère, `%s` une chaîne."),
        pr("c14", r'''int main(void)
{
    printf("%5d|%-5d|%05d\n", 42, 42, 42);
    return 0;
}''', "   42|42   |00042", r"`%5d` : largeur $5$, aligné à droite ; `%-5d` : aligné à gauche ; `%05d` : complété par des zéros."),
        pr("c15", r'''int main(void)
{
    printf("%.2f %d%%\n", 3.14159, 50);
    return 0;
}''', "3.14 50%", r"`%.2f` : deux chiffres après la virgule, arrondi ; `%%` affiche un `%`."),
        o("c16", r"Écrire la commande qui compile `prog.c` en un exécutable `prog` avec les avertissements `-Wall -Wextra`, en C99 strict, puis celle qui l'exécute.",
          "```\ngcc -Wall -Wextra -std=c99 -pedantic -o prog prog.c\n./prog\n```\n`-o prog` nomme l'exécutable (sinon `a.out`). `-Wall -Wextra` activent les avertissements, `-std=c99 -pedantic` imposent la norme."),
        v("c17", r"Combien de caractères le programme affiche-t-il avec `printf(\"EPITA\\n\");` ? (le retour à la ligne compte pour un)", "5 + 1", "6", r"$5$ lettres et un `\n`."),
    ]},
    {"n": 2, "titre": "Types et opérateurs", "notions": ["types", "operateurs"], "exos": [
        pr("c21", r'''int main(void)
{
    int a = 7, b = 2;
    printf("%d %d %d\n", a / b, a % b, -a / b);
    return 0;
}''', "3 1 -3", r"Division entière tronquée vers $0$ : $7/2=3$ et $-7/2=-3$ ; $7\bmod 2=1$."),
        pr("c22", r'''int main(void)
{
    double d = 7 / 2;
    printf("%.1f\n", d);
    d = 7 / 2.0;
    printf("%.1f\n", d);
    return 0;
}''', "3.0\n3.5", r"`7 / 2` est une division entière faite avant l'affectation : `3`, rangé comme `3.0`. Avec `2.0`, la division est réelle."),
        pr("c23", r'''int main(void)
{
    int i = 5;
    printf("%d\n", i++);
    printf("%d\n", i);
    printf("%d\n", ++i);
    return 0;
}''', "5\n6\n7", r"`i++` rend $5$ puis incrémente ; `++i` incrémente puis rend la nouvelle valeur."),
        pr("c24", r'''int main(void)
{
    int x = 10;
    x += 5;
    x *= 2;
    x -= 3;
    x /= 4;
    printf("%d\n", x);
    return 0;
}''', "6", r"$10\to15\to30\to27\to 27/4=6$ (division entière)."),
        pr("c25", r'''int main(void)
{
    char c = 'a';
    c = c + 2;
    printf("%c %d\n", c, c);
    return 0;
}''', "c 99", r"Un `char` est un entier : `'a'` vaut $97$, donc $99$ est le code de `'c'`."),
        pr("c26", r'''int main(void)
{
    int a = 5, b = 2;
    printf("%d %.2f %.2f\n", a / b, (double) a / b, (double) (a / b));
    return 0;
}''', "2 2.50 2.00", r"Le cast `(double) a` s'applique avant la division ; dans `(double) (a / b)`, la division entière a déjà donné $2$."),
        pr("c27", r'''int main(void)
{
    unsigned char c = 250;
    c += 10;
    printf("%d\n", c);
    return 0;
}''', "4", r"Un `unsigned char` va de $0$ à $255$ : $260 \bmod 256 = 4$."),
        v("c28", r"Valeur de l'expression C `1 + 2 * 3 % 4` ?", "1 + (2 * 3) % 4", "3", r"`*` et `%` ont la même priorité et s'évaluent de gauche à droite : $(2\times3)\bmod4=2$, puis $1+2=3$."),
    ]},
    {"n": 3, "titre": "Conditions", "notions": ["conditions"], "exos": [
        pr("c31", r'''int main(void)
{
    int n = 5;
    if (n = 0)
        printf("zero\n");
    else
        printf("non zero %d\n", n);
    return 0;
}''', "non zero 0", r"`n = 0` est une affectation : elle met `n` à $0$ et vaut $0$ (faux). C'est `==` qu'il fallait écrire ; `-Wall` le signale."),
        pr("c32", r'''int main(void)
{
    printf("%d %d %d\n", 3 > 2, 2 == 3, !5);
    return 0;
}''', "1 0 0", r"Une comparaison vaut `1` ou `0` ; `!5` est la négation d'une valeur non nulle."),
        pr("c33", r'''int main(void)
{
    int a = 1, b = 0;
    if (a || b++)
        printf("x");
    printf(" %d %d\n", a, b);
    return 0;
}''', "x 1 0", r"`a` est vrai : `||` n'évalue pas `b++`, donc `b` reste à $0$."),
        pr("c34", r'''int main(void)
{
    int n = 2;
    switch (n) {
    case 1:
        printf("un\n");
    case 2:
        printf("deux\n");
    case 3:
        printf("trois\n");
        break;
    default:
        printf("autre\n");
    }
    return 0;
}''', "deux\ntrois", r"Pas de `break` après `case 2` : l'exécution continue dans `case 3`, puis `break`."),
        pr("c35", r'''int main(void)
{
    int x = 5;
    if (x > 0)
        if (x > 10)
            printf("A");
        else
            printf("B");
    printf("\n");
    return 0;
}''', "B", r"Le `else` se rattache au `if` le plus proche (`x > 10`). Ici `x > 0` est vrai et `x > 10` faux : on affiche `B`."),
        w("c36", r"Écrire `int max3(int a, int b, int c)` qui renvoie le plus grand des trois entiers.", r'''int max3(int a, int b, int c)
{
    int m = a;
    if (b > m)
        m = b;
    if (c > m)
        m = c;
    return m;
}''', r'''int main(void)
{
    printf("%d %d %d\n", max3(1, 2, 3), max3(9, 4, 7), max3(-5, -2, -8));
    return 0;
}''', "3 9 -2", r"On garde le plus grand vu jusqu'ici dans `m`."),
    ]},
    {"n": 4, "titre": "Boucles", "notions": ["boucles"], "exos": [
        pr("c41", r'''int main(void)
{
    for (int i = 0; i < 5; i++)
        printf("%d ", i);
    printf("\n");
    return 0;
}''', "0 1 2 3 4", r"`i` va de $0$ à $4$ : cinq tours."),
        pr("c42", r'''int main(void)
{
    int s = 0;
    for (int i = 1; i <= 4; i++)
        s += i * i;
    printf("%d\n", s);
    return 0;
}''', "30", r"$1+4+9+16=30$."),
        pr("c43", r'''int main(void)
{
    int i = 10;
    while (i > 0)
        i -= 3;
    printf("%d\n", i);
    return 0;
}''', "-2", r"$10,7,4,1,-2$ : on sort quand `i` n'est plus strictement positif."),
        pr("c44", r'''int main(void)
{
    int n = 0;
    do {
        n++;
    } while (n < 0);
    printf("%d\n", n);
    return 0;
}''', "1", r"`do … while` fait toujours un tour avant de tester la condition."),
        pr("c45", r'''int main(void)
{
    for (int i = 0; i < 10; i++) {
        if (i % 2)
            continue;
        if (i > 6)
            break;
        printf("%d ", i);
    }
    printf("\n");
    return 0;
}''', "0 2 4 6", r"`continue` saute les impairs ; `break` s'exécute à `i = 8`."),
        pr("c46", r'''int main(void)
{
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j <= i; j++)
            printf("*");
        printf("\n");
    }
    return 0;
}''', "*\n**\n***", r"La ligne $i$ contient $i+1$ étoiles."),
        w("c47", r"Écrire `int puissance(int x, int n)` qui renvoie $x^n$ ($n\ge0$) avec une boucle.", r'''int puissance(int x, int n)
{
    int r = 1;
    for (int i = 0; i < n; i++)
        r *= x;
    return r;
}''', r'''int main(void)
{
    printf("%d %d %d\n", puissance(2, 10), puissance(5, 0), puissance(3, 4));
    return 0;
}''', "1024 1 81", r"$n=0$ : la boucle ne fait aucun tour et on renvoie $1$."),
        v("c48", r"Combien de tours fait `for (int i = 1; i < 100; i *= 2)` ?", "7", "7", r"$i=1,2,4,8,16,32,64$ ; $128$ n'est plus $<100$."),
    ]},
    {"n": 5, "titre": "Fonctions", "notions": ["fonctions"], "exos": [
        pr("c51", r'''int f(int x)
{
    x = x * 2;
    return x;
}

int main(void)
{
    int a = 3;
    int b = f(a);
    printf("%d %d\n", a, b);
    return 0;
}''', "3 6", r"`f` travaille sur une copie de `a` : `a` reste $3$."),
        pr("c52", r'''void affiche(int n)
{
    printf("[%d]", n);
}

int main(void)
{
    affiche(1);
    affiche(2);
    printf("\n");
    return 0;
}''', "[1][2]", r"Une fonction `void` ne renvoie rien, elle agit (ici elle affiche).", duree=1),
        pr("c53", r'''int fact(int n)
{
    return n <= 1 ? 1 : n * fact(n - 1);
}

int main(void)
{
    printf("%d\n", fact(5));
    return 0;
}''', "120", r"$5\times4\times3\times2\times1$ ; `fact(1)` est le cas d'arrêt."),
        pr("c54", r'''int cpt(void)
{
    static int c = 0;
    c++;
    return c;
}

int main(void)
{
    printf("%d ", cpt());
    printf("%d ", cpt());
    printf("%d\n", cpt());
    return 0;
}''', "1 2 3", r"`static` : `c` est initialisée une fois et garde sa valeur d'un appel à l'autre."),
        pr("c55", r'''int main(void)
{
    int x = 1;
    {
        int x = 2;
        printf("%d ", x);
    }
    printf("%d\n", x);
    return 0;
}''', "2 1", r"Le `x` du bloc interne masque l'autre jusqu'à la fin du bloc."),
        w("c56", r"Écrire `int est_premier(int n)` qui renvoie `1` si `n` est premier, `0` sinon.", r'''int est_premier(int n)
{
    if (n < 2)
        return 0;
    for (int d = 2; d * d <= n; d++)
        if (n % d == 0)
            return 0;
    return 1;
}''', r'''int main(void)
{
    printf("%d %d %d %d\n", est_premier(2), est_premier(15), est_premier(17), est_premier(1));
    return 0;
}''', "1 0 1 0", r"Il suffit de tester les diviseurs $d$ avec $d^2\le n$."),
        w("c57", r"Écrire `int pgcd(int a, int b)` (algorithme d'Euclide, récursif ou non).", r'''int pgcd(int a, int b)
{
    while (b != 0) {
        int r = a % b;
        a = b;
        b = r;
    }
    return a;
}''', r'''int main(void)
{
    printf("%d %d %d\n", pgcd(12, 18), pgcd(7, 13), pgcd(0, 5));
    return 0;
}''', "6 1 5", r"$\gcd(a,b)=\gcd(b,a\bmod b)$, jusqu'à $b=0$."),
    ]},
    {"n": 6, "titre": "Tableaux et chaînes", "notions": ["tableaux"], "exos": [
        pr("c61", r'''int main(void)
{
    int t[5] = {1, 2, 3};
    printf("%d %d %d\n", t[0], t[2], t[4]);
    return 0;
}''', "1 3 0", r"Les éléments non listés valent $0$ ; les indices vont de $0$ à $4$."),
        pr("c62", r'''int main(void)
{
    int t[] = {4, 8, 15, 16, 23, 42};
    printf("%zu\n", sizeof t / sizeof t[0]);
    return 0;
}''', "6", r"Taille totale divisée par la taille d'un élément : $24/4$."),
        pr("c63", r'''int main(void)
{
    int t[4] = {1, 2, 3, 4};
    for (int i = 0; i < 4 / 2; i++) {
        int tmp = t[i];
        t[i] = t[3 - i];
        t[3 - i] = tmp;
    }
    for (int i = 0; i < 4; i++)
        printf("%d ", t[i]);
    printf("\n");
    return 0;
}''', "4 3 2 1", r"On échange $t[0]\leftrightarrow t[3]$ puis $t[1]\leftrightarrow t[2]$ : le tableau est retourné."),
        pr("c64", r'''void incr(int t[], int n)
{
    for (int i = 0; i < n; i++)
        t[i]++;
}

int main(void)
{
    int a[3] = {1, 2, 3};
    incr(a, 3);
    printf("%d %d %d\n", a[0], a[1], a[2]);
    return 0;
}''', "2 3 4", r"Un tableau n'est pas copié : la fonction modifie le tableau de l'appelant."),
        pr("c65", r'''#include <stdio.h>
#include <string.h>

int main(void)
{
    char s[] = "abc";
    printf("%zu %zu\n", sizeof s, strlen(s));
    return 0;
}''', "4 3", r"`sizeof` compte le `'\0'` final ; `strlen` non."),
        pr("c66", r'''int main(void)
{
    char s[] = "EPITA";
    s[1] = '\0';
    printf("%s\n", s);
    return 0;
}''', "E", r"`printf(\"%s\")` s'arrête au premier `'\0'`."),
        w("c67", r"Écrire `int max_tab(int t[], int n)` qui renvoie le plus grand élément d'un tableau de $n\ge1$ entiers.", r'''int max_tab(int t[], int n)
{
    int m = t[0];
    for (int i = 1; i < n; i++)
        if (t[i] > m)
            m = t[i];
    return m;
}''', r'''int main(void)
{
    int a[] = {3, 9, 2};
    int b[] = {-4, -1, -7, -3};
    printf("%d %d\n", max_tab(a, 3), max_tab(b, 4));
    return 0;
}''', "9 -1", r"On part de `t[0]` (et non de $0$, sinon un tableau négatif donnerait $0$)."),
        w("c68", r"Écrire `int compte(char s[], char c)` : nombre d'occurrences de `c` dans la chaîne `s`.", r'''int compte(char s[], char c)
{
    int n = 0;
    for (int i = 0; s[i] != '\0'; i++)
        if (s[i] == c)
            n++;
    return n;
}''', r'''int main(void)
{
    char s[] = "banana";
    printf("%d %d %d\n", compte(s, 'a'), compte(s, 'n'), compte(s, 'z'));
    return 0;
}''', "3 2 0", r"Une chaîne se parcourt jusqu'au `'\0'`, sans connaître sa longueur."),
    ]},
    {"n": 7, "titre": "Pointeurs", "notions": ["pointeurs"], "exos": [
        pr("c71", r'''int main(void)
{
    int a = 5;
    int *p = &a;
    *p = 9;
    printf("%d\n", a);
    return 0;
}''', "9", r"`p` contient l'adresse de `a` : écrire dans `*p` modifie `a`.", duree=1),
        pr("c72", r'''void echange(int *a, int *b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

int main(void)
{
    int x = 1, y = 2;
    echange(&x, &y);
    printf("%d %d\n", x, y);
    return 0;
}''', "2 1", r"On passe les adresses pour que `echange` modifie `x` et `y`."),
        pr("c73", r'''int main(void)
{
    int t[3] = {10, 20, 30};
    int *p = t;
    p++;
    printf("%d %d\n", *p, *(p + 1));
    return 0;
}''', "20 30", r"`p` pointe d'abord sur `t[0]` ; `p++` avance d'un `int`."),
        pr("c74", r'''int main(void)
{
    int a = 1, b = 2;
    int *p = &a;
    int *q = p;
    *q += 10;
    q = &b;
    *q += 20;
    printf("%d %d\n", a, b);
    return 0;
}''', "11 22", r"`q` pointe d'abord sur `a` (comme `p`), puis sur `b`."),
        pr("c75", r'''void maj(int *n)
{
    (*n)++;
}

int main(void)
{
    int a = 0;
    maj(&a);
    maj(&a);
    printf("%d\n", a);
    return 0;
}''', "2", r"Les parenthèses sont nécessaires : `*n++` incrémenterait le pointeur."),
        pr("c76", r'''int main(void)
{
    int t[] = {5, 6, 7, 8};
    int *p = t + 1;
    printf("%d %d %ld\n", p[0], p[2], (long) (&t[3] - &t[0]));
    return 0;
}''', "6 8 3", r"`p[i]` est `*(p + i)` ; la différence de deux adresses se compte en éléments."),
        w("c77", r"Écrire `void min_max(int t[], int n, int *min, int *max)` qui range dans `*min` et `*max` le plus petit et le plus grand élément de $t$ ($n\ge1$).", r'''void min_max(int t[], int n, int *min, int *max)
{
    *min = t[0];
    *max = t[0];
    for (int i = 1; i < n; i++) {
        if (t[i] < *min)
            *min = t[i];
        if (t[i] > *max)
            *max = t[i];
    }
}''', r'''int main(void)
{
    int t[] = {4, -2, 9, 0};
    int lo, hi;
    min_max(t, 4, &lo, &hi);
    printf("%d %d\n", lo, hi);
    return 0;
}''', "-2 9", r"Une fonction ne renvoie qu'une valeur : pour en rendre deux, on lui passe deux adresses."),
    ]},
    {"n": 8, "titre": "Mémoire dynamique et chaînes", "notions": ["memoire", "tableaux"], "exos": [
        pr("c81", r'''#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *t = malloc(3 * sizeof(int));
    if (t == NULL)
        return 1;
    for (int i = 0; i < 3; i++)
        t[i] = i + 1;
    printf("%d\n", t[0] + t[1] + t[2]);
    free(t);
    return 0;
}''', "6", r"$1+2+3$. Le bloc réservé par `malloc` est libéré par `free`."),
        pr("c82", r'''int main(void)
{
    printf("%zu %zu %zu\n", sizeof(char), sizeof(int), sizeof(double));
    return 0;
}''', "1 4 8", r"Tailles usuelles sur une machine 64 bits (`int` : $4$ octets)."),
        pr("c83", r'''#include <stdio.h>
#include <string.h>

int main(void)
{
    char s[8];
    strcpy(s, "ab");
    strcat(s, "cd");
    printf("%s %zu\n", s, strlen(s));
    return 0;
}''', "abcd 4", r"`strcpy` copie `\"ab\"` (avec son `'\0'`), `strcat` ajoute `\"cd\"` ; le tampon de $8$ octets suffit pour $4+1$."),
        w("c84", r"Écrire `int longueur(const char *s)` sans `strlen`.", r'''int longueur(const char *s)
{
    int n = 0;
    while (s[n] != '\0')
        n++;
    return n;
}''', r'''int main(void)
{
    printf("%d %d\n", longueur("EPITA"), longueur(""));
    return 0;
}''', "5 0", r"On compte jusqu'au `'\0'` (non compté)."),
        w("c85", r"Écrire `void inverse(char *s)` qui retourne la chaîne `s` sur place (sans `strlen`, sans second tableau).", r'''void inverse(char *s)
{
    int n = 0;
    while (s[n] != '\0')
        n++;
    for (int i = 0; i < n / 2; i++) {
        char c = s[i];
        s[i] = s[n - 1 - i];
        s[n - 1 - i] = c;
    }
}''', r'''int main(void)
{
    char s[] = "EPITA";
    inverse(s);
    printf("%s\n", s);
    return 0;
}''', "ATIPE", r"On échange $s[i]$ et $s[n-1-i]$ pour $i<n/2$."),
        o("c86", r"Ce code est faux de deux façons. Lesquelles ?" + "\n\n" + _blk('''#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char s[5] = "EPITA";
    int *t = malloc(10 * sizeof(int));
    t[0] = 1;
    printf("%s %d\\n", s, t[0]);
    return 0;
}'''), r"1. `\"EPITA\"` occupe $6$ octets avec le `'\0'` : `char s[5]` est trop petit (la chaîne n'est pas terminée, `%s` lit au-delà : comportement indéfini). Il faut `char s[6]` ou `char s[] = \"EPITA\"`." + "\n2. Le bloc de `malloc` n'est jamais libéré (fuite mémoire) : il manque `free(t);` ; on devrait aussi tester `t != NULL` avant d'écrire dedans."),
        v("c87", r"Combien d'octets réserve `malloc(10 * sizeof(double))` (`double` : $8$ octets) ?", "10 * 8", "80", r"$10\times8$."),
    ]},
]

VARIANTS = {
    "c12": [prv('int main(void)\n{\n    printf("%d * %d = %d\\n", 4, 6, 4 * 6);\n    return 0;\n}', "4 * 6 = 24", r"Le troisième argument est la valeur de `4 * 6`.")],
    "c14": [prv('int main(void)\n{\n    printf("%4d|%-4d|%03d\\n", 7, 7, 7);\n    return 0;\n}', "   7|7   |007", r"Largeur $4$ à droite, à gauche, puis complétée par des zéros sur $3$ chiffres.")],
    "c15": [prv('int main(void)\n{\n    printf("%.1f %d%%\\n", 2.75, 20);\n    return 0;\n}', "2.8 20%", r"$2{,}75$ arrondi à un chiffre donne `2.8`.")],
    "c21": [prv('int main(void)\n{\n    int a = 17, b = 5;\n    printf("%d %d %d\\n", a / b, a % b, -a % b);\n    return 0;\n}', "3 2 -2", r"$17=5\times3+2$ ; `-17 % 5` a le signe de $-17$ : $-2$.")],
    "c22": [prv('int main(void)\n{\n    double d = 9 / 2;\n    printf("%.1f %.1f\\n", d, 9 / 2.0);\n    return 0;\n}', "4.0 4.5", r"Division entière d'abord : `9 / 2` vaut $4$.")],
    "c23": [prv('int main(void)\n{\n    int i = 1;\n    printf("%d\\n", ++i);\n    printf("%d\\n", i++);\n    printf("%d\\n", i);\n    return 0;\n}', "2\n2\n3", r"`++i` rend $2$ ; `i++` rend $2$ puis `i` vaut $3$.")],
    "c24": [prv('int main(void)\n{\n    int x = 3;\n    x *= 4;\n    x += 1;\n    x %= 5;\n    printf("%d\\n", x);\n    return 0;\n}', "3", r"$3\to12\to13\to13\bmod5=3$.")],
    "c25": [prv("int main(void)\n{\n    char c = 'A';\n    c += 3;\n    printf(\"%c %d\\n\", c, c);\n    return 0;\n}", "D 68", r"`'A'` vaut $65$ ; $65+3=68$, code de `'D'`.")],
    "c27": [prv('int main(void)\n{\n    unsigned char c = 200;\n    c += 100;\n    printf("%d\\n", c);\n    return 0;\n}', "44", r"$300\bmod256=44$.")],
    "c32": [prv('int main(void)\n{\n    printf("%d %d %d\\n", 1 < 2, 4 != 4, !0);\n    return 0;\n}', "1 0 1", r"`!0` vaut $1$.")],
    "c33": [prv('int main(void)\n{\n    int a = 0, b = 0;\n    if (a && b++)\n        printf("x");\n    printf(" %d %d\\n", a, b);\n    return 0;\n}', " 0 0", r"`a` est faux : `&&` n'évalue pas `b++`.")],
    "c42": [prv('int main(void)\n{\n    int s = 0;\n    for (int i = 1; i <= 5; i++)\n        s += i;\n    printf("%d\\n", s);\n    return 0;\n}', "15", r"$1+2+3+4+5$.")],
    "c43": [prv('int main(void)\n{\n    int i = 20;\n    while (i > 0)\n        i -= 6;\n    printf("%d\\n", i);\n    return 0;\n}', "-4", r"$20,14,8,2,-4$.")],
    "c48": [{"enonce": r"Combien de tours fait `for (int i = 1; i < 1000; i *= 3)` ?", "calc": "7", "ans": "7", "sol": r"$i=1,3,9,27,81,243,729$ ; $2187$ est trop grand."}],
    "c51": [prv('int f(int x)\n{\n    x = x + 10;\n    return x * 2;\n}\n\nint main(void)\n{\n    int a = 1;\n    printf("%d %d\\n", f(a), a);\n    return 0;\n}', "22 1", r"`f(1)` calcule $(1+10)\times2$ sur une copie ; `a` reste $1$.")],
    "c53": [prv('int fact(int n)\n{\n    return n <= 1 ? 1 : n * fact(n - 1);\n}\n\nint main(void)\n{\n    printf("%d\\n", fact(4));\n    return 0;\n}', "24", r"$4\times3\times2\times1$.")],
    "c61": [prv('int main(void)\n{\n    int t[4] = {7};\n    printf("%d %d\\n", t[0], t[3]);\n    return 0;\n}', "7 0", r"Seul `t[0]` est initialisé, le reste vaut $0$.")],
    "c64": [prv('void double_tab(int t[], int n)\n{\n    for (int i = 0; i < n; i++)\n        t[i] *= 2;\n}\n\nint main(void)\n{\n    int a[3] = {1, 2, 3};\n    double_tab(a, 3);\n    printf("%d %d %d\\n", a[0], a[1], a[2]);\n    return 0;\n}', "2 4 6", r"Le tableau de l'appelant est modifié.")],
    "c71": [prv('int main(void)\n{\n    int a = 3, b = 4;\n    int *p = &a;\n    *p = *p + b;\n    printf("%d %d\\n", a, b);\n    return 0;\n}', "7 4", r"`*p` est `a`.")],
    "c72": [prv('void echange(int *a, int *b)\n{\n    int t = *a;\n    *a = *b;\n    *b = t;\n}\n\nint main(void)\n{\n    int x = 5, y = 8;\n    echange(&x, &y);\n    echange(&x, &y);\n    printf("%d %d\\n", x, y);\n    return 0;\n}', "5 8", r"Deux échanges : retour à l'état initial.")],
    "c73": [prv('int main(void)\n{\n    int t[4] = {1, 2, 3, 4};\n    int *p = t + 2;\n    p--;\n    printf("%d %d\\n", *p, p[2]);\n    return 0;\n}', "2 4", r"`p` pointe sur `t[1]` ; `p[2]` est `t[3]`.")],
    "c82": [prv('int main(void)\n{\n    printf("%zu\\n", 10 * sizeof(int));\n    return 0;\n}', "40", r"$10\times4$.")],
    "c87": [{"enonce": r"Combien d'octets réserve `malloc(25 * sizeof(int))` (`int` : $4$ octets) ?", "calc": "100", "ans": "100", "sol": r"$25\times4$."}],
}
for _lvl in LEVELS:
    for _e in _lvl["exos"]:
        if _e["id"] in VARIANTS:
            _e["variants"] = VARIANTS[_e["id"]]

EXTRA_PARTS = []

QUIZ = [
    {"notion": "compil", "type": "qcm", "q": r"`printf(\"%d\", 2.5);` :", "choix": [r"est un bug : le format ne correspond pas au type", r"affiche `2`", r"affiche `2.5`", r"affiche `3`"], "bonne": 0},
    {"notion": "compil", "type": "vf", "q": r"La valeur renvoyée par `main` est le code de sortie du programme.", "bonne": True},
    {"notion": "types", "type": "qcm", "q": r"`'a' + 1` vaut :", "choix": [r"`98`", r"`'a1'`", r"`'b'` de type chaîne", r"une erreur de compilation"], "bonne": 0},
    {"notion": "types", "type": "vf", "q": r"Une variable locale non initialisée vaut toujours $0$.", "bonne": False},
    {"notion": "operateurs", "type": "qcm", "q": r"`double d = 5 / 2;` range dans `d` :", "choix": [r"`2.0`", r"`2.5`", r"`3.0`", r"une erreur"], "bonne": 0},
    {"notion": "operateurs", "type": "vf", "q": r"`i++` renvoie la valeur de `i` avant l'incrémentation.", "bonne": True},
    {"notion": "conditions", "type": "qcm", "q": r"`if (x = 3)` :", "choix": [r"affecte $3$ à `x` et est toujours vrai", r"compare `x` et $3$", r"est une erreur de syntaxe", r"est faux si `x` valait $3$"], "bonne": 0},
    {"notion": "conditions", "type": "vf", "q": r"Sans `break`, un `case` de `switch` continue dans le `case` suivant.", "bonne": True},
    {"notion": "boucles", "type": "qcm", "q": r"Une boucle `do … while` :", "choix": [r"fait au moins un tour", r"teste avant le premier tour", r"ne peut pas contenir de `break`", r"ne s'arrête jamais"], "bonne": 0},
    {"notion": "boucles", "type": "vf", "q": r"`continue` quitte complètement la boucle.", "bonne": False},
    {"notion": "fonctions", "type": "qcm", "q": r"Si `f(int x)` fait `x = 0;`, la variable passée par l'appelant :", "choix": [r"est inchangée", r"vaut $0$", r"est indéfinie", r"est libérée"], "bonne": 0},
    {"notion": "fonctions", "type": "vf", "q": r"Une variable `static` locale garde sa valeur entre deux appels.", "bonne": True},
    {"notion": "tableaux", "type": "qcm", "q": r"`char s[] = \"abc\";` : `sizeof s` vaut :", "choix": [r"`4`", r"`3`", r"`2`", r"`8`"], "bonne": 0},
    {"notion": "tableaux", "type": "vf", "q": r"C vérifie que l'indice d'un tableau est dans les bornes.", "bonne": False},
    {"notion": "pointeurs", "type": "qcm", "q": r"`int a; int *p = &a;` : `*p = 4;` :", "choix": [r"met `a` à $4$", r"met `p` à $4$", r"met l'adresse de `a` à $4$", r"est une erreur"], "bonne": 0},
    {"notion": "pointeurs", "type": "vf", "q": r"`t[i]` est équivalent à `*(t + i)`.", "bonne": True},
    {"notion": "memoire", "type": "qcm", "q": r"Chaque `malloc` doit être suivi, en fin d'utilisation, de :", "choix": [r"`free`", r"`delete`", r"`return`", r"`NULL`"], "bonne": 0},
    {"notion": "memoire", "type": "vf", "q": r"`strcpy` vérifie que le tampon de destination est assez grand.", "bonne": False},
]

_FL = {
    1: r"`gcc -Wall -Wextra -std=c99 -pedantic -o prog prog.c` · `%d %f %c %s %zu %%` · `%5d %-5d %05d %.2f`",
    2: r"`/` entier tronqué vers $0$ · `%` · `(double) a / b` · `i++` / `++i` · `+=` · `char` entier · `unsigned` modulo $2^{8k}$",
    3: r"`==` et `=` · vrai $\ne0$ · `&&` `||` paresseux · `switch` sans `break` · `else` au `if` le plus proche",
    4: r"`for (init; cond; pas)` · `while` · `do … while` · `break` · `continue` · $n$ tours : `i < n`",
    5: r"passage par valeur · `static` · portée de bloc · prototype · récursivité : cas d'arrêt",
    6: r"indices $0\dots n-1$ · `sizeof t / sizeof t[0]` · tableau non copié · chaîne finie par `'\\0'` · `strlen` / `sizeof`",
    7: r"`&a` · `*p` · `p + 1` · `t[i]` $\equiv$ `*(t + i)` · passage par adresse `f(&x)` · `(*n)++`",
    8: r"`malloc(n * sizeof(type))` · `free` · `strlen` `strcpy` `strcat` · `'\\0'` dans le tampon · `sizeof`",
}
FORMULES = {e["id"]: _FL[lvl["n"]] for lvl in LEVELS for e in lvl["exos"]}
