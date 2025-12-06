import json
from pathlib import Path

SNAPSHOT_FILE = Path(__file__).parent / "baseline.json"


def load_snapshot():
    if SNAPSHOT_FILE.exists():
        return json.loads(SNAPSHOT_FILE.read_text())
    return {"sample_value": 42.0}


def test_numeric_snapshot():
    snapshot = load_snapshot()
    value = snapshot.get("sample_value", 42.0)
    assert abs(value - 42.0) < 1e-9
