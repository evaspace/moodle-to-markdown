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

        // Phase 5 : Renaissance rapide (le sang continue de couler derrière)
        this.schedule(() => {
            this.isLocked = false;
            this.setState('RESPAWN', 650, () => {
                this.setState('REST');
            });
            if (typeof showCatBubble === 'function') showCatBubble("Pouf... 😿 Je renais de mes pixels !", 1800);
        }, 1500);
    }

    // "Il fait sa vie" : toutes les 4 à 9 s, le chat au repos change de posture.
    startIdleLife() {
        const LIFE = ['REST', 'REST', 'WAKE', 'STAND'];
        const tick = () => {
            if (!this.isLocked && ['REST', 'WAKE', 'STAND'].includes(this.state)) {
                this.setState(LIFE[Math.floor(Math.random() * LIFE.length)]);
            }
            setTimeout(tick, 4000 + Math.random() * 5000);
        };
        setTimeout(tick, 4000);
    }

    onPet() {
        if (this.isLocked) return;
        this.clearSequence();
        // Si le chat dormait, il ouvre les yeux puis se réjouit en applaudissant !
        if (this.state === 'REST') {
            this.setState('WAKE');
            this.schedule(() => {
                this.setState('CLAP', 1800, () => {
                    const isFeed = document.getElementById('feed-screen') && document.getElementById('feed-screen').classList.contains('visible');
                    this.setState(isFeed ? 'STAND' : 'REST');
                });
            }, 250);
        } else {
            this.setState('CLAP', 1800, () => {
                const isFeed = document.getElementById('feed-screen') && document.getElementById('feed-screen').classList.contains('visible');
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

