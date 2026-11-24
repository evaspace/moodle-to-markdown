const $ = id => document.getElementById(id);

// Elements
const feed = $('feed');
const chillCat = $('chill-cat');
const catBubble = $('cat-bubble');
const streakVal = $('streak-val');
const streakPill = $('streak-counter');
const heartAnim = $('like-animation');
const folderModal = $('folder-modal');
const folderList = $('folder-list');
const catList = $('category-list');
const searchOverlay = $('search-overlay');
const searchInput = $('search-input');
const searchResults = $('search-results');
const searchBtn = $('search-btn');
const headerBackBtn = $('header-back-btn');
const toastEl = $('toast');
const goreCanvas = $('gore-canvas');
const appViewport = $('app-viewport');

// ------------------------------------------------------------ CONFIGURATION & PARSER MATH LATEX ----
const UNICODE_MATH_SYMBOLS = {
    // Inégalités, équivalences et approximations
    '≤': '\\le ', '≥': '\\ge ', '≠': '\\ne ', '≈': '\\approx ', '≡': '\\equiv ',
    '∝': '\\propto ', '±': '\\pm ', '∓': '\\mp ', '∼': '\\sim ', '≃': '\\simeq ',
    
    // Opérateurs
    '×': '\\times ', '÷': '\\div ', '⋅': '\\cdot ', '·': '\\cdot ', '∘': '\\circ ',
    '⊗': '\\otimes ', '⊕': '\\oplus ',
    
    // Ensembles, logique et quantificateurs
    '∈': '\\in ', '∉': '\\notin ', '⊂': '\\subset ', '⊆': '\\subseteq ',
    '⊃': '\\supset ', '⊇': '\\supseteq ', '∪': '\\cup ', '∩': '\\cap ',
    '∅': '\\emptyset ', '∀': '\\forall ', '∃': '\\exists ', '∄': '\\nexists ',
    '⇒': '\\implies ', '⇐': '\\impliedby ', '⇔': '\\iff ', '→': '\\to ',
    '←': '\\leftarrow ', '↔': '\\leftrightarrow ', '↦': '\\mapsto ',
    '∧': '\\land ', '∨': '\\lor ', '¬': '\\neg ',
    
    // Analyse, calcul différentiel & sommations
    '∞': '\\infty ', '∑': '\\sum ', '∏': '\\prod ', '∫': '\\int ',
    '∬': '\\iint ', '∭': '\\iiint ', '∮': '\\oint ', '∂': '\\partial ',
    '∇': '\\nabla ', '√': '\\sqrt ',
    
    // Ensembles de nombres usuels
    'ℝ': '\\mathbb{R}', 'ℂ': '\\mathbb{C}', 'ℕ': '\\mathbb{N}',
    'ℤ': '\\mathbb{Z}', 'ℚ': '\\mathbb{Q}', '𝕂': '\\mathbb{K}'
};

const KATEX_OPTS = {
    delimiters: [
        { left: '$$', right: '$$', display: true },
        { left: '\\[', right: '\\]', display: true },
        { left: '$', right: '$', display: false },
        { left: '\\(', right: '\\)', display: false }
    ],
    ignoredTags: ["script", "noscript", "style", "textarea", "pre", "code"],
    throwOnError: false,
    errorColor: '#E63946',
    strict: false,
    trust: true
};

function formatMathMarkdown(text) {
    if (!text) return '';
    let s = String(text).trim();

    // 0. Nettoyage des accolades de titre de cours (ex: {Théorème de Pythagore})
    s = s.replace(/^\s*\{([^{}]+)\}\s*$/, '$1');

    const mathBlocks = [];

    // 1. Isoler les blocs de maths en affichage hors-ligne ($$...$$ et \[...\])
    s = s.replace(/(\$\$[\s\S]*?\$\$|\\\[[\s\S]*?\\\])/g, match => {
        const id = `___MATH_DISPLAY_${mathBlocks.length}___`;
        mathBlocks.push({ type: 'display', code: match });
        return id;
    });

    // 2. Isoler les blocs de maths inline (\(...\) et $...$)
    s = s.replace(/(\\\([\s\S]*?\\\)|\$([^\$\n]+?)\$)/g, match => {
        const id = `___MATH_INLINE_${mathBlocks.length}___`;
        mathBlocks.push({ type: 'inline', code: match });
        return id;
    });

    // 3. Détecter intelligemment les équations polynomiales et formules sans délimiteurs
    // Exemples : P(X) = -2X^3 + 3X - 4  ou  f'(x) = 2x + 1
    s = s.replace(/\b([A-Za-z](?:'[A-Za-z]*)?\([A-Za-z0-9_]+\)\s*=[^,;\n?]+)/g, match => {
        if (match.includes('___MATH_')) return match;
        const id = `___MATH_INLINE_${mathBlocks.length}___`;
        mathBlocks.push({ type: 'inline', code: `\\(${match.trim()}\\)` });
        return id;
    });

    // 4. Remplacer les symboles Unicode mathématiques isolés dans le texte restant
    for (const [sym, latex] of Object.entries(UNICODE_MATH_SYMBOLS)) {
        if (s.includes(sym)) {
            s = s.split(sym).join(` \\(${latex.trim()}\\) `);
        }
    }

    // 5. Échappement HTML sécurisé uniquement sur le texte pur
    s = s.replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

    // 6. Typographie Markdown standard
    s = s.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
    s = s.replace(/\*([^*\n]+?)\*/g, '<em>$1</em>');
    s = s.replace(/`([^`\n]+?)`/g, '<code class="math-code">$1</code>');
    s = s.replace(/\n/g, '<br>');

    // 7. Restauration des blocs LaTeX originaux avec normalisation Unicode interne
    mathBlocks.forEach((b, idx) => {
        let code = b.code;
        // Remplacer aussi les symboles Unicode à l'intérieur du LaTeX pour KaTeX
        for (const [sym, latex] of Object.entries(UNICODE_MATH_SYMBOLS)) {
            if (code.includes(sym)) {
                code = code.split(sym).join(latex);
            }
        }
        const placeholder = b.type === 'display' ? `___MATH_DISPLAY_${idx}___` : `___MATH_INLINE_${idx}___`;
        s = s.replace(placeholder, () => code);
    });

    return s;
}

let session = 0;
let isFetching = false;
let currentCat = null;   // one category id or an array of ids (merged duplicates)
let currentSub = null;
let currentTheme = null; // theme id: doomscroll every module of a theme
let currentCardToSave = null;
let uidCounter = 0;
let catTimer = null;
let toastTimer = null;

const seenIds = new Set();
const cardTimers = {};

const esc = s => String(s ?? '').replace(/[&<>"']/g,
    c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

const shuffle = a => {
    for (let i = a.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
};

const elapsed = uid => cardTimers[uid] ? Date.now() - cardTimers[uid] : 0;

// Initialisation des instances moteurs
const landingCat = $('landing-cat-img');
const landingCatBubble = $('landing-cat-bubble');
const catMascot = new CatMascotEngine([chillCat, landingCat]);
const pixelGore = new PixelGoreFX(goreCanvas, appViewport);
catMascot.startIdleLife();
catMascot.onBoom = () => {  // 10 caresses trop rapides
    const origin = getMascotCenter(chillCat);
    catMascot.onWrongAnswer(() => pixelGore.explode(origin.x, origin.y));
};

function getMascotCenter(el) {
    if (!el) {
        const w = appViewport ? appViewport.clientWidth : window.innerWidth;
        const h = appViewport ? appViewport.clientHeight : window.innerHeight;
        return { x: w - 50, y: h - 50 };
    }
    const rect = el.getBoundingClientRect();
    const vpRect = appViewport ? appViewport.getBoundingClientRect() : { left: 0, top: 0 };
    return {
        x: (rect.left + rect.width / 2) - vpRect.left,
        y: (rect.top + rect.height / 2) - vpRect.top
    };
}

// Événements de curiosité au survol sur desktop
[chillCat, landingCat].forEach(el => {
    if (!el) return;
    el.addEventListener('mouseenter', () => {
        if (!catMascot.isLocked && catMascot.state === 'REST') {
            catMascot.setState('WAKE');
        }
    });
    el.addEventListener('mouseleave', () => {
        if (!catMascot.isLocked && catMascot.state === 'WAKE') {
            catMascot.setState('REST');
        }
    });
});

// ------------------------------------------------------------ TOAST & FEEDBACK ----
function showToast(text, duration = 2500) {
    if (!toastEl) return;
    clearTimeout(toastTimer);
    toastEl.textContent = text;
    toastEl.classList.remove('hidden');
    toastTimer = setTimeout(() => toastEl.classList.add('hidden'), duration);
}

function showCatBubble(text, duration = 2200) {
    const isLanding = $('landing-screen') && $('landing-screen').classList.contains('visible');
    const bubble = isLanding && landingCatBubble ? landingCatBubble : catBubble;
    if (!bubble) return;
    clearTimeout(catTimer);
    bubble.textContent = text;
    bubble.classList.remove('hidden');
    catTimer = setTimeout(() => {
        bubble.classList.add('hidden');
    }, duration);
}

function petTheCat() {
    if (catMascot.onPet() === false) return;  // agacé ou explosé : il a déjà parlé
    const isLanding = $('landing-screen') && $('landing-screen').classList.contains('visible');
    const quotes = isLanding ? [
        "Ronron... Prêt à doomscroller les maths ? 🐾",
        "Miaou ! Les théorèmes n'attendent que toi 🧠",
        "Clique sur 'Tout doomscroller' ! ⚡",
        "Zzz... 5 minutes de plus... ou un QCM ? 😼",
        "Prépare tes neurones pour le 20/20 ! ✨"
    ] : [
        "Ronron... Reste concentré ! 🐾",
        "Miaou ! Les maths c'est la vie 🧠",
        "Objectif 20/20 au prochain partiel ! 🎯",
        "Scroll encore une carte pour voir... 😼",
        "Zzz... Tu gères la fougère ! ✨",
        "Câlin de pixel ! ❤️🐱"
    ];
    showCatBubble(quotes[Math.floor(Math.random() * quotes.length)], 2200);
    if (navigator.vibrate) navigator.vibrate([30, 40, 30]);
}

function triggerFeedback(correct) {
    const currentStreak = streakVal ? parseInt(streakVal.textContent || '0', 10) : 0;
    if (correct) {
        const nextStreak = currentStreak + 1;
        let quote = "Miaou ! 🎉 +1 STREAK !";
        if (nextStreak === 3) {
            quote = "🔥 COMBO x3 ! Tu chauffes !";
        } else if (nextStreak === 5) {
            quote = "⚡ SÉRIE DE 5 ! C'est le boss !";
        } else if (nextStreak === 10) {
            quote = "👑 STREAK DE 10 ! DIEU DES MATHS !";
        } else if (nextStreak > 10 && nextStreak % 5 === 0) {
            quote = `🏆 INCROYABLE ! SÉRIE DE ${nextStreak} !`;
        } else {
            const happyQuotes = [
                "Miaou ! 🎉 Bien joué !",
                "Parfait ! 🧠 En plein dans le mille !",
                "Machine de maths ! ✨",
                "Trop fort ! 🐾 On continue !",
                "Excellente intuition ! 🎯"
            ];
            quote = happyQuotes[Math.floor(Math.random() * happyQuotes.length)];
        }
        catMascot.onCorrectAnswer(nextStreak, quote);  // la phrase arrive après les « happy »
        if (streakPill) {
            streakPill.classList.add('pulse');
            setTimeout(() => streakPill.classList.remove('pulse'), 500);
        }
        if (navigator.vibrate) navigator.vibrate([40]);
    } else {
        // MAUVAISE RÉPONSE : Enchaînement Colère -> Surcharge -> EXPLOSION GORE PIXEL ART !
        const angryQuotes = [
            "Aïe... SURCHARGE COGNITIVE ! 💥",
            "NON ! Mes neurones fondent ! 🤯",
            "Erreur fatale ! KABOOM ! ⚡💥",
            "Grrr... Trop de maths d'un coup ! 😾"
        ];
        showCatBubble(angryQuotes[Math.floor(Math.random() * angryQuotes.length)], 1600);

        // Mesurer la position exacte du chat avant qu'il ne disparaisse
        const origin = getMascotCenter(chillCat);

        catMascot.onWrongAnswer(() => {
            pixelGore.explode(origin.x, origin.y);
            if (navigator.vibrate) navigator.vibrate([150, 50, 200, 80, 250]);
        });
    }
}

// ------------------------------------------------------------ PARTAGE (LE PETIT CHAT) ----
async function shareApp() {
    const shareData = {
        title: "Epita Doomscrolling",
        text: "Doomscrolle des maths au lieu de scroller TikTok ! 🧠🐱",
        url: window.location.origin
    };

    if (navigator.share && navigator.canShare && navigator.canShare(shareData)) {
        try {
            await navigator.share(shareData);
            showToast("Merci pour le partage ! 🐱");
            return;
        } catch (e) {
            if (e.name === 'AbortError') return;
        }
    }

    // Fallback : copie du lien dans le presse-papier
    try {
        await navigator.clipboard.writeText(window.location.origin);
        showToast("Lien copié dans le presse-papier ! 🐱");
        showCatBubble("Lien copié ! Fais tourner à tes potes 🐾", 2500);
    } catch (e) {
        showToast("epitadoomscrolling.pierref.eu");
    }
}

// ------------------------------------------------------------ CHARGEMENT CATÉGORIES ----
async function loadCategories() {
    try {
        const res = await fetch('/api/themes', { headers: { 'Accept': 'application/json' } });
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        const themes = await res.json();
        catList.innerHTML = '';

        if (!themes || !themes.length) {
            catList.innerHTML = '<div class="loading-state">Aucun module pour le moment.</div>';
            return;
        }

        themes.forEach(theme => catList.appendChild(buildThemeSection(theme)));
        if (window.slideInit) catList.querySelectorAll('[data-slide]').forEach(window.slideInit);
    } catch (e) {
        console.error('loadCategories error:', e);
        catList.innerHTML = `
            <div class="loading-state" role="alert">
                Impossible de charger les cours. Vérifie la connexion puis réessaie.
                <button type="button" class="subcat-btn" onclick="loadCategories()">Réessayer</button>
            </div>`;
    }
}

// Un thème (Maths, Physique...) : en-tête repliable + bouton « tout le thème » + ses modules
function buildThemeSection(theme) {
    const section = document.createElement('section');
    section.className = 'theme-section';

    const header = document.createElement('button');
    header.type = 'button';
    header.className = 'theme-header-btn';
    header.innerHTML = `
        <span class="theme-title"><span class="theme-icon">${esc(theme.icon)}</span>${esc(theme.label)}</span>
        <span class="cat-right-badge">
            <span class="cat-count">${theme.n}</span>
            <span class="cat-chevron">›</span>
        </span>`;
    header.onclick = () => section.classList.toggle('expanded');

    const body = document.createElement('div');
    body.className = 'theme-body';

    const allBtn = document.createElement('button');
    allBtn.type = 'button';
    allBtn.className = 'theme-all-btn';
    allBtn.innerHTML = `<span>⚡ Doomscroller tout le thème</span> <span>${theme.n} cartes →</span>`;
    allBtn.onclick = () => launchFeed(null, null, theme.id);
    body.appendChild(allBtn);

    theme.categories.forEach((cat, index) => body.appendChild(buildCategoryCard(cat, index)));
    body.dataset.slide = 'fill';
    body.dataset.slideItems = '.category-header-btn';

    section.appendChild(header);
    section.appendChild(body);
    return section;
}

function buildCategoryCard(cat, index) {
            const card = document.createElement('div');
            card.className = 'category-card';

            const numStr = String(index + 1).padStart(2, '0');
            const totalCount = cat.n || 0;
            const catIds = cat.ids && cat.ids.length ? cat.ids : [cat.id];

            const headerBtn = document.createElement('button');
            headerBtn.className = 'category-header-btn';
            headerBtn.innerHTML = `
                <div class="cat-title-wrap">
                    <span class="cat-num">[${numStr}]</span>
                    <span class="cat-name">${esc(cat.name)}</span>
                </div>
                <div class="cat-right-badge">
                    <span class="cat-count">${totalCount}</span>
                    <span class="cat-chevron">›</span>
                </div>
            `;

            // Menu déroulant des sous-catégories
            const subDropdown = document.createElement('div');
            subDropdown.className = 'subcategory-dropdown';
            subDropdown.dataset.slide = 'fill';

            // Option 1 : Tout le module
            const allSubBtn = document.createElement('button');
            allSubBtn.className = 'subcat-btn';
            allSubBtn.innerHTML = `<span>→ Tout le module</span> <span class="subcat-count">${totalCount} cartes</span>`;
            allSubBtn.onclick = (e) => {
                e.stopPropagation();
                launchFeed(catIds, null);
            };
            subDropdown.appendChild(allSubBtn);

            // Accès direct au cours complet du module
            if (cat.source_url) {
                const courseLink = document.createElement('a');
                courseLink.className = 'subcat-btn subcat-course-link';
                courseLink.href = cat.source_url;
                courseLink.innerHTML = '<span>📖 Lire le cours complet</span> <span class="subcat-count">→</span>';
                subDropdown.appendChild(courseLink);
            }

            // Sous-catégories individuelles
            if (cat.subcategories && cat.subcategories.length) {
                cat.subcategories.forEach(sub => {
                    const subBtn = document.createElement('button');
                    subBtn.className = 'subcat-btn';
                    subBtn.innerHTML = `<span>→ ${esc(sub.name)}</span> <span class="subcat-count">${sub.n} cartes</span>`;
                    subBtn.onclick = (e) => {
                        e.stopPropagation();
                        launchFeed(catIds, sub.id);
                    };
                    subDropdown.appendChild(subBtn);
                });
            }

            headerBtn.onclick = () => {
                const isExpanded = card.classList.contains('expanded');
                document.querySelectorAll('.category-card.expanded').forEach(c => {
                    if (c !== card) c.classList.remove('expanded');
                });
                card.classList.toggle('expanded', !isExpanded);
            };

            card.appendChild(headerBtn);
            card.appendChild(subDropdown);
            return card;
}

// ------------------------------------------------------------ NAVIGATION ----
// The feed has its own URL (/?cat=..&sub=..&theme=..) so the browser back button
// returns to the module list instead of leaving the site, and a reload keeps the feed.
function feedUrl(catId, subId, themeId) {
    const qs = new URLSearchParams();
    if (themeId) qs.set('theme', themeId);
    if (catId) qs.set('cat', [].concat(catId).join(','));
    if (subId) qs.set('sub', subId);
    return '/?' + (qs.toString() || 'feed=all');
}

function feedFromUrl() {
    const qs = new URLSearchParams(location.search);
    if (!['cat', 'sub', 'theme', 'feed'].some(k => qs.has(k))) return null;
    const cat = (qs.get('cat') || '').split(',').filter(x => /^\d+$/.test(x)).map(Number);
    const sub = /^\d+$/.test(qs.get('sub') || '') ? Number(qs.get('sub')) : null;
    return [cat.length ? cat : null, sub, qs.get('theme')];
}

function launchFeed(catId, subId, themeId = null, fromHistory = false) {
    if (!fromHistory) history.pushState({ feed: true }, '', feedUrl(catId, subId, themeId));
    session++;
    isFetching = false;
    currentTheme = themeId;
    currentCat = catId;
    currentSub = subId;
    seenIds.clear();

    $('landing-screen').classList.replace('visible', 'hidden');
    $('feed-screen').classList.replace('hidden', 'visible');
    if (headerBackBtn) headerBackBtn.classList.remove('hidden');

    catMascot.onFeedEntered();
    showCatBubble("C'est parti ! 🧠 Doomscrolle des maths !", 2000);

    fetchUserState();
    fetchFolders();
    loadCards();

    // Focus sur le feed pour permettre les touches fléchées desktop
    feed.focus({ preventScroll: true });  // focus alone scrolls #app-viewport and hides the header
}

function goHome(fromHistory = false) {
    // header ← button: undo our own pushState so browser history stays consistent
    if (!fromHistory && history.state && history.state.feed) { history.back(); return; }
    if (!fromHistory && location.search) history.replaceState(null, '', '/');
    session++;
    isFetching = false;
    observer.disconnect();
    Object.keys(cardTimers).forEach(k => delete cardTimers[k]);
    feed.innerHTML = '';
    closeFolderModal();

    $('feed-screen').classList.replace('visible', 'hidden');
    $('landing-screen').classList.replace('hidden', 'visible');
    if (headerBackBtn) headerBackBtn.classList.add('hidden');

    catMascot.onHomeEntered();

    loadCategories();
}

function renderState(s) {
    // combo = correct answers in a row in the feed (local to the page)
    if (s && streakVal && s.streak !== undefined) streakVal.textContent = s.streak;
}

// Navbar pill: paper levels validated (the figure that matters), links to /stats
async function fetchUserState() {
    const pill = $('me-pill');
    try {
        const me = await (await fetch('/api/me')).json();
        if (pill && me.logged) {
            pill.href = '/stats';
            pill.title = `${me.username} : ${me.xp} pts` + (me.streak ? `, ${me.streak} jour(s) d'affilée` : '');
            pill.textContent = `${me.levels_done}/${me.levels_total} niveaux`;
        }
        const st = await (await fetch('/api/user_state')).json();
        renderState(st);
    } catch (e) {}
}

// ------------------------------------------------------------ KATEX RENDER ----
function renderMath(element) {
    if (!element) return;
    const doRender = () => {
        if (window.renderMathInElement) {
            try {
                window.renderMathInElement(element, KATEX_OPTS);
            } catch (err) {
                console.error('KaTeX error:', err);
            }
        }
    };

    if (window.renderMathInElement) {
        doRender();
    } else {
        const checkInterval = setInterval(() => {
            if (window.renderMathInElement) {
                clearInterval(checkInterval);
                doRender();
            }
        }, 80);
        setTimeout(() => clearInterval(checkInterval), 6000);
    }
}

// Re-vérification automatique lorsque KaTeX finit de charger
window.addEventListener('load', () => {
    if (window.renderMathInElement) {
        document.querySelectorAll('.card').forEach(c => renderMath(c));
    }
});

// ------------------------------------------------------------ INTERSECTION OBSERVER ----
const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        const el = entry.target;
        const uid = el.dataset.uid;
        if (entry.isIntersecting) {
            cardTimers[uid] = Date.now();
            const idx = Array.prototype.indexOf.call(feed.children, el);
            if (idx >= feed.children.length - 3) {
                loadCards();
            }
            if (!el.classList.contains('answered')) {
                catMascot.onCardView();
            }
        } else if (cardTimers[uid]) {
            if (el.dataset.type === 'COURSE') {
                sendLog(el.dataset.id, Date.now() - cardTimers[uid], null);
            }
            delete cardTimers[uid];
        }
    });
}, { root: feed, threshold: 0.5 });

// ------------------------------------------------------------ CHARGEMENT CARTES ----
function retryCardLoad() {
    session++;
    isFetching = false;
    seenIds.clear();
    observer.disconnect();
    feed.replaceChildren();
    loadCards();
}

async function loadCards() {
    if (isFetching) return;
    isFetching = true;
    const mine = session;

    try {
        const qs = new URLSearchParams();
        if (currentCat) qs.set('cat', [].concat(currentCat).join(','));
        if (currentSub) qs.set('sub', currentSub);
        if (currentTheme) qs.set('theme', currentTheme);
        if (seenIds.size) qs.set('exclude', [...seenIds].slice(-300).join(','));

        const res = await fetch('/api/cards?' + qs, { headers: { 'Accept': 'application/json' } });
        if (!res.ok) throw new Error(res.status);
        const cards = await res.json();
        if (mine !== session) return;

        if (!cards.length && !feed.children.length) {
            feed.innerHTML = `
                <div class="card">
                    <div class="card-body" style="text-align: center;">
                        <div class="card-front">AUCUNE CARTE DISPONIBLE</div>
                        <div class="card-back" style="display:block">Aucune carte n’est disponible dans ce module. Réessaie le chargement ou ajoute des cartes via /admin.</div>
                        <button type="button" class="subcat-btn" onclick="retryCardLoad()">Réessayer</button>
                    </div>
                </div>
            `;
            return;
        }

        // Scroll infini : si tout le lot a déjà été vu (pool épuisé), on recycle
        // les cartes au lieu de bloquer le feed.
        let toAdd = cards.filter(c => !seenIds.has(c.id));
        if (!toAdd.length && cards.length) {
            seenIds.clear();
            toAdd = cards;
        }
        toAdd.forEach(c => {
            seenIds.add(c.id);
            const card = buildCard(c, ++uidCounter);
            feed.appendChild(card);
            renderMath(card);
            observer.observe(card);
        });
        // If all returned cards were duplicates and we got some, maybe still need more? but avoid infinite loop
        if (cards.length > 0 && feed.querySelectorAll('.card').length < 5 && !isFetching) {
            // load more
            setTimeout(loadCards, 10);
        }
    } catch (e) {
        console.error('loadCards error:', e);
        if (mine === session && !feed.children.length) {
            feed.innerHTML = `
                <div class="card">
                    <div class="card-body" style="text-align:center">
                        <div class="card-front">ERREUR DE CHARGEMENT</div>
                        <div class="card-back" style="display:block">Le serveur n’a pas pu charger les cours. Vérifie ta connexion puis réessaie.</div>
                        <button type="button" class="subcat-btn" onclick="retryCardLoad()">Réessayer</button>
                    </div>
                </div>`;
        }
    } finally {
        if (mine === session) isFetching = false;
    }
}

// ------------------------------------------------------------ CONSTRUCTION CARTE ----
function buildCard(c, uid) {
    const card = document.createElement('div');
    card.className = 'card';
    card.dataset.id = c.id;
    card.dataset.uid = uid;
    card.dataset.type = c.type;

    const subcatName = c.subcategory_name || 'Général';
    const isLiked = !!c.is_favorite;

    let html = `
        <div class="card-header-badge">
            <span class="card-type-tag">[ ${esc(c.type)} ]</span>
            <span class="card-subcat-tag">${esc(subcatName)}</span>
        </div>

        <div class="card-action-bar">
            <button class="action-btn like-btn ${isLiked ? 'liked' : ''}" data-id="${c.id}" title="Liker" aria-label="Liker">
                <span class="action-icon">${isLiked ? '❤️' : '🤍'}</span>
            </button>
            <button class="action-btn folder-btn" data-id="${c.id}" title="Dossier" aria-label="Enregistrer dans un dossier">
                📁
            </button>
            <button class="action-btn flip-btn" title="Explication" aria-label="Voir l'explication">
                💡
            </button>
            <button class="action-btn ia-btn" title="Copier pour une IA" aria-label="Copier la carte pour une IA">IA</button>
            ${c.source_url ? `<a class="action-btn course-btn" href="${esc(c.source_url)}" title="Lire le cours de ce chapitre" aria-label="Lire le cours de ce chapitre">📖</a>` : ''}
        </div>

        <div class="card-body">
            <div class="card-front">${formatMathMarkdown(c.front)}</div>
    `;

    let qcmMultiple = false;
    if (c.type === 'QCM') {
        const choices = shuffle([...(c.payload?.choices || [])]);
        qcmMultiple = choices.filter(ch => ch.correct).length > 1;
        if (qcmMultiple) {
            html += '<div class="qcm-mode-hint">Plusieurs réponses sont justes : sélectionne-les puis valide.</div>';
        }
        html += '<div class="qcm-choices">' +
            choices.map(ch => `<button type="button" class="choice-btn" data-correct="${ch.correct}" aria-pressed="false">${formatMathMarkdown(ch.text)}</button>`).join('') +
            '</div>' + (qcmMultiple ? '<button type="button" class="qcm-submit-btn">Valider mes réponses</button>' : '');
    } else if (c.type === 'TF') {
        html += `
            <div class="tf-actions">
                <button class="tf-btn btn-faux" data-ans="false">✕ FAUX</button>
                <button class="tf-btn btn-vrai" data-ans="true">✓ VRAI</button>
            </div>
            <div class="tf-indicator tf-left">FAUX</div>
            <div class="tf-indicator tf-right">VRAI</div>
            <div class="tf-swipe-hint">← SWIPE GAUCHE FAUX · SWIPE DROITE VRAI →</div>
        `;
    } else if (c.type === 'COURSE') {
        html += `<button class="reveal-btn">VOIR L'INTUITION 💡</button>`;
    }

    if (c.back) {
        html += `<div class="card-back">${formatMathMarkdown(c.back)}</div>`;
    }

    html += `</div>`;
    card.innerHTML = html;

    // Actions latérales
    const likeBtn = card.querySelector('.like-btn');
    if (likeBtn) {
        likeBtn.onclick = (e) => {
            e.stopPropagation();
            toggleLike(c.id, likeBtn);
        };
    }

    const fldBtn = card.querySelector('.folder-btn');
    if (fldBtn) {
        fldBtn.onclick = (e) => {
            e.stopPropagation();
            currentCardToSave = Number(c.id);
            folderModal.classList.remove('hidden');
        };
    }

    const flipBtn = card.querySelector('.flip-btn');
    if (flipBtn) {
        flipBtn.onclick = (e) => {
            e.stopPropagation();
            card.classList.toggle('revealed');
            renderMath(card);
        };
    }

    card.querySelector('.ia-btn').onclick = (e) => {
        e.stopPropagation();
        copyCardForLLM(card, e.currentTarget, subcatName);
    };

    const revBtn = card.querySelector('.reveal-btn');
    if (revBtn) {
        revBtn.onclick = (e) => {
            e.stopPropagation();
            card.classList.toggle('revealed');
            renderMath(card);
        };
    }

    // Gestion QCM
    if (c.type === 'QCM') {
        const choiceButtons = [...card.querySelectorAll('.choice-btn')];
        const finishQcm = (chosenButtons) => {
            if (card.classList.contains('answered')) return;
            const correct = choiceButtons.filter(btn => btn.dataset.correct === 'true');
            const chosenSet = new Set(chosenButtons);
            const ok = chosenSet.size === correct.length && correct.every(btn => chosenSet.has(btn));
            card.classList.add('answered', 'revealed');
            choiceButtons.forEach(btn => {
                btn.disabled = true;
                if (btn.dataset.correct === 'true') btn.classList.add('correct');
                else if (chosenSet.has(btn)) btn.classList.add('wrong');
            });
            const submit = card.querySelector('.qcm-submit-btn');
            if (submit) submit.disabled = true;
            answer(card, c.id, ok);
        };

        if (qcmMultiple) {
            choiceButtons.forEach(btn => {
                btn.addEventListener('click', (e) => {
                    e.stopPropagation();
                    if (card.classList.contains('answered')) return;
                    const selected = btn.classList.toggle('selected');
                    btn.setAttribute('aria-pressed', String(selected));
                });
            });
            card.querySelector('.qcm-submit-btn')?.addEventListener('click', (e) => {
                e.stopPropagation();
                finishQcm(choiceButtons.filter(btn => btn.classList.contains('selected')));
            });
        } else {
            card.querySelectorAll('.choice-btn').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    e.stopPropagation();
                    if (card.classList.contains('answered')) return;
                    card.classList.add('answered', 'revealed');
                    const ok = btn.dataset.correct === 'true';
                    btn.classList.add(ok ? 'correct' : 'wrong');
                    if (!ok) {
                        choiceButtons.forEach(choice => {
                            if (choice.dataset.correct === 'true') choice.classList.add('correct');
                        });
                    }
                    choiceButtons.forEach(choice => choice.disabled = true);
                    answer(card, c.id, ok);
                });
            });
        }
    } else if (c.type === 'TF') {
        card.querySelectorAll('.tf-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.stopPropagation();
                if (card.classList.contains('answered')) return;
                const chosen = btn.dataset.ans === 'true';
                const correct = chosen === !!c.payload?.correct;
                card.querySelectorAll('.tf-btn').forEach(b => b.disabled = true);
                card.classList.add('answered', 'revealed', correct ? 'answered-ok' : 'answered-ko');
                answer(card, c.id, correct);
            });
        });

        attachSwipe(card, c);
    }

    attachTaps(card, c);
    return card;
}

// ------------------------------------------------------------ TAPS & DOUBLE TAP ----
function attachTaps(card, c) {
    let lastTap = 0;
    card.addEventListener('click', e => {
        if (e.target.closest('button') || e.target.closest('.card-action-bar')) return;
        const now = Date.now();
        const isDouble = now - lastTap < 300;
        lastTap = isDouble ? 0 : now;

        if (isDouble) {
            const likeBtn = card.querySelector('.like-btn');
            toggleLike(c.id, likeBtn);
        } else if (c.type === 'COURSE') {
            card.classList.toggle('revealed');
        }
    });
}

// ------------------------------------------------------------ SWIPE VRAI / FAUX ----
function attachSwipe(card, c) {
    let startX = 0, startY = 0, gesture = null, locked = false;
    const indL = card.querySelector('.tf-left'), indR = card.querySelector('.tf-right');

    const resetInd = () => {
        if (indL) indL.style.opacity = 0;
        if (indR) indR.style.opacity = 0;
    };
    const snapBack = () => {
        card.style.transition = 'transform 0.25s ease-out';
        card.style.transform = '';
        resetInd();
    };

    card.addEventListener('touchstart', e => {
        if (locked || card.classList.contains('answered')) return;
        startX = e.touches[0].clientX;
        startY = e.touches[0].clientY;
        gesture = null;
    }, { passive: true });

    card.addEventListener('touchmove', e => {
        if (locked || card.classList.contains('answered') || gesture === 'v') return;
        const dX = e.touches[0].clientX - startX;
        const dY = e.touches[0].clientY - startY;

        if (!gesture) {
            if (Math.abs(dX) < 8 && Math.abs(dY) < 8) return;
            gesture = Math.abs(dX) > Math.abs(dY) ? 'h' : 'v';
            if (gesture === 'v') return;
            card.style.transition = 'none';
        }

        e.preventDefault();
        card.style.transform = `translateX(${dX}px) rotate(${dX * 0.03}deg)`;
        if (indR) indR.style.opacity = dX > 0 ? Math.min(dX / 120, 1) : 0;
        if (indL) indL.style.opacity = dX < 0 ? Math.min(-dX / 120, 1) : 0;
    }, { passive: false });

    card.addEventListener('touchend', e => {
        if (locked || gesture !== 'h' || card.classList.contains('answered')) {
            gesture = null;
            return;
        }
        gesture = null;
        const dX = e.changedTouches[0].clientX - startX;
        const threshold = Math.min(90, window.innerWidth * 0.22);
        if (dX > threshold) handleAns(true);
        else if (dX < -threshold) handleAns(false);
        else snapBack();
    });

    card.addEventListener('touchcancel', () => {
        if (!locked && gesture === 'h') snapBack();
        gesture = null;
    });

    function handleAns(ans) {
        locked = true;
        const correct = ans === !!c.payload?.correct;
        card.style.transition = 'transform 0.22s ease-in, opacity 0.22s';
        card.style.transform = `translateX(${ans ? 120 : -120}%) rotate(${ans ? 20 : -20}deg)`;
        card.style.opacity = '0';
        answer(card, c.id, correct);

        setTimeout(() => {
            card.style.transition = 'none';
            card.style.transform = '';
            card.style.opacity = '';
            resetInd();
            card.querySelectorAll('.tf-btn').forEach(b => b.disabled = true);
            card.classList.add('answered', 'revealed', correct ? 'answered-ok' : 'answered-ko');
        }, 240);
    }
}

// ------------------------------------------------------------ VALIDATION RÉPONSE ----
async function answer(card, id, ok) {
    triggerFeedback(ok);
    const state = await sendLog(id, elapsed(card.dataset.uid), ok ? 1 : 0);
    renderState(state);
}

async function sendLog(id, time, correct) {
    try {
        const res = await fetch('/api/log', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            keepalive: true,
            body: JSON.stringify({
                card_id: Number(id),
                time_spent_ms: Math.round(time),
                is_correct: correct
            })
        });
        const data = await res.json();
        return data.state || null;
    } catch (e) {
        return null;
    }
}

// ------------------------------------------------------------ FAVORIS / DOSSIERS ----
function playHeart(emoji = '❤️') {
    if (!heartAnim) return;
    heartAnim.textContent = emoji;
    heartAnim.classList.remove('like-active');
    void heartAnim.offsetWidth;
    heartAnim.classList.add('like-active');
}

async function toggleLike(id, btnEl) {
    try {
        const res = await fetch('/api/favorite', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ card_id: Number(id) })
        });
        const data = await res.json();
        if (data.action === 'removed') {
            playHeart('💔');
            if (btnEl) {
                btnEl.classList.remove('liked');
                btnEl.querySelector('.action-icon').textContent = '🤍';
            }
            showToast("Retiré des favoris");
        } else if (data.action === 'added') {
            playHeart('❤️');
            if (btnEl) {
                btnEl.classList.add('liked');
                btnEl.querySelector('.action-icon').textContent = '❤️';
            }
            showToast("Ajouté aux favoris !");
        }
    } catch (e) {}
}

async function fetchFolders() {
    try {
        const res = await fetch('/api/folders');
        const folders = await res.json();
        folderList.innerHTML = '';
        if (!folders || !folders.length) {
            folderList.innerHTML = '<div style="color:#888; font-size:0.8rem; margin-bottom:10px;">Aucun dossier créé pour le moment.</div>';
            return;
        }
        folders.forEach(f => {
            const btn = document.createElement('button');
            btn.className = 'folder-item-btn';
            btn.textContent = `📁 ${f.name}`;
            btn.onclick = () => saveToFolder(f.id);
            folderList.appendChild(btn);
        });
    } catch (e) {}
}

async function createFolder() {
    const input = $('new-folder-name');
    const name = input.value.trim();
    if (!name) return;
    await fetch('/api/folders', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name })
    });
    input.value = '';
    fetchFolders();
}

async function saveToFolder(folderId) {
    if (currentCardToSave == null) return;
    await fetch('/api/favorite', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ card_id: currentCardToSave, folder_id: folderId })
    });
    showToast("Enregistré dans le dossier ! 📁");
    closeFolderModal();
}

function closeFolderModal() {
    folderModal.classList.add('hidden');
    currentCardToSave = null;
}

// ------------------------------------------------------------ RECHERCHE ----
let searchDebounce = null;
let searchSession = 0;

function openSearch() {
    searchSession++;
    const s = searchSession;
    if (searchOverlay) searchOverlay.classList.remove('hidden');
    // Show on landing or feed — blur background
    document.querySelectorAll('.screen').forEach(screen => {
        screen.style.filter = 'blur(4px)';
        screen.style.pointerEvents = 'none';
    });
    searchOverlay.style.pointerEvents = 'all';
    if (searchInput) {
        searchInput.focus();
        searchInput.value = '';
        if (searchResults) searchResults.innerHTML = '';
    }
}

function closeSearch() {
    searchSession++;
    if (searchOverlay) {
        searchOverlay.classList.add('hidden');
        searchOverlay.style.pointerEvents = 'none';
    }
    document.querySelectorAll('.screen').forEach(screen => {
        screen.style.filter = '';
        screen.style.pointerEvents = '';
    });
}

function escapeHTML(s) {
    return String(s ?? '').replace(/[&<>"']/g, c =>
        ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
}

async function performSearch(query) {
    if (!searchResults || query.length < 2) {
        if (searchResults) searchResults.innerHTML = '';
        return;
    }

    try {
        const qs = new URLSearchParams({ q: query, limit: 20 });
        const res = await fetch('/api/search?' + qs);
        if (!res.ok) throw new Error(res.status);
        const data = await res.json();
        renderSearchResults(data);
    } catch (e) {
        if (searchResults) searchResults.innerHTML =
            '<div class="search-empty">Erreur de recherche. Réessayez.</div>';
    }
}

function renderSearchResults(data) {
    if (!searchResults) return;

    const cats = data.categories || [];
    const cards = data.cards || [];

    let html = '';

    if (cats.length === 0 && cards.length === 0) {
        html = '<div class="search-empty">Aucun résultat pour "' + escapeHTML(data.q || '') + '"</div>';
    } else {
        if (cats.length > 0) {
            html += '<div class="search-result-divider">Catégories</div>';
            cats.forEach(cat => {
                html += '<div class="search-result-item" onclick="openCategoryFromSearch(' + cat.id + ')">' +
                    '<div class="search-result-cat">' + escapeHTML(cat.name) + '</div>' +
                    '<div class="search-result-sub">' + cat.n + ' cartes</div>' +
                    '</div>';
            });
        }
        if (cards.length > 0) {
            html += '<div class="search-result-divider">Cartes</div>';
            cards.forEach(c => {
                const title = c.front || c.back || '';
                html += '<div class="search-card-result" onclick="openCardFromSearch(' + c.id + ')">' +
                    '<div class="search-card-type">[' + escapeHTML(c.type) + ']</div>' +
                    '<div class="search-card-title">' + escapeHTML(title.substring(0, 80)) + '</div>' +
                    '<div class="search-card-subcat">' + escapeHTML(c.category_name) + ' / ' + escapeHTML(c.subcategory_name) + '</div>' +
                    '</div>';
            });
        }
    }

    searchResults.innerHTML = html;
}

function openCategoryFromSearch(catId) {
    closeSearch();
    launchFeed(catId, null);
}

function openCardFromSearch(cardId) {
    closeSearch();
    const card = searchResults.querySelector(`[data-card-id="${cardId}"]`);
    // Find card in DOM — for now just launch the feed filtered by category
    // The card will be visible in the feed
}

// Search input handler
if (searchInput) {
    searchInput.addEventListener('input', (e) => {
        const query = e.target.value.trim();
        clearTimeout(searchDebounce);
        searchDebounce = setTimeout(() => performSearch(query), 300);
    });
}

// Escape to close search
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && searchOverlay && !searchOverlay.classList.contains('hidden')) {
        closeSearch();
    }
    if ((e.key === '/' || e.key === 'S' || e.key === 's') &&
        searchOverlay && searchOverlay.classList.contains('hidden') &&
        document.activeElement.tagName !== 'INPUT' &&
        document.activeElement.tagName !== 'TEXTAREA') {
        e.preventDefault();
        openSearch();
    }
});

// Click outside to close
if (searchOverlay) {
    searchOverlay.addEventListener('click', (e) => {
        if (e.target === searchOverlay) closeSearch();
    });
}

// ------------------------------------------------------------ NAVIGATION CLAVIER DESKTOP ----
function scrollFeed(dir) {
    const cardHeight = feed.clientHeight;
    feed.scrollBy({ top: dir * cardHeight, behavior: 'smooth' });
}

window.addEventListener('keydown', e => {
    if ($('feed-screen').classList.contains('visible') && folderModal.classList.contains('hidden')) {
        if (e.key === 'ArrowDown' || e.key === ' ' || e.key === 'j') {
            e.preventDefault();
            scrollFeed(1);
        } else if (e.key === 'ArrowUp' || e.key === 'k') {
            e.preventDefault();
            scrollFeed(-1);
        } else if (e.key === 'ArrowLeft' || e.key === 'ArrowRight') {
            const cards = feed.querySelectorAll('.card');
            const center = feed.scrollTop + feed.clientHeight / 2;
            let currentCard = null;
            cards.forEach(c => {
                if (c.offsetTop <= center && c.offsetTop + c.clientHeight >= center) {
                    currentCard = c;
                }
            });
            if (currentCard && currentCard.dataset.type === 'TF' && !currentCard.classList.contains('answered')) {
                const btn = e.key === 'ArrowLeft' ? currentCard.querySelector('.btn-faux') : currentCard.querySelector('.btn-vrai');
                if (btn) btn.click();
            }
        }
        if (e.key === 'l' || e.key === 'L') {
            const cards = feed.querySelectorAll('.card');
            const center = feed.scrollTop + feed.clientHeight / 2;
            cards.forEach(c => {
                if (c.offsetTop <= center && c.offsetTop + c.clientHeight >= center) {
                    const likeBtn = c.querySelector('.like-btn');
                    if (likeBtn) likeBtn.click();
                }
            });
        }
    }
    // Recherche rapide : '/' ou 'S' quand pas dans un input
    if ((e.key === '/' || e.key === 's' || e.key === 'S') &&
        searchOverlay && searchOverlay.classList.contains('hidden') &&
        document.activeElement.tagName !== 'INPUT' &&
        document.activeElement.tagName !== 'TEXTAREA' &&
        document.activeElement.tagName !== 'BUTTON') {
        e.preventDefault();
        openSearch();
    }
});

window.addEventListener('popstate', () => {
    const f = feedFromUrl();
    if (f) launchFeed(f[0], f[1], f[2], true);
    else goHome(true);
});

// INITIALISATION
loadCategories();
const initialFeed = feedFromUrl();
if (initialFeed) launchFeed(initialFeed[0], initialFeed[1], initialFeed[2], true);
fetchUserState();
