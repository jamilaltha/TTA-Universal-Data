import numpy as np

from src.d10z_simulator import D10ZSystem, D10ZBigStartSystem


def test_basic_run_records_states():
    system = D10ZSystem(initial_state=np.array([1.0, -1.0]), coupling=0.5, event_threshold=1e6)
    result = system.run(time_span=0.1, dt=0.01)

    assert result.states.shape[0] == len(result.times)
    assert result.states.shape[1] == 2


def test_big_start_detects_event():
    system = D10ZBigStartSystem(initial_state=np.array([5.0, 5.0]), event_threshold=1.0, big_start_factor=10.0)
    result = system.run(time_span=0.05, dt=0.01)

    assert any("Big Start" in msg for _, msg in result.events)
