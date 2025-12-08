"""Generate lineage report for TTA dataset."""
import json
import sys
from pathlib import Path


def load_records(path: Path):
    with path.open() as fh:
        return [json.loads(line) for line in fh]


def main():
    if len(sys.argv) < 2:
        raise SystemExit("Usage: generate_lineage.py <jsonl> > docs/datasets/lineage.md")
    source = Path(sys.argv[1])
    records = load_records(source)
    print("# Data Lineage Report")
    print()
    print(f"Source file: {source}")
    print()
    for idx, record in enumerate(records[:50]):
        print(f"## Record {idx}")
        print(f"- Source: {record.get('source', 'unknown')}")
        print(f"- Transformations: {record.get('transforms', [])}")
        print(f"- Dependencies: {record.get('dependencies', [])}")
        print(f"- License: {record.get('license', 'unspecified')}")
        print()


if __name__ == "__main__":
    main()
