"""D10Z: core interfaces for the D10Z-TTA framework.

This package exposes building blocks for the Big Start coherence ignition,
Temporal Tensorial Architecture (TTA) dynamics, infifoton energy utilities,
and representative simulation drivers.
"""

from .constants import ALPHA, BETA, EPS_IFI, ETA_GM, LAMBDA
from .big_start import big_start_phi
from .infifoton import infifoton_energy
from .laws import compute_tension
from .tta import sahana_dynamics

__all__ = [
    "ALPHA",
    "BETA",
    "EPS_IFI",
    "ETA_GM",
    "LAMBDA",
    "big_start_phi",
    "infifoton_energy",
    "compute_tension",
    "sahana_dynamics",
]

__version__ = "0.1.0"
