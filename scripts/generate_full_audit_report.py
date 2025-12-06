#!/usr/bin/env python
from pathlib import Path
import subprocess

OUT_PATH = Path("AUDIT_REPORT.md")


def run(cmd: list[str]) -> str:
    return subprocess.check_output(cmd, text=True, errors="ignore")


def main() -> None:
    sections = []

    sections.append("# TTA-Universal-Data — Audit Report (Skeleton)\n")

    sections.append("## Git status\n")
    sections.append("```bash\n" + run(["git", "status", "-sb"]) + "```\n")

    sections.append("## Últimos commits\n")
    sections.append("```bash\n" + run(["git", "log", "-5", "--oneline"]) + "```\n")

    sections.append("## Árbol del proyecto\n")
    try:
        tree = run(["tree", "-L", "3"])
    except Exception:
        tree = "Instala 'tree' para ver este apartado."
    sections.append("```text\n" + tree + "\n```\n")

    OUT_PATH.write_text("\n".join(sections), encoding="utf-8")


if __name__ == "__main__":
    main()
