#!/usr/bin/env python
from pathlib import Path

OUT_PATH = Path("docs/repo_dashboard.md")


def main() -> None:
    OUT_PATH.write_text("# Repo Dashboard (skeleton)\n\nCompletar con métricas y gráficas.\n", encoding="utf-8")
    print(f"Dashboard written to {OUT_PATH}")


if __name__ == "__main__":
    main()
