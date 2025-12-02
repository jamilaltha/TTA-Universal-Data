"""Simulador central del framework D10Z-TTA.

Incluye modelos base y el modo Big Start para explorar la dinámica nodal
fractal unificada. Proporciona detección de eventos y utilidades de
visualización rápida para inspeccionar resultados.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Dict, List, Optional, Tuple

import numpy as np


@dataclass
class SimulationResult:
    """Contenedor ligero para almacenar resultados de simulación."""

    times: np.ndarray
    states: np.ndarray
    events: List[Tuple[float, str]] = field(default_factory=list)


class D10ZSystem:
    """Simula la dinámica nodal fractal unificada en su forma base."""

    def __init__(
        self,
        initial_state: np.ndarray,
        coupling: float = 1.0,
        fractal_order: float = 1.5,
        event_threshold: float = 10.0,
        energy_fn: Optional[Callable[[np.ndarray], float]] = None,
    ) -> None:
        self.state = np.array(initial_state, dtype=float)
        self.coupling = coupling
        self.fractal_order = fractal_order
        self.event_threshold = event_threshold
        self.energy_fn = energy_fn or self._default_energy
        self._times: List[float] = [0.0]
        self._states: List[np.ndarray] = [self.state.copy()]
        self._events: List[Tuple[float, str]] = []

    def _default_energy(self, state: np.ndarray) -> float:
        potential = np.sum(np.abs(state) ** self.fractal_order)
        kinetic = 0.5 * np.sum(state ** 2)
        return kinetic + self.coupling * potential

    def equations_of_motion(self, _: float, state: np.ndarray) -> np.ndarray:
        gradient = self.coupling * self.fractal_order * np.sign(state) * (
            np.abs(state) ** (self.fractal_order - 1)
        )
        return -gradient

    def step(self, dt: float) -> None:
        derivative = self.equations_of_motion(self._times[-1], self.state)
        self.state = self.state + dt * derivative
        self._record_state(self._times[-1] + dt)
        self._detect_events()

    def _record_state(self, time_point: float) -> None:
        self._times.append(time_point)
        self._states.append(self.state.copy())

    def _detect_events(self) -> None:
        energy = self.energy_fn(self.state)
        amplitude = np.linalg.norm(self.state)
        if energy > self.event_threshold:
            self._events.append((self._times[-1], f"Energía crítica: {energy:.3f}"))
        if amplitude > self.event_threshold:
            self._events.append((self._times[-1], f"Amplitud crítica: {amplitude:.3f}"))

    def run(self, time_span: float, dt: float = 0.01) -> SimulationResult:
        steps = int(np.ceil(time_span / dt))
        for _ in range(steps):
            self.step(dt)
        return SimulationResult(
            times=np.array(self._times), states=np.vstack(self._states), events=self._events
        )

    def visualize(self) -> None:
        try:
            import matplotlib.pyplot as plt
        except ImportError as exc:  # pragma: no cover - fallback informativo
            raise RuntimeError("Matplotlib es requerido para visualizar.") from exc

        data = np.vstack(self._states)
        plt.figure(figsize=(8, 4))
        for dim in range(data.shape[1]):
            plt.plot(self._times, data[:, dim], label=f"Dimensión {dim}")
        plt.xlabel("Tiempo")
        plt.ylabel("Estado")
        plt.title("Evolución nodal fractal (D10Z)")
        plt.legend()
        plt.tight_layout()
        plt.show()


class D10ZBigStartSystem(D10ZSystem):
    """Extiende el sistema base con dinámica de arranque intensificado."""

    def __init__(
        self,
        initial_state: np.ndarray,
        big_start_factor: float = 3.0,
        **kwargs: Dict,
    ) -> None:
        super().__init__(initial_state, **kwargs)
        self.big_start_factor = big_start_factor

    def step(self, dt: float) -> None:
        derivative = self.equations_of_motion(self._times[-1], self.state)
        boosted = derivative * (1 + self.big_start_factor * np.exp(-self._times[-1]))
        self.state = self.state + dt * boosted
        self._record_state(self._times[-1] + dt)
        self._detect_events()
        if np.linalg.norm(self.state) > 2 * self.event_threshold:
            self._events.append((self._times[-1], "Big Start detectado"))


__all__ = [
    "D10ZSystem",
    "D10ZBigStartSystem",
    "SimulationResult",
]
