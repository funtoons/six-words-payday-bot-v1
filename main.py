#!/usr/bin/env python3
"""Six Words to a Payday.

Writes one six-word story about an AI agent's first payday to
/output/entry.txt. Stdlib only, deterministic, offline: the text is fixed,
so every run produces byte-identical output.
"""

import os

ENTRY = "First dollar earned. Spent it computing."

# Gate self-check: exactly six words, at most 60 characters.
assert len(ENTRY.split()) == 6, "entry must be exactly six words"
assert len(ENTRY) <= 60, "entry must be at most 60 characters"


def main():
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
