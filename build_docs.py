#!/usr/bin/env python3
"""Build index.html (the GitHub Pages site) from site/catalog.html.

    python3 build_docs.py

site/catalog.html is the same file published as a Claude Artifact. The artifact
host wraps it in <!doctype>/<head>/<body> at publish time; GitHub Pages serves
files raw, so this script adds that wrapper itself.

Output goes to the repo root (not docs/) because GitHub Pages here is
configured to deploy from the root of main -- with no root index.html,
Pages silently falls back to rendering README.md via Jekyll instead, which
is invisible until you actually load the site.

Run it after every edit to site/catalog.html. Skipping it means the website
silently serves an older page than the artifact -- which has already happened
once, and is invisible unless you diff them.
"""

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "site" / "catalog.html"
OUT = ROOT / "index.html"

DESCRIPTION = (
    "Learn to build chatbots from level 0 to expert: one story, ten words, "
    "six questions, five traps."
)

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="color-scheme" content="light dark">
<style>*{{box-sizing:border-box}}body{{margin:0}}img{{max-width:100%}}</style>
</head>
<body>
{body}
</body>
</html>
"""


def build() -> int:
    if not SRC.exists():
        print(f"error: {SRC} not found", file=sys.stderr)
        return 1

    src = SRC.read_text()

    match = re.search(r"<title>(.*?)</title>", src, re.S)
    if not match:
        print("error: source has no <title>", file=sys.stderr)
        return 1
    title = match.group(1).strip()

    # The wrapper supplies the title; leaving the original in the body would
    # give the page two.
    body = src.replace(match.group(0), "", 1).lstrip("\n")

    page = TEMPLATE.format(title=title, description=DESCRIPTION, body=body)

    OUT.parent.mkdir(exist_ok=True)
    (OUT.parent / ".nojekyll").touch()   # stop Pages running Jekyll over it
    OUT.write_text(page)

    # Cheap guards against the failure modes that actually bite: a truncated
    # copy, a lost script, or a second <html> from double-wrapping.
    assert page.lower().count("<html") == 1, "double-wrapped"
    assert page.count("<title>") == 1, "duplicate title"
    sections = len(re.findall(r'<section class="page"', page))
    assert sections >= 10, f"only {sections} sections -- source looks truncated"
    assert "<script>" in page, "script block missing"

    print(f"built {OUT.relative_to(ROOT)}  ({len(page):,} bytes, {sections} sections)")
    return 0


if __name__ == "__main__":
    raise SystemExit(build())
