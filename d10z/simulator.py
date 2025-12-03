"""Command-line entry point for D10Z simulations."""

from __future__ import annotations

import argparse
import json
from typing import Any

from .consensus import ConsensusEngine
from .corpus import DEFAULT_CORPORA, analyze


def run_consensus(args: argparse.Namespace) -> dict[str, Any]:
    engine = ConsensusEngine(
        n=args.nodes, gamma=args.gamma, alpha=args.alpha, beta=args.beta, seed=args.seed
    )
    metrics = engine.run(max_iterations=args.iterations, tolerance=args.tolerance)
    return {
        "iterations": engine.iteration,
        "final_integrity": metrics["integrity"],
        "final_energy": metrics["energy"],
        "z": metrics["z"],
    }


def run_corpus(args: argparse.Namespace) -> dict[str, Any]:
    corpus = DEFAULT_CORPORA[args.corpus]
    analysis = analyze(corpus)
    return {
        "corpus": corpus.name,
        "lambda2": analysis["lambda2"],
        "expected": analysis["expected_lambda2"],
        "bridges": analysis["bridges"],
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="D10Z-TTA simulation toolkit")
    subparsers = parser.add_subparsers(dest="command", required=True)

    consensus_parser = subparsers.add_parser(
        "consensus", help="Ejecuta el simulador de consenso"
    )
    consensus_parser.add_argument("--nodes", type=int, default=20, help="Número de nodos")
    consensus_parser.add_argument("--gamma", type=float, default=0.1, help="Tasa gamma")
    consensus_parser.add_argument("--alpha", type=float, default=0.5, help="Parámetro alpha")
    consensus_parser.add_argument("--beta", type=float, default=1.0, help="Parámetro beta")
    consensus_parser.add_argument("--tolerance", type=float, default=1e-5, help="Tolerancia de integridad")
    consensus_parser.add_argument("--iterations", type=int, default=500, help="Iteraciones máximas")
    consensus_parser.add_argument("--seed", type=int, default=None, help="Semilla aleatoria")
    consensus_parser.set_defaults(func=run_consensus)

    corpus_parser = subparsers.add_parser(
        "corpus", help="Evalúa un corpus de ejemplo y genera documentos puente"
    )
    corpus_parser.add_argument(
        "--corpus",
        choices=sorted(DEFAULT_CORPORA.keys()),
        default="arxiv",
        help="Nombre del corpus de referencia",
    )
    corpus_parser.set_defaults(func=run_corpus)

    return parser


def main(argv: list[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    result = args.func(args)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
