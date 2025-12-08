"""MorphoPy data connector.

This lightweight package provides metadata for the MorphoPy datasets
and a helper API to download sample files directly from GitHub or a
custom repository. It is designed to be publishable to PyPI so users can
quickly explore the catalog and pull down small test assets.
"""

from .data_registry import DATASETS, DatasetEntry, get_dataset, list_datasets
from .downloader import download_dataset, get_default_base_url

__all__ = [
    "DATASETS",
    "DatasetEntry",
    "list_datasets",
    "get_dataset",
    "download_dataset",
    "get_default_base_url",
]
