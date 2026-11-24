#!/usr/bin/env python3
"""One-Liner Marathon entry: a single deadpan one-line comedy joke.

Writes the joke to /output/entry.txt. Deterministic, stdlib only, no
network access. The output is byte-identical on every run.
"""

import os

JOKE = (
    "My Roomba filed for divorce \u2014 apparently 'cleaning up after me "
    "every day' doesn't count as quality time."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
