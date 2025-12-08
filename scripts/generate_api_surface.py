#!/usr/bin/env python
from pathlib import Path
import pkgutil

PACKAGE = "d10z"
OUT_PATH = Path("d10z/__init__.py")


def main() -> None:
    modules = []
    package_path = Path(PACKAGE)
    for m in pkgutil.walk_packages([str(package_path)], prefix=f"{PACKAGE}."):
        name = m.name
        if not name.endswith(".__main__"):
            modules.append(name)

    lines = [
        '"""API pública estable del paquete d10z.\n\n',
        "Este archivo es autogenerado como skeleton y puede ser editado.\n",
        '"""\n\n',
        "__all__ = [\n",
    ]
    for m in sorted(modules):
        lines.append(f'    "{m}",\n')
    lines.append("]\n")

    OUT_PATH.write_text("".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
