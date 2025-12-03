"""Simulación de la fase 3 en topología 2D."""

import numpy as np

from ..big_start import big_start_phi
from ..laws import compute_tension
from ..tta import sahana_dynamics


def _grid_connectivity(size):
    n = size * size
    C = np.zeros((n, n), dtype=float)
    for i in range(size):
        for j in range(size):
            idx = i * size + j
            neighbors = []
            if i > 0:
                neighbors.append((i - 1) * size + j)
            if i < size - 1:
                neighbors.append((i + 1) * size + j)
            if j > 0:
                neighbors.append(i * size + (j - 1))
            if j < size - 1:
                neighbors.append(i * size + (j + 1))
            for n_idx in neighbors:
                C[idx, n_idx] = 1.0
    return C


def run_phase3_2d(size=8, gamma=0.02, steps=3000, seed=None):
    """Configura y ejecuta la dinámica de fase 3 sobre una malla 2D."""
    rng = np.random.default_rng(seed)
    C = _grid_connectivity(size)
    n = size * size
    Z0 = rng.normal(scale=0.1, size=n) + 1j * rng.normal(scale=0.1, size=n)
    Z0 *= big_start_phi(t=1e-43)
    Zf = sahana_dynamics(Z0, C, gamma=gamma, steps=steps)
    tension = compute_tension(Zf, C)
    return {
        "initial_state": Z0,
        "final_state": Zf,
        "connectivity": C,
        "tension": tension,
    }
