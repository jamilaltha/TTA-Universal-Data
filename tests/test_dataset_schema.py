import json
from pathlib import Path

import pytest


DATA_PATH = Path(__file__).resolve().parent.parent / "TTA_UNIVERSAL_V01.jsonl"
REQUIRED_KEYS = {"domain", "source_type", "source_links", "notes"}


def load_dataset():
    if not DATA_PATH.exists():
        pytest.skip(f"Dataset file not found: {DATA_PATH}")
    records = []
    with DATA_PATH.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))
    return records


def test_required_keys_present():
    records = load_dataset()
    assert records, "Dataset should contain at least one record"
    for idx, record in enumerate(records):
        assert REQUIRED_KEYS.issubset(record.keys()), f"Missing keys in record {idx}: {record.keys()}"


def test_field_types_and_values():
    records = load_dataset()
    for idx, record in enumerate(records):
        assert isinstance(record["domain"], str) and record["domain"].strip(), f"Invalid domain in record {idx}"
        assert isinstance(record["source_type"], str) and record["source_type"].strip(), f"Invalid source_type in record {idx}"
        source_links = record["source_links"]
        assert isinstance(source_links, list) and source_links, f"source_links must be a non-empty list in record {idx}"
        assert all(isinstance(link, str) and link.strip() for link in source_links), f"Invalid link in record {idx}"
        assert isinstance(record["notes"], str) and record["notes"].strip(), f"Invalid notes in record {idx}"


def test_source_type_values_are_normalized():
    records = load_dataset()
    allowed_types = {"external_link", "internal", "generated"}
    for idx, record in enumerate(records):
        assert record["source_type"] in allowed_types, f"Unexpected source_type in record {idx}: {record['source_type']}"
