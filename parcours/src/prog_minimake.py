"""Level path: C advanced up to Minimake, the last C project of the EPITA prépa first year (Forge MINIMAKE-2030,
after PROG-102 C basics, PROG-103 and PROG-104 lists/processes).

Source: the Minimake 1.0.1 subject and the Pepexator notes (/opt/pierref/pepexator/documentation/pepex-subject.md,
nook-doc.md), which are the same material as pepexator.pierref.eu. Levels follow the order of the subject: data
structures, Makefile, strings, getline, lists, parsing, variables, options, processes, buffering, dependencies, stat.
No exercise gives a Minimake solution: each one trains one brick (rule of the Pepexator site: no solutions).

Every program is compiled and run by `parcours/check_c.py` (gcc in a throwaway Alpine container, stdout redirected
to a file, so stdio is fully buffered as in the moulinette): `CHECKS` holds (full source, expected output) pairs.
"""

SUBJECT = {
    "id": "prog-s2-c-minimake",
    "ordre": 710,
    "matiere": "prog",
    "semestre": "S2",
    "ecue": "C avancé (Minimake)",
    "titre": "C avancé jusqu'à Minimake : structs, getline, listes, parsing, fork, exec, stat",
    "chapitres_moodle": [],
    "td": "Sujet Minimake 1.0.1 (Forge EPITA) et fiches Pepexator : https://pepexator.pierref.eu",
    "examens": [],
}

CHECKS = []  # (full C source, expected output), replayed by parcours/check_c.py
# Hidden prelude of the checked source only. getline, fork, strdup... are POSIX: hidden by `-std=c99` without the
# macro. musl flushes the first stdout line even into a file; glibc (the moulinette) buffers it fully: emulate glibc.
POSIX = ("#define _POSIX_C_SOURCE 200809L\n#include <stdio.h>\n"
         "__attribute__((constructor)) static void glibc_like(void) { setvbuf(stdout, NULL, _IOFBF, BUFSIZ); }\n")
INC = "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n"
S = "Sujet Minimake 1.0.1 (Forge EPITA) et fiches Pepexator"
PEPEX = "https://pepexator.pierref.eu/?node="


def _full(code):
    return code if code.lstrip().startswith("#include") else INC + code


def _blk(s):
    return f"```c\n{s}\n```"


def _out(s):
    return f"```\n{s}\n```"


PR = "Qu'affiche ce programme, sortie redirigée vers un fichier (`./prog > out`) ? (donner exactement la sortie)"


def pr(id, code, out, sol, enonce=PR, duree=3):
    """« What does it print? » exercise; the output is checked by check_c.py."""
    code = _full(code).strip()
    CHECKS.append((POSIX + code + "\n", out))
    return {"id": id, "kind": "open", "src": S, "duree": duree, "enonce": f"{enonce}\n\n{_blk(code)}",
            "sol": f"**Affichage :**\n\n{_out(out)}\n\n{sol}"}


def w(id, enonce, fn, main, out, sol="", duree=8):
    """« Write the function » exercise: `fn` is the model code, `main` the test program shown to the student."""
    fn = _full(fn).strip()
    CHECKS.append((POSIX + fn + "\n\n" + main.strip() + "\n", out))
    return {"id": id, "kind": "open", "src": S, "duree": duree,
            "enonce": f"{enonce}\n\nCe `main` doit afficher :\n\n{_out(out)}\n\n{_blk(main.strip())}",
            "sol": f"{_blk(fn)}\n\n{sol}"}


def v(id, enonce, calc, ans, sol, duree=2):
    return {"id": id, "kind": "value", "enonce": enonce, "calc": calc, "ans": ans, "sol": sol, "src": S, "duree": duree}


def o(id, enonce, sol, duree=4):
    return {"id": id, "kind": "open", "enonce": enonce, "sol": sol, "src": S, "duree": duree}


def _fiche(node, nom):
    return f"\n\nFiche Pepexator : [{nom}]({PEPEX}{node})"


# ---------------------------------------------------------------- course

NOTIONS = [
    {"id": "structs", "titre": "struct, enum, typedef",
     "formule": r"`struct rule { char *target; struct rule *next; };` · `typedef struct rule rule_t;` · `p->champ` $\equiv$ `(*p).champ` · `enum mode { HELP, PRINT, EXEC };` (valeurs $0, 1, 2$) · `sizeof(struct …)` $\ge$ somme des champs (alignement) · `calloc(1, sizeof(*r))` : tout à $0$",
     "exemple": r"`enum mode m = PRINT;` puis `switch (m) { case HELP: … }`",
     "cours": r"Une `struct` regroupe des champs ; on la manipule presque toujours par pointeur (`->`). Un `enum` donne des noms à des entiers : le sujet conseille un `enum` pour l'action choisie (aide, affichage `-p`, exécution). `calloc` met tout à zéro : les pointeurs valent `NULL`, ce qui évite les champs non initialisés. Le compilateur peut ajouter du remplissage entre les champs : la taille d'une `struct` n'est pas toujours la somme des tailles." + _fiche("c_struct", "STRUCTS")},
    {"id": "makefile", "titre": "Makefile et compilation du projet",
     "formule": r"`cible: dépendances` puis recette, chaque commande commence par une **tabulation** · `CC = gcc` · `CFLAGS = -Wall -Wextra -fsanitize=address -g` · `${VAR}` · `make` construit la première cible · cible à jour si plus récente que ses dépendances · `.gitignore` : `*.o`, binaire",
     "exemple": "```make\nCC = gcc\nCFLAGS = -Wall -Wextra -fsanitize=address -g\nminimake: main.o parse.o exec.o\n\t${CC} ${CFLAGS} -o minimake main.o parse.o exec.o\n```",
     "cours": r"Le sujet impose un `Makefile` à la racine de `minimake/` qui produit le binaire `minimake`, avec les options `-Wall -Wextra -fsanitize=address -g` (AddressSanitizer détecte débordements et fuites : le projet doit être sans fuite). Une ligne de recette commence par une tabulation, pas des espaces. `make` ne reconstruit que ce qui est plus ancien que ses dépendances." + _fiche("git_root", "GIT ET RENDU")},
    {"id": "chaines", "titre": "Chaînes : strchr, strcmp, isblank, strdup",
     "formule": r"`strchr(s, c)` : pointeur sur la 1re occurrence ou `NULL` · `strcmp(a, b)` : $0$ si égales · `strncmp(a, b, n)` · `isblank(c)` : espace ou `'\\t'` (`<ctype.h>`) · `strdup(s)` : copie allouée, à libérer · `strndup(s, n)` · couper : écrire `'\\0'`",
     "exemple": r"`char *sep = strchr(line, ':');` puis `*sep = '\\0';` : `line` devient la cible, `sep + 1` les dépendances",
     "cours": r"Minimake découpe chaque ligne : chercher un séparateur (`strchr`), poser un `'\\0'` pour terminer la première partie, puis enlever les blancs (`isblank`) au début et à la fin. `strcmp` renvoie $0$ quand les chaînes sont égales : `if (!strcmp(a, b))` signifie « égales ». Toute chaîne gardée après la lecture de la ligne doit être copiée (`strdup`), car `getline` réutilise son tampon." + _fiche("c_strchr", "STRCHR")},
    {"id": "getline", "titre": "Lire un fichier ligne par ligne : fopen, getline",
     "formule": r"`FILE *f = fopen(path, \"r\");` (`NULL` si échec) · `char *line = NULL; size_t n = 0; ssize_t len;` · `while ((len = getline(&line, &n, f)) != -1)` · la ligne garde son `'\\n'` · `free(line);` une fois à la fin · `fclose(f);`",
     "exemple": r"ligne `all: foo\\n` : `len` $=9$, `line[len - 1]` $=$ `'\\n'`",
     "cours": r"Le sujet interdit toute taille maximale de ligne : `getline` alloue et agrandit le tampon lui-même. On passe l'adresse du pointeur et de la taille ; le même tampon est réutilisé à chaque appel, donc on le libère une seule fois après la boucle (même si `getline` a échoué). La ligne contient le `'\\n'` final (sauf peut-être la dernière) : on le retire avant d'analyser. Si `-f` désigne un fichier impossible à ouvrir, Minimake affiche une erreur et renvoie $3$." + _fiche("c_getline", "GETLINE")},
    {"id": "listes", "titre": "Listes chaînées : ajout en fin, recherche, libération",
     "formule": r"ajout en fin : garder l'ordre du Makefile (`-p` affiche dans l'ordre de définition) · recherche par nom : parcourir jusqu'à `strcmp == 0` · libération : sauver `next` avant `free` · double pointeur `struct node **head` pour modifier la tête",
     "exemple": r"`for (struct var *v = vars; v; v = v->next) if (!strcmp(v->name, name)) return v;`",
     "cours": r"Le nombre de variables et de règles est inconnu : une liste chaînée convient. Les ajouts se font en fin de liste pour garder l'ordre du fichier. On cherche souvent par nom (variable, cible) : une fonction `find` qui renvoie le maillon ou `NULL`. Pour libérer, on lit `next` avant le `free`, sinon on lit de la mémoire libérée (ASan le signale)." + _fiche("concept_dlist", "LISTES")},
    {"id": "parsing", "titre": "Analyser une ligne de Makefile",
     "formule": r"1er de `':'` ou `'='` rencontré : `':'` $\Rightarrow$ règle, `'='` $\Rightarrow$ variable, aucun $\Rightarrow$ pas une définition · ligne commençant par `'\\t'` : commande de la règle courante · ligne `'\\t'` sans règle : erreur « command outside of rule » · blancs autour de `=` ignorés · valeur jusqu'à la fin de ligne",
     "exemple": r"`  FOO  =   foo   bar` : nom `FOO`, valeur `foo   bar`",
     "cours": r"Le sujet donne la méthode : parcourir la ligne caractère par caractère, le premier `:` ou `=` décide du type. On coupe alors en deux (nom/valeur ou cible/dépendances). Les lignes suivantes qui commencent par une tabulation sont les commandes de la règle ; les lignes vides et les commentaires peuvent s'y glisser ; la recette s'arrête à la première autre ligne. Une cible vide (après expansion) est ignorée." + _fiche("concept_parsing", "PARSING")},
    {"id": "variables", "titre": "Variables et expansion ${VAR}",
     "formule": r"`${VAR}` remplacé par la valeur · variable inconnue $\to$ chaîne vide (pas une erreur) · expansion **au parsing** pour cible, dépendances, nom et valeur de variable · expansion **à l'exécution** pour les commandes · remplacement même entre `'…'` · `${` sans `}` : erreur",
     "exemple": r"`OBJ=${SRC}.o` avant `SRC = main.c` : `OBJ` vaut `.o`",
     "cours": r"L'ordre compte : pendant le parsing, seules les variables déjà lues sont connues. `all: ${FILE}` avant `FILE=foo` donne une règle sans dépendance. Dans une commande, l'expansion a lieu à l'exécution, quand tout le fichier est lu. L'expansion se fait sur une nouvelle chaîne allouée, car la valeur peut être plus longue que `${NOM}`." + _fiche("concept_parsing", "PARSING")},
    {"id": "options", "titre": "Ligne de commande : argc, argv, -f -h -p",
     "formule": r"`int main(int argc, char *argv[])` · `argv[0]` nom du programme · options n'importe où : `./minimake all -f file` · `-f fichier` : le dernier gagne ; sans fichier $\to$ erreur, code $2$ ; fichier absent $\to$ code $3$ · `-h` prioritaire sur tout, code $0$ · `-p` : afficher sans exécuter · autres mots : cibles, dans l'ordre",
     "exemple": r"`./minimake -f -h` ouvre le fichier nommé `-h` (ce n'est pas l'aide)",
     "cours": r"On parcourt tout `argv` une fois et on remplit une structure d'options (fichier, mode, liste des cibles) avant de faire quoi que ce soit : `-h` doit gagner même s'il est le dernier argument. Le mot qui suit `-f` est toujours un nom de fichier, même s'il commence par `-`. Sans cible, on construit la première règle du fichier." + _fiche("root", "ROADMAP")},
    {"id": "processus", "titre": "fork, exec, waitpid : lancer une commande",
     "formule": r"`pid_t pid = fork();` : $0$ dans le fils, pid du fils dans le père, $-1$ si échec · `execl(\"/bin/sh\", \"sh\", \"-c\", cmd, (char *) NULL);` (ne revient qu'en cas d'échec) · `waitpid(pid, &st, 0);` · `WIFEXITED(st)` · `WEXITSTATUS(st)` · commande introuvable : $127$",
     "exemple": r"`false` $\to$ statut $1$ ; `notACommand` $\to$ $127$",
     "cours": r"Chaque commande de recette s'exécute dans un processus séparé avec `/bin/sh -c` (imposé par le sujet). `fork` duplique le processus ; le fils remplace son programme par `sh` avec `exec` ; le père attend le fils avec `waitpid` et lit son code de sortie. Si `exec` échoue, le fils doit appeler `_exit` (sinon deux copies de Minimake continuent). Au premier code non nul, la règle s'arrête : `minimake: *** [cible] Error N`." + _fiche("c_fork", "FORK")},
    {"id": "tampons", "titre": "Tampons de sortie : fflush",
     "formule": r"`printf` met en tampon · terminal : vidé à chaque `'\\n'` · fichier ou tube : vidé quand plein ou à la sortie · `fork` copie le tampon non vidé (affichage en double) · `exec` jette le tampon du fils · `fflush(stdout); fflush(stderr);` avant `fork`",
     "exemple": r"`printf(\"echo hi\\n\"); fork(); …` redirigé dans un fichier : `echo hi` peut apparaître deux fois ou après `hi`",
     "cours": r"Minimake affiche chaque commande avant de l'exécuter. La moulinette lit la sortie dans un fichier, donc `stdout` n'est pas vidé à chaque ligne : sans `fflush` avant le `fork`, la ligne reste dans le tampon, est copiée dans le fils, et sort dans le désordre ou en double. Le sujet le dit : appeler `fflush` sur `stdout` et `stderr` avant de lancer le processus." + _fiche("c_fflush", "FFLUSH")},
    {"id": "dependances", "titre": "Dépendances, cibles et messages d'erreur",
     "formule": r"construire une règle : d'abord chaque dépendance (récursif), puis ses commandes · dépendance sans règle : `minimake: *** No rule to make target 'D', needed by 'R'.  Stop.` · cible demandée absente : `minimake: *** No rule to make target 'T'.  Stop.` · fichier vide : `minimake: *** No targets.  Stop.` · erreur $\Rightarrow$ code $2$, sinon $0$ · messages sur la sortie standard",
     "exemple": r"`./minimake all check` construit `all` puis `check`",
     "cours": r"Construire une règle, c'est construire d'abord ses dépendances dans l'ordre (appel récursif), puis exécuter sa recette. Une dépendance sans règle ou une commande en échec arrête cette règle. Les cibles de la ligne de commande sont construites dans l'ordre donné ; un échec sur l'une n'empêche pas de tenter les suivantes. Les messages sont exacts au caractère près (deux espaces avant `Stop.`)." + _fiche("concept_execution", "EXÉCUTION")},
    {"id": "stat", "titre": "Cibles à jour : stat et dates",
     "formule": r"`struct stat sb;` · `stat(path, &sb)` : $0$ si le fichier existe, $-1$ sinon · `sb.st_mtim.tv_sec` (ou `sb.st_mtime`) : date de dernière modification · à jour si le fichier cible existe, chaque dépendance-fichier est plus ancienne et chaque dépendance est à jour · message `minimake: 'cible' is up to date.`",
     "exemple": r"`file.c` puis `file.o` créés : `file.o` est à jour",
     "cours": r"C'est la partie bonus : ne pas reconstruire une cible plus récente que ses dépendances. `stat` remplit une `struct stat` ; son échec signifie en général que le fichier n'existe pas. On compare les dates de modification : si une dépendance est plus récente que la cible, il faut reconstruire." + _fiche("c_stat", "STAT")},
]

# ---------------------------------------------------------------- levels

LEVELS = [
    {"n": 1, "titre": "struct, enum, typedef", "notions": ["structs"], "exos": [
        pr("m11", r'''struct rule
{
    char *target;
    int nb_deps;
};

int main(void)
{
    struct rule r = { "all", 2 };
    struct rule *p = &r;
    p->nb_deps++;
    printf("%s %d %d\n", r.target, r.nb_deps, (*p).nb_deps);
    return 0;
}''', "all 3 3", r"`p->nb_deps` et `(*p).nb_deps` désignent le champ de `r` : l'incrément le modifie."),
        pr("m12", r'''enum mode { HELP, PRINT, EXEC = 5, OTHER };

int main(void)
{
    printf("%d %d %d %d\n", HELP, PRINT, EXEC, OTHER);
    return 0;
}''', "0 1 5 6", r"Les valeurs commencent à $0$ et suivent de $1$ en $1$ ; après `EXEC = 5`, `OTHER` vaut $6$."),
        pr("m13", r'''struct var
{
    char *name;
    char *value;
    struct var *next;
};

int main(void)
{
    struct var *v = calloc(1, sizeof(*v));
    printf("%d %d\n", v->name == NULL, v->next == NULL);
    free(v);
    return 0;
}''', "1 1", r"`calloc` met tout le bloc à zéro : les pointeurs valent `NULL`. `sizeof(*v)` est la taille de la structure, pas du pointeur."),
        w("m14", r"Écrire `struct rule *rule_new(const char *target)` : alloue une règle (`calloc`), copie la cible (`strdup`), sans dépendance ni commande. Et `void rule_free(struct rule *r)`.", r'''struct rule
{
    char *target;
    struct rule *next;
};

struct rule *rule_new(const char *target)
{
    struct rule *r = calloc(1, sizeof(*r));
    if (!r)
        return NULL;
    r->target = strdup(target);
    return r;
}

void rule_free(struct rule *r)
{
    free(r->target);
    free(r);
}''', r'''int main(void)
{
    char buf[] = "all";
    struct rule *r = rule_new(buf);
    buf[0] = 'X';
    printf("%s %d\n", r->target, r->next == NULL);
    rule_free(r);
    return 0;
}''', "all 1", r"`strdup` copie la chaîne : modifier `buf` ensuite ne change pas la cible. On libère la copie puis la structure (dans cet ordre)."),
        o("m15", r"Le sujet conseille un `enum` pour l'action à faire. Écrire cet `enum` et dire pourquoi c'est mieux que trois `int` booléens.",
          "```c\nenum action { ACTION_HELP, ACTION_PRINT, ACTION_EXEC };\n```\nUne seule variable de ce type ne peut valoir qu'une action à la fois : impossible d'avoir « aide » et « affichage » vrais ensemble. Le `switch` sur l'`enum` rend la priorité explicite (`-h` gagne sur `-p`) et `-Wall` avertit si un `case` manque."),
    ]},
    {"n": 2, "titre": "Makefile du projet", "notions": ["makefile"], "exos": [
        o("m21", r"Écrire le `Makefile` minimal du projet : binaire `minimake` à partir de `main.c` et `parse.c`, avec les options imposées par le sujet, une règle `clean`.",
          "```make\nCC = gcc\nCFLAGS = -Wall -Wextra -fsanitize=address -g\n\nminimake: main.o parse.o\n\t${CC} ${CFLAGS} -o minimake main.o parse.o\n\nmain.o: main.c\n\t${CC} ${CFLAGS} -c main.c\n\nparse.o: parse.c\n\t${CC} ${CFLAGS} -c parse.c\n\nclean:\n\trm -f minimake *.o\n```\n`-fsanitize=address` doit aussi être passé à l'édition de liens. `minimake` est la première règle : c'est elle que `make` construit par défaut."),
        o("m22", r"Un `Makefile` écrit avec des espaces devant les commandes donne `*** missing separator.  Stop.` Pourquoi ?",
          r"Une ligne de recette doit commencer par une **tabulation** (`'\t'`). Avec des espaces, `make` ne la reconnaît pas comme commande et ne sait pas l'analyser. C'est aussi la règle que Minimake applique : une commande est une ligne qui commence par `'\t'`."),
        v("m23", r"`all: a b`, `a: c`, `b: c`, `c:` (sans fichier). Combien de fois la recette de `c` est-elle exécutée par GNU `make all` ?", "1", "1", r"`make` ne construit une cible qu'une fois par exécution, même si plusieurs règles en dépendent."),
        o("m24", r"Pourquoi le dépôt Minimake doit-il avoir un `.gitignore`, et que doit-il contenir au minimum ?",
          "Le sujet l'impose avant le premier rendu. Il évite de pousser les fichiers produits par la compilation : `*.o`, `*.a`, `*.out`, le binaire `minimake`, les fichiers d'éditeur (`*~`, `.idea/`). On ne rend que les sources, le `Makefile` et les tests."),
        o("m25", r"Que signale `-fsanitize=address` à la fin d'un programme qui fait `malloc` sans `free`, et pourquoi c'est bloquant pour Minimake ?",
          "AddressSanitizer (avec LeakSanitizer) affiche `ERROR: LeakSanitizer: detected memory leaks` et le programme sort en erreur. La notation exige « no leaks » : un test qui fuit est raté même si la sortie est juste. Il faut donc libérer variables, règles, commandes et le tampon de `getline` avant de quitter, y compris sur les chemins d'erreur."),
    ]},
    {"n": 3, "titre": "Découper une chaîne", "notions": ["chaines"], "exos": [
        pr("m31", r'''int main(void)
{
    char line[] = "all: foo bar";
    char *sep = strchr(line, ':');
    *sep = '\0';
    printf("[%s] [%s]\n", line, sep + 1);
    return 0;
}''', "[all] [ foo bar]", r"Le `':'` est remplacé par `'\0'` : `line` s'arrête avant, et `sep + 1` commence juste après (avec l'espace)."),
        pr("m32", r'''int main(void)
{
    printf("%d %d %d\n", strcmp("all", "all") == 0, strcmp("a", "b") < 0, !strcmp("all", "al"));
    printf("%d\n", strchr("FOO=1", ':') == NULL);
    return 0;
}''', "1 1 0\n1", r"`strcmp` vaut $0$ si égales, négatif si la première est avant ; `strchr` renvoie `NULL` si le caractère est absent."),
        pr("m33", r'''#include <stdio.h>
#include <ctype.h>

int main(void)
{
    printf("%d %d %d %d\n", isblank(' ') != 0, isblank('\t') != 0, isblank('\n') != 0, isblank('a') != 0);
    return 0;
}''', "1 1 0 0", r"`isblank` : seulement l'espace et la tabulation. `'\n'` est un « space » (`isspace`) mais pas un « blank »."),
        w("m34", r"Écrire `char *trim(char *s)` qui enlève les blancs (`isblank`) au début et à la fin de `s`, en place, et renvoie le début de la chaîne utile.", r'''#include <stdio.h>
#include <string.h>
#include <ctype.h>

char *trim(char *s)
{
    while (isblank(*s))
        s++;
    size_t n = strlen(s);
    while (n > 0 && isblank(s[n - 1]))
        n--;
    s[n] = '\0';
    return s;
}''', r'''int main(void)
{
    char a[] = "  FOO \t";
    char b[] = "\t\t";
    printf("[%s] [%s]\n", trim(a), trim(b));
    return 0;
}''', "[FOO] []", r"On avance le début, puis on recule la fin et on pose un `'\0'`. Une chaîne toute blanche devient vide. Le pointeur renvoyé est dans le tableau d'origine : ne pas le passer à `free`."),
        pr("m35", r'''int main(void)
{
    char buf[16] = "foo";
    char *keep = buf;
    char *copy = strdup(buf);
    strcpy(buf, "bar");
    printf("%s %s\n", keep, copy);
    free(copy);
    return 0;
}''', "bar foo", r"`keep` pointe sur le même tableau : il voit la nouvelle valeur. `strdup` a fait une copie indépendante : c'est ce qu'il faut pour garder un nom après le `getline` suivant."),
    ]},
    {"n": 4, "titre": "Lire le Makefile : fopen, getline", "notions": ["getline"], "exos": [
        pr("m41", r'''int main(void)
{
    FILE *f = fopen("mk.txt", "w");
    fputs("all: foo\n\tgcc x\n", f);
    fclose(f);

    f = fopen("mk.txt", "r");
    char *line = NULL;
    size_t n = 0;
    ssize_t len;
    while ((len = getline(&line, &n, f)) != -1)
        printf("%zd %d\n", len, line[0] == '\t');
    free(line);
    fclose(f);
    return 0;
}''', "9 0\n7 1", r"`getline` renvoie la longueur **avec** le `'\n'` : `all: foo\n` fait $9$, `\tgcc x\n` fait $7$. Un seul `free` après la boucle."),
        pr("m42", r'''int main(void)
{
    FILE *f = fopen("absent/Makefile", "r");
    if (!f)
    {
        printf("cannot open\n");
        return 3;
    }
    printf("opened\n");
    fclose(f);
    return 0;
}''', "cannot open", r"`fopen` renvoie `NULL` si le fichier ne peut pas être ouvert. Le sujet : fichier de `-f` absent $\Rightarrow$ message d'erreur et code $3$."),
        w("m43", r"Écrire `void chomp(char *line)` qui retire le `'\n'` final s'il existe (la dernière ligne d'un fichier peut ne pas en avoir).", r'''void chomp(char *line)
{
    size_t n = strlen(line);
    if (n > 0 && line[n - 1] == '\n')
        line[n - 1] = '\0';
}''', r'''int main(void)
{
    char a[] = "all: foo\n";
    char b[] = "last";
    char c[] = "";
    chomp(a);
    chomp(b);
    chomp(c);
    printf("[%s] [%s] [%s]\n", a, b, c);
    return 0;
}''', "[all: foo] [last] []", r"Tester `n > 0` avant de lire `line[n - 1]` : sur une chaîne vide, l'indice $-1$ sort du tableau."),
        o("m44", r"Ce code fuit et ASan le signale. Pourquoi ? Corriger." + "\n\n" + _blk('''char *line = NULL;
size_t n = 0;
while (getline(&line, &n, f) != -1)
{
    parse(line);
    free(line);
    line = NULL;
}'''), r"Après le dernier appel (celui qui renvoie $-1$), `getline` a pu allouer un tampon : il n'est jamais libéré. Et libérer à chaque tour est inutile (le tampon est réutilisé). Correct : ne pas libérer dans la boucle, faire un seul `free(line);` après la boucle, même si aucune ligne n'a été lue."),
        v("m45", r"Une ligne `\tgcc -c foo.c\n` est lue par `getline`. Quelle valeur renvoie-t-il ?", "1 + 12 + 1", "14", r"Tabulation ($1$) + `gcc -c foo.c` ($12$) + `'\n'` ($1$)."),
    ]},
    {"n": 5, "titre": "Listes chaînées de variables et de règles", "notions": ["listes"], "exos": [
        w("m51", r"Écrire `void push_back(struct var **head, const char *name)` qui ajoute une variable (nom copié) **en fin** de liste, pour garder l'ordre du Makefile.", r'''struct var
{
    char *name;
    struct var *next;
};

void push_back(struct var **head, const char *name)
{
    struct var *v = calloc(1, sizeof(*v));
    v->name = strdup(name);
    while (*head)
        head = &(*head)->next;
    *head = v;
}''', r'''int main(void)
{
    struct var *l = NULL;
    push_back(&l, "CC");
    push_back(&l, "CFLAGS");
    push_back(&l, "SRC");
    for (struct var *v = l; v; v = v->next)
        printf("%s ", v->name);
    printf("\n");
    while (l)
    {
        struct var *next = l->next;
        free(l->name);
        free(l);
        l = next;
    }
    return 0;
}''', "CC CFLAGS SRC", r"`head` avance de champ `next` en champ `next` jusqu'au `NULL` final, qu'on remplace par le nouveau maillon. Le double pointeur gère aussi la liste vide sans cas particulier."),
        w("m52", r"Écrire `struct var *find(struct var *l, const char *name)` : le maillon de ce nom, ou `NULL`.", r'''struct var
{
    char *name;
    char *value;
    struct var *next;
};

struct var *find(struct var *l, const char *name)
{
    for (; l; l = l->next)
        if (!strcmp(l->name, name))
            return l;
    return NULL;
}''', r'''int main(void)
{
    struct var c = { "SRC", "main.c", NULL };
    struct var b = { "CC", "gcc", &c };
    struct var *v = find(&b, "SRC");
    printf("%s %d\n", v->value, find(&b, "OBJ") == NULL);
    return 0;
}''', "main.c 1", r"On compare les noms avec `strcmp`, jamais avec `==` (qui compare les adresses)."),
        o("m53", r"Ce code de libération est faux. Pourquoi ?" + "\n\n" + _blk('''for (struct var *v = l; v; v = v->next)
    free(v);'''), r"Après `free(v)`, l'incrément `v = v->next` lit dans un bloc libéré (*heap-use-after-free* pour ASan). Il faut sauver le suivant avant : `while (v) { struct var *n = v->next; free(v->name); free(v->value); free(v); v = n; }` (sans oublier les chaînes allouées dans le maillon)."),
        pr("m54", r'''struct node
{
    int val;
    struct node *next;
};

int main(void)
{
    struct node c = { 3, NULL }, b = { 2, &c }, a = { 1, &b };
    int n = 0, s = 0;
    for (struct node *p = &a; p; p = p->next)
    {
        n++;
        s += p->val;
    }
    printf("%d %d\n", n, s);
    return 0;
}''', "3 6", r"Parcours classique : on s'arrête sur le `next` qui vaut `NULL`."),
        o("m55", r"Une règle a une cible, des dépendances (en nombre quelconque) et des commandes (en nombre quelconque). Proposer les structures C.",
          "```c\nstruct str_list\n{\n    char *s;\n    struct str_list *next;\n};\n\nstruct rule\n{\n    char *target;\n    struct str_list *deps;\n    struct str_list *cmds;\n    struct rule *next;\n};\n\nstruct makefile\n{\n    struct var *vars;\n    struct rule *rules;\n};\n```\nUne liste de chaînes sert aux dépendances et aux commandes. Une structure `makefile` regroupe tout pour la passer aux fonctions (conseil du sujet)."),
    ]},
    {"n": 6, "titre": "Règle ou variable ? Analyser une ligne", "notions": ["parsing", "chaines"], "exos": [
        w("m61", r"Écrire `int line_kind(const char *s)` : renvoie `'R'` si le premier `':'` ou `'='` est un `':'`, `'V'` si c'est un `'='`, `0` si aucun des deux.", r'''int line_kind(const char *s)
{
    for (; *s; s++)
    {
        if (*s == ':')
            return 'R';
        if (*s == '=')
            return 'V';
    }
    return 0;
}''', r'''int main(void)
{
    printf("%c %c %d\n", line_kind("all: foo"), line_kind("X = a:b"), line_kind("echo hi"));
    printf("%c\n", line_kind("t: A=1"));
    return 0;
}''', "R V 0\nR", r"C'est le premier des deux caractères qui décide : `X = a:b` est une variable (le `=` vient avant le `:`)."),
        w("m62", r"Écrire `void split_var(char *line, char **name, char **value)` : coupe `NOM = valeur` sur le premier `'='`, enlève les blancs autour du nom et **avant** la valeur (la valeur garde ses blancs internes et finaux, comme dans le sujet).", r'''#include <stdio.h>
#include <string.h>
#include <ctype.h>

void split_var(char *line, char **name, char **value)
{
    char *eq = strchr(line, '=');
    *eq = '\0';
    while (isblank(*line))
        line++;
    char *end = eq;
    while (end > line && isblank(end[-1]))
        end--;
    *end = '\0';
    char *v = eq + 1;
    while (isblank(*v))
        v++;
    *name = line;
    *value = v;
}''', r'''int main(void)
{
    char l[] = "  FOO  =         foo               bar              ";
    char *n, *v;
    split_var(l, &n, &v);
    printf("[%s] [%s]\n", n, v);
    return 0;
}''', "[FOO] [foo bar ]", r"Le nom est nettoyé des deux côtés, la valeur seulement au début. Le vérificateur compacte les espaces ; la vraie sortie est `[FOO] [foo               bar              ]`, exactement l'exemple du sujet (la valeur s'étend jusqu'à la fin de ligne)."),
        w("m63", r"Écrire `int count_deps(const char *s)` : nombre de mots séparés par des blancs dans la partie dépendances d'une règle.", r'''#include <ctype.h>

int count_deps(const char *s)
{
    int n = 0;
    while (*s)
    {
        while (isblank(*s))
            s++;
        if (!*s)
            break;
        n++;
        while (*s && !isblank(*s))
            s++;
    }
    return n;
}''', r'''#include <stdio.h>

int main(void)
{
    printf("%d %d %d\n", count_deps(" foo.o  bar.o\tbaz.o "), count_deps(""), count_deps("   "));
    return 0;
}''', "3 0 0", r"On saute les blancs, on compte un mot, on saute le mot. Les chaînes vides ou toutes blanches n'ont aucune dépendance."),
        o("m64", r"Ces lignes suivent la règle `all: foo`. Lesquelles appartiennent à sa recette ? (`→` = tabulation)" + "\n\n" + _out("→echo a\n\n# commentaire\n→echo b\nFOO = 1\n→echo c"),
          r"`echo a` et `echo b` : la ligne vide et le commentaire peuvent se trouver dans une recette. La recette s'arrête à `FOO = 1` (ni tabulation, ni vide, ni commentaire). `→echo c` commence par une tabulation mais n'appartient à aucune règle : erreur « command outside of rule »."),
        v("m65", r"`./minimake -p` sur `sparse_rule: depa depb` : combien de dépendances sont affichées (format `[depa]`) ?", "2", "2", r"`(sparse_rule): [depa] [depb]`."),
    ]},
    {"n": 7, "titre": "Variables : expansion ${VAR}", "notions": ["variables"], "exos": [
        w("m71", r"Écrire `char *expand(const char *s, struct var *vars)` : renvoie une nouvelle chaîne où chaque `${NOM}` est remplacé par sa valeur (chaîne vide si inconnue). On suppose les `}` présents. Allouer assez grand.", r'''struct var
{
    char *name;
    char *value;
    struct var *next;
};

static const char *lookup(struct var *v, const char *name, size_t len)
{
    for (; v; v = v->next)
        if (strlen(v->name) == len && !strncmp(v->name, name, len))
            return v->value;
    return "";
}

char *expand(const char *s, struct var *vars)
{
    size_t cap = strlen(s) + 1, n = 0;
    char *out = malloc(cap);
    while (*s)
    {
        const char *val = NULL;
        size_t vlen = 1;
        if (s[0] == '$' && s[1] == '{')
        {
            const char *end = strchr(s + 2, '}');
            val = lookup(vars, s + 2, end - (s + 2));
            vlen = strlen(val);
            s = end + 1;
        }
        if (n + vlen + 1 > cap)
        {
            cap = 2 * (n + vlen + 1);
            out = realloc(out, cap);
        }
        if (val)
        {
            memcpy(out + n, val, vlen);
            n += vlen;
        }
        else
            out[n++] = *s++;
    }
    out[n] = '\0';
    return out;
}''', r'''int main(void)
{
    struct var b = { "SRC", "main.c", NULL };
    struct var a = { "CC", "gcc", &b };
    char *r = expand("${CC} -c ${SRC} ${NOPE}x", &a);
    printf("[%s]\n", r);
    free(r);
    return 0;
}''', "[gcc -c main.c x]", r"La valeur peut être plus longue que `${NOM}` : on agrandit le tampon (`realloc`). Variable inconnue : chaîne vide, pas d'erreur. Pour `${` sans `}`, `strchr` renvoie `NULL` : Minimake doit le traiter comme une erreur (non géré ici)."),
        o("m72", r"Valeur de `OBJ` et dépendances de `all` ?" + "\n\n" + _out("all: ${FILE}\n\techo useless rule\n\nFILE=foo bar\nOBJ=${SRC}.o\nSRC = main.c"),
          r"`all` n'a **aucune** dépendance : `FILE` n'est pas encore défini quand la ligne de `all` est lue (expansion au parsing, vide). `OBJ` vaut `.o` pour la même raison (`SRC` est défini après). C'est l'exemple du sujet."),
        o("m73", r"Qu'affiche `./minimake` ?" + "\n\n" + _out("all:\n\techo The answer is ${FOO}\n\nFOO  =   42"),
          "```\necho The answer is 42\nThe answer is 42\n```\nLes commandes sont expansées à l'exécution : tout le fichier est lu, `FOO` est connu. Minimake affiche la commande expansée, puis `sh` l'exécute."),
        v("m74", r"`A = x`, `B = ${A}${A}y`, `C = ${B}${B}`. Combien de caractères dans la valeur de `C` ?", "2 * 3", "6", r"`B` $=$ `xxy` ($3$), `C` $=$ `xxyxxy` ($6$) : chaque valeur est expansée au moment où elle est lue."),
        o("m75", r"`VAR=42` puis `echo ${VAR` dans une recette. Variable vide, ou erreur ?", r"Erreur : `${` sans `}` fermant est un cas d'erreur cité par le sujet (contrairement à une variable non définie, qui donne une chaîne vide). Minimake affiche un message sur la sortie standard et renvoie $2$."),
    ]},
    {"n": 8, "titre": "Ligne de commande : -f, -h, -p, cibles", "notions": ["options"], "exos": [
        pr("m81", r'''int main(int argc, char *argv[])
{
    (void) argc;
    char *av[] = { "./minimake", "all", "-f", "mk", "check", NULL };
    argv = av;
    argc = 5;
    for (int i = 1; i < argc; i++)
    {
        if (!strcmp(argv[i], "-f"))
            printf("file=%s\n", argv[++i]);
        else
            printf("target=%s\n", argv[i]);
    }
    return 0;
}''', "target=all\nfile=mk\ntarget=check", r"Les options peuvent être n'importe où ; `++i` consomme le mot qui suit `-f`, qui n'est donc pas une cible."),
        w("m82", r"Écrire `int parse_args(int argc, char **argv, struct opts *o)` : remplit `o->file` (dernier `-f`, par défaut `\"Makefile\"`), `o->help`, `o->print`, `o->ntargets`. Renvoie `2` si `-f` est le dernier argument, `0` sinon.", r'''struct opts
{
    const char *file;
    int help;
    int print;
    int ntargets;
};

int parse_args(int argc, char **argv, struct opts *o)
{
    o->file = "Makefile";
    o->help = o->print = o->ntargets = 0;
    for (int i = 1; i < argc; i++)
    {
        if (!strcmp(argv[i], "-f"))
        {
            if (i + 1 == argc)
                return 2;
            o->file = argv[++i];
        }
        else if (!strcmp(argv[i], "-h"))
            o->help = 1;
        else if (!strcmp(argv[i], "-p"))
            o->print = 1;
        else
            o->ntargets++;
    }
    return 0;
}''', r'''int main(void)
{
    struct opts o;
    char *a[] = { "m", "-f", "a", "x", "-f", "-h", "-p" };
    int r = parse_args(7, a, &o);
    printf("%d %s %d %d %d\n", r, o.file, o.help, o.print, o.ntargets);
    char *b[] = { "m", "all", "-f" };
    printf("%d\n", parse_args(3, b, &o));
    return 0;
}''', "0 -h 0 1 1\n2", r"Le dernier `-f` gagne et son argument est `-h` : c'est un **nom de fichier**, pas l'aide (piège cité par le sujet). `-f` sans fichier : code $2$."),
        o("m83", r"`./minimake all -h` : que se passe-t-il, et quel code de sortie ?", r"L'aide (`Usage: minimake [OPTIONS] [TARGETS]` …) est affichée sur la sortie standard et rien n'est construit : `-h` a priorité sur tout, même placé après une cible. Code de sortie $0$. D'où l'intérêt de lire tous les arguments avant d'agir."),
        o("m84", r"`./minimake -p -f Makefile all` : que doit faire Minimake ?", r"Analyser `Makefile` et afficher variables puis règles au format du sujet (`# variables`, `'NOM' = 'valeur'`, `# rules`, `(cible): [dep]`, commandes entre `'…'`), dans l'ordre du fichier, **sans rien exécuter** : la cible `all` est ignorée."),
        v("m85", r"Fichier donné à `-f` impossible à ouvrir : quel code de sortie ?", "3", "3", r"Le sujet : fichier inexistant $\Rightarrow$ message d'erreur et code $3$ (les autres erreurs donnent $2$)."),
    ]},
    {"n": 9, "titre": "Processus : fork, exec, waitpid", "notions": ["processus"], "exos": [
        pr("m91", r'''#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main(void)
{
    pid_t pid = fork();
    if (pid == 0)
    {
        printf("child\n");
        return 4;
    }
    int st;
    waitpid(pid, &st, 0);
    printf("parent %d %d\n", WIFEXITED(st) != 0, WEXITSTATUS(st));
    return 0;
}''', "child\nparent 1 4", r"Le fils affiche et sort avec $4$ (son tampon est vidé à sa sortie, avant que le père ne reprenne). Le père attend, puis lit le code avec `WEXITSTATUS`."),
        w("m92", r"Écrire `int run(const char *cmd)` : exécute `cmd` avec `/bin/sh -c` dans un processus fils, attend la fin et renvoie le code de sortie.", r'''#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int run(const char *cmd)
{
    fflush(stdout);
    fflush(stderr);
    pid_t pid = fork();
    if (pid == -1)
        return -1;
    if (pid == 0)
    {
        execl("/bin/sh", "sh", "-c", cmd, (char *) NULL);
        _exit(127);
    }
    int st;
    waitpid(pid, &st, 0);
    return WIFEXITED(st) ? WEXITSTATUS(st) : 1;
}''', r'''int main(void)
{
    printf("%d\n", run("true"));
    printf("%d\n", run("false"));
    printf("%d\n", run("exit 7"));
    printf("%d\n", run("notACommand 2>/dev/null"));
    return 0;
}''', "0\n1\n7\n127", r"`execl` ne revient qu'en cas d'échec : `_exit(127)` évite que le fils continue le code de Minimake. Commande introuvable : `sh` renvoie $127$. Le `fflush` avant `fork` est expliqué au niveau suivant."),
        pr("m93", r'''#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main(void)
{
    for (int i = 0; i < 3; i++)
    {
        pid_t pid = fork();
        if (pid == 0)
            _exit(i);
        int st;
        waitpid(pid, &st, 0);
        printf("%d", WEXITSTATUS(st));
    }
    printf("\n");
    return 0;
}''', "012", r"Chaque fils sort tout de suite avec `_exit(i)` (qui ne vide pas le tampon copié : avec `return`, les chiffres déjà dans le tampon du père sortiraient en double) ; le père les attend un par un, dans l'ordre : `0`, `1`, `2`."),
        o("m94", r"Une recette contient `false` puis `echo \"will not appear\"`. Qu'affiche Minimake et pourquoi le `echo` n'est-il pas lancé ?",
          "```\nfalse\nminimake: *** [falseRule] Error 1\n```\nLa commande est affichée puis exécutée ; son code ($1$) est non nul, donc Minimake arrête la règle à cette commande et affiche l'erreur avec le code. Le code de sortie final de Minimake est $2$."),
        o("m95", r"Que se passe-t-il si le fils oublie `_exit` après un `execl` qui échoue ?",
          r"`execl` revient et le fils continue d'exécuter la suite du code de Minimake : il construit les règles suivantes en même temps que le père (commandes exécutées deux fois, sorties mêlées), puis libère et quitte de son côté. Toujours terminer le fils juste après `exec` : `_exit(127);`."),
    ]},
    {"n": 10, "titre": "Afficher la commande avant : fflush", "notions": ["tampons", "processus"], "exos": [
        pr("m101", r'''#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main(void)
{
    printf("A\n");
    pid_t pid = fork();
    if (pid == 0)
        return 0;
    waitpid(pid, NULL, 0);
    return 0;
}''', "A\nA", r"Sortie dans un fichier : `A\n` reste dans le tampon. `fork` copie le tampon ; le fils et le père le vident chacun en sortant. Sur un terminal, on ne verrait qu'un `A` : c'est pour ça que le bug n'apparaît qu'avec la moulinette."),
        pr("m102", r'''#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main(void)
{
    printf("echo hi\n");
    pid_t pid = fork();
    if (pid == 0)
    {
        execl("/bin/sh", "sh", "-c", "echo hi", (char *) NULL);
        _exit(127);
    }
    waitpid(pid, NULL, 0);
    return 0;
}''', "hi\necho hi", r"La copie du tampon dans le fils est jetée par `exec` ; `sh` écrit `hi` tout de suite ; le père n'écrit `echo hi` qu'à sa sortie. Résultat : la commande s'affiche **après** son résultat. Test raté."),
        pr("m103", r'''#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main(void)
{
    printf("echo hi\n");
    fflush(stdout);
    pid_t pid = fork();
    if (pid == 0)
    {
        execl("/bin/sh", "sh", "-c", "echo hi", (char *) NULL);
        _exit(127);
    }
    waitpid(pid, NULL, 0);
    return 0;
}''', "echo hi\nhi", r"`fflush` vide le tampon avant le `fork` : le fils hérite d'un tampon vide, l'ordre est le bon. C'est la consigne « Logging » du sujet."),
        w("m104", r"Écrire `void log_cmd(const char *cmd)` : affiche la commande sans les espaces ni tabulations du début, puis un retour à la ligne, et vide les tampons.", r'''#include <stdio.h>
#include <ctype.h>

void log_cmd(const char *cmd)
{
    while (isblank(*cmd))
        cmd++;
    printf("%s\n", cmd);
    fflush(stdout);
    fflush(stderr);
}''', r'''int main(void)
{
    log_cmd("\t  echo toto");
    log_cmd("\techo foo");
    return 0;
}''', "echo toto\necho foo", r"Le sujet : « delete every space or tab before the command », puis `fflush` avant l'exécution."),
        o("m105", r"Pourquoi faut-il aussi `fflush(stderr)` alors que `stderr` n'a pas de tampon par défaut ?",
          r"`stderr` est non tamponné par défaut, mais un programme peut changer son mode (`setvbuf`), et le sujet le demande explicitement. L'appel ne coûte rien et garantit l'ordre des messages d'erreur par rapport aux sorties des commandes."),
    ]},
    {"n": 11, "titre": "Dépendances et messages d'erreur", "notions": ["dependances"], "exos": [
        w("m111", r"Règles simplifiées : `struct rule { const char *target; const char *deps[4]; }` (fin par `NULL`). Écrire `int build(struct rule *rules, int n, const char *t)` qui construit d'abord les dépendances, puis affiche `build T` ; renvoie $2$ avec le message exact si une dépendance n'a pas de règle.", r'''struct rule
{
    const char *target;
    const char *deps[4];
};

static struct rule *find_rule(struct rule *rules, int n, const char *t)
{
    for (int i = 0; i < n; i++)
        if (!strcmp(rules[i].target, t))
            return &rules[i];
    return NULL;
}

int build(struct rule *rules, int n, const char *t)
{
    struct rule *r = find_rule(rules, n, t);
    for (int i = 0; r->deps[i]; i++)
    {
        if (!find_rule(rules, n, r->deps[i]))
        {
            printf("minimake: *** No rule to make target '%s', needed by '%s'.  Stop.\n", r->deps[i], t);
            return 2;
        }
        if (build(rules, n, r->deps[i]))
            return 2;
    }
    printf("build %s\n", t);
    return 0;
}''', r'''int main(void)
{
    struct rule r[] = {
        { "all", { "foo", "bar", NULL } },
        { "foo", { "foo.o", NULL } },
        { "foo.o", { NULL } },
        { "bar", { "tutu", NULL } },
    };
    printf("%d\n", build(r, 4, "all"));
    return 0;
}''', "build foo.o\nbuild foo\nminimake: *** No rule to make target 'tutu', needed by 'bar'. Stop.\n2", r"Parcours en profondeur : `foo.o`, puis `foo` ; `bar` échoue sur `tutu`, donc `all` n'est pas construit. (Le vérificateur compacte les espaces : le vrai message a **deux** espaces avant `Stop.`.)"),
        o("m112", r"Le Makefile est vide. Message de `./minimake` ? Et de `./minimake toto` ?",
          "```\nminimake: *** No targets.  Stop.\nminimake: *** No rule to make target 'toto'.  Stop.\n```\nDans les deux cas le code de sortie est $2$. Deux espaces avant `Stop.`, apostrophes simples autour du nom."),
        o("m113", r"`./minimake -f Makefile.false falseRule good` : `falseRule` échoue. `good` est-elle construite ? Code de sortie ?",
          r"Oui : les cibles de la ligne de commande sont construites dans l'ordre, et un échec sur l'une n'empêche pas de tenter la suivante (exemple du sujet : `echo \"All good!\"` s'affiche après l'erreur). Le code de sortie est $2$ car une erreur a eu lieu."),
        v("m114", r"`all: a b`, `a: c`, `b:` et `c:`, chaque règle a une commande `echo`. Combien de lignes affiche `./minimake` (commande affichée + sa sortie) ?", "4 * 2", "8", r"$4$ règles construites (`c`, `a`, `b`, `all`), chacune affiche sa commande puis le résultat de `echo` : $8$ lignes."),
        o("m115", r"Le sujet ne teste ni les dépendances circulaires ni les cibles en double. Que risque malgré tout un Minimake récursif naïf sur `a: b` / `b: a` ?",
          r"Une récursion infinie : `build(a)` appelle `build(b)` qui appelle `build(a)`… jusqu'au débordement de pile (*stack overflow*, ASan l'affiche). Ce n'est pas testé, mais savoir pourquoi évite de chercher ce bug au mauvais endroit."),
    ]},
    {"n": 12, "titre": "Bonus : cibles à jour avec stat", "notions": ["stat"], "exos": [
        pr("m121", r'''#include <stdio.h>
#include <sys/stat.h>

int main(void)
{
    struct stat sb;
    FILE *f = fopen("x.c", "w");
    fputs("abc", f);
    fclose(f);
    int r = stat("x.c", &sb);
    printf("%d %ld\n", r, (long) sb.st_size);
    printf("%d\n", stat("absent.c", &sb));
    return 0;
}''', "0 3\n-1", r"`stat` est appelé avant de lire `sb` (dans un seul `printf`, l'ordre d'évaluation des arguments n'est pas fixé). Il renvoie $0$ et remplit la structure (ici la taille, $3$ octets) ; $-1$ si le fichier n'existe pas."),
        w("m122", r"Écrire `int newer(const char *a, const char *b)` : $1$ si le fichier `a` a été modifié strictement après `b`, $0$ sinon (et $0$ si l'un n'existe pas).", r'''#include <stdio.h>
#include <sys/stat.h>

int newer(const char *a, const char *b)
{
    struct stat sa, sb;
    if (stat(a, &sa) || stat(b, &sb))
        return 0;
    return sa.st_mtime > sb.st_mtime;
}''', r'''#include <utime.h>

int main(void)
{
    fclose(fopen("file.c", "w"));
    fclose(fopen("file.o", "w"));
    struct utimbuf old = { 1000, 1000 };
    utime("file.c", &old);
    printf("%d %d %d\n", newer("file.o", "file.c"), newer("file.c", "file.o"), newer("file.o", "nope"));
    return 0;
}''', "1 0 0", r"`st_mtime` (équivalent de `st_mtim.tv_sec`) est la date de modification. Le test recule la date de `file.c` avec `utime` pour ne pas dépendre de la seconde courante."),
        o("m123", r"`file.c` est créé, puis `file.o`. Règle `file.o: file.c` avec `echo Yes !`. Sortie de `./minimake file.o` ?",
          "```\nminimake: 'file.o' is up to date.\n```\nLe fichier cible existe et sa seule dépendance est plus ancienne : rien n'est exécuté. Le nom est entre apostrophes simples, suivi d'un retour à la ligne."),
        o("m124", r"Les trois conditions pour qu'une cible soit à jour ?",
          r"1. Un fichier du nom de la cible existe. 2. Chaque dépendance qui est un fichier est plus ancienne que la cible. 3. Chaque dépendance est elle-même à jour (la liste peut être vide). Une cible comme `all` (pas de fichier `all`) n'est donc jamais à jour."),
        v("m125", r"`stat` renvoie `st_mtim.tv_sec` $=1716800000$ pour la cible et $1716800060$ pour la dépendance. De combien de secondes la dépendance est-elle plus récente ?", "1716800060 - 1716800000", "60", r"La dépendance est plus récente de $60$ s : la cible n'est pas à jour, il faut la reconstruire."),
    ]},
    {"n": 13, "titre": "Récap Minimake", "notions": ["parsing", "variables", "options", "processus", "tampons", "dependances"], "exos": [
        o("m131", r"Donner les étapes de Minimake, dans l'ordre, et la donnée que chaque étape passe à la suivante.",
          r"1. **Arguments** : lire tout `argv` $\to$ structure d'options (fichier, action `enum`, liste des cibles). 2. **Aide** : si `-h`, afficher et sortir $0$. 3. **Lecture** : `fopen` + `getline` $\to$ listes de variables et de règles (expansion au parsing). 4. **Affichage** : si `-p`, afficher et sortir. 5. **Exécution** : pour chaque cible demandée (ou la première), construire récursivement dépendances puis commandes (expansion, affichage, `fflush`, `fork`/`exec`/`waitpid`). 6. **Fin** : tout libérer, renvoyer $0$ ou $2$."),
        o("m132", r"Qu'affiche `./minimake` ?" + "\n\n" + _out("NEEDED = hello\n\nall: ${NEEDED}\n\techo All good!\n\nhello:\n\techo Hello"),
          "```\necho Hello\nHello\necho All good!\nAll good!\n```\n`NEEDED` est défini avant `all` : la dépendance vaut `hello`. `all` (première règle) construit d'abord `hello`. Code de sortie $0$."),
        o("m133", r"Qu'affiche `./minimake -f Makefile_ls`, avec `ls to/` qui échoue (code $2$) ?" + "\n\n" + _out("all: l_rule\n\techo Hello\nl_rule:\n\tls to/"),
          "```\nls to/\nls: cannot access 'to/': No such file or directory\nminimake: *** [l_rule] Error 2\n```\nLa dépendance échoue : la recette de `all` n'est pas lancée. Le message d'erreur de `ls` vient de `ls` lui-même (sur sa sortie d'erreur)."),
        o("m134", r"Liste de contrôle avant le tag `submit-*` : citer cinq points du sujet.",
          r"Le binaire `minimake` se construit avec **votre** `Makefile` et `-Wall -Wextra -fsanitize=address -g` ; aucune fuite (ASan) ; arborescence `minimake/` + `.gitignore` + `README` ; au moins $35\%$ des tests de chaque catégorie *Fundamentals* ; des tests ajoutés à `tests/tests.yaml` ; prototypes respectés ; tests perso retirés. Rappel : `submit` $1$ par heure, la note prend le **dernier** `submit`."),
        w("m135", r"Écrire `int exit_code(int had_error)` puis le `main` d'un mini-programme qui exécute deux commandes avec `/bin/sh -c`, les affiche avant, s'arrête à la première en échec avec le message du sujet, et renvoie $2$ en cas d'erreur.", r'''#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int exit_code(int had_error)
{
    return had_error ? 2 : 0;
}

static int run(const char *cmd)
{
    printf("%s\n", cmd);
    fflush(stdout);
    fflush(stderr);
    pid_t pid = fork();
    if (pid == 0)
    {
        execl("/bin/sh", "sh", "-c", cmd, (char *) NULL);
        _exit(127);
    }
    int st;
    waitpid(pid, &st, 0);
    return WIFEXITED(st) ? WEXITSTATUS(st) : 1;
}''', r'''int main(void)
{
    const char *recipe[] = { "false", "echo \"will not appear\"" };
    int err = 0;
    for (int i = 0; i < 2 && !err; i++)
    {
        int code = run(recipe[i]);
        if (code)
        {
            printf("minimake: *** [falseRule] Error %d\n", code);
            err = 1;
        }
    }
    printf("exit %d\n", exit_code(err));
    return 0;
}''', "false\nminimake: *** [falseRule] Error 1\nexit 2", r"Affichage, `fflush`, `fork`, `exec`, `waitpid`, arrêt au premier code non nul : tout le moteur d'exécution de Minimake tient dans ces lignes."),
    ]},
]

EXTRA_PARTS = []

QUIZ = [
    {"notion": "structs", "type": "qcm", "q": r"`p->x` est équivalent à :", "choix": [r"`(*p).x`", r"`*p.x`", r"`&p.x`", r"`p.x`"], "bonne": 0},
    {"notion": "structs", "type": "vf", "q": r"`calloc` met tous les octets du bloc à zéro.", "bonne": True},
    {"notion": "makefile", "type": "qcm", "q": r"Une ligne de recette de Makefile commence par :", "choix": [r"une tabulation", r"quatre espaces", r"un `$`", r"un `@` obligatoire"], "bonne": 0},
    {"notion": "makefile", "type": "vf", "q": r"Sans cible, `make` construit la dernière règle du fichier.", "bonne": False},
    {"notion": "chaines", "type": "qcm", "q": r"`strcmp(a, b)` vaut $0$ quand :", "choix": [r"les chaînes sont égales", r"`a` est plus courte", r"`b` est vide", r"une erreur survient"], "bonne": 0},
    {"notion": "chaines", "type": "vf", "q": r"`isblank('\n')` est vrai.", "bonne": False},
    {"notion": "getline", "type": "qcm", "q": r"Le tampon de `getline` doit être libéré :", "choix": [r"une seule fois après la boucle", r"à chaque tour", r"jamais", r"seulement si une ligne a été lue"], "bonne": 0},
    {"notion": "getline", "type": "vf", "q": r"La ligne lue par `getline` contient le `'\n'` final s'il existe.", "bonne": True},
    {"notion": "listes", "type": "qcm", "q": r"Pour garder l'ordre du Makefile dans une liste, on ajoute :", "choix": [r"en fin de liste", r"en tête de liste", r"au milieu", r"dans un tableau fixe"], "bonne": 0},
    {"notion": "listes", "type": "vf", "q": r"On peut lire `v->next` juste après `free(v)`.", "bonne": False},
    {"notion": "parsing", "type": "qcm", "q": r"`X = a:b` est :", "choix": [r"une variable", r"une règle", r"une commande", r"une erreur"], "bonne": 0},
    {"notion": "parsing", "type": "vf", "q": r"Une ligne qui commence par une tabulation hors de toute règle est une erreur.", "bonne": True},
    {"notion": "variables", "type": "qcm", "q": r"Une variable non définie s'expanse en :", "choix": [r"chaîne vide", r"erreur, code 2", r"son nom", r"`NULL`"], "bonne": 0},
    {"notion": "variables", "type": "vf", "q": r"Dans une commande, on peut utiliser une variable définie plus bas dans le Makefile.", "bonne": True},
    {"notion": "options", "type": "qcm", "q": r"`./minimake -f -h` :", "choix": [r"ouvre le fichier nommé `-h`", r"affiche l'aide", r"renvoie $2$", r"ignore `-f`"], "bonne": 0},
    {"notion": "options", "type": "vf", "q": r"Si `-f` est donné deux fois, Minimake prend le premier.", "bonne": False},
    {"notion": "processus", "type": "qcm", "q": r"Dans le fils, `fork()` renvoie :", "choix": [r"$0$", r"le pid du père", r"le pid du fils", r"$-1$"], "bonne": 0},
    {"notion": "processus", "type": "vf", "q": r"`execl` revient seulement en cas d'échec.", "bonne": True},
    {"notion": "tampons", "type": "qcm", "q": r"Sortie redirigée vers un fichier, `printf(\"A\\n\")` puis `fork()` sans `fflush` :", "choix": [r"`A` peut sortir deux fois", r"`A` sort une fois, toujours", r"`A` est perdu", r"erreur de compilation"], "bonne": 0},
    {"notion": "tampons", "type": "vf", "q": r"`exec` vide le tampon de `stdout` du processus avant de le remplacer.", "bonne": False},
    {"notion": "dependances", "type": "qcm", "q": r"Code de sortie de Minimake après une erreur d'exécution :", "choix": [r"$2$", r"$1$", r"$127$", r"$0$"], "bonne": 0},
    {"notion": "dependances", "type": "vf", "q": r"Les messages d'erreur de Minimake vont sur la sortie standard.", "bonne": True},
    {"notion": "stat", "type": "qcm", "q": r"`stat` sur un fichier absent renvoie :", "choix": [r"$-1$", r"$0$", r"`NULL`", r"la date $0$"], "bonne": 0},
    {"notion": "stat", "type": "vf", "q": r"La cible `all`, sans fichier `all`, peut être à jour.", "bonne": False},
]

_FL = {
    1: r"`p->c` $\equiv$ `(*p).c` · `enum` : $0, 1, 2…$ · `calloc(1, sizeof(*p))` · `strdup` puis `free`",
    2: r"recette : tabulation · `-Wall -Wextra -fsanitize=address -g` · première règle par défaut · aucune fuite",
    3: r"`strchr` · `strcmp == 0` · `isblank` : espace, `'\\t'` · couper avec `'\\0'` · `strdup`",
    4: r"`getline(&line, &n, f)` · longueur avec `'\\n'` · un `free(line)` après la boucle · `fopen` `NULL` $\Rightarrow$ code $3$",
    5: r"ajout en fin · `find` par `strcmp` · sauver `next` avant `free` · `struct node **head`",
    6: r"1er de `:` / `=` · commande : `'\\t'` · blancs autour de `=` · valeur jusqu'en fin de ligne",
    7: r"`${VAR}` · inconnue $\to$ vide · parsing : déjà lues · exécution : tout le fichier · `${` sans `}` : erreur",
    8: r"`argv` en entier d'abord · dernier `-f` · `-h` prioritaire · `-f` sans fichier : $2$ · absent : $3$",
    9: r"`fork` · `execl(\"/bin/sh\", \"sh\", \"-c\", cmd, NULL)` · `_exit(127)` · `waitpid` · `WEXITSTATUS`",
    10: r"tampon copié par `fork` · jeté par `exec` · `fflush(stdout); fflush(stderr);` avant `fork`",
    11: r"dépendances d'abord (récursif) · `No rule to make target 'D', needed by 'R'.  Stop.` · code $2$",
    12: r"`stat(path, &sb)` · `st_mtim.tv_sec` · `minimake: 'T' is up to date.`",
    13: r"options $\to$ lecture $\to$ `-p` $\to$ exécution · `fflush` + `fork`/`exec`/`waitpid` · code $0$ / $2$",
}
FORMULES = {e["id"]: _FL[lvl["n"]] for lvl in LEVELS for e in lvl["exos"]}
