# PROTOCOLS: Procedimientos experimentales y de reproducibilidad

## Preparación numérica
1. Instalar dependencias desde `requirements.txt` en entorno aislado.
2. Ejecutar `examples/basic_simulation.py` para verificar integrador base.
3. Validar espectro energético con `analysis_tools.compute_energy_spectrum` y
   registrar resultados en `data/simulation_results/`.

## Protocolos de laboratorio
- **Efecto Hall**: medir plateaus en campos magnéticos crecientes, registrar
  desviaciones fraccionales y comparar con simulaciones Big Start.
- **Variación de \(\alpha\)**: emplear relojes ópticos estabilizados, aplicar
  compensación térmica sub-mK y muestrear en ventanas de 24 h.
- **Interferometría**: calibrar fase cero con vacío, introducir potencial
  efectivo equivalente \(|x|^{\alpha}\) mediante moduladores electro-ópticos.

## Adquisición y almacenamiento
- Guardar series temporales crudas en `data/experimental_data/` con metadatos
  de temperatura y calibración.
- Utilizar formatos `csv` o `hdf5` según el tamaño del dataset.
- Versionar configuraciones experimentales con etiquetas de fecha y órden
  fractal utilizado.

## Validación y reporte
1. Calcular índices de estabilidad y eventos críticos con los scripts de
   `examples/`.
2. Comparar observables con predicciones en `docs/PREDICTIONS.md`.
3. Publicar reportes reproducibles enlazando notebooks y resultados en el
   repositorio.
