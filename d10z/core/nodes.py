"""Nodal network definitions for D10Z simulations."""

from __future__ import annotations

import cmath
import math
import random
from dataclasses import dataclass
from typing import Dict, List, Optional

from .constants import FLOWER_OF_LIFE_NODES
from .coherence import compute_coherence


@dataclass
class NodalNetwork:
    """Simple complex nodal network with Sahana dynamics."""

    z_array: List[complex]

    @property
    def n_nodes(self) -> int:
        return len(self.z_array)

    @property
    def global_coherence(self) -> float:
        return compute_coherence(self.z_array)

    @property
    def total_energy(self) -> float:
        # Interpret nodal energy as squared amplitude sum
        return sum(abs(z) ** 2 for z in self.z_array)

    def evolve_sahana(self, *, dt: float = 0.1, steps: int = 1, coupling: float = 0.25) -> None:
        """Iteratively align node phases and amplitudes toward coherence."""
        for _ in range(steps):
            phases = [cmath.phase(z) for z in self.z_array]
            amplitudes = [abs(z) for z in self.z_array]

            mean_phase = cmath.phase(sum(cmath.exp(1j * p) for p in phases))
            mean_amplitude = sum(amplitudes) / len(amplitudes)

            aligned_phases = [p + coupling * dt * (mean_phase - p) for p in phases]
            aligned_amplitudes = [a + coupling * dt * (mean_amplitude - a) for a in amplitudes]

            self.z_array = [amp * cmath.exp(1j * phase) for amp, phase in zip(aligned_amplitudes, aligned_phases)]

    def get_state(self) -> Dict[str, List[float]]:
        """Return a shallow copy of the network state for logging."""
        return {
            'z_array': list(self.z_array),
            'phases': [cmath.phase(z) for z in self.z_array],
            'amplitudes': [abs(z) for z in self.z_array]
        }

    def __repr__(self) -> str:
        return (
            f"NodalNetwork(n_nodes={self.n_nodes}, "
            f"coherence={self.global_coherence:.4f}, "
            f"energy={self.total_energy:.4f})"
        )


def create_flower_of_life(*, scale: float = 1.0, seed: Optional[int] = None) -> NodalNetwork:
    """Create a simple Flower of Life inspired network."""
    rng = random.Random(seed)
    amplitudes = [rng.uniform(0.5, 1.0) * scale for _ in range(FLOWER_OF_LIFE_NODES)]
    phases = [rng.uniform(-math.pi, math.pi) for _ in range(FLOWER_OF_LIFE_NODES)]
    z_array = [amp * cmath.exp(1j * phase) for amp, phase in zip(amplitudes, phases)]
    return NodalNetwork(z_array=z_array)


__all__ = ['NodalNetwork', 'create_flower_of_life']
