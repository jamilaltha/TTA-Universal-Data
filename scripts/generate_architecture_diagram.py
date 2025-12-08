#!/usr/bin/env python
from pathlib import Path

OUT_PATH = Path("docs/architecture/diagram.txt")


def main() -> None:
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(
        OUT_PATH.read_text(encoding="utf-8") if OUT_PATH.exists() else "Architecture diagram placeholder\n",
        encoding="utf-8",
    )
    print(f"Architecture diagram ensured at {OUT_PATH}")


if __name__ == "__main__":
    main()
