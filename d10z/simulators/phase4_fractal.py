"""Simulación fractal para fase 4."""

import numpy as np

from ..laws import compute_tension
from ..tta import sahana_dynamics


def _fractal_connectivity(depth=2):
    base = np.array([[0, 1], [1, 1]], dtype=float)
    C = base.copy()
    for _ in range(depth - 1):
        C = np.kron(C, base)
    np.fill_diagonal(C, 0.0)
    return C


def run_phase4_fractal(depth=3, gamma=0.01, steps=2000, seed=None):
    """Ejecuta una simulación fractal que aproxima correlaciones de fase 4."""
    rng = np.random.default_rng(seed)
    C = _fractal_connectivity(depth)
    n = C.shape[0]
    Z0 = rng.normal(scale=0.02, size=n) + 1j * rng.normal(scale=0.02, size=n)
    Zf = sahana_dynamics(Z0, C, gamma=gamma, steps=steps)
    tension = compute_tension(Zf, C)
    return {
        "initial_state": Z0,
        "final_state": Zf,
        "connectivity": C,
        "tension": tension,
    }
