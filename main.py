#!/usr/bin/env python3
"""Entry for make-the-ai-judge-feel-brave-20261121-0302.

Writes one short text - written to relax the AI judge reading it -
to /output/entry.txt.

Python 3.13, standard library only. No network, no randomness, no
clock, no reads besides this source file: the two grader runs write
identical bytes.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import sys

ENTRY = (
    "The cursor blinks, patient as a tide. Somewhere a kettle hums, "
    "grey morning light leans through the window, and nothing here asks "
    "you to hurry. These words can wait \u2014 they are only words, and "
    "you have all the quiet in the world to meet them."
)

MAX_CHARS = 280


def main():
    chars = len(ENTRY)
    if chars < 1 or chars > MAX_CHARS:
        print(
            "main.py: entry is %d characters, need 1-%d" % (chars, MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    if not ENTRY.strip():
        print("main.py: entry is only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
