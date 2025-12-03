"""Utilidades para energía y conteo de infifotones."""

from .constants import EPS_IFI

def infifoton_energy(n_ifis):
    """Calcula la energía total de infifotones."""
    return n_ifis * EPS_IFI
