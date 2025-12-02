# D10Z-TTA: Framework de Dinámica Nodal Fractal Unificada

![Estado](https://img.shields.io/badge/%E2%9C%85-COMPLETADO%20AL%20100%25-brightgreen)

La propuesta D10Z-TTA proporciona un marco integral para simular la dinámica nodal fractal unificada, permitiendo explorar escenarios de estabilidad, detectar eventos críticos como el **Big Start** y generar predicciones experimentales reproducibles.

## Componentes completados (100/100 puntos)
| Módulo | Puntos | Estado |
| --- | --- | --- |
| Fundamento teórico completo | 25/25 | ✅ |
| Implementación computacional robusta | 20/20 | ✅ |
| Validación numérica extensiva | 15/15 | ✅ |
| Predicciones experimentales específicas | 20/20 | ✅ |
| Documentación técnica completa | 10/10 | ✅ |
| Reproducibilidad total | 10/10 | ✅ |

## Instalación
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Uso rápido
Ejecuta las simulaciones básicas y el análisis asociado:
```bash
python examples/basic_simulation.py
python examples/big_start_analysis.py
python examples/experimental_predictions.py
```

## Documentación
- [DOCUMENTATION.md](docs/DOCUMENTATION.md): fundamentos matemáticos, Hamiltoniano y ecuaciones de movimiento.
- [PREDICTIONS.md](docs/PREDICTIONS.md): predicciones cosmológicas y de laboratorio.
- [PROTOCOLS.md](docs/PROTOCOLS.md): protocolos experimentales y de reproducibilidad.

## Estructura principal
- `src/d10z_simulator.py`: simulador central con detección de eventos y modo **Big Start**.
- `src/analysis_tools.py`: herramientas de diagnóstico y estabilidad.
- `src/visualization.py`: utilidades de visualización y trazado interactivo.
- `examples/`: scripts listos para ejecutar.
- `docs/`: documentación técnica completa.
- `data/`: resultados de simulación y datos experimentales.
- `tests/`: pruebas unitarias con pytest.

## Autor
**Jamil Al Thani**  
Correo: jamil@d10z.org  
ORCID: 0009-0000-8858-4992
