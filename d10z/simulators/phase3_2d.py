"""Simulador Fase 3 en topología 2D simplificada."""

from typing import Optional

import numpy as np

from ..laws import compute_tension
from ..tta import sahana_dynamics


def _make_lattice_connectivity(n_rows: int, n_cols: int, coupling: float) -> np.ndarray:
    """Construye una malla 2D con conectividad de vecinos (torus)."""

    total = n_rows * n_cols
    C = np.zeros((total, total), dtype=float)
    for r in range(n_rows):
        for c in range(n_cols):
            idx = r * n_cols + c
            neighbors = [
                ((r + 1) % n_rows, c),
                ((r - 1) % n_rows, c),
                (r, (c + 1) % n_cols),
                (r, (c - 1) % n_cols),
            ]
            for nr, nc in neighbors:
                n_idx = nr * n_cols + nc
                C[idx, n_idx] = coupling
    return C


def run_phase3_2d(
    n_rows: int = 5,
    n_cols: int = 5,
    coupling: float = 0.5,
    steps: int = 500,
    gamma: float = 0.02,
    seed: Optional[int] = None,
):
    """Ejecuta la Fase 3 sobre una red 2D periódica.

    Parameters
    ----------
    n_rows, n_cols : int
        Dimensiones de la malla periódica.
    coupling : float
        Peso de acoplamiento para vecinos.
    steps : int
        Iteraciones de la dinámica Sahana.
    gamma : float
        Paso de relajación en :func:`sahana_dynamics`.
    seed : int, optional
        Semilla para reproducibilidad.

    Returns
    -------
    dict
        Diccionario con el estado final, tensión y conectividad.
    """

    rng = np.random.default_rng(seed)
    total = n_rows * n_cols
    Z0 = rng.normal(size=total) + 1j * rng.normal(size=total)
    C = _make_lattice_connectivity(n_rows, n_cols, coupling)
    Z_final = sahana_dynamics(Z0, C, gamma=gamma, steps=steps)
    tension = compute_tension(Z_final, C)
    return {"Z_final": Z_final, "tension": tension, "connectivity": C}
