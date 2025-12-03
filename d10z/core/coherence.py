"""Coherence utilities for complex networks."""

from __future__ import annotations

import cmath
from typing import Iterable


def compute_coherence(z_array: Iterable[complex]) -> float:
    """Compute global coherence using the Kuramoto order parameter.

    Parameters
    ----------
    z_array : Iterable[complex]
        Complex state vector for the nodal network.

    Returns
    -------
    float
        Order parameter magnitude in ``[0, 1]``.
    """
    values = list(z_array)
    if not values:
        return 0.0

    phases = [cmath.phase(z) for z in values]
    order_parameter = sum(cmath.exp(1j * phase) for phase in phases) / len(values)
    return abs(order_parameter)


__all__ = ['compute_coherence']
