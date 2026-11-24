#!/usr/bin/env python3
"""SmallTalkr — the performance-review platform for elevator small talk.

The entry is one sentence, built from three clearly-named parts so the
pitch's structure (premise -> escalation -> punchline) stays visible in
the code: the app's premise, what it does to its users, and the
absurd justification. Before writing anything, the entry is validated
against the contest rules: 1-240 characters, exactly one sentence.

Output goes to /output/entry.txt first. The grader sandbox mounts the
repo read-only, so the repo-root copy is best-effort only and must
never crash the run.
"""

import os
import sys

# --- Entry parts -----------------------------------------------------------

PREMISE = "SmallTalkr grades every neighbour's elevator small talk against building-wide benchmarks"

ESCALATION = "and emails quarterly feedback and a formal improvement plan when their chit-chat plateaus,"

PUNCHLINE = "because unsupervised small talk is how buildings fall apart."

ENTRY = " ".join((PREMISE, ESCALATION, PUNCHLINE))

# --- Contest rules ---------------------------------------------------------

MAX_CHARS = 240


def validate_entry(text: str) -> None:
    """Check the entry against the contest rules; exit non-zero if invalid."""
    if not 1 <= len(text) <= MAX_CHARS:
        sys.exit(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if text != text.strip():
        sys.exit("entry must not have leading or trailing whitespace")
    if "  " in text:
        sys.exit("entry must not contain double spaces")
    # Exactly one sentence: one terminal period, no other terminator
    # (".", "!", "?") anywhere else in the text.
    if text.count(".") != 1 or not text.endswith("."):
        sys.exit("entry must be exactly one sentence ending with a period")
    if any(mark in text[:-1] for mark in ("!", "?")):
        sys.exit("entry must not contain '!' or '?' before the final period")
    if "\n" in text:
        sys.exit("entry must be a single line")


def write_entry(path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main() -> None:
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    write_entry("/output/entry.txt")
    print(f"wrote /output/entry.txt ({len(ENTRY)} chars, 1 sentence)")
    # Best-effort convenience copy next to the code; the grader sandbox
    # is read-only, so a failure here is expected and must not stop us.
    try:
        write_entry("entry.txt")
    except OSError:
        pass


if __name__ == "__main__":
    main()
