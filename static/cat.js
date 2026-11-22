// Cat mascot + pixel gore, shared by the feed (app.js) and the levels pages (niveaux.js).
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
        this.wrongRow = 0;     // mauvaises réponses d'affilée (3 = chat carbonisé)
        this.pets = [];        // instants des dernières caresses (spam = chat agacé)
        this.views = [];       // instants des dernières cartes vues (doomscroll trop rapide)
        this.lastPointer = 0;
        this.onBoom = null;    // fourni par la page : explosion quand on caresse 10 fois trop vite
        this.calm = typeof matchMedia === 'function' && matchMedia('(prefers-reduced-motion: reduce)').matches;

        this.spriteSources = {
            REST: '/static/laying-cat-removebg-preview.png',
            WAKE: '/static/eyes-open-cat-removebg-preview.png',
            STAND: '/static/stand-up-cat-removebg-preview.png',
            CLAP: '/static/clapping-cat-removebg-preview.png',
            ANGRY: '/static/angry-cat-removebg-preview.png',
            EXPLODE_1: '/static/first-explosing-cat-removebg-preview.png',
            EXPLODE_2: '/static/seconde-explosing-cat-removebg-preview.png?v=2'
        };

        // Rétrocompatibilité avec les anciens alias
        this.spriteSources.TRANSITION = this.spriteSources.WAKE;
        this.spriteSources.JUMP_CLAP = this.spriteSources.CLAP;
        this.spriteSources.OVERHEAT = this.spriteSources.EXPLODE_1;
        this.spriteSources.EXPLOSION = this.spriteSources.EXPLODE_2;
        // Nouveaux états : mêmes sprites, autre animation CSS
        this.spriteSources.SLEEP = this.spriteSources.REST;
        this.spriteSources.STARTLE = this.spriteSources.WAKE;
        this.spriteSources.TILT = this.spriteSources.WAKE;
        this.spriteSources.NERVOUS = this.spriteSources.WAKE;
        this.spriteSources.DIZZY = this.spriteSources.WAKE;
        this.spriteSources.DANGLE = this.spriteSources.WAKE;
        this.spriteSources.ENTER = this.spriteSources.STAND;
        this.spriteSources.GRUMPY = this.spriteSources.ANGRY;

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

    say(text, ms) {
        if (typeof window.showCatBubble === 'function') window.showCatBubble(text, ms);
    }

    // Cadre (retournement, carbonisé) et conteneur fixe (glisser, Zzz) des chats en bas d'écran.
    frames() { return this.elements.map(el => el.closest('.mascot-frame')).filter(Boolean); }
    wraps() { return this.elements.map(el => el.closest('.bottom-cat-wrap')).filter(Boolean); }

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
            HIDDEN: 'state-hidden',
            SLEEP: 'state-sleep',
            STARTLE: 'state-startle',
            TILT: 'state-tilt',
            NERVOUS: 'state-nervous',
            DIZZY: 'state-dizzy',
            DANGLE: 'state-dangle',
            ENTER: 'state-enter',
            GRUMPY: 'state-grumpy'
        };

        const targetClass = classMap[newState] || 'state-rest';
        const spriteKey = (newState === 'RESPAWN') ? 'REST' : newState;
        this.applySprite(spriteKey);

        this.elements.forEach(el => {
            if (!el) return;
            const baseClass = el.id === 'landing-cat-img' ? 'landing-cat-img' : 'mascot-cat-img';
            el.className = `${baseClass} ${targetClass}`;
        });
        this.wraps().forEach(w => w.classList.toggle('cat-zzz', newState === 'SLEEP'));

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

    isIdle() { return !this.isLocked && ['REST', 'WAKE', 'STAND', 'SLEEP'].includes(this.state); }

    // Arrivée sur la page : le chat saute depuis le bas de l'écran.
    enter(then = 'REST') {
        if (this.isLocked) return;
        this.setState('ENTER', 700, () => this.setState(then));
    }

    onFeedEntered() {
        if (this.isLocked) return;
        this.enter('STAND');
    }

    onHomeEntered() {
        if (this.isLocked) return;
        this.setState('REST');
    }

    onCardView() {
        if (this.isLocked) return;
        // Doomscroll trop rapide : 4 cartes en moins de 2 s, le chat a le tournis.
        const now = Date.now();
        this.views = this.views.filter(t => now - t < 2000).concat(now);
        if (this.views.length >= 4 && this.state !== 'DIZZY') {
            this.views = [];
            this.setState('DIZZY', 1600, () => this.setState('STAND'));
            this.say('Ralentis, j\'ai le tournis !', 1600);
            return;
        }
        if (this.state === 'REST' || this.state === 'SLEEP') {
            this.setState('WAKE', 3200, () => {
                this.setState('REST');
            });
        }
    }

    // Mème « happy happy happy » : sauts verticaux secs, un « happy » de plus à chaque saut.
    // level (série en cours) monte la hauteur des sauts ; final = bulle affichée après les sauts.
    happy(hops = 4, level = 0, final = '', then = 'REST', words = true) {
        this.clearSequence();
        this.isLocked = false;
        this.unburn();
        const beat = 380; // = durée de @keyframes happyHop
        this.elements.forEach(el => el.style.setProperty('--hop', `${26 + Math.min(level, 10) * 3}px`));
        this.setState('CLAP');
        for (let i = 0; words && i < hops; i++) {
            const words = Array(Math.min(i + 1, 4)).fill('happy').join(' ');
            this.schedule(() => this.say(words[0].toUpperCase() + words.slice(1), beat + 250), i * beat);
        }
        this.schedule(() => {
            if (final) this.say(final, 2000);
            this.setState(then);
        }, hops * beat);
    }

    onCorrectAnswer(streak = 0, final = '') {
        this.happy(streak >= 5 ? 6 : 4, streak, final, streak > 0 ? 'STAND' : 'REST');
    }

    unburn() {
        this.wrongRow = 0;
        clearTimeout(this.burntTimer);
        this.frames().forEach(f => f.classList.remove('cat-burnt'));
    }

    onWrongAnswer(onImpactCallback) {
        this.clearSequence();
        this.isLocked = true;
        this.wrongRow += 1;

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

        // Phase 5 : Renaissance rapide (le sang continue de couler derrière)
        this.schedule(() => {
            this.isLocked = false;
            this.setState('RESPAWN', 650, () => {
                this.setState('REST');
            });
            if (this.wrongRow >= 3) {
                // 3 ratés d'affilée : il revient carbonisé quelques secondes
                this.frames().forEach(f => f.classList.add('cat-burnt'));
                clearTimeout(this.burntTimer);
                this.burntTimer = setTimeout(() => this.frames().forEach(f => f.classList.remove('cat-burnt')), 6000);
                this.say('Je suis cuit... 3 ratés d\'affilée', 2200);
            } else {
                this.say("Pouf... 😿 Je renais de mes pixels !", 1800);
            }
        }, 1500);
    }

    // Page d'exercice sur papier : à mi-chrono il penche la tête, à 30 s il stresse.
    ponder() {
        if (!this.isIdle()) return;
        this.setState('TILT', 2600, () => this.setState('STAND'));
        this.say('Hmm ?', 1800);
    }

    nervous() {
        if (this.isLocked) return;
        this.clearSequence();
        this.setState('NERVOUS');
        this.say('Plus que 30 s !', 2200);
    }

    relax() {
        if (['NERVOUS', 'TILT'].includes(this.state)) this.setState('STAND');
    }

    // "Il fait sa vie" : postures au hasard, sommeil quand on ne touche à rien, regard vers le
    // pointeur, et on peut le traîner à la souris ou au doigt.
    startIdleLife() {
        const late = () => new Date().getHours() < 5;
        const tick = () => {
            if (!this.isLocked && ['REST', 'WAKE', 'STAND'].includes(this.state)) {
                const life = late() ? ['SLEEP', 'SLEEP', 'REST', 'WAKE'] : ['REST', 'REST', 'WAKE', 'STAND'];
                this.setState(life[Math.floor(Math.random() * life.length)]);
                // sans pointeur (téléphone), il regarde parfois de l'autre côté
                if (Date.now() - this.lastPointer > 8000 && Math.random() < 0.3) {
                    this.frames().forEach(f => f.classList.toggle('cat-flip'));
                }
            }
            setTimeout(tick, 4000 + Math.random() * 5000);
        };
        setTimeout(tick, 4000);
        if (late()) setTimeout(() => { if (this.isIdle()) this.say('Il est tard... va dormir 😴', 2600); }, 15000);
        this.watchSleep(late);
        this.followPointer();
        this.wraps().forEach(w => this.enableDrag(w));
    }

    // 30 s sans rien toucher (10 s la nuit) : il s'endort, Zzz. Le moindre geste le réveille en sursaut.
    watchSleep(late) {
        let last = Date.now();
        const wake = () => {
            last = Date.now();
            if (this.state === 'SLEEP' && !this.isLocked) {
                this.setState('STARTLE', 600, () => this.setState('REST'));
            }
        };
        ['pointerdown', 'pointermove', 'keydown', 'wheel', 'touchstart'].forEach(ev =>
            window.addEventListener(ev, wake, { passive: true }));
        window.addEventListener('scroll', wake, { passive: true, capture: true });
        setInterval(() => {
            const idleFor = late() ? 10000 : 30000;
            if (Date.now() - last > idleFor && !this.isLocked && ['REST', 'WAKE', 'STAND'].includes(this.state)) {
                this.setState('SLEEP');
            }
        }, 2000);
    }

    // Le sprite regarde à gauche ; il se retourne quand le pointeur passe à sa droite.
    followPointer() {
        let queued = false;
        window.addEventListener('pointermove', e => {
            this.lastPointer = Date.now();
            if (queued || e.pointerType === 'touch') return;
            queued = true;
            requestAnimationFrame(() => {
                queued = false;
                this.frames().forEach(f => {
                    const r = f.getBoundingClientRect();
                    f.classList.toggle('cat-flip', e.clientX > r.left + r.width / 2 + 10);
                });
            });
        }, { passive: true });
    }

    // Glisser le chat : il pendouille en se balançant, puis retombe à sa place en rebondissant.
    enableDrag(wrap) {
        const img = this.elements.find(el => wrap.contains(el));
        if (!img) return;
        img.style.touchAction = 'none';
        img.addEventListener('dragstart', e => e.preventDefault());  // sinon le glisser d'image natif annule le geste
        let start = null, moved = false, dragged = false;
        img.addEventListener('pointerdown', e => {
            if (this.isLocked) return;
            e.preventDefault();
            start = { x: e.clientX, y: e.clientY };
            moved = false;
            dragged = false;
            img.setPointerCapture(e.pointerId);
        });
        img.addEventListener('pointermove', e => {
            if (!start) return;
            const dx = e.clientX - start.x, dy = e.clientY - start.y;
            if (!moved && Math.hypot(dx, dy) < 6) return;
            if (!moved) {
                moved = true;
                this.clearSequence();
                this.setState('DANGLE');
                this.say('Lâche-moi !', 1500);
            }
            wrap.style.transition = 'none';
            wrap.style.transform = `translate(${dx}px, ${dy}px)`;
        });
        const drop = () => {
            if (!start) return;
            start = null;
            if (!moved) return;
            dragged = true; // le clic qui suit le lâcher n'est pas une caresse
            wrap.style.transition = this.calm ? 'none' : 'transform .55s cubic-bezier(.34, 1.56, .64, 1)';
            wrap.style.transform = '';
            this.setState('STARTLE', 600, () => this.setState('REST'));
        };
        img.addEventListener('pointerup', drop);
        img.addEventListener('pointercancel', drop);
        img.closest('.mascot-frame').addEventListener('click', e => {
            if (!dragged) return;
            dragged = false;
            e.stopPropagation();
            e.preventDefault();
        }, true);
    }

    // Caresse. Retourne false quand le chat a déjà réagi lui-même (agacé ou explosé) :
    // la page ne doit alors pas ajouter sa propre bulle.
    onPet() {
        if (this.isLocked) return false;
        const now = Date.now();
        this.pets = this.pets.filter(t => now - t < 4000).concat(now);
        if (this.pets.length >= 10 && this.onBoom) {
            this.pets = [];
            this.say('Tu l\'as cherché.', 1200);
            this.onBoom();
            return false;
        }
        if (this.pets.length >= 5) {
            this.clearSequence();
            this.setState('GRUMPY', 900, () => this.setState('REST'));
            this.say(this.pets.length >= 8 ? 'Encore un et j\'explose !' : 'Stop ! Ça suffit !', 1400);
            return false;
        }
        const isFeed = document.getElementById('feed-screen') && document.getElementById('feed-screen').classList.contains('visible');
        this.happy(2, 0, '', isFeed ? 'STAND' : 'REST', false);  // muet : la page a sa propre phrase de caresse
        return true;
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

// Pixel-art confetti thrown everywhere, on the gore canvas (idle on a success). Used by levels and scroll.
function pixelConfetti(canvas, bursts) {
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const ctx = canvas.getContext('2d'), w = canvas.width = innerWidth, h = canvas.height = innerHeight;
  const colors = ['#FF5555', '#2ECC71', '#FFD23F', '#3A86FF', '#FFFFFF', '#111111'];
  const bits = [];
  for (let b = 0; b < bursts; b++) {
    const ox = Math.random() * w, oy = h * (0.2 + Math.random() * 0.6);
    for (let i = 0; i < 90; i++) {
      const angle = Math.random() * Math.PI * 2, speed = 4 + Math.random() * 16;
      bits.push({ x: ox, y: oy, vx: Math.cos(angle) * speed, vy: Math.sin(angle) * speed - 6, delay: b * 12,
        size: (1 + Math.floor(Math.random() * 3)) * 4, wide: Math.random() < 0.5, color: colors[i % colors.length] });
    }
  }
  (function frame() {
    ctx.clearRect(0, 0, w, h);
    let alive = false;
    for (const c of bits) {
      if (c.delay-- > 0) { alive = true; continue; }
      c.vy += 0.25; c.vx *= 0.985; c.x += c.vx; c.y += c.vy;
      if (c.y > h + 12) continue;
      alive = true;
      // snapped to a 4 px grid: hard pixels, no rotation or blur
      ctx.fillStyle = c.color;
      ctx.fillRect(Math.round(c.x / 4) * 4, Math.round(c.y / 4) * 4, c.wide ? c.size * 2 : c.size, c.size);
    }
    if (alive) requestAnimationFrame(frame); else ctx.clearRect(0, 0, w, h);
  })();
}
window.pixelConfetti = pixelConfetti;
