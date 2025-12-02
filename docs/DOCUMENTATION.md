# DOCUMENTATION: D10Z-TTA Framework

## Fundamentos matemáticos
El framework D10Z-TTA modela la dinámica nodal mediante un potencial fractal
\(V(\mathbf{x}) = \lambda \sum_i |x_i|^{\alpha}\) que conserva simetrías
de auto-similitud y acoplamiento nodal. El espacio de fase se propaga bajo
transformaciones que preservan la métrica nodal \(\mathcal{G}\) y un flujo
hamiltoniano efectivo.

## Derivación del Hamiltoniano
El Hamiltoniano efectivo se construye como
\[\mathcal{H}(\mathbf{x}, \mathbf{p}) = \frac{1}{2}\|\mathbf{p}\|^2 + \lambda \sum_i |x_i|^{\alpha}\]
donde \(\mathbf{p}\) incorpora el impulso nodal y \(\alpha\) define el orden
fractal. La cuantificación semiclasica permite ajustar \(\lambda\) para
recuperar espectros discretos observables en entornos cosmológicos y de
laboratorio.

## Ecuaciones de movimiento
A partir de \nabla_{\mathbf{p}} \mathcal{H} y \nabla_{\mathbf{x}} \mathcal{H} se obtienen
las ecuaciones de movimiento
\[\dot{\mathbf{x}} = \mathbf{p}, \quad \dot{\mathbf{p}} = -\lambda\,\alpha\, \mathrm{sgn}(\mathbf{x}) |\mathbf{x}|^{\alpha-1}\]
que se integran numéricamente con esquemas explícitos adaptados al orden
fractal \(\alpha\). El modo **Big Start** introduce un factor exponencial de
arranque para explorar regímenes altamente energéticos.

## Análisis de estabilidad
La estabilidad se evalúa mediante:
- Índice de estabilidad \(S = e^{-\sigma^2}(1+\|x\|)^{-1}\) calculado sobre
  la varianza \(\sigma^2\) y la norma media.
- Espectros de potencia para detectar resonancias nodales.
- Detección automática de eventos críticos (energía y amplitud) con registro
de tiempo.

## Interfaz de código
- `D10ZSystem`: integración base con umbrales de evento configurables.
- `D10ZBigStartSystem`: versión con arranque amplificado y detección de Big Start.
- `analysis_tools`: espectros, índices de estabilidad y observables básicos.
- `visualization`: trazado temporal y espacio de fases.
