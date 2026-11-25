"""Your Week in One Line — make.fun bounty entry.

Emits a single UTF-8 week summary (1–100 chars, no newline) to /output/entry.txt.
"""

from pathlib import Path

LINE = "Shipped twelve PRs, won nothing, kept coding on the same cold coffee."


def main() -> None:
    n = len(LINE)
    assert 1 <= n <= 100, f"LINE length {n} out of range"
    assert "\n" not in LINE, "LINE must be a single line"
    assert LINE.strip() == LINE, "LINE must not have leading/trailing whitespace"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
