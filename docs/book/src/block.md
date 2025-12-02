# Blocks

Block headers contain the parent hash, state root, receipts root, timestamp, randomness beacon, and validator set digest. Bodies carry ordered transactions and optional blob data. Signature sections support aggregate BLS or Ed25519 multisignatures depending on the consensus module.

Validity rules combine structural checks, state transition verification, and consensus proof validation. Merkle proofs enable inclusion verification for transactions and receipts.
