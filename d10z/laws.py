"""Leyes de Sahana e Isis."""

import numpy as np

def compute_tension(Z, C):
    """Métrica de tensión (Ley de Isis).

    Parameters
    ----------
    Z : array-like
        Vector complejo de nodos.
    C : array-like
        Matriz de conectividad.

    Returns
    -------
    float
        Tensión total del sistema.
    """
    Z = np.asarray(Z, dtype=complex)
    C = np.asarray(C, dtype=float)
    deg = C.sum(axis=1) + 1e-15
    Z_hat = (C @ Z) / deg
    return float(np.sum(np.abs(Z - Z_hat) ** 2))
