const $ = id => document.getElementById(id);

// Elements
const feed = $('feed');
const chillCat = $('chill-cat');
const catBubble = $('cat-bubble');
const streakVal = $('streak-val');
const streakPill = $('streak-counter');
const levelVal = $('level-val');
const heartAnim = $('like-animation');
const folderModal = $('folder-modal');
const folderList = $('folder-list');
const catList = $('category-list');
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
let currentCat = null;
let currentSub = null;
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

// ------------------------------------------------------------ MOTEUR D'ANIMATION DU CHAT ----
/**
 * Machine d'états du Chat en Pixel Art
 * Sprites PNG transparents (removebg-preview) :
 * 1. REST : laying-cat-removebg-preview.png (Allongé au calme, respiration douce)
 * 2. WAKE : eyes-open-cat-removebg-preview.png (Yeux écarquillés, attentif & curieux)
 * 3. STAND : stand-up-cat-removebg-preview.png (Debout, concentré, idle actif)
 * 4. CLAP : clapping-cat-removebg-preview.png (Bonne réponse, applaudit et saute de joie !)
 * 5. ANGRY : angry-cat-removebg-preview.png (Mauvaise réponse : Phase 1 - Colère rouge intense)
 * 6. EXPLODE_1 : first-explosing-cat-removebg-preview.png (Mauvaise réponse : Phase 2 - Surcharge critique)
 * 7. EXPLODE_2 : seconde-explosing-cat-removebg-preview.png (Mauvaise réponse : Phase 3 - Détonation explosive)
 */
class CatMascotEngine {
    constructor(elements = []) {
        this.elements = (Array.isArray(elements) ? elements : [elements]).filter(Boolean);
        this.state = 'REST';
        this.sequenceTimeouts = [];
        this.expireTimeout = null;
        this.isLocked = false; // Verrouillé pendant la séquence d'explosion

        this.spriteSources = {
            REST: '/static/laying-cat-removebg-preview.png',
            WAKE: '/static/eyes-open-cat-removebg-preview.png',
            STAND: '/static/stand-up-cat-removebg-preview.png',
            CLAP: '/static/clapping-cat-removebg-preview.png',
            ANGRY: '/static/angry-cat-removebg-preview.png',
            EXPLODE_1: '/static/first-explosing-cat-removebg-preview.png',
            EXPLODE_2: '/static/seconde-explosing-cat-removebg-preview.png'
        };

        // Rétrocompatibilité avec les anciens alias
        this.spriteSources.TRANSITION = this.spriteSources.WAKE;
        this.spriteSources.JUMP_CLAP = this.spriteSources.CLAP;
        this.spriteSources.OVERHEAT = this.spriteSources.EXPLODE_1;
        this.spriteSources.EXPLOSION = this.spriteSources.EXPLODE_2;

        this.loadedSprites = {};
        this.preloadSprites();
    }

    preloadSprites() {
        Object.entries(this.spriteSources).forEach(([key, src]) => {
            const img = new Image();
            img.src = src;
            img.onload = () => { this.loadedSprites[key] = src; };
        });
    }

    clearSequence() {
        this.sequenceTimeouts.forEach(t => clearTimeout(t));
        this.sequenceTimeouts = [];
        clearTimeout(this.expireTimeout);
        this.expireTimeout = null;
    }

    schedule(fn, delay) {
        const t = setTimeout(fn, delay);
        this.sequenceTimeouts.push(t);
        return t;
    }

    applySprite(stateKey) {
        const src = this.spriteSources[stateKey] || this.spriteSources.REST;
        this.elements.forEach(el => {
            if (el && !el.src.endsWith(src)) {
                el.src = src;
            }
        });
    }

    setState(newState, duration = 0, onExpire = null) {
        clearTimeout(this.expireTimeout);
        this.expireTimeout = null;
        this.state = newState;

        const classMap = {
            REST: 'state-rest',
            WAKE: 'state-wake',
            TRANSITION: 'state-wake',
            STAND: 'state-stand',
            CLAP: 'state-clap',
            JUMP_CLAP: 'state-clap',
            ANGRY: 'state-angry',
            EXPLODE_1: 'state-explode-1',
            OVERHEAT: 'state-explode-1',
            EXPLODE_2: 'state-explode-2',
            EXPLOSION: 'state-explode-2',
            RESPAWN: 'state-respawn',
            HIDDEN: 'state-hidden'
        };

        const targetClass = classMap[newState] || 'state-rest';
        const spriteKey = (newState === 'RESPAWN') ? 'REST' : newState;
        this.applySprite(spriteKey);

        this.elements.forEach(el => {
            if (!el) return;
            const baseClass = el.id === 'landing-cat-img' ? 'landing-cat-img' : 'mascot-cat-img';
            el.className = `${baseClass} ${targetClass}`;
        });

        if (duration > 0) {
            this.expireTimeout = setTimeout(() => {
                if (onExpire) {
                    onExpire();
                } else {
                    this.setState('REST');
                }
            }, duration);
        }
    }

    onFeedEntered() {
        if (this.isLocked) return;
        this.setState('STAND');
    }

    onHomeEntered() {
        if (this.isLocked) return;
        this.setState('REST');
    }

    onCardView() {
        if (this.isLocked) return;
        if (this.state === 'REST') {
            this.setState('WAKE', 3200, () => {
                this.setState('REST');
            });
        }
    }

    onCorrectAnswer(streak = 0) {
        this.clearSequence();
        this.isLocked = false;
        // Enchaînement : Danse et applaudissements victorieux (2200ms)
        this.setState('CLAP', 2200, () => {
            // Si une série est active, le chat reste debout et fier !
            if (streak > 0) {
                this.setState('STAND');
            } else {
                this.setState('REST');
            }
        });
    }

    onWrongAnswer(onImpactCallback) {
        this.clearSequence();
        this.isLocked = true;

        // Phase 1 : Colère rouge vive (300ms)
        this.setState('ANGRY');

        // Phase 2 : Montée en surcharge critique (250ms)
        this.schedule(() => {
            this.setState('EXPLODE_1');
        }, 300);

        // Phase 3 : Flash de détonation (150ms)
        this.schedule(() => {
            this.setState('EXPLODE_2');
        }, 550);

        // Phase 4 : IMPACT MAJEUR ! Le chat DISPARAÎT et EXPLOSE EN SANG ! (700ms)
        this.schedule(() => {
            this.setState('HIDDEN');
            if (onImpactCallback) onImpactCallback();
        }, 700);

        // Phase 5 : Renaissance du chat après que le sang a coulé (4200ms)
        this.schedule(() => {
            this.isLocked = false;
            this.setState('RESPAWN', 800, () => {
                this.setState('REST');
            });
            showCatBubble("Pouf... 😿 Je renais de mes pixels !", 2400);
        }, 4200);
    }

    onPet() {
        if (this.isLocked) return;
        this.clearSequence();
        // Si le chat dormait, il ouvre les yeux puis se réjouit en applaudissant !
        if (this.state === 'REST') {
            this.setState('WAKE');
            this.schedule(() => {
                this.setState('CLAP', 1800, () => {
                    const isFeed = $('feed-screen') && $('feed-screen').classList.contains('visible');
                    this.setState(isFeed ? 'STAND' : 'REST');
                });
            }, 250);
        } else {
            this.setState('CLAP', 1800, () => {
                const isFeed = $('feed-screen') && $('feed-screen').classList.contains('visible');
                this.setState(isFeed ? 'STAND' : 'REST');
            });
        }
    }
}

// ------------------------------------------------------------ MOTEUR PIXEL GORE FX ----
/**
 * Animation d'explosion rétro en Pixel Art avec sang qui gicle et coule le long des bords (Gravity Drop)
 */
class PixelGoreFX {
    constructor(canvas, container) {
        this.canvas = canvas;
        this.container = container;
        this.ctx = canvas ? canvas.getContext('2d') : null;
        this.particles = [];
        this.bloodDrips = [];
        this.shockwaves = [];
        this.animId = null;
        this.init();
    }

    init() {
        if (!this.canvas) return;
        this.resize();
        window.addEventListener('resize', () => this.resize());
    }

    resize() {
        if (!this.canvas || !this.container) return;
        const rect = this.container.getBoundingClientRect();
        this.canvas.width = rect.width;
        this.canvas.height = rect.height;
    }

    explode(originX, originY) {
        this.resize();
        if (!this.ctx) return;
        cancelAnimationFrame(this.animId);

        this.particles = [];
        this.bloodDrips = [];
        this.shockwaves = [];

        const w = this.canvas.width;
        const h = this.canvas.height;

        // Onde de choc géométrique (cercles concentriques pixelisés centrés sur le chat)
        this.shockwaves.push({ x: originX, y: originY, r: 6, maxR: 90, lw: 8, color: '#FF3344', alpha: 1 });
        this.shockwaves.push({ x: originX, y: originY, r: 14, maxR: 140, lw: 5, color: '#FFFFFF', alpha: 0.9 });
        this.shockwaves.push({ x: originX, y: originY, r: 24, maxR: 200, lw: 4, color: '#8B0000', alpha: 0.85 });

        // Palette gore pixel art : sang cramoisi, bordeaux, sang artériel vif
        const bloodColors = ['#8B0000', '#B22222', '#DC143C', '#FF0033', '#660000', '#990000'];
        const furColors = ['#FF8800', '#CC5500', '#FFAA33'];
        const boneColors = ['#FFFFFF', '#FFCCCC'];

        // 160 pixels projetés violemment dans toutes les directions
        const count = 160;
        for (let i = 0; i < count; i++) {
            const angle = Math.random() * Math.PI * 2;
            const speed = 5 + Math.random() * 19;
            const isBlood = Math.random() < 0.75;
            const color = isBlood 
                ? bloodColors[Math.floor(Math.random() * bloodColors.length)]
                : (Math.random() < 0.6 ? furColors[Math.floor(Math.random() * furColors.length)] : boneColors[Math.floor(Math.random() * boneColors.length)]);
            const size = (Math.floor(Math.random() * 3) + 1) * 3; // Tailles rétro : 3px, 6px, 9px

            this.particles.push({
                x: originX,
                y: originY,
                vx: Math.cos(angle) * speed,
                vy: Math.sin(angle) * speed,
                size: size,
                color: color,
                isBlood: isBlood,
                alpha: 1,
                gravity: 0.22,
                stuck: false
            });
        }

        // Screen shake intense sur le viewport
        if (this.container) {
            this.container.classList.add('viewport-screen-shake');
            setTimeout(() => this.container.classList.remove('viewport-screen-shake'), 450);
        }

        this.renderLoop();
    }

    renderLoop() {
        if (!this.ctx) return;
        const w = this.canvas.width;
        const h = this.canvas.height;

        this.ctx.clearRect(0, 0, w, h);

        // A. Ondes de choc géométriques pixelisées
        for (let i = this.shockwaves.length - 1; i >= 0; i--) {
            const sw = this.shockwaves[i];
            sw.r += 7;
            sw.alpha -= 0.035;
            if (sw.alpha <= 0) {
                this.shockwaves.splice(i, 1);
                continue;
            }
            this.ctx.save();
            this.ctx.globalAlpha = Math.max(0, sw.alpha);
            this.ctx.strokeStyle = sw.color;
            this.ctx.lineWidth = sw.lw;
            this.ctx.beginPath();
            this.ctx.arc(sw.x, sw.y, sw.r, 0, Math.PI * 2);
            this.ctx.stroke();
            this.ctx.restore();
        }

        // B. Particules de l'explosion
        for (let i = this.particles.length - 1; i >= 0; i--) {
            const p = this.particles[i];

            if (!p.stuck) {
                p.x += p.vx;
                p.y += p.vy;
                p.vy += p.gravity;

                // Collision violente avec les 4 bords intérieurs de l'écran (Éclaboussures)
                let hitEdge = false;
                let dripX = p.x;
                let dripY = p.y;

                if (p.x <= 12) {
                    p.x = 2 + Math.floor(Math.random() * 6);
                    p.stuck = true;
                    hitEdge = true;
                    dripX = p.x;
                    dripY = p.y;
                } else if (p.x >= w - 16) {
                    p.x = w - 14 - Math.floor(Math.random() * 6);
                    p.stuck = true;
                    hitEdge = true;
                    dripX = p.x;
                    dripY = p.y;
                } else if (p.y <= 14) {
                    p.y = 2 + Math.floor(Math.random() * 6);
                    p.stuck = true;
                    hitEdge = true;
                    dripX = p.x;
                    dripY = p.y;
                } else if (p.y >= h - 16) {
                    p.y = h - 14;
                    p.stuck = true;
                    hitEdge = true;
                    dripX = p.x;
                    dripY = p.y;
                }

                if (hitEdge && p.isBlood) {
                    // Création d'une coulure de sang qui glisse le long du bord (Gravity Drop)
                    this.bloodDrips.push({
                        x: Math.round(dripX / 3) * 3, // Snap sur la grille de pixels
                        y: Math.round(dripY / 3) * 3,
                        size: p.size,
                        length: 0,
                        maxLength: 35 + Math.random() * 110, // Traînée plus longue et visible
                        dripSpeed: 0.8 + Math.random() * 1.8,
                        color: p.color,
                        alpha: 1
                    });
                }
            }

            // Dessin du bloc pixel
            this.ctx.fillStyle = p.color;
            this.ctx.globalAlpha = Math.max(0, p.alpha);
            const px = Math.floor(p.x / 3) * 3;
            const py = Math.floor(p.y / 3) * 3;
            this.ctx.fillRect(px, py, p.size, p.size);

            if (p.stuck) {
                p.alpha -= 0.0035; // Les éclaboussures disparaissent lentement
                if (p.alpha <= 0) this.particles.splice(i, 1);
            }
        }

        // C. Glissement du sang le long des bords (Gravity Drop)
        for (let i = this.bloodDrips.length - 1; i >= 0; i--) {
            const d = this.bloodDrips[i];
            if (d.length < d.maxLength) {
                d.length += d.dripSpeed;
            } else {
                d.alpha -= 0.004;
            }

            this.ctx.fillStyle = d.color;
            this.ctx.globalAlpha = Math.max(0, d.alpha);

            // Traînée verticale de pixels rétro
            const curLen = Math.floor(d.length / 3) * 3;
            this.ctx.fillRect(d.x, d.y, d.size, curLen);

            // Goutte de sang plus épaisse au bas de la coulure
            this.ctx.fillRect(d.x - 1, d.y + curLen, d.size + 2, 4);

            if (d.alpha <= 0) {
                this.bloodDrips.splice(i, 1);
            }
        }

        this.ctx.globalAlpha = 1;

        // Boucle d'animation tant qu'il reste des éléments
        if (this.particles.length > 0 || this.bloodDrips.length > 0 || this.shockwaves.length > 0) {
            this.animId = requestAnimationFrame(() => this.renderLoop());
        } else {
            this.ctx.clearRect(0, 0, w, h);
        }
    }
}

// Initialisation des instances moteurs
const landingCat = $('landing-cat-img');
const landingCatBubble = $('landing-cat-bubble');
const catMascot = new CatMascotEngine([chillCat, landingCat]);
const pixelGore = new PixelGoreFX(goreCanvas, appViewport);

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
    catMascot.onPet();
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
        catMascot.onCorrectAnswer(nextStreak);
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
        showCatBubble(quote, 2200);
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
        title: "Maths Doomscrolling",
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
        showToast("mathsdoomscrolling.pierref.eu");
    }
}

// ------------------------------------------------------------ CHARGEMENT CATÉGORIES ----
async function loadCategories() {
    try {
        const res = await fetch('/api/categories');
        const cats = await res.json();
        catList.innerHTML = '';

        if (!cats || !cats.length) {
            catList.innerHTML = '<div class="loading-state">Aucun module pour le moment.</div>';
            return;
        }

        cats.forEach((cat, index) => {
            const card = document.createElement('div');
            card.className = 'category-card';

            const numStr = String(index + 1).padStart(2, '0');
            const totalCount = cat.n || 0;

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

            // Option 1 : Tout le module
            const allSubBtn = document.createElement('button');
            allSubBtn.className = 'subcat-btn';
            allSubBtn.innerHTML = `<span>→ Tout le module</span> <span class="subcat-count">${totalCount} cartes</span>`;
            allSubBtn.onclick = (e) => {
                e.stopPropagation();
                launchFeed(cat.id, null);
            };
            subDropdown.appendChild(allSubBtn);

            // Sous-catégories individuelles
            if (cat.subcategories && cat.subcategories.length) {
                cat.subcategories.forEach(sub => {
                    const subBtn = document.createElement('button');
                    subBtn.className = 'subcat-btn';
                    subBtn.innerHTML = `<span>→ ${esc(sub.name)}</span> <span class="subcat-count">${sub.n} cartes</span>`;
                    subBtn.onclick = (e) => {
                        e.stopPropagation();
                        launchFeed(cat.id, sub.id);
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
            catList.appendChild(card);
        });
    } catch (e) {
        catList.innerHTML = '<div class="loading-state">Erreur de connexion au serveur.</div>';
    }
}

// ------------------------------------------------------------ NAVIGATION ----
function launchFeed(catId, subId) {
    session++;
    isFetching = false;
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
    feed.focus();
}

function goHome() {
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
    if (!s) return;
    if (streakVal) streakVal.textContent = s.streak;
    if (levelVal) levelVal.textContent = s.level;
}

async function fetchUserState() {
    try {
        const res = await fetch('/api/user_state');
        renderState(await res.json());
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
async function loadCards() {
    if (isFetching) return;
    isFetching = true;
    const mine = session;

    try {
        const qs = new URLSearchParams();
        if (currentCat) qs.set('cat', currentCat);
        if (currentSub) qs.set('sub', currentSub);
        if (seenIds.size) qs.set('exclude', [...seenIds].slice(-300).join(','));

        const res = await fetch('/api/cards?' + qs);
        if (!res.ok) throw new Error(res.status);
        const cards = await res.json();
        if (mine !== session) return;

        if (!cards.length && !feed.children.length) {
            feed.innerHTML = `
                <div class="card">
                    <div class="card-body" style="text-align: center;">
                        <div class="card-front">AUCUNE CARTE DISPONIBLE</div>
                        <div class="card-back" style="display:block">Ajoute des cartes via l'interface /admin.</div>
                    </div>
                </div>
            `;
            return;
        }

        cards.forEach(c => {
            seenIds.add(c.id);
            const card = buildCard(c, ++uidCounter);
            feed.appendChild(card);
            renderMath(card);
            observer.observe(card);
        });
    } catch (e) {
        console.error('loadCards error:', e);
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
        </div>

        <div class="card-body">
            <div class="card-front">${formatMathMarkdown(c.front)}</div>
    `;

    if (c.type === 'QCM') {
        const choices = shuffle([...(c.payload?.choices || [])]);
        html += '<div class="qcm-choices">' +
            choices.map(ch => `<button class="choice-btn" data-correct="${ch.correct}">${formatMathMarkdown(ch.text)}</button>`).join('') +
            '</div>';
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
        card.querySelectorAll('.choice-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.stopPropagation();
                if (card.classList.contains('answered')) return;
                card.classList.add('answered', 'revealed');

                const ok = btn.dataset.correct === 'true';
                btn.classList.add(ok ? 'correct' : 'wrong');

                if (!ok) {
                    card.querySelectorAll('.choice-btn').forEach(b => {
                        if (b.dataset.correct === 'true') b.classList.add('correct');
                    });
                }
                card.querySelectorAll('.choice-btn').forEach(b => b.disabled = true);
                answer(card, c.id, ok);
            });
        });
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
        } else if (e.key === 'l' || e.key === 'L') {
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
});

// INITIALISATION
loadCategories();
fetchUserState();
