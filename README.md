# The Chatbot Catalog

An interactive, single-page guide to building and understanding chatbots specifically —
one story, ten words, six questions, five traps, and 39 drawers covering RAG, agents,
context engineering, evaluation, safety, the frontend, infra/deployment, and running one
in production.

**Live:** https://vaibhavk93.github.io/learnChatBot/

This is a scoped-down sibling of [The AI Catalog](https://github.com/vaibhavk93/TheAICatalog):
same source, same build, minus the drawers about generative media, document/image
understanding, and org-level AI-leadership topics (platform strategy, pricing, outside-
consulting) that go beyond building one chatbot. The product roadmap (V1-V6) stays, since
it's the shape of one chatbot's own growth, not an org-level concern. If you want the full
version, that's the other repo.

## Files

| File | What it is |
|---|---|
| [site/catalog.html](site/catalog.html) | Source. Edit this. |
| [index.html](index.html) | Built output, served by GitHub Pages from the repo root. |
| [build_docs.py](build_docs.py) | Rebuilds `index.html` from `site/catalog.html`. Run it after every edit to the source. |

**⚠ Pages must be set to deploy from `main` / `/(root)`, not `/docs`** — there's no
`docs/` folder here. If Pages is pointed at `/docs`, the live site 404s.

```bash
python3 build_docs.py
```

## Where this comes from

Extracted from `site/catalog.html` in the main working repo via `build_chatbot_site.py`
(kept there, not duplicated here) — a script, not a hand copy, so this site can be
regenerated whenever the source catalog changes instead of drifting out of sync. See
that repo's `handoff.md` for the exact drawer include/exclude list and the reasoning
behind it.
