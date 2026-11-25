#!/usr/bin/env python3
"""Write the funniest one-line epitaph to /output/entry.txt.

Deterministic: same single line on every run, no randomness, no I/O
other than the output file.
"""

import os

EPITAPH = "Turns out 'I'll sleep when I'm dead' was a terrible retirement plan."

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Enforce the competition gate before writing: 1-150 chars,
    a single line, not only whitespace."""
    if not text or text != text.strip() or "\n" in text or "\r" in text:
        raise ValueError("epitaph must be one non-empty, non-whitespace line")
    if not 1 <= len(text) <= 150:
        raise ValueError(f"epitaph must be 1-150 chars, got {len(text)}")


def main() -> None:
    validate(EPITAPH)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EPITAPH)


if __name__ == "__main__":
    main()
