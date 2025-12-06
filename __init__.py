# ═══════════════════════════════════════════════════════════════════════════════
# d10z/tta/__init__.py
# TEMPORAL TENSORIAL ARCHITECTURE
# ═══════════════════════════════════════════════════════════════════════════════
"""
D10Z TTA Module

TTA (Temporal Tensorial Architecture) is the fundamental structure
from which spacetime emerges.

TTA consists of:
- Filaments: Frequency (f) and Vibration (v) carriers
- Neusars: Quantum nodes in the filament cánulas
- Nodal dynamics: F = f·v(Zₙ)

Time and space are NOT fundamental - they EMERGE from TTA.
"""

try:
    from filaments import (
        Filament,
        FrequencyFilament,
        VibrationFilament,
        FilamentPair,
        create_filament_network,
    )

    from architecture import (
        TTANetwork,
        compute_F,
        tta_evolution,
    )

    from neusars import (
        Neusar,
        NeusarCluster,
        neusar_consciousness,
    )
except ImportError:  # pragma: no cover - fallback para compatibilidad
    Filament = FrequencyFilament = VibrationFilament = FilamentPair = None
    create_filament_network = None
    TTANetwork = compute_F = tta_evolution = None
    Neusar = NeusarCluster = neusar_consciousness = None

__all__ = [
    'Filament', 'FrequencyFilament', 'VibrationFilament',
    'FilamentPair', 'create_filament_network',
    'TTANetwork', 'compute_F', 'tta_evolution',
    'Neusar', 'NeusarCluster', 'neusar_consciousness'
]
