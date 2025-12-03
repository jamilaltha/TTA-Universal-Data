"""Ignición de coherencia (Big Start)."""

import numpy as np

def big_start_phi(t, tau=1e-43):
    """Evolución de coherencia desde t=0 (Planck time).

    Parameters
    ----------
    t : float or array-like
        Tiempo transcurrido desde t=0.
    tau : float, optional
        Escala característica de relajación.

    Returns
    -------
    float or ndarray
        Valor de la función de coherencia.
    """
    t = np.asarray(t, dtype=float)
    return 1.0 - np.exp(-t / tau)
