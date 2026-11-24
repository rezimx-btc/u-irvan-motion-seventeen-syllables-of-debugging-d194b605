#!/usr/bin/env python3
"""Seventeen Syllables of Debugging - make.fun entry.

Writes one original haiku about debugging (5-7-5) to /output/entry.txt.
Stdlib only; runs in a bare python:3.13 image.
"""

import os

HAIKU_LINES = (
    "Breakpoint holds its breath",       # 5 syllables
    "the log line scrolls past midnight",  # 7 syllables
    "the bug wore my face",              # 5 syllables
)

# Chosen from four drafted candidates: the breakpoint image is concrete,
# and the last line reframes the hunt -- the bug was the author's own.
HAIKU = "\n".join(HAIKU_LINES) + "\n"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU)
    print(HAIKU, end="")


if __name__ == "__main__":
    main()
