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
  const exo = $('exo');
  if (!exo) return;

  const renderMath = (el) => {
    if (window.renderMathInElement) {
      renderMathInElement(el, { delimiters: [{ left: '$$', right: '$$', display: true }, { left: '$', right: '$', display: false }], throwOnError: false });
    }
  };
  window.addEventListener('load', () => renderMath(document.body));

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
  const tick = setInterval(() => {
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

  // Level validated: pixel-art confetti thrown everywhere, on the gore canvas (idle on a success).
  function confetti(canvas, bursts) {
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

  const MESSAGES = {
    progress: (d) => `Bien joué. ${d.green}/${d.total} formules du niveau en vert.`,
    up: (d) => `Toutes les formules en vert : niveau validé ! Tu passes au niveau ${d.level}.`,
    finished: () => 'Dernier niveau validé : tu es au niveau examen + 20 %.',
    down: (d) => `Raté : retour au niveau ${d.level}. Relis les formules ci-dessus avant de continuer.`,
    retry: () => 'Raté : relis les formules ci-dessus, puis réessaie avec un autre exercice.',
    practice: () => 'Noté (entraînement libre, ta progression ne bouge pas).',
  };

  async function answer(ok, timeout = false) {
    $('btn-ok').disabled = $('btn-ko').disabled = true;
    const res = await post(`/api/niveaux/${exo.dataset.subject}/result`, { level: +exo.dataset.level, exo_id: exo.dataset.exo, ok, peek, timeout });
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
    if (ok) {
      cat.onCorrectAnswer(1);
      showCatBubble(d.event === 'up' || d.event === 'finished' ? 'Niveau validé !' : 'Bien joué !');
      if (d.event === 'up' || d.event === 'finished') confetti($('gore-canvas'), d.event === 'finished' ? 14 : 7);
      if (navigator.vibrate) navigator.vibrate([40]);
    } else {
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
    $('next').hidden = false;
    $('next').querySelector('a').focus();
  }
  $('btn-ok').onclick = () => answer(true);
  $('btn-ko').onclick = () => answer(false);
})();
