"""Ejemplo que enlaza predicciones con protocolos experimentales."""

import json
import numpy as np

from src.d10z_simulator import D10ZSystem
from src.analysis_tools import compute_energy_spectrum


if __name__ == "__main__":
    # Simulación corta para estimar observables relacionados con predicciones
    system = D10ZSystem(initial_state=np.array([0.8, 0.4]), coupling=0.9, fractal_order=1.7)
    result = system.run(time_span=0.25, dt=0.002)

    freq, power = compute_energy_spectrum(result.states, fs=1 / 0.002)
    prediction_payload = {
        "cmb_window_hz": [float(f) for f in freq[:10]],
        "spectral_density": [float(p) for p in power[:10]],
        "events": result.events,
    }

    print(json.dumps(prediction_payload, indent=2))
