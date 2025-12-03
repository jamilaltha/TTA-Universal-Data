"""Leyes de Sahana e Isis."""

import numpy as np


def compute_tension(Z: np.ndarray, C: np.ndarray) -> float:
    """Métrica de tensión (Ley de Isis).

    Calcula la desviación cuadrática entre cada nodo y la media ponderada
    por su conectividad.

    Parameters
    ----------
    Z : numpy.ndarray
        Vector complejo de nodos.
    C : numpy.ndarray
        Matriz de conectividad.

    Returns
    -------
    float
        Tensión total del sistema.
    """

    deg = C.sum(axis=1) + 1e-15
    Z_hat = (C @ Z) / deg
    return float(np.sum(np.abs(Z - Z_hat) ** 2))
