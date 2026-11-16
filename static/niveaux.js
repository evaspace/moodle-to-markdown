// Niveaux mode: account form, and the exercise page (formulas, correction, self-assessed result).
(function () {
  const $ = (id) => document.getElementById(id);

  async function post(url, body) {
    const r = await fetch(url, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body || {}) });
    let data = {};
    try { data = await r.json(); } catch (e) { /* empty body */ }
    return { ok: r.ok, data };
  }

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

  // Combo (server count: +1 per success, a miss halves it). Small feedback on every success,
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
    showCatBubble(big ? 'Niveau validé !' : milestone ? `Combo ×${n} !` : 'Bien joué !', big || milestone ? 2600 : 1600);
    cat.onCorrectAnswer(Math.min(1 + Math.floor(n / 5), 5));
    if (navigator.vibrate) navigator.vibrate(milestone ? [30, 40, 30, 40, 80] : [40]);
  }

  function setup() {
    const exo = $('exo');
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
      used[kind] = peek = true;
      const res = await post(`/api/niveaux/${exo.dataset.subject}/hint`, { kind });
      if (!res.ok || !res.data.extra || answered) return;
      left += res.data.extra;
      $('timer-left').textContent = fmt(left);
      $('timer-note').textContent = `Aide ouverte : +${fmt(res.data.extra)} de temps, points divisés par ${res.data.div}.`;
    };
    toggle($('btn-fiche'), $('fiche'), () => hint('fiche'));
    toggle($('btn-formules'), $('notions'), () => hint('solution'));

    // Forced solo thinking: countdown from data-duree; "J'ai ma réponse" stops it and shows the correction.
    let left = +exo.dataset.duree || 300, answered = false;
    const fmt = (s) => `${Math.floor(s / 60)}:${String(s % 60).padStart(2, '0')}`;
    const showSolution = () => {
      answered = true;
      clearInterval(tick);
      $('solution').hidden = false;
      $('btn-correction').disabled = true;
      renderMath($('solution'));
    };
    $('timer-left').textContent = fmt(left);
    clearInterval(tick);
    tick = setInterval(() => {
      left -= 1;
      $('timer-left').textContent = fmt(Math.max(left, 0));
      if (left <= 0 && !answered) {
        showSolution();
        $('timer').textContent = 'Temps écoulé : voici la correction.';
        answer(false, true);
      }
    }, 1000);
    $('btn-correction').onclick = () => {
      showSolution();
      $('timer').textContent = 'Compare ta réponse avec la correction.';
      $('btn-ok').disabled = false; $('btn-ko').disabled = false;
    };

    async function answer(ok, timeout = false) {
      $('btn-ok').disabled = $('btn-ko').disabled = true;
      const res = await post(`/api/niveaux/${exo.dataset.subject}/result`, { level: +exo.dataset.level, exo_id: exo.dataset.exo, ok, peek, timeout, revoir: exo.dataset.revoir === '1' });
      const fb = $('feedback');
      if (!res.ok) {
        fb.className = 'lv-feedback bad';
        fb.textContent = res.data.error || 'Erreur réseau, réessaie.';
        $('btn-ok').disabled = $('btn-ko').disabled = false;
        return;
      }
      const d = res.data;
      fb.className = 'lv-feedback ' + (ok ? 'good' : 'bad');
      const lines = [MESSAGES[d.event](d)];
      if (d.timeout) lines.push('Temps écoulé : cet exercice reviendra avec plus de temps.');
      if (ok && d.points) {
        const fast = d.secs && d.ref ? (d.secs <= d.ref ? `en ${fmt(d.secs)}, plus vite que la moyenne (${fmt(d.ref)})` : `en ${fmt(d.secs)}, moyenne ${fmt(d.ref)}`) : '';
        lines.push(`+${d.points} points ${fast}${d.peek === 2 ? ' · divisé par 2 : fiche du chapitre ouverte' : d.peek ? ' · divisé par 3 : formules de la solution ouvertes' : ''}`);
      }
      fb.replaceChildren(...lines.map((t, i) => { const p = document.createElement('p'); p.textContent = t; if (i) p.className = 'lv-points'; return p; }));
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
        $('copy-ia').hidden = false;  // only after a miss: the AI explains the correction not understood
        // show the formulas of the failed level
        $('notions').hidden = false;
        $('btn-formules').setAttribute('aria-expanded', 'true');
      }
      $('next').hidden = false;
      $('next').querySelector('a').focus();
    }
    $('btn-ok').onclick = () => answer(true);
    $('btn-ko').onclick = () => answer(false);
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
