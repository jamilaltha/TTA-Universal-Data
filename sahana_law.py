"""
Sahana Law (Coherence Dynamics).

This module re-exports the Sahana formulation from :mod:`coherence` with a
minimal convenience wrapper.
"""

import numpy as np

from .coherence import sahana_law as _sahana_law


def sahana(Z: np.ndarray, connectivity: np.ndarray, gamma: float = None) -> np.ndarray:
    """
    dZ/dt = -γ (Zₙ - Σ_j Cₙⱼ Zⱼ / kₙ)
    """
    if gamma is None:
        return _sahana_law(Z, connectivity)
    return _sahana_law(Z, connectivity, gamma=gamma)


__all__ = ["sahana"]
