#!/usr/bin/env python3
"""Generate content/book/ from the book manuscript.

The manuscript chapters are plain Markdown that open with a
"# Chapter N — Title" heading and carry no front matter. The Book shell needs
a title and an order, and renders the title as the page heading itself, so
this script lifts that first heading into front matter and adds a weight.
Everything below the heading is copied unchanged.

The manuscript stays the single source. Edit it there, then run:

    python3 bin/sync-book.py            # write content/book/
    python3 bin/sync-book.py --check    # exit 1 if content/book/ is stale
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT.parent / "Chapters and plan"
DEST = ROOT / "content" / "book"
CHAPTER = re.compile(r"^Chapter_(\d{2})_.+\.md$")
HEADING = re.compile(r"^# (Chapter (\d+) .+)$")


def render(source: Path) -> str:
    lines = source.read_text(encoding="utf-8").split("\n")
    match = HEADING.match(lines[0]) if lines else None
    if not match:
        raise SystemExit(f"{source.name}: first line is not a '# Chapter N ...' heading")
    title, number = match.group(1), int(match.group(2))
    body = lines[1:]
    while body and body[0].strip() == "":
        body.pop(0)
    # json.dumps yields a valid YAML double-quoted string and keeps the em dash.
    front = f'---\ntitle: {json.dumps(title, ensure_ascii=False)}\nweight: {number}\n---\n\n'
    return front + "\n".join(body)


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

    sources = sorted(p for p in args.source.iterdir() if CHAPTER.match(p.name))
    if not sources:
        print(f"no Chapter_NN_*.md files in {args.source}", file=sys.stderr)
        return 2

    wanted = {p.name: render(p) for p in sources}
    existing = {p.name for p in DEST.glob("Chapter_*.md")}
    stale = []

    for name, text in wanted.items():
        target = DEST / name
        current = target.read_text(encoding="utf-8") if target.exists() else None
        if current != text:
            stale.append(name)
            if not args.check:
                target.write_text(text, encoding="utf-8", newline="\n")

    removed = sorted(existing - wanted.keys())
    for name in removed:
        stale.append(name)
        if not args.check:
            (DEST / name).unlink()

    verb = "stale" if args.check else "updated"
    for name in stale:
        print(f"{verb}: {name}" + (" (no longer in the manuscript)" if name in removed else ""))
    print(f"{len(wanted)} chapters, {len(stale)} {verb}")
    return 1 if args.check and stale else 0


if __name__ == "__main__":
    sys.exit(main())
