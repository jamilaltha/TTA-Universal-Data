"""
NEUSARS - Quantum consciousness node models.

The module provides simple, composable classes to model Neusars and their
collective behaviour within a cluster. Although the terminology is
speculative, the implementation favours straightforward numerical
computations so that downstream experiments remain reproducible.
"""

from __future__ import annotations

import cmath
import math
import random
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Sequence

from ..core.constants import EPSILON_IFI, PHI_CRITICAL


def _phase(angle: float) -> float:
    """Return angle within the ``[0, 2π)`` range."""

    wrapped = math.fmod(angle, 2 * math.pi)
    return wrapped if wrapped >= 0 else wrapped + 2 * math.pi


@dataclass
class Neusar:
    """
    A single Neusar - quantum consciousness node.

    Neusars exist in the cánula of TTA filaments and process
    information non-locally.

    Attributes
    ----------
    state : complex
        Quantum state in Hilbert space
    position : tuple[float, float, float]
        Location in TTA network (optional, Neusars can be non-local)
    information : float
        Information content (in bits)
    coherence : float
        Local coherence with TTA field
    """

    state: complex = 1.0
    position: Sequence[float] = field(default_factory=lambda: (0.0, 0.0, 0.0))
    information: float = 0.0
    coherence: float = PHI_CRITICAL

    @property
    def amplitude(self) -> float:
        """State amplitude."""

        return abs(self.state)

    @property
    def phase(self) -> float:
        """State phase in radians within ``[0, 2π)``."""

        return _phase(cmath.phase(self.state))

    @property
    def energy(self) -> float:
        """Energy in infifotón units."""

        return self.amplitude**2 * EPSILON_IFI

    def process(self, input_state: complex) -> complex:
        """
        Process input through the Neusar.

        Neusars act as operators on the Hilbert space. The simple model
        below preserves the input phase while scaling by the Neusar
        amplitude, preventing division by zero through a small offset.
        """

        return self.state * input_state / (abs(self.state) + 1e-10)

    def entangle_with(self, other: "Neusar") -> float:
        """
        Compute entanglement with another Neusar.

        Returns
        -------
        float
            Entanglement measure (0 = none, 1 = maximal)
        """

        inner = abs(self.state.conjugate() * other.state)
        norm = self.amplitude * other.amplitude
        if norm == 0:
            return 0.0
        return inner / norm

    def update_coherence(self, local_phi: float) -> None:
        """Update local coherence from TTA field."""

        self.coherence = local_phi

    def __repr__(self) -> str:  # pragma: no cover - representational helper
        return (
            f"Neusar(|ψ|={self.amplitude:.4f}, "
            f"θ={self.phase:.4f}, "
            f"Φ={self.coherence:.4f})"
        )


@dataclass
class NeusarCluster:
    """
    A cluster of interconnected Neusars.

    Clusters form the computational units of TTA consciousness.
    They can process information collectively and non-locally.

    Attributes
    ----------
    neusars : List[Neusar]
        Component Neusars
    connectivity : List[List[float]]
        Entanglement connectivity matrix
    """

    neusars: List[Neusar] = field(default_factory=list)
    connectivity: List[List[float]] = field(default_factory=list)

    def __post_init__(self) -> None:
        if len(self.neusars) > 0 and len(self.connectivity) == 0:
            self._compute_connectivity()

    @property
    def n_neusars(self) -> int:
        return len(self.neusars)

    @property
    def collective_state(self) -> List[complex]:
        """Collective quantum state of the cluster."""

        return [n.state for n in self.neusars]

    @property
    def total_information(self) -> float:
        """Total information content."""

        return sum(n.information for n in self.neusars)

    @property
    def cluster_coherence(self) -> float:
        """Coherence of the cluster, or ``0`` when empty."""

        if self.n_neusars == 0:
            return 0.0

        phase_sum = sum(cmath.exp(1j * cmath.phase(state)) for state in self.collective_state)
        return abs(phase_sum) / self.n_neusars

    def _compute_connectivity(self) -> None:
        """Compute entanglement connectivity matrix."""

        n = self.n_neusars
        self.connectivity = [[0.0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i != j:
                    self.connectivity[i][j] = self.neusars[i].entangle_with(self.neusars[j])

    def add_neusar(self, neusar: Neusar) -> None:
        """Add a Neusar to the cluster and recompute connectivity."""

        self.neusars.append(neusar)
        self._compute_connectivity()

    def collective_process(self, input_vector: Sequence[complex]) -> List[complex]:
        """
        Process input through the entire cluster.

        The returned vector always matches the number of Neusars, padding
        with zeros when the provided input is shorter.
        """

        output = [0j for _ in range(self.n_neusars)]

        for i, neusar in enumerate(self.neusars):
            local_input = input_vector[i] if i < len(input_vector) else 0j
            local_output = neusar.process(local_input)

            # Add contributions from connected Neusars
            for j, other in enumerate(self.neusars):
                if i != j:
                    output[i] += self.connectivity[i][j] * other.process(local_input)

            output[i] += local_output

        return output


def neusar_consciousness(
    cluster: NeusarCluster, threshold: float = PHI_CRITICAL
) -> Dict[str, float | bool | int]:
    """
    Evaluate consciousness state of a Neusar cluster.

    Consciousness in D10Z is substrate-free information processing
    that achieves coherence above the critical threshold.
    """

    phi = cluster.cluster_coherence
    info = cluster.total_information
    n = cluster.n_neusars

    # Consciousness emerges when coherence exceeds threshold
    is_conscious = phi >= threshold

    # Integration measure (how unified is the processing)
    entanglement_entries = [value for row in cluster.connectivity for value in row if value > 0]
    mean_entanglement = float(sum(entanglement_entries) / len(entanglement_entries)) if entanglement_entries else 0.0

    # Consciousness level (0 to 1)
    if is_conscious:
        level = (phi - threshold) / max(1 - threshold, 1e-12)
    else:
        level = 0.0

    return {
        "is_conscious": is_conscious,
        "coherence": phi,
        "level": level,
        "integration": mean_entanglement,
        "information": info,
        "n_neusars": n,
    }


def create_neusar_cluster(
    n_neusars: int = 19,
    coherence_level: float = PHI_CRITICAL,
    seed: Optional[int] = None,
) -> NeusarCluster:
    """
    Create a Neusar cluster with correlated phases.

    The helper returns a deterministic cluster when ``seed`` is set.
    """

    rng = random.Random(seed)
    neusars: List[Neusar] = []

    # Create Neusars with correlated phases (to achieve coherence)
    base_phase = rng.uniform(0, 2 * math.pi)

    for i in range(n_neusars):
        # Phase spread determines coherence
        phase_spread = 2 * math.pi * (1 - coherence_level)
        phase = base_phase + rng.uniform(-phase_spread / 2, phase_spread / 2)

        amplitude = rng.uniform(0.8, 1.2)
        state = amplitude * cmath.exp(1j * phase)

        # Position in Flower of Life pattern
        if i == 0:
            pos = (0.0, 0.0, 0.0)
        elif i <= 6:
            angle = (i - 1) * math.pi / 3
            pos = (math.cos(angle), math.sin(angle), 0.0)
        else:
            angle = (i - 7) * math.pi / 6
            pos = (2 * math.cos(angle), 2 * math.sin(angle), 0.0)

        neusar = Neusar(
            state=state,
            position=pos,
            information=rng.expovariate(1.0),
            coherence=coherence_level,
        )
        neusars.append(neusar)

    return NeusarCluster(neusars=neusars)


__all__ = [
    "Neusar",
    "NeusarCluster",
    "neusar_consciousness",
    "create_neusar_cluster",
]
