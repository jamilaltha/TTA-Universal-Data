# Virtual Machine

Execution proceeds through a fetch–decode–execute loop with pre-paid gas per instruction. Memory growth charges gas proportional to pages. Host calls marshal inputs and outputs through a canonical ABI using little-endian scalars and length-prefixed byte arrays.

Termination occurs when the entrypoint returns, a `TRAP` is executed, or gas is exhausted. Non-deterministic host features (time, random hardware, syscalls) are excluded; randomness is only delivered through consensus-provided VRF outputs.
