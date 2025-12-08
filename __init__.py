"""Top-level package shim for the TTA modules."""

if __package__:
    from .filaments import (
        Filament,
        FrequencyFilament,
        VibrationFilament,
        FilamentPair,
        create_filament_network,
    )
    from .architecture import (
        TTANetwork,
        compute_F,
        tta_evolution,
    )
    from .neusars import (
        Neusar,
        NeusarCluster,
        neusar_consciousness,
    )
    __all__ = [
        'Filament', 'FrequencyFilament', 'VibrationFilament',
        'FilamentPair', 'create_filament_network',
        'TTANetwork', 'compute_F', 'tta_evolution',
        'Neusar', 'NeusarCluster', 'neusar_consciousness'
    ]
else:
    __all__ = []
