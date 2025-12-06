from pathlib import Path

ROOTS = ["d10z", "docs", "examples", "notebooks", "scripts", "tests"]


def iter_edges(root: Path, parent_label: str = None):
    for child in sorted([p for p in root.iterdir() if p.name != "__pycache__"]):
        child_label = child.relative_to(root.parent)
        yield (parent_label, child_label)
        if child.is_dir():
            yield from iter_edges(child, child_label)


def main():
    repo_root = Path(__file__).resolve().parent.parent
    print("digraph architecture {")
    print("    node [shape=box, fontname=Helvetica];")
    for root_name in ROOTS:
        root_path = repo_root / root_name
        if not root_path.exists():
            continue
        root_label = root_path.name
        print(f"    \"{root_label}\" [style=filled, fillcolor=lightgray];")
        for parent, child in iter_edges(root_path, root_label):
            if parent is None:
                continue
            print(f"    \"{parent}\" -> \"{child}\";")
    print("}")


if __name__ == "__main__":
    main()
