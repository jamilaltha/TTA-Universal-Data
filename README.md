# ADN-Chain v1

ADN-Chain v1 is a codon-inspired blockchain architecture that unifies a compact 64-bit instruction set architecture (ISA-64), a deterministic virtual machine, a bytecode toolchain, and a peer-to-peer network for verifiable distributed computation. This repository is the official scientific and technical archive for the ADN-Chain v1 specification, reference documentation, and supporting metadata.

## Project scope
- **ISA-64**: A 64-bit codon-based instruction set optimized for deterministic execution and compact encoding.
- **Virtual Machine**: A stack-and-register hybrid VM that enforces gas accounting, capability isolation, and deterministic host calls.
- **Bytecode & ABI**: A canonical binary format with stable ABI rules for contracts, transactions, and state transitions.
- **Block & Consensus**: A block format with Merkleized receipts and a modular consensus interface suitable for BFT or probabilistic protocols.
- **Networking**: A lightweight P2P protocol for block and state propagation, validator discovery, and capability negotiation.
- **Toolchain**: Rust crates for `adn_core` (VM, ISA, execution) and `adn_node` (networking, consensus, orchestration) that will be published in this repository.

## Repository layout
```
software/
  adn_core/   # Rust crate placeholder for the VM, ISA, and execution engine
  adn_node/   # Rust crate placeholder for networking, consensus, and orchestration

docs/
  whitepaper.tex    # LaTeX whitepaper describing ADN-Chain v1 end-to-end
  book/             # mdBook source with chaptered documentation

.github/workflows/  # CI for Rust crates and documentation builds
LICENSE             # MIT license
CITATION.cff        # Citation metadata
zenodo.json         # Zenodo deposition metadata
VERSION             # Repository version tag (1.0.0)
```

## Building the Rust crates
Rust source code will be uploaded to `software/adn_core` and `software/adn_node`. Once available:
1. Install Rust via [rustup](https://rustup.rs/).
2. From the repository root run:
   ```bash
   cargo build --workspace --all-targets
   cargo test --workspace
   ```
   The workspace manifests in each crate will coordinate shared dependencies for the VM, networking, and consensus components.

## Documentation
### Whitepaper (LaTeX)
The formal specification is provided in `docs/whitepaper.tex`. To build the PDF:
```bash
cd docs
pdflatex whitepaper.tex
```
Repeat `pdflatex` until cross-references stabilize.

### mdBook
An mdBook edition of the specification is located in `docs/book`.
```bash
cd docs/book
mdbook build
```
The rendered book will appear in `docs/book/book/` (ignored in git).

## Citation
If you use this work, please cite it using the metadata in `CITATION.cff`:
```
Al Thani, Jamil. "ADN-Chain v1: Codon-Based Virtual Machine and Blockchain System." Version 1.0.0, 2025. MIT License. ORCID: https://orcid.org/0009-0000-8858-4992.
```

## Status
This scaffold provides the full documentation toolchain, metadata, and CI required to publish ADN-Chain v1. Rust implementation crates will be added to `software/adn_core` and `software/adn_node` in subsequent commits.
