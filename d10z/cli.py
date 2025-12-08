import argparse
import json

from d10z.sdk.client import D10ZClient


def main() -> None:
    parser = argparse.ArgumentParser(prog="d10z", description="CLI para D10Z-TTA")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("rotation-demo", help="Ejecuta demo de curva de rotación")

    eval_sparc = sub.add_parser("eval-sparc", help="Evalúa modelo en SPARC")
    eval_sparc.add_argument("--n", type=int, default=20, help="Número de galaxias")

    args = parser.parse_args()
    client = D10ZClient.default()

    if args.cmd == "rotation-demo":
        out = client.run_rotation_curve_demo()
        print(json.dumps(out, indent=2))
    elif args.cmd == "eval-sparc":
        r2 = client.evaluate_sparc_sample(n_galaxies=args.n)
        print(json.dumps({"r2": r2}, indent=2))


if __name__ == "__main__":
    main()
