// Adaptive scroll on a level path: the server picks each card (scroll.py), this file shows it
// with the same card markup as the main feed (static/app.js buildCard, styles in style.css).
(function () {
  const $ = (id) => document.getElementById(id);
  const root = $('feed-screen');
  const feed = $('feed');
  const api = `/api/scroll/${root.dataset.subject}`;

  const cat = new CatMascotEngine([$('chill-cat')]);
  const gore = new PixelGoreFX($('gore-canvas'), $('gore-canvas'));
  cat.startIdleLife();
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
    const body = el('div', 'card-body');
    card.append(badge, body);
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
      feed.append(card);
      return;
    } finally { loading = false; }
    setProgress(data.progress);
    const card = data.card.kind === 'c' ? courseCard(data.card) : quizCard(data.card);
    feed.append(card);
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
      cat.onCorrectAnswer(1);
      showCatBubble('Bien joué !');
    } else {
      const rect = $('chill-cat').getBoundingClientRect();
      cat.onWrongAnswer(() => gore.explode(rect.left + rect.width / 2, rect.top + rect.height / 2));
      if (navigator.vibrate) navigator.vibrate([150, 50, 200]);
    }
    setTimeout(next, d.ok ? 500 : 900);
  }

  window.addEventListener('load', next);
})();
