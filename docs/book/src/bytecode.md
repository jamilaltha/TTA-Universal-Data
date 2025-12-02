# Bytecode

Bytecode is a little-endian stream of codons with a fixed module header:

1. Magic number `0x41444E31` ("ADN1").
2. Version `0x0001`.
3. Entrypoint offset.
4. Constant pool length and alignment.
5. Capability bitmap for host calls.

Sections follow in order: code, constant pool, debug metadata, and an optional signature block that binds the module hash to the author's key. All multi-byte fields use unsigned integers and little-endian encoding.
