# Contributing to D10Z-TTA

Thank you for your interest in contributing to D10Z-TTA! This document provides guidelines for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Contribution Types](#contribution-types)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Documentation](#documentation)
- [Scientific Contributions](#scientific-contributions)

## Code of Conduct

By participating, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

## Getting Started

### Prerequisites

- Python 3.8+
- Git
- (Optional) Virtual environment tool (venv, conda)

### Fork and Clone

```bash
# Fork on GitHub, then:
git clone https://github.com/YOUR-USERNAME/TTA-Universal-Data.git
cd TTA-Universal-Data
git remote add upstream https://github.com/jamilaltha/TTA-Universal-Data.git
```

## Development Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode with all dependencies
pip install -e .[dev,full]

# Verify installation
pytest tests/ -v
d10z info
```

## Contribution Types

### 1. Bug Fixes
- Search existing issues first
- Create an issue describing the bug
- Submit PR referencing the issue

### 2. New Features
- Open a feature request issue first
- Discuss design before implementation
- Include tests and documentation

### 3. Documentation
- Fix typos, improve clarity
- Add examples and tutorials
- Translate documentation

### 4. Scientific Contributions
- New validation datasets
- Improved models
- Additional theory reconciliations

### 5. Data Contributions
- New galaxy rotation curves
- Cosmological datasets
- Cross-validated results

## Pull Request Process

### 1. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-description
```

### 2. Make Changes

- Follow coding standards
- Add tests for new code
- Update documentation

### 3. Commit

Use conventional commits:

```bash
git commit -m "feat: add CMB validation module"
git commit -m "fix: correct chi-squared calculation"
git commit -m "docs: improve quickstart guide"
git commit -m "test: add tests for Isis law"
```

Types: `feat`, `fix`, `docs`, `test`, `refactor`, `style`, `chore`

### 4. Push and Create PR

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub.

### 5. Review Process

- Maintainers will review within 1 week
- Address feedback in new commits
- Once approved, maintainers will merge

## Coding Standards

### Python Style

```python
# Follow PEP 8
# Use type hints
def compute_fragmentation(
    coherence_matrix: np.ndarray,
    threshold: float = 0.5
) -> float:
    """
    Compute fragmentation index from coherence matrix.
    
    Parameters
    ----------
    coherence_matrix : np.ndarray
        Square symmetric matrix of coherence values.
    threshold : float, optional
        Minimum coherence threshold, by default 0.5.
    
    Returns
    -------
    float
        Fragmentation index I in [0, 1].
    
    Examples
    --------
    >>> C = np.array([[1.0, 0.8], [0.8, 1.0]])
    >>> compute_fragmentation(C)
    0.111...
    """
    # Implementation
    pass
```

### Formatting

```bash
# Format code
black d10z tests
isort d10z tests

# Check style
flake8 d10z
mypy d10z --ignore-missing-imports
```

## Testing

### Running Tests

```bash
# All tests
pytest tests/ -v

# Specific module
pytest tests/test_core.py -v

# With coverage
pytest tests/ --cov=d10z --cov-report=html

# Only fast tests
pytest tests/ -v -m "not slow"
```

### Writing Tests

```python
import pytest
import numpy as np
from d10z.core import PointZero

class TestPointZero:
    """Tests for PointZero class."""
    
    def test_default_initialization(self):
        """Test default Point Zero initialization."""
        p0 = PointZero()
        assert p0.scale == pytest.approx(1.616e-51, rel=1e-3)
    
    @pytest.fixture
    def sample_point_zero(self):
        """Fixture providing configured PointZero."""
        return PointZero(scale=1e-50)
    
    def test_custom_scale(self, sample_point_zero):
        """Test custom scale initialization."""
        assert sample_point_zero.scale == 1e-50
```

## Documentation

### Docstrings

Use NumPy style:

```python
def function_name(param1: type, param2: type) -> return_type:
    """
    Short description.
    
    Longer description if needed.
    
    Parameters
    ----------
    param1 : type
        Description of param1.
    param2 : type
        Description of param2.
    
    Returns
    -------
    return_type
        Description of return value.
    
    Raises
    ------
    ValueError
        When something is wrong.
    
    Examples
    --------
    >>> function_name(1, 2)
    3
    
    Notes
    -----
    Mathematical formulation:
    
    .. math::
        F = f \cdot v(Z_n)
    
    See Also
    --------
    related_function : Description.
    """
```

### Building Docs

```bash
cd docs
pip install -r requirements.txt
make html
# Open _build/html/index.html
```

## Scientific Contributions

### Adding New Validations

1. Create module in `d10z/validation/`
2. Implement model and validation function
3. Add tests in `tests/test_validation.py`
4. Update CLI in `d10z/cli.py`
5. Document in `docs/`

### Data Standards

- Use SI units
- Include error estimates
- Provide source citations
- Use standard formats (CSV, FITS)

### Mathematical Notation

| Symbol | Meaning |
|--------|---------|
| Z₀ | Point Zero |
| Dᵢ | Dimension i |
| SDᵢ,ⱼ | Subdimension j of dimension i |
| Φ | Coherence field |
| I | Fragmentation index |
| f_LI | Isis Law function |
| γ | Sahana damping |

## Recognition

Contributors are recognized in:
- CONTRIBUTORS.md
- Release notes
- Academic publications (where appropriate)

## Questions?

- Open an issue with the "question" label
- Email: jamil@d10z.org

---

*"Every contribution is a node in the TTA mesh, strengthening the fabric of understanding."*
