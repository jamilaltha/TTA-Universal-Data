"""Extract inline equations from docstrings and comments."""
import ast
from pathlib import Path

TARGET_MARKERS = ["EQUATION", "Eq.", "Equation"]


def find_equations_in_file(path: Path):
    equations = []
    text = path.read_text(encoding="utf-8")
    for line in text.splitlines():
        if any(marker in line for marker in TARGET_MARKERS):
            equations.append(line.strip())
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return equations
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and ast.get_docstring(node):
            doc = ast.get_docstring(node)
            for doc_line in doc.splitlines():
                if any(marker in doc_line for marker in TARGET_MARKERS):
                    equations.append(doc_line.strip())
    return equations


def main():
    repo_root = Path(__file__).resolve().parent.parent
    python_files = list(repo_root.glob("**/*.py"))
    output = ["# Extracted Equations", ""]
    for path in sorted(python_files):
        if "__pycache__" in path.parts:
            continue
        equations = find_equations_in_file(path)
        if not equations:
            continue
        output.append(f"## {path.relative_to(repo_root)}")
        output.extend([f"- {eq}" for eq in equations])
        output.append("")
    print("\n".join(output).rstrip())


if __name__ == "__main__":
    main()
