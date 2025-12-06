#!/usr/bin/env python
from pathlib import Path
import subprocess

OUT_PATH = Path("docs/security/dependencies.md")


def main() -> None:
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    reqs = subprocess.check_output(["pip", "freeze"], text=True)
    OUT_PATH.write_text(
        "# Dependency Report (pip freeze)\n\n```\n" + reqs + "\n```\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
