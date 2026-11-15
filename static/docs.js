(function () {
  var OPTS = {
    delimiters: [
      {left: '$$', right: '$$', display: true},
      {left: '\\[', right: '\\]', display: true},
      {left: '$', right: '$', display: false},
      {left: '\\(', right: '\\)', display: false}
    ],
    ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
    throwOnError: false,
    strict: false,
    trust: true
  };
  var tries = 0;
  function render() {
    var content = document.querySelector('.docs-content');
    if (!content) return;
    if (window.renderMathInElement) {
      renderMathInElement(content, OPTS);
    } else if (tries++ < 50) {
      setTimeout(render, 200);   // KaTeX (CDN) pas encore chargé
    }
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', render);
  else render();
})();
