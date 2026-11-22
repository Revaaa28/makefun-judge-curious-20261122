#!/usr/bin/env python3
"""Make the AI judge feel curious — entry generator.

Writes the 240-character curiosity text to /output/entry.txt (UTF-8,
no trailing newline).
"""

TEXT = (
    "A book came back to the library this winter,\n"
    "forty years out, its card still in the pocket.\n"
    "No fine was paid. No name was left.\n"
    "\n"
    "But the last page, blank since printing,\n"
    "is now full of handwriting,\n"
    "and it begins in the middle of a sentence."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
