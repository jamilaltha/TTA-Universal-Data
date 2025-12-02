"""Ejemplo de simulación básica D10Z-TTA."""

import numpy as np

from src.d10z_simulator import D10ZSystem
from src.analysis_tools import compute_energy_spectrum, stability_index


if __name__ == "__main__":
    system = D10ZSystem(initial_state=np.array([1.0, -0.5, 0.25]), coupling=0.8)
    result = system.run(time_span=1.0, dt=0.01)

    freq, power = compute_energy_spectrum(result.states)
    stability = stability_index(result.states)

    print("Tiempo final:", result.times[-1])
    print("Eventos registrados:", result.events)
    print("Índice de estabilidad:", stability)
    print("Frecuencias principales:", freq[:5])
    print("Potencia espectral:", power[:5])
