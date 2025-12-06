#!/usr/bin/env python
from pathlib import Path

DATA_PATH = Path("data/TTA_UNIVERSAL_V01.jsonl")


def main() -> None:
    if DATA_PATH.exists():
        print(f"Dataset encontrado en {DATA_PATH}. Verifica la licencia manualmente.")
    else:
        print("Dataset no encontrado; no se puede verificar la licencia.")


if __name__ == "__main__":
    main()
