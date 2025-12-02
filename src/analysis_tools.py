"""Herramientas de análisis para simulaciones del framework D10Z-TTA."""

from __future__ import annotations

from typing import Dict, List, Tuple

import numpy as np
from scipy.signal import welch

from .d10z_simulator import SimulationResult


def compute_energy_spectrum(states: np.ndarray, fs: float = 1.0) -> Tuple[np.ndarray, np.ndarray]:
    """Calcula el espectro de potencia de la trayectoria nodal."""

    flattened = states.reshape(states.shape[0], -1)
    signal = flattened.mean(axis=1)
    freq, power = welch(signal, fs=fs, nperseg=min(256, len(signal)))
    return freq, power


def stability_index(states: np.ndarray) -> float:
    """Índice heurístico de estabilidad basado en la varianza relativa."""

    variance = np.var(states, axis=0).mean()
    amplitude = np.linalg.norm(states, axis=1).mean()
    return float(np.exp(-variance) * (1 / (1 + amplitude)))


def summarize_events(result: SimulationResult) -> List[str]:
    """Devuelve mensajes de eventos en formato legible."""

    return [f"t={t:.3f}: {msg}" for t, msg in result.events]


def compute_observables(states: np.ndarray) -> Dict[str, float]:
    """Calcula observables básicos utilizados en los protocolos de validación."""

    return {
        "media": float(np.mean(states)),
        "desviacion": float(np.std(states)),
        "maximo": float(np.max(states)),
        "minimo": float(np.min(states)),
    }
