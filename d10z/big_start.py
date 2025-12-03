"""Big Start (ignición de coherencia) helpers."""

import numpy as np


def big_start_phi(t, tau: float = 1e-43):
    """Evolución de coherencia desde t=0 (Planck time).

    Parameters
    ----------
    t : float or array-like
        Tiempo (en segundos) a evaluar desde el arranque.
    tau : float, optional
        Escala de relajación, por defecto 1e-43.

    Returns
    -------
    numpy.ndarray or float
        Coherencia acumulada 1 - exp(-t / tau).
    """

    return 1.0 - np.exp(-np.asarray(t) / tau)
