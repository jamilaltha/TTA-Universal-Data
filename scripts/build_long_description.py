"""Build long description from README for packaging."""
from pathlib import Path


def main():
    readme = Path("README.md")
    if not readme.exists():
        print("README.md not found")
        return
    content = readme.read_text(encoding="utf-8")
    Path("build").mkdir(exist_ok=True)
    Path("build/desc.md").write_text(content, encoding="utf-8")
    print("Long description written to build/desc.md")


if __name__ == "__main__":
    main()
