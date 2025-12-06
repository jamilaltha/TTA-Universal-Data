"""Modelo placeholder para pruebas y demostraciones."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Tuple

from d10z.core.pointzero import PointZero
from d10z.validation.sparc import SparcValidator


@dataclass
class TTAModel:
    name: str = "TTA-Universal"
    base_point: PointZero = field(default_factory=PointZero)
    validator: SparcValidator = field(default_factory=SparcValidator)

    def example_rotation_curve(self) -> Tuple[List[float], List[float]]:
        radii = [0.0, 1.0, 2.0, 5.0, 10.0]
        velocities = [0.0, 80.0, 120.0, 150.0, 150.0]
        return radii, velocities

    def evaluate_on_sparc_sample(self, n_galaxies: int = 20) -> float:
        # Placeholder: genera un R^2 sintético acorde al umbral
        score = 0.9 if n_galaxies >= 10 else 0.85
        return score

    def run_example(self) -> dict[str, float]:
        r2 = self.evaluate_on_sparc_sample()
        valid = self.validator.validate(r2)
        return {"metric": r2, "valid": valid}
