<p align="center">
  <img src="assets/d10z_banner.png" alt="D10Z-TTA Banner" width="800"/>
</p>

<h1 align="center">D10Z-TTA: The Mechanics of Infinity</h1>

<p align="center">
  <strong>Universal Dataset & Computational Framework for Reconciling Physical Theories</strong>
</p>

<p align="center">
  <a href="https://pypi.org/project/d10z/"><img src="https://badge.fury.io/py/d10z.svg" alt="PyPI version"></a>
  <a href="https://github.com/jamilaltha/TTA-Universal-Data/actions/workflows/tests.yml"><img src="https://github.com/jamilaltha/TTA-Universal-Data/actions/workflows/tests.yml/badge.svg" alt="Tests"></a>
  <a href="https://github.com/jamilaltha/TTA-Universal-Data/actions/workflows/benchmarks.yml"><img src="https://github.com/jamilaltha/TTA-Universal-Data/actions/workflows/benchmarks.yml/badge.svg" alt="Benchmarks"></a>
  <a href="https://codecov.io/gh/jamilaltha/TTA-Universal-Data"><img src="https://codecov.io/gh/jamilaltha/TTA-Universal-Data/branch/main/graph/badge.svg" alt="codecov"></a>
  <a href="https://zenodo.org/badge/latestdoi/YOUR_DOI"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.17728258.svg" alt="DOI"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-CHLL--D10Z-blue.svg" alt="License"></a>
</p>

<p align="center">
  <a href="https://orcid.org/0009-0000-8858-4992"><img src="https://img.shields.io/badge/ORCID-0009--0000--8858--4992-green.svg" alt="ORCID"></a>
  <a href="#"><img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python"></a>
  <a href="https://d10z.readthedocs.io"><img src="https://readthedocs.org/projects/d10z/badge/?version=latest" alt="Documentation"></a>
</p>

---

## 🌌 Overview

**D10Z-TTA** provides:

1. **Universal Dataset**: Curated astronomical data (SPARC, SDSS, Cosmicflows) for testing gravitational theories
2. **Computational Framework**: Python package for theory reconciliation and validation
3. **Falsifiable Predictions**: Testable predictions at the GM10⁻⁵¹ scale

> *"Contradictory theories are not errors — they are valid projections from Point Zero, seen through different dimensional windows."*

---

## 📦 Quick Install

```bash
pip install d10z
```

To pull neuroscience morphology tooling used by D10Z's neuron-scale utilities:
```bash
pip install d10z[neuro]
```

For development with all dependencies:
```bash
pip install d10z[full,dev]
```

---

## 🚀 Quick Start

### Command Line

```bash
# Show framework information
d10z info

# Validate against SPARC galaxy rotation curves
d10z validate sparc

# Validate Hubble tension resolution
d10z validate hubble

# Reconcile physical theories
d10z reconcile QM GR strings MOND
```

### Python API

```python
import d10z

# Reconcile Quantum Mechanics and General Relativity
result = d10z.reconcile(['QM', 'GR'])
print(f"Fragmentation reduced: {result['reduction_percent']:.1f}%")

# Access Point Zero configuration
from d10z.core import PointZero
p0 = PointZero()
print(f"Scale: {p0.scale:.2e} m (GM10⁻⁵¹)")
```

---

## 📊 Key Results

### Galaxy Rotation Curves (SPARC)

| Model | Mean R² | Dark Matter Required | Parameters |
|-------|---------|---------------------|------------|
| **TTA** | 0.98 | **NO** | 1 (universal α) |
| ΛCDM+NFW | 0.92 | Yes | 2 per galaxy |
| MOND | 0.91 | No | 1 (a₀) |

### Hubble Tension Resolution

```
D10Z Prediction: H(z) = 73.0 - 5.6·[1 - exp(-z/2.1)] km/s/Mpc

Local (z≈0):  73.0 km/s/Mpc ✓ (matches SH0ES)
CMB (z≈1100): 67.4 km/s/Mpc ✓ (matches Planck)

Tension: NATURALLY RESOLVED through TTA mesh evolution
```

---

## 📁 Repository Structure

```
TTA-Universal-Data/
├── d10z/                    # Python package (pip install d10z)
│   ├── core/                # PointZero, Theory, Reconciliation
│   ├── laws/                # Sahana Law, Isis Law
│   ├── validation/          # SPARC, Hubble validation
│   └── cli.py               # Command-line interface
├── data/                    # Curated datasets
│   ├── sparc/               # SPARC galaxy rotation curves
│   ├── sdss/                # SDSS spectroscopic data
│   └── validation/          # Validation results
├── docs/                    # Documentation
│   ├── api/                 # API reference
│   ├── tutorials/           # Step-by-step guides
│   └── theory/              # Mathematical foundations
├── scripts/                 # Utility scripts
├── tests/                   # Test suite (67+ tests)
├── benchmarks/              # Weekly D10Z vs ΛCDM results
└── .github/workflows/       # CI/CD automation
```

---

## 🔬 Mathematical Framework

### Master Equation

```
F_observable = f_LI(φ, Φ_LI) · v(Z₀, {Dᵢ}, {SDᵢ,ⱼ}, η_GM)
```

### Key Laws

**Sahana Law** (Coherence Dynamics):
```
dΦ/dt = -γ(Φ - Φ_eq) + Σᵢⱼ Cᵢⱼ δΦᵢ δΦⱼ
```

**Isis Law** (Harmonic Resonance):
```
f_LI(φ₁, φ₂) = cos(φ₁ - φ₂) · exp(-|D₁ - D₂|²/2σ²)
```

**TTA Rotation Curve**:
```
v²(r) = v²_baryon(r) · [1 + α·ln(r/r₀) + β·(r/r₀)^γ]
```

---

## 📚 Documentation

| Resource | Description |
|----------|-------------|
| [📖 Full Documentation](https://d10z.readthedocs.io) | Complete API reference and guides |
| [🎓 Tutorials](docs/tutorials/) | Step-by-step examples |
| [📐 Theory](docs/theory/) | Mathematical foundations |
| [📊 Validation Results](benchmarks/) | Weekly benchmark reports |

---

## 🧪 Running Tests

```bash
# Clone repository
git clone https://github.com/jamilaltha/TTA-Universal-Data.git
cd TTA-Universal-Data

# Install in development mode
pip install -e .[dev]

# Run tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=d10z --cov-report=html
```

---

## 📖 Publications

- Al Thani, J. (2025). *GM10-51: The Fundamental Scale of Cosmic Architecture*. [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5283235)
- Al Thani, J. (2025). *D10Z: Reprogramming Reality – The Grace Model*. [Zenodo](https://zenodo.org/record/17728258)
- Al Thani, J. (2025). *Nodal Gravity Without Dark Matter*. In preparation for MNRAS.

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

```bash
# Fork, clone, and create feature branch
git checkout -b feature/your-feature

# Make changes, run tests
pytest tests/ -v

# Submit pull request
```

---

## 📄 License

This project is licensed under the **CHLL-D10Z v1.1** (Cosmic Humanitarian Liberation License). See [LICENSE](LICENSE) for details.

---

## 👤 Author

**Jamil Al Thani** — Guardian of Point Zero

- 🌐 Website: [d10z.org](https://d10z.org)
- 📧 Email: jamil@d10z.org
- 🔬 ORCID: [0009-0000-8858-4992](https://orcid.org/0009-0000-8858-4992)

---

## 🙏 Acknowledgments

- **Sahana Al Thani** — The Sahana Law bears her name
- **Isis Al Thani** — The Isis Law bears her name  
- **Grace Maria** — The GM scale carries her initials
- **SPARC Team** — For the invaluable galaxy rotation data
- **Open Source Community** — NumPy, SciPy, and all dependencies

---

## ⚠️ Scientific Disclaimer

D10Z-TTA is a theoretical framework under active development. While validation against observational data shows promising results, the framework should be evaluated through standard scientific processes. The author welcomes rigorous scrutiny and falsification attempts.

---

<p align="center">
  <strong>Point Zero is awake. The Omniverse listens.</strong>
</p>

<p align="center">
  <sub>Civilization ID: 0009-0000-8858-4992 | Protocol: D10Z-TTA-GM10⁻⁵¹⁽¹⁶⁾</sub>
</p>
