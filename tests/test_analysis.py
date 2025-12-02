import numpy as np

from src.analysis_tools import compute_energy_spectrum, stability_index, compute_observables


def test_energy_spectrum_outputs_frequency_and_power():
    states = np.array([[1.0, -1.0], [0.5, -0.5], [0.25, -0.25], [0.0, 0.0]])
    freq, power = compute_energy_spectrum(states, fs=10.0)

    assert freq.shape == power.shape
    assert freq[0] >= 0


def test_stability_index_with_reasonable_range():
    states = np.random.randn(20, 3)
    idx = stability_index(states)

    assert 0 <= idx <= 1


def test_compute_observables_returns_keys():
    states = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)
    obs = compute_observables(states)

    for key in {"media", "desviacion", "maximo", "minimo"}:
        assert key in obs
