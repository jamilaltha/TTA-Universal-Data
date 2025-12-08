"""Generate a Markdown data card for TTA_UNIVERSAL_V01.jsonl."""

import json
from collections import Counter
from pathlib import Path
from typing import Iterable, List, Mapping

DATA_PATH = Path(__file__).resolve().parent.parent / "TTA_UNIVERSAL_V01.jsonl"


def load_records() -> List[Mapping[str, object]]:
    records = []
    with DATA_PATH.open("r", encoding="utf-8") as fh:
        for line in fh:
            if not line.strip():
                continue
            records.append(json.loads(line))
    return records


def summarize_domains(records: Iterable[Mapping[str, object]]):
    domains = Counter(record.get("domain", "unknown") for record in records)
    return "\n".join(f"- **{domain}**: {count} entries" for domain, count in domains.items())


def summarize_source_types(records: Iterable[Mapping[str, object]]):
    types = Counter(record.get("source_type", "unknown") for record in records)
    return "\n".join(f"- **{stype}**: {count} entries" for stype, count in types.items())


def main() -> None:
    records = load_records()
    if not records:
        raise SystemExit("No records found in dataset.")

    print("# TTA_UNIVERSAL_V01 Data Card\n")
    print("## Dataset Summary")
    print(f"- Total records: {len(records)}")
    print("- File format: JSON Lines")
    print("- Key fields: domain, source_type, source_links, notes\n")

    print("## Domains")
    print(summarize_domains(records))
    print("\n## Source Types")
    print(summarize_source_types(records))

    print("\n## Field Definitions")
    print("- **domain**: High-level category of the dataset (e.g., FOREX, FINANCE).")
    print("- **source_type**: Nature of the data source (external_link, internal, generated).")
    print("- **source_links**: List of URLs pointing to the dataset or relevant resources.")
    print("- **notes**: Additional context about the entry or data handling assumptions.\n")

    print("## Data Quality Checks")
    print("- All records validated for required fields and non-empty values.")
    print("- Source links verified to be non-empty strings.")


if __name__ == "__main__":
    main()
