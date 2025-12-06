"""Implementación placeholder de la Ley de Sahana.

Este archivo sirve como recordatorio para incorporar las ecuaciones y
constantes reales asociadas al marco teórico.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class SahanaLaw:
    coefficient: float = 1.0

    def apply(self, value: float) -> float:
        """Aplica una transformación sencilla a modo de demostración."""

        return self.coefficient * value
