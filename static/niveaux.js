// Niveaux mode: account form, and the exercise page (formulas, correction, self-assessed result).
(function () {
  const $ = (id) => document.getElementById(id);

  async function post(url, body) {
    const r = await fetch(url, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body || {}) });
    let data = {};
    try { data = await r.json(); } catch (e) { /* empty body */ }
    return { ok: r.ok, data };
  }

  // ---- forced break (beta option, /admin/beta): full screen, cannot be closed before the end
  let breakTimer = null;
  function forcedBreak(st) {
    if (!st || !st.on || !st.force || breakTimer) return;
    const box = document.createElement('div');
    box.className = 'lv-break'; box.setAttribute('role', 'alertdialog'); box.setAttribute('aria-label', 'Pause forcée');
    box.innerHTML = '<strong></strong><h2></h2><p></p>';
    box.querySelector('h2').textContent = st.longue ? 'Grande pause' : 'Pause';
    box.querySelector('p').textContent = `${st.travaille} min de travail d'affilée (${st.source}). Lève-toi, bois de l'eau, regarde loin, pas d'écran. Les réponses reprennent à la fin du compte.`;
    document.body.appendChild(box);
    const end = Date.now() + st.restant * 1000;
    const tick = () => {
      const s = Math.max(0, Math.round((end - Date.now()) / 1000));
      box.querySelector('strong').textContent = `${Math.floor(s / 60)}:${String(s % 60).padStart(2, '0')}`;
      if (!s) { clearInterval(breakTimer); breakTimer = null; box.remove(); }
    };
    tick(); breakTimer = setInterval(tick, 1000);
  }
  const checkBreak = () => fetch('/api/pause').then(r => r.ok ? r.json() : null).then(forcedBreak).catch(() => {});

  // ---- account page
  const form = $('account-form');
  if (form) {
    let mode = 'login';
    const setMode = (m) => {
      mode = m;
      $('tab-login').setAttribute('aria-selected', m === 'login');
      $('tab-register').setAttribute('aria-selected', m === 'register');
      $('email-field').hidden = m !== 'register';
      form.password.autocomplete = m === 'login' ? 'current-password' : 'new-password';
      $('submit').textContent = m === 'login' ? 'Se connecter' : 'Créer le compte';
      $('form-error').textContent = '';
    };
    $('tab-login').onclick = () => setMode('login');
    $('tab-register').onclick = () => setMode('register');
    form.onsubmit = async (e) => {
      e.preventDefault();
      $('submit').disabled = true;
      const res = await post('/api/' + mode, { username: form.username.value, password: form.password.value, email: form.email.value });
      $('submit').disabled = false;
      if (!res.ok) { $('form-error').textContent = res.data.error || 'Erreur, réessaie'; return; }
      const next = new URLSearchParams(location.search).get('next');
      location.href = next && next.startsWith('/') && !next.startsWith('//') ? next : '/niveaux';
    };
  }
  const forgot = $('forgot-form');
  if (forgot) forgot.onsubmit = async (e) => {
    e.preventDefault();
    const res = await post('/api/reset/request', { who: forgot.who.value });
    $('forgot-msg').textContent = res.data.message || res.data.error || 'Erreur, réessaie';
  };
  const reset = $('reset-form');
  if (reset) reset.onsubmit = async (e) => {
    e.preventDefault();
    const res = await post('/api/reset/confirm', { token: reset.dataset.token, password: reset.password.value });
    if (!res.ok) { $('reset-error').textContent = res.data.error || 'Erreur, réessaie'; return; }
    location.href = '/niveaux';
  };
  const emailForm = $('email-form');
  if (emailForm) emailForm.onsubmit = async (e) => {
    e.preventDefault();
    const res = await post('/api/email', { email: emailForm.email.value });
    $('email-msg').textContent = res.ok ? 'E-mail enregistré' : (res.data.error || 'Erreur, réessaie');
  };
  const board = $('board-visible');
  if (board) board.onchange = async () => {
    const res = await post('/api/classement', { visible: board.checked });
    if (!res.ok) board.checked = !board.checked;
    else if (board.dataset.reload) return location.reload();
    $('board-msg').textContent = !res.ok ? 'Erreur, réessaie'
      : board.checked ? 'Tu apparais dans le classement' : "Tu n'apparais plus dans le classement";
  };
  document.querySelectorAll('[data-find]').forEach(btn => btn.onclick = () => {
    const me = document.querySelector(`#${btn.dataset.find} .me`);
    if (!me) return;
    const calm = matchMedia('(prefers-reduced-motion: reduce)').matches;
    me.scrollIntoView({ block: 'center', behavior: calm ? 'auto' : 'smooth' });
    me.focus({ preventScroll: true });
    me.classList.remove('cl-flash'); void me.offsetWidth; me.classList.add('cl-flash');
  });
  const logout = $('logout');
  if (logout) logout.onclick = async () => { await post('/api/logout'); location.href = '/compte'; };

  // ---- exercise page
  if (!$('exo')) return;

  const renderMath = (el) => {
    if (window.renderMathInElement) {
      renderMathInElement(el, { delimiters: [{ left: '$$', right: '$$', display: true }, { left: '$', right: '$', display: false }], throwOnError: false });
    }
  };
  window.addEventListener('load', () => renderMath(document.body));

  // Cat, gore canvas and combo live outside #exo: created once, kept across exercises.
  const cat = new CatMascotEngine([$('chill-cat')]);
  const gore = new PixelGoreFX($('gore-canvas'), $('gore-canvas'));
  cat.startIdleLife();
  cat.enter();
  const boom = () => {
    const r = $('chill-cat').getBoundingClientRect();
    cat.onWrongAnswer(() => gore.explode(r.left + r.width / 2, r.top + r.height / 2));
  };
  cat.onBoom = boom;  // 10 caresses trop rapides
  let bubbleTimer = null;
  window.showCatBubble = (text, ms = 2000) => {
    const b = $('cat-bubble');
    clearTimeout(bubbleTimer);
    b.textContent = text;
    b.classList.remove('hidden');
    bubbleTimer = setTimeout(() => b.classList.add('hidden'), ms);
  };
  $('chill-cat').onclick = () => cat.onPet();
  let tick = null;

  const MESSAGES = {
    progress: (d) => `Bien joué. ${d.green}/${d.total} formules du niveau en vert.`,
    up: (d) => `Toutes les formules en vert : niveau validé ! Tu passes au niveau ${d.level}.`,
    finished: () => 'Dernier niveau validé : tu es au niveau examen + 20 %.',
    warn: (d) => `Raté. Relis les formules ci-dessus. Un deuxième raté d'affilée sur ce niveau te ferait redescendre${d.level > 1 ? ` au niveau ${d.level - 1}` : ''}.`,
    down: (d) => `Deux ratés d'affilée : retour au niveau ${d.level}. Relis les formules ci-dessus avant de continuer.`,
    retry: () => 'Raté : relis les formules ci-dessus, puis réessaie avec un autre exercice.',
    review: (d) => d.ok ? 'Récupéré : cet exercice revient plus tard, de plus en plus espacé.' : 'Pas encore acquis : il revient demain. Ton niveau ne bouge pas.',
    practice: () => 'Noté (entraînement libre, ta progression ne bouge pas).',
  };

  // Combo (server count: +1 per success, a miss resets it to 0). Small feedback on every success,
  // the big slam only at milestones, so it does not wear off.
  const MILESTONES = [5, 10, 20, 30, 50, 75, 100, 150, 200];
  const TITLES = { 5: 'Bien lancé', 10: 'En feu', 20: 'Inarrêtable', 30: 'Machine', 50: 'Légende' };
  const title = (n) => TITLES[Math.max(...Object.keys(TITLES).map(Number).filter((k) => k <= n))] || 'Légende';
  function hud(n, from) {
    const h = $('combo-hud');
    if (!h) return;
    h.className = 'lv-combo' + (n >= 2 ? ' on' : '') + (n >= 10 ? ' hot' : '');
    h.replaceChildren();
    if (from !== undefined && from > n && from >= 2) h.append(`Combo ×${from} → `);
    if (n >= 2 || (from !== undefined && from >= 2)) {
      if (from === undefined || from <= n) h.append('Combo ');
      const b = document.createElement('strong');
      b.textContent = '×' + n;
      h.append(b);
      if (n >= 2) {  // loss aversion: the combo is worth keeping
        const r = document.createElement('span'); r.className = 'lv-risk'; r.textContent = ' un raté le remet à 0';
        h.append(r);
      }
    }
    h.classList.remove('bump'); void h.offsetWidth; h.classList.add('bump');
  }
  // Game-style swap: the old count is knocked out of the screen, the new one crashes in.
  // Every success with a combo; milestones add a title, a bigger number and a shake. A miss drops the old one.
  let slamTimer = null;
  function slam(n, old, kind) {
    const s = $('combo-slam');
    s.replaceChildren();
    const stage = document.createElement('div'); stage.className = 'lv-slam-stage';
    if (old >= 1 && old !== n) {
      const o = document.createElement('strong'); o.className = 'old'; o.textContent = '×' + old;
      stage.append(o);
    }
    const b = document.createElement('strong'); b.className = 'new'; b.textContent = '×' + n;
    stage.append(b);
    s.append(stage);
    if (kind === 'milestone') {
      const sub = document.createElement('span'); sub.textContent = title(n);
      s.append(sub);
    }
    s.className = `lv-slam go ${kind}` + (n >= 10 ? ' hot' : '');
    if (kind === 'milestone') { const w = $('exo'); w.classList.remove('lv-shake'); void w.offsetWidth; w.classList.add('lv-shake'); }
    clearTimeout(slamTimer);
    slamTimer = setTimeout(() => { s.className = 'lv-slam'; }, kind === 'milestone' ? 1600 : 1100);
  }
  function celebrate(d, sq, before) {
    const n = d.combo || 0;
    if (sq) { sq.classList.remove('pop'); void sq.offsetWidth; sq.classList.add('pop'); }
    const big = d.event === 'up' || d.event === 'finished';
    const milestone = MILESTONES.includes(n);
    hud(n);
    const canvas = $('gore-canvas');
    if (big || milestone) {
      pixelConfetti(canvas, d.event === 'finished' || n >= 20 ? 14 : 7);
      document.body.classList.remove('lv-flash'); void document.body.offsetWidth; document.body.classList.add('lv-flash');
    } else {
      pixelConfetti(canvas, 1);
    }
    if (n >= 2) slam(n, before, milestone ? 'milestone' : 'step');
    // happy happy happy : plus de sauts pour un palier, encore plus pour un niveau validé
    const hops = d.event === 'finished' ? 12 : big ? 8 : milestone ? 6 : 4;
    cat.happy(hops, n, big ? 'Niveau validé !' : milestone ? `Combo ×${n} !` : 'Bien joué !', 'STAND');
    if (navigator.vibrate) navigator.vibrate(milestone ? [30, 40, 30, 40, 80] : [40]);
  }

  function setup() {
    const exo = $('exo');
    if (exo) checkBreak();  // a break started before this page loaded
    const toggle = (btn, panel, onOpen) => {
      btn.onclick = () => {
        panel.hidden = !panel.hidden;
        btn.setAttribute('aria-expanded', String(!panel.hidden));
        if (!panel.hidden && onOpen) onOpen();
      };
    };
    // Opening a help before answering costs points and adds time; the server records it (session clock).
    let peek = false;
    const used = {};
    const hint = async (kind) => {
      if (answered || used[kind]) return;
      used[kind] = true;
      if (kind !== 'temps') peek = true;
      const res = await post(`/api/niveaux/${exo.dataset.subject}/hint`, { kind });
      if (!res.ok || !res.data.extra || answered) return;
      left += res.data.extra;
      if (left > 30) cat.relax();  // du temps ajouté : il arrête de stresser
      $('timer-left').textContent = fmt(left);
      $('timer-note').textContent = res.data.div > 1
        ? `Aide ouverte : +${fmt(res.data.extra)} de temps, points divisés par ${res.data.div}.`
        : `+${fmt(res.data.extra)} de temps, sans formule : seuls les points de vitesse baissent.`;
    };
    toggle($('btn-fiche'), $('fiche'), () => hint('fiche'));
    toggle($('btn-formules'), $('notions'), () => hint('solution'));
    $('btn-temps').onclick = () => { $('btn-temps').disabled = true; hint('temps'); };

    // Forced solo thinking: countdown from data-duree; "J'ai ma réponse" stops it and shows the correction.
    let left = +exo.dataset.duree || 300, answered = false;
    const half = Math.floor(left / 2);
    const fmt = (s) => `${Math.floor(s / 60)}:${String(s % 60).padStart(2, '0')}`;
    const showSolution = () => {
      answered = true;
      clearInterval(tick);
      $('solution').hidden = false;
      $('btn-correction').disabled = true;
      cat.relax();
      renderMath($('solution'));
    };
    $('timer-left').textContent = fmt(left);
    clearInterval(tick);
    tick = setInterval(() => {
      left -= 1;
      $('timer-left').textContent = fmt(Math.max(left, 0));
      if (!answered && left === half && half > 30) cat.ponder();
      if (!answered && left === 30) cat.nervous();
      if (left <= 0 && !answered) {
        showSolution();
        $('timer').textContent = 'Temps écoulé : voici la correction.';
        answer(false, true);
      }
    }, 1000);
    // Optional confidence bet (account setting): one tap before the correction, lucidity points after.
    let conf = null;
    const pariOn = $('pari-on');
    pariOn.onchange = async () => {
      const res = await post('/api/pari', { on: pariOn.checked });
      if (!res.ok) pariOn.checked = !pariOn.checked;
    };
    const reveal = () => {
      $('pari-row').hidden = true;
      showSolution();
      $('timer').textContent = $('grille') ? 'Coche le barème selon ce qui est écrit sur ta copie.' : 'Compare ta réponse avec la correction.';
      $('btn-ko').disabled = false;
      if ($('grille')) { $('grille').hidden = false; setTimeout(() => { $('btn-note').disabled = $('btn-ko').disabled; }, 1500); }
      // « Réussi » only after 1.5 s: read the correction instead of a reflex click
      setTimeout(() => { if (!$('btn-ko').disabled) $('btn-ok').disabled = false; }, 1500);
    };
    $('btn-correction').onclick = () => {
      if (!pariOn.checked) return reveal();
      $('btn-correction').disabled = true;
      $('pari-row').hidden = false;
      $('pari-row').querySelector('button').focus();
    };
    $('pari-row').querySelectorAll('[data-conf]').forEach(b => b.onclick = () => { conf = +b.dataset.conf; reveal(); });

    async function answer(ok, timeout = false, fautes = null) {
      $('btn-ok').disabled = $('btn-ko').disabled = true;
      $('pari-row').hidden = true;
      lockGrid();
      const res = await post(`/api/niveaux/${exo.dataset.subject}/result`, { level: +exo.dataset.level, exo_id: exo.dataset.exo, ok, peek, timeout, conf, revoir: exo.dataset.revoir === '1', fautes });
      const fb = $('feedback');
      if (res.data.pause) { forcedBreak(res.data.pause); $('btn-ok').disabled = $('btn-ko').disabled = false; unlockGrid(); return; }
      checkBreak();
      if (!res.ok) {
        fb.className = 'lv-feedback bad';
        fb.textContent = res.data.error || 'Erreur réseau, réessaie.';
        $('btn-ok').disabled = $('btn-ko').disabled = false;
        unlockGrid();
        return;
      }
      const d = res.data;
      fb.className = 'lv-feedback ' + (ok ? 'good' : 'bad');
      if (!ok && $('copie-tip')) $('copie-tip').hidden = false;  // the « copie 20/20 » trap, right after a miss
      const lines = [MESSAGES[d.event](d)];
      if (d.note !== null && d.note !== undefined) lines.unshift(d.note === 20 ? 'Copie 20/20 : tous les critères du barème y sont.' : `Copie ${d.note}/20 : les cases vides sont notées comme fautes.`);
      if (d.timeout) lines.push('Temps écoulé : cet exercice reviendra avec plus de temps.');
      if (ok && d.points) {
        const fast = d.secs && d.ref ? (d.secs <= d.ref ? `en ${fmt(d.secs)}, plus vite que la moyenne (${fmt(d.ref)})` : `en ${fmt(d.secs)}, moyenne ${fmt(d.ref)}`) : '';
        if (d.double) lines.push('Coup double : points ×2');
        lines.push(`+${d.points} points ${fast}${d.peek === 2 ? ' · divisé par 2 : fiche du chapitre ouverte' : d.peek ? ' · divisé par 3 : formules de la solution ouvertes' : ''}`);
      }
      if (d.calib) lines.push(ok ? `Pari tenu : tu étais sûr, +${d.calib} points de lucidité` : `Tu savais que tu ne savais pas : +${d.calib} points de lucidité`);
      fb.replaceChildren(...lines.map((t, i) => { const p = document.createElement('p'); p.textContent = t; if (i) p.className = 'lv-points'; return p; }));
      if (d.warning) {
        const w = document.createElement('p');
        w.className = 'fraud-warn';
        w.setAttribute('role', 'alert');
        w.textContent = d.warning;
        fb.append(w);
      }
      if (d.prereq && d.prereq.length) {
        const p = document.createElement('p');
        p.className = 'lv-points';
        p.append('Notions de base à revoir : ');
        d.prereq.forEach((r, i) => {
          if (i) p.append(', ');
          const a = document.createElement('a');
          a.href = `/niveaux/${r.id}`;
          a.textContent = r.titre;
          p.append(a);
        });
        fb.append(p);
      }
      if (d.xp !== undefined && $('xp')) $('xp').textContent = d.xp;
      const sq = document.querySelector(`.lv-squares i[data-exo="${exo.dataset.exo}"]`);
      if (sq) sq.className = (ok ? 'ok' : 'ko') + ' cur';
      if (d.percent !== undefined) { $('total-bar').style.width = d.percent + '%'; $('total-pct').textContent = d.percent; }
      const before = +(exo.dataset.combo || 0);
      exo.dataset.combo = d.combo || 0;
      if (ok) {
        celebrate(d, sq, before);
      } else {
        hud(d.combo || 0, before);
        if (before >= 2) slam(d.combo || 0, before, 'broken');
        const r = $('chill-cat').getBoundingClientRect();
        showCatBubble('Raté... KABOOM', 1200);
        cat.onWrongAnswer(() => {
          gore.explode(r.left + r.width / 2, r.top + r.height / 2);
          if (navigator.vibrate) navigator.vibrate([150, 50, 200]);
        });
        // show the formulas of the failed level
        $('notions').hidden = false;
        $('btn-formules').setAttribute('aria-expanded', 'true');
      }
      $('copy-ia').hidden = false;  // after every answer: a success can still hide a correction not understood
      $('next').hidden = false;
      $('next').querySelector('a').focus();
    }
    $('btn-ok').onclick = () => answer(true);
    // « copie 20/20 » mode: the grid replaces Réussi / Raté, success only when every criterion is ticked
    const grille = $('grille');
    const boxes = grille ? [...grille.querySelectorAll('input[data-i]')] : [];
    const note = () => boxes.reduce((t, b) => t + (b.checked ? +b.dataset.pts : 0), 0);
    boxes.forEach(b => b.onchange = () => { $('note').textContent = note(); });
    function lockGrid() {  // colour code: green = on your copy, red = flagged mistake
      boxes.forEach(b => { b.disabled = true; b.closest('li').className = b.checked ? 'ok' : 'ko'; });
      if (grille) $('btn-note').disabled = true;
    }
    function unlockGrid() { boxes.forEach(b => { b.disabled = false; b.closest('li').className = ''; }); if (grille) $('btn-note').disabled = false; }
    if (grille) $('btn-ok').parentElement.hidden = true;  // the grid's button is the answer
    // copy-rule reflex: one tap, verdict at once, the right line in green and the tapped wrong one in red
    if ($('choix')) {
      $('btn-ok').parentElement.hidden = true;
      $('choix').querySelectorAll('button').forEach(b => b.onclick = () => {
        $('choix').querySelectorAll('button').forEach(x => {
          x.disabled = true;
          if (x.dataset.bon === '1') x.classList.add('bon');
        });
        if (b.dataset.bon !== '1') b.classList.add('faux');
        showSolution();
        answer(b.dataset.bon === '1');
      });
    }
    if ($('methodo-on')) $('methodo-on').onchange = async (e) => {
      const r = await post('/api/methodo', { on: e.target.checked });
      if (!r.ok) { e.target.checked = !e.target.checked; return; }
      const u = new URL(location.href);  // same exercise, new mode
      u.searchParams.set('exo', exo.dataset.exo);
      location.href = u;
    };
    if (grille) $('btn-note').onclick = () => {
      answer(note() === 20, false, boxes.filter(b => !b.checked).map(b => +b.dataset.i));
    };
    $('btn-ko').onclick = () => answer(false);
    if ($('btn-signal')) $('btn-signal').onclick = async () => {
      const b = $('btn-signal');
      b.disabled = true;
      const r = await post(`/api/niveaux/${exo.dataset.subject}/signaler`,
        { level: +exo.dataset.level, exo_id: exo.dataset.exo, texte: $('signal-texte').value });
      $('signal-note').textContent = r.ok ? 'Merci, l’exercice est signalé.' : (r.data.error || 'Envoi impossible, réessaie');
      if (r.ok) $('signal-texte').value = ''; else b.disabled = false;
    };
    if ($('btn-copy-ia')) $('btn-copy-ia').addEventListener('click', () =>
      post(`/api/niveaux/${exo.dataset.subject}/copie`, { level: +exo.dataset.level, exo_id: exo.dataset.exo }));  // counted for /stats
    $('next').querySelector('a').onclick = (e) => { e.preventDefault(); next(e.currentTarget.href); };
    if ($('btn-skip')) $('btn-skip').onclick = (e) => { e.preventDefault(); clearInterval(tick); next(e.currentTarget.href); };
  }

  // Next exercise without a page reload: fetch the next page and swap #exo (a full load is the fallback).
  async function next(url) {
    try {
      const r = await fetch(url, { credentials: 'same-origin' });
      if (!r.ok) throw new Error(r.status);
      if (new URL(r.url).pathname === '/niveaux') { location.href = r.url; return; }  // review queue empty
      const doc = new DOMParser().parseFromString(await r.text(), 'text/html');
      const fresh = doc.getElementById('exo');
      if (!fresh) throw new Error('no #exo');
      const js = (d) => d.querySelector('script[src*="niveaux.js"]')?.getAttribute('src');
      if (js(doc) !== js(document)) { location.href = r.url; return; }  // new deploy: reload the code too
      $('exo').replaceWith(document.adoptNode(fresh));
      document.title = doc.title;
      if (r.url !== location.href) history.pushState(null, '', r.url);
      renderMath($('exo'));
      window.scrollTo(0, 0);
      setup();
      $('exo').querySelector('h1').focus({ preventScroll: true });
    } catch (err) {
      location.href = url;
    }
  }
  window.addEventListener('popstate', () => location.reload());
  setup();
})();
