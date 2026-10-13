"""
md_converter.py - Convertisseur HTML Moodle vers Markdown optimisé pour la prise de notes.
Gère le nettoyage des balises Moodle et préserve les formules LaTeX/MathJax intactes.
"""

import re
import urllib.parse
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# ---------------------------------------------------------------------------
# Balises mathématiques Moodle non standard (présentes dans 1 152 fichiers)
# [mathjaxinline]X[/mathjaxinline]  ->  $X$     (inline)
# [mathjax]X[/mathjax]              ->  $$X$$   (display)
# Le contenu TeX est préservé tel quel : seuls les espaces extérieurs sont
# nettoyés. md_converter.py:67 (html_to_markdown) ne les traite pas, d'où
# cette passe de normalisation utilisée par md_to_cards.py.
# ---------------------------------------------------------------------------
MATHJAX_INLINE_TAG_RE = re.compile(
    r"\[\s*mathjaxinline\s*\](.*?)\[\s*/mathjaxinline\s*\]",
    re.DOTALL | re.IGNORECASE,
)
MATHJAX_BLOCK_TAG_RE = re.compile(
    r"\[\s*mathjax\s*\](.*?)\[\s*/mathjax\s*\]",
    re.DOTALL | re.IGNORECASE,
)


def normalize_mathjax_tags(text: str) -> str:
    """Convertit les balises [mathjaxinline]/[mathjax] en $...$ / $$...$$."""
    if not text:
        return text
    text = MATHJAX_BLOCK_TAG_RE.sub(
        lambda m: "$$" + m.group(1).strip() + "$$", text
    )
    text = MATHJAX_INLINE_TAG_RE.sub(
        lambda m: "$" + m.group(1).strip() + "$", text
    )
    return text


def sanitize_filename(name: str, max_len: int = 100) -> str:
    """
    Nettoie une chaîne pour qu'elle devienne un nom de dossier ou de fichier valide
    sur tous les systèmes de fichiers (Linux, Windows, macOS).
    """
    if not name:
        return "sans_nom"
    # Remplacer les caractères interdits / \ : * ? " < > |
    cleaned = re.sub(r'[\\/*?:"<>|]', "-", name)
    # Nettoyer les répétitions de tirets et espaces
    cleaned = re.sub(r"-\s*-+", "-", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned)
    cleaned = cleaned.strip(" .-_")
    if len(cleaned) > max_len:
        cleaned = cleaned[:max_len].strip(" .-_")
    return cleaned or "item"


def clean_moodle_html(html_content: str, base_url: str = "") -> str:
    """
    Nettoie le HTML généré par Moodle :
    - Supprime les éléments invisibles d'accessibilité (sr-only, accesshide)
    - Supprime les aperçus MathJax doublons (MathJax_Preview)
    - Supprime les menus d'actions/édition
    - Résout les URLs relatives
    """
    if not html_content:
        return ""

    soup = BeautifulSoup(html_content, "html.parser")

    # Supprimer le bruit d'accessibilité et les menus
    unwanted_classes = [
        "sr-only",
        "accesshide",
        "MathJax_Preview",
        "hidden",
        "action-menu",
        "inplaceeditable",
        "quickeditlink",
    ]
    for el in soup.find_all(class_=lambda c: c and any(cls in c.split() for cls in unwanted_classes)):
        el.decompose()

    # Rendre absolus les liens et images relatifs
    if base_url:
        for tag in soup.find_all(["a", "img"]):
            attr = "href" if tag.name == "a" else "src"
            val = tag.get(attr)
            if val and not val.startswith(("http://", "https://", "mailto:", "data:")):
                tag[attr] = urllib.parse.urljoin(base_url, val)

    return str(soup)


def html_to_markdown(html_content: str, base_url: str = "") -> str:
    """
    Convertit du HTML Moodle en Markdown élégant avec prise en charge complète
    des équations LaTeX (MathJax) inline ($...$) et display ($$...$$).
    """
    if not html_content:
        return ""

    cleaned_html = clean_moodle_html(html_content, base_url)
    soup = BeautifulSoup(cleaned_html, "html.parser")

    math_store = {}

    def stash_math(content: str, is_block: bool = False) -> str:
        idx = len(math_store)
        placeholder = f"XMATHPH{idx}X"
        cleaned_tex = content.strip()
        if is_block:
            math_store[placeholder] = f"\n\n$$\n{cleaned_tex}\n$$\n\n"
        else:
            math_store[placeholder] = f" ${cleaned_tex}$ "
        return placeholder

    # 1. Traitement des images TeX (filtre tex Moodle)
    for img in soup.find_all("img"):
        classes = img.get("class", [])
        if isinstance(classes, str):
            classes = classes.split()
        is_tex_img = any(c in ["tex", "filter_mathjaxloader_equation"] for c in classes) or "filter/tex" in img.get("src", "")
        if is_tex_img:
            tex_code = img.get("alt", "").strip()
            if tex_code:
                is_display = tex_code.startswith("$$") and tex_code.endswith("$$")
                code = tex_code[2:-2] if is_display else tex_code
                ph = stash_math(code, is_block=is_display)
                img.replace_with(ph)

    # 2. Traitement des balises script MathJax
    for script in soup.find_all("script"):
        stype = script.get("type", "")
        if "math/tex" in stype:
            is_display = "mode=display" in stype
            code = (script.string or "").strip()
            ph = stash_math(code, is_block=is_display)
            script.replace_with(ph)
        else:
            script.decompose()

    raw_html = str(soup)

    # 3. Traitement des délimiteurs TeX dans le texte brut \( ... \) et \[ ... \]
    raw_html = re.sub(
        r"\\\((.+?)\\\)",
        lambda m: stash_math(m.group(1), is_block=False),
        raw_html,
        flags=re.DOTALL,
    )
    raw_html = re.sub(
        r"\\\[(.+?)\\\]",
        lambda m: stash_math(m.group(1), is_block=True),
        raw_html,
        flags=re.DOTALL,
    )
    raw_html = re.sub(
        r"\$\$(.+?)\$\$",
        lambda m: stash_math(m.group(1), is_block=True),
        raw_html,
        flags=re.DOTALL,
    )

    # 4. Conversion HTML -> Markdown
    markdown = md(
        raw_html,
        heading_style="ATX",
        autolinks=False,
        bullets="*",
        strip=["script", "style"],
    )

    # 5. Restauration des équations mathématiques sans altération
    for ph, actual_math in math_store.items():
        markdown = markdown.replace(ph, actual_math)

    # 6. Normalisation de la mise en page
    # Remplacer plus de 2 retours à la ligne consécutifs par 2
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    # Nettoyer les espaces en début/fin de ligne superflus
    lines = [line.rstrip() for line in markdown.splitlines()]
    markdown = "\n".join(lines).strip()

    return markdown


def preserve_user_notes(existing_markdown: str, new_markdown: str, marker: str = "## ✍️ Mes Notes Personnelles") -> str:
    """
    Préserve les notes rédigées par l'étudiant dans le fichier existant
    lorsqu'une resynchronisation est effectuée.
    """
    if not existing_markdown or marker not in existing_markdown:
        return new_markdown

    parts = existing_markdown.split(marker, 1)
    user_content = parts[1].strip()

    # Vérifier s'il y a du contenu réel au-delà du commentaire template
    has_real_notes = any(
        line.strip() and not line.strip().startswith("<!--")
        for line in user_content.splitlines()
    )

    if has_real_notes and marker in new_markdown:
        new_base = new_markdown.split(marker, 1)[0]
        return f"{new_base}{marker}\n\n{user_content}\n"

    return new_markdown
