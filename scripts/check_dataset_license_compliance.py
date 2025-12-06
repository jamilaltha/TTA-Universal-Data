"""Lightweight dataset license compliance scanner."""
import json
from pathlib import Path


REQUIRED_LICENSE_FIELDS = {"license", "source"}


def scan_record(record):
    missing = REQUIRED_LICENSE_FIELDS - set(record.keys())
    return list(missing)


def main():
    dataset = Path("TTA_UNIVERSAL_V01.jsonl")
    if not dataset.exists():
        print("Dataset file TTA_UNIVERSAL_V01.jsonl not found; skipping scan.")
        return
    issues = []
    for line_no, line in enumerate(dataset.read_text().splitlines(), start=1):
        record = json.loads(line)
        missing = scan_record(record)
        if missing:
            issues.append((line_no, missing))
    if not issues:
        print("All records include required license metadata.")
    else:
        print("License compliance issues detected:")
        for line_no, missing in issues[:20]:
            print(f"- Line {line_no}: missing fields {missing}")


if __name__ == "__main__":
    main()
