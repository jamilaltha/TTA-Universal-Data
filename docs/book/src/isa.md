# ISA-64

Each instruction encodes into 64 bits: 8-bit opcode, 8-bit flags, and 48 bits for operands or immediates. Instruction categories include:

- **Arithmetic:** `ADD`, `SUB`, `MUL`, `DIV`, `MOD`, with saturating and wrapping variants.
- **Logic:** Bitwise ops plus rotates and shifts.
- **Control:** `JMP`, `JZ`, `JNZ`, `CALL`, `RET`, and `TRAP`.
- **Stack:** `PUSH`, `POP`, `DUP`, `SWAP` with depth validation.
- **Memory:** `LD`, `ST`, `LDB`, `STB`, and `MEMSZ` for querying heap size.
- **Crypto:** `HASH` (BLAKE3), `SIGVERIFY` (Ed25519), `RAND` (consensus-provided VRF output).
- **Context:** `GET_TX_FIELD`, `GET_BLOCK_FIELD`, `READ_STATE`, `WRITE_STATE` for deterministic access to blockchain data.

Reserved opcodes keep space for forward-compatible extensions. Illegal or unassigned opcodes trap deterministically.
