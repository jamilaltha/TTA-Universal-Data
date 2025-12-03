# D10Z-TTA (Universal Data)

Pipeline D10Z para evaluar integridad en sistemas distribuidos y medir fragmentación de corpus. Ahora se publica como paquete Python para instalación vía `pip install d10z` y con utilidades CLI listas para reproducir la ignición.

## Instalación rápida

```bash
pip install d10z
```

Para desarrollo local:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Uso básico

### Simulador de consenso

Ejecuta una simulación determinista del modelo D10Z:

```bash
python -m d10z.simulator consensus --nodes 30 --gamma 0.08 --alpha 0.6 --beta 1.2 --iterations 400
```

El comando imprime un resumen en JSON con integridad final, energía y estados nodales. También puedes invocar la entrada instalada como script:

```bash
d10z consensus --nodes 16 --seed 42
```

### Analizador multi-corpus

Calcula la conectividad y sugiere documentos puente para un corpus de ejemplo (`arxiv`, `github` o `medical`):

```bash
python -m d10z.simulator corpus --corpus github
```

La salida muestra λ₂ aproximado y las parejas de documentos sugeridas para mejorarla.

### Datos incluidos

El dataset de referencia `TTA_UNIVERSAL_V01.jsonl` se incluye en el paquete. Puedes obtener la ruta absoluta con:

```python
from d10z import data_path
path = data_path("TTA_UNIVERSAL_V01.jsonl")
```

## Documentación

Los documentos de diseño y ejemplos extendidos viven en [`docs/`](docs/README.md). Allí se describe cómo reproducir experimentos y cómo extender los modelos.

## Publicación en PyPI

1. Instala las herramientas de build y twine:
   ```bash
   pip install build twine
   ```
2. Genera las distribuciones desde la raíz del proyecto:
   ```bash
   python -m build
   ```
   Esto crea `dist/d10z-<versión>.tar.gz` y `dist/d10z-<versión>-py3-none-any.whl`.
3. Define las credenciales en `~/.pypirc` o variables de entorno y sube los artefactos:
   ```bash
   twine upload dist/*
   ```

## Contribuciones

- Las contribuciones deben mantener reproducibilidad científica y trazabilidad.
- Utiliza ramas dedicadas (p. ej. `feat/update-readme-license`) y abre un PR explicando los cambios.
- Antes de solicitar revisión, verifica que `python -m build` se ejecute sin errores.

## Licencia

El código se distribuye bajo la licencia MIT. Consulta [`LICENSE`](LICENSE) para los términos completos.
