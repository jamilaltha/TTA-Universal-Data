from pathlib import Path

ROOTS = ["d10z", "docs", "examples", "notebooks", "scripts", "tests"]


def build_tree(root: Path, indent: str = "") -> str:
    lines = []
    children = sorted([p for p in root.iterdir() if p.name != "__pycache__"])
    for i, child in enumerate(children):
        connector = "└── " if i == len(children) - 1 else "├── "
        lines.append(f"{indent}{connector}{child.name}")
        if child.is_dir():
            extension = "    " if i == len(children) - 1 else "│   "
            lines.append(build_tree(child, indent + extension))
    return "\n".join(line for line in lines if line)


def main() -> str:
    """Generate an ASCII overview of the repository structure."""
    repo_root = Path(__file__).resolve().parent.parent
    output_lines = ["D10Z-TTA :: Architecture Diagram", "===============================", ""]
    for root_name in ROOTS:
        root_path = repo_root / root_name
        if root_path.exists():
            output_lines.append(root_name)
            tree = build_tree(root_path)
            if tree:
                output_lines.append(tree)
            output_lines.append("")
    output = "\n".join(output_lines).rstrip()
    print(output)
    return output


if __name__ == "__main__":
    main()
