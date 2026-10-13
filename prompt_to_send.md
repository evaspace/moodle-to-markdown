e te conseille de faire sortir le LLM dans le format texte de ton admin (Q: / R: / ---) plutôt qu’en JSON. Le LaTeX (\frac, \neq, \beta…) casse json.loads ou, pire, est interprété en silence comme un caractère de contrôle. En texte brut il n’y a rien à échapper. Ça permet aussi de réutiliser parse_blocks de ton app.py, puis d’ajouter par-dessus des vérifications plus strictes.

1. Le prompt (system prompt)

À mettre tel quel dans prompt.txt :
