"""Simulador Fase 3B en topología 3D."""

import numpy as np

from ..laws import compute_tension
from ..tta import sahana_dynamics


def _make_lattice_connectivity_3d(nx: int, ny: int, nz: int, coupling: float) -> np.ndarray:
    total = nx * ny * nz
    C = np.zeros((total, total), dtype=float)
    for x in range(nx):
        for y in range(ny):
            for z in range(nz):
                idx = (x * ny + y) * nz + z
                neighbors = [
                    ((x + 1) % nx, y, z),
                    ((x - 1) % nx, y, z),
                    (x, (y + 1) % ny, z),
                    (x, (y - 1) % ny, z),
                    (x, y, (z + 1) % nz),
                    (x, y, (z - 1) % nz),
                ]
                for nx_, ny_, nz_ in neighbors:
                    n_idx = (nx_ * ny + ny_) * nz + nz_
                    C[idx, n_idx] = coupling
    return C


def run_phase3b_3d(nx: int = 3, ny: int = 3, nz: int = 3, coupling: float = 0.3, steps: int = 300, gamma: float = 0.015, seed: int | None = None):
    """Ejecución de la fase 3B en retícula 3D periódica."""

    rng = np.random.default_rng(seed)
    total = nx * ny * nz
    Z0 = rng.normal(size=total) + 1j * rng.normal(size=total)
    C = _make_lattice_connectivity_3d(nx, ny, nz, coupling)
    Z_final = sahana_dynamics(Z0, C, gamma=gamma, steps=steps)
    tension = compute_tension(Z_final, C)
    return {"Z_final": Z_final, "tension": tension, "connectivity": C}
