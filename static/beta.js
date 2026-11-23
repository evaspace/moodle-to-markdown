// /admin/beta week grid: fetches /admin/beta/semaine, draws courses, evals and revision blocks, refreshes every minute.
(() => {
  const START = 8 * 60, END = 22 * 60, PX = 1.2;   // minutes shown, pixels per minute
  const root = document.getElementById('bt-cal');
  if (!root) return;
  let monday = null;
  const el = (tag, cls, text) => { const e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; };
  const iso = (d) => d.toISOString().slice(0, 10);

  function lanes(items) {           // side by side when two items overlap
    const ends = [];
    items.sort((a, b) => a.debut - b.debut).forEach((it) => {
      let k = ends.findIndex((e) => e <= it.debut);
      if (k < 0) { k = ends.length; ends.push(0); }
      ends[k] = it.fin; it.lane = k;
    });
    items.forEach((it) => { it.lanes = ends.length; });
  }

  function draw(w) {
    monday = w.lundi;
    document.getElementById('bt-week').textContent = 'Semaine du ' + new Date(w.lundi + 'T12:00').toLocaleDateString('fr-FR', { day: 'numeric', month: 'long' });
    const grid = el('div', 'bt-grid');
    grid.style.setProperty('--h', ((END - START) * PX) + 'px');
    const hours = el('div', 'bt-hours');
    hours.appendChild(el('div', 'bt-head', ''));
    const body = el('div', 'bt-col-body');
    for (let m = START; m < END; m += 60) {
      const h = el('span', 'bt-hour', (m / 60) + ' h'); h.style.top = ((m - START) * PX) + 'px'; body.appendChild(h);
    }
    hours.appendChild(body); grid.appendChild(hours);
    w.jours.forEach((name, d) => {
      const col = el('div', 'bt-col' + (d === w.aujourdhui ? ' bt-today' : ''));
      col.appendChild(el('div', 'bt-head', name));
      const b = el('div', 'bt-col-body');
      for (let m = START; m < END; m += 60) { const l = el('div', 'bt-line'); l.style.top = ((m - START) * PX) + 'px'; b.appendChild(l); }
      const items = w.items.filter((it) => it.jour === d && it.fin > START && it.debut < END);
      lanes(items);
      items.forEach((it) => {
        const box = el(it.lien ? 'a' : 'div', `bt-ev bt-${it.kind} bt-${it.matiere}`);
        box.style.animationDelay = (it.jour * 30 + (it.debut - START) / 6) + 'ms';
        if (it.lien) box.href = it.lien;
        const top = Math.max(it.debut, START), bot = Math.min(it.fin, END);
        box.style.top = ((top - START) * PX) + 'px';
        box.style.height = Math.max((bot - top) * PX - 2, 14) + 'px';
        const hpx = (bot - top) * PX;
        if (hpx < 40) box.classList.add('bt-short');        // title only
        else if (hpx < 100) box.classList.add('bt-mid');    // title, hour, bar
        box.style.left = (100 * it.lane / it.lanes) + '%';
        box.style.width = (100 / it.lanes) + '%';
        box.title = [it.heure, it.titre, it.detail, it.conseil].filter(Boolean).join('\n');
        box.appendChild(el('span', 'bt-ev-t', it.court));
        box.appendChild(el('span', 'bt-ev-h', it.heure));
        if (it.moi != null && it.kind !== 'eval') {
          const bar = el('span', 'bt-bar');
          const me = el('span', 'bt-bar-me'); me.style.width = it.moi + '%';
          const cl = el('span', 'bt-bar-cl'); cl.style.left = it.classe + '%';
          bar.append(me, cl);
          box.append(bar, el('span', 'bt-ev-p', `toi ${it.moi} % \u00b7 classe ${it.classe} %`));
        }
        b.appendChild(box);
      });
      if (d === w.aujourdhui && w.maintenant > START && w.maintenant < END) {
        const now = el('div', 'bt-now'); now.style.top = ((w.maintenant - START) * PX) + 'px'; b.appendChild(now);
      }
      col.appendChild(b); grid.appendChild(col);
    });
    const scroll = root.querySelector('.bt-grid-scroll');
    const keep = scroll.scrollLeft;
    scroll.replaceChildren(grid);
    scroll.scrollLeft = keep;

    cards(w.cours || []);
  }

  // one card per course, most urgent first (refreshed with the grid)
  function cards(list) {
    const box = document.getElementById('bt-cards');
    box.replaceChildren(...list.map((c) => {
      const card = el(c.lien ? 'a' : 'div', `bt-card bt-${c.matiere}${c.urgent ? ' urgent' : ''}`);
      if (c.lien) card.href = c.lien;
      const big = el('div', 'bt-card-big');
      if (c.jours_eval != null && c.jours_eval <= 21) {
        big.append(el('strong', null, c.jours_eval ? 'J-' + c.jours_eval : 'Auj.'), el('span', null, 'éval ' + c.eval));
      } else {
        big.append(el('strong', c.retard >= 15 ? 'late' : null, c.retard ? '−' + c.retard : 'OK'), el('span', null, c.retard ? 'pts de retard' : 'à jour'));
      }
      const main = el('div', 'bt-card-main');
      main.appendChild(el('h3', null, c.titre));
      const bar = el('span', 'bt-bar');
      const me = el('span', 'bt-bar-me'); me.style.width = c.moi + '%';
      const cl = el('span', 'bt-bar-cl'); cl.style.left = c.classe + '%';
      bar.append(me, cl);
      main.append(bar, el('p', 'bt-card-pct', `toi ${c.moi} % \u00b7 classe ${c.classe} % (${c.faits}/${c.total} séances passées)`));
      main.appendChild(el('p', 'bt-card-tip', c.conseil));
      card.append(big, main);
      return card;
    }));
  }

  // forced break option and live state
  async function pause(on) {
    try {
      const r = on == null ? await fetch('/api/pause', { credentials: 'same-origin' })
        : await fetch('/api/pause', { method: 'POST', credentials: 'same-origin', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ on }) });
      if (!r.ok) return;
      const st = await r.json();
      const big = document.getElementById('bt-pause-big'), unit = document.getElementById('bt-pause-unit');
      const text = document.getElementById('bt-pause-text'), btn = document.getElementById('bt-pause-btn');
      btn.hidden = false;
      btn.textContent = st.on ? 'Désactiver la pause forcée' : 'Activer la pause forcée';
      btn.className = 'lv-btn' + (st.on ? '' : ' primary');
      btn.onclick = () => pause(!st.on);
      document.getElementById('bt-pause').classList.toggle('on', st.on);
      const plan = `${st.travail} min de travail, puis ${st.pause} min de pause (${st.source}).`;
      if (st.force) {
        big.textContent = Math.ceil(st.restant / 60); unit.textContent = 'min de pause';
        text.textContent = `En pause après ${st.travaille} min d'affilée. ${plan}`;
      } else if (st.travaille) {
        big.textContent = st.avant_pause; unit.textContent = 'min avant la pause';
        text.textContent = `${st.travaille} min de travail d'affilée. ${plan}`;
      } else {
        big.textContent = st.travail; unit.textContent = 'min de travail';
        text.textContent = (st.on ? 'Activée. ' : 'Désactivée. ') + plan;
      }
    } catch (e) { /* offline */ }
  }
  pause();
  setInterval(() => pause(), 60000);

  async function load(lundi) {
    try {
      const r = await fetch('/admin/beta/semaine' + (lundi ? '?lundi=' + lundi : ''), { credentials: 'same-origin' });
      if (r.ok) draw(await r.json());
    } catch (e) { /* offline: keep the last grid */ }
  }
  const shift = (days) => { const d = new Date(monday + 'T12:00'); d.setDate(d.getDate() + days); load(iso(d)); };
  document.getElementById('bt-prev').onclick = () => shift(-7);
  document.getElementById('bt-next').onclick = () => shift(7);
  document.getElementById('bt-this').onclick = () => load('');
  load('').then(() => {   // phone: bring today's column into view
    const t = root.querySelector('.bt-today');
    if (t) root.querySelector('.bt-grid-scroll').scrollLeft = t.offsetLeft - 48;
  });
  setInterval(() => load(monday), 60000);
})();
