# Computation Model

The computation model emphasizes determinism, composability, and capability isolation.

- **Determinism:** All arithmetic is 64-bit two's complement with explicit overflow rules. Gas charges are fixed per opcode.
- **Composability:** Programs are sequences of 8-byte codons that can be statically inspected for stack depth, memory growth, and host dependencies.
- **Capability isolation:** Host calls are declared up front and executed through namespaced capabilities to avoid ambient authority.

The VM offers eight general-purpose registers (R0–R7), a logical stack with tracked depth, and linear memory that grows in fixed pages when gas allows.
