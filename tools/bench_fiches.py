"""Course search benchmark: run every query of tools/fiches_bench.json in the real Pagefind index (headless Chromium).

Pass if the expected sheet is in the top 3 for >= 80 % of queries; otherwise fix the sheets' `alias`.
Run with the Playwright venv: ~/.local/share/playwright-venv/bin/python tools/bench_fiches.py
"""
import functools
import http.server
import json
import sys
import threading
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
bench = json.loads((ROOT / 'tools' / 'fiches_bench.json').read_text(encoding='utf-8'))['queries']
handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(ROOT))
server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), handler)
threading.Thread(target=server.serve_forever, daemon=True).start()
base = f'http://127.0.0.1:{server.server_port}'
with sync_playwright() as p:
    page = p.chromium.launch().new_page()
    page.goto(base + '/static/docs.css')
    tops = page.evaluate('''async qs => { const {find} = await import('/static/search.js'); const out = [];
        for (const q of qs) out.push(await Promise.all((await find(q, 3)).map(async r => (await r.data()).meta.id)));
        return out; }''', [b['q'] for b in bench])
server.shutdown()
hits = 0
for b, top in zip(bench, tops):
    ok = any(i in b['ok'] for i in top)
    hits += ok
    print(f"{'OK ' if ok else 'RATÉ'} {b['q']!r} -> {top} (attendu {b['ok']})")
rate = hits / len(bench)
print(f'{hits}/{len(bench)} = {rate:.0%} dans le top 3 (objectif 80 %)')
sys.exit(0 if rate >= 0.8 else 1)
