# Security Model — TTA-Universal-Data

Este proyecto es principalmente científico, pero sigue buenas prácticas:

- No expone servicios de red por defecto.
- El código se ejecuta en entornos controlados del usuario.
- Las dependencias se auditan con:
  - bandit
  - pip-audit

Riesgos principales:
- Uso de datos externos sin validación explícita.
- Posible ejecución de código en notebooks (recomendación: entornos aislados).
