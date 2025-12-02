# Consensus

The consensus interface supports pluggable algorithms. The reference design targets a partially synchronous environment with BFT rounds:

1. Leader selection via VRF outputs and validator weights.
2. Pre-vote and pre-commit phases with aggregate signatures.
3. Finality after `2f+1` signatures within a round.

Other consensus modules (e.g., probabilistic Nakamoto-style) can be integrated if they honor the same block validation and hashing rules.
