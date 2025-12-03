"""Utilities for generating and analyzing Flower of Life geometry.

This module provides a lightweight representation of the 19-node Flower of
Life pattern along with helpers for constructing positions, computing a basic
connectivity matrix, and measuring weighted phase coherence.
"""
from __future__ import annotations

import cmath
import math
from dataclasses import dataclass
from typing import List, Optional

from ..core.constants import FLOWER_OF_LIFE_NODES

Vector3 = List[float]


def _zeros_matrix(rows: int, cols: int) -> List[List[float]]:
    return [[0.0 for _ in range(cols)] for _ in range(rows)]


def _add_vectors(a: Vector3, b: Vector3) -> Vector3:
    return [a[i] + b[i] for i in range(3)]


def _polar_to_cartesian(radius: float, angle: float) -> Vector3:
    return [radius * math.cos(angle), radius * math.sin(angle), 0.0]


def _normalize_center(center: Optional[Vector3], z_offset: float) -> Vector3:
    """Normalize and broadcast center coordinates.

    If no center is provided, the origin is used. A provided center is converted
    to a list and adjusted by ``z_offset`` to ensure consistent handling of
    vertical positioning.
    """

    if center is None:
        base_center: Vector3 = [0.0, 0.0, 0.0]
    else:
        if len(center) != 3:
            raise ValueError("center must be a 3-element coordinate")
        base_center = [float(c) for c in center]

    base_center[2] += z_offset
    return base_center


@dataclass
class FlowerOfLife:
    """The Flower of Life sacred geometry.

    19 nodes in hexagonal arrangement:
    - 1 center node
    - 6 first ring nodes
    - 12 second ring nodes
    """

    positions: List[Vector3]
    scale: float
    center: Vector3

    @property
    def n_nodes(self) -> int:
        return FLOWER_OF_LIFE_NODES

    @property
    def first_ring(self) -> List[Vector3]:
        """Positions of first ring (6 nodes)."""

        return self.positions[1:7]

    @property
    def second_ring(self) -> List[Vector3]:
        """Positions of second ring (12 nodes)."""

        return self.positions[7:19]

    def get_connectivity(self) -> List[List[float]]:
        """Get natural connectivity matrix for Flower of Life.

        Nodes are connected based on their ring membership and angular proximity.
        """

        connectivity = _zeros_matrix(self.n_nodes, self.n_nodes)

        # Center connects to all first ring
        for i in range(1, 7):
            connectivity[0][i] = 1.0
            connectivity[i][0] = 1.0

        # First ring connects to neighbors
        for i in range(1, 7):
            next_i = 1 + (i % 6)
            connectivity[i][next_i] = 1.0
            connectivity[next_i][i] = 1.0

        # First ring connects to second ring
        for i in range(1, 7):
            # Each first ring node connects to 2 second ring nodes
            j1 = 7 + 2 * (i - 1)
            j2 = 7 + (2 * (i - 1) + 1) % 12
            for j in (j1, j2):
                connectivity[i][j] = 0.8
                connectivity[j][i] = 0.8

        # Second ring connects to neighbors
        for i in range(7, 19):
            next_i = 7 + ((i - 7 + 1) % 12)
            connectivity[i][next_i] = 0.6
            connectivity[next_i][i] = 0.6

        return connectivity


def create_flower_geometry(
    scale: float = 1.0,
    center: Optional[Vector3] = None,
    z_offset: float = 0.0,
) -> FlowerOfLife:
    """Create Flower of Life geometry.

    Parameters
    ----------
    scale : float
        Radius of first ring
    center : list, optional
        Center position (default origin)
    z_offset : float
        Z coordinate offset applied even when ``center`` is provided

    Returns
    -------
    FlowerOfLife
        The geometry structure
    """

    normalized_center = _normalize_center(center, z_offset)
    positions: List[Vector3] = [[0.0, 0.0, 0.0] for _ in range(FLOWER_OF_LIFE_NODES)]

    # Node 0: Center
    positions[0] = normalized_center

    # Nodes 1-6: First ring (hexagon)
    for i in range(6):
        angle = i * math.pi / 3
        positions[1 + i] = _add_vectors(normalized_center, _polar_to_cartesian(scale, angle))

    # Nodes 7-18: Second ring
    # Outer hexagon (6 nodes)
    for i in range(6):
        angle = i * math.pi / 3 + math.pi / 6
        positions[7 + i] = _add_vectors(normalized_center, _polar_to_cartesian(2 * scale, angle))

    # Inner second ring (6 nodes at √3 distance)
    for i in range(6):
        angle = i * math.pi / 3
        positions[13 + i] = _add_vectors(normalized_center, _polar_to_cartesian(math.sqrt(3) * scale, angle))

    return FlowerOfLife(
        positions=positions,
        scale=scale,
        center=normalized_center,
    )


def flower_coherence(phases: List[float]) -> float:
    """Compute coherence specific to Flower of Life geometry.

    Weights the center node more heavily as it is the nexus of the pattern.
    """

    if len(phases) != FLOWER_OF_LIFE_NODES:
        raise ValueError(
            f"phases must have length {FLOWER_OF_LIFE_NODES}, got {len(phases)}",
        )

    # Weights: center = 3, first ring = 2, second ring = 1
    weights = [3.0] + [2.0] * 6 + [1.0] * 12
    total_weight = sum(weights)
    normalized_weights = [w / total_weight for w in weights]

    # Weighted phase sum
    weighted_sum = sum(
        normalized_weights[i] * cmath.exp(1j * phase) for i, phase in enumerate(phases)
    )

    return abs(weighted_sum)


def visualize_flower(
    flower: FlowerOfLife,
    phases: Optional[List[float]] = None,
    ax=None,
):
    """Visualize Flower of Life geometry using matplotlib."""

    import matplotlib.pyplot as plt

    if ax is None:
        _, ax = plt.subplots(figsize=(8, 8))

    pos_2d = [node[:2] for node in flower.positions]

    # Draw connections
    connectivity = flower.get_connectivity()
    for i in range(flower.n_nodes):
        for j in range(i + 1, flower.n_nodes):
            if connectivity[i][j] > 0:
                ax.plot(
                    [pos_2d[i][0], pos_2d[j][0]],
                    [pos_2d[i][1], pos_2d[j][1]],
                    "k-",
                    alpha=0.3 * connectivity[i][j],
                    lw=1,
                )

    # Draw nodes
    if phases is not None:
        colors = [phase % (2 * math.pi) / (2 * math.pi) for phase in phases]
        ax.scatter(
            [p[0] for p in pos_2d],
            [p[1] for p in pos_2d],
            c=colors,
            cmap="hsv",
            s=200,
            edgecolors="black",
            zorder=5,
        )
    else:
        ax.scatter(
            [p[0] for p in pos_2d],
            [p[1] for p in pos_2d],
            c="gold",
            s=200,
            edgecolors="black",
            zorder=5,
        )

    # Draw circles for visual reference
    for r in [flower.scale, 2 * flower.scale]:
        circle = plt.Circle(
            flower.center[:2],
            r,
            fill=False,
            color="gray",
            linestyle="--",
            alpha=0.5,
        )
        ax.add_patch(circle)

    ax.set_aspect("equal")
    ax.set_title("Flower of Life - Primordial Geometry")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    return ax


__all__ = [
    "FlowerOfLife",
    "create_flower_geometry",
    "flower_coherence",
    "visualize_flower",
]
