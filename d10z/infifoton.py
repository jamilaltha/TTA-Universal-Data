"""Utilidades relacionadas con el infifotón."""

from .constants import EPS_IFI


def infifoton_energy(n_ifis: float) -> float:
    """Calcula la energía asociada a un número de infifotones."""

    return float(n_ifis) * EPS_IFI
