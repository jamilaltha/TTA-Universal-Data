"""Command line interface for the D10Z framework."""
import argparse
from pathlib import Path


def build_parser():
    parser = argparse.ArgumentParser(description="D10Z CLI")
    sub = parser.add_subparsers(dest="command")

    diag = sub.add_parser("diagram", help="Generate architecture diagram")
    diag.add_argument("--output", type=Path, default=Path("docs/architecture/diagram.txt"))

    sanity = sub.add_parser("sanity", help="Run dimensional sanity checks")
    sanity.add_argument("--module", default="d10z")

    return parser


def cmd_diagram(output: Path):
    from scripts import generate_architecture_diagram

    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as fh:
        fh.write(generate_architecture_diagram.main.__doc__ or "")
    # regenerate using stdout so CLI stays simple
    content = generate_architecture_diagram.main()
    if content is None:
        content = "See generated file for architecture overview."
    print(content)


def cmd_sanity(module: str):
    from scripts import dimensional_consistency

    report = dimensional_consistency.run_checks(module)
    print(report)


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "diagram":
        cmd_diagram(args.output)
    elif args.command == "sanity":
        cmd_sanity(args.module)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
