document.addEventListener('DOMContentLoaded', () => {
  const content = document.querySelector('.docs-content');
  if (content && window.renderMathInElement) {
    renderMathInElement(content, {
      delimiters: [
        {left: '$$', right: '$$', display: true},
        {left: '$', right: '$', display: false},
        {left: '\\[', right: '\\]', display: true},
        {left: '\\(', right: '\\)', display: false}
      ],
      throwOnError: false
    });
  }
});
