#!/usr/bin/env python
import json
from pathlib import Path
from collections import Counter

DATA_PATH = Path("data/TTA_UNIVERSAL_V01.jsonl")
OUT_PATH = Path("docs/datasets/TTA_UNIVERSAL_V01_datacard.md")


def infer_schema(max_lines: int = 1000) -> dict:
    keys_counter: Counter[str] = Counter()
    types_map: dict[str, Counter[str]] = {}

    with DATA_PATH.open("r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i >= max_lines:
                break
            obj = json.loads(line)
            for k, v in obj.items():
                keys_counter[k] += 1
                t = type(v).__name__
                types_map.setdefault(k, Counter())[t] += 1

    schema = {}
    for k in keys_counter:
        schema[k] = {
            "seen": keys_counter[k],
            "types": dict(types_map.get(k, {})),
        }
    return schema


def main() -> None:
    schema = infer_schema()
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with OUT_PATH.open("w", encoding="utf-8") as f:
        f.write("# TTA_UNIVERSAL_V01 — Data Card (Auto-Generated Skeleton)\n\n")
        f.write("Este archivo es un boceto generado automáticamente. Debe ser editado a mano.\n\n")
        f.write("## Esquema inferido (primeras N filas)\n\n")
        for k, meta in schema.items():
            f.write(f"### Campo: `{k}`\n")
            f.write(f"- Registros donde aparece: {meta['seen']}\n")
            f.write(f"- Tipos detectados: {meta['types']}\n\n")


if __name__ == "__main__":
    main()
