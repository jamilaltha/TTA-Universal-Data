"""Utilidades de unidades físicas (esqueleto)."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Unit:
    name: str
    dimension: str


UNIT_TABLE: dict[str, Unit] = {
    "km": Unit(name="km", dimension="L"),
    "m": Unit(name="m", dimension="L"),
    "s": Unit(name="s", dimension="T"),
    "kg": Unit(name="kg", dimension="M"),
    "km/s": Unit(name="km/s", dimension="L T-1"),
}


def is_supported(unit: str) -> bool:
    return unit in UNIT_TABLE
