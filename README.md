# D10Z-TTA: Unified Nodal Fractal Dynamics Framework (Ignition Validated)

D10Z-TTA consolidates nodal fractal dynamics into a reproducible framework targeting ignition-grade stability. The current milestone delivers a validated ignition factor of \(\Phi \approx 1.05\) (``Big Start''), backed by an open Python simulator and LaTeX manuscript-ready paper. The repository is organized for rapid experimentation, manuscript generation, and archival of ignition search artifacts.

- **Ignition validation:** Stable ignition with \(\Phi \approx 1.05\) captured in the reference pipeline.
- **Reproducible codebase:** Python simulator with configurable parameters for nodal interactions and convergence.
- **Publication-ready LaTeX:** `latex/main.tex` hosts the paper converted from the ignition manuscript, ready for `pdflatex` or `xelatex`.
- **Data layout:** `data/` reserved for ignition results (e.g., `d10z_v3_results.pkl`, `ignition_search_results.pkl`).
- **Documentation:** Executive summary and master index live under `docs/` for quick navigation and review.
- **Next steps:** Integrate the full manuscript text, inject the executive summary, and align the simulator with the validated equations.

Clone, install `requirements.txt`, and run the simulator to reproduce the ignition dynamics. Contributions should preserve scientific reproducibility and keep ignition metrics front-and-center.
