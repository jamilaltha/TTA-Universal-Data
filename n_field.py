"""
Discrete n-field representation.

The n-field tracks nodal occupation numbers nₙ and their diffusion across the
network.
"""

import numpy as np


def evolve_n_field(n_field: np.ndarray, diffusion: float = 0.1, dt: float = 0.01) -> np.ndarray:
    """
    Diffusion update: n(t+dt) = n + D·∇²n·dt.
    """
    laplacian = np.zeros_like(n_field)
    for axis in range(n_field.ndim):
        laplacian += np.gradient(np.gradient(n_field, axis=axis), axis=axis)
    return n_field + diffusion * laplacian * dt


def occupation_fraction(n_field: np.ndarray) -> float:
    """Mean occupation ⟨n⟩ over the lattice."""
    return float(np.mean(n_field))


__all__ = ["evolve_n_field", "occupation_fraction"]
