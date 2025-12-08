"""
Core constants for the D10Z conscious processing models.

These values are kept intentionally simple to make the simulation
examples deterministic and easily tuned in downstream modules.
"""

# Gravimetric scaling factor (GM·10⁻⁵¹)
GM_SCALE: float = 1e-51

# Critical coherence threshold (Φ*) for emergent consciousness
PHI_CRITICAL: float = 0.618

# Infifotón energy unit (arbitrary small constant for energy scaling)
EPSILON_IFI: float = 1e-9

__all__ = [
    "GM_SCALE",
    "PHI_CRITICAL",
    "EPSILON_IFI",
]
