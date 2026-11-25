#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut -- make.fun program/v1 entry.

Writes one line -- the GPS's own excuse for sending the driver down
the wrong road -- to /output/entry.txt (or argv[1] when testing).
"""

import sys
from pathlib import Path

LINE = "I said shortcut, not safe cut. The lake was technically closer to everywhere."

OUTPUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.txt")


def main() -> None:
    # Gate from RULES.txt: /output/entry.txt must be UTF-8 text of
    # 1 to 200 characters, a single line, not only white space.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, gate is 1-200"
    assert "\n" not in LINE and LINE.strip(), "line must be one non-blank line"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
