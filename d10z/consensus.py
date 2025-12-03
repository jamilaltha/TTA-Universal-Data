"""Simple consensus simulator for the D10Z model."""

from __future__ import annotations

from dataclasses import dataclass, field
from math import exp
from random import Random
from typing import Iterable, List, Sequence


@dataclass
class NodeState:
    """State for a single node in the consensus network."""

    id: int
    z: float
    color: str = field(default="")


class ConsensusEngine:
    """Deterministic simulator for the consensus process described in D10Z."""

    def __init__(
        self,
        n: int = 20,
        gamma: float = 0.1,
        alpha: float = 0.5,
        beta: float = 1.0,
        seed: int | None = None,
    ) -> None:
        if n <= 1:
            raise ValueError("The system requires at least two nodes")

        self.n = n
        self.gamma = gamma
        self.alpha = alpha
        self.beta = beta
        self.random = Random(seed)
        self.iteration = 0
        self.nodes = self._initialize_nodes()
        self.integrity_history: List[float] = []
        self.energy_history: List[float] = []

    def _initialize_nodes(self) -> List[NodeState]:
        nodes = []
        for idx in range(self.n):
            z = self.random.random() * 0.8 + 0.2  # [0.2, 1.0]
            nodes.append(NodeState(id=idx, z=z))
        return nodes

    def _connectivity(self, nodes: Sequence[NodeState]) -> List[List[float]]:
        c = [[0.0 for _ in range(self.n)] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(i + 1, self.n):
                d_js = abs(nodes[i].z - nodes[j].z)
                c_ij = (nodes[i].z * nodes[j].z) ** self.alpha * exp(-self.beta * d_js)
                c[i][j] = c_ij
                c[j][i] = c_ij
        return c

    def _consensus(self, nodes: Sequence[NodeState], c: List[List[float]]) -> List[float]:
        estimates = []
        for i in range(self.n):
            sum_cz = 0.0
            sum_c = 0.0
            for j in range(self.n):
                if i == j:
                    continue
                sum_cz += c[i][j] * nodes[j].z
                sum_c += c[i][j]
            estimates.append(sum_cz / sum_c if sum_c else nodes[i].z)
        return estimates

    def _integrity(self, nodes: Sequence[NodeState]) -> float:
        mean = sum(node.z for node in nodes) / self.n
        variance = sum((node.z - mean) ** 2 for node in nodes) / self.n
        return variance

    def _energy(self, nodes: Sequence[NodeState], c: List[List[float]]) -> float:
        energy = 0.0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                energy += c[i][j] * (nodes[i].z - nodes[j].z) ** 2
        return energy / 2.0

    def step(self) -> dict:
        """Advance the simulation one iteration and return diagnostics."""

        c = self._connectivity(self.nodes)
        z_hats = self._consensus(self.nodes, c)

        new_nodes = []
        for node, z_hat in zip(self.nodes, z_hats):
            z_new = node.z - self.gamma * (node.z - z_hat)
            new_nodes.append(NodeState(id=node.id, z=z_new, color=node.color))

        self.nodes = new_nodes
        self.iteration += 1

        integrity = self._integrity(self.nodes)
        energy = self._energy(self.nodes, c)

        self.integrity_history.append(integrity)
        self.energy_history.append(energy)

        return {
            "iteration": self.iteration,
            "integrity": integrity,
            "energy": energy,
            "z": [node.z for node in self.nodes],
        }

    def run(self, max_iterations: int = 1000, tolerance: float = 1e-5) -> dict:
        """Run until convergence or until ``max_iterations`` is reached."""

        for _ in range(max_iterations):
            metrics = self.step()
            if metrics["integrity"] <= tolerance:
                break
        return metrics

    @staticmethod
    def summarize(history: Iterable[float]) -> dict:
        values = list(history)
        return {
            "min": min(values) if values else 0.0,
            "max": max(values) if values else 0.0,
            "last": values[-1] if values else 0.0,
        }
