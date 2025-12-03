"""Simulador Fase 4 con topología fractal simplificada."""

from typing import Optional

import numpy as np

from ..laws import compute_tension
from ..tta import sahana_dynamics


def _fractal_connectivity(levels: int, branching: int, coupling: float) -> np.ndarray:
    """Genera una matriz de conectividad jerárquica tipo árbol."""

    total = sum(branching**l for l in range(levels))
    C = np.zeros((total, total), dtype=float)
    offset = 0
    parent_indices = [0]
    C[0, 0] = 0.0
    for level in range(1, levels):
        level_nodes = branching**level
        start_idx = offset + len(parent_indices)
        child_indices = list(range(start_idx, start_idx + level_nodes))
        for i, parent in enumerate(parent_indices):
            for b in range(branching):
                child = child_indices[i * branching + b]
                C[parent, child] = coupling / level
                C[child, parent] = coupling / level
        parent_indices = child_indices
        offset = start_idx
    return C


def run_phase4_fractal(
    levels: int = 3,
    branching: int = 2,
    coupling: float = 0.4,
    steps: int = 400,
    gamma: float = 0.01,
    seed: Optional[int] = None,
):
    """Ejecuta la Fase 4 sobre una topología fractal jerárquica."""

    rng = np.random.default_rng(seed)
    total = sum(branching**l for l in range(levels))
    Z0 = rng.normal(size=total) + 1j * rng.normal(size=total)
    C = _fractal_connectivity(levels, branching, coupling)
    Z_final = sahana_dynamics(Z0, C, gamma=gamma, steps=steps)
    tension = compute_tension(Z_final, C)
    return {"Z_final": Z_final, "tension": tension, "connectivity": C}
