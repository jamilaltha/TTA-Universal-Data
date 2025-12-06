"""Ejemplo de pipeline empresarial utilizando el SDK."""

from d10z.sdk.client import D10ZClient


def main() -> None:
    client = D10ZClient.default()
    metrics = client.evaluate_sparc_sample(n_galaxies=50)
    print({"enterprise_score": metrics})


if __name__ == "__main__":
    main()
