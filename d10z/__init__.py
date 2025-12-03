"""D10Z-TTA toolkit for consensus simulations and corpus analysis."""

from importlib.resources import files

__all__ = [
    "__version__",
    "data_path",
]

__version__ = "0.1.0"

def data_path(filename: str) -> str:
    """Return the absolute path to a data asset shipped with the package.

    Parameters
    ----------
    filename: str
        Name of the file inside ``d10z/data``.
    """

    return str(files(__package__ + ".data").joinpath(filename))
