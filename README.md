# The Chatbot Catalog

An interactive, single-page guide to building and understanding chatbots — one story, ten
words, six questions, five traps, and 20 drawers covering RAG, agents, context engineering,
evaluation, safety, the frontend, infra/deployment, and running one in production.

**Live:** hosted via GitHub Pages from [`docs/index.html`](docs/index.html).

## Files

| File | What it is |
|---|---|
| [site/catalog.html](site/catalog.html) | Source. Edit this. |
| [docs/index.html](docs/index.html) | Built output, served by GitHub Pages. |
| [build_docs.py](build_docs.py) | Rebuilds `docs/index.html` from `site/catalog.html`. Run it after every edit to the source. |

```bash
python3 build_docs.py
```
