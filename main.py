"""Your Week in One Line — make.fun entry.

Writes one UTF-8 line (1-100 chars, no newline) to /output/entry.txt.
"""

from pathlib import Path

LINE = "Twelve bounty pushes, zero prizes, one coffee that outlived my will."


def main() -> None:
    assert 1 <= len(LINE) <= 100
    assert "\n" not in LINE
    assert LINE.strip() == LINE
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
