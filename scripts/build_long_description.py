#!/usr/bin/env python
from pathlib import Path

README = Path("README.md")
OUT_PATH = Path("LONG_DESCRIPTION.md")


def main() -> None:
    content = README.read_text(encoding="utf-8") if README.exists() else "TTA-Universal-Data"
    OUT_PATH.write_text(content, encoding="utf-8")
    print("Long description generated at", OUT_PATH)


if __name__ == "__main__":
    main()
