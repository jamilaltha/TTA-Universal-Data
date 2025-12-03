"""Simuladores de fases para el framework D10Z."""

from .phase3_2d import run_phase3_2d
from .phase3b_3d import run_phase3b_3d
from .phase4_fractal import run_phase4_fractal

__all__ = [
    "run_phase3_2d",
    "run_phase3b_3d",
    "run_phase4_fractal",
]
