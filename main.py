"""The Worst Pizza Topping — one funny line pitching a terrible pizza topping.

Writes the entry line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

LINE = "New on the menu: a pizza topped with your ex's apologies \u2014 cold, hard to swallow, and it shows up uninvited every Friday."


def validate(text: str) -> None:
    """Mirror the bounty gate: UTF-8 text, 1-200 chars, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    text.encode("utf-8")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    validate(LINE)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back what we wrote and confirm it is byte-identical to LINE,
    # so a silent write failure can never slip through as a valid entry.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("read-back mismatch: entry.txt does not match LINE")
    print(f"wrote {len(LINE)} chars to {path} (read-back verified)")


if __name__ == "__main__":
    main()
