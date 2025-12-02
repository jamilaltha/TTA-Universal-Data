# Cryptography

- **Hashing:** BLAKE3 for commitments and block hashing.
- **Signatures:** Ed25519 for transactions; Ed25519 multisig or BLS12-381 for committee aggregation.
- **Randomness:** Validator-supplied VRF outputs aggregated into unbiased beacons.

All primitives are versioned and feature-gated to permit upgrades without breaking determinism.
