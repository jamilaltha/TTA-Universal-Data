"""Utilidades de visualización para resultados del framework D10Z-TTA."""

from __future__ import annotations

from typing import Iterable, Optional

import numpy as np


def plot_time_series(times: Iterable[float], states: np.ndarray, title: str = "Dinámica D10Z") -> None:
    try:
        import matplotlib.pyplot as plt
    except ImportError as exc:  # pragma: no cover - fallback informativo
        raise RuntimeError("Matplotlib es requerido para visualizar.") from exc

    data = np.array(states)
    plt.figure(figsize=(8, 4))
    for dim in range(data.shape[1]):
        plt.plot(times, data[:, dim], label=f"Dimensión {dim}")
    plt.xlabel("Tiempo")
    plt.ylabel("Estado")
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_phase_space(states: np.ndarray, dims: Optional[tuple[int, int]] = None) -> None:
    try:
        import matplotlib.pyplot as plt
    except ImportError as exc:  # pragma: no cover - fallback informativo
        raise RuntimeError("Matplotlib es requerido para visualizar.") from exc

    data = np.array(states)
    dims = dims or (0, 1)
    plt.figure(figsize=(5, 5))
    plt.plot(data[:, dims[0]], data[:, dims[1]], linewidth=1.5)
    plt.xlabel(f"Dim {dims[0]}")
    plt.ylabel(f"Dim {dims[1]}")
    plt.title("Espacio de fases nodal")
    plt.tight_layout()
    plt.show()
