# Branching Strategy

- `main`: rama protegida, siempre en estado deployable.
- `feature/*`: nuevas funciones.
- `fix/*`: corrección de bugs.
- `release/*`: preparación de versiones públicas.

Reglas:
- Todo cambio a `main` entra vía Pull Request.
- CI obligatorio en verde.
