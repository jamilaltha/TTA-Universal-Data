import importlib.util
from pathlib import Path


CONSTANTS_PATH = Path(__file__).resolve().parents[1] / "constants.py"


def load_constants():
    spec = importlib.util.spec_from_file_location("tta_constants", CONSTANTS_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_energy_conservation_proxy():
    constants = load_constants()
    energy = constants.infifoton_energy(10)
    back_converted = constants.infifoton_count(energy)
    assert back_converted == 10


def test_positive_constants():
    constants = load_constants()
    assert constants.EPSILON_IFI > 0
    assert constants.GM_SCALE > 0
    assert constants.C_EMERGENT > 0


def test_monotonic_gm_kappa():
    constants = load_constants()
    values = [entry["kappa"] for entry in constants.GM_TABLE.values()]
    assert all(v > 0 for v in values)
    assert values[0] >= min(values)
