#!/usr/bin/env python3
"""Generate the book pages from the book manuscript.

The manuscript stays the single source. This script writes three things:

- content/book/: one page per chapter. The manuscript chapters open with a
  "# Title" heading and carry no front matter. The Book shell renders the
  title as the page heading itself, so the first heading is lifted into
  front matter. The chapter number comes from the filename (Chapter_NN_...)
  and becomes the page's weight and its book_number, which the theme shows
  beside the title. Everything below the heading is copied unchanged.
- content/topics/_index.md: the learning topics from learning-topics.md, with
  each numbered topic as a heading carrying a stable {#topic-N} anchor that
  the home page links to. The manuscript's planning preface is not copied.
- content/slides/NN-name/index.md: one lecture deck per slides/NN-name.md,
  copied unchanged. Each deck carries its own front matter, and its slides are
  separated by --- lines; layouts/slides/page.html presents them.

Edit the manuscript, then run:

    python3 bin/sync-book.py            # write the generated pages
    python3 bin/sync-book.py --check    # exit 1 if any generated page is stale
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT.parent / "Chapters and plan"
BOOK = ROOT / "content" / "book"
TOPICS = ROOT / "content" / "topics" / "_index.md"
TOPICS_SOURCE = "learning-topics.md"
SLIDES = ROOT / "content" / "slides"
SLIDES_SOURCE = "slides"
CHAPTER = re.compile(r"^Chapter_(\d{2})_.+\.md$")
DECK = re.compile(r"^\d{2}-[a-z0-9-]+\.md$")
HEADING = re.compile(r"^# (.+)$")
TOPIC = re.compile(r"^(\d+)\. \*\*(.+?)\*\*\s*$")
BULLET = re.compile(r"^\s+\*\s+(.+)$")

TOPICS_FRONT = """---
title: "Learning topics"
description: "The thirty-three topics the book teaches, from how websites work to long-term maintenance."
type: docs
---

These are the topics the book covers. They are not the chapter order: several
chapters touch each topic, and some topics are practised hands-on while others
are explained just enough for you to make informed decisions. The
[learning paths](../paths/) suggest where to start, depending on what you
already know.

"""


def yaml_string(text: str) -> str:
    # json.dumps yields a valid YAML double-quoted string and keeps the em dash.
    return json.dumps(text, ensure_ascii=False)


def render_chapter(source: Path) -> str:
    lines = source.read_text(encoding="utf-8").split("\n")
    match = HEADING.match(lines[0]) if lines else None
    if not match:
        raise SystemExit(f"{source.name}: first line is not a '# Title' heading")
    title = match.group(1).strip()
    number = int(CHAPTER.match(source.name).group(1))
    body = lines[1:]
    while body and body[0].strip() == "":
        body.pop(0)
    front = f"---\ntitle: {yaml_string(title)}\nweight: {number}\nbook_number: {number}\n---\n\n"
    return front + "\n".join(body)


def render_topics(source: Path) -> str:
    out: list[str] = []
    started = False
    for line in source.read_text(encoding="utf-8").split("\n"):
        topic = TOPIC.match(line)
        if topic:
            started = True
            number, title = topic.group(1), topic.group(2)
            if out:
                out.append("")
            out.append(f"## {number}. {title} {{#topic-{number}}}")
            out.append("")
            continue
        bullet = BULLET.match(line)
        if started and bullet:
            out.append(f"- {bullet.group(1)}")
    if not started:
        raise SystemExit(f"{source.name}: no numbered '1. **Topic**' lines found")
    return TOPICS_FRONT + "\n".join(out) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE,
                        help="manuscript folder (default: ../Chapters and plan)")
    parser.add_argument("--check", action="store_true",
                        help="report stale files and exit 1 instead of writing")
    args = parser.parse_args()

    if not args.source.is_dir():
        print(f"manuscript folder not found: {args.source}", file=sys.stderr)
        return 2

    chapters = sorted(p for p in args.source.iterdir() if CHAPTER.match(p.name))
    if not chapters:
        print(f"no Chapter_NN_*.md files in {args.source}", file=sys.stderr)
        return 2
    topics_source = args.source / TOPICS_SOURCE
    if not topics_source.is_file():
        print(f"{TOPICS_SOURCE} not found in {args.source}", file=sys.stderr)
        return 2

    decks_dir = args.source / SLIDES_SOURCE
    decks = sorted(p for p in decks_dir.iterdir() if DECK.match(p.name)) if decks_dir.is_dir() else []

    wanted = {BOOK / p.name: render_chapter(p) for p in chapters}
    wanted[TOPICS] = render_topics(topics_source)
    for deck in decks:
        wanted[SLIDES / deck.stem / "index.md"] = deck.read_text(encoding="utf-8")
    managed = set(BOOK.glob("Chapter_*.md")) | set(SLIDES.glob("*/index.md"))
    removed = sorted(managed - wanted.keys())
    stale = []

    for target, text in wanted.items():
        current = target.read_text(encoding="utf-8") if target.exists() else None
        if current != text:
            stale.append(target)
            if not args.check:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(text, encoding="utf-8", newline="\n")

    for target in removed:
        stale.append(target)
        if not args.check:
            target.unlink()
            if target.parent.parent == SLIDES and not any(target.parent.iterdir()):
                target.parent.rmdir()

    verb = "stale" if args.check else "updated"
    for target in stale:
        note = " (no longer in the manuscript)" if target in removed else ""
        print(f"{verb}: {target.relative_to(ROOT).as_posix()}{note}")
    print(f"{len(chapters)} chapters, the topics page, and {len(decks)} slide decks: {len(stale)} {verb}")
    return 1 if args.check and stale else 0


if __name__ == "__main__":
    sys.exit(main())
