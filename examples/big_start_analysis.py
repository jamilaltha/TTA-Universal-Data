"""Ejemplo de análisis con el modo Big Start del framework D10Z-TTA."""

import numpy as np

from src.d10z_simulator import D10ZBigStartSystem
from src.analysis_tools import summarize_events, compute_observables


if __name__ == "__main__":
    system = D10ZBigStartSystem(initial_state=np.array([2.0, -1.0]), coupling=1.2, big_start_factor=5.0)
    result = system.run(time_span=0.5, dt=0.005)

    print("Eventos Big Start:")
    for event in summarize_events(result):
        print(" -", event)

    metrics = compute_observables(result.states)
    print("Observables:", metrics)
