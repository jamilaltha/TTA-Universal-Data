"""D10Z framework package.

Provides modules for constants, Big Start coherence ignition,
Temporal Tensorial Architecture (TTA) dynamics, and simulation utilities.
"""

from .constants import ETA_GM, EPS_IFI, ALPHA, BETA, LAMBDA
from .big_start import big_start_phi
from .tta import sahana_dynamics
from .laws import compute_tension
from .infifoton import infifoton_energy

__all__ = [
    "ETA_GM",
    "EPS_IFI",
    "ALPHA",
    "BETA",
    "LAMBDA",
    "big_start_phi",
    "sahana_dynamics",
    "compute_tension",
    "infifoton_energy",
]
