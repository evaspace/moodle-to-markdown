// Adaptive scroll on a level path: the server picks each card (scroll.py), this file shows it
// with the same card markup as the main feed (static/app.js buildCard, styles in style.css).
(function () {
  const $ = (id) => document.getElementById(id);
  const root = $('feed-screen');
  const feed = $('feed');
  const foot = feed.querySelector('.morgan-footer');  // footer stays last in the feed
  // shortcut: temporary trace of the Android true/false tap bug (2026-11-17); remove once fixed
  const trace = (msg) => { try { navigator.sendBeacon('/api/client-log', msg); } catch (e) { /* no beacon */ } };
  addEventListener('error', (e) => trace(`error ${e.message} @${e.filename}:${e.lineno}`));
  addEventListener('unhandledrejection', (e) => trace(`rejection ${e.reason}`));
  const api = `/api/scroll/${root.dataset.subject}`;

  const cat = new CatMascotEngine([$('chill-cat')]);
  const gore = new PixelGoreFX($('gore-canvas'), $('gore-canvas'));
  cat.startIdleLife();
  cat.enter();
  cat.onBoom = () => {  // 10 caresses trop rapides
    const r = $('chill-cat').getBoundingClientRect();
    cat.onWrongAnswer(() => gore.explode(r.left + r.width / 2, r.top + r.height / 2));
  };
  let bubbleTimer = null;
  window.showCatBubble = (text, ms = 1800) => {
    const b = $('cat-bubble');
    clearTimeout(bubbleTimer);
    b.textContent = text;
    b.classList.remove('hidden');
    bubbleTimer = setTimeout(() => b.classList.add('hidden'), ms);
  };
  $('chill-cat').onclick = () => cat.onPet();

  const renderMath = (el) => {
    if (window.renderMathInElement) {
      renderMathInElement(el, { delimiters: [{ left: '$$', right: '$$', display: true }, { left: '$', right: '$', display: false }], throwOnError: false });
    }
  };
  const el = (tag, cls, html) => {
    const e = document.createElement(tag);
    if (cls) e.className = cls;
    if (html !== undefined) e.innerHTML = html; // server-rendered, bleach-cleaned Markdown
    return e;
  };
  const setProgress = (p) => { $('sc-progress').textContent = `Notion ${p.unlocked}/${p.total} : ${p.notion}`; };

  // Card shell identical to the main feed: badge, then .card-body with .card-front.
  function shell(tag, notion) {
    const card = el('div', 'card');
    const badge = el('div', 'card-header-badge');
    badge.append(el('span', 'card-type-tag'), el('span', 'card-subcat-tag'));
    badge.children[0].textContent = `[ ${tag} ]`;
    badge.children[1].textContent = notion || '';
    const bar = el('div', 'card-action-bar');
    const ia = el('button', 'action-btn ia-btn', 'IA');
    ia.type = 'button';
    ia.title = 'Copier pour une IA';
    ia.setAttribute('aria-label', 'Copier la carte pour une IA');
    ia.onclick = () => copyCardForLLM(card, ia, `${document.title.replace('Scroll · ', '')} : ${notion || tag}`);
    bar.append(ia);
    const body = el('div', 'card-body');
    card.append(badge, bar, body);
    return [card, body];
  }

  let loading = false;
  async function next() {
    if (loading) return;
    loading = true;
    let data;
    try {
      const r = await fetch(api + '/next');
      if (r.status === 401) { location.href = '/compte?next=' + location.pathname; return; }
      data = await r.json();
    } catch (e) {
      const [card, body] = shell('ERREUR', '');
      body.append(el('div', 'card-front', 'Erreur réseau : recharge la page.'));
      feed.insertBefore(card, foot);
      return;
    } finally { loading = false; }
    setProgress(data.progress);
    const card = data.card.kind === 'c' ? courseCard(data.card) : quizCard(data.card);
    feed.insertBefore(card, foot);
    renderMath(card);
    feed.scrollTo({ top: card.offsetTop, behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' });
    const first = card.querySelector('button');
    if (first) first.focus({ preventScroll: true });
  }

  function courseCard(c) {
    const [card, body] = shell('COURS', c.titre);
    body.append(el('div', 'card-front', `${c.titre}<div class="formule">${c.formule}</div>`));
    const reveal = el('button', 'reveal-btn', 'VOIR LE COURS 💡');
    reveal.type = 'button';
    reveal.onclick = () => { card.classList.toggle('revealed'); renderMath(card); };
    const back = el('div', 'card-back', `${c.exemple}<hr>${c.cours}`);
    const go = el('button', 'choice-btn', 'Compris, suivant');
    go.type = 'button';
    go.onclick = () => { go.disabled = true; next(); };
    body.append(reveal, back, go);
    return card;
  }

  function quizCard(q) {
    const [card, body] = shell(q.type === 'qcm' ? 'QCM' : 'VRAI / FAUX', q.notion_titre);
    body.append(el('div', 'card-front', q.q));
    if (q.type === 'vf') return tfCard(q, card, body);
    const choices = el('div', 'qcm-choices');
    const buttons = q.choix.map((html, i) => {
      const b = el('button', 'choice-btn', html);
      b.type = 'button';
      b.onclick = () => answer(q, i, buttons, card, body);
      return b;
    });
    choices.append(...buttons);
    body.append(choices);
    return card;
  }

  // True/false: same markup and gesture as the main feed (static/app.js): swipe right = vrai, left = faux.
  // Server choices for vf: 0 = Vrai, 1 = Faux.
  function tfCard(q, card, body) {
    const actions = el('div', 'tf-actions');
    const vrai = el('button', 'tf-btn btn-vrai', '✓ VRAI');
    const faux = el('button', 'tf-btn btn-faux', '✕ FAUX');
    vrai.type = faux.type = 'button';
    actions.append(faux, vrai);
    const indL = el('div', 'tf-indicator tf-left', 'FAUX');
    const indR = el('div', 'tf-indicator tf-right', 'VRAI');
    body.append(actions, indL, indR, el('div', 'tf-swipe-hint', '← SWIPE GAUCHE FAUX · SWIPE DROITE VRAI →'));
    const buttons = [vrai, faux];
    let locked = false, startX = 0, startY = 0, gesture = null;
    const resetInd = () => { indL.style.opacity = indR.style.opacity = 0; };
    const pick = (choice) => {
      if (locked) return;
      locked = true;
      const right = choice === 0;
      card.style.transition = 'transform 0.22s ease-in, opacity 0.22s';
      card.style.transform = `translateX(${right ? 120 : -120}%) rotate(${right ? 20 : -20}deg)`;
      card.style.opacity = '0';
      setTimeout(() => { card.style.transition = 'none'; card.style.transform = ''; card.style.opacity = ''; resetInd(); }, 240);
      answer(q, choice, buttons, card, body);
    };
    vrai.onclick = () => pick(0);
    faux.onclick = () => pick(1);
    const seq = [];
    const note = (e) => {
      const pt = e.changedTouches ? e.changedTouches[0] : e;
      const t = pt && Number.isFinite(pt.clientX) ? document.elementFromPoint(pt.clientX, pt.clientY) : null;
      seq.push(`${e.type}:${e.target.className || e.target.tagName}${t ? `@${Math.round(pt.clientX)},${Math.round(pt.clientY)}` : ''}${t && t !== e.target ? `>top:${t.className || t.tagName}` : ''}`);
      if (e.type === 'click' || e.type === 'pointercancel' || seq.length > 12) { trace(`tf ${innerWidth}x${innerHeight} locked=${locked} ` + seq.join(' ')); seq.length = 0; }
    };
    for (const t of ['pointerdown', 'pointerup', 'pointercancel', 'click', 'touchstart', 'touchend']) card.addEventListener(t, note, { capture: true, passive: true });
    // Pointer events: finger on a phone, mouse drag on a computer.
    card.addEventListener('pointerdown', (e) => {
      if (locked || e.target.closest('button')) return;
      startX = e.clientX; startY = e.clientY; gesture = null;
    });
    card.addEventListener('pointermove', (e) => {
      if (locked || gesture === 'v' || (e.pointerType === 'mouse' && !e.buttons)) return;
      const dX = e.clientX - startX, dY = e.clientY - startY;
      if (!gesture) {
        if (Math.abs(dX) < 8 && Math.abs(dY) < 8) return;
        gesture = Math.abs(dX) > Math.abs(dY) ? 'h' : 'v';
        if (gesture === 'v') return;
        card.style.transition = 'none';
        card.setPointerCapture(e.pointerId);
      }
      card.style.transform = `translateX(${dX}px) rotate(${dX * 0.03}deg)`;
      indR.style.opacity = dX > 0 ? Math.min(dX / 120, 1) : 0;
      indL.style.opacity = dX < 0 ? Math.min(-dX / 120, 1) : 0;
    });
    const end = (e) => {
      if (locked || gesture !== 'h') { gesture = null; return; }
      gesture = null;
      const dX = e.clientX - startX, threshold = Math.min(90, innerWidth * 0.22);
      if (dX > threshold) pick(0);
      else if (dX < -threshold) pick(1);
      else { card.style.transition = 'transform 0.25s ease-out'; card.style.transform = ''; resetInd(); }
    };
    card.addEventListener('pointerup', end);
    card.addEventListener('pointercancel', end);
    card.style.touchAction = 'pan-y';  // vertical scroll stays native, horizontal drags are ours
    return card;
  }

  async function answer(q, choice, buttons, card, body) {
    buttons.forEach((b) => { b.disabled = true; });
    const r = await fetch(api + '/answer', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ key: q.key, choice }) });
    if (!r.ok) { buttons.forEach((b) => { b.disabled = false; }); return; }
    const d = await r.json();
    buttons[d.bonne].classList.add('correct');
    if (!d.ok) buttons[choice].classList.add('wrong');
    card.classList.add('answered', d.ok ? 'answered-ok' : 'answered-ko');
    setProgress(d.progress);
    if (!d.ok) {
      body.append(el('div', 'card-back', 'Faux : la carte de cours arrive.'));
      card.classList.add('revealed');
    }
    if (d.ok) {
      cat.onCorrectAnswer(1, 'Bien joué !');
      pixelConfetti($('gore-canvas'), 2);
    } else {
      const rect = $('chill-cat').getBoundingClientRect();
      cat.onWrongAnswer(() => gore.explode(rect.left + rect.width / 2, rect.top + rect.height / 2));
      if (navigator.vibrate) navigator.vibrate([150, 50, 200]);
    }
    setTimeout(next, d.ok ? 500 : 900);
  }

  window.addEventListener('load', next);
})();
