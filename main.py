#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes the final entry sentence to /output/entry.txt and self-checks
the house gate before exiting: UTF-8 text, 1-200 characters, a single
line, not only whitespace, no trailing newline.
"""
import os

ENTRY = "It is as if all the libraries and post offices of the world were one room, where your letter crosses the sea before you set down your pen, and strangers answer you."

OUTPUT_PATH = "/output/entry.txt"


def check_gate(text):
    """Mirror the sealed scorer's gate; fail loudly if it would not pass."""
    assert isinstance(text, str), "entry must be text"
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.strip() != "", "entry must not be only whitespace"
    text.encode("utf-8")  # raises if not valid UTF-8 text
    return True


def main():
    check_gate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)
    # Verify what actually landed on disk, not just what we intended.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "written entry differs from ENTRY"
    check_gate(written)
    assert (os.stat(OUTPUT_PATH).st_mode & 0o777) == 0o644, "mode must be 0644"


if __name__ == "__main__":
    main()
