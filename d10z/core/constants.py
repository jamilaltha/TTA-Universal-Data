"""Physical constants used throughout the D10Z simulations."""

# Coherence thresholds
PHI_IGNITION: float = 0.99
PHI_CRITICAL: float = 0.95

# Energy quantum for infifotón emission
EPSILON_IFI: float = 1e-6

# Geometry
FLOWER_OF_LIFE_NODES: int = 19

__all__ = [
    'PHI_IGNITION',
    'PHI_CRITICAL',
    'EPSILON_IFI',
    'FLOWER_OF_LIFE_NODES'
]
