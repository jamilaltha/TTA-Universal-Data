from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

from d10z.models.tta_model import TTAModel


@dataclass
class D10ZClient:
    """SDK de alto nivel para consumir el framework D10Z-TTA."""

    model: TTAModel

    @classmethod
    def default(cls) -> "D10ZClient":
        return cls(model=TTAModel())

    def run_rotation_curve_demo(self) -> Dict[str, Any]:
        radii, velocities = self.model.example_rotation_curve()
        return {"radii": radii, "velocities": velocities}

    def evaluate_sparc_sample(self, n_galaxies: int = 20) -> float:
        return self.model.evaluate_on_sparc_sample(n_galaxies=n_galaxies)
