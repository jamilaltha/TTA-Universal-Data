"""Lightweight dimensional consistency checker for D10Z artifacts."""
from importlib import import_module
from pathlib import Path
from typing import Dict, List
import json

PHYSICAL_LOWER_BOUNDS = {
    "EPSILON_IFI": 0,
    "GM_SCALE": 0,
    "PHI_MIN": 0,
    "PHI_CRITICAL": 0,
    "PHI_IGNITION": 0,
    "GAMMA_SAHANA": 0,
    "FILAMENT_THICKNESS": 0,
    "FILAMENT_SEPARATION": 0,
    "C_EMERGENT": 0,
    "HBAR_EMERGENT": 0,
    "G_EMERGENT": 0,
    "KB_EMERGENT": 0,
}


class ConsistencyReport:
    def __init__(self):
        self.entries: List[str] = []
        self.issues: List[str] = []

    def add(self, message: str):
        self.entries.append(message)

    def warn(self, message: str):
        self.issues.append(message)

    def as_text(self) -> str:
        header = "D10Z Dimensional Consistency Report"
        body = "\n".join(self.entries or ["No checks executed."])
        footer = "\n".join(self.issues) if self.issues else "All checks passed."
        return f"{header}\n{'=' * len(header)}\n{body}\n\n{footer}"


def check_module_constants(module_name: str, report: ConsistencyReport):
    module = import_module(module_name)
    for name, lower_bound in PHYSICAL_LOWER_BOUNDS.items():
        if hasattr(module, name):
            value = getattr(module, name)
            if value is None:
                report.warn(f"{name} is undefined in {module_name}")
                continue
            if value <= lower_bound:
                report.warn(f"{name}={value} violates lower bound > {lower_bound}")
            else:
                report.add(f"{module_name}.{name} within physical bounds: {value}")
        else:
            report.warn(f"{module_name} missing expected constant: {name}")


def check_gm_table(module_name: str, report: ConsistencyReport):
    module = import_module(module_name)
    gm_table = getattr(module, "GM_TABLE", {})
    for scale, params in gm_table.items():
        if params.get("kappa", 1) <= 0:
            report.warn(f"GM_TABLE[{scale}] has non-physical kappa: {params.get('kappa')}")
        else:
            report.add(f"GM_TABLE[{scale}] kappa positive: {params.get('kappa')}")


def run_checks(module_name: str = "constants") -> str:
    report = ConsistencyReport()
    try:
        check_module_constants(module_name, report)
        check_gm_table(module_name, report)
    except ModuleNotFoundError as exc:
        report.warn(f"Module {module_name} not found: {exc}")
    return report.as_text()


if __name__ == "__main__":
    print(run_checks())
