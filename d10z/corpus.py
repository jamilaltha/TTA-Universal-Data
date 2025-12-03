"""Analysis utilities for the D10Z multi-corpus analyzer."""

from __future__ import annotations

from dataclasses import dataclass
from math import exp, sqrt
from typing import Dict, List, Tuple


@dataclass
class Document:
    id: str
    title: str
    z: float
    cluster: str


@dataclass
class Corpus:
    name: str
    description: str
    documents: List[Document]
    expected_lambda2: float
    fragmentation_level: str


DEFAULT_CORPORA: Dict[str, Corpus] = {
    "arxiv": Corpus(
        name="arXiv: Theory of Everything",
        description="Papers sobre teorías unificadas de física",
        documents=[
            Document("arxiv:2301.01234", "String Theory and Quantum Gravity", 0.72, "A"),
            Document("arxiv:2302.05678", "Loop Quantum Gravity Approach", 0.68, "B"),
            Document("arxiv:2303.09012", "M-Theory Compactifications", 0.75, "A"),
            Document("arxiv:2304.03456", "Causal Set Theory", 0.45, "C"),
            Document("arxiv:2305.07890", "Asymptotic Safety in Gravity", 0.52, "B"),
            Document("arxiv:2306.01122", "E8 Theory and Unification", 0.38, "D"),
            Document("arxiv:2307.04455", "Holographic Principle", 0.71, "A"),
            Document("arxiv:2308.08899", "Twistor Theory Applications", 0.49, "C"),
        ],
        expected_lambda2=0.042,
        fragmentation_level="CRÍTICA",
    ),
    "github": Corpus(
        name="GitHub: ML Frameworks",
        description="Repositorios de frameworks de Machine Learning",
        documents=[
            Document("tensorflow/tensorflow", "TensorFlow Core", 0.89, "A"),
            Document("pytorch/pytorch", "PyTorch Framework", 0.91, "A"),
            Document("keras-team/keras", "Keras High-level API", 0.82, "A"),
            Document("scikit-learn/scikit-learn", "Scikit-learn", 0.76, "B"),
            Document("jax/jax", "JAX Autodiff", 0.73, "A"),
            Document("microsoft/onnx", "ONNX Runtime", 0.68, "C"),
            Document("apache/mxnet", "Apache MXNet", 0.45, "D"),
            Document("chainer/chainer", "Chainer (deprecated)", 0.31, "D"),
        ],
        expected_lambda2=0.156,
        fragmentation_level="MODERADA",
    ),
    "medical": Corpus(
        name="Medical: Controversial Treatments",
        description="Literatura sobre tratamientos médicos controversiales",
        documents=[
            Document("pubmed:33445678", "Ivermectin for COVID-19: Meta-analysis", 0.62, "A"),
            Document("pubmed:34556789", "Ivermectin: No significant effect", 0.71, "B"),
            Document("pubmed:35667890", "Hydroxychloroquine efficacy study", 0.48, "A"),
            Document("pubmed:36778901", "HCQ: Negative results in RCT", 0.75, "B"),
            Document("pubmed:37889012", "Vitamin D supplementation outcomes", 0.58, "C"),
            Document("pubmed:38990123", "Homeopathy systematic review", 0.33, "D"),
            Document("pubmed:39001234", "Acupuncture pain management", 0.52, "C"),
            Document("pubmed:40112345", "Cannabinoids therapeutic potential", 0.64, "C"),
        ],
        expected_lambda2=0.028,
        fragmentation_level="EXTREMA",
    ),
}


def connectivity_matrix(documents: List[Document]) -> List[List[float]]:
    n = len(documents)
    matrix = [[0.0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            same_cluster = 1.0 if documents[i].cluster == documents[j].cluster else 0.1
            z_product = (documents[i].z * documents[j].z) ** 0.5
            semantic_distance = abs(documents[i].z - documents[j].z)
            c_ij = same_cluster * z_product * exp(-semantic_distance)
            matrix[i][j] = c_ij
            matrix[j][i] = c_ij
    return matrix


def laplacian(matrix: List[List[float]]) -> List[List[float]]:
    n = len(matrix)
    lap = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        degree = sum(matrix[i])
        lap[i][i] = degree
        for j in range(n):
            if i != j:
                lap[i][j] = -matrix[i][j]
    return lap


def approximate_lambda2(lap: List[List[float]]) -> float:
    n = len(lap)
    trace = sum(lap[i][i] for i in range(n))
    sum_squares = sum(val * val for row in lap for val in row)
    lambda2 = (trace - sqrt(max(0.0, trace * trace - 2 * sum_squares))) / max(1, n)
    return max(lambda2, 0.001)


def suggest_bridges(documents: List[Document], matrix: List[List[float]], target_lambda2: float) -> List[Tuple[str, str, float]]:
    suggestions: List[Tuple[str, str, float]] = []
    n = len(documents)

    for i in range(n):
        for j in range(i + 1, n):
            if documents[i].cluster == documents[j].cluster:
                continue
            gain = matrix[i][j] * 1.5
            suggestions.append((documents[i].id, documents[j].id, gain))

    suggestions.sort(key=lambda item: item[2], reverse=True)
    return suggestions[:5]


def analyze(corpus: Corpus) -> dict:
    matrix = connectivity_matrix(corpus.documents)
    lap = laplacian(matrix)
    lambda2 = approximate_lambda2(lap)
    bridges = suggest_bridges(corpus.documents, matrix, corpus.expected_lambda2)

    return {
        "lambda2": lambda2,
        "expected_lambda2": corpus.expected_lambda2,
        "fragmentation": corpus.fragmentation_level,
        "bridges": bridges,
    }
