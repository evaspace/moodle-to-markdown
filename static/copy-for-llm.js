/*! copy-for-llm v1.0.0 | MIT | https://github.com/evaspace/copy-for-llm
 *
 * "Copy for an AI" button: turns parts of a web page into clean Markdown that an LLM
 * can read, with the math as LaTeX source (KaTeX, MathJax 2/3, data-tex), a ready-made
 * prompt on top and the source URL at the bottom.
 *
 * Copying rendered math by hand gives garbage (each glyph twice, no structure); this
 * reads the TeX the renderer kept in the page instead.
 *
 * Declarative use:
 *   <button data-copy-llm="#statement|Exercise; #solution|Solution"
 *           data-copy-prompt="Explain this solution step by step."
 *           data-copy-title="Exercise 3">Copy for an AI</button>
 * Script use:
 *   CopyForLLM.config({ prompt: '...', footer: 'Source: {url}' });
 *   CopyForLLM.copy(CopyForLLM.build({ parts: [{ title: 'Exercise', el }] }));
 */
(function (root) {
  'use strict';

  var settings = {
    prompt: '',
    footer: 'Source: {url}',
    done: 'Copied',
    failed: 'Copy failed',
  };

  var SKIP = { SCRIPT: 1, STYLE: 1, NOSCRIPT: 1, TEMPLATE: 1, BUTTON: 1, SVG: 1, CANVAS: 1, NAV: 1 };

  function clean(tex) {
    return String(tex || '').replace(/\s+/g, ' ').trim();
  }

  // TeX source of a math element, or null when the element is not math.
  function texOf(node) {
    if (node.hasAttribute('data-tex')) return node.getAttribute('data-tex');
    if (node.hasAttribute('data-latex')) return node.getAttribute('data-latex');
    if (node.classList.contains('katex') || node.classList.contains('katex-display')) {
      var ann = node.querySelector('annotation[encoding="application/x-tex"]');
      return ann ? ann.textContent : null;
    }
    if (node.tagName === 'MJX-CONTAINER') {
      var items = root.MathJax && root.MathJax.startup && root.MathJax.startup.document &&
        root.MathJax.startup.document.getMathItemsWithin ?
        root.MathJax.startup.document.getMathItemsWithin(node) : [];
      return items.length ? items[0].math : null;
    }
    return null;
  }

  function isDisplay(node) {
    return node.classList.contains('katex-display') || node.getAttribute('display') === 'true' ||
      node.getAttribute('data-display') === 'true';
  }

  function inline(s) {
    return s.replace(/[ \t]*\n[ \t]*/g, ' ');
  }

  function table(node) {
    var rows = Array.prototype.slice.call(node.querySelectorAll('tr'));
    if (!rows.length) return '';
    var lines = rows.map(function (tr) {
      var cells = Array.prototype.slice.call(tr.children).map(function (c) {
        return inline(walk(c)).replace(/\|/g, '\\|').trim();
      });
      return '| ' + cells.join(' | ') + ' |';
    });
    var n = rows[0].children.length;
    lines.splice(1, 0, '|' + new Array(n + 1).join(' --- |'));
    return '\n\n' + lines.join('\n') + '\n\n';
  }

  function list(node) {
    var ordered = node.tagName === 'OL';
    var i = 0;
    var out = Array.prototype.slice.call(node.children).map(function (li) {
      i += 1;
      var body = walk(li).trim().replace(/\n/g, '\n   ');
      return (ordered ? i + '. ' : '- ') + body;
    });
    return '\n\n' + out.join('\n') + '\n\n';
  }

  function walk(node) {
    var out = '';
    for (var c = node.firstChild; c; c = c.nextSibling) {
      if (c.nodeType === 3) { out += c.textContent.replace(/\s+/g, ' '); continue; }
      if (c.nodeType !== 1) continue;
      if (SKIP[c.tagName.toUpperCase()] || c.hidden || c.hasAttribute('data-copy-ignore') ||
          c.getAttribute('aria-hidden') === 'true' && !texOf(c)) continue;
      // MathJax 2 keeps the source in a <script type="math/tex"> next to the rendering.
      if (c.classList.contains('MathJax_Preview')) continue;
      var mj2 = c.nextElementSibling;
      if (c.classList.contains('MathJax') || c.classList.contains('MathJax_Display')) {
        while (mj2 && !/^math\/tex/.test(mj2.type || '')) mj2 = mj2.nextElementSibling;
        if (mj2) out += /mode=display/.test(mj2.type) ? '\n\n$$' + clean(mj2.textContent) + '$$\n\n' : '$' + clean(mj2.textContent) + '$';
        continue;
      }
      var tex = texOf(c);
      if (tex !== null) {
        out += isDisplay(c) ? '\n\n$$' + clean(tex) + '$$\n\n' : '$' + clean(tex) + '$';
        continue;
      }
      var tag = c.tagName.toUpperCase();
      var inner;
      switch (tag) {
        case 'H1': case 'H2': case 'H3': case 'H4': case 'H5': case 'H6':
          out += '\n\n' + new Array(+tag[1] + 2).join('#') + ' ' + inline(walk(c)).trim() + '\n\n'; break;
        case 'P': case 'DIV': case 'SECTION': case 'ARTICLE': case 'BLOCKQUOTE': case 'FIGURE': case 'DETAILS':
          out += '\n\n' + walk(c) + '\n\n'; break;
        case 'SUMMARY': out += '**' + inline(walk(c)).trim() + '**\n\n'; break;
        case 'BR': out += '\n'; break;
        case 'HR': out += '\n\n---\n\n'; break;
        case 'UL': case 'OL': out += list(c); break;
        case 'TABLE': out += table(c); break;
        case 'STRONG': case 'B':
          inner = walk(c).trim(); out += inner ? '**' + inner + '**' : ''; break;
        case 'EM': case 'I':
          inner = walk(c).trim(); out += inner ? '*' + inner + '*' : ''; break;
        case 'CODE': out += '`' + c.textContent + '`'; break;
        case 'PRE': out += '\n\n```\n' + c.textContent.replace(/\n$/, '') + '\n```\n\n'; break;
        case 'A':
          inner = walk(c).trim();
          out += c.href && inner ? '[' + inner + '](' + c.href + ')' : inner; break;
        case 'IMG': out += c.alt ? '[image: ' + c.alt + ']' : ''; break;
        default: out += walk(c);
      }
    }
    return out;
  }

  function toMarkdown(el) {
    return walk(el).replace(/[ \t]+\n/g, '\n').replace(/\n{3,}/g, '\n\n').trim();
  }

  function fill(tpl, vars) {
    return String(tpl).replace(/\{(\w+)\}/g, function (m, k) { return k in vars ? vars[k] : m; });
  }

  // opts: { parts: [{title, el}], prompt, title, url, footer }
  function build(opts) {
    var vars = { url: opts.url || root.location.href, title: opts.title || root.document.title };
    var out = [];
    var prompt = opts.prompt != null ? opts.prompt : settings.prompt;
    if (prompt) out.push(fill(prompt, vars).trim());
    if (opts.title) out.push('# ' + opts.title);
    (opts.parts || []).forEach(function (p) {
      if (!p.el) return;
      var md = toMarkdown(p.el);
      if (md) out.push((p.title ? '## ' + p.title + '\n\n' : '') + md);
    });
    var footer = opts.footer != null ? opts.footer : settings.footer;
    if (footer) out.push('---\n' + fill(footer, vars).trim());
    return out.join('\n\n') + '\n';
  }

  function copy(text) {
    function fallback() {
      var ta = root.document.createElement('textarea');
      ta.value = text;
      ta.setAttribute('readonly', '');
      ta.style.cssText = 'position:fixed;top:0;left:0;opacity:0';
      root.document.body.appendChild(ta);
      ta.select();
      var ok = false;
      try { ok = root.document.execCommand('copy'); } catch (e) { ok = false; }
      ta.remove();
      return ok;
    }
    if (root.navigator.clipboard && root.navigator.clipboard.writeText) {
      return root.navigator.clipboard.writeText(text).then(function () { return true; }, fallback);
    }
    return Promise.resolve(fallback());
  }

  // "#a|Title A; #b|Title B" -> [{el, title}], hidden parts left out.
  function partsFrom(spec) {
    return String(spec || '').split(';').map(function (s) {
      var bits = s.split('|');
      var el = bits[0].trim() ? root.document.querySelector(bits[0].trim()) : null;
      return { el: el && !el.closest('[hidden]') ? el : null, title: (bits[1] || '').trim() };
    }).filter(function (p) { return p.el; });
  }

  function onClick(e) {
    var btn = e.target.closest && e.target.closest('[data-copy-llm]');
    if (!btn) return;
    e.preventDefault();
    var text = build({
      parts: partsFrom(btn.getAttribute('data-copy-llm')),
      prompt: btn.hasAttribute('data-copy-prompt') ? btn.getAttribute('data-copy-prompt') : null,
      title: btn.getAttribute('data-copy-title') || '',
      footer: btn.hasAttribute('data-copy-footer') ? btn.getAttribute('data-copy-footer') : null,
    });
    var label = btn.textContent;
    copy(text).then(function (ok) {
      btn.textContent = ok ? settings.done : settings.failed;
      btn.dispatchEvent(new CustomEvent('copy-llm', { bubbles: true, detail: { ok: ok, text: text } }));
      setTimeout(function () { btn.textContent = label; }, 1800);
    });
  }

  root.document.addEventListener('click', onClick);

  root.CopyForLLM = {
    config: function (o) { for (var k in o) settings[k] = o[k]; return settings; },
    toMarkdown: toMarkdown,
    build: build,
    copy: copy,
  };
})(window);
