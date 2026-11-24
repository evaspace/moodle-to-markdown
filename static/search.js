// Search box of /cours/: Pagefind index of the notion sheets (static/pagefind, built by `python3 fiches.py --index`).
// ES module: tools/bench_fiches.py imports `find` to score the exact same search.
let pagefind = null;
const load = () => (pagefind = pagefind || import('/static/pagefind/pagefind.js'));

// Pagefind keeps only sheets containing every word; a long query (an exam heading) then finds nothing,
// so fall back to one search per word and rank sheets by their summed scores.
export async function find(q, limit = 8) {
  const pf = await load();
  const all = await pf.search(q);
  if (all.results.length) return all.results.slice(0, limit);
  const words = q.split(/[^\p{L}\p{N}]+/u).filter(w => w.length > 1);
  const scores = new Map();
  for (const w of words) {
    for (const r of (await pf.search(w)).results) {
      const prev = scores.get(r.id);
      scores.set(r.id, {r, score: (prev ? prev.score : 0) + r.score});
    }
  }
  return [...scores.values()].sort((a, b) => b.score - a.score).slice(0, limit).map(x => x.r);
}

const input = document.getElementById('docs-q');
const list = document.getElementById('docs-results');
let seq = 0;
if (input) {
  input.addEventListener('focus', load, {once: true});
  input.addEventListener('input', async () => {
    const mine = ++seq, q = input.value.trim();
    await new Promise(r => setTimeout(r, 200));
    if (mine !== seq) return;  // superseded by a newer keystroke
    const items = q ? await Promise.all((await find(q)).map(r => r.data())) : [];
    if (mine !== seq) return;
    list.replaceChildren(...items.map(d => {
      const li = document.createElement('li'), a = document.createElement('a');
      const title = document.createElement('strong'), excerpt = document.createElement('span');
      a.href = d.url.replace(/\.html$/, '');
      title.textContent = d.meta.title;
      // Pagefind escapes the text and only adds <mark>; raw LaTeX (possibly cut by the excerpt) is unreadable here
      excerpt.innerHTML = d.excerpt.replace(/\$\$?[^$]*(\$\$?|$)/g, '… ');
      a.append(title, excerpt);
      li.append(a);
      return li;
    }));
    if (q && !items.length) {
      const li = document.createElement('li');
      li.textContent = 'Aucune fiche ne correspond.';
      list.replaceChildren(li);
    }
  });
}
