// Sliding indicator for tab rows, the navbar and the footer: a block (or a line) glides to the hovered item,
// returns to the current one when the pointer leaves, stays on a clicked one, and on a new page
// slides from the item clicked on the previous page. Markup: data-slide="fill" | "line" on the row;
// data-slide-items="<selector>" picks nested items. Rows built later by JS call window.slideInit(row).
(() => {
  const init = (box) => {
    if (box.classList.contains('slide-ready')) return;
    const items = [...box.querySelectorAll(box.dataset.slideItems || ':scope > a, :scope > button')];
    if (!items.length) return;
    items.forEach((el) => el.classList.add('slide-item'));
    const key = 'slide:' + (box.getAttribute('aria-label') || box.className);
    const line = box.dataset.slide === 'line';
    const pill = document.createElement('span');
    pill.className = 'slide-pill';
    pill.setAttribute('aria-hidden', 'true');
    box.prepend(pill);
    box.classList.add('slide-ready', line ? 'slide-line' : 'slide-fill');
    const current = () => items.find((i) => i.matches('[aria-current], [aria-selected="true"]'));
    let shown = null, pinned = null;
    const go = (el, instant) => {
      if (shown && shown !== el) shown.classList.remove('on');
      const hidden = !shown || pill.style.opacity === '0';
      shown = el;
      if (!el || !el.offsetWidth) { pill.style.opacity = '0'; return; }
      el.classList.add('on');
      const r = el.getBoundingClientRect(), b = box.getBoundingClientRect();  // works for nested items too
      const x = r.left - b.left - box.clientLeft, top = r.top - b.top - box.clientTop;
      const h = line ? 3 : el.offsetHeight;
      const y = line ? top + el.offsetHeight + 2 : top;
      if (instant || hidden) pill.style.transition = 'none';
      pill.style.transform = `translate(${x}px, ${y}px) scale(${el.offsetWidth}, ${h})`;
      pill.style.opacity = '1';
      if (instant || hidden) { void pill.offsetWidth; pill.style.transition = ''; }
    };
    const rest = () => go(pinned || current());
    items.forEach((el, i) => {
      el.addEventListener('pointerenter', () => go(el));
      el.addEventListener('focus', () => go(el));
      el.addEventListener('click', () => {
        pinned = el;
        try { sessionStorage.setItem(key, i); } catch (e) { /* storage off: no slide-in on the next page */ }
      });
    });
    box.addEventListener('pointerleave', rest);
    box.addEventListener('focusout', (e) => { if (!box.contains(e.relatedTarget)) rest(); });
    let from = null;
    try { from = items[sessionStorage.getItem(key)]; sessionStorage.removeItem(key); } catch (e) { /* ignore */ }
    if (from && current() && from !== current()) { go(from, true); requestAnimationFrame(() => requestAnimationFrame(rest)); } else go(current(), true);
    new ResizeObserver(() => go(shown, true)).observe(box);  // burger menu opening, wrapping, fonts loading
  };
  window.slideInit = init;
  document.querySelectorAll('[data-slide]').forEach(init);
})();
