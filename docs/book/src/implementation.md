# Reference Implementation

The reference implementation is organized as two Rust crates:

- `adn_core`: ISA encoding/decoding, VM runtime, gas accounting, ABI, and crypto adapters.
- `adn_node`: P2P networking, consensus orchestration, storage, and node lifecycle management.

This repository currently contains the documentation and metadata scaffold; the Rust sources will be added in future releases and covered by the Rust CI workflow.
