# MathsDoomScrolling — Project Direction

## Vision

Transform Moodle EPITA course exports into high-quality **spaced-repetition flashcards**
with a multi-pass LLM pipeline, and integrate all 18 Hetzner sites into a unified
**blogbot SEO/AEO system** with native site theming.

## Architecture (3-Repo Plan)

```
1. COURSES REPO          (this repo: mathsdoomscrolling)
   - EPITA_Moodle_Notes_MD/S      ← Moodle exports (source, never modified)
   - md_to_cards.py               ← 4-pass pipeline (A/B/C/D)
   - app.py                       ← Flask app, parse_blocks(), card DB
   - tests/test_md_to_cards.py    ← 62 tests (all pass)
   - README_md_to_cards.md        ← Pipeline docs + pricing + Pass C v2

2. CARD MAPPING REPO     (Hetzner: /opt/pierref/mathsdoomscroll/)
   - cards.db                     ← SQLite: 3,486 cards (COURSE + QCM + TF)
   - Generated_QCMs/              ← 304 generated .txt files (268 COURSE + 30 QCM/TF)
   - selected_courses.json        ← Category resolution
   - md_to_cards_progress.json    ← Pass tracker

3. COVERAGE AUDIT REPO   (Hetzner: /opt/pierref/blogbot/)
   - blogbot/                     ← Daily batch generation
   - /opt/pierref/blog/{site}/    ← 18 site blog directories
   - sites.json                   ← 22 discovered sites with themes
   - daily_batch.py               ← Multi-site batch pipeline
   - html_renderer.py             ← THEME_STYLES per site (11 themes)
   - prompt_engine.py             ← Site-specific AEO/SEO prompts
```

## Card Pipeline — 4 Passes

| Pass | Mode | Tokens | Output |
|---|---|---|---|
| A | Normalization | 0 | `[mathjaxinline]X[/mathjaxinline]` → `$X$`, `[mathjax]X[/mathjax]` → `$$X$$` |
| B | Deterministic QCM | 0 | QCM at full score only (note pleine = correct answers) |
| C | LLM COURSE generation | Paid | One COURSE card per chapter (theory, LaTeX, definitions) |
| **D** | **LLM QCM/TF generation** | **Paid** | **Conceptual QCM/TF for chapters lacking practice questions** |

### Pass D — QCM d'entraînement (new)

Generates **conceptual understanding questions** (not simple computation):

- **QCM format**: 4 choices, 1 correct — questions require reasoning/application/analysis
- **TF format**: True/False with `A: vrai` or `A: faux`
- **Key rule**: No "compute PGCD of 12342" — instead "Why is PGCD invariant under Euclidean division?"
- Uses `SYSTEM_PROMPT_QCM` with difficulty guidance
- Same rotation/429/fallback/verification as Pass C
- CLI: `make md-cards-d`, `make md-cards-d-limited`
- Tracker: `GENERATED_QCM` status in `md_to_cards_progress.json`

### Model Strategy

```
Generation: 1 model per chapter (rotation)
  open-mistral-nemo-2407 → mistral-small-latest → mistral-medium-latest
  (only nemo works reliably on "Experiment" tier; others return HTTP 400)

Verification: distinct model (DEFAULT_VERIFY_MODEL)
  Batch verify entire chapter in one call
  Advisory only — parse_blocks() is authoritative
```

### Rate Limiting Rules

- 429 → fallback to next model in rotation (max 2 fallbacks)
- All models 429 → `RateLimitError` → checkpoint `FAILED` (resume with `--retry-failed`)
- No retry loops: 429 = change model OR checkpoint
- 0.5s safe delay (60% of public limits)
- Multi-key rotation: `MISTRAL_API_KEY_2` (priority) + `MISTRAL_API_KEY`

### Budget

- Constraint: <€4 total for LLM generation
- Actual cost Pass C: ~€0.16 (268 chapters)
- Pass D estimate: ~€0.20-0.50 (selective, limited by `--pass-d-limit`)

## Blogbot Integration (18 Sites)

### Site Discovery

The `server_scanner.py` auto-discovers all directories under `/opt/pierref/`,
generates `BRAND_PRESETS` entries with per-site identity, and produces `sites.json`.

### Themes (`html_renderer.py` THEME_STYLES)

| Site | Theme | Status |
|---|---|---|
| opticars | opticars | Native |
| musicator | musicator | Native |
| streetsraces | streetsraces | Native |
| matchshot | matchshot | Native |
| larchitectweb | larchitect | Native |
| pepexator | pepexator | Native |
| focusator | focusator | New theme |
| lbcstudio | lbcstudio | New theme |
| salepute | salepute | New theme |
| wclproject | wclproject | New theme |
| dodomailator | dodomailator | New theme |
| mathsdoomscrolling | mathsdoomscrolling | New theme |
| shareperprojet | generic | Fallback |
| mailer | generic | Fallback |
| humanizator | generic | Fallback |
| aurigagcalsync | generic | Fallback |
| creepita | generic | Fallback |
| landing | generic | Fallback |

### Content Generation

- `daily_batch.py` runs `generate_article_for_site()` for each site in `PRIMARY_UTILITY_SITES`
- Site-specific `TOPICS_MATRIX` provides 5 SEO topics per site
- `prompt_engine.py` builds system/user prompts with `site_config` (brand name, utility, domain, CTA)
- `html_renderer.py` applies per-site theme CSS to rendered HTML
- Output goes to `/opt/pierref/blog/{site_id}/fr/`
