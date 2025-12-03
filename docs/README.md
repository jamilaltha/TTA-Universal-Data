# Documentación D10Z-TTA

## Contenido
- Descripción del modelo de consenso y parámetros (`gamma`, `alpha`, `beta`).
- Ejemplos de ejecución usando el CLI (`d10z consensus` y `d10z corpus`).
- Referencia del dataset `TTA_UNIVERSAL_V01.jsonl` incluido en `d10z/data`.
- Guía de publicación en PyPI y checklist de revisión.

## Reproducir la ignición
1. Instala el paquete en un entorno virtual.
2. Ejecuta `d10z consensus --nodes 24 --seed 7` para obtener la trayectoria de integridad.
3. Ejecuta `d10z corpus --corpus medical` y verifica las sugerencias de documentos puente.
4. Ajusta parámetros y guarda los JSON resultantes para tu experimento.

## Extensión

- Puedes cargar tus propios corpus creando listas de `Document` y usando `analyze` desde `d10z.corpus`.
- Para simulaciones personalizadas, instancia `ConsensusEngine` y ejecuta `step()` manualmente.

## Contacto

Abre un issue o PR en GitHub si encuentras discrepancias o quieres proponer mejoras.
