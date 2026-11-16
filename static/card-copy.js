// "Copier pour une IA" on feed and scroll cards (static/app.js, static/scroll.js).
// Uses the vendored copy-for-llm lib (static/copy-for-llm.js): statement, choices, and the
// explanation only once the card is revealed, like the solution on the exercise page.
(function () {
  const FOOTER = "Source : {url} (carte d'Epita Doomscrolling, site gratuit d'entraînement aux examens de la prépa EPITA, créé par Morgan Pierrefeu : https://morgan.pierref.eu)";
  const PROMPT = "Je révise un examen de prépa EPITA. Voici une carte de révision. Aide-moi à la comprendre sans me donner la réponse tout de suite : rappelle les notions utiles, puis attends ma proposition. Les formules sont écrites en LaTeX.";
  const PROMPT_AFTER = "Je révise un examen de prépa EPITA. Voici une carte de révision et son explication. Explique-la étape par étape, nomme chaque formule ou théorème utilisé, puis donne-moi une question semblable pour m'entraîner, sans sa réponse. Les formules sont écrites en LaTeX.";

  window.copyCardForLLM = function (card, btn, title) {
    const parts = [{ title: 'Question', el: card.querySelector('.card-front') }];
    const choices = [...card.querySelectorAll('.qcm-choices .choice-btn')];
    if (choices.length) {
      const ul = document.createElement('ul');
      choices.forEach((b) => { const li = document.createElement('li'); li.innerHTML = b.innerHTML; ul.append(li); });
      parts.push({ title: 'Choix', el: ul });
    }
    const shown = card.classList.contains('revealed');
    if (shown) card.querySelectorAll('.card-back').forEach((b) => parts.push({ title: 'Explication', el: b }));
    const text = CopyForLLM.build({ parts, title, prompt: shown ? PROMPT_AFTER : PROMPT, footer: FOOTER });
    const label = btn.textContent;
    CopyForLLM.copy(text).then((ok) => {
      btn.textContent = ok ? 'Copié' : 'Échec';
      setTimeout(() => { btn.textContent = label; }, 1800);
    });
  };
})();
