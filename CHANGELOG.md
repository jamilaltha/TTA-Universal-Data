# Changelog

All notable changes to D10Z-TTA will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- CMB analysis module
- JWST early galaxy validation
- Gravitational wave predictions
- Integration with astropy

## [2.0.0] - 2025-12-08

### Added
- Neuro optional extra (`pip install d10z[neuro]`) that pulls in `morphopy>=0.7.5` for neuron-scale morphology analysis

### Changed
- Bumped package version to 2.0.0 to align with the latest PyPI release

## [0.1.0] - 2025-11-29

### Added
- Initial release of D10Z-TTA framework
- Core module with PointZero, Theory, and ReconciliationProtocol
- Sahana Law implementation (coherence dynamics)
- Isis Law implementation (harmonic resonance)
- SPARC galaxy rotation curve validation
- Hubble tension validation
- Command-line interface (CLI)
- Statistical metrics module
- Data loading utilities
- Comprehensive test suite
- GitHub Actions CI/CD pipelines
- Weekly automated benchmarks vs ΛCDM

### Core Features
- Theory reconciliation through dimensional projection analysis
- Fragmentation index calculation (I metric)
- Master equation generation
- Falsifiable prediction generation

### Validation
- TTA rotation curve model
- ΛCDM+NFW comparison model
- D10Z Hubble evolution model
- R², χ², AIC, BIC metrics

### Documentation
- README with quick start guide
- API documentation
- Mathematical framework description
- CHLL-D10Z license

## [0.0.1] - 2025-11-26

### Added
- Project initialization
- Basic framework structure
- Preliminary equations

---

## Version Naming Convention

- **Major version (X.0.0)**: Breaking changes, paradigm shifts
- **Minor version (0.X.0)**: New features, validations, theories
- **Patch version (0.0.X)**: Bug fixes, documentation updates

## Links

- [PyPI](https://pypi.org/project/d10z/)
- [GitHub](https://github.com/jamilaltha/d10z)
- [Documentation](https://d10z.readthedocs.io)
