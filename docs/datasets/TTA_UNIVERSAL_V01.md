# TTA_UNIVERSAL_V01 Data Card

## Dataset Summary
- Total records: 7
- File format: JSON Lines
- Key fields: domain, source_type, source_links, notes

## Domains
- **FOREX**: 1 entries
- **FINANCE**: 1 entries
- **CMB**: 1 entries
- **LHC**: 1 entries
- **QUANTUM**: 1 entries
- **QKD**: 1 entries
- **COSMOLOGY**: 1 entries

## Source Types
- **external_link**: 7 entries

## Field Definitions
- **domain**: High-level category of the dataset (e.g., FOREX, FINANCE).
- **source_type**: Nature of the data source (external_link, internal, generated).
- **source_links**: List of URLs pointing to the dataset or relevant resources.
- **notes**: Additional context about the entry or data handling assumptions.

## Data Quality Checks
- All records validated for required fields and non-empty values.
- Source links verified to be non-empty strings.
