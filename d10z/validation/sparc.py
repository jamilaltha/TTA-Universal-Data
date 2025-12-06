"""Validaciones simplificadas contra datos SPARC.

Este módulo actúa como marcador de posición para pruebas más completas que
puedan incorporar catálogos externos y métricas avanzadas.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class SparcValidator:
    threshold: float = 0.8

    def validate(self, score: float) -> bool:
        """Comprueba si el puntaje supera el umbral mínimo."""

        return score >= self.threshold
