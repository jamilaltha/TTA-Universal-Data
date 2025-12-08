"""
Nodal density estimators.
"""

import numpy as np


def radial_density(r: np.ndarray, Z: np.ndarray, sigma: float = 1.0) -> np.ndarray:
    """
    Compute a smoothed radial density profile ρ_n(r).

    ρ_n(r) = Σ |Zₙ|² · exp(-(r - rₙ)² / 2σ²)
    """
    if r.shape != Z.shape:
        raise ValueError("r and Z must have same shape")
    amplitudes = np.abs(Z) ** 2
    profile = amplitudes * np.exp(-((r - r.mean()) ** 2) / (2 * sigma ** 2))
    return profile


def mean_density(Z: np.ndarray, volume: float) -> float:
    """⟨ρ_n⟩ = Σ |Zₙ|² / V"""
    return float(np.sum(np.abs(Z) ** 2) / volume)


__all__ = ["radial_density", "mean_density"]
