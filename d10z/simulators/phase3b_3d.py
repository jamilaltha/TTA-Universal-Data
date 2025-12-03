"""Simulación de la fase 3B en topología 3D."""

import numpy as np

from ..big_start import big_start_phi
from ..laws import compute_tension
from ..tta import sahana_dynamics


def _lattice3d_connectivity(size):
    n = size ** 3
    C = np.zeros((n, n), dtype=float)
    for x in range(size):
        for y in range(size):
            for z in range(size):
                idx = x * size * size + y * size + z
                neighbors = []
                if x > 0:
                    neighbors.append((x - 1) * size * size + y * size + z)
                if x < size - 1:
                    neighbors.append((x + 1) * size * size + y * size + z)
                if y > 0:
                    neighbors.append(x * size * size + (y - 1) * size + z)
                if y < size - 1:
                    neighbors.append(x * size * size + (y + 1) * size + z)
                if z > 0:
                    neighbors.append(x * size * size + y * size + (z - 1))
                if z < size - 1:
                    neighbors.append(x * size * size + y * size + (z + 1))
                for n_idx in neighbors:
                    C[idx, n_idx] = 1.0
    return C


def run_phase3b_3d(size=4, gamma=0.02, steps=3000, seed=None):
    """Ejecuta la dinámica de fase 3B sobre un cubo 3D."""
    rng = np.random.default_rng(seed)
    C = _lattice3d_connectivity(size)
    n = size ** 3
    Z0 = rng.normal(scale=0.05, size=n) + 1j * rng.normal(scale=0.05, size=n)
    Z0 *= big_start_phi(t=1e-43)
    Zf = sahana_dynamics(Z0, C, gamma=gamma, steps=steps)
    tension = compute_tension(Zf, C)
    return {
        "initial_state": Z0,
        "final_state": Zf,
        "connectivity": C,
        "tension": tension,
    }
