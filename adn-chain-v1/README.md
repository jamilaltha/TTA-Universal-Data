# ADN-Chain v1: Codon-Based Virtual Machine and Blockchain

ADN-Chain v1 es una plataforma de cómputo distribuido inspirada en biología.
Los programas se expresan en un ensamblador de codones (ISA-64) y se ejecutan
sobre una máquina virtual determinista con doble modelo (ADN-VM + CodonVM).
Los nodos intercambian bloques binarios en formato ADN-BLOCK v1 a través del
protocolo P2P ADN-Net v1.

## Estructura del repositorio

- `software/`
  - `adn_core/`: crate Rust con el lenguaje, bytecode, VMs y transpiler WASM.
  - `adn_node/`: crate Rust con el nodo ADN-Chain (estado, bloques, P2P, RPC, consenso).
- `docs/`
  - `whitepaper.tex`: whitepaper técnico oficial de ADN-Chain v1.
  - `book/`: documentación extendida en formato mdBook.
- `LICENSE`: MIT.
- `CITATION.cff`: metadatos de citación.
- `zenodo.json`: metadatos para Zenodo.
- `VERSION`: versión del release.

## Requisitos

- Rust (estable) y `cargo`.
- `mdbook` para la documentación en formato libro.
- LaTeX (pdflatex) para generar el whitepaper en PDF.

## Compilar los crates Rust

```bash
cd software/adn_core
# Cargo.toml se añadirá cuando se suba el código
cargo build
cargo test

cd ../adn_node
cargo build
cargo test
```

## Generar la documentación

### Whitepaper (PDF)

```bash
cd docs
pdflatex whitepaper.tex
```

### mdBook

```bash
cd docs/book
mdbook build
```

## Cómo citar

El DOI se añadirá tras publicar la versión en Zenodo. De forma provisional,
usar los metadatos en `CITATION.cff` y `zenodo.json`.

## Licencia

Este proyecto se distribuye bajo la licencia MIT.
