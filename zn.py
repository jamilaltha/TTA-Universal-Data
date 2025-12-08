"""
Nodal state helpers for Zₙ.
"""

import numpy as np


def amplitude(Z: np.ndarray) -> np.ndarray:
    """Return |Zₙ| for each node."""
    return np.abs(Z)


def phase(Z: np.ndarray) -> np.ndarray:
    """Return arg(Zₙ) in radians."""
    return np.angle(Z)


def normalize(Z: np.ndarray) -> np.ndarray:
    """Normalize amplitudes to unity while preserving phase."""
    phases = phase(Z)
    return np.exp(1j * phases)


def coherence(Z: np.ndarray) -> float:
    """
    Mean phase coherence κ = |Σ e^{iθₙ}| / N
    """
    return float(np.abs(np.sum(np.exp(1j * phase(Z)))) / len(Z))


__all__ = ["amplitude", "phase", "normalize", "coherence"]
