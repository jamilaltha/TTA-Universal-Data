#  D10Z-TTA: Unified Nodal Fractal Dynamics Framework (Ignition Validated)

D10Z-TTA consolidates nodal fractal dynamics into a reproducible framework targeting ignition-grade stability. The current milestone delivers a validated ignition factor of \(\Phi \approx 1.05\) (``Big Start''), backed by an open Python simulator and LaTeX manuscript-ready paper. The repository is organized for rapid experimentation, manuscript generation, and archival of ignition search artifacts.

---

##  Características Clave

* **Ignition validation:** Stable ignition with \(\Phi \approx 1.05\) captured in the reference pipeline.
* **Reproducible codebase:** Python simulator with configurable parameters for nodal interactions and convergence.
* **Publication-ready LaTeX:** `latex/main.tex` hosts the paper converted from the ignition manuscript, ready for `pdflatex` or `xelatex`.
* **Data layout:** `data/` reserved for ignition results (e.g., `d10z_v3_results.pkl`, `ignition_search_results.pkl`).
* **Documentation:** Executive summary and master index live under `docs/` for quick navigation and review.
* **Next steps:** Integrate the full manuscript text, inject the executive summary, and align the simulator with the validated equations.

---

## Reproducción de la Validación de Ignición

Para reproducir la estabilidad de ignición, instale el paquete y ejecute el pipeline de referencia:

```python
# Asegúrese de haber instalado el paquete localmente: python -m pip install -e .

from d10z import PHI_IGNITION_TARGET
from d10z.simulators.reference_pipeline import run_reference_pipeline

# --- EJECUCIÓN DEL PIPELINE ---
results = run_reference_pipeline(N_nodes=127, steps=200)

print(f"Objetivo de Coherencia de Ignición (Φ): {PHI_IGNITION_TARGET}")
print(f"Coherencia Final Promedio (Φ): {results['coherence_final']:.4f}")
print(f"Validación de Ignición: {results['ignition_validated']}")
print(f"Tensión Estructural Final: {results['tension_final']:.6f}")

# Los resultados completos y el estado Z final se archivan en data/
