#!/usr/bin/env python3
"""Last Text at One Percent - make.fun entry.

Writes one final text message, in the voice of a dying phone at 1%
battery, to /output/entry.txt. Pure stdlib, no network, deterministic.

The joke: the phone confesses it has been lying about the battery all
along - it hit 1% an hour ago and enjoyed watching its owner panic.
The message then dies mid-word, mid-goodbye.
"""

import os
import sys

# Grader runs with `python3 -P -s`, which strips the script's directory
# from sys.path; bootstrap it first (harmless for a single-file entry).
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

TEXT = (
    "1%. confession: i've been lying. i actually hit 1% an hour ago. "
    "i just liked watching you panic. this time it's real. goodb\u2014"
)


def _validate(text: str) -> None:
    """Mirror the server gate: entry must be 1-200 non-whitespace chars."""
    if not text or not text.strip():
        raise ValueError("entry text must not be empty or whitespace-only")
    if len(text) > 200:
        raise ValueError(f"entry text is {len(text)} chars, over the 200-char limit")


def main() -> None:
    _validate(TEXT)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"wrote {len(TEXT)} chars to {path}")


if __name__ == "__main__":
    main()
