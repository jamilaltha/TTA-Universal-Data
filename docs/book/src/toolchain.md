# Toolchain

Developers will interact with the toolchain through standard Rust workflows:

```bash
cargo build --workspace --all-targets
cargo test --workspace
```

Additional tools include `mdbook` for documentation and `pdflatex` for the LaTeX whitepaper. The `.github/workflows` directory wires CI to compile crates, run tests, and build documentation artifacts.
