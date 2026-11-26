"""One Line, One Laugh — make.fun entry.

Writes a single funny line (at most 200 characters) to /output/entry.txt,
the artifact the judge compares pairwise against other entries.

Pure standard library only; deterministic: the same line every run.
"""

import os

LINE = (
    "I asked my smart fridge for a joke. It said: "
    "'You open me at 2 a.m. looking for answers. "
    "I contain leftovers, not closure — "
    "and at this hour, neither do you.'"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars, must be 1-200"
    assert line.strip(), "line must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
