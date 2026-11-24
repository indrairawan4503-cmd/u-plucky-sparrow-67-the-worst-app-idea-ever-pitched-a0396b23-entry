#!/usr/bin/env python3
"""SmallTalkr — the performance-review platform for elevator small talk.

Writes the one-sentence entry to /output/entry.txt first (the grader
sandbox mounts the repo read-only, so the repo-root copy is best-effort
only and must never crash the run).
"""

import os

ENTRY = (
    "SmallTalkr grades every neighbour's elevator small talk against "
    "building-wide benchmarks and emails quarterly feedback and a formal "
    "improvement plan when their chit-chat plateaus, because unsupervised "
    "small talk is how buildings fall apart."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        pass


if __name__ == "__main__":
    main()
