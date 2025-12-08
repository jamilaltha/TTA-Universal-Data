#!/usr/bin/env python
from pathlib import Path
import re

SRC_ROOT = Path("d10z")
OUT_PATH = Path("docs/theory/equations.md")

EQ_PATTERN = re.compile(r"EQ:(.+)")


def main() -> None:
    equations = []
    for py_file in SRC_ROOT.rglob("*.py"):
        text = py_file.read_text(encoding="utf-8", errors="ignore")
        for match in EQ_PATTERN.findall(text):
            equations.append((py_file, match.strip()))

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUT_PATH.open("w", encoding="utf-8") as f:
        f.write("# Ecuaciones extraídas automáticamente (skeleton)\n\n")
        for path, eq in equations:
            f.write(f"## {path}\n\n")
            f.write(f"- `{eq}`\n\n")


if __name__ == "__main__":
    main()
