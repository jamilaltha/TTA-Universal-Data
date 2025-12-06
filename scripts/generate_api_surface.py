from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parent.parent / "d10z"


def discover_modules():
    modules = []
    for path in PACKAGE_ROOT.rglob("*.py"):
        if "__pycache__" in path.parts:
            continue
        if path.name == "__init__.py":
            continue
        relative = path.relative_to(PACKAGE_ROOT).with_suffix("")
        modules.append("d10z." + ".".join(relative.parts))
    return sorted(modules)


def main():
    modules = discover_modules()
    lines = ["\"\"\"Public API surface for d10z. Auto-generated.\"\"\"", "", "__all__ = ["]
    for module in modules:
        alias = module.split(".")[-1]
        lines.append(f"    '{alias}',")
    lines.append("]")
    lines.append("")
    for module in modules:
        alias = module.split(".")[-1]
        lines.append(f"from {module} import *  # noqa: F401,F403")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
