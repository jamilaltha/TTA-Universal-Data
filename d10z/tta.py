"""Temporal Tensorial Architecture (TTA) primitives."""

import numpy as np


def sahana_dynamics(Z: np.ndarray, C: np.ndarray, gamma: float = 0.02, steps: int = 3000):
    """Simulación básica de la dinámica de Sahana.

    Evolución iterativa Z_{n+1} = Z_n - γ(Z_n - Ẑ_n).

    Parameters
    ----------
    Z : numpy.ndarray
        Vector complejo de nodos (1D).
    C : numpy.ndarray
        Matriz de conectividad (2D, cuadrada) donde C[i, j] indica el
        acoplamiento entre nodos i y j.
    gamma : float, optional
        Paso de relajación (γ). Valores pequeños suavizan la evolución.
    steps : int, optional
        Número de iteraciones.

    Returns
    -------
    numpy.ndarray
        Estado final de los nodos tras la simulación.
    """

    Z_t = Z.astype(complex)
    for _ in range(int(steps)):
        deg = C.sum(axis=1) + 1e-15
        Z_hat = (C @ Z_t) / deg
        Z_t = Z_t - gamma * (Z_t - Z_hat)
    return Z_t
