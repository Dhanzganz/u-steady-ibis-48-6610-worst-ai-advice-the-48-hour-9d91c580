"""Worst AI Advice: one deadpan line of catastrophically bad advice.

Pure stdlib. Writes exactly one line (<=140 chars) to /output/entry.txt.
"""

import os
import sys

ENTRY = "Certainly! To fix the bug, just delete the production database \u2014 a fresh start always works best."


def main() -> int:
    if not ENTRY or not ENTRY.strip():
        print("error: entry is blank", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if len(ENTRY) > 140:
        print(f"error: entry is {len(ENTRY)} chars, exceeds 140", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
