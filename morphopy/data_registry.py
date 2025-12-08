from __future__ import annotations

import json
from dataclasses import dataclass
from importlib import resources
from typing import List


@dataclass(frozen=True)
class DatasetEntry:
    """Metadata for a MorphoPy dataset."""

    id: int
    slug: str
    name: str
    scale: str
    status: str
    metric: str
    sample_file: str
    description: str

    @property
    def download_name(self) -> str:
        """Return the default filename used when downloading the dataset."""

        return f"{self.slug}.csv"


def _load_registry() -> List[DatasetEntry]:
    with resources.open_text("morphopy.data", "registry.json", encoding="utf-8") as fp:
        raw = json.load(fp)
    return [DatasetEntry(**entry) for entry in raw]


DATASETS: List[DatasetEntry] = _load_registry()


def list_datasets() -> List[DatasetEntry]:
    """Return all dataset entries sorted by ID."""

    return sorted(DATASETS, key=lambda entry: entry.id)


def get_dataset(identifier: str | int) -> DatasetEntry:
    """Lookup a dataset by its numeric ID or slug."""

    for entry in DATASETS:
        if entry.id == identifier or entry.slug == identifier:
            return entry
    raise KeyError(f"Dataset '{identifier}' not found in registry")
