"""Temporal Tensorial Architecture (TTA) dynamics."""

import numpy as np

def sahana_dynamics(Z, C, gamma=0.02, steps=3000):
    """
    Simulación básica de la dinámica de Sahana: Z_{n+1} = Z_n - γ(Z_n - Ẑ_n).

    Parameters
    ----------
    Z : array-like
        Vector complejo de nodos inicial.
    C : array-like
        Matriz de conectividad (real) de NxN.
    gamma : float, optional
        Tasa de acoplamiento.
    steps : int, optional
        Iteraciones de la dinámica.

    Returns
    -------
    ndarray
        Estado final complejo de los nodos.
    """
    Z_t = np.asarray(Z, dtype=complex)
    C = np.asarray(C, dtype=float)
    for _ in range(int(steps)):
        deg = C.sum(axis=1) + 1e-15
        Z_hat = (C @ Z_t) / deg
        Z_t = Z_t - gamma * (Z_t - Z_hat)
    return Z_t
