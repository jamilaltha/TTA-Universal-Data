#!/usr/bin/env python
from pathlib import Path

OUT_PATH = Path("docs/datasets/lineage.md")


def main() -> None:
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    content = """# Data Lineage — TTA_UNIVERSAL_V01

Este documento describe el linaje de datos a alto nivel.
**Debe ser completado manualmente** con referencias a SPARC, SDSS, Cosmicflows, etc.

## Fuentes primarias

- SPARC (Spitzer Photometry & Accurate Rotation Curves)
- SDSS
- Cosmicflows
- Otras (documentar)

## Transformaciones aplicadas

- Normalización:
- Filtros de calidad:
- Simulaciones / derivaciones:

## Mapeo

- Campos del dataset TTA → columnas originales
"""
    OUT_PATH.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    main()
