"""Ejemplo simplificado de entrenamiento ML con el modelo TTA."""

from d10z.sdk.client import D10ZClient


def main() -> None:
    client = D10ZClient.default()
    demo = client.run_rotation_curve_demo()
    print("Datos simulados para entrenamiento:")
    print(demo)


if __name__ == "__main__":
    main()
