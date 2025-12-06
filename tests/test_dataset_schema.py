import json
from pathlib import Path

DATA_PATH = Path("data/TTA_UNIVERSAL_V01.jsonl")


def test_dataset_file_exists() -> None:
    assert DATA_PATH.exists(), "El dataset TTA_UNIVERSAL_V01.jsonl no existe en data/"


def test_dataset_has_valid_json_lines() -> None:
    with DATA_PATH.open("r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i > 1000:
                break
            line = line.strip()
            assert line, f"Línea vacía en registro {i}"
            json.loads(line)  # lanza excepción si está mal
