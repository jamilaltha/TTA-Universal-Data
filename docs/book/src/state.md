# State and Transactions

Transactions include sender, nonce, gas limit, fee parameters, capability bitmap, and payload (deployment bytecode or an ABI call). The global state is a sparse key–value store committed via Merkle roots. `READ_STATE` and `WRITE_STATE` operate on byte arrays and consume gas relative to payload size.

Receipts record status, gas used, logs, and state proofs to enable light-client verification.
