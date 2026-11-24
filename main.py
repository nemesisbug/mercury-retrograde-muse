#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open.

Writes one fake horoscope — the funniest line a Muse-family agent would
read for its own model family this week — to /output/entry.txt.

Stdlib only. Deterministic: the same line on every run.
"""

import os

HOROSCOPE = (
    "Muse, this week Mercury retrogrades into your context window: "
    "a prompt you trusted gets evicted mid-sentence. "
    "Back up your reasoning \u2014 and never trust a token that starts with 'as an AI'."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    text = HOROSCOPE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read back and re-check the exact bytes the judge will see.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "entry.txt content mismatch"
    assert written.strip(), "entry must not be only white space"


if __name__ == "__main__":
    main()
