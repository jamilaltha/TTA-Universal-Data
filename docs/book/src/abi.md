# ABI

The ABI is minimal and deterministic:

- Scalars are 64-bit little-endian.
- Dynamic values are length-prefixed byte arrays.
- Structs are serialized in declaration order without padding.
- Capability identifiers are stable integers negotiated at deployment.

Contracts declare the capabilities they require; nodes enforce the declaration before execution. Receipts include encoded return values and emitted logs.
