"""Componentes nucleares del framework D10Z-TTA.

Este módulo define primitivas base utilizadas en los modelos y utilidades del
paquete. El contenido es un esqueleto inicial que puede ampliarse con las
estructuras matemáticas reales.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class PointZero:
    """Representa un punto de referencia abstracto.

    En implementaciones reales, este objeto podría incorporar estructuras
    geométricas, sistemas de referencia o invariantes físicos.
    """

    name: str = "origin"
    metadata: dict[str, Any] | None = None

    def describe(self) -> str:
        """Devuelve una descripción breve del punto base."""

        return f"PointZero<{self.name}>"
