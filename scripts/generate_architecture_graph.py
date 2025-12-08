#!/usr/bin/env python
from pathlib import Path

OUT_PATH = Path("docs/architecture/diagram.dot")


def main() -> None:
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    content = OUT_PATH.read_text(encoding="utf-8") if OUT_PATH.exists() else "digraph G {}\n"
    OUT_PATH.write_text(content, encoding="utf-8")
    print(f"Architecture graph ensured at {OUT_PATH}")


if __name__ == "__main__":
    main()
