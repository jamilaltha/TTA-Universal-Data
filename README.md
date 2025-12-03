# D10Z Framework

Paquete Python que implementa el núcleo del marco D10Z: constantes fundamentales, ignición de coherencia (Big Start), arquitectura TTA y simuladores de fases. Está pensado para experimentación rápida y publicación en PyPI.

## Instalación local

```bash
python -m pip install .
```

## Uso rápido

```python
import numpy as np
from d10z import big_start_phi, sahana_dynamics, compute_tension
from d10z.simulators import run_phase3_2d

# Evolución de coherencia
phi = big_start_phi(1e-44)

# Dinámica TTA con conectividad simple
C = np.array([[0, 1], [1, 0]], dtype=float)
Z0 = np.array([1 + 0j, 0.2j])
Zf = sahana_dynamics(Z0, C, gamma=0.05, steps=500)
print("Tensión:", compute_tension(Zf, C))

# Simulación lista para fase 3 (2D)
resultado = run_phase3_2d(size=6, steps=500)
print("Tensión final fase 3:", resultado["tension"])
```

## Módulos principales

- `d10z/constants.py`: constantes ETA_GM, EPS_IFI, ALPHA, BETA y LAMBDA.
- `d10z/big_start.py`: ignición de coherencia `big_start_phi`.
- `d10z/tta.py`: dinámica de Sahana mediante `sahana_dynamics`.
- `d10z/laws.py`: métrica de tensión `compute_tension` (Ley de Isis).
- `d10z/infifoton.py`: utilidades de energía infifotónica.
- `d10z/simulators/`: simuladores de fases 3 y 4 listos para ejecutar.

## Publicación en PyPI

1. Construye el paquete: `python -m build`
2. Publica: `python -m twine upload dist/*`

## Secciones heredadas del repositorio

Plantillas APA, Chicago y BibTeX disponibles en: **Citing the Dataset** (Wiki)

---

##  Contribuciones

Las contribuciones están reguladas para garantizar reproducibilidad científica. Revisión estricta antes de aceptar PRs.

Normas completas: **Contributing Guidelines** (Wiki)

---

##  Roadmap

Próximas etapas:

- v0.2.0 — Expansión multi-dominio
- v1.0.0 — Dataset científico consolidado
- Integración completamente automática con Zenodo
- Validaciones extendidas por dominio
- Preparación para versiones shard para IA

Documento completo en: **Roadmap** (Wiki)

---

##  Licencia

Este repositorio está bajo licencia **MIT**, salvo las fuentes externas, que conservan sus licencias originales.

---

##  Estado actual

- Dataset v0.1.0 validado
- Wiki documentada completamente
- Estructura formal establecida
- Preparado para Zenodo y releases científicos
