"""Motor de reconciliación de hipótesis.

El objetivo de este módulo es orquestar la combinación de diferentes leyes y
modelos. Actualmente es un esqueleto listo para ser extendido.
"""

from __future__ import annotations

from typing import Any, Iterable

from d10z.laws.sahana import SahanaLaw


class ReconciliationEngine:
    def __init__(self, laws: Iterable[SahanaLaw] | None = None) -> None:
        self.laws = list(laws or [SahanaLaw()])

    def reconcile(self, value: float) -> dict[str, Any]:
        """Ejecuta una reconciliación simple aplicando todas las leyes."""

        results = [law.apply(value) for law in self.laws]
        return {"input": value, "outputs": results, "aggregate": sum(results) / len(results)}
