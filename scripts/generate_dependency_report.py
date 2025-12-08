"""Generate dependency report from requirements files."""
from pathlib import Path


def main():
    print("# Dependency Report")
    requirements = list(Path.cwd().glob("requirements*.txt"))
    if not requirements:
        print("No requirements files found.")
        return
    for req_file in requirements:
        print(f"## {req_file}")
        for line in req_file.read_text().splitlines():
            if line.strip():
                print(f"- {line}")
        print()


if __name__ == "__main__":
    main()
