"""Entry for make.fun competition: u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270.

Running this program writes the entry tip to /output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

OPENING = "Tip: The bug is not in the library. It's in the line you wrote "
MIDDLE = "at 2am and labeled 'temporary.' It has tenure now, "
LANDING = "a parking spot, and opinions about your roadmap."

ENTRY = OPENING + MIDDLE + LANDING


def write_entry(text: str, path: Path) -> None:
    """Write *text* to *path* as UTF-8, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    """Write the entry tip to the fixed output path."""
    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()
