# D10Z Package Skeleton

Implementación mínima del marco D10Z-TTA con constantes fundamentales, utilidades de Big Start, dinámica TTA y simuladores de fases.

## Estructura del paquete
- `d10z/` módulo raíz con constantes, Big Start, leyes y arquitectura TTA.
- `d10z/simulators/` simuladores de las fases 3 (2D y 3D) y fase 4 fractal.

## Instalación local

```bash
python -m pip install .
```

## Uso rápido

```python
from d10z import big_start_phi, sahana_dynamics, compute_tension
from d10z.simulators import run_phase3_2d
import numpy as np

# Evolución de coherencia
phi = big_start_phi(np.linspace(0, 1e-40, 5))

# Dinámica Sahana sobre conectividad aleatoria
C = np.eye(4)
Z0 = np.ones(4, dtype=complex)
Zf = sahana_dynamics(Z0, C)

# Métrica de tensión
T = compute_tension(Zf, C)

# Simulación fase 3 2D
result = run_phase3_2d(n_rows=4, n_cols=4, seed=123)
print(result["tension"])
```

## Simuladores
- `run_phase3_2d`: malla 2D periódica.
- `run_phase3b_3d`: retícula 3D periódica.
- `run_phase4_fractal`: topología jerárquica simplificada.

Cada función devuelve un diccionario con el estado final, la tensión calculada y la matriz de conectividad empleada.

## Publicación
Para construir y publicar el paquete:

```bash
python -m build
python -m twine upload dist/*
```
